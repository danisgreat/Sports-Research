<!-- THREE-SOURCE-TIME-GATE-2026-09-19-CR4 -->

**Live rules for Rugby union and sevens. Markdown-only operation, 2026-09-28.** Read §0 in full for every card: it governs this file.
- §1 onward is the reference algorithm and the competition rules; it is consulted by citation.
- The dated history (settlement learnings and the evidence behind every numbered control) moved verbatim to [`archive/superseded_2026-09-28/sport_history/RULES_RUGBY_UNION_history_to_2026-09-28.md`](archive/superseded_2026-09-28/sport_history/RULES_RUGBY_UNION_history_to_2026-09-28.md). Open it when a control's full text or evidence is needed.
- Arithmetic: `PROBABILITY_TOOLKIT.md`. Sources: `SOURCES.md` §3.7. Card and self-audit: `CARD_AND_LOG_TEMPLATES.md`. The cross-sport rules are in `CURRENT_RULES.md`, which outranks this file.
- No sport, competition or target is prospectively validated. Every card is LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE.

<!-- LIVE-RULES-PAGE-2026-09-26 -->
## 0. Live rules — one page (consolidated 2026-09-26)

**Status (md-only, 2026-09-28).** This page is the live rule set for this sport and governs the rest of the file. It was consolidated on 2026-09-26 from the numbered controls, the SFA algorithm and the dated sections through 2026-09-25(e). Those dated sections are now archived (see the header). Where a control below is one line, that line is the operative rule, and the archived history is its evidence.

**Evidence density: `SPARSE`** (L-099). There is **no union population reference and no TB-1 lane yet**: cards print `TEAM_BASELINE_P: NOT_COVERED` and `REFERENCE_BASE_RATE: NOT_YET_DERIVED`, the evidence grade is capped at LOW, and the departure ledger names every move away from an even-money prior. Deriving the ESPN rugby-union population is the next research step. Union is never pooled with league, and fifteens are never pooled with sevens (controls 1, 2).

### 0.1 Blocking preconditions (§10.1)
| Gate | Requirement | If it fails |
|---|---|---|
| RU-P1 code and format | Fifteens or sevens, law era, duration, stage, extra-time, draw and qualification terms | Stop |
| RU-P2 team sheet | Official XV or sevens squad, bench, late changes, halfback/fly-half pairing, front row and set-piece roles, substitution plan | Role mixtures; participant-sensitive rows capped (control 11) |
| RU-P3 goal kicker | Primary and replacement kicker, attempt choice and range (control 6) | Required before any total or margin row |
| RU-P4 conditions | Venue, surface, match-window weather through a named mechanism | No automatic total direction |
| RU-P5 sevens schedule | Daily schedule, match load, recovery | Widen tails (control 10) |

### 0.2 Building the score distribution
1. **Territory is not points** (control 4): opposition-22 entry → lineout/maul/breakdown → finishing and goal-kicking.
2. **Points composition** (control 5): tries and conversions versus repeated penalty goals respond differently to weather, discipline and score state. Set piece and breakdown are exposure engines (control 7).
3. **Cards** create asymmetric tails for the exact man-down duration (control 8).
4. **Margins (G-L12):** print the favourite's 8+ and 15+ margin families beside any handicap, with the late-try branch (bonus-point chasing, yellow cards) as mass. Sparse team lists widen the margin distribution rather than centring it on a close game. A low total is not a close margin (control 9).
5. **Broad totals need matchup-native mechanism support**; league averages and recent Over counts cannot outrank thin process evidence (control 3).

### 0.3 Ranking and settlement
Rank by RM-1 q; its cushion term applies to union +k.5 rows. A large cushion (k ≥ 10) stated at 0.60–0.65 is still scored by RM-1, and the reconciliation line names the margin band (`C-PLUS-CUSHION`). Print `TOP2_QUALITY`. Settle from the competition's official match centre plus two further lineages, read from the feed.

