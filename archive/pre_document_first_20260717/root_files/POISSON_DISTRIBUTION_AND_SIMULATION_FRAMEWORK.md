# Poisson Distribution and Simulation Framework for All Sports

Version: 1.0  
Added: 2026-06-24 Australia/Sydney  
Status: ARCHIVED / NON-OPERATIVE since 2026-07-16  

> Do not use this document to generate a forecast. It has been replaced by `SPORTS_MODEL_VALIDATION_AND_SIMULATION_FRAMEWORK_v3.md`. No model is currently ACTIVE; Poisson or simulation is permitted only inside a validated, scoped model card.
Scope: research-only pregame, live, phase, player, team and match predictions across every sport in the Sports Research workspace

## 1. Purpose and authority

This file converts the scattered Poisson, negative-binomial and simulation references in `combined_sports_doc_v2.txt` into one operational standard.

It inherits all source, ruleset, availability, weather, pitch/surface, game-state, settlement, calibration and retrospective requirements in the main sports document. If this file conflicts with a later dated active instruction, use the stricter and more recent rule and record the conflict.

Poisson is mandatory as a transparent count-model baseline whenever the target is a non-negative event count. It is not automatically the final model. The final distribution must be selected from diagnostics, sport mechanics and out-of-sample calibration.

This framework does not use betting odds or market prices unless the user explicitly authorizes them. A user-provided threshold is used only to calculate outcome probabilities after the score or event distribution is independently estimated.

### Hard data precondition — consolidated 2026-07-11

- No distribution may be fitted or simulated until the Canonical Hard Data Gate in `combined_sports_doc_v2.txt` and `SPORTS_SOURCE_REGISTRY_v2.md` is complete.
- American leagues require a StatMuse-first attempt for every supported decision-driving team/player/unit/phase split; stale, unsupported or misparsed results must be rejected and the fallback disclosed.
- Every decision-driving statistic uses L5/L10/L15/L20 wherever observations exist, plus season/year and historical/career or same-level baselines. Fewer than 20 observations are labelled with actual `N`; unavailable aspects are `MISSING` and cap confidence.
- This paragraph is the sole modelling-framework reminder. The main sports document and source registry hold the canonical operational wording, avoiding another duplicate policy block here.

## 2. Mandatory comprehensive sweep before any prediction-log entry

Before adding a new row to either prediction results log or calibration ledger, complete and record this sweep:

1. Read the Universal Core, Active Operating Index, current dated upgrades and the relevant sport annex in `combined_sports_doc_v2.txt`.
2. Search the entire sports document for the sport, competition, market type, phase, venue, teams/players, distribution family and any known failure mechanism.
3. Read the Learnings and Observations sections and all relevant settled/pending rows in both:
   - `PREDICTION_RESULTS_LOG_v2.md`
   - `PREDICTION_RESULTS_LOG_v3.md`
4. Sweep `SPORTS_CALIBRATION_LEDGER_v2.csv` for:
   - the sport and competition;
   - the same market family;
   - top-pick losses;
   - bottom-pick wins;
   - projection errors;
   - rank-slot calibration errors;
   - phase/full-game divergence;
   - availability, ruleset, settlement and source-status errors.
5. Read the relevant source and freshness rules in `SPORTS_SOURCE_REGISTRY_v2.md`.
6. Read this file's sport-specific model-selection rule and diagnostics.
7. Confirm that the previous enquiry is settled or correctly marked live/pending before logging the new card.
8. Write a short `FRAMEWORK SWEEP` line in the new log row naming:
   - files checked;
   - closest prior lessons;
   - model family chosen;
   - rejected challenger models and why;
   - unresolved conflicts or missing data.

No prediction-log entry may claim a simulation probability if this sweep, the model inputs, simulation seed and distribution diagnostics are absent.

## 3. Core statistical definition

For a count \(Y\) with expected rate \(\lambda > 0\):

\[
P(Y=k)=\frac{e^{-\lambda}\lambda^k}{k!},\qquad k=0,1,2,\ldots
\]

For a Poisson random variable:

\[
E[Y]=\lambda,\qquad Var(Y)=\lambda
\]

The equal mean-variance condition is the central diagnostic assumption. Sports scores frequently violate it because scoring rates change with game state, lineups, fatigue, wickets, penalties, substitutions, tactical response, overtime and shared match conditions.

