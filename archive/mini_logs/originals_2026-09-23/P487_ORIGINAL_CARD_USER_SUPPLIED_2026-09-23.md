DAL Wings @ PHX Mercury — WNBA

I completed the final participant/news refresh at approximately **12:01 PM AEST**. The official WNBA game page still exposed the scheduled game header in the retrievable data and did not provide a confirmed starting-five field, so I have **not used any live score, possession, or play-by-play information**. :chatgpt-content-reference{index="0"}

The current Drive framework remains **MDS-2026.09.19-v4.3 / CR-2026.09.21-3**, `SFA-BASKETBALL`, `SPORTS_ONLY / MARKET_BLIND`. The supplied ±5.5 and 174.5 thresholds were quarantined until the basketball distribution was constructed.

## Final ranking

| Rank | Pick | Estimated probability* | Evidence |
|---|---|---:|---|
| **1** | **Phoenix Mercury +5.5** | **~62%** | **MEDIUM-LOW** |
| **2** | **Over 174.5** | **~52–53%** | **LOW** |
| **3** | **Under 174.5** | **~47–48%** | Forced complement / LOW |
| **4** | **Dallas Wings -5.5** | **~38%** | Forced complement |

### Potential game winner
**Dallas Wings — ~58%**

### Central score
**Dallas 89 – Phoenix 86**

My weighted score object is approximately:

- **Dallas 89.1**
- **Phoenix 86.3**
- **Total 175.5**
- **Dallas margin +2.8**

The clearest distinction is therefore:

> **Dallas is still slightly more likely to win the game, but Phoenix +5.5 is substantially stronger than Dallas -5.5.**

\*All probabilities are `UNVALIDATED_SUBJECTIVE`. The Drive explicitly has no fitted, calibrated and prospectively validated basketball model.

---

## 1. Event and contract integrity

The official WNBA game page lists **Dallas at Phoenix, September 21 at 10:00 PM ET**, equivalent to **September 22 at 12:00 PM AEST**, at Mortgage Matchup Center. Phoenix's official schedule independently lists the game for September 21 at 7:00 PM local time. :chatgpt-content-reference{index="1"}

The relevant preconditions are:

| Gate | Status |
|---|---|
| `BK-P1` WNBA/rules/clock | **PASS** |
| `BK-P2` current availability + confirmed starting fives | **PARTIAL** |
| `BK-P3` full-game phase | **PASS** |
| `BK-P4` operator OT endpoint | **UNKNOWN_DEFINITION** |

The last point matters. Your operator was not specified, so I have not invented its exact overtime/void rules. The sporting distribution includes an explicit overtime branch.

---

# 2. The biggest late-news factor: Dallas's minutes

Dallas is **26-16** and already has a playoff berth secured. Official Wings material says postseason qualification is locked, although seeding can still move. :chatgpt-content-reference{index="2"}

More importantly, reporting attributed to WNBA reporter **Melissa Triebwasser of The IX Sports** says Dallas intends to restrict the regular-season minutes of:

- **Paige Bueckers**
- **Arike Ogunbowale**
- **Jessica Shepard**

during the final three games. :chatgpt-content-reference{index="3"}

I do **not** interpret "minutes restriction" as meaning 20 minutes each. Saturday illustrated why.

Against Phoenix two days ago:

- Bueckers still played **31:29**
- Ogunbowale **36:40**
- Shepard **26:56**
- Kuier **27:25**. :chatgpt-content-reference{index="4"}

So my Dallas exposure tree is not "stars barely play." It is:

**normal starting role → somewhat reduced expected minutes → meaningful chance Dallas still extends them in a close game.**

That uncertainty is particularly damaging to **Wings -5.5**, because final-margin separation depends heavily on who is on court in the fourth quarter.

---

# 3. Injury and availability picture

## Dallas

The strongest recovered late injury report has:

- **Alanna Smith — OUT/not with team, lower left leg**
- **Azzi Fudd — out for the season following right-knee surgery**
- **Costanza Verona — out, personal reasons**. :chatgpt-content-reference{index="5"}

Smith's absence matters beyond raw scoring. It removes frontcourt defensive/rebounding quality from a matchup involving Alyssa Thomas and potentially a returning Kahleah Copper.

