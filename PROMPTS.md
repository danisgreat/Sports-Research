# Operator prompts

**Local keys until settlement; updated mini after every game (MINI-v2).** Defined in [MINI_LOG_IDENTITY_PROTOCOL](MINI_LOG_IDENTITY_PROTOCOL.md); summarised in [CORE](CORE.md) §2.

**Persistent research and corroboration (EXH-v1).** Defined in [RESEARCH_EXHAUSTIVENESS_PROTOCOL](RESEARCH_EXHAUSTIVENESS_PROTOCOL.md); summarised in [CORE](CORE.md) §5.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** Defined in [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md); summarised in [CORE](CORE.md) §5.

**Required repository fallback (REF-v1).** Defined in [GITHUB_REFERENCE_PROTOCOL](GITHUB_REFERENCE_PROTOCOL.md); summarised in [CORE](CORE.md) §1.

**Google Drive (DRIVE-v2, optional).** Defined in [GOOGLE_DRIVE_EXCHANGE_PROTOCOL](GOOGLE_DRIVE_EXCHANGE_PROTOCOL.md); summarised in [CORE](CORE.md) §1.

**ML/RL scope (MLSCOPE-v3).** Defined in [FORECAST_CYCLE_PROTOCOL](FORECAST_CYCLE_PROTOCOL.md); summarised in [CORE](CORE.md) §7.

**Execution environment (ENV-v2).** Defined in [EXECUTION_ENVIRONMENT_PROTOCOL](EXECUTION_ENVIRONMENT_PROTOCOL.md); summarised in [CORE](CORE.md) §1.

**Active suite: P-2026.10.22-v24.0** (read [CORE](CORE.md) first; prompt 1 = core with the shared steps plus one sport file in [research/prompts/1_sports/](research/prompts/1_sports/); ENV-v2: every prompt runs in this repository with internet research and ends with a commit and push; MLSCOPE-v3: prompt 1 freezes the declared reference before the card, builds p_card as reference plus logged adjustments and freezes the card's final p after it, prompt 3 settles it and runs the import (canonical IDs assigned in the settlement phase), prompt 6 scores the ledger and prompt 8 owns references and releases; models are judged after 8 weeks and 50 paired games; optional DRIVE-v2 drop box under [GOOGLE_DRIVE_EXCHANGE_PROTOCOL](GOOGLE_DRIVE_EXCHANGE_PROTOCOL.md); new minis mini-log-10 / mini-settlement-10; existing formats retained; learning records and review levels under [LEARNING_PIPELINE_PROTOCOL](LEARNING_PIPELINE_PROTOCOL.md); dependency map in [research/prompts/DEPENDENCY_MAP.md](research/prompts/DEPENDENCY_MAP.md)). [Reading receipt and workflow](research/prompts/README.md). Use the complete selected prompt; its required rules/templates are linked there.

| # | Copy-ready prompt |
|---|---|
| 1 | [Individual game card: core](research/prompts/1_GAME_CARD.md) plus [one sport file](research/prompts/1_sports/) |
| 2 | [Start a local mini](research/prompts/2_START_LOCAL_MINI.md) |
| 3 | [Settle and review the mini](research/prompts/3_SETTLE_LOCAL_MINI.md) |
| 4 | [Import into the active Combined Log](research/prompts/4_CANONICAL_IMPORT.md) |
| 5 | [Start the next Combined Log](research/prompts/5_START_THE_NEXT_COMBINED_LOG.md) |
| 6 | [Combined-log retrospective](research/prompts/6_COMBINED_LOG_RETROSPECTIVE.md) |
| 7 | [Expand or repair historical results](research/prompts/7_EXPAND_PREVIOUS_RESULTS.md) |
| 8 | [Improve the framework](research/prompts/8_IMPROVE_THE_FRAMEWORK.md) |

Run 2 → 1 per event → 3 → 4; use 5–8 when needed. Current IDs/destination: [CURRENT_STATE](CURRENT_STATE.md). Implemented changes and recommendation roadmap: [2026-10-12-1](research/verification/framework_change_2026-10-12-1/IMPLEMENTATION.md) (current), [2026-10-11-1](research/verification/framework_change_2026-10-11-1/IMPLEMENTATION.md). Preserved previous suites: [v10](archive/superseded_2026-10-12/research/prompts/README.md), [pre-v10](archive/superseded_2026-10-11/prompt_v10/research/prompts/README.md).

These prompts improve evidence, consistency and measurement. Predictive improvement remains to be demonstrated prospectively against frozen baselines; no prompt guarantees outcomes.

Availability procedure: [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md), mandatory for every prompt-1 game.

All eight tasks require [COMMON_OPERATING_PROTOCOL](research/prompts/COMMON_OPERATING_PROTOCOL.md). Use the [prompt 1 core](research/prompts/1_GAME_CARD.md) with one of the eleven [sport files](research/prompts/1_sports/), each holding its own Upcoming game block. The supplied-first root draft is reference only; current P4/selection rules govern.

**Primary ML/RL (15 October 2026; scope narrowed 17 October 2026):** [PRIMARY_PREDICTION_PROTOCOL](PRIMARY_PREDICTION_PROTOCOL.md) now governs workshop models used only in prompts 6 and 8 (MLSCOPE-v1); game cards are ANALYST_PRIMARY_V1.

**Preferred historical recovery:** [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md) applies to every sport and competition. Missing, incomplete or incorrect local history is researched online first, with reviewed web rows usable in the named primary input scope; shared archive maintenance is separate. Source/known-at checks and unsupported-model limits remain.

**Strict research completion:** [RESEARCH_COMPLETION_PROTOCOL](RESEARCH_COMPLETION_PROTOCOL.md) requires full research, all applicable sport procedures and every requested contract assessment irrespective of model calibration/runtime, data/lineup gaps, kickoff or mini/write blockers. Supported automatic analyst comparisons stay NOT_PRIMARY; missing numerical ML never means stop research. The A9 evidence matrix is mandatory.

**Research retention before model availability (RETAIN-v2).** Defined in [RESEARCH_RETENTION_PROTOCOL](RESEARCH_RETENTION_PROTOCOL.md); summarised in [CORE](CORE.md) §2.

**Local research record and updated-document delivery (owner update, 16 October 2026).** Defined in [MINI_LOG_IDENTITY_PROTOCOL](MINI_LOG_IDENTITY_PROTOCOL.md); summarised in [CORE](CORE.md) §2.