Poisson is suitable only when:

- the target is a count;
- the exposure interval is known;
- event rates are sufficiently stable or explicitly modelled as time-varying;
- residual dependence is modest;
- dispersion and zero-frequency diagnostics are acceptable;
- walk-forward validation shows useful calibration.

## 4. Required three-model comparison

Every count-market model must compare at least:

1. **Baseline:** Poisson or independent Poisson.
2. **Dispersion/dependence challenger:** negative binomial, generalized Poisson, Conway-Maxwell-Poisson, bivariate Poisson, Dixon-Coles, zero-inflated/hurdle or compound model as appropriate.
3. **Non-parametric or sport-native challenger:** empirical residual bootstrap, possession/drive/innings/over simulation, Markov model, survival model, normal/Student-t/quantile model or calibrated machine-learning distribution.

The final model is the simplest model that survives diagnostics and performs best in time-ordered validation. Do not select a more complex model merely because it produces a preferred pick.

## 5. Distribution-selection diagnostics

Calculate these on training residuals and again by competition, season, venue class and market phase where sample size permits:

| Diagnostic | Calculation / test | Required response |
| --- | --- | --- |
| Mean-variance ratio | sample variance / sample mean | Near 1 supports Poisson; material deviation requires a challenger |
| Pearson dispersion | Pearson chi-square / residual degrees of freedom | Rough guide: 0.8-1.2 acceptable; 1.2-1.5 caution; above 1.5 normally reject raw Poisson |
| Zero frequency | observed zero rate vs fitted zero rate | Use zero-inflated/hurdle or a sport-state model if excess zeros persist |
| Tail coverage | observed vs predicted 5th/95th and 10th/90th percentiles | Reject models that systematically miss blowouts, collapses or shutouts |
| Score dependence | residual correlation between opponents/teams/phases | Use bivariate/shared-state or conditional simulation when material |
| Calibration | reliability by probability bucket | Recalibrate or reject if forecast probabilities are systematically high/low |
| Proper scores | log loss, Brier score, Poisson/NB deviance, ranked probability score | Compare out of sample, not on fitted data |
| Interval coverage | percentage inside predicted 50%, 80% and 90% intervals | Intervals must approximately match their stated coverage |
| Temporal stability | rolling residuals and parameter drift | Shorten decay window or use a dynamic/state-space model |
| Phase consistency | separately fitted phase vs full-game distributions | Never obtain phase probabilities by simple proportional scaling without validation |

Thresholds above are operational alerts, not immutable laws. Sample size and sport mechanics still control the final choice.

## 6. Estimating the expected rate

Never set \(\lambda\) equal to the user's line. Estimate it independently.

The preferred log-link structure is:

\[
\log(\lambda)=\beta_0+\text{attack}+\text{opponent defence}+\text{venue}
+\text{availability}+\text{form}+\text{rest/travel}
+\text{weather/surface}+\text{rules/context}
\]

Required input hierarchy:

1. Current confirmed role and availability.
2. Opponent-adjusted current-season baseline.
3. Last 5/10/15/20 with explanatory form delta.
4. Same format, competition and phase.
5. Similar venue, surface, weather and game-state samples.
6. Historical/career baseline with recency decay.
7. Replacement and bench/bullpen/bowling-unit effects.
8. Ruleset and settlement adjustments.

Use partial pooling or shrinkage for small samples. Do not let a tiny last-five sample replace the season/historical prior unless a verified role, lineup, tactical or physical change explains the shift.

## 7. Monte Carlo simulation standard

- Minimum production run: **100,000 simulations**.
- Minimum quick diagnostic run: **10,000 simulations**.
- Use a fixed, logged random seed for reproducibility.
- Run at least three seeds for a high-stakes or near-line decision.
- Report Monte Carlo standard error for the selected probability:

\[
SE(\hat p)=\sqrt{\frac{\hat p(1-\hat p)}{N}}
\]

- Increase simulations when two options are separated by less than one percentage point.
- Simulation count does not repair a wrong mean, wrong distribution or stale lineup.

Every simulation output must report:

