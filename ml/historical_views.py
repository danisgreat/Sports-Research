"""Hash-bound recovery of historical view/contract rows flattened by the rank index.

The rank index is immutable evidence. An explicitly reviewed guard may replace its
lossy aggregate in the reporting view with source-bound rows, retaining view and tied
rank identity. These older abstention/live/alternate views stay diagnostic and cannot
become primary forecasts, model feedback or new issue-time proof.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
from pathlib import Path
import re

import pandas as pd

BASE = "research/historical_resolution"
DIAGNOSTIC_COHORTS = {"LEGACY_ABSTENTION_NOT_PRIMARY", "LEGACY_VIEW_NOT_PRIMARY"}


class HistoricalViewError(ValueError):
    pass


def input_paths(root):
    return [Path(root) / BASE / name for name in ("VIEW_AGGREGATE_GUARDS.csv", "VIEW_ROWS.csv")]


def _read(path):
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def aggregate_digest(frame):
    """Bind the exact flattened inputs being retired, including missing probabilities."""
    rows = []
    for r in frame.sort_values(["card", "rank", "contract"]).to_dict("records"):
        row = {}
        for k in ("card", "rank", "contract", "grade", "p", "q"):
            value = r.get(k)
            row[k] = None if pd.isna(value) else int(value) if k == "rank" else value
        rows.append(row)
    return hashlib.sha256(json.dumps(rows, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def apply(frame, root):
    guards, rows = map(_read, input_paths(root))
    if not guards and not rows:
        return frame
    if not guards or not rows:
        raise HistoricalViewError("VIEW_INCOMPLETE_REGISTRY")
    cards = [r["canonical_id"] for r in guards]
    if len(cards) != len(set(cards)) or set(cards) != {r["canonical_id"] for r in rows}:
        raise HistoricalViewError("VIEW_CARD_GUARD_MISMATCH")
    for guard in guards:
        old = frame[frame.card == guard["canonical_id"]]
        if old.empty or aggregate_digest(old) != guard["aggregate_sha256"]:
            raise HistoricalViewError("VIEW_AGGREGATE_CHANGED")
        if old.grade.eq("UNATTAINABLE").any():
            raise HistoricalViewError("VIEW_CANNOT_REOPEN_CLOSED_CONTRACT")
        if old.p.notna().any() or old.q.notna().any():
            raise HistoricalViewError("VIEW_AGGREGATE_HAS_PROBABILITY")
    cache, replacements, keys = {}, [], set()
    for r in rows:
        key = (r["canonical_id"], r["view_id"], r["contract_id"])
        if key in keys:
            raise HistoricalViewError("VIEW_DUPLICATE_CONTRACT")
        keys.add(key)
        path = Path(root) / r["source_path"]
        if path not in cache:
            cache[path] = path.read_bytes()
        prefix = cache[path][:int(r["source_prefix_bytes"]) ]
        if len(prefix) != int(r["source_prefix_bytes"]) or hashlib.sha256(prefix).hexdigest() != r["source_prefix_sha256"]:
            raise HistoricalViewError("VIEW_SOURCE_CHANGED")
        lines = prefix.decode("utf-8").splitlines()
        number = int(r["line_number"])
        if not 1 <= number <= len(lines):
            raise HistoricalViewError("VIEW_LINE_OUT_OF_RANGE")
        line = lines[number - 1]
        if hashlib.sha256(line.encode()).hexdigest() != r["line_sha256"] or line != r["row_literal"]:
            raise HistoricalViewError("VIEW_ROW_CHANGED")
        cells = [re.sub(r"[`*]", "", c).strip() for c in line.strip().strip("|").split("|")]
        try:
            contract, rank, grade = (cells[int(r[x])] for x in ("contract_column", "rank_column", "grade_column"))
        except (IndexError, ValueError) as exc:
            raise HistoricalViewError("VIEW_COLUMN_INVALID") from exc
        grade_match = re.match(r"^(WIN|LOSS|PUSH|VOID)\b", grade, re.I)
        if contract != r["contract"] or rank != r["rank_label"] or not grade_match or grade_match[1].upper() != r["grade"]:
            raise HistoricalViewError("VIEW_VALUE_NOT_LITERAL")
        if r["cohort"] not in DIAGNOSTIC_COHORTS or not re.fullmatch(r"\d+[=*]?", rank):
            raise HistoricalViewError("VIEW_ROLE_OR_RANK_INVALID")
        if not r["view_id"].startswith(r["canonical_id"] + "/") or not r["contract_id"]:
            raise HistoricalViewError("VIEW_ID_INVALID")
        old = frame[frame.card == r["canonical_id"]].iloc[0]
        new = {k: None for k in frame.columns}
        new.update(card=r["canonical_id"], rank=int(re.match(r"\d+", rank)[0]), contract=contract,
                   event=old["event"], grade=r["grade"], literal_grade=r["grade"], p=math.nan, q=math.nan,
                   baseline=math.nan, record_status="RETAINED_LEGACY_VIEW_DIAGNOSTIC_NOT_PRIMARY",
                   grade_basis="HASH_BOUND_VIEW_CONTRACT_ROW", cohort=r["cohort"],
                   source=r["source_path"] + ":" + r["line_number"], view_id=r["view_id"],
                   contract_id=r["contract_id"], rank_label=rank, rank_tied="=" in rank,
                   issued_verdict=r["issued_verdict"], historical_eligibility=r["historical_eligibility"],
                   reporting_resolution="RESOLVED_VIEW_AND_CONTRACT_IDENTITY")
        replacements.append(new)
    return pd.concat([frame[~frame.card.isin(cards)], pd.DataFrame(replacements)], ignore_index=True)
