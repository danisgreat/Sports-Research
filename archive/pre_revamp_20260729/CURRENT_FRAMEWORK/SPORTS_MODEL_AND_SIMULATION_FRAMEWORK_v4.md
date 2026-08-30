# Sports model, distribution and simulation framework v4

Status: **ACTIVE RESEARCH STANDARD**  
Effective date: **2026-07-17**

## 1. Scope

This document defines when a quantitative model may be developed, compared, validated, and used. It replaces the idea that one Poisson or Monte Carlo procedure can be valid for every sport.

A simulation is a calculator for assumptions. More simulated trials reduce Monte Carlo noise; they do not correct a wrong mean, wrong distribution, stale lineup, hidden dependence, data leakage, or mismatched market contract.

## 2. First define the forecast target

Before choosing a distribution, specify:

- sport, competition, season and ruleset;
- market and settlement contract;
- forecast horizon and state (`PREGAME` or exact `LIVE` state);
- target variable and unit of exposure;
- information cutoff and feature availability;
- push, void, abandonment, overtime and shortened-event branches.

If the target cannot be stated precisely, do not model it.

## 3. Minimum model comparison

For a count-like target, compare at least three approaches where data permits:

1. A transparent baseline, such as historical rate, market-implied baseline, Poisson, or logistic model.
2. A dispersion/dependence challenger, such as negative binomial, generalized Poisson, Conway–Maxwell–Poisson, zero-inflated/hurdle, bivariate, hierarchical, or correlated-score model.
3. A sport-native or non-parametric challenger, such as an empirical bootstrap, possession/drive/innings/over simulation, point-game-set Markov chain, survival model, or event-level model.

The preferred model is selected by time-ordered out-of-sample evidence, not by which one supports a desired pick.

## 4. When Poisson is defensible

Poisson may be a useful baseline when:

- the target is a non-negative count over a defined exposure;
- event rate is reasonably stable within the forecast window;
- variance is not materially different from the mean after conditioning;
- events are not excessively clustered, inhibited or dependent;
- structural zeros and state changes are limited;
- exposure is known or explicitly modeled.

Test these assumptions. If variance materially exceeds the mean, consider negative-binomial, mixture, compound, or empirical alternatives. If opponents’ scores are dependent, consider bivariate or state-based models. If scoring rate changes with game state, model the state.

## 5. Sport-native starting matrix

| Sport / target | Primary modeling unit | Useful candidates | Common invalid shortcut |
|---|---|---|---|
| Soccer goals | possessions, shots, xG events | hierarchical xG, Dixon–Coles, bivariate score, event simulation | unadjusted recent goals Poisson |
| Baseball runs | plate appearances, innings | PA/inning model, negative binomial, empirical bootstrap, base-out state | one full-game Poisson from season average |
| Cricket innings/chase | balls, overs, wickets/resources | ball/over wicket-state, innings simulation, empirical state analogues | full-innings Poisson ignoring wickets |
| Basketball points | possessions | lineup/possession simulation, efficiency model | raw points average without pace |
| AFL points/margin | scoring shots, field position, conversion | scoring-shot plus conversion, state simulation | homogeneous point-count Poisson |
| Rugby league/union points | sets/possessions and scoring sequences | compound event/state model, empirical drive/set simulation | treating tries and conversions as independent |
| American football points | drives | drive outcome model, field-position state simulation | full-game Poisson ignoring possessions |
| Ice hockey goals | shots/xG and goalie state | hierarchical/bivariate goal model, shot-event simulation | goalie-unadjusted goal average |
| Tennis | points, games, sets | serve/return Markov model | modeling match wins as a count |
| Volleyball | rallies, sets | rally/set Markov model | total-points Poisson ignoring set count |
| Golf | holes | ordinal/multinomial hole scores, hierarchical player-course model | Poisson for rank |
| Motorsport | laps, reliability, rank | survival/reliability and rank model | normal/Poisson placement shortcut |
| Combat | time and finish hazard | competing-risk/survival model | independent round counts |

## 6. Data construction and leakage prevention

- Use only information available by the historical forecast cutoff.
- Split by time; do not randomly mix later games into earlier training folds.
- Put feature engineering, imputation, selection and hyperparameter tuning inside the training fold.
- Keep repeated teams, players, seasons and events grouped where leakage could occur.
- Version the ruleset and data definitions.
- Retain missingness indicators when availability itself is informative.
- Do not backfill confirmed lineups, final weather, closing prices or corrected statistics into an earlier snapshot.
- Deduplicate rescheduled or replayed events and resolve team/player aliases.

