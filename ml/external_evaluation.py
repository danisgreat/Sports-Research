"""EXT-EVAL-v2: assess the first 100 fully settled eligible paired games immediately.

No minimum weeks or completed-week wait. Forecast identities stay v24.15: this changes
assessment policy, not issued probabilities. Temporal coverage remains a reported diagnostic.
"""
from pathlib import Path
import csv
import hashlib

import pandas as pd

from ml.evaluation import prospective as P, event_assessment as A

MODELS = ("SINGLE_RESEARCH:v24.15", "REFERENCE:v24.15", "BASELINE:v24.15")
FIVE = "FIVE_LANES:v24.15"
ASSESSMENT_VERSION = "EXT-EVAL-v2"
MIN_EVENTS = 100
MIN_WEEKS = 0
DELTA = 0.01
COHORT_FIELDS = ("event_id", "scheduled_start", "week", "qualified_at", "shared_decisive_contracts")


def _write(path, fields, rows):
    with Path(path).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n"); w.writeheader(); w.writerows(rows)


def _digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def evaluate(forecasts, outcomes, out, *, as_of=None, cohort=None):
    rows = P.verify_ledger(Path(forecasts))
    labels = pd.read_csv(outcomes, keep_default_na=False, dtype=str)
    if tuple(labels.columns) != P.OUTCOME_FIELDS:
        raise ValueError("effective outcomes must have the existing prospective OUTCOME_FIELDS schema")
    if labels.duplicated(["event_id", "contract_key"]).any():
        raise ValueError("provide one validated effective outcome per event/contract, not raw revision history")
    if not labels.result.isin(("WIN", "LOSS", "PUSH", "VOID", "UNRESOLVED")).all():
        raise ValueError("unknown outcome result")
    horizon = pd.Timestamp(as_of) if as_of is not None else pd.Timestamp.now(tz="UTC")
    if horizon.tzinfo is None: raise ValueError("evaluation horizon needs an offset")
    labels = labels[labels.available_at.map(lambda s: pd.Timestamp(s) <= horizon).astype(bool)].copy()
    outcomes_by_key = {(r.event_id, r.contract_key): r for r in labels.itertuples()}
    rows = [r for r in rows if r["model_id"] + ":" + r["model_version"] in set(MODELS) | {FIVE}]
    by_tag = {tag: {(r["event_id"], r["contract_key"]): r for r in rows
                    if r["model_id"] + ":" + r["model_version"] == tag and r["evidence_status"] == "PRE_START_VERIFIED"
                    and pd.Timestamp(r["issued_at"]) < pd.Timestamp(r["scheduled_start"])}
              for tag in (MODELS[0], FIVE)}
    common = set(by_tag[MODELS[0]]) & set(by_tag[FIVE])
    by_event = {}
    for key in common: by_event.setdefault(key[0], []).append(key)
    events, coverage = {}, []
    for event_id in sorted({r["event_id"] for r in rows}):
        keys = by_event.get(event_id, [])
        status = "UNPAIRED_OR_NO_COMMON_PREGAME_CONTRACT"
        if keys:
            starts = set()
            for key in keys:
                single, five = by_tag[MODELS[0]][key], by_tag[FIVE][key]
                if pd.Timestamp(single["issued_at"]) > pd.Timestamp(five["issued_at"]):
                    raise ValueError("SINGLE_RESEARCH must be frozen before FIVE_LANES")
                if any(single[k] != five[k] for k in ("competition", "endpoint", "family", "side", "line")) or pd.Timestamp(single["scheduled_start"]) != pd.Timestamp(five["scheduled_start"]):
                    raise ValueError("paired comparisons need identical scope and evidenced horizon")
                starts.add(pd.Timestamp(five["scheduled_start"]).tz_convert("UTC"))
            if len(starts) != 1: raise ValueError("one event cannot have multiple evidenced start horizons")
            settled = [outcomes_by_key.get(k) for k in keys]
            if any(r is None or r.result not in ("WIN", "LOSS", "PUSH", "VOID") for r in settled):
                status = "AWAITING_COMPLETE_SHARED_CONTRACT_SETTLEMENT"
            elif not any(r.result in ("WIN", "LOSS") for r in settled):
                status = "NO_DECISIVE_PAIR"
            else:
                start = next(iter(starts)); monday = start.normalize() - pd.Timedelta(days=start.weekday())
                events[event_id] = dict(event_id=event_id, scheduled_start=start.isoformat(), week=monday.isoformat(),
                    qualified_at=max(pd.Timestamp(r.available_at).tz_convert("UTC") for r in settled).isoformat(),
                    shared_decisive_contracts=sum(r.result in ("WIN", "LOSS") for r in settled))
                status = "ELIGIBLE_SETTLED_PAIR"
        coverage.append(dict(event_id=event_id, shared_contracts=len(keys), status=status))
    ordered = sorted(events, key=lambda k: (pd.Timestamp(events[k]["qualified_at"]), k))
    if cohort is not None:
        cohort = Path(cohort); original = pd.read_csv(cohort, dtype=str, keep_default_na=False)
        receipt_path = cohort.parent / "COHORT_RECEIPT.csv"
        if tuple(original.columns) != COHORT_FIELDS or len(original) != MIN_EVENTS or original.event_id.duplicated().any():
            raise ValueError("reuse an exact immutable first-100 cohort")
        saved = pd.read_csv(receipt_path, dtype=str, keep_default_na=False)
        if len(saved) != 1 or saved.iloc[0].get("assessment_version") != ASSESSMENT_VERSION or saved.iloc[0]["cohort_sha256"] != _digest(cohort):
            raise ValueError("frozen cohort receipt/hash differs")
        selected = original.event_id.tolist()
        if any(k not in events for k in selected):
            raise ValueError("frozen cohort has missing/revised eligibility; audit it instead of substituting games")
        if any(str(events[r.event_id][f]) != getattr(r, f) for r in original.itertuples() for f in COHORT_FIELDS):
            raise ValueError("frozen cohort qualification metadata changed; retain the original report and audit")
    else:
        selected = ordered[:MIN_EVENTS]
    ready = len(selected) == MIN_EVENTS
    selected_set = set(selected)
    selected_rows = [r for r in rows if r["event_id"] in selected_set]
    selected_labels = labels[labels.event_id.isin(selected_set)]
    weeks = len({events[k]["week"] for k in selected})
    days = len({events[k]["scheduled_start"][:10] for k in selected})
    result, breakdown = [], []
    for champion in MODELS:
        r = A.evaluate(selected_rows, selected_labels, champion, FIVE, delta=DELTA,
                       assessment_unit="EVENT", minimum_events=MIN_EVENTS)
        iv = r.get("interval", {}); log_iv = r.get("log_loss_interval", {})
        candidate_metrics = r.get("models", {}).get(FIVE, {})
        count = int(iv.get("n_events", 0))
        disposition = r["disposition"]
        if count < MIN_EVENTS: disposition = "INSUFFICIENT_EVIDENCE"
        if champion != MODELS[0] and count >= MIN_EVENTS: disposition = "SECONDARY_DIAGNOSTIC_ONLY"
        result.append(dict(champion=champion, candidate=FIVE, assessment_version=ASSESSMENT_VERSION,
            assessment_status="READY" if ready and count >= MIN_EVENTS else "COLLECTING_INSUFFICIENT_PAIRS",
            paired_events=count, settled_weeks=weeks, event_days=days, mean_brier_difference=iv.get("mean", ""),
            interval_low=iv.get("lo", ""), interval_high=iv.get("hi", ""), log_loss_difference=log_iv.get("mean", ""),
            disposition=disposition, minimum_events=MIN_EVENTS, minimum_weeks=MIN_WEEKS, minimum_effect=DELTA,
            candidate_calibration_slope=candidate_metrics.get("slope", ""), candidate_calibration_intercept=candidate_metrics.get("intercept", ""),
            candidate_coverage=candidate_metrics.get("coverage", ""), analysis_unit="EVENT", interval_assumption="INDEPENDENT_EVENTS_REQUIRES_SHARED_DATE_TEAM_DEPENDENCE_AUDIT",
            estimated_events_for_effect=r.get("events_needed", ""),
            qualification="RECOMMENDATION_ONLY_REQUIRES_DEPENDENCE_PUBLICATION_AND_ROUTE_AUDIT", reason=r.get("reason", "")))
        if isinstance(r.get("breakdown"), pd.DataFrame):
            breakdown += [dict(champion=champion, candidate=FIVE, **v) for v in r["breakdown"].to_dict("records")]
    out = Path(out); out.mkdir(parents=True, exist_ok=False)
    _write(out / "PAIRED_RESULTS.csv", tuple(result[0]), result)
    _write(out / "COHORT.csv", COHORT_FIELDS, [events[k] for k in selected])
    _write(out / "LEDGER_EVENT_COVERAGE.csv", ("event_id", "shared_contracts", "status"), coverage)
    receipt = dict(ledger_sha256=_digest(forecasts) if Path(forecasts).is_file() else "NOT_PRESENT",
        outcomes_sha256=_digest(outcomes), cohort_sha256=_digest(out / "COHORT.csv"), assessment_version=ASSESSMENT_VERSION,
        events=len(selected), eligible_settled_events=len(events), settled_weeks=weeks, minimum_weeks=0,
        decision_window="FROZEN_FIRST_100_SETTLED_EVENTS" if ready else "COLLECTING_INSUFFICIENT_PAIRS",
        assessment_ready_at=events[selected[-1]]["qualified_at"] if ready else "", evaluated_as_of=horizon.isoformat(),
        evaluator_sha256=_digest(__file__), scoring_sha256=_digest(A.__file__), settlement_validator_sha256=_digest(P.__file__),
        reused_cohort_sha256=_digest(cohort) if cohort is not None else "NONE")
    _write(out / "COHORT_RECEIPT.csv", tuple(receipt), [receipt])
    if breakdown: _write(out / "STRATA.csv", tuple(breakdown[0]), breakdown)
    (out / "README.md").write_text(
        "# Count-based external research assessment\n\n"
        "Assess immediately at 100 eligible fully settled paired games. No week minimum and no end-of-week wait. "
        "The first 100 are ordered by actual complete shared-contract settlement availability, with event ID as a deterministic tie break. "
        "Every game contributes equally after averaging its contracts; pushes/voids are not decisive trials. "
        "Use --cohort ORIGINAL/COHORT.csv to retain the exact frozen cohort on later audits. "
        "Do not expand the cohort until a favourable result appears.\n\n"
        "The 95% event t interval assumes independent games. Shared dates, teams and competitions can make that assumption weak; "
        "audit dependence, time coverage, calibration, log loss, exclusions and publication before interpreting improvement. "
        "Weeks and event days are diagnostics, never calendar eligibility gates. A READY assessment may find no advantage. "
        "No model is promoted automatically and historical model-release registrations are unchanged.\n", encoding="utf-8")
    return result
