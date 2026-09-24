# Prediction and probability model review — 17 September 2026

**Conclusion:** the framework should change, especially its over/under measurement and several recently promoted rules. The strongest next modelling step is to implement and compare a small number of the distribution models already specified. Adding more retrospective rules or more sophisticated model names will not establish better predictions.

**Scope and delivery:** this is a review and proposed change set. No existing rule, issued forecast, result, probability, canonical ID or model status was changed. The supporting [evidence](audit_2026-09-17_models/REVIEW_EVIDENCE.md) and [reproduction code in Markdown](audit_2026-09-17_models/REPRODUCE.md) preserve the calculations and file inventory. Historical material remains learning-only.

## 1. What was reviewed and what can be measured

The audit read, hashed and indexed **all 354 pre-existing project Markdown files: 45,253,448 bytes, 269 unique byte contents and 85 redundant exact copies**. That includes 50 root documents, 146 archive files, seven older prediction-log files and 151 audit/snapshot files. Dependency documentation in node_modules, the spreadsheet scratch runtime and .git was excluded.

Full-text searches and section indexes cover the complete corpus. Detailed content inspection concentrated on the active method, all ten sport rule files, model/training/source specifications, four canonical logs, recent original mini logs, and historical model/review documents relevant to the current claims. This is not a claim of manually reading every line of 45 MB. Different archived versions of one forecast were not counted as separate predictions.

The active log is Part 4, through P-451, with P-452 next. Numerical modelling remains **Stage S0 / design only**: no fitted champion or calibrator exists. The probability-bearing cards contain **UNVALIDATED_SUBJECTIVE** estimates. Older probability-free cards can reveal reasoning failures but cannot retrospectively acquire probabilities or Brier scores. See [current method](METHOD.md), [numerical program](NUMERICAL_PROGRAM.md) and [model register](NUMERICAL_MODEL_REGISTER.md).

I reconstructed **477 booked probability rows on 114 cards** from canonical records, preserving the later P-402 corner settlements and P-406 phase settlement. The code found no conflicting repeated probability/outcome tuple and no error in the explicit table-level Brier cells it parsed. These are checks against the Markdown record; this review did not independently re-fetch all sporting results.

| Recorded cohort | Booked rows | W / L | Recomputed legacy mean Brier |
|---|---:|---:|---:|
| P-318–P-332 probability-bearing cards | 33 | 17 / 16 | 0.218121 |
| P-333–P-344 | 39 | 20 / 19 | 0.260131 |
| P-345–P-371 | 105 | 61 / 44 | 0.243439 |
| P-373–P-423, including later settlements | 196 | 108 / 88 | 0.226611 |
| P-424–P-437 | 52 | 36 / 16 | 0.189244 |
| P-438–P-451 | 52 | 31 / 21 | 0.209663 |
| **All probability-bearing cohorts** | **477** | **273 / 204** | **0.226548** |
| **PRIMARY_SCORED subset of the above** | **136** | **71 / 65** | **0.246825** |

The primary subset contains **33 cards**, not 136 independent experiments. Its mean is only 0.003175 below the trivial 0.25 binary benchmark. The mixed mean benefits from a different selection of competitions, target families and thresholds. Neither number establishes calibration, predictive superiority or market value, especially with the push-scoring defect below.

**A reproduced aggregation error:** P-344's four recorded Brier values are 0.3136, 0.2116, 0.2116 and 0.3969. Their mean is **0.283425**, not the printed **0.3334**. The difference accounts for approximately 0.00513 in that 39-row cohort and 0.000419 in the current 477-row aggregate. Part 4's approximate 0.2270 should therefore be read as **0.22655** when recomputed from the rows. The primary-population mean reproduces correctly. Source: [Part 3](PREDICTION_LOG_COMBINED_3.md), lines 219–253; complete row receipts in the evidence document.

## 2. What the over/under evidence actually says

### Promising target selection; main-line skill remains unresolved

