from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re,subprocess

ROOT=Path(__file__).resolve().parents[3];OUT=Path(__file__).resolve().parent
def load(name):return json.loads((OUT/name).read_text(encoding='utf-8'))
readback=load('final_readback.json');grades=load('conditional_diagnostic_grades.json');events=load('event_review.json')
before=load('before_log_import/command_results.json');after=load('post_import/command_results.json')
assert len(before)==len(after)==9
for phase,items in [('before_log_import',before),('post_import',after)]:
    for item in items:
        raw=(OUT/phase/(item['name']+'.output.txt')).read_bytes()
        assert hashlib.sha256(raw).hexdigest()==item['output_sha256']
        assert item['exit_code']==next(x['exit_code'] for x in before if x['name']==item['name'])
report='''# October 5 CSV cleanup, canonical reconciliation and settlement audit

Completed locally: 255 redundant export CSVs were verified against their exact archive copies and recycled; eleven unique historical research events were transactionally allocated P-527–P-537; four overlapping consolidated versions were appended under their existing IDs; eleven twelve-part retrospectives and deterministic conditional sporting grades were appended to Part 6 and both existing mini references. Next canonical ID is **P-538**. No mini was archived or newly started, and no commit/push was performed.

Five fallback mini records plus ten consolidated entries represent eleven unique events. The original local reservations P-527–P-531 were not prior canonical commitments; the logger allocated them in their retained order. The six additional unique events follow as P-532–P-537. The supplied P-516 mini reference path does not exist in the current repository. The actual existing repository P-523 mini and Downloads P-527 fallback mini were therefore updated in place as reference copies; Part 6 remains authoritative.

All eleven have observed full-game terminal results, with Kyrgyzstan–Lebanon's 3-1 still provisional multi-secondary evidence. Ten have complete conditional grades for their ranked rows; Kyrgyzstan–Lebanon retains unresolved first-half and corner fields. **Zero operator-certified or performance-eligible settlements.** Original unknown contract terms, missing/unadmitted actual-start/cutoff evidence, and lack of three audited independent terminal collections remain disclosed. Diagnostic W/L is not an original ticket or live-model performance grade.

## CSV cleanup

| Recycled root folder | Retained archive destination | Files |
|---|---|---|
| Austria_Bundesliga_Basketball_CSVs | Previous Sports Results/Basketball/Austria Basketball Bundesliga/<year>/<year>_games.csv | 51 |
| County_Cricket_CSVs | Previous Sports Results/Cricket Tests/County Championship/<year>/<year>_games.csv | 51 |
| Greek_Basket_League_CSVs | Previous Sports Results/Basketball/Greek Basket League/<year>/<year>_games.csv | 51 |
| IPL_CSVs | Previous Sports Results/Cricket T20/IPL/<year>/<year>_games.csv | 51 |
| NRL_CSVs | Previous Sports Results/Rugby League/NRL/<year>/<year>_games.csv | 51 |

Every 1975–2025 file was an exact SHA-256 byte match before removal; all destinations were rechecked afterwards, including 34,318 data rows. This is preservation evidence, not certification that every row is a genuine game: some builders contain historical placeholder/summary rows. No archive result CSV was changed. Five builders now write only to their existing archive destinations, preventing recreation of the root exports. The Austrian BSL mirror inside Previous Sports Results remains. Operational input/output ledgers, source caches and frozen custody CSVs remain functional; they are not redundant external archive exports. No root *_CSVs folder remains. Recovery is available through the Windows Recycle Bin.

Exact mappings, row counts and hashes: [csv_cleanup_plan.json](csv_cleanup_plan.json). Completed recycling/readback receipt: [csv_cleanup_receipt.json](csv_cleanup_receipt.json).

## Canonical reconciliation and Rank 1/2 outcomes

W/L below means conditional sporting diagnostic only. Unsupported alternatives stay flagged. Explicit NO_FORECAST lists are shadow research, not issued forecasts. NHL's later consolidated source has unranked supplied rows; no rank is backfilled. Multiple versions and rows from one event are not independent observations.

| ID | Event; final (home-away) | Retained source version | R1 | R2 |
|---|---|---|---|---|
'''
for e,g in zip(events,grades):
    for v in g['versions']:
        rows=v['rows']
        r1='NO_RANK / NO_FORECAST' if v['unranked'] else rows[0]['label']+': '+rows[0]['diagnostic_grade']
        r2='NO_RANK / NO_FORECAST' if v['unranked'] else rows[1]['label']+': '+rows[1]['diagnostic_grade']
        report+=f"| {e['id']} | {e['event']}; {e['score'][0]}-{e['score'][1]} | {v['source_version']} | {r1} | {r2} |\n"
