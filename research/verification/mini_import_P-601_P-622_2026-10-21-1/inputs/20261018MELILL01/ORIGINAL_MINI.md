<!-- MINI-LOG-FORMAT: mini-log-10 -->
<!-- DOCUMENT-STATUS: COMPLETE_STANDALONE_DRAFT_NOT_APPLIED_TO_EXISTING_ACTIVE_MINI -->
# Prediction Mini Running Log — 20261018MELILL01

> **Custody warning.** This is a complete, self-contained *proposed new mini*, NOT a verified update to any previously active mini and NOT an issued prospective pregame forecast. The existing active-original bytes/writer lease could not be verified. Save or import only after reconciling active-mini custody; do not overwrite another mini or treat the proposed local event key as an allocated canonical ID.

## A. Authority snapshot

| Field | Value |
|---|---|
| Authority mode | PUBLISHED_MAIN_PINNED; GitHub read-only |
| Repository / branch / read HEAD | `danisgreat/Sports-Research` / `main` / `3e29a58693e2ed02ff862e9bf0f751af2feadee1` |
| Working differences | Not observed; external-chat GitHub working tree inaccessible |
| Method / control / scoring / selection | MDS/P v22.2 / CR-2026.10.17-R6 / SCV-2026.10.16-v11 / SEL-2026.10.12-v3 |
| Active Combined Log | `prediction logs/PREDICTION_LOG_COMBINED_8.md` (read-only reference) |
| Highest committed / next canonical ID | P-600 / P-601, context only; reserved P-518–P-522 |
| Outstanding local minis and keys | An existing mini folder `2026101772F4B6FC9A` was located in the Google Drive `research/active_minis` mirror but contained no accessible file at inspection. GitHub `research/active_minis` directory exists, but directory inventory and unpublished originals could not be verified. Latest pinned GitHub `research/active_minis` inventory only contains `P-590_ONWARD`; Drive mirror dated 17 Oct empty. Other unpublished working originals/leases still UNKNOWN. |
| MINI_KEY / first provisional local key | `20261018MELILL01` / `LOCAL-20261018MELILL01-G0001` (DRAFT_ONLY; do not treat as issued) |
| New canonical ID / assignment stage | NOT_ASSIGNED / PROMPT_4_IMPORT |
| Writer / lease start / expiry | NO VERIFIED LEASE; standalone external-chat draft; start/expiry NOT_ESTABLISHED |
| Lease hand-over | NONE VERIFIED |
| Frozen for settlement | NO; draft not issued or frozen |
| Reading receipt / opened | GitHub `main` pinned at above SHA; read during 18 Oct 2026 AEDT: `CURRENT_STATE.md` (latest state), `METHOD.md` (current header), `CURRENT_RULES.md` (current header), `SELECTION_RULES.md` (selection gates), `CARD_AND_LOG_TEMPLATES.md` (§§2–3 and §3b), `research/prompts/README.md`, `research/prompts/COMMON_OPERATING_PROTOCOL.md` (§§1–4), `research/prompts/2_START_LOCAL_MINI.md`, `research/prompts/1_GAME_CARD.md` (shared steps), `research/prompts/1_sports/BASKETBALL.md` (steps 1–7), `research/prompts/1_sports/CRICKET.md` (steps 1–7), `RULES_CRICKET.md` (§0), `MINI_LOG_IDENTITY_PROTOCOL.md`, `EXECUTION_ENVIRONMENT_PROTOCOL.md`, `HISTORICAL_SOURCE_PROTOCOL.md` (opening), `ROSTER_AVAILABILITY_PROTOCOL.md` (search obligations), `RESEARCH_COMPLETION_PROTOCOL.md` (completion instructions), `PROBABILITY_TOOLKIT.md` (§§1,4,7,9,11), `BASE_RATES_REGISTER.md` (§7.1), `RULES_BASKETBALL.md` (§0), `GAME_LOG_STATUS_CURRENT.md` (current opening). Other cited large-file sections not fully read. |
| Mode | EXTERNAL_CHAT / LOCAL_MINI_STAGING; DRAFT_NOT_APPLIED |

SPORTS_ONLY / MARKET_BLIND · RESEARCH_ONLY_NOT_CERTIFIED · CANONICAL_IMPORT_STATUS: PENDING

## B. Local ID rules

A proposed draft local event key is used only for continuity inside this standalone copy. No canonical P-ID was allocated or reserved. Issued mini originals cannot be reconstructed from the Drive folder or an unverified GitHub directory. A valid writer must reconcile the original active mini and either authorize this new namespace or import the draft through the permitted workflow. Do not reissue the event after verification; use its confirmed native event identity for duplicate detection. No execution manifest, runtime, ML or RL was used.

## C. Carryover and evidence queue

| ID | Event key | Queue | Original card / frozen pick table | Latest revision | Open field | Responsible actor | Next source + exact field | Due (ISO, tz) | Final-time basis | Last attempt | Scheduled automation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Q01 | MEL–ILL 2026-10-18 | UNRESOLVED_EVIDENCE | Draft card below; NOT ISSUED | original draft | Confirmed starting fives/active bench and exact first-play time | Owner/researcher | Original NBL match-centre game sheet, team selection releases and first `jumpBall` | UNKNOWN | Actual first-play marker | Official NBL preview/depth-chart accessed; no confirmed five located | NO |
| Q02 | MEL–ILL 2026-10-18 | UNRESOLVED_EVIDENCE | Draft card below | original draft | Full independent source corroboration, ORtg/pace, current league mean and 2026-27 league comparator | Owner/researcher | NBL official team stats, exact-match advanced team possession/efficiency; cross-check historical rows | UNKNOWN | Pregame data availability, not final score | League + Basketball-Reference schedules and team previews searched | NO |
| Q03 | MINI identity | UNRESOLVED_EVIDENCE | Existing active original UNKNOWN | — | Active mini source bytes and exclusive writer lease | Owner/repository agent | Actual latest original in `research/active_minis/` and writer/lease/freeze evidence | UNKNOWN | Prior to custody hand-off | Drive mirror folder found empty; GitHub directory exists but contents not enumerated | NO |
| Q04 | PAK–SL Tri ODI 18 Oct | UNRESOLVED_EVIDENCE | Cricket draft card G0002, NOT ISSUED | original proposed draft | PCB official exact playing XIs, opener/new-ball roles and first-ball time | Owner/researcher | PCB/SLC scorecard selection tab with pre-first-ball publication times; official toss | UNKNOWN | Just before first ball; post-start sources not eligible unless field known-at proven | PCB squad and ICC conditional list consulted; no pre-start XI captured | NO |
| Q05 | PAK–SL Tri ODI 18 Oct | UNRESOLVED_EVIDENCE | Cricket draft card G0002 | original proposed draft | Five-over legal-ball rate and physical phase-to-innings transition model | Owner/researcher | Prior ODI ball-by-ball first five overs for both teams, date/role filters | UNKNOWN | Retrospective history known before event only | Series scorecards found, five-over paired source rows not verified | NO |
| Q06 | PAK–SL Tri ODI 18 Oct | UNRESOLVED_EVIDENCE | Cricket draft card G0002 | original proposed draft | Match operator void/DLS rules, league baseline, complete L20 independent corroboration | Owner/researcher | Named contract provider rules, PCB historical ball-by-ball and ground first-innings scorecards | UNKNOWN | Prior to issuing or settling, as applicable | Official historical fixtures and secondary series results reviewed, gaps retained | NO |

| Q07 | KP–Žabiny B 2026-10-18 | IDENTITY_CONFLICT | Proposed G0003 NOT ISSUED | new draft | User's KP Brno B is not federation's 18-Oct ŽBK KP Brno | Owner/researcher | Original supplier event ID compared with federation match 532124 and separate KP Brno B roster | UNKNOWN | Before actionable selection/import | Federation match and separate team entry opened | NO |
| Q08 | KP–Žabiny B 2026-10-18 | UNRESOLVED_EVIDENCE | Proposed G0003 NOT ISSUED | new draft | Exact starters/selected bench, medical and late rotation; 17-Oct recovery | Owner/researcher | Federation pre-tip lineups and independent team selection/injury reports | UNKNOWN | Publication timestamp before actual tip | League/team/club profiles searched; starting fives unconfirmed | NO |
| Q09 | KP–Žabiny B 2026-10-18 | UNRESOLVED_EVIDENCE | Proposed G0003 NOT ISSUED | new draft | 40 historical rows cross-confirmation, exact-competition league baseline, possessions/OT, operator contract rules | Owner/researcher | Federation/club historical match sheets, league-wide prior matches, operator full-game action | UNKNOWN | Pre-match known-at / contract settlement | 20+20 result rows and hand assumptions reviewed; independent corroboration incomplete | NO |
| Q10 | Beijing–Qingdao 2026-10-18 | UNRESOLVED_EVIDENCE | Proposed G0004 NOT ISSUED | new draft | Both current exact starting XIs, keepers and benches | Owner/researcher | Clubs official Oct18 lineup release and federated match sheet with pre-19:00 CST publication | UNKNOWN | Actual kickoff, not scheduled clock alone | Chinese and English pregame lineup sources queried; only prior XI verified | NO |
| Q11 | Beijing–Qingdao 2026-10-18 | UNRESOLVED_EVIDENCE | Proposed G0004 NOT ISSUED | new draft | Yang Liyu, Wu Shaocong and Qingdao Rezende/Peng exact current medical and suspension status | Owner/researcher | Club match-day eligibility and coach injury confirmation with actual known-at | UNKNOWN | Preissue verification time | 17-Oct Beijing press conference verified; old aggregator entries conflicted | NO |
| Q12 | Beijing–Qingdao 2026-10-18 | UNRESOLVED_EVIDENCE | Proposed G0004 NOT ISSUED | new draft | Exact competition frozen goals/first-half/corners baselines, independent corner variance, xG | Owner/researcher | CSL official match technical sheets and dated 2026 league event roster | UNKNOWN | Preissue cutoff | FBref/Scorestats/24score pregame aggregate records checked, no full cohort | NO |
| Q13 | Beijing–Qingdao 2026-10-18 | UNRESOLVED_EVIDENCE | Proposed G0004 NOT ISSUED | new draft | Operator 90-minute/abandonment rules, actual kickoff and issue, source provenance | Owner/researcher | Match federation native kickoff and contract provider rulebook | UNKNOWN | At actual start and first published issue | Official 19:00 CST scheduled start verified; exact start and bookmaker identity unverified | NO |

## D. Request intake

| Request key | Received (ISO, tz) | Event / alias as requested | Disposition | Pointer |
|---|---|---|---|---|
| REQ-20261018-MELILL | BEFORE_2026-10-18T17:00:00+11:00 (exact request receipt timestamp NOT_CAPTURED) | Melbourne United vs Illawarra Hawks, Australia NBL, Sunday 18 October 2026, 17:00 AEDT; four supplied contracts | READ_ONLY_DRAFT | Proposed `LOCAL-20261018MELILL01-G0001`; original active-mini custody and lease unverified |
| REQ-20261018-PAKSL | BEFORE_2026-10-18T19:00:00+11:00 (request receipt exact timestamp NOT_CAPTURED) | Pakistan vs Sri Lanka, ODI tri-series match 1, 18 Oct 2026 19:00 AEDT; first-innings Pakistan Over/Under 311.5, first five overs Over/Under 26.5 | READ_ONLY_DRAFT | Proposed `LOCAL-20261018MELILL01-G0002`, after scheduled start; pre-result research, active-mini and lease not verified |

| REQ-20261018-KPZAB | BEFORE_2026-10-18T20:15:00+11:00 (request receipt exact timestamp NOT_CAPTURED) | User: KP Brno B (W) vs Zabiny Brno B (W), Czechia 1. liga Women, 18-Oct 20:15 AEDT, KP +4.0, Zabiny −4.0, Under/Over 139.5; federation match is ŽBK KP Brno (not KP Brno B) vs Žabiny B | READ_ONLY_DRAFT_IDENTITY_CONFLICT | Proposed `LOCAL-20261018MELILL01-G0003`; CONDITIONAL on official ŽBK KP Brno identity; operator match unresolved, no lease |
| REQ-20261018-BEI-QWC | BEFORE_2026-10-18T22:00:00+11:00 (exact receipt timestamp NOT_CAPTURED; observed ~21:39 AEDT) | Beijing Guoan vs Qingdao West Coast, CSL, 18-Oct 22:00 AEDT, O/U 0.5 first-half goals, O/U 2.5 full-time goals, O/U 10.5 combined corners; winner and lineup research; no retrospective | READ_ONLY_UNISSUED_DRAFT | Proposed LOCAL-20261018MELILL01-G0004; no original active mini/writer lease; first-half family restriction, source gaps open |

# NEW LOCAL EVENT CARDS

<!-- BEGIN CARD LOCAL-20261018MELILL01-G0001 -->
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
<!-- END CARD LOCAL-20261018MELILL01-G0001 -->

<!-- BEGIN CARD LOCAL-20261018MELILL01-G0002 -->
## Card · LOCAL-20261018MELILL01-G0002 · CRICKET / Pakistan ODI Tri-Series · Pakistan vs Sri Lanka · 2026-10-18

### Owner-entered upcoming-game request (exact supplied contracts retained)

> Upcoming Cricket Game: Pakistan vs Sri Lanka, Tri-Nations ODI  
> Estimated Game Time Start: 18 October 2026, 7:00 PM AEDT (can be delayed so continue the process as normal)  
> Pakistan 1st Innings Runs at end of 50 overs Total: Over/Under 311.5 Runs  
> Pakistan 1st Innings Runs at the end of 5 overs: Over/Under 26.5 Runs  
> Research comprehensively using the latest GitHub main and verified official/public sources, including confirmed playing XI and injuries, four ranked contracts, winner, reasons and sources. No retrospective, score exposure, canonical import or settlement.

### Record metadata and authority

