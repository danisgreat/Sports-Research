# Cricket analysis rules

Status: **ACTIVE**
Effective: **2026-08-30**
Applies with RULES_GENERAL.md, MODEL_AND_DATA_SPEC.md, ALGORITHM_PORTFOLIO_AND_EVALUATION.md, and NUMERICAL_TRAINING_SPEC.md.
Numerical training specification: **NTS-2026.08.25-v0.2 — all-sports design only; no cricket model is fit**

## 1. Identity and contract

Resolve format and competition: Test, ODI, T20, The Hundred, domestic format, international, warm-up, or exhibition. Record innings, batting team, target/chase state, scheduled balls/overs, legal-ball definition, powerplay/field restrictions, DLS/shortening terms, winner/tie/super-over rules, and exact player/team metric.

Never assume that a broadcaster label uses the same boundary as the user's contract. Official current-season playing conditions control.

### Underlying cricket target hard gate

Freeze one exact target before modelling or mapping a line:

| Target ID family | Outcome and endpoint |
|---|---|
| `TEST_DAY_RUNS_FULL` | All runs by both teams during a named Test day, through stumps or earlier match completion |
| `TEST_DAY_RUNS_REMAINING` | Additional runs after a timestamped live state until that named day ends |
| `TEAM_FIRST_INNINGS_TOTAL` | Named team's completed first-innings total, even if it continues on another day |
| `TEAM_INNINGS_RUNS_REMAINING` | Additional runs from a frozen innings state to all-out, declaration, chase/forfeit or contract endpoint |
| `SESSION_RUNS` | Runs inside an officially defined session boundary |
| `MATCH_RESULT` | Governing result state, including draw/tie/abandonment rules |

These are not aliases. A day total may cross innings and batting-team boundaries; an innings total stops at that innings endpoint. Pregame, end-of-day and live versions have distinct target/horizon/model IDs.

## 2. Toss-window pitch and conditions hard gate

For every cricket card, search the exact match at toss time and immediately before delivery where practical.

Store two independent statuses:

- **STRIP STATUS:** OBSERVED / NOT FOUND AFTER SEARCH / CONFLICTING;
- **MATCH CONDITIONS STATUS:** OBSERVED / NOT AVAILABLE / CONFLICTING.

Search official toss/live commentary, match centre, broadcast/live blog, ground or curator report, and reputable exact-match reporting for strip/surface language. Separately obtain venue-local match-window weather/conditions. Seek two independent match-specific sources when available, but two weather pages are not two independent pitch signals.

Weather or an automated conditions field cannot imply unreported grass, hardness, pace, seam, turn, or deterioration. If no strip report exists after the search, continue with a disclosed evidence limit and forced/low-confidence ranking; never invent the strip.

## 3. High-value inputs

- Confirm toss, innings order, full XIs, batting order/roles, wicketkeeper, bowling resources, substitutes, and material availability.
- Estimate balls faced, batting position, bowling phase/overs, wicket-taking resources, and likely death roles.
- Use opponent-adjusted scoring and dismissal rates by phase and matchup.
- Build a format/competition/season/venue baseline with innings order, contest strength, boundary dimensions, and rules era.
- Record match-window weather, dew only when observed/forecast and mechanistically relevant, interruptions, and DLS risk.
- Use direct H2H only with meaningful XI/role/format continuity.

## 4. Model

The active MDS v2.7 method remains a qualitative rate × exposure corridor. The following numerical models are **training candidates only** under NTS-2026.08.25-v0.2. H0 is not built; none is fit, calibrated, validated, champion, or authorised to publish a probability.

### 4.1 Candidate probability-model ladder

