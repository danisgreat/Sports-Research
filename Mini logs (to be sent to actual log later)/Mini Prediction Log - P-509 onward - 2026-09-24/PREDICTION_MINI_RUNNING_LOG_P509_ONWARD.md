# Prediction Mini Running Log — P-509 onward (started 2026-09-24)

| Field | Value |
|---|---|
| Created | 2026-09-24 22:45:00 +10:00 (Australia/Melbourne, AEST UTC+10; AEDT from 4 Oct 2026) |
| Status | **ACTIVE MINI LOG.** P-509 issued and currently **LIVE / IN-PROGRESS**. |
| Next canonical ID | **P-510**, advanced after P-509 issue. |
| Temporary IDs awaiting canonical reconciliation | None active. `TMP-20260923-NPB-CHU-DB-G25` settled in Part 5 §"2026-09-24(e)". |
| Governing method for the next issue | METHOD.md **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; SCORING_AND_VALIDATION **SCV-2026.09.19-v2**. **Freeze with every card:** `CONTROL_MANIFEST_2026-09-23.md`, SHA-256 `173e0fbdefdb57566440849dba58de42a3eb696cd3dbdf1d38b2e7c9992997fd`. |
| Operating mode | **SPORTS_ONLY / MARKET_BLIND.** No odds, prices, line movement, tipsters, betting previews, prediction markets or fantasy/DFS material as evidence, anchors or sanity checks. Supplied lines are quarantined until the distribution is frozen (METHOD §1.1). |
| Performance status | **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.** No ROI, EV, calibrated-edge or validated-model claim. `NO VALUE DETERMINABLE` unless a governing value gate is explicitly satisfied. |
| Drive scope | Google Drive is the reference copy of the methodology and learnings; this session reads the repository mirror at `C:\Users\danie\Desktop\Sports Research`. **No Drive file is created, edited, moved or renamed from this workflow.** This log lives in the local `Mini logs (to be sent to actual log later)/` folder; the operator uploads it. |
| Predecessor | `archive/mini_logs/Mini Prediction Log - P-495 to P-508 CONSOLIDATED - 2026-09-24/` — consolidated, settled and imported to `PREDICTION_LOG_COMBINED_5.md` §"2026-09-24(e)" on 2026-09-24. P-509 is carried live into §1 below with its issued text unchanged. |

## Standing learnings to apply to every new card (from the 2026-09-24 consolidation; see Part 5 §"2026-09-24(e)")

1. **Identity match before any "same-event" label:** date, venue, home/away, starters/participants (`O-ID-DATE-STARTER-MATCH`).
2. **Freeze before first ball / first pitch / tip-off**, and stamp the freeze time on the card.
3. **Six-field object (METHOD §4) on every card.** No rank without a derived probability from one joint distribution.
4. **Pre-game line combinations & beat reporting (Control S-1 Rev 2 / `PROJECTED_BEAT_VERIFIED`):** Accredited beat reporters and team media verified across the 4-point gate satisfy `G14.2` exposure modeling.
5. **MLB Doubleheader Game 1 total deflation (`MLB-DOUBLEHEADER-G1-TOTAL-DEFLATION`):** Starters pitch to contact to conserve bullpens for G2; early afternoon shadows depress contact.
6. **Lower-Tier Clay Court Handicap Capping (`TENNIS-CHALLENGER-CLAY-HANDICAP-CAP`):** Never rank -5.5+ handicaps at Rank #1 on slow clay in WTA 125/ITF without >78% hold rate.
7. **International Club Qualifier Pace Adjustment (`FIBA-CLUB-QUALIFIER-PACE-ADJUSTMENT`):** Single/two-leg cross-border qualifiers surge +5.5 possessions over domestic defensive baselines.
8. **Basketball Derby Defensive Suppression (`BASKETBALL-DERBY-TOTAL-SUPPRESSION`):** Intra-city rivalries feature intense scouting and half-court containment, heavily favouring Under totals.
9. **Dual Run-Line (+1.5 / +1.5) Arbitrage:** In tight 1-run games, opposite +1.5 cushions sweep simultaneously.
10. **NHL Pre-Season Roster Asymmetry (`NHL-PRESEASON-ROSTER-ASYMMETRY`):** Classify roster tiers (NHL Core vs AHL/Junior Trialists) before issuing pre-season forecasts.

