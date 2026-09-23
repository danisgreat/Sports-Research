# Model and data specification
> **Current revision — CR-2026.09.21-3:** METHOD **MDS-2026.09.19-v4.3** is the workflow/template authority; **SCORING_AND_VALIDATION.md** controls conditioning, exact scoring, event-level evaluation and prospective evidence. All existing logs remain LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE. NUMERICAL_PROGRAM controls authorized implementation scope and actual build state; MODEL_IMPLEMENTATION_RECIPES contains the executable Markdown reference. Older dated policy blocks are historical where inconsistent. No source, dataset or model is approved/fitted by this banner.




> **`METHOD.md` is now the primary mandatory read (v4.0 comprehensive overhaul, 2026-09-06).** §§3–8 of this document (pipeline, data priority, provenance/missingness) remain the detailed reference; `METHOD.md` §3 restates the pipeline once at the operational level.


Status: **ACTIVE — DETAILED REFERENCE**
Method version: **MDS-2026.09.19-v4.3 / CR-2026.09.21-3**
Effective: **2026-09-06 (v4.0 comprehensive overhaul — see METHOD.md and FRAMEWORK_AND_GAME_LOG_OVERHAUL_REVIEW_2026-09-06.md)**
Numerical training specification: **NTS-2026.09.19-v0.5 — Stage 0 all-sports design/pre-fit**


This document defines the common forecasting, data, validation, and record design for every sport. NUMERICAL_TRAINING_SPEC.md defines the distribution-first training program; DATA_SOURCE_REGISTER.md, H0_DATASET_CARD.md, and NUMERICAL_MODEL_REGISTER.md hold its current source, dataset, and model state. ALGORITHM_PORTFOLIO_AND_EVALUATION.md defines the numerical challengers and acceptance protocol. No single universal statistical model is presumed best across sports; the governing design is one reproducible process with sport-specific rate and exposure models.


## 1. Objective and intended use


The system has two required outputs and one optional output:


1. a forecast of the event and each supplied contract; and
2. an ordinal ranking of the supplied contracts.
3. only on explicit request, an unordered top-two coverage portfolio that remains separate from the ordinal ranks.


Rank by marginal estimated chance and robustness of settling as a win under the exact contract using only sport, participant, venue and environment evidence. The active forecast is always `SPORTS_ONLY / MARKET_BLIND`; prices, implied probabilities, bookmaker/affiliate analysis, consensus and line movement do not enter it or check it. Lower loss probability and evidence quality are audit fields; dependence does not turn the ordinal ranking into a hedge. This is **not** an expected-value, staking, profitability, or diversification ranking. An explicitly requested post-freeze price audit is separate and cannot alter the forecast.


The framework is for research support. It cannot guarantee a result, and its current historical log does not establish a market edge.


The primary numerical object is the predictive distribution of an exactly defined underlying target. A bookmaker line is a deterministic query of that distribution, not the base training target. Named-day runs and a team's completed innings total, for example, require different target IDs even when both are discussed during the same match.


## 2. Historical development set D0 and evidence boundary


All canonical records P-001–P-060 are frozen as **Historical Development Set D0**. D0 contains 59 forecast events plus P-021, which closed without a forecast. It includes user-selected contracts, several live or revised views, dependent rows from the same event, changing schemas, no consistently captured prices, and no consistently issued probabilities.


D0 is a legitimate training set for **process and representation learning**: it may be used to design fields, identify recurring error mechanisms, build scenario and failure-path libraries, define sport-specific inputs, improve source checks, and retrieve comparable prior cases. It is **not** a valid numerical parameter-training, calibration, validation, accuracy, or profitability set.


| D0 use | Allowed treatment |
|---|---|
| Data/schema training | Define identity, state, exposure, rate, context, dependence, provenance, settlement, and retrospective fields |
| Mechanism training | Convert recurring misses and misleading wins into causal checks, tail branches, and candidate features |
| Case retrieval | Retrieve mechanism-matched prior cases to challenge a new forecast and expose missing branches |
| Process-rule promotion | Activate integrity, coherence, source, leakage, and record controls that do not claim predictive lift |
| Forecast-weight or probability fitting | **PROHIBITED** from D0 outcomes |
| Historical ranking performance | Original user-confirmed pre-game ranks may be scored by their issued method; include process mistakes and disclose live/partial exclusions |
| Calibration, validation of a later method, edge, or profit claims | Not established by these historical qualitative cards |


Special roles remain explicit: P-021 contributes administration/state logic only; the unsettleable P-003 corner row contributes source and settlement lessons only; P-057 is explicitly live-issued and remains outside pre-game performance, with its live research outcome retained. Multiple views or contracts from one event are not independent training examples.


Consequences:


- use every D0 case in the retrospective mechanism index, including wins that succeeded for the wrong reason and losses that followed a reasonable tail;
- do not estimate feature coefficients, probability calibration, or raw analogue win rates from the D0 outcomes;
- do not backfill D0 probabilities, prices, closing-line value, or prediction-time features;
- do not call the historical directional hit rate model accuracy;
- mark every historical qualitative view **PROBABILITY NOT ISSUED — NOT PROPER-SCORE ELIGIBLE**;
- treat retrospective feature importance as a hypothesis until it improves a chronological out-of-sample forecast;
- retain D0’s development role, but permit original non-live cards from P-001 onward in historical qualitative performance by their issued method, using the user-confirmed freeze basis. P-061 onward may be classified E1-Q / USER_CONFIRMED_PREGAME_FREEZE; prior local-import exclusions are superseded. Explicit live views remain separate. None becomes a later model’s untouched test set;
- start a distinct **E1-P** probabilistic shadow cohort only when a numerical model actually generates immutable pre-result outputs.


A separate **H0 source-derived historical feature store** may later support numerical training, but only when each feature has demonstrable prediction-time provenance. Reconstructing H0 does not edit or numerically fit D0. H0, E1-Q, E1-P, and rolling TRAIN/TUNE/CAL/TEST roles follow ALGORITHM_PORTFOLIO_AND_EVALUATION.md §3.


## 3. Canonical forecasting pipeline


Every forecast follows this order. The executable form of these ten stages, with named gates and evidence ceilings, is `GFA-2` in RULES_GENERAL.md §11; each sport file’s `SFA-<SPORT>` section supplies the sport-native content. This section defines what each stage must contain; `GFA-2` defines the order in which the stages run and the output when one fails.


