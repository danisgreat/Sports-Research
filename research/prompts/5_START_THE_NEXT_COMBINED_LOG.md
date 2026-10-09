# PROMPT 5 — START THE NEXT COMBINED PREDICTION LOG

**Run by:** Claude Code in a local checkout of the repository · **GitHub:** write (this rollover only) · **Mode:** `COMBINED_LOG_ROLLOVER`

The user authorises rolling the active Combined Prediction Log from Part N to Part N+1. A rollover only moves the destination for future canonical cards. It consumes **no** P-ID, changes **no** earlier byte and adds **no** card.

The architecture already separates the two kinds of custody:
- `research/src/combined_log.py` handles the **active log**: the configured `active_log` plus a per-part header receipt for every part.
- The **Part-6 legacy custody** (`LEGACY_PART6`) keeps the P-518 original-source block check.

`research/operations/rollover.py` automates the whole rollover. Do **not** hand-create the new file or edit any of these by hand:
- `research/current_combined_log.json`;
- the allocator;
- the logging code.

Run a rollover between mini imports, never while a mini import is half-done.

---

## 1. Authority and clean state

1. `git fetch`, check out the current `main` and record its 40-hex HEAD SHA. The working tree must be clean.
2. On Windows, use the normal checkout with `core.autocrlf=true`. On Linux or macOS, create a worktree with `git -c core.autocrlf=true worktree add <dir> main` and work there. Parts 1–5 and the root CSV are custody-hashed as CRLF. **Never** set `core.autocrlf` with `git config`, because the setting leaks into the shared configuration.
3. Read:
   - `METHOD.md`, `CURRENT_RULES.md` and `GAME_LOG_STATUS_CURRENT.md`;
   - `research/current_combined_log.json` and `research/src/combined_log.py`;
   - `research/operations/rollover.py` and `research/operations/log_card.py`;
   - `research/README.md`;
   - the selected control manifest.

## 2. Baseline

```powershell
py -3.14 -B -m research.operations.log_card verify
py -3.14 -B -m research.operations.log_card next-id
py -3.14 -B -m research.operations.control_freeze --verify
py -3.14 -B -m research.operations.verify_rollover
py -3.14 -B -m research.operations.verify_reconciliation
py -3.14 -B -m research.operations.verify_carryover_review
py -3.14 -B -m research.operations.verify_all_logs
py -3.14 -B -m research.operations.verify_custody
py -3.14 -B -m pytest -p no:cacheprovider research/tests research/operations -q
```

Save every result. A failure here is **pre-existing**. Report it, and never mask it as a rollover result.

If a canonical transaction is pending, stop. Recover it with `log_card recover` only after confirming that it is the expected transaction.

## 3. Plan (read-only)

```powershell
py -3.14 -B -m research.operations.rollover plan
```

Confirm each of these:
- `active_log` is Part N;
- `new_log` is Part N+1 and `new_log_exists` is `false`;
- `pending` is `false`;
- `next_id` equals the `log_card next-id` result and `GAME_LOG_STATUS_CURRENT.md`;
- `highest_committed` is the last ledger card;
- `first_in_active`–`last_in_active` matches the cards actually in Part N.

If any of these disagree, stop and report.

## 4. Apply

```powershell
py -3.14 -B -m research.operations.rollover apply --main-head <HEAD SHA from step 1> --carryover "<pointer to open PENDING_EVENT carryovers, or 'none open'>"
```

Under the ledger lock, `apply`:
1. Appends a dated closure block to Part N, `<!-- BEGIN ROLLOVER CLOSURE PART N -->`, which records:
   - the time and the main HEAD;
   - the range of cards in Part N;
   - the highest committed ID and the unchanged next ID;
   - the prefix length and SHA-256.

   Earlier bytes and Part N's header receipt are untouched.
