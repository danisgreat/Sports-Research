"""Append-only, hash-chained model registry with status transition rules (Improvement 26).

research/model_registry/MODEL_REGISTRY.csv records every model release state. A new state is a new row; earlier
rows never change (each row carries the hash of its predecessor). Statuses:

    RESEARCH_ONLY_NO_MODEL         a scope with research and no model (documentation of absence)
    DEVELOPMENT_EXPERIMENT         code exists; historical/synthetic checks only
    HISTORICAL_BACKTEST            evaluated on historical rows with a receipt; not prospective
    PROSPECTIVE_SHADOW             issuing frozen pre-start shadow forecasts; never on cards
    AUTHORISED_EXPERIMENTAL_PRIMARY owner-authorised primary use without predictive qualification
    PROSPECTIVELY_QUALIFIED        a prospective evaluation report reached PROMOTION_ELIGIBLE and the owner approved
    RETIRED / ROLLED_BACK          withdrawn; ROLLED_BACK names the model:version restored

No registry row changes an issued card, probability, grade or feedback row.
"""
from __future__ import annotations

import argparse
import hashlib
from datetime import datetime, timezone
from pathlib import Path

from ml import primary as p

REGISTRY = Path(__file__).resolve().parents[1] / "research" / "model_registry" / "MODEL_REGISTRY.csv"
FIELDS = ("entry", "recorded_at", "model_id", "version", "status", "scope", "generating_commit", "code_reference",
          "feature_spec", "dataset_release", "parameters", "evaluation_report", "deployment_scope", "rollback_to",
          "authority", "notes", "prev_entry_sha256", "entry_sha256")
STATUSES = ("RESEARCH_ONLY_NO_MODEL", "DEVELOPMENT_EXPERIMENT", "HISTORICAL_BACKTEST", "PROSPECTIVE_SHADOW",
            "AUTHORISED_EXPERIMENTAL_PRIMARY", "PROSPECTIVELY_QUALIFIED", "RETIRED", "ROLLED_BACK")
GENESIS = "0" * 64


def _hash(row: dict) -> str:
    return hashlib.sha256("\x1f".join(str(row[f]) for f in FIELDS[:-1]).encode()).hexdigest()


def _check(row: dict, history: list[dict], files: bool = True) -> None:
    if row["status"] not in STATUSES:
        raise p.AdmissionError("unknown registry status")
    if not row["model_id"].strip() or not row["version"].strip() or not row["scope"].strip():
        raise p.AdmissionError("model_id, version and scope are required")
    p.clock(row["recorded_at"])
    same = [h for h in history if (h["model_id"], h["version"]) == (row["model_id"], row["version"])]
    if row["status"] == "AUTHORISED_EXPERIMENTAL_PRIMARY" and not row["authority"].strip():
        raise p.AdmissionError("experimental primary use needs the owner authority reference")
    if row["status"] == "PROSPECTIVELY_QUALIFIED":
        if not any(h["status"] == "PROSPECTIVE_SHADOW" for h in same):
            raise p.AdmissionError("qualification requires an earlier PROSPECTIVE_SHADOW entry for this version")
        report = Path(row["evaluation_report"])
        if files and (not report.exists() or
                      "PROMOTION_ELIGIBLE" not in report.read_text(encoding="utf-8", errors="replace")):
            raise p.AdmissionError("qualification requires a prospective report with a PROMOTION_ELIGIBLE disposition")
        if not row["authority"].strip():
            raise p.AdmissionError("qualification requires an owner authority reference")
    if row["status"] == "ROLLED_BACK":
        target = row["rollback_to"]
        if not any(f"{h['model_id']}:{h['version']}" == target for h in history):
            raise p.AdmissionError("rollback_to must name an existing model_id:version")
    if same and same[-1]["status"] in ("RETIRED", "ROLLED_BACK") and row["status"] not in ("RETIRED", "ROLLED_BACK"):
        raise p.AdmissionError("a retired version cannot be reactivated; register a new version")


def verify(path: Path = REGISTRY) -> list[dict]:
    rows = p.read_rows(path) if Path(path).exists() else []
    if rows and tuple(rows[0]) != FIELDS:
        raise p.AdmissionError("registry columns differ from the registered schema")
    prev = GENESIS
    for i, r in enumerate(rows, 1):
        if r["entry"] != str(i) or r["prev_entry_sha256"] != prev or _hash(r) != r["entry_sha256"]:
            raise p.AdmissionError(f"registry chain broken at entry {r['entry']}")
        _check(r, rows[:i - 1], files=False)
        prev = r["entry_sha256"]
    return rows


def append(row: dict, path: Path = REGISTRY) -> dict:
    history = verify(path)
    row = {f: str(row.get(f, "")) for f in FIELDS[:-2]}
    row["entry"] = str(len(history) + 1)
    row["recorded_at"] = row["recorded_at"] or datetime.now(timezone.utc).isoformat()
    _check(row, history)
    row["prev_entry_sha256"] = history[-1]["entry_sha256"] if history else GENESIS
    row["entry_sha256"] = _hash(row)
    from ml.research_ingest import _append
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    _append(Path(path), FIELDS, [row])
    verify(path)
    return row


def current(path: Path = REGISTRY) -> dict:
    """Latest status per model_id:version."""
    out = {}
    for r in verify(path):
        out[f"{r['model_id']}:{r['version']}"] = r
    return out


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("verify")
    sub.add_parser("current")
    a = sub.add_parser("append")
    for f in FIELDS[2:-2]:
        a.add_argument("--" + f.replace("_", "-"), default="")
    args = parser.parse_args(argv)
    if args.command == "append":
        row = append({f: getattr(args, f) for f in FIELDS[2:-2]})
        print(f"entry {row['entry']}: {row['model_id']}:{row['version']} -> {row['status']}")
    elif args.command == "verify":
        print(f"registry chain intact: {len(verify())} entries")
    else:
        for key, r in current().items():
            print(f"{key:55} {r['status']:32} {r['deployment_scope']}")


if __name__ == "__main__":
    main()