1. **Canonicalise the decision set, event, target, and contracts.** Freeze the user-supplied candidate slate, eligibility/exclusion reasons, IDs, sport, competition, rules era, official event ID, participants, venue, scheduled start, state, the underlying target ID/definition/unit/start state/endpoint/exposure/termination, phase, exact lines, metrics, overtime/extra-time treatment, push intervals, and operator assumptions.
2. **Freeze the information set.** Separately store request, effective, first-known/published, observed, accessed, cutoff, and issue times plus method/source/definition versions. No later information may enter this view.
3. **Build the baseline and retrieve prior mechanisms.** Route each required field through DATA_SOURCE_REGISTER.md and acquire volatile facts before history. Start with a competition-, season-, rules-era-, venue-, and home/away-appropriate prior. Under a predeclared query, retrieve up to five genuinely comparable D0 cases; zero is valid and recorded as `NO COMPARABLE CASE`. Record similarities and regime differences. Use cases to expose missing branches, never as a raw win-rate prior. Never begin with a streak or one recent result.
4. **Estimate dynamic strength.** Use opponent-adjusted process data with time decay and explicit regime breaks for coach, role, lineup, rules, venue, injury, or season changes. Sparse estimates shrink toward an appropriate league, team, role, or position prior. New or weakly observed regimes widen uncertainty before shifting the centre unless a current directional mechanism is identified.
5. **Model participant exposure.** Estimate who will play, in which phase or score state, and how much: minutes, possessions, drives, plate appearances, innings, balls, overs, wickets, time on ground, centre-bounce attendance, sets, or attacking sequences. Store replacement and late-change branches. Availability without target-phase eligibility is not exposure.
6. **Apply matchup interactions.** Use current participants and roles. Direct history is secondary unless lineup, role, rules, and tactical continuity are meaningful.
7. **Complete environment admission, then apply context conditionally.** Every outdoor/open-roof event needs a qualified venue-coordinate forecast through the plausible endpoint plus a near-start observation/radar and a separately sourced current field/pitch/surface state. No forecast means no actionable forecast; missing current condition is explicit and receives the sport-specific ceiling. Rest, workload, travel, environment, officials, motivation, and comments change a forecast only through a stated exposure, rate, tactical or variance mechanism.
8. **Form one joint outcome distribution.** Model the native scoring/resource process and its lower and upper tails. Winner, margin, total, phase, team, and player contracts must be derived from the same coherent event distribution. For two-sided score events, retain low/close, low/separation, high/close and high/separation families before querying any side or total. If no validated numeric distribution exists, use a transparent central corridor plus explicit scenario branches and label it qualitative.
9. **Map and rank contracts.** Draw each settlement interval, deduplicate aliases, tag dependence, calculate win/push/loss only when a genuine numerical model exists, and rank all supplied unresolved rows by marginal win likelihood. Run a mechanism-to-contract check: identify the state that makes Rank #1 win and confirm that the evidence supports every extra condition the exact contract requires. For derivative/niche markets, require the target-event exposure/rate/opponent/context chain and exact settlement definition before `LEAN`/`SUPPORTED`; otherwise cap at `FORCED RANK` and LOW/MEDIUM-LOW evidence. An optional portfolio never silently changes these ranks.
10. **Challenge, freeze, and issue.** Compare the leading mechanism with its strongest ordinary kill path, run source/geometry/leakage checks, refresh volatile facts, freeze the information cutoff and any genuine shadow output, append the view, then deliver only information that has passed its publication gate. Research stops when material fields are resolved or explicitly missing/conflicting and another source is unlikely to change the decision before the refresh deadline.


### Target registry and contract separation


Before H0 construction or a numerical fit, register:


| Field | Requirement |
|---|---|
| Target identity | Stable ID/version, sport/population and exact outcome |
| Support and unit | Integer/continuous/discrete outcome and feasible bounds |
| Forecast mode | Pregame, named checkpoint or exact live state |
| Start and endpoint | Information boundary and target termination |
| Exposure | Scheduled and uncertain opportunities/time/resources |
| Censoring/void | Abandonment, early completion, declaration, shortening, push and exclusion rules |
| Label | Official source/version and correction policy |
| Derived contracts | Exact W/P/L integration rules and provider assumptions |


Store one underlying target/state/model row and link any number of derived contract rows to it. Multiple thresholds do not multiply the target row's training weight. H0_DATASET_CARD.md preregisters target families and design-only builds for every dedicated sport.


### Cross-sport target families


The shared schema does not imply one pooled cross-sport model. Each exact target belongs to one of these linked but separately validated families:


| Family | Numerical object | Typical derived contracts | Separation rule |
|---|---|---|---|
| Paired score/resource | Joint `P(X,Y given state)` or posterior sample | Winner, total, margin, handicap, team totals | Regulation, overtime/extra innings/golden point, shortening and home-last-exposure terms are target-specific |
| Multi-outcome result | Probability vector over home/draw/away, win/draw/loss, or match-state outcomes | Moneyline, draw-no-bet, double chance, qualify/advance | May be derived from the score/resource process only when its endpoint and rules exactly match |
| Phase/segment | Distribution from a frozen phase start to its own endpoint | Quarter, half, period, innings, session, named-day or remaining-segment totals | Never relabel a full-event or elapsed-pregame distribution as a phase/live target |
| Player/event count | Exposure × event-rate distribution linked to team/game state | Points, shots, SOT, strikeouts, runs, rebounds, tackles and similar props | Requires its own label/provider definition; a team-score proxy is insufficient |
| Niche team event | Target-specific count/resource process | Corners, cards, turnovers, scoring shots and other provider statistics | Shares scenarios where justified but cannot borrow probabilities from a different metric |


One event can have several linked targets. “One distribution” means one coherent distribution **per exact target**, with cross-target dependence represented when a joint process genuinely supports it.


## 4. Data priority


Source authority and predictive importance are separate. An official quote is authoritative evidence that the quote occurred, but it may have almost no forecast value.


| Priority | Data family | Default treatment |
|---|---|---|
| A — hard gate | Event identity, contract, rules, official state, information cutoff | Must be correct before analysis |
| A — volatile | Confirmed participants, starting roles, expected exposure, late changes, current live state | Highest predictive weight when relevant |
| B — process | Opponent-adjusted shot/contact quality, territory, pace, possession, pitching/bowling quality, lineup strength, role efficiency | Core rate layer |
| B — environment | Venue, surface, weather, rest, travel, schedule, rules era | Apply through a named mechanism |
| C — adjusted history | Time-decayed recent rows, comparable venue/opponent/role samples, direct history with continuity | Shrink and disclose sample/context |
| D — conditional | Officials, press conferences, motivation, social reporting | Use only when verified and mechanistically relevant |
| E — diagnostic only | Raw W/L, Over/Under or cover streaks; old H2H; generic reputation; selection-slot history | Never controls a rank by itself |


When A/B current-regime evidence conflicts with C/E history, the card must store separate baseline and regime branches, their sample/reliability/mechanism, and the reason for their qualitative mixture. This is a transparency and robustness control, not a permission to declare fresh small samples superior or to backfit weights from the latest result.


### Recency and streaks


Store recent source rows once, normally up to 20 where available. L5/L10/L20 summaries may be reported compactly as diagnostics; they are nested and must not be treated as independent confirmations. Use adaptive windows, time decay, opponent quality, venue, participant overlap, and regime breaks.


Whenever a trend is used directionally, record at least three candidate causes, whether each persists in the current event, and the contrary/regression path. A sequence is not a causal feature merely because it is recent.


### Head-to-head


H2H is conditional evidence. Record it only to the depth supported by the competition's history, then label continuity in lineup, coach, role, venue, format, and rules. Old meetings with little continuity are descriptive only; do not fill an arbitrary H2H denominator.


