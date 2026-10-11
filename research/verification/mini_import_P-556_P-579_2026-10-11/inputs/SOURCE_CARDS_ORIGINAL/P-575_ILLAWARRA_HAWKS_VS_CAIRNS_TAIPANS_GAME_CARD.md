<!-- BEGIN CARD P-575 -->
## Card · P-575 · BASKETBALL / AUSTRALIA NBL · Cairns Taipans @ Illawarra Hawks · 2026-10-11

- **Working ID:** `P-575 — LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT`
- **Event key:** `NBL:2026-27:36fb1b72-58ad-11f1-a2a4-7da015763581:2026-10-11`
- **Native event ID:** `36fb1b72-58ad-11f1-a2a4-7da015763581` (official NBL schedule game-centre UUID)
- **Sport:** `Basketball`
- **League:** `Australian National Basketball League, NBL27, regular season, Round 4`
- **Tracking alias:** `LOCAL-20261011-P-575-NBL-CNS-ILL`
- **Analysis status:** `UNCALIBRATED_ANALYST_SCENARIO`
- **Timing state:** `LATE_START_UNVERIFIED` — full card finalised after 17:00 AEDT scheduled tip, with only published pregame information; NOT a verified prospective forecast.
- **Research completed:** `2026-10-11T17:05:11+11:00` (source intake near 16:59 AEDT; calculation and card completion followed scheduled tip; exact actual first play NOT_VERIFIED).
- **Scheduled start:** `2026-10-11T17:00:00+11:00` (Sunday, 11 October 2026, confirmed by NBL and Hawks; venue WIN Entertainment Centre, Wollongong).
- **Endpoint:** `Full NBL game including all overtime periods; four 10-minute regulation quarters; no terminal draw. Operator terms for alternative period/action markets NOT_VERIFIED; standard full-game final-score research endpoint applied.`
- **Distribution object:** `NBL27_PACE_PPP_GAUSSIAN_OT_v1 — regulation pace=81.315 possessions/side; historical league PPP0=1.14278; Illawarra opponent-adjusted PPP=1.16654, Cairns=1.17543; regulation points Illawarra=95.707 Cairns=94.730, total=190.438; NBL home margin +1.70 points (+0.85H/-0.85C); regulation total Normal(μ=190.438, SD=19.60); 95.3% no-OT margin Normal(μ=+1.00, SD=16.60) and 4.7% tied-regulation branch adding 22 total points with OT margin ±4 (home 53%); team scores=(T±M)/2; continuous half-line proxy.`
- **Expected score:** `points, full game including OT; analytic unconditional mixture moments — Illawarra Hawks 96.22 (SD 12.92) · Cairns Taipans 95.25 (SD 12.95) · total 191.47 (SD 20.15) · margin Illawarra − Cairns +0.96 (SD 16.23); OT share 4.7% adds 1.034 expected full-game points, split 0.517 each before OT winner differential.`
- **Regime flags:** `NONE` — six 2026–27 games for each team, explicit 35% regular-season league PPP shrinkage used; the NBL-specific early-season benchmark is an uncertainty warning, not a signed league multiplier in SELECTION_RULES §6.
- **Retirement rule:** `N/A` (basketball)
- **Listed-pitcher rule:** `N/A` (basketball)
- **Abandonment rule:** `FRAMEWORK_DEFAULT: only an official completed/resumed game final can settle; if postponed, abandoned or cancelled without valid final, hold as PENDING_EVENT or VOID per sporting result; operator action terms unverified.`
- **Settlement fields:** `NBL official match UUID 36fb1b72-58ad-11f1-a2a4-7da015763581: game state FINAL, full-time Illawarra/Cairns points, all quarters and overtime, confirmed starters and didNotPlay if supplied, provider schedule.nbl.com.au match API / league game centre; independent scoreboard corroboration as available.`
- **Capture due:** `2026-10-12T05:00:00+11:00` (12 hours after scheduled tip).
- **Rules read:** `CURRENT_STATE, METHOD MDS-2026.10.09-v9.0, CURRENT_RULES §§1–10, SELECTION_RULES §§1–6, RULES_BASKETBALL §0 & §§3–5,7–9, PROBABILITY_TOOLKIT §§1,1.2,1.3, BASE_RATES_REGISTER §§3,7.1 & regime table, LEAGUE_PROFILES Basketball/NBL 2022–24 row, SOURCES §3.2 NBL, ARCHIVE_USE_GUIDE §§1–6, CARD_AND_LOG_TEMPLATES §§2,3,3a,7; main HEAD 33d0ea0c1c70056db7c7fb0a07dec77a633e573f.`
- **Archive check:** `ARCHIVE_PARTIAL current-season: opened Previous Sports Results/Basketball/NBL/2023/2023_games.csv, /2024/2024_games.csv, /2025/2025_games.csv (headers and first records); 2026 NBL yearly coverage not independently captured; derived R1/R8 from LEAGUE_PROFILES NBL regular-season n=425 for 2022–2024: home mean 91.41, away mean 89.72, total mean 181.13, SD_total=19.53, SD_margin=15.28, score correlation=0.241, OT=4.7%. Separate RealGM 2025–26 pace reference 79.25 is descriptive, not a retrospective test; 2026–27 current 6-game averages from NBL official 11 Oct and FanCrew feed. No future/current game data or postgame prose used.`
- **Evidence quotes:** `NBL official pregame article @ 2026-10-11 before scheduled start — "Sunday, October 11, 5pm AEDT"; same source — "Todd Blanchfield - Hand - TBC"; "Mason Peatling - Foot - Season"; "Sunday Dech - Hamstring - Round 8"; "Jaylin Galloway - Shoulder - Round 6"; Illawarra official preview published 2026-10-09 — "Hawks: 1-5 (1-1 at home), but scoring 99.7 points a game"; same preview — "Cairns score a league-low 88.5 points a game"; NBL official preview describes Cairns' Jaylon Brown recent 20/25 points. Official starters: NOT_VERIFIED.`

