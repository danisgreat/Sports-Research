"""Append exact dated diagnostic bytes to the existing external mini only."""
import hashlib, json, os
from datetime import datetime, timezone
from pathlib import Path
from research.src.eligibility import canonical_bytes, digest

OUT=Path(__file__).resolve().parent; ROOT=OUT.parents[2]
MINI=Path(r'C:\Users\danie\Downloads\PREDICTION_MINI_RUNNING_LOG_P527_ONWARD_UPDATED_4.md')
def sha(raw): return hashlib.sha256(raw).hexdigest()
def put(n,v):
    with (OUT/n).open('x',encoding='utf-8') as f: json.dump(v,f,indent=2,ensure_ascii=False);f.write('\n')
opening=json.loads((OUT/'opening_custody.json').read_text(encoding='utf-8'))
original=(OUT/'original_mini_evidence.txt').read_bytes()
assert MINI.read_bytes()==original and sha(original)==opening['original_mini_sha256']
for ref in opening['files']:
    assert sha((ROOT/ref['path']).read_bytes())==ref['sha256'], 'Authority changed during pass: '+ref['path']
appended=(OUT/'settlement_addendum.txt').read_bytes()
recorded=datetime.now(timezone.utc).isoformat()
with MINI.open('ab') as f:
    f.write(appended);f.flush();os.fsync(f.fileno())
assert MINI.read_bytes()==original+appended
source_refs=[]
for name in ['web_extract_manifest.json','source_body_validation.json','mlb_owner_fields.json','conditional_diagnostic_grades.json']:
    source_refs.append(dict(path=name,sha256=sha((OUT/name).read_bytes())))
grades=json.loads((OUT/'conditional_diagnostic_grades.json').read_text())['events']
previous='0'*64
with (OUT/'diagnostic_revisions.jsonl').open('xb') as f:
    for sequence, event in enumerate(grades,1):
        body=dict(schema_version='local-mini-diagnostic-revision-1',sequence=sequence,previous_sha256=previous,
            recorded_utc=recorded,local_reservation=event['local_reservation'],canonical_id=None,
            original_mini_sha256=sha(original),original_mini_bytes=len(original),
            addendum_sha256=sha(appended),authority_commit=opening['authority_commit'],
            diagnostic=event,source_refs=source_refs,formal_settlement='UNRESOLVED',
            admission='RESEARCH_ONLY_NOT_CERTIFIED',original_source_kind='RETAINED_LOCAL_FALLBACK_NOT_CANONICAL',
            reason='User-requested append-only sporting diagnostic; no original ISSUE record; no contract/source/start certification')
        previous=digest(body);f.write(canonical_bytes({**body,'record_sha256':previous})+b'\n')
put('append_receipt.json',dict(recorded_utc=recorded,mini_path=str(MINI),original_bytes=len(original),
    original_sha256=sha(original),appended_bytes=len(appended),appended_sha256=sha(appended),
    final_bytes=len(MINI.read_bytes()),final_sha256=sha(MINI.read_bytes()),
    original_prefix_verified=True,exact_append_verified=True,diagnostic_revision_count=4,diagnostic_chain_head=previous,
    canonical_records_added=0,canonical_ids_affected=[],archive_performed=False,new_running_log_created=False))
print('Exact in-place append verified; four separate diagnostic revisions, no canonical IDs')
