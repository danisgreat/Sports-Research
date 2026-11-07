<!-- SETTLEMENT-FORMAT: mini-settlement-10 -->
# SETTLEMENT AND RETROSPECTIVES — MINI 20261018Q7N4T9B2

**Document:** `20261018Q7N4T9B2_SETTLEMENT.md` · settlement-document revision 1 · prepared 2026-10-21 ≈00:55 AEDT.
**Mode / authority / reading receipt / model scope:** as in `20261018X7Q4M9R2_SETTLEMENT.md` (same folder): `LOCAL_MINI_SETTLEMENT`; `PUBLISHED_MAIN_PINNED 3e29a58693e2ed02ff862e9bf0f751af2feadee1`; Prompt 3 run in the repository session (ENV-v1 deviation disclosed); no repository writes, no hashes; no model output read.

## Frozen source and inventory
**FROZEN_SOURCE:** `20261018Q7N4T9B2_UPDATED_G0004_KIA_LG.md` (owner attachment; not on disk); format `mini-log-10`.
Block inventory in order: §A–§D (intake rows `INTAKE-MINI-INIT-20261018`, `…-G0001-FE-NAGOYA-OKAYAMA…`, `…-G0002-TNT-CONVERGE…`, `…-G0003-OSASUNA-RACING…`, `…-G0004-KIA-LG…`; two dated carryover addenda inside §C for G0001 and G0002) → `CARD …-G0001` → `CARD …-G0002` → `CARD …-G0003` → `CARD …-G0004` → `FOOTER`.
Card blocks 4 (G0001–G0004). **Status note:** the footer records G0001–G0003 as inherited draft cards and G0004 as an *unissued* research draft whose ordinal was "not consumed"; every card header says `READ_ONLY_DRAFT / NOT_ISSUED` or `OWNER-SAVE_DRAFT`. All four are settled here as retained research records (Prompt 3 "settle every card equally"); none is a verified issued prospective card. Freeze 2026-10-21T00:55+11:00. Lease (17:15 18 Oct → 17:15 19 Oct) expired; hand-over `NONE`. Bytes/SHA `PENDING_PROMPT_4`. Source growth: none after `END FOOTER` → `NO_GROWTH_OBSERVED`.
Inventory: 4 card blocks; 18 supplied contract rows (4+4+6+4); 0 settlement revisions before this; inherited canonical §C queue external and unchanged.

## LOCAL_ID_MAPPING
| Local key | Native identity | Canonical ID |
|---|---|---|
| `LOCAL-20261018Q7N4T9B2-G0001` | B.LEAGUE ONE 2026-27 Round 5, FE Nagoya v Tryhoop Okayama, 18 Oct 2026, ScheduleKey 507258 | `NOT_ASSIGNED / PENDING_PROMPT_4_IMPORT` |
| `LOCAL-20261018Q7N4T9B2-G0002` | PBA Season 50 Governors' Cup Group A, TNT Tropang 5G v Converge FiberXers, 18 Oct 2026 17:15 PHT, Ynares Center Antipolo; RealGM 544796 | `NOT_ASSIGNED / PENDING_PROMPT_4_IMPORT` |
| `LOCAL-20261018Q7N4T9B2-G0003` | LaLiga 2026-27 MD9, CA Osasuna v Racing Santander, 18 Oct 2026 14:00 CEST, El Sadar; ESPN 401882840 | `NOT_ASSIGNED / PENDING_PROMPT_4_IMPORT` |
| `LOCAL-20261018Q7N4T9B2-G0004` (proposed, unissued) | KBO 2026 semi-playoff Game 3, KIA @ LG, 20 Oct 2026, Jamsil; gameId `20261020HTLG0` | `NOT_ASSIGNED / PENDING_PROMPT_4_IMPORT` (ordinal itself awaits owner reconciliation) |

## Source discovery, corroboration and reuse register
**Information completion: `INFORMATION_INCOMPLETE`** — operator OT/action terms (decisive for G0002, where the contract endpoint changes grades), PBA field-owner box, final wall-clock times (G0002, G0003), G0002 venue label conflict (Antipolo vs RealGM "Pasig").

