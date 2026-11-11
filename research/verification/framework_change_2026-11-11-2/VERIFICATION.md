# Verification - v24.14 / CR-2026.11.11-R2

## Executed full regression

An isolated clean Git worktree at validation snapshot 5c1b12251b122ad1f929463eee1285f5dca30907 ran:

    python -B -m pytest ml/tests -q -p no:cacheprovider --tb=short --durations=8

Result: **843 passed, 8 warnings in 601.72 seconds (10:01)**, exit code 0. Exact output: [FROZEN_FULL_SUITE.txt](FROZEN_FULL_SUITE.txt). The eight RuntimeWarnings come from the synthetic constant-probability calibration case in the cohort-floor test; no real-sport calibration or qualification is claimed. The frozen core metrics implementation was not changed.

The earlier mutable-checkout run was not treated as a pass: it detected prompt-table version mismatches and one generating-source-changed ingestion guard. The prompt table was corrected; the final complete run used the isolated immutable snapshot so authoring could not change its source. Focused current-version regressions also passed (141 checks), including all negative reproductions, real five-lane intake/correction, exact receipt verification, mini append, learning/ledger/card binding, settlement, nonnumeric research retention and stable evaluation stopping.

## Exact source and custody

VALIDATED_CODE_IDENTITY.csv records every ml Python file and verifies that final executable source bytes equal the successfully tested snapshot. Post-test additions are verification artifacts and explicit CRLF whitespace interpretation in .gitattributes; no executable source or shared reference/model parameter changes were made after the snapshot.

CUSTODY_CHECKS.csv contains 195 passing checks, including all **181 protected files** under historical Combined Logs, issued originals, active minis, learning store and prospective ledgers. Raw SHA-256 values were checked again after the run. The frozen core distributions/metrics and shared competition reference table match the original HEAD bytes. No canonical ID, card, probability, grade, historical player availability or source clock was altered.

The archive contains **104 retained originals** plus its inventories. Every retained original was compared to its staged Git blob by raw SHA-256. New -text rules preserve archive, source/evidence and upload bytes across clones. ARTIFACTS.csv uses explicitly documented canonical-LF text hashes; raw returned originals, mini prefixes and lineage notes remain raw-byte hashes.

## Package and independent execution

- external package-check passes the complete versioned upload package, matching kit versions and unexpired reader decisions. PACKAGE_SHA256.csv gives the raw file hashes.
- The standalone sr_kit.py was copied outside the repository and run under Python isolated mode (-I), with only the upload parameter files and installed numpy/scipy. It produced coherent EXAMPLE W/P/L and SR-KIT-v24.14 receipt output.
- Current protocol/profile/brief/evaluation/report links resolve. Existing access/source observations are retained byte-for-byte with their original observation/expiry times; no new network audit is claimed.
- Retained study outputs match their original external hashes; soccer MATCHES.csv matches the input hash frozen in the retained DECISION.csv. Copying development outputs does not qualify a simulator.
- MODEL_SCOPE_CHECKS.csv confirms NBA and NHL match their original frozen cycle code; MLB retains its pre-existing stale code status. No model is promoted.
- LEARNING_READINESS.csv records actual data: 5,402 stored events, zero stored player-availability rows and zero current structured research logs. Feature evidence remains incomplete and predictive qualification UNPROVEN.

## Commit and scope

All intended paths are individually enumerated for staging. Historical originals were preserved; the inspected tree contains only permitted Markdown/CSV/text plus Python under ml. Strict staged whitespace checks apply to authored changes; any byte-exact archival whitespace is retained and recorded rather than normalized. The owner requested a local commit. Remote publication and actual ChatGPT sandbox/account operation are separate from these local checks and are not claimed.


Final staged review: strict authored-path whitespace check passed. Six inherited archive whitespace notices are retained, enumerated in ARCHIVE_WHITESPACE_NOTICES.csv and covered by raw archive/Git-blob hashes. All 138 executable Python files match the successfully tested snapshot byte-for-byte. No unexpected or unrelated paths were present in the final staged set.
