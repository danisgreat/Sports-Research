# PREDICTION MINI RUNNING LOG — FROM P-407

**Status:** ACTIVE LOCAL WORKING LOG  
**Created:** 2026-09-13T09:59:00Z / 2026-09-13 19:59 AEST  
**Google Drive access:** READ ONLY — no Drive files are modified by this log.  
**User-directed next working ID:** **P-407**  
**Drive canonical register observed:** `GAME_LOG_STATUS_CURRENT.md` currently ends at `P-371` and names `P-372` as the next canonical ID. Therefore `P-407+` in this mini-log is a **local/user-directed working sequence pending later reconciliation**, not a claim that Drive has already canonically assigned those IDs.

## PENDING SETTLEMENT — NEW P-407+ EVENTS

### P-407 — Club Brugge vs Royal Antwerp FC — Belgium Jupiler Pro League — PRE-MATCH / UNSETTLED

- **Scheduled start:** 2026-09-13 13:30 CEST / 21:30 AEST / 11:30 UTC
- **Forecast freeze:** approximately 2026-09-13 13:27 CEST / 21:27 AEST, before scheduled kickoff.
- **State at freeze:** SCHEDULED / PRE-MATCH. No live-match information used.
- **Venue:** Jan Breydel Stadium, Bruges.
- **Competition:** 2026-27 Jupiler Pro League, Matchday 6.
- **Working ID:** P-407 (local/user-directed; pending later canonical reconciliation).
- **Performance status:** LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE under the current Drive correction.
- **Settlement status:** PENDING. No retrospective performed.
- **Queue recheck 2026-09-13 23:24 AEST:** LIVE (Club Brugge 3-1 Royal Antwerp at retrieval); remains unsettled. No retrospective or grading performed.

#### Issued ranking

| Rank | Selection | `UNVALIDATED_SUBJECTIVE` probability | Evidence |
|---|---|---:|---|
| 1 | **Club Brugge team corners — Over 4.5** | **78%** | MEDIUM; direct official corner process, but confirmed XI not retrieved |
| 2 | **Royal Antwerp team goals — Under 1.5** | **74%** | MEDIUM-LOW; strong Club league defence, but Club defensive absences and XI uncertainty widen the tail |
| 3 | **1st Half total goals — Over 0.5** | **72%** | MEDIUM; current early-goal signal + longer-run first-half base rate, heavily shrunk |
| 4 | **Full match total goals — Under 3.5** | **68%** | MEDIUM; coherent with the same goal distribution as Rank 5 |
| 5 | **Full match total goals — Over 2.5** | **56%** | LOW-MEDIUM; preferred side of the supplied 2.5 line, but near the uncertainty band |

**Potential 90-minute winner:** Club Brugge — **60% `UNVALIDATED_SUBJECTIVE`**; Draw 22%; Antwerp 18%.  
**Central score corridor:** 2-1 Club Brugge, with 1-0 / 2-0 still material branches.  
**Important:** Rank 4 and Rank 5 are not complementary hedges. Both win on exactly three total goals; the common 3-goal state is intentionally carried in the joint distribution.

#### Participant / availability freeze

**Club Brugge same-day probable XI:** Sommer; Siquet, Lee Han-beom, Mechele, Seys; Potts, Vanaken?, Vetlesen; Forbs, Tresoldi, Virgili.

- Hans Vanaken: included in the match squad after hamstring stiffness/injury against Aston Villa; still a same-day starting/minutes question at the forecast freeze.
- Kyriani Sabbe: ruled out of the selection; recent groin/adductor/hamstring reporting agrees he is unavailable for this match. Hugo Siquet is the logical right-back replacement.
- Joel Ordóñez: not match fit following the metatarsal injury; not treated as an available starter.
- Club played Aston Villa on 8 September, five days before this match.

**Royal Antwerp same-day probable XI:** Nozawa; Renders, Van Helden, Cortés, Foulon; Somers, Vermeeren, Benítez, Salah; Fofana, Frey.

- No high-confidence official Antwerp absence was retrieved before the freeze.
- A lower-tier predicted-lineup page listed Carlos Mejia, Daam Foulon and Youssef Hamdaoui unavailable, but the fresher same-day HLN probable XI included Foulon. That conflict is preserved and **Foulon is not treated as a confirmed absence**.
- Antwerp's previous league game was at Standard on 5 September, giving them three additional rest days relative to Club.

**Confirmed XI status:** `XI_NOT_RETRIEVED_BEFORE_FREEZE`. The same-day probable XIs and Club squad selection were retrieved, but an official confirmed starting XI plus complete bench was not available in the research snapshot. Under `RULES_SOCCER.md`, this caps participant-dependent side/player outputs. No player prop is issued.

#### Competition-rules currency correction

The Drive's Belgian league section still describes the 2025-26 split system while noting an expansion for 2026-27. The field-owner Pro League confirms that **2026-27 uses 18 clubs, a classic 34-match regular season, and no playoffs; the bottom two are directly relegated**. This is a read-only observation for later reconciliation and belongs in `LEAGUE_RULES_SOCCER.md`; this mini-log does not edit Drive.

#### Current process evidence

**Official league record after five matches**
- Club Brugge: 4 W, 0 D, 1 L; 12 points; 9 scored, 2 conceded.
- Royal Antwerp: 2 W, 1 D, 2 L; 7 points; 10 scored, 10 conceded.

**Official season process statistics**
- Club Brugge: 1.8 goals/match; 11.2 shots/match; 5.4 shots on target/match; 65% possession; **9.4 corners/match**.
- Antwerp: 2.0 goals/match; 12.6 shots/match; 6.4 shots on target/match; 49% possession; **6.0 corners/match**.
- At OH Leuven, Club generated 28 shots, 60 penalty-area touches and **16 corners**.
- Even in the 2-1 loss at Gent, Club still won the corner count **5-1**.
- At Standard in Antwerp's most recent match, Antwerp lost 1-0; Standard produced 20 shots, 53 box touches, six big chances and **13 corners**, while Antwerp had four corners.

**First-half evidence**
- Current short-run cross-check: Club had scored in the first half in five straight league matches entering this game.
- Five-season Pro League first-half sample: Club Brugge matches had Over 0.5 first-half goals in 75.0% of 200 matches; Antwerp 69.5% of 200.
- Standard errors of those long-run rates are approximately 3.1 and 3.3 percentage points respectively.
- The current five-game streak is not assigned a coefficient; it is descriptive and reconciled against lineup/weather/current mechanisms.

**Full-match total evidence**
- Club's five league totals entering this game were 3, 3, 1, 3, 1: Over 2.5 in 3/5, all five Under 3.5.
- Antwerp's five league totals were 3, 3, 8, 5, 1: Over 2.5 in 4/5.
- These samples are very noisy: naive binomial SE is about 21.9 pp for Club's 3/5 and 17.9 pp for Antwerp's 4/5, so they do not justify a high-confidence 2.5-goal call.

#### Environment / current-surface gate

- Structured venue query at **Jan Breydel Stadium** at approximately 13:27 CEST: about **20°C, cloudy**; showers had occurred earlier.
- Independent Bruges hourly forecast around the game window: around 18-19°C, west/south-west winds roughly 13-17 km/h, with light drizzle possible from roughly 14:00-15:00.
- Belgian RMI/IRM national forecast: very cloudy with occasional light precipitation.
- Weather is treated primarily as **distribution width**, not as an automatic Under/Over sign. No pitch-condition report was recovered before the freeze.

#### Joint event object / arithmetic

**Goal centre**
- Club scoring-side base: midpoint of Club 1.8 GF/game and Antwerp 2.0 GA/game = **1.90**.
- Antwerp scoring-side base: midpoint of Antwerp 2.0 GF/game and Club 0.4 GA/game = **1.20**.
- Raw current-season centre = **3.10 goals**.
- Vanaken limited/absent branch lowers Club creation; Club's Sabbe/Ordóñez defensive branch raises Antwerp's transition/set-piece tail. These approximately offset at the centre rather than being treated as false precision.
- Early-season sample, Antwerp's 4-4/1-4 tail, Club's unusually low 0.4 GA/game, rain uncertainty and the five-day European turnaround are treated mainly as **width**.
- **Working subjective centre: ~3.0 goals; width: ~1.8 goals.**
- Normalised distance to 2.5 = |3.0-2.5| / 1.8 ≈ **0.28**.
- Normalised distance to 3.5 = |3.0-3.5| / 1.8 ≈ **0.28**.
- The different probabilities for O2.5 and U3.5 arise from the discrete **exactly-3-goals** state, which wins both contracts.

**Full-match goal-state masses**
- 0-1 total goals: 18%
- exactly 2: 26%
- exactly 3: 24%
- 4+: 32%
- Therefore: **O2.5 = 56%**; **U3.5 = 68%**.

**First-half goal-state masses**
- 0 first-half goals: 28%
- exactly 1: 44%
- 2+: 28%
- Therefore: **1H O0.5 = 72%**.

**Winner masses**
- Club Brugge regulation win: 60%
- Draw: 22%
- Antwerp regulation win: 18%

**Antwerp goal masses**
- 0: 38%
- 1: 36%
- 2+: 26%
- Therefore: **Antwerp U1.5 goals = 74%**.

**Club team-corner masses**
- 0-4: 22%
- 5-7: 42%
- 8+: 36%
- Therefore: **Club O4.5 corners = 78%**.

#### Complement / kill-path decomposition (`G-L9`)

| Selection | Win p | Complement | Main failure paths carried |
|---|---:|---:|---|
| Club O4.5 corners | 78% | 22% | early Club lead lowers attack demand; Antwerp prevents end-line/block sequences; personnel/weather/random set-piece variance |
| Antwerp U1.5 goals | 74% | 26% | transition efficiency through Frey/Fofana; set-piece/penalty event; Club defensive replacement/fatigue tail |
| 1H O0.5 | 72% | 28% | compact opening; Vanaken limitation reduces creation; finishing variance / wet-surface execution |
| U3.5 | 68% | 32% | early goal opens state; Antwerp's high-conversion tail persists; penalty/red-card/set-piece disruption |
| O2.5 | 56% | 44% | Club controls without conversion; Antwerp contributes little; match remains in 1-0 / 2-0 / 1-1 state |

**Top-two joint probability (`G-L10`):**  
`P(Club O4.5 corners ∧ Antwerp U1.5 goals) ≈ 60%` — **moderately positive coupling** because sustained Club territory can generate corners while suppressing Antwerp's possession/shot volume. This coupling disclosure does not reorder the marginal ranks.

#### Card completeness block

| Requirement | State |
|---|---|
| Identity / competition / time / venue frozen | PASS |
| 2026-27 competition rules re-verified at field owner | PASS; Drive correction noted read-only |
| Supplied contracts frozen | PASS |
| Exact source records + source roles recorded | PASS |
| Synthetic / prediction-content exclusion | PASS |
| L5 / current-season form and longer-run phase context | PASS, with small-sample uncertainty explicit |
| Starting XI + full bench | **PARTIAL — confirmed XI/bench not retrieved before freeze** |
| Injury / availability refresh | PASS with Antwerp conflict preserved |
| Outdoor venue weather/current-surface check | PASS WITH LIMITATION — venue query + RMI + hourly city cross-check; no pitch report |
| Goal / corner processes kept separate | PASS |
| Joint event masses / centre / width / normalised edges | PASS |
| Complement kill paths | PASS |
| `P(R1 ∧ R2)` + coupling | PASS |
| Small-sample SE where rates were used | PASS |
| Final volatile refresh | PASS at ~13:27 CEST |
| Settlement source named | PASS — official Pro League match centre controls score/corners; operator definition required for any non-standard offered market |

#### Sources used for P-407

| Source | Role / field | Grade in this card | Access snapshot |
|---|---|---|---|
| Google Drive `METHOD.md` | Governing lifecycle/probability/market-blind rules | GOVERNING | current Drive snapshot |
| Google Drive `CONTROLS.md` | G-L1/G-L2/G-L7/G-L8/G-L9/G-L10/G-L11, completeness | GOVERNING | current Drive snapshot |
| Google Drive `RULES_SOCCER.md` | Soccer-specific participant/goal/corner algorithm | GOVERNING | current Drive snapshot |
| Google Drive `LEAGUE_RULES_SOCCER.md` | Stored competition rules; stale Belgian 2025-26 split text identified | GOVERNING REFERENCE / CORRECTION NEEDED | current Drive snapshot |
| Pro League — 2026-27 format | Competition rules: 18 clubs, 34 matches, no playoffs | FIELD OWNER | 2026-09-13 pre-kickoff |
| Royal Antwerp FC official calendar | Fixture date/time and Antwerp schedule/rest | CLUB FIELD OWNER | 2026-09-13 pre-kickoff |
| Pro League — OH Leuven vs Club Brugge S2 | Club shots, box-entry/corner event chain and lineup | FIELD OWNER | 2026-09-13 pre-kickoff |
| Pro League — KAA Gent vs Club Brugge S4 | Club corner resilience / match process | FIELD OWNER | 2026-09-13 pre-kickoff |
| Pro League — Standard vs Antwerp S5 | Antwerp latest lineup, shots, box touches, corners; season aggregate | FIELD OWNER | 2026-09-13 pre-kickoff |
| Pro League — Kortrijk vs Antwerp S2 | Antwerp earlier lineup/process/corners | FIELD OWNER | 2026-09-13 pre-kickoff |
| HLN same-day probable lineups | Latest probable XI, Vanaken question, Foulon expected | REPUTABLE REPORTING / VOLATILE | published 2026-09-13 08:14 CEST |
| Club Brugge squad report / Club social embed | Vanaken included; Sabbe omitted | CLUB-SOURCE CORROBORATION VIA REPORT | published 2026-09-12 |
| VoetbalBelgie / Nieuwsblad corroboration | Ordóñez not match fit; Vanaken/Sabbe injury context | SECONDARY CORROBORATION | pre-kickoff |
| FirstHalfScore | Five-season Pro League first-half frequencies | HISTORICAL CROSS-CHECK | pre-kickoff |
| FootballZZ current statistical page | Short-run first-half/corner streak cross-check only | SECONDARY CROSS-CHECK; no prediction output used | pre-kickoff |
| Structured weather query — Jan Breydel Stadium | Exact venue current conditions | WEATHER FIELD | ~13:27 CEST |
| Belgian RMI/IRM | Official Belgian weather context | GOVERNMENT WEATHER | pre-kickoff |
| Bruges hourly weather cross-check | Game-window drizzle/wind detail | SECONDARY WEATHER | pre-kickoff |

#### Exact public URLs recorded

- https://www.proleague.be/nieuws/vanaf-seizoen-26-27-met-18-clubs-in-de-jupiler-pro-league
- https://www.proleague.be/nieuws/kalender-2026-2027-club-brugge-opent-tegen-kv-kortrijk-eerste-super-sunday-al-op-speeldag-4
- https://www.royalantwerpfc.be/nieuws/nieuws/kalender-jupiler-pro-league-2026-2027
- https://www.proleague.be/wedstrijden/seizoen-2026-2027-jupiler-pro-league-2-oh-leuven-vs-club-brugge-608
- https://www.proleague.be/wedstrijden/seizoen-2026-2027-jupiler-pro-league-4-kaa-gent-vs-club-brugge-629
- https://www.proleague.be/wedstrijden/seizoen-2026-2027-jupiler-pro-league-5-standard-de-liege-vs-royal-antwerp-fc-636
- https://www.proleague.be/wedstrijden/seizoen-2026-2027-jupiler-pro-league-2-kv-kortrijk-vs-royal-antwerp-fc-607
- https://www.hln.be/club-brugge/geraakt-hans-vanaken-fit-bij-club-brugge-daam-foulon-in-de-basis-verwacht-bij-antwerp-dit-zijn-de-vermoedelijke-opstellingen~a2bb4f1d/
- https://www.club-brugge.voetbalupdate.be/news/521248/avec-ou-sans-vanaken-leko-devoile-sa-selection
- https://www.voetbalbelgie.be/artikel/dan-toch-geen-transfer-voor-ordonez
- https://firsthalfscore.com/first-half-goals/belgium-pro-league
- https://footballzz.co.uk/head-to-head/2026-09-13/belgium/pro-league/club-brugge/royal-antwerp/MTAwMDctMTA3MjQ%3D
- https://nocdn.meteo.be/fr/belgique
- https://www.buluttan.com/weather/belgium/bruges

### P-408 — Coventry City vs Brighton & Hove Albion — English Premier League — PRE-MATCH / UNSETTLED

- **Scheduled start:** 2026-09-13 14:00 BST / 23:00 AEST / 13:00 UTC.
- **Forecast freeze:** 2026-09-13 13:52 BST / 22:52 AEST, approximately eight minutes before scheduled kickoff.
- **State at freeze:** SCHEDULED / PRE-MATCH. No post-kickoff or live-match evidence used.
- **Venue:** Coventry Building Society Arena, Coventry.
- **Competition:** 2026-27 English Premier League, Matchweek 4.
- **Working ID:** P-408 (local/user-directed; pending later canonical reconciliation).
- **Method:** MDS-2026.09.06-v4.0; SPORTS_ONLY / MARKET_BLIND.
- **Performance status:** LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE under the current Drive correction.
- **Settlement status:** PENDING. No retrospective performed.
- **P-408 queue recheck 2026-09-13 23:24 AEST:** LIVE, 0-0 at retrieval; remains unsettled. No retrospective or grading performed.

#### Issued ranking

| Rank | Selection | `UNVALIDATED_SUBJECTIVE` probability | Evidence |
|---|---|---:|---|
| 1 | **Brighton team corners — Over 3.5** | **75%** | MEDIUM; separate corner process with current volume + width/cross mechanism |
| 2 | **Brighton or Draw — Double Chance (90 min)** | **74%** | MEDIUM; stronger current chance creation but injury/away/home uncertainty retained |
| 3 | **1st Half total goals — Over 0.5** | **72%** | MEDIUM; early-goal mechanism present, not just streak continuation |
| 4 | **Coventry team goals — Under 1.5** | **68%** | MEDIUM-LOW; Coventry drought shrunk because recent xG is non-zero |
| 5 | **Full match total goals — Over 2.5** | **55%** | LOW-MEDIUM; only a small normalised edge, so probability remains near coin-flip |

**Potential regulation winner:** Brighton — **48% `UNVALIDATED_SUBJECTIVE`**; Draw 26%; Coventry 26%.  
**Central score corridor:** Coventry 1-2 Brighton; adjacent material states 1-1, 0-2 and 2-2.  
**Supplied-line calls:** 1H O0.5 = **OVER**; full-match 2.5 = **OVER**, but with substantially lower confidence.

If the available Brighton team-corner market begins at **4.5 rather than 3.5**, the preferred direction remains Over but the probability is reduced to approximately **66%**. The issued ranked contract is specifically **Brighton O3.5 team corners**.

#### Confirmed participants and bench

A same-day live report states that **both clubs field unchanged starting XIs from their previous league matches**. The current lineup page independently supplies the full matchday benches.

**Coventry — 3-4-2-1**
- GK: Carl Rushworth
- DEF: Aurèle Amenda, Bobby Thomas, Ethan Pinnock
- MID/WB: Milan van Ewijk, Frank Onyeka, Matt Grimes, Jay Dasilva
- AM: Jack Rudoni, Ephron Mason-Clark
- ST: Taiwo Awoniyi
- Bench: Daniel Bentley, Joel Latibeaudiere, Gustavo Hamer, Brandon Thomas-Asante, Caleb Yirenkyi, Tatsuhiro Sakamoto, Ellis Simms, Victor Torp, Loum Tchaouna.

**Brighton — 4-2-3-1**
- GK: Bart Verbruggen
- DEF: Ferdi Kadioglu, Luka Vušković, Lewis Dunk, Olivier Boscagli
- MID: Pascal Groß, Yasin Ayari
- AM: Diego Gómez, Malick Yalcouyé, Maxim De Cuyper
- ST: Charalampos Kostoulas
- Bench: João Costinha, Pascal Struijk, Jason Steele, Chema Andrés, Matt O'Riley, Nehemiah Oriola, Jaouen Hadjam, Ibrahim Osman, Promise David.

**Important availability consequences**
- Coventry are expected without **Haji Wright, Luke Woolfenden, Kaine Kesler-Hayden and Josh Eccles**; none appears in the matchday 20.
- Brighton's own pre-match report confirmed **Zadok Yohanna unavailable** and said Georginio Rutter and Femi Azeez might return if fit. Neither Rutter nor Azeez appears in the final matchday 20.
- Brighton also remain without the attacking/creative group **Kaoru Mitoma, Yankuba Minteh and Jack Hinshelwood**, while Mats Wieffer is also unavailable; none appears in the matchday 20.
- Evan Ferguson and Stefanos Tzimas are also absent from the matchday 20.
- Because the complete starting XIs and benches were recovered, `SO-P2` is treated as satisfied.
- No player prop is ranked: despite confirmed starters, no supplied player-stat contract/provider definition offered a cleaner probability than the five team/game markets.

#### Current form / continuity audit

**Coventry current 2026-27 competitive results**
1. Arsenal 3-0 Coventry — EPL
2. Plymouth 2-4 Coventry — EFL Cup
3. Coventry 0-1 Hull — EPL
4. Manchester City 1-0 Coventry — EPL

The headline “Coventry have not scored” applies to the **Premier League only**. Their current attackers scored four at Plymouth, including early goals by Awoniyi and Rudoni and a later Mason-Clark goal. This is why the EPL scoring drought is not treated as proof Coventry cannot score.

**Coventry L5 / L10 / L15 / L20**
- L5 (bridges May-to-August): **2W-0D-3L, 8-7 goals**.
- L10: **4W-3D-3L, 17-10 goals**.
- L15: **8W-3D-4L, 29-14 goals**.
- L20: **12W-4D-4L, 38-17 goals**.
- **Continuity verdict:** L10/L15/L20 are heavily contaminated by the 2025-26 Championship title run. Coventry changed division and personnel, so those strong longer windows are contextual priors only and carry no direct EPL coefficient.

**Brighton current-season L5, all competitions**
- Tromsø 0-0 Brighton
- Brighton 4-0 Aston Villa
- Brighton 4-0 Tromsø
- Chelsea 4-3 Brighton
- Brighton 1-1 Leeds
- L5: **2W-2D-1L, 12-5 goals**.

**Brighton longer trend**
- Last 10 league matches around the season boundary: mixed, approximately **4W-2D-4L**.
- Last 15 prior/current league window remains mixed rather than a simple “hot streak”.
- A 20-match league reference window is close to balanced (around eight wins, four-to-five draws, seven-to-eight losses depending the cutoff snapshot).
- **Continuity verdict:** Brighton have better same-competition continuity than Coventry, but summer transfers and the current injury cluster require current-XI weighting over old aggregate form.

**Head-to-head continuity**
- The clubs' last league meeting was in **December 2011**; their last meeting of any kind was an FA Cup tie in 2018.
- H2H therefore **fails the continuity gate for predictive weighting**. It is identity/history only, not a directional input.

#### Current chance / shot process

**Coventry EPL xG, consistent xGStat series**
- at Arsenal: **0.35 xG**
- vs Hull: **1.02 xG**
- at Man City: **1.05 xG**
- Mean = **0.81 xG/game**.
- Sample SE of the three-match mean ≈ **0.23 xG**.
- Coventry have scored 0 EPL goals from about **2.42 xG**, so the drought contains meaningful finishing variance.
- A separate Sky Sports provider graded the Man City match at **1.37 xG** for Coventry. Provider definitions are not merged; it is used only as directional corroboration that the City performance created real chances.
- Coventry won the corner count 5-4 at Man City and outshot the “zero-goal” narrative with 12 shots by the Sky feed.

**Brighton EPL attack**
- vs Aston Villa: about **3.69 xG**
- at Chelsea: about **1.57 xG**
- vs Leeds: about **2.20 xG**
- Mean ≈ **2.49 xG/game**; sample SE ≈ **0.63 xG**.
- Brighton's own club preview reports **7.4 total xG and 15 big chances**, both league-high at the pre-match freeze.
- The raw attack is therefore strong, but the final XI is missing Mitoma, Minteh and Hinshelwood, while Rutter/Azeez failed to make the bench. This is carried as a real downward participant adjustment rather than ignored.
- Brighton have allowed only **33 shots** through three league games, third-lowest by the club's official pre-match note, but their xGA has been volatile; defensive certainty is therefore not overstated.

#### Corner process — separate from goals

**Brighton EPL team corners:** 5 vs Aston Villa, 7 at Chelsea, 7 vs Leeds.
- Mean = **6.33 corners/game**.
- Sample SD ≈ 1.15; sample SE ≈ **0.67**.
- All three cleared 3.5, but n=3 is explicitly too small to be treated as a stable hit-rate coefficient.

**Coventry opponent corners:** 8 at Arsenal, 2 vs Hull, 4 at Man City.
- Mean allowed = **4.67/game**.
- High between-game variance; this is width, not a deterministic lean.

**Direct corner-causing mechanism**
- Brighton's official preview reports **71.6% average possession** and specifically notes Maxim De Cuyper has already made **29 passes into the box and seven successful crosses**, second only to Bruno Fernandes in the cited league comparison.
- Brighton's front/wide personnel is weakened, which prevents simply extrapolating 6.33 corners upward.
- Coventry's back-three/wing-back structure can concede sustained territorial attacks, but their Man City game also showed they can defend territory without automatically allowing a huge corner count.
- Working Brighton corner centre ≈ **5.4**, width ≈ **2.6**.
- State masses: 0-3 corners **25%**; 4-6 **48%**; 7+ **27%**.
- Therefore **Brighton O3.5 corners = 75%**.

#### Environment / surface gate

- Exact venue query at Coventry Building Society Arena near the forecast freeze: about **22°C, cloudy**, with a structured forecast showing possible showers around the game window.
- The **Met Office's City of Coventry Stadium** location is less wet at kickoff, showing sunny intervals and only about **10% precipitation probability from 14:00 onward**.
- The source disagreement is preserved. Weather therefore widens the distribution slightly but receives **no signed Over/Under coefficient**.
- No verified pitch-quality problem was recovered.

#### Joint goal object / explicit arithmetic

The calculation is deliberately subjective and transparent rather than pretending to be a fitted model.

**Coventry scoring centre**
- Coventry current own xG mean: **0.81**.
- Brighton current xGA has been much noisier and materially opponent-driven, so it is not copied directly into Coventry's expectation.
- Start from a reconciled current-event prior near **1.35** after considering Coventry's two latest ~1.0-xG displays and Brighton's variable chance concession.
- **−0.15** for Haji Wright unavailable / unchanged reduced attacking options.
- **−0.05** for Brighton's shot-suppression/territory profile.
- Coventry centre ≈ **1.15 goals** after rounding and uncertainty reconciliation.

**Brighton scoring centre**
- Brighton current own xG mean: **2.49**.
- Coventry current xGA environment has been roughly **1.7-1.8** per match on the consistent xG series.
- Reconciled prior ≈ **2.10**.
- **−0.30** for the missing attacking/creative group (Mitoma, Minteh, Hinshelwood; Rutter/Azeez not in matchday squad).
- **−0.05** for away/home-state uncertainty.
- Brighton centre ≈ **1.75 goals**.

**Total centre ≈ 2.90 goals; working width ≈ 1.90.**
- Normalised edge at 2.5: `|2.90 - 2.50| / 1.90 ≈ 0.21`.
- This is a **small edge**, so the full-match total probability is deliberately held near 50/50 rather than exaggerated.

**Full-match total state masses**
- 0-1 goals: **20%**
- exactly 2: **25%**
- exactly 3: **23%**
- 4+: **32%**
- Hence **Over 2.5 = 55%**.

**First-half state**
- Current league sequence: a first-half goal occurred in 5 of the six team-games making up Coventry's and Brighton's three EPL fixtures; Coventry-Hull was the exception.
- That 5/6 rate has a very large naive SE (~15 pp) and is not given a coefficient.
- Mechanism support: Brighton have league-leading current chance creation; Coventry conceded early to Arsenal and Man City; the unchanged starting XIs preserve the same basic attacking roles.
- Counterweight: Brighton's missing wide attackers and Coventry's ability to hold Hull 0-0 at HT.
- Working 1H centre ≈ **1.20 goals**, width ≈ **1.00**.
- State masses: 0 first-half goals **28%**; exactly 1 **43%**; 2+ **29%**.
- Hence **1H Over 0.5 = 72%**.
- Normalised distance to 0.5 ≈ `|1.20 - 0.50| / 1.00 = 0.70`.

**Winner state masses**
- Coventry regulation win: **26%**
- Draw: **26%**
- Brighton regulation win: **48%**
- Therefore Brighton-or-Draw = **74%**.

**Coventry goal state**
- 0 goals: **34%**
- exactly 1: **34%**
- 2+: **32%**
- Therefore Coventry Under 1.5 team goals = **68%**.

#### `G-L1` representative compatibility state

Representative Rank-1-compatible state:
- **HT:** Coventry 0-1 Brighton
- **FT:** Coventry 1-2 Brighton
- **Brighton corners:** 6

Under that one representative state:
- Brighton O3.5 corners wins;
- Brighton/Draw wins;
- 1H O0.5 wins;
- Coventry U1.5 team goals wins;
- O2.5 goals wins.

This is a compatibility demonstration only. It did **not** generate or force the five rankings.

#### Complement / kill-path decomposition (`G-L9`)

| Selection | Win p | Complement | Main failure paths |
|---|---:|---:|---|
| Brighton O3.5 team corners | 75% | 25% | early Brighton scoring reduces later territory; Coventry defend without blocks/end-line concessions; missing Brighton natural width suppresses delivery volume |
| Brighton or Draw | 74% | 26% | Coventry's home attack converts the chances it has been missing; Brighton's injury-reduced attack under-converts; set-piece edge from Coventry |
| 1H O0.5 | 72% | 28% | Coventry compact start; weakened Brighton wide creation; early finishing variance; wet-surface uncertainty |
| Coventry U1.5 team goals | 68% | 32% | regression from 0 goals/2.42 xG arrives strongly; Awoniyi/Rudoni/Mason-Clark recreate the Plymouth or Man-City chance volume; Brighton xGA volatility persists |
| O2.5 total goals | 55% | 45% | Brighton injury load lowers finishing; Coventry remain inefficient; match settles in 0-1, 1-1 or 0-2 corridor |

