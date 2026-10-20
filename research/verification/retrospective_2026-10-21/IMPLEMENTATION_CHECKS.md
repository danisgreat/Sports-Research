# Checks actually run — retrospective 2026-10-21

All times AEDT on 2026-10-21 unless stated. Helper scripts (`extract.py`, `build_export.py`, `build_labels.py`, `cohort.py`) were kept in the session scratchpad, outside the repository. Repository code was run as `python -m ml …`.

| # | Check | Result |
|---|---|---|
| 1 | HEAD / remote before work | local `06f9538d…` = `git ls-remote origin refs/heads/main`. `git fetch` fails on Drive `desktop.ini` files in `.git/refs` (known local defect; not repaired here) |
| 2 | `python -m ml learning-status` before ingest | store view 6, all 1,686 settled MLB/NHL, every clock NOT_DUE, 0 settled since the last review |
| 3 | Export dry run on a store copy | observations 33, new events 21, results 21, corroborating 4, quarantined 0 |
| 4 | `python -m ml ingest add` (real store) | `ingest_seq` 7, export `af6e90e372ba…f358`, counts equal to the dry run; `git diff` on `research/learning_store/` is append-only (+84 lines, 0 deletions) |
| 5 | Exact re-ingest (copy of the post-ingest store) | 0 observations, 33 exact duplicates |
| 6 | As-of rebuild | `ingest history` NHL as of 2026-10-16T23:00Z: identical bytes before and after (`d4ccce646a32…8b6f`, 1,312 rows); as of 2026-10-21 it has 1,313 rows including NHL:2026020119 |
| 7 | `ml.research_learning retain` + `verify` | 22 candidates written, 22 verify OK (`LABELS_RETAINED_NOT_MODEL_FEEDBACK`) |
| 8 | `python -m ml primary settle` (ESPN 401892159 bundle) | written to `SHADOW_SETTLEMENT/`; bundle receipt verified by settle |
| 9 | `python -m ml prospective verify` (owner's mini shadow ledger) | chain intact, 54 rows |
| 10 | `python -m ml primary verify-execution` (same attempt) | FAILS: `KeyError: 'baseline_dependency'` (finding F-04) |
| 11 | `python -m ml registry verify` | chain intact, 16 entries |
| 12 | `python -m ml card-history` | 2,322 rows / 599 cards; inputs and hashes are in the HISTORY receipt |
| 13 | `python -m ml learning-status` after ingest and review rows | store view 7; INTERIM 21/100, COMPREHENSIVE 21/300, all sport/competition clocks NOT_DUE; new review rows do not reset clocks (levels USER_REQUEST / MINI_SETTLEMENT) |
| 14 | `python -m pytest ml/tests -q` | 486 passed (run before the summary-document edits) |
| 15 | Re-run after edits: prompt-consistency, learning-store, research-learning, learning-governance tests | 112 passed |
| 16 | Cohort reconciliation | COHORT_ROWS totals equal the import report (Rank 1 6W/5L, Rank 2 5W/5L/1P, Brier 0.2041); row sums 102 = 52 + 50 |
| 18 | Byte custody across clones | `.gitattributes` gains `research/training_candidates/** -text` and `research/verification/retrospective_2026-10-21/** -text`, matching the existing LEARN-v1 rules. Without them, a Windows clone with `autocrlf` would rewrite the hashed candidate and export bytes. This repository's `research/verification/** -text` rule lives only in the local `.git/info/attributes`. Staged blobs were re-hashed against every candidate RECEIPT. |
| 17 | P-606 score | ESPN scoreboard 116, ESPN summary linescore 23/27/29/37 = 116, ESPN box 2×37 + 14 + 28 = 116, NBA.com final 116 (its Q3 30 sums to 117, an internal inconsistency) |
