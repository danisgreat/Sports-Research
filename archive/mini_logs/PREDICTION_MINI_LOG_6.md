# Prediction Mini Log 6

**Status:** ACTIVE LOCAL RUNNING LOG  
**Opened:** 2026-08-31 14:44 Australia/Melbourne  
**Governing method:** MDS-2026.08.31-v2.8 — qualitative champion  
**Numerical state:** NTS-2026.08.25-v0.2 — Stage 0 / pre-fit; no fitted, calibrated or validated numerical model  
**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value state:** `NO VALUE DETERMINABLE` unless exact same-time odds/terms and a future validated probability model satisfy the value gate  
**Predecessor authority:** `PREDICTION_LOG_COMBINED.md` through canonical `P-214`  
**Canonical continuation:** starts at **`P-215`**  
**Storage mode:** LOCAL ONLY — Google Drive remains read-only  
**Running-log mode:** after every new sports prediction query, return the complete updated Markdown log  
**Retrospective mode:** **MANUAL ONLY — do not automatically perform a retrospective on the previous query unless explicitly requested**

---

## 1. Current controlling snapshot

| Field | Current value |
|---|---|
| Current framework | `MDS-2026.08.31-v2.8` |
| Latest canonical predecessor | `P-214` |
| Next canonical forecast ID | **`P-217`** |
| Live predecessor events | **0** |
| Final-event follow-up queue inherited from canonical log | P-126 field-owner result/phase + C06 corners; P-148-C02; P-149-C02 provisional; P-151-C02 provisional; P-162 provisional final; P-166 operator OT/action definition; P-176-C05; P-178-C05; P-179-C05 provisional; P-200 operator OT/SO/action definition |
| New-log event count | **2** |
| New-log open forecasts | **2** |
| New-log settled forecasts | **0** |
| New-log retrospective count | **0** |
| Probability publication | **DISABLED** |
| Numerical model status | **DESIGN ONLY / DATA BLOCKED** |
| Next process/ranking checkpoint | **60 new clean, demonstrably pre-result v2.8 event units** |
| Next sport-specific algorithm review target | **100 new clean, balanced v2.8 event units**, with useful per-sport/market/horizon slices |

The final-event follow-up queue is carried for provenance/definition continuity only. It does not block a new `P-215` forecast.

---

## 2. User-directed operating rules for this mini log

1. **Every new sports prediction query receives the next canonical `P-###` ID.**
2. **Return the complete updated running Markdown log after each query.**
3. **Do not automatically perform a retrospective on the previous query.**
4. A retrospective is added only when explicitly requested.
5. Basic settlement/state verification may be appended when directly requested or when required for queue integrity, but **no why-it-won/why-it-lost analysis, lesson extraction, or retrospective method change is added without an explicit request**.
6. Never rewrite a frozen issued forecast. Corrections, live-state updates, settlements and retrospectives are appended as new sections.
7. Google Drive is used as a **read-only reference source**. This local mini log is not uploaded to or used to edit Drive.
8. New evidence must respect prediction-time chronology. Information first known after the forecast cutoff cannot be inserted into the issued forecast rationale.
9. No guaranteed-winner, lock, calibrated-probability, expected-value, ROI or market-edge claim is permitted under the current Stage-0 state.

---

## 3. MDS-2026.08.31-v2.8 controls carried forward

These are process/coherence controls, not retrospectively fitted forecast weights.

### 3.1 Uncertainty-width before centre

Sparse evidence, a new coach/QB, early-season samples, roster change, unresolved role, small-sample starter, uncertain goalie, or similar regime uncertainty should first **widen the scenario distribution**. Shift the central direction only when a current sport-native exposure/rate mechanism justifies that shift.

### 3.2 Exact phase- and score-state role

Availability alone is insufficient. Translate participants into their actual forecast exposure:

- cricket: batting position, balls/overs, phase role;
- baseball: starter hook, batting-order slot, score-state bullpen role;
- basketball: minutes, usage, lineup phase and closing role;
- American football: QB/unit snaps, drive role and phase;
- AFL/AFLW: time on ground, CBA/ruck/forward role;
- rugby league: spine role, minutes/interchange and set organisation;
- soccer: starting/substitute minutes, role, set pieces and score-state usage;
- hockey: goalie start probability, line/unit and special-teams exposure;
- tennis: serve/return exposure, set/match-length branches and retirement terms.

### 3.3 Four-family total/margin stress grid

Every side/total slate must explicitly consider:

| Family | Total state | Margin state |
|---|---|---|
| A | Low | Close |
| B | Low | Separation |
| C | High | Close |
| D | High | Separation |

A low-total thesis is not sufficient evidence for an underdog cushion, and a high-total thesis is not sufficient evidence for a favourite cover.

### 3.4 Mechanism-to-contract alignment

Rank the contract that directly matches the researched sporting mechanism.

Examples:
- attacking dominance does not automatically imply a full-game Over;
- possession/shots do not automatically imply a winner;
- goals do not automatically imply corners;
- a low-scoring central game does not automatically imply a close spread;
- one-team scoring strength may fit a team total better than a full-game total when that market is actually supplied and researchable.

### 3.5 Small streaks are diagnostic, not controlling

Recent win/loss, Over/Under, clean-sheet, blowout, shooting, finishing, save, conversion or scoring streaks must be decomposed into:
- exposure/opportunity;
- creation/territory/possession;
- conversion/finishing;
- participant role;
- opponent quality;
- environment;
- regime continuity.

Small or unstable samples normally widen uncertainty before moving direction.

### 3.6 Extension and termination endpoints

Regulation, overtime, shootout, extra innings, DLS/shortening, declarations, rain termination, 3/4/5-set tennis branches, golden point and similar endpoints must be represented explicitly and matched to the exact contract/operator terms.

### 3.7 Named kill-path reconciliation

If a plausible ordinary failure branch is strong enough to be written in the forecast, it must affect the ranking. If it cannot honestly remain subordinate, reduce the evidence grade or change the order before issue.

### 3.8 Source-state and provider-conflict control

Official status is field-specific, not site-wide. A stale placeholder, zero-filled shell, unfinished page or impossible state must be quarantined for the affected field.

For provider disagreement:
- preserve each credible value and lineage;
- do not invent a false consensus;
- if all credible values settle the contract on the same side of the threshold, the contract may be threshold-invariant while the raw statistic remains conflicting;
- if disagreement changes settlement, keep the row provisional/unresolved.

### 3.9 Result and process remain separate

When a retrospective is explicitly requested, use:

| Label | Meaning |
|---|---|
| Result right / process right | Expected mechanism occurred and contract won |
| Result right / process different | Contract won for a materially different mechanism |
| Result wrong / process broadly right | Core process occurred but variance/conversion/settlement tail defeated it |
| Result wrong / process wrong | Pregame assumptions, evidence hierarchy or ranking logic were materially incorrect |

