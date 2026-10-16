# Sports Research

**Persistent source research:** [EXH-v1](RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) requires alternative-source pursuit and independent corroboration across every applicable requirement. [Source observations](RESEARCH_SOURCE_REGISTER.md) preserve discoveries/limits. New settlements use mini-settlement-9 with a visible reuse section and S17. Unresolved required facts/corroboration keep information INCOMPLETE. Older originals and numerical policy remain unchanged.

**Persistent research and corroboration (EXH-v1).** Apply [RESEARCH_EXHAUSTIVENESS_PROTOCOL](RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) to every required field in research, logging, settlement and verification. If a source is incomplete, open alternatives and verify material facts with another independent source; track every remaining field and attempt. Unresolved facts/corroboration never qualify as complete information. New settlements use mini-settlement-9 with a visible source-discovery/reuse section, three source/attempt/closure CSVs and S17; older originals retain their rules and bytes. Consult [RESEARCH_SOURCE_REGISTER](RESEARCH_SOURCE_REGISTER.md) and prior package registers, recheck actual coverage, and continue discovery beyond them.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** For every game, research both sides' L5/L10/L15/L20 online under [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md), with opened sources, dated game rows and true n. Seek exact-game confirmed players, starting roles, bench/replacements and absences under [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md); projected players remain unconfirmed. The retired local results store and its derived profiles are not required inputs or fallbacks. Earlier archive-first directions are superseded.

