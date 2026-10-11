<!-- BEGIN CARD P-578 -->
## Card · P-578 · BASKETBALL / NBA Preseason · Dallas Mavericks @ Houston Rockets · 2026-10-11

- **Working ID:** `P-578 — LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT`
- **Event key:** `NBA_PRESEASON:2026-27:0012600016:2026-10-11`
- **Native event ID:** `NBA 0012600016` (NBA.com exact-game official page)
- **Sport:** `Basketball`
- **League:** `NBA Preseason (NBA China Games 2026)`
- **Tracking alias:** `LOCAL-20261011-P-578-NBAPRE-DAL-HOU`
- **Analysis status:** `UNCALIBRATED_ANALYST_SCENARIO`
- **Timing state:** `LATE_START_UNVERIFIED`
- **Research completed:** `2026-10-11T21:01:22+11:00`
- **Scheduled start:** `2026-10-11T21:00:00+11:00` (2026-10-11 18:00 Macao UTC+8, 06:00 US EDT; true first-jump time unverified)
- **Endpoint:** `Full official preseason game: four 12-minute quarters, overtime periods of 5 minutes if tied; all team points incl. any OT; NBA-declared terminal final. Neutral site Venetian Arena Macao; no Houston geographic home-court advantage. Operator-specific wager action/void terms unverified.`
- **Distribution object:** `basketball_nba_pre_pace_eff_joint_ot_v1` — seed 20261011578; 1,800,000 discretised joint Normal game draws; 101.195 possessions; regulation Dallas 112.6588 pts, Houston 114.4999 pts; regulation SD(total,margin)=(23.2,18.8), corr=.04; 4.7% OT branch +mean25.2 pts; full-game total 228.37, margin Houston−Dallas +1.78`
- **Expected score:** `points, full game including all overtime; SDs from 1,800,000 terminal-score draws — Dallas Mavericks 113.29 (SD 14.95) · Houston Rockets 115.08 (SD 15.43) · total 228.37 (SD 23.85) · margin Houston − Dallas +1.78 (SD 18.81)`
- **Regime flags:** `NBA_PRESEASON_NO_VALIDATED_PROFILE, PRESEASON_ROSTER_MINUTES_UNCERTAIN, SAME_OPPONENT_REMATCH, NEUTRAL_SITE, KD_REST_SECONDARY_REPORT, IRVING_RETURN_PROBABLE_SECONDARY_REPORT, ACTUAL_TIP_UNVERIFIED`
- **Retirement rule:** `N/A`
- **Listed-pitcher rule:** `N/A`
- **Abandonment rule:** `FRAMEWORK_DEFAULT: cancel/no official final => VOID for sporting-score propositions; operator-specific action terms UNKNOWN_DEFINITION`
- **Settlement fields:** `official full-game final team scores, regulation score, OT flag, four quarters, official five starters, DNPs, withdrawals, tip time (provider: NBA official game 0012600016 / official NBA Game Book; independent structured fallback ESPN or RealGM)`
- **Capture due:** `2026-10-12T21:00:00+11:00` (within 36 h of scheduled tip)
- **Rules read:** `CURRENT_STATE; METHOD; CURRENT_RULES; RULES_BASKETBALL §§0,2–4,8–10; SELECTION_RULES §§1–6; PROBABILITY_TOOLKIT §1 §§1.2–1.3, §§4–5,9; BASE_RATES_REGISTER §§3,7.1; LEAGUE_PROFILES Basketball/NBA; SOURCES §§1,2.1,3.2; ARCHIVE_USE_GUIDE §§1–5; CARD_AND_LOG_TEMPLATES §§3,3a,4,7; research/prompts/1_GAME_CARD; NBA official event 0012600016, read 2026-10-11T21:01:22+11:00; main HEAD 33d0ea0c1c70056db7c7fb0a07dec77a633e573f (read-only)`
- **Archive check:** `ARCHIVE_PARTIAL: Previous Sports Results/Basketball/NBA/2025/2025_games.csv opened, first 2025-10-21 regular-season row and documented columns Game Type, Home Score, Away Score, Total Points, Overtime; current NBA 2026/2026_games.csv NOT_FOUND; full season file not ingested, zero own-season 2026 game rows used. LEAGUE_PROFILES NBA 2023–2025 (n=3692, mean total 229.08, total SD 20.04, margin SD 15.98, score corr .223) and BASE_RATES NBA 2025–26 (total 230.7, OT 4.4%, +25.2 OT pts) are historical priors only. First Macao game's official/structured result 135–117 used for a heavily shrunk possession-rate input; no outcome from this second fixture used.`
- **Evidence quotes:** `NBA.com official event (fixture/date; no lineup): "Sunday, October 11th, 2026 6:00 AM ET"; NBA.com Oct 10 news: "Kyrie ... is expected to make his preseason debut"; Yahoo/Roundtable Oct 11: "Out: Kevin Durant (Rest)" and "Probable: Kyrie Irving (Rest/Injury Management)"; secondary reports only, not official starting-five validation; web read 2026-10-11T21:01:22+11:00`

