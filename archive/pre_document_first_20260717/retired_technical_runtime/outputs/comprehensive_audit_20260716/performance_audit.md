# Prediction performance and calibration audit — 2026-07-16

## Bottom line

The recorded prediction process is not currently auditable as a betting-performance system. The newest structured source has a gross 253-190-2 record (57.1% excluding pushes), but that number is materially distorted by exact complementary selections, repeated snapshots of the same event, mutable post-settlement rows, and the absence of prices/stakes. Ranking quality is below the workspace's own target: rank 1 is 69-34 (67.0%) and rank 4 wins 46 of 98 decisions (46.9%), versus the stated targets of at least 80% for rank 1 and at most 30% for rank 4 (`PREDICTION_RESULTS_LOG_v2.md:62`). Since 2026-07-10, the inversion is worse: rank 1 is 13-5 (72.2%), while rank 4 is 10-3 (76.9%).

This is not a small run of bad luck. The ledger's own flags identify projection and rank-slot errors as the dominant failure classes, while the ledger design makes headline hit rates look better than the underlying ranking performance.

## Scope and method

- Parsed all 437 non-template CSV records in `SPORTS_CALIBRATION_LEDGER_v2.csv` and all 449 non-template rows in the settled workbook table (`outputs/settlement_20260713/SPORTS_CALIBRATION_LEDGER_v2_settled.xlsx.inspect.ndjson:1-4`, workbook cells `A1:AU451`).
- Parsed 245 dated Markdown table rows in `PREDICTION_RESULTS_LOG_v2.md` and 171 in `PREDICTION_RESULTS_LOG_v3.md`.
- Reconciled records on `(card_id, rank, normalized option)`, checked rank and probability consistency, enumerated exact over/under and opposite-spread complements, and calculated accuracy, Brier score, and log loss only on W/L rows with a numeric probability.
- Metrics below are descriptive, not independently verified prospective results. The files do not preserve an immutable pre-event prediction timestamp/version.

## Source-of-truth reconciliation

| Source | Structured selections | Gross result | Problem |
| --- | ---: | ---: | --- |
| CSV ledger | 437 data rows + 1 embedded template | 246-185-2, plus 2 `UNGRADED` and 2 `U` | Stale; last structured card is missing later settlements |
| Settled XLSX | 449 data rows + 1 embedded template | 253-190-2, plus 2 `UNGRADED` and 2 `U` | Newest structured source, but still stops at 2026-07-13 |
| v3 later addenda | 8 further decided selections | 4-4 | Narrative-only; not synced to either ledger |

The 12 XLSX-only records are exactly three four-pick cards at workbook rows 440-451: `MLB-20260713-MIL-PIT` (2-2), `MLB-20260713-HOU-TEX` (3-1), and `WNBA-20260713-SEA-WAS-LIVE` (2-2). This explains the CSV-to-XLSX delta of 7 wins and 5 losses. See `csv_xlsx_diff.csv` and `PREDICTION_RESULTS_LOG_v3.md:42-45`.

The v3 log then adds France-Spain at 3-1 and LA-Minnesota at 1-3 (`PREDICTION_RESULTS_LOG_v3.md:34-40`). If those are appended to the workbook, the current gross count is 257-194-2, or 57.0% excluding pushes. This is a reconciliation only, not a certified KPI.

There is also a live contradiction inside v3: the header and pending index call LA-Minnesota settled (`PREDICTION_RESULTS_LOG_v3.md:5,12`) and the learning records the 1-3 result (`:39`), but the card row still says `PENDING PREGAME` (`:35`). That row must be replaced or versioned, not left in both states.

## Core performance

Using the settled XLSX as the latest structured snapshot:

- Overall: 253 W, 190 L, 2 P; 57.11% on 443 decisions.
- Mean stated probability: 54.28%; observed rate: 57.11%.
- Apparent Brier score: 0.2192; apparent log loss: 0.6261.
- Live-labelled records: 11-10 (52.4%) across 21 decisions and eight card IDs.
- Non-live-labelled records: 242-180-2 (57.3%), plus two void and two unresolved rows.

