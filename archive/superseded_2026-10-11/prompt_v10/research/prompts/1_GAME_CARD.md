# PROMPT 1 — GAME CARD (one event, appended to the active local mini)

**Run by:** external chat agent · **GitHub:** read only · **Output:** one card appended to the active local mini · **Mode:** `LOCAL_MINI_STAGING` · **Format:** `mini-log-5`

How to use: paste **Part A (common core)**, which now sits at the bottom of [2_START_LOCAL_MINI.md](2_START_LOCAL_MINI.md), and then the **one sport block** from Part B below that matches the event. Fill in the `<…>` fields. The core governs; a sport block adds the sport's research list, the distribution to build, the rules, sources and past-results files to open, and the family checks. Nothing here needs code: calculate by hand from the formulas and tables in the repository and show the working.

---

## PART B — SPORT BLOCKS (paste the one that applies)

Each block lists the files to open (**Open**), the research, the distribution and the family checks. Paths are relative to the repository root.

### B1. BASEBALL

Upcoming game: `<Away @ Home>`, `<League>` · Estimated start: `<date, time, time zone>` (can be delayed)
Supplied contracts (reference only): 1. `<…>` 2. `<…>` 3. `<…>` 4. `<…>`

**Open:** `RULES_BASEBALL.md` (§3 model, §4 controls, §5 live state, §7 research sequence, §8 SFA-BASEBALL, §9 league rules); `PROBABILITY_TOOLKIT.md` §3 and §3.1; `BASE_RATES_REGISTER.md` §3 and §5; `LEAGUE_PROFILES.md` Baseball (MLB, KBO, NPB); `SOURCES.md` §3.1 (and §3.14 to §3.16 for the league's history); archive `Previous Sports Results/Baseball/<MLB|KBO|NPB>/<year>/<year>_games.csv` (`Away Score`, `Home Score`, `Total Runs`, `Extra Innings`, starting pitcher and line-score columns).

**Research:** confirmed starting pitchers (announced or posted lineup), starting lineups and handedness and platoon splits; pitcher form, pitch mix, velocity, workload and pitch counts; K% and BB%; bullpen quality, recent usage and unavailable high-leverage relievers; team offence (opponent-adjusted); park factor; weather and wind; travel and rest; the league's extra-innings and tie rules (RULES_BASEBALL and the official league).

**Expected score (runs):** each team's expected runs over the endpoint, total runs, margin, and the SDs of the total and the margin, from the negative-binomial means. State the innings basis (§3a).

**Distribution:** per-team runs as a negative-binomial (over-dispersed) mixture of the starter segment (expected innings × starter run rate) and the bullpen segment, adjusted for the opposing offence, park and weather, with a shared game-environment factor for covariance (use the league's dispersion phi and environment sigma from LEAGUE_PROFILES). Resolve ties at nine innings with the league's extra-innings rule, or keep a tie outcome where the league allows ties. Account for the home team not batting in the bottom of the ninth when leading.

**Family checks:**
- For any ±1.5 run line, print P(win) + P(lose by exactly 1). Compare with the league's one-run share in LEAGUE_PROFILES (MLB 28.2%, KBO 23.8%, NPB 33.7%). An underdog +1.5 near 0.60 has no edge by construction; four Rank-1 +1.5 rows failed in the 2026-10-09 cohort, and a +1.5 is not Rank 1 below 65% (SELECTION_RULES §4).
- Make the one-run share a function of the expected total: high-run environments widen margins.
- A starter change after research invalidates the card. Write an addendum (A8).

### B2. CRICKET

Upcoming match: `<Team A vs Team B>`, `<competition, format>` · Estimated start: `<…>`
Supplied contracts (reference only): 1. `<…>` 2. `<…>` 3. `<…>` 4. `<…>`

**Open:** `RULES_CRICKET.md` and `LEAGUE_RULES_CRICKET.md` (format, playing conditions, DLS, super over, follow-on); `PROBABILITY_TOOLKIT.md` §1 and §7; `BASE_RATES_REGISTER.md` §6; `SOURCES.md` §3.3; archive `Previous Sports Results/Cricket T20/<competition>/<year>/<year>_games.csv`, `Cricket One-Day Format/...`, `Cricket Tests/...` (match results and innings totals; there is no cricket row in LEAGUE_PROFILES, so build the level from the files).

**Research:** confirmed XI (after the toss, where available); injuries and rested players; batting order, wicketkeeper, bowling attack and expected overs; batting and bowling form (opponent-adjusted), with powerplay, middle and death phases for limited overs; venue, pitch report and boundary dimensions; weather, rain and dew; toss status; batting-first and chasing effects; travel and rest; playing conditions.

**Expected score (runs):** each side's expected innings total (the chasing side capped at the target), the match total if a total is priced, and wickets if a wicket row is priced. Margin is `N/A` (§3a).

**Distribution:** one format-specific model. Limited overs: ball and over resource model with wickets, phase scoring rates and the chase stopping rule (a chase ends when the target is reached). Tests: session and day run and wicket model with draw and weather branches. If the toss is unknown, weight both batting-order branches explicitly. Include a rain, DLS or reduced-overs branch.

**Family checks:**
- Innings or phase totals and the match result come from the same model. The second-innings total is capped near the target (RULES_CRICKET controls CR-P3 and 21).
- Never pair opposite-direction phase and total picks unless the joint win mass is shown (the P-217 lesson).
- State how runs scored before a stoppage settle (runs scored before a stop count).

### B3. BASKETBALL

Upcoming game: `<Home vs Away>`, `<League>` · Estimated start: `<…>`
Supplied contracts (reference only): 1. `<…>` 2. `<…>` 3. `<…>` 4. `<…>`

**Open:** `RULES_BASKETBALL.md`; `PROBABILITY_TOOLKIT.md` §1 (totals §1.2, margins §1.3); `BASE_RATES_REGISTER.md` §3 and §7.1; `LEAGUE_PROFILES.md` Basketball (NBA, WNBA, NBL, EuroLeague, Greek Basket League; do not use the excluded leagues); `SOURCES.md` §3.2; archive `Previous Sports Results/Basketball/<NBA|WNBA|NBL|EuroLeague|...>/<year>/<year>_games.csv` (`Home Score`, `Away Score`, `Total Points`, `Overtime`, quarter or half scores).

**Research:** confirmed starters; injury report, game-time decisions and rested players; expected minutes and rotation; usage changes; offensive and defensive efficiency; pace; shot profile and three-point dependency; rebounding, turnovers and free-throw rate; matchup strengths; opponent-adjusted recent form; home and away splits; rest, back-to-backs and travel; series or playoff situation; league rule changes this season.

**Expected score (points):** each team, total, margin and SDs, from the pace × efficiency means (§3a).

**Distribution:** possessions × points-per-possession. Use team pace and efficiency (opponent-adjusted) to produce a total mean, a margin mean, SDs and their correlation (normal or Student-t). Use the league's own scoring level, margin SD, total SD and correlation from LEAGUE_PROFILES, never NBA defaults for another league. Apply early-season shrinkage toward the prior-season league mean (fewer than about 5 games) and the early-season regime table. Resolve overtime in the full-game distribution (overtime share in LEAGUE_PROFILES).

**Family checks:**
- A totals pick needs the pace × efficiency centre printed. Three Rank-1 totals failed in the 2026-10-09 cohort because centres were typed in or shifted by judgment.
- Name any analyst adjustment as a parameter with its size. If removing it would change the top two, say so.
- The potential winner and every handicap come from the same margin distribution.

### B4. ICE HOCKEY

Upcoming game: `<Away @ Home>`, `<League>` · Estimated start: `<…>`
Supplied contracts (reference only): 1. `<…>` 2. `<…>` 3. `<…>` 4. `<…>`

**Open:** `RULES_ICE_HOCKEY.md` and `RULES_NHL.md`; `PROBABILITY_TOOLKIT.md` §2 and §2.3; `BASE_RATES_REGISTER.md` §7.2; `LEAGUE_PROFILES.md` Ice hockey (NHL); `SOURCES.md` §3.9; archive `Previous Sports Results/Ice Hockey/NHL/<year>/<year>_games.csv` (`Home Score`, `Away Score`, `Total Goals`, `Decision Type`, `Overtime`, `Shootout`).

**Research:** confirmed starting goalies (if unconfirmed, model a goalie mixture), backup quality, goalie workload; scratches, forward lines and defence pairs; injuries; 5v5 expected goals and high-danger chances; shot generation and suppression; power play, penalty kill and penalty rates; finishing and save-percentage regression; rest, back-to-backs and travel; home ice.

**Expected score (goals):** each team over the full game including OT/SO, with the OT/SO share stated; total, margin and SDs (§3a).

**Distribution:** regulation goals as goalie-adjusted Poisson (or a bivariate variant). Resolve regulation ties with the league's overtime and shootout rules (a shootout adds one goal to the winner); about 22% of NHL games reach overtime (LEAGUE_PROFILES). Add an explicit late empty-net branch for one- and two-goal leads.

**Family checks:**
- State whether each row settles on regulation or the full game.
- A −1.5 or −2.5 puck line needs the margin distribution printed. P(margin ≥ 2) is about 60% and P(margin ≥ 3) about 40% of NHL games (LEAGUE_PROFILES), and larger margins are rarer (the P-200 lesson).
- An unconfirmed goalie blocks a fragile totals Rank 1.

### B5. TENNIS

Upcoming match: `<Player A vs Player B>`, `<Tournament, round>` · Estimated start: `<…>`
Supplied contracts (reference only): 1. `<…>` 2. `<…>` 3. `<…>` 4. `<…>`

**Open:** `RULES_TENNIS.md`; `PROBABILITY_TOOLKIT.md` §6 (tennis Elo) and §1; `BASE_RATES_REGISTER.md` §6 and §7.4 (deciding-set reference rates); `SOURCES.md` §3.10; archive: the tennis yearly files are header-only, so write `ARCHIVE_UNAVAILABLE: Tennis yearly files are header-only` and use the SOURCES tennis routes (match statistics and the Sackmann files) for serve and return statistics.

**Research:** verified players, round, surface, indoor or outdoor, best-of-3 or best-of-5, qualifying versus main draw; injury, medical and retirement news; recent workload and match durations; rest and travel; surface-specific form; opponent-adjusted quality; serve points won, first- and second-serve performance, hold rate, aces and double faults; return points won and break conversion; tiebreak record; handedness and style; overall and surface Elo benchmark. Head-to-head matters only when surface, level, fitness and style are comparable.

**Expected score (games):** each player's expected games, total games, margin in games, expected sets and P(deciding set) (§3a).

**Distribution:** one point-to-match score tree. Use point-on-serve probabilities for each player (opponent-adjusted, surface-adjusted), exact game, tiebreak and set enumeration, and a **match-level form random effect**. The plain independent-point model over-states deciding sets: P-551 and P-555 were reproduced at 0.50 deciding-set mass where the reference is 0.358. Winner, games handicaps and games totals all come from this one tree.

**Family checks:**
- Print P(deciding set) beside the reference (ATP best-of-3 0.358, WTA 0.340; BASE_RATES §7.4 and RULES_TENNIS). Explain any gap above about 8 points.
- Totals between 19.5 and 25.5 games are mostly deciding-set bets; say so.
- At most one of the two picks may need a deciding set.
- Endpoint: a completed match. Under the framework convention a retirement voids games rows, and the winner settles to the advancing player.

### B6. SOCCER

Upcoming match: `<Home vs Away>`, `<Competition>` · Estimated start: `<…>`
Supplied contracts (reference only): 1. `<…>` 2. `<…>` 3. `<…>` 4. `<…>`

**Open:** `RULES_SOCCER.md` and `LEAGUE_RULES_SOCCER.md` (competition format, extra time, tie-breaks); `PROBABILITY_TOOLKIT.md` §2.1 and §2.2; `BASE_RATES_REGISTER.md` §7.3; `LEAGUE_PROFILES.md` Soccer (EPL row); `SOURCES.md` §3.4 and the reachability matrix; archive: the soccer yearly files are header-only, so for the English Premier League open `research/data/processed/league_csv/epl_results.csv`, otherwise write `ARCHIVE_UNAVAILABLE: Soccer yearly files are header-only`.

**Research:** confirmed starting XI, goalkeeper and bench; injuries and suspensions; rotation (cup ties, congestion); tactical changes; xG and xGA; shots and shots on target; finishing and save regression; pressing and transitions; set pieces; home and away splits; opponent-adjusted form; rest and travel; weather and venue; competition incentives (aggregate state, table position, two-leg ties).

**Expected score (goals):** each team over 90 minutes plus stoppage, total, margin and SDs; first-half goals per team when a first-half row is priced; corners only with their provider (§3a).

**Distribution:** a Dixon–Coles score matrix for 90 minutes plus stoppage time, with **separate first-half and second-half λ**. In EPL 2025-26, first-half goals were 1.19 of 2.75 per match, and P(first-half goal) was 0.716 (BASE_RATES §7.3). 1X2 (with the draw), first-half rows, totals, team totals and double chance all come from this one matrix. Corners need their own negative-binomial count model with score-state effects (EPL mean 10.0 per match, SD 3.27) and a named settlement provider. Extra time and penalties apply only if the contract says so.

**Family checks:**
- A first-half Over 0.5 at Rank 1 needs the half-split λ printed, `p_card` of at least 72% (SELECTION_RULES §4) and at least 5 points above the next candidate. Five Rank-1 first-half Overs failed in the 2026-10-09 cohort.
- For a rotated or cup favourite, discount first-half conversion: territory is not timing.
- A team-to-score probability above 80% needs both confirmed XIs and the implied λ printed.
- Four candidates only. The format and the top-two rule replace the older five-pick slate.

### B7. RUGBY LEAGUE / RUGBY UNION

Upcoming match: `<Team A vs Team B>`, `<Competition>` · Estimated start: `<…>`
Supplied contracts (reference only): 1. `<…>` 2. `<…>` 3. `<…>` 4. `<…>`

**Open:** `RULES_NRL_RUGBY.md` (league) or `RULES_RUGBY_UNION.md` (union); `PROBABILITY_TOOLKIT.md` §1; `BASE_RATES_REGISTER.md` §7.7 and the finals and six-again rows of the regime table; `LEAGUE_PROFILES.md` Rugby league (NRL); `SOURCES.md` §3.6 (league) or §3.7 (union); archive `Previous Sports Results/Rugby League/NRL/<year>/<year>_games.csv` (scores, halftime scores, tries, goals, field goals); the rugby union yearly files are header-only (`ARCHIVE_UNAVAILABLE`).

**Research (league):** confirmed team list and late changes; spine (fullback, halves, hooker); forward pack and bench; metres per set and post-contact metres; line breaks and tackle breaks; ruck speed; completion and error rates; kicking and field position; red-zone attack; defensive efficiency; penalties and six-agains; rest, travel and weather.
**Research (union):** confirmed XV and bench; halves and goal-kicker; scrum and front-row matchup; lineout; breakdown; gain line; territory and kicking; discipline and cards; attacking entries; goal-kicking percentage; bench impact; rest, travel and weather.

**Expected score (points):** each team, total, margin and SDs, from the score-event means (§3a).

**Distribution:** a score-event model: tries, conversions, penalty goals and field goals as count processes from team ratings, giving joint margin and total (NRL: try 4, conversion 2, penalty goal 2, field goal 1; key margins in LEAGUE_PROFILES). Knockout and finals games are tighter and lower-scoring, so apply the finals compression from the regime table (the P-534 lesson). Resolve golden point or extra time as the endpoint requires.

**Family checks:** print the margin distribution around key numbers. A handicap above about 4.5 in a near-even final needs explicit support.

### B8. AFL / AFLW

Upcoming game: `<Team A vs Team B>`, `<AFL | AFLW>` · Estimated start: `<…>`
Supplied contracts (reference only): 1. `<…>` 2. `<…>` 3. `<…>` 4. `<…>`

**Open:** `RULES_AFL.md`; `PROBABILITY_TOOLKIT.md` §1; `BASE_RATES_REGISTER.md` §7.7 and the AFL rows of the regime table; `LEAGUE_PROFILES.md` Australian rules (AFL, AFLW); `SOURCES.md` §3.5; archive `Previous Sports Results/AFL/AFL/<year>/<year>_games.csv` or `AFL/AFLW/...` (`Game Score` text, `Total Points`, `Winning Margin`).

**Research:** final teams and late changes; injuries; midfield availability and ruck matchup; contested possessions; clearances and centre clearances; inside-50s; scoring shots and shot quality; goal accuracy and its regression; intercepts and turnovers; pressure and tackles; marks inside 50; defensive transition; venue; travel and rest; weather and wind; opponent-adjusted form.

**Expected score (points):** each team's expected goals and behinds, with points = 6 × goals + behinds; total, margin and SDs (§3a).

**Distribution:** scoring shots per team (negative binomial, mean and dispersion from LEAGUE_PROFILES) × goal conversion (beta-binomial around 53% for AFL and 46% for AFLW), with points = 6 × goals + behinds. Keep shot creation separate from accuracy. Shrink unusual recent accuracy toward the league rate. Apply weather and wind to both creation and conversion.

**Family checks:** totals use the current competition era's scoring level (AFLW totals differ markedly from AFL). Print P(total ≤ line) from the shot × conversion model.

### B9. AMERICAN FOOTBALL

Upcoming game: `<Away @ Home>`, `<NFL | CFB | other>` · Estimated start: `<…>`
Supplied contracts (reference only): 1. `<…>` 2. `<…>` 3. `<…>` 4. `<…>`

**Open:** `RULES_AMERICAN_FOOTBALL.md`; `PROBABILITY_TOOLKIT.md` §1; `BASE_RATES_REGISTER.md` §7.7 and the NFL rows of the regime table; `LEAGUE_PROFILES.md` American football (NFL profile and the absolute-margin table); `SOURCES.md` §3.8; archive `Previous Sports Results/American Football/NFL/<year>/<year>_games.csv` (`Game Score` text, `Total Points`, `Winning Margin`).

**Research:** starting QB, QB injuries and backup; offensive-line injuries; receivers, running backs and tight ends; defensive injuries; EPA per play and success rate; passing and rushing efficiency; pressure and sack rates; explosive plays; early-down efficiency; red-zone performance; turnover regression; pace and play volume; special teams; coaching and tactical changes; rest and travel; home field; weather and wind.

**Expected score (points):** each team, total, margin and SDs, from the drive model (§3a).

**Distribution:** drive-based discrete scoring. Model the number of drives and the drive outcome probabilities (0, 2, 3, 6, 7, 8 points) per team, giving a discrete joint score and margin. Key margins (3, 7, 10, 14) must emerge from the discrete model, not from a smoothed normal; compare with the NFL absolute-margin table in LEAGUE_PROFILES (margin 3 is 14.6% of games, margin 7 is 8.7%). Resolve overtime under the league's rule.

**Family checks:** print P(margin = 3) and P(margin = 7) beside any spread within 1 point of them. Re-forecast after any change of starting QB (A8).

---

## No fitted models

The Markdown-only framework has no fitted pipeline, calibrator or saved model. Every card is an `UNCALIBRATED_ANALYST_SCENARIO`. Winner-class, total and handicap probabilities all come from the one distribution you built by hand, and nothing is borrowed from another league. Never substitute a ranking q for a probability. Do not fabricate historical probabilities to populate a scoreboard. New rows keep their issued `p_card` values for later settlement and calibration scoring.
