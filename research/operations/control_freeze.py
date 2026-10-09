"""Create/verify METHOD's versioned control receipt without editing pinned code."""
import re,sys
from pathlib import Path
from research.src import control_manifest as frozen
from research.src.custody_text import CRLF_CUSTODY,custody_bytes
ROOT=Path(__file__).resolve().parents[2]
def controlled_bytes(path):
    """Normalize controlled runtime text, preserving raw evidence byte checks."""
    relative=path.relative_to(ROOT).as_posix()
    runtime_text=(relative.startswith(('runtime/src/','runtime/tests/','runtime/config/','runtime/r_ingestion/'))
                  or relative=='runtime/pyproject.toml')
    if runtime_text and path.suffix in {'.py','.json','.R','.toml','.txt'}:
        text=path.read_bytes().decode('utf-8-sig').replace('\r\n','\n').replace('\r','\n')
        return 'CRLF',text.replace('\n','\r\n').encode('utf-8')
    if relative in CRLF_CUSTODY:
        return 'RAW',custody_bytes(path,ROOT)        # the rank CSV is hashed over CRLF bytes on every platform (GOV-02)
    return frozen.normalization(path)
def selected():
    text=(ROOT/'METHOD.md').read_text(encoding='utf-8-sig')
    name=re.search(r'Active freeze:\s*\[([^\]]+)\]\(\1\)',text)
    method=re.search(r'Method \*\*([^*]+)\*\*',text)
    control=re.search(r'Control revision \*\*([^*]+)\*\*',text)
    if not name or not method or not control or not re.fullmatch(r'CONTROL_MANIFEST_\d{4}-\d{2}-\d{2}-\d+\.md',name[1]):
        raise ValueError('METHOD needs exact active method/control/manifest')
    old=frozen.NAME;frozen.NAME=name[1];frozen.EXCLUDE=frozen.EXCLUDE-{old}|{frozen.NAME}
    frozen.APPEND_STORES=frozen.APPEND_STORES+('research/issued_research/','research/experiments/runs/')
    # Generated or periodically refreshed state that every import / weekly probe rewrites; each has its own `verify` that regenerates and compares.
    frozen.APPEND_STORES=frozen.APPEND_STORES+('research/scoreboard/','research/reachability/','research/data/raw/evidence/')
    frozen.EXCLUDE=frozen.EXCLUDE|{'CURRENT_STATE.md'}
    from research.src.combined_log import active_log
    # The header and each later append have separate canonical custody.
    frozen.EXCLUDE=frozen.EXCLUDE|{active_log(ROOT).relative_to(ROOT).as_posix()}
    def custom_inventory():
        paths=list(ROOT.glob("*.md"))
        paths.extend(p for p in (ROOT/".github").rglob("*") if p.is_file())
        paths.extend(ROOT/name for name in (".gitignore",".gitattributes","GAME_PREDICTION_RANK_LOG.csv") if (ROOT/name).exists())
        paths.extend((ROOT/"prediction logs").glob("PREDICTION_LOG_COMBINED*.md"))
        paths.extend(p for p in (ROOT/"research").rglob("*") if p.is_file())
        paths.extend(p for p in (ROOT/"runtime").rglob("*") if p.is_file())
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
            if rel in frozen.EXCLUDE or rel=="research/canonical_ledger.jsonl" or rel.startswith(frozen.APPEND_STORES):continue
            if "/benchmark/" in f"/{rel}/" or "/cricsheet_odi/" in f"/{rel}/" or any(part.endswith("_cache") for part in rel.split("/")) or "__pycache__" in rel or ".pytest_cache" in rel or path.suffix==".pyc":continue
            mode,data=controlled_bytes(path)
            rows.append((rel,mode,frozen.hashlib.sha256(data).hexdigest(),len(data)))
        return rows
    frozen.inventory=custom_inventory
    return method[1],control[1]
def main():
    method,control=selected();path=ROOT/frozen.NAME
    if '--verify' in sys.argv:
        n,errors=frozen.verify()
        text=path.read_text(encoding='utf-8-sig')
        if f'Method: **{method}**; control **{control}**.' not in text:errors.append('MANIFEST_METHOD_CONTROL_MISMATCH')
        print(f'{frozen.NAME}: {n} files; {len(errors)} mismatches')
        for item in errors:print(item)
        return bool(errors)
    if path.exists():raise FileExistsError('Never overwrite a versioned receipt')
    text=frozen.render(frozen.inventory())
    text=text.replace('# Control manifest - 2026-10-01-1','# Control manifest - '+frozen.NAME.removeprefix('CONTROL_MANIFEST_').removesuffix('.md'),1)
    text=text.replace('Method: **MDS-2026.10.01-v7.0**; control **CR-2026.10.01-I1**.',f'Method: **{method}**; control **{control}**.',1)
    text=text.replace('User-authorized October overhaul.','User-authorized October overhaul and requested-analysis/canonical-log repair. Earlier receipts and pinned model dependencies remain unchanged.',1)
    text=text.replace('canonical ledger/issued/pilot transactions','canonical ledger/issued/issued_research/pilot/experiment-run transactions',1)
    with path.open('x',encoding='utf-8') as handle:handle.write(text)
    print(path)
    return 0
if __name__=='__main__':raise SystemExit(main())