| Source ID | URL / route | Fields observed / missing | Publisher / independence | Retrieval | Reuse limits |
|---|---|---|---|---|---|
| Q7-S01 B.League game record 507258 | `https://www.bleague.jp/game_detail/?ScheduleKey=507258&tab=1` (embedded JSON) | `GameEndedFlg/RecordFixedFlg true`; FE 30-23-17-12 = **82**; OKA 21-32-18-18 = **89**; MaxPeriod 4; attendance 2,686; first PBP 2026-10-18T06:40:16Z, last 08:49:16Z; starters FE Tinkle, Sugimoto, Tsukioka, Yasuoka, Fiedler; OKA Garcia, Sow, Fofana, Jackson, Yokoyama | B.LEAGUE (field owner) | 2026-10-21 ≈00:15 AEDT | Static text shows "--"; values read from embedded record |
| Q7-S02 KSB / FE club result (search-visible) | `https://news.ksb.co.jp/article/16971854`; `https://www.fightingeagles.jp/news/detail/id=20545` | Okayama 89–82, first back-to-back wins | KSB broadcaster; FE club | search 2026-10-21 | Independent of league feed |
| Q7-S03 RealGM scoreboard + box 544796 (via r.jina.ai) | `https://basketball.realgm.com/international/boxscore/2026-10-18/Converge-Fiber-Xers-at-Talk-N-Text-Tropang-Texters/544796` | XERS 27-28-19-32 **OT 8** = 114; TNT 35-21-30-20 **OT 6** = 112; regulation 106–106; starters both sides; venue label "Ynares Arena, Pasig" | RealGM compiler | ≈00:27 AEDT | Not field owner |
| Q7-S04 Tribune / Inquirer / GMA / Philstar / Manila Bulletin (search-visible) | `https://tribune.net.ph/2026/10/18/converge-clips-tnt-in-ot`; `https://sports.inquirer.net/702222/…`; `https://www.philstar.com/sports/2026/10/18/2564111/…` | Converge 114–112 in OT at Ynares Center **Antipolo**; Stockton forced OT and scored the go-ahead layup with 11.3 s left | Independent Philippine publishers | search | Corroborates OT and venue (Antipolo) |
| Q7-S05 ESPN soccer summary 401882840 | `…/soccer/esp.1/summary?event=401882840` | Osasuna 2–0, halves 1–0 / 1–0; HT end 45'+4'; Osambela 88'; `wonCorners` Osasuna **7**, Racing **4** | ESPN/Opta | ≈00:10 AEDT | Corner route per RULES_SOCCER §0 (card A2 pre-registration) |
| Q7-S06 YSScores / ScoreTab / StatsChecker / SofaScore news / La Nación (search-visible) | `https://www.ysscores.com/en/match/5868097/CA-Osasuna-vs-Racing-Santander`; `https://www.sofascore.com/news/osasuna-2-0-real-racing-club-xg-backs-a-clear-win`; `https://www.lanacion.com.ar/deportes/canchallena/osasuna-vencio-2-0-a-racing-de-santander-por-la-liga-de-espana-2026-nid18102026/` | 2–0; Budimir penalty 9'; Osambela 88'; corners **7–4** (SofaScore, La Nación) | Independent publishers; corner data likely shares Opta lineage | search | Corner corroboration lineage not proven independent |
| Q7-S07 KBO GetScoreBoardScroll | POST `https://www.koreabaseball.com/ws/Schedule.asmx/GetScoreBoardScroll` `leId=1&srId=3&seasonId=2026&gameId=20261020HTLG0` | KIA 0-7-0-0-1-1-1-3-0 = **13** (H16 E0); LG 0-0-0-0-0-1-0-0-0 = **1** (H8 E1); START 18:31, END 21:58 KST; series KIA 3–0 | KBO (field owner) | ≈00:35 AEDT | CROWD_CN reported 0 (field not populated) |
| Q7-S08 Sports Kyunghyang (search-visible) | `https://sports.khan.co.kr/article/202610202159003/` | LG 1–13; KIA 7-run 2nd incl. Kim Do-yeong grand slam; LG's run in the 6th at 0–9 | Independent Korean publisher (21:59 KST) | search | — |

**SOURCE_SEARCH_ATTEMPTS:** G0001 — B.League page raw fetch (text "--" → embedded JSON parsed); search "トライフープ岡山 FE名古屋 89-82". G0002 — search (index had no result) → RealGM direct (Cloudflare) → r.jina.ai proxy scoreboard + box → search "Converge beats TNT 114-112 overtime". pba.ph homepage reachable (200) but game page not located. G0003 — ESPN scoreboard/summary; search for 2–0 and for corner corroboration. G0004 — KBO JSON route (memory reference) → Korean search (first attempt previews only; second found the result).

