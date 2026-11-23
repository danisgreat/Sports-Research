# SELECT-SHADOW-v1: registered shadow plan for the top two picks (v29.2, 22 November 2026)

> **Superseded on 23 November 2026 (v29.4) by [SELECT-SHADOW-v2](SELECTION_SHADOW_PLAN_v2.md), before v1 reached any
> eligible game.** v1 judged picks one at a time, used the stated p for `NO_DIRECTION` while ranking on the
> conditional p, took its coverage and registration time from the caller, and let one outcome file overwrite another.
> Kept here as the record of what was registered; it decides nothing.

This registration takes effect at its first independently verified GitHub publication on `main`. It does not change
[EVALUATION_PLAN_v29.0](EVALUATION_PLAN_v29.0.md), whose card protocol, selection policy (the registered rank) and
600-game Brier test stay frozen. Nothing here reaches a card, a seal, a rank or the registered score. Code:
[`ml/selection_shadow.py`](../../ml/selection_shadow.py).

## 1. Why

The registered rank orders every priced line's favoured side by stated probability. It ranks a side at 0.50, can rank
two labels that settle on the same outcome (P-689), and counts a pick whose availability effect the card itself says it
could not measure. Two external reviews on 22 November 2026 recommended separating "the two highest numbers on the card"
from "two picks with enough evidence to recommend", and testing that separately and prospectively.

## 2. The policies, fixed now

All three policies are computed from the same sealed cards.

- **REGISTERED_RANK**: Rank 1 and Rank 2 exactly as the frozen ranker gives them.
- **SHADOW_SIGNAL**: the candidates are the favoured sides of priced supplied lines, using the probability conditional
  on a decision. A candidate is dropped if it is below 0.55 (the existing `NO_DIRECTION` boundary, not a value tuned
  on results) or flagged `CONTRADICTS_OWN_CENTRE`, `INCOHERENT_ACROSS_LINES` or `NO_RESULT_SOURCE`. A second candidate
  that is the same contract as a higher one is also dropped. "Same contract" is read from the registered request's
  definitions, using the registration's own rule (period, endpoint, action and unit). A winner equals a half-point
  handicap only on the deciding score with no draw possible, so hockey settled in regulation, or a handicap on another
  statistic, stays distinct. Without the definitions, only an exact repeat of family, sides and lines counts. The highest two remaining are kept, label order breaking ties. The list may hold one pick, or none
  (`NO_STRONG_PICK`).
- **SHADOW_STRICT**: as SIGNAL, and it also drops `UNMEASURED_AVAILABILITY_PRICED`. On the first 12 sealed cards every
  line carried that flag, so STRICT issued nothing. Its coverage measures whether abstaining on unmeasured absences is
  workable.

A pair of picks is marked `DEPENDENT` when both are totals, both handicaps or both team totals on one card (nested
lines or a shared game state). Its joint outcome is reported with that caveat.

## 3. Universe and denominators

The confirmatory universe is every game that is eligible in the registered score (`COVERAGE.csv` `eligible=Y`, with a
server seal before verified first play) and whose seal server time is later than this plan's first `main` publication
(`--coverage`, `--registered-at`). A run without both inputs is descriptive (`DESCRIPTIVE_INCOMPLETE_INPUTS`) and
never gives a verdict. Games are taken in the registered scorer's order: scheduled start, then game, then card key. The
cards sealed before publication are development data. They are reported, and they never
enter the decision. An unpriced line is never a candidate. A pick that ends as a push or void is reported and is not
decided. A game that is unsettled at the registered 14-day deadline is excluded from the universe, exactly as in the
registered score.

`SHADOW_SCORE.csv` always shows, for each policy: cards, cards with a pick, picks, wins, losses, pushes or voids,
unsettled picks, hit rate, cards with two decided picks, and how many of those won both, one or neither, plus how many
were dependent.

## 4. Decision

The objective is the most correct picks on average: hit rate per decided pick, the sum of marginal probabilities. The
decision is taken once, on the first 100 games of the universe (calendar-free, as the registered checkpoint). For each
variant, compute its hit rate minus the registered ranker's, on the same games, with a game-clustered bootstrap
interval (10,000 resamples, seed 20261122). Each of the two variants uses alpha 0.025, splitting 0.05 between them.

- `IMPROVEMENT_DEMONSTRATED`: the interval's lower end is above 0, **and** the variant issued at least half as many
  decided picks as the ranker.
- `NOT_DEMONSTRATED`: anything else.

Before 100 games, the result is `DESCRIPTIVE_BELOW_100_GAMES` and nothing is claimed. Both-won rates and joint
outcomes are reported alongside and are descriptive. A variant that passes is a candidate for a new registration of
the card selection policy. It never replaces the registered rank automatically.

## 5. Power and limits

How quickly a difference can show depends on how often the policies disagree and how many games produce two
qualifying picks. On the development cards, SIGNAL issued 13 decided picks to the ranker's 20. Thresholds such as 0.58
or 0.62, read off settled history, are not used: choosing them after the results would overstate them. Any later
threshold is registered here as a new version before it is tested.

```text
python -m ml.selection_shadow score --intake <intakes from seals> --outcomes <OUTCOMES.csv files> \
    --coverage <registered score>/COVERAGE.csv --registered-at <this file's first main publication> --out <folder>
```
