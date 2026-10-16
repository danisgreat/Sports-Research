"""Model-learning counters and evidence-aware review triggers (Improvements 21–23, 27).

Counts are derived from verified artifacts, never typed in:

    unique_settled_games     events with a reviewed FINAL result in the learning store
    ml_admissible_games      distinct events admitted to any verified training release
    frozen_model_forecasts   distinct events with a hash-verified primary bundle (V2/V3 receipts)
    hedge_feedback_games     distinct events with a full-information feedback row from ``primary settle``
    prospective_eval_games   distinct events with PRE_START_VERIFIED shadow rows and a settled WIN/LOSS outcome

Review clocks run per scope (ALL, each sport, each competition) and level. Defaults: INTERIM after ~100 newly
settled unique games (ALL), COMPREHENSIVE after ~300 (ALL), SPORT after 100 in that sport, COMPETITION after 50 in
that competition. These are workflow triggers, not sample-size guarantees. An alert (material software defect,
source-quality failure or sustained deterioration) makes the scope EARLY_REVIEW regardless of the count. A due
review never promotes a model by itself; its recorded disposition must use the review vocabulary.
"""
from __future__ import annotations

import argparse
import math
import secrets
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from ml import primary as p
from ml import research_ingest as ri
from ml.evaluation.prospective import DISPOSITIONS, verify_ledger

DEFAULT_THRESHOLDS = (("INTERIM", "ALL", 100), ("COMPREHENSIVE", "ALL", 300), ("SPORT", "*", 100),
                      ("COMPETITION", "*", 50))
REVIEW_FIELDS = ("review_id", "level", "scope", "through_at", "disposition", "report_path", "recorded_at")
ALERT_KINDS = ("MATERIAL_SOFTWARE_DEFECT", "SOURCE_QUALITY_FAILURE", "SUSTAINED_DETERIORATION")


def _sport(competition: str) -> str:
    return competition.split("/", 1)[0]


def settled_events(store: ri.Store) -> pd.DataFrame:
    """event_uid, competition, settled_at (first availability of a FINAL result)."""
    res = ri.effective_results(store)
    if res.empty:
        return pd.DataFrame(columns=["event_uid", "competition", "settled_at"])
    final = res[res.status.isin(ri.FINAL_STATUSES)]
    first, finals = {}, set(final.event_uid)
    obs = store.source_observations
    obs = obs[(obs.kind == "RESULT") & obs.disposition.isin(["FIRST_OBSERVED", "CORROBORATING", "CORRECTION"])]
    for r in obs.itertuples():
        t = p.clock(r.known_at)
        if r.event_uid in finals and (r.event_uid not in first or t < first[r.event_uid]):
            first[r.event_uid] = t
    comp = store.events.set_index("event_uid").competition
    return pd.DataFrame([dict(event_uid=u, competition=comp[u], settled_at=t) for u, t in sorted(first.items())])


def admitted_events(releases_root: Path | None) -> dict:
    from ml import training_admission as ta
    out = {}
    if releases_root and Path(releases_root).exists():
        for man in sorted(Path(releases_root).rglob("MANIFEST.csv")):
            m = ta.verify_release(man.parent, rebuild=False)
            for r in p.read_rows(man.parent / "ROWS.csv"):
                out[r["event_uid"]] = m["competition"]
    return out


def bundle_events(bundles_root: Path | None) -> dict:
    out = {}
    if bundles_root and Path(bundles_root).exists():
        for receipt in sorted(Path(bundles_root).rglob("RECEIPT.csv")):
            rows = p.read_rows(receipt)
            if len(rows) != 1 or rows[0].get("policy") not in (p.POLICY, p.LEGACY_POLICY):
                continue
            rec = p.verify_bundle(receipt.parent)
            out[rec["event_id"]] = rec["competition"]
    return out


def feedback_events(paths) -> dict:
    out = {}
    for path in paths or []:
        for r in p.read_rows(Path(path)):
            if r["event_id"] in out:
                raise p.AdmissionError("duplicate feedback event across inventories; reconcile one effective row")
            out[r["event_id"]] = r["context"].split("|")[1]
    return out


