# Baseball analysis rules


> **2026-09-12 operational correction:** The dated section at the end of this file and RULES_GENERAL section 16.9 control over conflicting older probability, coupling and source claims.


> **`METHOD.md` is now the primary mandatory read (v4.0 comprehensive overhaul, 2026-09-06).** This file remains the full sport-specific reference: its `SFA-<SPORT>` algorithm and competition-rules section (`§9`/`§10`/`§11`) are consulted in full when forecasting this sport; `METHOD.md` states the cross-sport process once.


<!-- THREE-SOURCE-TIME-GATE-2026-09-19-CR4 -->
> **Current cross-sport authority — MDS-2026.09.19-v4.3 / CR-2026.09.21-3:** this sport module inherits the reconciled all-sports controls, including three independent reliable event lineages, timezone-aware venue-local → `Australia/Melbourne` verification, terminal-state confirmation, market/fantasy source quarantine, and the current distribution-first ranking rules. Historical issued cards retain their own revision.


Status: **ACTIVE**
Effective: **2026-09-06 (v4.0 comprehensive overhaul — see METHOD.md and archive/audit_documents_implemented_2026-09-25/FRAMEWORK_AND_GAME_LOG_OVERHAUL_REVIEW_2026-09-06.md)**
Method version: **MDS-2026.09.06-v4.0**
Applies with RULES_GENERAL.md, MODEL_AND_DATA_SPEC.md, ALGORITHM_PORTFOLIO_AND_EVALUATION.md, and NUMERICAL_TRAINING_SPEC.md.
Executable algorithm: **SFA-BASEBALL (§8) — instantiates GFA-2 in RULES_GENERAL.md §11**
Numerical training specification: **NTS-2026.09.02-v0.3 — design only; no baseball model is fit**
Sport and competition rules reference: **§9 (added 2026-09-04)** — playing laws plus per-league rules for every baseball competition in the prediction logs (MLB, NPB, KBO, LMB, MiLB/Triple-A, WBSC/international). Reference material for identity, state classification and settlement; it does not change `SFA-BASEBALL`.


## 1. Identity and contract


Resolve league and level: MLB, NPB, KBO, LMB, WBSC, minor league, college, or another competition. Record season/rules era, venue, home batting entitlement, designated-hitter rule, scheduled innings, doubleheader format, extra-innings rule, probable/confirmed starters, and operator action/listed-pitcher terms.


For MLB, use the current official rule and technology environment. The 2026 ABS challenge system weakens transfer from old home-plate zone tendencies; do not use an umpire effect without current-system evidence.


## 2. High-value inputs


### Participants and exposure


- Complete the final starter-identity handshake for both sides against the official event page or official team/league release. Store event ID, team, role, participant ID/name and `CONFIRMED_OFFICIAL`/`PROBABLE_OFFICIAL`/unresolved status; never translate a same-day secondary preview into a confirmed starter.
- Confirm both posted batting orders, bench, catcher, defence, starters, and material absences. If official starters or orders are not released, model explicit participant mixtures and apply the general evidence cap rather than choosing one preview lineup.
- Estimate plate appearances by lineup slot.
- For each starter, model batters faced, pitches, innings, and hook point separately from runs allowed.
- For every relevant reliever, estimate availability probability and likely role. Build opener → bulk → bridge → leverage → low-leverage alternatives; workload informs availability, not performance.


### Starter and lineup process


Use the current arsenal against the current lineup:


- pitch mix, velocity, movement and location;
- K-BB%, whiff/chase, ground/fly-ball shape, HR, barrel/hard-hit and expected contact measures where valid;
- handedness and platoon shape;
- catcher, defence, park, and opponent quality;
- injury/return, pitch cap, rest, and recent mechanics.


ERA and WHIP are context, not a complete distribution. FIP/xFIP/xERA or league equivalents are supporting estimates with their definitions and limitations. Direct starter history receives weight only when current-lineup overlap and arsenal/role continuity are meaningful; never promote one prior start as ownership.


### Environment and context


Record park factors with year/rolling window, dimensions, roof, venue-local game-window weather, altitude, rest/travel, series state, and home last-bat. Hot air, humidity, rain, or wind has no automatic total direction. Officials, motivation, and press comments are conditional only.


## 3. Model


Exposure units are plate appearances, pitcher batters faced, pitches, innings, and live base-out state. Use a joint team-run distribution with overdispersion and explicit sequencing/HR tails rather than a naive homogeneous Poisson.


Build:


1. starter run-rate and exit distributions;
2. the named relief-chain distribution;
3. lineup PA and matchup rates;
4. park/weather/defence adjustments;
5. home-ninth, extra-innings, and score-state branches.


Derive winner, run line, team total, game total, and player contracts from that same distribution.


For numerical training, compare empirical and Poisson/negative-binomial team-run baselines with a plate-appearance/base-out A2 simulator. The structural candidate samples starter batters faced/hook state, the named relief chain, PA outcomes, base/out transitions, sequencing and HR clusters, home-ninth entitlement and extra innings. A bivariate/direct score model or boosted distribution is a challenger only after covariance, overdispersion, support, era and tail checks. All totals, run lines and winners integrate the same joint run distribution; line-specific binary classifiers cannot become the primary engine. All candidates remain unfit and unvalidated.


## 4. Structural controls


1. **Short start is exposure, not an automatic Over.** More bullpen innings raise uncertainty; direction depends on the likely arms and lineup.
2. **Recent run suppression does not erase the HR/contact tail.** Record central and short-start/two-homer branches.
3. **Pitch limit and innings are separate.** Efficiency, baserunners, plate-appearance length, and quick outs determine how far a pitch cap travels.
4. **Cushion decomposition.** For every +1.5 line record win, exactly-one-run loss, and 2+-run loss branches.
5. **Low total does not imply close margin.** One dominant starter and clustered damage can produce a multi-run Under.
6. **Bullpen freshness is not quality.** Name the likely chain and manager alternatives.
7. **Post-trade or role-change regime.** Rebuild catcher, arsenal, velocity/location, mechanics, role, and current-lineup fit.
8. **Trend mechanism.** Classify recent totals by starters, lineups, contact/HR, errors, relief chain, park and weather before using an Under/Over run.
9. **Gapped/overlapping lines.** Map every interval; opposite-team positive run lines can both win, and alternate totals can overlap.
10. **Home batting exposure is state-dependent.** Derive ninth-inning entitlement from the score distribution; do not apply a fixed innings fraction.
11. **Small-sample starters require a mixture.** A debut, return, young starter, opener, or one-start sample is pooled toward the league/role prior with explicit good-start, ordinary, early-hook and contact/HR tails. One good outing cannot collapse that uncertainty.
12. **Starter identity precedes starter quality.** No ERA, arsenal, platoon or hook analysis is decision-driving until the starter is linked to the exact official event/team role at the final volatile refresh.
13. **Season prior versus current starter regime.** When recent arsenal/velocity/location, role, opponent quality or contact indicators conflict with season ERA/reputation, retain a shrunk season/league prior and an explicit current-regime branch. State why each branch is weighted; do not let either a famous season line or a short hot/cold run win silently.
14. **Defence and unearned-run tails stay in the score tree.** Team fielding quality may adjust the baseline, but one game's error cluster is a realised tail unless a current personnel/positioning mechanism made it forecastable. Do not backfit a generic error penalty from a single final.
15. **Joint hook-tail reconciliation.** When either starter is debut/small-sample/returning or both starters have wide exit distributions, construct the joint early-hook branch: batters faced, inherited runners, first available relief arms, bullpen innings, contact/HR cluster and home-ninth exposure. Before an Under can outrank its Over, state why that joint upper tail remains subordinate; otherwise lower evidence or change the order.
16. **Strong opponent starter does not erase debut variance.** A favourable opposing-starter matchup may shift the centre, but it cannot collapse a rookie/first-starter's ordinary and early-hook branches. Both teams' exposure mixtures survive into the total and margin distribution.
17. **Low-total separation remains explicit.** For each underdog +1.5 or favourite -1.5 row in a low-total game, retain shutout and 2–0/3–0/4–1-style one-sided branches. Low expected runs do not mechanically create a close margin.
18. **Weather termination has an event order.** Under the competition's official-game and operator-action rules, separate runs-before-stop, stop-before-runs, restart/relief-transition and void/no-action branches. Rain or a shortened final is not mechanically an Under once a clustered inning has already crossed the line.
19. **Stable starter centres do not remove cluster risk.** Even when both starters have established central projections, retain walks/errors, sequencing, multi-run homer, inherited-runner and first-relief-transition branches. The upper tail is a joint inning/relief state, not only an “early hook” label.
20. **Bullpen availability is score-state specific.** Map starter/opener → bulk/middle → tied/leading leverage → one-run trailing → multi-run trailing arms, with inherited runners and prior workload. A rested closer does not protect a side or +1.5 line if the likely game state never triggers his entry.
21. **Favourite separation and run clusters are linked.** When the favourite's offensive/HR ceiling and the opponent's starter-to-middle-relief transition drive both the Over and a multi-run win, stress those outcomes jointly. Do not describe the favourite run line and upper total as unrelated remote tails while ranking the underdog cushion first.
22. **Extra innings are a different rate environment, not more of the same innings.** Under a rule that seeds each extra half-inning with a runner already in scoring position, assign the tie-after-nine branch its own materially higher per-inning run distribution (RULES_GENERAL.md §11.3, G22; branch `BB-B7`). A correct nine-inning read can still lose a total or a run line once the game reaches that state; quantify the probability of reaching a tie after nine separately from the extras scoring rate itself.
23. **A prior game in the same series is context, not a cause.** A team's result in the immediately preceding game of the same series requires a named, currently active mechanism — the specific starter/bullpen usage it created, a lineup or rotation change it triggered, or comparable evidence — before it may support either a "bounce back"/"response" lean or a continuation lean for today's game, per RULES_GENERAL.md §11.3E (G17.1). Record the series score and the disclosed bullpen/lineup consequence of the prior game(s) under the series-state block (RULES_GENERAL.md §5); a prior blowout or a prior close loss is not itself evidence for today's direction.


## 5. Live state


Store inning/half, score, outs, base state, current pitcher/pitch count, bullpen behind him, lineup slot due, challenges/reviews, weather/roof, and home batting entitlement. Recalculate remaining PA and named pitcher/reliever branches.


## 6. Sources and settlement


