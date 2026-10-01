"""Reviewable issuer transaction; real appends require validated live evidence.

The issuer never starts a pilot or promotes a shadow. Preparation is read-only.
A journal precedes the append, so interruption blocks later issuance until the
exact pending projection is recovered. Existing issued bytes are never edited.
"""
from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import uuid

from .eligibility import (REGISTRY, aware_time, canonical_bytes, digest, file_sha,
                          validate_evidence)
from .ledger import (_append_locked, committed_issues, event_identity, event_key, forecast_core,
                     locked, read_records)
from .load import ROOT

PART6 = ROOT.parent / "prediction logs/PREDICTION_LOG_COMBINED_6.md"
RECONCILIATION = ROOT.parent / "P518_P522_RECONCILIATION.md"
CANONICAL_LEDGER = ROOT / "canonical_ledger.jsonl"
ORIGINAL_SHA256 = "c4d497bf339010eae2ff5df23a2d76290983585671666e74791618342565cf30"
BEGIN_ORIGINAL = b"<!-- BEGIN ORIGINAL P518 SOURCE BYTES -->"
END_ORIGINAL = b"<!-- END ORIGINAL P518 SOURCE BYTES -->"


def _utc_now() -> datetime:
    return datetime.now(timezone.utc)


def _custody(part6_path: Path) -> tuple[bytes, bytes]:
    raw = Path(part6_path).read_bytes()
    if raw.count(BEGIN_ORIGINAL) != 1 or raw.count(END_ORIGINAL) != 1:
        raise ValueError("Part 6 original-source markers are absent or duplicated")
    first = raw.index(BEGIN_ORIGINAL) + len(BEGIN_ORIGINAL)
    last = raw.index(END_ORIGINAL)
    between = raw[first:last]
    if not between.startswith(b"\r\n") or not between.endswith(b"\r\n"):
        raise ValueError("Part 6 original-source boundary bytes changed")
    original = between[2:-2]
    if len(original) != 141740 or hashlib.sha256(original).hexdigest() != ORIGINAL_SHA256:
        raise ValueError("Part 6 original-source custody hash changed")
    return raw, raw[last+len(END_ORIGINAL):]


def next_card_id(part6_path: Path = PART6, reconciliation_path: Path = RECONCILIATION,
                 ledger_path: Path = CANONICAL_LEDGER) -> str:
    _, tail = _custody(part6_path)
    reconciliation = Path(reconciliation_path).read_text(encoding="utf-8")
    if not all(re.search(rf"P-{n}\b", reconciliation) for n in range(518, 523)) or "reserved" not in reconciliation.lower():
        raise ValueError("authoritative reserved-ID reconciliation is unavailable")
    ids = [522]
    text = tail.decode("utf-8")
    ids += [int(n) for n in re.findall(r"(?m)^<!-- BEGIN CANONICAL ISSUE P-(\d+) ", text)]
    ids += [int(n) for n in re.findall(r"(?m)^#{1,6}\s+(?:Prediction\s+|Game(?:\s+Card)?\s+)?P-(\d+)\b", text)]
    records = read_records(ledger_path)
    prepared = [r for r in records if r["record_type"] == "ISSUE_PREPARED"]
    complete = {r["payload"]["transaction_id"] for r in records if r["record_type"] == "ISSUE_COMMITTED"}
    if any(r["payload"]["transaction_id"] not in complete for r in prepared):
        raise ValueError("pending issuer transaction must be recovered before assigning another ID")
    for issue in committed_issues(records):
        if not re.fullmatch(r"P-\d+", issue["card_id"]):
            raise ValueError("canonical ledger contains an invalid card ID")
        ids.append(int(issue["card_id"][2:]))
    return f"P-{max(ids)+1}"


