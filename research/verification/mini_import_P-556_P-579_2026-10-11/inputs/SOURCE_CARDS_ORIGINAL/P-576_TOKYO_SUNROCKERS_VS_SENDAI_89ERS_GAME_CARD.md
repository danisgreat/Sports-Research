<!-- BEGIN CARD P-576 -->
## Card · P-576 · BASKETBALL / JAPAN B.LEAGUE PREMIER · Sendai 89ers @ Tokyo Sunrockers · 2026-10-11

- **Working ID:** `P-576 — LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT`
- **Event key:** `BPREMIER:2026-27:506457:2026-10-11`
- **Native event ID:** `506457` (B.LEAGUE ScheduleKey)
- **Sport:** `Basketball`
- **League:** `Japan B.LEAGUE PREMIER (B.PREMIER), 2026–27 regular season`
- **Tracking alias:** `LOCAL-20261011-P-576-BPREMIER-SEN-TOK`
- **Analysis status:** `UNCALIBRATED_ANALYST_SCENARIO`
- **Timing state:** `PREGAME`
- **Research completed:** `2026-10-11T18:55:25+11:00`
- **Scheduled start:** `2026-10-11T19:05:00+11:00` (17:05 JST, UTC+09)
- **Endpoint:** `Full game, four 10-minute regulation quarters and all 5-minute overtimes until a winner; all chosen lines are half-point no-push; the supplied ±1.0 lines push at exactly a one-point Tokyo margin (operator terms unknown)`
- **Distribution object:** `basketball_bpremier_pace_oppadj_gauss_ot_v1 — 1,200,000 seeded synthetic joint terminal score draws (seed 20261011576); 74.84 regulation possessions; shrinkage 60% 2026-27 BP stats /40% explicit scenario prior; regulation home 86.681, away 84.373; T SD 21.0, home margin SD 16.0, corr(T,M)=0.03; integer score conversion and full 5-minute OT resolution`
- **Expected score:** `points, full game incl. all overtime; SDs on seeded terminal simulation — Tokyo Sunrockers 86.98 (SD 13.55) · Sendai 89ers 84.68 (SD 13.21) · total 171.66 (SD 21.41) · margin Tokyo − Sendai +2.30 (SD 16.04)`
- **Regime flags:** `BPREMIER_2026_NEW_FORMAT`, `EARLY_SEASON_SIX_GAMES` (no fitted/registered B.PREMIER multiplier; 1.000 multiplier retained)
- **Retirement rule:** `N/A`
- **Listed-pitcher rule:** `N/A`
- **Abandonment rule:** `FRAMEWORK_DEFAULT: void if no official final/result is awarded; otherwise settle from league's official final and full-game rules`
- **Settlement fields:** `Official final score home/away, quarter-by-quarter splits and overtimes, official starters/active-roster and did-not-play (provider: B.LEAGUE game_detail ScheduleKey 506457; fallback: B.LEAGUE club match report and independent structured game summary)`
- **Capture due:** `2026-10-12T19:05:00+11:00`
- **Rules read:** `danisgreat/Sports-Research main @ 33d0ea0c1c70056db7c7fb0a07dec77a633e573f: CURRENT_STATE, METHOD, CURRENT_RULES §§2–9; SELECTION_RULES §§1–6; CARD_AND_LOG_TEMPLATES §§3,3a,4,7; RULES_BASKETBALL §§0,3,4,5,7,8,9; PROBABILITY_TOOLKIT §§1,1.2,1.3; BASE_RATES_REGISTER §§3,7.1 (other leagues, not transferred as B.PREMIER fitted priors); LEAGUE_PROFILES Basketball (NO Japan B.PREMIER row); SOURCES §3.2 with league/team direct fallback; ARCHIVE_USE_GUIDE §§1–5; research/prompts/README,1_GAME_CARD; league official competition format and overtime rule`
- **Archive check:** `ARCHIVE_UNAVAILABLE: Previous Sports Results/Basketball/B League/2024/2024_games.csv and /2025/2025_games.csv opened on main: one header only, zero match data rows; 2026/2026_games.csv NOT_FOUND; no archive-derived B.PREMIER SD, OT rate, league average or team form claimed. Historical 2025–26 B1 team lines shown on official club pages only as context, not pooled; use official 2026–27 pregame club stats for current six-game inputs.`
- **Evidence quotes:** `B.LEAGUE official match page (retrieved 2026-10-11 18:49–18:53 AEDT): "17:05 TIP OFF", "4勝-2敗", "3勝-3敗"; Tokyo club official stats (page update 2026-10-10 21:48 JST): 2026-27 BP "75.9 ... 119.6 ... 108.9" under PACE / OFFRTG / DEFRTG; Sendai official club page (updated 2026-10-10 21:48 JST): BP "74.9 ... 118.9 ... 111.8"; official starting fives and game-day absences: NOT_VERIFIED, no claim made.`

