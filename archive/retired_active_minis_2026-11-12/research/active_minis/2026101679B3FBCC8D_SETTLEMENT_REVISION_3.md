<!-- SETTLEMENT-FORMAT: mini-settlement-10 -->
# SETTLEMENT REVISION DOCUMENT — MINI 2026101679B3FBCC8D — revision-3 package

**Document:** `research/active_minis/2026101679B3FBCC8D_SETTLEMENT_REVISION_3.md` · written 2026-11-07T20:53:07+11:00 (clock read). A rerun returns a new revision document; the revision-1 package and the revision-2 document are **not** overwritten.
**Mode / authority:** `LOCAL_MINI_SETTLEMENT` (prompt 3, P-2026.10.22-v24.0), owner-invoked 2026-11-07 ("fully settle all of the logs in the mini logs to be settled folder ... following the audit/settlement process stipulated"). `LOCAL_WORKING_TREE`, branch `main`, HEAD `749bca06d2b63f358fce19a1969d6887ecfb8815` (= `origin/main` after `git fetch`).
**Reading receipt:** COMMON_OPERATING_PROTOCOL; prompts 3 and 4; SCORING_AND_VALIDATION §1–§3 (incl. §2a evidence strata); VERIFICATION_PROTOCOL; MINI_LOG_IDENTITY_PROTOCOL; RULES_BASKETBALL (BK-P4 endpoint); RULES_SOCCER; SOURCES; the frozen mini, the revision-1 package and the revision-2 document named below; the 21 October import report, its UNRESOLVED_POST_IMPORT queue, the rollover QUEUE_CONTINUITY and the 21 October retrospective (findings F-01, F-02).

## Frozen source, prior packages and scope
- **FROZEN_SOURCE (unchanged, already canonical):** `research/verification/mini_import_P-601_P-622_2026-10-21-1/inputs/2026101679B3FBCC8D/ORIGINAL_MINI.md` — 313,155 bytes, SHA-256 `b7478342e7ecba6861d9d79e4fc98b1dcd686356260f8b21911989847115ad7e`, 11 card markers G0001–G0011 + 2 G0001 addenda, first key `LOCAL-2026101679B3FBCC8D-G0001`, last `…-G0011`. Re-hashed at this settlement before any text was written; equals the import's FROZEN_SOURCE receipt. No later blocks exist in it.
- **Prior settlements:** revision-1 package `…/inputs/2026101679B3FBCC8D/PREDICTION_MINI_SETTLED_2026101679B3FBCC8D_20261017_R1.md` (387,500 bytes, `6cfea59c880c5d00a9d30c31942d097419c186e0d22be958393fabc976040ee6`); revision-2 document `…/inputs/2026101679B3FBCC8D/2026101679B3FBCC8D_SETTLEMENT_REVISION_2.md` (16,568 bytes, `60c1caae10873f7464e2d2aae8c5bd88851f042231d9a184e513233cdc524a76`). Both are imported (Part 8).
- **This document appends:** `revision-3` for G0004 (P-604) corner keys only (UNRESOLVED → graded) and `revision-2` for G0006 (P-606) final-score field only (score repair, grades unchanged). Revision numbers are per original record key: G0004 had revisions 1–2, G0006 had revision 1 only. No other card or key is touched; their effective revisions are unchanged.
- All 11 cards are `RESEARCH_ONLY_NO_MODEL`; the numbers are analyst diagnostics `NOT_PRIMARY`. Primary Rank-1/Top-2 denominators remain **0**; Brier values below are diagnostic for prompt 6 only (SCV §1).
- **Owner drop folder.** Every file of the owner drop `MINI LOGS TO BE SETTLED/` (14 files) was compared by SHA-256 with the 21 October import inputs: all 14 are byte-identical to retained inputs, so the folder holds no unsettled card, block or revision beyond those listed here. Its archive move is recorded in the prompt-4 report.

## LOCAL_ID_MAPPING
Existing canonical references retain their real mappings (MINI-v2): `LOCAL-2026101679B3FBCC8D-G0004` → **P-604**; `LOCAL-2026101679B3FBCC8D-G0006` → **P-606** (both assigned by the 2026-10-21 import, `LOCAL_ID_MAPPING.csv`). No new event; no P-number is planned or assigned here.

## Source discovery, corroboration and reuse register
**Information completion: `INFORMATION_INCOMPLETE`** — P-604 corners rest on two aggregators of unknown upstream lineage (no field-owner sheet); operator terms for all keys; exact final wall-clock times.

