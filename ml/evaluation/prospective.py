"""Prospective shadow ledger and paired candidate-versus-champion evaluation (Improvements 18–20, 23).

FREEZE: a candidate or champion appends frozen rows to an append-only, hash-chained SHADOW_LEDGER.csv before the
event starts (issued_at < scheduled_start, PRE_START_VERIFIED evidence). A changed or reordered earlier row breaks
the chain. A locally written ledger is not proof of publication; commit it before the start for that claim.

EVALUATE: after settlement, only rows of the two models on IDENTICAL (event, contract) pairs are compared. One
match with four contracts is one sporting event: paired differences are averaged within event, then within ISO
week, and intervals are t-intervals over week means (SCORING_AND_VALIDATION §5). The preregistered minimum effect
(``delta``) gives the weeks needed for a two-sided test at 80% power from the observed week SD; an interval that
cannot resolve that effect is INSUFFICIENT_EVIDENCE, never a win. Dispositions follow the review vocabulary:
NO_CHANGE, DATA_REPAIR_REQUIRED, EXPERIMENTAL_RETRAIN, CALIBRATION_STUDY, PROSPECTIVE_SHADOW, PROMOTION_ELIGIBLE,
INSUFFICIENT_EVIDENCE. PROMOTION_ELIGIBLE is a recommendation for an owner decision, never an automatic release.
"""
from __future__ import annotations

import argparse
import hashlib
import math
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

from ml import primary as p
from ml.core.metrics import calibration_fit, iso_week, paired_week_interval

LEDGER_FIELDS = ("forecast_id", "model_id", "model_version", "role", "event_id", "competition", "endpoint",
                 "contract_key", "family", "side", "line", "p", "rank", "issued_at", "scheduled_start",
                 "training_release", "param_version", "code_sha256", "evidence_status", "prev_row_sha256",
                 "row_sha256")
OUTCOME_FIELDS = ("event_id", "contract_key", "result", "final_at", "available_at", "evidence_sha256")
DISPOSITIONS = ("NO_CHANGE", "DATA_REPAIR_REQUIRED", "EXPERIMENTAL_RETRAIN", "CALIBRATION_STUDY",
                "PROSPECTIVE_SHADOW", "PROMOTION_ELIGIBLE", "INSUFFICIENT_EVIDENCE")
EVIDENCE_STATUSES = ("PRE_START_VERIFIED", "TIMING_UNVERIFIED", "POST_START")
GENESIS = "0" * 64


def _row_hash(row: dict) -> str:
    return hashlib.sha256("\x1f".join(str(row[f]) for f in LEDGER_FIELDS[:-1]).encode()).hexdigest()


def read_ledger(path: Path) -> list[dict]:
    if not Path(path).exists():
        return []
    rows = p.read_rows(path)
    if rows and tuple(rows[0]) != LEDGER_FIELDS:
        raise p.AdmissionError("shadow ledger columns differ from the registered schema")
    return rows


def verify_ledger(path: Path) -> list[dict]:
    rows = read_ledger(path)
    prev, seen = GENESIS, set()
    for r in rows:
        if r["prev_row_sha256"] != prev or _row_hash(r) != r["row_sha256"]:
            raise p.AdmissionError(f"shadow ledger chain broken at {r['forecast_id']}/{r['contract_key']}")
        key = (r["model_id"], r["model_version"], r["event_id"], r["contract_key"])
        if key in seen:
            raise p.AdmissionError("a model may freeze one row per event contract")
        seen.add(key)
        prev = r["row_sha256"]
    return rows