The apparent Brier score is better than a constant 57.1% forecast (about 0.245), but it cannot be accepted as prospective calibration because probability creation time is not locked and complementary outcomes are heavily duplicated.

### Rank performance

| Rank | W-L-P | Hit rate | Mean stated p | Verdict |
| ---: | ---: | ---: | ---: | --- |
| 1 | 69-34-0 | 67.0% | 65.5% | Below 80% target |
| 2 | 62-37-1 | 62.6% | 59.8% | Modest separation |
| 3 | 54-43-1 | 55.7% | 52.4% | Weak separation |
| 4 | 46-52-0 | 46.9% | 45.0% | Far above maximum 30% bottom-win target |
| 5 | 3-12-0 | 20.0% | 44.7% | Strong overstatement, n=15 |
| 6 | 10-5-0 | 66.7% | 40.5% | Severe inversion, n=15 |
| 7 | 6-2-0 | 75.0% | 39.6% | Severe inversion, n=8 |
| 8 | 3-5-0 | 37.5% | 36.7% | Small sample |

The rank-6/rank-7 inversions show that longer cards are not consistently ordered. The recent bottom-slot failure is more important: from 2026-07-10 onward, rank 4 won 10 of 13 decisions (76.9%); from 2026-07-12 onward it won 7 of 9 (77.8%). A rising all-pick hit rate in this window is therefore not evidence that ranking improved.

### Sport results

Canonical grouping is approximate because the source uses inconsistent labels such as `Soccer` versus `Soccer/FIFA World Cup`, `WNBA` versus `Basketball/WNBA`, and `MLB` versus `Baseball/MLB`.

| Canonical sport | Decisions | W-L-P | Hit rate | Brier | Assessment |
| --- | ---: | ---: | ---: | ---: | --- |
| AFL | 44 | 23-21-0 | 52.3% | 0.253 | Coin-flip level; no demonstrated edge |
| Baseball (other) | 24 | 15-9-0 | 62.5% | 0.210 | Small/mixed leagues |
| Basketball (other) | 115 | 60-55-0 | 52.2% | 0.240 | Near coin flip |
| Cricket | 97 decisions | 54-43-0, 2 void, 2 unresolved | 55.7% | 0.231 | Complement-heavy; phase model weak |
| KBO | 12 | 7-5-0 | 58.3% | 0.199 | Too small to trust |
| MLB | 44 rows / 42 decisions | 23-19-2 | 54.8% | 0.211 | Modest raw rate; duplicated/alternative lines |
| NPB | 4 | 2-2-0 | 50.0% | 0.261 | No conclusion |
| Soccer | 81 | 56-25-0 | 69.1% | 0.149 | Inflated by broad safety/ceiling outcomes and label mix |
| WNBA | 24 | 13-11-0 | 54.2% | 0.274 | Poor probability quality |

The soccer aggregate conceals a major taxonomy split: rows labelled simply `Soccer` are 45-12, while `Soccer/FIFA World Cup` rows are 11-13. These cannot be pooled without defining competition, market family, and selection policy. Adding the later LA-Minnesota 1-3 card makes the current WNBA gross result 14-14; its four stated probabilities produce a Brier score of about 0.306 for that card, worsening the already weak WNBA calibration.

Across the heuristic market-family parse, phase/innings totals are 131-126 with two pushes (51.0% on 257 decisions). This is the largest market family and shows essentially no directional edge. It matches the repeated narrative errors around pace propagation, T20 innings carry-forward, and live distribution tails (`PREDICTION_RESULTS_LOG_v3.md:39,45,46,50`).

## Complement and duplication distortion

This is the largest measurement defect.

