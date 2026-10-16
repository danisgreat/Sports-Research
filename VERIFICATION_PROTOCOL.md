# Verification protocol

**Online history and confirmed players (HIST-2026.10.16-v2 / AVAIL-2026.10.16-v3).** For every game, research both sides' L5/L10/L15/L20 online under [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md), with opened sources, dated game rows and true n. Seek exact-game confirmed players, starting roles, bench/replacements and absences under [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md); projected players remain unconfirmed. The retired local results store and its derived profiles are not required inputs or fallbacks. Earlier archive-first directions are superseded.

**Required repository fallback (REF-v1).** Always keep [https://github.com/danisgreat/Sports-Research/tree/main](https://github.com/danisgreat/Sports-Research/tree/main) as the standing reference. If required local files are not fully accessible (missing, unreadable, truncated or incomplete), retrieve the actual required contents from this repository before declaring them unavailable. Apply [GITHUB_REFERENCE_PROTOCOL](GITHUB_REFERENCE_PROTOCOL.md): resolve one main commit SHA, record exact files/read time and fallback results in the existing reading receipt, and preserve the declared authority mode. Never substitute an unpublished local mini, claim unread content or treat viewing code as executing it. If authorized remote access also fails, record the real gap and continue independent work.

**CR-2026.10.16-R2** ([previous](archive/superseded_2026-10-15-3/VERIFICATION_PROTOCOL.md); [earlier](archive/superseded_2026-10-12/VERIFICATION_PROTOCOL.md)). Markdown/CSV/text only. Checks establish their stated properties, never predictive skill. Use plain file/git commands and transparent arithmetic; do not add a validator runtime. Print `Check | PASS/FAIL/NOT_VERIFIED/N/A | evidence | limitation`.

## 1. Before changes

Record cwd, branch, HEAD, current status, authority mode and intended paths. Read the task's authority and preserve unrelated modifications. Inspect actual line endings and source contents. Do not blindly checkout, pull, reset, restore whole files or stage all paths. Read-only missing inputs block only dependent actions.

**Byte identity (R20).** For every file whose bytes matter, record:
- `git check-attr text <path>`: `-text` files are byte-exact in git;
- `git ls-files --eol <path>`;
- the raw CRLF/LF counts and SHA-256 of the working file.

Say which identity a comparison proves: raw source snapshot, imported core, destination prefix or committed blob (CURRENT_RULES §9). Edit `-text` or mixed-ending files at byte level, from the original bytes, and confirm that the CRLF/LF counts change only where intended. A text editor can rewrite every line ending of a mixed file.

## 2. Card and settlement

Primary ML/RL checks: actual fitted run/bundle, scope and input known-at/source hashes; coherent original rows versus the re-mixed frozen expert grids; mixture weights recomputed from the recorded cumulative losses and η; information horizon equals the game-log scheduled start unless an earlier actual issue/first play is recorded, and no `cutoff` request column; L5/L10/L15/L20 true n; no market columns; negative endpoint/source/duplicate/future-feedback/tamper cases. Unsupported or failed runs cannot claim numeric ML use. Settle original rows before generating sporting feedback; one effective event/revision and final/availability times required. Primary experimental use is separate from predictive qualification. See [primary protocol](PRIMARY_PREDICTION_PROTOCOL.md).
[Timing checks](TIMING_RESEARCH_PROTOCOL.md): ensure no fixed research deadline forces issue, preserve actual phase and source horizon separately, and require independent pre-start publication proof/no outcome exposure for CLEAN_PRE_START_INPUTS. Near-start or delayed PREGAME is valid with actual not-started evidence; post-start issue remains a separate scored research cohort. Unknown actual start, late-published inputs, changed dynamic pages, live-result exposure and backdated issue each fail the relevant clean-input/pre-start-release claim. Completing research after start alone is not a process failure. Legacy issued labels and registered model/prospective timing gates remain unchanged.
Availability checks use [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md): verify both sides, starters/bench/absence evidence separately, local-language escalation when needed, and final late-change recheck. An incomplete search fails C20; complete research with genuine missing publication remains unconfirmed. Check the exact side/field and scenario or qualitative disposition, not whether a CONFIRMED string is present.

Run C1-C21 and S1-S16 for mini-log-9 / mini-settlement-8; mini-log-8 / mini-settlement-7 use their declared EXEC-v1 checks and older formats use their own checks in [CARD_AND_LOG_TEMPLATES](CARD_AND_LOG_TEMPLATES.md), with actual arithmetic and readback. Retain missing values honestly. A negative fixture must fail the relevant check; do not claim checks are executed merely because the checklist is present.

## 3. Import

1. Reconcile current state/status with canonical blocks and dated changes; opening headers are historical.
2. Exact frozen mini prefix in settled file, actual bytes and line endings; line counts alone insufficient.
3. Inventory equals new + exact existing + conflicts for cards; separately account for every carryover/addendum/settlement. Existing cards may still need new addenda.
4. Compare every imported original core and appended source block, not a sample. Marker counts, event identity, contract/rank/p/baseline/expected score/cutoff and source provenance agree.
5. Compare complete pre-import log prefix byte-for-byte; appended suffix only. Numstat deleted=0 and end-only diff hunks are supporting checks, not substitutes.
6. Sequential new IDs, existing IDs preserved, reserved IDs untouched. Addenda and reruns consume none. Replay of an exact completed import plans zero changes.
7. Status/next ID/settlement queues/scoreboard reconcile; no timestamp or performance upgrade from import.
8. Partial-write recovery uses a source-to-destination block map. Identical completed blocks are skipped; conflicting or partial blocks block further mutation until scoped recovery.
9. **Markers (R19):**
   - every BEGIN has exactly one END with the same ID and revision key;
   - no cross-ID nesting;
   - no duplicate revision key per ID;
   - the declared format is known.

   Legacy keyless settlement markers pass under their declared format. Malformed blocks fail before any mutation.
10. **Pre-mutation recheck (R18):** immediately before each append batch, HEAD, active path, destination byte count/SHA-256/last marker and source inventory equal the plan; any difference stops the batch and forces a re-plan.
11. **Revisions (R17):** every contract key's effective revision follows one parent chain. REVISION_CONFLICT keys are UNRESOLVED in state and scoreboard.

## 4. Rollover

Trigger recorded with its measured value (prompt 5 defaults: 1.5 MB or 50 canonical entries). Pre-mutation recheck before the closure and before the new part. Old part is exact original prefix plus closure; new part contains only header/continuity/queue pointers. Next ID before/after identical; zero forecast blocks. Current state/status name the new part; opening header is explicitly dated. Rerun recognizes existing exact closure/new header; no duplicate closure or part.

## 5. Retrospective and archive

Retrospective: scope and prior exposure disclosed; full row inventory reconciles all totals; original and amended settlements not double-counted; ranks/shadows/timing/policy cohorts separated; baseline coverage and missingness shown. Allowed writes: new report folder, scoreboard, CURRENT_STATE, dated hypotheses and CHANGELOG only. No old report or log mutation.

Archive: logical CSV records counted with CSV-aware file facilities or an explicit verified no-embedded-newline convention, not blindly physical lines minus one. A `DATA_PROVENANCE.md` classifies every column. Values are absent where a builder default is proven (HISTORICAL_SOURCE_PROTOCOL §3). The canonical path holds the only copy, and IDs do not use row numbers. Exact headers/types, event keys, doubleheaders, dates, status/endpoint, known zero versus blank, totals/margins, coverage against official schedule and source provenance checked. A sample verifies only the sample; publish unchecked remainder and never call partial coverage complete.

## 6. Framework release and publication

Archive replaced files from the base commit before editing. Check all eight task contracts, every new/changed relative link, consistent method/control/scoring/format versions, examples versus templates, old-format migration and edge cases. Scan live instructions for contradictions and removed-tool dependencies, distinguishing historical citations from commands. New files must be permitted text types; no retired runtime is restored wholesale. Code may change only under `ml/`; then `python -m pytest ml/tests` must pass, every CSV under `research/model_shadow/` must pass the market-column guard (`ml.shadow.lane.assert_no_market_columns`), and a regenerated model file must match a recorded run receipt (code SHA-256, archive snapshot SHA-256).

Compare archived originals to the base revision and confirm issued logs, raw datasets, original sources and dated reports unchanged. Review full diff and staged paths. `git diff --check` must pass. Stage only intended paths; inspect staged status/stat/diff. Commit once checks pass; push without force only under task authorization. Fetch the destination ref afterwards, compare remote SHA with the commit and verify remote artifact contents. Local tracking refs without a fresh fetch are insufficient. Record what was committed/pushed and any unrelated remaining work.

## 7. Limits

A byte comparison proves identity, not source truth. A git SHA is not proof a card was issued before kickoff. A source quotation is not independently audited custody. Correct arithmetic is not a fitted model or calibrated probability. A plausible synthetic example is not live sports validation. Missing evidence must remain visible through every step.

Primary V3 integrity checks: warm training final/available time <= simulated refit; current labels available by issue horizon; no flagged expert in learning; history/feedback event deduplication and score/orientation consistency; finite positive admitted η with exact-policy/timing evidence, otherwise explicit provisional default; cumulative losses match both saved ledgers; no NaN masses/duplicate vector keys; pre-publication bundle verification and code stability. Verify replay coverage/failures, shared calendar-week pooling, DATA_HOLD exclusion, empty outputs and immutable reruns. Old proxy scores never validate the new runtime automatically.

Online history checks: every game requires exact-competition internet research regardless of local data. Check both sides' sourced L5/L10/L15/L20 with true n, corroboration/conflict attempts where needed and confirmed-player searches. Never restore the retired store as fallback. Verify field-level correction/deduplication and known-at evidence. Fresh normalized web history and reviewed competition-source routing must work without archive discovery, while wrong scope/hash/format/future source/unreviewed metadata/market columns and unsupported engines still reject. Count local/web origin honestly and retain the frozen source-config snapshot. No shared archive write is implied by game research.


Research-completion release checks: apply [RESEARCH_COMPLETION_PROTOCOL](RESEARCH_COMPLETION_PROTOCOL.md) to uncalibrated, missing/failed runtime, unsupported family, unconfirmed availability, missing history, active-mini/lease conflict and post-start cases. Each must preserve every independent sport procedure and contract assessment. A NO_FORECAST-only table or unattempted source route fails completion; genuine exhausted gaps pass only COMPLETE_WITH_DOCUMENTED_GAPS with evidence. A supported actual analyst calculation passes only in its labelled NOT_PRIMARY lane, never as a fake ML run, primary p_card or learning feedback. Check all eleven standalone sport workflows and their own Upcoming blocks.


**Research retention before model availability (RETAIN-v1).** [RESEARCH_RETENTION_PROTOCOL](RESEARCH_RETENTION_PROTOCOL.md) supersedes EXEC-v1's model prerequisite for recording/import. Write every identified researched event under its reconciled working P-ID and canonically retain it through verified import even if the model/adapter/runtime/module/baseline/calibration/receipt is absent or failed. Use RESEARCH_ONLY_NO_MODEL, explicit execution reason and blank nonexistent artifact paths; keep model p_card NOT_ESTIMATED and supported analyst_p NOT_PRIMARY. Missing ML never by itself blocks the ID or a source-backed settlement. Retain verified settled labels for future model development with source/known-at/revision/feature status; only actual frozen experts can supply Hedge losses. Never invent probabilities, execution, final scores or pregame timing. Identity/custody/write conflicts remain real blockers.

Legacy EXEC-v1 executable-model checks (recording gate superseded by RETAIN-v1): actual fitting without pre-existing profile/archive/baseline, reviewed exact-competition routing, durable nonzero failed attempts, interrupted/missing/duplicate/wrong-event/tampered execution rejection, mini coverage, baseline conditioning and actual source-backed delayed-feedback verification. Preserve all old log/mini bytes; missing numeric comparisons do not skip an accessible supported execution route; unavailable models retain an honest no-run disposition. Verification checks custody and computed mechanics, not independent source truth or actual pregame publication.

REF-v1 verification: missing, unreadable, truncated and partial required local reads must trigger actual GitHub main recovery. Require full file contents and one pinned commit; test browser/API failure with an authorized Git route, unpublished-local-mini absence, remote failure and local/remote revision conflict. Preserve independent research and honest write/execution limits. A link alone never passes the reading gate.



RETAIN-v1 acceptance: record and import a research-only card despite a missing ml module/adapter/history/receipt; reject the same evidence as a numeric model claim or fake expert feedback; settle verified labels without a model and preserve future training candidates with effective revisions. Check late-source/unknown-feature exclusions separately.


**Model use and mandatory running-log record (owner clarification, 16 October 2026).** Use the supported ML/RL mechanisms when they are available for the exact sport, competition and endpoint. Whether a model exists or not, assign the reconciled permanent P-ID, append the researched game card to the active running mini-log, read it back and advance its footer. A missing sport-specific model must not leave an otherwise recordable game as intake-only, unissued or without an ID. With no verified model output, record RESEARCH_ONLY_NO_MODEL, the actual reason and supported analyst work; never invent model probabilities or receipts. Carry that same P-ID through verified canonical import; do not allocate another ID. Before an authorized import, the local card may truthfully say PENDING_IMPORT; that status never cancels its ID or running-log entry. Identity/allocation conflicts, frozen or inaccessible originals and real write failures still block only the affected mutation. Verified settlements remain available for future model development in both paths.

See [RETAIN-v1](RESEARCH_RETENTION_PROTOCOL.md). This is an editorial clarification of the existing two-path behavior; no model, numerical policy or format change.
