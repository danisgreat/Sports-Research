# Sports Research

**Executable forecast cycle (CYCLE-v1).** Defined in [FORECAST_CYCLE_PROTOCOL](FORECAST_CYCLE_PROTOCOL.md); summarised in [CORE](CORE.md) §7.

**Local keys until settlement; updated mini after every game (MINI-v2).** Defined in [MINI_LOG_IDENTITY_PROTOCOL](MINI_LOG_IDENTITY_PROTOCOL.md); summarised in [CORE](CORE.md) §2.

**Persistent source research:** [EXH-v1](RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) requires alternative-source pursuit and independent corroboration across every applicable requirement. [Source observations](RESEARCH_SOURCE_REGISTER.md) preserve discoveries/limits. New settlements use mini-settlement-10 with a visible reuse section and S17. Unresolved required facts/corroboration keep information INCOMPLETE. Older originals and numerical policy remain unchanged.

**Persistent research and corroboration (EXH-v1).** Defined in [RESEARCH_EXHAUSTIVENESS_PROTOCOL](RESEARCH_EXHAUSTIVENESS_PROTOCOL.md); summarised in [CORE](CORE.md) §5.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** Defined in [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md); summarised in [CORE](CORE.md) §5.

**Required repository fallback (REF-v1).** Defined in [GITHUB_REFERENCE_PROTOCOL](GITHUB_REFERENCE_PROTOCOL.md); summarised in [CORE](CORE.md) §1.

**Google Drive (DRIVE-v2, optional).** Defined in [GOOGLE_DRIVE_EXCHANGE_PROTOCOL](GOOGLE_DRIVE_EXCHANGE_PROTOCOL.md); summarised in [CORE](CORE.md) §1.

**ML/RL scope (MLSCOPE-v3).** Defined in [FORECAST_CYCLE_PROTOCOL](FORECAST_CYCLE_PROTOCOL.md); summarised in [CORE](CORE.md) §7.

**Execution environment (ENV-v2).** Defined in [EXECUTION_ENVIRONMENT_PROTOCOL](EXECUTION_ENVIRONMENT_PROTOCOL.md); summarised in [CORE](CORE.md) §1.

A sports-only forecasting framework made of documents. It tells a research agent how to forecast, log and settle individual games across ten sports, how to verify past results online, and how to learn from the outcomes. **Controls and forecasts use Markdown/CSV/text.** New numerical primary forecasts are the analyst's own, with transparent arithmetic (ANALYST_PRIMARY_V1); after each card the forecast cycle in [`ml/`](ml/README.md) freezes a pregame model shadow beside it, which is settled in prompt 3, evaluated in prompt 6 and released in prompt 8. Code stays in ml/; JSON/binary artifacts remain excluded.

**What is true now** (method, next ID, active log, scoreboard): [CURRENT_STATE.md](CURRENT_STATE.md). Method **MDS-2026.10.22-v24.0**, control **CR-2026.10.22-R2**, scoring **SCV-2026.10.22-v12**, selection **SEL-2026.10.22-v4**, prompts **P-2026.10.22-v24.0** (new mini-log-10). A game card reads [CORE](CORE.md) first. Every prompt runs in this repository with internet research (ENV-v2); an optional Google Drive drop box exists ([GOOGLE_DRIVE_EXCHANGE_PROTOCOL](GOOGLE_DRIVE_EXCHANGE_PROTOCOL.md)) and nothing must be pushed there. [October 12 implementation map](research/verification/framework_change_2026-10-12-1/IMPLEMENTATION.md) (audit R01–R38 and prediction items PR-01–PR-10) · [October 11 roadmap](research/verification/framework_change_2026-10-11-1/IMPLEMENTATION.md). Active files and usable data: [ACTIVE_FILE_INDEX.md](ACTIVE_FILE_INDEX.md). The 2026-10-09 runtime remains removed. Development models from the `ml/` workshop are `HISTORICAL_DEVELOPMENT` only; old workshop outputs cannot substitute for a new primary run; experimental primary use is now authorised under PRIMARY_PREDICTION_PROTOCOL, with no predictive certification.