| Field | Status / evidence |
|---|---|
| Local event key | `LOCAL-20261018MELILL01-G0002` **PROVISIONAL COPY ONLY**; only use after duplicate/custody checks; native event surrogate `PCB-TRIODI-20261018-PAK-SL-M1`, official PCB tournament match number 1; ICC match page `/matches/274142/pakistan-vs-sri-lanka` |
| Canonical identifier | `NOT_ASSIGNED`; assigned only at verified PROMPT_4_IMPORT; no P-ID reserved |
| Authority | `PUBLISHED_MAIN_PINNED`, `danisgreat/Sports-Research`, commit `3e29a58693e2ed02ff862e9bf0f751af2feadee1`; `MDS/P v22.2` / `CR-2026.10.17-R6` / `SEL-2026.10.12-v3` / `SCV-v11` |
| References read | `research/prompts/1_GAME_CARD.md` shared steps; `research/prompts/1_sports/CRICKET.md` all seven steps; `RULES_CRICKET.md` §0; `PROBABILITY_TOOLKIT.md` §§1,7,9,11; `SELECTION_RULES.md` §§1–4; `BASE_RATES_REGISTER.md` cricket availability; preceding turn: `CURRENT_STATE`, `METHOD`, `CURRENT_RULES`, `CARD_AND_LOG_TEMPLATES`, `MINI_LOG_IDENTITY_PROTOCOL`, `HISTORICAL_SOURCE_PROTOCOL`, `ROSTER_AVAILABILITY_PROTOCOL`, `RESEARCH_COMPLETION_PROTOCOL`, `GAME_LOG_STATUS_CURRENT`; some entire long references not fully reread |
| Intended format | Men's one-day international, each side up to 50 overs, two white balls, 10-over initial powerplay, bowlers max 10 overs absent reduction; 5-over phase = after 30 legal balls, subject to early all-out/abandonment |
| Match/venue | PCB Pakistan–England–Sri Lanka men's ODI tri-series, match 1; Rawalpindi Cricket Stadium, Rawalpindi, Pakistan; 2026-10-18 13:00 PKT (+05:00) / 08:00 UTC / 19:00 AEDT (+11:00) |
| Toss | **Sri Lanka won and chose to bowl; Pakistan bats first**; current pre-start report https://www.thenews.pk/story/1443659-sri-lanka-win-toss-elect-to-bowl-first-against-pakistan-in-tri-nation-series-opener (18 October 2026). Not independently corroborated from a timestamped official scorecard; `SECONDARY_CONFIRMED/PRIMARY_UNVERIFIED` |
| Research/issue timing | Completed after scheduled start (19:00 AEDT); research session check after 19:06 AEDT. `POST_START_ISSUE` / `NOT_PROSPECTIVE_PRESTART`. Actual ball-one time not independently verified. No in-play or final score read for inference; sourced pre-start lineups/toss evaluated only when publication timing is explicit. Any source unverified before first ball is `KNOWN_AT_UNVERIFIED` |
| Model scope | `ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY`, hand-derived normal-mixture approximation, not trained/calibrated ML. No code/model/RL, no external prediction, odds, tips, implied market probabilities or bookmaker sources |
| Contract endpoint | Pakistan's **first innings** (it bats first). Innings ends at 50 overs or dismissal; a total beyond 311.5 can be reached before 50 overs. Five-over endpoint = runs after exactly five completed overs, when reached. No score substituted from a chase. Provider-specific reduced-overs/void rules UNVERIFIED |
| Weather | Pre-start Rawalpindi hazy sun forecast, roughly 1% rain probability from available daily forecast, but no live meteorological guarantee; exact surface `STRIP_UNCONFIRMED` |
| Performance | Research-only; NOT_PERFORMANCE_ELIGIBLE; INFORMATION_INCOMPLETE because official XI/phase inputs, operator settlement and full independent history corroboration not closed |
| Source state | Scores from previous dates only; match's live score/result/outcome NOT_USED; no retrospective or settlement |

### Decision block — four supplied propositions

| Rank | Role | Supplied exact contract | p_card | p_base | BASELINE_P | P(win)/P(loss)/P(push)/P(void)* | Signed line distance / z | Main failure mechanism |
|---:|---|---|---:|---:|---|---|---|---|
| 1 | PICK | **Pakistan first innings Under 311.5 runs, up to 50 overs** | **0.732** | 0.740 | `BASELINE_UNAVAILABLE: exact ODI first-innings cohort/window not verified` | .732/.268/0/0 | 311.5−277.75=+33.75; z_base=.644 | Pakistan's top order remains intact; unusually fast scoring, favourable pitch, SL attack absence |
| 2 | PICK | **Pakistan first innings Over 26.5 runs after 5 completed overs** | **0.606** | 0.608 | `BASELINE_UNAVAILABLE: verified 5-over field-owner history lacking` | .606/.394/0/0 | 26.5−29.5=−3.0; z_base=−.273 | Early wicket(s), powerplay swing/seam, opener dot-ball cluster |
| 3 | INFORMATIONAL | Pakistan first innings Under 26.5 runs after 5 completed overs | 0.394 | 0.392 | BASELINE_UNAVAILABLE | .394/.606/0/0 | +3.0 runs from 5-over mean | Fast first five overs, boundaries/extras |
| 4 | INFORMATIONAL | Pakistan first innings Over 311.5 runs, up to 50 overs | 0.268 | 0.260 | BASELINE_UNAVAILABLE | .268/.732/0/0 | +33.75 runs above projected full mean | Middle-order slowdown, wickets, 300-level ceiling |

\* `W/L/P/V` are conditional on two decisive, normally completed innings/phase endpoints and operator rules treating each half-run line as a two-way contract. These are **not unconditional no-result/void-inclusive masses**, because the user's operator was not provided. No in-play status or outcome has been used to grade them.

**Rank-1 gate:** p≈0.732 ≥ 0.62; next eligible non-complementary p≈0.606; lead≈0.126 ≥ 0.04; `PASS_BASE_SCENARIO`, ε≥0.002 for Φ-table precision and materially greater structural uncertainty. High-scoring sensitivity changes the order; `SCENARIO_UNSTABLE`, not a robust performance claim. **Rank-2 floor:** p≈0.606 ≥ 0.58 (`PASS_BASE`, yet not calibrated). Only two picks; the remaining two are complement rows. All four supplied rows printed without threshold shopping or invented replacement lines.

**Potential outright winner:** **Pakistan, conditional estimate approximately 0.60** (Sri Lanka approximately 0.40, excluding tie/no-result/DLS ambiguity). This is a separate, low-confidence analyst judgement from home venue, 2025 home ODI head-to-head and squads, **NOT** output from the quantified first-innings distribution, and not a calibrated win probability. Winner endpoint/tie/no-result shares NOT_COMPUTED; therefore the full three-/four-way winning state is INCOMPLETE. Confidence is lower than a 60% label may suggest.

**Decision rationale:** Pakistan's historical last-20 ODI innings averaged 237.5, but this includes shortened successful chases; this does not imply a 237.5 batting-first expectation. Sri Lanka conceded 282.2 per game across its last ten ODIs, while Pakistan posted 299/5 batting first against Sri Lanka in Rawalpindi in Nov 2025. The 311.5 total is above the conditional first-innings centre of 277.75 by 33.75. In contrast, Pakistan clearing 26.5 in five overs is a small cushion above the expected first-five run centre 29.5 and is sensitive to the unconfirmed opening batters/new-ball attack and actual strip. Both selected rows can lose together: a very slow opening followed by a later high score or a very fast opening coupled with below-312 finish has different consequences; their precise joint dependence is NOT estimated.

### A1. Fixture, temporal identity, format, toss and existing-record checks

- PCB official tournament fixture https://www.pcb.com.pk/tournament-reports.php?action=tournament_matches&sort_by=date_start&sort_order=desc&tournament_id=1465 lists 18 Oct match 1 at Rawalpindi. ECB corroboration https://www.ecb.co.uk/news/4562387/pakistan-to-host-sri-lanka-and-england-in-odi-triseries . PCB pregame announcement https://www.pcb.com.pk/press-release-detail/pakistan-england-sri-lanka-set-to-begin-preparations-for-odi-world-cup-with-tri-series-from-18-to-31.html confirms 13:00 PKT start / 12:30 PKT toss.
- Exact user contracts are Pakistan batting-first full 50-over total and first 5 overs, not Pakistan's second innings, not Sri Lanka's innings, not the match total, and not a T20 powerplay.
- Reported toss Sri Lanka field first as linked in metadata. Official match sheet, XI/bench and precise first ball time were not independently verified at research issue. Do not backdate a pre-start release because user submitted earlier.
- Existing combined canonical register latest pinned: P-600 highest, P-601 next; read-only contextual information; no claimed direct GitHub append. An extant active mini and exclusive writer lease are unverified. The prior MEL–ILL full MD is an **unissued draft**, not a verified active mini; this card's key is a **provisional continuation for the supplied cumulative draft copy**, not a reservation against other minis. Duplicates must be reconciled by the repository owner.
- No separate ODI match of these opponents on this date confused with Pakistan's preceding Oct 9–13 Sri Lanka T20Is or Nov 2025 three-ODI series.

### A2. Freeze the four user supplied lines and rules

| Contract key | Team | Period | Exact line | Action definition | Uncertainty |
|---|---|---|---|---|---|
| PAK_RUNS_INN1_50_O3115 / U3115 | Pakistan batting first | Innings 1, maximum 50 overs | 311.5 | Over ≥312; Under ≤311 in a completed, 50-over-scheduled innings | No specific operator void/reduction convention provided; team may be all out earlier |
| PAK_RUNS_INN1_05_O265 / U265 | Pakistan batting first | Total at 5.0 overs (30 legal balls) | 26.5 | Over ≥27; Under ≤26 | Can cease before 5 overs if all out/abandoned; operator's action not verified |

These two pairs are `FORCED_PAIR` complement relationships under a fully decisive endpoint; they cannot be four independent suggestions or combined for an artificial Hit@2. No price/odds supplied and no financial expected value computed. ODI powerplay lasts 10 overs; this five-over line is **not** the full powerplay.

### A3. Squad/selection, injury, bowlers and prior game history

**Pakistan (PCB announced 16-player ODI squad):** Shaheen Shah Afridi (captain), Abrar Ahmed, Salman Ali Agha, Arafat Minhas, Babar Azam, Faheem Ashraf, Fakhar Zaman, Muhammad Ghazi Ghori (wk), Haris Rauf, Hasan Nawaz, Naseem Shah, Razaullah, Saad Baig (wk), Saim Ayub, Shadab Khan, Sufiyan Moqim. Official source (5 Oct) https://www.pcb.com.pk/press-release-detail/pakistan-squads-announced-for-sri-lanka-t20is-and-odi-tri-series.html ; squad training confirmed PCB 15 Oct https://www.pcb.com.pk/press-release-detail/pakistan-odi-squad-begins-preparations-for-tri-series.html . Mohammad Rizwan is **not** in this ODI squad. Sahibzada Farhan and Maaz Sadaqat were on T20 duty, not the named ODI squad; do not transfer their T20 5-over scores to this ODI XI. **Confirmed openers, Nos. 3–4, wicketkeeper selection, actual bat-first batting order: NOT_VERIFIED**. Expected opener candidates Saim Ayub and Fakhar Zaman are projections, not an exact XI.

**Sri Lanka (ICC 4 Oct original conditional squad):** Kusal Mendis (capt/wk), Sahan Arachchige, Dushmantha Chameera, Sachindu Colombage, Avishka Fernando, Asitha Fernando, Janith Liyanage, Dilshan Madushanka, Eshan Malinga, Kamindu Mendis, Kamil Mishara, Pathum Nissanka (subject to medical clearance), Pavan Rathnayake, Dasun Shanaka, Maheesh Theekshana, Dunith Wellalage: https://www.icc-cricket.com/news/sri-lanka-unveil-odi-squad-for-tri-series-in-pakistan . **Revision (16 Oct)**: Pathum Nissanka ruled out by hamstring injury after no medical clearance; Lahiru Udara called in, reported by https://www.thenews.pk/print/1443109-nissanka-ruled-out-of-tri-series-as-pakistan-sl-step-up-preparations . **Wanindu Hasaranga injured/unavailable**; Sahan Arachchige is named among the replacement squad, reported https://www.wisden.com/series/pakistan-odi-tri-series-2026/cricket-news/pakistan-tri-series-2026-all-you-need-to-know-full-schedule-squads-venues-and-match-timings-for-the-odi-tri-series . Do not assume Nissanka played or Wasaranga bowled, and do not confuse a named squad with a final selected XI. **Confirmed Sri Lanka new-ball bowling pair, XI and bench: NOT_VERIFIED**.

**Conditional roster effects:** A missing Sri Lankan attacking spin option (Hasaranga) can affect middle-overs wickets/ceiling; size NOT_QUANTIFIED without opponent-adjusted role data. Nissanka's absence affects Sri Lanka's chase-strength/possible winner, **not Pakistan's first five overs batting directly**. Pakistan keeper/top-order selections could change batting depth; no fake run adjustments were applied. Player-specific current ODI balls faced, first-five strike rates and bowler five-over economy not verified, so not used as numerical evidence. No official exact-match medical clearances or final late XI announcement confirmed; `LINEUP_UNCONFIRMED` / `INFORMATION_INCOMPLETE`.

**Pakistan men's ODI results, most recent 20 eligible completed games (scores from Pakistan perspective; batting first / chase and reduced innings distinguished).** Series results cross-referenced through historical PCB/ICC/ESPN scorecards and Wisden series records (see A8), but NOT every row independently opened and double-verified; `ROW_CORROBORATION_OPEN`.

| Date | Opponent | Pakistan runs (overs) | Opponent runs (overs) | Pakistan innings role / context |
|---|---|---|---|---|
| 2026-06-04 | Australia | 161/6 (41.5) | 157 all out (42.0) | Chase ended early |
| 2026-06-02 | Australia | 190 all out (44.0) | 231/9 (50.0) | Chase, all out |
| 2026-05-30 | Australia | 202/5 (42.3) | 200 all out (44.1) | Chase ended early, Rawalpindi |
| 2026-03-15 | Bangladesh | 279 all out (50.0) | 290/5 (50.0) | Chase |
| 2026-03-13 | Bangladesh | 274 all out (47.3) | 114 all out (23.3) | Bat first; DLS-result context |
| 2026-03-11 | Bangladesh | 114 all out (30.4) | 115/2 (15.1) | Bat first |
| 2025-11-16 | Sri Lanka | 215/4 (44.4) | 211 all out (45.2) | Chase ended early, Rawalpindi |
| 2025-11-14 | Sri Lanka | 289/2 (48.2) | 288/8 (50.0) | Chase ended early, Rawalpindi |
| 2025-11-11 | Sri Lanka | 299/5 (50.0) | 293/9 (50.0) | Bat first, Rawalpindi |
| 2025-11-08 | South Africa | 144/3 (25.1) | 143 all out (37.5) | Chase ended early |
| 2025-11-06 | South Africa | 269/9 (50.0) | 270/2 (40.1) | Bat first |
| 2025-11-04 | South Africa | 264/8 (49.4) | 263 all out (49.1) | Chase ended early |
| 2025-04-05 | New Zealand | 221 all out (40.0) | 264/8 (42.0) | Bat in rain-shortened 42-over ODI; not full 50 |
| 2025-04-02 | New Zealand | 208 all out (41.2) | 292/8 (50.0) | Chase |
| 2025-03-29 | New Zealand | 271 all out (44.1) | 344/9 (50.0) | Chase |
| 2025-02-23 | India | 241 all out (49.4) | 244/4 | Bat first |
| 2025-02-19 | New Zealand | 260 all out (47.2) | 320/5 | Chase |
| 2025-02-14 | New Zealand | 242 all out (49.3) | 243/5 | Bat first |
| 2025-02-12 | South Africa | 355/4 (49.0) | 352/5 (50.0) | Chase ended at victory, overshoot allowed |
| 2025-02-08 | New Zealand | 252 all out (47.5) | 330/6 | Chase |

**Sri Lanka men's ODI results, most recent 20 eligible completed games (scores from Sri Lanka perspective):**

