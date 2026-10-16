"""Durable per-event execution attempts and strict mini-log coverage checks.

This enforces execution evidence, not source truth, pre-start publication or skill.
No pre-existing league profile or baseline probability is an input to execution.
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import csv
import re

from ml import primary as p


MANIFEST_FIELDS = ("card_id", "event_id", "competition", "endpoint", "execution_path",
                   "execution_sha256", "feedback_status", "feedback_path", "feedback_sha256", "reason")


def _now():
    return datetime.now(timezone.utc).isoformat()


def execute_files(request: Path, history: Path, contracts: Path, out: Path,
                  feedback: Path | None = None, competition_source: Path | None = None) -> dict:
    """Attempt the real primary pipeline, retaining success AND failure without overwriting.

    STARTED without EXECUTION means interrupted/incomplete, never a successful run.
    Existing predict remains available for historical compatibility; new logs use execute.
    """
    out.mkdir(parents=True, exist_ok=False)
    started = dict(started_at=_now(), code_sha256=p.source_hash(), repository_head=p.repository_head())
    (out / "STARTED.csv").write_bytes(p.csv_bytes([started]))
    rec = dict(**started, event_id="UNKNOWN", competition="UNKNOWN", endpoint="UNKNOWN",
               status="FAILED", stage="INPUT_LOADING", baseline_status="NO_RESULT",
               baseline_dependency="NO_PREEXISTING_PROFILE_REQUIRED", bundle="",
               receipt_sha256="", error_type="", error="")
    snapshots = []
    try:
        paths = dict(REQUEST=request, HISTORY=history, CONTRACTS=contracts)
        if feedback is not None:
            paths["FEEDBACK_INPUT"] = feedback
        if competition_source is not None:
            paths["COMPETITION_SOURCE"] = competition_source
        requests = p.read_rows(request)
        if len(requests) != 1:
            raise p.AdmissionError("exactly one event per execution required")
        req = requests[0]
        for key in ("event_id", "competition", "endpoint"):
            rec[key] = req[key]
        for name, path in paths.items():
            raw = path.read_bytes()
            rows = p.read_rows(path)
            snapshots.append(dict(name=name, path=str(path.resolve()), sha256=p.digest(raw),
                                  normalized_sha256=p.digest(p.csv_bytes(rows) if rows else b"")))
        source = p.read_rows(competition_source) if competition_source is not None else None
        rec["stage"] = "SCOPE_LOOKUP"
        lg = None if source is not None else p.get_league(req["competition"])
        rec["stage"] = "PRIMARY_PIPELINE"
        bundle = out / "BUNDLE"
        result = p.forecast(req, lg, p.read_rows(history), p.read_rows(contracts), bundle,
                            p.read_rows(feedback) if feedback is not None else [], competition_source=source)
        for snapshot in snapshots:
            p.receipt_file(snapshot["path"], snapshot["sha256"])
            saved = p.read_rows(bundle / (snapshot["name"] + ".csv"))
            if p.digest(p.csv_bytes(saved) if saved else b"") != snapshot["normalized_sha256"]:
                raise p.AdmissionError("execution input differs from fitted bundle")
        if result["code_sha256"] != started["code_sha256"] or p.source_hash() != started["code_sha256"]:
            raise p.AdmissionError("generating source changed during execution")
        rec.update(status="EXECUTED", stage="BUNDLE_VERIFIED", baseline_status="FITTED_FROM_HISTORY",
                   bundle="BUNDLE", receipt_sha256=p.digest((bundle / "RECEIPT.csv").read_bytes()))
    except Exception as exc:
        # Retain the actual failure. The caller exits nonzero; no fabricated probabilities or feedback.
        rec.update(error_type=type(exc).__name__, error=str(exc))
    rec["completed_at"] = _now()
    (out / "INPUTS.csv").write_bytes(p.csv_bytes(snapshots) if snapshots else b"name,path,sha256\n")
    rec["inputs_sha256"] = p.digest((out / "INPUTS.csv").read_bytes())
    rec["started_sha256"] = p.digest((out / "STARTED.csv").read_bytes())
    (out / "EXECUTION.csv").write_bytes(p.csv_bytes([rec]))
    return rec


def verify_execution(folder: Path, *, event_id=None, competition=None, endpoint=None) -> dict:
    rows = p.read_rows(folder / "EXECUTION.csv")
    if len(rows) != 1:
        raise p.AdmissionError("exactly one completed execution record required")
    rec = rows[0]
    p.receipt_file(folder / "STARTED.csv", rec["started_sha256"])
    p.receipt_file(folder / "INPUTS.csv", rec["inputs_sha256"])
    starts = p.read_rows(folder / "STARTED.csv")
    if len(starts) != 1 or any(starts[0][k] != rec[k] for k in starts[0]):
        raise p.AdmissionError("execution start differs from completed record")
    if p.clock(rec["completed_at"]) < p.clock(rec["started_at"]):
        raise p.AdmissionError("execution completed before start")
    for key, expected in (("event_id", event_id), ("competition", competition), ("endpoint", endpoint)):
        if expected is not None and rec[key] != expected:
            raise p.AdmissionError("execution " + key + " differs from log")
    if rec["baseline_dependency"] != "NO_PREEXISTING_PROFILE_REQUIRED":
        raise p.AdmissionError("baseline profile cannot be an execution prerequisite")
    if rec["status"] == "EXECUTED":
        if rec["bundle"] != "BUNDLE" or rec["stage"] != "BUNDLE_VERIFIED" or rec["baseline_status"] != "FITTED_FROM_HISTORY" or rec["error_type"] or rec["error"]:
            raise p.AdmissionError("invalid successful execution disposition")
        bundle = folder / "BUNDLE"
        p.receipt_file(bundle / "RECEIPT.csv", rec["receipt_sha256"])
        model = p.verify_bundle(bundle)
        if any(model[k] != rec[k] for k in ("event_id", "competition", "endpoint", "code_sha256")):
            raise p.AdmissionError("execution differs from verified model bundle")
        inputs = p.read_rows(folder / "INPUTS.csv")
        names = [r["name"] for r in inputs]
        allowed = {"REQUEST", "HISTORY", "CONTRACTS", "FEEDBACK_INPUT", "COMPETITION_SOURCE"}
        if len(names) != len(set(names)) or not {"REQUEST", "HISTORY", "CONTRACTS"}.issubset(names) or not set(names).issubset(allowed):
            raise p.AdmissionError("execution input coverage missing/duplicated")
        for row in inputs:
            saved = p.read_rows(bundle / (row["name"] + ".csv"))
            if p.digest(p.csv_bytes(saved) if saved else b"") != row["normalized_sha256"]:
                raise p.AdmissionError("execution input digest differs from bundle")
    elif rec["status"] == "FAILED":
        if not rec["error_type"] or not rec["error"] or rec["baseline_status"] != "NO_RESULT" or rec["bundle"] or rec["stage"] not in ("INPUT_LOADING", "SCOPE_LOOKUP", "PRIMARY_PIPELINE"):
            raise p.AdmissionError("failed execution requires actual failure evidence and no issued bundle")
    else:
        raise p.AdmissionError("unexecuted/incomplete execution record")
    return rec


def verify_log(manifest: Path, mini: Path) -> dict:
    """Verify local research dispositions without allocating canonical IDs.

    Only use on new mandatory-execution minis, not historical cards or canonical wrappers.
    Research-only cards may have no executable runtime/receipt. Verified settled labels
    can later train a model; they cannot invent a frozen expert's historical loss.
    """
    text = mini.read_text(encoding="utf-8-sig")
    formats = re.findall(r"<!-- MINI-LOG-FORMAT: (\S+) -->", text)
    if text.count("MINI-LOG-FORMAT:") != 1 or len(formats) != 1 or formats[0] not in ("mini-log-8", "mini-log-9", "mini-log-10"):
        raise p.AdmissionError("research verifier requires one mini-log-8/9/10 format; preserve legacy formats")
    cards, active = [], None
    markers = re.findall(r"<!-- (BEGIN|END) CARD ([^\r\n]*?) -->", text)
    if len(markers) != len(re.findall(r"<!--\s*(?:BEGIN|END)\s+CARD\b", text)):
        raise p.AdmissionError("malformed mini card marker")
    for action, key in markers:
        local = re.fullmatch(r"LOCAL-[A-Z0-9]+-G([0-9]{4,})", key)
        valid_local = local is not None and int(local[1]) > 0
        legacy = formats[0] != "mini-log-10" and re.fullmatch(r"P-\d+", key)
        if not (valid_local or legacy):
            raise p.AdmissionError("card identity must be a stable local key; P-IDs are legacy8/9 only")
        if action == "BEGIN":
            if active is not None or key in cards:
                raise p.AdmissionError("mini card markers duplicate/nested")
            active = key
            cards.append(key)
        elif active != key:
            raise p.AdmissionError("mini card markers orphaned/unbalanced")
        else:
            active = None
    if active is not None:
        raise p.AdmissionError("mini card markers unbalanced")
    with manifest.open(encoding="utf-8-sig", newline="") as handle:
        if csv.DictReader(handle).fieldnames != list(MANIFEST_FIELDS):
            raise p.AdmissionError("execution manifest header must match registered fields")
    rows = p.read_rows(manifest)
    ids = [r["card_id"] for r in rows]
    if len(ids) != len(set(ids)) or set(ids) != set(cards):
        raise p.AdmissionError("execution manifest must cover every mini card exactly once")
    events = [r["event_id"] for r in rows]
    if len(events) != len(set(events)):
        raise p.AdmissionError("duplicate event in execution manifest")
    executed = failed = feedback_count = research_only = 0
    for row in rows:
        if set(row) != set(MANIFEST_FIELDS):
            raise p.AdmissionError("unregistered/missing execution manifest fields")
        match = re.search(r"<!-- BEGIN CARD " + re.escape(row["card_id"]) + r" -->(.*?)<!-- END CARD " + re.escape(row["card_id"]) + r" -->", text, re.S)
        body = match.group(1)
        identity = f"- **ML execution identity:** {row['event_id']} | {row['competition']} | {row['endpoint']}"
        if identity not in body:
            raise p.AdmissionError("card identity differs from execution manifest")
        statuses = re.findall(r"^- \*\*Analysis status:\*\*\s+(\S+)", body, re.M)
        if len(statuses) != 1 or statuses[0] not in ("MODEL_ASSISTED_PRIMARY_V3", "MODEL_ASSISTED_CYCLE_V1", "RESEARCH_ONLY_NO_MODEL", "UNCALIBRATED_QUALITATIVE", "NO_FORECAST"):
            raise p.AdmissionError("one explicit primary analysis disposition required")
        if not row["execution_path"]:
            if row["execution_sha256"]:
                raise p.AdmissionError("execution hash without an actual attempt path")
            if statuses[0] in ("MODEL_ASSISTED_PRIMARY_V3", "MODEL_ASSISTED_CYCLE_V1"):
                raise p.AdmissionError("numeric primary card requires successful execution")
            if not row["reason"].strip() or row["feedback_status"] != "NOT_APPLICABLE_NO_MODEL" or row["feedback_path"] or row["feedback_sha256"]:
                raise p.AdmissionError("research-only retention requires honest missing-model reason and no invented expert feedback")
            research_only += 1
            continue
        folder = manifest.parent / row["execution_path"]
        p.receipt_file(folder / "EXECUTION.csv", row["execution_sha256"])
        record = p.read_rows(folder / "EXECUTION.csv")[0]
        cycle_attempt = record.get("entrypoint") == "python -m ml.workflow research"
        if cycle_attempt:
            from ml.workflow import verify
            rec = verify(folder)
            if any(rec[k] != row[k] for k in ("event_id", "competition", "endpoint")):
                raise p.AdmissionError("workflow identity differs from mini manifest")
            if statuses[0] == "MODEL_ASSISTED_CYCLE_V1" and rec["adapter"] != "context":
                raise p.AdmissionError("cycle primary status requires the contextual cycle adapter")
        else:
            rec = verify_execution(folder, **{k: row[k] for k in ("event_id", "competition", "endpoint")})
            if statuses[0] == "MODEL_ASSISTED_CYCLE_V1":
                raise p.AdmissionError("cycle primary status requires a cycle execution")
        if statuses[0] in ("MODEL_ASSISTED_PRIMARY_V3", "MODEL_ASSISTED_CYCLE_V1") and rec["status"] != "EXECUTED":
            raise p.AdmissionError("numeric primary card requires successful execution")
        if rec["status"] == "FAILED":
            failed += 1
            research_only += 1
            if row["feedback_status"] != "NOT_APPLICABLE_NO_MODEL" or not row["reason"]:
                raise p.AdmissionError("failed execution cannot supply model feedback")
        else:
            executed += 1
            state = row["feedback_status"]
            if state == "FEEDBACK_RETAINED":
                path = manifest.parent / row["feedback_path"]
                p.receipt_file(path, row["feedback_sha256"])
                feedback = p.read_rows(path)
                if len(feedback) != 1 or feedback[0]["event_id"] != row["event_id"]:
                    raise p.AdmissionError("one exact-event effective feedback row required")
                if cycle_attempt and rec["adapter"] == "context":
                    from ml import cycle
                    model = cycle.verify_bundle(folder / "BUNDLE")
                else:
                    model = p.verify_bundle(folder / "BUNDLE")
                if Path(feedback[0]["bundle"]).resolve() != (folder / "BUNDLE").resolve():
                    raise p.AdmissionError("feedback belongs to another execution")
                if cycle_attempt and rec["adapter"] == "context":
                    cycle.verify_settlement(path.parent)
                    count = 1
                else:
                    _, count = p.feedback_losses(feedback, model["context"], feedback[0]["available_at"])
                if count != 1:
                    raise p.AdmissionError("retained feedback is not admitted")
                feedback_count += 1
            elif state not in ("PENDING_EVENT", "BLOCKED_WITH_EVIDENCE") or not row["reason"]:
                raise p.AdmissionError("explicit pending/blocked feedback reason required")
        if row["feedback_status"] != "FEEDBACK_RETAINED" and (row["feedback_path"] or row["feedback_sha256"]):
            raise p.AdmissionError("non-retained feedback cannot name a learning row")
    return dict(cards=len(cards), executed=executed, failed=failed, feedback_retained=feedback_count,
                research_only=research_only)
