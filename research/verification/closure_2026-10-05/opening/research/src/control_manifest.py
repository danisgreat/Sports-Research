"""Create or verify the active control freeze, chained to the archive manifest."""
from __future__ import annotations
import hashlib
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
NAME=re.search(r"Active freeze: \[(CONTROL_MANIFEST_[^\]]+)\]", (ROOT/"METHOD.md").read_text(encoding="utf-8-sig"))[1]
EXCLUDE={NAME,"GAME_LOG_STATUS_CURRENT.md","VERIFICATION_RECEIPT_2026-09-28.md",
         "prediction logs/PREDICTION_LOG_COMBINED_6.md"}
APPEND_STORES=("research/daily/","research/verification/","research/issued/","research/transactions/",
              "research/pilot/","research/shadow/","research/data/source_receipts/",
              "research/data/raw/source_snapshots/")


def normalization(path):
    raw=path.read_bytes()
    if path.suffix.lower()!=".md":return "RAW",raw
    text=raw.decode("utf-8-sig").replace("\r\n","\n").replace("\r","\n")
    return "CRLF",text.replace("\n","\r\n").encode("utf-8")


def inventory():
    paths=list(ROOT.glob("*.md"))
    paths.extend(p for p in (ROOT/".github").rglob("*") if p.is_file())
    paths.extend(ROOT/name for name in (".gitignore",".gitattributes","GAME_PREDICTION_RANK_LOG.csv") if (ROOT/name).exists())
    paths.extend((ROOT/"prediction logs").glob("PREDICTION_LOG_COMBINED*.md"))
    paths.extend(p for p in (ROOT/"research").rglob("*") if p.is_file())
    archive=ROOT/"Previous Sports Results"
    paths.extend(archive.glob("*.md"))
    paths.extend((archive/"_canonical").glob("*manifest*.json"))
    paths.extend((archive/"_canonical").glob("*correction*.jsonl"))
    paths.extend((archive/"_canonical").glob("*.md"))
    paths.extend((archive/"_custody").glob("*manifest*.json"))
    paths.extend(archive/"_custody"/name for name in ("corrections.jsonl","originals_index.jsonl","verified_facts.json") if (archive/"_custody"/name).exists())
    paths.extend((archive/"_football_research").glob("*.py"))
    paths.extend((archive/"_football_research").glob("*.md"))
    rows=[]
    for path in sorted(set(paths)):
        rel=path.relative_to(ROOT).as_posix()
        if rel in EXCLUDE or rel=="research/canonical_ledger.jsonl" or rel.startswith(APPEND_STORES):continue
        if "/benchmark/" in f"/{rel}/" or "__pycache__" in rel or ".pytest_cache" in rel or path.suffix==".pyc":continue
        mode,data=normalization(path)
        rows.append((rel,mode,hashlib.sha256(data).hexdigest(),len(data)))
    return rows


def render(rows):
    lines=["# Control manifest - 2026-10-01-1","","Method: **MDS-2026.10.01-v7.0**; control **CR-2026.10.01-I1**.",
           "Status: **CURRENT; selected by METHOD.md**.","",
           "User-authorized October overhaul. Historical forecast values and original run bytes are preserved. No live qualification or prospective pilot is asserted.","",
           "CRLF entries decode optional UTF-8 BOM, normalize newline forms, then hash UTF-8 with CRLF. RAW entries hash exact bytes. This manifest excludes itself, the living status/verification output and active Part 6. Append stores (daily runs, source observations, shadows, canonical ledger/issued/pilot transactions) use their own retained hash chains; original shadow custody is separately checked. Restricted benchmark bodies remain local and ignored.","",
           "The archive's canonical manifest and source-custody manifest chain its complete indexed CSV/receipt/output scope. Bulk derived CSVs need not be duplicated here. Sport yearly narrative documents outside that archive hash scope remain reference documentation; they are not admitted forecast inputs. Do not infer unlisted source truth or procedural completeness from this receipt.","",f"Listed files: **{len(rows)}**.","","| File | Mode | SHA-256 | Bytes |","|---|---|---|---:|"]
    lines.extend(f"| `{p}` | {mode} | `{digest}` | {size} |" for p,mode,digest,size in rows)
    return "\n".join(lines)+"\n"


def write():
    target=ROOT/NAME
    if target.exists():raise FileExistsError("freeze already exists; use a versioned new control receipt")
    target.write_text(render(inventory()),encoding="utf-8")


def verify():
    rows={}
    for line in (ROOT/NAME).read_text(encoding="utf-8-sig").splitlines():
        match=re.match(r"^\| `([^`]+)` \| (CRLF|RAW) \| `([0-9a-f]{64})` \| (\d+) \|$",line)
        if match:rows[match[1]]=(match[2],match[3],int(match[4]))
    current={p:(mode,digest,size) for p,mode,digest,size in inventory()}
    return len(rows),[name for name in sorted(rows.keys()|current.keys()) if rows.get(name)!=current.get(name)]


if __name__=="__main__":
    import sys
    if len(sys.argv)>1 and sys.argv[1]=="verify":
        n,errors=verify();print(f"{n} files; {len(errors)} mismatches")
        for name in errors:print(name)
        raise SystemExit(bool(errors))
    write()