### Numerical shadow model (2026-09-26(c); suspended for md-only operation, 2026-09-28)

The rugby-union model (A1) is ridge ratings with key-number weights and draws allowed. **Not validated.** It is maintainer Python, never a card input, and the model does not run it: print `SHADOW: NO_LANE (md-only)` at settlement (`research/sport_models_2026-09-26/README.md`). The hand-computable team baseline that does feed cards is TB-1-MD (`PROBABILITY_TOOLKIT.md` §4).

**Predictability (2026-09-26(e)).** Not measured: no union results were reached. The reference is the population (`research/predictability_2026-09-26/README.md`; `BASE_RATES_REGISTER.md` §7.8).

### 0.4 Control index (full text in §6 and the dated sections)
1 union is not league · 2 fifteens and sevens separate · 3 broad totals need mechanism support · 4 territory is not points · 5 points composition matters · 6 goal kicker is a regime · 7 set piece and breakdown are exposure engines · 8 cards create asymmetric tails · 9 low total ≠ close margin · 10 sevens clusters need restart/card branches · 11 sparse lineups cap evidence.


## 1. Identity and contract


Resolve competition, season and law-trial era, 15s versus sevens, pool/knockout/tie state, venue, home/away/neutral status, match duration, extra-time/sudden-death/draw rules, bonus/qualification incentives, team/player/phase target, line, provider and operator settlement terms. Freeze whether the contract includes extra time.


## 2. Fifteen-a-side participants and exposure


- Confirm the official starting XV, bench, late changes, captain, halfback/fly-half pairing, primary and replacement goal kickers, front-row/set-piece roles and expected substitution/minutes plan.
- Translate absences and returns into set-piece stability, breakdown/ruck speed, territory kicking, gainline success, defensive alignment, goal-kicking and late bench state.
- Record rest, travel, short turnaround, venue, surface and match-window weather through a named mechanism.


## 3. Fifteen-a-side scoring process


Use opponent- and competition-adjusted:


- possession sequences, territory and opposition-22 entries;
- carries, metres/gainline success, clean breaks, defenders beaten and offloads;
- ruck speed/retention, turnovers won/conceded and handling errors;
- lineout and scrum retention/penalties, maul quality and restart outcomes;
- kicks in play, kick-return field position and tactical kicking;
- penalties by location, card/man-down exposure and referee effects only where current data support them;
- try creation and opposition-22 conversion;
- conversion, penalty-goal and drop-goal attempt/accuracy with current kicker identity;
- score-state decisions between goal, touch/lineout/maul and quick tap.


Raw points, broad competition averages and recent Over/Under hit counts describe outcomes. They cannot control a total unless the current lineup, territory/entry, set-piece/breakdown, discipline, try-conversion and goal-kicking pathways support the same scoring state.


## 4. Rugby sevens process


Freeze tournament stage, daily schedule, match duration, squad, rotation and recovery between games. Model:


- possession time and possessions;
- restart retention/regains;
- turnover-to-open-space conversion;
- passes/rucks per possession and retention;
- line breaks, missed-tackle/open-field exposure and tries per possession;
- conversion success and restart location;
- penalties, yellow cards/man-down minutes and sudden separation;
- score-state chasing and qualification incentives.


Sevens totals and margins are cluster-prone: one restart, turnover, breakaway or card can create several linked scores. Winner, handicap and total still come from one joint score tree, but a winner lean never implies a multi-score cover.


## 5. Joint model


For 15s, estimate possession/territory and scoring opportunities first, then split points into tries, conversions, penalty goals and drop goals. Use a joint team-score distribution with lineup, set-piece, discipline, weather, card, late-bench and extra-time branches.


For sevens, use a possession/restart/turnover/line-break state process with try/conversion, card, fatigue and stage-incentive branches. Keep 15s and sevens candidates and baselines separate.


