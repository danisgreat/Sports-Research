# Comprehensive methodology audit — 2026-07-16

## Scope and audit standard

This is an internal methodology audit of:

- `combined_sports_doc_v2.txt` (current active file as read on 2026-07-16);
- `POISSON_DISTRIBUTION_AND_SIMULATION_FRAMEWORK.md`;
- `AUDIT_AND_CHANGES_2026-06-12.md`;
- `PREDICTION_RESULTS_LOG_v2.md`, `PREDICTION_RESULTS_LOG_v3.md`, and `SPORTS_CALIBRATION_LEDGER_v2.csv` where they reveal how the rules were actually applied.

Line references are to the versions read during this audit. The combined document was being extended concurrently, but the cited material is before the appended tail and its line positions were stable during the audit.

This audit distinguishes four different questions that the current system repeatedly blends:

1. **Forecasting:** is the stated probability calibrated out of sample?
2. **Ranking:** is option A genuinely more likely than option B?
3. **Betting value:** is the calibrated probability above the price-implied break-even probability after vig/commission?
4. **Execution/staking:** given value, uncertainty, bankroll and correlation, should any stake be placed and how much?

The system is not currently reliable enough to claim a production-grade answer to any of those four questions across all sports. It contains many good safeguards, but the actual forecasting objective, evaluation design, and model implementation are not coherent. No honest process can promise “no mistakes.” The correct promise is a frozen, auditable process with measured error, explicit uncertainty, and abstention when evidence is insufficient.

## Executive finding

The largest cause of wrong or misleading predictions is **not merely failure to follow the written process**. It is a design failure: the system optimizes a custom four-option top/bottom-slot score instead of a predeclared, out-of-sample forecasting or expected-value objective. It then mixes user-supplied markets, self-selected “safety” outcomes, exact complements, overlapping outcomes, absurd structural thresholds, pregame forecasts, start-window forecasts, and live forecasts in the same performance narrative.

The prior audit said that process compliance rather than process design caused the failures (`AUDIT_AND_CHANGES_2026-06-12.md:21-24`). That conclusion was too charitable and is contradicted by the evidence below. The current process can be followed faithfully and still produce misleading performance claims because:

- its scoring rule is not proper and rewards card construction;
- its sample is selected after looking across many candidate markets;
- its probabilities are often narrative adjustments to nested last-N hit rates rather than reproducible model outputs;
- its live and pregame records are not cleanly separated;
- its simulations frequently quantify Monte Carlo noise while ignoring parameter and model uncertainty;
- no offered price means probability ranking is not betting value;
- one-off postmortem rules are repeatedly fit to the same outcomes later used to judge the system.

**Immediate recommendation:** retire the adjusted top/bottom “penalty record” as an accuracy KPI, suspend staking language, freeze the current heuristic system as an archived version, and rebuild calibration from immutable pre-event snapshots only. Keep the source, ruleset, settlement and availability controls, but replace the ranking economy and ad hoc probability construction.

## What the ledger actually shows

I programmatically recounted `SPORTS_CALIBRATION_LEDGER_v2.csv:2-439` as read during the audit:

- 438 data rows, of which one is the template row;
- 437 real option rows across 102 nominal card IDs;
- 431 rows with a decisive W/L and a numeric stated probability;
- four unresolved/ungraded rows and two pushes;
- 126/437 rows flagged `projection_error=TRUE` and 108/437 flagged `rank_slot_calibration_error=TRUE` (these are subjective flags, not independent tests).

Individual-option calibration by recorded rank was:

| Rank | Decisive N with probability | Mean stated probability | Actual hit rate | Mean Brier score |
| --- | ---: | ---: | ---: | ---: |
| 1 | 100 | 65.4% | 66.0% | 0.210 |
| 2 | 96 | 59.9% | 63.5% | 0.219 |
| 3 | 94 | 52.4% | 56.4% | 0.224 |
| 4 | 95 | 45.0% | 46.3% | 0.198 |

These figures do **not** validate the system, because the rows are correlated within events, the candidate markets were not predeclared, self-selected safety markets are mixed with user-provided lines, and pregame/live modes are mixed. They do, however, conclusively refute the recurring idea that #4 is normally a <=30% outcome. Its recorded probability is about 45% and it wins about 46%.

The older log itself reports raw #1/#2/#3/#4 rates of 64.8%/57.1%/47.9%/49.4% (`PREDICTION_RESULTS_LOG_v2.md:45`; `combined_sports_doc_v2.txt:8804-8810`). That is the honest raw result. The headline “~82.7% top-pick” number is an exemption-adjusted penalty statistic, not a hit rate (`PREDICTION_RESULTS_LOG_v2.md:17,34-48`; `combined_sports_doc_v2.txt:8807-8810`). Yet the system still tells itself to protect an 80% top KPI (`combined_sports_doc_v2.txt:8621-8624`).

Canonical family coverage in the current ledger is also uneven:

| Canonical family | Option rows | Decisive rows | Rank-1 W/N | Rank-4 W/N |
| --- | ---: | ---: | ---: | ---: |
| Basketball (all labels combined) | 135 | 135 | 12/24 | 18/23 |
| Cricket (all labels combined) | 101 | 97 | 15/24 | 10/24 |
| Soccer (all labels combined) | 81 | 81 | 16/20 | 9/19 |
| Baseball (all labels combined) | 76 | 74 | 15/19 | 4/19 |
| AFL | 44 | 44 | 8/13 | 3/10 |

