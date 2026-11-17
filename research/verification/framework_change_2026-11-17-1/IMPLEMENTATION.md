# Implementation · v28.0 / CR-2026.11.17-R1 · 17 November 2026

Prompt 8, branch `fix/v28-review-fixes` from main `9d3ee0ec7`, merged through a pull request with the required `framework-validation` check. Owner order: "implement all of the fixes correctly", after a review of v27.0 (PRs #4–#7). Classification: statistical (two registered constants) plus bug fixes and records, so method, prompt and scoring versions move to MDS-2026.11.17-v28.0 / P-2026.11.17-v28.0 / SCV-2026.11.17-v19.

## Fixes

| # | Finding | Fix | Test |
|---|---|---|---|
| 1 | `historical-pre-event append` crashed on Windows (`import fcntl`); CI ran on Linux only | `ml/file_lock.py`: one OS lock (msvcrt on Windows, flock elsewhere) on a side file in the temporary folder, held only by a live process; used by `historical_pre_event.append_evidence` and `timing_corrections.locked`. A `windows-portability` CI job runs the lock, custody and historical tests on Windows | `test_v28_fixes.py`: no POSIX-only import outside the helper; a second writer is refused; a lock held by another live process is never taken over and is released when it dies. The two HPPV tests that failed on Windows now pass |
| 1a | A run binds the code's bytes, so the fix invalidates the committed run | New run `research/verification/hppv_runs/2026-11-17-1` with the fixed code; the initial run is unchanged and verifies at 8f2f38f | `test_committed_assessment_rebuilds_identically` (current run); `test_the_initial_run_differs_from_the_current_run_only_in_its_code_hash` |
| 2 | v27.0 constants (eight lambdas, 400 games) gave a calibrated 58–72% card about 72% power and a 55–65% card about 4%; no power figures were published | v28.0 registers lambdas (0.5, 0.7, 0.9) and a 600-game horizon before any real request or seal, with `ml one-chat power` and [POWER.csv](power/POWER.csv) | `test_registered_constants_match_the_published_plan`, `test_power_study_is_deterministic_and_reports_every_scenario`; the existing null-error and power tests use the new horizon |
| 3 | Local rehearsal seals and requests shared the registered staging area and pending refs | `STAGING` and `PENDING_REFS` are per seal branch; the registered branch keeps the original names | `test_staging_and_pending_refs_are_kept_per_seal_branch`, `test_a_rehearsal_seal_left_in_local_staging_is_invisible_to_the_registered_evaluation` |
| 4 | Every repository read downloaded GitHub's whole activity history; a failed fetch read as "no pushes" | Activity fetched lazily, once per read, only when a server time is needed; `github_push_activity` raises on failure, and `score` records it as a custody problem | `test_github_activity_is_fetched_only_when_a_server_time_is_needed_and_a_failure_is_explicit`, `test_a_failed_gh_call_raises_instead_of_reading_as_no_pushes` |
| 6 | Stale or contradictory text | ACTIVE_FILE_INDEX, CURRENT_STATE (label and horizon), external README, every live pointer to the v28 plan and brief, RULES_REFERENCE §0 (the two authorized workflows), CORE's archive rule (copy or permalink), HPPV README link, lost dashes in CHANGELOG, CURRENT_STATE and HYPOTHESIS_REGISTER, one_chat duplicate import and stale comments | link and prompt-consistency tests |
| 7 | Drop-workflow trust model undocumented | RUNBOOK §3a "Trust" paragraph | — |

Item 5 (more FACTS per card) needs no code change: chats must use [ONE_CHAT_BRIEF_v28.0](../../external/ONE_CHAT_BRIEF_v28.0.md) and the template, or the card is refused at seal.

## Not changed

Custody, eligibility, comparator, alpha, the practical threshold, card format, historical outputs, cards, grades and canonical IDs are unchanged. The v27.0 plan and brief are retained. The new CI job is not a required check: making it required is a repository-settings change for the owner.