All numerical forms are design ideas only. Suitable future baselines include empirical/shrunk joint scores and component count models; challengers may simulate possessions, territory/entries, set pieces, penalties/cards, tries and kicks. No form may publish a probability until its own target/source/H0/model cards and chronological gates pass.


## 6. Structural controls


1. **Union is not league.** No tackle-set, six-again, interchange or golden-point mechanism transfers from rugby league.
2. **Fifteens and sevens are separate populations.** Do not transfer scoring averages, margins or rest effects between them.
3. **Broad totals need mechanism support.** League average and recent Over counts cannot outrank thin matchup-native scoring evidence.
4. **Territory is not points.** Opposition-22 entry, lineout/maul, breakdown and finishing/goal-kicking determine conversion.
5. **Points composition matters.** The same total can arise from tries/conversions or repeated penalty goals; weather, discipline and score-state decisions affect them differently.
6. **Goal kicker is a regime variable.** Record attempt choice, range and replacement; tries and final points are not independent.
7. **Set piece and breakdown are exposure engines.** Scrum/lineout/maul and ruck/turnover states change possession quality and field position.
8. **Cards create asymmetric tails.** Rebuild remaining possession, width, try and margin exposure for the exact man-down duration.
9. **Low total does not imply close margin.** One side can suppress entries and create a controlled separation while the total remains low.
10. **Sevens clusters require restart/card branches.** A short match and small sample require wide tails, not false confidence.
11. **Sparse lineups cap evidence.** If official teams/kickers and matchup-native process data are missing, rank as required but cap participant-sensitive totals/sides at `FORCED RANK` or `MEDIUM-LOW` evidence.


## 7. Live state


For 15s store score, clock/half, cards and remaining duration, current players/substitutions, kicker, territory, opposition-22 entries, set pieces, penalties, turnovers, line breaks, tries/kicks and weather/surface. Rebuild remaining possessions and scoring composition.


For sevens also store possession/restart state, elapsed/remaining match time, daily match load and qualification context. Do not extrapolate an early breakaway rate across the remaining short match.


## 8. Sources and settlement


- World Rugby laws and competition regulations control laws, variations and scoring rules.
- Official competition/union/tournament match centres, team sheets, disciplinary releases and finals control current facts.
- New Zealand Rugby/provincial unions are preferred current lanes for NPC identity, team and match facts where exposed.
- Ligue Nationale de Rugby's official SuperSevens hub controls its schedule, stage, tournament reports and official results where exposed.
- Reputable specialist rugby providers may fill defined process fields after provider/coverage checks; they do not override official team, law or final corrections.


Settle score, phase, extra time, cards and player/team statistics under the exact provider and endpoint. If the official final is inaccessible, use two independent high-quality current sources and mark the affected field provisional.


Method references:


