# Rugby league / NRL analysis rules


> **2026-09-12 operational correction:** The dated section at the end of this file and RULES_GENERAL section 16.9 control over conflicting older probability, coupling and source claims.


> **`METHOD.md` is now the primary mandatory read (v4.0 comprehensive overhaul, 2026-09-06).** This file remains the full sport-specific reference: its `SFA-<SPORT>` algorithm and competition-rules section (`§9`/`§10`/`§11`) are consulted in full when forecasting this sport; `METHOD.md` states the cross-sport process once.


<!-- THREE-SOURCE-TIME-GATE-2026-09-19-CR4 -->
> **Current cross-sport authority — MDS-2026.09.19-v4.3 / CR-2026.09.21-3:** this sport module inherits the reconciled all-sports source, timing, settlement and distribution-construction controls. Historical issued cards retain their own revision.


Status: **ACTIVE**
Effective: **2026-09-06 (v4.0 comprehensive overhaul — see METHOD.md and archive/audit_documents_implemented_2026-09-25/FRAMEWORK_AND_GAME_LOG_OVERHAUL_REVIEW_2026-09-06.md)**
Method version: **MDS-2026.09.06-v4.0**
Applies with RULES_GENERAL.md, MODEL_AND_DATA_SPEC.md, ALGORITHM_PORTFOLIO_AND_EVALUATION.md, and NUMERICAL_TRAINING_SPEC.md.
Executable algorithm: **SFA-RUGBY-LEAGUE (§8) — instantiates GFA-2 in RULES_GENERAL.md §11**
Numerical training specification: **NTS-2026.09.02-v0.3 — design only; no rugby-league model is fit**
Sport and competition rules reference: **§9 (added 2026-09-04)** — the laws of rugby league and the NRL Telstra Premiership competition rules (2026 season: 17 teams, 27 rounds, golden point, finals system, interchange/18th-man rules, captain's challenge, the Bunker). Reference material for identity, state and settlement; it does not change `SFA-RUGBY-LEAGUE`.
Evidence density: **MODERATE** (added 2026-09-06, `L-099`, external blindspot audit `B-13`) — more settled cards than the sparse codes (rugby union, ice hockey, American football) but fewer than baseball/soccer/cricket. Directional/magnitude claims in this file should still be checked against the underlying case count before being treated as strongly evidenced.


This file covers rugby league. Rugby union and rugby sevens are different codes and are governed by `RULES_RUGBY_UNION.md`; their data and scoring populations must not be pooled with rugby league.


<!-- LIVE-RULES-PAGE-2026-09-26 -->
## 0. Live rules — one page (consolidated 2026-09-26)

**Status.** This page consolidates everything in this file that is live on 2026-09-26: the numbered controls, SFA-RUGBY-LEAGUE and the dated sections through 2026-09-25(e). It is a derived index. If it disagrees with the section it cites, the cited section governs and this page is corrected in the same pass. **Reading gate (C-READING-GATE, 2026-09-26):** read this page in full for every rugby-league card, then open each cited section the card relies on (and §9 for the competition). Everything below §0 is the full reference and its history.

**Track record.** Rugby codes combined: 12 decisions won 58.3% at a stated 0.567 (too few to judge). NFL, AFL and NRL together went 12 W / 20 L at Rank 1/2, the worst group. NRL and NRLW are separate populations. League and union are never pooled (control 8).

### 0.1 Blocking preconditions (§8.1)
| Gate | Requirement | If it fails |
|---|---|---|
| RL-P1 laws | Law variations, interchange, six-again/set restarts, regulation, golden point and draw terms | Stop |
| RL-P2 team list | Official list, final match-day reduction and late mail, starting 13, bench and the confirmed spine (fullback, five-eighth, halfback, hooker), from the raw NRL match centre or club page with publication time (G-L13). After late mail, `NOT_RETRIEVED` is `RETRIEVAL_MISS` | Spine and role mixtures; dependent rows capped |
| RL-P3 goal kicker | Primary goal kicker and replacement (control 5) | Required before any total or margin row |
| RL-P4 conditions | Venue, surface and match-window weather with a named mechanism | Wet weather is bidirectional (control 4) |

### 0.2 Building the score distribution
1. **Anchor.** Sides and totals both anchor on the population (`BASELINE_P`).
   - **Sides (corrected 2026-09-26(e), validity repair):** TB-1's 2026 point gain (0.240 v 0.253) has a 95% interval that crosses 0 (−0.0294, +0.0044), so `TEAM_BASELINE_P` is printed with `TB1_NO_RESOLUTION:margin` and is not the anchor.
   - **Totals have no TB-1 resolution either** (its RMSE is worse than the league mean): anchor on the population row (2026: mean 47.8, SD 13.9).
2. **Scoring components, not points** (September 6). Points = 4×tries + 2×conversions + 2×penalty goals + 1×field goals, with conversions = tries × goal-kicking %. A debutant kicker's own reserve-grade kicking percentage enters the conversion term (L-075).
3. **Branches.** Before any Under or underdog cushion is ranked, write one favourite-only scoring path (RL-B2) and one low-total separation path (RL-B3) with their mechanisms (override 1; controls 13, 14). The second half carries score, possession, field position, bench and fatigue forward (control 15). Close-game winners need the terminal-event branch (RL-B5, control 16; override 3). Blowouts are possession-native (control 12).
4. **Regimes.** A changed spine rebuilds set organisation, kicking and edge attack (control 1). A current defensive collapse or spine return against season averages is a baseline/current-regime mixture (control 11).
5. **Small samples.** Completion, goal-kicking and try rates over three or four rounds print their standard error before any signed adjustment (G-L11).
6. **Width.** TB-1 residual widths: total 13.9, margin 19.9 (2026).
7. **One score object → total and margin queried separately** (override 2). Possession imbalance is bidirectional (control 2, override 4).

### 0.3 Row rules
- **Cushions (C-PLUS-CUSHION).** The TB-1 underdog covered +1.5 at 0.41–0.43, +2.5 at 0.44–0.49, +4.5 at 0.51, +6.5 at 0.55–0.57, +8.5 at 0.62, +12.5 at 0.65–0.67 (2025–26). Print the favourite's 7+ and 13+ margin families beside any cushion (G-L12). Stated more than 0.05 above the rate without a receipted mechanism, RM-1 flips it.
- **Over + underdog cushion.** When RL-B3 carries material mass, print P(R1 ∧ R2) and its sign (P-397). These are distinct targets with a shared driver (G-L15).
- **Totals departing from the population by about 0.10 or more** need a receipted mechanism, such as a confirmed wet-track forecast for the match window (P-515).
- **Recent cover rates, points averages and old H2H** are diagnostic only (control 3, override 5).

### 0.4 Reference rows (NRL, all completed games; `BASE_RATES_REGISTER.md` §7.7)
| Row | 2025 (n = 216) | 2026 (n = 213) |
|---|---:|---:|
| Home win | 0.551 | 0.545 |
| Total mean (SD) | 46.1 (14.0) | 47.8 (13.9) |
| Total 10th / 50th / 90th percentile | 29 / 44 / 64 | 30 / 48 / 66 |
| Home margin; margin SD | +3.8; 18.7 | +0.0; 20.7 |
| P(\|m\| ≤ 2); P(\|m\| ≤ 6) | 0.13; 0.34 | 0.15; 0.29 |

NRLW has no population reference yet (`NOT_YET_DERIVED`).

### 0.5 Ranking and settlement
- Rank by RM-1 q; its cushion term applies to NRL +k.5 rows.
- Settle from ESPN `rugby-league/3` (regular season is season type 1, finals type 2; `linescores` carry half-time then full-time) plus two further lineages. nrl.com statistics are admissible only when fetched and pasted with a URL.
- Record sin bins, send-offs and HIA removals with the minute and score.

### 0.6 Withdrawn or not operative in rugby league
`C-NRL-SPINE-PEDIGREE-TOTAL-FLOOR` (rejected: one game, invented statistic). `C-FINALS-BYE-RUST` is TESTING only (`T-NRL-BYE-RUST`, 30 games), with no ranking effect. Pseudo-tails, path-count categories, 40–60% bands and normalised-edge ordering.

### Numerical shadow model (2026-09-26(c); never a card input)

`python tools/sport_models.py shadow --league nrl …` (`C-SPORT-SHADOW`). A1 is ridge ratings with key-number weights. **Validated on 2026 (2026-09-26(e)):**
- results: not significant (−0.0273, +0.0003);
- margin RPS: better;
- totals: no better than the population.

TB-1's result gain was not significant either, so the NRL reference is the population. Record it after the freeze and before the start; it is never printed, ranked or cited on a card, and a promotion needs its 150-row review and your instruction (`RULES_GENERAL.md` §"2026-09-26" (e), (k); `research/sport_models_2026-09-26/README.md`).

**Predictability and cards (2026-09-26(e)).** The model's favourite reached 0.70 in 19% of games and won 68.3%. The 0.70–0.80 band won 67% at 0.737, so it is over-confident. On the cards' own NRL contracts (4, from 2 cards): card 0.271, A1 0.203. That is too few to read (`research/predictability_2026-09-26/README.md`; `BASE_RATES_REGISTER.md` §7.8).

### 0.7 Control index (full text in §4 and the dated sections)
1 spine is a regime · 2 possession imbalance drives dependence · 3 cover rates diagnostic · 4 wet weather bidirectional · 5 goal-kicker state · 6 sin-bin/send-off tail · 7 winner ≠ handicap · 8 league and union never pooled · 9 motivation conditional · 10 no calibration claim · 11 defensive regime and spine-return mixture · 12 blowouts are possession-native · 13 a total can clear through one team · 14 low total ≠ close margin · 15 halftime doesn't freeze separation · 16 close-game winner needs terminal events.


## 1. Identity and contract


Resolve NRL, NRLW, Super League, reserve-grade, international, or another league competition; current laws/interchange rules; venue; regulation/golden-point/draw terms; team/player/phase statistic; and exact settlement provider. Do not call a Super League fixture NRL.


## 2. High-value inputs


### Participants and roles


- Confirm the official team list, final match-day reduction/release, starting 13, bench, late changes, and current competition interchange/activation rules.
- Identify the spine: fullback, five-eighth, halfback, hooker; primary goal kicker; playmakers and replacement tree.
- Estimate minutes, interchange, carries, tackles, kicking role, goal-kicking share, and position changes.
- Translate absences into set organisation, field position, ruck speed, edge defence, and conversion.


### Possession and field position


Use opponent-adjusted:


- possessions/sets and set starts;
- completion and error rates;
- metres/set and post-contact metres;
- play-the-ball/ruck speed where defined;
- line breaks, tackle breaks, offloads and kick returns;
- repeat sets, penalties, six-again, field position and goal-line entries;
- tries, try location, goal conversion, and defensive conversion;
- tackle load and interchange fatigue.


Raw points and cover history do not substitute for possession and field position.


### Context


Record rest, travel, turnaround, venue, match-window weather, surface, ladder/finals incentives, referee only with current relevant data, and verified tactical changes. Wet conditions can reduce handling but also create short fields and fatigue; no automatic Under.


## 3. Model


Exposure units are possessions/sets, set starts, field position, carries/tackles, line-break opportunities, tries, and conversions. Estimate territory and try opportunities first, then finishing and goal-kicking. Use a joint score/margin distribution with sin-bin, intercept/short-field, fatigue, and golden-point tails.


Derive winner, handicap, total, phase, and player contracts from the same distribution.


For numerical training, compare empirical/simple set-and-try baselines with a sets → field position → goal-line entry → try → conversion A2 simulator. It samples completion/errors, repeat sets, penalties/six-again, ruck/fatigue, line breaks, sin-bin/send-off, kicker and golden-point states while preserving both teams' possession dependence. Direct score or boosted-distribution models are challengers only after discrete-support, scoring-combination, population and calibration checks. Elo is contextual strength, not the scoring engine. Every contract integrates the same joint score distribution. All candidates remain unfit and unvalidated.


## 4. Structural controls


1. **Spine is a regime variable.** Rebuild set organisation, kicking, and edge attack for a changed spine.
2. **Possession imbalance drives dependence.** It can raise favourite margin while suppressing the underdog contribution; total direction remains scenario-specific.
3. **Recent cover rates are diagnostic.** Current participants, set distance, line breaks, and field position control.
4. **Wet weather is bidirectional.** Trace handling errors, kicking, short fields, ruck speed, and goal-kicking.
5. **Goal-kicker state matters.** Tries and conversions are dependent; record the current kicker and replacement.
6. **Sin-bin/send-off is an explicit tail.** Rebuild remaining possessions when it occurs live.
7. **Winner and handicap differ.** Model separation, narrow result, and golden-point branches.
8. **League and union cannot be pooled.** Laws, scoring, possession and settlement differ.
9. **Motivation is conditional.** Tie it to selections, interchange, tempo or risk.
10. **No current calibration claim.** P-039 is one NRL event and cannot establish model performance.
11. **Current defensive regime and spine return require a mixture.** When a recent conceded-points/line-break/field-position collapse or a key spine return conflicts with season averages and old H2H, freeze baseline and current-regime branches with named mechanisms. Weather and historical close scores cannot silently suppress a credible separation tail.
12. **Blowout branch is possession-native.** Stress repeated short fields, missed-tackle/line-break clusters, spine-led set control and conversion quality before ranking a broad Under or underdog cushion. One realised blowout creates a candidate, not an automatic coefficient.
13. **A total can clear through one team.** For every broad Under, test a favourite-only scoring branch in which the underdog remains suppressed but errors, short fields, repeat sets, line breaks and conversions let the favourite carry the total over the line.
14. **Low total does not imply close margin.** A territorial/completion/defensive-control state can produce a multi-score favourite cover while the match stays Under. Margin and total must be queried separately from the joint score tree.
15. **Halftime does not freeze full-time separation.** Carry score, possession/set starts, field position, completion/error state, spine function, bench/interchange usage, defensive workload and conditions into the second-half branch. A competitive first half can become a favourite cover through opponent suppression and fatigue without creating a high total.
16. **Close-game winner needs terminal-event sensitivity.** In a competitive low-total branch, separately model final-five-minute field position, interchange/conditioning, spine/kicker availability, repeat sets, penalties, sin-bin/injury states and conversion/kick outcomes. A sound Under or broad cushion does not identify which side wins the last scoring sequence.


## 5. Live state


Store score, clock/half, possession/set and tackle, field position, repeat-set/six-again, penalties/errors, line breaks, sin bins/send-offs, injuries, interchanges, kicker, and current ruck/territory. Recompute remaining sets and field-position distribution.


## 6. Sources and settlement


- NRL official team lists, late mail, match centres, judiciary and [game/statistics resources](https://www.nrl.com/operations/the-game/) control NRL.
- Official competition sources control Super League, NRLW, internationals, and other leagues.
- Government weather services and venue reports control conditions.


Settle from the official final and named provider, preserving regulation/golden-point and exact player-stat definitions.


## 7. Upcoming-game research sequence


1. Freeze rugby-league competition/laws, regulation/golden-point/draw terms, player/stat provider and candidate slate.
2. Retrieve official team lists, injury/casualty status, reductions/late mail, starting 13, bench, spine and goal kicker. Refresh at the current competition's final-update deadline and immediately before kickoff.
3. Model player minutes/interchange, sets and set starts, field position/tackle state, completion/errors, ruck/fatigue, goal-line entry, try location, conversion, penalties/six-again, sin-bin and golden-point tails.
4. Possession dominance can increase margin while reducing the opponent contribution; total direction must be scenario-derived.
5. Before ranking an Under or underdog cushion, calculate one explicit favourite-only blowout path and one low-total separation path; record which mechanisms and score families make each credible.
6. Derive joint score, winner, total and handicap from the same score object. Player props use position, minutes, carries/tackles/kicks or goal-kicking exposure and exact provider definitions.


Official competition sources own current teams/state/rules. Historical archives are cross-check/research lanes and cannot override late mail or enter H0 before field-level approval.


## 8. SFA-RUGBY-LEAGUE — sport forecast algorithm


Algorithm ID: `SFA-RUGBY-LEAGUE`. Effective **2026-09-02**. Instantiates `GFA-2` (RULES_GENERAL.md §11) with rugby-league content. Process composition only; no fitted weight, scenario weight or published probability is introduced. NRL, NRLW, Super League, internationals and lower grades are separate populations, and no rugby-union or sevens data enters any step.


### 8.1 Blocking preconditions


| Precondition | Requirement | Failure output |
|---|---|---|
| `RL-P1` competition and laws | Competition, law variations, interchange and activation rules, six-again and set-restart conventions, regulation, golden-point and draw terms | `GATE-TARGET` failure; do not proceed |
| `RL-P2` team list | Official team list, final match-day reduction and late mail, starting 13, bench, and the confirmed spine — fullback, five-eighth, halfback, hooker — re-handshaken at the competition's final update deadline and again at G31 | Spine and role mixtures; dependent rows cap at `FORCED RANK` / `MEDIUM-LOW` |
| `RL-P3` goal kicker | Primary goal kicker and replacement | Required before any total or margin row, because tries and conversions are dependent |
| `RL-P4` conditions | Venue, surface and match-window weather with a named mechanism | Wet weather is bidirectional; no automatic Under |


### 8.2 Exposure chain


| Step | Output |
|---|---|
| `RL-S1` | Minutes and interchange by player, with the spine replacement tree and positional changes |
| `RL-S2` | Possession: sets and set starts for both sides, from completion rate, errors, penalties and six-again |
| `RL-S3` | Field position: metres and post-contact metres per set, kick metres, kick return, and resulting set-start position |
| `RL-S4` | Goal-line entry rate from `RL-S2` and `RL-S3`, including repeat sets and short fields |
| `RL-S5` | Try conversion from entries: line breaks, tackle breaks, offloads, edge defence, missed-tackle clusters and try location |
| `RL-S6` | Goal-kicking from the current kicker, plus penalty-goal and field-goal decisions by score state |
| `RL-S7` | Fatigue state: tackle load, interchange usage, ruck speed and second-half decay for both sides |
| `RL-S8` | One joint score and margin object with sin-bin, send-off, intercept, short-field and golden-point tails |


Raw points and cover history never substitute for `RL-S2`–`RL-S5`.


### 8.3 Mandatory branch set


| Branch | Content |
|---|---|
| `RL-B1` | Central possession with central entry conversion for both sides |
| `RL-B2` | Favourite-only scoring branch: the underdog stays suppressed while errors, short fields, repeat sets, line breaks and conversions carry the total up through one side |
| `RL-B3` | Low-total separation branch: territorial, completion and defensive control producing a multi-score cover inside an Under |
| `RL-B4` | Second-half separation: the complete halftime state — score, set starts, field position, completion, spine function, bench usage, defensive workload and conditions — carried forward |
| `RL-B5` | Terminal-sequence branch: final-five-minute field position, interchange and conditioning, spine and kicker availability, repeat sets, penalties and conversion outcomes |
| `RL-B6` | Sin-bin or send-off state, with the remaining possession rebuild for the exact man-down duration |
| `RL-B7` | Wet-weather state, with handling errors, kicking, short fields, ruck speed and goal-kicking each signed separately |
| `RL-B8` | Golden point or draw treatment under the exact competition and operator terms |


### 8.4 Contract derivation map


| Contract | Queried from | Extra condition the mechanism must predict |
|---|---|---|
| Total | Sum marginal | The component budget, including the `RL-B2` favourite-only path |
| Line and handicap | Margin marginal | Separation, narrow result and golden-point branches stated separately |
| Winner | Margin sign, including terminal sequence | A sound Under or broad cushion does not identify the last scoring sequence |
| Team total | Team marginal | That side's own entries and conversion, not the match tempo |
| Half or phase | The segment's own possession and field-position state | Halftime never freezes full-time separation |
| Player props | Position, minutes, carries, tackles, kicks or goal-kicking exposure | The exact provider definition |


### 8.5 Kill-path library


| Kill path | Defeats | Evidence origin |
|---|---|---|
| A favourite carrying the total alone while the underdog is suppressed | A broad Under justified by two-team scoring expectations | §4 control 13, C-PL6-RL-FAVOURITE-ONLY-TOTAL |
| Territorial and completion control producing a multi-score cover | The framing that a low total protects an underdog cushion | §4 control 14 |
| A competitive first half becoming a second-half cover through fatigue and suppression | A close-margin row anchored to the halftime state | §4 control 15, C-PL8-RL-H2-SEPARATION |
| Two late tries flipping the winner inside an otherwise correct low-total tree | An outright winner derived from the total and cushion | §4 control 16, C-PL9-RL-TERMINAL-WINNER |
| A changed spine rebuilding set organisation, kicking and edge attack | Season averages and old head-to-head retained at high evidence | §4 controls 1 and 11 |
| Repeated short fields and missed-tackle clusters | An Under ranked before a possession-native blowout branch is stressed | §4 control 12 |
| Wet conditions creating short fields and fatigue as well as handling errors | A one-sign wet-weather Under | §4 control 4 |
| A sin-bin rebuilding remaining possession | A margin or total row with no man-down branch | §4 control 6 |


### 8.6 Sport ordering overrides


1. Before any Under or underdog cushion is ranked, write one explicit `RL-B2` favourite-only path and one `RL-B3` low-total separation path, and record which mechanisms make each credible.
2. Total and margin are separate queries against the same score object. Neither raises the other's `states` count.
3. A close-margin or winner row requires the `RL-B5` terminal branch before it can exceed `LEAN`.
4. Possession imbalance is bidirectional: it can raise the favourite's margin while suppressing the opponent's contribution, so it may not be counted only in the direction that supports the selected total.
5. Recent cover rates, points averages and old head-to-head are `E — diagnostic only`. The single logged NRL event cannot calibrate anything.


### 8.7 Pre-issue checklist


1. `RL-P1`–`RL-P4` status printed, including late mail and the confirmed spine and kicker.
2. Competition and venue scoring baseline stated before any line.
3. Set, field-position and goal-line-entry chain written before any points figure.
4. All eight `RL-B*` branches represented; component budget solved at the supplied total.
5. Favourite-only and low-total-separation paths both written explicitly.
6. Kill-path rows selected from §8.5 and reconciled against the issued order.
7. Golden-point and draw treatment stated for every winner, total and margin row.
8. Team lists, late changes, kicker and conditions refreshed at G31 before the view is appended.
9. Recency block complete per §8.8: L5/L10/L15/L20 for both sides and for head-to-head, continuity count stated, trend verdict per metric, unique-event de-duplication done.
10. Environment block complete per §8.9: Match-window rain and wind recorded, with the bidirectional wet-weather audit run rather than an assumed Under.
11. `REFERENCE_BASE_RATE`, exact threshold, population and denominator recorded for every supplied row per §8.10 as a descriptive diagnostic only; no reference-band, trend or slot-frequency adjustment may move an ordinal (G23.1).
12. Extra-condition support audit (G24) recorded for every handicap, team-total and cushion row; no retrospective contract-family penalty is applied.
13. Separation budget (G20.1) solved for every margin, handicap and cushion row by half, with the closing twenty minutes, interchange state and late-try/penalty-goal paths held separately.
14. Rank-1 implied-target interval (G25.1) stated in the unit of every other supplied line, each remaining row classified `COHERENT`/`PARTIAL_OVERLAP`/`DISJOINT`, and every aggregate budget re-solved conditional on the Rank-1 state.
15. Winner-and-cushion reconciliation (G30.1) whenever Rank #1 is an underdog cushion, with the outright-win and narrow-loss branch ordering stated. Example separation kill path for this sport: a late try plus conversion.
16. Deficit attribution (G14.1) recorded for every weak, absent, returning or small-sample participant: which side's distribution moved and through which exposure step.


### 8.8 Recency, head-to-head and trend windows


Implements `GFA-2` step G13.1 (RULES_GENERAL.md §11.3B) and runs at that point in the algorithm, not at the end. Retrieval of L5/L10/L15/L20 for both sides and for the head-to-head series is mandatory; a window that does not exist is recorded with its true count and a missingness code.


Populate one windowed table per side with these metrics, and one head-to-head table:


| Window metric | Content |
|---|---|
| Possession | Sets and set starts, completion rate and error count, opponent-adjusted |
| Field position | Metres and post-contact metres per set, kick metres and average set start |
| Goal-line access | Goal-line entries, repeat sets and line breaks, for and against |
| Defence | Missed tackles and points conceded, held separately from points scored |
| Goal kicking | The current kicker's own last 5/10/15/20 games: attempts, success and range |


**Head-to-head continuity.** Continuity means the same spine and the same kicker. A head-to-head record across a halfback or hooker change fails continuity, which is the exact failure recorded when season averages and close head-to-head history outranked a current defensive collapse.


**Descriptive recency windows (G13.1; revised 2026-09-17).** Retrieve L5/L10/L15/L20 and continuity-qualified H2H with unique-event counts. These windows overlap. Monotonicity and dispersion among their averages are not a statistical trend/noise test. Report direction descriptively; estimate recency decay and opponent/regime effects using time-ordered validation. See SCORING_AND_VALIDATION section 5.


**De-duplication.** The windows overlap by construction and share matches with the head-to-head and venue series. Shrink from unique underlying events under G9; never treat L5, L10, L15 and L20 as four confirmations.


### 8.9 Environment and conditions


Implements `GFA-2` step G15.1 (RULES_GENERAL.md §11.3C). Venue classification for this sport is normally **OUTDOOR**.


| Field | Use in this sport |
|---|---|
| Hourly precipitation | Handling errors, short fields, ruck speed and goal kicking all move, and not in the same direction; run the G22 audit |
| Wind speed and direction | Kicking game, drop-outs and goal kicking, resolved against ground orientation |
| Surface state | Official venue source |
| Temperature and humidity | Interchange usage and second-half fatigue under `RL-B4` |


Failure to obtain the match-window forecast for an outdoor or open-roof event yields `WEATHER_NOT_AVAILABLE`, widened total and margin distributions, and a `LEAN` cap on every weather-dependent row. No factor above carries an automatic total direction.


### 8.10 Base-rate anchors and derived stat lanes


**Anchoring (G12.1).** Anchor totals on the competition scoring environment and margins on the competition margin distribution. A cushion is `CONJUNCT` and does not start level with a match total.


**Derived and low-salience fields that are available and routinely skipped:**


| Field | Note |
|---|---|
| Six-again and set-restart counts | Possession-native and often the mechanism behind a blowout |
| Interchange usage and tackle load | Feeds the fatigue state at `RL-S7` |
| Turnaround length and travel | Entered through fatigue and rotation |


## 9. Sport and competition rules reference


Added 2026-09-04; last reviewed 2026-09-04. Standing reference for the laws of rugby league and the competition rules of the NRL Telstra Premiership — the only rugby-league competition in the prediction logs. Supports `RL-P` identity and §6 settlement; introduces no rate, weight or ordering rule.


**Maintenance (RULES_GENERAL.md §3, `G2`).** Before the first card of a new NRL season, the pre-season Challenge, or the first finals card, re-verify the golden-point rule (regular season vs finals), the interchange/18th-man rules, the captain's-challenge and Bunker rules, the two-point field-goal rule, the team count and the finals bracket against nrl.com, and update this section **before** issuing the card — the NRL has changed the six-again, interchange, field-goal and finals rules within the last few seasons and adds an expansion team for 2028. The first time another rugby-league competition is forecast (Super League, State of Origin, an international, the NSW/Q Cup), document its full rules here first.


### 9.1 The laws of rugby league


**Field and teams.** A rectangular field ~100 m (try line to try line) × 68 m, with **in-goal areas** at each end. **13 players a side** on the field, **4 interchange** players on the bench.


**Scoring.**
- **Try = 4 points:** grounding the ball in the opponent's in-goal.
- **Conversion = 2 points:** a kick at goal from in line with where the try was scored.
- **Penalty goal = 2 points:** a kick at goal from a penalty.
- **Field goal (drop goal) = 1 point** — **or 2 points if kicked from 40 m or more** (an NRL rule since 2021).


**Possession — the six-tackle set.** The team in possession gets **six tackles** to advance and score. After the sixth tackle without a score, possession hands over (usually via a kick on the fifth or sixth). A **"six again"** (set restart) is called for a ruck infringement by the defence — the tackle count resets to zero with **no penalty and no stoppage** (introduced 2020; a major driver of fatigue-based blowouts, `SFA-RUGBY-LEAGUE` §8, §8.10). The **play-the-ball** restarts play after each tackle; the defensive line must retreat **10 m**.


**Kicking.** A **40/20** kick (kicked from inside your own 40, bouncing into touch inside the opponent's 20) or **20/40** wins the kicking team the next set with the feed. A kick dead in-goal or into touch on the full from open play hands possession to the defending team.


**Match structure.** **Two 40-minute halves**, running clock (stopped only for the Bunker, serious injury and other referee interventions), ~10-minute half-time. Teams change ends at half-time.


**Officiating.** One on-field referee (the NRL trialled and dropped two referees), two touch judges, and the **Bunker** (a central video-review centre) for tries and foul play. **Captain's challenge:** each team has **one** challenge of a referee's ruling (knock-on, ball-strip, obstruction, etc.); it is **retained if successful**, lost if not.


**Interchange and player-safety rules.** **8 interchanges** per team per game from the 4-man bench. An **18th player** may be activated if a team loses players to failed Head Injury Assessments (HIA) or foul-play send-offs beyond a threshold — a concussion/foul-play safety valve, not a free extra rotation. **Send-off (red card)** = off for the game, no replacement; **sin bin (yellow)** = 10 minutes off, no replacement; a "professional foul" in-goal can draw a sin bin plus a penalty try.


### 9.2 NRL Telstra Premiership — 2026


**Structure.** **17 clubs** (10 NSW, 4 Queensland, plus Melbourne, Canberra, and the New Zealand Warriors). **27 rounds**, each club with byes (an uneven fixture, not a full double round-robin). **Magic Round** (Round 11) stages the entire round at one venue. The **State of Origin** period (three interstate representative matches, ~May–July) removes many of the best players from their clubs for those weeks — a large, predictable availability shock (`SFA-RUGBY-LEAGUE` participant handling).


**Ladder.** Win **4**, draw **2**, loss **0**. Separated by: (1) competition points, (2) **points differential**, (3) percentage, (4) tries scored, then further tiebreakers. No bonus points.


**Golden point (extra time).**
- **Regular season:** if level after 80 minutes, **two 5-minute halves** of golden point — **first score of any kind wins** (a field goal, try or penalty goal). If still level after the 10 minutes, the match is a **draw**.
- **Finals:** the same two 5-minute halves, then, if still level, **unlimited golden point until a score** — **finals cannot be drawn**.


**Finals system (top 8).** Same structure as the AFL final-eight:
- **Week 1:** Qualifying Finals **1 v 4**, **2 v 3** (winners get a week off and a home Preliminary Final; losers get a second life); Elimination Finals **5 v 8**, **6 v 7** (losers eliminated).
- **Week 2 (Semi-Finals):** Qualifying-Final losers host Elimination-Final winners.
- **Week 3 (Preliminary Finals):** Qualifying-Final winners host Semi-Final winners.
- **Week 4:** the **Grand Final** (Accor Stadium, Sydney — 4 October 2026), a fixed neutral-ish venue.
Higher seed hosts every final before the Grand Final.


**Pre-season.** The **NRL Pre-season Challenge** (trial matches, February) — heavily rotated, experimental lineups; treat as friendlies, not form.


### 9.3 Settlement (NRL)


- Full-game line and total settle at the **end of 80 minutes for regular-season matches** — most operators settle the head-to-head and line **excluding golden point** (so a regular-season draw is a live outcome and pushes the line / settles the moneyline as "tie" or dead-heat), but **"including golden point"** markets exist — freeze which one the card is using.
- For **finals**, there is no draw; freeze whether the market endpoint is "regulation (80 min)" or "including golden point / eventual winner."
- The **2-point field goal** matters for margin and total settlement — a late long-range one-pointer-that-is-two can flip a handicap on a key number.
- Try-scorer, first-try, and player run/tackle-metre props settle on the official NRL statistics provider; freeze the provider.


### 9.4 Identity checklist (rugby league)


Resolve before any rate work: confirm the competition is the **NRL** (not the NSW Cup, Q Cup, Super League, or an international) and the **season's rule set** (six-again, captain's challenge, 18th-man, 2-point field goal are all current NRL); the **stage** (pre-season trial / regular season / Origin-affected round / finals bracket / Grand Final) and therefore whether a **draw is possible** and how **golden point** is handled; representative-window availability; and the operator's golden-point settlement rule for the market endpoint.


## September 5 settlement learning — prospective SFA amendment


P-280 reinforces L-038/L-042 and adds the operational L-069 check at the final team refresh. Map expected spine **playing minutes and entry time**, not just the printed jersey position. Arrow's ceremonial start did not remove Walker for an ordinary opening phase. Remove a withdrawn player from every exposure chain before using the remaining middle to justify a cushion. The timestamped NRL preview placed Collins' withdrawal before the frozen cutoff.


At `SFA` possession/field-position and G20.1 separation steps, run both depleted-side attack suppression and opponent repeated-opportunity scoring. A weak attack can coexist with an Over driven mostly by its opponent. Use scoring chronology to distinguish the threshold-crossing mechanism from later sin bins: the P-280 total had crossed before the paired 72nd-minute bins. Actual 50–20 is a case for the library, not a new blowout prior. Candidate C-P293-NRL-ROLE remains at zero prospective completions.




Full evidence and frozen-card comparisons: [September 5 audit](archive/audit_documents_implemented_2026-09-25/COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md).


## September 5(b) settlement learning — P-294–P-305 second continuation


Three NRL/NRLW cards settled this pass (`P-294`, `P-295`, `P-301`); the total (Under) was ranked #1 in all three and lost all three, while the spread/moneyline row ranked #2 won twice and lost once. Full driver analysis is in `PREDICTION_LOG_COMBINED_2.md`'s 2026-09-05(b) section; the load-bearing findings are recorded here.


**`P-295` (North Queensland Cowboys vs Canberra Raiders) — L-075.** Canberra debutant halfback Coby Black scored a premiership-record 26 points (2 tries, 9/9 goals) in a 50-30 Raiders win. The card's own research had already retrieved Black's NSW Cup rate stats (77 goals at 77% conversion, 17 try assists, 362.8 average kicking metres across 19 appearances) and explicitly called him "capable rather than replacement-level" — but `Cowboys -5.5` was still ranked #2 above `Raiders +5.5` at #3. **New rule:** when a reserve-grade or debutant player's own retrieved rate production materially exceeds a "replacement level" framing, write one explicit sentence stating the ranking consequence of that production before finalising the order — do not let the number sit in the availability paragraph while the rank proceeds as if a generic replacement were starting.


**`P-294` (Newcastle Knights (W) vs Canterbury-Bankstown Bulldogs (W)) and `P-297`-adjacent reasoning.** Newcastle won 56-22 (total 78, comfortably clearing 48.5) by carrying almost the entire total alone against a Bulldogs side whose recent defensive collapse (30, 48, 44 conceded in the three prior games) was **already the card's own primary evidence for ranking the Under #1** — the same underlying fact that should have flagged the favourite-only-blowout branch (`RL-B2`, kill-path library §8.5) as the more central state, not a tail risk to the Under. Confirms and extends `C-PL6-RL-FAVOURITE-ONLY-TOTAL` with a fourth data point.


**`P-301` (Cronulla Sharks vs Melbourne Storm).** Melbourne won by a last-second try, 24-20 — a final margin of 4, well inside the 8.5 line, and the exact "competitive game" branch (`RL-B5`/terminal-sequence branch) the card itself had named as live given Cronulla's strong record at Ocean Protect Stadium (won 6 of previous 7 there) and Melbourne's poor recent record at the venue (no win since 2017). The venue/recent-record evidence was recorded but again did not move the spread off Rank #1.


**Sport ordering override addition (§8.6):** before ranking a favourite's spread/handicap above a total in a two-sided NRL/NRLW slate, write one explicit sentence stating whether the favourite's own recently-recalled or in-form scoring capacity is already the evidence being used to justify the Under — if so, the same evidence supports a favourite-only-blowout branch at least as strongly as it supports the total, and the ranking order between them must be reconciled, not defaulted to "Under first."


**Kill-path library addition (§8.5):**


| Kill path | Defeats | Evidence origin |
|---|---|---|
| A reserve-grade or debutant player's own retrieved per-appearance production (goal-kicking %, assist rate, kicking/running metres) exceeds a "replacement level" framing used elsewhere in the same card | A favourite's spread/handicap ranked above the underdog's cushion on an unstated assumption of replacement-level opposition personnel | `P-295`; L-075 |


Full evidence: [PREDICTION_LOG_COMBINED_2.md, 2026-09-05(b) section](PREDICTION_LOG_COMBINED_2.md#component-import--p-294p-305-second-continuation--2026-09-05b).


## September 6 settlement learning — the tries-plus-conversions tail and the second-half window


`P-294` and `P-295` were the two clearest `TAIL_EXPOSED` failures in the whole `P-294`–`P-305` cohort, and both were rugby league.


| Card | Line | Actual | Why the tail budget would have flagged it |
|---|---|---|---|
| `P-294` Newcastle Knights (W) v Canterbury (W) | `Under 48.5` (rank #1) | **78** (56-22) | The Knights' own upper L10 output plus the Bulldogs' median already exceeds 48.5 before any variance is added. The complementary `Knights -15.5` at rank #2 **won** — the card's own margin read and its total read were pointing at incompatible totals, which `G25.1` should have caught and `G20.2` now makes arithmetic |
| `P-295` North Queensland v Canberra | `Under 56.5` (rank #1) | **80** (50-30 Raiders) | A genuine upset, but the Raiders were 30-12 up at half-time; a second-half exposure term held at the upper decile clears 56.5 on its own |


**Required from now on, `SFA-RUGBY-LEAGUE`:** the tail budget is computed on **tries, conversions and penalty/field goals as separate scoring components**, converted explicitly to points: `points = 4×tries + 2×conversions + 2×penalty_goals + 1×field_goals`, where `conversions = tries × goal-kicking%`. **Correction, 2026-09-06(d):** the original wording ("tries × kicking percentage") omitted the try points themselves and the penalty/field-goal terms — the formula above is the actual points total, not a proxy for it. Hold each side's try count at its second-highest L10 value and its goal-kicking percentage at its own L10 rate — not a generic 75%. Then hold the **second-half window separately**, because the fatigue and interchange regime after the 55th minute has its own scoring rate; `G20.1` already requires this split for margins, and it now applies to totals.


`P-295` is also the origin case for `L-075` (a debutant's own reserve-grade production must be carried into the ranking weight, not only the risk paragraph). Coby Black's 26-point debut record is exactly a goal-kicking-rate observation: the tail budget and `L-075` reinforce each other, because a debutant kicker with a strong NSW Cup goal-kicking percentage raises the conversion term directly.


### Kill-path library addition (§8.5)


| Kill path | Defeats | Evidence origin |
|---|---|---|
| **Conversion-rate compounding** — an ordinary try count converts at an upper-decile rate and clears an `Under` that the try count alone would not | A full-game `Under` budgeted on tries without a separate goal-kicking term | `P-294` (78 against `Under 48.5`), `P-295` (`L-075`) |
| **Half-time blowout state** — a 30-12 half-time score makes the second half a different scoring environment in both directions (garbage-time tries, or a shut-down) | A total budgeted from a single whole-game rate | `P-295` |
| **Own-margin/own-total incoherence** — the card's ranked margin row implies a total incompatible with its own ranked total row | Any slate carrying both, unreconciled | `P-294`: `Knights -15.5` won while `Under 48.5` lost — `G25.1` plus `G20.2` |




### Cross-sport gates instantiated here (v3.7)


| Gate | Sport-native instantiation |
|---|---|
| `G10.2` settlement-source pre-registration | NRL/NRLW finals settle from the ABC News Score Centre lane promoted on 2026-09-05(b); `nrl.com` remains behind a login wall for automated fetches. Name the exact Score Centre record at freeze. |
| `G14.2` coaching / bench / rotation record | Record the head coach, the named interchange bench (four in the NRL) and any 18th-man/concussion provision from §9, plus the rotation signal for a dead rubber or a finals-eve rest. Official club 24h cuts, 1h final team lists, or accredited rugby league beat reporting verified under Control `S-1 Rev 2` qualify as `PROJECTED_BEAT_VERIFIED`, satisfy `G14.2`, and do not block Rank #1. |
| `G20.2` distributional tail audit | Derive tail and boundary mass from the **same frozen rugby-league joint score distribution**, including final team/role/bench, possession and field position, set starts, ruck/play-the-ball, kicking/discipline, venue/weather and golden-point endpoint where applicable. Historical order-statistic stress sums are superseded as active gates. |
| `G21.1` exact target geometry | Map every supplied target to its exact settlement event and derive WIN/PUSH/LOSS from the same frozen sport-native PMF/CDF or coherent branch mixture. Historical path-count/category labels have no mandatory ordinal effect. |
| `G26.1` no universal separation floor | Reference rates and `rank_gap` are descriptive only. **No 40–60% or other pooled probability band can disqualify Rank #1.** Rank from exact marginal likelihood plus robustness/evidence uncertainty. |


**Pre-issue checklist additions (this sport):** settlement endpoint named per row; coaching/bench/rotation record for both sides with missingness codes; tail-budget sums printed against every total line; path-geometry class and `N` printed for every total and phase-total row; separation-floor result stated for Rank #1.


Full narrative and evidence: [`archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md`](archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md). Controlling gate text: [`RULES_GENERAL.md` §13](RULES_GENERAL.md).


## September 5 implementation after freeze confirmation


**ACTIVE REQUIRED PROCESS — MDS-2026.09.05-v3.6 / L-068–L-072.** Refresh final changes and expected actual roles/minutes immediately before issue, including ceremonial starting positions. Calculate favourite margin and opponent scoring jointly with repeat-set/territory exposure so a cushion and Under do not inherit the same unsupported resistance assumption.


At final delivery, record the preferred total direction for each exact target, the strongest evidenced failure path for ranks #1 and #2, and whether both can win under the stated joint scenario. Rank by supported marginal likelihood; do not promote an opposite pick solely to manufacture one O/U win. At settlement, keep all issued wins/losses, including defective reasoning, in the applicable historical scorecard and review failed #1/#2 and preferred totals.


[Eligibility policy](PERFORMANCE_ELIGIBILITY_POLICY.md): non-live history is user-confirmed frozen pre-game; explicit live-issued views stay separate. These process repairs are implemented now. Numerical weights and predictive-lift claims need a later frozen comparison; historical origin games do not supply those completions.


## 2026-09-06(f) — settlement and retrospective addendum


P-294 favourite scoring alone cleared the total; P-295 replacement-grade production was already knowable while the early sin-bin was not; P-301 a winning favourite did not cover the required margin. Reconcile two-team native-unit points and named replacement roles with the printed central/counter branches. Magnitudes and rank consequences remain candidates under METHOD v4. Preserve NRLW as a distinct competition in descriptive evaluation.


Full frozen ranks, actual drivers, knowability and smallest fixes: [PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md). Reinforcement only; METHOD v4.0 remains controlling and no new predictive weighting is promoted.


## 2026-09-09 — cross-sport controls instantiated here (`G-L1`, `G-L2`, `G-L7`, `G-L8`)


No NRL/NRLW card was issued in the `P-333`–`P-344` cohort. The four cross-sport requirements adopted from it (`RULES_GENERAL.md` §§16.5(a)–(d), full evidence in `PREDICTION_LOG_COMBINED_3.md` §"2026-09-09") apply to this sport from the next card — and they bear directly on `P-301`, where a winning favourite did not cover the required margin. All four are **disclosure/retrieval requirements — no fitted weight, no ordinal bar** (`L-087`).


| Cross-sport control | NRL / rugby league instantiation |
|---|---|
| **`G-L1` §16.5(a)** — enumerate outcome-state families with explicit mass | Enumerate the **margin families** in native units (favourite by 25+ / 13–24 / 7–12 / 1–6 / draw / underdog win) and the **total families** in points, each with an explicit mass summing to 1. Because scoring is quantised in 4s and 6s plus 2-point conversions and 1-point field goals, state families as **try-count × conversion-rate** combinations rather than a smooth corridor. Every current-evidence §8.5 kill path — including a **sin-bin or send-off**, and the **late consolation try** that decides so many handicap rows — appears as a weighted branch. Print a representative Rank-#1 final score as a try/goal breakdown and check it against the line, the total and any team-total row. |
| **`G-L2` — declared uncertainty model** | State the prior and scenario probabilities. Symmetric uncertainty around an unchanged prior affects width; hierarchical shrinkage or asymmetric scenarios may change both mean and variance. Regenerate all dependent probabilities; unsupported directional adjustments remain prohibited. SCORING_AND_VALIDATION section 5 controls. |
| **`G-L7` §16.5(c)** — aggregate-to-disaggregate retrieval | Do not let a season points-per-game figure or a "last N" summary carry directional weight while the **round-by-round log** is available. Print the per-round record for the decision-relevant window — points for/against, tries, completion rate and the decision-driving players' **minutes and involvements per match** — and state whether a run is front-loaded, back-loaded or uniform. For a returning player, print the **reserve-grade / return-to-play minutes ladder**, the analogue of the rehab pitch-count ladder that decided `P-335`. Quantify **every player in the spine and every top-three try-scorer on both sides**; a bare name in a "leaders include…" phrase is `AGGREGATE_ONLY` and caps the dependent margin/total rows. |
| **`G-L8` — distribution coherence** | Derive each total/spread probability from the exact joint PMF/CDF and settlement endpoint, with push mass. Absolute normalised distance does not order probabilities across different distributions. No missing width or realised result justifies an invented probability. |


## 2026-09-11 settlement learning — `P-363` (NRLW) — a positive model


**`P-363` — Sydney Roosters (W) 42–12 Canterbury-Bankstown Bulldogs (W), NRLW Round 11** ([`PREDICTION_LOG_COMBINED_3.md` §"2026-09-11"](PREDICTION_LOG_COMBINED_3.md)). Frozen card: R1 Bulldogs +40.5 (0.61) **W**; R2 Under 59.5 (0.55) **W**; R3 Over 59.5 **L**; R4 Roosters −40.5 **L**; winner Roosters (~97%) correct. **Top two both won; card mean Brier 0.1773 — the best card of the `P-358`–`P-371` block.** NRLW is a separate population from NRL (`SFA-RUGBY-LEAGUE` preamble) and remains `EXPLORATORY`.


**Why it worked.** The NRL late mail confirmed both 1–17s with no late changes (spines and goal-kickers identified); the `RL-B1`–`RL-B8` branch set named both the favourite-only-scoring Over path and the low-total-separation path; and the card anchored the handicap on a verifiable base rate — the Roosters had cleared a 40.5-point margin in only 2 of 10 wins. Canterbury led at half-time and scored 12; the Roosters' second-half surge (six tries in 16 minutes) still stopped at +30.


**Gaps (presentational):** no numeric width, no family masses and no head coaches on the card. The branch set did the work a family table would have done; print the masses next time (`RULES_GENERAL.md` §16.8).


| Cross-sport control (2026-09-11) | Rugby-league instantiation |
|---|---|
| `G-L9` §16.5(e) | Itemise the complement across the `RL-B` branches — favourite-only blowout (`RL-B2`), low-total separation (`RL-B3`), second-half separation (`RL-B4`), sin-bin/send-off (`RL-B6`). |
| `G-L10` §16.5(f) | Underdog +handicap and Under are **positively** coupled through a competitive underdog that also slows the game — but anti-coupled through `RL-B3` (favourite suppresses the underdog and wins big in a low-scoring game). Print the sign from the branch masses. |
| `G-L11` §16.5(g) | Completion rate, goal-kicking percentage and try-scoring rates over three or four rounds are small samples; print their standard error before a signed adjustment. |
| §16.8 | Late mail is published before kick-off; `NOT_RETRIEVED` after it is a `RETRIEVAL_MISS`. |




## 2026-09-12 algorithm corrections and retrospective integration


Use the joint team-points and game-phase branches for handicap/total dependence. P-363 correctly captured a competitive first half; the actual sin bin at 48 minutes and Baxter HIA are post-issue disruptions, not pregame predictive credits. Preserve them as explanatory match facts with chronology and examine the original ordinary separation branch separately. Confirm both starting 13s, interchange/reserves, goal-kickers and coaches from dated late mail. Trial/attempt rates require real denominators and repeated-team/game dependence disclosure.


For every supplied row, use exact target probabilities from a coherent joint distribution; handle push/void/censoring explicitly, avoid overlapping adverse-state counts, and report JOINT_UNQUANTIFIED with bounds if the dependence is not specified. Separate issued-time participant capture, later recovered evidence, source accuracy by field, observed mechanism, and unverified causal interpretation. Keep one preferred O/U direction per distinct target and report the top-two denominator honestly. Shared correction and methodology sources (`audit_2026-09-12/rule_corrections.md`, not present in this repository). All current log observations remain learning-only and not performance-eligible.




## 2026-09-15(b) settlement learning — `P-373`–`P-423` import


Learning-only; disclosure/process changes only — no coefficient or ordinal bar (`L-087`). Evidence and tables: [`PREDICTION_LOG_COMBINED_3.md` §"2026-09-15(b)"](PREDICTION_LOG_COMBINED_3.md). Cross-sport rule: `RULES_GENERAL.md` §16.10 (`G-L12` margin centre/width; fixture identity; official-record derivative settlement).


**Cards:** P-380 (NRLW), P-386 (Souths v Knights), P-394 (NRLW), P-397 (Sharks v Cowboys). Finals re-verified at ESPN (`rugby-league/3`) for P-386/P-397.


- **Positive:** P-380 realised the printed low-total favourite-separation branch (Raiders 22–10: −6.5 and Under 46.5 both won); P-386 Knights +8.5 won outright 20–10; P-394 Cowboys +10.5 won in a high-total close game. Rugby-league underdog cushions went 3 / 0 at Rank #1 — the one sport where the cross-sport pattern did not appear.
- **Negative:** P-397 — Over 48.5 (Rank #1) and Cowboys +7.5 (Rank #2) both lost to the low-total favourite-cover state (26–16) that branch `RL-B3` had printed. Add P-397 as the worked example: when RL-B3 carries material mass, `P(R1 ∧ R2)` for an Over + underdog cushion must be printed (`G-L10`).
- **`G-L12` instantiation:** print the favourite's 7+ and 13+ margin families beside any cushion; finals intensity is width.


## 2026-09-16 — cross-sport controls instantiated here (`G-L13`, `G-L14`, `G-L15`, disruption facts)


No rugby-league card was settled this pass. Rules: `RULES_GENERAL.md` §16.11.
- **`G-L13`:** team lists and late mail come from the raw NRL match centre or club page, with its publication time; never from a summary.
- **`G-L14`:** a half-time or first-try row names its settling record (ESPN `rugby-league/3` line scores are verified for finals).
- **`G-L15`:** P-397's Over 48.5 and Cowboys +7.5 were **distinct targets** with a shared driver. Their joint loss is reported against `Σp − P(A ∧ B)`, not as "one O/U lost".
- **Disruption facts:** record sin bins, send-offs and HIA removals with the minute and the score. P-363's 48-minute sin bin is the model entry.


## 2026-09-17 — cross-sport controls instantiated here (`G-L17`–`G-L20`)


No rugby-league card in this import. **`G-L17`:** `P-397` (Over + underdog cushion, both lost to the low-total favourite-cover state) is the worked example — now print `P(¬R1 ∧ ¬R2)`, not only the joint win. **`G-L18`:** print each side's own points marginal before a match total. **`G-L19`:** NRL regular-season games can be drawn (golden point applies only where the competition's rules say so) — the winner family carries draw mass. **`G-L20`:** a current-season meeting that cleared the line gets explicit mass.


Evidence and cohort audit: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17"](PREDICTION_LOG_COMBINED_4.md); rules in `RULES_GENERAL.md` §16.12.


## 2026-09-17(b) — cross-sport controls instantiated here (`G-L21`–`G-L24`)


**G-L24 in NRL RUGBY:** derive the exact signed-margin distribution under the competition endpoint, including draw, key-value and push masses. Pooled league bands are uncertain references, not mandatory matchup probabilities or rank prohibitions. Missing pooled bands do not invalidate a complete conditional joint distribution. **`G-L21`:** the recurring NRL slate — favourite line, Under, favourite team total — is one thesis in three rows; print the joint failure mass. **`G-L22`:** forced pairs; report preferred sides and derive push mass at whole-number lines. **`G-L23`:** completion rate, errors, penalties and **sin bins and send-offs with the minute and score** are the process and disruption fields.


Evidence and cohort audit: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17(b)"](PREDICTION_LOG_COMBINED_4.md); rules in `RULES_GENERAL.md` §16.13; bands and base rates in [`BASE_RATES_REGISTER.md`](BASE_RATES_REGISTER.md).


## Current model implementation — 2026-09-17


Use METHOD v4.2's six-field object and SCORING_AND_VALIDATION for exact outcome/push scoring, event-level comparison, descriptive recency and declared hierarchical uncertainty. MODEL_IMPLEMENTATION_RECIPES supplies this sport's retained model scope and endpoint design. Forecast probabilities come from the joint model; pooled base rates are uncertain context, not universal limits. Numeric row caps disconnected from that model, absolute-distance probability ordering and retrospective tail reweighting are withdrawn. No fitted coefficient or predictive improvement is claimed. New cards freeze the method/control hash; existing cards keep their issued versions.


## 2026-09-19 — recency/rebound, social sources and the top-O/U review


`R-1` ([`RECENCY_AND_REBOUND.md`](RECENCY_AND_REBOUND.md)) applies: recent results revise an estimated **rate** through a named mechanism, never forecast a **deviation**. No rebound and no hangover adjustment is permitted in either direction. This sport's magnitudes are **`NOT_YET_DERIVED`** — the MLB figures are not transferable and must not be imported; derive them from this competition's own record before any recent-form weighting.


Source controls `S-1` (social identity: X and Reddit return no usable content; Bluesky sports handles failed identity verification 6/6) and `S-2` (press conferences are availability/role evidence, never a signed adjustment to a modelled rate) apply — `SOURCES.md` §"2026-09-19".


A loss **or push** on the card's highest-ranked over/under now triggers the same enhanced failure review as a Rank #1 loss (`METHOD.md` §7).


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — market-independent totals/line addendum


**Source priority:** NRL/competition official team lists, match centre, judiciary/availability, club releases and government weather. Betting/fantasy content is prohibited.


Totals and handicaps should arise from a joint scoring model using lineup/spine availability, possession/territory/completion and line-break/kicking process, interchange/bench state, venue/weather and rest. Do not convert recent wins/losses or the market line into an unexplained point adjustment.




<!-- ALL-SPORTS-AUDIT-LIVE-RULE-CLEANUP-2026-09-21-CR3 -->
## 2026-09-21 — all-sports audit live-rule cleanup — CR-2026.09.21-3


Current prospective override. Retain final team/role/bench, possession/field-position/set starts, ruck/play-the-ball, kicking/discipline, venue/weather and golden-point endpoint. Withdraw pseudo-tail order-statistic constructions, path-count ranking shortcuts, universal probability-band top-slot rules, normalized-distance ordering, symmetric widening from a one-sided absence without a named mechanism, and automatic rebound/response rules. Build one coherent rugby-league joint outcome distribution before querying targets.

<!-- RANK-MODEL-2026-09-25E -->
## 2026-09-25(e) — the first NRL population reference, the team baseline, P-515 and the ranking model

Controls: `RULES_GENERAL.md` §"2026-09-25(e)". Evidence: `research/team_baseline_2026-09-25e/README.md`; `BASE_RATES_REGISTER.md` §7.7.

### (a) Sources

1. **ESPN NRL scoreboard** `…/rugby-league/3/scoreboard?dates=YYYYMMDD`.
   - The NRL regular season is ESPN **season type 1**; finals are type 2.
   - `linescores` carry cumulative values: the half-time score, then the full-time score.
   - It is admitted as one settlement lineage and as the TB-1 lane (`--league nrl`). The NRL team-schedule endpoint returns HTTP 500, so the tool reads the scoreboard; the first run takes about 2 minutes, then it is cached.
2. **P-515 correction.** The settled log recorded the Preliminary Final as Roosters 36, Dolphins 14 (total 50). ESPN event 604843 gives **36–20** (half time 16–6; total 56).
   - The grades are unchanged: Under 45.5 lost; Roosters +2.5 won; Dolphins −2.5 lost.
   - The process "facts" in that retrospective (329 run metres, 14 errors) were unsourced and are struck (`C-SETTLEMENT-FROM-FEED`).
3. **The nrl.com match centre** returned no statistics through the proxy on 2026-09-25. Its figures are admissible only when fetched and pasted with a URL.

### (b) Reference rows (NRL 2025 / 2026, all completed games, n = 216 / 213)

| Row | 2025 | 2026 |
|---|---:|---:|
| Home win | 0.551 | 0.545 |
| Total mean (SD) | 46.1 (14.0) | 47.8 (13.9) |
| Total, 10th / 50th / 90th percentile | 29 / 44 / 64 | 30 / 48 / 66 |
| Home margin | +3.8 | +0.0 |
| Margin SD | 18.7 | 20.7 |
| P(\|m\| ≤ 2) | 0.13 | 0.15 |
| P(\|m\| ≤ 6) | 0.34 | 0.29 |
| TB-1 residual width, total / margin | 13.8 / 18.3 | 13.9 / 19.9 |

### (c) Reasoning

1. **TB-1 is the anchor for sides** (0.240 v 0.253). **Totals have no resolution:** TB-1's total RMSE is worse than the league mean. NRL totals therefore anchor on the population row: in 2026, 47.8 with SD 13.9.
   - P-515's Under 45.5 at 0.635 sat about 0.10 above that population, where P(total < 45.5) ≈ 0.43–0.48 (TB-1 gave 0.445). It rested on an unmeasured "bye rust / wet track" story. Under the departure ledger it now needs a receipted mechanism, such as a confirmed wet-track forecast for the match window.
2. **Early season.** TB-1 was worse than the base rate in the NRL's early rounds (0.284 v 0.271). Before Round 5, anchor on `BASELINE_P`.
3. **Cushions.** The TB-1 underdog covered:

   | Cushion | Cover rate (2025–26) |
   |---|---|
   | +1.5 | 0.41–0.43 |
   | +2.5 | 0.44–0.49 |
   | +4.5 | 0.51 |
   | +6.5 | 0.55–0.57 |
   | +8.5 | 0.62 |
   | +12.5 | 0.65–0.67 |

   `C-PLUS-CUSHION`, as amended, applies.
4. **Finals and byes.** `C-FINALS-BYE-RUST` is **TESTING, non-binding** (`T-NRL-BYE-RUST`): collect the first-half margins of NRL finals played after a bye, from the ESPN scoreboard, over at least 30 games. `C-NRL-SPINE-PEDIGREE-TOTAL-FLOOR` is **REJECTED** (one game, and an invented statistic).
