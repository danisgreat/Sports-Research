# Predictability across sports — preregistration (2026-09-26(e))

**Committed before any analysis in this folder was run.** The git commit that adds this file precedes the commit that adds any result. Every constant is the one already in the repository at `0e98a46` (the merge of PR #2); nothing here is tuned.

**Origin.** On 2026-09-26 the user asked for predictability across all sports to be improved "properly".

The facts at `0e98a46`:
- **The cards show no skill.** They have not beaten a naive population baseline (`SKILL_BASELINE_LEDGER.md`).
- **The models show skill, but only in shadow.** The numerical models in `tools/sport_models.py` beat their league baselines on thousands of public games, but under `C-SPORT-SHADOW` / `C-MLB-SHADOW` they are never a card input.

**The questions.**
- Where can a model add information?
- Is it better than the cards' own probabilities on the same contracts?
- Where is there still no signal?

**Market-blind:** no odds, lines or prices are read by any analysis here.

## P1 — MLB: the declared starting-pitcher term

`tools/mlb_model.py` declares a starter term (PRIORS: `starter_prior_ip` 40, `starter_prior_gs` 5, `starter_prior_len` 5.3, `fip_weight` 0.5, `cfip` 3.15, `ra_per_er` 1.08, bounds [0.6, 1.5]). Until now it was judged "prospective only", because past probable starters were thought not to be recoverable leak-free.

They are recoverable:
- statsapi's schedule keeps each completed game's pre-game `probablePitcher`;
- `people/{id}/stats?stats=gameLog` gives every appearance, so a starter's record strictly before a date can be summed.

**Data.**
- The 2025 and 2026 regular seasons: 2026 through 24 Sep, from `schedule?hydrate=probablePitcher,linescore,venue`.
- The pitcher game logs of every probable starter.

**Models.**
- A0: the league to date.
- A1: team + park + home, PRIORS unchanged.
- A1S: A1 plus the starter term, PRIORS unchanged. Each starter's current-season lines are dated strictly before the game, exactly as the `pitcher()` date-range query would return them. A missing probable gives multiplier 1.0.
- TB-1: `tools/team_baseline.py` SeasonState, k 20, with its running one-run share for the run line.

**Protocol.** Rolling origin with the same rules as `mlb_model.validate`: a game is forecast from games strictly before its date, with a minimum of 300 prior games in the season.

**Metrics per game:**
- home-win Brier and log loss;
- Brier at total lines 7.5, 8.5 and 9.5;
- home −1.5 run-line Brier.

**Primary test:** A1S − A1 in home-win log loss.

**Secondary test:** A1S − A1 in the mean of the five Brier scores.

**Interval:** a day-block bootstrap, 2,000 resamples, seed 20260926.

**Decision:**

| Result | Verdict |
|---|---|
| The primary interval is below 0 in **both** seasons | "The starter term adds skill" |
| Below 0 in one season only | "Mixed" |
| Below 0 in neither season | "Not demonstrated" |

A1S − A0 and A1S − TB-1 are reported descriptively.

## P2 — coverage: NBL and NRL (the A1 models never validated)

**Data.** ESPN scoreboards already cached in `research/base_rates_2026-09-25/cache` (retrieved 2026-09-25). They are parsed only through `tools/sport_data.parse_espn_event`, which reads no market keys.
- NBL: 2023-24, 2024-25 and 2025-26.
- NRL: 2025 and 2026, all completed games; the regular season is ESPN type 1.

**Protocol.** `tools/sport_models.validate_team`, constants as at `0e98a46`. The earlier seasons serve as warm-up.

**Test windows:**
- NBL: 2024-09-01 to 2025-04-30, and 2025-09-01 to 2026-04-30;
- NRL: 2026-03-01 to 2026-09-24.

**Decision** (per window, per metric): "A1 better" only when the week-block 95% interval of A1 − A0 lies below 0, on result Brier and on the total at the fixed line. A1 − TB-1 is reported where the validator computes it.

## P3 — cards against models on the same contracts

**Population.** Every settled row in `research/settled_rows_2026-09-25/settled_rows.csv` (rebuilt at `0e98a46`) that meets all three conditions:
- it has a stated p;
- it is a full-game moneyline, a ±k.5 handicap or a full-game total;
- it belongs to a league a model covers here (MLB; NBA, WNBA, NBL, NFL, AFL, NRL, EPL, NHL).

**Matching.**
- The date, home side and away side come from the card's own identity line in the logs.
- A row whose event cannot be matched uniquely to one completed game is excluded, and the exclusions are counted.

**Model probability.**
- Each contract's probability comes from the model state as of the card's venue-local date (games strictly before).
- MLB uses A1S with the probable starters.
- Other leagues use A1 from `tools/sport_models.py` and TB-1.

**Scores:**
- Brier(card p) against Brier(model p), and against Brier(RM-1 q);
- on shared rows only, one decision per contract;
- **card-cluster** bootstrap, 2,000 resamples;
- pooled and by sport group.

**Decision:**

| Result | Verdict |
|---|---|
| The card − model interval lies above 0 | "The model beats the cards" |
| It lies below 0 | "The cards beat the model" |
| Otherwise | "No demonstrated difference" |

**Exploratory, labelled as such:** a 50/50 logit blend of card and model.

## P4 — the anchor registry (a selection rule, not a coefficient)

For each league and target (result or side, and total), the **anchor** is the first model in the list [A1S (MLB only), A1, TB-1] that beat A0 on held-out public data with a 95% interval below 0 on that target.

- If A1 and TB-1 both qualify, A1 is chosen only if it also beat TB-1 with its interval below 0. Otherwise TB-1, the incumbent.
- If none qualifies, the anchor is `BASELINE_P` (population).

The evidence is the 2026-09-26 validation (`research/sport_models_2026-09-26/README.md`) plus P1 and P2.

**Using the anchor on cards is a `MODEL_CHANGE` under `C-RULE-FREEZE`.** It is prepared here as a proposal and becomes operative only on the user's explicit instruction, after the user has seen the evidence-status table.
