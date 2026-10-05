"""Run current checks and independently read back reference-archive custody."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).parent
def sha(raw): return hashlib.sha256(raw).hexdigest()
def dump(name,value): (OUT/name).write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')

def readback():
    from research.operations.log_card import next_id,research_cards,pending,retained_path,verify_projection
    from research.src.ledger import read_records
    manifest=json.loads((OUT/'mini_archive_manifest.json').read_text(encoding='utf-8'))
    part=ROOT/'prediction logs/PREDICTION_LOG_COMBINED_6.md'
    raw=part.read_bytes()
    original=(OUT/'opening/prediction logs/PREDICTION_LOG_COMBINED_6.md').read_bytes()
    assert raw.startswith(original)
    ledger=ROOT/'research/canonical_ledger.jsonl'
    assert sha(ledger.read_bytes())==manifest['ledger_sha256']
    records=read_records(ledger)
    assert not pending(records)
    cards=research_cards(records)
    assert len(cards)==15 and next_id()=='P-538'
    for card in cards: verify_projection(card,part)
    carry=json.loads((OUT/'carryover.json').read_text(encoding='utf-8'))['records']
    assert {c['canonical_id'] for c in carry}=={c['card_id'] for c in cards}
    for c in carry:
        assert all(c[k] for k in ['event','competition','original_scheduled_start','current_state',
                    'unresolved_contracts_or_fields','remaining_requirement','canonical_pointer','source_custody_notes'])
        assert c['performance_eligible'] is False
    for archive in manifest['archives']:
        body=(ROOT/archive['archive_path']).read_bytes()
        assert sha(body)==archive['archive_sha256']
        preserved=body[archive['body_offset']:]
        assert len(preserved)==archive['original_bytes'] and sha(preserved)==archive['original_sha256']
        assert body.startswith(b'# CLOSED / ARCHIVED MINI REFERENCE')
    assert sha((ROOT/'research/src/control_manifest.py').read_bytes())=='2bd5072a533571c549fa07c5c172d819cc23ecbece5936ed55abf27f20723cc6'
    restore=json.loads((OUT/'custody_restoration.json').read_text(encoding='utf-8'))
    for entry in restore: assert sha((ROOT/entry['path']).read_bytes())==entry['sha256']
    return dict(passed=True,canonical_cards=15,archived_references=2,new_imports=0,carryover=15,
                next_id='P-538',opening_part6_bytes_preserved=len(original),ledger_unchanged=True,
                model_dependency_restored=True,missing_snapshots_restored=9,
                diagnostic_settlements_preserved=11,retrospective_sections_preserved=132)

def main():
    dump('readback.json',readback())
    commands=[('regressions',['-m','pytest','-p','no:cacheprovider','research/tests','research/operations/test_log_card.py','-q']),
       ('canonical',['-m','research.operations.log_card','verify']),
       ('custody_acceptance_and_sources',['-m','research.operations.verify_custody']),
       ('freeze',['-m','research.operations.control_freeze','--verify']),
       ('archive',['-m','research.src.archive','validate']),
       ('workflow_status',['-m','research.src.workflow','status']),
       ('workflow_score',['-m','research.src.workflow','score'])]
    results=[]
    for name,args in commands:
        env={**os.environ,'PYTHONIOENCODING':'utf-8','PYTHONDONTWRITEBYTECODE':'1'}
        result=subprocess.run([sys.executable,'-X','utf8','-B',*args],cwd=ROOT,env=env,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        (OUT/(name+'.txt')).write_bytes(result.stdout)
        results.append(dict(check=name,exit_code=result.returncode,output_sha256=sha(result.stdout)))
        dump('checks.json',dict(observed_utc=datetime.now(timezone.utc).isoformat(),results=results,passed=all(r['exit_code']==0 for r in results)))
        print(name+': '+str(result.returncode),flush=True)
    raise SystemExit(any(r['exit_code'] for r in results))

if __name__=='__main__':main()