### Decision block

**Distribution:** `basketball_bpremier_pace_oppadj_gauss_ot_v1` — possessions×opponent-adjusted efficiency; 74.84 possessions, Tokyo/Sendai regulation 86.681/84.373, bivariate total SD 21.0/margin SD 16.0/correlation 0.03; integer scoring plus repeated 5-minute overtime on a regulation tie. The seeded joint distribution prices every candidate and supplies terminal mean 171.66 total and 2.30 Tokyo margin.

| Rank | Role | Tag | Proposition | p_card | Probability status | Evidence | Failure route |
|---|---|---|---|---|---|---|---|
| 1 | PICK | ANALYST_DERIVED (replaces supplied Over 169.5) | Combined total Over 144.5 points — full game including OT | 89.9% | FROM_DISTRIBUTION:basketball_bpremier_pace_oppadj_gauss_ot_v1 | Official team pace 75.9/74.9, offensive ratings 119.6/118.9; shrunk regulation mean 171.05; final mean 171.66 | Slow tempo and extreme poor shooting keep the final at 144 or fewer |
| 2 | PICK | ANALYST_DERIVED (replaces supplied Under 169.5) | Combined total Under 198.5 points — full game including OT | 89.6% | FROM_DISTRIBUTION:basketball_bpremier_pace_oppadj_gauss_ot_v1 | Joint terminal total SD 21.41 and tail-inclusive OT branch; no fitted B.PREMIER historical profile | Exceptional offence, hot threes, fouling or one/multiple OTs yield at least 199 |
| 3 | INFORMATIONAL | ANALYST_DERIVED (replaces supplied Tokyo -1.0) | Tokyo Sunrockers +17.5 points — full game including OT | 89.2% | FROM_DISTRIBUTION:basketball_bpremier_pace_oppadj_gauss_ot_v1 | Home margin +2.30, SD 16.04; Tokyo 4–2 and strong offensive rebounding (17.7/game) | Sendai win by 18+; Culver/Layman shot-making and Tokyo 29.8% three-point form |
| 4 | INFORMATIONAL | ANALYST_DERIVED (replaces supplied Sendai +1.0) | Sendai 89ers +21.5 points — full game including OT | 88.5% | FROM_DISTRIBUTION:basketball_bpremier_pace_oppadj_gauss_ot_v1 | Sendai offence 118.9 OFFRTG, Culver 26.8 PPG; full-game mean margin Tokyo +2.30 | Tokyo victory by 22+, offensive boards and interior mismatch |

**P(Rank 1 and Rank 2 both lose):** `0.0% by construction` — combined total cannot be ≤144 and ≥199 in the same final.
**Rank 1 − Rank 2 gap:** `0.3 points` (89.9% vs 89.6%).
**Rank-1 gate:** `RANK1_UNSTABLE` — p_card 89.9%; best non-complementary alternative 89.6%; margin 0.3 points (<4.0 required; both ≥62%).
**Adjustment dependence:** `NONE` (no >0.25-SD directional analyst adjustment individually, but thresholds depend on shrinkage prior; sensitivity below).
**Supplied rows not selected:** `Tokyo Sunrockers −1.0 — WIN 53.0%, PUSH 2.7%, LOSS 44.3%; Sendai 89ers +1.0 — WIN 44.3%, PUSH 2.7%, LOSS 53.0%; combined total Over 169.5 — 53.8%; Under 169.5 — 46.2%; all full game including OT, same distribution; supplied ±1.0 operator-specific semantics not verified.`
**Potential winner:** `Tokyo Sunrockers — 55.7%` (full game including all overtime; Sendai 89ers 44.3%; no draw).

