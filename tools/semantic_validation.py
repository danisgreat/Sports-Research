#!/usr/bin/env python3
"""Semantic checks for versioned forecast and settlement records.

This validates relationships that a presence-only card checker cannot establish. It never
repairs, projects, or fills a probability. Rows failing an identity, timing, distribution,
source-lineage, or settlement check are returned as failures and must not enter a score.
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

TOL = 1e-8
HASH_RE = re.compile(r"^[0-9a-f]{64}$", re.I)
TIERS = {"COIN_FLIP": 0, "LEAN": 1, "SUPPORTED": 2, "STRONG": 3}
TOP2_LABELS = {"TOP2_COIN_FLIP": 0, "TOP1_ONLY": 1, "TOP2_SUPPORTED": 2, "TOP2_STRONG": 3}
REQUIRED = {
    "schema_version", "event_id", "event_cluster_id", "forecast_id", "card_id", "decision_id",
    "target_id", "contract_id", "contract", "contract_spec", "sport", "competition", "season", "participant_ids",
    "rank", "horizon", "input_cutoff_utc", "input_availability_latest_utc", "issued_at_utc", "event_start_utc",
    "distribution_id", "distribution_type", "distribution_sha256", "probabilities", "q", "q_semantics", "baseline",
    "method_version", "method_sha256", "control_sha256", "manifest_sha256", "ranking_model_version",
    "ranking_model_sha256", "ranking_model_code_sha256", "settlement_revision_id", "observed_value", "result",
    "outcome_verified", "issue_receipts", "terminal_receipts", "preferred_at_issue", "selection_policy_version",
    "complementary_pair_id", "covering_pair_id", "target_weight", "missingness",
}


def _finite_probability(v: Any) -> bool:
    return isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(v) and 0 <= v <= 1


def _utc(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        d = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if d.tzinfo is None or d.utcoffset() is None:
        return None
    return d


def score_wpl_brier(probabilities: dict[str, float], outcome: str) -> float:
    """Half-scaled categorical Brier for a complete, declared W/P/L(/V) vector."""
    keys = tuple(probabilities)
    if set(keys) not in ({"W", "P", "L"}, {"W", "P", "L", "V"}):
        raise ValueError("probabilities must declare W/P/L, optionally with V")
    if outcome not in probabilities:
        raise ValueError("outcome is outside the declared probability categories")
    if any(not _finite_probability(v) for v in probabilities.values()):
        raise ValueError("probabilities must be finite values from 0 to 1")
    if abs(sum(probabilities.values()) - 1.0) > TOL:
        raise ValueError("probability mass must sum to 1")
    return 0.5 * sum((probabilities[k] - (1.0 if k == outcome else 0.0)) ** 2 for k in keys)


def score_decisive_brier(probabilities: dict[str, float], outcome: str) -> float:
    """Binary Brier conditional on a decisive W/L outcome; never silently removes push mass."""
    if outcome not in ("W", "L"):
        raise ValueError("decisive-direction score is defined only for W/L")
    decisive = probabilities.get("W", 0.0) + probabilities.get("L", 0.0)
    if decisive <= TOL:
        raise ValueError("decisive probability is zero")
    p = probabilities.get("W", 0.0) / decisive
    return (p - (1.0 if outcome == "W" else 0.0)) ** 2


def performance_blockers(record: dict[str, Any]) -> list[str]:
    """Return explicit reasons this row cannot count in a prospective pregame comparison."""
    reasons: list[str] = []
    if record.get("horizon") != "PREGAME":
        reasons.append("HORIZON_NOT_VERIFIED_PREGAME")
    cutoff, available, issued, start = (_utc(record.get(k)) for k in
                                       ("input_cutoff_utc", "input_availability_latest_utc", "issued_at_utc", "event_start_utc"))
    if cutoff is None or available is None or issued is None or start is None:
        reasons.append("TIMESTAMPS_MISSING_OR_NOT_TIMEZONED")
    else:
        if available > cutoff:
            reasons.append("INPUT_NOT_AVAILABLE_BY_FROZEN_CUTOFF")
        if cutoff > issued:
            reasons.append("INPUT_CUTOFF_AFTER_ISSUE")
        if issued >= start:
            reasons.append("ISSUED_AT_OR_AFTER_EVENT_START")
    if not isinstance(record.get("event_id"), str) or not record["event_id"].strip():
        reasons.append("EVENT_ID_MISSING")
    if not isinstance(record.get("target_id"), str) or not record["target_id"].strip():
        reasons.append("TARGET_ID_MISSING")
    p = record.get("probabilities")
    if not isinstance(p, dict) or set(p) not in ({"W", "P", "L"}, {"W", "P", "L", "V"}):
        reasons.append("COMPLETE_OUTCOME_VECTOR_MISSING")
    elif any(not _finite_probability(v) for v in p.values()) or abs(sum(p.values()) - 1.0) > TOL:
        reasons.append("OUTCOME_VECTOR_INVALID")
    if record.get("q") is None or not _finite_probability(record.get("q")):
        reasons.append("RM1_Q_MISSING_OR_INVALID")
    if not record.get("q_semantics"):
        reasons.append("Q_INTERPRETATION_UNDECLARED")
    if record.get("preferred_at_issue") is not True:
        reasons.append("PREFERRED_DECISION_NOT_EXPLICITLY_FROZEN")
    for key in ("method_sha256", "control_sha256", "manifest_sha256", "distribution_sha256",
                "ranking_model_sha256", "ranking_model_code_sha256"):
        if not isinstance(record.get(key), str) or not HASH_RE.fullmatch(record[key]):
            reasons.append(key.upper() + "_MISSING_OR_INVALID")
    if record.get("ranking_model_version") != "RM-1":
        reasons.append("RM1_MODEL_VERSION_MISSING_OR_MISMATCHED")
    if not isinstance(record.get("ranking_model_sha256"), str) or not HASH_RE.fullmatch(record["ranking_model_sha256"]):
        reasons.append("RANKING_MODEL_SHA256_MISSING_OR_INVALID")
    if not isinstance(record.get("ranking_model_code_sha256"), str) or not HASH_RE.fullmatch(record["ranking_model_code_sha256"]):
        reasons.append("RANKING_MODEL_CODE_SHA256_MISSING_OR_INVALID")
    if record.get("outcome_verified") is not True:
        reasons.append("TERMINAL_OUTCOME_NOT_VERIFIED")
    receipts = record.get("terminal_receipts")
    if not isinstance(receipts, list):
        receipts = []
    valid_receipts = [r for r in receipts if isinstance(r, dict)
                      and r.get("event_id") == record.get("event_id")
                      and r.get("terminal") is True
                      and isinstance(r.get("lineage_id"), str) and r.get("lineage_id")
                      and isinstance(r.get("sha256"), str) and HASH_RE.fullmatch(r["sha256"])
                      and isinstance(r.get("source_ref"), str) and r.get("source_ref")
                      and isinstance(r.get("observed_at_utc"), str) and _utc(r.get("observed_at_utc")) is not None
                      and isinstance(r.get("fields"), dict)
                      and r["fields"].get("event_id") == record.get("event_id")
                      and r["fields"].get("result") == record.get("result")
                      and r["fields"].get("terminal_status") in ("FINAL", "COMPLETE")]
    if len({r["lineage_id"] for r in valid_receipts}) < 3:
        reasons.append("FEWER_THAN_THREE_INDEPENDENT_TERMINAL_LINEAGES")
    if start is not None and any(_utc(r["observed_at_utc"]) < start for r in valid_receipts):
        reasons.append("TERMINAL_SOURCE_OBSERVED_BEFORE_EVENT_START")
    issue_receipts = record.get("issue_receipts")
    if not isinstance(issue_receipts, list):
        issue_receipts = []
    valid_issue = [r for r in issue_receipts if isinstance(r, dict)
                   and r.get("event_id") == record.get("event_id")
                   and isinstance(r.get("lineage_id"), str) and r.get("lineage_id")
                   and isinstance(r.get("observed_at_utc"), str) and _utc(r.get("observed_at_utc")) is not None
                   and isinstance(r.get("sha256"), str) and HASH_RE.fullmatch(r["sha256"])
                   and isinstance(r.get("source_ref"), str) and r.get("source_ref")
                   and isinstance(r.get("fields"), dict)
                   and r["fields"].get("event_id") == record.get("event_id")
                   and r["fields"].get("event_state") == "PREGAME"
                   and r["fields"].get("event_start_utc") == record.get("event_start_utc")]
    if len({r["lineage_id"] for r in valid_issue}) < 3:
        reasons.append("FEWER_THAN_THREE_INDEPENDENT_ISSUE_LINEAGES")
    elif cutoff is not None and any(_utc(r["observed_at_utc"]) > cutoff for r in valid_issue):
        reasons.append("ISSUE_SOURCE_OBSERVED_AFTER_FROZEN_CUTOFF")
    baseline = record.get("baseline")
    if not isinstance(baseline, dict) or baseline.get("status") != "FROZEN_VALID":
        reasons.append("MATCHED_FROZEN_BASELINE_MISSING")
    elif not _finite_probability(baseline.get("p")):
        reasons.append("BASELINE_PROBABILITY_MISSING_OR_INVALID")
    else:
        for field in ("event_id", "target_id", "contract_id", "horizon", "input_cutoff_utc"):
            if baseline.get(field) != record.get(field):
                reasons.append("BASELINE_" + field.upper() + "_MISMATCH")
        baseline_cutoff = _utc(baseline.get("training_cutoff_utc"))
        if baseline_cutoff is None or (cutoff is not None and baseline_cutoff > cutoff):
            reasons.append("BASELINE_TRAINING_CUTOFF_MISSING_OR_AFTER_INPUT_CUTOFF")
        if not baseline.get("version"):
            reasons.append("BASELINE_VERSION_MISSING")
    return reasons


def validate_record(record: dict[str, Any], where: str = "record") -> list[str]:
    errors: list[str] = []
    missing = sorted(REQUIRED - set(record))
    if missing:
        errors.append(f"{where}: missing schema fields: {', '.join(missing)}")
    for key in ("event_id", "event_cluster_id", "forecast_id", "card_id", "decision_id", "target_id",
                "contract_id", "contract", "sport", "competition", "season", "distribution_id",
                "distribution_type", "method_version", "settlement_revision_id", "selection_policy_version"):
        if key in record and (not isinstance(record[key], str) or not record[key].strip()):
            errors.append(f"{where}: {key} must be a nonempty string")
    if record.get("schema_version") != 1:
        errors.append(f"{where}: unsupported schema_version")
    rank = record.get("rank")
    if not isinstance(rank, int) or isinstance(rank, bool) or rank < 1:
        errors.append(f"{where}: rank must be a positive integer")
    participants = record.get("participant_ids")
    if (not isinstance(participants, list) or len(participants) < 2
            or any(not isinstance(x, str) or not x.strip() for x in participants)
            or len(set(participants)) != len(participants)):
        errors.append(f"{where}: participant_ids must contain at least two distinct nonempty official IDs")
    spec = record.get("contract_spec")
    spec_fields = ("measure", "period", "line", "side", "units", "overtime_rule", "draw_rule",
                   "push_rule", "void_rule", "action_rule", "contract_version")
    if not isinstance(spec, dict) or any(k not in spec for k in spec_fields):
        errors.append(f"{where}: contract_spec must declare measure, period, line, side, units, overtime/draw/push/void/action rules and contract_version")
    elif any(not isinstance(spec[k], str) or not spec[k].strip() for k in spec_fields if k != "line"):
        errors.append(f"{where}: contract terms and contract_version must be explicit nonempty strings")
    elif spec["line"] is not None and (not isinstance(spec["line"], (int, float))
                                       or isinstance(spec["line"], bool) or not math.isfinite(spec["line"])):
        errors.append(f"{where}: contract_spec.line must be a finite number or null")
    weight = record.get("target_weight")
    if not isinstance(weight, (int, float)) or isinstance(weight, bool) or not math.isfinite(weight) or weight <= 0:
        errors.append(f"{where}: target_weight must be finite and positive")
    p = record.get("probabilities")
    if not isinstance(p, dict) or set(p) not in ({"W", "P", "L"}, {"W", "P", "L", "V"}):
        errors.append(f"{where}: probabilities must explicitly declare W/P/L, optionally V")
    elif any(not _finite_probability(v) for v in p.values()) or abs(sum(p.values()) - 1) > TOL:
        errors.append(f"{where}: probability vector is invalid or does not sum to 1")
    result = record.get("result")
    if result not in ("W", "P", "L", "V", "UNRESOLVED"):
        errors.append(f"{where}: invalid result category")
    elif result != "UNRESOLVED" and isinstance(p, dict) and result not in p:
        errors.append(f"{where}: result category is absent from the declared probability vector")
    q = record.get("q")
    if q is not None and not _finite_probability(q):
        errors.append(f"{where}: q must be null or a finite value from 0 to 1")
    if record.get("q_semantics") not in ("ROW_CALIBRATED_NOT_JOINT", "MARGINAL_EVENT_PROBABILITY", "RANKING_SCORE", "UNKNOWN"):
        errors.append(f"{where}: q_semantics is undeclared or invalid")
    for key in ("method_sha256", "control_sha256", "manifest_sha256", "distribution_sha256",
                "ranking_model_sha256", "ranking_model_code_sha256"):
        value = record.get(key)
        if value is not None and (not isinstance(value, str) or not HASH_RE.fullmatch(value)):
            errors.append(f"{where}: {key} is not a SHA-256 hex digest")
    horizon = record.get("horizon")
    if horizon not in ("PREGAME", "LIVE_ISSUED", "POST_START", "UNKNOWN"):
        errors.append(f"{where}: invalid horizon")
    for key in ("input_cutoff_utc", "input_availability_latest_utc", "issued_at_utc", "event_start_utc"):
        value = record.get(key)
        if value is not None and _utc(value) is None:
            errors.append(f"{where}: {key} must be null or an ISO-8601 timestamp with a timezone")
    if record.get("outcome_verified") is True and result in (None, "UNRESOLVED"):
        errors.append(f"{where}: verified outcome cannot be unresolved")
    if record.get("result") not in (None, "UNRESOLVED") and record.get("outcome_verified") is not True:
        errors.append(f"{where}: scored result must be explicitly verified")
    if record.get("outcome_verified") is True and record.get("observed_value") is None:
        errors.append(f"{where}: verified outcome requires observed_value")
    if record.get("ranking_model_version") == "RM-1" and record.get("q_semantics") != "ROW_CALIBRATED_NOT_JOINT":
        errors.append(f"{where}: RM-1 q must be declared ROW_CALIBRATED_NOT_JOINT")
    return errors


def validate_document(document: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if document.get("schema_version") != 1:
        errors.append("document: schema_version must be 1")
    records = document.get("records")
    if not isinstance(records, list):
        return errors + ["document: records must be an array"]
    collections = {}
    for name in ("complements", "geometry", "nested_events", "distributions", "rankings"):
        value = document.get(name, [])
        if not isinstance(value, list):
            errors.append(f"document: {name} must be an array")
            value = []
        collections[name] = value
    seen_decisions: set[tuple[str, str]] = set()
    records_by_id: dict[str, dict[str, Any]] = {}
    for i, record in enumerate(records):
        if not isinstance(record, dict):
            errors.append(f"records[{i}]: must be an object")
            continue
        errors.extend(validate_record(record, f"records[{i}]") )
        if isinstance(record.get("decision_id"), str):
            records_by_id[record["decision_id"]] = record
        key = (str(record.get("forecast_id", "")), str(record.get("decision_id", "")))
        if all(key) and key in seen_decisions:
            errors.append(f"records[{i}]: duplicate forecast_id/decision_id")
        seen_decisions.add(key)
    for i, pair in enumerate(collections["complements"]):
        label = f"complements[{i}]"
        if not isinstance(pair, dict):
            errors.append(f"{label}: must be an object")
            continue
        left = records_by_id.get(pair.get("left_decision_id"))
        right = records_by_id.get(pair.get("right_decision_id"))
        if left is None or right is None:
            errors.append(f"{label}: both decision IDs must resolve to records")
            continue
        if left.get("target_id") != right.get("target_id"):
            errors.append(f"{label}: complementary contracts must share one target_id")
            continue
        for field in ("event_id", "event_cluster_id", "forecast_id", "horizon", "input_cutoff_utc"):
            if left.get(field) != right.get(field):
                errors.append(f"{label}: complementary contracts disagree on {field}")
                break
        lp, rp = left.get("probabilities"), right.get("probabilities")
        if not isinstance(lp, dict) or not isinstance(rp, dict) or set(lp) != set(rp):
            errors.append(f"{label}: complementary outcome vectors must have the same declared categories")
            continue
        if any(not _finite_probability(v) for v in list(lp.values()) + list(rp.values())):
            errors.append(f"{label}: complementary outcome vectors contain invalid values")
            continue
        for a_cat, b_cat in (("W", "L"), ("L", "W"), ("P", "P"), ("V", "V")):
            if a_cat in lp and abs(lp[a_cat] - rp[b_cat]) > TOL:
                errors.append(f"{label}: complement/push identity fails for {a_cat}/{b_cat}")
                break
    for i, pair in enumerate(collections["geometry"]):
        label = f"geometry[{i}]"
        if not isinstance(pair, dict):
            errors.append(f"{label}: must be an object")
            continue
        vals = [pair.get(k) for k in ("p_left", "p_right", "p_intersection")]
        if any(not _finite_probability(v) for v in vals):
            errors.append(f"{label}: marginal and intersection probabilities must be finite values from 0 to 1")
            continue
        a, b, joint = vals
        if pair.get("semantics") != "MARGINAL_EVENT_PROBABILITY":
            errors.append(f"{label}: event geometry cannot be tested using row scores or unlabelled q values")
            continue
        if joint + TOL < max(0.0, a + b - 1.0) or joint - TOL > min(a, b):
            errors.append(f"{label}: intersection violates Fréchet bounds")
        if pair.get("union_covers") is True and abs(a + b - joint - 1.0) > TOL:
            errors.append(f"{label}: covering pair union probability must equal 1")
    for i, pair in enumerate(collections["nested_events"]):
        if not isinstance(pair, dict) or any(not _finite_probability(pair.get(k)) for k in ("p_inner", "p_outer")):
            errors.append(f"nested_events[{i}]: invalid probability")
        elif pair["p_inner"] > pair["p_outer"] + TOL:
            errors.append(f"nested_events[{i}]: inner event probability exceeds its outer event")
    for i, dist in enumerate(collections["distributions"]):
        label = f"distributions[{i}]"
        if not isinstance(dist, dict) or not isinstance(dist.get("states"), list) or not dist["states"]:
            errors.append(f"{label}: states must be a nonempty array")
            continue
        if any(not isinstance(s, dict) for s in dist["states"]):
            errors.append(f"{label}: every state must be an object")
            continue
        ids = [s.get("id") for s in dist["states"]]
        masses = [s.get("mass") for s in dist["states"]]
        if (len(ids) != len(dist["states"])
                or any(not isinstance(x, str) or not x for x in ids)
                or len(set(x for x in ids if isinstance(x, str))) != len(ids)):
            errors.append(f"{label}: state IDs must be present and unique")
        if any(not _finite_probability(m) for m in masses) or abs(sum(masses) - 1.0) > TOL:
            errors.append(f"{label}: state masses must be nonnegative and sum to 1")
            continue
        for j, state in enumerate(dist["states"]):
            if "home_score" not in state and "away_score" not in state:
                continue
            hs, aws = state.get("home_score"), state.get("away_score")
            if (not isinstance(hs, int) or isinstance(hs, bool) or hs < 0
                    or not isinstance(aws, int) or isinstance(aws, bool) or aws < 0):
                errors.append(f"{label}.states[{j}]: home/away scores must be nonnegative integers")
                continue
            if "total" in state and state["total"] != hs + aws:
                errors.append(f"{label}.states[{j}]: total does not equal home_score + away_score")
            if "margin" in state:
                if dist.get("margin_convention") != "HOME_MINUS_AWAY":
                    errors.append(f"{label}: margin_convention must be declared before checking score/margin identity")
                elif state["margin"] != hs - aws:
                    errors.append(f"{label}.states[{j}]: margin does not equal home_score - away_score")
            if hs == aws and dist.get("ties_allowed") is False:
                errors.append(f"{label}.states[{j}]: tie state is invalid for a no-tie endpoint")
        by_id = dict(zip(ids, masses))
        queries = dist.get("queries", [])
        if not isinstance(queries, list):
            errors.append(f"{label}: queries must be an array")
            continue
        for j, query in enumerate(queries):
            if not isinstance(query, dict):
                errors.append(f"{label}.queries[{j}]: query must be an object")
                continue
            match = query.get("matching_state_ids", [])
            if not isinstance(match, list) or any(x not in by_id for x in match):
                errors.append(f"{label}.queries[{j}]: query references unknown state IDs")
                continue
            expected = query.get("p")
            actual = sum(by_id[x] for x in match)
            if not _finite_probability(expected) or abs(actual - expected) > TOL:
                errors.append(f"{label}.queries[{j}]: printed probability does not reproduce from the frozen distribution")
    for i, slate in enumerate(collections["rankings"]):
        label = f"rankings[{i}]"
        if not isinstance(slate, dict) or not isinstance(slate.get("rows"), list):
            errors.append(f"{label}: rows must be an array")
            continue
        rows = slate["rows"]
        if any(not isinstance(r, dict) for r in rows):
            errors.append(f"{label}: every rank row must be an object")
            continue
        if any(not isinstance(r.get("rank"), int) or isinstance(r.get("rank"), bool) for r in rows):
            errors.append(f"{label}: each rank must be an integer")
            continue
        sorted_rows = sorted(rows, key=lambda r: r["rank"])
        if [r.get("rank") for r in sorted_rows] != list(range(1, len(sorted_rows) + 1)):
            errors.append(f"{label}: ranks must be unique, consecutive integers from 1")
        effective = []
        for row in sorted_rows:
            qv = row.get("q")
            raw_flags = row.get("flags", [])
            if not isinstance(raw_flags, list) or any(not isinstance(flag, str) for flag in raw_flags):
                errors.append(f"{label}: flags must be an array of strings")
                raw_flags = []
            flags = set(raw_flags)
            qsort = qv
            if "NEAR_TIED_FLIP" in flags:
                if row.get("ordering_exception") != "NEAR_TIED_FLIP_STATED_SIDE" or not _finite_probability(qv) or abs(qv - 0.5) > 0.05 + TOL:
                    errors.append(f"{label}: near-tied flip lacks its named, bounded ordering exception")
                p = row.get("p")
                if not _finite_probability(p):
                    errors.append(f"{label}: near-tied flip is missing issued p")
                else:
                    qsort = 0.501 if p > 0.5 else 0.499
            elif not _finite_probability(qv):
                errors.append(f"{label}: each rank row needs q")
            if "SIDE_FLIP" in flags and row.get("tier") == "STRONG":
                errors.append(f"{label}: a side-flipped row cannot retain STRONG tier")
            effective.append((qsort if _finite_probability(qsort) else -1, row))
        expected = sorted(effective, key=lambda x: (-x[0],
                                                   x[1].get("stated_rank") if isinstance(x[1].get("stated_rank"), int)
                                                   and not isinstance(x[1].get("stated_rank"), bool) else 10**9))
        if [r.get("contract_id") for _, r in expected] != [r.get("contract_id") for r in sorted_rows]:
            errors.append(f"{label}: order does not follow q plus the declared near-tie exception")
        if len(sorted_rows) >= 2:
            tiers = [TIERS.get(r.get("tier"), -1) for r in sorted_rows[:2]]
            if min(tiers) == 3:
                want = "TOP2_STRONG"
            elif min(tiers) >= 2:
                want = "TOP2_SUPPORTED"
            elif tiers[0] >= 2:
                want = "TOP1_ONLY"
            else:
                want = "TOP2_COIN_FLIP"
            if slate.get("top_two_label") != want:
                errors.append(f"{label}: TOP2 label ignores an effective tier cap; expected {want}")
            joint_p = slate.get("both_win_probability")
            if joint_p is not None:
                if not _finite_probability(joint_p):
                    errors.append(f"{label}: joint-success probability must be between 0 and 1")
                if not isinstance(slate.get("joint_model_id"), str) or not slate["joint_model_id"].strip():
                    errors.append(f"{label}: joint-success probability requires a coherent joint_model_id")
            product = slate.get("independence_product_claim")
            if product is not None:
                if not _finite_probability(product):
                    errors.append(f"{label}: independence product claim must be between 0 and 1")
                if not isinstance(slate.get("independence_basis"), str) or not slate["independence_basis"].strip():
                    errors.append(f"{label}: q product is not a joint estimate without an explicit independence basis")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="JSON object with schema_version and records")
    args = parser.parse_args(argv)
    try:
        doc = json.loads(args.path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    if not isinstance(doc, dict):
        print("ERROR: document root must be an object", file=sys.stderr)
        return 2
    errors = validate_document(doc)
    for error in errors:
        print("ERROR: " + error)
    if errors:
        print(f"INVALID: {len(errors)} semantic error(s); no rows should be scored")
        return 1
    print(f"VALID: {len(doc['records'])} record(s); semantics pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
