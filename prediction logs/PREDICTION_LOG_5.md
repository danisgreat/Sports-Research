# Prediction Mini Log 2

Status: **ACTIVE CONTINUATION LOG — NEW FORECASTS APPEND HERE**
Opened: **2026-08-28**
Current method: **MDS-2026.08.28-v2.4 — qualitative champion**
Numerical training specification: **NTS-2026.08.25-v0.2 — Stage 0 / pre-fit**
Predecessor: `PREDICTION_LOG_COMBINED.md` — historical evidence and canonical predecessor only.

This log continues the canonical `P-###` sequence from the previous combined prediction log.

The previous combined log remains the historical record for **P-001 through P-123**. Those records are not duplicated here.

---

## Current controlling snapshot

This is the controlling queue and canonical-ID authority for this continuation log.

| Field                                    | Current value                                                                                |
| ---------------------------------------- | -------------------------------------------------------------------------------------------- |
| As of                                    | 2026-08-28 — continuation initialized from `PREDICTION_LOG_COMBINED.md`                      |
| Previous canonical range                 | `P-001` through `P-123`                                                                      |
| Next canonical ID                        | **`P-124`**                                                                                  |
| Open — pregame                           | **0**                                                                                        |
| Open — live / state verification pending | **0**                                                                                        |
| Suspended / postponed                    | **0**                                                                                        |
| Final awaiting settlement                | **0**                                                                                        |
| New forecast events in this log          | **0**                                                                                        |
| Closed forecast events in this log       | **0**                                                                                        |
| Probability state                        | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`                                         |
| Value state                              | `NO VALUE DETERMINABLE` unless the applicable validated-model and same-time price gates pass |
| Governing forecast method                | `MDS-2026.08.28-v2.4`                                                                        |
| Numerical model state                    | **No fitted, calibrated, tested, or validated numerical model**                              |

**Canonical continuation rule:** the first new forecast recorded in this log is `P-124`. Each subsequent new event increments the canonical ID by one.

---

## Record boundary

`PREDICTION_LOG_COMBINED.md` remains the historical record for all canonical entries through `P-123`.

This continuation log does **not** reproduce previous completed forecasts, settlements, performance counts, historical retrospectives, or component logs.

Only forecasts issued from `P-124` onward are stored here.

---

## Queue procedure

Before researching each new event:

1. Check the active queue in this log.
2. If a queued event is verified **FINAL**, settle it before issuing the next forecast.
3. If a queued event is **LIVE**, leave it open and continue to the next event.
4. If an event is **POSTPONED**, **SUSPENDED**, or otherwise unresolved, preserve its exact state and continue.
5. If the new requested event becomes final before the forecast is delivered, record:
   `NO FORECAST — FINAL BEFORE DELIVERY`.
6. Never construct a hindsight forecast for an event or target that is already settled.
7. Earlier issued forecasts are immutable. Any later update must be appended rather than rewriting the original forecast.

---

## Forecasting standard

Every new game must follow the active Sports Research framework before a ranking is issued.

The required workflow is:

1. Verify the exact event, competition, participants, venue, rules and scheduled start.
2. Determine and refresh the current `GAME-STATE`.
3. Freeze the complete user-supplied candidate slate.
4. Freeze the exact underlying target separately from the bookmaker lines.
5. Resolve regulation/overtime/extra-time/golden-point/extra-innings/DLS/action/push/void terms as applicable.
6. Verify decision-driving participants and availability through the applicable official source hierarchy.
7. Research volatile information first, followed by opponent-adjusted process evidence, matchup, venue/environment, adjusted history and conditional context.
8. Separate broad baseline evidence from the current regime.
9. Build one coherent sport-native event/target corridor.
10. Explicitly model lower, central, upper and material adverse scenarios.
11. Identify the strongest ordinary kill path for the leading forecast.
12. Map contract overlap, complements, gaps, pushes and dependence before ranking.
13. Rank every valid unresolved supplied contract uniquely by marginal estimated likelihood of winning.
14. Identify a potential game winner separately.
15. Perform a final volatile-information refresh immediately before issue.
16. Freeze the information cutoff and append the complete forecast section before delivery.

---

## Current model and probability boundary

The governing method is presently qualitative.

`H0` has not been built or quality-approved.

No internal numerical model has been fitted, calibrated, tested, validated or promoted.

Therefore:

* no internally generated percentage probabilities are published;
* no invented probability may be added to a forecast;
* no historical directional percentage is treated as calibration;
* no directional record is presented as betting profitability or market edge;
* without a validated calibrated model and complete same-time market snapshot, the value state remains:

`NO VALUE DETERMINABLE`

The probability publication state for current forecasts is:

`NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

---

## Active queue

There are no inherited open events at initialization.

| Canonical ID | Sport / competition | Event | View | GAME-STATE | Scheduled start | Status    |
| ------------ | ------------------- | ----- | ---- | ---------- | --------------- | --------- |
| —            | —                   | —     | —    | —          | —               | **EMPTY** |

---

## Continuation index

No new forecasts have been issued in this continuation log yet.

| Canonical ID | Sport | Competition | Event | View | Initial state | Rank #1 | Potential winner | Current status |
| ------------ | ----- | ----------- | ----- | ---- | ------------- | ------- | ---------------- | -------------- |
| —            | —     | —           | —     | —    | —             | —       | —                | —              |

---

# New-game entry format

Every new game from `P-124` onward is appended using the following structure.

---

## P-### — [Event]

### Record metadata

| Field                                 | Recorded value                                       |
| ------------------------------------- | ---------------------------------------------------- |
| Canonical ID                          | `P-###`                                              |
| Sport                                 |                                                      |
| Competition / format                  |                                                      |
| Season / rules era                    |                                                      |
| Official event ID                     |                                                      |
| Event                                 |                                                      |
| Venue                                 |                                                      |
| Home / away / neutral                 |                                                      |
| Scheduled start — venue local         |                                                      |
| Scheduled start — Australia/Melbourne |                                                      |
| Request time                          |                                                      |
| Data refresh time                     |                                                      |
| Information cutoff                    |                                                      |
| Issue time                            |                                                      |
| GAME-STATE                            | `PREGAME` / `LIVE`                                   |
| Method version                        | `MDS-2026.08.28-v2.4`                                |
| Numerical status                      | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value status                          | `NO VALUE DETERMINABLE`                              |

### Decision set

**Decision-set ID:** `DS-P-###-V01`
**Candidate origin:** `USER_SUPPLIED`
**Ranking objective:** marginal estimated probability/robustness of settling as a win; **not** staking, EV or diversification.

| Candidate ID | User-supplied contract | Eligibility | Canonical contract ID |
| ------------ | ---------------------- | ----------- | --------------------- |
| P-###-C01    |                        | `ELIGIBLE`  |                       |
| P-###-C02    |                        | `ELIGIBLE`  |                       |
| P-###-C03    |                        | `ELIGIBLE`  |                       |
| P-###-C04    |                        | `ELIGIBLE`  |                       |

### Target definition

| Field                              | Definition |
| ---------------------------------- | ---------- |
| TARGET_ID                          |            |
| Exact target                       |            |
| Unit                               |            |
| Support                            |            |
| Start state                        |            |
| Endpoint                           |            |
| Scheduled exposure                 |            |
| Uncertain exposure                 |            |
| Termination / censoring            |            |
| Regulation / OT / extra-time terms |            |
| Push treatment                     |            |
| Void / action assumptions          |            |
| Statistic / settlement provider    |            |

### Event and participant verification

**Official event identity:**
[To be completed from research.]

**Participants / availability:**
[To be completed from research.]

**Decision-driving role verification:**
[Starter / XI / lineup / quarterback / goalie / team list / other applicable roles.]

**Material absences or role changes:**
[To be completed from research.]

**Highest-priority unresolved information:**
[None, or specify.]

---

### Baseline and current-regime evidence

#### Structural baseline

[Competition-, season-, rules-, venue- and opponent-adjusted baseline.]

#### Current regime

[Current lineup/participants, recent process, role, tactical, availability or structural changes.]

#### Adjusted recency

[Relevant recent performance after opponent, role, venue and regime adjustment.]

#### Matchup

[Sport-native matchup mechanisms.]

#### Venue / environment

[Venue, surface, roof, weather, travel, rest or other applicable context.]

#### Historical evidence

[Only adjusted and genuinely comparable history; old H2H or streaks remain secondary.]

---

### Sport-native mechanism

**Exposure:**
[Possessions / plate appearances / balls / overs / sets / drives / scoring shots / attacking sequences / shifts / games / service points, as applicable.]

**Rate / quality:**
[Opponent-adjusted scoring, creation, suppression, efficiency or event rate.]

**Participant / role influence:**
[How current participants change exposure or rate.]

**Matchup interaction:**
[Mechanism.]

**Context adjustment:**
[Mechanism.]

**Expected central event shape:**
[Qualitative central corridor.]

---

### Scenario map

| Scenario                     | Event path | Contracts helped | Contracts hurt |
| ---------------------------- | ---------- | ---------------- | -------------- |
| Lower-tail                   |            |                  |                |
| Central                      |            |                  |                |
| Upper-tail                   |            |                  |                |
| Material adverse / kill path |            |                  |                |

**Strongest ordinary kill path:**
[State the most credible ordinary way the leading pick loses.]

---

### Contract geometry and dependence

[Explain exact complements, overlapping alternate lines, gaps, pushes, shared mechanisms and dependence groups.]

No contract is treated as independent merely because it occupies a separate ranking row.

---

## Final ranking

|  Rank | Candidate / contract ID | Exact contract | Verdict | Evidence quality | Dependence group | Performance role | Actionability           | Probability state |
| ----: | ----------------------- | -------------- | ------- | ---------------- | ---------------- | ---------------- | ----------------------- | ----------------- |
| **1** |                         |                |         |                  |                  |                  | `NO VALUE DETERMINABLE` | `NOT GENERATED`   |
| **2** |                         |                |         |                  |                  |                  | `NO VALUE DETERMINABLE` | `NOT GENERATED`   |
| **3** |                         |                |         |                  |                  |                  | `NO VALUE DETERMINABLE` | `NOT GENERATED`   |
| **4** |                         |                |         |                  |                  |                  | `NO VALUE DETERMINABLE` | `NOT GENERATED`   |

### Ranking rationale

**#1 — [contract]**
[Why it ranks first, including the strongest opposing path.]

