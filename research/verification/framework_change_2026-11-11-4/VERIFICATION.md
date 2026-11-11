# Verification - ASSESS-100

Executed results are appended during this implementation. No unexecuted check is a pass.

## Complete isolated regression

Snapshot **61e4110d9520c957d54c9c8d342780c5779edb12**, detached clean worktree, command:

    python -B -m pytest ml/tests -q -p no:cacheprovider --tb=short --durations=8

**883 passed in 843.93 seconds (14:03), exit 0; no warnings reported.** FROZEN_FULL_SUITE.txt retains the readable transcript; TEST_RECEIPT.csv records the original PowerShell UTF-16 log hash and retained UTF-8 hash.

All **143 executable Python files** match the successfully tested snapshot by raw SHA-256. No executable changes were made after the snapshot. Later writes are implementation/verification evidence only.

The new regressions verify 100 games on a single day inside an unfinished week are READY immediately; 99 games remain insufficient even with multiple contracts; pending shared contracts, future-unavailable outcomes and all-push games do not inflate eligibility; settlement ordering selects exactly 100 games; cohort reuse preserves the exact original and rejects tampering; contract averaging does not multiply the event count; and legacy week-based experiments are unchanged. The earlier shared-scorer prototype triggered the model-state integrity check; the final dedicated assessor preserves the original legacy scorer bytes and the full suite passes.

## Custody and compatibility

- **184 protected files** preserve exact bytes: Combined Logs, active minis, issued originals, learning store, prospective ledgers and model core.
- **39 archived originals** match their pre-edit raw inventories and staged Git-blob readback. One inherited archive EOF-whitespace notice is retained rather than changing the original; strict authored-path whitespace passes.
- The legacy ml/evaluation/prospective.py is byte-for-byte unchanged. FORECAST_IDENTITY_CHECKS.csv confirms seven baseline model-core/legacy-scorer/kit/reference inputs retain canonical identity. The generated model state remains consistent.
- No forecast/card/grade/canonical ID, reference parameter, kit/profile version, existing model release, source clock or historical hypothesis registration is rewritten. Forecast identities remain v24.15; assessment is EXT-EVAL-v2 under governance release v24.16 / CR-2026.11.11-R4 and SCV-v13.
- Current prompt suite P-2026.11.11-v24.14, dependency links, CLI --cohort entry point and the unchanged seven-file upload package were checked. No calendar minimum remains in the current event assessor; the older week-based scorer remains outside that call path.

## Interpretation and publication

These are offline EXAMPLE mechanics, not evidence of actual predictive improvement. At 100 games READY means the assessment is available; calibration, uncertainty, dependence and publication/source audits still determine what can be concluded. No model is promoted automatically.

The final commit and live main SHA are verified after commit/push and returned with the handoff. Publication has no invented self-referential commit field in this report. The OneDrive checkout is retained as a mirror when safely fast-forwardable.
