# American football analysis rules


> **2026-09-12 operational correction:** The dated section at the end of this file and RULES_GENERAL section 16.9 control over conflicting older probability, coupling and source claims.


> **`METHOD.md` is now the primary mandatory read (v4.0 comprehensive overhaul, 2026-09-06).** This file remains the full sport-specific reference: its `SFA-<SPORT>` algorithm and competition-rules section (`§9`/`§10`/`§11`) are consulted in full when forecasting this sport; `METHOD.md` states the cross-sport process once.


<!-- THREE-SOURCE-TIME-GATE-2026-09-19-CR4 -->
> **Current cross-sport authority — MDS-2026.09.19-v4.3 / CR-2026.09.21-3:** this sport module inherits the reconciled all-sports source, timing, settlement and distribution-construction controls. Historical issued cards retain their own revision.


Status: **ACTIVE**
Effective: **2026-09-06 (v4.0 comprehensive overhaul — see METHOD.md and archive/audit_documents_implemented_2026-09-25/FRAMEWORK_AND_GAME_LOG_OVERHAUL_REVIEW_2026-09-06.md)**
Method version: **MDS-2026.09.06-v4.0**
Applies with RULES_GENERAL.md, MODEL_AND_DATA_SPEC.md, ALGORITHM_PORTFOLIO_AND_EVALUATION.md, and NUMERICAL_TRAINING_SPEC.md.
Executable algorithm: **SFA-AMERICAN-FOOTBALL (§8) — instantiates GFA-2 in RULES_GENERAL.md §11**
Numerical training specification: **NTS-2026.09.02-v0.3 — design only; no football model is fit**
Sport and competition rules reference: **§9 (added 2026-09-04)** — the rules of gridiron football and the NFL / NCAA / CFL / UFL rule differences, plus per-competition rules for every competition in the prediction logs (NFL incl. preseason, NCAA FBS and FCS, CFL). Reference material for identity, state and settlement; it does not change `SFA-AMERICAN-FOOTBALL`.
Evidence density: **SPARSE** (added 2026-09-06, `L-099`, external blindspot audit `B-13`) — this sport has markedly fewer settled cards in this log than baseball, soccer or cricket, and much of the sample is preseason/rotation-uncertain. Every identity/state/contract/source/coherence gate applies at full force regardless; any *directional or magnitude* claim in this file is held to lower confidence than an equivalent claim in a `DENSE` sport and may not be promoted `PROMOTED_PROCESS` on one or two cards alone.


<!-- LIVE-RULES-PAGE-2026-09-26 -->
## 0. Live rules — one page (consolidated 2026-09-26)

