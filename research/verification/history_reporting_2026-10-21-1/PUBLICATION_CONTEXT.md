# Publication context — 21 October 2026

The owner subsequently authorised publication of the history-reporting repair together with a prompt-5 Part 8-to-Part 9 rollover. [Rollover receipt](../combined_rollover_2026-10-21-1/README.md).

`HISTORY_FINAL/` remains the exact **pre-rollover** run, based on HEAD `476def8e29420f66335c09de74134495e367d234` plus the local reporting-code repair. Its 19 input identities and 500-test verification are not re-stamped or backdated. The rollover subsequently changes Part 8 by an append-only closure, changes the live status pointer and creates header-only Part 9. Therefore the report's Part-8 and status hashes identify their earlier snapshots, not the later current bytes. Those exact earlier inputs are recoverable from the base Git commit and the external rollover snapshots; other input paths remain unchanged.

The reporting code discovers Part 9 and later numbered parts on future runs. No new report/model/learning execution was required for the rollover, and no old report, grade, calibration or predictive eligibility is upgraded. Source bytes for the reporting code are unchanged since the successful 500-test run. Exact archive/evidence bytes are preserved by committed -text attributes.

Actual publication success and commit SHA are recorded by Git and reported only after push/fresh-fetch readback; this note makes no claim that a future push has succeeded.
