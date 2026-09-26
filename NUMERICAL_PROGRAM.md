# Numerical program — Track B


Program revision: **NP-2026.09.19-v2**. Training specification: **NTS-2026.09.19-v0.5**. Governing forecast method: **MDS-2026.09.19-v4.3 / CR-2026.09.21-3**.


**Current state (updated 2026-09-26(c)):** every sport now has a reduced-feature A0/A1 build in code. MLB is in `tools/mlb_model.py`. Soccer, ice hockey, basketball, American football, AFL, rugby league, rugby union, baseball outside MLB, tennis and cricket are in `tools/sport_models.py`, with adapters in `tools/sport_data.py`. Each has a prospective shadow lane (`C-MLB-SHADOW`, `C-SPORT-SHADOW`). **These are not the full recipes** (possession, drive, shot, delivery and point-state models need play-level data that no admitted source supplies). They are the "separately labelled reduced-feature build" of `MODEL_IMPLEMENTATION_RECIPES.md` §1, built from final scores, dates and venue roles. Rolling-origin comparisons on public results, where they could be reached, are in `research/sport_models_2026-09-26/README.md`. Those comparisons do not constitute an approved H0, and no build is promoted.

*Previous state (2026-09-26(b)):* the MLB A0/A1 pilot is implemented as tested code (`tools/mlb_model.py`, synthetic-data tests in `tools/test_mlb_model.py`), and its prospective shadow lane (stage S6, `C-MLB-SHADOW`) is open. **No empirical dataset is approved, no model is fitted, no calibrator is fitted, and no shadow forecast has been issued yet.** Every other scope remains Markdown-only. The user's 17 September request authorizes implementation of the audit findings; the subsequent clarification prioritizes implementation within Markdown. This satisfies the authorization question for this work. The previous statement that “implement all recommendations” could not authorize implementation is withdrawn. It is not a reason to request permission again.


The executable reference algorithms, sport-specific equations, forecast/evaluation schemas and acceptance cases are in [MODEL_IMPLEMENTATION_RECIPES.md](MODEL_IMPLEMENTATION_RECIPES.md). They are implementations/specifications, not numerical champions. Seasonal MLB data were retrieved in an earlier retrospective, but that does not constitute a point-in-time H0 training dataset. [H0_DATASET_CARD.md](H0_DATASET_CARD.md) restores the missing root dependency and defines the remaining data requirements.


## 1. One stage sequence and publication gate


| Stage | Deliverable | Current status / exit condition |
|---|---|---|
| S0 design | Exact target, algorithms and comparison plan | Markdown implementation provided; ten sport scopes registered |
| S1 authorization and source admission | User-authorized scope; exact field/source/endpoint/cutoff admission | Authorization for audit implementation recorded. Actual historical feature admission NOT COMPLETED; a generic CANDIDATE label is insufficient |
| S2 H0 | Systematic eligible-event universe and immutable point-in-time feature/label manifest | NOT BUILT; uniqueness, completeness, availability, joins, support and exclusions must pass |
| S3 A0/A1 | Fit empirical and interpretable conditional baselines on identical chronological folds | **Reduced-feature builds for every sport in code (2026-09-26(c)).** Rolling-origin A1 v A0 run on public results for soccer (five leagues), NFL, AFL, NBA (2013–15), MLB (team-only core) and ATP. MLB and tennis each needed one parameter re-selected on an earlier TUNE window (v2; disclosed). Not run: NHL, WNBA, NBL, NRL, rugby union, cricket, NPB/KBO/CPBL. Failed comparisons are preserved (`research/sport_models_2026-09-26/README.md`) |
| S4 optional challengers | Sport-state A2, then A3/A4 where justified | DEFERRED until A0/A1 and data coverage support the extra complexity; not a compulsory step toward publication |
| S5 held-out evaluation | Optional calibration on disjoint CAL, then untouched TEST opened once | NOT RUN; proper scores, coverage, calibration, support, critical slices and operational failure checks required |
| S6 prospective shadow | Immutable, time-stamped forecasts from the frozen build, before outcomes | MLB lane (`research/mlb_shadow/`) and every-other-sport lane (`research/sport_shadow/`, per league) OPEN 2026-09-26; 0 rows so far. Frozen after the card and before the start; append-only. Required before promotion or publication, and not bypassed by S5 |
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


Record fitting and evaluation artifacts in Markdown as requested; executable code blocks may be extracted in memory for checks. Implementation validation (`audit_2026-09-17_implementation/VALIDATION.md`, not present in this repository) reports which reference-algorithm and document checks actually ran. Those checks establish implementation consistency, not forecast accuracy. No external data retrieval, training, prospective run or result improvement is claimed by this revision.


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 5. Deep-research implementation priorities


Before S2/H0 is approved, complete the source firewall and provenance layer. H0 may not contain market/fantasy-derived predictive fields. The first end-to-end pilot remains MLB final-run distributions because official structured data and Statcast process information provide a comparatively strong independent sporting-data foundation.


For each sport, the first model must be a robust baseline plus a partially pooled interpretable challenger. Do not spend validation budget on neural/boosted/simulator complexity until the simple model has a frozen point-in-time dataset, rolling-origin predictions, CAL/TEST separation and source-latency checks.


A future claimed improvement must state: eligible population, exact dates, source manifest/hash, model/feature versions, TRAIN/TUNE/CAL/TEST blocks, baseline, proper-score differences with uncertainty, calibration/coverage, critical slices and prospective-shadow status. No undocumented "before/after" hit-rate comparison is acceptable.

<!-- SETTLED-ROW-REVIEW-2026-09-25D -->
## 6. Evidence from the settled-row review for where a numerical model would help (2026-09-25(d))

This is descriptive; the scope and build state above are unchanged.

**Where resolution is lowest.** In the full settled record (`research/settled_rows_2026-09-25/README.md`), the human card process shows its lowest resolution where it is used most:

| Sport | Resolution | Decision Brier | n |
|---|---:|---:|---:|
| MLB | 0.0075 | 0.238 | 70 |
| Basketball | 0.012 | 0.241 | 31 |
| Soccer (for comparison) | 0.036 | 0.170 | 143 |

The seed baseline check agrees: across 29 decisions the cards did not beat a population table (`SKILL_BASELINE_LEDGER.md`).

That strengthens, but does not change, the existing priority: **the MLB A0/A1 pilot (§2) is where a disciplined numerical model has the most room to add information.** Its A0 is the leak-free population baseline, which is already computed per game by `research/base_rates_2026-09-25/build_skill_baseline_seed.py`. It must be beaten on held-out games before any card may cite it.

**Tools the pilot should reuse.**
- `tools/card_math.py`: negative-binomial run totals, the `no_zero` margin and push mass. It is the query layer, so model outputs and card outputs are scored identically.
- `tools/calibration_report.py`: the calibration and resolution report used in §1's evaluation gate.

**Soccer (the second scope).** Its phase and team-total rows already carry resolution (phase decisions 76.6% at a stated 0.677; team totals 76.0% at 0.744). A phase model is therefore a calibration and efficiency project there, not a rescue.