**REQUIREMENT_CLOSURE**
| Event / field | Status | Sources | Next · actor · due · automation |
|---|---|---|---|
| G0001 final, quarters, OT | CLOSED | Q7-S01 + S02 | — |
| G0002 final, regulation, OT | CLOSED | Q7-S03 + S04 | PBA owner box · prompt-4 · NOT_SCHEDULED |
| G0002 operator endpoint (incl./excl. OT) | OPEN — grade-changing | — | Owner written terms · owner · before operator use · NOT_SCHEDULED |
| G0003 goals, HT | CLOSED | Q7-S05 + S06 | — |
| G0003 corners 11 | CLOSED (two publishers; Opta lineage likely shared) | Q7-S05 + S06 | LaLiga official stats · prompt-4 · NOT_SCHEDULED |
| G0004 final, innings | CLOSED | Q7-S07 + S08 | — |
| Final wall-clock times | G0001 08:49:16Z (last PBP); G0004 21:58 KST; G0002/G0003 UNKNOWN | — | owner gamebooks |
| Operator terms all | OPEN — UNKNOWN_DEFINITION | — | owner |

<!-- BEGIN SETTLEMENT LOCAL-20261018Q7N4T9B2-G0001 revision-1 -->
### Settlement · LOCAL-20261018Q7N4T9B2-G0001 · Fighting Eagles Nagoya v Tryhoop Okayama · 2026-10-21T00:55+11:00
**Revision:** revision-1 · parent NONE · effective 2026-10-21T00:55+11:00 · affected keys ALL four · changes NONE.
**Card state:** `SETTLED` (research draft record).
**Final event:** FE Nagoya **82** – Tryhoop Okayama **89**, regulation (30-23-17-12 v 21-32-18-18). Total 171; Nagoya margin −7. Tip 2026-10-18T06:40:16Z = **17:40:16 AEDT**; last PBP 08:49:16Z.
**Definition status:** full game incl. OT (card A2); no OT. Operator `UNKNOWN_DEFINITION`. **Evidence:** A (owner record) + independent broadcaster.
**Expected vs final:** total 159.5 (σ 20) → 171: +11.5, z +0.58. Nagoya margin +2.0 (σ 20) → −7: −9.0, z −0.45.

| Rank | Exact original proposition | Original p_card | Original BASELINE_P | Grade | Evidence | Counts toward wins | Basis |
|---|---|---:|---|---|---|---|---|
| 1 | **Fighting Eagles Nagoya +1.5** | 0.568 | NOT_ESTIMATED | **LOSS** | A | Yes | lost by 7 |
| 2 | **Combined Under 161.5** | 0.538 | NOT_ESTIMATED | **LOSS** | A | Yes | 171 |
| 3 | Combined Over 161.5 | 0.462 | NOT_ESTIMATED | **WIN** | A | No | |
| 4 | Tryhoop Okayama −1.5 | 0.432 | NOT_ESTIMATED | **WIN** | A | No | won by 7 |

**Top-two result:** `ALL_LOST`; denominator 2; 0/2.
**ML execution and feedback:** `NOT_APPLICABLE_NO_MODEL`.
**Proper scores:** R1 0.568² = 0.3226; R2 0.538² = 0.2894; R3 0.2894; R4 0.3226. Baseline pairs 0.
**Shadow results:** none. **Form-window check:** `NOT_APPLICABLE` (no form adjustment; card centre was a raw season blend).
**Winner call:** Nagoya ≈0.539 → **incorrect**.
**R1.** Rank 1 Nagoya +1.5 (0.568); Rank 2 Under 161.5 (0.538). **R2.** 82–89 verified on owner record. **R3.** Nagoya −7 < −1.5; 171 ≥ 162. **R4.** 0/2; Hit@2 miss; NDCG 0. **R5.** Wrong. **R6.** Margin 5.5 points beyond the +1.5 threshold; total 9.5 points over 161.5. **R7.** Both errors within ~0.6σ of the stated widths. **R8.** Okayama won the second quarter 32–23 (owner record). Lineup: the card's last-confirmed FE five had Harima; the actual FE five had Sugimoto instead (Q7-S01) — a confirmed-lineup gap at issue, cause share not measurable. **R9.** Tip 17:40:16 AEDT; the card's artifact was assembled after 17:41:02 AEDT → `POST_START_ISSUE` confirmed by the owner PBP timestamp. **R10.** Process `DEFICIENT` (post-start, starters unconfirmed); model uncalibrated; class `NEAR_COINFLIP / CENTRE_MISS_SMALL_N (n=8)`. **R11.** `PROPOSED_NOT_TESTED`: B.ONE same-venue back-to-back rematches — weight the previous day's result? Not testable on one event. **R12.** `MONITOR`.

