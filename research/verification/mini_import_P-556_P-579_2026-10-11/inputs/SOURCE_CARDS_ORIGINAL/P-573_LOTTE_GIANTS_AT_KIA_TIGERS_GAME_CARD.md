<!-- BEGIN CARD P-573 -->
## Card · P-573 · Baseball / Korea KBO · Lotte Giants @ KIA Tigers · 2026-10-11

- **Working ID:** `P-573 — LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT`
- **Event key:** `KBO:2026:LOTTE-KIA-GWANGJU-20261011:2026-10-11`
- **Native event ID:** `NOT_VERIFIED` (MyKBO secondary event 14036; not a confirmed KBO-native game identifier)
- **Sport:** `Baseball`
- **League:** `KBO League / 2026 regular season, makeup game; NOT postseason`
- **Tracking alias:** `LOCAL-20261011-P-573-KBO-LOT-KIA`
- **Analysis status:** `UNCALIBRATED_ANALYST_SCENARIO`
- **Timing state:** `LATE_START_UNVERIFIED`
- **Research completed:** `2026-10-11T16:04:07+11:00` (scheduled first pitch 16:00 AEDT; pregame source material only; official actual first-pitch timestamp unverified)
- **Scheduled start:** `2026-10-11T16:00:00+11:00` (14:00 KST; user-provided 15:00 AEDT was one hour early)
- **Endpoint:** `KBO regular-season full-game official final; nine regulation innings, up to 11 if tied; tie terminal after 11; home does not bat bottom nine when already ahead; home walk-off ends game; rain/suspension per official ruling. No named operator provided, so operator-specific two-way ML tie handling UNKNOWN_DEFINITION.`
- **Distribution object:** `kbo_lot_kia_nb_inning_extras_v1 — per-game common lognormal environment σ=0.044, independent team gamma-Poisson rates with φ=0.290; 9-inning opportunity mean Lotte 3.75, KIA 5.30; Oller segment Lotte 0.370 per inning (1–6), KIA relief exposure 0.510 per inning (7–9); Kim Jin-uk segment KIA 0.610 per inning (1–5), Lotte relief exposure 0.5625 per inning (6–9); skip/stop home ninth and cap walk-offs; tied after nine plays tenth/eleventh with bullpen per-inning rates, can still tie; simulation seed 5732026, N=750000; no bookmaker data`
- **Expected score:** `runs, KBO full official game incl. up to two extra innings; SDs from one reproducible marginal joint-score simulation — Lotte Giants 3.818 (SD 2.832) · KIA Tigers 4.973 (SD 3.309) · combined total 8.791 (SD 4.448) · margin KIA − Lotte +1.155 (SD 4.260)`
- **Regime flags:** `NONE (late regular-season makeup; neither EARLY_SEASON nor postseason; no regime multiplier)`
- **Retirement rule:** `N/A`
- **Listed-pitcher rule:** `FRAMEWORK_DEFAULT: sporting event forecast stands when the game is official; if announced starting pitcher changes before actual pitch, a dated addendum/reforecast is required; operator listed-pitcher action remains UNKNOWN_DEFINITION, not assumed.`
- **Abandonment rule:** `FRAMEWORK_DEFAULT: grade against official KBO FINAL/official-game decision only; a postponed/nonterminal game remains PENDING_EVENT for settlement; an abandoned game without an official terminal score yields VOID; no operator-specific action terms established.`
- **Settlement fields:** `official team scores, R/H/E and innings line scores including 9/10/11 and final status (KBO English Scoreboard https://eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=2026-10-11 ; KBO Korean Scoreboard as fallback); official starting pitchers from GameCenter if accessible; no narrative-only settlement.`
- **Capture due:** `2026-10-12T16:00:00+11:00` (24 hours after scheduled start, within 36 hours)
- **Rules read:** `METHOD.md; CURRENT_STATE.md; CURRENT_RULES.md §§1–9; SELECTION_RULES.md §§1–8; CARD_AND_LOG_TEMPLATES.md §§2–3a, 7; RULES_BASEBALL.md §0, §§3–5, 7–9; PROBABILITY_TOOLKIT.md §§3, 3.1; BASE_RATES_REGISTER.md §§3, 5; LEAGUE_PROFILES.md Baseball KBO row; SOURCES.md §3.1 and historical §§3.14–3.16; ARCHIVE_USE_GUIDE.md §§1–6; research/prompts/1_GAME_CARD.md B1; research/prompts/README.md.`
- **Archive check:** `BASELINE_AVAILABLE: LEAGUE_PROFILES.md KBO regular-season 2023–2025 n=2182, home 4.88, away 4.89, total 9.77, SD(total)=4.93, SD(margin)=4.79, NB φ=.290, env σ=.044, one-run 23.8%, tie 2.1%; headers opened for Previous Sports Results/Baseball/KBO/{2023,2024,2025}/{year}_games.csv (fields including Away/Home Score, Total Runs, Innings Played, Extra Innings, starting pitchers); exact 2026 KBO yearly path is NOT_FOUND; current-team 2026 numbers sourced instead from league-owned standings and MyKBO pregame snapshot. Archive-level aggregate used rather than pretending individual game rows were fully enumerated in this card.`
- **Evidence quotes:** `KBO league Scoreboard @ 2026-10-11T15:59:13+11:00: LOTTE–KIA; GWANGJU 14:00 KST; pregame dashes for inning scores. MyKBO @ pregame scan 15:58–15:59 AEDT: "October 11, 2026 2:00pm · Gwangju Kia Champions Field"; "Kim Jin-uk" / "Adam Oller". OSEN/Chosun pregame lineup releases published 12:10–12:40 KST: KIA order Park Jae-hyun, Han Jun-su, Kim Do-yeong, Castro, Na Sung-beom, Kim Sun-bin, Kim Ho-ryung, Kim Tae-gun, Park Min; Lotte order Reyes, Na Seung-yeop, Go Seung-min, Han Dong-hui, Jeon Min-jae, Son Seong-bin, Jang Du-seong, Yoon Dong-hee, Jo Se-jin. The third-party live lineup table disagrees in Lotte LF/RF; official GameCenter battingOrder not independently retrieved.`

