# Sports Research

A sports-only, market-blind forecasting framework and custody/evaluation harness across eleven sport sections. Controls, forecasts and evidence live in Markdown, CSV and text; all code lives under [`ml/`](ml/README.md).

<!-- BEGIN GENERATED README HEADER (python -m ml state --write) -->

*Generated from `VERSIONS.csv` and the registered plan; do not edit by hand (`python -m ml state --write`).*

| Field | Current value |
|---|---|
| Release | MDS-2026.11.18-v29.1 · CR-2026.11.18-R2 · P-2026.11.18-v29.1 · SCV-2026.11.18-v20 · SEL-2026.10.22-v4 |
| Active workflow | **ONE-CHAT-v3** — [Runbook](research/one_chat/RUNBOOK.md) · [Chat brief](research/external/ONE_CHAT_BRIEF_v29.0.md) |
| Registered plan (Track P) | [EVALUATION_PLAN_v29.0](research/external/EVALUATION_PLAN_v29.0.md) · **600-game horizon** · Live seals on `forecast-seals` (`python -m ml one-chat score`) |
| Historical validation (Track H) | [HPPV-v1](research/verification/historical_pre_event_v1/README.md) · 685 cards / 3,150 rows (280 with stated `p`) · 0 Tier-A (`HISTORICAL_EVIDENCE_INSUFFICIENT`) |
| Canonical log IDs | Highest `P-685` · Next **`P-686`** · Live state in [CURRENT_STATE.md](CURRENT_STATE.md) |

<!-- END GENERATED README HEADER -->

## Start here (active ONE-CHAT-v3 workflow)

1. **[Runbook](research/one_chat/RUNBOOK.md)** — how to prepare, register, seal (`forecast-seals`), settle and score one-chat cards across parallel chats.
2. **[Registered Evaluation Plan (v29.0)](research/external/EVALUATION_PLAN_v29.0.md)** — population, immutable request/card custody, 14-day settlement deadline, and the anytime-valid empirical-Bernstein confidence sequence (600-game horizon, alpha = 0.05, practical threshold 0.01).
3. **[Chat Brief (v29.0)](research/external/ONE_CHAT_BRIEF_v29.0.md)** & **[Upload Package](research/external/README.md)** — what to upload to each research chat (`ONE_CHAT_BRIEF_v29.0.md`, [`ml/kit/sr_kit.py`](ml/kit/sr_kit.py), kit parameters, and current access/source lists).
4. **[CURRENT_STATE.md](CURRENT_STATE.md)** — live generated state, canonical IDs, scoreboard, and version pointers.
5. **[CORE.md](CORE.md)** — standing honesty, custody, `SPORTS_ONLY / MARKET_BLIND`, `STATS-ONLY-v2`, `ML-SEP-v1` and `FREEZE-v1` rules.

## Daily commands

```text
python -m ml one-chat prepare --message CHAT1.txt --mini MINI21 --out <prep>/MINI21
python -m ml one-chat register-requests --folder <prep>/MINI21
python -m ml one-chat seal --watch <minis_dir>
python -m ml one-chat intake --from-seals --out research/one_chat/intake/<run>
python -m ml one-chat score --intake <intakes> --outcomes <outcomes> --out research/one_chat/scores/<run>
python -m ml state --write
```

## Honesty and limits

- **SPORTS_ONLY / MARKET_BLIND:** no odds, tips, line movement or prediction markets in research or pricing. Sources that carry prices may supply sporting fields only with prices dropped (`STATS-ONLY-v2`).
- **Separate evidence tracks:** Historical evidence (**Track H**, [HPPV-v1](research/verification/historical_pre_event_v1/README.md)) and prospective evidence (**Track P**, [EVALUATION_PLAN_v29.0.md](research/external/EVALUATION_PLAN_v29.0.md)) are never pooled.
- **No performance certification:** fitted models stay separate from cards until promoted (`ML-SEP-v1`); nothing here is certified until Track P crosses its registered threshold.

