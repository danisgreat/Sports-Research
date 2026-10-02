"""Retain exact evidence joins and conditional arithmetic; no certification."""
import hashlib, json, re
from pathlib import Path
from datetime import datetime, timezone
import numpy as np
from research.src.emit_card import _outcome
from research.src.sports.base import Contract
from research.operations.verify_custody import compatible_body
from research.src.issue import _custody, PART6
from research.src.ledger import read_records, committed_issues

ROOT=Path(__file__).resolve().parents[3]; OUT=Path(__file__).resolve().parent
def sha(b): return hashlib.sha256(b).hexdigest()
def put(n,v): (OUT/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
stamp=datetime.now(timezone.utc).isoformat()
web=[]
for p in sorted((ROOT/'research/data/benchmark/mini_settlement_2026-10-02').glob('web_tool_*.json')):
    raw=p.read_bytes(); v=json.loads(raw)
    web.append(dict(path=p.relative_to(ROOT).as_posix(),sha256=sha(raw),bytes=len(raw),
        kind='WEB_TOOL_EXTRACT_NOT_RAW_HTTP',original_retrieved_utc=v['original_retrieved_utc'],
        capture_persisted_utc=v['capture_persisted_utc'],market_quarantined=True,
        urls=sorted(set(re.findall(r'https?://[^\s)\"<>]+',str(v['tool_result']))))))
put('web_extract_manifest.json',dict(observed_utc=stamp,files=web,limitation='Hash proves retained tool extract; not original HTTP bytes, pregame availability, event truth or independent collection.'))
receipt_results=[]
for p in sorted((ROOT/'research/data/source_receipts').glob('*.json')):
    try:
        raw=compatible_body(json.loads(p.read_text(encoding='utf-8')),ROOT)
        receipt_results.append(dict(path=p.relative_to(ROOT).as_posix(),valid=True,bytes=len(raw),sha256=sha(raw)))
    except Exception as ex:
        receipt_results.append(dict(path=p.relative_to(ROOT).as_posix(),valid=False,error=type(ex).__name__+': '+str(ex)))
put('source_body_validation.json',dict(observed_utc=stamp,total=len(receipt_results),failed=sum(not r['valid'] for r in receipt_results),receipts=receipt_results))
manifest=json.loads((ROOT/'research/custody/implementation_2026-10-01/manifest.json').read_text())
gaps=[]
for r in manifest['files']:
    p=ROOT/'research/custody/implementation_2026-10-01'/r['path']
    if not p.exists(): gaps.append(dict(path=r['path'],problem='MISSING_RETAINED_SNAPSHOT'))
    elif sha(p.read_bytes())!=r['sha256']: gaps.append(dict(path=r['path'],problem='HASH_CHANGED'))
put('implementation_snapshot_gaps.json',dict(observed_utc=stamp,files=len(manifest['files']),gaps=gaps))
feed_path=next((ROOT/'research/data/raw/source_snapshots').glob('mlb_official_20261002T034828*.body'))
feed=json.loads(feed_path.read_bytes()); gd=feed['gameData']; live=feed['liveData']; ls=live['linescore']
assert feed['gamePk']==849844 and gd['game']['season']=='2026'
assert gd['teams']['home']['id']==144 and gd['teams']['away']['id']==143
assert gd['status']['detailedState']=='Final'
mlb=dict(native_id=feed['gamePk'],game=gd['game'],datetime=gd['datetime'],status=gd['status'],
    venue=gd['venue'],linescore=ls,boxscore={},first_plate_appearance_start=live['plays']['allPlays'][0]['about']['startTime'],
    first_pitch_candidate=None,actual_start_audit='NOT_ADMITTED; FIRST_PLAY_NOT_SUBSTITUTED',
    scoring_plays=[live['plays']['allPlays'][i]['result'] for i in live['plays']['scoringPlays']])
for play in live['plays']['allPlays']:
    for event in play['playEvents']:
        if event.get('isPitch'):
            mlb['first_pitch_candidate']={k:event.get(k) for k in ['startTime','endTime','isPitch','index']};break
    if mlb['first_pitch_candidate']:break
for side in ['home','away']:
    bx=live['boxscore']['teams'][side]
    starters=sorted([p for p in bx['players'].values() if p.get('battingOrder','').endswith('00')],key=lambda p:int(p['battingOrder']))
    mlb['boxscore'][side]=dict(team=bx['team'],teamStats=bx['teamStats'],
        starting_order=[dict(name=p['person']['fullName'],battingOrder=p['battingOrder'],position=p['position']) for p in starters],
        pitchers=[dict(name=bx['players']['ID'+str(i)]['person']['fullName'],stats=bx['players']['ID'+str(i)]['stats']['pitching']) for i in bx['pitchers']])
put('mlb_owner_fields.json',mlb)
# These are explicitly conditional interpretations of missing contracts, not reconstructions.
events=[('P-527',102,98,[('TOTAL','UNDER',174.5),('SPREAD','HOME',4.5),('SPREAD','AWAY',-4.5),('TOTAL','OVER',174.5)],'FULL_GAME_INTERPRETATION_ONLY',None),
    ('P-529',3,2,[('ML','HOME',None),('SPREAD','AWAY',1.5),('TOTAL','OVER',5.5),('TOTAL','UNDER',5.5)],'INCL_OT_INTERPRETATION_ONLY',{'home':2,'away':2}),
    ('P-530',6,2,[('SPREAD','HOME',1.5),('TOTAL','OVER',7.5),('ML','HOME',None),('ML','AWAY',None)],'FULL_GAME_INTERPRETATION_ONLY',None),
    ('P-531',94,83,[('SPREAD','AWAY',4.5),('TOTAL','OVER',181.5),('TOTAL','UNDER',181.5),('SPREAD','HOME',-4.5)],'ORIGINAL_RESEARCH_FULL_GAME_INCL_OT',None)]
results=[]
for pid,h,a,rows,scope,reg in events:
    grades=[]
    for rank,(market,side,line) in enumerate(rows,1):
        c=Contract(pid,market,side,line,scope)
        w,p=_outcome(np.array([h]),np.array([a]),c)
        value=(h-a if side=='HOME' else a-h)+line if market=='SPREAD' else h+a if market=='TOTAL' else h-a if side=='HOME' else a-h
        grades.append(dict(rank=rank,market=market,side=side,line=line,observed_value=value,
            diagnostic_grade='P' if bool(p[0]) else 'W' if bool(w[0]) else 'L',
            formal_grade='UNRESOLVED',formal_reason='ORIGINAL_OPERATOR_DEFINITION_NOT_RETAINED',
            p_model=None,p_card=None,baseline=None,q=None,Brier=None,log_loss=None))
    results.append(dict(local_reservation=pid,canonical_id=None,home_score=h,away_score=a,total=h+a,
        home_margin=h-a,endpoint_assessment=scope,regulation=reg,grades=grades,
        performance_eligible=False,certified=False,probability_state='NOT_ESTIMATED' if pid=='P-531' else 'NOT_RETAINED_IN_SUMMARY'))
put('conditional_diagnostic_grades.json',dict(observed_utc=stamp,arithmetic_engine='research.src.emit_card._outcome',
    warning='_outcome only supplies arithmetic. Contract metadata is an explicit postgame interpretation; no issuer settlement or admission.',events=results,
    carryover=[dict(local_reservation='P-528',status='UNRESOLVED_NOT_TERMINAL',scheduled_utc='2026-10-02T23:00:00Z',all_four_grades='UNRESOLVED')]))
_custody(PART6); records=read_records(ROOT/'research/canonical_ledger.jsonl')
put('independent_custody_readback.json',dict(observed_utc=stamp,canonical_chain_records=len(records),
    certified_issues=len(committed_issues(records)),part6_original_bytes=141740,part6_original_sha256='c4d497bf339010eae2ff5df23a2d76290983585671666e74791618342565cf30'))
print(json.dumps(dict(web_extracts=len(web),source_receipts=len(receipt_results),receipt_failures=sum(not r['valid'] for r in receipt_results),snapshot_gaps=len(gaps),diagnostic_events=len(results))))
