# PREDICTION MINI RUNNING LOG — RECONCILED CONTINUATION

**Status:** ACTIVE LOCAL APPEND-ONLY MIRROR  
**Reconciled:** 2026-09-04 Australia/Melbourne  
**Google Drive:** READ ONLY  
**Canonical authority:** `PREDICTION_LOG_COMBINED_2.md`  
**Current published method:** `MDS-2026.09.04-v3.4`  
**Forecast lane:** `SPORTS_ONLY / MARKET_BLIND`  
**Numerical state:** `NTS-2026.09.02-v0.3 — Stage 0 / pre-fit`  
**Probability state:** `NOT_GENERATED / NOT_PUBLISHED`  
**Value state:** `NO VALUE DETERMINABLE`  

> Fresh Drive reconciliation still shows **P-280** as the next ID in the read-only Drive snapshot because the locally issued P-280 card has not been imported into Drive. This local mirror therefore continues sequentially to **P-281** without reusing P-280. The earlier Geelong card labelled P-272 remains a **noncanonical local unresolved record** because it collides with Drive's already-used canonical P-272.

---

# UNSETTLED / INCOMPLETE QUEUE

| Local/canonical ID | Sport | Event | Frozen state | Rank #1 | Potential winner | Status |
|---|---|---|---|---|---|---|
| `LOCAL-GEELONG-20260904` *(previously labelled local P-272; noncanonical collision)* | AFL | Geelong Cats vs Carlton | PREGAME | Geelong +11.5 | Geelong Cats | UNSETTLED — no retrospective requested |
| **`P-280`** | NRL | South Sydney Rabbitohs vs Sydney Roosters | PREGAME | **Roosters +22.5** | **South Sydney Rabbitohs** | **UNSETTLED — no retrospective requested** |
| **`P-281`** | CPBL Baseball | Rakuten Monkeys @ Fubon Guardians | PREGAME | **Under 6.5 runs** | **Rakuten Monkeys** | **UNSETTLED — no retrospective requested** |
| **`P-282`** | CPBL Baseball | TSG Hawks @ Uni-Lions | PREGAME | **Under 6.5 runs** | **TSG Hawks** | **UNSETTLED — no retrospective requested** |
| **`P-283`** | Cricket T20I | Namibia vs South Africa | PREGAME — FINAL TOSS REFRESH | **South Africa Over 53.5 (6 overs)** | **South Africa** | **UNSETTLED — no retrospective requested** |
| **`P-284`** | FIBA Women's Basketball World Cup | USA (W) vs China (W) | PREGAME | **Under 161.5 points** | **USA (W)** | **UNSETTLED — no retrospective requested** |
| **`P-285`** | FIBA Women's Basketball World Cup | Korea (W) vs Nigeria (W) | PREGAME | **Under 143.5 points** | **Nigeria (W)** | **UNSETTLED — no retrospective requested** |
| **`P-286`** | ETPL Cricket | Glasgow Cosmic vs Belfast Wolves | PREGAME / RAIN-REDUCED 12 OVERS | **Wolves Under 120.5 (12 overs)** | **Belfast Wolves** | **UNSETTLED — no retrospective requested** |
| **`P-287`** | Tennis — US Open | Alexander Bublik vs Tommy Paul | PREGAME | **Over 40.5 total games** | **Tommy Paul** | **UNSETTLED — no retrospective requested** |
| **`P-288`** | MLB Baseball | Athletics @ Seattle Mariners | PREGAME | **Mariners -1.5** | **Seattle Mariners** | **UNSETTLED — no retrospective requested** |
| **`P-289`** | AFLW | Western Bulldogs (W) vs Sydney Swans (W) | PREGAME | **Sydney Swans -10.5** | **Sydney Swans** | **UNSETTLED — no retrospective requested** |
| **`P-290`** | Liga MX Soccer | FC Juárez vs Pachuca | PREGAME | **Pachuca Over 0.5 team goals** | **Pachuca** | **UNSETTLED — no retrospective requested** |
| **`P-291`** | Tennis — US Open | Ben Shelton vs Denis Shapovalov | PREGAME | **Shapovalov +5.5 games** | **Ben Shelton** | **UNSETTLED — no retrospective requested** |
| **`P-292`** | AFLW | St Kilda (W) vs North Melbourne (W) | PREGAME | **Under 89.5 points** | **North Melbourne** | **UNSETTLED — no retrospective requested** |
| **`P-293`** | AFLW | Port Adelaide (W) vs Gold Coast SUNS (W) | PREGAME | **Gold Coast +13.5** | **Port Adelaide** | **UNSETTLED — no retrospective requested** |

---

# SETTLED CHRONOLOGY

**None in this reconciled local mirror yet.**  
Canonical P-272–P-279 are already settled in the Drive authority and are not duplicated as fresh local cards here.

---

# P-280 — South Sydney Rabbitohs vs Sydney Roosters — 2026 NRL Round 27

## 1. Frozen identity, state and contracts

- **Canonical ID:** `P-280`
- **Sport:** Rugby league
- **Competition:** 2026 NRL Telstra Premiership, Round 27
- **Event:** South Sydney Rabbitohs vs Sydney Roosters
- **Venue:** Allianz Stadium, Sydney
- **Scheduled kickoff:** Friday 4 September 2026, 8:00 pm AEST
- **Information/state cutoff:** **2026-09-04 19:51:18 AEST**
- **Cutoff invariant:** PASS — approximately 8 minutes 42 seconds before scheduled kickoff
- **Game state:** `PREGAME`
- **Method:** `MDS-2026.09.04-v3.4`
- **Algorithms:** `GFA-2 + SFA-RUGBY-LEAGUE`
- **Numerical state:** `NTS-2026.09.02-v0.3 — Stage 0 / pre-fit`
- **Probability:** `NOT GENERATED / NOT PUBLISHED`
- **Value / ROI / staking:** `NOT AUTHORISED`
- **Operator settlement terms:** not supplied; regulation/golden-point and operator-specific settlement treatment are therefore `UNKNOWN_DEFINITION`
- **Retrospective:** **NOT PERFORMED — user explicitly requested none yet**

### User-supplied exact slate

| Contract ID | Contract | Ordinary full-game geometry |
|---|---|---|
| `P-280-C01` | **Rabbitohs -22.5** | Wins if South Sydney wins by 23+ |
| `P-280-C02` | **Roosters +22.5** | Wins if Sydney Roosters wins, draws, or loses by 1–22 |
| `P-280-C03` | **Combined Over 54.5** | Wins at 55+ total points |
| `P-280-C04` | **Combined Under 54.5** | Wins at 54 or fewer total points |

---

## 2. Canonical reconciliation

The active Drive authority `PREDICTION_LOG_COMBINED_2.md` showed, at the fresh read for this query:

- **Next canonical ID: P-280**
- **Open/live/pending queue: none**
- P-272–P-279 already imported and settled in Drive.

An earlier local Geelong card in this conversation had been labelled `P-272` from stale local state. That label collides with Drive's canonical sequence and therefore **does not control numbering**. It is preserved separately above as an unresolved **NONCANONICAL LOCAL RECORD** until the user later requests settlement. This P-280 card is the first new card in this reconciled local continuation.

---

## 3. Governing rugby-league process applied

The active NRL framework requires:

`sets / set starts -> field position -> goal-line entries -> try creation -> goal conversion -> fatigue -> joint score/margin`

Mandatory controls applied:
- changed spine is a regime variable;
- raw points and cover history are diagnostic only;
- winner, handicap and total are separate queries against one coherent score tree;
- a favourite can carry an Over almost alone;
- a low total can coexist with a large favourite margin;
- favourite-only blowout and low-total-separation branches must be tested before ranking an Under or underdog cushion;
- second-half fatigue, sin-bin/send-off and terminal-sequence states remain explicit tails;
- weather is bidirectional, never an automatic Under.

### Precondition status

| Gate | Status | Note |
|---|---|---|
| `RL-P1` competition/laws | **PASS** | NRL Round 27; NRL regulation/golden-point framework applies, but exact sportsbook settlement wording was not supplied. |
| `RL-P2` final team/spine | **PARTIAL** | Latest official NRL pregame team and late-mail material was retrieved. The exact independently timestamped final-17 release immediately before kickoff was not captured before the freeze, so no unverified late change is asserted. |
| `RL-P3` goal kicker | **PARTIAL / LIMITATION** | Latrell Mitchell's 2026 goal record strongly supports him as Souths' likely primary kicker; Toby Rodwell's NSW Cup/NLR goal-kicking record strongly supports him as the Roosters' likely kicker. The pre-cutoff official Round 27 material did not explicitly designate the kickers. |
| `RL-P4` conditions | **PASS** | Dry, mostly clear Sydney conditions; no rain-driven Under assumption. |

**Consequence:** because `RL-P2`/`RL-P3` were not fully green at the frozen cutoff, the four supplied contracts are **qualitative forced ranks**, not high-confidence or calibrated predictions.

---

## 4. Current participant and spine audit

### South Sydney Rabbitohs

Latest official pregame material had the principal structure as:

- **Fullback:** Jye Gray
- **Five-eighth:** Jai Arrow
- **Halfback:** Jayden Sullivan
- **Hooker:** Brandon Smith
- **Cody Walker:** named to begin from the interchange
- **Latrell Mitchell:** starting at centre
- **Key middle/forward experience:** Tevita Tatola, Keaon Koloamatangi, Cameron Murray, David Fifita, Adam Elliott
- **Outside backs:** Alex Johnston, Jack Wighton, Campbell Graham
- **Tallis Duncan:** rested after hamstring tightness

### Mechanism impact

Souths have the clearly superior first-choice talent and continuity across the wider 17, but their **starting spine is not standard**. Jai Arrow at five-eighth and Cody Walker beginning from the bench introduce uncertainty into early set organisation, last-play shape and edge timing.

Latrell Mitchell is another high-impact but high-uncertainty state:
- this is his **first start in nearly four months**;
- his prior appearance was a limited return from a long absence;
- Wayne Bennett publicly indicated the aim was for him to get through the match and perform, but full 80-minute effectiveness could not simply be assumed.

That matters specifically against a huge **-22.5** line. Souths can be the much more likely winner without a 23-point winning margin being the central state.

### Sydney Roosters

The Roosters' selection is the game's dominant regime change.

Trent Robinson rested **nine key players** for the qualifying final, including:
- James Tedesco
- Billy Smith
- Rob Toia
- Mark Nawaqanitawase
- Daly Cherry-Evans
- Naufahu Whyte
- Reece Robson
- Siua Wong
- Hugo Savala was also being rested in the halves context

Sam Walker was unavailable after ankle surgery.

Latest official pregame structure included:
- **Fullback:** Cody Ramsey
- **Five-eighth:** Reece Foley
- **Halfback:** Toby Rodwell
- **Hooker:** Benaiah Ioelu
- **Experienced middle/core:** Spencer Leniu, Lindsay Collins, Connor Watson
- **Daniel Tupou:** returned after a shoulder absence
- several inexperienced/debut-level players were included in the extended match-day group.

### Mechanism impact

The biggest Roosters downgrade is not merely "missing stars"; it is the **spine and set-control disruption**. Foley/Rodwell/Ioelu/Ramsey are a major continuity downgrade from a Tedesco/DCE-or-Walker/Robson configuration.

That raises:
- poor last-play execution risk;
- weak exit-set kicking risk;
- repeated poor set-starts;
- attacking suppression;
- short-field opportunities for Souths;
- second-half fatigue if the Roosters are forced to defend repeat entries.

However, the Roosters still retain Collins, Leniu and Watson through the middle. That is material support for the **+22.5** cushion because they can keep the ruck and field-position battle respectable even if the reserve spine creates less attack.

---

## 5. Motivation and finals context

- **South Sydney:** a win secures a **home elimination final**.
- **Sydney Roosters:** top-four status was already secured, enabling the deliberate rest strategy.

This is not treated as an abstract "motivation coefficient." It is tied to observable selection decisions:
- Souths retained a strong senior core and are chasing placement.
- The Roosters explicitly prioritised finals freshness and accepted major continuity loss in this fixture.

That strongly favours **Souths as the outright winner**, but motivation alone does not solve a 22.5-point handicap.

---

## 6. Recent form and diagnostic scoring environment

### Rabbitohs — last five known official results before this fixture

| Round | Result | Total |
|---|---|---:|
| R22 | lost Sharks 16–32 | 48 |
| R23 | beat Eels 28–24 | 52 |
| R24 | beat Bulldogs 22–6 | 28 |
| R25 | lost Warriors 26–45 | 71 |
| R26 | beat Titans 42–22 | 64 |

Descriptive L5:
- record **3–2**
- points for average **26.8**
- points against average **25.8**
- combined total average **52.6**
- winning margins in the three wins: **+4, +16, +20**
- **none** of those three wins cleared a 22.5-point handicap
- 2/5 totals were above 54.5

### Roosters — last five known official results

| Round | Result | Total |
|---|---|---:|
| R22 | beat Cowboys 82–12 | 94 |
| R23 | beat Bulldogs 20–18 | 38 |
| R24 | beat Panthers 12–6 | 18 |
| R25 | lost Tigers 24–25 | 49 |
| R26 | lost Dolphins 12–26 | 38 |

Descriptive L5:
- record **3–2**
- points for average **30.0**, heavily distorted by the 82-point outlier
- points against average **17.4**
- combined total average **47.4**
- excluding the 82–12 outlier, the next four Roosters scores were 20, 12, 24 and 12.

### Season-level diagnostic

Official NRL club profile snapshots indicated approximately:
- Roosters: **26 points scored / 19 conceded per game**
- Rabbitohs: **28 scored / 24 conceded per game**

These are deliberately **not** used as direct projections because the Roosters' Round 27 spine and participant regime is radically different from the season aggregate.

---

## 7. Head-to-head reconciliation

The earlier 2026 meeting at Allianz Stadium:
- **Roosters 26–18 Rabbitohs**
- combined total **44**

The official preview also noted the Roosters had won six of the previous seven rivalry meetings.

This has **low direct predictive weight** here because the Round 27 Roosters are missing most of the high-leverage spine/backline pieces that generated those historical outcomes. It remains useful as rivalry/context evidence only.

---

## 8. Depleted-Roosters blowout comparator

A much more relevant regime comparator is the Roosters' **48–10 loss to the Dolphins in Round 15** when heavily depleted by Origin absences.

That match demonstrated the possession-native kill path required by the NRL rules:
- disrupted combinations;
- weaker field position;
- repeated defensive sets;
- line-break and missed-tackle clusters;
- one side converting short fields into a large margin.

Important qualification:
- that Roosters side still contained some senior playmaking/forward personnel different from tonight;
- the current Round 27 side has experienced middle support through Collins, Leniu and Watson;
- therefore 48–10 is **evidence that a blowout tail exists**, not a reusable expected score.

It is the main reason **Rabbitohs -22.5 cannot be dismissed** and why **Under 54.5 cannot be rated strongly**.

---

## 9. Conditions

At the freeze:
- Sydney was mostly clear and around the high teens Celsius;
- no material rain signal was present for the 8–10 pm window;
- official BOM observation evidence showed dry conditions and light wind earlier in the evening.

**Mechanism:** conditions do not materially suppress handling or goal-kicking. There is therefore **no weather-derived Under boost**. Dry conditions also leave the Souths favourite-only blowout/Over path fully live.

---

## 10. Joint qualitative score tree

No fitted or calibrated numerical NRL model is authorised, so these are scenario families only.

### `RL-B1` — central possession / central conversion

Representative family:
- **Souths 30–14**
- **Souths 32–16**
- **Souths 34–14**

Implications:
- Rabbitohs win
- **Roosters +22.5 survives**
- **Under 54.5 usually survives**

Why:
- Souths' stronger senior roster wins more territory and goal-line entries;
- the Roosters' reserve spine suppresses their attack;
- Collins/Leniu/Watson provide enough middle resistance to prevent an automatic defensive collapse.

### `RL-B2` — favourite-only scoring / blowout path

Representative family:
- **Souths 42–12**
- **Souths 42–14**
- **Souths 44–10**

Mechanism:
- Roosters exit-set errors or weak long kicking;
- repeated Souths short fields;
- reserve edge combinations lose line-break contests;
- defensive workload compounds after halftime;
- Souths' strong outside backs convert repeat entries.

Implications:
- **Rabbitohs -22.5 wins**
- total sits directly around the 54.5 threshold:
  - 42–12 = 54, Under
  - 42–14 = 56, Over
  - 44–10 = 54, Under

This is why **a Souths blowout does not automatically mean Over**.

### `RL-B3` — low-total separation

Representative family:
- **Souths 34–8**
- **Souths 36–10**

Mechanism:
- Roosters attack is heavily suppressed by inexperienced spine organisation;
- Souths dominate territory without needing a high-possession shootout;
- Roosters' experienced middle prevents Souths reaching the mid-40s but cannot generate points itself.

Implications:
- **Rabbitohs -22.5 + Under 54.5 can win together**.

This branch is mandatory under the Drive rules and materially raises Rabbitohs -22.5 relative to a simplistic "Under means close" view.

### Roosters resistance branch

Representative family:
- **Souths 26–18**
- **Souths 28–18**
- **Souths 30–20**

Mechanism:
- Collins/Leniu/Watson stabilise the middle;
- Rodwell's long kicking limits poor set starts;
- Souths' Arrow-at-six / Walker-off-bench configuration is less fluent than expected;
- Latrell's workload is managed.

Implications:
- **Roosters +22.5 strongly survives**
- Under generally survives
- Souths still wins most of this branch.

### Upset / terminal-sequence branch

The Roosters' outright win requires more than the +22.5 cushion:
- parity in completions and set starts;
- their inexperienced spine to execute above expectation;
- Souths to create errors during the unusual early halves setup;
- late field position / penalty / conversion events to fall Roosters' way.

The outright upset is materially less central than the broad Roosters +22.5 cover state.

### `RL-B6` — sin-bin/send-off tail

A Souths numerical-advantage period could create the 23+ separation quickly and also threaten the total. A Rabbitohs man-down state would instead sharply strengthen Roosters +22.5. No pregame assumption is made about either.

### `RL-B7` — weather

Dry conditions leave ordinary ball movement and kicking conditions intact. No one-sign weather adjustment.

### `RL-B8` — golden point / draw treatment

Golden point only becomes relevant in the narrowest score states. It matters more for the winner than the ±22.5 handicap. Exact operator settlement wording was not supplied, so no operator-specific claim is made.

---

## 11. Ranked forecast — exact supplied contracts

| Rank | Contract | Verdict | Reason |
|---:|---|---|---|
| **1** | **Roosters +22.5** | **BEST RELATIVE LEAN — confidence capped by incomplete final-team/kicker handshake** | The 22.5-point cushion covers every Roosters win and every Souths win by 1–22. Souths are the more likely winner, but their own early spine is unconventional and Latrell is returning to a full start after a long absence. Collins/Leniu/Watson give the depleted Roosters a plausible middle-resistance path. A 23+ Souths separation is credible but is a narrower condition than simply winning. |
| **2** | **Under 54.5** | **LEAN / FORCED RANK** | The reserve Roosters spine is more likely to suppress Roosters scoring than create a shootout. Recent Roosters totals outside the 82–12 outlier were low, and the central score family is roughly mid-40s to low-50s. But the Under is not strong because Souths can carry the match near/over the line almost alone. |
| **3** | **Rabbitohs -22.5** | **LIVE BLOWOUT ALTERNATIVE** | The Roosters' nine-player rest strategy plus Walker's injury creates a genuine possession/field-position collapse tail. The Round 15 depleted 48–10 loss shows this mechanism can become extreme. Still, Souths must clear a very large 23-point separation threshold, and their own starting playmaking configuration is not optimal. |
| **4** | **Over 54.5** | **LIVE BUT LEAST LIKELY OF THE FOUR** | Dry conditions and a Souths favourite-only explosion keep the Over alive, particularly around 42–14 or 44–12. The issue is that the same Roosters personnel changes that weaken their defence also substantially reduce their likely attacking contribution. Souths can dominate and still produce a 34–8, 36–10 or 42–12 Under. |

### Ordinal interpretation

The gap between #2, #3 and #4 is not large. **Rank #1 is the clearest contract call.** The total is materially more uncertain than the broad Roosters cushion because the same Roosters depletion simultaneously:
- increases Souths' scoring ceiling;
- lowers the Roosters' own scoring expectation.

That dependence is exactly why the total cannot be inferred from the favourite margin.

---

## 12. Potential game winner

# **South Sydney Rabbitohs — solid qualitative lean**

This winner call is intentionally separated from Rank #1.

Souths have:
- the stronger available senior roster;
- far greater spine/NRL experience overall despite the unusual Arrow/Walker deployment;
- home-final placement incentive;
- a Roosters opponent deliberately resting nine key players with Sam Walker also unavailable.

The Roosters' experienced middle means I prefer **Roosters +22.5** over **Rabbitohs -22.5**, but it does not make the Roosters the central outright winner.

**Representative central shape only:** South Sydney by roughly **12–20 points**, with the total more often in the **mid-40s to low-50s** than clearly above 54.5.

This is **not** a calibrated score/probability projection.

---

## 13. Evidence quality / honesty boundary

- Fixture, venue, stakes: **HIGH** — official NRL.
- Named rest/injury changes: **HIGH** — official NRL.
- Latest available pregame team structure: **HIGH/MEDIUM-HIGH**.
- Exact final-17 independent timestamp immediately before kickoff: **NOT FULLY VERIFIED AT FROZEN CUTOFF**.
- Exact designated goal-kickers for this match: **NOT EXPLICITLY CONFIRMED in the official pre-cutoff team article**.
- Recent results: **HIGH** — official NRL.
- H2H: **HIGH factual quality, LOW predictive weight because of current roster discontinuity**.
- Weather: **HIGH** — official BOM + contemporaneous Sydney forecast.
- Probabilities / edge / ROI / stake sizing: **NOT AVAILABLE / NOT AUTHORISED**.
- Retrospective: **NOT PERFORMED**.

---

# SOURCE REGISTER — P-280

## A. Google Drive governing framework — READ ONLY

1. `README.md` — current active-log authority; MDS-2026.09.04-v3.4; GFA-2; NTS Stage 0.
2. `PREDICTION_LOG_COMBINED_2.md` — controlling snapshot; next canonical ID P-280 at fresh read; P-272–P-279 already settled.
3. `RULES_NRL_RUGBY.md` — active SFA-RUGBY-LEAGUE v3.4 controls, preconditions, exposure chain, mandatory branches and kill paths.
4. Current Drive framework references carried through the above documents: `MODEL_AND_DATA_SPEC.md`, `LEARNING_REGISTER.md`, and the general operating workflow.

**Drive modification:** NONE.

## B. Official NRL sources

1. **NRL Team Lists: Round 27** — official selections and match officials.  
   Source: NRL.com, "NRL 2026, Round 27, official team lists, injuries, updates, Fantasy"  
   URL: https://www.nrl.com/news/2026/09/01/nrl-team-lists-round-27/

2. **Rabbitohs v Roosters match preview** — venue, stakes, rivalry notes and selections.  
   Source: NRL.com, "Rabbitohs v Roosters: Trell set to start; Robbo rests stars"  
   URL: https://www.nrl.com/news/2026/09/01/rabbitohs-v-roosters-trell-set-to-start-robbo-rests-stars/

3. **NRL Late Mail: Round 27** — latest official pregame changes available before freeze.  
   Source: NRL.com, "NRL Late Mail: Round 27 - Halasima sidelined; Yeo in frame"  
   URL: https://www.nrl.com/news/2026/09/02/nrl-late-mail-round-27--yeo-in-frame-duncan-hamstrung/

4. **Roosters roster-rest rationale / Lindsay Collins leadership**.  
   Source: NRL.com, "Leading from the front: Collins taking youngsters under his wing for grudge match."

5. **Latrell Mitchell return-state article**.  
   Source: NRL.com, "Latrell ready to hit top speed as Rabbitohs chase perfection."

6. **Official NRL Friday night live-preview page** — fixture/venue pregame reference.

7. **Official NRL club/player profile resources** used for season scoring diagnostics and goal-kicking-role evidence:
   - South Sydney Rabbitohs 2026 club profile/statistics
   - Sydney Roosters 2026 club profile/statistics
   - Latrell Mitchell profile
   - Jayden Sullivan profile
   - Reece Foley profile
   - Toby Rodwell NRL profile
   - Toby Rodwell NSW Cup profile/statistics

8. **Official NRL match reports/results used for recent-form reconstruction**:
   - Rabbitohs v Sharks, Round 22
   - Eels v Rabbitohs / relevant Round 23 result
   - Rabbitohs v Bulldogs, Round 24
   - Warriors v Rabbitohs, Round 25
   - Titans v Rabbitohs, Round 26
   - Roosters v Cowboys, Round 22
   - Bulldogs v Roosters, Round 23
   - Panthers v Roosters, Round 24
   - Tigers v Roosters, Round 25
   - Dolphins v Roosters, Round 26

9. **2026 earlier Rabbitohs–Roosters meeting** — Roosters 26–18 at Allianz Stadium.

10. **Dolphins 48–10 Roosters, Round 15** — depleted-Roosters regime comparator; used only to demonstrate the blowout mechanism, not as a reusable coefficient.

## C. Weather

1. Australian Bureau of Meteorology — Sydney / Observatory Hill observation feed.
2. Contemporaneous Sydney 8–10 pm forecast retrieved in-session at approximately 7:50 pm AEST: mostly clear, no material precipitation signal.

---

## 14. Settlement / next-query instruction

- P-280 remains **UNSETTLED / PREGAME**.
- **Do not perform a retrospective** unless the user explicitly requests it.
- At the next query, state-check all local unresolved records.
- If an event is final, settle it only according to the user's requested workflow; preserve the frozen pregame forecast verbatim.
- Once settled, move it from the top unresolved queue into settled chronology.
- Record every source used for settlement.
- Next canonical forecast ID after P-280 is **P-281**, subject to a fresh read of the Drive controlling snapshot before issuance.

---

# LEGACY NONCANONICAL LOCAL RECORD — PRESERVED VERBATIM

> The following prior local card is retained for audit continuity only. Its `P-272` label is noncanonical after fresh Drive reconciliation. Do not use its internal next-ID instruction.

# PREDICTION MINI RUNNING LOG

**Status:** ACTIVE — LOCAL APPEND-ONLY CONTINUATION  
**Opened:** 2026-09-04 Australia/Melbourne  
**Google Drive policy:** READ ONLY — no Drive file edited, uploaded, replaced, moved, renamed or deleted  
**Canonical predecessor:** `PREDICTION_LOG_COMBINED_2.md`  
**Drive next canonical ID at opening:** `P-272`  
**Local next canonical ID after this card:** `P-273`  
**Current published method:** `MDS-2026.09.04-v3.4`  
**General algorithm:** `GFA-2`  
**Sport algorithm:** `SFA-AFL`  
**Forecast lane:** `SPORTS_ONLY / MARKET_BLIND`  
**Numerical training:** `NTS-2026.09.02-v0.3 — Stage 0 / pre-fit`  
**Probability:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value / staking / ROI:** `NO VALUE DETERMINABLE / NOT AUTHORISED`  

> The active Drive log was opened with a v3.2 header, but the current `LEARNING_REGISTER.md` and `MODEL_AND_DATA_SPEC.md` carry the same-day v3.4 patch. Per the method-currency control, this local card uses v3.4.

---

# UNSETTLED / INCOMPLETE QUEUE

Unsettled cards stay in this section until an authoritative final settlement is performed. Once settled, the card will be moved into the normal settled chronology without rewriting its frozen pre-game forecast.

| ID | Sport | Event | Frozen state | Rank #1 | Potential winner | Settlement | Retrospective |
|---|---|---|---|---|---|---|---|
| `P-272` | AFL | Geelong Cats vs Carlton | PREGAME | **Geelong +11.5** | **Geelong Cats** | **PENDING** | **NOT PERFORMED — user explicitly requested none yet** |

---

# SETTLED CHRONOLOGY

**None in this new mini log yet.**

---

# P-272 — Geelong Cats vs Carlton — 2026 AFL Finals Elimination Final

## 1. Frozen identity, state and contracts

- **Canonical ID:** `P-272`
- **Sport:** Australian rules football
- **Competition:** 2026 Toyota AFL Premiership, Elimination Final
- **Event:** Geelong Cats vs Carlton
- **Venue:** Melbourne Cricket Ground, Melbourne
- **Scheduled bounce:** Friday 4 September 2026, 7:40 pm AEST
- **Information/state cutoff:** **2026-09-04 19:33:09 AEST**
- **Cutoff invariant:** PASS — approximately 6 minutes 51 seconds before scheduled bounce
- **Game state:** `PREGAME`
- **AFL current-state evidence:** official AFL live article headline stated final teams were in; no game score had begun in the frozen source state
- **Operator:** not supplied
- **Draw / extra-time / settlement terms:** `UNKNOWN_DEFINITION`; operator-specific terms were not supplied
- **Retrospective:** **NO**

### User-supplied exact slate

| Contract ID | Contract | Ordinary full-game geometry |
|---|---|---|
| `P-272-C01` | **Geelong +11.5** | Wins if Geelong wins/draws or loses by 1–11 |
| `P-272-C02` | **Carlton -11.5** | Wins if Carlton wins by 12+ |
| `P-272-C03` | **Combined Over 165.5** | Wins at 166+ total points |
| `P-272-C04` | **Combined Under 165.5** | Wins at 165 or fewer total points |

---

## 2. Governing AFL process applied

The active AFL framework requires the forecast to be built from the current scoring chain rather than from raw points averages or head-to-head alone:

`clearance / turnover / intercept -> inside-50 -> scoring-shot creation and quality -> conversion`

