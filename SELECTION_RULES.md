# Selection rules: the gate, the top two, the families and the grading codes

**Version SEL-2026.10.09-v1 (Markdown only).** This page holds every number and label that used to live in `selection_rules.json`, `regimes.json` and the taxonomy inside `top_two.py`, and the hand procedures that used to run in code. Those files were removed on 2026-10-09; the last copies are in git history at commit `37203fc2b`. A card, a settlement and a retrospective cite this page by section number, for example "(SELECTION_RULES §2)".

**Status of the numbers: PROVISIONAL.** The gate, the Rank-2 floor and the family thresholds were derived from the 2026-10-09 retrospective ([FRAMEWORK_RETROSPECTIVE_2026-10-09.md](FRAMEWORK_RETROSPECTIVE_2026-10-09.md) §3.2 and §7). They become binding only after a prospective window of at least 8 weeks (experiments SEL-1 and XCARD-5 in [HYPOTHESIS_REGISTER.md](HYPOTHESIS_REGISTER.md)). Until then nobody changes them on the strength of one event, and every card prints the numbers it used.

## 1. Constants

| Constant | Value | Meaning |
|---|---:|---|
| `p_card` ceiling | 0.90 | A proposition above 90% is degenerate and is not a candidate. |
| Rank-1 gate, floor | 0.62 | Rank 1 passes only with `p_card` at least 62%. |
| Rank-1 gate, margin | 0.04 | Rank 1 must lead the best non-complementary alternative by at least 4 points. |
| Legacy unstable cut | 0.60 | Cards issued before the gate labelled a Rank 1 below 60% `RANK1_UNSTABLE`. Old cards keep that split. |
| Rank-2 floor | 0.58 | Rank 2 is the best remaining row with `p_card` of at least 58%. |
| Joint top-two failure, warning | 0.35 | Above this the two picks share one driver. Replace the weaker pick. |
| Joint top-two failure, target | 0.30 | The aim when choosing Rank 2. |
| Adjustment threshold | 0.25 SD | An analyst adjustment above this that changes the top two makes the card `ADJUSTMENT_DEPENDENT`. |
| Decision block size | about 650 words | The page you would act on. Everything else is appendix. |
| Settlement SLA | 72 hours | Settle each card within 72 hours of its final. |
| Open carryover cap | 5 | More than five open `PENDING_EVENT` records is a breach; report it. |
| Capture window | 36 hours | A corners, half-time, period or player row needs a capture time within 36 hours after the scheduled start. |

## 2. The Rank-1 gate (hand procedure)

1. Price the whole ladder from the one distribution (section 5).
2. Sort by `p_card`, highest first. Rank 1 is the top row.
3. Find the **best non-complementary alternative**: the highest `p_card` among rows that are not the opposite side of Rank 1's own line. The opposite side of a line (Over 5.5 against Under 5.5, a team's +1.5 against the other team's -1.5) is never the alternative, because it is the same bet.
4. Gate = PASS when `p_card` of Rank 1 is at least 62% **and** (Rank 1 minus alternative) is at least 4.0 points. Otherwise the card is `RANK1_UNSTABLE`.
5. Print `**Rank-1 gate:** PASS|RANK1_UNSTABLE — p_card x%; best non-complementary alternative y%; margin z points`. The label must agree with the numbers on the same line. Recompute them before printing.
6. A failing gate is not an error. The card is scored in its own cohort, and the card says why no stronger proposition exists.

## 3. Rank 2 and the joint failure probability

**Choosing Rank 2.** Among the remaining rows with `p_card` of at least 58%, take the one that minimises P(Rank 1 and Rank 2 both lose), not simply the next-highest `p_card`. If no remaining row reaches 58%, take the highest and say that the floor was not met.

**Computing P(both lose) by hand.** Let L1 and L2 be the losing events of the two picks, read from the same grid.

| Picks | P(both lose) |
|---|---|
| Bracketing total: Over A and Under B with A below B | 0. The two losses cannot happen together (total at or below A, total at or above B). State it as "0.0% by construction". |
| Same direction on one quantity (Under 7.5 and Under 6.5) | The smaller loss probability, because the narrower loss event sits inside the wider one: P(L1 and L2) = min(P(L1), P(L2)). |
| Total and margin from one grid (Under 7.5 and a team +1.5) | Sum the grid cells in which both lose. Show the cells or the formula. |
| Winner and the same team's handicap (A to win and A +1.5, or A to win and A -1.5) | The losing events nest: A losing by 2 or more sits inside A losing, and A losing sits inside A failing to cover -1.5. When one loss contains the other, P(both lose) is the smaller of the two loss probabilities. |
| Different outcome spaces (a first-half row beside a full-game row) | No exact joint exists. Use the conservative bound min(P(L1), P(L2)) and say so. |

