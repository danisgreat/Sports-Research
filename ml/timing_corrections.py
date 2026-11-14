"""Append-only official-first-play reviews; original adjustment-ledger rows never change."""
from __future__ import annotations

import contextlib
import csv
import hashlib
import io
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

from ml import timing

PATH = "research/adjustment_ledger/TIMING_CORRECTIONS.csv"
FIELDS = ("sequence", "local_key", "ledger_rows_sha256", "previous_timing", "effective_timing", "actual_start",
          "source_url", "evidence_path", "evidence_sha256", "recorded_at", "reason", "prev_sha256", "row_sha256")
PROOF_FIELDS = ("local_key", "actual_start", "source_url", "observed_at", "note")


def csv_bytes(fields, rows):
    out = io.StringIO(newline="")
    w = csv.DictWriter(out, fieldnames=fields, lineterminator="\n")
    w.writeheader(); w.writerows(rows)
    return out.getvalue().encode("utf-8")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def evidence_file(root, relative):
    root = Path(root).resolve(); p = (root / relative).resolve()
    if not p.is_relative_to(root) or not p.is_file():
        raise ValueError("missing/outside-root official first-play evidence")
    return p


def check_proof(path, key, actual_start, source_url, recorded_at):
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if tuple(reader.fieldnames or ()) != PROOF_FIELDS:
            raise ValueError("first-play evidence requires exact normalized CSV columns: " + ",".join(PROOF_FIELDS))
        rows = list(reader)
    if len(rows) != 1 or set(rows[0]) != set(PROOF_FIELDS) or any(v is None for v in rows[0].values()):
        raise ValueError("one complete first-play fact required")
    fact = rows[0]
    if fact["local_key"] != key or fact["source_url"] != source_url or not fact["note"].strip():
        raise ValueError("first-play evidence does not identify this card/source")
    if timing.clock(fact["actual_start"], "proof actual_start") != timing.clock(actual_start, "actual_start"):
        raise ValueError("first-play evidence contradicts correction time")
    observed = timing.clock(fact["observed_at"], "proof observed_at")
    if not timing.clock(actual_start, "actual_start") <= observed <= timing.clock(recorded_at, "recorded_at"):
        raise ValueError("first-play evidence observation is before play or after correction")


def read(root):
    path = Path(root) / PATH
    if not path.exists():
        return []
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if tuple(reader.fieldnames or ()) != FIELDS:
            raise ValueError("timing corrections schema mismatch")
        rows = list(reader)
    previous = ""
    for n, r in enumerate(rows, 1):
        if set(r) != set(FIELDS) or any(v is None for v in r.values()):
            raise ValueError("malformed timing correction")
        if r["sequence"] != str(n) or r["prev_sha256"] != previous or sha(csv_bytes(FIELDS[:-1], [{k: r[k] for k in FIELDS[:-1]}])) != r["row_sha256"]:
            raise ValueError("timing corrections chain mismatch")
        if r["effective_timing"] not in ("PRE_START_RESEARCH", "POST_START_ISSUE"):
            raise ValueError("invalid effective timing")
        url = urlparse(r["source_url"])
        if url.scheme not in ("http", "https") or not url.hostname or not r["reason"].strip():
            raise ValueError("official first-play source/reason missing")
        if timing.clock(r["recorded_at"], "recorded_at") < timing.clock(r["actual_start"], "actual_start"):
            raise ValueError("timing correction was recorded before actual first play")
        p = evidence_file(root, r["evidence_path"])
        if not p.stat().st_size or sha(p.read_bytes()) != r["evidence_sha256"]:
            raise ValueError("official first-play evidence hash mismatch")
        check_proof(p, r["local_key"], r["actual_start"], r["source_url"], r["recorded_at"])
        previous = r["row_sha256"]
    return rows


