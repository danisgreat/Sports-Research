<!-- SETTLEMENT-FORMAT: mini-settlement-10 -->
# SETTLEMENT AND RETROSPECTIVES — MINI 20261018X7Q4M9R2

**Document:** `20261018X7Q4M9R2_SETTLEMENT.md` · settlement-document revision 1 · prepared 2026-10-21 ≈00:40 AEDT (2026-10-20 ≈13:40Z).
**Mode:** `LOCAL_MINI_SETTLEMENT`. Prompt 3 text supplied by the owner (P-2026.10.17-v22.2). **Environment deviation (ENV-v1):** Prompt 3 is specified for an external chat; the owner invoked it inside the repository session. The prompt's write rules were still applied: no repository commit, no push, no canonical write, no hash claims. This file was saved to the owner's untracked local folder only, for the owner to keep or move.
**Authority:** `PUBLISHED_MAIN_PINNED 3e29a58693e2ed02ff862e9bf0f751af2feadee1` (local HEAD = origin/main at read time; `git fetch` failed on the known `refs/agents/desktop.ini` ref, so the pin is the last fetched origin/main).
**Reading receipt (this session, actually opened):** owner-pasted Prompt 3 (full); `research/prompts/3_SETTLE_LOCAL_MINI.md` lines 1–30 (identical in substance to the paste); `CARD_AND_LOG_TEMPLATES.md` §6 settlement package and §9 S1–S18; `SCORING_AND_VALIDATION.md` §§1–11 (SCV-v11 definitions); `PROBABILITY_TOOLKIT.md` §10 settlement arithmetic and §11. **Not reopened this session:** COMMON_OPERATING_PROTOCOL, TIMING_RESEARCH_PROTOCOL, VERIFICATION_PROTOCOL, RULES_CRICKET / RULES_BASKETBALL, SOURCES, ROSTER_AVAILABILITY_PROTOCOL, RESEARCH_SOURCE_REGISTER. Their requirements are applied only as restated in the pasted Prompt 3 and the templates above.
**Model scope (MLSCOPE-v1):** no model, runtime, shadow or feedback command was run or read. Data retrieval used public keyless JSON feeds and web pages; settlement arithmetic below is by hand.

## Frozen source and inventory

**FROZEN_SOURCE**
- File name: `UPDATED_PREDICTION_MINI_RUNNING_LOG_20261018X7Q4M9R2_G0003.md` (owner-supplied attachment in this conversation; not present on disk in the repository).
- Format: `mini-log-10`.
- Block inventory, in order: header §A–§D (incl. intake rows `INTAKE-…-CREATE`, `…-G0001`, `…-G0002`, `…-G0003`) → `BEGIN/END CARD LOCAL-20261018X7Q4M9R2-G0001` → `BEGIN/END CARD …-G0002` → `BEGIN/END CARD …-G0003` → `BEGIN/END FOOTER`.
- Card count 3; first local key `LOCAL-20261018X7Q4M9R2-G0001`; last `LOCAL-20261018X7Q4M9R2-G0003`. Addenda: none. Prior settlement revisions: none.
- Freeze time: 2026-10-21T00:40+11:00 (this document). Writer hand-over: the mini's documentary lease (`2026-10-18T17:15+11:00` → `2026-10-19T17:15+11:00`) has expired; any new event goes to the next authorised mini → `NONE` named here.
- Raw byte count and SHA-256: `PENDING_PROMPT_4` (ENV-v1 §6; not computed here).
- Source growth check: the attachment ends at `END FOOTER` with next key `G0004`; no block after the footer. `NO_GROWTH_OBSERVED` in the supplied text. Unpublished owner copies: `NOT_VERIFIED`.

**Inventory:** 3 cards / 12 supplied contract rows (4 per card, all ranked) / 0 addenda / 0 revisions / 0 pending events after this settlement / inherited canonical queue in §C (P-584 etc.) is external and **not** settled here (no new evidence gathered for it).

## Local identity and canonical handoff — LOCAL_ID_MAPPING

| Local key | Native event identity | Canonical ID |
|---|---|---|
| `LOCAL-20261018X7Q4M9R2-G0001` | Men's Test, South Africa v Australia, 2nd Test, St George's Park, 18–22 Oct 2026; ESPNcricinfo match 1525660 (series 24203); CA fixture `CA:39991` | `NOT_ASSIGNED / PENDING_PROMPT_4_IMPORT` |
| `LOCAL-20261018X7Q4M9R2-G0002` | LBA Serie A 2026-27 R4, Napoli Basketball v Olimpia Milano, 18 Oct 2026, PalaBarbuto/Alcott Arena; RealGM box 529586 | `NOT_ASSIGNED / PENDING_PROMPT_4_IMPORT` |
| `LOCAL-20261018X7Q4M9R2-G0003` | Women's T20I, India v Zimbabwe 2nd T20I, Raipur, 18 Oct 2026; ESPNcricinfo match 1535653 (series 24371); BCCI 239631 | `NOT_ASSIGNED / PENDING_PROMPT_4_IMPORT` |