**Learning from research (LEARN-v1):** [LEARNING_PIPELINE_PROTOCOL](LEARNING_PIPELINE_PROTOCOL.md) turns every researched and settled game into deduplicated, point-in-time learning data (store → features → immutable training releases) and gates any model change behind chronological studies, prospective shadows and an owner decision. The primary model is unchanged.

## Rules in force

- **Rule T2:** only Rank 1 and Rank 2 count as wins. Ranks 3 and 4 are informational.
- **Rule R1:** every Rank-1 failure gets a deep retrospection.
- **Rule P4:** supplied contracts are reference only. Retain up to four supported candidates from a coherent distribution, ranked by `p_card`, with a frozen same-line baseline where available. Qualitative/NO_FORECAST research remains explicit; shadow alternatives are separate.
- **Recent form, counted once (v11):** every team card reads L5, L10, L15 and L20, season and league form from dated games before the cutoff, with true counts and overlap disclosed. Only the shrunk L20/season rate may move the centre, as a listed adjustment; the four-window blend is printed for comparison.
- **Read first, cite what you use:** every task opens with a reading receipt of the current documents, and every card names the rules, sources and past results it applied.
- **SPORTS_ONLY / MARKET_BLIND:** no odds, tips or prediction markets anywhere in the research.
- **Honest labels:** new primary probabilities are ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY; historical manual scenarios retain their original label; nothing is performance-certified.

## Start here

1. [CURRENT_STATE.md](CURRENT_STATE.md), then [METHOD.md](METHOD.md) and [CURRENT_RULES.md](CURRENT_RULES.md).
2. [SELECTION_RULES.md](SELECTION_RULES.md): the gate, the families, the grades and the failure classes.
3. [research/prompts/](research/prompts/README.md): the eight operator prompts and the mini lifecycle.
4. [CARD_AND_LOG_TEMPLATES.md](CARD_AND_LOG_TEMPLATES.md): card, mini, settlement and log formats, and the self-audit checklists.
5. For a card: [mandatory starter/bench/injury research](ROSTER_AVAILABILITY_PROTOCOL.md), then the sport's `RULES_<SPORT>.md`, [PROBABILITY_TOOLKIT.md](PROBABILITY_TOOLKIT.md), [BASE_RATES_REGISTER.md](BASE_RATES_REGISTER.md), [LEAGUE_PROFILES.md](LEAGUE_PROFILES.md), [SOURCES.md](SOURCES.md) and [ARCHIVE_USE_GUIDE.md](ARCHIVE_USE_GUIDE.md).
6. [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md): mandatory online prior-game research.

## The cycle

```text
2 Start mini ─► 1 Card ─► 1 Card ─► … ─► 3 Settle ─► 4 Import ─► 2 Start next mini (new local namespace) ─► …
                                                              └─► 5 Roll over the Combined Log (when needed)
                                                              └─► 6 Retrospective (when enough cards are settled)
```

All eight prompts are run by Claude Code in this repository, with internet access for research (ENV-v2): prompt 1 writes each card into the active mini and freezes its model shadow, prompt 3 settles and imports (assigning canonical IDs), prompt 7 extends the archive and prompt 8 improves the framework ([PROMPTS.md](PROMPTS.md)).

## Document map

