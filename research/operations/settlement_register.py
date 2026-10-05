"""Read the selected, hash-bound all-log settlement register without reissuing IDs."""
import hashlib
import json
from pathlib import Path

def selected(root):
    root=Path(root).resolve()
    pointer=root/'research/current_settlement_register.json'
    if not pointer.exists(): return None
    config=json.loads(pointer.read_text(encoding='utf-8'))
    path=(root/config['manifest_path']).resolve()
    if not path.is_relative_to(root/'research/verification'):
        raise ValueError('Settlement manifest outside verification store')
    raw=path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=config['manifest_sha256']:
        raise ValueError('Selected settlement manifest changed')
    manifest=json.loads(raw)
    rows=manifest['records']
    ids=[r['canonical_id'] for r in rows]
    if len(ids)!=len(set(ids)) or manifest['event_count']!=len(rows):
        raise ValueError('Duplicate or incomplete settlement coverage')
    for r in rows:
        for key in ('event','competition','original_scheduled_start','current_state',
                    'unresolved_contracts_or_fields','remaining_requirement','canonical_pointer','source_custody_notes'):
            if not r.get(key): raise ValueError('Incomplete settlement carryover: '+r['canonical_id']+':'+key)
        if r.get('performance_eligible') is not False:
            raise ValueError('Historical settlement admission cannot be inferred from register')
    return {**config,'manifest':manifest}
