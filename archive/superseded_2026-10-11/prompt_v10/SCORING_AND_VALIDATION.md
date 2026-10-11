# Scoring and validation

**Scoring version SCV-2026.10.09-v5 (Markdown only).** [CURRENT_RULES.md](CURRENT_RULES.md) controls what may be claimed; this page defines how to measure. Everything below is calculated by hand from the settled tables. The pre-rewrite page, with its descriptions of the removed evaluators, is kept in [archive/superseded_2026-10-09/SCORING_AND_VALIDATION.md](archive/superseded_2026-10-09/SCORING_AND_VALIDATION.md). Historical cards keep their original conventions.

## 1. Units and scales

- An **event** is the statistical unit, not each complementary row. A card is one event; its four rows are dependent outcomes of it.
- PUSH and VOID keep their own disposition and are never turned into losses or silently removed.
- **Binary Brier** = (p - y)^2, where y is 1 for a win and 0 for a loss. **Binary log loss** = -ln(p) for a win and -ln(1 - p) for a loss. A stated 0 or 1 that is wrong has infinite log loss; report it as such rather than clipping.
- **Multiclass Brier** (a result with draw) = sum over outcomes of (p_k - y_k)^2, divided by 2, so it matches binary Brier for two complementary states.
- **Improvement** is candidate minus comparator; negative is better. Compare only on identical events and endpoints.
- **Climatology reference** for a set of rows with win rate b: Brier = b(1 - b). **Brier skill** = 1 - Brier / b(1 - b). Positive means better than always stating the base rate.
- q (the historical ordering score) is never scored as an event probability.

## 2. Counting (Rule T2, SCV-2026.10.09-v5)

1. **Counted rows.** For each settled card, the live top-two rows are Rank 1 and Rank 2 graded WIN or LOSS. PUSH and VOID rows are excluded from numerators and denominators. A NO_FORECAST intake has no counted rows.
2. **Card class.** `TOP2_ALL_WON`, `TOP2_SPLIT`, `TOP2_ALL_LOST`, `VOID`.
3. **Primary metrics.** Counted wins ÷ live top-two rows; Rank-1 W/L/VOID and win rate over live Rank-1 rows; Rank 2 likewise; **Hit@2** = cards with at least one counted win ÷ cards with a live top-two row. Always report the number of cards, and never treat the two picks as independent trials.
4. **Ranks 3-4** are graded and kept in a separate informational cohort for calibration. They never enter win counts, rates or performance statements.
5. **Evidence grade.** Record A/B/C/E/OP/X for every row and report counts by grade, so best-available (C) and estimated (E) settlements stay visible. Report a sensitivity line that excludes C and E rows.
6. **Rank-1 failures** each need the Rule R1 deep retrospection. Cohort reports list every one with its failure class and tally recurring classes ([SELECTION_RULES.md](SELECTION_RULES.md) §8).

### Cohorts (never mixed)

| Cohort | Rule |
|---|---|
| `COUNTED` | Rank 1 recorded `PASS` on the Rank-1 gate before the event. |
| `RANK1_UNSTABLE` | Rank 1 recorded `RANK1_UNSTABLE` before the event. Its own cohort. |
| `LEGACY_P_ONLY` | Issued before the gate; only `p_card` is known. |
| `UNKNOWN_GATE` | No recorded gate result. Never inferred to pass. |
| All forecast cards | Historical diagnostic view of every card. |
| Informational | Ranks 3-4. |

## 3. The Wilson 95% interval

For w wins in n counted rows: p̂ = w / n; z = 1.96.

- centre = (p̂ + z^2 / 2n) / (1 + z^2 / n)
- half-width = z × sqrt( p̂(1 - p̂)/n + z^2 / 4n^2 ) / (1 + z^2 / n)
- interval = centre ± half-width.

Check: 79 wins in 134 rows gives p̂ = 0.590, centre 0.587, half-width 0.082, interval 50.5% to 66.9%. Because the two picks of a card are dependent, the interval is **descriptive**; it understates the uncertainty. Promotion decisions use the week-block comparison in section 5.

## 4. Calibration table (by hand)

