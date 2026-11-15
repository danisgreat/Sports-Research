# Local hockey reference-and-input snapshot — LOCAL-20261114B4496A3F-G0004
- Created (Australia/Sydney): 2026-11-14T21:46:45+11:00
- Immutable-on-creation for this chat only; NOT a GitHub publication receipt nor compiled `ml` reference stage.
- GitHub repository: danisgreat/Sports-Research; main pinned 008cedc4ff469e7a808292aa3667a7bffe22e273, read only. Current rules MDS/P v24.16, ICE_HOCKEY prompt1 v24.14, SEL-v4.
- Event: Tappara U20 (home) vs HPK U20 (Hämeenlinna U20), Finnish U20 SM-sarja 2026-27, federation referee assignment 2710291, Hakametsä, Tampere, 2026-11-14 13:00 EET = 2026-11-14 22:00 AEDT = 2026-11-14 11:00 UTC.
- Current event state: pre-scheduled-start when reference frozen, actual first puck NOT_VERIFIED. No in-play or match outcome included.
- Supplied contracts: Tappara ML; HPK ML; combined Over 5.5; combined Under 5.5; full game ML assumed including OT/SO, total goal scoring convention assumed reported official final score (shootout deciding goal +1 for a tied regulation game). Actual named market operator settlement rule NOT_VERIFIED.
- Playing rules regime: U20 SM-sarja regular season, 60-minute three periods; prior documented extra time and shootouts exist. Exact length/manpower and operator total settlement not independently confirmed and require verified source if used prospectively.
- Source: Finnish federation referee allocation https://taso.sjtl.fi/index.php?t=3028 ; two independent club schedules https://www.tappara.fi/fi-fi/article/a-nuoret/u20-ottelut/12/?filter_view=1&results=1 and https://hpk.fi/joukkue/hpk-u20/otteluohjelma-u20/ ; Stadiro dated team results https://stadiro.com/teams/hockey/finland/tappara-u20/ and https://stadiro.com/teams/hockey/finland/hameenlinna-u20/ ; independent game confirmations https://www.eliteprospects.com/team/1754/tappara-u20 and https://www.eliteprospects.com/team/2468/hpk-u20.
- Tappara season current 18 games: 56 GF 58 GA. HPK 15 games 58 GF 39 GA. Score rows below current-season regular results known before event. Preliminary data excludes user-event game.
- League baseline 18 current teams 313 team-games, GF 1007, GA 1005 (2-goal mismatch potentially overtime/shootout recording); mean GF/team/game = 1007/313 = 3.217252396; independent Poisson climatology mean per side 3.217252. Not a certified calibration or an exact league-regulation score feed.
- Match-up raw season rate λT=(56/18 + 39/15)/2 = 2.855555556, λH=(58/15 + 58/18)/2 = 3.544444444. Using team and opponent conceded arithmetic blend as an unfitted approximate exposure model, no shot/xG correction.
- Home margin placeholder from repo `FAMILY_PRIOR:ICE_HOCKEY` 0.34 goals, based on NHL/Czech NOT on Finnish U20; shift half +0.17 to Tappara, -0.17 to HPK keeping raw total 6.40; base regulation Poisson λT=3.025555556, λH=3.374444444, λtotal=6.400000000. This is a declared SCENARIO, not a verified measured U20 effect.
- No quantified fatigue shift in base: Tappara away 13 Nov wins 4-2 at Jokerit and hosts 14 Nov; HPK rested since 11 Nov 2-3 Lukko. NHL rest effects are NOT shown to transfer to Finnish U20. Sensitivity later.
- Goaltender status: both starting goalies UNKNOWN / LINEUP_UNCONFIRMED; franchise roster lists possible keepers but exact game starters not confirmed. Do not infer goalie health or confirmed starter from roster.
- No confirmed exact skater lines, scratches, current injuries, PP/PK deployment, reliable shot-quality stats or per-game xG. Goals-only ensemble and sensitivity, not a model-qualified forecast. Unknown goalie prevents top-ranked fragile total per RULES_ICE_HOCKEY §0.1/§4.14.
- Model: independent regulation Poisson with means shown, exact integer grid 0..28 each side, residual tails bounded; baseline independent league Poisson same λ on each team, 50/50 tied OT. Regulation tie resolved in OT/SO using 50/50 for base; conditional OT scenario 40%-60% HPK; this is an unvalidated split, not a match-specific OT estimator.
- Full-game totals: assume tied regulation gets exactly +1 official-deciding goal, so 5.5 over is unchanged by an OT/SO goal (ties are even regulation totals; <=4→<=5 or >=6→>=7). Periods/empty-net tail not separately estimated; team goals include their historical final scores. This is a distributional approximation.
- Pricing decision froze before probabilities: SUPPLIED_ONLY 4 rows, no derived alternative/easy lines. ML as full game (not regulation 3-way), totals full-game 5.5. If operator terms resolve differently, status UNKNOWN_DEFINITION and numeric rows CONDITIONAL_ONLY.
- Model uncertainty/sensitivity scenarios: low/high home margin adjustment 0 to +0.6; goalie attack shifts ±0.5 expected goal at each team; target 5.5 Poisson total sensitivity μ=5.6/6.4/7.2; Tappara fatigue optional scenario λT−0.20 and λHPK+0.20. No independent goalie mixture evidence weights.
- Critical: No market/odds/betting-site values read into sporting features; supplied lines are contract metadata only. No ML release, Monte Carlo claim, match result, settlement or canonical ID.