| Candidate | Cricket role | Required caution |
|---|---|---|
| Conditional empirical CDF | Transparent target/state baseline | Sparse states require chronological hierarchical pooling |
| Poisson regression | Equidispersion diagnostic only | Cricket totals may be overdispersed; convenience is not model fit |
| Hierarchical negative-binomial distributional regression | Primary simple count challenger for integer run targets | One component may miss declaration/weather/innings-switch multimodality |
| GAMLSS-style or other hierarchical location/scale/shape regression | Interpretable flexible distribution challenger | Family, link, support, skew and tail behavior require held-out selection |
| Truncated/discretised Normal or Student-t | Direct day/innings-total benchmark | Untreated negative/fractional mass is invalid; symmetry may be wrong |
| Joint non-crossing quantile model | Flexible-shape challenger | Independently estimated quantiles can cross; interpolation and tails must be frozen |
| Ordered bucket/cumulative-link CDF | Discrete monotone challenger | Bucket and tail resolution must be selected before TEST |
| NGBoost/distributional boosting | Nonlinear conditional-distribution challenger | The chosen family can still have wrong support or tails |
| Bayesian hierarchical state simulator | Preferred structural A2 challenger | Highest data/transition/validation burden; not promoted by architecture alone |

Mean and standard deviation are sufficient only when they identify a tested predictive family with valid support and calibrated tails. For Test cricket, a stored PMF/CDF or posterior predictive trajectory sample is preferred because playable time, declaration, innings changes, collapse and early completion can create skewed or multimodal outcomes.

Zero-inflated/hurdle families are not automatic defaults. A no-play day is an exposure/weather scenario with its own label/void rule, not generic evidence that normal cricket scoring follows a zero-inflated count process.

### 4.2 Test cricket structural A2 candidate

Exposure units are sessions, scheduled and playable time, legal balls/overs, wickets, crease time, batter/bowler resources, ball age/new-ball cycles and innings state.

At the frozen start state, record only prediction-time-known fields:

- innings, batting side, score, wickets, lead/trail, day/session and target endpoint;
- striker/non-striker, current scores/balls, batting order and replacement queue;
- current/available bowlers, spell/workload, attack composition, ball age and new-ball eligibility;
- expected playable overs/time with weather, light, delay and over-rate scenario uncertainty;
- venue/era, exact-match strip evidence, dynamic team/player strengths and matchup;
- declaration, follow-on, chase, match-completion and draw/win incentives.

The engine then:

1. samples playable exposure and other discrete scenarios using only cutoff-safe information;
2. estimates a coupled transition such as `P(runs, wicket, extras | state)`, or another factorisation that preserves run/wicket dependence;
3. updates score, wickets, participants, bowling state, ball age, clock/session, innings and lead/trail;
4. applies explicit hazards for dismissal, all-out, declaration, innings change, chase/match completion, stumps, weather/bad-light interruption and abandonment/void treatment;
5. simulates to the exact target endpoint across scenario and parameter uncertainty;
6. stores one predictive distribution from which every contract is derived.

Runs and wickets may not be modelled as unrelated totals. A wicket changes subsequent rate, batter exposure, collapse risk, innings termination and possible transition to the next innings. A survival/hazard or competing-event component can model part of this process, but it is not a complete run-total distribution.

For `TEST_DAY_RUNS_FULL`, continue across any innings/team transitions until the day endpoint. For `TEAM_FIRST_INNINGS_TOTAL`, stop at that innings endpoint even if it occurs on a later day.

### 4.3 Limited-overs structural candidate

Exposure units are legal balls, wickets, batting position, batter/bowler resources, scheduled balls/overs and opening/powerplay, middle and death phases. Estimate a ball/over transition such as `P(runs, wicket, extras | state)`, conditioned on target, required rate, current resources, matchup, venue/conditions and phase. Wickets change both rate and remaining ceiling. A chase is capped by the target and may end early; DLS/shortening is a distinct rules/state branch.

Limited-overs and Test engines do not share fitted distributions merely because both use runs and wickets.

### 4.4 One CDF for every line

For integer target `Y` with `F(k)=P(Y<=k)`:

