# Audit closure ledger — 2026-09-25

**Status: CURRENT RECONCILIATION RECEIPT.** This ledger succeeds `AUDIT_RECONCILIATION_ALL_SPORTS_2026-09-21.md` (archived in this folder), which remains the historical supersession map for findings up to 2026-09-21. `METHOD.md` §11 classifies older findings against both documents.

**Method:** MDS-2026.09.19-v4.3. **Control revision:** CR-2026.09.21-3, unchanged by label. The additive integrity controls of 2026-09-24(f) and 2026-09-25 are receipted in `CONTROL_MANIFEST_2026-09-25.md`, following the 2026-09-23 precedent of a content receipt under the same label.

**Written:** 2026-09-24 23:46 to 2026-09-25 about 01:00 AEST, by repository session `sports-research-78`, on the operator's instruction: "fully and carefully implement all aspects from the audits … and if once they have been fully implemented, archive them into a new audit documents folder, and proceed accordingly."

**Performance status:** LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE. Implementing an audit is documentation and tooling work. It is not evidence of predictive lift.

## 1. Rule for "fully implemented"

An audit document was archived here only when **both** of these hold:
- every recommendation that can be implemented in documents or tooling is written into its governing home, and each is listed below with its location;
- every recommendation that needs empirical work (a dataset, a fit, a prospective sample) is recorded in an **active** document with its current status, and is **not** marked complete. Examples: `NUMERICAL_PROGRAM.md`, `H0_DATASET_CARD.md`, and the `LEARNING_REGISTER.md` prospective-test tables.

Recommendations that later evidence rejected or superseded are recorded with that disposition and were not implemented.

## 2. Audit documents archived in this folder

The files were moved with `git mv`; their bytes are unchanged. Their internal relative links refer to the repository root. Active governing documents were updated to point here (see §6).

