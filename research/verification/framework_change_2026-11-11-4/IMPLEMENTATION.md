# ASSESS-100 implementation - v24.16 / CR-2026.11.11-R4

Owner request: assessment can happen at 100 games without waiting eight weeks or another calendar floor. Baseline commit: 4d8bd1771d20974bcbfc7c694a009cd44e95a693. This is an assessment-only amendment: forecast/profile/kit and compared model identities remain v24.15. No numerical forecast or historical record is rewritten.

## Changes

- Remove both calendar barriers: the external selector no longer excludes games in incomplete weeks or waits for eight weeks; its scoring call now explicitly uses an EVENT path that has no legacy week minimum.
- Make the first assessment exactly 100 distinct fully settled eligible paired games. All common numeric contracts must be terminal and at least one must be decisive. Multiple picks/chats do not inflate the game count; missing/push-only outcomes retain explicit exclusions.
- Order eligibility by actual complete shared-contract outcome availability, with deterministic event-ID ties. Later audits can reuse the exact hash-bound original cohort using --cohort. Changed/revised eligibility is an audit problem, never permission to substitute games.
- Average contracts within each game, then games equally. Compute a 95% t interval over event means and report its independent-event assumption. Time coverage, shared-date/team dependence, calibration, log loss and forecast/publication evidence remain diagnostics and audit requirements. READY assessment is separate from a positive finding or model promotion.
- Preserve the old week-based scoring defaults for separately registered historical experiments; the current EXT-EVAL-v2 caller cannot silently inherit their eight-week wait. Frozen ml/core files remain unchanged.
- Publish EVALUATION_PLAN_v24.16, append an owner amendment to the hypothesis register, update the current rule/scoring/prompt/state/index documents and archive their exact originals. New governance version v24.16 and scoring SCV-v13 do not relabel v24.15 forecasts or change kit parameters.

## What changes for the owner

If game 100 has complete valid settlement on Tuesday of the first week, the assessment can run on Tuesday. It does not wait for Sunday or week eight. If the hundredth game still has an unresolved shared contract, retain the pending case and use the first 100 games that genuinely qualify. If the result is inconclusive or worse, report that; do not keep adding outcomes until it wins. Current synthetic checks demonstrate mechanics only; no live predictive advantage is invented.

The full source/contract/timing/publication requirements remain. Only eligible prospective pairs contribute, across any number of minis/combined imports. Existing historical logs cannot create missing comparison forecasts. Subsequent work retains one writer and the same custody rules. [Current plan](../../external/EVALUATION_PLAN_v24.16.md).

Verification results are recorded separately in VERIFICATION.md in this folder.


**Frozen model compatibility:** the new event assessor is ml/evaluation/event_assessment.py. The existing ml/evaluation/prospective.py remains byte-for-byte unchanged, including its old registered week-based defaults and the cycle import-closure hash. The current external evaluator calls the separate event assessor directly. Generated model state stays consistent; no existing bundle is invalidated solely to remove this assessment wait.