### Decision block

**Distribution:** `NBL27_PACE_PPP_GAUSSIAN_OT_v1`. Regulation pace 81.31 possessions × shrunk opponent-adjusted efficiencies Illawarra 1.167/Cairns 1.175, plus home-margin +1.70. Regulation total 190.44 (SD19.60), OT +22 points in 4.7% tied branch: full-game total 191.47 (SD20.15), home margin +0.96 (SD16.23). All four ranked rows arise from this one Gaussian/OT mixture and are uncalibrated, not odds-based.

| Rank | Role | Tag | Proposition | p_card | Probability status | Evidence | Failure route |
|---|---|---|---|---|---|---|---|
| 1 | PICK | ANALYST_DERIVED (replaces supplied total Over 195.5 line) | Combined total Over 166.5 points — full game incl. OT | 89.4% | FROM_DISTRIBUTION:NBL27_PACE_PPP_GAUSSIAN_OT_v1 | No last-game outcome used; possession model 81.32, regulation 190.44-point centre and NBL width | Severe conversion and/or pace collapse; 166 or fewer points |
| 2 | PICK | ANALYST_DERIVED (replaces supplied total Under 191.5 line) | Combined total Under 216.5 points — full game incl. OT | 89.3% | FROM_DISTRIBUTION:NBL27_PACE_PPP_GAUSSIAN_OT_v1 | NBL total-width prior plus OT branch, not recent two-game totals | 217+ points via high eFG%, free throws, added possessions or OT |
| 3 | INFORMATIONAL | ANALYST_DERIVED (replaces supplied Hawks -1.5 line) | Illawarra Hawks +18.5 points — full game incl. OT | 88.6% | FROM_DISTRIBUTION:NBL27_PACE_PPP_GAUSSIAN_OT_v1 | Home margin +0.96, wide 16.2-point margin SD; NBL population prior | Cairns wins by 19+ after perimeter, turnover and/or rebounding divergence |
| 4 | INFORMATIONAL | ANALYST_DERIVED (replaces supplied Taipans +1.5 line) | Cairns Taipans +18.5 points — full game incl. OT | 86.1% | FROM_DISTRIBUTION:NBL27_PACE_PPP_GAUSSIAN_OT_v1 | Cairns defence concedes 94.2 PPG; Illawarra strong scoring, but wide margin tail | Illawarra wins by 19+ following repeated Cairns defensive breakdowns |

