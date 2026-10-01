"""Hash-chained, append-only event, issuance and settlement custody.

There is no backfill of historical performance eligibility. Issuance records
are written only by the checked issuer; settlement revisions preserve earlier
scores and grades and bind their source evidence to the original frozen core.
"""
from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import uuid

import numpy as np

from .eligibility import (REGISTRY, aware_time, canonical_bytes, checked_json,
                          checked_ref, digest, validate_evidence)
from .emit_card import _outcome
from .sports.base import Contract

LEDGER_SCHEMA = "canonical-ledger-1"
ZERO = "0" * 64
PUBLIC_TYPES = {"EVENT_REGISTERED", "ABSTENTION", "PILOT_LOCK", "PILOT_INTERIM", "PILOT_FINAL"}


def event_key(value: dict) -> tuple[str, str, str, str]:
    fields = ("lane", "league", "season", "event_id")
    if any(not isinstance(value.get(f), str) or not value[f] for f in fields):
        raise ValueError("ledger record needs exact lane/league/season/event ID")
    return tuple(value[f] for f in fields)


def event_identity(value: dict) -> tuple[str,str,str]:
    """Stable provider event IDs cannot be reissued by changing season labels."""
    key=event_key(value)
    return key[0],key[1],key[3]


def forecast_core(bundle: dict) -> dict:
    excluded = {"terminal_receipts", "actual_start_receipt", "actual_start_utc", "settled_utc"}
    return {k: v for k, v in bundle.items() if k not in excluded}