def freeze(path: Path, rows: list[dict], *, now=None) -> list[dict]:
    """Append frozen forecasts; refuse late, malformed, market-bearing or duplicate rows."""
    existing = verify_ledger(path)
    seen = {(r["model_id"], r["model_version"], r["event_id"], r["contract_key"]) for r in existing}
    prev = existing[-1]["row_sha256"] if existing else GENESIS
    now = p.clock(now) if now is not None else pd.Timestamp.now(tz="UTC")
    out = []
    for r in rows:
        if set(r) != set(LEDGER_FIELDS[:-2]):
            raise p.AdmissionError("exact shadow row fields required; market/staking fields prohibited")
        prob = float(r["p"])
        if not math.isfinite(prob) or not 0 <= prob <= 1:
            raise p.AdmissionError("probability must be finite in [0,1]")
        if r["role"] not in ("CHAMPION", "CANDIDATE") or r["evidence_status"] not in EVIDENCE_STATUSES:
            raise p.AdmissionError("unknown role or evidence status")
        issued, start = p.clock(r["issued_at"]), p.clock(r["scheduled_start"])
        if r["evidence_status"] == "PRE_START_VERIFIED" and not (issued < start and now < start):
            raise p.AdmissionError("PRE_START_VERIFIED requires issue and freeze before the scheduled start")
        if issued > now:
            raise p.AdmissionError("issue time is in the future")
        key = (r["model_id"], r["model_version"], r["event_id"], r["contract_key"])
        if key in seen:
            raise p.AdmissionError("duplicate frozen contract for this model version")
        seen.add(key)
        row = {f: str(r[f]) for f in LEDGER_FIELDS[:-2]}
        row["prev_row_sha256"] = prev
        row["row_sha256"] = prev = _row_hash(row)
        out.append(row)
    if out:
        from ml.research_ingest import _append  # append-only: earlier bytes are never rewritten
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        _append(Path(path), LEDGER_FIELDS, out)
        verify_ledger(path)
    return out


def _grade(rows: pd.DataFrame, outcomes: pd.DataFrame) -> pd.DataFrame:
    if set(outcomes.columns) != set(OUTCOME_FIELDS):
        raise p.AdmissionError("exact outcome fields required")
    if outcomes.duplicated(["event_id", "contract_key"]).any():
        raise p.AdmissionError("duplicate outcome rows: reconcile one effective settlement first")
    merged = rows.merge(outcomes, on=["event_id", "contract_key"], how="left")
    merged["y"] = merged.result.map({"WIN": 1.0, "LOSS": 0.0})
    late = merged.available_at.notna() & (merged.available_at.map(lambda t: p.clock(t) if isinstance(t, str) else pd.NaT)
                                           <= merged.issued_at.map(p.clock))
    if late.any():
        raise p.AdmissionError("outcome available before the forecast was issued: not prospective")
    return merged


def _ranking(frame: pd.DataFrame) -> dict:
    """Rank-1 accuracy, Hit@2 and NDCG@2 over events whose top two rows are decisive."""
    r1 = hit2 = ndcg = n = 0
    for _, g in frame.groupby("event_id"):
        top = g.assign(rk=pd.to_numeric(g["rank"], errors="coerce")).dropna(subset=["rk"]).sort_values("rk").head(2)
        if len(top) < 2 or top.y.isna().any():
            continue
        n += 1
        rel = top.y.to_numpy()
        r1 += rel[0]
        hit2 += float(rel.max() > 0)
        ideal = 1 + (1 / math.log2(3) if rel.sum() == 2 else 0)
        ndcg += (rel[0] + rel[1] / math.log2(3)) / ideal if rel.sum() else 0.0
    return dict(ranked_events=n, rank1_accuracy=r1 / n if n else math.nan, hit_at_2=hit2 / n if n else math.nan,
                ndcg_at_2=ndcg / n if n else math.nan)


def weeks_needed(sd_week: float, delta: float, alpha: float = 0.05, power: float = 0.8) -> float:
    if not (math.isfinite(sd_week) and sd_week > 0 and delta > 0):
        return math.nan
    z = stats.norm.ppf(1 - alpha / 2) + stats.norm.ppf(power)
    return math.ceil((z * sd_week / delta) ** 2)