## Exact team result rows, newest first
| Side | Day | Opponent | Venue | GF | GA |
|---|---|---|---|---:|---:|
| Tappara | 2026-11-13 | Jokerit | A | 4 | 2 |
| Tappara | 2026-10-31 | Lukko | H | 5 | 2 |
| Tappara | 2026-10-30 | Ilves | A | 4 | 2 |
| Tappara | 2026-10-24 | KooKoo | H | 0 | 4 |
| Tappara | 2026-10-21 | Ilves | H | 2 | 6 |
| Tappara | 2026-10-17 | Jokerit | H | 4 | 3 |
| Tappara | 2026-10-16 | SaiPa | H | 3 | 7 |
| Tappara | 2026-10-10 | Assat | A | 6 | 3 |
| Tappara | 2026-10-07 | TPS | A | 1 | 4 |
| Tappara | 2026-10-03 | HPK | H | 0 | 5 |
| Tappara | 2026-10-02 | Assat | H | 4 | 2 |
| Tappara | 2026-09-27 | Lukko | H | 3 | 4 |
| Tappara | 2026-09-26 | Jukurit | H | 5 | 0 |
| Tappara | 2026-09-20 | Ilves | A | 4 | 2 |
| Tappara | 2026-09-19 | JYP | H | 2 | 1 |
| Tappara | 2026-09-12 | Jukurit | A | 2 | 5 |
| Tappara | 2026-09-09 | KalPa | A | 3 | 4 |
| Tappara | 2026-09-04 | TPS | A | 4 | 2 |
| HPK | 2026-11-11 | Lukko | H | 2 | 3 |
| HPK | 2026-10-28 | TPS | A | 0 | 1 |
| HPK | 2026-10-23 | Ilves | A | 4 | 2 |
| HPK | 2026-10-21 | Kiekko-Espoo | H | 4 | 8 |
| HPK | 2026-10-17 | Lukko | H | 2 | 3 |
| HPK | 2026-10-10 | Karpat | H | 1 | 3 |
| HPK | 2026-10-07 | Jukurit | H | 7 | 4 |
| HPK | 2026-10-03 | Tappara | A | 5 | 0 |
| HPK | 2026-09-27 | Jukurit | A | 7 | 1 |
| HPK | 2026-09-26 | KalPa | A | 5 | 6 |
| HPK | 2026-09-19 | KalPa | H | 4 | 2 |
| HPK | 2026-09-13 | Sport | A | 3 | 2 |
| HPK | 2026-09-12 | Assat | A | 2 | 3 |
| HPK | 2026-09-05 | TPS | H | 6 | 1 |
| HPK | 2026-09-04 | Ilves | H | 6 | 0 |

## Tappara form-window receipt (overlapping windows; counted once)
| Window | n | First/last date | GF/g | GA/g | Goal margin/g |
|---|---:|---|---:|---:|---:|
| L5 | 5 | 2026-10-21 to 2026-11-13 | 3.000 | 3.200 | -0.200 |
| L10 | 10 | 2026-10-03 to 2026-11-13 | 2.900 | 3.800 | -0.900 |
| L15 | 15 | 2026-09-19 to 2026-11-13 | 3.133 | 3.133 | +0.000 |
| L20 | 18 | 2026-09-04 to 2026-11-13 | 3.111 | 3.222 | -0.111 |

## HPK form-window receipt (overlapping windows; counted once)
| Window | n | First/last date | GF/g | GA/g | Goal margin/g |
|---|---:|---|---:|---:|---:|
| L5 | 5 | 2026-10-17 to 2026-11-11 | 2.400 | 3.400 | -1.000 |
| L10 | 10 | 2026-09-26 to 2026-11-11 | 3.700 | 3.100 | +0.600 |
| L15 | 15 | 2026-09-04 to 2026-11-11 | 3.867 | 2.600 | +1.267 |
| L20 | 15 | 2026-09-04 to 2026-11-11 | 3.867 | 2.600 | +1.267 |

## Known-at / identity limitations
- Pages list dated past finished games, but most dynamic sources lack original explicit publication timestamps. Availability before start logically follows from prior-game completion; exact first web availability is KNOWN_AT_UNVERIFIED.
- Third-party game-state pages updated asynchronously; no current score used. Exact release status of playing roster/goalies NOT_CONFIRMED.
- Finnish federation referee calendar exposes game ID 2710291; its linked event detail page is technically empty to the web text parser. Do not treat that as an official game-day lineup sheet.
- Full 2026 U20 league team aggregate list came from season table; 2-goal GF vs GA mismatch noted and retained. Competition historical data are too short to validate dispersion or calibrated team goal rates.