| Evidence slice | Recorded result | Interpretation |
|---|---|---|
| Earlier preferred side of forced O/U pairs, P-345–P-423 | 27 / 45 | Existing retrospective figure, not a newly independently reconstructed all-target sample. Selected sports and endpoints are mixed. |
| Earlier free team and phase scoring totals | Team totals 18 / 24; phases 9 / 11 | Easier thresholds and analyst selection are confounders. |
| Earlier soccer full-match forced pairs | 1 / 6 | A useful failure sample, far too small to justify banning soccer totals. |
| P-424–P-437: highest-ranked scoring total on each issued card | **10 / 12** | Recomputed from frozen ranks; includes team, phase and alternate totals. |
| P-438–P-451: same definition | **7 / 12** | Recomputed by exactly the same rule. |
| Latest eight MLB cards: preferred full-game total | **4 / 8** | Little directional separation on these particular lines. |

The last two cohorts together are **17 / 24** for the original highest-ranked scoring total. Corners, wickets, strikeouts, handicaps and winner rows are excluded; no lower-ranked winner is substituted. The full 24-card selection table is in the evidence file.

The earlier 27/45 and family figures are reported in [Part 3](PREDICTION_LOG_COMBINED_3.md), lines 3680–3719. They are not added to the 24-card total: their units and selection rules differ.

There is no defensible universal “prefer Overs,” “prefer Unders,” “prefer team totals” or “always prefer the first half” rule. Under 4.5 goals and a team Over 0.5 often have higher base probabilities than a main total near its median. Winning them more often may satisfy a high-hit-rate selection objective without demonstrating that the underlying distribution improved.

For a completed half-line pair with identical action terms, one side wins by construction. For an integer pair both may push. Report the **frozen preferred direction once per target**; retain both rows for settlement and coherence checking. Ranking a total below a run line may be correct when the requested objective is unconditional probability of winning: a push is not a win. That ranking is not automatically a distortion.

### Repeated mechanisms worth retaining

- **Baseball: workload and relief transitions matter as much as starter reputation.** P-335's omitted rehab pitch-count ladder weakened the assumed short-start Over mechanism. P-373, P-420 and P-442 show that a contained starter can be followed by decisive middle relief. Use starter workload, the likely first relief arm, inherited runners and score state. Do not count fatigue, short starts and bullpen exposure as three independent adjustments to the same causal pathway.
- **Baseball: the full-game endpoint matters.** P-443 was 4–4 after nine and finished 6–5; P-444 was 2–2 after nine and finished 5–4. A regulation total and an extras-inclusive total are different distributions.
- **Soccer: chance creation, conversion, team allocation and corners need separate treatment.** P-430's team-to-score loss and match Over win demonstrate that a combined total does not identify which team supplies the goals. P-408 and P-402 demonstrate that territory, goals and corners are not interchangeable.
- **Soccer: retain a real phase count distribution.** P-441 printed first-half and full-match count masses, making its totals reconstructable. That is a reproducibility advantage; one excellent realised score does not validate those masses. P-438's loss similarly does not prove every future first-half Under needs a lower probability.
- **Cricket: phase success can coexist with innings collapse.** P-406 reached 68/2 after six overs but finished on 118. Wickets, the middle-overs attack and the chase target must condition later exposure. P-445's unmet batting-first activation condition correctly produced no active total trial.
- **Basketball and American football: model shared volume and late states.** P-427's fourth quarter and the P-413/P-414 efficiency outcomes broke both a cushion and an Under. Shared pace, turnover scoring, late fouling and overtime belong in a joint process; a generic “defensive game” label cannot price them.

These lessons were already visible in the July archived model framework and the August/September retrospectives. The recurring gap is execution and estimation, not a shortage of named mechanisms.

## 3. Corrections to make before tuning any predictive model

### A. Fix integer-total scoring and conditioning — highest priority

