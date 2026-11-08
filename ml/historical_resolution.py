"""Receipt-bound historical identity, literal-contract recovery and dated grade revisions.

These overlays preserve original logs and rank data. An unbound new occurrence, changed
source prefix, unknown contract or broken parent chain cannot inherit a reviewed result.
"""
from __future__ import annotations

import csv
import hashlib
from datetime import date
from pathlib import Path

BASE = "research/historical_resolution"


class HistoricalResolutionError(ValueError):
    pass


def input_paths(root):
    return [Path(root) / BASE / n for n in ("IDENTITY_BINDINGS.csv", "ROW_METADATA.csv", "ROW_REVISIONS.csv", "EVENT_DATES.csv")]


def _rows(path):
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def _sha(data):
    return hashlib.sha256(data).hexdigest()


def event_dates(root):
    """Reviewed event dates supersede incidental import/review dates, never issue times."""
    out = {}
    for r in _rows(input_paths(root)[3]):
        path = Path(root) / r["source_document"]
        if not path.is_file() or _sha(path.read_bytes()) != r["source_document_sha256"]:
            raise HistoricalResolutionError("EVENT_DATE_EVIDENCE_CHANGED")
        if r["canonical_id"] in out or not r["canonical_id"].startswith("P-"):
            raise HistoricalResolutionError("EVENT_DATE_DUPLICATE_OR_MISSING_ID")
        value = date.fromisoformat(r["event_date"]).isoformat()
        if value != r["event_date"] or not r["date_basis"]:
            raise HistoricalResolutionError("EVENT_DATE_INVALID")
        out[r["canonical_id"]] = (value, "VERIFIED_EVENT_DATE:" + r["date_basis"])
    return out


def resolved_aliases(observations, root):
    """Only aliases whose *every current heading occurrence* has a verified binding."""
    if not observations:
        return set()
    rows = _rows(input_paths(root)[0])
    approved, touched, cache, prefixes = {}, set(), {}, {}
    for r in rows:
        path = Path(root) / r["source_path"]
        if path not in cache:
            cache[path] = path.read_bytes()
        size = int(r["source_prefix_bytes"])
        if (path, size) not in prefixes:
            prefix = cache[path][:size]
            prefixes[path, size] = (len(prefix), _sha(prefix), prefix.decode("utf-8").splitlines())
        length, digest, lines = prefixes[path, size]
        if length != size or digest != r["source_prefix_sha256"]:
            raise HistoricalResolutionError(f"IDENTITY_SOURCE_CHANGED: {r['source_path']}")
        n = int(r["line_number"])
        if not 1 <= n <= len(lines) or _sha(lines[n - 1].encode()) != r["heading_sha256"]:
            raise HistoricalResolutionError("IDENTITY_HEADING_CHANGED")
        key = (r["source_path"], n, r["alias_id"], r["heading_sha256"])
        if key in approved:
            raise HistoricalResolutionError("IDENTITY_DUPLICATE_BINDING")
        if not r["canonical_id"].startswith("P-") or not r["event_key"]:
            raise HistoricalResolutionError("IDENTITY_TARGET_MISSING")
        approved[key] = r["canonical_id"]
        touched.add(r["alias_id"])
    resolved = set()
    for alias in touched:
        current = [r for r in observations if r["alias_id"] == alias]
        if current and all((r["source_path"], r["line_number"], alias, r["heading_sha256"]) in approved for r in current):
            resolved.add(alias)
    return resolved


def recover_contracts(frame, root):
    """Fill a missing literal from a hash-bound original row; never replace p or a grade."""
    out = frame.copy()
    cache = {}
    for r in _rows(input_paths(root)[1]):
        path = Path(root) / r["source_path"]
        if path not in cache:
            cache[path] = path.read_bytes().decode("utf-8").splitlines(keepends=True)
        lines = cache[path]
        block = "".join(lines[int(r["start_line"]) - 1:int(r["end_line"])]).encode()
        if _sha(block) != r["block_sha256"] or r["row_literal"] not in block.decode():
            raise HistoricalResolutionError("CONTRACT_SOURCE_CHANGED")
        if r["contract"] not in r["row_literal"].replace("**", "").replace("`", ""):
            raise HistoricalResolutionError("CONTRACT_NOT_LITERAL")
        mask = (out.card == r["canonical_id"]) & (out["rank"].astype(str) == r["rank"])
        if not mask.any() and r.get("add_if_missing") == "YES":
            recovered = {k: None for k in out.columns}
            recovered.update(card=r["canonical_id"], rank=int(r["rank"]), contract=r["contract"], event=r["event"],
                             grade="UNRESOLVED", p=float("nan"), q=float("nan"), baseline=float("nan"),
                             cohort="LEGACY_ANALYST_NOT_PRIMARY", grade_basis="HASH_BOUND_RECOVERED_SOURCE_ROW",
                             record_status="RECOVERED_HISTORICAL_RESEARCH_ROW_NOT_PRIMARY",
                             source=r["source_path"] + ":" + r["start_line"])
            out.loc[len(out)] = recovered
            mask = (out.card == r["canonical_id"]) & (out["rank"].astype(str) == r["rank"])
        if mask.sum() != 1:
            raise HistoricalResolutionError("CONTRACT_ROW_NOT_UNIQUE")
        current = out.loc[mask, "contract"].iloc[0]
        if isinstance(current, str) and current.strip() and current != r.get("replace_existing_if_matches"):
            continue  # the original rank-log text is already present; keep it literal
        out.loc[mask, "contract"] = r["contract"]
        out.loc[mask, "contract_recovery_source"] = r["source_path"] + ":" + r["start_line"]
    return out


def apply_row_revisions(frame, root):
    """Explicit (card, rank, contract) chains for the older rank-log layout."""
    out = frame.copy()
    chain, used = {}, set()
    for r in _rows(input_paths(root)[2]):
        key = (r["canonical_id"], r["rank"], r["contract"])
        if r["parent_revision"] != chain.get(key, "BASE"):
            raise HistoricalResolutionError("HISTORICAL_REVISION_PARENT")
        if (key, r["revision"]) in used:
            raise HistoricalResolutionError("HISTORICAL_DUPLICATE_REVISION")
        mask = (out.card == key[0]) & (out["rank"].astype(str) == key[1]) & (out.contract == key[2])
        if mask.sum() != 1:
            raise HistoricalResolutionError(f"HISTORICAL_REVISION_TARGET: {key}")
        if out.loc[mask, "grade"].iloc[0] != r["prior_grade"]:
            raise HistoricalResolutionError(f"HISTORICAL_PRIOR_GRADE: {key}")
        if r["sporting_grade"] not in {"WIN", "LOSS", "PUSH", "VOID", "UNRESOLVED"}:
            raise HistoricalResolutionError("HISTORICAL_GRADE")
        document = Path(root) / r["source_document"]
        if not r["effective_at"] or not document.is_file() or _sha(document.read_bytes()) != r.get("source_document_sha256"):
            raise HistoricalResolutionError("HISTORICAL_REVISION_EVIDENCE")
        out.loc[mask, "grade"] = r["sporting_grade"]
        out.loc[mask, "evidence"] = r["evidence_class"]
        out.loc[mask, "effective_revision"] = r["revision"]
        out.loc[mask, "grade_basis"] = "DATED_HISTORICAL_REVISION:" + r["source_document"]
        chain[key] = r["revision"]
        used.add((key, r["revision"]))
    return out
