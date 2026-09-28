#!/usr/bin/env python3
"""Strict joins from a human ledger to versioned, semantically valid prospective evidence.

Markdown eligibility labels are declarations, not proof. This module checks the referenced JSON
record and its source/time/baseline semantics, then joins every scored value back to that record.
It intentionally fails closed: any missing, duplicated or mismatched key is excluded with reasons.
"""
from __future__ import annotations

import json
import hashlib
import re
import unicodedata
from pathlib import Path

import semantic_validation as sv

REPO = Path(__file__).resolve().parent.parent
DEFAULT_RECORDS = REPO / "research" / "settled_rows_2026-09-28" / "prospective_records.json"
TOL = 1e-9


def _contract_key(value: str) -> str:
    value = unicodedata.normalize("NFKC", re.sub(r"[*`]", "", value or "")).casefold()
    value = value.translate(str.maketrans({"−": "-", "–": "-", "—": "-"}))
    return " ".join(value.split())


def verified_records(path: Path = DEFAULT_RECORDS) -> tuple[dict[str, dict], dict[str, list[str]]]:
    """Return verified records by decision ID and blocked decision IDs with exact reasons."""
    try:
        doc = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError):
        return {}, {"<document>": ["PROSPECTIVE_RECORDS_MISSING_OR_INVALID_JSON"]}
    if not isinstance(doc, dict) or doc.get("schema_version") != 1 or not isinstance(doc.get("records"), list):
        return {}, {"<document>": ["PROSPECTIVE_RECORDS_SCHEMA_INVALID"]}

    counts: dict[str, int] = {}
    for row in doc["records"]:
        if isinstance(row, dict) and isinstance(row.get("decision_id"), str):
            counts[row["decision_id"]] = counts.get(row["decision_id"], 0) + 1

    accepted: dict[str, dict] = {}
    blocked: dict[str, list[str]] = {}
    for i, row in enumerate(doc["records"]):
        if not isinstance(row, dict):
            blocked[f"<records[{i}]>"] = ["RECORD_NOT_AN_OBJECT"]
            continue
        decision = row.get("decision_id")
        if not isinstance(decision, str) or not decision.strip():
            blocked[f"<records[{i}]>"] = ["DECISION_ID_MISSING"]
            continue
        reasons = []
        if counts.get(decision, 0) != 1:
            reasons.append("DUPLICATE_DECISION_ID")
        reasons.extend(sv.validate_record(row, f"{decision}"))
        reasons.extend(sv.performance_blockers(row))
        if reasons:
            blocked[decision] = sorted(set(reasons))
        else:
            accepted[decision] = row
    return accepted, blocked