def markdown_core(verified: dict, card_id: str, *, transaction_id: str, draft: bool = True) -> str:
    label = "PREPARED DRAFT / NOT_ISSUED" if draft else "FROZEN ISSUE CORE"
    lines = [f"## {card_id} — {verified['home']} vs {verified['away']}", "",
             f"**{label}.** SPORTS_ONLY / MARKET_BLIND.",
             f"- Event: `{verified['event_id']}`; {verified['league']} {verified['season']}; endpoint `{verified['endpoint']}`.",
             f"- Input cutoff: {verified['data_cutoff_utc']}; frozen issue: {verified['issued_utc']}.",
             f"- Verified scheduled start: {verified['scheduled_start_utc']}; actual start: UNKNOWN until verified after play.",
             f"- Model: `{verified['model_version']}`; evidence SHA-256: `{verified['bundle_sha256']}`.",
             f"- Admission registry: `{verified['registry_sha256']}`; source registry: `{verified['sources_registry_sha256']}`.",
             f"- Independent pregame lineages: {', '.join(verified['identity_lineages'])}.",
             f"- Adjustment: {verified['adjustment_type']}; transaction: `{transaction_id}`.",
             "- Performance eligibility remains pending actual-start and three-lineage terminal verification.", "",
             "| Rank | Contract | Baseline p | Model p | Card p | Push mass |",
             "|---:|---|---:|---:|---:|---:|"]
    for rank, row in enumerate(sorted(verified["rows"], key=lambda r: (-r["p_card"], r["market"], r["selection"])), 1):
        line = "" if row["line"] is None else f" {row['line']}"
        lines.append(f"| {rank} | {row['market']} {row['selection']}{line} | {row['p_baseline']:.8f} | {row['p_model']:.8f} | {row['p_card']:.8f} | {row['push_card']:.8f} |")
    return "\n".join(lines)+"\n"


def prepare_issue(bundle: dict, registry_path: Path = REGISTRY, *,
                  sources_registry_path: Path | None = None, evidence_root: Path | None = None,
                  ledger_path: Path = CANONICAL_LEDGER, part6_path: Path = PART6,
                  reconciliation_path: Path = RECONCILIATION) -> dict:
    """Validate and render a concrete draft without reserving an ID or writing."""
    now = _utc_now()
    candidate = deepcopy(bundle)
    candidate["issued_utc"] = now.isoformat()
    candidate["issuance_status"]="READ_ONLY_DRAFT_NOT_ISSUED"
    candidate.pop("actual_start_utc", None)
    if candidate.get("terminal_receipts") or candidate.get("actual_start_receipt"):
        raise ValueError("issuer input must be pregame evidence, not a settled event")
    verified = validate_evidence(candidate, registry_path, sources_registry_path=sources_registry_path,
                                 evidence_root=evidence_root, now=now).require()
    next_id = next_card_id(part6_path, reconciliation_path, ledger_path)
    key = event_key(candidate)
    records = read_records(ledger_path)
    if not any(r["record_type"] == "EVENT_REGISTERED" and event_key(r["payload"]) == key for r in records):
        raise ValueError("event must be registered in the complete frozen universe before preparation")
    if any(r["record_type"] in {"ISSUE_PREPARED", "ISSUE_COMMITTED", "ABSTENTION"} and event_identity(r["payload"]) == event_identity(candidate) for r in records):
        raise ValueError("event already has an issuance or abstention decision")
    transaction_id = uuid.uuid4().hex
    source_path = sources_registry_path or Path(registry_path).with_name("sources_registry.json")
    transaction = dict(schema_version="issuer-transaction-1", status="PREPARED_DRAFT_NOT_ISSUED",
                       transaction_id=transaction_id, proposed_card_id=next_id,
                       prepared_utc=now.isoformat(), bundle=candidate,
                       registry_path=str(Path(registry_path).resolve()), sources_registry_path=str(Path(source_path).resolve()),
                       evidence_root=str(Path(evidence_root).resolve()) if evidence_root else None,
                       ledger_path=str(Path(ledger_path).resolve()), part6_path=str(Path(part6_path).resolve()),
                       reconciliation_path=str(Path(reconciliation_path).resolve()),
                       expected_part6_sha256=file_sha(Path(part6_path)),
                       expected_ledger_head=records[-1]["record_sha256"] if records else "0"*64,
                       markdown_draft=markdown_core(verified, next_id, transaction_id=transaction_id))
    return {**transaction, "transaction_sha256": digest(transaction)}


def _projection(core: str, card_id: str, transaction_id: str) -> bytes:
    body = core.replace("\r\n", "\n").replace("\n", "\r\n").encode("utf-8")
    return (f"\r\n<!-- BEGIN CANONICAL ISSUE {card_id} {transaction_id} -->\r\n".encode()
            + body + f"<!-- END CANONICAL ISSUE {card_id} {transaction_id} -->\r\n".encode())


