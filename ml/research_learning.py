"""Retain verified research-only settlement labels for future model development.

These targets are NOT frozen expert feedback, prospective forecasts or automatic
training admission. Features, timing, scope and effective revisions need review.
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path
import re
import secrets
from datetime import datetime, timezone

from ml import primary as p


LABEL_FIELDS = ("event_id", "competition", "endpoint", "label_key", "label_value", "label_unit",
                "event_at", "final_at", "available_at", "source_url", "evidence_path", "evidence_sha256",
                "definition_status", "review_status", "revision_id", "feature_status")
KIND = "RESEARCH_TRAINING_CANDIDATE"


def validate_labels(rows: list[dict]) -> None:
    if not rows or any(set(row) != set(LABEL_FIELDS) for row in rows):
        raise p.AdmissionError("exact nonempty research label schema required; no extra/market columns")
    identities = {(r["event_id"], r["competition"], r["endpoint"], r["revision_id"]) for r in rows}
    if len(identities) != 1 or any(not str(value).strip() for value in next(iter(identities))):
        raise p.AdmissionError("one exact event/scope/effective settlement revision per candidate")
    keys = [r["label_key"] for r in rows]
    if len(keys) != len(set(keys)) or any(not k.strip() for k in keys):
        raise p.AdmissionError("unique nonempty settlement label keys required")
    for r in rows:
        if not p.clock(r["event_at"]) <= p.clock(r["final_at"]) <= p.clock(r["available_at"]):
            raise p.AdmissionError("label event/final/availability chronology invalid")
        if p.clock(r["available_at"]) > datetime.now(timezone.utc):
            raise p.AdmissionError("future terminal label is not available for retention yet")
        if r["review_status"] != "TERMINAL_LABEL_REVIEWED" or not r["source_url"].startswith("https://"):
            raise p.AdmissionError("source-reviewed terminal label required, not analyst estimate")
        if r["definition_status"] not in ("OPERATOR_VERIFIED", "FROZEN_FRAMEWORK_CONVENTION"):
            raise p.AdmissionError("defined settlement endpoint required")
        if r["feature_status"] not in ("POINT_IN_TIME_VERIFIED", "FEATURES_NOT_VERIFIED", "NO_FEATURES"):
            raise p.AdmissionError("explicit feature-admission status required")
        if r["label_unit"] == "OUTCOME":
            if r["label_value"] not in ("WIN", "LOSS", "PUSH", "VOID"):
                raise p.AdmissionError("unresolved/missing outcome is not a training target")
        elif r["label_unit"] in ("GOALS", "POINTS", "RUNS", "GAMES", "SETS", "WICKETS", "BALLS"):
            value = float(r["label_value"])
            if not math.isfinite(value) or value < 0 or value != int(value):
                raise p.AdmissionError("count target must be a finite nonnegative integer")
        else:
            raise p.AdmissionError("unsupported target unit; implement its validation before export")
        p.receipt_file(r["evidence_path"], r["evidence_sha256"])


def verify_candidate(folder: Path) -> dict:
    receipts = p.read_rows(folder / "RECEIPT.csv")
    if len(receipts) != 1 or receipts[0]["record_kind"] != KIND:
        raise p.AdmissionError("one research-only candidate receipt required")
    rec = receipts[0]
    for name in ("ORIGINAL_CARD.md", "SETTLEMENT.md", "LABELS.csv"):
        p.receipt_file(folder / name, rec[name.replace(".", "_").lower() + "_sha256"])
    rows = p.read_rows(folder / "LABELS.csv")
    validate_labels(rows)
    if any(rows[0][k] != rec[k] for k in ("event_id", "competition", "endpoint", "revision_id")) or len(rows) != int(rec["labels"]):
        raise p.AdmissionError("candidate labels differ from receipt identity/count")
    if rec["status"] != "LABELS_RETAINED_NOT_MODEL_FEEDBACK":
        raise p.AdmissionError("research targets cannot be labelled as model feedback")
    if not re.search(r"\b" + re.escape(rec["card_id"]) + r"\b", (folder / "ORIGINAL_CARD.md").read_text(encoding="utf-8-sig")):
        raise p.AdmissionError("original research card does not identify the retained P-ID")
    if not re.search(r"\b" + re.escape(rec["card_id"]) + r"\b", (folder / "SETTLEMENT.md").read_text(encoding="utf-8-sig")):
        raise p.AdmissionError("settlement does not identify the retained P-ID")
    return rec


def retain_candidate(card_id: str, record: Path, settlement: Path, labels: Path, out: Path) -> dict:
    if not re.fullmatch(r"P-\d+", card_id):
        raise p.AdmissionError("existing research P-ID required; export does not allocate IDs")
    if out.exists():
        raise FileExistsError(out)
    source = p.source_hash()
    rows = p.read_rows(labels)
    validate_labels(rows)
    original, settled = record.read_bytes(), settlement.read_bytes()
    artifacts = {"ORIGINAL_CARD.md": original, "SETTLEMENT.md": settled, "LABELS.csv": p.csv_bytes(rows)}
    rec = dict(record_kind=KIND, card_id=card_id, status="LABELS_RETAINED_NOT_MODEL_FEEDBACK",
               **{k: rows[0][k] for k in ("event_id", "competition", "endpoint", "revision_id")},
               labels=len(rows), code_sha256=source, repository_head=p.repository_head(),
               generated_at=datetime.now(timezone.utc).isoformat(),
               feature_admission="SEPARATE_REVIEW_REQUIRED", predictive_qualification="NONE",
               **{k.replace(".", "_").lower() + "_sha256": p.digest(v) for k, v in artifacts.items()})
    out.parent.mkdir(parents=True, exist_ok=True)
    temporary = out.parent / ("." + out.name + "." + secrets.token_hex(6))
    temporary.mkdir()
    try:
        for name, data in artifacts.items():
            (temporary / name).write_bytes(data)
        (temporary / "RECEIPT.csv").write_bytes(p.csv_bytes([rec]))
        verify_candidate(temporary)
        if p.source_hash() != source:
            raise p.AdmissionError("generating source changed during candidate export")
        temporary.rename(out)
    finally:
        if temporary.exists():
            for child in temporary.iterdir():
                child.unlink()
            temporary.rmdir()
    return rec


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    retain = sub.add_parser("retain")
    retain.add_argument("--card-id", required=True)
    for name in ("record", "settlement", "labels", "out"):
        retain.add_argument("--" + name, type=Path, required=True)
    verify = sub.add_parser("verify")
    verify.add_argument("--candidate", type=Path, required=True)
    args = parser.parse_args(argv)
    rec = (verify_candidate(args.candidate) if args.command == "verify" else
           retain_candidate(args.card_id, args.record, args.settlement, args.labels, args.out))
    print(f"{rec['card_id']}: {rec['status']}; labels={rec['labels']}; future admission required")


if __name__ == "__main__":
    main()