| Area | Documents |
|---|---|
| Authority | [CURRENT_STATE.md](CURRENT_STATE.md), [METHOD.md](METHOD.md), [CURRENT_RULES.md](CURRENT_RULES.md), [SELECTION_RULES.md](SELECTION_RULES.md), [CHANGELOG.md](CHANGELOG.md) |
| Operating | [research/prompts/](research/prompts/README.md), [PROMPTS.md](PROMPTS.md), [CARD_AND_LOG_TEMPLATES.md](CARD_AND_LOG_TEMPLATES.md), [VERIFICATION_PROTOCOL.md](VERIFICATION_PROTOCOL.md), [CONTRIBUTING.md](CONTRIBUTING.md) |
| Probability | [PROBABILITY_TOOLKIT.md](PROBABILITY_TOOLKIT.md), [LEAGUE_PROFILES.md](LEAGUE_PROFILES.md), [BASE_RATES_REGISTER.md](BASE_RATES_REGISTER.md), [SCORING_AND_VALIDATION.md](SCORING_AND_VALIDATION.md) |
| Sport rules | [RULES_BASEBALL.md](RULES_BASEBALL.md), [RULES_BASKETBALL.md](RULES_BASKETBALL.md), [RULES_ICE_HOCKEY.md](RULES_ICE_HOCKEY.md), [RULES_NHL.md](RULES_NHL.md), [RULES_SOCCER.md](RULES_SOCCER.md), [LEAGUE_RULES_SOCCER.md](LEAGUE_RULES_SOCCER.md), [RULES_CRICKET.md](RULES_CRICKET.md), [LEAGUE_RULES_CRICKET.md](LEAGUE_RULES_CRICKET.md), [RULES_TENNIS.md](RULES_TENNIS.md), [RULES_NRL_RUGBY.md](RULES_NRL_RUGBY.md), [RULES_RUGBY_UNION.md](RULES_RUGBY_UNION.md), [RULES_AFL.md](RULES_AFL.md), [RULES_AMERICAN_FOOTBALL.md](RULES_AMERICAN_FOOTBALL.md) |
| Sources and data | [SOURCES.md](SOURCES.md), [ARCHIVE_USE_GUIDE.md](ARCHIVE_USE_GUIDE.md), [RESULTS_REBUILD_PLAN.md](RESULTS_REBUILD_PLAN.md), `GAME_PREDICTION_RANK_LOG.csv` (the historical rank log) |
| Logs and status | `prediction logs/` (Combined Parts 1 to 9; [active Part 9](prediction%20logs/PREDICTION_LOG_COMBINED_9.md)), [GAME_LOG_STATUS_CURRENT.md](GAME_LOG_STATUS_CURRENT.md), [research/scoreboard/SCOREBOARD.md](research/scoreboard/SCOREBOARD.md), [research/issued_research/](research/issued_research/) (preserved original card texts) |
| Learning | [LEARNING_REGISTER.md](LEARNING_REGISTER.md), [LEARNINGS_INDEX.md](LEARNINGS_INDEX.md), [FRAMEWORK_RETROSPECTIVE_2026-10-09.md](archive/root_documents_2026-10-14/FRAMEWORK_RETROSPECTIVE_2026-10-09.md), [HYPOTHESIS_REGISTER.md](HYPOTHESIS_REGISTER.md), [research/verification/](research/verification/) (dated evidence reports) |
| Primary runtime and separate model workshop | [ml/](ml/README.md), [research/model_shadow/](research/model_shadow/README.md), [ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md](ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md) |
| History and design notes | [archive/](archive/), [NUMERICAL_MODEL_REGISTER.md](archive/root_documents_2026-10-14/NUMERICAL_MODEL_REGISTER.md), [H0_DATASET_CARD.md](archive/root_documents_2026-10-14/H0_DATASET_CARD.md), [DATA_SOURCE_REGISTER.md](archive/root_documents_2026-10-14/DATA_SOURCE_REGISTER.md), [HISTORICAL_LINK_INDEX.md](HISTORICAL_LINK_INDEX.md) |

