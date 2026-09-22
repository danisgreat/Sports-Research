# Prediction Mini Running Log — P-438 to P-451 — Settlement / Retrospective Implementation

**Settlement pass:** 2026-09-17 (Australia/Melbourne)  
**Drive access:** READ-ONLY  
**Method:** `MDS-2026.09.06-v4.0`  
**Mode:** `SPORTS_ONLY / MARKET_BLIND`  
**Performance status:** `LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE`  
**Issued-text integrity:** Original event blocks below are preserved verbatim. Settlement and retrospective material is appended; no pre-game rank, probability, rationale or source statement is rewritten.

**Canonical reconciliation update:** The current Drive `PREDICTION_LOG_COMBINED_4.md` now recognises `P-424`–`P-437` and identifies **P-438 as the next canonical ID**. Accordingly, the P-438–P-451 IDs in this mini log are now canonically aligned. The historical `[PROVISIONAL]` labels inside the original blocks remain untouched.

---

# 1. Incomplete / Unsettled Logs


## P-451 [PROVISIONAL] — Dorados de Chihuahua vs El Calor de Cancún

**Sport:** Basketball  
**Competition:** Liga Caliente.mx LNBP 2026 — Jornada 20  
**Venue:** Gimnasio Manuel Bernardo Aguirre (MBA), Chihuahua, Mexico  
**Scheduled start:** 16 Sep 2026 20:00 local Chihuahua / 17 Sep 2026 12:00 AEST  
**Frozen research cutoff:** **17 Sep 2026, 11:56:37 AEST**  
**State at cutoff:** **PREGAME / UPCOMING BY SCHEDULE**  
**Card status:** **BLOCKED — NO COMPLIANT FORECAST ISSUED**

### Fixture / identity verification
Verified:
- Dorados de Chihuahua vs El Calor de Cancún.
- Liga Caliente.mx LNBP 2026 regular season.
- Second game of the Sep. 15–16 two-game series.
- Jornada 20.
- Venue: Gimnasio Manuel Bernardo Aguirre.
- Scheduled for 20:00 Chihuahua local time on Sep. 16, which maps to 12:00 AEST Sep. 17.

The first game (Jornada 19) was completed the previous night:
- Dorados 91, El Calor 89.

No live or post-tip information from the second game is admitted into this record.

### Supplied markets
1. Dorados -4.5
2. El Calor +4.5
3. Over 176.5
4. Under 176.5

### Market-contract check
A currently indexed market for the same fixture showed a different main line:
- Dorados around -8
- game total around 174.5

Therefore the user's -4.5 / 176.5 thresholds appear to be **alternate or earlier/stale lines for the same fixture**, not markets belonging to another event.

This operator information is used **only for contract identity**, not as predictive evidence.

### Mandatory Drive gate failure
`RULES_BASKETBALL.md` §9.5 explicitly states:

- LNBP onboarding status: `PARTIAL / BLOCKING FOR A FUTURE CARD`.
- Before another LNBP/Copa Value card, an exact current league regulation, competition bulletin or field-owner statement must establish:
  - period length / clock;
  - foul-out and bonus rules;
  - challenge rules;
  - overtime/tie resolution;
  - roster size / activation;
  - import / foreign-player eligibility;
  - postponement, forfeit and abandonment treatment;
  - applicable competition-table implications.
- Until that packet is complete:
  - `BK-P1 = FAIL`;
  - the event is **not forecastable**;
  - no generic FIBA rate may be pooled into an LNBP forecast.

Current research re-searched for a 2026 LNBP regulation packet on the official LNBP domain and the wider web. No accessible current field-owner regulation packet closing those fields was recovered before the pregame cutoff.

Therefore:
- no ranked probabilities are issued;
- no projected winner is issued;
- no compliant total/spread card is issued;
- operator OT/regulation endpoint remains `UNKNOWN_DEFINITION`.

### Availability / rotation research

#### Dorados — previous-game starting five
From the Sep. 15 game:
- JR Clay
- Mikh McKinney
- Ricardo Valdez
- Markeith Cummings
- Austin Trice

Key previous-game contributors:
- Will Cherry: 19 points
- Mikh McKinney: 18
- Sindarius Thornwell: 11
- Austin Trice: 10
- Dorados bench: **43 points**

**Mikh McKinney status:** late in the Sep. 15 game he exited after suffering cramps. No authoritative pre-tip source was recovered confirming whether he had a minutes restriction or full clearance for the second game. Status therefore remains `UNCERTAIN`.

**Clint Chapman:** Dorados announced the arrival of the 2.08m American centre on Sep. 16. No authoritative pre-tip source was recovered confirming game-day registration, activation or expected minutes for Jornada 20. He is therefore **not assumed active**.

#### El Calor — latest rotation
Previous-game confirmed starters recovered:
- Paul Stoll
- Jarell Eddie
- D.J. Mitchell
- Francis King
- fifth starter not reliably reconstructed from the available pre-tip field-owner-quality sources.

Major rotation:
- Sa'eed Nelson: 18 points, 10 assists in ~26 minutes off the bench in the first game.
- Willie Reed: active and in the rotation after signing Sep. 11.
- Jarell Eddie: active after signing Sep. 11; scored 22 in the first game.

**José Jaime González:** unavailable. The 2.06–2.08m centre left El Calor and had already joined/trained with Salta Basket in Argentina before this second game.

### Current team context — descriptive only
Before the series:
**Dorados**
- 11-7; became 12-7 after Game 1.
- 7-3 at home entering the series.
- approximately 85.3 points scored / 83.3 allowed per game.
- coach: Jorge Elorduy.

**El Calor**
- 5-13; became 5-14 after Game 1.
- approximately 81.0 scored / 86.8 allowed.
- coach: Néstor "Che" García.

Season scoring leaders cited in current local reporting:
**Dorados**
- JR Clay ~14.5 PPG
- Jaden House ~13.9
- Will Cherry ~12.3
- Austin Trice ~11.5

**El Calor**
- Francis King ~14.3 PPG
- Sa'eed Nelson ~13.2
- D.J. Mitchell ~11.2
- plus current additions Jarell Eddie / Willie Reed.

These raw scoring averages are **context only**. Under `RULES_BASKETBALL.md`, raw PPG cannot substitute for opponent-adjusted possessions, shot profile, free-throw rate, turnover/rebound rates and lineup-specific efficiency.

### Previous game — current mechanisms only
Sep. 15:
- Dorados 91–89 El Calor.
- Quarter scores:
  - Q1 29–17 Dorados
  - Q2 21–25
  - Q3 21–30
  - Q4 20–17
- Dorados led for 29:05.
- Dorados made 11 threes.
- El Calor recovered from an 18-point deficit and briefly led.
- El Calor committed 12 turnovers.
- Dorados' bench produced 43 points.
- McKinney suffered late cramps.

The 180-point final and two-point margin are **not** used as automatic continuation evidence. Useful carry-forward mechanisms are:
- back-to-back at the same venue;
- possible McKinney conditioning/minutes uncertainty;
- Dorados bench depth;
- Eddie/Nelson/King current offensive roles;
- El Calor's interior rotation losing José Jaime González;
- possible Dorados frontcourt change through Chapman, if activated.

### Why no qualitative lean is promoted to a formal pick
The available descriptive data would tempt a model to:
- prefer Dorados from home record / superior season differential;
- prefer El Calor +4.5 from the first game's close margin;
- prefer Over from the first game's 180;
- prefer Under 176.5 from season scoring averages.

The Drive explicitly prohibits each shortcut without the current LNBP rules packet and a possession/efficiency/rotation model. Issuing one would knowingly bypass `BK-P1`.

### Material sources
1. El Calor official team site — Sep. 15–16 road schedule.
2. LNBP Oficial YouTube — official competition event stream/search lane.
3. Local Dorados press / Nuestras Noticias Chihuahua — exact Jornada 19 result and Jornada 20 20:00 schedule.
4. Deportes Locales / Dorados press — first-game starters, quarter flow, bench points, McKinney cramps, Chapman arrival.
5. RealGM — Sep. 15 box score / player rotation cross-check and current roster statistics.
6. Diario Cambio 22 + La Liga Argentina / Salta Basket reporting — José Jaime González departure/arrival.
7. Current local season preview reporting — team records, home record, scoring averages, coaches and leading scorers.
8. Current indexed operator page — **contract identity only**, confirming same fixture while showing a different main line.
9. Read-only Google Drive:
   - `METHOD.md`
   - `RULES_GENERAL.md`
   - `RULES_BASKETBALL.md`
   - `CONTROLS.md`
   - `SOURCES.md`
   - `PREDICTION_LOG_COMBINED_4.md`

### Current status
**BLOCKED_AT_ISSUE / NO PREDICTION**

Reason: `BK-P1 = FAIL` under current `RULES_BASKETBALL.md` LNBP onboarding instructions.

No retrospective or settlement performed.

### Document mapping
- Blocked event record → `PREDICTION_LOG_COMBINED_4.md` or current blocked/no-card section
- LNBP unresolved competition rules → existing `RULES_BASKETBALL.md` §9.5
- If a future official LNBP regulation packet is recovered → `RULES_BASKETBALL.md` §9.5 and `SOURCES.md` / `DATA_SOURCE_REGISTER.md`
- Event-specific player availability notes → P-451 block only unless later validated as durable process learning

### Current status audit — 2026-09-17 15:22 AEST

**State:** `START TIME PASSED / RESULT NOT RELIABLY RECOVERED — KEEP INCOMPLETE`  
The second Dorados–El Calor game (Jornada 20) was scheduled after the 91–89 Jornada 19 game. Current indexed schedule sources confirm the second fixture, but the searches in this settlement pass did **not** recover a sufficiently reliable final for that exact second event. Multiple result pages still point to the first 91–89 game, creating a material same-opponent/date collision risk.

Because **no compliant forecast was issued anyway** (`BK-P1 = FAIL`), there is no ranked selection or winner to grade. The blocked-at-issue decision remains methodologically correct.

**Do not use the 91–89 Jornada 19 final as the Jornada 20 result.**

#### Validation / source audit
1. Starting five: partial previous-game lineups only.
2. Bench/rotation: partial.
3. Coaches: yes.
4. Availability: McKinney/Chapman/González states were researched with uncertainty preserved.
5. Original sources: adequate to verify the fixture and justify the rules-gate block.
6. Better source needed: current LNBP field-owner result/gamebook for Jornada 20.
7. Blind spot: not a forecasting blind spot; the framework correctly blocked because competition rules remained unresolved.
8. Future: keep `BK-P1` fail-closed until the current rules packet is documented; separately resolve this final from a field-owning result source.

**Retry trigger:** official LNBP/Dorados/El Calor postgame record or a clearly identified reliable gamebook for **Jornada 20**, not the prior night's Jornada 19.

**Current source conflict**
- Nuestras Noticias Chihuahua confirms 91–89 was **Jornada 19** and explicitly says the second game was scheduled for Wednesday Sep 16.
- Current schedule feeds list a second Dorados–El Calor event, but no trustworthy final was recovered in this pass.


---
# 2. Temporary-ID / Canonical-ID Conflict Logs

**None.** Current Drive authority places the next canonical slot at P-438, so P-438–P-451 can be retained without renumbering.

---
# 3. Fully Settled Logs

## P-438 [PROVISIONAL] — Al Wahda Abu Dhabi vs Kuwait SC

**Competition:** AFC Champions League Two 2026/27, Group A  
**Venue:** Al Nahyan Stadium, Abu Dhabi  
**Scheduled start:** 17 Sep 2026, 02:00 AEST  
**Issue state:** PREGAME  
**Cutoff:** 01:52 AEST

### Ranked picks
1. First Half Under 1.5 — **84%**
2. Full Match Under 3.5 — **83%**
3. Al Wahda Team Total Under 2.5 — **82%**
4. Kuwait SC +1.5 — **75%**
5. Full Match Under 2.5 — **63%**

**Supplied markets:** 1H U0.5 52% / O0.5 48%; FT U2.5 63% / O2.5 37%.  
**Projected winner:** Al Wahda — 45%; Draw 30%; Kuwait 25%.  
**Status:** OPEN / UNSETTLED. No retrospective.

---

### Settlement and full retrospective — 2026-09-17

**Status:** `FINAL / SETTLED`  
**Official final:** **Al Wahda FC 3–2 Kuwait SC**. Kuwait scored twice inside eight minutes; Al Wahda pulled one back in the 23rd minute, later equalised, and won in second-half stoppage time. The first-half score was **Al Wahda 1–2 Kuwait SC**.

| Rank | Frozen contract | `p` (`UNVALIDATED_SUBJECTIVE`) | Result | Brier |
|---:|---|---:|---|---:|
| 1 | First Half Under 1.5 goals | 84% | **LOSS** | 0.7056 |
| 2 | Full Match Under 3.5 goals | 83% | **LOSS** | 0.6889 |
| 3 | Al Wahda team total Under 2.5 goals | 82% | **LOSS** | 0.6724 |
| 4 | Kuwait SC +1.5 | 75% | **WIN** | 0.0625 |
| 5 | Full Match Under 2.5 goals | 63% | **LOSS** | 0.3969 |

**Supplied 1H 0.5:** Under 0.5 = LOSS; Over 0.5 = WIN.  
**Supplied FT 2.5:** Under 2.5 = LOSS; Over 2.5 = WIN.  
**Projected winner:** Al Wahda — **WIN**.  
**Card mean Brier:** **0.5053** over five graded rows.  
**Rank-1:** LOSS. **Hit@2:** NO. **Wins@2:** 0/2. **Both Top 2:** NO.  
**NDCG@2:** not recomputed because the current v4.0 settlement schema does not define it as a mandatory score; no historical formula is silently recreated.

#### A. Prediction outcome
This was a poor ranked-card outcome: only Kuwait +1.5 won. The winner label was correct, but the ranked distribution materially underweighted a high-tempo/high-scoring branch.

#### B. Why each pick won or lost
- **R1 1H U1.5 — LOSS:** three goals arrived by the 23rd minute. The card's early-phase centre was too low and did not assign enough mass to a two-sided early conversion state.
- **R2 FT U3.5 — LOSS:** the match reached five goals. Once Kuwait led 2–0 almost immediately, the score-state incentives changed sharply: Al Wahda had to chase, Kuwait had transition space, and the original low-total state no longer described the game.
- **R3 Al Wahda TT U2.5 — LOSS:** Al Wahda scored three. The comeback state that was only a tail pregame became the dominant path after the 0–2 start.
- **R4 Kuwait +1.5 — WIN:** despite losing, Kuwait stayed within one goal. The cushion survived the comeback.
- **R5 FT U2.5 — LOSS:** the same early regime switch defeated the tighter Under even more decisively.

#### C. Deep Rank-1 failure review
| Question | Finding |
|---|---|
| Why was R1 ranked first? | It only lost with 2+ first-half goals and was intended to isolate a lower-variance phase from late-match uncertainty. |
| Was that logic justified pregame? | Partly, but 84% was too concentrated given unverified same-day XI/bench state and the possibility of an early goal causing a tactical regime switch. |
| Should another row have ranked higher? | Kuwait +1.5 had a wider set of survival states and was the only winner, but promoting it solely because it won would be hindsight. The pregame evidence did justify a smaller probability gap between it and the first-half Under. |
| What was missed/underweighted? | **Early-goal state transition.** Two Kuwait goals inside eight minutes made the original first-half and full-match Under centre obsolete. |
| Existing rule that should have helped | Soccer control 20 already requires explicit early-goal rank reconciliation; control 25 requires an early goal to propagate into later goal/transition states. |
| Smallest improvement | Before assigning >80% to an early Under, print explicit mass for `goal in first 10 minutes`, `second goal before 25`, and the resulting chase/transition branch. No new signed rule is needed. |

#### D. Top-two review
Both top selections lost through the same shared failure state: **very early Kuwait scoring -> forced Al Wahda chase -> open game**. This is a direct use case for current `G-L17`: correlated Top-2 rows need an explicit `P(¬R1 ∧ ¬R2)` shared-failure state, not merely a correlation label.

#### E. Over/Under review
The miss was primarily **state-transition geometry**, not generic venue scoring. The supplied Over 2.5 and 1H Over 0.5 both won. Future totals work should not infer that this competition is automatically “Over”; instead, the early-scoring branch needs more visible mass when lineups/defensive continuity are uncertain.

#### F. What went right
The outright Al Wahda winner call survived the 0–2 deficit, and Kuwait +1.5 correctly captured that the match could remain close even if Al Wahda eventually won.

#### G. Blind spots and mandatory validation
1. **Confirmed starting XIs both sides?** Not fully verified in the frozen card.
2. **Bench/reserves?** Incomplete.
3. **Coaches/managers?** Current team context was researched, but participant exposure remained the larger issue.
4. **Availability/rest/late withdrawals?** Partially checked; same-day participant confirmation was incomplete.
5. **Original sources accurate/current?** Fixture and competition sources were sound; participant completeness was weaker.
6. **Better sources?** AFC official match-centre/lineup release should be prioritised immediately before issue when accessible.
7. **Blind spot?** Early-goal/chase-state mass and probability extremity under participant uncertainty.
8. **Future treatment?** Execute existing early-goal regime-switch and `C-PROB-EXTREMITY` checks more strictly.

**Three-question retrospective**
1. **Actual driver:** two Kuwait goals inside eight minutes fundamentally changed the game state.
2. **Knowable pregame?** The exact sequence was not knowable, but the early-goal branch was knowable and should have had more mass.
3. **Smallest routine change:** quantify the early-score regime-switch branch before elevating a first-half Under above 80%.

**Event-specific learning:** `REINFORCES existing SO control 20/25 + G-L17`; no new forecast weight.

**Settlement/source audit**
- AFC official match report, “Group A: Al Wahda FC (UAE) 3-2 Kuwait SC”, retrieved 2026-09-17.
- AFC field owner is suitable for regulation score, scorers and event narrative.


---

## P-439 [PROVISIONAL] — Al Khaldiya vs Nasaf Qarshi

**Competition:** AFC Champions League Two 2026/27, Group A  
**Venue:** Bahrain National Stadium, Riffa  
**Scheduled start:** 17 Sep 2026, 02:00 AEST  
**Issue state:** PREGAME  
**Cutoff:** 01:57:30 AEST

### Ranked picks
1. First Half Under 2.5 — **87%**
2. Nasaf Team Total Under 2.5 — **85%**
3. Full Match Under 4.5 — **82%**
4. Al Khaldiya +1.5 — **79%**
5. First Half Under 1.5 — **73%**

**Supplied markets:** 1H O0.5 56% / U0.5 44%; FT U2.5 57% / O2.5 43%.  
**Projected winner:** Al Khaldiya — 42%; Draw 31%; Nasaf 27%.  
**Status:** OPEN / UNSETTLED. A later status check showed 0-0 live, but the pregame card remains frozen. No retrospective.

---

### Settlement and full retrospective — 2026-09-17

**Status:** `FINAL / SETTLED`  
**Official final:** **Al Khaldiya 0–0 Nasaf Qarshi**. **HT: 0–0**.

| Rank | Frozen contract | `p` (`UNVALIDATED_SUBJECTIVE`) | Result | Brier |
|---:|---|---:|---|---:|
| 1 | First Half Under 2.5 goals | 87% | **WIN** | 0.0169 |
| 2 | Nasaf team total Under 2.5 goals | 85% | **WIN** | 0.0225 |
| 3 | Full Match Under 4.5 goals | 82% | **WIN** | 0.0324 |
| 4 | Al Khaldiya +1.5 | 79% | **WIN** | 0.0441 |
| 5 | First Half Under 1.5 goals | 73% | **WIN** | 0.0729 |

**Supplied 1H 0.5:** Over = LOSS; Under = WIN.  
**Supplied FT 2.5:** Under = WIN; Over = LOSS.  
**Projected winner:** Al Khaldiya — **LOSS as a winner label; match drawn**.  
**Card mean Brier:** **0.0378**.  
**Rank-1:** WIN. **Hit@2:** YES. **Wins@2:** 2/2. **Both Top 2:** YES.

#### A/B. Outcome and pick causation
All five ranked rows won because neither side converted. The low-event/low-separation state dominated for 90 minutes. The protected Al Khaldiya handicap was robust to the draw, while the outright winner label was not.

#### C. Rank-1
No failure review required. R1 was structurally wide: even two first-half goals would still have won.

#### D. Top-two
Both won. Their relative ordering was defensible: the 1H U2.5 needed avoidance of an extreme early phase, while Nasaf U2.5 required Nasaf not to score three across the whole match.

#### E. O/U review
The supplied full-match Under 2.5 won, and 1H Under 0.5 also won. This is consistent with the card's low centre, but a single 0–0 does not validate a permanent competition-level Under bias.

#### F. What went right
The analysis appropriately preferred broad alternate Unders and a protected side over an aggressive winner claim.

#### G. Blind spots / validation
1. **Starting XIs?** Not fully field-owner confirmed at issue.
2. **Bench?** Incomplete.
3. **Coaches?** Context available, but no decisive coaching surprise established.
4. **Availability?** Partial.
5. **Source accuracy?** AFC competition identity and final were high quality.
6. **Better source?** AFC official lineups/match centre for same-day participant confirmation.
7. **Blind spot?** Winner distribution was still too willing to name Al Khaldiya despite a substantial draw band.
8. **Future treatment:** keep the draw state explicit and separate from protected-side confidence.

**Three-question retrospective**
1. **Driver:** neither side converted enough to break the low-event state.
2. **Knowable?** The low-scoring branch was reasonably knowable; exact 0–0 was not.
3. **Smallest change:** none; preserve draw-band discipline.

**Event-specific learning:** confirms soccer control 3 (draw-band discipline).

**Settlement source**
- AFC official: https://www.the-afc.com/en/club/afc_champions_league_two.html/news/group-a-al-khaldiya-sc-bhr-0-0-pfc-nasaf-uzb


---

## P-440 [PROVISIONAL] — Ararat-Armenia vs Sparta Praha

**Competition:** UEFA Europa League 2026/27, League Phase MD1  
**Venue:** Vazgen Sargsyan Republican Stadium, Yerevan  
**Scheduled start:** 17 Sep 2026, 02:45 AEST  
**Issue state:** PREGAME  
**Cutoff:** 02:31:53 AEST

### Ranked picks
1. First Half Under 2.5 — **89%**
2. Ararat-Armenia Team Total Under 2.5 — **87%**
3. Sparta Praha +1.5 — **86%**
4. Full Match Under 4.5 — **83%**
5. Sparta Praha Team Total Over 0.5 — **76%**

**Supplied markets:** 1H O0.5 64% / U0.5 36%; FT O2.5 56% / U2.5 44%.  
**Projected winner:** Sparta Praha — 51%; Draw 27%; Ararat-Armenia 22%.  
**Status:** OPEN / UNSETTLED. No retrospective.

---

### Settlement and full retrospective — 2026-09-17

**Status:** `FINAL / SETTLED`  
**Official final:** **Ararat-Armenia 1–4 Sparta Praha**. Goal timeline confirms **HT 0–2**.