### Historical case retrieval


Before issuing a forecast, query D0 by **sport/competition → market family → pregame/live state → exposure structure → mechanism**. Predeclare eligibility and similarity ordering, then retrieve up to five genuinely comparable cases. Zero is permitted. Log the query, eligible count, selected IDs, and `NO COMPARABLE CASE` where applicable; never choose cases because they had the desired result.


For each retrieved case, record:


- canonical ID and view;
- why the exposure and mechanism are comparable;
- material differences in participants, role, venue, rules era, state, and information quality;
- the failure branch or process check transferred to the current card;
- whether the old result is outcome variance, process-defective, or inconclusive.


The current event's forecast-time evidence controls the rank. Historical outcomes may widen a scenario corridor or trigger a missing-data check, but they cannot mechanically vote Over/Under, side, winner, or player prop. Retrieval without this similarity-and-difference ledger is not training evidence.


## 5. Provenance and missingness


Every decision-driving datum receives:


| Field | Required content |
|---|---|
| Source ID | Stable ID used by the card |
| Data item and definition | What was measured and in what unit |
| Value | Exact value or categorical state |
| Effective time | When the underlying fact became true |
| First-known/published time | Earliest demonstrable availability to the forecast process |
| State-observed time | Required for live data |
| Access time and feature age | When it was retrieved and age at cutoff |
| Source URL, tier, provider and definition version | Exact source, authority, and semantic version |
| Transformation/feature version | Formula, filter, adjustment, or none |
| Predictive tier | A, B, C, D, or E |
| Missing/conflict note | Explicit code, source conflict count, and explanation |


Allowed missingness codes:


- **NOT_CHECKED** — process failure; cannot be relabelled unavailable;
- **NOT_AVAILABLE** — sought but not published or accessible;
- **NOT_RELEASED** — expected later;
- **NOT_APPLICABLE** — not relevant to this contract;
- **CONFLICTING** — sources disagree;
- **STALE** — older than the required decision window;
- **UNKNOWN_DEFINITION** — metric or operator term is not sufficiently defined.


Facts and transformations form a simple source → transformation → feature → forecast chain. A source can be authoritative yet stale, and a fresh source can be low authority; store both dimensions.


Store artifact path/ID, hash and first observed time separately from forecast cutoff and issuance. Under PERFORMANCE_ELIGIBILITY_POLICY.md, the user’s September 5 confirmation establishes the pre-game freeze basis for existing non-live cards. Their historical rank evaluation is eligible without an earlier local copy. Record USER_CONFIRMED_PREGAME_FREEZE rather than independently timestamp verified; hashes and git timestamps alone do not supply independent timing proof.


For an appendable multi-card file, whole-file creation time is not inherited by sections that may have been added later. Each card requires a section-inclusive hash/append receipt or immutable revision demonstrating that exact content. Without it, the earliest whole artifact containing the section controls provenance. Record both the source artifact hash and any audited/normalised copy hash; normalisation or appended audit text must never be represented as byte-identical to the source.


Source approval and immutable raw-snapshot fields follow DATA_SOURCE_REGISTER.md. Dataset population, grain, label, split and quality state follow H0_DATASET_CARD.md. A candidate source name in a research report is not an approved H0 feature.


`NOT_CHECKED` is a compliance failure and cannot be a predictive feature. Other missingness indicators require prediction-time availability and prospective admission. The H0 dataset card, point-in-time join rules, feature admission card, fold-local transformation rules, and held-out ablation protocol are governed by ALGORITHM_PORTFOLIO_AND_EVALUATION.md §§3–5.


## 6. Sport-specific rate × exposure modules


| Sport | Exposure first | Rate/quality layer | Required tails and regime checks |
|---|---|---|---|
| Baseball | Lineup slot/PA; starter batters faced, pitches and innings; named bullpen chain | K-BB%, contact and barrel quality, handedness, batted-ball shape, defence/catcher, park | Opener/bulk role, pitch cap/efficiency, HR cluster, reliever availability, home ninth, extras |
| Limited-overs cricket | Balls, batting position, legal-ball phase, overs and wickets | Run and dismissal rates by phase, batter-bowler matchup, attack resources | Toss, chase cap, rain/DLS, shortened innings, wicket cluster, death overs |
| Test cricket | Sessions/overs, wickets, crease time | Scoring and dismissal rates by innings and pitch phase | Weather, declarations, follow-on, new ball, pitch deterioration |
| Soccer | Expected minutes, starts, set pieces, penalties, attacking sequences | Dynamic attack/defence, shots and xG, post-shot/keeper quality | Rotation, red card, score state, stoppage time; goals and corners are separate mechanisms |
| Basketball | Minutes, possessions, usage and lineup combinations | Per-possession efficiency, shot quality, turnover and rebound rates | Rotation, rest, foul trouble, blowout, late fouling, overtime |
| AFL/AFLW | Time on ground, role/CBA share, inside-50s, marks inside 50, scoring shots | Territory, pressure, shot location/quality and conversion | Venue, weather, ruck-to-clearance chain, late changes, game-state tempo; AFLW is a separate population |
| Rugby league/NRL | Minutes, interchange, possessions/sets, set starts and field position | Ruck speed, metres, line breaks, tries and goal conversion | Spine/goal-kicker changes, sin-bin, possession imbalance, wet handling/short fields, golden point |
| American football | Drives, plays, starting field position and expected snaps | QB-regime EPA/success, trenches, coverage, explosive plays, red zone | QB/line change, turnovers/non-offensive scores, weather, garbage time, OT and competition rules |
| Ice hockey | Regulation minutes, shifts, shots/chances, manpower states and goalie exposure | Shot quality/xG, finishing, goaltending, special teams and empty-net state | Starting goalie, back-to-back/rest, penalties, score state, pulled goalie, regulation versus OT/SO |


No scoring scale, feature coefficient, or empirical accuracy rate is pooled across unrelated sports. Hierarchical pooling is allowed only inside defensible populations.


### Quantitative skeleton for a future validated model


Within each homogeneous sport/competition/market/state family:


1. Estimate a latent event rate or strength:


   **linear predictor = competition/era baseline + venue/home effect + dynamic team/player strength + participant-exposure adjustment + matchup interaction + contextual adjustment**


2. Apply the sport-appropriate link and distribution to rate × exposure. Team, player, venue and role parameters use hierarchical priors so sparse estimates shrink toward a relevant population rather than a raw tiny-sample average.
3. Represent discrete availability, role, weather, tactical and tail branches as a scenario mixture:


   **event distribution = sum over scenarios of scenario weight × conditional score/resource distribution**


4. Generate the joint home/away, team/player, phase and full-event outcomes. Preserve dependence rather than simulating each contract independently.
5. For each supplied contract, integrate the same event distribution over its win/push/loss intervals and, for quarter lines, its equal-stake adjacent child contracts.
6. Exclude bookmaker/operator odds, implied probabilities, market movement, bookmaker/affiliate analysis and market-derived features from every build and comparison used for active prediction.
7. Freeze priors, decay, scenario definitions, transformations, calibration and ensemble weights for the next chronological evaluation block.


