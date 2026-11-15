# Audits on request at any count (AUDIT-ANYTIME-v1)

MDS-2026.11.15-v24.19 / CR-2026.11.15-R3 / P-2026.11.15-v24.17 / SCV-2026.11.15-v15.
Base main: 9259aad8619be5dca7964c394381635ae278b5e2.

Owner instruction, 15 November 2026: "change the rule so that you dont need 100 games or 8 weeks or
whatever to do the comprehensive audit, you can do it anytime".

## What changed

| Gate before | Now |
|---|---|
| Prompt 6 COMPREHENSIVE review described as "about 300 newly settled unique games"; INTERIM about 100 | Prompt 6 runs on the owner's request at any level, including COMPREHENSIVE, at any number of settled games. The learning-status counts are reminders only. |
| Prompt 6: "Fewer than eight weeks is INSUFFICIENT_EVIDENCE" | The eight-week floor limits only a week-based model-release decision, never whether or how fully the audit runs. |
| ASSESS-100: the paired assessment is READY only at the first 100 eligible games | `python -m ml external evaluate ... --on-request` audits every eligible settled paired game available now, at any count, with status AUDITED_ON_REQUEST and decision window ON_REQUEST_ALL_ELIGIBLE_TO_DATE. |

## What did not change

- Promotion is still decided only on the frozen first-100 cohort. An on-request audit never returns
  PROMOTION_ELIGIBLE, so repeated looks cannot be used to stop when results look favourable.
- FREEZE-v1, eligibility rules, the scoring definitions, forecasts, models, settlements and canonical IDs.
- Small-audit findings are registered as hypotheses, not fitted as parameters.

## Files

- Code: `ml/external_evaluation.py` (`on_request`), `ml/research_intake.py` (`--on-request`),
  `ml/learning_status.py` (docstring only).
- Tests: `ml/tests/test_audit_anytime.py` (21-game audit, all games beyond 100, promotion suppression,
  no mixing with `--cohort`, CLI flag, rule text).
- Rules: CORE, SCORING_AND_VALIDATION section 14, RULES_REFERENCE, ML_PIPELINE, EXTERNAL_RESEARCH_PROTOCOL_V3,
  HYPOTHESIS_REGISTER, research/external/EVALUATION_PLAN_v24.19.md (supersedes v24.16 by adding on-request
  audits), indexes, CURRENT_STATE, CHANGELOG; prompt 6 text; all prompt files restamped to P-2026.11.15-v24.17.
- Originals: [archive/superseded_2026-11-15-3](../../../archive/superseded_2026-11-15-3/ORIGINALS.csv)
  holds the exact committed bytes of the 34 changed documents.

## Validation

Full suite on these exact files: 942 passed, 0 failed (950 s). The archived originals match ORIGINALS.csv.