[METHOD.md](METHOD.md), section 5, scores p(win) on WIN/LOSS rows and omits pushes. [RULES_GENERAL.md](RULES_GENERAL.md), section 16.9, correctly requires exact Under/push/Over masses, but the operational scoring formula does not carry that distinction through.

For an active integer-total contract:

    p_under + p_push + p_over = 1
    q_over = p_over / (1 - p_push)

Use a full three-outcome Brier/log score, including realised pushes. A separate WIN/LOSS-only binary diagnostic must use q, not unconditional p_over. Alternatively, unconditional “wins versus does not win” is a legitimate binary event only if pushes are retained as non-wins for that diagnostic; it is not ticket-loss settlement.

Example: **P-443 Over 8.0** was frozen at 0.45 win / 0.13 push / 0.42 loss. Its conditional probability of winning a decisive result is **0.45/0.87 = 0.51724**. Calling this simply a “45% direction” conceals its conditioning.

Across the eight recent MLB total decisions, mean unconditional preferred p is **0.4725**, while mean non-push q is **0.53637**. The recorded preferred binary Brier is **0.2591**; the consistent non-push binary diagnostic is **0.24572**. The half-scaled three-outcome score is **0.259225**. These answer different questions; the change is a scoring correction, not a new predictive improvement or rewritten forecast.

For exact binary complements, two Brier rows carry the same error. Keep a decision-level average and event-level uncertainty so such pairs do not double their influence relative to a single free row. With integer pairs, preserve all three outcomes rather than forcing the two win probabilities to sum to one.

### B. Remove the universal MLB run-line ceiling

[RULES_BASEBALL.md](RULES_BASEBALL.md), control 34, and [METHOD.md](METHOD.md), line 259, assert that a favourite −1.5 probability above approximately 0.53 is not derivable and should essentially never rank first.

The identity is valid:

    P(favourite wins by 2+) =
        P(favourite wins) × [1 - P(favourite wins by exactly 1 | favourite wins)]

The universal bounds are not. A pooled realised winner-margin rate does not prove a lower bound for every matchup's conditional one-run rate, and the documents supply no theorem or fitted evidence limiting every MLB win probability to 0.70.

An illustrative coherent probability pair w=0.85 and r=0.23 gives 0.6545 for −1.5. This is a mathematical counterexample to the claimed ceiling, not an estimate for a real game. Derive winner and margin probabilities from one joint score distribution. Retain league one-run frequencies as uncertain comparison priors, never as universal limits or automatic rank demotions.

Also define r for the **specified team's** one-run win, with home/away, total environment and endpoint conditioning. The empirical “winner-minus-loser season win%” grouping must not be silently substituted for a pregame team-strength feature.

### C. Remove the 12% push ceiling and fixed variance floors

[RULES_BASEBALL.md](RULES_BASEBALL.md), control 35, says park identity explains 4.3% of unconditional variance and therefore no game-specific push mass above about 12% is supportable. That conclusion does not follow.

An unconditional league distribution is a mixture of matchup distributions. The variance decomposition is:

    Var(T) = E[Var(T | X)] + Var(E[T | X])

Park alone does not exhaust X: pitchers, orders, weather, bullpen state and other information may explain variation. Even a variance constraint would not uniquely bound a particular integer's probability. For illustration, a Poisson distribution with mean 8 has P(T=8)=0.13959. This refutes a universal mathematical 12% cap; it does not endorse Poisson as a calibrated MLB model.

Keep a requirement to derive and check push mass. Replace the cap with conditional residual/coverage checks on held-out games. Treat the NFL 13.9-point residual figure and the other historical width references as benchmarks, not universal minimum standard deviations for every conditional population. A mean/width or “corridor” with no defined coverage is insufficient.

### D. Repair the extra-innings calculation

[RULES_BASEBALL.md](RULES_BASEBALL.md), control 37, says a tie on the regulation total line becomes an Over “about 60%” of the time. This confuses **at least two extra runs** with **at least one extra run**.