Existing canonical references in §C (P-581–P-600, P-584) keep their real mappings; no new P-number is planned here.

## Source discovery, corroboration and reuse register

**Information completion: `INFORMATION_INCOMPLETE`.** Every supplied contract row has a definite sporting grade, but these fields remain open: G0001 final SA first-innings total (innings still live in the last feed; grade is decided by an invariant bound) and Test result; G0002 independent field-owner (LBA) box; all three operator action/void terms; final wall-clock times for G0001/G0002; G0003 match end time.

Shared/prior registers consulted: the cards' own A8 source lists (read in the attachment). `RESEARCH_SOURCE_REGISTER.md` was not reopened. No shared register was written.

| Source ID / scope | URL / route | Fields observed / still missing | Publisher / collector / independence | Retrieval | Reuse limits / next route |
|---|---|---|---|---|---|
| X7-S01 ESPN cricket scorepanel 18 Oct | `https://site.api.espn.com/apis/site/v2/sports/cricket/scorepanel?dates=20261018` | SA 320/7 (102.2 ov) live; ZIM-W 102/8, IND-W 104/1 (8.5) result | ESPN/Cricinfo feed | 2026-10-21 ≈00:05 AEDT | Score panel snapshot; SA row stale (still day 2 state) |
| X7-S02 ESPN cricket summary 1525660 | `…/sports/cricket/24203/summary?event=1525660` | Toss: "Australia won toss & fielded"; notes: 18–22 Oct, 9.45 start local; header still `Live` | ESPN/Cricinfo | ≈00:10 AEDT | Header frozen at 320/7; use S03 |
| X7-S03 ESPN ball-by-ball 1525660, innings 1 | `…/sports/cricket/24203/playbyplay?event=1525660&period=1&page=n` (all pages) | First ball Starc→Markram at **2026-10-18T10:00:43Z (21:00:43 AEDT)**; end of over 5: **10/0** (30 legal balls); end of over 6: 11/0; last delivery in feed 2026-10-20T13:27:12Z with SA **324/7** after 616 legal balls | ESPN/Cricinfo bbb | ≈00:20 AEDT | Feed's last row is mid-innings; final innings total MISSING |
| X7-S04 Cricinfo match report (search-visible) | `https://www.cricinfo.com/series/australia-in-south-africa-2026-27-1525634/south-africa-vs-australia-2nd-test-1525660/match-report` | Day 3 lunch SA 216/6 (Bavuma 76*, Jansen 72*); day 1 rain, Boland 2 wickets in his second over | Cricinfo editorial (same group as S01–S03) | search 2026-10-21 | Same lineage as ESPN feed; not independent |
| X7-S05 ABC day-one live (search-visible) | `https://www.abc.net.au/news/2026-10-18/live-updates-south-africa-vs-australia-second-test-day-one/107277420` | Rain ruined day one; Boland double strike | ABC (independent publisher) | search 2026-10-21 | Headline-level corroboration of delayed start |
| X7-S06 Sky Sports day two (search-visible) | `https://www.skysports.com/cricket/news/13601039/…` | Boland fourth wicket late on rain-hit day 2 | Sky (independent) | search | Corroborates innings progress; no total |
| X7-S07 RealGM scoreboard 18 Oct (via r.jina.ai) | `https://basketball.realgm.com/international/scores/2026-10-18` | Milano 98 @ Napoli 82, Final | RealGM compiler | ≈00:25 AEDT | Direct fetch blocked by Cloudflare; proxy copy |
| X7-S08 RealGM box 529586 (via r.jina.ai) | `https://basketball.realgm.com/international/boxscore/2026-10-18/AX-Armani-Exchange-Milan-at-Napoli-Basket/529586` | Quarters MIL 18-23-25-32 = 98; NAP 25-13-23-21 = 82; no OT column; venue PalaBarbuto; starters (MIL Cole, Mathews, Hall, Peters, Wright; NAP Dowtin, Ramsey, Faggian, Seljaas, Tarczewski) | RealGM | ≈00:27 AEDT | Not field owner; LBA box OPEN |
| X7-S09 napolimagazine / lanotiziaincomune / milanosportiva / Sportando (search-visible) | `https://www.napolimagazine.com/basket/articolo/napoli-basketball-primo-stop-per-gli-azzurri-l-olimpia-milano-vince-82-98-…-18-10-2026` and others | 82–98, Cole & Mathews 21 each, Milano won Q4 32–21 | Independent Italian publishers | search 2026-10-21 | Half-time reported as 42–38 by one source vs 41–38 from RealGM quarters (immaterial to contracts) |
| X7-S10 ESPN cricket summary/bbb 1535653 | `…/sports/cricket/24371/summary?event=1535653`, `…/playbyplay?event=1535653&period=1` | Result: IND-W won by 9 wkts (67 balls rem.); ZIM-W **102/8 in 20.0 ov** (batted first); first ball **2026-10-18T13:30:39Z (00:30:39 AEDT 19 Oct)**; end of over 5: 16/1; end of over 6: **20/1**; innings end 15:10:06Z | ESPN/Cricinfo | ≈00:20 AEDT | — |
| X7-S11 CricketWorld / Pragativadi / TheHawk / Cricinfo report (search-visible) | `https://www.cricketworld.com/india-women-vs-zimbabwe-women-2nd-t20i-india-crush-zimbabwe-by-9-wickets-to-take-series-win/113882.htm` | ZIM-W 102/8, chose to bat; India 9-wkt win | Independent publishers | search | Over-6 checkpoint is single-lineage (S10) |