**Top-two joint probability (`G-L10`):**  
`P(Brighton O3.5 corners ∧ Brighton/Draw) ≈ 58%` — **moderately positive coupling**. Sustained Brighton territory supports both corners and non-loss, but an early Brighton lead can reduce later corners and a high-corner Brighton performance can still occur in a Coventry counterattacking win. The joint value is disclosed and does not reorder the marginals.

#### Card completeness block

| Requirement | State |
|---|---|
| Identity / competition / scheduled time / venue frozen | PASS |
| EPL regulation endpoint frozen | PASS |
| Current method and soccer rules read fresh | PASS |
| Exact starting XIs and goalkeepers | PASS |
| Full benches | PASS via same-day lineup record, corroborated by unchanged-XI live report |
| Injury / availability refresh | PASS with official Brighton team-news hierarchy |
| L5 / L10 / L15 / L20 + continuity test | PASS; Coventry cross-division windows explicitly downweighted |
| H2H continuity | PASS — historical only / no predictive weight |
| Current chance / xG / shots | PASS with provider disagreement preserved rather than merged |
| Separate corner process | PASS |
| Outdoor venue weather/current-surface check | PASS with exact-location forecast conflict disclosed |
| Joint outcome-state masses | PASS |
| Centre / width arithmetic | PASS |
| Normalised total edges | PASS |
| Small-sample SE check | PASS |
| Complement kill paths | PASS |
| `P(R1 ∧ R2)` + coupling | PASS |
| Final volatile refresh | PASS at ~13:52 BST |
| Settlement source named | PASS — Premier League/Opta match centre for score and corners; exact operator terms control any bespoke contract |

#### Sources used for P-408

| Source | Role | Card use |
|---|---|---|
| Google Drive `METHOD.md` | Governing method | MDS-v4.0, probability tier, market-blind lifecycle |
| Google Drive `CONTROLS.md` | Governing controls | G-L1/L2/L7/L8/L9/L10/L11 and completeness |
| Google Drive `RULES_SOCCER.md` | Sport algorithm | participant, goal, corner, weather and continuity controls |
| Google Drive `LEAGUE_RULES_SOCCER.md` | EPL rules reference | 90-minute league settlement, EPL competition context |
| Premier League official 2026-27 fixtures | FIELD OWNER | fixture identity and 14:00 BST kickoff |
| Brighton official match preview | CLUB FIELD OWNER | team news; Coventry absences; 7.4 xG, 15 big chances, 33 shots allowed; possession/cross data; officials |
| The Times same-day live build-up | HIGH-QUALITY CURRENT REPORT | both teams unchanged starting XIs before kickoff |
| EL PAÍS lineup record | STRUCTURED CURRENT LINEUP CROSS-CHECK | full XI, formations and nine-man benches |
| xGStat Coventry match log | CURRENT PROCESS | consistent three-match Coventry xG series |
| xGStat Coventry-Hull / Man City-Coventry | CURRENT PROCESS | opponent xG, chance-quality context |
| Sky Sports Man City-Coventry | HIGH-QUALITY CROSS-CHECK | 1.37 xG alternate provider, 12 shots, 5 corners |
| Brighton official Leeds match centre | CLUB MATCH CENTRE | 20 shots, 5 SOT, 7 corners |
| StatMuse Brighton xG / corners | STRUCTURED RESEARCH | Brighton 3-game xG and 5/7/7 corner series |
| StatMuse Brighton L10/L15/L20 | STRUCTURED HISTORICAL RESEARCH | longer same-league continuity windows |
| FBref Coventry 2025-26 + 2026-27 | HISTORICAL/CURRENT RESEARCH | promotion regime, prior L-windows, cup scoring context |
| Sky Sports Plymouth-Coventry | MATCH REPORT | current attackers' 4-2 cup scoring evidence |
| Met Office City of Coventry Stadium | GOVERNMENT WEATHER | exact stadium-area hourly forecast |
| Structured venue weather query | WEATHER CROSS-CHECK | current 22°C/cloudy and shower-risk signal |

#### Public source URLs recorded

- https://www.premierleague.com/en/news/4675097/all-380-fixtures-for-202627-premier-league-season
- https://www.brightonandhovealbion.com/media-article/mft-match-preview-coventry-city-bha-pl-september-2026
- https://www.thetimes.com/sport/football/article/manchester-united-vs-manchester-city-coventry-brighton-premier-league-latest-news-mwl57pnv5
- https://elpais.com/deportes/resultados/futbol/inglaterra/2026_2027/directo/regular-a-4-6a38cde94568f66/alineaciones/
- https://www.xgstat.com/teams/coventry-city/matches?competition=premier-league&season=2026-2027
- https://www.xgstat.com/competitions/premier-league/2026-2027/fixtures?gameweek=2
- https://www.xgstat.com/competitions/premier-league/2026-2027/matches/manchester-city-coventry-city-2026-09-05/analysis/players/performance
- https://www.skysports.com/football/man-city-vs-coventry/stats/5277798263498676232
- https://www.brightonandhovealbion.com/match-centre-stats?gameId=2645217
- https://www.statmuse.com/fc/ask/brighton-game-logs-this-season-xg-xga
- https://www.statmuse.com/fc/ask/brighton-corners-each-game-this-season
- https://www.statmuse.com/fc/ask/brighton-last-15-matches-in-premier-league
- https://www.statmuse.com/fc/ask/brighton-stats-last-20-games
- https://fbref.com/en/squads/f7e3dfe9/2025-2026/matchlogs/c10/schedule/Coventry-City-Scores-and-Fixtures-Championship
- https://fbref.com/en/squads/f7e3dfe9/2026-2027/all_comps/Coventry-City-Stats-All-Competitions
- https://www.skysports.com/football/plymouth-argyle-vs-coventry-city/teams/577439
- https://weather.metoffice.gov.uk/forecast/gcqfmgyum?new-design=false

### P-409 — Lille OSC vs ESTAC Troyes — French Ligue 1 — PRE-MATCH FORECAST / NOW LIVE / UNSETTLED

- **Scheduled start:** 2026-09-13 15:00 CEST / 23:00 AEST / 13:00 UTC.
- **Forecast freeze:** **2026-09-13 14:58:08 CEST / 22:58:08 AEST**, before scheduled kickoff.
- **State at freeze:** SCHEDULED / PRE-MATCH.
- **Post-freeze state check:** LIVE, 0-0 at approximately 23:01 AEST. **This live information did not enter the forecast.**
- **Venue:** Decathlon Arena – Stade Pierre-Mauroy, Villeneuve-d'Ascq.
- **Competition:** 2026-27 Ligue 1, Matchweek 4.
- **Working ID:** P-409 (local/user-directed; pending later canonical reconciliation).
- **Method:** MDS-2026.09.06-v4.0; `SPORTS_ONLY / MARKET_BLIND`.
- **Performance status:** LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE under the current Drive correction.
- **Settlement status:** PENDING. No retrospective performed.
- **P-409 queue recheck 2026-09-13 23:24 AEST:** LIVE, Lille 1-0 Troyes at retrieval; remains unsettled. No retrospective or grading performed.

#### Issued ranking

| Rank | Selection | `UNVALIDATED_SUBJECTIVE` probability | Evidence |
|---|---|---:|---|
| 1 | **Lille team goals — Over 0.5** | **82%** | MEDIUM; Lille scored in all 3 league matches and Troyes' defensive tail is wide |
| 2 | **Troyes team corners — Over 2.5** | **79%** | MEDIUM; direct corner process: Troyes 6/5/11, Lille conceded 8/5/6 |
| 3 | **Lille or Draw — Double Chance (90 min)** | **76%** | MEDIUM; home + same-league continuity, tempered by Lille xGA and midweek fatigue |
| 4 | **1st Half total goals — Over 0.5** | **70%** | MEDIUM-LOW; 4/6 current league team-games had a first-half goal, with mechanism support but small n |
| 5 | **Full-match total goals — Under 3.5** | **65%** | MEDIUM-LOW; central 3-goal corridor, despite Troyes' high-tail Strasbourg game |

**Supplied 2.5-goal line:** **Over 2.5 goals — 57% `UNVALIDATED_SUBJECTIVE`**. This is a positive lean, but it does **not** make the top five because the exact 3-goal state makes Under 3.5 materially more robust.

**Potential regulation winner:** Lille — **51%**; Draw 25%; Troyes 24%.  
**Central score corridor:** Lille 2-1 Troyes; important adjacent states: 1-1, 2-0, 1-2.  
**No player prop issued:** confirmed official starting XIs and complete benches were not retrievable before the 14:58:08 CEST freeze.

#### Latest participant / availability check before freeze

**Freshest probable Lille XI (4-2-3-1)**
- GK: Berke Özer
- DEF: Tiago Santos, Nathan Ngoy, Alexsandro, Calvin Verdonk
- MID: Benjamin André, Nabil Bentaleb
- AM: Ethan Mbappé, Hákon Haraldsson, Osame Sahraoui
- ST: Olivier Giroud

**Lille availability**
- **Hamza Igamane:** unavailable with a knee injury.
- **Arnaud Bodart:** unavailable while completing a move to Le Havre.
- **Nabil Bentaleb:** specifically declared fit and available by Davide Ancelotti in the pre-match press conference.
- Lille played **Real Betis on 8 September**, losing 2-3, giving them five days between matches.

**Freshest Troyes continuity / probable XI**
The most recent settled league XI against Strasbourg was:
- GK: Patrick Beach
- DEF: Lucas Maronnier, Adrien Monfray, Junior Diaz, Anis Ouzenadji
- MID/AM: Mouhamed Diop, Iron Gomis, Merwan Ifnaoui, Antoine Mille, Hugo Picard / Karim Dermane
- ST: Renaud Ripart

Pre-match lineup services consistently listed **Ismaël Boura, Paolo Gozzi and Yvann Titi** unavailable. These are treated as secondary-source availability signals, not field-owner confirmations. Their absence mainly weakens defensive depth; the established front/midfield corner-producing group from the first three Ligue 1 matches remains substantially intact.

**Participant gate:** `XI_NOT_RETRIEVED_BEFORE_FREEZE`. Under `RULES_SOCCER.md`, participant-dependent player and exact side-strength claims are capped. Team/game processes with robust non-lineup evidence may still be ranked with lower evidence labels.

#### L5 / L10 / L15 / L20 + continuity

**Lille**
- Current Ligue 1: Angers 0-2 Lille; Lille 2-2 PSG; Toulouse 0-1 Lille → **2W-1D-0L, 5-2**.
- Midweek Champions League: Lille 2-3 Real Betis.
- Same-league last 20: **10W-6D-4L**, 24 goals scored over the 20-match window.
- Last 10 Ligue 1 xG aggregate: **15.90 xG**, showing a much broader attacking base than the three-game 2026-27 sample alone.
- Continuity verdict: same-division continuity is usable, but summer personnel change and five-day European turnaround widen the current-event distribution.

**Troyes**
- Current Ligue 1: 0-0 Paris FC; 2-1 at Lorient; 2-6 Strasbourg → **1W-1D-1L, 4-7**.
- 2025-26 Ligue 2 title season: **20W-7D-7L, 60-33**.
- Longer L10/L15/L20 windows are dominated by Ligue 2 and preseason. Promotion is a major population shift, so these older wins are context only, not a direct Ligue 1 coefficient.
- Current top-flight evidence therefore receives priority.

**H2H continuity**
- The most recent competitive meetings before this season were in 2022-23 and earlier. They are too old under current managers/rosters to receive directional weight.

#### Current goal / chance process

**Lille current Ligue 1**
- 5 goals scored, 2 conceded.
- StatMuse current xG: **3.74 total = 1.25 xG/game**.
- StatMuse current xGA: **7.01 total = 2.34 xGA/game**.
- Lille have therefore substantially outperformed their current xGA in actual goals conceded. That is treated as a warning against overrating the 2-goal defensive record.
- Match-level attack:
  - Angers: 2 goals, 11 shots, 8 SOT, 1.25 xG.
  - PSG: 2 goals, 9 shots, 4 SOT, 1.28 xG.
  - Toulouse: 1 goal, 10 shots, 6 SOT, ~1.21 xG by StatMuse; another provider gave ~1.06.
- Lille scored in every league match.

**Troyes current Ligue 1**
- 4 goals scored, 7 conceded.
- Cross-source current estimates: about **1.83 xG for / 1.97 xG against per match**.
- Paris FC: 0-0; 9 shots, 2 SOT, 6 corners.
- Lorient: won 2-1; ~1.57 xG, 11 shots, 5 corners.
- Strasbourg: lost 2-6 but generated **27 shots, 6 SOT and 11 corners**; external xG record around 2.48.
- The 2-6 score is therefore not treated as eight-goal evidence alone: Troyes created enough attacking volume that the game belongs in the high-width tail, not as a simple “bad team” marker.

#### First-half process

Current first halves:
- Angers-Lille: **0-2 HT**.
- Lille-PSG: **1-0 HT**.
- Toulouse-Lille: **0-0 HT**.
- Troyes-Paris FC: **0-0 HT**.
- Lorient-Troyes: **0-2 HT**.
- Troyes-Strasbourg: **1-2 HT**.

A first-half goal occurred in **4 of 6** combined current league team-games (66.7%).  
Naive SE for 4/6 ≈ **19.2 percentage points**, so the raw rate is too noisy to use as a direct probability.

Mechanism support for Over 0.5:
- Lille have current finishers Giroud/Haraldsson/Sahraoui available and scored twice before HT at Angers.
- Troyes scored before HT at Lorient and Strasbourg.
- Troyes' defensive-depth absences widen the early-concession tail.

Counterweights:
- Both teams have produced a 0-0 first half recently.
- Lille's five-day Champions League turnaround can depress opening intensity.
- Lille's current corner/territory numbers are not dominant.

Final 1H state:
- 0 goals: **30%**
- exactly 1: **42%**
- 2+: **28%**
- **1H O0.5 = 70%**.

#### Corner process — direct target evidence

**Troyes team corners in 2026-27 Ligue 1**
- vs Paris FC: **6**
- at Lorient: **5**
- vs Strasbourg: **11**
- Mean = **7.33**.
- Sample SD ≈ **3.21**; SE ≈ **1.85**. The small sample is explicitly noisy.

**Lille opponent corners in 2026-27 Ligue 1**
- Angers: **8**
- PSG: **5**
- Toulouse: **6**
- Mean conceded = **6.33**.
- Sample SD ≈ **1.53**; SE ≈ **0.88**.

**Direct corner-causing evidence**
- Troyes generated 27 shots against Strasbourg while chasing/attacking through a wide 4-2-3-1 and produced 11 corners.
- At Lorient, despite only 32.6% possession, Troyes still produced 11 shots and 5 corners: territory share did not suppress their corner exposure.
- Against Paris FC, Troyes produced 6 corners despite only 41.4% possession.
- Therefore the mechanism is not “Troyes dominate possession”; it is repeated attacking sequences, wide entries/blocks and score-state pressure.

Working Troyes corner centre ≈ **6.1**, width ≈ **3.0**.
State masses:
- 0-2 corners: **21%**
- 3-5: **39%**
- 6+: **40%**
- **Troyes O2.5 corners = 79%**.

#### Environment / surface

- Exact venue query at Decathlon Arena / Stade Pierre-Mauroy near 14:58 CEST: **~21°C, cloudy**.
- Forecast game window: shower probability approximately **51% at 15:00**, falling thereafter.
- Pierre-Mauroy has a retractable roof; no trustworthy pre-freeze confirmation of roof state was recovered.
- Therefore weather receives **no signed goal/corner adjustment**. It is carried as distribution width only.

#### Joint event object / explicit arithmetic

**Lille goal centre**
- Own current xG: 1.25
- Troyes current xGA: ~1.97
- Simple midpoint prior = `(1.25 + 1.97)/2 = 1.61`
- Home / Troyes defensive-depth adjustment: **+0.15**
- Five-day post-Champions-League fatigue adjustment: **−0.10**
- Working Lille centre ≈ **1.66**, rounded to **1.65**

**Troyes goal centre**
- Troyes own current xG: ~1.83
- Lille current xGA: ~2.34, but this is opponent-sensitive and paired with only 2 actual goals conceded.
- Rather than copy the raw midpoint above 2.0, shrink toward a promoted-away prior: working prior **1.45**
- Away adjustment: **−0.10**
- Lille short-rest defensive-fatigue branch: **+0.05**
- Working Troyes centre ≈ **1.40**

**Total centre ≈ 3.05 goals; working width ≈ 1.95.**
- Normalised edge at 2.5: `|3.05 - 2.50| / 1.95 ≈ 0.28`
- Normalised edge at 3.5: `|3.05 - 3.50| / 1.95 ≈ 0.23`

**Full-match goal-state masses**
- 0-1 goals: **18%**
- exactly 2: **25%**
- exactly 3: **22%**
- 4+: **35%**
- Therefore **O2.5 = 57%**
- Therefore **U3.5 = 65%**

**Lille team-goal masses**
- 0: **18%**
- 1: **34%**
- 2+: **48%**
- Therefore **Lille O0.5 team goals = 82%**

**Winner masses**
- Lille win: **51%**
- Draw: **25%**
- Troyes win: **24%**
- Therefore **Lille/Draw = 76%**

#### `G-L1` representative compatibility state

Representative state:
- HT Lille 1-0 Troyes
- FT Lille 2-1 Troyes
- Troyes corners: 5

This state wins:
- Lille O0.5 team goals
- Troyes O2.5 corners
- Lille/Draw
- 1H O0.5
- U3.5
- supplied O2.5

It is a compatibility demonstration, not the generator of the rankings.

#### Complement / kill-path decomposition (`G-L9`)

| Selection | Win p | Complement | Main failure paths |
|---|---:|---:|---|
| Lille O0.5 team goals | 82% | 18% | Lille post-UCL fatigue; Troyes low block; Özer/Beach game stays compressed; Lille finishing regression |
| Troyes O2.5 corners | 79% | 21% | Lille score control denies repeated Troyes entries; injured Troyes full-back depth reduces width; low-event game |
| Lille or Draw | 76% | 24% | Troyes xG signal is real; Lille current xGA warning materialises; transition/set-piece conversion |
| 1H O0.5 | 70% | 30% | slow Lille restart after Europe; Troyes compact opening; finishing variance |
| U3.5 | 65% | 35% | early goal destabilises game; Troyes 2-6-type high tail; penalty/red-card/late chase |
| Supplied O2.5 | 57% | 43% | match stays in 1-0 / 1-1 / 2-0 states; Lille fatigue; keeper finishing variance |

**Top-two joint probability (`G-L10`):**  
`P(Lille O0.5 team goals ∧ Troyes O2.5 corners) ≈ 64%` — **mildly positive / state-dependent coupling**. A Lille goal can force Troyes to chase and generate corners, but a very early Lille multi-goal lead can also reduce match competitiveness. This joint value does not alter the marginal ranks.

#### Card completeness

| Requirement | State |
|---|---|
| Identity / competition / kickoff / venue | PASS |
| Regulation endpoint | PASS |
| Drive method + soccer rules consulted | PASS |
| Confirmed official XI + full bench | **PARTIAL / NOT RETRIEVED BEFORE FREEZE** |
| Latest probable XI + injuries | PASS with source-grade labels |
| L5/L10/L15/L20 + continuity | PASS; Troyes cross-division history downweighted |
| H2H continuity | PASS — no directional weight |
| Goal/xG process | PASS with provider differences preserved |
| Separate corner process | PASS |
| Small-sample SE | PASS |
| Venue weather/current-surface | PASS WITH LIMITATION — roof state not confirmed |
| Joint masses / centre / width | PASS |
| Normalised total edges | PASS |
| Complement kill paths | PASS |
| `P(R1 ∧ R2)` | PASS |
| Pre-kickoff volatile freeze | PASS at 14:58:08 CEST |
| Settlement source named | PASS — Ligue 1/LFP/defined Opta-style match stats, cross-checkable through ESPN/FBref/StatMuse |

#### Sources used for P-409

| Source | Role |
|---|---|
| Google Drive `METHOD.md` | Governing lifecycle / probability / market-blind process |
| Google Drive `CONTROLS.md` | G-L controls and completeness |
| Google Drive `RULES_SOCCER.md` | Soccer participant/goal/corner framework |
| Google Drive `LEAGUE_RULES_SOCCER.md` | Ligue 1 rules / 90-minute endpoint |
| Ligue1.com J4 schedule | Field-owner fixture time |
| LOSC official calendar/site | Club fixture identity, recent result, official pre-match materials |
| ESTAC official calendar/results | Troyes fixture identity and current results |
| LOSC pre-match press-conference reporting | Bentaleb fit; Igamane unavailable; Bodart transfer state |
| LOSC Toulouse match report | Lille recent XI, substitutions, goal timing |
| LOSC Lille-PSG match page | Goal timing / current attacking continuity |
| ESTAC Strasbourg official recap | Troyes current attack and match narrative |
| Paris FC official Troyes recap | Troyes J1 first-half and process |
| FC Lorient official Troyes match page | Troyes J2 XI + 5 corners + 11 shots |
| StatMuse Lille current xG/corners | Structured current goal/corner process |
| StatMuse Troyes current corner evidence | 11-corner Strasbourg confirmation |
| FootyMetrics Troyes current xG summary | Cross-check current xG/xGA |
| FBref Troyes current/2025-26 logs | Promotion continuity and prior-season context |
| TotalCorner / match-stat cross-checks | Lille opponent-corner counts and HT states |
| Structured exact-venue weather query | Game-window conditions |
| Current match-status feed | Post-freeze queue state only; explicitly excluded from forecast |

#### Public URLs recorded

- https://ligue1.com/fr/articles/l1_article_5562-programmation-tv-j4-2
- https://www.losc.fr/actualites/2026-06-10/le-calendrier-2026-2027
- https://www.estac.fr/equipe-premiere/calendrier-resultats/
- https://losc.fr/
- https://www.losc.fr/actualites/2026-09-03/toulouse-losc-le-compte-rendu
- https://www.losc.fr/match/2026-2027/ligue-1/lille-vs-paris-saint-germain
- https://www.estac.fr/premiere-defaite-de-la-saison-face-a-strasbourg-2-6-j3/
- https://parisfc.fr/equipe-pro/le-paris-fc-ramene-un-point-du-stade-de-laube-0-0/
- https://www.fclorient.bzh/match/fc-lorient-2/
- https://www.statmuse.com/fc/ask/lille-xg-per-match-this-season?l=ligue1
- https://www.statmuse.com/fc/ask/lille-corners-by-game-this-ligue-1-season
- https://www.statmuse.com/fc/ask/which-teams-have-always-have-7-corners-each-game?l=ligue1
- https://www.footymetrics.com/teams/370-troyes
- https://fbref.com/en/squads/54195385/2026-2027/matchlogs/c13/schedule/Troyes-Scores-and-Fixtures-Ligue-1
- https://fbref.com/en/squads/54195385/2025-2026/matchlogs/c60/schedule/Troyes-Scores-and-Fixtures-Ligue-2
- https://www.totalcorner.com/fr/h2h/lille-vs-toulouse
- https://www.totalcorner.com/h2h/angers-vs-lille

### P-410 — RB Leipzig vs Hamburger SV — German Bundesliga — PRE-MATCH / UNSETTLED

- **Scheduled start:** 2026-09-13 15:30 CEST / 23:30 AEST / 13:30 UTC.
- **Forecast freeze:** **2026-09-13 15:24:00 CEST / 23:24:00 AEST**, six minutes before scheduled kickoff.
- **State at freeze:** SCHEDULED / PRE-MATCH. No live-match information used.
- **Venue:** Red Bull Arena, Leipzig.
- **Competition:** 2026-27 Bundesliga, Matchday 3.
- **Working ID:** P-410 (local/user-directed; pending later canonical reconciliation).
- **Method:** MDS-2026.09.06-v4.0; `SPORTS_ONLY / MARKET_BLIND`.
- **Performance status:** LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE under the current Drive correction.
- **Settlement status:** PENDING. No retrospective performed.

#### Issued ranking

| Rank | Selection | `UNVALIDATED_SUBJECTIVE` probability | Evidence |
|---|---|---:|---|
| 1 | **RB Leipzig team goals — Over 0.5** | **88%** | MEDIUM; strong current xG/shot process vs HSV's high xGA, tempered by short rest/rotation |
| 2 | **RB Leipzig or Draw — Double Chance (90 min)** | **86%** | MEDIUM; home + stronger same-league process, but Leipzig's recent defensive execution is unstable |
| 3 | **Hamburger SV team goals — Under 1.5** | **82%** | MEDIUM; HSV created only ~0.89 xG total across first two league matches |
| 4 | **1st Half total goals — Over 0.5** | **76%** | MEDIUM; all four current league team-games had a first-half goal, but n=4 is heavily shrunk |
| 5 | **RB Leipzig team corners — Over 4.5** | **68%** | MEDIUM-LOW; direct shot/cross/corner mechanism, but HSV have not conceded huge corner totals yet |

**Supplied full-match 2.5 line:** **Over 2.5 goals — 59% `UNVALIDATED_SUBJECTIVE`**. Positive direction, but the edge is too small to displace the five stronger contracts.

**Potential regulation winner:** RB Leipzig — **64%**; Draw 22%; Hamburger SV 14%.  
**Central score corridor:** RB Leipzig 2-0 / 2-1 Hamburger SV, with 1-0 and 3-0 also material.  
**No player prop issued:** officially confirmed starting XIs plus full benches were not retrievable before the freeze.

#### Latest participant / availability check

**Bundesliga official probable RB Leipzig XI**
- GK: Maarten Vandevoordt
- DEF: Ridle Baku, Willi Orbán, Castello Lukeba, David Raum
- MID: Neil El Aynaoui, Nicolas Seiwald, Ezechiel Banzuzi
- FWD/AM: Brajan Gruda, Christopher Nkunku, Marc Guiu

**Bundesliga official probable Hamburg XI**
- GK: Daniel Heuer Fernandes
- DEF: Nicolás Capaldo, Jordan Torunarigha, Shafiq Nandja
- WB/MID: Zakaria El Ouahdi, Albert Sambi Lokonga, Nicolai Remberg, David Møller Wolfe
- AM: Fábio Vieira, Albert Grønbæk
- ST: Patson Daka

**Availability**
- Bundesliga's pre-match team-news page listed Leipzig **Christoph Baumgartner (thigh), Viggo Gebel (knee), Lukas Klostermann (groin) and Rocco Reitz (hamstring)** out; **Assan Ouédraogo (shoulder) and Rômulo (knee)** doubtful.
- A same-day dpa/Welt report described Leipzig as otherwise close to full strength and specifically named **Reitz and Baumgartner** as the clear injury absences. This narrower same-day description is preserved rather than silently overwriting the Bundesliga list.
- Hamburg: **Fernando Dickes (shoulder) and Alexander Røssing-Lelesiit (ankle)** listed out; **Sebastiaan Bornauw (muscular), Miro Muheim (muscular), Warmed Omari (shoulder), Immanuel Pherai (illness)** listed doubtful.
- Miro Muheim has a separately recorded muscular-injury doubt for this exact fixture.
- Leipzig played **Como in the Champions League on 10 September**, losing 4-1, only three days before this game.
- Hamburg last played **Mainz on 6 September**, giving them a full week of recovery.
- Same-day reporting says Martín Demichelis intended several changes/rotation after the Bremen and Como defeats.
- `XI_NOT_RETRIEVED_BEFORE_FREEZE` remains active. No scorer/SOT/player-minutes market is ranked.

#### L5 / L10 / L15 / L20 + continuity

All windows below are **Bundesliga** windows unless noted.

**RB Leipzig**
- L5: **2W-0D-3L, 8-12 goals**.
- L10: **7W-0D-3L, 22-15 goals**.
- L15: **9W-2D-4L, 30-22 goals**.
- L20: **11W-3D-6L, 38-31 goals**.
- Current 2026-27 league: **1W-0D-1L, 4-3**.
- Same-league continuity is usable, but the current coach, summer squad changes and the 72-hour European turnaround make current participants/process more important than the older aggregate.

**Hamburger SV**
- L5: **2W-1D-2L, 6-11 goals**.
- L10: **2W-2D-6L, 11-24 goals**.
- L15: **3W-4D-8L, 16-30 goals**.
- L20: **5W-7D-8L, 23-34 goals**.
- Current 2026-27 league: **0W-0D-2L, 0-7**.
- Hamburg were already a Bundesliga club in 2025-26, so the longer same-competition windows are relevant; nevertheless, the 2026-27 squad contains meaningful new personnel such as Vieira/Daka/Møller Wolfe, so the 0-7 start is not extrapolated without the chance data.

**Recent H2H**
- Leipzig won both 2025-26 league meetings **2-1**.
- Because coaching/personnel have changed and the current match is already explained by stronger direct current mechanisms, those H2H results are context only and carry **no independent directional coefficient**.

#### Current goal / chance process

**RB Leipzig, first two Bundesliga matches**
1. RB Leipzig 3-0 Gladbach:
   - ~**3.95 xG** vs ~0.97
   - **25 shots**, 11 on target
   - **7 corners**
   - HT 1-0
2. Werder Bremen 3-1 RB Leipzig:
   - ~**1.50 xG** vs ~0.95
   - **19 shots**, 5 on target
   - **7 corners**
   - 71% possession
   - **35 crosses**
   - HT Bremen 1-0

Current league mean:
- Leipzig xG ≈ **2.73/game**
- Leipzig xGA ≈ **0.96/game**
- Leipzig shots ≈ **22/game**
- Leipzig corners = **7/game**

The Bremen scoreline was materially worse than the chance balance: Leipzig created ~1.5 xG while Bremen's xG was under 1.0. That does not erase the defensive execution problem, especially because Como then scored four, but it prevents treating the 3-1 defeat as pure process collapse.

**Hamburg, first two Bundesliga matches**
1. Dortmund 2-0 HSV:
   - HSV ~**0.63 xG**
   - 6-8 shots depending provider display, only 2-3 on target
   - **1 corner**
   - HT 0-2
