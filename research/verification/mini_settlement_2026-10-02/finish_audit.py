"""Final readback, source index, and report after mandatory command completion."""
import hashlib,json,subprocess,sys
from pathlib import Path
from datetime import datetime,timezone
from importlib.metadata import version
from collections import Counter
from research.src.eligibility import digest,canonical_bytes
from research.src.issue import _custody,PART6
from research.operations.log_card import next_id

ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parent
def sha(b):return hashlib.sha256(b).hexdigest()
def put(n,v):(OUT/n).write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
opening=json.loads((OUT/'opening_custody.json').read_text());append=json.loads((OUT/'append_receipt.json').read_text())
mini=Path(append['mini_path']);original=(OUT/'original_mini_evidence.txt').read_bytes();add=(OUT/'settlement_addendum.txt').read_bytes()
assert mini.read_bytes()==original+add
assert sha(mini.read_bytes())==append['final_sha256']
unchanged=[]
for ref in opening['files']:
    assert sha((ROOT/ref['path']).read_bytes())==ref['sha256'],ref['path']
    unchanged.append(ref['path'])
_custody(PART6);assert next_id()=='P-527'
previous='0'*64; revisions=[]
for line in (OUT/'diagnostic_revisions.jsonl').read_bytes().splitlines():
    record=json.loads(line);body={k:v for k,v in record.items() if k!='record_sha256'}
    assert record['previous_sha256']==previous and digest(body)==record['record_sha256'] and canonical_bytes(record)==line
    assert record['original_mini_sha256']==sha(original) and record['addendum_sha256']==sha(add)
    for ref in record['source_refs']:assert sha((OUT/ref['path']).read_bytes())==ref['sha256']
    revisions.append(record);previous=record['record_sha256']
assert len(revisions)==4 and previous==append['diagnostic_chain_head']
commands=json.loads((OUT/'post_append/command_results.json').read_text())
assert len(commands)==8
output_hashes=[]
for r in commands:
    raw=(OUT/'post_append'/r['output_path']).read_bytes()
    # subprocess text capture used LF; Path.write_text on Windows retained CRLF.
    # Bind both rather than silently treating the text hash as the file hash.
    assert sha(raw.replace(b'\r\n',b'\n'))==r['output_sha256']
    output_hashes.append(dict(path='post_append/'+r['output_path'],raw_file_sha256=sha(raw),
        normalized_lf_utf8_sha256=r['output_sha256'],original_hash_field_scope='CAPTURED_LF_TEXT_BEFORE_WINDOWS_WRITE'))
put('command_output_hash_audit.json',output_hashes)
# archive validate writes its report in the archive. Retain that generated output
# here and restore the exact clean opening Git bytes, without touching archive data.
target=ROOT/'Previous Sports Results/_canonical/validation.json'
generated=target.read_bytes();(OUT/'archive_validation_generated.json').write_bytes(generated)
original_validation=subprocess.check_output(['git','show',opening['authority_commit']+':Previous Sports Results/_canonical/validation.json'],cwd=ROOT)
target.write_bytes(original_validation)
assert target.read_bytes()==original_validation
archive=json.loads((OUT/'post_append/archive.output.txt').read_text())
receipt=json.loads((OUT/'source_body_validation.json').read_text());assert receipt['failed']==0
deps=[]
for line in (ROOT/'research/requirements.lock.txt').read_text().splitlines():
    if '==' in line and not line.startswith('#'):
        package,expected=line.split('==');actual=version(package);assert actual==expected;deps.append(dict(package=package,expected=expected,actual=actual))
checks=dict(observed_utc=datetime.now(timezone.utc).isoformat(),mini_exact_original_prefix=True,mini_exact_addendum=True,
    authority_files_unchanged=unchanged,canonical_next_id='P-527',canonical_ids_affected=[],
    original_part6_bytes=141740,diagnostic_revisions_verified=len(revisions),diagnostic_chain_head=previous,
    source_body_receipts=receipt['total'],source_body_receipt_errors=0,pinned_packages=deps,
    python_version=sys.version,archive_validator_output_retained='archive_validation_generated.json',
    archive_validation_restored_to_opening_git_bytes=True,archive_validation_original_sha256=sha(original_validation),
    archive_issue_count=len(archive['issues']),archive_issue_classes=dict(Counter(x.split(':')[0] for x in archive['issues'])))