**#2 — [contract]**
[Why it ranks second and why it does not outrank #1.]

**#3 — [contract]**
[Reasoning.]

**#4 — [contract]**
[Reasoning.]

---

## Potential game winner

**Potential winner:** [Team / player]
**Status:** `LEAN` / `FORCED WINNER — LOW CONFIDENCE`

**Canonical winner contract:**
[Alias an existing contract ID if identical; otherwise create the appropriate canonical winner contract reference.]

**Winner reasoning:**
[Separate winner reasoning from total/spread reasoning.]

---

## Important unknowns and limitations

* [Unknown / unavailable / conflicting information.]
* [Participant uncertainty.]
* [Source limitation.]
* [Contract-definition limitation.]
* [Sample/regime uncertainty.]
* [Any other material risk.]

---

## Final forecast card

|  Rank | Pick |
| ----: | ---- |
| **1** |      |
| **2** |      |
| **3** |      |
| **4** |      |

**Potential game winner:**

**GAME-STATE:**

**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`
**Value state:** `NO VALUE DETERMINABLE`

**Forecast status:** `ISSUED — PRE-RESULT`

---

## Source record

| Source | Source class | Decision-driving field | Freshness / access state |
| ------ | ------------ | ---------------------- | ------------------------ |
|        |              |                        |                          |

---

## Logging confirmation

**Canonical ID:** `P-###`

**Forecast appended before delivery:** `YES`

**Issued view:** `V01`

**Result status:** `OPEN — PENDING`

---

## P-124 — Chase Ferguson vs Fumin Jiang — M15 Maanshan 8 Quarterfinal

### Record metadata

| Field | Recorded value |
|---|---|
| Canonical ID | `P-124` |
| Sport | Tennis |
| Competition | ITF Men's World Tennis Tour — M15 Maanshan 8 |
| Round | Singles Quarterfinal |
| Event | Chase Ferguson (AUS) vs Fumin Jiang (CHN) |
| Host city | Ma'anshan, Anhui, China |
| Venue | ROGT Sports Event Center / Tennis Sports Center, Ma'anshan — venue association supported; exact match court NOT VERIFIED |
| Surface | Indoor hard |
| Recognised venue surface context | ITF-recognised DecoTurf Cat 3 acrylic court at ROGT Sports Event Center; medium pace. Exact court assignment for this match NOT VERIFIED. |
| Scheduled start — venue local | `CONFLICTING SECONDARY SOURCES`: approximately 11:30–12:00 China Standard Time on 2026-08-28 |
| Scheduled start — Australia/Sydney | approximately 13:30–14:00 AEST on 2026-08-28 |
| Final research refresh | 2026-08-28 approximately 14:23 AEST |
| GAME-STATE | `PREGAME / START-STATE VERIFICATION LIMITED` — current secondary match pages exposed no set/game score, but official ITF live state was not retrievable and nominal scheduled time may have crossed |
| State actionability | `NOT ACTIONABLE IF MATCH HAS STARTED` — reverify against the user's live sportsbook/official score before use |
| Method | `MDS-2026.08.28-v2.4` |
| Tennis model state | Qualitative module only; no approved/fitted tennis numerical model |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Result status | `OPEN — STATE VERIFICATION / FINAL PENDING` |

### Framework controls applied

`L-001`, `L-002`, `L-003`, `L-011`, `L-015`, `L-016`, `L-017`,
`L-018`, `L-021`, `L-024`, `L-026`, `L-029`.

Tennis-specific caution:
`C-PL5-TEN-SURFACE-H2H` is treated as a candidate lesson only, NOT as
an active forecast weight. Current surface evidence, ranking and historical
H2H are reconciled rather than allowing one source family to control automatically.

---

### Event / target definition

**Decision-set ID:** `DS-P-124-V01`

**Candidate origin:** `SYSTEMATIC_UNIVERSE`

**Reference market source:** current indexed MarathonBet Ma'anshan
quarterfinal markets, supplemented only where necessary to verify the same
contract family.

**Market-universe policy:** freeze the standard bilateral contracts available
before ranking:
1. match winner;
2. first-set winner;
3. main ±5.5-game handicap;
4. ±1.5-set handicap;
5. match total 19.5 games.

All opposite branches were retained in the decision set. No post-ranking search
for an easier alternate threshold was used.

**TARGET_ID:** `TEN-MATCH-BO3-INDOOR-HARD-P124-V01`

**Underlying target:** complete best-of-three singles match score tree —
service points → service games/breaks → sets → completed match.

**Start state:** pre-match / no verified ball played.

**Endpoint:** completed best-of-three match under the applicable operator's
retirement/walkover rules.

**Units:** games, sets and match winner.

**Tiebreak / deciding-set rules:** standard ITF best-of-three treatment assumed
for research; exact operator settlement terms control the wager.

**Retirement / walkover treatment:** `UNKNOWN_DEFINITION` because the user did
not supply an operator.

**Actionability consequence:** no value claim and contract settlement should be
checked against the user's actual operator before use.

---

### Frozen candidate universe

| Candidate ID | Contract | Reference line state | Dependence pair |
|---|---|---|---|
| `P-124-C01` | Chase Ferguson — Match Winner | Ferguson ML | `ML` |
| `P-124-C02` | Fumin Jiang — Match Winner | Jiang ML | `ML` |
| `P-124-C03` | Chase Ferguson — 1st Set Winner | Ferguson 1st-set ML | `S1` |
| `P-124-C04` | Fumin Jiang — 1st Set Winner | Jiang 1st-set ML | `S1` |
| `P-124-C05` | Chase Ferguson -5.5 Games | -5.5 | `GH55` |
| `P-124-C06` | Fumin Jiang +5.5 Games | +5.5 | `GH55` |
| `P-124-C07` | Chase Ferguson -1.5 Sets | Equivalent to Ferguson winning 2-0 if match completes normally | `SH15` |
| `P-124-C08` | Fumin Jiang +1.5 Sets | Jiang wins at least one set or the match if completed normally | `SH15` |
| `P-124-C09` | Under 19.5 Match Games | 19.5 | `TOT195` |
| `P-124-C10` | Over 19.5 Match Games | 19.5 | `TOT195` |

Reference prices were observed only to establish that these were real current
contracts. They are not internally generated probabilities and are not used to
claim expected value.

---

### Participant and event verification

#### Chase Ferguson

- Australian, age 27.
- Official ITF profile snapshot lists ATP singles ranking **640**, also his
  career high as of 27 July 2026.
- Official ITF snapshot had a 2026 professional record of 16-15 on hard at its
  update boundary.
- Current specialist records incorporating later matches show the additional
  August results.
- Current Ma'anshan run:
  - beat Yua Taka **6-3, 7-6(4)**;
  - beat Hanyi Liu **6-3, 6-2**.
- He therefore enters this quarterfinal without dropping a set in his first two
  singles matches this week.

#### Fumin Jiang

- Chinese, age 19.
- Right-handed; ITF lists hard as his preferred surface.
- Current secondary ranking snapshot: approximately ATP **1701**, career high
  approximately 1460.
- Current Ma'anshan run:
  - beat Dong Ju Kim **6-4, 7-6(5)**;
  - beat Qian Sun **6-3, 3-6, 6-2**.
- Jiang therefore arrives with two significant current-event wins and should not
  be treated as a generic No.1700-level opponent.
- Additional workload: Jiang/Zhang also played a doubles quarterfinal on
  27 August, losing **7-5, 7-5**, after Jiang's three-set singles match.
- No equivalent same-day Ferguson doubles exposure was verified in this research
  pass; absence of a retrieved result is not treated as proof that none existed.

---

### Surface and venue state

The ITF calendar identifies the 24–30 August M15 Maanshan event as
**Indoor — Hard**.

The ITF recognised-court register lists ROGT Sports Event Center in Ma'anshan,
Anhui with a DecoTurf Cat 3 acrylic centre court tested at **medium** pace.

This is useful venue-level surface evidence, but the exact court assigned to
Ferguson–Jiang was not verified and no court-specific coefficient is applied.

---

### Broad baseline

Ferguson owns the stronger established professional baseline.

Decision-driving supporting indicators from specialist statistical sources:

- Ferguson service hold approximately **73–76%** across the referenced
  broader samples.
- Ferguson first-serve points won approximately **63%**.
- Ferguson second-serve points won approximately **51–52%**.
- Ferguson return points won approximately **39–41%**.
- Ferguson break-point saving in the referenced samples is around **59–62%**.

Jiang's broader profile is more vulnerable behind serve:

- service hold approximately **65%** in the referenced specialist sample;
- break-point save approximately **54.5%**;
- broader second-serve conversion approximately mid-40s, with recent
  six-month snapshots at times below 40%;
- Jiang does, however, show useful second-serve return pressure, generally
  around the high-40% range in the available recent snapshots.

These provider figures are not treated as identical definitions or a fitted
model. They are directional process evidence only.

**Baseline branch:** Ferguson has the more stable hold/second-serve/pressure
profile and the more established professional level.

---

### Current-regime branch

The baseline cannot simply override Jiang's current tournament.

Jiang has just defeated Dong Ju Kim and Qian Sun, including winning four of his
last five completed sets. His current results suggest a materially more
competitive regime than his raw ranking alone.

Ferguson's current regime is also positive: two straight-set wins, including
scores of 6-3, 7-6 and 6-3, 6-2.

The correct interpretation is therefore:

- **Ferguson remains the stronger central match winner**;
- **Jiang's current regime materially increases the close-set / set-winning
  branch**;
- it weakens aggressive Ferguson game-spread confidence;
- it does not provide enough evidence to reverse the overall winner.

---

### Head-to-head continuity audit

Ferguson leads the recorded H2H **2-0**.

Both previous meetings were at M15 Maanshan on indoor hard in September 2025:

1. Ferguson def. Jiang **6-4, 5-7, 6-4**.
2. Ferguson def. Jiang **6-4, 3-6, 6-1**.

Important consequences:

- same venue/level/surface gives these meetings more continuity than a generic
  old H2H;
- Ferguson won the first set **6-4 in both**;
- Ferguson won both matches;
- Jiang nevertheless won one set in each meeting;
- game margins were only **+2 and +4 for Ferguson**, so Jiang +5.5 would have
  covered both historical meetings;
- both matches exceeded 19.5 total games.

The H2H is NOT promoted to a deterministic rule because Jiang is a young,
developing player and the meetings are roughly one year old. It supports the
shape of the match tree but does not override Jiang's 2026 current-event form.

---

### Workload / exposure branch

Ferguson's two singles wins this week were completed in straight sets.

Jiang required three sets against Qian Sun on 27 August and also has a verified
two-set doubles quarterfinal on the same date.

This creates a modest Ferguson exposure/recovery advantage.

It is NOT treated as an automatic fatigue penalty: the effect is expressed only
as a slightly larger late-set deterioration branch for Jiang if the match becomes
physical or extended.

---

### Coherent qualitative match tree

#### Lower / dominant-Ferguson branch

Example shapes:
- 6-2, 6-3
- 6-3, 6-2

Mechanism:
Ferguson's stronger hold profile and second-serve stability create repeated
pressure on Jiang's weaker service games; Jiang's current return gains are
insufficient to generate enough breaks.

Helps:
- Ferguson ML
- Ferguson 1st-set ML
- Ferguson -1.5 sets
- Ferguson -5.5 games
- Under 19.5

Hurts:
- Jiang +5.5
- Jiang +1.5 sets
- Over 19.5

#### Central branch

Example shapes:
- 6-4, 6-3
- 7-6, 6-3
- 6-4, 7-5

Mechanism:
Ferguson remains the stronger server/overall player, but Jiang's current return
quality and confidence keep one or both sets competitive.

This is the most useful branch for understanding the ranking because:
- Ferguson can win comfortably enough at match level;
- Jiang +5.5 can still cover;
- Ferguson can still win 2-0;
- the match-total direction changes around the precise set scores.

#### Competitive / deciding-set branch

Example shape:
- Ferguson wins 2-1.

Mechanism:
Jiang converts a return-pressure spell or Ferguson's second serve slips for one
set, similar to both 2025 H2Hs.

Helps:
- Ferguson ML can still win;
- Jiang +5.5;
- Jiang +1.5 sets;
- usually Over 19.5.

Hurts:
- Ferguson -1.5 sets.

#### Jiang-upset branch

Mechanism:
Jiang's current Maanshan improvement is real rather than short-run variance,
his second-serve return pressure persists, and Ferguson's indoor-hard baseline
proves less stable than the overall ranking gap suggests.

This is the strongest ordinary kill path to the rank-1 Ferguson winner.

---

### Contract geometry and dependence

The forecast is one match tree, not four independent stories.

- Ferguson ML and Jiang ML are exact match-result opposites if the match
  completes under matching terms.
- Ferguson 1st-set ML and Jiang 1st-set ML are exact first-set opposites.
- Ferguson -5.5 and Jiang +5.5 are exact game-handicap opposites.
- Ferguson -1.5 sets and Jiang +1.5 sets are opposite completed-match set
  branches under standard best-of-three treatment.
- Over 19.5 and Under 19.5 are exact total-game complements under matching
  completed-match rules.

**Important overlap:** Ferguson ML and Jiang +5.5 are NOT contradictory.
A score such as Ferguson 6-4, 6-3 wins both contracts.

Likewise, Ferguson -1.5 sets and Jiang +5.5 games can both win in a close
straight-set Ferguson victory.

The top four are therefore ranked by marginal likelihood from the same match
shape; they are not intentionally diversified as a hedge.

---

## Complete frozen ranking

| Rank | Candidate | Contract | Verdict | Evidence quality | Dependence | Performance role | Actionability | Probability |
|---:|---|---|---|---|---|---|---|---|
| **1** | `P-124-C01` | **Chase Ferguson — Match Winner** | `SUPPORTED` | `MEDIUM` | `ML / MATCHTREE` | `PRIMARY_FORMAL` | `NOT ACTIONABLE UNTIL STATE RECONFIRMED` | `NOT_GENERATED` |
| **2** | `P-124-C03` | **Chase Ferguson — 1st Set Winner** | `LEAN` | `MEDIUM` | `S1 / MATCHTREE` | `CORRELATED_SECONDARY` | `NOT ACTIONABLE UNTIL STATE RECONFIRMED` | `NOT_GENERATED` |
| **3** | `P-124-C06` | **Fumin Jiang +5.5 Games** | `LEAN` | `MEDIUM` | `GH55 / MATCHTREE` | `CORRELATED_SECONDARY` | `NOT ACTIONABLE UNTIL STATE RECONFIRMED` | `NOT_GENERATED` |
| **4** | `P-124-C07` | **Chase Ferguson -1.5 Sets / Ferguson 2-0** | `LEAN` | `MEDIUM` | `SH15 / MATCHTREE` | `CORRELATED_SECONDARY` | `NOT ACTIONABLE UNTIL STATE RECONFIRMED` | `NOT_GENERATED` |
| 5 | `P-124-C10` | Over 19.5 Games | `LEAN` | `LOW` | `TOT195 / MATCHTREE` | `CORRELATED_SECONDARY` | `NOT ACTIONABLE` | `NOT_GENERATED` |
| 6 | `P-124-C08` | Fumin Jiang +1.5 Sets | `FORCED RANK` | `LOW` | `SH15 / MATCHTREE` | `CORRELATED_SECONDARY` | `NOT ACTIONABLE` | `NOT_GENERATED` |
| 7 | `P-124-C09` | Under 19.5 Games | `FORCED RANK` | `LOW` | `TOT195 / MATCHTREE` | `CORRELATED_SECONDARY` | `NOT ACTIONABLE` | `NOT_GENERATED` |
| 8 | `P-124-C05` | Chase Ferguson -5.5 Games | `AVOID` | `MEDIUM` | `GH55 / MATCHTREE` | `CORRELATED_SECONDARY` | `NOT ACTIONABLE` | `NOT_GENERATED` |
| 9 | `P-124-C04` | Fumin Jiang — 1st Set Winner | `AVOID` | `MEDIUM` | `S1 / MATCHTREE` | `CORRELATED_SECONDARY` | `NOT ACTIONABLE` | `NOT_GENERATED` |
| 10 | `P-124-C02` | Fumin Jiang — Match Winner | `AVOID` | `MEDIUM` | `ML / MATCHTREE` | `CORRELATED_SECONDARY` | `NOT ACTIONABLE` | `NOT_GENERATED` |

---

## Top-four ranking rationale

### #1 — Chase Ferguson Match Winner

This is the strongest contract because it preserves Ferguson's structural
advantages without requiring a straight-set win or large margin.

Supporting mechanisms:
- materially stronger established professional baseline;
- superior broad hold / second-serve / break-point profile;
- two straight-set wins at this event;
- 2-0 same-surface/same-venue H2H;
- modest recovery/workload advantage.

Strongest kill path:
Jiang's current upset run is a genuine regime signal and his return pressure
could expose Ferguson's serve often enough to produce a third-set coin-flip.

**Verdict:** `SUPPORTED`
**Evidence:** `MEDIUM`

### #2 — Chase Ferguson 1st Set Winner

Ferguson won the opening set in both same-venue H2Hs, 6-4 each time, and has
also won the opening set in both matches at this event.

This does not rank #1 because Jiang also won the first set in both of his wins
this week, so current-form evidence is not one-sided.

**Verdict:** `LEAN`
**Evidence:** `MEDIUM`

### #3 — Fumin Jiang +5.5 Games

This is deliberately distinguished from a Jiang match-winner call.

The central forecast can be Ferguson to win while Jiang remains close enough
in games to cover +5.5.

Supporting mechanisms:
- both 2025 H2Hs stayed inside +5.5;
- Jiang is in improved current form;
- Ferguson's first-round win over Taka was only a four-game margin;
- close straight sets or a three-set Ferguson win strongly favour this contract.

Strongest kill path:
Ferguson reproduces the 6-3, 6-2 separation he showed against Hanyi Liu or
Jiang's extra workload contributes to a late-set break cluster.

**Verdict:** `LEAN`
**Evidence:** `MEDIUM`

### #4 — Chase Ferguson -1.5 Sets / Ferguson 2-0

Ferguson has not dropped a set this week and Jiang carries the heavier verified
recent match load.

It ranks below Jiang +5.5 because both previous same-venue H2Hs went three sets
and Jiang's current return form provides a credible set-winning pathway.

A result such as 6-4, 6-3 can satisfy both rank #3 and rank #4, so the two rows
are not contradictory.

**Verdict:** `LEAN`
**Evidence:** `MEDIUM`

---

## Potential game winner

**Potential winner:** **Chase Ferguson**

**Canonical winner contract:** `P-124-C01`

**Status:** `LEAN`

**Evidence quality:** `MEDIUM`

**Central mechanism:** Ferguson combines the stronger professional baseline,
better broad service-game stability and better second-serve resistance with
two straight-set wins this week.

**Strongest failure path:** Jiang's current improvement persists, he continues
to win a high share of Ferguson second-serve return points, and the match again
moves into the three-set structure seen in both 2025 Maanshan meetings.

The winner call is therefore Ferguson, but Jiang's current form is substantial
enough that this is not treated as a certainty.

---

## Final forecast card

| Rank | Pick |
|---:|---|
| **1** | **Chase Ferguson — Match Winner** |
| **2** | **Chase Ferguson — 1st Set Winner** |
| **3** | **Fumin Jiang +5.5 Games** |
| **4** | **Chase Ferguson -1.5 Sets / Ferguson 2-0** |

**Potential game winner:** **Chase Ferguson**

**GAME-STATE:** `PREGAME / STATE VERIFICATION LIMITED`

**Forecast status:** `RANKED FORECAST — NO BET ENDORSED UNTIL STATE RECONFIRMED`

**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value state:** `NO VALUE DETERMINABLE`

---

## Important limitations

1. The exact official ITF order-of-play/start time could not be reliably
   retrieved. Current secondary sources differed by roughly 30 minutes.
2. The nominal start window had reached/passed by the final research refresh,
   while current secondary match pages still exposed no score. Official live
   state was not available.
3. Therefore this is a PRE-MATCH view only. If any point has already been
   played, it must not be relabelled as a live forecast.
4. No sportsbook was supplied by the user. MarathonBet was used only as the
   frozen reference contract universe.
5. Retirement/walkover settlement remains `UNKNOWN_DEFINITION`.
6. No tennis numerical model is approved, fitted or validated; no internal
   percentage probabilities are generated.
7. H2H is unusually relevant because the two previous meetings were at the same
   level, venue and surface, but Jiang's age/development makes one-year-old H2H
   less stable than a same-regime adult sample.
8. Specialist serve/return providers have different coverage windows and
   definitions; the figures are directional process evidence rather than
   interchangeable model features.

---

## Source record

| Source | Role |
|---|---|
| ITF Men's World Tennis Tour Calendar | Official competition dates and indoor-hard surface |
| ITF Chase Ferguson profile | Official identity and ATP-ranking snapshot |
| ITF Fumin Jiang profile | Official identity, handedness and preferred surface |
| ITF Recognised Courts register | ROGT venue-level acrylic / pace context |
| Tennis Explorer | Current ranking/form and recent singles results |
| Tennis Explorer doubles result | Jiang's verified 27 August doubles workload |
| MatchSignal / historical result cross-check | Same-venue/surface Ferguson–Jiang H2H |
| SteveG Tennis / MatchStat | Specialist serve-return/hold/break context |
| MarathonBet current match page | Frozen reference contracts and thresholds only |
| TennisStats247 / current match-state pages | Secondary start/state cross-check |

---

## Logging confirmation

**Canonical ID:** `P-124`

**Issued view:** `V01`

**Forecast prepared before any verified final:** `YES`

**Official live-state verification:** `NOT AVAILABLE`

**Result status:** `OPEN — PENDING`

**Retrospective:** `NOT INCLUDED — per current user instruction`

## P-125 — Canberra Brave vs Sydney Bears — 2026 AIHL Goodall Cup Preliminary Final

### Record metadata

| Field                                   | Recorded value                                                                                                         |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Canonical ID                            | `P-125`                                                                                                                |
| Sport                                   | Ice Hockey                                                                                                             |
| Competition                             | Australian Ice Hockey League (AIHL) — 2026 Goodall Cup Playoffs                                                        |
| Round                                   | Preliminary Final 1                                                                                                    |
| Event                                   | Canberra Brave (3rd seed) vs Sydney Bears (6th seed)                                                                   |
| Venue                                   | O’Brien Icehouse, Docklands, Melbourne, Victoria                                                                       |
| Venue status                            | Neutral finals venue                                                                                                   |
| Official/venue scheduled start          | Friday 2026-08-28, 15:00 Australia/Melbourne                                                                           |
| Australia/Melbourne research-time state | Scheduled start crossed during research                                                                                |
| Final state refresh                     | 2026-08-28 approximately 15:06 AEST                                                                                    |
| GAME-STATE                              | `START CROSSED — LIVE STATE NOT VERIFIED`                                                                              |
| Live-score verification                 | Current sources continued to expose a scheduled/no-score fixture; no trustworthy exact score/period/clock was obtained |
| Method                                  | `MDS-2026.08.28-v2.4`                                                                                                  |
| Numerical model state                   | `DESIGN ONLY / DATA BLOCKED — NO FITTED OR VALIDATED ICE-HOCKEY MODEL`                                                 |
| Probability state                       | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`                                                                   |
| Value state                             | `NO VALUE DETERMINABLE`                                                                                                |
| Result status                           | `OPEN — LIVE/FINAL STATE PENDING`                                                                                      |
| Drive write state                       | `NO WRITE — COPY-PASTE SECTION ONLY`                                                                                   |

### State-integrity warning

The official O’Brien Icehouse finals schedule lists Preliminary Final 1 for
15:00 AEST.

That scheduled time crossed during this research pass.

At the final refresh, currently accessible score services still exposed the
fixture without a trustworthy live score. Because an exact score, period and
clock could not be verified, the forecast MUST NOT be represented as a verified
live forecast.

The four original contracts are preserved and ranked from the pre-start
evidence set, but:

`LIVE STATE NOT VERIFIED — NOT ACTIONABLE AS A LIVE FORECAST`

If the game has begun, the current score/clock/manpower/goalie state must be
verified before these lines can be used as live predictions.

---

### Framework controls applied

Promoted process controls materially relevant to this card:

* `L-001` — freeze event/state/contract before analysis.
* `L-002` — separate source authority, freshness and predictive importance.
* `L-003` — derive side and total contracts from one coherent score corridor.
* `L-004` — map every source result against the exact supplied threshold.
* `L-010` — separate winner from handicap/separation probability.
* `L-011` — use scoring streaks only after tracing their mechanisms.
* `L-015` — historical cases are mechanism checks, not outcome votes.
* `L-016` — freeze the complete supplied slate before ranking.
* `L-017` — do not invent numerical probabilities.
* `L-018` — ordinal ranking remains marginal-likelihood ranking, not hedging.
* `L-021` — no value claim without a validated calibrated model and price gate.
* `L-024` — field-owning sources and final volatile refresh.
* `L-026` — unverified live state cannot control a live forecast.
* `L-027` — decision-driving participant identity must be verified.
* `L-029` — explicitly reconcile season baseline with current regime.

### Historical-development-set retrieval

**Predeclared query:**
Ice hockey → full-game side/handicap + total → pregame → two-team joint-score
process → goalie/special-teams/separation mechanism.

**Result:** `NO CLEARLY COMPARABLE D0 ICE-HOCKEY CASE RETRIEVED`

No historical Sports Research result is used as a raw vote or probability for
this game.

---

## Decision set

**Decision-set ID:** `DS-P-125-V01`

**Candidate origin:** `USER_SUPPLIED`

The complete supplied candidate slate was frozen before directional ranking.

| Candidate ID | Supplied contract              | Eligibility                               |
| ------------ | ------------------------------ | ----------------------------------------- |
| `P-125-C01`  | Canberra Brave -1.5            | `ELIGIBLE — ENDPOINT ASSUMPTION REQUIRED` |
| `P-125-C02`  | Sydney Bears +1.5              | `ELIGIBLE — ENDPOINT ASSUMPTION REQUIRED` |
| `P-125-C03`  | Combined Total Over 8.5 Goals  | `ELIGIBLE — ENDPOINT ASSUMPTION REQUIRED` |
| `P-125-C04`  | Combined Total Under 8.5 Goals | `ELIGIBLE — ENDPOINT ASSUMPTION REQUIRED` |

### Contract-definition assumption

The user did not supply an operator or operator rules.

For research/ranking purposes only, the contracts are treated as full-game
hockey contracts using the final score under the applicable competition and
operator rules.

Exact treatment of:

* regulation versus overtime;
* any playoff overtime continuation;
* any shootout;
* whether a shootout deciding goal is added to the settled total;
* abandonment/void terms;

remains:

`UNKNOWN_DEFINITION`

If the user's bookmaker uses regulation-only settlement or materially different
playoff/tiebreak accounting, the contracts must be remapped before grading.

No prices are used to create the ranking.

---

## Target definition

**TARGET_ID:** `AIHL-JOINT-FINAL-SCORE-P125-V01`

| Field                 | Definition                                                                                     |
| --------------------- | ---------------------------------------------------------------------------------------------- |
| Underlying target     | Joint Canberra Brave / Sydney Bears final goal score                                           |
| Start state           | Original pre-start state; current state verification unresolved after scheduled start crossing |
| Endpoint              | Full game under the research assumption above                                                  |
| Unit                  | Official goals                                                                                 |
| Primary exposure      | Regulation minutes, shifts, ice time, shot/chance possessions and manpower states              |
| Structural state      | Goalies, lines, special teams, score state, penalties and empty-net/pull branches              |
| Derived contracts     | Winner, ±1.5 goal handicap and 8.5 total                                                       |
| Starting goalie state | `NOT VERIFIED / NOT RELEASED THROUGH A TRUSTWORTHY OFFICIAL SOURCE AT CUTOFF`                  |
| Exact scratches/lines | `NOT VERIFIED AT FINAL REFRESH`                                                                |
| Operator settlement   | `UNKNOWN_DEFINITION`                                                                           |

---

# Event verification

The 2026 Goodall Cup playoffs are being held at O’Brien Icehouse in Melbourne
from 28–30 August.

Preliminary Final 1 is:

**Canberra Brave (3rd) vs Sydney Bears (6th)**

The winner advances to play the Melbourne Mustangs in the semifinal on
Saturday 29 August.

This is therefore an elimination playoff game at a neutral finals venue rather
than an ordinary Canberra home game.

---

# Structural baseline

## Canberra Brave

Regular-season result:

* 30 games played;
* 61 standings points;
* 152 goals for;
* 109 goals against;
* goal differential: **+43**.

Actual scoring environment:

`(152 + 109) / 30 = 8.70 total goals per played game`

This number is a descriptive baseline only. It is NOT a fitted expected total.

Specialist process snapshot:

* shot share: **55.4%**
* power play: **29.9%**
* penalty kill: **80.3%**
* penalty minutes/game: **10.8**

These indicate that Canberra's strong results were supported by a substantial
territorial/shot-share advantage and a materially productive power play rather
than only a favourable win/loss record.

## Sydney Bears

Because the postponed Perth game was ultimately cancelled, Sydney has a
standings-game accounting wrinkle. The actual played-game scoring ledger is:

* 29 games actually played;
* 130 goals for;
* 131 goals against;
* actual played-game goal differential: **-1**.

Actual played-game scoring environment:

`(130 + 131) / 29 = 9.00 total goals per played game`

Again, this is descriptive evidence rather than a numerical forecast.

Specialist process snapshot:

* shot share: **50.6%**
* power play: **21.9%**
* penalty kill: **80.0%**
* penalty minutes/game: **15.6**

Sydney therefore enters with a much smaller overall territorial edge than
Canberra and with a weaker power play, while taking substantially more penalty
minutes in the season-level specialist snapshot.

---

# Current offensive regime

## Canberra scoring depth

Important current scoring contributors include:

* Jake Ratcliffe — **61 points in 23 games**
* Casey Kubara — **49 points in 25 games**
* Bray Crowder — **39 points in 26 games**
* Peter Bates — **36 points in 14 games**

Canberra's threat is therefore not dependent on one scorer.

The combination of high-end forwards, productive defence and a strong power
play supports multiple scoring paths.

## Sydney scoring regime

Important current contributors include:

* Lucas Herrmann — **53 points in 27 games**
* Nick Seitz — **28 points in 11 games**, including 18 goals

Sydney's raw season ranking understates the offensive danger of the current
Seitz/Herrmann regime.

However, Gustav Remler-Jensen departed the club during August after recording
10 goals and 18 assists in 25 games.

Therefore the current Sydney attack should neither be treated as the exact
same unit that produced its full-season totals nor dismissed because of the
team's sixth-place seed.

---

# Recent process

## Canberra

Recent completed games:

| Date   | Opponent             |   Result | Total goals |
| ------ | -------------------- | -------: | ----------: |
| 23 Aug | Melbourne Mustangs   | L 4-5 OT |           9 |
| 22 Aug | Melbourne Ice        | L 3-4 SO |           7 |
| 16 Aug | Brisbane Lightning   |    W 9-4 |          13 |
| 15 Aug | Newcastle Northstars |    W 6-3 |           9 |
| 9 Aug  | Melbourne Ice        |    W 5-2 |           7 |

Raw Over-8.5 result: **3 of 5**.

The streak itself is not the mechanism.

More important:

* Canberra outshot the Mustangs **37-30** in the 4-5 OT loss;
* Canberra erased a 3-0 first-period deficit to lead 4-3;
* Melbourne tied the game late and won in overtime on a power-play sequence.

That result does not show Canberra suddenly lost its territorial capability.
It shows a credible close-game / special-teams / late-state failure path.

Both of Canberra's final regular-season games were played at O’Brien Icehouse
and were decided by one goal after regulation.

That matters to the **Bears +1.5** branch.

## Sydney Bears

Recent completed games:

| Date   | Opponent             |   Result | Total goals |
| ------ | -------------------- | -------: | ----------: |
| 23 Aug | Newcastle Northstars |    L 5-8 |          13 |
| 15 Aug | Perth Thunder        |   W 10-5 |          15 |
| 9 Aug  | Central Coast Rhinos |    W 4-2 |           6 |
| 2 Aug  | Melbourne Ice        |    W 6-2 |           8 |
| 26 Jul | Central Coast Rhinos | W 7-6 SO |          13 |

Raw Over-8.5 result: **3 of 5**.

Again, the result sequence is diagnostic rather than controlling.

The mechanisms are more informative:

* Sydney demonstrated a genuine high-output ceiling by scoring 10 against Perth.
* Against Newcastle, Sydney led **5-3 after two periods** before conceding five
  unanswered third-period goals.
* That game exposes both the Bears' scoring ceiling and their defensive
  late-game volatility.

This supports a wider upper-total/separation tail rather than a simple claim
that Sydney is an automatic Over team.

---

# 2026 head-to-head audit

The two 2026 meetings were:

### 4 July — Sydney Bears 6, Canberra Brave 7 OT

* Canberra SOG: **42**
* Sydney SOG: **36**
* Total goals: **13**
* Canberra margin: **+1**

Contract mapping:

* Brave -1.5: LOSS
* Bears +1.5: WIN
* Over 8.5: WIN
* Under 8.5: LOSS

### 5 July — Canberra Brave 7, Sydney Bears 3

* Canberra SOG: **48**
* Sydney SOG: **25**
* Total goals: **10**
* Canberra margin: **+4**

Contract mapping:

* Brave -1.5: WIN
* Bears +1.5: LOSS
* Over 8.5: WIN
* Under 8.5: LOSS

### H2H interpretation

The H2H is useful because both meetings occurred in the current 2026 season.

It shows:

1. Canberra won both games.
2. Canberra generated a clear shot edge in both.
3. One meeting remained inside the Bears +1.5 cushion.
4. One meeting produced a large Canberra separation.
5. Both cleared 8.5 goals.

It does NOT establish an automatic Canberra cover or automatic Over.

The current playoff is at a neutral venue, has different current roster states,
and carries elimination-game score-state incentives.

---

# Goalie and participant uncertainty

Starting goalie is a regime variable under the active ice-hockey rules.

Canberra's official team page lists the current goaltender pool including:

* Joel Hasselman
* Victor Sjodin
* Alex Tetreault

A trustworthy official starting-goalie confirmation for this exact playoff was
not obtained at cutoff.

The same applies to Sydney's exact starter.

Therefore:

`STARTING GOALIES = NOT VERIFIED`

No goalie is silently assumed.

This is especially material to:

* the 8.5 total;
* the probability of a one-goal versus multi-goal result;
* rebound/second-chance quality;
* late pulling/empty-net scenarios.

It materially lowers forecast certainty.

---

# Matchup mechanism

## Canberra offensive path

Canberra owns the stronger overall process profile:

`shot-share edge -> offensive-zone/chance volume -> penalty-drawing/manpower
opportunity -> strong PP conversion -> multi-goal ceiling`

Sydney's season-level penalty rate creates a particularly important branch.

If Sydney gives Canberra repeated power-play opportunities, the Canberra
separation and Over tails rise together.

## Sydney offensive path

Sydney's current top-end scoring creates a real counterweight:

`Herrmann/Seitz scoring quality -> transition/finishing -> Canberra goalie
variance -> Sydney 3-5 goal contribution`

Sydney does not need to dominate shots for this path to occur.

Its 6-2 win over Melbourne Ice and recent 10-goal output show that efficient
finishing can produce high totals even when territorial dominance is not
continuous.

## Defensive / Under path

The Under requires a more specific chain:

* both starting goalies perform above the broad team defensive baseline;
* elimination-game discipline suppresses penalty volume;
* Canberra controls possession without converting its shot edge at an extreme rate;
* Sydney's current top scorers are held below their recent ceiling;
* no late empty-net sequence adds the ninth goal.

That branch is credible.

It is not the central branch supported by the combined season/current evidence.

---

# Coherent qualitative score corridor

No numerical probability or fitted expected score is generated.

### Lower-scoring / goalie-control branch

Representative shapes:

* Canberra 4-3
* Canberra 5-3
* Sydney 4-3

Mechanisms:

* strong goaltending;
* limited special teams;
* playoff risk control;
* weak conversion despite adequate shot volume.

Favours:

* Bears +1.5 in the one-goal branches;
* Under 8.5;
* Canberra -1.5 only in a 5-3-type separation.

### Central competitive-Canberra branch

Representative shapes:

* Canberra 5-4
* Canberra 6-4
* Canberra 5-3

Mechanisms:

* Canberra owns more of the shot/chance process;
* Sydney still generates meaningful scoring through its top-end forwards;
* exact conversion and special-team state determine whether Canberra separates.

This branch explains why:

* Canberra can be the potential winner;
* Bears +1.5 can simultaneously be the strongest handicap;
* Over 8.5 can rank above Under 8.5.

### Canberra separation branch

Representative shapes:

* Canberra 6-3
* Canberra 6-4
* Canberra 7-3

Mechanisms:

* Canberra's shot-share advantage translates cleanly;
* Sydney takes penalties;
* Canberra's PP converts;
* Sydney's defensive structure deteriorates while chasing;
* empty-net or late transition exposure expands the margin.

Favours:

* Brave -1.5;
* mostly Over 8.5.

### Sydney upset branch

Representative shapes:

* Sydney 5-4
* Sydney 6-4

Mechanisms:

* Seitz/Herrmann finishing remains hot;
* Canberra's goalie branch underperforms;
* Sydney scores efficiently without needing the larger shot share;
* Canberra's PP fails to convert its territorial edge.

Favours:

* Bears +1.5;
* Sydney winner;
* usually Over 8.5.

---

# Strongest kill paths

### Sydney Bears +1.5

**Kill path:** Canberra converts its territorial and special-teams advantage into
an early multi-goal lead and Sydney's chasing state creates further transition
or empty-net separation.

A 6-3 / 7-3 type result defeats the cushion.

### Over 8.5

**Kill path:** playoff pace is controlled, penalties remain low, and the starting
goalies suppress conversion enough to produce a 4-3 / 5-3 corridor.

### Canberra Brave -1.5

**Kill path:** Canberra is still the better team but wins by exactly one, or the
game reaches a tied late state/overtime.

This is a particularly important distinction: **Canberra winning does not imply
Canberra -1.5 winning.**

### Under 8.5

**Kill path:** either club converts the current offensive ceiling, special teams
add scoring, or the trailing side creates late empty-net/transition exposure.

---

# Contract geometry and dependence

### Handicap pair

`P-125-C01` Canberra Brave -1.5
vs
`P-125-C02` Sydney Bears +1.5

Under matching settlement terms these are exact opposites.

* Brave -1.5 wins if Canberra finishes at least two goals ahead.
* Bears +1.5 wins if Sydney wins or loses by exactly one.

There is no push at 1.5.

### Total pair

`P-125-C03` Over 8.5
vs
`P-125-C04` Under 8.5

Under matching settlement terms these are exact complements.

* Over wins at 9+ settled goals.
* Under wins at 8 or fewer.

There is no push at 8.5.

### Cross-pair dependence

The two pairs are not independent.

Examples:

* Canberra 5-4 -> Bears +1.5 + Over 8.5
* Canberra 6-4 -> Brave -1.5 + Over 8.5
* Canberra 5-3 -> Brave -1.5 + Under 8.5
* Sydney 5-4 -> Bears +1.5 + Over 8.5

Therefore the ranking is derived from one qualitative joint-score corridor
rather than four separate narratives.

---

# Final ranking

Because the scheduled start crossed and exact live state could not be verified,
all rows carry a state-integrity cap.

|  Rank | Candidate ID | Exact contract          | Verdict                                      | Evidence                            | Dependence               | Performance role       | Actionability                              | Probability     |
| ----: | ------------ | ----------------------- | -------------------------------------------- | ----------------------------------- | ------------------------ | ---------------------- | ------------------------------------------ | --------------- |
| **1** | `P-125-C02`  | **Sydney Bears +1.5**   | `FORCED RANK — PRE-START DIRECTION FAVOURED` | `MEDIUM-LOW — STATE LIMITED`        | `PUCKLINE / JOINT-SCORE` | `PRIMARY_FORMAL`       | `NOT ACTIONABLE — LIVE STATE NOT VERIFIED` | `NOT_GENERATED` |
| **2** | `P-125-C03`  | **Over 8.5 Goals**      | `FORCED RANK — PRE-START DIRECTION FAVOURED` | `MEDIUM-LOW — GOALIE/STATE LIMITED` | `TOTAL / JOINT-SCORE`    | `CORRELATED_SECONDARY` | `NOT ACTIONABLE — LIVE STATE NOT VERIFIED` | `NOT_GENERATED` |
| **3** | `P-125-C01`  | **Canberra Brave -1.5** | `FORCED RANK`                                | `MEDIUM-LOW — STATE LIMITED`        | `PUCKLINE / JOINT-SCORE` | `CORRELATED_SECONDARY` | `NOT ACTIONABLE — LIVE STATE NOT VERIFIED` | `NOT_GENERATED` |
| **4** | `P-125-C04`  | **Under 8.5 Goals**     | `FORCED RANK — EVIDENCE OPPOSED`             | `MEDIUM-LOW — GOALIE/STATE LIMITED` | `TOTAL / JOINT-SCORE`    | `CORRELATED_SECONDARY` | `NOT ACTIONABLE — LIVE STATE NOT VERIFIED` | `NOT_GENERATED` |

---

# Detailed ranking rationale

## #1 — Sydney Bears +1.5

This is the strongest pre-start contract despite Canberra being the stronger
potential winner.

The contract wins in:

* every Sydney outright-win branch;
* every one-goal Canberra win;
* any overtime/late-tied branch that ultimately leaves Sydney within one goal
  under matching settlement rules.

Canberra's season and shot-process advantages make Canberra the preferred winner,
but they do not automatically make a two-goal margin the most robust outcome.

Specific support:

* the 4 July H2H finished Canberra 7-6 OT;
* Canberra's final two regular-season games at this exact venue were both
  one-goal games beyond regulation;
* Sydney has enough current scoring quality to remain attached even when
  outshot.

The largest threat is Canberra's PP/shot-share edge creating an early separation
that forces Sydney into an increasingly open chasing state.

**Pre-start directional assessment:** strongest of the four.

---

## #2 — Over 8.5 Goals

The total sits close to the natural scoring environment of these teams rather
than far above it.

Supporting mechanisms:

* Canberra's actual regular-season game environment: 8.70 total goals/game;
* Sydney's 29 actually played games: 9.00 total goals/game;
* the two 2026 H2Hs produced 13 and 10 goals;
* Canberra has multiple high-rate scorers;
* Sydney's current Seitz/Herrmann combination gives the underdog a credible
  3-5 goal contribution;
* Canberra's 29.9% PP versus Sydney's higher penalty rate creates a direct
  special-teams scoring path;
* both teams have recent high-total outcomes;
* playoff trailing/empty-net state can add late tail scoring.

The reason this does not rank #1 is the unknown goalie state and a genuine
playoff suppression branch.

**Pre-start directional assessment:** Over preferred to Under.

---

## #3 — Canberra Brave -1.5

Canberra has the clearest structural path to a multi-goal win:

* +43 season goal differential;
* 55.4% shot share;
* materially stronger PP;
* deeper demonstrated scoring;
* two 2026 victories over Sydney;
* a 48-25 SOG advantage in the 7-3 meeting.

But this contract asks for substantially more than "Canberra is better."

A Canberra 5-4 win, 4-3 win, or any one-goal overtime result loses -1.5.

Because that close-game branch is material, Canberra -1.5 stays below
Bears +1.5 despite Canberra remaining the preferred game winner.

---

## #4 — Under 8.5 Goals

The Under has a coherent path and is not dismissed.

Its best scenario is:

`strong goalies + disciplined playoff game + lower special-teams exposure +
Canberra possession control without extreme finishing + no late empty-net ninth
goal`

The problem is that more of the current evidence points the other direction:

* both teams' played-game scoring environments sit around the line;
* both 2026 H2Hs went Over 8.5;
* Sydney's current high-end scorers increase its contribution ceiling;
* Sydney's recent defensive volatility widens Canberra's upper tail;
* Canberra's PP and Sydney's penalty profile create a direct high-scoring branch.

Therefore Under 8.5 ranks fourth.

---

# Potential game winner

**Potential winner:** **Canberra Brave**

**Winner status:** `FORCED WINNER — LOW CONFIDENCE DUE UNVERIFIED CURRENT STATE`

**Evidence quality:** `MEDIUM pre-start / LOW for current live use`

**Central mechanism:**

Canberra owns the stronger full-season process:

* substantially better goal differential;
* superior shot share;
* much stronger power play;
* lower penalty burden;
* deeper current scoring;
* two wins over Sydney in the current season.

The strongest ordinary failure path is Sydney's current finishing regime
outperforming its territorial share while Canberra's unverified starting-goalie
branch underperforms.

### Important distinction

Potential winner:

**Canberra Brave**

Strongest handicap:

**Sydney Bears +1.5**

These statements are coherent.

The central game tree includes a substantial:

**Canberra wins by exactly one goal**

branch, in which both forecasts are correct.

---

# Final forecast card

|  Rank | Pick                                 |
| ----: | ------------------------------------ |
| **1** | **Sydney Bears +1.5**                |
| **2** | **Combined Total — Over 8.5 Goals**  |
| **3** | **Canberra Brave -1.5**              |
| **4** | **Combined Total — Under 8.5 Goals** |

**Potential game winner:** **Canberra Brave**

**GAME-STATE:**
`START CROSSED — LIVE STATE NOT VERIFIED`

**Current actionability:**
`NOT ACTIONABLE AS A LIVE FORECAST UNTIL SCORE/PERIOD/CLOCK ARE VERIFIED`

**Probability state:**
`NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value state:**
`NO VALUE DETERMINABLE`

**Forecast status:**
`RANKED PRE-START EVIDENCE VIEW — STATE VERIFICATION CAP`

---

# Source record

| Source                                               | Source class                                       | Decision-driving field                                                          |
| ---------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------- |
| O’Brien Icehouse — AIHL Finals 2026                  | Official venue                                     | Finals schedule, venue, 15:00 scheduled start                                   |
| Ice Hockey News Australia — 23 Aug standings/results | Specialist league reporting linked to AIHL sources | Final seeds, records, recent results and SOG                                    |
| Eurohockey AIHL 2026 table                           | Established hockey database                        | Actual played-game goals for/against; cancelled-game distinction                |
| AIHL Forecaster                                      | Specialist research source                         | SF%, PP%, PK%, PIM/G and contextual strength data                               |
| Ice Hockey News Australia — 4 July                   | Specialist event record                            | 7-6 OT H2H and SOG 42-36                                                        |
| Ice Hockey News Australia / result archive — 5 July  | Specialist event record                            | 7-3 H2H and SOG 48-25                                                           |
| Canberra Brave official team page                    | Team official                                      | Current published goalie/player pool                                            |
| Elite Prospects                                      | Specialist player database                         | Current-season scoring profiles                                                 |
| Ice Hockey News Australia — Remler-Jensen departure  | Specialist current reporting                       | Sydney roster-regime change                                                     |
| Current 365Scores / Flashscore searches              | State cross-check                                  | No trustworthy live score exposed at final refresh                              |
| Current sportsbook pages                             | Market-state cross-check only                      | Confirmed the supplied contract family exists; NOT used as internal probability |

---

# Important limitations

1. **The scheduled start crossed during research.**
   A trustworthy exact live score/period/clock was not obtained.

2. **Starting goalies were not officially verified.**
   No goalie-specific forecast assumption is presented as fact.

3. **Exact current lines/scratches were not officially verified.**

4. **The operator was not supplied.**
   OT/playoff-tiebreak/settlement treatment is therefore
   `UNKNOWN_DEFINITION`.

5. **Sydney's cancelled Perth game creates standings-count bookkeeping.**
   Played-game scoring analysis uses 29 actual scored games rather than
   inventing goals for the cancelled game.

6. **AIHL Forecaster is a specialist external research source.**
   Its process statistics are supporting evidence; its Elo outputs are not
   internal Sports Research probabilities.

7. **No numerical ice-hockey model is fitted or validated.**
   No percentage probability is invented.

8. **H2H does not vote automatically.**
   The two 2026 meetings are used because they expose current-season
   shot/margin/total mechanisms, not because "both went Over" guarantees another
   Over.

9. **The four contracts form two exact complementary pairs.**
   They are one dependent event unit, not four independent forecasts.

---

# Logging confirmation

**Canonical ID:** `P-125`

**Issued view:** `V01`

**Storage mode:**
`COPY-PASTE MARKDOWN PROVIDED TO USER — NO GOOGLE DRIVE WRITE`

**Forecast document modified:** `NO`

**Google Drive modified:** `NO`

**First demonstrable forecast artifact:** this pre-result conversation response,
subject to the unresolved exact game-state caveat above.

**Result status:** `OPEN — LIVE/FINAL STATE PENDING`

**Retrospective:** `NOT INCLUDED — per current user instruction`

## P-126 — Sikkim Aakraman FC vs Sikkim Boys Club — SFA A Division S-League

### Record metadata

| Field                                              | Recorded value                                                                                                            |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Canonical ID                                       | `P-126`                                                                                                                   |
| Sport                                              | Soccer                                                                                                                    |
| Competition                                        | India — SFA A Division S-League 2026                                                                                      |
| Event                                              | Sikkim Aakraman FC vs Sikkim Boys Club                                                                                    |
| Venue                                              | Paljor Stadium, Gangtok expected from competition scheduling; exact fixture venue not independently reconfirmed at cutoff |
| Venue-local timezone                               | `Asia/Kolkata`                                                                                                            |
| Schedule                                           | `CONFLICTING`                                                                                                             |
| Current stronger schedule branch                   | 2026-08-29 11:00 IST                                                                                                      |
| Conflicting branch                                 | Multiple current feeds list 2026-08-28                                                                                    |
| Australia/Melbourne equivalent if 29 Aug 11:00 IST | 2026-08-29 15:30 AEST                                                                                                     |
| GAME-STATE                                         | `PREGAME / SCHEDULE CONFLICT — NO VERIFIED LIVE STATE`                                                                    |
| Official starting XI                               | `NOT_RELEASED / NOT AVAILABLE`                                                                                            |
| Official goalkeeper identities                     | `NOT_RELEASED / NOT AVAILABLE`                                                                                            |
| Method                                             | `MDS-2026.08.28-v2.4`                                                                                                     |
| Numerical model                                    | `NOT FIT / NOT VALIDATED`                                                                                                 |
| Probability state                                  | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`                                                                      |
| Value state                                        | `NO VALUE DETERMINABLE`                                                                                                   |
| Storage mode                                       | `COPY-PASTE MARKDOWN ONLY — NO DRIVE WRITE`                                                                               |

### State and identity warning

Current fixture providers disagree on whether this match is scheduled for
28 August or 29 August 2026.

Current 29-August branch:

* The Away End: 29 August, 11:00 IST.
* Sofascore: 29 August, 05:30 UTC / 11:00 IST.
* Additional current fixture reporting also supports the 29-August branch.

Current 28-August branch:

* AiScore.
* ScoutMe.
* FootballAnt.
* TotalCorner/current market feeds.

No authoritative current Sikkim Football Association order-of-play was
recovered that definitively resolves this conflict.

The earlier-start feeds were not exposing a trustworthy scored live state at
the final research refresh.

Therefore:

`GAME-STATE: PREGAME / SCHEDULE CONFLICT — NO VERIFIED LIVE STATE`

If a verified live score is visible at the user's operator, this pregame view
must not be relabelled as a live forecast.

---

## Framework controls applied

Relevant active process controls:

* `L-001` — exact identity/state/contract freeze.
* `L-002` — source authority/freshness separated.
* `L-003` — one coherent regulation-goal corridor.
* `L-004` — exact threshold classification.
* `L-007` — model the settled target itself.
* `L-011` — streaks require mechanisms.
* `L-015` — historical cases challenge process, not vote on outcomes.
* `L-016` — candidate universe frozen before ranking.
* `L-017` — no invented probabilities.
* `L-018` — marginal likelihood ranking, not hedging.
* `L-021` — no value claim without validated probabilities/prices.
* `L-023` — derivative markets require their own target-event chain.
* `L-024` — field-owning source routing.
* `L-026` — unverified live states cannot drive directional live analysis.
* `L-029` — current-regime evidence and broad baseline retained separately.
* `L-030` — stale/placeholder score states are quarantined.

Soccer-specific controls:

* sparse local competition + unverified XI/keeper caps side confidence;
* goals and corners are separate target processes;
* corner dominance cannot be inferred from goals/possession;
* missing direct corner-causing evidence caps the corner row at `FORCED RANK`;
* rain/weather effects must be mechanism-specific.

---

## Candidate universe

**Decision-set ID:** `DS-P-126-V01`

**Candidate policy:** user supplied the 0.5 first-half goal line and 2.5
full-match goal line and explicitly authorised analyst-selected team/corner picks.

Frozen candidates:

| Candidate ID | Contract                                     | Origin                                                                | Eligibility                                                        |
| ------------ | -------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------------------------ |
| `P-126-C01`  | Sikkim Aakraman FC — regulation Match Winner | Analyst-selected                                                      | `ELIGIBLE`                                                         |
| `P-126-C02`  | 1st Half Goals Over 0.5                      | User-supplied branch                                                  | `ELIGIBLE`                                                         |
| `P-126-C03`  | 1st Half Goals Under 0.5                     | User-supplied branch                                                  | `ELIGIBLE`                                                         |
| `P-126-C04`  | Combined Total Goals Over 2.5                | User-supplied branch                                                  | `ELIGIBLE`                                                         |
| `P-126-C05`  | Combined Total Goals Under 2.5               | User-supplied branch                                                  | `ELIGIBLE`                                                         |
| `P-126-C06`  | Total Corners Over 7.5 — research threshold  | Analyst-selected / same sparse-local corner research threshold family | `ELIGIBLE FOR RESEARCH RANKING; OPERATOR AVAILABILITY UNCONFIRMED` |

No price-derived probability is used.

---

# Target definitions

## Goal target

**TARGET_ID:** `SOC-SIKKIM-REG-GOALS-P126-V01`

| Field                  | Definition                                                   |
| ---------------------- | ------------------------------------------------------------ |
| Outcome                | Regulation joint score `(Aakraman goals, Sikkim Boys goals)` |
| Unit                   | Official regulation goals                                    |
| Start                  | Pregame                                                      |
| Endpoint               | 90 minutes + official stoppage time                          |
| Extra time / penalties | Not applicable to league regulation target                   |
| Derived contracts      | Regulation winner, 1H O/U 0.5, FT O/U 2.5                    |
| Exact operator         | Not supplied                                                 |
| Void/abandonment terms | `UNKNOWN_DEFINITION`                                         |

## Corner target

**TARGET_ID:** `SOC-SIKKIM-CORNERS-P126-V01`

| Field                   | Definition                                                                                                |
| ----------------------- | --------------------------------------------------------------------------------------------------------- |
| Outcome                 | Combined regulation corners                                                                               |
| Unit                    | Corners under named provider                                                                              |
| Research threshold      | Over 7.5                                                                                                  |
| Exact operator/provider | Not supplied                                                                                              |
| Current direct data     | Team corners for/conceded and recent match totals                                                         |
| Missing direct data     | crosses, blocked crosses, end-line entries, clearance events, set-play process, confirmed width/formation |
| Verdict ceiling         | `FORCED RANK`                                                                                             |
| Settlement state        | `UNKNOWN_DEFINITION` until provider is known                                                              |

---

# Participant verification

**Official starting XI — Sikkim Aakraman:** `NOT AVAILABLE`

**Official starting XI — Sikkim Boys:** `NOT AVAILABLE`

**Official goalkeepers:** `NOT AVAILABLE`

**Formation:** `NOT AVAILABLE`

**Current penalty/set-piece taker confirmation:** `NOT AVAILABLE`

No unverified player is treated as definitely starting.

This is a low-information local league and therefore side confidence is capped
under the active sparse-participant rule.

---

# Current league baseline

## Sikkim Aakraman

Reconstructed current league results:

| Opponent           | Result |
| ------------------ | -----: |
| Northerners        |  W 3-1 |
| Sang Mustang       |  W 3-0 |
| Gangtok Himalayan  |  W 2-0 |
| Sikkim Brotherhood |  W 1-0 |
| Dzongri            |  W 6-1 |
| Red Panda          |  W 2-1 |
| Howlers            |  W 5-0 |
| Sikkim Police      |  W 1-0 |

**Reconstructed league record:** 8 wins, 0 draws, 0 losses.

**Goals:** 23 for, 3 against.

The important mechanism is not simply the perfect record.

Aakraman have demonstrated both:

1. a separation branch — 3-1, 3-0, 6-1, 5-0;
2. a control branch — 2-0, 1-0, 1-0.

This means a strong winner forecast does not automatically require a high total.

---

## Sikkim Boys

Reconstructed current league results:

| Opponent           | Result |
| ------------------ | -----: |
| Sikkim Police      |  L 3-4 |
| Northerners        |  L 0-1 |
| Sang Mustang       |  L 1-2 |
| Gangtok Himalayan  |  D 1-1 |
| Sikkim Brotherhood |  L 1-6 |
| Dzongri            |  L 2-4 |
| Red Panda          |  L 0-6 |
| Howlers            |  W 8-3 |

**Reconstructed league record:** 1 win, 1 draw, 6 losses.

**Goals:** 16 for, 27 against.

The 8-3 win against Howlers is a material current-regime signal.

It proves Boys have a legitimate upper attacking tail and prevents the current
card from simply treating their season record as deterministic.

However, one 8-goal performance against Howlers is shrunk against the broader
league regime because Aakraman have conceded only three goals in eight league
matches.

---

# First-half goal evidence

Aakraman:

* at least one first-half goal in 6 of 8 reconstructed league games;
* recent HT states include 1-0 vs Police, 2-0 vs Howlers, 2-1 vs Red Panda and
  2-1 vs Dzongri;
* two meaningful 0-0 HT exceptions exist.

Sikkim Boys:

* at least one first-half goal in 7 of 8 reconstructed league games;
* each of the latest five had a first-half goal;
* recent first-half states include 3-1 vs Howlers, 0-3 vs Red Panda,
  0-1 vs Dzongri and 0-4 vs Brotherhood.

Mechanism:

`Aakraman early chance creation + Boys defensive instability + Boys transition
threat -> broad first-half scoring pathway`

Kill path:

`Aakraman possession control + low Boys block + wet surface/poor finishing ->
0-0 HT`

---

# Full-match goal evidence

Aakraman games Over 2.5:

**5 of 8**

Boys games Over 2.5:

**6 of 8**

Boys' four latest high-variance games:

* 1-6
* 2-4
* 0-6
* 8-3

All cleared 2.5.

The total is not ranked purely from those outcomes.

Central mechanisms:

1. Aakraman can create repeated chances against a defence conceding heavily.
2. Boys' current attack has a credible non-zero scoring branch after the
   Howlers performance.
3. An early Aakraman goal can force Boys into a more open trailing state.
4. Aakraman's own control game can still suppress the match into 1-0 or 2-0.

The 1-0 / 2-0 branch is why Over 2.5 does not outrank the first-half Over 0.5.

---

# Corner evidence

Current recoverable Aakraman corner totals:

* vs Sikkim Police: 6
* vs Howlers: 7
* vs Red Panda: 10
* vs Dzongri: 7
* vs Brotherhood: 8

Current recoverable Sikkim Boys corner totals:

* vs Howlers: 5
* vs Red Panda: 8
* vs Dzongri: 12
* vs Brotherhood: 11
* vs Gangtok Himalayan: 9

Recent observed distributions therefore support a broad 7-9 central corner
region with significant variance.

Historical Aakraman-Boys recorded H2H corner totals include:

* 4
* 13

This is too variable to treat H2H as a controlling prior.

### Missing corner mechanism

No reliable current data was recovered for:

* crossing volume;
* blocked crosses;
* end-line entries;
* defensive-clearance counts;
* current tactical width;
* confirmed winger/fullback roles;
* exact operator/stat-provider definition.

Therefore:

**Total Corners Over 7.5 = `FORCED RANK`, not `LEAN`.**

This line is a research threshold and should only be used if the user's operator
actually offers the same contract/provider definition.

---

# Weather/context

Current IMD warnings for Sikkim:

* 28 August: heavy-rain / thunderstorm-lightning warning.
* 29 August: thunderstorm/lightning warning.

Because the match schedule itself is conflicting, exact match-window conditions
cannot be frozen confidently.

Weather is bidirectional:

* poor surface/heavy rain may suppress clean combination play and finishing;
* it may also increase defensive errors, blocks, clearances and set plays.

No automatic weather-Under or weather-corner-Over adjustment is applied.

---

# Historical process reference

Prior Sports Research record `P-088` covered Howlers vs Sikkim Boys in this
same competition.

It established useful process warnings:

* official/current XIs may be unavailable;
* sparse-local team records do not remove participant uncertainty;
* direct corner-generation evidence is incomplete;
* corner settlement sources can remain unreliable after the final.

P-088's actual result is **not used as a forecast weight**.

Its process warnings are retained only to prevent repeating the same
source/derivative errors.

---

# Scenario map

| Scenario    | Match shape                                                            | Contracts helped                  |
| ----------- | ---------------------------------------------------------------------- | --------------------------------- |
| Lower       | Aakraman dominate but finish poorly; 1-0 / 2-0                         | Aakraman ML, Under 2.5            |
| Central     | Aakraman create early pressure and win 2-1 / 3-0 / 3-1                 | Aakraman ML, 1H O0.5, O2.5        |
| Upper       | Boys' defence collapses and/or contributes themselves; 4-1 / 5-1 / 4-2 | Aakraman ML, O2.5, likely 1H O0.5 |
| Upset       | Boys' Howlers-level attacking efficiency persists; 1-2 / 2-3           | O2.5, 1H O0.5, Aakraman ML fails  |
| Corner-low  | Early clean goals reduce prolonged crossing/clearance sequences        | Corner O7.5 fails                 |
| Corner-high | Boys trail and chase wide; repeated blocks/clearances/set plays        | Corner O7.5 helped                |

---

# Complete ranking

|  Rank | Candidate   | Contract                                        | Verdict       | Evidence                                | Dependence               | Actionability                                           | Probability     |
| ----: | ----------- | ----------------------------------------------- | ------------- | --------------------------------------- | ------------------------ | ------------------------------------------------------- | --------------- |
| **1** | `P-126-C01` | **Sikkim Aakraman FC — Match Winner**           | `FORCED RANK` | `MEDIUM-LOW — participant/schedule cap` | `GOAL TREE`              | `NO VALUE DETERMINABLE`                                 | `NOT_GENERATED` |
| **2** | `P-126-C02` | **1st Half Over 0.5 Goals**                     | `LEAN`        | `MEDIUM`                                | `GOAL TREE / FIRST HALF` | `NO VALUE DETERMINABLE`                                 | `NOT_GENERATED` |
| **3** | `P-126-C04` | **Combined Total Over 2.5 Goals**               | `LEAN`        | `MEDIUM`                                | `GOAL TREE`              | `NO VALUE DETERMINABLE`                                 | `NOT_GENERATED` |
| **4** | `P-126-C06` | **Total Corners Over 7.5 — research threshold** | `FORCED RANK` | `LOW-MEDIUM`                            | `CORNER TREE`            | `NOT ACTIONABLE UNTIL OPERATOR LINE/PROVIDER CONFIRMED` | `NOT_GENERATED` |
|     5 | `P-126-C05` | Combined Total Under 2.5 Goals                  | `AVOID`       | `MEDIUM`                                | `GOAL TREE`              | `NO VALUE DETERMINABLE`                                 | `NOT_GENERATED` |
|     6 | `P-126-C03` | 1st Half Under 0.5 Goals                        | `AVOID`       | `MEDIUM`                                | `GOAL TREE / FIRST HALF` | `NO VALUE DETERMINABLE`                                 | `NOT_GENERATED` |

---

# Ranking rationale

## #1 — Sikkim Aakraman FC Match Winner

Aakraman own the strongest overall regulation-win pathway:

* reconstructed 8-0-0 league record;
* 23-3 league goal differential;
* multiple strong scoring paths;
* multiple controlled clean-sheet paths;
* Sikkim Boys have lost six of eight league games;
* Boys' defensive concession regime remains severe despite their latest win.

The strongest failure path is Boys carrying their 8-3 attacking regime forward
while Aakraman's currently unverified XI/goalkeeper differs materially from
recent matches.

Because official participants are not confirmed, the row is capped at
`FORCED RANK / MEDIUM-LOW`.

---

## #2 — 1st Half Over 0.5 Goals

This has the strongest direct threshold-specific evidence of the supplied goal
markets.

A first-half goal appeared in:

* 6/8 reconstructed Aakraman games;
* 7/8 reconstructed Boys games;
* all five latest Boys matches.

Aakraman's early attacking strength and Boys' repeated first-half concessions
create several independent scoring routes.

Kill path: controlled Aakraman possession, compact Boys defence and poor
finishing produce 0-0 HT.

---

## #3 — Combined Total Over 2.5 Goals

The matchup supports a higher-scoring branch through:

* Boys' defensive leakage;
* Aakraman's scoring ceiling;
* Boys' newly demonstrated attacking ceiling;
* open trailing-state possibilities.

However, Aakraman have repeatedly demonstrated a 1-0/2-0 control branch.

That lowers the Over 2.5 ranking below the first-half Over 0.5.

---

## #4 — Total Corners Over 7.5

Recent direct corner counts provide some support, especially through a likely
Boys trailing/chasing branch.

However, the direct corner-causing chain is incomplete.

This contract therefore remains:

`FORCED RANK — LOW-MEDIUM`

and is not upgraded merely because Aakraman are likely to dominate the match.

---

# Potential winner

**Potential winner:** **Sikkim Aakraman FC**

**Canonical contract:** `P-126-C01`

**Winner status:** `FORCED WINNER — LOW CONFIDENCE`

The low-confidence token reflects sparse participant/schedule verification,
not a belief that the teams are evenly matched.

The football evidence itself clearly favours Aakraman.

Strongest upset path:

Sikkim Boys reproduce the unusually efficient transition/finishing state from
their 8-3 win while Aakraman's unavailable participant information hides a
meaningful lineup change.

---

# Final forecast card

|  Rank | Pick                                                                               |
| ----: | ---------------------------------------------------------------------------------- |
| **1** | **Sikkim Aakraman FC — Match Winner**                                              |
| **2** | **1st Half Goals — Over 0.5**                                                      |
| **3** | **Combined Total Goals — Over 2.5**                                                |
| **4** | **Total Corners — Over 7.5** *(research threshold; confirm operator availability)* |

**Potential game winner:** **Sikkim Aakraman FC**

**Supplied Under branches:**

* Full Match Under 2.5 — `AVOID`
* 1st Half Under 0.5 — `AVOID`

**GAME-STATE:**
`PREGAME / SCHEDULE CONFLICT — NO VERIFIED LIVE STATE`

**Probability state:**
`NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value state:**
`NO VALUE DETERMINABLE`

**Forecast status:**
`RANKED FORECAST — CORNER ROW REQUIRES OPERATOR/PROVIDER CONFIRMATION`

---

# Source record

| Source                                      | Role                                                                              |
| ------------------------------------------- | --------------------------------------------------------------------------------- |
| Sikkim Football Association / SFA reporting | Competition/governing context                                                     |
| The Away End                                | Current league fixtures, results and goal times                                   |
| Sikkim Express                              | SFA-reported match results and competition context                                |
| Sofascore                                   | Fixture/state/result cross-check                                                  |
| AiScore                                     | Conflicting schedule and current-form cross-check                                 |
| ScoutMe                                     | Conflicting 28-August fixture schedule                                            |
| TotalCorner                                 | Direct corner totals, current match/corner research and provider-specific history |
| ScanGoal                                    | Specialist shot/chance/corner process cross-check                                 |
| IMD Met Centre Gangtok                      | Weather-warning state                                                             |
| Current market aggregator                   | Contract/market context only; NOT sporting evidence                               |

---

# Logging confirmation

**Canonical ID:** `P-126`

**Issued view:** `V01`

**Storage mode:** `COPY-PASTE MARKDOWN — NO GOOGLE DRIVE WRITE`

**Google Drive modified:** `NO`

**Historical combined log:** remains read-only predecessor evidence.

**Result status:** `OPEN — PENDING`

**Retrospective:** `NOT INCLUDED — per current user instruction`


## P-127 — Iran vs New Zealand — FIBA Basketball World Cup 2027 Asian Qualifiers

### Record metadata

| Field                       | Recorded value                                                   |
| --------------------------- | ---------------------------------------------------------------- |
| Canonical ID                | `P-127`                                                          |
| Sport                       | Basketball                                                       |
| Competition                 | FIBA Basketball World Cup 2027 Asian Qualifiers                  |
| Stage                       | Second Round — Group E                                           |
| Event                       | Iran vs New Zealand                                              |
| Venue                       | Mall of Asia Arena, Pasay City / Manila, Philippines             |
| Venue status                | Neutral window venue                                             |
| Scheduled start — local     | 2026-08-28 14:00 Asia/Manila                                     |
| Scheduled start — Melbourne | 2026-08-28 16:00 Australia/Melbourne                             |
| Final volatile refresh      | 2026-08-28 15:52 Australia/Melbourne                             |
| GAME-STATE                  | `PREGAME`                                                        |
| Official roster state       | FIBA states August 28 competing-team rosters have been confirmed |
| Starting five               | `NOT YET VERIFIED / NOT USED AS CONFIRMED`                       |
| Method                      | `MDS-2026.08.28-v2.4`                                            |
| Numerical training state    | `NTS-2026.08.25-v0.2 — STAGE 0 / PRE-FIT`                        |
| Probability state           | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`             |
| Value state                 | `NO VALUE DETERMINABLE`                                          |
| Storage mode                | `COPY-PASTE MARKDOWN ONLY — NO GOOGLE DRIVE WRITE`               |
| Result status               | `OPEN — PENDING`                                                 |

---

## Framework controls applied

Relevant promoted controls include:

* `L-001` — freeze event, state and exact contracts before analysis.
* `L-002` — separate authority, freshness and predictive importance.
* `L-003` — one coherent game-score corridor controls spreads and total.
* `L-004` — classify historical results against exact thresholds.
* `L-010` — winner and margin are different objects.
* `L-011` — scoring trends require underlying mechanisms.
* `L-015` — historical cases challenge the mechanism; results do not vote.
* `L-016` — freeze the complete candidate slate before ranking.
* `L-017` — no invented numerical probability.
* `L-018` — rank by marginal likelihood, not portfolio hedging.
* `L-021` — no value claim without the full price/calibration gate.
* `L-024` — official/current field owners and final volatile refresh.
* `L-029` — reconcile current roster/regime with broad historical baselines.

Basketball-specific controls:

* possessions and per-possession efficiency precede raw PPG;
* minutes/lineup uncertainty widens the distribution;
* blowout and garbage-time states are two-sided;
* late fouling and overtime are explicit tails;
* winner and -7.5 separation are not interchangeable;
* spread and total are derived from the same joint-score tree.

---

## Decision set

**Decision-set ID:** `DS-P-127-V01`

**Candidate origin:** `USER_SUPPLIED`

| Candidate ID | Exact contract                    | Eligibility |
| ------------ | --------------------------------- | ----------- |
| `P-127-C01`  | New Zealand -7.5                  | `ELIGIBLE`  |
| `P-127-C02`  | Iran +7.5                         | `ELIGIBLE`  |
| `P-127-C03`  | Combined Total Over 158.5 Points  | `ELIGIBLE`  |
| `P-127-C04`  | Combined Total Under 158.5 Points | `ELIGIBLE`  |

No bookmaker price is used to estimate probability or value.

---

## Contract-definition assumptions

The operator was not supplied.

Research assumptions:

* full-game FIBA score;
* overtime included if the operator's ordinary full-game basketball market includes it;
* half-point spread and total cannot push;
* abandonment/void terms remain operator-specific.

Exact operator settlement:

`UNKNOWN_DEFINITION`

Value state:

`NO VALUE DETERMINABLE`

---

# Target definition

**TARGET_ID:** `FIBA-WCQ-JOINT-SCORE-P127-V01`

| Field                  | Definition                                                                                       |
| ---------------------- | ------------------------------------------------------------------------------------------------ |
| Outcome                | Joint Iran / New Zealand final score                                                             |
| Start state            | Pregame                                                                                          |
| Endpoint               | Full game under supplied operator terms                                                          |
| Regulation             | 4 × 10-minute FIBA quarters                                                                      |
| OT                     | Explicit tail; settlement depends on operator full-game rules                                    |
| Exposure               | Minutes, possessions, lineup stints and shot/rebound/turnover opportunities                      |
| Rate layer             | Opponent-adjusted 2PT/3PT/FT efficiency, offensive rebounding, turnover and transition processes |
| Derived contracts      | Winner, ±7.5 margin, O/U 158.5                                                                   |
| Numerical distribution | `NOT GENERATED`                                                                                  |

---

# Event and participant verification

FIBA officially lists:

**Iran vs New Zealand**
Second Round, Group E
Mall of Asia Arena, Manila/Pasay, Philippines
28 August 2026
14:00 local time.

FIBA announced on game day that the rosters for all six Group E teams playing
on August 28 had been confirmed.

### Iran current regime

Important current participant state:

* Mohammad Amini has returned to national-team duty for Window 4.
* FIBA states Amini is expected to play against New Zealand and the Philippines.
* Amini averaged 14.6 points and 5.8 rebounds at Asia Cup 2025.
* Arsalan Kazemi remains a key rebound/defensive connector.
* Behnam Yakhchali is part of the current senior structure.
* Sina Vahedi remains unavailable while recovering from an ACL injury.

Amini's return improves wing scoring, size and secondary creation.

Vahedi's absence removes a major guard-scoring/creation branch.

Both effects are retained rather than treating the roster change as uniformly
positive or negative.

### New Zealand current regime

Decision-driving current pieces include:

* Sam Mennenga;
* Flynn Cameron;
* Shea Ili;
* Sam Waardenburg;
* veteran perimeter options in the current Window 4 group.

FIBA specifically identifies Mennenga as a key current matchup player.

Mennenga has scored double figures in each of his five qualifier appearances.
New Zealand are 3-0 in qualifier games where he started and 0-2 where he came
off the bench.

The exact confirmed starting five was not exposed in the final research pass,
so no player is silently assumed to start.

---

# Structural baseline

## Iran — First Round

Record: **5-1**

Scores:

| Game      | Iran score | Opponent score | Total |
| --------- | ---------: | -------------: | ----: |
| vs Iraq   |         94 |             68 |   162 |
| at Iraq   |         86 |             71 |   157 |
| vs Jordan |         60 |             73 |   133 |
| vs Syria  |         72 |             68 |   140 |
| at Jordan |         67 |             49 |   116 |
| at Syria  |         73 |             52 |   125 |

Descriptive averages:

* Iran points: **75.3**
* Iran opponent points: **63.5**
* combined environment: approximately **138.8**

Against the supplied 158.5:

* Over: 1
* Under: 5

This is descriptive evidence, not a fitted probability.

Iran's first-round margin sequence:

* +26
* +15
* -13
* +4
* +18
* +21

Against a hypothetical +7.5 threshold:

* cover in 5 of 6 descriptive results.

Again, these are not raw forecast probabilities because opponents and rosters
differ.

---

## New Zealand — First Round

Record: **4-2**

Relevant results:

| Opponent    |         Result | Total |
| ----------- | -------------: | ----: |
| Australia   |        L 79-84 |   163 |
| Australia   |        L 77-79 |   156 |
| Philippines |        W 69-66 |   135 |
| Guam        |        W 99-67 |   166 |
| Philippines | W 106-102, 2OT |   208 |
| Guam        |       W 129-75 |   204 |

FIBA's official qualifier average:

**93.2 PPG**

This headline number requires context.

It contains:

* two games against Guam, including 129 points;
* a 106-point performance that required two overtime periods.

The Philippines 106-102 game was tied 83-83 after regulation.

Against Australia and the Philippines, using regulation score:

* 163
* 156
* 135
* 166

Average:

**155.0 combined regulation points**

That population is more relevant to today's opponent-strength regime than
mechanically applying the 93.2 PPG headline.

New Zealand margins against Australia/Philippines:

* -5
* -2
* +3
* +4

None produced an 8+ point New Zealand win.

Their large separation states occurred against Guam.

---

# Current official team comparison

FIBA's current qualifier comparison lists:

| Metric        |  Iran | New Zealand |
| ------------- | ----: | ----------: |
| Points/game   |  75.3 |        93.2 |
| Rebounds/game |  39.7 |        52.0 |
| Assists/game  |  20.8 |        22.8 |
| 2PT FG        | 51.8% |       54.5% |
| 3PT FG        | 30.9% |       29.4% |
| FT            | 61.2% |       70.1% |

Interpretation:

### New Zealand advantages

* larger rebound volume;
* higher 2PT conversion;
* higher overall scoring ceiling;
* more credible transition/offensive-rebound acceleration;
* better free-throw percentage for close-game late states.

### Iran advantages / resistance mechanisms

* much lower opponent scoring throughout the qualifiers;
* stable half-court defensive structure;
* strong defensive-rebound / second-chance suppression;
* Amini's return adds a new scoring/size branch.

---

# Offensive rebounding / second-chance matchup

FIBA identifies this as a central matchup.

New Zealand lead the Asian Qualifiers at:

**20.8 second-chance points per game**

Iran have allowed only:

**6.5 second-chance points per game**

This is unusually important because New Zealand's large rebound advantage does
not mechanically imply a large scoring advantage if Iran prevents offensive
rebounds from becoming efficient second possessions.

Central clash:

`NZ rebound/physicality edge`
versus
`Iran box-out / second-chance suppression`

If New Zealand wins that battle decisively, both:

* NZ -7.5;
* Over 158.5

receive a significant lift.

If Iran's existing defensive mechanism persists:

* Iran +7.5;
* Under 158.5

are helped together.

---

# Current ranking / team-strength baseline

Latest FIBA ranking:

* New Zealand: **#25**
* Iran: **#26**

This is context, not a prediction coefficient.

It supports treating the matchup as between near-neighbour international sides,
rather than assuming an enormous class gap from the -7.5 threshold.

Current carried qualifying records:

* Iran: **5-1**
* New Zealand: **4-2**

---

# Head-to-head continuity

Most recent meeting:

**Iran 79-73 New Zealand**
FIBA Asia Cup 2025 third-place game.

Total:

**152**

Margin:

**Iran +6**

Contract mapping to today's supplied thresholds:

* Iran +7.5: historical WIN
* New Zealand -7.5: historical LOSS
* Under 158.5: historical WIN
* Over 158.5: historical LOSS

The result itself does not vote on today's forecast.

Continuity is incomplete:

* both current rosters have meaningful changes;
* Iran are without Vahedi but regain Amini;
* New Zealand's present rotation contains different veteran/creator combinations.

Therefore H2H supports the close-game/Under branch but does not control it.

---

# Coherent qualitative game tree

## Lower-total / Iran-control branch

Representative shapes:

* New Zealand 76-72
* Iran 75-73
* New Zealand 79-74

Mechanism:

* Iran limits second chances;
* half-court possessions dominate;
* both teams' modest three-point conversion persists;
* New Zealand's rebound edge produces extra possessions but not extreme conversion.

Favours:

* Iran +7.5
* Under 158.5

Winner remains genuinely competitive.

---

## Central branch

Representative shapes:

* New Zealand wins by approximately one to two possessions;
* total finishes around the upper-140s to mid-150s.

Mechanism:

* New Zealand owns a moderate rebounding and two-point efficiency advantage;
* Iran's defence prevents sustained separation;
* Amini provides enough extra offence/size to prevent Iran's scoring floor
  becoming too low;
* New Zealand's late free-throw advantage helps close the game.

Favours:

* New Zealand potential winner
* Iran +7.5
* Under 158.5

This branch is the primary reason the potential winner and rank-1 spread are
not the same side.

---

## High-possession / scoring branch

Representative shapes:

* 82-79
* 85-78
* 86-80

Mechanism:

* New Zealand forces transition;
* offensive rebounds generate repeated shots;
* Iran's improved Amini rotation raises its own scoring;
* late fouling adds possessions/free throws.

Favours:

* Over 158.5
* Iran +7.5 in close variants
* NZ -7.5 only if New Zealand also creates separation.

---

## New Zealand separation branch

Representative shapes:

* New Zealand by 9-15.

Mechanism:

* New Zealand dominates offensive glass;
* Iran's Vahedi-less perimeter creation stalls;
* Iran's low FT rate/percentage hurts comeback efficiency;
* transition points and late fouling extend the margin.

Favours:

* New Zealand -7.5

This is a credible tail but not the central match state.

---

## Iran upset branch

Mechanism:

* Iran reproduces its defensive control;
* Kazemi neutralises enough of New Zealand's offensive rebounding;
* Amini provides the extra shot creation absent from earlier qualification
  windows;
* New Zealand's three-point shooting remains volatile.

Favours:

* Iran +7.5
* Iran outright
* usually Under 158.5

---

# Strongest kill paths

## Iran +7.5

New Zealand turns its rebounding advantage into actual second-chance scoring,
forces transition, and Iran's half-court creation deteriorates without Vahedi.

## Under 158.5

Amini materially lifts Iran's scoring while New Zealand's offensive rebounding
and transition game persists, followed by late fouling or overtime.

## Over 158.5

Iran successfully suppresses second chances and controls pace; New Zealand's
headline scoring average regresses after removing Guam/OT distortion.

## New Zealand -7.5

Iran remains within one or two possessions through its defence and rebounding
discipline, creating the exact kind of close finish seen in the 2025 matchup
and many New Zealand games against stronger opposition.

---

# Contract geometry

### Spread pair

`P-127-C01` New Zealand -7.5
`P-127-C02` Iran +7.5

Exact complementary branches under matching terms.

No push.

### Total pair

`P-127-C03` Over 158.5
`P-127-C04` Under 158.5

Exact complementary branches under matching terms.

No push.

### Cross-contract dependence

Examples:

* NZ 79-75 -> Iran +7.5 + Under
* NZ 82-78 -> Iran +7.5 + Over
* NZ 84-74 -> NZ -7.5 + Under
* NZ 87-76 -> NZ -7.5 + Over

The ranking therefore comes from one score/margin tree rather than independent
spread and total narratives.

---

# Final ranking

|  Rank | Candidate   | Contract               | Verdict       | Evidence      | Dependence             | Performance role       | Actionability           | Probability     |
| ----: | ----------- | ---------------------- | ------------- | ------------- | ---------------------- | ---------------------- | ----------------------- | --------------- |
| **1** | `P-127-C02` | **Iran +7.5**          | `SUPPORTED`   | `MEDIUM-HIGH` | `MARGIN / JOINT-SCORE` | `PRIMARY_FORMAL`       | `NO VALUE DETERMINABLE` | `NOT_GENERATED` |
| **2** | `P-127-C04` | **Under 158.5 Points** | `LEAN`        | `MEDIUM-HIGH` | `TOTAL / JOINT-SCORE`  | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED` |
| **3** | `P-127-C03` | **Over 158.5 Points**  | `FORCED RANK` | `MEDIUM`      | `TOTAL / JOINT-SCORE`  | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED` |
| **4** | `P-127-C01` | **New Zealand -7.5**   | `AVOID`       | `MEDIUM-HIGH` | `MARGIN / JOINT-SCORE` | `CORRELATED_SECONDARY` | `NO VALUE DETERMINABLE` | `NOT_GENERATED` |

---

# Ranking rationale

## #1 — Iran +7.5

Most robust contract in the slate.

Iran do not need to win.

They can:

* win outright;
* lose by 1-7;

and still settle this contract as a win.

The current teams are adjacent in FIBA ranking, Iran carry a 5-1 qualifying
record, New Zealand's comparable Australia/Philippines matches have all remained
inside an eight-point New Zealand winning margin, and Iran possess a direct
mechanism against New Zealand's offensive-rebound strength.

Amini's return further improves Iran's ability to remain attached.

**Verdict:** `SUPPORTED`
**Evidence:** `MEDIUM-HIGH`

---

## #2 — Under 158.5

Iran's qualifying scoring environment is strongly Under-oriented relative to
158.5.

Five of six Iran qualifier games finished below this threshold.

New Zealand's 93.2 scoring average materially overstates their comparable
regulation environment because of Guam and overtime.

The direct rebounding matchup also gives Iran a credible route to suppress
New Zealand's second-chance scoring.

It stays below Iran +7.5 because New Zealand still have enough pace/rebounding
and Iran enough returning offence to create a legitimate 160+ branch.

**Verdict:** `LEAN`
**Evidence:** `MEDIUM-HIGH`

---

## #3 — Over 158.5

The Over has a legitimate but secondary pathway:

* New Zealand's rebounding;
* transition;
* Amini increasing Iran's offence;
* late fouling;
* overtime.

However, it conflicts with Iran's strongest demonstrated current team identity:
defensive control.

Therefore it is uniquely ranked third but does not receive a directional LEAN.

**Verdict:** `FORCED RANK`
**Evidence:** `MEDIUM`

---

## #4 — New Zealand -7.5

New Zealand are the preferred outright winner but the supplied margin requires
an additional separation event.

A close New Zealand win is a failure for this contract.

The combination of:

* near-equal FIBA ranking;
* Iran's 5-1 record;
* Iran's defence;
* Amini return;
* New Zealand's narrow margins against Australia/Philippines;
* Iran's prior six-point win over New Zealand;

makes eight-plus points too demanding relative to the other three supplied
contracts.

**Verdict:** `AVOID`
**Evidence:** `MEDIUM-HIGH`

`AVOID` is evidence-relative only; it is not a negative expected-value claim.

---

# Potential game winner

**Potential winner:** **New Zealand**

**Status:** `LEAN`

**Evidence quality:** `MEDIUM`

Central mechanism:

* stronger rebound volume;
* higher 2PT efficiency;
* deeper high-end scoring ceiling;
* superior free-throw conversion in a close late game;
* multiple perimeter creators available in the current window.

Strongest failure path:

Iran's defensive rebounding/second-chance suppression removes New Zealand's
largest possession advantage, while Amini supplies enough extra scoring for
Iran to control the final possessions.

### Critical distinction

**Potential winner:** New Zealand

**Best spread:** Iran +7.5

These are fully coherent.

The central forecast contains a substantial:

`NEW ZEALAND WINS BY 1-7`

branch.

---

# Final forecast card

|  Rank | Pick                                    |
| ----: | --------------------------------------- |
| **1** | **Iran +7.5**                           |
| **2** | **Combined Total — Under 158.5 Points** |
| **3** | **Combined Total — Over 158.5 Points**  |
| **4** | **New Zealand -7.5**                    |

**Potential game winner:** **New Zealand**

**GAME-STATE:** `PREGAME`

**Final refresh:** approximately 8 minutes before scheduled tip.

**Probability state:**
`NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value state:**
`NO VALUE DETERMINABLE`

**Forecast status:**
`ISSUED — PRE-RESULT`

---

# Source record

| Source                                   | Class                        | Decision-driving field                                    |
| ---------------------------------------- | ---------------------------- | --------------------------------------------------------- |
| FIBA Iran–New Zealand game page          | Official                     | Event identity, venue, H2H, team comparison               |
| FIBA August 28 roster confirmation       | Official                     | Current roster-release state                              |
| FIBA Group E August 28 preview           | Official                     | records, scoring, second-chance matchup, Mennenga context |
| FIBA Mohammad Amini return report        | Official                     | Amini availability/regime change, Vahedi absence          |
| FIBA Iran team profile                   | Official                     | qualifier player/team statistics                          |
| FIBA New Zealand team profile            | Official                     | qualifier player/team statistics                          |
| FIBA first-round game pages              | Official                     | exact results, quarter scores, margins, overtime state    |
| FIBA Asia Cup 2025 Iran–New Zealand page | Official                     | 79-73 H2H result                                          |
| FIBA World Ranking                       | Official                     | current #25 NZ / #26 Iran structural context              |
| Sports Research `RULES_BASKETBALL.md`    | Governing internal framework | possession/minutes/score-tree/ranking controls            |

---

# Important limitations

1. Exact operator was not supplied.
2. Full-game OT settlement is assumed for research only; operator terms control.
3. No prices were supplied, so likelihood and value cannot be conflated.
4. FIBA confirmed game-day rosters, but the exact starting five was not
   independently exposed in the final research pass.
5. Iran's historical qualifier totals were earned against a different opponent
   group and cannot be converted into raw probabilities.
6. New Zealand's 93.2 PPG average is structurally distorted upward by Guam and
   overtime; it is retained as official data but not used unadjusted.
7. The 2025 H2H has meaningful but incomplete roster continuity.
8. No numerical basketball model is fitted, calibrated or validated.
9. No probability percentages are generated.
10. The four rows contain two exact complementary pairs and represent one
    dependent game unit rather than four independent predictions.

---

# Logging confirmation

**Canonical ID:** `P-127`

**Issued view:** `V01`

**Forecast prepared and delivered before scheduled tip:** `YES`

**Google Drive modified:** `NO`

**Storage mode:** `COPY-PASTE MARKDOWN PROVIDED TO USER`

**Result status:** `OPEN — PENDING`

**Retrospective:** `NOT INCLUDED — per current user instruction`
## P-128 — Auckland vs Bay of Plenty — Hilux NPC Round 5

### Record metadata

| Field                        | Recorded value                                             |
| ---------------------------- | ---------------------------------------------------------- |
| Canonical ID                 | `P-128`                                                    |
| Sport                        | Rugby union                                                |
| Competition                  | Hilux National Provincial Championship (NPC), New Zealand  |
| Round                        | Round 5                                                    |
| Event                        | Auckland vs Bay of Plenty                                  |
| Venue                        | Eden Park, Auckland                                        |
| Home / away                  | Auckland home; Bay of Plenty away                          |
| Scheduled start              | 2026-08-28 19:10 NZST                                      |
| Australia/Melbourne start    | 2026-08-28 17:10 AEST                                      |
| Final refresh                | Approximately 10 minutes before official scheduled kickoff |
| GAME-STATE                   | `PREGAME`                                                  |
| Method                       | `MDS-2026.08.28-v2.4 — GENERAL MODULE`                     |
| Dedicated rugby-union module | `NONE`                                                     |
| Probability state            | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`       |
| Value state                  | `NO VALUE DETERMINABLE`                                    |
| Result                       | `OPEN — PENDING`                                           |
| Google Drive write           | `NO`                                                       |

### Sport-module boundary

The active Sports Research rugby file covers **rugby league only**.

It explicitly states that rugby union is a different code and uses the general
module until a dedicated rugby-union specification exists.

Therefore no NRL-specific set/tackle/six-again/golden-point model is transferred
to this NPC game.

---

## Decision set

**Decision-set ID:** `DS-P-128-V01`

**Candidate origin:** `USER_SUPPLIED`

| Candidate ID | Contract                         |
| ------------ | -------------------------------- |
| `P-128-C01`  | Auckland +4.5                    |
| `P-128-C02`  | Bay of Plenty -4.5               |
| `P-128-C03`  | Combined Total Over 60.0 Points  |
| `P-128-C04`  | Combined Total Under 60.5 Points |

All four valid supplied rows are retained and uniquely ranked.

No price is supplied or used to claim value.

---

## Target definition

**TARGET_ID:** `NPC-JOINT-FINAL-SCORE-P128-V01`

Underlying target:

`joint Auckland / Bay of Plenty regulation final score`

Unit:

`official rugby-union points`

Exposure/process considered qualitatively:

* possession;
* territory;
* entries into opposition 22;
* try creation;
* goal kicking;
* set-piece and breakdown pressure;
* penalties/cards;
* transition/broken-field play;
* bench effects;
* late score-state behaviour.

No fitted numerical rugby-union distribution exists.

---

## Contract geometry

### Spread

**Auckland +4.5**

WIN:

* Auckland wins;
* draw;
* Auckland loses by 1–4.

LOSS:

* Auckland loses by 5+.

**Bay of Plenty -4.5**

WIN:

* Bay wins by 5+.

LOSS:

* any Auckland win/draw;
* Bay wins by 1–4.

These are exact opposite half-point branches.

### Totals

**Over 60.0**

* WIN at 61+
* PUSH at exactly 60
* LOSS at 59 or below

**Under 60.5**

* WIN at 60 or below
* LOSS at 61+

The totals are not exact half-point complements because the Over carries an
integer push boundary.

At total = 60:

* Over 60.0 = PUSH
* Under 60.5 = WIN

---

# Current competition baseline

## Auckland

2026 NPC through four games:

| Opponent      |  Result | Total |
| ------------- | ------: | ----: |
| Canterbury    | L 31-38 |    69 |
| Wellington    | W 34-31 |    65 |
| Hawke's Bay   | L 31-44 |    75 |
| North Harbour | L 19-27 |    46 |

Record:

`1-3`

Points:

* For: `115`
* Against: `140`
* Differential: `-25`

Tries:

* For: `18`
* Against: `21`

Current-game totals Over 60:

`3 of 4`

---

## Bay of Plenty

2026 NPC through four games:

| Opponent   |  Result | Total |
| ---------- | ------: | ----: |
| Waikato    | L 26-38 |    64 |
| Northland  | W 34-31 |    65 |
| Canterbury | L 28-33 |    61 |
| Taranaki   | W 28-24 |    52 |

Record:

`2-2`

Points:

* For: `116`
* Against: `126`
* Differential: `-10`

Tries:

* For: `17`
* Against: `19`

Current-game totals Over 60:

`3 of 4`

Bay winning margins:

* Northland: +3
* Taranaki: +4

Bay have not yet produced a 5+ point win in the 2026 NPC.

---

# Competition scoring environment

The current NPC standings through four rounds contain approximately:

`1,725 points / 28 matches = 61.6 combined points per match`

This is descriptive league context rather than a fitted forecast.

The supplied 60/60.5 total therefore lies close to, and marginally below, the
current broad competition scoring level.

---

# Recent target-process evidence

## Auckland vs North Harbour

Final:

`North Harbour 27-19 Auckland`

Opposition-22 entries:

* North Harbour: 11
* Auckland: 10

Average points per 22 entry:

* North Harbour: 2.4
* Auckland: 1.9

Interpretation:

Auckland's eight-point loss did not come from an absence of attacking-zone
exposure.

They reached the opposition 22 almost as frequently as North Harbour but
converted that exposure less efficiently.

This preserves an Auckland close-game/upset branch if conversion improves.

---

## Bay of Plenty vs Taranaki

Final:

`Bay of Plenty 28-24 Taranaki`

Half-time:

`Bay of Plenty 21-7`

Opposition-22 entries:

* Bay: 9
* Taranaki: 10

Average points per entry:

* Bay: 3.1
* Taranaki: 2.4

Bay created a strong first-half separation but allowed Taranaki back into the
match, particularly around a card/manpower-state branch.

This demonstrates both:

* Bay's ability to create early separation;
* Bay's vulnerability to finishing games inside a narrow margin.

That is directly relevant to Auckland +4.5 versus Bay -4.5.

---

# Participant state

The official NPC Round 5 page states that team lists have been published.

The player-by-player official list was not recoverable directly in the final
research extraction.

Two independent current specialist lineup sources agree on the following XVs.

### Auckland — current reported XV

1. Joshua Fusitu'a
2. Nathaniel Pole
3. Angus Ta'avao
4. Tai Cribb
5. Josh Beehre
6. Che Clark
7. Logan Platt
8. Titi Nofoagatotoa
9. Issak Fines-Leleiwasa
10. Alex Harford
11. Harlyn Saunoa
12. Xavi Taele
13. Tevita Latu
14. Payton Spencer
15. Rico Simpson

### Bay of Plenty — current reported XV

1. Benet Kumeroa
2. Taine Kolose
3. Tevita Mafileo
4. Naitoa Ah Kuoi
5. Jai Knight
6. Joe Johnston
7. Veveni Lasaqa
8. Nikora Broughton
9. Charlie Sinton
10. Lucas Cashmore
11. Rory van Vugt
12. Reon Paul
13. Tamiro Armstrong
14. Regan Ware
15. Cole Forbes

Participant status:

`PROVISIONAL CURRENT XV — OFFICIAL TEAM-LIST PUBLICATION EXISTS; EXACT NAMES
RECOVERED THROUGH TWO CURRENT SPECIALIST SOURCES`

No player prop is issued.

### Material lineup observations

Auckland's current reported side differs meaningfully from the North Harbour
game:

* Angus Ta'avao moves into the starting front row;
* Josh Beehre starts at lock;
* the loose-forward configuration changes;
* Alex Harford replaces Stephen Perofeta at first five;
* midfield personnel change.

Bay retain considerable continuity through:

* Ah Kuoi;
* Lasaqa;
* Broughton;
* Sinton;
* Cashmore;
* Paul;
* Armstrong.

Bay's back three changes from the Taranaki game, including Cole Forbes moving
to fullback in the current reported XV.

These changes widen uncertainty and are not assigned fitted numerical weights.

---

# H2H continuity audit

Last five:

| Season |                       Result | Margin | Total |
| ------ | ---------------------------: | -----: | ----: |
| 2024   | Bay of Plenty 26-24 Auckland |      2 |    50 |
| 2023   | Auckland 32-30 Bay of Plenty |      2 |    62 |
| 2022   | Bay of Plenty 21-17 Auckland |      4 |    38 |
| 2020   | Auckland 20-16 Bay of Plenty |      4 |    36 |
| 2019   | Auckland 19-13 Bay of Plenty |      6 |    32 |

All five were decided by six points or fewer.

Four of five finished Under 60.5.

However, the sample spans several seasons with major personnel and tactical
turnover.

Therefore:

* narrow-margin history remains relevant;
* old H2H total suppression is downweighted against the current 2026 scoring
  regime.

---

# Weather / environment

Current Auckland match-window conditions:

* cloudy;
* cool, around 15°C near kickoff;
* moderate but not severe precipitation probability;
* no current heavy-rain warning applying to the Friday-night match window.

The Auckland heavy-rain watch begins the following morning.

Therefore weather does **not** receive a strong directional Under adjustment.

Rain remains a conditional tail rather than an assumed scoring suppressant.

---

# Scenario corridor

## Central close/high-scoring branch

Representative shapes:

* Bay 32-30
* Bay 33-30
* Auckland 32-30

Mechanisms:

* both teams generate repeated 22 entries;
* current-season defensive concession rates persist;
* neither side establishes prolonged territorial domination;
* broken-field/penalty opportunities keep scoring active.

Favours:

* Over 60
* Auckland +4.5 in many Bay-win states

---

## Lower-scoring branch

Representative shapes:

* Bay 27-24
* Auckland 27-25
* Bay 28-25

Mechanisms:

* old-H2H type territorial contest;
* lower conversion of 22 entries;
* conservative tactical kicking;
* fewer transition opportunities.

Favours:

* Under 60.5
* Auckland +4.5

---

## Bay separation branch

Representative shapes:

* Bay 34-27
* Bay 38-29

Mechanisms:

* Bay forward/loose-forward advantage creates repeated gain-line wins;
* Cashmore controls territory;
* Auckland's defensive concession regime persists;
* late chasing state expands the margin.

Favours:

* Bay -4.5
* Over 60

---

## Auckland upset branch

Representative shapes:

* Auckland 31-29
* Auckland 34-30

Mechanisms:

* home territory;
* improved front-row/set-piece output;
* Fines-Leleiwasa generates fast attacking ball;
* Auckland converts the 22-entry exposure that was wasted against Harbour.

Favours:

* Auckland +4.5
* typically Over 60

---

# Final ranking

|  Rank | Candidate   | Contract               | Verdict       | Evidence     | Dependence             | Probability     |
| ----: | ----------- | ---------------------- | ------------- | ------------ | ---------------------- | --------------- |
| **1** | `P-128-C03` | **Over 60.0 Points**   | `LEAN`        | `MEDIUM`     | `JOINT SCORE / TOTAL`  | `NOT_GENERATED` |
| **2** | `P-128-C01` | **Auckland +4.5**      | `LEAN`        | `MEDIUM`     | `JOINT SCORE / MARGIN` | `NOT_GENERATED` |
| **3** | `P-128-C04` | **Under 60.5 Points**  | `FORCED RANK` | `MEDIUM-LOW` | `JOINT SCORE / TOTAL`  | `NOT_GENERATED` |
| **4** | `P-128-C02` | **Bay of Plenty -4.5** | `AVOID`       | `MEDIUM`     | `JOINT SCORE / MARGIN` | `NOT_GENERATED` |

---

# Detailed ranking rationale

## #1 — Over 60.0

Current-season evidence:

* Auckland: 3/4 games above 60.
* Bay: 3/4 games above 60.
* current NPC broad scoring environment approximately 61.6.
* Auckland and Bay both have high try-for and try-against counts.
* weather provides no strong suppression mechanism.

The integer line also provides a push at exactly 60.

Strongest kill path:

the matchup reverts to its historically tight territorial regime and inefficient
22-entry conversion produces a score around 27-24.

---

## #2 — Auckland +4.5

Bay are the preferred winner but have won their two current matches by only:

* 3;
* 4.

All five recent H2Hs were decided by six or fewer.

Auckland also generated near-equal 22-entry exposure in the North Harbour loss.

Therefore a narrow Bay win is a material central state.

Strongest kill path:

Bay's forward pack wins territory decisively and Auckland's current defensive
concession rate persists, creating a 5+ margin.

---

## #3 — Under 60.5

Support:

* four of five H2Hs Under 60.5;
* Auckland's latest match total = 46;
* Bay's latest match total = 52;
* the Under wins at exactly 60 while Over 60 pushes.

Opposition:

* six of eight combined 2026 team games above 60;
* current NPC scoring level approximately 61.6;
* no strong weather-Under mechanism.

Therefore the row remains below the Over.

---

## #4 — Bay of Plenty -4.5

Bay are the preferred game winner.

But requiring five or more points is a distinct separation event.

Bay's 2026 wins:

* +3
* +4

and the H2H series remains strongly close-margin oriented.

The handicap therefore ranks last despite the Bay winner lean.

`AVOID` is evidence-relative only and is not an expected-value statement.

---

# Potential winner

**Bay of Plenty — LEAN**

Central basis:

* superior 2026 record;
* better points differential;
* stronger recent result;
* considerable current core continuity;
* credible forward/territory advantage through Ah Kuoi, Lasaqa and Broughton.

Strongest failure path:

Auckland's home-side set-piece and attacking-entry process improves, while Bay
again fails to convert an early advantage into lasting separation.

Important coherence statement:

**Bay of Plenty can be the potential winner while Auckland +4.5 remains the
preferred spread.**

Representative central result:

`Bay wins by 1–4`

---

# Final forecast card

1. **Combined Total Over 60.0 Points**
2. **Auckland +4.5**
3. **Combined Total Under 60.5 Points**
4. **Bay of Plenty -4.5**

**Potential winner:** **Bay of Plenty**

**GAME-STATE:** `PREGAME`

**Probability state:**
`NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value state:**
`NO VALUE DETERMINABLE`

**Result status:**
`OPEN — PENDING`

---

# Source record

* New Zealand Rugby / Provincial Rugby — official NPC Round 5 fixture/team-list
  publication and referee.
* All Blacks / NZ Rugby — official 19:10 NZST stream/fixture time.
* Eden Park — official venue and kickoff.
* Auckland Rugby — competition and fixture confirmation.
* RugbyPass — current standings, points/tries, results and recent match process.
* Ultimate Rugby — current detailed lineup cross-check.
* Read Rugby Union — independent current detailed lineup cross-check and H2H.
* MetService — current Auckland regional conditions.
* Sports Research `RULES_GENERAL.md` — governing general framework.
* Sports Research `RULES_NRL_RUGBY.md` — explicit rugby-league/rugby-union
  separation rule.

---

# Logging confirmation

**Canonical ID:** `P-128`

**Issued view:** `V01`

**Google Drive modified:** `NO`

**Storage mode:** `COPY-PASTE MARKDOWN PROVIDED TO USER`

**Forecast issued pre-result:** `YES`

**Retrospective:** `NOT INCLUDED`

## P-129 — Manly Warringah Sea Eagles vs St George Illawarra Dragons — NRL Round 26

### Record metadata

| Field                  | Recorded value                                                                             |
| ---------------------- | ------------------------------------------------------------------------------------------ |
| Canonical ID           | `P-129`                                                                                    |
| Sport                  | Rugby league                                                                               |
| Competition            | NRL Telstra Premiership 2026                                                               |
| Round                  | 26                                                                                         |
| Event                  | Manly Warringah Sea Eagles vs St George Illawarra Dragons                                  |
| Venue                  | 4 Pines Park, Sydney                                                                       |
| Home                   | Manly Sea Eagles                                                                           |
| Away                   | St George Illawarra Dragons                                                                |
| Scheduled kickoff      | 2026-08-28 18:00 Australia/Sydney                                                          |
| Final research refresh | Approximately 17:49 Australia/Sydney                                                       |
| GAME-STATE             | `PREGAME`                                                                                  |
| Final team state       | `CONFIRMED_OFFICIAL — both clubs issued final teams; NRL live blog states no late changes` |
| Method                 | `MDS-2026.08.28-v2.4`                                                                      |
| Sport module           | `RULES_NRL_RUGBY.md`                                                                       |
| Numerical state        | `NTS-2026.08.25-v0.2 — STAGE 0 / PRE-FIT`                                                  |
| Probability state      | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`                                       |
| Value state            | `NO VALUE DETERMINABLE`                                                                    |
| Result                 | `OPEN — PENDING`                                                                           |
| Storage                | `COPY-PASTE ONLY — NO GOOGLE DRIVE WRITE`                                                  |

---

# Decision set

**Decision-set ID:** `DS-P-129-V01`

**Candidate origin:** `USER_SUPPLIED`

| Candidate ID | Exact contract                   |
| ------------ | -------------------------------- |
| `P-129-C01`  | Manly Sea Eagles +10.5           |
| `P-129-C02`  | St George Illawarra Dragons -4.5 |
| `P-129-C03`  | Combined Total Over 50.0 Points  |
| `P-129-C04`  | Combined Total Under 50.5 Points |

No candidate was replaced.

No bookmaker price was used as sporting evidence.

---

# Contract geometry

## Spread contracts

The supplied alternate spreads overlap.

### Manly +10.5

WIN:

* any Manly win;
* draw;
* Dragons win by 1–10.

LOSS:

* Dragons win by 11+.

### Dragons -4.5

WIN:

* Dragons win by 5+.

LOSS:

* any Manly win;
* draw;
* Dragons win by 1–4.

### Overlap interval

If the Dragons win by **5–10 points**, both:

* Manly +10.5;
* Dragons -4.5

settle as wins.

They are therefore not complementary contracts.

---

## Total contracts

### Over 50.0

* WIN at 51+
* PUSH at exactly 50
* LOSS at 49 or fewer

### Under 50.5

* WIN at 50 or fewer
* LOSS at 51+

At exactly 50:

* Over 50.0 = PUSH
* Under 50.5 = WIN

The Under therefore has superior boundary geometry at the central 50-point state.

---

# Underlying target

**TARGET_ID:** `NRL-JOINT-SCORE-P129-V01`

Outcome:

`Manly final points, Dragons final points`

Sport-native exposure/process chain:

* sets and set starts;
* field position;
* completion/error states;
* metres/set;
* ruck/play-the-ball state;
* line breaks/tackle breaks;
* repeat attacking sets;
* goal-line entries;
* try conversion;
* goal kicking;
* sin-bin/send-off tails;
* late chasing/garbage-time state.

No fitted or validated NRL model exists.

One qualitative joint score corridor therefore controls all four rows.

---

# Official participant state

## Manly Sea Eagles — final team

1. Tom Trbojevic — fullback
2. Jason Saab
3. Josh Feledy
4. Reuben Garrick
5. Lehi Hopoate
6. Clayton Faulalo
7. Jamal Fogarty
8. Simione Laiafi
9. Brandon Wakeham
10. Nathan Brown
11. Haumole Olakau'atu
12. Ben Trbojevic
13. Jake Trbojevic

Interchange:

* Jake Simpkin
* Nic Lenaz
* Corey Waddell
* Caleb Navale

### Material Manly changes/state

* Tom Trbojevic is confirmed at fullback after returning last round.
* Tolu Koula is out with a moderate syndesmosis injury.
* Josh Feledy starts at centre after scoring a hat-trick against Newcastle.
* Clayton Faulalo remains at five-eighth.
* Jamal Fogarty remains the organising half.
* Nathan Brown plays his 200th NRL game.
* Kobe Hetherington remains unavailable following a ruptured biceps injury.

---

## Dragons — final team

1. Daniel Atkinson — fullback
2. Mathew Feagai
3. Moses Suli
4. Valentine Holmes
5. Tyrell Sloan
6. Lyhkan King-Togia
7. Kyle Flanagan
8. Loko Jnr Pasifiki Tonga
9. Damien Cook
10. Toby Couchman
11. Dylan Egan
12. Hamish Stewart
13. Ryan Couchman

Interchange:

* Connor Muhleisen
* Josh Kerr
* Jacob Halangahu
* Jacob Webster

### Material Dragons changes/state

* Clint Gutherson remains unavailable with a knee injury.
* Daniel Atkinson starts at fullback.
* Jacob Liddle is out with a calf injury.
* Damien Cook starts at hooker.
* Connor Muhleisen returns to the NRL via the bench after an ACL reconstruction
  and four NSW Cup appearances during August.

Participant state for both sides:

`CONFIRMED_OFFICIAL`

---

# Season structural baseline

## Manly

Current NRL profile:

* Points scored: `549`
* Points conceded: `483`
* Average scored: approximately `24`
* Average conceded: approximately `21`
* Ladder: `10th`
* Competition points: `26`
* Differential: `+66`

Manly remain mathematically alive for the finals.

They must win their remaining games and receive help from other results.

---

## Dragons

Current NRL profile:

* Points scored: `358`
* Points conceded: `651`
* Average scored: approximately `16`
* Average conceded: approximately `29`
* Ladder: `17th`
* Differential: `-293`

This represents a materially weaker broad season scoring/defensive baseline than
Manly.

The differential cannot be used mechanically as a point spread, but it is a
strong structural strength prior.

---

# Manly current-regime branch

Manly entered Round 25 on a six-game losing sequence.

A decision-driving regime change then occurred:

**Tom Trbojevic returned.**

NRL reporting stated that Manly had lost all three games during his latest
absence.

Round 25:

**Manly 44 — Newcastle 24**

Tom Trbojevic:

* 154 run metres.

Outside-back contribution included:

* Lehi Hopoate 151 metres and nine tackle breaks;
* Reuben Garrick 156 metres;
* Josh Feledy three tries after entering for injured Koula.

Manly produced repeated attacking separation after initially trailing.

This is retained as a current-regime branch, not interpreted as proof that
44-point output must recur.

---

# Dragons current-regime branch

Recent Dragons results:

| Opponent     |  Result | Total |
| ------------ | ------: | ----: |
| Titans       | L 18-38 |    56 |
| Dolphins     | L 22-28 |    50 |
| Sharks       | W 24-16 |    40 |
| Wests Tigers | W 24-22 |    46 |
| Bulldogs     | L 14-44 |    58 |

The Dragons displayed a genuine improved branch in consecutive wins over
Cronulla and Wests Tigers.

Mechanisms supporting that improvement included:

* high defensive workload from Ryan Couchman/Hamish Stewart;
* young forward continuity;
* competitive effort;
* improved control through the middle.

However, the Bulldogs game exposed the downside branch again.

The Dragons were:

* 24-0 down at halftime;
* error-heavy;
* unable to execute consistently;
* beaten 44-14.

Current roster losses at fullback and hooker keep substantial uncertainty in
their attack/control floor.

---

# Recent Manly scoring environment

Relevant recent played games:

| Opponent |  Result | Total |
| -------- | ------: | ----: |
| Titans   | L 32-38 |    70 |
| Sharks   | L 12-48 |    60 |
| Storm    | L 20-42 |    62 |
| Dolphins |  L 0-22 |    22 |
| Knights  | W 44-24 |    68 |

This is a very volatile scoring environment.

The high totals were produced partly by defensive failure during Manly's losing
regime and, most recently, by a strong attacking rebound with Trbojevic restored.

Therefore the recent total history is not pooled blindly.

---

# H2H / current-season matchup

Round 6, 2026:

**Manly 28 — Dragons 18**

Total:
`46`

Margin:
`Manly +10`

Decision-driving process reported by NRL:

* Reuben Garrick ran approximately 240 metres and scored twice;
* Tom Trbojevic ran approximately 195 metres.

Applied descriptively to today's contracts:

* Manly +10.5 = WIN
* Dragons -4.5 = LOSS
* Under 50.5 = WIN
* Over 50.0 = LOSS

The prior result is not a forecast vote.

It is retained because Trbojevic, Garrick and several core players maintain
meaningful continuity.

---

# Weather

Bureau of Meteorology Manly/Sydney forecast:

* approximately 20°C maximum;
* 0 mm expected rainfall;
* around 5% rain probability;
* south/southeasterly winds easing during the evening.

Weather therefore provides no strong wet-weather scoring adjustment.

It also removes a major weather-error/short-field branch from the central
corridor.

---

# Joint qualitative score corridor

## Branch A — Manly control / lower total

Representative scores:

* Manly 28-16
* Manly 30-16
* Manly 30-18

Mechanism:

* Trbojevic/Fogarty improve attacking organisation;
* Manly win field position;
* Dragons struggle to turn possession into repeated goal-line entries;
* Manly can create separation without requiring a large Dragons contribution.

Favours:

* Manly +10.5
* Under 50.5
* Manly winner

---

## Branch B — close Manly win

Representative scores:

* Manly 26-22
* Manly 28-22

Mechanism:

* Dragons' young pack remains competitive;
* Manly create more attacking opportunities but do not fully separate;
* Dragons score enough to remain attached.

Favours:

* Manly +10.5
* Manly winner
* total sits around the supplied boundary.

---

## Branch C — open Manly win

Representative scores:

* Manly 32-22
* Manly 34-20
* Manly 34-24

Mechanism:

* Manly's restored outside-back attack creates line breaks;
* Dragons also exploit Manly's recent defensive instability;
* late chasing generates additional possessions.

Favours:

* Manly +10.5
* Over 50
* Manly winner

---

## Branch D — narrow Dragons upset

Representative scores:

* Dragons 22-20
* Dragons 26-22

Mechanism:

* Dragons middle defends strongly;
* Manly error/discipline regression;
* Holmes/Flanagan convert field position;
* Manly fail to convert possession.

Favours:

* Manly +10.5
* usually Under 50.5
* Dragons outright

Dragons -4.5 still loses in the 1–4 margin states.

---

## Branch E — Dragons separation tail

Representative scores:

* Dragons 28-20
* Dragons 30-18

Mechanism:

* Manly's prior defensive collapse returns;
* Dragons generate short fields from Manly errors;
* Trbojevic/Fogarty attack fails to control territory;
* possible card/injury tail amplifies separation.

Favours:

* Dragons -4.5
* Under or Over depending exact score.

Even some Dragons separation states from +5 through +10 still allow
**Manly +10.5 to win**.

---

# Strongest kill paths

## Manly +10.5

Dragons reproduce their Cronulla-level defensive effort while Manly revert to
their pre-Newcastle error/defensive regime, and St George Illawarra create an
11+ point upset.

## Under 50.5

Manly's Trbojevic-led attack continues the Newcastle regime while Manly's own
defence concedes enough for both sides to combine for 51+.

Late tries, penalties, sin-bin and chasing states are the main upper tail.

## Over 50.0

The Dragons' low season scoring output persists and Manly control the match
rather than trade tries, producing approximately 28-16 or 30-16.

## Dragons -4.5

Manly simply win the match or remain within four.

The Dragons must create genuine separation rather than merely stay competitive.

---

# Final ranking

|  Rank | Candidate   | Contract                   | Verdict       | Evidence      | Dependence             | Probability state |
| ----: | ----------- | -------------------------- | ------------- | ------------- | ---------------------- | ----------------- |
| **1** | `P-129-C01` | **Manly Sea Eagles +10.5** | `SUPPORTED`   | `MEDIUM-HIGH` | `JOINT SCORE / MARGIN` | `NOT_GENERATED`   |
| **2** | `P-129-C04` | **Under 50.5 Points**      | `LEAN`        | `MEDIUM`      | `JOINT SCORE / TOTAL`  | `NOT_GENERATED`   |
| **3** | `P-129-C03` | **Over 50.0 Points**       | `FORCED RANK` | `MEDIUM-LOW`  | `JOINT SCORE / TOTAL`  | `NOT_GENERATED`   |
| **4** | `P-129-C02` | **Dragons -4.5**           | `AVOID`       | `MEDIUM-HIGH` | `JOINT SCORE / MARGIN` | `NOT_GENERATED`   |

---

# Ranking rationale

## #1 — Manly +10.5

This is the most robust contract because:

* Manly have the materially stronger season profile;
* Manly have the better scoring differential;
* Trbojevic has returned;
* Manly won the current-season H2H by 10;
* the Dragons are without Gutherson and Liddle;
* the contract still wins if Manly lose by up to 10.

Failure requires a Dragons win by 11+.

**Verdict:** `SUPPORTED`
**Evidence:** `MEDIUM-HIGH`

---

## #2 — Under 50.5

Season environments for both clubs centre near approximately 45 total points.

The first H2H finished at 46.

Three of the Dragons' last five finished at 50 or lower.

The largest question is whether Manly's restored attack plus their unstable
defence generates another 50+ game.

The Under gets the important exact-50 boundary as a WIN.

**Verdict:** `LEAN`
**Evidence:** `MEDIUM`

---

## #3 — Over 50.0

The Over has a credible current-regime pathway through:

* Trbojevic;
* Manly outside-back speed;
* Dragons' season defensive leakage;
* Manly's recent defensive volatility;
* late chasing states.

But the Dragons' season attack remains only approximately 16 points per game,
and the first meeting finished below the threshold.

Exactly 50 also produces only a PUSH.

**Verdict:** `FORCED RANK`
**Evidence:** `MEDIUM-LOW`

---

## #4 — Dragons -4.5

This requires a last-placed Dragons side to win by 5+ away from home against a
Manly side still playing for a finals opportunity.

A narrow Dragons upset is not enough.

The row therefore has the narrowest ordinary success interval among the four
supplied contracts.

**Verdict:** `AVOID`
**Evidence:** `MEDIUM-HIGH`

`AVOID` is evidence-relative and does not constitute a negative-value claim.

---

# Potential game winner

**Manly Sea Eagles — LEAN**

Evidence:

`MEDIUM-HIGH`

Central mechanisms:

* substantially better season scoring differential;
* home venue;
* restored Tom Trbojevic;
* Fogarty/Trbojevic attacking organisation;
* stronger outside-back finishing ceiling;
* Dragons' league-worst defensive output;
* Dragons missing Gutherson and Liddle.

Strongest failure path:

Manly's recent defensive/error problems return while the Dragons' young pack
reproduces the defensive intensity seen in the Cronulla win.

---

# Final forecast card

1. **Manly Sea Eagles +10.5**
2. **Combined Total Under 50.5 Points**
3. **Combined Total Over 50.0 Points**
4. **St George Illawarra Dragons -4.5**

**Potential game winner:** **Manly Sea Eagles**

**GAME-STATE:** `PREGAME — FINAL TEAMS CONFIRMED`

**Probability state:**
`NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value state:**
`NO VALUE DETERMINABLE`

**Result status:**
`OPEN — PENDING`

---

# Source record

* NRL official Round 26 live blog — final game state / no late changes.
* NRL official Round 26 team lists — participant positions and match details.
* Manly Sea Eagles official final team — final 17 and Koula status.
* St George Illawarra Dragons official final team — final 17, Liddle/Muhleisen
  state.
* NRL club profiles — 2026 points scored/conceded and player statistics.
* NRL Round 20–25 match centres / live blogs — current-form results and
  mechanism evidence.
* NRL Round 6 preview/match material — current-season H2H.
* NRL Finals Tracker — Manly ladder/finals state.
* Bureau of Meteorology — Manly/Sydney match-window weather.
* Sports Research `RULES_NRL_RUGBY.md`.
* Sports Research `RULES_GENERAL.md`.
* Sports Research `LEARNING_REGISTER.md`.

---

# Logging confirmation

**Canonical ID:** `P-129`

**Issued view:** `V01`

**Forecast prepared before kickoff:** `YES`

**Official final teams verified:** `YES`

**Google Drive modified:** `NO`

**Storage mode:** `COPY-PASTE MARKDOWN PROVIDED TO USER`

**Result status:** `OPEN — PENDING`

**Retrospective:** `NOT INCLUDED`


# P-130 — Beitar Haifa Yakov vs Hapoel Bnei Arrara Ara — Israel State Cup 2026/27

## Record metadata

| Field | Recorded value |
|---|---|
| Canonical ID | `P-130` |
| Sport | Soccer |
| Competition | Israel State Cup 2026/27 — Round 1 |
| Event | Beitar Haifa Yakov vs Hapoel Bnei Arrara Ara |
| Date | 2026-08-28 |
| Initial pre-start evidence cutoff | 2026-08-28 17:59:22 Australia/Melbourne |
| Final state refresh | 2026-08-28 18:00:46 Australia/Melbourne |
| GAME-STATE | `START CROSSED ON EARLIER SCHEDULE BRANCH — LIVE STATE NOT VERIFIED` |
| Actionability | `NO ACTIONABLE LIVE FORECAST UNTIL SCORE/CLOCK ARE VERIFIED` |
| Kickoff source branch A | 08:00 UTC / 18:00 Melbourne — AiScore and multiple current fixture/market feeds |
| Kickoff source branch B | 09:00 UTC / 19:00 Melbourne — TotalCorner and some current listings |
| Official IFA kickoff confirmation | `NOT RECOVERED` |
| Venue | `NOT VERIFIED` |
| Starting XIs | `NOT RECOVERED FROM OFFICIAL SOURCE` |
| Goalkeepers | `NOT VERIFIED` |
| Method | `MDS-2026.08.28-v2.4` |
| Soccer module | `RULES_SOCCER.md` |
| Numerical model | `NOT FIT / NOT VALIDATED` |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Storage mode | `LOCAL DOWNLOADABLE FILE — NO GOOGLE DRIVE WRITE` |
| Retrospective | `NOT INCLUDED` |

> **State-integrity warning:** The 08:00 UTC kickoff branch passed during research. Current live-score pages still expose only blank/zero-filled shells and no trustworthy match clock, while another current source lists 09:00 UTC. Under the active Sports Research state rules this is not sufficient to assert a live 0-0. The rankings below are therefore preserved as a **pre-start evidence view** and are **not actionable as live picks** unless the user's operator confirms the match has not begun.

---

## Final ranked pre-start evidence view

| Rank | Pick | Verdict | Evidence | State cap |
|---:|---|---|---|---|
| **1** | **Beitar Haifa Yakov or Draw — Double Chance 1X** | `FORCED RANK` | `MEDIUM-LOW` | sparse participants + unverified live state |
| **2** | **1st Half Goals Over 0.5** | `LEAN — PRE-START EVIDENCE` | `MEDIUM` | no actionable live use |
| **3** | **Combined Total Goals Over 2.5** | `LEAN, THIN — PRE-START EVIDENCE` | `MEDIUM-LOW` | no actionable live use |
| **4** | **Total Corners Under 10.5 — research threshold** | `FORCED RANK` | `MEDIUM-LOW` | derivative/provider + state cap |

**Potential game winner:** **Beitar Haifa Yakov**  
**Winner status:** `FORCED WINNER — LOW CONFIDENCE / STATE-LIMITED`

---

# Framework controls applied

The active Sports Research soccer rules require:

- exact competition/event/contract identity;
- official participant/goalkeeper verification where available;
- one coherent goal corridor for winner and goal totals;
- separate modelling for corners rather than treating corners as a dominance proxy;
- a sparse-participant confidence cap where official XIs/keepers cannot be verified;
- no numerical probabilities without a fitted, validated model;
- explicit source-state conflicts rather than silently choosing one schedule;
- no directional live forecast when the exact live state cannot be reliably verified;
- exact settlement-provider definitions for niche markets such as corners.

Because no official XI/goalkeeper release was recovered, team-side confidence is capped and no player prop is recommended.

---

## Frozen candidate universe

**Decision-set ID:** `DS-P-130-V01`

The user supplied first-half O/U 0.5 and full-game O/U 2.5 and authorised analyst-selected team/corner picks.

| Candidate ID | Exact contract | Origin |
|---|---|---|
| `P-130-C01` | Beitar Haifa Yakov or Draw — Double Chance 1X | Analyst-selected |
| `P-130-C02` | 1st Half Goals Over 0.5 | User-supplied market branch |
| `P-130-C03` | 1st Half Goals Under 0.5 | User-supplied market branch |
| `P-130-C04` | Combined Total Goals Over 2.5 | User-supplied market branch |
| `P-130-C05` | Combined Total Goals Under 2.5 | User-supplied market branch |
| `P-130-C06` | Total Corners Under 10.5 — research threshold | Analyst-selected systematic corner threshold |

The corner threshold is research-grade only because the user's operator/provider was not specified.

---

# Current team-strength baseline

## Beitar Haifa Yakov

Latest recoverable 2025/26 results include:

- 6-0 vs FC Kababir
- 1-1 at Hapoel Daliyat Al-Karmel
- 4-0 vs Hapoel Ironi Or Akiva
- 4-1 vs Hapoel Ramot Menashe
- 4-0 at Maccabi Ahi Iksal
- 0-2 at Tirat HaCarmel
- 0-0 vs Hapoel Bnei Arrara Ara
- 4-1 at Hapoel Yafia
- 0-3 vs Tzeirey Haifa
- 3-0 at SC Mashhad

Latest-five recoverable line:

**4 wins, 1 draw, 0 losses; 19 goals scored, 2 conceded.**

Four of those five matches cleared 2.5 total goals.

A broader specialist summary lists Beitar with 55 goals scored and 33 conceded over 21 recorded matches. This is descriptive evidence, not a fitted attack coefficient.

---

## Hapoel Bnei Arrara Ara

Latest recoverable results include:

- 3-1 at SC Mashhad
- 2-0 at FC Kababir
- 0-0 at Beitar Haifa Yakov
- 3-0 vs Maccabi Ahi Iksal
- 0-0 at Hapoel Ihud Bnei Jatt
- 1-5 at Tzofi Haifa
- 0-4 at Tzeirey Haifa
- 2-1 vs SC Mashhad
- 0-3 at Hapoel Ihud Bnei Jatt
- 2-1 at Bnei Qalansawe

Latest-five recoverable line:

**3 wins, 2 draws, 0 losses; 8 goals scored, 1 conceded.**

This is a materially stronger defensive recent branch than the earlier 2025 period and prevents a high-confidence Beitar handicap or aggressive goal-total call.

---

# Head-to-head audit

Recoverable recent meetings:

| Date | Match | HT | FT |
|---|---|---:|---:|
| 2026-01-09 | Beitar Haifa Yakov vs Hapoel Bnei Arrara Ara | 0-0 | 0-0 |
| 2024-12-13 | Beitar Haifa Yakov vs Hapoel Bnei Arrara Ara | 3-0 | 4-0 |
| 2023-01-23 | Hapoel Bnei Arrara Ara vs Beitar Haifa Yakov | 0-1 | 1-1 |

Descriptive implications:

- Beitar are unbeaten in the three recoverable H2Hs.
- Two of three had at least one first-half goal.
- Only one of three cleared 2.5 full-match goals.
- The most recent meeting was 0-0 despite Beitar being a strong market favourite.

The H2H is a useful kill-path warning against assuming Beitar dominance or an automatic Over, but it is too small and roster-dependent to control the forecast.

---

# Market-state cross-check — not sporting evidence

Current external market feeds around the pre-start cutoff generally made Beitar the favourite:

- roughly 1.50–1.62 Beitar;
- roughly 3.8–4.0 draw;
- roughly 4.2–5.0 Hapoel Bnei Arrara;
- Asian handicap around Beitar -0.75;
- main goal line around 3.0.

These prices are recorded only to verify event/contract context. They are **not** converted into internal probabilities and are not used to claim value.

---

# Goal-process assessment

## First-half goal process

Recent Hapoel Bnei Arrara first-half states recoverable from current databases:

- SC Mashhad 1-2 Hapoel at HT
- FC Kababir 0-1 Hapoel at HT
- Beitar 0-0 Hapoel at HT
- Hapoel 3-0 Maccabi Ahi Iksal at HT
- Hapoel Ihud Bnei Jatt 0-0 Hapoel at HT

That gives a first-half goal in 3 of the latest 5 clearly recoverable Hapoel matches.

Beitar's late-season run includes repeated early scoring states:

- 2-0 HT in the 6-0 FC Kababir win;
- 2-0 HT in the 4-0 Hapoel Ironi Or Akiva win;
- 2-1 HT in the 4-1 Hapoel Ramot Menashe win;
- 2-0 HT in the 4-0 Maccabi Ahi Iksal win.

Two of the three recoverable H2Hs also contained a first-half goal.

**Central mechanism:** Beitar's recent attacking-start profile creates the clearest route to an early goal, while Hapoel possess enough transition/finishing ability to contribute.

**Kill path:** Hapoel reproduce the compact defensive state from the January 0-0 and slow the cup match into another 0-0 first half.

---

## Full-game goal process

Evidence supporting Over 2.5:

- Beitar's latest five recoverable matches: 4 of 5 Over 2.5.
- Beitar scored 19 goals in those five.
- Earlier Beitar results include repeated 4-, 5-, 6- and 8-goal match totals.
- A knockout/cup state can open if the trailing side must chase.

Evidence opposing Over 2.5:

- Hapoel's latest five recoverable matches: only 2 of 5 Over 2.5.
- Hapoel conceded only one goal across those five.
- The January H2H finished 0-0.
- Two of three recoverable H2Hs failed to clear 2.5.

### Qualitative pre-start score corridor

**Lower branch:** 1-0, 1-1, 2-0 Beitar  
**Central branch:** 2-1, 3-0 Beitar  
**Upper branch:** 3-1, 4-1 Beitar or an open 2-2 state  
**Upset branch:** Hapoel win 0-1 or 1-2 after absorbing Beitar pressure

---

# Corner process

The soccer framework requires a separate target-event chain for corners.

### Recoverable Beitar match corner totals

Recent direct samples include:

**9, 11, 7, 10, 7, 9, 9, 5**

Under 10.5 occurred in **7 of 8** samples.

### Recoverable Hapoel Bnei Arrara match corner totals

Recent direct samples include:

**16, 5, 4, 9, 7, 12, 5, 11**

Under 10.5 occurred in **5 of 8** samples.

Combined descriptive sample:

**12 of 16** recoverable matches finished below 10.5 corners.

The January 2026 H2H produced only **5 total corners**, all five recorded for Beitar.

### Missing corner layers

Not reliably available:

- crosses;
- blocked crosses;
- end-line entries;
- defensive clearances;
- tactical width;
- confirmed current formations;
- confirmed winger/fullback roles;
- exact bookmaker/stat-provider definition.

Therefore the corner selection cannot receive `LEAN` or `SUPPORTED`.

**Research corner:** Total Corners Under 10.5  
**Verdict:** `FORCED RANK`  
**Evidence:** `MEDIUM-LOW`

---

# Pre-start scenario map

| Scenario | Representative shape | Helps |
|---|---|---|
| Beitar controlled win | 2-0 | Beitar 1X; FT Under branch |
| Beitar normal attacking win | 2-1 / 3-0 | Beitar 1X, 1H O0.5, O2.5 |
| Hapoel compact branch | 0-0 / 1-0 / 1-1 | Beitar 1X often, 1H Under, FT Under |
| Open cup branch | 3-1 / 2-2 | 1H Over, FT Over |
| Hapoel upset | 0-1 / 1-2 | Beitar 1X fails |
| Corner-low | clean finishing / central play / few blocks | Corners U10.5 |
| Corner-high | repeated width + trailing-side chasing | Corners U10.5 fails |

---

# Detailed ranking rationale

## #1 — Beitar Haifa Yakov or Draw (1X)

- Beitar ended the recoverable 2025/26 sample 4-1-0 over the latest five, with a 19-2 goal balance.
- They are unbeaten in the three recoverable H2Hs.
- The contract survives a draw, important because the latest H2H was 0-0 and Hapoel themselves ended the recoverable sample 3-2-0.
- Beitar's attack supplies the wider ordinary win pathway, while Hapoel's recent defence preserves a draw branch.

It is capped at `FORCED RANK / MEDIUM-LOW` because official XIs/keepers are unavailable and the current game state became unverified once the earlier kickoff branch passed.

**Strongest failure path:** Hapoel's late-season defensive state persists and they win a low-event cup game.

---

## #2 — 1st Half Over 0.5 Goals

Beitar's late-season matches repeatedly contained early goals, and Hapoel had a first-half goal in 3 of the latest 5 clearly recoverable games.

Two of three recoverable H2Hs also had a first-half goal.

The January 0-0 and Hapoel's compact defensive state keep the 0-0 HT branch meaningful.

---

## #3 — Combined Total Over 2.5 Goals

Beitar's scoring form creates a credible 3+ goal pathway even if Hapoel contribute little.

However, Hapoel's latest five are much more Under-oriented and the latest H2H was 0-0.

Therefore this is only a thin pre-start lean.

---

## #4 — Total Corners Under 10.5

The direct historical corner ledger points toward a moderate rather than extreme corner total:

- Beitar sample: 7/8 below 10.5.
- Hapoel sample: 5/8 below 10.5.
- January H2H: 5 corners.

But the direct causal corner chain and exact provider definition are incomplete, so the active soccer derivative gate keeps this at `FORCED RANK`.

---

# Potential game winner

## Beitar Haifa Yakov — `FORCED WINNER — LOW CONFIDENCE / STATE-LIMITED`

Pre-start basis:

- stronger recoverable late-season attacking form;
- 4-1-0 latest-five record versus Hapoel's 3-2-0;
- 19-2 latest-five Beitar goal balance;
- unbeaten recoverable H2H;
- larger attacking ceiling.

**Strongest failure path:** Hapoel reproduce the compact defensive regime that held Beitar 0-0 in January and convert the cup match into a low-event upset.

The winner call is deliberately weaker than 1X because the draw remains a substantial branch.

---

# Final state notice

At 18:00:46 Melbourne time:

- the 08:00 UTC kickoff branch had passed;
- current AiScore/TotalCorner pages still exposed only zero-filled or blank state shells;
- no trustworthy clock, event timeline, or verified live score was recovered;
- TotalCorner simultaneously retained a later 09:00 UTC fixture listing.

Therefore:

`LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`

The four ranks are preserved solely as the pre-start evidence view.

---

# Source record

## Governing framework
- Sports Research Google Drive — `RULES_SOCCER.md`
- Sports Research Google Drive — `RULES_GENERAL.md`
- Sports Research Google Drive — active learning/model registers

## Current external research
- AiScore — exact fixture, H2H, historical results, current state shell
- TotalCorner — fixture cross-check, goal/corner event history, recent corner counts, alternate kickoff branch
- Betimate — Beitar historical team/results profile
- Tips.GG — State Cup Round 1 competition/fixture cross-check
- Current market feeds — event/line existence only, not sporting probability

## Source-quality limitations
- No official Israel Football Association match-centre page was successfully recovered for this exact event.
- Official starting XIs and goalkeepers were not recovered.
- Venue was not verified.
- Current fixture sources disagree on kickoff by one hour.
- Current live state is not trustworthy enough for directional live analysis.
- Corner-provider definition is unknown.

---

# Logging confirmation

**Canonical ID:** `P-130`

**Issued view:** `V01`

**Google Drive modified:** `NO`

**Delivery mode:** `DOWNLOADABLE MARKDOWN FILE`

**Retrospective:** `NOT INCLUDED`

**Current disposition:** `START CROSSED ON EARLIER SCHEDULE BRANCH — LIVE STATE NOT VERIFIED`

# P-131 — Penrith Panthers vs Canterbury-Bankstown Bulldogs — NRL Round 26

## Final pregame ranking

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Canterbury Bulldogs +9.5** | **LEAN** | **MEDIUM-HIGH** |
| **2** | **Combined Total Under 40.5 Points** | **LEAN** | **MEDIUM** |
| **3** | **Combined Total Over 40.5 Points** | **FORCED RANK** | **MEDIUM** |
| **4** | **Penrith Panthers -9.5** | **AVOID** | **MEDIUM-HIGH** |

**Potential game winner:** **Penrith Panthers — LEAN**

**Central thesis:** Penrith are the stronger team and preferred outright winner, but the current participant state makes a 10+ point Panthers win materially less robust than the winner call. Canterbury +9.5 survives every Bulldogs win and any Bulldogs loss by 1–9.

---

## Record metadata

| Field | Value |
|---|---|
| Canonical ID | `P-131` |
| Competition | NRL Telstra Premiership 2026 |
| Round | 26 |
| Venue | CommBank Stadium, Sydney |
| Kickoff | 2026-08-28 20:00 Australia/Sydney |
| Pregame refresh | 2026-08-28 19:58:10 Australia/Melbourne |
| GAME-STATE | `PREGAME` |
| Ground | Good |
| Weather | Fine |
| Final teams | `CONFIRMED_OFFICIAL` |
| Method | `MDS-2026.08.28-v2.4` |
| Sport module | `RULES_NRL_RUGBY.md` |
| Numerical model | `NOT FIT / NOT VALIDATED` |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Google Drive | `READ-ONLY REFERENCE — NOT MODIFIED` |
| Retrospective | `NOT INCLUDED` |

---

# Decision set and contract geometry

**Decision-set ID:** `DS-P-131-V01`

| Candidate | Exact contract |
|---|---|
| `P-131-C01` | Bulldogs +9.5 |
| `P-131-C02` | Panthers -9.5 |
| `P-131-C03` | Over 40.5 Points |
| `P-131-C04` | Under 40.5 Points |

The spread contracts are exact half-point complements.

- **Bulldogs +9.5 wins:** Bulldogs win/draw, or lose by 1–9.
- **Panthers -9.5 wins:** Penrith win by 10+.

The total contracts are exact half-point complements.

- **Over 40.5 wins:** 41+ points.
- **Under 40.5 wins:** 40 or fewer.

No push exists.

---

# Official final participant state

## Penrith Panthers

1. Dylan Edwards  
2. Thomas Jenkins  
3. Izack Tago  
4. Casey McLean  
5. Brian To'o  
6. Jack Cole  
7. Nathan Cleary  
8. Moses Leota  
9. Freddy Lussick  
10. Liam Henry  
11. Isaiah Papali'i  
12. Liam Martin  
13. Lindsay Smith  

Key interchange includes Scott Sorensen, Luke Garner and Billy Phillips.

### Material Penrith absences

- **Isaah Yeo — pectoral**
- **Mitch Kenny — leg**
- **Jack Cogger — suspended**
- **Paul Alamoti — hamstring**

This is the most important adjustment away from Penrith's dominant season baseline.

Yeo's absence changes middle distribution, defensive organisation and set connection. Kenny's absence changes hooker continuity. Cogger's suspension leaves Jack Cole at five-eighth in only his third NRL appearance of the season.

Penrith still retain their premium control pieces in **Nathan Cleary, Dylan Edwards, Brian To'o, Moses Leota and Liam Martin**, but today's organising unit is weaker than the broad-season average.

---

## Canterbury Bulldogs

1. Connor Tracey  
2. Jacob Kiraz  
3. Matt Burton  
4. Bronson Xerri  
5. Enari Tuala  
6. Stephen Crichton  
7. Lachlan Galvin  
8. Max King  
9. Bailey Hayward  
10. Leo Thompson  
11. Viliame Kikau  
12. Jacob Preston  
13. Jaeman Salmon  

Interchange:
- Jake Turpin
- Alekolasimi Jones
- Harry Hayes
- Josh Curran

### Material Canterbury state

- **Kurt Mann — groin / unavailable**
- Enari Tuala returns from a knee issue.
- A Monday illness scare affected multiple players, but coach Cameron Ciraldo reported the group recovered and trained normally by Wednesday.
- Stephen Crichton remains at five-eighth with Lachlan Galvin at halfback.
- Matt Burton remains in the centres.

---

# Broad 2026 strength baseline

| Metric | Panthers | Bulldogs |
|---|---:|---:|
| Record | 16-6 | 11-11 |
| Points scored | 621 | 446 |
| Points conceded | 327 | 478 |
| Avg points scored | ~28 | ~20 |
| Avg points conceded | ~14 | ~21 |
| Completion rate | 80% | 77% |
| Tackle efficiency | 88.6% | 87.8% |
| Avg play-the-ball | 3.37s | 3.48s |
| Points differential | +294 | -32 |

This clearly establishes Penrith as the stronger broad-season side.

It does **not** justify copying the season differential into today's -9.5 because Yeo, Kenny and Cogger are unavailable and Canterbury's recent defensive regime is materially better than its broad-season average.

---

# Recent-form regime

## Penrith latest five

| Opponent | Result | Total |
|---|---:|---:|
| Storm | W 22-14 | 36 |
| Roosters | L 6-12 | 18 |
| Warriors | L 12-28 | 40 |
| Raiders | W 42-18 | 60 |
| Eels | W 24-18 | 42 |

Recent averages:
- Penrith scored: **21.2**
- Opponents scored: **18.0**
- Combined: **39.2**
- Under 40.5: **3/5**

The Storm win is particularly relevant: Penrith led 22-0 at halftime and survived to win 22-14 despite only 42% possession, losing the penalty count 10-4 and spending periods with players in the sin bin. That demonstrates both their defensive control ceiling and the volatility created by discipline/card states.

---

## Canterbury latest five

| Opponent | Result | Total |
|---|---:|---:|
| Dragons | W 44-14 | 58 |
| Rabbitohs | L 6-22 | 28 |
| Roosters | L 18-20 | 38 |
| Storm | W 36-22 | 58 |
| Warriors | W 18-6 | 24 |

Recent averages:
- Canterbury scored: **24.4**
- Opponents scored: **16.8**
- Combined: **41.2**
- Under 40.5: **3/5**

Canterbury's recent defensive output is significantly stronger than its broad-season 21 points conceded per match, which is important when assessing Penrith -9.5.

---

# Current-season H2H

## Round 6 — Bulldogs 32, Panthers 16

Canterbury handed Penrith their first defeat of 2026.

Decision-relevant first-half process:

- Bulldogs completed **18 of 21 sets (85%)**.
- Bulldogs produced **five line breaks to Penrith's two**.
- Canterbury scored three tries in the first 20 minutes.
- Penrith made four first-half errors.

The result is not used as an automatic vote for Canterbury. The lineups differ. But it demonstrates a genuine repeatable matchup mechanism:

`completion + field position + Kikau/edge pressure + early line breaks -> Penrith forced out of preferred control state`

That makes a Bulldogs +9.5 branch materially credible.

---

# Venue and incentives

- **CommBank Stadium**
- Official current match page: **ground good, weather fine**
- Penrith have won nine of the last 11 meetings overall.
- Canterbury have lost seven of their last eight games at CommBank Stadium.
- Penrith are fighting at the top of the ladder/minor premiership race.
- Canterbury remain alive in the finals race and effectively need to keep winning.

These incentives increase competitive intensity but are not assigned an automatic Over/Under effect.

---

# Possession / field-position tree

## Penrith control pathway

`Cleary kicking + Edwards organisation/yardage + To'o/Jenkins exit metres + Leota/Henry middle carries -> strong set starts -> repeated attacking-zone possessions -> efficient finishing`

This remains the strongest winner pathway because Penrith retain Cleary, Edwards, To'o, Leota and elite defensive personnel.

### Why the 10+ separation branch is less certain

Missing Yeo, Kenny and Cogger means:
- less established middle ball-playing;
- changed dummy-half service;
- changed five-eighth combination;
- more variance in red-zone execution and defensive communication.

That weakens **Panthers -9.5** more than it weakens **Panthers winner**.

---

## Canterbury cover/upset pathway

`high completion + Max King/Leo Thompson carries + Kikau/Preston edge pressure + Galvin/Crichton kicking/shape -> prevent Penrith repeat-set avalanche -> remain within one or two scores`

Round 6 proved Canterbury can execute this mechanism against Penrith.

Canterbury do not need to win for +9.5 to succeed.

---

# Total analysis

## Under 40.5 support

- 3 of Penrith's last 5 finished Under.
- 3 of Canterbury's last 5 finished Under.
- Combined recent sample: **6/10 Under 40.5**.
- Penrith remain the competition's strongest broad defensive side by points conceded.
- Canterbury's recent defensive regime has improved.
- Penrith's Yeo/Kenny/Cogger absences lower confidence in projecting their season 28-point attack without adjustment.
- High-stakes set-for-set football can create long field-position phases.

## Over 40.5 support

- Penrith average ~28 scored over the season.
- Canterbury average ~20.
- The Round 6 H2H finished **48**.
- Canterbury just scored 44 against the Dragons.
- Missing Yeo/Kenny can weaken Penrith's middle defence as well as their attack.
- Cleary, Edwards, To'o, Kikau, Preston, Galvin, Crichton and Burton preserve substantial attacking upside.
- Sin bins, repeated infringements, short fields and late-chasing states can rapidly lift an NRL total.
- Ground and weather do not suppress scoring.

### Total conclusion

**Under 40.5 is only a moderate lean.**

The current-five-game defensive regimes and Penrith's organiser absences place the central lower corridor around the high-30s/40 mark, but the Over tail remains large. This is a much thinner call than Bulldogs +9.5.

---

# Joint qualitative score corridor

## Central branch — Penrith win, Bulldogs cover

Representative:
- Penrith 24-16
- Penrith 24-18
- Penrith 26-18

This is the most important branch.

It supports:
- **Penrith winner**
- **Bulldogs +9.5**
- total around the supplied 40.5 boundary.

## Low-total control branch

Representative:
- Penrith 20-12
- Penrith 22-14
- Penrith 24-12

Favours:
- Bulldogs +9.5 in most states
- Under 40.5
- Penrith winner

## Penrith separation branch

Representative:
- Penrith 28-12
- Penrith 30-14
- Penrith 32-16

Requires:
- Canterbury errors/completion decline;
- Cleary field-position dominance;
- repeated attacking sets;
- Penrith edge finishing.

Favours:
- Panthers -9.5
- Over increasingly as Canterbury contributes.

## Open competitive branch

Representative:
- Penrith 26-22
- Penrith 28-20
- Bulldogs 24-22

Favours:
- Bulldogs +9.5
- Over 40.5

## Bulldogs upset branch

Representative:
- Bulldogs 22-18
- Bulldogs 24-20
- Bulldogs 26-18

Favours:
- Bulldogs +9.5
- Bulldogs outright
- total depends exact score.

---

# Strongest kill paths

## Bulldogs +9.5

Canterbury's completion/field-position process collapses and Cleary creates a repeat-set avalanche, allowing Penrith to win by two or more converted tries.

## Under 40.5

Both sides finish efficiently; Canterbury exploit Penrith's missing Yeo/Kenny state while Penrith still produce 24–30 themselves. A sin-bin or late-chasing sequence is especially dangerous.

## Over 40.5

Canterbury's improved defence persists, Penrith's replacement organising unit lacks fluency, and the game finishes around 22-14 or 24-14.

## Panthers -9.5

Canterbury reproduce enough of the Round-6 completion/line-break mechanism to stay within nine even if Penrith win.

---

# Detailed ranking rationale

## #1 — Bulldogs +9.5 — LEAN / MEDIUM-HIGH

This is the most robust supplied contract.

It wins if:
- Canterbury win;
- the game is drawn;
- Penrith win by 1–9.

Penrith are clearly stronger over the season, but the exact current team is missing Yeo, Kenny and Cogger. Canterbury have demonstrated a real Penrith-specific upset mechanism this season and have recently defended better than their season average.

The line therefore provides substantial margin protection.

---

## #2 — Under 40.5 — LEAN / MEDIUM

Both clubs' latest-five combined scoring environments sit around 39–41 points, with six of ten games below 40.5.

Penrith's current organiser absences make a fully efficient 28-point attack less certain.

However, 40.5 is a low NRL total and the attacking/discipline tail remains substantial, so this cannot be rated as highly as Bulldogs +9.5.

---

## #3 — Over 40.5 — FORCED RANK / MEDIUM

The Over has a coherent route:
- Penrith's season offence;
- Canterbury's improved current offence;
- current-season H2H total of 48;
- Penrith middle-organisation absences;
- short-field/card/late-chase tails.

It ranks below Under only because recent defensive regimes and current Penrith attacking continuity slightly favour the lower corridor.

---

## #4 — Panthers -9.5 — AVOID / MEDIUM-HIGH

Penrith are the preferred winner, but -9.5 requires an additional **separation event**.

A 24-16, 26-18 or 24-18 Penrith win is entirely compatible with the central matchup view while losing this handicap.

Canterbury's Round-6 win and current recent defence make a 10+ Penrith margin less robust than the other supplied options.

`AVOID` is evidence-relative and is not a negative expected-value claim.

---

# Potential game winner

## Penrith Panthers — LEAN

Supporting mechanisms:
- 16-6 record;
- +294 points differential;
- league-best-level defensive baseline;
- Nathan Cleary available;
- Dylan Edwards, Brian To'o, Moses Leota, Liam Martin and Isaiah Papali'i available;
- stronger completion and season scoring profile;
- nine wins in the last 11 meetings.

Main failure path:
- Canterbury execute the same high-completion/line-break/edge-pressure mechanism seen in Round 6;
- Yeo/Kenny absence reduces Penrith control;
- Galvin/Crichton/Kikau create enough short-field pressure for another upset.

### Coherence statement

**Penrith winner** and **Bulldogs +9.5** are not contradictory.

The central model contains a substantial:

`PENRITH WIN BY 1–9`

branch.

---

# Final card

1. **Canterbury Bulldogs +9.5**
2. **Combined Total Under 40.5 Points**
3. **Combined Total Over 40.5 Points**
4. **Penrith Panthers -9.5**

**Potential game winner:** **Penrith Panthers**

**GAME-STATE at final frozen pregame refresh:** `PREGAME`

**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value state:** `NO VALUE DETERMINABLE`

---

# Sources used

## Sports Research / Google Drive
- `RULES_NRL_RUGBY.md`
- `RULES_GENERAL.md`
- `LEARNING_REGISTER.md`
- `PREDICTION_LOG_COMBINED.md` — historical mechanism evidence only

## Official/current external
- NRL Round 26 official team lists / late mail
- Penrith Panthers `NRL Late Mail: Round 26`
- Canterbury Bulldogs `Round 26 Team News: NRL Final Squad`
- Penrith official Round 26 match page
- NRL Penrith and Canterbury club profiles
- NRL casualty ward
- NRL Round 6 Bulldogs-Panthers match report/live blog
- NRL Round 25 Storm-Panthers match report

---

# Logging status

**Canonical ID:** `P-131`  
**Issued view:** `V01`  
**Google Drive modified:** `NO`  
**Delivery:** `DOWNLOADABLE MARKDOWN FILE`  
**Retrospective:** `NOT INCLUDED`

**Important:** This file freezes the pregame evidence state at 19:58:10 Australia/Melbourne, shortly before the scheduled 20:00 kickoff. If the match has started by the time the file is opened, it should not be reinterpreted as a live forecast.


# P-132 — RC Vannes Sevens vs LOU Rugby Sevens — In Extenso SuperSevens, Pau

## Executive forecast

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Combined Total Under 35.5 Points** | **LEAN** | **MEDIUM** |
| **2** | **Lyon +9.5** | **FORCED RANK** | **MEDIUM-LOW** |
| **3** | **Combined Total Over 35.5 Points** | **FORCED RANK** | **MEDIUM** |
| **4** | **Vannes -9.5** | **AVOID** | **MEDIUM-LOW** |

**Potential game winner:** **Vannes — FORCED WINNER / LOW CONFIDENCE**

### Short conclusion

Vannes are the stronger current team and the preferred outright winner, but the available 2026 evidence does not make a **10+ point Vannes win** the central state.

At the first Biarritz stage:
- Vannes beat Castres **24-19**
- Vannes beat Montpellier **28-12**
- Vannes then lost **5-10** to Toulouse in a sudden-death quarter-final
- Lyon lost **17-19** to the Baabaas
- Lyon lost **14-19** to Toulouse

That gives:
- Vannes margins: **+5, +16, -5**
- Lyon margins: **-2, -5**

Lyon therefore stayed inside +9.5 in both of its current-stage matches, while Vannes produced only one 10+ point win in three matches.

The strongest total signal comes from the tournament itself: across the **24 men's matches at Biarritz**, the average combined score was approximately **29.9 points**, and only **7 of 24** cleared 35.5. The 16 pool matches averaged **31.5**, with only **5 of 16** above 35.5.

---

## Record metadata

| Field | Value |
|---|---|
| Canonical ID | `P-132` |
| Sport | Rugby sevens |
| Competition | In Extenso SuperSevens 2026/27 |
| Stage | Pau — second qualifying stage |
| Pool | Men's Pool D |
| Event | RC Vannes Sevens vs LOU Rugby Sevens |
| Venue | Stade du Hameau, Pau, France |
| Scheduled kickoff | 2026-08-28 16:34 CEST |
| Australia/Melbourne kickoff | 2026-08-29 00:34 AEST |
| Final pregame state refresh | 2026-08-29 00:20:14 Australia/Melbourne |
| GAME-STATE | `PREGAME` |
| Method | `MDS-2026.08.28-v2.4 — GENERAL MODULE ADAPTED TO RUGBY SEVENS` |
| Dedicated rugby-sevens Drive module | `NONE` |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Google Drive | `READ-ONLY REFERENCE — NOT MODIFIED` |
| Delivery | `DOWNLOADABLE MARKDOWN FILE` |
| Retrospective | `NOT INCLUDED` |

---

# Framework boundary

The Sports Research Drive currently has a rugby-league/NRL module, but it explicitly says that rugby union is a different code and should not be pooled with rugby league.

Rugby sevens is also materially different from both NRL and ordinary 15-a-side union.

Therefore this card uses the **general framework** and adapts the score process to rugby sevens:

- short-duration possessions;
- restart retention;
- turnover-to-breakaway conversion;
- line-break frequency;
- try scoring;
- conversion value;
- yellow-card/man-down tails;
- pace and open-space exposure;
- late score-state chasing;
- pool-stage qualification incentives.

No NRL tackle-set/six-again/golden-point mechanics are transferred.

---

# Exact decision set

**Decision-set ID:** `DS-P-132-V01`

| Candidate ID | Exact contract |
|---|---|
| `P-132-C01` | Vannes -9.5 |
| `P-132-C02` | Lyon +9.5 |
| `P-132-C03` | Combined Total Over 35.5 |
| `P-132-C04` | Combined Total Under 35.5 |

The spread pair is an exact half-point complement.

- Vannes -9.5 wins if Vannes win by 10+.
- Lyon +9.5 wins if Lyon win/draw or lose by 1–9.

The total pair is an exact half-point complement.

- Over 35.5 wins at 36+.
- Under 35.5 wins at 35 or fewer.

No supplied line can push.

---

# Event verification

The Ligue Nationale de Rugby / SuperSevens schedule places:

**RC Vannes Sevens vs LOU Rugby Sevens**
at **16:34 local time in Pau on 28 August 2026**.

The match is part of **Pool D**, which contains:

- RC Vannes Sevens
- RC Toulon Sevens
- Castres Olympique Sevens
- LOU Rugby Sevens

The official/FFR preliminary schedule has:

- Toulon vs Castres
- Vannes vs Lyon
- Toulon vs Vannes
- Castres vs Lyon

Vannes' own official club article also lists:
- 16:34 Vannes vs Lyon
- 22:15 Vannes vs Toulon

At the final research cutoff the scheduled kickoff had **not** passed.

---

# Competition format / state

The 2026/27 SuperSevens uses two summer qualifying stages:

- Biarritz: 21–22 August
- Pau: 28–29 August

The men's tournament contains the 14 TOP 14 clubs plus Monaco and the Baabaas.

At each summer stage:
- Friday is pool play;
- Saturday is knockout/finals play.

Only eight men's teams qualify for the February 2027 final.

Vannes entered Pau in a strong qualification position after finishing sixth at Biarritz.

Lyon finished 13th at Biarritz and therefore has considerably more pressure to improve its Pau result.

That urgency is relevant only through tactics: Lyon cannot simply protect a narrow loss if qualification requires stronger pool performance, but a chasing state can also create turnover/breakaway opportunities for Vannes.

---

# Current participant certainty

## Vannes

Vannes published an official current Pau group on 27 August, but the roster is presented graphically and the player-by-player names could not be reliably extracted from the accessible text response.

The LNR had identified **Enzo Benmegal** as a Vannes France-7-level player at the Biarritz stage, but this card does **not** assume his Pau participation without a text-verifiable current roster.

## Lyon

A current official player-by-player Pau squad could not be reliably recovered from an authoritative source before the cutoff.

At Biarritz, LNR highlighted **Arthur Mathiron** and **Charly Mignot** as players with France 7 experience, but their participation in this exact Pau match is **not assumed as confirmed**.

### Participant consequence

Rugby sevens is highly participant-sensitive because one specialist playmaker, restart jumper, sweeper or elite finisher can materially change a 14-minute score distribution.

Therefore:
- side confidence is capped;
- no player props are issued;
- no named-player mechanism is treated as confirmed for this match.

---

# Biarritz 2026 — Vannes current-form baseline

Official/current-stage results:

| Match | Result | Margin | Total |
|---|---:|---:|---:|
| Vannes vs Castres | W 24-19 | +5 | 43 |
| Montpellier vs Vannes | W 12-28 | +16 | 40 |
| Vannes vs Toulouse | L 5-10, sudden death | -5 | 15 |

Across the three matches:

- Points for: **57**
- Points against: **41**
- Average scored: **19.0**
- Average conceded: **13.7**
- Average total: **32.7**

Vannes finished:
- **1st in its Biarritz pool**
- **6th overall at the stage**

### Vannes mechanisms

Positive:
- demonstrated ability to score 24–28 in pool play;
- enough pace/finishing to separate from Montpellier;
- strong enough defence to hold Toulouse to 10 in a knockout match;
- entered Pau virtually in a final-qualification position.

Counterweight:
- the Castres win was only by five;
- Toulouse held them to five;
- one 16-point win does not establish a reusable -9.5 separation rate.

---

# Biarritz 2026 — Lyon current-form baseline

FFR / specialist results:

| Match | Result | Margin | Total |
|---|---:|---:|---:|
| Lyon vs Baabaas | L 17-19 | -2 | 36 |
| Toulouse vs Lyon | L 19-14 | -5 | 33 |

Across the two matches:

- Points for: **31**
- Points against: **38**
- Average scored: **15.5**
- Average conceded: **19.0**
- Average total: **34.5**

Lyon finished:
- winless in Pool C;
- **13th overall at Biarritz**.

### Lyon mechanisms

Negative:
- did not win a Biarritz match;
- conceded 19 in both;
- entered Pau with substantially more qualification pressure.

Positive:
- both losses were competitive;
- both remained inside today's +9.5 line;
- 17 points against the Baabaas and 14 against Toulouse show a non-trivial scoring floor against quality sevens opposition.

This is the main reason **Lyon +9.5** is preferred to **Vannes -9.5**.

---

# Current-stage comparison

A simple descriptive blend — not a fitted model — gives:

- Vannes Biarritz scoring: 19.0
- Lyon Biarritz conceding: 19.0
- Lyon Biarritz scoring: 15.5
- Vannes Biarritz conceding: 13.7

That points to a rough **mid-30s combined environment** and a much smaller margin than 9.5 as the central descriptive state.

This arithmetic is used only as a sanity check.

No probability is generated from it.

---

# Tournament total environment

## Biarritz pool phase

The 16 men's pool matches produced **504 total points**.

Average:

**31.5 combined points per match**

Over 35.5:

**5 of 16**

Under 35.5:

**11 of 16**

## Entire Biarritz men's stage

Adding the 8 knockout/placement matches gives:

- total points: **718**
- matches: **24**
- average combined total: approximately **29.9**

Over 35.5:

**7 of 24**

Under 35.5:

**17 of 24**

This is descriptive current-competition evidence, not a calibrated probability.

### Why the line can still go Over

Vannes' two pool games were both above 35.5:
- 43
- 40

Lyon's Baabaas game finished:
- 36

So the Over has direct team-specific support even though the broader stage environment is lower.

---

# Weather / surface

Current Pau reporting before the stage described:

- sunshine;
- roughly low-to-mid 20s Celsius;
- well-prepared pitch.

Near the Vannes–Lyon match window, current forecasts remained:
- dry;
- warm;
- low precipitation risk.

There is therefore no meaningful wet-weather suppression mechanism.

For sevens this is relevant because:
- dry footing supports acceleration and offloads;
- clean handling can improve line-break conversion;
- but dry weather alone does not force a high total.

No automatic weather-Over adjustment is applied.

---

# Sevens-specific game tree

## Central close Vannes win

Representative shapes:

- Vannes 19-14
- Vannes 21-14
- Vannes 22-14

Implications:

- Vannes winner
- Lyon +9.5 in 19-14 and 21-14
- total frequently around or below 35.5

This is the central reason winner and handicap differ.

---

## Low-total control branch

Representative:

- Vannes 17-12
- Vannes 19-10
- Vannes 21-12

Mechanisms:
- restart possession is relatively balanced;
- Lyon limits clean first-phase line breaks;
- Vannes converts enough opportunities to win without repeated breakaways;
- conversion misses keep the score below the nominal try count.

Favours:
- Under 35.5
- Lyon +9.5
- Vannes winner

---

## Open trading branch

Representative:

- Vannes 24-14
- Vannes 24-19
- Vannes 28-12
- Vannes 26-17

Mechanisms:
- restart turnovers;
- rapid turnover-to-space conversion;
- defensive line-break misses;
- Lyon chasing qualification;
- yellow-card/man-down episode.

Favours:
- Over 35.5
- Vannes -9.5 only in wider-separation states.

---

## Lyon upset branch

Representative:

- Lyon 19-17
- Lyon 21-17
- Lyon 22-19

Mechanisms:
- Lyon's Biarritz close-game attack persists;
- Vannes fails to dominate restarts;
- Lyon finishes its break chances more efficiently;
- Vannes' Biarritz qualification cushion reduces the need to overextend tactically.

Favours:
- Lyon +9.5
- potential outright upset
- total around the line depending conversions.

---

## Vannes blowout branch

Representative:

- Vannes 26-12
- Vannes 28-10
- Vannes 31-12

Mechanisms:
- Vannes wins restart possession;
- Lyon's qualification chasing creates turnover exposure;
- Vannes repeatedly converts open-field mismatches;
- card/man-down state widens the game quickly.

Favours:
- Vannes -9.5
- Over 35.5 in many variants.

This is a credible tail, not the central branch.

---

# Strongest kill paths

## Under 35.5

Vannes reproduce the high-scoring pool attack rather than the Toulouse control game, while Lyon contribute 14–19 themselves. A 24-14 or 24-19 result clears the line.

## Lyon +9.5

Vannes win restarts, generate repeated clean breaks, and turn Lyon's qualification pressure into a multi-try separation.

## Over 35.5

The match follows Lyon's 19-14 Toulouse pattern or Vannes' 5-10 knockout pattern, with enough possession but insufficient finishing to reach six-try territory.

## Vannes -9.5

Lyon reproduce the competitive margins shown against the Baabaas and Toulouse and remain within one converted try or a single late score.

---

# Final ranking

| Rank | Candidate | Pick | Verdict | Evidence | Probability |
|---:|---|---|---|---|---|
| **1** | `P-132-C04` | **Under 35.5** | `LEAN` | `MEDIUM` | `NOT_GENERATED` |
| **2** | `P-132-C02` | **Lyon +9.5** | `FORCED RANK` | `MEDIUM-LOW` | `NOT_GENERATED` |
| **3** | `P-132-C03` | **Over 35.5** | `FORCED RANK` | `MEDIUM` | `NOT_GENERATED` |
| **4** | `P-132-C01` | **Vannes -9.5** | `AVOID` | `MEDIUM-LOW` | `NOT_GENERATED` |

---

# Ranking rationale

## #1 — Under 35.5

Best broad structural support.

Evidence:
- Biarritz men's stage average approximately 29.9;
- 17 of 24 stage matches below 35.5;
- pool-stage average 31.5;
- 11 of 16 pool matches below 35.5;
- Lyon's two current-stage totals: 36 and 33;
- simple Vannes/Lyon current-stage blend centres in the mid-30s.

Why not stronger:
- Vannes' two Biarritz pool games were 43 and 40;
- dry conditions favour clean attacking execution;
- sevens scoring is highly clustered around restart/card/breakaway events.

**Verdict:** `LEAN`

---

## #2 — Lyon +9.5

Lyon do not need to win.

They can:
- win;
- draw;
- lose by 1–9.

At Biarritz they lost by only:
- 2;
- 5.

Vannes' three current-stage margins were:
- +5;
- +16;
- -5.

Only one Vannes result produced a 10+ win.

Roster uncertainty prevents a stronger label.

**Verdict:** `FORCED RANK`

---

## #3 — Over 35.5

The Over has direct team-specific support:

- Vannes 24-19 = 43
- Vannes 28-12 = 40
- Lyon 17-19 = 36

It is helped by:
- dry surface;
- Vannes attacking ceiling;
- Lyon qualification urgency;
- restarts, cards and open-field turnovers.

But it sits against the broader current-stage scoring environment.

**Verdict:** `FORCED RANK`

---

## #4 — Vannes -9.5

Vannes are the preferred winner, but this line requires a **10+ point separation**.

The evidence for a winner is much stronger than the evidence for that margin.

Lyon's two Biarritz defeats were competitive, and Vannes covered a comparable 9.5 threshold in only one of their three Biarritz matches.

**Verdict:** `AVOID`

`AVOID` is evidence-relative and is not a negative expected-value statement.

---

# Potential game winner

## RC Vannes Sevens — `FORCED WINNER / LOW CONFIDENCE`

Why Vannes:

- 2-0 Biarritz pool record;
- 6th-place stage finish;
- +21 pool point differential;
- beat Castres and Montpellier;
- pushed Toulouse to sudden death in the quarter-final;
- entered Pau virtually inside the eight-team final qualification picture.

Why confidence remains low:

- exact Pau squads could not be fully text-verified;
- sevens has extreme match-to-match variance;
- Lyon's two Biarritz losses were both close;
- the match lasts only a short number of possessions, making one restart sequence or card disproportionately important.

### Coherence

**Vannes winner** and **Lyon +9.5** are compatible.

A central score such as:

**Vannes 21-14**

produces both outcomes.

---

# Source record

## Google Drive framework
- Sports Research `RULES_GENERAL.md`
- Sports Research `RULES_NRL_RUGBY.md` — used only for the explicit code-separation rule; its NRL mechanics were not applied
- Sports Research active model/learning controls

## Official / governing current sources
- Ligue Nationale de Rugby / SuperSevens official site — competition structure and Pau stage
- Fédération Française de Rugby — Pau Pool D preliminary schedule
- Rugby Club Vannes official article — current Pau schedule and Biarritz review
- FFR Biarritz results recap — exact 2026 men's results

## Specialist/current supporting sources
- Sevens Rugby — Biarritz men's results, pool standings and stage placing
- Rugbyrama — Pau opening-day conditions / stage context
- current Pau weather reports — environmental cross-check only

### Excluded / downweighted
- stale LNR roster pages from prior seasons were not treated as current squad evidence
- sportsbook/tipster model projections were not used as internal probability
- no historical H2H was found that was sufficiently relevant to control this current-stage matchup

---

# Logging confirmation

**Canonical ID:** `P-132`

**Issued view:** `V01`

**Google Drive modified:** `NO`

**Delivery mode:** `DOWNLOADABLE MARKDOWN FILE`

**GAME-STATE at final frozen cutoff:** `PREGAME`

**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value state:** `NO VALUE DETERMINABLE`

**Retrospective:** `NOT INCLUDED`

**Important:** This file freezes the pregame evidence state at 00:20:14 Australia/Melbourne, approximately 14 minutes before the scheduled kickoff. If the match has started when this file is opened, it should not be reinterpreted as a live forecast.

# P-134 — Cape Verde vs Guinea — FIBA Basketball World Cup 2027 African Qualifiers

## Executive forecast

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Cape Verde +10.5** | **LEAN** | **MEDIUM-HIGH** |
| **2** | **Combined Total Under 150.5 Points** | **LEAN** | **MEDIUM** |
| **3** | **Combined Total Over 150.5 Points** | **FORCED RANK** | **MEDIUM** |
| **4** | **Guinea -10.5** | **AVOID** | **MEDIUM-HIGH** |

**Potential game winner:** **Guinea — LEAN**

### Central interpretation

Guinea are the preferred outright winner because their current Window 4 talent pool is deeper and more physically complete, while Cape Verde are without Edy Tavares despite his appearance on an earlier preliminary roster. However, the evidence does **not** make a Guinea win by 11+ the central state.

The most coherent central branch is approximately:

- Guinea 75–69
- Guinea 77–70
- Guinea 78–71

Those branches support:
- **Cape Verde +10.5**
- **Guinea outright**
- **Under 150.5** in most central variants

---

## Record metadata

| Field | Recorded value |
|---|---|
| Canonical ID | `P-134` |
| Sport | Basketball |
| Competition | FIBA Basketball World Cup 2027 African Qualifiers |
| Stage | Second Round — Group E |
| Event | Cape Verde vs Guinea |
| Venue | Salle Multidisciplinaire de Radès, Radès, Tunisia |
| Scheduled tipoff | 2026-08-28 15:00 UTC |
| Melbourne tipoff | 2026-08-29 01:00 AEST |
| Final research refresh | 2026-08-29 00:47 Australia/Melbourne |
| GAME-STATE | `PREGAME` |
| Method | `MDS-2026.08.28-v2.4` |
| Basketball module | `RULES_BASKETBALL.md` |
| Numerical state | `NTS-2026.08.25-v0.2 — STAGE 0 / PRE-FIT` |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Google Drive | `READ-ONLY REFERENCE — NOT MODIFIED` |
| Retrospective | `NOT INCLUDED` |

---

# Framework controls applied

The active basketball framework requires:

- event, venue, FIBA rules and contract identity to be frozen before ranking;
- roster/availability to be treated separately from expected minutes and role;
- possession, shot quality, turnovers, offensive rebounds and free throws to drive the score process;
- raw PPG not to substitute for opponent-adjusted possessions/efficiency;
- spread and total to come from one coherent joint-score corridor;
- large spread separation to be modelled separately from the winner;
- late fouling/overtime and garbage time to remain explicit tails;
- no published probability or value claim because the basketball model is not fit or validated.

---

# Frozen decision set

**Decision-set ID:** `DS-P-134-V01`

| Candidate ID | Exact contract |
|---|---|
| `P-134-C01` | Cape Verde +10.5 |
| `P-134-C02` | Guinea -10.5 |
| `P-134-C03` | Combined Total Over 150.5 |
| `P-134-C04` | Combined Total Under 150.5 |

### Geometry

**Cape Verde +10.5**
- WIN if Cape Verde wins, draws, or loses by 1–10
- LOSS if Guinea wins by 11+

**Guinea -10.5**
- WIN if Guinea wins by 11+
- LOSS otherwise

**Over 150.5**
- WIN at 151+
- LOSS at 150 or below

**Under 150.5**
- WIN at 150 or below
- LOSS at 151+

All four are half-point contracts with no push.

Exact operator overtime/void rules were not supplied.

---

# Current official event state

FIBA lists:

**Cape Verde vs Guinea**  
Second Round, Group E  
Salle Multidisciplinaire de Radès, Tunisia  
28 August 2026, 15:00 UTC

At the final refresh approximately 13 minutes before tipoff, current score services still listed the game as scheduled/not started.

Therefore:

`GAME-STATE: PREGAME`

---

# Current standings / incentive state

After the first Window 4 games:

- Guinea: **4-3**
- Cape Verde: **3-4**

Cape Verde entered this game after losing 60-56 to Tunisia.

Guinea entered after losing 81-71 to South Sudan.

Both teams therefore have strong qualification urgency. This is not used as an automatic pace adjustment; it matters through late-game risk, rotations and foul/chasing states.

---

# Participant / roster audit

## Guinea current Window 4 pool

Current FIBA roster-tracker names include:

- Souleymane Boum Jr.
- Moussa Cisse
- Cheick Conde
- Mamadi Diakite
- Alpha Diallo
- Ibrahima Diallo
- Ahmed Doumbia
- Sekou Doumbouya
- Ousmane Drame
- Shannon Evans
- Ibrahima Kalil Fofana
- Kabinet Kaba
- Ousmane Araphan Kaba
- Tidjan Keita
- Aboubacar Soumpare
- Abdoulaye Sy

This is a stronger high-end talent pool than Guinea used in parts of the earlier qualifying campaign.

Important current creators/finishers include:

- Souleymane Boum Jr.
- Shannon Evans
- Sekou Doumbouya
- Mamadi Diakite
- Alpha Diallo

FIBA's current qualifier profile has Boum and Evans as Guinea's leading scorers and Ousmane Drame as a major rebounding contributor.

---

## Cape Verde current participant state

The initial Window 4 tracker listed:

- Ivan Almeida
- Joel Almeida
- William Brito
- Davide Buccilli
- Anderson Correia
- Anim Delgado
- Betinho Gomes
- Patrick Lima
- Ailton Lopes
- Kenneti Mendes
- Roesley Mendes
- Patrick Spencer
- Edy Tavares
- others

However, the participant state changed after that preliminary listing.

### Edy Tavares — current regime change

Contemporaneous reporting on 27–28 August records Tavares publicly withdrawing from this Window to remain with Real Madrid after a lengthy knee-injury layoff.

His quoted reason was to continue recovery/preseason work after approximately four months out.

FIBA's player profile also shows **no 2027 qualifier games recorded for Edy Tavares** in the current campaign.

Therefore this card does **not** model Tavares as an available/current Cape Verde rim protector.

That materially weakens:
- Cape Verde defensive rebounding;
- rim deterrence;
- interior finishing;
- defensive possession completion.

Cape Verde still retain:
- Ivan Almeida as the main creator/scorer;
- Marcus Santos Silva as a major rebound/inside presence;
- Joel Almeida;
- Patrick Spencer;
- Kenneti Mendes and other rotation players.

---

# Current FIBA team comparison

FIBA's current match page shows qualifier averages around:

| Metric | Cape Verde | Guinea |
|---|---:|---:|
| Points/game | 79.8 | 72.5 |
| Rebounds/game | 42.7 | 46.5 |
| Assists/game | 22.0 | 17.2 |
| 2PT FG | 50.0% | 44.9% |
| 3PT FG | 33.3% | 28.2% |
| FT | 68.1% | 71.8% |

Interpretation:

### Cape Verde positives
- better scoring average;
- higher two-point conversion;
- higher three-point conversion;
- more assists / better ball movement in the broad campaign.

### Guinea positives
- stronger rebounding volume;
- current roster has added high-level shot creation/size;
- more current qualifying wins;
- Cape Verde's Tavares absence removes the best possible answer to Guinea's physicality.

These differences support **Guinea winner**, but not automatically **Guinea -10.5**.

---

# Cape Verde qualifier results

Current seven-game sequence:

| Opponent | Result | Margin | Total |
|---|---:|---:|---:|
| Cameroon | W 82-77 | +5 | 159 |
| South Sudan | L 79-109 | -30 | 188 |
| Libya | W 85-74 | +11 | 159 |
| Cameroon | L 72-82 | -10 | 154 |
| South Sudan | L 63-83 | -20 | 146 |
| Libya | W 98-66 | +32 | 164 |
| Tunisia | L 56-60 | -4 | 116 |

### Against today's Cape Verde +10.5

Descriptively:
- cover: 5
- fail: 2

The two failures were the large South Sudan losses.

That does not establish a probability, but it shows that Cape Verde have frequently stayed inside a double-digit cushion against non-South-Sudan opponents.

### Against 150.5 total

- Over: 5
- Under: 2

This raw rate is not used without opponent/context adjustment. The two South Sudan games and two Libya games produce very different pace/efficiency environments from today's Guinea matchup.

---

# Guinea qualifier results

Current seven-game sequence:

| Opponent | Result | Margin | Total |
|---|---:|---:|---:|
| Nigeria | W 69-55 | +14 | 124 |
| Tunisia | W 66-57 | +9 | 123 |
| Rwanda | W 82-70 | +12 | 152 |
| Rwanda | W 89-63 | +26 | 152 |
| Nigeria | L 79-80 | -1 | 159 |
| Tunisia | L 50-61 | -11 | 111 |
| South Sudan | L 71-81 | -10 | 152 |

### Against Guinea -10.5

Descriptively, Guinea produced a 11+ margin in:
- 69-55 Nigeria
- 82-70 Rwanda
- 89-63 Rwanda

They did **not** create 11+ separation in four of seven.

### Against 150.5 total

- Over: 4
- Under: 3

The four Overs were:
- 152
- 152
- 159
- 152

Three of those were only 1.5 points above today's threshold.

That matters because a modest reduction in possessions or efficiency moves several historical "Overs" into today's Under branch.

---

# Latest-game process

## Cape Verde 56 — Tunisia 60

Cape Verde's Window 4 opener was a low-scoring, half-court game.

FIBA reporting highlighted:
- Cape Verde controlled early stages;
- a second-quarter scoring drought was costly;
- Ivan Almeida said the team lacked patience offensively;
- Tunisia were more disciplined;
- Cape Verde struggled with Omar Abada's foul-drawing/creation.

This result is not extrapolated mechanically.

The key takeaway is that Cape Verde can be dragged into a low-possession/low-efficiency game against a disciplined Group E opponent.

---

## Guinea 71 — South Sudan 81

Guinea fell behind by as many as 27 points before cutting the deficit to four.

FIBA described South Sudan's winning mechanism as:
- pace;
- spacing;
- outside shooting.

Guinea's comeback demonstrates a legitimate scoring/pressure branch, but the initial deficit also shows vulnerability when an opponent generates transition and perimeter efficiency.

Cape Verde are not South Sudan in pace/spacing quality, so that high-tempo loss is not directly transplanted into this matchup.

---

# Head-to-head audit

FIBA lists Cape Verde leading the historical series **6-1**.

Recent relevant meetings:

- 2023: Cape Verde 78-70 Guinea
- 2022: Guinea 48-65 Cape Verde

Older meetings also mostly favour Cape Verde.

This supports the idea that Cape Verde should not be treated as an ordinary 11+ point underdog.

However, the older H2H is materially downweighted because:
- Guinea's current roster is stronger;
- Cape Verde are without Edy Tavares;
- player and coaching regimes have changed.

It is therefore a supporting margin prior, not the main winner driver.

---

# Opponent-adjusted scoring sanity check

A simple descriptive scoring/allowance blend — used only as a sanity check — gives:

Cape Verde current average scoring:
**~79.8**

Guinea current average scoring:
**~72.5**

Cape Verde's seven opponents have scored roughly:
**~78.7 per game**

Guinea's seven opponents have scored roughly:
**~66.7 per game**

Simple blended central points:

- Cape Verde: `(79.8 + 66.7) / 2 ≈ 73.3`
- Guinea: `(72.5 + 78.7) / 2 ≈ 75.6`

Combined:
**~148.9**

This is not a fitted model.

It is used only to verify that a central score in the **high-140s** is coherent and that 150.5 is not a low line relative to the matchup.

---

# Market-state cross-check — excluded from internal probability

A current sportsbook snapshot shortly before tip showed approximately:

- Guinea -8.5
- Cape Verde +8.5
- total around 149

The user supplied:
- Cape Verde +10.5
- Guinea -10.5
- total 150.5

This market snapshot is used **only** to verify contract/state context.

It is not used as an internal sports probability or value model.

No expected-value claim is made.

---

# Joint qualitative score corridor

## Central Guinea win / Cape Verde cover / Under

Representative:
- Guinea 75-69
- Guinea 77-70
- Guinea 78-71

Mechanisms:
- Guinea wins the rebounding battle;
- Guinea's deeper current creator pool creates a modest efficiency edge;
- Cape Verde's ball movement/Ivan Almeida creation prevents offensive collapse;
- neither side generates a sustained transition avalanche.

Favours:
- Guinea winner
- Cape Verde +10.5
- Under 150.5

---

## Low-total physical branch

Representative:
- Guinea 72-65
- Guinea 74-66
- Guinea 75-67

Mechanisms:
- half-court possessions;
- physical defensive rebounding;
- Cape Verde repeat of its Tunisia offensive patience issues;
- Guinea's perimeter efficiency remains below elite levels.

Favours:
- Cape Verde +10.5 in most states
- Under 150.5
- Guinea winner

---

## Open competitive branch

Representative:
- Guinea 80-74
- Guinea 82-76
- Cape Verde 79-77

Mechanisms:
- Guinea's creators attack early;
- Cape Verde's higher historical shooting percentages persist;
- defensive rebounding generates transition;
- late fouling adds free throws.

Favours:
- Cape Verde +10.5
- Over 150.5

---

## Guinea separation branch

Representative:
- Guinea 82-68
- Guinea 84-70
- Guinea 86-72

Mechanisms:
- Cape Verde loses the rebounding battle badly without Tavares;
- Ivan Almeida is forced into difficult creation;
- Guinea's Boum/Evans/Doumbouya/Diakite talent creates repeated high-value shots;
- late-game chasing expands the margin.

Favours:
- Guinea -10.5
- total can be either side depending Cape Verde contribution.

This is credible but is not the central branch.

---

## Cape Verde upset branch

Representative:
- Cape Verde 76-73
- Cape Verde 78-75

Mechanisms:
- perimeter shooting/ball movement outperforms Guinea;
- Ivan Almeida controls the game;
- Cape Verde limits turnovers;
- Guinea's 3PT shooting remains inefficient.

Favours:
- Cape Verde +10.5
- winner upset
- total around the supplied boundary.

---

# Strongest kill paths

## Cape Verde +10.5

Guinea dominate the glass and paint, Cape Verde's half-court creation stalls without Tavares' interior gravity/rim presence, and Guinea's deeper creator group opens a 12–18 point lead that survives garbage-time compression.

## Under 150.5

Both teams shoot above current three-point baselines, rebounding creates repeated transition possessions, and late fouling pushes a close game from the mid-140s through 151+.

## Over 150.5

The game resembles Cape Verde-Tunisia or Guinea's lower-tempo wins, with disciplined half-court defence and enough shooting inefficiency to remain in the 140s.

## Guinea -10.5

Cape Verde's experienced guards/wings remain competitive and the game stays within two or three possessions into the final minutes.

---

# Final ranking

| Rank | Candidate | Pick | Verdict | Evidence | Probability |
|---:|---|---|---|---|---|
| **1** | `P-134-C01` | **Cape Verde +10.5** | `LEAN` | `MEDIUM-HIGH` | `NOT_GENERATED` |
| **2** | `P-134-C04` | **Under 150.5 Points** | `LEAN` | `MEDIUM` | `NOT_GENERATED` |
| **3** | `P-134-C03` | **Over 150.5 Points** | `FORCED RANK` | `MEDIUM` | `NOT_GENERATED` |
| **4** | `P-134-C02` | **Guinea -10.5** | `AVOID` | `MEDIUM-HIGH` | `NOT_GENERATED` |

---

# Detailed ranking rationale

## #1 — Cape Verde +10.5

This is the most robust supplied contract because Cape Verde do not need to win.

They can:
- win outright;
- lose by 1–10;

and still cash the handicap.

Evidence:
- Cape Verde have stayed inside this threshold in 5 of 7 current qualifier games.
- Guinea have created an 11+ margin in only 3 of 7.
- historical H2H strongly favours Cape Verde staying competitive.
- Cape Verde still possess experienced creators and better broad shooting/assist numbers.

Counterweight:
- Edy Tavares is absent;
- Guinea's current Window 4 roster is more talented than earlier versions;
- Guinea's rebounding advantage creates a real blowout branch.

**Verdict:** `LEAN`  
**Evidence:** `MEDIUM-HIGH`

---

## #2 — Under 150.5

The line sits just above the current matchup's blended scoring corridor.

Support:
- simple offense/defense blend ≈ 149;
- Cape Verde just played a 116-point game;
- Guinea's qualifier profile includes several very low totals;
- Guinea's 152-point Overs repeatedly sat only 1.5 points above today's line;
- both teams can win through half-court defence rather than needing pace.

Counterweight:
- Cape Verde's broad qualifier scoring average is high;
- the combined raw records contain several 150+ games;
- late fouling and transition can move a 145–149 game through the line quickly.

**Verdict:** `LEAN`

---

## #3 — Over 150.5

The Over remains very credible.

Support:
- Cape Verde's broad qualifier scoring average is nearly 80;
- 5 of Cape Verde's 7 qualifier games exceeded 150.5;
- 4 of Guinea's 7 exceeded 150.5;
- Cape Verde shoot more efficiently than Guinea in the broad FIBA comparison;
- both teams have strong qualification incentive and late-foul risk.

It remains below Under because many of the apparent Overs are opponent/environment driven and Guinea's current defensive/half-court profile lowers the central score.

**Verdict:** `FORCED RANK`

---

## #4 — Guinea -10.5

Guinea are the preferred outright winner.

But requiring **11+** is a materially different event.

Failure states include:
- any Cape Verde win;
- a draw;
- Guinea wins by 1–10.

The current evidence makes a Guinea win by approximately 5–9 more coherent than a routine double-digit blowout.

**Verdict:** `AVOID`

`AVOID` is evidence-relative and is not a negative expected-value claim.

---

# Potential game winner

## Guinea — LEAN

Supporting mechanisms:
- better current record;
- stronger rebound profile;
- current Window 4 talent additions;
- Cape Verde's Edy Tavares absence;
- Cape Verde enter off a 56-point offensive performance;
- Guinea's current roster has multiple independent shot creators.

Strongest failure path:
- Cape Verde's experienced Almeida-led perimeter group controls turnovers and tempo, Guinea's three-point inefficiency persists, and Cape Verde's ball movement produces enough efficient looks to win a close game.

### Coherence statement

**Guinea winner** and **Cape Verde +10.5** are fully compatible.

The central tree contains a large:

`GUINEA WINS BY 1–10`

branch.

---

# Final forecast card

1. **Cape Verde +10.5**
2. **Combined Total Under 150.5 Points**
3. **Combined Total Over 150.5 Points**
4. **Guinea -10.5**

**Potential game winner:** **Guinea**

**GAME-STATE:** `PREGAME`

**Probability state:**  
`NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value state:**  
`NO VALUE DETERMINABLE`

---

# Source record

## Sports Research / Google Drive
- `RULES_BASKETBALL.md`
- `RULES_GENERAL.md`
- active learning/model/evaluation controls

## Official FIBA
- Cape Verde vs Guinea official game page
- FIBA African Qualifiers official schedule
- FIBA team comparison
- Cape Verde team profile
- Guinea team profile
- Window 4 roster tracker
- final-roster announcement
- Cape Verde–Tunisia postgame report
- Guinea–South Sudan postgame report
- first-round official results/game pages
- official standings / qualification format

## Current participant cross-check
- contemporaneous reporting containing Edy Tavares' own withdrawal statement
- FIBA Edy Tavares profile showing no 2027 qualifier appearances

## Market state
- current sportsbook snapshot used only to verify the contract environment, not as internal prediction evidence

---

# Logging confirmation

**Canonical ID:** `P-134`

**Issued view:** `V01`

**Google Drive modified:** `NO`

**Delivery mode:** `DOWNLOADABLE MARKDOWN FILE`

**Retrospective:** `NOT INCLUDED`

**Important:** This file freezes the pregame evidence state approximately 13 minutes before the scheduled 01:00 Melbourne tip. If the game has started when this file is opened, it should not be reinterpreted as a live forecast.

# P-135 — Unión de Santa Fe vs Sarmiento — Torneo Clausura 2026

## State warning

**FINAL STATE:** `START CROSSED — LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`

The current official Unión match notice and current AFA referee assignment both scheduled the match for **19:00 Argentina time on 28 August 2026**, equivalent to **08:00 Australia/Melbourne on 29 August 2026**. That scheduled start passed during research.

At the first post-start refresh, no trustworthy source exposed both a verified live score and match clock. Some secondary feeds still carried conflicting 21:15 / 00:15 UTC schedule entries.

Under the active Sports Research state-integrity rules, the rankings below are preserved as a **frozen pre-start evidence view only** and are **not actionable as live picks**.

---

## Executive pre-start ranking

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Sarmiento Team Total Over 0.5 Goals** | `FORCED RANK` | `MEDIUM-LOW — lineup/state cap` |
| **2** | **1st Half Goals Over 0.5** | `FORCED RANK` | `MEDIUM-LOW — lineup/state cap` |
| **3** | **Sarmiento or Draw — Double Chance X2** | `FORCED RANK` | `MEDIUM-LOW — official XI not verified` |
| **4** | **Total Corners Under 10.5 — research threshold** | `FORCED RANK` | `MEDIUM-LOW — derivative/provider cap` |
| **5** | **Combined Total Goals Over 2.5** | `FORCED RANK` | `MEDIUM-LOW — participant/state cap` |

**Potential game winner:** **Sarmiento — FORCED WINNER / LOW CONFIDENCE**

Lower-ranked supplied branches:
- 1st Half Under 0.5
- Full Match Under 2.5

---

## Record metadata

| Field | Recorded value |
|---|---|
| Canonical ID | `P-135` |
| Sport | Soccer |
| Competition | Argentina Liga Profesional — Torneo Clausura 2026 |
| Round | Fecha 7 |
| Fixture type | Interzonal |
| Event | Unión de Santa Fe vs Sarmiento |
| Venue | Estadio 15 de Abril, Santa Fe |
| Official/current scheduled start | 2026-08-28 19:00 Argentina |
| Melbourne equivalent | 2026-08-29 08:00 AEST |
| Referee | Pablo Echavarría |
| VAR | Hernán Mastrángelo |
| Method | `MDS-2026.08.28-v2.4` |
| Sport module | `RULES_SOCCER.md` |
| Numerical status | `NO SOCCER MODEL FIT / VALIDATED` |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Google Drive | `READ-ONLY REFERENCE — NOT MODIFIED` |
| Delivery | `DOWNLOADABLE MARKDOWN FILE` |
| Retrospective | `NOT INCLUDED` |

---

# Framework controls applied

The active soccer rules require:

- exact event, competition and regulation identity;
- current starting XI and goalkeeper status for participant-dependent side or player claims;
- winner and goal-total markets to come from one coherent goal process;
- corners to come from a separate corner-event process;
- current form/regime to be reconciled against older H2H;
- red-card and score-state branches to remain explicit;
- exact provider definition for corners;
- verified score and clock before any live forecast after kickoff.

Because the official starting XIs and goalkeepers were not independently verified from an official field-owner release before start crossing, participant-sensitive rows remain capped.

---

# Frozen candidate universe

**Decision-set ID:** `DS-P-135-V01`

User-supplied market families:
- 1H Over/Under 0.5 goals
- Full Game Over/Under 2.5 goals

Analyst-added candidates frozen before ranking:
- Sarmiento Team Total Over 0.5 goals
- Sarmiento or Draw — Double Chance X2
- Total Corners Under 10.5 — research threshold

No player prop was added because the official XI could not be verified.

---

# Current competition form

## Unión — first six Clausura matches

| Match | Result | Total |
|---|---:|---:|
| Platense vs Unión | 2-2 | 4 |
| Unión vs Lanús | 2-1 | 3 |
| Gimnasia Mendoza vs Unión | 2-0 | 2 |
| Unión vs Central Córdoba | 1-2 | 3 |
| San Lorenzo vs Unión | 1-0 | 1 |
| Aldosivi vs Unión | 1-3 | 4 |

Record: **2-1-3**

Goals:
- For: **8**
- Against: **9**

Over 2.5:
- **4 of 6**

Unión enter after a 3-1 win at Aldosivi, but had lost the previous two.

### Material Unión availability notes

Current reporting identifies:
- Julián Palacios — suspended after a red card in the previous round
- Lautaro Vargas — knee injury
- Federico Gomes Gerth — long-term knee injury
- Ignacio Malcorra — returning from a muscle injury / squad-status uncertainty in current reports

No named-player effect is converted into a numerical coefficient.

---

## Sarmiento — first six Clausura matches

| Match | Result | Total |
|---|---:|---:|
| Sarmiento vs Argentinos Juniors | 2-3 | 5 |
| Banfield vs Sarmiento | 3-2 | 5 |
| Sarmiento vs Independiente Rivadavia | 2-1 | 3 |
| Atlético Tucumán vs Sarmiento | 1-2 | 3 |
| Sarmiento vs Huracán | 2-0 | 2 |
| Sarmiento vs Estudiantes | 2-0 | 2 |

Record: **4-0-2**

Goals:
- For: **12**
- Against: **8**

Over 2.5:
- **4 of 6**

Most important current-regime fact:

**Sarmiento scored exactly two goals in all six Clausura matches.**

This is not treated as a self-validating streak. The mechanism is more important:
- repeated multi-chance attacking output;
- Junior Marabel has been the main high-xG scorer;
- a stable two-forward structure;
- improved defensive control during the four-match winning run;
- enough transition/box-entry quality to score multiple times across different game states.

Latest four:
- 2-1
- 2-1
- 2-0
- 2-0

That is why **Sarmiento Team Total Over 0.5** ranks first.

---

# Table / regime comparison

Sarmiento enter:
- 2nd in Zone B
- 12 points
- four consecutive wins

Unión enter:
- 7 points
- 2-1-3
- coming off a rebound 3-1 win

### Baseline branch
Unión's home field and historical competitiveness keep the match close.

### Current-regime branch
Sarmiento's four-match winning run is supported by repeated two-goal output and improved defence, while Unión remain inconsistent.

The current regime is weighted above stale reputation, but not strongly enough to eliminate the Unión home-win path.

---

# Probable lineups — secondary only

## Unión probable XI
Matías Mansilla; Juan De Dios Pintado, Maizon Rodríguez, Juan Pablo Ludueña, Lucas Ayala; Brahian Cuello, Emilio Giaccone, Lucas Menossi, Mauro Luna Diale; Cristian Tarragona, Marcelo Estigarribia.

## Sarmiento probable XI
Thyago Ayala; Santiago Salle, Renzo Orihuela, Juan Manuel Insaurralde, Lucas Suárez; Julián Contrera, Mauricio Martínez, Cristian Zabala, Julián Mavilla; Junior Marabel, Jonathan Herrera.

These were repeated across current Argentine media but were **not** upgraded to `CONFIRMED_OFFICIAL`.

Participant state:
`SECONDARY_ONLY / NOT OFFICIALLY VERIFIED AT CUTOFF`

---

# First-half goal process

Directly recoverable recent states:

### Unión
- vs Central Córdoba: **1-0 HT**
- at Gimnasia Mendoza: **0-1 HT**
- at Platense: **0-1 HT**
- vs Lanús: **0-0 HT**
- at San Lorenzo: **0-0 HT**

At least **3 of 5** directly recoverable recent league first halves contained a goal.

### Sarmiento
- vs Huracán: **1-0 HT**
- vs Estudiantes: **1-0 HT**
- February 2026 H2H vs Unión: **0-2 HT**

### 1H Over 0.5 mechanism
`Sarmiento's current attacking start + Unión's recent first-half concession risk + both teams' current multi-goal environments -> meaningful early-goal branch`

Strongest kill path:
both teams begin conservatively, prioritising transition prevention and field position.

Therefore:
**1H Over 0.5 = Rank #2**

---

# Full-game goal process

## Over 2.5 support
- Unión: **4/6**
- Sarmiento: **4/6**
- combined descriptive sample: **8/12**
- Sarmiento: 12 goals in six
- Unión: 9 conceded in six
- February 2026 H2H: **Sarmiento 1-3 Unión**

## Under 2.5 support
- Sarmiento's last two were both **2-0**
- Unión recently had **1-0** and **0-2**
- historical H2H average is roughly **2.1 goals**
- a leading side can reduce risk and compress late attacking exposure

### Goal corridor

Lower:
- 1-0
- 1-1
- 2-0

Central:
- 1-2
- 2-1

Upper:
- 2-2
- 1-3
- 3-1

Current-regime evidence slightly favours 3+ goals, but not strongly enough for high confidence.

---

# Side / winner process

## Why Sarmiento X2 ranks above the outright winner

Sarmiento:
- four straight wins
- 2 goals in every Clausura game
- two consecutive clean sheets
- second in Zone B

Unión:
- 2-1-3
- rebound win last round, but inconsistent overall
- suspended Julián Palacios
- current rebuild/lineup uncertainty

Strongest contrary path:
Unión's home field, Tarragona/Estigarribia finishing and the momentum from the 3-1 Aldosivi win recreate the February 3-1 H2H.

Therefore:
**Sarmiento or Draw X2 = Rank #3**

---

# Corner process

The active soccer framework prohibits using goals or possession as substitutes for corner evidence.

## Direct H2H corner evidence

Across 13 recoverable H2Hs:
- average total corners: approximately **10.0**
- Over 9.5: approximately **54%**

Recent H2H:
- Feb 2026: **9**
- Sep 2024: **4**
- Mar 2024: **11**
- Oct 2023: **10**
- May 2023: **18**
- Sep 2022: **13**

The distribution is wide.

## Current-rate corroboration

Current secondary statistical summaries place approximately:
- Unión corners for: **4.0–4.6**
- Unión corners against: **4.0–4.8**
- Sarmiento corners for: **3.9–4.1**
- Sarmiento corners against: **5.1–5.3**

A simple cross-team blend lands around the high-8s/low-9s total-corner range.

That makes **Under 10.5** the preferred research threshold.

### Missing corner layers
Not fully verified:
- crosses
- blocked crosses
- end-line entries
- clearances
- exact tactical width
- confirmed current fullbacks/wingers
- exact settlement provider/definition

Therefore:
**Total Corners Under 10.5 = FORCED RANK / MEDIUM-LOW**

---

# H2H audit

13 recoverable meetings:
- Sarmiento wins: 5
- draws: 2
- Unión wins: 6
- average goals: ~2.1
- average corners: ~10.0

Latest:
**Sarmiento 1-3 Unión — 26 February 2026**
- HT: 0-2
- corners: 7-2
- total corners: 9

The current-year H2H matters, but it does not override:
- Sarmiento's four-match winning run;
- current two-goal-per-match Clausura output;
- Unión's changed personnel/availability state.

---

# Scenario tree

## Sarmiento competitive / scores
Representative:
- 1-1
- 1-2
- 2-2

Helps:
- Sarmiento TT O0.5
- 1H O0.5 in early-goal branches
- Sarmiento X2
- O2.5 in 1-2 / 2-2

## Sarmiento control
Representative:
- 0-1
- 0-2

Helps:
- Sarmiento TT O0.5
- Sarmiento X2
- corner Under remains live
- FT Under 2.5 threatens Rank #5

## Unión rebound
Representative:
- 2-1
- 3-1

Helps:
- 1H Over
- Over 2.5
- Sarmiento TT O0.5 may still survive

Kills:
- Sarmiento X2

## Closed tactical branch
Representative:
- 0-0
- 1-0
- 1-1

Helps:
- Under 2.5
- Corners Under 10.5

Kills:
- 1H Over in many variants
- Sarmiento TT O0.5 in a 1-0
- Over 2.5

---

# Final pre-start ranking

| Rank | Candidate | Pick | Verdict | Evidence | Probability |
|---:|---|---|---|---|---|
| **1** | `P-135-C01` | **Sarmiento Team Total Over 0.5 Goals** | `FORCED RANK` | `MEDIUM-LOW` | `NOT_GENERATED` |
| **2** | `P-135-C02` | **1st Half Over 0.5 Goals** | `FORCED RANK` | `MEDIUM-LOW` | `NOT_GENERATED` |
| **3** | `P-135-C03` | **Sarmiento or Draw — X2** | `FORCED RANK` | `MEDIUM-LOW` | `NOT_GENERATED` |
| **4** | `P-135-C04` | **Total Corners Under 10.5** | `FORCED RANK` | `MEDIUM-LOW` | `NOT_GENERATED` |
| **5** | `P-135-C05` | **Combined Total Over 2.5 Goals** | `FORCED RANK` | `MEDIUM-LOW` | `NOT_GENERATED` |

---

# Potential game winner

## Sarmiento — `FORCED WINNER / LOW CONFIDENCE`

Why:
- four consecutive wins
- second in Zone B
- two goals in every Clausura match
- two straight clean sheets
- current form stronger than Unión's
- Unión missing suspended Julián Palacios

Why confidence remains low:
- official XI/keeper verification incomplete
- Unión are at home
- Unión won the February H2H 3-1
- Unión enter off a 3-1 away win

---

# State-integrity conclusion

The scheduled **19:00 Argentina / 08:00 Melbourne** kickoff passed during research.

At the post-start refresh:
- no current source provided a trustworthy exact score and clock together;
- secondary schedule sources still disagreed with the current official 19:00 schedule.

Therefore:

**`LIVE STATE NOT VERIFIED — NO ACTIONABLE LIVE FORECAST`**

The five rankings above are the frozen pre-start evidence view only.

They should not be transferred to live markets without a verified:
- score
- match clock
- red-card state
- substitutions
- current shot/corner state

---

# Source record

## Google Drive framework
- `RULES_SOCCER.md`
- `RULES_GENERAL.md`
- active learning/model/evaluation specifications

## Official/current event sources
- Club Atlético Unión official match notice
- Asociación del Fútbol Argentino current referee assignment
- Liga Profesional current schedule
- TyC Sports current match preview
- current Argentine team/availability reporting

## Statistical support
- FotMob / Opta-powered current form and xG context
- TotalCorner direct H2H and corner-event records
- secondary aggregated corner-rate sources used only as corroboration

## Limitations
- official starting XIs/keepers were not recovered before start crossing
- corner provider/settlement definition not supplied
- exact live score/clock not verified after scheduled kickoff
- no fitted/validated soccer model exists

---

# Logging confirmation

**Canonical ID:** `P-135`  
**Issued view:** `V01`  
**Google Drive modified:** `NO`  
**Delivery:** `DOWNLOADABLE MARKDOWN FILE`  
**Probability:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value:** `NO VALUE DETERMINABLE`  
**Retrospective:** `NOT INCLUDED`  
**Current disposition:** `START CROSSED — LIVE STATE NOT VERIFIED — PRE-START RANKING PRESERVED FOR REFERENCE ONLY`

# P-136 — James Duckworth vs Arthur Fery — ATP Winston-Salem Open 2026 Semifinal

## Executive forecast

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Total Games Over 22.5** | **LEAN** | **MEDIUM-HIGH** |
| **2** | **James Duckworth +1.5 Games** | **LEAN** | **MEDIUM** |
| **3** | **Arthur Fery -1.5 Games** | **FORCED RANK** | **MEDIUM** |
| **4** | **Total Games Under 22.5** | **AVOID** | **MEDIUM-HIGH** |

**Potential match winner:** **Arthur Fery — LEAN**

### Central interpretation

Fery is the preferred outright winner because his current hard-court return profile is stronger, his 2026 level is materially higher, and he has the better recovery situation entering the semifinal.

However, Duckworth has been serving extremely well in Winston-Salem, and the most recent head-to-head — only two weeks ago in Cincinnati — ended:

**Fery 6-4, 2-6, 7-6(4)**

Fery won the match, but Duckworth actually won **16 total games to Fery's 15**.

That creates a coherent central state in which:
- **Fery wins the match**
- **Duckworth +1.5 still covers**
- **Over 22.5 wins**

Representative central score shapes:
- Fery 7-6, 4-6, 6-4
- Fery 6-4, 3-6, 7-6
- Fery 7-5, 4-6, 6-4

---

## Record metadata

| Field | Recorded value |
|---|---|
| Canonical ID | `P-136` |
| Sport | Tennis |
| Competition | ATP Winston-Salem Open 2026 |
| Level | ATP 250 |
| Round | Singles Semifinal |
| Event | James Duckworth vs Arthur Fery |
| Court | Stadium Court |
| Surface | Outdoor hard |
| Format | Best-of-three sets |
| Official scheduled start | Not before 6:30 PM EDT, Friday 28 Aug 2026 |
| Melbourne equivalent | Not before 8:30 AM AEST, Saturday 29 Aug 2026 |
| Final research refresh | 2026-08-29 08:05 AEST |
| GAME-STATE | `PREGAME` |
| Duckworth ranking | approximately ATP 79–86 depending live/static source |
| Fery ranking | ATP 37; live ranking at least mid-30s |
| H2H | Duckworth leads 2-1 |
| Method | `MDS-2026.08.28-v2.4` |
| Sport module | `RULES_TENNIS.md` |
| Numerical status | `NO TENNIS TARGET/SOURCE CARD, DATASET OR MODEL APPROVED OR FIT` |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Google Drive | `READ-ONLY REFERENCE — NOT MODIFIED` |
| Retrospective | `NOT INCLUDED` |

---

# Framework controls applied

The active Sports Research tennis module requires:

- exact competition, round, surface, format and participant identity;
- retirement/walkover terms treated as contract-specific;
- surface-specific serve/return form separated from ranking/reputation;
- first/second serve, hold/break and return pressure used as process evidence;
- head-to-head continuity audited for surface, level and current player regime;
- one coherent match tree for winner, game handicap and total games;
- explicit straight-set and three-set branches;
- qualifying/workload/recovery treated mechanistically rather than as an automatic fatigue penalty;
- no published numerical probability because no approved/fitted tennis model exists.

---

# Frozen decision set

**Decision-set ID:** `DS-P-136-V01`

| Candidate ID | Exact contract |
|---|---|
| `P-136-C01` | James Duckworth +1.5 Games |
| `P-136-C02` | Arthur Fery -1.5 Games |
| `P-136-C03` | Total Games Over 22.5 |
| `P-136-C04` | Total Games Under 22.5 |

### Contract geometry

**Duckworth +1.5**
- wins if Duckworth wins the match;
- also wins if Fery wins but Duckworth finishes no more than one game behind in total games.

**Fery -1.5**
- requires Fery to win the match and finish at least two total games ahead.

The two handicap rows are exact half-game complements.

**Over 22.5**
- wins at 23+ total games.

**Under 22.5**
- wins at 22 or fewer.

No push exists.

### Retirement / walkover rules

No operator was supplied.

Therefore exact retirement settlement is:

`UNKNOWN_DEFINITION`

No expected-value or price claim is made.

---

# Official event and state verification

The official Winston-Salem Open schedule lists:

**James Duckworth vs Arthur Fery (4)**  
Singles semifinal  
Stadium Court  
**Not Before 6:30 PM EDT on 28 August 2026**

At 08:05 AEST / 18:05 EDT, the match remained pre-start and current match feeds continued to list it as upcoming.

Therefore:

`GAME-STATE: PREGAME`

---

# Head-to-head audit

Current H2H:

**Duckworth 2-1 Fery**

All three meetings were on hard courts.

| Date | Event | Winner | Score | Total games | Duckworth +1.5 |
|---|---|---|---|---:|---|
| 2024-04-10 | Busan Challenger | Duckworth | 4-6, 6-1, 6-4 | 27 | WIN |
| 2024-05-16 | Taipei Challenger | Duckworth | 7-5, 7-5 | 24 | WIN |
| 2026-08-15 | Cincinnati ATP 1000 | Fery | 6-4, 2-6, 7-6(4) | 31 | WIN |

### Direct descriptive results

- Over 22.5: **3/3**
- Duckworth +1.5: **3/3**
- Fery -1.5: **0/3**
- Under 22.5: **0/3**

These are not used as raw probabilities.

### Continuity weighting

The two 2024 meetings are downweighted because Fery was then ranked around the mid-200s and was in a materially different development/fitness regime.

The **Cincinnati meeting from two weeks ago** receives much greater weight because:
- same outdoor-hard North American swing;
- both players in essentially current technical regimes;
- ATP main-tour level;
- no major current injury change identified.

That current meeting strongly supports a **close-match / long-match branch**.

---

# Most recent H2H — Cincinnati 2026

Fery won:

**6-4, 2-6, 7-6(4)**

Match stats:

| Metric | Fery | Duckworth |
|---|---:|---:|
| Aces | 9 | 6 |
| Double faults | 3 | 4 |
| First serve in | 51% | 51% |
| First-serve points won | 73% | **82%** |
| Second-serve points won | 59% | 58% |
| Service games held | 12/15 | **13/15** |
| Breaks converted | 2/3 | **3/6** |

Important interpretation:

Fery won the higher-leverage final-set tiebreak, but Duckworth:
- held more often;
- broke more often;
- won one more total game.

This is exactly why **Fery winner** can coexist with **Duckworth +1.5**.

---

# Current hard-court process

## Arthur Fery — recent hard split

Tennis Abstract recent hard-court profile:

- record: approximately **33-12**
- hold rate: approximately **81.2%**
- service points won: approximately **65.2%**
- break rate: approximately **29.0%**
- return points won: approximately **41.1%**
- dominance ratio: approximately **1.18**

Fery's key advantage is **return pressure**.

His hold rate is strong but not elite; the differential comes from creating substantially more return opportunities than Duckworth across the recent hard sample.

---

## James Duckworth — recent hard split

Tennis Abstract recent hard-court profile:

- record: approximately **28-22**
- hold rate: approximately **83.3%**
- service points won: approximately **66.4%**
- break rate: approximately **19.9%**
- return points won: approximately **35.6%**
- dominance ratio: approximately **1.06**

Duckworth's profile is more serve-led:
- stronger ace rate;
- slightly higher hold baseline;
- weaker return pressure.

That structure naturally creates:
- 6-4 sets;
- 7-5 sets;
- tiebreaks;
- close overall game margins.

This supports the Over and Duckworth +1.5.

---

# Winston-Salem current tournament

## Duckworth

| Round | Opponent | Score | Total games | Game margin |
|---|---|---|---:|---:|
| R64 | Quinn Vandecasteele | 6-2, 6-1 | 15 | +9 |
| R32 | Mariano Navone | 6-3, 7-6(5) | 22 | +4 |
| R16 | Lorenzo Sonego | 7-5, 6-3 | 21 | +5 |
| QF | Fábián Marozsán | 6-7(4), 6-2, 6-4 | 31 | +5 |

Duckworth is **4-0** this week.

The first three matches were straight-set control wins. The quarterfinal became a full three-set test.

### QF process vs Marozsán

Duckworth:
- 8 aces
- 8 double faults
- only 48% first serves in
- 76% first-serve points won
- 59% second-serve points won
- held 12 of 15 service games
- broke 6 of 15 Marozsán service games

The first-serve percentage was poor, but he still created significant return pressure and recovered after losing the first set.

---

## Fery

| Round | Opponent | Score | Total games | Game margin |
|---|---|---|---:|---:|
| R32 | Cruz Hewitt | 6-1, 7-5 | 19 | +7 |
| R16 | Mees Röttgering | 6-3, 6-3 | 18 | +6 |
| QF | Aleksandar Kovacevic | 3-6, 7-5, 6-3 | 30 | +2 |

Fery is **3-0** this week.

### QF process vs Kovacevic

Fery:
- 4 aces
- **0 double faults**
- 56% first serves in
- **82% first-serve points won**
- **62% second-serve points won**
- held **14 of 15** service games
- broke 2 of 15 return games

This is an excellent serving performance and shows Fery can win even when return opportunities are scarce.

---

# Current form / ranking regime

## Fery

Fery's 2026 rise is substantial:
- current ranking around No. 37;
- live ranking at least around No. 35 after reaching this semifinal;
- Wimbledon semifinalist;
- recent Cincinnati win over Duckworth;
- current hard-court results substantially stronger than his 2024 Challenger-level profile.

That means the old 2024 Duckworth H2H wins cannot simply be treated as equal evidence to the current Cincinnati meeting.

## Duckworth

Duckworth:
- remains an experienced hard-court player;
- has reached his fourth ATP Tour semifinal;
- is in his best ATP-level tournament run since 2025;
- has beaten Navone, Sonego and Marozsán this week;
- is producing a materially better current tournament level than his broad 2026 ranking/record alone suggests.

Therefore the correct regime mixture is:

**Fery stronger broad/current player + Duckworth unusually strong current tournament form**

This widens the distribution and supports a close-match tree.

---

# Recovery / workload

## Fery quarterfinal
- beat Kovacevic 3-6, 7-5, 6-3
- duration approximately **2h08**
- played earlier in the evening

## Duckworth quarterfinal
- beat Marozsán 6-7, 6-2, 6-4
- duration approximately **2h23**
- finished close to **1:00 AM local time**

Duckworth is also 34 years old versus Fery's 24.

### Mechanistic implication

This gives Fery a real recovery edge:
- later Duckworth finish;
- longer match;
- older player;
- one additional tournament match played this week.

It supports:
- Fery winner;
- Fery separation / straight-set tail.

It does **not** automatically imply fatigue failure:
Duckworth has shown no current injury/medical problem and has repeatedly recovered through long professional schedules.

This is the strongest kill path against Duckworth +1.5 and Over 22.5.

---

# Match tree

## Branch A — long, close Fery win

Representative:
- Fery 7-6, 4-6, 6-4
- Fery 6-4, 3-6, 7-6
- Fery 7-5, 4-6, 6-4

Favours:
- **Over 22.5**
- **Duckworth +1.5** in many variants
- Fery winner

This is the central branch.

---

## Branch B — Fery straight-set separation

Representative:
- Fery 6-4, 6-3
- Fery 7-5, 6-3
- Fery 6-3, 6-4

Mechanism:
- Fery's return advantage converts into repeated break pressure;
- Duckworth's short recovery reduces first-serve quality;
- Fery protects his own serve at the level shown vs Kovacevic.

Favours:
- Fery -1.5
- Under 22.5 in most variants

This is the strongest contrary path to ranks #1 and #2.

---

## Branch C — tight Fery straight-set win

Representative:
- Fery 7-6, 6-4 = 23
- Fery 7-5, 7-5 = 24
- Fery 7-6, 7-6 = 26

Favours:
- Over 22.5
- Fery -1.5 in most variants
- Duckworth +1.5 only if the total-game margin stays within one

This branch helps explain why the Over can win even without a third set.

---

## Branch D — Duckworth upset

Representative:
- Duckworth 7-5, 4-6, 6-4
- Duckworth 7-6, 6-4
- Duckworth 6-4, 3-6, 7-6

Mechanism:
- Duckworth continues to hold at ~85%+;
- first serve controls Fery's return edge;
- Fery's break conversion remains limited;
- Duckworth's experience wins pressure points.

Favours:
- Duckworth +1.5
- Over 22.5 in most three-set/tight variants

---

# Why Over 22.5 ranks #1

### Direct matchup support
All three H2Hs:
- 27 games
- 24 games
- 31 games

All cleared 22.5.

### Current-regime support
The most relevant H2H was only two weeks ago:
- three sets
- deciding tiebreak
- 31 games

### Serve/return structure
Both recent hard hold rates are above 81%.

Duckworth is serve-led and Fery is not such a dominant returner that a double-break-per-set straight-set match should be treated as the default.

### Current tournament
Both players' quarterfinals went three sets:
- Duckworth 31 games
- Fery 30 games

### Tight straight-set rescue
Scores such as:
- 7-6, 6-4
- 7-5, 7-5
- 7-6, 7-6

all clear 22.5.

### Kill path
Fery's recovery advantage plus stronger return rate produces a cleaner 6-4, 6-3 or 6-3, 6-4 win.

**Verdict:** `LEAN`  
**Evidence:** `MEDIUM-HIGH`

---

# Why Duckworth +1.5 ranks #2

Direct H2H descriptive record:
- **3/3 covers**

Most importantly, Duckworth covered +1.5 in the **current-regime Cincinnati loss**, because he won one more total game despite losing the match.

The handicap also wins automatically on any Duckworth upset.

This line fits the central close-Fery-win branch particularly well.

### Kill path
Fery wins in straights or produces a 3+ net game margin in three sets through superior return pressure and Duckworth recovery decline.

**Verdict:** `LEAN`  
**Evidence:** `MEDIUM`

---

# Why Fery -1.5 ranks #3

Fery is the preferred match winner.

Support:
- much stronger 2026 ranking/current level;
- stronger recent hard return profile;
- 29% recent hard break rate vs Duckworth around 20%;
- won their Cincinnati meeting;
- better recovery after the quarterfinal;
- 10-year age advantage.

But the exact market asks for more than winning.

Fery must finish **2+ games ahead**.

That has failed in all three prior H2Hs.

The current Cincinnati win is especially important because it shows the exact winner/handicap split:
**Fery won, Duckworth won the game count.**

**Verdict:** `FORCED RANK`  
**Evidence:** `MEDIUM`

---

# Why Under 22.5 ranks #4

There is a real Under branch because most of each player's earlier Winston-Salem matches were efficient straight-set wins.

Duckworth tournament totals:
- 15
- 22
- 21
- 31

Fery:
- 19
- 18
- 30

So the current tournament itself contains many Under outcomes.

However, those Under matches mostly occurred when one player was clearly controlling a weaker/different opponent.

Against each other:
- all three meetings have exceeded 22.5;
- the current-regime meeting went 31;
- the winner is not projected to dominate sufficiently for a short straight-set result to be the central branch.

**Verdict:** `AVOID`  
**Evidence:** `MEDIUM-HIGH`

`AVOID` is evidence-relative and is not a negative expected-value claim.

---

# Potential game winner

## Arthur Fery — `LEAN`

Why:
- ranking/current level advantage;
- stronger recent hard-court dominance ratio;
- substantially better return and break profile;
- won the most recent H2H;
- reached the Wimbledon semifinal this year;
- excellent quarterfinal service numbers;
- more recovery time than Duckworth;
- younger by approximately 10 years.

Strongest failure path:
Duckworth's current Winston-Salem serving level persists, Fery cannot create enough break chances, and Duckworth's experience in close/tiebreak sets decides the match.

### Coherence statement

**Fery winner** and **Duckworth +1.5 games** are fully coherent.

The most recent H2H produced exactly that combination.

---

# Final forecast card

1. **Total Games Over 22.5**
2. **James Duckworth +1.5 Games**
3. **Arthur Fery -1.5 Games**
4. **Total Games Under 22.5**

**Potential match winner:** **Arthur Fery**

**GAME-STATE:** `PREGAME`

**Probability state:**  
`NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`

**Value state:**  
`NO VALUE DETERMINABLE`

---

# Source record

## Google Drive framework
- `RULES_TENNIS.md`
- `RULES_GENERAL.md`
- active Sports Research model/evaluation/learning controls

## Official / primary current event sources
- Winston-Salem Open official schedule
- Winston-Salem Open official tournament news
- ATP Tour Winston-Salem results
- Tennis Australia current Duckworth reporting

## Current statistical sources
- Tennis Abstract — hard-court hold/break/serve/return and dominance splits
- Tennis.com — current Cincinnati H2H and Winston-Salem quarterfinal match stats
- tournament/result databases used to cross-check historical H2H

## H2H
- 2024 Busan Challenger: Duckworth 4-6, 6-1, 6-4
- 2024 Taipei Challenger: Duckworth 7-5, 7-5
- 2026 Cincinnati ATP Masters 1000: Fery 6-4, 2-6, 7-6(4)

## Limitations
- no operator was supplied, so retirement/walkover settlement rules are unknown;
- current statistical provider windows are not perfectly identical;
- no fitted/validated tennis probability model exists;
- old 2024 H2Hs are downweighted due to Fery's major development/fitness regime change;
- workload/recovery effect is treated as a branch rather than a deterministic penalty.

---

# Logging confirmation

**Canonical ID:** `P-136`

**Issued view:** `V01`

**Google Drive modified:** `NO`

**Delivery mode:** `DOWNLOADABLE MARKDOWN FILE`

**Retrospective:** `NOT INCLUDED`

**Final frozen state:** `PREGAME — approximately 25 minutes before the official not-before start`


# End of current log