| Date | Opponent | Sri Lanka runs (overs) | Opponent runs (overs) | Context |
|---|---|---|---|---|
| 2026-09-27 | England | 132 all out (29.1) | 355/7 (50.0) | Chase |
| 2026-09-24 | England | 321/6 (50.0) | 305/9 (50.0) | Bat first |
| 2026-09-22 | England | 176 all out (37.0) | 265 (48.1) | Chase |
| 2026-06-03 | West Indies | 303/7 (50.0) | 262 (49.2) | Bat first |
| 2026-01-27 | England | 304 (46.4) | 357/3 (50.0) | Chase |
| 2026-01-24 | England | 219 (49.3) | 223/5 (46.2) | Bat first |
| 2026-01-22 | England | 271/6 (50.0) | 252 (49.2) | Bat first |
| 2025-11-16 | Pakistan | 211 (45.2) | 215/4 (44.4) | Bat first, Rawalpindi |
| 2025-11-14 | Pakistan | 288/8 (50.0) | 289/2 (48.2) | Bat first, Rawalpindi |
| 2025-11-11 | Pakistan | 293/9 (50.0) | 299/5 (50.0) | Chase, Rawalpindi |
| 2025-08-31 | Zimbabwe | 278/5 (49.3) | 277/7 (50.0) | Chase ended at victory |
| 2025-08-29 | Zimbabwe | 298/6 (50.0) | 291/8 (50.0) | Bat first |
| 2025-07-08 | Bangladesh | 285/7 (50.0) | 186 (39.4) | Bat first |
| 2025-07-05 | Bangladesh | 232 (48.5) | 248 (50.0) | Chase |
| 2025-07-02 | Bangladesh | 244 all out | 167 all out | Bat first; exact overs not confirmed |
| 2025-02-14 | Australia | 281/4 (50.0) | 107 (24.2) | Bat first |
| 2025-02-12 | Australia | 214 all out (46.0) | 165 (33.5) | Bat first |
| 2025-01-11 | New Zealand | 290/8 (50.0) | 150 (29.4) | Bat first |
| 2025-01-08 | New Zealand | 142 all out (30.2) | 255/9 (37.0) | Chase in reduced-overs ODI |
| 2025-01-05 | New Zealand | 178 all out (43.4) | 180/1 (26.2) | Bat first |

**Compiled form aggregates; individual underlying score rows still require independent corroboration** (overlapping windows count once; simple completed-score mean is NOT a full-50-over mean):

| Side | Window | true n | Scored / match | Conceded / match | Mean signed run difference | Coverage and limitation |
|---|---|---:|---:|---:|---:|---|
| Pakistan | L5 | 5 | 221.2 | 198.4 | +22.8 | 2026-03-13 to 2026-06-04; multiple completed chases |
| Pakistan | L10 | 10 | 216.7 | 204.2 | +12.5 | 2025-11-08 to 2026-06-04 |
| Pakistan | L15 | 15 | 226.7 | 231.7 | −5.0 | 2025-03-29 to 2026-06-04 |
| Pakistan | L20 | 20 | 237.5 | 248.2 | −10.7 | 2025-02-08 to 2026-06-04; includes reduced-overs game |
| Sri Lanka | L5 | 5 | 247.2 | 308.8 | −61.6 | 2026-01-27 to 2026-09-27 |
| Sri Lanka | L10 | 10 | 251.8 | 282.2 | −30.4 | 2025-11-11 to 2026-09-27 |
| Sri Lanka | L15 | 15 | 257.0 | 266.1 | −9.1 | 2025-07-02 to 2026-09-27 |
| Sri Lanka | L20 | 20 | 248.0 | 242.4 | +5.6 | 2025-01-05 to 2026-09-27; includes reduced-overs game |

- Cricket format: international men's ODIs only, completed official matches; abandoned/washout games excluded. Date of latest eligible historical fixture 27 Sep (SL), 4 Jun (PAK). Recent ODI sample small and time-stale for PAK; roster changes mean past teams not identical.
- Season-to-date: no natural common ODI league season; tournament has no prior games (`n=0`); cricket ODI rolling form windows used instead. League/venue level: Cricbuzz Rawalpindi all-time first-innings ODI mean reported **242 across 31 matches**, mixture of eras/teams; `STALE_VENUE_REGIME`, not a current-season fitted baseline. No `BASELINE_LEAGUE_V1` with verified matching 2026 batting-first first-five cohort available. Do not present 242 as 2026-specific.
- **R2 window blend for comparison:** `WEIGHTS/RECIPE_NOT_FULLY_REPRODUCED` because overlapping windows cannot be independent fitted sample rates and the current true global ODI baseline/strength-adjusted opposition schedule is missing. No invented k or derived adjusted team strengths; manual scenario-centres below are exposed judgement rather than falsely labelled R2 output. Pakistan raw L20 237.5 is not automatically an expected 50-over innings, because many innings stopped when targets were reached. Season league means, strengths and exact 5-over distributions remain MISSING.
- Historical sources and independent verification attempts are in A8. Abandoned matches, 2026 recent T20s and game-day ODI outcomes are excluded from scoring windows. Rows with exact innings overs unclear are labelled rather than manufactured. **Windows overlap; counted once.**

### A4. Conditional distribution, arithmetic, expected score and sensitivity

**Why no exact ball-by-ball model:** No verified pre-first-ball live official XI, top-four ordering, new-ball pairing, recent five-over scores with legal-ball deliveries, or pitch strip data. No historical verified venue/phase residual variance estimate. Therefore the below is a transparent, **subjective analyst approximation** with uncertain inputs, not a calibrated fit, bootstrap or true derived innings/wicket transition grid. Model widths are assumptions; the missing inputs prevent objective accuracy assessment.

**Full first-innings runs:** one conditional three-component **normal approximation** for completed 50-over-scheduled innings including all-out termination in the historical dispersion; scenario weights low/base/high = 0.25 / 0.50 / 0.25, centres μ = 255 / 278 / 300 runs, common assumed SD = 52.0 runs. Rationale: blended manually from Pakistan's recent completed innings including a 299/5 first-innings ODI versus this opponent at the venue, Sri Lanka's recent L10 conceded 282.2, historical venue mean 242; scenario range for pitch/XI uncertainty. Does **not** assert a measured 52-run residual or mathematically explicit 10-wicket state: this remains the main structural limitation. Mean = .25×255 + .50×278 + .25×300 = **277.75 runs**; width ~54.4 after between-scenario spread, not a calibrated confidence interval.

\[
P(U311.5)=\sum_{j\in\{L,B,H\}}w_j\,\Phi((311.5-\mu_j)/52)
\]

- LOW z=(311.5−255)/52=1.087; Φ≈0.861; contribution .25×.861=.2153.
- BASE z=(311.5−278)/52=0.644; Φ≈0.740; contribution .50×.740=.3700.
- HIGH z=(311.5−300)/52=0.221; Φ≈0.588; contribution .25×.588=.1470.
- **Under 311.5** ≈ .2153+.3700+.1470=**0.7323**; **Over 311.5** ≈ 1−.7323=**0.2677**. Φ interpolation ε≈.002; additional model/parameter uncertainty much larger. Half-line yields no push if the innings contract is decisive.

**Pakistan first 5 completed overs:** separate conditional three-component normal **marginal approximation**, scenario weights 0.25/0.50/0.25, centres μ_5 = 27 / 29.5 / 32 runs, common **assumed** SD=11 runs; arbitrary judgement informed by plausible early ODI scoring, **not** derived from a verified opening-30-ball sample. This quantity is intrinsically integer and nonnegative; Gaussian tail below zero is a small unnormalised approximation (base Φ(−29.5/11) about 0.004), disclosed as such. No direct link to wickets modelled. Mean=29.5 runs.

- LOW z=(27−26.5)/11=.045; P(Over26.5)=Φ(.045)≈.518; weighted .25×.518=.1295.
- BASE z=(29.5−26.5)/11=.273; P(Over26.5)=Φ(.273)≈.608; weighted .50×.608=.3040.
- HIGH z=(32−26.5)/11=.500; P(Over26.5)=Φ(.5)≈.6915; weighted .25×.6915=.1729.
- **Over 26.5** ≈ .1295+.3040+.1729=**0.6064**; **Under 26.5** ≈ **0.3936**. Rounding to three decimals: .606 and .394.

**Scenario probabilities (not 95% confidence bounds):**

| Scenario / assumption | Under 311.5 | Over 26.5 | Consequence |
|---|---:|---:|---|
| Low: 255-run innings / 27 after five | 0.861 | 0.518 | Under stronger, first-five Over no longer rank-2-floor eligible |
| Base: 278-run innings / 29.5 after five | 0.740 | 0.608 | Both directions favoured |
| High: 300-run innings / 32 after five | 0.588 | 0.692 | Over five becomes Rank 1, total Under falls below Rank-1 threshold |
| Weighted primary | **0.732** | **0.606** | Scenario-dependent rankings; don't claim robust gate |

**Score/wickets expected object:** Pakistan first-innings runs 277.75, conditional full-overs-scheduled; projected five-over runs 29.5, SD 11 assumed. Wickets lost at five overs, total wickets/expected overs remaining, Sri Lanka response, run covariance, win margin and no-result probability **NOT_COMPUTED**; no falsely precise 50-over team v team score projected. The two marginal approximations don't constitute a physical monotone ball-by-ball shared grid; P(5-over result, 50-over result) joint is **unquantified**.

**Joint failure bounds, selected Rank 1 Under311.5 and Rank 2 Over26.5:** losses are innings Over311.5 p≈.268 and first-five Under26.5 p≈.394. Without a verified joint phase→innings model, Fréchet: `max(0,.268+.394−1)=0 ≤ P(both lose) ≤ min(.268,.394)=.268`. Historical diagnostic threshold 0.30/0.35 is not crossed at upper bound under these assumed marginals, but the true joint not estimated, and parameter uncertainty is omitted. Do **not** multiply as if independent.

**Baseline and EV:** Venue first-innings historical mean 242 with n=31 is contextual only, unverified source-date cutoff and mismatched competition-era; a valid matching league-only BASELINE_P is not reproducible. Five-over baseline unavailable. No market odds or stake conditions supplied; monetary EV cannot be computed and market odds are excluded under SPORTS_ONLY. Probabilities above are *not* price edges or validated advantages. `TEAM_BASELINE_P: NOT_COVERED_FOR_CRICKET`.

### A5. Full supplied candidate universe and exact complements

| Distinct quantity | Line | Side | Approximate p_card | p(loss) | Decision |
|---|---:|---|---:|---:|---|
| Pakistan bat-first innings runs | 311.5 | Under | .732 | .268 | Rank 1; selected |
| Pakistan after 5.0 overs runs | 26.5 | Over | .606 | .394 | Rank 2; selected |
| Pakistan after 5.0 overs runs | 26.5 | Under | .394 | .606 | Informational direct opposite |
| Pakistan bat-first innings runs | 311.5 | Over | .268 | .732 | Informational direct opposite |

No additional analyst-derived thresholds manufactured. Complement arithmetic `.732+.268=1.000`, `.606+.394=1.000`. No exact conditional pair correlation computed. A no-result or five-over-shortened match may trigger operator-specific void, not modelled as zero in unconditional probability.

### A6. Pitch, availability, toss, weather, conditions and alternatives

| Material input | Observed pre-start evidence | Applied effect / honest limit |
|---|---|---|
| Pakistan innings role | Sri Lanka chose to field, current 18 Oct source | Bat-first scenario only; no chase-target censoring for Pakistan's first innings |
| Current pitch strip | No independent official strip report verified | Three centres 255/278/300; cannot assert hard/flat/green pitch or seam swing |
| Historical venue | Previous Pakistan 299/5 vs Sri Lanka Nov 2025; venue compiled ODI mean ~242/31 | Old-game context, not first-five-phase rate nor current strip |
| Sri Lanka Hasaranga absence | Injured, squad change reported before match | Could weaken spin wicket containment in overs 11–40; *no numerical adjustment fitted* |
| Sri Lanka Nissanka absence | Hamstring injury, replacement Lahiru Udara (16 Oct) | Lowers/changes potential Sri Lanka batting side, not directly Pakistan first-innings run total |
| Pakistan top-order selection | ODI squad Babar, Fakhar, Saim, Salman; XI unverified | Unconfirmed opener composition; principal early-5-overs sensitivity |
| Sri Lanka new-ball pair | Chameera/Asitha Fernando/Madushanka/Malinga in squad; XI and allocations unverified | Critical uncertainty for Over26.5, no invented bowler economy |
| Weather/DLS | Pre-match forecast low rain risk; official rain/wet outfield not checked | Full 50-overs assumed; reduced innings case and void conventions unresolved |
| Recent T20Is at venue | 9–13 Oct 2026 Pakistan v Sri Lanka T20 series; separate teams/squads | Not pooled with ODI phase/innings distributions |
| Rest | ODI squads prepared at venue 15–17 Oct; SL some players had T20 series | No unverified fatigue-based expected-run adjustment |

Base figures are centre assumptions, not inferred numerical causal effects. Unadjusted counterfactual absent a fully fitted dataset is `NOT_COMPUTED`; label sensitivity `SCENARIO_UNSTABLE`. Any player-specific confirmed absence effect cannot be isolated with present data.

### A7. Statistical controls, comparisons and gates

- `P_ORDER_V2`: only four exact supplied directions priced; ranked by p_card; rank 1 and 2 are primary picks, 3 and 4 informational; no q tiers.
- **Rank-1 numerical gate:** PASS on chosen manual mixture at p .732, best independent alternative p .606, lead .126; in high-run scenario it fails for Under 311.5 and row order changes; `ADJUSTMENT_DEPENDENT/SCENARIO_UNSTABLE`.
- **Rank-2 floor:** PASS base at .606 but LOW scenario .518 fails. No extra confidence attributed to provider line or toss alone.
- `RET03` shadow gate (exclude same innings quantity as Rank 1): Over26.5, .606, lead .126, PASS_BASE. `RET04` alternate different quantity: same Over26.5; NOT_PRIMARY. `XCARD6` exact-joint failure optimization: NOT_COMPUTED, Fréchet interval only. `RANK_DELTA`: NONE because no frozen league-only comparator. `BASE_ONLY`: Under311.5 .740, Over26.5 .608; same rank1/2.
- `PRECISION ε`: .002 per Φ reading from official repo normal table, but true epistemic error from unvalidated μ, σ and missing innings/phase physical transition parameters is far larger; ε is not an accuracy uncertainty bound.
- `SAME-QUANTITY`: Over/Under at each threshold forced complements; no dummy Hit@2 credit, no pushes for half-run lines under a decisive endpoint.
- `PERFORMANCE_ELIGIBLE`: NO. Previous ODI examples are sourcing and contextual form, not an out-of-sample evaluation of this method.

### A8. Source registry, exact fields, attempts, unfinished corroboration

The following are the specific research routes that informed this card. Publication/retrieval precise ISO timestamps were not exposed for every item; source-known-before-first-ball remains unverified when not date-stamped. Every game row needs point-in-time official box-score and independently collected second lineage before this evidence set can be marked complete.