The appropriate link/distribution is sport-specific: overdispersed count or event simulation for baseball/cricket; dynamic bivariate score models for soccer; possession/drive/scoring-shot simulations for basketball, American football and AFL; and set/field-position simulation for rugby league. A simpler model remains champion until the challenger improves prospective proper score and calibration without unacceptable complexity or data fragility.


### Candidate probability-family selection


No family below is an active default. Select it only inside chronological TRAIN/TUNE on a frozen target, then calibrate on CAL and evaluate once on untouched TEST.


| Candidate | Role | Required challenge |
|---|---|---|
| Conditional empirical CDF | Minimal-assumption distribution baseline | Sparse-state pooling, decay, coverage and tail support |
| Poisson | Diagnostic count baseline | Equidispersion versus observed conditional dispersion |
| Negative binomial | Overdispersed count challenger | Dispersion stability, skew/tail fit and scenario multimodality |
| Hierarchical GLM/GAMLSS-style distributional regression | Interpretable location/scale/shape challenger | Family, link, support, pooling and complexity |
| Truncated/discretised Normal or Student-t | Direct-total benchmark | Invalid mass, symmetry, tail fit and conditional scale |
| Joint non-crossing quantiles | Flexible-shape challenger | Crossing, CDF reconstruction, interpolation and tail rules |
| Ordered bucket/cumulative-link model | Monotone discrete CDF challenger | Bin resolution, tail buckets and normalization |
| NGBoost or other distributional boosting | Nonlinear conditional-distribution challenger | Family/support risk, H0 support, OOD and calibration |
| Sport-native generative simulator | Structural joint-distribution challenger | Transition validity, exposure/termination, parameter uncertainty and simulation error |


Hurdle or zero-inflated families require a separately justified structural-zero process. Conformal intervals may challenge interval coverage but marginal coverage alone does not create a conditional CDF or line probability. Exact candidate IDs and current `NOT FIT` state live in NUMERICAL_MODEL_REGISTER.md.


## 7. Joint distribution and dependence


One event produces one forecast object. All contracts are functions of that object.


For an integer target `Y` and `F(k)=P(Y<=k)`, `P(Over k.5)=1-F(k)` and `P(Under k.5)=F(k)`. Integer lines preserve the point mass at the push boundary. This shared CDF is the production source of threshold probabilities; independent binary threshold heads are audit challengers only.


Quarter lines are equal-stake composites of adjacent integer/half lines. Store both child intervals and allow `HALF_WIN`/`HALF_LOSS` at the parent. A forecast objective involving fractional results must be frozen before issue; never score a half result as a full win/loss.


- Exact opposite sides of a half-point line cannot both win.
- Exact opposite sides of an integer line are mutually exclusive wins but can both push at the boundary.
- Alternate or gapped lines can overlap or leave a loss gap.
- Opposite-team positive handicaps can both win on a close result.
- Phase, full-game, team, winner, and player markets may share drivers but are not interchangeable.


Assign every row a dependence group. Only one row per shared thesis can be the primary event-level decision. Other rows remain fully settled but are labelled correlated secondary. A potential-winner field that repeats an existing winner contract is an alias of that contract, not a second forecast observation.


## 8. Bookmaker-independent model and ensemble policy


Every production, shadow and promotion-eligible build declares `SPORTS_ONLY / MARKET_BLIND`. An operator source may define only an exact supplied contract and its action/settlement terms. Odds, implied probabilities, closing lines, line movement, bookmaker previews, affiliate/tipster analysis, consensus and any market-derived feature are excluded from model features, calibration, stacking, selection, scenario weights, ordinal ranking and forecast validation.


If explicitly requested, a price snapshot may be stored after the sports forecast is immutably frozen for a segregated descriptive audit. It cannot be a comparator required for model promotion, cannot revise the forecast, and cannot support a claim of predictive lift. Do not estimate complex ensemble weights from the current log; adopt learned weights only after sports-only chronological out-of-sample evidence passes the active gates.


## 9. Validation and evaluation


### Chronological design


- Use rolling-origin or walk-forward evaluation with disjoint stages: **train → inner chronological tune/early-stop → out-of-fold base predictions → later calibration → untouched test**.
- Fit every imputer, encoder, scaler, target statistic, feature selector, stacker, and calibrator only inside its permitted earlier block.
- Freeze model version, features, transformations, decay rates, candidate policy, relevance mapping, calibration method, and primary/guardrail metrics before each evaluation block.
- Keep a final chronological holdout untouched until the full model specification is frozen. Once viewed, that block is spent.
- Separate pregame and live models, and separate live horizons/state families.
- Keep one event/series group in one block and rebuild dynamic ratings using earlier data only; random delivery-, play-, or candidate-row splits are prohibited.
- All rows and views from one event remain in one fold. Normalize event/decision-set weight so a card with more correlated candidates does not receive more influence.
- Multiple views of one event are not independent. Use the event or a predeclared date/schedule block for uncertainty estimation.
- In the current workflow, log the complete user-supplied candidate slate. Do not call it the full market universe. User-selected cards cannot establish performance on all games or markets.
- For H0/TEST performance, enumerate every eligible event in the preregistered population and freeze any main/alternate-line sampling grid before outcomes. Do not train or evaluate only games or lines selected because they looked interesting.
- E1-Q is qualitative and cannot be reused as same-version E1-P calibration/test evidence after its outcomes informed numerical design.


### Baselines


Every quantitative candidate must beat relevant simple baselines prospectively:


- league/competition base rate;
- home/away or venue-adjusted baseline;
- simple rate × exposure model;
- frozen previous method version.


### Metrics


| Output | Primary evaluation |
|---|---|
| Binary win/loss probability | Brier score and log loss |
| Win/half-win/push/half-loss/loss probability or decomposed children | Multiclass proper score on the frozen representation |
| Score, margin, total, or resource distribution | CRPS plus interval coverage/width |
| Ordered discrete distribution | CRPS/ranked probability score plus randomized PIT or discrete-rank calibration diagnostics |
| Joint multivariate distribution | Dependence-sensitive score when sample size supports it |
| Point/corridor forecast | MAE by native unit; empirical interval coverage and width |
| Ordinal ranking | Rank-1 result, NDCG@2, NDCG@4/full supplied slate, exact-pair ordering |
| Top-two diagnostic | Wins@2, Hit@2, conditional Recall@2, candidate availability and oracle regret; all at decision-set grain |
| Issued/shadow pair probability | Pair Brier for pre-result `P(any win)`; never backfilled |


Calibration and sharpness are reported together. AUC/PR-AUC are secondary. Hit@2 never substitutes for proper scoring and is reported beside Wins@2 and the marginal ranks. A result close to a line is tagged **BOUNDARY_SENSITIVE** for interpretation, but it still contributes fully to a proper score; excluding close results would bias evaluation.


Do not use raw hit rate, profit, or one realised event as proof of calibration. Do not run model-superiority significance tests on the present small, selected sample.


### Calibration and shadow evaluation


