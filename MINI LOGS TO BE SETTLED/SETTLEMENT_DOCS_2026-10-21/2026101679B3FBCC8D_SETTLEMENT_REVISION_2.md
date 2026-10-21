<!-- SETTLEMENT-FORMAT: mini-settlement-10 -->
# SETTLEMENT REVISION DOCUMENT — MINI 2026101679B3FBCC8D — revision-2 package

**Document:** `2026101679B3FBCC8D_SETTLEMENT_REVISION_2.md` · prepared 2026-10-21 ≈01:15 AEDT. A rerun returns a new revision document; the earlier settled file is **not** overwritten.
**Mode / authority:** `LOCAL_MINI_SETTLEMENT`; `PUBLISHED_MAIN_PINNED 3e29a58693e2ed02ff862e9bf0f751af2feadee1`; Prompt 3 run in the repository session (ENV-v1 deviation disclosed); no repository writes, no hashes. Reading receipt as in `20261018X7Q4M9R2_SETTLEMENT.md` (same folder), plus the prior settlement section of the R1 file (read in the owner attachment).

## Frozen source, prior package and scope
- **Frozen original (unchanged):** `MINI LOGS TO BE SETTLED/PREDICTION_MINI_RUNNING_LOG_2026101679B3FBCC8D.md` (218,460 bytes on disk; size from the directory listing, not a hash). The revision-1 package's FROZEN_SOURCE receipt (313,155 bytes, SHA-256 `b7478342…ad7e`, 11 card bodies, 2 addendum markers) refers to the sandbox copy that included G0011; the 218,460-byte disk file is an **earlier** cumulative copy. Reconciliation of which bytes are authoritative stays with prompt 4 (carried as R2-Q4 below).
- **Prior settlement:** `MINI LOGS TO BE SETTLED/PREDICTION_MINI_SETTLED_2026101679B3FBCC8D_20261017_R1.md` (`mini-settlement-10`, revision-1 for G0001–G0011, generated 2026-10-17T19:10:40+11:00).
- **This document appends** `revision-2` for: G0010 (PENDING_EVENT → settled), G0011 (PENDING_EVENT → settled), G0003 corner rows (UNRESOLVED → graded), G0004 corner rows (still UNRESOLVED; new attempts logged). No other card or contract key is touched; their effective revision remains revision-1.
- All 11 cards are `RESEARCH_ONLY_NO_MODEL`; their numbers are analyst diagnostics `NOT_PRIMARY`. No primary p_card exists → primary Rank-1/Top-2 denominators remain **0**, and binary Brier is not entered in any primary or prospective cohort (SCV-v11 §1). Brier values below are diagnostic for prompt 6 only.

## LOCAL_ID_MAPPING (unchanged)
All 11 keys `LOCAL-2026101679B3FBCC8D-G0001…G0011` → `NOT_ASSIGNED / PENDING_PROMPT_4_IMPORT`. Native IDs added this revision: G0010 B.LEAGUE ScheduleKey 506470; G0011 ESPN NBL 401875270; G0003 ESPN ISL 401925434.

## Source discovery, corroboration and reuse register
**Information completion: `INFORMATION_INCOMPLETE`** — G0004 corners unresolved; G0003 corners single-source; operator terms all; frozen-bytes reconciliation.

