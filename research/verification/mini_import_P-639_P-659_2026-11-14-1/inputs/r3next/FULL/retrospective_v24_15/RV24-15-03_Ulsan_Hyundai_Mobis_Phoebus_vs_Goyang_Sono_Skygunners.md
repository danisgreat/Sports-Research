# RV24-15-03 — v24.15 retrospective forecast reconstruction

**Record classification:** `RETROSPECTIVE_V24_15_RECONSTRUCTION / READ_ONLY_DRAFT / NOT_ISSUED / UNSETTLED`  
**Research provenance:** `RESEARCH-DRAFT-03` from this chat, originally prepared under v24.12 controls.  
**Conversion timestamp (actual, not a game-time issue):** `2026-11-11T08:43:39+00:00` UTC  
**Format/control target:** `MDS-2026.11.11-v24.15 / EXT-v3 / REQ-v5 / FREEZE-v1 / SEL-v4`  
**Read-only GitHub source:** `danisgreat/Sports-Research`, `main` `4d8bd1771d20974bcbfc7c694a009cd44e95a693`.  
**Original report SHA-256:** `2891f73b53c43569c19a81a0bf31ced26581e08913735781041948d30c94edfb`  
**Official mini key / EV2 key / canonical P-ID:** `NOT_ASSIGNED / NOT_CREATED / NOT_ASSIGNED`.  
**Official `p_card`, source-hashed primary receipt, committed manifest, L5 price, SINGLE/FIVE freeze:** `NOT_ESTIMATED / NOT_PERFORMED`.  
**Settlement status:** `DEFERRED_BY_OWNER`; result, score, grade, fact-scorecard and post-final analysis are intentionally **not** consulted or computed.  
**Evaluation cohort:** `EXCLUDED_RETROSPECTIVE` (not prospective, not FULL_FIVE, not SINGLE paired).  

## 1. v24.15 compatibility wrapper

| Property | Reconstructed original / truthful status |
|---|---|
| Event | Ulsan Hyundai Mobis Phoebus vs Goyang Sono Skygunners |
| Competition | KBL |
| Sport | Basketball |
| Original scheduled event time (AEDT) | 2026-11-10T21:00:00+11:00 |
| Venue | Ulsan Dongchun Gymnasium, South Korea |
| Authoritative event key (EV2) | `NOT_CREATED` — no immutable repository manifest or verified native identity digest |
| Original exact request scope | The `SUPPLIED` rows below; derived winner/complement rows are separated |
| Rank scope | `SUPPLIED_ONLY` (new default; older request did not specify this) |
| Original conditional recommendation | Mobis +3.0 points (conditional) |
| Original formal pick decision | `NO_STRONG_PICK / ABSTAIN` |
| Prospective issue / time validation | `NOT_VERIFIED` — reconstruction is performed after event's scheduled start |
| v24.15 source access and independent collector review | `NOT_ADMITTED` — original retrieval records are not sufficient for SRC-ALT-v3 current snapshots |
| Required L1–L5 (or reduced) returns | `NOT_AVAILABLE` — no package, manifest hashes or independently frozen packets |
| Actual v24.15 kit execution, complete W/P/L masses | `NOT_RUN / NOT_COMPUTED` |
| Official mini/custody changes | `NONE` — issuing-writer lease belongs to repository agent |
| Outcome exposure | `NOT_REVIEWED_FOR_CONVERSION` — no results fetched, not a proof of clean original exposure |
| Missing decisive inputs | Actual tip not proven; complete rotations, import replacement effects, score covariance and overtime missing; ±3 spread has push state. |

## 2. Exact original supplied contracts and legacy diagnostics

Values in the **legacy diagnostic** column are transcriptions of the earlier report, **not new model output**, and are never `ANALYST_PRIMARY_V1`, `reference_p`, `model_p` or formal `p_card`. The v24.15 primary row is explicitly **UNPRICED (`NOT_VALIDATED`)** where numeric qualification, manifests or source receipts are absent; no values have been silently filled in.