The most recent confirmed Dallas starting five against Phoenix on September 19 was:

**Paige Bueckers, Arike Ogunbowale, Maddy Siegrist, Awak Kuier, Jessica Shepard.** :chatgpt-content-reference{index="6"}

That is the most defensible working structure tonight, but **I did not recover an authoritative WNBA release confirming that exact five for this game**, so I will not relabel it as confirmed.

---

## Phoenix

The late injury report lists:

- **Kahleah Copper — probable, right groin**
- **Kara Dunn — probable, right knee**
- **Kelsey Plum — out, lower-left-leg injury / season-ending absence**. :chatgpt-content-reference{index="7"}

Copper is the major swing variable.

She leads Phoenix at approximately **21.3 points per game**, while Alyssa Thomas supplies about **14.5 points, 7.8 rebounds and 8.4 assists**. :chatgpt-content-reference{index="8"}

I have **not** assigned Copper a normal 33-minute workload automatically. Coming back from a three-game groin absence creates a minutes mixture. My central branch assumes something approximately in the high-20s/low-30s, with both lower-workload and normal-workload states retained.

Phoenix's September 19 starters without Copper were:

**Alyssa Thomas, Noemie Brochant, Natasha Mack, Sami Whitcomb, Lexi Held.** Thomas had a 19/10/11 triple-double. :chatgpt-content-reference{index="9"}

With Copper probable, that rotation changes materially.

---

# 4. Baseline team strength

Dallas remains the materially stronger team over the season.

Current StatMuse figures give:

| Metric | Dallas | Phoenix |
|---|---:|---:|
| Offensive rating | **111.5** | **105.4** |
| Defensive rating | **106.4** | **109.1** |
| Net rating | **+5.1** | **-3.7** |
| Pace | ~79–80 | ~79–80 |
| PPG | **89.1** | **84.4** | :chatgpt-content-reference{index="10"}


That is why **Dallas remains my potential winner**.

But season-long Dallas strength does not directly translate into **Dallas -5.5 tonight**, because today's rotation is not a full-strength average-Dallas exposure.

### Location

Dallas scores about **89.6 PPG away from home**. Phoenix averages about **85.8 PPG at home**, with a home ORtg around **107.4** and DRtg around **109.9**. :chatgpt-content-reference{index="11"}

Those figures are descriptive diagnostics, not my forecasting equation, but their combined scoring environment is broadly consistent with a game landing in the mid-170s.

---

# 5. Possession and efficiency model

I project approximately **79–80 possessions** in regulation.

Neither team's season pace supports a dramatic tempo game. The more important issue is efficiency by lineup.

### Dallas offensive advantages

Dallas has:

- higher season offensive efficiency;
- fewer turnovers;
- better overall rebounding;
- more offensive rebounds;
- a more efficient shooting profile.  

Dallas has averaged 89.1 points, 34.5 rebounds and only around 11 turnovers, while Phoenix is at 84.4, 31.6 rebounds and roughly 13 turnovers. :chatgpt-content-reference{index="12"}

The **turnover gap** is particularly important. If Phoenix gives Dallas transition opportunities, the Wings' margin can move from +2/+3 into +8/+10 quickly.

### Why I reduce that advantage tonight

Dallas's three principal creators/rebounders are precisely the players reported for managed workloads:

**Bueckers + Ogunbowale + Shepard.**

Phoenix, meanwhile, may be *adding* Copper back into its creation tree.

That creates an asymmetric rotation change relative to the season-long ratings.

---

# 6. Phoenix offensive route

Phoenix's most important mechanism is **Alyssa Thomas plus Copper**.

Thomas was excellent against Dallas on Saturday:

- 19 points
- 10 rebounds
- 11 assists
- 8-of-11 FG. :chatgpt-content-reference{index="13"}

Phoenix still scored only 82 because the rest of the offence was inconsistent, although Lexi Held supplied 21.

Copper's potential return adds:

- another high-usage scorer;
- rim/transition pressure;
- foul-drawing;
- another late-clock option;
- less creation burden on Thomas.

Phoenix also gets to the foul line more frequently over the full season: approximately **23 attempts/game versus 18.5 for Dallas**. :chatgpt-content-reference{index="14"}