| Source / original URL | Relevance; field and limitations |
|---|---|
| https://www.pcb.com.pk/press-release-detail/pakistan-england-sri-lanka-set-to-begin-preparations-for-odi-world-cup-with-tri-series-from-18-to-31.html | PCB 17 Oct match time (13:00 PKT), scheduled toss (12:30 PKT), tri-series |
| https://www.pcb.com.pk/tournament-reports.php?action=tournament_matches&sort_by=date_start&sort_order=desc&tournament_id=1465 | PCB organizer tournament match 1, date, venue |
| https://www.ecb.co.uk/news/4562387/pakistan-to-host-sri-lanka-and-england-in-odi-triseries | ECB independently corroborates teams/fixture/venue/date |
| https://www.thenews.pk/story/1443659-sri-lanka-win-toss-elect-to-bowl-first-against-pakistan-in-tri-nation-series-opener | 18 Oct toss Sri Lanka bowl first; one reporting lineage, official feed corroboration pending |
| https://www.pcb.com.pk/press-release-detail/pakistan-squads-announced-for-sri-lanka-t20is-and-odi-tri-series.html | PCB 5 Oct exact Pakistan 16-player ODI squad vs separately named T20 squad |
| https://www.pcb.com.pk/press-release-detail/pakistan-odi-squad-begins-preparations-for-tri-series.html | PCB 15 Oct training participants and role groups |
| https://www.icc-cricket.com/news/sri-lanka-unveil-odi-squad-for-tri-series-in-pakistan | ICC SLC 4 Oct 16-player list; Nissanka only conditional upon clearance |
| https://www.thenews.pk/print/1443109-nissanka-ruled-out-of-tri-series-as-pakistan-sl-step-up-preparations | 16 Oct dated Nissanka medically ruled out and Lahiru Udara called up; Sri Lanka match XI still unverified |
| https://www.wisden.com/series/pakistan-odi-tri-series-2026/cricket-news/pakistan-tri-series-2026-all-you-need-to-know-full-schedule-squads-venues-and-match-timings-for-the-odi-tri-series | 16 Oct squad comparison; Hasaranga injury and Arachchige role |
| https://www.pcb.com.pk/match/36405.html | **11 Nov 2025** PAK 299/5 and SL 293/9 ODI, Rawalpindi; historical, NOT today |
| https://www.cricbuzz.com/live-cricket-scorecard/170720/pak-vs-sl-1st-odi-match-pakistan-odi-tri-series-2026 | 18 Oct fixture/scorecard route, pre-match indexed; no score/playing XI used from live section |
| https://www.icc-cricket.com/matches/274142/pakistan-vs-sri-lanka | ICC exact 18 Oct match centre route; direct opening returned cache-miss, no XI claim |
| https://www.cricbuzz.com/cricket-series/ (search cricket ground records for Rawalpindi ODI) | Rawalpindi historical 31 ODI/242 first-innings mean from structured ground-stat discovery; current-regime count/time not certified |
| https://www.pcb.com.pk/ | Official Pakistan cricket match scorecards and team announcements as field-owner, match by date, Nov 2025/2026 home fixtures |
| https://www.icc-cricket.com/ | Independent international governing-body current ODI fixture and prior-series scorecards |
| https://www.espncricinfo.com/ | Cricket match scorecards/schedules for PAK AUS May–June 2026, Bangladesh March, NZ March–April 2025, SL England September 2026 and Jan 2026, WI June 2026, 2025 bilateral ODI games; individual exact paths not fully retained |
| https://www.wisden.com/ | Prior-series scorecard index and dated historical aggregates; does not by itself independently collect every official ball count |
| https://www.accuweather.com/ | Rawalpindi 18 Oct dated pre-match forecast: hazy sun, low precipitation probability; location/product exact route and issued time not retained |
| GitHub at SHA `3e29a58693e2ed02ff862e9bf0f751af2feadee1`: `PROBABILITY_TOOLKIT.md`, `BASE_RATES_REGISTER.md`, `SELECTION_RULES.md`, `RULES_CRICKET.md`, `research/prompts/1_sports/CRICKET.md` and shared core | Manual normal-mixture rule, historical cricket baseline not derived, selection thresholds, game-log statuses |

**Required open-field attempts/closure status:**

| Field | Actual search or comparison performed | Status / next field-owner route |
|---|---|---|
| Match ID/date, tournament | PCB + ECB organizer releases and ICC listed match | CLOSED at fixture level; native event IDs beyond ICC URL not independently reconciled |
| Toss and bat-first activation | Current 18 Oct independently dated local report | PARTIAL; open PCB exact match official toss and publication timestamp |
| Pakistan XI, openers, batting order, bench | PCB 5 Oct squad, PCB training, current match centre search | NOT_VERIFIED; PCB match 1 XI / scorecard selection, pre-first-ball timestamp |
| Sri Lanka XI, new-ball pair, bench | ICC 4 Oct squad, 16 Oct Udara report; official match centre discovery | NOT_VERIFIED; SLC/PCB XI and exact new-ball roles publication/time |
| Pakistan and Sri Lanka injury/selection | PCB official roster; ICC original SLC roster; latest Nissanka replacement; Hasaranga replacement coverage | PARTIAL; exact-match last-minute scratch/injury updates require checking |
| Form L5/L10/L15/L20 | Schedules/scorecards compiled into true-n, with reduced-overs and chase annotations | PARTIAL; row-by-row independent official+provider corroboration and correction/overs of some fixtures needed |
| Five-over phase sample | Scorecard/feed routes for 2025 and 2026; no systematic five-over legal-ball data recovered | MISSING; derive actual five-over runs/wickets by official ball-by-ball for each bat-first ODI before cutoff |
| Current venue pitch strip | Venue history and pre-match preview routes | NOT_VERIFIED; field-owner strip/pitch report and ground staff/official toss statements |
| Weather and DLS | Pre-match daily forecast | PARTIAL; official ground match conditions, precipitation radar/forecast time, interruption risk |
| Same-line venue baseline | Historical reported first-innings mean 242/31; not exact-era matched | MISSING; filter all ODI 50-over first-innings scorecards in chosen date interval and map historic full overs |
| Physical innings-wickets/phase joint | No verified bowling allocation or 5-over probabilities | NOT_COMPUTED; cannot claim exact joint or physically constrained grid |
| Operator action | User provided lines without bookmaker/operator | UNKNOWN_DEFINITION; obtain specific 50-over and phase rain/wicket rules if settling |
| Writer lease and verified cumulative active source | Checked GitHub active_minis inventory and previous local standalone draft; no verified active original | BLOCKED_APPEND; reconcile issuing writer before any official mini update |

### A9. Verification matrix, safety and file readback

| Requirement | Result |
|---|---|
| Step 1 GitHub pinned main and relevant controls | PASS for named controls; some lengthy ancillary sections not exhaustively reread |
| Step 2 official fixture/format/venue/toss | Fixture confirmed, toss single second-lineage report; exact first-ball and operator rules not independently verified |
| Step 3 exact XI, starters, bench, absences | Injury/squad updates covered; both XIs and new-ball pair OPEN; C20 INFORMATION_INCOMPLETE |
| Step 3 both teams' last 5/10/15/20 | True n=5/10/15/20 printed, pre-date rows, chases and reduced games annotated; independent row-by-row verification OPEN |
| Step 4 innings and phase conditional math | Four supplied numeric directions priced, formulas/weights/centres/widths shown; no predictive calibration or physically exact joint |
| Step 4 baseline/expected score/uncertainty | Expected innings 277.75 and 5-over 29.5 conditional estimates; league-only baselines missing; team wickets and all-match joint not modelled |
| Step 5 candidates/top-2/dependence | Four ranked directions; only 2 primary; complements checked; Fréchet joint interval only |
| Step 6 ODI phase, toss, weather, DLS rules | ODI vs T20 distinguished; limited DLS/operator detail; first innings confirmed via secondary toss source |
| Step 7 retain original, no retrospective/import | Proposed local draft only; event result excluded; no settlement, no canonical P-ID, no Github/Drive writes |
| Historical pregame performance eligibility | **FAIL**: issue completed after scheduled 19:00 AEDT; do not count prospective pre-start predictions |
| C21 probabilities | APPROXIMATE, UNCALIBRATED; primary analyst assumptions explicit; five-over parameter provenance weak |
| C16/C22 complete actual active-mini update | **BLOCKED**: real active original and writer lease not established. Companion cumulative DRAFT copy may include unchanged previous draft; no assertion of issued official mini |
| Overall | `RESEARCH_RETAINED_AS_DRAFT` / `INFORMATION_INCOMPLETE` / `POST_START_ISSUE` / `DRAFT_NOT_APPLIED` |

**SPORTS_ONLY_MARKET_BLIND: PASS** — user lines are thresholds, not odds. **OUTCOME_EXPOSURE:** match live/result intentionally not consulted; source publication-known-at may remain uncertain. **SETTLEMENT/RETROSPECTIVE: NOT_PERFORMED.** **CANONICAL_IMPORT: NOT_PERFORMED.** **ML/RL: NOT_RUN (per current methodology).**
<!-- END CARD LOCAL-20261018MELILL01-G0002 -->


# Standalone research card — Czech women's 1. liga, 18 October 2026
<!-- BEGIN CARD LOCAL-20261018MELILL01-G0003 -->

## Game card G0003 — ŽBK KP Brno vs Žabiny Brno B