**SOURCE_SEARCH_ATTEMPTS (actual routes this session)**

| Field | Route attempted | Result |
|---|---|---|
| G0001 innings/toss/checkpoints | ESPN scorepanel → summary → full bbb pagination (one 502 retried) | Toss, first ball, 5.0-over score, SA ≥324/7 found; final innings total not yet available |
| G0001 corroboration | Web search "South Africa Australia second Test Gqeberha October 2026 first innings scorecard" | Cricinfo/ABC/Sky items; Cricinfo full scorecard page is live/partial |
| G0002 result | Web search (Italian) → no current result indexed; RealGM direct (Cloudflare 403-challenge) → r.jina.ai proxy scoreboard + box | Final and quarters found |
| G0002 corroboration | Web search "Napoli Milano 82-98 Olimpia LBA quarta giornata 2026" | 4 independent Italian reports agree on 82–98 |
| G0002 field owner | `https://www.legabasket.it/calendar` | HTTP 404; LBA game page not located → OPEN |
| G0003 result/checkpoints | ESPN scorepanel → summary → bbb | Found |
| G0003 corroboration | Web search "India Women Zimbabwe Women 2nd T20I Raipur 102/8" | CricketWorld, Pragativadi, TheHawk agree |

**REQUIREMENT_CLOSURE**

| Event / field | Status | Primary / corroboration | Next route · actor · due · automation |
|---|---|---|---|
| G0001 SA 5.0-over score | CLOSED (single lineage, ball-level) | X7-S03 | Cricinfo full scorecard over-by-over · prompt-4 agent · next intake · NOT_SCHEDULED |
| G0001 SA 1st-innings total vs 282.5 | CLOSED_BY_INVARIANT_BOUND (≥324) | X7-S03, S04 (216/6 at lunch day 3, still batting) | Final total from Cricinfo scorecard · owner/prompt-4 · after Test ends 22 Oct · NOT_SCHEDULED |
| G0001 match result (winner call) | OPEN — PENDING_EVENT (Test in progress) | — | Cricinfo/CA result · owner · after 22 Oct 2026 · NOT_SCHEDULED |
| G0002 final / OT status | CLOSED | X7-S08 + X7-S09 | LBA official box (field owner) still OPEN · prompt-4 · NOT_SCHEDULED |
| G0003 Zim innings total; 6.0-over score | CLOSED (total two lineages; 6-over single lineage) | X7-S10 + X7-S11 | BCCI scorecard over summary · prompt-4 · NOT_SCHEDULED |
| All: operator action/void terms | OPEN — UNKNOWN_DEFINITION | not supplied | Owner supplies written terms · owner · before any operator settlement · NOT_SCHEDULED |
| G0001, G0002 final wall-clock time | OPEN (UNKNOWN) | — | Field-owner gamebooks · prompt-4 · NOT_SCHEDULED |

<!-- BEGIN SETTLEMENT LOCAL-20261018X7Q4M9R2-G0001 revision-1 -->
### Settlement · LOCAL-20261018X7Q4M9R2-G0001 · South Africa v Australia, 2nd Test · 2026-10-21T00:40+11:00
**Revision:** revision-1 · parent NONE · effective 2026-10-21T00:40+11:00 · affected contract keys ALL (`SA-I1-U2825`, `SA-I1-O2825`, `SA-F5-U135`, `SA-F5-O135`) · changes NONE (first settlement).
**Card state:** `SETTLED` (all four contract rows decisive); match winner call `PENDING_EVENT`.
**Original card:** frozen mini block `CARD LOCAL-20261018X7Q4M9R2-G0001`.
**Final event / verified final time:** Australia won the toss and fielded; South Africa batted first (X7-S02). First ball 2026-10-18T10:00:43Z = 21:00:43 AEDT, two hours after the scheduled 19:00 AEDT (rain). SA after 5.0 overs (30 legal balls): **10/0**. SA first innings: **at least 324/7** after 102.4 overs at the last feed row (2026-10-20T13:27:12Z), innings not yet ended. Final innings total and match result: `UNKNOWN` (Test scheduled to 22 Oct).
**Definition status:** sporting convention, frozen in the card's A2 (first Test innings until all out/declaration; 30 legal balls). Operator action `UNKNOWN_DEFINITION`. Both endpoints were reached (5.0 overs completed; innings total already above the line), so no void branch was triggered under the card's convention.
**Evidence grade:** 5-over field B (ball-by-ball feed, single lineage); innings field E (invariant bound: every feasible final ≥324 > 282.5).
**Expected vs final:** innings centre 272.0 (σ ≈ 115 base) → observed ≥324: error ≥ +52.0, z ≥ +0.45 (lower bound). 5-over centre 12.75 (σ 8 base) → 10: error −2.75, z ≈ −0.34.

