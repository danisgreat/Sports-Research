# Sports Research

**Executable forecast cycle (CYCLE-v1).** Apply [FORECAST_CYCLE_PROTOCOL](FORECAST_CYCLE_PROTOCOL.md). New contextual forecasts use MODEL_ASSISTED_CYCLE_V1 with a frozen exact-competition release, actual execution receipt, identical-contract baseline shadows and verified settlement feedback. Existing V3/tennis adapters retain their own cohorts; missing/unsupported inputs require a real failure receipt and retained research. This statistical/procedure release authorises experimental execution, not predictive qualification.

**Local keys until import; updated mini after every game (MINI-v1).** Apply [MINI_LOG_IDENTITY_PROTOCOL](MINI_LOG_IDENTITY_PROTOCOL.md). Prompts 1–3 use stable local event keys and never assign/reserve canonical P-IDs; prompt 4 alone assigns them during verified import. After each prompt-1 game request, append the research/addendum, update and read back the mini, and return its complete updated .md document. Preserve every owner-entered Upcoming game block and all earlier issued bytes. New formats: mini-log-10 / mini-settlement-10; earlier records retain their original formats.

**Persistent source research:** [EXH-v1](RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) requires alternative-source pursuit and independent corroboration across every applicable requirement. [Source observations](RESEARCH_SOURCE_REGISTER.md) preserve discoveries/limits. New settlements use mini-settlement-10 with a visible reuse section and S17. Unresolved required facts/corroboration keep information INCOMPLETE. Older originals and numerical policy remain unchanged.

**Persistent research and corroboration (EXH-v1).** Apply [RESEARCH_EXHAUSTIVENESS_PROTOCOL](RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) to every required field in research, logging, settlement and verification. If a source is incomplete, open alternatives and verify material facts with another independent source; track every remaining field and attempt. Unresolved facts/corroboration never qualify as complete information. New settlements use mini-settlement-10 with a visible source-discovery/reuse section, three source/attempt/closure CSVs and S17; older originals retain their rules and bytes. Consult [RESEARCH_SOURCE_REGISTER](RESEARCH_SOURCE_REGISTER.md) and prior package registers, recheck actual coverage, and continue discovery beyond them.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** For every game, research both sides' L5/L10/L15/L20 online under [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md), with opened sources, dated game rows and true n. Seek exact-game confirmed players, starting roles, bench/replacements and absences under [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md); projected players remain unconfirmed. The retired local results store and its derived profiles are not required inputs or fallbacks. Earlier archive-first directions are superseded.

