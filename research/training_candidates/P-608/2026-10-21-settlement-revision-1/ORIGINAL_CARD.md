<!-- BEGIN CANONICAL RESEARCH P-608 -->
## P-608 — BASKETBALL / NBA preseason · Portland Trail Blazers @ Golden State Warriors · 2026-10-16 (US)
Import: 2026-10-21T01:07:13+11:00; prompt 4 NEW_CANONICAL_EVENT. Local event key `LOCAL-2026101679B3FBCC8D-G0008` → canonical **P-608**; native identity NBA 0012600019. Source mini `2026101679B3FBCC8D`, frozen source SHA-256 `b7478342e7ecba6861d9d79e4fc98b1dcd686356260f8b21911989847115ad7e` (313,155 bytes). Card core SHA-256 `ad1a5d60aa7eef21a957a37df137b9f5f2cd62330d669361ee26b98ac8b9b6e6` (25,868 bytes) = the exact bytes between the local BEGIN/END CARD marker lines (source offsets 218794–244662); markers and headings outside them remain in the preserved source. Original method, probabilities, ranks, statuses, timing and gaps are literal; any NOT_ASSIGNED / PENDING wording inside the core is historical. Import is not a forecast timestamp and confers no certification.

## Card · LOCAL-2026101679B3FBCC8D-G0008 · NBA PRESEASON · Portland Trail Blazers @ Golden State Warriors · 2026-10-17 AEDT

**Owner-entered request — verbatim available user message (literal Markdown line-break escapes normalised only for display):**

```text
[$github](app://connector_76869538009648d5b282a4bb21c3d157)
Upcoming game — BASKETBALL
- Competition details: <POR Trail-Blazers @ GS Waarriors, NBA Pre-Season>
- Scheduled start: <1:00 PM AEDT, 17 October 2026> (can be delayed, so continue research and processes as normal)
- Supplied contracts: <Blazers -1.5>, <Warriors +1.5>, <Combined Total Points: Over/Under 227.5 Points>
- Research constraints: <continue pre game research even if game starts, continue until research is properly done>
i need the probability issue and expected value as well based on research and/or processes in the github/ML/RL.
```

**Identity and custody:** NBA event 0012600019, POR (Portland Trail Blazers) away @ GSW (Golden State Warriors) home, NBA preseason 2026–27, 2026-10-16 19:00 PDT = 2026-10-17 13:00 AEDT, Chase Center, San Francisco. Stage exhibition, 48m regulation, both handicap/total assume FULL_GAME_INCL_OT and decimal point lines no pushes under this assumption. Operator source NOT_PROVIDED. Confirmed arena/event from NBA + Chase Center. Local event **candidate** `LOCAL-2026101679B3FBCC8D-G0008`; canonical **NOT_ASSIGNED** / PROMPT_4_IMPORT. New card **READ_ONLY_DRAFT / NOT_ISSUED / owner desktop active lease not verified**, full cumulative copy retained; no target-event outcome used; exact actual first play NOT_VERIFIED. Research timestamps below do not imply pre-start issuance.

### Decision summary (A1 / A2; qualitative policy classification)
The *highest analyst probability* is **GSW +1.5 59.28%**, followed by **Under 227.5 57.16%**. Neither is an issued primary pick or calibrated `p_card`. Expected points **Portland 110.79 / Golden State 113.28**, total **224.07**, mean GSW winning margin **2.49**. Real fitted ML/online expert aggregation NOT_EXECUTED; no frozen same-line baseline; given spread and total analyst computations for all directions. Pure sporting expectation, no financial EV without payout. Substantial rotation/preseason phase uncertainty; numbers are scenario estimates, not confidence-calibrated frequencies. The earlier 123–118 Portland victory is evidence once, not two independent H2H observations.

