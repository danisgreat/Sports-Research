# Verification protocol

**Markdown only (CR-2026.10.09-R5).** Verification used to be a pipeline of programs: unit tests, custody and freeze verifiers, a canonical-log verifier, continuous integration. Those were removed on 2026-10-09 (last working state at commit `37203fc2b`). Verification is now a set of **hand checks that print their evidence**. The pre-rewrite page is kept in [archive/superseded_2026-10-09/VERIFICATION_PROTOCOL.md](archive/superseded_2026-10-09/VERIFICATION_PROTOCOL.md).

A passing check proves the thing it checks. It never proves the research was honest, the distribution sensible, the source true or the model skilful. Report failures as failures; never relax a check to make it pass.

## 1. Commands the repository agent may use

Reading and plain file commands only: `git status`, `git diff`, `git diff --numstat`, `git log`, `git ls-files`, `git show`, `ls`, `cp`, `grep`, `wc`, `cmp`, `head`, `tail`. No scripts are written into the repository, and no interpreter is run against its files.

## 2. Levels of verification

| Level | When | Checklist |
|---|---|---|
| Card | Before returning each card | Card self-audit C1-C20 ([CARD_AND_LOG_TEMPLATES.md](CARD_AND_LOG_TEMPLATES.md) §7) |
| Settlement | Before returning a settlement | Settlement self-audit S1-S13 (same file, §9) |
| Import | After appending to a Combined Log | Section 3 below |
| Rollover | After starting a new part | Section 4 below |
| Retrospective | Before publishing a report | Section 5 below |
| Repository | Before every push | Section 6 below |

## 3. Import checks (prompt 4)

Print each result with its evidence.

1. **Append-only.** For each Combined Log you edited: `git diff --numstat <file>` shows deleted lines = **0**. Any non-zero count means an earlier byte changed: restore the file and re-append.
2. **Frozen prefix.** The frozen mini is an exact prefix of the settled mini: compare the byte counts with `wc -c`, then `head -c <frozen bytes> <settled> | cmp - <frozen>` prints nothing.
3. **ID continuity.** Every working ID in the mini appears exactly once as a canonical block in the log: `grep -c "BEGIN CANONICAL RESEARCH P-NNN" <log>` is 1 for each. No ID is skipped, reused or renumbered. The new next ID equals the highest imported ID + 1.
4. **Duplicates.** No event key appears under two IDs: `grep` the event key in all Combined Logs and the status register.
5. **Verbatim.** For a sample of at least three cards, compare the pick table in the log with the one in the mini cell by cell.
6. **Status register.** The `Next canonical ID` line, the new rows and [CURRENT_STATE.md](CURRENT_STATE.md) agree.
7. **Scope.** `git status` shows changes only in the allowed paths: the active Combined Log, `GAME_LOG_STATUS_CURRENT.md`, `CURRENT_STATE.md`, `research/scoreboard/SCOREBOARD.md`, and the new `research/verification/mini_import_<P-AAA>_<P-BBB>_<date>/` folder.

## 4. Rollover checks (prompt 5)

1. Part N is unchanged except for the appended closure block (`git diff --numstat` deletions = 0).
2. Part N+1 exists once and contains a header and no card.
3. The next ID is identical before and after; the rollover consumed no ID.
4. [CURRENT_STATE.md](CURRENT_STATE.md), [GAME_LOG_STATUS_CURRENT.md](GAME_LOG_STATUS_CURRENT.md) and the continuity table in the new header all name Part N+1.

## 5. Retrospective checks (prompt 6)

1. The new-cohort and comparison-cohort ranges were written down before looking at results.
2. Every number in the report traces to a settled table; recompute five at random from the settlement blocks.
3. Only `research/verification/retrospective_<date>/`, the scoreboard and CURRENT_STATE changed. The Combined Logs, the ledger of cards and the rules are unchanged.

## 6. Repository checks before a push

1. `git status` lists only intended paths; nothing from `Previous Sports Results/_canonical/*.csv` (too large for GitHub) and no cache folders.
2. `git ls-files | grep -E "\.(py|json|jsonl|ipynb)$"` prints nothing: the repository holds Markdown, CSV and text.
3. Search the operating documents for instructions that need a program: `grep -rnE "python|py -3|research\.operations|\.json" README.md METHOD.md CURRENT_STATE.md CURRENT_RULES.md SELECTION_RULES.md CARD_AND_LOG_TEMPLATES.md SCORING_AND_VALIDATION.md VERIFICATION_PROTOCOL.md PROMPTS.md research/prompts` should print only the lines that describe the removal. Historical documents may still name removed tools; they are labelled historical.
4. Every link added in this change resolves to an existing file (open each).
5. The commit message states what changed and why; no history is rewritten and nothing is force-pushed.

## 7. Source and evidence verification

- A reachable page is not event-specific evidence. Open the exact field for the exact event.
- Distinct publishers are not independent lineages.
- Record source failures with time and reason. Do not fetch through an unauthorised route and never substitute different bytes for an unavailable page.
- Retained evidence is quoted in the card (`Evidence quotes`) and in the settlement Basis cell with the source and the time read. Hash receipts and stored response bodies no longer exist; the quote and the time are the audit trail.

## 8. What this cannot do

There is no machine check that a retained body matches a hash, that a log was not altered, or that a calculation was right. Protection against alteration is git history (every change is a commit; the previous commit is the comparison), the append-only rule and the numstat check. Protection against error is the printed arithmetic: another reader can redo it from the inputs on the page.
