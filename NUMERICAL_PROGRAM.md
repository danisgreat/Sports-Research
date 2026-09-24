# Numerical program — Track B


Program revision: **NP-2026.09.19-v2**. Training specification: **NTS-2026.09.19-v0.5**. Governing forecast method: **MDS-2026.09.19-v4.3 / CR-2026.09.21-3**.


**Current state: Markdown implementation complete; no empirical dataset built, model fitted, calibrator fitted or prospective shadow forecast issued.** The user's 17 September request authorizes implementation of the audit findings; the subsequent clarification prioritizes implementation within Markdown. This satisfies the authorization question for this work. The previous statement that “implement all recommendations” could not authorize implementation is withdrawn. It is not a reason to request permission again.


The executable reference algorithms, sport-specific equations, forecast/evaluation schemas and acceptance cases are in [MODEL_IMPLEMENTATION_RECIPES.md](MODEL_IMPLEMENTATION_RECIPES.md). They are implementations/specifications, not numerical champions. Seasonal MLB data were retrieved in an earlier retrospective, but that does not constitute a point-in-time H0 training dataset. [H0_DATASET_CARD.md](H0_DATASET_CARD.md) restores the missing root dependency and defines the remaining data requirements.


## 1. One stage sequence and publication gate


| Stage | Deliverable | Current status / exit condition |
|---|---|---|
| S0 design | Exact target, algorithms and comparison plan | Markdown implementation provided; ten sport scopes registered |
| S1 authorization and source admission | User-authorized scope; exact field/source/endpoint/cutoff admission | Authorization for audit implementation recorded. Actual historical feature admission NOT COMPLETED; a generic CANDIDATE label is insufficient |
| S2 H0 | Systematic eligible-event universe and immutable point-in-time feature/label manifest | NOT BUILT; uniqueness, completeness, availability, joins, support and exclusions must pass |
| S3 A0/A1 | Fit empirical and interpretable conditional baselines on identical chronological folds | NOT FIT; execute the supplied recipes only on admitted inputs; preserve failed comparisons |
| S4 optional challengers | Sport-state A2, then A3/A4 where justified | DEFERRED until A0/A1 and data coverage support the extra complexity; not a compulsory step toward publication |
| S5 held-out evaluation | Optional calibration on disjoint CAL, then untouched TEST opened once | NOT RUN; proper scores, coverage, calibration, support, critical slices and operational failure checks required |
| S6 prospective shadow | Immutable, time-stamped forecasts from the frozen build, before outcomes | NOT STARTED; required before promotion/publication, not bypassed by S5 |
| S7 optional decision models | A5 ranker/A7 pair selector on independent decision sets | DORMANT; neither is needed to query a coherent distribution |


**PUBLISHED requires S1–S3, the applicable S5 integrity/comparison checks and qualifying S6 shadow evidence for the exact scope.** S4/S7 sophistication is optional. Calibration fitted on CAL is not automatically beneficial or mandatory, but reliability must be assessed honestly. No single review count or p-value grants promotion. Current user-visible probabilities remain UNVALIDATED_SUBJECTIVE under METHOD; research recipe outputs may not be presented as validated forecasts.


## 2. First pilot: MLB regular-season final runs