- model family and version;
- number of simulations and seed;
- projected mean and median;
- standard deviation/dispersion;
- 10th, 25th, 75th and 90th percentiles;
- over, under, push and void probabilities;
- win/draw/loss or cover probabilities where relevant;
- probability of overtime, extra innings, Super Over, DLS/reduced-overs or shootout branches where applicable;
- sensitivity to key uncertain inputs.

## 8. Settlement-safe threshold logic

For simulated integer scores `scores` and line `L`:

- Half-line over: `scores > L`
- Half-line under: `scores < L`
- Whole-line over: `scores > L`
- Whole-line under: `scores < L`
- Whole-line push: `scores == L`

Do not force complementary probabilities when options overlap. Example: first-six Over 39.5 and Under 49.5 both win from 40 through 49.

For shortened, abandoned or interrupted events, model and settle only under the confirmed house/competition convention. Do not treat a reduced cricket innings, suspended baseball game or shortened match as the original exposure.

## 9. Sport-by-sport model-selection matrix

| Sport / market | Poisson role | Preferred final model | Key mechanism that Poisson misses |
| --- | --- | --- | --- |
| Soccer goals/team goals | Strong baseline | Dixon-Coles or dynamic bivariate Poisson; hierarchical model for sparse leagues | Low-score dependence, draws, changing team strength |
| Soccer cards/corners/shots | Baseline if count diagnostics pass | Negative binomial, bivariate or zero-inflated model | Referee/style effects, clustering, excess zeros |
| Ice hockey regulation goals | Useful baseline | Bivariate/dynamic Poisson or NB; separate OT/shootout branch | Empty-net state, goalie pulls, shared pace, OT/SO |
| Baseball runs | Benchmark only | Inning/plate-appearance simulation, NB or empirical residual model | Starter/bullpen transitions, batting order, extra innings, run clustering |
| Baseball strikeouts/HR/walks | Often useful baseline | Poisson/NB regression with opportunity exposure | Pitch count, lineup turnover, overdispersion |
| Cricket innings/phase runs | Benchmark only | Over/ball and wicket-state simulation, NB or empirical mixture | Wickets alter rate, boundary clustering, format and phase dependence |
| Cricket wickets/boundaries | Useful event-count baseline | Poisson/NB with overs/balls exposure and role adjustment | Bowling allocation, wicket dependence, innings truncation |
| Basketball/WNBA points | Diagnostic baseline only | Possession-based normal/Student-t/quantile or empirical simulation | Multi-point scoring, pace, fouling, OT, strong overdispersion |
| Basketball player event counts | Conditional baseline | Poisson/NB with minutes and usage exposure | Minutes uncertainty, role concentration, correlation |
| AFL/AFLW points | Diagnostic baseline only | Goals/behinds component simulation plus margin/total residual model | Six/one-point scoring, conversion, territory and blowouts |
| Rugby league/union points | Event baseline | Compound scoring-event simulation | Tries, conversions, penalties have different point values |
| NFL/college football points | Event baseline | Drive-based compound model or margin/total model | TD/FG structure, possession count, clock and OT |
| Tennis match score | Do not use as primary | Point-game-set Markov/binomial model | Hierarchical scoring and serve alternation |
| Tennis aces/double faults | Baseline if exposure known | Poisson/NB with service points/games exposure | Match-length uncertainty and opponent return quality |
| Volleyball set/match result | Do not use as primary | Rally/set Markov model | Win-by-two rules and set dependence |
| Volleyball aces/blocks | Baseline | Poisson/NB with sets/rallies exposure | Variable match length |
| Golf round score | Do not use raw Poisson | Hole-level multinomial/ordinal or normal/mixture model | Scores can be negative relative to par and holes differ |
| Golf birdies/bogeys | Event baseline | Binomial/Poisson-binomial or NB by hole/opportunity | Hole-specific probabilities and weather waves |
| Motorsport finishing position | Do not use | Survival/reliability plus rank/Plackett-Luce simulation | Censoring, DNFs, pit strategy and rank constraint |
| Motorsport incidents/pit stops | Baseline | Poisson/NB or recurrent-event process | Safety-car clustering and strategy dependence |
| Boxing/MMA result/time | Do not use primary Poisson | Survival/hazard plus categorical outcome model | Bout termination and censoring |
| Boxing/MMA strikes/takedowns | Baseline conditional on duration | NB or rate model with simulated fight duration | Endogenous bout length and pace shifts |
| Other low-count sports | Candidate baseline | Validate Poisson, bivariate and NB | Dependence and dispersion |
| Other high-scoring sports | Benchmark only | Sport-native opportunity simulation | Compound scoring and state dependence |