| Contract | Family | Origin | Legacy diagnostic / reference | v24.15 disposition | Definition and caveat |
|---|---|---|---|---|---|
| Mobis Phoebus +3.0 | HANDICAP | SUPPLIED | 53.0% conditional on decisive (~2.9% push) | `UNPRICED:NOT_VALIDATED` | Push if Goyang wins by exactly 3 |
| Goyang Skygunners -3.0 | HANDICAP | SUPPLIED | 47.0% conditional on decisive (~2.9% push) | `UNPRICED:NOT_VALIDATED` | Push if Goyang wins by exactly 3 |
| Over 175.5 points | TOTAL | SUPPLIED | 51.7% | `UNPRICED:NOT_VALIDATED` | Final including overtime >=176 |
| Under 175.5 points | TOTAL | SUPPLIED | 48.3% | `UNPRICED:NOT_VALIDATED` | Final including overtime <=175 |
| Mobis Phoebus ML | WINNER | DERIVED_INFORMATIONAL | 45.7% | `UNPRICED:NOT_VALIDATED` | Informational winner comparison |
| Goyang Skygunners ML | WINNER | DERIVED_INFORMATIONAL | 54.3% | `UNPRICED:NOT_VALIDATED` | Informational winner comparison |

## 3. Retrospective scope and research-transfer boundaries

- This is an **archival format conversion**, not a reforecast. No post-event performance has been consulted, no original number adjusted, no outcome assigned and no event graded.
- The original report remains the underlying A1–A9 evidence. Where its retrieved source timestamps, medical status, precise competition scope or lineups cannot be proved pre-event, the corresponding v24.15 requirement remains `UNAVAILABLE` or `NOT_VERIFIED` rather than marked complete.
- `SINGLE_RESEARCH`, `FULL_FIVE`, `REDUCED`, `FULL_SIX`, model/kit receipt and immutable packet hashes cannot be fabricated after the fact; they remain absent. Do **not** submit this as an L5 `LANE_RETURN` or a valid `PICKS_V2` block.
- The original conditional selection is retained as a **historical research opinion**, not a new primary ranked recommendation. The formal disposition remains `NO_STRONG_PICK / ABSTAIN`.
- The user's instruction was **not to settle**: no result lookup, match score, winner, WIN/LOSS/PUSH/VOID, settlement receipt or benchmark is included.
- No repository writer lease was transferred. All official local/card/canonical counters stay unchanged.

## 4. Original A1–A9 research (verbatim preservation)

Original file: `Mobis_Phoebus_Goyang_Skygunners_KBL_2026_Read_Only_Research_Draft.md`; SHA-256 `2891f73b53c43569c19a81a0bf31ced26581e08913735781041948d30c94edfb`. This section is copied byte-to-text from the previously created report without factual edits. Statements within retain their original dates and their original v24.12 methodological labels; the wrapper does not certify them under v24.15.

---

# KBL research-only draft — Ulsan Hyundai Mobis Phoebus v Goyang Sono Skygunners

**Research disposition:** `READ_ONLY_DRAFT / NOT_ISSUED / INFORMATION_INCOMPLETE`  
**Sport:** Basketball — South Korean KBL regular season, 2026–27  
**Estimated fixture:** 10 November 2026, 19:00 KST (21:00 AEDT / 10:00 UTC); Ulsan Dongchun Gymnasium, Ulsan, South Korea  
**Source timing:** Pre-game statistics and reports only; the research session began after the scheduled start, and actual first play was not independently verified. The source snapshots must not be presented as a verified pre-game-issued forecast.  
**User contracts:** Mobis +3.0 points; Goyang Sono −3.0 points; full-game Over/Under 175.5 points, all including overtime under BK-OT-1. Three-point handicap has a PUSH if Goyang wins by precisely three.  
**Repository authority:** `danisgreat/Sports-Research`, public `main` HEAD `f79559b45183ca63a2ce5fc2611321975bae744f`, read only. MDS-2026.11.10-v24.12; CR-2026.11.10-R2; prompt suite P-2026.11.10-v24.10; SEL-2026.10.22-v4; SCV-2026.10.22-v12. Active repo mini `research/active_minis/20261109R3NEXT.md`; no ID allocated, no lease acquired, no append or change to repository.  
**No official numeric `p_card` or model simulation was issued.** The transparent normal calculations below are exploratory and uncalibrated, not a validated joint distribution, a frozen reference receipt, or an established betting edge.