### Decision block

**Distribution:** `basketball_nba_pre_pace_eff_joint_ot_v1` — 101.195 regulation possessions × opponent-adjusted, roster-weighted PPP (Dallas 1.1133, Houston 1.1315); regulation Normal total 227.16, margin Houston +1.84, SD (23.2,18.8) and total/margin correlation +0.04; 4.7% close-game OT branch, ~25.2 points per OT. 1,800,000 deterministic full-game draws priced all rows.

| Rank | Role | Tag | Proposition | p_card | Probability status | Evidence | Failure route |
|---|---|---|---|---|---|---|---|
| 1 | PICK | ANALYST_DERIVED | Total points **Under 258.5**, NBA preseason full game incl. OT | 89.7% | FROM_DISTRIBUTION:basketball_nba_pre_pace_eff_joint_ot_v1 | Preseason-adjusted pace×PPP centre 228.37; wide NBA/rotation uncertainty | 259+ points from fast tempo, hot shooting, deep bench or overtime |
| 2 | PICK | ANALYST_DERIVED | Total points **Over 198.5**, NBA preseason full game incl. OT | 89.6% | FROM_DISTRIBUTION:basketball_nba_pre_pace_eff_joint_ot_v1 | Same total distribution, no new scoring estimate | 198 or fewer from rested scorers, slow pace, poor shooting |
| 3 | INFORMATIONAL | ANALYST_DERIVED | Houston Rockets **+21.5**, NBA preseason full game incl. OT | 89.3% | FROM_DISTRIBUTION:basketball_nba_pre_pace_eff_joint_ot_v1 | Houston+Dallas joint game margin, neutral-site scenario | Dallas wins by 22+ |
| 4 | INFORMATIONAL | ANALYST_DERIVED | Dallas Mavericks **+24.5**, NBA preseason full game incl. OT | 88.7% | FROM_DISTRIBUTION:basketball_nba_pre_pace_eff_joint_ot_v1 | Same margin distribution and preseason roster width | Houston wins by 25+ |

**P(Rank 1 and Rank 2 both lose):** 0.0% by construction: T≥259 and T≤198 cannot coincide (completed games only, excluding cancellation/void).
**Rank 1 − Rank 2 gap:** 0.1 percentage points (unrounded 0.102).
**Rank-1 gate:** RANK1_UNSTABLE — p_card 89.7%; best non-complementary alternative 89.6%; margin 0.1 points (minimum required 4.0).
**Adjustment dependence:** ADJUSTMENT_DEPENDENT — Houston rotation/Durant adjustments total −4.9 points (~0.32 team-score SD); disabling all analyst roster adjustments materially changes the top-two thresholds (A6).
**Supplied rows not selected:** Dallas Mavericks +1.5 48.0%; Houston Rockets −1.5 52.0%; total Over 230.5 46.1%; total Under 230.5 53.9% (same full-game distribution; the home/away lines have no push at 1.5).
**Potential winner:** Houston Rockets — 53.7% (full game including applicable overtime; neutral-site team listed home).

### Appendix

#### A1. Identity, timing and state
- NBA official game `0012600016`; second of two NBA China Games at Venetian Arena, Macao, 11 October 2026. Both scheduled 6 AM ET / 6 PM Macao / 9 PM AEDT. "Home" in schedule is an administrative label, not physical home court.
- Research timestamp 2026-10-11T21:01:22+11:00; `Timing state=LATE_START_UNVERIFIED`. Actual jump-ball independently NOT_VERIFIED. Research excludes live second-game score, in-game statistics and postgame facts. If after 21:00 AEDT, no claim of a certified pregame forecast. ESPN live feeds can show late statuses; they were not used as game outcome inputs.
- `PREGAME` is a documentary timing code only, not proof of actual first tip or performance eligibility. No betting provider has specified settlement/action semantics; sports-score probabilities are conditional on an official completed game.

#### A2. Supplied contracts — reference only
| Contract | Full-game estimated result | Probability |
|---|---|---:|
| Mavericks +1.5 | DAL final +1.5 exceeds HOU final | 48.0% |
| Rockets −1.5 | HOU final exceeds DAL by 2+ | 52.0% |
| Over 230.5 | Total ≥231 | 46.1% |
| Under 230.5 | Total ≤230 | 53.9% |