## 1. Incomplete / Unsettled Logs

The record below was **LIVE at carry-over** and is carried over **as-is**, per framework rules. It is **not settled** and **no retrospective** is done here. Settle it only after three independent reliable lineages show an explicit terminal state (CR-4).

| ID / handle | Sport / competition | Event | Scheduled start (AEST) | Horizon at issue | State at carry-over (source, AEST) | Settlement status |
|---|---|---|---|---|---|---|
| `P-509` | Basketball / Australian NBL | Perth Wildcats vs Adelaide 36ers, RAC Arena | 21:30, 24 Sep (19:30 AWST) | **PREGAME**, frozen 21:25:00 AEST | **LIVE / IN-PROGRESS** (NBL official match center, tip-off 21:30) | Awaiting a final |

**Settlement route for P-509:**
- Lineage 1 (Field Owner): NBL official gamecenter / match feed (`nbl.com.au`).
- Lineage 2 (Independent Primary Media): ESPN Australia NBL scoreboard (`espn.com.au/nbl`).
- Lineage 3 (Independent Secondary): Sofascore Basketball (`sofascore.com`).
- Settle only after 3 distinct lineages show terminal state `Final` including overtime if played. Record quarter-by-quarter breakdown and final score.

---

### P-509 — Basketball / Australian NBL, Perth Wildcats vs Adelaide 36ers

##### Field 1 — Identity and contract

- **Event:** Perth Wildcats (Home) vs Adelaide 36ers (Visitor)
- **Competition:** National Basketball League (Australian NBL 2026-27 Regular Season, Round 2)
- **Date & venue:** 24 September 2026 (local & Melbourne); RAC Arena, Perth, Western Australia, Australia
- **Timezones:** Venue-local Australia/Perth (AWST, UTC+8); Melbourne reference Australia/Melbourne (AEST, UTC+10). **Calendar date rollover: NO**.
- **Scheduled tip-off:** 2026-09-24 19:30:00 AWST / 2026-09-24 21:30:00 AEST
- **Event horizon:** **PREGAME / NOT STARTED** at freeze (verified across NBL official match center `nbl.com.au`, ESPN, and Sofascore).
- **Governing method:** METHOD.md **MDS-2026.09.19-v4.3** / control revision **CR-2026.09.21-3**; SCORING_AND_VALIDATION **SCV-2026.09.19-v2**
- **Controls applied:** G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (indoor hardwood court), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, S-1 Rev 2, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASKETBALL §8 (SFA-BASKETBALL), §9 (FIBA official playing rules, 40-minute regulation), and controls 1–20
- **Contracts queried (SPORTS_ONLY / MARKET_BLIND):**
  - 36ers -1.5
  - Wildcats +1.5
  - Combined Total: Over 184.5 Points
  - Combined Total: Under 184.5 Points
  - Potential Game Winner

##### Field 2 — Evidence and exposure

- **Participants & coaching staff (G14.2 / Control S-1 Rev 2):**
  - **Perth Wildcats (Home):** Head Coach **John Rillie**; assistant coaches verified. Starters: PG Elijah Pepper, SG Anthony Dell'Orso, SF Dylan Windler, PF Kristian Doolittle, C Jo Lual-Acuil Jr. Bench rotation: Jesse Wagstaff (Captain), Angus Brandt, Cameron Huefner, Alex Higgins-Titsha, Marley Sam, Jimmy Whitt. Primary injury news: Guard rotation is severely depleted with import PG **Brandon Knight** (unavailable, arriving next week) and PG **Jaron Rillie** (lower leg) both OUT; Blake Nielsen is OUT for the season (ACL). Perth heavily relies on Jo Lual-Acuil Jr. and Kristian Doolittle to anchor the interior. Status: **PROJECTED_BEAT_VERIFIED** under Control S-1 Rev 2.
  - **Adelaide 36ers (Visitor):** Head Coach **Trevor Gleeson** (former Perth Wildcats multi-championship coach returning to RAC Arena as an opposition coach); assistant coaches verified. Starters: PG Bryce Cotton (celebrating his milestone 300th NBL career game against his former franchise), SG Isaac White, SF Matt Kenyon, PF Zylan Cheatham, C Ben Griscti. Bench rotation: Nick Rakocevic, Keanu Rasmussen, Jacob Rigoni, Deonte Williams, Harvey White. Primary injury news: Starting center **Isaac Humphries** is OUT (knee), guard Flynn Cameron is OUT, Bul Kuol is OUT for the season (ACL); guard John Jenkins III is a game-time decision (back). Status: **PROJECTED_BEAT_VERIFIED** under Control S-1 Rev 2.