## Decision summary

| Contract | Evidence-based assessment | Formal probability |
|---|---|---|
| Mobis +3.0 | **Tentative lean**: home court, injuries affecting both import groups, direct defensive matchup against Lee Jung-hyun, and fragility of Goyang's recent high scoring | NOT_ESTIMATED |
| Goyang −3.0 | Slightly better season-long point differential and recent competitive margins; needs to win by 4 or more; imports and perimeter matchup present failure modes | NOT_ESTIMATED |
| Over 175.5 | Goyang's 3-point volume, both teams' porous scoring defence and season matchup midpoint near 176 provide the path | NOT_ESTIMATED |
| Under 175.5 | One import per team, possible reduced scoring efficiency, Mobis' recent low totals and strong 3-point suppression provide the path | NOT_ESTIMATED |
| Winner | Marginal Goyang lean in *unadjusted* season scoring, but near-even after home/away and changing rotations | NOT_ESTIMATED |

**Recommended decision under repository gate:** `NO_STRONG_PICK / ABSTAIN`. If forced to select a spread, Mobis +3.0 is the conditional qualitative preference. Neither side nor total meets the repo's supported 0.65 strong-pick requirement.

## A1. Identity, timing, event state

- Independent KBL organiser listing and Korean media identify the match as Ulsan Hyundai Mobis hosting Goyang Sono on 10 November at 19:00 Korea time, at Ulsan Dongchun Gymnasium.
- 10:00 UTC = 19:00 KST = 21:00 AEDT. The first time check in this analysis was 21:04:36 AEDT. The user supplied an estimated start and explicitly permits delays. Some web schedules continued to display *scheduled* and 0–0 placeholders, but these are not reliable first-play proof. The real opening tip is `NOT_VERIFIED`.
- No verified in-play score was used. Actual issue time relative to first play is `TIMING_UNVERIFIED` and this research cannot count as a clean, published pre-tip card.
- Identity source: https://www.kbl.or.kr/match/schedule ; official home-club https://phoebus.kbl.or.kr/ ; Korean reporting https://jumpball.co.kr/news/newsview.php?ncode=1065545227760436 ; corroboration https://sports.factnows.com/kbl/202611101066490163/ .

## A2. Exact contract freeze and definitions

| Exact contract | Settlement quantity and rule | Favours | Main failure mechanism |
|---|---|---|---|
| Mobis +3.0 | Mobis final points minus Goyang final points +3, including all overtime. W if Mobis wins or loses by 1–2; PUSH if loses by 3; L if loses by ≥4 | Mobis' home resilience / Goyang import vacancy | Goyang perimeter shooting runs away with game |
| Goyang −3.0 | Goyang final points minus Mobis final points −3, including overtime. W if Goyang wins by ≥4; PUSH if wins by 3 | Goyang offence / Mobis depleted depth | Spellman dominates and Mobis contain Lee Jung-hyun |
| Over 175.5 | Both teams' final score sum ≥176 including overtime | 3-point volume / weak defence / late fouling | Lower quality possessions with one foreign player each |
| Under 175.5 | Both teams' final score sum ≤175 including overtime | Reduced import depth / Mobis' 3P suppression | Goyang's high-volume 3P shooting or overtime |

Both handicap contracts refer to the same exact integer margin and are strict complements except for a shared push at exactly 3 points. Over and Under 175.5 have no integer push.

## A3. Evidence and match history

### Historical score rows (dated KBL games, newest first)

**Mobis:** 2026-11-08 Anyang 85–91; 11-05 Seoul Samsung 76–81; 10-31 @Daegu 67–94; 10-29 KCC 96–89; 10-24 Seoul Samsung 71–91; 10-22 LG 83–88; 10-18 @Suwon KT 96–80; 10-16 @Goyang 82–95; 10-12 Wonju DB 99–89; 10-10 Daegu 75–81; 10-05 KCC 87–97; 10-03 @Anyang 85–88.