| Rank | Exact original proposition | Original p_card | Original BASELINE_P | Grade | Evidence | Counts toward wins | Basis / definition / time |
|---|---|---:|---|---|---|---|---|
| 1 | South Africa 1st innings **Under 282.5** runs | 0.537 | `NO_LEAGUE_PROFILE` | **LOSS** | E | Yes (primary) | SA ≥324 > 282.5; bound invariant |
| 2 | South Africa after first **5.0 overs Under 13.5** runs | 0.524 | `PROFILE_LACKS_ENDPOINT` | **WIN** | B | Yes (primary) | 10 ≤ 13 |
| 3 | South Africa after 5.0 overs **Over 13.5** | 0.476 | `PROFILE_LACKS_ENDPOINT` | **LOSS** | B | No (informational) | complement |
| 4 | South Africa 1st innings **Over 282.5** | 0.463 | `NO_LEAGUE_PROFILE` | **WIN** | E | No (informational) | complement |

**Top-two result:** `SPLIT` — R1 LOSS, R2 WIN; decisive denominator 2; primary wins 1/2.
**ML execution and feedback:** `NOT_APPLICABLE_NO_MODEL` (MLSCOPE-v1 ANALYST_PRIMARY_V1 card; no bundle).
**Proper scores (binary Brier, by hand; evidence class shown):** R1 (0.537−0)² = 0.2884 [E]; R2 (0.524−1)² = 0.2266 [B]; R3 (0.476−0)² = 0.2266 [B]; R4 (0.463−1)² = 0.2884 [E]. Paired BASELINE_P rows: 0/4 → d_Brier `NOT_COMPUTABLE`. Log loss R1 −ln(0.463)=0.770; R2 −ln(0.524)=0.646.
**Shadow results:** `SHADOW_BASE_ONLY` p_base rows are diagnostic only and are deferred to prompt 6 (no model shadows exist). No RET03/RET04/XCARD6 frozen rows.
**Form-window check:** the card's centre was a manual blend (SA filtered 290.5 / AUS conceded 258.0 → 270 base); observed ≥324 exceeds both the unadjusted midpoint 274.25 and the adjusted 272. `NOT_APPLICABLE` as a formal FC11 pair.
**Winner call:** Australia (qualitative only, no probability issued) → `PENDING_EVENT` until the Test ends.

**R1. Original prediction:** Rank 1 SA 1st-innings Under 282.5 at 0.537; Rank 2 SA 5-over Under 13.5 at 0.524. Both flagged `RANK1_UNSTABLE` / `BELOW_FLOOR` at issue.
**R2. Final event:** 5-over 10/0 verified; innings ≥324/7 and ongoing; result pending.
**R3. Contract settlement:** 282.5 line: 324 − 282.5 = +41.5 runs past the line at the bound → Over wins. 13.5 line: 10 ≤ 13 → Under wins.
**R4. Rank diagnostics:** primary 1 W / 1 L; Hit@2 eligible (fully decisive) = hit. NDCG@2 (descriptive): winners at ranks 2 and 4 → DCG = 0 + 1/log2(3) = 0.631; IDCG (two winners) = 1.631 → 0.387.
**R5. Winner call:** qualitative Australia; pending.
**R6. Line assessment:** innings: observed ≥ +41.5 runs above 282.5 (≥ +0.36σ of the base width from the line); 5-over: 3.5 runs under 13.5.
**R7. Expected versus realised:** innings ≥ +52 above the 272 centre with a wide 105–125 σ scenario set; 5-over −2.75 runs. The lower-order partnership (Bavuma–Jansen, X7-S04) carried the innings from 97/5 to 216/6+.
**R8. Missed mechanism:** the card's LOW/BASE scenarios weighted early seam damage and collapse; the collapse happened (97/5) but the lower-middle order then recovered far past the line. The mixture did not condition the total on "survives a collapse"; supported observation, cause not quantified.
**R9. Source/timing review:** actual first ball was 21:00:43 AEDT. The card states research continued past the scheduled 19:00 with an intended issue after 19:07:57; its actual delivery time is not recorded, so whether it preceded the real first ball is `NOT_VERIFIED`. No freeze receipt exists → not a verified pre-start issue. The card's own lineup gaps (official XIs unconfirmed) stand.
**R10. Classification:** process `NOT_ASSESSABLE` (single event; lineups unverified at issue); model uncalibrated; failure class `TAIL_UNDERWEIGHTED / LOWER-ORDER RECOVERY` for R1.
**R11. Hypothesis:** `PROPOSED_NOT_TESTED` — a Test first-innings total model conditioned on wickets at a phase checkpoint (e.g. P(total > L | 5 down for <100)) would widen the upper tail after early collapses; test on future Test cards.
**R12. Disposition:** `MONITOR`; queue final innings total and Test result as learning-record completions.