## Document map

| Area | Primary files |
|---|---|
| Active operation (`ONE-CHAT-v3`) | [RUNBOOK](research/one_chat/RUNBOOK.md), [EVALUATION_PLAN_v29.0](research/external/EVALUATION_PLAN_v29.0.md), [ONE_CHAT_BRIEF_v29.0](research/external/ONE_CHAT_BRIEF_v29.0.md), [research/one_chat/](research/one_chat/README.md), [VERSIONS.csv](VERSIONS.csv) |
| Standing authority & state | [CURRENT_STATE.md](CURRENT_STATE.md), [CORE.md](CORE.md), [RULES_REFERENCE.md](RULES_REFERENCE.md), [SCORING_AND_VALIDATION.md](SCORING_AND_VALIDATION.md), [AUDIT_REVIEW_PROTOCOL.md](AUDIT_REVIEW_PROTOCOL.md), [CHANGELOG.md](CHANGELOG.md) |
| Probability, kit & code | [`ml/`](ml/README.md), [`ml/kit/sr_kit.py`](ml/kit/sr_kit.py), [PROBABILITY_TOOLKIT.md](PROBABILITY_TOOLKIT.md), [PARAMETERS.md](PARAMETERS.md), [SIMULATION_PROTOCOL.md](SIMULATION_PROTOCOL.md) |
| Sport rules (10 sports + Other) | [RULES_BASEBALL.md](RULES_BASEBALL.md), [RULES_BASKETBALL.md](RULES_BASKETBALL.md), [RULES_ICE_HOCKEY.md](RULES_ICE_HOCKEY.md), [RULES_SOCCER.md](RULES_SOCCER.md), [RULES_CRICKET.md](RULES_CRICKET.md), [RULES_TENNIS.md](RULES_TENNIS.md), [RULES_NRL_RUGBY.md](RULES_NRL_RUGBY.md), [RULES_RUGBY_UNION.md](RULES_RUGBY_UNION.md), [RULES_AFL.md](RULES_AFL.md), [RULES_AMERICAN_FOOTBALL.md](RULES_AMERICAN_FOOTBALL.md) |
| Sources & availability | [SOURCES.md](SOURCES.md), [RESEARCH_SOURCE_REGISTER.md](RESEARCH_SOURCE_REGISTER.md), [ROSTER_AVAILABILITY_PROTOCOL.md](ROSTER_AVAILABILITY_PROTOCOL.md), [HISTORICAL_SOURCE_PROTOCOL.md](HISTORICAL_SOURCE_PROTOCOL.md) |
| Logs, scoreboard & learning | [Active Combined Log (Part 11)](prediction%20logs/PREDICTION_LOG_COMBINED_11.md), [GAME_LOG_STATUS_CURRENT.md](GAME_LOG_STATUS_CURRENT.md), [SCOREBOARD.md](research/scoreboard/SCOREBOARD.md), [HYPOTHESIS_REGISTER.md](HYPOTHESIS_REGISTER.md), [ML_PIPELINE.md](ML_PIPELINE.md) |
| Retained legacy routes & history | [ACTIVE_FILE_INDEX.md](ACTIVE_FILE_INDEX.md), [research/prompts/](research/prompts/README.md), [EXTERNAL_RESEARCH_PROTOCOL.md](EXTERNAL_RESEARCH_PROTOCOL.md), [HISTORICAL_LINK_INDEX.md](HISTORICAL_LINK_INDEX.md), [archive/](archive/), [LICENSE.md](LICENSE.md) |

*Previous long-form README preserved byte-for-byte at [`cb97bbc2a`](https://github.com/danisgreat/Sports-Research/blob/cb97bbc2a9f882e7f8a093648b6137315951da8b/README.md). Working clone outside OneDrive: `C:\Users\danie\Projects\Sports-Research`.*
