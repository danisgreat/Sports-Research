"""HPPV-v1: historical evidence assessment, isolated from ONE-CHAT-v3.

All 685 cards remain in a frozen census. Default inputs are preserved records,
not proof of original publication. Reviewed, hash-bound evidence can qualify
individual original contracts. No command writes to the prospective registry.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import math
import re
import subprocess
import tempfile
from collections import Counter, defaultdict
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path

import numpy as np
from scipy import stats

ROOT = Path(__file__).resolve().parents[1]
BASE = "research/verification/historical_pre_event_v1"
# The current verified run. A run binds this file's exact bytes, so a code change needs a new run; the initial run
# in BASE stays unchanged and verifies at its implementation commit (8f2f38f).
CURRENT_RUN = "research/verification/hppv_runs/2026-11-17-1"
TRAIN = "research/card_training/2026-11-16-1/ROWS.csv"
AUDIT = "research/verification/framework_change_2026-11-16-4/historical_evidence/HISTORICAL_CARD_AUDIT.csv"
VERSION = "HPPV-v1"
FROZEN_COMMIT = "4e0cb198c50230d8e2abf2f1a976d92338301520"
EXPECTED_CARDS = 685
EXPECTED_ROWS = 3150
MIN_EVENTS = 100
MIN_ADVANTAGE = 0.01
SNAPSHOT_KEYS = ("row_id", "card", "rank", "contract", "p")
LEDGER_FIELDS = (
    "revision",
    "row_id",
    "recorded_at",
    "reviewer",
    "reason",
    "previous_sha256",
    "payload",
    "sha256",
)
IDENTITY_KEYS = {
    "event_id",
    "market",
    "selection",
    "line",
    "period",
    "unit",
    "overtime",
    "probability_basis",
    "origin",
}


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def input_bytes(root, name):
    if name.startswith("git:"):
        _, commit, path = name.split(":", 2)
        if commit != FROZEN_COMMIT:
            raise ValueError("unregistered historical source commit")
        result = subprocess.run(
            ["git", "show", commit + ":" + path], cwd=root, capture_output=True
        )
        return result.stdout if result.returncode == 0 else None
    path = Path(root) / name
    return path.read_bytes() if path.is_file() else None


def input_digest(root, name):
    raw = input_bytes(root, name)
    return digest(raw) if raw is not None else "MISSING"


def canonical(value):
    return json.dumps(
        value,
        sort_keys=True,
        ensure_ascii=False,
        separators=(",", ":"),
        allow_nan=False,
    )


def read_csv(path):
    with Path(path).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def csv_bytes(rows, fields):
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue().encode()


def timestamp(value):
    dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if dt.tzinfo is None or dt.utcoffset() is None:
        raise ValueError("timestamp requires a timezone")
    return dt.astimezone(timezone.utc)


def probability(value):
    p = float(value)
    if not math.isfinite(p) or not 0 <= p <= 1:
        raise ValueError("probability outside [0,1]")
    return p


def local_path(root, name):
    path = (Path(root) / name).resolve()
    if not path.is_relative_to(Path(root).resolve()) or not path.is_file():
        raise ValueError(f"missing or external evidence: {name}")
    return path


def artifact(root, ref, inputs):
    """A capture binds bytes; its URL and reviewer supply provenance, not timing by themselves."""
    if not isinstance(ref, dict) or not ref.get("url", "").startswith("https://"):
        raise ValueError("evidence needs a source URL and local capture")
    path = local_path(root, ref["path"])
    raw = path.read_bytes()
    if digest(raw) != ref["sha256"]:
        raise ValueError(f"evidence hash mismatch: {ref['path']}")
    inputs[ref["path"]] = digest(raw)
    return raw


def reviewed(root, proof, inputs):
    if (
        not isinstance(proof, dict)
        or not proof.get("reviewer")
        or not proof.get("finding")
    ):
        raise ValueError("independent review and finding required")
    timestamp(proof["reviewed_at"])
    return artifact(root, proof["capture"], inputs)


def load_ledger(path=None, *, raw=None):
    rows = (
        read_csv(path)
        if raw is None
        else list(csv.DictReader(io.StringIO(raw.decode("utf-8"))))
    )
    previous, revisions = "", Counter()
    for row in rows:
        rid = row["row_id"]
        revisions[rid] += 1
        if row["revision"] != str(revisions[rid]) or row["previous_sha256"] != previous:
            raise ValueError("evidence revision chain broken")
        body = {k: row[k] for k in LEDGER_FIELDS if k != "sha256"}
        if digest(canonical(body).encode()) != row["sha256"]:
            raise ValueError("evidence revision hash changed")
        timestamp(row["recorded_at"])
        if (
            not row["reviewer"]
            or not row["reason"]
            or not isinstance(json.loads(row["payload"]), dict)
        ):
            raise ValueError("evidence revision missing review or payload")
        previous = row["sha256"]
    return rows


def append_evidence(root, ledger, row_id, payload, reviewer, reason):
    """Append a full replacement assessment; earlier evidence and tier decisions survive."""
    root, ledger = Path(root), Path(ledger)
    known = {r["row_id"]: r for r in read_csv(root / TRAIN)}
    if row_id not in known or not reviewer.strip() or not reason.strip():
        raise ValueError("unknown row or missing reviewer/reason")
    before = ledger.read_bytes()
    rows = load_ledger(ledger)
    # Validate even superseded evidence on every rebuild; cannot erase inconvenient proof.
    assess(known[row_id], payload, root, {})
    row = dict(
        revision=str(1 + sum(r["row_id"] == row_id for r in rows)),
        row_id=row_id,
        recorded_at=datetime.now(timezone.utc).isoformat(),
        reviewer=reviewer,
        reason=reason,
        previous_sha256=rows[-1]["sha256"] if rows else "",
        payload=canonical(payload),
    )
    row["sha256"] = digest(canonical(row).encode())
    # Exclusive lock serializes writers and avoids a lost append from parallel reviewers (Windows and POSIX).
    from ml import file_lock

    with file_lock.exclusive(ledger, wait=10.0, what="the evidence ledger"):
        with ledger.open("r+b") as f:
            if f.read() != before:
                raise ValueError("ledger changed; inspect new head before retrying")
            f.seek(0, 2)
            f.write(csv_bytes([row], LEDGER_FIELDS).split(b"\n", 1)[1])
            f.flush()
    return row


def validate_identity(identity, row):
    if not isinstance(identity, dict) or set(identity) != IDENTITY_KEYS:
        raise ValueError("incomplete exact contract identity")
    if any(not str(identity[k]).strip() for k in IDENTITY_KEYS - {"line"}):
        raise ValueError("blank contract identity")
    if identity["origin"] not in {"USER_SUPPLIED", "ANALYST_ALTERNATIVE", "UNKNOWN"}:
        raise ValueError("unknown contract origin")
    if identity["market"] not in {"WINNER", "HANDICAP", "TOTAL", "PROP"}:
        raise ValueError("unsupported market identity")
    if identity["probability_basis"] not in {
        "UNCONDITIONAL_BINARY",
        "CONDITIONAL_DECISIVE",
        "THREE_WAY",
    }:
        raise ValueError("unknown probability basis")
    # Require literal signed handicaps and literal totals, preserving magnitude and units.
    text = row["contract"].replace("−", "-").replace("–", "-")
    if identity["market"] in {"HANDICAP", "TOTAL"}:
        pattern = (
            r"[+-]\d+(?:\.\d+)?"
            if identity["market"] == "HANDICAP"
            else r"(?<![\d.])\d+(?:\.\d+)?"
        )
        numbers = [float(x) for x in re.findall(pattern, text)]
        if not identity["line"] or float(identity["line"]) not in numbers:
            raise ValueError("line or handicap sign differs from original contract")


def assess(row, evidence, root, inputs):
    """Qualification ignores whether the forecast won; missing evidence stays explicit."""
    result = dict(
        row_id=row["row_id"],
        card=row["card"],
        tier="C",
        reason="ORIGINAL_ISSUANCE_UNVERIFIED",
        event_id="",
        method="UNKNOWN",
        competition="UNKNOWN",
        event_date="",
        teams="",
        issued_at="",
        first_play="",
        outcome_available_at="",
        baseline_kind="",
        identity="",
        outcome_verified=False,
        verified_grade="",
        paired=False,
        accuracy=False,
        p=row["p"],
        y="",
        baseline_p="",
        original_sha256="",
        forecast_source="",
        timing_source="",
        outcome_source="",
        baseline_source="",
    )
    if not row["contract"]:
        result.update(tier="E", reason="ORIGINAL_CONTRACT_MISSING")
    if not evidence:
        return result
    original = evidence.get("original")
    event = evidence.get("event")
    outcome = evidence.get("outcome")
    baseline = evidence.get("baseline")
    if original:
        raw = artifact(root, original["capture"], inputs)
        # The recovered record transcription is separately hash-bound and reviewed against
        # the raw original capture; exact probabilities/ranks cannot silently be replaced.
        snapshot = json.loads(artifact(root, original["transcription"], inputs))
        if snapshot.get("forecast") != {k: row[k] for k in SNAPSHOT_KEYS}:
            raise ValueError("original probability, rank, card or contract altered")
        reviewed(root, original["integrity_review"], inputs)
        if original["integrity_review"].get("first_recoverable_unchanged") is not True:
            raise ValueError(
                "original forecast not established as earliest unchanged version"
            )
        identity = snapshot["identity"]
        validate_identity(identity, row)
        if snapshot["method"] in {"", "UNKNOWN"}:
            raise ValueError("original operating method required")
        result.update(
            original_sha256=digest(raw),
            forecast_source=original["capture"]["url"],
            method=snapshot["method"],
            identity=canonical(identity),
            event_id=identity["event_id"],
            tier="B",
            reason="ORIGINAL_RECOVERED_TIMING_UNVERIFIED",
        )
    if event:
        reviewed(root, event["proof"], inputs)
        first = timestamp(event["actual_first_play"])
        if (
            event["proof"].get("actual_first_play_verified") is not True
            or len(event["teams"]) < 2
            or not event["competition"]
        ):
            raise ValueError("actual first play, competition and participants required")
        if original and event["event_id"] != result["event_id"]:
            raise ValueError("event identity mismatch")
        result.update(
            event_id=event["event_id"],
            competition=event["competition"],
            first_play=first.isoformat(),
            event_date=first.date().isoformat(),
            teams=canonical(sorted(event["teams"])),
        )
    if original and original.get("publication"):
        pub = original["publication"]
        reviewed(root, pub, inputs)
        issued = timestamp(pub["issued_at"])
        if (
            pub.get("independent_timestamp") is not True
            or pub.get("bound_original_sha256") != result["original_sha256"]
        ):
            raise ValueError("timestamp not independently bound to original bytes")
        result.update(issued_at=issued.isoformat(), timing_source=pub["capture"]["url"])
        if event and issued >= timestamp(result["first_play"]):
            result.update(tier="D", reason="FIRST_RECORDED_AT_OR_AFTER_FIRST_PLAY")
        elif event:
            review = original["integrity_review"]
            if (
                review.get("no_post_issue_information") is True
                and timestamp(review["information_cutoff"]) <= issued
            ):
                result.update(
                    tier="A", reason="INDEPENDENT_PRE_EVENT_ORIGINAL_VERIFIED"
                )
            else:
                result.update(reason="INFORMATION_CUTOFF_OR_LEAKAGE_UNVERIFIED")
    if evidence.get("known_outcome_exposed") is True:
        reviewed(root, evidence["exposure_proof"], inputs)
        result.update(tier="D", reason="KNOWN_OUTCOME_EXPOSED")
    if evidence.get("incomplete_reason"):
        result.update(tier="E", reason=evidence["incomplete_reason"])
    if outcome:
        reviewed(root, outcome["proof"], inputs)
        if (
            not original
            or not event
            or outcome["identity"] != json.loads(result["identity"])
        ):
            raise ValueError("outcome endpoint mismatch or missing original/event")
        if outcome["proof"].get("independent_result") is not True or not outcome.get(
            "grading_rule"
        ):
            raise ValueError("independent outcome source and grading rule required")
        if outcome["grade"] not in {
            "WIN",
            "LOSS",
            "PUSH",
            "VOID",
            "UNRESOLVED",
            "UNATTAINABLE",
        }:
            raise ValueError("unsupported outcome grade")
        if outcome["grade"] != row["grade"]:
            revision = outcome.get("settlement_revision", {})
            reviewed(root, revision, inputs)
            if (
                revision.get("previous_grade") != row["grade"]
                or revision.get("corrected_grade") != outcome["grade"]
            ):
                raise ValueError("settlement revision does not preserve frozen grade")
        available = timestamp(outcome["available_at"])
        if available < timestamp(result["first_play"]):
            raise ValueError("outcome available before first play")
        result.update(
            outcome_verified=True,
            verified_grade=outcome["grade"],
            outcome_source=outcome["proof"]["capture"]["url"],
            outcome_available_at=available.isoformat(),
            y="1"
            if outcome["grade"] == "WIN"
            else "0"
            if outcome["grade"] == "LOSS"
            else "",
        )
    if baseline:
        reviewed(root, baseline["proof"], inputs)
        if (
            not original
            or not result["issued_at"]
            or baseline["identity"] != json.loads(result["identity"])
        ):
            raise ValueError("baseline endpoint or information cutoff unverified")
        recipe = json.loads(artifact(root, baseline["recipe"], inputs))
        if recipe != {
            k: baseline[k]
            for k in (
                "identity",
                "p",
                "kind",
                "information_cutoff",
                "feature_cutoff",
                "training_outcome_cutoff",
                "hyperparameter_cutoff",
            )
        }:
            raise ValueError("baseline recipe differs from recorded values")
        if (
            baseline["kind"] not in {"FROZEN_PRE_EVENT", "RETROSPECTIVE_SPORTS_ONLY"}
            or baseline["proof"].get("sports_only_market_blind") is not True
        ):
            raise ValueError("baseline must be sports-only and explicitly labelled")
        cutoff = timestamp(baseline["information_cutoff"])
        if cutoff > timestamp(result["issued_at"]) or any(
            timestamp(baseline[k]) > cutoff
            for k in (
                "feature_cutoff",
                "training_outcome_cutoff",
                "hyperparameter_cutoff",
            )
        ):
            raise ValueError("baseline future information leakage")
        if baseline["kind"] == "FROZEN_PRE_EVENT":
            if (
                baseline["proof"].get("independent_timestamp") is not True
                or baseline["proof"].get("bound_recipe_sha256")
                != baseline["recipe"]["sha256"]
                or timestamp(baseline["proof"]["issued_at"])
                > timestamp(result["issued_at"])
            ):
                raise ValueError("frozen baseline publication unverified")
        elif baseline["proof"].get("outcome_blind_reconstruction") is not True:
            raise ValueError(
                "retrospective baseline selection/tuning exposed to test outcomes"
            )
        result.update(
            baseline_kind=baseline["kind"],
            baseline_p=probability(baseline["p"]),
            baseline_source=baseline["proof"]["capture"]["url"],
        )
    binary = bool(original) and json.loads(result["identity"])["probability_basis"] in {
        "UNCONDITIONAL_BINARY",
        "CONDITIONAL_DECISIVE",
    }
    result["accuracy"] = (
        result["tier"] == "A"
        and result["outcome_verified"]
        and result["y"] != ""
        and binary
    )
    try:
        probability(row["p"])
        has_p = True
    except (ValueError, TypeError):
        has_p = False
    result["paired"] = (
        result["accuracy"]
        and has_p
        and bool(baseline)
        and json.loads(result["identity"])["origin"] == "USER_SUPPLIED"
    )
    return result


def interval(values):
    values = np.asarray(values, dtype=float)
    n = len(values)
    mean = float(values.mean()) if n else ""
    if n < 2:
        return mean, "", "", n
    half = float(stats.t.ppf(0.975, n - 1) * values.std(ddof=1) / math.sqrt(n))
    return mean, mean - half, mean + half, n


def log_loss(p, y):
    # Preserve original p for Brier; explicit epsilon only for finite log loss.
    p = min(1 - 1e-15, max(1e-15, p))
    return -(y * math.log(p) + (1 - y) * math.log1p(-p))


def metrics(rows, label, stratum):
    numeric = []
    for r in rows:
        try:
            if r["accuracy"]:
                numeric.append((r, probability(r["p"])))
        except (ValueError, TypeError):
            pass
    paired = [r for r in rows if r["paired"]]
    per_event = defaultdict(list)
    for r in paired:
        y, p, b = int(r["y"]), probability(r["p"]), probability(r["baseline_p"])
        per_event[r["event_id"]].append(
            ((p - y) ** 2, (b - y) ** 2, log_loss(p, y), log_loss(b, y))
        )
    event_scores = {e: np.mean(v, axis=0) for e, v in per_event.items()}
    mean, low, high, n = interval([v[1] - v[0] for v in event_scores.values()])
    means = np.mean(list(event_scores.values()), axis=0) if n else ["", "", "", ""]
    rank = lambda k: [r for r in rows if r["accuracy"] and r["rank"] == str(k)]
    r1, r2 = rank(1), rank(2)
    output = dict(
        dimension=label,
        stratum=stratum,
        interpretation="EXPLORATORY_POST_OUTCOME_HISTORICAL",
        rows=len(rows),
        verified_accuracy_rows=sum(r["accuracy"] for r in rows),
        probability_rows=len(numeric),
        paired_rows=len(paired),
        events=n,
        effective_event_n=n,
        event_mean_brier=means[0],
        baseline_brier=means[1],
        paired_brier_advantage=mean,
        interval_low=low,
        interval_high=high,
        brier_skill_score=(1 - means[0] / means[1]) if n and means[1] else "",
        event_mean_log_loss=means[2],
        baseline_log_loss=means[3],
        accuracy_brier=float(np.mean([(p - int(r["y"])) ** 2 for r, p in numeric]))
        if numeric
        else "",
        accuracy_log_loss=float(np.mean([log_loss(p, int(r["y"])) for r, p in numeric]))
        if numeric
        else "",
        rank1_n=len(r1),
        rank1_hit_rate=sum(int(r["y"]) for r in r1) / len(r1) if r1 else "",
        rank2_n=len(r2),
        rank2_hit_rate=sum(int(r["y"]) for r in r2) / len(r2) if r2 else "",
    )
    sensitivities = []
    # A team appearing in several events induces an overlapping dependency graph.
    # Connected components conservatively group all linked games, rather than pretend
    # that each team or contract is an independent observation.
    for dimension in ("event_date", "competition", "teams"):
        groups, labels = defaultdict(list), {}
        for r in paired:
            labels.setdefault(r["event_id"], r)
        parent = {e: e for e in labels}

        def find(e):
            while parent[e] != e:
                parent[e] = parent[parent[e]]
                e = parent[e]
            return e

        if dimension == "teams":
            seen = {}
            for e, r in labels.items():
                for team in json.loads(r["teams"]):
                    key = (r["sport"], team)
                    if key in seen:
                        parent[find(e)] = find(seen[key])
                    seen[key] = e
        for e, v in event_scores.items():
            key = find(e) if dimension == "teams" else labels[e][dimension]
            groups[key].append(v[1] - v[0])
        m, lo, hi, count = interval([np.mean(g) for g in groups.values()])
        sensitivities.append(
            dict(
                dimension=label,
                stratum=stratum,
                block=dimension,
                blocks=count,
                block_mean_advantage=m,
                interval_low=lo,
                interval_high=hi,
                reason="" if count >= 2 else "INSUFFICIENT_INDEPENDENT_BLOCKS",
            )
        )
    calibration = []
    for b in range(10):
        cell = [(r, p) for r, p in numeric if min(9, int(p * 10)) == b]
        by_event = defaultdict(list)
        for r, p in cell:
            by_event[r["event_id"]].append((p, int(r["y"])))
        event_values = [np.mean(v, axis=0) for v in by_event.values()]
        calibration.append(
            dict(
                dimension=label,
                stratum=stratum,
                bin_low=b / 10,
                bin_high=(b + 1) / 10,
                rows=len(cell),
                events=len(by_event),
                mean_p=float(np.mean(event_values, axis=0)[0]) if cell else "",
                observed=float(np.mean(event_values, axis=0)[1]) if cell else "",
            )
        )
    return output, sensitivities, calibration


def verdict(score, accuracy_events):
    if not accuracy_events:
        return "HISTORICAL_EVIDENCE_INSUFFICIENT"
    if not score["events"]:
        return "HISTORICAL_PRE_EVENT_ACCURACY_MEASURED"
    if score["events"] < MIN_EVENTS or score["interval_low"] == "":
        return "HISTORICAL_SKILL_INCONCLUSIVE"
    if score["paired_brier_advantage"] >= MIN_ADVANTAGE and score["interval_low"] > 0:
        return "HISTORICAL_PRE_EVENT_SKILL_SUPPORTED"
    if score["interval_high"] < MIN_ADVANTAGE:
        return "HISTORICAL_PERFORMANCE_NOT_SUPPORTED"
    return "HISTORICAL_SKILL_INCONCLUSIVE"


def deduplicate(decisions):
    """Earliest original issuance wins; conflicts are integrity failures, not exclusions."""
    seen, event_metadata = {}, {}
    for d in sorted(decisions, key=lambda d: (d["issued_at"] or "9999", d["row_id"])):
        if not d["event_id"] or not d["identity"]:
            continue
        if d["first_play"]:
            meta = (d["first_play"], d["competition"], d["teams"], d["sport"])
            if event_metadata.setdefault(d["event_id"], meta) != meta:
                raise ValueError("conflicting metadata for same sporting event")
        identity = json.loads(d["identity"])
        identity.pop("origin")
        if identity["line"] != "":
            identity["line"] = str(Decimal(identity["line"]).normalize())
        key = (d["event_id"], canonical(identity))
        if d["accuracy"]:
            if key in seen:
                old = seen[key]
                if old["y"] != d["y"] or (
                    old["issued_at"] == d["issued_at"] and old["p"] != d["p"]
                ):
                    raise ValueError(
                        "conflicting duplicate original forecast or verified outcome"
                    )
                d.update(
                    accuracy=False,
                    paired=False,
                    reason=d["reason"] + ";DUPLICATE_EVENT_CONTRACT",
                )
            else:
                seen[key] = d


def build(root=ROOT, *, ledger_raw=None):
    root = Path(root)
    rows, audit = read_csv(root / TRAIN), read_csv(root / AUDIT)
    receipt_path = "research/card_training/2026-11-16-1/RECEIPT.csv"
    receipt = read_csv(root / receipt_path)[0]
    if digest((root / TRAIN).read_bytes()) != receipt["rows_sha256"]:
        raise ValueError("frozen original rows changed from training receipt")
    expected = {f"P-{i:03d}" for i in range(1, EXPECTED_CARDS + 1)}
    cards = [r["card"] for r in audit]
    if len(cards) != len(set(cards)) or set(cards) != expected:
        raise ValueError("duplicate canonical ID or historical census omission")
    if (
        len(rows) != EXPECTED_ROWS
        or {r["card"] for r in rows} != expected
        or len({r["row_id"] for r in rows}) != len(rows)
    ):
        raise ValueError("duplicate row ID or selective row/card omission")
    by_card = defaultdict(list)
    for r in rows:
        by_card[r["card"]].append(r)
    for a in audit:
        g = by_card[a["card"]]
        if (
            len(g) != int(a["rows"])
            or sum(r["admission"] != "EXCLUDED" for r in g) != int(a["admitted_rows"])
            or sum(r["admission"] == "OUTCOME_AND_CALIBRATION" for r in g)
            != int(a["probability_rows"])
        ):
            raise ValueError("census and training admissions disagree")
    ledger_path = BASE + "/EVIDENCE_REVISIONS.csv"
    inputs = {
        p: digest((root / p).read_bytes())
        for p in (
            TRAIN,
            AUDIT,
            receipt_path,
            BASE + "/REGISTRATION.md",
            "ml/historical_pre_event.py",
        )
    }
    # Bind the census back to every preserved training input and its original hash.
    training_inputs = "research/card_training/2026-11-16-1/INPUTS.csv"
    inputs[training_inputs] = digest((root / training_inputs).read_bytes())
    source_reconciliation = []
    if subprocess.run(
        ["git", "cat-file", "-e", FROZEN_COMMIT + "^{commit}"],
        cwd=root,
        capture_output=True,
    ).returncode:
        raise ValueError(
            "frozen source commit unavailable; fetch the repository history"
        )
    for name in (TRAIN, AUDIT, receipt_path, training_inputs):
        reference = "git:" + FROZEN_COMMIT + ":" + name
        if input_digest(root, reference) != inputs[name]:
            raise ValueError(
                "frozen census, probabilities or receipts changed from registered commit"
            )
        inputs[reference] = inputs[name]
    for r in read_csv(root / training_inputs):
        source_ref = "git:" + FROZEN_COMMIT + ":" + r["path"]
        raw = input_bytes(root, source_ref)
        actual = digest(raw) if raw is not None else "MISSING"
        match = "EXACT"
        # The older Windows run hashed CRLF before Git normalized some CSVs.
        # Permit only that explicit, reversible newline representation; never use
        # it for original publication evidence, which always needs exact bytes.
        if (
            actual != r["sha256"]
            and raw is not None
            and digest(raw.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n"))
            == r["sha256"]
        ):
            match = "CRLF_EQUIVALENT_TRAINING_INPUT_ONLY"
        elif actual != r["sha256"]:
            raise ValueError(f"frozen training source changed: {r['path']}")
        inputs[source_ref] = actual
        source_reconciliation.append(
            dict(
                path=r["path"],
                training_sha256=r["sha256"],
                frozen_blob_sha256=actual,
                source_ref=source_ref,
                match=match,
            )
        )
    ledger_raw = (root / ledger_path).read_bytes() if ledger_raw is None else ledger_raw
    ledger, latest, history = load_ledger(raw=ledger_raw), {}, []
    known = {r["row_id"]: r for r in rows}
    for rev in ledger:
        if rev["row_id"] not in known:
            raise ValueError("evidence for unknown census row")
        payload = json.loads(rev["payload"])
        decision = assess(known[rev["row_id"]], payload, root, inputs)
        history.append(
            dict(
                row_id=rev["row_id"],
                revision=rev["revision"],
                recorded_at=rev["recorded_at"],
                reviewer=rev["reviewer"],
                reason=rev["reason"],
                tier=decision["tier"],
                qualification_reason=decision["reason"],
                evidence_sha256=rev["sha256"],
            )
        )
        latest[rev["row_id"]] = payload
    decisions = []
    for row in rows:
        d = assess(row, latest.get(row["row_id"], {}), root, inputs)
        decisions.append(dict(row, admission_reason=row["reason"], **d))
    deduplicate(decisions)
    outputs = {"EVIDENCE_SNAPSHOT.csv": ledger_raw}

    def emit(name, records, fields):
        outputs[name] = csv_bytes(records, fields)

    emit(
        "SOURCE_RECONCILIATION.csv",
        source_reconciliation,
        ("path", "training_sha256", "frozen_blob_sha256", "source_ref", "match"),
    )
    census = []
    for a in audit:
        group = [d for d in decisions if d["card"] == a["card"]]
        census.append(
            dict(
                a,
                sports=";".join(sorted({d["sport"] for d in group})),
                dates=";".join(sorted({d["date"] for d in group})),
                contracts=canonical([d["contract"] for d in group]),
                original_probabilities=canonical([d["p"] for d in group]),
                original_ranks=canonical([d["rank"] for d in group]),
                settlement_statuses=";".join(sorted({d["grade"] for d in group})),
                source_references=";".join(sorted({d["source"] for d in group})),
                training_exclusions=";".join(
                    f"{d['row_id']}:{d['admission_reason']}"
                    for d in group
                    if d["admission"] == "EXCLUDED"
                ),
                competitions=";".join(sorted({d["competition"] for d in group})),
                tiers=";".join(
                    f"{k}:{v}"
                    for k, v in sorted(Counter(d["tier"] for d in group).items())
                ),
                original_methods=";".join(sorted({d["method"] for d in group})),
                exclusion_reasons=";".join(
                    sorted({d["reason"] for d in group if not d["paired"]})
                ),
            )
        )
    emit("HISTORICAL_CENSUS.csv", census, list(census[0]))
    emit("ORIGINAL_FORECASTS.csv", decisions, list(decisions[0]))
    emit(
        "TIMING_AND_CUSTODY_AUDIT.csv",
        [
            {
                k: d[k]
                for k in (
                    "row_id",
                    "card",
                    "tier",
                    "reason",
                    "issued_at",
                    "first_play",
                    "original_sha256",
                    "forecast_source",
                    "timing_source",
                )
            }
            for d in decisions
        ],
        (
            "row_id",
            "card",
            "tier",
            "reason",
            "issued_at",
            "first_play",
            "original_sha256",
            "forecast_source",
            "timing_source",
        ),
    )
    qfields = (
        "row_id",
        "card",
        "tier",
        "reason",
        "accuracy",
        "paired",
        "method",
        "event_id",
    )
    emit(
        "HISTORICAL_QUALIFICATION.csv",
        [{k: d[k] for k in qfields} for d in decisions],
        qfields,
    )
    emit(
        "QUALIFICATION_HISTORY.csv",
        history,
        (
            "row_id",
            "revision",
            "recorded_at",
            "reviewer",
            "reason",
            "tier",
            "qualification_reason",
            "evidence_sha256",
        ),
    )
    for name, fields in (
        (
            "VERIFIED_OUTCOMES.csv",
            (
                "row_id",
                "card",
                "event_id",
                "contract",
                "grade",
                "verified_grade",
                "outcome_verified",
                "y",
                "outcome_available_at",
                "outcome_source",
            ),
        ),
        (
            "HISTORICAL_BASELINES.csv",
            (
                "row_id",
                "card",
                "event_id",
                "identity",
                "baseline_p",
                "baseline_kind",
                "baseline_source",
                "paired",
            ),
        ),
    ):
        emit(name, [{k: d[k] for k in fields} for d in decisions], fields)
    scores, sensitivity, calibration = [], [], []
    # Never combine B/C/D/E rows with the verified A cohort; historical era is a
    # descriptive proxy only, while independently recovered method versions are separate.
    for dim in (
        "ALL",
        "method",
        "era",
        "sport",
        "competition",
        "family",
        "event_date",
        "baseline_kind",
    ):
        groups = (
            {"ALL": decisions}
            if dim == "ALL"
            else {
                k: [d for d in decisions if d[dim] == k]
                for k in sorted({d[dim] for d in decisions})
            }
        )
        for key, group in groups.items():
            s, checks, bins = metrics(group, dim, key)
            scores.append(s)
            sensitivity.extend(checks)
            calibration.extend(bins)
    emit("HISTORICAL_PERFORMANCE.csv", scores, list(scores[0]))
    emit("DEPENDENCE_SENSITIVITY.csv", sensitivity, list(sensitivity[0]))
    emit("CALIBRATION.csv", calibration, list(calibration[0]))
    descriptive = []
    for tier in "ABCDE":
        group = [d for d in decisions if d["tier"] == tier]
        scored = []
        for d in group:
            if d["grade"] not in {"WIN", "LOSS"}:
                continue
            try:
                scored.append((probability(d["p"]), int(d["grade"] == "WIN")))
            except (ValueError, TypeError):
                pass
        descriptive.append(
            dict(
                tier=tier,
                rows=len(group),
                cards=len({d["card"] for d in group}),
                preserved_probability_rows=len(scored),
                preserved_brier=float(np.mean([(p - y) ** 2 for p, y in scored]))
                if scored
                else "",
                interpretation="DESCRIPTIVE_PRESERVED_GRADES_NOT_VERIFIED_PRE_EVENT_SKILL",
            )
        )
    emit("EVIDENCE_TIER_SENSITIVITY.csv", descriptive, list(descriptive[0]))
    coverage = [
        dict(measure="census_cards", count=len(census)),
        dict(measure="contract_rows", count=len(rows)),
        dict(
            measure="cards_with_stated_probability",
            count=len({r["card"] for r in rows if r["p"]}),
        ),
        dict(measure="missing_probability_rows", count=sum(not r["p"] for r in rows)),
        dict(
            measure="explicit_abstention_rows",
            count=sum("ABSTENTION" in r["cohort"] for r in rows),
        ),
        dict(
            measure="request_level_abstention_frequency",
            count="UNKNOWN_NO_COMPLETE_REQUEST_CENSUS",
        ),
        dict(
            measure="tier_a_cards",
            count=len({d["card"] for d in decisions if d["tier"] == "A"}),
        ),
        dict(
            measure="fully_tier_a_cards",
            count=sum(
                all(d["tier"] == "A" for d in decisions if d["card"] == a["card"])
                for a in audit
            ),
        ),
    ]
    coverage += [
        dict(measure="grade_" + k, count=v)
        for k, v in sorted(Counter(r["grade"] for r in rows).items())
    ]
    coverage += [
        dict(measure="tier_" + k, count=sum(d["tier"] == k for d in decisions))
        for k in "ABCDE"
    ]
    coverage += [
        dict(
            measure="admitted_probability_rows",
            count=sum(r["admission"] == "OUTCOME_AND_CALIBRATION" for r in rows),
        ),
        dict(
            measure="admitted_outcome_only_rows",
            count=sum(r["admission"] == "OUTCOME_ONLY" for r in rows),
        ),
        dict(
            measure="excluded_training_rows",
            count=sum(r["admission"] == "EXCLUDED" for r in rows),
        ),
        dict(
            measure="numeric_contract_coverage_fraction",
            count=sum(bool(r["p"]) for r in rows) / len(rows),
        ),
        dict(
            measure="tier_a_contract_coverage_fraction",
            count=sum(d["tier"] == "A" for d in decisions) / len(rows),
        ),
    ]
    emit("COVERAGE.csv", coverage, ("measure", "count"))
    accuracy_events = len({d["event_id"] for d in decisions if d["accuracy"]})
    status = verdict(scores[0], accuracy_events)
    s = scores[0]
    report = f"""# Historical pre-event validation — {VERSION}