def commit_issue(transaction: dict, *, allow_real_issue: bool = False) -> dict:
    """Commit a validated real event. Default is deliberately nonmutating."""
    if not allow_real_issue:
        raise ValueError("real issuance is disabled; use the reviewable preparation result")
    body = {k: v for k, v in transaction.items() if k != "transaction_sha256"}
    if transaction.get("schema_version") != "issuer-transaction-1" or transaction.get("status") != "PREPARED_DRAFT_NOT_ISSUED" or digest(body) != transaction.get("transaction_sha256"):
        raise ValueError("prepared transaction changed or is not a draft")
    path, part6 = Path(transaction["ledger_path"]), Path(transaction["part6_path"])
    with locked(path):
        records = read_records(path)
        head = records[-1]["record_sha256"] if records else "0"*64
        if head != transaction["expected_ledger_head"] or file_sha(part6) != transaction["expected_part6_sha256"]:
            raise ValueError("authoritative ledger or Part 6 changed since preparation; prepare again")
        next_id = next_card_id(part6, Path(transaction["reconciliation_path"]), path)
        if next_id != transaction["proposed_card_id"]:
            raise ValueError("authoritative next card ID changed")
        now = _utc_now()
        bundle = deepcopy(transaction["bundle"])
        bundle["issued_utc"] = now.isoformat()
        bundle["issuance_status"]="ISSUED_PENDING_TERMINAL_ADMISSION"
        verified = validate_evidence(bundle, Path(transaction["registry_path"]),
                                     sources_registry_path=Path(transaction["sources_registry_path"]),
                                     evidence_root=Path(transaction["evidence_root"]) if transaction["evidence_root"] else None,
                                     now=now).require()
        if (aware_time(verified["scheduled_start_utc"])-now).total_seconds() < 30:
            raise ValueError("issuance needs at least 30 seconds before verified scheduled start")
        key = event_key(bundle)
        if any(r["record_type"] in {"ISSUE_PREPARED", "ISSUE_COMMITTED", "ABSTENTION"} and event_identity(r["payload"]) == event_identity(bundle) for r in records):
            raise ValueError("duplicate event issuance")
        core = markdown_core(verified, next_id, transaction_id=transaction["transaction_id"], draft=False)
        projection = _projection(core, next_id, transaction["transaction_id"])
        frozen_dir = path.parent / "issued"
        frozen_dir.mkdir(parents=True, exist_ok=True)
        frozen_path = frozen_dir / f"{next_id}_{digest(bundle)}.json"
        with frozen_path.open("xb") as handle:
            handle.write(canonical_bytes(bundle)+b"\n")
            handle.flush()
            os.fsync(handle.fileno())
        payload = {**{f: bundle[f] for f in ("lane", "league", "season", "event_id")},
                   "transaction_id": transaction["transaction_id"], "card_id": next_id, "bundle": bundle,
                   "forecast_core_sha256": digest(forecast_core(bundle)), "core": core,
                   "core_sha256": hashlib.sha256(projection).hexdigest(),
                   "frozen_bundle_path": str(frozen_path), "frozen_bundle_file_sha256": file_sha(frozen_path),
                   "part6_path": str(part6), "part6_before_sha256": transaction["expected_part6_sha256"],
                   "registry_path": transaction["registry_path"], "sources_registry_path": transaction["sources_registry_path"],
                   "evidence_root": transaction["evidence_root"]}
        preparation = _append_locked(path, "ISSUE_PREPARED", payload, recorded_utc=now.isoformat())
        _custody(part6)
        if file_sha(part6) != payload["part6_before_sha256"] or _utc_now() >= aware_time(bundle["scheduled_start_utc"]):
            raise ValueError("issuance interrupted or start reached; pending transaction requires audit/recovery")
        with part6.open("ab") as handle:
            handle.write(projection)
            handle.flush()
            os.fsync(handle.fileno())
        _custody(part6)
        commit = _append_locked(path, "ISSUE_COMMITTED", {
            **{f: bundle[f] for f in ("lane", "league", "season", "event_id")},
            "transaction_id": transaction["transaction_id"], "card_id": next_id,
            "core_sha256": payload["core_sha256"], "prepared_record_sha256": preparation["record_sha256"],
            "part6_after_sha256": file_sha(part6)})
        return {"status": "ISSUED_PENDING_TERMINAL_ADMISSION", "card_id": next_id,
                "issue_record_sha256": commit["record_sha256"], "frozen_bundle_path": str(frozen_path)}