**Required repository fallback (REF-v1).** Always keep [https://github.com/danisgreat/Sports-Research/tree/main](https://github.com/danisgreat/Sports-Research/tree/main) as the standing reference. If required local files are not fully accessible (missing, unreadable, truncated or incomplete), retrieve the actual required contents from this repository before declaring them unavailable. Apply [GITHUB_REFERENCE_PROTOCOL](GITHUB_REFERENCE_PROTOCOL.md): resolve one main commit SHA, record exact files/read time and fallback results in the existing reading receipt, and preserve the declared authority mode. Never substitute an unpublished local mini, claim unread content or treat viewing code as executing it. If authorized remote access also fails, record the real gap and continue independent work.

**Google Drive (DRIVE-v2, optional).** The owner's [Sports Research Google Drive folder](https://drive.google.com/drive/folders/1ChlwkiOvd8c4MTaLC5BvkLniWogrm8Lj?usp=drive_link) is an optional drop box under [GOOGLE_DRIVE_EXCHANGE_PROTOCOL](GOOGLE_DRIVE_EXCHANGE_PROTOCOL.md). A chat that cannot write the repository may upload its complete updated mini to `uploads/<YYYY-MM-DD>/<label>/` for the owner to import. Nothing has to be pushed or mirrored to Drive, Drive is never a source of controls, and an upload is not a commit, freeze or canonical record. Controls come from the latest `main` branch on GitHub.

**ML/RL scope (MLSCOPE-v1).** Owner instruction, 17 October 2026: ML/RL is not part of game research. Prompts 1–5 run no code, runtime pack, model, shadow or learning command and read no model output. Prompt 1 researches the game and derives every p_card by hand as ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY, using [PROBABILITY_TOOLKIT](PROBABILITY_TOOLKIT.md) arithmetic with every input and step shown. Prompts 2–5 create, settle, import and roll over records by hand. ML/RL runs only in prompt 6 (combined-log retrospective: learning-store ingest, model feedback, shadow settlement and comparisons) and prompt 8 (workshop code, releases, shadows and promotion decisions). Its findings reach game research only as reviewed Markdown changes (toolkit constants, base rates, rules) released through prompt 8. This rule supersedes any older text requiring prompts 1–5 to run ML, CYCLE-v1, CHAT-EXEC-v1, a capability receipt, an execution manifest or a learning-store export.

**Execution environments (ENV-v1).** Prompts 1–3 run in an external chat with internet access and read-only access to the GitHub repository at the latest `main` commit: no code, no repository writes, no hashes, a section-level reading budget, and every output returned in the reply for the owner to save. Prompts 4–8 run in this repository as the repository agent (`LOCAL_WORKING_TREE`); prompt 4 is the only intake point for external-chat output and computes the byte counts and SHA-256 the chat cannot. Details: [EXECUTION_ENVIRONMENT_PROTOCOL](EXECUTION_ENVIRONMENT_PROTOCOL.md).

A sports-only forecasting framework made of documents. It tells a research agent how to forecast, log and settle individual games across ten sports, how to verify past results online, and how to learn from the outcomes. **Controls and forecasts use Markdown/CSV/text.** New numerical primary forecasts are derived by hand with transparent arithmetic (ANALYST_PRIMARY_V1); the ML/RL workshop in [`ml/`](ml/README.md) is used only in the combined-log retrospective (prompt 6) and framework changes (prompt 8). Code stays in ml/; JSON/binary artifacts remain excluded.

**What is true now** (method, next ID, active log, scoreboard): [CURRENT_STATE.md](CURRENT_STATE.md). Method **MDS-2026.10.17-v22.2**, control **CR-2026.10.17-R6**, scoring **SCV-2026.10.16-v11**, selection **SEL-2026.10.12-v3**, prompts **P-2026.10.17-v22.2** (new mini-log-10). Game research (prompts 1–5) runs no code in any chat; an optional Google Drive drop box exists ([GOOGLE_DRIVE_EXCHANGE_PROTOCOL](GOOGLE_DRIVE_EXCHANGE_PROTOCOL.md)) and nothing must be pushed there. [October 12 implementation map](research/verification/framework_change_2026-10-12-1/IMPLEMENTATION.md) (audit R01–R38 and prediction items PR-01–PR-10) · [October 11 roadmap](research/verification/framework_change_2026-10-11-1/IMPLEMENTATION.md). Active files and usable data: [ACTIVE_FILE_INDEX.md](ACTIVE_FILE_INDEX.md). The 2026-10-09 runtime remains removed. Development models from the `ml/` workshop are `HISTORICAL_DEVELOPMENT` only; old workshop outputs cannot substitute for a new primary run; experimental primary use is now authorised under PRIMARY_PREDICTION_PROTOCOL, with no predictive certification.

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

Prompts 1 to 3 are run by an external chat with internet access that reads the latest `main` branch on GitHub, with no code and no repository writes; it returns its outputs for you to save. Prompts 4 to 8 are run by Claude Code in this repository: prompt 4 takes in the chats' outputs, prompt 7 extends the archive and prompt 8 improves the framework ([PROMPTS.md](PROMPTS.md)).

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

Baseball (MLB, KBO, NPB), cricket, basketball (NBA, WNBA, NBL, European and Asian leagues), ice hockey, tennis, soccer, rugby league, rugby union, Australian rules (AFL, AFLW) and American football. Each has its own [prompt 1 sport file](research/prompts/1_sports/), used with the [prompt 1 core](research/prompts/1_GAME_CARD.md), that sets the research list, the distribution to build by hand and the family checks.

## Honesty and limits

New numeric forecasts are uncalibrated analyst probabilities built by hand; historical model-assisted cards keep their original labels. The framework tests its own rules against settled results, publishes the failures, and changes a rule only after a pre-registered test ([HYPOTHESIS_REGISTER.md](HYPOTHESIS_REGISTER.md)). Past results are a research aid; an empty archive file is missing data, not a finding. Read [LICENSE.md](LICENSE.md) before reuse.

## October 14 ML review and complete prompts

[Implementation review](research/verification/framework_change_2026-10-14-5/ML_WORKSHOP_REVIEW.md) · [full prompts 1–8](research/prompts/README.md) · [individual game prompt: core](research/prompts/1_GAME_CARD.md) and [eleven sport files](research/prompts/1_sports/) · [artifact admission](research/model_shadow/ARTIFACT_PROVENANCE.md). Useful development mechanisms exist, but prospective predictive skill and RL benefits remain unestablished. Control CR-2026.10.14-R3; suite P-2026.10.14-v11.3.

## Research completion timing (15 October 2026)

[TIMING_RESEARCH_PROTOCOL](TIMING_RESEARCH_PROTOCOL.md) replaces scheduled lead deadlines with comprehensive research completion for every sport. Research may continue after play starts. Verified pre-start inputs with no outcome exposure can be CLEAN_PRE_START_INPUTS, while post-start issue and genuinely prospective pre-start release remain separate. [Current prompts](research/prompts/README.md) use P-2026.10.16-v19.2; no old card or model is upgraded.

**Primary ML/RL (15 October 2026; scope narrowed 17 October 2026):** [PRIMARY_PREDICTION_PROTOCOL](PRIMARY_PREDICTION_PROTOCOL.md) now governs workshop models used only in prompts 6 and 8 (MLSCOPE-v1); game cards are ANALYST_PRIMARY_V1.

**Current primary integrity review:** [review and comparison](research/verification/framework_change_2026-10-15-4/REVIEW.md). V3 retains deterministic mixing and fixes known-at replay, duplicate learning, parameter admission and receipts; prospective predictive gain remains unproven.

**Preferred historical recovery:** [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md) applies to every sport and competition. Missing, incomplete or incorrect local history is researched online first, with reviewed web rows usable in the named primary input scope; shared archive maintenance is separate. Source/known-at checks and unsupported-model limits remain.


**Strict research completion:** [RESEARCH_COMPLETION_PROTOCOL](RESEARCH_COMPLETION_PROTOCOL.md) requires full research, all applicable sport procedures and every requested contract assessment irrespective of model calibration/runtime, data/lineup gaps, kickoff or mini/write blockers. Supported automatic analyst comparisons stay NOT_PRIMARY; missing numerical ML never means stop research. The A9 evidence matrix is mandatory.


**Research retention before model availability (RETAIN-v2).** Retain every identified researched event under its stable local event key regardless of ML/runtime/baseline/calibration availability; use RESEARCH_ONLY_NO_MODEL and an honest execution disposition when needed. Prompts 1–3 neither assign nor reserve canonical P-IDs. Prompt 1 appends the full research card to the mini, updates its intake/footer, reads back the result and returns the complete updated Markdown document after every game request. Prompt 4 alone reconciles duplicates and assigns canonical P-IDs at import, preserving local originals and a local-to-canonical map. Verified labels remain future-development candidates; only real frozen bundles supply expert feedback. See RESEARCH_RETENTION_PROTOCOL and MINI_LOG_IDENTITY_PROTOCOL. Identity/custody/write conflicts remain real blockers; missing ML does not discard research.


**Local research record and updated-document delivery (owner update, 16 October 2026).** Use a stable local event key during research and local settlement; do not assign, reserve or advance any canonical P-ID. Append the researched card regardless of model availability, update intake and the local footer, verify the full mini and return its complete updated .md file after each game request. Prompt 4 alone assigns canonical IDs after duplicate/identity reconciliation and records the immutable local-to-canonical mapping. An already assigned canonical ID remains a reference, never a new pregame allocation. Preserve issued originals and actual timing. See MINI_LOG_IDENTITY_PROTOCOL.

See [RETAIN-v2](RESEARCH_RETENTION_PROTOCOL.md). This owner update changes local identity and delivery procedures; numerical model, selection and scoring formulas are unchanged.
