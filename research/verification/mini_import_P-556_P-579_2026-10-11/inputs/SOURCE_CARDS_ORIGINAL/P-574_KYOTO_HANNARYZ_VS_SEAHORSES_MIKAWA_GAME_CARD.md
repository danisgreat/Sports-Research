<!-- BEGIN CARD P-574 -->
## Card · P-574 · BASKETBALL / JAPAN B.LEAGUE PREMIER · SeaHorses Mikawa @ Kyoto Hannaryz · 2026-10-11

- **Working ID:** `P-574 — LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT`
- **Event key:** `BPREMIER:2026-27:506458:2026-10-11`
- **Native event ID:** `506458` (official B.LEAGUE ScheduleKey)
- **Sport:** `Basketball`
- **League:** `Japan B.LEAGUE PREMIER, 2026-27 regular season` (new competition format; **not** a historical B1 league profile)
- **Tracking alias:** `LOCAL-20261011-P-574-BPREMIER-MIK-KYO`
- **Analysis status:** `UNCALIBRATED_ANALYST_SCENARIO`
- **Timing state:** `PREGAME`
- **Research completed:** `2026-10-11T16:36:20+11:00` (research snapshot before scheduled tip; no result/live-play input)
- **Scheduled start:** `2026-10-11T17:35:00+11:00` (`2026-10-11T14:35:00+09:00` JST)
- **Endpoint:** `Full game including any five-minute overtime periods; final scores and no tied terminal game. All picks in this card use this endpoint. Operator void/action rules unverified.`
- **Distribution object:** `BPREMIER_PACE_EFFICIENCY_GAUSSIAN_MIX_OT_v1` — 73.513 regulation possessions/side; base regulation means KYO 81.538/MIK 82.252, total 163.790, MIK−KYO margin +0.715; joint Gaussian regulation total SD 19.0, margin SD 13.8, total-margin correlation 0; provisional 86% standard, 7% Kyoto −5, 7% Mikawa −5 point rotation states; rounded integer scoring; regulation-tie ≈2.852% with ~19-point OT extension and guaranteed winner; fixed-seed n=1,300,000.
- **Expected score:** `points, full game including OT; Monte Carlo SDs on unconditional full-game mixture` — Kyoto Hannaryz `81.45 (SD 11.94)` · SeaHorses Mikawa `82.18 (SD 11.93)` · total `163.63 (SD 19.36)` · margin `Mikawa − Kyoto +0.73 (SD 13.97)`.
- **Regime flags:** `EARLY_SEASON,RULE_CHANGE:on_court_free` — new B.PREMIER roster/on-court regime; no approved empirical multiplier for this league, so no unsupported total shift.
- **Retirement rule:** `N/A` (basketball)
- **Listed-pitcher rule:** `N/A` (basketball)
- **Abandonment rule:** `FRAMEWORK_DEFAULT: abandoned/cancelled game without official terminal result is VOID, or evaluated on the documented official endpoint if resumed; named operator's action terms not available.`
- **Settlement fields:** `Full-time team points and overtime/quarter periods; official FINAL event state; active player list and start indicator when published (B.LEAGUE game 506458 official box score / matchcentre; independent secondary if official unavailable).`
- **Capture due:** `2026-10-12T12:00:00+11:00` (within 36 h of scheduled start)
- **Rules read:** `CURRENT_STATE; METHOD; CURRENT_RULES §§1–10; SELECTION_RULES §§1–6; CARD_AND_LOG_TEMPLATES §§3–4,3a,7; RULES_BASKETBALL §0 and §§3–5,8–9; PROBABILITY_TOOLKIT §§1,1.2,1.3; BASE_RATES_REGISTER §§3,7.1 (cross-league structure only); LEAGUE_PROFILES Basketball (B.PREMIER not listed, no borrowed SD); SOURCES §3.2 (official B.LEAGUE used as field owner); ARCHIVE_USE_GUIDE §§1–5; official B.LEAGUE 2026–27 rule notices.`
- **Archive check:** `ARCHIVE_UNAVAILABLE: Previous Sports Results/Basketball/B League/2024/2024_games.csv and 2025/2025_games.csv each contain header only (0 data rows); 2026/2026_games.csv is missing (404). Current B.PREMIER has no eligible league row in LEAGUE_PROFILES, so historical B1 and NBA/NBL SDs were NOT labeled a B.PREMIER league benchmark. Fallback: official team 2025–26 B1 and 2026–27 B.PREMIER box-derived per-game statistics (6 Kyoto/5 Mikawa new-season games). R1 prior level only partial; R2 team rate from official aggregates, R6 rest and R7 home-court scenario; no archive game-event match or 2026 league-wide empirical total SD. Width an explicitly unvalidated analyst assumption.`
- **Evidence quotes:** `Official B.LEAGUE fixture @ 2026-10-11T16:32+11:00 — "2026.10.11（日）" / "14:35 TIP OFF"; official Kyoto club statistics @ 2026-10-11T16:33+11:00 — "2026-27  | BP  | 5  | 1  | 83.5  | 77.7"; official Mikawa club statistics @ 2026-10-11T16:33+11:00 — "2026-27  | BP  | 3  | 2  | 88.4  | 80.4"; club Kyoto column @ 2026-10-11T16:34+11:00 — "開幕から６戦を終え、5勝１敗"; official B.LEAGUE 2024 policy — "B.LEAGUE PREMIERはオンザコートフリーで決定". Exact starter/medical news: NOT_VERIFIED, not asserted.`