## 7. Validation design

Use rolling-origin or expanding-window validation:

1. train only on events before cutoff A;
2. predict the next block;
3. advance the cutoff;
4. repeat without using future outcomes;
5. reserve a final untouched period when sample size permits.

Report:

- number of events and independent forecast clusters;
- date range and competition coverage;
- missing/excluded records and reasons;
- baseline and challenger performance;
- uncertainty intervals or bootstrap distributions;
- subgroup performance by season, competition, market, state and line range;
- performance drift over time.

Do not optimize repeatedly on the final holdout.

## 8. Evaluation metrics

For probabilities:

- log loss;
- Brier score;
- calibration curve or reliability table;
- calibration intercept/slope where appropriate;
- sharpness only after checking calibration;
- uncertainty bands, not just point estimates.

For counts or continuous targets:

- proper predictive score such as log predictive density or CRPS;
- MAE/RMSE as secondary descriptive metrics;
- interval coverage and width;
- residual dispersion and tail checks.

For decisions:

- performance at the exact recorded line and price;
- push/void handling;
- closing-line comparison only when timestamp and comparable market are known;
- ROI/yield only when stake, odds, book, timestamp, commission and fill are recorded.

Raw hit rate is not sufficient. A collection of heavy favorites or complementary selections can show a high apparent hit rate without useful forecasting skill.

## 9. Calibration and publication

A reliability table must use prospectively frozen forecasts. Each row needs forecast time, event start, probability, outcome, market contract and model version.

Use sample-size-aware bins or isotonic/logistic recalibration fitted only on past validation data. Report uncertainty for each bin. Never label arbitrary verbal bands such as “high confidence” as calibrated without evidence.

Publication gate for a numeric probability:

- applicable registered model version;
- no unresolved leakage or identity issue;
- out-of-sample evaluation complete;
- calibration evidence adequate for the market/state;
- current inputs within supported ranges;
- prediction frozen before outcome information;
- probability and uncertainty logged before delivery.

If any gate fails, publish a qualitative verdict.

## 10. Simulation requirements

When simulation is useful:

1. sample parameter uncertainty, not only outcome randomness;
2. preserve dependence between teams, players and phases;
3. incorporate exposure and state transitions;
4. implement push/void/overtime/shortened-event rules explicitly;
5. set and record a random seed for reproducibility;
6. run enough draws for the requested precision and report Monte Carlo error;
7. perform sensitivity analysis on uncertain inputs;
8. compare simulated distributions with held-out empirical distributions.

There is no magic draw count. One hundred thousand trials can still give a precise answer to the wrong model.

## 11. Live-model requirements

A live model must condition on the complete current state and update future exposure. At minimum include the relevant sport state:

- baseball: inning half, outs, bases, score, current pitchers, batting order and home batting entitlement;
- cricket: innings, score, balls/overs, wickets, target/resources and batters/bowlers;
- soccer: score, clock, cards, substitutions and event quality;
- AFL/rugby/basketball: score, clock, possession/territory, player availability and tactical state;
- tennis/volleyball: server, point/game/set state.

Historical pregame accuracy does not validate a live model. Validate live snapshots by time remaining and state range.

## 12. Dependence and portfolio rules

- Tag exact complements, mutually exclusive branches, nested lines, same-game outcomes and shared-player/team exposures.
- Evaluate cards at the event or thesis cluster level as well as row level.
- Do not count both sides of a complementary pair as separate model opportunities.
- If multiple options are requested for comparison, only rows actually recommended are calibration-eligible.
- A four-selection response is not four units of independent evidence.

## 13. Development status labels

- `IDEA` — plausible mechanism; no working model.
- `RESEARCH_ONLY` — code or calculation exists; not validated for publication.
- `VALIDATED_LIMITED` — passes stated out-of-sample tests only for a narrow sport/competition/market/state.
- `MONITORED` — prospectively issuing, with ongoing calibration and drift checks.
- `SUSPENDED` — data, drift, integrity or performance issue prevents use.
- `RETIRED` — deliberately replaced; retained for history.

“Active model” must always include its scope and status. A qualitative sport module is active analysis guidance, not a calibrated quantitative model.

## 14. Honest limitations inherited from the audit

The legacy ledger cannot validate current performance because it included complementary outcomes, custom top/bottom scoring, mixed pregame/live records, mutable rows, and incomplete price/stake provenance. It may generate hypotheses but may not be used to claim verified accuracy, profitability, or calibration.

This framework becomes trustworthy only through future frozen forecasts and honest settlements.

