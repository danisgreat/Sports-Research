"""Finalize authored audit prose while preserving all pre-session bytes.

Also append a genuine learning-only correction for a detected provenance error.
No original forecast, previous ledger revision or initial audit revision changes.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess,re,pprint,sys
A=Path(__file__).resolve().parent;R=A.parents[2]
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(v):return json.dumps(v,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()
I=json.loads((A/'initial.json').read_text(encoding='utf-8'))
build=json.loads((R/'research/model_builds/current.json').read_text())
expected=next(a['sha256'] for a in build['builds'][0]['artifacts'] if a['path']=='research/src/control_manifest.py')
original=subprocess.run(['git','show','HEAD:research/src/control_manifest.py'],cwd=R,capture_output=True,check=True).stdout
assert sha(original)==expected,'Pinned module bytes differ from HEAD; do not overwrite'
if '--reports-only' not in sys.argv:(R/'research/src/control_manifest.py').write_bytes(original)

# A quoted review URL is not a returned native ID. Preserve the failed old HTTP
# response and append this correction rather than certifying its query parameter.
old=next(r for r in I['prior_receipts'] if r['label']=='P520_KBO_game_list')
body=(R/old['body_path']).read_bytes();assert sha(body)==old['original_receipt']['sha256']
assert b'20260927HHLT0' not in body and '에러'.encode() in body
chain_path=A/'historical_learning_revisions.jsonl';records=[json.loads(x) for x in chain_path.read_text(encoding='utf-8').splitlines()]
rid='HLR-20261001-P-520-NATIVE-ID-CORRECTION'
if not any(r['revision_id']==rid for r in records):
    row={'schema':'historical-learning-revision-1','record_type':'HISTORICAL_DIAGNOSTIC_CORRECTION','revision_id':rid,'created_utc':datetime.now(timezone.utc).isoformat(),'previous_revision_sha256':records[-1]['revision_sha256'],'payload':{'record_identity':'P-520','corrects_revision_id':'HLR-20261001-P-520','field':'native_event_id_custody','old_value':'20260927HHLT0 bound by retained GameCenter request metadata','new_value':'QUERY_CANDIDATE 20260927HHLT0; NOT_OWNER_CONFIRMED','evidence':old,'reason':'Game-list POST returned HTML error, not a game list or returned native ID. Review raw HTTP is a shell. URL query itself cannot certify identity. The exact date/venue/participants and official 6–2 final remain supported; diagnostic threshold grades do not change.','performance_eligible':False}}
    row['revision_sha256']=sha(canon(row))
    with chain_path.open('ab') as f:f.write(canon(row)+b'\n')
    records.append(row)
corr=records[-1]
(A/'READBACK_CORRECTIONS.json').write_text(json.dumps(corr,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
summary=json.loads((A/'SUMMARY.json').read_text());summary.update(diagnostic_revision_count=len(records),diagnostic_revision_head=records[-1]['revision_sha256'],readback_native_id_corrections=1)
sys.path.insert(0,str(R))
from research.src.legacy_ledger import append_correction,CORRECTIONS
import csv
with CORRECTIONS.open(encoding='utf-8',newline='') as f:corrections=list(csv.DictReader(f))
csv_rid='CORR-20261001-P-520-native-id-comment-readback'
if '--reports-only' not in sys.argv and not any(r['revision_id']==csv_rid for r in corrections):
    previous=next(r['new_value'] for r in reversed(corrections) if r['card_id']=='P-520' and r['field']=='comment')
    append_correction({'revision_id':csv_rid,'card_id':'P-520','field':'comment','old_value':previous,'new_value':'Learning-only official6–2 final and L/W/L/W retained. QUERY_CANDIDATE20260927HHLT0 remains NOT_OWNER_CONFIRMED: prior game-list response is HTMLERROR. Actual-start/core/baseline/quorum custody still open. HLR-20261001-P-520-NATIVE-ID-CORRECTION','reason':'Append correction to earlier native-ID custody claim; exact returned old response is an error page, not a native event record. No forecast or grade changes.','source_url':old['original_receipt']['url'],'retrieved_utc':old['original_receipt']['retrieved_utc'],'response_sha256':old['original_receipt']['sha256']})
with CORRECTIONS.open(encoding='utf-8',newline='') as f:corrections=list(csv.DictReader(f))
summary['historical_ledger_correction_fields']=len(corrections)
(A/'legacy_correction_receipt.json').write_text(json.dumps({'correction_ids':[r['revision_id'] for r in corrections],'count':len(corrections),'immutable_base_ledger_sha256':next(x['sha256'] for x in I['snapshots'] if x['path']=='research/SETTLED_OUTCOMES_LEDGER.csv'),'corrections_sha256':sha(CORRECTIONS.read_bytes()),'scope':'LEARNING_ONLY; NO_IDENTITY_OR_ELIGIBILITY_CHANGE'},indent=2)+'\n')
(A/'SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
inv_path=A/'initial_and_final_inventory.csv'
with inv_path.open(encoding='utf-8',newline='') as f:inv=list(csv.DictReader(f))
for row in inv:
    if row['card_id']=='P-520':
        row['native_event_id']='QUERY_CANDIDATE 20260927HHLT0; NOT_OWNER_CONFIRMED'
        note='Native owner-issued match ID still required: old POST game-list body is an HTML error, and the review URL is a shell. '
        if not row['remaining_gaps'].startswith(note):row['remaining_gaps']=note+row['remaining_gaps']
with inv_path.open('w',encoding='utf-8',newline='') as f:w=csv.DictWriter(f,fieldnames=list(inv[0]));w.writeheader();w.writerows(inv)
fields=json.loads((A/'owner_field_readbacks.json').read_text());fields['P520_KBO']['native_game_id']='QUERY_CANDIDATE 20260927HHLT0; NOT_OWNER_CONFIRMED';fields['P520_KBO']['game_id_basis']='Prior GameList body is HTML ERROR, not gameId evidence. Scoreboard exact date/teams/venue/final only; owner-native-ID binding not recovered.'
(A/'owner_field_readbacks.json').write_text(json.dumps(fields,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
notice='''
## Final readback correction — KBO native-ID custody

The earlier October 1 statement that KBO game ID `20260927HHLT0` was bound by retained request metadata is superseded. Readback of the actual retained `GetKboGameList` response (SHA `5f0a6c5e5345456410fcbc723872f67c673463b7446516ba35cfccdcd7b7c277`, retrieved 2026-09-30T08:35:42.562149+00:00) shows an HTML error page, with no returned game ID. The review route is also a shell; its query parameter is a candidate, not owner-confirmed identity. Require a returned field-owner game ID and certified actual-start evidence before closing those gaps. The official September 27 Sajik scoreboard still supports Hanwha 6–2 Lotte and the diagnostic L/W/L/W threshold grades; probabilities, ranks and scores are unchanged.

Correction revision: `HLR-20261001-P-520-NATIVE-ID-CORRECTION`. The original 116 review revisions remain unchanged; the separate learning chain now contains 117 revisions for 116 unique reviewed identities. No canonical settlement revision or prospective admission is created. The latest chain head is `{HEAD}`.

The ledger also appends `CORR-20261001-P-520-native-id-comment-readback`, superseding the earlier comment's identity implication. Total historical ledger field revisions are now 50 across the same seven IDs. Diagnostic grades and scores are unchanged.
'''.replace('{HEAD}',summary['diagnostic_revision_head'])
notice_tag='<!-- SETTLEMENT-READBACK-CORRECTION-20261001 -->'
appended=[x['path'] for x in I['snapshots'] if x['path'] in ['prediction logs/PREDICTION_LOG_COMBINED_6.md','GAME_LOG_STATUS_CURRENT.md','P518_P522_RECONCILIATION.md','LEARNING_REGISTER.md','LEARNINGS_INDEX.md','CHANGELOG.md'] or x['path'].startswith('Mini logs')]
if '--reports-only' in sys.argv:appended=[]
for rel in appended:
    p=R/rel;prefix=(A/'originals'/rel).read_bytes();raw=p.read_bytes();assert raw.startswith(prefix)
    tail=raw[len(prefix):].decode('utf-8')
    # Whitespace repairs only apply to this session's newly authored tail.
    tail='\n'.join(line.rstrip() for line in tail.replace('\r\n','\n').splitlines()).rstrip()+'\n'
    if rel in ['prediction logs/PREDICTION_LOG_COMBINED_6.md','GAME_LOG_STATUS_CURRENT.md','P518_P522_RECONCILIATION.md']:
        if notice_tag in tail:tail=tail.split(notice_tag)[0].rstrip()+'\n'
        tail+='\n'+notice_tag+'\n'+notice.strip()+'\n'
    p.write_bytes(prefix+tail.replace('\n','\r\n').encode('utf-8'))
report_path=A/'REPORT.md';report=report_path.read_text(encoding='utf-8')
report='\n'.join(line.rstrip() for line in report.splitlines()).rstrip()+'\n'
if notice_tag in report:report=report.split(notice_tag)[0].rstrip()+'\n'
report=report.replace('49 / 7; overlaps diagnostic cards','50 / 7; overlaps diagnostic cards')
report+='\n'+notice_tag+'\n'+notice.strip()+'\n'
report_path.write_text(report,encoding='utf-8')
print('Frozen module restored exactly; 7 append prefixes retained; 117 learning revisions including explicit KBO native-ID correction.')