Track H verdict: **{status}**.

Frozen census: {len(census)} cards, {len(rows)} contract rows, P-001–P-685.
Cards with stated probabilities: {coverage[2]["count"]}. Tier-A contracts: {sum(d["tier"] == "A" for d in decisions)};
cards with at least one Tier-A contract: {coverage[6]["count"]}; fully Tier-A cards: {coverage[7]["count"]}.
Independently verified decisive events: {accuracy_events}. Same-contract supplied-line paired events: {s["events"]}.
Event-mean Brier advantage: {s["paired_brier_advantage"] if s["paired_brier_advantage"] != "" else "NOT_COMPUTABLE"};
95% event-level interval: [{s["interval_low"] if s["interval_low"] != "" else "NA"}, {s["interval_high"] if s["interval_high"] != "" else "NA"}].

Every row is retained with a qualification reason. Preserved source references, dates
inside documents, later imports and byte hashes alone do not prove pre-event issuance.
No evidence has been inferred from a winning or losing outcome. Default C classification
means original publication is unverified, not that the forecast was necessarily late.
Missing probabilities are not invented; PUSH, VOID, UNRESOLVED and UNATTAINABLE are
unscored. Conditional decisive probabilities are scored only on decisive outcomes;
three-way probabilities require a separate multiclass protocol. Duplicate exact verified
event-contracts are retained and excluded from repeated scoring.

