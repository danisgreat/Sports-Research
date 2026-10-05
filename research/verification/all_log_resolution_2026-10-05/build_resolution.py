"""Create dated all-log corrections and recoverable append evidence; never edit issues."""
from datetime import datetime,timezone
from decimal import Decimal
from pathlib import Path
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).parent
sys.path.insert(0,str(ROOT))
from research.operations.log_card import next_id,research_cards
from research.src.issue import CANONICAL_LEDGER,PART6
from research.src.ledger import read_records
from research.src.eligibility import digest
def sha(raw):return hashlib.sha256(raw).hexdigest()
def load(name):return json.loads((OUT/name).read_text(encoding='utf-8'))
def save(name,obj):
 if (OUT/name).exists():
  if json.loads((OUT/name).read_text(encoding='utf-8'))==json.loads(json.dumps(obj)):return
  raise ValueError('Existing retained output differs: '+name)
 with (OUT/name).open('x',encoding='utf-8') as f:json.dump(obj,f,ensure_ascii=False,indent=2);f.write('\n')
def write(name,text):
 with (OUT/name).open('x',encoding='utf-8') as f:f.write(text.rstrip()+'\n')
DOC_IDS=['P-012','P-013','P-014','P-018','P-035','P-036','P-040','P-060','P-171']
EXPLANATIONS={
 'P-012':'Ranks 3= are an unordered pair, not contradictory grades for one selection: first-25 Under 32.5 WIN at 19, Over LOSS. Both remain PASS/abstention. Do not choose a tie winner or turn these rows into issued picks.',
 'P-013':'The two 2= rows have different thresholds and preserve opposite labels at 20: first-25 Over 30.5 LOSS and Under 40.5 WIN. Rank 4* retains its forced-lower-tier annotation. This is an unordered tie, not a missing fourth contract.',
 'P-014':'Ranks 3= separately preserve Padres +1.5 LOSS and total Over 7.5 LOSS. Arizona 5–1 supplies a four-run margin and six-run total in the retained documentary table. PASS/abstention remains literal; no tied ordering is inferred.',
 'P-018':'Pregame and live tables have different rankings. Keep two versions with four rows each: pregame 1 W,2 L,3 W,4 W; live 1 W,2 W,3 L,4 W. The same rank number across two versions never defines the same trial.',
 'P-035':'V01, V02 and V03 are separate recorded views, joined by version and C-ID. V01 rank 1 H1 Over 84.5 LOSS at 83; V02/V03 rank 1 Q1 Over 42.5 WIN at 45. Preserve all versions and original controlling-role annotations, without selecting the successful version after seeing the result.',
 'P-036':'V01 Twins ML rank 1 LOSS and V02/V03 Phillies ML rank 1 WIN are different recorded versions. Preserve all ten rows with version/C-ID; a rank-only index manufactured the apparent conflict. Final PHI 7–1 MIN is documentary, not new independent terminal custody.',
 'P-040':'Preserve V01–V06, including withdrawn Adelaide −23.5 VOID and the original before-final wording correction. V06 is explicitly marked controlling for Adelaide +23.5 and other side/168.5 rows; V05 controls C05 Under 176.5. V06 rank 1 loses by half a point when Adelaide loses by 24. Do not replace the supplied multi-contract version map with a single outcome-selected order.',
 'P-060':'V01 and late-imported V03 remain separate. V01 rank 1 Yankees +1.5 WIN; V03 rank 1 Under 8.5 WIN. Seven runs can make both Over 6.5 and Under 8.5 WIN, because these thresholds overlap. Different versions and different thresholds are not grade conflicts.',
 'P-171':'Cosmic and Glasgow denote the same side in the preserved exact-event card, and both six-over rows have explicit C-IDs. Retain the detailed checkpoint rows and summary aliases separately: Under 48.5 WIN at 44/2 and Over LOSS. Completed innings 183/5 gives Under 165.5 LOSS and Over WIN. This documentary alias resolution does not produce a new independent final.'}