There are no comparable current-ledger samples for NFL, NHL, NRL, tennis, volleyball, golf, motorsport, boxing or MMA. The broad “all sports” scope is therefore aspirational, not empirically supported. The main document names AFL, MLB, cricket, basketball, NFL, NHL, NRL and soccer (`combined_sports_doc_v2.txt:1-3`), while the Poisson matrix additionally names tennis, volleyball, golf, motorsport and combat sports (`POISSON_DISTRIBUTION_AND_SIMULATION_FRAMEWORK.md:175-204`). Only five canonical families have meaningful ledger data.

The sport labels are fragmented—e.g. `Basketball`, `WNBA`, `Basketball/WNBA`; `Baseball`, `MLB`, `Baseball/MLB`; `Cricket`, `Cricket/WT20I`, `Cricket/T20I`—with examples at `SPORTS_CALIBRATION_LEDGER_v2.csv:34-35,74-75,211-212,223-224,249-250`. This makes sport-level calibration dependent on naming choices and permits accidental cherry-picking.

## Highest-severity causes of wrong or misleading predictions

### S0-1. The objective and scoring rule are wrong

**Evidence**

- The system targets top-pick hit rate >=80% and bottom-pick win rate <=30% (`combined_sports_doc_v2.txt:8621-8630`).
- It adds extra losses when #1 loses or #4 wins, with exemptions when the top half sweeps (`combined_sports_doc_v2.txt:8652-8655`; `PREDICTION_RESULTS_LOG_v2.md:24-26,43-45`).
- It explicitly prioritizes “structural near-locks” for #1 and their mirrors for the bottom (`combined_sports_doc_v2.txt:8631-8653`).
- The chase-cap example calls Under 254.5 while chasing 167 a ~99.9% lock (`combined_sports_doc_v2.txt:3155`; `PREDICTION_RESULTS_LOG_v2.md:368`).
- The log can call a card 4-0 even when its separate winner prediction loses; Portugal-DR Congo is a clear example (`PREDICTION_RESULTS_LOG_v2.md:530`), as is Czechia-South Africa (`PREDICTION_RESULTS_LOG_v3.md:138`).

**Why this causes errors**

This is not a proper scoring rule. It rewards selecting trivially broad or structurally impossible thresholds, choosing positive “safety” outcomes, and excluding difficult but decision-relevant winner calls from the card record. A system can improve its top hit rate by choosing Under 4.5 goals, double chance, +2.5 run cushions, or a target-capped cricket under—without learning anything about value or becoming better at the user’s main question.

The extra penalty economy is entirely self-created. Saying the bottom slot is the “entire adjusted-record deficit” (`AUDIT_AND_CHANGES_2026-06-12.md:10-11`) is circular: the deficit exists because the system invented an extra loss whenever the chosen bottom wins. It is not evidence of financial loss or forecast skill.

The top-half-sweep exemption further makes the score non-stationary: the same #4 outcome is penalized or exempt depending on unrelated picks. That prevents clean calibration.

**Required replacement**

- Score every frozen probability with Brier score and log loss.
- Track the primary user-visible recommendation separately from secondary claims.
- Do not compute a composite W-L card score for correlated legs.
- Do not exempt or double-penalize any row.
- Report rank discrimination only as a secondary metric: pairwise ordering accuracy or Spearman correlation between forecast probability and outcomes, clustered by event.
- If a candidate market is structurally impossible because of a rules/target mismatch, flag likely bad market encoding; do not count it as forecast skill.

### S0-2. Candidate-selection bias makes hit rates and 4-0 cards non-comparable

**Evidence**

- Numerous rows are explicitly “self-selected best four,” “self-selected safety outcomes,” or self-selected parlays (`PREDICTION_RESULTS_LOG_v2.md:525,529-532`; `PREDICTION_RESULTS_LOG_v3.md:138,146,151,160,338,346`).
- Norway-England selected four outcomes all estimated at 75-86%, then reported a 4-0 sweep (`PREDICTION_RESULTS_LOG_v3.md:338`).
- Argentina-Switzerland selected broad Swiss Under 2.5, Argentina/draw, Argentina Over 0.5 and corners Under 13.5, then reported 4-0 (`PREDICTION_RESULTS_LOG_v3.md:346`).
- The system’s own language calls these “safety cards” (`PREDICTION_RESULTS_LOG_v3.md:41,49`).

**Why this causes errors**

Searching across many potential markets and logging only the four most likely creates winner’s-curse and multiple-testing bias. The recorded probability distribution depends on how many candidate markets were inspected. A four-pick safety card is not comparable with a card where the user forces two exact complements and two spreads. Card hit rate therefore measures card construction at least as much as predictive skill.

It also hides misses that matter to the user. A 4-0 safety card plus a wrong winner is described as strong even though the explicit event-outcome prediction was wrong.

**Required replacement**

- Predeclare the candidate market universe before research, or log every candidate inspected.
- Record `selection_mode = user_supplied | fixed_universe | model_selected`.
- Never combine these modes in one performance statistic.
- For model-selected markets, evaluate the full selection pipeline out of sample, including rejected candidates, and control false discovery/selection bias.
- Put the primary requested outcome in the primary-score field; secondary safety claims cannot overwrite it.

### S0-3. Pregame, start-window and live predictions are mixed, and immutable cutoff evidence is missing

**Evidence**