#### A3. Evidence summary
- **Fixture**: NBA official 0012600016 and Dallas official press release; second Macao exhibition. The older references to Friday's matchup are not this event. First game's 135–117 final is from Oct 9 only, never a result for Oct 11.
- **Preseason first game**: RealGM Oct 9 structured team box: DAL 94 FGA / 13 ORB / 19 TO / 17 FTA, HOU 86 FGA / 16 ORB / 21 TO / 32 FTA; estimate 107.48 and 105.08 possessions respectively (average 106.28). HOU 18/36 3P (50.0%), DAL 18/51 3P (35.3%); HOU exceptional shooting is not assumed repeatable. Dallas coach reports variable rotations in preseason.
- **Availability**: Oct 11 dated Roundtable/Yahoo injury story reports Durant OUT for rest; Irving PROBABLE after ACL recovery; DAL Lively/Aldama/Caleb Martin/PJ Washington/Sasser questionable. NBA official Oct 10 news expects Irving's Sunday preseason return. Reliable official starting-five, exact minutes limits, active rosters were NOT_OBTAINED. Contradictory general preview projected Durant in lineup: older projection not treated as actual.
- **History**: 2025–26 Dallas 114.1 PF / 119.6 PA and Houston 115.2 PF / 110.0 PA per preseason matchup profile; historical rosters differ. Prior NBA typical 99.5 poss/48 min is an explicit analyst baseline assumption (not a dated league stat); 2025–26 total mean 230.7 and profile 2023–25 mean 229.08. NBA default dispersion is used only because this is NBA; preseason-specific dispersion not validated.
- **Rotation**: Kyrie Irving long ACL absence (Reuters Oct 8); VanVleet returned for 24 min in Oct 9 game; Houston's Sengun recorded a triple-double in 22 min, reflecting preseason usage. No accurate confirmed Oct 11 minutes for rotation players, so no player props or starter-dependent Rank 1; no official minutes values invented.
- **Rest/travel**: both teams at Macao venue Oct 9 and Oct 11, roughly 2 days rest each; no long journey between matches; neutral-site court means no Houston geographic edge. Prior 2025–26 NBA home advantage not credited.

#### A4. Event distribution, arithmetic, endpoints and uncertainty
1. Regulation possession estimate: DAL 94−13+19+0.44×17 = **107.48**; HOU 86−16+21+0.44×32=**105.08**; same-game mean **106.28**. Shrink 75% to a tentative NBA baseline 99.5 possessions, 25% to that one game's 106.28: **101.195** expected possessions. This 99.5 assumption is model judgement; the numerical 25% weight is not calibrated.
2. Opponent-adjusted historical team scoring budgets (no home-court add): Dallas (114.1 scoring + Houston 110.0 conceded)/2 = **112.05** per 99.5 possessions, so 101.195×112.05/99.5 = **113.96**. Houston (115.2 scored + Dallas 119.6 conceded)/2 = **117.40** per 99.5, so 101.195×117.40/99.5=**119.40**. Historical players/defence are only priors, NOT known current lineups.
3. Availability/rotation prior weights (analyst judgements, not fitted): Dallas −2.0 points preseason minutes churn +0.7 Irving limited return = **−1.3** => **112.6588** regulation points (PPP 1.1133). Houston −2.0 preseason minutes churn −2.9 Durant rest/absence = **−4.9** => **114.4999** regulation points (PPP 1.1315). No Houston home advantage; all effects applied exactly once.
4. Regulation joint game: total Normal(mean **227.1587**, SD **23.2**); HOU−DAL margin Normal(mean **+1.8411**, SD **18.8**), rho(T,M)=**+0.04**; sample 1,800,000 from one correlated seed 20261011578, discretise to compatible integer total and margin. These SDs are *widened analyst preseason widths*, anchored to NBA 2025–26 residual total 19.4 and margin 15.1, and NBA 2023–25 profile raw total 20.04, margin15.98. Correlation of scores implied from total/margin object is close to 2023–25 raw NBA +.223, not forced as an NBA-preseason fit.
5. Overtime: sample an explicit 4.7% close-game branch (NBA profile historical 4.7%; BASE_RATES 2025–26 4.4%). When OT, draw added total with mean 25.2 and SD5.8, enforce a nonzero final winning margin; regulation two-team score remains tied on that branch. This stylised branch explicitly includes OT, does not simulate possession-by-possession 5-minute OT, and is not a fitted preseason OT kernel. All final scores integer, no final tied games.
6. Terminal grid arithmetic (simulation output): Dallas **113.29±14.95**, Houston **115.08±15.43**; total **228.37±23.85**, HOU−DAL margin **+1.78±18.81**. Expected full-game total equals combined expected team scores within rounding. Final-score integration yields every pick, all four supplied contracts and winner from one grid; marginal probability status uncalibrated.
7. Sensitivity: remove ALL discretionary rotation/availability shifts (Dallas +1.3 points, Houston +4.9), so the regulation total centre rises **6.2** to 233.36. A same-width Normal approximation makes P(Over198.5) >90% (excluded by framework ceiling), P(Under258.5) ≈84%, and changes the top-two valid total thresholds. A second direction stress case with Durant unexpectedly active adds about 2.9 HOU points, reducing the Under probability. Rerun if officially declared starters/participation change; the card is conditional and lineup-uncertain.
8. Required branches: normal established rotations, Irving restricted/reduced minutes, Durant rested vs unexpected appearance, bench-heavy fourth quarter, hot three-point tail, slow/cold early stretch, foul-driven FT variance, multiple overtime (not separately calibrated), and possible late scratches. None used to infer a certain winner from the Oct 9 final.

