"""Hash-checked file relocations (RELOC-v1, CR-2026.11.12-R1).

When the owner moves retained originals out of a working folder (12 November 2026: every file under
``research/active_minis/`` moved to ``archive/retired_active_minis_2026-11-12/``), the historical records that cite
the old path are not rewritten. Instead each move is listed in an ``archive/*/RELOCATIONS.csv`` table
(old_path, new_path, sha256), and readers resolve a cited path through it. A relocation is honoured only when the
file at the new path has exactly the recorded SHA-256, so a moved file cannot silently change.

    resolve(root, "research/active_minis/X.md")  -> the existing path, or the hash-verified relocated path, or None
"""
from __future__ import annotations

import csv
import hashlib
from functools import lru_cache
from pathlib import Path

FIELDS = ("old_path", "new_path", "sha256")


class RelocationError(ValueError):
    pass


@lru_cache(maxsize=None)
def table(root: str) -> dict[str, tuple[str, str]]:
    out: dict[str, tuple[str, str]] = {}
    for path in sorted(Path(root).glob("archive/*/RELOCATIONS.csv")):
        with open(path, newline="", encoding="utf-8") as fh:
            reader = csv.DictReader(fh)
            if tuple(reader.fieldnames or ()) != FIELDS:
                raise RelocationError(f"{path}: columns must be exactly {','.join(FIELDS)}")
            for r in reader:
                if r["old_path"] in out and out[r["old_path"]] != (r["new_path"], r["sha256"]):
                    raise RelocationError(f"{path}: {r['old_path']} is relocated twice to different targets")
                out[r["old_path"]] = (r["new_path"], r["sha256"])
    return out


def resolve(root, rel: str) -> Path | None:
    """The file a historical record cites: at its own path if present, else at its hash-verified relocated path."""
    root = Path(root)
    direct = root / rel
    if direct.is_file():
        return direct
    hit = table(str(root.resolve())).get(rel)
    if not hit:
        return None
    moved = root / hit[0]
    if not moved.is_file() or hashlib.sha256(moved.read_bytes()).hexdigest() != hit[1]:
        raise RelocationError(f"{rel}: relocated file {hit[0]} is missing or does not match its recorded SHA-256")
    return moved