| Rank | Frozen contract | `p` (`UNVALIDATED_SUBJECTIVE`) | Result | Brier |
|---:|---|---:|---|---:|
| 1 | First Half Under 2.5 goals | 89% | **WIN** | 0.0121 |
| 2 | Ararat-Armenia team total Under 2.5 goals | 87% | **WIN** | 0.0169 |
| 3 | Sparta Praha +1.5 | 86% | **WIN** | 0.0196 |
| 4 | Full Match Under 4.5 goals | 83% | **LOSS** | 0.6889 |
| 5 | Sparta Praha team total Over 0.5 | 76% | **WIN** | 0.0576 |

**Supplied 1H O0.5:** WIN. **Supplied FT O2.5:** WIN.  
**Projected winner:** Sparta Praha — **WIN**.  
**Card mean Brier:** **0.1590**.  
**Rank-1:** WIN. **Hit@2:** YES. **Wins@2:** 2/2.

#### A/B. Pick review
- **R1 1H U2.5 — WIN:** exactly two first-half goals; the wide phase cap survived.
- **R2 Ararat TT U2.5 — WIN:** Ararat scored once.
- **R3 Sparta +1.5 — WIN:** Sparta won outright.
- **R4 FT U4.5 — LOSS:** the fifth total goal arrived; the late/full-match upper tail was too light.
- **R5 Sparta TT O0.5 — WIN:** Sparta scored four.

#### C. Rank-1
Won. The first-half alternate was more robust than the full-game total because it reduced second-half substitution/game-state exposure.

#### D. Top-two
Both won. Their ordering was justified.

#### E. O/U review
The supplied Over 2.5 won and the ranked U4.5 lost at exactly five total goals. This was a full-match tail miss, not a first-half miss. The result supports retaining the existing distinction between early-phase and 90-minute distributions.

#### F. What went right
Sparta's superiority translated to the result and team-goal floor; the card did not require an exact margin to exploit that.

#### G. Blind spots / validation
1. Starting XIs: official squad lists were available; same-day XI/bench completeness at issue was limited.
2. Bench: incomplete.
3. Coaching: current context obtained.
4. Availability: checked to the extent supported by official/current sources.
5. Source quality: UEFA final/fixture record is strong.
6. Better source: UEFA lineups/event timeline for exact participant and phase fields.
7. Blind spot: second-half high-scoring tail.
8. Future treatment: when a superior side has multiple late scoring/substitution paths, keep full-match 5+ goal mass distinct from first-half control.

**Three-question retrospective**
1. Driver: Sparta converted its superiority repeatedly across both halves.
2. Knowable: superior-side scoring tail was knowable; exact four goals was not.
3. Smallest change: strengthen late/full-match upper-tail visibility without changing phase ranking rules.

**Source**
- UEFA official fixtures/results: https://www.uefa.com/uefaeuropaleague/news/02a8-2174cafa5bb6-82bbc20c9b92-1000--2026-27-europa-league-all-the-league-phase-fixtures/


---

## P-441 [PROVISIONAL] — Omonia Nicosia vs Celta Vigo

**Sport:** Soccer  
**Competition:** UEFA Europa League 2026/27  
**Stage:** League Phase, Matchday 1  
**Venue:** GSP Stadium, Nicosia, Cyprus  
**Scheduled start:** 16 Sep 2026 16:45 UTC / 19:45 Cyprus / 17 Sep 2026 02:45 AEST  
**Final issue cutoff:** 17 Sep 2026, 02:41:54 AEST  
**Game state at cutoff:** **PREGAME / SCHEDULED**

### Identity / rules
UEFA confirms Omonia vs Celta as a 2026/27 Europa League league-phase Matchday 1 fixture. This is a normal regulation match: a draw is valid after 90 minutes and there is no extra time.

### Frozen supplied markets
1. First-Half Goals Over/Under 0.5
2. Full-Match Goals Over/Under 2.5

### Ranked forecast

| Rank | Contract | Probability | Evidence |
|---:|---|---:|---|
| **1** | **First Half Under 2.5 Goals** | **92%** | Strongest / phase protected |
| **2** | **Full Match Under 4.5 Goals** | **91%** | Strong |
| **3** | **Celta Vigo Team Total Under 2.5 Goals** | **90%** | Strong, XI-limited |
| **4** | **Omonia Team Total Under 2.5 Goals** | **89%** | Strong, XI-limited |
| **5** | **Celta Vigo +1.5 Asian Handicap** | **86%** | Supported, XI/bench-limited |

Probability tier: `UNVALIDATED_SUBJECTIVE`.

### Supplied-market assessment

**1H 0.5 — FORCED_PAIR**
- Over 0.5 — **54%**
- Under 0.5 — **46%**

**FT 2.5 — FORCED_PAIR**
- Under 2.5 — **64%**
- Over 2.5 — **36%**

### Projected winner
**Celta Vigo — slight regulation-time preference**
- Celta 43%
- Draw 32%
- Omonia 25%
- Representative score: **Omonia 0-1 Celta**
- Close secondary states: 0-0, 1-1, 0-2.

### Pick #1 scrutiny
The 1H Under 2.5 only loses with 3+ first-half goals. Omonia's recent relevant HT states include:
- Omonia 0-0 Apollon — HT 0-0
- Aris 1-4 Omonia — HT 0-1
- Omonia 0-0 Omonia Aradippou — HT 0-0
- Omonia 4-2 STVV — HT 2-1
- Omonia 1-0 Lincoln Red Imps — HT 1-0
- Omonia 1-0 Kairat — HT 1-0
- Kairat 1-0 Omonia — HT 1-0

Only the STVV match produced 3 first-half goals.

Celta's last three verified HT states:
- Real Sociedad 0-0 Celta — HT 0-0
- Getafe 1-1 Celta — HT 1-0
- Celta 1-1 Málaga — HT 1-0

This gives the early phase a substantially narrower distribution than the full match while reducing exposure to late bench/fatigue uncertainty.

### Omonia recent form / process
Recent notable results:
- 0-0 vs Apollon
- 4-1 at Aris
- 0-0 vs Omonia Aradippou
- 4-2 vs STVV
- 0-1 at STVV
- 1-0 vs Lincoln Red Imps

Process evidence:
- vs Apollon: ~53–54% possession, 15–16 shots, 8 SOT, 5 corners; 0-0.
- vs Omonia Aradippou: 67% possession, 26 shots, 11 SOT, 10 corners; 0-0.
- at Aris: 60% possession, 12 shots, 10 SOT, 6 corners; won 4-1.
- vs STVV: 47% possession, 19–21 shots, 5 SOT, 5 corners, xG reported around 3.35; won 4-2.

Interpretation: Omonia's low-score results coexist with genuine chance volume and high-scoring tails. The forecast therefore does not blindly extrapolate the 0-0 trend.

### Celta recent form / process
Recent league results:
- 0-0 at Valencia
- 0-2 vs Athletic Club
- 0-0 at Real Sociedad
- 1-1 at Getafe
- 1-1 vs Málaga

**Goals scored:** 2 across those five league matches.

Process:
- at Real Sociedad: 7 shots, 2 SOT, 3 corners, xG ~0.6.
- at Getafe: 70% possession, 16 shots, 3 SOT, 5 corners, xG ~1.0–1.3 depending provider.
- vs Málaga: led 1-0 at HT, created further second-half chances, conceded from a corner in the 83rd minute.

Interpretation: the scoring drought is real, but the shot/xG process has been better than two goals alone suggests. A Celta trend-break branch remains live.

### Participants

**UEFA registered squads:** VERIFIED.  
**Confirmed official starting XIs/full benches:** **NOT RETRIEVED by issue cutoff**; UEFA still displayed the official squad list.

**Omonia official match squad:** Kaminski, Fabiano, Michail, Coulibaly, Montnor, Kakoullis, Ewandro, Maric, Tănase, Brouwers, Mayambela, Tankovic, Simic, Balkovec, Satka, Andreou, Nego, Christou, Neophytou, Konstantinidis, Christoforou, Duverne, Diony.

Projected Omonia XI remains uncertain, particularly goalkeeper (Kaminski/Fabiano) and attacking-midfield allocation.

**Celta official travelling squad:** Bayindir, Radu, Villar, Starfelt, Marcos Alonso, Faye, Carreira, Moriba, Miguel Román, Ferran Jutglà, Pablo Durán, Aleix Febas, Álvaro Núñez, Hugo González, Javi Rueda, Yoel Lago, Williot Swedberg, Javi Rodríguez, Sebastián Cáceres, Javi Galán, Hugo Álvarez, Driouech, Hugo Burcio, Jones El-Abdellaoui, Borja Iglesias.

Projected Celta shape: 3-4-3, with Radu commonly projected in goal and a back three drawn from Cáceres/Lago/Alonso/Starfelt.

### Injuries / suspensions
**Celta**
- **Iago Aspas — CONFIRMED OUT through injury by RC Celta.**
- Secondary reports claiming Borja Iglesias, Aleix Febas or Jones El-Abdellaoui are definitely unavailable are rejected because they appear in Celta's official travelling squad.
- No current suspension confirmed in the club's squad notice.

**Omonia**
- Official 23-player squad published.
- Carel Eiting and Fotis Kitsos are absent from the squad, but no current official medical notice retrieved in this pass proves the exact reason; they are not labelled as confirmed injuries.
- No current suspension confirmed from the club's preparation notice.

### Coaches
- Omonia: **Henning Berg**
- Celta: **Claudio Giráldez**

### Rest / congestion
- Omonia last played Apollon on 12 September and remain at GSP.
- Celta last played Málaga on 13 September, then travelled to Cyprus.
- Celta's official work plan shows Racing Santander at home on Saturday 19 September.
- Omonia's next domestic match is listed for 20 September.

Omonia therefore hold the smaller travel/recovery advantage; this increases the Omonia/draw and low-margin branches.

### Goalkeepers
- Omonia: Thomas Kaminski and Fabiano both available; exact starter not confirmed.
- Celta: Bayindir, Radu and Villar travelled; Radu started the recent Real Sociedad/Getafe/Málaga run. Exact starter not confirmed.

### xG / shots
No cross-league season-level xG blend was created.

Event-level values retained only within provider context:
- Omonia vs STVV: xG roughly 3.35–1.77.
- Real Sociedad vs Celta: Celta ~0.6 xG.
- Getafe vs Celta: Celta ~1.0–1.3 xG depending provider.

### Corners / set pieces
Recent evidence:
- Omonia: 10 corners vs Omonia Aradippou; 5 vs Apollon; 5 vs STVV; 6 at Aris.
- Celta: 3 at Real Sociedad; 5 at Getafe; 5 vs Málaga.
- Celta conceded Málaga's equaliser from a corner.
- Omonia scored an 82nd-minute corner-related goal against STVV.

No corner market issued because no exact corner line was supplied and no complete cross-competition corner distribution was built.

### Tactical matchup
Omonia can alternate between compact control and aggressive home pressure. Celta's 3-4-3 can generate wide possession and territorial control, but the opening league sample shows inefficient conversion. Aspas' confirmed absence removes a key creator/finisher and increases reliance on Jutglà, Swedberg, Hugo González, Driouech/Pablo Durán and wing-back progression.

### Weather
GSP Stadium/Nicosia event window:
- Clear
- ~28°C around 20:00 local, easing toward ~26°C
- No meaningful rain

Only a small home-comfort/fatigue adjustment is applied.

### Upset / trend-break branches
1. Omonia's home chance creation exceeds Celta's defensive expectation.
2. Celta's short rest/travel and Saturday league fixture reduce intensity or increase rotation.
3. Omonia's set-piece threat exploits Celta's recent corner concession.
4. Celta's underlying shot/xG process finally converts and breaks the low-scoring trend.
5. Early goal turns the game into an Omonia-STVV-style open state.
6. Red card, penalty or goalkeeper error.
7. Celta's class advantage manifests more strongly than its domestic results.
8. Omonia's recent 4-1/4-2 outputs prove a genuine high-tail attack.

### Probability geometry

**First-half state**
- 0 goals: 46%
- 1 goal: 36%
- 2 goals: 10%
- 3+ goals: 8%

Derived:
- 1H Over 0.5 = 54%
- 1H Under 0.5 = 46%
- 1H Under 1.5 = 82%
- 1H Under 2.5 = 92%

**Full-match total**
- 0 goals: 10%
- 1 goal: 24%
- 2 goals: 30%
- 3 goals: 19%
- 4 goals: 8%
- 5+ goals: 9%

Derived:
- FT Under 2.5 = 64%
- FT Over 2.5 = 36%
- FT Under 4.5 = 91%

### Top-two dependence
R1 and R2 are positively coupled.

`P(R1 ∩ R2) = JOINT_UNQUANTIFIED`

Fréchet bounds:
- Lower: **83%**
- Upper: **91%**

### Settlement routes
- Regulation result/full totals/team totals/handicap: UEFA official match event/final.
- First-half goals: UEFA official first-half score/timeline.
- Full-match scope: regulation 90 minutes + stoppage only.

### Material sources
1. UEFA league-phase fixtures:  
   https://www.uefa.com/uefaeuropaleague/news/02a8-2174cafa5bb6-82bbc20c9b92-1000--2026-27-europa-league-all-the-league-phase-fixtures/
2. UEFA Omonia-Celta official squad page:  
   https://www.uefa.com/uefaeuropaleague/match/2050063--omonia-vs-celta/lineups/
3. Omonia official preparation/match squad:  
   https://www.omonoiafc.com.cy/
4. Omonia official news / pre-game press conference:  
   https://www.omonoiafc.com.cy/news/
5. Celta official travelling squad:  
   https://rccelta.es/en/equipo/actualidad/celta-squad-list-for-first-uel-match-against-omonia-nicosia/
6. Celta official Málaga report:  
   https://rccelta.es/en/equipo/actualidad/points-shared-at-abanca-balaidos-celta-1-1-malaga-cf/
7. Celta official Real Sociedad report:  
   https://rccelta.es/en/equipo/actualidad/real-sociedad-vs-celta-0-0-summary-and-goals-highlights-laliga-ea-sports-26-27/
8. Celta official work plan:  
   https://rccelta.es/equipos/primer-equipo/plan-trabajo/
9. Omonia-Apollon process: Apollon official/FotMob.
10. Omonia-STVV process: STVV official/365Scores.
11. Omonia-Aradippou process: ZeroZero.
12. Aris-Omonia process: RedScores.
13. Celta-Getafe process: SoccerZZ/xGScore/StatMuse.
14. Real Sociedad-Celta process: SoccerZZ/xGScore.
15. Venue-specific weather source.
16. Read-only Drive governing docs: `METHOD.md`, `RULES_GENERAL.md`, `RULES_SOCCER.md`, `LEAGUE_RULES_SOCCER.md`, `CONTROLS.md`, `SOURCES.md`, `PREDICTION_LOG_COMBINED_4.md`.

### Social/current-source check
Official Omonia and Celta club channels provided the strongest current material. Indexed X searches surfaced the official club accounts but did **not** surface a fresh official starting-XI post before cutoff; no social lineup was promoted to confirmed status.

### Current status
**OPEN / UNSETTLED — PREGAME AT ISSUE**

No settlement or retrospective performed.

### Document mapping
- Card → `PREDICTION_LOG_COMBINED_4.md`
- ID reconciliation → `GAME_LOG_STATUS_CURRENT.md`
- Europa League rules currency → `LEAGUE_RULES_SOCCER.md`
- Source lanes → `SOURCES.md` / `DATA_SOURCE_REGISTER.md`
- Future learning → P-441 retrospective block first

---

---

### Settlement and full retrospective — 2026-09-17

**Status:** `FINAL / SETTLED`  
**Official final:** **Omonia 1–0 Celta Vigo**. The decisive Omonia goal came late; **HT 0–0**.

| Rank | Frozen contract | `p` (`UNVALIDATED_SUBJECTIVE`) | Result | Brier |
|---:|---|---:|---|---:|
| 1 | First Half Under 2.5 goals | 92% | **WIN** | 0.0064 |
| 2 | Full Match Under 4.5 goals | 91% | **WIN** | 0.0081 |
| 3 | Celta Vigo team total Under 2.5 goals | 90% | **WIN** | 0.0100 |
| 4 | Omonia team total Under 2.5 goals | 89% | **WIN** | 0.0121 |
| 5 | Celta Vigo +1.5 Asian Handicap | 86% | **WIN** | 0.0196 |

**Supplied 1H O0.5:** LOSS. **Supplied FT U2.5:** WIN.  
**Projected winner:** Celta — **LOSS**.  
**Card mean Brier:** **0.0112**.  
**Rank-1:** WIN. **Hit@2:** YES. **Wins@2:** 2/2. **All ranked rows:** WIN.

#### A/B. Pick review
Every ranked contract survived the 1–0 final. The outright winner did not: Omonia's home edge/set-piece/late-goal branch was sufficient to flip a low-event match.

#### C/D. Rank-1 and Top-two
R1 and R2 were appropriately broad low-tail contracts and both won. This is a good example of ranking robust event-shape contracts above a close 1X2 opinion.

#### E. O/U review
The FT Under 2.5 won. The 1H Over 0.5 lost, consistent with the card's own 46% 0-goal first-half state. No correction is warranted merely because the forced-pair preference missed.

#### F. What went right
The card explicitly retained Omonia home upset branches, Celta travel/rest uncertainty and Aspas' absence while keeping the low-score distribution primary.

#### G. Blind spots / validation
1. Starting XI: not retrieved by cutoff.
2. Bench: not retrieved by cutoff.
3. Coaches: Henning Berg and Claudio Giráldez obtained.
4. Injuries/availability: Aspas confirmed out; other claims appropriately filtered.
5. Sources: official club/UEFA sources were strong; some third-party xG remained provider-specific.
6. Better source: UEFA same-day lineup feed immediately before kickoff.
7. Blind spot: winner probability still leaned Celta despite meaningful Omonia/draw branch.
8. Future treatment: keep winner probability modest when participant completeness is weak and the total distribution is low.

**Three-question retrospective**
1. Driver: one late Omonia conversion in an otherwise low-scoring game.
2. Knowable: the Omonia upset branch was explicitly knowable and present.
3. Smallest change: none to the totals; preserve winner/handicap separation.

**Source**
- UEFA official Matchday 1 results: https://www.uefa.com/uefaeuropaleague/news/02a8-2174cafa5bb6-82bbc20c9b92-1000--2026-27-europa-league-all-the-league-phase-fixtures/


---

## P-442 [PROVISIONAL] — Chicago White Sox @ Cleveland Guardians

**Sport:** Baseball  
**Competition:** MLB 2026 regular season  
**Event:** Chicago White Sox @ Cleveland Guardians  
**Venue:** Progressive Field, Cleveland, Ohio  
**Scheduled start:** 16 Sep 2026 13:10 EDT / 17 Sep 2026 03:10 AEST  
**Issue-state verification:** PREGAME / SCHEDULED  
**Pregame research cutoff:** 17 Sep 2026, approximately 02:55 AEST  
**Scheduled innings:** 9; Cleveland has home-last-bat entitlement; MLB extra-inning runner rule applies if tied after nine.

### Contract correction
The user wrote `White Six +1.5`. This was treated as the obvious typo **White Sox +1.5** because the named MLB fixture and opposing `Guardians -1.5` line make the intended contract unambiguous.

### Frozen supplied markets
1. White Sox +1.5
2. Guardians -1.5
3. Combined Total Over 7.0 Runs
4. Combined Total Under 7.0 Runs

### Starter identity handshake
**Chicago White Sox:** Anthony Kay, LHP — `PROBABLE_OFFICIAL`  
**Cleveland Guardians:** Parker Messick, LHP — `PROBABLE_OFFICIAL`

MLB's current probable-pitcher page lists:
- Anthony Kay: 9-9, 4.53 ERA, 118 SO
- Parker Messick: 11-9, 2.51 ERA, 178 SO

No starter scratch was verified before issue.

### Starting lineups
**Official posted lineups:** `NOT RELEASED / TBD at final refresh`.

MLB's starting-lineup page still showed both CWS and CLE orders as TBD. Therefore:
- no specific projected nine-man batting order is treated as confirmed;
- lineup-slot PA and exact platoon-cluster effects remain widened;
- player-prop analysis is blocked;
- side/total confidence is capped accordingly.

### Ranked prediction

| Rank | Exact contract | Win probability | Push | Evidence status |
|---:|---|---:|---:|---|
| **1** | **White Sox +1.5 runs** | **65%** | 0% | Strongest of supplied slate |
| **2** | **Combined Total Over 7.0 runs** | **48%** | **15%** | Moderate / wide-tail |
| **3** | **Combined Total Under 7.0 runs** | **37%** | **15%** | Moderate-low |
| **4** | **Guardians -1.5 runs** | **35%** | 0% | Lowest of supplied slate |

Probability tier for every row: `UNVALIDATED_SUBJECTIVE`.

**NO VALUE DETERMINABLE** because no validated predictive model plus same-time price snapshot is available.

### Projected game winner
**Cleveland Guardians — slight preference**
- Cleveland win: **57%**
- Chicago win: **43%**

Representative central score: **Guardians 4, White Sox 3**.

Margin decomposition:
- White Sox outright win: ~43%
- Cleveland by exactly 1 run: ~22%
- Cleveland by 2+ runs: ~35%

This produces:
- White Sox +1.5 ≈ 65%
- Guardians -1.5 ≈ 35%

### Pick #1 scrutiny — White Sox +1.5
This is the strongest supplied contract because it does not require Chicago to beat Parker Messick outright. It survives:
- any White Sox win;
- a one-run Cleveland win.

That cushion is especially valuable in a low-to-moderate scoring game with a strong Cleveland starter, Cleveland home-last-bat entitlement, and a realistic one-run late-game branch.

Key support:
1. **Chicago has handled LHP reasonably well.**
   - 2026 season OPS vs LHP: about **.739-.740**.
   - Last 30 days vs LHP: **.781 OPS**.
2. **Cleveland has been much weaker against LHP.**
   - 2026 season OPS vs LHP: about **.665**.
   - Last 30 days vs LHP: about **.650**.
3. Kay is materially weaker than Messick overall, but the specific Cleveland-vs-LHP offensive environment reduces the expected separation.
4. Kay previously held Cleveland to 2 ER over 6.0 IP on Aug. 8. Per Drive rules this is contextual only, not ownership of the matchup.
5. Progressive Field is close to neutral/slightly suppressive in the current multi-year Statcast run environment, which supports a non-blowout branch more than an automatic multi-run Cleveland win.
6. Cleveland's high-leverage bullpen was used aggressively the previous night. Cade Smith threw 1.2 scoreless innings / five outs, and Cleveland also used multiple leverage arms. Freshness therefore differs from a completely rested late-game chain.

Important opposing evidence:
- Messick is clearly the superior starter.
- Chicago's official batting order had not posted at issue.
- Cleveland has home last bat and a deep/high-quality bullpen.
- Anthony Kay has been poor recently and often exits before six innings.
- If Kay's recent contact/early-hook state occurs and Cleveland clusters damage before Chicago reaches the bullpen, a 4-1/5-2/6-2 Cleveland branch defeats the cushion.