**Rank-1 LOSS — eight-part review:** (1) Nagoya loses by ≤1 or wins, p 0.568. (2) Lost by 7. (3) Centre +2.0, σ 20 → −7 is −0.45σ; ordinary. (4) The 17-Oct 76–90 loss and injuries were known; the Sunday starting five was not (the club announces at 15:30 JST) and was not backfilled. (5) Gate failed at issue (0.568 < 0.62); variance-dominated. (6) Cutoff-only: no defensible flip; honest output was no primary lean. (7) `NEAR_COINFLIP_RANKED / VARIANCE`. (8) Treat gate-failing rows as informational (`PROPOSED_NOT_TESTED`).
<!-- END SETTLEMENT LOCAL-20261018Q7N4T9B2-G0001 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261018Q7N4T9B2-G0002 revision-1 -->
### Settlement · LOCAL-20261018Q7N4T9B2-G0002 · TNT Tropang 5G v Converge FiberXers · 2026-10-21T00:55+11:00
**Revision:** revision-1 · parent NONE · effective 2026-10-21T00:55+11:00 · affected keys ALL four · changes NONE.
**Card state:** `SETTLED` under the card's declared endpoint; `ENDPOINT_SENSITIVE` (operator terms open).
**Final event:** **Converge 114 – TNT 112 after overtime.** Regulation **106–106** (XERS 27-28-19-32, TNT 35-21-30-20); OT 8–6. Full-game total 226; regulation total 212. Full-game TNT margin −2; regulation 0. Final wall-clock `UNKNOWN`. Venue Ynares Center **Antipolo** (Q7-S04; RealGM's "Pasig" label conflicts).
**Definition status:** the card's A2 interpreted all four rows on the **completed game including OT** ("analysis explicitly assumes normal completed-game OT-inclusive endpoint") → sporting grades below use that frozen convention. Regulation-only alternative shown for transparency; operator terms `UNKNOWN_DEFINITION` and here **grade-changing**.
**Evidence:** B (RealGM box + five independent Philippine reports).
**Expected vs final (full game):** total 220.0 (σ 24) → 226: +6.0, z +0.25. TNT margin −1.0 (σ 20) → −2: −1.0, z −0.05.

| Rank | Exact original proposition | Original p_card (decisive) | Original W / P / L | Original BASELINE_P | Grade (incl. OT — card convention) | Regulation-only alternative | Evidence | Counts toward wins |
|---|---|---:|---|---|---|---|---|---|
| 1 | **Combined Total Under 221.5** | 0.524 | 0.524 / 0 / 0.476 | NOT_ESTIMATED | **LOSS** (226) | WIN (212) | B | Yes |
| 2 | **Giga (TNT) +2.0** | 0.520 | 0.510 / 0.020 / 0.470 | NOT_ESTIMATED | **PUSH** (lost by exactly 2) | WIN (tie) | B | Yes — PUSH excluded from rate |
| 3 | Fiberxers (Converge) −2.0 | 0.480 | 0.470 / 0.020 / 0.510 | NOT_ESTIMATED | **PUSH** | LOSS | B | No |
| 4 | Combined Total Over 221.5 | 0.476 | 0.476 / 0 / 0.524 | NOT_ESTIMATED | **WIN** | LOSS | B | No |

**Top-two result:** `ONE_DECISIVE` — R1 LOSS, R2 PUSH; decisive denominator 1; primary wins 0/1; 1 PUSH.
**ML execution and feedback:** `NOT_APPLICABLE_NO_MODEL`.
**Proper scores:** binary Brier R1 0.524² = 0.2746; R4 0.476² = 0.2746. Push rows: binary `NOT_COMPUTED` (p_card scores decisive outcomes only, SCV §1); categorical half-sum Brier on the issued W/P/L vector, y = PUSH: R2 0.5×(0.510² + 0.980² + 0.470²) = 0.5×1.4414 = **0.7207**; R3 identical 0.7207 (scaling labelled; not mixed with binary).
**Shadow results:** none. **Form-window check:** `NOT_APPLICABLE`.
**Winner call:** Converge ≈0.52 → **correct** (full game).
**R1.** Rank 1 Under 221.5 (0.524); Rank 2 TNT +2.0 (0.520), a PRECISION_TIE at issue. **R2.** 114–112 OT; 106–106 regulation; verified two lineages. **R3.** Full game 226 ≥ 222 → Over; TNT −2 = handicap 0 → push. **R4.** 0 W / 1 L / 1 PUSH; Hit@2 miss; NDCG N/A (push in slate). **R5.** Converge correct. **R6.** Total +4.5 over 221.5 (full game), −9.5 under (regulation); margin exactly on the push point. **R7.** Full-game errors small (|z| ≤ 0.25). The decisive mechanism was the OT period, adding 14 points to a regulation total that sat 9.5 under the line. **R8.** The card flagged OT branching and the push mass as unmodelled ("exact OT winner/total scoring distribution missing"); this event realised exactly that branch. **R9.** Scheduled 20:15 AEDT; card's research clock 20:17 AEDT → `POST_START`; target outcome not used. Starters (Q7-S03): TNT Hollis-Jefferson, Heading, Nambatac, Galinato, Oftana — matches the card's prior-game five; Converge Clark, Baltazar, Tungcab, Stockton, Policarpio (card listed Gómez de Liaño/Williams among Oct-16 starters; both came off the bench). **R10.** Process `NOT_ASSESSABLE` for timing; model's OT branch absent (acknowledged); class `OT_TAIL_ENDPOINT`. **R11.** `PROPOSED_NOT_TESTED`: price PBA totals as regulation mixture + P(tie)×E[OT points] rather than one full-game normal. **R12.** `PROPOSE_EXPERIMENT`; operator-definition request queued (Q7-Q2).

**Rank-1 LOSS — eight-part review:** (1) Total ≤221 incl. OT, p 0.524. (2) 226 after OT; 212 in regulation. (3) Centre 220, σ 24 → 226 is +0.25σ; but the loss came entirely through the OT branch, which the single full-game normal did not represent explicitly. (4) OT occurrence is not knowable pre-start; the endpoint convention was knowable and was declared. (5) Endpoint/model-structure issue plus variance; the near-coinflip rank was flagged at issue. (6) Cutoff-only: a regulation+OT mixture would move this row only slightly (~1–2 pp); no flip. (7) `OT_TAIL_ENDPOINT / NEAR_COINFLIP`. (8) Test the explicit OT branch on PBA history (`PROPOSED_NOT_TESTED`).
<!-- END SETTLEMENT LOCAL-20261018Q7N4T9B2-G0002 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261018Q7N4T9B2-G0003 revision-1 -->
### Settlement · LOCAL-20261018Q7N4T9B2-G0003 · CA Osasuna v Real Racing Club de Santander · 2026-10-21T00:55+11:00
**Revision:** revision-1 · parent NONE · effective 2026-10-21T00:55+11:00 · affected keys ALL six directions · changes NONE.
**Card state:** `SETTLED`.
**Final event:** **Osasuna 2–0 Racing**, half-time **1–0** (Budimir penalty 9'), Osambela 88'. Corners **Osasuna 7 + Racing 4 = 11** (ESPN `wonCorners`; SofaScore and La Nación agree). 90 min + stoppage; KO 12:00Z (23:00 AEDT). Final wall-clock `UNKNOWN`.
**Definition status:** card A2 — 1H incl. added time; FT 90'+; corners per ESPN/Opta `wonCorners` (pre-registered RULES_SOCCER §0 route). Operator `UNKNOWN_DEFINITION`.
**Evidence:** goals B (Opta + independent publishers); corners B (two publishers, Opta lineage likely shared).
**Expected vs final:** Osasuna 1.8125 → 2; Racing 1.3125 → 0; FT 3.125 (mixture SD 1.796) → 2: −1.125, z −0.63; 1H 1.575 → 1: −0.575; corners 10.80 (Poisson SD 3.29) → 11: +0.20, z +0.06.

| Rank | Exact original proposition | Original p_card | Original BASELINE_P | Grade | Evidence | Counts toward wins | Basis |
|---|---|---:|---|---|---|---|---|
| 1 | **1H combined goals Over 0.5** | 0.790 | NOT_ESTIMATED | **WIN** | B | Yes | 1 goal by HT |
| 2 | **FT combined goals Over 2.5** | 0.600 | NOT_ESTIMATED | **LOSS** | B | Yes | 2 goals |
| 3 | FT corners Over 10.5 (PROVISIONAL_DIAGNOSTIC at issue) | 0.513 | NOT_ESTIMATED | **WIN** | B | No | 11 |
| 4 | FT corners Under 10.5 (PROVISIONAL_DIAGNOSTIC) | 0.487 | NOT_ESTIMATED | **LOSS** | B | No | 11 |
| 5 | FT goals Under 2.5 | 0.400 | NOT_ESTIMATED | **WIN** | B | No | |
| 6 | 1H goals Under 0.5 | 0.210 | NOT_ESTIMATED | **LOSS** | B | No | |
| — | Winner 3-way (informational): Osasuna 0.492 / D 0.230 / Racing 0.278 | — | — | Osasuna | B | No | |

**Top-two result:** `SPLIT` — R1 W, R2 L; 1/2.
**ML execution and feedback:** `NOT_APPLICABLE_NO_MODEL`.
**Proper scores:** R1 (1−0.790)² = 0.0441; R2 0.600² = 0.3600; R3 (1−0.513)² = 0.2372; R4 0.2372; R5 0.3600; R6 0.0441. Three-way winner half-sum Brier 0.5×(0.508² + 0.230² + 0.278²) = 0.5×0.3883 = **0.1941**. Baselines 0.
**Shadow results:** none. **Form-window check:** `NOT_APPLICABLE` (no R2 blend admitted; card said weights not available).
**Winner call:** Osasuna plurality → **correct**.
**R1.** Rank 1 1H Over 0.5 (0.790); Rank 2 FT Over 2.5 (0.600). **R2.** 2–0 / HT 1–0 / corners 11; verified. **R3.** 1 ≥ 1; 2 ≤ 2; 11 ≥ 11. **R4.** 1/2; Hit@2 hit; NDCG over ranks 1–4: winners at 1 and 3 → 1/1.631 = 0.613. **R5.** Correct. **R6.** 1H +0.5 goals over the 0.5 line; FT 0.5 goals under 2.5; corners 0.5 over 10.5 (one corner from the other side). **R7.** Racing scored 0 against 1.31 expected; xG reported 3.38 v 0.28 (SofaScore news) — Osasuna created far more than the 2 goals scored. **R8.** R2 loss came from Racing's attack producing nothing and Osasuna's finishing below its chances; supported observation. Process check on the R1 win: the same unconfirmed-XI gap applied (card `LINEUP_UNCONFIRMED`). **R9.** Research began before KO (22:49 AEDT), card assembled after 23:00 → `POST_SCHEDULED_START_ISSUE`; no outcome used. **R10.** Process `DEFICIENT` on lineup closure; model uncalibrated; R2 class `VARIANCE / FINISHING`. **R11.** `PROPOSED_NOT_TESTED`: none specific. **R12.** `MONITOR`.
<!-- END SETTLEMENT LOCAL-20261018Q7N4T9B2-G0003 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261018Q7N4T9B2-G0004 revision-1 -->
### Settlement · LOCAL-20261018Q7N4T9B2-G0004 · KIA Tigers @ LG Twins, KBO semi-playoff Game 3 · 2026-10-21T00:55+11:00
**Revision:** revision-1 · parent NONE · effective 2026-10-21T00:55+11:00 · affected keys ALL four · changes NONE.
**Card state:** `SETTLED` as a retained **unissued** research record (`READ_ONLY_DRAFT / NOT_ISSUED`; ordinal G0004 not consumed per the footer).
**Final event:** **KIA 13 – LG 1**, 9 innings (KIA 0-7-0-0-1-1-1-3-0, H16 E0; LG 0-0-0-0-0-1-0-0-0, H8 E1). Start 18:31 KST (20:31 AEDT), end 21:58 KST (23:58 AEDT). KIA won the series 3–0. No draw; the 15-inning tie branch did not arise.
**Definition status:** card A2 — ML conditional on a decisive game (tie → void assumed for p); game was decisive, so the conditional and unconditional grades coincide. Total = full-game runs. Operator `UNKNOWN_DEFINITION`.
**Evidence:** A (KBO owner JSON) + independent report.
**Expected vs final:** total 9.50 (σ 5.0) → 14: +4.5, z +0.90. KIA margin +0.40 (σ 4.8) → +12: +11.6, z **+2.42** (|z| > 2).

| Rank | Exact original proposition | Original p_card | Original BASELINE_P | Grade | Evidence | Counts toward wins (research record) | Basis |
|---|---|---:|---|---|---|---|---|
| 1 | **Combined Total Under 9.5 Runs** | 0.556 | NOT_ESTIMATED | **LOSS** | A | Research-record primary | 14 |
| 2 | **Tigers ML** (decisive-game conditional) | 0.533 | NOT_ESTIMATED | **WIN** | A | Research-record primary | 13–1 |
| 3 | Twins ML | 0.467 | NOT_ESTIMATED | **LOSS** | A | No | |
| 4 | Combined Total Over 9.5 Runs | 0.444 | NOT_ESTIMATED | **WIN** | A | No | |

**Top-two result:** `SPLIT`; 1/2 (unissued record — reported separately from issued cohorts).
**ML execution and feedback:** `NOT_APPLICABLE_NO_MODEL`.
**Proper scores:** R1 0.556² = 0.3091; R2 (1−0.533)² = 0.2181; R3 0.467² = 0.2181; R4 (1−0.444)² = 0.3091.
**Shadow results:** none. **Form-window check:** the card's season/L20 shrink (k=60) gave raw total 9.65 vs scenario 9.50; observed 14. Neither centre near the outcome.
**Winner call:** KIA (conditional 0.533) → **correct**.
**R1.** Rank 1 Under 9.5 (0.556); Rank 2 KIA ML (0.533). **R2.** 13–1, nine innings; verified. **R3.** 14 ≥ 10; KIA won. **R4.** 1/2; Hit@2 hit; NDCG winners at 2 and 4 → 0.631/1.631 = 0.387. **R5.** Correct. **R6.** Total 4.5 runs over the line (+0.9σ); margin 12 runs. **R7.** One-sided blowout: margin z +2.42 — a tail outcome relative to the stated width. **R8.** LG starter Carrasco conceded the 7-run 2nd inning (incl. Kim Do-yeong grand slam, Q7-S08); the card had modelled Carrasco as the better run-preventer. Supported observation. **R9.** Request 20:24 AEDT; first pitch 20:31 AEDT; card assembled after → `POST_START`; unissued. Announced lineups were press-corroborated pregame (one of the few cards with confirmed nines). **R10.** Process `NOT_ASSESSABLE` (unissued); model uncalibrated; class `STARTER_COLLAPSE / TAIL`. **R11.** `PROPOSED_NOT_TESTED`: KBO postseason margin width σ 4.8 may be too narrow (one |z|>2 is not evidence alone). **R12.** `MONITOR`; owner to decide whether G0004 is ever issued/imported.

**Rank-1 LOSS — eight-part review:** (1) Total ≤9, p 0.556. (2) 14. (3) +0.9σ from centre — inside the distribution. (4) Starters and lineups were known pregame and used; the 2nd-inning collapse was not knowable. (5) Variance; gate failed at issue (0.556). (6) Cutoff-only: none — the league mean (10.14) would have nudged toward Over, but the card already reported Under at 0.556 as unqualified. (7) `VARIANCE / STARTER_COLLAPSE`. (8) Compare postseason KBO totals against the regular-season 10.14 mean in prompt 6 (`PROPOSED_NOT_TESTED`).
<!-- END SETTLEMENT LOCAL-20261018Q7N4T9B2-G0004 revision-1 -->

## Shadows and legacy bundles for prompt 6
None (all `ANALYST_PRIMARY_V1`).

## UNRESOLVED_CARRYOVER
| ID | Event key | Queue | Original card | Latest revision | Open field | Responsible actor | Next source + exact field | Due | Final-time basis | Last attempt | Scheduled automation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q7-Q1 | G0002 | UNRESOLVED_EVIDENCE (corroboration) | G0002 | revision-1 | PBA field-owner box; venue label | Prompt-4 agent | pba.ph game page: final, OT, venue | NEXT_OWNER_INVOKED | UNKNOWN | 2026-10-21 (homepage only) | NOT_SCHEDULED |
| Q7-Q2 | G0002 | UNRESOLVED_DEFINITION (grade-changing) | G0002 | revision-1 | Operator OT inclusion for ±2.0 and 221.5 | Owner | Written operator terms | NEXT_OWNER_INVOKED | N/A | not supplied | NOT_SCHEDULED |
| Q7-Q3 | G0004 | CUSTODY | G0004 | revision-1 | Whether G0004 is an issued/imported record | Owner | Owner decision at prompt 4 | NEXT_OWNER_INVOKED | N/A | — | NOT_SCHEDULED |
| Q7-Q4 | all | UNRESOLVED_EVIDENCE | all | revision-1 | Operator terms; G0002/G0003 final times | Owner / prompt 4 | Operator rules; gamebooks | NEXT_OWNER_INVOKED | UNKNOWN | — | NOT_SCHEDULED |
| Q7-Q5 | §C inherited canonical queue | as recorded | external | unchanged | as recorded | as recorded | as recorded | as recorded | as recorded | no new attempt | NOT_SCHEDULED |

## Learning record (LEARN-v2)
| Local key | Final score | Regulation score | Decision | Final time | Terminal source (retrieved) |
|---|---|---|---|---|---|
| G0001 | FE 82 – OKA 89 | same | Okayama | last PBP 2026-10-18T08:49:16Z | B.League 507258 · ≈00:15 AEDT 21 Oct |
| G0002 | TNT 112 – Converge 114 (OT) | 106–106 | Converge (OT) | UNKNOWN | RealGM 544796 (proxy) · ≈00:27 AEDT |
| G0003 | Osasuna 2–0 Racing (HT 1–0); corners 7–4 | same | Osasuna | UNKNOWN | ESPN 401882840 · ≈00:10 AEDT |
| G0004 | KIA 13 – LG 1 | 9 inn | KIA | 2026-10-20T21:58+09:00 | KBO GetScoreBoardScroll · ≈00:35 AEDT |

## SETTLEMENT_MANIFEST
| Item | Value |
|---|---|
| Frozen source | `20261018Q7N4T9B2_UPDATED_G0004_KIA_LG.md`; 4 card blocks (G0004 unissued); bytes/SHA PENDING_PROMPT_4 |
| Revisions | revision-1 × 4, parent NONE |
| Contract rows | 18: **8 W / 8 L / 2 PUSH / 0 VOID / 0 UNRESOLVED** (card convention; under a regulation-only operator reading all four G0002 rows would change: Under W, TNT +2 W, Converge −2 L, Over L) |
| Primary rows (all four records) | 8: **2 W / 5 L / 1 PUSH** — Rank 1: 1 W / 3 L; Rank 2: 1 W / 2 L / 1 PUSH |
| Primary excl. unissued G0004 | 6: 1 W / 4 L / 1 PUSH |
| Card classes | ALL_LOST 1 (G0001), ONE_DECISIVE 1 (G0002), SPLIT 2 (G0003, G0004) |
| Hit@2 | 2/4 (G0003, G0004) |
| Mean binary Brier, decisive primary rows (n=7) | (0.3226+0.2894+0.2746+0.0441+0.3600+0.3091+0.2181)/7 = **0.2597** |
| Evidence mix (primary) | A 4 (G0001, G0004), B 4 |
| Timing | G0001 POST_START (owner PBP 17:40:16 v card ≥17:41:02); G0002 POST; G0003 POST; G0004 POST + unissued |
| Rank-1 LOSS deep reviews | 3/3 (G0001, G0002, G0004) |
| Canonical import / GitHub writes | PENDING / NO |

**MINI_SETTLEMENT review row:** `2026-10-21 | MINI 20261018Q7N4T9B2 | 4 draft records / 18 rows | primary 2W-5L-1P, mean Brier 0.260 (n=7) | DATA_REPAIR_REQUIRED (G0002 operator endpoint; G0004 custody) | no rank changes`.

## Verification S1–S18
S1 PASS (4 card blocks + 2 §C addenda inventoried) · S2 PENDING_PROMPT_4 · S3 PASS (incl. G0002 W/P/L vectors) · S4 PASS (G0002 endpoint alternative shown; grade follows the card's frozen convention) · S5 PASS · S6 PASS (8+8+2 = 18) · S7 PASS · S8 PASS (3 eight-part reviews; R1 win G0003 checked) · S9 PASS · S10 PASS · S11 PASS (incl. categorical push scoring kept separate) · S12 PARTIAL · S13 PASS · S14 PARTIAL · S15 PASS · S16 PASS · S17 PARTIAL · S18 PASS.
