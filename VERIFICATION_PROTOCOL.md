# Verification protocol

**CR-2026.10.11-R1.** Markdown/CSV/text only. Checks establish their stated properties, never predictive skill. Use plain file/git commands and transparent arithmetic; do not add a validator runtime. Print `Check | PASS/FAIL/NOT_VERIFIED/N/A | evidence | limitation`.

## 1. Before changes

Record cwd, branch, HEAD, current status and intended paths. Read the task's authority and preserve unrelated modifications. Inspect actual line endings and source contents. Do not blindly checkout, pull, reset, restore whole files or stage all paths. Read-only missing inputs block only dependent actions.

## 2. Card and settlement

Run C1–C16 and S1–S12 in [CARD_AND_LOG_TEMPLATES](CARD_AND_LOG_TEMPLATES.md), with actual arithmetic and readback. Retain missing values honestly. A negative fixture must fail the relevant check; do not claim checks are executed merely because the checklist is present.

## 3. Import

1. Reconcile current state/status with canonical blocks and dated changes; opening headers are historical.
2. Exact frozen mini prefix in settled file, actual bytes and line endings; line counts alone insufficient.
3. Inventory equals new + exact existing + conflicts for cards; separately account for every carryover/addendum/settlement. Existing cards may still need new addenda.
4. Compare every imported original core and appended source block, not a sample. Marker counts, event identity, contract/rank/p/baseline/expected score/cutoff and source provenance agree.
5. Compare complete pre-import log prefix byte-for-byte; appended suffix only. Numstat deleted=0 and end-only diff hunks are supporting checks, not substitutes.
6. Sequential new IDs, existing IDs preserved, reserved IDs untouched. Addenda and reruns consume none. Replay of an exact completed import plans zero changes.
7. Status/next ID/settlement queues/scoreboard reconcile; no timestamp or performance upgrade from import.
8. Partial-write recovery uses a source-to-destination block map. Identical completed blocks are skipped; conflicting or partial blocks block further mutation until scoped recovery.

## 4. Rollover

Old part is exact original prefix plus closure; new part contains only header/continuity/queue pointers. Next ID before/after identical; zero forecast blocks. Current state/status name the new part; opening header is explicitly dated. Rerun recognizes existing exact closure/new header; no duplicate closure or part.

## 5. Retrospective and archive

Retrospective: scope and prior exposure disclosed; full row inventory reconciles all totals; original and amended settlements not double-counted; ranks/shadows/timing/policy cohorts separated; baseline coverage and missingness shown. Allowed writes: new report folder, scoreboard, CURRENT_STATE, dated hypotheses and CHANGELOG only. No old report or log mutation.

Archive: logical CSV records counted with CSV-aware file facilities or an explicit verified no-embedded-newline convention, not blindly physical lines minus one. Exact headers/types, event keys, doubleheaders, dates, status/endpoint, known zero versus blank, totals/margins, coverage against official schedule and source provenance checked. A sample verifies only the sample; publish unchecked remainder and never call partial coverage complete.

## 6. Framework release and publication

Archive replaced files from the base commit before editing. Check all eight task contracts, every new/changed relative link, consistent method/control/scoring/format versions, examples versus templates, old-format migration and edge cases. Scan live instructions for contradictions and removed-tool dependencies, distinguishing historical citations from commands. New files must be permitted text types; no retired runtime is restored.

Compare archived originals to the base revision and confirm issued logs, raw datasets, original sources and dated reports unchanged. Review full diff and staged paths. `git diff --check` must pass. Stage only intended paths; inspect staged status/stat/diff. Commit once checks pass; push without force only under task authorization. Fetch the destination ref afterwards, compare remote SHA with the commit and verify remote artifact contents. Local tracking refs without a fresh fetch are insufficient. Record what was committed/pushed and any unrelated remaining work.

## 7. Limits

A byte comparison proves identity, not source truth. A git SHA is not proof a card was issued before kickoff. A source quotation is not independently audited custody. Correct arithmetic is not a fitted model or calibrated probability. A plausible synthetic example is not live sports validation. Missing evidence must remain visible through every step.