2. Writes the Part N+1 header. It contains the status, opening time, method, control, freeze, previous part, highest and next ID with the note "consumes no ID", the reserved-ID note, the carryover pointer, SPORTS_ONLY / MARKET_BLIND, the certification disclaimer, a continuity table of every earlier part, and the logging, addendum and duplicate rules.
3. Updates `research/current_combined_log.json` to the new `active_log`. It keeps every earlier `log_headers` receipt and adds Part N+1's.
4. Adds `"prediction logs/PREDICTION_LOG_COMBINED_<N+1>.md" -text whitespace=cr-at-eol` to `.gitattributes`.
5. Proves the result:
   - the next ID is unchanged;
   - the ledger bytes are unchanged;
   - the active log resolves to Part N+1;
   - every card and addendum projection verifies;
   - Part N custody, Part N+1 custody and Part-6 legacy custody all pass.

   Then it refreshes `GAME_LOG_STATUS_CURRENT.md`.
6. Writes `research/verification/rollover_<date>_partN_to_<N+1>/rollover_receipt.json`.

If `apply` raises, nothing after the failing step has happened. Report the error, and do not hand-edit to finish the job.

## 5. Update the living documents and issue a new freeze

Part N leaves the freeze exclusion and becomes controlled history, so a new versioned control manifest is required. **Never edit an earlier manifest.**

1. Update only the living documents that name the active destination:
   - `METHOD.md`;
   - `CURRENT_RULES.md`;
   - `research/README.md`;
   - `CHANGELOG.md` (a dated entry).

   Historical statements such as "P-523–P-549 live in Part 6" stay as they are.
2. In `METHOD.md`, set `Active freeze: [CONTROL_MANIFEST_<YYYY-MM-DD>-<k>.md](CONTROL_MANIFEST_<YYYY-MM-DD>-<k>.md)`. Use the next unused suffix `k` for today.
3. Generate the freeze, then verify it:

```powershell
py -3.14 -B -m research.operations.control_freeze
py -3.14 -B -m research.operations.control_freeze --verify
py -3.14 -B -m research.operations.log_card refresh-status
```

`--verify` must report **0 mismatches**. Every controlled file must already be in its final form when you generate the freeze, because any later edit to a controlled file needs another new freeze.

## 6. Verify

Re-run every baseline command from step 2, then check all of the following:

| Check | Expected |
|---|---|
| `log_card next-id` | Same ID as before the rollover |
| `git diff --stat` | Only these paths changed: Part N (closure appended), the new Part N+1, `research/current_combined_log.json`, `.gitattributes`, `GAME_LOG_STATUS_CURRENT.md`, the receipt folder, the new manifest, and the updated living documents |
| Part N | Its pre-rollover bytes are an exact prefix (compare with the receipt's `previous_log_prefix_sha256`) |
| Part N+1 | Exists exactly once and contains no card |
| Ledger | Unchanged |
| Pending transactions | None |
| Status page | Names Part N+1 |
| `control_freeze --verify` | 0 mismatches |
| Baseline failures | Identical before and after; any new failure blocks publication |

The `research/operations/test_rollover.py` tests (run in step 2) already prove the invariants on fixtures. Do **not** commit a fake production card to test the first ID.

## 7. Publish

Commit everything as one change, for example `Roll Combined Prediction Log N to N+1; issue CONTROL_MANIFEST_<date>-<k>`. Push to `main`, or to the branch the user names, without force. Re-read the remote HEAD. Confirm that the remote `research/current_combined_log.json` and `GAME_LOG_STATUS_CURRENT.md` name Part N+1.

## 8. Report

```text
Main HEAD before / after:
Previous active log / new active log:
Highest committed canonical ID:
Next canonical ID before / after: <must be identical>
P-ID consumed by rollover: NO
Closure block SHA-256 / Part N prefix SHA-256:
New header bytes / SHA-256:
Files changed:
Legacy Part-6 custody: <pass/fail>
Part N and Part N+1 custody: <pass/fail>
New control manifest / --verify result:
Tests and verifiers: <each, with pre-existing vs new failures>
Commit SHA / publication status:
```

If any core check fails, say that the rollover is **not complete**. Do not claim success.