| Rank (analyst diagnostic ONLY) | Exact supplied row | p(Win) | W | L | Push | Void | W/(W+L) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 1 | GSW +1.5 | 59.28% | 59.28% | 40.72% | 0 | 0 | 0.592781 |
| 2 | Under 227.5 | 57.16% | 57.16% | 42.84% | 0 | 0 | 0.571630 |
| 3 | Over 227.5 | 42.84% | 42.84% | 57.16% | 0 | 0 | 0.428370 |
| 4 | POR -1.5 | 40.72% | 40.72% | 59.28% | 0 | 0 | 0.407219 |

**Unconditional action accounting:** for each half-point row above, under full game incl OT and assumed no void, W=p, L=1−p, P=0, V=0. Complementary lines pair to 1. `p_card=NOT_ESTIMATED` in primary model and all above are analyst p. Rank-1 original gate NOT_APPLICABLE_NO_PRIMARY (for display-only analyst ladder: leading p 59.28% and next noncomplement p 57.16%, lead 2.12 pp, provisional 0.62 floor not met). Original Rank 2 floor 0.58 may also fail. Head-to-head overlap and score–margin dependence mean no independence claim about simultaneous losses; frozen RET03/RET04/XCARD6 and BASE_ONLY shadows NOT_FROZEN_NO_PRIMARY.

### A1. Fixture, source authority and timing
- GitHub `danisgreat/Sports-Research` READ-ONLY, pinned `main` SHA `27e013c35477dbffb7b7699b269a0b978fb69b7f` (2026-10-16T15:20:39Z). Read `CURRENT_STATE`, `CURRENT_RULES`, `METHOD`, `SELECTION_RULES`, `RULES_BASKETBALL`, `LEAGUE_PROFILES`, `PRIMARY_PREDICTION_PROTOCOL`, `FORECAST_CYCLE_PROTOCOL`, `CARD_AND_LOG_TEMPLATES`, `research/prompts/COMMON_OPERATING_PROTOCOL`, `RESEARCH_COMPLETION_PROTOCOL`, `ROSTER_AVAILABILITY_PROTOCOL`, `HISTORICAL_SOURCE_PROTOCOL`, `MINI_LOG_IDENTITY_PROTOCOL`, `LEARNING_PIPELINE_PROTOCOL`. Model code was viewed only as repository source, not installed/executed. GitHub state highest P-600/next P-601 (context only; no P-ID consumed). Source publication known-at not fully proven for every historical row; receipt time 2026-10-17T12:59:39+11:00; user submission time not instrumented. Actual first play and pre-start issue certification UNKNOWN. No game result from the target ingested.
- Competition-specific receipt: NBA game https://www.nba.com/game/por-vs-gsw-0012600019 ; Golden State official scheduling https://www.nba.com/warriors/news/warriors-announce-2026-home-preseason-schedule-20260720 ; Chase Center https://chasecenter.com/events/20261016-gsw-vs-por/. The same fixture exists 7 Oct but is a DIFFERENT date/game ID: https://www.nba.com/game/por-vs-gsw-0012600033 . No target duplicate among seven accessible prior mini cards. Other parallel unpublished desktop minis and full canonical body unavailable; global duplicate gate not certified.

### A2. Four exact supplied directions, definition and scoring decision
- POR -1.5 POINTS: Portland final full game incl OT wins by >=2; victory requires margin POR−GSW > 1.5. p=40.72%, analyst only. If alternative operator excludes OT, must recompute from regulation distribution (NOT_PRICED_OWN_DEFINITION).
- GSW +1.5 POINTS: GSW wins outright or loses by exactly 1 on full-game scoreboard incl OT; p=59.28%, analyst only.
- Combined Over 227.5 POINTS, FULL_GAME_INCL_OT: final total >=228, p=42.84%, analyst only.
- Combined Under 227.5 POINTS, FULL_GAME_INCL_OT: final total <=227, p=57.16%, analyst only.
- All four W/L/P/V shown above. NO bookmaker contract, settlement text, prices or payout entered. Financial EV undefined; per-point expected values are shown. No model primary p, no fabricated odds, no actual-sports-result contamination.

