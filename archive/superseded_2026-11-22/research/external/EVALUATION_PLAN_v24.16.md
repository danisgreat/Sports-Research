# Count-based paired research assessment (EXT-EVAL-v2 / ASSESS-100)

Owner instruction, CR-2026.11.11-R4: assessment must be available once 100 games qualify, without waiting eight weeks or any other calendar minimum. This prospectively amends the unstarted EXT-EVAL-v1 assessment policy. Forecast/profile/kit identities remain v24.15; no forecast probability, reference parameter, source clock, issued card or historical experiment is rewritten.

## Trigger and frozen cohort

Assess immediately when **100 distinct eligible fully settled paired games** are available. There is **no minimum weeks, no end-of-week wait, and no minimum elapsed duration**. A hundred games settled in one day can be assessed that day. Before 100, report progress and insufficient paired games.

Eligibility retains pre-exposure SINGLE_RESEARCH and pre-start FULL_FIVE forecasts, identical complete contract keys and evidence horizons, verified effective outcomes, and external publication/source audit. For a game to count, every common numeric contract must have a terminal effective outcome (WIN, LOSS, PUSH or VOID), and at least one common contract must be decisive (WIN/LOSS). Pending or missing outcomes do not let an early settled winning row qualify the entire game. All-push/all-void games remain retained but are not decisive trials. Count games, not picks, chats, imports or contracts.

Choose exactly the first 100 eligible settled games, ordered by the actual availability time of their last terminal common-contract outcome. Event ID breaks equal-time ties. Include games without looking at whether their forecast won. Freeze COHORT.csv and COHORT_RECEIPT.csv. Later audits reuse that exact file with --cohort; changed eligibility or qualification metadata requires an explicit audit, not replacement by another game. Extra games remain retained for separately registered follow-up cohorts. Do not keep enlarging the first cohort until it becomes favourable.

## Comparisons and inference

Forecast identities are unchanged:

1. SINGLE_RESEARCH:v24.15, frozen before external packet/return exposure.
2. FIVE_LANES:v24.15, current accepted FULL_FIVE evidence.
3. REFERENCE:v24.15, independently frozen reference (secondary).
4. BASELINE:v24.15, independently frozen exact-contract league baseline (secondary).

Average paired contract Brier differences within each game, then average games equally. The primary practical improvement remains FIVE minus SINGLE at most -0.01, with a 95% event-level t interval entirely below zero, calibration/coverage checks, proper log-loss reporting and explicit publication/source/dependence audit before any owner recommendation. Baseline/reference comparisons remain secondary and are reported even when unfavourable. No model is automatically promoted.

The event interval assumes independent games. Games sharing dates, teams or competition conditions can be dependent and make that interval optimistic. Report the number of event days and ISO weeks, shared-team/date concentration, scope, exclusions, calibration and log loss. Temporal coverage is a diagnostic, **never a calendar eligibility gate**. An assessment being READY at 100 does not guarantee an advantage; it may report no change, worse results, uncertain evidence or a calibration/dependence limitation. The estimated event count needed to resolve a small effect is a precision diagnostic, not an extra wait-to-assess rule.

The historical week-based inference path remains available for separately registered older model experiments. It is not called as the eligibility gate for EXT-EVAL-v2. No current assessment waits for eight weeks behind the interface.

## Commands and audit

```text
python -m ml external evaluate --forecasts FORECASTS.csv --outcomes EFFECTIVE_OUTCOMES.csv --out NEW_REPORT
python -m ml external evaluate --forecasts FORECASTS.csv --outcomes EFFECTIVE_OUTCOMES.csv --cohort ORIGINAL_REPORT/COHORT.csv --out LATER_AUDIT
```

The command returns assessment_status READY independently of the finding. COHORT.csv contains at most exactly 100 games. LEDGER_EVENT_COVERAGE.csv lists unpaired, incompletely settled and all-push/void cases represented by the supplied ledger; combine it with the request/intake coverage so NO_FORECAST requests absent from that ledger are not hidden. Keep effective-outcome revisions and all original publication evidence. Old logs remain historical audit inputs and cannot retrospectively supply missing pre-start comparison forecasts.

Weekly audited source refreshes retain the same forecast identity. Reduced/six-role, late, exposed, changed-horizon and unpaired cases retain separate denominators. Recent-team candidates remain shadow-only. The 200-card sport-specific availability-effect collection is a separate data requirement, not a calendar or assessment-readiness gate. Predictive improvement remains UNPROVEN until actual data and audits support the specific claim.