TERMINALS=[
 dict(id='P-524',event='KT Wiz @ KIA Tigers',native='20261001KTHT0',final='KT 7–5 KIA; normal completed ninth inning',total=12,winner='KT Wiz',
 rows=[(1,'KIA +1.5','L','0.592','0.638','KIA lost by 2: −2 + 1.5 = −0.5'),(2,'KT Wiz ML','W','0.530','0.471','KT won by 2'),(3,'Under 8.5 runs','L','0.527','0.509','12 > 8.5'),(4,'Over 8.5 runs','W','0.473','0.491','12 > 8.5')],
 right='The KT winner view succeeded. Its preserved starter/season advantage was directionally compatible with the result, although it cannot quantify why this particular game was won. The two-run final defeats the KIA cushion even though KIA briefly tied the game.',
 wrong='Rank 1 KIA +1.5 lost by only half a run relative to its adjusted line; rank 3 Under 8.5 lost with twelve runs. The total mean 8.80 already exceeded 8.5, while the card assigned Under 0.527: without a validated distribution the mean alone cannot justify that exact tail probability.',
 mechanism='Owner box: So Hyeong-jun completed six innings with two runs allowed; Yang Hyeon-jong left after 3⅓ with four allowed. The seventh-inning Kim Tae-gun three-run homer made the total ten; the eighth-inning Kim Hyun-soo two-run homer established the two-run final margin. These play facts explain the grade boundaries, without estimating counterfactual probabilities.',
 kill='The named low-walk/starter-quality route did not prevent later scoring. The retained facts support both starter-shortening and multi-run relief branches. They do not establish an estimated weather effect or prove that the qualitative run prevention thesis was generally invalid.',
 process='The card was explicitly observed after play began and imported as historical uncalibrated research. Literal p/baselines remain unvalidated, not certified. No field-owner final can repair missing pre-issue calibration or produce an earlier freeze.',
 hypothesis='For future KBO totals, compare a preregistered starter-plus-relief model against the unchanged baseline with date-held-out Brier/log loss, calibration and interval coverage. Audit available bullpen workload before issue; retain failures and missing workload rather than applying a postgame coefficient.'),
 dict(id='P-525',event='Chunichi Dragons @ Hiroshima Toyo Carp, Game 25',native='20261001-c-d-25',final='Hiroshima 5–1 Chunichi; nine innings, bottom ninth not required',total=6,winner='Hiroshima',
 rows=[(1,'Carp +1.5','W',None,None,'Hiroshima won by 4'),(2,'Over 6.5 runs','L',None,None,'6 < 6.5'),(3,'Under 6.5 runs','W',None,None,'6 < 6.5'),(4,'Dragons +1.5','L',None,None,'Chunichi lost by 4: −4 + 1.5 = −2.5')],
 right='The dated live rank-1 Carp cushion and Hiroshima winner were correct. The original unranked NO_FORECAST intake remains separate from that later qualitative view. This is an after-start observation, not a successful reconstructed pregame forecast.',
 wrong='Rank 2 Over 6.5 lost by half a run. At the retained 4–1/top-seventh observation, the Over needed at least two more runs; only one further Hiroshima run arrived. The opposing Under succeeded, but its success does not retrospectively make it the issued preferred direction.',
 mechanism='The owner linescore is Chunichi 000000100 and Hiroshima 00200210x. Tokoda completed nine innings; the sole visiting run came in the seventh. The bottom-seventh home run in the scorebook adds only one run to the five-run observed total. No shortened-game or extra-innings branch is needed to explain the final six.',
 kill='The live assessment acknowledged that two further runs would defeat Under, but the corresponding Over failure branch was at most one further run. Remaining opportunities do not by themselves establish a high chance of two runs; uncertainty about relief availability was already documented and cannot be filled with hindsight.',
 process='The original source had no numerical probabilities or baseline. The later qualitative ranking remains p/baseline NOT_ESTIMATED. Owner records minute-precision start 18:00 JST and end 20:12 JST, recovered now; these are not contemporaneous issue-time receipts and do not convert the live view into pregame eligibility.',
 hypothesis='For future live NPB totals, preregister exact inning/outs/base state and a remaining-runs distribution. Evaluate a held-out live-state baseline at the same observation horizon, without copying final state into inputs; require calibrated uncertainty and phase-correct coverage before attaching probabilities.'),
 dict(id='P-526',event='Hanwha Eagles @ Samsung Lions',native='20261001HHSS0',final='Samsung 3–2 Hanwha; normal completed top ninth, bottom ninth unnecessary',total=5,winner='Samsung Lions',
 rows=[(1,'Under 11.5 runs','W',None,None,'5 < 11.5'),(2,'Samsung −0.5','W',None,None,'Samsung won by 1'),(3,'Hanwha +2.5','W',None,None,'Hanwha lost by 1: −1 + 2.5 = +1.5'),(4,'Over 11.5 runs','L',None,None,'5 < 11.5')],
 right='Preferred Under and Samsung side/winner succeeded. Hanwha +2.5 also won because a one-run Samsung win satisfies both side propositions; three successful rows are not three independent decisions.',
 wrong='The least-preferred opposing Over lost; that is compatible with the analyst ordering, not an avoided actionable loss. The original uncertainty about ranks 1–2 stays. No numerical separation, calibration claim or perfect-process claim follows from three winning rows.',
 mechanism='Owner pitching tables: Hwang 4⅓ innings/one run and Won five innings/one run. Samsung scored a fifth-inning solo homer and a seventh-inning two-run homer; Hanwha reduced the gap in the eighth. Five combined runs leave 6.5 runs of clearance below the Under threshold. A high pitch count did not become a high-run final.',
 kill='The recorded Under danger was walks, early starter exits and relief blow-ups. Both starters stopped before six full innings, yet their short outings allowed only one run each. Four Hwang walks in the owner table are not proof the named scoring cascade occurred. This distinguishes exposure to a risk from realization of its full kill path.',
 process='The analysis and final refresh were explicitly live, at 0–0 in the third. Original p/baseline NOT_ESTIMATED remains correct. Later confirmed orders, final innings and narratives cannot be backdated into the original live evidence packet or certify an earlier issue.',
 hypothesis='Evaluate the proposed KBO starter/command/relief features prospectively at a frozen live or pregame horizon. Score one representative per decision group, include both wins and losses, and require held-out improvement beyond uncertainty before changing the existing ranking method.'),
 dict(id='P-492',event='San Diego Padres @ Los Angeles Dodgers',native='823897',final='Dodgers 7–0 Padres; nine innings, bottom ninth not played',total=7,winner='Los Angeles Dodgers',
 rows=[(1,'Michael King 15+ pitching outs / Over 14.5 outs','L',None,None,'Owner player 650633: 12 outs, 4.0 IP; 12 < 14.5'),(2,'Padres +1.5','L',None,None,'SD lost by 7: −7 + 1.5 = −5.5'),(3,'Dodgers ML','W',None,None,'Dodgers won 7–0'),(4,'Combined Total Over 8.5 runs','L',None,None,'7 < 8.5')],
 right='The original Dodgers potential-winner view and rank-3 moneyline were correct. The full original table is already retained in Part 5; the historical index pointed only to a merged summary and missed that custody. No new card or extra P-number is justified.',
 wrong='Rank-1 King outs, rank-2 Padres cushion and rank-4 full-game Over lost. The originally selected total is full-game Over 8.5, not a first-five contract. A carried requirement to recover a missing first-five forecast was therefore an audit misattribution; no F5 row is added to this card.',
 mechanism='Fresh owner feed 823897 has Final, away SD 0/home LAD 7 and player ID650633 with outs=12, inningsPitched=4.0, 81 pitches and five runs allowed. The first five completed innings total five runs, but that is an ancillary endpoint only. It does not replace the original full-game target.',
 kill='The original card treated contact/run risk as affecting runs much more than ability to reach the fifth. Five runs and 81 pitches in four innings show that the two risks can share a removal pathway. King workload and Padres close-margin support therefore shared a driver; both top rows lost when it failed.',
 process='The source explicitly reports 12:13 AEST verification after scheduled 12:10 and pregame state unverified. No p/baseline was attached. The retrieved owner pitching line now closes the documentary REVIEW-P490-PROP-BOX gap, while listed-pitcher/operator action, historical issue-time custody and audited certification remain separate.',
 hypothesis='Preregister a pitcher-outs model with removal-risk and lineup-strength features, evaluate held-out outs-distribution coverage and exact-contract Brier against the frozen baseline, and group related side/outs exposures. Do not infer a new coefficient or decision threshold from this single failure.')]