### A3. Form windows and online history
Online historic route: NBA game centres, CBS, independent Basketball-Reference historical league/game schedules, previously published Portland coverage. **All windows overlapping diagnostics only; they cannot count as independent evidence.** The 40 prior team rows below are reconstructed in `HISTORICAL_GAME_OBSERVATIONS.csv` with dates, endpoint phase, true n, opponents and source URL. Older published scores were pre-event but exact first-publication/capture times and independent row-by-row collector confirmation remain incomplete. NO retired local game-result store was used. Mixed phase means the L20 mean is NOT fed directly as identical league training observations.

| Team | Window n | Points for | Points against | For/game | Against/game | Composition |
|---|---:|---:|---:|---:|---:|---|
| POR | 5 | 540 | 510 | 108.00 | 102.00 | EXHIBITION_NON_NBA:1, NBA_PLAYOFF:2, NBA_PRESEASON:2 |
| POR | 10 | 1090 | 1051 | 109.00 | 105.10 | EXHIBITION_NON_NBA:1, NBA_PLAYOFF:5, NBA_PRESEASON:2, NBA_REGULAR:2 |
| POR | 15 | 1678 | 1598 | 111.87 | 106.53 | EXHIBITION_NON_NBA:1, NBA_PLAYOFF:5, NBA_PRESEASON:2, NBA_REGULAR:7 |
| POR | 20 | 2255 | 2128 | 112.75 | 106.40 | EXHIBITION_NON_NBA:1, NBA_PLAYOFF:5, NBA_PRESEASON:2, NBA_REGULAR:12 |
| GSW | 5 | 555 | 520 | 111.00 | 104.00 | NBA_PRESEASON:5 |
| GSW | 10 | 1108 | 1110 | 110.80 | 111.00 | NBA_PLAYIN:2, NBA_PRESEASON:5, NBA_REGULAR:3 |
| GSW | 15 | 1651 | 1693 | 110.07 | 112.87 | NBA_PLAYIN:2, NBA_PRESEASON:5, NBA_REGULAR:8 |
| GSW | 20 | 2239 | 2297 | 111.95 | 114.85 | NBA_PLAYIN:2, NBA_PRESEASON:5, NBA_REGULAR:13 |

**Preseason-only check:** POR NBA-opponent n=2: PF 116.50 PA 108.00 per game, vs GSW Oct 7 123–118 and Sacramento Oct 13 110–98. London Lions exhibition 119–66 Oct 12 is real prior history in L5/L20 but NON_NBA_EXHIBITION, therefore EXCLUDED from NBA-calibration centre. GSW preseason n=5: PF 111.00 PA 104.00. Season 2025–26 overall regular-season PPG/OPPG: POR 115.5/115.8 and GSW 114.6/115.2, historical prior not same roster. Previous-season NBA Portland playoff and Warriors play-in games identified as separate phases. NBA preseason target has highly unstable minutes/lineups; 20-match n is not equal to 20 homogeneous fitted historical examples.