#### A5. Priced ladder — same terminal score grid
| Family | Line | Probability | Complement |
|---|---|---:|---:|
| Total | Under 257.5 | 88.9% | Over 257.5 11.1% |
| Total | Under 258.5 | 89.7% | Over 258.5 10.3% |
| Total | Under 259.5 | 90.4% (EXCLUDED: >90%) | Over 259.5 9.6% |
| Total | Over 197.5 | 90.3% (EXCLUDED: >90%) | Under 197.5 9.7% |
| Total | Over 198.5 | 89.6% | Under 198.5 10.4% |
| Total | Over 199.5 | 88.8% | Under 199.5 11.2% |
| Total | Over 230.5 | 46.1% | Under 230.5 53.9% |
| Margin | Rockets +20.5 | 88.3% | Mavericks −20.5 11.7% |
| Margin | Rockets +21.5 | 89.3% | Mavericks −21.5 10.7% |
| Margin | Rockets +22.5 | 90.2% (EXCLUDED: >90%) | Mavericks −22.5 9.8% |
| Margin | Mavericks +23.5 | 87.6% | Rockets −23.5 12.4% |
| Margin | Mavericks +24.5 | 88.7% | Rockets −24.5 11.3% |
| Margin | Mavericks +1.5 | 48.0% | Rockets −1.5 52.0% |

**Caveat:** The candidate ladder is finite and the derived thresholds are hypothetical. Moving a cushion or total line to an even wider value can mechanically increase its probability; a high `p_card` is not evidence of value or commercial availability. Rankings are conditional on the disclosed candidate set, not optimal over every possible threshold.

#### A6. Analyst adjustments, size and dependence
| Name | Target | Size | SD units | Prior basis |
|---|---|---:|---:|---|
| Preseason limited/staggered minutes DAL | Dallas regulation mean | −2.0 | 0.134 Dallas-score SD | analyst_judgement |
| Irving restricted return DAL | Dallas regulation mean | +0.7 | 0.047 Dallas-score SD | analyst_judgement, reported probable not active confirmed |
| Preseason limited/staggered minutes HOU | Houston regulation mean | −2.0 | 0.130 Houston-score SD | analyst_judgement |
| Durant expected rest HOU | Houston regulation mean | −2.9 | 0.188 Houston-score SD | analyst_judgement, reported OUT (not official five) |
| Combined Houston roster/rotation effect | Houston regulation mean | −4.9 | 0.318 Houston-score SD | analyst_judgement total of preceding two rows; not applied twice |
| Neutral site | Houston margin home edge | 0.0 | 0.000 margin SD | fixture fact; no Houston-location adjustment |
**Unadjusted top two:** Under 258.5 and Over 198.5 do not retain the same probability ordering or ceiling eligibility with all roster adjustments removed; a valid unadjusted pair would require alternative derived lines (e.g., Over 204.5 / Under 258.5) and a fresh jointly priced ladder. This is a *sensitivity*, not a second issued prediction. `ADJUSTMENT_DEPENDENT`.