put('final_readback.json',checks)
# Index only event-relevant sources; mixed web extracts stay local/quarantined.
sources=[
 ('P-527','Real Madrid club','https://www.realmadrid.com/es-ES/noticias/baloncesto/primer-equipo/cronicas/cronica-hapoel-real-madrid-01-10-2026','Official participant; not a league-native receipt','FINAL 102-98','club article; league ID NOT_VERIFIED','UNKNOWN'),
 ('P-527','Hapoel club','https://hapoelbc.com/games/hapoel-ibi-tel-aviv-vs-real-madrid-8/','Official participant','quarter table ends 102-98; stale header 0-0 rejected','club CMS slug; league ID NOT_VERIFIED','UNKNOWN; may share official scoreboard upstream'),
 ('P-527','Sofascore','https://www.sofascore.com/basketball/match/hapoel-tel-aviv-real-madrid/PvbsETH','Secondary','Finished 102-98; venue field conflict','provider fixture URL','UNKNOWN'),
 ('P-527','Eurohoops','https://www.eurohoops.net/en/euroleague/2014883/euroleague-roundup-hapoel-survives-reals-comeback-and-secures-a-victory/','Secondary reporting','102-98','article 2014883','UNKNOWN'),
 ('P-528','Griffins club','https://griffinshockey.com/schedule/home-schedule','Official participant schedule','NOT_TERMINAL; isFinal false; scheduled 2026-10-02T19:00:00-04:00','club CMS 757375; AHL ID NOT_VERIFIED','UNKNOWN'),
 ('P-529','NHL game summary','https://www.nhl.com/scores/htmlreports/20262027/GS020009.HTM','League owner','FINAL Devils 3-2 OT; start 19:09 EDT minute precision','2026020009, season 20262027','Same NHL collection; no independent audit'),
 ('P-529','NHL roster','https://www.nhl.com/scores/htmlreports/20262027/RO020009.HTM','League owner','IN_PROGRESS CAPTURE; roster only, not terminal','2026020009, season 20262027','Same NHL collection'),
 ('P-529','Devils club recap','https://www.nhl.com/devils/news/topic/game-day/njd-vs-phi/10-01-2026/2026020009/game-story-2026020009','Official participant','3-2 OT','2026020009','UNKNOWN; NHL-hosted same-owner report'),
 ('P-529','Reddit NHL-linked bot','https://www.reddit.com/r/Flyers/comments/1wvhgpk/post_game_thread_the_flyers_fell_to_the_devils_in/','Secondary mirror','FINAL 3-2 OT; regulation 2-2','NHL-linked exact fixture','SHARED_OFFICIAL_UPSTREAM; not independent'),
 ('P-530','MLB-linked Reddit table','https://www.reddit.com/r/Braves/comments/1wvixxx/nl_wild_card_series_game_3_the_braves_defeated/','Secondary mirror','Game Over 6-2 Atlanta','MLB Gameday link','SHARED_OR_UNKNOWN; no second collection admitted'),
 ('P-531','WNBA event page','https://www.wnba.com/game/ind-vs-lva-1042600123','League owner fixture','SHELL; terminal fields not recovered','1042600123','Same WNBA collection; no terminal observation'),
 ('P-531','Sofascore','https://www.sofascore.com/basketball/match/las-vegas-aces-indiana-fever/cubsalo','Secondary','Finished IND83-LVA94; four quarters; secondary PBP','provider event URL','UNKNOWN'),
 ('P-531','Reddit early postgame','https://www.reddit.com/r/wnba/comments/1wvjiph/postgame_thread_fever_aces_game_3_01_oct_2026/','Secondary','conflicting 92-83; apparent incomplete result','ESPN link 401918022','UNKNOWN; not admitted terminal'),
 ('P-531','theScore','https://www.thescore.com/wnba/event/2474663?source=league_page','Secondary','STALE_LIVE 82-88; partial statistics rejected as final','2474663','UNKNOWN; not terminal'),
 ('P-531','StatMuse','https://www.statmuse.com/wnba/game/10-1-2026-ind-at-lva-8088','Secondary','STALE_LIVE 80-82','8088','UNKNOWN; not terminal'),
 ('P-531','WNBA daily CDN','https://cdn.wnba.com/static/json/liveData/scoreboard/todaysScoreboard_10.json','League owner','WRONG_DATE: scoreboard gameDate 2026-09-30','does not contain current fixture','Same WNBA collection; rejected for this event'),
 ('P-531','WNBA series preview','https://www.wnba.com/news/2026-playoffs-series-preview-first-round','League owner context','NOT_TERMINAL_EVIDENCE; 2026 1-1-1 format and original context','2026 first round','Same WNBA collection; context only')]