- MLB official StatsAPI and MLB match centres control schedule, lineups, live state, box score, transactions, and final.
- [MLB Statcast glossary](https://www.mlb.com/glossary/statcast) controls Statcast definitions; Baseball Savant supplies park and batted-ball data.
- NPB.jp/BIS, KBO, CPBL official/advanced game pages, LMB.com.mx, WBSC, and official league/team sources control their competitions. Each league remains a separate source/definition population.
- Government weather services and official roof reports control game-window conditions.


Settle from the official final and named statistic provider. Preserve extra-innings and listed-player rules. Recheck documented official stat corrections for props.


## 7. Upcoming-game research sequence


1. Freeze league/rules era, scheduled innings, home-last-bat/extra-inning terms, listed-pitcher/action rules and full candidate slate.
2. Retrieve official probable/confirmed starters, posted orders, catcher/defence, transactions/injuries, roof and park-local weather; refresh lineups, starters, roof and weather before issue.
3. Model lineup PA, starter batters faced/pitch/inning/hook distribution, current arsenal versus lineup, the named bullpen chain, base-out transitions, sequencing/HR clusters, park/defence and home-ninth/extras. If either starter is debut/small-sample or both exit distributions are wide, stress their joint early-hook/relief/cluster branch before ordering the total.
4. Maintain MLB, NPB and KBO as separate priors/rules/data cards; MLB Statcast-era measurements cannot be silently transferred to another league or earlier tracking regime.
5. Derive winner, total, team totals and run lines from the joint run object. Pitcher/batter props use action probability and their own PA/batters-faced/event-rate targets.


Official league/team sources control lineups, starters, rules and finals. Statcast/Savant controls only its defined MLB tracking metrics; projections are external challengers, not labels or ground truth.


## 8. SFA-BASEBALL — sport forecast algorithm


Algorithm ID: `SFA-BASEBALL`. Effective **2026-09-02**. Instantiates `GFA-2` (RULES_GENERAL.md §11) with baseball content. It is a process composition of promoted controls and §4 above; it introduces no fitted weight, scenario weight or published probability. MLB, NPB, KBO, CPBL, LMB, MiLB and other leagues remain separate populations at every step.


### 8.1 Blocking preconditions


Resolve these before any rate work. Each maps to a `GFA-2` gate.


| Precondition | Requirement | Failure output |
|---|---|---|
| `BB-P1` starter identity | Both starters carry `(official_event_id, team, SP, participant)` with `CONFIRMED_OFFICIAL` or `PROBABLE_OFFICIAL` from the field owner, re-handshaken at G31 | No ERA, arsenal, platoon or hook analysis is decision-driving; the affected rows cap at `FORCED RANK` / `MEDIUM-LOW` and the starter is carried as a mixture |
| `BB-P2` batting orders | Both posted orders, catcher, defensive alignment and material absences | Model lineup mixtures; slot-PA, platoon-cluster and player rows cap under RULES_GENERAL.md §11.5 |
| `BB-P3` league and rules era | League, scheduled innings, extra-innings rule, designated hitter rule, listed-pitcher and action terms, roof status | `GATE-TARGET` failure; do not proceed |
| `BB-P4` termination terms | Official-game rule and the operator's suspension/shortening/action rule where supplied | Label `UNKNOWN_DEFINITION`; keep the termination branch explicit |
| `BB-P5` home-last-bat | Which side bats last, and whether the contract endpoint includes extras | Required before any total or run-line is located |


### 8.2 Exposure chain


Run in order. Each step consumes the previous step's output; none may be skipped by asserting a team-level number.


| Step | Output |
|---|---|
| `BB-S1` | Lineup plate-appearance budget by slot for the scheduled innings, both sides |
| `BB-S2` | Starter batters-faced, pitch and inning distribution with an explicit hook point — modelled separately from runs allowed |
| `BB-S3` | Current arsenal against the current lineup: pitch mix, velocity/location, K-BB%, whiff/chase, batted-ball shape, barrel/hard-hit, home-run shape, handedness and platoon clusters |
| `BB-S4` | Named relief chain as a score-state ladder: opener, bulk, bridge, tied/leading leverage, one-run trailing, multi-run trailing, low leverage — each with availability probability, inherited-runner exposure and prior workload |
| `BB-S5` | Park factor with window, dimensions, roof, venue-local game-window weather, altitude, defence and catcher effects |
| `BB-S6` | Base-out transitions, sequencing and home-run cluster structure |
| `BB-S7` | Home-ninth entitlement derived from the score distribution, plus the extra-innings branch under the exact rule |
| `BB-S8` | One joint team-run object with overdispersion, from which winner, run line, team totals, game total and player rows are queried |


Workload informs availability, never performance. A rested arm that the likely score state never summons has no protective value.


### 8.3 Mandatory branch set


Every baseball card represents all nine states, with each supplied line located against them.


| Branch | Content |
|---|---|
| `BB-B1` | Both starters at their central length and run rate |
| `BB-B2` | Joint early-hook state: either or both starters exit early, with the first available arms and inherited runners named |
| `BB-B3` | Multi-run home-run or sequencing cluster inside one inning |
| `BB-B4` | One-sided separation with the opponent floor at nought to two runs — the low-total, wide-margin family |
| `BB-B5` | Relief-transition inning where the score state changes which arms appear |
| `BB-B6` | Home-ninth not batted because the home side leads, capping the total |
| `BB-B7` | Extra innings under the exact competition rule, modelled with that rule's own scoring-rate environment (for example a runner placed at second to open each half-inning materially raises the per-inning scoring rate above a regulation inning; do not extrapolate the nine-inning rate into extras under such a rule) |
| `BB-B8` | Termination order: runs before stop, stop before runs, restart and relief transition, official-game and no-action states |
| `BB-B9` | Late separation: the game is inside one run entering the last third and the margin expands by two or more runs after both starters are gone, through the relief chain, a home-run cluster or a bullpen collapse on one side only |


### 8.4 Contract derivation map


| Contract | Queried from | Extra condition the mechanism must predict |
|---|---|---|
| Game total | Joint run object, both teams | The component budget in RULES_GENERAL.md §11.4 G20, solved at the opponent floor, centre and ordinary high |
| Team total | Team marginal of the same object | Own-lineup exposure against the exact opposing starter and the arms that actually reach those innings |
| Run line and cushion | Margin marginal | Win, exactly-one-run loss and two-or-more-run loss branches stated separately |
| Winner | Margin sign, including home-ninth and extras | Not inferable from the total |
| Pitcher props | Batters faced and pitch budget from `BB-S2` | Hook risk and lineup turn count, not season rate |
| Batter props | Slot plate appearances from `BB-S1` | Opposing starter and the relievers that reach that slot |


**Worked run-line slate — you rank every row, you do not pick one.** A book that lists `Team A +1.5 / Team A ML` and `Team B −1.5 / Team B ML` has supplied **four** contract rows (plus the total pair). The question is never "which do I choose" — it is "rank all four by marginal win likelihood and robustness" (RULES_GENERAL.md §6, and §3: never replace the supplied slate with an easier market). The prices attached (e.g. `+1.5 @ 1.67`, `ML @ 2.50` for A; `−1.5 @ 2.10`, `ML @ 1.67` for B) are **recorded as metadata with a capture time and play no part in the forecast or the rank** — `SPORTS_ONLY / MARKET_BLIND` (§4 bookmaker-independence hard gate).


The four rows collapse to **two independent quantities** from the joint run object: `p_win = P(Team B wins)` and `p_one = P(the margin is exactly 1)`. Then, deriving from the same distribution (coherence is mandatory — G25.1):


| Row | Wins when | Probability |
|---|---|---|
| `Team B ML` | B wins by 1+ | `p_win` |
| `Team B −1.5` | B wins by 2+ | `p_win − P(B wins by exactly 1)` |
| `Team A +1.5` | A wins, or loses by exactly 1 | `1 − (p_win − P(B wins by exactly 1))` |
| `Team A ML` | A wins by 1+ | `1 − p_win` |


So `P(Team A +1.5) ≥ P(Team A ML)` and `P(Team B −1.5) ≤ P(Team B ML)` **always** — a rank order that violates this is an incoherence defect. The ordering then follows the game shape you forecast: a likely multi-run favourite game ranks `B ML ≈ B −1.5` above `A +1.5 > A ML`; a coin-flip game likely decided by one run ranks `A +1.5` and `B ML` up and both `−1.5 / underdog-ML` rows down (§4 control 4 cushion decomposition; §8.6 override 3). The **potential winner** is a separate single call with its endpoint stated (regulation vs eventual winner incl. extra innings; no automatic runner in the MLB postseason — §9.2).


### 8.5 Kill-path library


Each row names a mechanism, not an outcome, and the contracts it defeats. Use it to populate `kill` in the row robustness record.


| Kill path | Defeats | Evidence origin |
|---|---|---|
| Multi-run home-run cluster in a single inning | Under; and the underdog cushion when the cluster lands for the favourite | L-006, C-PL7-BB-HOOK-TAIL, C-PL9-BB-SCORESTATE-RELIEF |
| Early hook plus first relief transition with inherited runners | Under; and the side resting on starter quality | T-004, T-005, C-PL4-BB-SMALL-SAMPLE-STARTER |
| Opponent scoring floor near nought to one run in a low-total game | The positive run-line cushion, while the Under still wins | §4 control 17, C-PL9-BB-SCORESTATE-RELIEF |
| The closer never enters because his club trails | Any row justified by generic bullpen freshness | C-PL9-BB-SCORESTATE-RELIEF |
| Rain or curfew arriving after runs have already scored | The assumption that shortening implies Under | C-PL8-BB-TERMINATION-ORDER, §4 control 18 |
| Home side leads and does not bat in the ninth | Over, by removing scheduled exposure | §4 control 10 |
| A debut or small-sample starter delivering his ordinary good outing | An Over resting on projected rookie collapse | §4 control 11, C-PL4-BB-SMALL-SAMPLE-STARTER |
| Joint favourite separation and upper total, positively dependent | The framing that an underdog cushion and the Over are unrelated remote tails | §4 control 21, C-PL7-BB-HOOK-TAIL |
| Post-starter separation in a game the starters kept close | Any underdog cushion whose support is a close-game or head-to-head-margin narrative rather than a budgeted relief-inning margin | `BB-B9`, C-PL11-BB-SEPARATION-BUDGET (P-247) |
| The underdog's own offence supplies the Over | An Under ranked from the favourite's cooled scoring, and any pairing of an underdog cushion with that Under | C-PL11-BB-UNDERDOG-TAIL (P-248) |
| A hitter-friendly park failing to manufacture runs that neither lineup's exposure supports | An Over ranked from venue reputation rather than a two-team component budget | C-PL11-BB-VENUE-RESTRAINT (P-244) |
| Walk-off in a tight low-total state | A road side in a one-run corridor | §4 control 10; local lesson `M4-L10` in PREDICTION_MINI_LOG_4.md §E |


### 8.6 Sport ordering overrides


These refine `GFA-2` G24 within baseball; they never reverse a `GFA-2` gate.


1. A short start raises relief exposure and therefore uncertainty. It is not directional, so it may not move a total's `corridor` classification by itself.
2. Before an Under outranks its Over, state why the joint `BB-B2`/`BB-B3` upper tail is subordinate. If that cannot be stated, lower evidence or change the order.
3. Before a positive run line outranks the opposing side, state which `BB-B4` separation scores are excluded and why. A low total is not evidence for a close margin.
4. Recent earned-run averages, Under runs and cover counts are `E — diagnostic only`. They may not supply a decisive term in the G23.1 marginal-likelihood comparison.
5. When both starters are established but the lineups carry power, `BB-B3` still applies. A stable centre does not remove cluster risk.
6. A run-line or cushion row is budgeted across the starter innings and the post-hook relief innings separately under G20.1, then against the home-ninth entitlement and the extras branch. State which relief innings can produce a two-or-more-run swing and why the cushion survives them. `BB-B9` must be represented before any cushion is ranked first.
7. A park or altitude factor scales a component budget that both lineups' exposure already supports. It may never supply runs that neither `BB-S1`–`BB-S4` chain produces, and venue reputation is `E — diagnostic only`.
8. A weak, rehabilitating, returning or small-sample starter attaches to the **opponent's** scoring branch under G14.1. It does not widen both teams' run distributions, and a stale season line on one side does not outrank the opposing starter's current-regime run prevention.
9. When an underdog run-line cushion is ranked first, the total is re-solved conditional on that state under G25.1: the branches that keep the underdog inside the line are branches in which the underdog scores, so the underdog's own upper tail enters the total before an Under may be ranked above the Over.


### 8.7 Pre-issue checklist


1. `BB-P1`–`BB-P5` status printed, with release status per starter.
2. Slot plate-appearance budget and both hook distributions stated.
3. Score-state relief ladder named, arm by arm, with inherited-runner exposure.
4. All nine `BB-B*` branches represented; component budget solved at the supplied total.
5. Kill-path rows selected from §8.5 and reconciled against the issued order.
6. Home-ninth and extras treatment stated for every total and margin row.
7. Termination branch stated whenever weather or curfew is live.
8. Lineups, starters, roof and weather refreshed at G31 before the view is appended.
9. Recency block complete per §8.8: L5/L10/L15/L20 for both sides and for head-to-head, continuity count stated, trend verdict per metric, unique-event de-duplication done.
10. Environment block complete per §8.9: Field-relative wind bearing, roof state and umpire crew pulled from the official game feed.
11. `REFERENCE_BASE_RATE`, exact threshold, population and denominator recorded for every supplied row per §8.10 as a descriptive diagnostic only; no reference-band, trend or slot-frequency adjustment may move an ordinal (G23.1).
12. Extra-condition support audit (G24) recorded for every handicap, team-total and cushion row; no retrospective contract-family penalty is applied.
13. Separation budget (G20.1) solved for every margin, handicap and cushion row across the starter innings and the post-hook relief innings separately, then the home-ninth entitlement and the extra-innings branch.
14. Rank-1 implied-target interval (G25.1) stated in the unit of every other supplied line, each remaining row classified `COHERENT`/`PARTIAL_OVERLAP`/`DISJOINT`, and every aggregate budget re-solved conditional on the Rank-1 state.
15. Winner-and-cushion reconciliation (G30.1) whenever Rank #1 is an underdog cushion, with the outright-win and narrow-loss branch ordering stated. Example separation kill path for this sport: a post-starter multi-run relief inning.
16. Deficit attribution (G14.1) recorded for every weak, absent, returning or small-sample participant: which side's distribution moved and through which exposure step.
17. Streak persistence-versus-reversion audit (G17.1) recorded for every hot/cold offensive or pitching run and for any prior-game/series "response" lean; extra-innings branch (`BB-B7`) modelled at its own rule-defined scoring rate, not the nine-inning rate, whenever an automatic-runner or similar rule applies.


### 8.8 Recency, head-to-head and trend windows


Implements `GFA-2` step G13.1 (RULES_GENERAL.md §11.3B) and runs at that point in the algorithm, not at the end. Retrieval of L5/L10/L15/L20 for both sides and for the head-to-head series is mandatory; a window that does not exist is recorded with its true count and a missingness code.


Populate one windowed table per side with these metrics, and one head-to-head table:


| Window metric | Content |
|---|---|
| Team run production | Runs scored and allowed per game, split against right- and left-handed starters |
| Team contact quality | Team hard-hit, barrel and home-run rate, and strikeout and walk rate, opponent-adjusted |
| Each named starter | That starter's own last 5/10/15/20 starts: innings, batters faced, pitches, hook point, home runs allowed, K-BB% |
| Bullpen load | Innings and appearances for each likely relief arm over the last 5 and 10 days, with back-to-back flags |
| Target-relevant output | How often the team total, game total and run line at this line would have settled in each window |


**Head-to-head continuity.** Continuity for baseball means the same starters, the same park and the same season roster. Two teams meeting for the fourth time in a series with different starters each day are four different matchups, and the head-to-head window is close to worthless unless the pitching matchup repeats.


**Descriptive recency windows (G13.1; revised 2026-09-17).** Retrieve L5/L10/L15/L20 and continuity-qualified H2H with unique-event counts. These windows overlap. Monotonicity and dispersion among their averages are not a statistical trend/noise test. Report direction descriptively; estimate recency decay and opponent/regime effects using time-ordered validation. See SCORING_AND_VALIDATION section 5.


**De-duplication.** The windows overlap by construction and share matches with the head-to-head and venue series. Shrink from unique underlying events under G9; never treat L5, L10, L15 and L20 as four confirmations.


### 8.9 Environment and conditions


Implements `GFA-2` step G15.1 (RULES_GENERAL.md §11.3C). Venue classification for this sport is normally **OUTDOOR unless the venue has a roof**.


| Field | Use in this sport |
|---|---|
| Field-relative wind | `statsapi.mlb.com` `v1.1/game/{gamePk}/feed/live` exposes `gameData.weather.wind` as a bearing relative to the field, for example "10 mph, Out To RF". Prefer it over any city forecast |
| Roof state | `gameData.venue.fieldInfo.roofType`, refreshed at G31 because roofs close late |
| Temperature and humidity | Ball carry; combine with park dimensions before any home-run branch |
| Hourly precipitation | Feeds the `BB-B8` termination branch and the official-game rule, never an automatic Under |


Failure to obtain the match-window forecast for an outdoor or open-roof event yields `WEATHER_NOT_AVAILABLE`, widened total and margin distributions, and a `LEAN` cap on every weather-dependent row. No factor above carries an automatic total direction.


### 8.10 Base-rate anchors and derived stat lanes


**Anchoring (G12.1).** Anchor totals on the park-and-era run environment at that line, and run lines on the league frequency of one-run and two-or-more-run margins. A +1.5 run line and a game total are different propositions and never start level.


StatMuse is an accepted research accelerator for this sport under DATA_SOURCE_REGISTER.md §18, using the verified query patterns recorded there. Every returned row is date-checked and reconciled against the official league source before it is decision-driving, and StatMuse never controls participants, availability, rules, state or settlement.


**Derived and low-salience fields that are available and routinely skipped:**


| Field | Note |
|---|---|
| Umpire crew | `liveData.boxscore.officials`; the plate umpire is a strike-zone and pace factor, conditional and only with current data |
| Park factors with window | Recorded with the year or rolling window, never as a bare label |
| Catcher framing and defensive alignment | Affects the same starter differently by battery |
| Home-last-bat entitlement | Derived from the score distribution at `BB-S7`, not a fixed innings fraction |


## 9. Sport and competition rules reference


Added 2026-09-04; last reviewed 2026-09-04. This section is a standing reference for the playing laws of baseball and the competition-specific rules of every baseball league that appears in the prediction logs. It supports `BB-P3`/`BB-P4` (league and rules era, termination terms) and §6 settlement; it introduces no rate, weight or ordering rule. Where a 2026 rule is cited, it is the rule in force for the 2026 seasons covered by the current log. Verify the rules era for any event outside 2026 — leagues change tie, roster, DH and postseason rules frequently.


**Maintenance (RULES_GENERAL.md §3, `G2`).** Before the first card of a new season, spring training / pre-season, or postseason for any league here — MLB, NPB, KBO, LMB, MiLB and the international events all start at different times of year — re-verify the tie/extra-innings rule, the ball-strike technology in force, the import and active-roster rules, the DH rule, the pitch-clock/pace values and the postseason bracket against the official league source, and update this section **before** issuing the card. The first time a new baseball competition is forecast (a winter league, a new international event, another domestic league), document its full rules here first.


### 9.1 Universal playing rules (all baseball)


**Objective and structure.** Two teams of nine alternate on offence (batting) and defence (fielding). A game is scheduled for **nine innings**; each inning has a top half (visiting team bats) and a bottom half (home team bats). A half-inning ends when the fielding team records **three outs**. The team with more **runs** after the last scheduled out wins.


**Scoring a run.** A run scores when a baserunner legally touches first, second, third and home plate in order before the third out of the inning. A run does **not** count if the third out is a force out, a batter-runner put out before reaching first, or a preceding runner passing another — this is the "time play" rule and matters for totals settlement on the final play.


**Home-team last bat.** If the home team leads after the top of the ninth, the bottom of the ninth is not played. If the home team scores the go-ahead run in the bottom of the ninth (or any later inning), the game ends immediately ("walk-off") — the winning margin is capped at the runs needed plus, on a home run, the batter and any runners. This is why a home favourite can never "cover" a large run line in a game it walks off by one.


**The count.** Each plate appearance is a contest of **balls** (pitches outside the strike zone not swung at) and **strikes** (pitches in the zone, swung on and missed, or fouled with fewer than two strikes). Four balls = a **walk** (batter to first). Three strikes = a **strikeout**. A foul ball with two strikes is not a third strike (except on a bunt).


**Reaching base:** hit (single/double/triple/home run), walk, hit-by-pitch, fielder's choice, error, dropped third strike, catcher's interference.


**Being put out:** strikeout, ground/fly/line out caught, force out, tag out, appeal (missed base, left early on a fly), interference, running out of the baseline.


**Batting order and substitution.** Nine hitters bat in a fixed rotation. A substitute takes the replaced player's lineup slot. **A player removed from the game cannot re-enter** (no re-entry in professional baseball). Pinch hitters and pinch runners are common; a pitching change mid-inning is unlimited subject to the three-batter minimum (below, where adopted).


**Designated hitter (DH).** Where adopted, a tenth player bats in place of the pitcher every time the pitcher's slot comes up, without playing the field. The "Ohtani rule" (MLB, and most DH leagues) lets a team keep the DH when its starting pitcher is also the DH and is later removed as pitcher.


**Pitching.** The starter must face at least one batter (or, where adopted, three — see below). Relievers enter freely between batters. A **balk** (illegal pitching motion with runners on) advances all runners one base.


**Weather, official games and suspensions.** A game called by weather is an **official game** once the trailing team has had a chance to complete five innings (4½ if the home team leads) — earlier than that it is a "no game" and (in most competitions) replayed in full. Modern MLB/MiLB rules make most weather-shortened or interrupted games **suspended** and resumed from the point of stoppage rather than reverted; older eras and many other leagues revert to the last completed inning. The termination-order branch (`BB-B8`, §4 control 18) is decided by the competition's official-game rule, not by an assumption that "shortened = Under."


**Mercy / run rule.** Not used in MLB, NPB, KBO or LMB regular seasons. Used in WBSC/college/high-school/some winter leagues (typically 10 runs after 7 innings, 15 after 5).


**Doubleheaders.** MLB doubleheader games are nine innings (the 2020–2021 seven-inning rule was discontinued). MiLB doubleheader games remain **seven innings** each. Some winter/independent leagues also use seven.


### 9.2 MLB (Major League Baseball)


**Structure.** 30 clubs, two leagues (AL/NL), three divisions each. **162-game** regular season. Universal **DH** since 2022 (both leagues).


**Rosters.** 26 active players (28 from September 1), with a **13-pitcher maximum** (14 in September); 40-man roster; injured lists (15-day, 60-day, 7-day concussion, 15-day pitcher minimum). Option rules govern MiLB movement. Postseason rosters are **set separately for each round** (26 players), so bullpen composition can change between the Wild Card Series and the LDS.


**Pace-of-play (in force 2023–2026).** Pitch timer **15 seconds** bases empty, **18 seconds** with a runner on (Triple-A 14/19 in 2025, tweaked 2026); a violation is an automatic ball, or an automatic strike on the batter if not set and looking at the pitcher with 8 seconds left. **Two pickoff/disengagement attempts** per plate appearance (a third that fails to retire the runner is a balk). **Five mound visits** per team per nine innings. **Three-batter minimum** for pitchers (must face three batters or end the half-inning). **Shift restriction**: four infielders, two on each side of second base, on the infield dirt at the pitch. **18-inch bases** (up from 15). Base coaches must stay in the box until the pitch is delivered (enforced from 2026).


**ABS challenge system (new for 2026).** Full automated ball-strike calls are **not** used; instead each team gets **two challenges** of the home-plate umpire's ball/strike call per game. Only the **pitcher, catcher or batter** may challenge, immediately after the pitch, by tapping the helmet/cap, with no help from the dugout. A successful challenge is **retained**; an unsuccessful one is lost. In extra innings a team that used both challenges gets **one per extra inning** (non-accumulating); a team that kept both keeps both. Applies in the regular season and postseason. The personalised strike zone is set from measured player height and is slightly smaller than the umpire-called zone — this weakens transfer from pre-2026 umpire/framing tendencies (§1).


**Extra innings.** Each half-inning from the 10th begins with an **automatic runner on second base** (the player who made the last out of the previous inning, or a pinch runner). **Regular season only** — the automatic runner is **not** used in the postseason, where extra innings are played under standard rules with no inning cap. This makes the tie-after-nine branch (`BB-B7`) a materially higher-scoring environment in the regular season and an ordinary-inning environment in October.


**Standings and tiebreakers.** Since 2022 there is **no tiebreaker game** (no "Game 163"). Ties for a playoff spot or seed are broken by (1) head-to-head record, (2) intradivision record, (3) record vs. the relevant opponent group, (4) second-half record — mathematically, before the season ends.


**Postseason (2022 format, in force 2026).** **12 teams** — three division winners and three Wild Cards per league. The **top two division winners in each league get a first-round bye**. **Wild Card Series**: best-of-three, all games at the higher seed. **Division Series (LDS)**: best-of-five (2-2-1). **Championship Series (LCS)**: best-of-seven (2-3-2). **World Series**: best-of-seven (2-3-2), home field to the pennant winner with the better regular-season record. Home-field advantage within each earlier round goes to the higher seed. No mercy rule, no tie games, no automatic runner.


**Settlement conventions (MLB).** "Official game" for most bet types is **5 innings** (4½ if the home team is ahead); many books void full-game bets that do not reach 8½/9 unless already decided. **Listed pitcher** bets void if a named starter is changed; "action" bets stand. Run line is **−1.5 / +1.5**. Game totals **include extra innings**; **first-5-innings (F5)** markets settle at the end of the top of the 5th / bottom of the 5th and exclude the automatic runner and late bullpen. Suspended games: most books settle when the game is completed (even a day later); some void if not completed within a set window.


### 9.3 NPB (Nippon Professional Baseball, Japan)


**Structure.** 12 clubs in the **Central League** and **Pacific League**, six each. **143-game** regular season plus ~18 interleague games in a late-May-to-mid-June window.


**Designated hitter.** **Pacific League uses the DH; Central League does not** (Central League pitchers bat). The Central League has announced it will **adopt the DH from 2027** — for any 2026 Central League card the pitcher still hits, which affects the bottom of the order and the double-switch. Interleague and the Japan Series use the DH in all games.


**Tie games.** Regular-season games are capped at **12 innings**; still level after 12 = an official **tie** (no winner). Ties are excluded from winning percentage (the Japanese standings metric). The 2020–2021 no-extra-innings pandemic rule has been discontinued. **Climax Series and Japan Series** games are capped at **15 innings**, then tie (and are replayed / added to the series as needed).


**Rosters.** A ~70-player club control list; roughly **29 registered** with the top team ("ichi-gun") and **25 in uniform / eligible** for a given game. **Foreign-player limit: four on the active roster**, of whom no more than three may be pitchers and no more than three position players (so a 4-import active roster must mix). No pitch timer (trialed in the minors / second team). Three-batter minimum adopted.


**Postseason — Climax Series.** Each league's top three qualify. **First Stage**: 2nd vs. 3rd, **best-of-three**, all games at the 2nd-place club, no ties advantage. **Final Stage**: First Stage winner vs. the **pennant winner**, played at the pennant winner's park, effectively **best-of-seven but the pennant winner starts 1–0** (needs 4 wins from a possible 6 games; the challenger needs 4 of 6). **Japan Series**: best-of-seven (2-3-2), DH in all games, 15-inning tie cap. No mercy rule.


**Settlement note.** Because a regulation NPB game can end **tied**, moneyline/side bets need a stated tie rule (push, or "tie no bet"); this is unlike MLB. Totals settle on the 12-inning final. Draw is a live outcome for any NPB regular-season winner market.


### 9.4 KBO League (South Korea)


**Structure.** 10 clubs, single table, no divisions. **144-game** regular season, roughly late March to early October, no Monday games. Universal **DH** (KBO has always used it).


**Tie games.** Since **2025**, regular-season games are called a **tie after 11 innings** (previously 12), to limit pitcher workload. Ties are excluded from winning percentage and games-behind. Postseason games are called a tie only **after 15 innings**.


**Technology and pace.** KBO uses a **full Automated Ball-Strike System (ABS)** — every pitch is called by the automated zone and relayed to the umpire — **since 2024** (this is a full auto-call, not the MLB challenge model). Pitch clock since 2024, revised for 2026 to **18 seconds** bases empty and **23 seconds** with runners on; pickoff limits and larger bases also adopted. Three-batter minimum.


**Rosters.** 28-player first-team roster (26 dressed for a game in recent seasons); expanded in September. **Foreign players (2026):** three standard imports **plus one** additional player from an Asian country or Australia under a new "Asia quota" — **all four may appear in the same game**. Spending caps apply (roughly US$1m first-year total per standard new import; US$200k total for the Asia-quota player).


**Postseason — step-ladder.** Top **five** teams qualify. **Wild Card**: 4th vs. 5th — the 4th seed needs **one win**, the 5th seed needs **two** (effectively best-of-three with 4th starting 1–0). **Semi-Playoff**: WC winner vs. 3rd, **best-of-five**. **Playoff**: Semi-Playoff winner vs. 2nd, **best-of-five**. **Korean Series**: Playoff winner vs. **1st** (which has rested throughout), **best-of-seven**. Higher seed has home advantage and the rest edge at every rung. No mercy rule.


**Settlement note.** As with NPB, a **tie is a live regular-season outcome** (after 11 innings) — KBO side/handicap bets need a stated tie rule. KBO totals are settled on the 11-inning final in the regular season.


### 9.5 LMB (Liga Mexicana de Béisbol)


**Structure.** A large league (about 20 clubs) split into **Zona Norte** and **Zona Sur**. Regular season runs roughly April–July (schedule length has varied; ~90+ games per club in 2026), then a four-round postseason July–September. Summer heat and altitude are significant (Mexico City ~2,240 m, Puebla, Saltillo). **DH** used.


**Rosters.** 38-player list. **Foreign-player limit: 18** of the 38 for 2026–2027 (reduced from 20); **minimum 20 Mexican-born** players on the 38-man list. This is by far the most import-heavy of the leagues in this register — LMB rosters are close to half non-Mexican.


**2026 rule changes.** LMB adopted an **ABS challenge system** for 2026: **two challenges** per team over nine innings, retained if successful, **one extra challenge per extra inning**. **Three-batter minimum** for all pitchers. **No automatic runner** in extra innings (this was mistakenly applied by umpires in the opening series and publicly corrected — LMB extra innings are played under standard rules).


**Postseason.** Four best-of-seven rounds: **Primer Playoff** (six qualifiers per zone), **Series de Zona** (the three Primer Playoff winners per zone plus the best losing team as a wild card), **Series de Campeonato** (zone final, producing the Zona Norte and Zona Sur champions), and the **Serie del Rey** (Norte champion vs. Sur champion for the title). Seeding by winning percentage, then **run differential**.


**Settlement note.** Confirm the exact schedule/round in force — LMB has changed its playoff qualifier count and regular-season length repeatedly. A "Serie de Campeonato" or "Serie del Rey" game is best-of-seven with standard extra innings.


### 9.6 MiLB and Triple-A (Pacific Coast League)


**Placement.** Triple-A is one level below MLB. The two Triple-A leagues are the **Pacific Coast League (PCL)** and the **International League**. The PCL is a notoriously extreme **hitting environment** — Albuquerque, Las Vegas, Salt Lake, Reno and El Paso are high-altitude or hot-and-dry parks; PCL run environments do not transfer to MLB or to the International League.


**Rules.** Triple-A runs **ahead of** MLB as the rules laboratory, so most MLB rules apply and some are stricter: pitch timer (14 sec bases empty / 19 with runners in 2025, adjusted 2026; a batter timeout resets the clock at Double-A/Triple-A), **automatic runner** in extra innings, **larger bases**, **shift limits**, **three-batter minimum**, pickoff limits. **ABS**: Triple-A has trialed both a full auto-call zone and the challenge system in recent seasons; the **challenge system** is the current Triple-A model, and a **checked-swing challenge** was added to the PCL from **6 May 2026**. **Doubleheaders are seven innings.** Rookie-level games are frequently seven innings due to pitching shortages.


**Rosters and data.** ~28-player active rosters with constant MLB churn (optioned players, rehab assignments, "taxi" moves) — participant identity is more volatile than MLB and must be re-handshaken late (`BB-P1`). Statcast-grade tracking is **not** available at every Triple-A park; treat PCL batted-ball and velocity data as lower-fidelity than MLB (`SFA-BASEBALL` §8.4, and RULES_GENERAL data-priority).


**Postseason.** A single Triple-A National Championship Game between the PCL and International League champions (regular-season-split winners), plus a longer late-season "Triple-A Final Stretch" in some years. Confirm the current structure for any postseason card.


### 9.7 International baseball (WBSC / WBC / Premier12 / Olympics)


Not directly forecast in the current log but the identity template must handle it. Common features: **pool play then knockout**; a **mercy rule** (typically 15 runs after 5 innings, 10 after 7); an **extra-innings tiebreaker** that places runners on **first and second** (not just second) to open each half-inning from the 10th, sometimes with a re-set lineup; **pitch-count limits and mandatory rest** (WBC pitch-smart rules); 28-player rosters. Each event is its own rules era and its own population — do not transfer MLB/NPB/KBO rates into it.


### 9.8 Cross-league settlement and identity checklist (baseball)


| Question | MLB | NPB | KBO | LMB | Triple-A |
|---|---|---|---|---|---|
| Regulation length | 9 | 9 | 9 | 9 | 9 (7 in DH games) |
| Tie possible in regulation/standings? | No | **Yes** (after 12) | **Yes** (after 11) | No | No |
| Automatic runner in extras | Reg. season only | No | No | **No** | Yes |
| Extra-innings cap | None (reg. + post) | 12 reg. / 15 post | 11 reg. / 15 post | None | None |
| DH | Universal | Pacific only (Central from 2027) | Universal | Universal | Universal |
| Ball/strike tech (2026) | Challenge (2/game) | None | Full ABS auto-call | Challenge (2/game) | Challenge + checked-swing |
| Import limit | None | 4 active | 3 + 1 Asia quota | 18 of 38 | None (MLB org players) |
| Postseason champion | World Series (Bo7) | Japan Series (Bo7) | Korean Series (Bo7) | Serie del Rey (Bo7) | 1-game final |


Always resolve, per `BB-P3`/`BB-P4`: the exact league and season, DH status, scheduled innings, the tie/extra-innings rule, the import and active-roster rules, the ball-strike technology in force, and the operator's official-game and listed-pitcher terms — before any rate work.


## September 5 settlement learning — prospective SFA amendment


At the starter-quality, length, defence and relief transitions, add a worked adverse branch for **each** starter. An ace's low walk/home-run baseline does not delete contact sequences and unearned-run exposure. Name which side scores, which inning/base-out state carries the risk and which reliever would enter; do not describe only the less reputable starter's collapse. This operationalises existing controls 14/15/19 and L-039/L-058.


P-281 crossed 6.5 by the fourth inning against the preferred starter; P-282 crossed in a six-run seventh after a 6⅔-inning starter workload. Do not collapse these into one “bullpen” label. Separate runs charged to the departing pitcher from runs scoring while a reliever is on the mound, preserve inherited runners and outs, and model an adverse **long** start as well as an early hook. Both home teams did not bat in the ninth; record absent innings as unplayed exposure, not an observed scoreless inning.


A winning +1.5 in a 13–0 or 11–0 upset does not validate a close low-total mechanism or the opposing winner annotation. Keep result/mechanism grades separate. C-P293-BB-CLUSTERS is a future comparison only; no automatic CPBL Over, ace penalty or correlation coefficient is promoted.




Full evidence and frozen-card comparisons: [September 5 audit](archive/audit_documents_implemented_2026-09-25/COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md).


## September 5(b) settlement learning — P-294–P-305 second continuation


Two same-day, same-league KBO cards (`P-296`, `P-297`) settled with opposite total outcomes, both consistent with a correctly-run starter-quality read; one carried-forward MLB card (`P-288`) settled as an outright HR-cluster upset.


**`P-296` (Doosan @ SSG) — clean win, Under 10.5.** Final 3-2. Both starters (Choi Min-seok, Kim Min-jun) were correctly read as in-form, low-walk, low-home-run arms, and the card explicitly refused to let Doosan's 24-inning scoreless drought become a deterministic continuation signal — a correct, on-the-record application of L-011/L-062 (state the streak's own rate against a baseline, require a named mechanism, do not assume automatic continuation or automatic reversion). SSG's fresher bullpen (a complete-game shutout the day before) was a correctly-weighted tie-breaker.