`HISTORICAL_PERFORMANCE.csv` separates original recovered method, era proxy, sport,
competition, contract family, date and baseline kind. All subgroup comparisons are
exploratory. The pooled estimand is the observed mixture of historical methods, not
one fixed model. The primary paired mean and interval give each sporting event one
vote, including when several P-IDs refer to it. Date, competition and connected-team
block sensitivities report their own block counts; one-block intervals are unavailable.
Effective event n assumes independence across games; block counts show its limits.
Calibration gives each event equal weight within a bin. Log loss alone clips p at 1e-15.

The 100-event and 0.01 Brier gates were adopted after outcomes were observed. Even a
positive verdict is historical evidence, never prospectively preregistered certification.
The evidence reviews are human findings against retained captures; the software validates
their consistency and hashes, and does not itself authenticate a chat export or a result.
Original-method/cutoff/endpoint defects block Tier A or paired admission. A baseline
must be sports-only, market-blind, same-contract, and frozen or explicitly reconstructed
without future features, labels or outcome-informed tuning. Alternative lines cannot
enter the supplied-contract headline. Raw captures and reviewer findings remain required.

Coverage and exclusions: `COVERAGE.csv`, `HISTORICAL_CENSUS.csv`,
`HISTORICAL_QUALIFICATION.csv`. Request-level abstention frequency is unknown until a
complete request census is recovered. Historical training admissions are retained and
do not imply evidence qualification. Existing CARD-TRAIN-v1 approximate-time studies
remain separate; the strict-cutoff backtest command is a new retrospective model study
and cannot establish who generated an original forecast.