- The CSV contains at least 150 exact complement pairs: 127 over/under pairs and 23 opposite-spread pairs.
- Those pairs occupy 300 of 437 records (68.6%) across 75 of 102 card IDs.
- Thirty-seven four-pick cards consist entirely of two exact complementary pairs. Their aggregate is 73 W, 73 L, and 2 unresolved. Apart from pushes/unresolved states, 2-2 is guaranteed by construction and says nothing about predictive skill.
- This is a lower bound: the detector did not count every moneyline/double-chance logical complement or correlated safety structure.

The ledger also counts the same Collingwood-Richmond options four times under four card IDs without a usable prediction timestamp or `supersedes` field: Richmond +38.5 at CSV rows 361/365/371/375, Under 165.5 at 362/366/372/376, Over 165.5 at 363/367/369/373, and Collingwood -38.5 at 364/368/370/374. These may represent time-varying re-ranks, but the current schema multiplies the same final outcome fourfold and cannot distinguish independent predictions from revisions.

Consequences:

1. Do not report all-selection hit rate as model accuracy.
2. Do not count a forced complement as a second bet or independent forecast.
3. Do not combine pregame, live, and re-ranked snapshots unless each has an immutable cutoff and an explicit `supersedes_prediction_id`.

## Calibration, ROI, and leakage limitations

ROI is not computable. The 47-column schema has no bookmaker, decimal odds/price, price timestamp, stake, closing line, commission/vig, or payout (`SPORTS_CALIBRATION_LEDGER_v2.csv:1`). The logs repeatedly describe cards as `Research-only, no odds` (for example `PREDICTION_RESULTS_LOG_v3.md:138`). Some raw ESPN JSON snapshots contain odds objects, but there is no mapping from those snapshots to card/selection IDs or proof that the displayed price was available at the prediction cutoff.

Probability calibration is also not independently auditable:

- The ledger has no `prediction_created_at`, event-start timestamp, model version, source snapshot hash, or immutable pre-settlement revision.
- Probability, retrospective result, settlement source, and error classification live in the same mutable row.
- At least 60 rows put explicit post-event material such as `Results log settlement sweep`, `final settlement`, or a final/quarter table into `frequency_count_base`, a field intended to describe the prediction base. Examples are CSV rows 235-240, 241-248, and 257-306. This is field contamination and prevents proof that the probability inputs were outcome-blind.
- The XLSX is a later export rather than a frozen pre-event artifact; v3 is openly edited after settlement.

The reported Brier/log-loss figures should therefore be labelled `RETROSPECTIVE / UNVERIFIED LOCK` until a pre-event snapshot trail exists.

## Data-integrity defects

- Unresolved status: `CRIC-ODI-20260620-AFG-IND` ranks 1 and 4 remain `U` because the exact five-over score was not verified (CSV rows 265 and 268). They are opposing Over/Under 25.5 selections and must be settled together or explicitly `UNRESOLVED`, not left outside the enumerated status schema.
- Ungraded phase markets: `CRIC-20260614-AUB-JBB` ranks 1 and 3 are `UNGRADED` for unavailable phase data (rows 50 and 52). This is defensible, but `VOID`, `UNGRADED`, and `U` need one documented taxonomy.
- Ten probability-bucket labels disagree with numeric probabilities: rows 418-422, 426, and 434-437 (for example, 0.86 labelled `60-69`).
- Six detected complement pairs have probability sums materially/borderline different from one; examples include 0.88 at rows 161/162 and 399/400, and 1.06 at rows 405/407.
- `top_pick_loss` and `bottom_pick_win` mix row-level and card-level semantics. Under row-level semantics, 18 top flags and 27 bottom flags are misplaced. Entire cards have the flag repeated on every selection (for example rows 207-210, 223-226, and 235-240), while other cards flag only the affected row. Penalty totals cannot be reproduced until the field level is defined.
- The embedded `TEMPLATE` row is stored inside both data tables and must always be manually excluded.
- Feature coverage is incomplete: form-delta verdict 254/437 (58.1%), officials source/timestamp 186/437 (42.6%), similar-condition form 217/437 (49.7%), and prediction triggers 209/437 (47.8%). Missingness is concentrated in older rows, so before/after process comparisons need a documented effective date.

