# Unresolved after import — 2026-10-09

Nothing below was resolved, graded or upgraded by this import.

## New events P-550..P-556 (7)

Sporting results are verified from official finals and graded WIN/LOSS in the imported addenda. All seven remain **`NOT_PERFORMANCE_ELIGIBLE` / `NOT_CERTIFIED`**: issue-time start and independent contemporaneous evidence missing, source custody incomplete, named-operator retirement/void/action terms never supplied, probabilities uncalibrated. Process taxonomy per card is in each addendum's R10. R11 learning hypotheses are `PROPOSED_NOT_TESTED`; no experiment or model change was run.

## Older carryover (65 records)

Unchanged and still open: 65 earlier canonical-reference IDs with unresolved identity/operator/certification fields, carried by `research/verification/carryover_review_2026-10-08/carryover.json` and the full list in `inputs/UNRESOLVED_CARRYOVER.md`. Total carry-forward obligations: 72 (65 + 7).

## Follow-ups needing a separate authorised pass (not done here)

1. **Stale local reservation.** `carryover.json` `local_reservations` (and `research/current_settlement_register.json`, which points to it) still describe P-550 as `LOCAL_ONLY_PENDING_IMPORT` with next local ID `P-551`. P-550 is now canonical and the next ID is P-557. These files are hash-pinned by the settlement register and were deliberately not edited; the allocator already removed the matching line from `GAME_LOG_STATUS_CURRENT.md`.
2. **Control manifest.** `control_freeze --verify` passes, so no new manifest was required. If the owner wants the freeze to reflect the new log tail, a new `CONTROL_MANIFEST` must be generated last, as a separate decision.
3. **Six IDs without heading-form entries** (P-217, P-234, P-235, P-341, P-342, P-430): pre-existing; documentary only.
4. **Working-tree state not part of this import:** modified `SOURCES.md` and `research/src/control_manifest.py`, and many untracked data/script files, belong to other work and were left unstaged.
5. **Clean-checkout caveat.** `verify_custody` and `verify_all_logs` read gitignored raw snapshot bodies (`research/data/raw/**`, `research/data/benchmark/source_snapshots/**`). A fresh clone without those local files fails those two commands regardless of this import; GitHub CI would hit the same pre-existing condition.