### Decision block

**Distribution:** `kbo_lot_kia_nb_inning_extras_v1`. Nine-inning innings-exposure count with starter/bullpen segments, φ=.290 gamma mixture per team, shared game σ=.044, KBO exact 11-inning cap, home ninth omitted when leading and walkoff capped. 750,000 terminal scores (deterministic seed). Expected 8.791 total (SD 4.448); KIA−Lotte +1.155 (SD 4.260); simulated regulation tie 9.60%, terminal tie 2.52%. **Not fitted or calibrated.** Late first-pitch timing and missing independent official batting order prevent a qualified Rank 1.

| Rank | Role | Tag | Proposition | p_card | Probability status | Evidence | Failure route |
|---|---|---|---|---|---|---|---|
| 1 | PICK | ANALYST_DERIVED (replaces supplied Over/Under 8.5) | Combined total Under 14.5 runs — KBO full game incl. extras (max 11 innings) | 89.1% | FROM_DISTRIBUTION:kbo_lot_kia_nb_inning_extras_v1 | 8.791 expected total; heavy overdispersion φ=.290 and good Oller starting segment still leave P(15+)=10.9% | KIA early slugging and/or bullpen blowup pushes 15+ runs |
| 2 | PICK | ANALYST_DERIVED (replaces supplied Over/Under 8.5) | Combined total Over 4.5 runs — KBO full game incl. extras (max 11 innings) | 84.7% | FROM_DISTRIBUTION:kbo_lot_kia_nb_inning_extras_v1 | Team-scoring exposure and two pitching staffs: P(5+)=84.7%; chosen as non-cofailure cover versus Rank 1 | Shutout/low-conversion game ends at 0–4 total runs |
| 3 | INFORMATIONAL | ANALYST_DERIVED (team protected handicap) | KIA Tigers +2.5 runs — KBO full game incl. extras (max 11 innings) | 82.8% | FROM_DISTRIBUTION:kbo_lot_kia_nb_inning_extras_v1 | KIA home, Oller 3.03 ERA / 175 SO, strong lineup; permits KIA loss by ≤2 or tie | Lotte wins by 3+ on contact sequencing and KIA bullpen failure |
| 4 | INFORMATIONAL | ANALYST_DERIVED (away protected handicap) | Lotte Giants +4.5 runs — KBO full game incl. extras (max 11 innings) | 81.1% | FROM_DISTRIBUTION:kbo_lot_kia_nb_inning_extras_v1 | Broad underdog cushion; Lotte 4.70 season runs/game and .272 BA | KIA wins by 5+ on power hitting and Kim Jin-uk short outing |

