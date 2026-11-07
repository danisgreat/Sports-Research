# Consolidation — MDS/P v24.2 / CR-2026.11.07-R2 (FORMAT)

**Owner instruction, 7 November 2026:** "implement all of the merge and archive actions", meaning those of the [framework review](../review_2026-11-07_framework/REPORT.md) §4. Base HEAD `d6a6502db`.

## Method

1. **Merge verbatim.** Each merged document starts with a part table (former file, bytes, SHA-256 of the original). Each source follows as a part, in order, with two edits only: its title line became the part heading, and the banner paragraphs that every source repeated appear once at the top. A script asserted that every source's remaining text appears unchanged in its merged file before any link was touched.
2. **Keep originals.** Every merged or archived file was moved with `git mv` into `archive/consolidation_2026-11-07/` (`merged_sources/` or `archived/`), so history and blame follow it.
3. **Redirect links in live documents only.** These are the root documents, `research/prompts/`, `research/scoreboard/`, the `research/` READMEs and `ml/`. 488 link targets went to the new file and part (an existing anchor is kept where the merged file still has it). 48 plain path mentions were updated, outside history files and merged text. 41 link labels that named an old file now name the new one, with the old name in brackets. Immutable records (prediction logs, issued research, minis, settlements, dated verification folders, archive) were not edited; HISTORICAL_LINK_INDEX maps their old links.
4. **Check.** The broken relative links in live documents were counted before and after: **0 new**. Code paths to the rank log were updated in `ml/evaluation/card_calibration.py`, `ml/evaluation/card_history.py` and `ml/run.py`. `test_prompt_consistency` now looks for WORKFLOW where it looked for EXECUTION_ENVIRONMENT_PROTOCOL, and `research/prompts/DEPENDENCY_MAP.md` was regenerated from the prompt texts. Full test suite: see the commit.
5. **Lessons.** [LESSONS_PROMOTED.md](../../../LESSONS_PROMOTED.md) copies, verbatim, the lesson-index lines marked PROMOTED or NARROWED (with their table headers), and the whole "Recurring mistakes" and "Withdrawn — never apply" sections. The full index and register are archived.

## Not done, and why

- **External-route files** (GITHUB_REFERENCE_PROTOCOL, GOOGLE_DRIVE_EXCHANGE_PROTOCOL, `research/prompts/external_requests/`). The review made archiving them conditional on the owner's choice of request route (§3.6). REQ-v2 was added on 22 October at the owner's request after ENV-v2, so they stay until the owner decides.
- **Content consolidation.** The merges join files; they do not remove contradictions or shorten text. That rewrite (review §3.4, REV-08) is a separate prompt-8 change.
- **Long paths** (review §3.8) are unchanged: the October verification folders moved under `archive/verification_2026-10/`, so their longest path is now 198 characters.

## Map