That matters for both **Phoenix +5.5** and the small **Over** lean because close fourth-quarter games can add bonus/intentional-foul scoring.

---

# 7. Recent form

Dallas's last five:

- 92-70 Seattle
- 96-78 Portland
- 97-71 Connecticut
- 97-77 Los Angeles
- 87-82 Phoenix. :chatgpt-content-reference{index="15"}

That's excellent form, but the total scores were:

**162, 174, 168, 174, 169.**

All five finished below 174.5.

Phoenix's last five:

- 84-94 Washington
- 73-80 Washington
- 101-69 Toronto
- 94-91 Portland
- 82-87 Dallas. :chatgpt-content-reference{index="16"}

Totals:

**178, 153, 170, 185, 169.**

Only two exceeded 174.5.

This would superficially suggest **Under**.

However, the Drive explicitly prohibits turning a recent raw-total streak into a forecast without explaining the current mechanism. Tonight differs because:

1. Copper is expected back;
2. Dallas is managing key players;
3. Smith remains absent;
4. Dallas's reduced closing-lineup exposure can weaken defensive suppression;
5. bench minutes can maintain pace rather than automatically slowing the game.

Hence I keep the recent Under trend as a **diagnostic**, not the deciding factor.

---

# 8. Head-to-head

Dallas leads this season's series **2-0**:

- June 11: Dallas **85-70**
- September 19: Dallas **87-82**. :chatgpt-content-reference{index="17"}

Saturday is much more relevant than June, but even Saturday has an important continuity defect:

**Copper did not play.**

Dallas also had the rotation-management plan hanging over Bueckers/Ogunbowale/Shepard and was already without Smith.

Therefore I do not simply extrapolate Dallas's previous five-point victory into another Dallas cover.

The September 19 game was already exactly the sort of state I expect again: Phoenix remained close enough late that Dallas's outright strength was more convincing than its ability to generate large separation. :chatgpt-content-reference{index="18"}

---

# 9. Independent joint-score distribution

Constructed before querying ±5.5 / 174.5.

### `P-487-WNBA-joint-v1`
`UNVALIDATED_SUBJECTIVE`

| Branch | Weight | Representative score | Mechanism |
|---|---:|---:|---|
| **BK-B1 Central** | 26% | DAL 88-86 | ~79 possessions, Dallas efficiency edge but managed stars |
| **BK-B2 Shooting variance** | 13% | PHX 91-87 | Phoenix perimeter/Copper upside |
| **BK-B3 Dallas sustain** | 14% | DAL 94-84 | Bueckers/Arike minutes extend, PHX turnovers become transition points |
| **BK-B4 Dallas slowdown** | 12% | DAL 85-83 | Dallas manages stars and protects lead with reduced closing offence |
| **BK-B5 Phoenix response** | 13% | PHX 90-86 | Copper/Thomas attack reduced Dallas defensive lineups |
| **BK-B6 Phoenix suppression** | 10% | DAL 91-78 | Dallas defence/turnovers collapse PHX scoring |
| **BK-B7 Foul/bonus** | 7% | DAL 93-89 | close late game creates extra FT possessions |
| **BK-B8 OT** | 5% | DAL 96-94 | tie state reaches extra period |

The representative scores are **scenario centres, not deterministic outcomes inside each branch**.

Integrated distribution:

- **Dallas winner: ~58%**
- **Phoenix winner: ~42%**
- **Phoenix +5.5: ~62%**
- **Dallas -5.5: ~38%**
- **Over 174.5: ~52–53%**
- **Under 174.5: ~47–48%**
- weighted total centre: **~175.5**
- weighted Dallas margin: **~+2.8**

---

# 10. Spread separation budget

## Why Phoenix +5.5 is #1

A Dallas victory by **1-5 points** gives us both:

- Dallas as eventual winner;
- Phoenix +5.5 as winner.

And my score centre is only **Dallas +2.8**.

There are several reasons the five-point cushion is valuable:

- Dallas's best three offensive/creation pieces have reported workload-management plans.
- Phoenix gets home court.
- Copper is probable to return.
- Dallas is missing Smith.
- Phoenix stayed within five **without Copper** two days ago.
- Thomas showed that Dallas currently has difficulty completely suppressing Phoenix's primary creator.

