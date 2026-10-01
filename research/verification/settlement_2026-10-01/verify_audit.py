"""Verify actual writes, original bytes, source readbacks and diagnostic arithmetic."""
import csv,json,hashlib,re,sys
from pathlib import Path
from datetime import datetime,timezone
from math import log
A=Path(__file__).resolve().parent;R=A.parents[2];sys.path.insert(0,str(R))
from research.src.issue import _custody,next_card_id
from research.src.sources import verified_body
from research.src import control_manifest
sys.path.insert(0,str(A))
from freeze_current_manifest import selected_module
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(v):return json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()
I=json.loads((A/'initial.json').read_text());S=json.loads((A/'SUMMARY.json').read_text());checks={};errors=[]
append_paths=['prediction logs/PREDICTION_LOG_COMBINED_6.md','GAME_LOG_STATUS_CURRENT.md','P518_P522_RECONCILIATION.md','LEARNING_REGISTER.md','LEARNINGS_INDEX.md','CHANGELOG.md']
append_paths +=[x['path'] for x in I['snapshots'] if x['path'].startswith('Mini logs') and x['path'].endswith('.md')]
tag=b'<!-- SETTLEMENT-AUDIT-20261001 -->'
for rel in append_paths:
    original=(A/'originals'/rel).read_bytes();current=(R/rel).read_bytes()
    assert current.startswith(original),rel+' lost original byte prefix'
    assert current.count(tag)==1,rel+' missing or duplicate actual append'
checks['verified_actual_append_prefixes']=len(append_paths)
for item in I['snapshots']:
    retained=(A/'originals'/item['path']).read_bytes();assert sha(retained)==item['sha256']
    if item['path'] in append_paths or item['path'] in ('METHOD.md','CURRENT_RULES.md','research/SETTLED_OUTCOMES_CORRECTIONS.csv','research/data/processed/legacy_learning/source_anchor_corrections.json'):continue
    assert sha((R/item['path']).read_bytes())==item['sha256'],item['path']+' changed'
checks['initial_snapshot_files_verified']=len(I['snapshots'])
anchors=json.loads((R/'research/data/processed/legacy_learning/source_anchor_corrections.json').read_text())['revisions']
prior_anchors=json.loads((A/'originals/research/data/processed/legacy_learning/source_anchor_corrections.json').read_text())['revisions']
assert anchors[:len(prior_anchors)]==prior_anchors and len(anchors)-len(prior_anchors)==20
checks['legacy_source_anchor_revisions_added']=20
for n in range(1,6):
    name='prediction logs/PREDICTION_LOG_COMBINED'+('' if n==1 else f'_{n}')+'.md'
    assert (R/name).read_bytes()==(A/'originals'/name).read_bytes()
_custody(R/'prediction logs/PREDICTION_LOG_COMBINED_6.md')
checks['parts1_to5']='EXACT_BYTES_UNCHANGED';checks['part6_original_block']='141740_BYTES_SHA_MATCHED'
assert next_card_id()=='P-523';checks['canonical_next_id']='P-523'
assert not (R/'research/canonical_ledger.jsonl').exists();checks['canonical_transactions_created']=0
rows=list(csv.DictReader((A/'diagnostic_contracts.csv').open(encoding='utf-8')))
assert len(rows)==34
for r in rows:
    p=float(r['p_stated_original']);y=int(r['outcome']);assert abs((p-y)**2-float(r['diagnostic_brier']))<1e-12
    assert abs(-log(p if y else 1-p)-float(r['diagnostic_logloss']))<1e-12
    assert r['performance_eligible']=='False' and not r['p_model_original'] and not r['p_card_original']
    assert not r['approved_baseline_score']
    line=re.search(r'(Over|Under)\s+(\d+\.\d+)',r['contract'])
    if line:
        v=float(r['endpoint_value']);threshold=float(line[2]);assert int(v>threshold if line[1]=='Over' else v<threshold)==y
    else:
        line=re.search(r'([+−-])(\d+\.\d+)',r['contract'])
        if line:
            v=float(r['endpoint_value'].replace('Mets +','').replace('Nationals −','-'))
            adj=float(line[2])*(-1 if line[1] in ('−','-') else 1);assert int(v+adj>0)==y