**P(Rank 1 and Rank 2 both lose):** `0.0% by construction`: Over 166.5 loses at ≤166; Under 216.5 loses at ≥217. The losses cannot coexist, and this guarantee is threshold geometry, NOT evidence of calibrated predictive power.
**Rank 1 − Rank 2 gap:** `0.1 percentage points` (89.4% − 89.3%).
**Rank-1 gate:** `RANK1_UNSTABLE` — p_card 89.4%; best non-complementary alternative Under 216.5 89.3%; margin 0.1 points (below 4.0). Late timing and unconfirmed active fives further prohibit certification.
**Adjustment dependence:** `NONE` — the 1.70-point home-margin change is 0.105 margin SD; fixed shrinkage toward a population league prior is explicitly modelled, not an unreceipted fitted adjustment. Top two remain broad bracketing totals in a ±3.25-point total-centre sensitivity.
**Supplied rows not selected:** `Illawarra Hawks −1.5: 49.0%; Cairns Taipans +1.5: 51.0%; combined total Over 195.5: 41.7%; combined total Under 191.5: 50.4%`. All include OT. Hawks −1.5/Cairns +1.5 are complements (total 100%); the two supplied totals are NOT complements because their thresholds differ by 4 points.
**Potential winner:** `Illawarra Hawks — 52.4%` (full game including OT; Cairns 47.6%). Near-even game, not a strong winner call.

### Appendix

#### A1. Identity, timing and state
- Official NBL game-centre UUID `36fb1b72-58ad-11f1-a2a4-7da015763581`, Wollongong, Sunday 11 October at 17:00 AEDT, Illawarra at home. Round 4 of NBL27 regular season, four 10-minute quarters and five-minute extra periods until a winner.
- The source intake near 16:59 was pre-tip in scheduled clock terms, but the full analysis was completed after the advertised start; actual NBL first `jumpBall` time was not verified. Therefore `LATE_START_UNVERIFIED`, not `PREGAME`. No in-game score, box score, market odds or post-tip change was consumed. This card is time-contaminated for performance eligibility even if it proves right.
- Formal starting fives NOT_VERIFIED. The league's "Expected depth chart" describes a potential rotation, not confirmed participation. Watch any late updates to Shaun Bruce and other questionable minutes without assuming them unavailable unless the league declares them so.

#### A2. Supplied contracts and endpoint
| Supplied row (reference only) | Full game including OT | Model win | Model loss | Interpretation |
|---|---|---:|---:|---|
| Hawks −1.5 | Home final margin ≥2 | 49.0% | 51.0% | Near-even favourite spread |
| Taipans +1.5 | Cairns wins or loses by exactly one | 51.0% | 49.0% | Complements Hawks −1.5 |
| Combined Over 195.5 points | 196+ total | 41.7% | 58.3% | Above model total mean |
| Combined Under 191.5 points | ≤191 total | 50.4% | 49.6% | Just below model mean; 192–195 causes BOTH supplied total propositions to lose |

#### A3. Current evidence, player minutes, matchup, and uncertainty
1. **League/club identity and availability.** NBL game-day article 11 Oct lists expected Illawarra rotation Milton Doyle, William Hickey, Kyle Adnam, Tyler Harvey, Wani Swaka Lo Buluk, Daniel Grida, Kelan Martin, Sam Froling, Thon Maker. Cairns projected unit Jaylon Brown, Reyne Smith, Malique Lewis, Jack McVeigh, Keanu Pinder, plus Kyrin Galloway, Jonah Bolden, Shaun Bruce. Unconfirmed official fives and exact bench availability, so do not falsely assert player-specific minute ceilings.
2. **Official absences.** Illawarra: Peatling season (foot; limited to two appearances beforehand), Blanchfield hand TBC. Cairns: Sunday Dech hamstring (round 8 return), Jaylin Galloway shoulder (round 6 return). Offensive/defensive redistribution included only through the current team PPP inputs; no second unsupported injury-point penalty applied.
3. **Scoring and efficiency (6 games each, as publicly dated pregame):** Illawarra 99.7 PPG for / 107.7 against, 82.5 pace, offensive PPP 1.208, defensive conceded PPP 1.305, eFG 56.5%, 3P 36.3%, TOV rate 12.5%, ORB 31.6%, FTr .214. Cairns 88.5 PPG for / 94.2 against, pace 81.9, offence 1.081, defence 1.150, eFG 51.8%, 3P 32.3%, TOV 13.4%, ORB 21.6%, FTr .207. The large current defensive gap is shrunk in A4; 6 games do not measure stable defensive quality.
4. **Usage and minutes.** Hawks Martin 18.3 PPG, Milton Doyle 13.7, Froling 13.3, Hickey 13.0; Harvey 11.5 (official NBL pregame). Cairns Jack McVeigh 16.0 PPG and approximately 31.5 minutes, Pinder 15.2 PPG, Jaylon Brown 14.8, Malique Lewis 11.2. Their exact expected minutes and usage from the posted final active list are NOT_VERIFIED; player props are excluded.
5. **Rest and travel.** Illawarra played home on Friday 9 Oct (lost 112–122 to Tasmania), then home Sunday; Cairns played Thursday 8 Oct (won 97–91 against Brisbane), then travelled to Wollongong. Hawks 2-calendar-day / Cairns 3-calendar-day gap, no back-to-back; no unsupported fatigue penalty, travel is uncertainty only. Opponent-adjusted six-game schedule strength is not fitted.
6. **Mechanisms:** Hawks allow 1.32 PPP per official league article, bottom-ranked defensive efficiency; can drive Cairns higher than its season-low raw 88.5. Conversely Cairns are bottom of the league in offence and offensive boards (6.8 ORB/G), create comparatively few free throws, but lead steals (7.8/G); Hawks limit giveaways to about 10.3 per game. High three-point dependence widens tails. Bench scoring ~39.2 Hawks PPG and 18.7 fast-break PPG from official club preview; do not double-count these as incremental possessions above season PPP.
7. **Historically disparate baselines:** NBL archival 2022–2024 mean 181.13 versus six-game current gross combined scoring >190, so model explicitly shrinks pace/PPP; no borrowed NBA profile, no external forecasts or prices.