**P(Rank 1 and Rank 2 both lose):** `0.0% by construction` — Under 14.5 loses at total ≥15, Over 4.5 loses at total ≤4; cannot coincide. They are strongly dependent bracketing rows, not two independent achievements.
**Rank 1 − Rank 2 gap:** `4.5 percentage points` for the two selected picks. This is not the gate comparison.
**Rank-1 gate:** `RANK1_UNSTABLE` — Rank 1 89.117%, best alternative KIA +3.5 = 88.23%, lead only `0.89 percentage points <4.00` (SELECTION_RULES §2); also BB-P2 official batting order NOT_VERIFIED blocks a *qualified* full-game total at Rank 1. The score simulation is narrower than the historical KBO SD; qualification withheld.
**Adjustment dependence:** `NONE formally` — all inputs unfitted analyst modelling with no single separately applied offset above 0.25 game-total SD; sensitivity of starter/relief ability does change what line would rank first.
**Supplied rows not selected:** `Giants +2.5 66.3%; Tigers −2.5 33.7%; combined total Over 8.5 47.9%, Under 8.5 52.1%`. Endpoints include extra innings and possible terminal tie; two-way 'Giants ML' was not supplied. None of these probabilities expresses bookmaker value.
**Potential winner:** `KIA Tigers 61.3%`, Lotte Giants 36.2%, final KBO tie 2.5% (full game max 11 innings; **three-way**). A two-way operator ML's action on an 11-inning tie is `UNKNOWN_DEFINITION`.

### Appendix

#### A1. Identity, timing and endpoint
- Official KBO fixture 2026-10-11 at 14:00 KST / 16:00 AEDT, Lotte away at KIA home, Gwangju Kia Champions Field; 2026 *regular-season* makeup game. No postseason walkoff-format transplant. User stated 15:00 AEDT; this was one hour early.
- Last pregame source scans at 15:58–15:59 AEDT, content originated before 14:00 KST. Research and this full card finished *after scheduled kickoff* at 16:01:41 AEDT, actual first pitch not independently timestamped. `LATE_START_UNVERIFIED`; cannot certify PREGAME, and no observed inning/score is used.
- KBO 2026 regular season uses 11-inning maximum, may finish in a tie (Yonhap 2026-04-07); regulation is nine, home bottom nine omitted when already leading, walkoffs capped at winning run. No operator-specific abandonment/listed-pitcher/tie action supplied; keep these unknown.

#### A2. Supplied contracts (reference only)
| Contract | Model p_card | Complement or other state |
|---|---:|---|
| Lotte Giants +2.5 runs, full game | 66.3% | KIA Tigers −2.5 33.7% |
| KIA Tigers −2.5 runs, full game | 33.7% | Lotte Giants +2.5 66.3% |
| Combined total Over 8.5 runs, full game | 47.9% | Under 8.5 52.1% |
| Combined total Under 8.5 runs, full game | 52.1% | Over 8.5 47.9% |