Women's and men's competitions, junior/senior levels and different formats must be trained separately unless hierarchical pooling is explicitly validated.

## 10. Soccer and hockey implementation

### 10.1 Independent Poisson baseline

Estimate home and away scoring intensities separately, then form a score matrix:

\[
P(H=i,A=j)=P(H=i)P(A=j)
\]

Derive:

- home win: sum cells where \(i>j\);
- draw: sum cells where \(i=j\);
- away win: sum cells where \(i<j\);
- totals and team totals: sum relevant cells;
- exact scores: individual cells;
- margin: derive from \(H-A\), or use the Skellam distribution only when independence is acceptable.

### 10.2 Required upgrades

- Use Dixon-Coles for low-score dependence and time decay in soccer.
- Use bivariate Poisson when shared game intensity creates correlated scores.
- Use dynamic attack/defence strengths when rosters, coaches or form change.
- In hockey, simulate regulation first, then overtime/shootout under the competition rules.
- Model empty-net goals and goalie-pull state separately where data permits.

Never use one total-goals Poisson mean to infer both teams' score distributions without team-specific attack and defence rates.

## 11. Baseball implementation

Raw full-game Poisson is a baseline only.

Preferred hierarchy:

1. Simulate starting-pitcher innings/batters faced.
2. Simulate lineup plate appearances and run events.
3. Transition to bullpen by availability and leverage role.
4. Apply park, roof, wind, temperature, umpire and defence.
5. Simulate innings 1-9.
6. Add the correct extra-inning rules and suspended-game branch.

Use negative binomial or empirical residual sampling if full-game run variance exceeds its mean. Use separate first-five and full-game models; bullpen and extras make them different distributions.

## 12. Cricket implementation

Raw innings Poisson must not control a cricket total.

Preferred T20/ODI hierarchy:

1. Simulate balls or overs by innings phase.
2. At each ball/over, model runs and wicket probability from batter, bowler, handedness, venue, pitch, weather and field restrictions.
3. Update future scoring rate after every wicket.
4. Respect bowling allocation, player availability and remaining batting depth.
5. Model powerplay, middle and death overs separately.
6. Branch for chase state, DLS, reduced overs, Super Over and innings termination.

Minimum simplified model when ball-by-ball data are unavailable:

- powerplay runs: fitted distribution;
- middle-over runs: conditional on powerplay wickets and score;
- death runs: conditional on wickets in hand and available finishers;
- total: sum the conditional phase simulations.

Negative-binomial variance:

\[
E[Y]=\mu,\qquad Var(Y)=\mu+\frac{\mu^2}{\phi}
\]

Estimate \(\phi\) from comparable innings; never choose it only to widen probabilities around the user's line.

Mandatory cricket outputs:

- actual pitch report / unknown;
- captain/toss comments;
- live surface behaviour / not applicable;
- projected powerplay score and wickets;
- projected 10-over score and wickets where relevant;
- projected final score;
- probability by phase and full innings;
- two- and three-early-wicket sensitivity;
- shortened-innings settlement state.

## 13. Basketball, AFL, rugby and American football

These are compound high-scoring processes. Pure Poisson totals generally understate structure or tails.

### Basketball/WNBA

Simulate:

1. possessions;
2. offensive efficiency by lineup;
3. two-, three- and free-throw outcomes;
4. turnovers and offensive rebounds;
5. rotation/minutes;
6. late fouling and overtime.

Use Poisson/NB for player counts such as made threes, assists, rebounds, steals or blocks only after conditioning on projected minutes and role.

### AFL/AFLW

Simulate scoring shots, then classify goals and behinds:

\[
Points=6\times Goals+Behinds
\]

Condition scoring shots on territory, inside-50 quality and opponent defence; condition conversion on shot quality, venue and weather. Model AFLW and AFL separately.

### Rugby league/union

Simulate tries, conversion success, penalty goals and drop goals separately. Do not treat raw points as identical Poisson events.

### NFL/college football