### Appendix

#### A1. Identity, timing and state
- **Identity:** Tokyo Sunrockers (official 東京サンロッカーズ, Tokyo SR, recently named Sunrockers Shibuya in older databases) HOST vs Sendai 89ers AWAY. Official event ID 506457, Toyota Arena Tokyo, 2026-10-11 17:05 Japan = 19:05 Australia/Melbourne. League's 26-team B.PREMIER regular season; on-court-free foreign-player rules introduced this season. These roster regime changes invalidate blind transfer of B1 scoring defaults.
- **Point-in-time:** Prepared `2026-10-11T18:55:25+11:00`, against 19:05 scheduled tip, with only completed games through 2026-10-09. Official fixture page was still scheduled/pre-tip on retrieval; actual first jump ball was not independently observed. **PREGAME based on published schedule, START_UNVERIFIED**; if official tip unexpectedly occurred earlier, reclassify via dated addendum. No outcome, live scoreboard or in-game event used to forecast.
- **Game rules:** four 10-minute quarters and 5-minute overtime repeated until a winner; official B.LEAGUE basketball_rule and competition format; all main four rows half-point totals/handicaps with no ties or pushes.
- **Availability:** club rosters and six-game participation rates are authenticated, but **neither official active roster nor the two starting fives / game-day injury release were obtainable as exact-game documents**. The card carries an aggregate availability mixture (wider SD) and is not eligible for official lineup-confirmed certification. Neither absence nor fitness is inferred from silence.

#### A2. Supplied contracts (reference only, Rule P4)
| Supplied | Exact interpretation | Model grade candidates |
|---|---|---|
| Tokyo Sunrockers -1.0 | Full game incl. OT; Tokyo win by 2+ covers; win by 1 pushes; Tokyo loses/ties after regulation ultimately loses | WIN 53.0 / PUSH 2.7 / LOSS 44.3% |
| Sendai 89ers +1.0 | Full game incl. OT; Tokyo wins by 1 pushes; otherwise Sendai wins outright | WIN 44.3 / PUSH 2.7 / LOSS 53.0% |
| Total Over 169.5 | Full game incl. OT, total at least 170 | 53.8% |
| Total Under 169.5 | Full game incl. OT, total at most 169 | 46.2% |

**Definition flag:** the supplied integer spread rules are inferred from standard Asian handicap push geometry; the unnamed operator may treat draws/lines differently; `UNKNOWN_DEFINITION` for operator settlement. Under the declared sporting endpoint, they have 2.7% push and cannot both win.

#### A3. Pre-event evidence summary and team comparison
| Field | Tokyo (home) | Sendai (away) | Custody |
|---|---:|---:|---|
| Current record (six games) | 4–2 | 3–3 | Official B.LEAGUE game and club pages |
| Points for / against per game | 90.8 / 82.7 | 89.0 / 83.7 | Club statistics, through 2026-10-09 |
| Pace, 40-min possession basis | 75.9 | 74.9 | Official club advanced BP season row |
| OFFRTG / DEFRTG per 100 possessions | 119.6 / 108.9 | 118.9 / 111.8 | Official club advanced BP season row |
| FG%, 3P%, FT% | 43.5, 29.8, 66.9 | 44.5, 36.3, 80.5 | Official B.LEAGUE preview |
| Effective field goal percentage | 49.9% | 53.3% | Official team advanced stats |
| Off. reb / TO per game | 17.7 / 10.3 | 12.0 / 9.2 | Official club basic season row |
| Total reb / assists per game | 45.0 / 23.8 | 35.0 / 22.5 | Official club basic season row |