| Source ID | URL / route | Fields observed / missing | Publisher / independence | Retrieval | Reuse limits |
|---|---|---|---|---|---|
| R3-S01 Gioscore match page | `https://gioscore.com/es-ben-aknoun-olympique-akbou/MDAxNDQwOTEtMjMyNDc3` | 16 Oct 2026, Ligue 1, Stade de l'Unité Maghrébine; **Olympique Akbou 2–1 ES Ben Aknoun**; goals 4' (Tamimi, Ben Aknoun), 56', 58'; statistics "8 Corners 5", Akbou listed first | Aggregator; upstream feed not named → lineage UNKNOWN | 2026-11-07, before 20:48:26 AEDT (web fetch) | Statistic only; nothing else on the page used |
| R3-S02 Futbol24 match page (revision-1 terminal source S10) | `https://www.futbol24.com/match/2026/10/16/national/Algeria/Division-1/2026-2027/Oly-Akbou/vs/ES-Ben-Aknoun` | Corners **Akbou 8 – Ben Aknoun 5 = 13**, as captured by the 21 October retrospective (F-02) through a text-reader proxy; not re-read here (search did not surface it, and no proxy was used in this session) | Aggregator; lineage UNKNOWN; independent of R3-S01 not proven | 2026-10-21 (retrospective capture) | Single capture; see F-02 |
| R3-S03 Fox Sports box score | `https://www.foxsports.com/nba/charlotte-hornets-vs-memphis-grizzlies-oct-16-2026-game-boxscore-106518` | Linescore CHA 20-18-24-36 = **98**; MEM 23-27-29-37 = **116**; final **MEM 116 – CHA 98**; page header dates 16 Oct, scoreboard 17 Oct (time-zone display) | Independent media box score | 2026-11-07, before 20:48:26 AEDT | Score fields only |
| R3-S04 retrospective recapture (F-01) | ESPN scoreboard, summary and box; NBA.com game page | ESPN box 37 FG, 14 3PT, 28 FT → 2×37 + 14 + 28 = **116**; NBA.com final 116 with a linescore Q3 of 30 (sums to 117, internally inconsistent) | ESPN + league owner | 2026-10-21 | Recorded in `research/verification/retrospective_2026-10-21/RETROSPECTIVE_REPORT.md` |
| R3-S05 secondary blurbs (rejected for the score) | Fox/RotoWire player notes ("117-98") | Repeat the recap-video figure | Secondary text, no box | 2026-11-07 search | Not used: no sum check; contradicted by two box scores |
| R3-S06 Algeria other routes | Web search FR/EN "Akbou Ben Aknoun octobre 2026 corners"; FotMob team pages | No match-level corners | — | 2026-11-07, before 20:48:26 AEDT | — |

**Search attempts.** P-604: 3 searches + 1 page read (R3-S01 found). P-606: 1 search (blurbs only, rejected) + 1 box-score read (R3-S03). No price, line or odds page was opened or used.

**REQUIREMENT_CLOSURE**
| Field | Status | Next · actor · due · automation |
|---|---|---|
| P-604 FT corners per side | CLOSED_PROVISIONAL (evidence C: two aggregators agree, lineage unknown) | LFP official match sheet for a field-owner upgrade · settlement reviewer · next owner-invoked review · NOT_SCHEDULED |
| P-606 final score | CLOSED (two box scores with sum checks; owner page final agrees) | — |
| Operator terms, all keys | OPEN | owner · NOT_SCHEDULED |
| Exact final wall-clock times | OPEN (`UNKNOWN`) | field-owner gamebooks · settlement reviewer · NOT_SCHEDULED |

<!-- BEGIN SETTLEMENT LOCAL-2026101679B3FBCC8D-G0004 revision-3 -->
### Settlement · LOCAL-2026101679B3FBCC8D-G0004 (P-604) · Olympique Akbou v ES Ben Aknoun — corner rows · 2026-11-07T20:53:07+11:00
**Revision:** revision-3 · parent revision-2 · effective 2026-11-07T20:53:07+11:00 · affected keys: FT Over 10.5 corners, FT Under 10.5 corners only · changes: both `UNRESOLVED → graded` (reason: full-time corner count now found on a second aggregator and agreeing with the revision-1 terminal source; retrospective F-02). All other G0004 rows keep their revision-1 grades (1H Over 0.5 WIN, 1H Under 0.5 LOSS, FT Over 2.5 WIN, FT Under 2.5 LOSS).
**Final corners:** Olympique Akbou **8** + ES Ben Aknoun **5** = **13** (R3-S01 read 2026-11-07; R3-S02 captured 2026-10-21). R3-S01 also shows the final 2–1 and the 4' Ben Aknoun goal, matching the revision-1 score and first-half goal. **Evidence C** (two aggregators, upstream lineage unknown, so independence is not proven; sensitivity view only, SCV §2a). Definition: regulation 90 minutes plus stoppage, corner kicks awarded, as the card's A2 states; operator `UNKNOWN_DEFINITION`.