web=json.loads((OUT/'web_extract_manifest.json').read_text())['files'];rows=[]
for pid,publisher,url,ownership,state,native,lineage in sources:
    matches=[dict(path=f['path'],sha256=f['sha256'],capture_persisted_utc=f['capture_persisted_utc']) for f in web if url in json.loads((ROOT/f['path']).read_bytes())['tool_result']]
    rows.append(dict(local_reservation=pid,publisher=publisher,url=url,ownership=ownership,
        result_field_or_state=state,native_identity=native,independence=lineage,
        retrieved_utc='NOT_CAPTURED_BY_TOOL_RESULT',parser_id='MANUAL_WEB_TOOL_FIELD_READBACK_NOT_ADMITTED_NATIVE_PARSER',
        source_registry='NOT_REGISTERED_FOR_THIS_LEAGUE_ROUTE; manual research allowed, no certified adapter inferred',
        raw_http_body='NOT_RETAINED_BY_WEB_TOOL',retained_tool_extracts=matches))
for p in sorted((ROOT/'research/data/source_receipts').glob('mlb_official_20261002*.json')):
    r=json.loads(p.read_text());rows.append(dict(local_reservation='P-530',publisher=r['publisher'],url=r['source_url'],ownership='LEAGUE_FIELD_OWNER',
        result_field_or_state='FINAL ATL6-PHI2; nine-inning full-game completion',native_identity='849844; 2026/10/01/phimlb-atlmlb-1',
        independence=r['independence_status'],lineage=r['upstream_lineage_id'],retrieved_utc=r['retrieved_utc'],parser_id=r['parser_id'],
        source_registry=r['registry_sha256'],raw_http_body=r['body_path'],raw_body_sha256=r['response_sha256'],receipt_path=p.relative_to(ROOT).as_posix()))
put('source_event_audit.json',dict(observed_utc=checks['observed_utc'],sources=rows,
    certification='NO_THREE_AUDITED_INDEPENDENT_TERMINAL_LINEAGES_FOR_ANY_EVENT',
    rejected='Wrong-season NHL 20252026/RO020009; wrong-date WNBA daily feed; in-progress rosters; stale live scores; snippets without opened terminal fields; inaccessible pages.'))