2. HSV 0-5 Mainz:
   - HSV **0.26 xG**
   - **8 shots, 1 on target**
   - **4 corners**
   - Mainz ~**2.58 xG**
   - HT 0-2

Current league mean:
- HSV xG ≈ **0.45/game**
- HSV xGA ≈ **2.04/game**
- HSV scored **0 from ~0.89 total xG**

The zero-goal record is therefore not just bad finishing: current chance creation itself is weak.

#### First-half process

Current league first halves:
- Leipzig-Gladbach: **1-0**
- Bremen-Leipzig: **1-0**
- Dortmund-HSV: **2-0**
- HSV-Mainz: **0-2**

Thus a first-half goal occurred in **4/4 current team-games**.

A raw 100% hit rate at n=4 has a meaningless naive SE of zero. The card therefore uses an adjusted small-sample check rather than the raw rate:
- add-two / Agresti-style adjusted rate ≈ **75%**
- adjusted SE ≈ **15 percentage points**

Mechanism support:
- Leipzig produced first-half pressure in both league games and generated 44 shots total across two matches.
- HSV conceded at 9' vs Dortmund and 19'/41' vs Mainz.
- Leipzig's home opener produced a first-half goal despite only 47% possession.

Counterweights:
- Leipzig's three-day turnaround and announced rotation may reduce early cohesion.
- Rain/drizzle risk may alter technical execution.
- HSV's likely 3-4-2-1 can initially compress central space.

Final first-half states:
- 0 goals: **24%**
- exactly 1: **45%**
- 2+: **31%**
- **1H O0.5 = 76%**.

#### Corner process — direct target evidence

**Leipzig current league corners**
- vs Gladbach: **7**
- at Bremen: **7**
- Current mean = **7.0**.

**Hamburg current opponent corners**
- Dortmund: **3**
- Mainz: **5**
- Current mean conceded = **4.0**.

Longer context:
- Leipzig have taken **99 corners in their last 20 Bundesliga matches = 4.95/game**.
- Leipzig have taken **83 in their last 15 = 5.53/game**.
- Hamburg have taken only **47 in their last 15 = 3.13/game**, consistent with relatively low sustained attacking territory.

Direct corner-causing mechanism:
- Leipzig generated **25 shots** vs Gladbach and **19 shots + 35 crosses** at Bremen.
- At Bremen, 71% possession and repeated wide delivery translated into seven corners despite losing 3-1.
- HSV conceded 20 shots at Dortmund and 16 to Mainz; even though those teams generated only 3 and 5 corners, the defensive volume keeps a Leipzig 5+ corner path live.
- The counterpoint is important: HSV's two opponents averaged only four corners, so Leipzig's current seven-per-game is aggressively shrunk toward the longer ~5-per-game baseline.

Working Leipzig corner centre ≈ **5.4**, width ≈ **2.7**.
State masses:
- 0-4 corners: **32%**
- 5-7: **44%**
- 8+: **24%**
- **Leipzig O4.5 corners = 68%**.

#### Environment / current-surface gate

- Exact venue query at Red Bull Arena / Zentralstadion near 15:22 CEST: **~18°C, cloudy**.
- Structured game-window forecast: showers/rain risk rising into the match, around **46% at 16:00** and low-40s thereafter.
- No verified pitch-quality issue was recovered before freeze.
- Weather is therefore carried as **distribution width**, not as an automatic Under/Over or corner sign.

#### Joint event object / explicit arithmetic

**Leipzig scoring centre**
- Leipzig own current xG = **2.73**
- Hamburg current xGA = **2.04**
- simple midpoint prior = `(2.73 + 2.04)/2 = 2.385`
- short-rest / post-Como rotation: **−0.20**
- home / Hamburg defensive-depth branch: **+0.05**
- working Leipzig centre ≈ **2.24**

**Hamburg scoring centre**
- Hamburg own current xG = **0.45**
- Leipzig current Bundesliga xGA = **0.96**
- simple midpoint = `(0.45 + 0.96)/2 = 0.705`
- Leipzig defensive-execution / rotation branch after seven goals conceded across Bremen+Como: **+0.10**
- working Hamburg centre ≈ **0.81**

**Total centre ≈ 3.05 goals; working width ≈ 1.90.**
- Normalised edge at 2.5: `|3.05 - 2.50| / 1.90 ≈ 0.29`
- This is a modest edge, so O2.5 is only **59%**, not a high-confidence total.

**Full-match goal-state masses**
- 0-1 total goals: **17%**
- exactly 2: **24%**
- exactly 3: **25%**
- 4+: **34%**
- Therefore **O2.5 = 59%**
- Therefore **U3.5 = 66%**

**Leipzig team-goal masses**
- 0: **12%**
- exactly 1: **30%**
- 2+: **58%**
- Therefore **Leipzig O0.5 = 88%**

**Hamburg team-goal masses**
- 0: **48%**
- exactly 1: **34%**
- 2+: **18%**
- Therefore **Hamburg U1.5 = 82%**

**Winner masses**
- Leipzig win: **64%**
- Draw: **22%**
- Hamburg win: **14%**
- Therefore **Leipzig/Draw = 86%**

#### `G-L1` representative compatibility state

Representative state:
- HT: RB Leipzig 1-0 Hamburg
- FT: RB Leipzig 2-0 Hamburg
- Leipzig corners: 6

This one state wins:
- Leipzig O0.5 team goals
- Leipzig/Draw
- Hamburg U1.5 team goals
- 1H O0.5
- Leipzig O4.5 corners

The state is a compatibility check only; it did not force the rankings.

#### Complement / kill-path decomposition (`G-L9`)

| Selection | Win p | Complement | Main failure paths |
|---|---:|---:|---|
| Leipzig O0.5 team goals | 88% | 12% | post-UCL fatigue/rotation suppresses final action; HSV low block; keeper variance |
| Leipzig/Draw | 86% | 14% | Hamburg new attacking personnel finally convert; Leipzig defensive errors repeat; transition/set-piece upset |
| Hamburg U1.5 team goals | 82% | 18% | Leipzig's Bremen/Como defensive execution persists; Daka/Vieira/Grønbæk transition quality; penalty/red-card path |
| 1H O0.5 | 76% | 24% | low block survives early; Leipzig rotated XI starts slowly; weather/finishing variance |
| Leipzig O4.5 corners | 68% | 32% | early goals reduce attack demand; HSV defend without repeated blocks/end-line concessions; Leipzig rotation reduces width |
| Supplied O2.5 | 59% | 41% | Leipzig control but under-convert; HSV contribute little; 1-0 / 2-0 / 1-1 corridor |

**Top-two joint probability (`G-L10`):**  
`P(Leipzig O0.5 team goals ∧ Leipzig/Draw) ≈ 80%` — **strong positive coupling**, but not identity. Leipzig can score once and still lose 1-2 or 1-3; conversely a 0-0 draw wins the double chance but loses the team-goal leg. The joint figure does not alter marginal ranks.

#### Card completeness block

| Requirement | State |
|---|---|
| Identity / competition / kickoff / venue frozen | PASS |
| Regulation endpoint frozen | PASS |
| Current Drive method + soccer rules | PASS |
| Confirmed official XI + full bench | **PARTIAL / NOT RETRIEVED BEFORE FREEZE** |
| Latest probable XI + injuries/doubts | PASS with source conflict preserved |
| L5 / L10 / L15 / L20 | PASS |
| H2H continuity test | PASS — descriptive only |
| Current xG / shots / goal process | PASS |
| Separate corner process | PASS |
| Small-sample uncertainty | PASS |
| Outdoor venue weather/current surface | PASS |
| Joint centre / width / state masses | PASS |
| Normalised total edge | PASS |
| Complement kill paths | PASS |
| `P(R1 ∧ R2)` + coupling | PASS |
| Final pre-kickoff refresh | PASS at 15:24 CEST |
| Settlement source named | PASS — Bundesliga/DFB official final + field-defined stats, cross-checked by structured match records |

#### Sources used for P-410

| Source | Role |
|---|---|
| Google Drive `METHOD.md` | Governing method |
| Google Drive `CONTROLS.md` | G-L controls / completeness |
| Google Drive `RULES_SOCCER.md` | Soccer goal/corner/participant process |
| Google Drive `LEAGUE_RULES_SOCCER.md` | Bundesliga regulation/competition rules |
| Bundesliga official fixture page | Fixture identity/state |
| DFB Datencenter RB Leipzig/HSV | Field-owner schedule/result history |
| Bundesliga official Matchday 3 team-news page | Probable XIs and injury/doubt list |
| RB Leipzig official preview/ticket pages | Home fixture identity |
| HSV official schedule/news | Fixture/rest and preparation |
| dpa/Welt same-day reporting | Demichelis rotation, Reitz/Baumgartner absence, pressure/context |
| RB-Fans statistics | Leipzig current xG match-by-match |
| FotMob Gladbach-Leipzig | Current xG/shots/box-touch process |
| Guardian/TNT/Eurosport Bremen-Leipzig | 19 shots, 7 corners, 35 crosses, lineup/process |
| PlaymakerStats Dortmund-HSV | HSV xG/shots/corners/HT |
| PlaymakerStats/SoccerZZ HSV-Mainz | HSV xG/shots/corners/HT |
| StatMuse Leipzig L10/L15/L20/corners | Same-league trend and corner baseline |
| StatMuse Hamburg L15/L20/corners | Same-league trend/corner baseline |
| Structured Red Bull Arena weather query | Exact-venue game-window conditions |
| Current soccer schedule/status feed | Pre-kickoff identity/state only |

#### Public URLs recorded

- https://www.bundesliga.com/en/bundesliga/matchday/2026-2027/rb-leipzig
- https://datencenter.dfb.de/competitions/bundesliga/seasons/2026-2027/teams/rb-leipzig
- https://datencenter.dfb.de/en/competitions/bundesliga/seasons/2026-2027/teams/hamburger-sv-943
- https://www.bundesliga.com/en/bundesliga/news/team-news-line-ups-2026-27-bayern-dortmund-fantasy-20707
- https://www.bundesliga.com/de/bundesliga/news/voraussichtliche-aufstellungen-spieltag-verletzungen-sperren-ubersicht-3-39086
- https://rbleipzig.com/de/news/spielvorschau-rb-leipzig-vs-hamburger-sv-bundesliga-am-13-september-2026
- https://www.hsv.de/en/first-team/schedule
- https://www.hsv.de/news/HSV-splitter
- https://rbl-fans.de/stats
- https://www.fotmob.com/de/matches/borussia-monchengladbach-vs-rb-leipzig/852z0ko
- https://www.theguardian.com/football/match/2026/sep/05/werderbremen-v-red-bull-leipzig
- https://www.eurosport.de/fussball/bundesliga/2026-2027/live-sv-werder-bremen-rb-leipzig_mtc21893516/live-stats.shtml
- https://www.playmakerstats.com/match/2026-08-29-borussia-dortmund-hamburger-sv/12279228
- https://www.playmakerstats.com/match/2026-09-06-hamburger-sv-mainz/12279235
- https://www.statmuse.com/fc/ask/rb-leipzig-last-10-matches?l=bundesliga
- https://www.statmuse.com/fc/ask/rb-leipzig-corners-stats-in-last-20-games
- https://www.statmuse.com/fc/ask/hamburger-sv-corner-stats-last-20-games
- https://www.statmuse.com/fc/ask/hamburger-sv-corners-last-15-games

### P-411 — Spain (W) vs Germany (W) — FIBA Women's Basketball World Cup 2026, 3rd Place — PRE-GAME / UNSETTLED

- **Scheduled tip:** 2026-09-13 16:30 CEST / 2026-09-14 00:30 AEST / 14:30 UTC.
- **Forecast freeze:** **2026-09-13 16:28:15 CEST / 2026-09-14 00:28:15 AEST**, before scheduled tip.
- **State at freeze:** PRE-GAME. No post-tip information used.
- **Venue:** Berlin Arena, Berlin, Germany.
- **Competition/phase:** FIBA Women's Basketball World Cup 2026 — bronze / 3rd-place game.
- **Working ID:** P-411 (local/user-directed; pending later canonical reconciliation).
- **Method:** MDS-2026.09.06-v4.0; SFA-BASKETBALL; `SPORTS_ONLY / MARKET_BLIND`.
- **Performance status:** LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE under the current Drive correction.
- **Settlement status:** PENDING. No retrospective performed.
- **Operator endpoint:** `UNKNOWN_DEFINITION` because the operator was not supplied. Displayed full-game probabilities use an **including-overtime working endpoint** with an explicit OT tail. Regulation-only sensitivity does not change the rank order.

#### Issued ranking — supplied slate

| Rank | Selection | `UNVALIDATED_SUBJECTIVE` probability | Evidence |
|---|---|---:|---|
| 1 | **Germany (W) +6.5** | **56%** | LOW-MEDIUM; winner/spread split, strong current German rebound/ball-security mechanisms, but Spain remains likelier winner |
| 2 | **Under 147.5 total points** | **53%** | LOW; line sits very close to the working total centre |
| 3 | **Over 147.5 total points** | **47%** | LOW; exact complement of Rank 2, listed only because it is in the supplied slate |
| 4 | **Spain (W) -6.5** | **44%** | LOW-MEDIUM; exact complement of Rank 1, listed only because it is in the supplied slate |

**Potential winner:** **Spain (W) — 60%**, Germany 40%.  
**Working central score:** Spain **76** – Germany **71**.  
**Continuous team-score centre:** Spain ~75.8, Germany ~70.6 → **146.4 total / Spain +5.2 margin**.

The two O/U rows and the two spread rows are exact complements. Only the preferred side of each target is treated as a recommendation: **Germany +6.5** and **Under 147.5**.

#### Why the opening 83-53 Spain win is not the centre

Spain beat Germany **83-53** on September 4, but the shooting split was extreme:
- Spain: **54% FG, 50% 3PT**
- Germany: **29% FG, 17.4% 3PT**
- Spain led for 39:13 and by as many as 32.

That result remains important because Spain's physicality and defensive disruption were real. However, the Drive's basketball controls prohibit using one lopsided final as the next game's central margin when the current possession/efficiency tree has changed.

Germany's post-opener response:
- 74-58 Japan
- 83-58 Mali
- 94-56 Korea
- 93-74 Belgium
- 64-86 France

The Belgium quarterfinal is especially important: Germany beat the reigning European champions by **19**, shooting **48% FG / 60.6% 2PT**, with Nyara Sabally posting **16 points and 12 rebounds**. The current Drive audit explicitly cites this Germany-Belgium game as a case where an underdog-separation branch had been omitted pregame. That branch is therefore included here rather than assuming Spain's opening-night +30 repeats.

The August 15 preparation game, Spain 65-60 Germany, is descriptive only. `RULES_BASKETBALL.md` classifies World Cup warm-ups as friendlies and prohibits using them as a competitive margin anchor.

#### Tournament form and score environment

**Spain tournament results**
- Spain 83-53 Germany
- Mali 82-73 Spain
- Spain 79-59 Japan
- Spain 89-66 Australia
- USA 76-66 Spain

Spain through the semifinal:
- Record: **3-2**
- Points for: **78.0/game**
- Points against: **67.2/game**
- Mean game total: **145.2**
- Sample SD of game totals: **9.2**
- SE of mean game total: **4.1**
- Mean margin: **+10.8**, but heavily influenced by the opening +30 Germany result.

**Germany tournament results**
- Spain 83-53 Germany
- Germany 74-58 Japan
- Germany 83-58 Mali
- Germany 94-56 Korea
- Germany 93-74 Belgium
- France 86-64 Germany

Germany through the semifinal:
- Record: **4-2**
- Points for: **76.8/game**
- Points against: **69.2/game**
- Mean game total: **146.0**
- Sample SD of game totals: **12.6**
- SE of mean game total: **5.1**
- Excluding the opening Spain game, Germany averaged **81.6 scored / 66.4 allowed** over its next five games, but opponent strength varied materially.

The two teams' realized tournament-total means therefore sit almost on the supplied **147.5** line. That is the main reason neither total side is assigned high confidence.

#### Latest participant / availability state

No bronze-game starting five was officially confirmed in the retrieved field-owner material **before the 16:28:15 CEST freeze**.

**Spain latest confirmed starting five — semifinal vs USA**
- Maite Cazorla
- Iyana Martín
- María Conde
- Awa Fam
- Raquel Carrera

All 12 Spain players were listed in the semifinal box score:
Cazorla, Martín, Conde, Fam, Carrera, Buenavida, Mariona Ortiz, Helena Pueyo, Paula Ginzo, Alba Torrens, Megan Gustafson/DiLeo and Alicia Flórez.

**Germany latest fully verified rotation**
The official DBB quarterfinal report gives a starting five of:
- Britta Daub
- Leonie Fiebich
- Emma Eichmeyer
- Nyara Sabally
- Luisa Geiselsöder

All 12 German players were recorded in the semifinal box score:
Alexis Peterson, Alexandra Wilke, Nyara Sabally, Emma Eichmeyer, Leonie Fiebich, Luisa Geiselsöder, Britta Daub, Frieda Bühner, Marie Gülich, Emily Bessoir, Lina Sontag and Clara Bielefeld.

**Current injury/availability conclusion**
- No new Spain or Germany injury scratch was recovered before the freeze.
- Alexis Peterson missed the Japan group game earlier in the tournament with an acute infection, but subsequently returned and played through the knockout phase, including **7 points in the semifinal**, so that earlier illness is **not** treated as an active absence.
- Spain and Germany both had their full 12-player semifinal groups represented on the latest score sheets.
- Because the bronze starting fives were not yet confirmed, `BK-P2` is **PARTIAL** and margin/total confidence is capped.

#### Quantified rotation exposure — control 20

**Spain**
- **Iyana Martín:** 16.5 PPG, 3.3 APG pre-semifinal; **90 minutes / 4 games = 22.5 mpg** before the semi; scored **17** vs USA.
- **Awa Fam:** 11.5 PPG, 6.8 RPG pre-semifinal; **99 minutes / 4 = 24.8 mpg**; 9 points / 7 rebounds vs USA.
- **Raquel Carrera:** 6.8 PPG, 6.5 RPG; **94 minutes / 4 = 23.5 mpg**; 6 points vs USA.
- **María Conde:** 9.3 PPG and **20.0 mpg** through the quarterfinal; started the semifinal and scored **17**.
- **Megan Gustafson:** 10.5 PPG through the quarterfinal; 14.8 mpg over those four, then 6 points / 6 rebounds vs USA.
- **Alicia Flórez:** 6.8 PPG, 3.0 APG, 17.2 mpg through the quarterfinal; 4 points vs USA.

**Germany**
- **Leonie Fiebich:** 10.0 PPG, **9.0 RPG, 3.8 APG**, 145 minutes through five = **29.0 mpg**; 9 points / 8 rebounds vs France.
- **Frieda Bühner:** **14.8 PPG**, 4.0 RPG, **20.1 mpg** through five; 2 points in the semifinal.
- **Nyara Sabally:** **12.0 PPG, 7.2 RPG**, 97 minutes through five = **19.4 mpg**; 12 points vs France.
- **Alexis Peterson:** 9.0 PPG, 3.5 APG, **22.9 mpg in games played** through the quarterfinal; 7 points vs France.
- **Marie Gülich:** **11.8 PPG**, 4.2 RPG pre-semifinal; 12 points / **10 rebounds** vs France.

This satisfies the Drive requirement to quantify top-three / ~20-minute exposures rather than carrying the rotation as bare names.

#### Possession / efficiency mechanisms

**Working possession corridor: 68-72 possessions, centre ~70.**
No single official possession count was retrieved for the bronze match, so this is a widened process estimate rather than a fitted pace claim.

**Spain positive mechanisms**
- Current FIBA world rank **#6** vs Germany **#11** is background only, not a coefficient.
- Spain held USA to 76 and was tied **58-58 after three quarters** in the semifinal.
- Martín and Conde both scored 17 vs USA, giving Spain two current perimeter creators around the Fam/Carrera/Gustafson interior rotation.
- Spain's opening matchup showed it can disrupt Germany's half-court offense physically.

**Germany positive mechanisms**
- Before the semifinal Germany averaged **46.2 rebounds** and only **9.8 turnovers per game**, an unusually valuable combination for protecting possession volume.
- Fiebich was averaging **9.0 rebounds and 3.8 assists**, Sabally 7.2 rebounds, giving Germany a multi-position rebounding base.
- Germany's 93-74 Belgium win showed the current full tournament rotation can separate against elite opposition.
- Germany is the host in Berlin; large home crowds have been a persistent tournament condition.
- Germany's semifinal tipped at 16:30 CEST Saturday; Spain's at 20:00. The bronze game is 16:30 Sunday, so Germany receives roughly **3.5 additional hours of recovery** from scheduled tip-to-tip.
- Spain's semifinal was tied after three quarters but ended with an **18-8 USA fourth quarter**, so the shorter recovery branch is applied specifically to late-game legs/closing efficiency, not as a generic full-game penalty.

**Shooting variance**
The opening Spain-Germany game featured 50% vs 17.4% three-point shooting. Per the current Drive correction, that extreme one-game gap is held mainly as **width**, not as a signed assumption that either percentage repeats.

#### Joint team-score object

**Spain team centre**
- Tournament scoring mean: **78.0**
- Germany tournament points allowed: **69.2**
- Simple cross-opponent midpoint: `(78.0 + 69.2) / 2 = 73.6`
- Spain structural/quality advantage and direct matchup success: **+2.0**
- Germany home/rebound/ball-security + fresher recovery branch: **−0.5**
- Working Spain centre ≈ **75.1-75.8**, final card centre **75.8**

**Germany team centre**
- Tournament scoring mean: **76.8**
- Spain tournament points allowed: **67.2**
- Simple midpoint: `(76.8 + 67.2) / 2 = 72.0`
- Spain's direct defensive matchup advantage: **−2.0**
- Germany home/recovery + current rebound/turnover mechanism: **+0.6**
- Working Germany centre ≈ **70.6**

**Working total centre:** **146.4**  
**Working margin centre:** Spain **+5.2**  
**Total decision width:** ~**15 points**  
**Margin decision width:** ~**12 points**

Normalised edges:
- Spread: `|5.2 - 6.5| / 12 ≈ 0.11`
- Total: `|146.4 - 147.5| / 15 ≈ 0.07`

Both are **small edges**, which is why all four exact supplied rows remain low or low-medium evidence.

#### Team-score budget at 147.5

| State | Germany score | Spain score required to reach 148+ |
|---|---:|---:|
| Germany floor | 64 | 84 |
| Germany centre | 71 | 77 |
| Germany ordinary high | 78 | 70 |

Reverse budget:

| State | Spain score | Germany score required to reach 148+ |
|---|---:|---:|
| Spain floor | 69 | 79 |
| Spain centre | 76 | 72 |
| Spain ordinary high | 83 | 65 |

Interpretation:
- The Over does **not** require both teams to have ceiling games.
- The Under remains live when Spain wins through defensive suppression, or when Germany keeps the margin tight by slowing Spain rather than matching Spain possession-for-possession.
- A competitive Germany branch can also create late fouling and push the game Over; therefore **Germany +6.5 and Under are not assumed to be automatically positively coupled**.

#### Margin-family masses — `G-L1` / control 23

| Margin family | Probability |
|---|---:|
| Spain by 15+ | **16%** |
| Spain by 7-14 | **28%** |
| Spain by 1-6 | **16%** |
| Germany by 1-6 | **20%** |
| Germany by 7+ | **20%** |

Derived:
- Spain win = **60%**
- Germany win = **40%**
- Spain -6.5 = **44%**
- Germany +6.5 = **56%**

The **Germany by 7+ = 20%** branch is deliberately present because the current Drive audit requires an underdog-separation family when multiple current mechanisms support it. Germany has at least three: rebounding/possession protection, home environment, and demonstrated current-regime separation vs Belgium.

#### Total-family masses

| Total family | Probability |
|---|---:|
| 137 or fewer | **22%** |
| 138-147 | **31%** |
| 148-157 | **29%** |
| 158+ | **18%** |

Derived:
- Under 147.5 = **53%**
- Over 147.5 = **47%**

Tournament realized-total cross-check:
- Spain games: 136, 155, 138, 155, 142 → mean **145.2**, SE **4.1**
- Germany games: 136, 132, 141, 150, 167, 150 → mean **146.0**, SE **5.1**

These are descriptive small samples and do not independently set the total.

#### Mandatory branch set

- **Central:** ~70 possessions, Spain modest per-possession advantage → ~76-71.
- **Shooting-high:** either side's 3PT tail raises total into 150s/160s; opening-night percentages are not reused as fixed rates.
- **Spain separation:** Spain pressure disrupts German initiation and turns defensive stops into transition; Spain wins 10-20+.
- **Germany close-game:** Germany controls defensive boards, keeps turnovers near tournament baseline, and uses Fiebich/Peterson/Sabally creation to stay within one or two possessions.
- **Germany separation:** German size/rebounding plus secondary scoring transfers usage away from the most heavily defended option; home-crowd/transition branch produces a 7+ upset.
- **Low-total Spain win:** Germany's perimeter efficiency stalls and Spain wins around 74-65.
- **Competitive high-total:** Germany's cushion wins but Germany scores enough to trigger late fouling; game reaches 150+.
- **OT:** explicit small tail because operator endpoint is unknown; OT disproportionately helps the Over and can widen or reverse a close spread result.

#### Representative Rank-1 score

**Spain 75 – Germany 72**:
- Germany +6.5: **WIN**
- Spain -6.5: loss
- Under 147.5: **WIN** (147)
- Over 147.5: loss
- Potential winner Spain: **WIN**

This is a compatibility example only, not the source of the probabilities.

#### Complement / kill-path decomposition (`G-L9`)

| Selection | Win p | Complement | Main failure paths |
|---|---:|---:|---|
| Germany +6.5 | 56% | 44% | Spain pressure recreates the opener's separation without requiring 50% 3PT; Germany's 24-hour recovery still leaves flat legs; Spain frontcourt wins second chances |
| Under 147.5 | 53% | 47% | competitive Germany offense triggers late fouling; both teams' secondary scorers convert; transition/OREB extend possessions; OT |
| Over 147.5 | 47% | 53% | medal game becomes half-court/physical; Germany's offense regresses toward France/Spain games; Spain wins via suppression rather than scoring ceiling |
| Spain -6.5 | 44% | 56% | Germany's rebound + low-TO base compresses margin; home crowd; Spain shorter recovery; Germany secondary/tertiary scoring branch |

#### Top-two joint probability (`G-L10`)

`P(Germany +6.5 ∧ Under 147.5) ≈ 30%`.

Coupling label: **near-neutral / state-dependent**.
- Germany can cover through a low-scoring compressed game.
- Germany can also cover by scoring enough to push the total Over, especially with late fouls.
- Therefore no fixed "underdog cushion + Under" dependence is assumed.

#### Overtime sensitivity

Because operator settlement terms were not supplied:
- **Working displayed endpoint:** includes OT.
- **Regulation-only sensitivity:** Under 147.5 rises by roughly 1 percentage point; spread probabilities move less than ~1 point in this card.
- Rank order is unchanged.
- The card remains tagged `UNKNOWN_DEFINITION` until operator rules are supplied.

#### Card completeness block

| Requirement | State |
|---|---|
| Competition / phase / venue / scheduled tip | PASS |
| FIBA rule-set / 40-minute structure | PASS |
| Spread / total contracts frozen | PASS |
| Operator regulation-vs-OT definition | **UNKNOWN_DEFINITION; explicit OT sensitivity included** |
| Final 12-player rosters | PASS |
| Bronze starting fives | **PARTIAL — not field-owner confirmed before freeze** |
| Latest availability / injury search | PASS; no new scratch found |
| Top-three / ~20-minute player exposure quantified | PASS |
| Recent competitive tournament form | PASS |
| Friendly margin excluded from centre | PASS |
| Possession / efficiency / rebound / turnover mechanisms | PASS with possession estimate labelled as estimate |
| Margin families incl. Germany 7+ upset | PASS |
| Team-score budget | PASS |
| Total families | PASS |
| Normalised spread / total edges | PASS |
| Small-sample uncertainty | PASS |
| Complement kill paths | PASS |
| `P(R1 ∧ R2)` + coupling | PASS |
| Final pre-tip freeze | PASS at 16:28:15 CEST |
| Settlement source | FIBA official match centre / final box score |

#### Sources used for P-411

| Source | Role |
|---|---|
| Google Drive `METHOD.md` | Governing lifecycle / market-blind probability rules |
| Google Drive `CONTROLS.md` | G-L controls / completeness |
| Google Drive `RULES_BASKETBALL.md` | Basketball-specific possession, margin, total and roster process |
| Official World Cup schedule / DBB PDF | Bronze tip time and phase |
| FIBA Spain-Germany group game | Direct current-roster H2H score, quarters and shooting |
| FIBA Germany-Belgium QF | Current German separation mechanism / shooting |
| FIBA Australia-Spain QF | Spain current knockout ceiling |
| FIBA Spain team profile | Martin/Fam/Gustafson/Carrera/Flórez roles and rates |
| FIBA Germany team profile | Bühner/Sabally/Gülich/Fiebich/Peterson rates |
| FIBA individual player profiles | Minutes/usage exposure for decision-driving rotation players |
| FIBA France-Germany semifinal preview | Germany rebounds/assists/2PT/3PT/FT and 9.8 TO/game |
| Reuters / Guardian semifinal reports | Spain 66-76 USA; Germany 64-86 France; phase context |
| Semifinal box-score cross-check | Latest 12-player participation and scoring |
| DBB official Germany roster / QF report | Final Germany 12 and latest field-owner starting five available |
| FIBA preparation-game tracker | Spain 65-60 Germany friendly, context only |
| FIBA tournament page | Tournament results sequence |

#### Public URLs recorded