- `P(O185.5) = P(Y>=186) = 1-F(185)`;
- `P(O235.5) = P(Y>=236) = 1-F(235)`;
- `P(U235.5) = P(Y<=235) = F(235)`;
- `P(U285.5) = P(Y<=285) = F(285)`.

Therefore `O235.5` and `U235.5` are exact complements. `O185.5` and `U285.5` overlap and both win for `186<=Y<=285`; their joint probability is `F(285)-F(185)`, not the product of their marginals. Ask for every real line and its same-time price, but train the one target distribution. Without odds, rank likelihood only; do not claim value.

### 4.5 Training and evaluation

Use match/series-grouped chronological `TRAIN -> TUNE -> CAL -> untouched TEST`, followed by immutable E1-P shadow output. Random delivery-row splits, later lineups, realised weather, post-state declarations and closing prices fail the point-in-time gate.

Primary metrics are CRPS/ranked probability score and log score for the full distribution; randomized PIT/discrete-rank calibration; 50/80/90% interval coverage and width; and threshold Brier/log score/reliability at frozen lines. MAE/RMSE/bias are secondary point diagnostics. Required slices include target, pregame/live horizon, day/session/innings, venue/region, team/participant support, weather/exposure, declaration/innings-switch and OOD state.

Calibrate the whole CDF or a shared monotone transformation. Separate threshold calibrators that can reverse nested-line ordering are prohibited as the production output.

## 5. Structural controls

1. **Exact-ball contracts use legal deliveries.** Reconstruct from official delivery data when no phase row exists, reconciling extras and legality.
2. **Phase does not equal innings.** A fast or slow first phase cannot determine the full total.
3. **Wicket-cluster floor.** Map which bowlers and phases can create early/middle/death collapse, including support bowlers.
4. **Finisher ceiling.** Upper Unders require a separate last-phase branch using likely batters, wickets remaining, boundary access, and death bowling.
5. **Toss is context, not direction.** Bowl-first does not automatically support an Under or winner.
6. **Winner independence.** If a selected side is projected to post a low target, model whether that target is defendable against the confirmed chase.
7. **Venue samples are adjusted.** Do not mix formats, eras, innings order, or target-censored chases.
8. **Direct ceiling conflict.** A same-season comparable high innings cannot be dismissed by a venue median without current XI/bowling/strip evidence.
9. **Rain/dew are conditional.** DLS, interruptions, wet ball, skid, swing, spin grip, and chase incentives can have different signs.
10. **Player milestones are boundary-sensitive.** Model crease time and dismissal risk, not reputation alone.
11. **Target identity precedes the line.** Day runs, remaining-day runs and innings totals cannot share a label or be substituted after seeing the result.
12. **One CDF controls nested totals.** Over probability decreases as the line rises; Under probability increases. A violation is a failed model record.
13. **Exposure is stochastic.** Weather, light, over rate, early match completion and declarations change playable opportunities; they are scenario branches, not fixed afterthoughts.
14. **Calibration preserves geometry.** Do not calibrate each line independently and then publish crossed probabilities.
15. **Incomplete is not zero.** Abandoned, void, censored or not-yet-completed innings/days follow the frozen target/label policy and are never silently recorded as ordinary zero-run outcomes.
16. **Phase-to-innings transition is joint.** Link a powerplay/first-five/first-six target to the innings only through the phase-end state distribution—runs, wickets, batters/resources, bowling allocation and conditions. Phase runs alone cannot project the completed innings. A correct phase direction does not validate the innings direction, or vice versa.
17. **Sparse or inaugural competitions require hierarchical shrinkage.** One venue innings, one prior match or a short direct series cannot own the baseline. Separate competition, venue, team/player and broader format priors; disclose their compatibility and weight, then condition on verified toss/XI/strip. If toss/XI or start state is unresolved, lower evidence quality rather than using weather or one low total as a deterministic Under.
18. **Test rearguards are survival processes.** A large lead and wickets required are not sufficient for a win lean. Model remaining playable balls, current batters, partnership/farming ability, new-ball cycles, bowler workload, dismissal hazards, weather/light and follow-on fatigue. Repeated same-match tail resistance is current evidence, not merely a season-average outlier.
19. **Retained resources can reverse phase direction.** At every limited-overs phase boundary, condition the next rate on runs, wickets, batter identities/roles, boundary access, bowling overs remaining, target/required rate and conditions. A slow powerplay with wickets/resources intact can accelerate above the innings line; a fast powerplay with depleted batting resources can finish below it. Rank phase and innings contracts on their own conditional distributions.