- The core correctly says a cutoff violation must hard-fail the snapshot (`combined_sports_doc_v2.txt:750-771`) and the Poisson framework requires frozen features (`POISSON_DISTRIBUTION_AND_SIMULATION_FRAMEWORK.md:652-665`).
- But a historical soccer row says the match may already have been in play or complete and was nevertheless “treated as pregame per user framing” (`PREDICTION_RESULTS_LOG_v2.md:376`). That is an explicit game-state failure.
- A WNBA row contains pregame, live correction, weather correction and final retrospective in one mutable record (`PREDICTION_RESULTS_LOG_v2.md:373`).
- The current log counts a Q1 Over after 43 points had already been scored, despite the exact clock being unavailable, alongside ordinary cards (`PREDICTION_RESULTS_LOG_v3.md:340`).
- It also contains start-window re-ranks and live-halftime cards (`PREDICTION_RESULTS_LOG_v3.md:330,332,348,357,361,373`).
- The ledger’s final two rows are a live-halftime AFL forecast, yet the schema has no `forecast_mode`, `game_clock_at_cutoff`, `source_known_at`, `source_published_at`, `fetched_at`, `model_version` or immutable snapshot hash (`SPORTS_CALIBRATION_LEDGER_v2.csv:1,438-439`).
- The main document later requires those timestamp fields (`combined_sports_doc_v2.txt:9139-9155`), but the actual ledger does not carry them.

**Why this causes errors**

Live forecasts are easier or harder depending on the state and cannot be pooled with pregame forecasts. Selecting an Under 4.5 at 13 minutes while 0-0 (`PREDICTION_RESULTS_LOG_v3.md:357`) is a valid live question, but it is not evidence about pregame skill. Likewise, selecting Q1 Over after 43 points is a conditional in-play forecast, not a pregame phase forecast.

Mutable rows that contain prediction, live updates and settlement make it impossible to prove which facts were available when the probability was stated. Even where no leakage occurred, the data cannot establish that fact.

**Required replacement**

- Use append-only snapshots. Never edit the original forecast fields after publication.
- Required keys: `prediction_id`, `event_id`, `market_id`, `mode` (projected-lineup pregame / confirmed-lineup pregame / live), `cutoff_utc`, `game_clock`, `source_known_at`, `source_published_at`, `fetched_at`, `data_hash`, `feature_version`, `model_version`, `probability`, `uncertainty_interval`, `selection_mode`.
- Store settlement in a separate table linked by `prediction_id`.
- Calibrate each mode separately. A forecast at Q1 43 points can only be compared with forecasts made at equivalent live states.
- Quarantine every historical row whose cutoff cannot be reconstructed; use it as qualitative research, not quantitative calibration.

### S0-4. Recorded probabilities are frequently heuristic narratives, not reproducible estimates

**Evidence**

- The process says probability starts from exact-market L5/L10/L15/L20 hit counts and is then adjusted for context (`combined_sports_doc_v2.txt:8664-8666,8917-8919`).
- Those windows are nested, so they are not four independent confirmations. The system nevertheless mandates all four for both teams and decision-driving players (`combined_sports_doc_v2.txt:16-20,8927-8937`).
- A WNBA example pools L10/L20 counts for both teams, applies an availability haircut and market sanity check, and calls the result a model (`PREDICTION_RESULTS_LOG_v3.md:322`). No reproducible coefficient or transformation maps those inputs to the final percentages.
- The sport annexes assign round-number weights without fitted coefficients or validation: AFL (`combined_sports_doc_v2.txt:1856-1864`), MLB (`:2913-2920`), cricket (`:4579-4586`), NRL (`:5576-5583`), soccer (`:6532-6539`), NHL (`:7452-7459`) and NFL (`:8423-8430`).
- The Poisson framework correctly says weights must be learned or justified from backtests (`POISSON_DISTRIBUTION_AND_SIMULATION_FRAMEWORK.md:370-381`), contradicting those fixed weights.
- The practical blend asks for baseline, distribution and ML layers, but supplies no fitted ML pipeline and permits two layers when data are thin (`combined_sports_doc_v2.txt:778-797`).

**Why this causes errors**

An empirical hit rate at today’s threshold is a useful descriptive feature, not automatically a probability for today’s event. Schedule strength, venue, line movement, lineup and role changes alter the target distribution. Pooling two teams’ game logs can double-count their head-to-head games; treating L5/L10/L15/L20 as repeated evidence pseudo-replicates the same observations. Narrative “haircuts” and hand weights make the number non-reproducible and easy to tune toward the desired ranking.

**Required replacement**

- Treat last-N values as features, not votes. Prefer one prespecified decay function selected inside training folds.
- Fit coefficients on historical cutoff-safe data with hierarchical shrinkage by league/team/season.
- Every displayed probability must be reproducible from a model artifact and feature snapshot.
- If only a heuristic scenario range exists, report a qualitative band and `MODEL UNAVAILABLE`; do not attach a precise 58%, 66% or 82%.
- Remove all round-number sport weights unless out-of-sample evidence supports them.

### S0-5. Betting probability, EV and staking are not defined coherently

**Evidence**

- The main document allows odds as supporting context by default (`combined_sports_doc_v2.txt:13-14,1010-1016`), while the Poisson framework says no odds or prices unless the user explicitly authorizes them (`POISSON_DISTRIBUTION_AND_SIMULATION_FRAMEWORK.md:16`).
- Other sections say the workflow is market-aware, should establish opening/current/consensus price, and should be judged partly by CLV (`combined_sports_doc_v2.txt:1748-1775,2803-2827,4480-4500,6430-6453`).
- The document says staking belongs only in an explicit execution note and that account/stake-limit workflows are not implemented (`combined_sports_doc_v2.txt:570-585`).
- Nevertheless a no-edge WNBA row calls itself a “watchlist/micro-stake card” without establishing executable price, EV, bankroll or risk tolerance (`PREDICTION_RESULTS_LOG_v3.md:322`).
- The sport “minimum edge” thresholds are fixed differences in points/runs/goals (`combined_sports_doc_v2.txt:1776-1784`, repeated at `:2835-2843,4502-4510,5500-5508,6455-6463`). They do not account for price, distribution width, push probability, model error or commission.