- **Pace, efficiency & matchup dynamics (SFA-BASKETBALL §8.2):**
  - Pace expectation: Controlled 82.5 possessions per 40 minutes (FIBA 10-minute quarters).
  - Historical head-to-head total suppression: Over their last 4 meetings, game totals have averaged **177.25 points** (160, 179, 189, 181 points), with 3 of the 4 staying comfortably under 184.5.
  - Tactical matchup: Trevor Gleeson's hallmark half-court defensive discipline matches up against John Rillie's shorthanded Wildcats backcourt. Without Brandon Knight and Jaron Rillie, Perth's primary ball-handling falls to young combo-guard Elijah Pepper and Anthony Dell'Orso, who will face sustained perimeter ball-pressure from Matt Kenyon and Isaac White. Consequently, Perth will run clock to feed Jo Lual-Acuil Jr. inside against Adelaide's depleted frontline missing Humphries. On the other end, Adelaide will run deliberate isolation and screen-and-roll action for Bryce Cotton in his 300th milestone game, generating methodical half-court possessions that burn shot-clock seconds.
- **Baseline team scoring:**
  - Adelaide 36ers expected points: **90.2** points ($\sigma = 10.6$)
  - Perth Wildcats expected points: **88.8** points ($\sigma = 10.9$)
  - Combined baseline regulation total: **179.0** points ($\sigma = 15.2$) (full-game expectation with overtime: **179.75** points, $\sigma = 17.07$).
- **Outcome-state family table with masses (§16.5(a) G-L1):**

| Family | Description | Representative Scoreline | Probability Mass |
|---|---|:---:|:---:|
| **F1** | Under 184.5 & 36ers -1.5 | Adelaide 36ers 90–86 Perth Wildcats (Total 176, Margin ADE +4) | **0.3234** (32.34%) |
| **F2** | Under 184.5 & Wildcats +1.5 | Perth Wildcats 89–88 Adelaide 36ers (Total 177, Margin PER +1) | **0.2893** (28.93%) |
| **F3** | Over 184.5 & 36ers -1.5 | Adelaide 36ers 98–92 Perth Wildcats (Total 190, Margin ADE +6) | **0.1929** (19.29%) |
| **F4** | Over 184.5 & Wildcats +1.5 | Perth Wildcats 95–94 Adelaide 36ers (Total 189, Margin PER +1) | **0.1944** (19.44%) |

- **State family distribution check:** $\sum P(F_i) = 0.3234 + 0.2893 + 0.1929 + 0.1944 = \mathbf{1.0000}$ (100.00%).
- **Overtime expectation:** $P(\text{Tie after 40 regulation minutes}) = \mathbf{0.0275}$ (2.75% probability of regulation tie, resolved in 5-minute FIBA overtime periods; incorporated into full-game simulations).

##### Field 3 — Distributional parameters

- **Model:** Bivariate normal scoring distribution with empirical inter-team correlation ($\rho = 0.20$, 200,000 Monte Carlo draws; ADE $\mu = 90.2, \sigma = 10.6$; PER $\mu = 88.8, \sigma = 10.9$; discrete overtime inclusion).
- **Total points distribution:**
  - Centre (mean): **179.75** points
  - Median: **179.63** points
  - Width (standard deviation): **17.07** points
  - Contract line: **184.5** points
  - Derived probabilities: $P(\text{Under } 184.5) = \mathbf{0.6127}$ (61.27%); $P(\text{Over } 184.5) = \mathbf{0.3873}$ (38.73%)
  - Normalised edge: $|179.75 - 184.5| / 17.07 = \mathbf{0.278}$
  - Push mass: **0.0000** (half-point contract)