| Document | Date | Scope | Disposition | Where the implementable content lives | Empirical or open items still tracked elsewhere |
|---|---|---|---|---|---|
| `AUDIT_CHANGELOG_2026-09-05.md` | 09-05 | Settlement-audit changelog | IMPLEMENTED / RECONCILED (CR-2 ledger rows "2026-09-05") | `RULES_GENERAL.md`, sport modules, settlement workflow | Performance-eligibility expansion **SUPERSEDED** (logs remain LEARNING_ONLY) |
| `COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md` | 09-05 | Settlement and blind-spot audit | IMPLEMENTED / RECONCILED | Same | — |
| `FRAMEWORK_AND_GAME_LOG_OVERHAUL_REVIEW_2026-09-06.md` | 09-06 | v4.0 overhaul review | IMPLEMENTED (METHOD v4.x, §16 gate portfolio) | `METHOD.md`, `RULES_GENERAL.md` §16 | — |
| `GAME_LOG_BLINDSPOT_REVIEW_2026-09-06.md` | 09-06 | Blind-spot review | IMPLEMENTED; path-count, pseudo-tail and top-slot findings **REJECTED/SUPERSEDED** (CR-2, CR-3) | `RULES_GENERAL.md` §16.10–16.11; sport CR-3 sections | — |
| `IMPROVEMENT_PLAN_2026-09-06.md` | 09-06 | Improvement plan | IMPLEMENTED or SUPERSEDED per the CR-2 ledger | Same | Control-taxonomy retro-tagging **CLOSED / NOT TO BE DONE** |
| `COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-12.md` | 09-12 | Settlement, push/void and queue audit | IMPLEMENTED (`SCORING_AND_VALIDATION.md`) | `SCORING_AND_VALIDATION.md`, `GAME_LOG_STATUS_CURRENT.md` | Historical queue handles stay open in the status register. Its `audit_2026-09-12/` evidence folder was **never synced to this repository** (no git history) |
| `MODEL_REVIEW_2026-09-17.md` | 09-17 | Model audit | IMPLEMENTED (METHOD v4.1+, SCV, NTS) | `METHOD.md`, `SCORING_AND_VALIDATION.md`, `NUMERICAL_*` | **EMPIRICAL:** H0 dataset NOT BUILT; chronological fit/test; prospective shadow (`NUMERICAL_PROGRAM.md`, `H0_DATASET_CARD.md`) |
| `AUDIT_IMPLEMENTATION_2026-09-17.md` | 09-17 | Implementation ledger for the model audit | IMPLEMENTED | Same | Same. Its `audit_2026-09-17_models/` and `audit_2026-09-17_implementation/` folders were **never synced** |
| `AUDIT_IMPLEMENTATION_2026-09-19.md` | 09-19 | Deep-research gates, R-1, S-1, S-2, top-O/U trigger | IMPLEMENTED | `METHOD.md` §1.1, `CONTROLS.md`, `RECENCY_AND_REBOUND.md`, `prediction_preflight.py` | **EMPIRICAL:** non-MLB `R-1` magnitudes `NOT_YET_DERIVED` |
| `AUDIT_AND_CRICKET_SOURCE_UPDATE_2026-09-21.md` | 09-21 | Cricket toss/strip source audit | IMPLEMENTED (CR-2026.09.21-1) | `RULES_CRICKET.md` §2, `DATA_SOURCE_REGISTER.md` §6A, preflight cricket object | — |
| `AUDIT_IMPLEMENTATION_2026-09-21.md` | 09-21 | CR-1 implementation ledger | IMPLEMENTED | Same | — |
| `AUDIT_RECONCILIATION_ALL_SPORTS_2026-09-21.md` | 09-21 | All-sports supersession map (CR-2) | IMPLEMENTED; **still the historical supersession map**; succeeded by this ledger | `RULES_GENERAL.md` §16.10 (canonical rule set); `METHOD.md` §11 | Its §5 empirical list is unchanged and still pending |
| `AUDIT_IMPLEMENTATION_2026-09-21-CR3.md` | 09-21 | CR-3 live-rule cleanup | IMPLEMENTED | All ten sport modules' CR-3 sections; `METHOD.md` §12 | — |
| `IMPLEMENTED_CHANGES_2026_09_23.md` (+ `.docx`) | 09-23 | Implementation summary of the read-only audit `SPORTS_RESEARCH_READ_ONLY_AUDIT_2026-09-23.md` (**the full audit text is not present in the repository or on Drive**) | **IMPLEMENTED 2026-09-25**, item by item in §3 below; items 5–10 had not been implemented before this pass | See §3 | — |

## 3. Item-level implementation of audits whose recommendations were outstanding

### 3a. 2026-09-23 read-only audit (`IMPLEMENTED_CHANGES_2026_09_23.md`)

| # | Recommendation | Implemented at (2026-09-25 unless stated) |
|---|---|---|
| 1 | Append P-482 and P-483 to Part 5 | Done 2026-09-22 (Part 5 §"2026-09-22") |
| 2 | Status-register custody for P-482 and P-483 | Done (register rows) |
| 3 | Mark the P-482 mini log reconciled; `REVIEW-*` handles | Resolved in substance by the 2026-09-22 settlement: finality (four lineages each), pregame horizon, provenance and model review are all recorded there. `REVIEW-P490-PROP-BOX` closed 2026-09-25 (King 4.0 IP, 12 outs, statsapi 823897) |
| 4 | Learning-register observations (P-483 pathway, WTA match-page lane, Kalieva volatility, cricket early-wicket hypothesis) | `LEARNING_REGISTER.md` §"2026-09-25 audit closure" C, L-20260925-01 to 04 |
| 5 | Resolve the UNVALIDATED_SUBJECTIVE contradiction | `METHOD.md` §12, and the CR-3 sections of `RULES_BASEBALL.md`, `RULES_CRICKET.md` and `RULES_SOCCER.md` |
| 6 | Source-receipt criteria; "three hostnames do not certify C-FINAL3" | `CONTROLS.md` C-FINAL3; `FORECAST_PREFLIGHT_MANIFEST.md` §"2026-09-25" |
| 7 | Cricket: wicket identity and surviving-batter strike exposure with phase-bowler allocation; winner from explicit innings states | `RULES_CRICKET.md` control 19 extension |
| 8 | Tennis: serve/return numerators and denominators | `RULES_TENNIS.md` `TE-S2` / `TE-S4` |
| 9 | Official final reports first; zero is not a duck | `RULES_CRICKET.md` §7; `DATA_SOURCE_REGISTER.md` §"2026-09-25" (a); `SOURCES.md` §"2026-09-25" |
| 10 | Archive only after verified canonical custody | `EXTERNAL_LOGGING_WORKFLOW.md` §"2026-09-25" item 1 |

