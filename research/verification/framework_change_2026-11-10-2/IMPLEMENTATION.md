# Framework change 2026-11-10-2 — Australian rules request format and finals extra time (MDS v24.12 / CR-2026.11.10-R2)

**Owner instructions, 10 November 2026.** The owner supplied a tenth per-game request format, for Australian rules, with the words "add this as well". Asked whether AFL finals lines include extra time, the owner answered yes.

**Class.** PROCEDURE, plus an endpoint convention. No issued card, grade, probability, rank, canonical ID, method, model, release or selection rule changes. No Python changed. Versions: method MDS-2026.11.10-v24.12, control CR-2026.11.10-R2, prompts P-2026.11.10-v24.10.

## Changes

| Where | Change |
|---|---|
| [GAME_REQUEST_TEMPLATE](../../../GAME_REQUEST_TEMPLATE.md) §1 | The format, verbatim, after baseball. The sentence saying AFL keeps a free-form block now refers to other sports only |
| [GAME_REQUEST_TEMPLATE](../../../GAME_REQUEST_TEMPLATE.md) §1b | One row: family, endpoint and deep-loss-review roles; the owner-convention sentence names AFL-ET-1 |
| [AFL_AFLW sport file](../../prompts/1_sports/AFL_AFLW.md) | The format replaces the free-form Upcoming game fields, as in the other nine sport files; finals note added. The seven-step workflow is otherwise unchanged |
| [DEPENDENCY_MAP](../../prompts/DEPENDENCY_MAP.md) | AFL/AFLW now lists GAME_REQUEST_TEMPLATE |
| [RULES_AFL](../../../RULES_AFL.md) | AFL-ET-1 in §0, AF-B8, the AFL settlement paragraph and the AFLW finals paragraph |
| [RULES_REFERENCE](../../../RULES_REFERENCE.md), [CORE](../../../CORE.md) | The convention, beside BK-OT-1 |
| README, PROMPTS, CURRENT_STATE, CHANGELOG, 22 prompt files | Version strings and release notes |

## How the lines are read

The format covers AFL, AFLW and state leagues; the Competition field selects which, and AFL and AFLW stay separate populations. Home-and-away games run to the final siren of the fourth quarter, with a draw as a live, priced outcome.

**AFL-ET-1.** Every finals line includes extra time, unless its own text names regulation, the end of the fourth quarter, a quarter or a half. The endpoint is `FROZEN_FRAMEWORK_CONVENTION`. Quarter and half lines are unaffected. It is applied to every Australian rules competition whose finals use extra time, as BK-OT-1 applies to every basketball competition. AF-P1 still verifies each competition's finals rules.

## Earlier records

RULES_REFERENCE requires an owner convention to be recorded as a revision for affected earlier records. A search of all nine combined logs found no retained Australian rules final recorded as going to extra time. P-271 and P-638 are recorded as decided without it. So no revision is written and no grade changes. The search matched log text, so it depends on those records having noted extra time had it occurred.

## What the code does not do

`ml.config.SPORT_RULES` keeps `FULL_GAME` with a draw tie rule for Australian rules, because it has no stage field. No release or reference currently prices the finals extra-time branch automatically, so the card prices it by hand as explicit mass. No code changed.

## Custody

Pre-images of GAME_REQUEST_TEMPLATE, the AFL/AFLW sport file, CURRENT_STATE, RULES_AFL, RULES_REFERENCE and CORE are in [archive/framework_change_2026-11-10-2](../../../archive/framework_change_2026-11-10-2/MANIFEST.csv). The CORE and CURRENT_STATE pre-images are from their respective points in this round. No log or mini was touched. Test results are in [TEST_RECEIPT](TEST_RECEIPT.md).
