# METHOD: current authority

Status: **ACTIVE**. Method **MDS-2026.10.09-v9.0**. Control revision **CR-2026.10.09-R5**. Scoring **SCV-2026.10.09-v5**. Current values of the changing state (next ID, active log, scoreboard) are in [CURRENT_STATE.md](CURRENT_STATE.md).

## The method in one page

1. **The framework is Markdown.** Rules, formats, prompts, sources, base rates, league profiles and probability tables are documents; the archive of past results is CSV. No code and no JSON are used or needed ([CURRENT_RULES.md](CURRENT_RULES.md) §0).
2. **Read, then forecast.** Every task opens with a reading receipt of the current documents, and every card cites the rules, sources and past results it used ([CURRENT_RULES.md](CURRENT_RULES.md) §1, [ARCHIVE_USE_GUIDE.md](ARCHIVE_USE_GUIDE.md)).
3. **Event first.** Build one distribution of the sporting outcome by hand, then price four candidates from it. Supplied contracts are reference only (Rule P4). Rank by `p_card`.
4. **Top two count.** Only Rank 1 and Rank 2 can count as wins (Rule T2). A Rank-1 loss needs the eight-part deep retrospection (Rule R1).
5. **Gate and floors.** Rank-1 gate 62% and 4 points, Rank-2 floor 58%, joint failure warning 35% ([SELECTION_RULES.md](SELECTION_RULES.md)).
6. **Honest labels.** Every probability is an `UNCALIBRATED_ANALYST_SCENARIO`. Nothing is performance-certified. SPORTS_ONLY / MARKET_BLIND.
7. **Custody is git.** Issued bytes never change. Corrections are dated addenda. Published changes are commits on `main` ([CURRENT_RULES.md](CURRENT_RULES.md) §9).

## This version (v9.0, 2026-10-09)

The October 9 prediction repair (R4) and the framework-retrospective implementation (R3) built a Python runtime, JSON registries, validators and a hash-manifest freeze around the method. On 2026-10-09 all of that was removed (commits `a64675cf7` to `a93352c30`; last working state at `37203fc2b`), and the rules it carried were moved into documents:

| Purpose | Current file |
|---|---|
| Operating rules | [CURRENT_RULES.md](CURRENT_RULES.md) |
| Gate, families, grades, failure classes | [SELECTION_RULES.md](SELECTION_RULES.md) |
| Operator prompts and the mini lifecycle | [research/prompts/README.md](research/prompts/README.md), [PROMPTS.md](PROMPTS.md) |
| Card, mini, settlement and log formats; self-audits | [CARD_AND_LOG_TEMPLATES.md](CARD_AND_LOG_TEMPLATES.md) |
| Probability tables by hand | [PROBABILITY_TOOLKIT.md](PROBABILITY_TOOLKIT.md) |
| League scoring levels and shapes | [LEAGUE_PROFILES.md](LEAGUE_PROFILES.md) |
| Base rates and regime multipliers | [BASE_RATES_REGISTER.md](BASE_RATES_REGISTER.md) |
| Sources, reachability, exclusions | [SOURCES.md](SOURCES.md) |
| Previous results | [ARCHIVE_USE_GUIDE.md](ARCHIVE_USE_GUIDE.md), [Previous Sports Results/README.md](Previous%20Sports%20Results/README.md) |
| Scoring and counting | [SCORING_AND_VALIDATION.md](SCORING_AND_VALIDATION.md) |
| Verification by hand | [VERIFICATION_PROTOCOL.md](VERIFICATION_PROTOCOL.md) |
| Hypotheses and experiments | [HYPOTHESIS_REGISTER.md](HYPOTHESIS_REGISTER.md) |
| Sport rules | `RULES_<SPORT>.md`, [LEAGUE_RULES_SOCCER.md](LEAGUE_RULES_SOCCER.md), [LEAGUE_RULES_CRICKET.md](LEAGUE_RULES_CRICKET.md) |
| Retrospective | [FRAMEWORK_RETROSPECTIVE_2026-10-09.md](FRAMEWORK_RETROSPECTIVE_2026-10-09.md) |

What was suspended with the code, and is therefore not available: fitted models and calibrators, the numerical runtime ([NUMERICAL_MODEL_REGISTER.md](NUMERICAL_MODEL_REGISTER.md) is now a design note), live qualification and certification, and the daily shadow job. Issued forecasts keep their original values and timestamps. P-518 to P-522 remain reserved.

Earlier method statements (v8.4 and before) are kept in [archive/superseded_2026-10-09/METHOD.md](archive/superseded_2026-10-09/METHOD.md) and [archive/status_notes/](archive/status_notes/SUPERSEDED_STATUS_PARAGRAPHS_2026-10-09.md).