**Rank-1 LOSS — eight-part review**
1. *Exact claim:* SA 1st-innings total ≤282, p = 0.537 (uncalibrated three-scenario truncated normal; RANK1_UNSTABLE at issue).
2. *Verified outcome:* SA ≥324/7 and still batting (X7-S03), so the claim failed by at least 42 runs.
3. *Original-distribution check:* the card's own mixture gave Over 282.5 = 0.463; a ≥324 finish sits about +0.45σ above the base centre — well inside the issued distribution, not a tail event.
4. *Cutoff knowability:* the toss (AUS bowl first) and damp conditions were known pre-start and used. The 21:00 AEDT delayed start was knowable at issue only as "drizzle/delay"; it does not bear on the total.
5. *Process/model/variance:* a near-coin-flip probability (0.537) was ranked first; the card itself flagged it below the 0.62 gate. One loss on a 0.537 row is not evidence of miscalibration.
6. *Cutoff-only counterfactual:* with only pre-start evidence, the defensible alternative was to issue no ranked lean on the innings total (gate failure), not to flip to Over.
7. *Failure class:* `NEAR_COINFLIP_RANKED / VARIANCE`.
8. *Testable correction:* enforce the existing gate — when Rank 1 fails 0.62, record the row as INFORMATIONAL rather than a primary rank (process proposal for prompt 6/8 review, `PROPOSED_NOT_TESTED`).
<!-- END SETTLEMENT LOCAL-20261018X7Q4M9R2-G0001 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261018X7Q4M9R2-G0002 revision-1 -->
### Settlement · LOCAL-20261018X7Q4M9R2-G0002 · Napoli Basketball v Olimpia Milano · 2026-10-21T00:40+11:00
**Revision:** revision-1 · parent NONE · effective 2026-10-21T00:40+11:00 · affected contract keys ALL (`LBA:20261018:NAP:MARGIN:-1.5:FINAL`, `…MIL:MARGIN:+1.5…`, `…COMBINED:OVER:174.5…`, `…COMBINED:UNDER:174.5…`) · changes NONE.
**Card state:** `SETTLED`.
**Final event:** Napoli 82 – **Olimpia Milano 98**, regulation (quarters NAP 25-13-23-21, MIL 18-23-25-32; no OT column). Total 180; Napoli margin −16. Final wall-clock `UNKNOWN`.
**Definition status:** full game incl. OT (card A2); no OT occurred, so the convention question is moot. Operator `UNKNOWN_DEFINITION`.
**Evidence grade:** B (RealGM box + four independent Italian reports; LBA field-owner box not yet opened).
**Expected vs final:** total 172.25 (σ 21) → 180: error +7.75, z = +0.37. Napoli margin +2.10 (σ 16) → −16: error −18.10, z = −1.13.

| Rank | Exact original proposition | Original p_card | Original BASELINE_P | Grade | Evidence | Counts toward wins | Basis |
|---|---|---:|---:|---|---|---|---|
| 1 | Combined total **Under 174.5** (incl. OT) | 0.542 | 0.557 | **LOSS** | B | Yes | 180 ≥ 175 |
| 2 | **Napoli −1.5** (incl. OT) | 0.515 | 0.521 | **LOSS** | B | Yes | lost by 16 |
| 3 | **Milano +1.5** | 0.485 | 0.479 | **WIN** | B | No | won outright |
| 4 | Combined total **Over 174.5** | 0.458 | 0.443 | **WIN** | B | No | 180 |

