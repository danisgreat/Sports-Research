"""Shared helpers for control-manifest generation and verification (added 2026-09-25(c)).

A control manifest (CONTROL_MANIFEST_*.md) is a byte-level SHA-256 receipt of the governance files
that every new card freezes (METHOD.md header; PF-7). Hashes are taken in the CRLF form, which is
what a checkout produces under .gitattributes `eol=crlf` / core.autocrlf=true. That makes a
manifest reproducible on any platform.
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

ROW_RE = re.compile(r"^\| `([^`]+)` \| `([0-9a-f]{64})` \| (\d+) \|")
CURRENT_RE = re.compile(r"Freeze the SHA-256 file receipt from \[(CONTROL_MANIFEST_[^\]]+\.md)\]")
# Living logs change with every card; a manifest snapshots them but they are not expected to match later.
LIVING_RE = re.compile(r"^(PREDICTION_LOG_COMBINED(_\d+)?\.md|GAME_LOG_STATUS_CURRENT\.md)$")


def crlf_bytes(data: bytes) -> bytes:
    """Return the CRLF checkout form of a text file; binary data (NUL byte) is returned unchanged."""
    if b"\x00" in data:
        return data
    return data.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")


def file_digest(path: Path, eol: str = "crlf") -> tuple[str, int]:
    data = path.read_bytes()
    if eol == "crlf":
        data = crlf_bytes(data)
    return hashlib.sha256(data).hexdigest(), len(data)


def read_rows(manifest: Path) -> list[tuple[str, str, int]]:
    rows = []
    for line in manifest.read_text(encoding="utf-8-sig").splitlines():
        m = ROW_RE.match(line)
        if m:
            rows.append((m.group(1), m.group(2), int(m.group(3))))
    return rows


def current_manifest(repo: Path) -> Path:
    """The manifest named in METHOD.md's header ("Freeze the SHA-256 file receipt from [...]")."""
    text = (repo / "METHOD.md").read_text(encoding="utf-8-sig")
    m = CURRENT_RE.search(text)
    if not m:
        raise SystemExit("METHOD.md does not name a current control manifest")
    return repo / m.group(1)


def is_living(rel: str) -> bool:
    return bool(LIVING_RE.match(rel.split("/")[-1])) and "/" not in rel