@contextmanager
def locked(path: Path):
    """A cooperative exclusive writer lock. Stale locks require explicit audit."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    lock_path = path.with_name(path.name + ".writer-lock")
    token = uuid.uuid4().hex
    try:
        fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise RuntimeError(f"writer lock exists; audit active/stale writer: {lock_path}") from exc
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(canonical_bytes({"pid": os.getpid(), "token": token, "created_utc": datetime.now(timezone.utc).isoformat()}))
            handle.flush()
            os.fsync(handle.fileno())
        yield
    finally:
        if lock_path.exists():
            current = json.loads(lock_path.read_text(encoding="utf-8"))
            if current.get("token") != token:
                raise RuntimeError("writer lock ownership changed")
            lock_path.unlink()


def read_records(path: Path) -> list[dict]:
    path = Path(path)
    if not path.exists():
        return []
    raw = path.read_bytes()
    if raw and not raw.endswith(b"\n"):
        raise ValueError("ledger has a partial append; audit before further writes")
    records, previous = [], ZERO
    for line_no, line in enumerate(raw.splitlines(), 1):
        if not line:
            raise ValueError("ledger contains a blank record")
        record = json.loads(line)
        body = {k: v for k, v in record.items() if k != "record_sha256"}
        if (record.get("schema_version") != LEDGER_SCHEMA or record.get("sequence") != line_no
                or record.get("previous_sha256") != previous or record.get("record_sha256") != digest(body)
                or canonical_bytes(record) != line):
            raise ValueError(f"ledger chain or canonical bytes changed at record {line_no}")
        aware_time(record.get("recorded_utc"), "ledger custody time")
        records.append(record)
        previous = record["record_sha256"]
    return records


def _append_locked(path: Path, kind: str, payload: dict, *, recorded_utc: str | None = None) -> dict:
    records = read_records(path)
    when = recorded_utc or datetime.now(timezone.utc).isoformat()
    aware_time(when, "ledger custody time")
    if records and aware_time(when) < aware_time(records[-1]["recorded_utc"]):
        raise ValueError("append custody timestamp moves backwards")
    body = dict(schema_version=LEDGER_SCHEMA, sequence=len(records)+1,
                previous_sha256=records[-1]["record_sha256"] if records else ZERO,
                recorded_utc=when, record_type=kind, payload=payload)
    record = {**body, "record_sha256": digest(body)}
    with Path(path).open("ab") as handle:
        handle.write(canonical_bytes(record) + b"\n")
        handle.flush()
        os.fsync(handle.fileno())
    return record


def append_record(path: Path, kind: str, payload: dict) -> dict:
    """Append audit records. Typed issue/settlement APIs cannot be bypassed here."""
    if kind not in PUBLIC_TYPES:
        raise ValueError("use the checked issuer or settlement-revision API for this record type")
    canonical_bytes(payload)
    with locked(path):
        records = read_records(path)
        if kind == "EVENT_REGISTERED":
            key = event_key(payload)
            aware_time(payload.get("scheduled_start_utc"), "registered start")
            if not payload.get("universe_sha256") or not payload.get("universe_ref"):
                raise ValueError("event registration needs a frozen universe receipt")
            old = [r for r in records if r["record_type"] == kind and event_identity(r["payload"]) == event_identity(payload)]
            if old:
                if old[0]["payload"] == payload:
                    return old[0]
                raise ValueError("registered event identity changed; append an explicit audited revision")
        if kind == "ABSTENTION":
            key = event_key(payload)
            registered = [r for r in records if r["record_type"] == "EVENT_REGISTERED" and event_key(r["payload"]) == key]
            if len(registered) != 1 or not payload.get("reason"):
                raise ValueError("abstention needs a registered event and an explicit reason")
            if any(r["record_type"] in {"ABSTENTION", "ISSUE_PREPARED", "ISSUE_COMMITTED"} and event_key(r["payload"]) == key for r in records):
                raise ValueError("event already has a forecast decision")
        return _append_locked(path, kind, payload)


def validate_universe(universe_ref: dict, *, evidence_root: Path) -> dict:
    """Match every declared fixture to the full retained native source window."""
    universe = checked_json(universe_ref, evidence_root)
    if universe.get("schema_version") != "event-universe-1" or not universe.get("events") or not universe.get("source_refs"):
        raise ValueError("versioned full-universe source receipt is required")
    captured = aware_time(universe.get("captured_utc"), "universe capture time")
    rule = universe.get("population_rule", {})
    first, last = aware_time(rule.get("from_utc")), aware_time(rule.get("to_utc"))
    if not captured <= first < last or rule.get("state") != "PREGAME" or not rule.get("league") or not rule.get("season"):
        raise ValueError("universe needs an explicit pregame competition/season/time population rule")
    populations = []
    for ref in universe["source_refs"]:
        raw = checked_json(ref, evidence_root)
        if ref.get("league") != rule["league"]:
            raise ValueError("universe source competition differs from declared population")
        selected = {}
        if ref.get("parser_id") == "NBL_SCHEDULE_V1":
            matches = raw.get("matches", [])
            if raw.get("total") != len(matches):
                raise ValueError("universe native schedule pagination is incomplete")
            for match in matches:
                if match.get("phase") != "upcoming" or match.get("season_type") != "regular":
                    continue
                start = datetime.fromtimestamp(match["starts_at_ms"]/1000, timezone.utc)
                if first <= start < last:
                    event_id = str(match["id"])
                    if event_id in selected:
                        raise ValueError("duplicate event in native universe source")
                    selected[event_id] = start
        elif ref.get("parser_id") == "ESPN_SCOREBOARD_V1":
            for event in raw.get("events", []):
                status = event.get("status", {}).get("type", {})
                if status.get("name") != "STATUS_SCHEDULED" or status.get("completed"):
                    continue
                start = aware_time(event.get("date"), "native fixture start")
                if first <= start < last:
                    event_id = str(event["id"])
                    if event_id in selected:
                        raise ValueError("duplicate event in native universe source")
                    selected[event_id] = start
        else:
            raise ValueError("full-universe coverage needs a supported native schedule parser")
        populations.append(selected)
    events, keys = universe["events"], set()
    declared = {}
    for event in events:
        key = event_key(event)
        start = aware_time(event.get("scheduled_start_utc"))
        if key in keys or not captured < start or not first <= start < last or event["league"] != rule["league"] or event["season"] != rule["season"]:
            raise ValueError("universe contains duplicate or already-started events")
        keys.add(key)
        declared[event["event_id"]] = start
    if any(population != declared for population in populations):
        raise ValueError("declared universe omits/adds/changes fixtures in retained native source population")
    return universe


def register_universe(path: Path, universe_ref: dict, *, evidence_root: Path) -> list[dict]:
    """Register the entire retained universe before any event is selected."""
    universe = validate_universe(universe_ref, evidence_root=evidence_root)
    captured = aware_time(universe["captured_utc"])
    if captured > datetime.now(timezone.utc):
        raise ValueError("universe capture is in the future")
    events = universe["events"]
    output = []
    for event in sorted(events, key=lambda e: (aware_time(e["scheduled_start_utc"]), event_key(e))):
        payload = {**event, "universe_sha256": universe_ref["sha256"], "universe_ref": universe_ref,
                   "universe_captured_utc": captured.isoformat()}
        output.append(append_record(path, "EVENT_REGISTERED", payload))
    return output


def record_abstention(path: Path, identity: dict, reason: str, *, evidence_refs: list[dict], evidence_root: Path) -> dict:
    for ref in evidence_refs:
        checked_ref(ref, evidence_root)
    event_key(identity)
    records = read_records(path)
    registered = next((r["payload"] for r in records if r["record_type"] == "EVENT_REGISTERED" and event_key(r["payload"]) == event_key(identity)), None)
    if registered is None:
        raise ValueError("cannot abstain from an unregistered event")
    now = datetime.now(timezone.utc)
    payload = {**{f: identity[f] for f in ("lane", "league", "season", "event_id")}, "reason": reason,
               "evidence_refs": evidence_refs, "decision_utc": now.isoformat(),
               "timely": now < aware_time(registered["scheduled_start_utc"])}
    return append_record(path, "ABSTENTION", payload)


def committed_issues(records: list[dict]) -> list[dict]:
    prepared = {r["payload"]["transaction_id"]: r for r in records if r["record_type"] == "ISSUE_PREPARED"}
    output, seen_events, seen_cards = [], set(), set()
    for record in records:
        if record["record_type"] != "ISSUE_COMMITTED":
            continue
        p = record["payload"]
        source = prepared.get(p.get("transaction_id"))
        if source is None or p.get("prepared_record_sha256") != source["record_sha256"]:
            raise ValueError("committed issue has no matching preparation custody")
        frozen = source["payload"]
        key = event_key(frozen)
        if event_key(p) != key or p.get("card_id") != frozen.get("card_id") or p.get("core_sha256") != frozen.get("core_sha256"):
            raise ValueError("issue commit differs from prepared event/card/core")
        if event_identity(frozen) in seen_events or frozen["card_id"] in seen_cards:
            raise ValueError("duplicate issued event or card ID in ledger")
        if digest(forecast_core(frozen["bundle"])) != frozen.get("forecast_core_sha256"):
            raise ValueError("frozen issue bundle changed")
        seen_events.add(event_identity(frozen))
        seen_cards.add(frozen["card_id"])
        output.append({**frozen, "issue_record_sha256": record["record_sha256"],
                       "issue_recorded_utc": record["recorded_utc"]})
    return sorted(output, key=lambda p: (aware_time(p["bundle"]["issued_utc"]), event_key(p)))


def append_settlement_revision(path: Path, bundle: dict, registry_path: Path = REGISTRY, *,
                               reason: str, sources_registry_path: Path | None = None,
                               evidence_root: Path | None = None) -> dict:
    if not isinstance(reason, str) or not reason.strip():
        raise ValueError("settlement revision requires a reason")
    verified = validate_evidence(bundle, registry_path, sources_registry_path=sources_registry_path,
                                 evidence_root=evidence_root, require_terminal=True).require()
    key = event_key(bundle)
    with locked(path):
        records = read_records(path)
        issue = next((p for p in committed_issues(records) if event_key(p) == key), None)
        if issue is None:
            raise ValueError("settlement has no canonical issued event")
        if digest(forecast_core(bundle)) != issue["forecast_core_sha256"]:
            raise ValueError("settlement attempted to rewrite the frozen forecast core")
        previous = [r for r in records if r["record_type"] == "SETTLEMENT_REVISION" and event_key(r["payload"]) == key]
        rows = []
        for row in verified["rows"]:
            c = Contract(bundle["event_id"], row["market"], row["selection"], row["line"], row["endpoint"], row["period"])
            win, push = _outcome(np.array([verified["score_home"]]), np.array([verified["score_away"]]), c)
            rows.append({**row, "result": "W" if win[0] else "P" if push[0] else "L"})
        payload = {**{f: bundle[f] for f in ("lane", "league", "season", "event_id")},
                   "revision": len(previous)+1, "previous_revision_sha256": previous[-1]["record_sha256"] if previous else ZERO,
                   "issue_record_sha256": issue["issue_record_sha256"], "forecast_core_sha256": issue["forecast_core_sha256"],
                   "reason": reason, "bundle": bundle, "verified": {**verified, "rows": rows}}
        if previous and digest(previous[-1]["payload"]["bundle"]) == digest(bundle):
            raise ValueError("duplicate settlement revision")
        return _append_locked(path, "SETTLEMENT_REVISION", payload)


if __name__ == "__main__":
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    commands=parser.add_subparsers(dest="command",required=True)
    validate=commands.add_parser("validate")
    validate.add_argument("ledger",type=Path)
    register=commands.add_parser("register-universe")
    register.add_argument("universe",type=Path)
    register.add_argument("ledger",type=Path)
    register.add_argument("--evidence-root",type=Path,required=True)
    abstain=commands.add_parser("abstain")
    abstain.add_argument("identity",type=Path)
    abstain.add_argument("ledger",type=Path)
    abstain.add_argument("--reason",required=True)
    abstain.add_argument("--evidence-refs",type=Path)
    abstain.add_argument("--evidence-root",type=Path,required=True)
    settle=commands.add_parser("settle")
    settle.add_argument("bundle",type=Path)
    settle.add_argument("ledger",type=Path)
    settle.add_argument("--registry",type=Path,default=REGISTRY)
    settle.add_argument("--sources-registry",type=Path)
    settle.add_argument("--evidence-root",type=Path)
    settle.add_argument("--reason",required=True)
    args=parser.parse_args()
    if args.command=="validate":
        records=read_records(args.ledger)
        print(json.dumps({"records":len(records),"head_sha256":records[-1]["record_sha256"] if records else ZERO,"committed_issues":len(committed_issues(records))},indent=2))
    elif args.command=="register-universe":
        root=args.evidence_root.resolve()
        reference={"path":str(args.universe.resolve().relative_to(root)),"sha256":__import__("hashlib").sha256(args.universe.read_bytes()).hexdigest()}
        result=register_universe(args.ledger,reference,evidence_root=root)
        print(json.dumps({"registered_events":len(result)},indent=2))
    elif args.command=="abstain":
        refs=json.loads(args.evidence_refs.read_text(encoding="utf-8")) if args.evidence_refs else []
        result=record_abstention(args.ledger,json.loads(args.identity.read_text(encoding="utf-8")),args.reason,evidence_refs=refs,evidence_root=args.evidence_root)
        print(json.dumps({"record_sha256":result["record_sha256"]},indent=2))
    else:
        result=append_settlement_revision(args.ledger,json.loads(args.bundle.read_text(encoding="utf-8")),args.registry,
            reason=args.reason,sources_registry_path=args.sources_registry,evidence_root=args.evidence_root)
        print(json.dumps({"record_sha256":result["record_sha256"],"revision":result["payload"]["revision"]},indent=2))
