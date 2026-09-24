#!/usr/bin/env python3
"""Verify a control manifest against the working tree (added 2026-09-25(c)).

Usage:
    python tools/verify_manifest.py                      # the manifest METHOD.md currently names
    python tools/verify_manifest.py CONTROL_MANIFEST_2026-09-25-3.md
    python tools/verify_manifest.py --include-living     # also require the living logs to match
    python tools/verify_manifest.py --eol asis           # hash raw bytes (no CRLF normalisation)

Exit codes: 0 = every governance file matches; 1 = a mismatch or a missing file; 2 = usage error.
By default the two living logs (PREDICTION_LOG_COMBINED_<n>.md, GAME_LOG_STATUS_CURRENT.md) are
reported but not failed. They change with every card, and the manifest holds only a write-time
snapshot of them.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from manifest_lib import current_manifest, file_digest, is_living, read_rows  # noqa: E402

REPO = Path(__file__).resolve().parent.parent


def verify(manifest: Path, repo: Path = REPO, eol: str = "crlf", include_living: bool = False) -> dict:
    rows = read_rows(manifest)
    out = {"entries": len(rows), "match": [], "mismatch": [], "missing": [], "living_changed": []}
    for rel, sha, _size in rows:
        p = repo / rel
        if not p.exists():
            out["missing"].append(rel)
            continue
        digest, _ = file_digest(p, eol)
        if digest == sha:
            out["match"].append(rel)
        elif is_living(rel) and not include_living:
            out["living_changed"].append(rel)
        else:
            out["mismatch"].append(rel)
    return out


def main(argv=None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("manifest", nargs="?")
    ap.add_argument("--eol", choices=["crlf", "asis"], default="crlf")
    ap.add_argument("--include-living", action="store_true")
    args = ap.parse_args(argv)
    manifest = Path(args.manifest) if args.manifest else current_manifest(REPO)
    if not manifest.is_absolute():
        manifest = REPO / manifest
    if not manifest.exists():
        print(f"error: manifest not found: {manifest}", file=sys.stderr)
        return 2
    res = verify(manifest, REPO, args.eol, args.include_living)
    if res["entries"] == 0:
        print(f"error: no hash rows in {manifest.name}", file=sys.stderr)
        return 2
    print(f"{manifest.name}: {res['entries']} entries — {len(res['match'])} match, "
          f"{len(res['mismatch'])} mismatch, {len(res['missing'])} missing, "
          f"{len(res['living_changed'])} living log(s) changed since the snapshot")
    for k in ("mismatch", "missing"):
        for rel in res[k]:
            print(f"  {k.upper()}: {rel}")
    for rel in res["living_changed"]:
        print(f"  living (not failed): {rel}")
    if res["mismatch"] or res["missing"]:
        print("A governance file changed without a new manifest. Regenerate with tools/make_manifest.py "
              "and repoint METHOD.md and the active mini log (RULES_GENERAL §16.8; PF-7).")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
