# Sports research framework — active document set

Status: **ACTIVE from 2026-07-17**  
Operating style: **document-first; no per-request JSON required**

This folder is the portable working framework. Copy this folder when moving the process to another workspace. The older files outside this folder are preserved for audit history, but they are not the current operating instructions.

## Files to use

1. `combined_sports_doc_v4.md` — the full operating manual and sport-specific instructions.
2. `PREDICTION_RESULTS_LOG_v6.md` — the human-readable prediction, live-update, settlement, and retrospective log.
3. `SPORTS_CALIBRATION_LEDGER_v3.csv` — one row per genuine selection or abstention; suitable for analysis.
4. `SPORTS_SOURCE_REGISTRY_v4.md` — source hierarchy and sport-specific source starting points.
5. `SPORTS_MODEL_AND_SIMULATION_FRAMEWORK_v4.md` — model choice, validation, simulation, and probability rules.
6. `AUDIT_AND_CHANGES_2026-07-17.md` — the evidence-based audit and the reasons for this redesign.
7. `AUDIT_AND_CHANGES_2026-07-20.md` — final-state verification, settlement cleanup, and post-game reference updates.
8. `AUDIT_AND_CHANGES_2026-07-23.md` — MLB settlement cleanup and the first-X-ball contract control.
9. `AUDIT_AND_CHANGES_2026-07-24.md` — final closure of V6-016 and the completed-event contract-verification control.
10. `AUDIT_AND_CHANGES_2026-07-25.md` — final closure of V6-017, KBO source reconciliation, and the full-game contract-verification control.
11. `AUDIT_AND_CHANGES_2026-07-28.md` — settlement sweep closing V6-018, V6-019 and V6-020; the index-before-settlement prohibition, the ledger width assertion, and the ranking, winner-lean and contract-capture controls.
12. `AUDIT_AND_CHANGES_2026-07-29.md` — V6-021 settlement and grade; the venue-baseline control's first prospective application; the n=1 venue bat-first/chase-order prohibition in winner cases.

## Normal workflow

1. Read the combined sports document.
2. Check the previous log entry. Settle it only if the event is final and the outcome can be verified.
3. Research the new event using timestamped sources.
4. Produce the card or abstain honestly.
5. Append the complete decision to the Markdown log before delivery.
6. Add one CSV row for each actual selection. Do not count an opposite line as independent evidence.
7. After a final result, append a settlement and retrospective; never rewrite the original forecast.

JSON may still exist in the historical technical archive, but it is not part of the active manual process. A normal request should create or update only the Markdown log and CSV ledger.

## Claim boundary

The framework supports disciplined analysis, not guaranteed winners. A numeric probability is allowed only when a documented model has out-of-sample validation and an applicable calibration record. Otherwise use `SUPPORTED`, `LEAN`, `PASS`, or `AVOID` and state the uncertainty.