**Top-two result:** `ALL_LOST` — decisive denominator 2; primary wins 0/2.
**ML execution and feedback:** `NOT_APPLICABLE_NO_MODEL`.
**Proper scores:** binary Brier card / baseline / d_Brier — R1 0.2938 / 0.3102 (0.557²) / −0.0164; R2 0.2652 / 0.2714 (0.521²) / −0.0062; R3 0.2652 / 0.2714 / −0.0062; R4 0.2938 / 0.3102 / −0.0164. The card's baseline was the 24-game LBA league-only normal approximation; on these four rows the card scored marginally better than baseline (negative d), on one event — descriptive only.
**Shadow results:** none frozen; `SHADOW_BASE_ONLY` deferred to prompt 6.
**Form-window check:** unadjusted (raw shrink) margin +4.12 vs adjusted +2.10 (the card's subjective −2.0 Milano-quality prior); observed −16. The adjustment moved in the correct direction but was far too small; total unaffected.
**Winner call:** Napoli ≈0.551 → **incorrect** (Milano won).

**R1. Original prediction:** Rank 1 Under 174.5 at 0.542; Rank 2 Napoli −1.5 at 0.515 (both below gate/floor at issue).
**R2. Final event:** 82–98, regulation, verified on two lineages.
**R3. Contract settlement:** 180 − 174.5 = +5.5 over the line; Napoli −16 versus required +2.
**R4. Rank diagnostics:** 0/2 primary; Hit@2 miss; NDCG@2 0 (winners at ranks 3–4).
**R5. Winner call:** wrong.
**R6. Line assessment:** total +5.5 points above 174.5 (z vs line from centre: +0.26σ); margin 17.5 points beyond the Napoli −1.5 threshold.
**R7. Expected versus realised:** margin error −18.1 (z −1.13) dominates; total moderately above centre.
**R8. Missed mechanism:** Milano won the 4th quarter 32–21 and Mathews/Cole scored 21 each (X7-S09); the card's three-way Milano-foreign-exclusion uncertainty resolved with Mathews, Cole, Hall, Peters, Wright starting (X7-S08). The card had no confirmed Milano five; supported observation, not a measured effect size.
**R9. Source/timing review:** research completed after the scheduled 21:00 AEDT tip; actual tip `NOT_VERIFIED`; lineups unconfirmed at issue (card's own `LINEUP_UNCONFIRMED`). Not a pre-start issue.
**R10. Classification:** process `DEFICIENT` on lineup closure (C20 open at issue, by the card's own audit); model uncalibrated; class `SIDE_CENTRE_MISS / SMALL_SAMPLE_STRENGTH (n=3 LBA games)`.
**R11. Hypothesis:** `PROPOSED_NOT_TESTED` — early-season (n≤3) team rates against a EuroLeague side should shrink harder toward prior-season/roster strength than k=w 0.40.
**R12. Disposition:** `PROPOSE_EXPERIMENT` (shrinkage strength for n≤3 early-season LBA); LBA field-owner box remains an open corroboration task.

**Rank-1 LOSS — eight-part review**
1. *Claim:* combined points ≤174 incl. OT, p 0.542.
2. *Outcome:* 180 in regulation.
3. *Distribution check:* centre 172.25, σ 21 → 180 is +0.37σ; ordinary.
4. *Knowability:* the active XIIs and Milano's three domestic foreign exclusions were unknown at issue and were not backfilled here.
5. *Process/model/variance:* a 0.542 row ranked first with a 0.027 gap to Rank 2 — flagged RANK1_UNSTABLE at issue; variance-dominated.
6. *Cutoff-only counterfactual:* no defensible cutoff-only flip; the honest alternative was no primary lean.
7. *Failure class:* `NEAR_COINFLIP_RANKED / VARIANCE`.
8. *Correction:* same as G0001 — gate-failing rows recorded as informational (`PROPOSED_NOT_TESTED`).
<!-- END SETTLEMENT LOCAL-20261018X7Q4M9R2-G0002 revision-1 -->

<!-- BEGIN SETTLEMENT LOCAL-20261018X7Q4M9R2-G0003 revision-1 -->
### Settlement · LOCAL-20261018X7Q4M9R2-G0003 · India Women v Zimbabwe Women, 2nd T20I · 2026-10-21T00:40+11:00
**Revision:** revision-1 · parent NONE · effective 2026-10-21T00:40+11:00 · affected contract keys ALL (`ZIMW-TOTAL-U-1105`, `ZIMW-TOTAL-O-1105`, `ZIMW-PP-U-335`, `ZIMW-PP-O-335`) · changes NONE.
**Card state:** `SETTLED`.
**Final event:** Zimbabwe Women chose to bat first: **102/8 in 20.0 overs** (innings ended 2026-10-18T15:10:06Z). After 6.0 overs: **20/1** (after 5.0: 16/1). India Women 104/1 in 8.5 overs; India won by 9 wickets. First ball 2026-10-18T13:30:39Z = 00:30:39 AEDT 19 Oct.
**Definition status:** card's full-innings / 6.0-completed-overs convention; both endpoints reached (20 overs batted, 6 overs completed, no rain). The card's open questions (chase-truncation, early all-out) did not arise because Zimbabwe batted first and batted out the 20 overs. Operator `UNKNOWN_DEFINITION`.
**Evidence grade:** total B (two lineages); 6-over A/B single lineage ball-level (X7-S10).
**Expected vs final:** innings 107.0 (mixture SD 29.94) → 102: error −5.0, z −0.17. 6-over 34.75 (SD 13.96) → 20: error −14.75, z −1.06.

| Rank | Exact original proposition | Original p_card | Original BASELINE_P | Grade | Evidence | Counts toward wins | Basis |
|---|---|---:|---|---|---|---|---|
| 1 | Zimbabwe innings **Under 110.5** | 0.560 | `BASELINE_UNAVAILABLE` | **WIN** | B | Yes | 102 ≤ 110 |
| 2 | Zimbabwe after 6 overs **Over 33.5** | 0.527 | `BASELINE_UNAVAILABLE` | **LOSS** | B | Yes | 20 ≤ 33 |
| 3 | Zimbabwe after 6 overs **Under 33.5** | 0.473 | `BASELINE_UNAVAILABLE` | **WIN** | B | No | complement |
| 4 | Zimbabwe innings **Over 110.5** | 0.440 | `BASELINE_UNAVAILABLE` | **LOSS** | B | No | complement |

**Top-two result:** `SPLIT` — R1 W, R2 L; primary 1/2.
**ML execution and feedback:** `NOT_APPLICABLE_NO_MODEL`.
**Proper scores:** R1 (0.560−1)² = 0.1936; R2 (0.527)² = 0.2777; R3 0.2777; R4 0.1936. Baseline pairs 0/4.
**Shadow results:** none.
**Form-window check:** unadjusted powerplay anchor (selected five checkpoints, mean 36.2) gave Over 33.5 ≈0.577; the adjusted mixture gave 0.527; observed 20. The India-strength adjustment moved toward the outcome but the checkpoint centre was ~15 runs high either way.
**Winner call:** India Women (qualitative) → **correct**.

**R1. Original prediction:** Rank 1 Under 110.5 at 0.560; Rank 2 Over 33.5 at 0.527.
**R2. Final event:** 102/8 (20 ov), 20/1 at 6.0; verified.
**R3. Contract settlement:** 110.5 − 102 = 8.5 runs under; 33.5 − 20 = 13.5 runs under.
**R4. Rank diagnostics:** 1/2 primary; Hit@2 hit; NDCG@2 (descriptive): winners at ranks 1 and 3 → DCG = 1; IDCG (two winners) = 1.631 → 0.613.
**R5. Winner call:** correct.
**R6. Line assessment:** innings −8.5 runs (−0.28σ); powerplay −13.5 runs (−0.97σ).
**R7. Expected versus realised:** powerplay centre 34.75 vs 20 is the material miss; innings close to centre.
**R8. Missed mechanism:** the card's 6-over centre was anchored on five selected checkpoints (27–41) against weaker or different attacks; India's new-ball attack held Zimbabwe to 20/1. Supported observation; sample was explicitly n=5 and selected.
**R9. Source/timing review:** request 00:26 AEDT, first ball 00:30:39 AEDT, card completed after → `POST_START_ISSUE`. Second-match XIs and toss were unverified at issue.
**R10. Classification:** process `DEFICIENT` (phase-history n=5 selected, acknowledged in card); model uncalibrated; R2 class `PHASE_CENTRE_HIGH / SELECTED_SAMPLE`.
**R11. Hypothesis:** `PROPOSED_NOT_TESTED` — opponent-adjusted powerplay rates (Zimbabwe vs full-member new-ball attacks only) would centre lower.
**R12. Disposition:** `MONITOR`; no Rank-1 loss.
<!-- END SETTLEMENT LOCAL-20261018X7Q4M9R2-G0003 revision-1 -->

## Shadows and legacy bundles for prompt 6
None. All three cards are `ANALYST_PRIMARY_V1`; no model shadows or bundles exist.

## UNRESOLVED_CARRYOVER

| ID | Event key | Queue | Original card | Latest revision | Open field | Responsible actor | Next source + exact field | Due (ISO, tz) | Final-time basis | Last attempt | Scheduled automation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X7-Q1 | `LOCAL-20261018X7Q4M9R2-G0001` | PENDING_EVENT (winner call only) | G0001 | revision-1 | Test result; final SA 1st-innings total (learning record) | Owner / prompt-4 agent | Cricinfo match 1525660 full scorecard: SA 1st-innings total, result | 2026-10-23T09:00+11:00 (day after scheduled day 5) | UNKNOWN (match in progress) | 2026-10-21 ≈00:20 AEDT ESPN bbb | NOT_SCHEDULED |
| X7-Q2 | `LOCAL-20261018X7Q4M9R2-G0002` | UNRESOLVED_EVIDENCE (corroboration only) | G0002 | revision-1 | LBA field-owner box and final time | Prompt-4 agent | legabasket.it game page for R4 Napoli–Milano: final, quarters, end time | NEXT_OWNER_INVOKED | UNKNOWN | 2026-10-21 (404 on /calendar) | NOT_SCHEDULED |
| X7-Q3 | all three | UNRESOLVED_EVIDENCE | all | revision-1 | Operator action/void terms | Owner | Written operator rules | NEXT_OWNER_INVOKED | N/A | not supplied | NOT_SCHEDULED |
| X7-Q4 | §C inherited canonical items (P-584, P-581–P-583, P-590–P-600 tasks) | as recorded in the mini §C | external canonical | unchanged | as recorded | as recorded | as recorded | as recorded | as recorded | **no new attempt in this settlement** | NOT_SCHEDULED |

## Learning record (LEARN-v2)

| Local key | Final score | Regulation score | Decision | Final time | Terminal source (URL, retrieved) |
|---|---|---|---|---|---|
| G0001 | Test in progress; SA 1st inns ≥324/7; SA 10/0 at 5.0 ov | n/a | pending | UNKNOWN | ESPN bbb 1525660 · 2026-10-21 ≈00:20 AEDT |
| G0002 | Napoli 82 – Milano 98 | same | Milano win | UNKNOWN | RealGM box 529586 (proxy) · ≈00:27 AEDT |
| G0003 | ZIM-W 102/8 (20) – IND-W 104/1 (8.5) | same | India by 9 wkts | Zim innings end 2026-10-18T15:10:06Z | ESPN summary/bbb 1535653 · ≈00:20 AEDT |

Accounting: settled unique events 2 (G0002, G0003) + 1 with all contracts settled but event pending (G0001); learning records incomplete: G0001 (final total, result), G0002 (field-owner box).

## SETTLEMENT_MANIFEST

| Item | Value |
|---|---|
| Frozen source | `UPDATED_PREDICTION_MINI_RUNNING_LOG_20261018X7Q4M9R2_G0003.md`; 3 cards G0001–G0003; bytes/SHA-256 PENDING_PROMPT_4 |
| Revisions in this document | revision-1 × 3 (one per card), parent NONE |
| Contract rows | 12: **6 W / 6 L / 0 PUSH / 0 VOID / 0 UNRESOLVED** |
| Primary (ranks 1–2) | 6 rows: **2 W / 4 L** — Rank 1: 1 W / 2 L (G0003 W; G0001, G0002 L); Rank 2: 1 W / 2 L (G0001 W; G0002, G0003 L) |
| Card classes | SPLIT 2 (G0001, G0003), ALL_LOST 1 (G0002) |
| Hit@2 | 2/3 eligible cards |
| Mean Brier, primary rows | (0.2884+0.2266+0.2938+0.2652+0.1936+0.2777)/6 = **0.2576** |
| Mean Brier, all 12 rows | 0.2576 (complement rows repeat the same values) |
| Baseline pairs | 4 rows (G0002 only); mean d_Brier −0.0113 (descriptive, one event) |
| Evidence mix (primary) | B 5, E 1 |
| Timing cohort | G0001 issue-phase UNVERIFIED (actual first ball 21:00:43 AEDT); G0002 POST/UNVERIFIED; G0003 POST_START |
| Rank-1 LOSS deep reviews | 2/2 (G0001, G0002) |
| Canonical import | PENDING |
| GitHub writes | NO |

**MINI_SETTLEMENT review row (for prompt 6 → `research/learning_status/REVIEW_LOG.csv`):** `2026-10-21 | MINI 20261018X7Q4M9R2 | 3 cards / 12 rows | primary 2W-4L, mean Brier 0.258 (n=6, all <0.62 p) | disposition INSUFFICIENT_EVIDENCE | data: G0001 final total + LBA owner box open | no rank changes`.

## Verification S1–S18

| Check | Result |
|---|---|
| S1 | PASS — 3 card blocks + header/footer inventoried once; keys preserved |
| S2 | PENDING_PROMPT_4 — no byte comparison possible here; original text not reproduced or edited |
| S3 | PASS — ranks, propositions, p_card, BASELINE_P copied from the cards |
| S4 | PASS — arithmetic shown per row; bound grade only where invariant |
| S5 | PASS with gaps — source/time per row; operator terms separate (UNKNOWN) |
| S6 | PASS — 12 rows reconcile: 6 W + 6 L |
| S7 | PASS — R1–R12 for all 3 cards (G0001 winner R5 pending) |
| S8 | PASS — 2 Rank-1 losses with eight parts; the Rank-1 win (G0003) checked in R8–R10 |
| S9 | PASS — no shadows; baseline coverage 4/12 |
| S10 | PASS — queue rows with actor/route/due/automation |
| S11 | PASS — errors/z and Brier recomputed by hand |
| S12 | PARTIAL — this document written to an untracked local folder and re-read; no repo write |
| S13 | PASS — one revision-1 per key, parent NONE |
| S14 | PARTIAL — FROZEN_SOURCE inventory recorded; raw bytes/SHA PENDING_PROMPT_4 |
| S15 | PASS — queue complete; final times UNKNOWN where not verified |
| S16 | PASS — every retained event settled; learning records listed |
| S17 | PARTIAL — register and three tables present as Markdown; CSV files to be produced by prompt 4; INFORMATION_INCOMPLETE |
| S18 | PASS — all three NOT_ASSIGNED / PENDING_PROMPT_4_IMPORT |