Key controls applied:
- current shot-chain and territory evidence outranks old scoring/H2H;
- winner and handicap are separate thresholds;
- conversion is less stable than territory/shot creation;
- low/close, low/separation, high/close and high/separation branches are all tested;
- a streak is used only after assessing whether its mechanism persists;
- the latest meeting is reconciled rather than copied forward automatically;
- weather does not create an automatic Under;
- every contract is derived from one coherent game corridor.

---

## 3. Current selection and availability

### Geelong
Official club selection named:
- **IN:** Max Holmes, Mark Blicavs, Oli Wiltshire
- **OUT:** Jack Martin, Sam De Koning, Jhye Clark, all omitted
- Holmes was named for his first AFL game since Round 19.
- Blicavs returns after being managed in Round 24.

**Mechanism impact:** Holmes restores high-end run and transition speed, while Blicavs adds structural flexibility around stoppage, wing and defensive coverage. Holmes' layoff also adds uncertainty because his full-match workload and sharpness cannot simply be assumed.

### Carlton
Official club selection named:
- **IN:** Wade Derksen
- **OUT:** Nick Haynes, injured
- **Will Hayward:** unavailable after failing to get through main training

**Mechanism impact:** losing Haynes removes an experienced defensive option against a Geelong forward group with multiple tall/medium scoring threats. Hayward's absence removes another forward option. Carlton otherwise retained a settled side.

### Final-team limitation
The official AFL live article confirmed that final teams were in, but its static text did not expose a complete readable late-change/interchange table in the frozen capture. Therefore **no additional late change is asserted** beyond the official club selections above.

---

## 4. Form and regime audit

### Geelong
- Entered finals on **six consecutive wins by an average margin of 35 points**.
- Important qualification: the AFL's own preview notes those six wins came against teams now out of contention.
- In the second half of the season, Geelong had **three losses from three against top-six opponents**, plus the loss to Carlton.
- Geelong's current process profile is elite: **1st in forward-half intercepts, inside-50 differential and points from the forward half**.
- Jeremy Cameron returned in Round 24 after missing five consecutive wins through a shoulder injury and had 22 disposals. Shannon Neale had 47 goals for the season and Ollie Henry 42.

**Interpretation:** the six-win streak is real but cannot be carried forward as a simple "hot team" coefficient. Its competition-quality limitation is material. The stronger reusable signal is Geelong's persistent ability to win territory and lock the ball in its front half.

### Carlton
- After a 1–8 start, the Blues produced an **11–1–2 record across the next 14 matches** during their revival.
- In the wildcard win over Melbourne, Carlton kicked **nine goals to three after quarter-time**.
- Since Josh Fraser took charge, Carlton had been the **second-stingiest side**, conceding about **75 points per game across 15 matches**.
- During that revival period, Carlton ranked **4th for defensive-50-to-inside-50 against** and **3rd for scores per inside-50 against**.
- Sam Walsh produced 39 disposals, seven clearances, seven score involvements and five inside-50s against Melbourne; his five-final career disposal average was 32.4.

**Interpretation:** Carlton's turnaround has a tangible mechanism: stronger possession control, transition and defensive efficiency rather than a bare win streak. That makes the Blues a genuine winner/separation threat.

---

## 5. Most-recent-meeting reconciliation

**Round 12, 2026 at the MCG: Carlton 12.16 (88) defeated Geelong 12.12 (84). Total: 172.**

The relevant mechanism was not merely the four-point final margin:
- Geelong led by 20 points midway through the second quarter.
- Carlton changed the shape of the game by moving the ball with more speed and changing angles.
- In the decisive late sequence Carlton won the clearance, went deep inside 50 and Patrick Cripps converted the response.

### What persists
Carlton's possession/transition identity and ability to escape a high press are still live and are directly relevant against Geelong's forward-half pressure.

### What changed
- Geelong now has Holmes and Blicavs back in the selected side.
- Carlton is without Haynes and Hayward.
- Geelong has had the week off; Carlton comes in on a six-day break after the wildcard final.
- Geelong's current forward-half territory profile remains competition-leading.

**Conclusion:** the May result is a real Carlton matchup warning, but it is not sufficient to project Carlton to a 12+ win automatically.

---

## 6. Weather and surface gate

- Current Melbourne conditions at the freeze were cloudy and cool.
- BOM's Melbourne/Olympic Park observation at 5:40 pm recorded approximately **15.2°C, northerly wind 24 km/h with gusts to 35 km/h, and 0 mm rain since 9 am**.
- The broader Melbourne forecast was mostly cloudy and breezy.
- A severe-wind warning existed for parts of Victoria, but the warning text's damaging-wind timing/locations did **not** justify treating the MCG game itself as a damaging-wind event at the pre-game cutoff.
- **Current MCG turf/surface condition:** `NOT independently verified from an official current surface report`.

**Forecast implication:** some breeze increases kicking/ball-use variance, but the evidence does **not** support a weather-driven automatic Under.

---

## 7. Qualitative game corridor

Because no fitted or validated numerical model exists, this is a qualitative scenario corridor rather than a published probability distribution.

### Lower-scoring / control branch
**Approximate total family: 145–160**
- Carlton's improved defensive-50 control reduces clean Geelong shots.
- Finals pressure and possession control slow repeat scoring chains.
- Geelong still wins enough territory to prevent a large Carlton separation.

### Central branch
**Approximate total family: 158–174**
- Geelong wins more forward-half territory.
- Carlton still generates transition exits and periods of possession control.
- The margin remains mostly within about 10 points either way, with a slight Geelong game-winner lean.

### High-scoring branch
**Approximate total family: 176–190+**
- Geelong pressure creates repeated short-field shots and Carlton also breaks the press into open transition.
- Carlton's loss of Haynes is exposed by Geelong's Cameron/Neale/Henry forward mix.
- Conversion runs above ordinary expectation.

### Carlton separation / kill path
Carlton -11.5 becomes the leading outcome if Carlton repeatedly beats Geelong's first pressure layer, wins the important centre-clearance moments and forces the Cats into inefficient chase/transition defence, while Geelong's weaker record against high-end opposition proves more representative than its six-win close to the season.

### Geelong separation branch
Geelong can also create a 12+ margin if its league-leading forward-half intercept and inside-50 profile overwhelms Carlton's exits and Carlton's depleted defensive personnel cannot absorb the repeat-entry load.

---

## 8. Ranked forecast — exact supplied contracts

| Rank | Contract | Forecast status | Why it ranks here |
|---:|---|---|---|
| **1** | **Geelong +11.5** | **BEST / strongest relative lean** | The most robust contract across the central game tree. It survives a Geelong win, a draw, and Carlton wins by up to 11. Carlton's current regime and same-venue H2H make a Blues win plausible, but they do not make a 12+ separation the central requirement. Geelong's territory profile, week off and returning Holmes/Blicavs provide several independent paths to staying inside the cushion. |
| **2** | **Under 165.5** | **LEAN — lower confidence than Rank #1** | Carlton's defensive revival and elimination-final pressure support a lower-scoring path. However 165.5 sits inside the central corridor, the most recent H2H totalled 172, Geelong's forward-half scoring engine is strong and Carlton is missing Haynes. This is therefore only a modest directional edge, not a high-confidence Under. |
| **3** | **Over 165.5** | **LIVE ALTERNATIVE / slightly below Under** | The Over has a credible route through Geelong repeat entries, Carlton transition scoring and the weakened Carlton defensive matchup. It ranks just below the Under because Carlton's recent defensive control and finals context modestly favour a more compressed scoring environment. The total threshold remains central and uncertain. |
| **4** | **Carlton -11.5** | **LEAST LIKELY of supplied rows** | Carlton can absolutely win, but this contract specifically needs 12+ points. The strongest Carlton evidence supports matchup competitiveness and a viable winner branch more clearly than it supports sustained separation. Geelong +11.5 and Carlton -11.5 are not equivalent to the winner call. |

---

## 9. Potential game winner

### **Geelong Cats — narrow lean**

The winner call is deliberately weaker than Rank #1 Geelong +11.5.

The deciding factors are:
1. Geelong's league-leading forward-half intercept, inside-50 differential and forward-half scoring structure.
2. A week off versus Carlton's six-day turnaround.
3. Holmes and Blicavs returning.
4. Carlton's Haynes/Hayward absences.
5. Carlton's transition and defensive revival remains a strong adverse branch, which is why the winner call is **narrow rather than strong**.

**Representative central score shape only, not a model projection:** Geelong by roughly one to two goals, with the total clustering near the 165.5 threshold.

---

## 10. Evidence quality and limitations

- **Identity / venue / start:** HIGH — official AFL.
- **Selected-team changes:** HIGH — official club sources.
- **Final-team status:** HIGH for "final teams in"; MEDIUM for exact late-change detail because the static live article did not render the full final team table.
- **Current tactical/form profile:** HIGH/MEDIUM-HIGH — official AFL analytical preview and official match centre.
- **Weather:** HIGH for observed Melbourne/Olympic Park conditions; current MCG turf condition not independently verified.
- **Full L5/L10/L15/L20 exact threshold hit-rate reconstruction:** **NOT COMPLETED from an official stat feed before the pre-bounce cutoff.** No hit rates are invented. Current-regime summaries and the most recent meeting are used descriptively instead.
- **Operator settlement rules:** UNKNOWN.
- **Validated probabilities / edge / ROI / staking:** NOT AVAILABLE / NOT AUTHORISED.

---

# SOURCE REGISTER — P-272

## A. Google Drive governing framework, read-only
1. `PREDICTION_LOG_COMBINED_2.md` — active canonical log; P-272 next ID at opening; probability/value gates and append rules.
2. `README.md` — active workflow, source order, pre-game cutoff, corridor and settlement workflow.
3. `LEARNING_REGISTER.md` — current v3.4 method state and promoted controls, including AFL scoring-chain/coherence/streak/most-recent-meeting controls.
4. `RULES_AFL.md` — AFL identity, participant, territory, scoring-chain, context, branch and source rules.
5. `MODEL_AND_DATA_SPEC.md` — method-version history through MDS-2026.09.04-v3.4 and numerical publication boundary.

**Drive modification:** NONE.

## B. Official AFL / club sources
1. AFL — Finals week-two fixture:  
   https://www.afl.com.au/news/1597385/finals-fixture-ticket-details-schedule-confirmed-for-week-two-of-the-2026-finals-series

2. AFL — Elimination Final mega-preview, current form, tactical rankings, H2H, player context:  
   https://www.afl.com.au/news/1600128/mega-preview-cats-v-blues-stats-that-matter-who-wins-and-why

3. AFL — Current live pre-game article confirming final-team state:  
   https://www.afl.com.au/news/1601434/live-cats-take-on-hot-blues-in-elimination-final-blockbuster-at-the-g

4. AFL — Round 12 Carlton v Geelong official match centre and match report:  
   https://www.afl.com.au/afl/matches/8140

5. Geelong Cats — official elimination-final team selection:  
   https://www.geelongcats.com.au/news/2119044/afl-team-selection-cats-make-three-changes-for-elimination-final

6. Carlton — official elimination-final team news:  
   https://www.carltonfc.com.au/news/2119507/afl-team-news-one-change-for-cats-elimination-final

## C. Weather
1. Australian Bureau of Meteorology — Melbourne (Olympic Park) observations / current observation feed:  
   https://www.bom.gov.au/products/IDV60801/IDV60801.95936.shtml

2. Current Melbourne forecast card retrieved in-session at 19:31 AEST, including current cloudy conditions and the contemporaneous BOM severe-weather warning text.

---

# NEXT-QUERY OPERATING RULE

1. Keep every incomplete/unsettled card in the **UNSETTLED / INCOMPLETE QUEUE** at the top.
2. On the next query, state-check P-272 first.
3. If P-272 is final, perform settlement only unless the user explicitly asks for retrospective analysis; the user explicitly said **do not do a retrospective yet** for this card.
4. Once settled, move P-272 from the top unsettled queue into the normal settled chronology.
5. Preserve the frozen forecast unchanged.
6. Record every source used for settlement or any future analysis.
7. Re-read the current Drive method/version before issuing the next canonical local card.
8. Next local forecast ID: **P-273**, subject to reconciliation with the current Drive canonical snapshot.

---

# P-281 — Rakuten Monkeys @ Fubon Guardians — 2026 CPBL Regular Season

## 1. Frozen identity, state and supplied contracts

- **Local continuation ID:** `P-281`
- **Canonical-ID note:** the read-only Drive snapshot still lists P-280 as next because local P-280/P-281 have not been imported into Drive; this local mirror does not reuse an issued ID.
- **Sport:** Baseball
- **League:** Chinese Professional Baseball League (CPBL), first-team regular season
- **Event:** Rakuten Monkeys @ Fubon Guardians
- **Official CPBL event:** GAME307
- **Venue:** Taipei Dome (`大巨蛋`)
- **Scheduled start:** Friday 4 September 2026, 18:35 Taiwan / 20:35 Australia/Melbourne
- **Information/state cutoff:** **2026-09-04 20:13:51 Australia/Melbourne / 18:13:51 Taiwan**
- **Cutoff invariant:** PASS — about 21 minutes before scheduled first pitch
- **Official event state at final refresh:** **NOT STARTED / PREPARING (`未開始 / 比賽準備中`)**
- **Method:** `MDS-2026.09.04-v3.4`
- **Algorithms:** `GFA-2 + SFA-BASEBALL`
- **Numerical state:** `NTS-2026.09.02-v0.3 — Stage 0 / pre-fit`
- **Probability:** `NOT GENERATED / NOT PUBLISHED`
- **Value / ROI / staking:** `NOT AUTHORISED`
- **Retrospective:** **NOT PERFORMED — explicitly deferred by user**

### Exact user-supplied slate

| Contract ID | Contract | Ordinary geometry |
|---|---|---|
| `P-281-C01` | **Rakuten Monkeys -1.5** | Rakuten must win by 2+ runs |
| `P-281-C02` | **Fubon Guardians +1.5** | Fubon wins/ties under operator rules or loses by exactly 1 run |
| `P-281-C03` | **Combined Over 6.5** | 7+ settled runs |
| `P-281-C04` | **Combined Under 6.5** | 6 or fewer settled runs |

**Operator/listed-pitcher/action/shortening terms:** `UNKNOWN_DEFINITION` because the sportsbook/operator was not supplied.

---

## 2. Governing baseball controls applied

The active Drive baseball procedure is:

`lineup PA -> starter BF/pitches/innings/hook -> arsenal/contact -> relief chain -> park/defence -> base-out sequencing/HR clusters -> home ninth/extras -> one joint run object`

Key controls used on this card:

1. **Starter identity precedes starter quality.**
2. **Unposted lineups remain mixtures.**
3. **A low total does not imply a close margin.**
4. **For +1.5, separate Fubon win, one-run loss and 2+-run loss branches.**
5. **The joint early-hook/cluster state must be tested before ranking an Under.**
6. **Home batting entitlement is state-dependent.**
7. **Extra innings have a materially different scoring environment in CPBL because the tiebreak procedure seeds the inning with a runner in scoring position.**
8. **Recent H2H and same-series scores are descriptive context unless a current mechanism persists.**
9. **CPBL remains its own population; MLB/NPB/KBO priors are not silently transferred.**

---

## 3. Precondition / evidence-gate status

| Gate | Status | Frozen finding |
|---|---|---|
| `BB-P1` official starter identity | **PARTIAL** | Same-day/previous-day probable-starter reporting named **威能帝** for Rakuten and **江國豪** for Fubon, but the static official CPBL GAME307 page had not exposed the starter fields at the final refresh. They are therefore treated as **PROBABLE / NOT OFFICIALLY HANDSHAKEN** rather than upgraded to confirmed. |
| `BB-P2` posted lineups / catcher / defence | **PARTIAL** | Complete official batting orders and defensive alignments were not exposed in the static official event page before the freeze. Lineups stay as mixtures; no player prop is issued. |
| `BB-P3` league / innings / extras / DH | **PASS for league and scheduled format; operator terms unknown** | CPBL regular season, nine regulation innings; league materials show tiebreak extras can extend through the 12th. |
| `BB-P4` termination/action | **PARTIAL** | League framework known, but sportsbook action/shortening/listed-pitcher rules are not supplied. |
| `BB-P5` home last bat | **PASS** | Fubon is home at Taipei Dome. |

### Consequence

The forecast order is **qualitative and confidence-capped**. The probable starter matchup is used as a conditional branch, not falsely presented as a fully confirmed official starter state.

---

## 4. Probable starting-pitcher branch

### Rakuten probable: 威能帝 (Pedro Fernandez)

The official CPBL advanced player profile shows a strong 2026 run-prevention/process profile:

- opponent batting average approximately **.223**
- opponent on-base percentage approximately **.260**
- strikeout rate **25.6%**
- walk rate **3.9%**
- hard-hit rate approximately **22.8%**
- fastball average roughly **149.3 km/h**
- high strikeout/low-walk profile relative to the league

Same-day probable-starter reporting listed:
- **7-4, 2.27 ERA** in 2026
- **1-0, 1.80 ERA vs Fubon** in 2026

Recent official start:
- **28 August vs Uni-President at Taipei Dome:** 7 IP, 4 H, 7 K, 2 BB, 4 ER, 94 pitches.

Direct 2026 Fubon meeting:
- **26 June:** 5 IP, 3 H, 6 K, 0 BB, 1 ER, 71 pitches in a 3-1 Rakuten win.

### Interpretation

The decision-driving mechanism, **conditional on him actually starting**, is not the 2.27 ERA by itself. It is the combination of strikeout ability, very low walk rate and limited hard contact, which reduces free baserunners and lowers Fubon's route to multi-run innings.

However, his 28 August four-run outing and earlier higher-contact starts preserve the mandatory sequencing/contact tail. He is not treated as a deterministic shutdown arm.

---

### Fubon probable: 江國豪

Probable-starter reporting listed:
- **2-2, 3.93 ERA** in 2026
- 0.00 ERA vs Rakuten in the small 2026 sample.

The official CPBL advanced profile is less dominant than 威能帝's:
- opponent batting average about **.289**
- opponent on-base percentage about **.392**
- strikeout rate about **11.0%**
- walk rate about **12.7%**
- hard-hit rate about **36.5%**
- fastball average about **143.3 km/h**

Recent official outings included:
- **28 August vs CTBC:** 4.2 IP, 7 H, 3 K, 4 BB, 2 ER, 80 pitches.
- **16 August:** 5 IP, 3 H, 6 K, 1 ER, 90 pitches.

His 2026 0.00 ERA against Rakuten came from a **small relief sample**, not a fully comparable current starting-role sample. It is therefore not treated as proof that he "owns" this lineup.

### Interpretation

The main danger to the Under and Fubon +1.5 is **baserunner accumulation**. A low strikeout/high-walk profile gives Rakuten more opportunities for sequencing, and a 4–5 inning hook can move substantial exposure into Fubon's middle relief.

This is the strongest Monkeys -1.5 / Over kill path.

---

## 5. Current team / recent-regime evidence

A same-day pregame report using the current CPBL table listed:
- **Rakuten: 18-15, .545, 1st in the second-half standings**
- **Fubon: 15-20, .429, 6th, four games back**

This is contextual strength evidence only, not a substitute for the starter/lineup/run-distribution chain.

### Rakuten

Recent official results demonstrate both low-run and cluster states:
- **25 Aug:** Rakuten 11-1 CTBC at Taipei Dome.
- **28 Aug:** Rakuten 0-4 Uni-President at Taipei Dome.
- **30 Aug:** Rakuten 4-5 Uni-President at Taipei Dome.
- **2 Sep:** Rakuten won 5-4 over Wei Chuan in 10 innings.

The 11-run game shows the offensive-cluster ceiling cannot be discarded. The 0-run and 4-run Dome results show that the centre is not a simple high-scoring trend.

Rakuten also had the 3 September game postponed, reducing immediate back-to-back bullpen stress compared with a team coming directly from a played game.

### Fubon

Recent official results included:
- **26 Aug:** Fubon 5-4 TSG.
- **28 Aug:** Fubon 4-5 CTBC in 11 innings.
- **29 Aug:** Fubon 6-4 CTBC.
- **30 Aug:** Fubon 1-6 CTBC.
- **2 Sep:** official schedule/score feed ultimately showed Fubon losing **1-6** to Uni-President at Taipei Dome.

This is a mixed offensive regime rather than a clean Under streak. The important matchup-specific suppression mechanism is the probable 威能帝 profile, not a generic claim that Fubon "cannot score."

---

## 6. Head-to-head and Taipei Dome reconciliation

Relevant 2026 official CPBL results include:

- 22 May: Rakuten 3-2 Fubon — total 5
- 26 June: Rakuten 3-1 Fubon — total 4
- 27 June: Fubon 9-2 Rakuten — total 11
- 7 July: Rakuten 5-3 Fubon — total 8
- 8 July: Rakuten 1-0 Fubon — total 1

### Same-venue Taipei Dome series, 24–26 July

- **24 July:** Fubon 6-5 Rakuten after 12 innings. Importantly, it was **4-4 after nine**, then rose to 11 final runs through extras.
- **25 July:** Rakuten 3-2 Fubon — total 5.
- **26 July:** Rakuten 2-0 Fubon — total 2.

The same-venue July series therefore supplies two distinct lessons:

1. regulation/central matchup states can be very low scoring;
2. **extra innings can destroy an otherwise correct Under read**.

Historical matchup results are not used as automatic coefficients because starters, lineups and bullpen states differ. Their strongest current use is structural: they confirm that both 2–5 run regulation states and extra-inning scoring tails are plausible in this matchup/venue.

---

## 7. Venue and termination environment

**Taipei Dome is an indoor venue.**

Therefore:
- external rain is **not used as a direct Under driver**;
- ordinary outdoor wind/temperature effects are not decision-driving;
- the in-game weather termination branch is materially smaller than for an exposed outdoor CPBL venue.

Operator-specific suspension/action rules remain unknown, so no sportsbook settlement claim is made.

---

## 8. CPBL extra-innings branch

League rule material states that regular-season games are scheduled for nine innings and, if tied, can proceed under the tiebreak procedure through the 12th inning.

Official 2026 CPBL game reporting explicitly describes the extra-inning **tiebreak runner at second base**.

That matters sharply at **6.5 runs**:

- 3-3 after nine is still an Under at the regulation endpoint, but **one extra-inning run makes 7** and flips the game Over.
- 2-2 after nine leaves more room, but the seeded runner raises the per-inning run environment above an ordinary regulation inning.
- Extra innings also increase the chance that a +1.5 cushion survives a one-run final.

This is the primary structural reason the Under cannot be called high confidence despite a low central regulation tree.

---

## 9. Joint qualitative run tree

There is no fitted/validated CPBL numerical model, so the following are scenario families rather than probabilities.

### `BB-B1` — central starter-length state

Conditional on the expected starters:
- **Rakuten 3-2 Fubon**
- **Rakuten 3-1 Fubon**
- **Rakuten 2-1 Fubon**

Mechanism:
- 威能帝 limits free passes and Fubon multi-run innings;
- 江國豪 allows baserunners but avoids a full sequencing collapse;
- relief innings remain ordinary rather than explosive.

Contract effect:
- Under 6.5 is strong in this branch.
- Fubon +1.5 wins in 3-2 / 2-1.
- Rakuten -1.5 wins in 3-1.

### `BB-B2` — joint early-hook / relief exposure

Representative:
- **Rakuten 5-2**
- **Rakuten 5-3**
- **Fubon 4-3**

Mechanism:
- 江國豪's walk/contact profile forces an early transition, or 威能帝 has an inefficient/high-contact start;
- inherited runners and middle relief create the first multi-run inning.

Contract effect:
- Over 6.5 becomes live.
- Rakuten -1.5 is strongly linked to the 5-2/5-3 branches.

### `BB-B3` — sequencing / home-run cluster

A single 3-run inning can move a 1-1 or 2-1 game immediately toward the threshold. This matters especially because 6.5 is low: the Over does not require a true slugfest.

### `BB-B4` — low-total separation

Representative:
- **Rakuten 4-0**
- **Rakuten 4-1**
- **Rakuten 3-0**

This branch defeats the false inference that a low total automatically protects Fubon +1.5. If 威能帝 suppresses Fubon to 0–1 and Rakuten clusters one inning, **Under 6.5 and Monkeys -1.5 can win together**.

### `BB-B5` / `BB-B9` — late relief separation

Representative:
- game 2-1 or 2-2 after six/seven innings;
- one bullpen transition produces a two- or three-run late inning;
- final becomes 4-1, 4-2 or 5-2.

This is a key kill path against Fubon +1.5 and the Under.

### `BB-B6` — home ninth

Fubon bats last. If Fubon leads after Rakuten's ninth, the bottom of the ninth is not played, slightly capping total exposure in that branch. If Fubon trails or is tied, it retains its final regulation plate appearances, which supports the +1.5 cushion and upset branch.

### `BB-B7` — extra innings

Representative:
- 3-3 after nine -> 4-3 / 5-3 type final.
- 2-2 after nine -> 3-2 / 4-3 type final.

The tiebreak runner materially elevates run risk compared with simply extending the regulation scoring rate.

### `BB-B8` — termination

Indoor venue substantially lowers direct rain-shortening risk, but exact operator action rules remain unknown.

---

## 10. Ranked exact-contract forecast

| Rank | Contract | Verdict | Why |
|---:|---|---|---|
| **1** | **Under 6.5 runs** | **BEST RELATIVE LEAN — confidence capped** | Conditional on the expected pitchers, 威能帝's K/BB/contact profile is the best run-suppression mechanism in the matchup, while 江國豪's recent starts still support a viable 4–5 inning ordinary branch. Multiple 2026 H2Hs and two of three July Dome finals landed at five or fewer. The main kill paths are 江國豪's baserunner/early-hook state, one clustered inning, and CPBL tiebreak extras. |
| **2** | **Fubon Guardians +1.5** | **LEAN / very close to #1** | Low-run states create many 2-1 and 3-2 finals, and Fubon owns the home last bat. This cushion also survives a Fubon win and exactly-one-run loss. It ranks below the Under because Rakuten's probable starter edge creates a real 3-1/4-1 low-total separation branch. |
| **3** | **Rakuten Monkeys -1.5** | **LIVE SEPARATION ALTERNATIVE** | If 威能帝 starts as expected and Fubon is held to 0–2, Rakuten needs only one clustered inning to clear the run line in a 3-1, 4-1 or 5-2 game. 江國豪's walk/contact profile increases that route. The handicap is still less robust than simply backing Rakuten to win because many central low-total states finish by one run. |
| **4** | **Over 6.5 runs** | **LEAST LIKELY, but material kill path** | 6.5 is low enough that one early-hook/cluster inning or 3-3 regulation tie can flip the game Over. The Over is not remote. It ranks fourth because the central expected-starter and same-venue matchup state is more naturally 3–5 total runs than 7+. |

### Important ordinal note

**Ranks #1 and #2 are close.** Because the starters and final orders were not officially handshaken in the static event page at freeze, neither is promoted beyond a qualitative lean.

---

## 11. Potential game winner

### **Rakuten Monkeys — narrow-to-moderate qualitative lean**

Why:
1. conditional probable-starter advantage through 威能帝's superior strikeout, walk and contact-control profile;
2. his direct 26 June Fubon outing was efficient and low-damage;
3. Rakuten has demonstrated both a low-run win path and a late cluster path in this matchup;
4. Fubon's home last bat and strong one-run-game branches prevent the outright lean from becoming high confidence.

### Representative central shape

**Rakuten 3-2 or 3-1 Fubon.**

This is a scenario anchor only, **not a calibrated score prediction**.

---

## 12. Coherence / implied-target reconciliation

Rank #1 Under 6.5 implies a central total target of **0–6 runs**.

- **Fubon +1.5:** `COHERENT` with 2-1, 3-2, 2-2 regulation / one-run final branches.
- **Rakuten -1.5:** `PARTIAL_OVERLAP`, coherent with 3-1, 4-1, 4-0.
- **Over 6.5:** `DISJOINT` from the rank-one central state and requires the early-hook/cluster/extra-inning kill path.

Winner reconciliation:
- Under + Rakuten winner is coherent through 2-1 / 3-1 / 3-2.
- Under + Fubon +1.5 is also coherent through a one-run Rakuten win.
- Therefore the winner lean does **not** mechanically determine the run-line choice.

---

## 13. Evidence / honesty boundary

- Official event identity/state: **HIGH** — CPBL GAME307.
- Venue/home-last-bat: **HIGH** — official CPBL.
- Probable starters: **MEDIUM** — same-day/previous-day probable-starter report; **not promoted to confirmed official** because static CPBL event page had not exposed the fields at freeze.
- Starter advanced profiles: **HIGH once participant identity is conditional** — official CPBL advanced player pages.
- Final posted batting orders: **NOT VERIFIED** at frozen cutoff.
- Recent/H2H results: **HIGH factual quality** — official CPBL advanced game pages.
- H2H predictive weight: **LOW/MEDIUM**, because current participant continuity is incomplete.
- Venue/weather: **HIGH that venue is Taipei Dome; external weather not used as a directional game input**.
- Operator action / listed-pitcher / shortening rules: **UNKNOWN_DEFINITION**.
- Calibrated probability / edge / ROI / staking: **NOT AVAILABLE / NOT AUTHORISED**.
- Retrospective: **NOT PERFORMED**.

---

# SOURCE REGISTER — P-281

## A. Google Drive governing framework — READ ONLY

1. `PREDICTION_LOG_COMBINED_2.md`
   - active read-only canonical authority;
   - fresh snapshot still lists P-280 because local cards have not been imported;
   - MDS-2026.09.04-v3.4;
   - no calibrated probability/value claims authorised.