| Former path | Now | Original copy | Bytes | SHA-256 |
|---|---|---|---:|---|
| `CURRENT_RULES.md` | [RULES_REFERENCE.md](../../../RULES_REFERENCE.md#part-a-current_rules) (part A) | [original](../../../archive/consolidation_2026-11-07/merged_sources/CURRENT_RULES.md) | 40,096 | `c583a5bcb130855fcc534a9fd4690e39d7b67428ae4d135f783e15b8b382a769` |
| `SELECTION_RULES.md` | [RULES_REFERENCE.md](../../../RULES_REFERENCE.md#part-b-selection_rules) (part B) | [original](../../../archive/consolidation_2026-11-07/merged_sources/SELECTION_RULES.md) | 17,947 | `d7df34a0931267b7ed035a76bac79adf8ce228157db47bcc85f265ce4e760ead` |
| `RESEARCH_COMPLETION_PROTOCOL.md` | [RESEARCH_PROTOCOL.md](../../../RESEARCH_PROTOCOL.md#part-a-research_completion_protocol) (part A) | [original](../../../archive/consolidation_2026-11-07/merged_sources/RESEARCH_COMPLETION_PROTOCOL.md) | 13,948 | `d9f65ab6ee8c2dbc7eb9b73609f26a39a2e608ba46ecf822dfac09cbbc040419` |
| `RESEARCH_EXHAUSTIVENESS_PROTOCOL.md` | [RESEARCH_PROTOCOL.md](../../../RESEARCH_PROTOCOL.md#part-b-research_exhaustiveness_protocol) (part B) | [original](../../../archive/consolidation_2026-11-07/merged_sources/RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) | 12,698 | `bee4e597cf98a6c74f6faa4d7f07eff9e1cf22c4858c719ec8cbe714b5677491` |
| `RESEARCH_RETENTION_PROTOCOL.md` | [RESEARCH_PROTOCOL.md](../../../RESEARCH_PROTOCOL.md#part-c-research_retention_protocol) (part C) | [original](../../../archive/consolidation_2026-11-07/merged_sources/RESEARCH_RETENTION_PROTOCOL.md) | 7,888 | `45768e84e192c2d0f3b9832f612057489ff3870b4af6988114fd66950ca45e1f` |
| `RESEARCH_CHECKLISTS.md` | [RESEARCH_PROTOCOL.md](../../../RESEARCH_PROTOCOL.md#part-d-research_checklists) (part D) | [original](../../../archive/consolidation_2026-11-07/merged_sources/RESEARCH_CHECKLISTS.md) | 8,623 | `47a1f56f6161bef5c59d783a7201954568d8bfc6e2518de6a5fc3834fd894187` |
| `TIMING_RESEARCH_PROTOCOL.md` | [RESEARCH_PROTOCOL.md](../../../RESEARCH_PROTOCOL.md#part-e-timing_research_protocol) (part E) | [original](../../../archive/consolidation_2026-11-07/merged_sources/TIMING_RESEARCH_PROTOCOL.md) | 8,997 | `1acfc38a043aa03612d06ecf06b6e50faf782a234c0fa18a253769195bfb8987` |
| `EXECUTION_ENVIRONMENT_PROTOCOL.md` | [WORKFLOW.md](../../../WORKFLOW.md#part-a-execution_environment_protocol) (part A) | [original](../../../archive/consolidation_2026-11-07/merged_sources/EXECUTION_ENVIRONMENT_PROTOCOL.md) | 5,810 | `a44839f15fc8357a826ec45ddeb3d8b238c91723020f74f5b422e9ccc43f4b98` |
| `MINI_LOG_IDENTITY_PROTOCOL.md` | [WORKFLOW.md](../../../WORKFLOW.md#part-b-mini_log_identity_protocol) (part B) | [original](../../../archive/consolidation_2026-11-07/merged_sources/MINI_LOG_IDENTITY_PROTOCOL.md) | 11,720 | `cb11c76b710f8f6bfe61d9c72ace9daff216bb9c7f1a62406ad09c4867e4def7` |
| `PRIMARY_PREDICTION_PROTOCOL.md` | [ML_PIPELINE.md](../../../ML_PIPELINE.md#part-a-primary_prediction_protocol) (part A) | [original](../../../archive/consolidation_2026-11-07/merged_sources/PRIMARY_PREDICTION_PROTOCOL.md) | 16,513 | `13231e68e0484ae8f95079a557ce95a34b81774fe03b2de63834071fc05c972e` |
| `ML_EXECUTION_PROTOCOL.md` | [ML_PIPELINE.md](../../../ML_PIPELINE.md#part-b-ml_execution_protocol) (part B) | [original](../../../archive/consolidation_2026-11-07/merged_sources/ML_EXECUTION_PROTOCOL.md) | 7,152 | `0d000bb193fd29b25462412c8d6dde4bd32ea614c88eff18bd05b8fab98e477e` |
| `LEARNING_PIPELINE_PROTOCOL.md` | [ML_PIPELINE.md](../../../ML_PIPELINE.md#part-c-learning_pipeline_protocol) (part C) | [original](../../../archive/consolidation_2026-11-07/merged_sources/LEARNING_PIPELINE_PROTOCOL.md) | 18,164 | `cbc62472c83c479076552f75b8c5da849fe3d65f5a60dc929ab8ce98a704edab` |
| `COMPETITION_PARAMETERS.md` | [PARAMETERS.md](../../../PARAMETERS.md#part-a-competition_parameters) (part A) | [original](../../../archive/consolidation_2026-11-07/merged_sources/COMPETITION_PARAMETERS.md) | 9,703 | `d8d0f6fcdad43d3d8dcc61d307da386f5ea48780e1c49f42540e7a3480d1b752` |
| `EFFECT_TABLES.md` | [PARAMETERS.md](../../../PARAMETERS.md#part-b-effect_tables) (part B) | [original](../../../archive/consolidation_2026-11-07/merged_sources/EFFECT_TABLES.md) | 4,823 | `5daa7d736ff39805005f384f0051ef2b81d266df3f60be828540210a2a6f9e4e` |
| `BASE_RATES_REGISTER.md` | [PARAMETERS.md](../../../PARAMETERS.md#part-c-base_rates_register) (part C) | [original](../../../archive/consolidation_2026-11-07/merged_sources/BASE_RATES_REGISTER.md) | 40,440 | `0f2fd8eeef2aa8c19a7eaa49ea7877e1e50e9f5cda23de942c69de5fd16dc1ac` |
| `LEAGUE_PROFILES.md` | [PARAMETERS.md](../../../PARAMETERS.md#part-d-league_profiles) (part D) | [original](../../../archive/consolidation_2026-11-07/merged_sources/LEAGUE_PROFILES.md) | 2,070 | `e670bdfcad0659556ed6eb3fcfbfaf4be66d47254b9270b5f47d2ba828a9383b` |
| `FORECAST_CYCLE_PROTOCOL.md` | [REFERENCE_MODEL_PROTOCOL.md](../../../REFERENCE_MODEL_PROTOCOL.md#merged-forecast_cycle_protocol) (appended section) | [original](../../../archive/consolidation_2026-11-07/merged_sources/FORECAST_CYCLE_PROTOCOL.md) | 25,294 | `0b7fe060feb59310e84976f9dcbcf2e77ea51306ad5f22fc9e309cb232209164` |
| `RULES_NHL.md` | [RULES_ICE_HOCKEY.md](../../../RULES_ICE_HOCKEY.md#merged-rules_nhl) (appended section) | [original](../../../archive/consolidation_2026-11-07/merged_sources/RULES_NHL.md) | 4,976 | `4254f9691bd212a48267f892faeb8ad6c3d4b1db91611a389bf1f4b0d38bbedc` |
| `LEAGUE_RULES_SOCCER.md` | [RULES_SOCCER.md](../../../RULES_SOCCER.md#merged-league_rules_soccer) (appended section) | [original](../../../archive/consolidation_2026-11-07/merged_sources/LEAGUE_RULES_SOCCER.md) | 44,553 | `ecc71130f086ad01fb24ba6571f0ee8e4c401d71bcdd9d59ce10a02d3e3b448a` |
| `LEAGUE_RULES_CRICKET.md` | [RULES_CRICKET.md](../../../RULES_CRICKET.md#merged-league_rules_cricket) (appended section) | [original](../../../archive/consolidation_2026-11-07/merged_sources/LEAGUE_RULES_CRICKET.md) | 27,230 | `907dbd0b988e6b2cd7731736ec865d6e354e2847baeedec54cade46bbc84c5be` |
| `METHOD.md` | [CORE.md](../../../CORE.md#merged-method) (appended section) | [original](../../../archive/consolidation_2026-11-07/merged_sources/METHOD.md) | 3,707 | `7d4e83144a4bdd81fce816b410b970c35c030448dc3a26da7d653f82e776265b` |

| Archived or moved file | Now | Bytes | SHA-256 |
|---|---|---:|---|
| `BASKETBALL.txt` | [archive/consolidation_2026-11-07/archived/BASKETBALL.txt](../../../archive/consolidation_2026-11-07/archived/BASKETBALL.txt) | 9,596 | `742605930e98e208015f9929bb22285794f4f8395ffc1f3ba42f5520d50fcd1e` |
| `PROMPT_1_SUPPLIED_FIRST_EXTENDED_2026-10-14.md` | [archive/consolidation_2026-11-07/archived/PROMPT_1_SUPPLIED_FIRST_EXTENDED_2026-10-14.md](../../../archive/consolidation_2026-11-07/archived/PROMPT_1_SUPPLIED_FIRST_EXTENDED_2026-10-14.md) | 168,390 | `cb8076439f33ba0ae4299519f37918442b9f13bb0f8bf90933b07fc55b192efd` |
| `ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md` | [archive/consolidation_2026-11-07/archived/ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md](../../../archive/consolidation_2026-11-07/archived/ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md) | 78,221 | `01a69e0b13cc3af3599aee6cb863f4f626357642bfa15a27e272d463a325bb36` |
| `MODEL_PROBABILITY_ML_RECOMMENDATIONS_2026-10-12.md` | [archive/consolidation_2026-11-07/archived/MODEL_PROBABILITY_ML_RECOMMENDATIONS_2026-10-12.md](../../../archive/consolidation_2026-11-07/archived/MODEL_PROBABILITY_ML_RECOMMENDATIONS_2026-10-12.md) | 33,297 | `d973e944175036e3cfce66a0d1c44a4753a1c0f41a8ad06b320b633fc978fc86` |
| `VALIDATION_EVIDENCE.md` | [archive/consolidation_2026-11-07/archived/VALIDATION_EVIDENCE.md](../../../archive/consolidation_2026-11-07/archived/VALIDATION_EVIDENCE.md) | 50,637 | `b8ff0b2f6d9e572a7820127abcb8984ff939e9e7903ba095b0679d549e711600` |
| `RESULTS_REBUILD_PLAN.md` | [archive/consolidation_2026-11-07/archived/RESULTS_REBUILD_PLAN.md](../../../archive/consolidation_2026-11-07/archived/RESULTS_REBUILD_PLAN.md) | 5,003 | `0350d76093c13f197b3ee393db81779c3529e3b5b5f7424b5d271ff3ac2ed2be` |
| `LEARNING_REGISTER.md` | [archive/consolidation_2026-11-07/archived/LEARNING_REGISTER.md](../../../archive/consolidation_2026-11-07/archived/LEARNING_REGISTER.md) | 354,842 | `faeb6b790477aaf68215292efd4188cb285ad45951573e9f355c9474233f5006` |
| `LEARNINGS_INDEX.md` | [archive/consolidation_2026-11-07/archived/LEARNINGS_INDEX.md](../../../archive/consolidation_2026-11-07/archived/LEARNINGS_INDEX.md) | 47,801 | `8837c5b623fb09185cdba1fe9c32cc20016e6e669c3469285cd099db5264d9b5` |
| `GAME_PREDICTION_RANK_LOG.csv` | [research/data/GAME_PREDICTION_RANK_LOG.csv](../../data/GAME_PREDICTION_RANK_LOG.csv) (moved, not archived) | 2,072,080 | `49e3fd8dcc312206b173877dfd7cae46375fc6b07bb2429139eb28b58b981199` |

| Moved folder | Now |
|---|---|
| `research/verification/all_log_resolution_2026-10-05/` | [archive/verification_2026-10/all_log_resolution_2026-10-05/](../../../archive/verification_2026-10/all_log_resolution_2026-10-05/) |
| `research/verification/closure_2026-10-05/` | [archive/verification_2026-10/closure_2026-10-05/](../../../archive/verification_2026-10/closure_2026-10-05/) |
| `research/verification/experiment_measures_2026-10-05/` | [archive/verification_2026-10/experiment_measures_2026-10-05/](../../../archive/verification_2026-10/experiment_measures_2026-10-05/) |
| `research/verification/implementation_2026-10-05/` | [archive/verification_2026-10/implementation_2026-10-05/](../../../archive/verification_2026-10/implementation_2026-10-05/) |
| `research/verification/log_repair_2026-10-01/` | [archive/verification_2026-10/log_repair_2026-10-01/](../../../archive/verification_2026-10/log_repair_2026-10-01/) |
| `research/verification/mini_settlement_2026-10-02/` | [archive/verification_2026-10/mini_settlement_2026-10-02/](../../../archive/verification_2026-10/mini_settlement_2026-10-02/) |
| `research/verification/prompt_revision_2026-10-01/` | [archive/verification_2026-10/prompt_revision_2026-10-01/](../../../archive/verification_2026-10/prompt_revision_2026-10-01/) |
| `research/verification/reconciliation_2026-10-05/` | [archive/verification_2026-10/reconciliation_2026-10-05/](../../../archive/verification_2026-10/reconciliation_2026-10-05/) |
| `research/verification/reconciliation_2026-10-06/` | [archive/verification_2026-10/reconciliation_2026-10-06/](../../../archive/verification_2026-10/reconciliation_2026-10-06/) |
| `research/verification/settlement_2026-10-01/` | [archive/verification_2026-10/settlement_2026-10-01/](../../../archive/verification_2026-10/settlement_2026-10-01/) |
| `research/custody/implementation_2026-10-01/` | [archive/custody_implementation_2026-10-01/](../../../archive/custody_implementation_2026-10-01/) |
