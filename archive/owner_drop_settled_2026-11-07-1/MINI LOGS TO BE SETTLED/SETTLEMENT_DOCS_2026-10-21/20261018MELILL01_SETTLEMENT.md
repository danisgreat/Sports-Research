<!-- SETTLEMENT-FORMAT: mini-settlement-10 -->
# SETTLEMENT AND RETROSPECTIVES — MINI 20261018MELILL01

**Document:** `20261018MELILL01_SETTLEMENT.md` · settlement-document revision 1 · prepared 2026-10-21 ≈01:05 AEDT.
**Mode / authority / reading receipt / model scope:** as in `20261018X7Q4M9R2_SETTLEMENT.md` (same folder): `LOCAL_MINI_SETTLEMENT`; `PUBLISHED_MAIN_PINNED 3e29a58693e2ed02ff862e9bf0f751af2feadee1`; Prompt 3 run in the repository session (ENV-v1 deviation disclosed); no repository writes, no hashes; no model output read.

## Frozen source and inventory
**FROZEN_SOURCE:** `Sports_Research_20261018_MEL_ILL_PAK_SL_KP_ZAB_BEI_QWC_CUMULATIVE_UNISSUED_DRAFT.md` (owner attachment; not on disk); `mini-log-10`, self-declared `COMPLETE_STANDALONE_DRAFT_NOT_APPLIED_TO_EXISTING_ACTIVE_MINI`.
Block inventory in order: §A–§D (13 queue rows Q01–Q13; 4 intake rows) → `CARD LOCAL-20261018MELILL01-G0001` → `CARD …-G0002` → heading "Standalone research card — Czech women's 1. liga" → `CARD …-G0003` → format comments → `CARD …-G0004` → `FOOTER`.
Card count 4 (G0001–G0004); all `DRAFT_ONLY / NOT_ISSUED`; no verified writer lease (the mini says so). Freeze 2026-10-21T01:05+11:00; hand-over `NONE`. Bytes/SHA `PENDING_PROMPT_4`. Source growth: none after `END FOOTER` (next proposed key G0005) → `NO_GROWTH_OBSERVED`.
Inventory: 4 cards; 18 supplied contract rows (4+4+4+6); 0 addenda; 0 prior revisions; queue items Q01–Q13 addressed below where outcome evidence closes them.

## LOCAL_ID_MAPPING
| Local key | Native identity | Canonical ID |
|---|---|---|
| `LOCAL-20261018MELILL01-G0001` | NBL27 Round 5, Melbourne United v Illawarra Hawks, 18 Oct 2026 17:00 AEDT, John Cain Arena; ESPN 401875272 | `NOT_ASSIGNED / PENDING_PROMPT_4_IMPORT` |
| `LOCAL-20261018MELILL01-G0002` | Pakistan ODI Tri-Series Match 1, Pakistan v Sri Lanka, Rawalpindi, 18 Oct 2026; ESPNcricinfo 1550713 (series 1550706); ODI no. 5037 | `NOT_ASSIGNED / PENDING_PROMPT_4_IMPORT` |
| `LOCAL-20261018MELILL01-G0003` | Czech women's 1. liga R7, **ŽBK KP Brno** v Žabiny Brno B, 18 Oct 2026 11:15 CEST, STAREZ Aréna Vodova; ČBF match 532124; FIBA LiveStats 2910255 | `NOT_ASSIGNED / PENDING_PROMPT_4_IMPORT` |
| `LOCAL-20261018MELILL01-G0004` | CSL 2026 Round 28, Beijing Guoan v Qingdao West Coast, 18 Oct 2026 19:00 CST, Workers' Stadium; ESPN 401861481 | `NOT_ASSIGNED / PENDING_PROMPT_4_IMPORT` |

## Source discovery, corroboration and reuse register
**Information completion: `INFORMATION_INCOMPLETE`** — G0004 corners single-source (Opta only); G0003 operator label ("KP Brno B") unverified against the operator's event ID; operator terms all; final times for G0001/G0003/G0004.

