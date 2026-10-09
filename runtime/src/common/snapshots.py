"""Hashed raw snapshots in the documented layout `runtime/data/raw/<sport>/<provider>/<YYYY-MM-DD>/` (SRC-06).

DATA_SOURCE_REGISTER.md requires every external response to be stored verbatim with its SHA-256, retrieval time, endpoint and source
version. This module is that writer. A snapshot is two files: `<stamp>_<sha12>.body` (the bytes as received) and `<stamp>_<sha12>.json`
(the receipt). Existing snapshots are never overwritten, and `verify` re-hashes the body. The R bridges (`runtime/r_ingestion/*.R`) are
run by hand and their Parquet output is registered with `python -B -m runtime.src.common.snapshots register FILE ...`.
"""

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

DEFAULT_ROOT = Path(__file__).resolve().parents[2] / "data"
_SAFE = re.compile(r"^[a-z0-9][a-z0-9_\-]*$")


class SnapshotError(ValueError):
    """A snapshot could not be written or no longer matches its receipt."""


def _check(label: str, value: str) -> str:
    if not _SAFE.match(value):
        raise SnapshotError(f"{label} {value!r} must be lowercase letters, digits, '_' or '-'")
    return value


def write_snapshot(sport: str, provider: str, body: bytes, endpoint: str, source_version: str = "unversioned",
                   retrieved_utc: Optional[str] = None, root: Optional[Path] = None) -> Dict[str, Any]:
    """Store `body` verbatim and return its receipt (with the paths relative to `root`)."""
    if not body:
        raise SnapshotError("an empty response is not a snapshot")
    when = retrieved_utc or datetime.now(timezone.utc).isoformat()
    moment = datetime.fromisoformat(when.replace("Z", "+00:00"))
    if moment.tzinfo is None or moment.utcoffset() is None:
        raise SnapshotError("retrieved_utc needs a UTC offset")
    moment = moment.astimezone(timezone.utc)
    digest = hashlib.sha256(body).hexdigest()
    folder = Path(root or DEFAULT_ROOT) / "raw" / _check("sport", sport) / _check("provider", provider) / moment.strftime("%Y-%m-%d")
    folder.mkdir(parents=True, exist_ok=True)
    stem = f"{moment.strftime('%Y%m%dT%H%M%S%fZ')}_{digest[:12]}"
    receipt: Dict[str, Any] = {"sport": sport, "provider": provider, "endpoint": endpoint, "source_version": source_version, "retrieved_utc": moment.isoformat(),
               "sha256": digest, "bytes": len(body), "body": f"{stem}.body"}
    for name, payload in ((f"{stem}.body", body), (f"{stem}.json", (json.dumps(receipt, indent=1, sort_keys=True) + "\n").encode("utf-8"))):
        try:
            with (folder / name).open("xb") as handle:
                handle.write(payload)
        except FileExistsError as exc:
            raise SnapshotError(f"{folder / name} already exists; snapshots are immutable") from exc
    return {**receipt, "path": str((folder / f"{stem}.body").relative_to(Path(root or DEFAULT_ROOT)).as_posix())}


def verify(receipt_path: Path) -> Dict[str, str]:
    """Re-hash the body named by a receipt; raises if it is missing or changed."""
    receipt_path = Path(receipt_path)
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    body = receipt_path.with_name(receipt["body"])
    if not body.exists():
        raise SnapshotError(f"{body} is missing")
    raw = body.read_bytes()
    if len(raw) != receipt["bytes"] or hashlib.sha256(raw).hexdigest() != receipt["sha256"]:
        raise SnapshotError(f"{body} no longer matches its receipt")
    return receipt


def list_snapshots(sport: Optional[str] = None, provider: Optional[str] = None, root: Optional[Path] = None) -> List[Path]:
    base = Path(root or DEFAULT_ROOT) / "raw"
    pattern = f"{sport or '*'}/{provider or '*'}/*/*.json"
    return sorted(base.glob(pattern))


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    r = sub.add_parser("register", help="store a file (for example an R bridge's Parquet output) as a hashed snapshot")
    r.add_argument("file", type=Path)
    r.add_argument("--sport", required=True)
    r.add_argument("--provider", required=True)
    r.add_argument("--endpoint", required=True)
    r.add_argument("--source-version", default="unversioned")
    r.add_argument("--root", type=Path)
    v = sub.add_parser("verify", help="re-hash every snapshot under the root")
    v.add_argument("--root", type=Path)
    args = parser.parse_args(argv)
    if args.command == "register":
        print(json.dumps(write_snapshot(args.sport, args.provider, args.file.read_bytes(), args.endpoint, args.source_version, root=args.root), indent=1))
        return 0
    failures = []
    for path in list_snapshots(root=args.root):
        try:
            verify(path)
        except SnapshotError as exc:
            failures.append(str(exc))
    print(json.dumps({"passed": not failures, "failures": failures}, indent=1))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
