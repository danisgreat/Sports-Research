# Current state

> Maintained by hand. Import, rollover, retrospective and framework changes update this page with the corresponding work. Reconcile current values with the current section of [GAME_LOG_STATUS_CURRENT.md](GAME_LOG_STATUS_CURRENT.md), canonical entries and dated state addenda. A Combined Log opening header is a historical snapshot, not a current allocation record. A genuine current-record disagreement blocks allocation; do not guess or run retired tools named in old headers.

## Authority

| Item | Value |
|---|---|
| Status | ACTIVE |
| Method | MDS-2026.10.11-v10.0 (Markdown only) |
| Control revision | CR-2026.10.11-R1 |
| Scoring version | SCV-2026.10.11-v6 (historical v5 views retained) |
| Selection version | SEL-2026.10.11-v2 / P_ORDER_V2; alternatives recorded as shadows |
| Mini-log format | `mini-log-6` (in-progress `mini-log-2` through `mini-log-5` retain their format) |
| Settlement format | `mini-settlement-5` (earlier settlement formats remain accepted) |
| Freeze | None. Custody is the git history of `main` (CURRENT_RULES §9). Cards record the HEAD SHA they read. The last control manifest, `CONTROL_MANIFEST_2026-10-09-3.md`, is in [archive/controls/](archive/controls/). |
| Highest committed canonical ID | **P-579** |
| Next canonical ID | **P-580** (equal to the line in GAME_LOG_STATUS_CURRENT.md) |
| Reserved IDs | P-518 to P-522 |
| Active Combined Log | [prediction logs/PREDICTION_LOG_COMBINED_7.md](prediction%20logs/PREDICTION_LOG_COMBINED_7.md) |
| Previous parts | Parts 1 to 6, immutable; Part 6 keeps its original P-518 to P-522 source block |
| Final settlement register | All 72 event records through P-556 are final-settled: [final_settlement_2026-10-09](research/verification/final_settlement_2026-10-09/REPORT.md). P-557 to P-576 were imported final-settled on 2026-10-11; P-577 to P-579 were imported as `PENDING_EVENT` and carry forward to the next mini (open carryover 3): [mini_import_P-556_P-579_2026-10-11](research/verification/mini_import_P-556_P-579_2026-10-11/CANONICAL_IMPORT_REPORT.md). No record is performance-certified. |

## Selection rules (provisional until the prospective window completes)

- Only Rank 1 and Rank 2 count as wins (Rule T2). A Rank-1 loss gets a deep retrospection (Rule R1). Supplied contracts are reference only (Rule P4).
- `p_card` selection ceiling 90%, never a probability clip. Original Rank-1 gate: at least 62% and a 4-point lead over the best eligible non-complementary alternative. Primary order is decreasing p_card; Rank-2 floor 58% is disclosed. Joint failure is diagnostic; RET03 gate, RET04 different-quantity Rank 2 and XCARD6 diversification are separate frozen shadows. Up to four supported candidates; qualitative/NO_FORECAST research is retained.
- Source: [SELECTION_RULES.md](SELECTION_RULES.md) (status PROVISIONAL).

## Scoreboard

- **v10 prospective measurement:** 0 issued v10 cards at this release; paired baseline-relative skill NOT_COMPUTABLE. No old card is relabelled or given a backfilled baseline. [Implementation and pending work](research/verification/framework_change_2026-10-11-1/IMPLEMENTATION.md).
- **Historical v5 snapshot follows:** original cohorts and figures remain unchanged; these are descriptive, not prospective v10 evidence.

Full tables: [research/scoreboard/SCOREBOARD.md](research/scoreboard/SCOREBOARD.md).

- Forecast cards scored: 91 (P-126 to P-576). Gated counted cohort: 0 cards (no card yet carries a recorded Rank-1 gate PASS). RANK1_UNSTABLE cohort: 20 cards (P-557 to P-576), 34 counted wins in 40 live top-two rows = 85.0% (95% interval 70.9% to 92.9%). All forecast cards (historical, ungated): 113 counted wins in 174 live top-two rows = 64.9% (95% interval 57.6% to 71.6%). Rank 1 56-32, Rank 2 57-29, ranks 3-4 106-67 (informational).
- Last cohort retrospective: [2026-10-11](research/verification/retrospective_2026-10-11/RETROSPECTIVE_REPORT.md), new cohort P-557 to P-576 against P-126 to P-556. Rank 1 80.0% (58.4% to 91.9%) does not beat Rank 2 90.0% (69.9% to 97.2%) or ranks 3-4 77.5%. Top-two Brier 0.131 against climatology 0.128 (skill -0.03). Every RANK1_UNSTABLE top-two pair covers itself (stated joint failure 0.0%, realised all-lost 0 of 20), so its counted rate reflects line choice, not skill. 0 of 20 cards passed the Rank-1 gate; experiment SEL-1 has 1 of 8 week-blocks and no PASS card, so the gate stays provisional. Seven proposals (RET-01 to RET-07) are `PROPOSED_NOT_TESTED` in [HYPOTHESIS_REGISTER.md](HYPOTHESIS_REGISTER.md).
- Nothing here is performance-certified.

## October 11 implementation status

Prompts 1–8 and their supporting rules/templates/examples are replaced under the user-authorized v10 release. RET-02/05/06/07 are implemented as document/measurement/source-process controls; RET-03/04 are shadow recording protocols, not validated replacements. **Run 2 (same day):** the NBL profile was refreshed to the 2023-25 window (`LP-2026.10.11-v2`; the 2022-24 row is retained as the comparator), the KBO and NPB extra-innings shares were withdrawn as `NOT_ESTIMABLE` after the audit showed placeholder columns, a 29-game 2026-27 NBL snapshot was added to the archive, and the local-machine reachability column of the SOURCES matrix was probed by hand ([implementation](research/verification/framework_change_2026-10-11-2/IMPLEMENTATION.md)). Source lineage audits (SRC-04) and the repair of the archive defects found remain DATA_PENDING. All predictive effects remain untested; FC10-PROFILE-v1 predictive acceptance is BLOCKED_DESIGN. Original RET registrations and the dated retrospective remain unchanged; versioned amendments are in HYPOTHESIS_REGISTER. No log, grade, historical forecast, existing raw CSV or P-ID changed in either release; run 2 added one new partial CSV (`Basketball/NBL/2026`).

## Sources

- Register: [SOURCES.md](SOURCES.md) (rules, source register, adapter statuses, exclusions, reachability matrix). The source adapters and parsers were removed; the routes are used by hand.
- No lineage audit has established independent collection for any source. Treat independence as unknown.

## Models

- No fitted model exists. Supported numeric cards are `UNCALIBRATED_ANALYST_SCENARIO`; otherwise retain `UNCALIBRATED_QUALITATIVE` or `NO_FORECAST` with missing values explicit ([PROBABILITY_TOOLKIT.md](PROBABILITY_TOOLKIT.md), [LEAGUE_PROFILES.md](LEAGUE_PROFILES.md)).
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
| Retrospective and recommendation status | [FRAMEWORK_RETROSPECTIVE_2026-10-09.md](FRAMEWORK_RETROSPECTIVE_2026-10-09.md); latest cohort retrospective [retrospective_2026-10-11](research/verification/retrospective_2026-10-11/RETROSPECTIVE_REPORT.md) (register status in its §6) |
| Superseded documents | [archive/superseded_2026-10-09/](archive/superseded_2026-10-09/README.md), `archive/controls/` |