### Decision block

**Distribution:** `BPREMIER_PACE_EFFICIENCY_GAUSSIAN_MIX_OT_v1` — regulation 73.51 possessions × opponent-adjusted/shrunk team PPP (Kyoto 1.08875, Mikawa 1.11888) plus Kyoto's explicit +1.5 home-points assumption; correlated team-score normal (reg total SD 19.0, margin SD 13.8), unconfirmed rotation mixture, rounded scores and OT on tied regulation. Full-game total expected 163.63 (SD 19.36), margin Mikawa−Kyoto +0.73 (SD 13.97). Probability ceiling 90%, so no row above it is selected.

| Rank | Role | Tag | Proposition | p_card | Probability status | Evidence | Failure route |
|---|---|---|---|---|---|---|---|
| 1 | PICK | ANALYST_DERIVED (replaces supplied total Over 163.5 threshold) | Combined total **Over 139.5 points** — full game including OT | 89.4% | FROM_DISTRIBUTION:BPREMIER_PACE_EFFICIENCY_GAUSSIAN_MIX_OT_v1 | Official 6-/5-game shooting/possessions data; 163.63 centre; no league benchmark | Severe shot-conversion collapse or slower possessions, ≤139 total |
| 2 | PICK | ANALYST_DERIVED (replaces supplied total Under 163.5 threshold) | Combined total **Under 187.5 points** — full game including OT | 89.2% | FROM_DISTRIBUTION:BPREMIER_PACE_EFFICIENCY_GAUSSIAN_MIX_OT_v1 | Wide 19.36-point total SD; modest 73.51-possession pace | Exceptional perimeter efficiency, transition tempo or OT pushes total ≥188 |
| 3 | INFORMATIONAL | ANALYST_DERIVED (replaces supplied Mikawa −3.5 threshold) | SeaHorses Mikawa **+14.5 points** — full game including OT | 87.8% | FROM_DISTRIBUTION:BPREMIER_PACE_EFFICIENCY_GAUSSIAN_MIX_OT_v1 | Mikawa 2025–26 43–17; current scoring profile 88.4 PPG; projected near-even margin | Kyoto wins by 15+ via Mikawa turnover or 3P failure |
| 4 | INFORMATIONAL | ANALYST_DERIVED (replaces supplied Kyoto −3.5 threshold) | Kyoto Hannaryz **+14.5 points** — full game including OT | 85.5% | FROM_DISTRIBUTION:BPREMIER_PACE_EFFICIENCY_GAUSSIAN_MIX_OT_v1 | Kyoto home, 5–1 current record and rebound profile; projected near-even margin | Mikawa wins by 15+ with 3P/inside mismatch |

**P(Rank 1 and Rank 2 both lose):** `0.0% by construction` — Rank 1 loses if total ≤139; Rank 2 loses if total ≥188. Those events are mutually exclusive, not independent.

**Rank 1 − Rank 2 gap:** `0.3 percentage points` (89.4−89.2 after 1-decimal rounding).

