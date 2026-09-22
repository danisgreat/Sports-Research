# Audit and changes — 2026-07-17

Status: **COMPLETED DOCUMENT REDESIGN**

## 1. Scope

The redesign reviewed the seven user-nominated legacy files and the more recent v3/v5 framework material:

- `AUDIT_AND_CHANGES_2026-06-12.md`
- `combined_sports_doc_v2.txt`
- `POISSON_DISTRIBUTION_AND_SIMULATION_FRAMEWORK.md`
- `PREDICTION_RESULTS_LOG_v2.md`
- `PREDICTION_RESULTS_LOG_v3.md`
- `SPORTS_CALIBRATION_LEDGER_v2.csv`
- `SPORTS_SOURCE_REGISTRY_v2.md`

The originals remain unchanged in `archive/pre_audit_20260716/`. This audit does not certify their historical performance.

## 2. What was useful and retained

- Strong insistence on event identity, market terms, recency, lineups, weather and source quality.
- Sport-specific mechanisms rather than one universal model.
- The principle that Poisson is a baseline and must be challenged by dispersion/dependence and sport-native alternatives.
- Retrospective lessons about exact-winner overconfidence, phase/full-game mismatch, totals stacking, opponent suppression, late-game tails, wicket clusters, bullpen fatigue, territory dominance and unstable rotations.
- A copy-friendly prediction log and explicit source registry.
- The instruction not to grade a previous event while it remains live.

These ideas were consolidated, deduplicated and rewritten with clearer claim boundaries.

## 3. Material integrity problems found

The historical headline record cannot be treated as verified model performance.

- The audited legacy CSV contained 437 rows; 300 rows (68.6%) belonged to exact complementary pairs across 75 of 102 cards.
- At least 37 four-selection cards consisted entirely of two complement pairs. Their aggregate resolved record was approximately 73-73, with two unresolved outcomes, which is structurally near a forced two-win/two-loss result rather than four independent predictions.
- Totals and opposite handicaps were sometimes scored as if they were independent selections.
- User-supplied options, analyst-selected recommendations, comparison branches, live calls and pregame calls were mixed.
- The old top/bottom penalty system optimized a custom ranking score rather than a standard probabilistic objective.
- Some confidence labels conflicted with numeric values, and confidence was not prospectively calibrated.
- Rows could be mutable, allowing result leakage or later reinterpretation.
- Price, bookmaker, timestamp, stake, commission and fill were missing, so ROI/yield/profitability cannot be reconstructed honestly.
- At least one legacy settlement description contradicted its row status.

Accordingly, all legacy hit-rate or profit claims are classified `LEGACY_UNVERIFIED`. The data may support hypotheses, not current accuracy claims.

## 4. Research-based corrections

The revised framework follows three general principles from forecast-evaluation research:

1. Calibration is a relationship between predicted probabilities and observed frequencies; it requires careful assessment, not verbal confidence bands.
2. Sharp forecasts are desirable only subject to calibration, and proper scoring rules are preferable to raw hit rate.
3. Data leakage and non-independent train/test construction can produce inflated performance; evaluation must reproduce the information actually available at prediction time.

These principles are implemented through frozen cutoffs, time-ordered validation, proper scoring rules, uncertainty reporting and append-only human records.

Research references:

- Vaicenavicius et al., “Evaluating model calibration in classification,” AISTATS 2019: <https://proceedings.mlr.press/v89/vaicenavicius19a.html>
- Gneiting, Balabdaoui and Raftery, “Probabilistic forecasts, calibration and sharpness,” JRSS B 2007: <https://doi.org/10.1111/j.1467-9868.2007.00587.x>
- Kapoor and Narayanan, “Leakage and the reproducibility crisis in machine-learning-based science,” Patterns 2023: <https://doi.org/10.1016/j.patter.2023.100804>

## 5. Operating changes

| Before | Active v4 process |
|---|---|
| Per-request JSON packet/publication workflow | Direct Markdown log plus one CSV ledger |
| Four supplied outcomes could become four apparent picks | Rank all; recommend only evidence-clearing options |
| Complements counted row by row | Tag dependence; no independent-success claim |
| Custom top/bottom scoring | Standard result plus proper probabilistic metrics when eligible |
| Numeric confidence without validation | Qualitative verdict unless publication gate passes |
| Poisson/Monte Carlo could appear universal | Baseline plus challenger and sport-native model |
| Mutable or regenerated history | Original entry preserved; updates and corrections appended |
| Previous result could contaminate next analysis | Settle only verified finals; ignore live/upcoming |
| Source accessibility treated as permanent | Re-test source at every cutoff |

## 6. Files created

- `CURRENT_FRAMEWORK/combined_sports_doc_v4.md`
- `CURRENT_FRAMEWORK/PREDICTION_RESULTS_LOG_v6.md`
- `CURRENT_FRAMEWORK/SPORTS_CALIBRATION_LEDGER_v3.csv`
- `CURRENT_FRAMEWORK/SPORTS_SOURCE_REGISTRY_v4.md`
- `CURRENT_FRAMEWORK/SPORTS_MODEL_AND_SIMULATION_FRAMEWORK_v4.md`
- `CURRENT_FRAMEWORK/README.md`
- this audit file

The current human log migrates recent decisions without converting passes into predictions or adding probabilities after the fact.

## 7. JSON disposition

Per-request packet/publication JSON and unrelated root data dumps were moved into a dated archive, not deleted. This preserves evidence while keeping the active portable framework free of JSON. Technical package/schema/runtime JSON that may be needed to inspect the prior executable prototype remains historical implementation material and is not required by the active process.

## 8. Known limitations after the redesign

- No sport currently has enough audited prospective evidence in this workspace to justify broad calibrated probability claims.
- “Active” baseball, cricket, soccer, AFL and rugby-league modules are qualitative analysis models until their narrow quantitative implementations pass the v4 publication gate.
- The migrated live and upcoming entries remain ungraded unless a final result and market settlement are verified.
- The redesign improves process integrity; it does not retroactively repair old data.

## 9. Next honest development cycle

1. Accumulate prospectively frozen selections with exact lines and cutoffs.
2. Settle from official results without rewriting original entries.
3. Require a useful sample before evaluating calibration or sport/market subgroups.
4. Develop narrow models by competition and market, not a single all-sports probability engine.
5. Compare every model with transparent baselines and publish uncertainty.
6. Suspend a model when data integrity, drift or calibration fails.