#### A4. Reproducible distribution, moments and sensitivity
**Pace and efficiency:** NBL last-season 2025–26 RealGM league median/mean pace context ~79.25 possessions from ten team values; older NBL archival population μ total 181.13. Thus league baseline PPP = 181.13/(2×79.25) = 1.14278, a cross-season approximation with explicit era mismatch. Match observed pace = (82.5 + 81.9)/2 = 82.20, shrunk 70% toward observed, 30% to prior 79.25: `pace=.70×82.20+.30×79.25=81.315`. This shrinkage weight is **analyst judgement**, not a fitted optimum.

**Opponent adjustments and 6-game shrinkage:** raw Illawarra side `(99.7/82.5 + 94.2/81.9)/2=1.17933` PPP; raw Cairns `(88.5/81.9 + 107.7/82.5)/2=1.19302` PPP; 65% current matchup blend and 35% prior league PPP yields Illawarra 1.16654, Cairns 1.17543. Pre-game site PPG both role and defence are not independent observations; averaging mitigates (does not remove) that dependence.

**Regulation score:** Illawarra `81.315×1.16654+0.85=95.707`; Cairns `81.315×1.17543−0.85=94.730`; regulation total `190.438`. Total home-margin prior +1.70 uses archival home/away 91.41−89.72=1.69, rounded as transparent +1.70 assumption. This preserves total centre, rather than adding 1.70 only to the total.

**Total/OT object:** T_reg ~ Normal(190.438, 19.60²) NBL-specific total SD 19.53 widened to 19.60. OT branch weight 0.047 from NBL population; in OT the regulation score is tied and full total gains 22 points, representing approx five-minute extra period. Thus `E[T]=190.438+.047×22=191.472`, `Var(T)=19.60²+.047×.953×22²=405.839`, `SD(T)=20.145`. The 22 OT-point increment is an approximate analyst assumption, not an observed NBL27 conditional mean; additional overtime periods are width-only, not separately enumerated.

**Margin/teams:** no-OT margin Ill−Cairns Normal(+1.0, 16.6²) with weight .953; conditional OT winner creates a +4 margin with probability .53 or −4 with .47 and weight .047. `E[M]=.953×1.0+.047×(.53×4−.47×4)=0.964`. `SD(M)=sqrt(E[conditional SD² + conditional mean²]−E[M]²)=16.229`. Home win `.953×Φ(1/16.6)+.047×.53=52.4%`. The joint object defines T and M with a 0.047 common OT indicator, and team scores are H=(T+M)/2, C=(T−M)/2. `Cov(T,M)=.047×.953×22×(.24−1)=-0.749`, `SD(H)=sqrt((VarT+VarM+2Cov)/4)=12.920`, `SD(C)=sqrt((VarT+VarM−2Cov)/4)=12.949`. Continuous score approximations are used at half-point lines; exact integer tie handling is assigned to the overtime branch rather than independently rounding all non-OT normal draws. Correlation of team scores is scenario-derived, not the archival 0.241 exactly.