**Why this causes errors**

The most likely outcome is not necessarily the best wager. At decimal odds `d`, a no-push bet requires probability above `1/d`; at different prices, a 45% outcome can have more value than a 70% outcome. A raw projected-score gap is not a universal EV threshold. Three points in an NBA total have a different probability impact at different totals and variance regimes. A whole-number line also has push mass.

Staking without price and bankroll is unjustified. Even with positive point-estimate EV, estimation uncertainty and correlated positions can make the optimal stake zero.

**Required replacement**

- Establish two explicit modes:
  - `RESEARCH_ONLY`: no odds, no EV claim, no stake language.
  - `PRICE_ENABLED`: executable odds, bookmaker/exchange, timestamp, commission, limits and complete market captured.
- De-vig the complete market using a declared method. Keep market-implied probability separate from model probability.
- For decimal odds `d`, use `EV_per_unit = p_win*(d-1) - p_loss`; push/void contributes zero.
- Record break-even probability, model probability, uncertainty interval, EV interval and price expiry.
- Bet only if the conservative probability bound clears break-even plus a prevalidated model-risk buffer.
- If the user explicitly requests staking and provides bankroll/risk constraints, use capped fractional Kelly only: `f = k*(p*d - 1)/(d - 1)`, with `k <= 0.25`, probability shrunk toward the market/base rate, and event/portfolio correlation caps. Otherwise give no stake.

### S1-6. Poisson and simulation rules are theoretically stronger than their implementation

**What is correct and should be retained**

- The framework explicitly recognizes equal mean/variance, stable-rate and dependence assumptions (`POISSON_DISTRIBUTION_AND_SIMULATION_FRAMEWORK.md:55-78`).
- It requires Poisson, a dispersion/dependence challenger and a sport-native challenger (`:80-88`).
- It correctly says baseball and cricket need state/phase models, basketball/AFL/NFL need compound opportunity models, and soccer/hockey need dependence treatment (`:175-204,206-233,235-323`).
- It correctly requires walk-forward validation and frozen features (`:652-665`).

**What is wrong in implementation**

1. **The code simulates assumed parameters; it does not estimate or validate them.** The reference functions accept a mean and optional dispersion and generate outcomes (`POISSON_DISTRIBUTION_AND_SIMULATION_FRAMEWORK.md:454-589`). There is no fitted attack/defence model, likelihood, regularization, posterior, feature pipeline, temporal cross-validation or calibration code.

2. **100,000 simulations create false confidence.** The framework mandates 100,000 runs and multiple seeds (`:134-159`). That reduces Monte Carlo error conditional on the chosen parameters, but the dominant uncertainty is the chosen mean, dispersion, lineup state and model family. Three seeds that agree to a tenth of a point say nothing about model accuracy.

3. **The blend formula is not a coherent probability model.** `p_final = Calibrate(w_d p_distribution + w_b p_baseline + w_c p_context + w_l p_live)` (`:366-381`) can double-count correlated evidence; `p_context` is not defined as an independently calibrated probability; and pregame/live terms should not coexist once the event is live.

4. **Model selection is often conceptual, not fitted.** Norway-England applies an independent Poisson total and an unspecified “role/tournament adjustment and haircut” (`PREDICTION_RESULTS_LOG_v3.md:338`). No diagnostics, fitted challenger or seed are shown even though the framework says simulation probabilities cannot be claimed without them (`POISSON_DISTRIBUTION_AND_SIMULATION_FRAMEWORK.md:25-53`).

5. **The Argentina-Switzerland validation is circular.** Its Poisson lambdas were explicitly chosen to reproduce Opta’s 25,000-simulation outcome probabilities, after which Opta is called a calibrated sport-native check (`PREDICTION_RESULTS_LOG_v3.md:346`). The external forecast is both target and validator. The corner NB mean 10 and dispersion `k=8` are asserted rather than fitted. Running 100,000 draws at three seeds then reports only Monte Carlo repeatability, not forecast validity.

6. **The early-live France-Spain simulation is overprecise.** It reports three 300,000-run ranges to hundredths of a percentage point from manually described gamma-Poisson/bivariate models (`PREDICTION_RESULTS_LOG_v3.md:357`) while parameter/posterior uncertainty is not reported. The later result exposed the problem: the 78% Mbappe SOT leg failed, and the retrospective admitted opponent SOT suppression was underweighted (`PREDICTION_RESULTS_LOG_v3.md:39-40`).

7. **The bivariate reference has a structural limit.** The shared Poisson component in `simulate_bivariate_poisson` permits non-negative covariance only (`POISSON_DISTRIBUTION_AND_SIMULATION_FRAMEWORK.md:554-572`). Sports game-state relationships can induce different or state-dependent dependence. This baseline cannot be treated as universal.

8. **The cricket template contains invented constants.** It uses illustrative wicket probabilities and phase multipliers (`:591-650`). The file warns that these are not production values, which is good, but there is no fitted production replacement. The template should remain test-only and be physically separated from production code.

**Required replacement**

- Use analytic probabilities when available; simulate only when state branching or compound structure requires it.
- Select simulation count by a prespecified Monte Carlo error tolerance, not a universal 100,000 minimum.
- Propagate parameter, input and model uncertainty via posterior draws, nested bootstrap or scenario mixtures.
- Report three intervals separately: process/outcome variance, parameter uncertainty and model/scenario uncertainty.
- An external model may be a benchmark or an ensemble member, never both the target used to choose parameters and an independent validator.
- Require a model artifact with fit diagnostics and walk-forward scores before a distribution can generate published probabilities.

