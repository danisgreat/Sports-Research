# Basketball analysis rules


> **2026-09-12 operational correction:** The dated section at the end of this file and RULES_GENERAL section 16.9 control over conflicting older probability, coupling and source claims.


> **`METHOD.md` is now the primary mandatory read (v4.0 comprehensive overhaul, 2026-09-06).** This file remains the full sport-specific reference: its `SFA-<SPORT>` algorithm and competition-rules section (`§9`/`§10`/`§11`) are consulted in full when forecasting this sport; `METHOD.md` states the cross-sport process once.


<!-- THREE-SOURCE-TIME-GATE-2026-09-19-CR4 -->
> **Current cross-sport authority — MDS-2026.09.19-v4.3 / CR-2026.09.21-3:** this sport module inherits the reconciled all-sports source, timing, settlement and distribution-construction controls. Historical issued cards retain their own revision.


Status: **ACTIVE**
Effective: **2026-09-06 (v4.0 comprehensive overhaul — see METHOD.md and FRAMEWORK_AND_GAME_LOG_OVERHAUL_REVIEW_2026-09-06.md)**
Method version: **MDS-2026.09.06-v4.0**
Applies with RULES_GENERAL.md, MODEL_AND_DATA_SPEC.md, ALGORITHM_PORTFOLIO_AND_EVALUATION.md, and NUMERICAL_TRAINING_SPEC.md.
Executable algorithm: **SFA-BASKETBALL (§8) — instantiates GFA-2 in RULES_GENERAL.md §11**
Numerical training specification: **NTS-2026.09.02-v0.3 — design only; no basketball model is fit**
Sport and competition rules reference: **§9 (added 2026-09-04; Copa Value/LNBP onboarding audit updated 2026-09-04)** — playing rules and the FIBA / WNBA / NBA rule differences, plus per-competition rules for every basketball competition in the prediction logs (WNBA; FIBA World Cup 2027 qualifiers; FIBA Asia Cup pre-qualifiers; FIBA Women's events; LNBP/Copa Value with unresolved-rule gates). Reference material for identity, state and settlement; it does not change `SFA-BASKETBALL`.


## 1. Identity and contract


Resolve league, season/rules era, regulation/OT treatment, venue, scheduled start, quarter/half/full-game phase, team/player statistic, line, and operator terms. NBA, WNBA, NCAA, FIBA, domestic leagues, summer league, and preseason have different clocks, foul rules, rotations, and overtime environments.


A phase already completed at issue is SETTLED_AT_ISSUE and unranked.


## 2. High-value inputs


### Participants and minutes


- Use the newest official injury/availability report and confirmed starting five.
- Separate active status from expected minutes, role, usage, and closing-lineup probability.
- Model replacement minutes and lineup combinations; uncertain minutes widen the distribution rather than making all player projections worthless.
- Record rest, back-to-back, travel, altitude, and recent overtime.


### Possession process


Use opponent-adjusted:


- possessions/pace and transition share;
- half-court efficiency and shot quality;
- rim, three-point, and midrange mix;
- free-throw rate;
- turnover and offensive-rebound rates;
- lineup-specific offence/defence;
- foul/bonus and late-game behaviour.


Raw points per game and recent shooting percentage do not substitute for possessions and shot profile.


## 3. Model


Exposure units are minutes, possessions, lineup stints, usage, and shot/rebound/turnover opportunities. Estimate possessions and per-possession efficiency jointly, with lineup branches and overdispersed shooting outcomes.


Model Q1, Q2, first half, second half, and full game as related but distinct segments. Derive all totals, spreads, winners, and props from one coherent joint game distribution.


For numerical training, benchmark a conditional empirical/joint score distribution and simple regularized possession × efficiency model before a possession/lineup state simulator. Candidate nonlinear models estimate possession, efficiency, shot/rebound/turnover or distribution parameters—not unrelated classifiers for each total/spread. The A2 candidate samples remaining possessions, lineup stints, shot/FT/turnover/rebound outcomes, foul/bonus, late fouling, blowout and overtime, then produces one joint team-score distribution. Direct bivariate Normal/Student-t or distributional boosting forms are challengers only with discrete/support, tail, covariance and held-out calibration checks. None is currently fit or validated.


## 4. Structural controls


1. **Nested rows are dependent.** One Q1/H1/full-game pace thesis gets one PRIMARY_FORMAL row unless another phase has independent evidence.
2. **Q1 pace does not determine Q2.** Use rotation, matchup, fouls, possessions, and shot quality for the next segment.
3. **Small H2H phase samples are weak.** A two-game Q2 acceleration pattern cannot control a current H1 direction.
4. **Minutes uncertainty is a distribution.** Do not use active/inactive as a full-workload binary.
5. **Blowout and garbage time are two-sided.** They change starters' minutes, bench pace, defence, and late scoring differently by contract.
6. **Late fouling and overtime are explicit tails.** Match the operator's inclusion rule.
7. **Rest is mechanistic.** Connect fatigue to pace, transition defence, shot quality, or minutes; no automatic Under/Over.
8. **Player props need role coherence.** Usage, minutes, teammates, defensive matchup, and stat opportunity must point in the same direction.
9. **Extreme spread size is not automatic safety.** For large mismatches, model opening separation, maximum-lead and closing-margin distributions separately. Rest/back-to-back, depth, bench quality, rotation intent, mercy/clock rules where applicable and garbage-time compression can move the final margin in opposite directions.
10. **Friendly halves can be different games.** Preparation matches require starter, bench and closing-lineup mixtures. A strong first half does not validate the full-game side when creators, minutes and late-game roles are deliberately rotated.
11. **Mismatch total and margin share a state tree.** Favourite offensive dominance can lift both margin and total, while underdog suppression can lift margin and lower the total. Derive both branches from the same possession/lineup simulation instead of treating an extreme handicap and an Under as independent safety plays.
12. **Current roster regime must be reconciled explicitly.** A missing rim protector, rebound anchor, primary creator or closer changes minutes, paint deterrence, rebounding, turnover pressure and closing-lineup quality. Old H2H and cover counts remain priors and cannot retain a high evidence grade unless the card explains why the present replacements preserve the old mechanism.
13. **Regulation and overtime attribution is exact.** Settle under the operator's endpoint, then report whether the threshold was already crossed in regulation. Do not describe an Over/Under miss as overtime-caused when regulation alone settled it.
14. **Rest is segmented, not a full-game scalar.** When a back-to-back/travel/fatigue branch is material, estimate its first-half versus second-half effect on transition defence, turnovers, defensive rebounding, shot quality, foul/bonus exposure and closing-lineup probability. If the card names a supported late-fatigue failure path, reconcile it with the side rank before issue.
15. **Low total can coexist with favourite blowout.** In depleted-roster or depth mismatches, model the underdog scoring floor and favourite defensive suppression separately from pace. An Under centre does not make the extreme underdog spread safe.
16. **Large spreads require factorised separation.** Before ranking a double-digit favourite, separately estimate possessions, shooting-efficiency advantage, rebound/turnover conversion, bench/rotation separation and true blowout probability. A small set of recent ugly opponent finals widens the lower tail but cannot by itself place the next game's central margin beyond the line.
17. **Totals require an explicit team-score budget.** For each plausible underdog score at its floor, centre and ordinary high state, solve the favourite score that crosses the total line, and repeat in the other direction. Compare those thresholds with the possession, transition, shooting and bench branches. An underdog offensive downgrade cannot support an Under when the favourite's ordinary high branch consumes the remaining budget.
18. **Late blowouts are multi-axis states.** Separate favourite starter reduction, favourite bench offensive quality/pace, favourite defensive-intensity change, underdog response scoring and closing-margin compression. Garbage time can raise the total while preserving or widening the margin; never apply one automatic scoring or compression sign.
19. **Roster names become exposure before effects.** For every decision-driving player, distinguish available, confirmed starter, bench/closing role, expected minutes, lineup stints, usage and replacement quality. A deep roster can sustain a scoring tail with fewer starter minutes; availability of a star is not the same as full-event star-lineup exposure.


## 5. Live state


Store score, quarter/clock, possession estimate, lineups on court, fouls/bonus, timeouts, rotations/minutes, shot profile, turnovers, offensive rebounds, injuries, and current pace. Rebuild remaining possessions and each later segment independently.


## 6. Sources and settlement


- Official league match centres and play-by-play control state/final.
- Official injury reports and team releases control availability.
- The [NBA statistics glossary](https://www.nba.com/stats/help/glossary) controls NBA definitions; use the equivalent official competition source elsewhere.
- Reputable play-by-play/tracking sources may support lineup and shot-quality features after coverage checks.


Settle from the official final and named statistic provider, preserving regulation/OT and phase boundaries.


## 7. Upcoming-game research sequence


1. Verify league/rules, regulation/OT terms, phase and statistic provider; freeze the complete candidate slate.
2. Retrieve official injury/availability status and likely starters before process history. Recheck the official release and confirmed lineup near tip.
3. Estimate active/start probabilities, minutes/lineup stints and replacement tree, then possessions, shot volume/mix, two- and three-point conversion variance, transition/turnover opportunities, free throws, offensive rebounds, bench scoring and matchup effects.
4. Generate lower, central, shooting-variance, foul/late-foul, blowout and OT branches. Split every material blowout into favourite sustain/slowdown, underdog response/suppression, pace/defensive-intensity and margin-compression states. Phase targets use their own remaining rotations and possessions. Material rest/travel effects are segmented by half and mechanism rather than applied as one full-game scalar.
5. When current roster evidence conflicts with old H2H/cover history, show the baseline/current-regime mixture and make the spread ranking explain why the named separation branch is or is not subordinate.
6. Build the team-score budget at the supplied total and spread, then derive team scores, winner, total and margin from the joint game object. If the line is inside the stated central corridor or ordinary branches cross both sides without explicit weights, cap the directional evidence at LOW under RULES_GENERAL.md. Player props use a linked `participation × minutes × usage/opportunity × rate` target, not team score alone.


Official league/team sources control current facts; official metric glossaries and audited play-by-play/tracking sources control their defined fields. Query/reference sites may cross-check trends but never override injuries, starters, rules or the operator's price.


## 8. SFA-BASKETBALL — sport forecast algorithm


Algorithm ID: `SFA-BASKETBALL`. Effective **2026-09-02**. Instantiates `GFA-2` (RULES_GENERAL.md §11) with basketball content. Process composition only; no fitted weight, scenario weight or published probability is introduced. NBA, WNBA, NCAA, FIBA, EuroLeague, domestic, summer-league and preseason populations are never pooled.


### 8.1 Blocking preconditions


| Precondition | Requirement | Failure output |
|---|---|---|
| `BK-P1` league and clock | League, season/rules era, quarter or half structure, period length, foul and bonus rules, overtime terms | `GATE-TARGET` failure; do not proceed |
| `BK-P2` availability | Newest official injury/availability report plus the confirmed starting five for both sides, re-handshaken at G31 | Model start and minutes mixtures; dependent rows cap at `FORCED RANK` / `MEDIUM-LOW` |
| `BK-P3` phase identity | Which segment each supplied row settles on: Q1, Q2, H1, H2, full game, and whether overtime is included | A completed segment is `SETTLED_AT_ISSUE` and unranked |
| `BK-P4` operator endpoint | Regulation or including overtime, for every total, spread and team total | Label `UNKNOWN_DEFINITION` and keep the overtime branch explicit |


### 8.2 Exposure chain


| Step | Output |
|---|---|
| `BK-S1` | Availability to expected minutes: start probability, minutes distribution, lineup stints, closing-lineup probability and replacement quality for every decision-driving player |
| `BK-S2` | Possession estimate for the frozen segment, with transition share, from both teams' opponent-adjusted pace |
| `BK-S3` | Shot mix by lineup: rim, three-point and midrange share, free-throw rate, shot quality |
| `BK-S4` | Per-possession efficiency by lineup, with turnover and offensive-rebound rates on both sides |
| `BK-S5` | Foul, bonus and late-game behaviour, including intentional fouling and clock state |
| `BK-S6` | Segment linkage: Q1, Q2, H1, H2 and full game as related but separately parameterised states, each with its own rotations |
| `BK-S7` | One joint team-score object with lineup branches and overdispersed shooting, from which every contract is queried |


Raw points per game and a recent shooting percentage never substitute for `BK-S2`–`BK-S4`.


### 8.3 Mandatory branch set


| Branch | Content |
|---|---|
| `BK-B1` | Central possessions with central efficiency for both sides |
| `BK-B2` | Shooting-variance branch: three-point rate high and low against the same possession estimate |
| `BK-B3` | Favourite sustain: starters retained, pace and defensive intensity maintained — raises margin and total together |
| `BK-B4` | Favourite slowdown: starter reduction with bench offence sustaining scoring — can raise the total while compressing or preserving the margin |
| `BK-B5` | Underdog response: opponent scoring against reduced defensive intensity |
| `BK-B6` | Underdog suppression: opponent floor state — raises margin and lowers the total |
| `BK-B7` | Foul, bonus and late intentional fouling adding free-throw possessions |
| `BK-B8` | Overtime under the exact operator endpoint |


`BK-B3`–`BK-B6` are the mismatch state tree. They must be enumerated separately for any double-digit spread; a large handicap and an Under may never be treated as independent safety plays.


### 8.4 Contract derivation map


| Contract | Queried from | Extra condition the mechanism must predict |
|---|---|---|
| Full total | Sum marginal of the joint object | The team-score budget: for each ordinary underdog score at floor, centre and high, the favourite score that crosses the line, and the reverse |
| Spread and handicap | Margin marginal | Opening separation, maximum lead and closing margin as three distinct distributions |
| Team total | Team marginal | That team's own possessions and efficiency, not the game pace alone |
| Q1, Q2, H1, H2 | The segment's own rotations and possessions | A prior segment is neither a ceiling nor a continuation rule |
| Player props | `participation x minutes x usage/opportunity x rate` | Teammate competition, defensive matchup and closing-lineup role |


### 8.5 Kill-path library


| Kill path | Defeats | Evidence origin |
|---|---|---|
| Bench offence sustaining pace after starter reduction | An Under justified by garbage-time slowdown | §4 control 18, C-PL5-BSK-MISMATCH-PATH |
| Underdog scoring floor plus favourite suppression | An Over justified by the favourite's ceiling; and, in reverse, a cushion justified by a low total | §4 controls 15 and 17 |
| Signed turnover and transition effects running both ways | A one-sign turnover argument; transition possessions add to the opponent even while the turnover suppresses their half-court offence | C-PL9-BSK-MISMATCH-FACTORS |
| A short set of recent opponent blowout finals | A central margin placed beyond the line on outcome history rather than on possessions and efficiency | §4 control 16, C-PL9-BSK-MISMATCH-FACTORS |
| Second-half fatigue on a back-to-back, expressed through transition defence and closing lineups | A side ranked on full-game strength while the card itself names the late-fatigue path | §4 control 14, C-PL7-BSK-REST-SEGMENT |
| Overtime supplying points that regulation did not | An Over recorded as validation of a regulation scoring centre | §4 control 13 |
| A missing rim protector, rebound anchor, primary creator or closer | Old head-to-head and cover history retained at high evidence | §4 control 12 |
| Q2 rotation and foul state differing from Q1 | An H1 row inherited from a Q1 pace read | §4 controls 1–3 |


### 8.6 Sport ordering overrides


1. Nested Q1, H1 and full-game rows sharing one pace thesis contribute one `PRIMARY_FORMAL` row. A derivative segment reaches a top slot only on independent segment evidence.
2. An extreme spread is not `OUTSIDE` corridor by size alone. Classify it from the factorised separation estimate in `BK-B3`–`BK-B6`.
3. Rest and travel enter as half-segmented mechanisms, never as a full-game scalar. If the card names a supported late-fatigue failure path, it must be reconciled with the side rank before issue.
4. Minutes uncertainty widens the distribution. It never converts an availability binary into a full-workload assumption, and it never makes a player projection worthless.
5. Cover counts, recent scoring averages and reputation are `E — diagnostic only`.


### 8.7 Pre-issue checklist


1. `BK-P1`–`BK-P4` status printed, with the availability release time.
2. Minutes and lineup-stint distribution stated for every decision-driving player, including replacements.
3. Possession estimate and shot mix stated before any total is discussed.
4. All eight `BK-B*` branches represented; team-score budget solved at the supplied total and spread.
5. For any double-digit spread, the four mismatch states enumerated separately.
6. Kill-path rows selected from §8.5 and reconciled against the issued order.
7. Segment rows carry their own rotations and possessions.
8. Overtime treatment stated for every total, spread and team total.
9. Injury report and confirmed five refreshed at G31 before the view is appended.
10. Recency block complete per §8.8: L5/L10/L15/L20 for both sides and for head-to-head, continuity count stated, trend verdict per metric, unique-event de-duplication done.
11. Environment block complete per §8.9: Venue classified; altitude, rest and travel entered through a named mechanism.
12. `REFERENCE_BASE_RATE`, exact threshold, population and denominator recorded for every supplied row per §8.10 as a descriptive diagnostic only; no reference-band, trend or slot-frequency adjustment may move an ordinal (G23.1).
13. Extra-condition support audit (G24) recorded for every handicap, team-total and cushion row; no retrospective contract-family penalty is applied.
14. Separation budget (G20.1) solved for every margin, handicap and cushion row by quarter, with starter, bench and closing-lineup states and the maximum-lead/compression path held separately.
15. Rank-1 implied-target interval (G25.1) stated in the unit of every other supplied line, each remaining row classified `COHERENT`/`PARTIAL_OVERLAP`/`DISJOINT`, and every aggregate budget re-solved conditional on the Rank-1 state.
16. Winner-and-cushion reconciliation (G30.1) whenever Rank #1 is an underdog cushion, with the outright-win and narrow-loss branch ordering stated. Example separation kill path for this sport: a fourth-quarter closing-lineup run.
17. Deficit attribution (G14.1) recorded for every weak, absent, returning or small-sample participant: which side's distribution moved and through which exposure step.


### 8.8 Recency, head-to-head and trend windows


Implements `GFA-2` step G13.1 (RULES_GENERAL.md §11.3B) and runs at that point in the algorithm, not at the end. Retrieval of L5/L10/L15/L20 for both sides and for the head-to-head series is mandatory; a window that does not exist is recorded with its true count and a missingness code.


Populate one windowed table per side with these metrics, and one head-to-head table:


| Window metric | Content |
|---|---|
| Pace | Possessions per 48 or per 40 minutes, opponent-adjusted |
| Efficiency | Offensive and defensive rating, opponent-adjusted |
| Shot profile | Rim, three-point and midrange share, three-point attempt rate and free-throw rate |
| Ball control and boards | Turnover rate and offensive-rebound rate for both sides |
| Margin shape | Final margins in each window, held separately from the win-loss count |
| Decision-driving players | Each player's own last 5/10/15/20 games: minutes, usage and the contract's stat |


**Head-to-head continuity.** Continuity means the same rotation and coach. A two-game head-to-head phase pattern cannot control a current segment, and a meeting played before a trade, an injury return or a coaching change fails continuity.


**Descriptive recency windows (G13.1; revised 2026-09-17).** Retrieve L5/L10/L15/L20 and continuity-qualified H2H with unique-event counts. These windows overlap. Monotonicity and dispersion among their averages are not a statistical trend/noise test. Report direction descriptively; estimate recency decay and opponent/regime effects using time-ordered validation. See SCORING_AND_VALIDATION section 5.


**De-duplication.** The windows overlap by construction and share matches with the head-to-head and venue series. Shrink from unique underlying events under G9; never treat L5, L10, L15 and L20 as four confirmations.


### 8.9 Environment and conditions


Implements `GFA-2` step G15.1 (RULES_GENERAL.md §11.3C). Venue classification for this sport is normally **INDOOR**.


| Field | Use in this sport |
|---|---|
| Venue classification | Indoor; record it and move to the rows below |
| Altitude | Denver, Mexico City and similar venues, entered through conditioning and pace, not as a label |
| Rest, travel and back-to-back | Segmented by half under §8.6, never a full-game scalar |


Failure to obtain the match-window forecast for an outdoor or open-roof event yields `WEATHER_NOT_AVAILABLE`, widened total and margin distributions, and a `LEAN` cap on every weather-dependent row. No factor above carries an automatic total direction.


### 8.10 Base-rate anchors and derived stat lanes


**Anchoring (G12.1).** Anchor spreads on the league frequency of covering at that number and totals on the competition scoring environment. A double-digit handicap is `CONJUNCT` and anchors below a match total of similar apparent confidence.


StatMuse is an accepted research accelerator for this sport under DATA_SOURCE_REGISTER.md §18, using the verified query patterns recorded there. Every returned row is date-checked and reconciled against the official league source before it is decision-driving, and StatMuse never controls participants, availability, rules, state or settlement.


**Derived and low-salience fields that are available and routinely skipped:**


| Field | Note |
|---|---|
| Closing-lineup probability | Distinct from minutes; controls late scoring and margin compression |
| Foul and bonus state | Feeds `BK-B7` free-throw possessions |
| Officiating crew pace and foul rate | Conditional only, and only where current data support it |


## 9. Sport and competition rules reference


Added 2026-09-04; last reviewed 2026-09-04. Standing reference for the playing rules of basketball and the competition-specific rules of every basketball competition in the prediction logs. Supports `BK-P3` (rule set and duration) and §6 settlement; introduces no rate, weight or ordering rule. **The single most important identity fact in basketball is which rule set applies — FIBA, WNBA or NBA — because it changes game length, the foul/bonus economy, overtime, and the three-point distance.**


**Maintenance (RULES_GENERAL.md §3, `G2`).** Before the first card of a new WNBA season, a new FIBA qualifier window, or a new tournament edition, re-verify the rule set (FIBA / WNBA / NBA), the roster and expansion state, the playoff/finals format and any in-season-tournament structure against the official body, and update this section **before** issuing the card. Basketball adds structural events regularly (the NBA play-in tournament, in-season cups, WNBA's move to a best-of-seven final and 15-team league). The first time a new basketball competition is forecast (an NBA card, a EuroLeague card, another national league), document its full rules — including whether it is FIBA or NBA rules — here first.


### 9.1 Universal basketball rules


**Objective.** Two teams of five on court. Score by putting the ball through the opponent's basket: **2 points** inside the three-point arc, **3 points** beyond it, **1 point** per free throw. Most points at the end wins; a tie forces overtime.


**Game clock.** Four quarters. **Stop clock** — the game clock stops on every whistle, made basket in the last minutes, timeout and out-of-bounds. Quarter length is rule-set-specific (§9.2).


**Shot clock.** The offence must attempt a shot that hits the rim within **24 seconds**. After an offensive rebound the shot clock resets to **14** (FIBA, WNBA, NBA all use 14). Failure = shot-clock violation, ball over.


**Possession and restarts.** Opening tip-off is a jump ball. Thereafter, held balls and other tie situations are resolved by the **alternating-possession arrow** in FIBA and the WNBA; the **NBA still uses jump balls** for held balls. After a made basket the opponent inbounds from the baseline without the clock starting until the ball is touched in-bounds.


**Fouls.** A personal foul is illegal contact. Shooting fouls → free throws (2, or 3 beyond the arc, or 1 + the basket if it went in). Non-shooting fouls → inbound, unless the team is **in the bonus / penalty** (over the team-foul limit for the period), in which case → free throws. **Player foul-out** limit and **team-foul bonus** thresholds are rule-set-specific (§9.2). **Technical fouls** (unsportsmanlike conduct, illegal substitution, etc.) and **unsportsmanlike/flagrant fouls** (excessive contact) award free throws **and** possession.


**Violations.** Traveling, double dribble, carrying, 3-second (offensive) lane violation, 5-second closely guarded (FIBA/college), 8-second backcourt (FIBA/WNBA/NBA), backcourt ("over and back"), goaltending / basket interference, out of bounds, kicked ball.


**Substitutions and timeouts.** Unlimited substitutions at dead balls. Timeout counts, who may call one, and when, are rule-set-specific.


**Overtime.** **5 minutes**, repeated until a winner — in every professional rule set. Team fouls usually carry over or reset per rule set (NBA/WNBA: fouls carry; FIBA: bonus is per period and OT counts with the 4th quarter). Full-game betting contracts **include overtime** unless the operator states "regulation only" (RULES_BASKETBALL.md §1; the log's WNBA cards state this explicitly).


### 9.2 Rule-set differences — FIBA vs WNBA vs NBA


| Element | FIBA | WNBA | NBA |
|---|---|---|---|
| Game length | 4 × 10 min (40) | 4 × 10 min (40) | 4 × 12 min (48) |
| Overtime | 5 min | 5 min | 5 min |
| Shot clock / offensive-rebound reset | 24 / 14 | 24 / 14 | 24 / 14 |
| Three-point distance | 6.75 m (6.60 m corner) | 22'1¾" (6.75 m); 22' corner | 23'9" (7.24 m); 22' corner |
| Lane (key) | Rectangular; **no defensive 3-second rule** | Rectangular; **defensive 3-second violation** (tech FT + possession) | Rectangular; **defensive 3-second violation** |
| Personal fouls to foul out | **5** | 6 | 6 |
| Team-foul bonus | **5 per quarter** → 2 FT (OT counts with Q4) | 5 per quarter → 2 FT; also 2 FT on any foul in the last 2 min if the team already has 1; fouls **carry into OT** | Same structure as WNBA (bonus at 5, or 4 in the last 2 min); fouls carry into OT |
| Held ball | Alternating-possession arrow | Alternating-possession arrow | **Jump ball** |
| Goaltending / ball on the rim | Ball is **live once it touches the rim** — either team may play it (no basket interference off the rim) | NBA-style basket interference (cannot touch ball in the cylinder / on the rim on a downward flight to the basket) | NBA-style basket interference |
| Timeouts | Coach requests only, at a dead ball / made basket; 2 in H1, 3 in H2 (max 2 in last 2 min), 1 per OT; **no advance-the-ball** | Team timeouts; **advance-the-ball** to the frontcourt on a timeout in the last ~1–2 min | Team timeouts; advance-the-ball in the last 2 min; coach's challenge |
| Coach's challenge | Competition-dependent (some FIBA events use one) | Yes (one) | Yes (one, retained if successful) |
| Continuous vs stop clock in low minutes | Stop clock throughout | Stop clock | Stop clock |


**Analytical consequences.** A FIBA game is ~17% shorter than an NBA game (40 vs 48 min) and its foul economy is different: fewer fouls to foul out (5) and a quarter-reset bonus mean **star foul trouble bites earlier** and free-throw volume is lower per minute. FIBA's "no defensive 3 seconds" plus a live-off-the-rim ball favour **interior defence and second-chance points**. Never transfer an NBA or WNBA per-game total or pace figure into a FIBA game without rescaling to 40 minutes and the FIBA foul environment.


### 9.3 WNBA


**Structure (2026).** **15 teams** (Portland Fire and Toronto Tempo added for 2026), nominal Eastern/Western conferences but a **single league table for playoff seeding**. **44-game** regular season. Rosters **11–12 players** (hard salary cap frequently forces 11). WNBA plays under its own rule book, which is close to the NBA's but on a **40-minute** game (four 10-minute quarters).


**In-season tournament.** The **Commissioner's Cup** — designated early-season games count both for the standings and a separate Cup table; the two Cup finalists play a standalone final that does **not** count in the standings. Treat a Commissioner's Cup final as its own event/population.


**Playoffs (2026).** **Top 8 by record**, no conference requirement. **First round: best-of-three** (higher seed hosts Games 1 and 2). **Semi-finals: best-of-five.** **Finals: best-of-seven**, 2-2-1-1-1 (higher seed hosts Games 1, 2, 5, 7) — best-of-seven since 2025. Higher seed has home-court throughout. No play-in tournament (that is NBA-only).


**Settlement (WNBA).** Full-game lines include overtime. Quarter/half lines settle at the buzzer of that period. Player-prop providers differ on whether OT counts toward player totals — freeze the provider. A forfeit/abandonment is operator-specific.


### 9.4 FIBA national-team competitions


All FIBA events use the **FIBA rule set** (§9.2): 40-minute games, 5 fouls out, per-quarter bonus at 5, alternating possession, live-off-the-rim ball.


**FIBA Basketball World Cup 2027 — Qualifiers (the "Qualifiers" and "Pre-Qualifiers" cards).**
- **80 teams** across four regions (Africa 16, Americas 16, Asia/Oceania 16, Europe 32). **Six windows**, Nov 2025 → Mar 2027 (Africa five windows). Each window is a ~9-day FIBA international break with **two games per team**.
- **First round:** groups of four, **home-and-away round-robin** over the first three windows. **Second round:** the top three of each first-round group merge into new groups of six, **carrying their head-to-head results forward**, and play the teams they have not yet met, over windows 4–6.
- Qualification slots per region: Europe 12, Americas 7, Africa 5, Asia/Oceania (with the co-host) a similar number — the top teams in the second-round groups qualify for the 32-team World Cup.
- **Pre-Qualifiers** (e.g. the "FIBA Asia Cup 2029 Pre-Qualifiers" card, and European pre-qualifiers) are a preliminary knockout/group stage for lower-ranked nations to reach the main qualifiers — small home-and-away group or two-legged ties, same FIBA rules.
- **Standings within a group:** points (win 2, loss 1, forfeit 0), then, if level, the **mini-league of results between the tied teams** (head-to-head points, then head-to-head point difference, then head-to-head points scored), then overall point difference. Note this is **not** net-points-first like some leagues.
- **Roster:** 12 players per game from a wider registered pool; **NBA and top-league players are frequently unavailable in qualifier windows** because the windows fall inside club seasons — participant identity and effective strength are highly window-dependent. A qualifier "national team" is often a domestic-league + second-tier-Europe roster, not the World Cup roster.


**FIBA Women's Basketball World Cup 2026 and its warm-ups.** Same FIBA rules. Warm-up / preparation games are **friendlies** — treat as a phased, rotation-heavy population (RULES_GENERAL.md friendly handling), not competitive form.


### 9.5 LNBP (Mexico) and the 2026 Copa Value


**Onboarding status: `PARTIAL / BLOCKING FOR A FUTURE CARD`.** P-279 was the first Copa Value card and was issued before this competition existed in the reference section, so it failed the new-competition onboarding requirement in RULES_GENERAL.md §3. This subsection repairs the verified reference facts after the event; it does not retroactively make P-279 compliant and it is not permission to forecast the next Copa/LNBP event until the unresolved fields below are closed.


**Verified 2026 competition identity.** The Copa Value is an LNBP mid-season tournament for the top eight teams after the first half of the 2026 regular season. The 2026 edition runs 3–6 September at the Gimnasio Marcelino González in Zacatecas, using a single-game, single-elimination bracket: four quarterfinals, two semifinals and a final. Mineros is the arena's resident team and therefore had a real host/home-floor state against Abejas; the single-site label must not be converted into neutral-court treatment. The [Government of Zacatecas event release](https://www.zacatecas.gob.mx/zacatecas-epicentro-del-basquetbol-nacional-con-la-copa-value-2026-gobernador-david-monreal/) owns the host venue/date/format statement; the dated [NTR Zacatecas match report](https://ntrzacatecas.com/2026/09/mineros-avanza-a-las-semifinales-de-la-copa-value/) confirms that Mineros–Abejas was a quarterfinal, that Mineros won 96–86 and that the winner advanced to the 5 September semifinal. Named reporting may corroborate those fields but does not own the league's playing rules.


**Playing-law and roster gap.** No accessible 2026 LNBP/Copa Value regulations or field-owner rulebook was recovered in the P-279 promote/archive audit. Do **not** infer from the league's professional status, FIBA affiliation, a live-score front end or a sportsbook that the exact LNBP clock, bonus, challenge, roster/import, overtime, abandonment or player-eligibility provisions equal another FIBA competition. [FIBA's official download page](https://about.fiba.basketball/en/services/resource-hub/downloads) states that the 2026 FIBA rules become effective on **1 October 2026**; on 3 September the 2024 FIBA edition was still the current international rule baseline. That date distinction does not establish which edition or local variations LNBP adopted.


Before another LNBP or Copa Value card, obtain an exact current league regulation, competition bulletin or field-owner statement and record all of the following at `BK-P1`/`G2`: period length and clock; foul-out/bonus/challenge rules; overtime and tie resolution; Copa bracket/seeding and any reseeding; home/bench designation at the single site; roster size and game-day activation; foreign/import-player and replacement eligibility; postponement/forfeit/abandonment treatment; and whether the Copa result affects the regular-season table. Until that packet is complete, `BK-P1 = FAIL`, the event is not forecastable, and no LNBP rate may be pooled with a generic FIBA population.


**Settlement.** Freeze the operator's own regulation-versus-overtime, postponement, abandonment and player-prop terms. Without them, full-game side/total action is `UNKNOWN_DEFINITION` even if a research settlement is direction-invariant. P-279 did not require overtime and every recovered high-quality final agreed on 96–86, so its winner, ±5.5 and 169.5 result fields are direction-invariant; that does not validate an unstated operator rule. Quarter/player detail remains provisional unless an exact LNBP field-owner box or a provider with a frozen definition is recovered. Fox Sports México's statement that Mineros won all four quarters conflicts with the provisional 20–23 third-quarter row and may not control phase settlement.


**Source state at review (2026-09-04; superseded for results by §"2026-09-17(b)" — the domain now returns HTTP 200 with a JavaScript-only shell, and the per-Jornada finals are recoverable by rendering `lnbp.mx/<Team>/team_results.html`).** `https://lnbp.mx/` identifies the field owner but returned HTTP 403 to the scripted research route; the official mobile-app listing did not expose a validated API, stable event IDs, correction history or use/retention terms. Use the exact LNBP record when accessible; otherwise seek an official club/static report and then two independent dated high-quality reports for a provisional final. Never upgrade the fallback into a league-wide structured-stat source.


### 9.6 Identity checklist (basketball)


Resolve before any rate work: **rule set (FIBA / WNBA / NBA / other league)** and therefore game length, foul-out limit, bonus threshold, three-point distance and overtime economy; competition and stage (regular season / in-season cup / qualifier window / knockout / friendly); roster availability for the specific window; whether the contract is **regulation-only or includes overtime**; the standings tiebreak system if the card touches qualification; and the operator's forfeit/abandonment rule.


## September 5 settlement learning — prospective SFA amendment


At possession/shot-mix, availability and G20.1 terminal-allocation steps, separate (a) opponent scoring suppression, (b) favourite scoring opportunities and (c) margin continuation/compression. Injury to a rim protector can improve the opponent's paint efficiency without proving a low team total for the injured player's team. Map replacement minutes and perimeter volume; do not import world rank or raw warm-up scores as a possession forecast.


P-284 had Under plus USA cover; China's +29.5 failed even at 61 points. At USA 94, the China-cover boundary is 65 and the Under boundary 67. Use exact algebra rather than “below 60” as the only cover-failure path. Bench participation does not imply margin compression: last-quarter scoring belongs to both teams.


P-285's printed score families all had Nigeria ahead despite a Korean scoring/upset route in prose. Both teams must have contract-evaluable ordinary win/separation branches when supported, under L-070. Record three-point **attempt volume and conversion** separately; do not infer fast pace solely from the final 180 or treat FIBA efficiency 31 as 31 points. Candidate C-P293-BK-ALLOCATION remains untested; no national-team or injury coefficient changes.




Full evidence and frozen-card comparisons: [September 5 audit](COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md).


## September 5(b) settlement learning — P-294–P-305 second continuation


Two FIBA Women's World Cup group-stage cards settled this pass with opposite outcomes from opposite framings, plus one AFLW-style large-cushion confirmation carried over from `RULES_AFL.md`'s own cohort (`P-293` Gold Coast +13.5).


**`P-299` (Mali vs Spain) — major upset; L-076.** Mali won 82-73, outscoring Spain 31-19 in the third quarter — the exact mechanism ("Mali's elite offensive rebounding and Koné/Sangaré/N'Diaye interior/creation keep Spain from finishing defensive possessions and compress the margin") the card itself had named as Spain -25.5's kill path. The reference corridor was still anchored close to Spain's Aug 29 friendly win margin (97-58, a 39-point win) despite the card explicitly recording that Spain were missing five eventual rotation players in that friendly and that **Sika Koné, Mali's best player, did not appear in the friendly's box score at all**. **New rule:** an exhibition/preparation-game margin must be excluded from anchoring the reference corridor whenever either side's core rotation is confirmed absent by name from that exhibition; a same-tournament data point for the affected team's current full roster (here, Mali's competitive 97-102 near-upset of Japan in the tournament opener, already on record) must be weighted above the stale friendly.


**`P-303` (Nigeria vs Hungary) — clean top-two win.** Nigeria won 81-53, landing almost exactly inside the card's own stated 136-149 total corridor and 72-78/64-71 team corridors. The card used a conservative framing — backing the stronger, higher-ranked side's floor via a +25.5 cushion rather than an aggressive spread-cover on the favourite — and both the cushion and the Under total won.


**Cross-card contrast — new candidate `C-PL15-BSK-CUSHION-VS-SPREAD`.** In the same session, three large-cushion "team getting points" rows were issued (`P-293` Gold Coast +13.5, `P-299` Mali +25.5, `P-303` Nigeria +25.5) and all three covered, while the one large-favourite-spread row issued (`P-299` Spain -25.5) lost. This is a three-and-one same-session sample, tracked as a candidate only — no automatic preference for cushion framing over spread framing is adopted from it, but it is a specific, falsifiable pattern worth testing prospectively per LEARNING_REGISTER.md.


**Kill-path library addition (§8.5):**


| Kill path | Defeats | Evidence origin |
|---|---|---|
| Either side's confirmed core-rotation absence from a cited preparation/exhibition game | A reference corridor anchored to that exhibition's margin | `P-299`; L-076 |
| A same-tournament data point for the affected team's current full roster outweighing a stale core-absent friendly | The same anchoring error, from the opposite evidentiary direction | `P-299`; L-076 |


Full evidence: [PREDICTION_LOG_COMBINED_2.md, 2026-09-05(b) section](PREDICTION_LOG_COMBINED_2.md#component-import--p-294p-305-second-continuation--2026-09-05b).


## September 6 settlement learning — the pace × efficiency tail, worked on both sides


`P-299` and `P-303` were issued the same day, in the same competition, with structurally identical slates — a large handicap at Rank #1 or #2 and a full-game total alongside it. One failed on both top rows; the other won both. Under `G20.2` they separate cleanly, and the separation is arithmetic that was available before either tip-off.


| Card | Line | Actual total | Tail-budget position |
|---|---|---|---|
| `P-299` Mali (W) v Spain (W) | `Under 144.5` (rank #2) | **155** | Spain's plausible upper output plus Mali's median lands essentially **on** the actual 155 — the row was `TAIL_EXPOSED` and the card had no mechanism sentence for why that combination could not recur |
| `P-303` Nigeria (W) v Hungary (W) | `Under 145.5` (rank #2) | **134** | Both sides' central outputs sat comfortably below the line with room to spare — not `TAIL_EXPOSED` |


**Required from now on, `SFA-BASKETBALL`:** the tail budget is computed as **pace × efficiency at the upper decile**, expressed in points, not possessions. Take each side's second-highest L10 possessions figure `Poss` and its second-highest L10 offensive rating `ORtg` (points per 100 possessions), and compute `points = Poss × ORtg / 100` — **the /100 normalisation is required and was omitted in the original wording (correction, 2026-09-06(d))**; without it the units do not resolve to points. Hold the opponent at its median defensive rating for the symmetric term. Print the implied total. **`TAIL_EXPOSED` is disclosure only per `RULES_GENERAL.md` §15 — the prior hard bar ("may not be Rank #1") is withdrawn and reclassified as `CANDIDATE`, pending its own prospective test.**


`P-299` also remains the origin case for `L-076` — a 39-point preparation-game margin against a Mali side missing five of its eventual finalists anchored the corridor. The tail budget and `L-076` are complementary: `L-076` says the anchor was wrong, `G20.2` says the anchor was also never stress-tested against Spain's own upper output.


### Kill-path library addition (§8.5)


| Kill path | Defeats | Evidence origin |
|---|---|---|
| **Upper-decile pace blowout** — the favourite's own high-tempo mode clears the total on its own, regardless of the underdog's scoring | A full-game `Under` ranked on the underdog's low offensive rating | `P-299` (155 against `Under 144.5`) |
| **Quarter-level regime break** — one quarter's swing (Mali 31-19 in Q3) inverts both the handicap and the winner in a single ten-minute window | A large handicap justified by season-long ratings without a quarter-level variance term | `P-299` — reinforces `L-070` |




### Cross-sport gates instantiated here (v3.7)


| Gate | Sport-native instantiation |
|---|---|
| `G10.2` settlement-source pre-registration | FIBA, WNBA and NBA events settle from the competition's official box score; ESPN's `basketball/<league>/summary` is the structured corroboration lane. LNBP and comparable leagues need their own named endpoint per `SRC-BB-LNBP-OFFICIAL`. |
| `G14.2` coaching / bench / rotation record | Record the head coach, the confirmed inactive list, and the rotation depth (how many bench players average ≥15 minutes across the L10). International tournaments rotate heavily in group play — record the qualification state as a rotation signal. |
| `G20.2` distributional tail audit | Derive tail and boundary mass from the **same frozen basketball joint score distribution**: possessions/opportunity, minutes and usage mixtures, lineup state, shot mix/efficiency with shrinkage and uncertainty, rebounding/turnovers, fouls/bonus, garbage-time and overtime branches. Historical second-highest/median or hand-built upper-decile stress sums are superseded as active ranking gates. |
| `G21.1` exact target geometry | Map every supplied total/phase-total to its exact settlement event and derive WIN/PUSH/LOSS (plus void/censoring where applicable) from the same frozen sport-native PMF/CDF or coherent branch mixture. Historical path-count/category labels have no mandatory ordinal effect and are not a substitute for the distribution. |
| `G26.1` no universal separation floor | Print any relevant reference base rate and `rank_gap` descriptively. **No 40–60% or other pooled probability band can disqualify Rank #1.** Rank by exact marginal likelihood from the frozen joint distribution plus robustness/evidence uncertainty; precise probabilities require the validated-model gate. |


**Pre-issue checklist additions (this sport):** settlement endpoint named per row; coaching/bench/rotation record for both sides with missingness codes; tail-budget sums printed against every total line; path-geometry class and `N` printed for every total and phase-total row; separation-floor result stated for Rank #1.


Full narrative and evidence: [`IMPROVEMENT_PLAN_2026-09-06.md`](IMPROVEMENT_PLAN_2026-09-06.md). Controlling gate text: [`RULES_GENERAL.md` §13](RULES_GENERAL.md).


## September 5 implementation after freeze confirmation


**ACTIVE REQUIRED PROCESS — MDS-2026.09.05-v3.6 / L-068–L-072.** Build both teams’ scoring allocation from available possessions, shot opportunities/quality and rotations. Include each side’s supported win/separation branch and late-quarter allocation. A missing player changes supported role/exposure inputs; it does not by itself justify an opponent scoring ceiling or a pace claim.


At final delivery, record the preferred total direction for each exact target, the strongest evidenced failure path for ranks #1 and #2, and whether both can win under the stated joint scenario. Rank by supported marginal likelihood; do not promote an opposite pick solely to manufacture one O/U win. At settlement, keep all issued wins/losses, including defective reasoning, in the applicable historical scorecard and review failed #1/#2 and preferred totals.


[Eligibility policy](PERFORMANCE_ELIGIBILITY_POLICY.md): non-live history is user-confirmed frozen pre-game; explicit live-issued views stay separate. These process repairs are implemented now. Numerical weights and predictive-lift claims need a later frozen comparison; historical origin games do not supply those completions.


## 2026-09-06(f) — settlement and retrospective addendum


P-299 roster labels are team-specific: Spain lacked five eventual Spain rotation players in the friendly, with Mali’s Koné separately absent. Reconcile current competitive evidence with the reference corridor; no universal zero-weight-for-friendlies rule is inferred. P-303 winning cushion/Under still missed both team-score corridors, total corridor and margin corridor. Audit winners as rigorously as losers; no automatic cushion preference.


Full frozen ranks, actual drivers, knowability and smallest fixes: [PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md). Reinforcement only; METHOD v4.0 remains controlling and no new predictive weighting is promoted.


## 2026-09-09 settlement learning — P-334 (no forecast), P-344


`P-334` (Germany 83–58 Mali) was an administrative no-forecast closure — live-state gate failed after tip; a draft ranking existed but was not delivered. No retrospective model weight from an unpublished draft (`L-117`).


**`P-344` — Hungary 84–63 Japan (FIBA W World Cup, Qualification to QF) — deep Rank-#1 retro.** Frozen card: R1 `Japan +3.0` (p0.56 win), R2 `Over 146.5` (p0.54), R3 `Under 146.5` (p0.46), R4 `Hungary -3.0` (p0.37 win); potential winner Hungary (54%). Result: **Hungary +21, total 147.** Rank #1 lost by a large margin; `Over 146.5` survived by 0.5 (a boundary escape, not validation of the 149.5 centre); potential winner correct.


*What went right:* the size/rebounding mismatch (Hungary 43.7 RPG vs Japan 31.7; paint edge through Juhász + Takács-Kiss) was correctly identified as the foundation, and Hungary was correctly the likelier winner (control 11, control 12).


*What went wrong — corrected on second-pass research (2026-09-09).* The first reading called Lelik's 23 points an under-weighted "breakout". Opening the FIBA official player profiles — **already listed in the card's own source register** — shows it was not a breakout at all, and that the real failure was a **participant-exposure retrieval gap**:


| Hungary scorer, pregame (3 group games) | PPG | Minutes | In the card as… |
|---|---:|---:|---|
| Dorka Juhász | 17.0 | — | quantified line |
| Virág Takács-Kiss | 13.0 | — | quantified line |
| **Réka Lelik** | **8.7** (8 / 14 / 4) | **~26.3** | **an unquantified name** |


Lelik was Hungary's **third-highest scorer**, playing starter-level minutes, with 4.3 RPG and 3.5 APG, and a pregame range that already included a 14-point game. The card printed quantified exposure for the two players above her and carried the third as a bare name in a list. **A blowout requires a third scorer, and the card's margin distribution contained no third scorer with a number in it** — which is mechanically why a symmetric ±10–12-point width around Hungary +0.5 was the output. Her 23 was an upside game (~2.6× her pregame mean), not a black swan; FIBA's own framing of Hungary as a "Twin Towers" side is precisely the shape that transfers usage to a third option when the defence collapses inside.


Two further items: Japan's perimeter *floor* was set by 11.1% and 23.3% three-point shooting in its two European group losses, not by a tournament average inflated by a record 20-three game against Mali. And Saki Hayashi's 9th-minute broken arm (8 minutes played) was a genuine in-game shock, **not** a pregame model miss (`L-117`) — it does not excuse the separately underweighted Hungary separation branch.


This is an instance of the cross-sport retrieval gate **`RULES_GENERAL.md` §16.5(c) / `G-L7`**: an aggregate ("the leaders are A, B, C and D") stood in for a per-player record that was available and would have changed the margin width.


### Structural control additions


20. **Quantify every rotation-level scorer, not just the two most-cited names.** `BK-S1` already requires expected minutes and usage "for every decision-driving player"; this control fixes the threshold so it cannot be satisfied by a leaders list. **Print a quantified exposure line — PPG, minutes, rebounds, assists over the retrieved window — for every player above roughly 20 minutes a game or in the team's top three scorers, on both sides.** A player carried as a bare name inside a phrase like "the leaders include A, B, C and D" is `AGGREGATE_ONLY` and the margin/total rows that depend on the team's scoring ceiling are capped (`RULES_GENERAL.md` §16.5(c)). *Origin:* `P-344` — Hungary's third-highest scorer (8.7 PPG on ~26 minutes) was the only one of the top three without a number on the card; she scored 23 and the margin distribution had no room for her.


21. **Secondary-scorer usage transfer in a mismatch.** When one team holds a clear structural advantage (size/rebounding/pace) and the opponent's defence must key on the favourite's primary option(s), model an explicit branch in which a **secondary or tertiary scorer** absorbs that usage and produces the blowout. A "twin towers"/interior-dominance identity is exactly the shape that transfers usage outward when the paint is collapsed on. Conversely, when the opponent's offence depends on volatile perimeter shooting, its **floor is set by its worst recent same-regime shooting games, not by a tournament average** inflated by one outlier game — `P-344`: Japan's 11.1% and 23.3% three-point games against European opposition were the relevant floor, not the average that included a record 20-three game against Mali. Carry both into the total and margin distribution.


### Applying G-L1 / G-L4 here


- **`RULES_GENERAL.md` §16.5(a) / `G-L1`:** the joint game object must enumerate the **margin families** (favourite blowout 15+, clear win 6–14, close 1–5 or push, underdog win) with explicit mass, and the **total families**, and place every §8.5 kill path as a weighted branch. A representative Rank-#1 final score is written and checked against the spread, the total and any team-total line. `P-344`'s symmetric ±10–12 width around +0.5 would not have survived this: the size mismatch plus Japan's perimeter volatility puts material mass on a 15+ Hungary margin.
- **`G-L4`:** winner and spread are separate answers from the same family set. A correct winner call with a badly compressed margin distribution (`P-344`) is a **margin-model failure**, recorded as such — not a partial success because the winner was right.


### Kill-path library addition (§8.5)


| Kill path | Defeats | Evidence origin |
|---|---|---|
| A secondary/tertiary scorer absorbing usage for a blowout while the defence keys on the primary star(s) — **especially one already in the team's top three who was carried on the card as a name without a number** | An underdog `+handicap` or an `Under` ranked on a compressed cross-opponent margin centre | `P-344` (Lelik, 8.7 PPG / ~26 min pregame → 23 points); controls 20, 21, 11; `G-L7` |
| An opponent's volatile perimeter offence reverting to its worst recent same-regime shooting rather than its tournament average | An `Over` or an underdog `+handicap` built on the opponent's average scoring | `P-344` (Japan 11.1% / 23.3% vs Europe, average inflated by a 20-three outlier); control 21 |


### Pre-issue checklist additions (this sport)


- **Quantified exposure line printed for every top-three scorer and every ~20+ minute player on both sides** (control 20); any such player left as a bare name is recorded `AGGREGATE_ONLY` and the dependent margin/total rows are capped.
- **Margin-family enumeration with explicit mass** — favourite blowout (15+), clear win (6–14), close (1–5 / push), underdog win — plus the total-family enumeration, with every §8.5 kill path placed as a weighted branch (`RULES_GENERAL.md` §16.5(a) / **`G-L1`**).
- **G-L2:** State the prior and scenario probabilities. Symmetric uncertainty around an unchanged prior affects width; hierarchical shrinkage or asymmetric scenarios may change both mean and variance. Regenerate all dependent probabilities; unsupported directional adjustments remain prohibited. SCORING_AND_VALIDATION section 5 controls.
- **G-L8:** Derive each total/spread probability from the exact joint PMF/CDF and settlement endpoint, with push mass. Absolute normalised distance does not order probabilities across different distributions. No missing width or realised result justifies an invented probability.
- Representative Rank-#1 final score written and checked against the spread, the total and any team-total line.


## 2026-09-11 settlement learning — `P-358`, `P-359`, `P-360`, `P-367`, `P-371`


Five FIBA and Asian Games cards ([`PREDICTION_LOG_COMBINED_3.md` §"2026-09-11"](PREDICTION_LOG_COMBINED_3.md)). Rank #1 **3 W / 2 L** (`P-358`, `P-371` lost). Top two both won only on `P-367`. Winners 3 / 5. The preferred total was an **Under on all five cards: 2 W / 3 L.** None of the five printed a numeric width, a normalised edge or a margin-family table, although the issuing session had declared `G-L8` and `G-L2` in force. Learning-only; no fitted weight or ordinal bar (`L-087`).


### Measured precision — six cards (incl. `P-344`)


| Card | Stated total centre | Actual | Error | Stated margin centre | Actual margin |
|---|---:|---:|---:|---|---|
| `P-344` | 149.5 | 147 | −2.5 | HUN +0.5 | HUN +21 |
| `P-358` | 137 | 147 | +10 | CHN +7 | CHN +3 |
| `P-359` | 156 | 163 | +7 | JOR +6 | **TPE +3** |
| `P-360` | 155 | 148 | −7 | KOR +11 | KOR +16 |
| `P-367` | 152 | 151 | −1 | FRA +26 | FRA +29 |
| `P-371` | 144 | 167 | +23 | BEL +10 | **GER +19** |


Total error: mean **+4.9**, mean absolute **8.4** points. The three total misses all came in **competitive or upset** games (`P-358`, `P-359`, `P-371`); the two hits came in favourite separations (`P-360`, `P-367`). That is the coupling written up as control 24. Six cards is a watch item, not a bias estimate.


### What went right (keep it)


- **`P-367` is the model:** centre 89–63 against an actual 90–61, derived from rest asymmetry, pressure and turnovers. France won by 29 while shooting *worse* than China (FG 44% v 46%; 3P 37.8% v 43.8%) — the possession-volume mechanism, correctly identified.
- **Availability research that mattered:** An Youngjun out and Choi Junyong not yet with the Korea squad (`P-360`, Korean-language sources, `L-067`); Li Yueru's passport absence from the China roster (`P-367`); a secondary preview's "full-strength rosters" claim correctly overridden.
- The margin read in `P-358` (Puerto Rico's pressure against China's turnovers) and in `P-359` (Chinese Taipei's guard core) was right — the cushions won.


### What went wrong, linked to earlier lessons


1. **Observed top-two splits (`P-358`, `P-359`, `P-360`); dependence not established.** Exactly one of the top two won on each card. Extends controls 11 and 15. → **control 24**; `RULES_GENERAL.md` §16.5(f).
2. **Small-sample shooting treated as direction (`P-371`, and `P-358` in reverse).** A three-game three-point gap (38.1% v 25.2%) was a Belgian mechanism — the later 1.7-SE calculation used unsupported equal attempt assumptions and is withdrawn — and reversed. Puerto Rico's cold 25.9% was used as a floor under the Under; they shot 38.9%. Repeats `G-L2` and control 21. → **control 22**; §16.5(g).
3. **Control 20 broken two days after adoption (`P-358`).** Puerto Rico's leaders were carried as names without numbers. Trinity San Antonio's 35 points came on a pre-game line of about **9.0 PPG** (derived from her 15.5 average over four games) — an aleatory magnitude (`G-L6`) — but her 5.0 steals a game was exactly the transition route that fed the Over.
4. **No underdog-separation family (`P-371`).** Four German mechanisms were listed; every German-positive branch was a close game; Germany won by 19. → **control 23**.
5. **No widths or normalised edges on any card** (`G-L8` declared, not executed). → `RULES_GENERAL.md` §16.8.


### Structural control additions


22. **Shooting uncertainty with actual denominators (corrected 2026-09-12).** Print attempts, makes, minutes and opponent/time windows for 2P/3P/FT inputs. Use a suitable interval and explicit prior/shrinkage sensitivity; do not invent n, assume identical shrinkage in both directions, or use a two-SE cutoff as proof of noise. Unknown attempts stay unknown. A worst observed game is not a physical lower bound. See corrected G-L11 and section 16.9.


23. **Spread family including either team separating.** Use exhaustive nonoverlapping margin ranges with explicit mass, respecting draw/OT conventions. Include a plausible underdog-separation state whenever the current evidence permits it; no arbitrary two-mechanism threshold or independence claim is required. Named rebounding, bench, crowd and rest factors may overlap. Representative scorelines cannot determine branch probabilities. P-371 and P-242 motivate this disclosure, not a fitted mass.


24. **Conditional margin-total coupling (corrected 2026-09-12).** Late fouls, rotation and transition can connect margin and total, but their signs depend on the matchup and realized scoring process. Close games can be low scoring; separation can be high scoring. Compute joint probability from one model or state JOINT_UNQUANTIFIED with bounds. Do not label underdog cushion plus Under intrinsically anti-coupled or infer correlation from a few split results. See corrected G-L10.


### Kill-path library additions (§8.5)


| Kill path | Defeats | Origin |
|---|---|---|
| A competitive underdog (the state that wins its cushion) lifting the total through late possessions, fouls and its own transition scoring | An Under paired with the underdog's handicap | `P-358`, `P-359`; control 24 |
| A small-sample shooting gap reverting on the night | A spread or total leaning on tournament 3P% over ≤4 games | `P-371`, `P-358`; control 22 |
| An underdog with two or more current mechanisms separating, not merely covering | A favourite spread whose family set has no "underdog by 7+" branch | `P-371`; control 23 |
| An unquantified secondary scorer or ball-pressure guard producing a ceiling game | An Under built on the opponent's average scoring | `P-358` (San Antonio); controls 20, 21 |


### Pre-issue checklist additions (this sport)


- Attempts and binomial standard error printed beside every tournament shooting rate that carries direction (control 22).
- Margin families per control 23, with mass; the "underdog by 7+" family populated when the underdog has two or more current mechanisms.
- `P(R1 ∧ R2)` and the coupling sign for any handicap + total pair (control 24, `G-L10`).
- Numeric width and normalised edge on every total and spread (§16.8 item 3).
- Quantified exposure line for every top-three / 20-minute player on both sides — no bare names (control 20).




## 2026-09-12 algorithm corrections and retrospective integration


Control 24 is corrected: a close game can add late fouls but can also have slow pace; separation can arise from either excellent offence or suppressed opposition. Derive dependence from joint possessions, efficiency, rotation and foul states. No fixed cushion-plus-Under sign. In P-371 the frozen tournament sample was Belgium three games versus Germany four; actual attempt denominators were not captured. Withdraw the equal-75-attempt/1.7-SE and mostly-noise claim. Keep shooting reversals as observations and sensitivity hypotheses. Record both starting fives separately from the twelve-player eligible rosters and coaches. Germany won each quarter but did not lead throughout.


For every supplied row, use exact target probabilities from a coherent joint distribution; handle push/void/censoring explicitly, avoid overlapping adverse-state counts, and report JOINT_UNQUANTIFIED with bounds if the dependence is not specified. Separate issued-time participant capture, later recovered evidence, source accuracy by field, observed mechanism, and unverified causal interpretation. Keep one preferred O/U direction per distinct target and report the top-two denominator honestly. [Shared correction and methodology sources](audit_2026-09-12/rule_corrections.md). All current log observations remain learning-only and not performance-eligible.




## 2026-09-15(b) settlement learning — `P-373`–`P-423` import


Learning-only; disclosure/process changes only — no coefficient or ordinal bar (`L-087`). Evidence and tables: [`PREDICTION_LOG_COMBINED_3.md` §"2026-09-15(b)"](PREDICTION_LOG_COMBINED_3.md). Cross-sport rule: `RULES_GENERAL.md` §16.10 (`G-L12` margin centre/width; fixture identity; official-record derivative settlement).


**Cards:** P-378 (Philippines v Bahrain — Under 163.5 and Bahrain −9.5 lost; late-added Oftana scored 31), P-411 (Spain 81–58 Germany — Germany +6.5 LOST, Under 147.5 WIN, winner Spain correct).


### What went wrong, linked to earlier lessons
1. **P-411 discarded current evidence.** The same-competition, same-roster meeting ten days earlier (Spain 83–53) was set aside as an extreme-shooting outlier and the margin centred at Spain +5.2. Spain won by 23 with a Q4 of 20–7. "Spain pressure recreates the opener's separation" was the card's first kill path.
2. **P-378:** a late-added high-usage player without a minutes/usage mixture (reinforces control 21).
3. **`C-UNDERDOG-SEPARATION` direction challenged.** It assumed underdog states were under-weighted (P-358, P-359, P-371); P-411 is a favourite-separation miss. Generalised to `C-MARGIN-TAIL-MASS` (both tails) — `LEARNING_REGISTER.md` §"2026-09-15(b)".


### Structural control additions
25. **A same-competition, same-roster meeting is current evidence.** Decompose it (shooting luck v possessions, turnovers, rebounds) and give the separation family explicit mass; do not discard it as an outlier (`G-L7`, `G-L12`). Origin P-411.


## 2026-09-16 — external variant C′ reconciliation (`P-411`)


Learning-only; cross-sport rules in `RULES_GENERAL.md` §16.11.


**Control 25 worked example (adopted from C′; no new control).** Before shrinking a same-tournament blowout's margin, print a **repeatable-v-variance table**, and move the prior margin only by the variance share:
- **(a) repeatable:** turnover creation, rim and paint attempts, offensive rebounding, matchup size;
- **(b) variance:** 3P% and FT% gaps, opponent illness and absences.


P-411's rematch reproduced the separation (Spain +23 after +30).


**`G-L15`.** P-411's Under 147.5 was the preferred side of a forced pair and won. Across `P-345`–`P-423`, basketball forced-pair preferred sides went 3 of 6 — a coin flip, consistent with the §"2026-09-11" centre-error measurements.


**Disruption facts (§16.11(o)).** Record player ejections, injury exits and illness withdrawals with the quarter and the score at that time.


## 2026-09-17 settlement learning — `P-427` (BCL qualification) — **Rank #1 LOSS**


Learning-only (`L-087`). Cross-sport rule: `RULES_GENERAL.md` §16.12(a) (`G-L17`). Evidence: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17"](PREDICTION_LOG_COMBINED_4.md).


**What happened.** Kolossos +2.5 (0.61) and Under 162.5 (0.58) were the top two, declared "mildly positively coupled" with `P(R1 ∧ R2) ≈ 39%`. Kolossos led 70–66 after three quarters — the central thesis was sound — and then Körfez won the fourth quarter **25–9** with 12/24 from three. The single state broke the cushion **and** lifted the game to 170. Both rows lost; this was the only Hit@2 failure in a twelve-card batch. No overtime was involved: regulation alone cleared the total.


**What went right.** The winner label was correctly called a coin flip (52/48) rather than overstating Kolossos, and the `G-L12` separation audit did print a 39% chance of Körfez winning by more than 2.5.


### Structural control addition
26. **Shared late-game kill state for coupled top-two rows.** When a cushion and an Under (or any two rows resting on the same close, low-possession regime) occupy the top two, print `P(¬R1 ∧ ¬R2)` and name the state — typically a fourth-quarter shooting or turnover run that produces separation and points together — separating it from the intentional-foul and overtime tails, which are distinct mechanisms. Origin `P-427`; cross-sport form `G-L17`. Reinforces controls on late-game, closing-lineup and foul/bonus branches, which existed and were stated but not quantified as a joint failure.


## 2026-09-17(b) settlement learning — `P-451` (LNBP Jornada 20) — **the fail-close held, and the result lane is now solved**


Learning-only (`L-087`). Cross-sport rules: `RULES_GENERAL.md` §16.13. Evidence: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17(b)"](PREDICTION_LOG_COMBINED_4.md).


**What happened.** Dorados de Chihuahua v El Calor de Cancún, the second game of a two-night series at the Gimnasio Manuel Bernardo Aguirre. The card ran the §9.5 onboarding check, found no current LNBP regulation packet, set **`BK-P1 = FAIL`**, and issued **no rank, probability, winner or direction**. Nothing enters any W/L, Brier, Rank-#1 or winner count.


**Three things to record.**


1. **The block was correct and it was costless.** The card listed four shortcuts it refused — home record → Dorados, a two-point first game → El Calor +4.5, a 180-point first game → Over, season scoring averages → Under. The final was **Dorados 97–86** (total 183, margin 11): two of those shortcuts would have won and two would have lost. A fail-close under `BK-P1` is not a forecast forgone; it is a coin flip declined.
2. **The block held under maximum collision pressure**, which is the harder test. Same opponents, consecutive nights, same venue, and a search surface saturated with the previous night's 91–89 Jornada 19 result. The card explicitly refused to use that score and wrote the warning into its own record. This is `§16.10(i)` fixture identity working exactly as intended in the sparse-competition case it was written for.
3. **`BK-P1` remains `FAIL`.** A fresh search for a 2026 LNBP competition-regulation packet in this pass again returned nothing: period length, foul-out/bonus, challenge, overtime resolution, roster activation, import eligibility and abandonment treatment are still unclosed. The unresolved-fields list in §9.5 is unchanged and the competition stays not forecastable.


### Source addition to §9.5 — the LNBP result lane is a rendering problem, not an access problem


The 2026-09-04 note in §9.5 records `https://lnbp.mx/` as returning HTTP 403 to the scripted route. That is now **out of date and was the wrong diagnosis**. The current state, verified 2026-09-17:


- `https://lnbp.mx/<Team>/team_results.html` (e.g. `/Dorados/`) returns **HTTP 200** to `curl`, but the payload is a ~16 KB JavaScript shell containing **no scores** — the results are injected client-side from a Summit/True Wisdom front end. Every text-fetch and proxy route therefore reports "no result found", which is what produced the mini log's `RESULT_NOT_RELIABLY_RECOVERED`.
- **Rendered in a browser, the same URL returns the per-Jornada finals directly**, with a Jornada selector. Selecting *Jornada 20* on the Dorados page returned **Dorados 97 — El Calor 86** immediately and unambiguously, distinct from the Jornada 19 game.
- `https://www.lnbp.mx/scores.html` is the league-level equivalent and needs the same rendering plus a Jornada selection.


**Operational consequence.** For LNBP results, escalate straight to the rendering rung of the §"web access rendering ladder" — do not spend the text-fetch rungs. A JS-only field owner is **reachable**, so a missing LNBP final is a `RETRIEVAL_MISS`, not unavailability. This lane settles **finals**; it does not close `BK-P1`, which needs a regulation document, and a regulations search on the same domain still returns nothing.


**Unchanged:** never upgrade this lane into a league-wide structured-stat source, and never pool an LNBP rate with a generic FIBA population. Recorded in `SOURCES.md` and `DATA_SOURCE_REGISTER.md` §"2026-09-17(b)".


### Structural control addition


27. **A JavaScript-only field owner is a rendering escalation, not a dead route.** When the competition's own site returns HTTP 200 with a shell that carries none of the wanted fields, record the state as **`JS_ONLY — RENDER REQUIRED`** rather than `NOT_AVAILABLE`, name the rung that will recover it, and treat a subsequent miss as a `RETRIEVAL_MISS` (§16.8 field 7). Distinguish this from a genuine 403/404, from a paywall and from a field the owner simply does not publish — the AFC corner field in soccer control 38 is the last kind, and no amount of rendering will produce it. Origin `P-451`; the same diagnosis applies to any league front end built on a client-side stats widget.


### `G-L24` in basketball (added 2026-09-17(b))


Basketball margins are near-continuous and the cushion band is **line-specific, not sport-specific** — there is no single `b_L` for the code. Derive it per competition and per line from that competition's own completed-season margin record; `BASE_RATES_REGISTER.md` §1 records basketball as `NOT_YET_DERIVED`. Two sport-specific cautions: **late intentional fouling** thickens the 3–6 point band in ways that differ by competition rules (control 26 already separates this from the shooting-run tail), and **overtime** removes the small-margin band entirely by construction, so derive over regulation-decided games and carry the OT branch separately (`G-L19`). `P-427` is the standing reminder that a cushion and an Under can die to one late state.


### `G-L21`–`G-L23` in basketball (added 2026-09-17(b))


**`G-L21`:** control 26 already requires `P(¬R1 ∧ ¬R2)` for a coupled cushion-and-Under top two, from `P-427`. Extend it past the top two: a 'slow, half-court, favourite controls it' thesis routinely carries a cushion, an Under **and** a team total, and one fourth-quarter shooting run kills all three together — `P-427`'s Q4 was 25–9. Print `P(all fail)` with Fréchet bounds, and check the **sign**: a low-possession game supports an Under while working *against* a favourite covering a spread, so those two are negatively coupled on pace even though both feel like control.


**`G-L22`:** basketball's forced pairs differ from baseball's in one way that matters. Spreads and totals are usually quoted on **half-points**, so the push branch is genuinely near zero and the two sides really do sum to ~1 — unlike an MLB integer total, where an inflated push is the standing defect. The counting rule still applies (one decision, not two rows), but the push-mass caution does **not** transfer; where a whole-number line *is* supplied, derive the push from the competition's own margin record rather than importing a figure from another sport.


**`G-L23`:** the process record is the **quarter-by-quarter score**, shooting splits and turnover counts; the disruption facts are **ejections, disqualifications and injury exits with the clock and score**. `P-427` is the reference: a 70–66 lead after three quarters becoming a 12-point loss is a fourth-quarter process fact, and a card amended from the final margin alone would have learned the wrong thing.


## Current model implementation — 2026-09-17


Use METHOD v4.2's six-field object and SCORING_AND_VALIDATION for exact outcome/push scoring, event-level comparison, descriptive recency and declared hierarchical uncertainty. MODEL_IMPLEMENTATION_RECIPES supplies this sport's retained model scope and endpoint design. Forecast probabilities come from the joint model; pooled base rates are uncertain context, not universal limits. Numeric row caps disconnected from that model, absolute-distance probability ordering and retrospective tail reweighting are withdrawn. No fitted coefficient or predictive improvement is claimed. New cards freeze the method/control hash; existing cards keep their issued versions.


## 2026-09-19 — recency/rebound evidence, debutant gate and the top-O/U review


Cross-sport: [`RECENCY_AND_REBOUND.md`](RECENCY_AND_REBOUND.md) control `R-1`; source controls `S-1` (social identity) and `S-2` (press conferences) in `SOURCES.md` §"2026-09-19"; enhanced-failure trigger in `METHOD.md` §7.


**`R-1` applies qualitatively; basketball magnitudes are `NOT_YET_DERIVED`.** Basketball's higher-count scoring target may well show different game-to-game autocorrelation than baseball's — derive it before any recent-form weighting, do not assume the MLB result transfers.


**Press-conference tempo claims (`S-2`).** A coach stating an intention to raise pace or tighten defence is **not** a pace or efficiency adjustment. It may motivate a named branch carrying its own mass, or widen the distribution; it may not move a possessions or efficiency centre. Stated intent and realised tempo are weakly related, and converting the former into the latter is the unsupported signed adjustment `G-L2` prohibits.


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — market-independent totals/line addendum


**Source priority:** NBA/FIBA/NBL/competition official stats, injury reports, rosters and team releases. Fantasy/DFS projections, ownership and optimizer outputs are prohibited.


Estimate possessions/pace and offensive/defensive efficiency independently of the line, with rotation/availability, rest/travel, venue and role uncertainty. Produce a joint score/margin distribution; combined total, team totals, spread and winner are post-forecast queries. Avoid additive narrative point adjustments that were not estimated in chronological data.




<!-- ALL-SPORTS-AUDIT-LIVE-RULE-CLEANUP-2026-09-21-CR3 -->
## 2026-09-21 — all-sports audit live-rule cleanup — CR-2026.09.21-3


Current prospective override. Retain the possession/opportunity model, minutes/usage mixtures, shooting shrinkage/uncertainty, foul/garbage-time/overtime tails and spread-total coupling. Withdraw pseudo-tail order-statistic constructions, path-count ranking shortcuts, universal probability-band top-slot rules, normalized-distance ordering, and one-result response rules. Build one coherent basketball joint outcome distribution before querying targets; without a fitted/calibrated distribution, do not invent precise probabilities.