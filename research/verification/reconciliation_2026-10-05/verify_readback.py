"""Independent invariants for this cleanup/import/addendum; no source rewriting."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,csv,ast,subprocess
from research.src.issue import PART6,CANONICAL_LEDGER,_custody,BEGIN_ORIGINAL,END_ORIGINAL,ORIGINAL_SHA256
from research.src.ledger import read_records
from research.operations.log_card import research_cards,pending,next_id

ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parent
def sha(raw):return hashlib.sha256(raw).hexdigest()
def canonical(value):return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()
def save(name,value):(OUT/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
checks=[]
def check(name,condition,details=None):
    checks.append(dict(name=name,passed=bool(condition),details=details))
    if not condition:raise AssertionError(name)
opening=json.loads((OUT/'opening_custody.json').read_text(encoding='utf-8'))
append=json.loads((OUT/'append_receipt.json').read_text(encoding='utf-8'))
original=(OUT/'originals/prediction logs/PREDICTION_LOG_COMBINED_6.md').read_bytes()
part6,_=_custody(PART6)
source=part6[part6.index(BEGIN_ORIGINAL)+len(BEGIN_ORIGINAL)+2:part6.index(END_ORIGINAL)-2]
check('entire_opening_Part6_prefix_preserved',part6.startswith(original),dict(bytes=len(original),sha256=sha(original)))
check('frozen_141740_byte_source_block',len(source)==141740 and sha(source)==ORIGINAL_SHA256,sha(source))
check('settlement_exact_append_once',part6.count((OUT/'settlement_projection.bin').read_bytes())==1)
check('source_reconciliation_exact_append_once',part6.count((OUT/'source_reconciliation_projection.bin').read_bytes())==1)
records=read_records(CANONICAL_LEDGER)
check('canonical_ledger_prefix_preserved',CANONICAL_LEDGER.read_bytes().startswith((OUT/'originals/research/canonical_ledger.jsonl').read_bytes()))
check('settlement_did_not_change_allocation_ledger',sha(CANONICAL_LEDGER.read_bytes())==append['ledger_sha256'])
check('fifteen_canonical_research_cards',len(research_cards(records))==15)
check('no_pending_transaction_and_next538',not pending(records) and next_id()=='P-538')
allowed={'prediction logs/PREDICTION_LOG_COMBINED_6.md','research/canonical_ledger.jsonl','GAME_LOG_STATUS_CURRENT.md','Mini logs (to be sent to actual log later)/Mini Prediction Log - P-523 onward - 2026-10-01/PREDICTION_MINI_RUNNING_LOG_P523_ONWARD.md'}
for item in opening['files']:
    p=Path(item['path'])
    if not p.is_absolute():p=ROOT/p
    if item['path'] in allowed or p==Path('C:/Users/danie/Downloads/PREDICTION_MINI_RUNNING_LOG_P527_ONWARD_UPDATED_4.md'):continue
    check('original_or_authority_unchanged:'+item['path'],p.exists() and sha(p.read_bytes())==item['sha256'])
for receipt in append['minis']:
    p=Path(receipt['path']);snapshot=OUT/'originals/downloads_mini_current.md' if p.drive and p.parent.name=='Downloads' else OUT/'originals'/p.relative_to(ROOT)
    check('mini_prefix_preserved:'+str(p),p.read_bytes().startswith(snapshot.read_bytes()))
    check('mini_exact_result_hash:'+str(p),sha(p.read_bytes())==receipt['after_sha256'])
    check('mini_twelve_part_reference:'+str(p),len(re.findall(rb'^#### \d+\.',p.read_bytes(),re.M))>=132)
plan=json.loads((OUT/'csv_cleanup_plan.json').read_text(encoding='utf-8'))
for mapping in plan['files']:
    p=ROOT/mapping['destination']
    check('archive_copy_preserved:'+mapping['destination'],p.exists() and sha(p.read_bytes())==mapping['sha256'])
    check('duplicate_source_removed:'+mapping['source'],not (ROOT/mapping['source']).exists())
    with p.open(encoding='utf-8-sig',newline='') as f:count=max(0,len(list(csv.reader(f)))-1)
    check('archive_rowcount:'+mapping['destination'],count==mapping['data_rows'])
check('exact_255_recycled_csvs',plan['count']==255 and sum(x['data_rows'] for x in plan['files'])==34318)
check('no_root_export_folders_left',not list(ROOT.glob('*_CSVs')))
builders=['austria_bundesliga','county_cricket','greek_basket_league','ipl','nrl']
for name in builders:
    p=ROOT/f'research/src/build_{name}_all_years.py';text=p.read_text(encoding='utf-8');ast.parse(text)
    check('builder_AST_and_no_root_exports:'+name,'_CSVs' not in text)
capture=json.loads((OUT/'source_capture_manifest.json').read_text(encoding='utf-8'))
for rec in capture['raw_receipts']:
    if rec.get('body_path'):check('raw_source_hash:'+rec['name'],sha((ROOT/rec['body_path']).read_bytes())==rec['response_sha256'])
for rec in capture['tool_captures']:check('quarantined_tool_hash:'+rec['path'],sha((ROOT/rec['path']).read_bytes())==rec['sha256'])
expected={'P-527':[['L','W','L','W'],['L','L','W','W']],'P-528':[['W','W','L','L']],'P-529':[['W','W','L','W'],['W','W','L','W']],'P-530':[['W','W','W','L'],['W','W','L','L']],'P-531':[['L','L','W','W'],['L','W','W','L']],'P-532':[['L','W','W','L']],'P-533':[['W','L','L','W']],'P-534':[['L','L','W','W']],'P-535':[['W','W','L','L']],'P-536':[['W','W','L','L']],'P-537':[['UNRESOLVED_PERIOD','W','L','UNRESOLVED_PROVIDER_FIELD','W']]}
grades=json.loads((OUT/'conditional_diagnostic_grades.json').read_text(encoding='utf-8'))
for g in grades:
    check('row_grade_signature:'+g['card_id'],[[r['diagnostic_grade'] for r in v['rows']] for v in g['versions']]==expected[g['card_id']])
    for v in g['versions']:
        for r in v['rows']:
            if r['market']=='TOTAL':
                val=(sum(g['score'])-r['line'])*(1 if r['side']=='OVER' else -1)
                check('independent_total_arithmetic:'+g['card_id']+r['label'],r['diagnostic_grade']==('W' if val>0 else 'L' if val<0 else 'P'))
            if r['market']=='SPREAD':
                val=(g['score'][0]-g['score'][1])*(1 if r['side']=='HOME' else -1)+r['line']
                check('independent_spread_arithmetic:'+g['card_id']+r['label'],r['diagnostic_grade']==('W' if val>0 else 'L' if val<0 else 'P'))
    check('no_fabricated_probabilities_or_eligibility:'+g['card_id'],g['p'] is None and g['baseline'] is None and not g['performance_eligible'])
revisions=[json.loads(l) for l in (OUT/'diagnostic_revisions.jsonl').read_text(encoding='utf-8').splitlines()]
previous='0'*64
for i,rec in enumerate(revisions,1):
    body={k:v for k,v in rec.items() if k!='record_sha256'}
    check('diagnostic_chain:'+rec['canonical_id'],rec['sequence']==i and rec['previous_sha256']==previous and rec['record_sha256']==sha(canonical(body)))
    check('diagnostic_source_join:'+rec['canonical_id'],rec['source_event_audit_sha256']==sha((OUT/'source_event_audit.json').read_bytes()) and rec['addendum_sha256']==sha((OUT/'settlement_projection.bin').read_bytes()))
    previous=rec['record_sha256']
check('eleven_diagnostic_revisions',len(revisions)==11)
retros=(OUT/'settlement_addendum.md').read_text(encoding='utf-8')
check('eleven_twelve_part_retrospectives',len(re.findall(r'^#### \d+\.',retros,re.M))==132 and len(re.findall(r'^### Retrospective for P-',retros,re.M))==11)
names=subprocess.check_output(['git','diff','--name-only'],cwd=ROOT,text=True,encoding='utf-8').splitlines()
check('Parts1_to5_and_archive_results_not_edited',not any(n.startswith('Previous Sports Results/') or re.search(r'PREDICTION_LOG_COMBINED_[1-5]\.md$',n) for n in names))
raw=subprocess.check_output(['git','status','--porcelain=v1','--untracked-files=all'],cwd=ROOT)
(OUT/'git_status_exact.txt').write_bytes(raw)
save('changed_files.json',dict(recorded_utc=datetime.now(timezone.utc).isoformat(),git_status=[l.decode('utf-8') for l in raw.splitlines()],external_changed=[r['path'] for r in append['minis'] if 'Downloads' in r['path']],no_staging_commit_or_push=True))
save('final_readback.json',dict(recorded_utc=datetime.now(timezone.utc).isoformat(),passed=True,checks=checks,canonical_next_id=next_id(),canonical_cards=15,imported_unique_events=11,retrospectives=11,recycled_csvs=255,retained_archive_data_rows=34318,raw_source_bodies=sum(bool(r.get('body_path')) for r in capture['raw_receipts']),quarantined_tool_captures=len(capture['tool_captures']),certified=0,performance_eligible=0))
print(f'{len(checks)} scoped readbacks PASS; next P-538; original Part 6 bytes {len(original)} preserved.')
