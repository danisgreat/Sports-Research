<!-- BEGIN CANONICAL RESEARCH P-612 -->
## P-612 — BASKETBALL / NBL · Melbourne United vs Illawarra Hawks · 2026-10-18
Import: 2026-10-21T01:07:13+11:00; prompt 4 NEW_CANONICAL_EVENT. Local event key `LOCAL-20261018MELILL01-G0001` → canonical **P-612**; native identity ESPN NBL 401875272. Source mini `20261018MELILL01`, frozen source SHA-256 `f5163079058a28a8c9a900009f112838b0ca50c3f6985c8a363248d290b6e245` (142,555 bytes). Card core SHA-256 `ad26ba0ddeea90240748f62601a56e81c5c16d7717283f7030fe5f7a61bec019` (31,421 bytes) = the exact bytes between the local BEGIN/END CARD marker lines (source offsets 11488–42909); markers and headings outside them remain in the preserved source. Original method, probabilities, ranks, statuses, timing and gaps are literal; any NOT_ASSIGNED / PENDING wording inside the core is historical. Import is not a forecast timestamp and confers no certification.

## Card · LOCAL-20261018MELILL01-G0001 · BASKETBALL / NBL27 · Melbourne United vs Illawarra Hawks · 2026-10-18

### Owner-entered Upcoming Basketball Game block (retained verbatim in meaning)

> Upcoming Basketball Game: Melbourne United vs Illawarra Hawks, Australia NBL  
> Estimated Game Time Start: 18 October 2026, 5:00 PM AEDT (may be delayed; research continues)  
> Supplied: United -10.5; Hawks +10.5; Combined Total Over 201.5 Points; Combined Total Under 201.5 Points.  
> Research all sources, both teams, availability, injuries, and the best four picks where supportable. Include a winner. Do not perform retrospective or settlement. Accuracy, source quality and truthful timing take priority.

### Card metadata

- **Provisional local event key:** `LOCAL-20261018MELILL01-G0001` — DRAFT_ONLY; native surrogate `NBL27-2026-10-18-MEL-ILL`, pending exact official match identifier.
- **Canonical ID:** NOT_ASSIGNED; only prompt 4 may assign.
- **Analysis status:** ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY; approximate distribution, not a fitted or validated predictive model.
- **Issuance:** POST_SCHEDULED_START_DRAFT, NOT VERIFIED AS A PRE-TIP ISSUED CARD. The user request was received before the scheduled 17:00 AEDT start; this completed analysis is after that scheduled time. Actual tip, live score and outcome NOT INSPECTED / NOT VERIFIED; no score-result information was used. Evidence known-before-start status remains partly KNOWN_AT_UNVERIFIED.
- **Scheduled start:** 2026-10-18 17:00 AEDT (UTC+11, Australia/Melbourne/Sydney), 06:00 UTC. John Cain Arena, Melbourne, Australia. Confirmed by NBL official preview and both teams.
- **Format:** NBL regulation 4 × 10-minute quarters, five-minute overtime when tied. The user-supplied full-game handicaps/totals are **conditionally** interpreted as including overtime; operator-specific settlement/void rules have not been independently verified, so `UNKNOWN_DEFINITION` remains for settlement use.
- **Independent market-blind research:** YES. No bookmaker odds, tips, prediction sites, betting-derived signals or ML/RL used. Supplied numerical lines used only as contract thresholds.
- **Source horizon:** games through 2026-10-11 for Illawarra and 2026-10-10 for Melbourne; earlier dates for injury/preview reports. Retrospective match results, match live-state, and result-based model fitting expressly excluded.
- **Venue / playing conditions:** Indoor court; weather effect not applicable. Melbourne at home, Illawarra travelling interstate. No independently quantified rest/travel penalty assigned.
- **League-specific historical benchmark:** NBL 2025–26 total mean 182.5 points, width 18.7 points, margin width 15.2, pooled home-margin effect +1.57; historical OT rate 5.5%, average OT points added 24.4 (BASE_RATES_REGISTER §7.1 / PROBABILITY_TOOLKIT §4.3). The 2025–26 league-mean 91.25 points/team is the historical level; use with clear cross-season uncertainty.
- **Team form inputs:** Melbourne current n=6 PF=558 PA=539; Illawarra n=7 PF=698 PA=756. Distinct from old-season L20 comparisons.
- **Distribution object:** `MANUAL_NBL2026_NORMAL_V1`; score total T approx Normal(189.945, 21.0²), final no-tie Melbourne margin M approx Normal(+4.850, 17.0²); paired score means (T±M)/2. Dependence and covariance NOT_ESTIMATED; separate normal marginals do not establish an exact joint. Width inflation is judgemental 12% above historical residual benchmarks for early season and lineup uncertainty.
- **Pricing basis:** BASE, with low/high centre sensitivity disclosed; not a statistical confidence interval or trained mixture. The normal approximation uses historical final-score residual widths that already include overtime effects; no extra OT points are added again. Overtime branch detail is unresolved without regulation-tie and possession event data.
- **Expected points including overtime:** Melbourne 97.398; Illawarra 92.548; total 189.945; Melbourne margin +4.850. Team-specific SD, team-score covariance and any exact-score mode: NOT_COMPUTED.
- **Potential winner:** Melbourne United 0.612 / Illawarra Hawks 0.388, conditional on stated uncalibrated event distribution and a no-tie full-game endpoint.

