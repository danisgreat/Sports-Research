# Prompt walkthroughs and executed regression coverage

These are manual operating-document walkthroughs, not live game research or executed prompt agents. The separately executed Python regressions are in ml/tests/test_release_integrity.py and the workshop test suite.

| Fixture | Evidence-bound outcome after reading the final prompt |
|---|---|
| 1: blank Upcoming game blocks | All eleven are inactive templates: no allocated ID, invented match or forecast. Fill only the selected sport's input. |
| 1: rugby union request | Own union section and scoring/selection/archive rules; no league rules or 13-player starter assumption inherited. League has its separate section. |
| 1: obscure competition, provider missing bench | Official match record, both teams, discipline/medical, original team sheets, local-language organizer/club discovery and final release-window check required. Missing provider data does not end research. |
| 1: lineup genuinely unpublished after full search | Exact unconfirmed field and completed searches retained, supported scenarios or qualitative/NO_FORECAST. No fabricated CONFIRMED label. |
| 1: current injury verified after initial pricing | Reconcile actual selection/role, re-price changed inputs before freeze, avoid double counting. Prior-probable information is not confirmed. |
| 1: model result seen before manual freeze | Independence gate fails; cannot label the manual card independent. No silent copying or assistance. |
| 2: mini/start ID conflicts with current state | Read actual current allocation and outstanding local sequence; block allocation, preserve request; old log opening header cannot settle current disagreement. |
| 2: clean new mini | New format, custody/intake/lease and next-ID fields; no issued pick or model read. |
| 3: missing away final or operator action terms | Sporting and operator gates separate; unresolved fields stay unresolved. No VOID or guessed LOSS. Code regression independently checks missing final. |
| 3: terminal card with historical format | Preserve exact frozen source and format; append permitted settlement revisions; no original-probability or baseline backfill. |
| 4: exact existing import and later new addendum | Skip exact original, map/import new addendum separately without consuming an ID; complete source inventory still required. |
| 4: partial core or destination growth | Stop dependent append and re-plan scoped recovery; complete prefix/readback identities remain required. |
| 5: repeated rollover request | Resolve active pointer and prior closure idempotently; no duplicated part, card or ID advance. |
| 6: attractive Hit@2 without same-row baseline | Report construction, coverage and evidence limits; no predictive-skill certification. Decision lab excluded. |
| 6: missing independent model receipt | Diagnostic/excluded sporting comparison, with explicit reason and retained inventory; no prospective relabel. |
| 7: strong label inherited from league name | Reject admission until exact source fields/rows/known-at evidence is established; retain real missingness and invalidate affected model claims. |
| 7: observed zero vs blank | Preserve zero; blank remains missing; no healthy-roster, stage/date or score default. |
| 8: changed source during model run | Completion receipt guard rejects; preserve diagnostic/old artifacts, rerun from stable source. Executed positive and negative regression. |
| 8: favorable historical candidate | Scope-specific registered prospective design/source/calibration gates required; no automatic REFERENCE/ANCHOR promotion. |
| 8: user-authorised main publication | Review scope, stage exact paths, non-force commit/push, fetch and compare actual remote SHA and committed artifacts before claiming publication. |

Executed new regressions cover certainty-loss limits, exact behaviour probabilities, invalid contexts/sample counts, real commit receipt retrieval, all-event-start reveal, uncommitted receipt changes, partial/duplicate finals, freeze input/timing rejection, same-day delayed feedback and generating-source changes. Existing tests cover grid/contracts, chronology, model fits, calibration helpers, readers, decision mechanics and lane controls. All 60 pass; this does not establish source truth, prediction skill, a live lane, execution realism or future profit.
