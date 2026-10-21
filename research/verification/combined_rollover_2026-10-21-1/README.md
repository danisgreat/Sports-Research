# Combined Log rollover — Part 8 to Part 9

Applied **2026-10-21T02:30:23+11:00**, Australia/Sydney (AEDT). Owner invoked prompt 5 and explicitly authorised publication to main, including the immediately preceding history-reporting repair. LOCAL_WORKING_TREE, base main `476def8e29420f66335c09de74134495e367d234`; fresh origin/main matched. MDS/P v22.2 / CR-2026.10.17-R6 / SCV-v11 / SEL-v3; canonical-md-1 unchanged.

## Trigger and completed import

[Part 8](../../../prediction%20logs/PREDICTION_LOG_COMBINED_8.md) measured **851,514 working bytes** and **22 canonical originals P-601–P-622**. Neither default threshold (1.5 MB, 50 cards) was reached. **Explicit owner request** is the trigger; this is not a claim that a default threshold fired.

The latest import is complete: all 22 canonical wrappers and 28 addendum/settlement wrappers are balanced, and all **50 IMPORT_READBACK ranges** match their recorded lengths and hashes. The held local MELILL01-G0004 card is an intake defect without an allocated ID, not an unfinished canonical append. Open sporting/source/operator/custody queues do not prevent this completed-import rollover.

## Prefix and raw custody

The entire pre-closure Part 8 was saved outside the repository at `C:\Users\danie\Downloads\Sports_Research_rollover_2026-10-21-1\snapshots\prediction logs\PREDICTION_LOG_COMBINED_8.md`:

- Bytes: **851,514**.
- SHA-256: `2d799865a2346731e10b2f37f625a7dee1c1c4317f9925e2d42299f73fa379d2`.
- Final 4,096-byte tail SHA-256: `306e319840b8b09be70f22811687e68deef0704aef8e8ba4f48f856a07d070ae`.
- Pre-task Git blob: `19578585d0428475833f83e843a798a6503c5c21`; its bytes equal the raw snapshot.

The old file is exactly that full prefix plus one closure. Its historical opening and imported cores are unchanged. [Part 9](../../../prediction%20logs/PREDICTION_LOG_COMBINED_9.md) contains only a dated ACTIVE / OPENING_SNAPSHOT header, predecessor links and queue/custody pointers; **zero canonical/card/addendum/settlement blocks**. No placeholder forecast or copied card.

Committed -text attributes preserve Parts 8/9, live status, this receipt, and the history-repair evidence/backups exactly across clones. [FILE_IDENTITIES.csv](FILE_IDENTITIES.csv) distinguishes working bytes from staged/committed representation; equality is asserted only where the attributes require it. Receipt files with self-referential identities are excluded from their own identity table.

## Routing, queues and scope

Current state and the top status pointer now route to Part 9; README's live log index is updated. ACTIVE_FILE_INDEX already resolves the active path dynamically from CURRENT_STATE and needs no rewrite. All earlier dated opening/import/navigation snapshots retain their original paths and values.

Highest **P-622**, next **P-623**, reserved **P-518–P-522**, and retained inventory **138 records** are unchanged. [Queue continuity](QUEUE_CONTINUITY.md) carries pending P-584; P-620's pending winner/learning fields separately from terminal contracts; U-601–U-611; older open queues; and independent source/execution/learning custody. No settlement revision, source inquiry, grade, fit, feedback, model release, ID allocation or qualification is created.

The [history-reporting fix](../history_reporting_2026-10-21-1/IMPLEMENTATION.md) is included under the owner's publication instruction. Its production code is unchanged since the **500 passing tests**. Its generated report remains an immutable pre-rollover snapshot; [publication context](../history_reporting_2026-10-21-1/PUBLICATION_CONTEXT.md) explains the input hashes after the later closure/pointer changes. No model command was run for rollover.

## Checks and safe recovery

[Reading receipt](READING_RECEIPT.md) records the actual scope and sections. [VERIFICATION_CHECKS.csv](VERIFICATION_CHECKS.csv) records measured results. External `PLAN.json`, raw snapshots and a baseline hash inventory cover **2,668 pre-existing tracked/untracked files**; non-target bytes are compared after the rollover. Earlier code changes and owner material are preserved separately from the rollover write set.

The external `apply_rollover.py` rechecks HEAD, old bytes/hash/tail, next-ID context and live-pointer inputs before appending; it rechecks the closed old file and unchanged status before exclusively creating Part 9. An actual exact rerun returned **ALREADY_COMPLETED; zero writes**. Read-only injected cases for occupied successor, corrupted old prefix, partial closure and concurrent pointer drift each rejected before any write. They exercise the actual helper with filesystem writes prohibited, without corrupting repository records. A genuine partial/occupied state requires scoped recovery, never an overwrite or Part 10.

Git fetch initially failed on `refs/agents/desktop.ini`. **86** small files under `.git/refs` were verified as `[.ShellClassInfo]` metadata, moved to the external `quarantined_refs_metadata/` backup with path/hash manifest, and re-hashed. No actual ref/object/history was altered. Fetch then succeeded and origin/main matched the local base.

Publication stages only the reviewed rollover and history-fix paths, without force. Unrelated `BASKETBALL.txt` and `MINI LOGS TO BE SETTLED/` stay local. The final response reports the actual commit/push/fresh-fetch artifact result; this pre-publication receipt does not claim a future push succeeded.

Whitespace verification preserves original CRLF bytes: the default staged check reports inherited CRLF in the exact archived originals/status. `git -c core.whitespace=trailing-space,space-before-tab,cr-at-eol diff --cached --check` passes with no diagnostics. No original source bytes were normalised to suppress that inherited condition. Effective text attributes and raw/staged identities are verified separately.