### Decision block

**Primary direction: Under 201.5; secondary: Illawarra +10.5.** Melbourne is the more likely outright winner, but winning by eleven or more is a separate and less probable requirement. The total case is sensitive to Illawarra's volatile early-season scoring and the unknown starting fives. No betting profitability or model calibration is claimed.

| Rank among supplied propositions | Primary role | Tag | Exact contract | p_card | BASELINE_P | Distance from model centre | Main failure mechanism |
|---:|---|---|---|---:|---:|---|---|
| 1 | PICK, RANK1_UNSTABLE under sensitivity | SUPPLIED | Combined points Under 201.5 | **0.709** | 0.845 (historical league-only; stale-year comparator) | 201.5 − 189.945 = +11.555; z=+0.550 | High-possession Hawks offence, Melbourne transition scoring, late fouling/overtime |
| 2 | PICK, floor met | SUPPLIED | Illawarra Hawks +10.5 points | **0.630** | 0.722 (historical league-only) | (10.5 − 4.850)/17 = +0.332 | Hawks' league-worst defence allows a Melbourne double-digit breakaway |
| 3 | INFORMATIONAL — complement of Rank 2, NOT simultaneous pick | SUPPLIED | Melbourne United −10.5 points | 0.370 | 0.278 | z for cover=(4.850 − 10.5)/17 = −0.332 | Hawks' scoring/bench pace keeps margin within ten |
| 4 | INFORMATIONAL — complement of Rank 1, NOT simultaneous pick | SUPPLIED | Combined points Over 201.5 | 0.291 | 0.155 | 201.5 −189.945=+11.555; z=+0.550 | Melbourne defensive pressure, lower pace, Hawks inefficient shooting |

**Selection discipline.** These are all four supplied propositions in descending conditional probability, not four mutually compatible picks. The two lower-ranked rows are complements and therefore are *not* recommended alongside the corresponding higher-ranked rows. No additional player prop is fabricated to fill a four-pick slate. No line moving or margin selection based on odds.

**Rank-1 numeric gate:** arithmetic p=0.709 ≥0.620 and advantage over Rank 2 =0.709−0.630=0.079 ≥0.040; precision epsilon ≈0.002 per probability, difference epsilon ≈0.004. `PASS_BASE_CASE / RANK1_UNSTABLE_SENSITIVITY` (a +6-point total centre shift can push p below 0.62). **Rank 2:** 0.630 ≥0.580, PASS_BASE_CASE. Neither is calibrated or certified.

**Baseline coverage:** 4/4 conditional estimates from historical league-only NBL level/width; exact current-season league-rate reference not verified, marked STALE_COMPARATOR. Historical league-only baseline is not evidence of card skill. **TEAM_BASELINE_P:** the TB-1-MD centre below is used as manual starting point but has no separately calculated, independently frozen alternate output.

**Joint dependence:** under and Hawks +10.5 are not independent. Given marginals alone, joint win probability bounded by max(0,0.709+0.630−1)=0.339 and min(0.709,0.630)=0.630. Joint failure (Over 201.5 AND Melbourne −10.5) lies between 0 and min(0.291,0.370)=0.291; **NOT_COMPUTED exactly**. Avoid multiplying probabilities or claiming a protected two-leg slate.

### A1. Event identity, timing, competition and state