Simulate drives, field position and terminal outcomes: touchdown, field goal, turnover, punt, safety and end-of-half/game. Add the correct overtime rules. A team-points Poisson may be retained only as a benchmark.

## 14. Individual and event props

For player event count \(Y\), include exposure:

\[
\log(\lambda)=\log(\text{projected opportunity})+X\beta
\]

Examples of opportunity:

- minutes, possessions or usage;
- plate appearances or batters faced;
- overs/balls bowled and batting position;
- shots, shifts or ice time;
- snaps, routes or targets;
- service games/points;
- rounds/holes;
- expected bout duration.

Availability and role uncertainty must be simulated, not hidden inside one mean. Use a mixture:

\[
P(Y)=\sum_r P(Y\mid role=r)P(role=r)
\]

This is mandatory for questionable players, minutes limits, projected lineups, substitute roles and uncertain batting/bowling positions.

## 15. Pregame and live separation

Pregame and live forecasts are different models.

Pregame simulation may use only information available at the cutoff. Once play begins:

- condition on current score and time/exposure remaining;
- remove completed phases from the uncertainty;
- update rates from confirmed live pace and surface behaviour;
- update personnel, foul/wicket/card/penalty and fatigue state;
- preserve the pregame prior only as a shrinkage input.

Do not leave a pregame Poisson probability unchanged after a material live-state event.

## 16. Ranking and confidence rules

Simulation probability is one input to ranking, not permission to ignore source quality.

Required ranking probability:

\[
p_{final}=Calibrate\left(
w_d p_{distribution}
+w_b p_{baseline}
+w_c p_{context}
+w_l p_{live}
\right)
\]

Weights must be learned or justified from backtests. Do not use arbitrary fixed weights merely to make the numbers sum to one.

Apply these caps:

- Failed Poisson diagnostics with no valid challenger: maximum 55%.
- Missing confirmed lineup/XI for a lineup-sensitive market: maximum 58%.
- Missing actual cricket pitch report: apply the sports-doc confidence cap.
- Near-line projection within one model standard error or one typical scoring unit: label coin flip/low edge.
- Model disagreement above 10 percentage points: report disagreement and cap confidence.
- Fewer than 100 comparable observations: use shrinkage and a small-sample cap.

The #1 pick still needs the sports document's normal stress test and edge threshold. The bottom pick must survive a failure-path and swap test. A model probability above roughly 30-35% cannot honestly be called close to impossible.

## 17. Required log fields

Add these fields to every new prediction-log row:

```text
FRAMEWORK SWEEP:
MODEL TARGET:
EXPOSURE:
POISSON BASELINE:
POISSON DIAGNOSTICS:
CHALLENGER MODEL(S):
SELECTED MODEL + WHY:
TRAINING WINDOW / DECAY:
INPUT CUTOFF:
SIMULATIONS / SEED:
PROJECTED MEAN / MEDIAN / SD:
P10 / P25 / P75 / P90:
OVER / UNDER / PUSH / VOID:
WIN / DRAW / LOSS OR COVER:
MODEL DISAGREEMENT:
SENSITIVITY TRIGGERS:
CALIBRATION STATUS:
MODEL VERSION / DATA SNAPSHOT:
```

If the model is unavailable, write `MODEL UNAVAILABLE` and do not invent simulation percentages.

## 18. Retrospective and model updating

After settlement:

1. Record the exact score and required phase splits.
2. Record which prediction interval contained the result.
3. Calculate log loss/Brier contribution where applicable.
4. Record Poisson/NB deviance or randomized quantile residual.
5. Classify the miss:
   - mean-rate error;
   - dispersion/tail error;
   - dependence error;
   - opportunity/exposure error;
   - lineup/availability error;
   - surface/weather error;
   - live-state update error;
   - settlement/rules error;
   - rank-slot calibration error.
6. Update model parameters only through the scheduled rolling process; do not manually overreact to one result.
7. Add a new sports-doc lesson only when the mechanism is genuinely new. Otherwise reinforce the existing rule in the results log.

Track by sport and market:

- interval coverage;
- probability calibration;
- mean absolute error;
- Poisson/NB deviance;
- top-pick hit rate;
- bottom-pick win rate;
- model selection frequency;
- frequency with which the challenger beats Poisson;
- tail misses and phase/full-game divergence.