The main Phoenix +5.5 failure state is very specific:

> Phoenix turns it over repeatedly, Dallas gets transition opportunities, Bueckers/Arike are permitted normal-ish minutes because the game matters for seeding, and Phoenix's defence cannot contain Dallas's efficiency.

That creates 94-84 / 91-78 type states.

But I do not think those states dominate enough to justify -5.5.

### Rank-1 implied range

My primary Phoenix-cover corridor is approximately:

**PHX +4 through DAL +5**, with Phoenix outright wins included.

That corridor is consistent with a roughly **171-181** ordinary total window, so neither total side is completely tied to Rank #1.

---

# 11. Total budget at 174.5

The threshold is extremely close to the centre.

For the **Over**:

- PHX 86 needs DAL **89+**
- DAL 89 needs PHX **86+**
- PHX 88 needs DAL **87+**

My centre of roughly **89-86 = 175** clears by essentially one possession.

### Why Over narrowly edges Under

The reason is not raw recent totals.

It is the **upper-tail structure**:

- Copper return;
- Dallas star reductions potentially hurting late defence;
- Phoenix free-throw frequency;
- poor Phoenix season defence;
- Dallas's efficient offence;
- close-game intentional fouling;
- overtime.

These make 90-88/93-89/96-94 states somewhat heavier than a symmetric distribution around 174.

### Why confidence is LOW

The opposing mechanisms are strong:

- Dallas may actually cut Bueckers/Ogunbowale/Shepard minutes materially;
- Phoenix is only 11th in offensive rating;
- Phoenix's shooting is inconsistent;
- both teams play around 80 possessions rather than extreme pace;
- Dallas has held its previous five opponents to 82 or fewer.

So **Over is only around 52–53%**. This is not a strong totals position.

---

# 12. Pick-by-pick verdict

### **#1 Phoenix +5.5 — ~62%**
This is the most robust contract.

I can be wrong about the outright winner and still be right here. The central state is Dallas by only 2-3, and current rotation news compresses Dallas's expected closing margin.

**Best-supported selection.**

### **#2 Over 174.5 — ~52–53%**
Very slight lean.

Copper's likely return plus Dallas's weaker late defensive combinations gives the scoring distribution more upper-tail mass than Saturday's 169-point result implies.

**Low confidence.**

### **#3 Under 174.5 — ~47–48%**
There are plenty of Under paths, particularly if Dallas really restricts its primary trio and Copper has a controlled return workload.

It remains close enough that I would not describe the Over as clearly separated.

### **#4 Wings -5.5 — ~38%**
Dallas is the stronger team, but this requires **separation**, not merely victory.

The current rotation environment makes that the weakest of the four supplied selections.

---

# Potential winner

## **Dallas Wings ~58%**

Dallas remains superior in:

- season offensive efficiency;
- defensive efficiency;
- turnover control;
- rebounding;
- overall roster performance;
- recent form. :chatgpt-content-reference{index="19"}

So I still prefer Dallas to win narrowly.

That yields the coherent primary state:

> **Dallas 89, Phoenix 86**

which simultaneously gives:

- **Dallas winner — yes**
- **Phoenix +5.5 — yes**
- **Over 174.5 — narrowly yes**

---

# Source quality and limitations

The largest unresolved issue is **confirmed starting fives**. I recovered the recent starting structures and the final/current injury information, but no authoritative WNBA game-page field confirming both five-player starters appeared before issuance. The Drive's `BK-P2` rule therefore requires minutes/lineup mixtures and prevents a high evidence grade.

I also found a secondary betting-hosted lineup page showing Bueckers/Ogunbowale/Siegrist/Kuier/Shepard and Copper/Whitcomb/Brochant/Mack/Thomas. **I did not use that as authoritative lineup confirmation or use any odds/probabilities from that site**, because the project's source firewall prohibits sportsbook/fantasy/betting inputs from driving the prediction.

## Material sources used