**Required repository fallback (REF-v1).** Always keep [https://github.com/danisgreat/Sports-Research/tree/main](https://github.com/danisgreat/Sports-Research/tree/main) as the standing reference. If required local files are not fully accessible (missing, unreadable, truncated or incomplete), retrieve the actual required contents from this repository before declaring them unavailable. Apply [GITHUB_REFERENCE_PROTOCOL](GITHUB_REFERENCE_PROTOCOL.md): resolve one main commit SHA, record exact files/read time and fallback results in the existing reading receipt, and preserve the declared authority mode. Never substitute an unpublished local mini, claim unread content or treat viewing code as executing it. If authorized remote access also fails, record the real gap and continue independent work.

A sports-only forecasting framework made of documents. It tells a research agent how to forecast, log and settle individual games across ten sports, how to verify past results online, and how to learn from the outcomes. **Controls and forecasts use Markdown/CSV/text.** New numerical primary forecasts execute the sporting ML/RL runtime in [`ml/`](ml/README.md), retain its immutable receipt bundle and use its selected fitted distribution. Code stays in ml/; JSON/binary artifacts remain excluded.

**What is true now** (method, next ID, active log, scoreboard): [CURRENT_STATE.md](CURRENT_STATE.md). Method **MDS-2026.10.16-v18.0**, control **CR-2026.10.16-R3**, scoring **SCV-2026.10.16-v11**, selection **SEL-2026.10.12-v3**, prompts **P-2026.10.16-v18.0** (new mini-log-9). [October 12 implementation map](research/verification/framework_change_2026-10-12-1/IMPLEMENTATION.md) (audit R01–R38 and prediction items PR-01–PR-10) · [October 11 roadmap](research/verification/framework_change_2026-10-11-1/IMPLEMENTATION.md). Active files and usable data: [ACTIVE_FILE_INDEX.md](ACTIVE_FILE_INDEX.md). The 2026-10-09 runtime remains removed. Development models from the `ml/` workshop are `HISTORICAL_DEVELOPMENT` only; old workshop outputs cannot substitute for a new primary run; experimental primary use is now authorised under PRIMARY_PREDICTION_PROTOCOL, with no predictive certification.

## Rules in force

- **Rule T2:** only Rank 1 and Rank 2 count as wins. Ranks 3 and 4 are informational.
- **Rule R1:** every Rank-1 failure gets a deep retrospection.
- **Rule P4:** supplied contracts are reference only. Retain up to four supported candidates from a coherent distribution, ranked by `p_card`, with a frozen same-line baseline where available. Qualitative/NO_FORECAST research remains explicit; shadow alternatives are separate.
- **Recent form, counted once (v11):** every team card reads L5, L10, L15 and L20, season and league form from dated games before the cutoff, with true counts and overlap disclosed. The primary model learns team/time effects from admitted history; manual blends/mixtures remain comparison diagnostics, not silent probability adjustments.
- **Read first, cite what you use:** every task opens with a reading receipt of the current documents, and every card names the rules, sources and past results it applied.
- **SPORTS_ONLY / MARKET_BLIND:** no odds, tips or prediction markets anywhere in the research.
- **Honest labels:** new primary probabilities are EXPERIMENTAL_PRIMARY_NOT_CERTIFIED; historical manual scenarios retain their original label; nothing is performance-certified.

## Start here

1. [CURRENT_STATE.md](CURRENT_STATE.md), then [METHOD.md](METHOD.md) and [CURRENT_RULES.md](CURRENT_RULES.md).
2. [SELECTION_RULES.md](SELECTION_RULES.md): the gate, the families, the grades and the failure classes.
3. [research/prompts/](research/prompts/README.md): the eight operator prompts and the mini lifecycle.
4. [CARD_AND_LOG_TEMPLATES.md](CARD_AND_LOG_TEMPLATES.md): card, mini, settlement and log formats, and the self-audit checklists.
5. For a card: [mandatory starter/bench/injury research](ROSTER_AVAILABILITY_PROTOCOL.md), then the sport's `RULES_<SPORT>.md`, [PROBABILITY_TOOLKIT.md](PROBABILITY_TOOLKIT.md), [BASE_RATES_REGISTER.md](BASE_RATES_REGISTER.md), [LEAGUE_PROFILES.md](LEAGUE_PROFILES.md), [SOURCES.md](SOURCES.md) and [ARCHIVE_USE_GUIDE.md](ARCHIVE_USE_GUIDE.md).
6. [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md): mandatory online prior-game research.

## The cycle

```text
2 Start mini ─► 1 Card ─► 1 Card ─► … ─► 3 Settle ─► 4 Import ─► 2 Start next mini (next canonical ID) ─► …
                                                              └─► 5 Roll over the Combined Log (when needed)
                                                              └─► 6 Retrospective (when enough cards are settled)
```

Prompts 1 to 3 are run by an external chat agent with GitHub read-only. Prompts 4 to 6 are run by Claude Code in the repository. Prompt 7 extends the archive and prompt 8 improves the framework ([PROMPTS.md](PROMPTS.md)).

## Document map

| Area | Documents |
|---|---|
| Authority | [CURRENT_STATE.md](CURRENT_STATE.md), [METHOD.md](METHOD.md), [CURRENT_RULES.md](CURRENT_RULES.md), [SELECTION_RULES.md](SELECTION_RULES.md), [CHANGELOG.md](CHANGELOG.md) |
| Operating | [research/prompts/](research/prompts/README.md), [PROMPTS.md](PROMPTS.md), [CARD_AND_LOG_TEMPLATES.md](CARD_AND_LOG_TEMPLATES.md), [VERIFICATION_PROTOCOL.md](VERIFICATION_PROTOCOL.md), [CONTRIBUTING.md](CONTRIBUTING.md) |
| Probability | [PROBABILITY_TOOLKIT.md](PROBABILITY_TOOLKIT.md), [LEAGUE_PROFILES.md](LEAGUE_PROFILES.md), [BASE_RATES_REGISTER.md](BASE_RATES_REGISTER.md), [SCORING_AND_VALIDATION.md](SCORING_AND_VALIDATION.md) |
| Sport rules | [RULES_BASEBALL.md](RULES_BASEBALL.md), [RULES_BASKETBALL.md](RULES_BASKETBALL.md), [RULES_ICE_HOCKEY.md](RULES_ICE_HOCKEY.md), [RULES_NHL.md](RULES_NHL.md), [RULES_SOCCER.md](RULES_SOCCER.md), [LEAGUE_RULES_SOCCER.md](LEAGUE_RULES_SOCCER.md), [RULES_CRICKET.md](RULES_CRICKET.md), [LEAGUE_RULES_CRICKET.md](LEAGUE_RULES_CRICKET.md), [RULES_TENNIS.md](RULES_TENNIS.md), [RULES_NRL_RUGBY.md](RULES_NRL_RUGBY.md), [RULES_RUGBY_UNION.md](RULES_RUGBY_UNION.md), [RULES_AFL.md](RULES_AFL.md), [RULES_AMERICAN_FOOTBALL.md](RULES_AMERICAN_FOOTBALL.md) |
| Sources and data | [SOURCES.md](SOURCES.md), [ARCHIVE_USE_GUIDE.md](ARCHIVE_USE_GUIDE.md), [RESULTS_REBUILD_PLAN.md](RESULTS_REBUILD_PLAN.md), `GAME_PREDICTION_RANK_LOG.csv` (the historical rank log) |
| Logs and status | `prediction logs/` (Combined Parts 1 to 7), [GAME_LOG_STATUS_CURRENT.md](GAME_LOG_STATUS_CURRENT.md), [research/scoreboard/SCOREBOARD.md](research/scoreboard/SCOREBOARD.md), [research/issued_research/](research/issued_research/) (preserved original card texts) |
| Learning | [LEARNING_REGISTER.md](LEARNING_REGISTER.md), [LEARNINGS_INDEX.md](LEARNINGS_INDEX.md), [FRAMEWORK_RETROSPECTIVE_2026-10-09.md](archive/root_documents_2026-10-14/FRAMEWORK_RETROSPECTIVE_2026-10-09.md), [HYPOTHESIS_REGISTER.md](HYPOTHESIS_REGISTER.md), [research/verification/](research/verification/) (dated evidence reports) |
| Primary runtime and separate model workshop | [ml/](ml/README.md), [research/model_shadow/](research/model_shadow/README.md), [ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md](ML_RL_IMPLEMENTATION_FRAMEWORK_2026-10-14.md) |
| History and design notes | [archive/](archive/), [NUMERICAL_MODEL_REGISTER.md](archive/root_documents_2026-10-14/NUMERICAL_MODEL_REGISTER.md), [H0_DATASET_CARD.md](archive/root_documents_2026-10-14/H0_DATASET_CARD.md), [DATA_SOURCE_REGISTER.md](archive/root_documents_2026-10-14/DATA_SOURCE_REGISTER.md), [HISTORICAL_LINK_INDEX.md](HISTORICAL_LINK_INDEX.md) |

**Historical root documents (14 October 2026):** ten retired design, audit and ledger documents now live in [the root-document archive](archive/root_documents_2026-10-14/README.md). Frozen historical citations retain their original paths; use [the recovery map](HISTORICAL_LINK_INDEX.md#root-document-archive-2026-10-14) or the archive's [original-link context](archive/root_documents_2026-10-14/LINK_RECOVERY.md).

## Sports covered

Baseball (MLB, KBO, NPB), cricket, basketball (NBA, WNBA, NBL, European and Asian leagues), ice hockey, tennis, soccer, rugby league, rugby union, Australian rules (AFL, AFLW) and American football. Each has a sport block in [prompt 1](research/prompts/1_GAME_CARD.md) that sets the research list, the distribution to build by hand and the family checks.

## Honesty and limits

New numeric forecasts are experimental model-assisted primary research; historical manual cards remain uncalibrated analyst scenarios. The framework tests its own rules against settled results, publishes the failures, and changes a rule only after a pre-registered test ([HYPOTHESIS_REGISTER.md](HYPOTHESIS_REGISTER.md)). Past results are a research aid; an empty archive file is missing data, not a finding. Read [LICENSE.md](LICENSE.md) before reuse.

## October 14 ML review and complete prompts

[Implementation review](research/verification/framework_change_2026-10-14-5/ML_WORKSHOP_REVIEW.md) · [full prompts 1–8](research/prompts/README.md) · [individual game prompt with eleven sport/upcoming-game sections](research/prompts/1_GAME_CARD.md) · [artifact admission](research/model_shadow/ARTIFACT_PROVENANCE.md). Useful development mechanisms exist, but prospective predictive skill and RL benefits remain unestablished. Control CR-2026.10.14-R3; suite P-2026.10.14-v11.3.

## Research completion timing (15 October 2026)

[TIMING_RESEARCH_PROTOCOL](TIMING_RESEARCH_PROTOCOL.md) replaces scheduled lead deadlines with comprehensive research completion for every sport. Research may continue after play starts. Verified pre-start inputs with no outcome exposure can be CLEAN_PRE_START_INPUTS, while post-start issue and genuinely prospective pre-start release remain separate. [Current prompts](research/prompts/README.md) use P-2026.10.16-v18.0; no old card or model is upgraded.

**Primary ML/RL (15 October 2026):** [PRIMARY_PREDICTION_PROTOCOL](PRIMARY_PREDICTION_PROTOCOL.md) governs new experimental model-assisted primary rows and sports-only model-selection feedback. Actual per-event execution and receipts required; no old artifact is automatically qualified.

**Current primary integrity review:** [review and comparison](research/verification/framework_change_2026-10-15-4/REVIEW.md). V3 retains deterministic mixing and fixes known-at replay, duplicate learning, parameter admission and receipts; prospective predictive gain remains unproven.

**Preferred historical recovery:** [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md) applies to every sport and competition. Missing, incomplete or incorrect local history is researched online first, with reviewed web rows usable in the named primary input scope; shared archive maintenance is separate. Source/known-at checks and unsupported-model limits remain.


**Strict research completion:** [RESEARCH_COMPLETION_PROTOCOL](RESEARCH_COMPLETION_PROTOCOL.md) requires full research, all applicable sport procedures and every requested contract assessment irrespective of model calibration/runtime, data/lineup gaps, kickoff or mini/write blockers. Supported automatic analyst comparisons stay NOT_PRIMARY; missing numerical ML never means stop research. The A9 evidence matrix is mandatory.


**Research retention before model availability (RETAIN-v1).** [RESEARCH_RETENTION_PROTOCOL](RESEARCH_RETENTION_PROTOCOL.md) supersedes EXEC-v1's model prerequisite for recording/import. Write every identified researched event under its reconciled working P-ID and canonically retain it through verified import even if the model/adapter/runtime/module/baseline/calibration/receipt is absent or failed. Use RESEARCH_ONLY_NO_MODEL, explicit execution reason and blank nonexistent artifact paths; keep model p_card NOT_ESTIMATED and supported analyst_p NOT_PRIMARY. Missing ML never by itself blocks the ID or a source-backed settlement. Retain verified settled labels for future model development with source/known-at/revision/feature status; only actual frozen experts can supply Hedge losses. Never invent probabilities, execution, final scores or pregame timing. Identity/custody/write conflicts remain real blockers.


**Model use and mandatory running-log record (owner clarification, 16 October 2026).** Use the supported ML/RL mechanisms when they are available for the exact sport, competition and endpoint. Whether a model exists or not, assign the reconciled permanent P-ID, append the researched game card to the active running mini-log, read it back and advance its footer. A missing sport-specific model must not leave an otherwise recordable game as intake-only, unissued or without an ID. With no verified model output, record RESEARCH_ONLY_NO_MODEL, the actual reason and supported analyst work; never invent model probabilities or receipts. Carry that same P-ID through verified canonical import; do not allocate another ID. Before an authorized import, the local card may truthfully say PENDING_IMPORT; that status never cancels its ID or running-log entry. Identity/allocation conflicts, frozen or inaccessible originals and real write failures still block only the affected mutation. Verified settlements remain available for future model development in both paths.

See [RETAIN-v1](RESEARCH_RETENTION_PROTOCOL.md). This is an editorial clarification of the existing two-path behavior; no model, numerical policy or format change.
