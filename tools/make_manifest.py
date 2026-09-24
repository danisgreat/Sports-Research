#!/usr/bin/env python3
"""Generate a new control manifest (added 2026-09-25(c); replaces ad-hoc scratch scripts).

Usage:
    python tools/make_manifest.py --out CONTROL_MANIFEST_2026-09-25-3.md \
        --title "post-hygiene/CI pass" --note "What changed, in one or two sentences." \
        [--from CONTROL_MANIFEST_2026-09-25-2.md] [--add path ...] [--drop path ...]

The file list is copied from --from (default: the manifest METHOD.md currently names), plus --add,
minus --drop. Hashes are taken in CRLF form (tools/manifest_lib.py). The new manifest records
which files changed, which are new, and which were dropped relative to --from. It never lists
itself. After generating it:
- repoint METHOD.md's header;
- repoint the active mini log's "Freeze with every card" row, with the printed SHA;
- run tools/verify_manifest.py.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import sys
from pathlib import Path
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).resolve().parent))
from manifest_lib import current_manifest, file_digest, read_rows  # noqa: E402

REPO = Path(__file__).resolve().parent.parent


def build(prev: Path, out_name: str, title: str, note: str, add=(), drop=(), repo: Path = REPO,
          now: dt.datetime | None = None) -> tuple[str, dict]:
    prev_rows = {rel: sha for rel, sha, _ in read_rows(prev)}
    files = [rel for rel in prev_rows if rel not in set(drop)]
    for rel in add:
        if rel not in files:
            files.append(rel)
    files = [f for f in files if f != out_name]
    rows, changed, new, same = [], [], [], []
    for rel in files:
        p = repo / rel
        if not p.exists():
            raise SystemExit(f"error: listed file does not exist: {rel}")
        sha, size = file_digest(p, "crlf")
        rows.append(f"| `{rel}` | `{sha}` | {size} |")
        if rel not in prev_rows:
            new.append(rel)
        elif prev_rows[rel] != sha:
            changed.append(rel)
        else:
            same.append(rel)
    dropped = [rel for rel in prev_rows if rel not in files]
    now = now or dt.datetime.now(dt.timezone.utc)
    stamp = now.astimezone(ZoneInfo("Australia/Brisbane")).strftime("%Y-%m-%d %H:%M AEST")
    fmt = lambda xs: ", ".join(f"`{x}`" for x in xs) or "none"  # noqa: E731
    body = (
        f"# Control manifest — {out_name[len('CONTROL_MANIFEST_'):-3]} ({title})\n\n"
        f"Method: **MDS-2026.09.19-v4.3**\n"
        f"Control revision: **CR-2026.09.21-3** (label unchanged; content receipt under the same label)\n"
        f"Status: **CURRENT post-write content receipt**, generated {stamp} by `tools/make_manifest.py` "
        f"from `{prev.name}`.\n\n"
        f"**Purpose.** This is the byte-level SHA-256 receipt that every new card freezes (`METHOD.md` header; PF-7). {note}\n\n"
        "**It does not change any forecasting coefficient, probability cap or ranking override.**\n\n"
        "This manifest is excluded from its own hash table. The living logs (`PREDICTION_LOG_COMBINED_5.md`, "
        "`GAME_LOG_STATUS_CURRENT.md`) are a write-time snapshot and change with every card. Hashes are taken "
        "in CRLF form (`tools/manifest_lib.py`); verify with `python tools/verify_manifest.py`.\n\n"
        f"**Changed since {prev.name} (by bytes):** {fmt(changed)}.\n\n"
        f"**New in the receipt:** {fmt(new)}.\n\n"
        f"**Dropped:** {fmt(dropped)}.\n\n"
        f"**Unchanged:** {len(same)} files.\n\n"
        "## SHA-256 file receipt\n\n| File | SHA-256 | Bytes |\n|---|---|---:|\n" + "\n".join(rows) + "\n"
    )
    return "﻿" + body, {"changed": changed, "new": new, "dropped": dropped, "same": same, "files": files}


def main(argv=None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--note", required=True)
    ap.add_argument("--from", dest="prev")
    ap.add_argument("--add", nargs="*", default=[])
    ap.add_argument("--drop", nargs="*", default=[])
    args = ap.parse_args(argv)
    prev = REPO / args.prev if args.prev else current_manifest(REPO)
    out = REPO / args.out
    if out.exists():
        print(f"error: {args.out} already exists; choose a new name", file=sys.stderr)
        return 2
    text, info = build(prev, args.out, args.title, args.note, args.add, args.drop)
    out.write_bytes(text.encode("utf-8").replace(b"\r\n", b"\n").replace(b"\n", b"\r\n"))
    sha = hashlib.sha256(out.read_bytes()).hexdigest()
    print(f"wrote {args.out}: {len(info['files'])} files; changed {len(info['changed'])}, new {len(info['new'])}, "
          f"dropped {len(info['dropped'])}; SHA-256 {sha}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
