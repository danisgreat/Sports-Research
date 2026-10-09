"""Verify dated all-log evidence, immutable cores and selected carryover."""
from datetime import datetime,timezone
import hashlib,json,re
from research.operations.log_card import next_id,research_cards,verify_projection
from research.operations.settlement_register import selected
from research.src.issue import PART6,CANONICAL_LEDGER
from research.src.ledger import read_records
from research.src.eligibility import digest
from research.operations.verify_custody import compatible_body
from research.src.custody_text import custody_bytes
ROOT=PART6.parents[1]
OUT=ROOT/'research/verification/all_log_resolution_2026-10-05'
def sha(raw):return hashlib.sha256(raw).hexdigest()
def load(name):return json.loads((OUT/name).read_text(encoding='utf-8'))
def need(ok,msg):
 if not ok:raise ValueError(msg)
def run():
 raw=PART6.read_bytes();opening=load('opening.json')
 for item in opening['files']:
  path=ROOT/item['path']
  if item['path'].startswith(('prediction logs/','research/issued_research/','research/model_builds/')) or item['path']=='research/canonical_ledger.jsonl':
   body=custody_bytes(path)
   if path==PART6 or item['path']=='research/canonical_ledger.jsonl':body=body[:item['bytes']]
   need(len(body)==item['bytes'] and sha(body)==item['sha256'],'Immutable original changed: '+item['path'])
 for filename,projectionname in [('append_receipt.json','settlement_projection.bin'),('clarification_append_receipt.json','clarification_projection.bin'),('native_append_receipt.json','native_projection.bin')]:
  receipt=load(filename);projection=(OUT/projectionname).read_bytes()
  need(raw.count(projection)==1,'Missing/duplicate append: '+projectionname)
  need(sha(projection)==receipt['projection_sha256'],'Append projection changed')
  need(sha(raw[:receipt['before_bytes']])==receipt['before_sha256'],'Pre-append prefix changed')
  need(sha(raw[:receipt['before_bytes']+len(projection)])==receipt['after_sha256'],'Recorded append changed')
 doc=load('documentary_repairs.json');need(len(doc)==10,'Missing documentary repair')
 for d in doc:
  for r in d['source_rows']:
   body=custody_bytes(ROOT/r['retained_path']);line=body.decode('utf-8-sig').splitlines()[r['line']-1]
   need(sha(body)==r['file_sha256'] and line==r['line_literal'] and sha(line.encode())==r['line_sha256'],'Documentary row changed: '+d['canonical_id'])
  need(d['performance_eligible'] is False,'Documentary promoted')
 historical=load('historical_inventory.json')
 need(len(historical)==523 and len({r['canonical_id'] for r in historical})==523,'Historical inventory coverage')
 aliases=load('alias_reconciliation.json')
 need(len(aliases['records'])==72 and aliases['new_distinct_events']==0 and not aliases['new_ids'],'Alias accounting')
 known={r['canonical_id'] for r in historical}|{r['canonical_id'] for r in load('recent_canonical_carryover_snapshot.json')}
 need(len(known)==537,'Duplicate event-slot accounting')
 for r in aliases['records']:
  target=r['canonical_target']
  if target:need(target.split('-C')[0] in known,'Alias invented unknown ID')
 selected_register=selected(ROOT);need(selected_register is not None,'Missing selected settlement register')
 carry=selected_register['manifest'];need(carry['event_count']==len(carry['records']),'Current carryover coverage')
 dated=load('carryover_v3.json');need(dated['event_count']==len(dated['records'])==53,'Dated carryover coverage')
 cards=research_cards(read_records(CANONICAL_LEDGER))
 current_known=known|{c['card_id'] for c in cards}
 for r in carry['records']:
  need(r['canonical_id'] in current_known,'Unknown carryover event')
  for note in r.get('original_schedule_source_lines',[]):
   line=(ROOT/note['path']).read_text(encoding='utf-8-sig').splitlines()[note['line']-1]
   need(line==note['text'] and sha(line.encode())==note['line_sha256'],'Original schedule changed')
 previous='0'*64;payloads={d['canonical_id']:d for d in doc}
 terminal=load('new_sporting_settlements.json')
 terminal_payloads={t['id']:t for t in terminal}
 chain=[json.loads(line) for line in (OUT/'settlement_addenda.jsonl').read_text(encoding='utf-8').splitlines()]
 need(len(chain)==14,'Incomplete dated addenda chain')
 for i,r in enumerate(chain,1):
  need(r['sequence']==i and r['previous_sha256']==previous,'Addenda chain order')
  need(digest({k:v for k,v in r.items() if k!='record_sha256'})==r['record_sha256'],'Addenda hash')
  obj=payloads[r['canonical_id']] if r['revision_type']=='DOCUMENTARY_MAPPING' else terminal_payloads[r['canonical_id']]
  need(digest(obj)==r['payload_sha256'] and r['performance_eligible'] is False,'Addenda payload/admission changed')
  previous=r['record_sha256']
 for t in terminal:
  need(len(t['rows'])==4 and [r[0] for r in t['rows']]==[1,2,3,4],'Exact new ranked slate incomplete')
 for name in ['source_refresh.json','source_followups.json']:
  for r in load(name)['results']:
   if r.get('receipt'):compatible_body(r['receipt'],ROOT)
 for r in load('additional_sources.json'):
  if r.get('receipt'):compatible_body(r['receipt'],ROOT)
 native=load('P-520_native_owner.json')
 native_games=json.loads(compatible_body(native['receipt'],ROOT))['game']
 game=next(g for g in native_games if g['G_ID']=='20260927HHLT0')
 need(game==native['game'] and game['AWAY_ID']=='HH' and game['HOME_ID']=='LT','P-520 owner identity')
 need(game['GAME_STATE_SC']=='3' and game['GAME_RESULT_CK']==1 and game['CANCEL_SC_ID']=='0' and (game['T_SCORE_CN'],game['B_SCORE_CN'])==('6','2'),'P-520 owner final')
 # Required new sporting fields are re-extracted from the retained owner bodies.
 follow=load('source_followups.json')['results'];sources={r['key']:r for r in follow}
 games=json.loads((ROOT/sources['kbo_ajax_games']['receipt']['body_path']).read_bytes())['game']
 for gid,away,home in [('20261001KTHT0',7,5),('20261001HHSS0',2,3)]:
  g=next(g for g in games if g['G_ID']==gid)
  need(g['GAME_STATE_SC']=='3' and g['GAME_RESULT_CK']==1 and g['CANCEL_SC_ID']=='0','KBO terminal state')
  need((int(g['T_SCORE_CN']),int(g['B_SCORE_CN']))==(away,home),'KBO owner final')
 mlb_receipt=next(r['receipt'] for r in load('additional_sources.json') if r['key']=='mlb_p492')
 mlb=json.loads(compatible_body(mlb_receipt,ROOT))
 need(mlb['gamePk']==823897 and mlb['gameData']['status']['abstractGameState']=='Final','MLB exact terminal')
 need(mlb['liveData']['boxscore']['teams']['away']['players']['ID650633']['stats']['pitching']['outs']==12,'Pitcher outs')
 npb_rows=load('P-525_owner_table_rows.json')
 need(any(r[-3:]==['1','5','0'] for r in npb_rows) and any(r[-3:]==['5','9','0'] for r in npb_rows),'NPB exact owner totals')
 proposals=load('improvement_proposals.json');need(len(proposals['records'])==4,'New proposals incomplete')
 need(proposals['source_review_sha256']==sha((OUT/'new_sporting_settlements.json').read_bytes()),'Proposal source changed')
 for p in proposals['records']:
  t=terminal_payloads[p['canonical_id']]
  need(p['hypothesis_and_acceptance']==t['hypothesis'] and p['source_text_sha256']==sha(t['hypothesis'].encode()),'Proposal text changed')
  need(p['status']=='PROPOSED_NOT_TESTED' and p['performance_eligible'] is False,'Untested proposal promoted')
 registry=json.loads((ROOT/'research/improvement_register.json').read_text(encoding='utf-8'))
 need(any(r['sha256']==sha((OUT/'improvement_proposals.json').read_bytes()) for r in registry['additional_review_registers']),'Proposal register unbound')
 cards=research_cards(read_records(CANONICAL_LEDGER))
 for card in cards:verify_projection(card,PART6)
 following=next_id()
 queue=(ROOT/'GAME_LOG_STATUS_CURRENT.md').read_text(encoding='utf-8-sig').split('<!-- END CURRENT RESEARCH QUEUE -->')[0]
 need(selected_register['manifest_path'] in queue and f'Next canonical ID: {following}' in queue,'Current queue stale')
 projection=(OUT/'settlement_projection.bin').read_bytes()
 need(len(re.findall(rb'(?m)^#### (?:[1-9]|1[0-2])\.',projection))==48,'New twelve-part reviews incomplete')
 return dict(passed=True,observed_utc=datetime.now(timezone.utc).isoformat(),historical_slots=537,temporary_strings=71,
  local_trackers=1,documentary_repairs=10,new_sporting_reviews=4,new_retrospective_sections=48,
  current_carryovers=selected_register['manifest']['event_count'],dated_carryovers=53,new_ids=[],next_id=following,
  original_forecasts_ledger_and_projection_bytes_preserved=True,limitation='Custody and deterministic diagnostics; no historical or prospective certification is inferred.')
if __name__=='__main__':
 try:result=run()
 except (ValueError,OSError,KeyError,TypeError,StopIteration,IndexError) as exc:result=dict(passed=False,error=f'{type(exc).__name__}: {exc}')
 print(json.dumps(result,indent=2));raise SystemExit(not result['passed'])
