# BK-OT-1: basketball lines include overtime — MDS/P v24.1 / CR-2026.11.07-R1

**Owner instruction, 7 November 2026:** "all basketball games have overtime inclusive lines, so do it accordingly, if this hasnt been included in the rules, then include it now". Class: DEFINITION + PROCEDURE (settlement convention). No statistical method, fitted value, probability, rank or original card changed.

**Before.** RULES_BASKETBALL BK-P4 made the endpoint the operator's: "Regulation or including overtime for every total, spread and team total", with `UNKNOWN_DEFINITION` when the operator's terms were missing. Controls 6 and 13 said to match or settle under the operator's endpoint. A game that went to overtime therefore stayed definition-open, as P-616 did (U-603, grade-changing).

**After (BK-OT-1).** Every basketball line includes overtime: full-game totals, spreads/handicaps, team totals and winner lines settle on the final score after all overtime periods, in every basketball competition. Only a contract whose own text names regulation, a quarter or a half settles on that segment. The endpoint is `FROZEN_FRAMEWORK_CONVENTION`, so no operator term is needed for it. Overtime stays explicit mass in the price, and settlement still reports whether a threshold was crossed in regulation.

| File | Change |
|---|---|
| RULES_BASKETBALL.md | §0.1 BK-P4 row; §0.5 BK-OT-1 paragraph; §6 settlement line; §8.1 BK-P4 row; §8.3 branch BK-B8; controls 6 and 13 |
| CORE.md | Contract-action bullet names BK-OT-1; header method/control tags v24.1 / CR-2026.11.07-R1 |
| CURRENT_RULES.md | New "Basketball endpoint (BK-OT-1)" paragraph |
| README.md | Method and control tags |
| research/prompts/1_sports/BASKETBALL.md | States the endpoint as BK-OT-1 before the competition-rules step |
| research/prompts/external_requests/01_BASKETBALL.md | Replaces "include overtime when the contract includes it" with BK-OT-1 |
| CURRENT_STATE.md, CHANGELOG.md | Release note |

**Versioning.** Method and control move to MDS-2026.11.07-v24.1 / CR-2026.11.07-R1. The prompt suite keeps P-2026.10.22-v24.0, because no prompt changes its steps, outputs or templates: the two basketball prompt files only state the endpoint that the rules now fix.

**Applied to existing records:** [settlement_import_2026-11-07-2](../settlement_import_2026-11-07-2/CANONICAL_IMPORT_REPORT.md). It covers P-616 revision-2 (definition closed, grades unchanged). The other basketball events were already graded on the final score, so their grades stand. Historical cards keep their original text and labels. Their grades were already full-game, and a later settlement applies BK-OT-1 as a settlement convention, never as a rewrite of an issued card.

**Tests.** `python -m pytest ml/tests` before commit (result in the commit message).
