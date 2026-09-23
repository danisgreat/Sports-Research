# Prediction Mini Running Log — session 2026-09-23 (WTA Singapore, Andreeva vs Sasnovich)

**Custody.** This session is **read-only** for every existing project file (user directive, 2026-09-23). This file is the session's own running log and is the only file written. No canonical log, status register, rule file or other mini log was changed.
**ID.** Temporary ID `TMP-20260923-WTA-SGP-ANDREEVA-SASNOVICH`. The merged running log (`C:\Users\danie\Documents\Sports Research\PREDICTION_MINI_RUNNING_LOG_MERGED_P482_ONWARD.md`, read 2026-09-23 ~20:28 AEST) lists **next ID P-494**. This session does not assign it, because concurrent sessions have already produced collisions (P-484). The proposed canonical ID is **P-494, pending reconciliation**.
**Governing method (read fresh this session).** MDS-2026.09.19-v4.3 / CR-2026.09.21-3; SFA-TENNIS (RULES_TENNIS.md §9, controls 1–14); GFA-2; SCV-2026.09.19-v2. SPORTS_ONLY / MARKET_BLIND. LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE. NO VALUE DETERMINABLE.

---

## Entry 1 — score-blind prior (append-only; written 2026-09-23 ~20:44 AEST, BEFORE any live score was viewed)

**Horizon statement.** The supplied estimated start was 20:30 AEST. At 20:31 AEST the WTA field-owner feed showed match `LS008` with `MatchState "C"`, `NumSets 0`, `MatchTimeTotal 00:00:00`, empty score, stamped `2026-09-23T10:20:39Z` (20:20 AEST). Research could not be completed before the start. **This entry is therefore NOT a pregame issue.** It is labelled `START_CROSSED — SCORE-BLIND PRIOR`. It was built from pre-match records only. The research scripts excluded this match from every player log, so no score was seen.

- Distribution v1 (superseded before any line was queried): `TMP-20260923-WTA-SGP-ANDREEVA-SASNOVICH-prior-v1`, frozen 20:41:19 AEST, SHA-256 `e679a464853e0f7e5f3235f86252dcce77fc31626d0b246e57a2dc955996b3ec`. It had independent sets, so its deciding-set rate was 22%.
- **Distribution v2 (controlling):** `…-prior-v2`, frozen **20:42:18 AEST**, SHA-256 **`380df425355035dca0cc274022d81a57ccd7abede713532894c0bb95cc81528c`**.
  - Why v2 replaced v1: the direct comparables showed more deciding sets than the model. Andreeva went three sets in 6 of 17 hard-court matches against opponents ranked outside the top 50; Sasnovich went three sets in 35% of her hard L20. v2 adds declared set-level variation, shrunk toward a population rate.
  - The change was made before the lines were queried. It used sporting evidence only.
- Line query time: **20:42:57 AEST** (after the v2 freeze).

**Model.** Exact point → game → set → match Markov chain: ad scoring, 7-point tiebreak in every set including the decider (WTA rule).
- Andreeva serve-point probability = s + δ + ε; Sasnovich's = s − δ − ε.
- δ ~ N(0.070, 0.050) across matches (form).
- ε ~ N(0, 0.045) per set (within-match variation).
- s ∈ {0.54, 0.56, 0.58}, weights {0.25, 0.50, 0.25}. The court check this week (13 completed main-draw matches) was 992/1770 = 0.560.
- Retirement/walkover mass: 0.015. All probabilities below are conditional on normal completion unless stated.

| Family (`TE-B*`) | Mass | Mean total | Mean margin (A−S) |
|---|---:|---:|---:|
| B1 Andreeva straight-set control (≤3 games conceded per set) | 0.395 | 15.0 | +9.0 |
| B2 Andreeva close straight sets | 0.257 | 19.3 | +5.7 |
| B3 Andreeva deciding-set win | 0.193 | 27.4 | +4.3 |
| B4 Sasnovich straight-set control | 0.022 | 16.0 | −8.0 |
| B5 Sasnovich close straight sets | 0.052 | 20.3 | −5.0 |
| B6 Sasnovich deciding-set win | 0.081 | 28.3 | −2.5 |
| **Sum** | **1.000** | | |

