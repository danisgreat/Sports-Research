# PROMPT 4 — Canonical import with complete readback

**Mode:** CANONICAL_SETTLED_MINI_IMPORT. Run in the local checkout. Input: `<settlement folder>`. Writes: active Combined Log suffix; current GAME_LOG_STATUS_CURRENT rows; CURRENT_STATE; research/scoreboard/SCOREBOARD; one new `research/verification/mini_import_<range>_<date>-<run>/` folder containing inputs, plan, mapping and receipts. No rule changes, re-research, regrading or rewriting old reports/cards.

## 1. Read and inspect

Print the [reading receipt](README.md) after common controls, full input manifest/mapping/queue, frozen and settled minis, scoring, VERIFICATION_PROTOCOL §3, status, active log's dated opening and current tail/entries, relevant older event records and this prompt. Record cwd/branch/HEAD/status; preserve unrelated work. Fetch remote for publication planning without changing branches or overwriting local edits. Explain branch divergence before any dependent publication.

Reconcile current next ID and active path from CURRENT_STATE, current status section and actual canonical records/dated state addenda. A historical opening header may retain old IDs and retired commands; it is not current allocation authority. Snapshot the destination's entire original bytes for comparison, with count/end marker as supporting evidence. Authority mode is `LOCAL_WORKING_TREE` (CURRENT_RULES §0): print HEAD and every uncommitted control difference.

**Name the identity you are checking (R20).** Record:
- the raw source snapshot: SHA-256 and byte count of the settled mini's working bytes;
- the raw destination prefix: SHA-256 and byte count of the active log's working bytes before any append;
- the line-ending state of both (`git ls-files --eol` and a CRLF count).

Under `core.autocrlf=true` the committed blob is normalised to LF and is checked separately after commit. Copy imported cores byte-for-byte; if a normalised comparison is unavoidable, declare the transformation and keep the raw file.

## 2. Validate all inputs before changing canonical files

Require the exact frozen original; never reconstruct forecast bytes from summary. Confirm settled output begins with the exact frozen prefix. If only a settlement section exists, assemble a copy in the new report inputs and compare its prefix. Audit original-format card checks and settlement checks, recording historical gaps without inventing missing fields. Legacy VOID/no-evidence conventions remain literal and are flagged for a separate settlement-review task, not silently regraded during import.

Inventory every source card, carryover, addendum and settlement revision. Search all canonical logs/status by ID, event key and aliases. Plan actions independently:

| Source unit | Action |
|---|---|
| New event and next sequential working ID | NEW_CANONICAL_EVENT |
| Identical existing event/ID/core | ALREADY_IMPORTED_EXACT; still examine its addenda/settlements |
| Same ID with different event, same event with different ID, unexplained sequence gap | CONFLICT; stop dependent import, never renumber |
| Canonical/local carryover | Resolve parent; reference only; append only missing supported settlement revisions |
| Exact existing addendum/settlement | ALREADY_COMMITTED; no write |
| New addendum/revision with resolved parent | APPEND; keep original timestamp/content and supersession |

**Marker integrity before any write (R19).** Check every source block:
- each `BEGIN` has exactly one matching `END` with the same ID (and revision key where present);
- no block is nested inside another ID's block;
- no revision key repeats for an ID;
- each block's declared format is one of mini-log-2 to -7 or mini-settlement-2 to -6.

Legacy settlement markers without revision keys are accepted under their declared legacy format, and the wrapper records that format; legacy bytes are never rewritten. Any failure blocks the dependent import before mutation.

All source counts reconcile to dispositions; `new + exact + conflict = source cards`, not `new = all source cards`. Pending and evidence queues reconcile too. Validate the whole dependency set before starting an append. Write IMPORT_PLAN.md in the new report folder, including exact expected block markers/order and current-state changes. Conflict reporting does not permit a partial ID sequence.

## 3. Apply and recover idempotently

Copy complete inputs into the report folder.

**Recheck immediately before each mutation batch (R18).** Re-read HEAD, the active-log path, the destination's current byte count, SHA-256 and last marker, and the source inventory. Compare them with IMPORT_PLAN.md. If anything changed (another writer, a rollover, a new commit), stop and rebuild the plan against the new state; never append from the stale plan and never overwrite the other writer's work. Serialise local writers: one import at a time per active log.

Append new canonical-md-1 wrappers in ID order, preserving every original core byte; original mini remains retained in full. Append only missing addenda/settlements, including for already-imported cards. Non-terminal and terminal-unresolved records are importable research with their explicit queues; never certify them by import.

Maintain a source-block → canonical-block mapping including parent, source path, original revision, action and readback result. After each complete block, compare it to the planned source. Interrupted rerun compares actual blocks: exact complete blocks are skipped; a partial/mismatched block is reported and repaired only within the agent's known uncommitted suffix. Never reset a whole log or rewrite a committed block. New evidence after a committed import is a dated revision.

Update current status for new cards and changed carryovers; append/revise only the current administrative section, retaining historical snapshots. Next ID comes from the full canonical sequence, not blindly max ID in this input. Recompute scoreboard from original cards plus each contract key's effective revision (CURRENT_RULES §8; SCORING §7), using the correct version/cohort; baseline gaps stay missing. Update CURRENT_STATE's counts/queues and historical-versus-v10 separation. An exact repeated import with no new evidence plans zero canonical/state/scoreboard changes.

## 4. Verify and retain

Run VERIFICATION_PROTOCOL §3: complete original log prefix unchanged; end-only suffix and line endings; all card cores and every added block compared, not a three-card sample; one canonical card per new ID; no duplicate event; all source units accounted for; next ID/status/queues/scoreboard agree; scope respected. Print actual evidence for each. Check old log parts, issued-research files and unrelated work unchanged.

Write CANONICAL_IMPORT_REPORT.md, CANONICAL_ID_MAPPING.md, UNRESOLVED_POST_IMPORT.md and VERIFICATION_REPORT.md. Mark original mini CLOSED_IMPORTED only in a new receipt/pointer after every source unit has a verified destination or retained explicit disposition. Do not delete working or original minis automatically; unresolved evidence remains linked.

## 5. Publish and return

When this full prompt is invoked, commit the verified allowed paths and push to the instructed branch/main without force, unless the user requested local-only. Inspect staged diff, fetch remote after push, compare remote SHA and remote current-state/artifact contents. Concurrent remote change requires reconciliation preserving both histories; no silent force/reset.

Return input/output paths, HEAD before/commit/remote, new and existing IDs, added/skipped/conflicting blocks, all queue counts, preserved-byte/readback evidence, next ID, scoreboard coverage and publication status. Report partial/blocking work explicitly. Nothing is performance-certified.