| Source ID | URL / route | Fields observed / missing | Publisher / independence | Retrieval | Reuse limits |
|---|---|---|---|---|---|
| R2-S01 B.League game record 506470 | `https://www.bleague.jp/game_detail/?ScheduleKey=506470&tab=1` (embedded JSON) | `GameEndedFlg/RecordFixedFlg true`; Chiba 21-17-21-12 = **71**; Hiroshima 30-22-19-18 = **89**; MaxPeriod 4; attendance 4,311; first PBP 2026-10-17T05:10:24Z (**16:10:24 AEDT**), last 07:15:35Z; starters A千葉 Kida, Davis, Newbill, Pardon, Ando; 広島 Terashima, Smith, Evans II, Cockburn, Mayo | B.LEAGUE (owner) | 2026-10-21 ≈00:15 AEDT | — |
| R2-S02 Chugoku Shimbun / Hiroshima club / basketballking (search-visible) | `https://www.chugoku-np.co.jp/articles/-/910995`; `https://hiroshimadragonflies.com/topics_detail39/id=24854` | Hiroshima 89–71, 7–0 start; Q1 21–30, Q2 17–22; attendance 4,311; Cockburn 22, Smith 19 | Independent newspaper + club | search | — |
| R2-S03 ESPN NBL scoreboard 17 Oct | `https://site.api.espn.com/apis/site/v2/sports/basketball/nbl/scoreboard?dates=20261017` | PNX 27-35-27-26 = **115**; CNS 35-19-9-20 = **83**; Final; scheduled 06:30Z | ESPN | ≈00:12 AEDT | — |
| R2-S04 basketball.com.au / NBL / Junee Southern Cross (search-visible) | `https://www.basketball.com.au/news/nbl27-round-5-south-east-melbourne-phoenix-cairns-taipans-match-report`; `https://www.nbl.com.au/news/phoenix-dominate-snakes-in-strong-response` | 115–83; Sobey 29; **Jordan Hunter 19 pts 11 reb**; Cairns 9 points in Q3 | Independent + NBL | search | — |
| R2-S05 ESPN ISL summary 401925434 | `https://site.api.espn.com/apis/site/v2/sports/soccer/ind.1/summary?event=401925434` | SC Delhi 1–2 Mohun Bagan; halves 1–0 / 0–2; goals 23', 56', 60'; `wonCorners` SCD **1**, MBSG **5** | ESPN/Opta | ≈00:40 AEDT | Corners single source |
| R2-S06 Algeria corner attempts | FotMob `https://www.fotmob.com/matches/es-ben-aknoun-vs-olympique-akbou/1t0fnjjy9` (r.jina.ai: HT 0–1 only); BeSoccer `…/2026100627` (a different, Round-15 2025-26 fixture — rejected); 365Scores match page (no stats in proxy text); SofaScore API (HTTP 403); extended web search | Corners **not found** | — | ≈00:45 AEDT | — |

**REQUIREMENT_CLOSURE**
| Field | Status | Next · actor · due · automation |
|---|---|---|
| G0010 final/quarters/OT | CLOSED (owner + 2 independent) | — |
| G0011 final/quarters/OT | CLOSED (ESPN + NBL/independent) | NBL owner box · prompt 4 · NOT_SCHEDULED |
| G0003 full-time corners | CLOSED_SINGLE_SOURCE (evidence C) | ISL match centre 194640 stats · prompt 4 · NOT_SCHEDULED |
| G0004 full-time corners | OPEN — UNRESOLVED | LFP match sheet / Goaloo-derived corner rows · prompt 4 · NEXT_OWNER_INVOKED · NOT_SCHEDULED |
| Operator terms all | OPEN | owner |

<!-- BEGIN SETTLEMENT LOCAL-2026101679B3FBCC8D-G0010 revision-2 -->
### Settlement · LOCAL-2026101679B3FBCC8D-G0010 · Altiri Chiba v Hiroshima Dragonflies · 2026-10-21T01:15+11:00
**Revision:** revision-2 · parent revision-1 · effective 2026-10-21T01:15+11:00 · affected contract keys: Chiba +7.5, Dragonflies −7.5, Over 171.5, Under 171.5 · changes: all four `PENDING_EVENT → graded` (reason: verified terminal result now available).
**Card state:** `SETTLED_SPORTING_CONVENTION` (research-only).
**Final event:** **Altiri Chiba 71 – Hiroshima Dragonflies 89**, regulation (21-17-21-12 v 30-22-19-18). Total 160; Hiroshima margin +18. Tip 16:10:24 AEDT; last PBP 2026-10-17T07:15:35Z. The revision-1 note "live half-time 38–52" matches the owner record (38–52 at half).
**Definition:** full game incl. OT (card); no OT. Operator `UNKNOWN_DEFINITION`. **Evidence:** A.
**Expected vs final:** total 169.36 (σ 17) → 160: −9.36, z −0.55. Hiroshima margin +7.09 (σ 15.5) → +18: +10.91, z +0.70.

| Analyst order | Original proposition | Original primary p_card | Frozen analyst p (NOT_PRIMARY) | Grade | Primary count |
|---|---|---|---:|---|---|
| 1 | Combined Under 171.5 | NOT_ESTIMATED | 0.5501 | **WIN** | NO |
| 2 | Chiba +7.5 | NOT_ESTIMATED | 0.5105 | **LOSS** | NO |
| 3 | Dragonflies −7.5 | NOT_ESTIMATED | 0.4895 | **WIN** | NO |
| 4 | Combined Over 171.5 | NOT_ESTIMATED | 0.4499 | **LOSS** | NO |

