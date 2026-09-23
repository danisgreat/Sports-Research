# Ice hockey analysis rules


> **2026-09-12 operational correction:** The dated section at the end of this file and RULES_GENERAL section 16.9 control over conflicting older probability, coupling and source claims.


> **`METHOD.md` is now the primary mandatory read (v4.0 comprehensive overhaul, 2026-09-06).** This file remains the full sport-specific reference: its `SFA-<SPORT>` algorithm and competition-rules section (`§9`/`§10`/`§11`) are consulted in full when forecasting this sport; `METHOD.md` states the cross-sport process once.


<!-- THREE-SOURCE-TIME-GATE-2026-09-19-CR4 -->
> **Current cross-sport authority — MDS-2026.09.19-v4.3 / CR-2026.09.21-3:** this sport module inherits the reconciled all-sports source, timing, settlement and distribution-construction controls. Historical issued cards retain their own revision.


Status: **ACTIVE**
Effective: **2026-09-06 (v4.0 comprehensive overhaul — see METHOD.md and FRAMEWORK_AND_GAME_LOG_OVERHAUL_REVIEW_2026-09-06.md)**
Method version: **MDS-2026.09.06-v4.0**
Applies with RULES_GENERAL.md, MODEL_AND_DATA_SPEC.md, ALGORITHM_PORTFOLIO_AND_EVALUATION.md, and NUMERICAL_TRAINING_SPEC.md.
Executable algorithm: **SFA-ICE-HOCKEY (§8) — instantiates GFA-2 in RULES_GENERAL.md §11**
Numerical training specification: **NTS-2026.09.02-v0.3 — design only; no ice-hockey model is fit**
Sport and competition rules reference: **§9 (added 2026-09-04)** — the rules of ice hockey and the NHL / IIHF rule differences, plus per-competition rules for the ice-hockey competitions in the prediction logs (AIHL — note the 15-minute periods and Goodall Cup finals; Danish Metal Ligaen). Reference material for identity, state and settlement; it does not change `SFA-ICE-HOCKEY`.
Evidence density: **SPARSE** (added 2026-09-06, `L-099`, external blindspot audit `B-13`) — this sport has markedly fewer settled cards in this log than baseball, soccer or cricket. Every identity/state/contract/source/coherence gate applies at full force regardless; any *directional or magnitude* claim in this file is held to lower confidence than an equivalent claim in a `DENSE` sport and may not be promoted `PROMOTED_PROCESS` on one or two cards alone.


This module covers NHL and other ice-hockey competitions only after their rules, data and scoring populations are separated. It does not authorise an NHL probability model.


## 1. Identity and contract


Resolve competition, season/rules era, venue, home/away/neutral status, scheduled start, regulation versus overtime/shootout endpoint, tie/draw availability, puck-line/total/team/player/period target, goalie/action terms and provider statistic.


The following are distinct contracts and targets:


- regulation three-way result;
- moneyline including OT/SO;
- regulation score/total;
- full-match score as defined by the operator, including any shootout accounting convention;
- period target;
- team/player shots, points, saves and other provider events.


A completed period or settled player-action condition at issue is handled under the general SETTLED_AT_ISSUE rule.


## 2. High-value inputs


### Participants and exposure


- Confirm projected and, when available, official line combinations, defence pairs, power-play/penalty-kill units and scratches.
- Treat starting goalie as a regime variable. Model start probability, recent workload/rest, injury/return state, replacement quality and pull risk.
- Estimate skater ice time, line/unit role, shift distribution and special-teams exposure. Active does not guarantee normal minutes or role.
- Record back-to-back/rest, travel, altitude, venue and roster/coach/system changes.


### Shot and goal process


Use opponent- and manpower-adjusted:


- shot attempts, unblocked attempts and shots on goal under the named definition;
- shot location/angle/type, pre-shot movement/rebound context and expected-goal quality where provider-defined;
- finishing talent with shrinkage;
- goaltending/save quality and shot mix;
- offensive-zone/transition/forecheck process where available;
- power-play and penalty-kill opportunities/efficiency;
- penalties, score state, pulled-goalie and empty-net behavior.


Raw recent goals, save percentage, head-to-head and one hot/cold streak are outcomes, not stable rates without mechanism and opponent adjustment.


## 3. Model


Exposure units are regulation minutes, shifts, ice time, shot attempts/chances, shots on goal and manpower-state possessions. Estimate shot/chance intensity and quality first, then finishing/goaltending, special teams and empty-net branches.


Use a joint regulation goal distribution. Link it to a separate rules-correct OT/SO result process for full-match moneylines. Derive regulation winner, totals, team totals and puck lines only from the target object matching their endpoint. Player shots/points/saves use their own participation × ice-time/opportunity × event-rate distributions linked to team/score/manpower state.


Numerical candidates begin with empirical and independent-Poisson diagnostics, then hierarchical bivariate/count distributions. The A2 candidate simulates shifts/shots, manpower state, goalies, score effects, penalties, pulled goalie, empty net, OT and shootout. Boosted/ordered score grids are challengers only after support, dispersion, covariance, tail, OOD and calibration checks. Every candidate is unfit and unvalidated.


## 4. Structural controls