If regulation ends tied with total exactly L, and the game subsequently completes under the same full-game contract without a void, deciding the tie requires at least one additional run. The final total is therefore greater than L. For that precise state, it becomes an Over with probability **1 conditional on completion**, not 0.605.

The probability of reaching extras must come from a joint home/away score state. A total mean and width alone cannot determine whether the teams are tied. The quoted 8.75% extras rate, 2.88 additional-run mean and 68.5% one-run-margin rate are historical cohort references; they are not fixed matchup probabilities. Likewise, a dog +1.5 probability of roughly 0.84 in extras assumes a particular split of winners and margins, not just the one-run frequency.

The proposed implementation should sum over regulation states and conditional extra-inning transitions, preserving game type, home last-bat behaviour and termination rules. Do not add an extras allowance to a mean already estimated from extras-inclusive final totals.

### E. Fix the “prospective” label on C-OU-GEOMETRY

The manifest in [LEARNING_REGISTER.md](LEARNING_REGISTER.md), lines 762–774, opened on **16 September**. Part 4 calls the entire P-424–P-437 batch its first prospective evidence.

The [preserved mini log](archive/mini_logs/PREDICTION_MINI_RUNNING_LOG_P424_P437_RECONCILED_2026-09-17.md) records P-425 frozen at **15 September 19:49:10**, P-426 at **19:56:12**, P-427 at **23:25:06**, and P-429 at **23:53:08**, all Australia/Melbourne. These forecasts predate the manifest. Their later import on 17 September does not make them tests issued under it.

Classify those as historical or, only if supported by a pre-outcome locked evaluation plan, separately blinded holdout evidence. For same-day and later cards, verify the manifest freeze time, forecast time, outcome-availability time and rule version before crediting a prospective count. The entire batch cannot be counted by import date.

Match baseline difficulty as well as stated-p bands. A 0.60 analyst estimate for a naturally 0.80 event is not the same task as a 0.60 estimate for a naturally 0.50 event. The current 50-card/two-sport/0.02-Brier rule should be an operational review point, not sufficient evidence by itself.

### F. Repair two “bounded” corner settlements

[RULES_GENERAL.md](RULES_GENERAL.md), lines 1193–1203, requires settlement invariance across every admissible period split, but then treats P-255 and P-256 as bounded research wins:

- P-255: 24 whole-match corners; the regulation Over 8.5 loses if at least 16 occurred in the excess interval.
- P-256: 15 whole-match corners; the regulation Over 8.5 loses if at least seven occurred there.

The files show no actual period split or valid upper bound excluding those possibilities. “That many extra-time corners seems unlikely” is not an invariant bound. Whole-match counts supply an upper bound on regulation counts, not the lower bound needed for an Over.

Recommend restoring these rows to unresolved-period status until regulation counts, event timelines or a genuine mathematical bound are obtained. Preserve the existing issued forecasts and record the settlement correction separately. This is a label-quality correction; it does not imply either original pick lost.

### G. Retire statistical shortcuts that survived earlier corrections

- **Absolute normalised edge:** section 16.9 already corrects the universal ordering rule, but METHOD's checklist still says every total's probability must be monotone in its absolute normalised edge. Remove that stale wording. Use the actual CDF at the line, with signed direction, count support and push mass.
- **L5/L10/L15/L20 trend test:** these overlapping windows are not four independent samples. Monotonicity plus a gap exceeding dispersion among their averages is not a valid general test of “trend” versus “noise.” Retain them as descriptive displays; estimate recency decay, opponent adjustment and change-point effects with time-ordered validation.
- **Uncertainty always changes width only:** retain the useful rule against an unsupported directional adjustment. Remove an absolute prohibition on movement toward a legitimate population prior. Hierarchical shrinkage and integrating asymmetric injury/lineup scenarios can legitimately change both mean and variance. State the prior and scenario probabilities.
- **A named realised tail proves its probability was too low:** it does not. Review repeated residuals and outcome-frequency errors, including successful cards, before altering the mass.
- **Separate per-row confidence caps after deriving probabilities:** a change from a count-model probability to a lower “lineup-capped” row must be represented in the underlying distribution or clearly labelled as a different subjective model. Otherwise the displayed CDF ceases to explain its own row probabilities.