Track P: ONE-CHAT-v3 / v27.0 remains independent. Its registry, 400-game horizon,
benchmark, evidence threshold and sequential procedure are unchanged. Use
`python -m ml one-chat score --help` for its live-scoring arguments. No historical rows or counts
are imported into that track and no H/P statistical verdict is pooled.

Reproduce: `python -m ml historical-pre-event verify --run {BASE}`.
Add evidence through the append command, then generate a new immutable run directory.
`MANIFEST.csv` hashes every input and output except itself; verification regenerates
all tables and this report and checks the complete output inventory.
"""
    outputs["HISTORICAL_PROSPECTIVE_VALIDATION_REPORT.md"] = report.encode()
    # Detect source edits during generation, including recovered captures.
    for path, expected_hash in inputs.items():
        actual = input_digest(root, path)
        if actual != expected_hash:
            raise ValueError("input changed during historical assessment")
    return outputs, inputs, status


def run(out, root=ROOT):
    out = Path(out)
    if out.exists():
        raise FileExistsError(out)
    outputs, inputs, status = build(root)
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=out.parent) as temp:
        staging = Path(temp) / "run"
        staging.mkdir()
        for name, raw in outputs.items():
            (staging / name).write_bytes(raw)
        manifest = [
            dict(role="INPUT", path=p, sha256=h) for p, h in sorted(inputs.items())
        ]
        manifest += [
            dict(role="OUTPUT", path=p, sha256=digest(raw))
            for p, raw in sorted(outputs.items())
        ]
        (staging / "MANIFEST.csv").write_bytes(
            csv_bytes(manifest, ("role", "path", "sha256"))
        )
        staging.rename(out)
    return status


def verify(folder, root=ROOT):
    folder, root = Path(folder), Path(root)
    manifest = read_csv(folder / "MANIFEST.csv")
    if len({(r["role"], r["path"]) for r in manifest}) != len(manifest):
        raise ValueError("duplicate manifest entry")
    for r in manifest:
        if r["role"] not in {"INPUT", "OUTPUT"}:
            raise ValueError("unknown manifest role")
        actual = input_digest(root if r["role"] == "INPUT" else folder, r["path"])
        if actual != r["sha256"]:
            raise ValueError(f"manifest mismatch: {r['path']}")
    outputs, inputs, status = build(
        root, ledger_raw=(folder / "EVIDENCE_SNAPSHOT.csv").read_bytes()
    )
    expected = {(r["role"], r["path"]): r["sha256"] for r in manifest}
    rebuilt = {("INPUT", p): h for p, h in inputs.items()}
    rebuilt.update({("OUTPUT", p): digest(raw) for p, raw in outputs.items()})
    if expected != rebuilt or {p.name for p in folder.iterdir() if p.is_file()} - {
        "MANIFEST.csv",
        "REGISTRATION.md",
        "EVIDENCE_REVISIONS.csv",
        "README.md",
    } != set(outputs):
        raise ValueError("run output inventory differs from regeneration")
    if any((folder / p).read_bytes() != raw for p, raw in outputs.items()):
        raise ValueError("historical report does not rebuild byte for byte")
    return status


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    r = sub.add_parser("run")
    r.add_argument("--out", type=Path, required=True)
    v = sub.add_parser("verify")
    v.add_argument("--run", type=Path, required=True)
    a = sub.add_parser("append")
    a.add_argument("--row-id", required=True)
    a.add_argument(
        "--evidence",
        type=Path,
        required=True,
        help="JSON object in a UTF-8 .txt file; see README",
    )
    a.add_argument("--reviewer", required=True)
    a.add_argument("--reason", required=True)
    b = sub.add_parser(
        "backtest", help="separate strict-cutoff retrospective model study"
    )
    b.add_argument("--features", type=Path, required=True)
    b.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    if args.command == "run":
        print(run(args.out))
    elif args.command == "verify":
        print(verify(args.run))
    elif args.command == "backtest":
        from ml.historical_pre_event_backtest import run as backtest

        print(backtest(args.features, args.out))
    else:
        row = append_evidence(
            ROOT,
            ROOT / BASE / "EVIDENCE_REVISIONS.csv",
            args.row_id,
            json.loads(args.evidence.read_text(encoding="utf-8")),
            args.reviewer,
            args.reason,
        )
        print(f"appended {row['row_id']} revision {row['revision']}: {row['sha256']}")


if __name__ == "__main__":
    main()
