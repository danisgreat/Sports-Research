"""V3-equivalent rolling-origin backtest of PRIMARY_HEDGE_MIX_V3 (Improvement 17).

Unlike the preserved 41,752-game proxy replay (ml.evaluation.primary_replay), every evaluated event is issued with
the runtime's own functions and policy: ``primary.fit_experts_and_line`` at the event's horizon on rows whose game,
final and source availability were known by then; ``primary.warm_records`` for the 30-game-week warm start; and
full-information feedback from earlier backtest issues that were settled and available by the horizon, which take
precedence over overlapping warm events (one learning contribution per event). Weights use the provisional
η = DEFAULT_ETA exactly as the runtime does without an admitted parameter.

Evidence class HISTORICAL_V3_EQUIVALENT_BACKTEST_NOT_PROSPECTIVE: the inputs are historical rows, the "issue"
times are simulated horizons, and nothing here is a frozen pre-start forecast. The per-event ledger keeps every
expert's probabilities for the common questions so alternative learning-rate schedules can be studied without
refitting (ml.hedge), on separate tuning and evaluation windows.
"""
from __future__ import annotations

import argparse
import hashlib
import secrets
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from ml import primary as p
from ml.config import League
from ml.core.metrics import iso_week, paired_week_interval
from ml.models.common import FitError

EVIDENCE_CLASS = "HISTORICAL_V3_EQUIVALENT_BACKTEST_NOT_PROSPECTIVE"
ARMS = p.ARMS


def _visible(full: pd.DataFrame, horizon: pd.Timestamp, exclude: str) -> pd.DataFrame:
    h = horizon.tz_localize(None)
    keep = (full.date < h.normalize()) & (full.final_at <= h) & (full.available_at <= h) & (full.event_id != exclude)
    return full[keep].reset_index(drop=True)


def run(history: list[dict], lg: League, eval_start, eval_end=None, *, eta: float = p.DEFAULT_ETA,
        use_feedback: bool = True) -> pd.DataFrame:
    """Issue every evaluation event at its own start; return the per-event ledger (one row per event)."""
    latest = max(p.clock(r["available_at"]) for r in history) + pd.Timedelta(days=2)
    full = p.admit_history(history, latest, "", lg.path, lg.endpoint)  # validates every row and its evidence once
    start = p.clock(eval_start).tz_localize(None)
    end = p.clock(eval_end).tz_localize(None) if eval_end is not None else None
    targets = full[(full.date >= start) & ((full.date < end) if end is not None else True)]
    context = f"{p.POLICY}|{lg.path}|{lg.endpoint}"
    cricket = lg.engine == "cricket"
    issued, rows, warm_cache = [], [], {}
    coverage = dict(requested=len(targets), unseen=0, fit_failed=0, flagged=0)
    for t in targets.sort_values(["date", "event_id"]).itertuples():
        horizon = pd.Timestamp(t.date).tz_localize("UTC")
        train = _visible(full, horizon, t.event_id)
        known = set(train.home) | set(train.away)
        if t.home not in known or t.away not in known:
            coverage["unseen"] += 1
            continue
        try:
            experts, line = p.fit_experts_and_line(lg, train, horizon.isoformat(), t.home, t.away, getattr(t, "venue", "") or "")
        except FitError:
            coverage["fit_failed"] += 1
            continue
        except p.AdmissionError:
            coverage["flagged"] += 1
            continue
        fb = [r for r in issued if use_feedback and r["available_at"] <= horizon]
        fb_ids = {r["event_id"] for r in fb}
        key = (horizon.normalize(), hashlib.sha256("|".join(sorted(train.event_id)).encode()).hexdigest())
        if key not in warm_cache:
            warm_cache[key] = p.warm_records(lg, train, horizon.tz_localize(None))
        warm = [w for w in warm_cache[key] if w["event_id"] not in fb_ids]
        cumulative = p.loss_sum(warm + [{**{"loss_" + a: r["loss_" + a] for a in ARMS}} for r in fb])
        weights = p.hedge_weights(cumulative, eta)
        mix = p.mix_grids([experts[a] for a in ARMS], weights)
        hs, as_ = int(t.hs), int(t.as_)
        row = dict(event_id=t.event_id, context=context, season=int(t.season), issued_at=horizon.isoformat(),
                   available_at=pd.Timestamp(t.available_at).tz_localize("UTC").isoformat(),
                   week=iso_week(pd.Series([t.date])).iloc[0], league_line=line, y_home=float(hs > as_),
                   y_over=float(hs + as_ > line), home_score=hs, away_score=as_, n_warm=len(warm), n_feedback=len(fb),
                   **{"w_" + a: float(x) for a, x in zip(ARMS, weights)})
        for name, g in list(experts.items()) + [(p.MIX_ARM, mix)]:
            row["p_home_" + name] = g.winner()[0]
            row["p_over_" + name] = g.total(line, "OVER").win
            row["loss_" + name] = p.expert_loss(g, hs, as_, line, cricket)
            if not cricket:
                row["crps_margin_" + name] = g.crps_margin(hs - as_)
            row["crps_total_" + name] = g.crps_total(hs + as_)
        rows.append(row)
        issued.append(dict(event_id=t.event_id, available_at=p.clock(row["available_at"]),
                           **{"loss_" + a: row["loss_" + a] for a in ARMS}))
    ledger = pd.DataFrame(rows)
    ledger.attrs["coverage"] = coverage
    return ledger