## 4. Models to keep, prioritise, add or defer

The technical register already contains empirical distributions, hierarchical models, sport-state simulators and flexible distributional challengers. Most proposed sporting improvements belong inside those models rather than in a new algorithm.

| Sport / target | Recommended model action | Specific over/under purpose |
|---|---|---|
| **MLB runs — first pilot** | Implement the existing empirical baseline and an interpretable hierarchical joint-run challenger; retain Poisson as a diagnostic and test overdispersion. | Estimate both teams' scoring, their covariance, exact count masses, starter-to-relief exposure and the regulation/extras endpoint. Partial-pool venue effects; do not use each park's roughly 75 games as a precise standalone CDF. |
| **Soccer goals — second priority** | Retain independent Poisson baseline and dynamic hierarchical Dixon–Coles/bivariate challenger already registered. Add an explicit linked phase/full-match implementation within that family. | Opponent-adjusted creation and finishing, team allocation, low-score mass and score-state changes. First-half rates must not be an assumed fixed fraction of the full match. |
| **Cricket phase and innings** | Retain the ball/over, wicket and remaining-resource engine. Scope one competition/format before fitting. | Couple scoring with wickets, available batters, bowling phases, toss activation, chase termination and reduced exposure. Phase and innings share one trajectory but are distinct endpoints. |
| **Basketball totals** | Retain possession × efficiency baseline and joint score distribution, with a possession simulator only if useful. | Shared pace, lineup minutes, shooting uncertainty, turnovers, late fouling and overtime. Avoid a fixed points-average Normal with an assumed width. |
| **American football totals** | Retain drive/clock and discrete scoring-state models. | Volume, explosive efficiency, defensive/special-teams scoring, pace changes and overtime. Key-score mass cannot be reconstructed from a point mean alone. |
| **AFL / AFLW** | Retain competition-specific scoring-shot and goal/behind conversion models. | Separate opportunity volume from conversion, with distinct population scales and lineup regimes. |
| **Rugby league** | Retain set/field-position and try/conversion models. | Interchanges, errors, penalties, sin bins and golden-point treatment drive total exposure and dependence. |
| **Ice hockey** | Retain shot/goal and goalie/manpower models. | Goalie mixture, power plays, empty net and regulation versus overtime/shootout endpoints. |
| **Tennis** | Add a named numerical register entry if numerical support is intended; the existing sport rules and archived framework already describe the serve/return point–game–set tree. | Derive total games and games handicap together, with surface/format/tiebreak and retirement rules. A match-win Elo probability alone does not determine match length. |
| **Rugby union / sevens** | Add scoped numerical register entries if support is intended; these are missing from the current eight-sport main table. | Phase/territory scoring, goal-kicker and card states, format-specific exposure and termination. Do not silently reuse rugby-league parameters. |
| **Corners, SOT and player counts** | Keep separate exposure/rate/dispersion models; defer poorly settleable leagues. | Do not substitute team-goal or winner models. Freeze provider definitions and minutes/participation before training. |

**Keep dormant:** boosted distribution models, neural models, learned rankers, pair selectors and large ensemble searches until a simple baseline has a valid data pipeline and chronological benchmark. No evidence in the current logs establishes that those extra layers will solve the identified errors.

**Remove from the active sports-only pathway:** stale M0 market-only and M1 market-informed instructions remain in the numerical register even though the current training specification says they were retired. Preserve them as historical definitions if needed, but make their inactive status explicit. No market-derived input is needed for this review's proposed pilot.