1. List every row with a stated `p_card` and its outcome (1 or 0). Exclude PUSH and VOID.
2. Group by stated probability into bins: 50-59%, 60-69%, 70-79%, 80-90%.
3. For each bin report n, the mean stated probability, the win rate and the Wilson interval for the win rate.
4. Report the overall Brier score, the climatology Brier and the Brier skill.
5. Describe the pattern: within each bin, does the stated probability sit inside the win-rate interval? An over-confident pattern (high bins under-performing) is the most important finding to report.
6. Optional least-squares reliability line: win = a + b × p over the rows (perfect calibration is a = 0, b = 1). Report it only with its sample size and treat it as descriptive.

Missing probabilities stay missing. A genuine 0 or 1 probability is retained. Never substitute q.

## 5. Comparing two methods (week-block comparison, by hand)

Used for the pre-registered experiments in [HYPOTHESIS_REGISTER.md](HYPOTHESIS_REGISTER.md) and for any claim that one method beats another.

1. For each row both methods priced, compute the paired difference d = Brier(candidate) - Brier(baseline).
2. Group rows by ISO week of the event. Compute the mean difference per week.
3. Over the k weeks, take the mean of the weekly means and the standard error s / sqrt(k).
4. The 95% interval is the mean ± 1.96 standard errors (use 2.36 for k below 8, and treat k below 8 as insufficient).
5. A method is better only if the interval's upper bound is below 0, the calibration slope's interval contains 1, and at least 8 week-blocks are in the sample. Otherwise write `INSUFFICIENT_EVIDENCE` and the sample still needed.
6. Do not aggregate unrelated sports or families into one number.

## 6. Ranking diagnostics

- **Wins@2** = counted wins (0, 1 or 2) on a card.
- **NDCG@2** for binary relevance: DCG@2 = rel(rank 1)/log2(2) + rel(rank 2)/log2(3) = rel1 + 0.631 × rel2. IDCG@2 uses the ideal ordering **over the entire slate of four rows**, not only the top two observed rows: with m wins among the four rows, IDCG@2 is 1 for m = 1, 1.631 for m of 2 or more, and the card is unscored for m = 0. NDCG@2 = DCG@2 / IDCG@2. Unresolved, push and void slates stay unscored. NDCG is descriptive ranking quality, not a win count.

## 7. Scoreboard (kept by hand in `research/scoreboard/SCOREBOARD.md`)

After each import (prompt 4) and each retrospective (prompt 6), update the scoreboard from the settled tables:

1. Add each newly settled card to its cohort (section 2).
2. For each cohort recompute: cards, counted wins over live top-two rows, rate with its Wilson interval, Rank-1 W-L, Rank-2 W-L, and cards won / split / lost.
3. Update the by-sport and by-month tables and the Rank-1 results by proposition family.
4. Update the slot table: Rank 1, Rank 2, Ranks 1-2, Ranks 3-4. If Rank 1 does not beat Rank 2, and Rank 2 does not beat ranks 3-4, say plainly that ranking is not separating propositions.
5. Copy the headline numbers into [CURRENT_STATE.md](CURRENT_STATE.md).
6. Spot-check five random IDs against their settlement blocks in the Combined Log. If any number disagrees, fix the scoreboard, never the log.

## 8. Historical learning and the diagnostic cohorts

Historical rank logs (`GAME_PREDICTION_RANK_LOG.csv`) and reconstructed views are **learning-only**: literal grades, unresolved conflicts and missing cutoffs stay labelled. They never fill absent cutoffs, baselines, event IDs or endpoints and cannot establish source truth, prospective calibration or incremental skill. P-527 to P-537 are completed-game diagnostic reviews, not certified prospective outcomes; missing literal probabilities make their Brier and log loss `NOT_COMPUTABLE`. P-537 first-half and corners rows stay unresolved.

## 9. Release and failure policy

- **Certification is suspended** (CURRENT_RULES §10). All scores here are research scores.
- Classify every learning case as one or more of: data or source or identity, contract or period, timing or availability, model or calibration, research adjustment, true random miss, unresolved or censored. Review wins under the same checks as losses.
- Append a versioned hypothesis and an acceptance criterion to [HYPOTHESIS_REGISTER.md](HYPOTHESIS_REGISTER.md) before changing a rule; evaluate it chronologically against a fixed baseline. Never edit an old forecast to make a repair look successful.
- A written acceptance criterion is not a passed experiment.