- https://www.basketball-bund.de/wp-content/uploads/sites/2/2026/05/FWBWC-2026-Game-Schedule-2025-15-18.pdf
- https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/games/128117-ESP-GER
- https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/games/128150-BEL-GER
- https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/games/128148-AUS-ESP
- https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/teams/spain
- https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/teams/germany
- https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/teams/spain/295079-iyana-martin
- https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/teams/spain/300698-awa-fam
- https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/teams/spain/225137-raquel-carrera
- https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/teams/spain/268901-megan-gustafson
- https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/teams/spain/204187-maria-conde
- https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/teams/spain/300742-alicia-florez
- https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/teams/germany/218988-leonie-fiebich
- https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/teams/germany/266528-frieda-buhner
- https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/teams/germany/217770-nyara-sabally
- https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/teams/germany/239761-alexis-peterson
- https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/teams/germany/174996-marie-guelich
- https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/news/sf-preview-france-or-germany-whos-making-a-first-final
- https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/news/tracker-preparation-games-fiba-womens-basketball-world-cup-2026
- https://www.basketball-bund.de/womens-world-cup-2026-unsere-12-fuer-berlin/
- https://www.basketball-bund.de/wettbewerbe/fiba-womens-basketball-world-cup-2026/
- https://www.reuters.com/sports/holders-us-battle-past-spain-reach-womens-world-cup-final-2026-09-12/
- https://www.theguardian.com/sport/2026/sep/12/usa-spain-womens-basketball-world-cup-semi-final

### P-412 — Atlanta Falcons @ Pittsburgh Steelers — NFL Regular Season Week 1 — PRE-GAME / UNSETTLED

- **Scheduled kickoff:** 2026-09-13 13:00 EDT / 2026-09-14 03:00 AEST.
- **Forecast freeze:** 2026-09-13 12:38:42 EDT / 2026-09-14 02:38:42 AEST.
- **State at freeze:** PRE-GAME. No live information used.
- **Working ID:** P-412.
- **Method:** MDS-2026.09.06-v4.0 / SFA-AMERICAN-FOOTBALL / SPORTS_ONLY / MARKET_BLIND.
- **Settlement:** PENDING. No retrospective performed.

| Rank | Selection | `UNVALIDATED_SUBJECTIVE` p |
|---|---|---:|
| 1 | Atlanta Falcons +6.5 | 55% |
| 2 | Under 40.5 | 53% |
| 3 | Over 40.5 | 47% |
| 4 | Pittsburgh Steelers -6.5 | 45% |

**Potential winner:** Pittsburgh 66%, Atlanta 34%.  
**Representative score:** Pittsburgh 23-17 Atlanta.

Key freeze facts: Cooper Rush confirmed Atlanta starter; Tua Tagovailoa and Michael Penix Jr. out; rookie Jack Strand backup; Pittsburgh secondary missing DeShon Elliott with Joey Porter Jr. unavailable/expected out; Atlanta retains Bijan Robinson/Kyle Pitts/Drake London; exact Acrisure weather check showed warm/cloudy conditions with moderate shower risk. Operator OT definition not supplied; working full-game endpoint includes OT.

**P-412 source set:** NFL schedules/injury pages; Atlanta Falcons official game report/depth chart/QB updates; Steelers official injury report/depth chart/roster; Steelers Week 1 matchup statistics; Pro-Football-Reference 2025 Atlanta/Pittsburgh drive tables; NFL Football Operations 2026 rules; venue weather source.

### P-413 — Baltimore Ravens @ Indianapolis Colts — NFL Regular Season Week 1 — PRE-GAME / UNSETTLED

- **Scheduled kickoff:** 2026-09-13 13:00 EDT / 2026-09-14 03:00 AEST / 17:00 UTC.
- **Forecast freeze:** **2026-09-13 12:43:22 EDT / 2026-09-14 02:43:22 AEST**, before scheduled kickoff.
- **State at freeze:** PRE-GAME. No post-kickoff information used.
- **Venue:** Lucas Oil Stadium, Indianapolis.
- **Competition:** NFL regular season, Week 1.
- **Working ID:** P-413.
- **Method:** MDS-2026.09.06-v4.0; SFA-AMERICAN-FOOTBALL; `SPORTS_ONLY / MARKET_BLIND`.
- **Evidence density:** SPARSE under the Drive's American-football rules.
- **Performance status:** LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.
- **Settlement:** PENDING. No retrospective performed.
- **Operator endpoint:** `UNKNOWN_DEFINITION`; working probabilities assume the conventional full-game **including-overtime** endpoint with an explicit OT tail.

#### Issued ranking — supplied slate

| Rank | Selection | Exact settlement probability | Evidence |
|---|---|---:|---|
| 1 | **Indianapolis Colts +3.0** | **53% win / 8% push / 39% loss** | LOW-MEDIUM |
| 2 | **Under 48.5 total points** | **52% win / 48% loss** | LOW |
| 3 | **Over 48.5 total points** | **48% win / 52% loss** | LOW |
| 4 | **Baltimore Ravens -3.0** | **39% win / 8% push / 53% loss** | LOW-MEDIUM |

**Potential winner:** **Baltimore Ravens 56%**, Indianapolis 44%.  
**Representative score:** Baltimore **24** – Indianapolis **23**.  
**Continuous centre:** Baltimore ~24.6, Indianapolis ~23.3 = **47.9 total / Baltimore +1.3 margin**.

Only **Colts +3.0** and **Under 48.5** are preferred directions. The opposite spread/total rows are listed only because all four outcomes were supplied.

#### Participant / regime freeze

**Baltimore**
- QB1: Lamar Jackson; QB2 Tyler Huntley.
- RB1: Derrick Henry.
- Main WRs: Zay Flowers and Rashod Bateman; Devontez Walker inactive.
- New head coach: Jesse Minter.
- New offensive coordinator: Declan Doyle.
- New defensive play-calling structure under Minter/Anthony Weaver.
- New starting center: **Jovaughn Gwyn**, making his first NFL start after winning the job to replace Pro Bowler Tyler Linderbaum; Danny Pinter is out for the season.
- Defensive absences: **Nnamdi Madubuike OUT**, **Teddye Buchanan OUT**.
- Ravens inactive reporting also lists Devontez Walker, Elijah Sarratt, Emery Jones, Chandler Rivers and Joe Fagnano inactive.
- Zay Flowers returned to full practice and carried no final injury designation.

**Indianapolis**
- QB1: **Daniel Jones**, fully cleared from the December 2025 Achilles tear after taking essentially every first-team rep from the start of training camp.
- QB2: Anthony Richardson Sr.; Riley Leonard QB3.
- RB1: Jonathan Taylor.
- TE1: Tyler Warren.
- WR group: Alec Pierce, Josh Downs, Keenan Allen; Pierce is active/expected to play but secondary reporting indicates a managed snap count after ankle surgery.
- OL: Bernhard Raimann, Quenton Nelson, Tanor Bortolini, Matt Goncalves, Jalen Travis.
- Defence: DeForest Buckner, Grover Stewart, Laiatu Latu, Arden Key; Sauce Gardner, Charvarius Ward Sr., Cam Bynum, AJ Haulcy.
- Colts ruled nobody out on Friday; Austin Ajiake was the only final-questionable injury in official reporting, with a later local gameday report indicating he would miss the game.
- Charvarius Ward has been managing a back issue but practiced and expected to play.
- AJ Haulcy and several other limited players returned to full work.

#### 2025 drive baselines, with current-regime reconciliation

**Baltimore 2025**
- 8-9.
- 24.9 points/game.
- 178 offensive drives.
- 42.7% scoring-drive rate.
- 12.4% turnover-drive rate.
- **2.31 points per drive**.
- Defence allowed 23.4/game and **2.22 opponent points/drive**.
- Lamar Jackson missed time in 2025, so the full-season offense understates a healthy-Lamar ceiling.
- However, 2026 has a new HC, new OC and a first-time starting center; those are held primarily as width, not automatic negative direction.

**Indianapolis 2025**
- 8-9.
- 27.4 points/game.
- 170 offensive drives.
- 49.4% scoring-drive rate.
- **2.66 points per drive**.
- Defence allowed 24.2/game and 2.24 opponent points/drive.
- More relevant current-roster branch: with Daniel Jones healthy through the first 10 games, Indianapolis scored on **57.6% of possessions**, averaged **31.7 points/game**, and started 8-2.
- Jonathan Taylor through that 10-game phase: **1,139 rushing yards on 189 carries (6.0 YPC), 17 total TDs**.
- Jones has taken nearly every 2026 first-team camp rep, materially improving continuity relative to his 2025 camp competition.

#### Current matchup mechanisms

**Why Baltimore remains the likelier winner**
- Healthy Lamar Jackson + Derrick Henry creates the highest single-unit ceiling in the matchup.
- Baltimore still has Flowers/Bateman and a strong multi-dimensional run/pass stress profile.
- Minter adds a high-end defensive scheme background.
- Trey Hendrickson, Roquan Smith, Kyle Hamilton, Marlon Humphrey and Nate Wiggins give Baltimore enough front/coverage talent to create negative plays even without Madubuike.
- Daniel Jones is playing his first real game 280 days after his Achilles injury; uncertainty in movement under live pressure is real even though camp participation was excellent.

**Why Colts +3 is preferred to Ravens -3**
- Indianapolis is at home with strong same-system offensive continuity under Steichen/Jones/Taylor.
- The Colts' first-10-game 2025 offense was materially better than the full-season line after Jones was lost.
- Baltimore's new center is making his first NFL start against an Indianapolis interior that includes Buckner and Grover Stewart.
- Madubuike's absence weakens Baltimore's interior run/pressure profile against Jonathan Taylor and a Colts line that graded strongly in 2025.
- Indianapolis' secondary is materially upgraded with Sauce Gardner, Charvarius Ward and Cam Bynum.
- Baltimore's new-coach/new-OC Week 1 distribution must be widened, not treated as a fully known top-tier offense.
- The spread is exactly **3.0**, so Ravens-by-3 is a **push**, not a Colts loss.

#### Weather / roof

- Lucas Oil Stadium official gameday page still showed **Roof: TBD / Window: TBD** in the retrieved snapshot.
- Secondary same-day reporting expected the roof to be closed.
- Exact venue weather outside near 12:42 EDT: about **28°C / 82°F, mostly sunny**, with thunderstorm risk increasing later in the afternoon.
- Because the roof state was not field-owner confirmed before freeze, weather is carried as a small width term only. If closed, external weather has essentially no direct passing/kicking effect.

#### Joint drive / score object

**Expected drives:** roughly 10-11 meaningful offensive possessions per team.

**Baltimore team centre**
- 2025 offense: 2.31 points/drive.
- Indianapolis 2025 defence: 2.24 points allowed/drive.
- Healthy Lamar/Henry branch raises ceiling.
- New center/new OC/new HC installation and upgraded Colts secondary lower certainty.
- Working team-score centre: **~24.6**.

**Indianapolis team centre**
- 2025 offense: 2.66 points/drive.
- Baltimore 2025 defence: 2.22 points allowed/drive.
- Full-season Colts rate is blended with the much stronger Jones-healthy 2025 first-10-game regime.
- Baltimore's Madubuike absence and Colts run-game continuity lift the floor.
- Jones post-Achilles live-game uncertainty and Minter/Hendrickson pressure branch lower the ceiling.
- Working team-score centre: **~23.3**.

**Combined centre:** **47.9**.  
**Margin centre:** **Baltimore +1.3**.  
**Margin width:** ~10.5 points.  
**Total width:** ~14 points.

Normalised edges:
- Spread: `|1.3 - 3.0| / 10.5 ≈ 0.16` toward Indianapolis +3.
- Total: `|47.9 - 48.5| / 14 ≈ 0.04` toward Under — a very small edge.

#### Discrete margin families / push handling

| Margin family | Probability |
|---|---:|
| Baltimore by 14+ | 12% |
| Baltimore by 7-13 | 15% |
| Baltimore by 4-6 | 12% |
| **Baltimore by exactly 3** | **8%** |
| Baltimore by 1-2 | 9% |
| Indianapolis win | 44% |

Derived:
- Baltimore winner = **56%**
- Indianapolis winner = **44%**
- Ravens -3.0 = **39% win / 8% push / 53% loss**
- Colts +3.0 = **53% win / 8% push / 39% loss**

#### Total families

| Total points | Probability |
|---|---:|
| 0-40 | 23% |
| 41-48 | 29% |
| 49-55 | 25% |
| 56+ | 23% |

Derived:
- **Under 48.5 = 52%**
- **Over 48.5 = 48%**

#### Total component budget at 48.5

| Colts points | Ravens points required for 49+ |
|---|---:|
| 17 | 32 |
| 20 | 29 |
| 23 | 26 |
| 27 | 22 |

Reverse:

| Ravens points | Colts points required for 49+ |
|---|---:|
| 20 | 29 |
| 24 | 25 |
| 27 | 22 |
| 31 | 18 |

Implication:
- A competitive Colts offense can push the game Over even while +3 wins.
- A Ravens defensive-control win can still stay Under.
- A Baltimore blowout does not mechanically imply Over, and Colts +3 does not mechanically imply Under.

#### Mandatory branch set

- **Central:** competitive indoor game, Baltimore 24-23.
- **Ravens separation:** Lamar/Henry create explosives, Minter/Hendrickson pressure Jones, Ravens win by 7-14.
- **Colts control:** Taylor + OL sustain drives, Jones uses play action/quick game, Madubuike absence matters, Colts win or lose by 1-2.
- **Colts separation:** Baltimore's first-time center and new-coach installation create sacks/turnovers/failed drives while the Colts' healthy offense recreates 2025 early-season efficiency.
- **Low-Colts-score branch:** Jones' live mobility is materially worse than camp and Baltimore front pressure creates sacks/short fields; defeats +3 and often supports Under.
- **Explosive/non-offensive branch:** Lamar scramble/explosive TD, Pierce deep shot, turnover return or short field; raises total and margin variance.
- **Late-game branch:** close score creates fourth-down aggressiveness and possible late foul-free hurry-up possessions.
- **OT branch:** small but explicit under 2026 NFL regular-season rules; disproportionately helps Over and can move a push/cover state.

#### Representative Rank-1 score

**Baltimore 24 – Indianapolis 23**
- Colts +3.0: WIN
- Ravens -3.0: LOSS
- Under 48.5: WIN
- Over 48.5: LOSS
- Potential winner Baltimore: WIN

#### Complement / kill-path decomposition (`G-L9`)

| Selection | Win | Push | Loss | Main failure paths |
|---|---:|---:|---:|---|
| Colts +3.0 | 53% | 8% | 39% | Lamar/Henry explosive separation; Jones post-Achilles pressure failure; Baltimore short fields |
| Under 48.5 | 52% | — | 48% | both run games efficient; explosive QB runs/deep shots; short fields; close-game late scoring; OT |
| Over 48.5 | 48% | — | 52% | new-system Ravens start slowly; Colts play possession football; upgraded secondaries force FGs/punts |
| Ravens -3.0 | 39% | 8% | 53% | Colts healthy offensive continuity; Taylor vs Madubuike-less interior; Baltimore center/installation errors; home field |

#### Top-two joint probability (`G-L10`)

`P(Colts +3.0 win ∧ Under 48.5) ≈ 29%` with a **near-neutral / mildly positive** coupling.

- 24-23, 23-20 and 20-17 type states win both.
- Colts can cover in a high-scoring 30-28 game, which loses the Under.
- Baltimore can win 27-17, which wins Under but loses Colts +3.
No automatic underdog-plus-Under dependence is assumed.

#### Card completeness

| Requirement | State |
|---|---|
| NFL identity / kickoff / venue | PASS |
| 2026 NFL rules / OT regime | PASS |
| Starting QBs | PASS |
| QB backup branches | PASS |
| Material OL / skill / defensive unit exposure | PASS |
| Ravens key inactives | PASS, with field-owner injuries + current inactive reporting |
| Complete Colts inactive list | PARTIAL; official final report clean, full gameday inactive card not recovered |
| Current coaches / scheme transitions | PASS |
| 2025 drive baselines | PASS / downweighted |
| Current-regime Jones-healthy split | PASS |
| Expected-drive model | PASS |
| Discrete exact-3 push mass | PASS |
| Low-underdog-score branch | PASS |
| Explosive / turnover / special-team tails | PASS |
| Component total budget | PASS |
| Roof/weather | PASS WITH LIMITATION; official roof state TBD |
| Normalised spread / total edges | PASS |
| Complement kill paths | PASS |
| `P(R1 ∧ R2)` | PASS |
| Final pre-kickoff refresh | PASS at 12:43:22 EDT |
| Settlement source | NFL official gamebook / match centre |

#### Sources used for P-413

| Source | Role |
|---|---|
| Google Drive `METHOD.md`, `CONTROLS.md` | Governing method and completeness |
| Google Drive `RULES_AMERICAN_FOOTBALL.md` | QB/drive/key-number/OT/kill-path process |
| NFL schedule/game-state source | Kickoff and pregame state |
| NFL Week 1 injury report | Official designations |
| Ravens official Week 1 game page | Event identity |
| Ravens official Week 1 depth chart | Lamar/Henry/Flowers personnel |
| Ravens official Madubuike update | Madubuike/Buchanan outs, Flowers/Walker status |
| Ravens official center announcement | Jovaughn Gwyn first NFL start |
| Colts official Week 1 preview | Minter matchup, Jones/Taylor offensive context, upgraded secondary |
| Colts official injury updates | Pierce/Haulcy/Ward and clean team status |
| Colts official 2026 depth chart | Jones/Taylor/OL/defensive units |
| Colts official Jones recovery/camp reports | full first-team-rep continuity |
| Colts official 2025 offense review | 57.6% first-10 scoring-drive rate, Jones/Taylor regime |
| Pro-Football-Reference Baltimore 2025 | points/drives/PPD/offensive-defensive baselines |
| Pro-Football-Reference Indianapolis 2025 | points/drives/PPD/offensive-defensive baselines |
| Current inactive reporting | Walker/Sarratt/Emery Jones/Rivers/Fagnano inactive; Ajiake absence cross-check |
| Lucas Oil official gameday page | roof/window still TBD |
| Exact Lucas Oil weather query | external venue conditions |

#### Public URLs recorded

- https://www.nfl.com/injuries/
- https://www.nfl.com/schedules/2026/by-team/baltimore-ravens
- https://www.colts.com/schedule/2026/
- https://www.baltimoreravens.com/game-day/2026/reg-week1/ravens-at-colts/
- https://www.baltimoreravens.com/photos/ravens-2026-week-1-depth-chart
- https://www.baltimoreravens.com/news/nnamdi-madubuike-injury-report-ravens-colts-season-opener-neck
- https://www.baltimoreravens.com/news/jovaughn-gwyn-ravens-starting-center-nnamdi-madubuike-teddye-buchanan-tyler-loop
- https://www.colts.com/news/colts-week-1-preview-what-could-we-learn-about-2026-colts-in-season-opener-vs-jesse-minter-lamar-jackson-baltimore-ravens
- https://www.colts.com/news/colts-do-not-rule-out-any-players-for-week-1-game-against-baltimore-ravens
- https://www.colts.com/news/colts-release-first-unofficial-depth-chart-of-2026-regular-season
- https://www.colts.com/news/daniel-jones-availability-throughout-training-camp-preseason-underscores-colts-confidence-in-2026-offense
- https://www.colts.com/news/5-colts-things-the-biggest-reasons-to-be-optimistic-about-shane-steichen-daniel-jones-jonathan-taylor-colts-2026-offense
- https://www.pro-football-reference.com/teams/rav/2025.htm
- https://www.pro-football-reference.com/teams/clt/2025.htm
- https://www.colts.com/game-day/regular-season-game-1

### P-414 — Buffalo Bills @ Houston Texans — NFL Regular Season Week 1 — PRE-GAME / UNSETTLED

- **Scheduled kickoff:** 2026-09-13 13:00 EDT / 12:00 CDT / 2026-09-14 03:00 AEST.
- **Forecast freeze:** **2026-09-13 12:49:09 EDT / 11:49:09 CDT / 2026-09-14 02:49:09 AEST**, before scheduled kickoff.
- **State at freeze:** PRE-GAME. No post-kickoff information used.
- **Venue:** Reliant Stadium, Houston.
- **Competition:** NFL regular season, Week 1.
- **Working ID:** P-414 (local/user-directed; pending canonical reconciliation).
- **Method:** MDS-2026.09.06-v4.0; SFA-AMERICAN-FOOTBALL; `SPORTS_ONLY / MARKET_BLIND`.
- **Evidence density:** SPARSE under the Drive's American-football rules.
- **Performance status:** LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE under current Drive correction.
- **Settlement:** PENDING. No retrospective performed.
- **Operator endpoint:** `UNKNOWN_DEFINITION`; displayed full-game probabilities use an including-overtime working endpoint.

#### Issued ranking — supplied slate

| Rank | Selection | `UNVALIDATED_SUBJECTIVE` probability | Evidence |
|---|---|---:|---|
| 1 | **Houston Texans +1.5** | **55%** | LOW-MEDIUM; elite defensive baseline + home + healthier gameday availability, while Bills remain slightly likelier outright winner |
| 2 | **Under 44.5 total points** | **53%** | LOW; Houston defensive suppression vs elite Buffalo offense places the line almost exactly at centre |
| 3 | **Over 44.5 total points** | **47%** | LOW; exact complement of Rank 2, included because supplied |
| 4 | **Buffalo Bills -1.5** | **45%** | LOW-MEDIUM; exact complement of Rank 1, included because supplied |

**Potential winner:** **Buffalo Bills — 53%**, Houston 47%.  
**Representative compatible score:** Buffalo **22** – Houston **21**.  
**Continuous score centre:** Buffalo ~22.4, Houston ~21.7 → **44.1 total / Buffalo +0.7 margin**.

Only **Texans +1.5** and **Under 44.5** are preferred directions. The opposite rows are listed only because the full supplied slate contains both sides.

#### Current participant / inactive freeze

**Buffalo core**
- QB1: Josh Allen; QB2 Kyle Allen.
- RB: James Cook III, Ray Davis; **Ty Johnson inactive**.
- WR: DJ Moore, Khalil Shakir, Keon Coleman, Joshua Palmer.
- TE: Dalton Kincaid, Dawson Knox.
- OL core from official depth chart: Dion Dawkins, Alec Anderson, Connor McGovern, O'Cyrus Torrence, Spencer Brown.
- Key defensive names: Ed Oliver, Greg Rousseau, Bradley Chubb, Terrel Bernard, Christian Benford, C.J. Gardner-Johnson, Cole Bishop.
- **Jordan Hancock active** after being questionable.
- **T.J. Sanders inactive**.
- Other current Bills inactives: Skyler Bell, Jalon Kilgore, Mike Danna, Ar'maj Reed-Adams and Jude Bowry.
- New head coach: **Joe Brady**, but offensive continuity is stronger than a normal new-HC situation because Brady already coordinated the Buffalo offense.
- New defensive coordinator: **Jim Leonhard**, creating a genuine Week 1 defensive-scheme uncertainty branch.

**Houston core**
- QB1: C.J. Stroud; QB2 Davis Mills.
- RB: David Montgomery / Woody Marks. Joe Mixon was released in March; Montgomery was acquired from Detroit.
- WR: Nico Collins, Kayshon Boutte, Jaylin Noel/Xavier Hutchinson.
- TE: Dalton Schultz.
- Current OL cross-check: Aireontae Ersery, rookie Keylan Rutledge, Evan Brown, Ed Ingram, Trent Brown.
- Defensive core: Will Anderson Jr., Danielle Hunter, Sheldon Rankins, Azeez Al-Shaair, Derek Stingley Jr., Kamari Lassiter, Jalen Pitre, Calen Bullock.
- **Kayden McDonald on IR** with an ankle injury.
- Current Texans inactives: Brevin Jordan, Collin Wright, Aiden Fisher, Febechi Nwaiwu, Nate Thomas and Jaden Crumedy.
- The decision-driving Houston starters were otherwise largely available in the pregame snapshot.
- Houston's official week-of-game material repeatedly described the injury report as unusually clean.

#### 2025 drive baselines — current-regime priors, not copied forecasts

**Buffalo 2025**
- 481 points scored.
- **2.70 points per offensive drive**.
- 44.8% scoring-drive rate.
- 10.3% turnover-drive rate.
- 5.9 yards/play.
- Defence allowed **2.09 points per drive**, 5.2 yards/play.
- Buffalo rushing attack was elite: 2,714 team rushing yards and 30 rushing TDs.
- This remains a strong prior because Allen/Cook and much of the OL structure return, while DJ Moore adds a new receiving dimension.

**Houston 2025**
- 404 points scored.
- **2.00 points per offensive drive**.
- 42.9% scoring-drive rate.
- League-low-ish 5.8% turnover-drive rate in the retrieved table.
- Defence allowed only **1.54 points per drive**, **4.8 yards/play**, and 295 total points — the strongest defensive drive baseline in this matchup.
- Opponent turnover-drive rate: 14.6%.
- Current offence has changed materially: David Montgomery replaces Joe Mixon as the primary veteran RB, Kayshon Boutte joins Nico Collins, and the offensive line has been reshaped around Ersery/Rutledge/Evan Brown/Ingram/Trent Brown.

#### Direct matchup continuity — contextual, not a coefficient

Houston beat Buffalo **23-19 at Reliant Stadium in November 2025**.
- Josh Allen: **24/34, 253 yards, 0 TD, 2 INT**.
- James Cook: **17 carries, 116 yards, 1 TD**.
- Houston generated eight sacks in that meeting according to current team-preview reporting.
- Houston's quarterback that night was **Davis Mills**, not C.J. Stroud, so the 2025 final is not a same-offensive-regime H2H for Houston.
- The Texans defensive mechanism is more transferable than the raw final score: Houston's pressure/coverage structure has repeatedly caused Allen problems in this venue.
- H2H receives no independent numeric coefficient; it is used only where the current personnel/mechanism still exists.

#### Buffalo offence vs Houston defence

**Buffalo-positive**
- Allen/Cook produced one of the NFL's strongest 2025 drive offences.
- DJ Moore adds a proven YAC/deep/intermediate target; Allen-Moore produced explosive gains in preseason starter reps.
- Buffalo's offensive line is comparatively stable and healthy.
- Houston is missing rookie DT Kayden McDonald, weakening early-down interior depth.
- If Buffalo stays balanced, Houston cannot simply unleash Anderson/Hunter in known passing situations.

**Houston-positive**
- Houston's 2025 defence allowed only 1.54 opponent PPD and 4.8 yards/play.
- Current field-owner/team material still frames Houston as an elite defensive unit.
- Will Anderson Jr., Danielle Hunter, Stingley, Lassiter, Pitre and Bullock provide pass-rush/coverage strength at multiple levels.
- Allen's most recent Houston trip produced zero passing TDs, two INTs and eight sacks.
- Buffalo's new head-coach game-management layer and Houston road/venue communication preserve a lower offensive branch even with substantial scheme continuity.

Working Buffalo score centre: **~22.4**.

#### Houston offence vs Buffalo defence

**Houston-positive**
- C.J. Stroud is healthy and starts, unlike the late-2025 Bills matchup.
- Houston's official camp material described meaningful offensive-line improvement/continuity and one of its best offensive camp practices.
- David Montgomery adds a physical early-down/short-yardage option alongside Woody Marks.
- Nico Collins remains a high-end boundary target; Kayshon Boutte adds another vertical/route option.
- Buffalo's defence is changing coordinators and front structure for Week 1, so 2025 defensive efficiency cannot be treated as fully transferable.

**Buffalo-positive**
- Buffalo allowed 2.09 opponent PPD in 2025, a respectable baseline.
- The new Leonhard defence adds Bradley Chubb and C.J. Gardner-Johnson around Rousseau/Oliver/Benford/Bernard, giving Buffalo legitimate pressure/coverage upside.
- Houston's reshaped OL remains partly new despite camp improvement.
- Stroud's offense was only 2.00 PPD over the full 2025 season, so offseason optimism is not enough to assign an automatic positive coefficient.

Working Houston score centre: **~21.7**.

#### Game-state / score distribution

**Expected meaningful drives:** roughly 10-11 per side.

**Continuous centre**
- Buffalo: **22.4**
- Houston: **21.7**
- Total: **44.1**
- Buffalo margin: **+0.7**

**Decision widths**
- Margin width: ~10.5 points.
- Total width: ~13 points.

**Normalised edges (`G-L8`)**
- Spread: `|0.7 - 1.5| / 10.5 ≈ 0.08` toward Houston +1.5.
- Total: `|44.1 - 44.5| / 13 ≈ 0.03` toward Under.

Both are small edges. No supplied row is high-confidence.

#### Discrete margin families

| Margin family | Probability |
|---|---:|
| Buffalo by 14+ | **13%** |
| Buffalo by 7-13 | **15%** |
| Buffalo by 2-6 | **17%** |
| Buffalo by exactly 1 | **8%** |
| Houston win | **47%** |

Derived:
- Buffalo winner: **53%**
- Houston winner: **47%**
- Buffalo -1.5: **45%**
- Houston +1.5: **55%**

#### Total families

| Total points | Probability |
|---|---:|
| 0-37 | **28%** |
| 38-44 | **25%** |
| 45-51 | **25%** |
| 52+ | **22%** |

Derived:
- Under 44.5: **53%**
- Over 44.5: **47%**

#### Component budget at 44.5

| Houston score | Buffalo required for 45+ |
|---|---:|
| 14 | 31 |
| 17 | 28 |
| 21 | 24 |
| 24 | 21 |

Reverse:

| Buffalo score | Houston required for 45+ |
|---|---:|
| 17 | 28 |
| 21 | 24 |
| 24 | 21 |
| 28 | 17 |

Implications:
- A 21-point Houston game makes an ordinary 24-point Buffalo outcome enough for the Over.
- If Houston is suppressed to 14-17, Buffalo needs a relatively high scoring branch.
- Houston +1.5 can win in both low-total (20-19) and high-total (27-26) states.
- Under 44.5 can win with a Buffalo cover (24-17) or Houston cover (21-20); the two top selections are not mechanically identical.

#### Mandatory branch set

