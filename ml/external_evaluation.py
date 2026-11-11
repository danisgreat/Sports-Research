"""Frozen paired SINGLE_RESEARCH / FIVE_LANES / REFERENCE / BASELINE evaluation (EXT-EVAL-v1).

Uses the existing verified prospective ledger and effective sporting outcomes, never chat agreement as ground truth.
The decision floor is exactly 100 paired events and at least eight settled ISO weeks; this is a floor, not proven power.
"""
from pathlib import Path
import csv
import math
import hashlib

import pandas as pd

from ml.evaluation import prospective as P

MODELS = ("SINGLE_RESEARCH:v24.14", "REFERENCE:v24.14", "BASELINE:v24.14")
FIVE = "FIVE_LANES:v24.14"
MIN_EVENTS = 100
MIN_WEEKS = 8
DELTA = 0.01


def evaluate(forecasts, outcomes, out, *, as_of=None):
    rows = P.verify_ledger(Path(forecasts))
    labels = pd.read_csv(outcomes, keep_default_na=False, dtype=str)
    if tuple(labels.columns) != P.OUTCOME_FIELDS:
        raise ValueError("effective outcomes must have the existing prospective OUTCOME_FIELDS schema")
    if labels.duplicated(["event_id", "contract_key"]).any():
        raise ValueError("provide one validated effective outcome per event/contract, not raw revision history")
    horizon = pd.Timestamp(as_of) if as_of is not None else pd.Timestamp.now(tz="UTC")
    if horizon.tzinfo is None: raise ValueError("evaluation horizon needs an offset")
    labels = labels[labels.available_at.map(lambda s: pd.Timestamp(s) <= horizon).astype(bool)].copy()
    rows = [r for r in rows if r["model_id"] + ":" + r["model_version"] in set(MODELS) | {FIVE}]
    # Freeze the first completed-week cohort meeting the preregistered primary floor. Later data cannot move it.
    by_tag = {tag: {(r["event_id"], r["contract_key"]): r for r in rows
                    if r["model_id"] + ":" + r["model_version"] == tag and r["evidence_status"] == "PRE_START_VERIFIED"
                    and pd.Timestamp(r["issued_at"]) < pd.Timestamp(r["scheduled_start"])}
              for tag in (MODELS[0], FIVE)}
    available = {(r.event_id, r.contract_key) for r in labels.itertuples() if r.result in ("WIN", "LOSS")}
    common = set(by_tag[MODELS[0]]) & set(by_tag[FIVE]) & available
    events = {}
    for key in common:
        single, five = by_tag[MODELS[0]][key], by_tag[FIVE][key]
        if pd.Timestamp(single["issued_at"]) > pd.Timestamp(five["issued_at"]):
            raise ValueError("SINGLE_RESEARCH must be frozen before FIVE_LANES")
        start = pd.Timestamp(five["scheduled_start"]).tz_convert("UTC")
        monday = start.normalize() - pd.Timedelta(days=start.weekday())
        if monday + pd.Timedelta(days=7) > horizon: continue
        events[key[0]] = dict(event_id=key[0], scheduled_start=start.isoformat(), week=monday.isoformat())
    selected, event_count, week_count, stopped = set(), 0, 0, False
    for week in sorted({r["week"] for r in events.values()}):
        selected |= {k for k, r in events.items() if r["week"] == week}
        week_count += 1
        if len(selected) >= MIN_EVENTS and week_count >= MIN_WEEKS:
            stopped = True; break
    rows = [r for r in rows if r["event_id"] in selected]
    labels = labels[labels.event_id.isin(selected)]
    result = []
    breakdown = []
    for champion in MODELS:
        r = P.evaluate(rows, labels, champion, FIVE, delta=DELTA)
        iv = r.get("interval", {})
        count, weeks = int(iv.get("n_events", 0)), int(iv.get("k_weeks", 0))
        disposition = r["disposition"]
        if count < MIN_EVENTS or weeks < MIN_WEEKS:
            disposition = "INSUFFICIENT_EVIDENCE"
        if champion != MODELS[0] and disposition != "INSUFFICIENT_EVIDENCE":
            disposition = "SECONDARY_DIAGNOSTIC_ONLY"
        result.append(dict(champion=champion, candidate=FIVE, paired_events=count, settled_weeks=weeks,
                           mean_brier_difference=iv.get("mean", ""), interval_low=iv.get("lo", ""), interval_high=iv.get("hi", ""),
                           disposition=disposition, minimum_events=MIN_EVENTS, minimum_weeks=MIN_WEEKS, minimum_effect=DELTA,
                           qualification="RECOMMENDATION_ONLY_REQUIRES_PUBLICATION_AND_ROUTE_AUDIT",
                           reason=r.get("reason", "")))
        if isinstance(r.get("breakdown"), pd.DataFrame):
            breakdown += [dict(champion=champion, candidate=FIVE, **v) for v in r["breakdown"].to_dict("records")]
    out = Path(out)
    out.mkdir(parents=True, exist_ok=False)
    with (out / "PAIRED_RESULTS.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=tuple(result[0]), lineterminator="\n"); w.writeheader(); w.writerows(result)
    with (out / "COHORT.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=("event_id", "scheduled_start", "week"), lineterminator="\n"); w.writeheader()
        w.writerows(events[k] for k in sorted(selected))
    receipt = dict(ledger_sha256=hashlib.sha256(Path(forecasts).read_bytes()).hexdigest() if Path(forecasts).is_file() else "NOT_PRESENT",
                   outcomes_sha256=hashlib.sha256(Path(outcomes).read_bytes()).hexdigest(),
                   cohort_sha256=hashlib.sha256((out / "COHORT.csv").read_bytes()).hexdigest(), events=len(selected), settled_weeks=week_count,
                   decision_window="FROZEN_FIRST_COMPLETED_WEEK" if stopped else "COLLECTING_INSUFFICIENT_EVIDENCE", evaluated_as_of=horizon.isoformat())
    with (out / "COHORT_RECEIPT.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=tuple(receipt), lineterminator="\n"); w.writeheader(); w.writerow(receipt)
    if breakdown:
        with (out / "STRATA.csv").open("w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=tuple(breakdown[0]), lineterminator="\n"); w.writeheader(); w.writerows(breakdown)
    (out / "README.md").write_text(
        "# External research paired evaluation\n\n"
        "Negative Brier difference favours FIVE_LANES. One event contributes one event-level comparison; multiple contracts "
        "are dependent. The existing evaluator aggregates events and weeks. Do not repeatedly test an expanding cohort: "
        "the one decision is the first completed ISO week after both 100 paired settled events and eight settled weeks. "
        "Use the predeclared immutable cohort, effective outcomes and exact endpoint keys.\n\n"
        "This output does not certify source truth, pregame publication, route calibration, or causal improvement. Audit "
        "the original pushed publication evidence. Report every excluded/NO_FORECAST request, per-competition results, and "
        "effort minutes from the event requirements/receipts alongside these scores. No model is promoted automatically.\n",
        encoding="utf-8")
    return result