Conclusion: the exact matchup gives Cleveland the higher outright win probability, but **not enough reliable multi-run separation to make Cleveland -1.5 preferable to Chicago +1.5**.

### Parker Messick — current process
2026:
- ERA: **2.51**
- IP: **172.1**
- WHIP: **1.03**
- K%: **26.0%**
- BB%: **6.9%**
- FIP: **3.11**
- xERA: roughly **3.0** (Baseball Savant / Pitcher List)
- HR/9: **0.84**
- Hard-hit rate allowed: **32.6%**
- xBA allowed: **.221**
- xSLG allowed: **.334**

Recent starts:
- Sep. 11 @ MIN: 5.1 IP, 3 H, 1 ER, 2 BB, 5 K
- Sep. 5 vs DET: 6.0 IP, 7 H, 3 ER, 2 BB, 12 K
- Aug. 30 vs KC: 6.0 IP, 5 H, 1 ER
- Aug. 24 @ LAA: 6.0 IP, 3 H, 1 ER

Messick's 2026 fastball velocity has also improved relative to his earlier professional baseline, an MLB-reported mechanism behind his breakout.

### Anthony Kay — current process
2026:
- ERA: **4.53**
- IP: **145.0**
- WHIP: **1.37**
- K%: **18.1%**
- BB%: **7.8%**
- FIP: approximately **4.81-4.82**
- xERA: **5.01**
- xwOBA allowed: **.341**
- Hard-hit rate: **39.4%**

Recent starts:
- Sep. 11 @ STL: 4.0 IP, 5 H, 3 ER, 1 BB, 2 K
- Sep. 5 vs MIN: 4.1 IP, 6 H, 5 ER, 1 BB, 3 K
- Aug. 31 @ HOU: 4.2 IP, 6 H, 5 ER
- Aug. 25 vs TEX: 4.2 IP, 6 H, 4 ER

September to date before this game:
- 8.1 IP
- 11 H
- 8 ER
- 2 BB
- 5 K

This is a meaningful current-regime concern, but the Drive requires shrinkage toward the season process rather than letting two starts control the forecast.

### Platoon matchup
Both starters are left-handed.

**White Sox vs LHP**
- Season OPS: ~**.740**
- Last 30 days: **.781**

**Guardians vs LHP**
- Season OPS: ~**.665**
- Last 30 days: **.650**

This is one of the main reasons Cleveland's starter advantage does not translate directly into a high-confidence -1.5 call.

### Total 7.0 geometry
The total is an integer line, so exactly seven runs is a live push state.

Forecast state:
- **Over 7.0 win:** ~48%
- **Exactly 7:** ~15% push
- **Under 7.0 win:** ~37%

Preferred supplied direction: **Over 7.0**, but only moderately.

#### Why Over ranks #2
Upper-tail mechanisms:
- Kay's current early-hook/contact branch is materially live.
- Chicago has been strong vs LHP recently despite Messick's quality.
- The prior night's game taxed Cleveland leverage relief.
- White Sox closer Grant Taylor worked 1.2 innings and allowed two runs in the walk-off loss.
- Thunderstorm/delay risk can change starter warm-up/length and move innings into middle relief.
- MLB extra innings use a runner in scoring position, so a tied game after nine creates a higher-run-rate state rather than ordinary extra innings.

#### Why Under remains substantial
- Messick owns elite current run prevention and contact suppression.
- Cleveland has been one of the weaker MLB offences vs LHP.
- Progressive Field's multi-year Statcast run factor is slightly below average (~98 for runs).
- Cleveland's bullpen remains structurally strong even with some workload.
- A 3-2, 4-2, 3-3-through-nine or 4-3 type game remains very plausible.

### Bullpen state
**Cleveland**
- High-leverage bullpen is a team strength.
- Cade Smith: 1.2 IP, 0 ER on Sep. 15 and used for five outs.
- Guardians also used leverage arms such as Sabrowski and Gaddis earlier than usual in the walk-off win.
- Therefore "fresh bullpen" is not assumed; score-state-specific availability is widened.

**Chicago**
- Grant Taylor: 1.2 IP, 2 ER and took the loss on Sep. 15.
- The White Sox recently promoted LHP Noah Schultz and designated José Urquidy for assignment, changing available pitching depth.
- Workload affects availability, not assumed performance.

### Injuries / availability
**Guardians**
- Angel Martínez: right flank inflammation, day-to-day.
- Chase DeLauter: right wrist soreness, day-to-day.
- Shawn Armstrong: 60-day IL with calf strain, rehab progression.
- Colin Holderman: IL with right wrist inflammation.
- Exact availability of Martínez and DeLauter for today's lineup was unresolved because official orders were still TBD.

**White Sox**
- Tommy Pham: left calf strain, 10-day IL; manager indicated it was unlikely he would return during the Cleveland series.
- Huascar Brazobán: IL / rehab status.
- Other current IL designations remain subject to the official roster report.

### Recent offensive / series context
Series:
- Sep. 14: White Sox 7, Guardians 3
- Sep. 15: Guardians 7, White Sox 6

These finals are **context only**, not a trend signal by themselves.

Named active mechanisms from the series:
- Chicago has already created multi-run innings against Cleveland relief.
- Cleveland used leverage relief aggressively in Game 2.
- Chicago's Grant Taylor absorbed a high-leverage ninth-inning loss.
- Cleveland's Travis Bazzana and Jo Adell showed current HR power in Game 2.
- Chicago's Miguel Vargas has produced in the series.
- Cleveland's two key outfielders Martínez/DeLauter have current health uncertainty.

### Park / weather
**Progressive Field**
- Statcast 2024-26 run factor: approximately **98** (slightly suppressive).
- 2026 current run index around league average, HR environment below average in available Savant-derived records.

**Game-window weather**
- roughly 24-26°C;
- humid;
- thunderstorms possible around the early game window;
- intermittent clouds after the highest early storm risk.

No automatic Over/Under weather sign is applied. Rain is treated as a termination/delay/starter-disruption branch, as required by `RULES_BASEBALL.md` control 18.

### Upset / trend-break and tail branches
Explicit branches retained:
1. Messick central/quality start + Cleveland narrow win.
2. Messick dominant + Kay early hook → Cleveland 2+ margin.
3. Kay rebounds toward his earlier Cleveland start while Guardians' LHP weakness persists.
4. Chicago's strong LHP split creates 3-4 runs against Messick/first relief transition.
5. Cleveland's recent home-run burst repeats against Kay.
6. High-leverage bullpen fatigue changes late-game separation.
7. Weather delay disrupts either starter's normal length.
8. Tie-after-nine → automatic-runner extras raises total/margin variance.
9. Defensive/error cluster creates unearned-run tail.

### Settlement routes
- Official final/box score: MLB game centre / MLB StatsAPI.
- Run line: final score including MLB extra innings unless operator terms state otherwise.
- Total 7.0: final score including eligible extra innings; exact 7 = push under standard O/U 7.0 settlement.
- Listed-pitcher/action terms were not supplied by the user; operator-specific action rule remains `UNKNOWN_DEFINITION`.

### Material sources
1. MLB probable pitchers:
   https://www.mlb.com/probable-pitchers
2. White Sox probable pitchers:
   https://www.mlb.com/whitesox/roster/probable-pitchers
3. MLB starting lineups:
   https://www.mlb.com/starting-lineups
4. Baseball Savant — Parker Messick:
   https://baseballsavant.mlb.com/savant-player/parker-messick-800048
5. Baseball Savant — Anthony Kay:
   https://baseballsavant.mlb.com/savant-player/anthony-kay-641743
6. Pitcher List — Parker Messick / Anthony Kay current advanced lines.
7. StatMuse — 2026 and last-30-day team OPS vs LHP.
8. MLB Guardians injuries:
   https://www.mlb.com/news/guardians-injuries-and-roster-moves
9. MLB White Sox injuries:
   https://www.mlb.com/whitesox/news/white-sox-injuries-and-roster-moves
10. MLB Sep. 15 game recap / film room and official current team reporting.
11. Baseball Savant park factors — Progressive Field:
    https://baseballsavant.mlb.com/leaderboard/statcast-park-factors
12. Venue-local weather source for Progressive Field.
13. Read-only Google Drive governing docs:
    `METHOD.md`, `RULES_GENERAL.md`, `RULES_BASEBALL.md`, `CONTROLS.md`, `SOURCES.md`, `PREDICTION_LOG_COMBINED_4.md`.

### Social / reporter check
Searches of the official White Sox and Guardians channels did not surface a reliably indexed Sep. 16 posted batting order before the cutoff. MLB's official lineup page also remained TBD. No social-media lineup was therefore promoted to confirmed status.

### Current status
**OPEN / UNSETTLED — PREGAME AT ISSUE**

No settlement or retrospective performed.

### Document mapping
- Event card → `PREDICTION_LOG_COMBINED_4.md`
- Provisional ID/status → `GAME_LOG_STATUS_CURRENT.md`
- Baseball-specific matchup/bullpen/weather controls → existing `RULES_BASEBALL.md` (no new rule promoted)
- Any newly useful source lane → `SOURCES.md` / `DATA_SOURCE_REGISTER.md`
- Future event learning → P-442 retrospective block first; general promotion only under prospective-evidence requirements

---

### Settlement and full retrospective — 2026-09-17

**Status:** `FINAL / SETTLED`  
**Official MLB final:** **Guardians 6–3 White Sox**. Chicago led 3–2 after Tommy Pham's three-run homer; Cleveland then scored four in the sixth, including Petey Halpin's three-run homer. Parker Messick: **6.0 IP, 3 ER, 8 K**.

| Rank | Frozen contract | `p` (`UNVALIDATED_SUBJECTIVE`) | Result | Brier |
|---:|---|---:|---|---:|
| 1 | White Sox +1.5 runs | 65% | **LOSS** | 0.4225 |
| 2 | Combined Total Over 7.0 runs | 48% | **WIN** | 0.2704 |
| 3 | Combined Total Under 7.0 runs | 37% | **LOSS** | 0.1369 |
| 4 | Guardians -1.5 runs | 35% | **WIN** | 0.4225 |

**Projected winner:** Cleveland — **WIN**.  
**Final total:** 9; no push.  
**Card mean Brier:** **0.3131**.  
**Rank-1:** LOSS. **Hit@2:** YES. **Wins@2:** 1/2. **Both Top 2:** NO.

#### A/B. Pick review
- **R1 CWS +1.5 — LOSS:** Chicago's starter-side branch performed better than feared, but the sixth-inning relief transition produced exactly the multi-run Cleveland separation that killed the cushion.
- **R2 O7 — WIN:** nine runs; the upper-tail branch arrived through a bullpen/cluster inning rather than both starters collapsing.
- **R3 U7 — LOSS:** same sixth-inning cluster defeated the Under.
- **R4 CLE -1.5 — WIN:** Cleveland won by three.

#### C. Deep Rank-1 failure review
| Question | Finding |
|---|---|
| Why R1 first? | It combined every Chicago win with one-run Cleveland wins and was supported by Chicago's better LHP split plus Cleveland's weaker LHP offense. |
| Was ranking justified? | Defensible, but the 65% cushion underestimated a score-state-specific bullpen cluster. |
| Another row higher? | The Over was only 48% and Cleveland -1.5 35%; promoting them after the result would be hindsight. |
| Key missed/underweighted variable | The **relief transition**, not Anthony Kay. Kay allowed only two unearned runs over four innings; Sean Newcomb then gave up the decisive three-run homer. |
| Existing rule | Baseball controls 19–21 already require cluster risk and score-state bullpen mapping. |
| Improvement | Rank a +1.5 only after explicitly carrying the opponent's `starter contained -> damage first/middle relief -> 2+ separation` path, even if the starter matchup itself favours the cushion. |

#### D. Top-two
R1 lost, R2 won. Hit@2 succeeded, but the top ordering did not fully reflect that the same Cleveland late-separation branch could also push the game Over.

#### E. O/U
The Over won. This supports existing joint margin-total logic: Cleveland's multi-run sixth simultaneously created separation and the upper total state.

#### F. What went right
The projected Cleveland winner was correct; Messick's quality remained real; the card did not assume his presence made Cleveland -1.5 automatic.

#### G. Validation questions
1. Starting lineups: no official posted orders at issue.
2. Bench/bullpen: leverage workload researched, full score-state chain incomplete.
3. Manager: implicit bullpen deployment context, not fully modelled.
4. Injuries: Martínez/DeLauter uncertainty was checked; Halpin started because both were out.
5. Sources: MLB probable pitchers/injury pages were accurate; lineup timing was incomplete.
6. Better source: MLB GameDay posted lineup + bullpen availability immediately pregame.
7. Blind spot: middle-relief separation branch.
8. Future treatment: use explicit bullpen ladder by score state, not “bullpen quality/freshness” summary.

**Three-question retrospective**
1. Driver: Halpin's three-run homer off relief in a four-run sixth.
2. Knowable: bullpen transition risk was knowable; the exact Halpin outcome was not.
3. Smallest change: strengthen `BB-S4/BB-B2` score-state relief-chain execution.

**Sources**
- MLB official recap: https://www.mlb.com/news/petey-halpin-homers-guardians-take-al-central-lead-from-white-sox
- MLB Film Room/game summary: https://www.mlb.com/video/game/824382


---

## P-443 [PROVISIONAL] — San Francisco Giants @ St. Louis Cardinals

**Sport:** Baseball  
**Competition:** MLB 2026 regular season  
**Venue:** Busch Stadium, St. Louis, Missouri  
**Scheduled start:** 16 Sep 2026 13:15 EDT / 12:15 CDT / 17 Sep 2026 03:15 AEST  
**Final pregame cutoff:** 17 Sep 2026, 03:00:45 AEST  
**State at cutoff:** **PREGAME / SCHEDULED**

### Frozen supplied markets
1. Giants +1.5
2. Cardinals -1.5
3. Combined Total Over 8.0 Runs
4. Combined Total Under 8.0 Runs

### Starter identity handshake
- **SF:** Anthony Molina, RHP — `PROBABLE_OFFICIAL`
- **STL:** Matthew Liberatore, LHP — `PROBABLE_OFFICIAL`

MLB official probable-pitcher pages confirmed both names at cutoff.

### Official batting orders
**Not posted / TBD for both teams at cutoff.**

No projected nine-man order is treated as confirmed. Lineup-dependent effects remain capped and widened.

### Ranked forecast

| Rank | Exact contract | Win | Push | Evidence |
|---:|---|---:|---:|---|
| **1** | **Giants +1.5 runs** | **61%** | 0% | Strongest supplied contract |
| **2** | **Combined Total Over 8.0** | **45%** | **13%** | Moderate / upper-tail lean |
| **3** | **Combined Total Under 8.0** | **42%** | **13%** | Moderate-low |
| **4** | **Cardinals -1.5 runs** | **39%** | 0% | Lowest supplied contract |

Probability tier: `UNVALIDATED_SUBJECTIVE`.

**NO VALUE DETERMINABLE** without a validated probability model and same-time price snapshot.

### Projected winner
**St. Louis Cardinals — slight preference**
- STL win: **55%**
- SF win: **45%**

Margin decomposition:
- Giants outright win: ~45%
- Cardinals by exactly 1: ~16%
- Cardinals by 2+: ~39%

Representative score corridor: **STL 4-3 / 5-4 SF**, with 8-run push states also material.

### Pick #1 scrutiny — Giants +1.5
Why it ranks first:
1. It captures every Giants win plus every one-run Cardinals win.
2. Liberatore's run prevention remains weak:
   - 5.53 ERA
   - 1.486 WHIP
   - 4.71 FIP
   - 146 K / 52 BB in 143.1 IP
   - 1.7 HR/9
3. Molina's 5.24 ERA overstates his limited 2026 underlying line somewhat:
   - xERA 4.08
   - FIP 3.82
   - xFIP 4.44
   - 20.2% K
   - 5.3% BB
   but his sample is only 22.1 IP and his latest start produced 7 ER in 3.0 IP.
4. The Cardinals are stronger against RHP than the Giants are against LHP, but neither split supports assuming a blowout:
   - STL OPS vs RHP: .696 season, .710 last 30 days.
   - SF OPS vs LHP: about .667 season, .663 last 30 days.
5. Busch Stadium is run suppressive in the 2024-26 Statcast window (run factor ~94; HR factor notably below average), helping the one-run/close-game branch.
6. St. Louis has home last bat, which improves its outright win probability but also creates many one-run home-win outcomes that still cash SF +1.5.

Opposing evidence:
- Giants are heavily injury-depleted.
- Rafael Devers is out for the season; Willy Adames, Matt Chapman, Harrison Bader and other regulars are on the IL.
- Giants' current lefty split is weak.
- Wetherholt has been activated for St. Louis and could strengthen the lineup if he starts.
- Molina's small-sample exit distribution remains wide; another early hook materially raises the STL 2+ margin branch.

Conclusion: **Cardinals are the slight winner preference, but Giants +1.5 is the stronger exact contract.**

### Anthony Molina
2026:
- 3-1
- 5.24 ERA
- 1.25 WHIP
- 22.1 IP
- 19 K
- 20.2% K
- 5.3% BB
- 4.08 xERA
- 3.82 FIP
- 4.44 xFIP
- 96.2 mph fastball average

Recent starts:
- Sep 11 vs SD: 3.0 IP, 9 H, 7 ER, 2 BB, 4 K
- Sep 5 at NYM: 5.0 IP, 1 H, 0 ER, 1 BB, 6 K
- Aug 31 at ATL: 5.0 IP, 6 H, 3 ER, 0 BB, 6 K
- Aug 25 vs CIN: 4.1 IP, 1 H, 0 ER, 1 BB

Interpretation: wide small-sample mixture. One disastrous start does not erase the better FIP/xERA branch, but neither do three good starts remove the early-hook/contact tail.

### Matthew Liberatore
Current 2026 official line:
- 5-14
- 5.53 ERA
- 143.1 IP
- 161 H
- 88 ER
- 27 HR
- 52 BB
- 146 K
- 1.486 WHIP
- 4.71 FIP

Recent starts:
- Sep 11 vs CWS: 4.1 IP, 6 H, 2 ER, 3 BB, 2 K, 2 HR
- Sep 5 at COL: 4.1 IP, 4 H, 5 ER, 2 BB, 3 K
- Aug 30 vs PIT: 5.2 IP, 6 H, 3 ER, 2 BB, 9 K
- Aug 25 vs BAL: 4.0 IP, 9 H, 8 ER, 1 BB, 7 K

Interpretation: strikeout ability survives, but contact, HR and short-start risk remain significant.

### Platoon/offensive context
**Giants vs LHP**
- 2026 OPS: ~.667
- last 30 days: .663
- last-30-day AVG/OBP/SLG: .209/.277/.386

**Cardinals vs RHP**
- 2026 OPS: .696
- last 30 days: .710
- last-30-day AVG/OBP/SLG: .256/.320/.390

This is a modest STL matchup advantage, not an overwhelming one.

### Current roster / injury context
**Giants**
- Rafael Devers: season-ending core surgery / 60-day IL.
- Willy Adames: IL.
- Matt Chapman: IL.
- Harrison Bader: IL.
- Casey Schmitt and other regulars also unavailable.
- The current offense contains numerous rookies/call-ups.

**Cardinals**
- JJ Wetherholt activated from the IL for the series finale; exact starting status unresolved because the lineup was still TBD.
- Masyn Winn recently returned from IL.
- Blaze Jordan remains out.
- Peter Strzelecki remains on IL/rehab path.
- Jordan Walker had recent ankle soreness but was expected to play.

### Recent series / offense
Series so far:
- Sep 14: STL 2, SF 1
- Sep 15: SF 10, STL 3

The 10-3 result is **not** treated as a continuation trend.

Useful current mechanisms:
- Bryce Eldridge hit a 461-foot HR and is an active power threat.
- Alec Burleson remains hot; MLB's current preview notes a .325/.426/.550 line over his recent 47 PA.
- The Giants' replacement-heavy lineup has shown both very low and explosive scoring states in consecutive games.

### Bullpen availability
- SF starter Blade Tidwell worked 6.2 IP Tuesday, so the Giants needed only 2.1 bullpen innings; broad relief workload was relatively light.
- STL starter Andre Pallante worked 5.0 IP. St. Louis used middle/low-leverage relief in the blowout; primary late-inning arms had worked in Monday's 2-1 win but were not all required Tuesday.
- St. Louis' bullpen has been a season-long weakness by advanced measures, with poor walk rate/strand performance in current reporting.
- Workload is used only to estimate availability, not assumed performance.

### Total 8.0 geometry
Integer total:
- Over 8.0 win: **45%**
- Exactly 8: **13% push**
- Under 8.0 win: **42%**

Why Over is preferred:
- both starters carry short-start / contact-cluster risk;
- Liberatore's 1.7 HR/9 and current short outings widen the SF scoring tail;
- Molina's latest 7-ER start keeps the STL cluster branch large;
- St. Louis' bullpen quality creates late-run exposure;
- hot game-time conditions can aid carry.

Why Under remains close:
- Giants are weak vs LHP and heavily depleted;
- Busch Stadium suppresses runs/HR relative to league average;
- Cardinals are only around a .696 season OPS vs RHP;
- both bullpens enter without extreme previous-night volume;
- no strong wind/rain mechanism points clearly upward.

### Park / weather
**Busch Stadium**
- 2024-26 Statcast run factor: ~94
- HR factor: below average

**Game-window weather**
- around 31-36°C / very hot
- humid
- ~20% precipitation risk around early innings
- partly sunny/intermittent cloud

Weather is not assigned an automatic Over sign. Heat may increase carry while Busch dimensions and HR factor suppress it; rain/delay remains a starter-disruption branch.

### Upset / trend-break branches
1. Molina rebounds toward his 3.82 FIP / 4.08 xERA process and STL's offense stays modest.
2. Molina repeats the San Diego early-hook state and STL creates a multi-run win.
3. Liberatore's HR/contact issues recur despite SF's weak LHP split.
4. Giants' rookie-heavy offense repeats Tuesday's power cluster.
5. Wetherholt's return meaningfully improves STL's lineup.
6. St. Louis bullpen leakage turns a lead into a one-run game or SF win.
7. Hot-weather carry offsets Busch's suppressive park profile.
8. Eight-run exact total lands on the push state.

### Settlement routes
- MLB official GameDay / StatsAPI final for score.
- Run line includes eligible extra innings under standard MLB settlement unless operator rules say otherwise.
- Total 8.0 includes eligible extra innings under standard settlement; exactly 8 = push.
- Operator-specific listed-pitcher/action terms were not supplied and remain `UNKNOWN_DEFINITION`.

### Material sources
1. MLB probable pitchers:
   https://www.mlb.com/probable-pitchers
2. Giants probable pitchers:
   https://www.mlb.com/giants/roster/probable-pitchers
3. Cardinals probable pitchers:
   https://www.mlb.com/cardinals/roster/probable-pitchers