| Field | Frozen design for the first build |
|---|---|
| Population and unit | All enumerated MLB regular-season games in the declared season range, one event cluster per gamePk; record suspended, shortened, cancelled and missing games with reasons, never drop a loss after inspection |
| Target | Joint home/away completed full-game runs including extras and actual home batting termination. A separate full-nine-inning contract excludes shortened action-invalid games under preregistered terms. Never mix these endpoints |
| Forecast horizon | Pregame cutoff explicitly frozen before scheduled start; all feature availability must precede it. Current reconstructed historical data without availability evidence can support development only |
| A0 | Rolling empirical joint final-score distribution, pooled league context, optional partially pooled home/away/venue strata with prior strength selected within TUNE. No precise standalone park CDF |
| A1 | Hierarchical joint count model with team attack/opponent prevention, home, partially pooled park and available starter/relief/lineup exposures; shared scoring environment or residual dependence estimated within training. Exact final-score route and explicit regulation/extras state route are distinct builds |
| Minimal implementation | Executable A0 empirical joint grid and hierarchical Gamma-Poisson shared-environment mixture in MODEL_IMPLEMENTATION_RECIPES. Parameters/priors are explicit inputs; no default is described as fitted. The state-kernel function composes admitted regulation/extra transitions when available |
| Starter-to-relief feature | Expected batters/innings under the freeze-time workload limit; first likely relief arm and its availability conditional on exit inning/score. Do not separately count the same short-start effect as fatigue, bullpen exposure and early-relief adjustments |
| Missing feature policy | Marginalize over sourced scenarios or use the preregistered reduced-feature baseline; missingness is recorded. Do not reconstruct past probable starters, lineups or bullpen availability from final box scores |
| Comparators | A0 versus A1; genuinely issued subjective probabilities only on the shared available sample. No retrospective subjective forecast generation |
| Evaluation | One distribution-level weight per event; integer RPS/CRPS, observed-total log score, count calibration, central interval coverage/width; fixed thresholds 4.5 through 14.5 and integers 5 through 14 plus the exact frozen supplied lines. W/P/L and decisive diagnostics per SCORING_AND_VALIDATION |
| Temporal blocks | Before data inspection, freeze exact TRAIN/TUNE/CAL/TEST dates in H0. No invented dates or completed stage is claimed here. Rolling origins keep all training observations earlier than the evaluated game; all same-game views stay in one block |
| Decision rule | Paired event-level score differences and event/schedule-block uncertainty; important endpoint/venue/season slices non-inferior within preregistered tolerances. If uncertainty is material, keep A0 and accrue evidence. 150 games is a review point, not proof |


## 3. Subsequent scopes and deferred models


Soccer goals are second: independent Poisson baseline; dynamic hierarchical Dixon–Coles/bivariate challenger; linked first-half and conditional second-half score states, not a fixed first-half fraction. Soccer corners are a separate event process. Cricket retains resource/wicket state and target-censoring models. Basketball/football/AFL/rugby/hockey retain their sport-native exposure and scoring processes. Tennis and rugby union receive explicit scoped register entries and endpoint gates. See the recipes and each sport rule file.


A3/A4 flexible boosting/neural/distributional challengers, learned ranking and pair selection remain dormant until simple baselines and adequate independent samples exist. M0/M1 market-only/hybrid predictive lanes are RETIRED under SPORTS_ONLY / MARKET_BLIND. No automatic Over/Under lean, generic probability shrink factor, universal MLB margin/push cap or conditional variance floor is added.


## 4. Reproducibility and source admission


An actual build requires immutable input hashes, source/field availability, population exclusions, exact settings/code hash, training maximum time, validation split manifest, numerical tolerances and every test result. The source owner and endpoint must be checked at field level; qualitative source use does not imply approved model-feature use. Observed final scores are labels, never issue-time covariates. Current-season end-of-season W% must not be joined into earlier forecasts.


Record fitting and evaluation artifacts in Markdown as requested; executable code blocks may be extracted in memory for checks. [Implementation validation](audit_2026-09-17_implementation/VALIDATION.md) reports which reference-algorithm and document checks actually ran. Those checks establish implementation consistency, not forecast accuracy. No external data retrieval, training, prospective run or result improvement is claimed by this revision.


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 5. Deep-research implementation priorities


Before S2/H0 is approved, complete the source firewall and provenance layer. H0 may not contain market/fantasy-derived predictive fields. The first end-to-end pilot remains MLB final-run distributions because official structured data and Statcast process information provide a comparatively strong independent sporting-data foundation.


For each sport, the first model must be a robust baseline plus a partially pooled interpretable challenger. Do not spend validation budget on neural/boosted/simulator complexity until the simple model has a frozen point-in-time dataset, rolling-origin predictions, CAL/TEST separation and source-latency checks.


A future claimed improvement must state: eligible population, exact dates, source manifest/hash, model/feature versions, TRAIN/TUNE/CAL/TEST blocks, baseline, proper-score differences with uncertainty, calibration/coverage, critical slices and prospective-shadow status. No undocumented "before/after" hit-rate comparison is acceptable.