**Selection math:** `P(Under L)=.953Φ((L−190.438)/19.60)+.047Φ((L−212.438)/19.60)`, Over is its complement. A half-point line avoids pushes. Rank 1 `89.4%` is highest eligible total within the 90% ceiling at the chosen half-line ladder (Over 165.5 would be 90.3%, ineligible); Rank 2 `89.3%` is the nearest high-probability opposing bracket below ceiling (Under 217.5 would be 90.2%, ineligible). This candidate-grid selection is threshold-extreme by design and has no price/value claim.

**Sensitivity (weak defence/pace assumption):** shift regulation total −3.25 while preserving total SD/OT. Under 216.5 rises to 91.9%, above the ceiling; Over 166.5 falls to 86.1% and new eligible top-two thresholds become Under 213.5 ≈89.5% and Over 166.5 ≈86.1% (still a bracketing pair). Shift total +3.25: Over 166.5 reaches ≈92.1% (ineligible); Over 169.5 reaches ≈89.6%, Under 216.5 ≈86.1%; new top-two thresholds also change. Consequently the **chosen line values depend on uncertain centre assumptions** even though the bracketing logic remains.

#### A5. Priced ladder and complement check
| Family / exact full-game line | Over / Hawks side | Under / Cairns side | Sum check |
|---|---:|---:|---|
| Total 165.5 | 90.3% | 9.7% | 100.0%, Over ineligible >90% |
| Total 166.5 | 89.4% | 10.6% | 100.0% |
| Total 167.5 | 88.4% | 11.6% | 100.0% |
| Total 191.5 | 49.6% | 50.4% | 100.0% |
| Total 195.5 | 41.7% | 58.3% | 100.0% |
| Total 215.5 | 11.6% | 88.4% | 100.0% |
| Total 216.5 | 10.7% | 89.3% | 100.0% |
| Total 217.5 | 9.8% | 90.2% | 100.0%, Under ineligible >90% |
| Illawarra / Cairns ±1.5 (Hawks −1.5/Cairns +1.5) | 49.0% | 51.0% | 100.0% |
| Hawks +18.5 / Hawks −18.5 | 88.6% | 11.4% | 100.0% |
| Cairns +18.5 / Cairns −18.5 | 86.1% | 13.9% | 100.0% |

**OT geometry and rank-two dependency:** the total brackets span 167 through 216 inclusive (after integer score reporting), so `P(both lose)=0`. The two sides of the *same* supplied spread are complementary; no quarter, player, or period prop is issued.

#### A6. Adjustments and regime
| Name | Target | Size | SD units | Prior basis |
|---|---|---|---|---|
| Home-court margin prior | Illawarra − Cairns margin | +1.70, symmetrically ±0.85 points | +0.105 margin SD | archive_estimate (NBL home−away mean 1.69) |
| Early-season pace shrinkage | pace | −0.885 possessions vs raw 82.20 | −0.044 total SD if PPP ~2.34 | analyst_judgement, league prior |
| PPP sample shrinkage | offence/defence interaction | raw matchup 195.0 to shrunk ~190.44 regulation points (partially offset by reduced pace) | <0.25 total SD | analyst_judgement, paired team PPP |
| Missing active fives | rotation uncertainty | no directional point shift, total SD 19.53→19.60; margin 15.28→16.2 | small width only | analyst_judgement |

**Regime check:** no NBL-specific `EARLY_SEASON` signed multiplier in SELECTION_RULES §6; n=6 completed games each, so an explicit sample-weight shrink rather than borrowing the NBA's .988 factor. The overall top two are bracketing totals in both unshrunk (reg centre ~195) and shrunk scenarios, though threshold lines change. No >0.25 SD single analyst adjustment is asserted as fitted.

#### A7. Family checks and selection gates
1. Pace×efficiency is printed in A4 with every term, and includes the opposing defensive rate. The total 191.47 is *computed*, not typed from the 191.5/195.5 supplied contracts.
2. Hist. NBL regular season (2022–24) total SD 19.53 and margin SD 15.28. Scenario full-game 20.15 / 16.2 respectively, not narrowed; correlation is implied by the same T/M object. No NBA standards used.
3. NBL OT ~4.7% branch explicit and included in all four picks and supplied-contract checks. No regulation-only proposition issued.
4. Injuries and usage: four field-owner listed absences are accounted through team current sample without inventing a second penalty; official starters/participation not verified. All player/period props excluded.
5. Rank 1 floor≥62: YES; 4-point separation: NO (0.1); label RANK1_UNSTABLE. Rank 2≥58 YES; joint failure=0.0% by construction. Four `p_card` values <=90%; Rank3/4 informational.
6. The four ranked propositions use threshold-extreme lines, not necessarily contracts offered by a sportsbook. Threshold diversification and overlapping win regions explain apparently high percentages; this is not out-of-sample skill.
7. No externally fitted league matchup model, no calibrated predictions. PREGAME certification fails due to post-scheduled issuance, and process gate BK-P2 incomplete because active fives not verified.