4. MLB starting lineups:
   https://www.mlb.com/starting-lineups
5. Anthony Molina — MLB / Pitcher List / Baseball Savant current data.
6. Matthew Liberatore — Baseball-Reference / Pitcher List current data.
7. StatMuse — SF vs LHP and STL vs RHP current splits.
8. MLB Giants injury/news pages.
9. MLB Cardinals injury/transaction pages.
10. Reuters/MLB game reports for Sep. 14-15 series context.
11. Baseball Savant park factors:
    https://baseballsavant.mlb.com/leaderboard/statcast-park-factors
12. Busch Stadium venue-local weather source.
13. Read-only Google Drive:
    `METHOD.md`, `RULES_GENERAL.md`, `RULES_BASEBALL.md`, `CONTROLS.md`, `SOURCES.md`, `PREDICTION_LOG_COMBINED_4.md`.

### Social / current-team-source check
Official team/MLB current pages were checked. Search-indexed X results did not surface a reliable fresh batting-order post before cutoff, and MLB's official lineup page remained TBD; therefore no social-media lineup was promoted to confirmed status.

### Current status
**OPEN / UNSETTLED — PREGAME AT ISSUE**

No retrospective or settlement performed.

### Document mapping
- Event card → `PREDICTION_LOG_COMBINED_4.md`
- Provisional ID/status → `GAME_LOG_STATUS_CURRENT.md`
- Baseball process/bullpen/weather controls → existing `RULES_BASEBALL.md`
- Any useful new source lane → `SOURCES.md` / `DATA_SOURCE_REGISTER.md`
- Future learning → P-443 retrospective block first

---

### Settlement and full retrospective — 2026-09-17

**Status:** `FINAL / SETTLED`  
**Official MLB final:** **Giants 6–5 Cardinals in 10 innings**. Regulation ended **4–4**; Drew Gilbert hit a two-run homer in the 10th. Anthony Molina delivered **5.2 scoreless innings**.

| Rank | Frozen contract | `p` (`UNVALIDATED_SUBJECTIVE`) | Result | Brier |
|---:|---|---:|---|---:|
| 1 | Giants +1.5 runs | 61% | **WIN** | 0.1521 |
| 2 | Combined Total Over 8.0 runs | 45% | **WIN** | 0.3025 |
| 3 | Combined Total Under 8.0 runs | 42% | **LOSS** | 0.1764 |
| 4 | Cardinals -1.5 runs | 39% | **LOSS** | 0.1521 |

**Projected winner:** Cardinals — **LOSS**.  
**Total endpoint note:** exactly eight runs after nine would have been a push; MLB automatic-runner extras lifted the final to 11, so Over 8.0 won.  
**Card mean Brier:** **0.1958**.  
**Rank-1:** WIN. **Hit@2:** YES. **Wins@2:** 2/2.

#### A/B. Pick review
R1 won outright. R2 only became a winning Over because extra innings moved the game from an 8-run regulation push to 11. Molina's rebound branch was much stronger than the card's central concern after his prior poor start.

#### C/D. Rank-1 and Top-two
Both won. R1 was correctly more robust than the Cardinals winner. R2's win is specifically an extras-state outcome and must not be misread as proof the nine-inning scoring centre was high.

#### E. O/U review
This is a textbook confirmation of baseball control 22: extra innings are a different rate environment. The regulation read landed exactly on the push boundary; the automatic runner then transformed the settlement.

#### F. What went right
The card explicitly retained Molina's good-start branch based on his better FIP/xERA and did not let one disastrous prior start own the forecast. That branch realised.

#### G. Validation
1. Official lineups: not posted at cutoff.
2. Bench/bullpen: broad state researched; exact late bullpen sequence not known.
3. Manager: not a primary missing pregame fact.
4. Injuries: major Giants depletion and Wetherholt return checked.
5. Sources: starter and injury sources were current; lineup confirmation weak.
6. Better source: MLB GameDay lineups and bullpen availability.
7. Blind spot: extra-inning reach probability may have been too implicit.
8. Future: print tie-after-nine mass beside integer totals.

**Three-question retrospective**
1. Driver: Molina's strong start kept SF live; late bullpen/error states forced extras; automatic-runner inning produced the Over.
2. Knowable: all were plausible pregame branches; exact sequence not knowable.
3. Smallest change: quantify `P(tie after 9)` and extras contribution beside integer total.

**Sources**
- MLB Film Room: https://www.mlb.com/video/game/823004
- Reuters/AP contemporary recap of Giants 6–5 Cardinals.


---

## P-444 [PROVISIONAL] — New York Yankees @ Minnesota Twins

**Sport:** Baseball  
**Competition:** MLB 2026 regular season  
**Venue:** Target Field, Minneapolis, Minnesota  
**Scheduled start:** 16 Sep 2026 13:40 EDT / 12:40 CDT / 17 Sep 2026 03:40 AEST  
**Final pregame cutoff:** 17 Sep 2026, 03:30:48 AEST  
**State at cutoff:** **PREGAME / SCHEDULED**

### Frozen supplied markets
1. Twins +1.5
2. Yankees -1.5
3. Combined Total Over 8.0 Runs
4. Combined Total Under 8.0 Runs

### Starter identity handshake
- **NYY:** Carlos Rodón, LHP — `PROBABLE_OFFICIAL`
- **MIN:** Zebby Matthews, RHP — `PROBABLE_OFFICIAL`

MLB official probable-pitcher pages confirmed both starters. No scratch or bullpen-game replacement was verified before issue.

### Official batting orders
**MLB official lineup page remained `TBD` for both teams at final refresh.**

Therefore:
- no full projected order is treated as confirmed;
- lineup-slot exposure is widened;
- exact platoon stacking remains uncertain;
- side/total confidence is capped.

A current Yankees pregame report listed Aaron Judge expected back in the lineup after his Sept. 15 rest day, consistent with Aaron Boone's statement that the plan was to have Judge back on Sept. 16. This is treated as **high-quality projected availability**, not as an officially posted batting order.

### Ranked prediction

| Rank | Exact contract | Win probability | Push | Evidence |
|---:|---|---:|---:|---|
| **1** | **Yankees -1.5 runs** | **56%** | 0% | Strongest supplied contract |
| **2** | **Combined Total Under 8.0** | **46%** | **13%** | Moderate / Rodón-led |
| **3** | **Twins +1.5 runs** | **44%** | 0% | Live cushion branch |
| **4** | **Combined Total Over 8.0** | **41%** | **13%** | Upper-tail but subordinate |

Probability tier: `UNVALIDATED_SUBJECTIVE`.

**NO VALUE DETERMINABLE** because no validated predictive model plus same-time price snapshot is available.

### Projected game winner
**New York Yankees**
- Yankees win: **69%**
- Twins win: **31%**

Margin decomposition:
- Twins outright win: **31%**
- Yankees by exactly 1: **13%**
- Yankees by 2+ runs: **56%**

Representative central score: **Yankees 5, Twins 2**.

### Pick #1 scrutiny — Yankees -1.5
This is the strongest supplied contract because multiple independent mechanisms point toward Yankees separation rather than merely a New York win.

#### Starter quality gap
**Carlos Rodón, 2026**
- 6-3
- 2.94 ERA
- 70.1 IP
- 1.12 WHIP
- 78 K
- 26.9% K
- 12.1% BB
- 0.77 HR/9
- 3.56-3.57 FIP
- Statcast: .217 xBA, .340 xSLG, .300 xwOBA, 38.9% hard-hit, 6.4% barrels

Recent:
- Sep. 11 vs NYM: 6.1 IP, 3 H, 1 ER, 1 BB, 8 K
- Sep. 5 @ SD: 5.0 IP, 2 H, 1 ER, 3 BB, 7 K
- September: 11.1 IP, 2 ER, 15 K

**Zebby Matthews, 2026**
- 9-10
- 4.98 ERA
- 119.1 IP
- 1.27 WHIP
- 99 K
- 19.8% K
- 7.4% BB
- 1.73 HR/9
- 4.97 FIP
- 4.65 xERA
- .255 xBA / .438 xSLG / .330 xwOBA
- 41.7% hard-hit
- 11.1% barrels

Recent:
- Sep. 9 @ DET: 2.1 IP, 2 H, 5 ER, 4 BB, 2 K
- Sep. 4 @ CHW: 5.0 IP, 4 H, 4 ER, 1 BB, 4 K, 3 HR
- September: 7.1 IP, 9 ER, 4 HR, 5 BB

The Drive's current-regime rule prevents those two Matthews starts from replacing his season prior, but his season ERA/FIP/xERA all already sit near five, so the recent branch is directionally consistent rather than a lone outlier.

#### Platoon split
**Yankees vs RHP**
- 2026 OPS: **.715**
- last 30 days: **~.726**

**Twins vs LHP**
- 2026 OPS: **.676**
- last 30 days: **.613**

That is a material matchup advantage for Rodón/New York.

#### Current personnel
**Minnesota**
- Byron Buxton: season over, right hip surgery.
- Kaelen Culpepper: day-to-day with left hamstring tightness after leaving Sept. 15; MRI status unresolved at issue.
- Trevor Larnach: day-to-day with right wrist soreness.
- Exact batting order remained unposted.

**New York**
- Jazz Chisholm Jr.: 10-day IL, right thumb sprain.
- Trent Grisham: IL, right hamstring strain.
- Aaron Judge: activated Sept. 7; rested Sept. 15. Boone said the plan was to have him back Sept. 16.
- Judge's exact lineup slot remained unofficial because MLB's lineup page was still TBD.

#### Bullpen state
The Yankees enter with a favourable immediate workload state:
- Max Fried threw 7.0 innings Tuesday.
- Ryan Yarbrough covered the final 2.0 scoreless innings.
- New York's primary late-inning arms were therefore largely spared Tuesday after heavier use Monday.

Minnesota:
- Bailey Ober lasted 5.1 innings Tuesday.
- The Twins covered the final 3.2 innings with relief.
- Taylor Rogers was hit during the sixth-inning rally.
- Andrew Morris also appeared after being charged with three runs in only 0.1 inning Monday, creating a two-day usage concern for that branch of the relief chain.

Workload is treated as an **availability** input, not as automatic performance.

#### Main opposing evidence
- Matthews has been much better at home than on the road in 2026; StatMuse lists a **2.84 home ERA** versus 6.93 away.
- Target Field's three-year Statcast run factor is above average.
- Yankees' official batting order had not posted, and Judge is still being managed after a long rib-injury absence.
- Rodón's 12.1% walk rate creates baserunner/cluster risk despite elite run prevention.
- A 3-2 or 4-3 Yankees win loses -1.5 while still validating the winner read.

Conclusion: New York is the stronger outright side and the 2+ run branch is slightly more likely than every Twins +1.5 state combined, but the line is not treated as a lock.

### Total 8.0 geometry
Integer total:
- **Under 8.0 win:** 46%
- **Exactly 8:** 13% push
- **Over 8.0 win:** 41%

#### Why Under ranks #2
- Rodón has allowed only two earned runs in 11.1 September innings.
- Minnesota has a .613 OPS vs LHP over the last 30 days.
- Buxton is out and Culpepper/Larnach availability is uncertain.
- Yankees' high-leverage bullpen is relatively fresh after Fried + Yarbrough covered all nine innings Tuesday.
- Game-time weather is mild with no meaningful rain risk and only light wind.

#### Why the upper tail remains substantial
- Matthews has a 4.97 FIP, 4.65 xERA and 1.73 HR/9.
- New York scored eight runs in each of the first two games of the series.
- Those scores are not used as a trend by themselves, but the active mechanism is a favourable Yankees-vs-Matthews/middle-relief matchup.
- Target Field's 2024-26 Statcast run factor is **106**, although the HR factor is only **94**, so the park can inflate run production without being an extreme HR venue.
- Minnesota's relief chain has more immediate two-day workload than New York's.
- MLB extra innings use the automatic runner, creating a higher-run-rate tie-after-nine state.

### Recent series context
- Sep. 14: Yankees 8, Twins 3
- Sep. 15: Yankees 8, Twins 1

Per Drive rules, those finals are **context, not a causal continuation signal**.

Current mechanisms carried forward:
- Yankees bullpen freshness after Fried/Yarbrough Tuesday.
- Twins bullpen workload and Morris' consecutive-day exposure.
- Minnesota's current injury state.
- Judge expected back after a planned rest day.
- Matthews' current September pitching regime.

### Park / environment
**Target Field Statcast 2024-26**
- overall park factor: 103
- runs: **106**
- HR: **94**

**Game-window weather**
- ~22-23°C
- partly sunny / increasing clouds
- light ESE/SE wind around 5-10 km/h
- essentially no precipitation risk during the game window

No strong weather-direction adjustment is applied.

### Upset / trend-break branches
1. Matthews reverts to his strong home form and contains NYY.
2. Rodón's walk rate creates a clustered Minnesota inning despite weak LHP splits.
3. Judge returns but is still below peak timing after the long IL absence.
4. Matthews' HR/contact issues continue and NYY opens a multi-run lead.
5. Minnesota bullpen workload creates late separation.
6. Culpepper/Larnach unexpectedly start at full effectiveness and improve Minnesota's offense.
7. Target Field's run-friendly non-HR profile lifts BABIP/doubles scoring.
8. Tie-after-nine automatic-runner state breaks an otherwise low-total read.

### Settlement routes
- MLB GameDay / StatsAPI official final.
- Run line includes eligible extra innings under standard MLB settlement unless operator rules say otherwise.
- Total 8.0 includes eligible extra innings; exactly 8 = push.
- User did not supply listed-pitcher/action rules, so operator-specific action remains `UNKNOWN_DEFINITION`.

### Material sources
1. MLB probable pitchers:
   https://www.mlb.com/probable-pitchers
2. Twins probable pitchers:
   https://www.mlb.com/twins/roster/probable-pitchers
3. Yankees probable pitchers:
   https://www.mlb.com/yankees/roster/probable-pitchers
4. MLB starting lineups:
   https://www.mlb.com/starting-lineups
5. Baseball Savant — Carlos Rodón:
   https://baseballsavant.mlb.com/savant-player/carlos-rodon-607074
6. Baseball Savant — Zebby Matthews:
   https://baseballsavant.mlb.com/savant-player/zebby-matthews-805673
7. StatMuse — Rodón / Matthews current pitching metrics and team platoon splits.
8. MLB Yankees injury/roster pages.
9. MLB Twins injury/roster pages.
10. MLB Sept. 14 and Sept. 15 game records / Film Room.
11. Baseball Savant park factors:
    https://baseballsavant.mlb.com/leaderboard/statcast-park-factors
12. National Weather Service Minneapolis forecast.
13. Read-only Google Drive governing docs:
    `METHOD.md`, `RULES_GENERAL.md`, `RULES_BASEBALL.md`, `CONTROLS.md`, `SOURCES.md`, `PREDICTION_LOG_COMBINED_4.md`.

### Social / reporter / team-source check
- MLB Yankees beat coverage from Patrick Donnelly reported Aaron Boone planned to have Judge back in the lineup on Sept. 16 after resting him Sept. 15.
- A current Yankees pregame secondary report also listed Judge batting third, but because MLB's official lineup page still showed `TBD`, this was retained only as a projection.
- No indexed official Yankees/Twins social post with both confirmed batting orders was recovered before cutoff.

### Current status
**OPEN / UNSETTLED — PREGAME AT ISSUE**

No settlement or retrospective performed.

### Document mapping
- Event card → `PREDICTION_LOG_COMBINED_4.md`
- Provisional ID/status → `GAME_LOG_STATUS_CURRENT.md`
- Existing baseball starter/bullpen/platoon/park controls → `RULES_BASEBALL.md`
- Any useful new source lane → `SOURCES.md` / `DATA_SOURCE_REGISTER.md`
- Future learning → P-444 retrospective block first

---

### Settlement and full retrospective — 2026-09-17

**Status:** `FINAL / SETTLED`  
**Official MLB final:** **Twins 5–4 Yankees in 13 innings**. Regulation ended **2–2**. Carlos Rodón allowed two runs over six innings. Aaron Judge exited with lower-right-leg tightness. New York repeatedly left scoring opportunities unused before Minnesota walked it off in the 13th.

| Rank | Frozen contract | `p` (`UNVALIDATED_SUBJECTIVE`) | Result | Brier |
|---:|---|---:|---|---:|
| 1 | Yankees -1.5 runs | 56% | **LOSS** | 0.3136 |
| 2 | Combined Total Under 8.0 | 46% | **LOSS** | 0.2116 |
| 3 | Twins +1.5 runs | 44% | **WIN** | 0.3136 |
| 4 | Combined Total Over 8.0 | 41% | **WIN** | 0.3481 |

**Projected winner:** Yankees — **LOSS**.  
**Final total:** 9. Regulation total was 4; the Under loss was created by the extra-inning state.  
**Card mean Brier:** **0.2967**.  
**Rank-1:** LOSS. **Hit@2:** NO. **Wins@2:** 0/2. **Both Top 2:** NO.

#### A/B. Pick review
- **R1 NYY -1.5 — LOSS:** Matthews' strong-home branch realised, New York failed to separate, and Judge exited. Even after late rallies, the Yankees never produced a two-run final margin.
- **R2 U8 — LOSS:** the nine-inning thesis was actually low-scoring (2–2), but four extra frames plus the automatic runner pushed the final to nine.
- **R3 MIN +1.5 — WIN:** the exact close-game branch the card named became dominant.
- **R4 O8 — WIN:** only after extras.

#### C. Deep Rank-1 failure review
| Question | Finding |
|---|---|
| Why ranked first? | Rodón/Matthews season gap, Yankees-vs-RHP advantage, Twins-vs-LHP weakness and bullpen freshness all pointed toward NY separation. |
| Was it justified? | The Yankees were a defensible winner favourite, but **-1.5 at 56% was too strong relative to the card's own contrary evidence**: Matthews' 2.84 home ERA and a live 3–2/4–3 branch were explicitly acknowledged. |
| Should another row have ranked higher? | Twins +1.5 had a coherent home-Matthews/close-game case, but it was assigned only 44%. The pregame evidence justified a wider margin distribution than the final 56/44 split. |
| Missed/underweighted | Matthews home regime, the value of a close low-scoring state to +1.5, and the probability of reaching tied extras. |
| Unforeseen event | Judge's in-game leg tightness was not reasonably knowable pregame and should be treated as realised injury variance, not a sourcing failure. |
| Existing rule | `G-L12` favourite-separation/tail mass and baseball control 22 on extras should have constrained confidence. |
| Improvement | When a favourite side and Under share a “starter suppression/close game” state, quantify the contradiction: the Under can increase one-run/extras mass rather than automatically support -1.5. |

#### D. Top-two
Both failed, but for different settlement phases: R1 failed because the game stayed close; R2 was still winning through regulation and failed in extras. Their shared pregame issue was too little mass on **close game -> tie after nine -> automatic-runner extras**.

#### E. O/U
Do not grade this as a failed nine-inning run environment. Regulation produced only four runs. It is specifically an **extra-innings endpoint miss**, validating the rule that final-total contracts include a higher-rate extras branch.

#### F. What went right
Rodón's run-prevention case was accurate. The major mistake was margin/endpoint conversion, not the starting-pitcher read.

#### G. Validation
1. Starting lineups: MLB page still TBD at freeze; Judge expected return was high-quality projection.
2. Bench: incomplete.
3. Manager: Boone's Judge plan was captured.
4. Injuries: known pregame injuries checked; Judge's in-game tightness unforeseeable.
5. Sources: MLB/Savant/beat reporting were accurate.
6. Better source: official posted lineups if released in the final minutes.
7. Blind spot: Matthews home split and extras reach mass underweighted.
8. Future: run `G-L12` and `BB-B7` together for favourite -1.5 + low total cards.

**Three-question retrospective**
1. Driver: Matthews/home close-game performance, missed Yankees opportunities, then 13-inning variance.
2. Knowable: close/extras branch yes; Judge's in-game injury no.
3. Smallest change: quantify tie-after-nine and one-run margin mass before ranking a favourite run line #1.

**Sources**
- AP/CBS: https://www.cbsnews.com/minnesota/news/twins-vs-yankees-game-sept-16-2026/
- Contemporary Yankees recap documenting Judge exit and 13-inning missed opportunities.


---

## P-445 [PROVISIONAL] — Barbados Tridents vs Jamaica Kingsmen

**Sport:** Cricket  
**Competition:** Republic Bank Caribbean Premier League 2026  
**Stage:** Eliminator (3rd vs 4th)  
**Venue:** Kensington Oval, Bridgetown, Barbados  
**Scheduled start:** 16 Sep 2026 19:00 AST / 23:00 UTC / 17 Sep 2026 09:00 AEST  
**Frozen pregame cutoff:** **17 Sep 2026, 08:59:56 AEST**  
**State at cutoff:** **PREGAME / scheduled**  
**Format:** T20, scheduled 20 overs per side

### Contract identity / target gate
User supplied:
1. Jamaica Kingsmen first-innings 20-over runs O/U 157.5.
2. Jamaica Kingsmen first-six-overs runs O/U `455`, interpreted as **45.5** because the decimal is evidently missing.

The user defines “first innings” as the team batting first. A pre-first-ball toss/confirmed innings order was **not retrieved before the frozen cutoff**, so all Jamaica first-innings and Powerplay rows below are **conditional on Jamaica batting first**. If Barbados bats first, these exact targets are not silently transferred to Jamaica's second innings.

Operator-specific shortened-match/DLS action terms were not supplied, so settlement under a reduced innings remains `UNKNOWN_DEFINITION`.

### Pitch / conditions hard gate
**STRIP STATUS:** `NOT FOUND AFTER SEARCH` for a trustworthy exact-match men's strip report before cutoff.  
**MATCH CONDITIONS STATUS:** `OBSERVED / PARTIAL`.

Pitch-report ladder completed:
1. Windies Cricket/CPL official fixture and match-centre lanes: exact event/venue verified; no attributable exact-strip report or pre-cutoff toss retrieved.
2. Current broadcast/specialist match shells (Cricbuzz/FanCode): squads/event identity retrieved; no trustworthy pre-cutoff strip observation.
3. Kensington Oval pitch/curator search: historical venue context only; no current men's strip statement.
4. Exact-match specialist preview searches: no trustworthy attributable strip report; generic fantasy/tipping pitch pages excluded.
5. Same-day/recent venue evidence: WCPL playoff earlier Sep. 16 was rain-delayed and reduced to eight overs; recent men's Jamaica match had fast/bounce and pace/swing characteristics. This is adjacent/recent evidence, **not today's exact strip**.
6. ICC/official pitch-rating search: no current exact-match rating found.

Same-day official CPL report: overnight rain and early-morning showers delayed the WCPL playoff and reduced it to eight overs under cloudy conditions. Barbados Meteorological Services showed no current bulletin/warning in the retrieved current page. Evening drying remains possible; no exact rain percentage is invented.