- **Central:** high-level defensive game, Buffalo 22-21 Houston.
- **Houston defensive squeeze:** Anderson/Hunter pressure creates sacks and long-yardage; Stingley/Lassiter limit explosives; 20-17/21-17 type Houston or Buffalo result.
- **Allen/Cook explosive branch:** Buffalo stays balanced, Cook forces light boxes, Allen/Moore hit explosives; Buffalo wins 27-20/30-20 and covers.
- **Houston offensive-upside branch:** Stroud benefits from improved protection and Collins/Boutte/Montgomery balance; new Buffalo defensive calls have communication errors; Houston wins 24-21/27-24.
- **Buffalo defensive-upside branch:** Leonhard pressure disguises create sacks/turnovers against Houston's new OL; Buffalo wins a low-total 24-13/23-16.
- **Short-field/non-offensive branch:** turnover return, blocked kick or special-teams swing raises total and margin volatility.
- **Late-game branch:** one-score game adds fourth-down aggression and potential hurry-up scoring; also preserves Houston +1.5 mass.
- **OT branch:** small explicit tail under 2026 NFL regular-season rules; disproportionately raises Over probability.

#### Representative Rank-1-compatible score

**Buffalo 22 – Houston 21**
- Texans +1.5: **WIN**
- Bills -1.5: loss
- Under 44.5: **WIN**
- Over 44.5: loss
- Potential winner Buffalo: **WIN**

This is a compatibility state, not the generator of the probabilities.

#### Complement / kill paths (`G-L9`)

| Selection | Win p | Loss p | Main failure paths |
|---|---:|---:|---|
| Texans +1.5 | 55% | 45% | Allen/Cook explosive efficiency; Houston new OL loses to Buffalo pressure; turnover/short-field Bills separation |
| Under 44.5 | 53% | 47% | both QBs efficient; explosive Allen/Moore plays; Houston improved offence; defensive/ST TD; OT |
| Over 44.5 | 47% | 53% | Houston defence compresses Buffalo; new Bills defence disrupts Stroud; long rushing drives drain clock; red-zone FG outcomes |
| Bills -1.5 | 45% | 55% | Houston defensive pressure repeats; Stroud healthy vs prior H2H; home field; one-point Buffalo win loses -1.5 |

#### Top-two joint probability (`G-L10`)

`P(Texans +1.5 ∧ Under 44.5) ≈ 31%`.

Coupling: **mildly positive / state-dependent**.
- 22-21 Buffalo, 20-17 Houston and 21-20 Houston win both.
- Houston can cover by scoring enough to push the game Over.
- Buffalo can cover while the Under wins if Houston's offence is suppressed.
No automatic underdog-plus-Under dependence is assumed.

#### Weather / roof

- Exact venue weather outside near freeze: about **30°C / 86°F, humid**, with roughly **44-51% precipitation/thunderstorm risk** through the game window.
- Reliant Stadium has a retractable roof.
- The Texans' field-owner roof policy says the roof decision is made two hours before kickoff and normally cannot then change.
- **The actual field-owner roof decision was not recovered before the forecast freeze.**
- A secondary game-day board labelled the venue as dome, but because the field-owner decision was not retrieved, that is not treated as decisive.
- Weather therefore receives **no signed total/spread adjustment**. If the roof is closed, external weather is largely irrelevant; if open, heat/humidity/storm risk primarily widens fatigue/ball-security/kicking tails.

#### Overtime / operator caveat

The user did not supply sportsbook settlement terms.
- Working endpoint: full game **including OT**.
- Regulation-only sensitivity changes the Under by roughly ~1 percentage point and slightly reduces spread tail width.
- Rank order is unchanged.
- Card remains `UNKNOWN_DEFINITION` until operator terms are supplied.

#### Card completeness

| Requirement | State |
|---|---|
| NFL identity / venue / kickoff | PASS |
| Current 2026 NFL / OT rules | PASS from governing Drive/NFL rules carried from current workflow |
| Starting QBs | PASS |
| Material RB/WR/TE/OL exposure | PASS |
| Official Friday injury reports | PASS |
| Current gameday inactive lists | PASS via current high-quality game-day reporting; field-owner list not separately indexed |
| Key Houston/Buffalo roster changes | PASS |
| 2025 drive baselines | PASS / explicitly downweighted |
| Current coaching/scheme transition | PASS |
| Expected-drive object | PASS |
| Discrete half-point margin families | PASS |
| Low-score and explosive branches | PASS |
| Component total budget | PASS |
| Venue weather | PASS |
| Final roof decision | **PARTIAL / field-owner decision not recovered** |
| Normalised spread / total edges | PASS |
| Complement kill paths | PASS |
| `P(R1 ∧ R2)` | PASS |
| Final pre-kickoff refresh | PASS at 12:49:09 EDT |
| Settlement source | NFL official gamebook / match centre |

#### Sources used for P-414

| Source | Role |
|---|---|
| Google Drive `METHOD.md`, `CONTROLS.md` | Governing lifecycle / probability / completeness |
| Google Drive `RULES_AMERICAN_FOOTBALL.md` | QB/drive/key-number/OT/weather/kill-path process |
| NFL.com schedule / game state | Fixture and pregame state |
| NFL official Week 1 injury report | Current injury designations |
| Buffalo Bills official Week 1 injury report | Johnson/Hancock/Sanders status |
| Buffalo Bills official depth chart / 53-man roster | Allen/Cook/Moore/OL/defensive personnel |
| Buffalo Bills Week 1 storylines | Houston defensive matchup, Allen venue history, new Leonhard defence |
| Houston Texans official Week 1 injury report | Houston availability |
| Houston Texans official roster / transactions | current roster; Montgomery acquisition / Mixon release |
| Houston Texans Week 1 radio/team material | offensive-line reshaping/continuity and current roster context |
| Current high-quality game-day inactive reporting | final inactive lists |
| Pro-Football-Reference Buffalo 2025 | offensive/defensive PPD, scoring rate, yards/play |
| Pro-Football-Reference Houston 2025 | offensive/defensive PPD, scoring rate, yards/play |
| Buffalo official 2025 Texans gamebook/recap | 23-19 prior meeting and direct matchup details |
| Houston official stadium A-Z guide | retractable-roof decision policy |
| Exact venue weather query | external game-window conditions |

#### Public URLs recorded

- https://www.nfl.com/injuries/
- https://www.nfl.com/schedules/2026/by-team/houston-texans
- https://www.buffalobills.com/game-day/2026/reg-week1/bills-at-texans/
- https://www.buffalobills.com/news/bills-injury-report-vs-texans-week-1
- https://www.buffalobills.com/news/top-storylines-for-bills-at-texans-nfl-week-1
- https://www.buffalobills.com/team/depth-chart
- https://www.buffalobills.com/news/position-by-position-look-at-bills-initial-53-man-roster-2026
- https://www.houstontexans.com/news/week-1-injury-report-texans-vs-bills
- https://www.houstontexans.com/team/players-roster/
- https://www.houstontexans.com/team/transactions/2026
- https://www.houstontexans.com/podcasts/texans-all-access
- https://www.houstontexans.com/podcasts/buffalo-memories-and-preseason-risers-texans-matchup
- https://www.pro-football-reference.com/teams/buf/2025.htm
- https://www.pro-football-reference.com/teams/htx/2025.htm
- https://www.buffalobills.com/news/bills-19-texans-23-final-score-game-recap-highlights
- https://www.houstontexans.com/gameday/2025/week-12-texans-vs-bills/box-score
- https://www.houstontexans.com/stadium/a-z-guide

### P-415 — LA Angels @ Washington Nationals — MLB — NOT ISSUED / INTERRUPTED

- User requested a pregame card for LA Angels (Grayson Rodriguez) @ Washington Nationals (Jake Irvin).
- Research began and the working ID was announced, but the user supplied a new event before a forecast was issued.
- **No picks, probabilities, winner call, or settlement-eligible forecast were issued.**
- This ID is retained as **NOT ISSUED / INTERRUPTED** so the local sequence is auditable and is not silently reused.
- No retrospective or settlement applies.

### P-416 — New York Mets @ New York Yankees — MLB — PRE-GAME / DELAYED START / UNSETTLED

- **Scheduled first pitch:** 2026-09-13 13:35 EDT / 2026-09-14 03:35 AEST.
- **Forecast freeze:** **2026-09-13 13:32:17 EDT / 2026-09-14 03:32:17 AEST**.
- **State at freeze:** PRE-GAME. Multiple live scoreboard threads mirroring MLB Gameday reported **Delayed Start: Wet Grounds**; no pitch had been thrown.
- **Venue:** Yankee Stadium, Bronx, New York.
- **Competition:** MLB regular season.
- **Working ID:** P-416.
- **Method:** MDS-2026.09.06-v4.0; SFA-BASEBALL; `SPORTS_ONLY / MARKET_BLIND`.
- **Performance status:** LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE under the current Drive correction.
- **Settlement:** PENDING. No retrospective performed.
- **Operator action/listed-pitcher/shortened-game terms:** `UNKNOWN_DEFINITION`; weather termination/void branches remain explicit.

#### Issued ranking — supplied slate

| Rank | Selection | Exact settlement probability | Evidence |
|---|---|---:|---|
| 1 | **Under 8.0 runs** | **52% win / 11% push / 37% loss** | MEDIUM-LOW |
| 2 | **Mets +1.5** | **51% win / 49% loss** | MEDIUM-LOW |
| 3 | **Yankees -1.5** | **49% win / 51% loss** | MEDIUM-LOW |
| 4 | **Over 8.0 runs** | **37% win / 11% push / 52% loss** | LOW-MEDIUM |

**Potential winner:** **New York Yankees — 63%**, Mets 37%.  
**Representative central score:** Yankees **4-3** Mets.  
**Working continuous centre:** Yankees ~4.4 runs, Mets ~3.0 runs → **7.4 total / Yankees +1.4**.

Only **Under 8.0** and **Mets +1.5** are preferred directions. The opposite rows are listed because the user supplied both sides of each target.

#### Official starter handshake

MLB's official probable-pitcher pages list:
- **NYM: Christian Scott, RHP — 4-4, 3.81 ERA, 120 SO**
- **NYY: Cam Schlittler, RHP — 13-6, 2.01 ERA, 220 SO**

`BB-P1` = PASS at the freeze as `PROBABLE_OFFICIAL`.

#### Posted batting orders / participant state

The same-day posted orders were consistently recovered from two current team-focused game threads, but MLB's indexed starting-lineup page had not refreshed to September 13 in the search snapshot. Therefore `BB-P2` is **PARTIAL / SECONDARY_POSTED_ORDER**, not falsely marked field-owner-confirmed.

**Mets**
1. Francisco Lindor — SS
2. Juan Soto — DH
3. Bo Bichette — 3B
4. Carson Benge — RF
5. Jared Young — 1B
6. A.J. Ewing — CF
7. Francisco Alvarez — C
8. Brett Baty — 2B
9. Nick Morabito — LF

**Yankees**
1. Ben Rice — DH
2. Cody Bellinger — LF
3. Aaron Judge — RF
4. Luis García Jr. — 1B
5. Spencer Jones — CF
6. Anthony Volpe — 2B
7. Ryan McMahon — 3B
8. Austin Wells — C
9. José Caballero — SS

Material availability:
- **Brett Baty starts** after knee discomfort; MRI reportedly showed no structural damage.
- **Aaron Judge starts in RF** after recently returning from a fractured rib. He had been 3-for-14 with six strikeouts since returning in the latest same-day report, so full season power is retained but return-form uncertainty is width rather than a signed downgrade.
- Marcus Semien, Mark Vientos and Christopher Morel are not in the Mets starting nine today.
- Paul Goldschmidt/Heliot Ramos/Amed Rosario are not in the Yankees starting nine today.

#### Starter process

**Cam Schlittler**
- 2026: **178.2 IP, 2.01 ERA, 0.92 WHIP, 220 K, 42 BB, 16 HR**.
- Advanced current line: **2.77 xERA, 2.60 FIP, 2.83 xFIP, 31.3% K, 6.0% BB, 0.81 HR/9**.
- Last five starts: **32.0 IP, 4 ER, 38 K — 1.13 ERA**.
- Most recent start: 7.0 IP, 1 ER, 10 K vs Colorado.
- Earlier 2026 matchup vs Mets: 6.2 IP with 9 K in a 5-2 Yankees win.
- The prior Mets start is context only; current arsenal/lineup process owns the projection.

**Christian Scott**
- 2026: **99.1 IP, 3.81 ERA, 1.29 WHIP, 120 K**.
- Advanced line: **3.85 xERA, 3.59 FIP, 4.16 xFIP, 27.8% K, 10.2% BB, 0.91 HR/9**.
- 21 starts but only 99.1 innings (~4.7 IP/start) and only two quality starts in the retrieved advanced line: his shorter hook is an exposure fact, not an automatic Over.
- Recent retrieved starts: 4.2 IP/2 ER vs SF; 5.1 IP/3 ER vs HOU; 4.2 IP/4 ER at CWS.
- No explicit same-day pitch cap was recovered; observed hook distribution is used rather than inventing one.

Starter conclusion:
- Schlittler owns the clear run-prevention/strikeout/command advantage.
- Scott has enough strikeout skill and HR suppression to keep a central competitive branch alive, but his walk rate and shorter outings increase Mets relief exposure.

#### Team / lineup context

**Season baseline**
- Mets: **4.29 runs/game**, .238/.309/.394; pitching **4.58 RA/game, 4.21 ERA**.
- Yankees: **4.58 runs/game**, .235/.313/.410; pitching **3.67 RA/game, 3.20 ERA**.
- Yankees team pitching over the latest retrieved 14-day window: **2.79 ERA**, 26.2% K, 7.5% BB.

**Recent form**
- Both clubs entered the current weekend with strong recent records; Baseball-Reference's pregame preview had each at 7-3 over the latest 10-game window available in that snapshot.
- The Mets' offense had been extremely hot recently, including 9, 7, 15 and then 12 runs in notable recent games.
- The immediately preceding **12-2 Mets win is not used as a continuation signal**. Its only decision-driving consequences are today's lineup/health and bullpen workload.
- The Mets hit six homers Saturday, but that occurred against Gerrit Cole and lower-leverage relief, not Schlittler; it does not transfer as an automatic HR/Over coefficient.

#### Bullpen chain / availability

**Mets**
- Thornton worked 7 innings Saturday and **Tobias Myers handled the final 2 scoreless innings**, so the broader high-leverage relief group was largely spared.
- Common 2026 relief names in the retrieved staff listing include Devin Williams, Brooks Raley, Luke Weaver and Huascar Brazobán.
- This gives the Mets a meaningful freshness branch if Scott exits around his normal 4.5-5.0 innings.

**Yankees**
- Gerrit Cole lasted only 4.1 innings Saturday, requiring **4.2 bullpen innings**; Bradley Hanner was among the relievers used in the blowout.
- David Bednar worked 1.2 innings Friday for the save but appears to have been spared Saturday.
- Recent bullpen reinforcements Michael Fulmer and John Schreiber add depth; Schreiber entered this series with four-plus hitless innings after joining New York in the cited analysis.
- Workload is treated as availability only, not as a performance coefficient.

Bullpen conclusion:
- Mets have the cleaner broad freshness profile.
- Yankees retain the better overall season pitching environment and a rested/partly rested high-leverage path if Schlittler works deep.

#### Park / weather / termination branch

- Exact Yankee Stadium structured weather around 13:29 EDT: **72°F / 22°C, rain**.
- Forecast showed roughly **75% rain probability through 14:00-16:00**.
- Multiple live scoreboard threads linked to MLB Gameday reported **Delayed Start: Wet Grounds** before scheduled first pitch.
- A current game thread reported ~5 mph wind **in from left field**, but this is secondary and too weak to receive a large signed coefficient.
- No field-owner resumption/start time was recovered at the freeze.

Weather treatment:
- **No automatic Under** for rain.
- Pre-start delay leaves open two main states:
  1. delayed first pitch but both starters retain normal preparation → central model mostly unchanged;
  2. prolonged/interrupted conditions reduce starter length or create a midgame restart → more bullpen exposure and larger upper tail.
- Operator suspension/shortened-game/action rules were not supplied, so any postponement/shortened-final settlement remains `UNKNOWN_DEFINITION`.

#### Joint run object

**Mets run centre**
- Season offense: 4.29 R/G.
- Yankees season run prevention: 3.67 RA/G.
- Base cross-opponent midpoint ≈ **3.98**.
- Schlittler's elite current starter regime and expected 6+ inning exposure: **−0.9**.
- Mets current top-of-order quality/hot-contact branch + fresher bullpen opposing late-game Yankee relief uncertainty: **+0.1**.
- Working Mets centre ≈ **3.0**.

**Yankees run centre**
- Season offense: 4.58 R/G.
- Mets season run prevention: 4.58 RA/G.
- Base midpoint = **4.58**.
- Scott's better-than-team-average FIP/xERA and HR suppression: **−0.3**.
- Scott short-hook/walk exposure + home last-bat / Yankee power cluster: **+0.1**.
- Working Yankees centre ≈ **4.4**.

**Total centre:** **7.4 runs**.  
**Run differential centre:** Yankees **+1.4**.  
**Total width:** ~4.1 runs.  
**Margin width:** ~3.8 runs.

Normalised edges:
- Run line: `|1.4 - 1.5| / 3.8 ≈ 0.03`.
- Total: `|7.4 - 8.0| / 4.1 ≈ 0.15` toward Under.

The total has the clearer centre-vs-line distance, but weather-delay/relief-cluster uncertainty prevents high confidence.

#### Discrete run-line families

| Final margin family | Probability |
|---|---:|
| Yankees by 4+ | **22%** |
| Yankees by 2-3 | **27%** |
| Yankees by exactly 1 | **14%** |
| Mets win | **37%** |

Derived:
- Yankees winner: **63%**
- Mets winner: **37%**
- **Yankees -1.5 = 49%**
- **Mets +1.5 = 51%**

Home-last-bat matters: some Yankees-leading states omit a bottom ninth, modestly supporting the Mets +1.5 cushion relative to a neutral-inning-count margin model.

#### Total families / push handling at 8.0

| Total runs | Probability |
|---|---:|
| 0-6 | **34%** |
| exactly 7 | **18%** |
| **exactly 8** | **11%** |
| 9-10 | **19%** |
| 11+ | **18%** |

Derived:
- **Under 8.0 = 52% win / 11% push / 37% loss**
- **Over 8.0 = 37% win / 11% push / 52% loss**

#### Mandatory baseball branches

- **Central:** Schlittler 6-7 strong innings; Scott 4.5-5.5 competitive innings; Yankees 4-3.
- **Schlittler dominance / low-Mets-score:** 5-1 / 4-1 / 3-0; supports Yankees winner, often -1.5 and Under.
- **Scott walk/short-hook cluster:** early baserunners, Yankees homer or inherited-run scoring, Mets middle relief exposed; supports Yankees -1.5 and Over.
- **Mets hot-lineup contact branch:** Lindor/Soto/Bichette/Benge create early extra-base damage before Schlittler settles; supports Mets +1.5 and Over.
- **Bullpen-compression branch:** both leverage groups execute after central starts; 3-2 / 4-2 / 4-3 type Under states.
- **Weather/restart branch:** prolonged delay or later interruption shortens one/both starters and widens the total; no automatic sign.
- **Home-ninth branch:** Yankees lead after top 9 and do not bat bottom 9; supports Under and some Mets +1.5 states.
- **Extra-inning ghost-runner branch:** tie after nine enters a higher run-rate environment; materially damages Under and can flip the run line.

#### Representative Rank-1 compatible state

**Yankees 4 – Mets 3**
- Under 8.0: **WIN**
- Mets +1.5: **WIN**
- Yankees -1.5: loss
- Over 8.0: loss
- Potential winner Yankees: **WIN**

This is a compatibility demonstration, not the source of the probabilities.

#### Complement / kill paths (`G-L9`)

| Selection | Win | Push | Loss | Main failure paths |
|---|---:|---:|---:|---|
| Under 8.0 | 52% | 11% | 37% | prolonged delay/early hook; Scott walk + HR cluster; hot Mets top order; extras ghost-runner scoring |
| Mets +1.5 | 51% | — | 49% | Schlittler domination plus Yankees 2+ run cluster; Scott exits early with inherited runners; Mets bullpen middle-relief failure |
| Yankees -1.5 | 49% | — | 51% | low total + one-run Yankees win; home ninth not played; Mets fresh relief chain keeps game compressed |
| Over 8.0 | 37% | 11% | 52% | Schlittler extends 6-7 innings; Yankees staff suppresses Mets; wet/inward-wind contact suppression; leverage relief closes game |

#### Top-two joint probability (`G-L10`)

`P(Under 8.0 win ∧ Mets +1.5) ≈ 33%`.

Coupling: **moderately positive but not deterministic**.
- 4-3, 3-2 and 4-2 Yankees wins can win both.
- A 5-1 Yankees win wins Under but loses Mets +1.5.
- A 6-5 Mets/Yankees game can win Mets +1.5 while losing Under.
- Exactly eight total runs pushes Rank 1 and can still settle the run line.

#### Card completeness

| Requirement | State |
|---|---|
| MLB identity / venue / scheduled innings / home last bat | PASS |
| Official probable starters | PASS |
| Starter advanced process | PASS |
| Same-day posted batting orders | PASS WITH LIMITATION — current secondary posted orders; MLB indexed lineup page lagged |
| Catchers / defensive positions | PASS from posted orders |
| Material injury/return context | PASS |
| Starter hook / BF exposure | PASS |
| Bullpen workload / likely chain | PASS WITH LIMITATION |
| Season + recent offense/pitching | PASS |
| Park / weather | PASS |
| Delay / termination branch | PASS; operator action terms unknown |
| Home ninth / extras | PASS |
| Discrete run-line families | PASS |
| Integer-total push mass | PASS |
| Joint cluster / early-hook tails | PASS |
| Normalised edges | PASS |
| Complement kill paths | PASS |
| `P(R1 ∧ R2)` | PASS |
| Final volatile refresh | PASS at 13:32 EDT |
| Settlement source | MLB official final/gamebook; operator action terms govern weather-related void/suspension handling |

#### Sources used for P-416

| Source | Role |
|---|---|
| Google Drive `METHOD.md`, `CONTROLS.md` | Governing lifecycle / market-blind / coherence controls |
| Google Drive `RULES_BASEBALL.md` | starter/order gates, hook, bullpen, weather, home ninth, extras, cluster tails |
| MLB probable pitchers | Official Scott / Schlittler starter handshake |
| Baseball Savant — Schlittler | Official Statcast/season line |
| Pitcher List — Schlittler / Scott | xERA/FIP/xFIP/K-BB/SwStr cross-check |
| Baseball-Reference pregame preview | current records / recent windows / RHP splits / season series |
| Baseball-Reference team batting/pitching | season R/G, RA/G, ERA |
| StatMuse Schlittler last five | current starter regime |
| StatMuse Yankees pitching last 14 days | recent staff process |
| Same-day Mets/Yankees game threads | posted orders and current player placement |
| Reuters / team-focused recaps | recent series context, Judge return, Mets offense |
| Mets/Yankees game recap Sep 12 | bullpen workload consequence |
| Exact Yankee Stadium weather query | current rain / game-window precipitation |
| Live scoreboard threads linked to MLB Gameday | delayed-start / wet-grounds cross-check |

#### Public URLs recorded

- https://www.mlb.com/probable-pitchers/2026-09-13
- https://www.mlb.com/yankees/roster/probable-pitchers
- https://www.mlb.com/mets/roster/probable-pitchers
- https://baseballsavant.mlb.com/savant-player/cam-schlittler-693645
- https://pitcherlist.com/player/cam-schlittler/
- https://pitcherlist.com/player/christian-scott/
- https://www.baseball-reference.com/previews/2026/NYA202609130.shtml
- https://www.baseball-reference.com/teams/NYM/batteam.shtml
- https://www.baseball-reference.com/teams/NYM/pitchteam.shtml
- https://www.baseball-reference.com/teams/NYY/batteam.shtml
- https://www.baseball-reference.com/teams/NYY/pitchteam.shtml
- https://www.statmuse.com/mlb/ask/cam-schlittler-last-5-games-yankees
- https://www.statmuse.com/mlb/ask/yankees-era-last-14-days
- https://www.mlb.com/yankees/video/schlittler-fans-9-in-6-2-3-innings-in-yankees-win
- https://www.amazinavenue.com/new-york-mets-discussion/100629/mets-at-yankees-lineups-broadcast-info-and-open-thread-9-13-26-scott-schlittler
- https://www.pinstripealley.com/pinstripe-alley-discussions/207228/yankees-game-thread-mets-how-to-watch-subway-series-streaming-lineups-cam-schlittler

### P-417 — Chunichi Dragons @ Hanshin Tigers — NPB Central League — PRE-GAME / UNSETTLED

- **Scheduled start:** 2026-09-14 18:00 JST / 19:00 AEST.
- **Forecast freeze:** **2026-09-14 17:49:49 JST / 18:49:49 AEST**, before scheduled first pitch.
- **Venue:** Hanshin Koshien Stadium, Nishinomiya.
- **Method:** MDS-2026.09.06-v4.0 / SFA-BASEBALL / `SPORTS_ONLY / MARKET_BLIND`.
- **Rules:** 2026 Central League has no DH; regular-season tie remains possible after 12 innings; no automatic runner.
- **Settlement:** PENDING; no retrospective. Operator tie/action terms `UNKNOWN_DEFINITION`.

| Rank | Selection | `UNVALIDATED_SUBJECTIVE` p | Evidence |
|---|---|---:|---|
| 1 | **Chunichi Dragons +1.5** | **62%** | MEDIUM-LOW |
| 2 | **Under 5.5 runs** | **55%** | MEDIUM-LOW |
| 3 | **Over 5.5 runs** | **45%** | LOW-MEDIUM |
| 4 | **Hanshin Tigers -1.5** | **38%** | MEDIUM-LOW |

**Potential winner:** Hanshin 55%, Chunichi 39%, draw 6%.  
**Representative score:** Hanshin 3-2 Chunichi.  
**Continuous centre:** Hanshin ~2.9, Chunichi ~2.3 = 5.2 total / Hanshin +0.6.

#### Participant / starter freeze
Fresh current listings have **Masashi Itoh (Hanshin, LHP)** vs **Kyle Muller (Chunichi, LHP)**. NPB's indexed probable-starter page still surfaced the prior day's pairing during the research snapshot, while SportsNavi's Sep 14 page listed Itoh/Muller, so `BB-P1` remains PARTIAL/PROBABLE rather than falsely CONFIRMED_OFFICIAL.

Official NPB season lines: Itoh 9 G, 2-2, 46.0 IP, 41 H, 5 HR, 11 BB, 35 K, 13 ER, **2.54 ERA** (~5.1 IP/start); Muller 17 G, 6-7, 108.1 IP, 93 H, 10 HR, 23 BB, 86 K, 32 ER, **2.66 ERA** (~6.4 IP/start). Muller has the stronger normal length profile; Itoh has the slightly lower ERA.

No official Sep 14 batting-order/bench card was recovered before freeze. Chunichi catcher **Yuta Ishii was injured and replaced by Takuma Kato** in the Sep 13 game, and no official Sep 14 status was recovered. `BB-P2 = PARTIAL`; no player prop issued.

#### Team baseline / recent state
Official NPB baselines through Sep 12: Hanshin 454 R / 124 = **3.66 R/G**, .246/.316/.371, 111 HR; Chunichi 431 / 130 = **3.32 R/G**, .229/.301/.350, 108 HR. Hanshin pitching **2.85 ERA**, ~3.11 RA/G; Chunichi pitching **3.25 ERA**, ~3.42 RA/G.

Sep 13 ended Chunichi 1-0 Hanshin in 11 innings. The final itself is not a predictive trend. Workload consequence: Hiroto Takahashi threw 9 scoreless innings / 142 pitches; Chunichi then used Hiroto Mori and Shinya Matsuyama. Hanshin Saiki threw 9 scoreless; Kudo/Kinoshita handled extras, while the broader Hanshin leverage group was largely spared. Workload affects availability, not quality.

#### Joint run object
Hanshin base cross-opponent run prior ~3.54, adjusted down for Muller's 2.66 ERA / ~6.4-IP exposure and 2026 Central League pitcher-batting/Koshien environment → **~2.9**. Chunichi base prior ~3.22, adjusted down for Itoh 2.54 ERA + Hanshin 2.85 staff ERA and pitcher-batting environment, with a small short-hook relief add → **~2.3**.

**Total centre 5.2; total width ~3.2.** Normalised edge at 5.5 = `|5.2-5.5|/3.2 ≈ 0.09`, a small Under edge.

#### Run-line families
- Hanshin by 2+: **38%**
- Hanshin by exactly 1: **17%**
- Draw after 12: **6%**
- Chunichi by exactly 1: **16%**
- Chunichi by 2+: **23%**

Derived: Hanshin win 55%, Chunichi win 39%, draw 6%; **Dragons +1.5 62%**, **Tigers -1.5 38%**.

#### Total families
- 0-3 runs: **30%**
- 4-5: **25%**
- 6-7: **24%**
- 8+: **21%**

Derived: **Under 5.5 55%**, **Over 5.5 45%**.

#### Mandatory branches / kill paths
Central 3-2 Hanshin. Muller-control 2-1/2-2/1-0 states support Chunichi +1.5 and often Under. Itoh-control can produce 3-0/2-0, supporting Under while killing +1.5. Itoh short-hook/inherited-run states and a Hanshin power cluster (Morishita/Sato/Oyama) lift both Tigers -1.5 and Over. Chunichi right-handed damage against Itoh can win/cover and lift total. Catcher uncertainty is held mainly as width. Hanshin-leading states may remove bottom-nine batting exposure, mildly helping Under/+1.5. NPB extras have no ghost runner but can still add scoring; a tie can remain after 12.

#### Weather
Exact Koshien query near 17:46 JST: ~28°C, mostly cloudy/humid; precipitation ~44% at 18:00, 40% at 19:00, falling later. JMA-linked gale/high-wave/thunderstorm advisories were active for Nishinomiya. No verified delay/cancellation was recovered before freeze. Without exact field-level wind direction/speed or a stoppage, weather receives no signed total adjustment; it widens fly-ball, fielding and interruption/relief-transition tails.