A single result does not promote a new forecast weight.

---

## 4. Source hierarchy for new forecasts

Use sources field-by-field:

1. official league/federation/event/team source for identity, schedule, participant state, rules and final;
2. official box score/stat provider for defined statistics;
3. government/official venue weather source where relevant;
4. specialist process/stat provider only for metrics it defines;
5. reputable reporting for context, role and chronology when official detail is unavailable;
6. aggregators/discovery sources only as corroboration unless no stronger source exists.

Always record missingness, conflicts and freshness. Do not treat website count as evidence strength.

---

## 5. Forecast construction standard

For each new `P-###` event:

1. verify exact event identity and current game state;
2. freeze request time, information cutoff, target, endpoint and complete supplied candidate slate;
3. resolve operator/OT/extra-time/retirement/DLS/action terms where supplied;
4. refresh decision-driving participants;
5. build the relevant sport-native exposure × rate corridor;
6. represent lower, central, upper and material tail states;
7. run the four-family total/margin geometry where applicable;
8. reconcile the strongest ordinary kill path;
9. derive every ranked contract from one coherent event view;
10. rank all valid supplied rows uniquely;
11. name the potential winner with its exact endpoint;
12. append the immutable forecast to this running log before delivery;
13. **do not append a retrospective for the previous query unless the user explicitly requests one.**

---

## 6. Running event index

| Canonical ID | Event | Sport | State | Rank #1 | Potential winner | Settlement | Retrospective |
|---|---|---|---|---|---|---|---|
| `P-215` | Japan vs Qatar | Basketball | PREGAME | Under 169.5 | Japan winner | OPEN | NOT PERFORMED |
| `P-216` | Namibia vs Zimbabwe | Cricket | PREGAME / toss not verified | Zimbabwe Under 165.5 | Namibia winner — low confidence | OPEN | NOT PERFORMED |

---

## 7. New-event append template

# P-### — [Event]

## 7.1 Event / state freeze

