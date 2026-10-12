# PROMPT 6 — Evidence-grounded Combined Log retrospective

**Mode:** COHORT_RETROSPECTIVE. Run after about 30 newly settled cards or on user request; neither trigger implies statistical sufficiency. Writes: a new uniquely named retrospective folder, scoreboard, CURRENT_STATE, dated HYPOTHESIS_REGISTER additions and CHANGELOG. No log/grade/forecast/rule/prompt changes and no edits to earlier dated reports.

## 1. Read and freeze scope

Print the [reading receipt](README.md) after common controls, scoring, verification, hypotheses, latest completed retrospective and implementation roadmap, relevant learning/source/archive/profile sections, original cards and latest valid settlement evidence. A folder containing an unfinished draft is not automatically a completed retrospective. Record branch/HEAD/dirty inventory.

Before constructing result tables, write SCOPE.md: fixed issue/event dates and IDs, policy/format versions, inclusion/exclusion rules, original-gate/timing/lead/evidence strata, last completed-review boundary, comparisons, snapshot time and outcomes already seen. Do not claim prospective registration for a scope written after exposure. Include all requested/research events in coverage, even pending/NO_FORECAST, while scoring only appropriate resolved rows.

## 2. Build an inspectable inventory

Create DATA_INVENTORY.md and row-level COHORT_TABLES.md. Join each original card to its latest valid dated settlement; retain original contract/rank/p/baseline/expected score and all revision pointers. Reject duplicate counting. Recover an original probability only by reading its actual frozen card, not from a later paraphrase; missing stays missing. Record every omitted metric and reason.

Reconcile all IDs, rows, grades and queue statuses to source blocks before aggregating. Separate original primary picks, informational ranks, frozen shadows, qualitative cards and post-event reconstructions. Respect old scoring/selection versions. Historical totals can remain a labelled diagnostic view; v10 outcomes start with actual v10 cards, not relabelled history.

## 3. Quantitative review

Report every sport, league, format and endpoint present in the cohort, each in its own stratum; never pool unlike competitions, and list strata too small to report with their counts. For each suitable league/format/endpoint/policy cohort report:

1. Coverage: requested events, retained forecasts, numeric/qualitative/NO_FORECAST, pending, unresolved, decisive and paired-baseline counts; missingness sensitivity.
2. Primary W/L/PUSH/VOID/UNRESOLVED by rank, card class and Hit@2 with exact denominators; mechanically protected pairs separately.
3. Baseline-relative Brier and log loss on identical frozen rows, event means and week means, events/weeks, and justified uncertainty. Report NOT_COMPUTABLE when paired data is absent. Realised in-sample climatology is descriptive only.
4. Calibration bins over the full probability range, distinct-event counts, mean p versus outcome, resolution limitations. No proof from an interval merely including p or slope 1.
5. Expected-score bias/MAE/RMSE and issued-interval coverage by sport/term; z only from valid original SDs. Do not infer good tails merely from a small mean |z|.
6. Original gate versus instability and the shadow gate and shadow pairs defined in SELECTION_RULES §2–3 (RET03, RET04, XCARD6), declared alternative/quantity and policy version. Compare outcomes on paired events; a reachable gate is not necessarily useful.
7. Joint-loss predictions versus matching observed endpoints; exact values separate from bounds; pushes/voids conditioned consistently; structural zero acknowledged.
8. Timing/source process: PREGAME/LIVE/LATE/HISTORICAL, actual issue lead, outcome exposure, lineup evidence, provider grade/lineage, source failures, capture completion, review SLA and evidence backlog.
9. Adjusted/unadjusted and sensitivity results, including sub-0.25-SD rank flips, approved regime vocabulary and complete winner masses.
10. Family failure classes and exposure counts, matched wins and process NOT_ASSESSABLE. Zero recurrence without exposure is not a successful correction. A losing high-p row is not by itself evidence of miscalibration.
11. Archive/profile freshness and exact usable coverage; small selected cohorts do not estimate league population shifts. Historical results must precede the relevant issue cutoff.

Use SCORING_AND_VALIDATION for arithmetic and limitations. Same-event dependence, repeated teams, one-week samples, multiple comparisons and non-comparable line difficulty limit inference. Supply a sample-size plan only when its inputs and method exist; otherwise SAMPLE_SIZE_NOT_ESTIMATED. Do not compare raw hit rates across easy derived lines and harder supplied lines as if task difficulty were fixed.

## 4. Review learning and recommend

Read every new Rank-1 loss review and matched wins. Name shared mechanisms and whether knowable at cutoff, but do not invent causal percentages. Review every recommendation in the latest register by separate statuses: document control implemented, data ready, test registered, test run/result and production release. Archived runtime claims do not establish a current implemented model.

Write prioritised recommendations with ID, evidence, concrete change, dependencies/files, operational owner/task, acceptance criteria, justified prospective sample plan, failure/rollback condition and status. Prefer highest-impact correctness/measurement/source repairs first; model/selection experiments remain untested until supported. Append new hypotheses with version/date instead of editing an old registration. Do not force exactly five findings when evidence supports a different number.

## 5. Report and publish

Produce RETROSPECTIVE_REPORT.md with findings, evidence tables, what worked, limits, recommendation status and next tests; retain scope/inventory/calculations. Reconcile every aggregate to the row inventory, then independently recompute representative arithmetic. Update scoreboard/state without changing underlying grades; baseline-unavailable headline stays explicit. Verify allowed scope and unchanged log bytes.

Commit by exact paths and push without force when this prompt is invoked unless user requests local-only. Fetch/verify remote SHA and report artifact. Return scope, paired-data sufficiency, primary descriptive results, unresolved coverage, evidence-supported findings, priority recommendations, report links and publication state. Avoid claims of predictive improvement unsupported by a fixed prospective comparator.