| Original proposition | Original primary p_card | Frozen analyst p (NOT_PRIMARY) | Verified field | Grade | Evidence | Primary count |
|---|---|---:|---|---|---|---|
| FT Over 10.5 corners | NOT_ESTIMATED | 0.51310 | 13 | **WIN** | C | NO |
| FT Under 10.5 corners | NOT_ESTIMATED | 0.48690 | 13 | **LOSS** | C | NO |

**Expected vs final:** card corner centre 11.125 (Akbou 6.750, Ben Aknoun 4.375; negative binomial r=12, analyst-assumed) → 13 (8, 5): +1.875, z ≈ +0.40 (SD √(11.125 + 11.125²/12) = 4.63). Akbou +1.25 and Ben Aknoun +0.625 above their side centres.
**Diagnostic Brier (prompt 6 only, not a primary score):** Over (0.5131−1)² = 0.2371; Under (0.4869−0)² = 0.2371.
**R3/R6/R7/R8:** 13 ≥ 11 → Over; 2.5 corners beyond the line; inside the card's base-scenario distribution (high scenario μ 12.75). Nothing in the outcome is attributed to a pre-start input. **R9:** terminal evidence is post-event; issue phase unchanged from revision-1. **R12:** `DATA_REPAIR_REQUIRED` stays only for a field-owner corner source (upgrade C → A/B by a later revision); grades stand. Other R sections unchanged from revision-1.
<!-- END SETTLEMENT LOCAL-2026101679B3FBCC8D-G0004 revision-3 -->

<!-- BEGIN SETTLEMENT LOCAL-2026101679B3FBCC8D-G0006 revision-2 -->
### Settlement · LOCAL-2026101679B3FBCC8D-G0006 (P-606) · Charlotte Hornets @ Memphis Grizzlies — score repair · 2026-11-07T20:53:07+11:00
**Revision:** revision-2 · parent revision-1 · effective 2026-11-07T20:53:07+11:00 · affected keys: Hornets +2.5, Grizzlies −2.5, Combined Over 229.5, Combined Under 229.5 · changes: verified final **117–98 → 116–98** (combined 215 → 214; Memphis margin 19 → 18); **no grade changes** (reason: revision-1 read the score from a recap-video title; two box scores with sum checks give 116; retrospective F-01).
**Final event:** **Memphis Grizzlies 116 – Charlotte Hornets 98**, regulation (MEM 23-27-29-37; CHA 20-18-24-36; R3-S03). ESPN box sum 2×37 FG + 14 3PT + 28 FT = 116 (R3-S04). NBA.com's final also reads 116; its linescore Q3 of 30 is internally inconsistent and is not used. Final wall-clock time `UNKNOWN`.
**Definition:** full game incl. OT (card); no OT. Operator `UNKNOWN_DEFINITION`. **Evidence:** B (two independent box scores with sum checks).

| Original proposition | Original primary p_card | Frozen analyst p (NOT_PRIMARY) | Verified field | Grade | Primary count |
|---|---|---:|---|---|---|
| Hornets +2.5 | NOT_ESTIMATED | 0.46340 | Hornets −18 | **LOSS** (unchanged) | NO |
| Grizzlies −2.5 | NOT_ESTIMATED | 0.53660 | Grizzlies +18 | **WIN** (unchanged) | NO |
| Combined Over 229.5 | NOT_ESTIMATED | 0.35910 | 214 | **LOSS** (unchanged) | NO |
| Combined Under 229.5 | NOT_ESTIMATED | 0.64090 | 214 | **WIN** (unchanged) | NO |

**Expected vs final:** analyst expected combined 222.50 → 214: residual **−8.50** (revision-1 recorded −7.50 from the wrong score). Fitted-model residual and z `NOT_COMPUTABLE`.
**Diagnostic Brier (prompt 6 only):** Hornets +2.5 0.4634² = 0.2147; Grizzlies −2.5 (0.5366−1)² = 0.2147; Over 0.3591² = 0.1290; Under (0.6409−1)² = 0.1290 — unchanged, because no grade changed.
**R2:** 116–98, two box scores. **R3:** 214 ≤ 229 → Under; Memphis by 18 → Grizzlies −2.5. **R6:** total 15.5 under the line; margin 15.5 beyond −2.5. **R7:** −8.50 against the analyst centre. **R9:** revision-1's terminal source (a recap-video title) is a headline, not a box score; SOURCES and prompt 3 §4 require box-score or linescore scores with a sum check. **R12:** `NO_CHANGE` to grades; data repair done. Other R sections unchanged from revision-1.
<!-- END SETTLEMENT LOCAL-2026101679B3FBCC8D-G0006 revision-2 -->