### S1-7. Small samples, nested windows and multiple testing create overconfidence

**Evidence**

- Every card is required to collect nested L5/L10/L15/L20 windows for both teams and many players (`combined_sports_doc_v2.txt:16-20,149-153,8927-8937`).
- Press signals can be promoted at 20 observations and 60% directional accuracy, or extreme-slot influence at 30/65% (`combined_sports_doc_v2.txt:8940-8959`).
- Form thresholds are reconsidered every 20 graded cards based on proportions of labels (`combined_sports_doc_v2.txt:9026-9031`).
- The Poisson framework uses a generic “fewer than 100 comparable observations” cap without defining effective sample or cap size (`POISSON_DISTRIBUTION_AND_SIMULATION_FRAMEWORK.md:383-392`).
- A Summer League card assigned 74%, 68% and 65% based on one Knicks game and four Spurs games (`PREDICTION_RESULTS_LOG_v3.md:342`). It won, but the probabilities are not supported by that sample.
- The next Summer League side assigned Minnesota 68% from one current-squad game per side and lost outright (`PREDICTION_RESULTS_LOG_v3.md:344`). The later retrospective correctly admits one opener cannot support high-60s side probability (`PREDICTION_RESULTS_LOG_v3.md:48`).
- Haaland’s 86% SOT estimate was largely supported by four starts (`PREDICTION_RESULTS_LOG_v3.md:338`).

**Why this causes errors**

L5 is contained in L10, which is contained in L15 and L20. Treating agreement across the four windows as multiple evidence exaggerates effective N. Testing many players, phases, venues, officials, comments and context filters guarantees apparently strong patterns by chance. Twelve successes in 20 observations has a wide uncertainty interval and may be worse than the outcome’s unconditional base rate. A 60% directional accuracy threshold does not test incremental forecast value.

**Required replacement**

- Use effective sample size, not nominal nested-window counts.
- Use hierarchical priors and partial pooling for teams, players and competitions.
- Preselect decay/window hyperparameters inside training folds; do not choose the best-looking window on the current event.
- For candidate signals, require incremental out-of-sample Brier/log-loss improvement versus a base model, with clustered confidence intervals—not raw accuracy >=60%.
- Correct for multiple comparisons or use shrinkage/regularization across the signal family.
- No universal minimum N. Define sport/target-specific precision or posterior-width requirements.

### S1-8. One-result rule creation is retrospective overfitting

**Evidence**

- A #1 loss or #4 win triggers a serious retrospective with “ONE concrete rule change” (`combined_sports_doc_v2.txt:8654`).
- The Poisson framework says the opposite: update parameters only on schedule, do not overreact to one result, and add a new lesson only for a genuinely new mechanism (`POISSON_DISTRIBUTION_AND_SIMULATION_FRAMEWORK.md:421-440`).
- The current log repeatedly adds a new sport rule after individual settlements (`PREDICTION_RESULTS_LOG_v3.md:39-46,48-53,80-127,354,356`).
- The document contains event-specific thresholds and named analogies such as “Australia-tier,” “Garth/Hamilton-class,” and fixed default T20 bands derived from the same historical failures (`combined_sports_doc_v2.txt:86-96,162-168,8823-8827`).

**Why this causes errors**

The same outcomes are used to invent rules and then to claim those rules explain past performance. This is in-sample storytelling. It creates a growing decision tree where almost any future result can be rationalized by selecting a matching lesson, increasing analyst discretion rather than reducing it.

**Required replacement**

- Postmortems may file a candidate hypothesis, not an active rule.
- Promote a rule only at a scheduled model review after testing on subsequent, untouched events.
- Maintain train/validation/test time blocks. A lesson learned from block T can first be evaluated on T+1.
- Consolidate mechanisms into model features; do not create named rules for individual matches unless they reveal a ruleset/settlement bug.
- Use change control: hypothesis, expected direction, affected sport/market, preregistered test, promotion criterion, retirement criterion.

### S1-9. The process is internally contradictory and too large to execute consistently

**Evidence**

- Gate -1 says to read all all-sports governance, the entire sport section, both logs and the ledger before opening any source (`combined_sports_doc_v2.txt:63-70`).
- The active index also requires the full Poisson framework, multiple dated upgrades and a very large output schema (`combined_sports_doc_v2.txt:42-61`).
- Yet a shortcut says only Gates 1, 2, 7 and 9 are unskippable when time-constrained (`combined_sports_doc_v2.txt:8472-8485`).
- The prior audit similarly says skip Section 17 colour first under time pressure (`AUDIT_AND_CHANGES_2026-06-12.md:21-24`).
- Market use is default-allowed in the main file but explicit-authorization-only in the Poisson file, as noted above.
- The top-slot target is described as ~82.7% in one section and ~65% raw in another (`combined_sports_doc_v2.txt:8621-8624,8806-8810`).
- Slot #4 is supposed to be <=30%, but the protocol also permits a forced bottom at 30-40 and current cards routinely place 40-55% outcomes last (`combined_sports_doc_v2.txt:8626-8630`; `PREDICTION_RESULTS_LOG_v3.md:322,344`).

**Why this causes errors**

A protocol that requires thousands of lines of reading before time-sensitive sourcing is not an enforceable control. It encourages checkbox claims, stale cutoffs and selective invocation of whichever rule fits. “Use the stricter/current rule” is not enough when rules conflict and no machine-readable precedence/version exists.