**Rank-1 gate:** `RANK1_UNSTABLE` — p_card 89.4%; best non-complementary alternative 89.2% (Under 187.5); margin +0.3 percentage points <4.0. Official starting fives/complete game-day injury statuses unavailable, so no high-confidence first-ranked call.

**Adjustment dependence:** `NONE` — Kyoto home adjustment +1.5 points is 0.08 total SD / 0.11 margin SD (<0.25); the early-season 20% prior blend and rotation mixture are disclosed model assumptions, not certified fitted effects.

**Supplied rows not selected:** `SeaHorses Mikawa −3.5 42.8%; Kyoto Hannaryz −3.5 38.7%; Combined total Over 163.5 points 50.0%; Combined total Under 163.5 points 50.0%`. User's wording "Runs" on basketball totals is interpreted as **points**, not baseball runs. The two negative spread rows are NOT complements; 18.5% of the modeled margin interval [−3,+3] makes both lose.

**Potential winner:** `SeaHorses Mikawa — 52.1%` (full game including OT; Kyoto 47.9%, no terminal draw). **Not a strong winner call.**

### Appendix

#### A1. Identity, timing and state
- Field owner: https://www.bleague.jp/game_detail/?ScheduleKey=506458&tab=1; B.PREMIER, Sunday October 11 2026, Kyoto HOME / Mikawa AWAY, Nissin Denki Arena Kyoto (Kyoto City Gymnasium). Official `14:35 JST` is exactly `17:35 AEDT`.
- Research timestamp 2026-10-11T16:36:20+11:00, 58m 40s before scheduled tip. Fixture source showed pregame `--` for both sides; **no observed in-game score, odds, market prices, win tips or live play were consumed**. Later page refreshes/results must not backfill this card.
- Official club team-rate pages had `2026年10月10日21:48更新`, hence preceded this event.
- Pre-tip confirmed starting fives: **NOT_VERIFIED**. Game-day official active list: **NOT_VERIFIED**. Official up-to-date team medical reports: **NOT_VERIFIED**. This is an uncalibrated *pregame* scenario with roster mixtures, not a lineup-certified forecast.
- Previous result (Oct 9, per official club pages): Kyoto beat Yokohama B-Corsairs 74–73 at home; Mikawa lost 90–105 at Sendai. Both last played Oct 9, so neither is on a back-to-back; Mikawa's away travel exists but magnitude not quantified. Their short windows (6/5 games) have high uncertainty.

#### A2. Supplied contracts (reference only, Rule P4)
| Supplied | Literal target interpreted | Probability / settlement | Status |
|---|---|---:|---|
| Seahorses −3.5 | Mikawa wins by at least four points, full incl. OT | 42.8%; complement Kyoto +3.5 is 57.2% (note: opponent +3.5 is not its complement) | PROVIDED_REFERENCE |
| Hannaryz −3.5 | Kyoto wins by at least four points, full incl. OT | 38.7%; complement Mikawa +3.5 = 61.3% | PROVIDED_REFERENCE |
| Total Over 163.5 "Runs" | Basketball points at least 164 | 50.0% | PROVIDED_REFERENCE / unit corrected |
| Total Under 163.5 "Runs" | Basketball points at most 163 | 50.0% | PROVIDED_REFERENCE / unit corrected |