Calibrate the final deployed probability output on a later disjoint block, then evaluate it once on untouched data. For nested thresholds, prefer calibration of the full CDF or a shared monotone transformation. Separately calibrated lines can cross and are prohibited as the production output unless they are recombined through a frozen coherence method and the resulting distribution is re-evaluated. Leakage-safe component calibration is permitted, but combining calibrated components does not prove the final blend is calibrated. Logistic/Platt is the first modest-sample binary baseline; temperature scaling is a low-parameter multiclass/logit challenger; beta, isotonic, and Dirichlet-style approaches require separately justified sample support and held-out improvement. Isotonic ties and small-sample overfit must be audited.


Store raw and calibrated W/P/L vectors, fit/evaluation dates, calibrator version, reliability bins with counts and uncertainty, calibration intercept/slope, Brier/log score, and sharpness. A numerical challenger may produce immutable **SHADOW — NOT PUBLISHED** probabilities before the result. A model that did not run records **NOT_GENERATED**; never fill the field retrospectively.


### Monitoring and promotion


Monitor feature/category distributions, missingness, feature age, provider versions, score distributions, reliability, Brier/log loss, interval coverage, rank metrics, top-two redundancy, slice behavior, and operational failures. Thresholds and cadence are frozen before observation. Alerts trigger review, not automatic retraining.


Champion–challenger comparisons use identical snapshots and candidate slates, event/date-block paired uncertainty, a predeclared minimally useful effect and slice non-inferiority rules. Multiple model/feature searches are controlled before the final holdout is opened. Ranker scores are never treated as probabilities.


### Probability publication gate


Numeric probabilities may be published only after the exact target, applicable sport, competition/rules population, market family, and pregame/live horizon—or an explicitly predeclared exchangeable hierarchical population—has passed the H0, coherence, calibration, rolling-origin, proper-score, held-out-slice, untouched-TEST and prospective-shadow gates in NUMERICAL_TRAINING_SPEC.md, with a frozen method version. Sparse slices without defensible pooling remain disabled. Until then publish a qualitative corridor and verdicts only.


## 10. Ranking and actionability


The fields are orthogonal:


| Field | Allowed use |
|---|---|
| Rank | Unique ordinal among supplied unresolved contracts |
| Verdict | SUPPORTED, LEAN, FORCED RANK, or AVOID |
| Evidence quality | HIGH, MEDIUM, LOW, or specified limitation |
| Dependence group | Shared event mechanism |
| Performance role | PRIMARY_FORMAL, CORRELATED_SECONDARY, or INELIGIBLE |
| Actionability | VALUE SUPPORTED, NO VALUE DETERMINABLE, or NOT ACTIONABLE |
| Probability generation | NOT_GENERATED, SHADOW, or GENERATED_VALIDATED |
| Probability publication | NOT PUBLISHED — VALIDATION PENDING, PUBLISHED, or SUPPRESSED |


**AVOID** means the supplied branch is materially opposed by the event evidence. It is not a claim that the available price has negative expected value unless a valid price comparison is recorded.


A required ordinal #1 can still be **FORCED RANK**, low evidence, and **NO VALUE DETERMINABLE**. Ranking does not manufacture a recommendation.


**VALUE SUPPORTED** requires a published calibrated W/P/L distribution, a same-time exact-contract price, a frozen de-vig policy, expected-return calculation including push/refund terms, and an uncertainty margin exceeding a predeclared decision threshold. Qualitative evidence is always **NO VALUE DETERMINABLE**. Value rank and win-likelihood rank remain separate unless the user explicitly requests value ordering.


The ordinary rank table is marginal-likelihood order. Hit@2 and union-win probability do not reorder it. An optional unordered coverage portfolio follows ALGORITHM_PORTFOLIO_AND_EVALUATION.md §9 only on explicit request.


## 11. Canonical Markdown record


### Event manifest


| Field | Value |
|---|---|
| Record / view / method version | |
| Canonical event ID / issued-label alias / storage status | One canonical ID per distinct event; preserve reused/skipped issued labels; mark duplicate text `DUPLICATE_STORAGE` |
| Target ID/version/definition | Exact outcome, unit, start state, endpoint, exposure and termination |
| Dataset cohort / model roles | E1-Q by default; E1-P only for an actually running frozen shadow model |
| Decision-set ID / candidate-policy version | |
| Candidate-universe scope / frozen time / completeness | SUPPLIED SLATE unless a versioned generator exists |
| Retrieved D0 analogues | Query, eligible count, up to five IDs/comparison notes, or NO COMPARABLE CASE |
| Sport / competition / rules era | |
| Official event ID / venue | |
| Scheduled start local / Australia-Sydney | |
| Request / state-checked / cutoff / issue times | `PREGAME` requires cutoff before scheduled start; otherwise verified LIVE, fail-closed or FINAL |
| Champion / challenger / simulator / calibrator IDs | Qualitative champion; NOT_GENERATED where no numerical model ran |
| Phase and verified state | |
| Participants and exposure branches | |
| Bookmaker-independence state | `SPORTS_ONLY / MARKET_BLIND`; operator source only if needed for supplied contract/terms |


### Evidence ledger


| Evidence-unit / lineage ID | Exact source ID / record / URL | Data item / owner | Value/unit | Effective | First known/published | Observed | Accessed / feature age | Source/tier/provider version | Transformation/feature version | Predictive tier | Missingness / full conflict set + impact / commercial-affiliation + market-derived flags |
|---|---|---|---|---|---|---|---|---|---|---|---|


### Candidate slate


Freeze every user-supplied row before ranking. Include malformed and SETTLED_AT_ISSUE rows as excluded, with reasons. Add a potential winner only if it is a distinct contract; otherwise store it as an alias.


| Decision-set ID | Candidate ID | Origin | Canonical contract / alias | Exact geometry | Eligible for rank | Exclusion reason | Dependence/relation | Issuance status |
|---|---|---|---|---|---|---|---|---|


### Scenario and contract map


| Scenario | Evidence-unit IDs | Preconditions | Relative-plausibility basis | Exposure/rate effect | Outcome corridor | Threshold/corridor relation | Same-mechanism adverse sign | Contracts helped | Contracts hurt |
|---|---|---|---|---|---|---|---|---|---|


| Candidate / contract ID | Exact contract and settlement interval | Marginal rank | Verdict | Evidence quality | Dependence group | Performance role | Actionability | Central mechanism | Strongest kill path | Generation / publication state |
|---|---|---:|---|---|---|---|---|---|---|---|


Numerical state is **NOT_GENERATED**, **SHADOW — NOT PUBLISHED**, **PUBLISHED**, or **SUPPRESSED**. Shadow values live in the technical ledger and are not shown as user-facing probabilities. The potential winner cites its canonical contract ID or is explicitly a distinct contract.


When a numerical model genuinely ran, add:


| Candidate/model | Raw P(W/P/L) | Calibrated P(W/P/L) | Ranker score | Uncertainty/OOD | Distribution ref | Calibrator evidence | Shadow/publication state |
|---|---|---|---:|---|---|---|---|


### Settlement