| Team | # | Date | Opponent | H/A/N | Team–opponent pts | Source phase | URL |
|---|---:|---|---|---|---|---|---|
| POR | 1 | 2026-10-13 | Sacramento Kings | A | 110–98 | NBA_PRESEASON | https://www.nba.com/game/por-vs-sac-0012600016 |
| POR | 2 | 2026-10-12 | London Lions | H | 119–66 | EXHIBITION_NON_NBA | https://www.blazersedge.com/gameday-coverage/117011/trail-blazers-portland-london-lions-final-score-stats-nba-preseason-today |
| POR | 3 | 2026-10-07 | Golden State Warriors | H | 123–118 | NBA_PRESEASON | https://www.nba.com/game/por-vs-gsw-0012600033 |
| POR | 4 | 2026-04-28 | San Antonio Spurs | A | 95–114 | NBA_PLAYOFF | https://www.basketball-reference.com/teams/POR/2026_games.html |
| POR | 5 | 2026-04-26 | San Antonio Spurs | H | 93–114 | NBA_PLAYOFF | https://www.basketball-reference.com/teams/POR/2026_games.html |
| POR | 6 | 2026-04-24 | San Antonio Spurs | H | 108–120 | NBA_PLAYOFF | https://www.basketball-reference.com/teams/POR/2026_games.html |
| POR | 7 | 2026-04-21 | San Antonio Spurs | A | 106–103 | NBA_PLAYOFF | https://www.basketball-reference.com/teams/POR/2026_games.html |
| POR | 8 | 2026-04-19 | San Antonio Spurs | A | 98–111 | NBA_PLAYOFF | https://www.basketball-reference.com/teams/POR/2026_games.html |
| POR | 9 | 2026-04-12 | Sacramento Kings | H | 122–110 | NBA_REGULAR | https://www.basketball-reference.com/teams/POR/2026_games.html |
| POR | 10 | 2026-04-10 | Los Angeles Clippers | H | 116–97 | NBA_REGULAR | https://www.basketball-reference.com/teams/POR/2026_games.html |
| POR | 11 | 2026-04-08 | San Antonio Spurs | A | 101–112 | NBA_REGULAR | https://www.basketball-reference.com/teams/POR/2026_games.html |
| POR | 12 | 2026-04-06 | Denver Nuggets | A | 132–137 | NBA_REGULAR | https://www.basketball-reference.com/teams/POR/2026_games.html |
| POR | 13 | 2026-04-02 | New Orleans Pelicans | H | 118–106 | NBA_REGULAR | https://www.basketball-reference.com/teams/POR/2026_games.html |
| POR | 14 | 2026-03-31 | Los Angeles Clippers | A | 114–104 | NBA_REGULAR | https://www.basketball-reference.com/teams/POR/2026_games.html |
| POR | 15 | 2026-03-29 | Washington Wizards | H | 123–88 | NBA_REGULAR | https://www.basketball-reference.com/teams/POR/2026_games.html |
| POR | 16 | 2026-03-27 | Dallas Mavericks | H | 93–100 | NBA_REGULAR | https://www.basketball-reference.com/teams/POR/2026_games.html |
| POR | 17 | 2026-03-25 | Milwaukee Bucks | H | 130–99 | NBA_REGULAR | https://www.basketball-reference.com/teams/POR/2026_games.html |
| POR | 18 | 2026-03-23 | Brooklyn Nets | H | 134–99 | NBA_REGULAR | https://www.basketball-reference.com/teams/POR/2026_games.html |
| POR | 19 | 2026-03-22 | Denver Nuggets | A | 112–128 | NBA_REGULAR | https://www.basketball-reference.com/teams/POR/2026_games.html |
| POR | 20 | 2026-03-20 | Minnesota Timberwolves | A | 108–104 | NBA_REGULAR | https://www.basketball-reference.com/teams/POR/2026_games.html |
| GSW | 1 | 2026-10-13 | Los Angeles Lakers | A | 101–89 | NBA_PRESEASON | https://www.cbssports.com/nba/teams/gs/golden-state-warriors/schedule/preseason/ |
| GSW | 2 | 2026-10-10 | Sacramento Kings | H | 111–106 | NBA_PRESEASON | https://www.cbssports.com/nba/teams/gs/golden-state-warriors/schedule/preseason/ |
| GSW | 3 | 2026-10-07 | Portland Trail Blazers | A | 118–123 | NBA_PRESEASON | https://www.nba.com/game/por-vs-gsw-0012600033 |
| GSW | 4 | 2026-10-06 | Los Angeles Lakers | H | 124–98 | NBA_PRESEASON | https://www.nba.com/team/1610612744/schedule |
| GSW | 5 | 2026-10-04 | Los Angeles Clippers | N | 101–104 | NBA_PRESEASON | https://www.cbssports.com/nba/teams/gs/golden-state-warriors/schedule/preseason/ |
| GSW | 6 | 2026-04-17 | Phoenix Suns | A | 96–111 | NBA_PLAYIN | https://www.basketball-reference.com/teams/GSW/2026_games.html |
| GSW | 7 | 2026-04-15 | Los Angeles Clippers | A | 126–121 | NBA_PLAYIN | https://www.basketball-reference.com/teams/GSW/2026_games.html |
| GSW | 8 | 2026-04-12 | Los Angeles Clippers | A | 110–115 | NBA_REGULAR | https://www.basketball-reference.com/teams/GSW/2026_games.html |
| GSW | 9 | 2026-04-10 | Sacramento Kings | A | 118–124 | NBA_REGULAR | https://www.basketball-reference.com/teams/GSW/2026_games.html |
| GSW | 10 | 2026-04-09 | Los Angeles Lakers | H | 103–119 | NBA_REGULAR | https://www.basketball-reference.com/teams/GSW/2026_games.html |
| GSW | 11 | 2026-04-07 | Sacramento Kings | H | 110–105 | NBA_REGULAR | https://www.basketball-reference.com/teams/GSW/2026_games.html |
| GSW | 12 | 2026-04-05 | Houston Rockets | H | 116–117 | NBA_REGULAR | https://www.basketball-reference.com/teams/GSW/2026_games.html |
| GSW | 13 | 2026-04-02 | Cleveland Cavaliers | H | 111–118 | NBA_REGULAR | https://www.basketball-reference.com/teams/GSW/2026_games.html |
| GSW | 14 | 2026-04-01 | San Antonio Spurs | H | 113–127 | NBA_REGULAR | https://www.basketball-reference.com/teams/GSW/2026_games.html |
| GSW | 15 | 2026-03-29 | Denver Nuggets | A | 93–116 | NBA_REGULAR | https://www.basketball-reference.com/teams/GSW/2026_games.html |
| GSW | 16 | 2026-03-27 | Washington Wizards | H | 131–126 | NBA_REGULAR | https://www.basketball-reference.com/teams/GSW/2026_games.html |
| GSW | 17 | 2026-03-25 | Brooklyn Nets | H | 109–106 | NBA_REGULAR | https://www.basketball-reference.com/teams/GSW/2026_games.html |
| GSW | 18 | 2026-03-23 | Dallas Mavericks | A | 137–131 | NBA_REGULAR | https://www.basketball-reference.com/teams/GSW/2026_games.html |
| GSW | 19 | 2026-03-21 | Atlanta Hawks | A | 110–126 | NBA_REGULAR | https://www.basketball-reference.com/teams/GSW/2026_games.html |
| GSW | 20 | 2026-03-20 | Detroit Pistons | A | 101–115 | NBA_REGULAR | https://www.basketball-reference.com/teams/GSW/2026_games.html |