2. `RULES_BASEBALL.md`
   - active v3.4 baseball process;
   - starter/lineup preconditions;
   - joint starter-hook/relief/cluster, home-ninth and extra-inning branches;
   - CPBL treated as a separate population.

3. `LEARNING_REGISTER.md`
   - promoted general and sport-specific controls carried forward.

**Drive changes made:** NONE.

## B. Official CPBL sources

1. **GAME307 — Rakuten Monkeys vs Fubon Guardians, 4 Sep 2026**
   https://stats.cpbl.com.tw/schedule/2026-A-307
   - fixture, venue, date, official `NOT STARTED` state.

2. **威能帝 official advanced player profile**
   https://stats.cpbl.com.tw/players/0000007062
   - opponent batting/on-base, K%, BB%, hard-hit and pitch velocity profile.

3. **26 Jun 2026 — Rakuten 3-1 Fubon**
   https://stats.cpbl.com.tw/schedule/2026-A-80
   - direct 威能帝/Fubon sample; 5 IP, 3 H, 6 K, 0 BB, 1 ER.

4. **28 Aug 2026 — Uni-President 4-0 Rakuten**
   https://stats.cpbl.com.tw/schedule/2026-A-293
   - 威能帝 recent start; 7 IP, 4 H, 7 K, 2 BB, 4 ER, 94 pitches.

5. **7 Jul 2026 — Rakuten 5-3 Fubon**
   https://stats.cpbl.com.tw/schedule/2026-A-190

6. **8 Jul 2026 — Rakuten 1-0 Fubon**
   https://stats.cpbl.com.tw/schedule/2026-A-192

7. **24 Jul 2026 — Fubon 6-5 Rakuten, 12 innings**
   https://stats.cpbl.com.tw/schedule/2026-A-219
   - 4-4 through nine; extra-inning total expansion.

8. **25 Jul 2026 — Fubon 2-3 Rakuten**
   https://stats.cpbl.com.tw/schedule/2026-A-222

9. **26 Jul 2026 — Fubon 0-2 Rakuten**
   https://stats.cpbl.com.tw/schedule/2026-A-225

10. **25 Aug 2026 — Rakuten 11-1 CTBC**
    https://stats.cpbl.com.tw/schedule/2026-A-286

11. **30 Aug 2026 — Uni-President 5-4 Rakuten**
    https://stats.cpbl.com.tw/schedule/2026-A-300

12. **26 Aug 2026 — TSG 4-5 Fubon**
    https://stats.cpbl.com.tw/schedule/2026-A-290

13. **28 Aug 2026 — Fubon 4-5 CTBC, 11 innings**
    https://stats.cpbl.com.tw/schedule/2026-A-292

14. **29 Aug 2026 — Fubon 6-4 CTBC**
    https://stats.cpbl.com.tw/schedule/2026-A-295

15. **30 Aug 2026 — Fubon 1-6 CTBC**
    https://stats.cpbl.com.tw/schedule/2026-A-299

16. **2 Sep official CPBL schedule/game feed**
    https://stats.cpbl.com.tw/schedule
    - latest official schedule/result-state context.

17. **CPBL official rule supplement — extra innings**
    https://cpbl.com.tw/theme/client/download/%E8%A3%81%E5%88%A4%E5%9F%B7%E6%B3%95%E6%89%8B%E5%86%8A%E8%A6%8F%E5%89%87%E8%A3%9C%E8%BF%B0.pdf
    - regular season nine innings; tiebreak extras; maximum 12 innings.

18. **Official CPBL 2026 game report demonstrating the tiebreak runner at second**
    https://cpbl.com.tw/box/news?gameSno=220&kindCode=A&year=2026

19. **Official CPBL report for 24 Jul Fubon–Rakuten 12-inning game**
    https://cpbl.com.tw/box/news?gameSno=219&kindCode=A&year=2026

## C. Same-day starter/standings reporting and secondary corroboration

20. **NOWnews — 4 Sep 2026 CPBL pregame report**
    https://www.nownews.com/news/6872173
    - same-day matchup lists **江國豪 vs 威能帝**;
    - pregame second-half standings: Rakuten 18-15, Fubon 15-20.
    - Use classification: current media confirmation, but not a substitute for `BB-P1` official-field-owner handshake.

21. **PTT Monkeys board — 9/4 probable starters**
    https://www.ptt.cc/bbs/Monkeys/M.1788429861.A.BAA.html
    - 威能帝 vs 江國豪, scheduled 18:35.
    - **Use classification: secondary probable-starter source only.**
    - It was **not** used to claim official final starter confirmation.

---

## 14. Local running-log state after P-281

### Unsettled / incomplete queue

1. `LOCAL-GEELONG-20260904` — Geelong Cats vs Carlton — unresolved local record.
2. `P-280` — South Sydney Rabbitohs vs Sydney Roosters — unsettled.
3. `P-281` — Rakuten Monkeys @ Fubon Guardians — **PREGAME / unsettled**.

### Settlement / retrospective control

- No retrospective performed for P-281.
- Do not rewrite the frozen ranked order after the result.
- When the user requests settlement/cleanup, use official final state first, then move the settled card from the top unresolved queue into settled chronology.
- Record every settlement source.
- Next local continuation ID: **P-282**, subject to fresh Drive reconciliation before issue.

---

# P-282 — TSG Hawks @ Uni-Lions — 2026 CPBL Regular Season

## 1. Frozen identity and contracts

- **Local continuation ID:** `P-282`
- **Canonical reconciliation:** read-only Drive snapshot still lists `P-280` as next because local P-280/P-281/P-282 have not been imported into Drive; issued local IDs are not reused.
- **Sport:** Baseball
- **League:** Chinese Professional Baseball League (CPBL), first-team regular season
- **Official event:** GAME308
- **Event:** TSG Hawks (`台鋼雄鷹`) @ Uni-President 7-ELEVEN Lions (`統一7-ELEVEn獅`)
- **Venue:** Asia-Pacific International Baseball Stadium main field (`亞太主`), Tainan
- **Scheduled first pitch:** 2026-09-04 18:35 Taiwan / 20:35 Australia/Melbourne
- **Information/state cutoff:** **2026-09-04 20:31:53 Australia/Melbourne / 18:31:53 Taiwan**
- **Official state at final refresh:** **NOT STARTED / PREPARING (`未開始 / 比賽準備中`)**
- **Method:** `MDS-2026.09.04-v3.4`
- **Algorithms:** `GFA-2 + SFA-BASEBALL`
- **Numerical state:** `NTS-2026.09.02-v0.3 — Stage 0 / pre-fit`
- **Probability / edge / staking:** `NOT GENERATED / NOT AUTHORISED`
- **Retrospective:** **NOT PERFORMED — user explicitly deferred**

### Exact supplied slate

| Contract | Ordinary geometry |
|---|---|
| **TSG Hawks -1.5** | Hawks must win by 2+ |
| **Uni-Lions +1.5** | Lions win or lose by exactly one run under normal settlement geometry |
| **Over 6.5** | 7+ settled runs |
| **Under 6.5** | 6 or fewer settled runs |

**Operator/listed-pitcher/rain-shortening/action terms:** `UNKNOWN_DEFINITION`; operator was not supplied.

---

## 2. Baseball precondition audit

| Gate | Status | Frozen finding |
|---|---|---|
| `BB-P1` starter identity | **PARTIAL** | Same-day reporting names **Eric Stout / 艾速特** for TSG and **Brock Dykxhoorn / 布雷克** for Uni. The static official CPBL event page did not expose starter names before freeze, so they remain probable rather than falsely promoted to `CONFIRMED_OFFICIAL`. |
| `BB-P2` posted batting orders | **PARTIAL** | Complete official orders/catcher/defensive alignment were not visible in the static event page before freeze. No player prop is issued. |
| `BB-P3` league/rules | **PASS for competition and nine-inning regulation structure** | CPBL first-team regular season. |
| `BB-P4` termination/action | **PARTIAL** | Current rain risk is material; operator shortening/suspension/action rules are unknown. |
| `BB-P5` home last bat | **PASS** | Uni-Lions are home. |

**Consequence:** all four rows are qualitative, confidence-capped forecasts. Starter-driven analysis is explicitly conditional on Stout–Dykxhoorn being the actual matchup.

---

## 3. Probable starting pitchers

### TSG probable — Eric Stout (`艾速特`)

Official CPBL 2026 profile:
- opponent AVG about **.190**
- opponent OBP about **.273**
- opponent SLG about **.235**
- strikeout rate **23.5%**
- walk rate **7.7%**
- hard-hit rate about **15.6%**
- whiff rate about **27.9%**
- fastball average roughly **146.6 km/h**
- 2026 ERA listed by CPBL leaderboard: **1.81**, third-best qualified mark
- 2026 record entering the game: **9-5**

Latest official start:
- **28 Aug @ Wei Chuan:** 6 IP, 4 H, 5 K, 1 ER, 100 pitches; TSG won 7-4.

### Direct 2026 Uni-Lions evidence

Official CPBL game pages show:
- **22 May:** 7 IP, 5 H, 5 K, 0 BB, 1 ER; TSG won 3-1.
- **19 Jun at this venue:** 7 IP, 4 H, 9 K, 1 BB, 0 ER; TSG won 1-0.
- **3 Jul:** 6 IP, 3 H, 4 K, 0 ER; TSG won 6-3.

Same-day probable-starter reporting summarised Stout as **3-0 with a 0.84 ERA versus Uni in 2026**.

### Mechanism

Stout supplies the strongest single run-suppression mechanism:
- very low opponent batting average;
- strong strikeout/whiff profile;
- unusually low hard-contact rate;
- repeated current-season success against the same opponent.

The direct H2H is supportive only because the current pitcher/club matchup is still continuous; it is **not** treated as automatic future ownership.

---

### Uni probable — Brock Dykxhoorn (`布雷克`)

Official CPBL 2026 profile:
- opponent AVG about **.241**
- opponent OBP about **.261**
- opponent SLG about **.313**
- strikeout rate **16.1%**
- walk rate only **2.6%**
- hard-hit rate about **26.0%**
- chase rate approximately **35.8%**
- fastball average around **142.6 km/h**
- CPBL qualified ERA leaderboard: **1.79**, second-best
- entering record: **5-7**

Recent official starts:
- **28 Aug vs Rakuten:** 6 IP, 6 H, 6 K, **0 ER**, 94 pitches; Uni won 4-0.
- **21 Aug vs CTBC:** 7 IP, 2 H, 6 K, 1 BB, 1 ER; Uni ultimately lost 2-1.
- **31 Jul vs Rakuten:** 7 IP, 5 H, 6 K, 0 BB, 1 ER.

He has shown the ability to work deep while issuing very few free passes, which protects both the Under and Uni +1.5.

### TSG direct evidence

Same-day probable-starter reporting lists Dykxhoorn at **0-1, 1.84 ERA against TSG in 2026**. An official 23 May game shows:
- 7 IP, 6 H, 1 K, 0 BB, 2 ER in a 2-0 TSG win.

This is not a weak opponent-starter setup for TSG. The projected starter matchup is **elite versus elite**, not elite versus replacement-level pitching.

---

## 4. Same-matchup rain precedent

A particularly relevant official CPBL report from **7 April 2026** featured this same starting-pitcher pairing:

- Stout: 6 IP, 8 K, one unearned run.
- Dykxhoorn: 7.2 IP, 5 H, one run.
- Game was repeatedly interrupted by rain and ultimately called at **1-1**.

This is useful in two ways:

1. It confirms both starters can suppress this opponent in the current roster/pitching regime.
2. It shows rain is a **termination/state-management risk**, not simply an Under signal.

The Drive rules require the order to be:
`runs before stop -> stop before runs -> restart/relief transition -> official-game/no-action state`.

Because operator action terms were not supplied, no claim is made about how a shortened game would settle.

---

## 5. Current team state

Official CPBL second-half standings immediately before the card showed:
- **Uni-Lions: 19-19, .500, 4th**
- **TSG Hawks: 16-18, .471, 5th**
- both around the middle of a tightly packed second-half race.

Recent official TSG results:
- 28 Aug: **TSG 7-4 Wei Chuan**
- 29 Aug: **TSG 2-1 Wei Chuan**
- 30 Aug: **TSG 0-3 Wei Chuan**
- 1/2 Sep scheduled TSG games were affected by postponement, reducing immediate bullpen usage compared with a normal uninterrupted sequence.

Recent official Uni results:
- 28 Aug: **Uni 4-0 Rakuten**
- 29 Aug: **Uni 4-8 Rakuten**
- 30 Aug: **Uni 5-4 Rakuten**
- Uni's second-half record sits slightly above TSG's.

These results show no clean team-level Under streak. The Under case is therefore built primarily on **the Stout/Dykxhoorn exposure chain**, not on raw recent totals.

---

## 6. Head-to-head reconciliation

Relevant 2026 official results include:
- 22 May: **TSG 3-1 Uni** — total 4
- 23 May: **TSG 2-0 Uni** — total 2
- 24 May: **Uni 7-5 TSG** — total 12
- 19 Jun: **TSG 1-0 Uni** — total 1
- 3 Jul: **TSG 6-3 Uni** — total 9

This spread matters. The matchup has produced both:
- true run-suppression games;
- clustered 9–12 run states.

The current starter pairing makes the low-run family more relevant than the high-run games with different pitching contexts, but the cluster tail remains mandatory.

---

## 7. Weather / venue branch

Tainan conditions near freeze:
- around **27°C**
- overcast
- meaningful evening shower/rain probability
- Taiwan's Central Weather Administration described southern Taiwan as having occasional showers/thunderstorms with locally heavy rain possible.

This is an outdoor venue and weather therefore matters.

### Directional treatment

Rain does **not** create an automatic Under:
- interruptions can shorten starter rhythm;
- restarts can force earlier bullpen entry;
- wet conditions can create defensive mistakes or walks;
- a game can cross 6.5 before any stoppage;
- operator action may differ if the game is suspended or shortened.

Therefore weather lowers confidence rather than providing a one-way Under adjustment.

---

## 8. Joint score / branch tree

No fitted CPBL model is authorised. These are qualitative representative families.

### `BB-B1` — both starters at central length
Representative:
- **TSG 2-1**
- **TSG 3-1**
- **Uni 2-1**
- **TSG 3-2**

This is the dominant central family if both named starters take the mound and retain ordinary efficiency.

Contract effects:
- Under 6.5 wins.
- Uni +1.5 wins in every state except a 3-1 or wider TSG result.
- TSG winner remains slightly favoured because Stout has the stronger opponent-specific suppression record.

### `BB-B2` — early hook / rain interruption / relief transition
Representative:
- **TSG 4-3**
- **Uni 4-3**
- **TSG 5-2**

Mechanism:
- rain delay breaks starter continuity or pitch readiness;
- either starter exits before normal length;
- middle relief inherits runners;
- one transition inning crosses the total.

This is the principal kill path against the Under.

### `BB-B3` — sequencing / multi-run cluster
A two-out walk/single followed by extra-base contact can flip a 1-1 game to 4-1 quickly. At 6.5, only one additional scoring inning is then needed to threaten the Over.

### `BB-B4` — low-total separation
Representative:
- **TSG 4-0**
- **TSG 4-1**
- **Uni 4-0**

This prevents the false conclusion that low expected scoring automatically makes Uni +1.5 safe. Stout's suppression plus one TSG cluster can produce **Hawks -1.5 + Under 6.5 simultaneously**.

### `BB-B5/B9` — late relief separation
A 1-1 or 2-1 game can become 4-1/5-1 after the starters leave. This is especially relevant to the run-line ordering.

### `BB-B6` — home ninth
Uni bats last. If Uni leads after the top of the ninth, the bottom half is not played, which caps exposure. If Uni trails by one, it retains its final regulation plate appearances, structurally supporting +1.5.

### `BB-B7` — extra innings
A low-scoring tie after nine threatens the Under because CPBL tiebreak extras introduce a runner in scoring position. A 3-3 tie has already reached six; the first extra-inning run flips Over 6.5.

### `BB-B8` — rain termination
Current rain risk makes suspension/shortening material. Exact sportsbook action is unknown, so this branch is recorded but not given a settlement assumption.

---

## 9. Ranked four-contract forecast

| Rank | Contract | Verdict | Reason |
|---:|---|---|---|
| **1** | **Under 6.5 runs** | **BEST RELATIVE LEAN — confidence capped by rain/action and lineup uncertainty** | Both probable starters are top-three qualified CPBL ERA arms with strong underlying run-prevention profiles. Stout has repeated 2026 suppression of Uni, while Dykxhoorn's very low walk rate and recent deep quality starts constrain TSG. Central states cluster around 3–5 total runs. Rain interruption, early bullpen entry, a cluster inning and extras are the key kill paths. |
| **2** | **Uni-Lions +1.5** | **LEAN / close second** | Dykxhoorn is strong enough to keep the game close, Uni bats last, and most central Under states are 2-1/3-2 type games. This contract survives a Uni win and a one-run TSG win. It ranks behind the Under because Stout's opponent-specific dominance creates a real 3-1/4-1 TSG separation branch. |
| **3** | **TSG Hawks -1.5** | **LIVE SEPARATION ALTERNATIVE** | Stout gives TSG the better opponent-specific starter branch, and 3-1/4-1 is coherent with the Under. But asking TSG to win by 2+ against the league's No. 2 qualified ERA starter is materially more demanding than simply favouring TSG to win. |
| **4** | **Over 6.5 runs** | **LEAST LIKELY, but not remote** | 6.5 is low, so one rain-disrupted starter exit or clustered relief inning can create 4-3/5-2. Extra innings are another strong kill path. It ranks last because the central starter matchup has unusually strong suppression on both sides. |

---

## 10. Potential game winner

### **TSG Hawks — narrow lean**

The winner call is weaker than the Under.

Why TSG:
1. Stout's official process profile is stronger in strikeout/whiff/hard-contact suppression.
2. His current-season matchup history against Uni is exceptionally good.
3. TSG has won multiple low-scoring 2026 meetings in which Uni's offence was held to 0–1 runs.

Why only narrow:
1. Dykxhoorn is himself second in qualified CPBL ERA.
2. Uni has the home last bat.
3. Uni's second-half record is slightly better.
4. Rain/interruption creates additional variance.

### Representative central shapes
- **TSG 2-1**
- **TSG 3-1**
- **TSG 3-2**

These are scenario anchors, not calibrated score predictions.

---

## 11. Coherence audit

Rank #1 Under 6.5 implies a central total state of 0–6 runs.

- **Uni +1.5:** `COHERENT` through 2-1, 3-2, 1-0, 2-2-to-one-run-final families.
- **TSG -1.5:** `PARTIAL_OVERLAP` through 3-1, 4-1, 4-0.
- **Over 6.5:** `DISJOINT` from the central Under state; needs rain/early-hook/cluster/extras.

Winner reconciliation:
- TSG winner + Uni +1.5 is coherent through a one-run TSG victory.
- TSG winner + TSG -1.5 is a separate wider-margin branch.
- Therefore outright winner and run line are not conflated.

---

## 12. Evidence boundary

- Event identity / venue / pregame state: **HIGH — official CPBL GAME308**
- Current second-half standings: **HIGH — official CPBL**
- Starter identities: **MEDIUM-HIGH probable, not officially handshaken in static event page**
- Starter process data: **HIGH — official CPBL advanced player profiles**
- Direct starter/team game history: **HIGH factual quality — official CPBL**
- Final batting orders / catcher / defence: **NOT VERIFIED before freeze**
- Weather: **HIGH/MEDIUM-HIGH — government CWA plus contemporaneous forecast**
- Operator rain/listed-pitcher/action rules: **UNKNOWN**
- Published win probability / edge / ROI / staking: **NOT AUTHORISED**
- Retrospective: **NOT PERFORMED**

---

# SOURCE REGISTER — P-282

## A. Google Drive — read only

1. `PREDICTION_LOG_COMBINED_2.md`
   - current Drive authority;
   - snapshot still lists P-280 because local cards have not been imported;
   - MDS-2026.09.04-v3.4;
   - probability/value publication gates remain closed.

2. `RULES_BASEBALL.md`
   - SFA-BASEBALL;
   - official starter handshake requirement;
   - lineup mixture rule;
   - low-total separation;
   - joint early-hook and relief-cluster branches;
   - home ninth, extras and termination-order controls.

**Drive modification:** NONE.

## B. Official CPBL sources

1. GAME308 — TSG Hawks @ Uni-Lions
   https://stats.cpbl.com.tw/schedule/2026-A-308

2. Eric Stout official CPBL advanced profile
   https://stats.cpbl.com.tw/players/0000007053

3. Brock Dykxhoorn official CPBL advanced profile
   https://stats.cpbl.com.tw/players/0000005731

4. CPBL 2026 qualified leaderboard
   https://cpbl.com.tw/stats/toplist

5. CPBL 2026 second-half standings
   https://cpbl.com.tw/standings/season

6. 22 May — Uni 1-3 TSG
   https://stats.cpbl.com.tw/schedule/2026-A-115

7. 23 May — Uni 0-2 TSG; Dykxhoorn 7 IP, 2 ER
   https://stats.cpbl.com.tw/schedule/2026-A-116

8. 24 May — Uni 7-5 TSG
   https://stats.cpbl.com.tw/schedule/2026-A-120

9. 19 Jun — TSG 1-0 Uni; Stout 7 IP, 0 ER
   https://stats.cpbl.com.tw/schedule/2026-A-172

10. 3 Jul — Uni 3-6 TSG; Stout 6 IP, 0 ER
    https://stats.cpbl.com.tw/schedule/2026-A-181

11. 28 Aug — TSG 7-4 Wei Chuan; Stout 6 IP, 1 ER
    https://stats.cpbl.com.tw/schedule/2026-A-294

12. 29 Aug — TSG 2-1 Wei Chuan
    https://stats.cpbl.com.tw/schedule/2026-A-297

13. 30 Aug — TSG 0-3 Wei Chuan
    https://stats.cpbl.com.tw/schedule/2026-A-298

14. 28 Aug — Uni 4-0 Rakuten; Dykxhoorn 6 IP, 0 ER
    https://stats.cpbl.com.tw/schedule/2026-A-293

15. 29 Aug — Uni 4-8 Rakuten
    https://stats.cpbl.com.tw/schedule/2026-A-296

16. 30 Aug — Uni 5-4 Rakuten
    https://stats.cpbl.com.tw/schedule/2026-A-300

17. 21 Aug — CTBC 2-1 Uni; Dykxhoorn 7 IP, 1 ER
    https://stats.cpbl.com.tw/schedule/2026-A-278

18. 31 Jul — Rakuten 1-0 Uni; Dykxhoorn 7 IP, 1 ER
    https://stats.cpbl.com.tw/schedule/2026-A-234

19. Official CPBL 7 Apr rain-interrupted Stout/Dykxhoorn matchup report
    https://cpbl.com.tw/xmdoc/cont?SId=0Q097826754573241228

## C. Current matchup / weather sources

20. NOWnews same-day CPBL preview — Stout vs Dykxhoorn and current standings
    https://www.nownews.com/news/6872173
    - current media corroboration; not promoted over the official event page for starter confirmation.

21. PTT TSG-Hawks probable-starter post
    https://www.ptt.cc/bbs/TSG-Hawks/M.1788430073.A.073.html
    - secondary probable-starter corroboration only.

22. Taiwan Central Weather Administration, Southern Region Weather Center
    https://south.cwa.gov.tw/eng
    - southern Taiwan: occasional showers/thunderstorms, locally heavy rain possible.

23. Contemporaneous Tainan hourly forecast retrieved in-session immediately before first pitch.

---

## 13. Local running-log status

Unsettled queue:
1. `LOCAL-GEELONG-20260904` — Geelong vs Carlton
2. `P-280` — Rabbitohs vs Roosters
3. `P-281` — Rakuten Monkeys @ Fubon Guardians
4. `P-282` — **TSG Hawks @ Uni-Lions**

No retrospective has been performed on P-282.

Next local continuation ID: **P-283**, subject to fresh Drive reconciliation.

---

# P-283 — Namibia vs South Africa — 2026 Namibia T20I Tri-Series

## Frozen state

- **Local continuation ID:** `P-283`
- **Sport/format:** Men's T20I
- **Venue:** FNB Namibia Cricket Ground, Windhoek
- **Scheduled start:** 2026-09-04 14:00 CAT / 22:00 AEST
- **Cutoff:** **2026-09-04 13:50:06 CAT / 21:50:06 AEST**
- **State at cutoff:** `PREGAME / UPCOMING`; current match centre still showed teams TBA and no toss.
- **Method:** `MDS-2026.09.04-v3.4 + GFA-2 + SFA-CRICKET`
- **Numerical state:** `NTS-2026.09.02-v0.3 — no fitted cricket model`
- **Probability/value/staking:** NOT GENERATED / NOT AUTHORISED
- **Retrospective:** NOT PERFORMED

### Supplied contracts

1. South Africa **Over 183.5** — team innings / end-of-20-over target
2. South Africa **Under 183.5**
3. South Africa **Over 53.5** — first six legal overs
4. South Africa **Under 53.5**

Operator DLS/shortening/early-chase settlement terms were not supplied and remain `UNKNOWN_DEFINITION`.

## CR-P1–CR-P5 gate

| Gate | Status |
|---|---|
| `CR-P1` format/rules | PASS — standard men's T20I, 20 overs, six-over powerplay |
| `CR-P2` target identity | PASS — six-over phase and full team innings are distinct targets |
| `CR-P3` toss/innings order | **UNRESOLVED -> LOW evidence cap** |
| `CR-P4` XI/phase roles | **UNRESOLVED -> LOW evidence cap** |
| `CR-P5` strip/conditions | Exact strip not found; match-window weather observed |

## Mandatory conditions ladder

| Rung | Attempt/result |
|---:|---|
| 1 | **ATTEMPTED** rights/official toss-time commentary and exact-match centre; no accessible toss-time pitch assessment before cutoff. |
| 2 | **ATTEMPTED** `"Namibia Cricket Ground" curator pitch` / groundsman searches; Cricket Namibia identifies head curator Tuhafeni Erastus and praises venue surfaces, but no exact 4 September strip statement. |
| 3 | **ATTEMPTED** current exact-match centre; game remained Upcoming, teams TBA, no toss/pitch report. |
| 4 | **ATTEMPTED** exact-match specialist preview/pitch-and-conditions searches; no current exact-match strip report located before cutoff. |
| 5 | **ATTEMPTED** named ICC reporting; Prenelan Subrayen described a preceding match at this venue as offering something for pace, spin and batting and said the wicket played well. Historical venue tendency only. |
| 6 | **COMPUTED** current tri-series first innings at this venue: **163, 144, 195, 185, 156**; `n=5`, mean **168.6**, only **2/5** above 183.5. |

**STRIP STATUS:** `NOT FOUND AFTER SEARCH`  
**MATCH CONDITIONS STATUS:** `OBSERVED` — dry/hazy afternoon, no material rain signal.  
No exact in-ground wind vector was observed.

## Current personnel

South Africa's young touring squad is captained by Bjorn Fortuin. Current batting resources include Lhuan-dré Pretorius, Dewald Brevis, Jordan Hermann, Rubin Hermann and Connor Esterhuizen. Lutho Sipamla was ruled out with a hamstring injury and replaced by Andile Simelane; Jason Smith had already been ruled out.

Namibia's experienced core includes Gerhard Erasmus, Jan Frylinck, JJ Smit, Ruben Trumpelmann, Jan-Nicol Loftie-Eaton and Bernard Scholtz.

Exact XIs and batting order were not confirmed at cutoff, so these are role branches rather than asserted starters.

## Current-series scoring evidence

### Same-venue first innings
- Namibia 163/9 vs South Africa
- Zimbabwe 144/8 vs South Africa
- Zimbabwe 195/6 vs Namibia
- South Africa 185/7 vs Zimbabwe
- Namibia 156/6 vs Zimbabwe

Mean: **168.6**.  
The 183.5 line is above the current-series centre.

### South Africa powerplays
- vs Namibia: **34/2**
- vs Zimbabwe: **61/2**
- vs Zimbabwe: **59/0**

Mean: **51.3**. Over 53.5 occurred in 2/3, but the line sits close to the centre.

### Namibia's last two powerplays conceded
- Zimbabwe: **64/1**
- Zimbabwe: **59/1**

This is the strongest current evidence for South Africa Over 53.5.

## Direct matchup

On 28 August:
- Namibia 163/9
- South Africa 145/9
- South Africa powerplay **34/2**
- Namibia won by 18 runs.

ICC noted Namibia has won both T20Is played between these countries. This keeps both the South Africa winner call and the powerplay Over below high confidence.

## Phase-resource / toss mixture

### South Africa bats first
The main Over-183.5 branch. South Africa posted **185/7** on 1 September, with Pretorius scoring 94. A retained-wickets state can reach 190+.

### South Africa bats second
Target-censoring supports Under 183.5 in many states. Namibia's two completed bat-first totals in this series were **163** and **156**. A sub-184 target can end South Africa's innings before 20 overs and below 183.5 under ordinary team-innings interpretation.

### Six-over phase
Recent SA acceleration plus Namibia's recent leakage supports Over 53.5, but the direct matchup's 34/2 is a clear wicket-cluster kill path.

A fast powerplay does not determine the innings:
- **58/1 after six -> 178/7 after 20** is coherent.
A slow powerplay can still recover:
- **44/2 after six -> 180+** remains possible if resources survive.

## Ranked forecast