#### Top-two dependence
`P(Dragons +1.5 ∧ Under 5.5) ≈ 40%`, moderately positive/state-dependent. 3-2, 2-1 and low-scoring tie/Chunichi states often win both; 3-0/4-1 Hanshin can win Under but lose +1.5, while 4-3 can win +1.5 but lose Under.

#### Completeness
Starter identity PARTIAL/probable; official posted lineups PARTIAL; Ishii catcher status unresolved; official NPB starter/team season stats PASS; bullpen workload PASS; NPB no-DH/tie/extras rules PASS; run-line decomposition incl draw PASS; total families PASS; weather/termination branch PASS; normalized edge/kill paths/top-two joint PASS; settlement source pre-registered to NPB official box score/native-language lane.

#### Sources
NPB official schedule, team standings, team batting/pitching and individual pitcher statistics; SportsNavi Sep 14 probable-starter listing and Sep 13 game/bench log; Hanshin official Sep schedule; Koshien stadium schedule; same-day Japanese reporting on Sep 13 extra-inning game/Ishii injury; structured Koshien weather/JMA-linked advisories.

Public URLs: https://npb.jp/games/2026/ ; https://npb.jp/games/2026/schedule_09_detail.html ; https://npb.jp/bis/teams/index_d.html ; https://baseball.yahoo.co.jp/npb/teams/4/stats?team_vs=1 ; https://baseball.yahoo.co.jp/npb/teams/5/schedule/?month=2026-09 ; https://baseball.yahoo.co.jp/npb/teams/4/schedule/?month=2026-09 ; https://baseball.yahoo.co.jp/npb/game/2021039417/score ; https://hanshintigers.jp/game/schedule/ ; https://koshien.hanshin.co.jp/event/202609.html


### P-418 — Drukpa FC vs Royal Thimphu College (RTC) FC — Bhutan Premier League — PRE-MATCH / UNSETTLED

- **User-supplied scheduled start:** 2026-09-14 22:00 AEST / 18:00 Bhutan time / 12:00 UTC.
- **Forecast freeze:** **2026-09-14 21:56:12 AEST / 17:56:12 Bhutan time**, before the user-supplied start.
- **Fixture-time conflict:** AiScore/Sofascore/other schedules list 12:00 UTC; TNT surfaced 13:00 UTC, while Drukpa's own website schedule appears stale and omits the Sep 14 fixture. RSSSF and multiple current fixture feeds independently list Drukpa–RTC on Sep 14. Card is issued against the user's 22:00 AEST / 12:00 UTC contract, with identity/time evidence capped.
- **Venue:** Changlimithang Stadium is Drukpa's stated home ground; some third-party fixture pages omit the venue.
- **Competition:** Bhutan Premier League, 90-minute regulation market.
- **Working ID:** P-418.
- **Method:** MDS-2026.09.06-v4.0; SFA-SOCCER; `SPORTS_ONLY / MARKET_BLIND`.
- **Performance status:** LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.
- **Settlement:** PENDING; no retrospective performed.
- **Participant gate:** `XI_NOT_RETRIEVED_BEFORE_FREEZE`; no player prop issued.

#### Issued ranking

| Rank | Selection | `UNVALIDATED_SUBJECTIVE` p | Evidence |
|---|---|---:|---|
| 1 | **Drukpa team goals Over 0.5** | **80%** | MEDIUM-LOW |
| 2 | **Drukpa or Draw (1X), 90 min** | **76%** | MEDIUM-LOW |
| 3 | **RTC team goals Under 1.5** | **70%** | MEDIUM-LOW |
| 4 | **Total corners Over 4.5** *(self-generated alternate; only if offered with standard full-match corner settlement)* | **65%** | LOW-MEDIUM |
| 5 | **1st Half Over 0.5 goals** | **58%** | LOW-MEDIUM |

**Supplied full-match total:** Over 2.5 = **52%**, Under 2.5 = **48%**.  
**Potential regulation winner:** Drukpa **47%**, Draw **29%**, RTC **24%**.  
**Representative score:** Drukpa **2-1** RTC.  
**Working goal centres:** Drukpa ~1.65, RTC ~1.12, total ~2.77.

#### Current table / scoring environment

Current reconstructed table after Sep 10/11:
- Drukpa: **14 matches, 27 GF, 22 GA, 17 pts**.
- RTC: **14 matches, 14 GF, 16 GA, 18 pts**.
The BFF standings page indexed during research was one match stale at 13 GP for both; RSSSF/current result feeds include the Sep 10 RTC and Sep 11 Drukpa matches.

Home/away split available before freeze:
- Drukpa home: ~**14 GF / 10 GA in 7** → 2.00 scored, 1.43 conceded.
- RTC away: ~**6 GF / 6 GA in 6** → 1.00 scored, 1.00 conceded.

Recent L5:
- Drukpa: L 1-2 Thimphu FC; D 2-2 Thimphu City; L 1-3 Paro; W 5-1 BFF Academy; W 3-2 Tsirang → **12 GF / 10 GA**.
- RTC: L 1-2 Thimphu City; L 0-1 Paro; L 1-2 Thimphu Raven; W 1-0 Ugyen Academy; D 0-0 BFF Academy → **3 GF / 5 GA**.

H2H:
- Only current-season meeting: RTC 1-1 Drukpa on Jun 13; HT 0-0; corners 2-2.
- H2H receives descriptive/continuity weight only, not an independent directional coefficient.

#### Goal arithmetic

**Drukpa centre**
- Drukpa home scoring 2.00 vs RTC away concession 1.00 → midpoint ~1.50.
- Recent Drukpa attacking output (12 in L5) adds a small current-process branch.
- Rain/lineup uncertainty held as width, not signed direction.
- Final centre ~**1.65**.

**RTC centre**
- RTC away scoring 1.00 vs Drukpa home concession 1.43 → midpoint ~1.22.
- RTC recent output only 3 goals in L5 gives a small negative current-process branch.
- Final centre ~**1.12**.

**Total centre:** ~**2.77 goals**.

Approximate goal-state masses:
- 0-1 goals: **24%**
- exactly 2: **24%**
- exactly 3: **22%**
- 4+: **30%**

Derived:
- Over 2.5 ≈ **52%**
- Under 2.5 ≈ **48%**
- Drukpa O0.5 ≈ **80%**
- RTC U1.5 ≈ **70%**

Winner object is widened from the raw independent-goal centre because confirmed XIs/bench were unavailable and rain is active:
- Drukpa **47%**
- Draw **29%**
- RTC **24%**
- Drukpa/Draw **76%**

#### First-half process

Historical/current evidence is mixed:
- The Jun 13 H2H was 0-0 at HT.
- Drukpa had five consecutive 0-0 first halves from May 25 through Jul 7, but its later games became much more first-half active: BFF 1-1, Tsirang 1-0, Paro 0-3, Thimphu City 0-1, Thimphu FC 0-1.
- RTC also had a long early-season 0-0-HT pattern, but conceded a first-half goal in recent losses to Paro and Thimphu City and had a first-half goal state against Thimphu Raven.

Small-sample/current-regime reconciliation:
- 0 first-half goals: **42%**
- exactly 1: **39%**
- 2+: **19%**
- **1H O0.5 = 58%**.

The older slow-start pattern prevents promotion above the stronger full-game/team rows.

#### Corner process

Direct observed corner samples, not possession proxies:

**Drukpa recent**
- at Thimphu FC: **5** corners (match total 9)
- vs Thimphu City: **0** (total 9)
- vs Paro: **5** (total 7)
- at Transport United: **4** (total 10)
- vs Tensung: **4** (total 6)
- at RTC: **2** (total 4)

**RTC recent**
- vs Thimphu City: **2** (total 7)
- at Paro: **3** (total 6)
- vs Thimphu Raven: **5** (total 9)
- vs BFF Academy: provider recorded **0** (total 0; treated as a possible low-event/data-quality tail)
- vs Drukpa: **2** (total 4)

Observed total-corner sample clears 4.5 in most recent data-rich games, but data quality is materially weaker than for major leagues.

Working corner total centre ~**6.2**, wide width ~**3.1**:
- 0-4 corners: **35%**
- 5-7: **37%**
- 8+: **28%**
- **O4.5 corners = 65%**.

This is a self-generated alternate and should be used only if the operator offers a standard full-match total-corners 4.5 contract. No inference from shots/possession alone is used.

#### Participant / availability research

No trustworthy official matchday XI, goalkeeper confirmation, full bench or current injury/suspension list was retrievable before the freeze.

Known current squad/core evidence:
- Drukpa season records include GK Sachin Jha and regulars such as Phuntsho Jigme, Woo Gyeong-yun, Philip Eugine, Kencho Tobgay and Leon Sullivan Taylor; coach Dorji Khandu is confirmed by BFF/club material.
- RTC current roster sources include captain Yeshey Gyeltshen and players such as Jigdrel Wangchuk, Kinzang Tenzin, Jun-young Park, Sardor Jakhonov and others; BFF identifies Ugyen Dorji as head coach.
- Old Drukpa red-card suspensions from June are not carried forward without current suspension evidence.
- No player is assumed healthy merely because no current injury report was found.

Under RULES_SOCCER, the missing confirmed XI/GK/bench caps player- and exact-side-strength confidence. Hence no scorer, SOT or player-minute prop is issued.

#### Weather / surface

Exact Changlimithang query near 17:55 Bhutan time:
- **~16°C, rain**
- precipitation ~**60% at 18:00**, ~49% at 19:00, ~51% at 20:00.
- No verified pitch/surface problem or postponement was recovered before freeze.

Weather is carried as **distribution width only**. Rain is not automatically an Under/corner sign without a verified footing, drainage, wind or tactical mechanism.

#### Representative compatibility state

Drukpa 2-1 RTC, HT 1-0, 6 total corners:
- Drukpa O0.5: WIN
- Drukpa/Draw: WIN
- RTC U1.5: WIN
- corners O4.5: WIN
- 1H O0.5: WIN
- O2.5: WIN

Compatibility only; this state did not generate the rankings.

#### Complement / kill paths (`G-L9`)

| Selection | Win p | Loss p | Main failure paths |
|---|---:|---:|---|
| Drukpa O0.5 | 80% | 20% | RTC's compact low-event defence; rain/finishing variance; missing-XI attacking downgrade |
| Drukpa/Draw | 76% | 24% | RTC repeats disciplined away profile; transition/set-piece winner; Drukpa defensive errors |
| RTC U1.5 | 70% | 30% | Drukpa open game-state lets RTC counter; set pieces; red-card/penalty state |
| Corners O4.5 | 65% | 35% | low-event midfield game; early goal reduces chase width; provider-data uncertainty |
| 1H O0.5 | 58% | 42% | both teams revert to long 0-0-HT pattern; rain/slow opening; finishing variance |
| Supplied O2.5 | 52% | 48% | RTC scoring remains suppressed and Drukpa wins 1-0/2-0; early control state |

#### Top-two joint (`G-L10`)

`P(Drukpa O0.5 ∧ Drukpa/Draw) ≈ 68%`.

Coupling: **strong positive, not identity**.
- Drukpa can score and still lose.
- A 0-0 draw wins 1X but loses Drukpa O0.5.

#### Completeness

| Requirement | State |
|---|---|
| Fixture identity/date | PASS with source conflict disclosed |
| Exact kickoff | **PARTIAL / conflicting sources** |
| Competition / 90-min endpoint | PASS |
| Confirmed XI / GK / full bench | **FAIL-PARTIAL; not retrieved** |
| Current injury/suspension list | **PARTIAL / unavailable** |
| L5 / longer form | PASS |
| H2H continuity | PASS |
| Goal process | PASS |
| Separate corner process | PASS, sparse data |
| Current weather | PASS |
| Surface problem check | PARTIAL; none verified |
| Joint states / complements / top-two joint | PASS |
| Final pregame freeze | PASS at 21:56:12 AEST |
| Settlement source | BFF/native Bhutan source lane + corroborated final stats |

#### Sources

- Bhutan Football Federation 2026 standings/news and BPL reports.
- BFF official Jun 13 RTC–Drukpa match report.
- BFF preseason press conference for coaches.
- RSSSF Bhutan 2026 table/results.
- Drukpa FC official site for home ground/club identity (noted schedule staleness).
- RTC/college official pages for club/captain identity.
- TotalCorner Bhutan Premier League for field-defined corner samples.
- Camel Live / NetScores / AiScore / SoccerPunter for cross-checked match-level stats/HT states.
- Sofascore/AiScore/RSSSF for current fixture corroboration.
- Exact Changlimithang weather source.

Public URLs:
- https://bhutanfootball.org/
- https://bhutanfootball.org/2026/
- https://bhutanfootball.org/rtc-fc-and-drukpa-fc-share-spoils-in-thrilling-1-1-draw-at-rtc-artificial-turf/
- https://bhutanfootball.org/voices-set-season-ready-bpl-2026-pre-season-press-conference-concludes/
- https://www.rsssf.org/tablesb/bhutan2026.html
- https://www.drukpafc.com/
- https://my.rtc.bt/student-services/rtc-fc
- https://www.totalcorner.com/league/view/15293
- https://www.totalcorner.com/stats/rtc-fc-vs-drukpa-fc/196049328
- https://www.aiscore.com/en/match-drukpa-fc-rtc-fc/wv78xiv099gbokr
- https://www.sofascore.com/football/match/drukpa-royal-thimphu-college-fc/YfrdscuMj

### P-419 — Djurgårdens IF vs GAIS — Sweden Allsvenskan — PRE-MATCH / UNSETTLED

- **Scheduled kickoff:** 2026-09-14 19:00 CEST / 2026-09-15 03:00 AEST.
- **Forecast freeze:** **2026-09-14 18:53:55 CEST / 2026-09-15 02:53:55 AEST**, before scheduled kickoff.
- **Venue:** 3Arena, Stockholm.
- **Competition:** Allsvenskan regular season, Matchweek 21, 90-minute endpoint.
- **Working ID:** P-419.
- **Method:** MDS-2026.09.06-v4.0; SFA-SOCCER; `SPORTS_ONLY / MARKET_BLIND`.
- **Performance status:** LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.
- **Settlement:** PENDING. No retrospective performed.
- **Participant gate:** `XI_NOT_RETRIEVED_BEFORE_FREEZE`; no player prop issued.

#### Issued ranking

| Rank | Selection | `UNVALIDATED_SUBJECTIVE` p | Evidence |
|---|---|---:|---|
| 1 | **Djurgården team goals Over 0.5** | **84%** | MEDIUM |
| 2 | **Djurgården or Draw (1X)** | **83%** | MEDIUM |
| 3 | **GAIS team goals Under 1.5** | **79%** | MEDIUM |
| 4 | **Under 3.5 total goals** | **70%** | MEDIUM-LOW |
| 5 | **Total corners Over 7.5** *(self-generated alternate, if standard full-match corner settlement is offered)* | **69%** | MEDIUM-LOW |

**Supplied 1H 0.5:** Over 0.5 = **62%**, Under 0.5 = **38%**.  
**Supplied full-game 2.5:** Under 2.5 = **51%**, Over 2.5 = **49%** — essentially a pass.  
**Potential winner:** Djurgården **60%**, Draw **23%**, GAIS **17%**.  
**Representative score:** Djurgården **2-0** GAIS.  
**Working goal centres:** Djurgården ~1.83, GAIS ~0.85, total ~2.68.

#### Identity / fixture / schedule

- Djurgården official preview: Monday 14 Sep, 19:00 CEST at 3Arena.
- GAIS official site independently lists the same date/time/venue.
- Allsvenskan's published 2026 order includes Djurgården-GAIS in Matchweek 21.
- User time 03:00 AEST is consistent with 19:00 CEST.

#### Current table / form

Through 20 Allsvenskan matches:
- Djurgården: **12-2-6, 44 GF, 19 GA, 38 pts**, 2nd.
- GAIS: **7-6-7, 25 GF, 18 GA, 27 pts**, 9th/10th depending source update order.

Djurgården last five league:
- L 1-3 AIK
- W 3-0 Malmö
- W 4-0 Mjällby
- W 2-0 Mjällby
- W 1-0 Kalmar
→ **11 GF / 3 GA**, four straight league wins and four straight clean sheets.

GAIS last five league:
- W 2-0 Halmstad
- L 0-1 Malmö
- L 0-2 Hammarby
- W 4-0 Brommapojkarna
- D 0-0 Häcken
→ **6 GF / 3 GA**.

Home/away:
- Djurgården home: roughly **27 GF / 12 GA in 10**.
- GAIS away: roughly **9 GF / 14 GA in 9**.

Current xG context:
- Djurgården's most recent available season xG line was close to **2.0 xG/game** with xGA around **1.2/game**.
- GAIS have defended materially better in actual goals than their earlier xGA profile, so their low concession rate is not assumed to persist perfectly.
- Published external match predictions/odds were excluded from the active feature set.

#### Participant / availability state

**Djurgården**
- Official pre-match article said the match squad would be published one hour before kickoff, but the indexed field-owner source did not expose the final XI/bench before freeze.
- Latest league XI (Kalmar, Sep 7): Jacob Rinne; Piotr Johansson, Miro Tenho, Jacob Une, Max Larsson; Christos Almyras, Bo Hegland, Matias Siltanen, Patric Åslund; Kristian Lien, Jeppe Okkels.
- Djurgården rotated heavily in the Sep 10 Swedish Cup 7-1 win over Haninge: Lukas Jonsson; Adam Ståhl, Daryl Tschoumy, Mikael Marques, Max Larsson; Christos Almyras, Alexander Johansson; Peter Langhoff, Sander Ringberg, Oskar Fallenius; Alexander Andersson.
- Therefore the six-matches-in-three-weeks congestion is real, but many core league starters received meaningful rest in the cup.
- No decisive new Djurgården injury was confirmed in the official pre-match material.

**GAIS**
- **Róbert Frosti Þorkelsson: confirmed ACL rupture**, official GAIS, Sep 10.
- Official Sep 4 squad note: Samuel Salter rested after a knock; Mohamed Bawa and Christos Gravius had physical concerns; Robin Wendin Thomasson and Lucas Hedlund were still building up; Gustav Lundgren and Kevin Holmén long-term injured.
- Djurgården's official preview also flagged goalkeeper Mergim Krasniqi as a question after a recent head injury.
- Secondary current trackers list several of those GAIS players as unavailable, but no field-owner final matchday squad was recovered pre-freeze; exact Salter/Krasniqi status therefore remains unresolved rather than assumed.
- No player prop issued.

#### Goal arithmetic

**Djurgården centre**
- Home scoring 2.7 vs GAIS away concession ~1.56 → raw midpoint ~2.13.
- GAIS strong season defence/current low concession profile → downward shrink.
- Þorkelsson ACL + unresolved keeper/availability branch → small upward width/centre restoration.
- Congestion → small negative, mitigated by Sep 10 cup rotation.
- Final centre ~**1.83**.

**GAIS centre**
- Away scoring ~1.0 vs Djurgården home concession ~1.2 → midpoint ~1.10.
- Djurgården four straight league clean sheets + current defensive continuity → downward adjustment.
- GAIS attacking availability uncertainty → small downward adjustment.
- Final centre ~**0.85**.

**Total centre:** ~**2.68 goals**.

Approximate full-time state masses:
- 0-1 goals: **25%**
- exactly 2: **26%**
- exactly 3: **19%**
- 4+: **30%**

Derived:
- Under 2.5 ≈ **51%**
- Over 2.5 ≈ **49%**
- Under 3.5 ≈ **70%**
- Djurgården O0.5 ≈ **84%**
- GAIS U1.5 ≈ **79%**

Winner:
- Djurgården **60%**
- Draw **23%**
- GAIS **17%**
- Djurgården/Draw **83%**

#### First-half process

Recent first-half evidence is mixed and less compelling than the full-game team markets:
- Djurgården's 1-0 at Kalmar was 0-0 HT.
- Djurgården's 2-0 away win at Mjällby was 0-0 HT.
- The 3-0 Malmö win had a first-half Djurgården goal.
- GAIS' latest five include 0-0 HT states against Häcken, Malmö and Halmstad, while the Brommapojkarna and Hammarby matches had first-half scoring.

Working first-half states:
- 0 goals: **38%**
- exactly 1: **42%**
- 2+: **20%**
- **1H O0.5 = 62%**.

This is a positive lean but not strong enough for the top five.

#### Corner process

Direct recent corner samples:

**Djurgården last 10 team corners**
6, 3, 4, 7, 5, 7, 5, 6, 13, 10
- mean **6.6**
- sample SD ~**2.95**
- SE ~**0.93**

**GAIS recent opponent corners**
5, 4, 8, 3, 7, 2, 5, 6, 4, 6
- mean **5.0**
- SD ~**1.83**
- SE ~**0.58**

**Djurgården match-total corners last 10**
9, 3, 5, 10, 6, 11, 6, 12, 16, 17
- mean **9.5**
- SE ~**1.47**

**GAIS match-total corners last 10**
8, 11, 9, 11, 14, 3, 15, 14, 9, 12
- mean **10.6**
- SE ~**1.13**

Mechanism:
- Djurgården's home attack produces sustained final-third entries and shot/cross volume.
- GAIS can also generate corners when trailing, but their low-event defensive games create a real floor branch.
- No corner probability is inferred from possession alone.

Working total-corner centre ~**9.3**, width ~**3.4**.
- 0-7: **31%**
- 8-10: **39%**
- 11+: **30%**
- **Total corners O7.5 = 69%**.

#### Weather / venue

- 3Arena has a **retractable roof**.
- Stockholm around 19:00 CEST: ~**15°C**, mostly cloudy; ~14°C at 20:00, ~13°C at 21:00.
- No verified pre-freeze roof-state announcement was recovered.
- Weather therefore receives no signed goal/corner coefficient; roof uncertainty and cool conditions are width only.

#### Representative compatibility state

Djurgården 2-0 GAIS, HT 1-0, 9 total corners:
- Djurgården O0.5: WIN
- Djurgården/Draw: WIN
- GAIS U1.5: WIN
- Under 3.5: WIN
- Corners O7.5: WIN
- 1H O0.5: WIN
- Under 2.5: WIN

Compatibility illustration only.

#### Complement / kill paths (`G-L9`)

| Selection | Win p | Loss p | Main failure paths |
|---|---:|---:|---|
| Djurgården O0.5 | 84% | 16% | GAIS low block/keeper performance; fatigue; finishing variance |
| Djurgården/Draw | 83% | 17% | GAIS transition/set piece; Djurgården rotation error; early red-card/penalty branch |
| GAIS U1.5 | 79% | 21% | Djurgården chase state opens transition space; set pieces; defensive errors |
| Under 3.5 | 70% | 30% | early goal destabilises shape; GAIS forced chase; Djurgården current finishing ceiling; red card |
| Corners O7.5 | 69% | 31% | early control with few blocked/end-line actions; GAIS low-event shell; efficient finishing suppresses repeat attacks |
| 1H O0.5 | 62% | 38% | recent 0-0 HT pattern repeats; cautious GAIS block; Djurgården congestion |
| U2.5 | 51% | 49% | 2-1/3-0/3-1 scoring branch; GAIS defensive absences; current Djurgården attacking form |

#### Top-two joint (`G-L10`)

`P(Djurgården O0.5 ∧ Djurgården/Draw) ≈ 77%`.

Coupling: **strong positive, not identity**.
- Djurgården can score and still lose.
- A 0-0 draw wins 1X but loses the team-goal selection.

#### Completeness

| Requirement | State |
|---|---|
| Fixture / kickoff / venue / 90-min endpoint | PASS |
| Current Drive soccer method | PASS |
| Confirmed XI / GK / full bench | **PARTIAL / not retrieved before freeze** |
| Latest league XI / cup rotation | PASS |
| GAIS official injury information | PASS with unresolved late statuses |
| L5 / season / home-away form | PASS |
| xG/context | PASS with source-age caveat |
| Separate corner process | PASS |
| Small-sample corner SE | PASS |
| Weather / roof | PASS with roof-state limitation |
| Goal-state arithmetic | PASS |
| Complement kill paths | PASS |
| Top-two joint | PASS |
| Final pre-kickoff freeze | PASS at 18:53:55 CEST |
| Settlement source | Allsvenskan/club official final + trusted field-stat source |

#### Sources

- Djurgården official Sep 13 preview and Sep 10 cup report.
- GAIS official fixture page, Sep 10 ACL announcement, Sep 4 squad/availability note.
- Allsvenskan official schedule.
- FotMob current match page for availability cross-check/top-scorer context.
- FBref/current result records for Djurgården.
- FootyStats for home/away split context.
- Statz direct corner match logs for both teams.
- xGscore for season xG context only; its match prediction was excluded.
- Stockholm/3Arena venue and structured weather data.

Public URLs:
- https://www.dif.se/nyheter/2026/infor-djurgarden-gais
- https://www.dif.se/nyheter/2026/malkalas-pa-stadion-nar-dif-avancerade-i-cupen
- https://www.dif.se/nyheter/2026/infor-ifk-haninge-djurgarden
- https://www.gais.se/index.html
- https://www.gais.se/nyheter/frosti-thorkelsson-korsbandsskadad
- https://www.gais.se/nyheter/truppen-till-gais---bk-hacken-5-9
- https://allsvenskan.se/nyheter/spelordningen-klar-for-2026/
- https://www.fotmob.com/en-GB/matches/gais-vs-djurgarden/2pixbs
- https://fbref.com/en/squads/9423c05a/2026/matchlogs/all_comps/schedule/Djurgarden-Scores-and-Fixtures-All-Competitions
- https://footystats.org/clubs/djurgardens-if-659
- https://footystats.org/clubs/gais-679
- https://statz.ai/team/djurgarden/corners
- https://statz.ai/team/gais/corners
- https://xgscore.io/xg-statistics/sweden-allsvenskan
- https://foretagsservice.stockholm/hitta-plats-lokal-och-anlaggning-for-evenemang/evenemangsanlaggning/3arena

### P-420 — Atlanta Braves @ Chicago Cubs — MLB — PRE-GAME / UNSETTLED

- **Scheduled first pitch:** 2026-09-14 18:40 CDT / 19:40 EDT / 2026-09-15 09:40 AEST.
- **Forecast freeze:** **2026-09-14 18:26:43 CDT / 2026-09-15 09:26:43 AEST**, before scheduled first pitch.
- **Venue:** Wrigley Field, Chicago.
- **Competition:** MLB regular season.
- **Method:** MDS-2026.09.06-v4.0 / SFA-BASEBALL / SPORTS_ONLY / MARKET_BLIND.
- **Working ID:** P-420.
- **Performance status:** LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.
- **Settlement:** PENDING. No retrospective performed.
- **Operator listed-pitcher/action/suspension terms:** UNKNOWN_DEFINITION.

#### Issued ranking

| Rank | Selection | `UNVALIDATED_SUBJECTIVE` p | Evidence |
|---|---|---:|---|
| 1 | **Atlanta Braves +1.5** | **57%** | MEDIUM-LOW |
| 2 | **Over 9.5 total runs** | **53%** | LOW-MEDIUM |
| 3 | **Under 9.5 total runs** | **47%** | LOW-MEDIUM |
| 4 | **Chicago Cubs -1.5** | **43%** | MEDIUM-LOW |

**Potential winner:** Chicago Cubs **56%**, Atlanta Braves **44%**.  
**Representative central score:** Cubs **5-4** Braves.  
**Continuous centre:** Cubs ~4.9, Braves ~4.6, total ~9.5, Cubs margin ~+0.3.

Only Braves +1.5 and Over 9.5 are preferred directions.

#### Starter identity / exposure

Official MLB Sep 14 probable-pitcher listing:
- ATL: **Reynaldo López, RHP — 4-4, 4.13 ERA, 71 SO**
- CHC: **David Peterson, LHP — 7-8, 5.28 ERA, 117 SO**

`BB-P1 = PASS`.

**López return ladder**
- Jul 21 vs SD: 4.1 IP, 9 H, 5 ER, 3 BB, 6 K.
- Jul 26 at BAL: 5.2 IP, 5 H, 0 ER, 1 BB, 6 K.
- IL from late July with left-knee inflammation.
- Sep 3 rehab: five scoreless innings; exact pitch count not recovered.
- Sep 9 vs TB return: **4.2 IP, 7 H, 6 ER, 3 BB, 5 K**.
He is modelled around ~4.5-5.5 innings with a real early-hook branch, not as a normal six-plus-inning starter.

**Peterson current regime**
- Official full-season ERA: 5.28.
- Same-day Cubs preview reports **3.17 ERA / 49 K over his latest 11 games/appearances**.
- Recent starts: Sep 8 at MIL 4.1 IP/1 ER; Sep 2 vs MIL 3.2/6 ER; Aug 28 vs CIN 5.0/2 ER; Aug 22 at SEA 6.0/2 ER.
Season prior is shrunk toward this better current regime, but his length/efficiency remains variable.

#### Pregame batting orders

Current pregame sources corroborated:

**Atlanta:** Acuña RF; Baldwin DH; Olson 1B; Albies 2B; Harris CF; Dubón LF; Riley 3B; Murphy C; Kim SS.

**Chicago:** Crow-Armstrong CF; Suzuki RF; Busch 1B; Bregman 3B; Happ LF; Hoerner SS; Conforto DH; Ramírez 2B; Kelly C.

MLB's indexed lineup page still showed TBD in its crawl snapshot, so `BB-P2 = PASS WITH SOURCE LIMITATION`.

#### Injuries / roster

**Atlanta**
- Lane Thomas IL, strained left intercostal.
- Bryce Elder IL after right-knee surgery.
- Robert Suarez remains unavailable with elbow/forearm issue.
- López is a recent IL return.
- Owen Murphy recalled Sep 14, adding bulk/long-relief depth.

**Chicago**
- Edward Cabrera activated Sep 12 and available from bullpen.
- Trent Thornton IL, left-ankle sprain.
- Ian Happ has a minor foot issue but is in the current order.
- No major top-order scratch was recovered before freeze.

#### Team baseline

