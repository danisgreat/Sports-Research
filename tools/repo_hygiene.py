#!/usr/bin/env python3
"""Repository hygiene check for CI (added 2026-09-25(c)).

Fails (exit 1) when any of these holds:
1. a tracked path is a dependency tree or build output: node_modules/, __pycache__/, *.pyc,
   .codex_spreadsheet_tmp/, .claude/settings.local.json;
2. a tracked file is larger than --max-mb (default 10 MB), unless it is allow-listed below;
3. a tracked Markdown or Python file contains a control character. Heredoc and `python -c` edits have
   silently written backspace bytes before (memory: shell-quoting corruption);
4. a tracked Markdown file contains a literal "\\n" joining two table rows ("|\\n|") or following
   bold text ("**\\nWord"). This is the corruption shape found in README and RULES_GENERAL on 2026-09-25;
5. (added 2026-09-26) two tracked files over 1 KB are byte-identical and at least one of them lives outside
   `archive/` and `prediction logs/`. The retired runtime once stored 319 identical copies of its inputs
   (archive/DEDUP_INDEX_2026-09-26.md); live folders must not start doing the same. Historical duplicates
   inside the archive and the component-log folder are provenance and are allowed.

Usage: python tools/repo_hygiene.py [--max-mb 10]
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

FORBIDDEN = [
    (re.compile(r"(^|/)node_modules/"), "dependency tree (node_modules)"),
    (re.compile(r"(^|/)__pycache__/|\.py[cod]$"), "Python build output"),
    (re.compile(r"^\.codex_spreadsheet_tmp/"), "Codex tool scratch directory"),
    (re.compile(r"^\.claude/settings\.local\.json$"), "machine-local agent settings"),
]
# Large files that are canonical records, not artefacts (the combined prediction logs and archives).
LARGE_OK = re.compile(r"^(PREDICTION_LOG_COMBINED(_\d+)?\.md|archive/.+|prediction logs/.+)$")
CTRL = re.compile(rb"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
LITERAL_NL = re.compile(r"\|\\n\||\*\*\\n[A-Z]")


def tracked_files(repo: Path = REPO) -> list[str]:
    out = subprocess.run(["git", "-C", str(repo), "ls-files", "-z"], capture_output=True, check=True).stdout
    return [p for p in out.decode("utf-8").split("\0") if p]


def check(paths: list[str], repo: Path = REPO, max_mb: float = 10.0) -> list[str]:
    problems = []
    for rel in paths:
        for rx, why in FORBIDDEN:
            if rx.search(rel):
                problems.append(f"FORBIDDEN ({why}): {rel}")
                break
        p = repo / rel
        if not p.is_file():
            continue
        size = p.stat().st_size
        if size > max_mb * 1024 * 1024 and not LARGE_OK.match(rel):
            problems.append(f"LARGE ({size / 1048576:.1f} MB > {max_mb} MB): {rel}")
        if rel.endswith((".md", ".py")) and not rel.startswith("archive/") and not rel.startswith("prediction logs/"):
            data = p.read_bytes()
            m = CTRL.search(data)
            if m:
                problems.append(f"CONTROL CHARACTER {m.group()!r} at byte {m.start()}: {rel}")
            if rel.endswith(".md"):
                t = data.decode("utf-8", errors="replace")
                for mm in LITERAL_NL.finditer(t):
                    line = t.count("\n", 0, mm.start()) + 1
                    problems.append(f"LITERAL \\n ARTEFACT at line {line}: {rel}")
    problems += duplicate_problems(paths, repo)
    return problems


HISTORICAL = ("archive/", "prediction logs/")


def duplicate_problems(paths: list[str], repo: Path = REPO, min_bytes: int = 1024) -> list[str]:
    """Byte-identical tracked files (> min_bytes) where at least one copy is outside the historical folders.
    Content is compared in the CRLF-normalised form, so a checkout's line endings do not matter."""
    import hashlib
    groups: dict[str, list[str]] = {}
    for rel in paths:
        p = repo / rel
        if not p.is_file() or p.stat().st_size <= min_bytes:
            continue
        data = p.read_bytes()
        if b"\x00" not in data:
            data = data.replace(b"\r\n", b"\n")
        groups.setdefault(hashlib.sha256(data).hexdigest(), []).append(rel)
    out = []
    for rels in groups.values():
        if len(rels) > 1 and any(not r.startswith(HISTORICAL) for r in rels):
            out.append("DUPLICATE (byte-identical): " + ", ".join(sorted(rels)))
    return out


def main(argv=None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--max-mb", type=float, default=10.0)
    args = ap.parse_args(argv)
    paths = tracked_files()
    problems = check(paths, REPO, args.max_mb)
    print(f"repo hygiene: {len(paths)} tracked files, {len(problems)} problem(s)")
    for p in problems[:200]:
        print("  " + p)
    if len(problems) > 200:
        print(f"  … and {len(problems) - 200} more")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