**Required replacement**

- Reduce the operating standard to a short set of hard gates: identity/rules, cutoff/mode, official status/availability, frozen data, model validity, settlement, uncertainty/abstention.
- Put sport detail in versioned model cards, not a single ever-growing instruction stream.
- Archive historical lessons outside the active standard.
- Give every rule an ID, owner, effective date, superseded ID and executable acceptance test.

### S1-10. Calibration and governance are described but not operationalized

**Evidence**

- The document calls for Brier score, log loss, reliability tables, drift monitoring and versioned models (`combined_sports_doc_v2.txt:789-807`), while the old calibration tracker says probability buckets were not yet tracked and core counts were approximate (`PREDICTION_RESULTS_LOG_v2.md:34-53`).
- The Poisson retrospective requires Brier/log loss and residual diagnostics (`POISSON_DISTRIBUTION_AND_SIMULATION_FRAMEWORK.md:421-452`), but most log rows do not contain them.
- The ledger has one mutable row per option and many context fields, but lacks model version, data snapshot hash, cutoff/source timing fields, candidate universe, forecast mode, odds/price, market no-vig probability and closing price (`SPORTS_CALIBRATION_LEDGER_v2.csv:1`).
- Bucket labels are inconsistent (`0-9`, `0-19`, `30-49`, `80+`, `80-89`) across `SPORTS_CALIBRATION_LEDGER_v2.csv:2-439`, making automated calibration fragile.

**Why this causes errors**

The system measures compliance and narrative completeness more consistently than forecast quality. Subjective fields such as source-confidence 1-5 or projection-error flags cannot replace reproducible model metrics. Without a model/version/cutoff key, recalibration can silently mix different forecasting systems.

**Required replacement**

- Build a normalized append-only prediction table and separate settlement table.
- Canonicalize sport, league, competition, market family, mode and model version.
- Produce automated weekly/monthly calibration by sport + league + market + mode + model version.
- Cluster uncertainty by event because multiple legs from one match are correlated.
- Compare against naive and market baselines; report confidence intervals and sample size.
- Do not publish a KPI until its denominator and inclusion rules are immutable.

### S2-11. “StatMuse first” is an access rule masquerading as a modelling rule

**Evidence**

- StatMuse is mandatory first for American leagues (`combined_sports_doc_v2.txt:16-20,82-84,8921-8937`; `POISSON_DISTRIBUTION_AND_SIMULATION_FRAMEWORK.md:18-23`).
- The same file documents venue-qualifier drops, stale tables and misparses (`combined_sports_doc_v2.txt:84,8544-8559,8921-8925`).
- Recent Summer League and WNBA cards repeatedly find it unsupported, stale or misparsed (`PREDICTION_RESULTS_LOG_v3.md:322,340,342,344`).

**Why this causes errors**

Source order should be fact-specific and based on fidelity, latency and reproducibility. A natural-language query site is useful for discovery but should not be a mandatory model gate when official structured APIs or specialist databases better expose the target. Requiring repeated StatMuse attempts wastes the most valuable pre-event time and can encourage misparse acceptance.

**Required replacement**

- Use a fact-to-source registry: official API for event state; official/validated event logs for historical features; specialist sources for advanced metrics; query interfaces only for discovery/cross-check.
- Score source reliability empirically by field and latency, not brand.
- Keep a parser test suite with known fixtures and reject schema/query drift automatically.

## Why the 2026-06-12 audit did not fix the system

The prior audit correctly identified some useful controls—source honesty, form deltas, officials, press-signal caution and bottom-slot leakage. But it missed the core statistical design problems:

1. It called the Gate 0-10 sequence the system’s best feature and praised the existing honesty layer (`AUDIT_AND_CHANGES_2026-06-12.md:5-8`) without testing whether the objective or scoring rule was valid.
2. It described the bottom slot as “the entire deficit” (`:10-11`), accepting the custom penalty economy instead of asking whether the penalty was a meaningful loss function.
3. It concluded that process compliance, not design, caused June failures (`:21-22`). The evidence above shows design failures even under perfect compliance.
4. It added more fields and more rules (`:13-19`) instead of an immutable forecast schema, proper scoring, a fixed candidate universe and out-of-sample validation.
5. Its press-signal promotion thresholds (`:14-15`) were based on raw directional accuracy, not incremental proper-score improvement over a baseline.
6. It acknowledged operational thresholds were unmeasured (`:23-24`) but left them active, allowing them to affect rankings before validation.

The lesson is that more written checks are not a substitute for a valid experimental design.

## Sport-specific replacement requirements

The following are minimum model requirements, not claims that the current data can support them immediately.