**Proposed local event key:** `LOCAL-20261018MELILL01-G0003` (**DRAFT_ONLY**; original active mini/lease unverified). **Canonical ID:** `NOT_ASSIGNED / PROMPT_4_IMPORT`. **Mode:** `PUBLISHED_MAIN_PINNED / EXTERNAL_CHAT / LOCAL_MINI_STAGING`. **Pinned repository:** [`danisgreat/Sports-Research` commit `3e29a58693e2ed02ff862e9bf0f751af2feadee1`](https://github.com/danisgreat/Sports-Research/tree/3e29a58693e2ed02ff862e9bf0f751af2feadee1); MDS/P v22.2 / CR-2026.10.17-R6 / SEL-2026.10.12-v3. **Method:** `ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY`, no code/model/ML/RL and no outcome-based adjustment. **Card issuance:** `DRAFT_NOT_APPLIED`; research begun before scheduled tip but this file is not a verified pre-tip issued prediction; avoid prospective pre-start grading. **Operator action:** `UNKNOWN_DEFINITION`.

### Owner-entered Upcoming game block — retained

> Upcoming Basketball Game: KP Brno B (W) vs Zabiny Brno B (W), Czechia Liga 1 Women.  
> Estimated Game Time Start: 18 October 2026, 8:15 PM AEDT (may be delayed).  
> Supplied: KP (W) +4.0; Zabiny (W) -4.0; Combined Total Over 139.5 Points; Combined Total Under 139.5 Points.  
> Research all sources, recent games, injuries and players; rank four picks, name a winner, no retrospective; comply with current main methodology.

### Decision block: four supplied propositions

**CRITICAL CONTRACT IDENTITY CONFLICT:** Official 18-Oct-2026 women's 1. liga game is **ŽBK KP Brno vs Žabiny Brno B**, *not* **KP Brno B vs Žabiny Brno B**. KP Brno B is separately listed by the federation in another schedule. The date and time match the official ŽBK KP Brno fixture precisely, but the requested KP Brno B label is NOT equivalent. **All numbers below are CONDITIONAL on the intended first team being ŽBK KP Brno; they cannot be transferred to an actual KP Brno B youth fixture. Do not represent this as a verified contract until operator/team identity is reconciled.**

| Rank | Supplied full-game proposition | Uncalibrated `p_card` | Role / limitation |
|---:|---|---:|---|
| **1** | **Total points UNDER 139.5** | **0.678 (67.8%)** | Primary research direction, not certified; low scoring environment central assumption |
| **2** | **Žabiny Brno B −4.0** | **0.551 (55.1%)** | Secondary direction, **FAIL rank-2 0.58 floor**; exact 4-point win treated as PUSH |
| 3 | ŽBK KP Brno +4.0 | 0.449 (44.9%) | INFORMATIONAL, opposite direction of rank 2 |
| 4 | Total points OVER 139.5 | 0.322 (32.2%) | INFORMATIONAL, opposite direction of rank 1 |

**Potential game winner:** Žabiny Brno B `p_win ≈ 0.646` (64.6%), ŽBK KP Brno ≈35.4% under the illustrative full-game signed-margin family; calibrated status **NONE**. **Projected final including a small implicit overtime allowance:** ŽBK KP Brno **61.9**, Žabiny B **67.9**, total **129.8**, Žabiny margin **+6.0**. Do **not** interpret this point forecast as exact precision. Unverified lineups and identity are material; **NO actionable confirmed-team selection**.

**Selection discipline:** only ranks 1–2 are the framework's nominal primary selections; complementary ranks 3–4 document the full supplied universe. Rank1 numeric test `0.678 >= 0.620`, best eligible non-complementary alternative `0.551`, gap `0.127 >= 0.040`: `PASS_BASE_CASE` at epsilon 0.002; **unstable under scoring scenarios**. Rank2 `0.551 < 0.580`: **FLOOR_FAIL**. Selection ceiling 0.90 not triggered. No odds, odds-derived expected value, bookmaker tips or predictor websites were read. Neither cross-market joint nor guaranteed Hit@2 is claimed.

### A1 — Fixture identity, timing and rules

- **Official match owner:** Czech Basketball Federation 1. liga ženy 2026–27 Round 7, [official match ID 532124](https://sec.cz.basketball/zapas/532124), **ŽBK KP Brno (home) vs Žabiny Brno B (away)**, **18 October 2026, 11:15 Europe/Prague (CEST, UTC+2) = 09:15 UTC = 20:15 AEDT (UTC+11)**; venue **STAREZ Aréna Vodova, Brno**. These details from the official fixture page, not a score or match outcome.
- **Explicit alias conflict:** federation [KP Brno B separately registered](https://www.cz.basketball/tym/15882) and its [2026 schedules](https://kv.cz.basketball/zapasy?c=15882&d_do=&d_od=&y=2026). Do not silently collapse `ŽBK KP Brno`, `KP Brno B` and KP Brno's top-division first team.
- **Regulation:** Czech women's 1. liga uses FIBA 40-minute game (four 10-minute periods); 5-minute overtime if tied. This analysis assumes full-game final including OT; **contract operator overtime/cancel/void rules NOT VERIFIED**. Half-point total cannot push; exactly four-point away win pushes both ±4.0 handicap sides if normal handicap action applies.
- **Timing:** request received before the scheduled start, but exact request timestamp `NOT_CAPTURED`. Source histories screened to include fixtures completed before scheduled 18-Oct tip; official game outcome/live result intentionally **NOT consulted**. The actual tip time, research completion and first source-publication times remain partially unverified; this is NOT a verified pre-tip issued card, not retrospective or settled.
- **Home/travel:** both teams based in Brno. Žabiny B played away at Havířov on 17 October; KP played home against USK Praha B on 17 October. This is a back-to-back turnaround for both; travel/rotation effect has NOT been objectively measured.

### A2 — Historical online score rows (pre-event, official club/federation)

Read rows newest-to-oldest; entries H/A, PF–PA from the named team's viewpoint. L5/L10/L15/L20 are **overlapping windows of this one list**, not 50 independent observations. Current-season samples are only 5 per team. The 2025–26 competitions and squads can differ from 2026–27; cross-season interpretation requires shrinkage/sensitivity. Every historical datum before 18 October 2026 only. For individually uncorroborated rows, the federation schedule is primary, independent corroboration remains `OPEN`.

**ŽBK KP Brno — official [2026–27 schedule](https://sec.cz.basketball/tym/15880?y=2026) and [2025–26 schedule](https://sec.cz.basketball/tym/641?y=2025).** The 17-Oct home result was separately found on [USK official results](https://www.uskbasket.cz/liga?sezona=2023), but its independence/season-path mismatch merits verification.

| # | Date | H/A | Opponent | KP PF–PA | Source key |
|---:|---|---|---|---|---|
| 1 | 2026-10-17 | H | USK Praha B | 70–61 | KP-26 / USK |
| 2 | 2026-10-04 | A | BA Sparta | 40–48 | KP-26 |
| 3 | 2026-10-03 | A | Sokol Nusle | 35–57 | KP-26 |
| 4 | 2026-09-20 | A | TJ Sokol Pečky | 69–67 | KP-26 |
| 5 | 2026-09-19 | A | ŠBK Sadská | 93–95 | KP-26 |
| 6 | 2026-04-19 | H | TJ Sokol Pečky | 30–89 | KP-25 |
| 7 | 2026-04-17 | A | TJ Sokol Pečky | 40–93 | KP-25 |
| 8 | 2026-03-29 | A | TJ Sokol Pečky | 43–80 | KP-25 |
| 9 | 2026-03-28 | A | ŠBK Sadská | 61–86 | KP-25 |
| 10 | 2026-03-08 | H | DBaK | 72–41 | KP-25 |
| 11 | 2026-03-07 | H | BK Levhartice Chomutov B | 56–48 | KP-25 |
| 12 | 2026-02-22 | H | SK UP Olomouc | 86–83 | KP-25 |
| 13 | 2026-02-21 | H | BK Havířov | 61–68 | KP-25 |
| 14 | 2026-02-08 | A | USK Praha B | 59–69 | KP-25 |
| 15 | 2026-02-07 | A | BA Sparta | 51–79 | KP-25 |
| 16 | 2026-01-18 | H | Sokol Nusle | 73–61 | KP-25 |
| 17 | 2026-01-17 | H | HB Aritma | 85–68 | KP-25 |
| 18 | 2025-12-14 | A | Žabiny Brno B | 39–70 | KP-25 |
| 19 | 2025-12-13 | H | Žabiny Brno B | 57–65 | KP-25 |
| 20 | 2025-11-23 | H | ŠBK P-H Sadská | 84–78 | KP-25 |

**Žabiny Brno B — official [2026–27 schedule](https://www.cbf.cz.basketball/tym/9293), [2025–26 schedule](https://sec.cz.basketball/tym/9293?y=2025) and [club's fixture results](https://www.bkzabiny.cz/program-zapasu).** Note 17-Apr match required overtime in official historical page.

| # | Date | H/A | Opponent | Žabiny B PF–PA | Source key |
|---:|---|---|---|---|---|
| 1 | 2026-10-17 | A | BK Havířov | 58–81 | ZAB-club |
| 2 | 2026-10-04 | H | ŠBK Sadská | 74–56 | ZAB-26 |
| 3 | 2026-10-03 | H | TJ Sokol Pečky | 76–44 | ZAB-26 |
| 4 | 2026-09-20 | A | BK Strakonice | 70–59 | ZAB-26 |
| 5 | 2026-09-19 | A | HB Aritma | 66–81 | ZAB-26 |
| 6 | 2026-05-03 | A | BK Havířov | 58–63 | ZAB-25 |
| 7 | 2026-05-02 | A | TJ Sokol Pečky | 73–54 | ZAB-25 |
| 8 | 2026-04-21 | H | USK Praha B | 67–57 | ZAB-25 |
| 9 | 2026-04-19 | A | USK Praha B | 61–66 | ZAB-25 |
| 10 | 2026-04-17 | H | USK Praha B | 80–76 OT | ZAB-25 |
| 11 | 2026-03-28 | A | TJ Sokol Pečky | 59–68 | ZAB-25 |
| 12 | 2026-03-26 | A | ŠBK P-H Sadská | 85–74 | ZAB-25 |
| 13 | 2026-03-08 | H | BK Levhartice Chomutov B | 79–47 | ZAB-25 |
| 14 | 2026-03-07 | H | DBaK | 87–35 | ZAB-25 |
| 15 | 2026-02-22 | H | BK Havířov | 60–84 | ZAB-25 |
| 16 | 2026-02-21 | H | SK UP Olomouc | 78–48 | ZAB-25 |
| 17 | 2026-02-08 | A | BA Sparta | 56–62 | ZAB-25 |
| 18 | 2026-02-07 | A | USK Praha B | 65–73 | ZAB-25 |
| 19 | 2026-01-18 | H | HB Aritma | 80–68 | ZAB-25 |
| 20 | 2026-01-17 | H | Sokol Nusle | 61–52 | ZAB-25 |

**Observed window summaries (PF / PA, per game, true n shown):**

| Team | L5 (n=5) | L10 (n=10) | L15 (n=15) | L20 (n=20) | Interpretation |
|---|---|---|---|---|---|
| ŽBK KP Brno | 61.4 / 65.6 | 55.3 / 71.7 | 57.7 / 70.9 | 60.2 / 70.3 | Inconsistent offence; first 5 current season, older 15 separate season |
| Žabiny B | 68.8 / 64.2 | 68.3 / 63.7 | 70.2 / 63.0 | 69.7 / 62.4 | Moderately better offence and defence, recent away loss and rotation risk |

**Direct adult-team head-to-head:** [13-Dec-2025 match](https://cz.basketball/zapas/340518) ŽBK KP Brno 57–65 Žabiny Brno B; 14-Dec-2025 Žabiny B 70–39 KP. Historic Zab winning margins +8 and +31 are NOT representative of all current-player conditions and are not directly used as today's expected spread. Older meetings require separate date/roster validity checks.

### A3 — Exact-game players, starters, benches, injuries, rotation

**League-level rosters / prior performance, NOT confirmed for this match:**

- **ŽBK KP Brno** [federation player roster/stat page](https://sec.cz.basketball/tym/15880?y=2026): Tereza Trávníčková (23.0 ppg, n=2), Vendula Krausová (23.0, n=2), Karolína Cahová (15.3, n=4), Veronika Kunešová (7.3, n=4). Games-count disparities warn of eligibility/rotation changes and small-n bias.
- **Žabiny Brno B** [federation player roster/stat page](https://www.cbf.cz.basketball/tym/9293): Barbora Šubová (13.0 ppg, n=4), Babeta Loučková (11.8, n=4), Nikola Ježová (11.5, n=4); Aneta Kytlicová, Marie Hamzová and Ema Kameníková appear with n=1 game and cannot be treated as regular or available.

| Mandatory availability field | ŽBK KP Brno | Žabiny Brno B | Status / attempt |
|---|---|---|---|
| Exact 18-Oct confirmed starting five | NOT VERIFIED | NOT VERIFIED | Official match and team pages searched; past rosters cannot substitute for lineups |
| Exact active reserves / substitutes | NOT VERIFIED | NOT VERIFIED | Search official match sheet and game-day lists; none corroborated at issue |
| Medical injuries / illness / suspensions | NOT VERIFIED | NOT VERIFIED | No reliable exact-game verified OUT/fit list found; **do not infer no injuries** |
| Day-before/quick turnaround | 17-Oct home game verified | 17-Oct Havířov away game verified | Both short rest; selected rotation/minutes remain UNKNOWN |
| Venue/coach/scouting context | Same-city home team | Same-city away team | No reliable team-specific scheme, lineups or possession count established |

**Evidence ladder attempted:** organizer fixture/team profile and archived box/result listings; respective clubs, Czech-language player/news searches and alternate structured schedule sources. Further corroboration and late-change verification remain mandatory; `LINEUP_UNCONFIRMED / INFORMATION_INCOMPLETE`. No fabricated absence/healthy-player statement or star-player adjustment.

### A4 — Distribution, formulas, expected values and line action

**Scope:** simple hand-priced **conditional normal approximation**, not a possession-fitted model and not externally validated. Exact-competition league-wide `BASELINE_LEAGUE_V1` unavailable: `BASELINE_P = NOT_DERIVED_EXACT_COMPETITION` for every contract. No NBA/WNBA/NBL parameters transferred. No exact quarter/overtime grid enumerated; assumed final-score distributions implicitly include overtime and require live operating-rule check. Normal continuity corrections are approximate, not exact integer score probabilities.

**Raw current-season n=5 team comparison:**

- KP points = 61.4 PF / 65.6 conceded; Žabiny B = 68.8 PF / 64.2 conceded.
- KP matched centre `(61.4 + 64.2)/2 = 62.8`; Zab centre `(68.8 + 65.6)/2 = 67.2`; **raw total 130.0, away signed margin 4.4**. This is a *raw points-matching approximation*; offensive/defensive rating per 100 possessions unavailable. League game-wide scoring and distribution parameters not derived.
- **Analyst adjustment ledger:** historical adult matchup direction +2.1 to Žabiny, local-home advantage +0.5 to KP: away margin `4.4+2.1−0.5=6.0`. Back-to-back/rest uncertainty lower total centre by 0.45, residual possibility of OT partly returns 0.25: `130.0−0.45+0.25=129.8`. These magnitudes are explicit **subjective analyst assumptions**, not measured Czech league effects. Unadjusted p values separately below.
- **Assumed outcome SDs**: full final total σ_T = **21.0 points**; signed Zab−KP margin σ_D = **16.0 points**. These widths reflect uncertainty, not independently measured league residual widths. Let T∼Normal(129.8,21²), D∼Normal(6,16²). **Assume T independent of D** as a simplifying joint assumption only; no fitted covariance. Expected KP=(T−D)/2=**61.9**; Zab=(T+D)/2=**67.9**; team marginal SD `sqrt((21²+16²)/4) ≈ 13.2`, Cov(KP,Zab)=(21²−16²)/4=46.25 points², correlation ≈0.265. These are implied mathematical parameters, not directly observed.

**Total family (139.5, final points):**

`z_U=(139.5−129.8)/21 = +0.462`. With toolkit Φ table `P(UNDER)=Φ(+0.462)≈0.678`, `P(OVER)=1−0.678=0.322`. Unconditional W/P/L/V: Under `(0.678/0/0.322/0)`, Over `(0.322/0/0.678/0)` under assumed no-void full game.

**Margin family (Zab signed D and integer final scores):**

- `D≥5` wins Zab -4.0; `D=4` pushes; `D≤3` wins KP +4.0.
- Standard continuity bins give `W_Z≈P(D>4.5)=Φ((6−4.5)/16)=Φ(0.09375)≈0.5374`.
- `Push≈P(3.5<D<4.5)=Φ((4.5−6)/16)−Φ((3.5−6)/16)=Φ(−0.09375)−Φ(−0.15625)≈0.0247`.
- `L_Z≈P(D<3.5)=Φ((3.5−6)/16)=Φ(−0.15625)≈0.4379`.
- `p_card_Z=W/(W+L)=0.5374/(0.5374+0.4379)≈0.551`; KP reversed `0.4379/(0.9753)≈0.449`. Unconditional W/P/L/V for Zab -4: `(0.5374/0.0247/0.4379/0)` and KP +4 `(0.4379/0.0247/0.5374/0)`. Conditional decisive denominator about **0.9753**. Exact push bin requires true integer model; the smoothed bin is approximation.
- Winner `P(Zab wins)=Φ(6/16)=Φ(0.375)≈0.646`, complement KP 0.354 (draw after overtime excluded). Expected win margin 6.0 for Zab; **winner is not a 64.6% calibrated market model**.
- **Arithmetic precision:** Φ table/interpolation ε≈0.002 p per row; push-bin uncertainty may be greater because no fitted discrete league margin mass or OT tie enumeration. Complements total 1 on decisive events.

**Unadjusted sensitivity anchor:** T130.0, D4.4, same assumed widths: `P(Under)=Φ((139.5−130)/21)=Φ(0.452)≈0.674`; `P(Zab-4 | decisive)` with continuous push approximation ≈0.512. Thus margin preference is adjustment-dependent and fragile; result is **not** described as empirically proven.

**Low/base/high assumptions** (not confidence intervals; fixed widths, varied scoring and roster scenarios):

| Scenario | T centre | D (Zab−KP) centre | P(Zab −4 given decisive) | P(Under 139.5) | Notes |
|---|---:|---:|---:|---:|---|
| Low-pace / KP resilience | 122 | 3 | ≈0.475 | ≈0.797 | League scoring below current five-game blended anchor |
| Base | 129.8 | 6 | ≈0.551 | ≈0.678 | Tiny current-season sample, subjective adjustments |
| High-pace / Zab advantage | 141 | 9 | ≈0.626 | ≈0.472 | Rank1 can change; NOT stable at 62% selection floor |

**Joint dependence:** same coherent mathematical T,D independent *assumed*, but no calibrated joint or rigorous OT/int integer grid exists. Don't multiply to claim two-hit percentage. For rank1 Under (loss mass .322) and rank2 Zab -4 (loss mass .4379 unconditional, push .0247), Fréchet joint-loss range `max(0,.322+.4379−1)=0` to `min(.322,.4379)=.322`; **JOINT_UNQUANTIFIED / bounds only**. The straight Over and Under force exactly one success absent void; ±4 identical margin pair is complementary with common push.

### A5 — Baseline, candidate selection, shadow controls

- Four supplied propositions priced once on same final-score family and listed in probability rank order. Candidate universe **restricted to four supplied contracts** because no independent sourced, fixed-derived line recipe exists for other thresholds or player props. **No invented alternate totals or player lines**; no threshold tuning toward 90%.
- `BASELINE_LEAGUE_V1`: `NOT_DERIVED_EXACT_COMPETITION`, because a separate full 2026–27 women's 1. liga eligible fixture cohort, mean, SD and action-endpoint convention were not compiled; 20 games per team are not this cohort. Shadow rank-delta `NONE_BASELINES`, baseline-only `NONE_LEAGUE_COMPARATOR`; alternative shadow across different quantity is rank2 Zab −4 conditional p≈.551 and fails p≥0.58.
- Rank-1 gate: candidate Under 0.678, best alternative Zab−4 0.551, margin .127 > .04, floor > .62, **numeric PASS in base case**; scenario high pace drops Under to ~0.472, **SCENARIO_UNSTABLE / ADJUSTMENT_DEPENDENT**. Rank2 0.551 < 0.58 **FLOOR_FAIL**, cannot call top-two compliant high-confidence slate.
- Selection-line distance: total `139.5−129.8=+9.7` or z +.462; away cover at 4 uses continuous z `(6−4.5)/16=+.09375` before push adjustment. A margin only two points above the spread is vulnerable to minute/selection shocks.

### A6 — Failure routes, contextual mechanisms and current uncertainty

1. **Unders:** unexpected pace or unusually effective three-point shooting (KP recent 5-game variability 35–93 PF; Zab 58–76), weak defensive rebounding or OT/late fouling could move the total above 139.5.
2. **Žabiny −4:** if KP's high-scoring contributors are selected while Žabiny rotates after 17-Oct travel, a 1–3 point Žabiny win or KP outright victory loses; exact 4-point margin pushes; starting fives and bench unverified.
3. **Same-city home advantage:** smaller than generic inter-city factor; magnitude of +0.5 for KP speculative.
4. **Team-name mismatch and book settlement:** user line may refer to entirely different KP Brno B squad/competition. Do not act on the four percentages without original event ID and operator settlement definition.
5. **No injuries confirmed:** no verified absence is not proof of player fitness. Attempts do not close exact-game medical data.
6. **Distribution approximation:** normal family can emit non-integer, negative, or nonphysical scores in tails and does not calculate per-possession attack/defence, exact injury scenarios, score-state dependence or OT as separate states. This may be material in a second-tier small-sample league.

### A7 — Source ledger (market blind) and provenance

| Key | Source URL / owner | Primary observations | Independence and limitations |
|---|---|---|---|
| FIX | https://sec.cz.basketball/zapas/532124 | 18-Oct 11:15 CEST ŽBK KP Brno v Žabiny B, official native match identity | Organizer/field owner; postgame edits prohibited as inputs |
| KP-26 | https://sec.cz.basketball/tym/15880?y=2026 | KP current 2026–27 fixture scores / roster | Federation; 17-Oct score separately searched |
| KP-25 | https://sec.cz.basketball/tym/641?y=2025 | 15 historical KP entries | Federation; many remain secondary corroboration OPEN |
| ZAB-26 | https://www.cbf.cz.basketball/tym/9293 | Žabiny current 2026–27 results and player season rates | Federation mirror; not independent of sec.cz federation feed |
| ZAB-25 | https://sec.cz.basketball/tym/9293?y=2025 | 15 older Žabiny fixtures incl overtime | Federation; row-by-row independent checks OPEN |
| ZAB-club | https://www.bkzabiny.cz/program-zapasu | 17-Oct Havířov 58–81; club schedule | Club separate publisher; may share league underlying score feed |
| USK | https://www.uskbasket.cz/liga?sezona=2023 | 17-Oct USK Praha B 61–70 at ŽBK KP | Independent publisher claim, URL season query mismatch; verify exact fixture |
| H2H | https://cz.basketball/zapas/340518 | Prior adult matchup 2025-12-13 | Another official federation front end, same lineage as sec.cz |
| ALTTEAM | https://www.cz.basketball/tym/15882 | KP Brno B separately registered | Identity proof, not equivalent team |
| ALTTEAM-SCH | https://kv.cz.basketball/zapasy?c=15882&d_do=&d_od=&y=2026 | Alternate-team games with Žabiny B, different dates/competition | Do not borrow youth league scores |
| Github | https://github.com/danisgreat/Sports-Research/tree/3e29a58693e2ed02ff862e9bf0f751af2feadee1 | Governing prompt core and basketball sport file, current selection/toolkit | Read-only rules, not event evidence |

**Reading receipt:** During 2026-10-18 AEDT read pinned `CURRENT_STATE.md`, `research/prompts/1_GAME_CARD.md` and `research/prompts/1_sports/BASKETBALL.md` (all 7 steps), `SELECTION_RULES.md`, `PROBABILITY_TOOLKIT.md` §1, `CARD_AND_LOG_TEMPLATES.md`, `LEAGUE_PROFILES.md`, `RULES_BASKETBALL.md`, `ROSTER_AVAILABILITY_PROTOCOL.md`, `HISTORICAL_SOURCE_PROTOCOL.md`, `BASE_RATES_REGISTER.md`; other large sibling controls not reread in full in this turn. Drive active mini folder `1vgvDUB8-t4cfrmp0t3DH9NugcHEszgtq` inspected; **0 files**. Fallback to actual GitHub controls worked; unpublished original mini/lease cannot be recovered. Official match, current and archived team pages and club/USK corroboration searched. No post-match results were used. Exact URLs above are evidence paths, not claims of independently checked original publication timestamps.

### A8 — Persistent open-field/source-exhaustiveness queue

| Field | Attempt and result | Closure / next independent check |
|---|---|---|
| KP Brno B versus ŽBK KP Brno contract identity | Federation native match 532124 versus separately registered team | **CONFLICTING / BLOCKING**: resolve operator native match ID and exact displayed team |
| Starting five — both teams | Federation match/roster, club schedules and Czech name searches | **NOT_VERIFIED**: official 18-Oct playing sheet captured with pretip known-at timestamp |
| Bench, substitutions and medical — both | Federation team and roster listings; club news routes | **NOT_VERIFIED**: explicit active, scratch and verified absence/fitness reports |
| Current 17-Oct scores | Club and federation/USK cross-sources | **PARTIAL**: verify final status and exact timestamp pre-18-Oct tip from match sheet |
| Historical score L20 each | 40 dated rows from official 2025/2026 fixtures | **PARTIAL**: independent event-by-event checks, eligibility and correction times needed |
| Exact competition full cohort for baseline | Official tables read only, no deduplicated all-team season schedule | **MISSING**: 1. liga ženy 2026–27 game-level total/margin baseline before cutoff |
| Pace, possessions, adjusted efficiency and covariance | Team raw PF/PA sourced, no exact possession stats | **NOT_DERIVED**: obtain box-score possessions/ratings and uncertainty widths |
| Home/rest and OT rates | Same-city and 17-Oct schedule established | **ANALYST_ASSUMPTION**: measure rates for exact league/roster context |
| Overtime and operator 4.0 push/void conditions | FIBA sport defaults only | **UNKNOWN_DEFINITION**: named supplier rulebook, contract time-period and settlement |
| Exact tip, issue cutoff and official feed known-at | Scheduled time 20:15 AEDT from fixture | **UNVERIFIED**: no live or final result used; do not promote to pre-start issue |
| Writer lease / active original and canonical duplicate | Google Drive mini folder empty; GitHub main rules pinned | **BLOCKED_APPEND**: reconcile original mini, active-writer authority, duplicate check in unissued minis |

### A9 — Audit, disposition and future capture

| Check | Disposition |
|---|---|
| Official exact-game identity and time | **PARTIAL: confirmed schedule for ŽBK KP Brno vs Žabiny B; user KP Brno B different** |
| Sports-only and no-odds firewall | **PASS**; supplied thresholds only |
| Latest main pinned, read-only, no code/model | **PASS on opened controls** |
| History of both squads L5/L10/L15/L20 dated and printed | **40 rows collected; independent row checks OPEN** |
| Exact starters, selected bench, medical absence | **INFORMATION_INCOMPLETE / LINEUP_UNCONFIRMED** |
| Team and match score projection | **Reproducible hand approximation, not fitted possession model** |
| All 4 original lines and unconditional W/P/L/V | **PROVISIONALLY PRICED**; operator definition and roster open |
| Same-line league-only baseline | **MISSING**, do not replace with 0.5 |
| Rank1/R2 gates | **BASE PASS / R2 FLOOR_FAIL / SCENARIO_UNSTABLE** |
| Odds/EV | **NO_ODDS; financial EV NOT DETERMINABLE**, p_card are sporting probabilities |
| Actual mini lease and issue | **DRAFT_NOT_APPLIED**, original not available, P-ID not allocated |
| Settlement/retrospective/score exposure | **NONE**; do not grade this research as prospectively issued |
| Final | **RESEARCH_RETAINED_AS_DRAFT / IDENTITY_CONFLICT / UNCALIBRATED / SOURCE_GAPS_OPEN** |

<!-- END CARD LOCAL-20261018MELILL01-G0003 -->



<!-- CARD-FORMAT: mini-log-10 research card -->
<!-- STATUS: DRAFT_NOT_APPLIED / UNCALIBRATED_ANALYST_PRIMARY / LINEUP_UNCONFIRMED -->
# Soccer game research card — Beijing Guoan vs Qingdao West Coast, 18 October 2026

## Owner-entered Upcoming game request (preserved)

> Upcoming Soccer/Football Game: Beijing Guoan vs Qingdao West Coast, China Super League, 18 October 2026, estimated 10:00 PM AEDT (can be delayed, continue research).  
> Combined First Half Goals: Over/Under 0.5 Goals  
> Combined Total Goals: Over/Under 2.5 Goals  
> Combined Total Corners: Over/Under 10.5 Corners  
> Research both teams, verified lineups, injuries, current online history, probabilities, best four ranked directions, winner, sources and limitations. No settlement or retrospective, even if research passes kickoff.

### Owner's exact current request (verbatim transcription)

> Upcoming Soccer/Football Game: Beijing Guoan vs Qingdao West Coast, China Super League,  
> Estimated Game Time Start: 18 October 2026, 10:00 PM AEDT (can be delayed so continue the process as normal)
>
> Do comprehensive and accurate research, based on the instructions in the documents/drive. Provide the best 4 picks in order from most likely to least likely, for players and/or teams or anything else and pick your own picks, making the decision based on all the instructions and information provided in the documents. Provide accurate and detailed reasoning, based on the research and instructions. Always seek to find the latest starting and available players and players on the injury list or rested, and factor that into calculations. Refer to the GitHub main branch repo and associated documents.
>
> Combined First Half Goals: Over/Under 0.5 Goals  
> Combined Total Goals: Over/Under 2.5 Goals  
> Combined Total Corners: Over/Under 10.5 Corners
>
> Add a potential game winner as well, and make no mistakes, no hallucinations, and, importantly, be honest and accurate. Don't do a retrospective yet. Add all sources of information.  
> Accuracy, source quality, transparency, and compliance with the GitHub methodology on the main branch, and take accuracy over speed. if your analysis goes beyond the start time, I would rather you take a long time than rush it and be wrong, so take as long as you need, this is strict instructions. if your analysis goes beyond the start time. @GitHub

## A1 — Identity, authority, timing, and custody

| Control | Observation / state |
|---|---|
| Sport / exact league | Association football, China PR Super League, 2026 regular season, Round 28 |
| Teams / identity | Beijing Guoan (北京国安), home, vs Qingdao West Coast (青岛西海岸), away; no identified duplicate card in accessible standalone draft |
| Source/fixture | Beijing Guoan club ticketing notice and Beijing municipal government sport calendar; official schedule corroborated by FBref and Chinese fixture listings |
| Venue | Beijing Workers' Stadium (北京工人体育场), Beijing, China |
| Scheduled kickoff | Sunday 2026-10-18 19:00 CST / 11:00 UTC / 22:00 AEDT (Australia/Melbourne) |
| Actual kickoff / delayed? | NOT_VERIFIED. Do not infer from scheduled start. |
| Source research horizon | Prior matches must be completed before this fixture's actual kickoff; no 18-Oct fixture outcomes used |
| Request receipt | 2026-10-18 ~21:39 AEDT based on chat-local clock; exact request-time audit timestamp unavailable |
| Research/issue phase | Research begun before scheduled start; completed issue phase and original authorisation must be determined at handoff. No independent evidence of actual starting whistle in this card. |
| Authority | `PUBLISHED_MAIN_PINNED`, GitHub `main`, SHA `3e29a58693e2ed02ff862e9bf0f751af2feadee1` |
| Rules | MDS/P v22.2, CR-2026.10.17-R6, SEL-2026.10.12-v3; `research/prompts/1_GAME_CARD.md` plus `1_sports/SOCCER.md`; current core outranks retired model statements |
| Research/selection lane | `ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY / LEARNING_ONLY / NOT_PERFORMANCE_ELIGIBLE` |
| Local key | Proposed `LOCAL-20261018MELILL01-G0004` in an **unissued standalone draft**; active original and writer lease NOT_VERIFIED |
| Canonical ID | `NOT_ASSIGNED / PROMPT_4_IMPORT`; no ID allocated or reserved |
| GitHub/Drive edits | NONE; read-only controls. File returned to owner, not an issued active-mini append. |
| Model/runtime/odds | No ML/RL, executable sport model, bookmaker pricing, forecasts from tipsters, or odds used. Arithmetic derived by hand from displayed historical inputs and stated assumptions. |

### A2 — Decision summary: supplied universe and ranked eligible rows

**Important eligibility decision:** The highest raw six-contract probability is 1H Over 0.5 at ~0.685. Its half-specific data are available, but soccer `SELECTION_RULES §4` requires **p >= 0.72 and a 0.05 lead** for 1H Over 0.5 to occupy Rank 1. Because it would otherwise be first, it is **INELIGIBLE_FOR_PRIMARY_RANK1** and retained in the diagnostic universe, not misleadingly moved to Rank 2. The four below are ranked by probability among eligible remaining supplied contracts, following the prescribed family gate. Complementary rows are information, not independent picks.

| Rank | Supplied 90-min market | `p_card` | Unconditional W | P | L | V | Selection / interpretation |
|---:|---|---:|---:|---:|---:|---:|---|
| 1 | **Combined corners Under 10.5** | **0.645** | .645 | 0 | .355 | 0 | PRIMARY DIRECTION, gate precision unresolved, sensitive to corners sample weighting |
| 2 | **Combined goals Over 2.5** | **0.605** | .605 | 0 | .395 | 0 | SECONDARY DIRECTION, rank-2 0.58 floor met; close competitor |
| 3 | Combined goals Under 2.5 | 0.395 | .395 | 0 | .605 | 0 | INFORMATIVE OPPOSITE to rank 2 |
| 4 | Combined corners Over 10.5 | 0.355 | .355 | 0 | .645 | 0 | INFORMATIVE OPPOSITE to rank 1 |

| Not eligible for numeric primary ranking / diagnostic | p | Reason |
|---|---:|---|
| 1st-half combined goals **Over 0.5** | 0.685 | Half-specific model exists, but fails required 0.72 threshold for otherwise highest row, so the special Rank-1 family rule removes it from the eligible primary slate. |
| 1st-half combined goals Under 0.5 | 0.315 | Lower-ranked sixth option; all six supplied directions priced; not selected among four. |

**Potential 90-minute winner:** Beijing Guoan **0.530**; DRAW **0.224**; Qingdao West Coast **0.246**, from one independent-Poisson final-score family. If a non-draw result is required, Beijing's *conditional* share would be about 0.683 (0.530 / (0.530+0.246)), not an outright win probability. No extra time or shootout in an ordinary CSL league match.

**Expected regulation score:** Beijing **1.90**, Qingdao **1.23**, combined **3.13** goals, Beijing signed goal-margin mean +0.67. First half combined **1.155** goals. Total corners **9.50**. These are conditional analyst estimates, NOT validated xG or a fitted calibrated prediction.

### A3 — Official fixture, playing conditions, availability and travel

- Beijing Guoan's officially published 11-Oct ticket announcement fixes Round 28, Workers' Stadium and 18-Oct 19:00 Beijing time: https://www.bjnews.com.cn/detail/1791721820019001.html . Municipal verification: https://www.beijing.gov.cn/fwcj/calendar/tyss/6a38eb3a92c0e70bf722e62d.html .
- Beijing Daily's report of the 17-Oct pre-match press conference, posted 18-Oct 00:27 local, says Beijing had beaten Buriram United 1-0 during the previous week after travelling to Thailand; coach Nick Montgomery said recovery had been addressed. **Zhang Yuning was rested for the Buriram trip and described himself as ready to play; this is fitness availability, not proof of starting.** **Yang Liyu aggravated an existing injury against Buriram and may miss this match; conditional, not official ruled-out list.** Source: https://news.bjd.com.cn/2026/10/18/11998865.shtml ; independently reported press conference: https://www.sohu.com/a/1089057104_463728 .
- Qingdao manager named Zheng Zhi by FBref; Davidson and Aziz Yakubu were attack regulars in earlier confirmed matches. Their presence in the **18-Oct XI is NOT_CONFIRMED**. Prior 11-Oct list: https://bulinews.com/fixture/978165/predicted-lineups/beijing-guoan-qingdao-west-coast . Do not label past starting XI as today’s XI.
- Additional status reports conflict or are stale: current aggregator shows Qingdao's Rezende as injured and Wu Shaocong as a Beijing medical doubt, while other lists show old suspensions (Dawhan, Peng Xinli) and even Fabio Abreu as injured despite documented later appearances. No credible same-day independent recheck resolves these; **do not assume those bans or reports remain active**. Sources: https://www.flashscore.com/match/football/beijing-guoan-WSLjVBLN/qingdao-west-coast-0QkqH4Gf/ ; https://www.qiumiwu.com/game/114463542711 ; https://matchatlaslive.com/detail.php?id=2944828&kind=match .
- Both 18-Oct starting XIs and goalkeepers: `NOT_VERIFIED`; the available FotMob, Flashscore and TNT previews label previous XI or squad lists, NOT a confirmed exact-event XI. The benches, scratches, substitutions and individual medical records likewise `NOT_VERIFIED`: https://www.fotmob.com/en-GB/matches/beijing-guoan-vs-qingdao-west-coast/akpprg7m ; https://www.flashscore.com/match/football/beijing-guoan-WSLjVBLN/qingdao-west-coast-0QkqH4Gf/ ; https://www.tntsports.co.uk/football/china-resources-beverage-cfa-super-league/2026/beijing-guoan-qingdao-west-coast_mtc20006671/live-lineup.shtml .
- Last current CSL: Beijing away 3-0 Qingdao Hainiu on 9-Oct, Qingdao home 0-4 Dalian Yingbo on 11-Oct. Beijing additional Asian Champions League appearance at Buriram on 13-Oct, raising rotation/fatigue risk. Round and schedule independently corroborated by FBref and Beijing Daily.
- Exact pitch, 19:00 stadium weather, wind and injuries affecting specific minutes: `NOT_VERIFIED`; prior rain at 17-Oct training is **not** an 18-Oct pitch-condition measurement.
- Rules: CSL league, regulation 90 minutes + added time, draw permitted; official completed corners and halftime at referee whistle, subject to data provider/operator definitions; full-time markets exclude cup-only extra time. Abandonment/void definitions and specific unnamed operator unknown. Half-point goals/corners have no normal scoring push on completed action-valid matches.

### A3b — Dated CSL L20 history, one overlapping sample per team

**Scope:** Completed 2026 **Chinese Super League** only, latest 20, newest first and every record before 18-Oct kickoff. Dated match scores from FBref, independently compared by name/date against BeSoccer and theScore schedules; this is *not* 20 independent collectors, and event-by-event source timestamp capture remains incomplete. Team scores are from named team's perspective (`GF–GA`). Cup/ACL excluded from same-competition history, but travel considered independently. Source links: https://fbref.com/en/squads/8ab37ab8/2026/matchlogs/c62/schedule/Beijing-Guoan-Scores-and-Fixtures-Chinese-Super-League ; https://fbref.com/en/squads/d87e75be/2026/matchlogs/c62/schedule/Qingdao-West-Coast-Scores-and-Fixtures-Chinese-Super-League ; https://www.thescore.com/liga/teams/3345-beijing-guoan-fc/schedule ; https://www.thescore.com/mls/teams/3332-qingdao-west-coast-fc/schedule (site league URL slug is misleading; fixture content refers to the CSL); https://www.besoccer.com/team/matches/qingdao-youth-island .

| # | Beijing date | Opponent | H/A | GF–GA | Qingdao date | Opponent | H/A | GF–GA |
|---:|---|---|:---:|:---:|---|---|:---:|:---:|
|1|Oct 09|Qingdao Hainiu|A|3–0|Oct 11|Dalian Yingbo|H|0–4|
|2|Sep 05|Shanghai Port|A|0–0|Sep 05|Wuhan Three Towns|A|2–2|
|3|Aug 28|Dalian Yingbo|A|1–1|Aug 29|Tianjin Jinmen Tiger|A|1–1|
|4|Aug 22|Yunnan Yukun|H|3–3|Aug 22|Shandong Taishan|H|2–0|
|5|Aug 18|Shanghai Shenhua|A|3–0|Aug 14|Chongqing Tonglianglong|H|0–0|
|6|Aug 15|Tianjin Jinmen Tiger|A|4–2|Aug 09|Henan|A|0–0|
|7|Aug 07|Shenzhen Peng City|H|4–0|Aug 02|Qingdao Hainiu|H|2–0|
|8|Aug 01|Zhejiang|H|2–1|Jul 25|Liaoning Tieren|A|1–0|
|9|Jul 26|Chengdu Rongcheng|A|2–2|Jul 17|Chengdu Rongcheng|H|1–1|
|10|Jul 17|Liaoning Tieren|H|1–1|Jul 11|Shenzhen Peng City|A|0–3|
|11|Jul 04|Shandong Taishan|H|2–0|Jul 04|Shanghai Port|H|2–1|
|12|Jun 27|Wuhan Three Towns|H|1–0|Jun 28|Zhejiang|H|3–1|
|13|May 30|Chongqing Tonglianglong|A|3–2|May 30|Shanghai Shenhua|H|2–2|
|14|May 23|Henan|H|1–2|May 24|Yunnan Yukun|A|3–2|
|15|May 19|Qingdao West Coast|A|1–1|May 19|Beijing Guoan|H|1–1|
|16|May 15|Qingdao Hainiu|H|4–2|May 15|Dalian Yingbo|A|3–2|
|17|May 10|Shanghai Port|H|2–2|May 10|Wuhan Three Towns|H|1–1|
|18|May 06|Dalian Yingbo|H|3–0|May 05|Tianjin Jinmen Tiger|H|1–1|
|19|May 02|Yunnan Yukun|A|3–3|May 01|Shandong Taishan|A|1–1|
|20|Apr 25|Tianjin Jinmen Tiger|H|2–4|Apr 26|Chongqing Tonglianglong|A|1–1|

**R2 overlapping window arithmetic, matches counted once:**

| Window | Beijing n | GF | GA | GF/match | GA/match | Qingdao n | GF | GA | GF/match | GA/match |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| L5 | 5 | 10 | 4 | 2.00 | 0.80 | 5 | 5 | 7 | 1.00 | 1.40 |
| L10 | 10 | 23 | 10 | 2.30 | 1.00 | 10 | 9 | 11 | 0.90 | 1.10 |
| L15 | 15 | 31 | 15 | 2.07 | 1.00 | 15 | 20 | 18 | 1.33 | 1.20 |
| L20 | 20 | 45 | 26 | 2.25 | 1.30 | 20 | 27 | 24 | 1.35 | 1.20 |

Season-to-date **n=27 each**: Beijing 52 GF, 33 GA (1.93/1.22), home n=13 scored 27, conceded 18 (2.08/1.38). Qingdao 31 GF, 36 GA (1.15/1.33), away n=13 scored 14, conceded 23 (1.08/1.77). Source: https://fbref.com/en/squads/8ab37ab8/2026/matchlogs/c62/schedule/Beijing-Guoan-Scores-and-Fixtures-Chinese-Super-League ; https://fbref.com/en/squads/d87e75be/2026/matchlogs/c62/schedule/Qingdao-West-Coast-Scores-and-Fixtures-Chinese-Super-League ; independent contextual rates: https://www.soccerstats.com/pmatch.asp?league=china&stats=223-16-14-2026 .

### A3c — Phase and corners samples (independently sourced quantities)

- First-half, site/role-specific **current 2026 league**: Beijing home n=13: GF 10, GA 4 first-half; Qingdao away n=13: GF 6, GA 10 first-half. First-half combined over 0.5 occurred in approximately 69% of Beijing home fixtures and 69% of Qingdao away fixtures, according to published season rates. The two records describe overlapping *team populations*, not 26 independent matchup simulations. Source: https://www.soccerstats.com/pmatch.asp?league=china&stats=223-16-14-2026 .
- Corners: 24score separate *actual recorded corner counts* (not prices): Beijing full-season 27 matches, mean total 10.63; Beijing home n=13, mean combined 10.62. Qingdao full-season n=27 mean total 9.30; Qingdao away n=13 mean total 10.00. Recent ten-game means 10.3 Beijing and 7.9 Qingdao. These rates are from provider's corner tables; venue means are not a full exact-venue covariance estimate. Source: https://m.24score.com/football/match/844270-beijing_guoan-qingdao_west_coast .
- Sample prior actual corner count rows: 9-Oct Hainiu–Beijing 2+4=6; 5-Sep Shanghai Port–Beijing 14+1=15; 28-Aug Dalian–Beijing 4+1=5; 22-Aug Beijing–Yunnan 9+5=14; 18-Aug Shenhua–Beijing 8+5=13; 11-Oct Qingdao–Dalian 3+3=6; 5-Sep Wuhan–Qingdao 6+4=10; 29-Aug Tianjin–Qingdao 5+6=11; 22-Aug Qingdao–Shandong 3+4=7; 14-Aug Qingdao–Chongqing 3+4=7. Same 24score source, additional data lineage not proven independent.
- Most recent H2H 19-May 2026 was Qingdao West Coast 1–1 Beijing, HT 0–0, full corners 3–9 (12); H2H as weak contextual illustration, not enough to set baseline. Sources https://fbref.com/en/stathead/matchup/teams/d87e75be/8ab37ab8/Qingdao-West-Coast-vs-Beijing-Guoan-History and https://m.24score.com/football/match/844270-beijing_guoan-qingdao_west_coast .
- xG/shot quality adjusted for opponents: `NOT_DERIVED`, no verified exact-match and same-competition xG sample located; GF/GA are explicitly raw realised-goal proxies and not masqueraded as expected goals.

### A4 — Coherent hand probability construction, four supplied market rows plus phase pair

#### Regulation-goal family (independent half and team Poisson approximations)

1. Unadjusted team goal means: Beijing from season home scoring and Qingdao away conceding = (27/13 + 23/13)/2 = **1.9231**, about 1.925; Qingdao from season away scoring and Beijing home conceding = (14/13 + 18/13)/2 = **1.2308**. Total unadjusted **3.154**.
2. Availability/rest **subjective** Beijing adjustment: Buriram travel/possible Yang Liyu absence −0.08 goals, return/rested Zhang Yuning +0.05 goals, net −0.03 => Beijing **1.90**; Qingdao **1.23**, total **3.13**. No assertion of measured player impact or opponent-adjusted xG. No numerical Qingdao medical adjustment (unverified).
3. First-half attack from exact site-and-innings splits: Beijing `(10/13 + 10/13)/2 = 0.7692`; Qingdao `(6/13 + 4/13)/2 = 0.3846`; aggregate **1.1538**, rounded to **1.155** for calculation. Second-half centres defined as residual Beijing `1.90 − .770=1.130`, Qingdao `1.23 − .385=.845`. Thus half-by-team processes sum to the full team goal means. Independent Poisson increments and teams are simplifying assumptions, with possible shared tempo/low-score correction MISSING.
4. Full-game goals `G = GB + GQ ~ Poisson(3.13)`; P(total 0–2) = `exp(−3.13) [1 + 3.13 + (3.13)^2/2]` = `~0.04372 × 9.02845 = 0.395`; P(Over 2.5) = **0.605**. This is a 90-min result, no overtime mixture.
5. First-half goals `H ~ Poisson(1.155)`; P(Under 0.5)=`exp(−1.155)=0.315`; Over 0.5=**0.685**. The 1H variable is explicitly coupled to regulation full-time as `G=H + G_second`, not an unlinked substitute.
6. Winner: independent team goal Poisson(1.90) vs Poisson(1.23), summing shared scoreline states: Beijing victory **~0.530**, exact draw **~0.224**, Qingdao victory **~0.246** (sums 1.000 at shown precision). Home signed margin expected +0.67, exact integer scoreline implied. 90-minute draw not voided in three-way winner; two-way action convention unknown and no two-way contract is ranked.

#### Provider-backed separate corner-count family

1. Relevant location 13-game combined-corner averages: Beijing home **10.62**, Qingdao away **10.00**; mean **10.31**. Last-ten-match combined means Beijing **10.3**, Qingdao **7.9**, mean **9.10**.
2. To avoid a stale-season-only anchor, analyst recipe is predeclared: **one-third location sample + two-thirds last-ten sample**, `λ_C = (1/3)(10.31)+(2/3)(9.10)=9.503`, round **9.50**. This arbitrary weighting is a source-backed *assumption*, not a fitted corner model. Other weights are tested in sensitivity.
3. Corners `C ~ Poisson(9.50)` independent of goal counts **only for marginal pricing**; no cross-quantity joint is claimed. The distribution is analytically normalized on all nonnegative integers. P(Under 10.5)=`Σ_(k=0)^10 exp(−9.5)×9.5^k/k!` ≈ **0.645**. Checkpoints `P(C=9)≈0.1300, P(C=10)≈0.1235`; cumulative through 10 ≈0.645. Therefore P(Over 10.5)=**0.355**.
4. This Poisson may understate corner-count overdispersion. Variance, team/team and goal/corner dependence are not measured and the exact count provider settlement definition is unconfirmed. The corner choice is therefore unusually fragile.

**Precision:** Poisson recurrence and 3-decimal display give an effective probability precision around ±0.002 (with greater uncertainty from *assumptions*); comparisons use unrounded intermediate values conceptually. All six W/P/L/V: no ties/half-point pushes on normally completed fixtures; W=p, L=1-p, P=0, V=0 *conditional on action*, with action probability itself not estimated. Complements sum to one; H and G share an explicit nested mechanism.

#### League-only comparator attempt

Published prematchstats league context reports a 2026 CSL mean of **3.11 goals per game** from **217 matches** and Over 2.5 at **58%**: https://prematchstats.com/china/chinese-super-league/beijing-guoan-vs-qingdao-west-coast-stats/15552654 . If 3.11 were a justified Poisson league-only intensity, its *illustrative* same-line Over 2.5 would be `1−exp(−3.11)[1+3.11+(3.11²/2)]≈0.60`. **Do not treat this as an official frozen `BASELINE_LEAGUE_V1`:** individual 217 match IDs, independent corroboration and strict known-at cutoff were not reconciled. `BASELINE_P = NOT_FROZEN_DATE_VERIFIED` for all rows, and exact CSL league-only corners and halftime inputs remain `NOT_ESTIMATED`. No placeholder .50 baseline.

### A5 — Frozen candidates, ranking policy, sensitivities, dependence and gates

- Candidate universe frozen to **six** named directions supplied by user (1H O/U0.5, FT goals O/U2.5, FT corners O/U10.5); no invented alternate lines or player props. All six explicitly priced once from their own physical quantities. No selection above ceiling 0.90.
- The rank-1 `1H Over 0.5` special family rule mandates half-specific evidence **AND** 0.72 minimum **AND** 0.05 lead if it would be rank1. Its empirical 1H rates support about .685 but not .720, so `FAMILY_RANK1_INELIGIBLE`, diagnostic only. Removing it, selected ranking: Corners U10.5 0.645, FT O2.5 0.605, FT U2.5 0.395, Corners O10.5 0.355. Rank 3/4 are opposites, NOT extra independent recommendations.
- Rank-1 numeric gate: probability ~0.645 passes 0.62 floor; strongest eligible non-complementary alternative FT O2.5 ~0.605, gap **~0.040**, indistinguishable from the 0.04 threshold within 2ε≈0.004. **`GATE_UNRESOLVED_PRECISION`**, not PASS. Separate `SHADOW_GATE_RET03` (other lines on same *corners* quantity removed): same FT O2.5 competitor, likewise unresolved. Rank-2 0.605 ≥0.58, nominal pass.
- Rank-2 shadow different quantity `SHADOW_R2_RET04`: FT goals Over 2.5, same as selected rank2. `SHADOW_R2_XCARD6`: FT goals Over 2.5; no exact goal/corner joint derived. `SHADOW_RANK_DELTA`: NONE, no verified league-only baseline for two eligible rows. `SHADOW_BASE_ONLY`: same goal baseline before small player rest change, but not separately certified as mixture from material branches.
- Failure of both top two = `(corners ≥11) ∩ (goals ≤2)`. Marginal losses 0.355 and 0.395; **Fréchet bounds [0, 0.355]**. No unjustified product 0.355×0.395. The historical 0.30 target / 0.35 warning cannot be decisively evaluated because joint correlation is unmeasured. Both complementary pairs are `FORCED_PAIR` and excluded as independent Hit@2 evidence.
- Total-goal Over2.5 line distance from mean: `3.13−2.5=+0.63 goals`. Corners Under10.5 distance: `10.5−9.5=+1.0 corner`; 1H Over0.5 distance `1.155−0.5=+0.655 goals`. Discrete threshold cdfs computed via integer events, not normal z.

| Sensitivity case | FT goal λ | P(O2.5) | HT λ | P(HT O0.5) | Corner λ | P(U10.5) | Mechanism / caution |
|---|---:|---:|---:|---:|---:|---:|---|
| Low-scoring, corner-suppressing | 2.70 | ~0.506 | 0.95 | ~0.613 | 8.5 | ~0.760 | Defences/absences inhibit finishing and corner demand |
| **Base** | **3.13** | **0.605** | **1.155** | **0.685** | **9.5** | **0.645** | Current season, site split and chosen weighting |
| High-scoring, high-corner | 3.60 | ~0.697 | 1.35 | ~0.741 | 10.5 | ~0.521 | Fast match, efficient finishing and repeated wide attacks |

Separate *unadjusted* scoring mean 3.154 implies Over2.5 about 0.611, vs base about 0.605. Corner venue-only mean 10.31 gives Under10.5 about 0.55, while recent-only mean 9.10 gives about 0.69. Therefore use `ADJUSTMENT_DEPENDENT`: a defensible alternate corner weighting can change which row ranks first or whether Rank1 reaches 0.62. Sensitivity ranges are scenarios, not confidence intervals.

### A6 — Tactical/evidence synthesis, failure paths, winner

1. Beijing's current-season home scoring 2.08 per match meets Qingdao away concessions 1.77; however Qingdao's season-long draw rate (14/27) and the 1–1 reverse fixture warn against treating home victory as certain.
2. Beijing's 18-event all-competition unbeaten narrative includes ACL and Cup opponents; exact-competition L20 is separately displayed so those are not misclassified as 20 CSL results. Beijing recent 3–0 and Qingdao recent 0–4 are context, not sole projection anchors.
3. Beijing's overseas travel may suppress late attacking intensity; Zhang Yuning's return potentially offsets some of that, and Yang Liyu's old injury flare could reduce wing depth. Numeric magnitudes are not sourced player impact figures.
4. Qingdao's defensive ability varies: 0–0 against Henan and Chongqing in August, 0–4 against Dalian in October. A sustained low block could suppress 1H and total goals, while conceding corners to Beijing pressure.
5. Beijing strong home attacking means goals may exceed 2.5, but 0–0/1–1 routes remain tangible. The margin winner estimate is **Beijing 53.0%, draw 22.4%, Qingdao 24.6%** (Poisson approximation).
6. Corners may exceed 10.5 even with fewer than three goals if one side trails and generates repeat attacks, or remain below if play is central or conversion rapid. A goal model alone cannot size corners; the separate actual-corners provider is essential.
7. Starting XIs, late replacements, goalkeeper fitness and the pitch have not been verified. This is **LINEUP_UNCONFIRMED**, not fully evidenced pregame prediction. A late reported XI cannot be assumed known before research cutoff unless its own publication time is demonstrated.

### A7 — Source and observation register (no market-derived estimates)

| Key | Direct URL | Field / date known, limitations |
|---|---|---|
| FIX-OFFICIAL-CLUB | https://www.bjnews.com.cn/detail/1791721820019001.html | Club's 2026-10-11 match date/time/stadium/round notice |
| FIX-BEIJING | https://www.beijing.gov.cn/fwcj/calendar/tyss/6a38eb3a92c0e70bf722e62d.html | Government sport schedule; independently corroborates venue/date |
| FIX-FBREF | https://fbref.com/en/stathead/matchup/teams/d87e75be/8ab37ab8/Qingdao-West-Coast-vs-Beijing-Guoan-History | Fixture and past H2H results; prior H2H May 2026 1–1 |
| HISTORY-BEIJING | https://fbref.com/en/squads/8ab37ab8/2026/matchlogs/c62/schedule/Beijing-Guoan-Scores-and-Fixtures-Chinese-Super-League | Dated 2026 CSL results, season GF/GA and home splits; provider may block full page fetch but search-index exact rows recovered |
| HISTORY-QINGDAO | https://fbref.com/en/squads/d87e75be/2026/matchlogs/c62/schedule/Qingdao-West-Coast-Scores-and-Fixtures-Chinese-Super-League | Same for Qingdao West Coast, 2026 season and away splits |
| VERIFY-BEIJING | https://www.thescore.com/liga/teams/3345-beijing-guoan-fc/schedule | Independently indexed dated 2026 match scores |
| VERIFY-QINGDAO | https://www.thescore.com/mls/teams/3332-qingdao-west-coast-fc/schedule | Independently indexed 2026 results; URL league slug mislabelled |
| VERIFY-QINGDAO2 | https://www.besoccer.com/team/matches/qingdao-youth-island | Independent dated results and alias Qingdao Youth Island |
| HALF-SPLITS | https://www.soccerstats.com/pmatch.asp?league=china&stats=223-16-14-2026 | Pre-match 2026 venue scoring / first-half totals and team goal timing, n=13 each relevant venue side |
| CORNERS | https://m.24score.com/football/match/844270-beijing_guoan-qingdao_west_coast | 2026 same-league FT corners n27 each, relevant n13 venue, L10 n10 and past corner rows; **prices/odds on page ignored**, raw stats only |
| CORNER-CHECK | https://matchatlaslive.com/detail.php?id=2944828&kind=match | Date-specific copies of underlying Goaloo corner rows (18 Oct 00:47 Beijing time); likely common underlying feed, not an independent collector |
| PREMATCH-REPORT | https://news.bjd.com.cn/2026/10/18/11998865.shtml | Newspaper reporting 17-Oct coach/player press conference, rest/return and injury doubt |
| PRESS-CHECK | https://www.sohu.com/a/1089057104_463728 | 17-Oct press conference independent publisher/report; content lineage may still derive same interview |
| PLAYER-STATUS | https://www.flashscore.com/match/football/beijing-guoan-WSLjVBLN/qingdao-west-coast-0QkqH4Gf/ | Official XI not confirmed; aggregator doubtful/injury field may be stale |
| PLAYER-STATUS-CN | https://www.qiumiwu.com/game/114463542711 | Old injury and suspension lists; **not accepted as live-confirmed** |
| LAST-XI | https://bulinews.com/fixture/978165/predicted-lineups/beijing-guoan-qingdao-west-coast | Exact 13-Oct and 11-Oct past XI, **not today's XI** |
| CSL-BASELINE-ATTEMPT | https://prematchstats.com/china/chinese-super-league/beijing-guoan-vs-qingdao-west-coast-stats/15552654 | Reported 217 league matches / goals mean3.11; date-level frozen roster lacking |
| REPO-CONTROLS | https://github.com/danisgreat/Sports-Research/tree/3e29a58693e2ed02ff862e9bf0f751af2feadee1 | Read-only authority for current methodology; not game data |

**Reading receipt and failures:** GitHub main commit resolved before calculation, opened exact `research/prompts/1_GAME_CARD.md`, `research/prompts/1_sports/SOCCER.md`, `CURRENT_RULES.md`, `SELECTION_RULES.md`, `CARD_AND_LOG_TEMPLATES.md`, `PROBABILITY_TOOLKIT.md` operative distribution, `RULES_SOCCER.md` live §0, `ROSTER_AVAILABILITY_PROTOCOL.md`, `HISTORICAL_SOURCE_PROTOCOL.md`, `LEAGUE_PROFILES.md`, `BASE_RATES_REGISTER.md`, `research/prompts/COMMON_OPERATING_PROTOCOL.md`, and state as discussed; not all large controls read in full. Web research opened multiple Chinese-language sources and structured score histories; some FBref, matchatlas, Soccerstats and newspaper pages returned cache miss / 403 on direct open but search-index extracts supplied specific rows; partial source access recorded, not falsely claimed fully opened. Actual roster announcement was not obtained. No synthetic result or post-fixture grade inserted. Writer's active mini and lease not established; original mini in Drive previously inspected empty.

### A8 — Outstanding evidence/field closure

| Field | Source attempts | Status / next verification |
|---|---|---|
| Beijing first XI / keeper | Beijing Daily, Flashscore, FotMob, TNT, indexed CN sources; earlier confirmed 9-Oct, 13-Oct lineups distinct | `NOT_VERIFIED`: official Oct18 lineup announcement/club social with publication time |
| Beijing selected bench, scratches | Same routes | `NOT_VERIFIED`, roster/previous-match bench is NOT today’s selection |
| Beijing injuries / return | 17-Oct press conference corroborated; other aggregator conflicts | `PARTIAL`: Zhang fit but starting unverified; Yang injury doubt; Wu/He/Han current status unresolved |
| Qingdao first XI / keeper / bench | Club/lineup providers, 11-Oct XI indexed | `NOT_VERIFIED`: official Oct18 sheet / original club announcement |
| Qingdao injuries / suspensions | Flashscore, Qiumiwu, player roster | `PARTIAL/STALE_CONFLICT`: Rezende possible injury; Peng ban from Aug not proof for Oct; verify original match-day suspension notice |
| Raw 20-score cohort | 20 dated CSL rows each from FBref, independent theScore/BeSoccer comparison | `PARTIAL`: some date/index/known-at independent row-to-row audit still open |
| 1H sample | 2026 site split and 69% venue over | `PARTIAL`: no official per-match 27-game 1H scoreline ledger, no xG split |
| Corners provider n/variance | 24score seasonal/recent averages, source examples, Goaloo-linked partial replicate | `PARTIAL`: same-origin issue, no dispersion estimate or xG-corner covariance |
| League baseline | 217-game summary found | `NOT_FROZEN_DATE_VERIFIED`: individual fixture IDs, exact cutoff and comparator for corners/halves lacking |
| Actual weather/surface | Weather and pitch search inconclusive; rain at prior-day training | `NOT_VERIFIED`: game-day pitch inspection and weather official observation |
| Actual kickoff and pre-start known-at | Scheduled 19:00 CST verified | `NOT_VERIFIED`: preserve actual issue clock and evidence boundary separately |
| Operator endpoint and abandonment action | Standard regulation football understood; unnamed supplier | `UNKNOWN`: provider-specific 90-min corner/stoppage and abandonment rulebook |
| Original active mini / writer lease | Existing 17-Oct Drive active-mini folder empty; GitHub pinned main read-only; previous standalone cumulative draft exists but unissued | `BLOCKED_APPEND`: reconcile verified original and exclusive writer; draft is not a commit or issued card |

### A9 — Completed research audit and disposition

| Audit | Result |
|---|---|
| Confirmed exact official fixture, date/venue/kickoff | YES, official club + municipal + provider |
| No same-event duplicate in accessible 3-card standalone draft | YES; unpublished other minis not fully searchable |
| Recent both-team L5/L10/L15/L20 with true n/date/scores | YES for 20 indexed CSL results each; independent complete corroboration still open |
| Both sides today's confirmed XI/keeper/bench | NO: LINEUP_UNCONFIRMED |
| Both sides' current absences | PARTIAL: direct press conference for Beijing; stale/unverified Qingdao reports |
| Season-specific 1H and corner source endpoint | YES at aggregate level, conditional on provider; exact xG and corner covariance unavailable |
| Coherent hand marginal probabilities / full win-draw-loss | YES approximated, not calibrated; sport model no code executed |
| All six user O/U directions | YES, four primary-eligible ranked and first-half pair separately documented; family exclusion disclosed |
| Family/gates / joint top-two failure | first-half Rank1 NOT ELIGIBLE; Rank1 GATE_UNRESOLVED_PRECISION; joint bounded not point-estimated |
| Same-line frozen league-only baselines | NO, source event-date cohort insufficient, no .50 fill |
| Unperformed model/odds/retrospective/settlement | NONE |
| Active mini writer/issue/canonical import | DRAFT_NOT_APPLIED / NOT_IMPORTED / NO CANONICAL ID |
| Overall | `RESEARCH_RETAINED / UNCALIBRATED / UNVERIFIED_LINEUPS / LEAGUE_BASELINE_OPEN / DRAFT_ONLY` |

<!-- END CARD LOCAL-20261018MELILL01-G0004 -->

# RUNNING FOOTER
<!-- BEGIN FOOTER -->
| Field | Value |
|---|---|
| Last provisional local key / next proposed key | `LOCAL-20261018MELILL01-G0004` / `LOCAL-20261018MELILL01-G0005`; proposed namespace only, **no verified active mini was edited** |
| Canonical IDs assigned | **NONE**; only prompt 4 can assign them after verified local-to-canonical mapping |
| Repo next canonical snapshot | P-601, contextual read-only value at pinned `3e29a58693e2ed02ff862e9bf0f751af2feadee1` |
| Draft cards / model lane | **4 cumulative research draft cards** (Melbourne–Illawarra; Pakistan–Sri Lanka; ŽBK KP–Žabiny B; Beijing–Qingdao) / uncalibrated manual analysis; **0 verified issued** |
| Research requests / intake | 4; all original earlier card bodies preserved |
| Open unresolved queue | 13 queue items, including prior KP B identity conflict and current exact XI, league baselines/corners correlation |
| Eligibility notes | Beijing 1H Over0.5 estimated .685 but excluded from rank1 by soccer p≥.72 family rule; remaining Rank1 corners Under10.5 .645 has `GATE_UNRESOLVED_PRECISION`; no certified ranking |
| Mode / lease | LOCAL_MINI_STAGING as self-contained **DRAFT_NOT_APPLIED** / actual original and issuing writer lease NOT_VERIFIED |
| Reconciliation | Check unpublished active original and duplicate map before importing; this is not a GitHub commit or active-mini issuance |
| All GitHub/Drive writes | NONE |
| Sports ML/RL/model code execution | NONE; hand probability arithmetic only (file assembly does not run a sport model) |
| Settlement or retrospective performed | **NO** |
<!-- END FOOTER -->
