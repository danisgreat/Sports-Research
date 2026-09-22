# Sports Scoring Specification v3

Effective: 2026-07-16  
Status: CANONICAL SPECIFICATION  
Operational status: **SUSPENDED — NO ACTIVE MODELS**  
Scoring-spec version: `SPORTS_SCORE_V3_20260716`

This file fixes score definitions before any v3 result exists. Lower Brier/log loss is better. Scoring a historical legacy row under these formulas does not make its missing cutoff/model/source evidence valid.

## 1. Evaluation units and eligibility

### Proper-score eligible

A row is `ELIGIBLE_V3` only if it was an ISSUE and all of the following are true:

- immutable request, snapshot and prediction IDs exist;
- primary question and complete pre-outcome candidate universe are frozen;
- exact ACTIVE model/coverage scope and artifacts passed at issue time;
- full mutually exclusive/exhaustive outcome branches reconciled before the event/state advanced;
- cutoff/source/uncertainty gates passed;
- settlement references the exact stored convention and branch;
- scoring uses the registered scoring-code and scoring-spec versions.

WATCH and PASS have no proper score because they contain no forecast probability. They remain in request coverage, abstention and source/model-failure denominators.

### Excluded

- `LEGACY_UNVERIFIED_SNAPSHOT` is always `EXCLUDED_LEGACY`.
- Contract, cutoff, leakage or incomplete-outcome-space failures are excluded from forecast-skill metrics and separately counted as control failures.
- An administrative VOID outside the model's declared outcome space is `EXCLUDED_VOID` but remains in coverage. If VOID was a declared forecast branch, it is scored normally.
- PENDING/UNGRADABLE remains out of proper-score aggregates until resolved; counts are always reported.

Eligibility rules and denominators are frozen before report generation. Analysts may not omit difficult settled forecasts.

## 2. Outcome-space rules

For one prediction, define `K` mutually exclusive and exhaustive branches with full-precision probabilities `p_1...p_K` and observed indicators `y_k`, where one `y_k=1` and the rest are zero.

- Branch probabilities must each be in `[0,1]` and sum to 1 within `1e-9` before display rounding.
- Non-structural model probabilities must be strictly inside `(0,1)`.
- Whole-number markets include a separate PUSH branch.
- A foreseeable/contractual VOID branch is separate; its probability is never duplicated on both selections.
- Overlapping candidates have separate outcome spaces and are never forced into one probability sum.
- A rules-mandated structural zero/one is labelled structural and excluded from model-skill claims; a malformed/impossible market is a contract failure, not an easy win.

The user-facing `decision_probability` for a selection is the sum of its WIN branch probabilities. It is unconditional: do not silently renormalize away PUSH/VOID mass.

## 3. Brier loss

### Canonical binary-compatible multiclass Brier

For K branches:

`Brier_K = 0.5 * sum_k (p_k - y_k)^2`.

This is one-half of the categorical quadratic loss. The positive constant scaling preserves strict propriety, equals the conventional binary Brier `(p_win-y_win)^2` for K=2, and keeps the worst possible loss at 1 for every K. The former `1/K` scaling is prohibited because it mechanically reduced the scale as branches were added and made PUSH/VOID markets incomparable with binary markets.

Do not compare a differently normalized multiclass Brier without conversion and an explicit version. Compute at stored full precision; rounding is display-only.

## 4. Log loss

`LogLoss = -log(p_observed)` using the natural logarithm.

No hidden clipping is allowed in the canonical primary score. If the observed branch has probability zero, canonical log loss is positive infinity. An implementation may calculate a separately labelled finite diagnostic using a preregistered epsilon for numerical plots, but it must retain the raw probability and infinite canonical score.

## 5. Baseline comparison and skill

Model and baseline must have the identical event/candidate eligibility set, branch definitions and weights. Report:

- `score_delta = baseline_score - model_score` (positive favours model);
- `skill_descriptive = 1 - model_score / baseline_score` when baseline score is positive;
- paired event-level score differences with preregistered uncertainty;
- raw model and baseline scores, unique event count, cluster count and effective N.

The paired score difference—not a skill ratio—is the promotion estimand. Skill ratios are descriptive only: they can be unstable near a zero baseline and skill scores are generally not themselves proper scoring rules. Choosing the best baseline or metric after viewing results is prohibited. In PRICE_ENABLED mode the no-vig market comparator is additional; it does not replace a credible naive model baseline.

## 6. Aggregation and dependence

1. Score each unique eligible `forecast_distribution_id` once. Opposing or overlapping candidates that map to the same frozen outcome distribution do not create extra proper-score observations.
2. Identify the primary user question separately from secondary/model-selected candidates.
3. Preregister the point-estimate unit and production-opportunity weights. Report primary-request, decision-level and equal-event summaries when they answer different questions; do not let the number of generated candidates silently determine weight.
4. Use paired event-level cluster bootstrap or an appropriate paired block method for model-baseline differences. Clustering controls uncertainty; it does not silently redefine the point-estimate estimand.
5. Add participant/time/competition blocks when residual dependence remains; card ID never substitutes for event ID.
6. Report exact model version, sport, competition, market family, settlement, forecast state, state/horizon bucket and selection mode. No pooled all-sport calibration KPI.

Nested forecast updates are separate predictions at distinct states but must not be treated as independent. Segment them by state/horizon and cluster by event/series as declared.

## 7. Candidate-selection pipeline

For `MODEL_SELECTED` forecasts, report the full frozen universe:

- candidate count, eligible count, selected count, rejected/pass count and reason distribution;
- ISSUE/WATCH/PASS coverage;
- proper-score distribution for every unique market outcome distribution generated by the registered production pipeline, not only published selections;
- performance of the predeclared selection rule on untouched/shadow data;
- primary requested-question performance separately.

Candidates map to one or more winning branches through the frozen candidate-to-branch bridge. Exact complements share a single `forecast_distribution_id`; candidate marginals may be displayed, but the distribution is scored only once. If rejected candidates lack a forecast distribution, do not fabricate one. Report selection coverage and evaluate the entire production decision policy using its preregistered metric. A published hit rate alone is never selection-pipeline validation.

## 8. Calibration and reliability reporting

- Preserve raw and decision probabilities.
- For K>2, calibrate the joint vector with a simplex-preserving method or a validated coupling step; independently calibrated one-vs-rest branches that do not reconcile are invalid.
- Select the calibration method and its hyperparameters inside development/tuning. Fit the frozen method on the later calibration partition and do not choose it after viewing test or shadow outcomes.
- Freeze bin edges or adaptive-bin algorithm before evaluation; show count and uncertainty per bin.
- Report calibration intercept/slope where appropriate and state the model/segment/sample limitations.
- Report sharpness/resolution as the distribution and spread of issued probabilities at the preregistered coverage level; sharpness never substitutes for calibration or baseline skill.
- Use event/block resampling for uncertainty.
- Do not call a model calibrated from mean predicted versus observed frequency in a small/mixed sample.
- Do not pool pregame-projected, pregame-confirmed or live state/horizon buckets without validated hierarchical calibration.

## 9. Count and continuous targets

The model card preregisters a strictly proper full-distribution score such as log score, CRPS or RPS. A model-family deviance that assesses only a conditional mean is diagnostic, not the primary distribution score. Also report:

- predictive interval coverage and width at declared levels;
- relevant tail probabilities/calibration;
- MAE/RMSE only as secondary summaries of point forecasts;
- event/block uncertainty and identical baseline eligibility.

Predictive outcome interval coverage is distinct from uncertainty in the estimated probability.

## 10. Price, EV and execution metrics

Quoted selections and settlement branches are different objects. A complete quote set contains every opposing side the venue actually prices under the same line and rules. PUSH/VOID may be refund settlement states without a standalone quote.

For a complete set of quoted decisive sides, raw implied probability is `q_i=1/d_i`; the proportional no-vig comparator is `q_i/sum(q_j)`. Any other de-vig method requires a registered version and validation. The snapshot stores `no_vig_estimand` and `conditioning_event`.

If PUSH/VOID is possible but unquoted, the proportional two-side comparator estimates probability conditional on action/decisive settlement. Compare it with the like-for-like model quantity `p_win/(p_win+p_loss)`. An unconditional market comparator is permitted only when a preregistered source/model supplies the refund-state mass; label that comparator hybrid and retain its provenance. Never subtract a conditional no-vig probability from an unconditional `decision_probability`. No-vig probability is a market comparator, not truth or model calibration.

Expected return is calculated over all outcome branches:

`EV_per_unit = sum_b p_b * net_profit_per_unit_b`.

For standard fixed odds before commission:

- WIN net payoff = `d-1`;
- LOSS net payoff = `-1`;
- PUSH/VOID net payoff = `0`;
- hence `EV = p_win*(d-1) - p_loss`.

The shortcut `p*d-1` is allowed only when `p_loss=1-p`, PUSH/VOID probability is zero and commission is zero. Price edge, EV point estimate and EV interval use the immutable contemporaneous market snapshot and declared de-vig/payoff method.

Realized yield/P&L require an authorized execution. CLV requires the accepted execution price and a valid comparable closing snapshot plus a preregistered CLV definition. Quoted/watchlist prices are not executions. Never infer stakes or returns from confidence labels.

## 11. Settlement corrections and evaluation versions

Settlement corrections append a new settlement version. Re-evaluation appends a new evaluation run keyed by settlement version, scoring-spec version and scoring-code hash. Prior settlement/evaluation artifacts remain immutable. Generated reports identify the exact versions used.

## 12. Canonical test fixtures

Implementations must reproduce these values within `1e-12` unless the expected result is infinity.

| Fixture | Probabilities / observed | Expected Brier | Expected log loss |
| --- | --- | ---: | ---: |
| `SCORE-BINARY-WIN` | `[0.7,0.3]`, WIN | `0.09` | `0.35667494393873245` |
| `SCORE-BINARY-LOSS` | `[0.7,0.3]`, LOSS | `0.49` | `1.2039728043259361` |
| `SCORE-THREE-PUSH` | `[0.55,0.35,0.10]`, PUSH (third branch) | `0.6175` | `2.302585092994046` |
| `SCORE-ZERO-OBSERVED` | `[1,0]`, second branch | `1.0` | `+Infinity` |

EV fixtures:

| Fixture | Inputs | Expected EV |
| --- | --- | ---: |
| `EV-NO-PUSH` | `p_win=.55`, `p_loss=.45`, `d=2.0` | `0.10` |
| `EV-WITH-PUSH` | `p_win=.45`, `p_loss=.45`, `p_push=.10`, `d=2.0` | `0.00` |
| `PRICE-PUSH-CONDITIONAL` | `p_win=.45`, `p_loss=.45`, `p_push=.10`; two quoted sides at `d=2.0` | model conditional win `0.50`; no-vig conditional win `0.50`; conditional edge `0.00` |

For `EV-WITH-PUSH`, the invalid shortcut `p*d-1` equals `-0.10`; this fixture exists to prevent that error.
