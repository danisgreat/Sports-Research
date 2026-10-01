"""Versioned documentation receipt without editing frozen model dependency code.

The original control_manifest module is pinned in all four model builds. Reuse
its inventory/normalization with METHOD's selected filename in this process;
never rewrite its bytes or silently rehash a model build for a log append.
"""
import sys,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from research.src import control_manifest as frozen
def selected_module():
    m=re.search(r'Active freeze:\s*\[([^\]]+)\]\(\1\)',(ROOT/'METHOD.md').read_text(encoding='utf-8-sig'))
    if not m or not re.fullmatch(r'CONTROL_MANIFEST_\d{4}-\d{2}-\d{2}-\d+\.md',m[1]):raise ValueError('METHOD does not select an exact versioned receipt')
    old=frozen.NAME;frozen.NAME=m[1];frozen.EXCLUDE=frozen.EXCLUDE-{old}|{frozen.NAME}
    return frozen
def main():
    module=selected_module()
    if '--verify' in sys.argv:
        n,errors=module.verify();print(f'{module.NAME}: {n} files; {len(errors)} mismatches')
        for name in errors:print(name)
        return int(bool(errors))
    target=ROOT/module.NAME
    if target.exists():raise FileExistsError('Versioned receipt exists; never overwrite')
    text=module.render(module.inventory()).replace('# Control manifest - 2026-10-01-1','# Control manifest - '+module.NAME.removeprefix('CONTROL_MANIFEST_').removesuffix('.md'),1)
    text=text.replace('User-authorized October overhaul.','User-authorized October overhaul and October 1 settlement/learning appends. The earlier freeze remains immutable. The frozen model dependency code and all four model builds are unchanged.',1)
    target.write_text(text,encoding='utf-8');print(target)
    return 0
if __name__=='__main__':raise SystemExit(main())