#### A3. Pregame evidence and exposure
- **Teams:** KBO 2026 prior to game: KIA 78–62–2 (3rd), 764 runs for/658 allowed in 142 games: 5.38 RF/G / 4.63 RA/G; home 5.17 RF/G /4.39 allowed (71 games). Lotte 62–77–3 (8th), 668/737 in 142: 4.70/5.19; road 4.51/4.44 (71 games). KIA 172 HR vs Lotte 109, both .272 batting. KIA win may clinch third; a qualitative urgency input, not a free +0.5 run.
- **Opposing starters:** Lotte LHP **Kim Jin-uk** 25 starts, 138⅓ IP, 4.29 ERA, 1.36 WHIP, 117 K / 50 BB in 606 batters faced (K%=19.3, BB%=8.3). Most recent Oct 5 vs KT: 4.0 IP, 7 ER, nine hits, 1 K, 1 BB — game log and official pregame reporting; the last outing is a volatility indicator, not automatically his true rate. His last six starts include short exposure; working starter 5.0 innings (uncertain 4–6.5).
- KIA RHP **Adam Oller** 29 starts, 172⅓ IP, 3.03 ERA, 1.07 WHIP, 175 K /60 BB in 695 batters faced (K%=25.2%, BB%=8.6%). Oct 5 vs LG: 6.0 IP, 4 ER, 5 hits, 4K/4BB. Opponent Lotte April 24 shutout (9IP, 0R, 11K) is only one start, explicitly shrunk toward his season rate. Working starter 6.0 innings (uncertain 5–7). No authenticated same-day pitch count/velocity/pitch-mix adjustment.
- **Lineups:** Two pregame beat reports at 12:10–12:40 KST carry complete order and positions; KIA Park Jae-hyun LF, Han Jun-su DH, Kim Do-yeong 3B, Castro 1B, Na Sung-beom RF, Kim Sun-bin 2B, Kim Ho-ryung CF, Kim Tae-gun C, Park Min SS. Lotte Reyes DH, Na Seung-yeop 1B, Go Seung-min 2B, Han Dong-hui 3B, Jeon Min-jae SS, Son Seong-bin C, Jang Du-seong CF, Yoon Dong-hee RF, Jo Se-jin LF. Alternative secondary lineup page prints differing Lotte outfield order; official gamecentre `battingOrder` release not retrieved. Hwang Seong-bin absent from Lotte order after shoulder injury vs LG on Oct 10. Note replacement effects as model uncertainty.
- **Bullpen:** KIA reported all relievers ready to pitch to clinch third, including Jeon Sang-hyun; historical KIA 2026 home relief ERA 3.04, Lotte away relief ERA 3.43 (MyKBO splits; not complete availability lists). No detailed pitch-count last-two-days or every availability clearance; workload/unavailable high leverage `NOT_VERIFIED`. Lotte Oct 10 went 10 innings vs LG, a possible but unquantified relief-workload risk. KIA Oct 10 vs SSG late reporting existed but exact final bullpen workload not independently reconciled.
- **Park/weather:** venue official identity Gwangju Kia Champions Field. Pregame secondary on-site estimate ~28°C partly cloudy, southerly ~6 km/h, light rain risk, not an exact field-relative wind direction or verified park HR factor. `WEATHER_EFFECT=0`, venue park multiplier `1.000 analyst placeholder`; no invented launch factor.
- **Recent form:** Lotte last 10 reported 6.5 RF/G, KIA 4.1 RF/G in third-party team-splits table; this is noisy and receives shrinkage rather than being inserted as forecasts. No comprehensive opponent-adjusted pitches-by-type velocity or 2026 roster-adjusted park factors measured. KIA offensive slug and Oller's stronger K% are meaningful qualitative components; point shifts still analyst assumptions.

