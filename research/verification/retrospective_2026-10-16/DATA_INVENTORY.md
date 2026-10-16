# Data inventory — retrospective 2026-10-16 (P-577 to P-600)

## 1. Scope

Scope was fixed mechanically from prompt 6 before any cohort arithmetic: every canonical ID settled or retained since the last completed retrospective ([retrospective_2026-10-11](../retrospective_2026-10-11/RETROSPECTIVE_REPORT.md), cohort P-557–P-576, which excluded P-577–P-579 as `PENDING_EVENT`). This file was written afterwards, at 2026-10-16T20:30+11:00.

| Item | Value |
|---|---|
| Repository / branch / HEAD | `danisgreat/Sports-Research` · `main` · `bd813b5ab4d2d931d91c1f3971a33d812b281cb9`, equal to `origin/main` after fetch; working tree clean apart from the unrelated `.gitignore` edit and untracked sync/editor files, all out of scope |
| Authority | LOCAL_WORKING_TREE · MDS-2026.10.16-v19.1 · CR-2026.10.16-R5 · SCV-2026.10.16-v11 · SEL-2026.10.12-v3 · P-2026.10.16-v19.1 · LEARN-2026.10.16-v1 |
| Trigger | User request. `python -m ml learning-status` gives INTERIM and COMPREHENSIVE `NOT_DUE` (0 store games: no cohort card carried a RESEARCH_EXPORT and nothing has been ingested). 22 newly terminal cards, below the 30-card trigger |
| Event dates | 2026-10-11 to 2026-10-16 (scheduled starts, UTC); ISO weeks 2026-W41 and 2026-W42 |
| Policies and formats | C1 pre-v10 carryover cards (mini-log-5 lineage, full-ladder P_ORDER); C2 v10 cards (mini-log-6, BASELINE_P column); C3 `SUPPLIED_FIRST_V1 / SF-2` (mini-log-7, user-local policy, never pooled with P_ORDER_V2); L legacy retained research P-590–P-600 (RETAIN-v1, `NOT_VERIFIED_PRIMARY`, analyst diagnostics only) |
| Included, counted | C1 P-577–P-579; C2 P-580–P-582; C3 P-585–P-589: 11 cards, 22 primary rows, 44 numeric rows |
| Included, separate | L P-590–P-600: 11 events, 46 supplied propositions (37 numeric decisive analyst rows), never counted as primary |
| Included, qualitative | P-583 `NO_FORECAST` (terminal KT 4–2 Samsung; box-source conflict open) |
| Excluded | P-584 `PENDING_EVENT` (no verified terminal result) |
| Timing strata | Before the scheduled or estimated start (actual start unverified): P-577, P-582, P-583, P-585, P-594, P-599, P-600 (7). After the scheduled start: P-578–P-581, P-584, P-586–P-591, P-593, P-596–P-598 (15). Unverified: P-592, P-595 (2). No card is a certified prospective pre-start issue |
| Gate | C1/C2: 6/6 `RANK1_UNSTABLE`. C3 supplied-scope gate: 4 `RANK1_UNSTABLE`, 1 `FAIL_FLOOR`. Legacy P-591 `PASS_NUMERIC_UNCALIBRATED` (not primary) |
| Original baselines | Numeric BASELINE_P on 8 of 22 decisive primary rows (P-581, P-582, P-587, P-589) |
| Comparison cohorts | P-557–P-576 (prior new cohort) and P-126–P-556, from the 2026-10-11 report, unchanged |
| Model lanes | PRIMARY_HEDGE_MIX_V3 executions 0 of 24; prospective model shadows frozen 0; decision lab excluded |
| Prior exposure | Outcome-exposed retrospective. The analyst read the three import reports (with their packet totals) before computing; those totals were then reproduced independently from the row inventories (§3) |

## 2. Reading receipt