report='''# Local mini settlement audit — October 2, 2026

The existing Downloads mini was updated in place with four twelve-part retrospectives and all ranked-row diagnostic grades. Five records were inventoried. No canonical IDs were affected, no import or archive occurred, and the next canonical ID remains P-527. This is an audit report, not another running log.

## Authority and preserved original

METHOD.md and CURRENT_RULES.md at fetched GitHub main commit `5ce5de3ed9a70ecae173dbe4e9a05445ca97e1d9` govern this pass. The mandatory documents, current implementation and relevant basketball/baseball/hockey league sections were freshly inspected. The attached mini's old read-only and deferred-retrospective statements are historical forecast context; the user's pasted request explicitly authorizes the present append. Current authority hashes are in [opening_custody.json](opening_custody.json); no authority file was changed. Current strict ISSUE settlement tooling is inapplicable because none of these fallback reservations has a genuine canonical ISSUE. Separate diagnostic addenda follow the current dated audit pattern; no issuer schema is fabricated.

Original mini: `C:\\Users\\danie\\Downloads\\PREDICTION_MINI_RUNNING_LOG_P527_ONWARD_UPDATED_4.md`. Its exact first 7,831 bytes are preserved, SHA-256 `3da1ef7437d05f70e2a36b6ed7e66d848e04d48c16b1aba5d802c923b8c7e5b8`. The source exhibit is [original_mini_evidence.txt](original_mini_evidence.txt), not an archived replacement. Only P-531 retains its full original card; P-527–P-530 retain a summary table. Missing rationale, probabilities, cutoffs and contracts are not reconstructed.

## Dispositions

| Local reservation | Diagnostic result | R1 | R2 | R3 | R4 | Formal grade/status |
|---|---|---|---|---|---|---|
| P-527 | Hapoel 102–98 Madrid; total 200 | L* | W* | L* | W* | Every row UNRESOLVED: original endpoint/terms missing |
| P-528 | October 3 09:00 AEST schedule; not final | UNRESOLVED | UNRESOLVED | UNRESOLVED | UNRESOLVED | Future/unsettled |
| P-529 | Devils 3–2 OT; regulation 2–2 | W* incl OT | W* | L* | W* | Every row UNRESOLVED; regulation ML definition especially material |
| P-530 | Braves 6–2; total 8 | W* | W* | W* | L* | Every row UNRESOLVED: original endpoint/action terms missing |
| P-531 | Aces 94–83; provisional secondary finished score | L† | L† | W† | W† | Research endpoint defined; operator UNKNOWN_DEFINITION and final owner/quorum missing |

* Conditional full-game interpretation only, not an original ticket grade. † Original full-game research scope including OT; still provisional secondary evidence. Zero certified/performance-eligible settlements, four separate diagnostic revisions, one unplayed carryover. Potential winner missed for P-527; correct full-game directions for P-529/P-530/P-531; P-528 unresolved. P-531's narrow-margin expectation failed. Complete twelve-part retrospectives are appended to the active mini and reproduced exactly as append custody in [settlement_addendum.txt](settlement_addendum.txt). No new active log was created.

## Evidence and independence

[source_event_audit.json](source_event_audit.json) gives exact URLs, ownership, event/native IDs, score/period fields, source-registry/parser status, retrieval timestamp or explicit missingness, body/extract hashes and upstream assessment. [web_extract_manifest.json](web_extract_manifest.json) hashes every retained tool extract. These are **WEB_TOOL_EXTRACT_NOT_RAW_HTTP**. The tool did not expose exact original HTTP retrieval times; persistence timestamps are separate. Mixed navigation/market fields remain in ignored, quarantined `research/data/benchmark/mini_settlement_2026-10-02/` files; no prices or market opinions are used. Successful original raw-body custody exists for the two approved MLB requests:

| Registered receipt | Retrieved UTC | Body SHA-256 | Scope |
|---|---|---|---|
| mlb_official_20261002T034536833748Z_b2a1d2537f87.json | 2026-10-02T03:45:36.833748+00:00 | b2a1d2537f87edc190f8a03394e63282dae9353b934539c87b052af1b2725006 | Schedule/linescore |
| mlb_official_20261002T034828704675Z_e28f14e4f1f7.json | 2026-10-02T03:48:28.704675+00:00 | e28f14e4f1f7680f57d1ee5d2a1fbc11040aa707d7caf6abb0a9197ddfdb9d08 | Native owner feed 849844 |

Both share `MLB_OFFICIAL_COLLECTION`, parser `MLB_STATSAPI_V1`, registry SHA `031ca77a5d8fb791c3f0dc9e8fecd62e7cba5647ba7ba63ddba11cd2817f4716`, independence UNKNOWN. They count as one owner collection, not two independent finals. The retained [MLB fields](mlb_owner_fields.json) include exact completion, innings, starters, starting orders, bullpen sequence and first-play candidates; first play is not substituted for an audited actual-start field.

NHL owner actual start 19:09 EDT is explicitly reported with minute precision, but lacks an admitted event-specific parser/lineage audit. All other audited actual-start fields remain missing. Scheduled starts stay separate. The NHL same-number wrong-season roster link is rejected. Hapoel's stale 0–0 header and venue metadata conflict are retained rather than voted into final truth. WNBA's owner fixture opens only a shell; its daily CDN feed is wrong date, exact boxscore attempt failed, ESPN returned robot verification, and the local browser runtime could not start. The 92–83 secondary report is apparently incomplete relative to the later finished 94–83 play sequence. Stale theScore/StatMuse statistics and search-only final tables are not adopted as final participation evidence. No event has three audited independent terminal collections.

## Learning boundaries

All five original qualitative/research-only classifications remain; P-530/P-531 remain LATE_RESEARCH. P-531 literal p/baseline remain NOT_ESTIMATED. The other summaries lack literal p/q/baseline: NOT_RETAINED_IN_SUMMARY is retained as missingness. Brier/log loss/surprise and adjustment comparisons are not computable. Four complementary rows per event are not four independent observations; no aggregate accuracy, calibration, skill or ROI is claimed.

P-531 shows why a correct outright direction does not validate a cushion or a narrow score corridor. Its late-foul branch can support scoring while worsening an underdog spread, and the named injury/pace mechanisms cannot be confirmed without actual participation and possessions. P-529 requires separating regulation from OT: the top moneyline won only at full game. P-530's successful cushion won through an outright win and Over only narrowly crossed; original reasoning is missing and is reviewed with the same scrutiny as losses. P-527's cushion win coexists with a wrong winner lean and wrong total direction. Each completed event has an explicitly censored mechanism review, error taxonomy, next prospective test/acceptance criterion and a no-weight-change conclusion. No result is promoted into a new rule.

## Verification

All eight prescribed command groups ran before and again after the actual append. Exact commands, timestamps and exit codes are in [command_results.json](command_results.json) and [post_append/command_results.json](post_append/command_results.json). Their output_sha256 fields hash the captured LF text before Windows text-file writing; [command_output_hash_audit.json](command_output_hash_audit.json) separately binds retained CRLF file bytes and the normalized text hashes. Current checks:

'''
report+='| Check | Result | Evidence |\n|---|---|---|\n'
notes={'tests':'113 passed, 2 failed; pinned model artifact research/src/control_manifest.py differs',
    'archive':f"FAIL; {len(archive['issues'])} archive manifest issues; see complete JSON/output",
    'custody':'FAIL; retained historical manifest missing; wrapper stops before completing acceptance',
    'acceptance':'FAIL; same missing retained manifest; not a successful acceptance receipt',
    'canonical_log':'PASS; P-523–P-526 projections verified, next P-527',
    'freeze':'FAIL; 374 files / 20 mismatches, already observed before this work',
    'workflow_status':'PASS; no canonical prospective issues; four model registrations remain SHADOW_ONLY',
    'workflow_score':'PASS; zero issued/scored events; no local diagnostics injected into live scoring'}