def evaluate(ledger: list[dict], outcomes: pd.DataFrame, champion: str, candidate: str, *, delta: float,
             slope_band=(0.8, 1.25), coverage_tolerance: float = 0.05) -> dict:
    """``champion``/``candidate`` are 'model_id:model_version'. ``delta`` is the preregistered Brier improvement."""
    frame = pd.DataFrame(ledger)
    frame["tag"] = frame.model_id + ":" + frame.model_version
    eligible = frame[(frame.evidence_status == "PRE_START_VERIFIED") &
                     (frame.issued_at.map(p.clock) < frame.scheduled_start.map(p.clock))]
    graded = _grade(eligible, outcomes)
    champ, cand = graded[graded.tag == champion], graded[graded.tag == candidate]
    keys = ["event_id", "contract_key"]
    union = len(pd.concat([champ[keys], cand[keys]]).drop_duplicates())
    pair = champ.merge(cand, on=keys, suffixes=("_c", "_k"))
    pair = pair[pair.y_c.notna()]
    if pair.empty:
        return dict(disposition="INSUFFICIENT_EVIDENCE", reason="no settled identical pre-start contracts", pairs=0)
    pair["week"] = iso_week(pair.scheduled_start_c.map(lambda t: p.clock(t).tz_localize(None)))
    pair["d_brier"] = (pair.p_k.astype(float) - pair.y_c) ** 2 - (pair.p_c.astype(float) - pair.y_c) ** 2
    iv = paired_week_interval(pair.d_brier, pair.event_id, pair.week)
    need = weeks_needed(iv["sd_w"], delta)
    per = {}
    for tag, rows in ((champion, champ), (candidate, cand)):
        rows = rows[rows.y.notna()]
        q = rows.p.astype(float)
        fit = calibration_fit(q, rows.y)
        per[tag] = dict(rows=len(rows), events=rows.event_id.nunique(), coverage=len(rows) / union if union else math.nan,
                        brier=float(((q - rows.y) ** 2).mean()),
                        log_loss=float(-np.mean(np.log(np.clip(np.where(rows.y == 1, q, 1 - q), 1e-12, 1)))),
                        slope=fit["slope"], intercept=fit["intercept"], **_ranking(rows))
    breakdown = []
    for by in ("competition_c", "family_c", "endpoint_c"):
        for value, g in pair.groupby(by):
            biv = paired_week_interval(g.d_brier, g.event_id, g.week)
            breakdown.append(dict(dimension=by[:-2], value=value, contracts=len(g), events=g.event_id.nunique(),
                                  mean_d_brier=biv["mean"], k_weeks=biv["k_weeks"], status=biv["status"]))
    unsettled = graded.y.isna().mean()
    c, k = per[champion], per[candidate]
    if unsettled > 0.2:
        disposition, reason = "DATA_REPAIR_REQUIRED", f"{unsettled:.0%} of eligible rows unsettled"
    elif iv["k_weeks"] < 8 or (math.isfinite(need) and iv["k_weeks"] < need and iv["status"] == "SPANS_ZERO"):
        disposition, reason = "INSUFFICIENT_EVIDENCE", f"{iv['k_weeks']} weeks; about {need} needed for delta={delta}"
    elif iv["status"] == "BELOW_ZERO" and iv["mean"] <= -delta / 2:
        guard = (slope_band[0] <= k["slope"] <= slope_band[1]) and k["coverage"] >= c["coverage"] - coverage_tolerance
        disposition = "PROMOTION_ELIGIBLE" if guard else "CALIBRATION_STUDY"
        reason = "candidate better on paired Brier" + ("" if guard else "; calibration/coverage guard failed")
    elif iv["status"] == "ABOVE_ZERO":
        disposition, reason = "NO_CHANGE", "candidate worse on paired Brier"
    else:
        disposition, reason = "NO_CHANGE", "no resolvable difference at the registered effect size"
    return dict(disposition=disposition, reason=reason, pairs=len(pair), interval=iv, weeks_needed=need,
                models=per, unsettled_share=float(unsettled), breakdown=pd.DataFrame(breakdown))


def _common(model_id, version, role, event_id, competition, endpoint, issued_at, start, release, params, code, status):
    return dict(model_id=model_id, model_version=version, role=role, event_id=event_id, competition=competition,
                endpoint=endpoint, issued_at=issued_at, scheduled_start=start, training_release=release,
                param_version=params, code_sha256=code, evidence_status=status)


def _status(issued_at, start, now) -> str:
    return "PRE_START_VERIFIED" if p.clock(issued_at) < p.clock(start) and now < p.clock(start) else "TIMING_UNVERIFIED"