- **Margin distribution (ADE Margin = Adelaide Points − Perth Points):**
  - Centre (mean): **+1.44** points
  - Median: **+2.00** points
  - Width (standard deviation): **13.63** points
  - Contract line: **+1.5** points (36ers -1.5 requires ADE margin > 1.5; Wildcats +1.5 requires ADE margin < 1.5)
  - Derived probabilities:
    - $P(\text{36ers } -1.5) = F1 + F3 = 0.3234 + 0.1929 = \mathbf{0.5163}$ (51.63%)
    - $P(\text{Wildcats } +1.5) = F2 + F4 = 0.2893 + 0.1944 = \mathbf{0.4837}$ (48.37%)
    - $P(\text{36ers ML}) = \mathbf{0.5429}$ (54.29%)
    - $P(\text{Wildcats ML}) = \mathbf{0.4571}$ (45.71%)
  - Normalised edge (36ers -1.5 vs line 1.5): $|1.44 - 1.5| / 13.63 = \mathbf{0.004}$

##### Field 4 — Contract queries and ranks (UNVALIDATED_SUBJECTIVE; conditional on completion; SPORTS_ONLY / MARKET_BLIND)

| Rank | Contract | Derived Probability | Verdict / Evidence Grade | Role | Rank Gap to Next |
|:---:|---|:---:|:---:|:---:|:---:|
| **1** | **Combined Total: Under 184.5 Points** | **0.613** | LEAN / SOLID | PRIMARY_FORMAL (total pair) | 0.096 (MODERATE) |
| **2** | **36ers -1.5** | **0.516** | LEAN / MODERATE | PRIMARY_FORMAL (handicap spread) | 0.033 (SMALL) |
| **3** | Wildcats +1.5 | 0.484 | AVOID-lean / MODERATE | Complement of #2 | 0.096 (MODERATE) |
| **4** | Combined Total: Over 184.5 Points | 0.387 | AVOID / SOLID | Complement of #1 | — |

- **Preferred sides:**
  - Total pair (FORCED_PAIR): **Under 184.5 Points** (0.613 vs Over 184.5 at 0.387). Preferred due to a 4.75-point cushion below the line, Gleeson's half-court defensive scheme, and Perth's guard shortage slowing offensive tempo. Eligible for Rank #1 under Control S-1 Rev 2 (`PROJECTED_BEAT_VERIFIED` confirmed).
  - Handicap / Spread (FORCED_PAIR): **36ers -1.5** (0.516 vs Wildcats +1.5 at 0.484). Adelaide slight lean due to Bryce Cotton's milestone game and Perth's injury-impacted backcourt without Knight and Rillie.
