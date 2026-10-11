# Implementation: finishing the latest retrospective's recommendations (run 2)

**Date:** 2026-10-11, Australia/Sydney. **Base:** local `main` `abb3e98d7ab2dfc3bd33bcdf42b4a3bf3a11a7d4` (v10, unpushed) on published `2d6d86350ce4d6bd9f4ae0f34a42351e71ff0e4b`. **Versions:** unchanged (MDS-2026.10.11-v10.0, CR-2026.10.11-R1, SCV-2026.10.11-v6, SEL-2026.10.11-v2) except the profile document, now LP-2026.10.11-v2. Proposal: [CHANGE_PROPOSAL.md](CHANGE_PROPOSAL.md). Evidence: [NBL_PROFILE_AUDIT.md](NBL_PROFILE_AUDIT.md), [KBO_NPB_EXTRAS_AUDIT.md](KBO_NPB_EXTRAS_AUDIT.md), [VERIFICATION_REPORT.md](VERIFICATION_REPORT.md).

## 1. Result in one paragraph

Six of the seven RET proposals were already carried by the v10 release as document controls, and this run confirmed that by reading the live documents, not the status labels (§2). The seventh, RET-01 (the NBL profile refresh), was `DATA_PENDING`; it is now done, together with a partial 2026-27 NBL archive file, a correction to the KBO/NPB profile rows and a first local-machine pass over the source matrix. The things that remain are not things a document edit can finish: they need issued v10 cards (RET-02 to RET-07 monitoring and the shadow comparisons), a decision on effect sizes (the three `BLOCKED_DESIGN` experiments), or investigation of publishers (lineage audit). **No predictive improvement is claimed or shown.**

## 2. The seven proposals, checked against the live documents

Status vocabulary follows v10: `DOCUMENTED_ACTIVE` (controls written and present), `SHADOW_READY`, `DATA_READY`, `DATA_PENDING`, `BLOCKED_DESIGN`.