### 3b. 2026-09-22 cohort audit (Part 5 §"2026-09-22", §4.3 and the §5 mapping). Its own text says "no governing … document was edited in this pass"

| Map # | Item | Implemented at |
|---|---|---|
| 1 / R-1 | Phase totals conditioned on innings order | `RULES_CRICKET.md` control 21 extension; §10.4 phase row; §10.7 item 17; §10.8 phase-output row |
| 2 | P-482 as reverse-direction kill-path evidence | `RULES_CRICKET.md` §10.5 new row |
| 3 | Name Nos. 3–4 and both new-ball bowlers | `RULES_CRICKET.md` control 20; §10.7 item 3 |
| 4 | Toss via ESPN `notes[]` at toss + 5 minutes | `RULES_CRICKET.md` §2.7 (the route pre-existed in `DATA_SOURCE_REGISTER.md`) |
| 5 | ESPN cricket league-ID route (`8623`) and `playbyplay` | `DATA_SOURCE_REGISTER.md` §"2026-09-25" (a) |
| 6 | Kensington powerplays by innings order | `BASE_RATES_REGISTER.md` §6 |
| 7 | Nation News independent; CaribbeanCricket.com and CricTracker are the CPL lineage | `DATA_SOURCE_REGISTER.md` §"2026-09-25" (a) |
| 8 / R-6 | Dominant-hitter collapse keying | `LEARNING_REGISTER.md` `T-CRI-DOMINANT-HITTER` (TESTING) |
| 9 / R-2 | Tennis benchmark as a blocking pre-freeze field | `RULES_TENNIS.md` `TE-P5`; §9.7 item 17; audit field T13 |
| 10 / R-3 | Matchup holds from serve × return | `RULES_TENNIS.md` `TE-S4`; §9.7 item 18 |
| 11 / R-4 | Decisive-branch disclosure; P-483 kill-path evidence | `RULES_TENNIS.md` §9.4 total-games row; §9.5; §9.7 item 19 |
| 12 | Tennis Abstract WTA Elo; WTA draw PDFs; Sackmann 404 | `DATA_SOURCE_REGISTER.md` §"2026-09-25" (b) |
| 13 | WTA totals base-rate gap | `BASE_RATES_REGISTER.md` §6 |
| 14 | `C-TEN-FAV-SEPARATION` manifest | `LEARNING_REGISTER.md` §"2026-09-25 audit closure" A |
| 15 / R-5 | Numeric shared-failure mass when the joint states are explicit | `METHOD.md` §4 field 5; `RULES_GENERAL.md` §16.12(a) |
| 16 / R-7 | Completeness tooling aligned to the template and sport checklists | `audit_card_controls.py` (fields BR, T13, CVW) and `test_audit_card_controls.py` |
| 17 | Recurring-mistake registry update (M15, M19, M17, M11; the proposed "M21") | `LEARNING_REGISTER.md` §"2026-09-25 audit closure" B: M1–M30 in-repo; the proposed M21 became **M24** |
| 18 | P-482 "result-right / process-different" worked example | `RULES_GENERAL.md` G37 |
| 19–20 | Cards and register rows | Done 2026-09-22 |
| 21 | 24-hour registration | `METHOD.md` §3 step 7 (pre-existing); recurrence recorded in `EXTERNAL_LOGGING_WORKFLOW.md` §"2026-09-25" item 2 |
| §4.6 | Data quality: ESPN over labels; WTA profile renders; draw-PDF summaries; the Elo page date | `RULES_CRICKET.md` §7; `DATA_SOURCE_REGISTER.md` §"2026-09-25" (b) |
| §4.8 | Items needing more evidence | `LEARNING_REGISTER.md` A: `T-TEN-BENCHMARK-GAP`, `T-CRI-POST-TOSS-FREEZE`; the Kensington chase effect is context only (`BASE_RATES_REGISTER.md` §6) |