| Sport/market | Current major failure | Required production model and adjustments | Go/no-go standard |
| --- | --- | --- | --- |
| Basketball (NBA/WNBA/FIBA/NZNBL/Summer League) | Recent hit rates and simple PF/PA blends; phase/full totals and OT tails inconsistently propagated; tiny Summer League samples overconfident (`PREDICTION_RESULTS_LOG_v3.md:322,340,342,344`) | Joint possession model: possessions distribution; lineup/minutes/usage mixtures; shot-location/2P/3P/FT, turnover and rebound components; late fouling, garbage time and OT; league/ruleset-specific priors; separate Q1/1H/full residual calibration | Separate backtest by NBA, WNBA, FIBA domestic and Summer League. No Summer League side probability from one opener without strong hierarchical shrinkage and wide uncertainty. |
| AFL/AFLW | Simple recent totals/public-model consensus underprices conversion and blowout tails (`PREDICTION_RESULTS_LOG_v3.md:330,348,361`) | Model scoring shots/inside-50 opportunities and goal-vs-behind conversion separately; joint team state; venue dimensions, wind/roof, territory, lineup/ruck/midfield; margin-dependent pace and fourth-quarter blowout/rebound mixtures; AFL and AFLW separate | Walk-forward interval coverage and Brier improvement over Squiggle/season baselines; pregame and halftime models separate. |
| Baseball (MLB/KBO/NPB) | Full-game means over-rely on starter form or recent scoring; bullpen/bridge and extras create tails; leagues and tie rules mixed | Plate-appearance or inning-state simulation; starter batters-faced/innings distribution; handed lineup; bullpen arm availability and leverage order; park/roof/weather/umpire; defence/baserunning; extra-inning/tie branches; separate F5/full/NRFI/props; league-specific rules | Validate separately by MLB/KBO/NPB and market. Compare with no-vig close where price-enabled. No full-game probability from starter-only model. |
| Cricket (T20/WT20I/MLC/ODI/U19) | Narrative surface/venue and nested phase hit rates; hot powerplay carried into full innings; illustrative rather than fitted state model | Ball/over-level run and wicket hazard; batter/bowler roles; phase, wickets in hand, bowling allocation, boundary geometry, toss/XI, pitch/weather/dew; innings truncation, chase target, DLS/reduced overs; hierarchical competition/sex/age priors; scenario mixture when pitch unknown | Separate models by format, competition level and innings role. A missing pitch report widens scenario uncertainty; it does not justify an invented single distribution. No ball/over model means qualitative band only. |
| Soccer | Independent Poisson and broad “safety” selection; hand-chosen lambdas; goals/corners/SOT treated with ad hoc mixtures | Dynamic hierarchical attack/defence model using pre-cutoff xG/shot quality and lineups; Dixon-Coles/bivariate dependence for score; tournament/knockout state; ET/penalties separate; corner NB/state model; player SOT as opportunity/minutes/shot-quality mixture; referee only for relevant markets | Competition/market-specific walk-forward calibration. External Opta forecasts are benchmark/ensemble input, not target and validator. All self-selected markets logged before selection. |
| NRL/rugby | Detailed checklist but no meaningful current ledger evidence | Possession/set simulation with field position, completion/error/penalty/six-again process; try/conversion/penalty/drop-goal compound scoring; spine and forward rotation; HIA/interchange; referee and weather; golden point branch | No “all-sports” confidence claim until a frozen NRL sample beats league-average and market baselines. NRLW separate. |
| NHL | Checklist and arbitrary weights, no meaningful current ledger evidence | Dynamic/bivariate regulation goals from 5v5 xG and special teams; goalie confirmation/mixture; shot-quality and shooting/save regression; empty-net and pull-goalie state; OT/SO branch; lines/TOI for props | NHL-specific walk-forward calibration and goalie-state split before use. |
| NFL/college football | Checklist and arbitrary weights, no meaningful current ledger evidence | Drive-level state model with EPA/success/explosives, field position, pace, fourth-down decisions, TD/FG/punt/turnover/safety, QB/OL/defence availability, weather/kicking and correct OT rules; separate college/NFL | Current-rulebook, league-specific validation; no transfer between college and NFL without a validated hierarchy. |
| Tennis/volleyball/golf/motorsport/MMA | Named only in the Poisson matrix, with no operating annex, data pipeline or calibration | Tennis/volleyball point/rally Markov; golf hole-level ordinal/multinomial with wave weather; motorsport survival/reliability + rank model; combat survival/hazard + categorical result and duration-conditioned counts | **No forecast probabilities** until each has a model card, source map, cutoff-safe dataset and out-of-sample report. |

## Proposed replacement process

### 1. Define the forecast contract before research

Freeze:

- event and competition/ruleset;
- market and settlement convention;
- requested mode: research-only or price-enabled;
- forecast mode: projected-lineup pregame, confirmed-lineup pregame, or live at an exact state;
- candidate universe and selection mode;
- primary user question and secondary outputs;
- cutoff time.

If the event, market or settlement convention is ambiguous, abstain until resolved. Do not turn a bad or impossible user line into an easy “lock” and count it as skill.

### 2. Create an immutable source/data snapshot

Acquire official state first, then model features. Each value carries source, known/published/fetched timestamps, transformation version and quality status. Save the feature vector and hash it. Later updates create a new prediction ID; they never overwrite the old one.

Hard failures:

- event/ruleset mismatch;
- post-cutoff fact in a pregame feature;
- missing target/settlement definition;
- source date mismatch;
- model used outside its intended league/market/mode;
- live state without clock/exposure needed by the model.

### 3. Use a registered sport/market model

Every production model card records:

- target and settlement;
- league/season population;
- feature list and availability time;
- training/calibration/test windows;
- baseline and challenger;
- hyperparameter selection method;
- probability-calibration method;
- drift/retrain triggers;
- known exclusions;
- last out-of-sample results.

If no registered model exists, report `MODEL UNAVAILABLE` and a non-probabilistic research summary. This is more honest than fabricated precision.

### 4. Validate strictly out of sample

- Use expanding/walk-forward splits.
- Tune model/decay/dispersion only within training folds.
- Fit probability calibration on a later calibration window.
- Evaluate once on an untouched test window.
- Cluster/bootstrap by event, not option row.
- Compare against naive league/team baselines and, where authorized, no-vig market probability.
- Report Brier, log loss, calibration intercept/slope, reliability diagram, MAE/interval coverage for numeric targets, and selection coverage/abstention rate.
- Require confidence intervals; do not promote a model on a handful of wins.

