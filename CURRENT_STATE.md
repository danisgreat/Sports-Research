# Current state

> Maintained by hand. The import step (prompt 4), the rollover step (prompt 5), the retrospective (prompt 6) and any rule change update this page in the same commit as the change they describe. Other documents state rules and history; this page alone states what is true now. If this page disagrees with [GAME_LOG_STATUS_CURRENT.md](GAME_LOG_STATUS_CURRENT.md) or the active Combined Log header, stop and report the disagreement; do not guess.

## Authority

| Item | Value |
|---|---|
| Status | ACTIVE |
| Method | MDS-2026.10.09-v9.0 (Markdown only) |
| Control revision | CR-2026.10.09-R5 |
| Scoring version | SCV-2026.10.09-v5 |
| Mini-log format | `mini-log-5` (`mini-log-4`, `mini-log-3` and `mini-log-2` minis in progress are still accepted) |
| Settlement format | `mini-settlement-4` (`mini-settlement-3` and `mini-settlement-2` still accepted) |
| Freeze | None. Custody is the git history of `main` (CURRENT_RULES §9). Cards record the HEAD SHA they read. The last control manifest, `CONTROL_MANIFEST_2026-10-09-3.md`, is in [archive/controls/](archive/controls/). |
| Highest committed canonical ID | **P-556** |
| Next canonical ID | **P-557** (equal to the line in GAME_LOG_STATUS_CURRENT.md) |
| Reserved IDs | P-518 to P-522 |
| Active Combined Log | [prediction logs/PREDICTION_LOG_COMBINED_7.md](prediction%20logs/PREDICTION_LOG_COMBINED_7.md) |
| Previous parts | Parts 1 to 6, immutable; Part 6 keeps its original P-518 to P-522 source block |
| Final settlement register | All 72 event records through P-556 are final-settled: [final_settlement_2026-10-09](research/verification/final_settlement_2026-10-09/REPORT.md). No record is performance-certified. |

## Selection rules (provisional until the prospective window completes)

- Only Rank 1 and Rank 2 count as wins (Rule T2). A Rank-1 loss gets a deep retrospection (Rule R1). Supplied contracts are reference only (Rule P4).
- `p_card` ceiling 90%. Rank-1 gate: `p_card` at least 62% and a lead of at least 4 points over the best non-complementary alternative. Rank 2: `p_card` at least 58%. Joint top-two failure above 35% means replace the weaker pick.
- Source: [SELECTION_RULES.md](SELECTION_RULES.md) (status PROVISIONAL).

## Scoreboard

Full tables: [research/scoreboard/SCOREBOARD.md](research/scoreboard/SCOREBOARD.md).

- Forecast cards scored: 71 (P-126 to P-556). Gated counted cohort: 0 cards (no card yet carries a recorded Rank-1 gate result). All forecast cards (historical, ungated): 79 counted wins in 134 live top-two rows = 59.0% (95% interval 50.5% to 66.9%). Rank 1 40-28, Rank 2 39-27, ranks 3-4 75-58 (informational).
- Nothing here is performance-certified.

## Sources

- Register: [SOURCES.md](SOURCES.md) (rules, source register, adapter statuses, exclusions, reachability matrix). The source adapters and parsers were removed; the routes are used by hand.
- No lineage audit has established independent collection for any source. Treat independence as unknown.

## Models

- No fitted model exists. Every card is an `UNCALIBRATED_ANALYST_SCENARIO` built by hand ([PROBABILITY_TOOLKIT.md](PROBABILITY_TOOLKIT.md), [LEAGUE_PROFILES.md](LEAGUE_PROFILES.md)).
- The numerical runtime and its model register are archived design notes ([NUMERICAL_MODEL_REGISTER.md](NUMERICAL_MODEL_REGISTER.md)).

## Where things are

| Need | Document |
|---|---|
| Rules | [CURRENT_RULES.md](CURRENT_RULES.md), [METHOD.md](METHOD.md), [SELECTION_RULES.md](SELECTION_RULES.md) |
| Operator prompts | [research/prompts/](research/prompts/README.md), [PROMPTS.md](PROMPTS.md) |
| Card, mini and log formats; self-audit checklists | [CARD_AND_LOG_TEMPLATES.md](CARD_AND_LOG_TEMPLATES.md) |
| Probability tables | [PROBABILITY_TOOLKIT.md](PROBABILITY_TOOLKIT.md) |
| League scoring levels | [LEAGUE_PROFILES.md](LEAGUE_PROFILES.md) |
| Base rates and regimes | [BASE_RATES_REGISTER.md](BASE_RATES_REGISTER.md) |
| Sources and reachability | [SOURCES.md](SOURCES.md) |
| Previous results | [ARCHIVE_USE_GUIDE.md](ARCHIVE_USE_GUIDE.md), [Previous Sports Results/README.md](Previous%20Sports%20Results/README.md) |
| Scoring | [SCORING_AND_VALIDATION.md](SCORING_AND_VALIDATION.md) |
| Verification | [VERIFICATION_PROTOCOL.md](VERIFICATION_PROTOCOL.md) |
| Proposed improvements | [HYPOTHESIS_REGISTER.md](HYPOTHESIS_REGISTER.md) |
| Retrospective and recommendation status | [FRAMEWORK_RETROSPECTIVE_2026-10-09.md](FRAMEWORK_RETROSPECTIVE_2026-10-09.md) |
| Superseded documents | [archive/superseded_2026-10-09/](archive/superseded_2026-10-09/README.md), `archive/controls/` |