**Status.** This page consolidates everything in this file that is live on 2026-09-26: the numbered controls, SFA-AMERICAN-FOOTBALL and the dated sections through 2026-09-25(e). It is a derived index. If it disagrees with the section it cites, the cited section governs and this page is corrected in the same pass. **Reading gate (C-READING-GATE, 2026-09-26):** read this page in full for every gridiron card, then open each cited section the card relies on (and §9 for the code's rules). Everything below §0 is the full reference and its history.

**NFL/NCAA is `NO_DEMONSTRATED_SKILL` and over-confident.** 12 decisions won 25% at a stated 0.544 (gap −0.29, card-cluster interval −0.47 to −0.12). Every Rank-1 loss was an underdog cushion of +1.5 to +6.5 stated at 0.53–0.58 (P-412, P-413, P-414, P-422, P-472). The evidence grade is capped at LOW and the departure ledger is required. NFL, NCAA, CFL and UFL are separate populations.

### 0.1 Blocking preconditions (§8.1)
| Gate | Requirement | If it fails |
|---|---|---|
| AM-P1 code and rules | Downs, field, regulation, overtime and tie terms, and each row's phase | Stop |
| AM-P2 quarterback | Starter with release status, backup branch, health and mobility, re-handshaken after the inactive release | QB mixture; dependent rows capped |
| AM-P3 units | Offensive-line combination, skill snaps, defensive front and coverage absences, kickers where a row depends on them | Widen side and total; cap unit-dependent claims |
| AM-P4 preseason rep plan | QB, line, skill and defensive rotation by quarter | Never project a starter or one reserve sample through four quarters (controls 9, 11) |
| AM-P5 college availability | The absence of an NFL-style report is not evidence of health | Missingness code (control 10) |

### 0.2 Building the score distribution
1. **Anchor.** NFL: `TEAM_BASELINE_P` (`tools/team_baseline.py --league nfl`) for sides (0.231 v 0.252). Totals anchor on the population: TB-1's marginal total gain (0.246 v 0.254) is not significant (corrected 2026-09-26(e); `TB1_NO_RESOLUTION:total`). Weeks 1–3 are flagged `TB1_EARLY_SEASON`. NCAA has no TB-1 lane (`NOT_COVERED`).
2. **Margin prior and width (control 17, G-L12).** Print the margin prior (prior-season differential adjusted for QB status) and a width no narrower than the residual SD (**13.6**, TB-1 2025) unless the card shows why. New-regime uncertainty widens; it does not centre the margin toward pick'em (controls 15, 16). Prior-season unit ratings are width in a new season (control 19).
3. **Discrete scoring.** Key numbers and pushes come from score combinations (control 6). Every handicap row prints the exact masses at 3 and 7 (control 18); a card without a margin table caps its handicap rows at FORCED RANK.
4. **Non-offensive scores (control 20).** A handicap row within one score of the centre carries a defensive or special-teams TD branch: 0.217 per game, at least one in 18.8% of games (2025), adjusted only with named evidence (backup QB, sack or turnover rates).
5. **Game script and dependence.** A leading favourite drains clock; a trailing team adds yards, sacks and garbage-time points (control 3). Low total ≠ close spread (control 13). When a handicap and a total are both in the top two, print P(favourite covers ∧ Under) and P(underdog covers ∧ Over) from the joint table (control 21).
6. **Shrink turnovers and one-score records** without a pressure, decision or ball-security mechanism (control 4). Weather is matchup-specific; rain is not an automatic Under (control 5).
7. **One joint score object → every row.** Overtime follows the exact competition rules (control 7).

### 0.3 Row rules
- **Cushions (C-PLUS-CUSHION).** The TB-1 underdog covered +1.5 at 0.35–0.42, +2.5 at 0.38–0.46, +3.5 at 0.45–0.54, +6.5 at 0.57–0.60, +7.5 at 0.61–0.66. A cushion at or above that without a receipted mechanism is `PLUS_CUSHION_UNSUPPORTED`, and RM-1 flips it. A +2.5/+3.5 prints the mass at 3 (0.14–0.15); a +6.5/+7.5 prints the mass at 7 (0.07–0.10).
- **Aligned current-regime uncertainty caps a favourite** (control 15): several uncertainties supporting the favourite's kill path keep its spread below SUPPORTED.
- **CFL** uses its own possession-to-points chain (control 14). **Preseason** is a quarter-by-quarter unit mixture with reserve-sample shrinkage and explosive tails (controls 11, 12).

### 0.4 Reference rows (NFL regular season, n = 272 each; `BASE_RATES_REGISTER.md` §7.7)
| Row | 2024 | 2025 |
|---|---:|---:|
| Home win | 0.524 | 0.536 |
| Total mean (SD) | 45.8 (13.1) | 46.0 (13.8) |
| Home margin; margin SD | +1.7; 14.5 | +2.2; 14.2 |
| TB-1 residual width, total / margin | 13.1 / 13.7 | 13.4 / 13.6 |
| P(\|m\| = 3); P(\|m\| = 7) | 0.136; 0.074 | 0.151; 0.096 |
| P(\|m\| ≤ 3); P(\|m\| ≤ 7) | 0.24; 0.52 | 0.27; 0.50 |

Margin bands (2025): 0–6 40.1%, 7–13 24.6%, 14+ 35.3%; mean absolute margin 11.15.

### 0.5 Ranking and settlement
Rank by RM-1 q; its cushion term applies to gridiron +k.5 rows. Settle from ESPN `football/nfl` summaries (with `scoringPlays`) plus two further lineages; record non-offensive scores, turnovers and sacks as process facts.

### 0.6 Withdrawn in gridiron — never apply
A universal 13.9 SD floor (the residual benchmark is a disclosure reference, not a floor); a hand-picked healthy-QB window as the prior; pseudo-tails, path-count categories, 40–60% bands and normalised-edge ordering.

### Numerical shadow model (2026-09-26(c); never a card input)

`python tools/sport_models.py shadow --league <nfl|ncaaf> …` (`C-SPORT-SHADOW`). A1 is ridge ratings with the league's own key-number weights (3, 7, …). On the NFL 2021–2025 it beat the league baseline on results and margins. It was ahead of TB-1 on results, but the interval crosses 0. It gave **no gain on totals**. Record it after the freeze and before the start; it is never printed, ranked or cited on a card, and a promotion needs its 150-row review and your instruction (`RULES_GENERAL.md` §"2026-09-26" (e), (k); `research/sport_models_2026-09-26/README.md`).

**Predictability and cards (2026-09-26(e)).** In the NFL 2025, the model's favourite reached 0.70 in 27% of games and won **73.1%**. The 0.70–0.80 band won only 67% at a stated 0.747, so it is over-confident. Totals reach 0.70 in only 8% of games. The side reference is TB-1, because A1 was not separated from it. On the cards' own NFL contracts (9, from 5 cards): card 0.266, A1 0.274, population 0.301 (`research/predictability_2026-09-26/README.md`; `BASE_RATES_REGISTER.md` §7.8).

### 0.7 Control index (full text in §4 and the dated sections)
1 QB identity is a regime · 2 line continuity is combinatorial · 3 game script creates dependence · 4 turnovers and one-score records shrink · 5 weather is matchup-specific · 6 key numbers and pushes are discrete · 7 OT matches the competition · 8 special teams are field position · 9 preseason is a separate phase · 10 college availability is asymmetric · 11 preseason quarter-by-quarter unit mixture · 12 reserve-sample shrinkage and explosive tails · 13 low total ≠ close spread · 14 CFL possession chain · 15 aligned regime uncertainty caps a favourite · 16 new-regime uncertainty two-sided · 17 margin prior and width · 18 key numbers at 3 and 7 · 19 prior-season ratings are width · 20 non-offensive score branch · 21 favourite covers inside the Under.


## 1. Identity and contract


Resolve NFL preseason/regular/postseason, NCAA level/conference/bowl/playoff, UFL, high school, CFL, or another code. These are different rules and data environments. Record regulation/OT/tie terms, spread/total/team/player phase, stat provider, and listed-player/action terms.


Verify the current governing rulebook. Relevant 2026 regime checks include NFL kickoff/onside/overtime rules, NCAA timing/overtime and conference availability systems, and UFL four-point field goal, 1/2/3-point try, punt, catch, and shootout-style overtime rules. Never transfer NFL key numbers or possession rules to NCAA/UFL/CFL.


## 2. High-value inputs


### Quarterback and expected snaps


- Confirm starting quarterback, backup branch, health/mobility, expected snaps, and scheme.
- For side, total, passing, rushing, or pressure-sensitive markets, map the material offensive-line combination and replacements. Do not require irrelevant roster detail for an unrelated contract.
- Estimate expected snaps/routes/carries/targets for material skill players and replacement roles.
- Record defensive front, coverage, and sub-package absences that affect the matchup; confirm kicker/punter/long snapper when the contract depends on them.
- Preseason requires quarterback/unit rotation and expected reps, not regular-season power ratings.


### Drive process


Use opponent- and quarterback-regime-adjusted:


- expected drives and neutral pace;
- starting field position;
- early-down EPA/success;
- pass/run rate and play action;
- pressure, sack, scramble and explosive rates;
- coverage and protection matchup;
- third/fourth-down and red-zone process;
- turnovers with shrinkage;
- special-teams field position and scoring.


Raw points, one-score record, turnover margin, and defensive touchdowns are outcomes, not stable abilities by default.


### Context


Record rest/bye/short week, travel/time zones, surface/roof, venue-local weather, altitude, opponent quality, and verified roster/coach changes. College homecoming, exams, rivalry, bowl, portal or opt-out context matters only when verified and connected to participation or tactics.


## 3. Model


Exposure units are drives, plays within drives, starting field position, and expected snaps. Map drive outcomes to touchdown, field goal, no score, safety, and non-offensive score, then add dependent tries/kicks.


Use quarterback-regime dynamic strength, trench and coverage interactions, and explicit explosive/turnover/non-offensive-score tails. Points cluster around football scoring values and are not a homogeneous Poisson process. Derive side, total, team, phase and player contracts from one joint score distribution.


For numerical training, retain empirical and simple drive-rate baselines, then challenge them with a drive/possession A2 simulator. It samples remaining drives, start field position, plays, TD/FG/safety/no-score/turnover outcomes, dependent tries, non-offensive-score tails, clock/game script and competition-specific overtime. Tree or distributional models estimate state components or a coherent score grid; they do not fit one independent classifier per spread/total. Exact football key values and push mass come from the discrete joint score distribution. All candidates remain unfit and unvalidated.


## 4. Structural controls


1. **Quarterback identity is a regime change.** Rebuild pace, pass/run, pressure, scramble and receiver distribution.
2. **Line continuity is combinatorial.** One returning tackle does not repair every pressure path.
3. **Game script creates dependence.** A leading favourite may drain clock; a trailing team can add yards, sacks, turnovers and garbage-time points.
4. **Turnovers and one-score records shrink.** Require pressure, decision, ball-security or coaching mechanisms.
5. **Weather is matchup-specific.** Wind, cold/heat, snow, footing and roof affect passing/kicking/tempo differently; rain is not an automatic Under.
6. **Key numbers and pushes are discrete.** Model score combinations and exact integer boundaries.
7. **Overtime matches the competition/contract.** NFL regular/postseason, NCAA and UFL rules differ.
8. **Special teams are field-position mechanisms.** Use current kickoff and return rules.
9. **Preseason is a separate phase model.** Starter quality matters only for expected reps.
10. **College availability is asymmetric.** Absence of an NFL-style report does not mean healthy.
11. **Preseason is a quarter-by-quarter unit mixture.** Freeze expected quarterback, offensive-line, skill-unit and defensive-rotation reps by phase. If rep plans are missing, widen the side and total distributions and cap unit-dependent claims; never project a starter or one reserve sample through four quarters.
12. **Reserve-sample shrinkage and explosive tails.** Pool tiny backup/deep-reserve quarterback samples toward the relevant role/competition prior. Retain coverage busts, return/non-offensive scores, short fields, long conversion drives and fourth-down/red-zone variance even when the central reserve efficiency is low.
13. **Low total does not imply close spread.** Preserve low-underdog-score and shutout branches before ranking a positive underdog cushion over the favourite.
14. **CFL possession-to-points chain is code-specific.** For Canadian football, model expected rushing workload, second-down conversion, protection/explosives, red-zone touchdown conversion and possession share under CFL downs, field and timing rules. A supported underdog-control branch can defeat both favourite and Under and must be reconciled with their ranks.
15. **Aligned current-regime uncertainty caps a favourite.** In openers and transitions, separately branch new quarterback/coordinator, protection, availability, neutral-site, weather and opponent-upgrade states. When several current uncertainties all support the favourite's ordinary kill path, a prior-season power rating, reputation or broad market direction cannot leave the favourite spread `SUPPORTED`; lower evidence or rank the robust opposing spread/total branch unless current matchup evidence resolves the conflict.
16. **New-regime uncertainty is two-sided before it is directional.** A new coach, quarterback or scheme expands drive-efficiency, pace, explosive and turnover tails. Apply a directional downgrade only after current personnel, role, protection, installation or matchup evidence identifies the sign; lack of observations alone does not suppress the offence or total.


## 5. Live state


Store score, quarter/clock, possession, ball spot, down/distance, timeouts, drive origin/count, opening/second-half possession, penalties, turnovers/short fields, fourth-down decisions, QB/line status, injuries/ejections, snap/route/carry distribution, roof/weather, and scoring type.


Recalculate remaining drives from clock, pace, timeouts, game script, field position, fourth-down aggression, onside/kneel-down branches, and competition rules.


## 6. Sources and settlement


- [NFL rules and operations](https://operations.nfl.com/rules-officiating/), NFL official injury reports, match centres and gamebooks control NFL.
- [NCAA football playing rules](https://www.ncaa.org/championships/playing-rules/football-playing-rules), official conference/school availability, schedules and gamebooks control college.
- Official UFL rules, match centres, transactions and team releases control UFL.
- NFHS/state associations control high school; CFL official sources control Canadian football.
- Government weather services and venue/airport observations control conditions.


Settle from the official final/gamebook and named stat provider. Reconcile kneel-downs, sacks, laterals, returns, defensive scores and stat corrections under the competition's conventions.


## 7. Upcoming-game research sequence


1. Freeze code/competition, current rules, regulation/OT/tie terms, phase, listed-player/action rules and candidate slate.
2. Retrieve official QB, injury/availability, roster/inactive and weather/roof facts before historical trends; refresh after the applicable inactive/availability release and just before issue.
3. Model QB/regime and line/skill exposure, expected drives/plays/field position, drive outcome probabilities, red-zone/fourth-down process, special teams and turnover/explosive tails. In preseason, do this by expected unit and quarter; in CFL, include rushing possession, second-down and red-zone conversion explicitly.
4. Preserve football's discrete scoring combinations and exact key-value/push mass. Competition-specific OT and try rules are part of the target, not a display adjustment.
5. Derive winner, total, margin and team scores from one joint score object. Props use snaps/routes/carries/targets/kicking opportunities and their own provider labels.


nflverse/nflfastR-style data is a candidate NFL play-by-play lane, not the official owner of current availability or rules and not approved for H0 until the source card passes.


## 8. SFA-AMERICAN-FOOTBALL — sport forecast algorithm


Algorithm ID: `SFA-AMERICAN-FOOTBALL`. Effective **2026-09-02**. Instantiates `GFA-2` (RULES_GENERAL.md §11) with gridiron content. Process composition only; no fitted weight, scenario weight or published probability is introduced. NFL regular season, NFL preseason, NFL postseason, NCAA, UFL, CFL and high school are separate populations with different downs, field, timing and overtime rules.


### 8.1 Blocking preconditions


| Precondition | Requirement | Failure output |
|---|---|---|
| `AM-P1` code and rules | Code, competition, current rules, downs and field dimensions, regulation, overtime and tie terms, and the phase each row settles on | `GATE-TARGET` failure; do not proceed |
| `AM-P2` quarterback | Starting quarterback with release status, backup branch, health and mobility, re-handshaken at G31 after the applicable inactive or availability release | Quarterback mixture; dependent rows cap at `FORCED RANK` / `MEDIUM-LOW` |
| `AM-P3` unit exposure | Material offensive-line combination, skill-player snap expectation, defensive front, coverage and sub-package absences, and the kicking specialists when a row depends on them | Widen the side and total distributions; cap unit-dependent claims |
| `AM-P4` preseason rep plan | For preseason, the expected quarterback, offensive-line, skill and defensive rotation by quarter | Without a rep plan, never project a starter or one reserve sample through four quarters; widen and cap instead |
| `AM-P5` college availability | Note that the absence of an NFL-style report is not evidence of health | Record the missingness code; do not infer availability |


### 8.2 Exposure chain


| Step | Output |
|---|---|
| `AM-S1` | Expected snaps, routes, carries and targets by player and by quarter, with the replacement tree |
| `AM-S2` | Expected drives for each side from neutral pace, clock state and game script |
| `AM-S3` | Starting field position from special teams, turnovers and punt/return outcomes |
| `AM-S4` | Within-drive efficiency under the current quarterback regime: early-down success, pass/run rate, play action, pressure, sack, scramble and explosive rates, trench and coverage matchups |
| `AM-S5` | Drive-outcome mapping: touchdown, field goal, no score, safety, turnover, and non-offensive score |
| `AM-S6` | Dependent tries and kicks: extra point, two-point decision by score state, field-goal range and accuracy |
| `AM-S7` | Game-script feedback: a leading side draining clock, a trailing side adding plays, yards, sacks, turnovers and late points |
| `AM-S8` | One discrete joint score object that preserves football scoring combinations, key values and exact push mass |


### 8.3 Mandatory branch set


| Branch | Content |
|---|---|
| `AM-B1` | Central drives with central efficiency for both sides |
| `AM-B2` | Explosive branch: coverage bust, long completion or long run producing points from a single snap |
| `AM-B3` | Long-drive branch: sustained conversion including fourth-down and red-zone variance |
| `AM-B4` | Non-offensive branch: return, defensive or special-teams score, and short fields from turnovers |
| `AM-B5` | Low-underdog-score and shutout branch, held explicitly before any positive cushion is ranked |
| `AM-B6` | Game-script branch: clock drain by the leader, and garbage-time accumulation by the trailer |
| `AM-B7` | Weather and surface branch, with passing, kicking, footing and tempo each signed separately |
| `AM-B8` | Overtime or tie under the exact competition and operator rules |


For preseason, `AM-B1`–`AM-B6` are constructed quarter by quarter, per unit, not once for the whole game.


### 8.4 Contract derivation map


| Contract | Queried from | Extra condition the mechanism must predict |
|---|---|---|
| Total | Sum marginal of the discrete score object | The component budget at the opponent's floor, centre and high, with `AM-B2`/`AM-B4` included |
| Spread | Margin marginal | Exact key values and push mass at integer lines |
| Winner | Margin sign | Not inferable from the total |
| Team total | Team marginal | That side's own drives and efficiency, not the game's pace |
| Quarter or half | The segment's own drive count and unit rotation | A prior segment is neither a ceiling nor a continuation rule |
| Player props | Snaps, routes, carries, targets or kicking opportunities | The provider's own definition |


### 8.5 Kill-path library


| Kill path | Defeats | Evidence origin |
|---|---|---|
| A coverage bust or single explosive play, plus sustained reserve-unit drives | A preseason Under built on low central reserve efficiency | C-PL7-AF-PRESEASON-UNIT-TAIL, §4 control 12 |
| A new coach or quarterback regime with a real upside ceiling | A directional downgrade applied because observations are few | §4 control 16, C-PL9-AF-REGIME-WIDTH |
| Several current-regime uncertainties all pointing at the favourite's ordinary kill path | A favourite spread left `SUPPORTED` on a prior-season rating or market direction | §4 control 15, C-PL8-AF-ALIGNED-REGIME |
| An underdog controlling possession through rushing workload and second-down conversion | A favourite side and an Under held simultaneously without reconciliation, particularly in CFL | §4 control 14, C-PL7-CFL-POSSESSION-CONVERSION |
| A low underdog score or shutout | A positive underdog cushion ranked above the favourite because the total is low | §4 control 13 |
| Garbage-time points from a trailing offence | An Under justified by a leading team's clock drain | §4 control 3 |
| Turnover and one-score records treated as stable ability | A side or total ranked on outcome history without a pressure, decision or ball-security mechanism | §4 control 4 |
| Competition-specific overtime supplying points or changing the endpoint | A total or spread settled under the wrong overtime rule | §4 control 7 |


### 8.6 Sport ordering overrides


1. New-regime uncertainty is two-sided before it is directional. A downgrade requires an identified sign from personnel, role, protection, installation or matchup evidence.
2. In preseason, a full-game central projection may not be a decisive term in the G23.1 marginal-likelihood comparison. Winning states are counted quarter by quarter and unit by unit.
3. Key values and push mass are part of the contract geometry at G4, not a display adjustment. An integer spread or total row records its push interval before ranking.
4. Special teams and non-offensive scores remain in the total's `states` count even when the offensive centre is low.
5. Raw points, one-score records, turnover margin and defensive touchdowns are `E — diagnostic only`.


### 8.7 Pre-issue checklist


1. `AM-P1`–`AM-P5` status printed, with the quarterback release status and inactive-report time.
2. Competition and matchup drive baseline stated before any line.
3. Expected drives, starting field position and drive-outcome mapping written before any points figure.
4. All eight `AM-B*` branches represented; in preseason, by quarter and unit.
5. Component budget solved at the supplied total; push mass recorded at every integer line.
6. Kill-path rows selected from §8.5 and reconciled against the issued order.
7. Overtime and tie treatment stated for every total, spread and winner row.
8. Quarterback, inactives, roster and weather refreshed at G31 before the view is appended.
9. Recency block complete per §8.8: L5/L10/L15/L20 for both sides and for head-to-head, continuity count stated, trend verdict per metric, unique-event de-duplication done.
10. Environment block complete per §8.9: Roof/dome state and kick-window wind gusts and direction recorded against stadium orientation.
11. `REFERENCE_BASE_RATE`, exact threshold, population and denominator recorded for every supplied row per §8.10 as a descriptive diagnostic only; no reference-band, trend or slot-frequency adjustment may move an ordinal (G23.1).
12. Extra-condition support audit (G24) recorded for every handicap, team-total and cushion row; no retrospective contract-family penalty is applied.
13. Separation budget (G20.1) solved for every margin, handicap and cushion row by quarter and by remaining possession count, with reserve-unit, explosive-play and non-offensive scoring states held separately.
14. Rank-1 implied-target interval (G25.1) stated in the unit of every other supplied line, each remaining row classified `COHERENT`/`PARTIAL_OVERLAP`/`DISJOINT`, and every aggregate budget re-solved conditional on the Rank-1 state.
15. Winner-and-cushion reconciliation (G30.1) whenever Rank #1 is an underdog cushion, with the outright-win and narrow-loss branch ordering stated. Example separation kill path for this sport: a late explosive or non-offensive score.
16. Deficit attribution (G14.1) recorded for every weak, absent, returning or small-sample participant: which side's distribution moved and through which exposure step.


### 8.8 Recency, head-to-head and trend windows


Implements `GFA-2` step G13.1 (RULES_GENERAL.md §11.3B) and runs at that point in the algorithm, not at the end. Retrieval of L5/L10/L15/L20 for both sides and for the head-to-head series is mandatory; a window that does not exist is recorded with its true count and a missingness code.


Populate one windowed table per side with these metrics, and one head-to-head table:


| Window metric | Content |
|---|---|
| Drive efficiency | Expected points added per play and early-down success rate, opponent-adjusted |
| Pace and volume | Drives per game and neutral situation pace |
| Explosives and pressure | Explosive-play rate, pressure and sack rate for and against |
| Conversion | Third and fourth-down conversion and red-zone touchdown rate |
| Quarterback window | The starting quarterback's own last 5/10/15/20 starts, and the backup's if the branch is live |


**Head-to-head continuity.** Continuity means the same quarterback, coordinators and material line. In preseason, head-to-head carries no weight at all because participation is a rotation decision, not a contest.


**Descriptive recency windows (G13.1; revised 2026-09-17).** Retrieve L5/L10/L15/L20 and continuity-qualified H2H with unique-event counts. These windows overlap. Monotonicity and dispersion among their averages are not a statistical trend/noise test. Report direction descriptively; estimate recency decay and opponent/regime effects using time-ordered validation. See SCORING_AND_VALIDATION section 5.


**De-duplication.** The windows overlap by construction and share matches with the head-to-head and venue series. Shrink from unique underlying events under G9; never treat L5, L10, L15 and L20 as four confirmations.


### 8.9 Environment and conditions


Implements `GFA-2` step G15.1 (RULES_GENERAL.md §11.3C). Venue classification for this sport is normally **OUTDOOR unless the venue has a dome or a closed roof**.


| Field | Use in this sport |
|---|---|
| Wind speed, gusts and direction | Kicking, deep passing and field-goal range; resolved against stadium orientation. Gusts matter more than mean speed for kicking |
| Roof and dome state | Official club or venue source |
| Hourly precipitation and temperature | Footing, handling and tempo; rain is not an automatic Under |
| Surface | Turf or grass, from the official venue source |


Failure to obtain the match-window forecast for an outdoor or open-roof event yields `WEATHER_NOT_AVAILABLE`, widened total and margin distributions, and a `LEAN` cap on every weather-dependent row. No factor above carries an automatic total direction.


### 8.10 Base-rate anchors and derived stat lanes


**Anchoring (G12.1).** Anchor spreads on the frequency of covering at that number, respecting the key values at 3 and 7 and their push mass, and totals on the competition scoring environment for that phase.


StatMuse is an accepted research accelerator for this sport under DATA_SOURCE_REGISTER.md §18, using the verified query patterns recorded there. Every returned row is date-checked and reconciled against the official league source before it is decision-driving, and StatMuse never controls participants, availability, rules, state or settlement.


**Derived and low-salience fields that are available and routinely skipped:**


| Field | Note |
|---|---|
| Kicker range and recent attempt distribution | Interacts directly with the wind vector |
| Starting field position and special-teams net | Feeds `AM-S3` and the `AM-B4` non-offensive branch |
| Rest, bye, short week and time-zone travel | Entered through a named mechanism |
| Snap counts by unit | Required for preseason quarter-by-quarter mixtures |


## 9. Sport and competition rules reference


Added 2026-09-04; last reviewed 2026-09-04. Standing reference for the rules of American/Canadian football and the competition-specific rules of every gridiron competition in the prediction logs. Supports `AM-P` identity and §6 settlement; introduces no rate, weight or ordering rule. Where a 2026 rule is cited it is the rule in force for the 2026 seasons the current log covers.


**Maintenance (RULES_GENERAL.md §3, `G2`).** Before the first card of a new NFL/CFL/UFL season, a new preseason, a new college-football season, or a new bowl/playoff cycle, re-verify the overtime rule, the kickoff rule, the playoff/CFP/FCS-bracket format and size, roster rules, and any new playing-rule package against the league/NCAA source, and update this section **before** issuing the card — the NFL and NCAA change rules every offseason (kickoff, OT, CFP field size, two-minute warning). The first time a new gridiron competition is forecast, document its full rules here first.


### 9.1 Universal gridiron rules


**Objective.** Two teams. The offence has a set number of **downs** (plays) to advance the ball **10 yards** for a new set of downs; failing that, possession turns over. Score by **touchdown** (6, ball into the opponent's end zone), **extra point** (1, kick after a TD) or **two-point conversion** (2, a play from close range after a TD), **field goal** (3, a kick through the uprights), or **safety** (2 to the defence, offence tackled in its own end zone).


**Structure of play.** The ball is put in play by a **snap**. A play ends when the ball-carrier is tackled/down, goes out of bounds, scores, or an incomplete pass. A **play clock** (40 seconds, or 25 after certain stoppages) limits time between plays. The team on offence may **punt** (kick possession away, usually on 4th/3rd down) or attempt a field goal.


**Turnovers.** Interception (defence catches a pass), fumble recovery (loose ball recovered by the defence), turnover on downs (offence fails to gain 10 yards), or a blocked/missed kick.


**Game clock.** Four quarters. The clock runs during play and between many plays, but **stops** on incomplete passes, out-of-bounds (rules vary — see §9.2), scores, penalties, timeouts, change of possession (temporarily), and the two-minute warning. Each team has **three timeouts per half**. This stop-start structure is why the number of **possessions** — not raw time — is the exposure unit (`AM-S1`).


**Penalties.** Enforced in yards (5, 10 or 15) and sometimes an automatic first down or loss of down. Pre-snap (false start, offside, delay of game), during the play (holding, pass interference, block in the back), and dead-ball / personal fouls (unnecessary roughness, unsportsmanlike, **targeting** in college → ejection).


**Overtime.** Rule-set-specific (§9.2) — this is a major settlement variable. A full-game bet **includes overtime** unless the operator says "regulation only."


### 9.2 Rule-set differences — NFL vs NCAA vs CFL vs UFL


| Element | NFL | NCAA (FBS/FCS) | CFL | UFL |
|---|---|---|---|---|
| Players per side | 11 | 11 | **12** | 11 |
| Downs to make 10 yards | 4 | 4 | **3** | 4 |
| Field | 100 yд + two 10-yд end zones; 53⅓ yд wide | Same as NFL; **wider hash marks** | **110 yд** + two **20-yд** end zones; **65 yд** wide | NFL dimensions |
| Goalposts | Back of end zone | Back of end zone | **On the goal line** | Back of end zone |
| Play clock | 40 / 25 sec | 40 / 25 sec | **35 sec**, drops to **20** inside the last 3 min of a half (2026) | 35 sec |
| Pre-snap motion | One player, moving laterally/backward at the snap | One player, not toward the line at the snap | **Multiple backs may run full-speed toward the line** ("the waggle") | Motion allowed; NFL-style |
| Catch (feet in bounds) | **Two feet** | **One foot** | One foot | One foot |
| Clock after a first down | Runs | **Runs** (since 2023), except last 2 min of each half | Runs | Runs |
| Clock after out of bounds | Stops until snap in the last 2 min of half / 5 min of Q4; otherwise restarts on the ready | Stops, restarts on the ready except last 2 min of each half | **Stops** (Canadian rule keeps the clock stopped more) | NFL-style |
| Two-minute warning | Yes, each half | Yes, each half (added 2024) | **Three-minute warning**, each half | Yes |
| Pass interference | **Spot foul** (defensive) | **15-yard** maximum (defensive) | Spot foul | 15-yard max |
| Kickoff | Dynamic kickoff; touchback to the 35 (to the 20 if kicked from midfield out of bounds, 2026); onside can be **declared any time** (2026) | Fair catch inside the 25 or touchback → ball at the **25**; touchback to the 25 | Kickoffs from the 35; **no fair catch** — the "rouge"/single point applies | Modified — no traditional onside; a 4th-and-12 "scrimmage" alternative |
| The "rouge" (single point) | No | No | **Yes** — 1 point if a kick (punt/missed FG/kickoff) is not returned out of the end zone | No |
| Overtime — regular season | One **10-minute** period; **both teams get a possession** even after a first-drive TD; a tie stands if still level (2025 rule) | See §9.3 — 25-yard-line possessions, then 2-point shootout; **no ties** | Two possession series from the opponent's 35; 2-point converts mandatory from OT2; regular-season OT can end in a tie | 25-yard-line possession shootout, best-of-3 rounds |
| Overtime — playoffs | **15-minute** periods, both possess, repeated **until a winner** | Same as college regular season (no ties) | Same format, played until a winner | Played until a winner |
| Roster (game day) | 53 roster / 48 active | 85 scholarship (FBS) / 63 (FCS); large travel roster | 45-ish active + practice roster; **national vs global player ratio rules** | ~50 |
| Regular-season length | 17 games + 3 preseason | 12 games + conference title game + bowls/CFP | 18 games | 10 games |


### 9.3 NCAA college football overtime (FBS and FCS — same rulebook)


- **1st OT:** each team gets one possession starting at the opponent's **25-yard line**. Touchdown → a PAT kick **or** a two-point try. Highest score after both possessions wins; still tied → next OT.
- **2nd OT:** same, but after a touchdown the **two-point try is mandatory**.
- **3rd OT and beyond:** teams **alternate two-point conversion attempts** from the 3-yard line only — no more full possessions. First team to out-score the other in a round wins. This makes long college OT games a **rapid, high-variance** scoring environment — a very different total-scoring regime from regulation.
- Applies identically to bowl games and the College Football Playoff.


### 9.4 NFL


**Structure (2026).** 32 clubs, AFC/NFC, four divisions each. **17-game** regular season (+ 3 preseason). **Playoffs:** 7 teams per conference — 4 division winners (seeded 1–4) + 3 wild cards (5–7). **The No. 1 seed gets a first-round bye**; Wild Card round is 2v7 / 3v6 / 4v5; then Divisional, Conference Championship, and the **Super Bowl** at a neutral site. Home team = higher seed at every round except the Super Bowl.


**Overtime.** Regular season: a single **10-minute** period; since 2025 **both teams are guaranteed a possession** (a first-possession touchdown no longer ends it); if still tied after 10 minutes the game is a **tie**. Postseason: **15-minute** periods, both possess, and play continues until someone leads at the end of a period.


**2026 rule changes.** Onside kick may be **declared at any point** in the game (no longer 4th-quarter-trailing only); a touchback on a kickoff **from the 50-yard line that goes out of bounds** is spotted at the **20** (deep in-bounds kicks otherwise go to the 35); receiving-team setup-zone alignment eased (5 on the line, 4 in the setup zone); league may consult on missed disqualification fouls.


**Preseason.** Three games. Starters play limited, escalating snaps (often none in Week 1, a quarter or two by Week 3); **outcomes are close to coin-flips** and depth-chart-dependent. `SFA-AMERICAN-FOOTBALL` treats preseason as a snap-count mixture, not competitive form (§8.3, `AM-B` preseason branches). No overtime is played in the preseason — a tie stands.


**Settlement (NFL).** Full-game spread/total **includes overtime**. A game is "official" once it starts for most books but individual-game markets may void on postponement. Player props: OT counts unless the provider says otherwise. Team totals and the moneyline include OT; the **regular-season tie** pushes the spread at "pick" and settles the moneyline as a push / "tie no bet" depending on the book.


### 9.5 NCAA — FBS and FCS


**Same playing rules** (NCAA football rulebook); the divisions differ in **postseason** and **scholarship limits**.


- **FBS (Bowl Subdivision):** ~134 teams in ten conferences. Season = 12 games + conference championship games. Postseason = **bowl games** plus the **12-team College Football Playoff** (2024 onward; **12 teams for 2026**, straight-seeded from the CFP committee rankings — the **four highest-ranked** teams get first-round byes; conference champions get automatic bids but **not** guaranteed a top-4 seed; seeds 5–8 host first-round games vs 12–9). Examples in the log: "NCAA FBS — 2026 regular season opener / Aer Lingus College Football Classic" (a neutral-site opener in Dublin).
- **FCS (Championship Subdivision):** ~128 teams. Postseason = a **24-team single-elimination bracket**; the **top 8 seeds get a first-round bye**; culminates in the FCS National Championship. Conferences in the log: MEAC, SWAC (which send their champions to the separate **Celebration Bowl** rather than the FCS playoff), Northeast Conference. The **MEAC/SWAC Challenge** is a season-opening showcase game, not a playoff fixture.
- **Neutral-site "Classic" games** (Aer Lingus College Football Classic, MEAC/SWAC Challenge) are regular-season games that count toward records and bowl/playoff eligibility; no OT distinction.


### 9.6 CFL (Canadian Football League)


**Structure.** 9 clubs, East and West divisions. **18-game** regular season (June–October). **Playoffs:** top three per division (plus a **crossover** — a fourth-place team from one division can take the other division's third seed if it has a better record). Division Semi-Final → Division Final → the **Grey Cup** (championship).


**Canadian rules (vs NFL — see §9.2).** **12 players**, **three downs**, a **110 × 65-yard** field with **20-yard end zones**, goalposts **on the goal line**, unlimited backfield motion toward the line at the snap, **no fair catch** (with a 5-yard no-yards halo around the returner), **one foot in bounds** for a catch, and the **rouge** (single point) for an unreturned kick into the end zone. Three downs and the wide field make the CFL a **higher-tempo, more pass-heavy, more field-position-driven** game than the NFL — do not transfer NFL drive-efficiency or scoring baselines.


**Roster ratio.** CFL rosters must carry a minimum number of **Canadian ("national") players**, with limits on **American ("global"/international)** starters — this constrains roster construction and depth in a way with no NFL analogue.


**Overtime.** Not sudden death: each team gets a possession from the opponent's **35-yard line**; from the **second** OT round a **two-point convert is mandatory**; regular-season games may still **end in a tie** after one full round if level; playoff games continue until a winner.


### 9.7 UFL (spring league — in scope per README, not yet in the log)


A single spring league (2024 merger of the USFL and XFL). NFL-style 11-a-side, 4 downs, but with distinct rules: a **three-point** distance option is not used, there is a **two-forward-pass** rule (a second forward pass allowed from behind the line if the first is also behind the line), a **3rd-and-long "scrimmage kick" alternative to the onside kick** (4th-and-12 from your own 28), a **defensive PAT/two-point return** for points, a shorter play clock, and a 25-yard-line overtime shootout. 10-game season, then playoffs and the **UFL Championship**. Its own scoring environment — keep a separate population.


### 9.8 Identity checklist (gridiron)


Resolve before any rate work: **league and therefore rule set** (downs, players, field, motion, catch rule, clock rules); stage (**preseason** / regular season / conference title / bowl / playoff / Grey Cup / championship) and whether starters play a full game; the **overtime rule** and whether the contract includes overtime; whether a **regular-season tie** is possible (NFL, CFL — yes; NCAA, UFL — no); playoff seeding/bye structure if the card touches qualification; and the operator's postponement/abandonment rule. Neutral-site "Classic" and "Challenge" games are ordinary regular-season fixtures.


## September 5 cross-sport process inheritance


L-068–L-071 in RULES_GENERAL §12 apply to this SFA through quarter/drive score budgets, actual personnel snaps and special-team scoring. Validate arithmetic, propagate failed evidence caps, make both sides’ material winning states evaluable and keep source identity/field definitions explicit. No new completed game in this sport was available in the current cohort; no sport-specific empirical improvement or parameter change is claimed.


## September 6 settlement learning — cross-sport gates instantiated


No American-football card was settled in the `P-294`–`P-305` cohort. The v3.7 gates are instantiated here so that NFL, college, UFL and CFL cards carry the same disclosures.


**Sport-native tail example.** An American-football total is a **drive-count × points-per-drive** product, and the two terms move in opposite directions in the two states that matter most: a run-heavy blowout *reduces* drive count while raising points-per-drive, and a shootout raises both. **Define "drive" and "drives allowed" consistently first** (a possession that starts on a turnover or a short field is a different scoring-rate environment than one starting after a punt from your own 20; use the same definition for both sides' L10 figures, and record it). The tail budget is computed on both terms, not on a points total: hold each side's second-highest L10 points-per-drive against the opponent's median drives allowed, then repeat with the drive counts swapped, and print both. **Correction, 2026-09-06(d):** the original QB-only framing for `G14.2`'s bench analogue was too narrow — offensive- and defensive-line rotation and unit-level substitution matter for drive count and points-per-drive at least as much as the backup quarterback; record both. The historical CFL failure recorded at `P-150` (Montreal `-6.5` and `Under 60.5` both lost to a 44–28 Winnipeg possession-control win) is the origin case for treating possession share as a scoring-rate input rather than a game-script narrative.


**Special-teams and defensive scoring** are a separate additive term with their own rate and belong in the tail budget explicitly — a defensive/special-teams touchdown adds points without consuming a drive, so it breaks the drive-count model and is the single most common way a well-reasoned `Under` fails.


**Path geometry.** A first-quarter or first-half `Over` at a low threshold is `UNION_LOW_THRESHOLD` with `N` = expected drives in the interval. A full-game `Under` is `INTERSECTION_CONSTRAINT` across four quarters plus the overtime branch, which in NCAA and NFL formats carries a materially different scoring rate under `G22`.




### Cross-sport gates instantiated here (v3.7)


| Gate | Sport-native instantiation |
|---|---|
| `G10.2` settlement-source pre-registration | NFL and NCAA settle from the official league/NCAA box score; ESPN's `football/<league>/summary` is the structured corroboration lane. UFL/CFL need their own named official endpoint. |
| `G14.2` coaching / bench / rotation record | Record the head coach and coordinators where a change has occurred inside five games, the inactives list, and the QB depth chart — the bench-depth analogue in this sport is almost entirely the backup quarterback. 90-minute inactives, starter notices, and workload limits verified across accredited beat reporters or official team media releases under Control `S-1 Rev 2` qualify as `PROJECTED_BEAT_VERIFIED`, satisfy `G14.2`, and do not block Rank #1. |
| `G20.2` distributional tail audit | Derive tail and boundary mass from the **same frozen American-football joint score distribution**, including drive/play opportunity, QB/offensive-line/skill availability, EPA/success, turnover and field-position branches, pace/game state and overtime/rules era. Historical order-statistic stress sums are superseded as active gates. |
| `G21.1` exact target geometry | Map every supplied target to its exact settlement event and derive WIN/PUSH/LOSS from the same frozen sport-native PMF/CDF or coherent branch mixture. Historical path-count/category labels have no mandatory ordinal effect. |
| `G26.1` no universal separation floor | Reference rates and `rank_gap` are descriptive only. **No 40–60% or other pooled probability band can disqualify Rank #1.** Rank from exact marginal likelihood plus robustness/evidence uncertainty. |


**Pre-issue checklist additions (this sport):** settlement endpoint named per row; coaching/bench/rotation record for both sides with missingness codes; tail-budget sums printed against every total line; path-geometry class and `N` printed for every total and phase-total row; separation-floor result stated for Rank #1.


Full narrative and evidence: [`archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md`](archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md). Controlling gate text: [`RULES_GENERAL.md` §13](RULES_GENERAL.md).


## September 5 implementation after freeze confirmation


**ACTIVE REQUIRED PROCESS — MDS-2026.09.05-v3.6 / L-068–L-072.** Apply the shared native-score arithmetic, final-role/exposure gate, both-side score/separation budgets and source-field checks to drives, possessions and quarterback/line roles. This audit supplies no new American-football-specific coefficient evidence.


At final delivery, record the preferred total direction for each exact target, the strongest evidenced failure path for ranks #1 and #2, and whether both can win under the stated joint scenario. Rank by supported marginal likelihood; do not promote an opposite pick solely to manufacture one O/U win. At settlement, keep all issued wins/losses, including defective reasoning, in the applicable historical scorecard and review failed #1/#2 and preferred totals.


[Eligibility policy](PERFORMANCE_ELIGIBILITY_POLICY.md): non-live history is user-confirmed frozen pre-game; explicit live-issued views stay separate. These process repairs are implemented now. Numerical weights and predictive-lift claims need a later frozen comparison; historical origin games do not supply those completions.


## 2026-09-06(f) — settlement and retrospective addendum


P-309 Under won although both printed team-score corridors missed low. Separate offensive yards/drives, non-offensive touchdowns, field position and finishing. Gardner-Webb had 438 yards despite scoring 13; do not label the offence ineffective solely from points. The recorded storm risk was knowable, its exact delay and late interception were not. No weather coefficient or universal Under rule.


Full frozen ranks, actual drivers, knowability and smallest fixes: [PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md). Reinforcement only; METHOD v4.0 remains controlling and no new predictive weighting is promoted.


## 2026-09-09 — cross-sport controls instantiated here (`G-L1`, `G-L2`, `G-L7`, `G-L8`)


No American-football card was issued in the `P-333`–`P-344` cohort. The four cross-sport requirements adopted from it (`RULES_GENERAL.md` §§16.5(a)–(d), full evidence in `PREDICTION_LOG_COMBINED_3.md` §"2026-09-09") apply to this sport from the next card. All four are **disclosure/retrieval requirements — no fitted weight, no ordinal bar** (`L-087`).


| Cross-sport control | American-football instantiation |
|---|---|
| **`G-L1` §16.5(a)** — enumerate outcome-state families with explicit mass | Enumerate the **margin families** (favourite by 17+ / 9–16 / 4–8 / within a field goal / underdog win) and the **total families** in points, each with an explicit mass summing to 1. Because scoring is quantised in 3s and 7s, state the families as **drive-count × points-per-drive** combinations rather than a smooth corridor, and locate the supplied line against the modal family. Every current-evidence §8.5 kill path — including **non-offensive touchdowns, special-teams scores and turnover-driven short fields**, which `P-309` showed can decouple points from yardage — must appear as a weighted branch, not a sentence. Print a representative Rank-#1 final score and check it against the spread, the total and any team-total row. |
| **`G-L2` — declared uncertainty model** | State the prior and scenario probabilities. Symmetric uncertainty around an unchanged prior affects width; hierarchical shrinkage or asymmetric scenarios may change both mean and variance. Regenerate all dependent probabilities; unsupported directional adjustments remain prohibited. SCORING_AND_VALIDATION section 5 controls. |
| **`G-L7` §16.5(c)** — aggregate-to-disaggregate retrieval | Do not let a season passer rating, a yards-per-game figure or a "last N games" summary carry directional weight while the **game log and snap counts** are available. Print the **per-game log** for the decision-relevant window and state whether a run is front-loaded, back-loaded or uniform. For a returning player, print the **practice-participation ladder** (DNP / limited / full, by day) — the direct analogue of the rehab pitch-count ladder that decided `P-335`. Quantify **every skill player above roughly 50% offensive snaps**; a name in a "leaders include…" phrase without a number is `AGGREGATE_ONLY` and caps the dependent total/margin rows. |
| **`G-L8` — distribution coherence** | Derive each total/spread probability from the exact joint PMF/CDF and settlement endpoint, with push mass. Absolute normalised distance does not order probabilities across different distributions. No missing width or realised result justifies an invented probability. |


## 2026-09-11 — cross-sport controls instantiated here (`G-L9`, `G-L10`, `G-L11`, §16.8)


No American-football card in the `P-345`–`P-371` import. From the next card ([`RULES_GENERAL.md` §§16.5(e)–(g), §16.8](RULES_GENERAL.md)):


| Control | American-football instantiation |
|---|---|
| `G-L9` §16.5(e) | Itemise the complement of a spread across the key-number families (a field goal, a touchdown, 10) and the named paths — turnover margin, a backup quarterback, special-teams scores, late garbage-time touchdowns. |
| `G-L10` §16.5(f) | A favourite spread + Over pair is positively coupled when the favourite's offence creates the margin; an underdog spread + Under pair is positively coupled through a slow, defensive game. Print the sign. |
| `G-L11` §16.5(g) | Red-zone touchdown rate, third-down conversion and turnover rates over three or four games are small samples; print their standard error before they carry direction. |
| §16.8 | Inactive lists are published before kick-off; `NOT_RETRIEVED` after publication is a `RETRIEVAL_MISS`. |




## 2026-09-12 algorithm corrections and retrospective integration


Apply section 16.9 to joint possessions, touchdowns/field goals, team totals, margins and overtime scope. Garbage-time pace, late stops and trailing-team aggression can change dependence in either direction. Record active/inactive lists, projected versus confirmed starters, depth/reserves and coaches separately. Completion percentage has attempt exposure; points per drive and yards per play need different uncertainty models. No new American-football result was settled in this pass; validate any predictive weighting prospectively.


For every supplied row, use exact target probabilities from a coherent joint distribution; handle push/void/censoring explicitly, avoid overlapping adverse-state counts, and report JOINT_UNQUANTIFIED with bounds if the dependence is not specified. Separate issued-time participant capture, later recovered evidence, source accuracy by field, observed mechanism, and unverified causal interpretation. Keep one preferred O/U direction per distinct target and report the top-two denominator honestly. Shared correction and methodology sources (`audit_2026-09-12/rule_corrections.md`, not present in this repository). All current log observations remain learning-only and not performance-eligible.




## 2026-09-15(b) settlement learning — `P-373`–`P-423` import


Learning-only; disclosure/process changes only — no coefficient or ordinal bar (`L-087`). Evidence and tables: [`PREDICTION_LOG_COMBINED_3.md` §"2026-09-15(b)"](PREDICTION_LOG_COMBINED_3.md). Cross-sport rule: `RULES_GENERAL.md` §16.10 (`G-L12` margin centre/width; fixture identity; official-record derivative settlement).


**Cards:** P-376 (49ers +3.5 WIN, won 27–7), P-412 (Falcons +6.5 LOSS by exactly 7), P-413 (Colts +3.0 and Under 48.5 LOSS, Ravens 41–23), P-414 (Texans +1.5 and Under 44.5 LOSS, Bills 36–31), P-422 (Broncos +2.5 LOSS, Chiefs 31–10). Potential winners 4 of 5. Rank #1 1 W / 4 L — every loss an underdog cushion whose favourite won by 5–21.


### What went right (keep it)
- Winner identification (4 / 5) and the injury/inactive ladders (P-413, P-414, P-422).
- P-413 printed the push mass at exactly 3 (8%).


### What went wrong, linked to earlier lessons
1. **Uncertainty put into the centre.** Control 16 ("new-regime uncertainty is two-sided") was cited, but P-413 (BAL +1.3), P-414 (BUF +0.7) and P-422 (KC +1.0) all centred within ~1 point of pick'em beside 53–56% winner labels. Actual margins +18, +5, +21 → `G-L12`.
2. **Margin width too narrow.** ~10.5 points against a published NFL spread-to-result SD of about 13.9 (Stern 1991) — both tails under-massed.
3. **A hand-picked window as the prior.** P-413 used the Colts' first 10 games of 2025 with a healthy quarterback (57.6% scoring possessions) — `L-011`/`G17`.
4. **One thesis, two rows.** P-413 and P-414 ranked an underdog cushion and an Under on the same "controlled, defensive game" idea; both pairs lost together (`G-L10`).
5. **No margin table at all** on P-412 (23-line card), which then lost at exactly 7.


### Structural control additions
17. **Margin prior and width.** Print the margin prior (prior-season point differential adjusted for quarterback status) and a width no narrower than the published residual SD unless the card shows why; Week 1 widens, it does not centre toward zero (`G-L12`).
18. **Key numbers.** Every NFL handicap row prints the exact masses at 3 and 7 from its margin table; a card without a margin table caps its handicap rows at `FORCED RANK`.
19. **Prior-season unit ratings in a new season are width.** A defence's prior-season rating may not set both a margin compressor and a total suppressor without current-season evidence (P-414: 67 points).


### Kill-path additions
| Kill path | Defeats | Origin |
|---|---|---|
| Favourite separation after a near-pick'em centre (new QB/HC/OC held as centre shift) | Small underdog cushions | P-413, P-414, P-422 |
| Exactly-7 result | +6.5 cushions | P-412 |


## 2026-09-16 settlement learning — external variant C′ facts verified (`P-412`, `P-413`, `P-414`, `P-422`)


Learning-only; disclosure only (`L-087`). Cross-sport rules: `RULES_GENERAL.md` §16.11. Facts verified at the ESPN `football/nfl` summaries on 2026-09-16.


### What the verified box scores add
- **P-412 (Steelers 20–13 Falcons).** T.J. Watt's **35-yard interception-return TD at Q4 14:05** turned 13–10 into 20–10; Atlanta's later field goal left the final margin at exactly 7. Cooper Rush went 12/22 for 143 yards with **2 INT and 4 sacks**. The +6.5 was decided by a non-offensive score under a backup quarterback.
- **P-413 (Ravens 41–23 Colts).** Baltimore gained 506 yards at 7.9 a play. Jackson went 17/25 for 324 yards; Henry ran 24 times for 144 yards and 3 TD; Flowers scored on a 54-yard catch. This was the intact-star explosive branch.
- **P-414 (Bills 36–31 Texans).** Buffalo gained 409 yards on 52 plays (7.9 a play) with 0 turnovers; Houston committed 2.
- **P-422 (Chiefs 31–10 Broncos).** Denver gained 176 yards at 3.7 a play; Nix went 17/28 for 131 yards with 1 INT and 4 sacks. Walker ran 23 times for 173 yards, including a 60-yard TD. A 21-point cover inside a 41-point Under.


### 2025 regular-season reference base rates (`REFERENCE_BASE_RATE`, descriptive)
Computed 2026-09-16 from ESPN `scoreboard?dates=2025&seasontype=2&week=1…18` plus `summary` `scoringPlays` (272 completed games; 14 overtime games; 1 tie).


| Quantity | Value |
|---|---|
| Final margin exactly 3 | 15.1 % |
| Final margin exactly 7 | 9.6 % |
| Margin 0–6 / 7–13 / 14+ | 40.1 % / 24.6 % / 35.3 % |
| Mean / median absolute margin | 11.15 / 8 |
| Mean total points (SD) | 46.0 (13.8) |
| Non-offensive TDs (interception, fumble, punt, kickoff and blocked-kick returns) | 59 — **0.217 a game; at least one in 18.8 % of games** |


Definitions follow ESPN `scoringPlays[].type.text`; "Sack Opp Fumble Recovery" (12) and safeties (10) are excluded. These are league-wide unconditional rates. A card still conditions on its own game (quarterback, turnover and sack rates), and the rates are width references, not coefficients.


### Structural control additions
20. **Non-offensive score branch.** Any handicap row within one score of the printed centre carries "defensive or special-teams TD" as an explicit branch mass. Anchor it on the reference rate above, and adjust only with named evidence (backup quarterback, sack or turnover rates). Origin: P-412; C′ candidate `C-P407-23-AF-NONOFFENSIVE-SPREAD`.
21. **Favourite covers inside the Under.** When a handicap and a total are both in the top two, print P(favourite covers ∧ Under) and P(underdog covers ∧ Over) from the joint margin × total table. Origin: P-422 (KC by 21, total 41) and P-412 (PIT by 7, total 33); C′ candidate `C-P407-23-AF-FAVOURITE-UNDER-SEPARATION`.


Control 18 now cites the reference key-number masses above as its default when no current-season table exists.


### Kill-path additions
| Kill path | Defeats | Origin |
|---|---|---|
| Backup-QB interception returned for a TD | Underdog cushion at 6.5–7.5 | P-412 |
| Favourite run game + opponent offence under 4 yards a play | Underdog cushion, while the Under also wins | P-422 |


## 2026-09-17 — cross-sport controls instantiated here (`G-L17`–`G-L20`)


No American-football card in this import. **`G-L17`:** `P-413` and `P-414` are the origin recurrences — an underdog cushion and an Under built on one 'controlled game' thesis; print `P(¬R1 ∧ ¬R2)` and name the state, alongside control 21's favourite-covers-inside-the-Under branch. **`G-L18`:** print each side's own points marginal before ranking a game total. **`G-L19`:** regular-season ties are possible (one occurred in the 2025 reference season, 272 games); a winner family that sums to 1 over two teams is incomplete. **`G-L20`:** a current-regime same-venue comparable that already cleared the line gets explicit mass.


Evidence and cohort audit: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17"](PREDICTION_LOG_COMBINED_4.md); rules in `RULES_GENERAL.md` §16.12.


## 2026-09-17(b) — cross-sport controls instantiated here (`G-L21`–`G-L24`)


**G-L24 in AMERICAN FOOTBALL:** derive the exact signed-margin distribution under the competition endpoint, including draw, key-value and push masses. Pooled league bands are uncertain references, not mandatory matchup probabilities or rank prohibitions. Missing pooled bands do not invalidate a complete conditional joint distribution. NFL 13.9 is a historical residual benchmark, not a width floor. **`G-L21`:** `P-413`/`P-414` are already the origin recurrences; extend the printed failure mass past the top two whenever a cushion, an Under and a team total all rest on one 'controlled game' thesis. **`G-L22`:** the supplied NFL slate is almost always two forced pairs (spread and total), so the row tally is arithmetic — report the preferred side of each pair as the trial, and derive the push mass at whole-number spreads and totals rather than asserting it. **`G-L23`:** settle from a feed carrying drive charts, turnovers and player exits with the game clock, not a recap.


Evidence and cohort audit: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17(b)"](PREDICTION_LOG_COMBINED_4.md); rules in `RULES_GENERAL.md` §16.13; bands and base rates in [`BASE_RATES_REGISTER.md`](BASE_RATES_REGISTER.md).


## 2026-09-19 — recency/rebound, social sources and the top-O/U review


`R-1` ([`RECENCY_AND_REBOUND.md`](RECENCY_AND_REBOUND.md)) applies: recent results revise an estimated **rate** through a named mechanism, never forecast a **deviation**. No rebound and no hangover adjustment is permitted in either direction. This sport's magnitudes are **`NOT_YET_DERIVED`** — the MLB figures are not transferable and must not be imported; derive them from this competition's own record before any recent-form weighting.


Source controls `S-1` (social identity: X and Reddit return no usable content; Bluesky sports handles failed identity verification 6/6) and `S-2` (press conferences are availability/role evidence, never a signed adjustment to a modelled rate) apply — `SOURCES.md` §"2026-09-19".


A loss **or push** on the card's highest-ranked over/under now triggers the same enhanced failure review as a Rank #1 loss (`METHOD.md` §7).


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — market-independent totals/line addendum


**Source priority:** NFL/competition official gamebooks, injury/practice reports, transactions and tracking/stat products; nflverse sports-statistical lanes may support historical research with lineage checks. Sportsbook/fantasy/DFS projections are prohibited.


Use drive/possession scoring distributions with QB/offense/defence/special-teams state, participant availability, rest/travel, weather and turnover uncertainty. Preseason and regular-season populations stay separate. Totals/spreads are queried only after the score/margin distribution is frozen.




<!-- ALL-SPORTS-AUDIT-LIVE-RULE-CLEANUP-2026-09-21-CR3 -->
## 2026-09-21 — all-sports audit live-rule cleanup — CR-2026.09.21-3


Current prospective override. Retain drive/play opportunity, QB/offensive-line/skill availability, EPA/success/turnover/field-position branches, pace/game state and overtime/rules era. Withdraw pseudo-tail order-statistic constructions, path-count ranking shortcuts, universal probability-band top-slot rules, one-score “due” logic and generic recent-score trend adjustments. Build one coherent American-football joint outcome distribution before querying targets.

<!-- SETTLED-ROW-REVIEW-2026-09-25D -->
## 2026-09-25(d) — track record from the full settled-row review

**Track record (`C-TRACK-RECORD`).** 12 NFL/NCAA decisions from 6 cards: won **25%** at a mean stated 0.544. The gap is −0.29, with a card-cluster interval of [−0.47, −0.12]: **over-confident**. These cards are labelled **`NO_DEMONSTRATED_SKILL`**.

- **Underdog cushions (+k.5): 1/6** at 0.554. `C-PLUS-CUSHION` applies.
- **Required on every margin row:** the G-L12 residual benchmark (about 13.9 points), and key-number masses at 3 and 7, which are `NOT_YET_DERIVED`, so they are derived before the next NFL handicap card.

Source: `research/settled_rows_2026-09-25/README.md`. The figures are hindsight on the framework's own cards, descriptive, and use card-cluster intervals. None is a coefficient (`L-087`). Controls: `RULES_GENERAL.md` §"2026-09-25(d)".


<!-- RANK-MODEL-2026-09-25E -->
## 2026-09-25(e) — the first NFL population reference, key numbers, the team baseline and the ranking model

Controls: `RULES_GENERAL.md` §"2026-09-25(e)". Evidence: `research/team_baseline_2026-09-25e/README.md`; `BASE_RATES_REGISTER.md` §7.7.

**Record.** NFL/NCAA stays `NO_DEMONSTRATED_SKILL`: 3/12 at 0.544; cushions 1/6. The losses at Rank 1 were five underdog cushions of +1.5 to +6.5 (P-412, P-413, P-414, P-422, P-472).

### (a) Sources

- **ESPN NFL scoreboard** (`…/football/nfl/scoreboard?dates=…`) and **team schedule** (`…/football/nfl/teams/{id}/schedule?seasontype=2`): the TB-1 lane (`--league nfl`).
- **NCAA:** no TB-1 lane (`NOT_COVERED`).

### (b) Reference rows (NFL 2024 / 2025, regular season, n = 272 each)

| Row | 2024 | 2025 |
|---|---:|---:|
| Home win | 0.524 | 0.536 |
| Total mean (SD) | 45.8 (13.1) | 46.0 (13.8) |
| Home margin | +1.7 | +2.2 |
| Margin SD | 14.5 | 14.2 |
| TB-1 residual width, total / margin | 13.1 / 13.7 | 13.4 / 13.6 |

**Key numbers** (previously `NOT_YET_DERIVED`; this is the G-L12 residual benchmark):

| Margin | 2024 | 2025 |
|---|---:|---:|
| P(\|margin\| = 3) | 0.136 | 0.151 |
| P(\|margin\| = 7) | 0.074 | 0.096 |
| P(\|margin\| ≤ 3) | 0.24 | 0.27 |
| P(\|margin\| ≤ 7) | 0.52 | 0.50 |

### (c) Reasoning

1. **TB-1 is the anchor.**
   - Sides: 0.231 v 0.252.
   - Totals: 0.246 v 0.254, which is marginal. **Corrected 2026-09-26(e):** the 2025 interval is [−0.018, +0.002] and 2021–2025 gave 0.2403 v 0.2423, so totals anchor on the population (`TB1_NO_RESOLUTION:total`); §0.2 governs.
   - Early season (Weeks 1–3) is flagged `TB1_EARLY_SEASON`. Its early-season result still beat the base rate (0.246 v 0.253).
2. **Cushions at their population rate.** The TB-1 underdog covered:

   | Cushion | Cover rate |
   |---|---|
   | +1.5 | 0.35–0.42 |
   | +2.5 | 0.38–0.46 |
   | +3.5 | 0.45–0.54 |
   | +6.5 | 0.57–0.60 |
   | +7.5 | 0.61–0.66 |

   Every Rank-1 cushion that lost sat in the +1.5 to +6.5 range and was stated at 0.53–0.58. That is at or above the population rate, with no receipted mechanism. Such a row is now `PLUS_CUSHION_UNSUPPORTED`, and RM-1 flips it.
3. **Key numbers.** A +2.5 or +3.5 row prints the mass at 3 (0.14–0.15). A +6.5 or +7.5 row prints the mass at 7 (0.07–0.10). These are the only places the half-point matters.