### A4. Model attempts and expected score distribution
Central **UNCALIBRATED_ANALYST_SCENARIO / NOT_PRIMARY** (no executable fitted model). Deterministic recipe frozen before probability calculation:
- POR NBA-preseason matchup = (116.50 team scored +104.00 GSW allowed)/2 = **110.25**.
- GSW NBA-preseason matchup = (111.00 team scored +108.00 POR allowed)/2 = **109.50**.
- POR league-prior comparison = (115.5 POR 2025–26 scored +115.2 GSW 2025–26 allowed)/2 = **115.35**.
- GSW league-prior comparison = (114.6 GSW scored +115.8 POR allowed)/2 = **115.20**.
- Team expected final scores: **POR 0.60 × 110.25 + 0.40 × 115.35 − 1.50 assumed away adjustment = 110.79**; **GSW 0.60 × 109.50 + 0.40 × 115.20 + 1.50 home adjustment = 113.28**. The home ±1.50 is a *mean margin 3.0* total home-relative shift and is not fitted/venue-specific.
- μ_total = 224.07; μ_PORminusGSW = -2.49. Assume total SD **19.00 points** and margin SD **17.00 points** (heuristic; no fitting), normal tails, correlation between total and margin **not fitted**, full-game including OT. Sum and difference are treated as separate marginals consistent in their means; **no validated common joint scoring grid**.
- `p(GSW +1.5)=Φ((1.5−μ_PORminusGSW)/17)=0.59278149`; `p(POR −1.5)=1−that=0.40721851`.
- `p(Under 227.5)=Φ((227.5−μ_total)/19)=0.57163030`; `p(Over 227.5)=1−that=0.42836970`. Half-point lines have zero pushes under normal expected scoreboard and no void branch known.
- Machine roundoff ε substantially below 0.001, **structural/sampling uncertainty much larger**. No Monte Carlo claims, no correlations, fitted possession/shot, player-minute model, shot-inferred pace, overtime frequency, feedback losses or learned expert mixture. Not a model receipt. More precise display digits do not imply precision of the sporting assumptions. No immutable league-only `BASELINE_LEAGUE_V1` frozen; `BASELINE_P` MISSING, reason `NO_LEAGUE_PROFILE` for each supplied row (0/4). NO official banked ML/RL expected value.
- Exact `ml` attempt: `python -m ml capability --out CAPABILITY_RECEIPT.csv` returns `No module named ml`; `git ls-remote` cannot resolve github.com in local worker. Further `ml.workflow research`, `verify`, `ml ingest ... --dry-run` NOT_RUN because pinned checkout/model release not present. Captured in `MODEL_RUNTIME_ATTEMPT.json`; no invented EXECUTION.csv, expert weights, η, release/ledger/shadow or calibration.

