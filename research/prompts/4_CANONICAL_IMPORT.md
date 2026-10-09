# PROMPT 4 — CANONICAL IMPORT OF A SETTLED LOCAL MINI

**Run by:** Claude Code in a local checkout of the repository · **GitHub:** write (this import only) · **Mode:** `CANONICAL_SETTLED_MINI_IMPORT`

Import one settled local mini into the active Combined Prediction Log by hand edit. The frozen original mini holds the forecasts, the settled mini holds the settlements and retrospectives, and their working P-IDs are kept. There is no importer program: you read, compare and edit Markdown with your file tools and use `git` and plain file commands only. Do not write scripts into the repository and do not run an interpreter against it.

**Input folder:** `<path to "Mini Settlement - P-AAA to P-BBB - YYYY-MM-DD/">`

**Allowed writes:**
- the active Combined Log, **append-only**, after its last block;
- `GAME_LOG_STATUS_CURRENT.md` (new rows and the `Next canonical ID` line);
- `CURRENT_STATE.md` (next ID, highest committed ID, scoreboard headline);
- `research/scoreboard/SCOREBOARD.md` (updated by hand, [SCORING_AND_VALIDATION.md](../../SCORING_AND_VALIDATION.md) §7);
- one new folder `research/verification/mini_import_<P-AAA>_<P-BBB>_<YYYY-MM-DD>/` holding the import report, the ID mapping and a copy of the inputs.

Do not change methodology, rules, earlier forecasts, probabilities, ranks, timestamps or historical grades. Do not research, predict, re-settle or re-write retrospectives.

---

## 0. Reading gate

Print the **reading receipt** ([research/prompts/README.md](README.md)) after opening: [CURRENT_STATE.md](../../CURRENT_STATE.md), [METHOD.md](../../METHOD.md), [CURRENT_RULES.md](../../CURRENT_RULES.md) (Rules T2, R1, P4; §8 lifecycle; §9 custody), [SELECTION_RULES.md](../../SELECTION_RULES.md), [CARD_AND_LOG_TEMPLATES.md](../../CARD_AND_LOG_TEMPLATES.md) (§6 settled mini, §8 canonical entry format), [VERIFICATION_PROTOCOL.md](../../VERIFICATION_PROTOCOL.md) (§3 import checks), [SCORING_AND_VALIDATION.md](../../SCORING_AND_VALIDATION.md), [GAME_LOG_STATUS_CURRENT.md](../../GAME_LOG_STATUS_CURRENT.md) and the header and end of the active Combined Log.

## 1. Authority and clean state

1. `git fetch` and check out the current `main`; record the HEAD SHA. `git status` must show no changes inside the paths you will edit. Unrelated dirty work belongs to someone else: leave it exactly as it is and never stage it.
2. Read CURRENT_STATE and confirm it agrees with the first lines of GAME_LOG_STATUS_CURRENT.md (`Next canonical ID`) and with the active Combined Log header (`Highest committed canonical ID`, `Next available canonical ID`). If they disagree, stop and report.
3. **Baseline snapshot.** For the active Combined Log record: `wc -l`, `wc -c`, and the last 3 lines (`tail -n 3`). Record the number of `BEGIN CANONICAL RESEARCH` markers (`grep -c`). These are the "before" values for the append-only check.
4. The log is stored with Windows line endings. Before and after the edit, `git diff --numstat <log>` must show **0 deleted lines** after the edit.

## 2. Inputs

The folder must contain:
- `ORIGINAL_MINI/<frozen>.md` (exactly one file);
- `PREDICTION_MINI_SETTLED_<P-AAA>_<P-BBB>.md`;
- `SETTLEMENT_MANIFEST.md`;
- `LOCAL_ID_MAPPING.md`;
- `UNRESOLVED_CARRYOVER.md`.

If the frozen or settled file is missing, stop. **Never rebuild forecast bytes from a summary.** If the chat agent delivered only `SETTLEMENT_SECTION.md`, build the settled file now: copy the frozen file to `PREDICTION_MINI_SETTLED_<P-AAA>_<P-BBB>.md` with `cp`, then append the section.

## 3. Verify and plan (read-only)

Print each result with its evidence.