- Organizer exact-game preview: https://www.nbl.com.au/news/how-to-watch-talking-points-melbourne-united-v-illawarra ; event page https://www.nbl.com.au/matches/melbourne-united-v-illawarra-hawks-men-18-10-2026 . League Round 5, NBL27 regular season, 17:00 AEDT 18 October 2026, John Cain Arena.
- Melbourne team preview 17 Oct: https://www.melbourneutd.com.au/news/nbl27-preview---round-5-vs-illawarra-hawks . NOTE: This preview erroneously labels 17:00 as AEST although the date is in AEDT; use NBL fixture/other club's AEDT, +11 UTC.
- Illawarra preview 17 Oct: https://www.hawks.com.au/news/game-preview-hawks-melbourne-united-rd5-nbl27 .
- Identity searched under MEL v ILL, Melbourne United–Illawarra Hawks, NBL27 Round 5. Native match ID not verified; game URL identifies matchup/date. No confirmed earlier copy of this exact game found in the material inspected, but unenumerated active minis prevent a definitive no-duplicate assertion.
- User submitted before the 17:00 scheduled start. The exact start/first jump ball and final forecast issue time are unverified. No live scoreboard, live roster or current result was consulted. The draft is not a pre-tip issuance, not retrospective analysis and is not eligible for prospective pregame performance grading.

### A2. Frozen supplied contracts and candidate recipe

At intake (not the match result), four half-point full-game propositions: United −10.5; Illawarra +10.5; total Over 201.5; total Under 201.5. All retained. Endpoints conditionally include overtime; verify the operator's settlement wording before ever settling. Analysis recipe fixed as current-season shrunk scored/conceded averages versus a historical league anchor with NBL normal residual widths; not candidate-scanned or price-derived. Exactly two complementary pairs; no exact push on half points.

### A3. Evidence: availability, tactical mechanisms and online historical rows