**Top-two primary:** NONE (denominator 0). Analyst diagnostic only: R1 W / R2 L.
**Diagnostic Brier (prompt 6 only, not a primary score):** U 0.2024; Chiba +7.5 0.2606; Hir −7.5 0.2606; O 0.2024.
**Winner call (analyst diagnostic):** Hiroshima ≈0.676 → correct.
**R1–R12 (compact):** R1 analyst top two Under (0.550) / Chiba +7.5 (0.511); no primary. R2 71–89, owner-verified. R3 160 ≤ 171; Chiba −18 vs −7. R4 primary N/A. R5 Hiroshima correct. R6 total 11.5 under; spread 10.5 beyond Chiba +7.5. R7 errors within 0.7σ. R8 Hiroshima won every quarter except Q3 (Chiba 21–19), including Q1 30–21; starters matched the card's named roster players (Smith, Evans II, Cockburn, Mayo; Newbill, Davis, Pardon, Ando) — card had them as unconfirmed. R9 tip 16:10:24 AEDT; card research completion 16:15:11 AEDT → **post-tip, confirmed** by owner PBP. R10 RESEARCH_ONLY; process NOT_ASSESSABLE for a primary. R11 none. R12 `NO_CHANGE / LEARNING_LABEL_CANDIDATE`.
<!-- END SETTLEMENT LOCAL-2026101679B3FBCC8D-G0010 revision-2 -->

<!-- BEGIN SETTLEMENT LOCAL-2026101679B3FBCC8D-G0011 revision-2 -->
### Settlement · LOCAL-2026101679B3FBCC8D-G0011 · South East Melbourne Phoenix v Cairns Taipans · 2026-10-21T01:15+11:00
**Revision:** revision-2 · parent revision-1 · effective 2026-10-21T01:15+11:00 · affected keys: Phoenix −4.5, Taipans +4.5, Over 195.5, Under 195.5 · changes: all four `PENDING_EVENT → graded`.
**Card state:** `SETTLED_SPORTING_CONVENTION` (research-only).
**Final event:** **Phoenix 115 – Taipans 83**, regulation (27-35-27-26 v 35-19-9-20). Total 198; Phoenix margin +32. Scheduled tip 06:30Z (17:30 AEDT); final time `UNKNOWN`.
**Definition:** full game incl. OT; no OT. **Evidence:** B.
**Expected vs final:** total 189.60 (σ 20) → 198: +8.4, z +0.42. Phoenix margin +6.02 (σ 16) → +32: +25.98, z **+1.62**.

| Analyst order | Original proposition | Original primary p_card | Frozen analyst p (NOT_PRIMARY) | Grade | Primary count |
|---|---|---|---:|---|---|
| 1 | Under 195.5 | NOT_ESTIMATED | 0.6160 | **LOSS** | NO |
| 2 | Phoenix −4.5 | NOT_ESTIMATED | 0.5379 | **WIN** | NO |
| 3 | Taipans +4.5 | NOT_ESTIMATED | 0.4621 | **LOSS** | NO |
| 4 | Over 195.5 | NOT_ESTIMATED | 0.3840 | **WIN** | NO |

**Top-two primary:** NONE. Analyst diagnostic: R1 L / R2 W.
**Diagnostic Brier:** U 0.3795; Phoenix −4.5 0.2135; Taipans +4.5 0.2135; O 0.3795.
**Winner call (diagnostic):** Phoenix ≈0.647 → correct.
**R1–R12 (compact):** R1 analyst Under 195.5 (0.616) / Phoenix −4.5 (0.538). R2 115–83 verified. R3 198 ≥ 196; Phoenix +32. R4 primary N/A. R5 correct. R6 total 2.5 over 195.5; spread 27.5 beyond −4.5. R7 margin +1.62σ; total +0.42σ. R8 Cairns scored 9 in Q3 (R2-S03). The card logged a source conflict on **Jordan Hunter** (NBL game-day preview listed him OUT, Cairns preview projected him to start); he played and posted 19 points, 11 rebounds (R2-S04) — the card correctly refused to resolve the conflict and that availability uncertainty mattered. R9 card observation 17:40:55 AEDT after the 17:30 scheduled tip → post-start. R10 RESEARCH_ONLY; analyst R1 loss class `AVAILABILITY_CONFLICT / VARIANCE`. R11 `PROPOSED_NOT_TESTED`: when an "OUT" report conflicts with a projected start, price both branches. R12 `NO_CHANGE / LEARNING_LABEL_CANDIDATE`.