**Do not implement a blanket bias shift:** the twelve-card baseball centre table mixes leagues and includes three retrospectively inferred corridor midpoints. Later MLB residuals move in the other direction. Neither that table nor the six-card basketball sample supports a permanent run/point correction. Log an actual issued mean, median and interval definition separately before estimating bias.

## 5. A concrete over/under workflow and evaluation plan

### Forecast object

Each forecast should retain one compact authoritative object:

1. Event, competition/rules era, pregame or live horizon, cutoff, model version, exact endpoint and activation/void terms.
2. Source snapshots for the inputs that can move this target, with effective and first-known times.
3. One joint score/resource distribution, plus any genuinely separate niche-target process. Identify whether it is fitted or subjective.
4. Team/phase marginals; total mean and median; defined prediction intervals; exact masses at supplied thresholds.
5. Each row's unconditional win/push/loss/void probabilities, with conditional-on-action quantities explicitly labelled.
6. The frozen supplied slate, any predeclared analyst-added lines, dependence groups and one preferred direction per target.

For integer-valued scoring totals, query the same CDF:

    Under L = P(T < L)
    Push L  = P(T = L), where the contract provides a push
    Over L  = P(T > L)

A terminal total-count CDF is sufficient for totals, but not for winner, margin, team allocation or phase dependence. Those require the corresponding joint object. Scenario buckets that straddle a threshold must be subdivided or retain explicit unresolved within-bucket mass.

### Baseline and pilot

**Start with the already proposed MLB full-game-runs pilot, revised to use complete event records and exact endpoints.** Enumerate a fixed eligible population rather than collecting only requested games. Choose a freeze horizon consistent with source availability. Fit or estimate baselines on earlier games only; include home/away, lineup and pitcher information only when demonstrably available at that horizon.

Compare on identical games and thresholds:

- A0: a rolling, competition-aware empirical distribution with properly pooled context.
- A1: an interpretable conditional count/joint-run distribution.
- The original subjective forecast, when one was genuinely frozen for that game.

Use a fixed grid of scoring thresholds as well as the exact supplied lines, with **one distribution-level weight per game**. Fix analyst-added-line generation before the result and log all candidate lines considered. This distinguishes better predictions from easier selections.

Use distribution scores such as CRPS or ranked probability score, the log score of the observed outcome, interval coverage/width and count calibration. For supplied integer totals use the complete outcome vector and a separately labelled non-push directional score. Retain preferred-side accuracy as a secondary descriptive metric.

