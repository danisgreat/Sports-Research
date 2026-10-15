# Game/mini ML implementation audit and enforcement

Authority: LOCAL_WORKING_TREE, base main 72d00384147cefacdd8d82c0689ae391608ae39d, owner instruction 15 October 2026. [Proposal](CHANGE_PROPOSAL.md), [verification](VERIFICATION_REPORT.md), [per-file inventory](LOG_INVENTORY.csv), [strict protocol](../../../ML_EXECUTION_PROTOCOL.md).

## Audit of recorded execution

Read the complete text of all seven canonical Combined Logs and the 24 identified preserved mini/master/settlement snapshots in the tracked workspace, plus six existing format examples. LOG_INVENTORY.csv records each path, raw bytes/SHA-256, literal format tokens, marker/reference counts and current-policy/execution-path mentions. Counts of P references include repeated carryovers/settlements and are not event totals. There is no active Mini logs directory or research/primary_predictions bundle directory in this checkout at the audit snapshot. External minis/runs not supplied to this checkout are not inspected or assumed nonexistent.

| Canonical file | Current V1/V2/V3 primary-policy tokens | New execution receipt references | Finding |
|---|---:|---:|---|
| PREDICTION_LOG_COMBINED.md | 0 | 0 | No evidenced current primary-runtime execution in this file |
| PREDICTION_LOG_COMBINED_2.md | 0 | 0 | Same |
| PREDICTION_LOG_COMBINED_3.md | 0 | 0 | Same |
| PREDICTION_LOG_COMBINED_4.md | 0 | 0 | Same |
| PREDICTION_LOG_COMBINED_5.md | 0 | 0 | Same |
| PREDICTION_LOG_COMBINED_6.md | 0 | 0 | Same |
| PREDICTION_LOG_COMBINED_7.md | 0 | 0 | Same; preserves manual/diagnostic originals and prior formats |

All 24 preserved mini snapshots and six examples also contain zero searched current-primary policy tokens and zero EXECUTION.csv mentions. This is an execution-evidence inventory, not proof that no historical tool or external model ever ran, or a semantic re-audit of every historical forecast/source. Old rule versions are not retrospectively failed for lacking a newly introduced field. Do not rerun settled cards and label the resulting hindsight models pregame forecasts.

## Requirement-by-requirement findings and changes

| Requirement/stage | Before this change | Implemented now |
|---|---|---|
| Game fitting and ML probabilities | Actual three-expert primary runtime exists; bundle required by protocol/C19 | Preserve algorithm; require durable execute receipt and manifest/C21 on each new game |
| League with no baseline/profile/archive routing | Reviewed source route already fits its own league grid; no external baseline value is a runtime input | Explicit universal no-skip rule; executable missing-archive/profile regression and CLI example |
| Failed/unsupported run | CLI rejection, no standard attempt artifact | STARTED/INPUTS/EXECUTION records, actual stage/error, nonzero failure exit; no fabricated numeric output |
| Full-information sporting learning | Warm source-known-at loss ledgers, deduplication, eta and Hedge weights already implemented | Bind actual execution to bundle; require honest warm/feedback coverage and feedback disposition |
| Prompt1: all game sections | Eleven sport/general sections describe primary mixture but have no mandatory attempt manifest | Each of eleven step4 sections directly requires EXEC-v1, exact identity, receipt and coverage |
| Prompt2: start mini | Markdown mini only | New mini-log-8 plus header-only manifest; zero dummy fits/IDs; verify empty coverage |
| Prompt3: settle mini | Header requires primary settle, but numbered flow/checklist lacks explicit per-event feedback verification | Freeze original manifest, create effective manifest, actually settle eligible frozen grids, require S16 and feedback reason/output |
| Prompt4: canonical import | Retains original primary receipt/policy, no machine attempt coverage | Verify new-format manifest before import; preserve attempts/bundles/feedback custody and coverage; keep legacy gaps visible |
| Prompt5: rollover | Preserves model/shadow pointers generally | Explicit execution/feedback continuity and outstanding repair queue; no refit/copied forecasts |
| Prompt6: retrospective | Assisted cohorts and learning receipts requested | Per-game successful/failed/not-run and terminal-feedback coverage by exact scope; missing baseline only limits paired scores |
| Prompt7: archive recovery | Reviewed web metadata/history route exists | Explicit missing-baseline recovery/attempt handover; no borrowed league parameters |
| Prompt8: framework changes | Actual run/tests generally required | Explicit no-profile fit, durable failure, manifest, settle and future-consumption acceptance cases |
| Templates/common protocol | C19 checks model bundle, C14/C18 baseline missingness; C1-C20/S1-S15 | New fields/manifest, C21/S16, mini-log-8/mini-settlement-7 and current execution lifecycle example |
| Existing historical records | Immutable originals | All originals preserved, no probabilities/grades/IDs/baselines/times backfilled |

## Sport support versus mandatory attempts

The execution rule applies to every requested sport and competition. Actual numerical support remains scope-specific:

| Game section | Existing numerical engine/scope | Remaining limit |
|---|---|---|
| Basketball | Joint normal, exact configured full-game endpoint | No fitted lineup/player effects or unsupported phase/player adapters |
| Soccer | Dixon-Coles, regulation | First-half/corners need separate adapters; preserve supported full-game run |
| Ice hockey | Count, regulation fit with configured extra-time resolution | Exact endpoint/decision source fields required |
| Baseball | Count/negative-binomial with configured extras | Exact endpoint/decision source fields required |
| Cricket | Limited-overs full first innings | No multi-day, chase, phase or match-winner adapter |
| Tennis | No numerical adapter | Actual scope rejection retained; substantive analyst/qualitative research, no fake ML probability |
| Rugby league | Joint normal, exact configured endpoint | Local scoring/extra-time metadata required |
| Rugby union | Joint normal, exact configured endpoint | Local format/draw metadata required |
| AFL | Joint normal, exact configured endpoint | Competition/season/format source admission required |
| American football | Joint normal, exact configured endpoint | Exact extra-time/tie metadata required |
| Upcoming/general section | Dispatch to exact supported configuration | Field hockey/unsupported sport or endpoint rejects honestly |

This release does not implement new sport engines. The current learning mechanism is supervised score fitting plus full-information online expert aggregation, not a trained environment-control RL policy. If three-expert V3 cannot fit its own comparator/history, preserve the executed failure instead of silently substituting another algorithm. A genuinely inaccessible runtime remains an explicit noncompliant/incomplete execution gap; it cannot be signed off as a successful run. Independent research continues.

## Code and custody

ml/execution.py adds execute_files, verify_execution and verify_log. ml/primary.py exposes execute / verify-execution / verify-log while retaining predict/settle compatibility. The new execution wrapper calls the actual existing forecast path, not a mocked numeric substitute. Input raw and normalized hashes distinguish Windows source bytes from retained canonical CSVs. Successful attempts verify the immutable bundle and source stability; failed attempts retain actual errors. The manifest verifier checks identity/coverage, dispositions and retained feedback against original grids/evidence. Source truth, declared pending/blocked reasons, every narrative contract match and independent publication still require the existing human evidence checks.

Base committed document originals are preserved under archive/superseded_2026-10-15-7. Raw dirty prompt bytes and transformation helper remain external. Publication excludes pre-existing filled event inputs/availability wording; the local diff is preserved. Code lives only under ml/. No model-shadow output or historical dataset is regenerated/restamped.