def prospective_events(ledger: Path | None, outcomes: Path | None) -> dict:
    out = {}
    if ledger and outcomes and Path(ledger).exists() and Path(outcomes).exists():
        rows = pd.DataFrame(verify_ledger(ledger))
        res = pd.read_csv(outcomes, dtype=str)
        ok = res[res.result.isin(["WIN", "LOSS"])][["event_id", "contract_key"]]
        pre = rows[rows.evidence_status == "PRE_START_VERIFIED"].merge(ok, on=["event_id", "contract_key"])
        out = dict(zip(pre.event_id, pre.competition))
    return out


def read_reviews(path: Path | None) -> pd.DataFrame:
    if not path or not Path(path).exists():
        return pd.DataFrame(columns=list(REVIEW_FIELDS))
    rows = p.read_rows(path)
    if rows and set(rows[0]) != set(REVIEW_FIELDS):
        raise p.AdmissionError("REVIEW_LOG requires the exact registered columns")
    for r in rows:
        if r["disposition"] not in DISPOSITIONS:
            raise p.AdmissionError(f"unknown review disposition {r['disposition']}")
        if r["disposition"] == "PROMOTION_ELIGIBLE" and not Path(r["report_path"]).exists():
            raise p.AdmissionError("PROMOTION_ELIGIBLE needs its prospective evaluation report")
        p.clock(r["through_at"])
    return pd.DataFrame(rows, columns=list(REVIEW_FIELDS))


def _scopes(competitions) -> list[tuple[str, str]]:
    comps = sorted(set(competitions))
    return [("ALL", "ALL")] + [("SPORT", s) for s in sorted({_sport(c) for c in comps})] + [("COMPETITION", c) for c in comps]


def _in_scope(level: str, scope: str, competition: str) -> bool:
    return level == "ALL" or (level == "SPORT" and _sport(competition) == scope) or competition == scope


def status(store: ri.Store, *, releases_root=None, bundles_root=None, feedback=(), shadow_ledger=None,
           outcomes=None, reviews=None, thresholds=DEFAULT_THRESHOLDS, alerts=None, now=None) -> dict:
    settled = settled_events(store)
    admitted, bundles = admitted_events(releases_root), bundle_events(bundles_root)
    fb, pro = feedback_events(feedback), prospective_events(shadow_ledger, outcomes)
    reviews = reviews if reviews is not None else pd.DataFrame(columns=list(REVIEW_FIELDS))
    comps = list(settled.competition) + list(admitted.values()) + list(bundles.values()) + list(fb.values()) + list(pro.values())
    rows, triggers = [], []
    for level, scope in _scopes(comps):
        inside = lambda comp: _in_scope(level, scope, comp)
        rows.append(dict(scope_level=level, scope=scope,
                         unique_settled_games=int(settled.competition.map(inside).sum()) if len(settled) else 0,
                         ml_admissible_games=sum(map(inside, admitted.values())),
                         frozen_model_forecasts=sum(map(inside, bundles.values())),
                         hedge_feedback_games=sum(map(inside, fb.values())),
                         prospective_eval_games=sum(map(inside, pro.values()))))
    for review_level, scope_rule, threshold in thresholds:
        for level, scope in _scopes(comps):
            wanted = {"INTERIM": "ALL", "COMPREHENSIVE": "ALL", "SPORT": "SPORT", "COMPETITION": "COMPETITION"}[review_level]
            if level != wanted or (scope_rule not in ("*", scope)):
                continue
            past = reviews[(reviews.level == review_level) & (reviews.scope == scope)]
            through = max((p.clock(t) for t in past.through_at), default=None)
            mine = settled[settled.competition.map(lambda c: _in_scope(level, scope, c))] if len(settled) else settled
            since = int(sum(1 for t in mine.settled_at if through is None or t > through))
            alert = None
            if alerts is not None and len(alerts):
                hits = alerts[alerts.scope.isin([scope, "ALL"]) & alerts.raised_at.map(
                    lambda t: through is None or p.clock(t) > through)]
                alert = ";".join(sorted(set(hits.kind))) if len(hits) else None
            state = "EARLY_REVIEW" if alert else ("DUE" if since >= int(threshold) else "NOT_DUE")
            triggers.append(dict(level=review_level, scope=scope, settled_since_last=since, threshold=int(threshold),
                                 last_review_through=through.isoformat() if through else "NEVER", status=state,
                                 reason=alert or ("threshold reached; review proposes a disposition, never an automatic "
                                                  "promotion" if state == "DUE" else "")))
    return dict(status=pd.DataFrame(rows), triggers=pd.DataFrame(triggers),
                generated_at=(p.clock(now) if now else datetime.now(timezone.utc)).isoformat())