### A5. Contract ranking / sensitivity / model uncertainty
| Sensitivity scenario | POR expected | GSW expected | POR −1.5 | GSW +1.5 | Over 227.5 | Under 227.5 |
|---|---:|---:|---:|---:|---:|---:|
| Central | 110.8 | 113.3 | 40.72% | 59.28% | 42.84% | 57.16% |
| Season prior heavy, w=0.30 | 112.3 | 115.0 | 40.31% | 59.69% | 49.60% | 50.40% |
| NBA preseason heavy, w=0.80 | 109.8 | 112.1 | 41.00% | 59.00% | 38.43% | 61.57% |
| No home shift | 112.3 | 111.8 | 47.68% | 52.32% | 42.84% | 57.16% |
| High GSW home shift | 109.3 | 114.8 | 34.05% | 65.95% | 42.84% | 57.16% |
| High-scoring +8 | 114.8 | 117.3 | 40.72% | 59.28% | 59.50% | 40.50% |
| Low-scoring -8 | 106.8 | 109.3 | 40.72% | 59.28% | 27.37% | 72.63% |
| Portland rotation boost +6 | 113.8 | 110.3 | 54.71% | 45.29% | 42.84% | 57.16% |
| GSW rotation boost +6 | 107.8 | 116.3 | 27.84% | 72.16% | 42.84% | 57.16% |
| Wide total/margin | 110.8 | 113.3 | 42.09% | 57.91% | 44.32% | 55.68% |
| Tight total/margin | 110.8 | 113.3 | 38.78% | 61.22% | 41.51% | 58.49% |

Data weighting, score environment, rotation, variance and home adjustment are **illustrative scenarios**, not statistical intervals and not empirically assigned scenario weights. Any row near 50% is substantially uncertain; projected stars can play 0–35 minutes independent of full-season PPG. Direction changes across scenarios. No numerical Rank-1 PASS or calibrated primary selection. Supplied complementary handicap rows have disjoint decisive losses (P(GSW+1.5 loses)=p(POR−1.5 wins)), and complementary totals too; cross-quantity co-loss under unknown correlation can only get **Fréchet bounds** [max(0,L_A+L_B−1), min(L_A,L_B)]. No protective joint-loss skill claim without a measured joint object.