**Team/league official pre-match evidence.** NBL official match preview dated 18 Oct gives an **expected** depth chart, not a confirmed game-selected five. Melbourne: Anthony/Ili, Machar/Wilson, Travers/Ingles, Waardenburg/Bowen and Oduro/Krslovic are depth-chart members across positions; Austin Shelley, Jai Fa'Ale and Jensen Bradtke selected to suit up per Melbourne's 17 Oct squad update (https://www.melbourneutd.com.au/news/nbl27-squad-update-round-5). Chris Goulding OUT (calf, illness delaying return to around Round 7); Sean Macdonald OUT (ACL, season). The official update is one club lineage, the NBL preview a related re-publication, not independent proof of every field.

Illawarra: NBL **expected** depth chart includes Milton Doyle, Will Hickey, Tyler Harvey, Kobe Narkle, Wani Swaka Lo Buluk, Daniel Grida, Kelan Martin, LaMarcus Days, Sam Froling, Makur Maker and other reserves. Todd Blanchfield OUT (hand, return TBC); Mason Peatling OUT (foot, season-ending surgery, original Illawarra release 9 Oct: https://www.hawks.com.au/news/mason-peatling-injury-update-nbl27). Exact starters and active bench unconfirmed. No assumption that other depth-chart players are medically cleared or will play specific minutes.

**Player and matchup evidence.** Hawks official pregame describes Hawks' 99.7 points scored, 108.0 conceded, league-leading fast-break/paint/bench scoring, and deficient defence, plus second-most fouls; United has comparatively low 3-point volume, second-most free-throw attempts, and 30.3% 3-point shooting (club: https://www.hawks.com.au/news/game-preview-hawks-melbourne-united-rd5-nbl27). For United, Josh Oduro season 17.5 points/7.5 rebounds at 71.4% FG; Luke Travers 13.5 points/6.3 rebounds/4 assists, Joe Ingles 10.8 points/3.8 assists (Hawks' preview, independent of United's club), with Travers' recent 24-point outing noted by NBL. Hawks official player statistics (https://www.hawks.com.au/statistics) list Kelan Martin 16.86 PPG, Sam Froling 13.71 PPG and 7.43 RPG, Will Hickey 13.00 PPG/3.86 APG, Tyler Harvey 11.43 PPG/3.14 APG and Milton Doyle 11.71 PPG. The source displays season-to-date through seven games for those players; role/minute forecasts are NOT inferred from their averages.

**Historical eligibility:** Ordered newest-to-oldest, both sides. 2026–27 regular season and relevant late-2025/26 competitive games, including Melbourne's verified March 2026 postseason. Scores always `team PF–PA`, not the home-away orientation in the schedule. Dates before Oct 18 kickoff. Basketball-Reference season schedules + NBL original match accounts provide partial independent corroboration, not verified row-by-row independent collection.

**Melbourne United — last 20 eligible dated games (newest first).** Sources: https://www.basketball-reference.com/international/schedules/melbourne/2027.html ; https://www.basketball-reference.com/international/schedules/melbourne/2026.html ; March play-ins: https://www.nbl.com.au/news/delany-leads-united-over-plucky-jackjumpers and https://www.nbl.com.au/news/second-half-blitz-sees-wildcats-advance .

| Date | Season / status | Opponent (venue) | Melbourne PF–PA |
|---|---|---|---:|
| 2026-10-10 | NBL27 regular | South East Melbourne Phoenix (away) | 104–99 |
| 2026-10-07 | NBL27 regular | Adelaide 36ers (away) | 96–91 |
| 2026-10-03 | NBL27 regular | Cairns Taipans (home) | 95–107 |
| 2026-10-01 | NBL27 regular | Tasmania JackJumpers (away) | 82–84 |
| 2026-09-24 | NBL27 regular | South East Melbourne Phoenix (away) | 86–61 |
| 2026-09-19 | NBL27 regular | Adelaide 36ers (home) | 95–97 |
| 2026-03-07 | NBL26 play-in | Perth Wildcats (away) | 77–95 |
| 2026-03-05 | NBL26 play-in | Tasmania JackJumpers (home) | 82–68 |
| 2026-02-19 | NBL26 regular | South East Melbourne Phoenix (home) | 95–91 |
| 2026-02-14 | NBL26 regular | Illawarra Hawks (home) | 91–100 |
| 2026-02-12 | NBL26 regular | Cairns Taipans (away) | 89–85 |
| 2026-02-07 | NBL26 regular | Adelaide 36ers (home) | 76–87 |
| 2026-01-30 | NBL26 regular | New Zealand Breakers (away) | 95–97 |
| 2026-01-25 | NBL26 regular | Perth Wildcats (away) | 74–73 |
| 2026-01-21 | NBL26 regular | Brisbane Bullets (home) | 98–66 |
| 2026-01-17 | NBL26 regular | Tasmania JackJumpers (home) | 79–77 |
| 2026-01-11 | NBL26 regular | Sydney Kings (away) | 94–97 |
| 2026-01-07 | NBL26 regular | Cairns Taipans (home) | 92–93 |
| 2026-01-03 | NBL26 regular | Tasmania JackJumpers (away) | 75–84 |
| 2025-12-27 | NBL26 regular | Brisbane Bullets (away) | 92–87 |

**Illawarra Hawks — last 20 eligible dated games (newest first).** Sources: https://www.basketball-reference.com/international/schedules/illawarra/2027.html ; https://www.basketball-reference.com/international/schedules/illawarra/2026.html ; https://www.nbl.com.au/club-schedule/ill ; season-close team context https://www.nbl.com.au/news/illawarra-hawks-justin-tatum-what-might-have-been-nbl26 .

| Date | Season / status | Opponent (venue) | Illawarra PF–PA |
|---|---|---|---:|
| 2026-10-11 | NBL27 regular | Cairns Taipans (home) | 100–110 |
| 2026-10-09 | NBL27 regular | Tasmania JackJumpers (home) | 112–122 |
| 2026-10-04 | NBL27 regular | South East Melbourne Phoenix (away) | 96–113 |
| 2026-10-02 | NBL27 regular | Adelaide 36ers (home) | 114–92 |
| 2026-09-27 | NBL27 regular | Sydney Kings (away) | 100–121 |
| 2026-09-25 | NBL27 regular | Brisbane Bullets (away) | 95–103 |
| 2026-09-20 | NBL27 regular | New Zealand Breakers (away) | 81–95 |
| 2026-02-18 | NBL26 regular | Tasmania JackJumpers (away) | 103–70 |
| 2026-02-14 | NBL26 regular | Melbourne United (away) | 100–91 |
| 2026-02-13 | NBL26 regular | Sydney Kings (home) | 94–120 |
| 2026-02-07 | NBL26 regular | New Zealand Breakers (away) | 95–106 |
| 2026-02-05 | NBL26 regular | Adelaide 36ers (home) | 100–99 |
| 2026-01-31 | NBL26 regular | Perth Wildcats (home) | 99–106 |
| 2026-01-29 | NBL26 regular | Sydney Kings (away) | 104–122 |
| 2026-01-26 | NBL26 regular | Brisbane Bullets (away) | 113–75 |
| 2026-01-24 | NBL26 regular | Tasmania JackJumpers (away) | 101–91 |
| 2026-01-16 | NBL26 regular | Perth Wildcats (away) | 87–92 |
| 2026-01-10 | NBL26 regular | New Zealand Breakers (home) | 96–101 |
| 2026-01-08 | NBL26 regular | South East Melbourne Phoenix (away) | 113–124 |
| 2026-01-03 | NBL26 regular | Cairns Taipans (home) | 96–78 |

**Form windows, true n and source-supported rates.** Cross-season rows include substantial roster/coach-regime changes and are descriptive, not carried as equal-strength current forecasts. Windows overlap; counted once.

| Side / window | True n | Scored PG | Conceded PG | Net PG | Prior-season rows | Source coverage status |
|---|---:|---:|---:|---:|---:|---|
| United L5 | 5 | 92.60 | 88.40 | +4.20 | 0 | same-season |
| United L10 | 10 | 90.30 | 89.30 | +1.00 | 4 | 2 playoff +2 regular |
| United L15 | 15 | 89.00 | 86.73 | +2.27 | 9 | postseason/regular |
| United L20 | 20 | 88.35 | 86.95 | +1.40 | 14 | postseason/regular |
| United 2026–27 | 6 | 93.00 | 89.83 | +3.17 | 0 | PF 558, PA 539 |
| Hawks L5 | 5 | 104.40 | 111.60 | −7.20 | 0 | same-season |
| Hawks L10 | 10 | 99.50 | 103.70 | −4.20 | 3 | 3 old regular |
| Hawks L15 | 15 | 100.40 | 103.00 | −2.60 | 8 | 8 old regular |
| Hawks L20 | 20 | 99.95 | 101.55 | −1.60 | 13 | 13 old regular |
| Hawks 2026–27 | 7 | 99.71 | 108.00 | −8.29 | 0 | PF 698, PA 756 |
| NBL historical league | 165 (2025–26) | 91.25 per side | 91.25 per side | +1.57 pooled home edge, not team margin | previous season | mean total 182.5, BASE_RATES_REGISTER §7.1 |

For the current-season centre the shrinkage recipe (§A4) uses the season-to-date PF/PA and league mean, *not* an extra unquantified overlapping L5/L10/L15/L20 recency overlay. Full opponent-quality ratings and complete independent row-by-row verification are not available; `INFORMATION_INCOMPLETE` remains. Roster continuity is poor enough that older-season rows are descriptive only. League current-season offensive rate and full possession/ORtg/DRtg were not established independently.

### A4. Distribution, shrinkage, baseline and manual arithmetic

**Inputs; no code run.** Historical NBL 2025–26 league per-team mean `LM = 182.5/2 = 91.25`. Toolkit §4 NBL shrinkage `k=5`; pooled home edge `HE=+1.57`. Melbourne PF=558 PA=539 n=6; Illawarra PF=698 PA=756 n=7. Historical widths total σ=18.7, margin σ=15.2. No odds or online predictor inputs.

| Quantity | Manual expression | Result |
|---|---|---:|
| United shrunk offence `O_U` | (558 + 5×91.25)/(6+5) = 1014.25/11 | 92.205 |
| United shrunk defence `D_U` | (539 + 5×91.25)/(6+5) = 995.25/11 | 90.477 |
| Hawks shrunk offence `O_H` | (698 + 5×91.25)/(7+5) = 1154.25/12 | 96.188 |
| Hawks shrunk defence `D_H` | (756 + 5×91.25)/(7+5) = 1212.25/12 | 101.021 |
| Expected total `T` | (O_U+D_H)/2 + (O_H+D_U)/2 | 189.945 |
| Expected United margin `M` | ((O_U−D_U)−(O_H−D_H))/2 +1.57 | +4.850 |
| United expected score | (T+M)/2 | 97.398 |
| Hawks expected score | (T−M)/2 | 92.547 |
| Total σ | historical 18.7 widened by factor 21/18.7=1.123 | 21.0 |
| Margin σ | historical 15.2 widened by factor 17/15.2=1.118 | 17.0 |

**Structural limitation:** These team PF/PA per-game ratings are a transparent **proxy**, not measured possessions×ORtg/DRtg; genuine possessions, four-factor efficiency, lineup stints, team-score covariance and within-game end-period dependence were not obtained. The normal total and final-margin marginals do not define a fully coherent bivariate score grid with legal support. Probability estimates are therefore approximate and uncalibrated; exact joint and team variances NOT_COMPUTED. The width factors are analyst assumptions for incomplete 2026–27 exposure/lineups, not fitted parameters. Scores from regulation and OT are already present in historical full-game residuals: league OT rate ~5.5%, +24.4 points in OT, roughly +1.34 expected points spread across all historical games. Do **not** add +1.34 again. A separate verified pregame overtime/tie-conditional calculation is unavailable.

**Probability formulas (PROBABILITY_TOOLKIT §1, half-point no push):**

- Under 201.5: `z=(201.5−189.945)/21.0=0.5502`; Φ(0.55)=0.7088 ⇒ **0.709**.
- Over 201.5: `1−0.7088=0.2912` ⇒ **0.291**.
- Illawarra +10.5: `z=(10.5−4.850)/17.0=0.3324`; Φ(0.3324)≈0.6302 ⇒ **0.630**.
- United −10.5: `1−0.6302=0.3698` ⇒ **0.370**.
- United wins full game: `z=4.850/17.0=0.2853`; Φ(0.2853)≈**0.612**; Hawks win 0.388. No final-game draw after required OTs.
- W/P/L/V per half-point row: W=`p_card`, L=`1−p_card`, P=0, V=0 **conditional on the assumed operator full-game/OT-inclusive action**. Unverified operator void rules may change action and must be resolved prior to settlement.
- Approximate numerical interpolation ε=0.002 per marginal p. Sampling/structural and input uncertainty is much larger than this tabular ε.

**Frozen league-only comparator, not fitted:** 2025–26 NBL total μ=182.5/σ=18.7 ⇒ Under 201.5 = Φ((201.5−182.5)/18.7) = Φ(1.016)=**0.845** (Over 0.155). Home-margin μ=+1.57/σ=15.2 ⇒ Hawks +10.5 = Φ((10.5−1.57)/15.2)=Φ(0.588)=**0.722** (United −10.5 0.278). These comparator parameters are from the historical league cohort, and do not represent current-season adaptation. No calibrated baseline skill claim.

**Sensitivity (alternative centres, not statistical confidence intervals):**

| Parameter scenario | Under 201.5 | Hawks +10.5 | United winner |
|---|---:|---:|---:|
| Baseline μT=189.945, μM=+4.850 | 0.709 | 0.630 | 0.612 |
| High-scoring +6 pts (μT=195.945); unchanged margin | Φ(5.555/21)=0.604 | 0.630 | 0.612 |
| Low-scoring −6 pts (μT=183.945); unchanged margin | Φ(17.555/21)=0.799 | 0.630 | 0.612 |
| United stronger by +4 margin pts (μM=+8.850); unchanged total | 0.709 | Φ(1.65/17)=0.539 | Φ(8.85/17)=0.699 |
| United weaker by −4 margin pts (μM=+0.850); unchanged total | 0.709 | Φ(9.65/17)=0.715 | Φ(0.85/17)=0.520 |

Genuine dependence between higher total and wider United winning margin may make both top picks fail together; no invented covariance or joint. A 2026 pace/regime revision could substantially affect Under 201.5. The current n is too small to equate recent form with persistent skill.

### A5. Supplied universe, action and exclusions

All four supplied contracts were priced, with exact proposition, half-point line, normal approximation, W/L from A4 and conditional full-game endpoint. Numeric eligible p values <=0.90. Primary selected Rank 1 Under, Rank 2 Hawks +10.5; complement rows Rank 3/4 informational. No further supported player-prop contract thresholds supplied or sourced. No derived line selected merely to inflate probability. No alternative at the same time may be represented as a distinct independent edge.

### A6. Mechanisms and adjustment register

| Adjustment or uncertainty | Applied centre change | Why |
|---|---|---|
| Venue/home | +1.57 United margin, league pooled NBL value | Historical NBL home effect per toolkit; not applied to total |
| Known Goulding/Macdonald absence | 0 additional, already captured in United 2026–27 form | Out per official club; avoid double-counting prior absence |
| Known Peatling/Blanchfield absence | 0 additional, already represented in Hawks 2026–27 mixed appearances/form | Out per official injury/preview; no verified minute-on/off coefficients |
| Potential late lineup changes | centre not shifted; widths widened | Starters not confirmed; do not invent replacements |
| Indoor weather | 0 | Not relevant |
| Rest/travel | 0 | Qualitative away travel, no validated NBL-specific quantified effect |
| Different prior-season rosters | 0 centre, old rows descriptive | 2025–26 L20 rows not transferred as equal-strength 2026–27 player regime |
| Historical-vs-2026 league pace shift | unresolved, high/low ±6 points total sensitivity | True 2026–27 league mean/possessions not independently measured |

**Mismatch-state checks:** Favourite sustains advantage => United −10.5/possibly high total; Hawks offensive response => Hawks +10.5/possibly high total; slow defensive match => Under; offensive suppression plus late fouling => Under may turn Over. No exact state weights estimated. No adjustments are falsely attributed to individual player plus-minus or a specific possession count.

### A7. Baseline/gates/selection/covariance and competing scenarios

- Primary p ordering exact to available 0.002 interpolation; complements sum 1.000 at stated precision. No draw, push or void under conditional stated full-game half-line assumptions. Overtime approximated as historical component of final scores only; exact OT accounting remains an unresolved field.
- Rank 1 p=0.709 gap=.079 (base gate pass); high-scoring scenario yields 0.604 below 0.62 threshold => RANK1_UNSTABLE_SENSITIVITY. Rank 2 base p=0.630 ≥0.58, but stronger-United scenario may fall to 0.539. Do not present numerical gates as success guarantees.
- Baseline difference (card − league-only comparator): Under 0.709−0.845=−0.136; Hawks cushion 0.630−0.722=−0.092. League-only comparator may be stale; no evidence of incremental predictive edge or calibration.
- Uncalibrated sensitivity means **not a reliable implied probability for financial or staking decisions**. No odds/expected monetary value, EV or market-adjusted inputs considered.
- `SHADOW: NOT_IN_SCOPE`, `ML/RL: NOT_RUN`, `SETTLEMENT: NOT_PERFORMED`, `CANONICAL_IMPORT: NOT_PERFORMED`.

### A8. Source and field-level research register

All listed pages concern the correct league/year or are explicitly historical controls. Publication dates are given only when displayed; exact per-field web retrieval/known-at stamps and all independent collection routes were not established. `OPEN_ATTEMPT_CACHE_MISS` is distinct from source non-publication.

| Source (URL) | Dated field(s) used | Independence and evidence limits |
|---|---|---|
| https://www.nbl.com.au/news/how-to-watch-talking-points-melbourne-united-v-illawarra | 18 Oct fixture, venue, expected depth charts, listed absences | Official organizer pregame, roster **not confirmation**; direct-open cache miss, search-index content recovered |
| https://www.nbl.com.au/matches/melbourne-united-v-illawarra-hawks-men-18-10-2026 | Fixture identity | Match centre returned limited details; starter/bench and first jump ball not verified |
| https://www.melbourneutd.com.au/news/nbl27-squad-update-round-5 | 17 Oct Goulding, Shelley, Fa'Ale, Bradtke | Primary Melbourne club announcement; direct-open cache miss, search-index content recovered |
| https://www.melbourneutd.com.au/news/nbl27-preview---round-5-vs-illawarra-hawks | 17 Oct personnel and tactics | Official United preview; time-zone typography erroneously says AEST |
| https://www.hawks.com.au/news/game-preview-hawks-melbourne-united-rd5-nbl27 | 17 Oct Hawks form 99.7 / 108, speed/defensive mechanisms, both teams' prominent players | Official Hawks article; direct-open cache miss, search-index content recovered |
| https://www.hawks.com.au/news/mason-peatling-injury-update-nbl27 | 9 Oct Peatling foot injury surgery, out season | Primary independent Hawks club release |
| https://www.hawks.com.au/statistics | Illawarra seven-game player stats | Hawks provider data, exact player minutes/selected bench not game-specific confirmation |
| https://www.basketball-reference.com/international/schedules/melbourne/2027.html | Melbourne 6 current dated score rows | Independent schedule compiler; direct-open cache miss but search text available |
| https://www.basketball-reference.com/international/schedules/illawarra/2027.html | Illawarra 7 current dated score rows | Independent schedule compiler |
| https://www.basketball-reference.com/international/schedules/melbourne/2026.html | Melbourne late 2025–26 regular-season dated score rows | Historical schedule, old player regime |
| https://www.basketball-reference.com/international/schedules/illawarra/2026.html | Illawarra late 2025–26 regular-season dated score rows | Historical schedule, old player regime |
| https://www.nbl.com.au/news/delany-leads-united-over-plucky-jackjumpers | 5 March Melbourne 82–68 Tasmania play-in | Official game report, corroboration for postseason row |
| https://www.nbl.com.au/news/second-half-blitz-sees-wildcats-advance | 7 March Melbourne 77–95 Perth play-in | Official game report, corroboration for postseason row |
| https://www.nbl.com.au/news/illawarra-hawks-justin-tatum-what-might-have-been-nbl26 | Hawks season ended 18 Feb, 13–20 record | Organizer historical club context |
| https://www.nbl.com.au/club-schedule/ill | Hawks matches; some entries stale/partial | Supplemental organizer dates and results; cross-check not exhaustive |
| `BASE_RATES_REGISTER.md` §7.1 / `PROBABILITY_TOOLKIT.md` §§1,4 at pinned SHA | Historical NBL level, widths, OT parameters, HE, k, normal Φ math | Internal released Markdown constants; validation/cross-season limitations as documented |

**Open field/attempt ledger:** (1) Confirm exact starters/bench from official pre-tip NBL match sheet: attempted organizer fixture and 18 Oct expected-depth preview, NOT_VERIFIED. (2) Injury/late changes: team releases + previews checked, final exact-match late recheck not independently closed. (3) Historical rows L20: two season schedules read through search-index records, original basketball-reference direct open cache miss, official individual-game cross-verification incomplete. (4) Pace/efficiency and current league mean: official pregame team/club commentary found, exact possessions and complete league season level NOT_VERIFIED. (5) Operator OT-inclusive spread/total action: user did not supply provider; UNKNOWN_DEFINITION. (6) Active writer and existing original: Drive active-mini folder inspected empty, GitHub directory list not available; original NOT_VERIFIED. (7) Actual 17:00 first-play marker not fetched because no live/outcome exposure was permitted; kickoff NOT_VERIFIED. Source-deficient fields are not falsely marked closed.

### A9. Completion, integrity, timing and delivery receipt

| Check | Result |
|---|---|
| Control authority | PASS pinned SHA and current relevant sections; not every entire long reference file read |
| Sport-specific steps 1–7 | Attempted with research, arithmetic and ranked supplied universe; true missing fields listed; INFORMATION_INCOMPLETE |
| Event identity | Correct participants, venue, day and NBL27 verified; native match ID not closed |
| Historic L5/L10/L15/L20 | All current+eligible prior rows printed with true n; independent per-row corroboration INCOMPLETE |
| Medical/absence field | Two club originals/league preview checked; material known absences verified; final starters/bench NOT_VERIFIED |
| Probabilities / C21 | Four supplied rows manually calculated from a single stated T/M centre with widths, complements verified; APPROXIMATE / UNCALIBRATED |
| Gate/rank and sensitivity | Base Rank 1/2 arithmetic pass; sensitivity instability disclosed |
| Venue, rules and conditional full-game endpoint | Venue/time confirmed; conditional NBL four-quarter/OT; operator action definition UNKNOWN |
| Pre-start issue / timing | **FAIL prospective pre-start issue**: research document after scheduled 17:00; actual first-play not verified; outcome information deliberately not accessed |
| ML/shadow | NOT_RUN / OUT_OF_SCOPE (current prompts 1–5 require no code) |
| Settlement and retrospective | NOT_PERFORMED (user explicit) |
| Canonical import | NOT_PERFORMED, no canonical ID assigned/reserved |
| Existing mini append / C16,C22 | BLOCKED: full active original and writer lease unavailable; self-contained downloadable **draft**, not verified cumulative update. Original bytes not invented/overwritten. |
| Result status | DRAFT_NOT_APPLIED / INFORMATION_INCOMPLETE / NOT_PERFORMANCE_ELIGIBLE |

SPORTS_ONLY_MARKET_BLIND: PASS · OUTCOME_EXPOSURE: no event score/result intentionally read; source publication-time uncertainty retained · SETTLEMENT: NOT_PERFORMED · CANONICAL_IMPORT: NOT_PERFORMED
<!-- END CANONICAL RESEARCH P-612 -->
