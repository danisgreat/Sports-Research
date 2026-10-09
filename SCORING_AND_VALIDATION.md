# Scoring and validation

**Local authority and all-log reconciliation (October 5):** Local working files govern; GitHub main publishes them. The latest user instruction supersedes earlier GitHub-only prompts. Current [all-log evidence](research/verification/all_log_resolution_2026-10-05/REPORT.md) accounts for all 537 slots and temporary aliases, ten repaired documentary mappings, four new sporting reviews and 53 precise carryovers. Existing IDs and frozen forecast/source bytes remain unchanged.

**October 1 v7.1 clarification:** Calibration, model qualification and prospective cohort controls determine the claims that may be made about performance. They do not prevent requested research, qualitative ranks, transparent uncalibrated analyst scenarios, late/live analysis or canonical IDs in the active combined log. See CURRENT_RULES.md and research.operations.log_card. Preserve original forecasts and score each appropriate cohort separately. No retrospective when the user has deferred it.

Current scoring: **SCV-2026.10.09-v4** (adds the October 9 top-two counting rule below; SCV-2026.10.01-v3 definitions otherwise unchanged). [CURRENT_RULES.md](CURRENT_RULES.md) controls admission. This file defines measurement; historical cards retain their original conventions.

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

`ledger.py` records frozen universe registration, abstention, issue preparation/commitment and append-only settlement revisions in a hash chain. `pilot.score_events` validates those records and frozen ledger-selected projections, derives the contract outcomes and probabilities, and emits exclusions for every omitted event. No current canonical live issue exists.

`pilot.freeze_lock` refuses a retrospective or overwritten lock and pins the model/source registries, exact registered baseline definition/code, universe, power plan and ledger head. `decision` enrols the chronological issued cohort, waits on unsettled earlier members and records a single interim even if a batch passes its exact count. Futility is terminal across future reads. Final decisions report paired card-vs-model and model/card-vs-baseline results. The current template is NOT_FROZEN; the live composite families and requisite power evidence are absent.

## Historical learning

`research/data/processed/legacy_learning/contracts.csv` preserves all 2,004 rank-log rows; `cards.csv` covers all 522 IDs. It retains 630 literal probabilities and marks unresolved or disputed fields. It never fills absent cutoffs, baselines, event IDs or endpoints. Brier values there are explicitly literal-grade diagnostics. They cannot establish source truth, prospective calibration or incremental baseline skill. Every historical row remains performance-ineligible.

## October 5 diagnostic cohort

P-527–P-537 retain eleven completed-game diagnostic reviews, not certified prospective outcomes. Missing literal probabilities/baselines make Brier/log loss and adjustment improvement NOT_COMPUTABLE; ordinal ranks, duplicated rows, alternative versions and complementary picks do not create extra trials. P-537 first-half and corners rows remain unresolved. The [carryover](research/verification/closure_2026-10-05/carryover.md) also retains P-523–P-526 custody requirements. No original NO_FORECAST or LATE_RESEARCH state is upgraded.

All eleven retrospective hypotheses are recorded verbatim in [the improvement register](research/improvement_register.json) as PROPOSED_NOT_TESTED. A written acceptance criterion is not a passed experiment; no weights, probabilities or model qualifications change from those proposals.

## Release and failure policy

Qualification is model-version/family/endpoint specific. A new model needs fresh qualified evidence, source lineage audit, checked temporal features and at least 50 unique prospective shadows spanning at least 28 days. A different sport starts with league-specific endpoint/source adapters and a simple baseline before complex models. Archive completeness is measured as verified event coverage, not files created.

Classify every learning case as one or more of: data/source/identity, contract/period, timing/availability, model/calibration, research adjustment, true random miss, and unresolved/censored. Review successes under the same checks. Append a versioned hypothesis and acceptance criterion before changing a model; evaluate it chronologically against a fixed baseline. Do not edit an old forecast to make a repair look successful.