### Current Kensington men's first-innings environment
Recent completed CPL first innings at Kensington:
- TKR 147/6
- Saint Lucia 138/6
- St Kitts & Nevis 118
- Jamaica 150/9
- Guyana 99

Mean: **130.4**; median: **138**; range: **99–150**. All five were below 157.5.

### Jamaica batting-first / Powerplay sample
Current 2026 examples:
- 117, PP 26/2
- 181, PP 42/3
- 169, PP 55/5
- 182, PP 42/2
- 159, PP 46/2
- 150, PP 50/1

Summary: first-innings mean **159.7**, median **164**; PP mean **43.5**, median **44**.  
Under 157.5 = 2/6; Under 169.5 = 4/6; PP Under 55.5 = 6/6; PP Over 34.5 = 5/6; supplied PP 45.5 = 3 over / 3 under.

### Frozen ranked picks — conditional on Jamaica batting first
| Rank | Exact selection | Probability | Evidence status |
|---:|---|---:|---|
| **1** | **Jamaica first 6 overs UNDER 55.5 runs** | **78%** | `FORCED_RANK / MEDIUM` |
| **2** | **Jamaica 1st innings UNDER 169.5 runs** | **74%** | `FORCED_RANK / MEDIUM` |
| **3** | **Jamaica first 6 overs OVER 34.5 runs** | **68%** | `FORCED_RANK / MEDIUM` |
| **4** | **Jamaica 1st innings UNDER 157.5 runs** | **60%** | `FORCED_RANK / MEDIUM` |

Probability tier: `UNVALIDATED_SUBJECTIVE`.  
**NO VALUE DETERMINABLE** without same-time prices and a validated model.

### Supplied-market assessment
**Jamaica 1st innings 157.5 — FORCED_PAIR**: Under 60% / Over 40%.  
**Jamaica first 6 overs 45.5 — FORCED_PAIR**: Under 52% / Over 48%.

The 45.5 line is not selected because the current Jamaica batting-first PP sample is exactly 3–3 around it, including 50/1 against Barbados at Kensington days earlier.

### Pick #1 scrutiny
Jamaica's six listed batting-first Powerplays were 26, 42, 55, 42, 46 and 50 — all below 55.5. Barbados also have active early-wicket mechanisms: AM Ghazanfar took three wickets in five balls in the third over against Guyana, who reached only 30/3 in the Powerplay. Against Jamaica, Barbados allowed 50/1 but recovered to hold them to 150/9.

Failure branch: Saim Ayub, if available, materially lifts the PP ceiling; Maaz Sadaqat scored 47 off 34 in the prior matchup; one 20+ run over can break U55.5 even without a collapse in wickets.

### Full-innings read
The Under 169.5 gets support from 4/6 Jamaica batting-first samples and 5/5 recent Kensington men's first innings. Under 157.5 is weaker because Jamaica's own batting-first sample is actually 4/6 **over** 157.5; the venue and Barbados bowling are what shift the current estimate toward the Under. Jamaica's 181/182 ceiling, Russell/Powell/Paul/Hassan finishing, and a possible Ayub return stay live as counter-branches.

### Latest squads / XI state
**Confirmed XIs at frozen cutoff:** `NOT RETRIEVED`.

Latest confirmed Jamaica XI against Barbados: Maaz Sadaqat, Kirk McKenzie, Keacy Carty, Usman Khan, Rovman Powell, Andre Russell, Hassan Khan, Keemo Paul, Odean Smith, Vitel Lawes, Hunain Shah.

Latest confirmed Barbados XI against Jamaica: Brandon King, Zachary Carter, Rivaldo Clarke, Quinton de Kock, Sadrack Descarte, Sherfane Rutherford, Chris Green, Daniel Sams, Gudakesh Motie, AM Ghazanfar, Jakeem Pollard.

Barbados changed their bowling combination in the next game, with Johann Layne and George Linde prominent against Guyana. CPL's max-four-overseas rule means the exact Sams/Linde/Mujeeb/Ghazanfar mix cannot be assumed before the XI.

### Availability
**Saim Ayub:** unresolved material availability. He starred with 102 earlier in CPL 2026, his return was delayed by Pakistan's Test in England, and he missed the previous Barbados game. No sufficiently authoritative pre-cutoff source confirmed him in today's XI. Two branches remain: Ayub plays (higher PP/full-innings ceiling) vs absent (latest Jamaica XI gets more weight).

No other current injury/rest absence was promoted without reliable confirmation.

### Recent form / H2H
Barbados entered on **four consecutive wins**, closing the group stage by dismissing Guyana for 99. They beat Jamaica twice in 2026: 206/3 vs 201/9 at Sabina Park, and 151/8 chasing Jamaica's 150/9 at Kensington. H2H is contextual only because the venue/run regimes were very different.

### Projected winner
**Barbados Tridents — 62% conditional completed-match preference**  
**Jamaica Kingsmen — 38%**

Barbados get home familiarity, current bowling form and four straight wins. The opposing branch is substantial: the prior Kensington meeting was decided off the last ball, Jamaica retain a higher batting ceiling than the venue sample implies, and toss/XI/strip were unresolved at cutoff.

### DLS / shortening branch
The same-day women's playoff was shortened to eight overs after rain. A reduced men's match could materially change phase rates and operator settlement. The probabilities above assume the stated contracts receive normal action under the user's operator terms; those terms were not supplied.

### Material sources
- Windies Cricket official fixture/results lanes.
- CPL official newsroom: `MOTIE MAGIC SEALS PLAYOFFS FOR TRIDENTS`; `TRIDENTS TURN UP THE HEAT WITH FOURTH STRAIGHT WIN`; same-day WCPL rain-shortened playoff report.
- Barbados Tridents official site / recent Jamaica match report.
- Cricbuzz current Eliminator squads.
- CricketWorld specialist scorecards for phase reconstruction.
- Jamaica Observer current playoff reporting / Rovman Powell comments.
- GeoSuper/current reporting on Saim Ayub's delayed return.
- Barbados Meteorological Services.
- Read-only Drive: `METHOD.md`, `RULES_GENERAL.md`, `RULES_CRICKET.md`, `LEAGUE_RULES_CRICKET.md`, `DATA_SOURCE_REGISTER.md`, `CONTROLS.md`, `SOURCES.md`, `PREDICTION_LOG_COMBINED_4.md`.

### Current status
**OPEN / UNSETTLED — PREGAME CARD FROZEN AT 08:59:56 AEST**

No settlement or retrospective performed.

### Document mapping
- Event card → `PREDICTION_LOG_COMBINED_4.md`
- Provisional ID/status → `GAME_LOG_STATUS_CURRENT.md`
- CPL rules → existing `LEAGUE_RULES_CRICKET.md`
- Exact strip/toss/XI missingness → P-445 event block
- Future learning → P-445 retrospective block first

---

### Settlement and retrospective — 2026-09-17

**Status:** `FINAL / CONDITION NOT MET — RANKED CONTRACTS NO ACTION / UNGRADED`  
**Final:** Barbados Tridents **144/6 (20)**; Jamaica Kingsmen **145/1 (14.1)**. Jamaica won by **9 wickets**.  
**Toss:** Jamaica won the toss and **elected to bowl**. Therefore **Barbados batted first**.

The original card explicitly froze every ranked Jamaica innings/Powerplay row as **conditional on Jamaica batting first**. That condition did not occur. Those rows are not transferred to Jamaica's chase and are not graded.

| Rank | Frozen conditional contract | Result |
|---:|---|---|
| 1 | Jamaica first 6 overs Under 55.5 | **NO ACTION / CONDITION NOT MET** |
| 2 | Jamaica first innings Under 169.5 | **NO ACTION / CONDITION NOT MET** |
| 3 | Jamaica first 6 overs Over 34.5 | **NO ACTION / CONDITION NOT MET** |
| 4 | Jamaica first innings Under 157.5 | **NO ACTION / CONDITION NOT MET** |

**Supplied Jamaica 157.5 and first-six 45.5 markets:** also **inactive under the frozen batting-first definition**.  
**Projected winner:** Barbados — **LOSS**; Jamaica won.  
**Brier:** none for the ranked rows because no ranked contract became active.

#### A. Prediction outcome
The ranked slate is an administrative no-action, not a 0–4 or 4–0 card. The independent projected winner lost.

#### B. Why the active winner call lost
Jamaica's bowling attack reduced Barbados to **24/4 in the Powerplay** before de Kock/Green recovered to 144/6. In the chase, Maaz Sadaqat made **112 off 49**, and Jamaica reached 145/1 in 14.1 overs. The major pregame unresolved player, **Saim Ayub, did play**, but Sadaqat was the decisive scorer.

#### C/D. Rank-1 / Top-two
Not applicable to performance scoring because the conditional target never activated. This is a process success: target identity prevented hindsight reassignment.

#### E. O/U review
Do **not** compare Jamaica's chase Powerplay of 79/0 or chase total to the batting-first contracts. Chase exposure is target-censored and tactically different. Barbados' first-innings Powerplay was 24/4, which is informative about conditions and Jamaica bowling but does not settle the frozen Jamaica targets.

#### F. What went right
The exact toss/innings-order condition was frozen before play. That prevented a severe target-identity error.

#### G. Validation
1. Confirmed XIs pregame: no.
2. Bench/squad: latest XIs/squads retrieved, but not confirmed same-match.
3. Coaching: not the material target uncertainty.
4. Availability: Saim Ayub remained unresolved pregame; he ultimately played.
5. Sources: current venue/CPL evidence was useful, but toss/XI were missing at freeze.
6. Better source: toss + official scorecard immediately before/after issue window.
7. Blind spot: winner call overrated Barbados despite Jamaica's batting ceiling.
8. Future: preserve the current conditional-contract gate exactly; never convert first-innings targets into chase targets.

**Three-question retrospective**
1. Driver: Jamaica's new-ball collapse of Barbados and Sadaqat's dominant chase.
2. Knowable: Jamaica bowling strength and batting ceiling were knowable; exact Sadaqat century was not.
3. Smallest change: none to target identity; improve winner branch weighting only after toss/XI.

**Sources**
- CricketWorld scorecard: https://www.cricketworld.com/cricket/barbados-tridents-vs-jamaica-kingsmen/match/scorecard/98191
- Cricbuzz scorecard/match info confirming toss and playing XIs.


---

## P-446 [PROVISIONAL] — Atlanta Braves @ Chicago Cubs

**Sport:** Baseball  
**Competition:** MLB 2026 regular season  
**Venue:** Wrigley Field, Chicago, Illinois  
**Scheduled start:** 16 Sep 2026 19:40 EDT / 18:40 CDT / 17 Sep 2026 09:40 AEST  
**State at final pregame research:** **PREGAME / warmup / scheduled**  
**Starters:** JR Ritchie (RHP) vs Shota Imanaga (LHP)

### Supplied markets
1. Braves +1.5
2. Cubs -1.5
3. Combined Total Over 7.5
4. Combined Total Under 7.5

### Ranked forecast

| Rank | Exact contract | Probability | Evidence |
|---:|---|---:|---|
| **1** | **Cubs -1.5 runs** | **56%** | Strongest supplied contract |
| **2** | **Combined Total Under 7.5 runs** | **53%** | Moderate |
| **3** | **Combined Total Over 7.5 runs** | **47%** | Moderate / upper-tail |
| **4** | **Braves +1.5 runs** | **44%** | Live but subordinate |

Probability tier: `UNVALIDATED_SUBJECTIVE`.  
**NO VALUE DETERMINABLE** without same-time price capture and a validated model.

### Projected winner
**Chicago Cubs**
- Cubs win: **66%**
- Braves win: **34%**
- Representative central score: **Cubs 5, Braves 2**

### Starter identity / role
**JR Ritchie — Atlanta**
- Official probable starter.
- 2026 MLB: 1-2, 4.50 ERA, 58.0 IP, 53 K, 1.43 WHIP.
- FIP: **5.41**
- BB%: **14.1%**
- K%: **20.7%**
- HR/9: **1.40**
- xERA: ~**4.43**
- Returned from Triple-A after Reynaldo López was placed on the IL.
- Current reporting says Atlanta is using Ritchie rather than Chris Sale, effectively giving Sale extra rest.
- Recent Triple-A reporting credited Ritchie with 24 K and 3 BB over his last two starts, so an improved-command branch is retained.

**Shota Imanaga — Chicago**
- Official probable starter.
- 2026: 10-10, 3.88 ERA, 162.1 IP, 156 K, 1.12 WHIP.
- Current FIP: ~**4.69-4.70**
- K%: **23.6%**
- BB%: **5.6%**
- HR/9: **1.89**
- Last three: 6 IP/2 ER vs PIT; 6 IP/1 ER at MIA; 5 IP/6 ER vs CIN.
- Recent pitching-report analysis noted a change away from four-seam reliance toward more splitter usage after a home-run-heavy stretch.

### Current lineups
MLB's generic starting-lineup page lagged during the research pass, but multiple current pregame reporting sources converged on the following actual lineups:

**Atlanta**
1. Ronald Acuña Jr. RF
2. Drake Baldwin DH
3. Matt Olson 1B
4. Ozzie Albies 2B
5. Michael Harris II CF
6. Mauricio Dubón LF
7. Austin Riley 3B
8. Sean Murphy C
9. Ha-Seong Kim SS

**Chicago**
1. Pete Crow-Armstrong CF
2. Seiya Suzuki RF
3. Michael Busch 1B
4. Alex Bregman 3B
5. Ian Happ LF
6. Nico Hoerner SS
7. Michael Conforto DH
8. Pedro Ramírez 2B
9. Carson Kelly C

These were treated as **reported current lineups**, not upgraded to official-MLB-lineup-page confirmation where that page still lagged.

### Injuries / unavailable players

**Atlanta**
- Reynaldo López: 15-day IL, right shoulder inflammation; Ritchie recalled in corresponding move.
- Lane Thomas: 10-day IL, strained left intercostal.
- Bryce Elder: 15-day IL after right knee procedure.
- Robert Suarez: 60-day IL, right elbow inflammation.
- Joe Jiménez: rehab assignment after multiple knee surgeries; not available as a normal late-inning arm.

**Chicago**
- Dansby Swanson: IL with left side/oblique strain; targeted for return around Sep. 18.
- Trent Thornton: 15-day IL, left ankle sprain.
- Justin Steele: 60-day IL, elbow flexor strain; rehab progression.
- Ian Happ returned to the lineup after recent knee discomfort/scratch.

### Platoon / offensive split
**Atlanta vs LHP**
- Season OPS: **.697**
- Last 30 days OPS: **.581**, lowest in MLB over that window.
- Last-30-day slash vs LHP: approximately .220/.277/.304.

**Chicago vs RHP**
- Season OPS: **.756**
- Last 30 days OPS: **.838**
- Last-30-day slash: roughly .272/.355/.483.

This is the largest lineup-level matchup edge in the card and strongly supports Chicago's side.

### Pick #1 scrutiny — Cubs -1.5
Support:
1. Large starter command/underlying gap: Ritchie 14.1% BB and 5.41 FIP vs Imanaga 5.6% BB and 1.12 WHIP.
2. Cubs are scorching RHP over the last month (.838 OPS).
3. Braves are MLB's weakest team vs LHP over the same window (.581 OPS).
4. Wrigley wind was reported around **8 mph in from left field**, which suppresses one of Imanaga's principal weakness branches: home runs.
5. Atlanta is starting Ritchie after recalling him to replace injured Reynaldo López while preserving Chris Sale for later.
6. Chicago bats last, so lead/margin states have home-game asymmetry.

Opposing evidence:
- Ritchie has a small MLB sample and a meaningful improved-command Triple-A branch.
- He previously held the Cubs to 1 run in 4.1 IP in May; contextual only.
- Atlanta has real power and hit three two-run homers in Tuesday's 6-3 win.
- The Cubs bullpen has been volatile and was damaged Tuesday.
- Imanaga's season FIP (~4.70) is worse than his ERA and he has allowed 34 HR.

Margin estimate:
- Braves outright win: ~34%
- Cubs by exactly 1: ~10%
- Cubs by 2+: **56%**

### Total 7.5
**Under 7.5: 53%**  
**Over 7.5: 47%**

#### Under mechanisms
- Braves' extreme recent weakness vs LHP.
- Imanaga's last two starts: 12 IP, 3 ER.
- Wind reported in from LF around 8 mph.
- NWS forecast around first pitch: ~69°F, NNE wind ~8 mph, high humidity, ~26% rain chance.
- Wrigley 2024-26 Statcast run factor ~94, though HR factor is closer to/above neutral.

#### Over mechanisms
- Ritchie's 5.41 FIP, 14.1% BB and short-start/early-hook distribution.
- Cubs .838 OPS vs RHP over the last 30 days.
- Chicago bullpen volatility.
- Atlanta's power remains real despite weak lefty split.
- Rain/delay risk can disrupt starter length.
- MLB extra-inning automatic-runner state widens the upper total tail if tied after nine.

### Bullpen state
**Atlanta**
- Martín Pérez gave 6 innings Tuesday; Atlanta needed only 3 relief innings.
- Raisel Iglesias worked 1 inning for the save Tuesday.
- Atlanta had much heavier bullpen exposure Monday because López lasted only 3 innings.
- Two-day workload is therefore mixed, not fully fresh.

**Chicago**
- Kevin Gausman went 5.2 innings Tuesday.
- Jacob Webb allowed the go-ahead two-run HR and recorded only two outs.
- Edward Cabrera allowed another two-run HR in the ninth.
- Chicago's relief chain therefore enters with both workload and performance uncertainty.
- Monday required multiple relievers after David Peterson's six innings.

Workload controls availability, not assumed performance.

### Recent series context
- Sep. 14: Cubs 7, Braves 3
- Sep. 15: Braves 6, Cubs 3

These results are **not** treated as continuation signals.

Active mechanisms carried forward:
- Cubs bullpen instability.
- Atlanta's current power.
- Ritchie's recall and López injury.
- Imanaga's recent pitching-mix adjustment.
- Current Wrigley wind/conditions.

### Park / weather
**Wrigley Field**
- 2024-26 Statcast overall park factor: ~97.
- Run factor: ~94.
- HR factor: ~107.

**Current evening conditions**
- roughly 68-69°F / 20-21°C.
- NNE wind about 8 mph, reported **in from LF**.
- humidity >90%.
- precipitation probability around 25-30% through early/mid game.
- thunder risk rises later overnight.

No automatic weather total sign is applied; wind-in is specifically used as a home-run suppression mechanism, while rain remains a delay/starter-transition branch.

### Upset / trend-break branches
1. Ritchie carries his Triple-A command improvement back to MLB.
2. Atlanta's Acuña/Olson/Albies/Baldwin power breaks through Imanaga despite the LHP split and wind.
3. Imanaga's HR problem resurfaces despite the wind.
4. Chicago's bullpen again gives away a multi-run lead.
5. Ritchie walks multiple hitters and the Cubs' patient RHP-dominant lineup turns the game into an early-hook state.
6. Rain delay shortens one or both starter exposures.
7. Low-scoring starter phase flips to a higher-scoring relief phase.

### Settlement
- MLB GameDay / StatsAPI official final.
- Run line includes eligible extra innings under standard settlement unless operator-specific terms differ.
- Total 7.5 has no push under normal scoring.
- User did not supply listed-pitcher/action terms; operator-specific action remains `UNKNOWN_DEFINITION`.

### Material sources
- MLB schedule / probable pitchers / scoreboard.
- MLB team transaction and injury pages.
- Baseball-Reference current season FIP/standard lines.
- Baseball Savant current JR Ritchie / Wrigley park data.
- StatMuse platoon splits.
- MLB game stories/Film Room for Sep. 14-15 bullpen and scoring state.
- National Weather Service Chicago hourly forecast.
- Current Braves and Cubs pregame reporting for lineups and Ritchie's role.
- Read-only Google Drive `METHOD.md`, `RULES_GENERAL.md`, `RULES_BASEBALL.md`, `CONTROLS.md`, `SOURCES.md`, `PREDICTION_LOG_COMBINED_4.md`.

### Social / reporter check
Official team X search did not surface a reliably indexed same-day lineup post through search. Current Braves/Cubs beat-style sources and multiple lineup aggregators converged on the same batting orders. Those lineups were used as **current reported**, not falsely labeled as official MLB confirmation where the generic MLB lineup page lagged.

### Current status
**OPEN / UNSETTLED — PREGAME**

No retrospective or settlement performed.

### Document mapping
- Event card → `PREDICTION_LOG_COMBINED_4.md`
- Provisional ID/status → `GAME_LOG_STATUS_CURRENT.md`
- Existing baseball starter/platoon/bullpen/weather controls → `RULES_BASEBALL.md`
- Any new durable source lane → `SOURCES.md` / `DATA_SOURCE_REGISTER.md`
- Future learning → P-446 retrospective block first

---

### Settlement and full retrospective — 2026-09-17

**Status:** `FINAL / SETTLED`  
**Official MLB final:** **Cubs 8–4 Braves**. Shota Imanaga allowed one run over six innings; J.R. Ritchie allowed six runs over 4.2 innings. Pete Crow-Armstrong homered twice; Alex Bregman homered and drove in four.

| Rank | Frozen contract | `p` (`UNVALIDATED_SUBJECTIVE`) | Result | Brier |
|---:|---|---:|---|---:|
| 1 | Cubs -1.5 runs | 56% | **WIN** | 0.1936 |
| 2 | Combined Total Under 7.5 runs | 53% | **LOSS** | 0.2809 |
| 3 | Combined Total Over 7.5 runs | 47% | **WIN** | 0.2809 |
| 4 | Braves +1.5 runs | 44% | **LOSS** | 0.1936 |

**Projected winner:** Cubs — **WIN**.  
**Card mean Brier:** **0.2373**.  
**Rank-1:** WIN. **Hit@2:** YES. **Wins@2:** 1/2.

#### B. Why
R1 correctly identified the starter/platoon separation: Chicago's strong current RHP production met Ritchie's walk/FIP/short-start risk, while Imanaga controlled Atlanta. The Under failed because the same Chicago separation branch plus four Atlanta runs generated 12 total.

#### C/D. Rank-1/Top-two
R1 won; R2 lost. The ranking correctly prioritised margin over total, but the top-two shared-state audit should have made clear that **Cubs offensive dominance can win -1.5 while simultaneously defeating the Under**.

#### E. O/U
Wind-in suppressed one HR mechanism but did not neutralise Ritchie's contact/command tail or Chicago's ability to score through multiple paths. Weather should remain mechanism-specific, not a total override.

#### F. What went right
The current platoon data (.838 Cubs OPS vs RHP, Atlanta .581 vs LHP in the rolling sample) and Ritchie's 5.41 FIP/14.1% BB were high-value current mechanisms.

#### G. Validation
1. Lineups: reported/current but not fully field-owner-confirmed.
2. Bench: incomplete.
3. Manager/rotation: Ritchie/Sale rest decision captured.
4. Injuries: relevant IL changes captured.
5. Sources: starter/platoon/weather sources were useful.
6. Better: official MLB posted lineups near first pitch.
7. Blind spot: total allocation after a favourite-separation branch.
8. Future: use `G-L18` allocation marginals and explicit score examples for spread-total coupling.