**`P-297` (Hanwha @ Lotte) — Hanwha ML won, Under 11.0 lost, total 17.** The card had explicitly named Hwang Jun-seo's Aug 30 return-from-injury start (3 IP, 7 H, 1 HR, 4 ER, described as a flat forkball and an early exit) as a live Over mechanism, and Hanwha's own recent form (1-9 in the last ten games before this one) was correctly *not* allowed to override the season-long power/roster-quality read for the moneyline call, which won. But `Under 11.0` was still ranked #2 above `Lotte ML` at #3 despite the same early-hook risk sentence sitting one paragraph away. This is the same subordinate-named-kill-path pattern found in `P-295`/`P-299` this session (see L-075), folded into that rule rather than a duplicate.


**`P-288` (Athletics @ Seattle Mariners, carried forward) — HR-cluster upset.** Athletics hit four home runs in a five-run third inning to beat the home-favoured Mariners 7-6 outright. This is not a new mechanism for this log — it reinforces the already-open `C-PL7-BB-HOOK-TAIL` and `C-PL9-BB-SCORESTATE-RELIEF` candidates (explicit joint batters-faced/hook/inherited-runner/HR-cluster mixture versus a centre-led starter/total treatment) with a fresh supporting case; no new rule is created from a single inherited-deferred card.