- **Winner:** P(Andreeva) = 0.845.
- **Set count:** P(two sets) = 0.725.
- **Total games:** mean 19.84, SD 5.67, median 18, 10/25/75/90th percentiles 14/15/24/29.
- **Margin:** mean +5.24, SD 4.84, median +6, 10/90th percentiles −3/+10.

**Queries (after freeze).**

| Contract | P(win given completion) | Unconditional (retirement → void 0.015) |
|---|---:|---:|
| Under 18.5 | 0.5296 | 0.5216 |
| Sasnovich +6.5 | 0.5008 | 0.4933 |
| Andreeva −6.5 | 0.4992 | 0.4917 |
| Over 18.5 | 0.4704 | 0.4634 |

- Joint probabilities: P(U18.5 ∧ S+6.5) = 0.090; P(U18.5 ∧ A−6.5) = 0.440; P(O18.5 ∧ S+6.5) = 0.411; P(O18.5 ∧ A−6.5) = 0.060.
- Sensitivity (8 parameter sets): Under 18.5 is preferred in 7 of 8. The handicap flips with the dominance centre (A−6.5 ranges 0.42–0.58), so it is a NEAR_TIE.

*(Live state check and issued view follow in Entry 2.)*

---

## Entry 2 — ISSUED LIVE VIEW `TMP-20260923-WTA-SGP-ANDREEVA-SASNOVICH-LIVE-v1` (append-only; written ~20:53 AEST)

**Status:** UNSETTLED — **LIVE-ISSUED VIEW**. This is not a pregame card. It belongs in the separate live horizon and is excluded from pregame metrics. No retrospective has been done, per the user's instruction.

### Field 1 — Identity and contract

**Event.**
- Singapore Tennis Open presented by BNP Paribas 2026. WTA 500, 28-player draw, singles Round of 16 (`RoundID 2`).
- WTA event 1152/2026, match `LS008`, Court 1 (Tennis.com labels it "Center Court").
- Venue: Singapore; **indoor hard** (WTA tournament record `inOutdoor: "I"`, `surface: "Hard"`).