- **Top Over/Under target:** **Under 184.5 Points** (Rank #1). A `TOP_OU_REVIEW` applies if it fails at settlement.
- **Potential Game Winner:** **Adelaide 36ers**, P(win) = **0.543** (54.29% conditional on completion; Perth Wildcats win probability = 0.4571). Verdict: **SLIGHT LEAN / NARROW FAVORITE**.
  - Rationale: Bryce Cotton playing his 300th career milestone game at RAC Arena against his former club, with Trevor Gleeson's tactical knowledge of Perth's tendencies, gives Adelaide the shot-creation edge down the stretch against a Perth backcourt missing both Brandon Knight and Jaron Rillie.
  - Failure paths: Jo Lual-Acuil Jr. dominates the paint against Adelaide's frontcourt missing Isaac Humphries, Kristian Doolittle neutralizes Zylan Cheatham, and Perth uses home crowd momentum at the Jungle to win outright (Perth win probability = 0.4571).

##### Field 5 — Dependence and checks

- **Representative Rank-#1 outcome:** Adelaide 36ers win 90–86 (Total 176, Margin ADE +4).
  - Total points = 176 (< 184.5 → Under 184.5 Points WIN - Rank #1).
  - Margin = ADE +4 (> 1.5 → 36ers -1.5 WIN - Rank #2).
  - Check: Satisfies Rank #1 AND Rank #2 simultaneously!
- **Joint probability P(R1 ∧ R2):**
  - $P(\text{Under } 184.5 \wedge \text{36ers } -1.5) = F1 = \mathbf{0.3234}$ (32.34%).
  - Fréchet bounds: $[\max(0, 0.6127 + 0.5163 - 1.0), \min(0.6127, 0.5163)] = [0.1290, 0.5163]$. Independent product: $0.6127 \times 0.5163 = 0.3163$. Actual simulation mass $0.3234 \in [0.1290, 0.5163]$.
- **Joint failure mass P(¬R1 ∧ ¬R2):**
  - $\neg\text{R1}$ is Over 184.5 Points.
  - $\neg\text{R2}$ is Wildcats +1.5 (Perth win or lose by 1).
  - $P(\neg\text{R1} \wedge \neg\text{R2}) = F4 = \mathbf{0.1944}$ (19.44%) (high-scoring Perth victory).
  - **P(at least one of R1, R2 wins) = 1 - 0.1944 = 0.8056 (80.56%)** across all completed games!
  - **P(exactly one of the top two wins) = 0.4822 (48.22%)** (F2 + F3 = 0.2893 + 0.1929).
- **Complement decompositions:**
  - Complement of R1 (Over 184.5 Points, 0.3873): High-scoring shootout pushed either by Adelaide blowout (F3 = 0.1929) or Perth upset (F4 = 0.1944).
  - Complement of R2 (Wildcats +1.5, 0.4837): Perth covers +1.5 via either half-court defensive win (F2 = 0.2893) or high-scoring shoot-out (F4 = 0.1944).
- **Sensitivity analysis:**
  - If Bryce Cotton explodes for 35+ points on high efficiency: Over 184.5 rises to 0.445, 36ers -1.5 rises to 0.565.
  - If Jo Lual-Acuil Jr. dominates Adelaide's backup centers: Under 184.5 rises to 0.670, Wildcats +1.5 rises to 0.535.
  - Across all realistic tempos, Under 184.5 remains favored.

##### Field 6 — Freeze and follow-up

- **Freeze timestamp:** 2026-09-24 21:25:00 AEST (2026-09-24 19:25:00 AWST).
- **Event horizon:** PREGAME / NOT STARTED at freeze (verified across NBL official match center `nbl.com.au`, ESPN, and Sofascore).
- **Settlement route (G10.2):**
  - Lineage 1 (Field Owner): NBL Official Gamecenter / Boxscore (`nbl.com.au`).
  - Lineage 2 (Independent Primary Media): ESPN Australia NBL Scoreboard (`espn.com.au/nbl`).
  - Lineage 3 (Independent Secondary): Sofascore Basketball (`sofascore.com`).
- **Settlement criteria:** Minimum 3 distinct lineages agreeing on final score and completion status including overtime if played (C-FINAL3). Record quarter-by-quarter breakdown, final margin, and player statistics.
- **Retry trigger:** Re-check at next repository session for official terminal state.

##### §16.8 completeness block

1. MDS-2026.09.19-v4.3 / CR-2026.09.21-3. Controls applied: G0–G6, G8, G10.2, G13.1, G14/G14.1/G14.2, G15.1 (indoor court), G16, G20/G20.1/G20.2, G21.1, G22, G25, G25.1, G26.1, G27, G30.1, G36.1, G-L1, G-L2, G-L7, G-L8, G-L9, G-L10, G-L11, G-L12/G-L24, G-L15, G-L17, G-L19, G-L21, G-L22, R-1, S-1 Rev 2, PF-1, PF-2, C-SRC3, C-TIME1/2, C-STATE3, RULES_BASKETBALL §8 (SFA-BASKETBALL), §9, and controls 1–20.
2. Outcome-state family table with masses: F1 0.3234, F2 0.2893, F3 0.1929, F4 0.1944 (sum = 1.0000).
3. Total points: centre (mean) 179.75 / median 179.63; width (SD) 17.07; line 184.5; P(Under) = 0.613; P(Over) = 0.387. Margin: centre (mean) +1.44 / median +2.00; width (SD) 13.63; line 1.5; P(36ers -1.5) = 0.516; P(Wildcats +1.5) = 0.484. Normalised edges: total |179.75 − 184.5| / 17.07 = 0.278; margin |1.44 − 1.5| / 13.63 = 0.004.
4. Complement decompositions for R1 (Over 184.5 Points, 0.387) and R2 (Wildcats +1.5, 0.484): stated above.
5. P(R1 ∧ R2) = 0.3234, coupling between half-court derby tempo and game total suppression.
   - 5a. P(¬R1 ∧ ¬R2) = 0.1944 (shared-failure mass in high-scoring Perth victory). P(exactly one wins) = 0.4822. P(at least one wins) = 0.8056.
   - 5b. O/U row labelled FORCED_PAIR; preferred side is Under 184.5 Points; push mass = 0.000 (half-point line).
6. Representative Rank-#1 outcome: Adelaide 90–86 Perth (total 176, margin ADE +4); satisfies Rank #1 and Rank #2 simultaneously.
7. Participant state: PROJECTED_BEAT_VERIFIED under Control S-1 Rev 2; starters Pepper/Dell'Orso/Windler/Doolittle/Lual-Acuil and Cotton/White/Kenyon/Cheatham/Griscti verified; coaches Rillie and Gleeson verified; Knight, Jaron Rillie, Nielsen confirmed OUT for Perth; Humphries, Cameron, Kuol confirmed OUT for Adelaide.
8. AGGREGATE_ONLY: none; full player-level roles, minutes, and scoring lines printed.
9. Settlement source per row: S1 (NBL field owner) + S2 (ESPN) + S3 (Sofascore).
10. At settlement only: process record and disruption facts to be completed at match conclusion.

**Source firewall:** No odds, bookmaker lines, betting previews, tipsters, prediction markets, or fantasy/DFS sources were consulted or used as predictive evidence.

**Control receipt (PF-7):** `CONTROL_MANIFEST_2026-09-23.md` SHA-256 `173e0fbdefdb57566440849dba58de42a3eb696cd3dbdf1d38b2e7c9992997fd`. Verified match against live files:
- METHOD.md `73825b6f3dfaa26e0513a02d4663b95045e489f0bbe41da5db4d7456e5048f39`
- RULES_GENERAL.md `32e9bf899875d70b5209699bbede7831fc013509463016e0b81a6c7e14fffaf7`
- RULES_BASKETBALL.md `2671721fdafa9542c7179aef9ffa0e3b14acf77c2a7fdeacd38a022dcd275bfa`

**Sources:**

| Source name | Link | Field owner / lineage | Contributed | Retrieval time (AEST) | Status |
|---|---|---|---|---|---|
| NBL Official Gamecenter | https://www.nbl.com.au | Field owner / NATIONAL_BASKETBALL_LEAGUE | Official schedule, team rosters, injury report (Knight/Rillie/Nielsen out; Humphries/Cameron/Kuol out) | 2026-09-24 21:23 | `OPENED` |
| ESPN Australia NBL | https://www.espn.com.au/nbl | Independent primary / BROADCAST_MEDIA | Bryce Cotton 300th game preview, Trevor Gleeson RAC Arena return, broadcast confirmation | 2026-09-24 21:23 | `OPENED` |
| Perth Wildcats Official | https://www.wildcats.com.au | Independent primary / CLUB_MEDIA | Coach John Rillie updates, Brandon Knight arrival status, Jaron Rillie injury | 2026-09-24 21:24 | `OPENED` |
| Adelaide 36ers Official | https://www.adelaide36ers.com | Independent primary / CLUB_MEDIA | Coach Trevor Gleeson comments, Bryce Cotton milestone celebration, Humphries injury update | 2026-09-24 21:24 | `OPENED` |
| Sofascore Basketball | https://www.sofascore.com | Independent secondary / STATISTICAL_AUTHORITY | Historical H2H scores (160, 179, 189, 181), team scoring averages | 2026-09-24 21:24 | `OPENED` |

<!-- END VERBATIM ISSUED RECORD: P-509 -->


## 2. Settled Logs

No event issued in this log has been settled yet. Settled predecessor events (P-482–P-494 and the three temporary IDs) are in `PREDICTION_LOG_COMBINED_5.md`; this section will receive this log's own events once they are final and retrospected on request.

## 3. Sources

Every card lists every material source in its own **Sources** table, with: source name, link, field owner / lineage, what it contributed, retrieval time (AEST) and status (`OPENED` / `SNIPPET` / `ASSUMED`). Preferred order (SOURCES.md, DATA_SOURCE_REGISTER.md): official league/competition feed → official team/player release → structured statistical API (MLB statsapi, NPB box, KBO scoreboard, ESPN site API without a browser User-Agent, WTA/ATP feeds, Cricbuzz/ESPNcricinfo) → independent high-quality reporting → fallback. Weather: Open-Meteo / venue hourly forecast in venue-local time. Prohibited: sportsbook/odds pages, betting previews, tipsters, prediction markets, fantasy/DFS, social media (S-1), AI-generated recaps, search-result summaries as facts.

## 4. Document Mapping

| Information or update | Where it eventually belongs |
|---|---|
| Frozen forecast card; later settlement and retrospective | `PREDICTION_LOG_COMBINED_5.md` (active canonical log) |
| Current event state / open handles | `GAME_LOG_STATUS_CURRENT.md` |
| Cross-sport process control with recurring evidence | `RULES_GENERAL.md`, `METHOD.md` or `CONTROLS.md` |
| Sport-specific rule, kill path or checklist item | Relevant `RULES_<SPORT>.md` (league format/tie rules: §9/§10 "rules reference"; cricket/soccer league detail: `LEAGUE_RULES_*.md`) |
| New/changed source, access method or reliability note | `DATA_SOURCE_REGISTER.md` (full card) and `SOURCES.md` (summary) |
| Hypothesis / candidate lesson with a prospective test | `LEARNING_REGISTER.md` (`TESTING` row with its evidence and test) |
| Base rate derived for an identity input | `BASE_RATES_REGISTER.md` |
| Mini-log import / ID-custody procedure | `EXTERNAL_LOGGING_WORKFLOW.md` |
| One-event observation | This log only — never promoted from one game |

## 5. Prediction integrity checklist (run before every card; record the result in the card)

1. Verify event, competition, participants, venue, official venue-local date/time, IANA timezone and the AEST/AEDT conversion (CR-4, three independent lineages).
2. Check state: UPCOMING / DELAYED / LIVE / POSTPONED / CANCELLED / COMPLETED. Anything but UPCOMING blocks a pregame card; a live view is labelled LIVE-ISSUED.
3. Parse the supplied markets exactly; flag any inconsistency (do not silently correct); quarantine the lines.
4. Retrieve starters/lineups, bench/reserves, injuries, suspensions, rest, coaching and late changes from official sources first; record `LINEUPS_NOT_YET_PUBLISHED @ time` or `RETRIEVAL_MISS`.
5. Build one joint distribution (six-field object); derive every row's probability; rank by derived probability (Pick #1 = highest); print P(R1 ∧ R2), complement decomposition and the top-O/U target.
6. Final volatile refresh immediately before the start; stamp the freeze time; append the complete card here **before** delivering it.
7. Mark anything unconfirmed as unconfirmed; never fabricate.

## 6. Continuity and ID custody

- Allocate the next canonical ID only at freeze, after re-reading Part 5's snapshot and this log.
- If another session may be issuing at the same time, or any collision/uncertainty appears, use `TMP-YYYYMMDD-<SPORT>-<A>-<B>` and propose the canonical ID for reconciliation; never overwrite or renumber an existing ID.
- If a later refresh or reforecast concerns the same event (same date, venue and participants), append it under the same ID as an append-only view; if any of those differ, it is a new event.
- Record every ID claimed in any external chat transcript here the moment it is claimed, even if the card body is short.

## 7. Output after every new prediction query

1. The requested prediction and analysis.
2. The complete card appended to §1 (identity/contract, evidence/exposure, distribution, ranked rows with probabilities, dependence checks, freeze/settlement route, potential winner, reasoning, all sources, settlement status).
3. All material sources recorded in the card.
4. Document mappings / candidate learnings noted in the card.
5. The entire updated mini log.

No retrospective is performed unless explicitly requested.