def read_thresholds(path: Path | None):
    if not path:
        return DEFAULT_THRESHOLDS
    rows = p.read_rows(path)
    out = []
    for r in rows:
        if r["level"] not in ("INTERIM", "COMPREHENSIVE", "SPORT", "COMPETITION") or int(r["threshold"]) <= 0:
            raise p.AdmissionError("unknown review level or nonpositive threshold")
        out.append((r["level"], r["scope"], int(r["threshold"])))
    return tuple(out)


def read_alerts(path: Path | None) -> pd.DataFrame | None:
    if not path:
        return None
    rows = pd.read_csv(path, dtype=str, keep_default_na=False)
    if set(rows.columns) != {"scope", "kind", "raised_at", "evidence_path"} or not rows.kind.isin(ALERT_KINDS).all():
        raise p.AdmissionError("alerts need scope,kind,raised_at,evidence_path with a registered kind")
    for path_ in rows.evidence_path:
        if not Path(path_).exists():
            raise p.AdmissionError("an early-review alert needs existing evidence")
    return rows


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--store", type=Path, required=True)
    parser.add_argument("--releases-root", type=Path)
    parser.add_argument("--bundles-root", type=Path)
    parser.add_argument("--feedback", type=Path, nargs="*", default=())
    parser.add_argument("--shadow-ledger", type=Path)
    parser.add_argument("--outcomes", type=Path)
    parser.add_argument("--review-log", type=Path)
    parser.add_argument("--thresholds", type=Path)
    parser.add_argument("--alerts", type=Path)
    parser.add_argument("--out", type=Path, help="new folder for LEARNING_STATUS.csv / REVIEW_TRIGGERS.csv / .md")
    args = parser.parse_args(argv)
    res = status(ri.load_store(args.store), releases_root=args.releases_root, bundles_root=args.bundles_root,
                 feedback=args.feedback, shadow_ledger=args.shadow_ledger, outcomes=args.outcomes,
                 reviews=read_reviews(args.review_log), thresholds=read_thresholds(args.thresholds),
                 alerts=read_alerts(args.alerts))
    print(res["status"].to_string(index=False))
    print(res["triggers"].to_string(index=False))
    if args.out:
        from ml.evaluation.report import md_table
        if args.out.exists():
            raise FileExistsError(args.out)
        tmp = args.out.parent / ("." + args.out.name + "." + secrets.token_hex(6))
        tmp.mkdir(parents=True)
        res["status"].to_csv(tmp / "LEARNING_STATUS.csv", index=False, lineterminator="\n")
        res["triggers"].to_csv(tmp / "REVIEW_TRIGGERS.csv", index=False, lineterminator="\n")
        s, t = res["status"], res["triggers"]
        (tmp / "LEARNING_STATUS.md").write_text(
            f"# Learning status ({res['generated_at']})\n\nStore view {ri.load_store(args.store).view_seq}. Counts are "
            "derived from verified artifacts. Triggers propose reviews; none promotes a model.\n\n"
            + md_table(s, list(s.columns), 0) + "\n" + md_table(t, list(t.columns), 0), encoding="utf-8", newline="\n")
        tmp.rename(args.out)


if __name__ == "__main__":
    main()