**General rule.** If one losing event contains the other, P(both lose) is the smaller loss probability. If the two losing events cannot happen together, it is 0. Otherwise add up the grid cells in which both rows lose and show them.

If P(both lose) is above 35%, replace the weaker pick with the best less-correlated candidate, re-rank by `p_card`, and write what changed.

## 4. Family rules

| Family | Rule | How to check |
|---|---|---|
| First-half Over 0.5 goals | Not Rank 1 unless `p_card` is at least **72%** from a half-split model (separate first-half and second-half rates). The soccer block also asks for 5 points over the next candidate. | Print the first-half and second-half lambdas. Compare with the league first-half goal share in [LEAGUE_PROFILES.md](LEAGUE_PROFILES.md) and [BASE_RATES_REGISTER.md](BASE_RATES_REGISTER.md) §7.3. |
| Baseball +1.5 run line | Not Rank 1 unless `p_card` is at least **65%**. | Print P(win) + P(lose by exactly 1), and the one-run share of the league from LEAGUE_PROFILES. |
| Tennis games rows | Only from the exact point-to-match tree **with a match-level form shock**. The plain independent-point tree over-states deciding sets (0.50 against a 0.358 reference). | Print P(deciding set) beside the reference in BASE_RATES_REGISTER §7.4. Explain a gap above about 8 points. |
| Corners rows | Only with a named settlement provider **and** a negative-binomial count model for the corners. | Name the provider in Settlement fields; print the mean, SD and the dispersion used. |
| Half-time, period and player rows | A named provider and a capture time within 36 hours after the start. | Settlement fields and Capture due. |

Record the result of every applicable family check in appendix A7.

## 5. Ladders: which lines to price

Price every candidate from the one distribution. Use half lines unless the sport allows pushes. Span the lines from about 2.5 SD below to 2.5 SD above the relevant mean (2.0 SD for cricket). Price the winner (or double chance where a draw exists), handicaps, the match total, team totals and period totals.

| Sport | Draw in full-game ladder | Line step (handicap / total / team total) | Ladder span (SD around the mean) | Integer lines allowed | Extra rows |
|---|---|---|---:|---|---|
| soccer | yes | 1 / 1 / 1 | 2.5 | no (half lines) | both teams to score |
| ice_hockey | no | 1 / 1 / 1 | 2.5 | no (half lines) |  |
| baseball | no | 1 / 1 / 1 | 2.5 | no (half lines) |  |
| basketball | no | 1 / 1 / 1 | 2.5 | no (half lines) |  |
| american_football | no | 1 / 1 / 1 | 2.5 | yes (pushes possible) |  |
| afl | no | 1 / 1 / 1 | 2.5 | no (half lines) |  |
| rugby_league | no | 1 / 1 / 1 | 2.5 | no (half lines) |  |
| cricket | no | 1 / 1 / 1 | 2 | no (half lines) |  |
| tennis | no | 1 / 1 / 1 | 2.5 | no (half lines) |  |

Soccer prices a draw in the full-game ladder; hockey, baseball, basketball, rugby, Australian rules and tennis do not (the endpoint rules resolve overtime, extra innings, extra time or tie-breaks inside the grid). A row with a possible push (American football integer lines) leaves the push mass out of the denominator: `p_card` = win ÷ (win + loss).

## 6. Regime flags

`Regime flags` on a card is `NONE` or a comma-separated list of `FINALS_COMPRESSION`, `EARLY_SEASON`, `CUP_ROTATION` and `RULE_CHANGE:<name>`. The measured multipliers on game totals are in the regime table in [BASE_RATES_REGISTER.md](BASE_RATES_REGISTER.md) (section "Regime flags"). Rules:

- Apply the table's **Recommended** column and nothing else. Where it reads 1.000 the 95% interval contains 1, so the distribution is **not** shifted.
- Record an applied multiplier in the adjustments table (name, target = total mean, size, SD units, basis `archive_estimate`).
- `FINALS_COMPRESSION` multipliers: AFL 0.943, MLB 0.924, NBA 0.970, NFL 1.057, NHL 0.917, NRL 0.938, WNBA 1.000. `EARLY_SEASON`: NBA 0.988, NHL 1.024, NRL 0.938; the others 1.000. `RULE_CHANGE:six_again` (NRL from 2020): 1.121.
- Not estimable from the archive, so no multiplier exists: `CUP_ROTATION` (needs lineups) and `RULE_CHANGE:kbl_foreign_player_2026_27` (no game under the rule yet). Flag them, say the effect is unmeasured, and widen the distribution rather than shifting it.
- Ignoring a flag that applies is the failure class `REGIME_IGNORED`.