**Goyang:** 2026-11-07 @LG 85–86; 11-03 @KCC 102–105; 11-01 KT 96–103; 10-30 Samsung 87–95; 10-26 LG 107–109; 10-24 KCC 97–96; 10-18 @Seoul SK 87–81; 10-16 Mobis 95–82; 10-13 @Anyang 81–85; 10-11 @Samsung 81–82; 10-09 @Suwon KT 79–88; 10-04 @Wonju DB 86–95; 10-03 Daegu 82–73.

Source routes: https://m.aiscore.com/en/basketball/team-ulsan-mobis-phoebus/w6975lsegwcnk23/matches ; https://m.aiscore.com/basketball/team-sligo-rovers/2ezk96irwgcwkn5/matches ; independent schedule/score cross-check: https://basketball.eurobasket.com/team/Goyang-Sono-Skygunners/1982/Games ; official KBL schedule above. The AiScore results contain erroneous W/L labels in some versions; team points and winning side were recomputed from raw displayed scores rather than trusting that label.

| Team | Window / actual n | Points scored | Points conceded | Combined | W–L |
|---|---:|---:|---:|---:|---:|
| Mobis | L5 / 5 | 79.0 | 89.2 | 168.2 | 1–4 |
| Mobis | L10 / 10 | 83.0 | 87.9 | 170.9 | 3–7 |
| Mobis | Season/L12 / 12 | 83.50 | 88.67 | 172.17 | 3–9 |
| Goyang | L5 / 5 | 95.4 | 99.6 | 195.0 | 0–5 |
| Goyang | L10 / 10 | 91.8 | 92.4 | 184.2 | 3–7 |
| Goyang | Season/L13 / 13 | 89.62 | 90.77 | 180.38 | 4–9 |

L15 and L20 are **short-season censored**: n=12 Mobis, n=13 Goyang. Do not import unverified previous-season results into these 2026–27 within-season windows. Sources are dated game results; an original source-publication timestamp for each row is not individually archived (`KNOWN_AT_UNVERIFIED` for rigorous prospective evidence).

### Prior head-to-head

Goyang beat Mobis 95–82 on 16 October 2026 (177 total). The 10 November pregame local report warns three of the four foreign players from that meeting were unavailable for the rematch. That materially reduces the current roster relevance of one-game historical matchup evidence. A full 10–20 meeting historical roster-adjusted series was **not** independently established.

### Both-team player availability, minutes and matchup

- **Mobis OUT:** Gage Prim (left knee ligament, approximately six-week recovery); Darius Bazley (left foot plantar injury, approximately six weeks). **Available as temporary replacement:** Omari Spellman; coach Yang Dong-geun said he intended to play all 40 minutes. Spellman played 40 minutes against Anyang on November 8 and scored 33 points. Long exposure presents fatigue and late-foul risk.
- **Mobis starting changes:** the pre-tip interview identifies Jerry Abadiano and Lee Do-heon replacing Park Mu-bin and Seo Myung-jin to defend Lee Jung-hyun. This corroborates two lineup slots, **not** a verified complete five or full active bench.
- **Goyang OUT:** Scotty James, fracture of lumbar transverse process with six-week estimate; older injury listings also mention Ahn Jeong-wook and Park Jong-ha, with their exact roster-day participation not verified. **Johnny O'Bryant** is expected to play as the sole foreign import, contradicting an older third-party tracker that still calls him questionable.
- **Goyang offensive form:** Lee Jung-hyun scored in double figures in nine consecutive games after his opening four; approximately 21.0 points and 3.7 threes in those nine. Goyang had made ≥10 threes in each of 13 games, averaging 14.6 makes at 36.5%; Mobis had allowed 8.6 made threes per game (league minimum), but surrendered 16 in the October H2H.
- **Players/bench gap:** one foreign player per club is well-supported; full official active lists, five starters on both sides, substitution/closing patterns, per-player shot attempts and opponent-adjusted minute effects are not fully verified. Replacements cannot automatically be treated as zero contributors.