| Source ID | URL / route | Fields observed / missing | Publisher / independence | Retrieval | Reuse limits |
|---|---|---|---|---|---|
| ML-S01 ESPN NBL scoreboard 18 Oct | `https://site.api.espn.com/apis/site/v2/sports/basketball/nbl/scoreboard?dates=20261018` | MEL 27-16-22-24 = **89**; HWK 21-35-22-13 = **91**; Final; scheduled 06:00Z | ESPN | 2026-10-21 ≈00:12 AEDT | — |
| ML-S02 NBL recap + reports (search-visible) | `https://www.nbl.com.au/news/hawks-hold-out-united-for-critical-win`; `https://au.headtopics.com/news/illawarra-hawks-stun-melbourne-united-in-thrilling-91-89-88932761` | 91–89 Hawks; HT 56–43; 3QT 78–65; Maker 23 off the bench; Anthony 24 | NBL (owner) + independent | search | — |
| ML-S03 ESPN cricket summary/bbb 1550713 | `…/sports/cricket/1550706/summary?event=1550713`; `…/playbyplay?event=1550713&period=1` | Result: Pakistan won by 37 runs; PAK **305 all out in 49.5 ov** (innings 1); after 5.0 ov **31/1**; after 6.0 ov 32/2; first ball 2026-10-18T08:02:47Z (**19:02:47 AEDT**); PAK innings end 12:07:32Z; SL 268 (48.1) | ESPN/Cricinfo | ≈00:22 AEDT | 5-over checkpoint single lineage |
| ML-S04 ProPakistani / CricTracker / Sri Lanka Mirror / Dialogue Pakistan (search-visible) | `https://propakistani.pk/2026/10/19/pakistan-beat-sri-lanka-to-make-winning-start-to-odi-tri-series/`; `https://www.crictracker.com/…2593/` | 305 in 49.5; Agha 107 (90); SL 268 in 48.1; Malinga 4/46 | Independent publishers | search | — |
| ML-S05 ČBF match page 532124 (via r.jina.ai) | `https://www.cbf.cz.basketball/zapas/532124` | ŽBK KP Brno **82:51** Žabiny Brno B; cumulative 30:11, 59:25, 75:37; date 18.10.2026 11:15; venue STAREZ Aréna Vodova hala 3 | ČBF (field owner) | ≈00:30 AEDT | `sec.cz.basketball` and `cz.basketball` returned 403 directly |
| ML-S06 FIBA LiveStats 2910255 | `https://fibalivestats.dcd.shared.geniussports.com/data/2910255/data.json` | KP 30-29-16-7 = 82; Žabiny B 11-14-12-14 = 51; period 4 REGULAR, clock 00:00 | Genius Sports official stats feed (scorer's table) | ≈00:31 AEDT | Same scoring event, different system from ČBF page |
| ML-S07 ČBF team 15882 (KP Brno B) (via r.jina.ai) | `https://www.cbf.cz.basketball/tym/15882` | KP Brno B is an U17 team; on 18 Oct it played SKB Fastav Zlín (75:40, 10:00); its fixtures v Žabiny Brno B are 7 Nov and 8 Nov | ČBF | ≈00:31 AEDT | Resolves the card's identity conflict by elimination |
| ML-S08 ESPN CSL summary 401861481 | `…/soccer/chn.1/summary?event=401861481` | Beijing **1–0**; HT **0–0** (45'+3'); Zhang Yuning header 78'; end 90'+7'; `wonCorners` Beijing **5**, Qingdao **5** | ESPN/Opta | ≈00:08 AEDT | Corner count single source |
| ML-S09 163.com / Sohu / Sina / ifeng (search-visible) | `https://www.163.com/dy/article/L9I5JH5I0552YIYQ.html`; `https://k.sina.com.cn/article_1644114654_61ff32de02002buzg.html` | 1–0; first half 0–0; 78' header from a Sérgio corner; Fábio injured 16'–21' | Independent Chinese publishers | search | No corner totals published in results seen |

**SOURCE_SEARCH_ATTEMPTS:** G0001 — web search (index initially stale) → ESPN NBL API → NBL recap search. G0002 — ESPN scorepanel → summary → bbb pages (one 502 retried) → search. G0003 — `sec.cz.basketball` (403), `cz.basketball` (403), `cbf.cz.basketball` via r.jina.ai (found) → FIBA LiveStats JSON → team 15882 schedule. G0004 — ESPN scoreboard/summary → Chinese search for result → Chinese search "角球 技术统计" (no corner figures found; the only corner figures surfaced were from the 19 May reverse fixture, 3–9, and were rejected as a different event).

**REQUIREMENT_CLOSURE**
| Field | Status | Sources | Next · actor · due · automation |
|---|---|---|---|
| G0001 final/quarters/OT | CLOSED | ML-S01 + S02 | — |
| G0002 PAK innings total; 5-over score; result | CLOSED (5-over single lineage, ball-level) | ML-S03 + S04 | PCB scorecard over summary · prompt 4 · NOT_SCHEDULED |
| G0003 final/quarters/OT | CLOSED | ML-S05 + S06 | — |
| G0003 identity v user label "KP Brno B" | CLOSED_BY_ELIMINATION for the sporting event; operator label OPEN | ML-S07 | Operator event ID · owner · NOT_SCHEDULED |
| G0004 goals, HT | CLOSED | ML-S08 + S09 | — |
| G0004 corners (10 v 10.5 line) | PROVISIONAL — single source, one corner from the line | ML-S08 | CSL/club technical stats or second data provider · prompt 4 · NEXT_OWNER_INVOKED · NOT_SCHEDULED |
| Operator terms all | OPEN | — | owner |
| Final times G0001/G0003/G0004 | UNKNOWN | — | gamebooks |

<!-- BEGIN SETTLEMENT LOCAL-20261018MELILL01-G0001 revision-1 -->
### Settlement · LOCAL-20261018MELILL01-G0001 · Melbourne United v Illawarra Hawks · 2026-10-21T01:05+11:00
**Revision:** revision-1 · parent NONE · effective 2026-10-21T01:05+11:00 · affected keys ALL four · changes NONE.
**Card state:** `SETTLED` (draft research record).
**Final event:** Melbourne United **89** – Illawarra Hawks **91**, regulation (27-16-22-24 v 21-35-22-13). Total 180; Melbourne margin −2. Final time `UNKNOWN`.
**Definition status:** full game incl. OT (card); no OT. Operator `UNKNOWN_DEFINITION`. **Evidence:** B (ESPN + NBL recap).
**Expected vs final:** total 189.945 (σ 21) → 180: −9.95, z −0.47. Melbourne margin +4.85 (σ 17) → −2: −6.85, z −0.40.

| Rank | Exact original proposition | Original p_card | Original BASELINE_P | Grade | Evidence | Counts toward wins | Basis |
|---|---|---:|---:|---|---|---|---|
| 1 | **Combined points Under 201.5** | 0.709 | 0.845 (STALE_COMPARATOR) | **WIN** | B | Research-record primary | 180 |
| 2 | **Illawarra Hawks +10.5** | 0.630 | 0.722 | **WIN** | B | Research-record primary | Hawks won |
| 3 | Melbourne United −10.5 | 0.370 | 0.278 | **LOSS** | B | No | |
| 4 | Combined points Over 201.5 | 0.291 | 0.155 | **LOSS** | B | No | |

**Top-two result:** `ALL_WON`; 2/2.
**ML execution and feedback:** `NOT_APPLICABLE_NO_MODEL`.
**Proper scores (card / baseline / d_Brier; negative favours card):** R1 0.0847 / 0.0240 / **+0.0607**; R2 0.1369 / 0.0773 / **+0.0596**; R3 0.1369 / 0.0773 / +0.0596; R4 0.0847 / 0.0240 / +0.0607. The stale 2025-26 NBL league-only comparator out-scored the card on every row of this event (descriptive, n = 1 event).
**Shadow results:** none. **Form-window check:** `NOT_APPLICABLE` (shrinkage only, no separate form overlay).
**Winner call:** Melbourne ≈0.612 → **incorrect**.
**R1.** Rank 1 Under 201.5 (0.709); Rank 2 Hawks +10.5 (0.630). **R2.** 89–91 verified. **R3.** 180 ≤ 201; Hawks +2 margin vs threshold −10. **R4.** 2/2; Hit@2 hit; NDCG 1.0. **R5.** Wrong. **R6.** Total 21.5 under; Hawks covered by 12.5. **R7.** Both errors within 0.5σ. **R8.** Hawks won Q2 35–16 (Maker 23 off the bench, ML-S02); wins checked for the same defect as losses: starters were unconfirmed at issue. **R9.** Card completed after the scheduled 17:00 tip; `POST_SCHEDULED_START_DRAFT`; no outcome used. **R10.** Process `DEFICIENT` (post-start, starters unconfirmed); class for winner miss `CENTRE_MISS_SMALL_N`. **R11.** `PROPOSED_NOT_TESTED`: none from one aligned result. **R12.** `NO_CHANGE`; note baseline out-performed card on this event.
<!-- END SETTLEMENT LOCAL-20261018MELILL01-G0001 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261018MELILL01-G0002 revision-1 -->
### Settlement · LOCAL-20261018MELILL01-G0002 · Pakistan v Sri Lanka, ODI Tri-Series Match 1 · 2026-10-21T01:05+11:00
**Revision:** revision-1 · parent NONE · effective 2026-10-21T01:05+11:00 · affected keys ALL four · changes NONE.
**Card state:** `SETTLED`.
**Final event:** Sri Lanka won the toss and fielded (card's secondary-source toss confirmed: Pakistan is innings 1 in the feed). Pakistan **305 all out in 49.5 overs**; after 5.0 overs **31/1**. Sri Lanka 268 all out (48.1). Pakistan won by 37 runs. First ball 19:02:47 AEDT; PAK innings ended 2026-10-18T12:07:32Z.
**Definition status:** card A2 — first innings until 50 overs or all out; 30 legal balls. Both endpoints reached; no DLS/reduction. Operator `UNKNOWN_DEFINITION`.
**Evidence:** B (ball-by-ball feed + four independent reports; 5-over field single lineage).
**Expected vs final:** innings 277.75 (σ 52 base) → 305: +27.25, z +0.52. 5-over 29.5 (σ 11) → 31: +1.5, z +0.14.

| Rank | Exact original proposition | Original p_card | Original BASELINE_P | Grade | Evidence | Counts toward wins | Basis |
|---|---|---:|---|---|---|---|---|
| 1 | **Pakistan 1st innings Under 311.5** | 0.732 | BASELINE_UNAVAILABLE | **WIN** | B | Research-record primary | 305 |
| 2 | **Pakistan after 5 overs Over 26.5** | 0.606 | BASELINE_UNAVAILABLE | **WIN** | B | Research-record primary | 31 |
| 3 | Pakistan after 5 overs Under 26.5 | 0.394 | BASELINE_UNAVAILABLE | **LOSS** | B | No | |
| 4 | Pakistan 1st innings Over 311.5 | 0.268 | BASELINE_UNAVAILABLE | **LOSS** | B | No | |

**Top-two result:** `ALL_WON`; 2/2.
**ML execution and feedback:** `NOT_APPLICABLE_NO_MODEL`.
**Proper scores:** R1 (1−0.732)² = 0.0718; R2 (1−0.606)² = 0.1552; R3 0.1552; R4 0.0718.
**Winner call:** Pakistan ≈0.60 (qualitative) → **correct**.
**R1.** Rank 1 Under 311.5 (0.732); Rank 2 5-over Over 26.5 (0.606). **R2.** 305 (49.5 ov); 31/1 at 5.0. **R3.** 305 ≤ 311; 31 ≥ 27. **R4.** 2/2; Hit@2 hit; NDCG 1.0. **R5.** Correct. **R6.** Innings 6.5 runs under 311.5 (−0.13σ); 5-over 4.5 runs over 26.5. **R7.** Innings above the 277.75 centre but below the line; the card's HIGH scenario (300) was closest. **R8.** Agha 107 lifted the total; being all out with one ball left capped it. Wins checked: XIs were unverified at issue (same gap as elsewhere). **R9.** First ball 19:02:47 AEDT; card's research check after 19:06 → `POST_START_ISSUE`. **R10.** Process `DEFICIENT` (post-start; XIs unconfirmed); outcomes inside the issued distribution. **R11/R12.** `NO_CHANGE`.
<!-- END SETTLEMENT LOCAL-20261018MELILL01-G0002 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261018MELILL01-G0003 revision-1 -->
### Settlement · LOCAL-20261018MELILL01-G0003 · ŽBK KP Brno v Žabiny Brno B · 2026-10-21T01:05+11:00
**Revision:** revision-1 · parent NONE · effective 2026-10-21T01:05+11:00 · affected keys ALL four · changes NONE.
**Card state:** `SETTLED` on the sporting event; operator-identity label `OPEN`.
**Identity:** the card priced the federation match 532124 (ŽBK KP Brno) conditionally because the request said "KP Brno B". ČBF shows KP Brno B is an U17 side that played Zlín at 10:00 the same day and meets Žabiny Brno B only on 7–8 Nov (ML-S07). The only 18 Oct 11:15 KP–Žabiny B game is 532124, so the sporting identity is closed by elimination; whether the user's operator listed this exact event remains unverified.
**Final event:** **ŽBK KP Brno 82 – Žabiny Brno B 51**, regulation (KP 30-29-16-7; Žabiny 11-14-12-14). Total 133; Žabiny margin −31. Final time `UNKNOWN`.
**Definition status:** full game incl. OT; ±4.0 handicap with a push at exactly 4; no OT and no push. Operator `UNKNOWN_DEFINITION`.
**Evidence:** A (ČBF field owner + FIBA LiveStats).
**Expected vs final:** total 129.8 (σ 21) → 133: +3.2, z +0.15. Žabiny margin +6.0 (σ 16) → −31: −37.0, z **−2.31** (|z| > 2).

| Rank | Exact original proposition | Original p_card (decisive) | Original W / P / L | Original BASELINE_P | Grade | Evidence | Counts toward wins |
|---|---|---:|---|---|---|---|---|
| 1 | **Total Under 139.5** | 0.678 | 0.678 / 0 / 0.322 | NOT_DERIVED_EXACT_COMPETITION | **WIN** | A | Research-record primary |
| 2 | **Žabiny Brno B −4.0** | 0.551 | 0.5374 / 0.0247 / 0.4379 | NOT_DERIVED_EXACT_COMPETITION | **LOSS** | A | Research-record primary |
| 3 | ŽBK KP Brno +4.0 | 0.449 | 0.4379 / 0.0247 / 0.5374 | NOT_DERIVED_EXACT_COMPETITION | **WIN** | A | No |
| 4 | Total Over 139.5 | 0.322 | 0.322 / 0 / 0.678 | NOT_DERIVED_EXACT_COMPETITION | **LOSS** | A | No |

**Top-two result:** `SPLIT`; 1/2.
**ML execution and feedback:** `NOT_APPLICABLE_NO_MODEL`.
**Proper scores:** binary — R1 (1−0.678)² = 0.1037; R2 0.551² = 0.3036; R3 (1−0.449)² = 0.3036; R4 0.322² = 0.1037. Categorical half-sum on the push-capable vectors (separate, labelled): R2 0.5×(0.5374² + 0.0247² + 0.5621²) = **0.3027**; R3 identical 0.3027.
**Winner call:** Žabiny B ≈0.646 → **incorrect** (KP won by 31).
**R1.** Rank 1 Under 139.5 (0.678); Rank 2 Žabiny −4 (0.551). **R2.** 82–51; verified two systems. **R3.** 133 ≤ 139; Žabiny −31 vs required +5. **R4.** 1/2; Hit@2 hit; NDCG 1/1.631 = 0.613. **R5.** Wrong. **R6.** Total 6.5 under; handicap missed by 35 points. **R7.** Margin error −37 (z −2.31) — a tail result against the stated width. **R8.** ČBF team stats (ML-S05): KP shot 34.8% from three vs Žabiny 5.0%, and out-rebounded them 57–40. The card had no confirmed lineups for either side, and both teams had played the previous day. Supported observation; cause shares not assessable. **R9.** Card begun before tip, completed time unverified; `ISSUE_PHASE_UNVERIFIED`. **R10.** Process `DEFICIENT` (identity conflict and unconfirmed lineups at issue, per the card's own audit); class `SIDE_CENTRE_MISS / TAIL`. **R11.** `PROPOSED_NOT_TESTED`: second-tier women's leagues with reserve ("B") teams may need much wider margin widths and a roster-availability gate. **R12.** `PROPOSE_EXPERIMENT`.
<!-- END SETTLEMENT LOCAL-20261018MELILL01-G0003 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261018MELILL01-G0004 revision-1 -->
### Settlement · LOCAL-20261018MELILL01-G0004 · Beijing Guoan v Qingdao West Coast · 2026-10-21T01:05+11:00
**Revision:** revision-1 · parent NONE · effective 2026-10-21T01:05+11:00 · affected keys ALL six directions · changes NONE.
**Card state:** `SETTLED` (corner rows on provisional single-source evidence C).
**Final event:** **Beijing Guoan 1–0 Qingdao West Coast**, half-time **0–0**, Zhang Yuning header 78' (from a corner). Corners per ESPN/Opta `wonCorners`: Beijing **5**, Qingdao **5** = **10**. KO 11:00Z (22:00 AEDT). Final time `UNKNOWN`.
**Definition status:** 90 min + stoppage. The card left the corner provider definition "unconfirmed"; this settlement uses the framework's default ESPN/Opta `wonCorners` route (RULES_SOCCER §0 as cited by the sibling soccer cards). A one-corner discrepancy in any other provider would flip both corner rows → evidence **C**, sensitivity view only, until corroborated. Operator `UNKNOWN_DEFINITION`.
**Expected vs final:** Beijing 1.90 → 1; Qingdao 1.23 → 0; FT 3.13 (Poisson SD 1.77) → 1: −2.13, z −1.20; 1H 1.155 → 0: −1.155; corners 9.50 (Poisson SD 3.08) → 10: +0.5, z +0.16.

| Rank | Exact original proposition | Original p_card | Original BASELINE_P | Grade | Evidence | Counts toward wins | Basis |
|---|---|---:|---|---|---|---|---|
| 1 | **Combined corners Under 10.5** | 0.645 | NOT_FROZEN_DATE_VERIFIED | **WIN** | **C** | Research-record primary (sensitivity view) | 10 |
| 2 | **Combined goals Over 2.5** | 0.605 | NOT_FROZEN_DATE_VERIFIED | **LOSS** | B | Research-record primary | 1 goal |
| 3 | Combined goals Under 2.5 | 0.395 | NOT_FROZEN_DATE_VERIFIED | **WIN** | B | No | |
| 4 | Combined corners Over 10.5 | 0.355 | NOT_FROZEN_DATE_VERIFIED | **LOSS** | C | No | |
| diag | 1H goals Over 0.5 (family-ineligible for Rank 1) | 0.685 | — | **LOSS** | B | No | HT 0–0 |
| diag | 1H goals Under 0.5 | 0.315 | — | **WIN** | B | No | |
| — | Winner 3-way (informational): Beijing 0.530 / D 0.224 / Qingdao 0.246 | — | — | Beijing | B | No | |

**Top-two result:** `SPLIT`; 1/2 (R1 on evidence C — headline view excludes it pending corroboration).
**ML execution and feedback:** `NOT_APPLICABLE_NO_MODEL`.
**Proper scores:** R1 (1−0.645)² = 0.1260 [C]; R2 0.605² = 0.3660; R3 (1−0.395)² = 0.3660; R4 0.355² = 0.1260 [C]; 1H O 0.685² = 0.4692; 1H U (1−0.315)² = 0.4692. Three-way winner half-sum 0.5×(0.470² + 0.224² + 0.246²) = 0.5×0.3317 = **0.1659**.
**Winner call:** Beijing → **correct**.
**R1.** Rank 1 corners Under 10.5 (0.645, GATE_UNRESOLVED_PRECISION at issue); Rank 2 FT Over 2.5 (0.605). **R2.** 1–0 / HT 0–0 verified on two lineages; corners 10 single-source. **R3.** 10 ≤ 10; 1 ≤ 2. **R4.** 1/2; Hit@2 hit; NDCG 0.613. **R5.** Correct. **R6.** Corners 0.5 under the line (one corner from flipping); goals 1.5 under 2.5. **R7.** Goals far below the 3.13 centre (z −1.20) — the card's goal centre came from realised GF/GA, not xG, and the card said so. **R8.** Beijing's Fábio left injured at 16'–21' (ML-S09), removing a set-piece and box focal point; supported observation, effect not measurable. **R9.** Card begun ~21:39 AEDT, KO 22:00; completion time unverified → `ISSUE_PHASE_UNVERIFIED`; lineups unconfirmed at issue. **R10.** Process `DEFICIENT` on lineup closure; R2 class `CENTRE_HIGH (realised-goals proxy) / VARIANCE`. **R11.** `PROPOSED_NOT_TESTED`: CSL goal centres from realised goals overshot here; compare against an xG-based centre when a verified xG source exists. **R12.** `MONITOR`; corroborate corners.
<!-- END SETTLEMENT LOCAL-20261018MELILL01-G0004 revision-1 -->

## Shadows and legacy bundles for prompt 6
None.

## UNRESOLVED_CARRYOVER
Disposition of the mini's own queue: Q01/Q02 (MEL–ILL lineups, efficiency) — outcome settled; research-side gaps remain historical, no action. Q03 (mini identity/lease) — still OPEN for prompt 4. Q04–Q06 (PAK–SL) — outcome settled; operator rules remain OPEN. Q07 (KP identity) — sporting identity CLOSED_BY_ELIMINATION; operator label OPEN. Q08/Q09 — outcome settled; research-side gaps historical. Q10–Q12 (Beijing lineups/injuries/baselines) — research-side, historical. Q13 (operator 90-min/abandonment) — OPEN.

| ID | Event key | Queue | Original card | Latest revision | Open field | Responsible actor | Next source + exact field | Due | Final-time basis | Last attempt | Scheduled automation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ML-Q1 | G0004 | UNRESOLVED_EVIDENCE (grade-sensitive) | G0004 | revision-1 | Corner count corroboration (10 v 10.5) | Prompt-4 agent | CSL official technical statistics or a second provider: corners per side | NEXT_OWNER_INVOKED | UNKNOWN | 2026-10-21 ≈00:50 AEDT (Chinese search; no figures) | NOT_SCHEDULED |
| ML-Q2 | G0003 | UNRESOLVED_DEFINITION | G0003 | revision-1 | Operator event ID for "KP Brno B (W) v Zabiny Brno B (W)" | Owner | Operator ticket/event listing | NEXT_OWNER_INVOKED | N/A | — | NOT_SCHEDULED |
| ML-Q3 | MINI | CUSTODY | — | — | Active original, writer lease, issue status of all four drafts | Owner / prompt 4 | Owner decision at intake | NEXT_OWNER_INVOKED | N/A | — | NOT_SCHEDULED |
| ML-Q4 | all | UNRESOLVED_EVIDENCE | all | revision-1 | Operator terms; final wall-clock times | Owner / prompt 4 | Operator rules; gamebooks | NEXT_OWNER_INVOKED | UNKNOWN | — | NOT_SCHEDULED |

## Learning record (LEARN-v2)
| Local key | Final score | Regulation | Decision | Final time | Terminal source (retrieved) |
|---|---|---|---|---|---|
| G0001 | MEL 89 – ILL 91 | same | Illawarra | UNKNOWN | ESPN NBL 401875272 · ≈00:12 AEDT 21 Oct |
| G0002 | PAK 305 (49.5) – SL 268 (48.1); PAK 31/1 at 5 ov | same | Pakistan by 37 | PAK inns end 2026-10-18T12:07:32Z | ESPN cricket 1550713 · ≈00:22 AEDT |
| G0003 | KP Brno 82 – Žabiny B 51 | same | KP Brno | UNKNOWN | ČBF 532124 + FIBA LS 2910255 · ≈00:31 AEDT |
| G0004 | Beijing 1–0 Qingdao (HT 0–0); corners 5–5 (single source) | same | Beijing | UNKNOWN | ESPN 401861481 · ≈00:08 AEDT |

## SETTLEMENT_MANIFEST
| Item | Value |
|---|---|
| Frozen source | `Sports_Research_20261018_MEL_ILL_PAK_SL_KP_ZAB_BEI_QWC_CUMULATIVE_UNISSUED_DRAFT.md`; 4 draft cards; bytes/SHA PENDING_PROMPT_4 |
| Revisions | revision-1 × 4 |
| Contract rows | 18: **9 W / 9 L / 0 PUSH / 0 VOID / 0 UNRESOLVED** (2 corner rows on evidence C) |
| Primary rows | 8: **6 W / 2 L** — Rank 1: 4 W / 0 L (one on C); Rank 2: 2 W / 2 L |
| Headline view (evidence A/B only) | primary 5 W / 2 L (G0004 R1 excluded pending corroboration) |
| Card classes | ALL_WON 2 (G0001, G0002), SPLIT 2 (G0003, G0004) |
| Hit@2 | 4/4 |
| Mean binary Brier, primary (n=8) | (0.0847+0.1369+0.0718+0.1552+0.1037+0.3036+0.1260+0.3660)/8 = **0.1685** |
| Baseline pairs | 4 rows (G0001); mean d_Brier **+0.0602** (baseline better; one event) |
| Timing | G0001 POST; G0002 POST (first ball 19:02:47); G0003 UNVERIFIED; G0004 UNVERIFIED; all NOT_ISSUED drafts |
| Rank-1 LOSS deep reviews | 0 required |
| Canonical import / GitHub writes | PENDING / NO |

**MINI_SETTLEMENT review row:** `2026-10-21 | MINI 20261018MELILL01 | 4 draft records / 18 rows | primary 6W-2L, mean Brier 0.169 (n=8); NBL card worse than stale league baseline on 4 paired rows | INSUFFICIENT_EVIDENCE | data: Beijing corners single-source | no rank changes`.

## Verification S1–S18
S1 PASS · S2 PENDING_PROMPT_4 · S3 PASS · S4 PASS · S5 PASS (evidence C flagged) · S6 PASS (9 + 9 = 18) · S7 PASS · S8 PASS (no R1 losses; wins checked for lineup gaps) · S9 PASS (baseline coverage 4/18) · S10 PASS · S11 PASS · S12 PARTIAL · S13 PASS · S14 PARTIAL · S15 PASS · S16 PASS · S17 PARTIAL · S18 PASS.