for r in commands:
    report+=f"| {r['check']} | {'PASS' if r['exit_code']==0 else 'FAIL'} — {notes[r['check']]} | [{r['output_path']}](post_append/{r['output_path']}) |\n"
report+='''
Independent scoped readbacks pass: original mini prefix and exact append; four diagnostic revision hashes/source joins; unchanged canonical ledger/Part 6/status/control documents; 141,740-byte frozen source block; 75 source-receipt bodies (zero errors); exact pinned package versions. These scoped successes do not turn failed full checks into a pass. [implementation_snapshot_gaps.json](implementation_snapshot_gaps.json) enumerates nine missing retained historical manifests among 89 snapshot files. No manifests are recreated and no frozen receipt/build is refreshed to conceal failures. Archive validation records existing indexed input changes and one body-not-retained receipt; archive data and its manifest were not edited. The validator's generated validation.json was retained as [archive_validation_generated.json](archive_validation_generated.json), then its exact clean opening Git bytes restored. [final_readback.json](final_readback.json) records the restoration and complete scoped checks.

## Exact changed/created files

The sole existing user document changed is the named Downloads mini. Repository additions are this audit directory and two MLB raw bodies/two corresponding receipts; seventeen quarantined web extract files are local/ignored. No existing repository control, canonical log/ledger, sport rule, archive result or source registry is changed. No Git staging, commit or push occurred in this task.

'''
report+='Files in this audit directory (including this REPORT.md):\n\n'
names=sorted(set([p.relative_to(OUT).as_posix() for p in OUT.rglob('*') if p.is_file()]+['REPORT.md','final_inventory.json']))
for name in names: report+=f'- `{name}`\n'
report+='\nRaw source additions:\n\n'
for p in sorted((ROOT/'research/data/source_receipts').glob('mlb_official_20261002*.json')):
    r=json.loads(p.read_text());report+=f"- `{p.relative_to(ROOT).as_posix()}`\n- `{r['body_path']}`\n"
report+='\nIgnored local tool extracts: `research/data/benchmark/mini_settlement_2026-10-02/web_tool_01.json` through `web_tool_17.json`, all individually hashed in the manifest.\n'
(OUT/'REPORT.md').write_text(report,encoding='utf-8')
inventory=dict(observed_utc=checks['observed_utc'],mini_path=str(mini),mini_sha256=sha(mini.read_bytes()),
    files=[dict(path=p.relative_to(ROOT).as_posix(),sha256=sha(p.read_bytes()),bytes=len(p.read_bytes())) for p in sorted(OUT.rglob('*')) if p.is_file() and p.name!='final_inventory.json'],
    git_status=subprocess.check_output(['git','status','--short'],cwd=ROOT,text=True),
    no_git_publication=True,scope='Existing mini updated; audit and source evidence additions only')
put('final_inventory.json',inventory)
print(json.dumps(dict(original_prefix=True,diagnostic_revisions=4,certified_settlements=0,canonical_next_id='P-527',archive_issues=len(archive['issues']),report=str(OUT/'REPORT.md'))))