def card_rows(ledger, key):
    from ml import ledger as L
    rows = ledger[ledger.local_key == key]
    if rows.empty or set(rows.timing) != {"PRE_START_RESEARCH"}:
        raise ValueError("timing correction requires an original PRE_START_RESEARCH card")
    if len(set(rows.timing_evidence)) != 1 or len(set(rows.issued_at)) != 1:
        raise ValueError("inconsistent original timing declarations")
    evidence = rows.iloc[0].timing_evidence
    m = re.fullmatch(r"DECLARED_RESEARCH_START:([^|]+)\|NOT_STARTED:(.+)@([^|]+)", evidence)
    if not m:
        raise ValueError("original research/observation evidence missing")
    meta = dict(research_started_at=m[1], not_started_source=m[2], not_started_observed_at=m[3],
                issued_at=rows.iloc[0].issued_at, outcome_exposure="NONE_RECORDED")
    errors = timing.problems(meta)
    if errors:
        raise ValueError("invalid original timing declaration: " + " | ".join(errors))
    # Include original chain identities; appending unrelated cards cannot alter this binding.
    binding = sha(csv_bytes(tuple(ledger.columns), rows.to_dict("records")))
    return binding, meta


def reviewed_phase(meta, actual_start):
    return "POST_START_ISSUE" if timing.problems(meta, actual_start=actual_start) else "PRE_START_RESEARCH"


def apply(ledger, root):
    """Only reviewed originals can join the pooled pre-start scoring cohort."""
    result = ledger.copy()
    result["timing_revision"] = "ORIGINAL"
    pending = result.timing == "PRE_START_RESEARCH"
    result.loc[pending, "timing"] = "TIMING_UNVERIFIED"
    result.loc[pending, "timing_revision"] = "PENDING_OFFICIAL_FIRST_PLAY"
    current = {}
    for row in read(root):
        key = row["local_key"]
        binding, meta = card_rows(ledger, key)
        prior = current.get(key, "PRE_START_RESEARCH")
        if row["ledger_rows_sha256"] != binding or row["previous_timing"] != prior or row["effective_timing"] != reviewed_phase(meta, row["actual_start"]):
            raise ValueError("timing correction is stale, misbound or contradicts its first-play evidence")
        current[key] = row["effective_timing"]
        result.loc[result.local_key == key, "timing"] = row["effective_timing"]
        result.loc[result.local_key == key, "timing_revision"] = row["row_sha256"]
    return result


@contextlib.contextmanager
def locked(path):
    lock = path.with_suffix(".lock")
    with lock.open("x") as f:
        f.write(str(os.getpid()))
    try:
        yield
    finally:
        lock.unlink()


def correct(ledger_path, key, actual_start, source_url, evidence, reason, *, root, at=None):
    from ml import ledger as L
    root = Path(root)
    ledger = L.read(Path(ledger_path))
    binding, meta = card_rows(ledger, key)
    stamp = at or datetime.now(timezone.utc).isoformat()
    if timing.clock(stamp, "recorded_at") < timing.clock(actual_start, "actual_start"):
        raise ValueError("cannot settle timing before first play")
    source = urlparse(source_url)
    if source.scheme not in ("http", "https") or not source.hostname or not reason.strip():
        raise ValueError("official source URL and review reason required")
    p = evidence_file(root, evidence)
    if not p.stat().st_size:
        raise ValueError("official evidence is empty")
    check_proof(p, key, actual_start, source_url, stamp)
    path = root / PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    with locked(path):
        prior_rows = read(root)
        apply(ledger, root)  # Reject a broken earlier chain before appending.
        same = [r for r in prior_rows if r["local_key"] == key]
        phase = reviewed_phase(meta, actual_start)
        if same and all(same[-1][k] == v for k, v in dict(actual_start=actual_start, source_url=source_url,
                             evidence_sha256=sha(p.read_bytes()), reason=reason).items()):
            return dict(status="ALREADY_EXISTS", effective_timing=phase, row_sha256=same[-1]["row_sha256"])
        row = dict(sequence=str(len(prior_rows) + 1), local_key=key, ledger_rows_sha256=binding,
                   previous_timing=same[-1]["effective_timing"] if same else "PRE_START_RESEARCH", effective_timing=phase,
                   actual_start=actual_start, source_url=source_url, evidence_path=p.resolve().relative_to(root.resolve()).as_posix(),
                   evidence_sha256=sha(p.read_bytes()), recorded_at=stamp, reason=reason,
                   prev_sha256=prior_rows[-1]["row_sha256"] if prior_rows else "")
        row["row_sha256"] = sha(csv_bytes(FIELDS[:-1], [row]))
        data = csv_bytes(FIELDS, [row])
        with path.open("ab") as f:
            f.write(data.split(b"\n", 1)[1] if f.tell() else data)
            f.flush(); os.fsync(f.fileno())
        return dict(status="APPENDED", effective_timing=phase, row_sha256=row["row_sha256"])