**Historical root documents (14 October 2026):** ten retired design, audit and ledger documents now live in [the root-document archive](archive/root_documents_2026-10-14/README.md). Frozen historical citations retain their original paths; use [the recovery map](HISTORICAL_LINK_INDEX.md#root-document-archive-2026-10-14) or the archive's [original-link context](archive/root_documents_2026-10-14/LINK_RECOVERY.md).

## Sports covered

Baseball (MLB, KBO, NPB), cricket, basketball (NBA, WNBA, NBL, European and Asian leagues), ice hockey, tennis, soccer, rugby league, rugby union, Australian rules (AFL, AFLW) and American football. Each has its own [prompt 1 sport file](research/prompts/1_sports/), used with the [prompt 1 core](research/prompts/1_GAME_CARD.md), that sets the research list, the distribution to build by hand and the family checks.

## Honesty and limits

New numeric forecasts are uncalibrated analyst probabilities, each with a pregame model shadow where a release exists; historical model-assisted cards keep their original labels. The framework tests its own rules against settled results, publishes the failures, and changes a rule only after a pre-registered test ([HYPOTHESIS_REGISTER.md](HYPOTHESIS_REGISTER.md)). Past results are a research aid; an empty archive file is missing data, not a finding. Read [LICENSE.md](LICENSE.md) before reuse.

## October 14 ML review and complete prompts

[Implementation review](research/verification/framework_change_2026-10-14-5/ML_WORKSHOP_REVIEW.md) · [full prompts 1–8](research/prompts/README.md) · [individual game prompt: core](research/prompts/1_GAME_CARD.md) and [eleven sport files](research/prompts/1_sports/) · [artifact admission](research/model_shadow/ARTIFACT_PROVENANCE.md). Useful development mechanisms exist, but prospective predictive skill and RL benefits remain unestablished. Control CR-2026.10.14-R3; suite P-2026.10.14-v11.3.

## Research completion timing (15 October 2026)

[TIMING_RESEARCH_PROTOCOL](TIMING_RESEARCH_PROTOCOL.md) replaces scheduled lead deadlines with comprehensive research completion for every sport. Research may continue after play starts. Verified pre-start inputs with no outcome exposure can be CLEAN_PRE_START_INPUTS, while post-start issue and genuinely prospective pre-start release remain separate. [Current prompts](research/prompts/README.md) use P-2026.10.16-v19.2; no old card or model is upgraded.

**Primary ML/RL (15 October 2026; scope narrowed 17 October 2026):** [PRIMARY_PREDICTION_PROTOCOL](PRIMARY_PREDICTION_PROTOCOL.md) now governs workshop models used only in prompts 6 and 8 (MLSCOPE-v1); game cards are ANALYST_PRIMARY_V1.

**Current primary integrity review:** [review and comparison](research/verification/framework_change_2026-10-15-4/REVIEW.md). V3 retains deterministic mixing and fixes known-at replay, duplicate learning, parameter admission and receipts; prospective predictive gain remains unproven.

**Preferred historical recovery:** [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md) applies to every sport and competition. Missing, incomplete or incorrect local history is researched online first, with reviewed web rows usable in the named primary input scope; shared archive maintenance is separate. Source/known-at checks and unsupported-model limits remain.

**Strict research completion:** [RESEARCH_COMPLETION_PROTOCOL](RESEARCH_COMPLETION_PROTOCOL.md) requires full research, all applicable sport procedures and every requested contract assessment irrespective of model calibration/runtime, data/lineup gaps, kickoff or mini/write blockers. Supported automatic analyst comparisons stay NOT_PRIMARY; missing numerical ML never means stop research. The A9 evidence matrix is mandatory.

**Research retention before model availability (RETAIN-v2).** Defined in [RESEARCH_RETENTION_PROTOCOL](RESEARCH_RETENTION_PROTOCOL.md); summarised in [CORE](CORE.md) §2.

**Local research record and updated-document delivery (owner update, 16 October 2026).** Defined in [MINI_LOG_IDENTITY_PROTOCOL](MINI_LOG_IDENTITY_PROTOCOL.md); summarised in [CORE](CORE.md) §2.