| Rank | Contract | Verdict | Main reason |
|---:|---|---|---|
| **1** | **South Africa Under 183.5 — 20 overs** | **BEST RELATIVE LEAN / LOW cap** | 183.5 is above the current venue-series centre; only 2/5 first innings cleared it; SA's only bat-first innings was 185/7; unresolved toss creates a strong chase-censoring Under branch. |
| **2** | **South Africa Over 53.5 — first 6 overs** | **LEAN / LOW cap** | SA's last two powerplays were 61/2 and 59/0; Namibia conceded 64/1 and 59/1 in its last two powerplays. |
| **3** | **South Africa Under 53.5 — first 6 overs** | **FORCED RANK / close opposite** | SA's three-match PP mean is 51.3 and Namibia held this same side to 34/2 in the opener. |
| **4** | **South Africa Over 183.5 — 20 overs** | **LEAST LIKELY, but live bat-first ceiling** | 185/7 and the venue's 195 show 184+ is plausible, but the threshold is high relative to the current series centre and innings-order uncertainty hurts it. |

## Potential winner

### **South Africa — narrow-to-moderate qualitative lean**

Reasons:
- consecutive wins over Zimbabwe after the opening loss;
- Brevis 75* off 32 in the first Zimbabwe match;
- Pretorius 94 in the 185/7 win;
- Fortuin, Subrayen and Duan Jansen provide multiple wicket-taking paths.

Counterweight:
- Namibia beat South Africa by 18 runs in the opener;
- Namibia has won both historical T20Is against South Africa;
- home familiarity and experienced Namibia core;
- toss, XI and exact strip unresolved.

## Source register

### Google Drive — read only
- `PREDICTION_LOG_COMBINED_2.md` — active authority; current method v3.4, publication/value gates.
- `RULES_CRICKET.md` — SFA-CRICKET, CR-P1–P5, phase/innings separation, LOW-evidence caps.
- `LEAGUE_RULES_CRICKET.md` — current T20I rules reference.
- `DATA_SOURCE_REGISTER.md` — mandatory six-rung conditions ladder and cricket source ownership.

### Governing / official cricket
- ICC: **All the details about Namibia, South Africa and Zimbabwe tri-series**
  https://www.icc-cricket.com/news/all-the-details-about-namibia-south-africa-and-zimbabwe-tri-series
- Cricket Namibia: **FNB T20 Tri-Series announcement**
  https://cricketnamibia.com/cricket-namibia-to-host-the-proteas-and-zimbabwe-in-fnb-t20-tri-series/
- ICC: **Namibia beat South Africa to kickstart home tri-series**
  https://www.icc-cricket.com/news/namibia-inch-past-south-africa-to-kickstart-home-tri-series
- ICC: **Brevis blitz sees off Zimbabwe as South Africa bounce back**
  https://www.icc-cricket.com/news/brevis-blitz-sees-off-zimbabwe-as-south-africa-bounce-back
- ICC: **Splendid win boosts South Africa's tri-series final chances**
  https://www.icc-cricket.com/news/splendid-win-boosts-south-africa-s-tri-series-final-chances
- ICC: **Zimbabwe survive Namibia fightback in Windhoek thriller**
  https://www.icc-cricket.com/news/zimbabwe-survive-namibia-fightback-in-windhoek-thriller
- ICC: **Zimbabwe beat Namibia to keep tri-series final hopes alive**
  https://www.icc-cricket.com/news/zimbabwe-beat-namibia-to-keep-tri-series-final-hopes-alive
- ICC: **Injury setback for South Africa in Namibia**
  https://www.icc-cricket.com/news/south-africa-suffer-another-injury-setback-in-namibia
- ICC: **Namibia name strong squad for home tri-series**
  https://www.icc-cricket.com/news/namibia-name-strong-squad-for-home-tri-series
- ICC: **Subrayen on Windhoek conditions**
  https://www.icc-cricket.com/news/a-privilege-to-watch-subrayen-on-sensational-brevis
- Cricket Namibia: **2026 Annual Awards / head curator context**
  https://cricketnamibia.com/celebrating-excellence-at-2026-cricket-namibia-annual-awards/

### Phase/scorecard research
- NDTV: Namibia v South Africa, 28 Aug — SA PP 34/2, final 145/9.
- NDTV: South Africa v Zimbabwe, 29 Aug — SA PP 61/2, chase 146/3 in 13.4.
- NDTV: Zimbabwe v South Africa, 1 Sep — SA PP 59/0, final 185/7.
- NDTV: Namibia v Zimbabwe, 3 Sep — Zimbabwe PP 59/1, Namibia 156/6, Zimbabwe 159/5.
- Current Cricket Australia exact-match centre — at cutoff: Upcoming, teams TBA. Used as a moving corroboration source, not the event field owner.

### Weather
- Contemporaneous Windhoek forecast at ~13:48 CAT: hazy/dry, no meaningful precipitation signal through the match window.

## Local queue after P-283

1. `LOCAL-GEELONG-20260904` — Geelong Cats vs Carlton
2. `P-280` — Rabbitohs vs Roosters
3. `P-281` — Rakuten Monkeys @ Fubon Guardians
4. `P-282` — TSG Hawks @ Uni-Lions
5. `P-283` — Namibia vs South Africa

No retrospective has been performed. Next local continuation ID: **P-284**, subject to fresh Drive reconciliation.

---

## P-283 FINAL PRE-GAME TOSS / INNINGS-ORDER REFRESH

**Refresh cutoff:** **2026-09-04 13:58:21 CAT / 21:58:21 AEST**, before the scheduled 14:00 CAT first ball.

**New volatile fact:** South Africa are **batting first**.

The currently indexed exact-match Cricket Australia page still rendered the fixture as `Upcoming` with teams TBA at this refresh, so no live score, delivery, wicket or post-start information is used. The batting-first fact is incorporated as the final pregame innings-order update.

### Material model change

The original pre-toss P-283 rank #1, **South Africa Under 183.5**, was partly supported by an unresolved-toss branch in which Namibia batted first and South Africa chased a sub-184 target. That branch is now impossible.

With South Africa batting first:
- South Africa is guaranteed ordinary first-innings scoring exposure up to 20 overs unless all out/shortened;
- the **target-censoring Under branch is removed**;
- the 1 September **185/7** innings becomes more directly comparable;
- the venue's **195/6** first-innings ceiling remains relevant;
- South Africa's recent powerplay scores **61/2 and 59/0**, plus Namibia conceding **64/1 and 59/1** in its last two powerplays, become relatively more important.

Toss direction itself is not treated as proof of a batting-friendly strip. The exact strip report remains `NOT FOUND AFTER SEARCH`.

### Revised ranked slate — supersedes the earlier pre-toss order

| Rank | Contract | Revised verdict | Reason |
|---:|---|---|---|
| **1** | **South Africa Over 53.5 — first 6 overs** | **BEST RELATIVE LEAN / LOW evidence cap** | SA cleared 53.5 in its last two powerplays (61/2, 59/0), while Namibia conceded 64/1 and 59/1 in its last two. With SA batting first, there is no chase-tempo suppression in the powerplay. The direct 34/2 is the principal kill path. |
| **2** | **South Africa Under 183.5 — 20 overs** | **LEAN / materially downgraded** | The threshold remains above the five-match venue first-innings mean of 168.6, and Namibia has already suppressed this SA batting group. But the chase-censoring branch is gone and SA's only previous bat-first innings in this series was 185/7, so the Under is now much less robust. |
| **3** | **South Africa Over 183.5 — 20 overs** | **LIVE / upgraded** | Batting first guarantees full first-innings intent/exposure, subject to wickets/shortening. SA already made 185/7 here and Zimbabwe made 195/6. A 55–65 powerplay with wickets retained creates a coherent 184+ path. |
| **4** | **South Africa Under 53.5 — first 6 overs** | **CLOSE OPPOSITE / forced rank** | Still credible because Namibia held SA to 34/2 in the first meeting. It falls to fourth because all four most recent relevant powerplay observations — SA 61/2, SA 59/0, Namibia conceded 64/1, Namibia conceded 59/1 — sit above 53.5. |

### Revised central score tree

- **Powerplay central family:** roughly **52–61**, with the line at 53.5 close to the lower edge of that family.
- **20-over central family:** roughly **174–188**.
- **High ceiling:** **190–205+** if Pretorius/Brevis retain wickets into overs 12–16.
- **Under kill path for the powerplay Over:** Namibia reproduces its first-meeting new-ball wicket cluster, leaving SA around **38–50/2 or 3** after six.
- **Over kill path for the innings Under:** SA reaches **58–65/0 or 1** after six and keeps two set batters through the middle, creating a **188–200+** finish.

### Winner

**South Africa remains the potential match winner — narrow-to-moderate lean.**

Batting first does not mechanically increase the winner call. Namibia has already beaten this South African side in the series and has won both historical T20Is between the teams. The winner view therefore remains separate from the two South Africa scoring contracts.

### Audit note

- This is a **pre-delivery volatile refresh under the same P-283 event ID**, not a new prediction card.
- The original pre-toss ranking is preserved earlier in the log for audit continuity.
- This revised ranking **supersedes the earlier P-283 order for the final pregame forecast**.
- No retrospective has been performed.
- No live/post-start cricket information has been used.

---

# P-284 — USA (W) vs China (W) — 2026 FIBA Women's Basketball World Cup

## 1. Frozen identity, state and contracts

- **Local continuation ID:** `P-284`
- **Canonical reconciliation:** Drive remains read-only and its current imported snapshot still trails this local continuation. Issued local IDs are not reused.
- **Competition:** FIBA Women's Basketball World Cup 2026
- **Stage:** Group D, Game #1
- **Event:** United States vs China
- **Venue:** Max-Schmeling-Halle, Berlin, Germany
- **Scheduled tip:** Friday 4 September 2026, approximately **12:15 UTC / 14:15 Berlin / 22:15 Australia/Melbourne**
- **Information/state cutoff:** **2026-09-04 22:08:07 Australia/Melbourne**
- **Official FIBA event state at freeze:** pregame; no score/live game state was displayed.
- **Method:** `MDS-2026.09.04-v3.4`
- **Algorithms:** `GFA-2 + SFA-BASKETBALL`
- **Numerical state:** `NTS-2026.09.02-v0.3 — no fitted/validated basketball model`
- **Probability / edge / staking:** `NOT GENERATED / NOT AUTHORISED`
- **Retrospective:** **NOT PERFORMED — user explicitly requested none**

### Exact supplied slate

| Contract | Ordinary geometry |
|---|---|
| **USA -29.5** | USA must win by 30+ |
| **China +29.5** | China wins or loses by 29 or fewer |
| **Over 161.5** | 162+ settled points |
| **Under 161.5** | 161 or fewer settled points |

**Operator endpoint:** `UNKNOWN_DEFINITION`; user did not supply regulation-vs-overtime settlement terms. The ordinary FIBA game includes four 10-minute quarters and five-minute overtime periods as needed, but sportsbook inclusion of overtime is not assumed without operator terms.

---

## 2. Basketball gate audit

| Gate | Status | Frozen finding |
|---|---|---|
| `BK-P1` league/clock | **PASS** | FIBA senior women's World Cup; four 10-minute quarters, FIBA foul/bonus/OT environment. |
| `BK-P2` availability / starters | **PARTIAL** | Final tournament rosters were confirmed. Major withdrawals were verified. Exact starting fives were not exposed on the official event page at freeze, so minutes/start mixtures remain. |
| `BK-P3` phase | **PASS** | All supplied rows are full-game. |
| `BK-P4` operator endpoint | **UNKNOWN_DEFINITION** | Regulation/OT settlement terms not supplied. OT retained as explicit tail. |

**Evidence consequence:** team rows remain qualitative. The missing confirmed starting five prevents false precision but does not erase strong roster-level and team-process evidence.

---

## 3. Current roster regime

### USA — final 12 at World Cup

Official WNBA World Cup roster release listed:
- Aliyah Boston
- Paige Bueckers
- Sonia Citron
- Caitlin Clark
- Napheesa Collier
- Kahleah Copper
- Chelsea Gray
- Rhyne Howard
- Kiki Iriafen
- Angel Reese
- Breanna Stewart
- Jackie Young

### Major USA availability changes

- **A'ja Wilson withdrew** before the tournament for health reasons.
- **Kelsey Plum withdrew** due to a lower-left-leg injury.
- **Sonia Citron and Kiki Iriafen** were added/reconfirmed into the final group.

This is a major roster-regime change from the initially announced USA World Cup roster. Wilson's interior scoring/defence and Plum's downhill/spacing creation are absent.

However, the current roster is still extraordinarily deep:
- Stewart and Collier supply elite two-way forward play;
- Gray, Clark and Bueckers provide multiple creation engines;
- Copper, Young and Howard maintain transition/rim/wing pressure;
- Boston, Reese and Iriafen maintain rebounding and paint depth.

Nine USA players are World Cup debutantes, so international continuity is lower than in older USA teams despite the enormous individual talent base.

### China — final World Cup regime

Current China roster reporting lists:
- Han Xu
- Zhang Ziyu
- Chen Mingling
- Chen Yujie
- Jia Saiqi
- Li Yuan
- Luo Xinyu
- Sun Yu
- Tang Ziting
- Wang Siyu
- Yang Shuyu
- Zhang Manman

### Major China availability change

**Li Yueru is absent** after losing her passport during mailing and missing the registration/travel deadline.

This matters materially:
- China loses a proven interior scoring/rebounding body;
- the "Triple Towers" concept becomes mostly Han Xu + 2.20 m Zhang Ziyu rather than a Han/Li/Zhang three-big rotation;
- frontcourt ceiling remains substantial, but foul/minutes/spacing combinations are less flexible.

China's backcourt remains the weaker area relative to its frontcourt, with FIBA specifically flagging guard/wing creation as the primary roster concern.

---

## 4. Current competitive baselines

### USA — March 2026 World Cup Qualifying Tournament

USA went **5-0** in San Juan.

Official scores:
- USA 110-46 Senegal
- USA 91-48 Puerto Rico
- USA 93-59 Italy
- USA 101-46 New Zealand
- USA 84-70 Spain

Descriptive five-game averages:
- **USA points:** 95.8
- **Opposition points:** 53.8
- **Combined:** 149.6
- **Average margin:** +42.0

Important opponent-quality split:
- vs Spain: **+14**, total 154
- vs Italy: **+34**, total 152
- vs Puerto Rico/New Zealand/Senegal: very large 43–64 point margins

The weaker-opponent blowouts cannot be copied directly onto China, the FIBA world #4 team.

The current USA roster is also not identical to San Juan:
- Plum/Hamby were in the qualifying group;
- Stewart/Collier now replace that exposure;
- Wilson still was not part of the San Juan baseline, so her World Cup withdrawal does not invalidate those qualifying results as a current-style reference.

### China — March 2026 Wuhan Qualifying Tournament

China went **4-1**:
- China 81-68 Mali
- Belgium 80-65 China
- China 86-76 South Sudan
- China 84-74 Czechia
- China 83-71 Brazil

Descriptive averages:
- **China points:** 79.8
- **Opposition points:** 73.8
- **Combined:** 153.6
- **Average margin:** +6.0

This was with Li Yueru available, so the current frontcourt rotation is weaker than the March baseline.

### China — pre-World Cup preparation

Recorded FIBA preparation results:
- 74-76 Australia
- 82-84 Australia
- 70-67 Nigeria
- 69-65 Nigeria
- 77-88 Nigeria
- 76-88 Italy
- 57-81 Italy
- 71-72 Spain
- plus additional Mali/France preparation entries whose usable final score was not confirmed in the retrieved tracker

Across the eight scored games above:
- **China scored:** 72.0 per game
- **Allowed:** 77.6
- **Combined:** ~149.6
- **Average margin:** about -5.6

Against Australia/Italy/Spain specifically, China lost by:
- 2
- 2
- 12
- 24
- 1

No recorded preparation loss in that high-quality subset reached 30 points.

This is descriptive and preparation-game rotations differ from World Cup rotations, but it is direct evidence against treating +29.5 as automatically unsafe.

---

## 5. Direct USA-China history — downweighted

Official FIBA event history:
- 2022 World Cup Final: USA 83-61 China — margin 22, total 144
- 2022 World Cup Group Phase: USA 77-63 China — margin 14, total 140
- 2018 World Cup: USA 100-88 China — margin 12, total 188
- USA leads the official FIBA H2H **15-0**

The 2022 games both:
- would have cashed **China +29.5**
- would have cashed **Under 161.5**

But current roster continuity is incomplete:
- USA no longer has the same Wilson/Plum-led structure and now has a younger Clark/Bueckers generation;
- China is without Li Yueru and has added Zhang Ziyu.

Therefore old H2H is supporting context, not a governing coefficient.

---

## 6. Possession / efficiency mechanism

No fitted possession model exists, so pace is handled as a qualitative corridor.

### USA offensive process
Primary routes:
- live-ball turnovers -> transition;
- Clark/Gray/Bueckers creation and early offence;
- Stewart/Collier mismatch scoring;
- offensive rebounding from Boston/Reese/Iriafen;
- deep bench maintaining pressure after starter reduction.

USA's key route to **-29.5 + Over** is not simply shooting well. It is:
1. force China turnovers;
2. create transition and paint/free-throw opportunities before China's size is set;
3. maintain offensive quality with the second unit;
4. keep defensive intensity high enough that China's response scoring does not compress the margin.

### China offensive process
Primary routes:
- Han Xu high-post/pop skill and interior finishing;
- Zhang Ziyu rim pressure/size;
- Wang Siyu / Yang Shuyu / Li Yuan ball handling;
- offensive rebounding and half-court post mismatches.

China's main risk is guard pressure:
- if USA disrupts entry passes and creates live-ball turnovers, China's size becomes less valuable because it cannot consistently establish half-court position;
- if China gets clean half-court entries and controls the glass, its scoring floor rises and the 29.5 cushion becomes much stronger.

---

## 7. Team-score budget at 161.5

The active Drive basketball framework requires solving the favourite score needed to cross the total at plausible underdog scores.

| China score | USA needs for **Over 161.5** | Interpretation |
|---:|---:|---|
| **55** | **107** | Requires an extreme USA offensive game |
| **60** | **102** | High USA ceiling needed |
| **65** | **97** | Plausible but above ordinary strong-opponent central scoring |
| **70** | **92** | Very plausible if China sustains offence |
| **75** | **87** | Over becomes easy, but this requires a strong China offensive response |

The total therefore depends heavily on **China's scoring floor**.

A USA blowout is not automatically an Over:
- 96-60 = **156**, USA -29.5 + Under
- 92-61 = **153**, USA -29.5 + Under

And an underdog cover is not automatically an Under:
- 94-70 = **164**, China +29.5 + Over

This prevents spread and total from being treated as independent safety plays.

---

## 8. Mandatory mismatch branches

### `BK-B1` — central possessions / efficiency
Representative:
- USA **92-65** (157, margin 27)
- USA **94-66** (160, margin 28)
- USA **95-64** (159, margin 31)

This is the key central family around both supplied thresholds.

### `BK-B2` — shooting variance
USA three-point/transition efficiency runs hot:
- USA **101-66** (167, margin 35)

Or China shooting/spacing holds:
- USA **91-70** (161, margin 21)

### `BK-B3` — favourite sustain
USA keeps primary creators/defensive pressure active into the second half:
- **100-62**
- **102-64**

Effects:
- USA -29.5 strong
- total can land either side depending on China's floor

### `BK-B4` — favourite slowdown / bench sustain
USA opens a 25–35 point lead, reduces veteran minutes, but bench offence remains competent:
- **96-67**
- **98-65**

Margin compression and total can diverge.

### `BK-B5` — China response
China's size generates offensive rebounds, paint touches and free throws against reduced USA defensive intensity:
- **93-69**
- **95-71**

China +29.5 becomes strong; Over becomes live.

### `BK-B6` — China suppression
USA ball pressure disrupts China's guards and entry passes:
- **95-57**
- **99-59**

USA -29.5 + Under 161.5 can win together.

### `BK-B7` — foul / bonus tail
A high foul/free-throw game can push a 156–160 central state through 161.5 without changing the possession thesis much.

### `BK-B8` — overtime
OT is a low-probability tail in a matchup with this winner separation. Operator endpoint is unknown; no settlement assumption is made.

---

## 9. Spread decomposition

### USA -29.5 needs all of:
- opening separation;
- efficient conversion of turnover/rebound advantages;
- China scoring suppression;
- limited second-half garbage-time compression.

The first three are plausible. The fourth is the main uncertainty.

USA's March qualifiers show the ceiling:
- +64 Senegal
- +43 Puerto Rico
- +34 Italy
- +55 New Zealand

But against the best opponent in that field, Spain, USA won only by **14**.

China is FIBA #4 and, despite a poor warm-up record, stayed within 1–2 points of Australia twice and Spain once and within 12 of Italy in one meeting. This materially widens the China-cover branch.

### China +29.5 survives:
- any China upset;
- any USA win by 1–29;
- many ordinary late-margin-compression states.

The primary kill path is a USA defensive avalanche that turns China turnovers into repeated transition points and leaves China's half-court offence below 60.

---

## 10. Ranked forecast

| Rank | Contract | Verdict | Why |
|---:|---|---|---|
| **1** | **Under 161.5 points** | **BEST RELATIVE LEAN** | The total demands either a very high USA score when China is suppressed or a 68–75 point China response. USA's qualifier totals averaged 149.6; China's eight scored warm-ups also averaged about 149.6 combined. Current branches around 92-65, 94-66 and 95-64 all stay Under. Favourite blowout can coexist with Under. |
| **2** | **China +29.5** | **LEAN / close second** | 29.5 is an extreme margin against the world #4 side. China stayed within 24 or less in every scored high-level warm-up retrieved and within 1–2 of Australia/Spain multiple times. Han Xu/Zhang Ziyu provide a frontcourt floor. USA's depth can still break this through turnover/transition pressure. |
| **3** | **USA -29.5** | **LIVE BLOWOUT ALTERNATIVE** | USA's qualifier baseline shows genuine 30–60 point blowout capacity, and China's Li Yueru absence plus backcourt pressure vulnerability create a clear 30+ path. It ranks below China +29.5 because this line needs separation to persist through bench/garbage time against a top-four national team. |
| **4** | **Over 161.5 points** | **LEAST LIKELY, but live** | Over requires roughly USA 97+ if China scores 65, or China 70+ if USA stays near 92. USA's offensive depth can get there, but China's current scoring/guard profile and USA's defensive turnover pressure make the combined upper branch less central. |

### Central qualitative score corridor

Representative central families:
- **USA 92-64** — 156, USA +28 -> China +29.5 / Under
- **USA 94-66** — 160, USA +28 -> China +29.5 / Under
- **USA 96-64** — 160, USA +32 -> USA -29.5 / Under

This is why the Under is ranked above either spread side.

---

## 11. Potential game winner

### **USA — STRONG qualitative winner lean**

Winner confidence is materially stronger than spread confidence.

Reasons:
1. USA is FIBA world #1 and four-time defending World Cup champion.
2. Current 12-player roster retains elite creation, shooting, defence and rebounding even without Wilson/Plum.
3. USA went 5-0 at the March qualifier and has won 30 straight World Cup games entering Berlin.
4. China is in a generational transition and lacks Li Yueru.
5. China's primary roster concern is guard/wing creation, directly vulnerable to USA perimeter pressure.

China's size means the upset is not literally impossible, but it is a tail outcome rather than a central state.

---

## 12. Evidence / honesty boundary

- Competition/event/venue: **HIGH — official FIBA**
- Final tournament rosters: **HIGH — FIBA confirms all 16 rosters; current USA/China roster details corroborated by official USA/WNBA and Chinese Olympic Committee/Xinhua reporting**
- Major withdrawals: **HIGH**
- Confirmed starting fives: **NOT EXPOSED at freeze**
- USA March results/statistics: **HIGH — official FIBA**
- China March results/statistics: **HIGH — official FIBA**
- China preparation results: **HIGH — official FIBA tracker**
- Old H2H: **HIGH factual quality, LOW/MEDIUM predictive weight due roster regime change**
- Operator OT terms: **UNKNOWN_DEFINITION**
- Calibrated probability / value / ROI / staking: **NOT AUTHORISED**
- Retrospective: **NOT PERFORMED**

---

# SOURCE REGISTER — P-284

## A. Google Drive — READ ONLY

1. `PREDICTION_LOG_COMBINED_2.md`
   - active canonical authority / current method and publication gates.

2. `RULES_BASKETBALL.md`
   - SFA-BASKETBALL v3.4;
   - availability/minutes -> possessions -> shot mix -> efficiency -> foul/late-game -> joint score;
   - mismatch state tree;
   - extreme-spread, team-score-budget and garbage-time controls.

3. `LEARNING_REGISTER.md`
   - promoted controls carried forward.

**Drive modification:** NONE.

## B. Official FIBA / governing sources

1. **USA vs China — official FIBA game page**
   https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/games/128134-USA-CHN
   - Group D, Max-Schmeling-Halle, scheduled game, H2H.

2. **FIBA — Rosters confirmed ahead of tip-off**
   https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/news/rosters-confirmed-ahead-of-tip-off-at-fiba-womens-basketball-world-cup-2026
   - final tournament roster confirmation.

3. **WNBA official — 70 current/former WNBA players at 2026 World Cup**
   https://www.wnba.com/news/2026-fiba-womens-basketball-world-cup-wnba-rosters
   - exact current USA 12-player roster.

4. **USA Basketball — Citron and Iriafen added**
   https://www.usab.com/news/2026/08/sonia-citron-and-kiki-iriafen-added-to-2026-usa-basketball-womens-national-team-roster
   - current USA roster change.

5. **FIBA — Citron, Iriafen join USA's cast**
   https://www.fiba.basketball/en/news/sonia-citron-kiki-iriafen-join-usas-star-studded-cast-for-berlin
   - current roster experience/medal context.

6. **Reuters — USA prepare without Wilson/Plum**
   - A'ja Wilson and Kelsey Plum withdrawals; current USA core.
   - 3 Sep 2026.

7. **Chinese Olympic Committee / Xinhua — China World Cup roster**
   https://en.olympic.cn/news/Sports_News/2026/0903/706963.html
   - exact China roster and Li Yueru passport-related absence.

8. **FIBA — China team profile**
   https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/news/team-profile-can-china-repeat-their-sydney-success
   - China ranking, qualifier results, Han Xu/Zhang Ziyu frontcourt, guard-depth concern.

9. **FIBA — China Wuhan qualifier team profile**
   https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026-qualifying-tournament-wuhan-china/teams/china
   - March player leaders / roster regime.

10. **FIBA — Wuhan qualifier competition**
    https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026-qualifying-tournament-wuhan-china
    - China 4-1 qualification result set.

11. **FIBA — USA San Juan qualifier**
    https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026-qualifying-tournament-san-juan-puerto-rico
    - USA 5-0 scores.

12. **FIBA — USA qualifier team profile**
    https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026-qualifying-tournament-san-juan-puerto-rico/teams/usa
    - Clark, Copper, Reese and other March player production.

13. **FIBA — USA vs Italy qualifier**
    https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026-qualifying-tournament-san-juan-puerto-rico/games/128178-USA-ITA
    - 93-59; +34 against a World Cup-level opponent.

14. **FIBA — preparation-game tracker**
    https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/news/tracker-preparation-games-fiba-womens-basketball-world-cup-2026
    - China's Australia/Nigeria/Italy/Spain preparation results.

15. **FIBA — must-watch USA-China game preview**
    https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/news/the-must-watch-group-games-of-the-fiba-womens-basketball-world-cup-2026
    - USA #1 vs China #4; event context.

## C. Independent state/time corroboration

16. **Sofascore event listing**
    - USA-China scheduled 12:15 UTC at Max-Schmeling-Halle.
    - Used only to disambiguate displayed clock/timezone, not as official event owner.

---

## 13. Local running-log state after P-284

### Unsettled / incomplete queue

1. `LOCAL-GEELONG-20260904` — Geelong Cats vs Carlton
2. `P-280` — South Sydney Rabbitohs vs Sydney Roosters
3. `P-281` — Rakuten Monkeys @ Fubon Guardians
4. `P-282` — TSG Hawks @ Uni-Lions
5. `P-283` — Namibia vs South Africa
6. `P-284` — **USA (W) vs China (W)**

No retrospective has been performed for P-284.

Next local continuation ID: **P-285**, subject to fresh Drive reconciliation.

---

# P-285 — Korea (W) vs Nigeria (W) — 2026 FIBA Women's Basketball World Cup

## 1. Frozen identity / contract

- **Local continuation ID:** `P-285`
- **Competition:** FIBA Women's Basketball World Cup 2026
- **Stage:** Group B, Game #2
- **Event:** Korea vs Nigeria
- **Venue:** Berlin Arena, Berlin, Germany
- **Scheduled tip:** Friday 4 September 2026, 12:30 UTC / 14:30 Berlin / 22:30 Australia/Melbourne
- **Information/state cutoff:** **2026-09-04 22:28:20 Australia/Melbourne**
- **Official FIBA event state at cutoff:** pregame; no score/live state shown
- **Method:** `MDS-2026.09.04-v3.4`
- **Algorithms:** `GFA-2 + SFA-BASKETBALL`
- **Numerical state:** `NTS-2026.09.02-v0.3 — no fitted/validated basketball model`
- **Probability / edge / staking:** NOT GENERATED / NOT AUTHORISED
- **Retrospective:** NOT PERFORMED — explicitly deferred

### Exact supplied slate

1. **Nigeria -12.5**
2. **Korea +12.5**
3. **Over 143.5**
4. **Under 143.5**

**Operator regulation/overtime endpoint:** `UNKNOWN_DEFINITION`.

---

## 2. BK-P1–BK-P4 gate