## UNRESOLVED_CARRYOVER (supersedes U-602 for P-604; other rows unchanged)
| ID | Event key | Queue | Original card | Latest revision | Open field | Responsible actor | Next source + exact field | Due | Final-time basis | Last attempt | Scheduled automation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R3-Q1 | G0004 (P-604) | UNRESOLVED_EVIDENCE (upgrade only, non-grading) | G0004 | revision-3 | Field-owner corner count to lift evidence C | Settlement reviewer | LFP official match sheet, corner line | Next owner-invoked review | UNKNOWN | 2026-11-07, before 20:48:26 AEDT (R3-S06) | NOT_SCHEDULED |
| R3-Q2 | G0003 (P-603) | UNRESOLVED_EVIDENCE (corroboration, non-grading) | G0003 | revision-2 | Second corner source (ESPN 1+5 only) | Settlement reviewer | ISL match centre statistics | Next owner-invoked review | UNKNOWN | 2026-11-07, before 20:48:26 AEDT (2 searches; no match-level corners found) | NOT_SCHEDULED |
| R3-Q3 | all 11 | UNRESOLVED_DEFINITION | all | latest per key | Operator terms | Owner | Written rules | Next owner-invoked review | N/A | not supplied | NOT_SCHEDULED |
| — | Final wall-clock times and other revision-1/2 items | unchanged | — | as recorded | as recorded | as recorded | as recorded | as recorded | as recorded | no new attempt | NOT_SCHEDULED |

## Learning record additions (LEARN-v2)
| Local key | Final score | Regulation | Decision | Final time | Terminal source |
|---|---|---|---|---|---|
| G0004 (P-604) corners | Akbou 2 – Ben Aknoun 1; corners 8–5 | same | Akbou | UNKNOWN | R3-S01 Gioscore, retrieved 2026-11-07, before 20:48:26 AEDT; R3-S02 Futbol24 |
| G0006 (P-606) | Grizzlies 116 – Hornets 98 (replaces 117–98) | same | Grizzlies | UNKNOWN | R3-S03 Fox Sports box, retrieved 2026-11-07, before 20:48:26 AEDT; R3-S04 ESPN box |

## SETTLEMENT_MANIFEST (effective state after revision-3)
| Item | after revision-2 | after revision-3 |
|---|---|---|
| Verified terminal events | 11 | 11 |
| Supplied contract directions | 52 | 52 |
| Sporting W / L | 25 / 25 | **26 / 26** |
| UNRESOLVED | 2 (G0004 corners) | **0** |
| PENDING_EVENT | 0 | 0 |
| Primary Rank-1 / Top-2 denominators | 0 / 0 | 0 / 0 |
| Evidence C rows | 2 (G0003 corners) | **4** (G0003, G0004 corners) |
| Revision chain | revision-2 for G0010, G0011, G0003 corners, G0004 corners; revision-1 elsewhere | **revision-3** for G0004 corner keys; **revision-2** for G0006; otherwise as before. One chain per key; no branch |
| Canonical import | done for revisions 1–2 | revision-3 package → prompt 4 in this session |

**MINI_SETTLEMENT review row:** `2026-11-07 | MINI 2026101679B3FBCC8D revision-3 | 11 research-only events | 26W-26L of 52 decisive analyst directions, 0 unresolved | primary N/A (no p_card) | NO_CHANGE (data repairs applied: P-606 score; P-604 corners graded on C) | no rank changes`.

## Verification (S1–S19, revision-3 scope)
S1 PASS (2 keys, existing canonical mappings) · S2 PASS (frozen source re-hashed = import receipt) · S3 PASS (analyst p copied literally; primary NOT_ESTIMATED kept) · S4 PASS (grades from verified fields only) · S5 PASS (evidence C flagged; B for P-606) · S6 PASS (26 + 26 + 0 = 52) · S7 PASS (R sections for changed keys; unchanged parts cite revision-1) · S8 N/A (no primary Rank-1 loss) · S9 PASS (no rank change) · S10 PASS (no backfilled pregame field) · S11 PASS (diagnostic Brier only) · S12 PASS (local write; import in this session) · S13 PASS (G0004 revision-3 names parent revision-2; G0006 revision-2 names parent revision-1; no branch) · S14 PASS (queue rows carry actor, source, due, last attempt, NOT_SCHEDULED) · S15 PASS (no price, line or odds source) · S16 PASS (manual check against the frozen mini: both keys exist with these exact propositions) · S17 PASS (source register, attempts and closure tables present) · S18 PASS (handoff: canonical IDs already assigned; prompt 4 appends revisions only) · S19 PASS (owner-drop folder fully reconciled by hash to retained inputs).
