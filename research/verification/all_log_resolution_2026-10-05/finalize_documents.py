"""Select local authority and the full carryover, preserving historical snapshots."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).parent
def sha(raw):return hashlib.sha256(raw).hexdigest()
def write_json(path,obj):
 with path.open('x',encoding='utf-8') as f:json.dump(obj,f,ensure_ascii=False,indent=2);f.write('\n')
def main():
 old=json.loads((OUT/'carryover.json').read_text(encoding='utf-8'))
 competitions={'P-126':'SFA A Division S-League','P-136':'ATP Winston-Salem Open semifinal','P-148':'Liga MX Femenil Apertura','P-149':'MLS NEXT Pro',
 'P-166':'AIHL Goodall Cup semifinal','P-176':'France Ligue 3','P-178':'France Ligue 3','P-179':'France Ligue 3','P-200':'Danish Metal Ligaen',
 'P-217':'Caribbean Premier League','P-233':'China FA Cup quarterfinal','P-234':'China FA Cup quarterfinal','P-235':'China FA Cup quarterfinal',
 'P-250':'China FA Cup','P-251':'Coppa Italia','P-255':'UEFA Women Champions League','P-256':'UEFA Women Champions League',
 'P-265':'Leagues Cup','P-274':'MLB','P-341':'Uganda Premier League','P-342':'Slovnaft Cup','P-368':'UAE Pro League',
 'P-369':'UAE Pro League; retained competition label requires exact identity confirmation','P-377':'Guatemala Liga Nacional Apertura',
 'P-399':'Serie A','P-401':'Allsvenskan','P-407':'Belgium Jupiler Pro League','P-409':'France Ligue 1','P-410':'German Bundesliga',
 'P-418':'Bhutan Premier League','P-419':'Allsvenskan','P-430':'AFC Champions League Elite','P-492':'MLB',
 'P-518':'MLB','P-519':'AFLW','P-520':'KBO','P-521':'ACB','P-522':'ACB'}
 schedule={'P-126':('PREDICTION_LOG_COMBINED.md',[22039,22040]),'P-136':('PREDICTION_LOG_COMBINED.md',[28434]),
 'P-149':('PREDICTION_LOG_COMBINED.md',[41565]),'P-166':('PREDICTION_LOG_COMBINED.md',[49852]),
 'P-176':('PREDICTION_LOG_COMBINED.md',[52458]),'P-178':('PREDICTION_LOG_COMBINED.md',[53036]),'P-179':('PREDICTION_LOG_COMBINED.md',[53384]),
 'P-200':('PREDICTION_LOG_COMBINED.md',[59086]),'P-250':('PREDICTION_LOG_COMBINED.md',[68606]),'P-251':('PREDICTION_LOG_COMBINED.md',[68742]),
 'P-255':('PREDICTION_LOG_COMBINED.md',[69971]),'P-256':('PREDICTION_LOG_COMBINED.md',[70263]),'P-265':('PREDICTION_LOG_COMBINED.md',[73304]),
 'P-274':('PREDICTION_LOG_COMBINED_2.md',[903]),'P-492':('PREDICTION_LOG_COMBINED_5.md',[10597])}
 for r in old['records']:
  cid=r['canonical_id']
  if cid in competitions:r['competition']=competitions[cid]
  notes=[]
  if cid in schedule:
   name,nums=schedule[cid];path=ROOT/'prediction logs'/name;lines=path.read_text(encoding='utf-8-sig').splitlines()
   notes=[dict(path=path.relative_to(ROOT).as_posix(),line=n,text=lines[n-1],line_sha256=sha(lines[n-1].encode())) for n in nums]
  elif cid in {'P-518','P-519','P-520','P-521','P-522'}:
   path=ROOT/'research/verification/settlement_2026-10-01/issue_text'/(cid+'.md')
   lines=path.read_text(encoding='utf-8-sig').splitlines()
   notes=[dict(path=path.relative_to(ROOT).as_posix(),line=n+1,text=line,line_sha256=sha(line.encode())) for n,line in enumerate(lines)
    if re.search(r'scheduled|scheduled start|start time',line,re.I) and ('2026' in line or 'UTC' in line)]
  if notes:
   r['original_scheduled_start']='VERBATIM_ORIGINAL_SCHEDULE: '+' / '.join(n['text'] for n in notes)
   r['original_schedule_source_lines']=notes
  r['canonical_pointer']='prediction logs/PREDICTION_LOG_COMBINED_6.md#all-log-resolution--2026-10-05'
 old.update(created_utc=datetime.now(timezone.utc).isoformat(),revision='SCHEDULE_AND_COMPETITION_CUSTODY_ENRICHMENT',supersedes_manifest='research/verification/all_log_resolution_2026-10-05/carryover.json',supersedes_sha256=sha((OUT/'carryover.json').read_bytes()))
 write_json(OUT/'carryover_v2.json',old)
 pointer=dict(schema_version=1,manifest_path='research/verification/all_log_resolution_2026-10-05/carryover_v2.json',manifest_sha256=sha((OUT/'carryover_v2.json').read_bytes()),report_path='research/verification/all_log_resolution_2026-10-05/REPORT.md')
 (ROOT/'research/current_settlement_register.json').write_text(json.dumps(pointer,indent=2)+'\n',encoding='utf-8')
 events=json.loads((OUT/'new_sporting_settlements.json').read_text(encoding='utf-8'))
 proposals=dict(source_review_path='research/verification/all_log_resolution_2026-10-05/new_sporting_settlements.json',source_review_sha256=sha((OUT/'new_sporting_settlements.json').read_bytes()),records=[dict(proposal_id='RIP-20261005-ALLLOG-'+e['id'],canonical_id=e['id'],hypothesis_and_acceptance=e['hypothesis'],source_text_sha256=sha(e['hypothesis'].encode()),status='PROPOSED_NOT_TESTED',performance_eligible=False) for e in events])
 write_json(OUT/'improvement_proposals.json',proposals)
 path=ROOT/'research/improvement_register.json';reg=json.loads(path.read_text(encoding='utf-8'))
 reg['additional_review_registers']=[dict(path='research/verification/all_log_resolution_2026-10-05/improvement_proposals.json',sha256=sha((OUT/'improvement_proposals.json').read_bytes()),proposals=4,status='PROPOSED_NOT_TESTED')]
 path.write_text(json.dumps(reg,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 # Append a precise clarification; the first appended projection remains immutable.
 clarification='''\n## All-log resolution — source and schedule clarification, October 5\n\nCurrent selected carryover is `research/verification/all_log_resolution_2026-10-05/carryover_v2.json`, hash-bound by `research/current_settlement_register.json`. It retains the same 53 IDs and adds recovered verbatim schedule pointers and exact competition labels; missing schedules remain explicitly unrecovered. The 71 TMP strings comprise 67 event/contract aliases and four namespace/group labels; LOCAL-P528-GR-CLE-20261002 is one additional already canonical local tracker. No ID is assigned twice.\n\nP-525 wording clarification: the single Hiroshima run in the bottom seventh was a run scored on Nakamura Shosei's RBI single, not a home run. The owner linescore remains 5–1, combined six; all four diagnostic grades are unchanged. The preceding phrase “bottom-seventh home run” meant the home side's run and was ambiguous. The home runs in the owner record were Nakamura's third-inning two-run homer and Sakakura's sixth-inning solo; Chunichi's Hosokawa homered in the seventh.\n\nFour additional retrospective hypotheses are retained in `research/verification/all_log_resolution_2026-10-05/improvement_proposals.json`, linked by `research/improvement_register.json`. All 15 original-plus-new suggestions remain PROPOSED_NOT_TESTED; no retrospective result is promoted into a model change.\n'''
 raw=clarification.replace('\n','\r\n').encode();before=(ROOT/'prediction logs/PREDICTION_LOG_COMBINED_6.md').read_bytes()
 with (OUT/'clarification_projection.bin').open('xb') as f:f.write(raw)
 with (ROOT/'prediction logs/PREDICTION_LOG_COMBINED_6.md').open('ab') as f:f.write(raw)
 write_json(OUT/'clarification_append_receipt.json',dict(before_bytes=len(before),before_sha256=sha(before),projection_sha256=sha(raw),after_sha256=sha(before+raw)))
 with (OUT/'REPORT.md').open('a',encoding='utf-8') as f:f.write(clarification)
 current_note='**Local authority and all-log reconciliation (October 5):** Local working files govern; GitHub main publishes them. The latest user instruction supersedes earlier GitHub-only prompts. Current [all-log evidence](research/verification/all_log_resolution_2026-10-05/REPORT.md) accounts for all 537 slots and temporary aliases, ten repaired documentary mappings, four new sporting reviews and 53 precise carryovers. Existing IDs and frozen forecast/source bytes remain unchanged.'
 docs=set(json.loads((ROOT/'research/verification/implementation_2026-10-05/document_changes.json').read_text())['files'][i]['path'] for i in range(len(json.loads((ROOT/'research/verification/implementation_2026-10-05/document_changes.json').read_text())['files'])))
 docs|={'METHOD.md','README.md','CURRENT_RULES.md','research/README.md','CONTRIBUTING.md','PROMPTS.md'}
 edits=[]
 for name in sorted(docs):
  if name=='GAME_LOG_STATUS_CURRENT.md':continue
  path=ROOT/name;raw=path.read_bytes();text=raw.decode('utf-8-sig')
  text=text.replace('CR-2026.10.05-I3','CR-2026.10.05-I4')
  if name=='METHOD.md':text=text.replace('CONTROL_MANIFEST_2026-10-05-3.md','CONTROL_MANIFEST_2026-10-05-4.md')
  note=current_note
  if name.startswith('research/'):
   note=note.replace('(research/verification/','(verification/')
  position=text.index('\n')+1
  text=text[:position]+'\n'+note+'\n'+text[position:]
  if name in ['README.md','VERIFICATION_PROTOCOL.md','research/README.md']:
   anchor='py -3.14 -B -m research.operations.verify_reconciliation'
   text=text.replace(anchor,anchor+'\npy -3.14 -B -m research.operations.verify_all_logs',1)
  path.write_bytes(text.replace('\r\n','\n').replace('\n','\r\n').encode('utf-8'))
  edits.append(dict(path=name,before_sha256=sha(raw),after_sha256=sha(path.read_bytes())))
 # Preserve restricted full narrative copies locally; receipt hashes are unchanged.
 exclusions=['newsis_terminal_*','khan_terminal_*','nikkan_terminal_*','sportkg_terminal_*','kbo_osen_p526_*']
 with (ROOT/'.gitignore').open('a',encoding='utf-8') as f:
  f.write('\n# Full publisher narrative captures are local evidence, not redistributed articles.\n')
  for pat in exclusions:f.write('research/data/raw/source_snapshots/'+pat+'\n')
  for label in ['newsis_terminal','khan_terminal','nikkan_terminal','sportkg_terminal','championat_terminal','kbo_home','kbo_schedule','npb_final','uefa_inter','uefa_psg','afc_owner','proleague_event','dfl_event','toluca_report','bhutan_owner','uae_owner','allsvenskan_owner','cfa_owner','kfu_owner','kfu_news','leaguescup_owner','guatemala_owner','carp_report','npb_schedule']:
   f.write('research/verification/all_log_resolution_2026-10-05/'+label+'.txt\n')
 write_json(OUT/'document_changes.json',dict(files=edits,control='CR-2026.10.05-I4',selected_freeze='CONTROL_MANIFEST_2026-10-05-4.md'))
 print('documents',len(edits),'schedule pointers',sum(bool(r.get('original_schedule_source_lines')) for r in old['records']))
if __name__=='__main__':main()
