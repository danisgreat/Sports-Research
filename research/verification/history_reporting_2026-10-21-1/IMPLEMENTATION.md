# History-reporting repair — implementation

Scope: owner-confirmed **point 2**, reporting missing P-601–P-622. Local implementation on main from `476def8e2`; no commit or publication is implied. [Proposal](CHANGE_PROPOSAL.md).

## Result

The reproducible [final history report](HISTORY_FINAL/CARD_HISTORY.md) contains **2,424 rows from 621 cards, through P-622**. The prior tool returned 2,322 rows from 599 cards through P-600. The difference is exactly the latest import's 102 rows / 22 cards.

| Current cohort | Cards | Rows | Primary slots | Primary WIN / LOSS / PUSH | Decisive primary Brier | Frozen baseline coverage |
|---|---:|---:|---:|---|---:|---|
| ANALYST_PRIMARY_V1 | 11 | 50 | 22 | 11 / 10 / 1 | 0.204092523809524 (21 decisive rows) | 8 / 50 rows |
| RESEARCH_ONLY_NOT_PRIMARY | 11 | 52 | 0 | Not primary | Not computed | 0 / 52 rows |

All 102 new rows are checked against the preserved retrospective for contract, original rank, probability role, probability, grade, event date/week, revision, evidence wording and available baseline. The input's literal `R1 package` evidence wording is retained rather than replaced by the retrospective's abbreviated `R1`.

## Mechanism

- Discover `mini_import_*/EFFECTIVE_SETTLEMENT_ROWS.csv`, falling back to `IMPORTED_ROW_INVENTORY.csv` within each package. Read the four supported historical/local-key schemas; reject unsupported schemas, unknown local probability roles, duplicate effective contract keys and overlapping import packages that need reconciliation.
- Discover numbered Combined Log parts on each invocation, including two-digit parts. Preserve existing historical date behaviour while accepting later event years and four-digit P-IDs; historical birth/source dates before this card history began are excluded.
- Preserve research-only analyst values as diagnostics. They cannot contribute primary slots, primary proper scores or calibration. Valid unranked primary-card directions retain rank 0 and do not become top-two slots.
- Keep existing rank-log rows without double importing the same local-key contract. Preserve the imported probability role and reject grade/probability disagreements. The historical rank log is an input snapshot, not rewritten by this reporting command.
- Report cohort-level coverage, primary counts, Brier and baseline pairing. Pooled historical summaries remain explicitly descriptive across different policies and timing strata.
- Emit `CANONICAL_COVERAGE.csv`; canonical records with no contract rows are visibly queued for review. P-584 is the only such current record and remains pending; no forecast is fabricated.
- Hash all 19 input paths in the actual CLI run, including Part 8, current import rows and local-to-canonical mappings. Missing optional mapping files are recorded as MISSING. Reject changed inputs, newly discovered sources or generating source during the run.

## Measured verification

- Focused pre-final checks: **39 passed**. Final full workshop suite: **500 passed in 282.39 seconds**, using `python -m pytest ml/tests -q -p no:cacheprovider` with bytecode writes disabled. This includes receipt mutation, later-year/date, missing-canonical coverage and cohort-bounded regression checks. [Test result](TEST_RESULTS.txt).
- Actual CLI: `python -m ml card-history --out research/verification/history_reporting_2026-10-21-1/HISTORY_FINAL` → 2,424 rows / 621 cards.
- [Readback checks](READBACK_CHECKS.csv): all 19 receipt input states/hashes match current files; generating `ml/` digest matches `73e95ff94b2c978d56a193676ace502572ddfbe51b295d6569cf9470e4e27c27`.
- Exact historical comparison: the prior 2,322 rows retain identifiers, original ranks, contracts, grades, stated probabilities, baselines, primary-slot eligibility and event dates unchanged.
- [Preserved originals](PRESERVED_ORIGINALS.csv): four byte-preserved backups; each matches the baseline Git blob after LF normalisation. Raw backup byte counts/hashes are recorded separately.
- Canonical logs, GAME_PREDICTION_RANK_LOG.csv, IDs, source minis, settlements, learning store, model registry and training releases are untouched. The two unrelated initial untracked paths are preserved.

## Attempt history and limits

`HISTORY/` is an initial **withdrawn diagnostic run**, not the final output. Historical comparison found four P-524 rows using a player's 2001 birth date after a date-parser broadening. That run remains preserved with its original receipt. The parser was corrected and `HISTORY_FINAL/` regenerated; all original event dates now match. The full test run in progress at discovery was stopped and restarted after the correction.

This is a reporting repair, not predictive validation. Timing, operator definitions, source admission, sparse baseline coverage and the other framework-review findings are not retrospectively repaired by adding rows. Existing forecasts/grades/reports remain immutable. The reporting code changes the aggregate `ml/` digest; no old model release or artifact is re-hashed, regenerated or promoted. The historical rank-log refresh proposed alongside RET-17 remains a separate source-table maintenance task; current reporting no longer depends on it to see new imports.

Future import schemas need an explicit adapter and tests. Conflicting effective packages need an explicit revision/identity resolution rather than a filename-order winner. Dates and sports from older free-text records remain labelled heuristic/descriptive, with missingness retained.