- **Tokyo availability/exposure:** Rowdy Alkins 21.2 PPG, 31:44 MPG, 4.8 APG; Josh Hawkinson 14.5 PPG, 31:31 MPG, 11.2 RPG; Donte Grantham 12.8 PPG, 24:42 MPG; Daiki Tanaka 8.7 PPG, 22:53 MPG; Bryson Williams 9.2 PPG, 21:06 MPG. Their historical 2026–27 participation is confirmed but game-day starts are not. The team has just lost 90–96 at home to Toyama (9 October), giving no single-game rebound penalty or boost.
- **Sendai availability/exposure:** Jarrett Culver 26.8 PPG, 31:02 MPG and 6.8 RPG; Jake Layman 18.8 PPG, 30:45 MPG (3P 44.7% in six games); Sergio El Darwich 12.5 PPG, 27:53 MPG, 6.0 APG; Nathan Booth 12.5 PPG, 28:19 MPG. Recent home win 105–90 vs Mikawa (9 October), but no last-game momentum multiplier. Higher three-point share supports upside and a higher-variance scenario.
- **Schedule:** both clubs played 9 October; at least 10 October was an off-day. Tokyo stayed home; Sendai travels from Sendai to Tokyo. No verified jet lag or fatigue advantage, so directional adjustment **0.0**. Neither game is a back-to-back.
- **No B.PREMIER profile in LEAGUE_PROFILES.** NBA/NBL/EuroLeague/Greek Basket League means and SDs are not copied into this competition. The 2024 and 2025 B League yearly archives are header-only; there are no usable league-specific completed-game SD estimates from those files. SD 21/16 and prior 113.5 are analyst assumptions explicitly NOT calibrated or validated.

#### A4. Distribution and expected score arithmetic
1. **Current-season sample shrinkage (transparent scenario, not fitted).** Six current BP matches each. Assigned current weight 0.60, prior weight 0.40 (pseudo-prior four games), prior 113.5 points per 100 possessions, and prior pace 74.0 per 40 minutes (assumptions, **NOT** measured 2026–27 league averages). This prevents raw six-game season shooting/PPPs becoming entire predictive centre.
2. **Shrunk ratings:** Tokyo offence 0.6×119.6+0.4×113.5 = **117.16**, defence 0.6×108.9+0.4×113.5 = **110.74**; Sendai offence **116.74**, defence **112.48**.
3. **Possession and matchup rates:** pace = 0.6×((75.9+74.9)/2)+0.4×74.0 = **74.84** possessions; opponent-adjusted Tokyo PPP = (117.16+112.48)/200 = **1.1482**; Sendai PPP = (116.74+110.74)/200 = **1.1374**.
4. **Home effect:** +1.50 points to Tokyo−Sendai margin, symmetrically +0.75 Tokyo and −0.75 Sendai, as an **unvalidated scenario assumption** (not a B.PREMIER measured factor). Tokyo 74.84×1.1482+0.75 = **86.6813**; Sendai 74.84×1.1374−0.75 = **84.3730**. Regulation mean **171.0543**, margin **+2.3083**.
5. **Distribution and width:** joint continuous regulation (T, M) normal with SD(total) **21.0**, SD(home margin) **16.0**, corr(T,M)=**0.03**; draw 1,200,000 pairs with RNG seed `20261011576`, convert to non-negative integer team points `round((T±M)/2)`. The width deliberately covers missing starting-fives and early-season 3-point volatility; no B.PREMIER holdout test exists. Conditional equality of rounded regulation team scores enters 5-minute overtime; draw independent Poisson(11.5) scoring for each team per overtime period, repeating until scores differ (rare six-period cap forces one point and is immaterial at this simulation scale). **Model OT incidence 2.44%** (derived from reg-tie kernel, not represented as an official B.PREMIER rate), expected total points add about **0.60**.
6. **Full-game output from the same 1,200,000 simulated endpoints:** Tokyo **86.9782** (SD **13.5482**), Sendai **84.6778** (SD **13.2055**), total **171.6560** (SD **21.4112**), home margin **+2.3004** (SD **16.0448**), final corr(T,M)≈**0.027**. Tokyo wins **55.69%** and Sendai **44.31%**. Both teams cannot draw at terminal sporting endpoint.
7. **Scenario stress:** With current-data weight 0.30 instead of 0.60, the regulation mean total is **169.51**, margin **+1.90**; with 100% unsmoothed six-game rates, regulation total **173.12**, margin **+2.86**. The strongest lower/upper total *families* remain bracketing, but a 90%-ceiling optimal ladder would move the **exact threshold lines 2–4 points**, so the specific ranks depend on the declared prior. If Sendai unexpectedly misses Culver, a −5 to −8 away-team directional perturbation would materially change winning probability and the totals; no such injury is asserted. A confirmed surprise late lineup calls for a dated addendum, not an original-card rewrite.