#### A3. Evidence and availability
| Variable | Official pregame value | Model implication / limitation |
|---|---|---|
| Kyoto W–L | 5–1 in B.PREMIER; prior 2025–26 B1 20–40 | Small new-season sample; new league on-court rules and roster mean old season is a lightly weighted prior only |
| Mikawa W–L | 3–2 in B.PREMIER; prior B1 43–17 | Better historical results but no raw win%→margin conversion |
| Kyoto scoring | PPG 83.5; opponent 77.7; FGA 64.2; ORB 15.5; TO 16.7; FTA 23.5; 3PA 25.8, 3P 29.0% | Strong offensive rebounds, relatively low 3P accuracy, high turnovers; short-sample exposure |
| Mikawa scoring | PPG 88.4; opponent 80.4; FGA 69.6; ORB 12.4; TO 8.6; FTA 17.6; 3PA 28.0, 3P 36.4% | Lower turnovers, greater shooting volatility on 28 threes/game |
| Kyoto principal usage (per game) | Charles Jackson 19.2 PPG /29:12 min, 13.5 RPG /4.5 APG; Angelo Caloiaro 16.7 PPG /31:01, 7.3 RPG/4.3 APG; Ryuichi Kishimoto 10.3 PPG /23:35, 1.7 RPG/3.3 APG | Season rotation, **not** confirmation that each is active or starts today |
| Mikawa principal usage (per game) | Sean O'Mara 16.8 PPG /28:53, 10.0 RPG/1.8 APG; Yudai Nishida 16.6 PPG /27:23, 2.6 RPG/2.6 APG; Davante Gardner 15.6 PPG /27:40, 7.8 RPG/3.2 APG | Season rotation, **not** confirmation that each is active or starts today |
| Rest / venue | Each last played Oct 9; Kyoto remains at home; Mikawa last played at Sendai | No invented fatigue penalty; Kyoto home-point component +1.5 analyst scenario |
| League change | B.PREMIER inaugural 2026–27; 2024 official rules notice establishes unlimited simultaneous foreign-player use ("on-court free") | Historical B1 player-minute split/roster strength cannot be assumed unchanged; new league multiplier NOT_ESTIMATED |
| Missing | Official starting fives, day-of active roster, complete game-day injury status, opponent-adjusted tracking possessions and B.PREMIER empirical scoring SD | Core evidence gate partial; no confident team-specific availability effect asserted |

#### A4. Reproducible score distribution and expected-score working
**Exposure formula:** `poss/G ≈ FGA − offensive rebounds + turnovers + 0.44 × FTA`. Each recorded pace is corrected for team player-minutes in games with overtime (`200 / team-minutes`), then 80% new-season +20% prior-season pace. 2025–26 B1 is a low-weight structural prior, **not** a new-league replacement distribution.

| Quantity | Current 2026–27 | Prior B1 2025–26 | Working value |
|---|---:|---:|---:|
| Kyoto raw possessions proxy | 64.2 − 15.5 + 16.7 + 0.44×23.5 = **75.740** | 63.3 − 12.4 + 14.7 + 0.44×16.6 = **72.904** | 40-min corrected blend **73.846** |
| Mikawa raw possessions proxy | 69.6 − 12.4 + 8.6 + 0.44×17.6 = **73.544** | 64.4 − 10.4 + 10.9 + 0.44×16.2 = **72.028** | 40-min corrected blend **73.181** |
| Pace forecast | — | — | (73.846+73.181)/2 = **73.513 possessions per side in 40 min** |
| Kyoto offence PPP (80/20 prior) | 83.5/75.740=1.1024 | 74.7/72.904=1.0246 | **1.086892** |
| Kyoto conceded PPP (80/20 prior) | 77.7/75.740=1.0259 | 81.2/72.904=1.1138 | **1.043461** |
| Mikawa offence PPP (80/20 prior) | 88.4/73.544=1.2020 | 83.8/72.028=1.1634 | **1.194289** |
| Mikawa conceded PPP (80/20 prior) | 80.4/73.544=1.0932 | 77.8/72.028=1.0801 | **1.090606** |