| ID | What the retrospective proposed | Where it lives now (checked in this run) | Gap found | Status after this run |
|---|---|---|---|---|
| RET-01 | Recompute the NBL row from 2025-26 and 2026-27; flag profiles over a season old | Freshness rule: LEAGUE_PROFILES "How to use" rule 3; prompt 7 §1 (NBL coverage inspection); prompt 1 basketball block (league/era profile). **Refresh: this run** | The refresh had not been done; the file for 2026-27 did not exist; two archive defects (blank dates, mistyped stage) would have contaminated a naive rebuild | Row refreshed to 2023-25 (n 450) with the 2022-24 row retained as comparator; 29-game 2026-27 snapshot; **`DATA_READY`**; predictive acceptance **`BLOCKED_DESIGN`** |
| RET-02 | Print a league-only `BASELINE_P` on every row and score against it | SELECTION_RULES §9 (`BASELINE_LEAGUE_V1`); CARD_AND_LOG_TEMPLATES: Baseline bullet (line 75), `BASELINE_P` column (84), settlement original `BASELINE_P` (154); CURRENT_RULES line 63; prompt 1 line 31; both golden examples | None | `DOCUMENTED_ACTIVE`; 0 paired events |
| RET-03 | Shadow Rank-1 gate excluding same-quantity alternatives | SELECTION_RULES §2 (`SHADOW_GATE_RET03`); template "Shadow gate / Rank 2" (92) and "Shadow results" (160); check C5 | None | `SHADOW_READY`; 0 events |
| RET-04 | Rank 2 on a different quantity | SELECTION_RULES §3 (`SHADOW_R2_RET04`, `SHADOW_R2_XCARD6`); prompt 1 line 41; template A7 (104) | None (v10 made them shadows, not the primary rule, a deliberate change from the retrospective's wording) | `SHADOW_READY`; 0 events |
| RET-05 | Late-start sub-cohort | Template Timing (69) and "Scheduled lead / band" (71); CURRENT_RULES lines 47 and 49 (`LATE_START` at 5 minutes or less); SCORING line 21 | None | `DOCUMENTED_ACTIVE`; monitoring 0 of 40 collected |
| RET-06 | Official KBO box score first | Prompt 3 line 23 (official terminal box promptly; stale route triggers a retained fallback and a documented retry after about 12 hours); SOURCES line 3 | No test that the official route can be read | **New evidence:** at 23:56 AEDT the official English scoreboard (`eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=2026-10-11`) showed both 11 October games as FINAL with innings, R/H/E and pitchers (KT 12–3 Samsung; Lotte 4–1 KIA), matching the MyKBO-based settlements of P-572 and P-573, which had logged the official page as still non-terminal at 21:58 (about 6 hours after the 16:00 AEDT first pitch). So the route works and had finals about 8 hours after first pitch on this slate. One observation, not the 8-of-10 test. `DOCUMENTED_ACTIVE`; monitoring 0 of 10 |
| RET-07 | Self-audit gaps: gate numbers (C5), vocabulary (C8), result masses (C4) | Template checks C4, C5, C8 (lines 187, 188, 191); EDGE_CASES fixtures | None | `DOCUMENTED_ACTIVE`; monitoring 0 of 40 |

## 3. What this run implemented

| # | Work item | Files | Acceptance evidence (documentary, not predictive) | Rollback |
|---|---|---|---|---|
| 1 | NBL profile refresh, windows compared, prior retained | LEAGUE_PROFILES | Method reproduces the old row exactly (all 9 statistics); 450 games = 140 + 145 + 165; 2025-26 reconciled to 33 per club and to the processed file (165 of 165 scores, 165 of 165 native IDs) | Restore the retained row as default |
| 2 | 2026-27 NBL partial snapshot | `Previous Sports Results/Basketball/NBL/2026/2026_games.csv` | Header identical to the 2025 file; 29 of 29 rows pass 15 consistency checks run by separate code; round trip to the source parse identical; 10 of 29 games confirmed by other publishers with no disagreement | Delete the file (withdraw in changelog) |
| 3 | Archive defect register | ARCHIVE_USE_GUIDE §8; `NBL_2025_26_DATE_EVIDENCE.csv` | Every claimed count re-run (see audit); no archive cell changed | Revert the guide edit |
| 4 | KBO/NPB extras withdrawn | LEAGUE_PROFILES; KBO_NPB_EXTRAS_AUDIT | Both rows reproduce except the extras share; 62 KBO and 72 NPB ties against 1 and 0 marked tied games | Restore the old lines (not advised) |
| 5 | Local reachability pass | SOURCES matrix and §F note | 12 non-manual sources fetched (4 returned the expected content, 7 a home page or shell, 1 a 404 at the host root); contents classified, not assumed | Revert the matrix edit |
| 6 | FC10-PROFILE-v1 definitions frozen | HYPOTHESIS_REGISTER dated status | Candidate and baseline rows, trigger, unit and metric fixed before any card cites them | Add a dated revision |

## 4. What was not done, and why

| Item | Why it is not done | What would finish it |
|---|---|---|
| Repair of the NBL 2025 file (dates, mistyped stage, quarters) | An edit to a published historical file needs the old value, new value and evidence per row and an owner decision; the evidence sidecar is ready (165 rows) | A prompt-7 repair run authorised to edit the 2025 file |
| KBO/NPB innings recovery (so the extras shares can be measured) | 5,370 rows; sources need route-by-route checks. The official KBO English scoreboard gives innings per game by date (confirmed readable today), so the KBO part is feasible; the NPB source is untested | A prompt-7 run for KBO first (about 450 daily pages), then NPB |
| Official 2026-27 NBL schedule denominator and an NBL-owner source for the 19 single-source games | The schedule and ladder pages render client-side | A browser-capable read of the NBL schedule |
| Source lineage audit (FC10-10, SRC-04) | Needs publisher-by-publisher investigation of who collects and who copies | A dedicated audit task |
| Refresh of other leagues' profile rows | Out of scope; only NBL and the KBO/NPB extras were audited | Per-league prompt-7 runs |
| Predictive acceptance for FC10-BASELINE, GATE, PAIR, PROFILE | `BLOCKED_DESIGN`: effect size, tolerance and sample plan are not set, and no v10 card exists | The user's decision on those inputs, then issued v10 cards |
| RET-05/06/07 monitoring targets | They count future events | 40 requested events (10 for KBO) |
| ENG, ML, DST fitted-model items | `SUSPENDED_MD_ONLY` by the Markdown-only scope | A scope decision to allow a runtime |

## 5. Limits that matter

- A refreshed profile is a better-documented prior, not a better forecaster. The 2026-27 NBL level is not established as different (z 1.1 against the new row).
- The 2026-27 file rests on one provider for 19 of its 29 games and cannot prove completeness.
- The reachability pass is one observation from one machine at one time.
- Everything here is research-only and `RESEARCH_ONLY_NOT_CERTIFIED`.

## 6. Publication state

The v10 release (commit `abb3e98d7`) was committed locally and was not on `origin/main` when this run started. A push of this run's commit also publishes it. See the delivery message for what was done.