#### A5. Priced ladder / complementary checks (same seeded distribution)
| Full-game family and line | Primary win | Complement win | Push | Comment |
|---|---:|---:|---:|---|
| Total Over 143.5 / Under 143.5 | 90.65% | 9.35% | 0.0% | Over disallowed by 90% ceiling |
| Total Over 144.5 / Under 144.5 | **89.86%** | 10.14% | 0.0% | **Rank 1** |
| Total Over 145.5 / Under 145.5 | 88.96% | 11.04% | 0.0% | Next ladder rung |
| Total Over 169.5 / Under 169.5 | **53.83%** | **46.17%** | 0.0% | Supplied total |
| Total Over 197.5 / Under 197.5 | 11.26% | 88.74% | 0.0% | Adjacent high threshold |
| Total Over 198.5 / Under 198.5 | 10.44% | **89.56%** | 0.0% | **Rank 2** |
| Total Over 199.5 / Under 199.5 | 9.61% | 90.39% | 0.0% | Under disallowed by 90% ceiling |
| Tokyo -1.0 / Sendai +1.0 | **53.00%** | **44.31%** | **2.69%** | Complementary sporting settlement with common push |
| Tokyo +16.5 / Tokyo -16.5 | 87.95% | 12.05% | 0.0% | Tokyo alternate nearby |
| Tokyo +17.5 / Tokyo -17.5 | **89.15%** | 10.85% | 0.0% | **Rank 3** |
| Tokyo +18.5 / Tokyo -18.5 | 90.27% | 9.73% | 0.0% | First side above ceiling |
| Sendai +20.5 / Sendai -20.5 | 87.19% | 12.81% | 0.0% | Sendai alternate nearby |
| Sendai +21.5 / Sendai -21.5 | **88.45%** | 11.55% | 0.0% | **Rank 4** |
| Sendai +22.5 / Sendai -22.5 | 89.62% | 10.38% | 0.0% | Alternative ladder rung, not issued in the four-row slate |

#### A6. Adjustment and regime ledger
| Name | Parameter | Size | SD units | Basis / applicability |
|---|---|---|---|---|
| New-format / six-game shrink | Possessions, both OFFRTG and DEFRTG | pace 75.4→74.84; regulation centre unsmoothed 173.12→171.05 | −0.098 regulation total SD | Analyst prior, not estimated B.PREMIER league rate |
| Home court prior | Tokyo minus Sendai margin | +1.50, each team ±0.75 | +0.094 margin SD | Assumed; **not** measured from 2026 BP |
| Unconfirmed availability | T width / margin width | SD(total)=21.0, SD(margin)=16.0 vs no eligible BP fitted SD | N/A: no measured comparator | Wide scenario uncertainty; no player-specific directional injury invented |
| Prior-sample regime flag | EARLY_SEASON_SIX_GAMES / BPREMIER_2026_NEW_FORMAT | recorded multiplier 1.000 | 0 | No recommended B.PREMIER multiplier in SELECTION_RULES §6 |

**Unadjusted top two:** with zero home-court prior and 100% season rates, the ranked total families remain an Over below the total centre and an Under above it but their **cutoff lines would be repriced** (not retroactively substituted for issued ranks). No single analyst shift >0.25 SD is asserted. `Adjustment dependence: NONE` per fixed-parameter test, but scenario-prior sensitivity is material to exact threshold choice.