1. **WNBA official game page** — fixture, venue, scheduled game identity. :chatgpt-content-reference{index="20"}
2. **Phoenix Mercury official schedule/ticket page** — independent date/time confirmation. :chatgpt-content-reference{index="21"}
3. **Dallas Wings official site** — playoff qualification/current schedule. :chatgpt-content-reference{index="22"}
4. **WNBA official recap** — Dallas 87-82 Phoenix on September 19. :chatgpt-content-reference{index="23"}
5. **StatMuse** — current Dallas and Phoenix ratings, pace and recent games. :chatgpt-content-reference{index="24"}
6. **StatMuse** — Dallas road and Phoenix home splits. :chatgpt-content-reference{index="25"}
7. **StatMuse** — September 19 Phoenix player/starting-five box score. :chatgpt-content-reference{index="26"}
8. **Her Hoop Stats** — exact Dallas September 19 minutes. :chatgpt-content-reference{index="27"}
9. **Current injury reporting** — Alanna Smith, Copper, Dunn, Plum, Fudd and Verona status. :chatgpt-content-reference{index="28"}
10. **Reporting attributed to Melissa Triebwasser/The IX Sports** — Bueckers/Ogunbowale/Shepard workload restrictions. :chatgpt-content-reference{index="29"}
11. **Sports Research Google Drive** — `METHOD.md`, `RULES_GENERAL.md`, `RULES_BASKETBALL.md`, `SOURCES.md`, `DATA_SOURCE_REGISTER.md`, `UPCOMING_GAME_RESEARCH_GUIDE.md`, current control manifest.
12. User-supplied GitHub repository remains an additional source; no GitHub-only fact was used without verification. :chatgpt-content-reference{index="30"}

---

# Updated Prediction Mini Running Log

The mini-log procedure requires incomplete entries to remain at the top and a fully updated running log after each prediction query. :chatgpt-content-reference{index="31"}

## Prediction Mini Running Log — P-482 onward

**Method:** MDS-2026.09.19-v4.3 / CR-2026.09.21-3  
**Operating mode:** SPORTS_ONLY / MARKET_BLIND  
**Performance status:** LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE  
**Next ID:** **P-488**  
**Retrospective policy:** No automatic retrospective.

### P-482 — CPL Final — Antigua & Barbuda Falcons vs Jamaica Kingsmen
**Status:** UNSETTLED.  
**Market:** Jamaica first six overs O/U 47.5.  
**Ranking:** #1 Over 47.5 ~59.9% LOW; #2 Under ~40.1%.  
**Potential winner:** Antigua ~53%.  
**Distribution:** first-six mean 51.75, SD ~14.43.  
**Main uncertainty:** toss/XI/exact strip unresolved.  
**Sources:** CWI, CPL official material, Jamaica Gleaner/CMC, Wisden, weather, Drive.

### P-483 — WTA Seoul — Katie Volynets vs Elvina Kalieva
**Status:** UNSETTLED.  
**Ranking:** #1 Over 19.5 ~65.2%; #2 Kalieva +4.5 ~58.4%; #3 Volynets -4.5 ~41.6%; #4 Under ~34.8%.  
**Winner:** Volynets ~62%.  
**Centre:** 23.1 games, Volynets +1.66.

### P-484 — WNBA — Atlanta Dream @ New York Liberty
**Status:** UNSETTLED.  
**Ranking:** #1 Under 177.5 ~54%; #2 Atlanta -1.5 ~53–54%; #3 NYL +1.5 ~46–47%; #4 Over ~46%.  
**Winner:** Atlanta ~58%.  
**Centre:** ATL 88-86 NYL.

### P-485 — NFL — NY Giants @ LA Rams
**Status:** UNSETTLED.  
**Ranking:** #1 Giants +6.5 ~61%; #2 Under 47.5 ~54%; #3 Over ~46%; #4 Rams -6.5 ~39%.  
**Winner:** Rams ~64%.  
**Centre:** LAR 24-20 NYG.

### P-486 — MLB — Minnesota Twins @ San Francisco Giants
**Status:** UNSETTLED.  
**Ranking:** #1 Twins ML ~59%; #2 Giants +1.5 ~57%; #3 Under 8 ~47% win/~10% push; #4 Over 8 ~43% win/~10% push.  
**Winner:** Minnesota ~59%.  
**Centre:** MIN 4.2-SF 3.3.

---

## **P-487 — WNBA — Dallas Wings @ Phoenix Mercury**

