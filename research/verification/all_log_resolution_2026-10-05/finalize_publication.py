"""Retain actual published failures and fix byte preservation for workflow files."""
from collections import Counter
from pathlib import Path
import json, subprocess

ROOT=Path(__file__).resolve().parents[3]; OUT=Path(__file__).parent
text=(OUT/'published_run_failure.txt').read_text(encoding='utf-8-sig')
names=[]
for line in text.splitlines():
    if '\tSelected control freeze\t' in line and 'Z ' in line:
        name=line.split('Z ',1)[1]
        if name.startswith(('research/','.github/')):names.append(name)
tracked=set(subprocess.check_output(['git','ls-files','-z'],cwd=ROOT).decode().split('\0'))
rows=[dict(path=name,tracked=name in tracked,present_locally=(ROOT/name).exists()) for name in names]
assert len(rows)==153 and sum(not r['tracked'] and r['present_locally'] for r in rows)==152
data=dict(run_id=37305349280,published_commit='87a2df6dc8e08b84221abf0463b14702b8479fc0',
          mismatches=len(rows),records=rows,counts_by_directory=dict(Counter(str(Path(n).parent).replace('\\','/') for n in names)))
(OUT/'published_freeze_inventory.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
for item in json.loads((OUT/'native_document_changes.json').read_text())['files']:
    path=ROOT/item['path']; raw=path.read_bytes()
    path.write_bytes(raw.replace(b'CR-2026.10.05-I5',b'CR-2026.10.05-I6').replace(b'CONTROL_MANIFEST_2026-10-05-5.md',b'CONTROL_MANIFEST_2026-10-05-6.md'))
note='''
Publication readback: 152 ignored local cache files listed in the full local control freeze remain absent from Git. The first publication also had one workflow line-ending mismatch, corrected with byte-preserving Git attributes. Remote validation remains incomplete; the local freeze does not establish clean-checkout evidence availability. The exact paths are retained in `research/verification/all_log_resolution_2026-10-05/published_freeze_inventory.json`.
'''
for name in ('SOURCES.md','VERIFICATION_PROTOCOL.md','research/README.md'):
    with (ROOT/name).open('a',encoding='utf-8') as stream:stream.write(note)
report='''
## Verified GitHub publication and remaining checkout gaps

The substantive 201-file publication was pushed to GitHub main as `87a2df6dc8e08b84221abf0463b14702b8479fc0`; the remote main SHA matched the local commit and the working tree was clean. GitHub is the publication destination; local working files remain authoritative.

[Actions run 37305349280](https://github.com/danisgreat/Sports-Research/actions/runs/37305349280) completed with regression, canonical projection and reconciliation checks passing. Strict source custody failed on exactly 52 absent local-only bodies (59 verified of 111). All-log readback failed on an absent retained owner body, as expected. The full local freeze reported 153 mismatches: 152 ignored, locally present cache files plus a workflow checkout line-ending mismatch. Its complete path inventory, raw failure output and run metadata are retained beside this report. No evidence gate is bypassed.

The workflow line-ending mismatch is repaired by preserving `.github/**` bytes through Git attributes. The new active control is CR-2026.10.05-I6 / CONTROL_MANIFEST_2026-10-05-6.md. The full local freeze still retains all 152 cache hashes; missing clean-checkout caches remain a real failure. Earlier control receipts and failed run evidence remain unchanged. This publication follow-up changes no issued forecasts, IDs, sporting outcomes or performance eligibility.

The earlier implementation report is a historical pre-publication checkpoint. Its statement that no push had been requested or performed describes that earlier scope, superseded by the later explicit publication request and this verified push. The selected current carryover remains `carryover_v3.json` with 53 records. Fifteen retrospective experiments remain registered but unrun; no prospective success or fitted improvement is claimed.
'''
with (OUT/'REPORT.md').open('a',encoding='utf-8') as stream:stream.write(report)
with (ROOT/'research/verification/implementation_2026-10-05/REPORT.md').open('a',encoding='utf-8') as stream:
    stream.write('\n## Later authorized publication — historical checkpoint clarification\n\nThis report retains the earlier implementation checkpoint. The later user instruction makes local files authoritative and authorizes publication to main. These changes were included in substantive commit 87a2df6dc8e08b84221abf0463b14702b8479fc0, remotely SHA-verified. Current all-log state, control, 53 carryovers and actual remote failures are recorded in [the later all-log report](../all_log_resolution_2026-10-05/REPORT.md). Earlier control/count/no-push statements above are historical evidence, superseded for current operations.\n')
print(json.dumps({k:v for k,v in data.items() if k!='records'},indent=2))
