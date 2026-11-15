# Local analytical input snapshot — LOCAL-20261114B4496A3F-G0002
Captured: 2026-11-14T15:35:35+11:00
Reference SHA: GitHub main 008cedc4ff469e7a808292aa3667a7bffe22e273
Local-only read-only framework reference; no repository reference run / no Git freeze / no publication.

Event: WBBL|12 Match 21, Hobart Hurricanes Women vs Brisbane Heat Women.
Venue: Ninja Stadium/Bellerive Oval, Hobart, Tasmania, Australia
Scheduled first ball: 14 November 2026 15:40 AEDT = 04:40 UTC.
Toss at capture: Brisbane Heat Women chose to field (Cricbuzz match centre);
Hobart bats FIRST, not a chase. Confirmed XI in source below.
No in-play scores/outcomes used. Actual first ball NOT_VERIFIED.

Supplied full-innings Hobart contracts:
- runs at completion of first six legal overs, Over/Under 41.5
- first batting innings final (scheduled 20 overs), Over/Under 152.5.
A shortened innings/abandoned play requires operator settlement terms; not assumed an Under.
WBBL12 field restriction powerplay is first FOUR overs, then 2-over Power Surge; six-over checkpoint is different.

Recent WBBL-only Hobart 2026 before event (chronological 29 Oct, 1 Nov, 4 Nov, 7 Nov, 10 Nov):
- first six runs: [62, 21, 34, 23, 40]; mean 36.000, sample sd 16.508; n5 (the Nov 1 109 all-out later at 17.4 overs but reached 6).
- final runs: [174, 109, 154, 116, 138]; mean 138.200, sample sd 26.818; n5.
- innings batting first: Nov 4 154, Nov 7 116, Nov 10 138 (n3 mean 136.0).
- Bellerive only Nov 4 154, Nov 10 138 (n2 mean 146.0).
- Heat opponent runs allowed last 5: [157, 180, 170, 116, 165]; mean 157.600; n5, last H2H 116 counted in both teams' records (do not count as independent event).
- Venue Bellerive womens T20 historical first-innings 141 runs in 48 matches, descriptive CREX source; scope/method not independently certified.
- Spring Challenge Oct2026 Hobart scores 127,136,136,129 (different competition; descriptive sensitivity only).

Model assumptions locked before probability calculation (local analyst only):
- Hobart first six P6 ~ Normal(mu=36.000, sd=16.508) as small-sample retrospective phase proxy; unusual opening-overs wicket volatility retained.
- Innings total I20 ~ Normal(mu = 0.65 * Hobart WBBL L5 mean 138.200
    +0.25 * Heat opponents L5 mean 157.600
    +0.10 * Bellerive first-innings historical mean 141.0
    = 143.330, sd=28.000 runs).
- 0.65/0.25/0.10 weights are analyst judgement, not fit/calibrated. Opponent/wbbl runs include the same 7 Nov H2H event; blend is an overlapping descriptive lens, not 3 independent observations.
- Empirical current sample std innings 26.818; inflated to 28.000 due venue, XI and weather uncertainty.
- Same innings dependence: model full I20 = P6 + R(overs 7–20). Choose a bivariate normal with Corr(P6,I20)=0.50 as an unvalidated sensitivity assumption; all ranked rows are marginal p only and joint outcomes NOT_COMPUTED, Fréchet bounds reported. No binomial simulation or validated phase/wicket model exists.
- Treat probabilities conditional on a complete/sportingly settled six-over checkpoint and a scheduled-20-over innings, not an unverified bookmaker-void schedule.
- Climate: BOM Bellerive 14 Nov forecast issued 09:45 AEDT: 95% rain chance across DAY, showers easing by late afternoon. Do not read this as 95% probability of rain during innings. No unsubstantiated numerical weather shift; interruption risk kept as separately unpriced branch.
- Squads/availability: Hurricanes XI Lee, Trenaman, Carey, Green, Graham, Henry, Strano, Silver-Holmes, Lauren Smith, Malgioglio, Linsey Smith. Heat XI Knott, Harris, Redmayne, Bhatia, Prendergast, Hamilton, O'Neil, Ginger, Wrigley, Glenn, Bassingthwaighte. Confirmed via Cricbuzz at research time; source capture timestamp not independently stamped by provider.
- Athapaththu omitted, Linsey Smith added (bowler returning quad injury). Lee and Trenaman first listed for Hobart, presumed top-order; no unsupported official fixed batting position beyond teams.
- Source-access audit from repo `ml source-audit` NOT_RUN; original published source pages were fetched by web search; same-retreival time exact publication time unknown.
- Price candidate universe: supplied only (Under/Over 41.5; Under/Over 152.5), avoiding easy constructed alternate lines.
- Baseline independent-source WBBL PP6 rate: NOT_AVAILABLE; no published BASELINE_P for phase without valid league data.
- Non-causal 2025-26 results L10/15/20 kept for descriptive continuity only; major roster changes and chase truncation keep them out of centre.
- Uncertain switch/low/base/high sensitivity to be computed later; no rain-shortening win/void p assigned.

Evidence sources:
1. https://www.hobarthurricanes.com.au/news/4608444/smith-set-for-wbbl-return-against-heat
2. https://www.cricbuzz.com/live-cricket-scores/162851/hbhw-vs-brhw-21st-match-wbbl-2026
3. https://www.cricket.com.au/news/4568917/big-bash-league-batters-to-benefit-from-tougher-over-rate-penalties-bbl16-wbbl12-playing-conditions-changes-countdown-timer-powerplay
4. https://www.bom.gov.au/places/tas/bellerive/forecast/
5. https://www.sportsguff.com/scorecard/women-s-big-bash-league-2026-27/brisbane-heat-women-vs-hobart-hurricanes-women-14th-match
6. https://cricketfieldguide.com/match/melbourne-stars-women-v-hobart-hurricanes-women-01m65hhqp7fthbrcn0e57r7cpy
7. https://cricketfieldguide.com/match/sydney-sixers-women-v-hobart-hurricanes-women-01m6d8wdwjfs3b2w310hf2z2pj
8. https://cricketfieldguide.com/match/hobart-hurricanes-women-v-melbourne-renegades-women-01m6mzzbxmebhv0z5fsx6qypvg
9. https://cricketfieldguide.com/match/hobart-hurricanes-women-v-adelaide-strikers-women-01m74ep1pfeess3vad7byr4z5a
10. https://crex.com/cricket-live-score/bh-w-vs-hbh-w-21st-t20-womens-big-bash-league-2026-match-updates-12XO