**Status:** **UNSETTLED — PREGAME/NEAR-TIP FORECAST — NO RETROSPECTIVE**

**Scheduled start:** 22 Sep 2026, 12:00 PM AEST / 21 Sep 10:00 PM ET.  
**Venue:** Mortgage Matchup Center, Phoenix.  
**Final research state:** official retrievable game page still displayed scheduled game information; no live score used.

### Contracts
- Wings -5.5
- Mercury +5.5
- Over 174.5
- Under 174.5

### Availability
**Dallas**
- Alanna Smith OUT, lower left leg.
- Azzi Fudd season-ending knee absence.
- Costanza Verona out/personal.
- Bueckers/Ogunbowale/Shepard reported for managed minutes in final three regular-season games.
- Exact starting five not authoritative-source confirmed tonight.

**Phoenix**
- Kahleah Copper probable, right groin, returning from three-game absence.
- Kara Dunn probable, right knee.
- Kelsey Plum out/season-ending lower-leg absence.
- Exact starting five not authoritative-source confirmed tonight.

### Current team baseline
- Dallas ORtg ~111.5 / DRtg ~106.4.
- Phoenix ORtg ~105.4 / DRtg ~109.1.
- Both approximately 79-80 possessions/game.
- Dallas stronger turnover and rebounding profile.
- Phoenix gains creator/scoring upside if Copper returns.

### Independent joint-score object
`UNVALIDATED_SUBJECTIVE`

| State | Weight | Representative score |
|---|---:|---:|
| BK-B1 central | 26% | DAL 88-86 |
| BK-B2 shooting variance | 13% | PHX 91-87 |
| BK-B3 Dallas sustain | 14% | DAL 94-84 |
| BK-B4 Dallas slowdown | 12% | DAL 85-83 |
| BK-B5 Phoenix response | 13% | PHX 90-86 |
| BK-B6 Phoenix suppression | 10% | DAL 91-78 |
| BK-B7 foul/bonus | 7% | DAL 93-89 |
| BK-B8 overtime | 5% | DAL 96-94 |

**Integrated centre**
- Dallas ~89.1
- Phoenix ~86.3
- Total ~175.5
- Dallas margin ~+2.8

### Ranked picks
1. **PHOENIX +5.5 — ~62% — MEDIUM-LOW**
2. **OVER 174.5 — ~52–53% — LOW**
3. **UNDER 174.5 — ~47–48% — LOW / forced complement**
4. **DALLAS -5.5 — ~38% — forced complement**

### Potential winner
**Dallas Wings ~58%.**

### Rank-1 coherence
- Dallas narrow win + Phoenix +5.5 = **COHERENT**
- Phoenix outright win +5.5 = **COHERENT**
- Over 174.5 = **PARTIAL_OVERLAP**
- Under 174.5 = **PARTIAL_OVERLAP**
- Dallas -5.5 = **DISJOINT from the central Rank-1 state**, though it survives in Dallas sustain/suppression branches.

### Main Rank-1 failure path
Dallas extends Bueckers/Ogunbowale/Shepard toward normal minutes, Phoenix's turnover problem creates transition scoring, Copper's return is limited/ineffective, and Dallas establishes a 7+ closing margin.

### Source mapping
- `RULES_BASKETBALL.md`: BK-P1–P4, minutes mixtures, possession/efficiency model, eight mandatory branches, team-score budget, quarter-by-quarter separation, OT.
- `SOURCES.md` / `DATA_SOURCE_REGISTER.md`: WNBA/team sources primary; secondary availability reports disclosed; betting/fantasy outputs excluded from prediction.
- `LEARNING_REGISTER.md`: **observation only**, not a permanent new rule — late-season playoff-qualified teams require explicit star-minutes distributions rather than assuming season-average exposure.
- No methodology file changed.

---

### Settled section
**No entries settled in this query. No retrospective performed.**

### Current unsettled queue
**P-482, P-483, P-484, P-485, P-486, P-487.**

### Next canonical ID
**P-488**

## Bottom line

**#1 Phoenix +5.5** is clearly the pick I trust most.

Then:

**#2 Over 174.5**  
**#3 Under 174.5**  
**#4 Dallas -5.5**

**Potential winner: Dallas Wings**, most likely by a narrow margin rather than by six or more.