1. **Prefix.** `wc -c` the frozen file (N bytes), then `head -c N <settled> | cmp - <frozen>` prints nothing. The settled file continues with `# SETTLEMENT AND RETROSPECTIVES` and the tag `<!-- SETTLEMENT-FORMAT: mini-settlement-3 -->` (or `-2`).
2. **Frozen check.** The settlement header's `Frozen original check` (line count, first and last card IDs, footer line) matches the frozen file.
3. **Format.** Run the settlement self-audit S1 to S13 ([CARD_AND_LOG_TEMPLATES.md](../../CARD_AND_LOG_TEMPLATES.md) §9) on the settled file and the card self-audit C1 to C20 on every card. Stop on any failure you cannot attribute to a pre-existing, documented gap.
4. **Classify every card** by searching the Combined Logs and the status register (`grep -n "P-NNN"` and the event key):

| Classification | Meaning | Action |
|---|---|---|
| `NEW_CANONICAL_EVENT` | The event key is new and the working ID equals the next ID in sequence | Append |
| `ALREADY_IMPORTED_EXACT` | The same event key and ID are already in the log with identical card lines | Skip; consumes no ID |
| `IDENTITY_CONFLICT` | The event key is already canonical under another ID or other content, or the ID belongs to another event | **Stop** |
| `ID_COLLISION` | The working ID is not the next ID in sequence (a gap or an overlap) | **Stop**; never renumber |

5. **Classify every carryover:** `CARRYOVER_REFERENCE_ONLY` (already canonical with the same event key; settlement addendum only) or `SOURCE_CUSTODY_UNRESOLVED` (not in the log with this event key; **stop**).
6. **Classify every addendum:** `TO_APPEND` or `ALREADY_COMMITTED` (skip); an addendum whose parent card is blocked waits (`PARENT_BLOCKED`).
7. **Blocking list.** If any item is `IDENTITY_CONFLICT`, `ID_COLLISION` or `SOURCE_CUSTODY_UNRESOLVED`, stop before writing anything. Report each item and propose the reconciliation. The user decides. Do not guess, renumber, overwrite or bypass the sequence.
8. **Cross-check:** the number of new cards equals the cards in the mini; the highest ID + 1 equals the mini footer's `Next local working P-ID` (unless a later mini was already imported); the pending IDs equal `UNRESOLVED_CARRYOVER.md`.

Write the plan (the classification table and the checks) into `research/verification/mini_import_<P-AAA>_<P-BBB>_<date>/IMPORT_PLAN.md`.

## 4. Apply

Perform these steps in order. Use your file-edit tools; append at the end of the log by editing after its last block. Do not touch any earlier line.

1. **Copy inputs.** `cp` the input folder's files into `<report folder>/inputs/`.
2. **Cards.** For each `NEW_CANONICAL_EVENT`, in ID order, append one canonical entry in the exact `canonical-md-1` form ([CARD_AND_LOG_TEMPLATES.md](../../CARD_AND_LOG_TEMPLATES.md) §8): the `<!-- BEGIN CANONICAL RESEARCH P-NNN -->` marker, the heading `## P-NNN — <SPORT / LEAGUE> — <Event> — <YYYY-MM-DD>`, the import note, the card's lines **byte for byte** from `- **Working ID:**` to the integrity receipt, and the closing marker.
3. **Addenda.** Append each pre-settlement `ADDENDUM` block, in file order, as `<!-- BEGIN RESEARCH ADDENDUM P-NNN <YYYYMMDD>-<k> -->` … under its card's ID.
4. **Settlements.** Append each `SETTLED` settlement block, verbatim, as a dated addendum under its card's or carryover's ID, headed `**Final settlement (<date>).**`. A `PENDING_EVENT` card is imported without a settlement; the next mini carries it.
5. **Status register.** In GAME_LOG_STATUS_CURRENT.md add one row per new ID (`| **P-NNN** | <Event> | <tracking alias> | <status> |`) and set `Next canonical ID` to the highest imported ID + 1. Edit only those lines.
6. **Reports.** Write in the report folder: `CANONICAL_IMPORT_REPORT.md` (inputs, classification, appended blocks, the Rule T2 numbers, the checks), `CANONICAL_ID_MAPPING.csv` (`local_id,canonical_id,event_key,state`; local equals canonical) and `UNRESOLVED_POST_IMPORT.md`.