def summarise(ledger: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    names = list(ARMS) + [p.MIX_ARM]
    summary = []
    for n in names:
        summary.append(dict(arm=n, events=len(ledger),
                            brier_home=float(((ledger["p_home_" + n] - ledger.y_home) ** 2).mean()),
                            brier_over=float(((ledger["p_over_" + n] - ledger.y_over) ** 2).mean()),
                            common_loss=float(ledger["loss_" + n].mean()),
                            crps_margin=float(ledger["crps_margin_" + n].mean()) if "crps_margin_" + n in ledger else float("nan"),
                            crps_total=float(ledger["crps_total_" + n].mean())))
    paired = []
    for n in ARMS:
        for metric in ("loss", "crps_total"):
            if metric + "_" + n in ledger:
                iv = paired_week_interval(ledger[f"{metric}_{p.MIX_ARM}"] - ledger[f"{metric}_{n}"], ledger.event_id, ledger.week)
                paired.append(dict(candidate=p.MIX_ARM, reference=n, metric=metric, **iv))
    return pd.DataFrame(summary), pd.DataFrame(paired)


def write(ledger: pd.DataFrame, out: Path, receipt: dict) -> None:
    from ml.evaluation.report import md_table
    out = Path(out)
    if out.exists():
        raise FileExistsError(out)
    summary, paired = summarise(ledger)
    tmp = out.parent / ("." + out.name + "." + secrets.token_hex(6))
    tmp.mkdir(parents=True)
    for name, frame in (("LEDGER.csv", ledger), ("SUMMARY.csv", summary), ("PAIRED.csv", paired)):
        frame.to_csv(tmp / name, index=False, lineterminator="\n")
    receipt = dict(receipt, evidence_class=EVIDENCE_CLASS, policy=p.POLICY, eta=p.DEFAULT_ETA,
                   **{"coverage_" + k: v for k, v in ledger.attrs.get("coverage", {}).items()},
                   **{n.lower().replace(".", "_") + "_sha256": p.digest((tmp / n).read_bytes())
                      for n in ("LEDGER.csv", "SUMMARY.csv", "PAIRED.csv")})
    (tmp / "RECEIPT.csv").write_bytes(p.csv_bytes([receipt]))
    lines = [f"# V3-equivalent backtest — {receipt.get('competition', '')}", "",
             f"**Evidence class: `{EVIDENCE_CLASS}`.** Each event issued at its own start with the runtime's fitting, "
             "warm-start and delayed-feedback functions (module docstring). Simulated issue times are not frozen "
             "forecasts. Negative paired means favour the mixture. Fewer than eight weeks is INSUFFICIENT_EVIDENCE.", "",
             md_table(summary, list(summary.columns), 4), "",
             md_table(paired, list(paired.columns), 4) if len(paired) else "No paired rows.", "", "## Receipt", "",
             "\n".join(f"- `{k}`: {v}" for k, v in receipt.items())]
    (tmp / "RESULTS.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    tmp.rename(out)


def main(argv=None):
    from ml import research_ingest as ri
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = parser.add_mutually_exclusive_group(required=True)
    src.add_argument("--history", type=Path, help="primary HISTORY.csv rows")
    src.add_argument("--store", type=Path, help="learning store; history = every reviewed FINAL known now")
    parser.add_argument("--competition-source", type=Path, required=True)
    parser.add_argument("--eval-start", required=True)
    parser.add_argument("--eval-end")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    rows = p.read_rows(args.competition_source)
    now = datetime.now(timezone.utc).isoformat()
    lg = p.reviewed_source_league(dict(competition=rows[0]["sport"] + "/" + rows[0]["competition"],
                                       endpoint=rows[0]["endpoint"], scheduled_start=now, issue_at=now), rows[0])
    code = p.source_hash()
    history = p.read_rows(args.history) if args.history else ri.history_rows(ri.load_store(args.store), lg.path, lg.endpoint, now)
    ledger = run(history, lg, args.eval_start, args.eval_end)
    if p.source_hash() != code:
        raise RuntimeError("generating source changed during the backtest")
    write(ledger, args.out, dict(competition=lg.path, endpoint=lg.endpoint, eval_start=args.eval_start,
                                 eval_end=args.eval_end or "", history_sha256=p.digest(p.csv_bytes(history)),
                                 code_sha256=code, repository_head=p.repository_head(), generated_at=now))
    print(f"{len(ledger)} events -> {args.out}")


if __name__ == "__main__":
    main()
