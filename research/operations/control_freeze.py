"""Create/verify METHOD's versioned control receipt without editing pinned code."""
import re,sys
from pathlib import Path
from research.src import control_manifest as frozen
ROOT=Path(__file__).resolve().parents[2]
def selected():
    text=(ROOT/'METHOD.md').read_text(encoding='utf-8-sig')
    name=re.search(r'Active freeze:\s*\[([^\]]+)\]\(\1\)',text)
    method=re.search(r'Method \*\*([^*]+)\*\*',text)
    control=re.search(r'Control revision \*\*([^*]+)\*\*',text)
    if not name or not method or not control or not re.fullmatch(r'CONTROL_MANIFEST_\d{4}-\d{2}-\d{2}-\d+\.md',name[1]):
        raise ValueError('METHOD needs exact active method/control/manifest')
    old=frozen.NAME;frozen.NAME=name[1];frozen.EXCLUDE=frozen.EXCLUDE-{old}|{frozen.NAME}
    frozen.APPEND_STORES=frozen.APPEND_STORES+('research/issued_research/','research/experiments/runs/')
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
