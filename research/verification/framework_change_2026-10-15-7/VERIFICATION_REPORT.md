# EXEC-v1 verification

Actual local verification on 15 October 2026. Authority LOCAL_WORKING_TREE; base main 72d00384147cefacdd8d82c0689ae391608ae39d plus this release's declared changes. Scope and limits are in [implementation](IMPLEMENTATION.md). No live game was issued and no P-ID allocated.

## Executed workshop checks

Final `python -m pytest ml/tests -q`: **267 passed in 100.83 seconds**. The execution tests cover actual model/Hedge fitting without archive/baseline discovery, Windows CRLF source normalization, retained unknown-scope/unsupported/missing/future-input failures, nonzero failed CLI status, immutable attempts, exact mini coverage, missing/duplicate/wrong-identity/tampered receipts, invalid manifest header, feedback disposition, frozen-grid feedback recomputation and subsequent-event feedback consumption. A required comparator fit failure retains a failed attempt and never invents a 50% baseline or silently changes V3.

Earlier intermediate checks: first execution-test run had a fixture-key typo (13 passed / 1 failed); corrected it and reran (14 passed). The first complete intermediate suite passed 265 checks. Added explicit header and comparator-failure cases and reran the final complete suite above. No unresolved test failures.

## Actual CLI integration, separate from pytest

[Transcript](SMOKE_TRANSCRIPT.txt) and [receipts summary](SMOKE_RESULTS.csv) come from an actual subprocess CLI flow. Fixture history is synthetic and labelled as such, with reviewed-source-shaped metadata/captures; it is not genuine sporting source admission or predictive evidence. Complete bulky inputs/grids remain external under C:/Users/danie/Downloads/ml_execution_rule_2026-10-15/synthetic_cli. The displayed transcript normalizes CRLF to LF and trims trailing display whitespace; it does not change the external execution artifacts. Published summaries retain actual paths, timestamps, code/HEAD and hashes; they are not a portable full bundle or an independently frozen prospective forecast.

| Step | Actual result |
|---|---|
| Execute EXAMPLE-PRIMARY-1, Basketball/EXAMPLE, no discovered archive/profile/TB-1 | Exit 0; real team models and fresh league comparator fitted; 79 admitted warm observations, 0 issued feedback observations |
| Verify execution | Exit 0, EXECUTED; immutable bundle verified |
| Settle frozen expert grids with synthetic final 110-95 | Exit 0; actual source-capture-bound feedback CSV retained |
| Verify mini/manifest and retained feedback | Exit 0; cards 1, executed 1, failed 0, feedback retained 1 |
| Execute EXAMPLE-PRIMARY-2 using available prior feedback | Exit 0; 79 warm observations and **1** verified feedback observation consumed |
| Attempt outcome-exposed EXAMPLE-FAILED | Exit 1; actual AdmissionError retained as FAILED/NO_RESULT; no numeric primary forecast |
| Verify rejected attempt | Exit 0 reporting FAILED, never success/numeric authorization |

Generating source SHA-256: a118b15002386102b9ff614905e9e175795fdcb03f33e451565166f9ad7bf556. The CLI run's repository HEAD is the base commit with this release's explicit uncommitted source changes, not a false claim that that base commit contains the new code. Current generating source was checked against these receipts before publication.

## Documents and custody

[Per-file inventory](LOG_INVENTORY.csv): seven canonical logs, 24 preserved mini/master/settlement snapshots and six historical format examples. Complete files inspected for current-policy/receipt references; zero searched current-primary tokens/execution receipts found. No primary event-bundle directory is present in this checkout. External unprovided runs are outside scope. This does not certify all legacy sources or imply no earlier tool ever ran.

[Custody checks](CUSTODY_CHECKS.txt): **777 pre-existing protected files unchanged** by raw SHA-256, including every canonical log, issued research, old verification record, retained mini and current game-status register in the protected snapshot. **23 archived originals** match exact base committed blobs. Six pre-existing prompt edit hunks remain unchanged relative to this release's clean published prompt; filled event inputs are excluded from the commit. No original probabilities/ranks/baselines/timestamps/grades/IDs are changed.

All eleven standalone sport/general step4 workflows directly contain the strict execution rule, and the canonical publishable prompt retains eleven inactive Upcoming blocks. All eight lifecycle prompts, current versions, templates and new example are aligned. New/changed relative links, markdown tables/fences, permitted types/paths, archive identities and staged whitespace are checked before commit; [document checks](DOCUMENT_CHECKS.txt) records final results. Archive originals keep base link context and are not rewritten to satisfy a current-link scan.

Release MDS-v16.0 / CR-R7 / P-v16.0 / PRIMARY control v3.2; mini-log-8 / mini-settlement-7. Numerical policy PRIMARY_HEDGE_MIX_V3, SCV-v10 and SEL-v3 unchanged. Legacy active minis keep their format and reconcile only new EXEC-v1 cards as a subset; historical cards are not retroactively assigned receipts.

## Remaining limits

The implemented mechanism is supervised score models plus full-information Hedge, not a trained environment-control RL agent. Unsupported tennis/field-hockey/multi-day/phase/player adapters remain unimplemented; they require actual failure evidence and complete independent research, not made-up numeric forecasts. Missing pre-existing baseline/profile never skips execution; insufficient admitted history or a failed required three-expert fit can still prevent a numeric result. Capability-blocked execution cannot pass as EXECUTED. Verification establishes custody/computed mechanics; sources, participant/contract correspondence, truthful pending/blocker reasons, known-at evidence and independent publication require their separate existing checks. Predictive calibration and prospective improvement remain unproven.