| Gate | Status |
|---|---|
| `BK-P1` league/clock | PASS — FIBA senior women's rules, four 10-minute quarters |
| `BK-P2` availability/starters | PARTIAL — tournament rosters/current availability were researched; exact starting fives were not exposed on the official event page at freeze |
| `BK-P3` phase identity | PASS — all rows are full-game |
| `BK-P4` operator endpoint | UNKNOWN_DEFINITION — OT treatment not supplied |

### Decision-driving availability

**Korea have lost Jisu Park** for the World Cup. This is the most important roster change on the card.

Why it matters:
- 1.98 m center and primary rim/rebounding anchor;
- in Korea's March 77-60 win over Nigeria she had **11 points, 10 rebounds, 4 assists, 4 blocks and +21** in 28 minutes;
- across the March qualifier she averaged **8.4 points, 6.6 rebounds, 3.4 assists and 2.0 blocks**.

Korea's current offence therefore leans more heavily on **Leeseul Kang**, **Jihyun Park**, **Yeeun Heo** and perimeter shot-making, while its interior defence/rebounding becomes materially thinner.

Nigeria's current core remains veteran-heavy:
- **Ezinne Kalu** — lead guard / pressure / creation
- **Victoria Macaulay** — interior scoring/size
- **Murjanatu Musa** — rebounding/interior activity
- **Amy Okonkwo** — scoring forward
- support from Promise Amukamara, Elizabeth Balogun, Pallas Kunaiyi-Akpanah and other established internationals

FIBA's current team profile specifically flags Macaulay and Musa as a potent paint duo and Kalu as the heartbeat of the team.

---

## 3. Rankings / current tournament context

- Nigeria: **FIBA world #8**
- Korea: **FIBA world #15**
- FIBA's final pre-tournament Smart Power Rankings placed Nigeria **#10** and Korea **#13**.
- Nigeria's preparation form was poor enough for FIBA to describe the team as unpredictable.
- Korea's major downgrade is the loss of Jisu Park, described by FIBA as a "hammer-blow."

This is not used as a numerical coefficient; it frames the current roster/quality regime.

---

## 4. March 2026 qualifying baseline

Both teams played in the same Lyon-Villeurbanne World Cup qualifying tournament.

### Korea — 3-2

- Germany 76-49 Korea
- Korea 77-60 Nigeria
- Korea 82-52 Colombia
- Korea 105-74 Philippines
- Korea 62-89 France

Descriptive averages:
- Korea scored **75.0**
- allowed **70.2**
- combined **145.2**
- average margin **+4.8**

### Nigeria — 2-3

- Nigeria 70-37 Colombia
- Korea 77-60 Nigeria
- Nigeria 101-84 Philippines
- France 93-86 Nigeria
- Nigeria 73-81 Germany

Descriptive averages:
- Nigeria scored **78.0**
- allowed **74.4**
- combined **152.4**
- average margin **+3.6**

These raw averages are diagnostic only under the Drive rules.

---

## 5. Direct March rematch — highly relevant but roster-adjusted

**Korea 77-60 Nigeria**, 12 March 2026.

Quarter scores:
- Q1: 20-16 Korea
- Q2: 16-16
- Q3: 22-19 Korea
- Q4: 19-9 Korea

Game-level process:
- Korea shot **40% FG** vs Nigeria **36%**
- Korea shot **57.7% on 2PT** vs Nigeria **40%**
- Korea's 3PT rate was not exceptional: **28.2%** vs Nigeria **23.5%**
- Korea's biggest lead reached 19
- Jihyun Park was the principal scorer
- Jisu Park's interior/rebounding/defensive impact was material

### How to use it now

The 17-point Korea win is **not reusable as a straight H2H coefficient** because Jisu Park is absent.

But it still matters:
- Korea already showed it can handle Nigeria's pressure and physicality;
- Nigeria's offence was held to 60;
- Nigeria now gains a major interior matchup improvement without Jisu.

This creates a much closer present-day spread tree than "Nigeria #8 vs Korea #15" alone suggests.

---

## 6. Preparation form

### Korea — Japan friendlies
- lost **59-77**
- lost **77-78**

Descriptive:
- scored 68.0
- allowed 77.5
- combined 145.5
- average margin -9.5

The second game shows Korea can still produce a high-quality offensive response without using the March result as its only positive evidence.

### Nigeria — recent national-team preparation
Against China, Spain and Belgium:
- 67-70 China
- 65-69 China
- **88-77 win over China**
- 58-83 Spain
- 55-90 Belgium

Descriptive five-game averages:
- Nigeria scored **66.6**
- allowed **77.8**
- combined **144.4**
- average margin **-11.2**

Nigeria's full preparation tracker is 1-7 when games against WNBA clubs are also included. Those WNBA games are lower-compatibility and are not allowed to dominate the FIBA national-team forecast.

### Interpretation

Nigeria's recent offence has not consistently supported an 80+ central score against strong national teams. Korea's loss of Jisu raises Nigeria's paint/rebound ceiling, but it does not erase Nigeria's recent perimeter/half-court inconsistency.

---

## 7. Possession / shot-profile mechanism

### Nigeria
Likely strengths:
- physical ball pressure
- live-ball turnovers into transition
- offensive rebounding
- Kalu point-of-attack pressure and creation
- Macaulay/Musa/Okonkwo paint and second-chance scoring

Main upside mechanism:
`Korea turnover -> Nigeria transition -> offensive glass / paint foul pressure -> repeat high-value possessions`

### Korea
Likely strengths:
- Leeseul Kang high-volume three-point shooting
- Jihyun Park all-around creation/scoring
- Yeeun Heo playmaking
- ability to stretch a defence if given clean catch-and-shoot windows

Main resistance mechanism:
`secure ball -> avoid live-ball turnovers -> generate threes -> force Nigeria into half-court offence`

### Jisu Park absence
This shifts:
- defensive rebounding toward Nigeria
- paint deterrence toward Nigeria
- foul-trouble resilience toward Nigeria
- Korea's half-court facilitation slightly downward

But it can also push Korea toward a more perimeter-heavy/high-variance attack, widening both its shooting-upside and shooting-collapse branches.

---

## 8. Team-score budget at 143.5

| Korea score | Nigeria needs for **Over 143.5** |
|---:|---:|
| 55 | 89 |
| 60 | 84 |
| 62 | 82 |
| 65 | 79 |
| 68 | 76 |
| 70 | 74 |

This is why the total is sensitive to Korea's offensive floor.

If Nigeria suppresses Korea into the high-50s/low-60s, Nigeria itself must score roughly **82-89** for the Over.

Representative:
- Nigeria 76-61 = **137**
- Nigeria 78-63 = **141**
- Nigeria 80-62 = **142**
- Nigeria 81-65 = **146**

The line sits inside the upper part of the central corridor, so the Under is a lean rather than a high-confidence call.

---

## 9. Mandatory mismatch branches

### `BK-B1` central
- Nigeria **76-64** = 140, margin 12
- Nigeria **78-64** = 142, margin 14
- Nigeria **79-65** = 144, margin 14

Both supplied thresholds are near this family.

### `BK-B2` shooting variance
Korea shoots well from three:
- Nigeria **76-70** = 146, Korea +12.5

Korea shoots poorly:
- Nigeria **80-58** = 138, Nigeria -12.5

### `BK-B3` favourite sustain
Nigeria pressure remains high and interior edge persists:
- **82-60**
- **84-61**

Nigeria -12.5 + Under/Over can split depending on Nigeria's own scoring ceiling.

### `BK-B4` favourite slowdown
Nigeria opens a double-digit lead but older/veteran rotation slows or bench offence dips:
- **75-65**
- **77-66**

Korea +12.5 becomes live without requiring a Korea upset.

### `BK-B5` underdog response
Kang/Jihyun Park create enough perimeter scoring:
- **77-69**
- **79-70**

Korea +12.5 + Over becomes the main counter-state.

### `BK-B6` Korea suppression
Nigeria's physicality wins the possession battle:
- **78-58**
- **82-59**

Nigeria -12.5 + Under becomes highly coherent.

### `BK-B7` foul/bonus
Nigeria's interior advantage can create free throws and move a 138-142 central state over 143.5.

### `BK-B8` overtime
Low-probability but total-sensitive tail. Operator inclusion is unknown.

---

## 10. Spread decomposition

### Nigeria -12.5 requires
1. Nigeria to win the turnover/transition battle;
2. Nigeria to exploit Korea's weakened interior/rebounding;
3. Korea's threes not to run hot;
4. separation to survive the fourth quarter.

### Korea +12.5 survives
- any Korea win;
- any Nigeria win by 1-12;
- a meaningful portion of the central "Nigeria better, Korea still shoots enough" tree.

The strongest argument for the cushion is that:
- Korea beat Nigeria by 17 in March;
- Nigeria's August preparation was poor;
- FIBA itself moved Nigeria down to #10 in its current power ranking.

The strongest argument against it is Jisu Park's absence, which removes the exact player who was +21 with a 10-rebound/4-block performance in the March matchup.

---

## 11. Ranked forecast

| Rank | Contract | Verdict | Why |
|---:|---|---|---|
| **1** | **Under 143.5 points** | **BEST RELATIVE LEAN / LOW-MEDIUM evidence** | Nigeria's recent national-team prep offence averaged only 66.6, and a Korea scoring state around 58-64 forces Nigeria into the low/mid-80s to beat the total. The March direct game ended 137. Nigeria's interior edge can widen the margin while still suppressing the total. Main kill path: Korea's threes hold and Nigeria scores efficiently inside/free throws. |
| **2** | **Korea +12.5** | **LEAN / line inside central margin corridor** | 12.5 is significant given Korea's 17-point March win and Nigeria's poor prep. Korea can cover through threes even if Nigeria wins. Jisu Park's absence is the major reason this is not #1 and keeps the Nigeria separation branch strong. |
| **3** | **Nigeria -12.5** | **LIVE SEPARATION ALTERNATIVE** | Jisu Park's absence materially improves Nigeria's paint/rebound/foul-pressure matchup, and Korea's offence becomes more perimeter-dependent. Nigeria can cover in 78-58 / 80-62 / 82-60 states. It ranks below the cushion because Nigeria's recent form does not establish a stable 13+ central margin against this opponent. |
| **4** | **Over 143.5 points** | **LIVE BUT LEAST LIKELY** | Over is reachable around 79-65 or 76-70 and gains from Korean three-point variance plus Nigeria free throws/second chances. It ranks last because Nigeria's recent scoring and the direct March total both lean below the line, while a Nigeria blowout can occur via Korea suppression rather than a high total. |

---

## 12. Potential winner

### **Nigeria — moderate qualitative lean**

Reasons:
1. Nigeria is FIBA world #8 vs Korea #15.
2. Korea has lost its most important interior defender/rebounder, Jisu Park.
3. Nigeria's Macaulay/Musa/Okonkwo frontcourt is positioned to attack that absence.
4. Kalu gives Nigeria experienced point-of-attack pressure and international creation.
5. Nigeria has greater physical depth and Olympic-level experience.

