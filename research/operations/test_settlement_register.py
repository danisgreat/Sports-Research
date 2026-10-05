import hashlib,json
import pytest
from research.operations.settlement_register import selected

def setup_register(tmp_path,rows=None):
    folder=tmp_path/'research/verification/review';folder.mkdir(parents=True)
    record=dict(canonical_id='P-100',event='A v B',competition='League',original_scheduled_start='MISSING',
                current_state='UNRESOLVED',unresolved_contracts_or_fields=['corners'],remaining_requirement='owner field',
                canonical_pointer='log.md',source_custody_notes='retained original',performance_eligible=False)
    manifest=dict(event_count=len(rows or [record]),records=rows or [record])
    raw=json.dumps(manifest).encode();(folder/'carryover.json').write_bytes(raw)
    pointer=tmp_path/'research/current_settlement_register.json'
    pointer.write_text(json.dumps(dict(manifest_path='research/verification/review/carryover.json',manifest_sha256=hashlib.sha256(raw).hexdigest())))
    return pointer,folder/'carryover.json',record

def test_selected_manifest_hash_and_complete_fields(tmp_path):
    setup_register(tmp_path)
    assert selected(tmp_path)['manifest']['event_count']==1

def test_changed_manifest_fails_before_status_refresh(tmp_path):
    _,body,_=setup_register(tmp_path);body.write_bytes(body.read_bytes()+b' ')
    with pytest.raises(ValueError,match='manifest changed'):selected(tmp_path)

def test_duplicate_event_rejected(tmp_path):
    _,_,r=setup_register(tmp_path)
    # Rebind deliberately malformed content to test semantics beyond the hash.
    body=tmp_path/'research/verification/review/carryover.json';raw=json.dumps(dict(event_count=2,records=[r,r])).encode();body.write_bytes(raw)
    pointer=tmp_path/'research/current_settlement_register.json';obj=json.loads(pointer.read_text());obj['manifest_sha256']=hashlib.sha256(raw).hexdigest();pointer.write_text(json.dumps(obj))
    with pytest.raises(ValueError,match='Duplicate'):selected(tmp_path)

def test_manifest_cannot_escape_verification_store(tmp_path):
    pointer,_,_=setup_register(tmp_path);obj=json.loads(pointer.read_text());obj['manifest_path']='outside.json';pointer.write_text(json.dumps(obj))
    with pytest.raises(ValueError,match='outside verification'):selected(tmp_path)
