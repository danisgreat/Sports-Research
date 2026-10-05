> **Current authority (October 5):** [METHOD.md](METHOD.md) and [CURRENT_RULES.md](CURRENT_RULES.md) govern new work. Requested qualitative or explicitly uncalibrated research receives canonical Part 6 IDs regardless of calibration; numerical performance certification is separate. Read current IDs/freeze from the [status register](GAME_LOG_STATUS_CURRENT.md), unresolved items from the [carryover](research/verification/closure_2026-10-05/carryover.md), and [current implementation evidence](research/verification/implementation_2026-10-05/REPORT.md). Earlier method, queue, freeze and eligibility statements below retain their historical scope.

**Local authority and all-log reconciliation (October 5):** Local working files govern; GitHub main publishes them. The latest user instruction supersedes earlier GitHub-only prompts. Current [all-log evidence](research/verification/all_log_resolution_2026-10-05/REPORT.md) accounts for all 537 slots and temporary aliases, ten repaired documentary mappings, four new sporting reviews and 53 precise carryovers. Existing IDs and frozen forecast/source bytes remain unchanged.

# Ice hockey analysis rules

**Live rules for Ice hockey. Markdown-only operation, 2026-09-28.** Read §0 in full for every card: it governs this file.
- §1 onward is the reference algorithm and the competition rules; it is consulted by citation.
- The dated history (settlement learnings and the evidence behind every numbered control) was moved verbatim to `archive/superseded_2026-09-28/sport_history/RULES_ICE_HOCKEY_history_to_2026-09-28.md`, which is no longer in the Markdown tree. A maintainer can recover it from the pinned commit ([Git 3fbf0c981b40](https://github.com/danisgreat/Sports-Research/blob/3fbf0c981b40a1d0e3ffff9725dcc8e383ff05fa/archive/superseded_2026-09-28/sport_history/RULES_ICE_HOCKEY_history_to_2026-09-28.md); [index](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)) when a control's full text or evidence is needed. The model works from §0 and the sections below.
- Arithmetic: `PROBABILITY_TOOLKIT.md`. Sources: `SOURCES.md` §3.9. Card and self-audit: `CARD_AND_LOG_TEMPLATES.md`. The cross-sport rules are in `CURRENT_RULES.md`, which outranks this file.
- No sport, competition or target is prospectively validated. Every card is LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.

<!-- LIVE-RULES-PAGE-2026-09-26 -->
## 0. Live rules — one page (consolidated 2026-09-26)

**Status (md-only, 2026-09-28).** This page is the live rule set for this sport and governs the rest of the file. It was consolidated on 2026-09-26 from the numbered controls, the SFA algorithm and the dated sections through 2026-09-25(e). Those dated sections are now archived (see the header). Where a control below is one line, that line is the operative rule, and the archived history is its evidence.

Hockey is **sparse**: too few settled cards for a track record (evidence density `SPARSE`, L-099). Treat every card as low-evidence until the record exists.

### 0.1 Blocking preconditions (§8.1)
| Gate | Requirement | If it fails |
|---|---|---|
| IH-P1 endpoint | Rules, overtime format, shootout treatment, and whether each row settles on regulation or the full match | Stop. Regulation and full match are different targets (control 7) |
| IH-P2 goaltender | Both starting goalies with release status, backup quality and pull risk, re-handshaken at freeze. **Preseason goalies stay `PROJECTED`** until the official lineup or warm-up report | Goalie mixture (IH-B3). In early-season or sparse competitions an unresolved starter keeps a total off Rank 1 (control 14, override 1) |
| IH-P3 operator terms | Whether moneyline, puck line and total include OT/SO, and how a shootout goal counts | `UNKNOWN_DEFINITION`; keep the regulation-draw and one-goal-OT branch (control 13) |
| IH-P4 metric definition | Blocked-shot treatment under the named provider for shot/attempt rows | Capped until reconciled (control 3) |

### 0.2 Building the goal distribution
1. **Anchor.** TB-1 has **no resolution in the NHL** (sides 0.2477 v 0.2503; totals 0.2490 v 0.2502), so anchor on `BASELINE_P` and the §7.2 population. Goalies and the preseason regime are the named departures.
2. **Regular season v preseason (H-R3).** Regular-season total mean 6.25 (SD 2.30). Preseason runs 0.6–0.9 goals lower (2025: 5.68; 2026 to 24 Sep: 5.33). A preseason card prints the preseason reference. Roster tier per side (regulars v AHL/junior/try-outs) is a disclosure with no ranking effect (L-20260924-F08).
3. **Recency (H-R4).** A season scoring rate predicts no better than the league constant; the last game is 40% worse. A back-to-back is −0.20 goals, not distinguishable from zero. Team-scoring leans need a named mechanism (goalie, injuries, special teams); otherwise they are width.
4. **Exposure and conversion.** Shot volume is exposure, never a goal total (control 11). Conversion runs through shot quality, finishing shrinkage and the goalie mixture (IH-S4, IH-S5). Special teams change both opportunity and rate (control 4).
5. **Late state.** Score effects, pulled goalie and empty net are explicit branches (IH-B5, IH-B6).
6. **Width (H-R5).** Total residual SD 2.29, margin 2.57. Below 1.95 (total) or 2.18 (margin), name what the card knows.
7. **One regulation goal object, plus a rules-correct OT/SO object where needed → every row** (IH-S8).

### 0.3 Row rules
- **Totals (H-R1).** OT/SO winners add exactly one goal to a regulation tie, so full-game totals of those games are odd: a 2–2 tie always lands Under 5.5 and a 3–3 tie always lands Over 6.5. A full-game 5.5 or 6.5 prints the regulation-tie mass as its own branch. 24.8% of games reach OT (9.1% shootouts). Regulation-only contracts settle on the 60-minute score.
- **Puck line (H-R2).** P(margin ≥ 2) = 0.568 of all games (0.756 of regulation-decided games). **73% of two-goal regulation wins contain an empty-net goal.** A −1.5 row carries the empty-net route as explicit mass; a +1.5 row names it as its main kill path.
- **Moneyline** matches its endpoint: a regulation draw is not a loss on a full-match line (§8.4).
- **Props:** participation × ice time × event rate (control 9).

### 0.4 Ranking
Rank by RM-1 q with the `TOP2_QUALITY` line. A +1.5 puck line is classed with baseball (`hcp_plus_low`) and carries **no cushion penalty**, because one-goal games are common.

### 0.5 Settlement
The NHL api-web boxscore (`SOURCES.md` §3.9) gives the goalies who played with time on ice, the empty-net goals and the regulation score (H-R6). It also supplies `T-NHL-PRESEASON-GOALIE`. Record regulation versus OT/SO exactly.

### 0.6 Withdrawn in hockey — never apply
`NHL-PRESEASON-ROSTER-ASYMMETRY` as a ranking rule; any "confirmed" preseason goalie without an official report; pseudo-tails, path-count categories, 40–60% bands and normalised-edge ordering.

### Numerical shadow model (2026-09-26(c); suspended for md-only operation, 2026-09-28)

The NHL model (A1) is regulation Poisson ratings, with OT won in proportion to scoring rates and the shoot-out a coin flip. Validated on 2023-24 to 2025-26: A1 beat the league baseline and TB-1 on the result, and beat the baseline on the regulation three-way and the margin. It was **worse than the baseline on totals**, and slightly worse than TB-1 at the total line. It is maintainer Python, never a card input, and the model does not run it: print `SHADOW: NO_LANE (md-only)` at settlement (`research/sport_models_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents))). The hand-computable team baseline that does feed cards is TB-1-MD (`PROBABILITY_TOOLKIT.md` §4).

**Predictability (2026-09-26(e)).** In the NHL 2025-26, the model's favourite reached 0.70 in only 6% of games (won 72.9%), and 67% of games sat at 0.50–0.60 (Brier 0.248 against 0.250). Totals are not predictable by any model here: A1 was worse than the population, and TB-1 no better. A STRONG NHL Rank 1 is rare (`research/predictability_2026-09-26/README.md` ([removed; recovery](HISTORICAL_LINK_INDEX.md#removed-paths-cited-in-operating-documents)); `BASE_RATES_REGISTER.md` §7.8).

### 0.7 Control index (full text in §4 and the dated sections)
1 goalie uncertainty is a mixture · 2 shots and goals linked, not interchangeable · 3 blocked shots definition-sensitive · 4 special teams change exposure and rate · 5 score state changes pace · 6 empty-net goals are an explicit tail · 7 regulation ≠ moneyline · 8 back-to-back is mechanistic · 9 props need role and ice time · 10 external xG models are challengers · 11 shot volume is exposure · 12 sparse competitions keep a conversion cap · 13 OT geometry v operator settlement · 14 unconfirmed goalie blocks a fragile Rank-1 total. References: H-R1 totals and odd OT totals · H-R2 puck line is an empty-net market · H-R3 preseason rates · H-R4 recency · H-R5 width · H-R6 settlement receipt.


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


Algorithm ID: `SFA-ICE-HOCKEY`. Effective **2026-09-02**. Instantiates `GFA-2` (RULES_GENERAL (archived) §11) with ice-hockey content. Process composition only; no fitted weight, scenario weight or published probability is introduced, and this section does not authorise an NHL or any other probability model. Each competition remains a separate rules, data and scoring population.


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
3. A shot or attempt row whose blocked-shot treatment is unreconciled is capped under RULES_GENERAL (archived) §11.5.
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


Implements `GFA-2` step G13.1 (RULES_GENERAL (archived) §11.3B) and runs at that point in the algorithm, not at the end. Retrieval of L5/L10/L15/L20 for both sides and for the head-to-head series is mandatory; a window that does not exist is recorded with its true count and a missingness code.


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


Implements `GFA-2` step G15.1 (RULES_GENERAL (archived) §11.3C). Venue classification for this sport is normally **INDOOR**.


| Field | Use in this sport |
|---|---|
| Venue classification | Indoor; record it and move on |
| Travel, altitude and back-to-back | Entered through goalie choice, line workload and forecheck quality |


Failure to obtain the match-window forecast for an outdoor or open-roof event yields `WEATHER_NOT_AVAILABLE`, widened total and margin distributions, and a `LEAN` cap on every weather-dependent row. No factor above carries an automatic total direction.


### 8.10 Base-rate anchors and derived stat lanes


**Anchoring (G12.1).** Anchor regulation totals on the competition goal environment and full-match moneylines on the frequency of regulation ties proceeding to overtime. Regulation and full-match rows never share an anchor.


StatMuse is an accepted research accelerator for this sport under `SOURCES.md`, using the verified query patterns recorded there. Every returned row is date-checked and reconciled against the official league source before it is decision-driving, and StatMuse never controls participants, availability, rules, state or settlement.


**Derived and low-salience fields that are available and routinely skipped:**


| Field | Note |
|---|---|
| Blocked-shot treatment of the shot metric | A dataset that omits blocked shots cannot control an all-attempt claim |
| Empty-net and pulled-goalie behaviour | Its own branch at `IH-B6`, affecting totals and margins differently |
| Scheduled back-to-back goalie tendencies by club | Conditional; supports the `IH-B3` mixture |


## 9. Sport and competition rules reference


Added 2026-09-04; last reviewed 2026-09-04. Standing reference for the rules of ice hockey and the competition-specific rules of every ice-hockey competition in the prediction logs. Supports `IH-P` identity and §6 settlement; introduces no rate, weight or ordering rule. **Two facts dominate ice-hockey identity: the period length (the AIHL uses 15-minute periods, not 20) and the overtime/points regime, which differ by league and between regular season and playoffs.**


**Maintenance (RULES_GENERAL (archived) §3, `G2`).** Before the first card of a new AIHL or Metal Ligaen season, or the first playoff card, re-verify the period length, the points system, the regular-season vs playoff overtime/shootout rules, the import-player limits, the team count and the playoff bracket against the league source, and update this section **before** issuing the card — both leagues have changed team counts recently, and the AIHL's 15-minute-period and finals-weekend format are unusual and worth re-confirming each year. The first time another hockey competition is forecast (NHL, an IIHF event, another European league), document its full rules — periods, points, OT — here first.


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
