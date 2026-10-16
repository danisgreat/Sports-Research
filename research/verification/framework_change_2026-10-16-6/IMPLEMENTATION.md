# Implementation: learning pipeline (LEARN-v1, P-2026.10.16-v19.1 / CR-2026.10.16-R5)

Authority LOCAL_WORKING_TREE, branch `main`, base `ba4fefaee4c1c63641c104a395edd987e022ab92` (equal to `origin/main` after fetch at the start of the task). Starting state: the unrelated tracked edit to `.gitignore` and existing untracked configuration, sync metadata (`desktop.ini`) and cache folders belong to other work and are left out of scope and unstaged. Dispositions for all 28 recommendations: [CHANGE_PROPOSAL](CHANGE_PROPOSAL.md). Verification: [VERIFICATION](VERIFICATION.md).

## Code (`ml/` only)

| Module | Purpose |
|---|---|
| `research_ingest.py` | LEARN-v1 store; identity/aliases; result and statistic revisions; availability snapshots; quarantine with reasons; atomic receipts; never reuses the sequence of an interrupted ingest; primary HISTORY bridge |
| `features.py` | FEAT-2026.10.16-v1 point-in-time features; frozen snapshots |
| `training_admission.py` | Immutable releases; candidate linkage; reproducible rebuild |
| `models/basketball_features.py` | BKB-FEATURE-RIDGE-C1 and the chronological ablation against exact V3 experts |
| `evaluation/v3_backtest.py` | V3-equivalent rolling-origin backtest and expert ledger |
| `hedge.py` | Learning-rate, forgetting, ESS-floor, AdaHedge, contextual study; regime alerts |
| `calibration.py` | Chronological calibration study; coherent grid raking |
| `evaluation/prospective.py` | Hash-chained shadow ledger; paired evaluation with breakdowns, power and dispositions |
| `learning_status.py` | Counters and review triggers |
| `registry.py` | Hash-chained model registry with transition rules |
| `run.py` | `python -m ml <command>` dispatch for the above |

`primary.py`, `tennis_primary.py`, `research_learning.py`, `execution.py` and every existing model are unchanged. The runtime source hash changes for new runs because new files were added under `ml/`. Existing bundles keep their recorded hashes; nothing is restamped or regenerated.

**Tests (new):** `test_learning_store.py`, `test_learning_models.py`, `test_learning_governance.py`, `test_learning_lifecycle.py`, `test_prompt_consistency.py`, plus the fixture helper `learning_fixtures.py`. All use synthetic EXAMPLE data and throwaway IDs (P-900010 only inside temporary folders).

## Data and governance files

- `research/model_registry/MODEL_REGISTRY.csv`: eight entries written by `registry.append`, recorded from Git history: PRIMARY_EXP3_V1 (a826cf6c6 → retired 869a4776e), PRIMARY_HEDGE_MIX_V2 (869a4776e → retired 7b60dc106), PRIMARY_HEDGE_MIX_V3 (7b60dc106, AUTHORISED_EXPERIMENTAL_PRIMARY), TENNIS_EXPERIMENTAL_HEDGE_V1 (92129032c/ba4fefaee), ML_WORKSHOP_R1 (980e60178, HISTORICAL_BACKTEST), BKB-FEATURE-RIDGE-C1 (this change). `recorded_at` is the actual recording time; the notes give the original dates. The one-off seeding script stayed outside the repository.
- `research/learning_status/REVIEW_LOG.csv` (header only) and READMEs for `research/learning_store/`, `research/learning_status/`, `research/prospective/` and `research/training_releases/`. The store, releases and shadow ledger are empty at release.
- `.gitattributes`: `-text` for the five LEARN-v1 folders, so append-only and hash-chained CSVs keep exact LF bytes on Windows clones.

## Documents

- New: [LEARNING_PIPELINE_PROTOCOL](../../../LEARNING_PIPELINE_PROTOCOL.md) and [research/prompts/DEPENDENCY_MAP.md](../../prompts/DEPENDENCY_MAP.md).
- Prompt 1: the header version and Writes line now include RESEARCH_EXPORT, and a LEARN-v1 banner was added. One identical **Structured research export (LEARN-v1)** paragraph sits in each of the eleven sport/general workflows, before its mandatory-output paragraph. One basketball sentence states that the feature challenger is shadow-only. **All eleven owner-entered Upcoming game blocks, from their heading to the line before the first Read paragraph, are byte-identical to HEAD.** That includes the populated basketball block (Aanekosken Huima vs Lappeenrannan NMKY).
- Prompts 3/4/6/8 gain learning accounting, the training-data handoff, evaluation levels and dispositions, and the promotion gates. Prompt 6's trigger line adds the learning-status triggers. COMMON_OPERATING_PROTOCOL and the prompt README describe the lanes. Prompts 2, 5 and 7 only change version.
- Current controls aligned to MDS/P v19.1 / CR-R5: CURRENT_RULES (new R35 learning-pipeline rule, navigation), CURRENT_STATE (current release, versions table, learning-pipeline row), METHOD (step 10), PRIMARY_PREDICTION_PROTOCOL §7, HISTORICAL_SOURCE_PROTOCOL §5, RESEARCH_RETENTION_PROTOCOL (candidate-to-training admission), VERIFICATION_PROTOCOL (LEARN-v1 checks), CONTRIBUTING (permitted learning locations, CI owner decision), README, PROMPTS, ACTIVE_FILE_INDEX and ml/README. Version-only alignment: CARD_AND_LOG_TEMPLATES, GITHUB_REFERENCE_PROTOCOL, ML_EXECUTION_PROTOCOL, MINI_LOG_IDENTITY_PROTOCOL, RESEARCH_COMPLETION_PROTOCOL and RESEARCH_EXHAUSTIVENESS_PROTOCOL.
- Originals: [archive/superseded_2026-10-16-6/](../../../archive/superseded_2026-10-16-6/ARCHIVE_HASHES.csv) holds the exact HEAD blobs of all 29 changed operating files, with their SHA-256 values and the working-tree hash before editing. `ml/README.md` and `.gitattributes` were CRLF in the working tree and LF in the blob; their content is otherwise equal.

## Not changed and not claimed

PRIMARY_HEDGE_MIX_V3 (experts, η, warm start, feedback, selection), scoring, card/mini/settlement formats, highest P-600 / next P-601, every log, settlement, scoreboard, generated model artifact and issued record. No real-data ingest, ablation, backtest, study, calibration or shadow has been run. No model is promoted or qualified. CI and branch protection remain owner decisions.