- [World Rugby Laws of the Game](https://passport.world.rugby/laws-of-the-game/).
- [Performance Analysis in Rugby Union: a Critical Systematic Review](https://doi.org/10.1186/s40798-019-0232-x), supporting context-specific use of territory, line breaks, metres, kicking, tackles, turnovers and penalties rather than a universal outcome statistic.
- [Performance Indicators Related to Points Scoring and Winning in International Rugby Sevens](https://pmc.ncbi.nlm.nih.gov/articles/PMC3990890/), supporting possession, restarts, set piece, phase play, turnovers, cards and scoring-rate decomposition; it does not establish an active coefficient.


## 9. Upcoming-game research sequence


1. Freeze code/format, competition/law era, stage, duration, extra-time/draw/qualification and contract/provider terms.
2. Retrieve the official fixture and teams/squad, bench/rotation, kickers and current availability; refresh immediately before start.
3. For 15s, build possession/territory/entry, set-piece/breakdown, discipline/card, try-conversion and goal-kicking branches.
4. For sevens, build possession/restart/turnover/open-space, try/conversion, card, recovery and qualification branches.
5. Stress lower, central, high-conversion, penalty-goal, card and controlled-separation states. Explain why broad scoring averages remain relevant after current matchup adjustment.
6. Derive winner, handicap and total from one format-correct joint score tree and log all missing participant/provider fields.


## 10. SFA-RUGBY-UNION — sport forecast algorithm


Algorithm ID: `SFA-RUGBY-UNION`. Effective **2026-09-02**. Instantiates `GFA-2` (RULES_GENERAL (archived) §11) with rugby-union content. Process composition only; no fitted weight, scenario weight or published probability is introduced, and no rugby-union or sevens target, source, dataset or model is approved or fit. Fifteens and sevens run separate branch sets and are never pooled with each other or with rugby league.


### 10.1 Blocking preconditions


| Precondition | Requirement | Failure output |
|---|---|---|
| `RU-P1` code and format | Fifteens or sevens, competition, law era, match duration, tournament stage, extra-time, draw and qualification terms | `GATE-TARGET` failure; do not proceed |
| `RU-P2` team sheet | Official starting XV or sevens squad, bench, late changes, captain, halfback and fly-half pairing, front-row and set-piece roles, and the substitution or rotation plan | Role mixtures; participant-sensitive totals and sides cap at `FORCED RANK` / `MEDIUM-LOW` |
| `RU-P3` goal kicker | Primary and replacement goal kicker, with attempt choice and range | Required before any total or margin row, because tries and points are dependent |
| `RU-P4` conditions | Venue, surface and match-window weather, each entered through a named mechanism | No automatic total direction |
| `RU-P5` sevens schedule | For sevens, the daily schedule, match load and recovery between fixtures | Widen tails; a short match with a small sample does not support confidence |


### 10.2 Exposure chain — fifteens


| Step | Output |
|---|---|
| `RU-S1` | Minutes and substitution plan by player, with set-piece and bench impact by phase |
| `RU-S2` | Possession sequences and territory, opponent-adjusted |
| `RU-S3` | Opposition-22 entries from `RU-S2`, including kick-return field position and tactical kicking |
| `RU-S4` | Entry conversion: carries, gainline success, clean breaks, defenders beaten, offloads, ruck speed and retention, turnovers won and conceded |
| `RU-S5` | Set piece: lineout and scrum retention and penalties, maul quality, restart outcomes |
| `RU-S6` | Discipline: penalties by location, card and man-down exposure |
| `RU-S7` | Points composition: tries, conversions, penalty goals and drop goals, split by score-state decisions between goal, touch and quick tap |
| `RU-S8` | One joint team-score object with lineup, set-piece, discipline, weather, card, late-bench and extra-time branches |


### 10.3 Exposure chain — sevens


| Step | Output |
|---|---|
| `RU-V1` | Squad rotation and recovery state across the day |
| `RU-V2` | Possession time and possession count |
| `RU-V3` | Restart retention and regains |
| `RU-V4` | Turnover-to-open-space conversion, passes and rucks per possession, retention |
| `RU-V5` | Line breaks, missed-tackle and open-field exposure, tries per possession |
| `RU-V6` | Conversion success and resulting restart location |
| `RU-V7` | Penalties, yellow cards and man-down minutes, with sudden separation |
| `RU-V8` | One joint score tree with cluster, card, fatigue and stage-incentive branches |


### 10.4 Mandatory branch set


| Branch | Content |
|---|---|
| `RU-B1` | Central territory with central entry conversion for both sides |
| `RU-B2` | Territory-without-points branch: entries that do not convert because of set piece, breakdown or finishing |
| `RU-B3` | Penalty-goal composition branch: the same total reached through repeated shots at goal rather than tries |
| `RU-B4` | Controlled-separation branch: one side suppressing entries inside a low total |
| `RU-B5` | Card branch: remaining possession, width, try and margin exposure rebuilt for the exact man-down duration |
| `RU-B6` | Kicker branch: a change of goal kicker or range, altering points per try |
| `RU-B7` | Weather branch, with handling, kicking, maul and set-piece effects signed separately |
| `RU-B8` | Sevens cluster branch: restart, turnover, breakaway and card sequences producing several linked scores; and, for fifteens, the extra-time or draw state |


### 10.5 Contract derivation map


| Contract | Queried from | Extra condition the mechanism must predict |
|---|---|---|
| Total | Sum marginal | Points composition, not only scoring opportunity; the component budget at each side's floor, centre and high |
| Handicap | Margin marginal | Separation, and the man-down and kicker branches |
| Winner | Margin sign | A winner lean never implies a multi-score cover, especially in sevens |
| Team total | Team marginal | That side's own entries, set piece and kicking |
| Player and stat props | Minutes, position and the exact provider definition | Role continuity across substitutions |


### 10.6 Kill-path library


| Kill path | Defeats | Evidence origin |
|---|---|---|
| Thin matchup-native territory, entry, set-piece and conversion evidence behind a broad recent-totals read | A total ranked on competition scoring averages or recent Over counts | C-PL6-RU-TOTAL-MECHANISM, §6 control 3 |
| Entries that do not convert | An Over ranked on territory or possession | §6 control 4 |
| A total reached through penalty goals rather than tries, or the reverse | A total whose branches assume one composition | §6 control 5 |
| A card rebuilding remaining possession and width | A margin or total row with no man-down branch | §6 control 8 |
| One side suppressing entries inside a low total | A cushion inferred from an Under | §6 control 9 |
| A sevens restart, turnover or breakaway cluster | A short-match total or margin ranked with narrow tails | §6 control 10 |
| Missing official teams, kickers or matchup-native process data | A participant-sensitive total or side above `FORCED RANK` | §6 control 11 |
| Rugby-league mechanisms imported into union analysis | Any step resting on tackle sets, six-again, interchange or golden point | §6 control 1 |


### 10.7 Sport ordering overrides


1. Fifteens and sevens rows are never compared using a shared scoring baseline, even within one tournament day.
2. A total row whose points composition is unresolved between tries and penalty goals is capped at `LEAN` until `RU-B3` is written.
3. In sevens, no row exceeds `LEAN` on a sample smaller than the stage's own credible population; cluster branches widen the corridor first.
4. Broad competition averages and recent Over counts may not supply a decisive term in the G23.1 marginal-likelihood comparison.
5. Recent points, cover counts and reputation are `E — diagnostic only`.


### 10.8 Pre-issue checklist


1. `RU-P1`–`RU-P5` status printed, including the kicker and any sevens match-load state.
2. Format-correct competition and venue scoring baseline stated before any line.
3. Full chain written — `RU-S1`–`RU-S7` for fifteens, `RU-V1`–`RU-V7` for sevens.
4. All eight `RU-B*` branches represented; component budget solved at the supplied total.
5. Points composition stated explicitly before any total is located.
6. Kill-path rows selected from §10.6 and reconciled against the issued order.
7. Card and man-down branch written for every margin and total row.
8. Team sheets, kickers, late changes and conditions refreshed at G31 before the view is appended.
9. Recency block complete per §10.9: L5/L10/L15/L20 for both sides and for head-to-head, continuity count stated, trend verdict per metric, unique-event de-duplication done.
10. Environment block complete per §10.10: Match-window rain and wind recorded and mapped to points composition and goal kicking.
11. `REFERENCE_BASE_RATE`, exact threshold, population and denominator recorded for every supplied row per §10.11 as a descriptive diagnostic only; no reference-band, trend or slot-frequency adjustment may move an ordinal (G23.1).
12. Extra-condition support audit (G24) recorded for every handicap, team-total and cushion row; no retrospective contract-family penalty is applied.
13. Separation budget (G20.1) solved for every margin, handicap and cushion row by half, with set-piece dominance, the finishers' bench window and late penalty/try paths held separately.
14. Rank-1 implied-target interval (G25.1) stated in the unit of every other supplied line, each remaining row classified `COHERENT`/`PARTIAL_OVERLAP`/`DISJOINT`, and every aggregate budget re-solved conditional on the Rank-1 state.
15. Winner-and-cushion reconciliation (G30.1) whenever Rank #1 is an underdog cushion, with the outright-win and narrow-loss branch ordering stated. Example separation kill path for this sport: a late try or a sequence of penalty goals.
16. Deficit attribution (G14.1) recorded for every weak, absent, returning or small-sample participant: which side's distribution moved and through which exposure step.


### 10.9 Recency, head-to-head and trend windows


Implements `GFA-2` step G13.1 (RULES_GENERAL (archived) §11.3B) and runs at that point in the algorithm, not at the end. Retrieval of L5/L10/L15/L20 for both sides and for the head-to-head series is mandatory; a window that does not exist is recorded with its true count and a missingness code.


Populate one windowed table per side with these metrics, and one head-to-head table:


| Window metric | Content |
|---|---|
| Possession and territory | Possession share and territory, opponent-adjusted |
| Access | Opposition-22 entries for and against, and entries converted to points |
| Set piece | Lineout and scrum retention, maul success and penalties conceded at the set piece |
| Points composition | The split of points between tries, conversions, penalty goals and drop goals |
| Goal kicking | The current kicker's own last 5/10/15/20 games: attempts, success and range |


**Head-to-head continuity.** Continuity means the same coaching group, a comparable matchday squad and the same law era. Fifteens and sevens head-to-head are never pooled, and neither is pooled with rugby league.


**Descriptive recency windows (G13.1; revised 2026-09-17).** Retrieve L5/L10/L15/L20 and continuity-qualified H2H with unique-event counts. These windows overlap. Monotonicity and dispersion among their averages are not a statistical trend/noise test. Report direction descriptively; estimate recency decay and opponent/regime effects using time-ordered validation. See SCORING_AND_VALIDATION section 5.


**De-duplication.** The windows overlap by construction and share matches with the head-to-head and venue series. Shrink from unique underlying events under G9; never treat L5, L10, L15 and L20 as four confirmations.


### 10.10 Environment and conditions


Implements `GFA-2` step G15.1 (RULES_GENERAL (archived) §11.3C). Venue classification for this sport is normally **OUTDOOR**.


| Field | Use in this sport |
|---|---|
| Hourly precipitation | Handling, maul and set-piece behaviour, and the points-composition mix |
| Wind speed, gusts and direction | Territorial kicking and goal kicking, resolved against ground orientation |
| Surface state | Official venue source |
| Temperature and, for sevens, the day schedule | Recovery between fixtures is a sevens-specific exposure variable |


Failure to obtain the match-window forecast for an outdoor or open-roof event yields `WEATHER_NOT_AVAILABLE`, widened total and margin distributions, and a `LEAN` cap on every weather-dependent row. No factor above carries an automatic total direction.


### 10.11 Base-rate anchors and derived stat lanes


**Anchoring (G12.1).** Anchor totals on the competition scoring environment for that exact format, and margins on its margin distribution. Fifteens and sevens anchors are separate.


**Derived and low-salience fields that are available and routinely skipped:**


| Field | Note |
|---|---|
| Kicker range and attempt-choice tendency | Decides whether a total is reached through tries or through repeated shots at goal |
| Card history and discipline at the set piece | Feeds the `RU-B5` man-down branch |
| Bench composition and the substitution plan | Front-row and finisher impact by phase |


## 11. Sport and competition rules reference


Added 2026-09-04; last reviewed 2026-09-04. Standing reference for the laws of rugby union (15s and 7s) and the competition rules of the two rugby competitions in the prediction logs: the **New Zealand NPC** (now the Hilux NPC) and the **French In Extenso SuperSevens**. Supports `RU-P` identity and §8 settlement; introduces no rate, weight or ordering rule.


**Maintenance (RULES_GENERAL (archived) §3, `G2`).** World Rugby runs frequent law trials (the 20-minute red card, the goal-line drop-out, scrum/breakdown tweaks, a shot-clock) that competitions adopt at different times; SuperSevens changed its whole format for 2026. Before the first card of a new NPC or SuperSevens season, re-verify the red-card law in force, the bonus-point rules, the team count and single-division status, the playoff bracket, and (for SuperSevens) the current stage structure against the competition's site, and update this section **before** issuing the card. The first time another union or sevens competition is forecast (Super Rugby, URC, Top 14, a Test, a World Series leg), document its full rules here first, and keep 15s and 7s as separate populations.


### 11.1 The laws of 15-a-side rugby union


**Field and teams.** ~100 m (goal line to goal line) × 70 m, plus in-goal areas. **15 players a side** (8 forwards, 7 backs), **8 replacements** on the bench. Substitutions are permanent except a front-rower may return to cover an injury/blood/HIA (and there are minimum front-row-cover requirements — if a team cannot field a safe front row, scrums become **uncontested** and that team plays a man short).


**Scoring.**
- **Try = 5 points** — grounding the ball in the opponent's in-goal.
- **Conversion = 2 points** — a place- or drop-kick from in line with where the try was scored.
- **Penalty goal = 3 points.**
- **Drop goal (from open play) = 3 points.**


**Play.** Continuous. The ball may be **carried, passed backwards or kicked** — a forward pass or knock-on is a **scrum** to the other team. Contact contests: the **tackle** (tackler must release, tackled player must release/play the ball), the **ruck** (players bind over the ball on the ground — offside lines apply), the **maul** (ball-carrier held up, teammates bind and drive). Set pieces: the **scrum** (8 v 8 contest to restart after a minor infringement) and the **lineout** (throw-in from touch, with lifting). **Offside** applies at every phase and is one of the most penalised areas.


**Match structure.** **Two 40-minute halves** (running clock, stopped by the referee for injuries, TMO reviews, kicks at goal and scrum resets; a half only ends when the ball next becomes dead after 40:00). ~10–15 min half-time. **TMO** (Television Match Official) reviews tries and foul play. **Yellow card** = 10 minutes in the sin bin, no replacement; **red card** = off for the match — many competitions now use a **20-minute red card** (the sent-off player cannot return but a replacement enters after 20 minutes). Confirm which red-card law the competition uses.


**Bonus points (standard union system).** In the league table: **4 for a win, 2 for a draw, 0 for a loss**, plus **1 bonus point for scoring 3 (or in some competitions 4) more tries than the opponent** ("try bonus"), plus **1 bonus point for losing by 7 points or fewer** ("losing bonus"). This makes the union table markedly different from rugby league's — a losing team routinely banks points, and blowouts are chased for the try bonus.


**Knockouts.** Level after 80 minutes → **two 10-minute halves of extra time**; if still level, a period of **sudden-death extra time**, then a **kicking competition** (place kicks from set marks) as a last resort. Confirm per competition.


### 11.2 The laws of rugby sevens


Same field, posts and scoring **values** as 15s, but:


- **7 players a side** (3 forwards, 4 backs), **5 replacements**, 5 substitutions.
- **Two 7-minute halves** (2 min half-time); **finals are two 10-minute halves**.
- **Conversions are drop-kicks** and must be taken **quickly** (within ~30–40 seconds); after a try the **scoring team kicks off** (opposite to 15s, where the conceding team restarts).
- **Scrums are 3 v 3.** Fewer lineout options. Far more space → tries roughly every 90 seconds; a single defensive lapse is often decisive.
- **Yellow card = 2 minutes** in the sin bin (a huge disadvantage on a 7-a-side field for that duration).
- **Knockouts:** level at full time → **sudden-death extra time** in periods of ~5 minutes, first score wins.
- **Tournament format:** pools (round-robin) over 1–2 days, then a **knockout** — typically a **Cup** bracket for the top finishers and secondary placings brackets. Pool ranking by match points (win 3 / draw 2 / loss 1 / forfeit 0 in the World Rugby system), then head-to-head, then points difference, then tries.


Sevens and 15s are **entirely separate populations** (RULES_RUGBY_UNION.md preamble, §4) — no scoring, margin or pace figure transfers between them.


### 11.3 New Zealand NPC (National Provincial Championship — "Hilux NPC")


**Governing body:** New Zealand Rugby. **Sponsor:** Toyota took title sponsorship from late 2025 (previously "Bunnings NPC"), branding it the **Hilux NPC**; the women's Farah Palmer Cup and the third-tier Heartland Championship are separate competitions.


**Structure (current format).** **14 provincial unions** in a **single division, single table** (the old Premiership/Championship two-division split with promotion/relegation has been dropped). Each team plays **10 round-robin matches** (an uneven fixture — not everyone plays everyone). August–October.


**Table and playoffs.** Standard union points + bonus points (try bonus, losing-bonus within 7). **Top 8** advance to **quarter-finals**, then **semi-finals**, then the **NPC Final** — hosted by the higher-ranked team at each stage.


**Ranfurly Shield.** A **challenge trophy** contested *within* selected NPC (and other) fixtures: the holder defends it in each home match; a challenger who wins takes the Shield. It does **not** affect the league table but is a major motivational and selection factor for the specific fixture in which it is on the line — flag it in the identity check.


**Analytical notes.** NPC squads are **below Super Rugby level** and rotate heavily around All Blacks/Super Rugby availability; depth, weather (spring in New Zealand) and travel matter. It is its own scoring population — do not import Super Rugby or Test rates.


### 11.4 In Extenso SuperSevens (France)


**Governing body:** Ligue Nationale de Rugby (LNR). France's domestic rugby-sevens championship.


**2026 format (new).** From the 2026–2027 season the competition is **fully gender-equal** and restructured into **two "summer stages"** (each a two-day event: a pool phase + a "night session" on day one, direct-elimination knockouts on day two — held **21–29 August 2026**) followed by a **finals stage** (5–6 February 2027, Plenitude/Paris La Défense Arena) that crowns the French champions.


**Field.** Men's: the **14 Top 14 clubs** plus the **French Barbarians** and **Monaco Rugby Sevens** (16). Women's: the **10 Élite 1 clubs**.


**Rules.** Standard World Rugby sevens laws (§11.2): 2 × 7 min (10 min for a final), drop-kick conversions taken quickly, scoring team kicks off, 2-minute yellow cards, sudden-death extra time in knockouts. Each stage produces stage points toward overall standings that seed the finals.


**Analytical notes.** SuperSevens uses **Top 14 club rosters**, but which players a club sends to a sevens weekend is highly variable and often not its 15s stars — participant identity and effective strength are very weakly predictable (`SFA-RUGBY-UNION` §10.3 sevens exposure chain; sparse-competition handling). Sevens tournaments have **large within-day variance**: a team can top its pool and lose a quarter-final to one intercept.


### 11.5 Identity checklist (rugby)


Resolve before any rate work: **which code and format** (15s vs 7s — never pooled); the **competition** (NPC / SuperSevens / other) and its **bonus-point and table rules**; the **stage** (round-robin / pool / quarter-final / final) and therefore whether a **draw is possible** or the match goes to **extra time / kicks**; the **red-card law** in force (straight red vs 20-minute red); whether the **Ranfurly Shield** or a similar trophy is on the line for that specific fixture; squad availability against higher-level competitions; and the operator's market endpoint for a knockout (regulation vs eventual winner).
