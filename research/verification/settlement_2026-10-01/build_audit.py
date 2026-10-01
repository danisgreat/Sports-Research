"""Reproduce the October 1 learning audit from retained original bytes and receipts.

Preparation is read-only with respect to forecast logs. --append performs the
authorized, idempotent diagnostic appends after generating inspectable artifacts.
This program never writes research/canonical_ledger.jsonl or a historical core.
"""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter,defaultdict
from math import log
import json,csv,hashlib,re,sys

A=Path(__file__).resolve().parent;ROOT=A.parents[2]
sys.path.insert(0,str(ROOT));sys.path.insert(0,str(A))
from review_facts import FACTS,SPECIAL,COLLISIONS,COMMON_GAP
from research.src.sources import verified_body
from html.parser import HTMLParser
class SportsText(HTMLParser):
    def __init__(self):super().__init__();self.out=[];self.ignore=0
    def handle_starttag(self,tag,attrs):
        if tag in ('script','style'):self.ignore+=1
    def handle_endtag(self,tag):
        if tag in ('script','style'):self.ignore=max(0,self.ignore-1)
    def handle_data(self,value):
        if not self.ignore and value.strip():self.out.append(value.strip())

def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode('utf-8')
def dump(name,obj): (A/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False,allow_nan=False)+'\n',encoding='utf-8')
def mdcell(s):return str(s).replace('|','&#124;').replace('\n',' ')
def table(headers,rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','|'+'|'.join('---' for _ in headers)+'|']+['| '+' | '.join(mdcell(v) for v in row)+' |' for row in rows])
def csvout(name,rows,fields=None):
    with (A/name).open('w',encoding='utf-8',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields or list(rows[0]));w.writeheader();w.writerows(rows)

I=json.loads((A/'initial.json').read_text(encoding='utf-8'))
REC=json.loads((A/'source_recovery_v2.json').read_text(encoding='utf-8'))
STAMP=I['created_utc']
snapshots={x['path']:x for x in I['snapshots']}
current={p.stem:json.loads(p.read_text(encoding='utf-8')) for p in sorted((A/'current_receipts').glob('*.json'))}
prior={r['label']:r for r in I['prior_receipts']}
for label,r in current.items():
    if r['status']=='FETCHED':verified_body(r['receipt'],ROOT)
for label,r in prior.items():
    if r['raw_body_verified']:assert sha((ROOT/r['body_path']).read_bytes())==r['original_receipt'].get('sha256',r['original_receipt'].get('response_sha256'))

mini_rel=next(x for x in snapshots if x.startswith('Mini logs') and x.endswith('.md'))
part6='prediction logs/PREDICTION_LOG_COMBINED_6.md'
issue_claims={}
for pid in [f'P-{n}' for n in range(518,523)]:
    text=(A/'originals'/part6).read_text(encoding='utf-8-sig')
    m=re.search(rf'(?m)^### {pid}\b',text);assert m
    later=re.search(r'(?m)^#### Settlement and full retrospective',text[m.end():]);end=m.end()+later.start() if later else len(text)
    claim=text[m.start():end].rstrip()+'\n';dst=A/'issue_text'/f'{pid}.md';dst.parent.mkdir(exist_ok=True);dst.write_text(claim,encoding='utf-8')
    issue_claims[pid]={'path':dst.relative_to(ROOT).as_posix(),'retained_issue_text_sha256':sha(claim.encode()),'canonical_core_sha256':'NOT_RECOVERED','basis':'DERIVED_LITERAL_EXCERPT_OF_UNCHANGED_ORIGINAL; NOT_CERTIFIED_ISSUE_CORE'}
text=(A/'originals'/mini_rel).read_text(encoding='utf-8-sig');m=re.search(r'(?m)^### P-523\b',text);assert m
end=re.search(r'(?m)^## 2\.',text[m.end():]);claim=text[m.start():m.end()+end.start()].rstrip()+'\n'
dst=A/'issue_text/CLAIMED_P-523.md';dst.write_text(claim,encoding='utf-8')
issue_claims['CLAIMED_P-523']={'path':dst.relative_to(ROOT).as_posix(),'retained_issue_text_sha256':sha(claim.encode()),'canonical_core_sha256':'NOT_RECOVERED','basis':'MANUAL_CLAIM_EXCERPT; NO_ISSUE_TRANSACTION'}
dump('issue_text_index.json',issue_claims)

# Exact source fields extracted from retained owner bodies. Skeleton panels are never state evidence.
def raw(label):return verified_body(current[label]['receipt'],ROOT).decode('utf-8','replace')
def sporttext(label):
    parser=SportsText();parser.feed(raw(label));return '\n'.join(parser.out)
fields={}
for label,event in [('P521_ACB',105378),('P522_ACB',105380)]:
    decoded=raw(label).replace('\\"','"')
    marker=f'"initialMatchHeader":{{"matchId":{event}'
    n=decoded.index(marker)+len('"initialMatchHeader":')
    header,_=json.JSONDecoder().raw_decode(decoded[n:]);assert header['status']=='FINALIZED'
    fields[label]={'parser':'ACB_EXACT_INITIAL_MATCH_HEADER_V1','event_header':header,'semantics':'start is scheduled; no actual-start certification'}
for label in ['P255_UEFA_event','P256_UEFA_event']:
    obj=json.loads(raw(label));fields[label]={k:obj[k] for k in ['id','status','seasonYear','kickOffTime','fullTimeAt','score','leg']}
for label in ['P255_UEFA_stats','P256_UEFA_stats']:
    fields[label]=[{'teamId':t['teamId'],'corners':[s['value'] for s in t['statistics'] if s['name']=='corners'],'period':'WHOLE_MATCH; NO_PERIOD_FIELD'} for t in json.loads(raw(label))]
mlb=json.loads(raw('P518_MLB'));fields['P518_MLB']={'gamePk':mlb['gamePk'],'status':mlb['gameData']['status'],'datetime':mlb['gameData']['datetime'],'linescore':mlb['liveData']['linescore'],'actual_start':'NOT_VERIFIED; datetime is schedule and about.startTime is first play'}
fields['P518_MLB']['teams']=mlb['gameData']['teams']
assert mlb['gameData']['teams']['away']['name']=='New York Mets'
assert mlb['gameData']['teams']['home']['name']=='Washington Nationals'
assert fields['P521_ACB']['event_header']['currentHomeScore']==110
assert fields['P521_ACB']['event_header']['currentAwayScore']==104
assert fields['P522_ACB']['event_header']['currentHomeScore']==80
assert fields['P522_ACB']['event_header']['currentAwayScore']==81
assert mlb['liveData']['linescore']['teams']['away']['runs']==7
assert mlb['liveData']['linescore']['teams']['home']['runs']==1
assert 'DFL-MAT-J043GU' in raw('P410_DFL_candidate') and 'FINAL_WHISTLE' in raw('P410_DFL_candidate')
dfldata=sporttext('P410_DFL_candidate');assert 'Corners\n7\n7' in dfldata
fields['P410_DFL_candidate']={'native_event_id':'DFL-MAT-J043GU','status':'FINAL_WHISTLE','corners_home':7,'corners_away':7,'parser':'EXACT_EVENT_HYDRATION_AND_RENDERED_SPORTS_LABEL_V1'}
club=sporttext('P407_ProLeague');assert 'Corners:Club Brugge 9 versus Royal Antwerp FC 4' in club
assert 'FC Bruges 3, Antwerp 1' in club
fields['P407_ProLeague']={'native_event_id':'6fcfe69f-a383-4a47-af15-6687fdbe245c','final':[3,1],'corners':[9,4],'parser':'EXACT_MATCH_PAGE_SPORTS_LABEL_V1','period_limit':'Use explicit halftime final commentary, not inferred elapsed-clock goals'}
kbo=raw('P520_KBO')
for key,value in [('lblAwayTeamScore_1','6'),('lblHomeTeamScore_1','2'),('lblGameState_1','FINAL')]:
    assert re.search(r'id="[^"]*'+key+r'"[^>]*>'+value+r'</span>',kbo)
fields['P520_KBO']={'native_game_id':'20260927HHLT0','date_query':'2026-09-27','home':'LOTTE','away':'HANWHA','away_runs':6,'home_runs':2,'status':'FINAL','parser':'KBO_EXACT_SCOREBOARD_ROW1_V1','game_id_basis':'Retained original GameCenter request metadata; current review URL and same-date/venue/participants corroborate; HTTP review body is a shell'}
for label in ['P523_Diez','P523_Vision']:
    body=sporttext(label)
    assert 'Oriente' in body and 'Strongest' in body
    assert 'primer tiempo' in body and ('1-1' in body or 'igualado a un gol' in body)
    fields[label]={'final':[1,1],'halftime':[1,1],'endpoint_basis':'Full original report explicitly says both goals first half and final draw','goal_minute_conflict':'Ventura26 versus28; preserved and immaterial to 1H grade','parser':'ORIGINAL_REPORT_EXPLICIT_PHASE_NARRATIVE_V1','official_owner':False}
dump('owner_field_readbacks.json',fields)

queue_by_id=defaultdict(list)
for q in I['prior_open_items']:queue_by_id[q[0].split('-C')[0]].append(q)
queue_by_id['P-410'].append(['P-410-C05','Leipzig Over4.5 corners','TMP-OPEN-20260915-03','P410_DFL_candidate','OWNER_RECOVERED','Owner7; unresolved source/start/custody certification'])
for pid in ['P-520','P-521']:queue_by_id[pid].append([pid,'Reserved original card',pid,'P520_KBO' if pid=='P-520' else 'P521_ACB','DIAGNOSTIC_FINAL','No canonical issue or actual-start evidence'])

def disposition(entry):
    pid=entry['card_id'];status=entry.get('status','');rows=I['contracts_by_id'].get(pid,[])
    if pid in FACTS:return 'DIAGNOSTIC_GOAL_ROWS_COMPLETE_CORNER_UNISSUED' if pid=='CLAIMED_P-523' else 'DIAGNOSTIC_ALL_RANKED_ROWS_COMPLETE'
    if pid in SPECIAL:return SPECIAL[pid][0]
    if pid in COLLISIONS:return 'UNRESOLVED_CONTRACT_RANK_MERGE'
    if 'ADMINISTRATIVE' in status or 'NO FORECAST' in status or 'BLOCKED AT ISSUE' in status or 'ALIAS' in status or 'UNUSED' in status or 'No event maps' in status:return 'ADMINISTRATIVE_NO_DISTINCT_ISSUED_TRIAL'
    if pid in queue_by_id:return 'UNRESOLVED_TARGET_FIELD_OR_PROVIDER'
    if any(r['logged_result'] in ('U','L/W','L/V','') and r['contract_literal'] for r in rows):return 'UNRESOLVED_LITERAL_GRADE'
    if pid in I['selected_ids']:return 'DOCUMENTARY_CUSTODY_RECOVERED_CARRY_PRIOR_GRADES'
    return 'CARRIED_CLOSED_OR_ADMINISTRATIVE_NOT_RECERTIFIED'

score_rows=[]
for pid,f in FACTS.items():
    for rank,contract,p,y,value,family in f['rows']:
        if pid=='P-518' and family in ('Mets margin','Nationals margin'):family='Signed margin'
        score_rows.append(dict(card_id=pid,rank=rank,contract=contract,family=family,p_stated_original=p,p_model_original='',p_card_original='',ranking_q_status='RANKING_ONLY_NOT_SCORED',outcome=y,grade='WIN' if y else 'LOSS',endpoint_value=value,diagnostic_brier=(p-y)**2,diagnostic_logloss=-log(p if y else 1-p),performance_eligible=False,grade_scope='LEARNING_ONLY; NO_CERTIFIED_SETTLEMENT',baseline_literal=f.get('baseline',['NOT_RECOVERED']*len(f['rows']))[rank-1],approved_baseline_score='',source_labels=';'.join(f['labels'])))
assert len(score_rows)==34 and len({r['card_id'] for r in score_rows})==8
csvout('diagnostic_contracts.csv',score_rows)
bycard=defaultdict(list)
for row in score_rows:bycard[row['card_id']].append(row)
card_scores=[]
for pid,rows in bycard.items():
    fam=defaultdict(list)
    for r in rows:fam[r['family']].append(r['diagnostic_brier'])
    card_scores.append(dict(card_id=pid,n_rows=len(rows),wins=sum(r['outcome'] for r in rows),losses=sum(not r['outcome'] for r in rows),row_mean_brier=sum(r['diagnostic_brier'] for r in rows)/len(rows),n_target_families=len(fam),family_equal_mean_brier=sum(sum(v)/len(v) for v in fam.values())/len(fam),mean_logloss=sum(r['diagnostic_logloss'] for r in rows)/len(rows),approved_paired_comparators=0,performance_eligible=False))
csvout('diagnostic_card_scores.csv',card_scores)

# All 2,004 historical rows remain immutable and diagnostic-only. This additional
# scoring slice describes existing literal labels without adjudicating their truth.
legacy=I['contracts_by_id'];literal=[]
for pid,rows in legacy.items():
    for row in rows:
        if row['exclusion_reasons'] or row['logged_result'] not in ('W','L') or not row['stated_p']:continue
        p=float(row['stated_p']);y=int(row['logged_result']=='W')
        if 0<=p<=1:literal.append({'card_id':pid,'rank':row['rank'],'p':p,'y':y,'brier':(p-y)**2,'scope':'INHERITED_LITERAL_DIAGNOSTIC_NOT_NEW_SETTLEMENT'})
csvout('inherited_literal_scores.csv',literal)

inventory=[]
for e in I['inventory']:
    pid=e['card_id'];f=FACTS.get(pid,{});contracts=legacy.get(pid,[])
    aliases=[q[2] for q in queue_by_id.get(pid,[])]
    if pid=='CLAIMED_P-523':aliases=['TMP-20261001-BOLCOPA-OPE-STR']
    if pid=='P-492':aliases+=['source claim P-484','retired provisional P-490']
    if pid=='P-148':aliases+=['raw local P-147']
    inventory.append(dict(card_id=pid,claimed_id='P-523' if pid=='CLAIMED_P-523' else pid,canonical_issue_id='',tracking_aliases=';'.join(aliases),event=e.get('event',''),initial_status=e.get('status',''),final_disposition=disposition(e),reviewed=pid in I['selected_ids'] or pid=='CLAIMED_P-523',native_event_id=f.get('native','NOT_RECOVERED_IN_THIS_PASS'),secondary_id_mapping=f.get('secondary','ORIGINAL_LITERAL_ONLY; NOT_AUTHENTICATED'),source_location=e['pointer'],certified_frozen_core_sha256='NOT_RECOVERED; NO_CANONICAL_ISSUE',retained_text_sha256=issue_claims.get(pid,{}).get('retained_issue_text_sha256','SEE_INITIAL_SOURCE_SNAPSHOT'),issue_status='MANUAL_CLAIM' if pid=='CLAIMED_P-523' else next((r['issued_utc'] for r in contracts if r['issued_utc']),'NOT_CERTIFIED; preserve original state literal'),contracts_literal='; '.join(r['contract_literal'] for r in contracts) if contracts else '; '.join(r[1] for r in f.get('rows',[])),remaining_gaps=f.get('gaps',SPECIAL.get(pid,('',COMMON_GAP))[1] if pid not in queue_by_id else ' | '.join(q[5] for q in queue_by_id[pid])+' '+COMMON_GAP),performance_eligible=False))
assert len(inventory)==523 and len({e['card_id'] for e in inventory})==523
csvout('initial_and_final_inventory.csv',inventory)
reviews=[e for e in inventory if e['reviewed']]
assert len(reviews)==116
counts=Counter(e['final_disposition'] for e in reviews)
summary={'created_utc':datetime.now(timezone.utc).isoformat(),'method':'MDS-2026.10.01-v7.0','scoring':'SCV-2026.10.01-v3','initial_register_slots':522,'manual_claims':1,'canonical_issues':0,'reviewed_historical_ids':115,'reviewed_manual_claims':1,'carried_inventory_only':407,'new_certified_fully_settled':0,'diagnostic_ranked_cards':8,'diagnostic_ranked_rows':34,'new_operator_voids':0,'current_disposition_counts':dict(counts),'legacy_literal_score_count':len(literal),'legacy_literal_cards':len({r['card_id'] for r in literal}),'legacy_literal_mean_brier':sum(r['brier'] for r in literal)/len(literal),'diagnostic_row_mean_brier':sum(r['diagnostic_brier'] for r in score_rows)/len(score_rows),'diagnostic_card_equal_mean_brier':sum(r['row_mean_brier'] for r in card_scores)/len(card_scores),'eligible_comparator_pairs':0,'new_canonical_settlement_revisions':0,'verified_recovered_pointer_references':len(REC['references']),'verified_prior_raw_bodies':sum(p['raw_body_verified'] for p in I['prior_receipts']),'current_retrieval_attempts':len(current),'current_retained_raw_bodies':sum(r['status']=='FETCHED' for r in current.values()),'remaining_historical_primary_tasks':35,'additional_retirement_operator_case':'P-136','manual_extra_unissued_corner':'UNRESOLVED_LINE','source_access_failures':sum(r['status']=='UNAVAILABLE' for r in current.values())}

# Fresh official NBL schedule is checked against each unchanged frozen shadow.
nbl=json.loads(raw('NBL_OFFICIAL'));matches={m.get('id',m.get('matchId')):m for m in nbl['matches']}
# Provider uses match_id in this calendar; retain the actual mapping below.
for m in nbl['matches']:
    for v in m.values():
        if isinstance(v,str) and re.fullmatch(r'[0-9a-f-]{36}',v):matches[v]=m
shadow_paths=[ROOT/e['path'] for e in I['snapshots'] if e['path'].startswith('research/shadow/') and e['path'].endswith('.json')]
shadow_paths += [ROOT/e['path'] for e in I['snapshots'] if '/shadows/' in e['path'] and e['path'].endswith('.json')]
shadows=[]
oldgrades=json.loads((ROOT/'research/daily/20261001T021702970997Z/NBL/nbl_shadow_diagnostic_grades.json').read_text())
grade_lookup={g['event_id']:g for g in oldgrades}
for p in shadow_paths:
    s=json.loads(p.read_text())
    if not isinstance(s,dict) or 'event_id' not in s:continue
    eid=s['event_id'];g=grade_lookup.get(eid);m=matches.get(eid)
    assert m is not None
    result={'event_id':eid,'shadow_path':p.relative_to(ROOT).as_posix(),'unchanged_shadow_sha256':sha(p.read_bytes()),'frozen_original':s,'current_owner_record':m,'current_receipt':current['NBL_OFFICIAL']['receipt'],'performance_eligible':False,'canonical_card_id':None,'actual_start':'NOT_CERTIFIED','terminal_quorum':'SINGLE_OWNER_COLLECTION; INDEPENDENCE_UNKNOWN','baseline_status':'NO_NEW_AFTER_RESULT_BASELINE'}
    if g:
        result.update(disposition='MODEL_ONLY_DIAGNOSTIC_GRADE_CARRIED_AND_RECHECKED',final_home=g['final_home'],final_away=g['final_away'],p_home=g['p_home'],brier=g['brier'],logloss=g['logloss'])
        # Exact owner score fields are pinned, reviewed below by readback.
        assert m['phase']=='complete' and m['home_score']==g['final_home'] and m['away_score']==g['final_away']
    else:result['disposition']='FROZEN_MODEL_ONLY_SHADOW; NOT_TERMINAL_AT_AUDIT'
    shadows.append(result)
assert len(shadows)==5
dump('shadow_dispositions.json',shadows)
summary['model_only_shadows']=5;summary['shadow_diagnostic_finals']=2;summary['shadow_future_at_audit']=3
summary['shadow_mean_brier']=sum(g['brier'] for g in oldgrades)/2

source_rows=[]
for label,r in current.items():
    v=r.get('receipt',{});source_rows.append([label,r['status'],r['url'],v.get('retrieved_utc',r.get('attempt_utc','NOT_RECORDED')),v.get('response_sha256',''),v.get('body_path',''),r.get('reason','RETAINED_BYTES; EVENT/FIELD_READBACK_REQUIRED')])
source_md='# October 1 source receipts and limits\n\nRaw bodies were fetched through scoped audit registries. Every new body is quarantined locally because the broad page can contain market/fantasy fields; only sports event fields were inspected. Live admission/source registries remain unchanged and UNKNOWN independence never passes a quorum. A fetched homepage or JS shell is not a final. Failed attempts remain failed.\n\n'+table(['Label','Read status','Exact URL','UTC retrieval','Response SHA-256','Retained body','Limit'],source_rows)+'\n\n## Prior retained observations\n\n'+table(['Label','Verified raw body','Original URL','Original UTC','Body hash','Retained path'],[[r['label'],r['raw_body_verified'],r['original_receipt'].get('url',''),r['original_receipt'].get('retrieved_utc',''),r['original_receipt'].get('sha256',''),r['body_path']] for r in I['prior_receipts']])+'\n'
(A/'SOURCE_RECEIPTS.md').write_text(source_md,encoding='utf-8')

# Append-only diagnostic chain deliberately uses a different schema/file/type
# than the canonical issuance ledger. It cannot confer performance eligibility.
chain=[];prev='0'*64
for e in reviews:
    pid=e['card_id'];payload={'record_identity':pid,'final_disposition':e['final_disposition'],'initial_snapshot_sha256':sha((A/'initial.json').read_bytes()),'source_recovery_sha256':sha((A/'source_recovery_v2.json').read_bytes()),'original_literal_rows':legacy.get(pid,[]),'diagnostic_rows':bycard.get(pid,[]),'issue_text_reference':issue_claims.get(pid),'facts':FACTS.get(pid),'remaining_gaps':e['remaining_gaps'],'performance_eligible':False,'canonical_issue_core_hash':None}
    body={'schema':'historical-learning-revision-1','record_type':'HISTORICAL_DIAGNOSTIC_REVIEW','revision_id':'HLR-20261001-'+pid,'created_utc':STAMP,'previous_revision_sha256':prev,'payload':payload};body['revision_sha256']=sha(canon(body));prev=body['revision_sha256'];chain.append(body)
chain_path=A/'historical_learning_revisions.jsonl'
encoded=b''.join(canon(x)+b'\n' for x in chain)
if chain_path.exists() and b'<!-- SETTLEMENT-AUDIT-20261001 -->' in (ROOT/part6).read_bytes():assert chain_path.read_bytes().startswith(encoded)
elif chain_path.exists():chain_path.write_bytes(encoded) # Unpublished preparation; no append has occurred.
else:chain_path.write_bytes(encoded)
summary['diagnostic_revision_head']=prev;summary['diagnostic_revision_count']=len(chain)
dump('SUMMARY.json',summary)
summary['reviewed_unresolved_row_identity_operator_rank_ids']=sum(n for k,n in counts.items() if k.startswith('UNRESOLVED_'))
summary['historical_ledger_correction_cards']=7;summary['historical_ledger_correction_fields']=49
summary['manual_claim_custody_corrections']=1
dump('SUMMARY.json',summary)

report=['# All-log settlement audit — October 1, 2026','',
'This is a completed evidence audit and append-only learning reconciliation. It does not certify every historical settlement. No canonical live issue exists; no new canonical transaction or prospective credit is manufactured. Historical cores, Parts 1–5, original Part 6 source bytes, rank CSVs, normalized legacy views and frozen shadows stay unchanged. Results supported by exact retained endpoints are recorded as diagnostic outcomes. Every missing field and operator definition remains explicit.','',
f'Authority at opening: MDS-2026.10.01-v7.0 / CR-2026.10.01-I1 / SCV-2026.10.01-v3. Opening custody: `{STAMP}`. The old freeze is retained; a versioned receipt records the authorized log/register appends. No model coefficients, rankings, admissions or numerical forecast cores change.','',
'## Scope, counts and measurement','',
table(['Item','Count / meaning'],[['Historical register slots',522],['Manually claimed mini-log card',1],['Selected historical IDs reviewed',115],['Manual claims reviewed',1],['Inventory-only carried records',407],['New certified fully settled cards',0],['Complete ranked-row diagnostic cards',8],['New/current exact-endpoint diagnostic rows',34],['Corrected historical ledger fields / identities', '49 / 7; overlaps diagnostic cards'],['Manual identity/custody correction',1],['Reviewed IDs retaining specific row/identity/operator/rank blockers',summary['reviewed_unresolved_row_identity_operator_rank_ids']],['New operator VOID decisions',0],['Canonical issue/settlement transactions',0],['Frozen model-only shadows',5],['Shadow finals, separate diagnostics',2],['Future shadows at audit',3]]),'',
'The historical queue contained 35 handles across 34 events: 23 primary result/derivative handles, five documentary/period handles, three reserved final reconciliations and four operator cases. All 35 receive current dispositions. P-136 adds a retirement/operator exception overlooked by the parent settled label. P-518/P-522 get verification of their prior diagnostic corrections. The manual Bolivia claim is a separate unconsumed alias, with four diagnostic goal rows and one unissued unknown corner line. A handle can have resolved sporting arithmetic while its certification work remains open; these counts do not retire handles by silently relaxing the evidence gate.','',
table(['Review disposition','IDs / claims'],sorted(counts.items())),'',
f'Full initial/final census: [initial_and_final_inventory.csv](initial_and_final_inventory.csv), 523 unique identities. Raw opening snapshot: [initial.json](initial.json), 42 retained files. All original 2,004 contracts and their missingness remain in the immutable legacy view; no missing probability or baseline is filled. [source_recovery_v2.json](source_recovery_v2.json) recovers {len(REC["references"])} literal pointer references from 12 sources, including removed files from pinned Git history. A source-line hash proves custody of a statement, not sporting truth.','',
'## Aggregate scores and limits','',
table(['Card / claim','Rows','W–L','Row Brier mean','Target families','Family-equal Brier','Mean log loss'],[[s['card_id'],s['n_rows'],f"{s['wins']}–{s['losses']}",f"{s['row_mean_brier']:.8f}",s['n_target_families'],f"{s['family_equal_mean_brier']:.8f}",f"{s['mean_logloss']:.8f}"] for s in card_scores]),'',
f'The 34-row descriptive mean Brier is {summary["diagnostic_row_mean_brier"]:.8f}; the eight-card equal-weight mean is {summary["diagnostic_card_equal_mean_brier"]:.8f}. These cards span unrelated sports and endpoints, include live/manual issues and dependent/nested/complementary rows, and were selected because of unresolved custody. Neither is a performance claim. Family means group shared target definitions; they do not turn multi-threshold scores into independent trials. Binary Brier=(p−y)²; binary log loss=−ln(p for WIN, 1−p for LOSS). q is never scored. Push/void/censored rows are omitted with explicit disposition, not assigned y=0.','',
f'The separate inherited-literal slice contains {len(literal)} rows across {summary["legacy_literal_cards"]} cards, mean Brier {summary["legacy_literal_mean_brier"]:.8f}, using only already logged W/L, a literal numeric p and no normalized exclusion flag. It is not a refreshed settlement cohort. Its omissions and inherited truth limits are visible in [inherited_literal_scores.csv](inherited_literal_scores.csv). Do not combine it with the eight-card current endpoint slice or the two NBL shadows.','',
'Performance-eligible cohort size: zero. Approved paired comparator count: zero. Parenthesized0.500, missing/register-not-derived rates and card-derived diagnostics never become approved baselines. Numeric original baseline literals are preserved but their custody is not certified, so comparator scores and incremental skill estimates remain blank. No valid identical-event paired baseline/model comparison exists here; a week-cluster interval or skill p-value would misrepresent missing comparators and this selected mixed cohort. No calibration, model qualification or adjustment benefit is claimed.','',
'## Complete initial and final disposition table','',
table(['Identity','Exact original event label','Initial status','Current disposition','Review'],[[e['card_id'],e['event'],e['initial_status'],e['final_disposition'],e['reviewed']] for e in inventory]),'',
'## Every reviewed card: settlement and A–F retrospective','',
'The normalized table is a literal index and may merge conflicting same-rank contracts. The separate historical source rows below preserve those variants instead of choosing a convenient postgame rank. Blank native IDs, start fields, baselines and model artifacts remain unknown. Full issue excerpts for the five reserved cards and the manual claim are retained under `issue_text/` and hashed in `issue_text_index.json`; those derived text hashes are not canonical issue-core receipts.']

for e in reviews:
    pid=e['card_id'];f=FACTS.get(pid);rows=legacy.get(pid,[]);sources=REC['cards'].get(pid,{}).get('references',[])
    report.extend(['',f'### Review: {pid} — {e["event"]}','',f'**Disposition:** `{e["final_disposition"]}`. Revision `HLR-20261001-{pid}`. Canonical issue core hash: NOT_RECOVERED; performance eligible: false.','',
        '**A. What was issued.** '+('The manual mini-log claims four ranked goal rows and one quarantined corner with no line. Its canonical-ID/pregame assertions are disputed, not adopted.' if pid=='CLAIMED_P-523' else 'The retained historical record and row literals follow; a rank-index row is not a certified issue transaction.'),''])
    if pid in issue_claims:report.extend([f'Complete preserved issue-text excerpt: [{pid}](issue_text/{pid}.md), derived text SHA `{issue_claims[pid]["retained_issue_text_sha256"]}`. Original method/manifest/contract/timing/baseline claims in that excerpt are preserved as claims.',''])
    if pid in issue_claims:
        original=(ROOT/issue_claims[pid]['path']).read_text(encoding='utf-8')
        all_lines=original.splitlines();groups=[];group=[]
        for line in all_lines+['']:
            if line.startswith('|'):group.append(line)
            elif group:groups.append(group);group=[]
        # Copy the actual issued rank table literally, including baseline/q,
        # flags, units and preferred sides. Later settlement0.500 tables are
        # outside the retained pre-settlement excerpt.
        issued=[g for g in groups if 'Rank' in g[0] and ('Contract' in g[0] or 'Market' in g[0])]
        if issued:report.extend(['Exact issued ranked table(s), literal transcription:','',*['\n'.join(g)+'\n' for g in issued]])
    if rows:
        report.append(table(['Rank literal','Contract literal','p literal','q literal','Baseline in index','Logged result','Observed value','Exclusion flags'],[[r['rank'],r['contract_literal'],r['stated_p_literal'] or 'MISSING',r['ranking_q_literal'] or 'MISSING',r['baseline_p'] or 'NOT_EXTRACTED; SEE_ORIGINAL',r['logged_result'] or 'MISSING',r['observed_value_literal'] or 'NOT_EXTRACTED',r['exclusion_reasons'] or 'NONE_IN_LITERAL_VIEW'] for r in rows]))
    if sources:
        report.extend(['','Literal historical source rows (unchanged wording, each separately anchored; these are documentary grade/order claims, not new independent finals):','',table(['Pointer','Line SHA-256','Exact source line'],[[r['pointer'],r.get('line_sha256',''),r.get('line_literal',r.get('reason',''))] for r in sources]),''])
    if f:
        report.extend(['','Forecast mechanism / cutoff limits: '+f['mechanism'],'','**B. What happened.** '+f['outcome']+' '+f['period'],'',
            'Native identity: '+f['native']+'. Secondary mapping: '+f['secondary']+'. Terminal state: '+f['state']+'. Source/body receipts: '+', '.join('`'+x+'`' for x in f['labels'])+' in [SOURCE_RECEIPTS.md](SOURCE_RECEIPTS.md). No unverified lineup, weather or injury effect is added.','',
            '**C. Forecast validity.** '+f['gaps']+' '+f.get('correction','No probability, rank or threshold correction is made. Missing approved baselines remain blank.'),'',
            '**D. Predictive assessment.** '+f['assessment'],'','**E. Scoring.** Exact frozen contract arithmetic and diagnostic scores:','',
            table(['Rank','Issued contract','p','Observed endpoint','Diagnostic result','(p−y)²','Log loss','Issued baseline literal'],[[r['rank'],r['contract'],r['p_stated_original'],r['endpoint_value'],r['grade'],f"{r['diagnostic_brier']:.8f}",f"{r['diagnostic_logloss']:.8f}",r['baseline_literal']] for r in bycard[pid]]),'',
            'These p values are historical stated probabilities, not reconstructed p_model/p_card decomposition. Comparators remain unapproved and unscored; q remains ordering only. W/L here is an exact-endpoint learning diagnostic, not canonical settlement.','',
            '**F. Learning.** '+f['learning']+' This is a parked hypothesis, not a coefficient, qualification, active rule or prospective test enrollment. One winning or losing outcome does not establish probability skill.'])
        if pid=='CLAIMED_P-523':report.extend(['','Unissued corner row: `Combined Total Corners: ?` — UNRESOLVED_LINE. Threshold, frozen provider and complete corner endpoint missing. No grade, score, operator settlement or ID is manufactured.'])
    else:
        note=SPECIAL.get(pid,('',None))[1] or (' | '.join(q[5] for q in queue_by_id[pid]) if pid in queue_by_id else None)
        admin=e['final_disposition']=='ADMINISTRATIVE_NO_DISTINCT_ISSUED_TRIAL'
        if not note:note='No distinct issued trial exists; administrative/unused/alias closure remains.' if admin else 'Historical grade source lines are recovered. Existing sporting labels are carried as literal diagnostics; independently collected terminal/phase evidence and genuine issue core are not reconstructed from prose.'
        oldretros=list(dict.fromkeys(r['retrospective_literal'] for r in rows if r['retrospective_literal']))
        report.extend(['','**B. What happened.** '+note,'',
            '**C. Forecast validity.** '+('No forecast was issued under this separate identity; it cannot be enrolled as a loss, void or missing settlement.' if admin else COMMON_GAP)+' Original operator/period terms govern. An endpoint in another phase does not settle this one. '+('Same-rank contract variants remain separately preserved; a merged index is unsuitable for rank/grade inference. Require original issue-table/core and the dated correction that selects a controlling order; do not choose the outcome-favourable variant.' if pid in COLLISIONS else ''),'',
            '**D. Predictive assessment.** '+('No prediction performance is assessable for a no-issue/alias slot.' if admin else 'The recovered original retrospective below is attribution by its original author, not a new causality finding. Without independently retained pre-cutoff model/base/adjustment and lineup/condition artifacts, numerical contribution and ordinary-variance versus model-miss classification remain INCONCLUSIVE. Source/contract/custody limits above are observed process defects; unavailable outcome fields are censoring, not negative outcomes.'),''])
        if oldretros:report.extend(['Original card assessment literal(s), preserved for both wins and losses:','',*['> '+t.replace('\n','\n> ') for t in oldretros],''])
        report.extend(['**E. Scoring.** '+('NOT_APPLICABLE: no issued trial.' if admin else 'No newly verified numeric score is admitted for this review. Missing p/baseline stays missing; contradictory merged grades, unknown operator rules, terminal censoring and no-action rows are not losses. Any inherited literal-grade score appears only in the separately labelled inherited slice, never prospective totals.'),'',
            '**F. Learning.** '+('Count issue transactions/events rather than numbering slots; hypothesis: an immutable identity census reduces duplicate/no-issue enrollment to zero.' if admin else ('Hypothesis: storing original ties/contract IDs separately from rank indices eliminates false same-rank result conflicts; check zero merged mutually exclusive contracts before any ranking analysis.' if pid in COLLISIONS else 'Hypothesis: exact event, provider and period tags plus a frozen action/void definition reduce this documented missing-field failure; require that endpoint and original issue receipt before admitting a comparable new trial.'))+' Parked only. Postgame explanations are never retroactive input features. Remaining evidence: '+e['remaining_gaps']])

report.extend(['','## Shadow records — separate A–F reviews','',
    'Five frozen model-only records are inventoried. The two September30 finals retain their already recorded diagnostics and are rechecked against the newly retained official schedule. The three October1/2 fixtures remain future at the audit observation (~07:32Z). No event not yet terminal is scored; no retrospective model run creates a forecast. The later TAS/MEL tipoff at09:30Z is not waited on or guessed.'])
for s in shadows:
    frozen=s['frozen_original'];p=frozen.get('p_model_home_ml',frozen.get('p_home'))
    report.extend(['',f'### Shadow review: {s["event_id"]}','',
      '**A. Issued object.** NO_CARD_ISSUED / MODEL_ONLY_SHADOW. Frozen JSON `'+s['shadow_path']+'`, raw SHA `'+s['unchanged_shadow_sha256']+'`; complete original probability/distribution/input/build/time fields in [shadow_dispositions.json](shadow_dispositions.json).','',
      '**B. Outcome.** '+(f'Owner final home{s["final_home"]}–away{s["final_away"]}. Native calendar row and exact receipt retained.' if 'brier' in s else 'No terminal result at the audit observation; upcoming frozen shadow retained.'),'',
      '**C. Validity.** No canonical issue; single owner collection; actual start and independent terminal quorum absent. Original shadow bytes remain unchanged. Baseline/comparator missingness preserved.','',
      '**D. Assessment.** '+('The winning home direction is compatible with the model but two results cannot estimate calibration or skill. No manual research adjustment was frozen.' if 'brier' in s else 'Future outcome and mechanism realization remain unknown; no speculative retrospective.'),'',
      '**E. Scores.** '+(f'Original homep={s["p_home"]}; binaryBrier={s["brier"]:.10f}, logloss={s["logloss"]:.10f}; learning-only. No after-result comparator.' if 'brier' in s else 'No outcome => no Brier/logloss. This is not an unresolved issued card.'),'',
      '**F. Learning.** Preserve chronological frozen shadows and exact official endpoint receipts. Hypothesis: a cohort meeting the registered duration, sample and independent-custody gates can support a paired calibration test; these five records do not meet it.'])
report.extend(['','## Revision receipts and readback','',
f'This pass writes {len(chain)} historical-learning revisions, final diagnostic chain head `{prev}`, in [historical_learning_revisions.jsonl](historical_learning_revisions.jsonl). Every revision binds initial snapshot/source recovery, copied original literal rows, diagnostic outcomes and remaining gaps. The distinct schema is not the canonical issuer ledger. Canonical settlement revisions: zero because canonical issues: zero.','',
'[SOURCE_RECEIPTS.md](SOURCE_RECEIPTS.md) records exact URLs, raw hashes, UTC times, body paths and failure reasons. [owner_field_readbacks.json](owner_field_readbacks.json) keeps exact native owner state/score fields without mistaking page skeletons or scheduled times for actual start. Raw source bodies under `research/data/benchmark/` are local quarantined artifacts and remain ignored by Git. A portable copy lacking them must report unavailable body validation.','',
'Reproduction: run `py -3.14 -X utf8 -B research/verification/settlement_2026-10-01/build_audit.py`; generation uses retained sources only and does not refetch or rewrite issue cores. [review_facts.py](review_facts.py) contains explicit human-reviewed event interpretations; [audit_checks.ipynb](audit_checks.ipynb) presents the arithmetic/readback checks. Final check output is in [VERIFICATION.json](VERIFICATION.json) once the authorized appends and versioned freeze are verified.'])
report_text='\n'.join(report)+'\n'
(A/'REPORT.md').write_text(report_text,encoding='utf-8')

# Notebook contains only readback and calculation, never log-writing cells.
cells=[{'cell_type':'markdown','metadata':{},'source':['# October 1 diagnostic audit checks\n','All scores are learning-only; this notebook reads retained artifacts and does not issue, fetch or settle a canonical card.']},
 {'cell_type':'code','execution_count':None,'metadata':{},'outputs':[],'source':['from pathlib import Path\n','import csv, json, hashlib, math\n',"audit = Path(r'C:\\Users\\danie\\Desktop\\Sports Research\\research\\verification\\settlement_2026-10-01')\n","rows = list(csv.DictReader((audit/'diagnostic_contracts.csv').open(encoding='utf-8')))\n","assert len(rows) == 34\n","for r in rows:\n","    p, y = float(r['p_model_original']), int(r['outcome'])\n","    assert abs((p-y)**2 - float(r['diagnostic_brier'])) < 1e-12\n","    assert abs(-math.log(p if y else 1-p)-float(r['diagnostic_logloss'])) < 1e-12\n","    assert r['performance_eligible'] == 'False'\n","print('34 exact-row diagnostic scores checked; no eligible rows')\n"]},
 {'cell_type':'code','execution_count':None,'metadata':{},'outputs':[],'source':["canon = lambda v: json.dumps(v, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode()\n","prev = '0'*64\n","for line in (audit/'historical_learning_revisions.jsonl').read_text(encoding='utf-8').splitlines():\n","    r=json.loads(line); digest=r.pop('revision_sha256')\n","    assert r['previous_revision_sha256']==prev\n","    assert hashlib.sha256(canon(r)).hexdigest()==digest\n","    assert r['payload']['performance_eligible'] is False\n","    prev=digest\n","print('Diagnostic chain valid:', prev)\n"]}]
dump('audit_checks.ipynb',{'cells':cells,'metadata':{'kernelspec':{'display_name':'Python3','language':'python','name':'python3'}},'nbformat':4,'nbformat_minor':5})
notebook=json.loads((A/'audit_checks.ipynb').read_text())
for cell in notebook['cells']:
    cell['source']=[s.replace("r['p_model_original']","r['p_stated_original']") for s in cell['source']]
dump('audit_checks.ipynb',notebook)

if '--append' in sys.argv:
    from research.src.legacy_ledger import append_correction,CORRECTION_FIELDS,OUTPUT,CORRECTIONS
    with OUTPUT.open(encoding='utf-8',newline='') as f:base={r['card_id']:r for r in csv.DictReader(f)}
    with CORRECTIONS.open(encoding='utf-8',newline='') as f:oldcorr=list(csv.DictReader(f))
    seen={r['revision_id'] for r in oldcorr}
    correction_ids=[]
    for sc in card_scores:
        pid=sc['card_id']
        if pid=='CLAIMED_P-523':continue
        source=next(current[label]['receipt'] for label in FACTS[pid]['labels'] if label in current and current[label]['status']=='FETCHED')
        changes={'record_status':'HISTORICAL_DIAGNOSTIC_ALL_RANKED_ROWS_COMPLETE_NOT_CERTIFIED','mean_brier_p':f"{sc['row_mean_brier']:.8f}",'n_rows_with_p':str(sc['n_rows']),'n_ranked_rows_graded':str(sc['n_rows']),'wins':str(sc['wins']),'losses':str(sc['losses']),'comment':'October1 learning-only exact endpoint readback; core/start/quorum/baseline custody remains uncertified. HLR-20261001-'+pid}
        for field,value in changes.items():
            rid='CORR-20261001-'+pid+'-'+field;correction_ids.append(rid)
            if rid in seen:continue
            current_value=base[pid][field]
            for revision in oldcorr:
                if revision['card_id']==pid and revision['field']==field:current_value=revision['new_value']
            c=dict(revision_id=rid,card_id=pid,field=field,old_value=current_value,new_value=value,reason='User-authorized learning-only diagnostic settlement; literal probabilities and ranks preserved; '+FACTS[pid].get('correction','New exact owner endpoint readback'),source_url=source['source_url'],retrieved_utc=source['retrieved_utc'],response_sha256=source['response_sha256'])
            assert set(c)==set(CORRECTION_FIELDS);append_correction(c);oldcorr.append(c);seen.add(rid)
    dump('legacy_correction_receipt.json',{'correction_ids':correction_ids,'count':len(correction_ids),'immutable_base_ledger_sha256':snapshots['research/SETTLED_OUTCOMES_LEDGER.csv']['sha256'],'corrections_sha256':sha(CORRECTIONS.read_bytes()),'scope':'LEARNING_ONLY; NO_IDENTITY_OR_ELIGIBILITY_CHANGE'})
    tag='<!-- SETTLEMENT-AUDIT-20261001 -->'
    link_targets=['initial_and_final_inventory.csv','initial.json','source_recovery_v2.json','inherited_literal_scores.csv','SOURCE_RECEIPTS.md','shadow_dispositions.json','historical_learning_revisions.jsonl','owner_field_readbacks.json','review_facts.py','audit_checks.ipynb','VERIFICATION.json']+[x['path'].split('/settlement_2026-10-01/',1)[1] for x in issue_claims.values()]
    def project(body):
        for rel in link_targets:body=body.replace(']('+rel+')',']('+str(A/rel).replace('\\','/')+')')
        return body
    def append_once(rel,body):
        p=ROOT/rel;original=(A/'originals'/rel).read_bytes();present=p.read_bytes()
        if tag.encode() in present:return
        assert present==original,'Concurrent changes: '+rel
        payload=('\n\n'+tag+'\n'+project(body)+'\n').replace('\r\n','\n').replace('\n','\r\n').encode('utf-8')
        with p.open('ab') as f:f.write(payload)
        assert p.read_bytes().startswith(original)
    # Full A-F reviews are mirrored in the running Part6 append, including manual
    # claim heading prefixed Review: so canonical ID detection cannot consume523.
    append_once(part6,report_text.replace('# All-log settlement audit','## All-log settlement audit',1))
    append_once(mini_rel,'## Current diagnostic reconciliation — October1\n\nThe inherited empty-intake header contradicts the retained manual card. ClaimedP523 is MANUAL_CLAIM with TMP-20261001-BOLCOPA-OPE-STR, no canonical issue transaction. Canonical nextID remainsP523; earlier nextP524 assertion is superseded. No silent renumbering. Four goal rows diagnosticW/W/L/L; no canonical certification. Corners? remains UNRESOLVED_LINE and unissued. Full evidence, exact original row arithmetic and A–F review are in the Part6 October1 appendix and `research/verification/settlement_2026-10-01/REPORT.md`.\n\n'+report_text[report_text.index('### Review: CLAIMED_P-523'):report_text.index('## Shadow records')])
    status_body='## Current all-log audit disposition — October1,2026\n\nThis dated append supersedes older queue summaries only for the dispositions listed here. No original row is rewritten. Historical label FINAL/SETTLED is not recertification. P518–P522 remain reserved; canonicalP523 remains unconsumed despite a manual mini-log claim. Certified new settlements0; complete ranked-row diagnosticcards8,rows34; new operatorVOID0. Full523identity inventory and116card/claimA–F reviews: `research/verification/settlement_2026-10-01/REPORT.md`.\n\n'+table(['Reviewed identity (not a new canonical row)','Current disposition','Remaining evidence'],[[f'`{e["card_id"]}`',e['final_disposition'],e['remaining_gaps']] for e in reviews])+'\n\nAll35 inherited handles remain explicit certification/operator tasks; add retirement/operatorP136. The manual corner line is unissued. Source-line pointer recoveries are documentary closure only. Score/comparator eligibility remains false for every historical/manual record and shadow. Canonical settlement revisions0; separate diagnostic chain head `'+prev+'`. Full raw-body/score/core readback receipt is linked in the report.'
    append_once('GAME_LOG_STATUS_CURRENT.md',status_body)
    reserved='## October1 reserved-card diagnostic update\n\nAllfiveP518–P522 remain reserved and performance-ineligible. No canonical import or transaction is manufactured. Current owner final readbacks and exact frozen probabilities give the following learning diagnostics. Baselines retain the original table above and their provenance limits.\n\n'+table(['Reserved identity','Exact final','Ranks','Mean Brier(p)','Revision','Certification gaps'],[[pid,FACTS[pid]['outcome'],'/'.join(r['grade'] for r in bycard[pid]),f"{next(s for s in card_scores if s['card_id']==pid)['row_mean_brier']:.8f}",'HLR-20261001-'+pid,FACTS[pid]['gaps']] for pid in [f'P-{n}' for n in range(518,523)]])+'\n\nKBO gameId20260927HHLT0 is now bound by retained original request metadata and exact final reports; the old stable-ID-not-preserved label is superseded as a sporting identity gap only. Actual-start/cutoff, core and baseline custody are still open. P519owner ID8942 andP522ID105380 control their wrong-event working citations. See the Part6October1append and full audit report.'
    append_once('P518_P522_RECONCILIATION.md',reserved)
    lessons=[('OBS-20261001-AUDIT-01','Source and period','P407/P410/P255/P256','Exact owner fields can resolve arithmetic while independence/start/period custody stays open.','Check exact native event/period/provider tags; require zero endpoint substitutions.'),('OBS-20261001-AUDIT-02','Arithmetic and dependence','P520/manualP523','Signed adjustments, printed Normal marginals and top-two joint probabilities do not reconcile in the retained cards.','Compare frozen scalar/grid/joint outputs with analytic reconstruction before any qualified future issue.'),('OBS-20261001-AUDIT-03','Baselines and timing','P518–P522/manualP523','Unapproved numeric diagnostics and parenthesized0.500 were presented as settlement baselines; schedule crossing and canonical claims are unreconciled.','Require approved exact baseline artifacts and issue transaction before cohort enrollment.'),('OBS-20261001-AUDIT-04','Ranks and administration','Nine same-rank merged cards;P136/P445','Merged rank variants, unknown retirement rules and conditional no-action slots create false performance trials.','Preserve original row IDs/ties/operator terms and reject duplicate/no-issue enrollment.'),('OBS-20261001-AUDIT-05','Mechanism validation','P519/P520/P521/P522','Winning cushion or short-leash realization does not prove calibration or the causal adjustment.','Freeze paired model-only and adjusted distributions on identical endpoints, then test an untouched chronological eligible cohort.')]
    lesson_table=table(['ObservationID','Scope','Cases','Observed evidence','Testable follow-up (parked)'],lessons)
    append_once('LEARNING_REGISTER.md','## October1 settlement audit — parked observations\n\nAuthority MDS-2026.10.01-v7.0 / SCV-2026.10.01-v3. Status PARKED_LEARNING_ONLY; no active coefficients, rules, weights, qualification or prospective test enrollment. Eight exact-endpoint diagnostic cards and116card/claim reviews are documented in the Part6 append / `research/verification/settlement_2026-10-01/REPORT.md`. Eligible cohort0 and paired approved comparators0.\n\n'+lesson_table+'\n\nOriginal per-card narratives are retained as source claims. No one-result rule promotion, hindsight model refit or numeric q score follows. Registered chronological testing is required before changing a coefficient.')
    append_once('LEARNINGS_INDEX.md','## October1 settlement audit index\n\nAll entries PARKED_LEARNING_ONLY; full evidence and individual A–F reviews in the matching LEARNING_REGISTER append and audit report.\n\n'+lesson_table)
    append_once('CHANGELOG.md','## 2026-10-01 — all-log settlement and learning reconciliation\n\nInventoried522historical slots plus one manual claim; reviewed115historicalIDs and the manual claim. Added34exact-endpoint diagnostic grades on8cards/claims,455documentarysource-pointer recoveries, five shadow dispositions,49append-only legacy correction fields, and dated status/learning/Part6/mini-log appends. No certified prospective settlement, operatorVOID, canonical issue, model coefficient or rank change. Original forecast cores/source bytes/normalized views/shadows remain unchanged. Exact source receipts, unresolved cases and reproducible readback: `research/verification/settlement_2026-10-01/REPORT.md`.')
if (A/'READBACK_CORRECTIONS.json').exists():
    import subprocess
    subprocess.run([sys.executable,'-X','utf8','-B',str(A/'finalize_readback.py'),'--reports-only'],check=True)
    summary=json.loads((A/'SUMMARY.json').read_text())
print(json.dumps(summary,indent=2))
