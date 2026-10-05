"""Append the newly recovered P-520 native proof and select a new control version."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json

ROOT=Path(__file__).resolve().parents[3]; OUT=Path(__file__).parent
def sha(raw): return hashlib.sha256(raw).hexdigest()
def write(path,obj):
    with path.open('x',encoding='utf-8') as stream:
        json.dump(obj,stream,ensure_ascii=False,indent=2);stream.write('\n')

prior=OUT/'carryover_v2.json'; data=json.loads(prior.read_text())
row=next(r for r in data['records'] if r['canonical_id']=='P-520')
requirement='Owner native game 20260927HHLT0 is now verified: Hanwha 6–2 Lotte, September 27, scheduled 17:00 KST, normal final in the ninth. Scheduled time is not certified actual first pitch. Original operator action terms, actual-start semantics, canonical issue/source/baseline receipts and independently audited terminal collection status remain unresolved. No certification or performance eligibility is granted.'
row['remaining_requirement']=requirement
row['unresolved_contracts_or_fields']=[row['unresolved_contracts_or_fields'][0],requirement]
row['source_custody_notes']+=' Native follow-up: research/verification/all_log_resolution_2026-10-05/P-520_native_owner.json; full owner body hash retained in its receipt.'
row['current_state']='OWNER_NATIVE_FINAL; ALL_FOUR_SPORTING_ROWS_DIAGNOSTICALLY_COMPLETE'
data.update(created_utc=datetime.now(timezone.utc).isoformat(),revision='P520_NATIVE_OWNER_IDENTITY_RECOVERED',
            supersedes_manifest=prior.relative_to(ROOT).as_posix(),supersedes_sha256=sha(prior.read_bytes()))
current=OUT/'carryover_v3.json';write(current,data)
pointer=json.loads((ROOT/'research/current_settlement_register.json').read_text())
pointer.update(manifest_path=current.relative_to(ROOT).as_posix(),manifest_sha256=sha(current.read_bytes()))
(ROOT/'research/current_settlement_register.json').write_text(json.dumps(pointer,indent=2)+'\n',encoding='utf-8')
text='''
## Final native-owner follow-up — P-520

This addendum supersedes the earlier P-520 native-ID gap and selects `research/verification/all_log_resolution_2026-10-05/carryover_v3.json`. The official KBO dated game list now returns `20260927HHLT0`, Hanwha away at Lotte, normal final in the ninth, score 6–2, scheduled September 27 at 17:00 KST. The retained full body and receipt are at `research/verification/all_log_resolution_2026-10-05/P-520_native_owner.json`. The scheduled field does not prove actual first pitch. Existing sporting grades are unchanged; original operator terms, issue/baseline custody and audited source independence still prevent formal certification. All 53 carryover IDs remain, with this one native-owner requirement removed.

The local source registry now contains 111 verified receipt bodies; 59 are available from the staged publication and 52 remain excluded local-only. Earlier 110-body counts describe the preceding checkpoint. Local files remain authoritative; GitHub main is the destination. The selected control is CR-2026.10.05-I5, frozen by CONTROL_MANIFEST_2026-10-05-5.md. Earlier append projections and control receipts remain unchanged. No IDs are added; P-538 remains next.
'''
raw=text.replace('\n','\r\n').encode(); part6=ROOT/'prediction logs/PREDICTION_LOG_COMBINED_6.md'; before=part6.read_bytes()
with (OUT/'native_projection.bin').open('xb') as stream:stream.write(raw)
with part6.open('ab') as stream:stream.write(raw)
write(OUT/'native_append_receipt.json',dict(before_bytes=len(before),before_sha256=sha(before),projection_sha256=sha(raw),after_sha256=sha(before+raw)))
with (OUT/'REPORT.md').open('a',encoding='utf-8') as stream:stream.write(text)
with (OUT/'carryover.md').open('a',encoding='utf-8') as stream:stream.write('\nThis is the original dated table. The current hash-bound register is `carryover_v3.json`; its P-520 native-ID gap is superseded by the retained official owner follow-up. Other requirements and all 53 IDs remain.\n')
changed=[]
for item in json.loads((OUT/'document_changes.json').read_text())['files']:
    path=ROOT/item['path']; before_doc=path.read_bytes(); value=before_doc.decode('utf-8-sig').replace('CR-2026.10.05-I4','CR-2026.10.05-I5')
    if path.name=='METHOD.md':value=value.replace('CONTROL_MANIFEST_2026-10-05-4.md','CONTROL_MANIFEST_2026-10-05-5.md')
    value=value.replace('110 receipt bodies verify locally','111 receipt bodies verify locally').replace('clean checkout has 58 bodies','clean checkout has 59 bodies')
    path.write_bytes(value.encode('utf-8'));changed.append(dict(path=item['path'],before_sha256=sha(before_doc),after_sha256=sha(path.read_bytes())))
write(OUT/'native_document_changes.json',dict(files=changed,control='CR-2026.10.05-I5',selected_freeze='CONTROL_MANIFEST_2026-10-05-5.md'))