#### A4. Reproducible distribution, innings, mean and SD
1. Historical KBO regular-season LEAGUE_PROFILES n=2,182 (2023–2025): home 4.88, away 4.89, full total 9.77, total SD4.93, margin SD4.79; φ=.290, shared log environment σ=.044; one-run game 23.8%, terminal tie 2.1%. Current 2026 team season scoring high enough to justify event-specific 9-inning opportunities rather than use 9.77 blindly.
2. Nine-inning available-exposure anchor for KIA: average KIA home offence 5.17 and Lotte road concessions 4.44 yields unadjusted 4.805. Analyst KIA power/lineup and Kim starting workload adjustment combined +0.495 → 5.30 over nine *available innings* (not actual final mean); no external fitted causal interpretation. For Lotte: average away 4.51 and KIA home concessions 4.39 =4.45; Oller strong starting segments and Hwang absence combine −0.70 → 3.75. Both adjustments are `analyst_judgement`; uncertainty is high.
3. Exposures per side (nominal 9 full batting innings): KIA versus Kim 5×0.610=3.050 runs, versus Lotte relief 4×0.5625=2.250; total 5.300. Lotte versus Oller 6×0.370=2.220, versus KIA relief 3×0.510=1.530; total 3.750. Source 2026 9-inning rates do not uniquely identify the component effects; components sum exactly by construction. Stadium weather adjusted at 1.000; no named pitch-count override.
4. For each simulation, environment `E=exp(Zσ−σ²/2)` with σ=.044; team exposure multiplier `G~Gamma(shape=1/φ,scale=φ)`, φ=.290, independent conditional on E. Each team's runs in inning i `Pois(E×G_team×nominal_inning_rate)`; marginal single-team conditional sums have Var(R)=μ+φμ², plus small shared E covariance. Same gamma applies to its starter and relief innings, a **simplification**: individual starter and bullpen shock dispersion is not separately identified; the innings rates explicitly distinguish starter vs bullpen.
5. Generate top of innings 1–9 and home 1–8, then if home already leads skip bottom nine. Otherwise generate bottom nine, stopping at first walkoff-winning run (cap realised home inning runs at the deficit+1). If tied after nine, play ten and (if still tied) eleven with bullpen rates Lotte 0.510 and KIA 0.5625, stopping at home walkoffs. Remaining tie after 11 terminal; no runner-on-second rule imported. Tail retained beyond 20 runs, no arbitrary cap.
6. Deterministic Monte Carlo PCG64/NumPy `default_rng(5732026)`, N=750000 complete trajectories. **Final expected:** Lotte 3.818 (SD2.832), KIA 4.973 (SD3.309), total 8.791 (SD4.448), margin KIA−Lotte +1.155 (SD4.260). All final means include extra-innings and truncation. Regulation tie 9.60%, final tie 2.52%; P(KIA win/Lotte win/tie) 61.31%/36.18%/2.52%. Team mean sum 3.818+4.973=8.791; SD(total) from full joint terminal sample, not falsely `√(SDteam²+SDteam²)`.
7. Margin P(KIA wins by ≥1/2/3/4/5) = 61.31%/43.11%/33.67%/25.60%/18.91%. P(Lotte win by exactly 1)=11.32%; P(KIA win by exactly 1)=18.20%; P(|margin|=1)=29.51%, above historical 23.8% (+5.71 pp): **MODEL_ONE_RUN_OVERSHOOT** / cannot assert calibrated puck/run-line family. A low-total game (≤7 runs) has P(one-run)=39.5% and margin SD2.69 versus ≥10-run games P(one-run)=19.9%, margin SD5.61; the model correctly increases margin spread with total, despite its imperfect unconditional benchmark.
8. Rank 1 Under14.5 = P(total≤14) 89.117%; rank2 Over4.5 = P(total≥5) 84.655%; their losses are disjoint. Monte Carlo standard error approx 0.036pp for 89.1%, 0.042pp for 84.7% (sampling error only, excludes model error). Historic SD4.93 vs scenario 4.448 (10% narrower) and margin 4.79 vs scenario 4.260 (11% narrower) are calibration warning signals; named causes not demonstrated.

#### A5. Priced ladder and complements (from SAME terminal sample)
| Proposition, full game incl. up to 11 innings | p_card | Complement |
|---|---:|---|
| Combined total Under 14.5 | 89.1% | Over 14.5 10.9% |
| Combined total Over 4.5 | 84.7% | Under 4.5 15.3% |
| Combined total Under 13.5 | 86.1% | Over 13.5 13.9% |
| KIA +3.5 | 88.2% | Lotte −3.5 11.8% |
| KIA team Over 1.5 | 87.7% | KIA team Under 1.5 12.3% |
| Lotte +5.5 | 86.3% | KIA −5.5 13.7% |
| KIA +2.5 | 82.8% | Lotte −2.5 17.2% |
| Lotte +4.5 | 81.1% | KIA −4.5 18.9% |
| Combined total Under 12.5 | 80.9% | Over 12.5 19.1% |
| Combined total Over 5.5 | 74.6% | Under 5.5 25.4% |
| KIA +1.5 | 75.1% | Lotte −1.5 24.9% |
| Lotte +1.5 | 56.9% | KIA −1.5 43.1% |
| Lotte +2.5 (supplied) | 66.3% | KIA −2.5 33.7% |
| Combined total Over 8.5 (supplied) | 47.9% | Under 8.5 52.1% |
| KIA win (3-way) | 61.3% | Lotte win 36.2% + tie 2.5% |
| Over 3.5 | 90.067% — NOT ELIGIBLE, strict unrounded >90% ceiling | Under 3.5 9.933% |

Rank-2 choice follows SELECTION_RULES §3 joint-loss minimisation, rather than simply taking the second-highest individual p. Under14.5 + KIA+3.5 have a model joint-failure mass 1.90% (KIA loses by ≥4 while total ≥15); Under14.5 + Over4.5 have **0.00% joint failure** by construction, though the latter p is smaller. Four issued rows are nonincreasing by p_card. Other high-p rows in this diagnostic ladder are unissued alternatives, not silently recast as lower ranks.

