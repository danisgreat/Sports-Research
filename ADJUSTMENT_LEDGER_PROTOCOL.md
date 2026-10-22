# Adjustment ledger, picks block and abstention (LEDGER-v1 / PICKS-v2)

**P-2026.10.22-v24.0 · CR-2026.10.22-R2.** Implements REV-02, REV-03, REV-05, REV-09, REV-10 and REV-17 of the [framework revamp review](research/verification/review_2026-10-22_framework_revamp/REPORT.md). The card's probability is the frozen **reference** ([REFERENCE_MODEL_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md)) plus **logged adjustments**. Each adjustment is a verified fact with a source, a publication time, a size taken from an effect-table row and a direction. At settlement the final probability is scored against the reference on the same rows, so for the first time the framework measures whether the analyst's research adds accuracy.

## 1. The procedure

1. Run the reference stage and print the Reference block (REFMODEL-v1).
2. Research under [RESEARCH_CHECKLISTS](RESEARCH_CHECKLISTS.md): the value-ranked inputs for the sport, each timed to when it is published.
3. For each confirmed fact that the reference cannot know, write one **adjustment row**:

| Field | Content |
|---|---|
| Fact | The verified claim (player out, starter confirmed, wind, rest, venue change) |
| Source and times | URL or feed, publication time, retrieval time, corroboration (decisive facts need two independent sources) |
| Target | The quantity it moves: home margin, away points, total, or one team's rating |
| Effect row | The [EFFECT_TABLES](EFFECT_TABLES.md) row id, or `SCENARIO_NO_TABLE` |
| Size | Signed, in the quantity's units, with the table's interval |
| Entry | `FULL` (measured and confirmed out of sample), `HALF` (the provisional rule below) or `SCENARIO` |
| Overlap | The reference input it must not double count (a player already out for the reference's whole window; a team rating already reflecting the absence) |

4. Apply the sizes to the reference **centre** (margin and total, or the Poisson means), recompute the one score grid, and read every supplied contract from it. Winner, handicap and total rows come from the same grid. The width never falls below the competition's floor ([COMPETITION_PARAMETERS](COMPETITION_PARAMETERS.md)).
5. Write the **picks block** (section 3), lint it, ledger it, commit and push.

**Entry rule (provisional).** A row whose effect is `MEASURED_CONFIRMED` enters at full size. A row whose effect is `LITERATURE_START` or `MEASURED_NOT_CONFIRMED` enters at **half size** until the ledger has an adjustment-value estimate λ from at least 40 adjusted rows (section 5); from then on the entry factor is the estimated λ, capped at 1, and never below 0. A fact with no effect row (`SCENARIO_NO_TABLE`, for example a player whose impact has not been measured) may not change a number silently: price it as a declared low/base/high mixture with weights written before pricing (CURRENT_RULES section 7), and label the row `SCENARIO`. Half size is a starting value, not a tuned parameter, and exists because the card record shows the analyst's unaided probabilities over-confident at the top and uninformative in the middle.

## 2. Effect tables (REV-17)

[EFFECT_TABLES](EFFECT_TABLES.md) lists every size the analyst may use, with its measurement: estimate, standard error, n, period, evidence status and, where tested, the out-of-sample result. Status classes:

| Status | Meaning | Entry |
|---|---|---|
| `MEASURED_CONFIRMED` | Estimated on this repository's verified finals and the effect improved a held-out season | FULL |
| `MEASURED_NOT_CONFIRMED` | Estimated here but not shown to help out of sample | HALF |
| `LITERATURE_START` | A published estimate, not re-estimated on current seasons | HALF |
| `NOT_ESTIMATED` | No usable number | SCENARIO only |

Prompt 7 and 8 re-estimate rows between seasons. Hand-invented sizes stay out.

## 3. The picks block

Every new card carries one `PICKS_V2` block between `<!-- BEGIN PICKS_V2 <key> -->` and `<!-- END PICKS_V2 <key> -->`, inside its card markers: a header of `key: value` lines, a blank line, then one CSV row per priced contract. The template is [CARD_AND_LOG_TEMPLATES](CARD_AND_LOG_TEMPLATES.md) section 3c. `python -m ml card lint --mini M --key K` checks it:

- masses W, P, L sum to one, and the printed p equals W/(W+L);
- complementary totals and handicaps agree;
- the tier equals the tier rule; a reference exists when `reference_status` says so and is `NONE` otherwise;
- each margin or total row prints its centre and SD, one pair per quantity, and its line distance in SD matches;
- the SD is not below the competition's floor unless `width_floor_exception` is written with its reason;
- the most-likely list is ordered, within 1-4 rows, and every ranked row is at or below the 0.90 selection ceiling;
- `information_row` is `Y` exactly when |final − reference| ≥ 0.03;
- `line_implied_p` is 0.5 for a supplied two-way line and blank otherwise (REV-03);
- `abstain` follows from the numbers (section 4).

The linter reads no model, price or outcome. A card that does not lint clean is not ledgered or committed as an issued card.

## 4. What the card says

- **Probability table:** every supplied contract with reference p, final p, and the model challenger p where one exists. Winner probabilities for both sides, including a draw where the competition allows one.
- **Most-likely list** (up to four rows, ordered by final p): each labelled `SUPPLIED` or `ANALYST_DERIVED` with its distance from the centre in SD. It answers "which outcomes are most likely". A near-certain row on an analyst-chosen line says nothing about skill, and the card says so.
- **Information list:** the rows the adjustments moved by at least 0.03, with the facts. This is the list that tests the research.
- **Abstain.** If no ranked row has a final p of at least 0.65 and no row is an information row, the card says **no strong pick** (`abstain: YES`). A probability between 0.40 and 0.65 has not distinguished winners from losers in 525 stated rows; the 0.65 floor is the point from which stated p has tracked outcomes (slope 0.89 on 256 rows). The most-likely list may still be shown, labelled as not strong.
- **Covering pairs.** If the first two ranked rows cover each other (opposite sides of one line, or a moneyline with the opposite handicap), the card says so and counts them as one pick (FORCED_PAIR_MECHANICAL).

Rule T2 (rank 1 and rank 2) is kept as a descriptive count of the most-likely list. It is no longer the headline: the headline is the paired proper score of the final p against its references.

## 5. Scoring at settlement

`python -m ml ledger add --mini M --key K` appends the lint-clean block to [ADJUSTMENT_LEDGER.csv](research/adjustment_ledger/ADJUSTMENT_LEDGER.csv) (once per card). Prompt 3 writes `RESULTS.csv` (`local_key,label,grade`), `ACTUALS.csv` (`local_key,quantity,actual` for margin and total) and, if the owner supplies them, a [benchmark file](BENCHMARK_PROTOCOL.md). `python -m ml ledger score --results R --benchmarks B --out DIR` then reports, on identical decisive rows and by scope (ALL, tier, family, information rows, most-likely list):

| Comparison | Reads |
|---|---|
| final minus reference | The value of the analyst's adjustments; negative favours the analyst |
| final minus league baseline | Skill against a league-only forecast |
| final minus line-implied 0.5 | Skill against a coin at a supplied two-way line, which needs no price |
| final minus frozen model | The fitted challenger against the card |
| final minus a hand-entered benchmark | The no-vig close or an external model, if the owner enters one |

Each is a mean paired Brier difference with a week-block interval (`INSUFFICIENT_EVIDENCE` below eight weeks). The same command estimates **λ** (logit P = logit reference + λ·(logit final − logit reference)): 1 means the adjustments were worth their size, 0 that they added nothing, above 1 that they were too timid, `NOT_ESTIMATED` below 40 adjusted rows. `python -m ml ledger coverage` reports the z RMS and the shares beyond one and two SD of the margin and total widths against the 0.85-1.15 band, `INSUFFICIENT_EVIDENCE` below 40 cards.

## 6. Decision rules (registered before data)

- **LEDGER-1 (value of research).** After at least 150 information rows over at least eight weeks, if the mean of final − reference is not below zero with its interval, the next prompt-8 review proposes reference-only cards with confirmed-availability scenarios. If it is below zero, the entry factor follows λ.
- **LEDGER-2 (abstention).** The share of abstained cards and the Brier of the most-likely list at p ≥ 0.65 are reported monthly. The 0.65 floor is revisited only on 400 or more rows from this procedure.
- **WIDTH-1.** The margin and total z RMS sits in 0.85-1.15 over 40 cards per family. Outside it, the competition row is the first suspect.

These are registered as `REV-H2` to `REV-H4` in the [hypothesis register](HYPOTHESIS_REGISTER.md). Sample sizes that depend on unknown variances stay `BLOCKED_DESIGN` until an eight-week pilot supplies them.

## 7. Limits

- A single analyst (an LLM) writes both the adjustments and the card; their errors are correlated, which is why the ledger scores them rather than trusting them.
- Rows in a card are dependent and cards in a week share conditions; the week-block interval is the unit of evidence.
- The ledger measures information that was published before the freeze. A fact that appears later, or a late issue, is a different stratum (`POST_START_ISSUE`).