checks['diagnostic_scores_and_numeric_thresholds_verified']=34
prev='0'*64;seen=[]
for line in (A/'historical_learning_revisions.jsonl').read_text(encoding='utf-8').splitlines():
    record=json.loads(line);digest=record.pop('revision_sha256');assert record['previous_revision_sha256']==prev
    assert sha(canon(record))==digest and record['payload']['performance_eligible'] is False
    assert record['record_type'] in ('HISTORICAL_DIAGNOSTIC_REVIEW','HISTORICAL_DIAGNOSTIC_CORRECTION');prev=digest;seen.append(record['payload']['record_identity'])
assert len(seen)==117 and len(set(seen))==116 and prev==S['diagnostic_revision_head']
checks['diagnostic_revision_count']=117;checks['diagnostic_reviewed_identities']=116;checks['diagnostic_revision_head']=prev
report=(A/'REPORT.md').read_text(encoding='utf-8');assert len(re.findall(r'^### Review:',report,re.M))==116
for letter in 'ABCDEF':assert len(re.findall(r'^\*\*'+letter+r'\.',report,re.M))==121,letter+' review sections'
checks['complete_A_to_F_reviews']='116_CARD_OR_CLAIM_PLUS5_SHADOW'
inventory=list(csv.DictReader((A/'initial_and_final_inventory.csv').open(encoding='utf-8')))
assert len(inventory)==len({r['card_id'] for r in inventory})==523
checks['initial_final_inventory_identities']=523
for p in (A/'current_receipts').glob('*.json'):
    receipt=json.loads(p.read_text())
    if receipt['status']=='FETCHED':verified_body(receipt['receipt'],R)
checks['current_raw_source_bodies_verified']=S['current_retained_raw_bodies']
receipt=json.loads((A/'legacy_correction_receipt.json').read_text());corrections=list(csv.DictReader((R/'research/SETTLED_OUTCOMES_CORRECTIONS.csv').open(encoding='utf-8')))
assert len(corrections)==len({r['revision_id'] for r in corrections})==50
assert sha((R/'research/SETTLED_OUTCOMES_LEDGER.csv').read_bytes())==receipt['immutable_base_ledger_sha256']
assert sha((R/'research/SETTLED_OUTCOMES_CORRECTIONS.csv').read_bytes())==receipt['corrections_sha256']
checks['historical_ledger_corrections']=50;checks['historical_base_ledger']='EXACT_BYTES_UNCHANGED'
for shadow in json.loads((A/'shadow_dispositions.json').read_text()):
    assert sha((R/shadow['shadow_path']).read_bytes())==shadow['unchanged_shadow_sha256']
checks['frozen_shadows_unchanged']=5
nb=json.loads((A/'audit_checks.ipynb').read_text());ns={}
for c in nb['cells']:
    if c['cell_type']=='code':exec(''.join(c['source']),ns)
checks['companion_notebook_cells']='EXECUTED_SUCCESSFULLY'
control_manifest=selected_module()
checks['selected_manifest']=control_manifest.NAME
if (R/control_manifest.NAME).exists():
    count,mismatches=control_manifest.verify();assert not mismatches,mismatches
    checks['control_manifest_listed_files']=count;checks['control_manifest_mismatches']=0
else:checks['control_manifest']='NOT_CREATED_YET'
result={'observed_utc':datetime.now(timezone.utc).isoformat(),'valid':True,'checks':checks,'limitation':'Byte/score checks confirm mechanics and unchanged custody; zero certified issue/settlement or predictive-skill admission.'}
(A/'VERIFICATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