#### A6. Adjustments and counterfactual
| Name | Target | Size | SD units | Prior basis |
|---|---|---:|---:|---|
| KIA power/current lineup + Kim segment relative to simple home/road scoring anchor | KIA nine-inning opportunity runs | +0.495 | 0.111× scenario total SD | `analyst_judgement` |
| Oller relative to KIA home concessions plus Hwang Lotte lineup absence | Lotte nine-inning opportunity runs | −0.700 | 0.157× scenario total SD | `analyst_judgement` |
| Weather and ballpark scale (unverified field direction) | both | +0.000 | 0.000 | `analyst_judgement` (no direction assumed) |

**Sensitivity:** If Oller's suppression is 0.55 runs weaker (Lotte nine-inning opportunity 3.75→4.30, starter/relief segment rates rescaled), with same random seed, Lotte full mean 4.370, KIA 5.001, total 9.371; KIA winner 56.5%, Lotte 41.1%, tie 2.3%. Under14.5 falls 89.1%→86.2%; Over4.5 rises 84.7%→87.1%, flipping top-two rank order. Over8.5 shifts 47.9%→52.9%. The issued baseline remains frozen; sensitivity only. All scenario adjustments individually below ≥0.25-SD gate; **Adjustment dependence:** formally `NONE`, but practical top-two order sensitive to assumed Lotte suppression. **Unadjusted top two:** no separate large SD override; scenario anchors are uncalibrated.

#### A7. Family checks, limitations and blocking gates
1. **BB-P1:** announced starters Kim Jin-uk (LHP) and Adam Oller (RHP) verified from independent morning reporting and structured schedule; no independent warm-up proof of actual starter at actual first pitch; replacement requires addendum. **BB-P2:** order exists in pregame beat reports, but official gamecenter `battingOrder` not retrieved, and Lotte LF/RF order conflicts with a third-party page ⇒ **OFFICIAL_LINEUP_NOT_VERIFIED; blocking qualified full-game total/run-line Rank 1**, notwithstanding exploratory rankings.
2. **BB-P3/P5:** regular season, max 11 innings, tied terminal; exact home batting and walkoff model included. **BB-P4:** absent operator settlement definition means `UNKNOWN_DEFINITION` for listed-pitcher/tie/cancellation action; sporting endpoint probabilities not substituted for a two-way ticket win.
3. **±1.5 decomposition:** KIA +1.5 = KIA win 61.31% + KIA loss by 1 11.32% + tie 2.52%=75.14%; Lotte +1.5 = Lotte win 36.18% + loss by 1 18.20% + tie 2.52%=56.89%; (Lotte +1.5 <65% so barred from Rank1). KIA −1.5 = KIA margin≥2 43.11%; Lotte −1.5 = Lotte margin≥2 24.86%. Lotte +2.5 supplied = Lotte win 36.18 + tie2.52 + KIA margin=1 18.20 + margin=2 9.44 = **66.33%**; KIA−2.5 33.67%. Opposite-runline probabilities sum 100%.
4. **One-run structure:** P(|margin|=1)=29.5% model vs 23.8% KBO 2023–25; model recognizes higher totals widen the margin (SD 2.69 for ≤7 total vs 5.61 at ≥10), but unconditional excess needs future model assessment. Do not read the underdog +2.5 as strong evidence of an upset or assume low total automatically means close game.
5. **Width:** total SD4.45 vs KBO 4.93 (90.2%), margin4.26 vs4.79 (88.9%); model may be underdispersed, so extreme-line 89.1% is fragile. Past archive's KBO extra-inning frequency is unreliable for the revised 11-inning rule; current 2026 tie endpoint uses official current rules.
6. **SELECTION_RULES §2:** Rank1 89.117%, strongest eligible non-complementary KIA+3.5 88.23%, margin 0.89pp <4.0; `RANK1_UNSTABLE`, separate unqualified cohort. Rank2 84.655% ≥58%; same-grid joint top-two failure =0.0%, not an independent accuracy guarantee. Four rows ≤90% at unrounded precision. KBO regular-season late date: `Regime flags NONE`, no finals or early-season multiplier imported.
7. **Timing:** pregame material only, but card completed after scheduled pitch and cannot certify timing, so not a performance-eligible prospective card. No odds, implied lines, prediction websites' picks or live scores used. `SPORTS_ONLY_MARKET_BLIND` passes. In-game state, whether first pitch was delayed, is NOT_VERIFIED.