#### A7. Family checks
- **All rows from one grid:** P(Rockets−1.5) 52.0% + P(Mavericks+1.5) 48.0% = 100.0%; P(Over230.5) 46.1% + P(Under230.5) 53.9% = 100.0%. Margin win Rockets 53.7% from same distribution; no draw in completed NBA games.
- **Total centre from possession×PPP:** 101.195×(1.1133+1.1315)=227.16 regulation; OT +1.20 approx = 228.37 completed-game mean; not a typed 230.5 line-centre. Means and SD in A4. Preseason one-game 252-point total is not used as an unshrunk forecast.
- **Family nesting/monotonic:** Under257.5 88.9% < Under258.5 89.7% < Under259.5 90.4%; Over197.5 90.3% > Over198.5 89.6% > Over199.5 88.8%; favourites/underdogs consistent with one HOU−DAL margin random variable.
- **Joint failure:** rank1 Under258.5 loss T≥259, rank2 Over198.5 loss T≤198: intersection empty, p=0.0%. This trivial wide-bracket property cannot be interpreted as evidence of calibration or betting value.
- **Gate:** 89.7% vs best non-complementary 89.6% gap 0.102 percentage points <4 => RANK1_UNSTABLE. Rank2≥58%. Both top two are totals on the same underlying score process. Correlated meaningful risk (regime shift) remains even though mathematical paired losses are impossible under completion.
- **NBA PRESEASON:** separate from NBA regular season; historical NBA priors widened by judgment, NOT fitted preseason distribution; missing precise starters/active minutes. No player prop or opening-margin claims. Neutral site correctly removes Houston geographical home advantage.
- **Timing:** actual first-jump time unverified; analytical completion 2026-10-11T21:01:22+11:00; state LATE_START_UNVERIFIED. Neither official 11 Oct live score nor game-final facts used. Operator contract void/resolution terms unknown.

#### A8. Sources (field, link, access time)
1. NBA official Oct 11 event `https://www.nba.com/game/DAL-vs-HOU-0012600016` — participants, league phase, game ID, planned 6 AM EDT, venue; read 2026-10-11T21:01:22+11:00.
2. Dallas Mavericks official 2026 preseason schedule `https://www.nba.com/mavs/news/mavericks-announce-2026-preseason-schedule` — Oct 9/11 Macao exhibitions, Oct11 5 AM CDT; read 2026-10-11T21:01:22+11:00.
3. NBA 2026 China Games primer `https://www.nba.com/news/2026-nba-china-games-everything-to-know` — both games in Macao 6 PM Sunday local; read 2026-10-11T21:01:22+11:00.
4. NBA official Oct10 Starting 5 `https://cdn-uat.nba.com/news/starting-5-october-10-2026` — completed *first* game 135–117 and Kyrie expected to debut on Sunday; read 2026-10-11T21:01:22+11:00.
5. Reuters Oct 8 `https://www.reuters.com/sports/dallas-mavericks-irving-excited-play-again-after-lengthy-injury-absence-2026-10-08/` — Irving long ACL recovery and intended first return; read 2026-10-11T21:01:22+11:00.
6. Yahoo/Roundtable Oct11 `https://sports.yahoo.com/articles/october-11th-injury-report-houston-073032121.html` — secondary injury status reporting (Durant rest OUT, Irving probable and Dallas questionables); browser returned 429 but search result full text accessible, evidence marked secondary/limited; read 2026-10-11T21:01:22+11:00.
7. RealGM exact matchup `https://basketball.realgm.com/nba/preview/2026-10-11/Dallas-at-Houston/526583` — Oct9 prior-game 2026–27 preseason box team field stats, not official Oct11 starters; read 2026-10-11T21:01:22+11:00.
8. Public Rockets game preview `https://www.thedreamshake.com/rockets-game-previews/41862/houston-rockets-vs-dallas-mavericks-game-preview` — reported uncertain projected players and injury/later availability, secondary not a line-up authority; read 2026-10-11T21:01:22+11:00.
9. GitHub main `https://github.com/danisgreat/Sports-Research` @ `33d0ea0c1c70056db7c7fb0a07dec77a633e573f` — rules/templates/base rates, read 2026-10-11T21:01:22+11:00; GitHub read-only.
10. `Previous Sports Results/Basketball/NBA/2025/2025_games.csv` — header, at least first historical row opened; 2026 path unavailable, 2025 whole-file count not verified; read 2026-10-11T21:01:22+11:00.

#### A9. Integrity receipt
`SPORTS_ONLY_MARKET_BLIND: PASS` · `OBSERVED_IN_GAME_OUTCOME_USED: NO` · `SETTLEMENT: NOT_PERFORMED` · `ADJUSTMENT_DEPENDENT` · `STARTING_FIVES_NOT_CONFIRMED` · `GAME_PHASE: PRESEASON` · `SPORTS_SCORE_ONLY / ACTION_TERMS_UNKNOWN` · `RANK1_UNSTABLE` · `CANONICAL_IMPORT: PENDING`.
<!-- END CARD P-578 -->
