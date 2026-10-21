"""Browser-chat execution (CHAT-EXEC-v1): run the real forecast cycle inside a chat sandbox.

A web chat with a Python sandbox but no repository checkout cannot import ``ml``. This module packs the
committed runtime, runs the unchanged cycle from two small CSVs inside the sandbox, and brings the
verified attempt back into the repository with an honest freeze clock.

On a checkout (owner PC or a coding agent):
    python -m ml.chat pack --out DIR_OUTSIDE_THE_REPOSITORY
Inside the chat sandbox, from the root of the unzipped runtime:
    python -m ml.chat run --game GAME.csv --lines LINES.csv --capture SOURCE.txt --out OUT --confirm-no-outcome-seen
Back on a checkout, before the scheduled start whenever possible:
    python -m ml.chat accept --attempt UPLOAD.zip --local-key LOCAL-<MINI_KEY>-G0001
    python -m ml.chat accept --attempt research/cycle_attempts/<key>/<attempt> --local-key <key> --freeze-basis commit

The pack contains committed files only and is never written inside the repository. ``run`` writes the exact
cycle inputs, executes ``python -m ml.workflow`` and verifies the attempt; it never edits a probability.
``accept`` re-verifies the attempt and freezes its shadow rows with the actual clock, or with the committer
time of the pushed commit that first contained the unchanged attempt. Unsupported competitions, contract
families and team names are refused with the reason, so the card stays RESEARCH_ONLY_NO_MODEL.
"""
from __future__ import annotations

import argparse
import csv
import difflib
from datetime import datetime, timezone
import hashlib
import io
import math
from pathlib import Path, PurePosixPath
import re
import shutil
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
FORMAT = "CHAT-EXEC-v1"
STORE = "research/learning_store"
RELEASES = "research/cycle_releases"
CURRENT = RELEASES + "/CURRENT_RELEASES.csv"
FEEDBACK = "research/cycle_feedback"
CAPTURES = "research/chat_captures"
ATTEMPTS = "research/cycle_attempts"
LEDGER = "research/prospective/CYCLE_SHADOW_LEDGER.csv"
GAME_FIELDS = ("local_key", "competition", "native_event_id", "season", "scheduled_start", "home", "away", "venue", "source_url")
LINE_FIELDS = ("label", "family", "side", "line")
SIDES = {"winner": ("HOME", "AWAY", "DRAW"), "handicap": ("HOME", "AWAY"), "total": ("OVER", "UNDER")}
ACTIONS = {"winner": "THREE_WAY_DRAW_LOSES", "handicap": "STANDARD_COMPLETED", "total": "STANDARD_COMPLETED"}
CAPTURE_SUFFIXES = (".txt", ".csv", ".md")
# Mirrors ml.research_ingest; a test keeps them identical. Kept literal so a missing numerical
# dependency is still captured by ml.workflow's own failure receipt rather than an import error here.
TARGET_FIELDS = ("competition", "endpoint", "native_event_id", "season", "scheduled_start", "home", "away", "venue",
                 "source_url", "known_at", "capture_path", "capture_sha256", "collected_by")
EMPTY_EXPORTS = {
    "GAME_OBSERVATIONS.csv": ("competition", "endpoint", "native_event_id", "season", "event_at", "home", "away", "venue",
                              "status", "hs", "as_", "reg_hs", "reg_as", "decision", "final_at", "source_url",
                              "source_kind", "published_at", "retrieved_at", "known_at", "capture_path", "capture_sha256",
                              "review_status", "collected_by"),
    "TEAM_GAME_STATS.csv": ("competition", "native_event_id", "team", "stat", "value", "source_url", "source_kind",
                            "published_at", "retrieved_at", "known_at", "capture_path", "capture_sha256",
                            "review_status", "collected_by"),
    "AVAILABILITY.csv": ("competition", "native_event_id", "team", "player", "role", "status", "confirmation",
                         "published_at", "retrieved_at", "known_at", "source_url", "capture_path", "capture_sha256",
                         "review_status", "collected_by"),
}
CONTRACT_FIELDS = ("contract_key", "family", "side", "line", "endpoint", "definition", "action")
REQUEST_FIELDS = ("event_id", "competition", "endpoint", "home", "away", "venue", "scheduled_start", "issue_at",
                  "outcome_exposure", "candidate_recipe")