report+='''
All ranked/supplied row grades, winner projections, exact lines and version constraints are in [conditional_diagnostic_grades.json](conditional_diagnostic_grades.json). Eleven full twelve-part reviews are in [settlement_addendum.md](settlement_addendum.md), reproduced in Part 6 and the existing mini references. The separate eleven-record [diagnostic revision chain](diagnostic_revisions.jsonl) joins each canonical research commitment, unchanged original source checksum, prior October 2 diagnostic revision where present, all source evidence and exact appended projection. It does not fabricate an ISSUE/SETTLEMENT record in the strict prospective ledger. [import_results.json](import_results.json) binds actual allocations; [append_receipt.json](append_receipt.json) binds all target writes and readbacks.

## Remaining settlement blocks and retrospective findings

- **P-537 first-half O/U 0.5:** UNRESOLVED_PERIOD. Detailed reports/explicit halftime say 2-0; ESPN split fields say 0-0. No admitted authoritative phase receipt resolves the conflict. First-half Over would win under one version and lose under the other; neither is silently selected. **Corners Over 9.5:** UNRESOLVED_PROVIDER_FIELD; no count/provider terms were recovered. Missing corners are not zero. Full-time Over wins provisionally; Draw and Lebanon win fail. Unsupported alternatives remain outside supplied contracts/performance scoring.
- **All eleven:** operator/action definitions and audited independent terminal quorum remain absent; actual starts are missing or unadmitted. NHL owner reports a minute-precision actual start, but it is not an admitted parser/lineage audit. No certification is fabricated. NBL and later EuroLeague/NHL NO_FORECAST states remain abstentions; MLB/WNBA LATE_RESEARCH remain late. Original PREGAME/VERIFIED labels are source claims, not retroactive certification.
- **WNBA:** owner final 94-83 is now recovered, superseding the earlier owner-evidence gap diagnostically while preserving the earlier audit. Fever +4.5 and original Over 181.5 lost through the stated one-side-mid-80s/closing-separation risk branch. Later Under-second order is retained separately. Loyd started instead of the original probable Talbot; participation does not prove injury causality. The correct outright lean did not validate the narrow-margin expectation.
- **EuroLeague:** a winning Hapoel cushion coexists with the wrong Madrid winner and wrong Under. Changed rank order is not a frozen paired adjustment. Venue metadata/stale owner header are retained. Native event ID was not recovered; failed league-feed pagination did not supply this event.
- **NHL:** full-game Devils ML wins through OT, regulation was 2-2; undefined regulation ML action is not assigned a push/void. Wrong-season roster/report evidence is rejected. Shots and final goals are distinct.
- **MLB/KBO:** Over crossings were narrow, while successful side directions do not validate a total or weather/bullpen mechanism. MLB duplicate Over row is not silently replaced by Under; Under is a separate unsupported shadow alternative. KBO shadow KIA ML differs from the supplied Tigers +1.5.
- **AHL:** October 2 regular-season 5-2 is separated from September 27 preseason 5-2 and October 4 rematch 4-5 OT. The prior unplayed carryover is now completed. Cleveland's 4-2 introductory sentence conflicts with its 5-2 table/goal sequence; retained rather than erased. Over was already above 5.5 before the empty-net goal.
- **NRL/Greek/BBL:** gapped spreads and totals are not complementary outcomes. Winner/cover and one-team/combined scoring budgets are reviewed separately. Bayern's top ranks win despite its incorrect full-roster and PREGAME claims; a 40-hour turnaround is not consecutive-day back-to-back play. Sydney DST labels and the soccer two-hour schedule discrepancy remain explicit.

Only WNBA retains a full original rationale; the first four fallback records have summary-only originals, and consolidated entries omit full mechanisms. Missing rationale, probabilities, cutoff, distributions and baseline remain censored. Every review covers wins with the same scrutiny as losses, names observed versus predeclared mechanisms, classifies errors, and supplies a prospective test/acceptance criterion. No original p, cap, weight or ranking rule is rewritten. No calibration, predictive skill, ROI or correlated-row accuracy is claimed.

## Sources and custody

The fetched authority is main `c730d3de094e4e8ecd12cdbe1776f5f0da1bd7d3`: MDS-2026.10.01-v7.1, CR-2026.10.01-I2, SCV-2026.10.01-v3, selected CONTROL_MANIFEST_2026-10-01-5.md. Current rules/templates/verification/sport definitions were freshly read; original attachments and fallback mini were retained exactly in `originals/`. Governing documents were unchanged. [opening_custody.json](opening_custody.json) records authority/source hashes and the initial clean Git HEAD; its dirty entry contains the audit preparation script already created for this task.

[source_event_audit.json](source_event_audit.json) records exact URLs, owner/provider identity, native IDs or explicit UNKNOWN, endpoints, timing and conflicts. [source_capture_manifest.json](source_capture_manifest.json) binds raw-body retrieval timestamps and hashes, source failures, and WEB_TOOL_EXTRACT_NOT_RAW_HTTP captures. Tool persistence times are not relabelled as HTTP retrieval. Mixed navigation/market-bearing extracts and manually fetched bodies stay in ignored benchmark quarantine; only sports facts/receipt metadata are projected. No market data was used: SPORTS_ONLY / MARKET_BLIND. Registered approved NBL/MLB receipts remain normal source custody, not automatic terminal certification.

No web publisher is assumed independent merely because its domain differs. League/club/AP/AAP mirrors and possible provider reuse are identified; all unaudited upstream relationships remain UNKNOWN. Source presence does not equal admitted parser/event evidence. Shells, wrong dates/seasons, search-only conflicts, stale scores and missing period fields are rejected or explicitly censored. Failed source attempts are retained.

## Verification

All nine prescribed command groups ran before and after the actual changes. Exact command, UTC timestamps, exit codes and verified retained-output hashes are in [before_log_import/command_results.json](before_log_import/command_results.json) and [post_import/command_results.json](post_import/command_results.json).

| Check | Final result | Evidence/limit |
|---|---|---|
| Canonical log/ledger | PASS | 15 research cards, no pending transaction, next P-538 |
| Logging tests | PASS | 7 passed |
| Research tests | FAIL | 106 passed, 2 failed; both pinned research/src/control_manifest.py mismatch, already failed before import |
| Custody | FAIL | Missing retained implementation CONTROL_MANIFEST_2026-09-28-4.md; pre-existing |
| Acceptance | FAIL | Same missing retained manifest; no successful acceptance receipt |
| Freeze | FAIL | 374 files / 118 mismatches, same count/categories as opening check |
| Archive/source validation | FAIL | 614 existing issues; 1,614 retained bodies verified, one body not retained; exact validation output saved and original tracked validation.json restored |
| Workflow status | PASS | Research records do not become live/prospective issues |
| Workflow score | PASS | No diagnostic grades injected as certified performance |
'''
report+=f"\nIndependent scoped readbacks: **{len(readback['checks'])} PASS**. All **930,958 pre-existing Part 6 bytes** are preserved, including its frozen 141,740-byte block with SHA-256 `c4d497bf339010eae2ff5df23a2d76290983585671666e74791618342565cf30`. Parts 1–5 and all archive result CSVs have no edits. The original ledger prefix and both mini prefixes are preserved; all 255 archive hashes/row counts, fifteen canonical projections, eleven diagnostic chain/source joins, 132 retrospective sections and independent spread/total arithmetic checks pass. {readback['raw_source_bodies']} captured raw bodies and {readback['quarantined_tool_captures']} quarantined tool extracts match retained hashes. Five edited builders parse and have no root export writes; generators were not rerun over the archive. [final_readback.json](final_readback.json) gives each invariant.\n"
report+='''
Full `git diff --check` returns 227 warnings, all retained source Markdown hard-break lines; exact source/forecast projections are immutable. The editable status/ledger/builder scope passes. [diff_check_audit.json](diff_check_audit.json) classifies every warning; this is not described as a full whitespace pass. No freeze/model/archive manifest was regenerated to conceal failures.

## Exact changed files

The complete file-level inventory, including all 255 removed paths, eleven issued_research source/projection pairs, approved source bodies/receipts and all new audit artifacts, is [changed_files.json](changed_files.json), with exact Git porcelain readback in [git_status_exact.txt](git_status_exact.txt). No unrelated dirty files existed at opening.

Existing non-CSV repository files changed:

- `prediction logs/PREDICTION_LOG_COMBINED_6.md`
- `GAME_LOG_STATUS_CURRENT.md`
- `research/canonical_ledger.jsonl` (11 PREPARED/COMMITTED research pairs; settlement leaves this allocation ledger unchanged)
- `Mini logs (to be sent to actual log later)/Mini Prediction Log - P-523 onward - 2026-10-01/PREDICTION_MINI_RUNNING_LOG_P523_ONWARD.md`
- `research/src/build_austria_bundesliga_all_years.py`
- `research/src/build_county_cricket_all_years.py`
- `research/src/build_greek_basket_league_all_years.py`
- `research/src/build_ipl_all_years.py`
- `research/src/build_nrl_all_years.py`

Existing external file updated in place: `C:/Users/danie/Downloads/PREDICTION_MINI_RUNNING_LOG_P527_ONWARD_UPDATED_4.md`. Original byte prefix is retained; its old administrative read-only/deferred-retrospective/local-ID statements are historical, superseded by this user-authorized dated appendix. Neither mini was archived. No Git staging, commit or push occurred.
'''
(OUT/'REPORT.md').write_text(report,encoding='utf-8')
(OUT/'report_receipt.json').write_text(json.dumps(dict(recorded_utc=datetime.now(timezone.utc).isoformat(),report_sha256=hashlib.sha256((OUT/'REPORT.md').read_bytes()).hexdigest(),verification_output_hashes_match=True,all_command_exit_codes_same_before_after=True),indent=2)+'\n',encoding='utf-8')
print('Completion report written; all nine before/after output hashes and exit-code comparisons verified.')
