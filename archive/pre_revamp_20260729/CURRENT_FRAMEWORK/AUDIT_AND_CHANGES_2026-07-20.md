# Settlement audit and reference updates — 2026-07-20

Status: **COMPLETED SETTLEMENT CLEANUP**

## Scope

This audit closes every event that was unresolved in `PREDICTION_RESULTS_LOG_v6.md` as of 2026-07-20T08:09:01Z. It verifies final state before settlement, records outcome-neutral closures for prior passes, settles every actual forecast in the CSV ledger, and adds only evidence-supported process references.

## Final-state review

| Record group | Status after check | Treatment |
|---|---|---|
| V6-MIG-001, V6-MIG-002, V6-001, V6-002 | Final | Closed as `NOT GRADED`: each was a documented pass with no formal selection. |
| V6-003 | Final | Fully settled: Diablos 13, Tigres 5. |
| V6-005 | Final | Fully settled: Connecticut 96, Phoenix 83. |
| V6-008 | Final | Fully settled: Collingwood 90, Carlton 69. |
| V6-010 | Final | Fully settled: Chicago White Sox 3, Toronto Blue Jays 0. |

No event remained live, postponed, abandoned, or unverified at the settlement check. Earlier V6-004, V6-006, V6-007, and V6-009 settlements were also reconciled in the open-event index.

## Research and process conclusions

| Sport | What was right/wrong | Persistent reference update |
|---|---|---|
| LMB | Over 17.5 and the Diablos winner won, but the game slowed dramatically after the live snapshot. The adjacent Under 18.5 also won, and both supplied run lines lost at an unprotected eight-run gap. | Store exact alternate-line intervals and model early-score cooling explicitly. |
| WNBA | The 3:36 low-scoring sample failed at every recommended total horizon, and Phoenix never led. | Do not extrapolate a sub-four-minute sample across Q1, half, and full-game totals without possessions, shot quality, and lineup context. |
| AFL | Collingwood side/winner calls were right; the over was wrong. Post-start Carlton injuries help describe the result but must not justify the pregame case. | Keep total views capped without scoring-shot, territory, and conversion evidence; preserve the cutoff boundary. |
| MLB | Chicago side/winner calls were right; the Over 8.0 was wrong as both listed starters performed strongly. | Keep starter quality explicit and do not let an unvalidated rate blend or one volatile outing dominate a total. |

## Integrity conclusion

The ledger now contains no `PENDING` results. Result rows remain calibration-ineligible because the framework has no eligible quantitative probabilities, incomplete price/contract provenance, and several comparison-only/pass rows. These settlements must not be used to claim a hit rate, ROI, calibration, or model validation.