```text
READING RECEIPT
Repository / branch / HEAD SHA: danisgreat/Sports-Research · main · bd813b5ab4d2d931d91c1f3971a33d812b281cb9 · read 2026-10-16T19:40–20:30+11:00 (LOCAL_WORKING_TREE)
Read: research/prompts/6_COMBINED_LOG_RETROSPECTIVE.md (as supplied by the user, identical to v19.1) · COMMON_OPERATING_PROTOCOL · LEARNING_PIPELINE_PROTOCOL §§6–8 ·
      CURRENT_STATE · CURRENT_RULES · SCORING_AND_VALIDATION · HYPOTHESIS_REGISTER (FC10 rows, Retrospective 2026-10-11, timing and primary amendments) ·
      PRIMARY_PREDICTION_PROTOCOL · RESEARCH_RETENTION_PROTOCOL · research/scoreboard/SCOREBOARD.md (current sections)
Latest completed retrospective: research/verification/retrospective_2026-10-11/RETROSPECTIVE_REPORT.md (full)
Settlement/import evidence: mini_import_P-577_P-584_2026-10-13-1 (CANONICAL_IMPORT_REPORT, UNRESOLVED_POST_IMPORT, IMPORTED_ROW_INVENTORY.csv, HISTORICAL_PRIMARY_RECONCILIATION.csv);
      mini_import_P-585_P-589_2026-10-14-1 (CANONICAL_IMPORT_REPORT, IMPORTED_ROW_INVENTORY.csv, EXPECTED_SCORE_READBACK.csv);
      mini_import_P-590_P-600_2026-10-16-1 (CANONICAL_IMPORT_REPORT, UNRESOLVED_POST_IMPORT, EFFECTIVE_SETTLEMENT_ROWS.csv)
Original cards and settlements: prediction logs/PREDICTION_LOG_COMBINED_7.md lines 7470–13212 (card headers, decision blocks, gate/joint lines, A9 audits, settlement revisions and Rank-1 deep reviews; key lines extracted by a read-only helper, not every appendix paragraph read in full)
Learning layer: python -m ml learning-status (store empty), research/model_registry/MODEL_REGISTRY.csv, research/model_shadow (no freeze receipts for these events)
Not read in full: every A1–A9 appendix paragraph of the 24 cards; external source pages (no sporting source re-fetched in this review)
GitHub fallback: not needed (all required files locally complete)
```

## 3. Inventory and sources

| ID | Sport / competition | Cohort | State | Original block (Part 7 lines) | Effective settlement source |
|---|---|---|---|---|---|
| P-577 | Tennis / ATP Shanghai | C1 | SETTLED | 7470–7592 | Part 7 9663–9712 (revision-1), evidence B |
| P-578 | Basketball / NBA preseason | C1 | SETTLED | 7594–7726 (+ addendum 7845) | 9713–9752, A |
| P-579 | Basketball / Liga ACB | C1 | SETTLED | 7728–7843 | 9753–9792, A |
| P-580 | Ice hockey / Czech Extraliga | C2 | SETTLED | 8721–8868 | 9793–9832, A |
| P-581 | Soccer / Danish Superliga | C2 | SETTLED (corners field task open) | 8870–9022 | 9833–9882, A |
| P-582 | Soccer / Premier League | C2 | SETTLED (corners definition task open) | 9024–9207 (+ addendum 9538) | 9883–9922, A |
| P-583 | Baseball / KBO | NO_FORECAST | TERMINAL, box conflict open | 9209–9377 (+ addenda 9557, 9569) | 9923–9959, B |
| P-584 | Soccer / Liga Premier Serie A (MX) | excluded | PENDING_EVENT | 9379–9536 (+ addendum 9621) | 9960–9997, not terminal |
| P-585 | Tennis / ATP Shanghai | C3 | SETTLED | 9998–10193 | 11164–11226, B |
| P-586 | Basketball / EuroCup | C3 | SETTLED | 10196–10335 | 11227–11280, B |
| P-587 | Ice hockey / NHL | C3 | SETTLED (two PUSH informational rows) | 10338–10566 (+ shadow addendum 10569) | 11281–11334, A |
| P-588 | Basketball / NBA preseason | C3 | SETTLED | 10589–10855 | 11335–11387, B |
| P-589 | Ice hockey / NHL | C3 | SETTLED | 10858–11161 | 11388–11449, B |
| P-590–P-600 | Cricket, basketball ×6, soccer, tennis, ice hockey, NFL | L | Terminal sporting reviews; P-596 Saryarka ML and P-598 Huima −8.5 ML UNKNOWN_DEFINITION | 11450–13212 | EFFECTIVE_SETTLEMENT_ROWS.csv (46 rows) and the grouped documentary settlement corpus in Part 7 |

Row-level inputs are reproduced in [COHORT_TABLES.md](COHORT_TABLES.md) §0. Independent reproductions of the import reports: C1+C2 primary 10W/2L, Brier 0.136673655, log loss 0.442657664 (import 2026-10-13: identical); C3 primary 5W/5L, Brier 0.236405693, log loss 0.665503988, paired 4 rows +0.022155049 (import 2026-10-14: identical); legacy 37 analyst rows MSE 0.2860831242, log loss 0.7704050975 (import 2026-10-16: identical to rounding).

## 4. Open queues carried (not resolved here)

P-584 terminal result; P-583 4–2 versus 4–1 box conflict; P-581 corners owner corroboration; P-582 corners field/operator definition; P-596 and P-598 contract definitions; P-598 and P-600 field-owner result confirmation; operator action terms for all 24 events; verified final wall-clock (and therefore 72-hour SLA) for every terminal record; P-596's full original A1–A9 draft (never supplied). This review fetched no source and closes none of them.