### 3c. 2026-09-23(c) mapping items left "Proposed"

| Item | Implemented at |
|---|---|
| Audit-script segmentation false negatives | `audit_card_controls.py`: verbatim markers, `TMP-` IDs, level-5/6 headings, `## Entry N`, and the root-cause fix to the settlement-boundary regex. `test_audit_card_controls.py` has 17 tests |
| P-487 card-body recovery | Done 2026-09-23(d) |
| Full verbatim import of P-484–P-486, P-488 and P-492, with G-L13 re-verification | Part 5 §"2026-09-25(a)". Finals re-verified from ESPN, statsapi and the WTA API. The Codex attachments were archived byte-exact in `archive/mini_logs/originals_2026-09-25/` |
| `O-START-MARKER` field definition | Confirmed for the NBL (first `jumpBall` event): `RULES_BASKETBALL.md` K-3; `DATA_SOURCE_REGISTER.md` §"2026-09-25" (c); L-20260925-05. The WTA definition is still pending |

### 3d. 2026-09-24(f) verification audit: items not completed on 2026-09-24

| Item | Implemented at |
|---|---|
| `COVERING_PAIR` in the scoring authority | `SCORING_AND_VALIDATION.md` §3; §12 labels |
| Settlement-integrity labels | `SCORING_AND_VALIDATION.md` §12 |
| Settlement controls in the primary workflow | `METHOD.md` §7; `UPCOMING_GAME_RESEARCH_GUIDE.md` §16 Steps 4a, 4b, 6, 6a and 7 plus §19 checklist; `AGENT_ROLE_AND_TASK.md` settled-view record |
| S-1 Rev 2 receipt and lineup diff in tooling | `audit_card_controls.py` fields 7r, 10p and 10l with `--strict`; `prediction_preflight.py` `participants` object (`PF-LINEUP-*`); `test_prediction_preflight.py` now 29 tests |
| TESTING hypotheses in the prospective table | `LEARNING_REGISTER.md` §"2026-09-25 audit closure" A |
| Settle P-509 once final, with the §(f) part N checklist | Part 5 §"2026-09-24(g)" (three lineages: NBL feed, ESPN, Flashscore) |

## 4. What remains open — explicitly not implemented, with its active home

| Item | Why it is open | Tracked in |
|---|---|---|
| H0 dataset construction and quality approval; chronological TRAIN/TUNE/CAL/TEST; prospective shadow | Empirical work | `H0_DATASET_CARD.md`, `NUMERICAL_PROGRAM.md` |
| Non-MLB `R-1` magnitudes | Empirical work | **DONE 2026-09-25(b)** for the NBA, WNBA, NBL, NHL and EPL (`RECENCY_AND_REBOUND.md` §7). Cricket, NPB, other soccer and other basketball leagues remain `NOT_YET_DERIVED` |
| All TESTING rows (`T-TEN-LOWTIER-HCP`, `T-BKB-SEASON-OPENER-WIDTH`, `T-NHL-PRESEASON-GOALIE`, `T-MLB-WIND-IN-OVER`, `C-TEN-FAV-SEPARATION`, `T-TEN-BENCHMARK-GAP`, `T-CRI-DOMINANT-HITTER`, `T-CRI-POST-TOSS-FREEZE`, `C-RUN-CENTRE-BIAS`) | Need prospective cards | `LEARNING_REGISTER.md` |
| WTA `O-START-MARKER` field definition | Needs a WTA feed observation | `LEARNING_REGISTER.md` L-20260925-05 |
| Canonical numbers for TMP-NBL-CNS-TAS and TMP-G25 | Operator decision | `GAME_LOG_STATUS_CURRENT.md`; Part 5 snapshot |
| Historical documentary and settlement queue handles | Operational queue work | `GAME_LOG_STATUS_CURRENT.md` |
| The `audit_2026-09-12/`, `audit_2026-09-17_models/` and `audit_2026-09-17_implementation/` evidence folders | Never synced to the repository (no git history); links in active documents now say so | This ledger |
| `PREDICTION_MINI_RUNNING_LOG_P474_ONWARD.md` at the repository root | A settled P-474–P-481 log copy that is not byte-identical to its archive copies; moving it needs a Part 4 custody check | **RESOLVED 2026-09-25(b).** The custody check found: the file was clean against its commit (`59bda0f`); SHA-256 `48532d08…6a300f4b`; it is the consolidated 2026-09-21 re-audited version (all eight "independent re-audit" blocks, also carried in the archived `…_AUDIT_2026-09-21_PART_A/B.md`); and no live governance path linked to it. Neither it nor the 139 KB archive copy (`1d9e777b…`) matches the Part 4 import's recorded source SHA (`5239a9…`). That import therefore used an intermediate version, and Part 4's verbatim text stays the canonical issued record. The file was moved **intact** with `git mv` to `archive/mini_logs/Mini Prediction Log - P-474 onward - 2026-09-20/PREDICTION_MINI_RUNNING_LOG_P474_ONWARD_REAUDITED_2026-09-21.md`; its SHA is unchanged |
| The full `SPORTS_RESEARCH_READ_ONLY_AUDIT_2026-09-23.md` text | Not present in the repository or on Drive; only the implementation summary survives | This ledger |

