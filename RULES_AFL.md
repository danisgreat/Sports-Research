# Australian rules football analysis rules


> **2026-09-12 operational correction:** The dated section at the end of this file and RULES_GENERAL section 16.9 control over conflicting older probability, coupling and source claims.


> **`METHOD.md` is now the primary mandatory read (v4.0 comprehensive overhaul, 2026-09-06).** This file remains the full sport-specific reference: its `SFA-<SPORT>` algorithm and competition-rules section (`§9`/`§10`/`§11`) are consulted in full when forecasting this sport; `METHOD.md` states the cross-sport process once.


<!-- THREE-SOURCE-TIME-GATE-2026-09-19-CR4 -->
> **Current cross-sport authority — MDS-2026.09.19-v4.3 / CR-2026.09.21-3:** this sport module inherits the reconciled all-sports source, timing, settlement and distribution-construction controls. Historical issued cards retain their own revision.


Status: **ACTIVE**
Effective: **2026-09-06 (v4.0 comprehensive overhaul — see METHOD.md and archive/audit_documents_implemented_2026-09-25/FRAMEWORK_AND_GAME_LOG_OVERHAUL_REVIEW_2026-09-06.md)**
Method version: **MDS-2026.09.06-v4.0**
Applies with RULES_GENERAL.md, MODEL_AND_DATA_SPEC.md, ALGORITHM_PORTFOLIO_AND_EVALUATION.md, and NUMERICAL_TRAINING_SPEC.md.
Executable algorithm: **SFA-AFL (§8) — instantiates GFA-2 in RULES_GENERAL.md §11**
Numerical training specification: **NTS-2026.09.02-v0.3 — design only; no AFL model is fit**
Sport and competition rules reference: **§9 (added 2026-09-04)** — the laws of Australian football and the competition rules for the AFL (men's premiership + 2026 Wildcard finals system) and AFLW, including the 2026 rule changes, quarter/time-on structure, interchange caps, finals brackets and extra-time rules. Reference material for identity, state and settlement; it does not change `SFA-AFL`.


<!-- LIVE-RULES-PAGE-2026-09-26 -->
## 0. Live rules — one page (consolidated 2026-09-26)

**Status.** This page consolidates everything in this file that is live on 2026-09-26: the numbered controls, SFA-AFL and the dated sections through 2026-09-25(e). It is a derived index. If it disagrees with the section it cites, the cited section governs and this page is corrected in the same pass. **Reading gate (C-READING-GATE, 2026-09-26):** read this page in full for every AFL or AFLW card, then open each cited section the card relies on (and §9 for the competition's rules). Everything below §0 is the full reference and its history.

**AFL is `NO_DEMONSTRATED_SKILL` and over-confident.** 10 decisions won 30% at a stated 0.662 (gap −0.36, card-cluster interval −0.60 to −0.10). Underdog cushions went 0/3. NFL, AFL and NRL together went 12 W / 20 L at Rank 1/2, the worst group. The evidence grade is capped at LOW and the departure ledger is required. AFL men's and AFLW evidence are never pooled.

### 0.1 Blocking preconditions (§8.1)
| Gate | Requirement | If it fails |
|---|---|---|
| AF-P1 rules | Rules era, quarter length, interchange/substitute rules, draw and extra-time terms | Stop |
| AF-P2 selected teams | Official teams, late changes, substitute and material outs, re-handshaken after the final late-change window. Returning forwards get play/limited/withdrawn states until the warm-up check | Role mixtures; dependent rows capped |
| AF-P3 venue | Venue, dimensions, roof and ground orientation | Required before wind enters any branch |
| AF-P4 wind vector | Near-bounce wind speed and direction mapped to ground orientation and scoring ends, plus surface (control 14) | Totals and handicaps capped at LEAN; widen margin and total states (override 3) |

Match IDs are host-qualified: verify date and participants before reusing an AFL/club ID pairing (L-071).

### 0.2 Building the score distribution
1. **Anchor.** Sides and margins: `TEAM_BASELINE_P` from `tools/team_baseline.py --league afl` — the strongest resolution of any league (P(home win) Brier 0.202 v 0.249). **Totals have no TB-1 resolution**; anchor them on the 2026 population row. Finals print `TB1_FINALS_CONTEXT` and name the finals departures (venue, rest days, ground weather).
2. **Scoring shots × conversion, never points as one number** (September 6). Points = S × (1 + 5p), with S = goals + behinds and p = goals/S, per side. The shot chain runs territory → inside-50 → mark/shot → shot quality → conversion (control 1). Conversion persistence is estimated, not assumed (control 2). Near a line, show lower/central/upper conversion branches (control 12).
3. **Mismatches.** The dominant side's shots compound while the weaker side is already at its floor, so a one-sided game is more dangerous for an Under (September 6 item 3; P-292). A high-shot branch is mandatory for 180+ men's totals (control 9).
4. **Personnel.** Availability goes through role and time on ground into shots and conversion; no name-only bump (control 11). A personnel-loss discount is conditioned on the opponent's own roster quality (L-077, P-298).
5. **Conditions.** Wind is a quarter/end-switch variable (control 14). AFLW late territorial durability is separate from the total (control 15).
6. **Width.** TB-1 residual widths: total 29.1, margin 36.7 (2026).
7. **One score object → totals and margins queried separately** (override 1). A broad Under never supports an underdog cushion (control 13).

### 0.3 Row rules
- **Cushions (C-PLUS-CUSHION).** The TB-1 underdog covered +6.5 at 0.38–0.43, +12.5 at 0.48–0.51, +18.5 at 0.56–0.59 and +24.5 at 0.60–0.62 (2025–26). Stated more than 0.05 above that without a receipted mechanism on the favourite's side, RM-1 flips it.
- **Winner and handicap are different thresholds** (control 3); overlapping positive handicaps are mapped (control 4). Finals margins take their centre from the scoring-shot differential chain, not a shrink toward a close game (G-L12).
- **Hitouts are opportunity**, never a decisive term (control 8, override 4). Raw totals, Under/Over counts and cover history are diagnostic only (override 5).

### 0.4 Reference rows (AFL, n = 207 per season; `BASE_RATES_REGISTER.md` §7.7)
| Row | 2025 | 2026 |
|---|---:|---:|
| Home win / draw | 0.565 / 0.005 | 0.585 / 0.015 |
| Total mean (SD) | 168.6 (29.8) | 178.2 (29.1) |
| Total 10th / 50th / 90th percentile | 132 / 168 / 208 | 142 / 181 / 216 |
| Home margin; margin SD | +6.0; 42.5 | +7.1; 40.8 |
| P(\|m\| ≤ 12); P(\|m\| ≤ 24) | 0.30; 0.48 | 0.28; 0.47 |

AFLW has no population reference yet (`NOT_YET_DERIVED`).

### 0.5 Ranking and settlement
Rank by RM-1 q (its cushion term applies to AFL +k.5 rows). Settle from the AFL/AFLW official match centre with ESPN `australian-football/afl` as corroboration; record goals and behinds per side so the shot/conversion split is auditable.

### 0.6 Withdrawn in AFL — never apply
Points budgeted as one number; name-only personnel bumps; fixed conversion regression; pseudo-tails, path-count categories, 40–60% bands and normalised-edge ordering.

### Numerical shadow model (2026-09-26(c); never a card input)

`python tools/sport_models.py shadow --league afl …` (`C-SPORT-SHADOW`). A1 is ridge ratings with draws allowed. On 2021–2024 it beat the league baseline on results and margins, and TB-1 on results. It gave **no gain on totals**. At the total line TB-1 was ahead by 0.008, but the interval crosses 0. Record it after the freeze and before the start; it is never printed, ranked or cited on a card, and a promotion needs its 150-row review and your instruction (`RULES_GENERAL.md` §"2026-09-26" (e), (k); `research/sport_models_2026-09-26/README.md`).

**Predictability and cards (2026-09-26(e)).** AFL sides are the most predictable target in the repository. In 2026 the model's favourite reached 0.70 in **39%** of games and won **90.6%** of them (result Brier 0.183 against the population's 0.244). Totals are not predictable: 11% of games reach 0.70 at the league line, and those won 67%. On the cards' own AFL contracts (6, from 3 cards) the model was no better than the cards (A1 0.315, card 0.348, population 0.338). A STRONG Rank 1 is realistic on an AFL side, not on a total (`research/predictability_2026-09-26/README.md`; `BASE_RATES_REGISTER.md` §7.8).

### 0.7 Control index (full text in §4 and the dated sections)
1 decompose the shot chain · 2 conversion persistence estimated · 3 winner ≠ handicap · 4 overlapping positive handicaps · 5 live Under needs observed suppression · 6 large Q4 cushion needs remaining-possession analysis · 7 venue and competition matter · 8 hitouts are opportunity · 9 high totals need a high-shot branch · 10 motivation is conditional · 11 availability-to-conversion handshake · 12 conversion sensitivity near the line · 13 volume and margin separate · 14 ground-level wind is a phase variable · 15 Q4 territorial durability.


## 1. Identity and contract


Resolve AFL, AFLW, VFL, SANFL, WAFL, or another competition; season/rules era; round/finals state; venue; home/away/neutral; named teams and late changes; regulation/draw/overtime terms; and whether the contract is margin, total, quarter/half, team, player, or statistic.


AFL and AFLW are separate modelling populations. Do not transfer scoring levels or volatility without an explicit hierarchical adjustment.


## 2. High-value inputs


### Participants and roles


- Confirm the named team, interchange, substitute/activation rules for the current competition, late outs, and replacement.
- Estimate time on ground, position, centre-bounce attendance, ruck share, forward/defensive role, and expected matchup.
- Translate each absence into the territory/scoring chain; do not count a name without role consequence.


### Territory and shot creation


Use opponent-adjusted:


- centre and stoppage clearances;
- contested possession and pressure;
- turnovers/intercepts and rebound;
- inside-50s and repeat entries;
- marks inside 50;
- scoring shots, shot location/pressure quality, and expected score where available;
- conversion, separated from shot creation.


A ruck or clearance edge is not points until it survives the chain from hitout/contest → clearance → inside-50 → mark/shot → conversion.


### Context


Record venue dimensions/roof, surface, match-window weather, rest, travel, ladder incentives, and coaching/tactical changes. Weather can suppress clean handling or create territory/short-field repeat entries; no automatic Under is allowed.


## 3. Model


Exposure units are time on ground, centre/stoppage possessions, inside-50s, marks inside 50, and scoring shots. Estimate territory and shot creation first, then shot quality/conversion. Use a joint score and margin distribution with overdispersion and both late-separation and tempo-control branches.


Derive winner, handicap, total, phase, and player/stat contracts from that same distribution.


For numerical training, compare empirical and simple scoring-shot baselines with a territory → inside-50 → mark/shot → goal/behind A2 simulator. The simulator preserves both teams' tempo/territory dependence, shot quality, conversion, late separation and phase transitions. Direct joint-score, distributional boosting and hierarchical conversion candidates must pass AFL/AFLW population, support, covariance, overdispersion and calibration checks. Elo is an upstream strength feature/baseline, not a replacement for the scoring chain. Every line integrates the same joint score distribution. All candidates remain unfit and unvalidated.


## 4. Structural controls


1. **Decompose the current shot chain.** Model territory → inside-50 → mark/shot → shot quality/conversion separately. Raw recent totals and old H2H are diagnostic only; any numerical relative weight must be learned from prediction-time-safe data.
2. **Estimate conversion persistence separately.** Do not assume unusually accurate or inaccurate kicking persists or regresses at a fixed rate without current shot-quality and comparable-population evidence.
3. **Winner and handicap are different thresholds.** Model the whole margin distribution; do not align them mechanically.
4. **Positive handicaps for both teams can overlap.** Map every interval.
5. **Live Under requires observed suppression.** Remaining allowance must be supported by current inside-50/scoring-shot/tempo evidence.
6. **Large Q4 cushion requires remaining-possession analysis.** A tied or close state plus favourite clearance/territory control can create fast separation.
7. **Venue and competition matter.** Marvel/MCG/Optus and AFL/AFLW baselines are not interchangeable.
8. **Hitouts are opportunity, not territory.** Use clearance and post-clearance outcomes.
9. **High total needs a high-shot branch.** For 180+ men's totals, store both teams' current inside-50, marks-I50, scoring-shot, ruck/clearance and venue distributions.
10. **Motivation remains conditional.** Ladder urgency changes weight only through selection, roles, pressure, tempo, or tactics.
11. **Availability-to-conversion handshake.** Returning or absent forwards, midfield creators and goal kickers must be translated through role/time on ground, centre-bounce or inside-50 involvement, shot location/pressure, scoring-shot volume and goal/behind conversion. Do not apply a name-only scoring bump.
12. **Conversion sensitivity near the line.** When current personnel or shot-quality evidence makes conversion materially uncertain, report the total/margin ordering under at least a lower, central and upper conversion branch. Recent raw points or accuracy cannot fix the branch weight by themselves.
13. **Scoring volume and margin allocation are separate.** A low aggregate scoring-shot or conversion state can still create decisive separation when one side suppresses the opponent. Query the total and margin independently from the joint score tree; a broad Under is not evidence that an underdog cushion is safe.
14. **Ground-level wind is a phase variable.** At exposed venues, obtain the best available near-bounce wind speed/direction and map it to ground orientation and scoring ends. Generic city weather or a daily maximum is insufficient. Build quarter/end-switch branches for kicking, marks, territory and conversion; if the vector cannot be verified, widen margin and total states rather than calling conditions neutral.
15. **Fourth-quarter territorial durability is distinct from the total.** For AFLW and other lower-scoring states, separately model interchange availability, conditioning/heat, ruck/clearance persistence, repeat entries and defensive exit quality late. An Under can remain correct while one late quarter produces a favourite cover.


## 5. Live state


Store score, quarter/clock, scoring shots and accuracy, inside-50s, marks inside 50, centre/stoppage clearances, current-quarter territory, rotations, injuries/substitute, weather/roof, and tactical state. Recompute remaining scoring shots and margin branches rather than extending points per minute.


## 6. Sources and settlement


- AFL/AFLW official match centres, team sheets, injury reports, tribunal/late-change notices, and official statistics control.
- The [AFL statistics glossary](https://www.afl.com.au/news/144837/stats-glossary-every-stat-explained) controls definitions.
- BOM and official venue sources control weather/roof.
- Reputable tracking providers may supply expected score or role detail after definitions and coverage are checked.


Settle from the official final/stat provider, preserving draw/overtime and phase terms.


## 7. Upcoming-game research sequence


1. Freeze competition/rules era, venue, phase, draw/overtime terms and candidate slate; AFL and AFLW remain distinct populations.
2. Retrieve official selected teams, injuries, substitute/interchange rules and late changes first. Refresh after the current official final-team/late-change window and just before the bounce.
3. Model role/time-on-ground/CBA/ruck exposure, territory and clearance chain, inside-50s/marks-I50, scoring-shot volume/quality, goal/behind conversion, venue dimensions, roof/weather and tempo/separation tails. Translate returning/absent scoring personnel through that chain and run conversion sensitivity when it can cross the supplied line.
4. Treat conversion separately from shot creation and hitouts separately from clearances/territory. External ratings/consensus are baselines or challengers, not the scoring engine.
5. Derive joint scores, winner, total and margin/handicaps from the same score object; player/stat targets retain their own role/exposure labels.


Official AFL/AFLW sources own current teams, state and definitions. AFL Tables/Squiggle-style sources are candidate historical or external-model lanes only, with access/coverage limits recorded in DATA_SOURCE_REGISTER.md.


## 8. SFA-AFL — sport forecast algorithm


Algorithm ID: `SFA-AFL`. Effective **2026-09-02**. Instantiates `GFA-2` (RULES_GENERAL.md §11) with Australian rules content. Process composition only; no fitted weight, scenario weight or published probability is introduced. AFL, AFLW, state leagues and any other competition remain separate populations at every step.


### 8.1 Blocking preconditions


| Precondition | Requirement | Failure output |
|---|---|---|
| `AF-P1` competition and rules | Competition, rules era, quarter length and time-on convention, interchange and substitute/activation rules, draw and extra-time terms | `GATE-TARGET` failure; do not proceed |
| `AF-P2` selected teams | Official selected teams, late changes, substitute nomination and material outs for both sides, re-handshaken at G31 after the final late-change window | Role mixtures; dependent rows cap at `FORCED RANK` / `MEDIUM-LOW` |
| `AF-P3` venue and orientation | Venue, dimensions, roof status and ground orientation | Required before wind can enter any branch |
| `AF-P4` conditions vector | Best available near-bounce wind speed and direction mapped to ground orientation and scoring ends, plus surface state | Generic city weather or a daily maximum is insufficient; widen margin and total states instead of calling conditions neutral |


### 8.2 Exposure chain


Points are the last step, never the first. No step may be replaced by a recent points average.


| Step | Output |
|---|---|
| `AF-S1` | Role and exposure: time on ground, position, centre-bounce attendance, ruck share, forward and defensive role, expected matchup, and the replacement for every out |
| `AF-S2` | Contest and territory: centre and stoppage clearances, contested possession, pressure, turnovers and intercepts, rebound |
| `AF-S3` | Entry volume: inside-50s and repeat entries, both directions |
| `AF-S4` | Entry quality: marks inside 50, shot location and pressure, expected score where defined |
| `AF-S5` | Scoring-shot volume for both teams, derived from `AF-S3` and `AF-S4` |
| `AF-S6` | Conversion: goal and behind split, estimated separately from shot creation, with a lower, central and upper branch |
| `AF-S7` | Venue, roof, wind vector by end and quarter, and end-switch effects applied to `AF-S3`–`AF-S6` |
| `AF-S8` | One joint score and margin object with tempo-control and late-separation branches |


A ruck or clearance edge is not points until it survives hitout or contest, clearance, inside-50, mark or shot, and conversion.


### 8.3 Mandatory branch set


| Branch | Content |
|---|---|
| `AF-B1` | Central shot volume with central conversion for both sides |
| `AF-B2` | Lower conversion branch: same shot volume, accuracy below centre |
| `AF-B3` | Upper conversion branch: same shot volume, accuracy above centre |
| `AF-B4` | High-shot branch: both teams' current inside-50, marks-inside-50 and scoring-shot ceilings together — mandatory for any men's total at or above 180 |
| `AF-B5` | Suppression branch: one side limiting entries and entry quality, producing separation inside a low total |
| `AF-B6` | Quarter and end-switch branch: wind vector applied by quarter, with kicking, marking, territory and conversion each treated separately |
| `AF-B7` | Fourth-quarter territorial durability: interchange availability, conditioning and heat, ruck and clearance persistence, repeat entries, defensive exit quality |
| `AF-B8` | Draw and extra-time treatment under the exact competition and operator terms |


### 8.4 Contract derivation map


| Contract | Queried from | Extra condition the mechanism must predict |
|---|---|---|
| Total | Sum marginal of the joint score object | The component budget: each team's scoring-shot floor, centre and high, times each conversion branch |
| Line and handicap | Margin marginal | Separation, not merely which side is stronger; overlapping positive handicaps are mapped as intervals |
| Winner | Margin sign | A different threshold from the handicap; never aligned mechanically |
| Team total | Team marginal | That team's own entries and conversion against the opposing defensive exit |
| Quarter or half | The segment's own rotations, wind end and territory | A prior quarter is neither a ceiling nor a continuation rule |
| Player and stat props | Role, time on ground, centre-bounce or inside-50 involvement | The exact provider definition |


### 8.5 Kill-path library


| Kill path | Defeats | Evidence origin |
|---|---|---|
| Late territorial surge and repeat entries in the final quarter | An underdog cushion protected by a correct Under | §4 control 15, C-PL9-AFL-WIND-Q4 |
| A strong directional ground-level breeze shaping scoring end by end | A double-digit handicap or total ranked on generic city weather | §4 control 14, C-PL9-AFL-WIND-Q4 |
| Conversion moving while shot creation stays flat | A total ranked on recent points averages | L-008, §4 controls 2 and 12 |
| Returning or absent scoring personnel changing shot volume and quality | A name-only scoring bump, or an absence with no role consequence | §4 control 11, C-PL7-AFLW-CONVERSION-AVAIL |
| Territory dominance not converting | An Over ranked on clearances, hitouts or inside-50 volume alone | §4 controls 1 and 8; local lesson `M4-L08` in PREDICTION_MINI_LOG_4.md §E |
| One side suppressing entries inside a low-scoring state | A broad Under used as evidence that a cushion is safe | §4 control 13 |
| A venue baseline transferred between AFL and AFLW or between grounds | Any total ranked on a mismatched population | §4 control 7 |


### 8.6 Sport ordering overrides


1. Totals and margins are queried separately from the same score object. A broad Under never raises the `states` count of an underdog cushion.
2. When conversion uncertainty alone can cross a supplied line, that line's `corridor` is `INSIDE_CENTRAL` and the RULES_GENERAL.md §11.5 ceiling applies until an auditable conversion mixture is written.
3. If the wind vector cannot be verified at `AF-P4`, no total or handicap row exceeds `LEAN`, and margin and total states are widened rather than treated as neutral.
4. Hitouts are opportunity. They may not supply a decisive term in the G23.1 marginal-likelihood comparison for any scoring row.
5. Raw recent totals, old Under/Over counts and cover history are `E — diagnostic only`.


### 8.7 Pre-issue checklist


1. `AF-P1`–`AF-P4` status printed, including the late-change window and the wind vector source.
2. Venue and competition scoring-shot baseline stated before any line.
3. Full chain written from `AF-S1` to `AF-S6`, with conversion separated from shot creation.
4. All eight `AF-B*` branches represented; component budget solved at the supplied total.
5. Conversion sensitivity reported under lower, central and upper branches whenever it can cross the line.
6. Kill-path rows selected from §8.5 and reconciled against the issued order.
7. Fourth-quarter durability branch written whenever a handicap or close-margin row is ranked.
8. Selected teams, late changes, roof and near-bounce conditions refreshed at G31 before the view is appended.
9. Recency block complete per §8.8: L5/L10/L15/L20 for both sides and for head-to-head, continuity count stated, trend verdict per metric, unique-event de-duplication done.
10. Environment block complete per §8.9: **Near-bounce wind vector resolved against ground orientation** and mapped to scoring ends and quarters, or `WEATHER_NOT_AVAILABLE` declared.
11. `REFERENCE_BASE_RATE`, exact threshold, population and denominator recorded for every supplied row per §8.10 as a descriptive diagnostic only; no reference-band, trend or slot-frequency adjustment may move an ordinal (G23.1).
12. Extra-condition support audit (G24) recorded for every handicap, team-total and cushion row; no retrospective contract-family penalty is applied.
13. Separation budget (G20.1) solved for every margin, handicap and cushion row quarter by quarter, with the final quarter's territory, rotation and fatigue state held separately.
14. Rank-1 implied-target interval (G25.1) stated in the unit of every other supplied line, each remaining row classified `COHERENT`/`PARTIAL_OVERLAP`/`DISJOINT`, and every aggregate budget re-solved conditional on the Rank-1 state.
15. Winner-and-cushion reconciliation (G30.1) whenever Rank #1 is an underdog cushion, with the outright-win and narrow-loss branch ordering stated. Example separation kill path for this sport: a late-quarter territorial run.
16. Deficit attribution (G14.1) recorded for every weak, absent, returning or small-sample participant: which side's distribution moved and through which exposure step.


### 8.8 Recency, head-to-head and trend windows


Implements `GFA-2` step G13.1 (RULES_GENERAL.md §11.3B) and runs at that point in the algorithm, not at the end. Retrieval of L5/L10/L15/L20 for both sides and for the head-to-head series is mandatory; a window that does not exist is recorded with its true count and a missingness code.


Populate one windowed table per side with these metrics, and one head-to-head table:


| Window metric | Content |
|---|---|
| Territory | Inside-50s for and against, and repeat entries, opponent-adjusted |
| Entry quality | Marks inside 50 and shot location or expected score where defined |
| Scoring shots | Scoring shots for and against, held separately from points |
| Conversion | Goal-to-behind conversion, tracked separately from shot creation |
| Venue window | The same metrics at this exact ground, because Marvel, the MCG and Optus are different scoring environments |


**Head-to-head continuity.** Continuity means the same coach, a comparable list and the same ground. AFL and AFLW head-to-head are never pooled.


**Descriptive recency windows (G13.1; revised 2026-09-17).** Retrieve L5/L10/L15/L20 and continuity-qualified H2H with unique-event counts. These windows overlap. Monotonicity and dispersion among their averages are not a statistical trend/noise test. Report direction descriptively; estimate recency decay and opponent/regime effects using time-ordered validation. See SCORING_AND_VALIDATION section 5.


**De-duplication.** The windows overlap by construction and share matches with the head-to-head and venue series. Shrink from unique underlying events under G9; never treat L5, L10, L15 and L20 as four confirmations.


### 8.9 Environment and conditions


Implements `GFA-2` step G15.1 (RULES_GENERAL.md §11.3C). Venue classification for this sport is normally **OUTDOOR unless the venue roof is closed**.


| Field | Use in this sport |
|---|---|
| Near-bounce wind speed, gusts and direction | **Mandatory at exposed grounds.** Resolved against ground orientation and mapped to scoring ends and to each quarter |
| Roof state | Official venue source for Marvel Stadium and any covered ground |
| Hourly precipitation | Clean handling, ground-ball congestion and short-field repeat entries; no automatic Under |
| Temperature | Interchange rotation and fourth-quarter conditioning under `AF-B7` |


Failure to obtain the match-window forecast for an outdoor or open-roof event yields `WEATHER_NOT_AVAILABLE`, widened total and margin distributions, and a `LEAN` cap on every weather-dependent row. No factor above carries an automatic total direction.


### 8.10 Base-rate anchors and derived stat lanes


**Anchoring (G12.1).** Anchor totals on the ground-and-competition scoring-shot distribution, not on recent points averages, and margins on the competition margin distribution. AFL and AFLW anchors are separate.


**Derived and low-salience fields that are available and routinely skipped:**


| Field | Note |
|---|---|
| Ground dimensions and orientation | Required before any wind vector can be resolved |
| Centre-bounce attendance and ruck share | Role exposure, not a points input on its own |
| Substitute and late-change rules for the current competition | Changes the replacement tree |


## 9. Sport and competition rules reference


Added 2026-09-04; last reviewed 2026-09-04. Standing reference for the laws of Australian football and the competition rules of the AFL and AFLW. Supports `AF-P` identity and §6 settlement; introduces no rate, weight or ordering rule. The 2026 rules below are those in force for the 2026 seasons the current log covers.


**Maintenance (RULES_GENERAL.md §3, `G2`).** The AFL publishes a rule-change package almost every pre-season (the 2026 set added the last-disposal out-of-bounds rule and the centre-bounce ruck rule; the finals system changed to the Wildcard structure). Before the first card of a new AFL or AFLW season, or the first finals card of a season, re-verify the quarter/time-on structure, the interchange cap, the medical-sub rule, the current rule-change package and the finals bracket against afl.com.au, and update this section **before** issuing the card. The first time a state league (VFL, SANFL, WAFL) or a local competition is forecast, document its format and any local law variations here first.


### 9.1 The laws of Australian football


**Field and teams.** A large **oval** grass ground (typically 135–185 m long, 110–155 m wide — every ground is a different size, which is why ground dimensions gate the wind vector, §8.9). **18 players a side** on the field. Four **tall goalposts** at each end: two central **goal posts** ~6.4 m apart, flanked by shorter **behind posts**.


**Scoring.**
- **Goal = 6 points:** the ball kicked (by an attacking player, not touched after the kick, not off a post) entirely through the two central goal posts.
- **Behind = 1 point:** the ball goes through between a goal post and a behind post, or is touched before crossing the line, or is carried/knocked through, or hits a goal post, or comes off a defender's body.
- A score is written **goals.behinds (total)** — e.g. 14.9 (93). The behind is the key structural feature: it makes AFL totals near-continuous and means "accuracy" (goals ÷ scoring shots) is a separate random variable from scoring-shot generation (`SFA-AFL` §8, and §8.10 anchoring on the **scoring-shot** distribution, not points).


**Play.** Continuous, no offside. Move the ball by **kicking** or **handballing** (punching off the open palm) — **throwing is not allowed**. A player who takes a **mark** (cleanly catches a kick of 15+ m) gets a free, unimpeded kick. A player running with the ball must **bounce or touch it to the ground** every 15 m. Tackling is legal between the shoulders and knees; an illegal tackle, holding the ball, high contact, etc. → **free kick**. Out of bounds → a **ruck throw-in** (or, from 2026, a **free kick against the last team to dispose of it** if the disposal is between the two 50 m arcs — the "lasso"/last-disposal rule, previously AFLW-only).


**Match structure.** **Four quarters.** Each quarter is **20 minutes of playing time plus "time-on"** — the timekeeper stops the clock for stoppages (behinds, boundary throw-ins, injuries, etc.), so a quarter runs **~28–33 real minutes** and a full match ~2 hours. Quarter-time and three-quarter-time breaks are short; half-time is longer. Teams **change ends** each quarter (wind advantage alternates).


**Bench.** A matchday squad of **23**: 18 on field, **4 interchange** players who may rotate on and off freely, and **1 medical substitute** who can be activated once to permanently replace an injured/concussed player (the team then plays out with 3 on the bench).


**Result and the ladder.** A drawn home-and-away match **stands as a draw** — 2 premiership points each (win = 4, loss = 0). Ladder position is separated by **percentage** = (points for ÷ points against) × 100. Finals matches cannot be drawn — see §9.2.


### 9.2 AFL (men's Toyota AFL Premiership) — 2026


**Home-and-away season.** 18 clubs, **23 rounds**, each club playing 22 or 23 matches (an uneven fixture — not a full round-robin), March–August.


**Interchange cap.** **75 rotations per team per match** (unchanged for 2026). Rotations at quarter breaks, and for injury/blood-rule and the medical sub, do not count.


**2026 rule changes** (pace / "dead time" package): no player is required to stand in the goal square at a kick-in; the **last-disposal out-of-bounds free kick** between the arcs (as above); ruckmen at a centre bounce **cannot cross the centre line before the bounce** and umpires may restart without nominated rucks; kick-in time cut to **8 seconds**; stronger enforcement of "the stand" rule (the man on the mark must not retreat). These modestly **reduce stoppage time and slightly favour attacking transition** — a small nudge to scoring-shot rate, not a regime change.


**Finals — new Wildcard system for 2026** (replaces the pre-finals bye):


1. **Wildcard Round** (an extra week): the teams finishing **7th–10th** play off — **7 v 10** and **8 v 9**, hosted by the higher seed, single elimination. The **top six have a bye** this week.
2. The two Wildcard winners become the **7th and 8th seeds**, and the **top eight** then play the **"final eight" system in use since 2000**:
   - **Week 1:** Qualifying Finals **1 v 4** and **2 v 3** (winners advance to a Preliminary Final and earn a week off; losers drop to Week 2); Elimination Finals **5 v 8** and **6 v 7** (losers out).
   - **Week 2 (Semi-Finals):** Qualifying-Final losers host Elimination-Final winners.
   - **Week 3 (Preliminary Finals):** Qualifying-Final winners host Semi-Final winners.
   - **Week 4:** the **Grand Final** at the MCG (fixed venue).
3. Higher-seeded team hosts every final except the Grand Final.


**Extra time (all finals, including the Grand Final since 2016).** If scores are level at the final siren: a **6½-minute break**, then **two 3-minute halves plus time-on** (change ends at the interval, no break). Still level → repeat two more 3-minute halves, and so on **until a winner**. There are **no replays**.


**Settlement (AFL).** Full-game line and total settle at the **final siren of the fourth quarter** — for home-and-away matches a **draw is a live outcome** (spread pushes at the line, moneyline is a push / dead-heat / "tie no bet" by book). For **finals**, the market endpoint must be frozen: "including extra time" vs "regulation / end of the fourth quarter." Quarter and half lines settle at each siren, **including accumulated time-on** (so a "1st quarter total" is over a ~30-minute quarter). Margin and "winning margin band" markets are common and interact with the behind granularity.


### 9.3 AFLW (NAB AFLW Premiership) — 2026


**Structure.** The women's competition, 18 clubs, played **August–November** (spring), separate from the men's season. A **12-round** home-and-away season for 2026 (uneven fixture — not a full round-robin), then a four-week finals series ending with the Grand Final on the last weekend of November.


**Quarters (lengthened for 2026).** **17 minutes** per quarter — **15 minutes with time-on only for goals and major injuries**, then **~2 further minutes with time-on for all stoppages** — a deliberate change from the previous shorter, tighter-timed quarters. This raises the per-quarter and full-match scoring-shot budget versus earlier AFLW seasons, so **pre-2026 AFLW totals do not transfer without re-scaling** (`SFA-AFL` §8.8/§8.10; AFL and AFLW anchors were already separate).


**Interchange cap.** **60 rotations per team per match** (lower than the men's 75), excluding injury/blood and quarter breaks.


**Other AFLW-specific rules.** The **last-disposal out-of-bounds** rule has applied in AFLW for several seasons (the men's game only adopted it for 2026). Otherwise the laws match the men's game (18 a side, 6/1 scoring, marks, handball, bounce rule). Runner access is limited (three times per quarter, ≤90 seconds, not in the last three minutes).


**Finals and extra time.** **Top eight** into a final-eight bracket (same 1v4 / 2v3 / 5v8 / 6v7 structure), culminating in the **AFLW Grand Final** at a host venue. Finals level at the siren go to **extra time** (two short halves, repeated until a winner) — no replays. Home-and-away draws stand (2 points each), separated on the ladder by percentage.


### 9.4 Lower grades and state leagues (context)


The identity check may surface **VFL / VFLW, SANFL, WAFL** (state-league second tiers) and local competitions. These follow the same laws with local variations (some use shorter quarters, different interchange caps, and the last-disposal rule earlier than the AFL did). Each is its **own scoring population** — do not transfer AFL scoring-shot rates to a state league or vice versa (RULES_GENERAL.md, and `SFA-AFL` sparse-competition handling).


### 9.5 Identity checklist (Australian football)


Resolve before any rate work: **competition** (AFL / AFLW / VFL / SANFL / WAFL / local) and therefore quarter length + time-on rules, interchange cap, and which rule-change package is in force; **stage** (home-and-away vs Wildcard Round vs finals bracket vs Grand Final) and therefore whether a **draw is possible** or the match goes to **extra time**; the **ground** and its dimensions/orientation (for the wind vector); the medical-sub and late-change rules; and the operator's market **endpoint** for any final (regulation vs including extra time).


## September 5 settlement learning — prospective SFA amendment


At the territory→inside-50→chance→conversion chain, distinguish goals+behinds (scoring shots) from all attempted shots, rushed behinds, entry volume and chance quality. Opponent-adjust small current-season samples before treating scoring-shot differential as territorial superiority. AFL men's and AFLW evidence stay separate; a North Melbourne opponent and a Euro-Yroke opponent are not interchangeable exposure tests.


At G20/G20.1, cross high/low opportunity volume with ordinary/poor/hot conversion **for each team** and carry a final-quarter scoring-allocation branch. Geelong's 37 scoring shots overcame poor conversion; Bulldogs–Sydney changed from Sydney +4 after three to Bulldogs +27. Wind/precipitation may change opportunity generation and conversion in opposite directions. A modest Under lean still needs a conditional budget; no generic weather sign overrides it.


A Bulldogs/other opponent win in prose is insufficient if every printed score example has the selected favourite ahead. Include the opposite win/separation family without forcing arbitrary equal weights. Returning forwards receive play/limited/withdrawn states until the final warm-up check; unknown publication time is not proof of an ignored pre-cutoff withdrawal (Taylor Smith, P-289). Candidate C-P293-AFL-VOLUME is untested; no inferred wind or opposition-adjustment coefficient is promoted.


Match identifiers are host-qualified: this audit's Bulldogs–Sydney is AFL `/aflw/matches/8905` but Sydney club `/matches/8907`. AFL `/aflw/matches/8907` is Euro-Yroke–North; AFL `/aflw/matches/8910` is Yartapuulti–Gold Coast. Verify date/participants before reusing any host/ID pairing.




Full evidence and frozen-card comparisons: [September 5 audit](archive/audit_documents_implemented_2026-09-25/COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md).


## September 5(b) settlement learning — P-294–P-305 second continuation


Four AFLW cards settled this pass (`P-292`, `P-293`, `P-298`, plus carried-forward context): three different score textures in one round confirm that AFLW margins cannot be treated as a single distribution shape.


**`P-292` (St Kilda/Euro-Yroke vs North Melbourne) — extreme blowout.** North Melbourne 99, St Kilda 7 (92-point margin), against an Under 89.5 total pick — the total lost by 16.5 points because North Melbourne alone produced a score above the entire combined line. This is the AFLW-specific instance of the favourite-only-blowout branch already named in RULES_NRL_RUGBY.md's kill-path library, now with a second-code confirmation: extends `C-P293-AFL-VOLUME` (opponent-adjusted opportunities versus raw shot differential) with a case where the raw mismatch (undefeated top side vs a struggling bottom side) was itself sufficient signal that was still under-weighted relative to a season-average total line.


**`P-293` (Port Adelaide vs Gold Coast) — extreme low-scoring competitive game.** Gold Coast won 2.5 (17) to 1.8 (14) — a combined total of only 31 points in difficult conditions at Alberton Oval, with the underdog cushion (`Gold Coast +13.5`) covering by winning outright. This is the AFLW mirror of `P-299`/`P-303`'s large-cushion success in FIBA (see `C-PL15-BSK-CUSHION-VS-SPREAD` in LEARNING_REGISTER.md and RULES_BASKETBALL.md) and confirms L-054's conditions-widening treatment: the card's own "difficult conditions" note was correctly not converted into a one-sign automatic total adjustment, and a genuinely low-event game occurred inside the range that treatment allowed.


**`P-298` (Brisbane Lions vs GWS GIANTS) — L-077.** Brisbane, missing 5-6 rotation players including a recognised on-baller (Ally Anderson) and fielding two debutants, still won by 31 points (55-24), clearing `Brisbane -29.5` while `GWS +29.5` was ranked #1 and lost. Brisbane's absence list was real and correctly documented, but the discount applied to Brisbane's ceiling did not condition on GWS's own materially lesser roster depth (GWS themselves missing Goldsworthy and Srhoj, and fielding their own debutant). **New rule:** state the opponent's own roster quality in the same sentence as any personnel-loss discount — a depleted favourite against a weaker opponent is a different state from a depleted favourite against a comparable or stronger one, and the same absence list cannot receive the same numeric discount in both cases without that comparison being made explicit.


**Kill-path library addition (§8.5):**


| Kill path | Defeats | Evidence origin |
|---|---|---|
| A personnel-loss discount applied without comparing the opponent's own roster quality | An underdog cushion ranked above a quality favourite's spread purely on the favourite's absence list | `P-298`; L-077 |
| A raw top-vs-bottom AFLW mismatch (undefeated leader vs struggling/winless side) treated as ordinary variance around a season-average total | A total line set near the season-average combined score in an extreme-mismatch fixture | `P-292` |


Full evidence: [PREDICTION_LOG_COMBINED_2.md, 2026-09-05(b) section](PREDICTION_LOG_COMBINED_2.md#component-import--p-294p-305-second-continuation--2026-09-05b).


## September 6 settlement learning — separate the scoring-shot count from the conversion rate


`P-292` (North Melbourne 14.15 (99) d. St Kilda 1.1 (7); `Under 89.5` **LOSS** at rank #1, total 106) is the AFL/AFLW instance of the same defect that produced `P-294` in rugby league: the total was budgeted as a points figure rather than as **scoring shots × conversion**.


North Melbourne recorded **29 scoring shots** (14 goals, 15 behinds). At a league-typical conversion that is a ~100-point game on its own; St Kilda's 2 scoring shots were almost irrelevant to whether 89.5 was cleared. A card that budgeted only "St Kilda are a low-scoring side, so the total should stay down" was measuring the wrong side of the equation. Under `G20.2` this row is `TAIL_EXPOSED` on North Melbourne's own upper output before St Kilda's floor is considered at all.


**Required from now on, `SFA-AFL`:**


1. **Budget scoring shots and conversion rate as two separate terms.** Never carry a points total forward as a single number. AFLW in particular has a wide conversion band, so a 29-shot game can land anywhere from ~75 to ~115 points.
2. For the tail budget, hold each side's **scoring-shot count** (`S`, goals+behinds) at its second-highest L10 value and its **conversion rate** (`p` = goals/`S`) at its own L10 rate, then convert to **points**, not shots: `points = 6×goals + 1×behinds = S×(1 + 5p)`. **Correction, 2026-09-06(d):** the original wording here ("conversion rate ... print the implied total") never converted shot count to points, which silently drops behinds — applied to `P-292`'s actual 29 shots (14 goals, 15 behinds), a shots-only or naive shots-times-conversion reading understates the total; the correct formula, `29×(1+5×14/29) = 99`, matches the real total exactly.
3. A one-sided AFLW fixture is *more* dangerous for an `Under`, not less: the dominant side's inside-50 count compounds while the weaker side's floor is already near zero and cannot compress further. State this asymmetry explicitly whenever the expected margin exceeds ~40 points.


`P-298` (Brisbane 7.13 (55) d. GWS 3.6 (24); `Under 95.5` **WIN** at rank #2, `GWS +29.5` **LOSS** at rank #1) is the contrasting case and the origin of `L-077`. Brisbane's 20 scoring shots converted at 7/20 — a *low* conversion rate — which is precisely why the total stayed under despite a 31-point margin. Same structure as `P-292`, opposite conversion outcome. That is the argument for splitting the terms rather than modelling points directly.


### Kill-path library addition (§8.5)


| Kill path | Defeats | Evidence origin |
|---|---|---|
| **Scoring-shot compounding in a mismatch** — the dominant side's inside-50 and shot count rise together while the weaker side is already at its floor | A full-game `Under` justified by the weaker side's low scoring | `P-292` (106 against `Under 89.5`) |
| **Low-conversion suppression** — a high scoring-shot count converts poorly and holds the total down despite a comfortable margin | An `Over` justified by territory/inside-50 dominance alone | `P-298` (7.13 — 20 shots, 55 points) |




### Cross-sport gates instantiated here (v3.7)


| Gate | Sport-native instantiation |
|---|---|
| `G10.2` settlement-source pre-registration | AFL/AFLW settle from the AFL official match report and its host-qualified event ID per `L-071`; name the exact match record at freeze. |
| `G14.2` coaching / bench / rotation record | Record the senior coach, the named emergencies/medical substitute, and the AFL/AFLW substitution provision from §9, plus any confirmed managed-rest signal. Official club team announcements (released 60 minutes pre-bounce) or accredited AFL Media reporting verified under Control `S-1 Rev 2` qualify as `PROJECTED_BEAT_VERIFIED`, satisfy `G14.2`, and do not block Rank #1. |
| `G20.2` distributional tail audit | Derive tail and boundary mass from the **same frozen AFL/AFLW scoring distribution**, explicitly separating scoring-shot opportunity from conversion and conditioning on role/selection/bench, venue/weather and quarter-state exposure. Historical second-highest-L10 scoring-shot constructions are superseded as active gates. |
| `G21.1` exact target geometry | Map every supplied target to its exact settlement event and derive WIN/PUSH/LOSS from the same frozen sport-native PMF/CDF or coherent branch mixture. Historical path-count/category labels have no mandatory ordinal effect. |
| `G26.1` no universal separation floor | Reference rates and `rank_gap` are descriptive only. **No 40–60% or other pooled probability band can disqualify Rank #1.** Rank from exact marginal likelihood plus robustness/evidence uncertainty. |


**Pre-issue checklist additions (this sport):** settlement endpoint named per row; coaching/bench/rotation record for both sides with missingness codes; tail-budget sums printed against every total line; path-geometry class and `N` printed for every total and phase-total row; separation-floor result stated for Rank #1.


Full narrative and evidence: [`archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md`](archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md). Controlling gate text: [`RULES_GENERAL.md` §13](RULES_GENERAL.md).


## September 5 implementation after freeze confirmation


**ACTIVE REQUIRED PROCESS — MDS-2026.09.05-v3.6 / L-068–L-072.** Separate opportunity volume from conversion, adjust short windows for opponents, and evaluate each side’s final-quarter separation path. Weather informs the opportunity/conversion chain rather than applying a blanket Under adjustment. Recheck final warm-up availability and preserve its publication timing.


At final delivery, record the preferred total direction for each exact target, the strongest evidenced failure path for ranks #1 and #2, and whether both can win under the stated joint scenario. Rank by supported marginal likelihood; do not promote an opposite pick solely to manufacture one O/U win. At settlement, keep all issued wins/losses, including defective reasoning, in the applicable historical scorecard and review failed #1/#2 and preferred totals.


[Eligibility policy](PERFORMANCE_ELIGIBILITY_POLICY.md): non-live history is user-confirmed frozen pre-game; explicit live-issued views stay separate. These process repairs are implemented now. Numerical weights and predictive-lift claims need a later frozen comparison; historical origin games do not supply those completions.


## 2026-09-06(f) — settlement and retrospective addendum


P-292/P-294 cross-sport contrast and P-315 reinforce a favourite-driven high-total path even when the opponent is weak. P-298/P-315 require role/replacement and opponent context for absences, not a flat injury discount. P-315 territory reversed by quarter; no unverified wind-to-end cause is asserted. Preserve points = scoring shots + 5 × goals, and audit winning thresholds separately from inaccurate score corridors. These are existing analytical controls, not new ordinal weights.


Full frozen ranks, actual drivers, knowability and smallest fixes: [PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md). Reinforcement only; METHOD v4.0 remains controlling and no new predictive weighting is promoted.


## 2026-09-09 — cross-sport controls instantiated here (`G-L1`, `G-L2`, `G-L7`, `G-L8`)


No AFL/AFLW card was issued in the `P-333`–`P-344` cohort. The four cross-sport requirements adopted from it (`RULES_GENERAL.md` §§16.5(a)–(d), full evidence in `PREDICTION_LOG_COMBINED_3.md` §"2026-09-09") apply to this sport from the next card, instantiated as follows. All four are **disclosure/retrieval requirements — no fitted weight, no ordinal bar** (`L-087`).


| Cross-sport control | AFL/AFLW instantiation |
|---|---|
| **`G-L1` §16.5(a)** — enumerate outcome-state families with explicit mass | Enumerate the **margin families** in native units (favourite by 40+ / 20–39 / 6–19 / within a goal / underdog win) and the **total families** in points, each with a probability mass summing to 1. Every kill path in the §8.5 library that has current specific evidence must appear as one of those weighted branches. Print a **representative Rank-#1 final score** in points and check it simultaneously against the line, the total and any team-total row — remembering `points = scoring shots + 5 × goals`, so a representative score must be stated as a goals/behinds pair, not a bare number. |
| **`G-L2` — declared uncertainty model** | State the prior and scenario probabilities. Symmetric uncertainty around an unchanged prior affects width; hierarchical shrinkage or asymmetric scenarios may change both mean and variance. Regenerate all dependent probabilities; unsupported directional adjustments remain prohibited. SCORING_AND_VALIDATION section 5 controls. |
| **`G-L7` §16.5(c)** — aggregate-to-disaggregate retrieval | Do not let a season average or a "last N" summary carry directional weight while the **per-game log** is available. Print the **round-by-round record** for the decision-relevant window — score, scoring shots, goals/behinds split, and for the decision-driving players their **game time and goal/disposal output per match** — and state whether a run of poor or strong results is front-loaded, back-loaded or uniform. Quantify **every top-three goalkicker and every player above roughly 75% game time on both sides**; a player carried as a bare name in a "leaders include…" phrase is `AGGREGATE_ONLY` and the margin/total rows that depend on the team's scoring ceiling are capped. |
| **`G-L8` — distribution coherence** | Derive each total/spread probability from the exact joint PMF/CDF and settlement endpoint, with push mass. Absolute normalised distance does not order probabilities across different distributions. No missing width or realised result justifies an invented probability. |


## 2026-09-11 — cross-sport controls instantiated here (`G-L9`, `G-L10`, `G-L11`, §16.8)


No AFL/AFLW card in the `P-345`–`P-371` import. The three disclosure requirements and the completeness block adopted from it ([`RULES_GENERAL.md` §§16.5(e)–(g), §16.8](RULES_GENERAL.md)) apply from the next card. AFL is `PRIMARY_SCORED`, so this is where they will first count.


| Control | AFL / AFLW instantiation |
|---|---|
| `G-L9` §16.5(e) | A 0.70 line or total row itemises its 0.30 across the named paths — goal-kicking inaccuracy (goals v behinds), a late key-position out, wet-weather low scoring, the underdog winning the clearance battle. |
| `G-L10` §16.5(f) | A favourite line + Over pair is positively coupled when the favourite's scoring drives the margin; an underdog line + Under pair is positively coupled through a contested, low-possession game. Print the sign. |
| `G-L11` §16.5(g) | Goal-kicking accuracy over a few matches (goals ÷ scoring shots) is a small-sample proportion — print its standard error before it moves a centre. |
| §16.8 | Teams are named before the match and finalised before the bounce; `NOT_RETRIEVED` after publication is a `RETRIEVAL_MISS`. |




## 2026-09-12 algorithm corrections and retrospective integration


Apply section 16.9 to joint goals/behinds, total points, margins and quarter targets. A high-scoring favourite separation and a slow close contest both remain possible. Confirm both selected sides, interchange/substitute rules for the competition and season, late changes and coaches. No new AFL result was settled in this pass: these are transferable arithmetic/provenance repairs, not an AFL-specific empirical improvement. Count event clusters for any future total-family comparison.


For every supplied row, use exact target probabilities from a coherent joint distribution; handle push/void/censoring explicitly, avoid overlapping adverse-state counts, and report JOINT_UNQUANTIFIED with bounds if the dependence is not specified. Separate issued-time participant capture, later recovered evidence, source accuracy by field, observed mechanism, and unverified causal interpretation. Keep one preferred O/U direction per distinct target and report the top-two denominator honestly. Shared correction and methodology sources (`audit_2026-09-12/rule_corrections.md`, not present in this repository). All current log observations remain learning-only and not performance-eligible.




## 2026-09-15(b) settlement learning — `P-373`–`P-423` import


Learning-only; disclosure/process changes only — no coefficient or ordinal bar (`L-087`). Evidence and tables: [`PREDICTION_LOG_COMBINED_3.md` §"2026-09-15(b)"](PREDICTION_LOG_COMBINED_3.md). Cross-sport rule: `RULES_GENERAL.md` §16.10 (`G-L12` margin centre/width; fixture identity; official-record derivative settlement).


**Cards:** P-388 (Fremantle 120–106 Geelong; Geelong +11.5 LOST), P-396 (Brisbane 144–91 Adelaide; Adelaide +21.5 and Under 188.5 LOST). Finals re-verified at ESPN `australian-football/afl`.


- **P-396:** 65 scoring shots against a central ~50 — the miss was shot volume, not conversion; the high-shot branch (`AF-B4`, control 9) existed but carried too little mass, and it killed both top rows together (`G-L10`).
- **P-388:** the high-shot / upper-conversion family was printed and under-massed (`G-L9`).
- **`G-L12` instantiation:** finals margins take their centre from the scoring-shot differential chain, not from a shrink toward a close game; print P(favourite by more than the line) from the shot × conversion families.


## 2026-09-16 — cross-sport controls instantiated here (`G-L13`, `G-L14`, `G-L15`, disruption facts)


No AFL card was settled this pass. Rules: `RULES_GENERAL.md` §16.11.
- **`G-L13`:** quarter scores, scoring shots and team selections come from the raw AFL match centre or ESPN `australian-football/afl` JSON, never from a summary.
- **`G-L14`:** a quarter or half target names its settling record. ESPN quarter line scores were verified for finals in 2026-09-15(b).
- **`G-L15`:** label total rows forced-pair or free. Rugby league/AFL forced-pair preferred sides went 2 of 3 in `P-345`–`P-423`.
- **Disruption facts:** record medical-substitute activations and concussion withdrawals, with the quarter and the margin at the time.


## 2026-09-17 — cross-sport controls instantiated here (`G-L17`–`G-L20`)


No AFL card in this import. **`G-L17`:** when a margin row and a total row share one game-shape thesis, print `P(¬R1 ∧ ¬R2)` and name the state (usually a scoring-shot surge that breaks the margin and the total together). **`G-L18`:** print each side's own score marginal before ranking a match total. **`G-L19`:** AFL permits a drawn home-and-away match — a winner family must carry draw mass. **`G-L20`:** a current-season same-venue meeting that already cleared a line gets explicit mass.


Evidence and cohort audit: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17"](PREDICTION_LOG_COMBINED_4.md); rules in `RULES_GENERAL.md` §16.12.


## 2026-09-17(b) — cross-sport controls instantiated here (`G-L21`–`G-L24`)


**G-L24 in AFL:** derive the exact signed-margin distribution under the competition endpoint, including draw, key-value and push masses. Pooled league bands are uncertain references, not mandatory matchup probabilities or rank prohibitions. Missing pooled bands do not invalidate a complete conditional joint distribution. **`G-L21`:** a 'wet weather, low-scoring, favourite controls it' thesis routinely carries a line, an Under and a team total at once — print `P(all fail)` with bounds. **`G-L22`:** line and total arrive as forced pairs; report preferred sides. **`G-L23`:** inside-50s, clearances and the quarter-by-quarter record are the process fields; sub/injury exits with the clock are the disruption facts.


Evidence and cohort audit: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17(b)"](PREDICTION_LOG_COMBINED_4.md); rules in `RULES_GENERAL.md` §16.13; bands and base rates in [`BASE_RATES_REGISTER.md`](BASE_RATES_REGISTER.md).


## Current model implementation — 2026-09-17


Use METHOD v4.2's six-field object and SCORING_AND_VALIDATION for exact outcome/push scoring, event-level comparison, descriptive recency and declared hierarchical uncertainty. MODEL_IMPLEMENTATION_RECIPES supplies this sport's retained model scope and endpoint design. Forecast probabilities come from the joint model; pooled base rates are uncertain context, not universal limits. Numeric row caps disconnected from that model, absolute-distance probability ordering and retrospective tail reweighting are withdrawn. No fitted coefficient or predictive improvement is claimed. New cards freeze the method/control hash; existing cards keep their issued versions.


## 2026-09-19 — recency/rebound evidence, debutant gate and the top-O/U review


Cross-sport: [`RECENCY_AND_REBOUND.md`](RECENCY_AND_REBOUND.md) control `R-1`; source controls `S-1` (social identity) and `S-2` (press conferences) in `SOURCES.md` §"2026-09-19"; enhanced-failure trigger in `METHOD.md` §7.


**`R-1` applies qualitatively; AFL magnitudes are `NOT_YET_DERIVED`.** Note the finals-specific caution already recorded: `P-459` carried a total centre near 184 into a game that produced 154, in dry conditions with no weather mechanism. Home-and-away scoring rates are a poor prior for finals.


**Press-conference and selection material (`S-2`).** AFL clubs publish selected teams, ins/outs and coach commentary on official domains, and `P-459` used them correctly — it is the only card in that cohort with confirmed participants for both sides. Continue treating stated tactical intent as branch-motivating, not centre-moving.


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — market-independent totals/line addendum


**Source priority:** AFL official match centre/team sheets/injury information, club releases and BOM/appropriate government weather. Betting/fantasy content is prohibited predictive evidence.


Use a joint team-score/margin distribution driven by current personnel, venue dimensions/home state, weather, rest/travel and stable process statistics such as scoring opportunities/inside-50/clearance/shot-conversion components when sourced and definition-stable. Supplied totals/lines cannot anchor the score centre.




<!-- ALL-SPORTS-AUDIT-LIVE-RULE-CLEANUP-2026-09-21-CR3 -->
## 2026-09-21 — all-sports audit live-rule cleanup — CR-2026.09.21-3


Current prospective override. Retain scoring-shot opportunity versus conversion, role/selection/bench, venue/weather, quarter-state exposure and three-source finality. Withdraw pseudo-tail order-statistic constructions, path-count ranking shortcuts, universal probability-band top-slot rules, normalized-distance ordering and one-result response rules. Build one coherent AFL/AFLW joint outcome distribution before querying targets; do not invent precise probabilities without a fitted/calibrated distribution.

<!-- SETTLED-ROW-REVIEW-2026-09-25D -->
## 2026-09-25(d) — track record from the full settled-row review

**Track record (`C-TRACK-RECORD`).** 10 decisions from 4 cards: won **30%** at a mean stated 0.662. The gap is −0.36, with a card-cluster interval of [−0.60, −0.10]: **over-confident**. AFL cards are labelled **`NO_DEMONSTRATED_SKILL`**: the evidence grade is capped at LOW and the departure ledger is required.

- **Underdog cushions (+k.5): 0/3.** `C-PLUS-CUSHION` applies.
- **Missing reference.** There is no AFL population reference yet (`BASELINE_P: NOT_YET_DERIVED`). Deriving an AFL margin and total population from the field owner is the first step to an honest baseline.

Source: `research/settled_rows_2026-09-25/README.md`. The figures are hindsight on the framework's own cards, descriptive, and use card-cluster intervals. None is a coefficient (`L-087`). Controls: `RULES_GENERAL.md` §"2026-09-25(d)".


<!-- RANK-MODEL-2026-09-25E -->
## 2026-09-25(e) — the first AFL population reference, the team baseline and the ranking model

Controls: `RULES_GENERAL.md` §"2026-09-25(e)". Evidence: `research/team_baseline_2026-09-25e/README.md`; `BASE_RATES_REGISTER.md` §7.7.

This implements the 2026-09-25(d) to-do ("deriving an AFL margin and total population from the field owner is the first step").

**Record at Rank 1/2, NFL, AFL and NRL together: 12 W / 20 L,** the worst of any group. The losses were mostly underdog cushions and totals. AFL stays `NO_DEMONSTRATED_SKILL`.

### (a) Sources

- **ESPN AFL scoreboard** `…/australian-football/afl/scoreboard?dates=YYYYMMDD`: one date per call; season type 2 = home-and-away.
- **ESPN team schedule** `…/australian-football/afl/teams/{id}/schedule?seasontype=2`: the TB-1 lane (`python tools/team_baseline.py predict --league afl …`).
- **Unchanged:** the settlement sources.

### (b) Reference rows (AFL 2025 / 2026, n = 207 each)

| Row | 2025 | 2026 |
|---|---:|---:|
| Home win | 0.565 | 0.585 |
| Draw | 0.005 | 0.015 |
| Total mean (SD) | 168.6 (29.8) | 178.2 (29.1) |
| Total, 10th / 50th / 90th percentile | 132 / 168 / 208 | 142 / 181 / 216 |
| Home margin | +6.0 | +7.1 |
| Margin SD | 42.5 | 40.8 |
| P(\|m\| ≤ 12) | 0.30 | 0.28 |
| P(\|m\| ≤ 24) | 0.48 | 0.47 |
| TB-1 residual width, total / margin | 29.8 / 36.9 | 29.1 / 36.7 |

These replace `NOT_YET_DERIVED` for `BASELINE_P`, the reference row and the reference width.

### (c) Reasoning

1. **TB-1 is the anchor for sides and margins.**
   - It has the strongest resolution of any league: P(home win) Brier 0.202 against 0.249 (2026, chosen on 2025).
   - **Totals have no resolution** (0.248 v 0.255, below the 3% bar). Totals anchor on the 2026 population row.
2. **Cushions.** The TB-1 underdog covered:

   | Cushion | Cover rate (2025–26) |
   |---|---|
   | +6.5 | 0.38–0.43 |
   | +12.5 | 0.48–0.51 |
   | +18.5 | 0.56–0.59 |
   | +24.5 | 0.60–0.62 |

   A cushion stated above its rate by more than 0.05 needs a receipted mechanism on the favourite's side (`C-PLUS-CUSHION`). Otherwise RM-1 flips it. The record's AFL cushions were 0/3.
3. **Finals.** TB-1 is a regular-season model. For finals, print `TB1_FINALS_CONTEXT` and name the finals-specific departures: venue, rest days, and the weather at the ground.