**Three-question retrospective**
1. Driver: Chicago punished Ritchie while Imanaga controlled Atlanta.
2. Knowable: yes; this was the central side mechanism.
3. Smallest change: stronger coupling audit between favourite separation and total upper tail.

**Source**
- MLB game story: https://www.mlb.com/stories/game/824626


---

## P-447 [PROVISIONAL] — Boston Red Sox @ Texas Rangers

**Sport:** Baseball  
**Competition:** MLB 2026 regular season  
**Venue:** Globe Life Field, Arlington, Texas  
**Scheduled start:** 16 Sep 2026 20:05 EDT / 19:05 CDT / 17 Sep 2026 10:05 AEST  
**Final pregame cutoff:** 17 Sep 2026, 09:46:45 AEST  
**State at cutoff:** **PREGAME / SCHEDULED**

### Supplied markets
1. Rangers +1.5
2. Red Sox -1.5
3. Combined Total Over 8.0
4. Combined Total Under 8.0

### Starter identity handshake
- **BOS:** Jake Bennett, LHP — `PROBABLE_OFFICIAL`
- **TEX:** MacKenzie Gore, LHP — `PROBABLE_OFFICIAL`

MLB official probable-pitcher pages confirmed both starters before issue. No scratch or bullpen-game replacement was verified.

### Lineup state
**Boston official MLB lineup page:** still `TBD` at cutoff.  
**Texas:** current same-day Rangers reporting published a right-handed-heavy lineup:
1. Justin Foscue 2B
2. Corey Seager SS
3. Josh Jung 3B
4. Jake Burger 1B
5. Brandon Nimmo RF
6. Wyatt Langford LF
7. Ezequiel Duran CF
8. Elias Díaz DH
9. Danny Jansen C

Because MLB's generic field-owner lineup page was still lagging, Texas is stored as **current reported lineup**, not falsely upgraded to `CONFIRMED_OFFICIAL`. Boston player-level projections remain capped.

### Ranked forecast

| Rank | Exact contract | Win probability | Push | Evidence |
|---:|---|---:|---:|---|
| **1** | **Rangers +1.5 runs** | **66%** | 0% | Strongest supplied contract |
| **2** | **Combined Total Under 8.0 runs** | **44%** | **14%** | Moderate |
| **3** | **Combined Total Over 8.0 runs** | **42%** | **14%** | Moderate / upper-tail |
| **4** | **Red Sox -1.5 runs** | **34%** | 0% | Lowest supplied contract |

Probability tier: `UNVALIDATED_SUBJECTIVE`.  
**NO VALUE DETERMINABLE** without a validated model and same-time price capture.

### Projected game winner
**Texas Rangers**
- Texas win: **59%**
- Boston win: **41%**

Margin decomposition:
- Boston outright win: ~41%
- Texas by exactly 1: ~25%
- Texas by 2+: ~34%

Representative score corridor: **Texas 4-3 / 5-3**, with 4-4 through nine / exact-eight push states material.

### Pick #1 scrutiny — Rangers +1.5
The contract survives:
- every Texas win;
- every one-run Boston win.

#### Texas platoon edge
**Rangers vs LHP**
- Last 30 days OPS: **.869**, best in MLB.
- Last 30 days home OPS vs LHP: **.936**.
- Slash at home vs LHP over that window: roughly .323/.379/.556.

This is the strongest lineup-process signal in the matchup.

#### Boston recent LHP split
**Red Sox vs LHP**
- 2026 season OPS: **.748**.
- Last 30 days OPS: **.677**.
- Last-30-day road OPS vs LHP: **.673**.

Boston's season platoon profile remains respectable, but the current regime is notably weaker.

#### Jake Bennett
2026:
- 9-7
- 3.69 ERA
- 105.0 IP
- 1.07 WHIP
- 83 K / 19 BB
- 19.9% K
- 4.5% BB
- 1.03 HR/9
- **3.63 FIP**
- Road ERA: **3.19**

Recent:
- Sep. 9 vs LAA: 5.1 IP, 9 H, 6 ER, 1 BB, 2 K, 3 HR
- Sep. 3 at BAL: 6 IP, 3 ER, 7 K, 0 BB
- Aug. 29 at NYY: 6 IP, 0 ER, 7 K, 0 BB
- MLB preview: **5.26 ERA over his past seven starts**

Interpretation: Bennett's season process is real and his low walk rate is excellent. The Texas lean is therefore not based on calling him a poor pitcher; it comes from Texas' elite current LHP matchup and Bennett's wider recent HR/contact branch.

#### MacKenzie Gore
2026:
- 8-11
- 4.62 ERA
- 161.2 IP
- 1.35 WHIP
- 172 K / 66 BB
- 24.4% K
- 9.4% BB
- 1.00 HR/9
- **3.77 FIP**

Statcast current profile:
- xBA around .241
- xSLG around .379
- xwOBA around .309
- hard-hit ~40.7%
- barrel ~8.5%

Gore's ERA overstates the weakness of his underlying fielding-independent profile, although his walk rate remains a material downside.

#### Direct batter history
Baseball Savant current-roster sample vs Gore:
- 46 PA
- .385 AVG
- .459 wOBA
- .394 xwOBA

This is adverse for Gore but is a small, roster-dependent historical sample and does **not** override current team splits or season process.

Boston Globe reporting also notes Gore has a 1.46 ERA with 16 strikeouts in two starts against Boston, creating a contradictory H2H picture. Both samples are kept descriptive only.

#### Bullpen state
**Boston**
Tuesday relief workload after Patrick Sandoval lasted 2.2 IP:
- Brayan Bello: 1.2 IP
- Gamboa: 1.0
- Wyatt Olds: 0.2
- Jovani Morán: 2.0
- Primary high-leverage arms Garrett Whitlock and Aroldis Chapman were not required and are comparatively fresh.
- Boston relievers had allowed only five runs in 33 innings over their prior 10 games per current Boston reporting.

**Texas**
Tuesday after deGrom's 5 IP:
- Chase Silseth: 1.0
- Tyler Alexander: 1.0
- Robert Garcia: 0.1
- Jacob Latz: **1.2 IP / five-out save**
Latz's heavier usage slightly weakens today's late-game protection.

This is important contrary evidence to Rangers +1.5: Boston's best late arms are fresher than Texas' closer.

#### Injuries / availability
**Boston**
- Ceddanne Rafaela: 10-day IL, right quad strain.
- Anthony Seigler: 10-day IL, right wrist inflammation.
- Eli White: 10-day IL, right-foot ligament injury.
- Masataka Yoshida: IL, left hamstring strain.
- Garrett Crochet: 60-day IL, shoulder inflammation; not part of today's rotation.
- Justin Slaten: elbow injury, season over.
- Willson Contreras has been activated and was in the prior game's lineup.

**Texas**
- Joc Pederson: current MLB injury update lists a **left-hand fracture** from Sep. 12 HBP and he is not assumed available.
- Kyle Higashioka: IL / rehab, right flexor strain.
- Cole Winn: IL, rotator-cuff strain.
- Jack Leiter: 60-day IL / ankle surgery.
- Josh Jung was activated Sep. 12 and is back in the current reported lineup.
- Nathan Eovaldi was activated Sep. 12 but is not today's starter.

### Total 8.0 geometry
- **Under 8.0 win:** **44%**
- **Exactly 8:** **14% push**
- **Over 8.0 win:** **42%**

#### Under mechanisms
1. Globe Life Field is strongly run-suppressive in the 2024-26 Statcast window:
   - overall factor ~94
   - runs factor **88**
   - HR factor **94**
2. The retractable roof is likely to be closed because outside temperature is around 36°C near game time. Exact official roof status was not independently confirmed pregame, so this remains an expectation, not a fact.
3. Bennett owns a 3.63 FIP / 1.07 WHIP.
4. Gore's 3.77 FIP is materially better than his 4.62 ERA.
5. Boston's recent offense vs LHP is only .677 OPS.
6. Boston's high-leverage bullpen enters relatively fresh.

#### Over mechanisms
1. Texas has the best MLB OPS vs LHP over the last 30 days and .936 at home.
2. Bennett just allowed six runs and three HR in his latest start.
3. Gore's walk rate remains 9.4% and current Boston hitters have strong small-sample Statcast history against him.
4. Gore reportedly has allowed nine earned runs across his last seven innings.
5. Texas' closer Latz worked five outs Tuesday, widening the late-relief branch.
6. Extra innings use the automatic runner and materially raise the tie-after-nine scoring rate.

### Park / roof / weather
**Globe Life Field**
- Retractable roof.
- 2024-26 Statcast:
  - overall park factor ~94
  - runs **88**
  - HR **94**
- 2026 raw scoring has been higher recently, but the multi-year adjusted park remains suppressive.

**Outside game-window weather**
- ~36°C at 7 PM local, easing toward ~32-34°C later.
- clear/mostly clear.
- no meaningful rain risk in the retrieved forecast.

A same-day secondary weather source expected the roof closed due to heat. Last night's official box score also recorded **Roof Closed**, but that is only prior-game context; today's exact official roof call was not recovered before cutoff.

### Series / prior-game mechanism
Sep. 15: Rangers 4, Red Sox 2.

The final itself is not predictive. Current consequences:
- Boston middle/long relief worked 5.1 innings but top leverage was largely saved.
- Texas used four relievers and Latz for a five-out save.
- Texas' right-handed-heavy configuration vs a Boston lefty is retained today.
- Boston again faces a left-handed starter after struggling recently in that split.

### Upset / trend-break branches
1. Bennett returns to his season 3.63-FIP / low-walk profile and neutralizes Texas' LHP split.
2. Boston's strong season-long .748 OPS vs LHP matters more than its weak last-30-day split.
3. Gore's walks plus Boston's favorable small-sample BvP history create a multi-run inning.
4. Texas' Latz workload causes a late one-run loss or blown lead.
5. Bennett's recent HR/contact problems persist and Texas separates early.
6. Gore's ERA regresses toward his stronger FIP and suppresses Boston.
7. Roof status differs from expectation and slightly changes the park environment.
8. Tie-after-nine creates a high-run extra-inning state.

### Settlement
- MLB GameDay / StatsAPI official final.
- Run line includes eligible extras under standard MLB settlement unless operator rules differ.
- Total 8.0: exact eight is a push under standard settlement.
- Listed-pitcher/action terms were not supplied and remain `UNKNOWN_DEFINITION`.

### Material sources
1. MLB probable pitchers:
   https://www.mlb.com/probable-pitchers
2. Red Sox probable pitchers:
   https://www.mlb.com/redsox/roster/probable-pitchers
3. Rangers probable pitchers:
   https://www.mlb.com/rangers/roster/probable-pitchers
4. MLB starting lineups:
   https://www.mlb.com/starting-lineups
5. Baseball Savant probable-pitcher matchup / Gore Statcast profile.
6. StatMuse — Bennett/Gore season metrics and BOS/TEX LHP splits.
7. MLB Red Sox injury/transaction pages.
8. MLB Rangers injury/transaction pages and Kennedi Landry reporting.
9. MLB/Reuters Sep. 15 game recap.
10. Baseball Almanac exact Sep. 15 box score for bullpen workloads / roof state.
11. Baseball Savant Globe Life Field park factors.
12. Venue-local structured weather source.
13. Boston Globe current preview.
14. Lone Star Ball same-day Texas reported lineup.
15. Read-only Google Drive:
    `METHOD.md`, `RULES_GENERAL.md`, `RULES_BASEBALL.md`, `CONTROLS.md`, `SOURCES.md`, `PREDICTION_LOG_COMBINED_4.md`.

### Social / current reporting
- Same-day Rangers reporting published a right-handed-heavy lineup tailored to Bennett.
- Searches of indexed official Red Sox/Rangers social sources did not yield a trustworthy field-owner Boston lineup before the frozen cutoff.
- No post-first-pitch information is admitted into this forecast.

### Current status
**OPEN / UNSETTLED — PREGAME CARD FROZEN AT 09:46:45 AEST**

No retrospective or settlement performed.

### Document mapping
- Event card → `PREDICTION_LOG_COMBINED_4.md`
- Provisional ID/status → `GAME_LOG_STATUS_CURRENT.md`
- Existing baseball starter/platoon/bullpen/roof controls → `RULES_BASEBALL.md`
- Durable source lane, if later justified → `SOURCES.md` / `DATA_SOURCE_REGISTER.md`
- Future learning → P-447 retrospective block first

---

### Settlement and full retrospective — 2026-09-17

**Status:** `FINAL / SETTLED`  
**Official MLB final:** **Rangers 7–3 Red Sox**. Texas broke a 3–3 tie with three runs in the seventh and one in the eighth. MacKenzie Gore left after four-plus innings with back/under-shoulder muscle spasms; Nathan Eovaldi delivered four scoreless relief innings.

| Rank | Frozen contract | `p` (`UNVALIDATED_SUBJECTIVE`) | Result | Brier |
|---:|---|---:|---|---:|
| 1 | Rangers +1.5 runs | 66% | **WIN** | 0.1156 |
| 2 | Combined Total Under 8.0 runs | 44% | **LOSS** | 0.1936 |
| 3 | Combined Total Over 8.0 runs | 42% | **WIN** | 0.3364 |
| 4 | Red Sox -1.5 runs | 34% | **LOSS** | 0.1156 |

**Projected winner:** Texas — **WIN**.  
**Card mean Brier:** **0.1903**.  
**Rank-1:** WIN. **Hit@2:** YES. **Wins@2:** 1/2.

#### B. Why
Texas' elite recent LHP split translated into 13 hits. The Under failed because a tied game entered the Texas late-separation state. Gore's physical issue was unforeseen, but Eovaldi's four scoreless relief innings prevented it from becoming a Boston scoring tail.

#### C/D. Rank-1/Top-two
R1 won comfortably; R2 lost. The side read was more robust than the total because Texas could win a 7–3 type state even in a run-suppressive park.

#### E. O/U
The final reached 10 in regulation; this was **not** an overtime/extras issue. The key miss was underweighting Texas' lineup-vs-LHP ceiling and late scoring despite the park factor.

#### F. What went right
The card explicitly identified Texas' .869 recent OPS vs LHP as its strongest lineup signal and projected Texas as winner.

#### G. Validation
1. Boston official lineup: not recovered; Texas same-day lineup was reported, not field-owner confirmed.
2. Bench: incomplete.
3. Manager: current deployment context partially captured.
4. Injuries: major IL states checked; Gore's in-game spasms unforeseeable.
5. Sources: current Rangers reporting and MLB starter sources were useful.
6. Better: official MLB lineup/roof source at issue.
7. Blind spot: late Texas scoring ceiling vs Bennett/middle relief.
8. Future: when one offense has an extreme current platoon split, widen its team-score upper marginal even in a suppressive park.

**Three-question retrospective**
1. Driver: Texas sustained contact and a three-run seventh, then Eovaldi closed the game.
2. Knowable: Texas platoon advantage yes; Gore spasms no.
3. Smallest change: stronger team-score marginal under `G-L18`.

**Sources**
- AP/Washington Post recap, Rangers 7–3 Red Sox.
- MLB final highlight: https://www.mlb.com/rangers/video/caleb-durbin-lines-out-to-second-baseman-nicky-lopez


---

## P-448 [PROVISIONAL] — Kansas City Royals @ Houston Astros

**Sport:** Baseball  
**Competition:** MLB 2026 regular season  
**Venue:** Daikin Park, Houston, Texas  
**Scheduled start:** 16 Sep 2026 20:10 EDT / 19:10 CDT / 17 Sep 2026 10:10 AEST  
**Final pregame cutoff:** 17 Sep 2026, 09:58:42 AEST  
**State at cutoff:** **PREGAME / SCHEDULED**

### Supplied markets
1. Royals +1.5
2. Astros -1.5
3. Combined Total Over 9.0
4. Combined Total Under 9.0

### Starter identity handshake
- **KC:** Daniel Lynch IV, LHP — `PROBABLE_OFFICIAL`
- **HOU:** Cristian Javier, RHP — `PROBABLE_OFFICIAL`

MLB official probable-pitcher pages confirmed both starters before issue. No scratch/bullpen-game substitution was verified.

### Lineup state
MLB's generic starting-lineup page was still lagging at the final refresh. Current team/community game threads indicated normal pregame status, but no field-owner batting order was recovered before cutoff.

Therefore:
- no projected nine-man order is called official;
- exact lineup-slot exposure is widened;
- no player-prop row is issued;
- side/total probabilities retain lineup uncertainty.

### Ranked forecast

| Rank | Exact contract | Win probability | Push | Evidence |
|---:|---|---:|---:|---|
| **1** | **Royals +1.5 runs** | **65%** | 0% | Strongest supplied contract |
| **2** | **Combined Total Under 9.0 runs** | **49%** | **15%** | Moderate |
| **3** | **Combined Total Over 9.0 runs** | **36%** | **15%** | Upper-tail but subordinate |
| **4** | **Astros -1.5 runs** | **35%** | 0% | Lowest supplied contract |

Probability tier: `UNVALIDATED_SUBJECTIVE`.  
**NO VALUE DETERMINABLE** without a validated model plus same-time price capture.

### Projected game winner
**Houston Astros — slight preference**
- Houston win: **55%**
- Kansas City win: **45%**

Margin decomposition:
- Kansas City outright win: **45%**
- Houston by exactly 1: **20%**
- Houston by 2+: **35%**

Representative central score: **Astros 4, Royals 3**.

### Pick #1 scrutiny — Royals +1.5
The key distinction is winner vs margin.

Houston has the slight outright edge from:
- home last bat;
- a strong Astros bullpen;
- recent Javier improvement;
- Houston's solid current production vs lefties.

But Kansas City +1.5 covers:
- every Royals win;
- every one-run Houston win.

#### Daniel Lynch IV
2026:
- 5-5
- 3.52 ERA
- 71.2 IP
- 1.10 WHIP
- 49 K
- 22 BB
- 16.6% K
- 7.5% BB
- 0.75 HR/9
- **3.86 FIP**

Recent starts:
- Sep. 9 vs Arizona: 5.0 IP, 4 H, 2 ER, 2 BB, 3 K
- Sep. 4 vs Toronto: 5.0 IP, 7 H, 5 ER, 1 BB, 0 K
- Aug. 29 at Cleveland: 3.1 IP, 3 H, 2 ER
- Aug. 23 vs Detroit: 4.1 IP, 4 H, 2 ER

Interpretation: Lynch suppresses walks/HR reasonably well, but the low strikeout rate leaves a larger balls-in-play/sequence tail.

#### Cristian Javier
2026:
- 2-5
- 5.50 ERA
- 55.2 IP
- 1.46 WHIP
- 55 K
- 23 BB
- 22.6% K
- 9.5% BB
- 1.46 HR/9
- **4.57 FIP**

Recent:
- Sep. 10 at Philadelphia: 6.0 IP, 3 H, 1 ER, 1 BB, 5 K
- Sep. 4 vs Arizona: 5.0 IP, 1 H, 1 ER, 3 BB, 8 K

Last two:
- **11.0 IP, 4 H, 2 ER, 13 K, 4 BB**
- reported recent-two ERA: **1.64**

Interpretation: this is a real current-regime improvement branch, but the Drive requires the 5.50 ERA / 4.57 FIP season prior to remain alive rather than declaring the problem solved after two starts.

#### Platoon matchup
**Royals vs RHP**
- 2026 OPS: **.721**
- last 30 days: **.792**
- last 30 days on road vs RHP: **.743**

**Astros vs LHP**
- 2026 OPS: **.711**
- last 30 days: **.751**

Kansas City's current RHP split is at least as strong as Houston's LHP split, which reduces the separation expected from Houston's side despite home field.

#### Bullpen state
**Houston**
Tuesday after Hunter Brown's 5 innings:
- Bennett Sousa worked after Brown
- AJ Blubaugh appeared
- Bryan Abreu appeared
- Josh Hader threw the ninth for the save

The key leverage chain therefore worked, but in normal one-inning doses rather than extreme multi-inning exposure.

Houston's bullpen remains a structural strength:
- Hader entered this series with a sub-1.00 ERA and 26 straight converted saves.
- Abreu remains a high-strikeout leverage option.

**Kansas City**
Michael Wacha supplied 6 innings Tuesday, limiting total bullpen exposure.
Lucas Erceg returned and threw a clean inning.
Kansas City therefore did not burn an extreme number of relief innings.

Workload is treated as availability, not automatic performance.

#### Injuries / availability
**Kansas City**
- Maikel Garcia was activated from the 10-day IL on Sep. 15.
- Jac Caglianone: Grade 1 left elbow flexor strain; recent status was day-to-day and exact lineup status remained unresolved pregame.
- James McArthur remained on rehab assignment / unavailable as a normal leverage option.

**Houston**
- Carlos Correa: officially shut down for the rest of 2026 following left-ankle rehab soreness.
- Brice Matthews: 60-day IL, left knee sprain.
- Mike Burrows: IL.
- Steven Okert: IL, right hamstring strain.
- Taylor Trammell: paternity list.
- Yordan Alvarez had recently returned after right-ankle soreness and homered Tuesday.
- Jeremy Peña also homered twice Tuesday after a prior slump.

### Total 9.0 geometry
- **Under 9.0 win:** **49%**
- **Exactly 9:** **15% push**
- **Over 9.0 win:** **36%**

#### Under mechanisms
1. Nine is a relatively high total.
2. Lynch owns a 3.86 FIP / 1.10 WHIP and low HR rate.
3. Javier has allowed only two earned runs over his last 11 innings.
4. Both clubs have strong late-game bullpen pieces.
5. Tuesday's bullpen usage was normal rather than catastrophic for either side.
6. Daikin Park has a roof-closed game state, removing outdoor weather variance.
7. Central score distribution remains in the 3-3 / 4-3 / 4-4 corridor.

#### Over mechanisms
1. Javier's season prior remains weak: 5.50 ERA, 4.57 FIP, 1.46 WHIP.
2. Kansas City owns a .792 last-30-day OPS vs RHP.
3. Houston owns a .751 last-30-day OPS vs LHP.
4. Lynch's low strikeout rate creates BABIP/sequence dependence.
5. Daikin Park's current three-year Statcast environment is around league average/slightly hitter-friendly, with a particularly strong HR factor in the retrieved split table.
6. Peña and Alvarez showed current power Tuesday.
7. Extra innings use the automatic runner, increasing the tie-after-nine scoring rate.

### Park / roof / environment
**Daikin Park**
- retractable roof
- current pregame game-thread data: **roof closed**
- indoor game environment; outside weather not decision-driving

Astros official roof guidelines support closing for game-window heat index/temperature above the threshold.

Baseball Savant 2024-26:
- overall park factor around **101** in the retrieved handedness table
- runs around **102**
- HR factor materially above average in the displayed split

Because the roof is closed, no wind/rain adjustment is applied.

### Recent series context
Sep. 15:
- Astros 4, Royals 2

This score is **context only**.