2026:
- Atlanta offense: **4.62 R/G**, .247/.310/.410, 187 HR.
- Chicago offense: **5.34 R/G**, .252/.340/.431, 206 HR.
- Atlanta pitching: **3.81 RA/G, 3.56 ERA**, 1.239 WHIP.
- Chicago pitching: **4.41 RA/G, 4.19 ERA**, 1.268 WHIP, 223 HR allowed.

Recent retrieved 10-game scoring:
- Atlanta: **45 runs**
- Chicago: **50 runs**
Recent totals are descriptive only.

#### Bullpen availability

**Atlanta**
- Grant Holmes only 4 IP Sunday.
- Ray Kerr threw 3 scoreless IP Sunday and is materially less available for length.
- Dylan Lee and Victor Mederos handled the seven-run eighth.
- Raisel Iglesias / Didier Fuentes were not the main Sunday workload in the retrieved recap.
- Robert Suarez remains out.
- Owen Murphy adds a bulk branch.

**Chicago**
- Matthew Boyd lasted 5.1 IP Sunday, requiring 3.2 bullpen IP.
- Aaron Civale was used in a meaningful Sunday state.
- Ryan Rolison worked 1.2 IP Saturday; Ryan Zeferjahn saved Saturday.
- Edward Cabrera is newly activated.
- Thornton unavailable.

Workload informs availability, not quality.

#### Weather / Wrigley

Exact structured weather near 18:25 CDT:
- ~21°C / 70°F
- mostly cloudy
- breezy at times
- no major rain signal during the game window.

Exact field-level wind direction/speed was not verified from a controlling source. Because Wrigley is wind-sensitive, **no signed HR/total weather coefficient** is applied.

#### Joint run object

**Atlanta centre**
- 4.62 R/G offense vs 4.41 Cubs RA/G → midpoint ~4.52.
- Peterson recent improvement: modest negative.
- Peterson variable length + Cubs 4.19 ERA/1.51 HR9 + Atlanta power: positive restoration.
- Working Atlanta centre ≈ **4.6**.

**Chicago centre**
- 5.34 R/G offense vs 3.81 Braves RA/G → midpoint ~4.58.
- López pre-injury talent lowers centre slightly.
- Return-from-IL / 4.5-5.5 IP exposure / Sep 9 contact branch raises it.
- Atlanta's better overall bullpen offsets part of that.
- Working Chicago centre ≈ **4.9**.

**Total centre:** ~9.5.  
**Margin centre:** Cubs +0.3.  
**Total width:** ~4.3.  
**Margin width:** ~4.0.

Normalized edge at 9.5: approximately **0.00**. The slight Over lean comes from asymmetric upper-tail branches, not a large centre-line gap.

#### Run-line families

| State | Probability |
|---|---:|
| Cubs by 4+ | 18% |
| Cubs by 2-3 | 25% |
| Cubs by exactly 1 | 13% |
| Braves win | 44% |

Derived:
- Cubs winner **56%**
- Braves winner **44%**
- Cubs -1.5 **43%**
- Braves +1.5 **57%**

#### Total families

| Total runs | Probability |
|---|---:|
| 0-7 | 27% |
| 8-9 | 20% |
| 10-11 | 26% |
| 12+ | 27% |

Derived:
- Over 9.5 **53%**
- Under 9.5 **47%**

#### Mandatory branches

- Central: Cubs 5-4.
- López good-return: 4-3/5-3 range, lower total.
- López early hook: Cubs reach middle relief early, supports Cubs separation + Over.
- Peterson improved: Atlanta 2-3 runs, supports Cubs + Under.
- Peterson walk/HR branch: Atlanta creates a cluster, supports Braves +1.5/win + Over.
- Two-offense HR cluster: 6-5/7-5 type state.
- Bullpen compression: leverage relief suppresses late scoring.
- Bullpen workload failure: secondary arms create late Over.
- Home ninth: Cubs-leading states may remove bottom ninth, mildly helping Braves +1.5/Under.
- Extras: automatic runner increases scoring rate materially.

#### Representative Rank-1/Rank-2 compatible state

**Cubs 6-5 Braves**
- Braves +1.5 WIN
- Over 9.5 WIN
- Under 9.5 LOSS
- Cubs -1.5 LOSS
- Cubs winner WIN

Central score remains 5-4; 6-5 only demonstrates compatibility.

#### Complement / kill paths

| Selection | Win | Loss | Main failure paths |
|---|---:|---:|---|
| Braves +1.5 | 57% | 43% | López return collapses; Cubs power cluster; Atlanta secondary relief exposed |
| Over 9.5 | 53% | 47% | Peterson improved regime; López rebound; leverage relief; neutral/inward wind |
| Under 9.5 | 47% | 53% | early hook; multi-HR inning; bullpen workload; extras |
| Cubs -1.5 | 43% | 57% | Atlanta reaches Peterson; one-run Cubs win; home ninth removed; Atlanta late relief |

#### Top-two joint

`P(Braves +1.5 ∧ Over 9.5) ≈ 30%`.

Coupling: near-neutral/slightly positive. Cubs 6-5 wins both; Cubs 5-4 wins the cushion but loses Over; Cubs 7-4 wins Over but loses the cushion.

#### Completeness

| Requirement | State |
|---|---|
| MLB identity / venue / scheduled innings | PASS |
| Official probable starters | PASS |
| López rehab/return ladder | PASS with pitch-count limitation |
| Current Peterson regime | PASS |
| Pregame batting order / catcher | PASS WITH SOURCE LIMITATION |
| Material injuries | PASS |
| Bullpen workload | PASS WITH LIMITATION |
| Season offense/pitching baselines | PASS |
| Weather | PASS |
| Exact Wrigley wind direction | PARTIAL / not verified |
| Home ninth / extras | PASS |
| Run-line decomposition | PASS |
| Total families | PASS |
| Kill paths / top-two joint | PASS |
| Final pregame freeze | PASS at 18:26:43 CDT |
| Settlement source | MLB official final/gamebook |

#### Source register

- Google Drive `RULES_BASEBALL.md` (MDS-2026.09.06-v4.0 / SFA-BASEBALL).
- MLB Sep 14 starting-lineup/probable-pitcher page.
- MLB Reynaldo López player/game-log page.
- MLB Braves injury/transaction pages.
- MLB Cubs transaction page.
- Baseball-Reference 2026 MLB batting and ATL/CHC team pitching tables.
- Baseball-Reference game preview.
- Reuters López activation; Sep 13 Braves/Cubs recaps.
- Battery Power same-day Braves lineup/starter/bullpen reporting.
- Bleed Cubbie Blue same-day Cubs preview.
- CBS/current pregame lineup corroboration.
- Structured Wrigley weather source.

Public URLs:
- https://www.mlb.com/starting-lineups/2026-09-14
- https://www.mlb.com/probable-pitchers/2026-09-14
- https://www.mlb.com/player/reynaldo-lopez-625643
- https://www.mlb.com/braves/roster/transactions
- https://www.mlb.com/braves/news/braves-injuries-and-roster-moves
- https://www.mlb.com/cubs/roster/transactions
- https://www.baseball-reference.com/leagues/majors/2026-standard-batting.shtml
- https://www.baseball-reference.com/teams/ATL/pitchteam.shtml
- https://www.baseball-reference.com/teams/CHC/pitchteam.shtml
- https://www.baseball-reference.com/previews/2026/CHN202609140.shtml

### P-421 — New York Yankees @ Minnesota Twins — MLB — PRE-GAME / UNSETTLED

- **Scheduled first pitch:** 2026-09-14 18:40 CDT / 19:40 EDT / 2026-09-15 09:40 AEST.
- **Forecast freeze:** **2026-09-14 18:34:41 CDT / 19:34:41 EDT / 2026-09-15 09:34:41 AEST**, before scheduled first pitch.
- **Venue:** Target Field, Minneapolis.
- **Competition:** MLB regular season.
- **Working ID:** P-421.
- **Method:** MDS-2026.09.06-v4.0; SFA-BASEBALL; `SPORTS_ONLY / MARKET_BLIND`.
- **Performance status:** LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.
- **Settlement:** PENDING. No retrospective performed.
- **Operator listed-pitcher/action/suspension terms:** `UNKNOWN_DEFINITION`.

#### Issued ranking — supplied slate

| Rank | Selection | Exact settlement probability | Evidence |
|---|---|---:|---|
| 1 | **New York Yankees -1.5** | **52% win / 48% loss** | MEDIUM-LOW |
| 2 | **Over 8.0 total runs** | **50% win / 12% push / 38% loss** | MEDIUM-LOW |
| 3 | **Minnesota Twins +1.5** | **48% win / 52% loss** | MEDIUM-LOW |
| 4 | **Under 8.0 total runs** | **38% win / 12% push / 50% loss** | LOW-MEDIUM |

**Potential winner:** **New York Yankees — 65%**, Minnesota **35%**.  
**Representative central score:** Yankees **5-3** Twins (8 total = push).  
**Rank-1/Rank-2 compatible score:** Yankees **6-3** Twins.  
**Working continuous centre:** Yankees ~**5.0**, Minnesota ~**3.7** → **8.7 total / Yankees +1.3**.

Only Yankees -1.5 and Over 8.0 are preferred directions.

#### Starter identity / source discrepancy

MLB official field-owner page confirms:
- **NYY: Will Warren, RHP — 10-6, 4.05 ERA, 141 SO**
- **MIN: Dean Kremer, RHP — 3-5, 5.65 ERA, 69 SO**

Several secondary previews still listed Bailey Ober, likely stale rotation planning. MLB official controls the starter identity, so the forecast uses **Dean Kremer**. No Ober statistics are used.

`BB-P1 = PASS`.

#### Will Warren current process

Season:
- ~142.1 IP
- 4.05 ERA
- 1.36 WHIP
- Savant xERA ~**4.48**
- FIP ~**4.16**
- K% ~**22.9%**
- BB% ~**7.9%**
- Hard-hit ~44%
- 21 HR allowed

Recent:
- Sep 9 vs COL: **6 IP, 1 ER, 8 K**
- Sep 4 at SD: **2.1 relief IP, 0 ER**
- Aug 30 vs BOS: **7 IP, 1 ER**
- Aug 25 vs HOU: **5 IP, 2 ER**
- Aug 19 at BAL: **4 IP, 2 ER**

The last few appearances are materially better than his season ERA, but xERA/FIP do not support treating him as an ace. The current-form improvement is therefore a positive branch, while season contact/HR risk remains in the width.

Central exposure: approximately **5.5-6.0 innings**, with an ordinary 4-5 inning hook branch.

#### Dean Kremer current process

Season:
- 71.2 IP
- **5.65 ERA**
- 1.30 WHIP
- **5.13 FIP**
- ~8.7 K/9
- 16 HR allowed (~2.0 HR/9)
- K% ~23%, BB% ~8%

Recent five:
- Sep 8 at DET: **5 IP, 2 ER**
- Sep 2 vs DET: **4 IP, 4 ER**
- Aug 28 vs CWS: **4 IP, 5 ER / 6 R**
- Aug 22 at SD: **5.1 IP, 2 ER**
- Aug 16 vs PHI: **5.1 IP, 4 ER**

Minnesota altered Kremer's pitch usage after acquiring him, including more splitter usage. That creates an improved-regime branch, but the recent results and season FIP/HR profile show the ordinary contact/HR tail remains substantial.

Central exposure: approximately **4.5-5.5 innings**.

#### Lineup / availability state

A fully field-owner-confirmed September 14 batting order was not recovered in the indexed snapshot before freeze, so `BB-P2 = PARTIAL` and no player prop is issued.

**Yankees major availability**
- Jazz Chisholm Jr.: IL, right-thumb sprain.
- Trent Grisham: IL, right-hamstring strain.
- Aaron Judge: recently activated from rib injury; same-day reporting indicates a slow initial return at the plate, treated as uncertainty rather than erasing elite baseline.
- Giancarlo Stanton: same-day team coverage lists him unavailable.
- Anthony Volpe was recalled recently, but current secondary lineup reporting had José Caballero at 2B.
- Jasson Domínguez optioned Sep 11.

Secondary current Yankees order was built around:
Ben Rice, Cody Bellinger, Aaron Judge, Luis García Jr., Spencer Jones, George Lombard Jr., Ryan McMahon, Austin Wells, José Caballero.

**Minnesota major availability**
- Byron Buxton: out / headed for season-ending right-hip surgery.
- Royce Lewis: exited Sep 13 with **left-shoulder soreness**; final Sep 14 availability was unresolved before freeze.
- Kaelen Culpepper recently had a shoulder contusion; X-rays showed no fracture, but final current status was not field-owner-confirmed.
- Austin Martin activated Sep 10.
- Emmanuel Rodriguez recalled Sep 12.
- Joe Ryan activated Sep 7.

Most recent actual Twins order before Lewis exited included Keaschall, Brooks Lee, Kody Clemens, Ryan Jeffers, Trevor Larnach, Royce Lewis, Emmanuel Rodriguez, Walker Jenkins and Ryan Kreidler.

The Buxton absence and unresolved Lewis shoulder state are meaningful Minnesota offensive-deficit branches.

#### Team environment

**Yankees 2026**
- **4.54 R/G**
- .235/.312/.409
- ~204 HR
- pitching **3.73 RA/G, 3.26 ERA, 1.169 WHIP**

**Twins 2026**
- **4.58 R/G**
- .244/.318/.405
- ~174 HR
- pitching **5.00 RA/G, 4.69 ERA, 1.377 WHIP**

Recent record snapshots:
- Yankees L5: **4-1**, but small-sample win-rate SE ~**18 percentage points**.
- Twins L5: **2-3**, SE ~**22 percentage points**.
- Yankees L10: 7-3; SE ~14.5 pp.
- Twins L10: 4-6; SE ~15.5 pp.

These form rates are descriptive only and too noisy to carry independent signed coefficients.

Longer current preview:
- Yankees L20: **12-8**
- Twins L20: **7-13**
- Yankees L30: **19-11**
- Twins L30: **12-18**

L15 snapshots were stale/inconsistent across sources and are marked partial rather than invented.

#### Season series / H2H

July:
- Yankees 5-2 Twins
- Twins 11-4 Yankees
- Twins 6-1 Yankees

Minnesota leads the season series 2-1, but current starters and lineups differ materially. H2H is descriptive only and receives no independent coefficient.

#### Bullpen availability

**Yankees**
Sep 13 2-0 Mets:
- Schlittler 6 IP
- Brent Headrick 1 IP
- Paul Blackburn 1 IP
- David Bednar 1 IP
Bednar also handled 1.2 innings on Sep 11. The leverage group is still usable, but recent workload adds availability width.

**Twins**
Sep 13 9-2 loss:
- Joe Ryan 4 IP
- Adams, Taylor Rogers and Nance covered the remaining five innings.
Recent games also required meaningful relief work, though not every high-leverage arm was used each day.

Minnesota's season staff is much weaker overall, but workload is treated as availability, never as an automatic performance downgrade.

#### Weather / termination branch

Exact Target Field weather near 18:30 CDT:
- about **14°C / 57°F**
- cloudy
- rain/thunderstorm risk rising sharply
- precipitation: ~54% at 19:00; ~83% at 20:00-22:00
- breezy conditions possible

No verified official delay/postponement existed before the forecast freeze.

No automatic total sign is assigned:
1. delayed start but normal starters → centre little changed;
2. long delay or midgame interruption → starters shortened, bullpen exposure and upper tail increase;
3. played-through cool/wet conditions could suppress contact depending wind direction;
4. operator weather/action terms are unknown.

Exact controlling wind direction was not verified, so weather is primarily **width**, not signed lean.

#### Joint run arithmetic

**Yankees**
- own scoring: **4.54 R/G**
- Twins run prevention: **5.00 RA/G**
- midpoint: `(4.54 + 5.00)/2 = 4.77`
- Kremer 5.65 ERA / 5.13 FIP / HR-prone contact branch: **+0.35**
- Chisholm/Grisham/Stanton absences + Judge return uncertainty: **−0.25**
- Twins recent bullpen exposure: **+0.10**
- working Yankees centre ≈ **4.97 ≈ 5.0**

**Twins**
- own scoring: **4.58 R/G**
- Yankees run prevention: **3.73 RA/G**
- midpoint: `(4.58 + 3.73)/2 = 4.16`
- Warren recent positive regime, shrunk by 4.48 xERA / 4.16 FIP: **−0.15**
- Buxton out + Lewis shoulder uncertainty / younger lineup: **−0.35**
- Yankees recent leverage workload: **+0.05**
- working Twins centre ≈ **3.71 ≈ 3.7**

**Total centre:** ~**8.7**  
**Margin centre:** Yankees ~**+1.3**  
**Total width:** ~**4.2**  
**Margin width:** ~**4.0**

Normalized total edge:
`|8.7 - 8.0| / 4.2 ≈ 0.17` toward Over — modest, not large.

#### Run-line families

| Final state | Probability |
|---|---:|
| Yankees by 4+ | **24%** |
| Yankees by 2-3 | **28%** |
| Yankees by exactly 1 | **13%** |
| Twins win | **35%** |

Derived:
- Yankees winner = **65%**
- Twins winner = **35%**
- **Yankees -1.5 = 52%**
- **Twins +1.5 = 48%**

Minnesota's home-last-bat slightly protects its comeback/cushion branch relative to a neutral batting-exposure model.

#### Total families / push handling at 8.0

| Total runs | Probability |
|---|---:|
| 0-6 | **23%** |
| exactly 7 | **15%** |
| **exactly 8** | **12%** |
| 9-10 | **25%** |
| 11+ | **25%** |

Derived:
- **Over 8.0 = 50% win / 12% push / 38% loss**
- **Under 8.0 = 38% win / 12% push / 50% loss**

The meaningful eight-run push mass is why the two rows are not written as 50%/50% complementary win probabilities.

#### Component budget at 8.0

| Twins runs | Yankees needed for 9+ |
|---|---:|
| 2 | 7 |
| 3 | 6 |
| 4 | 5 |
| 5 | 4 |

Central 5-3 lands **exactly 8 and pushes** both total directions.

#### Mandatory baseball branches

- **Warren strong-current branch:** 5.5-6+ effective innings; Minnesota held to 2-3 → Yankees separation, Under/push.
- **Warren regression/contact branch:** 4.48 xERA / hard-contact risk reappears → Twins score 4-5, helping +1.5 and Over.
- **Kremer HR/early-hook branch:** Yankees power exploits his season HR/FIP profile → Yankees -1.5 and Over become positively linked.
- **Kremer splitter-improvement branch:** post-trade pitch-mix adjustment works → Yankees held to 3-4; helps Twins +1.5 and Under.
- **Twins lineup-deficit branch:** Buxton absent and Lewis unavailable/limited → Minnesota lower tail.
- **Yankees bullpen workload branch:** recent Headrick/Blackburn/Bednar usage limits some ideal leverage sequencing.
- **Weather-interruption branch:** starter length shortened; bullpen and inherited-run upper tail expands.
- **Cool/wet suppression branch:** if played through and wind suppresses contact, Under improves; wind direction not verified enough for signed central adjustment.
- **Home ninth:** Minnesota retains full bottom-nine comeback exposure when trailing.
- **Extras:** automatic runner creates materially higher scoring rate and hurts the Under.

#### Representative outcomes

**Central:** Yankees 5-3 Twins
- Yankees -1.5: WIN
- Twins +1.5: LOSS
- Over 8.0: PUSH
- Under 8.0: PUSH
- Winner Yankees: WIN

**Rank-1/Rank-2 compatible:** Yankees 6-3 Twins
- Yankees -1.5: WIN
- Over 8.0: WIN

#### Complement / kill paths

| Selection | Win | Push | Loss | Main failure paths |
|---|---:|---:|---:|---|
| Yankees -1.5 | 52% | — | 48% | Kremer splitter regime works; Judge/lineup deficit; Warren/Twins offense creates close game; weather suppresses NYY HR; one-run Yankees win |
| Over 8.0 | 50% | 12% | 38% | both starters reach central/good length; weather suppresses contact; Minnesota lineup deficit; high-leverage relief succeeds |
| Twins +1.5 | 48% | — | 52% | Kremer HR/early hook; Minnesota bullpen transition; Buxton/Lewis deficit; Yankees multi-run separation |
| Under 8.0 | 38% | 12% | 50% | Kremer/Warren hook; HR cluster; bullpen workload; delay/interruption; extra innings |

#### Top-two joint

`P(Yankees -1.5 ∧ Over 8.0 win) ≈ 31%`.

Coupling: **moderately positive** because Yankees separation often occurs through Kremer's HR/early-hook upper tail. It is not deterministic: 5-1 can win -1.5 while staying Under, and 6-4 wins both.

#### Completeness

| Requirement | State |
|---|---|
| MLB identity / venue / scheduled innings / home-last-bat | PASS |
| Current method read fresh | PASS |
| Official starter identity | PASS |
| Secondary starter discrepancy resolved | PASS — MLB official Kremer controls |
| Current starter regimes | PASS |
| Posted batting orders / catcher | **PARTIAL / final official order not recovered** |
| Material injuries / deficits | PASS WITH LEWIS STATUS UNCERTAINTY |
| Bullpen workload / score-state chain | PASS WITH LIMITATION |
| L5/L10/L20/L30 trend | PASS; L15 PARTIAL |
| H2H continuity | PASS / no independent coefficient |
| Weather / termination branch | PASS |
| Exact wind direction | PARTIAL / no signed coefficient |
| Joint run arithmetic | PASS |
| Run-line family decomposition | PASS |
| Integer total push mass | PASS |
| Component budget | PASS |
| Small-sample SE | PASS |
| Complement kill paths | PASS |
| Top-two joint | PASS |
| Final pregame freeze | PASS at 18:34:41 CDT |
| Settlement source | MLB official final/gamebook |

#### Source register

- Google Drive `METHOD.md` / current 2026-09-12 corrections.
- Google Drive `RULES_BASEBALL.md`.
- MLB official Sep 14 starting-lineups/probable-pitcher page.
- Baseball-Reference Warren 2026 line / current matchup preview.
- Baseball Savant Warren current metrics.
- Dean Kremer current game log / Savant / FIP cross-check.
- Current post-trade Kremer pitch-mix reporting.
- Baseball-Reference Yankees/Twins batting and pitching tables.
- MLB Yankees transactions/injury pages.
- MLB Twins transactions.
- MLB official Royce Lewis shoulder update.
- Reuters Sep 13 Yankees and Twins recaps for bullpen workload.
- Structured Target Field weather.

Public URLs:
- https://www.mlb.com/starting-lineups/2026-09-14
- https://www.mlb.com/probable-pitchers/2026-09-14
- https://www.baseball-reference.com/players/w/warrewi02.shtml
- https://baseballsavant.mlb.com/
- https://www.baseball-reference.com/previews/2026/MIN202609140.shtml
- https://www.mlb.com/yankees/roster/transactions
- https://www.mlb.com/yankees/news/yankees-injuries-and-roster-moves
- https://www.mlb.com/twins/roster/transactions

### P-422 — Denver Broncos @ Kansas City Chiefs — NFL Regular Season Week 1 — PRE-SNAP / UNSETTLED

- **Scheduled kickoff:** 2026-09-14 19:15 CDT / 2026-09-15 10:15 AEST.
- **Forecast freeze:** **2026-09-14 19:15:32 CDT / 2026-09-15 10:15:32 AEST**.
- **State at freeze:** structured NFL state showed **Q1 15:00, 0-0, no play recorded**. No post-snap information used.
- **Venue:** Arrowhead Stadium, Kansas City.
- **Method:** MDS-2026.09.06-v4.0 / SFA-AMERICAN-FOOTBALL / `SPORTS_ONLY / MARKET_BLIND`.
- **Evidence density:** SPARSE.
- **Performance status:** LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.
- **Settlement:** PENDING; no retrospective performed.
- **Operator endpoint:** `UNKNOWN_DEFINITION`; working full-game endpoint includes OT.

| Rank | Selection | `UNVALIDATED_SUBJECTIVE` p | Evidence |
|---|---|---:|---|
| 1 | **Denver Broncos +2.5** | **56%** | MEDIUM-LOW |
| 2 | **Under 42.5** | **53%** | LOW-MEDIUM |
| 3 | **Over 42.5** | **47%** | LOW-MEDIUM |
| 4 | **Kansas City Chiefs -2.5** | **44%** | MEDIUM-LOW |

**Potential winner:** Kansas City **54%**, Denver **46%**.  
**Representative score:** Kansas City **21-20** Denver.  
**Continuous centre:** KC ~21.4, DEN ~20.4, total ~41.8, KC margin ~+1.0.

#### Quarterback / unit regime
- KC: Patrick Mahomes returns from Dec-2025 left ACL surgery. He was cleared for full camp work and was a full Week 1 participant. QB2 Justin Fields. Eric Bieniemy returns as OC. Skill core: Kenneth Walker III, Rashee Rice, Xavier Worthy, Travis Kelce. **LT Josh Simmons OUT**; rookie Kahlil Benson expected at LT.
- DEN: Bo Nix returns 240 days after the ankle injury that ended his 2025 postseason. QB2 Jarrett Stidham. Davis Webb is a first-time NFL play-caller but has worked with Nix for three years. Skill core: Jaylen Waddle, Courtland Sutton, Marvin Mims, Evan Engram, J.K. Dobbins/RJ Harvey. Starting OL intact.

#### Final availability
- KC official designations: **Josh Simmons OUT, Chamarri Conner OUT**. Chris Jones has no game designation and is active; Mahomes/Rice/Worthy/Trey Smith were full participants; L'Jarius Sneed had no final designation. Gameday cross-check also listed Diego Pounds, Bryson Eason, Jared Wiley and Jack Pyburn inactive.
- DEN: official final report had **no injury designations**; Mims full. Official inactives were Sam Ehlinger, Tyler Badie, Kage Casey, Dallen Bentley, Jordan Jackson and Tyler Onyedim. **Jonathon Cooper** is unavailable on the Commissioner's Exempt List.

#### 2025 baselines
- KC: 6-11, 21.3 PF/G, 19.3 PA/G, **2.16 offensive PPD**, **1.90 opponent PPD**.
- DEN: 14-3 regular season, 23.6 PF/G, 18.3 PA/G, **2.05 offensive PPD**, **1.64 opponent PPD**.
- One-score outcomes are shrunk: KC's 1-9 one-score record and Denver's strong close-game record are outcomes, not standalone abilities.

#### Trend disclosure
- KC L5 **0-5**, L10 **2-8**, L15 regular-season **6-9**, L20 unavailable. L5 was heavily contaminated by Mahomes' injury/absence, so no direct coefficient.
- DEN L5 competitive **3-2**, L10 **8-2**, L15 competitive ~**13-2**, L20 unavailable (19 total 2025 competitive games). Descriptive only.
- 2025 H2H: DEN 22-19 KC with Mahomes active; DEN 20-13 KC with Mahomes absent. Current roster changes prevent an independent H2H coefficient.

#### Joint drive arithmetic
Expected meaningful drives: ~10.5-10.8 each.

**KC:** midpoint of 2.16 offensive PPD and Denver's 1.64 allowed = **1.90 PPD**. Mahomes/Walker/Rice/Worthy/Kelce/Bieniemy raise ceiling; ACL return and Simmons absence reduce/provide width; Cooper absence offsets some pressure. Working ~**1.98 PPD x 10.8 = 21.4**.

**DEN:** midpoint of 2.05 offensive PPD and KC's 1.90 allowed = **1.98 PPD**. Waddle/intact OL/Nix-Webb continuity help; Nix first regular game back and Webb first play-calling game widen; Chris Jones active suppresses; KC secondary turnover and Conner absence restore upside. Working ~**1.94 PPD x 10.5 = 20.4**.

- Margin width ~10.5; total width ~13.
- Spread normalised edge: `|1.0 - 2.5| / 10.5 ≈ 0.14` toward DEN +2.5.
- Total normalised edge: `|41.8 - 42.5| / 13 ≈ 0.05` toward Under.

#### Margin families
| State | Probability |
|---|---:|
| KC by 14+ | 10% |
| KC by 7-13 | 14% |
| KC by 3-6 | 20% |
| KC by 1-2 | 10% |
| Denver win | 46% |

Derived: KC winner 54%, DEN winner 46%, KC -2.5 44%, DEN +2.5 56%.

#### Total families
| Total | Probability |
|---|---:|
| 0-34 | 21% |
| 35-42 | 32% |
| 43-49 | 26% |
| 50+ | 21% |

Derived: Under 42.5 53%, Over 42.5 47%.

#### Component budget at 42.5
- DEN 17 -> KC needs 26 for 43+.
- DEN 20 -> KC needs 23.
- DEN 24 -> KC needs 19.
- KC 17 -> DEN needs 26.
- KC 21 -> DEN needs 22.
- KC 24 -> DEN needs 19.

#### Mandatory branches
- Central 21-20 KC.
- Mahomes mobility/Walker upside: KC 27-20/28-21 -> Chiefs -2.5 + Over.
- KC protection failure at rookie LT: DEN cover/win, often Under.
- Nix/Webb/Waddle upside vs reshaped KC secondary: DEN 24-21/27-23 -> DEN +2.5, often Over.
- Denver offensive suppression by Chris Jones/front -> Chiefs cover + Under.
- Cooper absence weakens Denver edge pressure -> KC separation branch.
- Non-offensive/short-field score -> raises Over and margin tails.
- Leader clock drain vs trailing garbage-time scoring preserved.
- OT explicit small tail.

#### Weather
Arrowhead near kickoff: ~32°C, clear/hot, increasingly windy in the daily forecast, no precipitation concern. Exact field-level wind direction/speed was not frozen from a controlling source, so heat/wind are **width**, not a signed total coefficient.

#### Kill paths
| Selection | Win p | Loss p | Main failures |
|---|---:|---:|---|
| Broncos +2.5 | 56% | 44% | Mahomes fully mobile; Walker protects LT; Cooper absence decisive; Nix/Webb mistakes |
| Under 42.5 | 53% | 47% | Waddle/Worthy explosives; short fields; hot-weather fatigue; OT |
| Over 42.5 | 47% | 53% | both strong defenses carry; Simmons absence; cautious QB returns; clock drain |
| Chiefs -2.5 | 44% | 56% | Denver OL/defense keeps it one-score; Waddle; KC secondary turnover; 1-2 point KC win |