## 5. Validation (run 2026-09-25)

- `python -m unittest test_prediction_preflight`: **29/29 PASS** (20 existing, 9 new `participants` tests).
- `python -m unittest test_audit_card_controls`: **17/17 PASS**. The 17th test is a regression for a sport-heuristic false positive found during final validation: an NBL card's "full-game handicap" had been read as tennis. It was fixed by classifying from the card title first and requiring the plural "games handicap".
- `audit_card_controls.py` regression on the archived P-495–P-508 log: P-493 and TMP-G25 are now audited. Their gaps (fields 2 and 3; fields 2, 3 and 5a) match the 2026-09-23(c) manual check. P-494's false negatives are gone. Under `--strict`, 7r fails on P-505–P-509 (no S-1 Rev 2 receipt) and T13 on P-495 and P-496. Both are real findings, recorded as `CURRENT_RULE_GAP` for those historical cards, not as defects.
- **Link check after the move:** 624 relative Markdown links checked across the active governing documents and Part 5. The only missing target was a link in Part 5's P-494 stub to a mini-log folder archived on 2026-09-23/24. It was already dangling before this pass and is corrected with a pointer note to Appendix Z.
- A control-character and stripped-text scan found no corruption in any edited file. Two tooling slips in this pass were caught and repaired before this ledger was written: a heredoc escape in `audit_card_controls.py` and a shell-stripped paragraph in `RULES_BASKETBALL.md`.

## 6. Path updates made when archiving

In the active governing documents, every reference to an archived audit file now points to `archive/audit_documents_implemented_2026-09-25/<file>`. This covers clickable links, backticked pointers and plain mentions. The documents are the root `README.md`, `METHOD.md`, `CONTROLS.md`, `AGENT_ROLE_AND_TASK.md`, the `RULES_*.md` files, `SOURCES.md`, `DATA_SOURCE_REGISTER.md`, `LEARNING_REGISTER.md`, `EXTERNAL_LOGGING_WORKFLOW.md`, `UPCOMING_GAME_RESEARCH_GUIDE.md`, `SCORING_AND_VALIDATION.md`, `FORECAST_PREFLIGHT_MANIFEST.md`, `GAME_LOG_STATUS_CURRENT.md`, `PERFORMANCE_ELIGIBILITY_POLICY.md`, `MODEL_AND_DATA_SPEC.md` and `ALGORITHM_PORTFOLIO_AND_EVALUATION.md`. Only paths changed.

The following were **not** edited, because they are immutable evidence or historical receipts:
- the closed logs (Parts 1–4) and the historical sections of Part 5;
- `drive_settlement_2026-09-21/before/`;
- the earlier `CONTROL_MANIFEST_*` files (their paths describe the tree at the time);
- the superseded 2026-09-05 registers;
- the archived audit files themselves.

Readers of those files should resolve an audit filename to this folder.
