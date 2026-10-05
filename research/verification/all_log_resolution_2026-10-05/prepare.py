"""Capture local authority and enumerate every historical slot without mutation."""
from datetime import datetime, timezone
from pathlib import Path
import csv
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).parent
def sha(raw): return hashlib.sha256(raw).hexdigest()
def save(name, obj):
    with (OUT/name).open('x', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2); f.write('\n')

def main():
    names = ['METHOD.md', 'CURRENT_RULES.md', 'CARD_AND_LOG_TEMPLATES.md',
             'SCORING_AND_VALIDATION.md', 'GAME_LOG_STATUS_CURRENT.md',
             'VERIFICATION_PROTOCOL.md', 'research/README.md',
             'research/operations/log_card.py', 'research/canonical_ledger.jsonl']
    names += [p.relative_to(ROOT).as_posix() for p in sorted((ROOT/'prediction logs').glob('PREDICTION_LOG_COMBINED*.md'))]
    names += [p.relative_to(ROOT).as_posix() for p in sorted((ROOT/'research/issued_research').glob('*')) if p.is_file()]
    names += [p.relative_to(ROOT).as_posix() for p in sorted((ROOT/'research/model_builds').rglob('*')) if p.is_file()]
    save('opening.json', dict(created_utc=datetime.now(timezone.utc).isoformat(),
         authority='LOCAL_WORKING_FILES; latest user instruction overrides GitHub-only attachment',
         head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
         branch=subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip(),
         initial_status=subprocess.check_output(['git','status','--short'],cwd=ROOT,text=True),
         files=[dict(path=n,bytes=len((ROOT/n).read_bytes()),sha256=sha((ROOT/n).read_bytes())) for n in names]))
    request=Path(r'C:\Users\danie\.codex\attachments\3e190708-8b5c-405d-b990-a76435b2dffd\Pasted text.txt').read_bytes()
    with (OUT/'request.txt').open('xb') as f: f.write(request)
    old=list(csv.DictReader((ROOT/'research/verification/settlement_2026-10-01/initial_and_final_inventory.csv').open(encoding='utf-8-sig',newline='')))
    recent=json.loads((ROOT/'research/verification/closure_2026-10-05/carryover.json').read_text(encoding='utf-8'))['records']
    # CLAIMED_P523 now has a ledger canonical P-523; count this event once.
    normalized=[]
    for r in old:
        r=dict(r); r['canonical_id']='P-523' if r['card_id'] in {'CLAIMED_P523','CLAIMED_P-523'} else r['card_id']
        normalized.append(r)
    assert len(normalized)==523 and len({r['canonical_id'] for r in normalized})==523
    save('historical_inventory.json', normalized)
    save('recent_canonical_carryover_snapshot.json',recent)
    occurrences=[]
    for n in names:
        if not n.startswith('prediction logs/'): continue
        for i,line in enumerate((ROOT/n).read_text(encoding='utf-8-sig').splitlines(),1):
            for handle in sorted(set(re.findall(r'TMP-[A-Z0-9]+(?:-[A-Z0-9]+)*',line))):
                occurrences.append(dict(handle=handle,path=n,line=i,text=line))
    save('temporary_handle_occurrences.json', occurrences)
    selected=[r for r in normalized if r['final_disposition'].startswith('UNRESOLVED') or r['canonical_id'] in {'P-407','P-410','P-492','P-518','P-519','P-520','P-521','P-522'}]
    save('historical_open_review.json', selected)
    print(json.dumps(dict(historical_slots=len(normalized),recent_cards=len(recent),
        total_unique_event_slots=len(normalized)+14,review_cases=len(selected),
        distinct_temporary_handles=len({r['handle'] for r in occurrences})),indent=2))
    for r in selected: print(r['canonical_id'],r['final_disposition'],r['event'],r['remaining_gaps'])

if __name__=='__main__': main()