### A6. Confirmed availability, bench and late-news attempts
- Portland: NBA reporting confirms Shaedon Sharpe unavailable with right knee issue. Previous Oct 12 team sheet had Damian Lillard and Robert Williams III resting; Oct 13 Lillard played, Deni Avdija scored 26, Ja Morant played second unit. These are previous-game statuses, NOT current-game confirmed active/minutes. Chris Youngblood calf issue previously ruled out Oct 13, current status not independently certified. Portland head coach Micah Nori rotated key starters in preseason. Confirmed exact-game starters, bench and scratch list NOT_VERIFIED.
- Golden State: Reuters Oct 15 reported Kristaps Porziņģis out indefinitely; other pregame reporting lists Jimmy Butler III (knee) and Moses Moody (knee) OUT for this fixture. Stephen Curry and Draymond Green are intended regular-season starter candidates but that is NOT an exact-game pretip confirmation. Coach Steve Kerr management of veteran minutes, Al Horford usage and small lineup experimental rotation changes material assumptions. **No exact-game confirmed starters/selected bench independent match-sheet proof.**
- Official matchup game centre and injury listing checked, independent journalistic reports for both teams, coach comments checked; exact NBA official 30-minute starting-lineup publication and same-day availability recheck NOT_CLOSED. Lineup/bench/inactive eligibility NOT_ESTABLISHED for all players. All health/rotation uncertainty remains an analyst sensitivity; it does not become learned feature effects.

### A7. Conditions, comparison, expected score and failure routes
Chase Center home GSW. Both 48m NBA exhibition context; less consistent rotations/motivation than regular season. Prior Oct 7 123–118 is same opponents but different venue, rosters/minutes not necessarily repeated. Last five GSW totals 205, 222, 241, 217, 190 (chronological reversed here: Oct4→Oct13). Portland two NBA opponent totals 241 and 208; London Lions 185 is an out-of-league noncomparable fixture. Scoring-environment mean around 224.1 is below line 227.5 but SD assumption high; high pace or garbage-time bench scoring easily flips. GSW+1.5 preferred by *the central heuristic only* and is far from proven edge. No financial EV because payout unspecified; if hypothetical decimal odds `d`, unit-stake cash EV = `p_win × (d−1) − (1−p_win)` (no pushes/voids) and fair break-even `d=1/p`, but **no odds were read, sought or used in model**.

### A8. Evidence, source routes, discrepancies and closure
**Actual opened/searched internet routes (note some `open` retrievals returned 403/cache miss even though search-visible text exists; do not claim successful independent collector reading):**
- https://www.nba.com/game/por-vs-gsw-0012600019
- https://www.nba.com/warriors/news/warriors-announce-2026-home-preseason-schedule-20260720
- https://www.nba.com/game/por-vs-gsw-0012600033
- https://www.cbssports.com/nba/teams/gs/golden-state-warriors/schedule/preseason/
- https://www.blazersedge.com/trail-blazers-analysis/117058/portland-trail-blazers-sacramento-kings-final-score-boxscore-lillard-morant-stats
- https://www.blazersedge.com/gameday-coverage/117011/trail-blazers-portland-london-lions-final-score-stats-nba-preseason-today
- https://www.basketball-reference.com/teams/POR/2026_games.html
- https://www.basketball-reference.com/teams/GSW/2026_games.html
- https://www.reuters.com/sports/warriors-kristaps-porzingis-out-indefinitely-due-health-issue--flm-2026-10-15/
- https://www.si.com/nba/scoreboard/trail-blazers-vs-warriors-10-16-2026-1487
- https://www.nba.com/team/1610612757/schedule
- https://www.nba.com/team/1610612744/schedule