def main():
 old=load('historical_inventory.json');oldmap={r['canonical_id']:r for r in old}
 prior=json.loads((ROOT/'research/verification/settlement_2026-10-01/source_recovery_v2.json').read_text(encoding='utf-8'))
 doc=[]
 for cid in DOC_IDS:
  references=prior['cards'][cid]['references'];unique=[];seen=set()
  for ref in references:
   key=(ref['retained_path'],ref['line'])
   if key in seen:continue
   seen.add(key);path=ROOT/ref['retained_path'];raw=path.read_bytes();line=raw.decode('utf-8-sig').splitlines()[ref['line']-1]
   if sha(raw)!=ref['file_sha256'] or line!=ref['line_literal'] or sha(line.encode())!=ref['line_sha256']:raise ValueError('Historical source mismatch: '+cid)
   unique.append(ref)
  doc.append(dict(canonical_id=cid,event=oldmap[cid]['event'],status='DOCUMENTARY_MAPPING_REPAIRED_NOT_RECERTIFIED',
   explanation=EXPLANATIONS[cid],source_rows=unique,performance_eligible=False,
   prior_retrospective='research/verification/settlement_2026-10-01/REPORT.md'))
 # Bind recovered P-492 original ranks, not its abbreviated merged summary.
 path=ROOT/'prediction logs/PREDICTION_LOG_COMBINED_5.md';raw=path.read_bytes();lines=raw.decode('utf-8-sig').splitlines()
 start=next(i for i,s in enumerate(lines) if s.startswith('### Original supplied research card for P-492'))
 rows=[dict(retained_path=path.relative_to(ROOT).as_posix(),file_sha256=sha(raw),line=i+1,line_literal=s,line_sha256=sha(s.encode())) for i,s in enumerate(lines) if start<i<start+40 and re.match(r'^\| \*\*#\d',s)]
 assert len(rows)==4
 doc.append(dict(canonical_id='P-492',event=oldmap['P-492']['event'],status='DOCUMENTARY_MAPPING_REPAIRED_NOT_RECERTIFIED',
  explanation='The complete Part-5 original table has four exact full-game/outs selections. No first-five forecast exists in this table. Native MLB feed 823897 now retains King 12 outs as well as the final. The older summary-only rank pointer and prop-body gap are repaired.',source_rows=rows,performance_eligible=False,prior_retrospective='prediction logs/PREDICTION_LOG_COMBINED_5.md'))
 save('documentary_repairs.json',doc)
 sources=load('source_refresh.json')['results']+load('source_followups.json')['results']+load('additional_sources.json')
 source_map={r['key']:r for r in sources}
 # Validate the actual retained terminal payloads before producing any grade.
 games=source_map['kbo_ajax_games']['data']['game']
 for cid,gid,away,home in [('P-524','20261001KTHT0',7,5),('P-526','20261001HHSS0',2,3)]:
  g=next(g for g in games if g['G_ID']==gid)
  assert g['GAME_STATE_SC']=='3' and g['GAME_RESULT_CK']==1 and g['CANCEL_SC_ID']=='0'
  assert (int(g['T_SCORE_CN']),int(g['B_SCORE_CN']))==(away,home)
  save(cid+'_terminal_owner.json',g)
 mlb=json.loads((ROOT/source_map['mlb_p492']['receipt']['body_path']).read_bytes())
 assert mlb['gamePk']==823897 and mlb['gameData']['status']['abstractGameState']=='Final'
 assert mlb['liveData']['boxscore']['teams']['away']['players']['ID650633']['stats']['pitching']['outs']==12
 assert mlb['liveData']['linescore']['teams']['home']['runs']==7 and mlb['liveData']['linescore']['teams']['away']['runs']==0
 npb=(ROOT/source_map['npb_final']['receipt']['body_path']).read_text(encoding='utf-8')
 assert '2026年10月1日' in npb and '試合終了' in npb and '25回戦' in npb
 from bs4 import BeautifulSoup
 table=BeautifulSoup(npb,'html.parser')
 # Exact owner rows, including inning total/H/E, are captured for reproducible review.
 npb_rows=[[c.get_text(' ',strip=True) for c in tr.find_all(['th','td'])] for tr in table.find_all('tr')]
 save('P-525_owner_table_rows.json',npb_rows)
 assert any(row[-3:]==['1','5','0'] for row in npb_rows) and any(row[-3:]==['5','9','0'] for row in npb_rows)
 save('new_sporting_settlements.json',TERMINALS)
 recent=load('recent_canonical_carryover_snapshot.json');research={c['card_id']:c for c in research_cards(read_records(CANONICAL_LEDGER))}
 aliases={
  'TMP-20260922-WNBA-DAL-PHX':'P-487','TMP-WNBA':'P-487','TMP-20260923-WNBA-ATL-NYL':'P-484',
  'TMP-20260923-NFL-NYG-LAR':'P-485','TMP-20260923-MLB-MIN-SF':'P-486','TMP-20260923-WTA-WOLFF-OLI':'P-488',
  'TMP-20260923-KBO-KIA-DOO':'P-493','TMP-20260923-WTA-SGP-ANDREEVA-SASNOVICH':'P-494',
  'TMP-20260923-WTA-SGP-ANDREEVA-SASNOVICH-LIVE':'P-494','TMP-20260923-NBL-CNS-TAS':'P-517',
  'TMP-NBL-CNS-TAS':'P-517','TMP-NBL':'P-517','TMP-20260923-NPB-CHU-DB-G25':'P-516','TMP-G25':'P-516',
  'TMP-CANON-20260911-01':'P-358','TMP-SETTLED-20260911-01':'P-374','TMP-RECON-20260912-01':'P-374'}
 aliases.update({r['tracking_handle']:r['canonical_id'] for r in recent})
 for stamp,pairs in [('20260909',['P-341-C03','P-342-C03','P-126','P-148-C02','P-149-C02','P-176-C05','P-178-C05','P-179-C05','P-233','P-234-C03','P-235']),
                     ('20260910',['P-345-C03','P-346-C05','P-355-C05']),
                     ('20260911',['P-368-C02','P-369-C01','P-364']),('20260912',['P-377-C02']),
                     ('20260914',['P-399-C02','P-401-C01','P-401-C03','P-402-C02','P-402-C03','P-406']),
                     ('20260915',['P-407-C01','P-409-C02','P-410-C05','P-418','P-419-C05']),
                     ('20260917',['P-430-C05','P-451'])]:
  for i,target in enumerate(pairs,1):aliases[f'TMP-OPEN-{stamp}-{i:02}']=target
 for i,target in enumerate(['P-250-C05','P-251-C05','P-255-C05','P-256-C05','P-265-C05'],1):aliases[f'TMP-AUDIT-20260912-{i:02}']=target
 occurrences=load('temporary_handle_occurrences.json');seen={r['handle'] for r in occurrences}
 generic={'TMP-20260923','TMP-AUDIT','TMP-OPEN','TMP-SETTLED'}
 assert seen=={h for h in aliases if h.startswith('TMP-')}|generic,(seen-set(aliases)-generic,set(aliases)-seen)
 aliasrows=[]
 for h in sorted(seen):
  evidence=[dict(path=r['path'],line=r['line'],text_sha256=sha(r['text'].encode())) for r in occurrences if r['handle']==h]
  aliasrows.append(dict(handle=h,canonical_target=aliases.get(h),classification='NAMESPACE_OR_GROUP_SHORTHAND' if h in generic else 'EXISTING_CANONICAL_ALIAS_OR_CONTRACT_HANDLE',references=evidence))
 for h,target in aliases.items():
  if not h.startswith('TMP-'):
   card=research[target]
   aliasrows.append(dict(handle=h,canonical_target=target,classification='EXISTING_CANONICAL_LOCAL_TRACKER',references=[dict(path=card['projection_path'],sha256=card['projection_sha256'])]))
 save('alias_reconciliation.json',dict(records=aliasrows,new_distinct_events=0,new_ids=[],next_id=next_id(),
  ordering='No unassigned distinct event remains. Future genuine mini-only imports sort documented original issue/delivery times, with scheduled event time as explicitly labelled fallback; the transactional allocator assigns each ID. Never renumber existing events.'))
 # All genuinely open field/operator cases plus completed-but-uncertified diagnostic cards.
 openold=load('historical_open_review.json');carry=[]
 for r in openold:
  if r['canonical_id'] in DOC_IDS:continue
  cid=r['canonical_id']
  req=r['remaining_gaps']
  if cid=='P-492':req='All four original sporting selections are now diagnosed L/L/W/L and original ranks recovered. No first-five forecast was issued in the recovered table. Remaining: original operator action terms, issue-time/source/baseline certification and independently audited terminal quorum; START_CROSSED remains permanently excluded from pregame metrics.'
  routes=[dict(key=s['key'],status=s.get('status','RETAINED' if s.get('receipt') else 'UNAVAILABLE'),receipt_path=s.get('receipt',{}).get('receipt_path'),error=s.get('error')) for s in sources if cid in s.get('canonical_ids',[])]
  carry.append(dict(canonical_id=cid,event=r['event'],competition='SEE_ORIGINAL_EXACT_COMPETITION: '+r['event'],
   original_scheduled_start='NOT_RECOVERED_IN_THIS_REGISTER; exact retained source must control, never substitute retrieval time',
   current_state='ALL_ORIGINAL_SPORTING_ROWS_DIAGNOSTICALLY_COMPLETE' if cid=='P-492' else r['final_disposition'],
   unresolved_contracts_or_fields=[r['contracts_literal'] or 'Original exact contract field not authenticated',req],remaining_requirement=req,
   canonical_pointer='prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution-2026-10-05',
   source_custody_notes='Original historical text preserved; prior per-event full review and retained literals in research/verification/settlement_2026-10-01/REPORT.md. '+('Recovered original Part-5 rank table and owner prop receipt retained in this dated repair.' if cid=='P-492' else 'Field/source certification limits remain separate from sporting outcomes.'),
   prior_source_location=r['source_location'],tracking_aliases=[h for h,t in aliases.items() if t.split('-C')[0]==cid],
   prior_retrospective='prediction logs/PREDICTION_LOG_COMBINED_5.md' if cid=='P-492' else 'research/verification/settlement_2026-10-01/REPORT.md',
   refreshed_owner_routes=routes,performance_eligible=False))
 for r in recent:
  r=dict(r);cid=r['canonical_id']
  if cid in {'P-524','P-525','P-526'}:
   t=next(t for t in TERMINALS if t['id']==cid)
   r.update(current_state='OWNER_FINAL; ALL_FOUR_SPORTING_ROWS_DIAGNOSTICALLY_COMPLETE',
    remaining_requirement='Original operator/action terms and audited independent terminal collection status remain missing; no new pregame or prospective certification can be inferred from a live/historical import. Original p/baseline and timing labels unchanged.',
    retrospective_pointer='research/verification/all_log_resolution_2026-10-05/REPORT.md')
   r['sporting_diagnostic_grades']=[x[2] for x in t['rows']]
  if cid=='P-537':
   r['remaining_requirement']='First-half field remains contradictory: fresh Sport.kg detailed narrative supports goals 19 and 31 (2–0), but original ESPN display 0–0 disagrees and fresh KFU pages are still pregame. Owner period/timeline, exact corners aggregate for Over 9.5, original operator definitions and audited independent terminal quorum required. Do not certify either conflicting halftime solely from a final 3–1.'
  if cid=='P-523':r['remaining_requirement']='Existing October-1 diagnostic goal review is retained; undefined corner threshold cannot be graded. Original operator rules, actual-start/issue-time conflict and independently audited terminal quorum remain missing; preserve W/W/L/L goal diagnostics as conditional only.'
  carry.append(r)
 carry.sort(key=lambda r:int(r['canonical_id'][2:]));assert len(carry)==53
 save('carryover.json',dict(schema_version=1,created_utc=datetime.now(timezone.utc).isoformat(),event_count=len(carry),documentary_repairs=len(doc),
  scope='537 canonical/admin/reserved slots inventoried; 53 specific sporting/operator/certification carryovers. Other historical closed entries are not recertified.',records=carry))
 manifestpath='research/verification/all_log_resolution_2026-10-05/carryover.json'
 pointer=dict(schema_version=1,manifest_path=manifestpath,manifest_sha256=sha((OUT/'carryover.json').read_bytes()),report_path='research/verification/all_log_resolution_2026-10-05/REPORT.md')
 with (ROOT/'research/current_settlement_register.json').open('x',encoding='utf-8') as f:json.dump(pointer,f,indent=2);f.write('\n')
 sections=['## All-log resolution — 2026-10-05','',
 '**Local working files are the authority; GitHub main is the publication destination.** SPORTS_ONLY / MARKET_BLIND. This dated append preserves every earlier forecast/source/projection byte. No new event, new ID, certified settlement or performance admission is created.',
 '',f'All six combined logs: 537 canonical/admin/reserved slots accounted for; 71 distinct temporary strings reconciled (67 actual aliases/contract handles, four namespace/group labels). Next from allocator: **{next_id()}**. Ten documentary mappings repaired, four exact sporting reviews appended, 53 event-specific settlement/certification carryovers retained.',
 '', '### Documentary corrections to the October-1 audit','',
 'The old UNRESOLVED_CONTRACT_RANK_MERGE and P-492 rank-custody conclusions are superseded only for these recovered documentary mappings. Their inherited grades remain documentary and performance-ineligible. Original p/q, PASS, tie symbols, version IDs, withdrawn/VOID annotations and controlling roles are not rewritten.', '']
 for d in doc:
  sections+=['#### Documentary repair '+d['canonical_id'], '',d['explanation'],'',
   '| Original source | Line SHA-256 | Exact retained row |','|---|---|---|']
  for r in d['source_rows']:sections.append(f"| {r['retained_path']}:{r['line']} | `{r['line_sha256']}` | {r['line_literal'].replace('|','&#124;')} |")
  sections+=['','The existing full retrospective remains at `'+d['prior_retrospective']+'`; this restores its version/contract association, not independent source truth or numerical skill.','']
 source_roles={
 'P-524':[('kbo_ajax_games','KBO/Sports2i owner final; same collection as schedule and box'),('kbo_box_kt','Owner exact-event box and decisive plays'),('newsis_terminal','Kim Hee-jun / Moon Chae-hyeon original terminal narrative, Daum is a mirror'),('khan_terminal','Kim Eun-jin on-site report/interview, Daum is a mirror')],
 'P-525':[('npb_final','NPB owner finished innings, score, minute-precision start/end'),('nikkan_terminal','Nikkan agreeing detailed scorebook; upstream collection independence unverified'),('carp_report','Club page returned title-only shell; not agreeing terminal evidence')],
 'P-526':[('kbo_ajax_games','KBO/Sports2i owner final; same collection as schedule/box'),('kbo_box_hh','Owner exact-event box and decisive plays'),('newsis_terminal','Original Newsis terminal narrative; mirror not an extra lineage'),('kbo_osen_p526','KBO-hosted separate narrative; original reporting lineage not authenticated by hosting')],
 'P-492':[('mlb_p492','MLB field owner exact event/player/innings; original independent recap pointers preserved in Part 5')]}
 for t in TERMINALS:
  cid=t['id'];sections+=['### Sporting diagnostic and retrospective '+cid+' — '+t['event'],'',
   '#### 1. Exact event, final and endpoint','',f"Native identity `{t['native']}`. **{t['final']}**. Total {t['total']}. Sporting grades are deterministic on the retained official endpoint; operator grades remain UNRESOLVED and performance eligibility false.",'',
   '#### 2. Original selections and ranks','', '| Rank | Original proposition | Original p | Original baseline | Sporting diagnostic | Exact reason |','|---|---|---|---|---|---|']
  for rank,contract,grade,p,b,reason in t['rows']:sections.append(f'| {rank} | {contract} | {p or "NOT_ESTIMATED"} | {b or "NOT_ESTIMATED"} | {grade} | {reason} |')
  sections+=['',f"Potential winner: **{t['winner']} — W**, already represented by the side view; not an additional independent pick.",'',
   '#### 3. What went right','',t['right'],'','#### 4. What went wrong','',t['wrong'],'',
   '#### 5. Observed mechanism','',t['mechanism'],'','#### 6. Named failure paths','',t['kill'],'',
   '#### 7. Process and timing audit','',t['process'],'',
   '#### 8. Source and lineage audit','', '| Retained receipt | Source role |','|---|---|']
  for k,role in source_roles[cid]:
   r=source_map[k];receipt=r.get('receipt',{});sections.append('| `'+receipt.get('receipt_path','UNAVAILABLE')+'` | '+role+' |')
  sections+=['','Multiple endpoints or publishers are not automatically independent collectors. Owner grade fields are verified; three independently audited terminal lineages and issue-time certification are not asserted. Raw restricted narrative/benchmark captures remain local; Git publishes receipts and limited derived facts.','',
   '#### 9. Probability and scoring diagnosis','']
  if cid=='P-524':
   scores=[(Decimal(p)-Decimal(int(g=='W')))**2 for _,_,g,p,_,_ in t['rows']]
   sections+=['Literal unvalidated p gives descriptive sporting-only Brier rows '+', '.join(str(s) for s in scores)+'. These are not certified scores, calibrated probabilities or baseline-skill claims. The mean across four correlated rows is not evidence of independent predictive trials. The inherited baseline values remain literal and unapproved.']
  else:sections+=['p/baseline NOT_ESTIMATED: no Brier, log score, ECE, likelihood contribution or fabricated 0.500 baseline. A qualitative rank cannot be converted into a probability from its grade.']
  sections+=['','#### 10. Dependence and evidence limits','',
   'Opposing totals are one decision family. Cushioned sides can overlap with winner outcomes; rank hit counts are descriptive and shared drivers are retained. Missing operator terms do not become VOID, and missing sporting fields do not become losses. Outcome-consistent stories do not establish causal contribution or general model improvement.','',
   '#### 11. Preregistered improvement candidate','',t['hypothesis']+' Status: **PROPOSED_NOT_TESTED**. No frozen model build or forecast coefficient is changed.','',
   '#### 12. Final disposition and carryover','',
   'All four original sporting rows are now diagnostic; original issue/research bodies, ranks and numerical missingness are unchanged. Formal action/settlement and historical admission remain unresolved where evidence is missing. Current event-specific carryover: `research/verification/all_log_resolution_2026-10-05/carryover.json`. Existing old reviews remain linked, not duplicated as new predictions.','']
 sections+=['### P-537 period evidence correction','',
  'A fresh Sport.kg detailed account again describes goals in the 19th and 31st minutes, consistent with 2–0 at halftime, while the preserved ESPN halftime display is 0–0. The reports also disagree about the scorer/minute of the third goal. KFU owner/news refreshes retain pregame notices rather than an exact final period record. Final 3–1 remains a conditional sporting fact; the first-half conflict and Over 9.5 corners are still UNRESOLVED. No match against the U-20 sides in September is substituted. See source followup receipts and the 53-record carryover.','',
  '### Complete remaining settlement queue','', '| Existing ID | Event | State | Exact remaining requirement |','|---|---|---|---|']
 for r in carry:sections.append('| '+r['canonical_id']+' | '+r['event'].replace('|','/')+' | '+r['current_state'].replace('|','/')+' | '+r['remaining_requirement'].replace('|','/')+' |')
 sections+=['','Closed original mini bodies remain in `archive/mini_logs/originals_2026-10-05/`; original archive verification is preserved. Earlier snapshots are historical, not overwritten to appear current. All legacy terminal no-action/censored/unsettleable closures remain exactly their original administrative disposition.','']
 report='\n'.join(sections)
 projection=('\r\n<!-- BEGIN ALL LOG RESOLUTION 2026-10-05 -->\r\n'+report.replace('\r\n','\n').replace('\n','\r\n')+'\r\n<!-- END ALL LOG RESOLUTION 2026-10-05 -->\r\n').encode()
 with (OUT/'settlement_projection.bin').open('xb') as f:f.write(projection)
 write('REPORT.md','# All-log reconciliation and settlement evidence\n\n'+report)
 write('carryover.md','# Current all-log carryover\n\nThe hash-bound machine-readable register is `carryover.json`. '+str(len(carry))+' event records retain settlement/certification requirements, distinct from the ten repaired documentary mappings.\n\n'+'\n'.join(sections[sections.index('### Complete remaining settlement queue'):]))
 before=PART6.read_bytes();save('append_receipt.json',dict(part6_path=PART6.relative_to(ROOT).as_posix(),before_bytes=len(before),before_sha256=sha(before),projection_bytes=len(projection),projection_sha256=sha(projection),after_bytes=len(before)+len(projection),after_sha256=sha(before+projection),new_ids=[],next_id=next_id()))
 chain=[];previous='0'*64
 for d in doc+TERMINALS:
  cid=d.get('canonical_id',d.get('id'));record=dict(sequence=len(chain)+1,previous_sha256=previous,canonical_id=cid,
   revision_type='DOCUMENTARY_MAPPING' if 'source_rows' in d else 'SPORTING_DIAGNOSTIC',performance_eligible=False,
   payload_sha256=digest(d),projection_sha256=sha(projection),canonical_research_commit_sha256=research.get(cid,{}).get('commit_sha256','LEGACY_NOT_CERTIFIED'),
   original_research_source_sha256=research.get(cid,{}).get('source_sha256','SEE_RETAINED_LEGACY_ROWS'))
  record['record_sha256']=digest(record);previous=record['record_sha256'];chain.append(record)
 with (OUT/'settlement_addenda.jsonl').open('x',encoding='utf-8') as f:
  for r in chain:f.write(json.dumps(r,ensure_ascii=False,sort_keys=True)+'\n')
 # Append exactly once, requiring the saved prefix and pre-append canonical checks.
 assert next_id()=='P-538' and PART6.read_bytes()==before
 with PART6.open('ab') as f:f.write(projection);f.flush();import os;os.fsync(f.fileno())
 assert PART6.read_bytes()==before+projection and next_id()=='P-538'
 print(json.dumps(dict(documentary_repairs=len(doc),new_sporting_reviews=len(TERMINALS),retrospective_sections=48,carryovers=len(carry),new_ids=[],next_id=next_id(),append_bytes=len(projection)),indent=2))
if __name__=='__main__':main()