def rows_from_primary_bundle(folder: Path, role: str = "CHAMPION", now=None) -> list[dict]:
    """Shadow-ledger rows from a verified PRIMARY_HEDGE_MIX bundle (every priced contract, original ranks kept)."""
    rec = p.verify_bundle(Path(folder))
    req = p.read_rows(Path(folder) / "REQUEST.csv")[0]
    now = p.clock(now) if now is not None else pd.Timestamp.now(tz="UTC")
    base = _common(rec["policy"], rec["model_id"], role, rec["event_id"], rec["competition"], rec["endpoint"],
                   rec["issue_at"], req["scheduled_start"], "BUNDLE_HISTORY:" + rec["history_sha256"][:16],
                   f"eta={rec['eta']};{rec['eta_source']}", rec["code_sha256"], _status(rec["issue_at"], req["scheduled_start"], now))
    out = []
    for r in p.read_rows(Path(folder) / "PREDICTIONS.csv"):
        if r["p_card"] == "NOT_COMPUTED":
            continue
        out.append(dict(forecast_id=f"{rec['policy']}:{rec['event_id']}", contract_key=r["contract_key"], family=r["family"],
                        side=r["side"], line=r["line"], p=r["p_card"], rank=r["rank"], **base))
    return out


def rows_from_tennis_bundle(folder: Path, role: str = "CANDIDATE", now=None) -> list[dict]:
    """Shadow-ledger rows from a verified TENNIS_EXPERIMENTAL_HEDGE_V1 bundle; rank = descending p."""
    from ml import tennis_primary as t
    t.verify(Path(folder))
    rec = t.rows(Path(folder) / "RECEIPT.csv")[0]
    req = t.rows(Path(folder) / "REQUEST.csv")[0]
    now = p.clock(now) if now is not None else pd.Timestamp.now(tz="UTC")
    preds = [r for r in t.rows(Path(folder) / "PREDICTIONS.csv") if r.get("p_card") not in ("", "None", None)]
    preds.sort(key=lambda r: (-float(r["p_card"]), r["contract_key"]))
    base = _common(rec["policy"], "1", role, rec["event_id"], req["competition"], f"COMPLETED_BEST_OF_{req['best_of']}",
                   req["issue_at"], req["scheduled_start"], "BUNDLE_HISTORY:" + rec["sha256_HISTORY.csv"][:16],
                   f"eta={rec['eta']}", rec["code_sha256"], _status(req["issue_at"], req["scheduled_start"], now))
    return [dict(forecast_id=f"{rec['policy']}:{rec['event_id']}", contract_key=r["contract_key"], family=r["family"],
                 side=r["side"], line=r.get("line", ""), p=r["p_card"], rank=str(i), **base)
            for i, r in enumerate(preds, 1)]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    fz = sub.add_parser("freeze")
    fz.add_argument("--ledger", type=Path, required=True)
    fz.add_argument("--rows", type=Path, required=True)
    rw = sub.add_parser("rows", help="shadow rows from a verified primary or tennis bundle")
    rw.add_argument("--bundle", type=Path, required=True)
    rw.add_argument("--kind", choices=("primary", "tennis"), required=True)
    rw.add_argument("--role", choices=("CHAMPION", "CANDIDATE"), required=True)
    rw.add_argument("--out", type=Path, required=True)
    vf = sub.add_parser("verify")
    vf.add_argument("--ledger", type=Path, required=True)
    ev = sub.add_parser("evaluate")
    ev.add_argument("--ledger", type=Path, required=True)
    ev.add_argument("--outcomes", type=Path, required=True)
    ev.add_argument("--champion", required=True)
    ev.add_argument("--candidate", required=True)
    ev.add_argument("--delta", type=float, required=True, help="preregistered minimum Brier improvement")
    args = parser.parse_args(argv)
    if args.command == "rows":
        make = rows_from_primary_bundle if args.kind == "primary" else rows_from_tennis_bundle
        rows = make(args.bundle, args.role)
        with args.out.open("xb") as f:
            f.write(p.csv_bytes(rows))
        print(f"{len(rows)} shadow rows ({rows[0]['evidence_status'] if rows else 'none'}) -> {args.out}")
    elif args.command == "freeze":
        print(f"froze {len(freeze(args.ledger, p.read_rows(args.rows)))} rows")
    elif args.command == "verify":
        print(f"chain intact: {len(verify_ledger(args.ledger))} rows")
    else:
        res = evaluate(verify_ledger(args.ledger), pd.read_csv(args.outcomes, dtype=str), args.champion,
                       args.candidate, delta=args.delta)
        print(res["disposition"], "-", res["reason"])
        for k, v in res.get("models", {}).items():
            print(k, {kk: round(vv, 4) if isinstance(vv, float) else vv for kk, vv in v.items()})


if __name__ == "__main__":
    main()