Key pregame first-party-adjacent reporting (with embedded coach quotes): 2026-11-10 18:48 KST https://jumpball.co.kr/news/newsview.php?ncode=1065606520760737 ; 2026-11-10 10:00 KST https://jumpball.co.kr/news/newsview.php?ncode=1065545227760436 ; registered replacement https://jumpball.co.kr/news/newsview.php?ncode=1065574501927079 ; secondary injury corroboration https://www.dailyil.com/en/league/kbl/ .

## A4. Numerical attempts and reference suitability

### Historical repo league profile vs current league

The repository's 22 Oct 2026 KBL historical parameter row states mean total 159.39, home margin +1.18, residual margin SD 12.61 and total SD 16.82 points (`PARAMETERS.md`, Part A). However, the October-November 2026–27 league is scoring more: summing the published team *points-for* in the 10-team current standings (10,466 points across 122 team games, equivalent to 61 scheduled games) yields 171.57 points per game. That aggregate is a cross-sectional **approximation**, not a validated point-in-time official league baseline. Data: https://www.linevs.com/stats/?left_country=South+Korea&left_league=KBL&tab=teams . Source table may be refreshed after the issue horizon, so prospective admissibility is **not established**.

The 12/13-game team scoring midpoint is:
- Mobis expected from own offense versus opponent allowance = (83.5 + 90.8) / 2 = **87.15**.
- Goyang expected from own offense versus opponent allowance = (89.6 + 88.7) / 2 = **89.15**.
- Exploratory total = **176.30** points; Goyang expected lead **2.00** points, before proper opponent strength, home, player availability and current 3P effects.

Recent-form (L5) midpoint, highly exposed to pre-injury regimes:
- Mobis (79.0 + 99.6) / 2 = 89.3; Goyang (95.4 + 89.2) / 2 = 92.3; exploratory total 181.6 and Goyang +3.0.

Current home/away alternate midpoint based on published rounded splits:
- Mobis home 84.0 scored, Goyang away 88.9 conceded → Mobis 86.45;
- Goyang away 85.9 scored, Mobis home 88.4 conceded → Goyang 87.15;
- Alternative total 173.60 and Goyang +0.70, before player revisions.

Thus even **before injury adjustment**, reasonable simple calculations span totals ~173.6–181.6 and away leads ~0.7–3.0. Because the available data do not establish a measured effect size for a foreign-player absence or a validated matchup-specific pace × efficiency distribution, do **not** arbitrarily subtract a fixed number of points and call the result the `ANALYST_PRIMARY_V1` forecast.

### Transparency-only numeric calculation (NOT PRIMARY)

As a **demonstration only**, treating integer margin and total as marginal Normal variables around the *unadjusted season midpoint*, widening historical KBL residual SDs by 10% to represent uncertainty, gives margin SD ~13.87, total SD ~18.50. The probabilities below are not a complete joint possession-grid forecast; margin/total covariance, discrete overtime outcome paths, adjusted player minutes and calibration are missing. Approximate integer continuity cells for the 3-point spread are used, but are not validated model probabilities.

| Demonstration | Conditional decisive estimate | Limitation |
|---|---:|---|
| Goyang match win (winner margin ≥1) | ≈54.3% | simple unadjusted score-margin model |
| Mobis match win | ≈45.7% | same model, no team draw after OT |
| Mobis +3.0 cover given decisive | ≈53.0% | 2.9% illustrative exact-three PUSH mass |
| Goyang −3.0 cover given decisive | ≈47.0% | same push mass |
| Over 175.5 | ≈51.7% | unadjusted total normal, without availability |
| Under 175.5 | ≈48.3% | complement |

These approximate figures should **not** be used as final rank or confidence numbers: the present roster changes could move them by several percentage points, and the framework's issuance/freeze gates have not run. Strict publishable `p_card` for all contracts remains `NOT_ESTIMATED`.

