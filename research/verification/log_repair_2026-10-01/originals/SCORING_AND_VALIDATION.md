# Scoring and validation

Current scoring: **SCV-2026.10.01-v3**. [CURRENT_RULES.md](CURRENT_RULES.md) controls admission. This file defines measurement; historical cards retain their original conventions.

## Units, cohorts and scales

An event-family is the statistical unit, not each complementary contract row. Regulation EPL 1X2 has outcomes home/draw/away; NBL moneyline includes overtime. A different period, endpoint or competition requires a separate definition and registration. Pushes and voids retain their own mass/disposition; never turn them into losses or silently remove them.

Binary Brier is `(p-y)^2`. Multiclass Brier is `sum((p_k-y_k)^2)/2`, making the scale compatible with binary Brier for the two complementary states. Multiclass log loss is `-log(p_observed)`; binary log loss uses the two actual outcome probabilities. All model comparisons use identical events and endpoints. Improvement is **candidate minus comparator**; negative is better.

The legacy seven-contract EPL composite scores each event once as the mean of 1X2, total-2.5 and BTTS scores. It is available only for a separately qualified complete family scope. A passed 1X2 test cannot activate that composite. New candidate research compares 1X2 and NBL ML separately. q is an ordering transform from historical methods and is never scored as a coherent event probability.

## Experiments and calibration

Preserve the original September tuning/holdout CSVs, reports and receipts. Tuning/holdout commands refuse overwrites. New code creates new versioned experiments; the complete dependency graph and input hashes are frozen in model-build receipts. Runtime packages are pinned in `research/requirements.lock.txt`.

October's `development_protocol.json` was written before candidate calculation. It declares chronological folds, comparisons, selection periods, model grid, score scales, block bootstrap and seed. Those historical data had already been opened; the resulting `family_diagnostics.json` is **CHRONOLOGICAL_DEVELOPMENT_ONLY**. Selection on earlier periods followed by comparison on later periods reduces leakage, but does not restore an untouched test.

`model_diagnostics.py` reports family-specific reliability bins with sample counts and Wilson outcome-rate intervals, including empty bins, plus descriptive calibration intercept/slope. These are diagnostics, not fitted operational recalibration. No posthoc calibration curve is fitted to the final evaluation outcomes and deployed. Population scoring distributions, TB1-MD and fixed Elo supply stronger comparators; an odds benchmark remains separate.

Week-block paired bootstrap uses 10,000 replicates and the frozen seed. Report event count and independent block count. Do not infer future accuracy from a single point estimate or aggregate unrelated sports/families. A miss can be well-calibrated; a win can come from a bad process.

## Prospective evidence and admission

`eligibility.py` validates native cached event bodies, content hashes, exact identity/endpoint, registry/model qualification, input/distribution joins, source independence and time ordering. Valid-looking CSV booleans do not count. Issue requires fresh pregame sources with cutoff strictly before issue and issue before verified scheduled start. Final scoring additionally requires a supported actual-start field and three independently audited terminal lineages.

`ledger.py` records frozen universe registration, abstention, issue preparation/commitment and append-only settlement revisions in a hash chain. `pilot.score_events` validates those records and frozen Part 6 projections, derives the contract outcomes and probabilities, and emits exclusions for every omitted event. No current canonical live issue exists.

`pilot.freeze_lock` refuses a retrospective or overwritten lock and pins the model/source registries, exact registered baseline definition/code, universe, power plan and ledger head. `decision` enrols the chronological issued cohort, waits on unsettled earlier members and records a single interim even if a batch passes its exact count. Futility is terminal across future reads. Final decisions report paired card-vs-model and model/card-vs-baseline results. The current template is NOT_FROZEN; the live composite families and requisite power evidence are absent.

## Historical learning

`research/data/processed/legacy_learning/contracts.csv` preserves all 2,004 rank-log rows; `cards.csv` covers all 522 IDs. It retains 630 literal probabilities and marks unresolved or disputed fields. It never fills absent cutoffs, baselines, event IDs or endpoints. Brier values there are explicitly literal-grade diagnostics. They cannot establish source truth, prospective calibration or incremental baseline skill. Every historical row remains performance-ineligible.

## Release and failure policy

Qualification is model-version/family/endpoint specific. A new model needs fresh qualified evidence, source lineage audit, checked temporal features and at least 50 unique prospective shadows spanning at least 28 days. A different sport starts with league-specific endpoint/source adapters and a simple baseline before complex models. Archive completeness is measured as verified event coverage, not files created.

Classify every learning case as one or more of: data/source/identity, contract/period, timing/availability, model/calibration, research adjustment, true random miss, and unresolved/censored. Review successes under the same checks. Append a versioned hypothesis and acceptance criterion before changing a model; evaluate it chronologically against a fixed baseline. Do not edit an old forecast to make a repair look successful.

Baseline provenance is mandatory for certified admission: exact lane/league/endpoint/families/version, a pinned approved definition and code artifacts, approval strictly before cutoff, and matching distribution/holdout/shadow/pilot comparator. Hash joins verify retained bytes and declared metadata; they do not independently prove every declared input availability time or recompute every distribution. Review the original source field and baseline construction. The point-in-time feature filter likewise labels declared metadata and cannot confer live admission by itself.
