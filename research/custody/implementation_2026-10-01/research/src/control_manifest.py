"""Create or verify the active freeze receipt including research code/data."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
NAME = "CONTROL_MANIFEST_2026-09-29-3.md"
EXCLUDE = {NAME, "GAME_LOG_STATUS_CURRENT.md", "VERIFICATION_RECEIPT_2026-09-28.md",
           "prediction logs/PREDICTION_LOG_COMBINED_6.md"}


def normalization(path: Path) -> tuple[str,bytes]:
    raw = path.read_bytes()
    if path.suffix.lower() != ".md":
        return "RAW",raw
    text = raw.decode("utf-8-sig").replace("\r\n","\n").replace("\r","\n")
    return "CRLF",text.replace("\n","\r\n").encode("utf-8")


def inventory() -> list[tuple[str,str,str,int]]:
    paths = list(ROOT.glob("*.md"))
    for control_file in (".gitignore", ".gitattributes"):
        if (ROOT / control_file).exists():
            paths.append(ROOT / control_file)
    paths += [p for p in (ROOT / "prediction logs").glob("PREDICTION_LOG_COMBINED*.md")]
    paths += [p for p in (ROOT / "research").rglob("*") if p.is_file()]
    rows=[]
    for path in sorted(set(paths)):
        rel=path.relative_to(ROOT).as_posix()
        if rel in EXCLUDE or "/benchmark/" in f"/{rel}/" or "__pycache__" in rel or ".pytest_cache" in rel:
            continue
        if path.suffix in {".pyc"}:
            continue
        mode,data=normalization(path)
        rows.append((rel,mode,hashlib.sha256(data).hexdigest(),len(data)))
    return rows


def render(rows) -> str:
    lines=["# Control manifest - 2026-09-29-3", "",
           "Method: **MDS-2026.09.29-v6.0**", "Control revision: **CR-2026.09.29-P1**",
           "Category: **USER_INSTRUCTED_PIPELINE / freeze exception D1-D2; D5 location modified by user**",
           "Status: **CURRENT, selected by METHOD.md**", "",
           "The user's 2026-09-29 instruction authorizes research code/data and the new p-ranked pilot. Historical cards, Parts 1–5 and the frozen original P-518 source block in Part 6 are untouched. P-518–P-522 remain reserved; new cards continue at P-523 in Part 6. EPL's retrospective holdout pass is not prospective card skill.",
           "", "For CRLF rows, decode UTF-8 with an optional BOM, normalize CRLF/CR to LF, then encode every LF as CRLF before hashing. RAW rows hash exact bytes. The manifest excludes itself, the living status file, active Part 6 and the living verification receipt. Odds-bearing or locally restricted secondary raw files stay under ignored `research/data/benchmark/`; their hashes are in data receipts. Forecast modules read only processed score inputs.",
           "",f"Listed files: **{len(rows)}**.","",
           "| File | Mode | SHA-256 | Bytes |", "|---|---|---|---:|"]
    lines += [f"| `{path}` | {mode} | `{digest}` | {size} |" for path,mode,digest,size in rows]
    lines.append("")
    return "\n".join(lines)


def write() -> None:
    (ROOT / NAME).write_text(render(inventory()),encoding="utf-8")


def verify() -> tuple[int,list[str]]:
    content=(ROOT / NAME).read_text(encoding="utf-8-sig")
    rows={}
    for line in content.splitlines():
        match=re.match(r"^\| `([^`]+)` \| (CRLF|RAW) \| `([0-9a-f]{64})` \| (\d+) \|$",line)
        if match:
            rows[match.group(1)]=(match.group(2),match.group(3),int(match.group(4)))
    current={p:(mode,digest,size) for p,mode,digest,size in inventory()}
    errors=[]
    for name in sorted(rows.keys()|current.keys()):
        if rows.get(name)!=current.get(name):
            errors.append(name)
    return len(rows),errors


if __name__=="__main__":
    import sys
    if len(sys.argv)>1 and sys.argv[1]=="verify":
        n,errors=verify()
        print(f"{n} listed files; {len(errors)} mismatches")
        for name in errors: print(name)
        raise SystemExit(bool(errors))
    write()