#### A7. Family and process checks
- **Model foundation:** `74.84 possessions × (1.1482+1.1374) PPP = 171.0543` expected regulation total; OT resolution yields 171.6560 full-game. No total centre entered from supplied 169.5. All spreads and winner from the one terminal home-margin distribution.
- **Family checks:** no baseball +1.5, tennis, soccer corners, or halftime/player prop. Full-game integer ±1.0 **PUSH 2.7%** explicitly. Half-point candidate props all no push.
- **Ranking:** Rank 1 89.9% below the 90% ceiling and over 62% floor, but the lead over non-complementary Rank 2 89.6% is 0.3 points: `RANK1_UNSTABLE`; Rank 2 above 58%; top-two both-loss **0** by complementary bracketing, even when source data are wrong. Grade only these two as counted picks under Rule T2. Ranks 3–4 informational.
- **Availability:** official B.LEAGUE team season player participation is dated, **today's starting fives and full injury releases not authenticated**. Applies BK-P2 aggregate lineup-width caveat; no player points/rebounds/first-half prop. No false assertion that Culver/Hawkinson/Alkins are confirmed available.
- **Integrity:** No available calibrated B.PREMIER historical profile, no purported fitting or backtest, no transfer of excluded Austria/BSL profiles or NBA rate. Derived threshold bets might **not be commercially offered**; high nominal `p_card` is partly an artefact of generous handicap/total bands. Sport-only, market-blind; never use supplied line as model feature.

#### A8. Sources and availability receipts (all research pre-tip)
1. B.LEAGUE official match centre `https://www.bleague.jp/game_detail/?ScheduleKey=506457&tab=1`, read 2026-10-11 around 18:49 AEDT: match 506457, 17:05 JST, TOYOTA ARENA TOKYO, records 4–2/3–3, six-game PPG and shooting; the game-score section still unpopulated at retrieval. Official team page and game centre represent **one upstream league lineage**.
2. Tokyo official club stats `https://www.sunrockers.jp/stats/?Year=529`, page update 2026-10-10 21:48 JST, read 18:50–18:53 AEDT: BP pace, OFFRTG/DEFRTG, shot/board/TO rates and named player minute/usage summary; team statistics are not game-day starting-five verification.
3. Sendai B.LEAGUE official club stats `https://www.bleague.jp/club_detail/?TeamID=692&tab=1`, page update 2026-10-10 21:48 JST, read 18:50–18:53 AEDT: six games, pace 74.9, OFFRTG 118.9, DEFRTG 111.8; Culver/Layman/El Darwich/Booth minutes and shooting; independently maintained injury status NOT_RETRIEVED.
4. Tokyo home-game official notice `https://www.sunrockers.jp/lp/game_20261011/`, retrieved 18:49 AEDT: venue and 17:05 JST; opposing player background (older roster); official host corroboration.
5. B.LEAGUE official rule format `https://www.bleague.jp/regulation/`, 2026-27 rules (26-club B.PREMIER, 60-game regular season; on-court foreign-player changes) and official game rules `https://www.bleague.jp/basketball_rule/?tab=5` (four regulation quarters, repeated five-minute overtime); read around 18:52 AEDT.
6. Repo main HEAD `33d0ea0c1c70056db7c7fb0a07dec77a633e573f`; documents in `Rules read` above and `Previous Sports Results/Basketball/B League/2024/2024_games.csv` and `.../2025/2025_games.csv` fetched header only; `.../2026/2026_games.csv` NOT_FOUND. **No prior-season CSV score data imported or reconstructed.**
7. Two latest official club scorecards through 9 October, `https://www.sunrockers.jp/` and `https://www.89ers.jp/`: Tokyo 90–96 Toyama, Sendai 105–90 Mikawa; isolated prior results only, no market prediction-page exposure.

#### A9. Integrity and custody receipt
`SPORTS_ONLY_MARKET_BLIND: PASS` · `EVENT: 506457` · `RESEARCH_TIME: 2026-10-11T18:55:25+11:00` · `SCHEDULED_START: 2026-10-11T19:05:00+11:00` · `ISSUED_BEFORE_SCHEDULED_TIP: YES` · `ACTUAL_TIP: NOT_INDEPENDENTLY_VERIFIED` · `OUTCOME/IN_GAME_OBSERVED: NO` · `STARTING_FIVES: NOT_VERIFIED` · `INJURY_STATUS: INCOMPLETE` · `ARCHIVE_2026_BPREMIER: NOT_AVAILABLE` · `CALIBRATION: NONE` · `RANK1: RANK1_UNSTABLE` · `STATUS: UNCERTIFIED` · `SETTLEMENT: NOT_PERFORMED` · `CANONICAL_IMPORT: PENDING` · `GITHUB_WRITES: NO`.
<!-- END CARD P-576 -->