Why not strong:
1. Korea beat Nigeria 77-60 only six months ago.
2. Nigeria's recent preparation form has been poor.
3. Korea retains high three-point variance through Leeseul Kang and creation through Jihyun Park.
4. The current final pre-tournament FIBA power rankings had the teams only three slots apart (#10 Nigeria, #13 Korea).

Representative central score shapes:
- **Nigeria 76-64**
- **Nigeria 78-64**
- **Nigeria 79-65**

---

## 13. Evidence boundary

- Event/venue/tip: HIGH — official FIBA
- World ranking: HIGH — official FIBA
- Jisu Park absence: HIGH — current official FIBA group preview/power ranking
- March direct game: HIGH — official FIBA box score
- March qualifier player stats: HIGH — official FIBA
- Current preparation results: HIGH — official FIBA preparation tracker
- Exact starting fives: NOT EXPOSED at freeze
- Nigeria exact final starting rotation/minutes: uncertain
- Operator OT terms: UNKNOWN_DEFINITION
- Probabilities/value/ROI/stakes: NOT AUTHORISED
- Retrospective: NOT PERFORMED

---

# SOURCE REGISTER — P-285

## A. Google Drive — READ ONLY

1. `PREDICTION_LOG_COMBINED_2.md`
   - active authority / current method / value gates.
2. `RULES_BASKETBALL.md`
   - SFA-BASKETBALL v3.4;
   - mismatch branches, current-roster reconciliation, team-score budget, extreme-spread and garbage-time controls.

**Drive modification:** NONE.

## B. Official FIBA sources

1. Korea vs Nigeria — official World Cup game page  
   https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/games/128123-KOR-NGR

2. World Cup 2026 main schedule  
   https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026

3. Korea current team profile  
   https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/teams/korea

4. Nigeria current team profile  
   https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/teams/nigeria

5. Group B preview — Jisu Park absence / rematch context  
   https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/news/preview-will-anyone-slow-down-favorties-france-in-group-b

6. Final pre-tournament Smart Power Rankings, Volume 4  
   https://www.fiba.basketball/en/news/womens-world-cup-smart-power-rankings-volume-4

7. Korea World Cup team profile  
   https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/news/team-profile-will-korea-be-the-surprise-package

8. Nigeria World Cup team profile  
   https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/news/team-profile-are-nigeria-knocking-on-the-door-of-history-again

9. March 2026 Korea 77-60 Nigeria official game page  
   https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026-qualifying-tournament-villeurbanne-france/games/128160-KOR-NGR

10. Jisu Park March qualifier player page  
    https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026-qualifying-tournament-villeurbanne-france/teams/korea/197069-jisu-park

11. Korea March qualifier team profile  
    https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026-qualifying-tournament-villeurbanne-france/teams/korea

12. Nigeria March qualifier team profile  
    https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026-qualifying-tournament-villeurbanne-france/teams/nigeria

13. Lyon-Villeurbanne qualifier results/standings  
    https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026-qualifying-tournament-villeurbanne-france

14. FIBA World Cup preparation-game tracker  
    https://www.fiba.basketball/en/events/fiba-womens-basketball-world-cup-2026/news/tracker-preparation-games-fiba-womens-basketball-world-cup-2026

15. Rosters confirmed ahead of World Cup tip-off  
    https://www.fiba.basketball/en/news/rosters-confirmed-ahead-of-tip-off-at-fiba-womens-basketball-world-cup-2026

---

## 14. Local queue

1. `LOCAL-GEELONG-20260904` — Geelong Cats vs Carlton
2. `P-280` — Rabbitohs vs Roosters
3. `P-281` — Rakuten Monkeys @ Fubon Guardians
4. `P-282` — TSG Hawks @ Uni-Lions
5. `P-283` — Namibia vs South Africa
6. `P-284` — USA (W) vs China (W)
7. `P-285` — **Korea (W) vs Nigeria (W)**

P-285 remains **PREGAME / UNSETTLED**. No retrospective has been performed.

Next local continuation ID: **P-286**, subject to fresh Drive reconciliation.

---

# P-286 — Glasgow Cosmic vs Belfast Wolves — 2026 European T20 Premier League

## 1. Frozen identity, state and exact contracts

- **Local continuation ID:** `P-286`
- **Competition:** European T20 Premier League (ETPL), inaugural 2026 season
- **Event:** Glasgow Cosmic vs Belfast Wolves
- **Venue:** Sportpark Duivesteijn / Voorburg Cricket Club, Voorburg, Netherlands
- **Original scheduled start:** Friday 4 September 2026, 15:15 CEST
- **Frozen research cutoff:** approximately **2026-09-04 16:51 CEST / 2026-09-05 00:51 AEST**
- **Weather delay state:** toss/start delayed by wet outfield in the live specialist match centre; later match state supplied by user/market is a **12-over rain-reduced innings** with **Belfast Wolves batting first**
- **Official ETPL dynamic-page limitation:** at the frozen research point the official competition page was still stale, showing the fixture as upcoming / both sides yet to bat and no score.
- **Method:** `MDS-2026.09.04-v3.4`
- **Algorithms:** `GFA-2 + SFA-CRICKET`
- **Numerical state:** `NTS-2026.09.02-v0.3 — no fitted/validated cricket model`
- **Probability / edge / staking:** NOT GENERATED / NOT AUTHORISED
- **Retrospective:** **NOT PERFORMED — user explicitly requested none**

### Exact user-supplied market state

1. **Belfast Wolves Over 120.5 runs — first innings, end of 12 overs**
2. **Belfast Wolves Under 120.5 runs — first innings, end of 12 overs**
3. **Belfast Wolves Over 57.5 runs — end of first 6 overs**
4. **Belfast Wolves Under 57.5 runs — end of first 6 overs**

### Endpoint clarification

The user market calls the six-over checkpoint the "powerplay". In a rain-reduced T20 the official fielding-restriction powerplay can be recalculated. A field-owner source confirming the exact reduced-match fielding-restriction length was not recovered before the freeze. This card therefore models the exact **six-over cumulative-run endpoint** without falsely asserting that all six overs remain the regulatory powerplay.

**Operator DLS/abandonment/shortening settlement wording:** `UNKNOWN_DEFINITION`.

---

## 2. CR-P1–CR-P5 precondition audit

| Gate | Status | Frozen finding |
|---|---|---|
| `CR-P1` format/rules | **PARTIAL** | ETPL base format is T20, 20 overs, with overs 1–6 as the normal full-match powerplay. Current user/market state says 12 overs after rain. Exact reduced fielding-restriction table not field-owner verified. |
| `CR-P2` target identity | **PASS** | Two distinct Belfast targets: runs after six legal overs and runs at the 12-over first-innings endpoint. |
| `CR-P3` toss/innings order | **PASS for forecast state, with source caveat** | User's current market state identifies Wolves as the first-innings batting side; a secondary current toss feed also reported Belfast chose to bat, while the official ETPL page had not updated. |
| `CR-P4` XI/phase roles | **PARTIAL -> LOW cap** | Squads verified; current probable XIs available, but no official final XI exposed on the stale official page at freeze. |
| `CR-P5` strip/conditions | **PARTIAL** | Wet outfield and showers observed. No exact toss-time strip report found; same-venue/current-series surface descriptions conflict. |

---

## 3. Mandatory six-rung strip / conditions search

| Rung | Attempt | Result |
|---:|---|---|
| 1 | **ATTEMPTED:** official ETPL page and live specialist toss commentary | Wet-outfield delay reported; no exact-match strip assessment from captain/curator/broadcaster recovered before freeze. |
| 2 | **ATTEMPTED:** `Voorburg curator pitch`, `Sportpark Duivesteijn groundsman`, VCC ground material | Historical pitch-preparation/hybrid-surface material found, but no exact 4 Sep 2026 strip statement. |
| 3 | **ATTEMPTED:** Cricbuzz exact-match page | Toss delayed due to wet outfield and inspection reported; no current strip description. |
| 4 | **ATTEMPTED:** current exact-match specialist preview | One preview expected a batting-friendly, true-bounce surface with possible early seam; preview opinion only. |
| 5 | **ATTEMPTED:** same-week Voorburg reports/previews | Conflicting descriptions: one same-week report described slow/low variable bounce; a recent scorecard labelled the strip Fast & Bounce / batting average. |
| 6 | **COMPUTED:** venue/format baseline | Current venue T20 sample reported roughly **154 first-innings runs** and **45.4 powerplay runs** with rain-affected matches excluded; seam economy about 7.96 and spin about 7.33. |

- **STRIP STATUS:** `NOT FOUND AFTER SEARCH`
- **Current venue-tendency evidence:** `CONFLICTING`
- **MATCH CONDITIONS STATUS:** `OBSERVED`
- **Observed current condition:** wet outfield significant enough to delay toss/start; light rain/showers with continued shower risk.
- Rain is not treated as an automatic Under: wetness can slow the outfield and assist seam, while a wet ball can reduce bowling control and the 12-over reduction increases batting intent.

---

## 4. Rain-reduced scoring geometry

### 12-over line: 120.5
To score 121:
- **121 / 12 = 10.08 runs per over**

### 6-over line: 57.5
To score 58:
- **58 / 6 = 9.67 runs per over**

The six-over checkpoint consumes **half of the shortened innings**, so Belfast can attack earlier than in a normal T20, but a wicket cluster leaves almost no rebuilding time.

---

## 5. Belfast current scoring evidence

### vs Dublin Chiefs — Belfast first innings
- **184/7**
- first six overs: **52/3**
- Mark Chapman 54, Glenn Maxwell 60

### vs Rotterdam Dockers — Belfast first innings
- **156/9**
- first six overs: **46/1**

### vs Edinburgh Castle Rockers — Belfast chasing
- **130 all out in 17.1**
- score after six: **51/4**

### vs Amsterdam Flames — rain-reduced five-over chase
- Amsterdam 56/2 in five
- Belfast **59/1 in 3.5 overs**
- Stirling 25*, Chapman 19, Maxwell 11*

This last match is strong evidence of shortened-game ceiling, but it is target-censored chase evidence and not a first-innings 12-over baseline.

### Completed six-over diagnostic
Normal-length six-over checkpoints:
- **52/3**
- **46/1**
- **51/4**

Mean: **49.7**

Today's **57.5** is about eight runs above Belfast's completed full-length six-over average. The shortened format warrants an aggression uplift, but the market line has already moved substantially toward that uplift.

---

## 6. Glasgow bowling-resource map

Current Glasgow bowling resources include:
- Lungi Ngidi
- Paul van Meekeren
- Keshav Maharaj
- Ali Khan / Brad Currie branches
- Liam Livingstone / Michael Leask support depending on XI

Ngidi and van Meekeren have been among Glasgow's leading wicket-takers in the ETPL.

Mechanism:
- new-ball seam/wet-surface uncertainty can punish Belfast's forced aggression;
- Maharaj becomes especially important in overs 7–9 because one spin wicket can derail the 11+ rpo second-six requirement;
- the short game also raises the risk that Maxwell/Miller/Chapman can overwhelm even good bowling in only two overs.

---

## 7. Belfast batting-resource map

Available explosive resources include:
- Paul Stirling
- Tim Tector
- Lorcan Tucker
- Mark Chapman
- David Miller
- Glenn Maxwell
- Chris Jordan
- Mark Adair

Exact XI/order was not officially handshaken in the stale competition page.

High branch:
- 58–65 after six with 0–1 wicket can support 121+.

Wicket-cluster branch:
- two or three early wickets can shrink the 12-over ceiling sharply, as shown by the recent 51/4 checkpoint.

---

## 8. Phase-to-innings transition at the exact lines

If Belfast is **52/2 after six**, it needs **69 from the last six** to reach 121:
- **11.50 rpo**

If Belfast is **58/1 after six**, it needs **63 from the last six**:
- **10.50 rpo**

If Belfast is **62/1 after six**, it needs **59 from the last six**:
- **9.83 rpo**

Therefore **Over 57.5 at six does not imply Over 120.5 at 12**. A 60/1 start can still finish 116–119 if Glasgow controls overs 7–9.

---

## 9. Scenario tree

### Central shortened state
- six overs: **50–56 / 1–2**
- 12 overs: **104–117**
- supports both Unders

### Early wicket cluster
- six: **42–50 / 2–4**
- 12: **92–108**
- strong Under/Under

### Clean acceleration
- six: **58–65 / 0–1**
- 12: **116–132**
- PP Over live; 12-over line depends on second-six control

### Fast first six / middle braking
- **60/1 -> 116/5**
- Over 57.5 + Under 120.5

### Modest first six / finish explosion
- **53/2 -> 124/5**
- Under 57.5 + Over 120.5

### Maximum batting ceiling
- **63/0 -> 132–145**
- primary kill path against both Under rankings

### Winner branch
Glasgow's Munsey/Roy/Livingstone/Berrington group has enough short-format power to chase a middling Belfast first innings; a 12-over match raises upset variance.

### Further-rain branch
Further reduction, DLS or abandonment remains material. Operator settlement terms are unknown.

---

## 10. Ranked exact-contract forecast

| Rank | Contract | Verdict | Main reason |
|---:|---|---|---|
| **1** | **Belfast Wolves Under 120.5 — 12 overs** | **BEST RELATIVE LEAN / LOW-MEDIUM cap** | 121 needs 10.08 rpo for all 12. Belfast's normal 20-over first-innings outputs and the venue's ~154 first-innings centre do not naturally map there without a major shortening uplift. Wet/new-ball uncertainty plus Glasgow's Ngidi/van Meekeren/Maharaj resources support a central 104–118 family. |
| **2** | **Belfast Wolves Under 57.5 — first 6 overs** | **LEAN / close** | Belfast's three completed six-over checkpoints are 52/3, 46/1 and 51/4, mean 49.7. The 12-over format increases intent, but 58 still requires a materially stronger first half than Belfast's normal ETPL powerplays. |
| **3** | **Belfast Wolves Over 57.5 — first 6 overs** | **LIVE SHORTENED-GAME ALTERNATIVE** | The first six are half the match exposure, and Belfast's 59/1 in 3.5 overs in a five-over chase demonstrates extreme short-game ceiling. If Stirling/Chapman/Maxwell survive the first 2–3 overs, 58–65 is realistic. |
| **4** | **Belfast Wolves Over 120.5 — 12 overs** | **LEAST LIKELY, but live high-variance branch** | Needs sustained 10+ rpo and usually a strong first six with wickets retained. Belfast has enough power, but there is little room for a two-over slowdown, wicket cluster or successful Maharaj spell. |

---

## 11. Potential winner

### **Belfast Wolves — narrow qualitative lean**

Why Belfast:
1. More shortened-match boundary depth through Stirling, Chapman, Miller and Maxwell.
2. Already showed a rain-reduced ceiling by chasing 57 with 59/1 in 3.5 overs.
3. Better current season results than Glasgow before this match.
4. Elite individual hitters gain value as match length shrinks.

Why only narrow:
1. Glasgow can concentrate Ngidi, van Meekeren and Maharaj in a 12-over contest.
2. Glasgow also owns short-format match-winners in Munsey, Roy and Livingstone.
3. Wet-outfield/weather uncertainty increases variance.
4. Final XIs and exact reduced fielding restrictions were not officially handshaken.

Representative Belfast first-innings centre: **104–118**.

---

## 12. Coherence audit

Central combination:
- **Under 57.5 at six**
- **Under 120.5 at 12**

Representative: **53/2 -> 114/6**

Independent second branch:
- **Over 57.5 at six**
- **Under 120.5 at 12**

Representative: **60/1 -> 117/5**

So Rank #1 does not require Rank #2 to be correct.

---

## 13. Evidence / honesty boundary

- Event identity/original schedule/venue: **HIGH — official ETPL**
- Wet-outfield delay: **MEDIUM-HIGH — live specialist exact-match commentary**
- 12-over reduction: **USER-SUPPLIED current market state; secondary/community corroboration; official ETPL page stale**
- Belfast batting first: **USER-SUPPLIED current first-innings market state; secondary toss corroboration; official page stale**
- Final XI: **NOT OFFICIALLY VERIFIED**
- Exact current strip: **NOT FOUND AFTER SEARCH**
- Current conditions: **OBSERVED — wet outfield + showers**
- Venue scoring baseline: **specialist statistical sample**
- Exact reduced regulatory powerplay length: **NOT FIELD-OWNER VERIFIED**
- Operator DLS/abandonment terms: **UNKNOWN_DEFINITION**
- Probability/value/ROI/stakes: **NOT AUTHORISED**
- Retrospective: **NOT PERFORMED**

---

# SOURCE REGISTER — P-286

## Google Drive — read only
1. `PREDICTION_LOG_COMBINED_2.md`
2. `RULES_CRICKET.md`
3. `LEAGUE_RULES_CRICKET.md`
4. `DATA_SOURCE_REGISTER.md`

## Official / venue
5. ETPL official homepage and results — https://www.etplofficial.com/
6. Official Glasgow Cosmic vs Belfast Wolves page — https://www.etplofficial.com/matches/6a688c61b30844b0969df8af
7. KNCB / Voorburg Cricket Club venue information
8. Historical VCC grounds-maintenance / hybrid-pitch material

## Current match / conditions
9. Cricbuzz Match 13 exact-match page — https://www.cricbuzz.com/live-cricket-scores/169330/ggc-vs-bfw-13th-match-etpl-2026
10. Current Voorburg weather forecast — light rain/showers, wet-outfield-consistent conditions
11. Secondary current toss report — Belfast won toss/elected to bat; corroboration only
12. Community live thread reporting 12-over reduction; corroboration only

## Belfast / venue evidence
13. Belfast vs Dublin — 184/7, six-over 52/3
14. Belfast vs Rotterdam — 156/9, six-over 46/1
15. Belfast vs Edinburgh — 130 all out, six-over 51/4
16. Belfast vs Amsterdam rain-reduced match — 59/1 in 3.5-over chase
17. Current Voorburg venue statistical baseline — ~154 first innings, ~45.4 powerplay
18. Current exact-match preview — batting-friendly/true-bounce expectation, possible early seam
19. Same-week Voorburg preview/report — slow/low variable-bounce description, used only to establish surface conflict

**Drive modification:** NONE.

---

## 14. Local running-log state

Unsettled:
1. `LOCAL-GEELONG-20260904`
2. `P-280` Rabbitohs vs Roosters
3. `P-281` Rakuten Monkeys @ Fubon
4. `P-282` TSG Hawks @ Uni-Lions
5. `P-283` Namibia vs South Africa
6. `P-284` USA (W) vs China (W)
7. `P-285` Korea (W) vs Nigeria (W)
8. `P-286` Glasgow Cosmic vs Belfast Wolves

P-286 remains **PREGAME / UNSETTLED**. No retrospective has been performed.

Next local continuation ID: **P-287**, subject to fresh Drive reconciliation.

---

# P-287 — Alexander Bublik vs Tommy Paul — 2026 US Open

## Frozen state
- Event: US Open men's singles, Round 3
- Court: Louis Armstrong Stadium, outdoor hard
- Format: best-of-five
- Cutoff: **2026-09-05 02:06:59 AEST / 2026-09-04 12:06:59 EDT**
- Official US Open SlamTracker state at cutoff: **UPCOMING**
- Method: `MDS-2026.09.04-v3.4 + GFA-2 + SFA-TENNIS`
- Retirement/walkover terms: `UNKNOWN_DEFINITION`
- No fitted/validated tennis model; no probability/value/staking claims
- No retrospective performed

## Exact supplied slate
1. Bublik +2.5 games
2. Paul -2.5 games
3. Over 40.5 total games
4. Under 40.5 total games

## Current tournament / workload
**Bublik**
- R1: beat J.J. Wolf 6-4, 6-2, 3-6, 6-1 — 34 games
- R2: beat Adrian Mannarino 6-3, 6-1, 6-1 — 23 games
- R2 specialist stats: 16 aces, 3 DFs, 73% first serves in, 91% first-serve points won, 53% second-serve points won
- Tournament exposure: **57 games**

**Paul**
- R1: beat Coleman Wong 6-7, 6-1, 6-3, 6-3 — 38 games
- R2: beat Dino Prizmic 6-2, 6-3, 5-7, 6-4 — 39 games, about 3h04
- R2 specialist stats: 9 aces, 4 DFs, 54% first serves in, 83% first-serve points won, 48% second-serve points won
- Tournament exposure: **77 games**

Bublik is substantially fresher through two rounds; Paul has the stronger North American hard-court lead-in.

## Current hard-court regime
Paul reached the Cincinnati quarterfinal and beat Alexander Zverev 4-6, 7-6(6), 6-4, showing strong late return pressure and second-serve attack. Bublik did not play Montreal/Cincinnati; the US Open was his first North American summer hard-court event, but he has served exceptionally well through two rounds.

## H2H continuity
Official US Open SlamTracker lists Paul leading the career H2H **3-1**.

Highest-continuity meeting:
- **2025 US Open R3:** Bublik d. Paul 7-6, 6-7, 6-4, 6-7, 6-1
- 55 total games, three tiebreaks
- Paul's 2025 medical timeout means the fifth-set 6-1 margin is not reused as a clean coefficient.

Other useful meetings:
- 2025 Miami hard: Paul won 5-7, 7-5, 6-4; Bublik lost by only two games
- 2024 Wimbledon: Paul won 6-3, 6-4, 6-2; lower surface continuity
- 2021 Rotterdam: Paul won in three; old indoor-hard meeting, heavily downweighted

## Serve/return matchup
- Bublik owns the bigger first-strike serve/ace ceiling and current R2 serving form.
- Paul owns the more stable return/second-serve pressure and has stronger recent high-level North American hard evidence.
- Bublik's second serve/double-fault volatility is Paul's main separation route.
- Paul's lower first-serve percentage in R2 creates a Bublik set-winning route if Bublik keeps return games short and protects his own serve.

## Environment
NWS around noon in Flushing: about 27°C/81°F, light NW wind around 6 mph, low near-term rain risk. Louis Armstrong has a retractable roof; exact roof state was not confirmed. No strong environment sign is applied.

## Best-of-five set-count mixture
Qualitative pre-total mixture:
- 3-set branch: meaningful but subordinate
- 4-set branch: largest branch
- 5-set branch: material
The combination of Bublik serve resistance, Paul's return quality, both players already dropping sets, and the 2025 same-site five-set meeting increases 4/5-set mass.

## Representative score tree
- Bublik 3-0: 7-6, 6-4, 7-6 = 33 → Bublik +2.5 / Under
- Bublik 3-1: 7-6, 4-6, 7-6, 6-4 = 43 → Bublik +2.5 / Over
- Bublik 3-2: 7-6, 4-6, 7-6, 4-6, 6-4 = 50 → Bublik +2.5 / Over
- Paul 3-0: 6-4, 7-6, 6-4 = 33 → Paul -2.5 / Under
- Paul 3-1: 7-6, 6-4, 4-6, 6-4 = 43 → Over; game handicap near boundary
- Paul 3-2: 6-7, 7-6, 6-4, 4-6, 6-4 = 49 → Over; Bublik +2.5 remains live depending cumulative margin

## Ranked forecast
| Rank | Contract | Verdict | Reason |
|---:|---|---|---|
| **1** | **Over 40.5 games** | **BEST RELATIVE LEAN** | Large four-set branch plus material five-set branch. Bublik's serve/tiebreak ceiling and Paul's return resilience make set trading plausible. Same-site 2025 meeting reached 55 games. Kill path: straight sets or compact 3-1 at 38-40 games. |
| **2** | **Bublik +2.5 games** | **LEAN** | Covers all Bublik wins plus some narrow Paul wins. Bublik is fresher by 20 tournament games, in elite current serving form, and this handicap would have survived both relevant 2025 outdoor-hard meetings. |
| **3** | **Paul -2.5 games** | **LIVE ALTERNATIVE** | Better North American hard preparation and stronger return/second-serve pressure. Can accumulate 6-4/7-5 margins if Bublik's second serve breaks down. |
| **4** | **Under 40.5 games** | **LEAST LIKELY, but real control branch** | Wins through either player's 3-0 and some compact 3-1 outcomes. It conflicts with the same close-set/tiebreak evidence supporting Bublik +2.5. |

## Potential winner
### **Tommy Paul — narrow qualitative lean**
Paul has the stronger recent hard-court preparation and return base. Bublik's same-site 2025 win, fresher workload and current serving level keep the winner call narrow.

Representative central Paul-win state: **Paul in four close sets**, with the match landing above 40.5.

## Evidence limitations
- Official event state/round/court: HIGH
- Current US Open scores: HIGH
- Paul Cincinnati form: HIGH, ATP
- Current match stats: MEDIUM-HIGH specialist cross-check
- H2H factual quality: HIGH; predictive weight MEDIUM
- Current medical issue: none found, but this is not a medical clearance
- Roof state: not confirmed
- Operator retirement terms: unknown
- Full same-provider L15/L20 hard-court windows: not recovered before start; not invented
- No calibrated probability/value/ROI/stake

# Sources — P-287
1. Google Drive `PREDICTION_LOG_COMBINED_2.md` — active authority/method gates
2. Google Drive `RULES_TENNIS.md` — SFA-TENNIS v3.4
3. US Open IBM SlamTracker — https://www.usopen.org/en_US/scores/stats/1315.html
4. US Open 2026 men's draw breakdown — https://www.usopen.org/en_US/news/articles/2026-08-27/mens_draw_breakdown_will_an_american_win_the_2026_us_open.html
5. US Open Bublik-Wolf R1 report — https://www.usopen.org/amp/en_US/news/articles/2026-08-30/bublik_beats_wolf_on_americans_return_from_injury_at_2026_us_open.html
6. US Open 2025 Bublik-Paul R3 report — https://www.usopen.org/en_US/news/articles/2025-08-30/alexander_bublik_vs_tommy_paul_2025_us_open_round_3.html
7. ATP Paul-Zverev Cincinnati report — https://www.atptour.com/en/news/zverev-paul-cincinnati-2026-wednesday
8. ATP Cincinnati results — https://www.atptour.com/en/scores/current/cincinnati/422/results
9. ATP US Open 2026 guide — https://www.atptour.com/en/news/us-open-2026-history-draw-schedule
10. Tennis.com Bublik-Paul current match page
11. TennisTonic Paul-Prizmic stats
12. SteveG Tennis Bublik-Mannarino stats/profile
13. TennisMyLife hard-court summaries for both players
14. Tennis Majors current player profiles
15. TennisStats247/TennisTonic H2H cross-checks
16. US National Weather Service Flushing digital forecast

## Queue
P-287 remains **PREGAME / UNSETTLED**. No retrospective performed.
Next local continuation ID: **P-288**, subject to fresh Drive reconciliation.

---

# P-288 — Athletics @ Seattle Mariners — 2026 MLB Regular Season

## Frozen state
- **Local continuation ID:** `P-288`
- **Event:** Athletics @ Seattle Mariners
- **Venue:** T-Mobile Park, Seattle
- **Scheduled first pitch:** 2026-09-04 19:10 PDT / 2026-09-05 12:10 AEST
- **Freeze:** **2026-09-05 11:56:41 AEST / 2026-09-04 18:56:41 PDT**
- **State:** PREGAME
- **Probable starters (MLB):** Kade Morris (ATH, RHP) vs Logan Gilbert (SEA, RHP)
- **Method:** `MDS-2026.09.04-v3.4 + GFA-2 + SFA-BASEBALL`
- No fitted baseball model; no probability/value/staking claims.
- No retrospective performed.

## Supplied contracts
1. Mariners -1.5
2. Athletics +1.5
3. Over 7.0
4. Under 7.0

Ordinary total geometry: Over wins 8+, Under wins <=6, exactly 7 pushes. Operator action/listed-pitcher/shortening terms are `UNKNOWN_DEFINITION`.

## Gate audit
- `BB-P1` starter identity: PASS — MLB probable-pitcher pages link Morris/Gilbert to exact event.
- `BB-P2` batting orders: PARTIAL — MLB static lineup page still showed TBD at freeze; secondary current threads carried full orders, so no player props are issued and lineup-specific confidence is capped.
- `BB-P3` league/rules/roof: PARTIAL — MLB nine innings/current extras; roof position not independently confirmed.
- `BB-P4` action/termination: UNKNOWN_DEFINITION.
- `BB-P5` home last bat: PASS — Seattle.

## Starter mismatch
### Kade Morris
Current MLB: 0-1, 9.82 ERA, 14.2 IP, 10 K, 2.11 WHIP in only five appearances and one prior MLB start. His appearance sequence includes a 4 IP/9 ER debut at Houston and recent relief-sized outings of 2.2 IP/2 ER vs Minnesota and 2 IP/1 ER vs Baltimore. This is treated as a wide small-sample starter mixture rather than a stable 9.82-ERA forecast.

Baseball Savant current pitch sample: sinker .500 AVG/.708 SLG allowed with 52.2% hard-hit; changeup .556/.889 with xSLG about .662. Older MLB bio minor-league splits show lefties hit .332 with a .928 OPS in 2025 versus .214/.614 for righties. This older split is shrunk but relevant against Seattle's left/switch-heavy batting group.

### Logan Gilbert
Current 2026: 11-8, 3.42 ERA, 160.1 IP, 166 K, 1.04 WHIP, about 26.0% K and 6.3% BB. Last five earned runs: 3,2,3,0,2. Savant shows strong splitter/slider/sweeper miss-bat shapes; splitter opponents around .139 AVG/.213 SLG with ~40% whiff.

MLB preview: career 2.81 ERA vs Athletics, quality starts in three of last four meetings; 27 May 2026 vs ATH: 6 scoreless innings, 5 hits.

## Current lineup/injury regime
Athletics are materially depleted: Brent Rooker, Nick Kurtz, Tyler Soderstrom, Jacob Wilson and Shea Langeliers are absent from the ordinary core/current starting group. Current secondary pregame lineup reporting lists Bolte, McNeil, Gelof, Butler, Cortes, Heim, Muncy, Walton and Williams.

Secondary Seattle reporting lists Arozarena, Canzone, Rodríguez, Raleigh, Naylor, Young, Crawford, Montes and Rodden, creating multiple left/switch matchups against Morris. MLB's static lineup page remained TBD at freeze, so these orders are not promoted to official posted lineups.

## Current team / series state
Entering tonight: Seattle 66-75, Athletics 55-86. Season run differentials at the official standings snapshot: Seattle -68; Athletics -191. Both were 4-6 over their last 10.

Athletics won the opener 7-4. The result itself is not used as a bounce-back/continuation signal. The actionable consequence is bullpen workload: Oakland starter Jack Perkins lasted only 3 innings, and Oakland used Blewett 2.0, Roycroft 1.2, Medina 1.1 and Harris 1.0. Seattle used Vargas, Speier, Bazardo and Milner for one inning each. Morris's recent 2-3 inning exposure creates another possible six-plus-inning Oakland relief night.

## Park
Baseball Savant 2026: T-Mobile Park overall factor 94, run factor 88, hit factor 92. Two-year 2025-26 overall 93, run factor 86. Strong run suppression supports the Under branch, but 2026 HR factor around 110 preserves home-run cluster risk. Roof state unconfirmed; no weather adjustment applied.

## Joint score tree
- Central Gilbert/Morris state: SEA 4-2, 5-1, 5-2.
- Morris early hook / Oakland relief exposure: SEA 6-2, 7-2, 6-3.
- Low-total separation: SEA 4-0, 4-1, 5-1.
- One-run Athletics resistance: SEA 3-2 / 4-3 or ATH win.
- Late separation: 3-2/4-3 can widen after the Oakland relief transition.
- Home ninth may be unplayed in Seattle-win states, capping total exposure.
- Tie-after-nine extras are a higher-rate automatic-runner environment and threaten Under/+1.5 settlement.

## Ranked forecast
| Rank | Contract | Verdict | Reason |
|---:|---|---|---|
| **1** | **Mariners -1.5** | **BEST RELATIVE LEAN** | Gilbert is established and well matched to a depleted Athletics lineup, while Morris is a small-sample/short-exposure starter facing a left/switch-heavy Seattle group. Oakland's likely starter-to-bullpen exposure gives Seattle multiple 4-1/5-1/6-2 separation paths. |
| **2** | **Over 7.0** | **LEAN — close to Under** | Morris's wide hook/contact tail plus Oakland's six bullpen innings last night links Seattle separation with an 8+ run state. Exactly seven pushes under ordinary terms. |
| **3** | **Under 7.0** | **LIVE CLOSE OPPOSITE** | Gilbert, Oakland's depleted batting core and T-Mobile's run suppression support 4-0/4-1/5-1 states. It ranks below Over because the Morris early-hook/relief upper tail is too material to subordinate. |
| **4** | **Athletics +1.5** | **LEAST LIKELY OF SUPPLIED ROWS** | One-run variance keeps it live, but today's starter/exposure mismatch makes a 2+ Seattle win more central than a one-run game or Oakland win. |

## Potential winner
### **Seattle Mariners — strong qualitative lean**
Representative central family: **Seattle 5-1, 5-2 or 6-2**. The run line is cleaner than the total because 5-2 lands exactly on seven runs.

## Evidence boundary
- Event/start/venue: HIGH — MLB
- Starters: HIGH — MLB probable pages
- Official posted orders: NOT POPULATED in MLB static page at freeze
- Morris rates: HIGH factual quality but VERY SMALL MLB sample
- Gilbert rates/arsenal: HIGH — MLB/Savant
- Bullpen prior-game workload: HIGH factual quality
- Park factor: HIGH — Savant
- Roof: NOT CONFIRMED
- Operator action terms: UNKNOWN
- Probability/value/ROI/stakes: NOT AUTHORISED

# Sources — P-288
## Google Drive — read only
1. `PREDICTION_LOG_COMBINED_2.md` — active authority/current method gates.
2. `RULES_BASEBALL.md` — SFA-BASEBALL v3.4, small-sample starter, hook/relief, low-total separation, series-state and extras controls.

## Official MLB / Statcast
3. MLB probable pitchers — https://www.mlb.com/probable-pitchers/2026-09-04
4. Athletics probable pitchers — https://www.mlb.com/athletics/roster/probable-pitchers
5. Mariners starting lineups — https://www.mlb.com/mariners/roster/starting-lineups
6. Kade Morris MLB profile — https://www.mlb.com/player/kade-morris-695034
7. Logan Gilbert MLB profile — https://www.mlb.com/mariners/player/logan-gilbert-669302
8. Baseball Savant Kade Morris — https://baseballsavant.mlb.com/savant-player/kade-morris-695034
9. Baseball Savant Logan Gilbert — https://baseballsavant.mlb.com/savant-player/logan-gilbert-669302
10. Baseball Savant park factors — https://baseballsavant.mlb.com/leaderboard/statcast-park-factors
11. MLB Athletics-Mariners preview — https://www.mlb.com/stories/game-preview/823093
12. MLB Sept. 3 Athletics-Mariners game story / recap.
13. Athletics transactions/injury pages.
14. Mariners current injury/news pages.

## Cross-checks
15. Baseball-Reference current matchup preview.
16. StatMuse Kade Morris 2026 game log.
17. Baseball-Reference / Baseball Almanac Sept. 3 box score for bullpen workload.
18. Athletics Nation current game preview/thread for secondary lineup/roster context.
19. Reddit current game thread for secondary lineup corroboration only.
20. DraftKings Network current matchup analysis as secondary pitch/platoon corroboration; Savant/MLB fields control.

## Queue
P-288 remains **PREGAME / UNSETTLED**. No retrospective performed.
Next local continuation ID: **P-289**, subject to fresh Drive reconciliation.

---

# P-289 — Western Bulldogs (W) vs Sydney Swans (W) — 2026 AFLW Round 4

## 1. Frozen identity / state

- **Local continuation ID:** `P-289`
- **Competition:** 2026 NAB AFLW Premiership Season
- **Round:** 4 — Indigenous Round
- **Event:** Western Bulldogs v Sydney Swans
- **Venue:** Mission Whitten Oval, Footscray, Victoria
- **Scheduled ball-up:** Saturday 5 September 2026, 12:35 pm AEST
- **Information/state cutoff:** **2026-09-05 12:27:35 Australia/Melbourne**
- **State at cutoff:** `PREGAME`
- **Official current match page:** fixture scheduled, no score/live state at freeze
- **Method:** `MDS-2026.09.04-v3.4`
- **Algorithms:** `GFA-2 + SFA-AFL`
- **Numerical state:** no fitted/validated AFL/AFLW model
- **Probability / edge / staking:** NOT GENERATED / NOT AUTHORISED
- **Retrospective:** NOT PERFORMED

### Exact supplied slate
1. **Western Bulldogs +10.5**
2. **Sydney Swans -10.5**
3. **Over 82.5 combined points**
4. **Under 82.5 combined points**

Operator draw/settlement wording was not supplied; ordinary AFLW full-time score geometry is used for ranking only.

---

## 2. Current selections / availability

### Western Bulldogs
Official Round 4 change:
- **IN:** Ellie Gavalas
- **OUT:** Lauren Ahrens (omitted)

Gavalas returns after 26 disposals, nine tackles and two goals in the VFLW.

Important current absences:
- **Ellie Blackburn — hamstring, 2–4 weeks**
- **De Berry — collarbone, 2–4 weeks**

These absences reduce experienced midfield/defensive structure around Isabelle Pritchard and Jess Fitzgerald.

### Sydney
Official Round 4 changes:
- **IN:** Taylor Smith, Holly Cooper, Tanya Kennedy
- **OUT:** P. McCarthy, M. Thomas, C. Reid (all omitted)

The returns are material:
- Taylor Smith had three goals in Sydney's Round 1 win over Adelaide.
- Holly Cooper had two goals in that same match.
- Tanya Kennedy returns for her first 2026 appearance and adds midfield/scramble pressure.

Sydney therefore enters with a materially stronger forward/midfield availability state than it had in the low-scoring Round 3 win.

---

## 3. Current form and scoring-shot process

### Western Bulldogs
2026:
- R1 beat Gold Coast **40–14** — scoring shots 10–9
- R2 beat Richmond **48–37** — scoring shots 13–12
- R3 lost North Melbourne **23–70** — scoring shots 8–15

Three-game totals:
- points for: **111 (37.0/game)**
- points against: **121 (40.3/game)**
- scoring shots for: **31 (10.3/game)**
- scoring shots against: **36 (12.0/game)**

The 2–1 record is positive, but the scoring-shot differential is **-5**. Round 1's 26-point win was amplified by Gold Coast's 1.8 conversion, while the Round 3 margin was amplified in the opposite direction by North's 11.4 efficiency.

### Sydney
2026:
- R1 beat Adelaide **61–53** — scoring shots 16–18
- R2 beat Essendon **66–42** — scoring shots 21–12
- R3 beat Euro-Yroke **38–15** — scoring shots 13–10

Three-game totals:
- points for: **165 (55.0/game)**
- points against: **110 (36.7/game)**
- scoring shots for: **50 (16.7/game)**
- scoring shots against: **40 (13.3/game)**

Sydney's scoring-shot differential is **+10**. That is the strongest current territory/shot-creation signal on this card.

Conversion caveat:
- Adelaide kicked 7.11 in Round 1.
- Euro-Yroke kicked 1.9 in Round 3.

So Sydney's 3–0 record and margins have benefited from opponent inaccuracy in two games. The underlying process still favours Sydney, but raw winning margins are not copied forward.

---

## 4. Territory / midfield / forward chain

### Sydney
Key chain:
`Morphett ruck influence -> Ham/Gardiner/Kennedy midfield access -> Fish/wing transition -> Taylor Smith/Cooper/Molloy forward targets -> scoring shots`

Evidence:
- Ally Morphett was rated among Sydney's best repeatedly through the opening rounds.
- Laura Gardiner had 30 disposals in the Round 2 win.
- Montana Ham had 27 disposals, eight inside-50s, six tackles and a goal in Round 3.
- Taylor Smith and Holly Cooper materially raise forward conversion/target depth on return.

### Bulldogs
Key chain:
`Pritchard/Fitzgerald contest work -> controlled entries -> McDonald/Hartwig/Gutknecht scoring`

The Bulldogs remain competitive around the ball, but Blackburn's absence removes an experienced midfield/leadership piece and De Berry's absence weakens structural depth. Gavalas' return helps, but does not fully replace both losses.

### Process conclusion
Sydney projects to generate the larger inside-50/scoring-shot budget. The question for -10.5 is whether that territory edge converts into 11+ points rather than a close low-scoring win.

---

## 5. Recent totals / threshold audit

Bulldogs game totals:
- **54**
- **85**
- **93**
Average: **77.3**

Sydney game totals:
- **114**
- **108**
- **53**
Average: **91.7**

Combined simple matchup average of those team game-total environments: about **84.5**, very close to the supplied **82.5** line.

Most recent H2H:
- Western Bulldogs 39–32 Sydney in 2024
- total **71**
- Bulldogs +7

That H2H is downweighted because the current Sydney roster/process and coaching regime have changed.

---

## 6. Conditions

Mission Whitten Oval / West Footscray near freeze:
- around **19°C**
- mostly cloudy
- BOM around 1 pm: approximately **60% chance of rain**
- winds around **11–20 km/h**, broadly southerly/south-westerly depending local forecast point
- severe-weather warning existed for parts of Victoria, but the damaging-wind locations highlighted by BOM did not establish Mission Whitten Oval itself as a damaging-wind venue at freeze

AFL weather treatment is bidirectional:
- wind/showers can lower kicking efficiency and marking cleanliness;
- they can also create repeat entries, turnovers and territory lock-ins.

Therefore conditions give only a **modest Under lean**, not an automatic Under.

---

## 7. Joint game tree

### Central Sydney territory edge
Representative:
- Sydney **47–34** = 81, margin 13
- Sydney **48–33** = 81, margin 15

Effects:
- Sydney -10.5
- Under 82.5

### Close Bulldogs resistance
Representative:
- Sydney **43–36** = 79, margin 7
- Sydney **45–37** = 82, margin 8

Effects:
- Bulldogs +10.5
- Under 82.5

### Sydney forward-return uplift
Representative:
- Sydney **52–34** = 86, margin 18
- Sydney **54–35** = 89, margin 19

Effects:
- Sydney -10.5
- Over 82.5

### High-scoring close branch
Representative:
- Sydney **47–41** = 88, margin 6

Effects:
- Bulldogs +10.5
- Over 82.5

### Low-total separation
Representative:
- Sydney **42–27** = 69, margin 15

This is the mandatory control showing that Under 82.5 does **not** imply Bulldogs +10.5.

### Bulldogs upset branch
Requires:
- Pritchard/Fitzgerald/Gavalas parity or advantage at stoppage;
- Sydney's returning forwards failing to convert;
- Bulldogs controlling territory at home;
- Sydney's prior opponent-inaccuracy benefit regressing.

---

## 8. Ranked forecast

| Rank | Contract | Verdict | Why |
|---:|---|---|---|
| **1** | **Sydney Swans -10.5** | **BEST RELATIVE LEAN** | Sydney's current scoring-shot differential (+10 across three games) is materially better than the Bulldogs' (-5), and Sydney regain Smith, Cooper and Kennedy while the Bulldogs remain without Blackburn and De Berry. The key risk is conversion/margin variance: Sydney's R1 and R3 margins were helped by opponent inaccuracy, so this is not a high-confidence cover. |
| **2** | **Under 82.5 points** | **LEAN / very close total** | The line sits near the reconstructed matchup centre. Weather adds a small efficiency drag, the 2024 H2H finished at 71, and central score families around 47–34/48–33 stay Under. But Sydney's returning forward personnel materially raises the Over branch, so this is only a lean. |
| **3** | **Over 82.5 points** | **LIVE OPPOSITE / close to Under** | Four of the six combined 2026 team-game samples are above 82.5, and Sydney scored 61/66 before injuries reduced its Round 3 forward group. Smith and Cooper returning directly improve scoring ceiling. It ranks just below Under because conditions and Bulldogs' lower scoring-shot creation keep the central corridor close to 80–84. |
| **4** | **Western Bulldogs +10.5** | **LEAST LIKELY, but credible** | Home ground, a low-total environment and Sydney's conversion-assisted margins create a real close-game branch. It ranks fourth because the current territory/shot-creation gap plus Sydney's returning personnel create more 11+ Sydney-win states than one-score/10-point-or-less states. |

---

## 9. Potential winner

### **Sydney Swans — moderate qualitative lean**

Why:
1. 3–0 current record and stronger scoring-shot differential.
2. Better current ruck/midfield territory chain through Morphett/Ham/Gardiner.
3. Taylor Smith, Holly Cooper and Tanya Kennedy return.
4. Bulldogs remain without Ellie Blackburn and De Berry.
5. Sydney has shown both high-scoring (61, 66) and defensive-control (38–15) winning routes.

Why not strong:
1. Sydney's R1 and R3 margins were helped by poor opponent conversion.
2. Bulldogs are 2–1 and return Gavalas.
3. Mission Whitten Oval home familiarity and variable weather raise game-to-game variance.
4. The previous meeting was a seven-point Bulldogs win, albeit in a lower-continuity 2024 regime.

Representative central score:
- **Sydney approximately 47–49**
- **Bulldogs approximately 32–36**

---

## 10. Evidence / honesty boundary

- Event / venue / start: **HIGH — official AFL/AFLW and club sources**
- Selected team changes: **HIGH — official clubs/AFL**
- Exact late-change/final interchange state: **NOT independently published in a current AFLW final-team article at freeze**
- Injury state: **HIGH — official club medical rooms**
- Scores/scoring shots: **HIGH — official AFLW match centres**
- Process interpretation from scoring shots: **descriptive, not fitted**
- Weather: **HIGH — BOM + current structured forecast**
- Current exact turf condition: **NOT independently verified**
- Probability / edge / ROI / staking: **NOT AUTHORISED**
- Retrospective: **NOT PERFORMED**

---

# SOURCE REGISTER — P-289

## A. Google Drive — READ ONLY
1. `PREDICTION_LOG_COMBINED_2.md`
   - active canonical authority / method and publication gates.
2. `RULES_AFL.md`
   - active SFA-AFL v3.4; territory/scoring-chain, conversion, winner/handicap/total and weather controls.

**Drive modification:** NONE.

## B. Official AFL / club sources
3. AFLW Round 4 preview  
   https://www.afl.com.au/aflw/news/1600054/aflw-r4-preview-unbeaten-quartet-eye-another-win-bates-set-for-milestone-match

4. AFLW Round 4 teams  
   https://www.afl.com.au/aflw/news/1600813/aflw-teams-swans-tall-call-important-pie-rested-cats-turn-to-top-ups

5. Western Bulldogs Round 4 team  
   https://www.westernbulldogs.com.au/news/2119105/aflw-team-round-4-v-sydney-swans

6. Sydney Round 4 team  
   https://www.sydneyswans.com.au/news/2119452/aflw-team-three-changes-for-dog

7. Sydney AFLW injury update  
   https://www.sydneyswans.com.au/news/2118723/aflw-injury-update-round-4

8. Western Bulldogs AFLW medical room  
   https://www.westernbulldogs.com.au/aflw/medical-room

9. Current match page — Western Bulldogs v Sydney  
   https://www.sydneyswans.com.au/matches/8907

10. Bulldogs Round 1 — Gold Coast 14, Bulldogs 40  
    Official AFLW match centre.

11. Bulldogs Round 2 — Bulldogs 48, Richmond 37  
    https://www.afl.com.au/aflw/matches/8892

12. Bulldogs Round 3 — North Melbourne 70, Bulldogs 23  
    https://www.afl.com.au/aflw/matches/8897

13. Sydney Round 1 — Adelaide 53, Sydney 61  
    https://www.afl.com.au/aflw/matches/8888

14. Sydney Round 2 — Sydney 66, Essendon 42  
    https://www.sydneyswans.com.au/matches/8891

15. Sydney Round 3 — Sydney 38, Euro-Yroke 15  
    https://www.afl.com.au/aflw/matches/8902

16. AFL.com.au current round expert/preview material  
    - official preview tips Sydney by 13; expert tipping panel showed genuine disagreement and is used only as secondary context, not as forecast input.

## C. Weather
17. Bureau of Meteorology — West Footscray detailed forecast  
    https://www.bom.gov.au/places/vic/west-footscray/forecast/detailed/

18. Current West Footscray structured weather at freeze:
    - mostly cloudy, ~19°C
    - occasional rain risk
    - current Victorian warning context

---

## 11. Local running-log state

Unsettled / incomplete:
1. `LOCAL-GEELONG-20260904`
2. `P-280` Rabbitohs vs Roosters
3. `P-281` Rakuten Monkeys @ Fubon
4. `P-282` TSG Hawks @ Uni-Lions
5. `P-283` Namibia vs South Africa
6. `P-284` USA (W) vs China (W)
7. `P-285` Korea (W) vs Nigeria (W)
8. `P-286` Glasgow Cosmic vs Belfast Wolves
9. `P-287` Bublik vs Paul
10. `P-288` Athletics @ Mariners
11. `P-289` **Western Bulldogs (W) vs Sydney Swans (W)**

P-289 remains **PREGAME / UNSETTLED**.  
No retrospective performed.  
Next local continuation ID: **P-290**, subject to fresh Drive reconciliation.

---

# P-290 — FC Juárez vs Pachuca — 2026 Liga MX Apertura, Round 7

## 1. Frozen identity / state

- **Local continuation ID:** `P-290`
- **Competition:** Liga MX Apertura 2026
- **Round:** 7
- **Event:** FC Juárez vs Pachuca
- **Venue:** Estadio Olímpico Benito Juárez, Ciudad Juárez
- **Scheduled kickoff:** Friday 4 September 2026, 21:00 local / Saturday 5 September 2026, 13:00 AEST
- **Information/state cutoff:** pregame, approximately 20–25 minutes before kickoff
- **State:** `PREGAME`
- **Method:** `MDS-2026.09.04-v3.4`
- **Algorithms:** `GFA-2 + SFA-SOCCER`
- **Numerical state:** no fitted/validated soccer model
- **Probability / edge / staking:** NOT GENERATED / NOT AUTHORISED
- **Retrospective:** NOT PERFORMED

### User-supplied goal lines

- 1st Half Goals: **Over/Under 0.5**
- Full Match Goals: **Over/Under 2.5**

### Additional self-selected markets

- Pachuca team total Over 0.5 goals
- Pachuca double chance (X2)
- Pachuca most corners / corner-race lean

**Important corner limitation:** the user did not provide an exact corner handicap/total line or operator definition. Therefore the corner row is a directional **Pachuca most-corners** lean only and is evidence-capped under `SO-P3`.

---

## 2. Current event / schedule

Current structured soccer schedule source:
- FC Juárez vs Pachuca
- Scheduled
- 5 Sep 2026, 03:00 UTC / 13:00 AEST
- Apertura group/league fixture

Independent current sources also list:
- 21:00 local kickoff
- Estadio Olímpico Benito Juárez
- Liga MX Round 7

Referee:
- Katia Itzel García Mendoza
- VAR: Luis Enrique Santander Aguirre

---

## 3. Current form / regime

### FC Juárez — 0 points from 6 league games

League results:
- 0-1 Puebla
- 0-1 Chivas
- 1-5 Pumas
- 1-6 Monterrey
- 1-2 América
- 0-4 Toluca

Totals:
- goals for: **3**
- goals against: **19**
- average goals scored: **0.50**
- average conceded: **3.17**
- conceded in **6/6**
- Over 2.5 occurred in **4/6**

Juárez's current underlying volume is also weak:
- roughly **7.7 shots per match**
- about **42% possession**
- dangerous-attack volume below Pachuca's current rate

### Major regime change

This is **Gustavo Lema's first game as Juárez coach**.

This materially reduces confidence in blindly projecting the 0-0-6 trend forward. A new coach can:
- compress defensive spacing;
- change press height;
- alter full-back exposure;
- reduce transition concessions;
- shift set-piece roles.

Therefore the recent 19-goal concession sample is decision-relevant but is not treated as a stationary defensive rate.

### Juárez current absences

Current FotMob availability:
- Ettson Ayón — injured
- Luca Martínez Dupuy — injured
- Lucas Romero — injured
- Bryan Romero — injured

These absences further lower confidence in Juárez's attacking floor.

---

### Pachuca — 5 points from 6

Recent Liga MX:
- 3-0 Pumas
- 1-2 Querétaro
- 0-1 León
- 2-3 Puebla
- 1-1 Atlético San Luis
- 1-1 Chivas

Season snapshot:
- **8 scored**
- **8 conceded**
- scored in **5/6**
- Salomón Rondón leads Pachuca with **5 league goals**
- Oussama Idrissi is the main creator with **2 assists**

Recent form is mixed rather than dominant:
- last three Liga MX: 2-3, 1-1, 1-1
- Pachuca has not shown a reliable multi-goal attacking baseline against every opponent

### Pachuca current absences

Current FotMob:
- Alexéi Domínguez — injured
- Andrés Micolta — injured

---

## 4. Goal-process comparison

### Juárez attack
Current mechanism:
- low shot volume
- depleted forward options
- poor score-state confidence after repeated defeats
- new manager creates tactical uncertainty

### Juárez defence
Current mechanism:
- repeated transition/box-entry failures
- 19 goals conceded in 6
- conceded in every league match

### Pachuca attack
Current mechanism:
- Rondón as primary box finisher
- Idrissi / Montiel creation
- higher current shot volume, around **14.5 shots per game**
- stronger dangerous-attack volume than Juárez

The strongest one-sided goal mechanism is therefore **Pachuca to score at least once**, not necessarily a full-game Over 2.5.

This follows the Drive's `contract choice must match the mechanism` rule: one-team attacking superiority should not be automatically promoted into a high combined total.

---

## 5. First-half goal audit

Juárez's six Liga MX first-half states:
- vs Puebla: 0-1 HT — goal
- at Chivas: 0-0 HT — no goal
- vs Pumas: 1-3 HT — goal
- at Monterrey: 1-4 HT — goal
- vs América: 1-1 HT — goal
- at Toluca: 0-2 HT — goal

**1H Over 0.5: 5/6**

Pachuca recent first-half states:
- at León: 0-1 HT — goal
- vs Puebla: 1-2 HT — goal
- at San Luis: 0-0 HT — no goal
- vs Chivas: 0-1 HT — goal

**3/4 recent confirmed Liga MX matches had a first-half goal.**

Most relevant H2H:
- Pachuca 2-0 Juárez — 1-0 HT
- Juárez 2-1 Pachuca — 2-1 HT
- Juárez 2-2 Pachuca — 2-1 HT
- Juárez 2-2 Pachuca — 2-0 HT

**Last four H2Hs: 4/4 Over 0.5 first half.**

This is supporting evidence only. The new Juárez coach is the main regime change that prevents the early-goal streak from being treated as deterministic.

---

## 6. Full-match 2.5-goal line

Juárez:
- 4/6 league matches Over 2.5

Pachuca:
- 3/6 league matches Over 2.5

Recent H2H:
- 2-0 — Under
- 2-1 — Over
- 2-2 — Over
- 2-2 — Over

So the latest four H2Hs were **3/4 Over 2.5**.

However:
- Pachuca's latest two league matches were both 1-1
- Juárez's attacking depth is weakened
- Lema's arrival may produce a lower-risk first game

Therefore Over 2.5 is only the fifth-ranked selection despite Juárez's defensive collapse.

Central score corridor:
- **0-2**
- **1-2**
- **1-1**

This places 2.5 directly on the central threshold.

---

## 7. Corner process

SFA-SOCCER requires corners to be treated separately from goals.

Available current evidence:
- Juárez roughly **7.7 shots per game**
- Pachuca roughly **14.5 shots per game**
- Juárez dangerous attacks around **37.7/game**
- Pachuca around **42.5/game**
- current corner projection source expects approximately **4 Juárez corners to 6 Pachuca**
- combined corner environment around **9.6**

Recent Juárez corner results include:
- vs Puebla: **5-7**
- at Chivas: **2-19**
- at Monterrey: **0-10**
- vs América: **5-7**
- at Toluca: **3-5**

This strongly supports a **Pachuca corner-share advantage** more than a precise total-corners line.

Why not promote a total-corners Over?
- current 9.5 projection is almost 50/50
- no exact operator line was supplied
- score-state can suppress Pachuca corners if they lead early
- Juárez trailing may inflate their late corner share

Therefore the best derivative is:
### **Pachuca most corners / corner race**

Evidence cap: `FORCED RANK / MEDIUM-LOW` because the exact provider/settlement line was not supplied.

---

## 8. Weather / venue

Ciudad Juárez near kickoff:
- around **30°C**
- mostly cloudy
- current hourly forecast showed possible thunderstorms later in the match window

Mechanism:
- heat can reduce sustained pressing tempo
- a later storm can change surface speed / crossing / set-piece exposure
- neither effect is one-directional

Weather therefore adds uncertainty but does not control the goal ranking.

---

## 9. Joint score-state tree

### `SO-B1` Pachuca central control
- Pachuca 2-0
- 1H goal likely
- Pachuca non-loss
- full total Under 2.5

### `SO-B2` Pachuca transition success / Juárez response
- Pachuca 2-1
- 1H Over
- Over 2.5
- Pachuca non-loss

### `SO-B3` new-coach defensive compression
- 1-1
- first-half goal still possible
- Under 2.5
- Pachuca X2 survives

### `SO-B4` Juárez rebound
- Juárez 1-0 / 2-1
- requires new-manager defensive improvement plus Pachuca conversion failure
- main kill path against Pachuca X2 / team-goal picks

### `SO-B5` corner chase
- Pachuca leads early -> Juárez pushes width late
- can reduce Pachuca corner-share edge
- this is why the corner pick is ranked below the core goal/side picks

---

## 10. Ranked five picks

| Rank | Pick | Verdict | Why |
|---:|---|---|---|
| **1** | **Pachuca Over 0.5 team goals** | **BEST RELATIVE LEAN** | Juárez conceded in all 6 Liga MX games and 19 total; Pachuca scored in 5/6 and owns the stronger current shot/creation profile. The new coach can compress Juárez, but preventing Pachuca from scoring entirely remains the narrower branch. |
| **2** | **1st Half Over 0.5 goals** | **STRONG RELATIVE LEAN** | Juárez had a first-half goal in 5/6 league games; Pachuca in 3/4 recent confirmed league matches; last four H2Hs all had a first-half goal. New-coach tactical compression is the primary kill path. |
| **3** | **Pachuca Double Chance (X2)** | **LEAN** | Juárez are 0-0-6 and have major defensive/attacking issues; Pachuca are imperfect but materially more stable. X2 protects the 1-1 branch, which is important because Pachuca's recent form includes consecutive draws and Juárez have a new-manager bounce possibility. |
| **4** | **Pachuca most corners** | **FORCED RANK / MEDIUM-LOW** | Pachuca's shot/territory volume is materially higher; recent Juárez corner splits have often favoured opponents heavily; current projection is around 4-6. Exact provider/market definition not supplied, so this cannot be promoted beyond a capped directional corner lean. |
| **5** | **Over 2.5 total goals** | **LIVE / lowest of the five** | Juárez have gone Over in 4/6 and conceded 19; latest four H2Hs were 3/4 Over. But Pachuca's last two were 1-1, Juárez's attack is depleted, and Lema's first game can compress risk. 0-2 and 1-1 remain major Under branches. |

### User-supplied opposite sides

- **1H Under 0.5:** below the top five
- **Full-match Under 2.5:** very close to Over 2.5, but slightly behind after accounting for Juárez's extreme defensive exposure

---

## 11. Potential winner

### **Pachuca — narrow-to-moderate regulation-time lean**

Reasons:
1. Juárez are 0-0-6 with a -16 goal difference.
2. Pachuca have the superior current shot/territory profile.
3. Rondón provides the strongest individual scoring threat in the match.
4. Juárez's attacking options are reduced by multiple injuries.
5. Pachuca won the most recent meeting 2-0.

Why not strong:
1. Pachuca are only 1-2-3 themselves.
2. Their last two league games ended 1-1.
3. Juárez are at home.
4. This is Gustavo Lema's first match, creating a meaningful tactical-regime break.
5. Exact final starting XIs were not confirmed in the current field-owner/aggregator state before freeze.

Representative central scores:
- **Pachuca 2-0**
- **Pachuca 2-1**
- **1-1**

---

## 12. Evidence / honesty boundary

- Event / venue / schedule: HIGH — structured soccer schedule + multiple current Liga MX media sources
- Juárez/Pachuca table records: HIGH/MEDIUM-HIGH
- Current final XI: NOT CONFIRMED before freeze
- FotMob unavailable-player list: MEDIUM-HIGH
- Goal/shot/possession stats: MEDIUM-HIGH aggregator/stat source
- Corner process: MEDIUM-LOW because exact provider/line was not supplied
- Weather: HIGH structured current forecast
- Calibrated probability/value/ROI/staking: NOT AUTHORISED
- Retrospective: NOT PERFORMED

---

# SOURCE REGISTER — P-290

## A. Google Drive — READ ONLY

1. `PREDICTION_LOG_COMBINED_2.md`
2. `RULES_SOCCER.md`
3. `LEAGUE_RULES_SOCCER.md`

Key rules used:
- current XI/keeper regime
- goal process separated from corner process
- first-half evidence reconciliation
- score-state corner dependence
- contract choice must match mechanism
- new tactical regime / current roster outranks raw historical outcome

**Drive modification:** NONE.

## B. Current fixture / Liga MX reporting

4. Soccer schedule source — FC Juárez vs Pachuca, scheduled 5 Sep 2026 03:00 UTC
5. Sofascore current event page  
   https://www.sofascore.com/football/match/fc-juarez-cf-pachuca/LNszHFb
6. FotMob current event page  
   https://www.fotmob.com/matches/pachuca-vs-fc-juarez/2r8ayb2c
7. RÉCORD match preview / schedule / Gustavo Lema debut  
   https://www.record.com.mx/historia/donde-ver-fc-juarez-vs-pachuca-canales-y-hora-del-partido-de-liga-mx-2026090405295280000
8. RÉCORD — Gustavo Lema appointed  
   https://www.record.com.mx/historia/oficial-gustavo-lema-regresa-para-dirigir-en-la-liga-mx-2026090221543043149
9. Fox Sports — Gustavo Lema / Juárez coaching change
10. Fox Sports / Mediotiempo — referee assignment, Katia Itzel García

## C. Current form / goal / corner research

11. FotMob FC Juárez overview / fixtures
12. FotMob Pachuca overview / fixtures
13. Forebet current Juárez-Pachuca statistical page
    - 6-game goals / shots / possession / dangerous attacks
    - current H2H
14. Forebet current corner page
    - ~9.63 combined-corner environment
    - projected 4-6 split
15. Forebet Juárez-Puebla
    - 0-1, HT 0-1, corners 5-7
16. Forebet Chivas-Juárez
    - 1-0, HT 0-0, corners 19-2
17. Forebet Juárez-Pumas
    - 1-5, HT 1-3
18. Forebet Monterrey-Juárez
    - 6-1, HT 4-1, corners 10-0
19. Forebet Juárez-América
    - 1-2, HT 1-1, corners 5-7
20. Forebet Toluca-Juárez
    - 4-0, HT 2-0, corners 5-3
21. Forebet León-Pachuca
    - 1-0, HT 1-0
22. Sofascore Pachuca-Puebla
    - 2-3, HT 1-2
23. Sofascore San Luis-Pachuca
    - 1-1, HT 0-0
24. Forebet Pachuca-Chivas
    - 1-1, HT 0-1
25. RÉCORD — Apertura scoring leaders
    - Salomón Rondón leads Pachuca scoring

## D. Weather

26. Current Ciudad Juárez hourly weather:
- roughly 30°C around kickoff
- mostly cloudy
- thunderstorm risk later in match window

---

## 13. Local running-log state

Unsettled / incomplete queue now includes:
- prior unresolved local entries through `P-289`
- `P-290` — **FC Juárez vs Pachuca**

P-290 remains **PREGAME / UNSETTLED**.
No retrospective performed.

Next local continuation ID: **P-291**, subject to fresh Drive reconciliation.

---

# P-291 — Ben Shelton vs Denis Shapovalov — 2026 US Open

## 1. Frozen identity / state

- **Local continuation ID:** `P-291`
- **Competition:** 2026 US Open, Men's Singles
- **Round:** Third Round / Round of 32
- **Court:** Arthur Ashe Stadium
- **Surface:** Outdoor hard court
- **Format:** Best-of-five sets
- **Scheduled start:** Friday 4 September 2026, approximately 22:45 EDT / Saturday 5 September 2026, 12:45 AEST
- **Information/state cutoff:** **2026-09-05 12:44:16 Australia/Melbourne / 2026-09-04 22:44:16 New York**
- **Current structured bracket state at cutoff:** `NOT_STARTED`
- **Official US Open SlamTracker state immediately before cutoff:** `Upcoming`
- **Method:** `MDS-2026.09.04-v3.4`
- **Algorithm:** `GFA-2 + SFA-TENNIS`
- **Numerical state:** no fitted / validated tennis model
- **Probability / edge / staking:** NOT GENERATED / NOT AUTHORISED
- **Retrospective:** **NOT PERFORMED**

### Exact supplied slate

1. **Denis Shapovalov +5.5 games**
2. **Ben Shelton -5.5 games**
3. **Over 38.5 total games**
4. **Under 38.5 total games**

**Operator retirement / walkover settlement terms:** `UNKNOWN_DEFINITION`.

---

## 2. Governing tennis controls applied

The Drive's active tennis framework requires:
- best-of-five to remain a separate population from best-of-three;
- current surface and tournament regime to outrank generic career reputation;
- serve, return, set-count and cumulative-game-margin processes to remain linked;
- winner and game handicap to be treated as different contracts;
- retirement/walkover rules to be frozen when supplied; here they were not;
- H2H to be weighted by format, surface, recency and participant continuity rather than copied mechanically.

The current Drive authority remains `PREDICTION_LOG_COMBINED_2.md`; the local mirror continues sequentially because Drive is read-only.

---

## 3. Current ranking and broad current regime

Current ranking sources around the event:
- **Ben Shelton: ATP #9**
- **Denis Shapovalov: ATP #48**

Shelton is seeded **No. 8** at this US Open.

The ranking gap favours Shelton as winner, but the current H2H and serve profiles make a 6+ cumulative-game win materially more demanding than the moneyline.

---

## 4. Current US Open path and workload

### Ben Shelton

Round 1:
- beat Tallon Griekspoor **1-6, 6-1, 7-6(3), 6-2**
- total games: **35**

Round 2:
- beat Hubert Hurkacz **6-3, 5-7, 7-6(3), 7-5**
- total games: **46**

Tournament exposure through two rounds:
- **81 games**
- two four-set matches
- one tiebreak in each match

Official US Open reporting notes Shelton hit **148 mph** in Round 2, the fastest recorded serve of the tournament through two rounds.

Against Hurkacz:
- Shelton had to solve another elite-serving opponent;
- the match remained close deep into the fourth set;
- Shelton saved break pressure and created the decisive late break.

This is strong evidence for Shelton's current ability to navigate close service-dominated sets, but it is not evidence that every set will separate by multiple games.

### Denis Shapovalov

Round 1:
- beat Miomir Kecmanovic **6-4, 4-6, 6-4, 6-1**
- total games: **37**

Round 2:
- beat Luca Van Assche **6-0, 6-4, 7-6(7)**
- total games: **29**

Tournament exposure:
- **66 games**

Shapovalov therefore enters with roughly **15 fewer games of match exposure** than Shelton through two rounds.

Current physical caveat:
- Shapovalov retired from Montreal on 4 August with an ankle injury suffered around the Los Cabos final;
- he subsequently completed a close three-set Cincinnati match and has completed two US Open wins;
- no current match-day medical limitation was found.
This is functional evidence of recovery, not a formal medical clearance.

---

## 5. North American hard-court form

### Shelton

Shelton's strongest current external evidence:
- defended the Montreal Masters 1000 title;
- beat Brandon Nakashima **6-3, 7-6(4)** in the final;
- won the entire Montreal event **without dropping a set across six matches**;
- rose to World No. 6 after that title before later ranking movement.

He then lost his Cincinnati opener to Jaime Faria **6-4, 6-4**, a reminder that his high ceiling still has lower-level volatility.

### Shapovalov

Shapovalov:
- reached the Los Cabos final;
- beat Cameron Norrie **6-3, 5-7, 6-4** in the semifinal;
- then carried an ankle injury into Montreal and retired;
- returned in Cincinnati and lost to Rafael Jodar **7-5, 4-6, 7-5** after leading 5-1 in the third.

This is a mixed current regime:
- high first-strike ceiling;
- enough physical/competitive evidence to extend strong opponents;
- still meaningful volatility and game-management risk.

---

## 6. Official H2H continuity

Official US Open sources list:
- **Shelton leads 4-0**

Important detail:
- **three of the four meetings went to a deciding set**
- **all but one included a tiebreak**

### 2026 Dallas — indoor hard
Shelton won:
- **4-6, 6-4, 7-6(4)**
- cumulative game margin: **Shelton +1**
- total: **33 games** in best-of-three

Shapovalov created 11 break points; Shelton saved 10 of them. This was a highly competitive match.

### 2024 Shanghai — outdoor hard
Shelton won:
- **6-3, 7-5**
- cumulative game margin: **Shelton +5**

This is highly relevant to today's **+5.5** line:
Shapovalov would have covered +5.5 despite losing in straight sets.

### 2024 Washington — outdoor hard
Shelton was leading:
- **7-6(5), 6-6**, 6-3 in the second-set tiebreak
when Shapovalov was defaulted after an exchange with a spectator.

The official H2H counts this as a Shelton win, but it is **not a completed performance result** and must not be used as a clean margin/total observation.

### 2024 Wimbledon — grass, best-of-five
Shelton won:
- **6-7(4), 6-2, 6-4, 4-6, 6-2**
- total: **49 games**
- cumulative game margin: **Shelton +7**

This is the highest **format continuity** meeting but lower **surface continuity** than today's hard court.

### H2H conclusion

The four-match record strongly supports Shelton as the winner lean.

But the shape of the H2H supports Shapovalov's game cushion:
- Dallas: +1 Shelton
- Shanghai: +5 Shelton
- Washington: incomplete, very close through nearly two sets
- Wimbledon: +7 Shelton in five

A 5.5-game line sits directly inside the historical separation corridor rather than outside it.

---

## 7. Serve / return interaction

Both are left-handed first-strike players.

### Shelton
Strengths:
- elite serve speed and free-point creation;
- current US Open serve confidence;
- superior current ranking and recent hard-court results;
- improving ability to return big servers after Griekspoor/Hurkacz.

Primary separation mechanism:
`big first serve -> short return games -> Shapovalov second-serve pressure/errors -> one break per set -> cumulative margin`

### Shapovalov
Strengths:
- explosive lefty serve;
- one-handed backhand capable of early first-strike aggression;
- enough return aggression to create break chances against Shelton;
- current freshness advantage.

Primary cushion/extension mechanism:
`hold-heavy set -> tiebreak or 7-5 set -> steal one set -> cumulative game margin remains compressed`

Primary risk:
- double-fault / aggressive-error clusters;
- scoreboard volatility after losing a close set;
- Shelton's superior recent consistency can turn one bad service stretch into a 6-2 or 6-3 set.

---

## 8. Match environment

National Weather Service evening forecast around Arthur Ashe:
- approximately **26°C at 9 pm**
- around **24–25°C by 10–11 pm**
- NW/N winds around **6–8 mph**
- near-zero precipitation risk

This is broadly neutral-to-good serving weather.

Arthur Ashe has a retractable roof, but exact roof state was not confirmed at the frozen cutoff. No one-sign environmental total adjustment is applied.

---

## 9. Best-of-five set-count / total-games structure

The supplied total is **38.5**.

This line does not require five sets, but it does require the four-set branch to avoid being too compact.

### Over examples
- Shelton 7-6, 6-4, 4-6, 7-6 = **46**
- Shelton 6-4, 7-6, 4-6, 6-4 = **42**
- Shelton 7-5, 4-6, 7-6, 6-3 = **44**

### Under examples
- Shelton 6-3, 6-4, 6-4 = **29**
- Shelton 7-6, 6-4, 6-3 = **32**
- Shelton 6-3, 6-4, 4-6, 6-3 = **38**

The current central tree is:
- Shelton 3-0: meaningful
- Shelton 3-1: largest single branch
- Shelton 3-2: material but smaller
- Shapovalov win: live but subordinate

The 38.5 line therefore sits near the compact-four-set / ordinary-four-set boundary.

---

## 10. Cross-market score tree

### `TE-B1` Shelton close straight sets
Example:
- **7-6, 6-4, 6-4**
- total 33
- Shelton game margin +5

Results:
- **Shapovalov +5.5**
- Under 38.5
- Shelton winner

This is important: Shapovalov +5.5 can survive even a Shelton 3-0.

### `TE-B2` Shelton separated straight sets
Example:
- **6-3, 6-3, 6-4**
- total 28
- Shelton +8

Results:
- Shelton -5.5
- Under 38.5

### `TE-B3` central competitive four-set Shelton win
Example:
- **7-6, 6-4, 4-6, 7-6**
- total 46
- Shelton +2

Results:
- **Shapovalov +5.5**
- **Over 38.5**
- Shelton winner

This is the main central branch.

### `TE-B4` separated four-set Shelton win
Example:
- **6-3, 6-4, 4-6, 6-3**
- total 38
- Shelton +6

Results:
- Shelton -5.5
- Under 38.5

This is the principal alternative branch.

### `TE-B5` five-set extension
Most ordinary five-set score shapes are well above 38.5 and usually keep the game margin compressed unless one set is a blowout.

### `TE-B6` Shapovalov upset
Any Shapovalov win automatically cashes +5.5; most four/five-set upset branches also support Over.

### `TE-B8` retirement
Unknown operator rules. Current pregame medical evidence does not justify assuming a retirement.

---

## 11. Ranked forecast

| Rank | Contract | Verdict | Why |
|---:|---|---|---|
| **1** | **Denis Shapovalov +5.5 games** | **BEST RELATIVE LEAN** | The cushion survives every Shapovalov win and many Shelton wins, including close straight-set or four-set results. Shelton is 4-0 H2H, but three meetings reached a deciding set; Dallas was only a one-game margin and Shanghai only five. Shapovalov is also 15 tournament games fresher. Main kill path is Shelton repeatedly breaking the volatile Shapovalov second serve and producing two or more 6-2/6-3 sets. |
| **2** | **Over 38.5 total games** | **LEAN** | A competitive four-set match clears this line in many ordinary score shapes, and the matchup has repeated tiebreak/deciding-set history. Shapovalov's current form is sufficient to give him a strong set-winning branch. It is not #1 because both players have also produced compact US Open wins and Shelton has a credible 3-0 / compact 3-1 route. |
| **3** | **Ben Shelton -5.5 games** | **LIVE SEPARATION ALTERNATIVE** | Shelton is the better current player, ranked #9 vs #48, owns the 4-0 H2H and recently won Montreal without dropping a set. If Shapovalov's second-serve/error clusters appear, +6 to +10 game margins are plausible. It ranks below the cushion because today's number demands meaningful cumulative separation, not merely a Shelton win. |
| **4** | **Under 38.5 total games** | **LEAST LIKELY, but substantial control branch** | Under is live through Shelton 3-0 and compact 3-1 states, and both men's first two rounds include several matches below 38.5. It ranks fourth because the same serve/tiebreak/set-winning evidence that supports Shapovalov +5.5 also pushes many central four-set branches above the total. |

---

## 12. Potential match winner

### **Ben Shelton — moderate-to-strong qualitative lean**

Why:
1. official H2H **4-0**;
2. current ATP ranking **#9 vs #48**;
3. defended the Montreal Masters title without dropping a set;
4. home-crowd / Arthur Ashe environment suits his first-strike game;
5. current return preparation against Griekspoor and Hurkacz is directly relevant to another big-serving opponent.

Why not stronger:
1. three of four H2Hs went to a deciding set;
2. Shapovalov is playing well enough to have won five sets across two rounds with only one lost set;
3. Shapovalov has lower tournament workload;
4. both are high-variance first-strike players, so tiebreaks materially widen upset variance.

### Representative central score family
**Shelton in four competitive sets**, e.g.
- 7-6, 6-4, 4-6, 7-6

This produces:
- Shelton winner
- Shapovalov +5.5
- Over 38.5

---

## 13. Evidence / honesty boundary

- Event / court / round / pregame state: **HIGH — official US Open + current tournament bracket**
- H2H official count: **HIGH — US Open official**
- Washington 2024: **incomplete/default result, not a clean performance sample**
- Current rankings: **HIGH — ATP**
- US Open scores: **HIGH**
- Shelton Montreal form: **HIGH — ATP**
- Shapovalov ankle history: **HIGH — ATP; current limitation not independently found**
- Current exact medical clearance: **NOT AVAILABLE**
- Roof state: **NOT CONFIRMED**
- Operator retirement terms: **UNKNOWN_DEFINITION**
- Calibrated probabilities / value / ROI / stakes: **NOT AUTHORISED**
- Retrospective: **NOT PERFORMED**

---

# SOURCE REGISTER — P-291

## A. Google Drive — READ ONLY

1. `RULES_TENNIS.md`
   - active tennis-specific controls;
   - best-of-five vs best-of-three separation;
   - serve/return, H2H continuity, retirement and settlement controls.

2. `PREDICTION_LOG_COMBINED_2.md`
   - active canonical authority from P-272 onward;
   - current governing methodology / publication gates.

**Drive modification:** NONE.

## B. Official US Open / ATP

3. Official US Open SlamTracker — Shelton vs Shapovalov  
   https://www.usopen.org/en_US/scores/stats/1313.html

4. US Open official matchup preview — "lefty, big-hitting battle"  
   https://www.usopen.org/en_US/news/articles/2026-09-03/denis_shapovalov_ben_shelton_prepare_for_lefty_big-hitting_battle_at_2026_us_open.html

5. US Open official Friday storylines / night-session preview  
   https://www.usopen.org/en_US/news/articles/2026-09-04/top_5_matches_and_storylines_to_watch_on_friday_at_the_2026_us_open.html

6. US Open official Shelton vs Griekspoor R1 report  
   https://www.usopen.org/en_US/news/articles/2026-08-31/ben_shelton_vs_tallon_griekspoor_at_the_2026_us_open.html

7. US Open official Shelton vs Hurkacz R2 report  
   https://www.usopen.org/en_US/news/articles/2026-09-02/ben_shelton_tops_big-serving_hubert_hurkacz_in_round_2_of_the_2026_us_open.html

8. US Open "By the numbers" after Round 2  
   - Shelton 148 mph fastest recorded serve.

9. Current US Open men's bracket source  
   - Shelton R1/R2 and Shapovalov R1/R2 scores;
   - current Shelton-Shapovalov state `not_started`.

10. ATP — Shelton vs Shapovalov Dallas 2026 semifinal  
    https://www.atptour.com/en/news/fritz-cilic-dallas-2026-sf

11. ATP — Shelton vs Shapovalov Shanghai 2024  
    https://www.atptour.com/en/news/shelton-shapovalov-paul-fognini-shanghai-2024-thursday

12. ATP — Shelton vs Shapovalov Wimbledon 2024  
    https://www.atptour.com/en/news/shelton-shapovalov-wimbledon-2024-saturday

13. ATP / current records — Washington 2024 H2H default state  
    - Shelton 7-6, 6-6, second-set TB 6-3 when Shapovalov was defaulted.

14. ATP — Shelton wins Montreal 2026 without dropping a set  
    https://www.atptour.com/en/news/shelton-nakashima-montreal-2026-thursday-final

15. ATP — Shelton Cincinnati loss to Jaime Faria  
    https://www.atptour.com/en/news/shelton-faria-cincinnati-2026-sunday

16. ATP — Shapovalov Los Cabos semifinal / final run  
    https://www.atptour.com/en/news/shapovalov-norrie-los-cabos-2026-saturday

17. ATP — Shapovalov Montreal ankle retirement  
    https://www.atptour.com/en/news/shapovalov-svajda-montreal-2026-tuesday

18. ATP — Shapovalov vs Rafael Jodar, Cincinnati  
    https://www.atptour.com/en/news/jodar-shapovalov-cincinnati-2026-r2-saturday

19. ATP current rankings / Canadian rankings page  
    - Shelton current #9 from current ranking source;
    - Shapovalov official #48.

## C. Other current research

20. Tennis.com current Shelton-Shapovalov match page  
    - current rankings and H2H score cross-check.

21. Reuters Day 6 / Friday preview
    - current US Open day state and matchup context.

## D. Conditions

22. US National Weather Service — Flushing, NY digital forecast  
    - evening roughly 24–26°C, NW/N wind ~6–8 mph, minimal precipitation risk.

---

## 14. Local running-log state

Unsettled queue now includes prior unresolved records through P-290 plus:

- `P-291` — **Ben Shelton vs Denis Shapovalov**

P-291 remains **PREGAME / UNSETTLED**.  
No retrospective performed.

Next local continuation ID: **P-292**, subject to fresh Drive reconciliation.

---

# P-292 — St Kilda (W) vs North Melbourne (W) — 2026 AFLW Round 4

## 1. Frozen identity / state

- **Local continuation ID:** `P-292`
- **Competition:** 2026 NAB AFLW Premiership Season
- **Round:** 4 — Indigenous Round
- **Event:** Euro-Yroke (St Kilda) vs North Melbourne
- **Venue:** RSEA Park, Moorabbin, Victoria
- **Scheduled ball-up:** Saturday 5 September 2026, **1:05 pm AEST**
- **Frozen research window:** approximately **12:57 pm AEST**, before scheduled ball-up
- **Official match state:** pregame / no score shown in the current AFL match centre at the final check
- **Method:** `MDS-2026.09.04-v3.4`
- **Algorithms:** `GFA-2 + SFA-AFL`
- **Numerical state:** no fitted/validated AFLW model
- **Probability / edge / staking:** NOT GENERATED / NOT AUTHORISED
- **Retrospective:** **NOT PERFORMED — user explicitly requested none**

### Exact user-supplied slate

1. **St Kilda +51.5**
2. **North Melbourne -51.5**
3. **Over 89.5 combined points**
4. **Under 89.5 combined points**

Operator settlement wording was not supplied. Ordinary full-time AFLW score geometry is used for ranking only.

---

## 2. Current team selection / availability

### St Kilda / Euro-Yroke

Official Round 4 changes:
- **IN:** Molly McDonald
- **IN:** Nicola Barr
- **IN:** Carys D'Addario — AFLW debut
- **OUT:** Abby Hobson — ankle
- **OUT:** Alice Burke — ACL
- **OUT:** Saoirse Lally — omitted

Material injury state:
- **Alice Burke — ACL, season**
- **Amber Clarke — ankle, long-term**
- **J'Noemi Anderson — hamstring, medium-term**
- Abby Hobson unavailable this week
- Molly McDonald returns for her first match in 349 days after long-term leg/toe issues

This leaves St Kilda without several established defensive/forward contributors, although McDonald/Barr add experience and D'Addario adds contested pressure.

### North Melbourne

Official Round 4 changes:
- **IN:** Erika O'Shea
- **IN:** Eilish Sheerin
- **OUT:** Tessa Boyd
- **OUT:** Abby Favell

O'Shea returns from concussion protocols and Sheerin from knee swelling.

Material remaining absences:
- **Mia King — neck, season**
- **Amy Smith — knee, season**
- **Taylah Gatt — groin, 2–3 weeks**
- **Nicole Bresnehan — knee, approximately 1 week**

The North defence/transition chain is therefore stronger than in Round 3 because O'Shea and Sheerin return, even though the midfield/outside rotation is not at full strength.

---

## 3. Current 2026 results

### St Kilda — 0-3

- R1: lost to Carlton **40–66**
- R2: lost to Geelong **15–100**
- R3: lost to Sydney **15–38**

Three-game totals:
- **Points for:** 70 = **23.3/game**
- **Points against:** 204 = **68.0/game**
- **Average margin:** **-44.7**
- **Average match total:** **91.3**

### North Melbourne — 3-0 / 30 straight wins overall

- R1: beat Geelong **100–27**
- R2: beat Brisbane **44–33**
- R3: beat Western Bulldogs **70–23**

Three-game totals:
- **Points for:** 214 = **71.3/game**
- **Points against:** 83 = **27.7/game**
- **Average margin:** **+43.7**
- **Average match total:** **99.0**

North's Round 3 victory extended the club's winning streak to **30 consecutive AFLW matches**.

Important caution:
North's margin mean is still below today's **51.5** line, and the Brisbane game shows that elite opponents can compress them significantly.

---

## 4. Scoring-shot / territory process

### North Melbourne

2026 scoring shots:
- vs Geelong: **25** (15.10)
- vs Brisbane: **14** (6.8)
- vs Bulldogs: **15** (11.4)

Total:
- **54 scoring shots**
- **18.0 per game**

Opponents:
- Geelong: 12
- Brisbane: 8
- Bulldogs: 8

Opposition average:
- **9.3 scoring shots/game**

North therefore has a massive current scoring-shot differential.

### St Kilda

2026 scoring shots:
- vs Carlton: **10** (6.4)
- vs Geelong: **5** (2.3)
- vs Sydney: **10** (1.9)

Total:
- **25 scoring shots**
- **8.3 per game**

Opponents:
- Carlton: 21
- Geelong: 20
- Sydney: 13

Opponent average:
- **18.0 scoring shots/game**

The matchup is therefore unusually symmetric:
- North creates about **18** scoring shots/game
- St Kilda concedes about **18**
- St Kilda creates about **8–9**
- North concedes about **9**

This is the strongest process evidence on the card.

---

## 5. Conversion / total interaction

Raw scoring-shot expectation points to something around:
- North: high teens in scoring shots
- St Kilda: high single digits

But AFLW scoring conversion is highly volatile.

St Kilda:
- 6.4 against Carlton — efficient
- 2.3 against Geelong
- 1.9 against Sydney — extremely inefficient despite periods of territorial pressure

North:
- 15.10 against Geelong
- 6.8 against Brisbane
- 11.4 against the Bulldogs

North therefore has both:
- 100-point offensive ceiling
- controlled 44-point winning state

The 89.5 total is not automatically Over simply because North are dominant. A 65–18 or 68–15 result is an Under and can still produce a North -51.5 cover.

---

## 6. Current personnel mechanisms

### North midfield / territory
Key chain:
`Rennie / ruck contest -> Garner + Riddell + Sheerin -> front-half lock -> King / Shierlaw / Randall / Bogue / O'Loughlin`

Current evidence:
- Ash Riddell had 42 disposals against Brisbane.
- Jasmine Garner had 31 in that game.
- North repeatedly won field position through contest and clearance pressure.
- Sheerin's return adds another experienced contest/transition piece.

Mia King's season-ending absence reduces midfield rotation depth, but it has not materially changed North's ability to control territory through three rounds.

### North forward line
Recent contributions are distributed:
- Bogue, O'Loughlin and Shierlaw kicked two each against the Bulldogs.
- Emma King remains a difficult aerial matchup and plays her 100th AFLW game.
- Tahlia Randall remains a strong forward/ruck scoring threat.

This lowers dependence on one single goal scorer.

### St Kilda
Key resistance chain:
`Tyanna Smith / Georgia Patrikios / Serene Watson -> stoppage parity -> Tawhiao-Wardlaw contested marking -> scoring conversion`

St Kilda actually generated periods of dominance against Sydney, especially early and late, but finished **1.9** and failed to convert.

Tawhiao-Wardlaw remains a legitimate high-end marking forward, but the current season conversion/output has been poor.

---

## 7. Head-to-head continuity

Most recent meeting:
- **North Melbourne 67–21 St Kilda**
- margin **46**
- total **88**
- Round 11, 2025

That exact score would:
- cash **St Kilda +51.5**
- cash **Under 89.5**

Process from that game:
- North controlled outside ball and defensive structure;
- Garner/Riddell dominated midfield;
- Emma King kicked three;
- St Kilda competed early but could not maintain field position.

This H2H has reasonable tactical continuity but is still lower-weight than the 2026 scoring-shot/availability state.

---

## 8. Conditions at RSEA Park / Moorabbin

Current structured weather near freeze:
- around **18°C**
- cloudy
- windy
- showers possible later

Bureau of Meteorology severe-weather information also indicated strong/damaging winds in parts of Victoria, while Moorabbin-area observations showed a notably windy broader weather regime.

### AFL weather treatment

Wind/showers are **bidirectional**:
- can reduce set-shot accuracy and long-kick efficiency;
- can reduce clean marks / forward connection;
- can create repeat territory, turnovers and short-field scoring.

For this matchup, the more likely directional effect is:
- **lower conversion efficiency**
- especially harmful to the weaker St Kilda attack

That modestly supports **Under 89.5**, but weather is not used as a stand-alone Under trigger.

---

## 9. Extreme-spread audit: 51.5 points

North -51.5 requires a **52+ point win**.

North's 2026 margins:
- +73
- +11
- +47

Only **1 of 3** has cleared 51.5.

St Kilda's 2026 loss margins:
- 26
- 85
- 23

Only **1 of 3** has exceeded 51.5.

These are tiny descriptive samples, not cover probabilities, but they demonstrate the line sits in the upper tail rather than the ordinary centre.

The official AFLW Round 4 preview tipped North by **53**, almost exactly on the market threshold. That reinforces the conclusion that the spread itself is finely balanced, not a strong favourite handicap.

---

## 10. Joint game tree

### `AFL-B1` — central North dominance, St Kilda resistance
Representative:
- North **62–20** = total 82, margin 42
- North **65–18** = total 83, margin 47

Results:
- St Kilda +51.5
- Under 89.5
- North winner

### `AFL-B2` — North separation / St Kilda suppression
Representative:
- North **68–15** = total 83, margin 53
- North **70–16** = total 86, margin 54

Results:
- North -51.5
- Under 89.5

This branch is why an Under does **not** imply the underdog spread.

### `AFL-B3` — maximum North offensive ceiling
Representative:
- North **80–18** = 98, margin 62
- North **84–20** = 104, margin 64

Results:
- North -51.5
- Over 89.5

### `AFL-B4` — St Kilda converts more normally
Representative:
- North **66–26** = 92, margin 40

Results:
- St Kilda +51.5
- Over 89.5

### `AFL-B5` — weather-compressed game
Representative:
- North **58–17** = 75, margin 41

Results:
- St Kilda +51.5
- Under 89.5

### `AFL-B6` — St Kilda upset / close-game tail
Requires:
- unusually strong stoppage parity;
- North conversion collapse;
- Tawhiao-Wardlaw dominating marks inside 50;
- St Kilda finally converting its own chances.

This is a very low-probability winner branch.

---

## 11. Ranked forecast

| Rank | Contract | Verdict | Why |
|---:|---|---|---|
| **1** | **Under 89.5 points** | **BEST RELATIVE LEAN** | St Kilda average only 23.3 points and now face North's elite defensive/territory system with O'Shea and Sheerin returning. The current scoring-shot matchup heavily favours North while the windy/showery environment modestly reduces conversion. North can dominate 60–70 to 10–20 and still stay Under. Main kill path: North's offence repeats its 100-point Geelong ceiling or St Kilda finally converts its opportunities efficiently. |
| **2** | **St Kilda +51.5** | **LEAN / extreme-cushion value** | North are vastly more likely to win, but 51.5 is a huge margin. North's average 2026 win is +43.7, St Kilda's average loss -44.7, and the 2025 H2H was North by 46. The line therefore asks for a greater separation than the ordinary recent centre. Main kill path: St Kilda are held under ~18 and North reaches the high 60s/70s. |
| **3** | **North Melbourne -51.5** | **LIVE BLOWOUT ALTERNATIVE** | North's scoring-shot edge is enormous, St Kilda are 0-3 with a 34.3 percentage, and Geelong already beat them by 85. North have a real 68-15 / 75-15 / 80-18 family. It ranks behind the cushion because the market asks for 52+, while North's recent +47 over the previously unbeaten Bulldogs and +46 H2H last year both fell short. |
| **4** | **Over 89.5 points** | **LEAST LIKELY, but live through North ceiling** | Over mainly needs North itself to score 70–80+ or St Kilda to contribute 25–30. North's 100-point R1 shows the ceiling, and St Kilda's first two games both had totals above 100. It ranks fourth because St Kilda's own scoring floor is extremely low, North's defence is stronger this week, and conditions are not ideal for clean conversion. |

---

## 12. Potential winner

### **North Melbourne — VERY STRONG qualitative winner lean**

Reasons:
1. **30 consecutive wins**
2. reigning back-to-back premiers chasing a third straight flag
3. current scoring-shot differential approximately **+8.7 per game**
4. St Kilda sit 0-3 with a percentage around **34.3**
5. North regain **Erika O'Shea and Eilish Sheerin**
6. North own decisive advantages through Garner/Riddell, defensive structure and distributed forward targets

Why winner confidence is much stronger than -51.5 confidence:
- a 30–45 point North win still represents complete game control but loses the handicap;
- St Kilda showed against Sydney that it can create enough territory to slow a game despite poor finishing;
- extreme margins are more conversion-sensitive than winner markets.

Representative central score family:
- **North 60–68**
- **St Kilda 16–23**

---

## 13. Evidence / honesty boundary

- Event / venue / scheduled time: **HIGH — AFL/AFLW + official club**
- Team selections: **HIGH — official Saints / North Melbourne**
- Injury state: **HIGH — official club medical updates**
- 2026 results / scoring shots: **HIGH — official AFL match centres**
- 30-game winning streak: **HIGH — official North / AFL**
- 2025 H2H: **HIGH factual quality; medium predictive weight**
- Weather: **HIGH — current structured forecast + BOM context**
- Exact final warm-up / late-change state: **not independently verified after team-sheet publication**
- Probability / value / ROI / staking: **NOT AUTHORISED**
- Retrospective: **NOT PERFORMED**

---

# SOURCE REGISTER — P-292

## A. Google Drive — READ ONLY

1. `RULES_AFL.md`
   - active v3.4 SFA-AFL process;
   - territory, scoring-shot, conversion, extreme-spread and weather controls.
2. `PREDICTION_LOG_COMBINED_2.md`
   - active canonical authority from P-272 onward;
   - current method/publication gates.

**Drive modification:** NONE.

## B. Official AFL / club sources

3. AFLW Round 4 preview  
   https://www.afl.com.au/aflw/news/1600054/aflw-r4-preview-unbeaten-quartet-eye-another-win-bates-set-for-milestone-match

4. AFL 2026 fixture  
   https://www.afl.com.au/news/1523395/full-fixture-no-re-match-for-former-melbourne-coach-mick-stinear-at-geelong-west-coast-eagles-get-a-break-by-avoiding-north-melbourne

5. Official current St Kilda/North match page  
   https://www.saints.com.au/matches/8909

6. St Kilda Round 4 team selection  
   https://www.saints.com.au/news/2119057/aflw-team-selection-round-4-v-north-melbourne

7. St Kilda injury update  
   https://www.saints.com.au/news/2118711/aflw-injury-update-defender-ruled-out-for-season

8. North Melbourne Round 4 team selection  
   https://www.nmfc.com.au/news/2119014/aflw-r4-team-stars-return-for-saturday-stoush

9. North Melbourne Round 4 injury update  
   https://www.nmfc.com.au/news/2118658/aflw-r4-injury-update-stk-v-nmfc

10. St Kilda v Carlton, Round 1  
    https://www.afl.com.au/aflw/matches/8988

11. Geelong v St Kilda, Round 2  
    https://www.afl.com.au/aflw/matches/8890

12. Sydney v St Kilda, Round 3  
    https://www.afl.com.au/aflw/matches/8902

13. North Melbourne v Geelong, Round 1  
    https://www.afl.com.au/aflw/matches/8881

14. Brisbane v North Melbourne, Round 2  
    https://www.afl.com.au/aflw/matches/8893

15. North Melbourne v Western Bulldogs, Round 3  
    https://www.afl.com.au/aflw/matches/8897

16. North Melbourne Round 3 match report / 30 straight  
    https://www.afl.com.au/aflw/news/1596973/north-melbourne-roos-cut-loose-of-western-bulldogs-dogs-determined-defence-to-claim-another-big-win

17. North Melbourne v St Kilda, Round 11 2025  
    https://www.afl.com.au/aflw/matches/7953

## C. Weather

18. Current Moorabbin structured forecast:
- around 18°C near pregame;
- cloudy/windy;
- showers possible later.

19. Bureau of Meteorology current Victoria / Moorabbin context
- current severe-weather/wind warning environment and nearby observation data.

---

## 14. Local running-log state after P-292

Unsettled / incomplete queue includes:
1. `LOCAL-GEELONG-20260904`
2. `P-280` Rabbitohs vs Roosters
3. `P-281` Rakuten Monkeys @ Fubon
4. `P-282` TSG Hawks @ Uni-Lions
5. `P-283` Namibia vs South Africa
6. `P-284` USA (W) vs China (W)
7. `P-285` Korea (W) vs Nigeria (W)
8. `P-286` Glasgow Cosmic vs Belfast Wolves
9. `P-287` Bublik vs Paul
10. `P-288` Athletics @ Mariners
11. `P-289` Bulldogs (W) vs Sydney (W)
12. `P-290` Juárez vs Pachuca
13. `P-291` Shelton vs Shapovalov
14. `P-292` **St Kilda (W) vs North Melbourne (W)**

P-292 remains **PREGAME / UNSETTLED**.  
No retrospective performed.  
Next local continuation ID: **P-293**, subject to fresh Drive reconciliation.

---

# P-293 — Port Adelaide (W) vs Gold Coast SUNS (W) — 2026 AFLW Round 4

## Frozen state
- Competition: 2026 NAB AFLW Premiership Season, Round 4
- Event: Yartapuulti (Port Adelaide) vs Gold Coast SUNS
- Venue: Alberton Oval, Adelaide
- Scheduled ball-up: **2:05 pm ACST / 2:35 pm AEST**
- Frozen research cutoff: approximately **2:02 pm ACST / 2:32 pm AEST**
- Official current match page at final check: pregame / no score displayed
- Method: `MDS-2026.09.04-v3.4 + GFA-2 + SFA-AFL`
- No fitted/validated AFLW model
- No probability/value/staking claims
- No retrospective performed

### Exact supplied slate
1. Port Adelaide -13.5
2. Gold Coast +13.5
3. Over 87.5 combined points
4. Under 87.5 combined points

## Current team selection / availability

### Port Adelaide
Official Round 4 changes:
- IN: Sophie Eaton, Grace Parsons (debut), Kirsty Lamb, Julia Teakle
- OUT: Ella Boag, Emily Elkington (managed), Indy Tahau (ACL), Olivia Crane (managed)

Tahau is the major change:
- 2025 AFLW leading goalkicker
- season-ending ACL
- Port coach Glenn Strachan said Port now needs broader forward contribution from Lauren Young, Piper Window, Gemma Houghton, Ash Woodland, Teakle and others.

Current Port AFLW injuries:
- Chloe Gaunt (hip) 2–3 weeks
- Ellie Hampson (hip) 3–4 weeks
- Jasmine Sowden (foot) 4–6 weeks
- Jemma Charity (knee) season
- Indy Tahau (knee) season
- Caitlin Wendland (training block) season

### Gold Coast
Official Round 4 changes:
- IN: Meara Girvan, Lily Mithen
- OUT: Katie Lynch (injured), Mia Salisbury (omitted)

Gold Coast's key current core includes Charlie Rowbottom, Anne Hatchard, Havana Harris, Alannah Welsh, Ava Usher and Lucy Single.

## 2026 form

### Port Adelaide — 2-1
- R1: defeated Fremantle **41–20**
- R2: lost to Hawthorn **33–65**
- R3: defeated GWS **52–48**

Averages:
- PF **42.0**
- PA **44.3**
- margin **-2.3**
- match total **86.3**

Margins: +21, -32, +4.

### Gold Coast — 1-2
- R1: lost Western Bulldogs **14–40**
- R2: defeated West Coast **69–34**
- R3: lost Geelong **57–64**

Averages:
- PF **46.7**
- PA **46.0**
- margin **+0.7**
- match total **92.7**

Margins: -26, +35, -7.

## Scoring-shot process

Port:
- 6.5 = 11 shots
- 5.3 = 8
- 7.10 = 17
- average **12.0 scoring shots/game**

Gold Coast:
- 1.8 = 9
- 10.9 = 19
- 8.9 = 17
- average **15.0 scoring shots/game**

This current scoring-shot advantage is the strongest evidence for Gold Coast +13.5.

## Territory / personnel mechanisms

### Port
Primary chain:
`Matilda Scholz -> Abbey Dowrick / Kirsty Lamb -> Young / Window / Woodland / Houghton`

Scholz:
- 35 hitouts against Hawthorn
- 30 hitouts, 24 disposals, five clearances and six score involvements against GWS

Young:
- 18 disposals, two goals in Round 3
- match-winning goal
- Rising Star nomination

Window:
- three goals against GWS

Port still has scoring routes, but Tahau's loss lowers the forward ceiling and increases role uncertainty.

### Gold Coast
Primary chain:
`Rowbottom + Hatchard + Mithen -> fast turnover game -> Welsh / Harris / Usher`

R2:
- Welsh kicked five
- Suns scored 69 from 19 shots

R3:
- Rowbottom 39 disposals
- Hatchard 28
- Suns produced 17 scoring shots
- Harris three goals, Usher two

## H2H

Most recent:
- **Port 108–40 Gold Coast, R3 2025**
- margin +68

This is downweighted because:
- Gold Coast's 2026 young core has improved materially
- Anne Hatchard has been added
- Welsh/Usher now contribute meaningful scoring
- Port have lost Tahau
- Port now play under Glenn Strachan's refreshed system

Official AFL Round 4 preview tips **Port by seven**, much closer to the current process than the 2025 margin.

## Weather

Alberton around the pregame window:
- about **16°C**
- breezy/windy
- showers in the Adelaide forecast
- Bureau forecasts: west/southwesterly winds around **35–50 km/h**
- damaging winds possible

Weather can reduce:
- set-shot accuracy
- long-kick efficiency
- clean marking/transition

But can also create:
- repeat entries
- turnovers
- wind-assisted quarters

Therefore weather provides a meaningful but non-deterministic Under adjustment.

## Spread audit

Port -13.5 requires a 14+ win.

Port margins: +21, -32, +4.  
Gold Coast margins: -26, +35, -7.

The current ordinary margin centre does not support Port by 14+ as the default.

### Port cover path
- Scholz controls territory
- Suns youth turns it over under pressure
- Teakle/Young/Window replace Tahau's scoring
- weather hurts Suns fast transition

### Suns cover path
- any Gold Coast win
- draw
- Port win by 1–13

This is the broader state family.

## Total 87.5 audit

Port totals: **61, 98, 100** — avg **86.3**  
Gold Coast totals: **54, 103, 121** — avg **92.7**

Combined recent environment: about **89.5**, very near the line.

Under factors:
- Tahau absent
- strong wind/showers
- Port's strength is contest/ruck control rather than explosive scoring
- Suns fast transition is vulnerable to wind

Over factors:
- Suns scored 69 and 57 in last two
- Port's last two totals were 98 and 100
- both sides have multiple current scoring routes

## Joint score tree

| Scenario | Score | Suns +13.5 | Port -13.5 | U87.5 |
|---|---:|:---:|:---:|:---:|
| Central Port edge | Port 46–39 | ✅ | ❌ | ✅ |
| Central Port edge | Port 48–39 | ✅ | ❌ | ✅ |
| Port territory control | Port 50–33 | ❌ | ✅ | ✅ |
| Open transition | Port 52–46 | ✅ | ❌ | ❌ |
| Port separation | Port 61–40 | ❌ | ✅ | ❌ |
| Suns upset | Suns 49–43 | ✅ | ❌ | ❌ |
| Weather compressed | Port 41–32 | ✅ | ❌ | ✅ |

## Ranked forecast

| Rank | Contract | Verdict | Why |
|---:|---|---|---|
| **1** | **Gold Coast +13.5** | **BEST RELATIVE LEAN** | Suns' last two performances are strong, current scoring-shot average is higher, and Port have lost Tahau. Port have only one 14+ win this season, while the official AFL preview tips Port by seven. |
| **2** | **Under 87.5** | **LEAN / CLOSE TOTAL** | Strong wind/showers plus Tahau's absence slightly suppress expected conversion. Central 46–39 / 48–39 / 50–33 states remain Under. |
| **3** | **Port Adelaide -13.5** | **LIVE HOME-SEPARATION ALTERNATIVE** | Port own the stronger ruck/experienced structure and Alberton advantage, but current margins do not make 14+ the central state. |
| **4** | **Over 87.5** | **LEAST LIKELY, BUT LIVE** | Four of six combined team-games are above the line and Gold Coast's attack has improved, but the weather and Port's major forward loss add meaningful suppression. |

## Potential winner

### **Port Adelaide — narrow qualitative lean**

Why:
1. home Alberton advantage
2. Matilda Scholz is the clearest individual ruck/territory edge
3. Port still has experienced midfield/forward structure
4. Port are 2-1
5. official AFL preview tips Port by seven

Why only narrow:
1. Gold Coast's last two games were a +35 win and -7 loss
2. Suns average more scoring shots and points per game
3. Rowbottom/Hatchard/Welsh/Harris/Usher give real upside
4. Tahau is a major Port loss
5. weather raises margin variance

Representative central family:
- Port **44–49**
- Gold Coast **36–42**

# Sources — P-293

## Google Drive — read only
1. `RULES_AFL.md`
2. `PREDICTION_LOG_COMBINED_2.md`

## Official AFL / clubs
3. Port v Gold Coast match page — https://www.portadelaidefc.com.au/matches/8912
4. AFLW R4 preview — https://www.afl.com.au/aflw/news/1600054/aflw-r4-preview-unbeaten-quartet-eye-another-win-bates-set-for-milestone-match
5. AFLW R4 teams — https://www.afl.com.au/aflw/news/1600813/aflw-teams-swans-tall-call-important-pie-rested-cats-turn-to-top-ups
6. Port R4 team — https://www.portadelaidefc.com.au/news/2119501/team-selection-parsons-to-debut-as-four-changes-made
7. Port injury report — https://www.portadelaidefc.com.au/news/2118616/injury-report-tahau-sidelined-for-remainder-of-season
8. Port coach media — https://www.portadelaidefc.com.au/news/2120160/strachan-on-youngs-rise-round-3-review-and-suns-challenge
9. Gold Coast R4 team — https://www.goldcoastfc.com.au/news/2119511/aflw-round-4-team-girvan-and-mithen-are-in
10. Fremantle v Port R1 — official AFL match centre
11. Port v Hawthorn R2 — official AFL match centre
12. GWS v Port R3 — https://www.gwsgiants.com.au/matches/8903
13. Gold Coast v Bulldogs R1 — official AFL match centre
14. West Coast v Gold Coast R2 — official AFL match centre
15. Gold Coast v Geelong R3 — official AFL match centre
16. Lauren Young R3 report — https://www.portadelaidefc.com.au/news/2118214/a-star-on-the-rise-lauren-youngs-match-winning-moment-earns-rising-star-nomination

## Weather
17. Bureau of Meteorology, Port Adelaide/Adelaide forecast
18. Current structured Alberton forecast around frozen cutoff

## Queue
P-293 remains **PREGAME / UNSETTLED**. No retrospective performed.  
Next local continuation ID: **P-294**, subject to fresh Drive reconciliation.