**Analyst Rank-1 LOSS — eight-part review (NOT_PRIMARY):** (1) Total ≤195, analyst 0.616. (2) 198. (3) +0.42σ from centre; inside the distribution. (4) Hunter's availability was conflicting pre-start, not knowable; not backfilled. (5) Variance plus an unresolved availability branch. (6) Cutoff-only: two-branch pricing (Hunter in/out) would widen, not flip. (7) `AVAILABILITY_CONFLICT / VARIANCE`. (8) Test branch pricing on NBL cards with conflicting injury reports.
<!-- END SETTLEMENT LOCAL-2026101679B3FBCC8D-G0011 revision-2 -->

<!-- BEGIN SETTLEMENT LOCAL-2026101679B3FBCC8D-G0003 revision-2 -->
### Settlement · LOCAL-2026101679B3FBCC8D-G0003 · Sporting Club Delhi v Mohun Bagan SG — corner rows · 2026-10-21T01:15+11:00
**Revision:** revision-2 · parent revision-1 · effective 2026-10-21T01:15+11:00 · affected keys: FT Over 10.5 corners, FT Under 10.5 corners only · changes: both `UNRESOLVED → graded` (reason: final corner count found; revision-1 had only a 63' live snapshot of 1–3, correctly not used). All other G0003 rows keep their revision-1 grades.
**Final corners:** SC Delhi **1** + Mohun Bagan **5** = **6** (ESPN/Opta `wonCorners`, R2-S05). Consistent with the 63' snapshot (1–3) in revision-1. Single source → evidence **C** (sensitivity view).

| Original proposition | Original primary p_card | Frozen analyst p (NOT_PRIMARY) | Grade | Evidence | Primary count |
|---|---|---:|---|---|---|
| FT Over 10.5 corners | NOT_ESTIMATED | 0.51347 | **LOSS** | C | NO |
| FT Under 10.5 corners | NOT_ESTIMATED | 0.48653 | **WIN** | C | NO |

**Expected vs final:** analyst corner centre 11.20 (NB k=10, SD 4.87) → 6: −5.2, z −1.07.
**R3/R7/R8:** 6 ≤ 10; the analyst corner centre rested on a cross-provider join the card itself flagged as not definition-compatible; observed far below. **R12:** `DATA_REPAIR_REQUIRED` (second corner source). Other R sections unchanged from revision-1.
<!-- END SETTLEMENT LOCAL-2026101679B3FBCC8D-G0003 revision-2 -->

<!-- BEGIN SETTLEMENT LOCAL-2026101679B3FBCC8D-G0004 revision-2 -->
### Settlement · LOCAL-2026101679B3FBCC8D-G0004 · Olympique Akbou v ES Ben Aknoun — corner rows · 2026-10-21T01:15+11:00
**Revision:** revision-2 · parent revision-1 · effective 2026-10-21T01:15+11:00 · affected keys: FT Over 10.5 corners, FT Under 10.5 corners · changes: NONE to grades (both remain `UNRESOLVED`); evidence attempts added.
**Attempts this revision:** FotMob match page via proxy (half-time 0–1 only, no stats); BeSoccer URL from search (a different fixture — Round 15, 2025-26 — rejected); 365Scores match page (stats not exposed in proxy text); SofaScore public API (HTTP 403); extended web search "Olympique Akbou ES Ben Aknoun 2-1 corners 16 octobre 2026" (score confirmed 2–1, HT 0–1; no corner count in any result).
**Grades:** Over 10.5 `UNRESOLVED`; Under 10.5 `UNRESOLVED`. No guessed value.
<!-- END SETTLEMENT LOCAL-2026101679B3FBCC8D-G0004 revision-2 -->

## UNRESOLVED_CARRYOVER (supersedes revision-1's open-event rows for G0010/G0011/G0003-corners)
| ID | Event key | Queue | Original card | Latest revision | Open field | Responsible actor | Next source + exact field | Due | Final-time basis | Last attempt | Scheduled automation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R2-Q1 | G0004 | UNRESOLVED_EVIDENCE | G0004 | revision-2 | FT corners per side | Prompt-4 agent / owner | LFP official match sheet; Goaloo/MatchAtlas corner rows for 16 Oct | NEXT_OWNER_INVOKED | UNKNOWN | 2026-10-21 ≈00:45 AEDT | NOT_SCHEDULED |
| R2-Q2 | G0003 | UNRESOLVED_EVIDENCE (corroboration) | G0003 | revision-2 | Second corner source | Prompt-4 agent | ISL match centre 194640 statistics | NEXT_OWNER_INVOKED | UNKNOWN | ≈00:40 AEDT | NOT_SCHEDULED |
| R2-Q3 | all 11 | UNRESOLVED_DEFINITION | all | latest per key | Operator terms | Owner | Written rules | NEXT_OWNER_INVOKED | N/A | not supplied | NOT_SCHEDULED |
| R2-Q4 | MINI | CUSTODY | — | — | Which frozen bytes are authoritative (disk 218,460-byte copy vs revision-1's 313,155-byte sandbox copy incl. G0011) | Prompt-4 agent | Byte/SHA comparison at intake | at prompt-4 intake | N/A | listing only | NOT_SCHEDULED |
| — | Earlier revision-1 queue items (operator terms, final times, raw captures for G0001–G0009) | unchanged | — | revision-1 | as recorded in revision-1 | as recorded | as recorded | as recorded | as recorded | no new attempt | NOT_SCHEDULED |

## Learning record additions (LEARN-v2)
| Local key | Final score | Regulation | Decision | Final time | Terminal source |
|---|---|---|---|---|---|
| G0010 | Chiba 71 – Hiroshima 89 | same | Hiroshima | last PBP 2026-10-17T07:15:35Z | B.League 506470 · retrieved ≈00:15 AEDT 21 Oct |
| G0011 | Phoenix 115 – Cairns 83 | same | Phoenix | UNKNOWN | ESPN NBL 401875270 · ≈00:12 AEDT |
| G0003 (corners) | corners 1–5 | — | — | — | ESPN ISL 401925434 · ≈00:40 AEDT |

## SETTLEMENT_MANIFEST (effective state after revision-2)
| Item | revision-1 | after revision-2 |
|---|---|---|
| Verified terminal events | 9 | **11** |
| Supplied contract directions | 52 | 52 |
| Sporting W / L | 20 / 20 | **25 / 25** |
| UNRESOLVED | 4 (G0003, G0004 corners) | **2** (G0004 corners) |
| PENDING_EVENT | 8 | **0** |
| Primary Rank-1 / Top-2 denominators | 0 / 0 | 0 / 0 |
| Revision chain | revision-1 for all keys | revision-2 for G0010 (4 keys), G0011 (4), G0003 (2 corner keys), G0004 (2 corner keys); revision-1 effective elsewhere |
| Canonical import / GitHub writes | PENDING / NO | PENDING / NO |

**MINI_SETTLEMENT review row:** `2026-10-21 | MINI 2026101679B3FBCC8D revision-2 | 11 research-only events | 25W-25L of 50 decisive analyst directions, 2 unresolved | primary N/A (no p_card) | DATA_REPAIR_REQUIRED (Algeria corners; frozen-bytes reconciliation) | no rank changes`.

## Verification (S1–S18, revision-2 scope)
S1 PASS (11 keys, revisions mapped) · S2 PENDING_PROMPT_4 (and R2-Q4 bytes question) · S3 PASS (analyst p copied; primary NOT_ESTIMATED kept) · S4 PASS · S5 PASS (C evidence flagged) · S6 PASS (25 + 25 + 2 = 52) · S7 PASS (compact R1–R12 for G0010/G0011; corner-only revisions cite revision-1 for unchanged parts) · S8 PASS (analyst R1 loss G0011 reviewed) · S9 PASS · S10 PASS · S11 PASS (diagnostic only) · S12 PARTIAL (local write only) · S13 PASS (each revision-2 names parent revision-1; no branches) · S14 PARTIAL · S15 PASS · S16 PASS · S17 PARTIAL · S18 PASS.
