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

A manifest that changes a forecasting coefficient, cap or ranking rule must say so with
--model-change "..." (added 2026-09-25(e), when RM-1 made the default no-change line false).

C-RULE-FREEZE (added 2026-09-26). Every manifest names its --category: INTEGRITY, MEASUREMENT,
DOCUMENTATION, VALIDITY_REPAIR or MODEL_CHANGE. MODEL_CHANGE requires --model-change and, while
tools/evidence_status.py reports the freeze IN FORCE, --freeze-override "<the user's instruction>".
A second manifest on the same date (by the --out name) is refused unless it is a VALIDITY_REPAIR.
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


NO_MODEL_CHANGE = "**It does not change any forecasting coefficient, probability cap or ranking override.**"
CATEGORIES = ("INTEGRITY", "MEASUREMENT", "DOCUMENTATION", "VALIDITY_REPAIR", "MODEL_CHANGE")


def freeze_in_force(repo: Path = REPO) -> bool:
    """C-RULE-FREEZE state from tools/evidence_status.py (in force until both evidence gates report)."""
    import evidence_status as es  # local import: keeps build() usable without the evidence tools
    rows = es.collect(repo, [])
    return not next(r for r in rows if r["gate"] == "C-RULE-FREEZE")["done"]


def category_errors(category: str | None, model_change: str | None, freeze_override: str | None,
                    in_force: bool, same_day: int) -> list[str]:
    errs = []
    if category not in CATEGORIES:
        errs.append(f"--category must be one of {', '.join(CATEGORIES)}")
    if category == "MODEL_CHANGE" and not model_change:
        errs.append("MODEL_CHANGE needs --model-change stating the coefficient, cap or ranking rule changed")
    if model_change and category != "MODEL_CHANGE":
        errs.append("--model-change is only valid with --category MODEL_CHANGE")
    if category == "MODEL_CHANGE" and in_force and not freeze_override:
        errs.append("C-RULE-FREEZE is in force: a MODEL_CHANGE needs --freeze-override quoting the user's instruction")
    if same_day and category != "VALIDITY_REPAIR":
        errs.append(f"{same_day} manifest(s) already exist for this date: one per issuing day unless VALIDITY_REPAIR")
    return errs


def build(prev: Path, out_name: str, title: str, note: str, add=(), drop=(), repo: Path = REPO,
          now: dt.datetime | None = None, model_change: str | None = None, category: str | None = None,
          freeze_override: str | None = None) -> tuple[str, dict]:
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
        + (f"**Model change:** {model_change}" if model_change else NO_MODEL_CHANGE) + "\n\n"
        + (f"**Category (C-RULE-FREEZE):** {category}.\n\n" if category else "")
        + (f"**Freeze override (user instruction):** {freeze_override}\n\n" if freeze_override else "")
        + "This manifest is excluded from its own hash table. The living logs (`PREDICTION_LOG_COMBINED_5.md`, "
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
    ap.add_argument("--model-change", default=None,
                    help="state a change to a forecasting coefficient, cap or ranking rule (replaces the no-change line)")
    ap.add_argument("--category", required=True, choices=CATEGORIES)
    ap.add_argument("--freeze-override", default=None, help="the user's instruction authorising a MODEL_CHANGE")
    args = ap.parse_args(argv)
    import re as _re
    date = _re.search(r"CONTROL_MANIFEST_(\d{4}-\d{2}-\d{2})", args.out)
    same_day = len(list(REPO.glob(f"CONTROL_MANIFEST_{date.group(1)}*.md"))) if date else 0
    errs = category_errors(args.category, args.model_change, args.freeze_override,
                           freeze_in_force(REPO) if args.category == "MODEL_CHANGE" else False, same_day)
    if errs:
        for e in errs:
            print("error: " + e, file=sys.stderr)
        return 2
    prev = REPO / args.prev if args.prev else current_manifest(REPO)
    out = REPO / args.out
    if out.exists():
        print(f"error: {args.out} already exists; choose a new name", file=sys.stderr)
        return 2
    text, info = build(prev, args.out, args.title, args.note, args.add, args.drop,
                       model_change=args.model_change, category=args.category,
                       freeze_override=args.freeze_override)
    out.write_bytes(text.encode("utf-8").replace(b"\r\n", b"\n").replace(b"\n", b"\r\n"))
    sha = hashlib.sha256(out.read_bytes()).hexdigest()
    print(f"wrote {args.out}: {len(info['files'])} files; changed {len(info['changed'])}, new {len(info['new'])}, "
          f"dropped {len(info['dropped'])}; SHA-256 {sha}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
