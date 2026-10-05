"""Build reproducible research-only outcomes; never creates an ISSUE or certifies it."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,re
from research.src.settle import FinalReceipt,settle
from research.src.sports.base import Contract

ROOT=Path(__file__).resolve().parents[3]
OUT=Path(__file__).resolve().parent
def sha(raw):return hashlib.sha256(raw).hexdigest()
def canonical(value):return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode('utf-8')
def save(name,value):
    (OUT/name).write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
events=json.loads((OUT/'event_review.json').read_text(encoding='utf-8'))
receipts=[x for p in sorted(OUT.glob('collection_receipts*.json')) for x in json.loads(p.read_text(encoding='utf-8'))]
by_name={x['name']:x for x in receipts}
now=datetime.now(timezone.utc)
captures=[]
for p in sorted((ROOT/'research/data/benchmark/reconciliation_2026-10-05').glob('web_*.json')):
    captures.append(dict(path=p.relative_to(ROOT).as_posix(),sha256=sha(p.read_bytes()),bytes=p.stat().st_size,capture_type='WEB_TOOL_EXTRACT_NOT_RAW_HTTP',retrieved_utc='NOT_EXPOSED_BY_TOOL',persisted_utc=datetime.fromtimestamp(p.stat().st_mtime,timezone.utc).isoformat(),parser_id='MANUAL_TOOL_EXTRACT_REVIEW_NOT_REGISTERED',independence='UNKNOWN',quarantined=True))
for r in receipts:
    if r.get('body_path'):
        p=ROOT/r['body_path'];actual=sha(p.read_bytes())
        if actual!=r['response_sha256']:raise ValueError('Source body changed: '+str(p))
        r['body_readback']='HASH_MATCH'
        r['use_limit']='SPORTS_FIELDS_ONLY; source presence is not parser admission, lineage audit or contract certification'
save('source_capture_manifest.json',dict(recorded_utc=now.isoformat(),raw_receipts=receipts,tool_captures=captures,market_usage='SPORTS_ONLY / MARKET_BLIND; market-bearing navigation/fields not used',public_projection='Sports facts, source metadata and hashes only. Mixed tool extracts stay in ignored benchmark quarantine.'))

def load_body(name):return json.loads((ROOT/by_name[name]['body_path']).read_text(encoding='utf-8'))
fields={}
nbl=load_body('nbl_match')['match']
fields['P-532']={k:nbl[k] for k in ['id','match_status','start_time_datetime','current_period','home_score','away_score']}
assert [int(nbl['home_score']),int(nbl['away_score'])]==[84,82]
mlb=load_body('mlb_feed')
fields['P-530']=dict(gamePk=mlb['gamePk'],status=mlb['gameData']['status'],game=mlb['gameData']['game'],linescore=mlb['liveData']['linescore'])
assert mlb['gamePk']==849844 and [mlb['liveData']['linescore']['teams'][s]['runs'] for s in ['home','away']]==[6,2]
nhl=load_body('nhl_box')
fields['P-529']={k:nhl[k] for k in ['id','season','gameType','gameDate','startTimeUTC','gameState','periodDescriptor','gameOutcome']}
fields['P-529']['scores']=[nhl[s]['score'] for s in ['homeTeam','awayTeam']]
assert fields['P-529']['scores']==[3,2] and nhl['season']==20262027
for name,cid,expected in [('wnba_espn','P-531',[94,83]),('soccer_summary','P-537',[3,1])]:
    d=load_body(name);c=d['header']['competitions'][0]
    teams={t['homeAway']:t for t in c['competitors']}
    fields[cid]=dict(provider_event=d['header']['id'],status=c['status'],teams={s:{k:t.get(k) for k in ['id','homeAway','score','linescores']} for s,t in teams.items()})
    assert [int(teams[s]['score']) for s in ['home','away']]==expected
    assert c['status']['type']['completed'] is True
nrl=load_body('nrl_owner')['fixtures'][0]
fields['P-534']={k:v for k,v in nrl.items() if k in ['matchState','matchMode','venue','matchCentreUrl','kickOffTimeLong','clock','homeTeam','awayTeam']}
# Restrict team objects to sporting identity/score fields, excluding nested commercial metadata.
for team in ['homeTeam','awayTeam']:
    fields['P-534'][team]={k:v for k,v in nrl[team].items() if k in ['nickName','name','score','teamId','theme','position']}
assert [nrl[s]['score'] for s in ['homeTeam','awayTeam']]==[19,18]
save('reviewed_owner_provider_fields.json',dict(reviewed_utc=now.isoformat(),parser='MANUAL_SPORTS_FIELD_PROJECTION_NOT_ADMITTED',fields=fields,source_join={cid:[by_name[n] for e in events if e['id']==cid for n in e['receipt_names'] if n in by_name] for cid in fields}))

grades=[]
for e in events:
    event_key=next(x['tracking_handle'] for x in json.loads((OUT/'import_results.json').read_text(encoding='utf-8'))['records'] if x['card_id']==e['id'])
    # This timestamp is a review time and this hash binds DERIVED fields, never an HTTP retrieval claim.
    score_hash=sha(canonical(dict(event_key=event_key,home=e['home'],away=e['away'],score=e['score'],endpoint=e['endpoint'])))
    receipt=FinalReceipt(event_key,'FINAL',*e['score'],e['endpoint'],e['sources'][0][1],now,score_hash,str(e['score']))
    def grade(row,rank=None):
        label,market,side,line,*flags=row
        data=dict(rank=rank,label=label,market=market,side=side,line=line,source_flags=flags,formal_grade='UNRESOLVED',formal_blockers=['UNKNOWN_DEFINITION','NO_THREE_AUDITED_INDEPENDENT_TERMINAL_LINEAGES','NO_CANONICAL_PROSPECTIVE_ISSUE'],performance_eligible=False)
        if market.startswith('UNRESOLVED'):
            data.update(diagnostic_grade=market,diagnostic_scope='NOT_GRADED_MISSING_OR_AMBIGUOUS_FIELD')
        else:
            contract=Contract(event_key,market,side,line,e['endpoint'])
            outcome=settle(contract,receipt)
            data.update(diagnostic_grade=outcome.result,diagnostic_scope=e['endpoint'],deterministic_settlement=outcome.__dict__)
            if market=='SPREAD':data['adjusted_margin']=(e['score'][0]-e['score'][1])*(1 if side=='HOME' else -1)+line
            if market=='TOTAL':data['threshold_difference']=(sum(e['score'])-line)*(1 if side=='OVER' else -1)
        return data
    versions=[]
    for v in e['versions']:
        rows=[grade(row,None if v.get('unranked') else i+1) for i,row in enumerate(v['ranks'])]
        winner=v.get('winner');actual=e['home'] if e['score'][0]>e['score'][1] else e['away'] if e['score'][1]>e['score'][0] else 'DRAW'
        versions.append(dict(source_version=v['name'],original_status=v.get('status','UNCALIBRATED_RESEARCH_ONLY'),unranked=v.get('unranked',False),rows=rows,potential_winner=winner,potential_winner_diagnostic=None if winner is None else 'W' if winner==actual else 'L'))
    grades.append(dict(card_id=e['id'],event_key=event_key,native_id=e['native_id'],score=e['score'],total=sum(e['score']),endpoint=e['endpoint'],status='PARTIALLY_DIAGNOSTICALLY_SETTLED_PERIOD_AND_PROVIDER_OPEN' if e['id']=='P-537' else 'DIAGNOSTICALLY_SETTLED_NOT_CERTIFIED',receipt_semantics='DERIVED_REVIEWED_SPORTS_FIELDS: retrieved_utc in deterministic output is REVIEW_TIME, response_sha256 is DERIVED_FIELD_HASH, not raw HTTP custody or formal certification',versions=versions,extra_rows=[grade(row) for row in e.get('extra_rows',[])],p=None,baseline=None,brier=None,log_loss=None,surprise=None,performance_eligible=False))
save('conditional_diagnostic_grades.json',grades)
audit=[]
for e in events:
    audit.append(dict(card_id=e['id'],native_id=e['native_id'],scheduled_utc=e['scheduled_utc'],actual_start=e['actual_start'],terminal_score=e['score'],endpoint=e['endpoint'],period_scores=e.get('period_scores'),regulation_score=e.get('regulation_score'),innings=e.get('innings'),sources=[dict(label=s[0],url=s[1],lineage_note=s[2],independence='UNKNOWN',terminal_admission='NOT_CERTIFIED') for s in e['sources']],raw_receipts=[by_name[n] for n in e['receipt_names'] if n in by_name],tool_capture_manifest='source_capture_manifest.json',identity_findings=e['identity'],quorum='NOT_ESTABLISHED: published reports do not prove three independent registered terminal collections',operator='UNKNOWN_DEFINITION',certified=False))
save('source_event_audit.json',audit)

headings=[('expectation','Expectation vs reality'),('probability','Issued probability/baseline review'),('identity','Source and identity audit'),('participants','Participant/availability audit'),('occurred','Mechanisms that occurred'),('absent','Mechanisms that did not occur'),('adjustment','Model versus research-adjustment effect'),('paths','Failure-path analysis'),('errors','Error classification'),('hypothesis','Next testable hypothesis')]
text='\n<!-- BEGIN DIAGNOSTIC SETTLEMENT RECONCILIATION 2026-10-05 -->\n## October 5 canonical research settlements and twelve-part retrospectives\n\n'
text+='All eleven retained events now have observed terminal full-game results. Ten have complete conditional sporting grades for their ranked rows; P-537 retains an unresolved first-half and corner field. Every original operator grade remains UNRESOLVED, no event has three audited independent terminal collections, and zero records are certified or performance eligible. Missing cutoff/actual-start evidence is retained. These are historical research imports, including explicit NO_FORECAST/live/late records, not issued predictions. W/L below is a **conditional sporting diagnostic**, never an original ticket or model-performance grade. WNBA scope including overtime is explicitly retained; other full-game assumptions are conditional. NHL regulation is separately 2-2. The duplicate MLB supplied row is not repaired into Under.\n\n'
text+='Authority: MDS-2026.10.01-v7.1 / CR-2026.10.01-I2 / SCV-2026.10.01-v3 at fetched main c730d3de094e4e8ecd12cdbe1776f5f0da1bd7d3; freeze CONTROL_MANIFEST_2026-10-01-5.md. Original forecasts, existing canonical cards and prior October 2 audit are retained. This dated addendum updates outcomes/evidence only; it does not rewrite original ranks, missing probabilities or live/late status. Full source/body hashes and retrieval or explicit missingness are in research/verification/reconciliation_2026-10-05/source_event_audit.json and source_capture_manifest.json. Mixed bodies stay quarantined; SPORTS_ONLY / MARKET_BLIND.\n\n'
text+='| Canonical ID | Event | Home-away final | Original/source R1 | R2 | Current disposition |\n|---|---|---|---|---|---|\n'
for e,g in zip(events,grades):
    rows=g['versions'][0]['rows'];text+=f"| {e['id']} | {e['event']} | {e['score'][0]}-{e['score'][1]} | {rows[0]['label']}: {rows[0]['diagnostic_grade']} | {rows[1]['label']}: {rows[1]['diagnostic_grade']} | {g['status']} |\n"
text+='\nDifferent versions are fully listed below. The stale P-516 mini path named in the attachment is absent; the existing P-523 repository mini and existing Downloads fallback mini are updated in place as reference copies. Next canonical ID is **P-538**. No mini is archived and no new running log is started.\n'
for e,g in zip(events,grades):
    text+=f"\n### Retrospective for {e['id']} — {e['event']}\n\n#### 1. Observed endpoint and result\n\n{e['home']} {e['score'][0]}, {e['away']} {e['score'][1]}; total {sum(e['score'])}, home margin {e['score'][0]-e['score'][1]:+}. Diagnostic endpoint `{e['endpoint']}`. Native identity: `{e['native_id']}`. Status: `{g['status']}`. All formal/operator grades UNRESOLVED; no performance scoring.\n\n"
    if 'regulation_score' in e:text+='Regulation was 2-2; full-game winner includes overtime. No regulation two-way ML grade is invented.\n\n'
    if 'period_scores' in e:text+=f"Period scores: home {e['period_scores']['home']}, away {e['period_scores']['away']}; four-quarter regulation endpoint.\n\n"
    if 'innings' in e:text+=f"Innings: home {e['innings']['home']}; away {e['innings']['away']}; nine innings, no extras.\n\n"
    for v in g['versions']:
        text+=f"**Retained version: {v['source_version']}**. Original status `{v['original_status']}`. Potential winner {v['potential_winner'] or 'NOT_PROJECTED'}: {v['potential_winner_diagnostic'] or 'NO_FORECAST'}.\n\n| Rank/row | Exact retained selection | Diagnostic | Source constraint |\n|---|---|---|---|\n"
        for i,row in enumerate(v['rows']):text+=f"| {'Unranked supplied row '+str(i+1) if v['unranked'] else row['rank']} | {row['label']} | {row['diagnostic_grade']} | {', '.join(row['source_flags']) or ('NO_FORECAST' if 'NO_FORECAST' in v['original_status'] else 'Qualitative; not certified')} |\n"
        text+='\n'
    if g['extra_rows']:
        text+='**Additional supplied rows (not new ranks):**\n\n'
        for row in g['extra_rows']:text+=f"- {row['label']}: {row['diagnostic_grade']}; {', '.join(row['source_flags']) or 'conditional sporting diagnostic only'}.\n"
        text+='\n'
    for i,(key,title) in enumerate(headings,2):text+=f"#### {i}. {title}\n\n{e[key]}\n\n"
    text+='#### 12. What should NOT change\n\nKeep every original forecast literal, source-version rank, missing p/baseline, and research/no-forecast/live/late disposition unchanged. No model weight, probability, cap, availability penalty or ranking rule is updated from this single event. Complementary or gapped rows and multiple versions remain one event cluster; no calibration, predictive skill, ROI or independent-row accuracy claim is made. The proposed hypothesis is prospective only.\n\n'
    text+='**Reviewed source register (not an independence certificate):**\n\n'
    for s in e['sources']:text+=f'- [{s[0]}]({s[1]}): {s[2]}.\n'
    text+='\nThe event audit joins exact body/extract checksums, raw receipt retrieval times and explicit missingness to this ID. Web-tool extracts are not raw HTTP receipts; their persistence time is not relabelled as retrieval. Registered owner receipt membership alone does not certify the operator, actual start or upstream independence.\n'
text+='\n### Carryover and verification boundary\n\nP-537 first-half Over/Under 0.5 remains UNRESOLVED_PERIOD; corners Over 9.5 remains UNRESOLVED_PROVIDER_FIELD. All eleven events retain formal UNKNOWN_DEFINITION/quorum blocks, missing or unadmitted actual starts, and performance ineligibility. P-528 is no longer unplayed. P-531 now has an owner final corroboration, but the earlier provisional audit remains immutable. Source-schema/custody, freeze, archive and pinned model-build failures present at opening are recorded separately; no regenerated manifest conceals them. Exact current check outcomes are in the dated REPORT.md.\n\n<!-- END DIAGNOSTIC SETTLEMENT RECONCILIATION 2026-10-05 -->\n'
(OUT/'settlement_addendum.md').write_text(text,encoding='utf-8')
save('build_receipt.json',dict(built_utc=now.isoformat(),events=11,retrospective_sections=132,source_manifest_sha256=sha((OUT/'source_capture_manifest.json').read_bytes()),event_audit_sha256=sha((OUT/'source_event_audit.json').read_bytes()),grades_sha256=sha((OUT/'conditional_diagnostic_grades.json').read_bytes()),projection_lf_sha256=sha(text.encode()),certified=0,performance_eligible=0))
print('Built eleven diagnostic settlements and 132 retrospective sections; no certified issues.')