**Players.**
- [1] Mirra Andreeva (RUS; WTA #5; right-handed; born 2007-04-29). Seeded 1; R1 bye.
- Aliaksandra Sasnovich (BLR; WTA #132; right-handed; born 1994-03-22; career high #29). Direct entry. Beat Kasatkina 7-5 6-0 in R1 on 21 Sep (1:19:54).

**Time and state.**
- Venue zone `Asia/Singapore` (UTC+8). Melbourne zone `Australia/Melbourne` = **AEST** (UTC+10; DST starts 4 Oct 2026). No calendar rollover.
- The user's 20:30 AEST start is an estimate; it equals 18:30 SGT. ESPN lists the start as 2026-09-23T10:35Z (20:35 AEST).
- The WTA feed implies first ball at about **10:38:15Z (20:38 AEST)**: feed update 10:43:40Z minus 00:05:25 elapsed.
- **GAME-STATE: LIVE.** Observation: WTA feed `lastUpdated 2026-09-23T10:51:14.687Z` (20:51:14 AEST); state `P`; elapsed `00:12:59`.
- **Set 1: Andreeva 2–1. Andreeva serving at 0–0 in game 4.**
- Serving history in set 1: Sasnovich served game 1 and was broken (Andreeva converted 1/1 break points). Andreeva held game 2. Sasnovich held game 3 from 40–Ad.
- Computed at 20:51:54 AEST.

**Contracts (supplied; quarantined until the v2 freeze at 20:42:18).**
- Andreeva −6.5 games / Sasnovich +6.5 games: aggregate games margin.
- Total games Over / Under 18.5.
- Both are half-lines, so there is no push. Each is a FORCED_PAIR conditional on action.
- A tiebreak set counts as 7–6 = 13 games.
- WTA rules: best of three, 7-point tiebreak at 6–6 in every set including the decider (RULES_TENNIS §10.2).

**Operator retirement/walkover terms:** not supplied → `UNKNOWN_DEFINITION` / NO VALUE DETERMINABLE.
- The research grade assumes normal completion.
- Under standard conventions (§10.6), a retirement voids handicap and total rows unless the threshold was already decided. Over 18.5 can be decided before a retirement once 19 games have been completed.

**The supplied pregame lines may no longer be offered at this state.**

**Method/controls:** MDS-2026.09.19-v4.3 / CR-2026.09.21-3 / SFA-TENNIS; RULES_GENERAL §7 live analysis; RULES_TENNIS §6 live state ("recalculate only the remaining point/game/set tree; do not extrapolate a short hot spell as a permanent rate change").

**Preflight:** `prediction_preflight.py` is a normal-pregame validator and requires `event_state PREGAME/SCHEDULED`. This view is LIVE, so the pregame path is **BLOCKED by design** and was not used. The live path was run under §7: the official field-owner live state controls, and two further independent front ends agree on orientation.

### Field 2 — Evidence and exposure

**Source record.** All retrieved 2026-09-23 between 20:31 and 20:52 AEST.

| # | Source (lineage) | Field owner? | What it established | Retrieved (AEST) |
|---|---|---|---|---|
| S1 | WTA API `api.wtatennis.com/tennis/tournaments/1152/2026/matches/` (WTA) | Yes | Identity, round, court, seeds, entries; state C→P; live score, point and server; R1 results; indoor hard; 28-player draw | 20:31, 20:44, 20:49, 20:51 |
| S2 | WTA API `…/matches/{id}/stats` (WTA) | Yes (same lineage as S1) | Per-match serve/return totals for 2025–26 matches; this match's live set-1 stats; the week's court serve environment | 20:34–20:52 |
| S3 | WTA API `…/players/{331809,317790}/matches/?year=2023…2026` (WTA) | Yes (same lineage) | Match logs, L5–L20 windows, H2H (Iasi 2024) | 20:32–20:36 |
| S4 | ESPN `site.api.espn.com/apis/site/v2/sports/tennis/wta/scoreboard` (ESPN) | No; independent publisher | "In Progress, 1st Set", Andreeva 1–0 and serving (at 20:45); start listing 10:35Z; R1 Sasnovich d. Kasatkina 7-5 6-0 Final | 20:45 |
| S5 | Tennis.com match page (Tennis Channel), raw HTML plus `r.jina.ai` text | No; independent publisher | "Live"; Round 2 WTA Singapore; rankings 5/132; both right-handed; career-high 29; H2H Iasi 23 Jul 2024, Andreeva 6-1 6-3. Its snapshot lagged S1 (1–0, 40–40): publication lag, not a conflict | 20:50 |
| S6 | Tennis Abstract WTA Elo `tennisabstract.com/reports/wta_elo_ratings.html`, "Last update: 2026-09-21" | Rating benchmark only (control 13) | Andreeva Elo 2047.9 / hElo 1981.4; Sasnovich 1701.9 / 1668.5; Kasatkina 1783.7 / 1741.1 | 20:36 |

- The upstream vendors behind the S4/S5 live scores are not documented, so shared vendor lineage cannot be excluded. The official feed S1 controls the state (§7). Event identity rests on three distinct publishers: WTA, ESPN and Tennis Channel.

**Participants.**
- Tennis bench: NOT_APPLICABLE.
- Coaches: `COACH_NOT_RETRIEVED` for both. Coaching is not used directionally.

**Workload.**
- Andreeva: first match of the event (R1 bye). Her last match was a US Open QF loss to Gauff, 6-2 6-7(7) 2-6, during the 30 Aug–13 Sep event, so about two weeks' rest.
- Sasnovich: R1 on 21 Sep (1:19:54). She is also entered in doubles with Friedsam (LD014, later today, "After suitable rest").
- No withdrawal or medical marker in S1 at any check.

**Environment.** Indoor; weather gate not applicable. Current court: `SURFACE_CONDITION_NOT_PUBLISHED`. Observed proxy: pooled serve points won this week, 992/1770 = 0.560 across 13 completed main-draw matches.

**Disaggregated serve/return records (G-L7, not aggregate-only).** Both players' per-match 2025–26 hard-court logs were printed. Aggregates, with SE:

| Player / split | Matches | Serve points won | Return points won |
|---|---:|---|---|
| Andreeva, hard 2026, all | 27 | 1151/1909 = .603 (SE .011) | 917/1936 = .474 (SE .011) |
| Andreeva, vs top 50 | 20 | .586 | .455 |
| Andreeva, vs outside top 50 | 7 | 259/386 = .671 | 221/406 = .544 |
| Sasnovich, hard 2025–26, all | 38 | 1537/2703 = .569 | 1205/2665 = .452 |
| Sasnovich, vs top 50 | 10 | .540 | .425 |
| Sasnovich, vs top 20 (6 matches) | 6 | 195/356 = .548 | 144/374 = .385 |

- Sasnovich's six hard-court matches against top-20 players, with game totals: Paolini L 3-12, Samsonova L 8-12, **Tauson W 12-5**, Bencic L 7-12, Kostyuk L 6-12, **Osaka W 13-12**.
- Sasnovich's R1 here (S2): serve 33/50 = .660, return 32/58 = .552, 0 double faults. Kasatkina made 7 double faults.

**Recency windows (hard court; descriptive only; overlapping; one evidence unit).**

| Window | Andreeva W-L | Games % | Avg total | 3-set % | Margin | Opp. rank | Sasnovich W-L* | Games % | Avg total | 3-set % | Margin | Opp. rank |
|---|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|---:|
| L5 | 4-1 | .613 | 22.2 | 40 | +5.0 | 39 | 1-4 | .435 | 23.0 | 40 | −3.0 | 110 |
| L10 | 7-3 | .593 | 19.9 | 30 | +3.7 | 39 | 4-6 | .473 | 22.0 | 30 | −1.2 | 130 |
| L15 | 10-5 | .588 | 21.3 | 40 | +3.7 | 39 | 6-9 | .467 | 21.0 | 20 | −1.4 | 106 |
| L20 | 12-8 | .569 | 22.1 | 40 | +3.0 | 35 | 10-10 | .493 | 22.5 | 35 | −0.3 | 111 |

- \*The WTA player feed excludes Sasnovich's Singapore R1 win (12-5 games). Including it, her L5 is 2-3.
- Andreeva's 2025 post-US Open Asian swing (Beijing R16 L to Kartal, Wuhan R32 L to Siegemund with 15 double faults, Ningbo R16 L to Lin Zhu (#219) with 12 double faults) and her flat 2026 hard-court losses (Fernandez 5-12; Kostyuk 8-16) are context under R-1. They widen the distribution and carry no signed lean.

**H2H.** One meeting: Iasi 2024 (outdoor clay, WTA 250), Andreeva 6-1 6-3 (S3, S5). Continuity count 0 (different surface; more than two years old; Andreeva's level has changed). **Zero directional weight.**

**Reference base rate:** `NOT_YET_DERIVED` (BASE_RATES_REGISTER; tennis) for every row.

### Field 3 — Joint distribution

- **Prior:** frozen v2 (Entry 1; SHA-256 `380df425…28c`). δ ~ N(0.070, 0.050); ε per set ~ N(0, 0.045); serve environment s ∈ {.54, .56, .58}.
- **How the centre was set.**
  - Andreeva-side comparables (similar opposition, including her 2025 losses) point to a total-points share of about .58–.59.
  - Sasnovich-side comparables (her record against the top 20, adjusted because Andreeva is stronger than the average top-20 player) point to about .55.
  - The midpoint is .57, i.e. δ = .07.
  - Form SD widened for named regime uncertainty: Andreeva's first match in about two weeks and her first indoor hard event of the swing.
- **Elo benchmark (control 13):** the Elo gaps (313 hard, 346 overall) imply Andreeva .86–.88 before the match. The frozen prior's .845 is within 3.5 points, so no mechanism is required.
- **Live transformation:** exact remaining point/game/set tree from the S1 state (set 1 at 2–1, Andreeva serving at 0–0; Sasnovich served first in set 1), at frozen-v2 rates. No parameter update (RULES_TENNIS §6).
  - Sensitivity with a Bayesian point update on set-1 points (A 4/4, B 5/11 on serve; the stats lag the score): posterior mean δ .0855.

| Family (live, given completion) | Mass |
|---|---:|
| B1 Andreeva straight-set control | 0.4157 |
| B2 Andreeva close straight sets | 0.2864 |
| B3 Andreeva deciding-set win | 0.1704 |
| B4 Sasnovich straight-set control | 0.0096 |
| B5 Sasnovich close straight sets | 0.0406 |
| B6 Sasnovich deciding-set win | 0.0773 |
| **Sum** | **1.0000** |

- **Winner and set count:** P(Andreeva) = 0.8725; P(three sets) = 0.2477.
- **Total games:** mean 19.86, median 18, 10/90th percentiles 14/29. Mass at 18 = .100; at 19 = .053.
- **Margin:** mean +5.49, median +6, 10/90th percentiles −2/+10. Mass at +6 = .149; at +7 = .116.
- Most likely set sequences: 6-2 6-2 (.059), 6-1 6-1 (.052), 6-2 6-1 (.046), 6-2 6-4 (.038), 6-2 6-0 (.038).
- Retirement/walkover: 0.015, carried as void/unknown. The unconditional win probability is about p × 0.985.
- Output receipt: `final_refresh2.txt`, SHA-256 `bed8c304fdaa4b19aad2e27fda9449340dc86222569da3e2dc561404c6e5bb74` (session scratchpad).

### Field 4 — Ranked contracts (all `UNVALIDATED_SUBJECTIVE`; conditional on completion; SPORTS_ONLY / MARKET_BLIND)

| Rank | Contract | p (issued) | p (Bayes sensitivity) | Verdict / evidence | Role | rank_gap to next |
|---|---|---:|---:|---|---|---|
| **1** | **Under 18.5 total games** | **0.550** | 0.645 | LEAN / LOW (line inside the central corridor; median 18) | PRIMARY_FORMAL (total pair) | SMALL |
| **2** | **Sasnovich +6.5 games** | **0.510** | 0.409 | FORCED RANK / LOW, **NEAR_TIED with #3** (the line sits on the median margin, +6; the order flips under sensitivity) | PRIMARY_FORMAL (handicap pair) | NEAR_TIE |
| **3** | Andreeva −6.5 games | 0.490 | 0.591 | FORCED RANK / LOW | CORRELATED complement of #2 | SMALL |
| **4** | Over 18.5 total games | 0.450 | 0.355 | AVOID-lean / LOW | Complement of #1 | — |

- **Preferred sides:** Under 18.5 (total pair); Sasnovich +6.5 (handicap pair, near-tie).
- **Top over/under:** Under 18.5, which is also Rank #1. A `TOP_OU_REVIEW` applies if it fails.
- **Potential winner:** **Mirra Andreeva**, 0.8725 given completion (sensitivity 0.929; score-blind pre-match 0.845; Elo benchmark .86–.88). Verdict LEAN.
  - Main failure paths: Sasnovich's first-strike, backhand-led upset branch (she beat #14 Tauson and #14 Osaka on hard in the last 12 months) = B4–B6, 0.1275; retirement 0.015.

### Field 5 — Dependence and checks

- **Representative Rank-#1 outcome:** Andreeva 6-2 6-2 (the modal sequence).
  - 16 games → Under WIN. Margin +8 → Andreeva −6.5 WIN, Sasnovich +6.5 **LOSS**. Andreeva wins.
  - So the modal branch **defeats Rank #2** (C-MODAL-BRANCH-CHECK disclosure).
  - A joint-success representative for R1 ∧ R2 is 6-3 6-3 or 6-4 6-2: 18 games, +6.
- **P(R1 ∧ R2) = 0.106** (U ∧ S). Fréchet bounds [0.060, 0.510]. **Strongly anti-coupled (M18).**
  - The shared driver is match shape. An Andreeva routine straight-sets win helps #1 and hurts #2. A competitive or three-set match helps #2 and hurts #1.
- **P(¬R1 ∧ ¬R2) = 0.046** (Over ∧ Andreeva −6.5). The single state: Andreeva wins by 7+ in an extended match, e.g. 7-5 6-1 or 6-1 4-6 6-1.
- **P(exactly one of the top two wins) = 0.848.**
- **Complement of R1 (Over 18.5, 0.450):** B3 0.170 + B6 0.077 (every deciding set; the minimum three-set total is 18) + the ≥19-game parts of B2/B5 (6-4 6-3, 7-5 6-2, 7-6 …) 0.203.
- **Complement of R2 (Andreeva −6.5, 0.490):** U ∧ A 0.444 (B1: 6-2 6-2, 6-1 6-1 …) + O ∧ A 0.046.
- **Bidirectional sign (G22):** Andreeva's double-fault spells (15 at Wuhan, 12 at Ningbo 2025) lengthen sets (→ Over, +6.5) and do not flip the winner; handled through ε width. Sasnovich's double-fault volatility (5–7 double faults in several matches; 0 in R1) produces breaks → shorter, one-sided sets (→ Under, −6.5). Both signs are in the ε/δ width; no signed lean.
- **G27 swap test (#4 Over vs #3 Andreeva −6.5):** Over survives every deciding set plus close straight sets. Andreeva −6.5 survives only dominant straight sets. The marginal favours #3 (0.490 vs 0.450). Order kept.
- **Sensitivity (v2 prior, 8 parameter sets, before the live state):** Under preferred in 7 of 8; the handicap spans .42–.58. The live Bayesian sensitivity flips #2/#3. **No confidence claim on the handicap.**

### Field 6 — Freeze and follow-up

- **Freeze:** the issued numbers are from the refresh computed 20:51:54 AEST on feed state 20:51:14. The live state will have moved by delivery; this view is valid only for its observation state.
- **Settlement route (G10.2).** Verified this session to return final set scores for this event:
  - S1 WTA feed: `ScoreSet*`, `ResultString`, `MatchState "F"`.
  - S4 ESPN linescores.
  - S5 Tennis.com.
  - Games = sum of set games (a tiebreak set counts as 13). Settlement needs three lineages with a terminal marker (C-FINAL3).
- **Retirement/medical time-outs:** record the set and game score at the time if one occurs (G-L23).
- **Retry trigger:** at the next session, check that S1 `MatchState = "F"` and that ResultString is present.
- **Not appended** to `PREDICTION_LOG_COMBINED_5.md` or any other existing file (read-only directive). Proposed canonical ID P-494, pending reconciliation.

### §16.8 completeness block

1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (indoor), G16, G20/G20.1, G22, G27, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L22, R-1, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_TENNIS §6 and controls 1–14.
2. Families with masses: above (sum 1.0000).
3. Total: centre (mean) 19.86 / median 18; SD about 5.7 (prior); line 18.5; P(Under) .550. Margin: mean +5.49 / median +6; SD about 4.8 (prior); line 6.5; P(Sasnovich +6.5) .510. Normalised edges: total |19.86 − 18.5| / 5.7 = 0.24 (the mean is above the line while the median is below it, because the total is right-skewed); margin |5.49 − 6.5| / 4.8 = 0.21.
4. Complement decompositions for R1 and R2: above.
5. P(R1 ∧ R2) = 0.106, anti-coupled.
   - 5a. P(¬R1 ∧ ¬R2) = 0.046; state named above.
   - 5b. Both pairs are FORCED_PAIR; preferred sides Under 18.5 and Sasnovich +6.5; push mass 0 (half-lines).
6. Representative R1 outcome 6-2 6-2: checked; it defeats R2 (disclosed).
7. Participants: both confirmed on court by the S1 live state; bench NOT_APPLICABLE; coaches `COACH_NOT_RETRIEVED`.
8. AGGREGATE_ONLY: none (per-match logs printed). SEs printed. Small-sample note: the live Bayesian update rests on about 15 points, so it is reported as sensitivity only.
9. Settlement source per row: S1 (field owner) + S4 + S5.
10. At settlement only: to be completed later.

**Source firewall:** no odds, betting previews, tipsters, prediction markets, fantasy or DFS material was opened or used. Tennis Abstract Elo is a sports rating used as a benchmark only.

**Control receipt (PF-7), checked at ~20:55 AEST.** `CONTROL_MANIFEST_2026-09-21-3.md` SHA-256 `079b43f75681818724723556d66a82c01f56f6383f82055f0f50af88c97c0c00`. The live file hashes equal the manifest rows:
- METHOD.md `4f400025…f820b`
- RULES_GENERAL.md `08cf84fc…0522c`
- RULES_TENNIS.md `0994c197…dcd1`

**ID note.** A concurrent local log, `Mini Prediction Log - P-494 onward - 2026-09-23/`, was created at 20:44 AEST during this session. At 20:55 it had issued nothing and said "allocate P-494 only when a new forecast is actually frozen". This view was frozen at 20:51:54 AEST. It keeps `TMP-20260923-WTA-SGP-ANDREEVA-SASNOVICH` and proposes P-494 (or the next free ID) at reconciliation. The concurrent log was only read, not written.

**Delivery-time snapshot (not used in the numbers).** Feed 20:53:12 AEST: `P`, elapsed 00:14:57, set 1 Andreeva 2–1, Andreeva serving at 15–0.