`REFERENCE_TIER_COMMAND`: NOT_RUN (repository runtime unavailable). `REFERENCE_FROZEN_RECEIPT`: NOT_PERFORMED. `BASELINE_LEAGUE_V1`: approximate current league descriptive average available, exact-row frozen baseline NOT_COMPUTED. `MODEL_SHADOW`: NOT_RUN; no promotion entry in `ML_PROMOTIONS.csv`. No Monte Carlo simulation or code linter run is claimed.

## A5. Supplied contract assessment and risk

| Supplied row | Why it could win | Why it could lose | Assessment |
|---|---|---|---|
| Mobis +3.0 | At home; Mobis perimeter suppression; Goyang missing James; Spellman heavy-usage producer; intentional Lee Jung-hyun containment | Goyang still has O'Bryant, Lee and elite 3P volume; Mobis thin rotation and poor defence | Tentative conditional preference, no strong probability |
| Goyang −3.0 | Season net scoring margin better; won last H2H by 13; Mobis lost 4/5; Goyang's three-point volume creates separation | Home court; changed imports mean H2H stale; key Goyang shooter/injury volatility; could win close or lose | Not supported as clear favourite cover |
| Over 175.5 | Team matchup season 176.3; Goyang last5 total 195; 14.6 made threes per game; Mobis allowed almost 89 | James absence, Goyang shooting variance, intentional anti-shooter lineup, short bench fatigue | Near even, high volatility |
| Under 175.5 | Mobis last5 combined 168.2; two teams short of imports; Mobis holds other teams to fewer threes | Goyang 40 3PA/game; game may end in fouling or overtime; season totals already high | Near even, conditional under lean only |

The supplied spread is **+3.0/−3.0**, not a half-point line. A 3-point Goyang victory is a shared PUSH; the total half-point line has no push.

## A6. Injury/rest/venue scenario ledger (qualitative)

- **Regime:** one import per team, each with high-minute exposure; coaching/rotation effects not measured. `SCENARIO_UNQUANTIFIED`.
- **Rest/travel:** Mobis last played 8 Nov at home (two calendar days), Goyang 7 Nov at Changwon (three calendar days) and is travelling within southern Korea. No quantified KBL back-to-back effect is applicable. `REST_FACT_VERIFIED, EFFECT_NOT_ESTIMATED`.
- **Venue:** Ulsan Dongchun Gymnasium, Mobis home. Current home/away marks entering game: Mobis 2–6 home, Goyang 1–6 away. Quantified home-court delta unresolved.
- **Tempo / scoring regime:** current KBL scoring visibly higher than historical repo aggregate. Do not interchange older historical parameters with a point-in-time current league without documenting population drift.
- **In-game contingencies:** long stretches without a second import, O'Bryant foul trouble, Spellman fatigue and opponent-adjusted 3-point accuracy are the most important uncertain forks.

## A7. Distribution coherence and dependence

- Mobis +3.0 and Goyang −3.0 are opposite outcomes conditioned on the shared point-margin push at −3; they do not form independent selections.
- O175.5 and U175.5 are complementary with zero integer push and include every overtime point.
- Side and total are **correlated through import absences, shooting variance and foul/OT exposure**; no joint model was constructed, so the exact joint failure and derived two-leg safe-pair claims are `NOT_COMPUTED`.
- The illustrative normal margin/total computations lack an explicit KBL possession grid and calibrated overtime branch. No false 100,000-run simulation, fitted model or pregame freeze is claimed.
- The framework's rank-1 threshold (0.65) cannot be met by any *supported* adjusted numeric record here. `NO_STRONG_PICK / ABSTAIN`.

## A8. Source register, provenance and unresolved items