def recover_issue(ledger_path: Path, transaction_id: str, *, allow_real_issue: bool = False) -> dict:
    """Complete an exact pending append while still pregame; never rewrite it."""
    if not allow_real_issue:
        raise ValueError("real recovery append is disabled")
    with locked(ledger_path):
        records = read_records(ledger_path)
        prep = next((r for r in records if r["record_type"] == "ISSUE_PREPARED" and r["payload"]["transaction_id"] == transaction_id), None)
        if prep is None:
            raise ValueError("pending transaction is absent")
        existing = next((r for r in records if r["record_type"] == "ISSUE_COMMITTED" and r["payload"]["transaction_id"] == transaction_id), None)
        if existing:
            return {"status": "ALREADY_COMMITTED", "issue_record_sha256": existing["record_sha256"]}
        p = prep["payload"]
        now = _utc_now()
        if now >= aware_time(p["bundle"]["scheduled_start_utc"]):
            raise ValueError("post-start pending transaction requires manual custody audit; no automatic issuance")
        validate_evidence(p["bundle"], Path(p["registry_path"]), sources_registry_path=Path(p["sources_registry_path"]),
                          evidence_root=Path(p["evidence_root"]) if p["evidence_root"] else None, now=now).require()
        if file_sha(Path(p["frozen_bundle_path"])) != p["frozen_bundle_file_sha256"]:
            raise ValueError("pending frozen bundle changed")
        part6 = Path(p["part6_path"])
        raw, _ = _custody(part6)
        projection = _projection(p["core"], p["card_id"], transaction_id)
        if hashlib.sha256(projection).hexdigest() != p["core_sha256"]:
            raise ValueError("pending issue core changed")
        if raw.endswith(projection):
            if hashlib.sha256(raw[:-len(projection)]).hexdigest() != p["part6_before_sha256"]:
                raise ValueError("Part 6 prefix differs from prepared custody")
        elif hashlib.sha256(raw).hexdigest() == p["part6_before_sha256"]:
            with part6.open("ab") as handle:
                handle.write(projection)
                handle.flush()
                os.fsync(handle.fileno())
        else:
            raise ValueError("Part 6 has a partial/conflicting append; preserve bytes for manual audit")
        commit = _append_locked(ledger_path, "ISSUE_COMMITTED", {
            **{f: p[f] for f in ("lane", "league", "season", "event_id")},
            "transaction_id": transaction_id, "card_id": p["card_id"], "core_sha256": p["core_sha256"],
            "prepared_record_sha256": prep["record_sha256"], "part6_after_sha256": file_sha(part6), "recovery": True})
        return {"status": "RECOVERED", "issue_record_sha256": commit["record_sha256"]}


if __name__ == "__main__":
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    commands=parser.add_subparsers(dest="command",required=True)
    prepare=commands.add_parser("prepare")
    prepare.add_argument("bundle",type=Path)
    prepare.add_argument("output",type=Path)
    prepare.add_argument("--registry",type=Path,default=REGISTRY)
    prepare.add_argument("--sources-registry",type=Path)
    prepare.add_argument("--evidence-root",type=Path)
    prepare.add_argument("--ledger",type=Path,default=CANONICAL_LEDGER)
    prepare.add_argument("--part6",type=Path,default=PART6)
    prepare.add_argument("--reconciliation",type=Path,default=RECONCILIATION)
    commit=commands.add_parser("commit")
    commit.add_argument("transaction",type=Path)
    commit.add_argument("--allow-real-issue",action="store_true")
    recover=commands.add_parser("recover")
    recover.add_argument("ledger",type=Path)
    recover.add_argument("transaction_id")
    recover.add_argument("--allow-real-issue",action="store_true")
    args=parser.parse_args()
    if args.command=="prepare":
        result=prepare_issue(json.loads(args.bundle.read_text(encoding="utf-8")),args.registry,
            sources_registry_path=args.sources_registry,evidence_root=args.evidence_root,
            ledger_path=args.ledger,part6_path=args.part6,reconciliation_path=args.reconciliation)
        args.output.parent.mkdir(parents=True,exist_ok=True)
        with args.output.open("xb") as handle:
            handle.write(canonical_bytes(result)+b"\n");handle.flush();os.fsync(handle.fileno())
        print(json.dumps({"status":result["status"],"draft_transaction":str(args.output.resolve())},indent=2))
    elif args.command=="commit":
        print(json.dumps(commit_issue(json.loads(args.transaction.read_text(encoding="utf-8")),allow_real_issue=args.allow_real_issue),indent=2))
    else:
        print(json.dumps(recover_issue(args.ledger,args.transaction_id,allow_real_issue=args.allow_real_issue),indent=2))
