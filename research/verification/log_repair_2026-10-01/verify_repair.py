from pathlib import Path
import hashlib,json,re,sys,html
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from research.operations.verify_custody import run
from research.operations.control_freeze import selected
from research.src import control_manifest
from research.src.ledger import read_records
from research.src.issue import PART6,CANONICAL_LEDGER,_custody
from research.operations.log_card import research_cards,next_id,pending
A=Path(__file__).resolve().parent
receipt=run();assert receipt['valid'],receipt['issues']
selected();count,errors=control_manifest.verify();assert not errors,errors
receipt['checks'].update(active_freeze=control_manifest.NAME,active_manifest_files=count,active_manifest_mismatches=errors)
records=read_records(CANONICAL_LEDGER);cards=research_cards(records)
assert len(cards)==4 and len(records)==8 and not pending(records)
assert [c['card_id'] for c in cards]==['P-523','P-524','P-525','P-526'] and next_id()=='P-527'
raw,_=_custody(PART6)
old=(A/'originals/prediction logs/PREDICTION_LOG_COMBINED_6.md').read_bytes()
assert raw.count(old)==1,'pre-repair Part 6 bytes must remain contiguous and unchanged'
receipt['checks'].update(part6_pre_repair_bytes_retained_contiguously=True,ledger_records=len(records),pending_research_transactions=0,ledger_head_sha256=records[-1]['record_sha256'])
status=(ROOT/'GAME_LOG_STATUS_CURRENT.md').read_text(encoding='utf-8')
assert status.count('<!-- BEGIN CURRENT RESEARCH QUEUE -->')==1
assert status.count('## Historical status snapshots — superseded for current queue')==1
assert 'Next canonical ID: P-527' in status and control_manifest.NAME in status
original_status=(A/'originals/GAME_LOG_STATUS_CURRENT.md').read_bytes()
assert (ROOT/'GAME_LOG_STATUS_CURRENT.md').read_bytes().count(original_status)==1
mini=next((ROOT/'Mini logs (to be sent to actual log later)').rglob('PREDICTION_MINI_RUNNING_LOG_P523_ONWARD.md'))
assert 'not an active running log' in mini.read_text(encoding='utf-8')
receipts=json.loads((A/'COMMIT_RECEIPTS.json').read_text(encoding='utf-8'))
assert hashlib.sha256((A/'originals/mini_at_retirement.md').read_bytes()).hexdigest()==receipts['mini_original_sha256']
assert all(c['source_sha256']==hashlib.sha256(Path(c['source_path']).read_bytes()).hexdigest() for c in cards)
receipt['checks'].update(status_register='ONE_CURRENT_QUEUE_ONE_HISTORY_HEADING',mini='RETIRED_EXACT_ORIGINAL_RETAINED',original_import_hashes_verified=4)
# Compare posted names, not changing live averages/WAR fields.
D=Path((A/'delivery_dir.txt').read_text(encoding='utf-8'))
initial=json.loads((A/'api_lineup.body').read_text(encoding='utf-8'))
latest=json.loads((D/'kbo_lineup.body').read_text(encoding='utf-8'))
def order(data,index):
    raw=data[index][0]
    t=json.loads(raw) if isinstance(raw,str) else raw
    return [html.unescape(re.sub('<[^>]+>',' ',r['row'][1]['Text'])).strip() for r in t['rows']]
assert order(initial,3)==order(latest,3) and order(initial,4)==order(latest,4)
receipt['checks']['posted_lineup_names_unchanged_on_delivery_refresh']=True
source=json.loads((A/'verified_sources.json').read_text(encoding='utf-8'))
for r in source['receipts']:
    assert hashlib.sha256((ROOT/r['body_path']).read_bytes()).hexdigest()==r['response_sha256']
receipt['checks']['current_research_source_bodies_verified']=source['verified_source_bodies']
body=next(c for c in cards if c['card_id']=='P-526')
text=Path(body['projection_path']).read_text(encoding='utf-8')
assert 'top third' in text and 'No final score, grade or retrospective' in text
assert text.index('| **1** | **Combined Under')<text.index('| **2** | **Samsung')<text.index('| **3** | **Hanwha')<text.index('| **4** | **Combined Over')
receipt['checks']['kbo_ranks_and_live_timing_readback']=True
(A/'FINAL_CHECKS.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2,ensure_ascii=False))