ACCEPT_FIELDS = ("local_key", "attempt_path", "execution_sha256", "status", "freeze_basis", "freeze_clock", "freeze_commit",
                 "evidence_status", "ledger_path", "ledger_rows", "accepted_at")
LOCAL_KEY = re.compile(r"LOCAL-[A-Za-z0-9-]+-G\d{4}")
LABEL = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.+-]{0,63}")
NATIVE_ID = re.compile(r"[A-Z][A-Z0-9_]*:[A-Za-z0-9._-]+")


class ChatError(ValueError):
    """An input or custody problem: retain the research and record the reason."""


def _rows(path) -> list[dict]:
    with Path(path).open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def _csv(rows, fields) -> bytes:
    text = io.StringIO(newline="")
    writer = csv.DictWriter(text, fieldnames=list(fields), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return text.getvalue().encode()


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _clock(text: str) -> datetime:
    try:
        value = datetime.fromisoformat(text.strip().replace("Z", "+00:00"))
    except ValueError as exc:
        raise ChatError(f"not an ISO time: {text!r}") from exc
    if value.tzinfo is None:
        raise ChatError(f"time needs an explicit UTC offset: {text!r}")
    return value.astimezone(timezone.utc)


def _git(root, *args) -> str:
    result = subprocess.run(["git", *args], cwd=root, capture_output=True)
    if result.returncode:
        raise ChatError("git " + " ".join(args) + " failed: " + result.stderr.decode(errors="replace").strip())
    return result.stdout.decode()


def _git_bytes(root, *args) -> bytes:
    result = subprocess.run(["git", *args], cwd=root, capture_output=True)
    if result.returncode:
        raise ChatError("git " + " ".join(args) + " failed: " + result.stderr.decode(errors="replace").strip())
    return result.stdout


def _one(rows, fields, name) -> dict:
    if len(rows) != 1:
        raise ChatError(f"{name} needs exactly one row")
    if set(rows[0]) != set(fields):
        raise ChatError(f"{name} columns must be exactly: {','.join(fields)}")
    row = {k: (v or "").strip() for k, v in rows[0].items()}
    if missing := [k for k in fields if not row[k]]:
        raise ChatError(f"{name} has empty fields: {','.join(missing)}")
    return row


def archive_code_digest(files: dict) -> str:
    """The release code digest (ml.cycle.code_hash) over archived bytes (``{posix path: bytes}``), so a pack can be
    checked without a checkout."""
    from ml import code_identity
    return code_identity.digest(files.get)


# ------------------------------------------------------------------ pack (checkout side)
def pack(out, ref="HEAD", root=ROOT) -> dict:
    root = Path(root).resolve()
    out = Path(out).resolve()
    if out == root or root in out.parents:
        raise ChatError("write the pack outside the repository: the zip is a binary and is never committed")
    commit = _git(root, "rev-parse", "--verify", ref + "^{commit}").strip()
    observed = _git_bytes(root, "show", f"{commit}:{STORE}/SOURCE_OBSERVATIONS.csv").decode("utf-8-sig")
    captures = sorted({r["capture_path"] for r in csv.DictReader(io.StringIO(observed)) if r["capture_path"]})
    paths = ["ml", STORE, RELEASES]
    if subprocess.run(["git", "cat-file", "-e", f"{commit}:{FEEDBACK}"], cwd=root, capture_output=True).returncode == 0:
        paths.append(FEEDBACK)
    for path in captures:
        if PurePosixPath(path).is_absolute() or ".." in PurePosixPath(path).parts:
            raise ChatError(f"store capture is not repository-relative: {path}")
        if not any(path == p or path.startswith(p + "/") for p in paths):
            paths.append(path)
    # Exact committed bytes: no clone-specific line-ending conversion, because captures and releases are hashed.
    raw = _git_bytes(root, "-c", "core.autocrlf=false", "-c", "core.eol=lf", "archive", "--format=zip", commit, "--", *paths)
    with zipfile.ZipFile(io.BytesIO(raw)) as zf:
        files = {i.filename: zf.read(i) for i in zf.infolist() if not i.is_dir()}
    if missing := [c for c in captures if c not in files]:
        raise ChatError("store captures absent from the commit: " + ", ".join(missing[:5]))
    code = archive_code_digest(files)
    current = list(csv.DictReader(io.StringIO(files[CURRENT].decode("utf-8-sig"))))
    stale = []
    for row in current:
        release = files.get(row["release_path"])
        if release is None or _sha(release) != row["release_sha256"]:
            raise ChatError(f"active release file missing or changed: {row['release_path']}")
        frozen = next(csv.DictReader(io.StringIO(release.decode("utf-8-sig"))))["code_sha256"]
        if frozen != code:
            stale.append(row["active_experimental_release"])
    if stale:
        raise ChatError("active releases were frozen for different code (" + ", ".join(stale) +
                        "); freeze new release versions before packing")
    out.mkdir(parents=True, exist_ok=True)
    target = out / f"SR_RUNTIME_{commit[:12]}.zip"
    if target.exists():
        raise ChatError(f"{target} already exists")
    receipt = dict(format=FORMAT, ref=ref, commit=commit, created_at=_now().isoformat(), code_sha256=code,
                   releases=";".join(r["competition"] + "=" + r["active_experimental_release"] for r in current),
                   files=len(files), archive_sha256=_sha(raw))
    with zipfile.ZipFile(io.BytesIO(raw)) as source, zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as zf:
        for info in source.infolist():
            zf.writestr(info, source.read(info))
        zf.writestr("CHAT_PACK_RECEIPT.csv", _csv([receipt], receipt))
    dirty = _git(root, "status", "--porcelain", "--", *paths).strip()
    return dict(receipt, path=str(target), bytes=target.stat().st_size,
                uncommitted_not_packed=dirty.replace("\n", "; ") if dirty else "NONE")


# ------------------------------------------------------------------ run (sandbox side)
def _release(root: Path, competition: str) -> dict:
    current = _rows(root / CURRENT)
    match = [r for r in current if r["competition"] == competition]
    if not match:
        supported = ", ".join(sorted(r["competition"] for r in current))
        raise ChatError(f"no active model release for {competition!r}; supported now: {supported}. "
                        "Keep this card RESEARCH_ONLY_NO_MODEL (NOT_RUN_DATA_UNAVAILABLE).")
    row = match[0]
    if _sha((root / row["release_path"]).read_bytes()) != row["release_sha256"]:
        raise ChatError("release file differs from CURRENT_RELEASES.csv; repack from a clean commit")
    return row


def _teams(root: Path, competition: str) -> set:
    names = set()
    for row in _rows(root / STORE / "EVENTS.csv"):
        if row["competition"] == competition:
            names.update((row["home"], row["away"]))
    return names


def _team_check(name: str, names: set, side: str):
    if name in names:
        return
    near = difflib.get_close_matches(name, sorted(names), n=5, cutoff=0.3)
    listing = ", ".join(sorted(names)) if len(names) <= 60 else ", ".join(sorted(names)[:60]) + ", ..."
    raise ChatError(f"{side} team {name!r} is not a stored participant; use the store's exact name"
                    + (f" (closest: {', '.join(near)})" if near else "") + f". Stored names: {listing}")


def _contracts(rows, endpoint) -> list[dict]:
    if not rows:
        raise ChatError("LINES.csv needs at least one supported contract")
    if set(rows[0]) != set(LINE_FIELDS):
        raise ChatError("LINES.csv columns must be exactly: " + ",".join(LINE_FIELDS))
    out, labels = [], set()
    for raw in rows:
        row = {k: (v or "").strip() for k, v in raw.items()}
        label, family, side, line = row["label"], row["family"].lower(), row["side"].upper(), row["line"]
        if not LABEL.fullmatch(label) or label in labels:
            raise ChatError(f"label {label!r} must be unique and use letters, digits, _ . + - only")
        labels.add(label)
        if family not in SIDES:
            raise ChatError(f"{label}: family {row['family']!r} is not priced by the model (full-game winner, handicap "
                            "or total only; periods, halves, corners and props stay research-only). Remove the line.")
        if side not in SIDES[family]:
            raise ChatError(f"{label}: side for {family} must be one of {'/'.join(SIDES[family])}")
        if family == "winner":
            if line:
                raise ChatError(f"{label}: winner contracts take an empty line")
        else:
            try:
                value = float(line)
            except ValueError as exc:
                raise ChatError(f"{label}: {family} needs a numeric line") from exc
            if not math.isfinite(value) or (family == "total" and value <= 0):
                raise ChatError(f"{label}: invalid {family} line {line!r}")
        out.append(dict(contract_key=label, family=family, side=side, line=line, endpoint=endpoint,
                        definition="FROZEN_FRAMEWORK_CONVENTION", action=ACTIONS[family]))
    return out


def run(game, lines, capture, out, *, confirmed=False, root=None) -> dict:
    if not confirmed:
        raise ChatError("pass --confirm-no-outcome-seen only if no live score, result or post-start report of this game was opened")
    root = Path(root or Path.cwd()).resolve()
    if Path.cwd().resolve() != root or not (root / "ml" / "workflow.py").exists() or not (root / CURRENT).exists():
        raise ChatError("run from the root of the unzipped runtime (the folder that contains ml/ and research/)")
    out = Path(out).resolve()
    if out.exists():
        raise ChatError(f"{out} exists; every run uses a new output folder")
    g = _one(_rows(game), GAME_FIELDS, "GAME.csv")
    if not LOCAL_KEY.fullmatch(g["local_key"]):
        raise ChatError("local_key must be the card's stable key, e.g. LOCAL-<MINI_KEY>-G0001")
    if not NATIVE_ID.fullmatch(g["native_event_id"]) or re.fullmatch(r"P-\d+", g["native_event_id"]):
        raise ChatError("native_event_id must be PROVIDER:ID, e.g. NHL:2026020119 (never a P-ID)")
    start = _clock(g["scheduled_start"])
    release = _release(root, g["competition"])
    names = _teams(root, g["competition"])
    _team_check(g["home"], names, "home")
    _team_check(g["away"], names, "away")
    if g["home"] == g["away"]:
        raise ChatError("home and away must differ")
    contracts = _contracts(_rows(lines), release["endpoint"])
    source = Path(capture)
    if not source.is_file() or source.suffix.lower() not in CAPTURE_SUFFIXES or source.stat().st_size == 0:
        raise ChatError("capture must be a non-empty .txt/.csv/.md copy of the opened fixture source")
    data = source.read_bytes()
    rel = f"{CAPTURES}/{g['local_key']}/{source.name}"
    stored = root / rel
    if stored.exists() and _sha(stored.read_bytes()) != _sha(data):
        raise ChatError(f"{rel} already holds a different capture; rename the new capture file")
    stored.parent.mkdir(parents=True, exist_ok=True)
    stored.write_bytes(data)
    now = _now()
    inputs = out / "INPUTS"
    (inputs / "EXPORT").mkdir(parents=True)
    target = dict(competition=g["competition"], endpoint=release["endpoint"], native_event_id=g["native_event_id"],
                  season=g["season"], scheduled_start=start.isoformat(), home=g["home"], away=g["away"], venue=g["venue"],
                  source_url=g["source_url"], known_at=now.isoformat(), capture_path=rel, capture_sha256=_sha(data),
                  collected_by=g["local_key"])
    (inputs / "EXPORT" / "TARGET_EVENT.csv").write_bytes(_csv([target], TARGET_FIELDS))
    for name, fields in EMPTY_EXPORTS.items():
        (inputs / "EXPORT" / name).write_bytes(_csv([], fields))
    (inputs / "CONTRACTS.csv").write_bytes(_csv(contracts, CONTRACT_FIELDS))
    request = dict(event_id=g["native_event_id"], competition=g["competition"], endpoint=release["endpoint"],
                   home=g["home"], away=g["away"], venue=g["venue"], scheduled_start=start.isoformat(),
                   issue_at=_now().isoformat(), outcome_exposure="NONE_RECORDED", candidate_recipe=FORMAT + "_SUPPLIED_CONTRACTS")
    (inputs / "REQUEST.csv").write_bytes(_csv([request], REQUEST_FIELDS))
    from ml import workflow
    attempt = out / ("ATTEMPT_" + _now().strftime("%Y%m%dT%H%M%S%fZ"))
    feedback = root / FEEDBACK if (root / FEEDBACK).is_dir() else None
    rec = workflow.execute(inputs / "EXPORT", root / STORE, inputs / "REQUEST.csv", inputs / "CONTRACTS.csv",
                           root / release["release_path"], attempt, feedback_root=feedback, ledger=None)
    execution_sha = _sha((attempt / "EXECUTION.csv").read_bytes())
    results = []
    if rec["status"] == "EXECUTED":
        workflow.verify(attempt)
        receipt = _rows(attempt / "BUNDLE" / "RECEIPT.csv")[0]
        timing = "PRE_START" if _clock(receipt["generated_at"]) < start else "POST_START"
        for row in _rows(attempt / "BUNDLE" / "PREDICTIONS.csv"):
            results.append(dict(local_key=g["local_key"], label=row["contract_key"], family=row["family"], side=row["side"],
                                line=row["line"], p_card=row["p_card"], baseline_p=row["baseline_p"], model_rank=row["rank"],
                                status="EXECUTED", timing_at_generation=timing, generated_at=receipt["generated_at"],
                                release=receipt["version"], weights=receipt["weights"], training_rows=receipt["training_rows"],
                                execution_sha256=execution_sha, error=""))
    else:
        results.append(dict(local_key=g["local_key"], label="", family="", side="", line="", p_card="NOT_ESTIMATED",
                            baseline_p="NOT_ESTIMATED", model_rank="", status="FAILED", timing_at_generation="",
                            generated_at="", release=release["active_experimental_release"], weights="", training_rows="",
                            execution_sha256=execution_sha, error=rec["error_type"] + ": " + rec["error"]))
    (out / "RESULT.csv").write_bytes(_csv(results, results[0]))
    upload = out / f"UPLOAD_{g['local_key']}_{attempt.name}.zip"
    prefix = f"{ATTEMPTS}/{g['local_key']}/{attempt.name}"
    with zipfile.ZipFile(upload, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(attempt.rglob("*")):
            if path.is_file():
                zf.write(path, prefix + "/" + path.relative_to(attempt).as_posix())
        zf.write(out / "RESULT.csv", prefix + "_RESULT.csv")
        zf.write(stored, rel)
    return dict(status=rec["status"], attempt=str(attempt), upload=str(upload), results=results)


# ------------------------------------------------------------------ accept (checkout side)
def _safe_extract(zf: zipfile.ZipFile, root: Path, local_key: str) -> Path:
    allowed = (f"{ATTEMPTS}/{local_key}/", f"{CAPTURES}/{local_key}/")
    attempts = set()
    for info in zf.infolist():
        name = info.filename
        parts = PurePosixPath(name).parts
        if info.is_dir():
            continue
        if PurePosixPath(name).is_absolute() or ".." in parts or not name.startswith(allowed):
            raise ChatError(f"upload member outside {ATTEMPTS}/{local_key} or {CAPTURES}/{local_key}: {name}")
        if Path(name).suffix.lower() not in (".csv", ".txt", ".md"):
            raise ChatError(f"upload member type not allowed in the repository: {name}")
        if name.startswith(allowed[0]) and len(parts) >= 5:
            attempts.add("/".join(parts[:4]))
    if len(attempts) != 1:
        raise ChatError("upload must contain exactly one attempt folder")
    for info in zf.infolist():
        if info.is_dir():
            continue
        data = zf.read(info)
        dest = root / info.filename
        if dest.exists() and _sha(dest.read_bytes()) != _sha(data):
            raise ChatError(f"refusing to overwrite a different existing file: {info.filename}")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
    return root / attempts.pop()


def _commit_clock(root: Path, attempt: Path) -> tuple[datetime, str]:
    rel = attempt.relative_to(root).as_posix()
    if _git(root, "status", "--porcelain", "--", rel).strip() or not _git(root, "ls-files", "--", rel + "/EXECUTION.csv").strip():
        raise ChatError("--freeze-basis commit needs the attempt committed unchanged; otherwise use --freeze-basis now")
    log = _git(root, "log", "--diff-filter=A", "--format=%H %cI", "--", rel + "/EXECUTION.csv").strip().splitlines()
    if not log:
        raise ChatError("no commit added this attempt")
    commit, stamp = log[-1].split()
    if subprocess.run(["git", "merge-base", "--is-ancestor", commit, "origin/main"], cwd=root, capture_output=True).returncode:
        raise ChatError("the adding commit is not on origin/main; push (or fetch) before using its time")
    return _clock(stamp), commit


def accept(attempt, local_key, *, freeze_basis="now", ledger=LEDGER, root=ROOT) -> dict:
    root = Path(root).resolve()
    if not LOCAL_KEY.fullmatch(local_key):
        raise ChatError("local_key must be the card's stable key, e.g. LOCAL-<MINI_KEY>-G0001")
    source = Path(attempt)
    if source.suffix.lower() == ".zip":
        if freeze_basis == "commit":
            raise ChatError("--freeze-basis commit applies to an attempt already committed in the repository")
        with zipfile.ZipFile(source) as zf:
            folder = _safe_extract(zf, root, local_key)
    else:
        folder = source.resolve()
        if not folder.is_relative_to((root / ATTEMPTS / local_key).resolve()):
            raise ChatError(f"attempt folder must be under {ATTEMPTS}/{local_key}/")
    receipt = folder.parent / (folder.name + "_ACCEPTANCE.csv")
    if receipt.exists():
        raise ChatError(f"{receipt.name} exists; this attempt was already accepted")
    from ml import cycle, workflow
    from ml.evaluation import prospective
    rec = workflow.verify(folder)
    target = _rows(folder / "EXPORT" / "TARGET_EVENT.csv")
    for row in target:
        capture = root / row["capture_path"]
        if not capture.is_file() or _sha(capture.read_bytes()) != row["capture_sha256"]:
            raise ChatError(f"target capture missing or changed: {row['capture_path']}")
    if any(row["collected_by"] != local_key for row in target):
        raise ChatError("attempt was collected for a different local key")
    out = dict(local_key=local_key, attempt_path=folder.relative_to(root).as_posix(),
               execution_sha256=_sha((folder / "EXECUTION.csv").read_bytes()), status=rec["status"],
               freeze_basis=freeze_basis, freeze_clock="", freeze_commit="", evidence_status="", ledger_path="",
               ledger_rows="0", accepted_at=_now().isoformat())
    if rec["status"] == "EXECUTED":
        if freeze_basis == "commit":
            clock, commit = _commit_clock(root, folder)
        elif freeze_basis == "now":
            clock, commit = _now(), ""
        else:
            raise ChatError("freeze basis must be now or commit")
        rows = cycle.shadow_rows(folder / "BUNDLE", now_at=clock.isoformat())
        prospective.freeze(root / ledger, rows, now=clock.isoformat())
        out.update(freeze_clock=clock.isoformat(), freeze_commit=commit, evidence_status=rows[0]["evidence_status"],
                   ledger_path=Path(ledger).as_posix(), ledger_rows=str(len(rows)))
    receipt.write_bytes(_csv([out], ACCEPT_FIELDS))
    out["manifest_row"] = dict(card_id=local_key, event_id=rec["event_id"], competition=rec["competition"],
                               endpoint=rec["endpoint"], execution_path=out["attempt_path"],
                               execution_sha256=out["execution_sha256"],
                               feedback_status="PENDING_EVENT" if rec["status"] == "EXECUTED" else "NOT_APPLICABLE_NO_MODEL")
    return out


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    pk = sub.add_parser("pack", help="zip the committed runtime for a chat sandbox (outside the repository)")
    pk.add_argument("--out", type=Path, required=True)
    pk.add_argument("--ref", default="HEAD")
    rn = sub.add_parser("run", help="inside the unzipped runtime: build inputs, execute and verify one game")
    for name in ("game", "lines", "capture", "out"):
        rn.add_argument("--" + name, type=Path, required=True)
    rn.add_argument("--confirm-no-outcome-seen", action="store_true")
    ac = sub.add_parser("accept", help="verify a returned attempt and freeze its shadow rows")
    ac.add_argument("--attempt", type=Path, required=True)
    ac.add_argument("--local-key", required=True)
    ac.add_argument("--freeze-basis", choices=("now", "commit"), default="now")
    ac.add_argument("--ledger", default=LEDGER)
    args = parser.parse_args(argv)
    try:
        if args.command == "pack":
            result = pack(args.out, args.ref)
            for key in ("path", "commit", "code_sha256", "releases", "files", "bytes", "uncommitted_not_packed"):
                print(f"{key}: {result[key]}")
        elif args.command == "run":
            result = run(args.game, args.lines, args.capture, args.out, confirmed=args.confirm_no_outcome_seen)
            print(f"status: {result['status']}  attempt: {result['attempt']}")
            for row in result["results"]:
                print(f"  {row['label'] or '-'}: p_card={row['p_card']} baseline_p={row['baseline_p']} rank={row['model_rank']} "
                      f"{row['timing_at_generation']} {row['error']}")
            print(f"upload: {result['upload']}")
            if result["status"] != "EXECUTED":
                raise SystemExit(1)
        else:
            result = accept(args.attempt, args.local_key, freeze_basis=args.freeze_basis, ledger=args.ledger)
            for key in ACCEPT_FIELDS:
                print(f"{key}: {result[key]}")
            print("manifest_row: " + ",".join(result["manifest_row"].values()))
    except ChatError as exc:
        print(f"REFUSED: {exc}")
        raise SystemExit(2)


if __name__ == "__main__":
    main()