Addenda never consume an ID. If you stop part-way, do not edit anything else by hand: use `git diff <log>` to see exactly which lines you appended, report which blocks are complete, and remove only a partial block with your edit tool (never restore the whole file, which would discard other uncommitted work). Then continue from the first missing block.

### 4a. Refresh the state

1. **Scoreboard** (by hand, [SCORING_AND_VALIDATION.md](../../SCORING_AND_VALIDATION.md) §7): add each newly settled card to its cohort, recompute the counted wins, rates and Wilson intervals, the by-sport and by-month tables, the slot table and the Rank-1 failure classes. Spot-check five IDs against their settlement blocks.
2. **CURRENT_STATE.md:** set `Next canonical ID`, `Highest committed canonical ID`, the settlement note and the scoreboard headline. Nothing else states them.

## 5. Verify

Run [VERIFICATION_PROTOCOL.md](../../VERIFICATION_PROTOCOL.md) §3 and print each result:

1. **Append-only:** `git diff --numstat <log>` shows deleted lines = **0**; `wc -l` after equals `wc -l` before plus the lines you appended; the "before" tail lines are unchanged.
2. **IDs:** `grep -c "BEGIN CANONICAL RESEARCH P-NNN" <log>` is 1 for every new ID; no ID skipped, reused or renumbered; the new next ID equals the highest imported ID + 1; it equals the status register line and CURRENT_STATE.
3. **Duplicates:** no event key under two IDs.
4. **Verbatim:** compare the pick table of at least three cards in the log with the mini, cell by cell.
5. **Rule T2 numbers** in the import report equal the settlement section's own tallies.
6. **Scope:** `git status` and `git diff --stat` list only the allowed paths.
7. Nothing else changed: no earlier Combined Log, no rule file, no issued card text under `research/issued_research/`.

Report any failure as a failure. A new failure blocks publication until fixed by editing the new text only.

## 6. Write the verification record

In `<report folder>/VERIFICATION_REPORT.md` record: HEAD before and after, each check with its evidence, the next ID before and after, the line counts, and any pre-existing gap reported unchanged.

## 7. Publish

1. Review `git status` and `git diff --stat`. Only the allowed paths may change.
2. Commit with a message such as `Import settled local P-AAA–P-BBB cards, addenda and settlements`.
3. Push to `main` (or the branch the user names) **without force**.
4. Re-read the remote HEAD (`git log -1 origin/main`). Confirm that the remote `GAME_LOG_STATUS_CURRENT.md` shows the expected next ID.
5. If the push conflicts, stop and report. Do not rebase over, reset or force-push someone else's work.

## 8. Report

```text
READING RECEIPT: <as printed>
GitHub main HEAD before / after:
Active Combined Log: <lines and bytes before / after>
Input folder:
Cards examined: <n> · New canonical: <ids> · Already imported: <ids> · Blocked: <ids or none>
Carryover settlements appended: <ids or none>
Pre-settlement addenda appended: <n>
Settlement addenda appended: <n>
PENDING_EVENT cards imported without settlement (carry forward): <ids or none>
Counted (Rule T2): <wins>/<live top-two rows> · Rank 1 <W–L–V> · Rank 2 <W–L–V> · Hit@2 <n> · Mean NDCG@2 <x>
Scoreboard after import: gated counted cohort <wins>/<rows> (95% interval <lo>–<hi>) · RANK1_UNSTABLE cohort <wins>/<rows> · all forecast cards <wins>/<rows>
Rank-1 failure classes: <class × n>
Winner calls: <correct>/<issued>
Next canonical ID: <P-NNN>  (the FIRST working ID for the next mini, prompt 2)
Original forecasts changed: NO · Duplicate events created: NO · IDs renumbered: NO
Checks: append-only <…> · IDs <…> · duplicates <…> · verbatim <…> · T2 numbers <…> · scope <…>
Pre-existing gaps (unchanged):
Commit SHA / publication status:
Remaining blockers:
```

Imported records stay `RESEARCH_ONLY_NOT_CERTIFIED`. A verified sporting result is not operator certification or pregame performance eligibility. When the active Combined Log is approaching its practical size, or the user asks, run **prompt 5** before the next import.
