# Verification report — canonical import P-556 to P-579 (2026-10-11)

Hand checks with printed evidence (VERIFICATION_PROTOCOL §3 and §6). Commands: `git`, `wc`, `cmp`, `grep`, `head`, `tail`, `cp`, run against the repository; block assembly and arithmetic ran on scratch copies outside it.

| Item | Before | After |
|---|---|---|
| `main` HEAD | `33d0ea0c1c70056db7c7fb0a07dec77a633e573f` | the import commit (its SHA is reported in the session's final report; a file cannot contain its own commit hash) |
| Next canonical ID | P-557 | **P-580** |
| Highest committed ID | P-556 | P-579 |
| Combined Log 7 | 4,865 lines, 646,033 bytes, 7 canonical markers | 8,718 lines, 1,255,058 bytes, 30 canonical markers |

## §3 Import checks

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Append-only | PASS | `git diff --numstat` on Combined Log 7: `3853 0` (0 deleted). The first 646,033 bytes are identical to `HEAD:prediction logs/PREDICTION_LOG_COMBINED_7.md` (`cmp` silent). The "before" last 3 lines are unchanged at lines 4,863–4,865. 4,865 + 3,853 = 8,718 lines; 646,033 + 609,025 = 1,255,058 bytes. |
| 2 | Frozen prefix | PASS | `head -c 593775 <settled> \| cmp - <frozen>` prints nothing; frozen SHA-256 `3a406f539b43c982d1bfa8274d18be0d0670e73a59b10944ab6d90c5d48cc875` equals the settlement header and manifest. |
| 3 | ID continuity | PASS | `grep -c "BEGIN CANONICAL RESEARCH P-NNN"` = 1 for each of P-557 to P-579 (23 IDs, none skipped, reused or renumbered). New next ID P-580 = P-579 + 1 = the mini footer's `Next local working P-ID`. |
| 4 | Duplicates | PASS | Each of the 23 event keys occurs in Combined Log 7 only, and every occurrence lies inside its own ID's blocks (owner per key = its own ID); none occurs in Parts 1–6 or under another ID. |
| 5 | Verbatim | PASS | The whole appended region (lines 4,866–8,718), with CRs removed, is byte-identical to the scratch build, and in the build all 44 blocks were compared with their source slices: 23 card bodies (every pick table and every `Expected score` bullet included), 20 settlement blocks and the A8 addendum — 44 of 44 identical. The P-572–P-579 cards and the A8 addendum also equal the separate original files in `inputs/SOURCE_CARDS_ORIGINAL/`. |
| 6 | Status register | PASS | `GAME_LOG_STATUS_CURRENT.md` line 4 `Next canonical ID: P-580`, CURRENT_STATE `Next canonical ID **P-580**`, `Highest committed canonical ID **P-579**`; the 23 new rows equal the generated rows. `git diff --numstat`: `25 2`. Untouched regions are byte-identical to HEAD (the register mixes CRLF and LF lines; both were preserved). |
| 7 | Scope | PASS | `git status` lists only: Combined Log 7, `GAME_LOG_STATUS_CURRENT.md`, `CURRENT_STATE.md`, `research/scoreboard/SCOREBOARD.md`, and this new folder. |
| — | Rule T2 numbers | PASS | Re-derived from the appended blocks: P-557–P-576 counted 34/40, Rank 1 16–4–0, Rank 2 18–2–0, Hit@2 20/20, mean NDCG@2 0.8387, winners 10/20. The P-572–P-576 subtotal (9/10; Rank 1 4/5; Rank 2 5/5; NDCG@2 0.8774; winners 2/5) equals the settlement section's own tallies. |
| — | Nothing else changed | PASS | Parts 1–6: `git diff --stat` empty. No rule, method, prompt or issued-card file changed (`research/issued_research/` untouched). |

## §6 Repository checks before the push

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Intended paths only | PASS | as §3.7; nothing under `Previous Sports Results/_canonical/`, no cache folders |
| 2 | No code or JSON | PASS | `git ls-files \| grep -E "\.(py\|json\|jsonl\|ipynb)$"` prints nothing; the new files are `.md` and one `.csv` |
| 3 | No program instructions added | PASS | 0 added lines in the changed operating documents match `python\|py -3\|research\.operations\|\.json` |
| 4 | Links resolve | PASS | every link added (this folder's files, `inputs/`, the carryover review report) opens |
| 5 | Commit | — | one descriptive commit; no history rewrite, no force push |

## Scoreboard spot check (SCORING_AND_VALIDATION §7.6)

P-559 TOP2_SPLIT (Rank 1 WIN, Rank 2 LOSS; evidence B), P-564 TOP2_SPLIT (LOSS, WIN; C; deep retrospection present), P-570 TOP2_SPLIT (WIN, LOSS; A), P-574 TOP2_ALL_WON (WIN, WIN; A), P-576 TOP2_SPLIT (LOSS, WIN; A; deep retrospection present). All agree with the scoreboard tallies.

## Deviations and pre-existing gaps (reported unchanged)

- **Part 7 header line 10** (P-549 / P-550) disagrees with CURRENT_STATE; reported at step 1.2, user instructed the import to proceed; header left untouched as the immutable opening header (see IMPORT_PLAN.md).
- **Append method**: the prompt asks for the file-edit tool; the 609,025-byte append was made with one plain file concatenation of a pre-verified build so that no card text was retyped. The status register was rebuilt the same way after the edit tool normalised its mixed line endings (first attempt `893 870`, reverted; final `25 2`).
- **Line endings**: appended text converted LF → CRLF to match the log's stored form; no other byte differs.
- **Packet format**: compiled master of four earlier minis; P-557–P-571 settlements sit in the frozen prefix; nonstandard settlement-section heading and tag. All custody checks pass.
- Card-level limitations carried as written (see CANONICAL_IMPORT_REPORT.md).