| Field | Frozen value |
|---|---|
| Sport | |
| Competition | |
| Event | |
| Official event ID | |
| Venue | |
| Scheduled start | |
| Australia/Melbourne start | |
| Final research refresh | |
| GAME-STATE | |
| Method | `MDS-2026.08.31-v2.8` |
| Decision-set ID | |
| Candidate origin | |
| Operator / terms | |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` unless the complete value gate passes |

## 7.2 Target and contract freeze

| Contract ID | Exact supplied contract | Endpoint / settlement geometry | Dependence group |
|---|---|---|---|
| | | | |

## 7.3 Participant / role state

| Participant / unit | Official status | Expected exposure / phase role | Forecast consequence |
|---|---|---|---|
| | | | |

## 7.4 Evidence summary

### Baseline
- 

### Current regime
- 

### Matchup / exposure
- 

### Environment / context
- 

### Source-state / missingness
- 

## 7.5 Scenario map

| Scenario family | Mechanism | Expected contract effect |
|---|---|---|
| Lower / suppressed | | |
| Central | | |
| Upper / acceleration | | |
| Material tail / kill path | | |

### Four-family geometry, where applicable

| Family | Total | Margin | Current plausibility / mechanism |
|---|---|---|---|
| Low / close | | | |
| Low / separation | | | |
| High / close | | | |
| High / separation | | | |

## 7.6 Ranked picks

| Rank | Contract | Verdict | Evidence | Main reason | Strongest kill path |
|---:|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

## 7.7 Potential winner

**[Team / player / endpoint] — [LEAN / FORCED WINNER — LOW CONFIDENCE]**

Reasoning:
- 

## 7.8 Final freeze

1. 
2. 
3. 
4. 
5. 

Potential winner: **...**

Next canonical forecast ID: **P-###**

---

## 8. Settlement template — no automatic retrospective

When settlement is requested or required for queue integrity:

| Field | Value |
|---|---|
| Official final | |
| Settlement source | |
| Contract results | |
| Rank #1 result | |
| Potential winner result | |
| Operator-definition caveat | |
| Retrospective status | **NOT PERFORMED — USER REQUEST REQUIRED** |

Do **not** add causal why-right/why-wrong analysis or new lessons here unless explicitly requested.

---

## 9. Retrospective template — use only on explicit request

| Preissue expectation | Actual driver | Difference | Knowability at issue | Process classification | Defect / success class | Linked lesson | Proposed future test |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

If Rank #1 failed, perform the deeper audit requested by the user:
- strongest pregame rationale;
- exact realised failure mechanism;
- whether it was knowable before issue;
- whether the kill path was already identified but underweighted;
- source-quality audit;
- what was right;
- what was wrong;
- market/contract geometry error if any;
- links to prior lessons/cases;
- candidate improvement only, with no retrospective weight promotion.

---

**Next canonical event:** `P-217`

---

# P-215 — Japan vs Qatar — FIBA Basketball World Cup 2027 Asian Qualifiers

## Event / state freeze

| Field | Frozen value |
|---|---|
| Sport | Basketball |
| Competition | FIBA Basketball World Cup 2027 Asian Qualifiers |
| Stage | Second Round — Group F, Window 4 |
| Event | Japan vs Qatar |
| Venue | TOYOTA ARENA TOKYO, Tokyo, Japan |
| Scheduled tip — Tokyo | 2026-08-31 19:10 Asia/Tokyo |
| Scheduled tip — Melbourne | 2026-08-31 20:10 Australia/Melbourne |
| Final state refresh | 2026-08-31 ~20:11 Australia/Melbourne |
| GAME-STATE | `PREGAME / OFFICIAL LIVE GAME NOT YET VERIFIED` — FIBA's current schedule still showed 0 live games at final refresh |
| Method | `MDS-2026.08.31-v2.8` |
| Decision set | `DS-P215-V01` |
| Candidate origin | `USER_SUPPLIED` |
| Operator / settlement terms | `NOT SUPPLIED`; full-game FIBA research geometry used, exact OT/void rules remain operator-specific |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |

## Frozen contracts

| Contract ID | Contract | Settlement geometry |
|---|---|---|
| `P-215-C01` | Qatar +34.5 | Qatar wins or loses by <=34 |
| `P-215-C02` | Japan -34.5 | Japan wins by >=35 |
| `P-215-C03` | Combined Total Over 169.5 | 170+ combined points |
| `P-215-C04` | Combined Total Under 169.5 | <=169 combined points |

The spread pair and total pair are exact half-point complements. Spread and total come from one joint score tree.

## Current participant regime

### Japan — official 12-player game roster

Japan Basketball Association confirmed:
- Yuki Kawamura
- Rui Hachimura
- Yuta Watanabe
- Joshua Hawkinson
- Keisei Tominaga
- Takumi Saito
- Yudai Baba
- Yudai Nishida
- Avi Koki Schafer
- Ryusei Sasaki
- Shinji Takashima
- Hirotaka Yoshii

Hachimura returned against Saudi Arabia and scored 29 points in 28 minutes. FIBA reported Japan's 106-78 win was built on 53% shooting, 29 assists, only 2 turnovers and 29 fast-break points. Kawamura had 9 assists, Hawkinson 21 points and Tominaga 14.

### Qatar — current federation game-window roster

The Qatar Basketball Federation listed:
- Mustafa Fouda
- Mike Lewis
- Mahmoud Darwish
- Abdullah Mousa
- Ndawi Elhaj Sidou
- Abdullah Saad
- Mohamed Hashem
- Ousmane Dieng
- Osama Arafa
- Abdulrahman Yahya
- Omar Saad
- Aladji Bobo Magassa

Critically, this current federation roster does not include Brandon Goodwin or Alen Hadzibegovic even though FIBA's season team page still lists them among Qatar's qualifier leaders. Under the v2.8 current-roster rule, those season-leader numbers are not treated as the present offensive centre.

Qatar entered after a 57-83 home loss to China.

## Baseline and current-regime reconciliation

Before this matchup:
- Japan: 5-2, 605 points for / 528 against, 86.4 scored and 75.4 allowed per game.
- Qatar: 4-3, 537 for / 529 against, 76.7 scored and 75.6 allowed per game.

Those carried-forward averages understate the current roster shift:
- Japan have a Hachimura-Kawamura-Watanabe-Hawkinson core.
- Qatar's current federation roster omits two players responsible for a major share of the season-level scoring/creation profile.

Therefore the centre shifts toward:
1. lower Qatar offensive efficiency;
2. a larger Japan separation branch;
3. a low-total/separation state in which Japan can cover while the total remains Under.

## Four-family stress grid

| Family | Total | Margin | Main mechanism |
|---|---|---|---|
| A | Low | Close/moderate | Japan control pace but Qatar avoid turnover collapse; Japan win comfortably but <35 |
| B | Low | Separation | Qatar scoring floor collapses, Japan score efficiently without needing 110+ |
| C | High | Close/moderate | Qatar shoot unusually well from three and Japan also score efficiently |
| D | High | Separation | Japan transition/turnover pressure creates 108-115+ while Qatar still reach mid/high 60s |

The strongest central family is **B: low total + Japan separation**.

Representative qualitative score family:
- Japan 101-108
- Qatar 58-67
- total 159-175
- margin 34-50

Representative central scoreline: **Japan 104-62 (166 total, Japan +42)**.

This is a qualitative corridor, not a fitted probability.

## Ranked picks

| Rank | Pick | Verdict | Evidence | Reason |
|---:|---|---|---|---|
| **1** | **Combined Total Under 169.5** | **LEAN** | **MEDIUM-HIGH** | Qatar's current roster is missing the season-profile creators Goodwin and Hadzibegovic, and they just scored 57 against China. Japan can dominate through defence, transition and efficient half-court scoring while the game still stays below 170. The Under survives both moderate-margin and many blowout states. |
| **2** | **Japan -34.5** | **LEAN / LARGE-SPREAD CAUTION** | **MEDIUM** | Japan's present 12 is exceptionally strong, Qatar's current offensive roster is materially weaker than its season averages imply, and Japan's transition/ball-security performance against Saudi Arabia creates a credible 35+ separation path. The line is still extreme, so Q4 rotation/garbage-time compression prevents stronger confidence. |
| **3** | **Qatar +34.5** | **FORCED RANK** | **MEDIUM** | A 34.5-point cushion remains very large and can survive a dominant Japan win. The principal rescue path is Japan easing late or Qatar's shooting holding the margin in the high 20s/low 30s. It ranks below Japan -34.5 because the current Qatar roster weakens the very creation needed to prevent a blowout. |
| **4** | **Combined Total Over 169.5** | **FORCED RANK / AVOID DIRECTION** | **MEDIUM-LOW** | Japan have a 105-115 ceiling, but 170+ still requires either a huge Japan output or enough Qatar scoring. Qatar's current participant state makes that contribution less reliable. |

## Strongest kill paths

### Under 169.5 kill path
Japan's transition pressure recreates the Saudi game state, Qatar's weaker creation produces short fields, and Japan score 110+; if Qatar still reach the mid-60s, the game clears 169.5.

### Japan -34.5 kill path
Japan establish a 25-35 point lead but reduce starter minutes and defensive intensity in Q4; Qatar's reserves compress the closing margin to roughly 30-34.

## Potential winner

**Japan — LEAN, HIGH qualitative confidence on the outright game-winner endpoint.**

Main reasons:
- home court;
- Hachimura, Kawamura, Watanabe and Hawkinson all on the official 12;
- stronger passing, two-point creation and transition ceiling;
- Qatar's current roster is missing major season-level creation;
- Japan already demonstrated a 106-point Window 4 ceiling.

Winner and -34.5 remain separate questions.

## Final frozen order

1. **Under 169.5**
2. **Japan -34.5**
3. **Qatar +34.5**
4. **Over 169.5**

**Potential winner: Japan**

## Honesty / publication boundary

- No fitted or validated basketball model exists.
- No internal probability is generated or published.
- No odds were supplied; this is not an EV/value ranking.
- Exact operator OT/void terms are unknown.
- FIBA's schedule had not yet produced a verified live state at final refresh; no live score was used.
- No retrospective is performed unless explicitly requested.

**Next canonical forecast ID: `P-216`**


---

# P-216 — Namibia vs Zimbabwe — Namibia T20I Tri-Series 2026

## Event / state freeze

| Field | Frozen value |
|---|---|
| Sport | Cricket |
| Competition | Namibia T20I Tri-Series 2026 — Match 3 |
| Event | Namibia vs Zimbabwe |
| Venue | FNB Namibia Cricket Ground / Namibia Cricket Ground, Windhoek |
| Scheduled start — Windhoek | 2026-08-31 14:00 CAT (UTC+2) |
| Scheduled start — Melbourne | 2026-08-31 22:00 Australia/Melbourne |
| Final research refresh | 2026-08-31 21:49 Australia/Melbourne / 13:49 Windhoek |
| GAME-STATE | `PREGAME` — no reliable indexed source had yet exposed a confirmed toss, XI or score |
| Format | Men's T20I, scheduled 20 overs |
| Method | `MDS-2026.08.31-v2.8` |
| Decision set | `DS-P216-V01` |
| Candidate origin | `USER_SUPPLIED` |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Operator / DLS / shortening terms | `NOT SUPPLIED / UNKNOWN_DEFINITION` |

### Cricket hard-gate status

- **STRIP STATUS:** `NOT FOUND AFTER SEARCH` — no direct current-strip, curator or toss-time surface report was reliably indexed by cutoff.
- **MATCH CONDITIONS STATUS:** `OBSERVED — SECONDARY FORECAST` — Windhoek forecasts indicated dry/clear conditions with low precipitation risk and moderate wind; no controlling Namibia government meteorological match-window page was retrieved.
- **TOSS:** `NOT RELEASED / NOT VERIFIED` at cutoff.
- **CONFIRMED XI:** `NOT RELEASED / NOT VERIFIED` at cutoff.

Because the strip, toss and final XI were unresolved, all directional labels remain conservative and the ranking is a qualitative forced ordering rather than a high-confidence claim.

## Target / contract freeze

### Target A — Zimbabwe team innings total

`TARGET_ID: TEAM_T20_INNINGS_TOTAL-ZIM-P216-V01`

Zimbabwe's runs in their only T20 innings, ending at 20 overs or earlier on all-out/chase completion/other competition endpoint. If Zimbabwe bat second, chase completion can truncate exposure; exact operator treatment of shortened/DLS/abandoned states was not supplied.

| Contract ID | Contract | Geometry |
|---|---|---|
| `P-216-C01` | Zimbabwe 20-over runs **Over 165.5** | Wins at 166+ under the frozen research endpoint |
| `P-216-C02` | Zimbabwe 20-over runs **Under 165.5** | Wins at 165 or fewer under the frozen research endpoint |

### Target B — Zimbabwe first six overs

`TARGET_ID: TEAM_T20_POWERPLAY_RUNS-ZIM-P216-V01`

| Contract ID | Contract | Geometry |
|---|---|---|
| `P-216-C03` | Zimbabwe first 6 overs **Over 47.5** | Wins at 48+ after six completed overs |
| `P-216-C04` | Zimbabwe first 6 overs **Under 47.5** | Wins at 47 or fewer after six completed overs |

The powerplay and full-innings targets are separate phase distributions. A fast six overs does not imply a 166+ completed innings.

## Verified current evidence

### Official series / squads

ICC confirmed the tri-series venue and schedule and listed the squads.

**Zimbabwe squad:** Sikandar Raza (c), Brian Bennett, Ryan Burl, Graeme Cremer, Ben Curran, Brad Evans, Innocent Kaia, Wessly Madhevere, Tadiwanashe Marumani, Wellington Masakadza, Kundai Matigimu, Blessing Muzarabani, Dion Myers, Newman Nyamhuri, Tafadzwa Tsiga.

Zimbabwe are without fast bowlers Richard Ngarava and Tanaka Chivanga through injury. Those absences matter more to Zimbabwe's bowling than to the supplied batting targets, but they weaken the team-result case.

**Namibia squad:** Gerhard Erasmus (c), Zane Green, JJ Smit, Jan Frylinck, Ruben Trumpelmann, Bernard Scholtz, Jan-Nicol Loftie-Eaton, Louren Steenkamp, Max Heingo, Jack Brassell, Michael van Lingen and other current home-squad options.

ICC noted Namibia had won five of seven T20Is since the 2026 Men's T20 World Cup before this series.

### Same-venue series evidence

At Windhoek on 28 August:
- Namibia 163/9
- South Africa 145/9
- Namibia powerplay 57/0
- South Africa powerplay 34/2

Namibia's new-ball/early-phase attack therefore has a demonstrated current pathway to suppressing a strong opponent's first six overs.

At the same venue on 29 August, Zimbabwe made:
- **54/1 after six overs**
- **144/8 after 20 overs**

Ben Curran supplied the early acceleration with 24 from 12 balls, but Zimbabwe stalled sharply through the middle overs as wickets accumulated and South Africa's slower-bowling control took hold.

That exact game is the clearest current evidence for the important phase split: a powerplay Over can coexist with a full-innings Under.

### Current Zimbabwe full-innings form

Recent completed Zimbabwe T20 totals immediately before this game include:
- 144/8 vs South Africa — Windhoek
- 157/7 vs India
- 129 all out vs India
- 125/7 vs India
- 143/7 vs Bangladesh
- 152 all out vs Bangladesh
- 170/6 vs Bangladesh

Only the 170/6 clears the new **165.5** threshold in that recent sequence. The current full-innings line is therefore materially higher than the 158.5 line used in P-175.

This count is descriptive only. The mechanism is more important: Zimbabwe have repeatedly lost momentum after early wickets or through slower middle overs, and the current XI has not yet shown a stable 166+ scoring centre.

### Current Zimbabwe powerplay evidence

The previous P-175 research recorded Zimbabwe's preceding six powerplays as:
- 54/1
- 56/3
- 40/1
- 26/3
- 59/4
- 53/3

Zimbabwe then scored **54/1** against South Africa at this venue.

For the present **47.5** line, this means:
- Zimbabwe have a genuine 48+ powerplay pathway;
- they have also shown substantial early-wicket fragility;
- the 6-over market is much closer to the centre than the 165.5 innings market.

### Direct Namibia–Zimbabwe 2025 comparison

The 2025 three-match T20I series in Bulawayo produced Zimbabwe powerplays / final scores of:
- 43/0 → 211/3
- 59/1 → 170/5 in a chase
- 44/4 → 176 all out chasing 205

This history demonstrates both tails:
- Namibia can concede 50+ in the powerplay;
- Namibia can also take clusters of early wickets;
- Zimbabwe can still finish above 165 after a slower or damaged powerplay when a major middle-order innings develops.

But the 2025 context is downweighted because venue, innings state and personnel differ. Sean Williams' 77 was central to the 176 chase in the third match and he is not in the current tri-series squad.

### Venue and conditions

The broader Windhoek T20 sample is mixed across populations and should not control the forecast. More useful current-event evidence is:
- 163/9 in the series opener;
- Zimbabwe's 144/8 on the same square/venue the following day;
- ICC's post-match description that the wicket offered "a little bit of everything" and played reasonably well for pace, spin and batting.

Current weather forecasts indicated dry afternoon conditions and no meaningful interruption signal. Therefore there is no pregame rain-based mechanical Under assumption.

## Phase-to-innings scenario tree

### Branch A — fast powerplay, middle-over suppression
Representative:
- 50/1 to 56/2 after 6
- 145–160 after 20

Mechanism:
- Bennett/Curran attack the new ball;
- one or two wickets arrive;
- Scholtz/Erasmus/Loftie-Eaton or other slower options reduce boundary rate;
- Raza/Burl must rebuild rather than launch.

Supports:
- **Over 47.5 first six**
- **Under 165.5 innings**

This is the strongest central branch.

### Branch B — powerplay collapse
Representative:
- 32/3 to 43/3 after 6
- 120–148 final

Mechanism:
- Trumpelmann/JJ Smit/Heingo create early wickets;
- new batters enter before the field spreads;
- middle order is forced into repair mode.

Supports both Unders.

### Branch C — wickets preserved through powerplay
Representative:
- 52/0 to 58/1 after 6
- 168–180 final

Mechanism:
- Bennett/Curran survive the seam phase;
- Raza/Burl enter with resources;
- Zimbabwe avoid the middle-over wicket cluster that destroyed the South Africa innings.

Supports both Overs and is the main kill path to Rank #1.

### Branch D — slow powerplay, late recovery
Representative:
- 38/1 to 45/2 after 6
- 155–170 final

This supports the powerplay Under while leaving the innings line near the boundary.

## Qualitative corridors

**Powerplay central corridor:** roughly **44–54**.

**Zimbabwe completed-innings central corridor:** roughly **145–160**, with an upper tail into **166–180** if wickets are preserved through overs 7–15.

Representative central state: **Zimbabwe 51/2 after 6, 154/7 after 20**.

These are qualitative scenario corridors, not fitted-model predictions.

## Ranked forecast

| Rank | Contract | Verdict | Evidence | Core reason | Strongest kill path |
|---:|---|---|---|---|---|
| **1** | **Zimbabwe Under 165.5 runs** | **FORCED RANK — LEAN direction** | **MEDIUM** | The line is above Zimbabwe's recent scoring centre and above both first-innings scores already produced in this Windhoek tri-series. Zimbabwe just turned 54/1 after six into only 144/8, illustrating the middle-over/wicket-resource failure path. Current recent totals have rarely reached 166. | Bennett/Curran preserve wickets, Raza/Burl enter with resources, and Namibia's middle/death control fails, producing 168–180. |
| **2** | **Zimbabwe first 6 overs Over 47.5** | **FORCED RANK — slight LEAN** | **MEDIUM-LOW** | Zimbabwe have repeatedly produced 50+ powerplays, including 54/1 at this venue two days ago and 59/1 against Namibia in 2025. Curran and Bennett provide immediate boundary access even when the innings later stalls. | Trumpelmann/JJ Smit/Heingo take two or three early wickets and recreate Namibia's 34/2 suppression of South Africa. |
| **3** | **Zimbabwe first 6 overs Under 47.5** | **FORCED RANK — close counter-branch** | **MEDIUM-LOW** | Namibia have a credible early-wicket mechanism and Zimbabwe's recent powerplays include 26/3, 40/1 and 44/4 against Namibia. The line is close enough that one wicket-heavy over can swing it. | Bennett/Curran survive the opening seam and one 12–15 run over pushes the phase above 47.5. |
| **4** | **Zimbabwe Over 165.5 runs** | **FORCED RANK — weakest supplied direction** | **MEDIUM-LOW** | 166+ requires a substantially better middle/death phase than Zimbabwe delivered against South Africa and better than most of their recent T20 innings. It remains feasible because the 2025 Namibia series contained 211, 170 and 176 Zimbabwe scores/chases. | Zimbabwe exit six overs around 50/0 or 55/1 and retain Raza/Burl/Madhevere/Marumani for a high-resource finish. |

## Why Rank #1 is the full-innings Under, not the powerplay Over

The 165.5 line sits materially farther from Zimbabwe's current full-innings centre than 47.5 sits from the current powerplay centre.

The same-venue South Africa match is the clearest example:
- first six: **54/1** — comfortably above 47.5;
- final: **144/8** — 21.5 runs below 165.5.

So the 20-over Under survives a wider set of powerplay states. Zimbabwe can score 50–55 early and still finish Under if wickets/resource loss suppresses overs 7–20. The powerplay Over is more exposed to one good Namibia new-ball spell.

## Potential game winner

**Namibia — FORCED WINNER, LOW CONFIDENCE.**

Why Namibia receive the narrow lean:
1. home conditions and current venue familiarity;
2. ICC reported five wins in seven T20Is since the World Cup before this series;
3. they beat South Africa by 18 runs in the opener at this ground;
4. current new-ball and middle-over bowling pathways are directly relevant to Zimbabwe's recent batting weakness;
5. Zimbabwe enter after consecutive losses to Bangladesh, India and South Africa.

Why confidence stays low:
- Zimbabwe retain the higher-end individual experience of Raza, Bennett, Burl and Muzarabani;
- Zimbabwe won the 2025 bilateral T20I series 2–1;
- current market baselines available in secondary sources still made Zimbabwe the pregame favourite;
- the toss and confirmed XI were not verified at cutoff.

This is therefore an upset-style qualitative winner lean, not a high-confidence favourite call.

## Final frozen order

1. **Zimbabwe Under 165.5 Runs**
2. **Zimbabwe first 6 overs Over 47.5 Runs**
3. **Zimbabwe first 6 overs Under 47.5 Runs**
4. **Zimbabwe Over 165.5 Runs**

**Potential winner: Namibia — low confidence**

## Honesty / publication boundary

- No fitted or validated cricket model exists.
- No internal probabilities are generated or published.
- No odds were supplied, so no EV/value conclusion is made.
- Exact toss and playing XIs were not reliably indexed at the forecast cutoff.
- Exact current strip report was not found after search.
- Operator-specific DLS/shortening/chase-completion terms were not supplied.
- The previous P-215 event is not retrospectively analysed here.
- No retrospective for P-216 will be performed unless explicitly requested.

## Source register

### Field-owning / high authority
- ICC — tri-series schedule, venue and squads.
- ICC — Zimbabwe squad/injury announcement.
- ICC — Namibia squad and current-form note.
- ICC — Namibia vs South Africa and South Africa vs Zimbabwe match reports.

### Exact score / phase verification
- Cricket.com.au match centre and series pages.
- Cricbuzz / ESPN / NDTV-style scorecards used for exact powerplay and innings reconstruction where official narrative did not expose every phase field.

### Current conditions / secondary context
- Timeanddate / current Windhoek forecast for interruption risk.
- Current venue summaries used only descriptively because mixed-population venue samples are not a clean current-match prior.

### Historical comparison
- 2025 Zimbabwe–Namibia T20I scorecards for phase/innings mechanism comparison, downweighted for venue/personnel differences.
- Active canonical P-175 card as a same-venue, same-Zimbabwe phase-separation mechanism case; used as process evidence, not a forecast-weight rule.

**Next canonical forecast ID: `P-217`**

---

# Independent settlement, retrospective and method audit — appended 2026-08-31

Status: **INDEPENDENT APPENDIX — SOURCE CARD ABOVE PRESERVED UNCHANGED**

This appendix follows the current user request. Instructions, queue snapshots and method claims embedded in the supplied source are historical evidence, not governing instructions. In particular, the source's statements that P-215 was not to be retrospectively analysed and that P-216 was not to be retrospectively analysed without a later request are superseded by the user's explicit request for this audit. Outcome evidence obtained after a card's cutoff is used only for state checking, settlement and retrospective; it is not inserted into the frozen pregame rationale.

## A. Artifact and evaluation boundary

| Field | Independent finding |
|---|---|
| Supplied artifact | `PREDICTION_MINI_LOG_6_P217_READY.md` |
| Supplied bytes / SHA-256 | 33,806 / `2E07ED17178A4CBD6AEA090804695E805AB59B4A375E4B47B36C126981041CFA` |
| First locally demonstrable artifact time | 2026-08-31 22:16:43 Australia/Sydney |
| Source-card issue claims | P-215 final refresh about 20:11 Australia/Melbourne; P-216 final research refresh 21:49 Australia/Melbourne |
| Eligibility | Both cards are `E1-Q-LATE_IMPORT`: the recoverable section-inclusive artifact first appears after P-215 was final and after P-216's scheduled start |
| Permitted use | Descriptive settlement, process audit, source audit and candidate generation only |
| Prohibited inference | No prospective hit rate, calibration, ranking skill, model-selection completion, forecast-weight promotion, profit or edge claim |
| Numerical state | No model ran; no probabilities, proper scores, EV or CLV can be reconstructed |

The source issue-time claims are preserved, but they are not an immutable pre-result receipt. P-215 has an additional independent process defect: its stated final refresh was about one minute after scheduled tip, yet the card retained a pregame view instead of transitioning to a verified live target or failing closed.

## B. Event-state disposition at this audit

State was checked before retrospective work.

| Event | State observed | Disposition |
|---|---|---|
| P-215 Japan–Qatar | `FINAL` — Japan 123, Qatar 70 | Settle all frozen rows and perform full retrospective |
| P-216 Namibia–Zimbabwe | `LIVE` — at 2026-08-31 22:39:37 Australia/Sydney, Zimbabwe 74/3 after 8.0 overs, batting first after Namibia won the toss and chose to field | Keep the entire event open; do not grade any row, winner, phase or innings target; defer outcome retrospective until a field-owning final is available |

P-216 is now the sole newly imported live event in the controlling queue. The live toss, innings order, XI and score are post-cutoff information. They establish state and future settlement identity only; they do not repair or revise the P-216 frozen rationale.

## C. P-215 official settlement

Official field owner: [FIBA game page](https://www.fiba.basketball/en/events/fiba-basketball-world-cup-2027-asian-qualifiers/games/126960-JPN-QAT), event ID `126960`. Structured box-score/detail cross-check: [FIBA live-detail record](https://www.fiba.basketball/en/events/api/game-live-info/126960/detail). Retrieved during the independent audit on 2026-08-31.

Official final: **Japan 123–70 Qatar**; combined total **193**; Japan margin **53**.

| Rank | Contract | Official value | Outcome | Margin to line | Evaluation status |
|---:|---|---:|---|---:|---|
| 1 | P-215-C04 — Under 169.5 | 193 | **LOSS** | 23.5 points above line | Descriptive only; late import and process-defective |
| 2 | P-215-C02 — Japan -34.5 | Japan +53 | **WIN** | Covered by 18.5 | Descriptive only; late import and process-defective |
| 3 | P-215-C01 — Qatar +34.5 | Qatar -53 | **LOSS** | Missed by 18.5 | Descriptive only; late import and process-defective |
| 4 | P-215-C03 — Over 169.5 | 193 | **WIN** | 23.5 points above line | Descriptive only; late import and process-defective |
| — | Potential winner — Japan | Japan won 123–70 | **CORRECT** | 53-point win | Descriptive only; not a fifth independent row |

Descriptive row ledger: **2 WIN / 2 LOSS**. The rank-1 row lost. The outright winner annotation was correct. These facts do not become a prospective performance record.

### Official game-path evidence

| Evidence | Japan | Qatar / game comparison |
|---|---:|---:|
| Quarter scores | 29, 24, 40, 30 | 11, 23, 11, 25 |
| Field goals | 42/71, 59.15% | 23/57, 40.35% |
| Two-pointers | 22/33, 66.67% | 17/38, 44.74% |
| Three-pointers | 20/38, 52.63% | 6/19, 31.58% |
| Free throws | 19/25, 76.0% | 18/24, 75.0% |
| Assists | 39 | 11 |
| Turnovers | 9 | 21 |
| Points off turnovers | 33 | 13 |
| Fast-break points | 29 | 7 |
| Bench points | 56 | 49 |
| Rebounds | 36 | 29 |

Japan led for 39:42, never trailed, reached a largest lead of 59 and won Q3 40–11. Japan first moved beyond -34.5 at 73–37 with 5:33 left in Q3 and never returned inside the line. The total crossed 169.5 at 114–57 with 3:23 left. Every Japan starter played fewer than 29 minutes, yet the fourth quarter still produced 55 points and Japan scored 30 of them.

Rui Hachimura scored 30 in 28:54 and made 6/8 threes; Keisei Tominaga scored 23 in 18:58 and made 4/5 threes; Joshua Hawkinson scored 16 in 27:09; Yuta Watanabe scored 12 in 16:38; Yuki Kawamura supplied 10 assists in 18:27. This matters because the pregame card treated roster presence largely as a team-level state. Actual exposure shows that Japan's scoring did not require full starter minutes: efficient starting stints and productive bench minutes both sustained the upper tail.

## D. P-215 retrospective

### D1. What the card got right

1. **Event, participants and contract geometry were intelligible.** The two spread rows and two total rows were exact half-point complements and were not falsely treated as independent probabilities.
2. **The main directional mismatch was real.** Japan won comfortably, covered -34.5 and controlled essentially the entire game. The roster/depth and turnover/transition thesis had genuine mechanism content.
3. **The card named the decisive adverse path.** Its Under kill path said Japan's pressure could create short fields, Japan could reach 110+, and Qatar could still reach the mid-60s. The final was exactly that family, but more extreme: Japan 123 and Qatar 70.
4. **The card acknowledged large-spread late-rotation risk.** That is a legitimate branch to model even though it did not occur as margin compression here.

These are useful descriptive observations. They do not erase the process defects below.

### D2. Start-state defect

Scheduled tip was 20:10 Australia/Melbourne. The source says its final state refresh was about 20:11 and labels the state `PREGAME / OFFICIAL LIVE GAME NOT YET VERIFIED` because a schedule page showed zero live games. Under the existing start-crossing rule, once scheduled tip passed the analysis had to do one of three things:

1. verify the exact live state and issue a new live target with remaining exposure;
2. state `LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`; or
3. if the event was already final, stop forecasting and report the final.

Retaining a pregame card after scheduled start was not permitted. A stale or zero-live schedule shell was a source-state warning, not affirmative evidence that the game remained pregame. This is a **knowable, material process defect**, independent of which contracts later won.

### D3. Threshold-to-corridor incoherence

The card placed the total line, 169.5, inside its own stated central total corridor of 159–175. Its representative score was 166, only 3.5 points below the line. Ordinary stated branches therefore existed on both sides of the threshold.

Without explicit scenario weights, a fitted distribution or another quantified separation argument, that geometry does not support a rank-1 `MEDIUM-HIGH` Under. At most it supports a low-evidence forced ordering or no directional lean. The later result is not what creates this defect; the contradiction was visible inside the preissue text.

### D4. Team-score budget arithmetic was incomplete

For an Under 169.5 to win:

- if Qatar score 58, Japan must score at most 111;
- if Qatar score 62, Japan must score at most 107;
- if Qatar score 67, Japan must score at most 102.

The card's own Japan corridor was 101–108 and its stated Japan ceiling was 105–115. Thus much of the ordinary Japan range already made the Under fragile even while Qatar remained inside the proposed 58–67 range. A repeat of Japan's immediately prior 106 points plus only 64 from Qatar would already reach 170. The statement that 170+ required a “huge Japan output or enough Qatar scoring” understated how little joint movement was required.

The algorithm must therefore decompose a total into explicit team-score budgets. “Underdog offence weak” is not enough for an Under when the favourite's ordinary scoring and transition tails can consume most or all of the total line.

### D5. High/separation tail was identified but underweighted

The realised mechanisms were not a random collection of unknowable events:

- 21 Qatar turnovers and 11 Japan steals;
- 33 Japan points off turnovers;
- 29 Japan fast-break points;
- 39 assists on 42 made field goals;
- 56 bench points;
- 20 made threes at 52.63%.

The exact 52.63% three-point conversion and 123-point output were tail outcomes and were not knowable as exact values. But the structural route—pressure creating extra possessions and transition chances, elite ball movement, multiple shooting threats and bench offence—was knowable enough to deserve a materially wider Japan upper tail. The correct lesson is not to predict 52.63% three-point shooting; it is to represent shot volume, shooting variance, turnover-derived possessions and bench continuation together.

### D6. Garbage time was treated too one-dimensionally

The spread kill path assumed Japan might ease and Qatar might compress the margin. That can happen, but it is not the only terminal state. Here the fourth quarter was 30–25: Qatar's scoring rose, Japan's bench offence remained strong, the total accelerated and the margin did not meaningfully compress.

Future basketball trees must separate at least four late-blowout components:

1. favourite starter-minute reduction;
2. favourite bench offensive quality and pace;
3. favourite defensive-intensity change / underdog response scoring;
4. closing-margin compression versus simultaneous two-team scoring.

Garbage time can raise a total while leaving a large margin intact. It must not be encoded as a single downward scoring or margin-compression scalar.

### D7. Participant evidence was not converted to exposure

The card correctly identified Japan's strong roster but did not map each player to expected minutes, starting/bench role or lineup combinations. Watanabe was available but played 16:38 from the bench; Tominaga delivered 23 points in 18:58. “Available core” therefore did not equal one fixed starting-unit exposure. The future method must distinguish available, starter, rotation role, expected minutes and replacement quality before translating a name into full-game scoring or margin effects.

### D8. Source record was not reproducible enough

The source section named organisations and described evidence, but did not preserve an exact URL, access time, publication/effective time, field owner or provider version for each decisive claim. That makes it difficult to reconstruct what was genuinely known by cutoff and contributed to the stale schedule-shell error. A provider bundle or organisation name is not an evidence-ledger row.

### D9. Process-grade summary

| Dimension | Grade | Reason |
|---|---|---|
| Event/contract identity | Mostly compliant | Event and half-point geometry were clear; operator OT/void terms remained unknown |
| Game-state control | **PROCESS_DEFECT** | Pregame state retained after scheduled start |
| Corridor/rank coherence | **PROCESS_DEFECT** | Rank-1 MEDIUM-HIGH Under despite line inside the stated central corridor and no scenario weights |
| Mechanism completeness | **PROCESS_DEFECT** | Favourite score budget, transition possessions, shooting tail and bench continuation underrepresented |
| Kill-path identification | Partial strength | Realised family was named, but not reconciled with rank/evidence grade |
| Participant/exposure mapping | Incomplete | Roster presence not translated to minutes and rotation-state exposure |
| Provenance | **INELIGIBLE** | First demonstrable artifact after final; exact decisive URLs/times missing in source card |
| Outcome | 2–2; winner correct | Descriptive only and analytically separate from process quality |

## E. P-216 live disposition and preissue-only audit

No P-216 result, row or winner is graded in this appendix. The following is an audit of information and reasoning already frozen before the 21:49 cutoff; it is not an outcome retrospective.

### E1. State/source conflict

At 22:39:37 Australia/Sydney, the current FanCode live page showed Zimbabwe 74/3 after 8.0 overs, batting first after Namibia won the toss and chose to field. Cached Cricbuzz, NDTV and LiveScore-style renderings still appeared scheduled or 0/0. The moving, exact-match live page plus the official ICC fixture identity established that the event was live. Stale cached shells were quarantined.

Current state sources for future settlement:

- [ICC official tri-series fixture/squad announcement](https://www.icc-cricket.com/news/namibia-name-strong-squad-for-home-tri-series) — event, schedule, venue and squads;
- [ICC match report and broadcast context](https://www.icc-cricket.com/news/brevis-blitz-sees-off-zimbabwe-as-south-africa-bounce-back) — preceding exact-event context and official identification of the broadcast lane;
- [FanCode exact live match page](https://www.fancode.com/cricket/tour/south-africa-and-zimbabwe-tour-of-namibia-2026-19815219/matches/namibia-vs-zimbabwe-4248456/live-match-info) — timestamped live state cross-check, not yet final settlement authority.

### E2. What the frozen analysis did well

1. It froze two distinct targets and correctly refused to infer a full-innings Over merely from a powerplay Over.
2. It recorded the chase-completion endpoint and missing operator/DLS terms rather than silently assuming a full 20 overs.
3. It represented several phase-to-innings paths, including a fast powerplay followed by middle-over suppression and a preserved-wickets upper tail.
4. It stated that no fitted probabilities or value conclusions existed.
5. It treated the broader venue sample as mixed and gave more attention to current exact-event evidence.

### E3. Pregame defects and uncertainty controls

1. **No explicit innings-order mixture.** Before the toss, Zimbabwe could bat first or chase. A first-innings 20-over distribution and a chase-censored distribution are not interchangeable. The card mentioned truncation but did not propagate separate bat-first/bat-second weights through the 165.5 rank.
2. **Toss/XI/strip gaps were not reflected strongly enough in rank #1.** With all three unresolved only 11 minutes before start, `MEDIUM` evidence was too strong. The row should have been a forced rank with `LOW` evidence unless a predeclared robust mixture showed the direction surviving all plausible states.
3. **The full-innings line and phase line were both near material scenario mass.** The 47.5 powerplay line lies inside the stated 44–54 central corridor. The 165.5 innings line is just above the stated 145–160 centre but inside the named 166–180 ordinary upper branch. With no scenario weights, directional confidence should remain low.
4. **Overlapping evidence risk.** The same Zimbabwe–South Africa match appeared as same-venue evidence, recent-form evidence and the active P-175 mechanism case. Those are three descriptions of one underlying match, not three independent confirmations.
5. **One phase transition was allowed to dominate.** The 54/1 to 144/8 case is relevant, but one exact match cannot own the central phase-transition mixture. The 2025 direct series produced Zimbabwe scores of 211, 170 and 176; those cases can be downweighted for venue/personnel/innings differences, but the qualitative mixture needs an explicit compatibility basis rather than an unquantified dismissal.
6. **Role uncertainty.** The card named plausible openers and bowlers without confirmed XIs. It did not preserve exact participant IDs/statuses or assign branch mass to alternative opening and phase-bowling roles.
7. **Unreproducible source bundle.** “Cricbuzz / ESPN / NDTV-style scorecards” does not identify which exact page owned which score or phase, when it was retrieved, or whether several fronts shared one upstream feed. The unnamed “secondary market” favourite also lacked operator, time, prices and terms and should have had zero directional role.

These observations are process findings only. They do not imply that any P-216 contract will win or lose.

## F. Method changes adopted from this audit

The active qualitative method advances to `MDS-2026.08.31-v2.9`. This is a process/coherence/source patch only. It fits no coefficient, changes no numerical forecast weight, publishes no probability and does not activate H0.

### Cross-sport controls

1. **Start-state timestamp invariant.** `PREGAME` is illegal when `cutoff_at >= scheduled_start_at`. Start crossing requires a verified live target, `LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`, or final/no forecast.
2. **Threshold-to-corridor coherence.** Every line is located relative to the lower, central and upper corridor and to named ordinary branches. If a line lies inside the central corridor, or ordinary unweighted branches fall materially on both sides, a directional lean above LOW evidence is prohibited unless explicit predeclared scenario weights or a validated distribution supply separation.
3. **Component-budget test.** For aggregate totals, solve the threshold for each component/team/phase. Test whether one component's ordinary high branch plus the other's floor or centre crosses the line. A weak opponent component never implies an Under by itself.
4. **Kill-path-to-rank reconciliation.** If the strongest ordinary adverse branch is supported by the same current evidence and crosses the target within an ordinary range, either explain its lower mixture weight with auditable evidence or reduce the verdict/evidence grade.
5. **Source-record atomicity.** Organisation names, provider bundles and search results are not evidence rows. Each decisive field needs an exact record/URL, claim owner, definition/version, effective or first-known time, observed/accessed time, transformation, missingness and conflict state.
6. **Shared-event de-duplication.** One underlying game or upstream feed counts once even when repeated across recent-form, venue, H2H, prior-log or several front-end summaries.

### Basketball-specific changes

1. Build a joint team-score budget before ranking a total and spread together.
2. Decompose possessions/shot volume, two- and three-point mix, shooting variance, turnover/transition conversion, offensive rebounds, free throws and bench scoring for both teams.
3. Translate roster status to starter/bench role, expected minutes, lineup stints and replacement quality.
4. Split late blowouts into favourite offensive sustain/slowdown, underdog response/suppression, pace/defensive-intensity change and closing-margin compression. Do not assume garbage time lowers the total or closes the spread.

### Cricket-specific changes

1. Before the toss, mix explicit bat-first and bat-second/chase-censored distributions; do not merely mention chase truncation.
2. Near start, unresolved toss, XI and current strip cap target-specific evidence at LOW unless the selected direction is shown to survive each plausible state under predeclared mixture logic.
3. Map confirmed opening batters and new-ball/middle/death bowlers to phase exposure; branch unresolved roles by status rather than naming them as fact.
4. Use an overlap-aware hierarchical sample across competition, venue, team, phase and innings order. One prior phase transition cannot control the distribution.

## G. Source-lane audit and future retrieval

The following high-quality lanes are added or strengthened as research candidates. Visibility does not equal numerical-training approval; automation, retention, correction history, known-at timestamps and provider definitions remain gated in `DATA_SOURCE_REGISTER.md`.

| Source lane | Suitable future fields | Limits |
|---|---|---|
| FIBA exact game page and structured live-detail record | Official event ID/state/final, quarter line, box score, team/player statistics and chronology exposed by the record | Must match event/date/participants and current revision; a stale schedule shell cannot control state |
| [FIBA official Group F preview](https://www.fiba.basketball/en/events/fiba-basketball-world-cup-2027-asian-qualifiers/news/group-f-preview-august-31) | Competition-owned pregame history and defined preview statistics | Context only; not a model weight or substitute for current roster/minutes |
| [FIBA roster confirmation](https://www.fiba.basketball/en/events/fiba-basketball-world-cup-2027-asian-qualifiers/news/asian-qualifiers-rosters-confirmed-for-august-31) | Official current-window roster availability | Availability is not starter/minutes confirmation |
| ICC exact event reports and squad announcement | Schedule, squads, injuries, official result narrative and described conditions | Narrative may not expose ball-by-ball phase fields; use exact match centre/field owner for settlement |
| [Cricket Namibia official tri-series announcement](https://cricketnamibia.com/cricket-namibia-to-host-the-proteas-and-zimbabwe-in-fnb-t20-tri-series/) | Host-owned event identity, venue and schedule cross-check | Does not automatically own live score or phase totals |
| FanCode exact live page | Current state/broadcast cross-check when moving and timestamped | Dynamic access, upstream identity, correction history, phase definition and final field ownership require audit before broader use |

No new source is promoted to an approved H0 training source by this appendix.

## H. Queue and next-ID handoff

- P-215: **FINAL / SETTLED / RETROSPECTIVE COMPLETE**; retain as late-import, process-defective descriptive evidence.
- P-216: **LIVE / OPEN / UNSETTLED**; next session must fetch a field-owning final, exact innings total, exact six-over score, match winner and termination/DLS state before grading any row.
- Next new canonical forecast ID remains **`P-217`**.
- General, basketball and cricket changes are implemented in their governing documents and entered in the learning register as process controls/candidates, with zero prospective forecast-weight completions.