| View/contract | Official final value | Outcome | Margin to line | Official/source-qualified field | Model score | Source status |
|---|---:|---|---:|---|---:|---|


Use only `WIN`, `HALF_WIN`, `PUSH`, `HALF_LOSS`, `LOSS`, `VOID`, `UNRESOLVED`, or `UNSETTLEABLE`. Preserve quarter-line child outcomes. Never convert an avoided loss into a contract win.


For a still-live event, a threshold that is already impossible to reverse may be annotated `MATHEMATICALLY WON/LOST — LIVE`, but that annotation is not the final contract settlement row. Keep the event open until the official endpoint/termination and then append the formal outcome.


### Training label and decision-set evaluation


`settlement_state` preserves full/half/push/loss outcomes or links to separately scored child contracts. VOID, UNSETTLEABLE, and SETTLED_AT_ISSUE are excluded under a frozen policy. An alias shares its canonical label. Any rank relevance mapping for half results must be preregistered; a binary `is_win` field cannot silently collapse fractional settlements.


| Decision set | WinnerAvailable | Rank-1 | Wins@2 | Hit@2 | NDCG@2 / @4 | OracleWins@2 / regret | Pair Brier eligibility | Independent event N |
|---|---:|---:|---:|---:|---|---|---|---:|


### Retrospective driver table


| Preissue expectation | Actual driver | Difference | Knowability | Process grade | Defect class | Lesson/test ID | Method change |
|---|---|---|---|---|---|---|---|


Process grade is **COMPLIANT**, **PROCESS_DEFECT**, or **INCONCLUSIVE**. Defect classes are:


- IDENTITY_CONTRACT
- STATE_FRESHNESS
- TEMPORAL_LEAKAGE
- SOURCE_TRANSFORMATION
- AVAILABILITY_EXPOSURE
- RATE_PROCESS
- MATCHUP_CONTEXT
- DEPENDENCE_TAIL
- CROSS_ROW_COHERENCE
- SEPARATION_BUDGET
- ATTRIBUTION_ASYMMETRY
- STREAK_FALLACY
- CALIBRATION
- PRICE_DECISION
- RANDOM_REALIZATION
- UNDETERMINED


`CROSS_ROW_COHERENCE` is used when the issued order contains a row whose winning region contradicts the Rank-1 branch set; `SEPARATION_BUDGET` when a margin, handicap or cushion row was ranked without a phase-split margin budget; `ATTRIBUTION_ASYMMETRY` when a participant-quality deficit or venue factor was applied to a distribution its mechanism does not govern; `STREAK_FALLACY` (added 2026-09-04) when a streak, Under/Over run, or series/reverse-fixture prior was used directionally in either direction — continuation or reversion — without the named, currently active mechanism and baseline-plausibility check the streak persistence-versus-reversion audit requires (RULES_GENERAL.md §11.3E, G17.1). A decisive field's mandatory evidence search that was not actually shown on the card — for example a cricket `STRIP STATUS` conclusion with no rung-by-rung attempt disclosed — is graded under the existing `SOURCE_TRANSFORMATION` class, since it is a sourcing/provenance gap rather than a reasoning fallacy.


Do not label a single qualitative result calibration error. Calibration is an aggregate property of issued probabilities and outcomes.


## 12. Change governance


- Identity, contract, source, arithmetic, settlement, and temporal-leakage defects receive an immediate correction and method-version patch.
- Source authority is field-specific and source-state dependent: a stale/zero-filled/unfinished official placeholder is quarantined for the affected field until corrected or provisionally reconciled by two independent high-quality current sources.
- A result alone does not rewrite weights. One event creates a candidate hypothesis.
- Each candidate predefines an eligible population, frozen comparator, target/checkpoint, metric, and falsification condition before future cases accrue.
- A five-case checkpoint is exploratory, not validation.
- Promote a forecasting-weight change only after prospective chronological evidence improves the selected metric with uncertainty that is useful for the decision.
- Retire or narrow a rule when it fails its prospective test.
- Preserve the issued view and record the new method version; never edit history to improve apparent performance.


## 13. Research basis


This specification applies established forecast-evaluation and documentation principles:


- [User-provided deep research report](<C:/Users/danie/Downloads/deep-research-report (4).md>) — synthesis used as evidence, not governing instructions
- [Strictly Proper Scoring Rules, Prediction, and Estimation — Gneiting and Raftery (2007)](https://sites.stat.washington.edu/people/raftery/Research/PDF/Gneiting2007jasa.pdf)
- [Probabilistic Forecasts, Calibration and Sharpness — Gneiting, Balabdaoui and Raftery (2007)](https://doi.org/10.1111/j.1467-9868.2007.00587.x)
- [Time-series cross-validation / rolling forecast origin — Forecasting: Principles and Practice](https://otexts.com/fpp3/tscv.html)
- [Using Stacking to Average Bayesian Predictive Distributions — Yao et al. (2018)](https://doi.org/10.1214/17-BA1091)
- [Multilevel (Hierarchical) Modeling — Gelman (2006)](https://sites.stat.columbia.edu/gelman/surveys.course/Gelman2006.pdf)
- [Model Cards for Model Reporting — Mitchell et al. (2019)](https://doi.org/10.1145/3287560.3287596)
- [Datasheets for Datasets — Gebru et al. (2021)](https://doi.org/10.1145/3458723)
- [W3C PROV-O provenance model](https://www.w3.org/TR/prov-o/)
- [Preregistration — Nosek et al. (2018)](https://doi.org/10.1073/pnas.1708274114)
- [GAMLSS — Rigby and Stasinopoulos (2005)](https://doi.org/10.1111/j.1467-9876.2005.00510.x)
- [NGBoost — Duan et al. (2020)](https://proceedings.mlr.press/v119/duan20a.html)
- [Noncrossing quantile regression — Bondell, Reich and Wang (2010)](https://doi.org/10.1093/biomet/asq048)


Sport modules also use official statistical definitions and governing rules cited in each sport file.


## 14. Current model card


| Field | Current state |
|---|---|
| Model/method ID | MDS-2026.09.05-v3.6 / GFA-2 |
| Intended use | Research and ordinal ranking of user-supplied sports contracts |
| Current output | Qualitative event corridor, scenario map, verdicts and unique ranks |
| Numeric probability output | Publication disabled until the §9 gate passes; no numerical model currently exists to generate shadow output |
| Development/training data | D0 = P-001–P-060, used for schema, mechanism, process-control, and case-retrieval training only |
| Numerical parameter-training data | H0 NOT BUILT / NOT QUALITY-APPROVED; none from D0 |
| Prospective qualitative data | Queue IDs and counts are not duplicated here; use the active log named in README and its top controlling snapshot. User-confirmed non-live cards are historically rank-eligible by issued method, including process mistakes; preserve live and unscorable-row exclusions under PERFORMANCE_ELIGIBILITY_POLICY.md |
| Prospective probability data | E1-P NOT STARTED; requires an actually running frozen challenger |
| Algorithm portfolio | A0 qualitative champion; A1–A8 documented, NOT TRAINED / NOT VALIDATED |
| Numerical training program | NTS-2026.09.02-v0.3 Stage 0 all-sports design/pre-fit; source, H0 and model registries exist only as Markdown specifications |
| Validation status | VALIDATION PENDING for every sport/competition/market/state slice |
| Bookmaker-input state | PROHIBITED FROM PREDICTIVE ANALYSIS; operator record limited to supplied contract/terms |
| Profitability status | NOT MEASURABLE from the current no-price/no-stake log |
| Known limitations | User-selected event sample, sparse sport slices, correlated contracts, mixed pregame/live views, changing historical schemas |
| Prohibited uses | Guaranteed-winner claims, staking advice without price/value analysis, historical probability backfill, pooled cross-sport accuracy claims |
| Review trigger | Scheduled prospective checkpoint or immediate identity/source/arithmetic/leakage defect |


## 15. Version history


| Version | Effective | Change |
|---|---|---|
| MDS-2026.08.22-v1 | 2026-08-22 | Introduced the causal pipeline, canonical schema, learning register, and validation gates |
| MDS-2026.08.22-v1.1 | 2026-08-22 | Activated all P-001–P-060 as D0 process-development training; added mechanism-matched historical retrieval; froze P-061 onward under the then-current E1 label |
| MDS-2026.08.22-v2 | 2026-08-22 | Added H0/E1-Q/E1-P roles, candidate/decision-set schema, feature admission, shadow probabilities, algorithm portfolio, disjoint calibration, groupwise metrics, monitoring, value gate, and optional anti-gaming pair portfolio |
| MDS-2026.08.24-v2.1 | 2026-08-24 | Added first-demonstrable-artifact provenance firewall, late-import cohort, exact derivative-provider gate, soccer corner-process completeness and player-SOT exposure decomposition; no numerical weights or probabilities changed |
| MDS-2026.08.26-v2.2 | 2026-08-26 | Added official-or-two-source live-state corroboration, no-action handling for unresolved live state, top-rank derivative-concentration audit, P-085 process-evaluation exclusion and prospective sport-candidate registry; no numerical weights or probabilities changed |
| MDS-2026.08.27-v2.3 | 2026-08-27 | Added final participant event/team/role identity handshake, secondary-only evidence cap, process-defect performance quarantine, baseball small-sample starter mixtures, cricket phase-end resource transitions, soccer aggregate early-goal regimes and sparse-participant side caps; no numerical weights or probabilities changed |
| MDS-2026.08.28-v2.4 | 2026-08-28 | Added explicit baseline-versus-current-regime reconciliation, field-level stale official-placeholder quarantine/fallback, dedicated qualitative tennis rules, and sport-specific sparse-competition, rearguard, mismatch/blowout and current-regime stress branches; no fitted coefficients, numerical probabilities or forecast-weight promotions |
| MDS-2026.08.29-v2.5 | 2026-08-29 | Added two-sided scenario/kill-path completeness, outcome-conditioned-stat quarantine, explicit ranking reconciliation for supported adverse branches, a dedicated qualitative rugby-union/sevens module, and enforcement clarifications for tennis, hockey, basketball, rugby league and soccer; no fitted coefficient, numerical probability or retrospective forecast-weight promotion |
| MDS-2026.08.29-v2.6 | 2026-08-29 | Added canonical alias/duplicate-storage integrity, section-level artifact provenance, whole-event-open handling for mathematically decided live rows, and sport-specific exposure/tail reconciliation for baseball, American football, basketball, soccer and AFLW; no fitted coefficient, numerical probability or retrospective forecast-weight promotion |
| MDS-2026.08.30-v2.7 | 2026-08-30 | Added late-import batch quarantine enforcement, total-volume/team-allocation/winner-margin decomposition, complete phase-end state propagation, participant exposure across starter/replacement phases, and event-versus-termination ordering; amended baseball, cricket, AFL, rugby league, American football, soccer and ice-hockey process controls; no fitted coefficient, numerical probability or retrospective forecast-weight promotion |
| MDS-2026.08.31-v2.8 | 2026-08-31 | Added uncertainty-width-before-centre, exact phase/score-state role eligibility, four-family total/margin stress testing, mechanism-to-contract alignment, official-page state/identity validation and threshold-invariant provider-conflict settlement; amended cricket, AFL, rugby league, American football, baseball, basketball, soccer, ice-hockey and tennis process controls; no fitted coefficient, numerical probability or retrospective forecast-weight promotion |
| MDS-2026.08.31-v2.9 | 2026-08-31 | Added the pregame start-timestamp invariant, threshold-to-corridor and component-budget coherence caps, bidirectional mechanism signs, atomic source/evidence-unit lineage and de-duplication, basketball team-score/terminal-blowout decomposition, and cricket pre-toss innings-order/chase-censoring plus near-start evidence caps; no fitted coefficient, numerical probability or retrospective forecast-weight promotion |
| MDS-2026.09.02-v3.0 | 2026-09-02 | Enforced SPORTS_ONLY/MARKET_BLIND issuance; separated weather from current field/pitch/surface evidence and made the outdoor forecast packet an admission gate; added rule-adoption and participant-release clocks, typed source conflicts, qualified complement invariants and quarter-line half outcomes; superseded retrospective reference-band moves, blanket conjunct penalties and forced extreme-slot reordering; no fitted coefficient, scenario weight, calibrated probability or predictive-lift claim |
| MDS-2026.09.02-v3.1 | 2026-09-02 | Added Rank-1 conditional coherence (G25.1), the phase-split separation budget for margin/handicap/cushion rows (G20.1), participant-deficit attribution with venue-factor restraint (G14.1/§11.3D) and winner/cushion reconciliation (G30.1); realigned all ten `SFA-<SPORT>` sections from the retired `GFA-1` to `GFA-2` and removed their residual reference-band, lexicographic-key and conjunct-penalty language; narrowed L-053 accordingly; no fitted coefficient, scenario weight, calibrated probability or predictive-lift claim |
| MDS-2026.09.04-v3.2 | 2026-09-04 | Added the streak persistence-versus-reversion audit (G17.1/§11.3E) as the symmetric counterpart to the existing trend-mechanism audit (G17); an extension-endpoint own-rate-environment requirement inside G22; and the mandatory series/two-leg state block (§5). Cricket: made the six-rung pitch-report search auditable (a shown attempt-and-result table is now required before `STRIP STATUS: NOT FOUND AFTER SEARCH`), added toss-decision-as-circumstantial-context guidance, and registered two new research lanes (ICC Pitch and Outfield Monitoring ratings; CricViz PitchViz, citation-only). Baseball: extra innings under an automatic-runner-type rule get their own scoring-rate environment; a prior game in the same series requires a named mechanism before it supports a lean. Soccer: a knockout/cup/two-leg fixture's pregame scoring baseline is shrunk toward knockout-fixture history before any goal occurs, distinct from the existing post-goal aggregate-regime-switch control. No fitted coefficient, scenario weight, calibrated probability or predictive-lift claim; corrects a confirmed execution gap (two live cricket cards satisfied the letter of the existing pitch-report gate with no shown search) rather than adding a new evidentiary claim |
| MDS-2026.09.04-v3.3 | 2026-09-04 (same day as v3.2) | Added the method-version-currency requirement inside `G0`/`GATE-READ` (RULES_GENERAL.md §11.1) after P-268/P-270/P-271 were found declaring a method version already one full patch behind what this repository actually contained when they were frozen (LEARNING_REGISTER.md L-065); added a new `STREAK_FALLACY` defect class (§11 below); consolidated the complete settlement protocol into one walkthrough at UPCOMING_GAME_RESEARCH_GUIDE.md §16, restating no new authority; restructured logging into two files — `PREDICTION_LOG_COMBINED.md` closed as historical archive at P-271, `PREDICTION_LOG_COMBINED_2.md` opened as the active canonical log at P-272 (administrative under RULES_GENERAL.md §0, not a method change in itself). No fitted coefficient, scenario weight, calibrated probability or predictive-lift claim |
| MDS-2026.09.04-v3.4 | 2026-09-04 (same day as v3.2/v3.3) | Added the most-recent-meeting reconciliation requirement to the regime-dominance audit (RULES_GENERAL.md §5, `L-066`) and the native-language sourcing requirement to the acquisition order (RULES_GENERAL.md §4, `L-067`); added the two-track "Path to performance-eligibility" roadmap to README.md, recording that the running count of clean, demonstrably pre-result event units toward the 60-unit checkpoint is currently 0. No fitted coefficient, scenario weight, calibrated probability or predictive-lift claim |
| MDS-2026.09.05-v3.5 | 2026-09-05 | L-068–L-071: native-score/contract arithmetic, failed-gate propagation, two-sided phase/separation branches, host-qualified source semantics; correct tennis games-handicap logic and narrow unsupported blanket knockout suppression. Non-performance-eligible settlement audit; no model fit, coefficients, weights or calibrated probabilities |
| MDS-2026.09.05-v3.6 | 2026-09-05 | L-072: accept user-confirmed pre-game freeze for existing non-live cards; separate issue horizon from settlement state; include process mistakes in historical ranking denominators; apply L-068–L-071 controls without retroactively validating new weights |


The numerical architecture is separately versioned as `NTS-2026.09.02-v0.3`. Version 0.3 removes market-derived predictive lanes and adds fractional-contract and environment/source-governance design; no dataset or model was created. Tennis, rugby union and rugby sevens remain outside numerical scope until explicit target/source/model cards are approved. MDS v3.0 does not create H0, fit a model, promote a coefficient or publish a probability.


## September 5 user confirmation — controlling eligibility correction


[Controlling policy](PERFORMANCE_ELIGIBILITY_POLICY.md). The user confirmed: **all existing game logs except views explicitly labelled LIVE were strictly frozen pre-game**. Accept this as the provenance basis `USER_CONFIRMED_PREGAME_FREEZE`, effective September 5. Non-live issued cards are eligible for historical qualitative directional/ranking evaluation. A late local import alone no longer excludes them. This correction supersedes earlier blanket `E1-Q-LATE_IMPORT`, “all non-performance-eligible” and “zero eligible historical units” statements. It records user confirmation; it does not assert independent timestamp verification or change original file times.


Keep four distinct fields: **forecast horizon at issue**, **event state when checked for settlement**, **provenance basis**, and **endpoint settlement status**. An originally pre-game card found live during settlement stays pre-game and awaits a final; it does not become a live-issued forecast. A live source/page, a “live counter-branch”, or a post-issue status check is not an issuance label. Explicit live or live-state-unverified issued views stay outside pre-game metrics. Original pre-game and later live views of one event must retain their own ranks and share an event cluster.


The headline historical scorecard includes all identifiable, genuinely issued, settled contracts/ranks in its stated cohort, including `FORCED RANK`, LOW evidence, and `PROCESS_DEFECT` outcomes. Do not remove a bad pick because its reasoning was poor. Process grade is a diagnostic column and a separately labelled compliance slice. No-forecast/no-action records are not trials; unresolved/void/push/partial rows have explicit denominators; materially unidentifiable contracts remain unscorable with the reason recorded. A row’s missing operator terms may limit ticket settlement without erasing a clearly defined research endpoint. Never use an issue-time row already decided as a predictive success.


Use the exact original pre-game order, including the latest genuinely pre-game refresh; never substitute a later live or retrospective order. Deduplicate aliases and group related targets/views by underlying event. Report historical performance by issued method, sport/competition, horizon and target. The ten newly settled cards are an evaluated v3.4 pre-game cohort. Earlier historical scorecards need those same row/view joins before a new all-history aggregate is reported; the complete status index is not itself a performance denominator.


Old games may measure their issued methods and supply development evidence for improvements. They cannot validate a v3.5/v3.6 change designed after their outcomes were seen. Keep the historical ranking count separate from each frozen challenger’s later test count. No probabilities, fitted coefficients, calibration or market-edge claims are created by this provenance correction. Future snapshots/hashes and externally timestamped revisions are useful provenance records; a local hash or editable git timestamp alone is not an independent timestamp authority, and no git-only approval gate is imposed on this user-confirmed history.


## Current scoring, build and evaluation contract — 2026-09-17


SCORING_AND_VALIDATION defines exact binary versus W/P/L/action-conditional scoring; the full categorical Brier is half-scaled, realised pushes stay in its denominator, and WIN/LOSS-only scoring uses q=p_win/(1-p_push). Retain incompatible old scores as labelled legacy diagnostics. Average once per prespecified target then once per event; compare identical held-out events and fixed threshold grids with a frozen empirical/conditional baseline. Report paired event uncertainty, coverage, calibration and target difficulty. No global absolute-normalised-edge ranking is valid across unrelated distributions.


MODEL_IMPLEMENTATION_RECIPES supplies the executable empirical/count/scenario/scoring/phase/extra-state primitives. NUMERICAL_PROGRAM provides the single stage sequence: field-specific source admission and H0 before fitting; S5 held-out checks **and S6 prospective shadow before publication**. A3/A4 and learned rank/pair models are optional/dormant, not compulsory predecessors. Reference code tests do not establish model performance. Historical user-confirmed forecasts remain learning-only under the later controlling directive; no retrospective data join is called prospective.


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — market-independent data architecture


The production architecture is now explicitly five-layered:


`raw immutable snapshots -> canonical sporting facts -> prediction-time features -> frozen predictive distribution -> post-forecast contract queries`.


The user-supplied total/spread belongs only to the final contract-query layer. It cannot cross backward into raw facts, features, priors, model inputs, scenario selection, centre/width estimation or calibration. A build artifact should be reproducible from the first four layers **without any betting line present**.


Every material raw/canonical field stores source class, field owner, upstream lineage, known/retrieval time, definition version and snapshot hash. Labels/results are stored separately and become visible to training only after their event/label availability time. Historical revised values may be used as labels when documented, never as evidence that the same value was known pregame.


Feature engineering should prefer stable, mechanism-level inputs and partial pooling over tiny recent-result windows. Recent information earns weight through a measurable state change (participant, workload, process, environment or role), not through "hot/cold", rebound or due narratives.