## Causal error pattern

The retrospective flags point mainly to modelling and ranking, not rules or settlement:

| Recorded flag | Rows | Distinct cards |
| --- | ---: | ---: |
| Projection error | 126 | 55 |
| Rank-slot calibration error | 108 | 44 |
| Both projection + rank-slot | 95 | — |
| Source-status error | 5 | 4 |
| Ruleset error | 2 | 1 |
| Availability/eligibility error | 2 | 1 |
| Settlement-convention error | 0 | 0 |

These counts are not independent because some flags are copied card-wide, but the direction is clear. The recurring mechanisms are:

- Recent-form overreaction without matchup-level support: LA-Minnesota stacked Q1/first-half overs from LA's recent pace and went 1-3 (`PREDICTION_RESULTS_LOG_v3.md:39`).
- Failure to price opponent suppression into player props: Mbappé's historical SOT rate was overweighted against Spain's opponent-SOT suppression (`:40`).
- Failure to propagate or re-anchor phase state: Seattle-Washington did not carry a fast Q1 into the half (`:45`); Texas-Washington carried a hot powerplay too far through a later wicket collapse (`:50`).
- Under-modelled variance/tails: Brisbane-Essendon ignored simultaneous favourite continuation and trailing-team rebound routes (`:46`); MLB replacement-starter/bridge failure was repeatedly under-ranked (`:43-44`).
- Ranking alternatives instead of making one market decision: complement-heavy cards guarantee results but obscure whether the selected side had a real probability edge.

## Required fixes before the next KPI claim

1. Create one append-only canonical prediction table. Freeze `prediction_id`, `request_cutoff_utc`, event start, pregame/live state, model version, source snapshot IDs/hashes, probability, market line, bookmaker, odds, and stake before the event/phase resolves.
2. Put settlement in a separate table keyed to `prediction_id`; never edit the frozen probability/input fields. Record `settled_at`, official source, W/L/P/VOID/UNRESOLVED, payout, and retrospective flags there.
3. Record one selected side per market. Store the mathematical complement as metadata, not as another prediction. Separate recommended bets from scenario/safety alternatives.
4. Add `supersedes_prediction_id` for live re-ranks. Only the frozen snapshot requested at that cutoff enters its own cohort; do not multiply an outcome across undocumented revisions.
5. Reconcile the XLSX-only 12 rows and the v3-only eight decisions into the canonical store, then regenerate CSV/XLSX/log summaries from it. Fix the stale LA-Minnesota pending row.
6. Replace penalty bookkeeping with reproducible KPIs: rank-1 accuracy, calibration by locked probability bucket, Brier/log loss, closing-line value, and ROI after vig. Treat rank-4 wins as a ranking diagnostic, not an ordinary success added to the headline hit rate.
7. Enforce controlled enums and validation: canonical sport/league, market family, phase, prediction state, status, and card-vs-selection error flags. Block export on bucket/probability mismatch or unresolved complement inconsistency.
8. Put AFL, general basketball, WNBA, and phase/innings totals into `NO CLAIM / RESEARCH` mode until a new locked holdout sample shows improvement. The current data is near coin flip or poorly calibrated.
9. Trigger an automatic model review whenever rolling locked rank-1 hit rate is below target or rank-4 win rate exceeds 30%; the recent 10-3 rank-4 window would have stopped publication immediately.

## Machine-readable outputs

- `performance_summary.json`: full counts, calibration, recent windows, coverage, and source reconciliation.
- `sport_summary.csv`, `rank_summary.csv`, `calibration_buckets.csv`, `market_summary.csv`: metric tables.
- `complement_pairs.csv`, `cross_card_repeats.csv`, `ledger_issue_records.csv`, `csv_xlsx_diff.csv`: record-level audit evidence.