Active mechanisms carried forward:
- Houston used Brown + four relief arms, including Hader.
- Kansas City used Wacha for six innings and limited relief exposure.
- Peña hit two homers and Alvarez one, showing current power.
- Kansas City managed only four hits and struck out 14, but the opponent starter changes from Hunter Brown to Javier.
- Maikel Garcia has been activated, potentially improving KC's lineup construction.

### Upset / trend-break branches
1. Javier's two-start rebound proves durable and Houston controls the game.
2. Javier regresses toward the 5.50 ERA / 4.57 FIP season prior and KC scores 4-5 early.
3. Lynch's low-K contact profile gets punished by Peña/Alvarez/Paredes/Altuve-type bats.
4. Lynch suppresses HR/walks and Houston struggles to separate despite winning.
5. KC's strong current RHP split translates against Javier.
6. Houston's leverage bullpen protects a one-run lead — a Houston winner but Royals +1.5 success.
7. Houston's previously used leverage chain leaks late and KC wins outright.
8. A 4-4 or 5-4 exact-nine state creates a total push rather than an Over/Under win.

### Settlement
- MLB GameDay / StatsAPI controls official final.
- Run line includes eligible extra innings under standard settlement unless operator rules differ.
- Total 9.0: exactly nine runs = push under standard settlement.
- Listed-pitcher/action terms were not supplied and remain `UNKNOWN_DEFINITION`.

### Material sources
1. MLB probable pitchers:
   https://www.mlb.com/probable-pitchers
2. Royals probable pitchers:
   https://www.mlb.com/royals/roster/probable-pitchers/1000
3. Astros probable pitchers:
   https://www.mlb.com/astros/roster/probable-pitchers/
4. MLB starting lineups:
   https://www.mlb.com/starting-lineups
5. StatMuse — Lynch / Javier season metrics and game logs.
6. StatMuse — KC vs RHP and Houston vs LHP season/30-day splits.
7. MLB Royals transactions/injury reporting.
8. MLB Astros injury/transaction reporting.
9. MLB Sep. 15 game recap / Film Room.
10. Reuters Sep. 15 Astros-Royals recap.
11. Baseball Savant Daikin Park factor table.
12. Astros official Daikin Park retractable-roof guidelines.
13. Current pregame Houston/Kansas City reporting for game state.
14. Read-only Google Drive:
    `METHOD.md`, `RULES_GENERAL.md`, `RULES_BASEBALL.md`, `CONTROLS.md`, `SOURCES.md`, `PREDICTION_LOG_COMBINED_4.md`.

### Social / current reporting
Current team/community pregame sources reflected a pregame state and confirmed roof-closed conditions, but a field-owner official batting-order page was not recovered before the frozen cutoff. No post-first-pitch lineup or live result was used to change the card.

### Current status
**OPEN / UNSETTLED — PREGAME CARD FROZEN AT 09:58:42 AEST**

No retrospective or settlement performed.

### Document mapping
- Event card → `PREDICTION_LOG_COMBINED_4.md`
- Provisional ID/status → `GAME_LOG_STATUS_CURRENT.md`
- Existing starter/platoon/bullpen/roof controls → `RULES_BASEBALL.md`
- Any genuinely new durable source lane → `SOURCES.md` / `DATA_SOURCE_REGISTER.md`
- Future learning → P-448 retrospective block first

---

### Settlement and full retrospective — 2026-09-17

**Status:** `FINAL / SETTLED`  
**Official MLB final:** **Royals 5–2 Astros**. Daniel Lynch IV threw **5 scoreless innings, 2 H, 1 BB, 3 K**. John Rave hit a two-run homer; Michael Massey homered in a three-run eighth.

| Rank | Frozen contract | `p` (`UNVALIDATED_SUBJECTIVE`) | Result | Brier |
|---:|---|---:|---|---:|
| 1 | Royals +1.5 runs | 65% | **WIN** | 0.1225 |
| 2 | Combined Total Under 9.0 runs | 49% | **WIN** | 0.2601 |
| 3 | Combined Total Over 9.0 runs | 36% | **LOSS** | 0.1296 |
| 4 | Astros -1.5 runs | 35% | **LOSS** | 0.1225 |

**Projected winner:** Houston — **LOSS**.  
**Card mean Brier:** **0.1587**.  
**Rank-1:** WIN. **Hit@2:** YES. **Wins@2:** 2/2. **Both Top 2:** YES.

#### B. Why
The protected Royals side was stronger than the winner label because Lynch's low-HR/low-WHIP branch plus Kansas City's strong current RHP split could produce either a close game or outright KC win. Both happened. Houston's offense produced only two late runs.

#### C/D. Rank-1/Top-two
Both won. Relative ordering was justified: KC +1.5 had every Royals win plus one-run Houston wins; Under 9 had a wider push boundary and more Javier-season upper-tail exposure.

#### E. O/U
Under won at seven total runs. Javier's recent rebound held reasonably well (two runs in 5.1), and Lynch's stronger season process dominated Houston's lineup.

#### F. What went right
The card did **not** let Houston's home status or bullpen quality force an Astros -1.5 rank. It correctly separated outright winner from margin.

#### G. Validation
1. Official batting orders: not recovered before issue.
2. Bullpen/bench: leverage usage checked, full lineup incomplete.
3. Manager: no decisive missing pregame manager fact.
4. Injuries: Correa shutdown and current returns checked.
5. Sources: starter/platoon sources were strong.
6. Better: final posted MLB lineups.
7. Blind spot: the 55% Houston winner probability still underweighted Lynch/KC outright-win state.
8. Future: continue protected-side versus winner separation; do not promote a generic underdog rule.

**Three-question retrospective**
1. Driver: Lynch shut out Houston for five; KC generated enough power/separation.
2. Knowable: Lynch's 3.86 FIP/low HR profile and KC RHP split were known.
3. Smallest change: none to Rank-1; winner distribution should better reflect the same KC branch.

**Sources**
- AP/CBS recap: Kansas City 5–2 Houston.
- Reuters contemporary recap.


---

## P-449 [PROVISIONAL] — San Diego Padres @ Colorado Rockies

**Sport:** Baseball  
**Competition:** MLB 2026 regular season  
**Venue:** Coors Field, Denver, Colorado  
**Scheduled start:** 16 Sep 2026 18:40 MDT / 17 Sep 2026 10:40 AEST  
**Frozen pregame research window:** approximately 17 Sep 2026 10:22–10:30 AEST  
**State at issue:** **PREGAME / SCHEDULED**

### Supplied markets
1. Rockies +1.5
2. Padres -1.5
3. Combined Total Over 11.0
4. Combined Total Under 11.0

### Starter identity handshake
- **SD:** Robbie Ray, LHP — `PROBABLE_OFFICIAL`
- **COL:** Mason Adams, RHP — `PROBABLE_OFFICIAL`

MLB official probable-pitcher pages confirmed both starters. No scratch or bullpen-game replacement was verified before issue.

### Lineup state
MLB's official generic starting-lineup page was still showing lineups as unavailable/TBD during the research pass.

A current same-day lineup source projected:
**San Diego:** Fernando Tatis Jr., Dustin Harris, Manny Machado, Ty France, Jackson Merrill, Luis Campusano, Xander Bogaerts, Jake Cronenworth, Freddy Fermin.
**Colorado:** Jake McCarthy, Connor Norby, Hunter Goodman, TJ Rumfield, Cole Carrigg, Kyle Karros, Jordan Beck, Adael Amador, Ezequiel Tovar.

These remain **PROJECTED / NOT OFFICIAL**. Exact batting-order exposure is widened and player props are blocked.

### Ranked forecast

| Rank | Exact contract | Win probability | Push | Evidence |
|---:|---|---:|---:|---|
| **1** | **Padres -1.5 runs** | **55%** | 0% | Strongest supplied contract |
| **2** | **Combined Total Under 11.0 runs** | **49%** | **11%** | Moderate |
| **3** | **Rockies +1.5 runs** | **45%** | 0% | Live cushion branch |
| **4** | **Combined Total Over 11.0 runs** | **40%** | **11%** | Upper-tail but subordinate |

Probability tier: `UNVALIDATED_SUBJECTIVE`.  
**NO VALUE DETERMINABLE** without a validated predictive model plus same-time prices.

### Projected game winner
**San Diego Padres**
- Padres win: **64%**
- Rockies win: **36%**

Margin decomposition:
- Rockies outright win: **36%**
- Padres by exactly 1: **9%**
- Padres by 2+: **55%**

Representative central score: **Padres 6, Rockies 4**.

### Pick #1 scrutiny — Padres -1.5

#### Mason Adams — small-sample / hidden-regression risk
2026 MLB:
- 0-0
- **3.38 ERA**
- 18.2 IP
- 18 H
- 7 ER
- **5 HR**
- **9 BB**
- 22 K
- **1.446 WHIP**
- **5.68 FIP**
- 2.4 HR/9
- 4.3 BB/9
- 10.6 K/9

The ERA is substantially better than the fielding-independent line.

Current Rockies reporting also indicates Adams is working around a **75-pitch cap**, which materially increases the probability that San Diego sees Colorado's bullpen by the fifth/sixth inning even if Adams is pitching effectively.

#### Robbie Ray — strong ERA, weak current-regime branch
2026 overall:
- 12-8
- **3.57 ERA**
- 156.1 IP
- 132 K
- **81 BB**
- **1.35 WHIP**
- **4.73 FIP**
- 20.0% K
- **12.3% BB**
- 1.21 HR/9

Since joining San Diego:
- 7 starts
- 33.2 IP
- **5.35 ERA**
- **24 BB**
- 25 K
- 1.57 WHIP

Latest starts:
- Sep. 11 @ SF: 5 IP, 4 H, **5 ER**, 4 BB, 5 K
- Sep. 5 vs NYY: 2.1 IP, 5 H, **5 ER**, 4 BB, 1 K

September so far: **10 ER over 7.1 IP**.

Ray therefore has a significant walk/early-hook/contact tail at Coors. Pick #1 is not based on treating him as a dominant current starter.

#### Platoon matchup
**Padres vs RHP**
- last 30 days OPS: **.718**
- slash: about .244/.323/.395

**Rockies vs LHP**
- last 30 days OPS: ~**.718**
- home vs LHP last 30 days: **.673**
- home split: roughly .235/.305/.368

This is important contrary evidence to the Coors narrative: Colorado has not been especially strong against lefties at home recently.

#### Why San Diego still separates
1. Adams has a wide rookie mixture despite the good ERA.
2. His 5.68 FIP / HR/walk shape is dangerous against Tatis, Machado, France, Merrill, Campusano and Bogaerts.
3. The likely 75-pitch cap creates early Colorado-bullpen exposure.
4. Colorado's bullpen has reportedly posted a **7.66 ERA in September**, second-worst in MLB in current Rockies reporting.
5. San Diego is in a live Wild Card race and keeps a strong veteran batting core available.
6. Colorado is 56-95 with a deeply negative run differential, though record is contextual rather than a causal input.

#### Main contrary evidence
- Ray's recent command is poor enough to create an early Colorado lead.
- Coors creates wider variance than most parks, reducing run-line confidence.
- Colorado just scored nine runs with 16 hits; the result itself is not predictive, but Carrigg/McCarthy/Rumfield current contact is real.
- Hunter Goodman could return after his thumb MRI came back clean; his 38-HR power would raise Colorado's ceiling if he starts.
- Adams' MLB sample is only four starts and must be shrunk rather than treated as a 5.68-FIP certainty.

### Total 11.0 geometry
- **Under 11.0 win:** **49%**
- **Exactly 11:** **11% push**
- **Over 11.0 win:** **40%**

#### Under mechanisms
1. Eleven is a very high total even at Coors.
2. Colorado's home OPS vs LHP over the last 30 days is only ~.673.
3. San Diego's recent OPS vs RHP is only .718 rather than elite.
4. Colorado used only Kyle Freeland + Ryan Feltner Tuesday; Feltner covered **5 scoreless relief innings**, leaving the rest of the bullpen largely unused.
5. San Diego's Wandy Peralta/Randy Vásquez absorbed all relief work Tuesday, leaving primary leverage arms such as Mason Miller comparatively protected.
6. Current weather around game time is mild for Denver/Coors (~23°C) rather than extreme heat.

#### Over mechanisms
1. Coors Field remains MLB's strongest run environment.
2. 2024-26 Statcast:
   - overall park factor **112**
   - runs **125**
   - doubles **123**
   - triples **208**
   - HR **108**
3. Ray's current 12.3% walk rate and poor Padres-period control are dangerous at altitude.
4. Adams has allowed **5 HR in only 18.2 innings** and carries a ~75-pitch cap.
5. Colorado's September bullpen performance has been extremely poor despite Tuesday's rest state.
6. San Diego's bullpen showed fatigue/leakage in the first two games of the series.
7. Extra innings use the automatic runner, creating a high-scoring tie-after-nine state.

### Bullpen state

**San Diego — Sep. 15**
- Walker Buehler: 4.2 IP / 92 pitches
- Wandy Peralta: 0.2 IP / 24 pitches / 4 ER
- Randy Vásquez: 2.2 IP / 44 pitches / 3 ER

Implication:
- Peralta and Vásquez carry recent workload.
- Main leverage arms were not used Tuesday.
- Mason Miller worked the Sep. 14 game for the save but had Tuesday off.

**Colorado — Sep. 15**
- Kyle Freeland: 4.0 IP / 50 pitches
- Ryan Feltner: **5.0 IP / 61 pitches / 0 ER**

Implication:
- Colorado did not expose its usual bullpen at all Tuesday.
- Feltner himself is unlikely to be a normal relief option today after five innings.
- The wider bullpen is fresh but still carries poor recent-quality indicators.

Workload affects availability, not assumed performance.

### Injuries / unavailable players

**Colorado**
- Hunter Goodman: right thumb soreness, day-to-day; MRI fine. Exact starting status unresolved.
- Willi Castro: IL with left heel plantar fasciitis / right knee soreness; had not returned as of Sep. 15.
- Jose Quintana: 60-day IL / rehab from left elbow sprain.
- Sean Sullivan: rehab path.
- Kyle Freeland was just activated and pitched Tuesday.

**San Diego**
- Jason Adam: rehab assignment after right shoulder strain; not treated as normal leverage availability.
- Gavin Sheets: IL with left-foot sprain/plantar-plate tear.
- Ramón Laureano: 60-day IL / right hip surgery; unlikely before October.
- Bryan Hoeing: out for 2026 after flexor-tendon surgery.
- Yu Darvish: out after UCL/internal-brace procedure.
- Ty France was activated from the paternity list Sep. 14.

### Recent series context
Sep. 14:
- Padres 8, Rockies 7.

Sep. 15:
- Rockies 9, Padres 3.

These finals are **context only**.

Active mechanisms:
- Padres bullpen allowed Colorado back into Game 1 and collapsed in Game 2.
- Ryan Feltner's five-inning relief appearance preserved Colorado's wider bullpen.
- Colorado's Carrigg is in a current power/contact surge.
- San Diego's Tatis/Campusano/Hays showed home-run power Tuesday, though the offense stranded opportunities.
- Wild-card urgency is context only and not a standalone win mechanism.

### Park / weather
**Coors Field**
Statcast 2024-26:
- Park factor: **112**
- Run factor: **125**
- HR: **108**
- 2B: **123**
- 3B: **208**
- Hits: **117**

This is the largest environment adjustment in the matchup.

**Current conditions**
- around **23°C** / 73°F near the pregame window
- cloudy
- daily forecast included scattered afternoon thunderstorm risk
- no automatic Over adjustment from weather itself

Weather-related delay risk remains a starter-transition branch.

### Upset / trend-break branches
1. Ray's San Diego-period command issues continue and Colorado posts 4-5 early runs.
2. Hunter Goodman returns and adds major RHP power against Ray.
3. Adams' ERA proves more representative than his FIP for another start and he navigates 4-5 innings efficiently.
4. Adams hits the 75-pitch cap early and Colorado's poor September bullpen is exposed.
5. Padres convert their strong contact/power into a large Coors inning.
6. Colorado's fresh bullpen outperforms its September aggregate.
7. San Diego's main leverage bullpen benefits from Tuesday rest.
8. A 6-5 exact-11 state produces a push.
9. Rain/delay changes both starter lengths and relief sequencing.

### Settlement
- MLB GameDay / StatsAPI controls final.
- Run line includes eligible extras under standard MLB settlement unless operator rules differ.
- Total 11.0: exactly 11 = push under standard settlement.
- Listed-pitcher/action terms were not supplied and remain `UNKNOWN_DEFINITION`.

### Material sources
1. MLB probable pitchers — official starter identity and schedule.
2. MLB Padres/Rockies probable-pitcher pages.
3. MLB starting-lineup page — lineup field-owner check.
4. MLB Mason Adams player page.
5. Baseball-Reference — Ray and Adams standard/FIP lines.
6. Baseball Savant — Ray profile and Coors Field park factors.
7. StatMuse — Padres vs RHP / Rockies vs LHP splits.
8. MLB Rockies injury page — Goodman, Castro, Quintana.
9. MLB Padres injury/transaction page — Adam, Sheets, Laureano and current roster changes.
10. Reuters Sep. 14-15 Padres/Rockies reports.
11. MLB Film Room / Baseball Almanac Sep. 15 box score for bullpen usage.
12. Current Rockies reporting — Adams pitch cap and September pitching/bullpen state.
13. Venue-local weather widget / current Coors conditions.
14. Read-only Google Drive:
    `METHOD.md`, `RULES_GENERAL.md`, `RULES_BASEBALL.md`, `CONTROLS.md`, `SOURCES.md`, `PREDICTION_LOG_COMBINED_4.md`.

### Social / current reporting
Same-day team-community reporting was searched for lineups and current pitcher role. No fresh indexed official-team X post with a field-owner-confirmed full batting order was recovered before issue, so current lineups remain projected.

### Current status
**OPEN / UNSETTLED — PREGAME**

No retrospective or settlement performed.

### Document mapping
- Event card → `PREDICTION_LOG_COMBINED_4.md`
- Provisional ID/status → `GAME_LOG_STATUS_CURRENT.md`
- Existing small-sample starter / Coors / bullpen / run-line controls → `RULES_BASEBALL.md`
- Any future source promotion → `SOURCES.md` / `DATA_SOURCE_REGISTER.md`
- Future learning → P-449 retrospective block first

---

### Settlement and full retrospective — 2026-09-17

**Status:** `FINAL / SETTLED`  
**Official MLB final:** **Padres 9–3 Rockies**. Robbie Ray worked **6 innings with 6 strikeouts**; Mason Adams allowed early damage and San Diego scored in five of the first six innings.

| Rank | Frozen contract | `p` (`UNVALIDATED_SUBJECTIVE`) | Result | Brier |
|---:|---|---:|---|---:|
| 1 | Padres -1.5 runs | 55% | **WIN** | 0.2025 |
| 2 | Combined Total Under 11.0 runs | 49% | **LOSS** | 0.2401 |
| 3 | Rockies +1.5 runs | 45% | **LOSS** | 0.2025 |
| 4 | Combined Total Over 11.0 runs | 40% | **WIN** | 0.3600 |

**Projected winner:** Padres — **WIN**.  
**Final total:** 12.  
**Card mean Brier:** **0.2513**.  
**Rank-1:** WIN. **Hit@2:** YES. **Wins@2:** 1/2.

#### B. Why
The favourite-separation thesis was correct: Adams' small-sample/FIP/pitch-cap risk and Colorado bullpen exposure outweighed Ray's recent struggles. The total Under missed by one run because the exact high-variance Coors/Adams branch the card named became the realised state.

#### C/D. Rank-1/Top-two
R1 won; R2 lost. This is another coupling lesson: the Padres separation branch was also a major Over branch.

#### E. O/U
At 11.0, exactly 11 was a live push; the game reached 12. Coors' 125 run factor and the rookie/pitch-cap upper tail were not sufficiently reflected in a 49% Under preference.

#### F. What went right
The card did not treat Ray's poor two-start September sample as his only state; he rebounded to six strong innings. Adams' underlying 5.68 FIP and early bullpen exposure were appropriately highlighted.

#### G. Validation
1. Official lineups: projected, not field-owner confirmed.
2. Bench/bullpen: recent workload well researched.
3. Manager: Adams pitch cap current reporting captured.
4. Injuries: Goodman uncertainty and both clubs' IL states checked.
5. Sources: Coors/Savant and MLB starter data were strong.
6. Better: official same-day lineups.
7. Blind spot: Coors upper-tail mass still too low.
8. Future: record exact `P(12+)` branch under `C-OU-GEOMETRY`; do not convert one result into a permanent Coors Over rule.

**Three-question retrospective**
1. Driver: San Diego repeatedly scored against Adams/relief while Ray suppressed Colorado.
2. Knowable: yes as a major branch.
3. Smallest change: increase visibility, not necessarily weight, of high-run Coors tail before selecting an Under near 50%.

**Sources**
- MLB/Sportsnet game recap, Padres 9–3 Rockies.
- MLB final scoreboard and Ray/Adams game data.


---

## P-450 [PROVISIONAL] — Miami Marlins @ Arizona Diamondbacks

**Sport:** Baseball  
**Competition:** MLB 2026 regular season  
**Venue:** Chase Field, Phoenix, Arizona  
**Scheduled start:** 16 Sep 2026 21:40 EDT / 18:40 MST / 17 Sep 2026 11:40 AEST  
**Frozen pregame cutoff:** **17 Sep 2026, 11:38:34 AEST**  
**State at cutoff:** **PREGAME / SCHEDULED**

### Supplied markets
1. Marlins +1.5
2. Diamondbacks -1.5
3. Combined Total Over 9.0
4. Combined Total Under 9.0

### Starter identity handshake
- **MIA:** Ryan Gusto, RHP — `PROBABLE_OFFICIAL`
- **ARI:** Merrill Kelly, RHP — `PROBABLE_OFFICIAL`

Official MLB/MiLB Gameday shell confirmed the fixture, venue, start time and both starters. No scratch or bullpen-game replacement was verified before the freeze.

### Lineup state
MLB's official starting-lineup page still showed both lineups as unavailable/TBD immediately before the cutoff.

Current high-quality preview feeds converged on likely orders but were not promoted to `CONFIRMED_OFFICIAL`.

Likely Miami core:
Kyle Stowers, Heriberto Hernández, Otto Lopez, Griffin Conine, Javier Sanoja, Jakob Marsee, Xavier Edwards, Joe Mack/Agustín Ramírez, Esteury Ruiz/Graham Pauley.

Likely Arizona core:
Lars Nootbaar, Ketel Marte, Gabriel Moreno, Geraldo Perdomo, Corbin Carroll, Nolan Arenado, Jesús Sánchez, Pavin Smith, Tim Tawa/Jordan Lawlar.

Because the field-owner lineup remained unposted, exact lineup-slot exposure is widened and no player prop is issued.

### Ranked forecast