## 19. Reference Python implementation

```python
from __future__ import annotations

from dataclasses import dataclass
from math import sqrt

import numpy as np


@dataclass
class SimulationResult:
    model: str
    simulations: int
    seed: int
    mean: float
    median: float
    std: float
    p10: float
    p25: float
    p75: float
    p90: float
    p_over: float
    p_under: float
    p_push: float
    monte_carlo_se_over: float


def settle_total(scores: np.ndarray, line: float) -> tuple[float, float, float]:
    over = float(np.mean(scores > line))
    under = float(np.mean(scores < line))
    push = float(np.mean(scores == line)) if float(line).is_integer() else 0.0
    return over, under, push


def summarize(
    scores: np.ndarray,
    line: float,
    model: str,
    seed: int,
) -> SimulationResult:
    over, under, push = settle_total(scores, line)
    n = scores.size
    return SimulationResult(
        model=model,
        simulations=n,
        seed=seed,
        mean=float(np.mean(scores)),
        median=float(np.median(scores)),
        std=float(np.std(scores, ddof=1)),
        p10=float(np.percentile(scores, 10)),
        p25=float(np.percentile(scores, 25)),
        p75=float(np.percentile(scores, 75)),
        p90=float(np.percentile(scores, 90)),
        p_over=over,
        p_under=under,
        p_push=push,
        monte_carlo_se_over=sqrt(over * (1.0 - over) / n),
    )


def simulate_poisson(
    mean: float,
    line: float,
    simulations: int = 100_000,
    seed: int = 20260624,
) -> SimulationResult:
    if mean < 0:
        raise ValueError("mean must be non-negative")
    rng = np.random.default_rng(seed)
    scores = rng.poisson(lam=mean, size=simulations)
    return summarize(scores, line, "poisson", seed)


def simulate_negative_binomial(
    mean: float,
    dispersion_phi: float,
    line: float,
    simulations: int = 100_000,
    seed: int = 20260624,
) -> SimulationResult:
    """
    NB2 parameterization:
      E[Y] = mean
      Var[Y] = mean + mean**2 / dispersion_phi
    Larger phi approaches Poisson.
    """
    if mean < 0 or dispersion_phi <= 0:
        raise ValueError("mean must be non-negative and phi positive")
    rng = np.random.default_rng(seed)
    probability = dispersion_phi / (dispersion_phi + mean)
    scores = rng.negative_binomial(
        n=dispersion_phi,
        p=probability,
        size=simulations,
    )
    return summarize(scores, line, "negative_binomial_nb2", seed)


def simulate_bivariate_poisson(
    home_independent: float,
    away_independent: float,
    shared_intensity: float,
    simulations: int = 100_000,
    seed: int = 20260624,
) -> tuple[np.ndarray, np.ndarray]:
    """
    H = X1 + X3, A = X2 + X3.
    X3 creates positive score correlation.
    """
    values = (home_independent, away_independent, shared_intensity)
    if any(value < 0 for value in values):
        raise ValueError("intensities must be non-negative")
    rng = np.random.default_rng(seed)
    home_only = rng.poisson(home_independent, simulations)
    away_only = rng.poisson(away_independent, simulations)
    shared = rng.poisson(shared_intensity, simulations)
    return home_only + shared, away_only + shared


def outcome_probabilities(
    home_scores: np.ndarray,
    away_scores: np.ndarray,
) -> dict[str, float]:
    if home_scores.shape != away_scores.shape:
        raise ValueError("score arrays must have the same shape")
    return {
        "home_win": float(np.mean(home_scores > away_scores)),
        "draw": float(np.mean(home_scores == away_scores)),
        "away_win": float(np.mean(home_scores < away_scores)),
        "home_mean": float(np.mean(home_scores)),
        "away_mean": float(np.mean(away_scores)),
        "total_mean": float(np.mean(home_scores + away_scores)),
    }
```

## 20. Simplified conditional cricket simulation

This is a template, not a fitted production model:

```python
def simulate_t20_innings(
    phase_means: tuple[float, float, float],
    phase_phi: tuple[float, float, float],
    simulations: int = 100_000,
    seed: int = 20260624,
) -> np.ndarray:
    """
    Phases: powerplay (1-6), middle (7-15), death (16-20).
    Replace illustrative wicket probabilities and penalties with fitted values.
    """
    rng = np.random.default_rng(seed)
    totals = np.zeros(simulations, dtype=int)

    powerplay_wickets = rng.choice(
        [0, 1, 2, 3, 4],
        size=simulations,
        p=[0.18, 0.35, 0.29, 0.14, 0.04],
    )

    pp_mean, middle_mean, death_mean = phase_means
    pp_phi, middle_phi, death_phi = phase_phi

    pp_p = pp_phi / (pp_phi + pp_mean)
    pp_runs = rng.negative_binomial(pp_phi, pp_p, simulations)

    middle_multiplier = np.select(
        [
            powerplay_wickets <= 1,
            powerplay_wickets == 2,
            powerplay_wickets >= 3,
        ],
        [1.04, 0.92, 0.78],
    )
    adjusted_middle = middle_mean * middle_multiplier
    middle_p = middle_phi / (middle_phi + adjusted_middle)
    middle_runs = rng.negative_binomial(middle_phi, middle_p)

    wickets_after_15 = powerplay_wickets + rng.binomial(4, 0.35, simulations)
    death_multiplier = np.select(
        [
            wickets_after_15 <= 3,
            wickets_after_15 <= 5,
            wickets_after_15 >= 6,
        ],
        [1.12, 0.94, 0.67],
    )
    adjusted_death = death_mean * death_multiplier
    death_p = death_phi / (death_phi + adjusted_death)
    death_runs = rng.negative_binomial(death_phi, death_p)

    totals += pp_runs + middle_runs + death_runs
    return totals
```

Production cricket code must fit wicket probabilities, phase means, dispersion and role effects from same-format ball-by-ball data. The illustrative constants above must never be presented as researched probabilities.

## 21. Validation and leakage controls

- Use walk-forward or expanding-window validation.
- Never randomly shuffle future matches into training folds.
- Freeze every feature at the historical prediction cutoff.
- Keep lineup-confirmed and projected-lineup models separate.
- Tune decay, regularization and dispersion only inside training folds.
- Calibrate probabilities on a separate rolling calibration window.
- Compare against naive baselines:
  - league/competition average;
  - season team average;
  - opponent-adjusted rolling mean;
  - empirical score distribution.
- Save model, data and source versions for every logged card.

## 22. Research basis

Primary and official references:

- NIST Poisson definition and probability mass function:  
  https://www.itl.nist.gov/div898/handbook/eda/section3/eda366j.htm
- Maher, *Modelling Association Football Scores* (1982):  
  https://doi.org/10.1111/j.1467-9574.1982.tb00782.x
- Dixon and Coles, *Modelling Association Football Scores and Inefficiencies in the Football Betting Market* (1997):  
  https://doi.org/10.1111/1467-9876.00065
- Karlis and Ntzoufras, *Analysis of Sports Data by Using Bivariate Poisson Models* (2003):  
  https://doi.org/10.1111/1467-9884.00366
- Koopman and Lit, dynamic bivariate Poisson football model:  
  https://doi.org/10.1111/rssa.12042
- Stan negative-binomial-2 mean/variance parameterization:  
  https://mc-stan.org/docs/2_20/functions-reference/nbalt.html
- SciPy Poisson and Skellam implementations:  
  https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html  
  https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.skellam.html
- NumPy Poisson and negative-binomial random generators:  
  https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.poisson.html  
  https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.negative_binomial.html
- scikit-learn Poisson regression and mean Poisson deviance:  
  https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.PoissonRegressor.html  
  https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_poisson_deviance.html
- Cricket run-rate modelling example using a Poisson log-linear framework:  
  https://doi.org/10.1111/rssc.12298
- Low-level point model for tennis rather than match-score Poisson:  
  https://doi.org/10.1093/imaman/dps010

## 23. Final operating rule

Always run Poisson when the target is a defensible event count, but never worship it.

The model must earn promotion from baseline to selected distribution through:

1. correct rules and exposure;
2. fresh source inputs;
3. acceptable dispersion and dependence diagnostics;
4. time-ordered out-of-sample calibration;
5. sport-specific mechanics;
6. agreement with the retrospective lessons already stored in the workspace.

If those conditions fail, use the better sport-native model or declare the simulation unavailable.