- Match event `0012600019`, team aliases and 13:00 AEDT schedule verified by official NBA and Chase Center. NBA game IDs differ: historical POR@GSW on 7 Oct is `0012600033`, not same event.
- Independent history: NBA league team schedule and CBS/FOX match results corroborate GSW five preseason scores; Portland Oct 7 league box, Oct 12 coverage, Oct 13 coverage independently source visible. Basketball-Reference supplies old playoff/regular scores; source `open` returned 403, but search result excerpts contained dated rows. Mark prior 2026 rows **SEARCH_RESULT_VISIBLE / INDEPENDENT_RAW_CAPTURE_INCOMPLETE**. No bogus hash or definitive known-at claim; CSV has true n for each window but ML admission is QUARANTINED.
- Explicit unresolved: game-specific confirmed starters, bench/scratches and publication timestamps; possibility of Curry/Green/other rotation-rest decision; actual first tip; operator-specific OT action; possession/event pace for either team; pregame source publication/known-at proof for each older row; full competition-admitted 30+ historical research store; coach tactics quantification; independent source-lineage for all dated rows; owner laptop mini writer lease/duplicate inventory. Status **INFORMATION_INCOMPLETE**, source field closure partial only. Research completed as far as accessible public routes, not all missing facts established.

### A9. Execution, completion matrix and final audit
| Required research area | Work status | Evidence/limitation |
|---|---|---|
| 1 Identity / stage / venue / schedule | DONE | Official NBA and Chase Center sources; estimated 13:00 AEDT |
| 2 Official players / starters / bench | INCOMPLETE | Current team injury indications, coach projection; exact game confirmed lineups not independently found |
| 3 Historical L5/L10/L15/L20 both | RESEARCHED_SOURCE_CORROBORATION_INCOMPLETE | 40 dated team rows attached, overlapping phases, exact known-at/capture audit incomplete |
| 4 Exact competition season-to-date + pace / possession | PARTIAL | Five GSW and two POR vs NBA; opponent London separated; possession/rotation not verified |
| 5 Each supplied direction definitions + arithmetic | DONE_ANALYST_ONLY | All 4 directions, no pushes; operator actions ambiguous |
| 6 Model release / fitting / baseline | BLOCKED_WITH_ACTUAL_RECEIPT | Python no `ml` module; git DNS fail; no pinned checkout, 30 reviewed games or release |
| 7 Sensitivity, dependence and baseline reasons | DONE_ANALYST_ONLY | 11 regimes, Fréchet only for cross-quantity joint, no calibrated primary |
| 8 Learning export | QUARANTINE / PARTIAL | `HISTORICAL_GAME_OBSERVATIONS.csv` research ledger; exact `RESEARCH_EXPORT` missing capture hash/published time, not admissible |
| 9 Custody, issue and C1–C22 | DRAFT_ONLY | Seven earlier exact marked blocks preserved, no desktop lease, no issue/no settlement; primary/execution audit below |

**Audit C1–C22:** C1 identity PASS; C2 stage PASS; C3 duplicate PARTIAL; C4 timing UNVERIFIED_ACTUAL_TIP; C5 known-at PARTIAL; C6 exact players OPEN; C7 historic windows true n PASS_ARITHMETIC, SOURCE_REVIEW_OPEN; C8 pace/possession OPEN; C9 competition population OPEN; C10 contract definitions PARTIAL; C11 expected scores PASS_ANALYST; C12 probability four directions PASS_ANALYST; C13 W/P/L/V PASS_UNDER_ASSUMPTION; C14 sensitivity PASS; C15 primary execution FAIL_WITH_RECEIPT; C16 baseline 0/4 NO_LEAGUE_PROFILE; C17 selection gate nonprimary only; C18 seven previous original card markers BYTE_PRESERVED; C19 no P-ID PASS; C20 availability confirmation incomplete; C21 honest no-model status PASS; C22 complete cumulative separate draft readback pending independent file verification.

**Status:** READ_ONLY_DRAFT / NOT_ISSUED / LOCAL_RESEARCH_CONTINUATION / CYCLE_NO_MODEL / NOT_PRIMARY. The requested original active mini on desktop is not demonstrably writable; sandbox cumulative updated copy only. The uncalibrated results are not a frozen pretip forecast, not ML/RL weights, not a proper score entry, and not an authorized import. No GitHub writes; settlement NOT_PERFORMED.
<!-- END CANONICAL RESEARCH P-608 -->