A 0.5 reference can remain as a simple binary diagnostic, but the important comparator is the same game's preregistered empirical/conditional baseline. Report a skill score against that baseline on the **same sample**, not against a baseline fitted to the outcomes being evaluated. Proper scores measure more than calibration alone; [scikit-learn's calibration documentation](https://scikit-learn.org/stable/modules/calibration.html) explains why a lower Brier score need not mean better calibration.

### Training and decision rule

Use training → tuning → later calibration → untouched test, preserving event groups and prediction-time joins. [Rolling-origin validation](https://otexts.com/fpp3/tscv.html) explicitly requires each training set to precede the evaluated observation.

Freeze the candidate and evaluation plan before a new prospective run. Compare paired game-level score differences, with uncertainty clustered by event and, where warranted, schedule blocks. Separate league, endpoint, horizon and line difficulty. Avoid repeatedly opening the same test sample after every change.

The existing “25 cards,” “50 cards” and “150 games” can schedule a review, but do not establish adequacy automatically. Set the required evidence from the precision of the paired comparison and coverage of important regimes. If results are inconclusive, retain the simpler model and continue the fixed test; do not infer improvement from a short winning run.

Do not fit a recalibrator to all current mixed rows. If later calibration is supported, fit it on a disjoint calibration set and verify that the final joint distribution still obeys support, complements, nesting and endpoint relationships.

## 6. Proposed file changes, in execution order

| Priority | Files | Proposed change |
|---|---|---|
| **1 — correctness** | METHOD, RULES_GENERAL, MODEL_AND_DATA_SPEC, NUMERICAL_TRAINING_SPEC | One operational scoring definition for binary, push and action-conditional outputs; remove conflicting normalised-edge wording. Preserve historical probabilities. |
| **1 — correctness** | RULES_BASEBALL, METHOD, CONTROLS, LEARNING_REGISTER | Withdraw universal −1.5 and push ceilings; correct the tie-on-line extras identity; retain source frequencies as contextual priors. |
| **1 — label integrity** | RULES_GENERAL, Part 4 Appendix A, GAME_LOG_STATUS_CURRENT | Correct unsupported P-255/P-256 period-bound settlements through appended corrections and restore the required follow-up status. |
| **2 — measurement** | Parts 3/4, README, relevant scorecard summaries | Append P-344 aggregation correction; derive future means from row-level sums; split decision, event and row measures. |
| **2 — validation** | LEARNING_REGISTER, CONTROLS, Part 4 | Reclassify C-OU-GEOMETRY evidence by manifest/issue/result times; replace global normalised-edge matching with a defined baseline-difficulty comparison. |
| **2 — operational clarity** | METHOD, RULES_GENERAL, ten sport files | Consolidate repeating overlays into the compact forecast object; descriptive recency windows; uncertainty through a declared model; preserve old gate IDs as history. |
| **3 — model scope** | NUMERICAL_PROGRAM, NUMERICAL_MODEL_REGISTER, NUMERICAL_TRAINING_SPEC | Prioritise A0/A1 MLB pilot; keep advanced candidates dormant; add explicit tennis/union scope only if intended; mark M0/M1 retired. |
| **3 — dependencies** | H0_DATASET_CARD, README, source/model specifications | Root H0_DATASET_CARD.md is missing although repeatedly referenced. Recover and reconcile an archived version or explicitly document its absence before any build. Do not claim it is current merely because two before-snapshots exist. |

The numerical program also contradicts itself: its S1 table requires feature-source approval while the pilot says no approval beyond CANDIDATE is needed; its body suggests publication after S5 while the model register also requires prospective shadow evidence. Resolve those states in one model card. “No data has been pulled” also needs narrowing: the latest retrospective records season-scale MLB retrieval, while no training dataset or fitted build exists.

The existing version remains v4.0 despite many subsequent behavioural changes. Future cards should freeze a control-set revision or hash alongside the method version so that an apparent improvement can be attributed to an actual unchanged method.

## 7. Decision

**Edit** the probability/settlement mathematics and validation labels first. **Prioritise** implementation of the existing simple, sport-specific distribution models, beginning with MLB totals. **Add** a complete event-level evaluation record, fixed baseline comparison and explicit missing sport registrations only where support is intended. **Remove** unsupported hard probability limits, pseudo-statistical trend rules and stale active model instructions.

Preserve the useful work already done: exact target definitions, source provenance, immutable issued forecasts, explicit count distributions, score-state transitions, coherent team/phase relationships and honest missingness. Those are the foundation for better over/unders. The present evidence identifies defects and testable improvements; it does not yet demonstrate that a changed model will outperform on future games.

### Validation of this review

- All 354 original Markdown contents were read and fingerprinted; exact duplicate storage was identified.
- All 477 booked probability tuples were joined by canonical ID and rank, including explicitly documented later settlements.
- Both recent 52-row cohort Brier means reproduce; the 136-row primary mean reproduces; the historical aggregate discrepancy is traced to P-344.
- The last 24 highest-ranked scoring-total decisions and eight MLB push vectors are listed explicitly in the evidence document.
- No sporting final was newly settled, no model was fitted and no forecast was retrospectively altered.
- See [evidence and inventory](audit_2026-09-17_models/REVIEW_EVIDENCE.md) and [reproduction code](audit_2026-09-17_models/REPRODUCE.md).