1. **Goalie uncertainty is a scenario mixture.** Do not use a reported expectation as confirmed fact.
2. **Shots and goals are linked but not interchangeable.** Shot quality, finishing and goalie state mediate conversion.
3. **Blocked shots are definition-sensitive.** A dataset that omits them cannot control all-attempt metrics without reconciliation.
4. **Special teams change both exposure and rate.** Use current units and penalty environment; season percentage alone is incomplete.
5. **Score state changes pace and shot mix.** Trailing teams may create more attempts while allowing transition/empty-net risk.
6. **Empty-net goals are an explicit tail.** They affect totals and margins differently from five-on-five central play.
7. **Regulation and moneyline are different targets.** A regulation draw can proceed to OT/SO; never infer one contract mechanically from the other without the linked process.
8. **Back-to-back is mechanistic.** Connect rest to goalie choice, line workload, forecheck/transition and late-game quality.
9. **Player props require role and ice time.** Recent shots/points do not substitute for line, unit and matchup exposure.
10. **External xG/forecast models are challengers.** Cite their provider/method/version and never present them as internal probabilities.
11. **Shot volume is exposure, not a goal total.** A high SOG forecast or realised shot edge cannot by itself support an Over. The total rationale must separately represent shot quality, finishing shrinkage, confirmed/probable goalie mixtures, special teams and empty-net exposure.
12. **Sparse competitions retain a conversion cap.** When current goalie identity, shot quality or manpower context is unavailable, recent high-scoring results and raw SOG may describe the ceiling but cannot remove the low-conversion branch or justify false confidence.
13. **OT result geometry and operator settlement remain separate.** In sparse competitions, a verified overtime final can settle the research event path, but it does not establish whether a supplied moneyline, puck line or total included OT/SO or how shootout goals are counted. Preserve the regulation-draw/one-goal-OT branch and use `UNKNOWN_DEFINITION` until the named operator/action terms are available.
14. **Unconfirmed goalie blocks a fragile top-ranked total.** In early-season or sparse competitions, unresolved starting goalie identity normally prevents a total from Rank #1 unless unusually deep current defensive-process evidence survives every credible goalie mixture. One low-scoring opener, old H2H or unverified expected starter cannot remove the conversion tail.


## 5. Live state


Store score, period/clock, current manpower/penalties, goalie in net, shots/attempts and xG under named definitions, line/unit changes, injuries/ejections, timeouts, pull state and venue conditions. Rebuild remaining regulation exposure, goalie/pull/empty-net branches and any later OT/SO process; do not extrapolate elapsed goals per minute.


## 6. Sources and settlement