## 7. Grades, evidence codes and card classes

**Grades.** `WIN`, `LOSS`, `PUSH` (an exact integer line or a void-on-tie rule) and `VOID` (no admissible data, abandoned or cancelled with no result, or voided by rule). PUSH and VOID leave the denominators and are never losses.

**Evidence codes.**

| Code | Use when |
|---|---|
| A | An official or field-owner terminal record covers the target field. |
| B | A structured provider or multi-source agreement covers the target field, with an official score. |
| C | The best available evidence is a single secondary, conflicted or provisional source, adopted as final. |
| E | The value is estimated from a partial measurement that bounds the target field; state your confidence. |
| OP | The sporting endpoint is known but the operator rule is not; the card's frozen assumption or the framework default applies. |
| X | No admissible data exists; the row **must** be VOID. |

**Card classes (Rule T2).** `TOP2_ALL_WON`, `TOP2_SPLIT`, `TOP2_ALL_LOST`, `VOID` (no live top-two row) and `NO_FORECAST` (intake with no ranked rows). Only Rank 1 and Rank 2 can count as wins.

**Settlement allowance for the 72-hour clock.** The clock starts at the scheduled start plus the time the event needs to finish: baseball 5 h, cricket 12 h, tennis 8 h, American football 5 h, soccer 4 h, basketball 4 h, ice hockey 4 h, rugby 4 h, Australian rules 4 h, anything else 6 h.

## 8. Failure classes (Rule R1)

Use the closest class; `OTHER` only with an explanation. `VARIANCE` is right only when the outcome was an ordinary draw from a sound distribution with sound inputs.

| Class | Meaning |
|---|---|
| `FIRST_HALF_GOAL_OVERSELECTION` | A first-half goals row was ranked high from a full-game model or territory, not from a half-split rate. |
| `RUNLINE_CUSHION_CEILING` | A +1.5 baseball cushion was priced near its structural ceiling (the one-run rate caps the edge). |
| `BASKETBALL_TOTAL_WITHOUT_PACE_MODEL` | A basketball total was centred by a points average or by judgment, not by pace times efficiency. |
| `TENNIS_IID_UNDERDISPERSION` | A tennis games row used independent points, so the deciding-set mass was too low or too high. |
| `RANK_BY_Q_NOT_P` | The row was ranked by a historical ordering score q, not by `p_card`. |
| `SHARED_DRIVER_TOP_TWO` | Rank 1 and Rank 2 lost together because one driver sat under both. Alias: `TOP_ROW_DEPENDENCE`. |
| `HANDICAP_TAIL_OVERREACH` | A large handicap needed a tail the distribution did not support. |
| `SMALL_SAMPLE_STRENGTH_OVERREACH` | A few games were read as team strength. |
| `PHASE_INCOHERENCE` | Phase and total rows contradicted each other (cricket phase against innings total). |
| `CORNER_ROW_WITHOUT_PROVIDER_OR_NB_MODEL` | A corners row had no provider or no count model. |
| `OVERCONFIDENT_PROBABILITY` | The stated probability was too high for the evidence. Alias: `OVERCONFIDENT_TEAM_TOTAL`. |
| `WEAK_SLATE_FORCED_RANK` | The slate had no strong proposition and a pick was forced. |
| `QUALITATIVE_RANKS_WITHOUT_DISTRIBUTION` | Ranks were given with no distribution behind them. |
| `REGIME_IGNORED` | A measured regime (finals, early season, rule change) applied and was not used. Alias: `FINALS_REGIME_IGNORED`. |
| `UNFITTED_ANALYST_ADJUSTMENT` | An adjustment had no stated size or basis. |
| `LATE_INFORMATION` | A lineup, goalie, starter or injury change arrived after the research time. |
| `ENDPOINT_OR_CONTRACT` | The endpoint or contract definition was wrong or unresolved. |
| `SOURCE_OR_IDENTITY` | The wrong event, team, date or a bad source. |
| `VARIANCE` | An ordinary draw from a sound distribution. |
| `OTHER` | Explain in one sentence. |

## 9. Reading and citing this page

A card's `Rules read` line cites the sections of this page it applied (for example `SELECTION_RULES §2, §3, §4, §6`). A settlement's R9 and R10 cite §7 and §8. A retrospective counts failure classes from §8 only.