- **Matchup PPP:** Kyoto `(1.086892+1.090606)/2=1.088749`; Mikawa `(1.194289+1.043461)/2=1.118875`. These are simple opponent-defence averages, **not fitted opponent-strength regressions**. They are exposed to early schedule strength.
- **Regulation means:** Kyoto `73.513345×1.088749 +1.5 home points=81.5376`; Mikawa `73.513345×1.118875=82.2522`. Regulatory total `163.7898`, Mikawa−Kyoto margin `+0.7147`. Home-point adjustment `+1.5` is analyst judgment, not fitted; no rest adjustment.
- **Joint regulation object:** sample total `T_reg ~ Normal(163.7898, 19.0²)` and away–home margin `M_reg ~ Normal(+0.7147, 13.8²)` independently. Side scores `(T±M)/2` are rounded to nonnegative integers. Induced team SD before shock `sqrt((19²+13.8²)/4)=11.743`; induced score correlation `(19²−13.8²)/(19²+13.8²)=+0.309`.
- **Roster uncertainty (unconfirmed starters):** scenario probability 0.86 normal rotation, 0.07 Kyoto −5 points, 0.07 Mikawa −5 points; those are illustrative exposure-risk weights, **NOT confirmed scratches**. Their rotation-mixture adjustment reduces regulation total mean by 0.70 to 163.09 and raises width; conditional absences should trigger addendum/reforecast.
- **OT:** under B.LEAGUE 40-minute (4×10) rules, a regulation tie enters five-minute overtime and cannot remain terminally tied; the rounded-score distribution reaches a tie **2.852%** of the time. An OT adds about 9.5±3.3 points/side, and any residual tie is resolved in an additional integer-point branch (proxy for repeated OT). This is a simplified extra-period kernel, not a fitted minute-by-minute model. Unconditional OT total contribution is approximately `0.02852 × 19 ≈ +0.542 points`. The emitted model therefore has full-game expected total `163.63`, not the 163.79 unshocked regulation centre.
- **Full-game simulation:** seed `57420261011`, N=1,300,000; expected Kyoto 81.4493, Mikawa 82.1772, total 163.6264; Mikawa−Kyoto +0.7279; SDs Kyoto11.9422, Mikawa11.9280, total19.3570, margin13.9675; correlation +0.3152. `E[total]=E[Kyoto]+E[Mikawa]=163.6264` and `E[margin]=82.1772−81.4493=+0.7279`. Using total/margin SDs implies individual SD `sqrt((19.357² + 13.968²)/4)=11.93`, consistent with Monte Carlo team SDs.
- **Winner:** P(Mikawa>Kyoto) 0.520959; P(Kyoto>Mikawa) 0.479041, terminal draw exactly zero. In the supplied winner-relative points, `P(Mikawa margin≥4)=0.427593`, `P(Kyoto margin≥4)=0.387411` — do not confuse these with complements. The remaining central mass is the margins −3 to +3 (`18.5%`).
- **Width honesty:** B.PREMIER has **no registered empirical total/margin SD**, so 19.0 and 13.8 are conservative judgment widths, **not** NBA, NBL, EuroLeague or historic B1 estimates smuggled in as league-calibrated. The resulting numbers are descriptive scenarios only.

#### A5. Priced ladder, complements and monotonicity
Same full-game distribution and same draw-resolving overtime kernel for every row (percentage rounded to one decimal).

| Family and line | Left proposition | P(left) | Complement | P(complement) |
|---|---|---:|---|---:|
| Total 139.5 | Over 139.5 | 89.4% | Under 139.5 | 10.6% |
| Total 140.5 | Over 140.5 | 88.5% | Under 140.5 | 11.5% |
| Total 163.5 | Over 163.5 | 50.0% | Under 163.5 | 50.0% |
| Total 186.5 | Under 186.5 | 88.1% | Over 186.5 | 11.9% |
| Total 187.5 | Under 187.5 | 89.2% | Over 187.5 | 10.8% |
| Total 188.5 | Under 188.5 | 90.03% UNELIGIBLE | Over 188.5 | 9.97% |
| Mikawa +14.5 | Mikawa +14.5 | 87.8% | Kyoto −14.5 | 12.2% |
| Kyoto +14.5 | Kyoto +14.5 | 85.5% | Mikawa −14.5 | 14.5% |
| Mikawa −3.5 | Mikawa −3.5 | 42.8% | Kyoto +3.5 | 57.2% |
| Kyoto −3.5 | Kyoto −3.5 | 38.7% | Mikawa +3.5 | 61.3% |

`Over 138.5` ≈90.4% and `Under 188.5` ≈90.03% exceed the raw 90% p_card ceiling and are not eligible even when rounding could display 90.0%. `Mikawa +16.5` ≈90.4% is also over the ceiling. `Under 187.5` and `Over 139.5` form a strict total bracket: no total can fall both ≤139 and ≥188; P(both lose) exactly 0.

**Sensitivity/uncertain input:** If Mikawa's current 36.4% 3P success shrinks to 32.0% on 28.0 3PA, direct scored difference is `28.0×3×(0.320−0.364)=−3.696 points`. In an exploratory −4 point Mikawa scoring scenario on the same draws, Over139.5 drops 89.4→**85.1%**, Under187.5 rises 89.2→**92.5%**, Mikawa favourite falls 52.1→about **41%** after recalculating ties; the **top-two order reverses**, while their bracketing joint loss remains zero. Note: Under187.5 exceeding 90% in the sensitivity would be ineligible for a *new* card under p_ceiling; the issued baseline remains frozen. The sensitivity confirms material fragility to early-season 3P conversion.