- NHL/competition official rules, match centres, roster/lineup/goalie reporting, statistics and finals control official facts.
- The [NHL hockey glossary](https://www.nhl.com/info/hockey-glossary) controls NHL official-stat definitions where applicable.
- [NHL projected lineups/goalies](https://www.nhl.com/news/topic/game-previews/nhl-projected-lineup-projections) is an official reporting lane but remains projected until confirmed.
- [MoneyPuck downloads](https://www.moneypuck.com/data.htm) and methodology may support specialist research only within current use/attribution terms. Its documented downloadable shot data omits blocked shots; do not silently treat it as all shot attempts.
- Other shot/xG/line providers control only their defined metrics after coverage, method, licence and correction checks.


Settle from the official final and named statistic provider, preserving regulation/OT/SO and shootout-score conventions. Retry official stat corrections for player props before UNSETTLEABLE.


## 7. Upcoming-game research sequence


1. Freeze competition/rules, regulation/full-match endpoint, goalie/action/stat-provider terms and complete candidate slate.
2. Retrieve official event/roster/injury state, projected goalie/lines and current specialist shot/process data; refresh confirmed goalie, scratches, lines/units and state immediately before puck drop.
3. Estimate regulation minutes/shifts, shots/chances by manpower and score state, shot quality, finishing, goalie/save distribution, penalties/special teams and pulled-goalie/empty-net branches.
4. Audit whether the total direction survives a high-shot/low-conversion branch and each unresolved starting-goalie branch.
5. Produce one regulation joint goal object and, where required, a linked OT/SO result object. Player props retain their own ice-time/opportunity target.
6. Derive and rank only contracts whose exact endpoints and definitions are resolved. Missing goalie confirmation widens scenarios; it does not authorise an invented starter or probability.


## 8. SFA-ICE-HOCKEY — sport forecast algorithm


Algorithm ID: `SFA-ICE-HOCKEY`. Effective **2026-09-02**. Instantiates `GFA-2` (RULES_GENERAL.md §11) with ice-hockey content. Process composition only; no fitted weight, scenario weight or published probability is introduced, and this section does not authorise an NHL or any other probability model. Each competition remains a separate rules, data and scoring population.


### 8.1 Blocking preconditions


| Precondition | Requirement | Failure output |
|---|---|---|
| `IH-P1` competition and endpoint | Competition, rules, period structure, overtime format, shootout treatment, and whether each supplied row settles on regulation or on the full match | `GATE-TARGET` failure. Regulation and full-match are different targets |
| `IH-P2` goaltender | Starting goalie for both sides with release status, plus replacement quality and pull risk, re-handshaken at G31 | Goalie mixture. In early-season or sparse competitions an unresolved starter normally prevents a total from Rank #1 |
| `IH-P3` operator terms | Whether the operator's moneyline, puck line or total includes overtime and shootout, and how a shootout goal is counted | `UNKNOWN_DEFINITION`; preserve the regulation-draw and one-goal-overtime branch |
| `IH-P4` metric definition | For shot or attempt rows, whether blocked shots are included under the named provider | A dataset that omits blocked shots cannot control an all-attempt metric without reconciliation |


### 8.2 Exposure chain


| Step | Output |
|---|---|
| `IH-S1` | Line combinations, defence pairs, power-play and penalty-kill units, scratches, and ice time by skater and unit |
| `IH-S2` | Regulation exposure: minutes, shifts and manpower states — even strength, power play, penalty kill, and late empty-net time |
| `IH-S3` | Shot and chance intensity by manpower and score state, under the named definition |
| `IH-S4` | Shot quality: location, angle, type, pre-shot movement and rebound context, where provider-defined |
| `IH-S5` | Conversion: finishing talent with shrinkage, goaltending and save quality against the actual shot mix |
| `IH-S6` | Special teams: penalty environment, opportunities and current unit efficiency, kept separate from season percentages |
| `IH-S7` | Late-state process: score effects, pulled goalie, empty net |
| `IH-S8` | One regulation joint goal object, and where required a separate rules-correct overtime and shootout result object |


Shot volume is exposure. It is never a goal total on its own.


### 8.3 Mandatory branch set


| Branch | Content |
|---|---|
| `IH-B1` | Central shot volume with central conversion for both sides |
| `IH-B2` | High-shot, low-conversion branch: a shot edge that does not become goals |
| `IH-B3` | Goalie-mixture branch: one branch per credible starter on each side, including the backup |
| `IH-B4` | Special-teams branch: a penalty-heavy state raising power-play exposure for both sides |
| `IH-B5` | Score-effect branch: a trailing side generating attempts while conceding transition chances |
| `IH-B6` | Pulled-goalie and empty-net branch, affecting totals and margins differently |
| `IH-B7` | Regulation-draw branch proceeding to overtime, then to a shootout where the format applies |
| `IH-B8` | Sparse or early-season branch: wide conversion tails retained when goalie identity, shot quality or manpower context is unavailable |


### 8.4 Contract derivation map


| Contract | Queried from | Extra condition the mechanism must predict |
|---|---|---|
| Regulation total | Regulation goal object | The component budget across both teams at the floor, centre and high, under every `IH-B3` goalie branch |
| Full-match total | Regulation object plus the overtime and shootout object | The exact operator counting rule for overtime and shootout goals |
| Puck line | Margin marginal, with the empty-net branch | Whether the endpoint includes overtime |
| Moneyline | The result object matching its endpoint | A regulation draw is not a loss on a full-match line |
| Team total | Team marginal | That team's own chances against the confirmed opposing goalie |
| Player props | `participation x ice time/opportunity x event rate` | Line, unit and matchup exposure, not recent shot or point counts |


### 8.5 Kill-path library


| Kill path | Defeats | Evidence origin |
|---|---|---|
| An unconfirmed starting goalie whose identity controls conversion | A top-ranked total in an early-season or sparse competition | §4 control 14, C-PL9-IH-GOALIE-TOTAL |
| A shot edge that does not convert | An Over ranked on projected or realised shots on goal | §4 control 11 |
| One low-scoring opener or old head-to-head across roster change | A total or margin centre placed on outcome history | §4 control 12 |
| A regulation tie resolved in overtime or a shootout | A margin row and a settlement assumption that never named the endpoint | §4 controls 7 and 13 |
| An empty-net goal late | An Under or a one-goal margin row with no late-state branch | §4 control 6 |
| Special-teams exposure changing both rate and opportunity | A total ranked on even-strength process and a season power-play percentage | §4 control 4 |
| A back-to-back changing goalie choice and line workload | A side ranked on team strength without a rest mechanism | §4 control 8 |


### 8.6 Sport ordering overrides


1. In an early-season or sparse competition, a total row may not be Rank #1 while `IH-P2` is unresolved, unless unusually deep current defensive-process evidence survives every credible goalie branch.
2. Regulation and full-match rows are different targets and never share a `states` count.
3. A shot or attempt row whose blocked-shot treatment is unreconciled is capped under RULES_GENERAL.md §11.5.
4. Pulled-goalie and empty-net states remain in both the total and the margin `states` counts.
5. Recent goals, save percentage, head-to-head and one hot or cold streak are `E — diagnostic only`.


### 8.7 Pre-issue checklist


1. `IH-P1`–`IH-P4` status printed, with goalie release status for both sides.
2. Competition and matchup goal baseline stated before any line.
3. Shot intensity, shot quality and conversion written as three separate layers.
4. All eight `IH-B*` branches represented; component budget solved at the supplied total.
5. Every total's direction audited against `IH-B2` and against each `IH-B3` goalie branch.
6. Kill-path rows selected from §8.5 and reconciled against the issued order.
7. Overtime and shootout treatment stated for every total, puck line and moneyline row.
8. Confirmed goalie, scratches, lines and state refreshed at G31 before the view is appended.
9. Recency block complete per §8.8: L5/L10/L15/L20 for both sides and for head-to-head, continuity count stated, trend verdict per metric, unique-event de-duplication done.
10. Environment block complete per §8.9: Venue classified indoor; travel, altitude and back-to-back entered through goalie choice and line workload.
11. `REFERENCE_BASE_RATE`, exact threshold, population and denominator recorded for every supplied row per §8.10 as a descriptive diagnostic only; no reference-band, trend or slot-frequency adjustment may move an ordinal (G23.1).
12. Extra-condition support audit (G24) recorded for every handicap, team-total and cushion row; no retrospective contract-family penalty is applied.
13. Separation budget (G20.1) solved for every margin, handicap and cushion row by period, with special-teams exposure, the empty-net state and the overtime/shootout endpoint held separately.
14. Rank-1 implied-target interval (G25.1) stated in the unit of every other supplied line, each remaining row classified `COHERENT`/`PARTIAL_OVERLAP`/`DISJOINT`, and every aggregate budget re-solved conditional on the Rank-1 state.
15. Winner-and-cushion reconciliation (G30.1) whenever Rank #1 is an underdog cushion, with the outright-win and narrow-loss branch ordering stated. Example separation kill path for this sport: an empty-net or special-teams swing.
16. Deficit attribution (G14.1) recorded for every weak, absent, returning or small-sample participant: which side's distribution moved and through which exposure step.


### 8.8 Recency, head-to-head and trend windows


Implements `GFA-2` step G13.1 (RULES_GENERAL.md §11.3B) and runs at that point in the algorithm, not at the end. Retrieval of L5/L10/L15/L20 for both sides and for the head-to-head series is mandatory; a window that does not exist is recorded with its true count and a missingness code.


Populate one windowed table per side with these metrics, and one head-to-head table:


| Window metric | Content |
|---|---|
| Shot and chance volume | Shot attempts and shots on goal for and against under the named definition, opponent-adjusted |
| Chance quality | Expected goals for and against where the provider defines them |
| Conversion | Shooting and save percentage, held separately from volume and shrunk |
| Special teams | Power-play and penalty-kill opportunities and efficiency, with the penalty environment |
| Goaltenders | Each credible starter's own last 5/10/15/20 starts: workload, save percentage and rest |


**Head-to-head continuity.** Continuity means the same goaltenders and comparable lines. A head-to-head record across a goalie change fails continuity, which is exactly the unresolved-starter failure recorded in the log.


**Descriptive recency windows (G13.1; revised 2026-09-17).** Retrieve L5/L10/L15/L20 and continuity-qualified H2H with unique-event counts. These windows overlap. Monotonicity and dispersion among their averages are not a statistical trend/noise test. Report direction descriptively; estimate recency decay and opponent/regime effects using time-ordered validation. See SCORING_AND_VALIDATION section 5.


**De-duplication.** The windows overlap by construction and share matches with the head-to-head and venue series. Shrink from unique underlying events under G9; never treat L5, L10, L15 and L20 as four confirmations.


### 8.9 Environment and conditions


Implements `GFA-2` step G15.1 (RULES_GENERAL.md §11.3C). Venue classification for this sport is normally **INDOOR**.


| Field | Use in this sport |
|---|---|
| Venue classification | Indoor; record it and move on |
| Travel, altitude and back-to-back | Entered through goalie choice, line workload and forecheck quality |


Failure to obtain the match-window forecast for an outdoor or open-roof event yields `WEATHER_NOT_AVAILABLE`, widened total and margin distributions, and a `LEAN` cap on every weather-dependent row. No factor above carries an automatic total direction.


### 8.10 Base-rate anchors and derived stat lanes


**Anchoring (G12.1).** Anchor regulation totals on the competition goal environment and full-match moneylines on the frequency of regulation ties proceeding to overtime. Regulation and full-match rows never share an anchor.


StatMuse is an accepted research accelerator for this sport under DATA_SOURCE_REGISTER.md §18, using the verified query patterns recorded there. Every returned row is date-checked and reconciled against the official league source before it is decision-driving, and StatMuse never controls participants, availability, rules, state or settlement.


**Derived and low-salience fields that are available and routinely skipped:**


| Field | Note |
|---|---|
| Blocked-shot treatment of the shot metric | A dataset that omits blocked shots cannot control an all-attempt claim |
| Empty-net and pulled-goalie behaviour | Its own branch at `IH-B6`, affecting totals and margins differently |
| Scheduled back-to-back goalie tendencies by club | Conditional; supports the `IH-B3` mixture |


## 9. Sport and competition rules reference


Added 2026-09-04; last reviewed 2026-09-04. Standing reference for the rules of ice hockey and the competition-specific rules of every ice-hockey competition in the prediction logs. Supports `IH-P` identity and §6 settlement; introduces no rate, weight or ordering rule. **Two facts dominate ice-hockey identity: the period length (the AIHL uses 15-minute periods, not 20) and the overtime/points regime, which differ by league and between regular season and playoffs.**


**Maintenance (RULES_GENERAL.md §3, `G2`).** Before the first card of a new AIHL or Metal Ligaen season, or the first playoff card, re-verify the period length, the points system, the regular-season vs playoff overtime/shootout rules, the import-player limits, the team count and the playoff bracket against the league source, and update this section **before** issuing the card — both leagues have changed team counts recently, and the AIHL's 15-minute-period and finals-weekend format are unusual and worth re-confirming each year. The first time another hockey competition is forecast (NHL, an IIHF event, another European league), document its full rules — periods, points, OT — here first.


### 9.1 The rules of ice hockey


**Rink and teams.** A rink ~60 m × 26–30 m with rounded corners and boards. **6 players a side** — 3 forwards, 2 defencemen, 1 goaltender — from a roster of ~20 skaters + 2 goalies. Unlimited "on the fly" line changes.


**Objective and scoring.** Shoot the puck into the opponent's net — every **goal = 1**. Most goals wins; a regulation tie goes to overtime (§9.2).


**Structure of play.** **Three periods** (length is league-specific — §9.3), with two intermissions and ends changed each period. The clock **stops** on every whistle (goals, offside, icing, penalties, puck out of play, goalie freeze). Face-offs restart play.


**Key violations.**
- **Offside:** an attacker precedes the puck over the opponent's blue line → face-off outside the zone.
- **Icing:** shooting the puck from behind the centre line all the way past the opponent's goal line untouched → face-off back in the offending team's zone, and (in most leagues) **no line change** for the offending team.
- **Penalties:** **minor** (2 min), **double minor** (4), **major** (5, + game misconduct), **misconduct** (10), **match penalty**. The penalised team plays **short-handed** (a "power play" for the other team); a minor ends early if the power-play team scores. **Too many men**, high-sticking, tripping, hooking, slashing, interference, boarding, cross-checking, fighting (a major).
- **Delayed penalty:** play continues until the offending team touches the puck, so the non-offending team often pulls its goalie for an extra attacker.


**Goaltending / empty net.** A team trailing late routinely **pulls its goalie** for a 6th skater — this inflates late-game variance and produces empty-net goals (`IH-B6`), which matter disproportionately for totals and puck-line settlement.


**Video review.** Goal/no-goal, offside challenges, goalie interference — scope varies by league.


### 9.2 Overtime, shootout and points — the regime that varies most


| Regime | NHL regular season | NHL playoffs | IIHF tournament (group) | IIHF playoff/medal | Typical European league (incl. AIHL, Metal Ligaen) |
|---|---|---|---|---|---|
| Overtime | 5 min, **3-on-3**, sudden death | **20-min periods, 5-on-5**, sudden death, repeated until a goal | 5–10 min 3-on-3 sudden death | Longer sudden-death periods until a goal | 5–10 min 3-on-3 (or 4-on-4) sudden death |
| Shootout | Yes, if OT scoreless | **No** | Yes | **No** | Yes, if OT scoreless (regular season) |
| Can a game end tied? | **No** (SO guarantees a winner) | No | No | No | No (regular season — SO decides) |
| Points for a win | 2 (reg or OT/SO) | n/a (series) | **3** regulation / **2** OT-SO | n/a | **3** regulation / **2** OT-SO |
| Points for an OT/SO loss | **1** ("loser point") | n/a | **1** | n/a | **1** |
| Points for a regulation loss | 0 | n/a | 0 | n/a | 0 |


**Settlement consequence.** A **"regulation" (60-minute) market** and a **"full-time / including OT" market** are different propositions — a regulation-time bet can be a **push/tie** even though the game itself always produces a winner. The **puck line** (usually ±1.5) interacts strongly with empty-net goals and the OT/SO cutoff. The **"3-way" moneyline** (home / draw / away, settled at 60 minutes) is common in European hockey and is the correct market to fade or back a tie. For AIHL/Metal Ligaen always confirm whether the operator settles the head-to-head at 60 minutes or after the shootout.


### 9.3 AIHL (Australian Ice Hockey League)


**Structure (2026).** A semi-professional league of **10 teams** (Newcastle Northstars, Sydney Ice Dogs, Sydney Bears, Central Coast Rhinos, Canberra Brave, Melbourne Thunder, Melbourne Mustangs, Perth Ice, Brisbane Lightning, Adelaide Adrenaline). Regular season runs the **Australian winter (~April–August)**.


**Period length — 15 minutes.** AIHL games are **three 15-minute periods**, not 20 — a full match is 45 minutes of play, so **per-game goal totals run well below NHL/IIHF levels** and NHL/IIHF scoring rates cannot be transferred without rescaling to 45 minutes (`SFA-ICE-HOCKEY` §8.10 anchoring; this is the single biggest AIHL-specific trap).


**Imports.** Maximum **6 North American or European import players** plus **1 Asian import** per team — imports are typically 2–3 forwards, a goalie and 1–2 defencemen, so a small change in import availability is a large effective-strength swing.


**Points.** **3 for a regulation win, 2 for an OT/SO win, 1 for an OT/SO loss, 0 for a regulation loss** (European-style, used since 2006).


**Regular-season overtime.** 5-minute **3-on-3** sudden death (since 2019); scoreless → **shootout** (5 rounds, then sudden-death rounds).


**Goodall Cup playoffs (2026).** The **top 6** regular-season teams qualify; the finals are a **single-weekend event** at one venue (O'Brien Icehouse, Docklands, 28–30 August 2026): **preliminary finals** (Fri), **semi-finals** (Sat), **Grand Final** (Sun). Preliminary and semi-final ties → **straight to a shootout** (no OT period). The **Grand Final** ties → **continuous 20-minute sudden-death OT periods** until a goal. (2026 result: Newcastle Northstars 2–1 Canberra Brave.)


**Settlement note.** Because playoffs use different OT rules at different rounds, and the regular season is 45 minutes, freeze the exact stage and period length before setting any total or OT-related market.


### 9.4 Metal Ligaen (Denmark — top division)


**Structure.** Denmark's top ice-hockey league, **9 teams** (recently reduced). Season starts late August. Each team plays **48 regular-season games** (six against each opponent — three home, three away). **Standard 20-minute periods** (IIHF).


**Points.** **3 regulation win / 2 OT-SO win / 1 OT-SO loss / 0 regulation loss.** Regular-season ties go to 3-on-3 OT then a shootout. The regular-season winner qualifies for the **IIHF Continental Cup**.


**Playoffs.** **Top 8** into a bracket: **Quarter-finals → "Metal4" (semi-finals) → Final**, each a **best-of-seven** series. Seeding **1 v 8, 2 v 7, 3 v 6, 4 v 5**, higher seed has home advantage (in some seasons the top seeds "pick" their opponent). Playoff OT is full sudden-death periods, no shootout.


**Promotion/relegation** with the Danish **1. Division** applies at the bottom of the table (playout / qualification series) — confirm the season's exact mechanism if a card touches it. Import limits are lighter than the AIHL's but exist — confirm per season.


### 9.5 IIHF national-team context


Not directly in the log but the identity template must handle it: IIHF rules (20-minute periods, wider rink historically, 3-2-1-0 points, 3-on-3 OT + shootout in group games, long sudden-death OT with **no shootout** in medal/elimination games), tournament format = groups then a single-elimination knockout. Olympic and World Championship rosters and rules are their own era/population.


### 9.6 Identity checklist (ice hockey)


Resolve before any rate work: **league and therefore period length** (AIHL 15 min; almost everything else 20 min) and rink; the **points and overtime regime** and whether it changes for the playoffs; whether the contract is **"regulation / 60 (or 45) minutes"** or **"full-time including OT/SO"**; **import-player availability** for the specific game; goalie confirmation and back-to-back status; and the operator's settlement for the 3-way line and the puck line (empty-net and OT exposure).


## September 5 settlement learning — prospective SFA amendment


P-166 and P-200 remain completed-event **research** settlements with unresolved operator endpoints. Maintain regulation score, OT score and any shootout accounting as separate fields. A corroborated final is not evidence of what an unnamed operator includes. P-200's regulation total six versus final seven crosses 6.5; do not invent an action rule. P-166's final 5–4 versus regulation 4–4 likewise requires row-level endpoint comparison.


L-068–L-071 apply at this SFA's identity/goalie-exposure/period-to-OT/settlement stages. They repair arithmetic, gate propagation, two-sided phases and field semantics; this pass introduces no hockey scoring-rate or goalie coefficient.




Full evidence and frozen-card comparisons: [September 5 audit](COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md).


## September 6 settlement learning — cross-sport gates instantiated, and the overtime-terms closure route


No ice-hockey card was settled in the `P-294`–`P-305` cohort. Two inherited follow-ups (`P-166` Melbourne Mustangs v Canberra Brave, AIHL; `P-200` Herning Blue Fox v Rungsted, Metal Ligaen) have sat `FINAL / RESEARCH SETTLED — operator OT/action unresolved` for weeks. Both are cases where the *game result is known and undisputed* (Canberra 5–4 in overtime, regulation 4–4; Herning 4–3 in overtime, regulation 3–3) and the only obstacle is that no operator terms were supplied to say whether the contract settles on regulation or on the final including overtime.


**New gate `G36.1` supplies the route to close them:** grade under stated standard rules, with the standard-rules assumption written down beside the grade. The governing price-independence rule already says a missing price or missing operator wording never justifies leaving a finished event ungraded. Both cards are therefore flagged for closure under `G36.1` at the next settlement pass rather than carried indefinitely. **They are not regraded in this pass**, because regrading a historical settlement is a decision that should be taken deliberately rather than as a side effect of a rule change.


**Ice-hockey-native tail example.** A total-goals `Under` is exposed to the empty-net tail: a one-goal game in the final two minutes has a materially higher scoring rate than the preceding 58, and a 5-on-6 empty-net situation can add two goals in under a minute. Hold the final-two-minutes window as its own term in the tail budget, exactly as `G20.1` already requires the scoring-allocation phases to be split for margins. Overtime and the shootout are separate branches with their own rate environments under `G22`.




### Cross-sport gates instantiated here (v3.7)


| Gate | Sport-native instantiation |
|---|---|
| `G10.2` settlement-source pre-registration | NHL settles from the official NHL game summary; AIHL, Metal Ligaen and comparable leagues need their own named official endpoint. Where overtime/shootout action terms are unsupplied, `G36.1` governs: grade under standard rules with the assumption stated. |
| `G14.2` coaching / bench / rotation record | Record the head coach, the confirmed starting goaltender (the single highest-leverage participant in this sport), the scratches, and back-to-back/travel signals. |
| `G20.2` distributional tail audit | Derive tail and boundary mass from the **same frozen ice-hockey joint score distribution**, including confirmed goalie state, 5v5 shot/xG process, special teams, score effects, empty-net and overtime branches, with travel/rest used only through a named mechanism. Historical order-statistic stress sums are superseded as active gates. |
| `G21.1` exact target geometry | Map every supplied target to its exact settlement event and derive WIN/PUSH/LOSS from the same frozen sport-native PMF/CDF or coherent branch mixture. Historical path-count/category labels have no mandatory ordinal effect. |
| `G26.1` no universal separation floor | Reference rates and `rank_gap` are descriptive only. **No 40–60% or other pooled probability band can disqualify Rank #1.** Rank from exact marginal likelihood plus robustness/evidence uncertainty. |


**Pre-issue checklist additions (this sport):** settlement endpoint named per row; coaching/bench/rotation record for both sides with missingness codes; tail-budget sums printed against every total line; path-geometry class and `N` printed for every total and phase-total row; separation-floor result stated for Rank #1.


Full narrative and evidence: [`IMPROVEMENT_PLAN_2026-09-06.md`](IMPROVEMENT_PLAN_2026-09-06.md). Controlling gate text: [`RULES_GENERAL.md` §13](RULES_GENERAL.md).


## September 5 implementation after freeze confirmation


**ACTIVE REQUIRED PROCESS — MDS-2026.09.05-v3.6 / L-068–L-072.** Keep regulation and overtime/shootout endpoints explicit in total and margin calculations. An unknown operator endpoint is a contract-specific follow-up; it does not invalidate an otherwise frozen pre-game card or justify a new scoring coefficient.


At final delivery, record the preferred total direction for each exact target, the strongest evidenced failure path for ranks #1 and #2, and whether both can win under the stated joint scenario. Rank by supported marginal likelihood; do not promote an opposite pick solely to manufacture one O/U win. At settlement, keep all issued wins/losses, including defective reasoning, in the applicable historical scorecard and review failed #1/#2 and preferred totals.


[Eligibility policy](PERFORMANCE_ELIGIBILITY_POLICY.md): non-live history is user-confirmed frozen pre-game; explicit live-issued views stay separate. These process repairs are implemented now. Numerical weights and predictive-lift claims need a later frozen comparison; historical origin games do not supply those completions.


## 2026-09-06(f) — settlement and retrospective addendum


P-166/P-200 retain regulation and completed-match scores side by side. P-166 all four ranked rows are invariant across 4–4 regulation and 5–4 OT; P-200 6.5 totals reverse between 3–3 regulation and 4–3 OT. Research uses the stated full-match convention, with unknown operator action separate. Competitive wins do not establish multi-goal separation; no goalie/fatigue mechanism is invented from final scores.


Full frozen ranks, actual drivers, knowability and smallest fixes: [PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md). Reinforcement only; METHOD v4.0 remains controlling and no new predictive weighting is promoted.


## 2026-09-09 — cross-sport controls instantiated here (`G-L1`, `G-L2`, `G-L7`, `G-L8`)


No ice-hockey card was issued in the `P-333`–`P-344` cohort. The four cross-sport requirements adopted from it (`RULES_GENERAL.md` §§16.5(a)–(d), full evidence in `PREDICTION_LOG_COMBINED_3.md` §"2026-09-09") apply to this sport from the next card. All four are **disclosure/retrieval requirements — no fitted weight, no ordinal bar** (`L-087`).


| Cross-sport control | Ice-hockey instantiation |
|---|---|
| **`G-L1` §16.5(a)** — enumerate outcome-state families with explicit mass | Enumerate the **goal-total families** (≤3 / 4 / 5 / 6 / 7+) and the **margin families** (regulation blowout 3+ / regulation 2 / regulation 1 / tied-after-60 → OT/SO), each with an explicit mass summing to 1. The **tied-after-regulation branch must carry its own stated mass** and its own empty-net/OT/shootout scoring rate — `P-166` and `P-200` both settled differently at the regulation and completed-game endpoints, so the family enumeration must be produced **once per endpoint** and the invariant rows identified. Every current-evidence §8.5 kill path, including the **empty-net goal** and the **late push**, appears as a weighted branch. Print a representative Rank-#1 final score and check it against the line, the total and the endpoint convention. |
| **`G-L2` — declared uncertainty model** | State the prior and scenario probabilities. Symmetric uncertainty around an unchanged prior affects width; hierarchical shrinkage or asymmetric scenarios may change both mean and variance. Regenerate all dependent probabilities; unsupported directional adjustments remain prohibited. SCORING_AND_VALIDATION section 5 controls. |
| **`G-L7` §16.5(c)** — aggregate-to-disaggregate retrieval | Do not let a season save percentage, a goals-against average or a "last N" summary carry directional weight while the **per-start log** is available. Print the goaltender's **start-by-start record** (shots faced, saves, goals against, save percentage) for the decision-relevant window and state whether a slump is front-loaded, back-loaded or uniform, and whether the **underlying workload/shot-quality held** — the direct analogue of the walk-rate check that decided `P-339`. Quantify **every forward line's recent goal/assist output and every goaltender's per-start line**; a name in a "leaders include…" phrase without a number is `AGGREGATE_ONLY` and caps the dependent total/margin rows. |
| **`G-L8` — distribution coherence** | Derive each total/spread probability from the exact joint PMF/CDF and settlement endpoint, with push mass. Absolute normalised distance does not order probabilities across different distributions. No missing width or realised result justifies an invented probability. |


## 2026-09-11 — cross-sport controls instantiated here (`G-L9`, `G-L10`, `G-L11`, §16.8)


No ice-hockey card in the `P-345`–`P-371` import. From the next card ([`RULES_GENERAL.md` §§16.5(e)–(g), §16.8](RULES_GENERAL.md)):


| Control | Ice-hockey instantiation |
|---|---|
| `G-L9` §16.5(e) | Itemise the complement of an Under or a +1.5 puck line across the named paths — empty-net goals, a power-play cluster, a backup goaltender, overtime. |
| `G-L10` §16.5(f) | A favourite −1.5 and an Over are positively coupled through empty-net goals; an underdog +1.5 and an Under are positively coupled through a tight, goaltender-driven game. Print the sign. |
| `G-L11` §16.5(g) | A goaltender's save percentage over a few starts is a proportion over shots faced — print its standard error before it moves the centre. |
| §16.8 | The starting goaltender is confirmed before puck drop; `NOT_RETRIEVED` after confirmation is a `RETRIEVAL_MISS`. |




## 2026-09-12 algorithm corrections and retrospective integration


Apply section 16.9 to joint regulation goals and the overtime/shootout contract. Confirm starting goalies separately from roster membership, skater lines, scratches, reserves and coaches. Empty-net and power-play states can alter total/margin dependence; include them once in exclusive outcome branches. Shot/save rates use actual attempts and quality/context, not invented denominators. No new hockey result was settled in this pass; transferred controls repair arithmetic/provenance only.


For every supplied row, use exact target probabilities from a coherent joint distribution; handle push/void/censoring explicitly, avoid overlapping adverse-state counts, and report JOINT_UNQUANTIFIED with bounds if the dependence is not specified. Separate issued-time participant capture, later recovered evidence, source accuracy by field, observed mechanism, and unverified causal interpretation. Keep one preferred O/U direction per distinct target and report the top-two denominator honestly. [Shared correction and methodology sources](audit_2026-09-12/rule_corrections.md). All current log observations remain learning-only and not performance-eligible.




## 2026-09-15(b) settlement learning — `P-373`–`P-423` import


Learning-only; disclosure/process changes only — no coefficient or ordinal bar (`L-087`). Evidence and tables: [`PREDICTION_LOG_COMBINED_3.md` §"2026-09-15(b)"](PREDICTION_LOG_COMBINED_3.md). Cross-sport rule: `RULES_GENERAL.md` §16.10 (`G-L12` margin centre/width; fixture identity; official-record derivative settlement).


No ice-hockey card in this import. **`G-L12` instantiation:** for any puck line in the top two, print P(favourite by 2+) from the goal-margin families, including the empty-net branch for one-goal games; goalie uncertainty (control 14) widens, it does not move the centre toward a one-goal game.


## 2026-09-16 — cross-sport controls instantiated here (`G-L13`, `G-L14`, `G-L15`, disruption facts)


No ice-hockey card was settled this pass. Rules: `RULES_GENERAL.md` §16.11.
- **`G-L13`:** the starting goalie is confirmed from a raw league or team record, not a summary.
- **`G-L14`:** period totals and shots-on-goal rows name their settling record at issue; the operator's overtime and shootout terms are recorded separately (`G36.1`).
- **`G-L15`:** label total rows forced-pair or free.
- **Disruption facts:** record major penalties, match penalties, goalie changes and empty-net goals with the game clock and score.


## 2026-09-17 — cross-sport controls instantiated here (`G-L17`–`G-L20`)


No ice-hockey card in this import. **`G-L17`:** a puck line and an Under commonly share one low-event state — print the joint failure mass and name it. **`G-L18`:** print each side's goal marginal before a game total. **`G-L19`:** the end-state family must distinguish regulation win, overtime win and shoot-out win, and must match the operator's stated endpoint (`G36.1`); a two-outcome label is invalid where the competition records regulation ties. **`G-L20`:** a recent same-venue meeting that cleared the total gets explicit mass.


Evidence and cohort audit: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17"](PREDICTION_LOG_COMBINED_4.md); rules in `RULES_GENERAL.md` §16.12.


## 2026-09-17(b) — cross-sport controls instantiated here (`G-L21`–`G-L24`)


**G-L24 in ICE HOCKEY:** derive the exact signed-margin distribution under the competition endpoint, including draw, key-value and push masses. Pooled league bands are uncertain references, not mandatory matchup probabilities or rank prohibitions. Missing pooled bands do not invalidate a complete conditional joint distribution. **`G-L21`:** 'goaltender steals it' carries an Under, a dog line and a team total together — print `P(all fail)`. **`G-L22`:** puck line and total are forced pairs. **`G-L23`:** shots, high-danger chances, goaltender changes and **the empty-net timestamp** are the process record; a goal scored into an empty net is an endpoint artefact, not evidence about the run of play.


Evidence and cohort audit: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17(b)"](PREDICTION_LOG_COMBINED_4.md); rules in `RULES_GENERAL.md` §16.13; bands and base rates in [`BASE_RATES_REGISTER.md`](BASE_RATES_REGISTER.md).


## Current model implementation — 2026-09-17


Use METHOD v4.2's six-field object and SCORING_AND_VALIDATION for exact outcome/push scoring, event-level comparison, descriptive recency and declared hierarchical uncertainty. MODEL_IMPLEMENTATION_RECIPES supplies this sport's retained model scope and endpoint design. Forecast probabilities come from the joint model; pooled base rates are uncertain context, not universal limits. Numeric row caps disconnected from that model, absolute-distance probability ordering and retrospective tail reweighting are withdrawn. No fitted coefficient or predictive improvement is claimed. New cards freeze the method/control hash; existing cards keep their issued versions.


## 2026-09-19 — recency/rebound, social sources and the top-O/U review


`R-1` ([`RECENCY_AND_REBOUND.md`](RECENCY_AND_REBOUND.md)) applies: recent results revise an estimated **rate** through a named mechanism, never forecast a **deviation**. No rebound and no hangover adjustment is permitted in either direction. This sport's magnitudes are **`NOT_YET_DERIVED`** — the MLB figures are not transferable and must not be imported; derive them from this competition's own record before any recent-form weighting.


Source controls `S-1` (social identity: X and Reddit return no usable content; Bluesky sports handles failed identity verification 6/6) and `S-2` (press conferences are availability/role evidence, never a signed adjustment to a modelled rate) apply — `SOURCES.md` §"2026-09-19".


A loss **or push** on the card's highest-ranked over/under now triggers the same enhanced failure review as a Rank #1 loss (`METHOD.md` §7).


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — market-independent totals/line addendum


**Source priority:** NHL/competition official Gamecenter/stats/EDGE and team roster/goalie releases; valid independent structured stats only with known lineage. Betting/fantasy projections are prohibited.


Model regulation/OT score states with confirmed/probabilistic goalie, lineup/lines, shot/quality process where definition-stable, special teams, rest/travel and venue state. Moneyline/puck-line/total queries must come from the same coherent distribution and correct competition end-state rules.




<!-- ALL-SPORTS-AUDIT-LIVE-RULE-CLEANUP-2026-09-21-CR3 -->
## 2026-09-21 — all-sports audit live-rule cleanup — CR-2026.09.21-3


Current prospective override. Retain confirmed goalie state, 5v5 shot/xG process, special teams, score effects, empty-net/overtime branches and travel/rest only with a named mechanism. Withdraw pseudo-tail order-statistic constructions, path-count ranking shortcuts, universal probability-band top-slot rules, automatic goalie-unknown total direction and recent-finishing-streak conversion shifts. Build one coherent ice-hockey joint outcome distribution before querying targets.