## 6. Live state

Store target ID/version, cutoff and endpoint; innings, score, legal balls/overs, wickets, striker/non-striker, current bowler, ball age/new-ball state, target/required rate, powerplay/field state, session/time remaining, interruptions/DLS par where official, weather/light observation and resources remaining. Rebuild future phases from current batters, wickets, bowlers, playable exposure and termination branches; never extrapolate run rate alone. A live row uses a distinct remaining-output target/model ID rather than reusing the pregame distribution.

## 7. Sources and settlement

- ICC/ECB/national-board playing conditions control rules.
- Official competition scorecards and delivery feeds control state, exact balls, result, and statistics.
- Government weather services and official venue reporting control conditions.
- Reputable match specialists may supply exact-match strip reports after date/event verification.

For DLS, use the official revised target/result; do not reverse-engineer proprietary resource tables. Settle exact phases from official phase data or a legality-reconciled delivery reconstruction.

## 8. Numerical research basis

- [Cricsheet official JSON format](https://cricsheet.org/format/json/) — candidate versioned event-data format; source approval remains pending in DATA_SOURCE_REGISTER.md
- [A simulator for Twenty20 cricket — Davis, Perera and Swartz](https://doi.org/10.1111/anzs.12109) — limited-overs component precedent, not an active Test model
- [Modelling and simulation for one-day cricket — Swartz, Gill and Muthukumarana](https://doi.org/10.1002/cjs.10017) — ODI simulation precedent only
- [Bayesian survival analysis of batsmen in Test cricket — Stevenson and Brewer](https://doi.org/10.1515/jqas-2016-0090) — dismissal-hazard and hierarchical evidence, not a complete team-total model
- [On the distribution of runs scored and batting strategy in Test cricket — Scarf, Shi and Akhtar](https://doi.org/10.1111/j.1467-985X.2010.00672.x) — evidence to test count-family candidates, not proof of transfer to this target
- [NGBoost — Duan et al.](https://proceedings.mlr.press/v119/duan20a.html) and [noncrossing quantile regression — Bondell, Reich and Wang](https://doi.org/10.1093/biomet/asq048) — general distributional challengers

These sources justify candidate components and safeguards only. Model family selection and any probability claim require the local H0, chronological and prospective gates.

## 9. Upcoming-game research sequence

1. Freeze format, rules, scheduled day/innings/phase, target endpoint, toss state, DLS/shortening terms and every line before analysis.
2. Retrieve official event/state, squad/XI/toss and rules first; exact-match strip evidence and government match-window weather/light next; historical ball/innings process and comparable venue/format evidence after volatile facts.
3. Build separate playable-exposure, run-rate, dismissal/wicket-resource, batting-order/bowling-resource and termination branches. For Tests include innings changes, declaration/follow-on/chase/match-completion; for limited overs include target pressure, phase/death resources and DLS.
4. Refresh state, XI/toss, weather/radar and surface reporting immediately before issue. A scheduled start crossing creates a new live target and remaining-exposure view.
5. Derive every total/milestone from the exact target corridor/CDF. Match winner/draw comes from the full match-resource process, not mechanically from an innings-total lean.

Source examples in DATA_SOURCE_REGISTER.md are candidates by function. Do not make one scorecard, query site or archive a permanent mandatory source, and do not retain its data for H0 until approved.