**Kill-path library addition (§8.5):**


| Kill path | Defeats | Evidence origin |
|---|---|---|
| An early-hook/short-start risk already named for a returning or recently-struggling starter, sitting one paragraph from a ranked total that assumes his full workload | An Under total ranked above the opposing side's moneyline/total row it is one step from contradicting | `P-297`; L-075 |


Full evidence: [PREDICTION_LOG_COMBINED_2.md, 2026-09-05(b) section](PREDICTION_LOG_COMBINED_2.md#component-import--p-294p-305-second-continuation--2026-09-05b).


## September 6 settlement learning — the bullpen tail, and two new keyless lanes


**Two ESPN fields verified 2026-09-06 that this file did not previously use.** `https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/summary?event=<id>` returns:


- **`injuries[]`** — a per-team injury list with player, status (`Day-To-Day`, `10-Day-IL`, `15-Day-IL`, `60-Day-IL`) and body part. This is a keyless, structured availability feed and belongs in the `G6` participant ledger as a *corroboration* lane; the club/league transaction wire remains the field owner for a same-day activation or scratch.
- **`gameInfo.officials`** — the full umpire crew by position, including the home-plate umpire. Registered as a `SRC-ESPN-SITE-API-BASEBALL` field; it does not by itself license any umpire-based rate adjustment, which would require a validated model.


### `P-297` re-attribution — a contributing factor, not the sole cause


`P-297` (Hanwha Eagles 11, Lotte Giants 6; `Under 11.0` **LOSS** at rank #2) was recorded on September 5(b) alongside a correct Rank #1 (`Hanwha ML` **WIN**). Re-examined under `G20.2`'s tail-budget disclosure, the Under row is a `TAIL_EXPOSED` case worth naming precisely: a total of 17 against a line of 11.0 is consistent with, but not conclusively proven to be, driven by the innings after both starters leave — a card cannot infer the *cause* of a large final total from its size alone. **Correction (2026-09-06(d), second independent review):** the earlier draft of this section overclaimed that a 17-run game "cannot be a starter misread and must arise after the starters." That is too strong. Attribution requires inning-by-inning scoring and pitcher-exposure data, not the size of the final score by itself — early starter failure is an equally live explanation until the innings are actually checked. This file's own recorded case `P-281` (a seven-run fourth inning against the *preferred* starter, per the September 5 section above) is a direct counterexample to any blanket "large total ⇒ bullpen" rule.


**Required from now on, `SFA-BASEBALL` — the tail budget must conserve innings, not just compare rates:**


1. Split the nine-inning exposure explicitly into **starter innings** and **relief innings**, using each starter's own L10 average outs recorded — not a league-average assumption.
2. **Multiply each segment's rate by its actual expected innings/exposure, and conserve the total innings of the game** — a "starter-centre plus relief-high-rate" sum that skips this multiplication is dimensionally incomplete (it adds a per-inning rate to a full-game centre without accounting for how many innings each state actually covers), which was flagged as a defect in the version of this section drafted earlier the same day.
3. Check **both** tails explicitly: an early starter-failure branch (large total from the first several innings, `P-281`-style) and a bullpen-tail branch (large total concentrated after the hook, `P-297`-style). Do not assume the tail must be one or the other without checking inning-by-inning data.
4. Where either bullpen has thrown on each of the previous two days, that side's relief tail term is raised one step and the reason is written down.


### Kill-path library addition (§8.5)


| Kill path | Defeats | Evidence origin |
|---|---|---|
| **Bullpen tail** — both starters perform to expectation and the total still clears, entirely from relief innings | A full-game `Under` budgeted from starting-pitcher quality alone, without checking relief exposure | `P-297` (17 runs against `Under 11.0`) — disclosure only, per the firewall correction below |
| **Early-inning starter failure** — the preferred starter concedes the decisive runs before any hook, independent of bullpen quality | An `Under` or cushion row that assumes the total's shape must come from a bullpen collapse | `P-281` (seven-run fourth inning against the preferred starter) |
| **Early-inning slugging burst** — a single multi-homer inning consumes the whole Under budget before the fifth | `Under` rows in parks/lineups with an upper-decile home-run branch | `P-288` (four home runs in a five-run third; `Mariners -1.5` also lost) |


### Cross-sport gates instantiated here (v3.9)


| Gate | Sport-native instantiation |
|---|---|
| `G10.2` settlement-source pre-registration | MLB, and any competition ESPN carries, settle from `site.api.espn.com/.../baseball/<league>/summary`. KBO/NPB/CPBL are **not** ESPN-covered — name the league's own official box score and the native-language reporting lane instead (`L-067`). |
| `G14.2` coaching / bench / rotation record | Baseball's analogue is the bullpen and bench: available relievers with days-of-rest, the confirmed lineup card, and the manager. Where official feeds have not yet populated (`hydrate=lineups` empty), batting orders and bullpen availability verified across accredited beat reporters or team media releases under Control `S-1 Rev 2` qualify as `PROJECTED_BEAT_VERIFIED`, satisfy `G14.2` exposure modeling, and do not block Rank #1. `injuries[]` corroborates but does not own availability. |
| `G20.2` distributional tail audit | Derive lower-tail, line-boundary/push and upper-tail mass from the **same frozen baseball joint distribution** used for ranking: PA/BF exposure, starter hook distribution, named bullpen chain, park/defence, base-out/HR sequencing, home-ninth entitlement and extra-inning state. Historical second-highest/median order-statistic sums are superseded and must not be used as an active gate or probability proxy. |
| `G21.1` exact target geometry | Map every supplied total/phase-total to its exact settlement event and derive WIN/PUSH/LOSS (plus void/censoring where applicable) from the same frozen sport-native PMF/CDF or coherent branch mixture. Genuine unions may be described as unions, but historical `TRUE_UNION` / `LOW_BAR_CUMULATIVE` / `CENTRAL_BAND` path-count labels have **no mandatory ordinal effect** and are not a substitute for the distribution. |
| `G26.1` no universal separation floor | Print any relevant reference base rate and `rank_gap` descriptively. **No 40–60% or other pooled probability band can disqualify Rank #1.** Rank by the row's exact marginal likelihood from the frozen joint distribution plus robustness/evidence uncertainty; precise probabilities require the validated-model gate. |


**Pre-issue checklist additions (this sport):** settlement endpoint named per row; coaching/bench/rotation record for both sides with missingness codes; tail-budget sums printed against every total line **with innings conserved and both failure branches checked**; path-geometry class printed for every total and phase-total row.


Full narrative and evidence: [`archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md`](archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md). Controlling gate text: [`RULES_GENERAL.md` §§13–15](RULES_GENERAL.md).


## September 5 implementation after freeze confirmation


**ACTIVE REQUIRED PROCESS — MDS-2026.09.05-v3.6 / L-068–L-072.** Before ordering the total, evaluate both starters’ contact/traffic/error failure paths and the starter-to-reliever transition, including inherited runners. A strong opposing starter can support a total without supporting the other side’s cushion. Record the exact scoring budget under each side’s winning/separation branch.


At final delivery, record the preferred total direction for each exact target, the strongest evidenced failure path for ranks #1 and #2, and whether both can win under the stated joint scenario. Rank by supported marginal likelihood; do not promote an opposite pick solely to manufacture one O/U win. At settlement, keep all issued wins/losses, including defective reasoning, in the applicable historical scorecard and review failed #1/#2 and preferred totals.


[Eligibility policy](PERFORMANCE_ELIGIBILITY_POLICY.md): non-live history is user-confirmed frozen pre-game; explicit live-issued views stay separate. These process repairs are implemented now. Numerical weights and predictive-lift claims need a later frozen comparison; historical origin games do not supply those completions.


## 2026-09-06(f) — settlement and retrospective addendum


P-288/P-312/P-313/P-314/P-317 reinforce separate starter, reliever, lineup and score-state exposure. P-313 stayed Under despite early hooks; P-317 reached 25 despite Logue delivering six one-run innings. A bullpen game or a scoring drought has no automatic directional sign. P-314 seven runs wins Under 8.5 but loses Under 6.5; alternate lines share an event. P-274 operator-listed starter terms remain separate from actual-game research grades.


Full frozen ranks, actual drivers, knowability and smallest fixes: [PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md). Reinforcement only; METHOD v4.0 remains controlling and no new predictive weighting is promoted.


## 2026-09-09 settlement learning — P-335 (MLB), P-339 (KBO)


Two cards, two different leagues, **the same failure mode**, both landing on the total and the margin ([`PREDICTION_LOG_COMBINED_3.md` §"2026-09-09"](PREDICTION_LOG_COMBINED_3.md)):


| Card | Frozen Rank #1 / Rank #2 | Result | Mechanism |
|---|---|---|---|
| `P-335` San Diego 3–2 Washington (`MLB PRIMARY_SCORED`) | R1 `WSH +1.5` p0.59 **W**; R2 `Over 8.0` p0.52 **L** | Pivetta 5.0 scoreless IP on his return; 5 total runs | Return-uncertainty was given a **+0.20 net Over** adjustment; the normal/strong return branch carried no comparable mass |
| `P-339` Hanwha 6–1 Doosan (`EXPLORATORY`) | R1 `Doosan +1.5` p0.60 **L**; R2 `Over 9.5` p0.56 **L** | Ryu Hyun-jin 6 IP / 1 R; 7 total runs, margin 5 | Ryu's established skill prior was outvoted in the arithmetic by a 7-start second-half slump and a 3-start opponent split; the "reverts to skill" branch was *named* but not weighted competitively |


**Root cause — corrected on second-pass research (2026-09-09).** The first reading of this cohort called it a mass-allocation error. Opening the underlying records shows something sharper and more fixable: **in both cards an aggregate statistic stood in for a disaggregated record that was available from a source the card had already cited, and the disaggregated record pointed the other way.**


**`P-339` — Ryu Hyun-jin's actual game log.** The card used "0–3, 7.31 ERA through seven second-half starts". The KBO official English player page — **already listed in the card's own source register** — carries the game log. His four starts entering 2026-09-08 were:


| Date | Opp | IP | ER | SO | BB |
|---|---|---:|---:|---:|---:|
| Aug 13 | Doosan | 3⅓ | 7 | 3 | 2 |
| Aug 20 | Kia | 6.0 | 4 | 5 | 0 |
| Aug 26 | SSG | 5.0 | **0** | **7** | **0** |
| Sep 2 | KT | 5.0 | 3 | 5 | 1 |


Three things the aggregate hid: the slump was **front-loaded** (the disaster start was three weeks old); the **most recent quality evidence was a scoreless 7-strikeout start**; and **his command never broke** — 2/0/0/1 walks across the window, against **17 walks in 125⅔ innings** for the season (~1.2 BB/9, elite). An ERA-only slump with an intact walk rate and a recent dominant start is a **noisy-outcome slump**, not a skill decline — and control 13 already asks for exactly these "arsenal/velocity/location" indicators rather than the ERA line. He then threw 6.0 IP / 1 ER.


**`P-335` — Pivetta's rehab pitch-count ladder.** The card recorded "4.1 innings for Triple-A El Paso on Aug 30" — **innings only**. The full rehab ladder was **14 pitches → 47 pitches (3 IP) → 64 pitches (4⅓ IP, scoreless, 7 K, 44 strikes)**. A starter who has just completed 64 pitches scorelessly is stretched to roughly 5 major-league innings, and that is precisely what happened: **63 pitches, 5.0 scoreless innings, 39 strikes**. The "short start → early relief transition → Over" branch that received a `+0.20` net scoring adjustment was **contradicted by the rehab evidence the card had partially retrieved**. The innings figure was recorded; the pitch count, strike rate, strikeout total and scoreless result — the four fields that actually forecast the MLB workload ceiling — were not.


Both are instances of the new cross-sport retrieval gate **`RULES_GENERAL.md` §16.5(c) / `G-L7`**. The secondary error — converting the resulting uncertainty into a signed Over lean rather than width (§16.5(b) / `G-L2`) — is real but downstream of the retrieval gap.


**What went right (keep it):** `P-335` cushion decomposition (control 4) and the one-run-favourite-win coexistence (control 17) were correct — Rank #1 won. `P-339` potential winner (Hanwha) was correct, Choi's traffic vulnerability + Hanwha's power were correctly named as the run mechanism, and the KBO tie branch was preserved (control 22). Winner identification is working; the total and margin corridors are where both cards missed.


### Structural control additions


24. **The starter's game log outranks any multi-start aggregate.** Before an ERA line, a "last N starts" summary or an opponent split may carry directional weight, retrieve and print the **per-start log** for that window: innings, earned runs, strikeouts and **walks** per start. State explicitly whether the run of poor results is front-loaded, back-loaded or uniform, and whether **command (BB/9) held** through it. A slump in which walks stayed at or below the pitcher's season rate and at least one recent start was strong is a **noisy-outcome slump** and is shrunk hard toward the season/skill prior; a slump accompanied by a walk-rate breakdown, a velocity drop or an arsenal change is a **regime change** and may move the centre. `AGGREGATE_ONLY` (log not retrieved) caps the dependent total and margin rows at `FORCED RANK` (`RULES_GENERAL.md` §16.5(c)).


25. **A returning starter's workload ceiling comes from the rehab pitch-count ladder, not from innings.** For any starter returning from the injured list, record the **full ladder** — pitches, innings, earned runs, strikeouts and strike rate for **every** rehab outing in order. The last rehab pitch count is the primary estimator of the first major-league start's ceiling (`P-335`: 64 rehab pitches → 63 major-league pitches; 4⅓ rehab innings → 5.0 innings). Only after that ladder is printed may a short-start/early-relief branch take a **signed** total adjustment; a ladder ending in a long, efficient, scoreless outing is evidence *against* that branch, not neutral.


**Fixes — reinforcement of existing controls plus the two new controls above, no fitted weight (`L-087`):**


- **Control 11 (small-sample starter mixture) and control 13 (season prior vs current regime) remain the governing controls**; controls 24 and 25 specify the *retrieval* they require, which is what actually failed here. Control 13 already said "do not let a famous season line **or** a short hot/cold run win silently" — the short run won because nobody opened the log.
- **`RULES_GENERAL.md` §16.5(c) / `G-L7`** generalises this across sports: an aggregate cannot carry directional weight while its disaggregated record sits unopened in a source the card already cites.
- **G-L2:** State the prior and scenario probabilities. Symmetric uncertainty around an unchanged prior affects width; hierarchical shrinkage or asymmetric scenarios may change both mean and variance. Regenerate all dependent probabilities; unsupported directional adjustments remain prohibited. SCORING_AND_VALIDATION section 5 controls.
- **`RULES_GENERAL.md` §16.5(a) / `G-L1`:** the joint run object must enumerate the run-total families with explicit mass and place every §8.5 kill path as a weighted branch — a "Ryu reverts" or "Pivetta returns strong" sentence must carry a number.
- **`RULES_GENERAL.md` §16.5(d) / `G-L8`:** print the total row's normalised edge `|centre − line| / width` beside its probability. `P-335` computed a `+1.1` edge on a `±3.2` width (normalised **0.34**, the largest on its cohort) and assigned the Over the *lowest* probability of any total on the cohort (0.52). The ordering was not derived from the arithmetic.


### Kill-path library addition (§8.5)


| Kill path | Defeats | Evidence origin |
|---|---|---|
| A returning or slumping starter performing at or above his shrunk skill prior (strong 4–6 scoreless innings) while the card took a net Over adjustment from "return/slump uncertainty" | An `Over` ranked above its `Under`, and an underdog `+1.5` ranked on an expected close low-total game | `P-335`, `P-339`; controls 11, 13, 24, 25; `G-L2` |
| A veteran's short bad-run ERA line or small opponent split treated as an active mechanism rather than a noisy outcome summary — **front-loaded slump, command intact, recent strong start already in the log** | A total or margin centre shifted toward the opponent on streak evidence with no current pitch-quality mechanism | `P-339` (7 ER/3⅓ → 4 ER/6 → **0 ER/5, 7 K, 0 BB** → 3 ER/5; 1.2 BB/9 season); `G17`/`G17.1`, controls 13, 24 |
| A rehab pitch-count ladder ending in a long, efficient, scoreless outing, read as "innings only" and treated as neutral | A short-start/early-relief `Over` adjustment on a returning starter | `P-335` (14 → 47 → **64 pitches, 4⅓ scoreless, 7 K** → 63 MLB pitches, 5.0 scoreless); control 25, `G-L7` |


### Pre-issue checklist addition (§8.7)


Add:


- **Per-start game log printed for both starters** over the decision-relevant window (IP / ER / SO / **BB** per start), with an explicit front-loaded / back-loaded / uniform verdict and a command-held yes/no (control 24). `AGGREGATE_ONLY` if not retrieved, and the dependent total/margin rows capped.
- **Full rehab pitch-count ladder printed** for any returning starter — pitches, innings, ER, SO, strike rate per outing, in order — before any short-start branch takes a signed total adjustment (control 25).
- Run-total family enumeration printed with explicit mass (`RULES_GENERAL.md` §16.5(a)); the normal/strong-outing branch quantified and given mass before any net total adjustment (§16.5(b) / `G-L2`).
- **G-L8:** Derive each total/spread probability from the exact joint PMF/CDF and settlement endpoint, with push mass. Absolute normalised distance does not order probabilities across different distributions. No missing width or realised result justifies an invented probability.
- Representative Rank-#1 final score written and checked against the run line and the total line.


## 2026-09-11 settlement learning — `P-347`, `P-348`, `P-349`, `P-351` (MLB), `P-353`, `P-354`, `P-361` (NPB), `P-356`, `P-362` (KBO), `P-365` (CPBL)


Ten baseball cards ([`PREDICTION_LOG_COMBINED_3.md` §"2026-09-11"](PREDICTION_LOG_COMBINED_3.md)). Rank #1 **8 W / 2 L** (`P-356`, `P-365` lost). Top two both won on 2 of 10 (`P-349`, `P-351`). Potential winners 6 / 10. Preferred main-line total: **Unders 6 W / 2 L; Overs 0 W / 2 L** (`P-348`, `P-351`). Team totals: **Unders anchored on the stronger, established starter 6 W / 2 L; Overs on the side facing the weaker starter 2 W / 4 L.** Learning-only per user direction; no fitted weight or ordinal bar (`L-087`).


### Measured precision of the run centres — twelve cards


| Card | League | Stated centre | Actual total | Actual − centre |
|---|---|---:|---:|---:|
| `P-335` | MLB | 9.10 | 5 | −4.10 |
| `P-339` | KBO | 10.25 | 7 | −3.25 |
| `P-347` | MLB | 7.60 | 15 | +7.40 |
| `P-348` | MLB | 9.87 | 6 | −3.87 |
| `P-349` | MLB | 7.70 | 3 | −4.70 |
| `P-351` | MLB | 8.36 | 5 | −3.36 |
| `P-353` | NPB | 6.03 | 6 | −0.03 |
| `P-354` | NPB | 5.51 | 4 | −1.51 |
| `P-356` | KBO | 9.99 | 2 | −7.99 |
| `P-361` | NPB | ~5.0 (corridor midpoint; no numeric centre printed) | 8 | +3.00 |
| `P-362` | KBO | ~7.75 (corridor midpoint) | 7 | −0.75 |
| `P-365` | CPBL | ~5.8 (corridor midpoint) | 6 | +0.20 |


**Mean −1.58 runs; mean absolute 3.35; 9 of 12 games finished below the stated centre.** Twelve dependent, mixed-league cards prove nothing statistically, but the direction is consistent and the mechanism is visible in the cards' own arithmetic (control 26). Registered as the prospective test **`C-RUN-CENTRE-BIAS`** (`LEARNING_REGISTER.md`); no recalibration coefficient is applied meanwhile.


### What went right (keep it)


- **Cushion decomposition (control 4) and low-total separation (control 17) work when applied:** `P-347` TEX +1.5, `P-349` SF +1.5, `P-354` HIR +1.5, `P-356` KT +1.5 and `P-362` HAN +1.5 all won.
- **Team-total Unders anchored on starter skill:** `P-349` (both, behind Roupp and Mathews), `P-351` (Reds v Skubal), `P-353` (Chunichi), `P-354` (Hiroshima), `P-356` (KT).
- **Field-owner handshakes:** NPB posted batting orders, batteries and full benches (`P-353`, `P-361`); `P-356` printed a final-state mass table and a normalised edge (0.12) — the only baseball card to do both.
- `P-349` is the model low-total card: protected side plus two team-total Unders, all four rows won.


### What went wrong, linked to earlier lessons


1. **Same-channel adjustments stacked (`P-348`, `P-356`, `P-351`).** `P-348` built 8.42 + 0.60 park + 0.30 heat + 0.45 Perkins + 0.20 Athletics form + 0.10 bullpen − 0.20 Springer = 9.87 (actual 6). Park, heat and same-park recent scoring are largely one channel. Repeats the `P-297` double-count note (§"September 6") and `G22`. → **control 26**.
2. **An elite-hitter absence and a platoon edge treated as scalars (`P-351`, `P-353`, `P-361`).** Ohtani's absence was −0.40 runs; a "five left-handers in the top six" headcount stood in for PA-weighted exposure — while Dalbec, the right-handed #3, homered against a left-hander on consecutive days. → **control 27**.
3. **The opponent's established starter's long-start branch carried no mass (`P-354`, `P-356`).** Tokoda threw 8 scoreless; Ko 7 scoreless — after the card weighted one 3-inning / 7-run start equal to 41.1 second-half innings. Repeats control 13 and `G-L2`/`G-L7`. → **control 28** and `RULES_GENERAL.md` §16.5(g).
4. **Named kill paths without mass (`P-347`, `P-361`, `P-362`, `P-365`).** Miller's hook branch; a single multi-run homer on a 5.5 line; the one-run favourite win against −1.5; the 4–1 / 5–1 separation against +1.5. → `RULES_GENERAL.md` §16.5(e) (`G-L9`).
5. **`G14.2` breached (`P-362`, `P-365`).** Posted batting orders and benches, normally available before first pitch, were not retrieved, yet a full-game total (`P-362`) and a margin (`P-365`) were ranked #1. The block exists precisely for this. → §16.8 item 7.
6. **Mean centre above the line with an Under chosen on skew, not shown (`P-347`, `P-349`).** → `RULES_GENERAL.md` §16.5(d) addendum: print the median-based `P(total ≤ line)`.


### Structural control additions


26. **Mechanism-overlap audit for run-centre adjustments.** List every signed adjustment with its causal channel — starter run prevention, bullpen, lineup quality, park/HR factor, weather carry, recent same-park scoring, defence. Adjustments that share a channel do not each take full weight: park factor, same-park recent scoring and hot-weather carry are largely one "the ball carries here" channel; a starter's ERA, his "last N starts" and his opponent split are largely one starter-quality channel. When three or more same-signed adjustments move the centre by more than one run from the season-prior sum, print the net in one line and justify it against the starter-skill prior. Origin `P-348`, `P-356`, `P-351`. Disclosure/arithmetic only — no coefficient.


27. **Lineup exposure is plate-appearance-weighted.** Convert an absent hitter, a platoon edge or a lineup change through **expected plate appearances by batting slot** — roughly 4.6–4.8 for the leadoff spot, falling to about 3.8–3.9 for the ninth in a nine-inning game (approximate; state the figures used) — multiplied by the hitter's run value and home-run rate. Not a flat run subtraction; not a count of same-handed hitters. Origin `P-351` (Ohtani), `P-353` and `P-361` (Dalbec).


28. **Opponent starter and full-game branch.** Before a team-total Over, favourite win or handicap, inspect the established starter's per-start workload, contact, strikeout and walk record, then continue every scenario through relief and any extra innings. Six-plus innings allowing at most one run is not itself a guaranteed full-game losing state. Count disjoint completed-game failures, not overlapping mechanism masses (corrected G-L9/G-L11 and section 16.9). P-354/P-356 motivate this check; P-266 shows why strong starts can coexist with a full-game Over.


### Kill-path library additions (§8.5)


| Kill path | Defeats | Origin |
|---|---|---|
| The opponent's established starter going six-plus innings with one run or fewer | Favourite team-total Over; favourite moneyline / −1.5 | `P-354`, `P-356`; control 28 |
| One run-environment channel counted as several Over adjustments | A game Over built on park + heat + same-park form | `P-348`; control 26 |
| An elite hitter's absence treated as a flat run subtraction | Favourite team-total Over and −1.5 (a dependent pair) | `P-351`; control 27 |
| One ordinary cluster — a multi-run homer or one relief inning — crossing a low line | Under 5.5 / 6.5 at 0.56+ | `P-361`; `G-L9` |
| Low-total separation (shutout; 4–1; 6–0) | Underdog +1.5 ranked #1 in a low-total game | `P-365`; control 17 |


### Pre-issue checklist additions (§8.7)


- Mechanism-overlap line: each adjustment's channel, and the net when three or more share a sign (control 26).
- PA-weighted exposure line for any absent hitter or platoon claim (control 27).
- The opposing established starter's long-start branch with mass, before any team-total Over or favourite row (control 28).
- Complement decomposition for Rank #1 and Rank #2 (`G-L9`); `P(R1 ∧ R2)` with its coupling label (`G-L10`).
- Median-based `P(total ≤ line)` printed beside the run-total probability (§16.5(d) addendum).
- Posted batting orders and benches for both sides (`CONFIRMED_OFFICIAL` or `PROJECTED_BEAT_VERIFIED` under Control `S-1 Rev 2`), or `RETRIEVAL_MISS` — and no margin or full-game total at Rank #1 without the bench (`G14.2`).


### Source notes (this pass)


- **MLB statsapi** returned HTTP 406 to the WebFetch tool; a plain `curl` client works (schedule, linescore). A candidate route for posted batting orders — the statsapi live feed's `battingOrder` field — is to be **tested at the next MLB card** before any lineup is labelled `SECONDARY_ONLY`; its pre-game availability has not yet been demonstrated.
- **KBO English scoreboard** (`eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=YYYY-MM-DD`) gives line scores and decisions and is readable by the fetch tool — the English field-owner rung under `L-067`.
- NPB BIS and CPBL Advanced Stats remain the field owners for their leagues.




## 2026-09-12 algorithm corrections and retrospective integration


Use a joint home/away final-run distribution with regulation/extra-innings scope explicit. A six-inning, one-run starter branch still needs the remaining bullpen and batting innings before a full-game team-total grade follows; remove control 28's automatic subtraction of its entire mass from every favourite/Over probability. P-361 Under 5.5 crossed at 3-3 in inning four; inning eight decided the side. P-365 requires the walk/control branch as well as contact: Yu walked five and allowed four runs (three earned), while Dykxhoorn completed seven scoreless innings. PA weights are scenario inputs, not universal league-independent constants. Verify actual eligible reserves as well as the nine starters; a postgame substitution list alone is not the pregame bench.


For every supplied row, use exact target probabilities from a coherent joint distribution; handle push/void/censoring explicitly, avoid overlapping adverse-state counts, and report JOINT_UNQUANTIFIED with bounds if the dependence is not specified. Separate issued-time participant capture, later recovered evidence, source accuracy by field, observed mechanism, and unverified causal interpretation. Keep one preferred O/U direction per distinct target and report the top-two denominator honestly. Shared correction and methodology sources (`audit_2026-09-12/rule_corrections.md`, not present in this repository). All current log observations remain learning-only and not performance-eligible.




## Recovered mini-log reinforcement - 2026-09-12


P-266 (official MLB 823983) was 1-1 after nine and 6-3 after ten despite both starters allowing one run: extend the same score model into ties/extra innings and remaining relief, rather than declaring the starter thesis false. P-260 (823339) finished 5-4 after ten and both 9.0 totals pushed: show push probability separately. P-259 (822931) demonstrates why a returning favourite starter's workload/early-traffic failure and bullpen state need complete-game scenarios. These reinforce CL-P267 and corrected G-L9; no automatic Over or underdog coefficient is promoted. Exact evidence and frozen-row grades: audit_2026-09-12/recovered_historical_retrospectives.md and recovered_mlb_evidence.md in that folder.






## 2026-09-15(b) settlement learning — `P-373`–`P-423` import


Learning-only; disclosure/process changes only — no coefficient or ordinal bar (`L-087`). Evidence and tables: [`PREDICTION_LOG_COMBINED_3.md` §"2026-09-15(b)"](PREDICTION_LOG_COMBINED_3.md). Cross-sport rule: `RULES_GENERAL.md` §16.10 (`G-L12` margin centre/width; fixture identity; official-record derivative settlement).


**Cards:** MLB P-373, P-390–P-393, P-403, P-404, P-416, P-420, P-421, P-423; NPB P-381–P-383, P-405, P-417; KBO P-384, P-385. Every final re-verified (MLB statsapi, NPB and KBO English pages).


### What went right (keep it)
- Official starter identity over stale previews (P-421 Kremer not Ober; P-423 Mize not TBD); every log-C starter matched the box score.
- P-381/P-384/P-385 run lines and P-421 (top two both won): starter asymmetry + lineup deficit with named mechanisms.


### What went wrong, linked to earlier lessons
1. **Run-line underdog cushions:** baseball Rank-#1 +1.5 rows `P-345`–`P-423` went **4 W / 6 L** at a mean stated ≈ 0.62 (P-365, P-373, P-383, P-391, P-403, P-420 lost). P-420 printed López's IL-return ladder (Sep 9 return: 4.2 IP, 6 ER) and "López return collapses" as its first kill path, yet centred the margin at Cubs +0.3; López lasted 3.0 IP (5 ER). → control 29, `G-L12`.
2. **Road favourite −1.5 at a high-scoring park:** P-423 lost by one run at Coors with Colorado batting last; the exactly-one-run mass (≈12%) was implied but not printed.
3. **Extra innings:** P-393 (MLB automatic runner: 4–4 after nine, 6–5 in the 10th killed Under 10.5) v P-405 (NPB: 0–0 through ten, 1–0 in 11). Control 22 already requires competition-specific extras — reinforced with these worked examples.
4. **One-team total branch:** P-417 Under 5.5 lost at 6, all Chunichi (two in the 9th); P-404 Seattle alone scored 19 (`G-L9`).
5. **`C-RUN-CENTRE-BIAS` update:** log-C MLB total residuals −5.4, +0.5, +2.3, +3.8 (mean +0.3, n=4) — no support in this cohort for centres running high.


### Structural control additions
29. **Run-line decomposition.** For any ±1.5 row ranked in the top two, print (a) P(favourite by 2+) from the margin table, (b) the exactly-one-run mass split by whether the home side bats last, and (c) for a starter back from the injured list within his last two starts, the early-hook branch mass (fewer than 4 IP) with its source (rehab/return ladder, control 25).


### Kill-path additions
| Kill path | Defeats | Origin |
|---|---|---|
| IL-return starter hooked in the first three innings | Underdog +1.5 on his side | P-420 |
| Home-last-bat one-run finish | Road favourite −1.5 at a high-scoring park | P-423 |
| One team alone clears the total | A full-game Under built on one strong starter | P-404, P-417 |


## 2026-09-16 settlement learning — external variant C′ facts verified (`P-416`, `P-417`, `P-420`, `P-421`, `P-423`)


Learning-only; disclosure only (`L-087`). Cross-sport rules: `RULES_GENERAL.md` §16.11. Facts verified on 2026-09-16 at MLB statsapi `api/v1.1/game/<gamePk>/feed/live` and the NPB English box score.


### What the verified records add
- **P-416 (Yankees 2–0 Mets).** Both runs were solo home runs (Rice in the 1st, Wells in the 3rd). Schlittler went 6.0 IP, 1 H, 0 R, 8 K; conditions were rain with a 5 mph wind in from left. Under 8 and Yankees −1.5 won together: a low total does not imply a close margin.
- **P-417 (Dragons 6–0 Tigers, NPB Central League).** Muller pitched 9.0 IP, 4 H, 0 R, 7 K, **and went 4 AB, 2 H, 4 RBI**, including a two-run homer in the 5th. The starting pitcher batted in this game, so his plate appearances were live run exposure.
- **P-420 (Cubs 7–3 Braves).** López lasted 3.0 IP (5 ER, 62 pitches). **Smith-Shawver absorbed 5.0 IP** (2 R, including Crow-Armstrong's two-run homer in the 6th for 7–0). Atlanta's three-run 7th off Assad took the total to 10, so the Over won by 0.5.
- **P-421 (Yankees 8–3 Twins).** Correction to C′: the Twins **led 2–1 entering the 8th** (C′ said "tied 2–2"). Morris (0.1 IP, 3 R) and Minter (0.0 IP, 3 R) allowed the six-run 8th, which included Judge's three-run homer.
- **P-423 (Padres 8–7 Rockies).** San Diego led 6–1 after three. Mize went 5.0 IP with 8 H and **0 K**; **Kyle Hart then gave up 3 runs in 0.1 IP in the 6th** (6–2 → 6–5). Wind was 19 mph in from left at Coors.


### Structural control additions
30. **Starter-exit transition inning.** For any run line or total in the top two:
    - name the starter's expected exit point (pitch-count and innings distribution);
    - name the reliever(s) most likely to take the next inning in each score state, with their recent workload;
    - give the branch "first relief inning concedes 2+" explicit mass.


    At settlement, record the runs scored in that inning. Origin: P-420 (length reliever after a three-inning start), P-423 (Hart's 6th), P-421 (the 8th). This joins control 29's hook branch to the relief ladder; it supersedes nothing.
31. **NPB/KBO/CPBL team-total rows.** (a) Free team-total rows in these leagues went **3 of 6 at a mean stated 0.72** (`P-345`–`P-423`). Open the opposing starter's game log (`G-L7`) and the posted batting order before a team total carries p ≥ 0.65. (b) Where the starting pitcher bats (as in P-417, NPB Central League), his plate appearances are a named exposure branch.


### Kill-path additions
| Kill path | Defeats | Origin |
|---|---|---|
| First reliever after a five-inning start concedes a crooked number | Favourite −1.5 at a high-scoring park | P-423 |
| Starting pitcher drives in runs | A full-game Under built on both starters' run suppression | P-417 |


## 2026-09-17 settlement learning — `P-432`–`P-435` (KBO)


Learning-only (`L-087`). Cross-sport rules: `RULES_GENERAL.md` §16.12. Evidence: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17"](PREDICTION_LOG_COMBINED_4.md). **Verification limitation:** the four finals were **not** independently re-verified this pass — the KBO English scoreboard returned 174 bytes and the proxy 385; they are carried from the mini log's cited Korean reports (see `SOURCES.md` §"2026-09-17").


### What went right (keep it)
- **`P-434` and `P-435` won every ranked row** (Brier 0.0809 and 0.0629) on the same structure: a **pitcher strikeout floor with a real exposure base**, a wide Under, and a protected handicap. `P-435`'s Avila had 4+ K in all ten KBO starts and 6 K in each of two starts against this exact opponent; he returned 11 K.
- **Sport-native current-regime mechanisms beat narrative** (`P-433`): Clevinger's manager-stated 50–60 pitch cap on a KBO debut forced early middle-relief exposure, which drove both LG rows.
- **Low totals still do not imply close margins** — `P-435` finished 4–1 under a winning Under, and `P-434` 3–1.


### What went wrong, linked to earlier lessons
1. **`P-432`: the winner family omitted the tie.** KT 55% / Hanwha 45% summed to 100% in a competition that permits a terminal tie after capped extra innings; the game finished **4–4**. The graded rows were unaffected — this is a labelling-integrity defect. → control 32 and `G-L19`.
2. **Allocation again** (`P-433`): the combined Over 10.5 won with **LG supplying nine of eleven runs** while the NC team-total Over lost. → `G-L18`.


### Structural control additions
32. **Terminal end-state ontology for tie-permitting competitions.** For KBO, NPB and any competition whose regular-season rules allow a game to end tied after a capped extra-inning limit, the winner/end-state family must be **three-way**: home win / away win / tie, summing to 1, with the competition's exact innings cap recorded from its own rulebook as a `G0`/`G2` identity field. Never renormalise tie mass into the two sides, and never issue a two-outcome winner label in these competitions. Handicap and total rows are unaffected. Origin `P-432`.
33. **Strikeout-floor prop gate (positive model).** A pitcher strikeout-floor row may be ranked highly only with all four printed: (a) the **exposure base** — starts at or above the threshold out of total starts, plus innings and K rate; (b) a **direct opponent split** where one exists; (c) the **early-exit branch** — injury, weather, a short leash or an unusually low batters-faced path — with its own mass; (d) the settlement definition (official credited strikeouts). Origin `P-434` (3+ K in all nine KBO starts) and `P-435` (4+ K in all ten, 6 K twice against this opponent). This is a contract-selection disclosure, not a claim that props are generally superior.


## 2026-09-17(b) settlement learning — `P-442`–`P-444`, `P-446`–`P-450` (MLB) — **the first `PRIMARY_SCORED` cohort in Part 4**


Learning-only (`L-087`). Cross-sport rules: `RULES_GENERAL.md` §16.13 (`G-L21` card-level failure mass, `G-L22` forced-pair measurement, `G-L23` result-versus-process). Evidence: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17(b)"](PREDICTION_LOG_COMBINED_4.md). **All eight finals and both extra-inning regulation splits were independently verified this pass** at `statsapi.mlb.com`.


Eight cards, all issued on the same supplied structure `{dog +1.5, fav −1.5, Over L, Under L}` — two forced pairs, so each card scored 2 W / 2 L by construction. As **decisions** they went **10 / 16**: run lines 6/8 (mean stated 60.9%, realised 75%), totals 4/8 (mean stated 47.4%, realised 50%). Rank #1: 6 W / 2 L. Mean row Brier 0.2293.


### The 2026 MLB reference geometry


Derived in this pass from `statsapi.mlb.com/api/v1/schedule?sportId=1&startDate=…&endDate=…&gameType=R&hydrate=linescore`, **every completed 2026 regular-season game through 16 September, n = 2,286**. These are **published base rates from the competition's own record**, used as identity inputs in the same way the NFL width floor is used in `G-L12` (§16.10(h)). They are not fitted, and they carry no ordinal bar. Refresh them at the start of each season and record the `n` and the retrieval date with any card that cites them.


| Quantity | 2026 value | Note |
|---|---:|---|
| P(final margin = 1 run) | **27.8%** | 635 of 2,286 |
| **`r` = P(margin = 1 \| winner), by winner-minus-loser season W% gap** | −0.2: **28.4%** · −0.1: **30.1%** · 0.0: **28.2%** · +0.1: **26.8%** · +0.2: **22.9%** | **Nearly flat.** Only the largest mismatches move it, and only to ~23% |
| P(margin ≥ 2) / P(margin ≥ 3) | 72.2% / 53.3% | |
| **P(tie after 9 → extras)** | **8.75%** | 200 games |
| P(final margin = 1 \| extras) | **68.5%** | 2 runs 20.5%; 3+ 11.0% |
| Runs added by extras | mean **2.88**; P(≥2 added) **60.5%**; P(≥4) ~24% | regulation total in those games: mean **6.81**, median 6 |
| Mean / median total runs, sd | 8.98 / 8, sd 4.53 | |
| Largest unconditional push mass at any integer total | **11.5% at L = 7** | L = 8 → 8.1%; L = 9 → 9.1%; L = 11 → 7.3% |
| Share of total-runs variance explained by park identity | **4.3%** | 30 parks, between-park variance of means 0.885 against a total variance of 20.49 |
| 9-inning games only: P(margin = 1) | 23.9% | extras are what lift the all-game figure to 27.8% |


### What went right (keep it)


- **Winner and margin kept separate** (`P-448`, `P-450`, `P-442`). Three cards refused to convert home last-bat, bullpen quality or starter quality into a favourite run line. The two that held the separation cleanly (`P-448`, `P-450`) won **both** top rows while the winner label lost on both. This is the most reliable structure in the cohort and it is preserved unchanged.
- **Disaggregated records beat aggregates, twice, decisively** (`G-L7`, `M13`). `P-449` refused to let Robbie Ray's two poor September starts define him — he threw six innings with six strikeouts. `P-443` kept Anthony Molina's good-start branch alive on FIP 3.82 / xERA 4.08 against a 5.24 ERA — he threw 5.2 scoreless. Both branches were named *before* the game and both realised.
- **Honest near-50% totals.** All eight preferred total sides sat at 44–53% and went 4/4. A no-signal forecast that says so and lands at the coin flip is working correctly. **Do not "fix" this by manufacturing separation between the two sides of a forced pair.**
- **Small-sample handling** (`G-L11`): `P-449` treated Mason Adams' short MLB sample as width and named the hidden-regression branch rather than taking a signed direction from it.
- **Partial information stored at its true grade**: `P-447` kept a same-day reported Texas lineup as `current reported` rather than upgrading it to `CONFIRMED_OFFICIAL`; `P-444` kept Judge's expected return as a high-quality projection, not a posted order.


### What went wrong, linked to earlier lessons


1. **Every favourite −1.5 row compressed the one-run band.** `P-444` implied `r` = 18.8%, `P-446` 15.2%, `P-449` 14.1% — against a 2026 range of 22.9–30.1%. Applying the correct `r` moves all three rows to **0.46–0.53** and takes each out of Rank #1. This is the mirror image of the `G-L12` failure the NFL width floor was written for: there, uncertainty was centring the margin toward pick'em; here, confidence was narrowing it toward separation. → **control 34**.
2. **Push mass over-stated on seven of eight cards** (11–15% used; 5.4–13.2% realised at those venues; 11.5% is the league maximum at any integer). Inflating the push deflates both sides of the pair, flatters Brier on a loss and pushes the whole total pair down the rank order — plausibly why a side row was ranked #1 on all eight. → **control 35**.
3. **The venue's own base rate was not printed beside any line.** The preferred side opposed it on 4 of 8 cards; those went 1 W / 3 L, against 3 W / 1 L for the four that agreed. `P-446` is the clearest: Wrigley's 2026 realised P(Over 7.5) is **60.3%** and the card used 47%, letting a wind-in note override a venue base rate it should only have modified. `P-449`: Coors P(≥12) is **47.3%** and the card used 40%. → **control 35**.
4. **The extras endpoint was never priced, and it settled two cards.** `P-443` regulation ended **4–4 — exactly the push at L = 8** — and extras made it an Over. `P-444` regulation produced **4 runs** at L = 8 and four extra frames made it an Over. Neither is a nine-inning run-environment miss. Control 22 names extras as a different rate environment; nothing required the probability to be printed. → **control 37**.
5. **Rank-#1 run-line work stopped at the starters** (`P-442`). Anthony Kay, the card's main worry, allowed two *unearned* runs in four innings. Sean Newcomb then gave up the decisive three-run homer in a four-run sixth. Controls 19–21 require score-state relief mapping; the card printed leverage *workload* and never a middle-relief ladder. → **control 36**.
6. **Winner label and ranked-row evidence diverged** (`P-450`, `P-448`). Arizona was given 54% on the same evidence base that made Miami +1.5 the strongest contract; Houston 55% on the evidence that made Kansas City +1.5 strongest. Both winner labels lost, both +1.5 rows won. → `G-L21`(3).


### Structural control additions


34. **MLB run-line margin identity (corrected 2026-09-17).** From the same joint final-score distribution, let w=P(the specified favourite wins) and r=P(that favourite wins by exactly one | that favourite wins). Then P(favourite −1.5)=w(1−r), and P(opponent +1.5)=P(opponent wins)+wr for a completed no-tie contract. Include draw/action mass explicitly in competitions that permit it. Condition on team identity, home/away and endpoint; the favourite does not become the realised winner after the fact. The pooled 2026 one-run frequencies 0.28/0.23 are historical context, not lower bounds on r or upper bounds on w. The universal 0.53/0.54 cap and automatic rank demotion are withdrawn. Winner-minus-loser season win% groups are not pregame features. Example w=.85,r=.23 gives .6545 coherently; this is a counterexample, not a forecast.


35. **Conditional total distribution and exact push mass (corrected 2026-09-17).** Derive Under/push/Over from one endpoint-valid count distribution. Show venue context with n and cutoff when available, partially pooled with league/team information; roughly one park-season is not a precise standalone matchup CDF. A conditional model may differ from a venue's realised proportions without a veto. State the relevant pitcher, lineup, weather and relief mechanisms and their uncertainty. The 12% push cap is withdrawn: Var(T)=E[Var(T|X)]+Var(E[T|X]); a park-only variance decomposition neither limits conditional variance nor bounds a PMF cell. Use held-out count calibration, residual dispersion and interval coverage. Do not lower a row probability without changing the underlying distribution.


    **Coupling:** show representative final scores against both a run line and a total, then obtain the joint queries from the complete joint distribution or report valid bounds. Representative scores alone are not probabilities.


36. **Score-state relief ladder before a run line is ranked #1.** A run line may be ranked #1 only after the card prints the **`starter contained → first damage in middle relief → 2+ run separation`** path as a weighted branch for **both** sides — even, and especially, when the starter matchup favours the row. The ladder names the likely first relief arm by score state, not just the closer and the setup man, and it distinguishes *workload* (who threw last night) from *role* (who pitches the sixth in a one-run game). Origin `P-442`: the card researched Cade Smith's five outs the previous night and the Guardians' leverage usage, then lost to Sean Newcomb in the sixth.


37. **Explicit regulation-to-completion endpoint (corrected 2026-09-17).** Choose and label one of two model routes. (A) A final-score model trained on completed full-game endpoints already includes home batting termination and extras in its label distribution; never add another extras allowance. (B) A state model supplies the joint home/away regulation distribution, home-ninth/walk-off termination and a rules-versioned extra-inning transition kernel for each tied state. Sum transition-weighted states to obtain the completed final-score distribution. A total mean/width cannot determine P(tie after nine).


    If the regulation score is tied and the total is exactly L, subsequent completion under an action-valid full-game contract necessarily adds at least one run: P(final total > L | that state, completion/action)=1. The old 60% conversion is withdrawn; 60.5% concerned at least two extra runs, a different event. Historical extras frequency 8.75%, added-run mean 2.88 and one-run final margin 68.5% remain cohort context only. No fixed 7.4/1.4 percentage-point run-line contributions or 0.84 underdog coverage follow from them. Derive team-specific winner and margin mass jointly. Handle capped/tied/void competitions separately. See MODEL_IMPLEMENTATION_RECIPES for executable state-kernel checks and the scoped A0/A1 pilot.


### Kill-path additions


| Kill path | Defeats | Origin |
|---|---|---|
| Starter contained; first damage arrives against middle relief and produces 2+ separation | Underdog `+1.5` ranked #1 on a starter-matchup thesis | `P-442` |
| Close low-scoring game → tie after nine → automatic-runner extras | Favourite `−1.5` **and** a same-card Under, simultaneously | `P-444` |
| Regulation lands exactly on an integer total | Both sides may push only at the final contract endpoint; regulation alone does not settle an extras-inclusive contract | `P-443` |
| Favourite's separation branch is also the Over branch | A `−1.5` row ranked beside a same-card Under | `P-446`, `P-449` |
| Venue base rate opposed with no named mechanism | The preferred total side | `P-444`, `P-446`, `P-447` |


### `G-L24` in baseball — the identity is control 34, and the band now lives in the register


Control 34 above **is** the baseball instantiation of the cross-sport `G-L24` (`RULES_GENERAL.md` §16.13(e)). The cushion band `b_1` and every figure it depends on now live in **[`BASE_RATES_REGISTER.md`](BASE_RATES_REGISTER.md) §1–§3** as the single maintained copy; the values restated in control 34 carry their `n` and derivation date so a stale copy is self-evident. **Cite the register; do not re-derive a second copy here.** Refresh each season, and treat any figure cited more than one completed season after 2026-09-17(b) as `STALE` until recomputed.


## 2026-09-19 — recency/rebound evidence, debutant gate and the top-O/U review


Cross-sport: [`RECENCY_AND_REBOUND.md`](RECENCY_AND_REBOUND.md) control `R-1`; source controls `S-1` (social identity) and `S-2` (press conferences) in `SOURCES.md` §"2026-09-19"; enhanced-failure trigger in `METHOD.md` §7.


**`R-1` is derived on this sport.** MLB 2026, 4,594 team-games and 108 starters: after a 0-run game a team scores **0.102 runs below** its own leave-two-out mean (95% CI [−0.456, +0.251]); top-10 offences after ≤2 runs are **−0.126** and behave no differently from bottom-10; a starter's next-start ER after a ≥6-ER outing lands **−0.017** from his own average, and his strikeouts do **not** rise (−0.070). Lag-1 autocorrelation is +0.019 (team runs) and −0.037 (starter ER). Out-of-sample, the shorter the recency window the worse the forecast: last-1 RMSE **2.7677** against season-to-date **2.0177** and a flat league constant **1.9844**.


**Operational consequence for baseball cards.** A starter's recent poor run may revise his estimated rate only through a **named mechanism** in the disaggregated record — velocity or release-point change, IL stint, role or leash change, workload limit. Without one, use the longer-window rate and let the recent run widen the distribution. `P-443` (Molina, FIP 3.82/xERA 4.08 over a 5.24 ERA) and `P-449` (Ray, two poor September starts set aside) are the correct pattern and are now empirically supported. `P-453`'s Rank #1 rested on a **three-start** ER run — the third-worst predictor measured — and won; record it as directionally lucky, not as validation of three-start form.


**Debutant/service-time gate.** `statsapi.mlb.com/api/v1/people/{id}` exposes **`mlbDebutDate`**. Check it for every starting-lineup player once the order is posted, and record any player with under ~30 days of MLB service as `LOW_SERVICE_SAMPLE`: his projection is a prior, not a rate, and he widens the team-score marginal rather than shifting it. Verified case: **Josue De Paula batted sixth for the Dodgers in `P-455` having debuted six days earlier (2026-09-11)**, and no card flagged it.


**Line-up state.** Use `hydrate=lineups` and `game/{pk}/boxscore` (`battingOrder`, `bench`, `bullpen`) rather than the human-facing page, and apply the `NOT_YET_PUBLISHED` vs `RETRIEVAL_MISS` distinction in `SOURCES.md` §"2026-09-19". The boxscore route supplies precisely the bench/bullpen field that has been capping Rank-#1 margin rows.


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — market-independent totals/line addendum


**Source priority:** MLB/league official game feeds, Baseball Savant/Statcast, official club transactions/lineups; NPB/KBO official league sources for those competitions; government weather/verified venue state. Betting/fantasy sources are prohibited.


For totals/run lines, build one joint home/away run distribution before seeing the supplied threshold in the modeling stage. Prefer partially pooled team offence/opponent prevention, starter skill/workload, bullpen availability, lineup/handedness, park, weather and rest/travel. Short recent scores cannot directly shift the centre; use measurable process/state changes. Query totals, team totals, winner and margin from the same distribution.




<!-- ALL-SPORTS-AUDIT-LIVE-RULE-CLEANUP-2026-09-21-CR3 -->
## 2026-09-21 — all-sports audit live-rule cleanup — CR-2026.09.21-3


This section is the current prospective override for audit-derived ranking logic in this sport. Earlier dated examples remain historical evidence, but any incompatible active instruction is superseded.


- **Retained sport package:** PA/BF exposure; starter hook distribution; named bullpen chain; park/defence; base-out and HR sequencing; home-ninth entitlement; extra-inning state; debut/small-sample mixture.
- **Withdrawn here:** second-highest/median or second-lowest/median pseudo-tail construction; path-count/category shortcuts as ranking rules; universal 40–60% top-slot bands; normalized-distance ordering; any one-result rebound/hangover/“due” rule; and any implication that a cushion determines the outright winner.
- **Current construction:** build one coherent sport-native joint outcome distribution/branch mixture, freeze it before supplied lines are queried, then derive exact target marginals and dependencies from that object. When a fitted/calibrated numerical distribution does not exist, a probability may be printed only as an `UNVALIDATED_SUBJECTIVE` output of the card's own complete, reproducible, declared distribution (METHOD §5). A number that cannot be reproduced from the printed distribution is invented precision and is not permitted. No subjective number carries a performance, calibration or value claim. *(Wording corrected 2026-09-25: the earlier "keep probabilities unquantified" contradicted METHOD §5; 2026-09-23 read-only audit item 5.)*


<!-- CONSOLIDATED-MINI-LOG-IMPORT-2026-09-23 -->
## 2026-09-23 settlement learning — `P-489` (NPB, 22 Sep game 24) and `P-491` (NPB); `TMP-20260923-NPB-CHU-DB-G25` and `P-493` carried live

Full records: [`PREDICTION_LOG_COMBINED_5.md` §"2026-09-23(c)"](PREDICTION_LOG_COMBINED_5.md). Learning-only. **No coefficient, cap or ordinal bar is added** (`L-087`).

| Card | Rank #1 | Result | Top O/U | Centre → actual | Verdict |
|---|---|---|---|---|---|
| `P-489` (START_CROSSED) | Under 6.5 (~0.62) — **L** | DeNA 7–3 | Under — **L** (`TOP_OU_REVIEW`) | 5.3 → 10 | Result-wrong / process-wrong in part |
| `P-491` (PREGAME) | Orix +1.5 (0.676) — **W** | Orix 1–0 | Under 7.0 — **W** | 7.19 → 1 | Result-right / process-right |

### What went right (keep it)

- **`P-491` is the reference NPB construction.**
  - Team centres came from partially pooled team R/G × opponent run prevention × a starter adjustment, applied once.
  - One per-inning simulation generated winner, margin, total and joint probabilities.
  - The override forms were honest: override 3 named the BB-B4 separation mass (0.32) rather than excluding it; override 8 attached the small-sample starter to the opponent's branch as width; override 9 re-solved `P(U ∧ +1.5)`.
  - Posted orders came from the NPB box pregame.
  - **Use this order of operations as the default baseball template.** It is a construction standard, not a fitted model.
- **R-1 held in both cards.** Kuri's three-start walk spike (P-491) and DeNA's worked bullpen (P-489) were treated as width, not direction; Kuri walked two, and DeNA's pen threw four scoreless innings.
- **Weather as a termination branch, not an automatic Under** (P-489, 45–52% shower risk; control 18). This was correct.

### What went wrong, linked to earlier lessons

1. **Control 26 was not executed (P-489).**
   - Each starter's quality entered three times: season ERA, L5 ERA and v-opponent ERA. The no-DH effect was added on top.
   - No team R/G or RA/G baseline was printed; DeNA 3.9 and Chunichi 3.4 R/G sum to about 7.3.
   - The centre (5.3) sat about 2 runs below the teams' own scoring with no adjustment chain.
   - Illustrative pregame-only arithmetic anchored on team rates gives about 6.0–6.3, which would have put Under 6.5 below the ML (0.60).
   - **M3/M15.** This is the same class as P-348, P-351 and P-356.
2. **The §8.5 kill-path row "one ordinary cluster crossing a low line — Under 5.5/6.5 at 0.56+" (origin P-361, NPB) recurred** in the same league and contract family: Under 6.5 at 0.62, lost to a 3-run 1st (after an error) and a 3-run 4th.
3. **ERA-anchored centres omit unearned runs.** 3 of 10 runs were unearned (Muller 7 R / 4 ER). → **TESTING `O-NPB-ERA-CENTRE`** (`LEARNING_REGISTER.md` L-20260923-03). When a run projection is built from ERA, add back the unearned-run share and print the reconciliation with team R/G and RA/G before an Under can rank #1. This is disclosure and arithmetic; it is not promoted to the §8.7 checklist until a third case and a prospective check exist.
4. **BB-P2 PARTIAL with a full-game total at #1 (P-489)** — `G14.2` / M19 again. The NPB box posts スタメン about an hour before first pitch (the P-491 lane). Tsutsugo, listed in the card's "Sep 21 core", did not start.
5. **`C-RUN-CENTRE-BIAS` (NPB leg):** P-489 +4.7 and P-491 −6.19. The signs conflict, so **no directional tilt** is supported; consistent construction is the lesson.

### Source notes (this pass)

- **NPB box raw HTML** (`npb.jp/scores/YYYY/MMDD/<home>-<away>-NN/box.html`) parses cleanly with curl plus a tag-strip: state (試合開始前 / 試合中 N回表 / 試合終了), start/end/attendance, per-batter results and per-pitcher pitch counts and BF. P-491's "reliever lines not reliably extracted" was a summarising-fetch artefact (M20).
- **Sports Navi schedule page** (`baseball.yahoo.co.jp/npb/schedule/?date=YYYY-MM-DD`) gives final state plus W/L/S for the whole slate: settlement lineage 2.
- **Kyodo wire** ("D7―3中（22日）") and **Nikkan staff reports** via Yahoo! News: settlement lineage 3.
- **Mynavi "プロ野球試合結果" pages are AI-generated. Exclude them.**

### Carried live (not settled; no learning drawn)

- `TMP-20260923-NPB-CHU-DB-G25`: the 23 Sep game 25. It was formerly mis-appended to P-489 as "R1"; see `O-ID-DATE-STARTER-MATCH` in `EXTERNAL_LOGGING_WORKFLOW.md`.
- `P-493` (KBO).
- Both are in the P-495-onward mini log.

<!-- CONSOLIDATED-MINI-LOG-IMPORT-2026-09-24 -->
<!-- AUDIT-2026-09-24F -->
## 2026-09-24 settlement learning — P-500, P-501, P-502, P-506 (MLB), P-493, P-507 (KBO) and TMP-20260923-NPB-CHU-DB-G25 (NPB), corrected 2026-09-24(f)

**Full record:** `PREDICTION_LOG_COMBINED_5.md` §"2026-09-24(e)" (the peer settlement, subject to its audit banner) and §"2026-09-24(f)" (the verification audit). This is learning-only.

**What changed.** The peer version of this section (`cb95acd`) mis-stated three Rank-1 contracts and two top-O/U results, and promoted two rules that are withdrawn below. The table is now copied from the issued Field 4 tables (`C-SUMMARY-FROM-CARD`). The process lines come from statsapi, the KBO scoreboard and the NPB box.

| Card | League | Rank #1 (p) | Final (verified) | Top O/U (rank) | Process note (verified) |
|---|---|---|---|---|---|
| TMP-G25 | NPB | Chunichi +1.5 **W** | DeNA 4–3 **F/12** (3–3 after 9) | Under 7.5 (#3) **W** (7) | The card named the tie/one-run branch. R1/R2 (DeNA ML) are a `COVERING_PAIR` |
| P-493 | KBO | Doosan +1.5 (0.582) **W** | Doosan 3–2, walk-off in the 9th | Over 7.5 (#2) **L** (5) | KIA's three Asian Games bats were disclosed on the card but not priced into the 8.68 centre |
| P-500 | MLB | Nationals +1.5 (0.587) **W** | WSH 4–2 | Over 7.5 (#3) **L** (6) | **Wind 14 mph in from LF** (the card said "out"); card DET order 3/9 correct. R1/R2 (DET ML) are a `COVERING_PAIR` |
| P-501 | MLB (DH G1) | Over 7.5 (0.662) **L** | BAL 4–2 | Over 7.5 (#1) **L** | **Lineups stale** (BAL 2/9, TOR 3/9 named starters played); overcast, 63 °F, wind in from CF (the card said 73 °F, out) |
| P-502 | MLB | White Sox +1.5 (0.700) **W** | KC 5–4 | Over 8.5 (#3) **W** (9) | Opener Hudson 0.1 IP, 4 R; Fedde 2.2 scoreless. R1/R2 (KC +1.5) are a `COVERING_PAIR` |
| P-506 | MLB | Astros +1.5 (0.685) **W** | SEA 6–5 F/10 | Under 7.5 (#3) **L** (8 after 9) | A 7-run 3rd inning (Pecko 2.2 IP; Kirby 5.0 IP, 4 ER). Honest coin flip (0.506). R1/R2 are a `COVERING_PAIR` |
| P-507 | KBO | KT ML (0.637) **W** | KT 3–2 | Under 9.5 (#2) **W** (5) | W Daniel, S Kim Jeong-woon, L Song Myung-gi |

### Withdrawn (not operative)

**`MLB-DOUBLEHEADER-G1-TOTAL-DEFLATION` — REJECTED (L-20260924-F05).**
- It came from one game.
- 2026 statsapi finals over 9 innings: doubleheader G1 n=23, mean 7.78, P(total ≤ 7) **0.435** (95% CI 0.23–0.64). G2 n=23, mean 7.91. Non-doubleheader games n=2,328, mean 8.98, P(≤ 7) **0.427**.
- G1 and G2 are both low relative to the league, which points to a makeup-game or season-timing confound rather than a G1 effect.
- P-501 was overcast, which refutes the "afternoon shadows" mechanism. The claimed "57.3% G1 Under base rate" is unsourced.
- The base rate is recorded in `BASE_RATES_REGISTER.md`.

**"Dual run-line (+1.5/+1.5) arbitrage" — REJECTED (L-20260924-F09).**
- MLB has no ties, so opposite +1.5 rows cover every outcome. At least one wins every game, and both win in a one-run game: 27.6% of 2026 finals (n=2,374).
- Two such "sweeps" in one batch (P-502, P-506) have a joint chance of about 0.28² ≈ 0.08 and say nothing about skill.
- Measurement rule: `RULES_GENERAL.md` §16.13(b) item 4 / §"2026-09-24(f)"(d), **`COVERING_PAIR`**.

### Controls added (retrieval and integrity only; no coefficient)

**B-1. Official MLB lineup at freeze (M19; `C-LINEUP-DIFF`).**
- A baseball card that prints a batting order prints the statsapi `battingOrder` (`/game/{pk}/boxscore`, or `schedule?hydrate=lineups`) with its fetch time. It never prints a remembered, previewed or "reported" order.
- If the order is not published at freeze, the state is `LINEUPS_NOT_YET_PUBLISHED @ time`. If it is published but was not fetched, the state is `RETRIEVAL_MISS`, and no full-game total or run line may be ranked #1 (G14.2).
- Evidence: P-500 (DET 3/9) and P-501 (BAL 2/9, TOR 3/9; Santander's "44 HR" is a 2024 figure).

**B-2. Gamefeed weather at freeze (L-20260924-F11).**
- A baseball total at #1 or as the top O/U prints the statsapi `gameData.weather` block (condition, temperature, field-relative wind, e.g. "14 mph, In From LF") retrieved at freeze. Otherwise it prints `WEATHER_NOT_RETRIEVED`. A generic city forecast does not qualify.
- This extends the existing weather game-window rule.
- Evidence: in P-500 and P-501 the card's wind was "out" and the official record says "in"; both were losing top Overs.

**B-3. `C-RUN-CENTRE-BIAS`, accrual only.**
- Residuals (actual − centre): P-493 −3.68, P-500 −2.40, P-501 −3.82, P-502 −0.50, P-506 +2.99 (regulation −0.01), P-507 −4.59. The mean is −2.0; 5 of 6 are below the centre.
- This is prospective relative to the 2026-09-12 finding (mean −1.58, 9 of 12 below).
- **No coefficient and no Under tilt, per the manifest.** Two of the three losing Overs also had lineup or wind retrieval defects, so B-1 and B-2 come first.

**B-4. Opener caution (observation only).**
- P-502's CWS opener (Hudson, 3.03 ERA) gave up 4 runs in 0.1 IP. The card had retrieved the opener-then-bulk plan correctly.
- An opener's first inning is a short-exposure, high-variance branch: width, not direction.

<!-- RESEARCH-2026-09-25 -->
## 2026-09-25(b) — freeze receipts, all-park references, first five innings and width (research pass)

**Status.** A retrieval control and reference rates (`C-PROMOTION-RECEIPT`: `PROMOTED_PROCESS` / `REFERENCE`). No coefficient. Sources: `BASE_RATES_REGISTER.md` §7.5 (statsapi, 2,373 nine-inning Finals through 24 Sep) and `RULES_GENERAL.md` §"2026-09-25(b)"(c).

**B-5. Freeze and settlement receipts (M19, M25, M30).**
- **At freeze,** run `python receipts.py pregame mlb <gamePk>`. It prints, from the live gamefeed with UTC and AEST times:
  - probable pitchers;
  - gamefeed weather (condition, temperature, field-relative wind);
  - the official batting orders;
  - umpires;
  - the feed state.
- **Before publication,** it prints `LINEUPS_NOT_YET_PUBLISHED` or `WEATHER_NOT_YET_PUBLISHED`. Those states are printed on the card as they are:
  - a projected lineup is never labelled confirmed;
  - a city forecast never replaces the gamefeed wind.
- **Re-run within 60 minutes of first pitch** when a card is frozen earlier.
- **At settlement,** `python receipts.py settle mlb <gamePk> --card-away "…" --card-home "…" --card-sp-away X --card-sp-home Y` prints:
  - the final and linescore;
  - the **regulation (9-inning) score when extras were played**, which is what settles a regulation-only contract;
  - decisions and box weather/wind;
  - the `C-LINEUP-DIFF` lines.
- **Replay check.** It reproduces two settled records: P-500 (wind "14 mph, In From LF") and P-506 (4–4 after 9; SEA won 6–5 in the 10th).

**B-6. All 30 parks are derived.** Every MLB total card prints its venue row from §7.5: mean, P(total ≤ 7), P(total ≥ 10). The 16 Sep eight-park table is superseded. Examples:

| Venue | Mean | P(≤ 7) |
|---|---:|---:|
| Sutter Health Park | 11.41 | 0.225 |
| Coors Field | 11.12 | 0.225 |
| Nationals Park | 10.83 | 0.231 |
| T-Mobile Park | 7.78 | 0.494 |
| Petco Park | 7.78 | 0.500 |

Each park mean has an SE of about 0.4–0.6 runs. The row is a disclosure anchor, not a tiebreaker.

**B-7. First five innings.**
- Mean 5.00, SD 3.29.
- P(F5 ≤ 4) = 0.499; P(tied after five) = **0.154**.
- The first five carry 55.9% of runs.
- An F5 row prints these. An F5 moneyline or −0.5 row carries the tie mass explicitly.

**B-8. Width benchmark (`C-WIDTH-BENCHMARK`).**
- Around a season-to-date team predictor, the total residual SD is **4.50** against a raw SD of 4.51: team rates explain almost none of the game-total variance (RECENCY §2).
- A total width below **3.8** (0.85 × 4.5) names what justifies it: both starters' run-prevention estimates, bullpen availability, gamefeed weather.
- In the 2026-09-24 cohort, P-506 (3.83) was at the threshold and P-500 (3.97) above it.