#### A6. Adjustments and assumptions
| Name | Target | Size | SD units | Prior basis |
|---|---|---:|---:|---|
| Venue/home points | Kyoto regulation score mean | +1.5 points | +0.0775 total SD / +0.107 margin SD | analyst_judgement (not a calibrated B.PREMIER venue estimate) |
| Early-season cross-era prior | Season rates/pace | 80% 2026–27 B.PREMIER +20% 2025–26 B1 | rate mix, not additive SD | analyst_judgement; roster and format shifts limit prior relevance |
| Unconfirmed rotation | Team scores | 86% no shock /7% each side −5 points | conditional ±5, mixture-centre −0.70 total | analyst_judgement, not verified absences |
| Court composition rule | Width/caveat | No scored shift | 0 | official 2026–27 rule change; B.PREMIER effect not estimated |
| Travel/rest | Means | 0 | 0 | team match dates only; no invented magnitude |

**Adjustment dependence:** `NONE` for the formal above-0.25-SD single-adjustment trigger; **sensitivity-dependent ranking** remains explicit because 3P and rotation states can reverse the order. No adjustment or rule regime is performance-tested.

#### A7. Family checks and qualification
1. **BK-P1 league/clock/endpoint:** confirmed B.LEAGUE 2026–27 B.PREMIER regular season, 4×10 regulation, five-minute OT continuation, no regulation-only row; all four and supplied rows full-game.
2. **BK-P2 availability:** no verified game-day official starting fives, full active-roster box or complete injury bulletin at the research cutoff; **PARTIAL**. Published club seasonal player rows ≠ confirmed tonight. Model uses explicitly uncalibrated rotation states and avoids individual player props. An authoritative late availability update requires an addendum, not a rewritten card.
3. **BK-P3 phase:** full game only; no period/half derivatives; no completed phase at issue. **BK-P4:** on-field full game incl OT clear; commercial operator's void/action definition absent (`UNKNOWN_DEFINITION`), so no bet-settlement claim.
4. **Totals centre:** printed possessions 73.513 × both PPPs 1.08875/1.11888, +1.5 home = regulation 163.79; rotation −0.70, OT +0.54 ⇒ full-game 163.63; this is not a typed-in centre or a line/odds inference. 3P mix and foul-rate risks included via variance/sensitivity, not claimed deterministic outcomes.
5. **Width:** 19.36 total /13.97 margin; no B.PREMIER reference in LEAGUE_PROFILES. No NBA/NBL SD used as if league matched; unknown calibration is explicit. Early regime note `EARLY_SEASON,RULE_CHANGE:on_court_free` has **no** approved multiplier for this population.
6. **Selection:** four roles and non-increasing issued probabilities 89.4 ≥89.2 ≥87.8 ≥85.5; Rank1 ≥62%, but best non-complementary alternative 89.2 and lead +0.3pp => `RANK1_UNSTABLE`; Rank2 ≥58%; joint loss0.0%. The 90% ceiling excludes nearby stronger threshold candidates and makes the Rank1 gate unlikely to pass.
7. **Spread/winner single object:** P(Mikawa −3.5)=42.8%, P(Kyoto −3.5)=38.7%, Mikawa outright52.1%; two −3.5 supplied rows are NOT opposites. No crowding a favourite's spread via historical wins alone. Total Over/Under163.5 exactly 100%.
8. **Regime:** official 2026–27 inaugural B.PREMIER on-court free; prior-season B1 numbers 20% only, no unapproved numerical 2026 rule multiplier. Explicit changes in role allocation can matter and are included in uncertainty.
9. **Benchmark/source limitations:** no B.PREMIER LEAGUE_PROFILES row and no populated archived B League CSV; official two-team current stats are 11 team-games, small correlated samples, and no opponent-strength schedule adjustment fit. Neither rank nor winner is performance-certified.
10. **SPORTS_ONLY / MARKET_BLIND:** supplied contract lines used solely as scoring thresholds; no external market quotes, betting odds, tipsters, or forecast odds for probabilities.

