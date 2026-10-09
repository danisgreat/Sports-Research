# PROMPT 5 — START THE NEXT COMBINED PREDICTION LOG

**Run by:** Claude Code in a local checkout of the repository · **GitHub:** write (this rollover only) · **Mode:** `COMBINED_LOG_ROLLOVER`

The user authorises rolling the active Combined Prediction Log from Part N to Part N+1. A rollover only moves the destination for future canonical cards. It consumes **no** P-ID, changes **no** earlier byte and adds **no** card. There is no rollover program: you create and edit Markdown with your file tools and use `git` and plain file commands only. Do not write scripts into the repository.

Run a rollover between mini imports, never while a mini import is half-done.

---

## 0. Reading gate

Print the **reading receipt** ([research/prompts/README.md](README.md)) after opening: [CURRENT_STATE.md](../../CURRENT_STATE.md), [METHOD.md](../../METHOD.md), [CURRENT_RULES.md](../../CURRENT_RULES.md) (§8 and §9), [CARD_AND_LOG_TEMPLATES.md](../../CARD_AND_LOG_TEMPLATES.md) (§8, rollover), [VERIFICATION_PROTOCOL.md](../../VERIFICATION_PROTOCOL.md) (§4), [GAME_LOG_STATUS_CURRENT.md](../../GAME_LOG_STATUS_CURRENT.md), and the header and end of the active Combined Log and of the previous rollover's header.

## 1. Authority and clean state

1. `git fetch`, check out the current `main` and record its 40-hex HEAD SHA. `git status` must show no changes in the paths you will edit.
2. The Combined Logs are stored with Windows line endings. Write every new line with the same ending as the file you extend (open it and check), and confirm with `git diff --numstat` that the active log shows 0 deleted lines after your edit. Never change a file's line endings wholesale.
3. Read CURRENT_STATE and the active log header. They must agree on the active log, the highest committed ID and the next ID. If they disagree, stop and report.

## 2. Baseline

Record for the active log (Part N): `wc -l`, `wc -c`, the last 3 lines, and the number of `BEGIN CANONICAL RESEARCH` markers. Record the highest committed ID and the next ID. If a mini import is half-done (a card appended without its status row), stop and finish or revert it first.

## 3. Plan (read-only)

Confirm and print each of these:
- the active log is Part N and `prediction logs/PREDICTION_LOG_COMBINED_<N+1>.md` does not exist;
- the next ID equals the status register line and CURRENT_STATE;
- the first and last canonical IDs in Part N match what the header range says;
- no pending half-import exists.

If any of these disagree, stop and report.

## 4. Apply

1. **Closure block.** Append to Part N (after its last block) a dated block:

```markdown
<!-- BEGIN ROLLOVER CLOSURE PART N -->
## Rollover closure — Part N — <YYYY-MM-DD>

Closed at <ISO 8601 with offset> on `main` at <HEAD SHA>. Cards in this part: P-AAA to P-BBB (<n> canonical entries). Highest committed ID: P-BBB. Next canonical ID: P-NNN (unchanged; this rollover consumed no ID). Part N before this block: <lines> lines. Part N+1 continues at [PREDICTION_LOG_COMBINED_<N+1>.md](PREDICTION_LOG_COMBINED_<N+1>.md).
<!-- END ROLLOVER CLOSURE PART N -->
```

2. **New part.** Create `prediction logs/PREDICTION_LOG_COMBINED_<N+1>.md` with this header, then the line `<!-- END ACTIVE COMBINED LOG HEADER -->`:
   - `# Combined Prediction Log <N+1>`
   - `**Status: ACTIVE FOR NEW CANONICAL RESEARCH.** SPORTS_ONLY / MARKET_BLIND.`
   - `Opened:` the time (Sydney and UTC), `Repository main at rollover:` the HEAD SHA, `Method:` and `Control:` from CURRENT_STATE.
   - `Previous active log:` a link to Part N with the committed range, and the note that P-518 to P-522 remain reserved and the Part-6 source block stays immutable.
   - `**Highest committed canonical ID: P-BBB. Next available canonical ID: P-NNN.** Creating this file consumes no ID. The first real committed new event receives the next ID; this header is not a forecast.`
   - `Unresolved carryover:` a pointer to the open `PENDING_EVENT` records, or `none open`.
   - The statement that research IDs identify retained work independently of calibration and certification, and that nothing is performance-certified.
   - A `## Continuity` table listing every earlier part (copy the previous header's table and add Part N).
   - A `## Canonical logging` section: append-only after the end marker; entries use the `canonical-md-1` format; a duplicate event key returns the existing ID; changed delivered content is a dated addendum under the original ID; never rewrite prior probabilities, ranks, cutoffs, native identities or operator terms.
3. **State.** Update CURRENT_STATE.md (`Active Combined Log`, previous parts), the first lines of GAME_LOG_STATUS_CURRENT.md (`Active Combined Log: ...`), and the "Previous active log" pointers that name the active log (search for the old file name in `README.md`, `CURRENT_RULES.md`, `research/prompts/`, `CARD_AND_LOG_TEMPLATES.md` and the examples, and change only live pointers; leave historical statements such as "P-523 to P-549 live in Part 6" alone).
4. **Changelog.** Add a dated entry to CHANGELOG.md (what rolled, the range, the commit that follows).
5. **Line endings.** If the repository's local attributes do not list the new part, tell the user that `.git/info/attributes` should get a `-text` line for it; do not create any non-Markdown file in the repository.

## 5. Verify

Print each result ([VERIFICATION_PROTOCOL.md](../../VERIFICATION_PROTOCOL.md) §4):

| Check | Expected |
|---|---|
| Next canonical ID before and after | Identical |
| `git diff --numstat` on Part N | Deleted lines = 0 (only the closure block added) |
| `wc -l` of Part N | Before + the closure block's lines |
| Part N+1 | Exists exactly once; contains the header and no card |
| Status register and CURRENT_STATE | Both name Part N+1 and the same next ID |
| `git status` | Only: Part N, the new Part N+1, GAME_LOG_STATUS_CURRENT.md, CURRENT_STATE.md, CHANGELOG.md and any live pointer you updated |

Any failure blocks publication.

## 6. Publish

Commit everything as one change, for example `Roll Combined Prediction Log N to N+1`. Push to `main` (or the branch the user names) **without force**. Re-read the remote HEAD and confirm that the remote CURRENT_STATE.md and GAME_LOG_STATUS_CURRENT.md name Part N+1.

## 7. Report

```text
READING RECEIPT: <as printed>
Main HEAD before / after:
Previous active log / new active log:
Highest committed canonical ID:
Next canonical ID before / after: <must be identical>
P-ID consumed by rollover: NO
Part N lines before / after: <…>
New header lines:
Files changed:
Checks: <each with its result>
Commit SHA / publication status:
```

If any core check fails, say that the rollover is **not complete**. Do not claim success.
