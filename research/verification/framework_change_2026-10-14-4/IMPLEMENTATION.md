# Implementation — starters, bench and absence research

**Status:** local document procedure implemented; predictive effect untested. **Date:** 14 October 2026. **Scope:** [proposal](CHANGE_PROPOSAL.md). **Protocol:** [AVAIL-2026.10.14-v1](../../../ROSTER_AVAILABILITY_PROTOCOL.md). **Prompt:** [game card](../../prompts/1_GAME_CARD.md). **Verification:** [report](VERIFICATION_REPORT.md).

## Review of the prediction changes

The workshop currently supplies a useful development structure: archive-backed league discovery, coherent distribution engines, baselines, chronological comparison and isolated shadow work. Its README and prior change report explicitly keep model outputs out of cards and label results historical development. The archive loader's opening declaration uses LABEL_B unless stronger admission exists; parsing consistency is not current player-availability evidence.

The inspected prior implementation report still contains `<<RESULTS>>`, and `research/model_shadow/STATUS.md` was absent in this working snapshot. Consequently this review does not claim that all described runs were completed, that models improve prediction, or that the workshop is qualified. No workshop code or results were changed or rerun. The remaining field-owner admission/prospective evidence limitations described in that report still matter.

For active cards, comprehensive availability research addresses a direct input weakness: missing starting roles, unavailable substitutes and unreported absences can distort expected scores, widths and ranks. It should reduce avoidable assumptions. The size and direction of any predictive benefit remain unknown until frozen same-event comparisons are measured. A confirmed bench does not determine minutes; injury absence must not be counted both in source-adjusted statistics and a second unsupported adjustment.

## Implemented changes

| ID | Change | Paths / behaviour | Status |
|---|---|---|---|
| AV-R01 | Mandatory source escalation | ROSTER_AVAILABILITY_PROTOCOL §§1–2; official exact event → both teams → medical/eligibility/discipline → structured fallback → native-language discovery → final recheck | IMPLEMENTED |
| AV-R02 | Separate evidence for starters, bench and absences | Existing Evidence receipt, lineup metadata and A3/A8 hold each field's evidence and uncertainty; membership/probables never establish selection | IMPLEMENTED |
| AV-R03 | Updated source routes | SOURCES §3.11 and protocol §3; current-season navigation, WNBA path, ACB medical reports, NBL injury discovery, A-Leagues, AFC/CAF, FIBA scorer and Korean/Japanese sources | IMPLEMENTED; review labels distinguish O/I/D/B |
| AV-R04 | Obscure competitions | Protocol §4 requires exact organizer, both teams, local scripts/aliases, original team sheets and actual failure/escalation ledger | IMPLEMENTED |
| AV-R05 | Final update and truthful non-publication | CURRENT_RULES §5b and timing paragraph; a failed extraction is not NOT_PUBLISHED; no guarantee of universal pregame disclosure | IMPLEMENTED |
| AV-R06 | All sport requests use the procedure | Ten prompt-1 Evidence sections and all eleven operative RULES_<SPORT> files link the protocol | IMPLEMENTED |
| AV-R07 | Process verification | C20 and VERIFICATION_PROTOCOL distinguish incomplete research from completed research with unconfirmed information | IMPLEMENTED |
| AV-R08 | Authority and navigation | Control R2, suite v11.2 in active surfaces; METHOD, CURRENT_STATE, indexes, README and CHANGELOG aligned | IMPLEMENTED |
| AV-R09 | Compatibility and fixtures | Existing card formats/scoring/selection unchanged; current synthetic examples explain their structural N/A; eighteen manual cases | IMPLEMENTED |
| AV-R10 | Predictive qualification / guaranteed confirmation | No numeric effect claimed; no fabricated lineup, healthy roster, weights, scheduled job or new fitted model | NOT_ESTABLISHED / not promised |

## Versions and preserved scope

**CR-2026.10.14-R2 / P-2026.10.14-v11.2**, revision class PROCEDURE plus source maintenance. Additional research is recorded in existing outputs; method, mini-log-7, mini-settlement-6, selection and scoring stay at their existing versions. Existing in-progress minis finish unchanged. New work that reads these local controls applies the procedure; an external PUBLISHED_MAIN_PINNED run needs these changes published in its pinned revision before it can apply them.

Pre-edit working originals, including prior unpublished workshop amendments, are preserved in [archive](../../../archive/superseded_2026-10-14-4/ARCHIVE_RECEIPT.md). No model code/results, issued logs, grades, P-IDs, datasets, hypotheses or scoreboard are modified. No commit or push was requested/performed. [Exact path and preservation checks](VERIFICATION_REPORT.md) distinguish this delta from the pre-existing dirty tree.

## Source review limits

The protocol's O/I/D/B legend records actual review depth. League homepages, official search results and historic examples establish routes and types of publication, not every current game's lineup. WNBA/NPB/NFL/PL routes and several official organizer examples were checked; direct access failed for a guessed NBA 2026-27 page, wrong WNBA path, an EuroLeague news route and ATP scores. The protocol requires fallback when those fail rather than guaranteeing accessibility.

No live game was supplied for a complete current starters/bench/injury audit. No account was contacted and no restricted access bypassed. Some competitions have no public complete injury report. The enforceable improvement is a complete search, exact field/time evidence and honest disposition for every requested game.