#### A8. Source and reading receipt (field, lineage, time)
1. **Official event owner** B.LEAGUE https://www.bleague.jp/game_detail/?ScheduleKey=506458&tab=1 — identity, competition, venue, start, 5–1 vs 3–2, pregame state and point averages. Read 2026-10-11T16:32–16:35+11:00, site statistical update 2026-10-10 21:48 JST. One league-owner lineage.
2. **Kyoto official club stat page** https://www.bleague.jp/club_detail/?TeamID=699 — 2026–27 and 2025–26 PPG, concessions, FGA, ORB, TO, FTA, minutes, role/PPG/RPG/APG; read 16:33–16:35 AEDT; same upstream league lineage as #1, not independent.
3. **Mikawa official club stat page** https://www.bleague.jp/club_detail/?TeamID=728 — 2026–27 / 2025–26 full team stat rows, shots, usage minutes; read 16:33–16:35 AEDT, same league lineage.
4. **Kyoto original pregame team column**, dated 2026-10-10 https://hannaryz.jp/news/detail/id=24976 — 5–1, plan/Charles Jackson quotes and October 9 result; read 16:34+11:00. Original home-club statement; not verified day-of active list.
5. **League 2026–27 policy** https://www.bleague.jp/basketlive_news_detail/id=371340 — on-court free, new roster/format era, published 2024-02-28; read 16:33 AEDT. Rules owner.
6. **League duration explainer** https://www.bleague.jp/en/basketball_rule/ — four 10-minute quarters and nonterminal tie; read 16:33 AEDT. Relevant source, but not a bespoke 2026–27 rule packet.
7. **Official teams' match histories** https://www.bleague.jp/club_detail/?TeamID=699 and `TeamID=728` — Oct 9 outcomes, home/away/rest history; read 16:33 AEDT; league lineage.
8. **GitHub** `https://github.com/danisgreat/Sports-Research` `main` at SHA `33d0ea0c1c70056db7c7fb0a07dec77a633e573f` — CURRENT_STATE, METHOD v9.0, CURRENT_RULES, SELECTION_RULES, RULES_BASKETBALL, PROBABILITY_TOOLKIT §§1,1.2,1.3, BASE_RATES §§3,7.1, LEAGUE_PROFILES Basketball (no B.PREMIER row), SOURCES §3.2, ARCHIVE_USE_GUIDE, CARD_AND_LOG_TEMPLATES §3a and C1–C21; fetched 2026-10-11 during card research, GitHub read-only.
9. **Archive attempted and inspected:** `Previous Sports Results/Basketball/B League/2024/2024_games.csv` and `.../2025/2025_games.csv` (headers, zero game rows); `.../2026/2026_games.csv` (404); the fallback is official B.LEAGUE own team stats. These archives furnish no 2026–27 B.PREMIER empirical sample.
10. **Unverified:** day-of lineup five, complete actives, quantified injuries and late scratches; no false “confirmed” status. Contingency mixture and sensitivity substitute only for uncertainty, not facts.

#### A9. Integrity receipt
`READING_HEAD_SHA: 33d0ea0c1c70056db7c7fb0a07dec77a633e573f` · `EVENT_KEY_VERIFIED: 506458` · `RESEARCH_ISSUED_BEFORE_SCHEDULED_TIP: YES` · `TIMING: PREGAME` · `OBSERVED_IN_GAME_OUTCOME_USED: NO` · `SPORTS_ONLY_MARKET_BLIND: PASS` · `OFFICIAL_STARTERS: NOT_VERIFIED` · `OFFICIAL_ACTIVE_ROSTER: NOT_VERIFIED` · `BPREMIER_PROFILE: NOT_AVAILABLE` · `ARCHIVE: HEADER_ONLY_2024_2025` · `COMPUTATION: REPRODUCIBLE_UNCALIBRATED_SCENARIO` · `RANK1: RANK1_UNSTABLE` · `PERFORMANCE_ELIGIBILITY: NOT_CERTIFIED` · `SETTLEMENT: NOT_PERFORMED` · `CANONICAL_IMPORT: PENDING` · `GITHUB_WRITES: NO`.
<!-- END CARD P-574 -->
