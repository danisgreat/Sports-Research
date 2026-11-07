# Effect tables: the only sizes an adjustment may use (EFFECT-v1)

**P-2026.10.22-v24.0 · CR-2026.10.22-R2.** Implements REV-17 of the [framework revamp review](research/verification/review_2026-10-22_framework_revamp/REPORT.md). The authoritative table is [EFFECT_TABLES.csv](research/effect_tables/EFFECT_TABLES.csv); this page explains it and records what was measured on 22 October 2026. Rules for using a row are in [ADJUSTMENT_LEDGER_PROTOCOL](ADJUSTMENT_LEDGER_PROTOCOL.md) section 1.

## 1. Status classes

| Status | Meaning | Entry in the ledger |
|---|---|---|
| `MEASURED_CONFIRMED` | Estimated on this repository's verified finals and shown to help a held-out season (or a structural fact observed directly) | Full size |
| `MEASURED_NOT_CONFIRMED` | Estimated here, significant in sample, but not shown to improve a held-out season | Half size until λ exists |
| `MEASURED_NULL` | Estimated here; the interval contains zero | No adjustment |
| `LITERATURE_START` | A published estimate for another period or data set | Half size until λ exists |
| `NOT_ESTIMATED` | No usable number; the row lists the data needed | Scenario with declared weights only |

## 2. Measured on 22 October 2026 (NBA 2023-24 to 2025-26, NHL 2024-25)

Method (script outside the repository, MD-only rule): for each game after the league had played 300 team-games in the season, the home margin was regressed on the difference in season-to-date net rating (points for minus against per game, shrunk with k = 2, same-season earlier games only) and on rest flags built from the teams' previous game dates in the US Eastern calendar (back-to-back = played the previous calendar day; long rest = three or more days). Ordinary least squares with heteroskedasticity-robust (HC1) standard errors. Data: the learning store's verified finals ([nba_backfill](research/verification/framework_change_2026-10-22-2/nba_backfill/)). Output: [REST_EFFECT_MEASUREMENT.csv](research/effect_tables/REST_EFFECT_MEASUREMENT.csv).

| Competition | Term | Estimate | SE | Share of games | Reading |
|---|---|---:|---:|---:|---|
| NBA | Home edge (given net rating) | +1.66 pts | 0.35 | | Matches the toolkit's 1.71 |
| NBA | Net-rating coefficient | 0.90 | 0.03 | | Close to 1: the additive form is right and the average form (0.5) is not |
| NBA | Home team back-to-back | −2.88 pts | 0.71 | 17.5% | Significant in sample |
| NBA | Away team back-to-back | +2.74 pts to the home margin | 0.69 | 18.6% | Significant in sample |
| NBA | Home or away three or more rest days | +0.65, −0.02 | 0.66, 0.70 | 20.4%, 18.7% | Null |
| NHL | Home edge | +0.31 goals | 0.11 | | |
| NHL | Home or away back-to-back | −0.31, +0.29 goals | 0.28, 0.20 | 9.5%, 21.7% | Null |

**Out of sample, the NBA back-to-back effect did not help.** Fitting the two flags on 2023-24 and 2024-25 (−3.2 and +3.7 points) and applying them to 2025-26 left the Brier of home win at 0.2043 against 0.2037 without them (paired difference +0.0008, interval −0.0013 to +0.0029, 23 weeks). A significant coefficient in sample is therefore `MEASURED_NOT_CONFIRMED`, and enters a card at half size. This is the reason for the status classes: the literature's back-to-back estimate (Small 2007: 2.26 points, 1999-2000) and this repository's agree in sign and size, and still the adjustment has not been shown to add accuracy.

## 3. Structural facts already measured

NFL margins of exactly 3 and 7 occur in 14.2% and 8.3% of games against 5.7% and 5.2% under a discretised normal; hockey and baseball one-goal and one-run margins are 39.9% and 28.1% against 28.7% and 17.4% ([simulation review](research/verification/framework_change_2026-10-22-1/SIMULATION_REVIEW.md)). These are distribution shapes, handled by the margin table and by the simulators ([SIMULATION_PROTOCOL](SIMULATION_PROTOCOL.md)), not by adjustments.

## 4. What is missing, and what would fill it

Every `NOT_ESTIMATED` row names its data. The largest gap is player availability: the store's `PLAYER_AVAILABILITY.csv` holds no rows, so no availability effect can be measured until lineups are captured with publication times at every freeze (RESEARCH_RETENTION_PROTOCOL, REV-07). Prompt 7 should capture them for every game the league-day lane freezes; prompt 8 re-estimates the table between seasons.

## 5. Use

1. Find the row for the factor and competition. No row, or `NOT_ESTIMATED`: scenario only.
2. Apply the estimate to the reference centre, at the entry size the status gives. Print the row id, estimate, interval and entry size in the adjustment table.
3. Do not count an effect twice: a season-to-date net rating already contains the games a rested or tired team played; a player out for most of the window is already in the rating.
4. A new estimate appends a row; an old row is never overwritten.