def join_binary_baseline_rows(rows: list[dict], records_path: Path = DEFAULT_RECORDS
                              ) -> tuple[list[dict], dict[str, list[str]]]:
    """Join only explicit eligible, exact binary decisions to verified pregame JSON records.

    The C-BASELINE-SKILL ledger is currently a binary diagnostic. Push/void mass is therefore not
    discarded here: push-capable records need a future vector-aware baseline ledger and stay out.
    """
    records, blocked = verified_records(records_path)
    joined, failures = [], dict(blocked)
    seen: set[str] = set()
    for row in rows:
        if row.get("section") != "prospective":
            continue
        decision = row.get("decision", "")
        if row.get("eligible") is not True:
            failures[decision or "<ledger-row>"] = ["LEDGER_ROW_NOT_EXPLICITLY_ELIGIBLE"]
            continue
        if not row.get("eligibility_receipt") or row["eligibility_receipt"] != f"prospective_records.json#{decision}":
            failures[decision or "<ledger-row>"] = ["LEDGER_ELIGIBILITY_RECEIPT_DOES_NOT_RESOLVE_TO_RECORD"]
            continue
        record = records.get(decision)
        if record is None:
            failures.setdefault(decision or "<ledger-row>", []).append("VERIFIED_STRUCTURED_RECORD_MISSING")
            continue
        reasons = []
        probs = record.get("probabilities", {})
        baseline = record.get("baseline", {})
        if record.get("card_id") != row.get("card"):
            reasons.append("LEDGER_CARD_ID_MISMATCH")
        if record.get("rank") != row.get("rank"):
            reasons.append("LEDGER_RANK_MISMATCH")
        if _contract_key(record.get("contract", "")) != _contract_key(row.get("contract", "")):
            reasons.append("LEDGER_CONTRACT_MISMATCH")
        if record.get("result") != row.get("result"):
            reasons.append("LEDGER_RESULT_MISMATCH")
        if not isinstance(probs, dict) or set(probs) not in ({"W", "P", "L"}, {"W", "P", "L", "V"}):
            reasons.append("LEDGER_REQUIRES_COMPLETE_OUTCOME_VECTOR")
        elif probs.get("P", 0.0) > sv.TOL or probs.get("V", 0.0) > sv.TOL:
            reasons.append("PUSH_OR_VOID_VECTOR_REQUIRES_VECTOR_AWARE_LEDGER")
        else:
            expected_p = probs.get("W")
            actual_p = row.get("p")
            if (not isinstance(expected_p, (int, float)) or not isinstance(actual_p, (int, float))
                    or abs(expected_p - actual_p) > TOL):
                reasons.append("LEDGER_CARD_PROBABILITY_MISMATCH")
        expected_baseline = baseline.get("p") if isinstance(baseline, dict) else None
        actual_baseline = row.get("b")
        if (not isinstance(expected_baseline, (int, float)) or not isinstance(actual_baseline, (int, float))
                or abs(expected_baseline - actual_baseline) > TOL):
            reasons.append("LEDGER_BASELINE_PROBABILITY_MISMATCH")
        if record.get("preferred_at_issue") is not True:
            reasons.append("LEDGER_ROW_NOT_FROZEN_PREFERRED_DECISION")
        if decision in seen:
            reasons.append("DUPLICATE_LEDGER_DECISION")
        seen.add(decision)
        if reasons:
            failures[decision] = sorted(set(reasons))
        else:
            joined.append({**row, "event_cluster_id": record["event_cluster_id"], "verified_record": record})
    return joined, failures


def rm1_blockers(record: dict) -> list[str]:
    """Validate q against the shipped RM-1 code/coefficients for a prospective no-push row."""
    reasons = []
    if record.get("ranking_model_version") != "RM-1":
        reasons.append("RM1_MODEL_VERSION_MISSING_OR_MISMATCHED")
    coefficient_path = REPO / "tools" / "rank_model_coefficients.json"
    try:
        digest = hashlib.sha256(coefficient_path.read_bytes()).hexdigest()
    except OSError:
        digest = ""
    if record.get("ranking_model_sha256") != digest or not digest:
        reasons.append("RM1_COEFFICIENT_HASH_DOES_NOT_MATCH_SHIPPED_BUILD")
    code_path = REPO / "tools" / "rank_model.py"
    try:
        code_digest = hashlib.sha256(code_path.read_bytes()).hexdigest()
    except OSError:
        code_digest = ""
    if record.get("ranking_model_code_sha256") != code_digest or not code_digest:
        reasons.append("RM1_CODE_HASH_DOES_NOT_MATCH_SHIPPED_BUILD")
    probabilities = record.get("probabilities")
    if not isinstance(probabilities, dict):
        return reasons + ["RM1_PROBABILITY_VECTOR_MISSING"]
    if probabilities.get("P", 0.0) > sv.TOL or probabilities.get("V", 0.0) > sv.TOL:
        reasons.append("RM1_PUSH_CONDITIONING_UNVALIDATED")
    if record.get("q_semantics") != "ROW_CALIBRATED_NOT_JOINT":
        reasons.append("RM1_Q_SEMANTICS_MISMATCHED")
    try:
        import rank_model as rm
        coef = rm.load_coef(coefficient_path)
        expected = rm.score_row(coef, record.get("sport", ""), record.get("contract", ""), probabilities["W"])["q"]
        actual = record.get("q")
        if not isinstance(actual, (int, float)) or abs(expected - actual) > 0.0005000001:
            reasons.append("RM1_Q_DOES_NOT_REPRODUCE_FROM_FROZEN_BUILD")
    except (KeyError, TypeError, ValueError, OSError):
        reasons.append("RM1_Q_REPRODUCTION_FAILED")
    return reasons
