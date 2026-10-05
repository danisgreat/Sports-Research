"""Retain the first draft receipt and advance the final joint-score correction."""
from pathlib import Path
import hashlib,json

ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).parent
old=json.loads((OUT/'document_changes.json').read_text())
target=OUT/'document_changes_v2.json'
if target.exists():raise FileExistsError('Already finalized')
for row in old['files']:
    path=ROOT/row['path'];raw=path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=row['after_sha256']:raise ValueError('Document changed outside measured delivery')
    text=raw.decode('utf-8-sig').replace('CR-2026.10.05-I7','CR-2026.10.05-I8')
    if row['path']=='METHOD.md':text=text.replace('CONTROL_MANIFEST_2026-10-05-7.md','CONTROL_MANIFEST_2026-10-05-8.md')
    updated=text.encode('utf-8');path.write_bytes(updated)
    row['after_sha256']=hashlib.sha256(updated).hexdigest()
old['reason']='Final joint-score support guards; first draft document changes and receipt 7 retained.'
with target.open('x',encoding='utf-8') as handle:json.dump(old,handle,indent=2);handle.write('\n')