#### A8. Sources (field, original publication, read at research)
1. NBL official game-day article `https://league.nbl.com.au/news/how-to-watch-talking-points-illawarra-hawks-v-cairns-taipans-nbl27`, published 2026-10-11; fixture, roster depth chart, four dated injuries, reported Hawks defensive rating 132.2, Jaylon Brown's 20/25-point performances. Source intake around 16:59 AEDT, before listed start; content is league pregame article, NOT live box.
2. Hawks official `https://www.hawks.com.au/news/game-preview-hawks-vs-taipans-rd4-nbl27`, published 2026-10-09; Hawks 1-5, Cairns 3-3, 99.7/88.5 PPG, Friday Tasmania 112–122, Harvey 200-game milestone, Jack McVeigh 16 PPG, team turnover/bench/fast break. Intake around 16:59 AEDT.
3. Cairns official `https://www.taipans.com/news/game-preview-hawks-v-taipans-nbl27-round-4`, published 2026-10-10; travel/rest and back-to-back wins context. Intake around 16:59 AEDT.
4. Official NBL match centre `https://schedule.nbl.com.au/match?league=NBL&match=36fb1b72-58ad-11f1-a2a4-7da015763581&year=2026`; official native game ID and score source for future settlement; **NO scoreboard/results queried as forecast inputs**.
5. FanCrew NBL27 team stats (derived from NBL public feeds, not an independent official injury lineage) `https://www.fancrew.com.au/stats/teams` and `https://fancrew.com.au/games/illawarra-hawks-v-cairns-taipans-men-11-10-2026`; six-game pace and scoring, eFG/TOV/ORB, PPG, key player rates, cutoff original near 16:59 AEDT; secondary field calculations rather than game-result claims. Does not supply an externally valid prediction.
6. Official Taipans injury page `https://www.taipans.com/pages/injuries`: Jaylin Galloway and Sunday Dech. Official NBL injury article 2026-10-09 `https://league.nbl.com.au/news/season-over-for-two-time-champion-mason-peatling`: surgery and Peatling out remainder of season. Both before game.
7. `https://basketball.realgm.com/international/league/5/Australian-NBL/team-stats/2026/Advanced_Stats`: **2025–26** ten-team pace observations 79.5,82.2,78.2,79.5,76.7,76.2,80.2,82.4,77.5,80.1; mean 79.25 as population-scale prior, not current form and not a 2026–27 roster predictor.
8. GitHub `danisgreat/Sports-Research` `main` @ `33d0ea0c1c70056db7c7fb0a07dec77a633e573f`. Read current state, selection/timing rules, basketball specifics, toolkit §§1,1.2,1.3, scoring benchmarks from LEAGUE_PROFILES NBL, SOURCES §3.2, ARCHIVE_USE_GUIDE, CARD_AND_LOG_TEMPLATES; GitHub READ ONLY. 2023/2024/2025 NBL CSV headers fetched from repository.

#### A9. Integrity receipt
`HEAD: 33d0ea0c1c70056db7c7fb0a07dec77a633e573f` · `NBL_EVENT_UUID: 36fb1b72-58ad-11f1-a2a4-7da015763581` · `PREGAME_SOURCES_ONLY: YES` · `ISSUED_BEFORE_SCHEDULED_TIP: NO` · `TIMING: LATE_START_UNVERIFIED` · `OBSERVED_IN_GAME_OUTCOME_USED: NO` · `MARKET_ODDS_INPUT: NONE` · `FOUR_RANKS: YES` · `PROBABILITY_CALIBRATION: NONE` · `STARTING_FIVES: NOT_VERIFIED` · `ROTATION_INJURY_COVERAGE: PARTIAL` · `RANK1: RANK1_UNSTABLE` · `PERFORMANCE_ELIGIBILITY: NOT_CERTIFIED` · `SETTLEMENT: NOT_PERFORMED` · `CANONICAL_IMPORT: PENDING` · `GITHUB_WRITES: NO`.
<!-- END CARD P-575 -->