#### A8. Evidence sources (all pregame facts, not live result inputs)
1. Official KBO scoreboard, 2026-10-11: https://eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=2026-10-11 — matchup, 14:00 KST, Gwangju, inning-state fixture; retrieved 2026-10-11T15:58–15:59+11:00 (league-owner lineage).
2. Yonhap official fixture schedule https://www.yna.co.kr/view/AKR20261008095500007 — 11th Lotte-KIA in Gwangju at 14:00 KST; publication before match; retrieved pregame 2026-10-11T15:58+11:00.
3. MyKBO game https://mykbostats.com/games/14036-Lotte-vs-Kia-20261011 — listed Kim Jin-uk / Adam Oller, standings, HR and batting, venue, weather, secondary lineup; pregame read ~15:58–15:59 AEDT; starter/lineup are secondary, not independent league-confirmed participation.
4. OSEN/Chosun 2026-10-11 12:40 KST https://biz.chosun.com/en/en-sports/2026/10/11/CW5S52SHNNHYRMF3VHPRTXQWZY/ — Lotte reported batting order, Kim Jin-uk, Hwang Seong-bin shoulder; fetched before first pitch; AI-translated republication of original reporter, **one** source lineage.
5. OSEN/Chosun 2026-10-11 12:10 KST https://biz.chosun.com/en/en-sports/2026/10/11/5OVAASYQXVFWXKWANL4CDEDPWA/?outputType=amp — KIA reported batting order, Oller start and bullpen readiness; read pregame, primary reporter via AI-translated page; league GameCenter not independently retrieved.
6. Official KBO standings https://eng.koreabaseball.com/Standings/TeamStandings.aspx — KIA 764/658, Lotte 668/737, 142 games; pregame 2026-10-11 afternoon (league-owner aggregate).
7. MyKBO 2026 split https://mykbostats.com/stats/team_splits/2026 — team home/away R/G/RA, past-ten, bullpen home/away ERA, no reliable event-specific available pitchers; read ~15:59 AEDT.
8. MyKBO starter logs https://pgtest.mykbostats.com/players/2114 and https://mykbostats.com/players/2770 — 2026 K/BB/ERA/IP and recent starts, season through Oct 5; secondary structured, read ~15:58–15:59 AEDT.
9. 2026 11-inning rule, Yonhap https://en.yna.co.kr/view/AEN20260407002800315 — ties declared after 11 innings since 2025; rule verified pregame.
10. Current GitHub `main` HEAD `33d0ea0c1c70056db7c7fb0a07dec77a633e573f` — METHOD v9.0, CURRENT_RULES, SELECTION_RULES, CARD_AND_LOG_TEMPLATES §3a, RULES_BASEBALL, PROBABILITY_TOOLKIT §§3–3.1, BASE_RATES_REGISTER §§3,5 and LEAGUE_PROFILES Baseball KBO, SOURCES §§3.1,3.14–3.16, ARCHIVE_USE_GUIDE; archive KBO 2023/24/25 CSV headers verified; current 2026 CSV path 404. **No GitHub write.**

#### A9. Integrity receipt
`SPORTS_ONLY_MARKET_BLIND: PASS` · `EVENT_IDENTITY_KBO: VERIFIED` · `START_TIME_CORRECTED: 16:00 AEDT` · `PREMATCH_SOURCE_SNAPSHOT: YES` · `CARD_PREGAME_COMPLETED: NO` · `TIMING: LATE_START_UNVERIFIED` · `STARTER_ANNOUNCEMENTS: YES` · `ACTUAL_STARTER_HANDSHAKE: NOT_VERIFIED` · `OFFICIAL_BATTING_ORDER: NOT_VERIFIED` · `SOURCE_GATE: PARTIAL` · `KBO_11_INNING_TIE: MODELED` · `N=750000` · `NO_LIVE_SCORE_USED: YES` · `BASELINE_TOTAL/MARGIN_SD_LOW: FLAGGED` · `RANK1: RANK1_UNSTABLE` · `PERFORMANCE_ELIGIBILITY: NOT_CERTIFIED` · `SETTLEMENT: NOT_PERFORMED` · `CANONICAL_IMPORT: PENDING` · `GITHUB_WRITES: NO`.
<!-- END CARD P-573 -->