1. Organiser and venue: https://www.kbl.or.kr/match/schedule and https://phoebus.kbl.or.kr/ (fixture verified; actual tip NOT_VERIFIED).
2. Jumpball pre-tip coach interview (10 Nov 18:48 KST): https://jumpball.co.kr/news/newsview.php?ncode=1065606520760737 (critical active-import and starters change).
3. Jumpball pre-game report (10 Nov 10:00 KST): https://jumpball.co.kr/news/newsview.php?ncode=1065545227760436 (injuries, 3P, Lee, previous matchup warning).
4. Jumpball Spellman signing report (5 Nov): https://jumpball.co.kr/news/newsview.php?ncode=1065574501927079 .
5. Season score summaries: https://sports.factnows.com/kbl/202611101066490163/ ; https://m.aiscore.com/en/basketball/team-ulsan-mobis-phoebus/w6975lsegwcnk23/matches ; https://m.aiscore.com/basketball/team-sligo-rovers/2ezk96irwgcwkn5/matches ; https://basketball.eurobasket.com/team/Goyang-Sono-Skygunners/1982/Games .
6. Historical repository snapshot `main` HEAD `f79559b45183ca63a2ce5fc2611321975bae744f`, `CORE.md`, `research/prompts/1_GAME_CARD.md`, `research/prompts/1_sports/BASKETBALL.md`, `RULES_BASKETBALL.md`, `PARAMETERS.md`, `CURRENT_STATE.md`, `research/active_minis/20261109R3NEXT.md`, and empty `research/model_registry/ML_PROMOTIONS.csv`.

**Unresolved:** actual tipoff and first play; complete official game-day starters, bench, medical/eligibility statuses beyond documented out players; exact opponent-adjusted current ORtg/DRtg/pace; full native prior-game and publication timestamps; exact same-line empirical KBL reference distribution; measured import/replacement effect sizes; overtime model; joint score grid; writer authority and code-based card lint/freeze; a published research artifact in repository. Exact future evidence to pursue: KBL match feed first jump ball, confirmed active roster and minute log, up-to-date team possession splits, audited event score lines. No automation scheduled.

## A9. Integrity / completion matrix

| Required procedure | Work actually performed | Remaining limitation | Status |
|---|---|---|---|
| Authority / identity / timing | Read current GitHub published `main` at explicit full SHA; checked league schedule and venue | Local working tree inaccessible; first-play timestamp unknown | INFORMATION_INCOMPLETE |
| Both-side starters, bench, absences | Checked two detailed game-day Korean sport reports, coach quotes and injury tracker | Full five and bench unconfirmed, some older injury ambiguity | INFORMATION_INCOMPLETE |
| Online history / correction / known-at | Listed 12 Mobis and 13 Goyang dated 2026–27 KBL games; checked score direction against independent scores | Source-publication times for every game not retained | INFORMATION_INCOMPLETE |
| L5/L10/L15/L20/season/league | Computed valid L5,L10,season n; censored L15/L20 honestly; compared current and historical league point average | Exact current provider league total distribution, pace and rating data incomplete | INFORMATION_INCOMPLETE |
| Mechanisms/conditions/rules | Studied heavy import losses, replacement, Lee defence, 3P offence, rest and home court; included overtime/push | No observed second-lineup release or measured effect sizes | INFORMATION_INCOMPLETE |
| Reference/freeze/model receipts | Explicitly recorded no repository model, no freeze, no release | Repository runtime and publishing forbidden by user's read-only instruction | NOT_PERFORMED |
| Calculations and adjustments | Transparent matchup averaging, retrospective-only Normal demonstration; no unsupported numeric injury delta | Coherent adjusted joint possession/OT model not computed | INFORMATION_INCOMPLETE |
| Every supplied contract | Both directions of spread and total checked, including three-point push; qualitative pathways documented | Valid final adjusted `p_card` not estimated | DONE (assessment only) |
| Expected scores/baselines/dependence | Simplified means and league descriptive average; missing exact joint explicitly marked | No certified exact-row baseline, covariance, joint failure | INFORMATION_INCOMPLETE |
| A1–A9/delivery/custody | Separate complete research draft created in local sandbox | No GitHub append, lint, readback, commit, push or canonical import | READ_ONLY_DRAFT / NOT_ISSUED |

**No sporting result was observed or used.** `ISSUE=NOT_ISSUED`, `P_ID=NOT_ASSIGNED`, `LOCAL_KEY=NOT_ALLOCATED`, `SETTLEMENT=NOT_PERFORMED`, `CANONICAL_IMPORT=NOT_PERFORMED`, `REPOSITORY_WRITES=NONE`, `MODEL_SHADOW=NOT_RUN`. The active mini and canonical sequence remain untouched.