Baseline provenance is mandatory for certified admission: exact lane/league/endpoint/families/version, a pinned approved definition and code artifacts, approval strictly before cutoff, and matching distribution/holdout/shadow/pilot comparator. Hash joins verify retained bytes and declared metadata; they do not independently prove every declared input availability time or recompute every distribution. Review the original source field and baseline construction. The point-in-time feature filter likewise labels declared metadata and cannot confer live admission by itself.

## Versioned fifteen-experiment measurement protocol

[EXPERIMENT-MEASURES-1](research/experiments/protocols_v1.json) implements all fifteen source-bound hypotheses separately from the frozen certified pilot/scoring code. It measures exact contract Brier/log loss, per-target CRPS and 50/80/95-percent interval coverage/score, fixed-bin reliability and paired week-block uncertainty. Composite primary scores use fixed target weights and one score per event. Pushes remain outcome categories. Raw-unit distribution scores remain separate by target. Zero-probability observed outcomes retain an explicit infinite-loss flag; no silent clipping.

The fixed family is fifteen experiments: family alpha .05, per-comparison alpha .05/15, 60,000 paired week-block percentile replicates. Approximate inference requires a source-backed dependence audit. Sample planning uses a separate pilot with at least eight week blocks and a larger anticipated improvement than the minimum worthwhile threshold; the final cohort needs at least twenty blocks and its calculated numeric sample. No numbers or achieved power are invented for currently absent data. All acceptance tolerances remain unfilled until justified. [Full definitions, commands and next steps](research/experiments/NEXT_STEPS.md).

Every registry entry is MEASURES_IMPLEMENTED with experiment NOT_RUN_AT_REGISTRATION. Immutable locks pin evaluator code/runtime, model/input refs and cohort identities. Missing/invalid/pending observations block statistical decisions, and CANDIDATE_FOR_REVIEW never grants performance eligibility or changes an issued forecast. The original fifteen proposal texts and status remain unchanged.

## October 8 full-slate ranking clarification

For binary relevance, NDCG@2 = DCG@2 / IDCG@2; ideal relevance is sorted over the entire frozen ranked slate, including wins below rank 2. Do not compute ideal relevance from only the top two observed rows. Unresolved, push and void slates remain unscored until an applicable policy is frozen; they are not losses. `research.operations.diagnostic_rank` implements this descriptive policy. P-539 and P-548 receive dated corrections, preserving the supplied historical figures in the original mini archive.

## October 9 top-two counting (SCV-2026.10.09-v4)

Rule T2 (CURRENT_RULES.md): **only Rank 1 and Rank 2 can count as a win.**

- **Counted rows.** For each settled card, the live top-two rows are ranks 1–2 graded WIN or LOSS. PUSH and VOID rows are excluded from numerators and denominators; they are never losses. A NO_FORECAST intake has no counted rows.
- **Card class.** `TOP2_ALL_WON` (every live top-two row won), `TOP2_SPLIT` (one of two won), `TOP2_ALL_LOST` (every live top-two row lost), `VOID` (no live top-two row).
- **Primary counting metrics.** Counted wins ÷ live top-two rows; Rank-1 W/L/VOID and Rank-1 win rate over live Rank-1 rows; Rank-2 likewise; Hit@2 = cards with at least one counted win ÷ cards with a live top-two row. Report the event count and never treat the two picks as independent trials.
- **Ranks 3–4.** Graded and retained in a separate *informational* cohort for calibration (Brier/log loss where p exists) and ranking diagnostics. They never enter win counts, win rates or performance statements.
- **Ranking diagnostics.** Wins@2 and full-slate NDCG@2 (October 8 clarification) stay descriptive ranking-quality measures. They are not win counts.
- **Rank-1 failures.** Each one requires the Rule R1 deep retrospection. Cohort reports list every Rank-1 failure with its failure class and tally recurring classes.
- **Evidence grade.** Every settled row records its evidence grade (A/B/C/E/OP/X). Cohort reports give counts by grade, so best-available (C) and estimated (E) settlements stay visible.
- **Reference implementation.** `research/verification/final_settlement_2026-10-09/build/build_settlement.py`.