**Top-two joint:** `P(Broncos +2.5 ∧ Under 42.5) ≈ 32%`, mildly positive/state-dependent.

#### Completeness
- Identity/venue/rules/QBs/backup branches: PASS.
- Final Denver inactives: PASS.
- Chiefs injury designations: PASS; full inactive list corroborated secondarily.
- OL/skill/front/coverage exposure: PASS.
- L5/L10/L15/L20: PASS with L20 unavailable.
- H2H continuity: PASS.
- Drive arithmetic/margin families/total budget/kill paths/top-two joint: PASS.
- Weather: PASS; exact wind direction PARTIAL.
- Final freeze: PASS, pre-snap at 19:15:32 CDT.
- Settlement source: NFL official final/gamebook.

#### Source register
- Google Drive `METHOD.md`, `CONTROLS.md`, `RULES_AMERICAN_FOOTBALL.md`.
- NFL official Week 1 injury report and Broncos-Chiefs game centre.
- Chiefs official injury report, preview, depth chart, roster and Mahomes rehab/camp updates.
- Broncos official injury report, inactives, depth chart, Nix return and 2026 coaching staff.
- Pro-Football-Reference 2025 Chiefs/Broncos drive tables.
- NFL 2025 schedules / prior matchup.
- Structured Arrowhead weather.

Public URLs include:
- https://www.nfl.com/news/nfl-week-1-injury-report-2026-season
- https://www.nfl.com/games/broncos-at-chiefs-2026-reg-1
- https://www.chiefs.com/news/week-1-injury-report-broncos-vs-chiefs-2026
- https://www.chiefs.com/news/five-things-to-watch-on-monday-broncos-vs-chiefs
- https://www.chiefs.com/team/depth-chart
- https://www.denverbroncos.com/news/broncos-announce-inactives-for-week-1-game-vs-chiefs
- https://www.denverbroncos.com/team/depth-chart/
- https://www.pro-football-reference.com/teams/kan/2025.htm
- https://www.pro-football-reference.com/teams/den/2025.htm

### P-423 — San Diego Padres @ Colorado Rockies — MLB — PRE-GAME / UNSETTLED

- **Scheduled first pitch:** 2026-09-14 18:40 MDT / 20:40 EDT / 2026-09-15 10:40 AEST.
- **Forecast freeze:** **2026-09-14 18:22:53 MDT / 2026-09-15 10:22:53 AEST**, before scheduled first pitch.
- **Venue:** Coors Field, Denver.
- **Competition:** MLB regular season.
- **Working ID:** P-423.
- **Method:** MDS-2026.09.06-v4.0; SFA-BASEBALL; `SPORTS_ONLY / MARKET_BLIND`.
- **Performance status:** LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.
- **Settlement:** PENDING. No retrospective performed.
- **Operator listed-pitcher/action/weather terms:** `UNKNOWN_DEFINITION`.

#### Issued ranking

| Rank | Selection | Exact settlement probability | Evidence |
|---|---|---:|---|
| 1 | **San Diego Padres -1.5** | **54% win / 46% loss** | MEDIUM-LOW |
| 2 | **Over 11.0 total runs** | **48% win / 10% push / 42% loss** | LOW-MEDIUM |
| 3 | **Colorado Rockies +1.5** | **46% win / 54% loss** | MEDIUM-LOW |
| 4 | **Under 11.0 total runs** | **42% win / 10% push / 48% loss** | LOW-MEDIUM |

**Potential winner:** **San Diego Padres 66%**, Colorado 34%.  
**Representative central score:** Padres **6-5** Rockies (11 total = push).  
**Top-two compatible score:** Padres **7-5** Rockies.  
**Working continuous centre:** Padres ~**6.2**, Colorado ~**5.0** → total ~**11.2**, Padres margin ~**+1.2**.

Only Padres -1.5 and Over 11.0 are preferred directions.

#### Starter identity

MLB's live Sep 14 scoreboard lists:
- **SD: Casey Mize, RHP — 5-9, 3.70 ERA**
- **COL: Tomoyuki Sugano, RHP — 12-9, 5.30 ERA**

Earlier official probable-pitcher pages still showed San Diego TBD, but the live MLB scoreboard and same-day team coverage both identify Mize. `BB-P1 = PASS` at final refresh.

#### Casey Mize current regime

Season: **5-9, 3.70 ERA**.
Padres tenure: **1-3, 6.34 ERA across 32.2 IP** entering tonight.

Recent starts:
- Sep 8 vs WSH: **5.2 IP, 4 H, 3 ER, 1 BB, 7 K**
- Sep 2 at CIN: **4.0 IP, 5 H, 4 ER, 1 BB, 4 K**
- Aug 28 at TB: **5.0 IP, 6 H, 2 ER / 7 R**
- Aug 22 vs MIN: **2.2 IP, 4 ER, 3 HR**
- Aug 16 at CLE: **6.0 IP, 0 ER**

Mize was traded from Detroit Aug 3 and has had an unstable post-trade run. The season 3.70 is retained as a talent prior, but the Padres-specific 6.34 and short/volatile recent outings are carried as a wide current-regime branch. Central exposure ~**5.0-5.5 IP**.

#### Tomoyuki Sugano current regime

Season:
- **12-9, 5.30 ERA**
- 137.2 IP
- 84 K
- 1.34 WHIP

Recent:
- Sep 9 at NYY: **6 IP, 5 ER, 2 HR**
- Sep 2 vs BAL: **6 IP, 3 ER**
- Aug 28 at ATL: **4 IP, 6 ER**
- Aug 23 vs CLE: **3 IP, 5 ER**
- Aug 17 vs LAD: **5 IP, 6 ER / 7 R**

Last five: **24 IP, 25 ER** (~9.38 ERA). Broader last-seven reporting: **1-5, 7.71 ERA**.
Savant splits also show heavy damage against both left and right hitters. Sugano's season line is retained, but current contact/HR and shortened-outing risk substantially raise San Diego's upper tail.

#### Batting-order gate

Colorado's current pregame lineup was corroborated:
1. Jake McCarthy LF
2. Connor Norby 2B
3. Hunter Goodman C
4. TJ Rumfield 1B
5. Cole Carrigg CF
6. Kyle Karros 3B
7. Mickey Moniak RF
8. Adael Amador DH
9. Ezequiel Tovar SS

A fully field-owner-confirmed San Diego batting order was not recovered before freeze. Current projected/current core is Fernando Tatis Jr., Jackson Merrill, Manny Machado, Ty France, Xander Bogaerts and the regular Padres support group.

`BB-P2 = PARTIAL`, so no player prop is issued and side/total confidence is capped.

#### Injuries / roster

**San Diego**
- Ty France reinstated from paternity list Sep 14; season line around .294 with 20 HR.
- Jason Adam 60-day IL, shoulder.
- Jeremiah Estrada IL, shoulder impingement.
- Ramón Laureano 60-day IL, hip surgery.
- Gavin Sheets IL, left-foot sprain.
- Miguel Andujar rehabbing right-wrist fracture.
- Luis Rengifo out for season, torn ACL/MCL.
- Joe Musgrove, Yu Darvish, Lucas Giolito and Bryan Hoeing remain unavailable.

**Colorado**
- Willi Castro IL with heel/knee issues.
- Kyle Freeland nearing return but not tonight's starter.
- Jose Quintana remains on rehab path.
- Kris Bryant long-term unavailable.
- Kyle Karros recently activated and is in current order.

#### Team environment

Through Sep 13/14:
- Padres: **81-68**, ~**639 RS / 617 RA** → **4.29 R/G, 4.14 RA/G**.
- Rockies: **55-94**, **696 RS / 865 RA** → **4.67 R/G, 5.81 RA/G**.
- Coors Field multi-year park factor: approximately **114 batting / 117 pitching-side**, one-year roughly **112 / 114**.

Recent:
- Padres: **8-2 last 10**, **12-8 last 20**, **19-11 last 30**, current **W7**.
- Rockies: roughly **2-8 to 3-7 last 10 depending snapshot cutoff**, **5-15 last 20**, **5-20 last 25**, current **L7**.
Small-sample W/L form is descriptive only, not an independent coefficient.

Season series before tonight:
- San Diego leads **8-1**.
- Prior Coors games include 1-0 SD, 8-3 COL, 10-8 SD.
H2H is descriptive; only current roster/starter/bullpen mechanisms transfer.

#### Bullpen availability

**Padres**
Sunday's 6-4 win:
- Nick Pivetta 4 IP
- Kyle Hart 1 IP
- David Morgan 0.2
- Wandy Peralta 1.1
- Randy Vásquez 1
- Yuki Matsui 1
Team reporting said key leverage arms Mason Miller, Adrian Morejón and Bradgley Rodriguez had already carried heavy workloads, forcing less-used relievers Sunday. The bullpen is talented but not fully fresh.

**Rockies**
Sunday starter Gabriel Hughes lasted only **2 innings**, forcing **7 bullpen innings**.
Saturday's 11-7 loss included a seven-run eighth against Jaden Hill and Jordan Romano.
That back-to-back workload raises the probability Colorado reaches secondary middle/low-leverage arms if Sugano exits around 4-5 innings.

Workload changes availability/role only, not arm quality.

#### Coors weather / environment

Exact structured query near 18:21 MDT:
- ~**28°C / 82°F**
- mostly cloudy
- thunderstorms possible around 19:00-20:00
- temperatures ~29°C at 19:00, ~27°C at 20:00
- high-altitude Coors environment already explicit in park factor

No official delay/postponement was verified before freeze.

Weather is not automatically Over:
- warm air/altitude support carry;
- thunderstorm delay can shorten starters and increase relief exposure;
- wet/cool post-storm conditions can counter that;
- exact controlling wind direction/speed was not recovered.

Weather therefore widens the upper tail and termination branch but receives only a modest signed positive run adjustment.

#### Joint run arithmetic

**San Diego**
- own scoring: **4.29 R/G**
- Colorado run prevention: **5.81 RA/G**
- midpoint = `(4.29 + 5.81)/2 = 5.05`
- Coors home environment relative to San Diego's mixed-season venues: **+0.45**
- Sugano current 7.71 last-seven / 9.38 last-five ER-rate branch: **+0.55**
- Padres recent leverage/bullpen state does not affect their batting; current lineup injuries/partial order: **−0.10**
- Colorado bullpen fatigue/secondary-arm probability: **+0.25**
- working Padres centre ≈ **6.2**

**Colorado**
- own scoring: **4.67 R/G**
- San Diego run prevention: **4.14 RA/G**
- midpoint = `(4.67 + 4.14)/2 = 4.41`
- Coors specific environment: **+0.45**
- Mize Padres-tenure volatility / ~5 inning exposure: **+0.30**
- Colorado lineup losses + San Diego bullpen quality: **−0.20**
- Padres leverage workload/short-Mize transition: **+0.05**
- working Rockies centre ≈ **5.0**

**Total centre:** ~**11.2**.  
**Margin centre:** Padres ~**+1.2**.  
**Total width:** ~**5.0 runs**.  
**Margin width:** ~**4.4 runs**.

Normalized total edge:
`|11.2 - 11.0| / 5.0 ≈ 0.04` → extremely small. The Over ranks above Under because its cluster/relief/weather upper-tail mass is larger, not because the centre is far above the line.

#### Run-line families

| Final state | Probability |
|---|---:|
| Padres by 4+ | **27%** |
| Padres by 2-3 | **27%** |
| Padres by exactly 1 | **12%** |
| Rockies win | **34%** |

Derived:
- Padres winner **66%**
- Rockies winner **34%**
- **Padres -1.5 = 54%**
- **Rockies +1.5 = 46%**

#### Total families / push at 11.0

| Total runs | Probability |
|---|---:|
| 0-8 | **23%** |
| 9-10 | **19%** |
| **exactly 11** | **10%** |
| 12-13 | **23%** |
| 14+ | **25%** |

Derived:
- **Over 11.0 = 48% win / 10% push / 42% loss**
- **Under 11.0 = 42% win / 10% push / 48% loss**

#### Component budget at 11.0

For 12+:
- Rockies 3 → Padres need 9
- Rockies 4 → Padres need 8
- Rockies 5 → Padres need 7
- Rockies 6 → Padres need 6

Central **Padres 6-5** lands exactly 11 and pushes both total directions.

#### Mandatory branches

- **Central:** SD 6-5 COL → Padres -1.5 loses, total pushes.
- **Sugano current-contact branch:** SD scores 7-9; supports Padres -1.5 + Over.
- **Sugano rebound/April-H2H branch:** he suppresses San Diego for 5-6 IP; Rockies +1.5 and Under improve. Prior April success is context only.
- **Mize good branch:** his Sep 8 form transfers and Rockies stay 3-4 runs → Padres separation, possibly Under/push.
- **Mize post-trade volatility branch:** 4-5 inning exit plus Coors contact cluster → Rockies +1.5/win and Over.
- **Bullpen-fatigue branch:** Colorado's 7 bullpen innings Sunday + Saturday collapse creates Padres late separation.
- **Padres leverage-fatigue branch:** Miller/Morejón/Rodriguez workload and Sunday relief usage create Rockies late-run comeback.
- **Weather interruption branch:** delay/shortened starter prep increases bullpen exposure and upper-tail variance.
- **Home ninth:** Colorado retains bottom-nine comeback/scoring exposure when trailing, supporting Rockies +1.5 and Over.
- **Extras:** automatic runner materially increases high-total and margin-flip tails.

#### Representative outcomes

**Central:** Padres 6-5 Rockies
- Padres -1.5: LOSS
- Rockies +1.5: WIN
- O11: PUSH
- U11: PUSH
- Padres winner: WIN

**Rank-1/Rank-2 compatible:** Padres 7-5 Rockies
- Padres -1.5: WIN
- O11: WIN

#### Kill paths

| Selection | Win | Push | Loss | Main failure paths |
|---|---:|---:|---:|---|
| Padres -1.5 | 54% | — | 46% | Mize struggles; Colorado home-last-bat rally; Sugano rebound; Padres leverage fatigue |
| Over 11.0 | 48% | 10% | 42% | Sugano rebound; Mize 5-6 efficient innings; storm suppresses/interrupts without relief chaos; high-leverage relief succeeds |
| Rockies +1.5 | 46% | — | 54% | Sugano current form persists; Colorado bullpen forced deep; Padres top order creates HR/extra-base cluster |
| Under 11.0 | 42% | 10% | 48% | Coors cluster; either starter early hook; fatigued relief; delay transition; extras |

#### Top-two joint

`P(Padres -1.5 ∧ Over 11.0 win) ≈ 34%`.

Coupling: **moderately positive** because Sugano/Colorado-bullpen failure drives both San Diego separation and high totals. It is not deterministic: 7-3 wins the run line but stays Under 11, while 7-6 wins Over but loses Padres -1.5.

#### Completeness

| Requirement | State |
|---|---|
| MLB identity / venue / scheduled innings / home-last-bat | PASS |
| Current Drive baseball method | PASS |
| Starter identity | PASS at live MLB scoreboard |
| Starter current regimes / hook | PASS |
| Current Rockies order / catcher | PASS |
| Current Padres field-owner order | **PARTIAL / not recovered** |
| Injuries / roster | PASS |
| Bullpen workload | PASS |
| L5/L10/L20/L30 / trend | PASS with L15 not separately recovered |
| H2H continuity | PASS / no independent coefficient |
| Coors park factor | PASS |
| Venue weather / termination branch | PASS |
| Exact wind | PARTIAL |
| Joint run arithmetic | PASS |
| Run-line decomposition | PASS |
| Integer push mass at 11 | PASS |
| Component budget | PASS |
| Kill paths / top-two joint | PASS |
| Final pregame freeze | PASS at 18:22:53 MDT |
| Settlement source | MLB official final/gamebook |

#### Source register

Primary/current:
- Google Drive `METHOD.md` and `RULES_BASEBALL.md`.
- MLB Sep 14 scoreboard / starting-lineup page for event and starter identity.
- MLB Padres/Rockies injury and transaction pages.
- Baseball Savant Casey Mize and Tomoyuki Sugano pages.
- Baseball-Reference current Padres/Rockies team pages and matchup preview.
- Reuters Sep 13 Padres and Rockies game recaps.
- Same-day Rockies/Padres team-focused game previews.
- Structured Coors Field weather.

Public URLs:
- https://www.mlb.com/scores/2026-09-14
- https://www.mlb.com/starting-lineups/2026-09-14
- https://www.mlb.com/padres/roster/probable-pitchers
- https://www.mlb.com/rockies/roster/probable-pitchers
- https://www.mlb.com/padres/news/padres-injuries-and-roster-moves
- https://www.mlb.com/rockies/news/rockies-injuries-and-roster-moves
- https://baseballsavant.mlb.com/savant-player/casey-mize-663554?season=2026
- https://baseballsavant.mlb.com/savant-player/tomoyuki-sugano-608372
- https://www.baseball-reference.com/previews/2026/COL202609140.shtml
- https://www.baseball-reference.com/teams/SDP/2026-roster.shtml
- https://www.baseball-reference.com/teams/COL/2026-roster.shtml

When a new event is forecast, it is inserted here first and remains here while:
- not started;
- live;
- awaiting an official final;
- awaiting a required field-owning settlement record; or
- otherwise incomplete under the governing settlement standard.

Only after settlement is complete should the event be moved from this section into its ID-ordered position in the settled body.

## INHERITED DRIVE FOLLOW-UP QUEUE — REFERENCE ONLY

These are **not** new P-407+ forecasts and must not be duplicated as new prediction rows. They are carried here only so unresolved Drive work remains visible while the new mini-log operates.

### Primary result / derivative follow-ups

| Handle | Parent | Remaining item | Drive disposition |
|---|---|---|---|
| `TMP-OPEN-20260911-03` | `P-364` potential winner | England to win the 3rd Test | Live at last Drive retrieval; settle only on official result |
| `TMP-OPEN-20260911-01` | `P-368-C02` | Over 7.5 total corners | Provisional research win; field-owner independence unresolved |
| `TMP-OPEN-20260911-02` | `P-369-C01` | Under 10.5 total corners | Provisional research loss; field-owner independence unresolved |
| `TMP-OPEN-20260909-01` | `P-341-C03` | Over 7.5 total corners | Unsettleable to frozen standard at last re-probe |
| `TMP-OPEN-20260909-02` | `P-342-C03` | Over 8.5 total corners | Provisional research win |
| `TMP-OPEN-20260909-03` | `P-126` | Corners + event identity | Identity/state conflict unresolved |
| `TMP-OPEN-20260909-04` | `P-148-C02` | Toluca team corners | Provisional loss |
| `TMP-OPEN-20260909-05` | `P-149-C02` | Ventura team corners | Provisional win |
| `TMP-OPEN-20260909-06` | `P-176-C05` | Amiens/Versailles U10.5 corners | Provisional win |
| `TMP-OPEN-20260909-07` | `P-178-C05` | Cannes/Le Puy U10.5 corners | Provisional loss |
| `TMP-OPEN-20260909-08` | `P-179-C05` | Thionville/Paris 13 U10.5 corners | Provisional win |
| `TMP-OPEN-20260909-09` | `P-233` | Beijing/Lanzhou O8.5 corners | Provisional win |
| `TMP-OPEN-20260909-10` | `P-234-C03` | Dalian/Shenhua O8.5 corners | Provisional win; disrupted match |
| `TMP-OPEN-20260909-11` | `P-235` | Shandong/Shanghai Port O8.5 corners | Provisional win |

### Historical documentary-audit follow-ups

| Handle | Parent | Requirement |
|---|---|---|
| `TMP-AUDIT-20260912-01` | `P-250-C05` | Recover missing later field-owner/provider corner settlement |
| `TMP-AUDIT-20260912-02` | `P-251-C05` | Recover missing later field-owner/provider corner settlement |
| `TMP-AUDIT-20260912-03` | `P-255-C05` | Recover missing later field-owner/provider corner settlement |
| `TMP-AUDIT-20260912-04` | `P-256-C05` | Recover missing later field-owner/provider corner settlement |
| `TMP-AUDIT-20260912-05` | `P-265-C05` | Recover missing later field-owner/provider corner settlement |

## CONTROLLING METHOD SNAPSHOT FOR THIS MINI-LOG

- Primary operational method: **MDS-2026.09.06-v4.0** (`METHOD.md`).
- Current Drive correction: all present combined-log material is **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**.
- Forecast mode: **SPORTS_ONLY / MARKET_BLIND**. Sportsbook odds, implied probability, line movement, consensus, tipsters and bookmaker previews do not drive ranks or probabilities. A supplied operator record may define the exact contract only.
- Every valid ranked row must carry an explicit **`UNVALIDATED_SUBJECTIVE` probability**. Rank is derived from the row probabilities, not assigned independently.
- New forecasts must use the relevant current `RULES_<SPORT>.md`, `CONTROLS.md`, source rules, competition rules and current-surface/weather requirements where applicable.
- A blocking identity/contract/time/participant/environment failure means the actionable card does not issue.
- Required analysis includes L5/L10/L15/L20 + trend test, both sides/H2H where valid, exposure/deficit chain, bench/coaching/rotation, joint event distribution, component/separation budgets, two-way mechanism sign audit, and final volatile refresh.
- Joint-event arithmetic must explicitly carry:
  - outcome-state probability masses (`G-L1`);
  - uncertainty as width unless a directional mechanism exists (`G-L2`);
  - disaggregated evidence where accessible (`G-L7`);
  - normalised edge for totals (`G-L8`);
  - complement / kill-path decomposition (`G-L9`);
  - `P(Rank #1 ∧ Rank #2)` with coupling label (`G-L10`);
  - standard error before using small-sample rates directionally (`G-L11`);
  - the §16.8 card-completeness block.
- Do not hedge by ranking both complementary sides merely to manufacture a hit. Preferred-direction performance is the meaningful object.
- Never rewrite a frozen forecast after the result.
- Every decisive factual claim must record its exact source/record, source role/field owner, access time, and source state where applicable.
- Synthetic, simulated, projected, AI-generated or tipster material is prohibited as a settlement source.

## SOURCE OPERATING RULES

1. Prefer field-owning official event/league/team records for identity, participants, state, final results and contract-relevant statistics.
2. Prefer verified structured/keyless endpoints before narrative pages where available.
3. ESPN site API is an important structured research lane for supported soccer, cricket and baseball competitions, but route coverage must be verified per competition/event.
4. Official event/static reports remain the controlling settlement lane where available.
5. Outdoor-event weather must be venue-coordinate and game-window specific; a generic city forecast is insufficient.
6. Search snippets are discovery aids, not source records. Open the underlying record.
7. Synthetic/simulated prediction content never settles a market.
8. Source access failure is route-specific evidence; do not generalise one failed route into permanent competition non-coverage.
9. No current source in the Drive source register is authorised as `APPROVED FOR FEATURE` for numerical-model training merely because it is useful for research.

## RECENT LEARNINGS CARRIED FORWARD

The September control-execution audit found that merely listing controls without numerically executing them is a major failure mode. For new P-407+ cards, the arithmetic and disclosure controls must actually appear in the card.

Recent cross-sport learnings to preserve:
- Most Rank-#1 failures should be tested against mechanisms already known pre-issue before inventing post-hoc explanations.
- Aggregate statistics should not receive decisive directional weight when an accessible disaggregated record can materially change the interpretation.
- Small normalised-edge main totals should be treated probabilistically as near-coin-flip rather than overstated.
- Phase totals and alternate/far-from-centre lines may be useful research families, but existing observations are guidance/testing evidence, not automatic ranking rules.
- Small-sample rates require sampling-error disclosure before directional use.
- Top-two success is a joint event and its probability must be reported with dependence/coupling made explicit.
- Sport-specific controls and any prospective candidates remain subject to the `L-087` firewall: one cohort can motivate disclosure/testing, not a fitted weight or automatic ordinal rule.

## NEW P-407+ EVENT INDEX

| Working ID | Sport | Competition | Event | State | Rank #1 | Potential winner | Sources recorded | Settlement |
|---|---|---|---|---|---|---|---|---|
| `P-407` | Soccer | Belgium Jupiler Pro League | Club Brugge vs Royal Antwerp FC | PRE-MATCH / PENDING SETTLEMENT | Club O4.5 team corners | Club Brugge | Yes | PENDING |
| `P-408` | Soccer | English Premier League | Coventry City vs Brighton & Hove Albion | PRE-MATCH / PENDING SETTLEMENT | Brighton O3.5 team corners | Brighton | Yes | PENDING |
| `P-409` | Soccer | France Ligue 1 | Lille OSC vs ESTAC Troyes | PRE-MATCH FORECAST / NOW LIVE / PENDING | Lille O0.5 team goals | Lille | Yes | PENDING |
| `P-410` | Soccer | German Bundesliga | RB Leipzig vs Hamburger SV | PRE-MATCH / PENDING SETTLEMENT | Leipzig O0.5 team goals | RB Leipzig | Yes | PENDING |
| `P-411` | Basketball | FIBA Women's Basketball World Cup | Spain (W) vs Germany (W), 3rd Place | PRE-GAME / PENDING SETTLEMENT | Germany +6.5 | Spain | Yes | PENDING |
| `P-412` | American Football | NFL | Atlanta Falcons @ Pittsburgh Steelers | PRE-GAME / PENDING SETTLEMENT | Falcons +6.5 | Pittsburgh Steelers | Yes | PENDING |
| `P-413` | American Football | NFL | Baltimore Ravens @ Indianapolis Colts | PRE-GAME / PENDING SETTLEMENT | Colts +3.0 | Baltimore Ravens | Yes | PENDING |
| `P-414` | American Football | NFL | Buffalo Bills @ Houston Texans | PRE-GAME / PENDING SETTLEMENT | Texans +1.5 | Buffalo Bills | Yes | PENDING |
| `P-415` | Baseball | MLB | LA Angels @ Washington Nationals | NOT ISSUED / INTERRUPTED | — | — | No | CLOSED-NO-FORECAST |
| `P-416` | Baseball | MLB | New York Mets @ New York Yankees | PRE-GAME DELAY / PENDING SETTLEMENT | Under 8.0 | New York Yankees | Yes | PENDING |
| `P-417` | Baseball | NPB Central League | Chunichi Dragons @ Hanshin Tigers | PRE-GAME / PENDING SETTLEMENT | Dragons +1.5 | Hanshin Tigers | Yes | PENDING |
| `P-418` | Soccer | Bhutan Premier League | Drukpa FC vs RTC FC | PRE-MATCH / PENDING SETTLEMENT | Drukpa O0.5 team goals | Drukpa FC | Yes | PENDING |
| `P-419` | Soccer | Sweden Allsvenskan | Djurgården vs GAIS | PRE-MATCH / PENDING SETTLEMENT | Djurgården O0.5 team goals | Djurgården | Yes | PENDING |
| `P-420` | Baseball | MLB | Atlanta Braves @ Chicago Cubs | PRE-GAME / PENDING SETTLEMENT | Braves +1.5 | Chicago Cubs | Yes | PENDING |
| `P-421` | Baseball | MLB | New York Yankees @ Minnesota Twins | PRE-GAME / PENDING SETTLEMENT | Yankees -1.5 | New York Yankees | Yes | PENDING |
| `P-422` | American Football | NFL | Denver Broncos @ Kansas City Chiefs | PRE-SNAP / PENDING SETTLEMENT | Broncos +2.5 | Kansas City Chiefs | Yes | PENDING |
| `P-423` | Baseball | MLB | San Diego Padres @ Colorado Rockies | PRE-GAME / PENDING SETTLEMENT | Padres -1.5 | San Diego Padres | Yes | PENDING |

## SETTLED P-407+ EVENTS

_None yet._

When an event is fully settled, move it here in working-ID order and preserve:
- original issued rows and probabilities unchanged;
- exact result/field-owner settlement evidence;
- WIN / LOSS / PUSH / VOID / CENSORED state per contract;
- why each pick went right or wrong;
- Rank-1 deep retrospective when required;
- what went right and why;
- source-quality review;
- knowability at issue time;
- process grade;
- learning disposition;
- Brier score where eligible under the issued probability state.

## DOCUMENT-DESTINATION NOTES FOR FUTURE LEARNINGS

This mini-log does **not** edit Google Drive. When later reconciled by a repository/write-enabled workflow:

| Finding type | Intended destination |
|---|---|
| Event forecast + final settlement | Current canonical prediction log / status ledger |
| New P-407+ unresolved event | `GAME_LOG_STATUS_CURRENT.md` equivalent pending queue during reconciliation |
| Sport-specific process learning | Relevant `RULES_<SPORT>.md` |
| Cross-sport process correction | `RULES_GENERAL.md` + `LEARNING_REGISTER.md` |
| New prospective hypothesis | `LEARNING_REGISTER.md` as `CANDIDATE` / `TESTING`, not immediate rule weight |
| Source discovery / source re-grade | `SOURCES.md` + `DATA_SOURCE_REGISTER.md` |
| Competition rules change | Relevant sport/league rules document |
| Method-level workflow correction | `METHOD.md` / `CONTROLS.md` only after justified governance review |
| Reconciliation / audit record | Appropriate dated `AUDIT_CHANGELOG_YYYY-MM-DD.md` |
| Raw completed mini-log | archive/mini_logs after canonical reconciliation |

## DRIVE GOVERNING SOURCES CONSULTED AT INITIALISATION

- `METHOD.md` — current operational method and 2026-09-12 controlling correction.
- `CONTROLS.md` — quick-reference hard controls, recent G-L additions, completeness rules and open-queue governance.
- `EXTERNAL_LOGGING_WORKFLOW.md` — pending-at-top running-log workflow, freeze/reconciliation rules and source requirements.
- `GAME_LOG_STATUS_CURRENT.md` — current canonical state, next canonical Drive ID and open/audit queues.
- `SOURCES.md` — source hierarchy, ESPN structured lanes, official-source preference and synthetic-content exclusion.
- `AUDIT_CHANGELOG_2026-09-11.md` — latest detailed control-execution findings and recent cross-sport changes available in the Drive snapshot.

---

**Last issued working event ID:** `P-423`  
**Next working event ID:** `P-424`