### 5. Produce probability with full uncertainty

The output must distinguish:

- point estimate;
- aleatoric/outcome interval;
- parameter uncertainty;
- lineup/weather/pitch scenario uncertainty;
- model-disagreement range.

Round probabilities to a precision supported by calibration. Hundredths of a percent from Monte Carlo are prohibited unless total forecast uncertainty is genuinely that small, which it will almost never be in sports.

### 6. Make the decision appropriate to mode

**Research-only:** rank by calibrated probability only if the user explicitly asks; otherwise present the distribution and uncertainty. No “micro-stake,” “value,” “lock” or bankroll language.

**Price-enabled:** calculate no-vig market probability, break-even probability, EV and an EV interval. A higher-probability outcome may rank below a lower-probability outcome on value. PASS when the conservative EV is not positive after model-risk margin.

Correlated alternatives are not a parlay recommendation. Report event-level joint/correlation risk where multiple positions are discussed.

### 7. Settle without rewriting history

Settlement appends:

- official result and source;
- W/L/P/Void;
- proper-score contribution;
- numeric forecast error and interval inclusion;
- CLV/P&L only if a real execution record exists;
- predefined error taxonomy.

Do not add an active rule from one miss. File a hypothesis for the scheduled review.

### 8. Review on a fixed cadence

Monthly or after a prespecified minimum effective N:

- calibration by sport/league/market/mode/model version;
- drift and missingness;
- baseline comparison;
- candidate hypotheses tested only on subsequent events;
- promotion/retirement decisions with version change.

## Proposed document and data architecture

Replace the single ever-growing active instruction file with:

1. `SPORTS_OPERATING_STANDARD.md` — short universal hard gates, modes, cutoff rules, output schema, abstention and settlement.
2. `MODEL_REGISTRY/` — one versioned model card per sport/league/market family.
3. `SOURCE_REGISTRY/` — fact-specific source priority, parser tests, latency and known failure states.
4. `PREDICTIONS.csv` or database table — immutable forecast snapshots.
5. `SETTLEMENTS.csv` — append-only outcomes linked by prediction ID.
6. `EXECUTIONS.csv` — optional and separate; only real odds, stakes, timestamps, commission, CLV and P&L.
7. `CALIBRATION_REPORT.md` — generated metrics and confidence intervals, never hand-maintained approximate counts.
8. `RESEARCH_HYPOTHESES.md` — postmortem ideas awaiting prospective validation.
9. `HISTORICAL_LESSONS_ARCHIVE.md` — current narrative history, explicitly non-operative unless promoted through testing.

The current combined document remains valuable as an archive of failure mechanisms and source lessons, but it should not remain the executable forecasting algorithm.

## Immediate remediation order

1. **Stop publishing the adjusted penalty record and 4-0 card score as accuracy.** Re-label old figures as custom historical scoring only.
2. **Remove all staking language immediately** unless a price-enabled execution request supplies executable odds and bankroll/risk context.
3. **Freeze current heuristic version.** No new one-result rules while the audit migration is underway.
4. **Build immutable prediction and settlement schemas.** Add forecast mode, cutoff/source times, candidate universe, model/data versions and hash.
5. **Quarantine unauditable historical rows.** Rows with mixed pregame/live/settlement text or uncertain cutoff remain qualitative only.
6. **Recompute calibration from eligible frozen rows, clustered by event.** Separate user-provided, fixed-universe and model-selected markets; separate pregame and live.
7. **Canonicalize sport/league/market labels.** Merge aliases only after preserving original values.
8. **Remove arbitrary percentage weights and narrative probability haircuts.** Replace with fitted model coefficients or `MODEL UNAVAILABLE`.
9. **Make external models and markets explicit benchmarks/features.** Never use one to set parameters and then claim it independently validates the result.
10. **Pilot one sport/market at a time.** Recommended order by data quality: MLB full-game/F5 totals; NBA/WNBA phase/full totals; soccer regulation goals; then AFL and cricket state models. Do not claim “all sports” readiness.
11. **Require an untouched prospective test period before reactivation.** No production confidence/staking until calibration and baseline improvement are demonstrated with uncertainty bounds.

## Acceptance tests for the rebuilt system

A sport/market model is not active until all are true:

- Every published probability is exactly reproducible from a frozen snapshot and model version.
- Pregame and live forecasts are stored and scored separately.
- Candidate selection is predeclared or fully logged.
- No test event was used to create rules, tune parameters or calibrate probabilities.
- Brier/log loss and calibration are reported with event-clustered uncertainty.
- The model beats its declared naive baseline on an untouched test window; if price-enabled, it is also compared with no-vig market probability and CLV.
- Parameter/input/model uncertainty is materially larger than reported Monte Carlo error and is shown.
- Whole-line push/void and competition settlement branches are explicit.
- Sport/league/ruleset scope is exact; unsupported sports return `MODEL UNAVAILABLE`.
- Staking is absent by default and cannot appear without price, authorization and risk constraints.

## Final audit conclusion

The current documents contain a substantial amount of useful sport knowledge, source discipline and settlement hygiene. The Poisson framework also states many statistically correct cautions. The unacceptable error rate persists because those strengths sit on top of an invalid evaluation economy and a largely heuristic probability engine.

The honest repair is not another layer of gates or another list of match-specific lessons. It is to replace the custom top/bottom score with immutable forecasts, proper scoring, predeclared selection, mode separation, fitted sport-native models, full uncertainty, and price-aware EV only when explicitly authorized. Until that replacement passes prospective tests, the system should describe itself as research support—not a calibrated all-sports prediction or staking system.