| Rank | Exact contract | Win probability | Push | Evidence |
|---:|---|---:|---:|---|
| **1** | **Marlins +1.5 runs** | **63%** | 0% | Strongest supplied contract |
| **2** | **Combined Total Under 9.0 runs** | **44%** | **14%** | Very close total |
| **3** | **Combined Total Over 9.0 runs** | **42%** | **14%** | Bullpen/park upper tail |
| **4** | **Diamondbacks -1.5 runs** | **37%** | 0% | Lowest supplied contract |

Probability tier: `UNVALIDATED_SUBJECTIVE`.  
**NO VALUE DETERMINABLE** without validated probabilities and same-time prices.

### Projected game winner
**Arizona Diamondbacks — slight preference**
- Arizona win: **54%**
- Miami win: **46%**

Margin decomposition:
- Miami outright win: **46%**
- Arizona by exactly 1: **17%**
- Arizona by 2+: **37%**

Representative central score corridor: **ARI 5-4 / MIA 5-4**, with exactly nine runs a material push state.

### Pick #1 scrutiny — Marlins +1.5

#### Ryan Gusto
2026:
- 1-5
- **4.14 ERA**
- **4.08 FIP**
- 78.1 IP
- 1.40 WHIP
- 65 K
- 25 BB
- 18.7% K
- 7.2% BB
- 1.03 HR/9

Recent:
- Sep. 11 vs LAD: **6.0 IP, 5 H, 2 ER, 3 BB, 3 K**
- Sep. 5 vs CHC: 4.2 IP, 10 H, 5 ER, 2 BB, 5 K

Interpretation: Gusto is not dominant, but his season ERA/FIP alignment is considerably healthier than Kelly's.

#### Merrill Kelly
2026:
- 9-13
- **4.97 ERA**
- **5.46 FIP**
- 152.0 IP
- **1.46 WHIP**
- 102 K
- 67 BB
- 15.5% K
- 10.2% BB
- 1.60 HR/9

Recent:
- Sep. 11 vs TEX: **4.1 IP, 2 H, 1 ER, 3 BB, 3 K**
- Sep. 4 at HOU: 6.0 IP, 7 H, 3 ER, 0 BB, 4 K
- Aug. 29 at SF: **7.0 IP, 2 H, 0 ER, 4 BB, 7 K**
- Aug. 24 vs CHC: 5.2 IP, 5 H, 3 ER, 3 BB, 4 K

Kelly's recent run prevention is clearly better than his full-season 4.97/5.46 profile. This current-regime improvement is retained, but four starts do not erase the weaker season prior.

#### Current platoon/offensive matchup
**Miami vs RHP**
- last 30 days OPS: **.756**
- previous rolling query through Sep. 15: as high as **.781**
- last 30 days road vs RHP: **.732**

**Arizona vs RHP**
- last 30 days OPS: **.677**
- last 30 days home vs RHP: **.652**
- last 15 days vs RHP: **.698**

This is the strongest process argument for Miami +1.5: Miami has been materially better in the exact handedness matchup than Arizona.

#### Bullpen state — major contrary evidence
Sep. 15 was an **11-inning game**.

**Miami**
- Starter Janson Junk: only 3.0 IP / 72 pitches.
- Miami then used **seven relievers** for eight innings:
  - Cade Gibson 1.0
  - Calvin Faucher 1.0
  - Tyler Zuber 1.0
  - Michael Petersen 1.0
  - Dax Fulton 0.2
  - Victor Vodnik 1.1
  - Josh Ekness **2.0**
- Pete Fairbanks was placed on the 15-day IL with right median nerve/brachial-plexus irritation.
- Miami therefore enters with both depth fatigue and closer-quality loss.

**Arizona**
- Michael Soroka: 5.0 IP / 80 pitches.
- Arizona still needed six relief innings.
- Arizona also had a demanding late game, but used fewer bullpen innings than Miami.
- Ryne Nelson was activated from the 60-day IL on Sep. 16 and current reporting says he shifts into a relief role, increasing available depth.
- Zac Gallen has also been moved into a bullpen role after returning.

This late-game state is why Arizona remains the slight outright winner despite Miami's starter/platoon advantages.

### Injuries / availability

**Miami**
- Pete Fairbanks: 15-day IL, nerve irritation; expected out for 2026.
- Owen Caissie: 10-day IL, lumbar stress reaction.
- Max Meyer: neck strain; expected out through season.
- Anthony Bender: season-ending right shin surgery.
- Xavier Edwards was activated Sep. 13 and is available.

**Arizona**
- Tyler Locklear: 60-day IL, fractured right thumb.
- Lourdes Gurriel Jr.: designated for assignment Sep. 13.
- Jesús Sánchez was activated Sep. 15 after waiver claim.
- Ryne Nelson activated Sep. 16 and moved toward relief role.
- Corbin Burnes and Zac Gallen have returned from long IL stints, although Gallen is now being used from the bullpen.

### Total 9.0 geometry
- **Under 9.0 win:** **44%**
- **Exactly 9:** **14% push**
- **Over 9.0 win:** **42%**

This total is intentionally close.

#### Under mechanisms
1. Arizona's current offense vs RHP is weak: .677 last 30 days, .652 at home.
2. Gusto's 4.08 FIP is respectable.
3. Kelly's last four starts have been much better than his season baseline.
4. Chase Field roof is **officially CLOSED** for Sep. 16, eliminating wind/weather variability.
5. Arizona's available bullpen depth improved with Nelson/Gallen relief options.

#### Over mechanisms
1. Kelly's season profile remains poor: 5.46 FIP, 1.46 WHIP, 10.2% BB, 1.60 HR/9.
2. Miami owns a .756-.781 recent OPS vs RHP.
3. Miami's bullpen is highly taxed after eight relief innings Tuesday.
4. Miami has lost Fairbanks, weakening the late-game run-suppression path.
5. Arizona's bullpen also covered six innings Tuesday.
6. Chase Field is hitter-friendly in the 2024-26 Statcast window:
   - overall park factor around **106**
   - runs around **112**
   - doubles around **113**
   - triples around **204**
   - HR around **104** for the retrieved right-handed split.
7. MLB extra innings use the automatic runner, widening the high-scoring tie branch.

### Park / roof / weather
**Chase Field**
- Retractable roof.
- Arizona's official roof page lists **Sep. 16 vs Miami: CLOSED**.
- Therefore outside Phoenix weather/wind is not a material game-environment input.

### Recent series context
Sep. 14:
- Arizona 8, Miami 7, walk-off.

Sep. 15:
- Miami 4, Arizona 2 in 11 innings.

These finals are not used as automatic trend signals.

Active mechanisms:
- Miami's bullpen was heavily used Tuesday.
- Arizona also used substantial late relief.
- Miami's offense has remained competitive against RHP.
- Arizona has struggled to cash scoring opportunities recently; Tuesday they went 1-for-13 with runners in scoring position.
- Corbin Carroll/Gabriel Moreno/Marte remain meaningful top-order threats.
- Fairbanks' injury is a genuine late-game change for Miami.

### Upset / trend-break branches
1. Gusto repeats his six-inning Dodgers outing and suppresses Arizona's weak RHP split.
2. Kelly's recent improvement persists and Miami's road offense underperforms its .732 split.
3. Kelly regresses toward the 5.46 FIP / 1.60 HR/9 season prior and Miami scores early.
4. Miami's tired bullpen loses a one-run lead late.
5. Arizona's newly expanded Nelson/Gallen relief depth stabilizes a close lead.
6. Arizona's poor recent RHP split reverses through Carroll/Marte/Moreno/Arenado power.
7. Both taxed bullpens create a late Over despite good starter phases.
8. A 5-4 / 4-5 final produces an exact-nine push.
9. Tie-after-nine automatic-runner scoring creates a multi-run extra-inning branch.

### Settlement
- MLB GameDay / StatsAPI controls official final.
- Run line includes eligible extra innings under standard settlement unless operator rules differ.
- Total 9.0: exactly nine = push.
- Listed-pitcher/action terms were not supplied and remain `UNKNOWN_DEFINITION`.

### Material sources
1. MLB/MiLB Gameday:
   https://www.milb.com/gameday/marlins-vs-d-backs/2026/09/16/825031
2. MLB starting lineups:
   https://www.mlb.com/starting-lineups
3. MLB D-backs lineup page:
   https://www.mlb.com/dbacks/roster/starting-lineups
4. MLB Marlins transactions/injuries:
   https://www.mlb.com/marlins/roster/transactions
   https://www.mlb.com/marlins/news/marlins-injuries-and-roster-moves
5. MLB D-backs transactions:
   https://www.mlb.com/dbacks/roster/transactions
6. Baseball-Reference / StatMuse — Gusto and Kelly season/current game logs.
7. StatMuse — MIA vs RHP and ARI vs RHP current splits.
8. MLB/Reuters Sep. 14-15 series reports.
9. Exact Sep. 15 scorecard/officially reconciled pitching usage.
10. Arizona Diamondbacks official Chase Field roof page:
    https://www.mlb.com/dbacks/ballpark/information/roof
11. Baseball Savant Chase Field park factors:
    https://baseballsavant.mlb.com/leaderboard/statcast-park-factors
12. Current Arizona roster reporting on Ryne Nelson/Zac Gallen bullpen roles.
13. Read-only Google Drive:
    `METHOD.md`, `RULES_GENERAL.md`, `RULES_BASEBALL.md`, `CONTROLS.md`, `SOURCES.md`, `PREDICTION_LOG_COMBINED_4.md`.

### Social / current-reporting check
Official MLB/team pages and same-day current reporting were searched. No field-owner official batting-order post was recovered before the 11:38:34 AEST freeze; therefore likely lineups remain projected and no post-first-pitch information is admitted.

### Current status
**OPEN / UNSETTLED — PREGAME CARD FROZEN AT 11:38:34 AEST**

No retrospective or settlement performed.

### Document mapping
- Event card → `PREDICTION_LOG_COMBINED_4.md`
- Provisional ID/status → `GAME_LOG_STATUS_CURRENT.md`
- Existing starter/bullpen/roof/run-line controls → `RULES_BASEBALL.md`
- Any durable source promotion → `SOURCES.md` / `DATA_SOURCE_REGISTER.md`
- Future learning → P-450 retrospective block first

---

### Settlement and full retrospective — 2026-09-17

**Status:** `FINAL / SETTLED`  
**Official MLB final:** **Marlins 4–3 Diamondbacks**. Jakob Marsee hit a two-run homer; Arizona's three runs came on solo homers by Pavin Smith, Gabriel Moreno and Nolan Arenado. Merrill Kelly struck out nine but Miami scored four.

| Rank | Frozen contract | `p` (`UNVALIDATED_SUBJECTIVE`) | Result | Brier |
|---:|---|---:|---|---:|
| 1 | Marlins +1.5 runs | 63% | **WIN** | 0.1369 |
| 2 | Combined Total Under 9.0 runs | 44% | **WIN** | 0.3136 |
| 3 | Combined Total Over 9.0 runs | 42% | **LOSS** | 0.1764 |
| 4 | Diamondbacks -1.5 runs | 37% | **LOSS** | 0.1369 |

**Projected winner:** Arizona — **LOSS**.  
**Card mean Brier:** **0.1910**.  
**Rank-1:** WIN. **Hit@2:** YES. **Wins@2:** 2/2. **Both Top 2:** YES.

#### B. Why
The exact matchup evidence behind Miami +1.5 held: Miami's recent RHP split was stronger, Kelly's season prior remained vulnerable, and Arizona did not create enough sustained offense to separate. The Under survived despite both teams' bullpen workload.

#### C/D. Rank-1/Top-two
Both won. This is a good example of the protected side and low total being coherent without requiring the Marlins winner to be selected outright.

#### E. O/U
Seven total runs. The roof-closed environment and starter phases kept the game below nine; Arizona's offense scored only via three solo HRs rather than sustained traffic.

#### F. What went right
The card correctly identified Miami's platoon/process advantage and treated Arizona only as a slight winner, not a strong favourite.

#### G. Validation
1. Official lineups: not posted at freeze.
2. Bench/bullpen: unusually heavy prior-night relief work was well documented.
3. Manager: bullpen-role changes (Nelson/Gallen) researched.
4. Injuries: Fairbanks loss and current Arizona roster moves checked.
5. Sources: MLB transactions/roof page and pitcher records were strong.
6. Better: official posted lineups before issue.
7. Blind spot: Arizona winner still received 54% despite Miami's strongest process signals.
8. Future: winner and run-line distributions should inherit the same current platoon evidence consistently.

**Three-question retrospective**
1. Driver: Miami generated four early runs and Arizona never produced a multi-run inning.
2. Knowable: Miami RHP matchup strength and Arizona offensive weakness were known.
3. Smallest change: improve winner-allocation coherence; no new side rule.

**Sources**
- Reuters recap: Jakob Marsee, Marlins 4–3 Diamondbacks.
- MLB game story: https://www.mlb.com/stories/game/825031


---


# 4. General Learnings, Rule Changes, Observations, and New Sources

## Cross-sport learnings

1. **Robust contract selection and outright-winner selection remain different tasks.** P-439, P-441, P-443, P-448 and P-450 all reinforce that a protected side/alternate total can be correct while the plurality winner label is wrong. This confirms existing objective separation; it does **not** support a blanket preference for underdogs or handicaps.
2. **Top-two shared failure states require explicit mass.** P-438 lost both top rows through one early-score regime switch; P-444 lost both through a close-game/extras path. This directly supports the newly carried `G-L17` disclosure.
3. **A correct total can be produced by a different allocation than forecast.** Spread/total and team-score marginals must stay linked through `G-L18`.
4. **Participant uncertainty mainly widens tails.** Missing official lineups were common. It should lower probability extremity rather than create arbitrary signed adjustments.
5. **Process integrity can be a success even when no ranked result exists.** P-445's toss made every conditional ranked contract inactive; refusing to transfer the target into the chase is exactly the correct behaviour.

## Soccer-specific learnings

- **P-438:** early goals can invalidate a low-tempo centre almost immediately. Existing soccer controls 20/25 need more explicit probability mass before >80% early Unders.
- **P-439/P-441:** low-event matches strengthen protected-side and draw-band logic but do not validate generic Under rules.
- **P-440:** first-half and full-match tails can diverge materially; a successful phase Under does not imply a full-match Under.

## Baseball-specific learnings

- **Extra innings:** P-443 and P-444 are unusually clean paired examples of control 22. In P-443, regulation landed exactly on the 8-run push and extras created the Over; in P-444, regulation had only four runs and extras turned an Under into a loss. `P(tie after 9)` should be printed beside integer totals where it is material.
- **Bullpen transition:** P-442's Rank-1 loss came after the starter phase, when Cleveland's first/middle relief matchup generated a four-run sixth. Rank #1 run-line work must carry score-state relief chains, not only starter quality.
- **Favourite separation vs total:** P-446 and P-449 show the same favourite-scoring branch can win -1.5 and defeat an Under. This is a `G-L18` allocation/coupling issue.
- **Protected sides:** P-448 and P-450 won outright after being ranked as +1.5 contracts. Preserve the cushion decomposition; do not infer a generic “take +1.5” rule.
- **Current splits vs winner allocation:** P-450's Miami process advantage was correctly used for +1.5 but not fully propagated into the 1X2 winner distribution.

## Cricket-specific learnings

- **Conditional innings identity worked exactly as intended in P-445.** Jamaica won the toss and chased, so Jamaica batting-first contracts were no-action.
- **Same-match current XI mattered:** Saim Ayub played despite pregame uncertainty. That was legitimately unresolved at the freeze; do not treat post-toss knowledge as a pregame sourcing failure.
- **Target-censored chases are not innings-total substitutes.** Jamaica's 79/0 Powerplay cannot retrospectively settle or validate a Jamaica batting-first Powerplay forecast.

## Potential rule/process changes

| Proposal | Status | Reason |
|---|---|---|
| Mandatory printed `P(tie after 9)` beside MLB integer totals when > de minimis | **REINFORCE / operationalise existing BB control 22** | P-443 and P-444 provide opposite settlement examples. |
| Shared Top-2 failure-state row with explicit mass | **Already active as G-L17; reinforce execution** | P-438 and P-444. |
| Participant-missingness probability-extremity audit | **Continue C-PROB-EXTREMITY; no new cap yet** | Several cards carried 80%+ rows without final XIs. |
| Favourite-separation / total shared-state table | **Reinforce G-L18 + baseball control 21** | P-446/P-449. |
| Early-goal regime-switch mass before soccer early Under >80% | **Candidate execution refinement; no signed rule** | P-438. |

No permanent directional coefficient or automatic market-family preference is promoted from this cohort.

## Algorithm improvements

- Build a **three-layer MLB settlement object**: nine-inning score distribution -> tie-after-nine probability -> automatic-runner extras distribution.
- For margin + total Top-2 combinations, show the **same representative score states** in both settlement units.
- Carry participant missingness into **distribution width and probability extremity**, not into ad hoc direction.
- For soccer early-phase rows, enumerate first-10-minute goal states and their downstream tactical transition.
- For conditional cricket markets, store the activation condition as a first-class field and grade `NO ACTION` before any outcome lookup.

## Source improvements

| Source | Best field | Assessment |
|---|---|---|
| MLB GameDay / MLB Film Room | Final score, innings sequence, starters, box/event timeline | High-authority; should remain primary MLB settlement lane. |
| AFC official competition reports | Soccer final and scorer/timeline narrative | Strong field owner for AFC scores/results. |
| UEFA official fixtures/results and lineups | Europa League final, regulation identity, participant lists | Strong field owner. |
| CricketWorld scorecard | CPL innings, Powerplay note, toss and detailed scorecard | Useful detailed settlement/corroboration route; official CPL/Cricket West Indies remains preferred where equivalent data are exposed. |
| AP/Reuters game reports | Mechanism narrative and injury/event context | Strong corroboration, not a replacement for official box score. |
| Nuestras Noticias Chihuahua / Dorados press | LNBP local schedule and Jornada identity | Useful for collision resolution; final settlement still needs a clearly identified field-owner/reliable game record. |

## Data-quality observations

- **Date/opponent collision risk** is real in back-to-back basketball series: P-451 searches repeatedly returned the prior night's 91–89 result.
- MLB generic lineup pages lagged on many cards. Final-refresh workflow should query exact event/GameDay endpoints and team channels, then explicitly record publication time.
- Search snippets remain discovery only; all numeric settlement fields in this pass were checked against opened/structured or high-quality result records.
- No unresolved derivative statistic from this cohort was force-settled.

## Recurring blind spots

1. Same-day starting-lineup completeness.
2. Explicit score-state bullpen mapping.
3. Extra-inning reach probability on integer totals.
4. Probability extremity under participant uncertainty.
5. Coupling between favourite separation and total upper tail.
6. Winner-label allocation when protected-side evidence is stronger.

## Items requiring more evidence before becoming formal rules

- Any numerical maximum probability when official lineups are missing.
- Any general preference for +1.5 underdogs over favourites.
- Any automatic Over adjustment at Coors or from bullpen fatigue.
- Any automatic Under bias in AFC/UEFA openers.
- Any new coefficient from the 9/12 Rank-1 result in this small cohort.

## Learning-only descriptive diagnostics

For the **12 cards with activated, graded ranked rows** (`P-438`–`P-444`, `P-446`–`P-450`; excluding conditional-no-action `P-445` and blocked `P-451`):

- **Rank #1:** 9 W / 3 L.
- **Hit@2 (at least one Top-2 win):** 10 / 12.
- **Both Top 2 won:** 6 / 12.
- **Top-two slots:** 16 wins / 24.
- **Ranked rows:** 31 W / 21 L over 52 rows.
- **Mean Brier:** 0.2097 vs trivial 0.25 baseline.
- **Projected winners:** 6 correct / 13 settled winner labels (`P-438`–`P-450`, including P-445 winner); P-451 had no winner forecast.

These numbers are **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**. They do not establish calibration, market edge, ROI, value or model superiority.


---


# 5. Document Update Mapping

**Google Drive remained READ-ONLY. No Drive file was modified.**

| Finding / material | Intended Markdown home | Proposed implementation when write access is explicitly authorised |
|---|---|---|
| P-438–P-451 canonical records | `PREDICTION_LOG_COMBINED_4.md` | Import these records under canonical IDs P-438–P-451, preserving issued text and settlement appendices. |
| Current unresolved P-451 result | `GAME_LOG_STATUS_CURRENT.md` | Add a result-recovery handle for exact Jornada 20 until a reliable final is recovered; do not reuse Jornada 19's 91–89. |
| MLB extras paired evidence | `RULES_BASEBALL.md` control 22 / `LEARNING_REGISTER.md` evidence | Add P-443/P-444 as execution examples; no new signed coefficient. |
| Shared Top-2 failure state | `RULES_GENERAL.md` G-L17 / `LEARNING_REGISTER.md` | Add P-438/P-444 as supporting evidence for the already-active disclosure. |
| Allocation/margin-total coupling | `RULES_GENERAL.md` G-L18 and `RULES_BASEBALL.md` | Add P-446/P-449 examples. |
| Soccer early-goal regime switch | `RULES_SOCCER.md` controls 20/25 | Add P-438 as an execution example; candidate refinement only. |
| Conditional cricket activation | `RULES_CRICKET.md` target/innings identity | Add P-445 as positive evidence that the gate prevented target substitution. |
| MLB GameDay exact-event retrieval | `SOURCES.md` / `DATA_SOURCE_REGISTER.md` | Reinforce exact GameDay/Film Room route for final/innings sequence and late lineup retrieval. |
| CPL detailed scorecard lane | `SOURCES.md` / `DATA_SOURCE_REGISTER.md` | Record CricketWorld/Cricbuzz as detailed corroboration routes; keep official competition source priority. |
| LNBP collision/result recovery | `SOURCES.md` / `DATA_SOURCE_REGISTER.md` | Document that local series reporting is useful for Jornada identity but requires exact-event final disambiguation. |
| External mini reconciliation | `EXTERNAL_LOGGING_WORKFLOW.md` | Reconcile this updated mini into Part 4 in the normal import flow; archive raw + settled variant only after write authorisation. |

## Canonical-ID integrity

Current Drive Part 4 explicitly states **next canonical ID P-438** after reconciliation of P-424–P-437. Therefore:

- `P-438` through `P-451` are now the correct canonical slots for these 14 event/query records.
- The original `[PROVISIONAL]` labels are preserved inside issued text as historical evidence only.
- **No canonical collision was found.**
- No temporary prediction IDs are required.
- Next canonical slot after this mini is **P-452**, subject to later Drive reconciliation.
- P-451 remains an unresolved result-recovery item, not an ID conflict.

## Explicit settlement lists

**Settled / administratively settled logs, first to most recent:**  
`P-438`, `P-439`, `P-440`, `P-441`, `P-442`, `P-443`, `P-444`, `P-445` (conditional ranked rows NO ACTION; winner settled), `P-446`, `P-447`, `P-448`, `P-449`, `P-450`.

**Logs still awaiting settlement, first unresolved to most recent:**  
`P-451` — blocked/no-card at issue; exact Jornada 20 final not reliably recovered in this pass.
