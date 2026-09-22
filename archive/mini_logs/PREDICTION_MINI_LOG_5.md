# Prediction Mini Log 5

**Status:** ACTIVE LOCAL CONTINUATION LOG  
**Opened:** 2026-08-30 (Australia/Melbourne)  
**Governing method:** MDS-2026.08.29-v2.6 — qualitative champion  
**Numerical state:** NTS-2026.08.25-v0.2 — Stage 0 / pre-fit; no fitted, calibrated or validated numerical model  
**Probability state:** `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`  
**Value state:** `NO VALUE DETERMINABLE` — same-time contract odds were not supplied  
**Predecessor:** `PREDICTION_MINI_LOG_4_P186_CLEANED_SETTLED_2026-08-30.md`  
**Canonical continuation:** starts at `P-187`  

This is a new local mini running log. Google Drive is not edited. Future game-log requests should append to this file and preserve the canonical `P-###` sequence.

---

## Current controlling snapshot

| Field | Current value |
|---|---|
| Snapshot time | 2026-08-30 08:57:44 Australia/Melbourne / 2026-08-29 18:57:44 AST |
| Latest issued event | `P-190` — New Zealand Warriors (W) vs St George Illawarra Dragons (W) |
| Event state at final research refresh | `PREGAME / PRE-FIRST-BALL FEED` — scheduled start 19:00 AST; current scorecard still showed no score, toss or confirmed XI |
| Next canonical forecast ID | **`P-191`** |
| Open event queue | `P-187` — open/pending settlement; `P-188` — live/pending settlement; `P-189` — frozen pregame view pending final |
| Carried provenance-only queue | P-126; P-148-C02; P-149-C02; P-151-C02; P-162; P-166 operator definition; P-176-C05; P-178-C05; P-179-C05 |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Performance note | This is a qualitative pre-first-ball research view. No realised delivery/score was incorporated. |

---

# P-187 — Trinbago Knight Riders vs Jamaica Kingsmen — Republic Bank CPL 2026

## 1. Event / state freeze

| Field | Frozen value |
|---|---|
| Sport | Cricket |
| Competition | 2026 Republic Bank Caribbean Premier League |
| Match | Trinbago Knight Riders vs Jamaica Kingsmen |
| Match number | Match 20 on the freshest current fixture/live feeds |
| Venue | Queen's Park Oval, Port of Spain, Trinidad |
| Scheduled start | 2026-08-29 19:00 AST / 23:00 UTC / 2026-08-30 09:00 Australia/Melbourne |
| Final research refresh | 2026-08-30 08:57:44 Australia/Melbourne |
| Game state | `PREGAME / PRE-FIRST-BALL FEED` |
| Toss | **NOT POSTED at final refresh** |
| Confirmed playing XIs | **NOT POSTED at final refresh** |
| Strip status | **NOT FOUND AFTER SEARCH** — no direct current-strip/curator/toss report was available at cutoff |
| Match conditions status | **FORECAST OBSERVED** — official Trinidad & Tobago Met Service forecast available |
| Operator / shortening / DLS terms | **NOT SUPPLIED / UNKNOWN_DEFINITION** |
| Prices | NOT SUPPLIED |
| Ranking objective | Marginal win-likelihood ordering and robustness, not EV/value |
| Candidate origin | USER_SUPPLIED |
| Decision-set ID | `DS-P187-V01` |
| Method | MDS-2026.08.29-v2.6 qualitative exposure × rate/scenario corridor |

### Schedule/venue reconciliation

A material schedule conflict existed in indexed pages. An older CWI series schedule snapshot still showed TKR–Guyana on 29 August and TKR–Jamaica on 31 August at Brian Lara Cricket Academy. The **fresher current CWI Queen's Park Oval fixture page**, current live-score feeds and current broadcast listing instead identified **TKR vs Jamaica on 29 August at 19:00 AST at Queen's Park Oval**. Under the field-owner + freshness rule, the fresher current CWI venue schedule controls this card. The conflict is retained here rather than silently erased.

---

## 2. Frozen supplied contracts

Research grading assumes a normal, uninterrupted TKR innings and includes extras. Bookmaker-specific DLS, shortening, chase-completion and void/action terms were not supplied and will not be guessed.

| Contract ID | Supplied contract | Research geometry |
|---|---|---|
| `P-187-C01` | TKR score after 20 overs — **Over 178.5** | Wins at 179+ if the research target reaches a normal 20-over endpoint |
| `P-187-C02` | TKR score after 20 overs — **Under 178.5** | Wins at 178 or fewer under the same research endpoint |
| `P-187-C03` | TKR score after 6 overs — **Over 51.5** | Wins at 52+ after exactly six completed overs |
| `P-187-C04` | TKR score after 6 overs — **Under 51.5** | Wins at 51 or fewer after exactly six completed overs |

`C01/C02` and `C03/C04` are exact complementary pairs under this research geometry. Powerplay and full-innings targets are **separate phase distributions** and are not extrapolated mechanically from one another.

---

## 3. Evidence audit

### A. Direct same-opponent evidence

The teams met earlier in CPL 2026 at Sabina Park. Jamaica won the toss and fielded. TKR made **182/6 from 20 overs**, but their first six overs produced only **38/1** and they were only **69/1 after 10 overs**.

The recovery was late-phase driven:
- Nicholas Pooran: 44
- Kieron Pollard: 44 from 22 balls
- Sunil Narine: 19* from 8 balls

Jamaica's bowling in that match included:
- Andre Russell 2/34
- Hunain Shah 2/31
- Keemo Paul 1/31
- Hassan Khan 0/5 from 2 overs
- Vitel Lawes 1/51
- Odean Smith 0/26

**Interpretation:** this is unusually useful for phase geometry. Jamaica demonstrated a credible pathway to hold TKR well below 51.5 in the powerplay, while TKR simultaneously demonstrated a credible Pooran/Pollard/Narine pathway to recover beyond 178.5 later. Therefore the powerplay Under can be stronger than the full-innings Under without contradiction.

### B. TKR current full-innings scoring

Recent completed 20-over TKR innings before this match include:
- **182/6 vs Jamaica**
- **165/6 vs Antigua & Barbuda Falcons**
- **175/6 vs Saint Lucia Kings**

That small current sample is **1 of 3 above 178.5 and 2 of 3 below**. It is diagnostic only, not a calibrated hit-rate estimate.

TKR's most recent game at Queen's Park Oval was a chase of only 128; they reached **128/3 in 14.5 overs** after restricting Barbados to 127/9, so that chase cannot be treated as a completed 20-over team-total observation.

### C. Venue / surface state

Recent Queen's Park Oval cricket has been highly variable:
- Saint Lucia posted **211/4**, with TKR replying **175/6**.
- Barbados were then restricted to **127/9** before TKR chased 128 in 14.5 overs.
- Contemporary reporting described the Barbados-match pitch as **sluggish** and helpful to TKR's slow bowlers.

This is evidence of **strip-to-strip volatility**, not proof that the current strip is slow. Because no direct current-strip report was found, the current strip remains `NOT FOUND AFTER SEARCH`.

### D. Match conditions

The official Trinidad & Tobago Meteorological Service forecast issued on 29 August called for predominantly sunny conditions with only brief isolated showers, plus a **30–40% chance of a heavier shower or thunderstorm favouring western/hilly Trinidad**; nighttime was expected to be mostly fair apart from the odd shower.

No automatic Under adjustment is applied. The weather matters mainly as an interruption/DLS and surface-moisture tail because operator shortening terms are unknown.

### E. Participants / availability

Current squads contain TKR's principal batting ceiling pieces: Colin Munro, Alex Hales, Sunil Narine, Nicholas Pooran and Kieron Pollard.

Jamaica's squad contains Andre Russell, Keemo Paul, Hunain Shah, Odean Smith, Vitel Lawes and Hassan Khan, but **the final XI was not posted at cutoff**. Russell was not in Jamaica's XI in their immediately preceding match according to current preview reporting, so his current selection is a material unresolved branch.

This missing participant release lowers confidence and prevents a `SUPPORTED` grade.

---

## 4. Scenario tree

### Lower-scoring / Under branch

Mechanisms:
- Jamaica reproduce the new-ball control from the first meeting.
- TKR lose an opener inside the powerplay and Pooran/Pollard enter against a still-functional bowling attack.
- A slower or used strip rewards pace-off/spin through overs 7–15.
- Wickets prevent the late Pollard/Narine acceleration from reaching full strength.

Indicative qualitative corridor:
- Powerplay: low-to-high 40s is the central Under branch.
- Full innings: mid-160s to mid-170s central suppression branch.

### Central branch

Mechanisms:
- TKR score steadily rather than explosively in the first six.
- One or two top/middle-order batters establish a base.
- Jamaica contain part of the middle phase but TKR retain enough wickets for a late surge.

Indicative qualitative corridor:
- Powerplay: upper 40s / around the low-50 boundary.
- Full innings: low-to-high 170s, putting 178.5 near an important upper-central boundary rather than deep inside either side.

### High-scoring / Over branch

Mechanisms:
- Fresh/better-paced strip.
- Munro/Hales/Narine win the first six.
- Jamaica omit a key control bowler, especially Russell, or execute poorly.
- Pooran and Pollard enter with wickets in hand.
- Death overs reproduce the prior-match acceleration.

Indicative qualitative corridor:
- Powerplay: 52+ becomes live quickly.
- Full innings: 180s and beyond.

### Key asymmetry

A powerplay Under **does not require** the full-innings Under to win. The earlier H2H itself demonstrated the path:
**38 in the first six → 182/6 after 20 overs**.

---

## 5. Ranked contracts — immutable P-187/V01 forecast

Because the current strip, toss and confirmed XIs were unavailable, all rows are capped below `SUPPORTED`.

| Rank | Contract | Verdict | Evidence | Why it ranks here |
|---:|---|---|---|---|
| **1** | **P-187-C04 — TKR Powerplay Under 51.5** | **LEAN / FORCED-RANK CAP** | **MEDIUM** | Best direct matchup evidence: Jamaica held TKR to 38/1 in the first six in the prior meeting. The 51.5 line requires a genuinely fast 52+ start, while current XI/strip uncertainty argues against upgrading confidence. |
| **2** | **P-187-C02 — TKR 20-over Under 178.5** | **LEAN / FORCED-RANK CAP** | **MEDIUM-LOW** | TKR's recent completed 20-over scores of 182, 165 and 175 put 178.5 near the upper edge of their small current corridor; the recent venue also produced a 127/9 first innings. But the prior 182 and TKR's late-order power make this materially less robust than Rank #1. |
| **3** | **P-187-C01 — TKR 20-over Over 178.5** | **FORCED RANK** | **MEDIUM-LOW** | Real and important counter-branch: TKR already made 182 against this opponent after a slow first half, with Pooran/Pollard/Narine driving late acceleration. Fresh-strip or weakened-Jamaica-bowling scenarios can carry this above 178.5. |
| **4** | **P-187-C03 — TKR Powerplay Over 51.5** | **FORCED RANK** | **LOW–MEDIUM** | TKR have enough top-order firepower to clear 52, but it is the branch most directly contradicted by the only same-opponent powerplay sample (38) and is especially sensitive to the unknown current strip and bowling XI. |

### Bottom/swap test

- Rank #1 vs #2: keep **PP Under 51.5** first because it has the cleaner same-opponent phase evidence and does not depend on predicting TKR's volatile death acceleration.
- Rank #2 vs #3: keep **full Under 178.5** ahead, but only narrowly. Recent completed TKR totals lean below the line; the prior 182 proves the opposite branch is substantial.
- Rank #3 vs #4: keep **full Over 178.5** above PP Over 51.5 because TKR can recover late even after failing the powerplay line.

---

## 6. Potential winner

**Trinbago Knight Riders — `LEAN`, MEDIUM-LOW evidence.**

Supporting mechanisms:
- Home-ground familiarity and a strong immediate rebound against Barbados.
- TKR's spin/pace-off attack was highly effective in the previous Queen's Park Oval match.
- TKR retain multiple match-winning batting finishers.

Contrary mechanisms:
- Jamaica beat TKR by five wickets in their first 2026 meeting.
- Jamaica enter off an 11-run win in which Saim Ayub made a century.
- Toss and confirmed XIs were unavailable at cutoff.
- If Jamaica bowl first with their strongest attack, particularly if Russell returns, the match-winner lean narrows materially.

This is a **winner lean, not a probability or value claim**.

---

## 7. Main kill paths

1. **Fresh batting strip:** the previous game's sluggish surface does not repeat.
2. **TKR opening burst:** Munro/Hales/Narine clear 50 rapidly before Jamaica can establish control.
3. **Jamaica bowling downgrade:** Russell or another control/death bowler is omitted.
4. **Wickets-in-hand at 15 overs:** Pooran/Pollard/Narine convert a moderate first half into 180+.
5. **Weather/shortening:** any DLS or shortened-innings treatment interacts with operator rules that were not supplied.
6. **Toss/chase endpoint:** if TKR bat second and complete a chase before 20 overs, operator settlement for the 20-over team-score market is unknown and must not be guessed.

---

## 8. Source-quality audit

| Source class | Use on this card | Assessment |
|---|---|---|
| Cricket West Indies — current Queen's Park Oval fixture page | Current event identity, venue and scheduled start | **FIELD OWNER / HIGH**, freshest official schedule page used to resolve conflict |
| Cricket West Indies — series/results page | Prior/current official results context | **FIELD OWNER / HIGH**, but older cached schedule rows were treated as stale where they conflicted |
| Trinidad & Tobago Meteorological Service | Match-window weather | **FIELD OWNER / HIGH** |
| Cricket.com.au / Cricbuzz scorecards | Prior TKR–Jamaica score, players and innings flow | **HIGH-QUALITY SECONDARY / SPECIALIST** |
| Current live-score feeds | Pre-first-ball state, no toss/XI yet | **CURRENT CORROBORATION** |
| Nation News / local reporting | Previous QPO surface description | **REPUTABLE LOCAL SECONDARY**; previous-strip evidence only |
| Preview/prediction sites | Availability leads / contextual corroboration | **DISCOVERY ONLY**; not allowed to control decisive facts |

---

## 9. Logging and settlement instructions

At the next query:

1. Check P-187 state first.
2. If live, retain it open unless a requested six-over contract is already mathematically/officially settled.
3. At final, use an official/field-owning result or high-quality scorecard to verify:
   - TKR score after exactly six completed overs;
   - TKR innings endpoint/score;
   - toss, XI and whether TKR batted first or chased;
   - whether any shortening/DLS applied;
   - match winner.
4. If the 20-over market is not research-settleable because TKR chased successfully before 20 overs or weather shortened the innings, record the research outcome separately from unknown operator settlement.
5. If Rank #1 loses, perform the mandatory deep retrospective:
   - opening pair and new-ball matchup;
   - current strip vs prior sluggish strip;
   - Jamaica bowling XI/roles;
   - powerplay boundary rate and wickets;
   - whether the prior-match 38-run powerplay was overweighted.
6. Regardless of outcome, separately retrospect:
   - middle-overs control;
   - wickets in hand at 15 overs;
   - Pooran/Pollard/Narine death acceleration;
   - source freshness and schedule-conflict handling.

---

## 10. Issued forecast freeze

**P-187/V01 controlling ranking**

1. **TKR Powerplay Under 51.5**
2. **TKR 20-over Under 178.5**
3. **TKR 20-over Over 178.5**
4. **TKR Powerplay Over 51.5**

**Potential winner:** **Trinbago Knight Riders — LEAN**

**Probability state:** `NOT GENERATED / NOT PUBLISHED`  
**Value state:** `NO VALUE DETERMINABLE`  
**No realised delivery or match result was used in this forecast.**

---


# P-188 — Boston Red Sox @ New York Yankees — MLB

## 1. Event / state freeze

| Field | Frozen value |
|---|---|
| Sport | Baseball |
| Competition | Major League Baseball — 2026 regular season |
| Event | Boston Red Sox @ New York Yankees |
| Context | Game 2 of a separate-admission day-night doubleheader on 2026-08-29 |
| Venue | Yankee Stadium, Bronx, New York |
| Scheduled start | 2026-08-29 19:15 EDT / 2026-08-30 09:15 Australia/Melbourne |
| Frozen pregame cutoff | **2026-08-29 19:13:12 EDT / 2026-08-30 09:13:12 Australia/Melbourne** |
| Game state at frozen cutoff | **PREGAME — first pitch not yet due** |
| Start-crossing policy | If first pitch occurs before delivery, this V01 remains frozen to the pregame cutoff; no subsequent pitch/score/state may improve it |
| Home batting entitlement | Yankees bat last |
| Operator/action terms | NOT SUPPLIED |
| Prices | NOT SUPPLIED |
| Ranking objective | Marginal win-likelihood / settlement robustness, not EV/value |
| Candidate origin | USER_SUPPLIED |
| Method | MDS-2026.08.29-v2.6 qualitative champion |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |

Official MLB schedule/probable-pitcher pages controlled event identity, venue, time and starter status.

---

## 2. Participant / lineup handshake

### Starting pitchers — official

- **Boston:** LHP **Alec Gamboa** — MLB listed 1-0, 1.31 ERA, 14 SO.
- **New York:** LHP **Max Fried** — MLB listed 4-4, 2.81 ERA, 79 SO.

Important exposure context:
- Gamboa entered with only **20.2 MLB innings**, 12 appearances and **one prior start**. His prior start on Aug. 17 lasted 1.1 innings; the current role is therefore best treated as an **opener / short-start state**, not a normal six-inning starter assumption.
- Fried was scheduled to be **activated from the injured list** for this start after a left-elbow bone bruise. His skill indicators were strong, but post-IL workload/length uncertainty is a real exposure branch.

### Confirmed Boston lineup

1. Jahmai Jones — DH  
2. Ceddanne Rafaela — CF  
3. Wilyer Abreu — RF  
4. Willson Contreras — 1B  
5. Caleb Durbin — 3B  
6. Andruw Monasterio — SS  
7. Nick Sogard — 2B  
8. Connor Wong — C  
9. Eli White — LF  

Boston changed only the catcher from Game 1: **Connor Wong replaced Adley Rutschman**, who caught the afternoon game.

### Confirmed New York lineup

1. Trent Grisham — CF  
2. Ben Rice — DH  
3. Heliot Ramos — RF  
4. Luis García Jr. — 1B  
5. Jazz Chisholm Jr. — 2B  
6. George Lombard Jr. — SS  
7. Spencer Jones — LF  
8. Austin Wells — C  
9. José Caballero — 3B  

Major availability context:
- **Aaron Judge remained on the IL** with a rib stress fracture.
- Current reporting also indicated Giancarlo Stanton was unavailable, materially lowering New York's right-handed power ceiling against a left-handed Boston opener.

---

## 3. Bullpen availability / doubleheader state

### Boston

The Red Sox won Game 1, 6-0. Jake Bennett supplied six scoreless innings, after which:
- **Tyron Guerrero**
- **Garrett Whitlock**
- **Jovani Morán**

each worked in relief.

The key positive for Game 2 is that Boston's four-run ninth inning let the club **avoid using closer Aroldis Chapman**, so the highest-leverage finishing branch remained fresher. Whitlock had also just returned from the IL and therefore should not be presumed to carry a normal repeat-game workload.

Boston's likely pitching tree is therefore:
`Gamboa opener/short start -> bulk innings (Brayan Bello branch reported as possible) -> remaining relief -> Chapman high-leverage close if game state warrants`.

### New York

Game 1 forced New York to use its starter and multiple relief innings. Contemporary box-score reporting showed work from **Yerry De Los Santos, Justin Topa and Ryan Yarbrough** after Carlos Rodón. The important inference is not that the Yankees bullpen is "spent"; it is that **some depth arms carry same-day usage**, while higher-leverage pieces such as David Bednar remained more plausible late-game options.

**Bullpen conclusion:** both clubs have same-day workload effects. This widens late-run variance and prevents a broad Under thesis from becoming a high-confidence play.

---

## 4. Starter / contact-process audit

### Alec Gamboa

2026 MLB sample entering the game:
- 20.2 IP
- 1.31 ERA
- 0.97 WHIP
- 3.23 FIP
- 6.1 K/9
- 2.6 BB/9

Statcast through the pregame dataset:
- .197 BA allowed
- approximately **.246 xwOBA**
- approximately **.271 xSLG**
- ~31.7% hard-hit rate
- ~3.4% barrel rate

Those contact results are legitimately strong, but the sample is only 80 batters faced and his strikeout rate is modest. The correct interpretation is:
**good contact suppression signal + major exposure/sample uncertainty**, not "1.31 ERA true-talent ace."

### Max Fried

Statcast entering the game:
- approximately **.248 xwOBA**
- approximately **.264 xSLG**
- ~31.3% hard-hit rate
- ~1.8% barrel rate

Those indicators are elite and come over a much larger sample than Gamboa's. Fried therefore owns the clearer starter-quality edge. However, because he is returning from an IL stint for a left-elbow bone bruise, the forecast does not assume normal maximum length.

---

## 5. Offence / matchup state

### Boston vs Fried

Boston's confirmed lineup is mostly right-handed, which reduces the raw same-handed platoon problem against Fried. However:
- Rutschman rests after catching Game 1.
- Jarren Duran is not in the Game 2 starting lineup.
- The lineup is deeper in competent contact than in elite top-end power.

Fried's weak-contact profile keeps Boston's central scoring branch compressed despite the handedness mix.

### New York vs Gamboa / Boston bulk relief

New York's lineup is notably left-handed:
- Grisham
- Rice
- García
- Chisholm
- Spencer Jones
- Wells

all bat left-handed.

That gives Boston's left-handed opener a meaningful same-handed matchup pathway early. New York still has right-handed threats in Ramos, Lombard and Caballero, and home last-bat matters in a one-run game, but the absence of Judge sharply reduces the separation tail.

---

## 6. Venue / weather

National Weather Service point forecast for the Bronx around first pitch:
- ~76–77°F
- very light wind, roughly 2–3 mph
- little/no precipitation risk
- relatively clear sky

**Interpretation:** weather is close to neutral. No automatic Over/Under adjustment is justified from conditions.

---

## 7. Coherent joint run corridor

The card is derived from one joint game-state object, not independent narratives.

### Lower-scoring branch
- Fried suppresses hard contact for 4–6 innings.
- Gamboa gets through the top of the Yankees order and Boston's bulk/relief chain avoids free baserunners.
- Missing Yankees power pieces and Boston's reduced lineup keep home-run clustering limited.

Representative scores:
- NYY 3–2
- BOS 3–2
- NYY 2–1

### Central branch
- Fried is better than Boston's lineup but not fully extended.
- Gamboa handles the opener phase but Boston needs significant bullpen/bulk exposure.
- Yankees gain some late leverage without creating a blowout.

Representative scores:
- **NYY 4–3**
- **NYY 3–2**
- BOS 4–3

This branch strongly supports **Boston +1.5** even while keeping **Yankees ML** as the winner lean.

### High-run / separation tail
- Fried's post-IL workload is short and Boston reaches New York's middle relief.
- Gamboa's small-sample suppression regresses sharply or the Yankees' right-handed bats punish mistakes.
- Same-day bullpen use creates late clusters.

Representative scores:
- NYY 6–3
- BOS 5–4
- NYY 7–2

This branch is why **Under 7.0** cannot outrank both side contracts despite the low central score.

---

## 8. Contract geometry

| Contract ID | Contract | Win geometry |
|---|---|---|
| `P-188-C01` | Boston +1.5 | Wins on every Boston win or a one-run Boston loss |
| `P-188-C02` | Yankees ML | Wins on any Yankees victory |
| `P-188-C03` | Over 7.0 | Wins at 8+ total runs; push at exactly 7 |
| `P-188-C04` | Under 7.0 | Wins at 6 or fewer; push at exactly 7 |

Important dependence:
- **Boston +1.5 and Yankees ML overlap** in every one-run Yankees win.
- The central 3–2 or 4–3 Yankees branches can therefore make both side contracts succeed together.
- The 7.0 total has material push mass; Over and Under are not exact binary complements because exactly seven runs pushes both under standard integer-total rules.

---

## 9. P-188/V01 ranked forecast

| Rank | Contract | Verdict | Evidence | Decision |
|---:|---|---|---|---|
| **1** | **Boston Red Sox +1.5** | **LEAN** | **MEDIUM** | Broadest central geometry: Boston can win outright or lose by one. Fried gives New York a starter edge, but the low-run corridor, depleted Yankees offence and Fried workload uncertainty make multi-run separation less robust than the ML edge itself. |
| **2** | **New York Yankees ML** | **LEAN** | **MEDIUM** | Fried is the strongest individual run-suppression component and New York has home last-bat. Yankees are still only a modest winner lean because Fried returns from the IL and Boston's Gamboa/bulk-relief state has legitimate suppression pathways. |
| **3** | **Under 7.0 runs** | **LEAN / THIN** | **MEDIUM-LOW** | Fried's elite contact suppression, Gamboa's early contact profile and New York's missing power support a low central score. The integer 7 provides push protection, but same-day bullpen exposure and both starters' workload uncertainty widen the 8+ tail. |
| **4** | **Over 7.0 runs** | **FORCED RANK** | **MEDIUM-LOW** | Viable mainly through a short Fried return, Gamboa regression, or bullpen cluster. The weather is not an Over driver and the confirmed lineups do not create enough central power to put this above the Under. |

### Final order

1. **Boston Red Sox +1.5**
2. **New York Yankees ML**
3. **Under 7.0**
4. **Over 7.0**

---

## 10. Potential game winner

**New York Yankees — LEAN**

Why:
- Fried supplies the clearer pitcher-quality edge.
- New York has final at-bat.
- Boston's opener/bulk state carries more role/exposure uncertainty than a normal starter.

Why this is not stronger:
- Fried is returning from the IL.
- Judge is unavailable and the New York lineup is left-handed enough to give Gamboa a favourable early matchup.
- Boston just shut New York out 6-0 in Game 1, and its high-leverage closer was preserved.

Potential winner is an alias of the Yankees-ML thesis and is **not** a fifth independent pick.

---

## 11. Main kill paths / retrospective checkpoints

### For Rank #1 Boston +1.5
1. Fried returns at full effectiveness and length, suppressing Boston through six or more innings.
2. Gamboa's small sample fails immediately and Boston's bulk-relief plan allows repeated traffic.
3. Yankees right-handed bats create early extra-base damage despite the left-heavy lineup.
4. Boston's same-day relievers are unavailable and the middle bullpen breaks before Chapman can matter.

### For the Under
1. Fried is restricted to a short post-IL workload.
2. Gamboa exits after 1–2 innings and the bulk arm is ineffective.
3. Doubleheader bullpen fatigue creates a late cluster.
4. Yankee Stadium's HR geometry converts a few otherwise ordinary fly balls into multi-run innings.

If Rank #1 loses, the mandatory deep retrospective must specifically examine:
- actual Fried workload and post-IL stuff;
- Gamboa opener length and bulk-reliever identity;
- Yankees vs LHP platoon execution;
- whether Boston's +1.5 cushion was incorrectly elevated by the low-total thesis;
- whether same-day bullpen depletion was underweighted.

---

## 12. Source-quality audit

**Field-owner / official**
- MLB schedule — event/time/venue.
- MLB Red Sox/Yankees probable-pitcher pages — Gamboa/Fried starter handshake.
- MLB starting-lineup page — confirmed Game 2 lineups.
- MLB injury/roster pages — Fried IL return; Judge absence; Whitlock return context.
- MLB Game 1 reports — 6-0 final, Bennett six scoreless, Boston bullpen usage and Chapman preservation.
- Baseball Savant — pitcher contact-quality metrics.
- National Weather Service — Bronx game-window weather.

**High-quality specialist / secondary**
- Baseball-Reference — Gamboa career/sample size, previous start/exposure.
- Contemporary Game 1 box-score sources — Yankees reliever usage where the official narrative did not enumerate every bullpen arm.

No secondary projection or market model controls the forecast.

---

## 13. Issued forecast freeze

**P-188/V01 — frozen pregame at 19:13:12 EDT**

1. Boston Red Sox +1.5  
2. New York Yankees ML  
3. Under 7.0 runs  
4. Over 7.0 runs  

**Potential winner:** New York Yankees — LEAN  
**Central corridor:** Yankees 3–2 / Yankees 4–3, with Boston one-run-win/loss branches materially represented.  
**Probability:** `NOT_GENERATED / NOT PUBLISHED`  
**Value:** `NO VALUE DETERMINABLE`  

Any game action first known after the frozen cutoff is excluded from this forecast and may be used only for later settlement/retrospective.

---

## Controlling continuation snapshot — after P-188

| Field | Current value |
|---|---|
| Latest canonical event | `P-188` |
| Next canonical ID | **`P-189`** |
| Open forecast queue | `P-187`, `P-188` pending settlement |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |


# P-189 — Alabama A&M Bulldogs vs Howard Bison — Cricket MEAC/SWAC Challenge

## 1. Event / state freeze

| Field | Frozen value |
|---|---|
| Sport | American football |
| Competition | NCAA Division I FCS — Cricket MEAC/SWAC Challenge |
| Event | Alabama A&M Bulldogs vs Howard Bison |
| Site status | **Neutral site** — Center Parc Stadium, Atlanta, Georgia |
| User wording correction | This is **not at Howard**; official Howard, Alabama A&M, MEAC and SWAC sources place the game in Atlanta |
| Scheduled kickoff | 2026-08-29 19:30 EDT / 2026-08-30 09:30 Australia/Melbourne |
| Frozen information cutoff | **2026-08-29 19:24:51 EDT / 2026-08-30 09:24:51 Australia/Melbourne** |
| Game state at cutoff | **PREGAME** |
| Start-crossing rule | If kickoff occurs before delivery, P-189/V01 remains locked to the 19:24:51 EDT pregame information boundary; no live action may improve it |
| TV | ABC |
| Operator / overtime terms | NOT SUPPLIED; research geometry assumes standard NCAA full-game spread/total including NCAA overtime |
| Odds | NOT SUPPLIED |
| Ranking objective | Marginal likelihood / settlement robustness, not EV |
| Method | MDS-2026.08.29-v2.6 qualitative champion |
| Numerical state | Stage 0 / no fitted or validated numerical model |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |

Official schedule control:
- Howard Athletics: Aug. 29, 7:30 p.m. ET, Center Parc Stadium, Atlanta.
- Alabama A&M Athletics: Aug. 29, 6:30 p.m. CT, Center Parc Stadium, Atlanta.
- MEAC/SWAC official schedules corroborate the neutral-site national-TV opener.

---

## 2. Supplied contracts

| Contract ID | Contract | Research geometry |
|---|---|---|
| `P-189-C01` | Alabama A&M +2.5 | Wins on any Alabama A&M win or Howard win by 1–2 |
| `P-189-C02` | Howard -2.5 | Wins only if Howard wins by 3+ |
| `P-189-C03` | Over 46.5 points | Wins at 47+ combined points |
| `P-189-C04` | Under 46.5 points | Wins at 46 or fewer combined points |

Spread pair is complementary around a 2.5-point boundary. Total pair is complementary at 46.5. All four are derived from one discrete scoring tree.

---

## 3. Quarterback / regime handshake

### Alabama A&M — Cornelious Brown IV

Brown is the clearest high-value continuity input on either side.

Official 2025 line before his season was cut short by injury:
- 81/125 passing
- 64.8% completion
- 1,060 passing yards
- 7 passing TD
- 1 INT
- 265.0 passing yards per game
- 21 rushes, 80 yards, 3 rushing TD

Game-by-game examples:
- 260 pass yards, 3 pass TD + 69 rush yards, 2 rush TD vs Alcorn
- 329 pass yards, 2 TD at Tennessee State
- 341 pass yards, 2 TD + rush TD vs Jackson State

Brown is listed on the 2026 roster and was Alabama A&M's representative at SWAC media day / HBCU National Player of the Year preseason watch list.

**Interpretation:** returning, experienced, efficient QB with legitimate pass + scramble/red-zone value. The injury history prevents a full-strength certainty assumption, but the available pregame evidence is materially firmer than Howard's current quarterback regime.

### Howard — Ja'Shawn Scroggins

Howard's official preseason material identifies graduate **Ja'Shawn Scroggins** as a 2026 Preseason All-MEAC Second-Team quarterback.

However, his 2025 Howard usage was extremely limited:
- 5/17 passing
- 33 yards
- 0 TD
- 1 INT
- 13 rushes, 41 yards, 1 TD

Howard's Aug. 28 preview points back to a more substantial 2024 body of work (123/231, 1,262 passing yards, 9 TD), but that older sample belongs to a different prior season/regime and is not treated as equivalent to current 2026 form.

**Interpretation:** plausible experienced starter, but current Howard-system predictive evidence is thin. That uncertainty widens both Howard's scoring floor and ceiling.

---

## 4. Coaching / roster regime

### Howard

- **Ted White begins his first season as head coach.**
- Howard finished 5-7 in 2025.
- Howard was picked sixth in the 2026 MEAC preseason poll.
- The defense/secondary is the more stable unit: Kedrick Green, Kaleb Gallop and Ben Chandler IV return, with Green carrying major preseason recognition.
- RB **Eden James** returns as a Preseason All-MEAC First-Team player. Howard's official preview cites his 2024 production at 97 carries for 422 yards and 23 receptions for 146 yards; he appeared only twice in the 2025 team stats.

**Effect:** Howard has a credible run-game/field-position route to winning, but the new head coach + current QB sample means its offensive drive efficiency should not be projected as a settled regime.

### Alabama A&M

- Sam Shade enters his second season.
- Alabama A&M finished 4-8 in 2025 after starting 3-1 in non-conference play.
- Defensive returners include preseason All-SWAC first-team DL **Arenza Davis** and LB **Wyatt Wright**, plus returning DB Jeremiah Hudson-Davis.
- K **David Faulk** was a preseason first-team SWAC specialist, supporting field-goal conversion in stalled red-zone drives.

**Effect:** A&M owns greater QB/coaching continuity, but cannot simply erase the 2025 defensive weakness because several returners received preseason honors.

---

## 5. 2025 process baselines — descriptive only

### Alabama A&M
2025 team:
- 23.4 points/game scored
- 33.4 points/game allowed
- 348.3 offensive yards/game
- 423.8 yards/game allowed
- 5.4 offensive yards/play
- 6.6 yards/play allowed
- 5.0 opponent rush yards/attempt
- 9.04 opponent pass yards/attempt

This is a **major defensive warning**, particularly for the Howard cover/favourite and Over branches.

### Howard
2025 team:
- 19.8 points/game scored
- 24.6 points/game allowed
- 288.6 offensive yards/game
- 334.7 yards/game allowed
- 4.6 offensive yards/play
- 5.8 yards/play allowed
- 123.3 rush yards/game
- 165.3 pass yards/game

Howard's 2025 defense was materially stronger than Alabama A&M's, but its offense was also clearly less productive.

These rates are priors only. They are not copied mechanically into a 2026 Week 0 forecast because Howard changed head coach/QB regime and both teams changed personnel.

---

## 6. Weather / venue

Latest NWS Atlanta point forecast before kickoff:
- mostly cloudy Saturday night
- around low 70s later in the evening
- light southeast wind around 5 mph
- point forecast had only a small precipitation chance around the kickoff transition

The broader NWS area discussion warned of scattered afternoon/evening thunderstorms and locally gusty/heavy-rain cells, but the latest point forecast near Atlanta had the immediate storm chance falling by early evening.

**Weather decision:** no automatic Under. Retain a small wet-ball/field-position branch, but the observed forecast does not justify making weather the controlling total signal.

Center Parc Stadium is neutral; neither side receives a true campus home-field assumption.

---

## 7. One coherent drive / score tree

### Low-scoring branch
Mechanisms:
- Howard's new offensive regime struggles on early downs.
- Scroggins faces pressure / passing efficiency remains modest.
- Howard's secondary limits Brown's explosive pass game.
- Both teams settle for punts/field goals; field position from Howard punter Liam Allen IV matters.

Representative scores:
- Alabama A&M 23–17
- Howard 21–20
- Alabama A&M 20–17

This branch strongly supports **A&M +2.5** and **Under 46.5**.

### Central branch
Mechanisms:
- Brown provides Alabama A&M with the better quarterback efficiency.
- Howard's run game with Eden James keeps possession and avoids a collapse.
- Alabama A&M's defense allows enough successful drives to keep the game within one score.

Representative scores:
- **Alabama A&M 24–21**
- **Alabama A&M 23–21**
- Howard 24–23

This is the controlling corridor.

### High-scoring branch
Mechanisms:
- Alabama A&M's 2025 defensive leakage persists despite returning defenders.
- Howard converts explosive runs/short fields into touchdowns.
- Brown attacks Howard's coverage successfully and both teams trade scores.
- Turnovers or special teams create short-field/non-offensive scoring.

Representative scores:
- Alabama A&M 30–24
- Howard 28–24
- Alabama A&M 31–27

This branch supports the Over but does not automatically support Howard -2.5.

### Howard separation branch
For Howard -2.5 to become the best side, the Bison need more than simply "A&M had a bad defense last year." The 3+ margin branch is strongest if:
- Scroggins proves materially better than his small 2025 Howard sample;
- Eden James consistently wins early downs;
- Howard's secondary suppresses Brown;
- A&M's protection/penalties create drive-killing sacks and long downs;
- Brown's injury/return state reduces his mobility or efficiency.

That branch is real, but it is less central than a one-score game.

---

## 8. P-189/V01 ranked forecast

| Rank | Contract | Verdict | Evidence | Why |
|---:|---|---|---|---|
| **1** | **Alabama A&M +2.5** | **LEAN** | **MEDIUM** | Broadest side geometry plus the clearer returning-QB regime. Brown is a much more established current offensive driver than Howard's 2026 QB situation. This wins on any A&M victory and Howard wins by 1–2. |
| **2** | **Under 46.5 points** | **LEAN / THIN** | **MEDIUM-LOW** | Howard's 2025 offense was modest and now enters a new coaching/QB regime; Howard's defense is the more stable unit. Central 23–21 / 24–21 outcomes fall below the line. A&M's defensive history prevents a stronger grade. |
| **3** | **Over 46.5 points** | **FORCED RANK / LIVE COUNTER-BRANCH** | **MEDIUM-LOW** | A&M allowed 33.4 ppg and 6.6 yards/play in 2025, so Howard has a genuine route to 24–28 points; Brown also raises A&M's offensive ceiling. This is close to the Under and would rise quickly if A&M's defensive problems persist. |
| **4** | **Howard -2.5** | **FORCED RANK** | **LOW-MEDIUM** | Howard can win, but winning by 3+ asks the least robust side geometry given the QB/regime uncertainty and A&M's offensive continuity. |

### Frozen order

1. **Alabama A&M +2.5**
2. **Under 46.5**
3. **Over 46.5**
4. **Howard -2.5**

---

## 9. Potential winner

**Alabama A&M — slight LEAN**

Why:
- Cornelious Brown IV is the strongest proven current offensive player/regime in the matchup.
- A&M has coaching continuity entering Sam Shade's second season.
- Howard is starting a new head-coach era and has much less current-team evidence at quarterback.

Why the lean stays slight:
- Alabama A&M's 2025 defense was poor across both run and pass efficiency.
- Howard's secondary is a credible strength.
- Eden James' return adds a run-game component that was largely absent from Howard's 2025 baseline.
- Neutral-site Week 0 games carry substantial personnel and early-season variance.

Potential winner is an alias of the A&M side thesis, not a fifth independent contract.

---

## 10. Main kill paths

### Rank #1 A&M +2.5
1. Howard's new offense is immediately more efficient than its 2025 baseline.
2. Eden James establishes a strong rushing possession edge against A&M's previously weak run defense.
3. Howard's secondary takes away Brown's explosive passing routes.
4. A&M's 2025 penalty/defensive mistakes persist and create short fields.
5. Brown's prior injury materially affects mobility or availability.

### Under 46.5
1. A&M's defensive weakness persists and Howard reaches the mid/high 20s.
2. Brown creates explosives and red-zone touchdowns rather than field goals.
3. Turnovers/returns create short-field or non-offensive touchdowns.
4. Weather is benign enough that neither offense faces a suppression mechanism.

---

## 11. Retrospective requirements

If Rank #1 loses, deep review must examine:
- Brown's actual health/mobility and pressure rate;
- Howard's Scroggins passing efficiency vs the pregame uncertainty;
- Eden James rushing success and early-down conversion;
- A&M defensive yards/play and explosive-play allowance;
- whether "QB continuity" was overweighted relative to Howard's defensive/field-position edge;
- whether the +2.5 cushion was incorrectly treated as broad enough despite a credible Howard separation branch.

Regardless of result, audit:
- actual drive count / neutral pace;
- third/fourth-down conversion;
- red-zone TD vs FG conversion;
- turnover/short-field scores;
- punt/field-position effects;
- any weather interruption or wet-ball mechanism.

---

## 12. Source-quality audit

**Official / field-owner**
- Howard Athletics — schedule, neutral site, kickoff, roster, 2025 stats, 2026 preseason personnel and coaching regime.
- Alabama A&M Athletics — schedule, roster, 2025 stats, Brown history, 2026 preseason personnel.
- MEAC and SWAC — competition identity, TV/kickoff, preseason conference context.
- National Weather Service Peachtree City / Atlanta point forecast — weather.

**Secondary use**
- ESPN game log for Brown was used only to corroborate the official A&M season totals and game-by-game passing outputs.

No sportsbook editorial model or public pick is used as a controlling forecast input.

---

## 13. Issued forecast freeze

**P-189/V01 — frozen 19:24:51 EDT, pregame**

1. Alabama A&M +2.5  
2. Under 46.5  
3. Over 46.5  
4. Howard -2.5  

**Potential winner:** Alabama A&M — slight LEAN  
**Central score corridor:** Alabama A&M 24–21 / 23–21, with Howard 24–23 retained as a central counter-branch.  
**Probability:** `NOT_GENERATED / NOT PUBLISHED`  
**Value:** `NO VALUE DETERMINABLE`

Any game action first known after the frozen cutoff is excluded from this forecast and belongs only to later settlement/retrospective.

---

## Controlling continuation snapshot — after P-189

| Field | Current value |
|---|---|
| Latest canonical event | `P-189` |
| Next canonical ID | **`P-190`** |
| Open forecast queue | `P-187`, `P-188`, `P-189` pending settlement/final |
| Probability state | `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |




# P-190 — New Zealand Warriors (W) vs St George Illawarra Dragons (W) — NRLW Round 9

## Event freeze
- Venue: Go Media Stadium, Auckland.
- Scheduled kickoff: 2026-08-30 13:45 NZST / 11:45 Australia/Melbourne.
- Frozen cutoff: 2026-08-30 13:30 NZST / 11:30 Australia/Melbourne.
- State: PREGAME.
- Method: MDS-2026.08.29-v2.6 qualitative champion.
- Probability: NOT_GENERATED / NOT PUBLISHED.
- Value: NO VALUE DETERMINABLE.

## Final teams and key availability
Warriors: Anastasia Sekene; Lavinia Tauhalaliku, Mele Hufanga, Stacey Waaka, Tysha Ikenasio; Gayle Broughton, Patricia Maliepo; Annetta Nuuausala, Jasmin Huriwai, Matekino Gray, Kaiyah Atai, Shakira Baker, Maarire Puketapu. Bench: Capri Paekau, Harata Butler, Ivana Lauitiiti, Ashlee Matapo. Apii Nicholls, Emmanita Paki, Mya Hill-Moana and Payton Takimoana are unavailable. Sekene debuts at fullback; Gray and Tauhalaliku return.

Dragons: Teagan Berry; Maria Paseka, Tyra Ekepati, Tahlia O'Brien, Jayme Millard; Zali Hopkins, Kasey Reh; Amelia Huakau, Brooke Anderson, Ruby-Jean Kennard-Ellis, Montana Clifford, Ella Koster, Hannah Southwell. Bench: Tori Shipton, Seriah Palepale, Trinity Tauaneai, Keele Browne. Taliah Fuimaono, Shenae Ciesiolka and Nita Maynard-Perrin are out. Anderson shifts to hooker and Southwell to lock.

## Current season state
Warriors: 4-4, 172 points for, 196 against. Recent: lost 30-22 to Wests Tigers and 66-8 to the Roosters. Their New Zealand results have been materially stronger, including 32-10 over Canterbury, 42-4 over North Queensland and 22-14 over Newcastle.

Dragons: 1-7, 92 points for, 206 against. Recent: lost 16-12 to Wests Tigers, 26-10 to Gold Coast and 32-28 to North Queensland. The Round 8 loss is an important counter-signal because the Dragons scored six tries.

## Weather
Auckland was mostly cloudy, around 17 C and windy near the cutoff, with spotty afternoon shower risk. This is treated as bidirectional: possible handling/kicking suppression, but also error/short-field risk.

## Joint score tree
Central suppressed states: Warriors 26-12, 28-14, 30-14.
Competitive Dragons states: Warriors 26-18, 28-18, 24-20.
Warriors separation states: 32-12, 34-14, 36-10.
Open-game states: 32-20, 34-18, 30-22.

## P-190/V01 ranking
1. Under 47.5 points — LEAN, MEDIUM.
2. Dragons +15.5 — LEAN / THIN, MEDIUM-LOW.
3. Warriors -15.5 — FORCED RANK, MEDIUM-LOW.
4. Over 47.5 points — FORCED RANK, MEDIUM-LOW.

Potential winner: New Zealand Warriors — LEAN.

## Main reasoning
Under 47.5 ranks first because the strongest central states remain in the low-to-mid 40s. The Warriors' stronger New Zealand/home regime, the Dragons' additional role disruption, a debut Warriors fullback and windy/showery conditions all support less clean sustained scoring than a two-way shootout.

Dragons +15.5 ranks second because a 16+ Warriors margin is a materially stronger requirement than an outright Warriors win. The Dragons have just shown a six-try attacking ceiling and have recent narrow losses, while the Warriors have key spine/backline changes.

Warriors -15.5 remains a credible third-ranked separation branch because the Warriors are the stronger winner, have previously produced large New Zealand wins and face a 1-7 Dragons side with current role reshuffling.

Over 47.5 ranks fourth. It requires the Warriors' recent defensive collapse to persist, a short-field/error cluster, or both teams to convert attacking opportunities efficiently.

## Rank #1 retrospective trigger
If Under 47.5 loses, review set count, completion rate, field position, line breaks, missed tackles, goal-line entries, try conversion, weather/handling direction, goal-kicking and any sin-bin/injury branch.

## Continuation
Next canonical ID: P-191.
Open queue at issue: P-187 schedule-conflicted/upcoming; P-188 live/pending settlement; P-189 live/pending settlement; P-190 pregame.

---

# Settlement sweep before P-191

## P-188 — Boston Red Sox @ New York Yankees — SETTLED
Official final: **Yankees 9, Red Sox 2**.

| Rank | Contract | Result |
|---:|---|---|
| 1 | Boston +1.5 | LOSS |
| 2 | Yankees ML | WIN |
| 3 | Under 7.0 | LOSS |
| 4 | Over 7.0 | WIN |

Potential winner Yankees: **WIN**.

**Rank-1 retrospective:** Boston +1.5 remained live deep into the game, but New York turned a 4-2 game into 9-2 with a five-run eighth. The forecast correctly retained an upper-total/bullpen-cluster branch, but underweighted a one-sided late-relief separation path. Preserving Boston's closer did not protect the cushion while Boston was trailing; the relevant state was the middle/low-leverage chain before a save situation existed. Candidate lesson: for baseball +1.5, explicitly stress the trailing-team relief hierarchy and one-sided late cluster even when the central total is low.

## P-189 — Alabama A&M vs Howard — SETTLED
Official final: **Howard 31, Alabama A&M 24**.

| Rank | Contract | Result |
|---:|---|---|
| 1 | Alabama A&M +2.5 | LOSS |
| 2 | Under 46.5 | LOSS |
| 3 | Over 46.5 | WIN |
| 4 | Howard -2.5 | WIN |

Potential winner Alabama A&M: **LOSS**.

**Rank-1 retrospective:** Howard led 13-0, Alabama A&M recovered to lead 24-23 with 7:49 left, then Howard hit a 51-yard touchdown with 2:41 remaining and added two points for the final seven-point margin. Brown IV still threw for 254 yards and two touchdowns, so the A&M QB-continuity thesis was not fictitious. The main error was treating uncertainty in Howard's new offensive regime too directionally against Howard rather than widening both tails. The late explosive-score branch was also underweighted for both spread and total.

## P-190 — Warriors (W) vs Dragons (W) — SETTLED
Official final: **Dragons 22, Warriors 18**.

| Rank | Contract | Result |
|---:|---|---|
| 1 | Under 47.5 | WIN |
| 2 | Dragons +15.5 | WIN |
| 3 | Warriors -15.5 | LOSS |
| 4 | Over 47.5 | LOSS |

Potential winner Warriors: **LOSS**.

The total/cushion structure was correct: 40 total points and a competitive Dragons path. The weaker element was winner allocation: two Dragons tries in the final five minutes flipped an 18-14 Warriors lead. Rank #1 process remains broadly compliant; late finishing/man-down states matter more for the winner branch than the total centre.

---

# P-191 — Walyalup (Fremantle W) vs Carlton W — AFLW Round 3

## Event freeze
- Venue: **Cockburn ARC Oval, Western Australia**.
- Scheduled start: **30 Aug 2026, 3:05 PM AWST / 5:05 PM Australia/Sydney**.
- Forecast refresh: approximately **2:48 PM AWST / 4:48 PM Australia/Sydney**.
- GAME-STATE: **PREGAME**; current official/ABC pages showed no live score.
- Method: **MDS-2026.08.30-v2.7** qualitative champion.
- Target: `AFLW_JOINT_FINAL_SCORE-v1` — official final scores at the final siren; margin and total derived from the same joint score tree.
- Prices/operator terms: not supplied; no value claim.
- Late changes: no field-owning late-change bulletin found at final refresh; last confirmed selection releases control.

## Contracts
1. Fremantle +11.5
2. Carlton -11.5
3. Over 85.5
4. Under 85.5

## Current selection regime
**Fremantle/Walyalup:** Holly Egan and Noa McNaughton debut; Georgie Brisbane returns for her first home-and-away match of 2026. Ash Brazill is out in concussion protocols; Laura Pugh and Tunisha Kikoak were omitted. Brazill's absence removes an experienced defensive/transition role, while Brisbane and McNaughton add forward options but with limited current AFLW sample.

**Carlton:** Tara Bohanna returns for Brooke Vickers; otherwise the Blues retain a settled side from their 2-0 start. Bohanna kicked 15 goals in 2025 and adds another established forward target.

## Territory / scoring-shot evidence
**Carlton:**
- R1 beat St Kilda 66-40, kicking 9.12: **21 scoring shots**; won clearances 32-22.
- R2 beat Adelaide 50-23, kicking 7.8: **15 scoring shots**. Adelaide finished +12 inside 50s, but Carlton's defence repelled shallow entries and Carlton generated cleaner scoring opportunities.
- Current mechanism: contest/spread -> transition -> higher-quality entries -> multiple scoring sources, with strong defensive interception/shot-quality suppression.

**Fremantle:**
- R1 lost to Port Adelaide 20-41, kicking 2.8: **10 scoring shots**. Fremantle had 11 first-quarter inside 50s but kicked 0.4.
- R2 beat Collingwood 50-30, again on exactly **10 scoring shots**, but converted 8.2. Fremantle won inside 50s 40-29 and controlled possession; Mim Strom was dominant in ruck/clearance work.
- The same 10-shot volume produced 20 one week and 50 the next. Therefore recent points cannot be projected without conversion sensitivity.

## Weather / venue
Cockburn conditions were sunny/mostly sunny, mid-20s Celsius, negligible rain risk and light wind. Weather is effectively neutral and does **not** supply an Under shortcut. Cockburn is Fremantle's new AFLW home base, but the Dockers already lost their first premiership match there, so no strong automatic home coefficient is applied.

## Conversion-sensitive score tree
- Lower conversion / Carlton control: **44-28, 46-30, 42-32** Carlton.
- Central: **48-32, 50-34, 52-35** Carlton.
- Fremantle home-pressure branch: **43-36, 45-38 Carlton; 42-39 Fremantle**.
- High-conversion/open branch: **57-40, 59-38, 53-44 Carlton**.

## P-191/V01 ranking
| Rank | Contract | Verdict | Evidence | Reason |
|---:|---|---|---|---|
| 1 | **Carlton -11.5** | LEAN | MEDIUM | Carlton has won by 26 and 27, owns the more stable midfield/front-half regime, adds Bohanna, while Fremantle loses Brazill and has two debutants. Low aggregate scoring can still coexist with Carlton separation through Fremantle suppression. |
| 2 | **Under 85.5** | LEAN / THIN | MEDIUM-LOW | Fremantle has only 10 scoring shots in each game and Carlton's defence has suppressed shot quality. Three of four current game totals involving these sides are below 85.5. Dry conditions and extra forward personnel prevent stronger confidence. |
| 3 | **Fremantle +11.5** | FORCED RANK / credible counter-branch | MEDIUM-LOW | Home ground, Strom/Bowers contest strength and the 2025 nine-point H2H create a close-game route. It ranks below Carlton because current 2026 performance and Fremantle's defensive personnel change strengthen the ordinary Carlton separation path. |
| 4 | **Over 85.5** | FORCED RANK | MEDIUM-LOW | Needs combined scoring-shot volume nearer the upper branch and/or strong conversion. Carlton can carry much of the total, but Fremantle's ordinary shot-volume centre keeps this fourth. |

## Potential winner
**Carlton — LEAN**.

Main path: stable midfield and front-half, multiple scoring sources, Bohanna return, and Fremantle's Brazill absence. Strongest kill path: Strom/Bowers control stoppage/territory, Fremantle's returning forwards improve shot quality, and Carlton's first interstate trip suppresses its transition efficiency.

## Rank-1 kill paths
Carlton -11.5 loses if Fremantle holds Carlton around the low/mid-40s while reaching the mid-30s; Fremantle's new forward mix materially lifts inside-50 efficiency; the interstate trip reduces Carlton's transition; or Carlton's first-two-round defensive shot-quality edge regresses.

If Rank #1 loses, retrospect clearances, inside-50s, marks inside 50, scoring shots, shot quality/pressure, conversion, and Brazill replacement effects before changing any rule weight.

## Issued freeze
1. **Carlton -11.5**
2. **Under 85.5**
3. **Fremantle +11.5**
4. **Over 85.5**

Potential winner: **Carlton**.
Central score corridor: **Carlton 48-32 / 50-34 / 52-35**.
Probability state: `NOT_GENERATED / NOT PUBLISHED`.
Value state: `NO VALUE DETERMINABLE`.

Next canonical ID: **P-192**.


---

# P-192 — SSG Landers @ KIA Tigers — KBO

## Status
**POSTPONED / RAIN — NO ACTIONABLE FORECAST ISSUED**

The 2026-08-30 KBO game at Gwangju-KIA Champions Field was scheduled for 18:00 KST but was officially postponed because of rain before first pitch. This P-192/V01 entry preserves the research state and a conditional matchup ordering only. It is not performance-eligible and must not be graded as a forecast.

## Frozen event identity
- Competition: 2026 KBO regular season
- Event: SSG Landers @ KIA Tigers
- Original venue: Gwangju-KIA Champions Field
- Original start: 2026-08-30 18:00 KST / 19:00 Australia/Melbourne
- Actual state: POSTPONED — rain
- Originally announced starters: SSG RHP Lee Jun-ki vs KIA RHP James Naile
- Operator terms: NOT SUPPLIED
- Probability state: NOT_GENERATED / NOT_PUBLISHED
- Value state: NO VALUE DETERMINABLE
- Performance role: EXCLUDED — POSTPONED BEFORE FIRST PITCH

## Original supplied contracts
1. SSG Landers +1.5
2. KIA Tigers -1.5
3. Combined Over 9.5
4. Combined Under 9.5

## Starter evidence before postponement

### James Naile — KIA
- 24 games, 140 2/3 IP
- 9-5, 3.71 ERA
- Four consecutive quality starts entering the scheduled game
- 3 starts / 18 IP vs SSG in 2026 with a 3.50 ERA

### Lee Jun-ki — SSG
Scheduled first KBO start.
- First-team sample: 3 IP, 6.00 ERA
- 2026 Futures: 16 G, 75 1/3 IP, 3-5, 2.75 ERA
- 63 H, 4 HR, 15 BB, 53 SO
- Opponent BA .230

The Futures record creates a legitimate good-start branch, but first-team starter exposure remained highly uncertain.

## KIA lineup published before postponement
1. Park Jae-hyun — LF
2. Lee Ho-yeon — 2B
3. Kim Do-young — 3B
4. Harold Castro — 1B
5. Na Sung-bum — RF
6. Kim Sun-bin — DH
7. Kim Ho-ryeong — CF
8. Kim Tae-gun — C
9. Jeong Hyeon-chang — SS

A current field-owning SSG starting nine was not verified before the cancellation, so no exact SSG batting-order assumption is frozen into this conditional card.

## Team / matchup baseline
- KIA: 63-50-2, 3rd
- SSG: 48-65-5, 9th
- KIA entered on a three-game winning streak
- KIA held a 9-3-1 season H2H advantage entering the scheduled game
- The previous night's game went 10 innings, KIA winning 2-1
- SSG had scored 13, 6 and 7 in its previous three wins over Hanwha before being held to 1 by KIA

## Conditional joint run tree
Only relevant if the same starter/participant regime is retained on the rescheduled date.

### KIA-control branch
Representative scores:
- KIA 4-2
- KIA 5-2
- KIA 5-3

### Close branch
Representative scores:
- KIA 4-3
- KIA 5-4
- SSG 4-3

### KIA separation branch
Representative scores:
- KIA 6-2
- KIA 7-3
- KIA 8-3

### High-total branch
Representative scores:
- KIA 7-4
- KIA 8-5
- SSG 6-5

## Conditional research ordering
**NON-ACTIONABLE — full re-verification required on rescheduled date**

1. **KIA Tigers -1.5 — LEAN, CONDITIONAL**
2. **Under 9.5 runs — LEAN / THIN, CONDITIONAL**
3. **SSG Landers +1.5 — FORCED RANK, CONDITIONAL**
4. **Over 9.5 runs — FORCED RANK, CONDITIONAL**

### Potential winner
**KIA Tigers — LEAN, conditional on the same starter/participant regime.**

## Reissue requirements
Before any rescheduled P-192 forecast:
1. verify the new official date/time and venue;
2. reconfirm both starters;
3. reconfirm both starting lineups;
4. rebuild bullpen availability from the new preceding workload;
5. refresh injuries/roster moves;
6. refresh weather;
7. rebuild the joint run tree;
8. freeze a new P-192 view before first pitch.

## Continuation
This event occupies canonical ID **P-192** but has no performance-eligible forecast in V01.

**Next distinct event ID: P-193.**


---

# P-193 — Essendon (W) vs Richmond (W) — AFLW Round 3

## Event/state freeze

| Field | Frozen value |
|---|---|
| Competition | 2026 NAB AFLW Premiership Season — Round 3 / Indigenous Round |
| Event | Essendon vs Richmond |
| Venue | TIO Stadium, Darwin, Northern Territory |
| Official latest start | 2026-08-30 18:50 ACST / 19:20 AEST (Australia/Sydney/Melbourne) |
| Forecast cutoff | 2026-08-30 19:16 AEST / 18:46 ACST |
| GAME-STATE | **PREGAME** at cutoff |
| Target | `AFLW_JOINT_FINAL_SCORE-v1` |
| Endpoint | Final siren; home-and-away draw permitted |
| Decision set | `DS-P193-V01` |
| Dependence group | `DG-P193-JOINT-SCORE` |
| Method | MDS-2026.08.30-v2.7 qualitative champion |
| Probability state | `NOT_GENERATED / NOT_PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Operator terms | NOT SUPPLIED |

If first bounce occurs after the frozen cutoff but before delivery, no subsequent score, possession, injury or other live information is permitted to change this V01 ranking.

## Supplied contracts
1. Essendon +2.5
2. Richmond -2.5
3. Over 83.5 points
4. Under 83.5 points

## Current teams / availability

### Essendon
Confirmed changes:
- IN: Brooke Walker, Sophie Van De Heuvel
- OUT: Maddison Gay (shoulder), Chloe Adams (omitted)

Additional injury context:
- Maddison Gay: posterior shoulder subluxation, unavailable.
- Emma Dineen: back, unavailable.
- Brooke Brown: season-ending bone-stress injury.
- Daria Bannister and Amelia Radford remained on the injury list/test states.

Role impact:
Walker and Van De Heuvel restore defensive/transition options, but Gay's absence removes a current intercept/defensive piece. Essendon's back-half regime therefore improves in depth without becoming fully stable.

### Richmond
Confirmed change:
- IN: Georgia Stubs (AFLW debut)
- OUT: Maddie Shevlin (omitted)

Unavailable:
- Ellie McKenzie — arm, expected Round 4-5.
- Baia Pugh — high-grade ankle sprain, expected Round 4.

Richmond retains Monique Conti, Emelia Yassir, Poppy Kelly, Gabby Seymour, Katie Brennan, Olivia Wolmarans, Caitlin Greiser and Mackenzie Ford in its current structure.

## 2026 current process baseline

### Essendon — 0-2
Round 1: Brisbane 85, Essendon 37 — total 122.
- Brisbane restricted Essendon to four inside 50s in Q1.
- Repeated Brisbane forward-half pressure overwhelmed Essendon's defence.
- Essendon kicked 6.1: only seven scoring shots.

Round 2: Sydney 66, Essendon 42 — total 108.
- Essendon improved to 6.6: 12 scoring shots.
- Sophie Alexander kicked three.
- Maddy Prespakis, Amy Gaylor and Georgia Nanscawen remained important midfield contributors.

Interpretation:
Essendon's raw 0-2 record came against two strong/top-four-calibre opponents. The major concern is defensive shot suppression, not an inability to score at all.

### Richmond — 1-1
Round 1: Richmond 46, Collingwood 28 — total 74.
- Richmond won inside 50s 43-24.
- Won clearances 25-17, including centre clearances 10-2.
- Kicked 6.10 from 16 scoring shots: strong territorial/shot volume but inefficient conversion.

Round 2: Western Bulldogs 48, Richmond 37 — total 85.
- Richmond managed only eight inside 50s in the first half, its equal-lowest halftime figure on record.
- Finished 5.7 from 12 scoring shots.
- Conti: 26 disposals, six clearances, seven inside 50s.
- Wolmarans kicked three goals and has four goals across her first two games.

Interpretation:
Richmond's midfield/territory ceiling is real through Conti, but the non-Conti midfield and forward-entry chain remains less stable. The absence of Ellie McKenzie removes another high-value movement/contest pathway.

## Direct prior
2025 Round 3: Essendon 6.7 (43) defeated Richmond 3.10 (28), a 15-point Essendon win.

This is descriptive only; current coaches/personnel differ materially.

## Venue / weather
Darwin at the match window:
- approximately 30°C around 6:30pm,
- clear / 0% rain through 6:30-9:30pm,
- humid conditions around the 50% range,
- light-to-moderate evening wind.

Mechanism treatment:
Heat/humidity is not automatically Over or Under. It can:
- reduce repeated high-intensity running and clean disposal;
- increase late fatigue and defensive spacing;
- increase interchange/recovery dependence;
- create a late-scoring tail if one side's pressure/transition defence breaks down.

Both clubs prepared specifically for the Darwin heat, so no one-sided conditioning assumption is made.

## One coherent score tree

### Essendon-control / lower-total branch
Representative scores:
- Essendon 43-32
- Essendon 45-34
- Essendon 42-35

Mechanisms:
Prespakis/Gaylor/Nanscawen compete well at stoppage, Essendon's defensive inclusions improve transition defence, and Richmond struggles to convert territory.

Favours:
Essendon +2.5, Under 83.5.

### Central competitive branch
Representative scores:
- Essendon 44-40
- Essendon 45-41
- Richmond 43-41

Mechanisms:
Both sides generate roughly 11-14 scoring shots; neither fully controls field position. Richmond's Conti/Wolmarans pathway and Essendon's Prespakis/Toogood/Alexander pathway both remain functional.

Favours:
Essendon +2.5 strongly; total sits directly around the 83.5 boundary.

### Richmond territorial branch
Representative scores:
- Richmond 47-38
- Richmond 48-40
- Richmond 46-39

Mechanisms:
Conti wins repeat clearances/inside-50 supply, Essendon's defensive issues persist despite returning personnel, and Wolmarans/Brennan/Greiser convert enough entries.

Favours:
Richmond -2.5; Over becomes more live if Essendon still scores around 40.

### Heat/fatigue open branch
Representative scores:
- Essendon 50-43
- Richmond 49-42
- Essendon 48-45

Mechanisms:
late defensive spacing deteriorates, repeat entries produce higher-quality shots and both forward lines convert.

Favours:
Over 83.5.

## Frozen P-193/V01 ranking

| Rank | Contract | Verdict | Evidence | Core reason |
|---:|---|---|---|---|
| **1** | **Essendon +2.5** | **LEAN** | **MEDIUM** | Essendon has faced materially stronger opposition than Richmond, retains a credible midfield/forward scoring core, regains Walker and Van De Heuvel, and the +2.5 cushion wins on any Essendon victory or 1-2 point Richmond win. Richmond is without Ellie McKenzie and its Round 2 first-half entry creation was poor. |
| **2** | **Under 83.5** | **LEAN / THIN** | **MEDIUM-LOW** | Richmond has scored only 46 and 37 with 16 then 12 scoring shots; Essendon regains defensive personnel. A large part of Essendon's current high totals came from elite opponents generating 21-25 scoring shots, which Richmond has not yet shown consistently. |
| **3** | **Over 83.5** | **FORCED RANK / LIVE COUNTER-BRANCH** | **MEDIUM-LOW** | Essendon's games have reached 122 and 108, its defence remains vulnerable, and Darwin heat can create late fatigue/separation. But those totals were opponent-driven and 83.5 still requires Richmond to exploit Essendon's defence or both sides to convert efficiently. |
| **4** | **Richmond -2.5** | **FORCED RANK** | **MEDIUM-LOW** | Richmond's Conti/Wolmarans core and Essendon's 0-2 start create a real win-and-cover path, but -2.5 is less robust than the Essendon cushion given schedule strength, McKenzie's absence, Essendon's returning defenders and the 2025 matchup prior. |

## Potential winner
**Essendon — LEAN**

Primary mechanisms:
- tougher opening schedule than Richmond;
- Maddy Prespakis-led midfield can generate enough territory against a Richmond midfield overly dependent on Conti;
- Walker/Van De Heuvel improve current defensive/transition options;
- Toogood/Alexander give Essendon usable forward targets.

Strongest kill path:
Richmond wins the clearance/territory chain through Conti, Essendon remains unable to suppress repeated entries, and Wolmarans plus the experienced Richmond forwards convert the resulting shot volume.

## Final freeze
1. Essendon +2.5
2. Under 83.5
3. Over 83.5
4. Richmond -2.5

Potential winner: Essendon — LEAN.

No internal probabilities are generated or published. No value claim is made without same-time prices.

**Next canonical distinct event ID: P-194.**



---

# P-194 — FC St. Pauli vs 1. FC Kaiserslautern — Germany 2. Bundesliga

## Event / state freeze
- Competition: 2026/27 2. Bundesliga — Matchday 3
- Venue: Millerntor-Stadion, Hamburg
- Scheduled kickoff: 2026-08-30 13:30 CEST / 21:30 Australia/Melbourne
- Frozen cutoff: 2026-08-30 13:29:45 CEST / 21:29:45 Australia/Melbourne
- GAME-STATE: PREGAME
- Method: MDS-2026.08.30-v2.7 qualitative champion
- Goal target: SOCCER_REGULATION_JOINT_GOALS-v1
- Corner target: SOCCER_MATCH_CORNERS-STP-v1
- Probability state: NOT_GENERATED / NOT_PUBLISHED
- Value state: NO VALUE DETERMINABLE

No information first known after the frozen cutoff may change this V01 forecast.

## Decision set
1. 1H Over 0.5 goals
2. 1H Under 0.5 goals
3. FT Over 2.5 goals
4. FT Under 2.5 goals
5. Generated corner row: St. Pauli Over 5.5 team corners

Corner operator/provider terms were not supplied, so the corner row is capped at FORCED RANK / MEDIUM-LOW evidence.

## Current regime

### St. Pauli
- League: 1-1 vs Greuther Fürth; 2-2 at Holstein Kiel.
- Cup: lost 0-2 at Rot-Weiss Essen.
- Scored three league goals, conceded three.
- Current secondary near-kickoff lineups listed Hara and Kaars in attack with Hrgota behind.
- Ceesay was reported available for limited minutes after injury, but his exact matchday role was not field-owner confirmed at cutoff.

### Kaiserslautern
- League: 0-0 at Wolfsburg; 0-0 vs Karlsruhe.
- Cup: 0-0 after 90 at Waldhof, won 1-0 in extra time.
- Therefore three straight 0-0 first halves and three straight 0-0 regulation scorelines entering this match.
- Current secondary near-kickoff feeds listed Krahl in goal and a back three including Elvedi/Gyamfi/Jacob Rasmussen.

## Weather
DWD forecast around midday in Hamburg: roughly 20°C, light rain and gusty winds.
A local forecast also called for afternoon showers and strong southwesterly gusts.

Mechanism:
- may suppress clean crossing/finishing accuracy,
- but may increase blocks, clearances and deflections,
- therefore can support lower finishing without implying low corners.

## Goal-state tree
Lower/central:
- 0-0
- St. Pauli 1-0
- 1-1

Early-goal branch:
- HT 1-0, FT 1-0
- HT 1-0, FT 1-1
- HT 1-0, FT 2-0

Open tail:
- 2-1
- 2-2
- 3-1

## Corner process
Recent current corner evidence:
- St. Pauli: 9 vs Fürth, 5 at Kiel, 1 at RW Essen.
- Kaiserslautern conceded 9 at Wolfsburg and 11 vs Karlsruhe in the first two league matches.
- Current specialist long-window rates: St. Pauli ~5.6 corners for/game, Kaiserslautern ~6.4 conceded/game.
- Current published St. Pauli team-corner line: 5.5.
- Current match total-corner market: around 10.5.

Mechanism:
St. Pauli's wingback width through Pyrka/Oppie can create crosses, blocks and clearances against Kaiserslautern's compact back-three/wingback shape. Low goals and high corners can coexist.

## P-194/V01 ranking
1. **FT Under 2.5 goals — LEAN, MEDIUM**
2. **St. Pauli Over 5.5 corners — FORCED RANK, MEDIUM-LOW**
3. **1H Under 0.5 goals — LEAN / THIN, MEDIUM-LOW**
4. **1H Over 0.5 goals — FORCED RANK / counter-branch, MEDIUM-LOW**
5. **FT Over 2.5 goals — AVOID / FORCED RANK, MEDIUM-LOW**

## Potential winner
**FC St. Pauli — FORCED WINNER / LOW CONFIDENCE**

Why:
- home venue,
- more current attacking creation,
- three league goals versus FCK's zero,
- strong recent second-division H2H.

Why confidence stays low:
- St. Pauli remains winless this season,
- FCK has conceded zero in regulation across three competitive matches,
- the draw is a major central branch,
- final official XI was not field-owner verified before cutoff.

## Final freeze
1. Under 2.5 goals
2. St. Pauli Over 5.5 corners
3. 1H Under 0.5 goals
4. 1H Over 0.5 goals
5. Over 2.5 goals

Potential winner: FC St. Pauli — FORCED WINNER / LOW CONFIDENCE.

Next canonical distinct event ID: **P-195**.




---

# P-195 — KAA Gent vs Club Brugge — Belgium First Division A

## Event/state freeze

| Field | Frozen value |
|---|---|
| Competition | 2026/27 Jupiler Pro League — Matchday 4 |
| Event | KAA Gent vs Club Brugge |
| Venue | Planet Group Arena, Gent |
| Scheduled kickoff | 2026-08-30 13:30 CEST / 21:30 Australia/Melbourne |
| Forecast cutoff | ~2026-08-30 13:29 CEST / 21:29 Australia/Melbourne |
| GAME-STATE | PREGAME at final verified refresh; multiple current live pages still showed "Not started" / no score |
| Goal target | SOCCER_REGULATION_JOINT_GOALS-v1 |
| Corner target | SOCCER_TEAM_CORNERS_CLUB-v1 |
| Method | MDS-2026.08.30-v2.7 qualitative champion |
| Probability state | NOT_GENERATED / NOT_PUBLISHED |
| Value state | NO VALUE DETERMINABLE |

Final field-owner starting XIs were not independently verified at cutoff. Current secondary lineup feeds showed stable recent shapes, but those are treated as projected/secondary only.

## Decision set

User-supplied:
1. 1H Over 0.5 goals
2. 1H Under 0.5 goals
3. FT Over 2.5 goals
4. FT Under 2.5 goals

Generated corner row:
5. Club Brugge Over 5.5 team corners.

The corner threshold was current in published market/specialist pages, but the user's sportsbook/provider definition was not supplied, so the row is capped at FORCED RANK / MEDIUM-LOW evidence.

## Current regime

### KAA Gent
League:
- 2-0 vs KV Mechelen
- 2-1 at RAAL La Louvière
- 6 points from 2 games, 4 goals for, 1 against

First-half states:
- 2-0 HT vs Mechelen
- 1-1 HT at La Louvière

Europe:
- 0-0 vs Hibernian
- 3-2 win at Hibernian on Thursday 27 Aug to qualify for the Conference League league phase

Context:
Gent therefore enters on a short turnaround after a high-stakes away match in Edinburgh. This is not an automatic negative scalar; it specifically raises second-half rotation/fatigue uncertainty and may reduce sustained pressing/transition defence.

### Club Brugge
League:
- 3-0 vs Kortrijk
- 3-0 at OH Leuven
- 1-0 vs Cercle Brugge
- 9 points from 3 games, 7 goals for, 0 against

First-half scoring:
- Vetlesen 30' vs Kortrijk
- Diakhon 26' at OH Leuven
- Tresoldi 37' vs Cercle

Thus Club has scored before half-time in all three league matches and has yet to concede a league goal.

Recent stable attacking roles have included:
- Hans Vanaken
- Carlos Forbs
- Hugo Vetlesen
- Mamadou Diakhon
- Nicolò Tresoldi

Current exact XI remains secondary/projection-only at cutoff.

## Goal-process assessment

### Gent creation
Gent has scored in both league games and generated multiple first-half chances at home against Mechelen. The 2-0 opener was built through a stronger final 15 minutes of the first half.

### Club suppression
Club has three league clean sheets and has allowed little scoring despite playing both home and away. This materially strengthens the 1-0/2-0 Club branch and prevents a high-confidence full-game Over.

### Club attack
Club has scored 7 in 3 league games with goals from multiple roles. The early-scoring pattern has been stable enough to support 1H goal exposure without relying on one scorer.

## Weather
Current Ghent observations/forecasts:
- around 20-22°C,
- cloudy,
- SW winds roughly 10-20 mph,
- some forecast sources carried shower risk around the afternoon.

Mechanism:
wind/showers can reduce cross/shot precision but can also increase blocks, clearances and defensive errors. No automatic total direction is applied.

## Corner process

Current specialist long-window context:
- Gent around 4.5 team corners per league game; around 4.6 at home.
- Gent opponents around 5.0 corners overall and ~5.6 in Gent home matches.
- Club Brugge around 6.9 corners for per league match; ~6.1 away.
- Current Club Brugge team-corner line: 5.5.
- Current total-corner market: around 10.5.

Current concrete example:
Club won 6 corners against Kortrijk while holding 74-75% possession.

Mechanism:
Club's 4-2-3-1/wing-attacking structure, with wide threats and overlapping fullbacks, creates repeated crossing/end-line/block states. Gent's Thursday travel/short turnaround can increase late territorial defending even if it does not immediately create goals.

This is a separate corner process; low goals and high Club corner volume can coexist.

## Joint goal-state tree

### Club control / low total
Representative scores:
- Club 1-0
- Club 2-0
- 1-1

Favours:
- 1H Over remains live if Club scores early
- FT Under 2.5
- Club corner Over can still win through sustained territorial pressure

### Central attacking branch
Representative scores:
- Club 2-1
- Club 3-1
- 2-2

Favours:
- 1H Over 0.5
- FT Over 2.5
- Club corner Over

### Gent resistance branch
Representative scores:
- Gent 1-0
- 1-1
- Gent 2-1

Mechanisms:
Gent's home defensive organisation holds and Club's conversion regresses from its 3-0 starts.

Favours:
- 1H goal direction depends on first score timing
- Under is stronger in 1-0 / 1-1

### Fatigue/open second half
Representative scores:
- Club 3-1
- Club 3-2
- 2-2

Mechanism:
Gent's short turnaround affects transition defence and closing intensity after an initially competitive first half.

Favours:
- FT Over 2.5
- Club winner
- corners can remain elevated

## P-195/V01 ranking

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **1H Over 0.5 goals** | **LEAN** | **MEDIUM** |
| **2** | **Club Brugge Over 5.5 corners** | **FORCED RANK — derivative/provider cap** | **MEDIUM-LOW** |
| **3** | **FT Over 2.5 goals** | **LEAN / THIN** | **MEDIUM-LOW** |
| **4** | **FT Under 2.5 goals** | **FORCED RANK / strong counter-branch** | **MEDIUM-LOW** |
| **5** | **1H Under 0.5 goals** | **AVOID / FORCED RANK** | **MEDIUM-LOW** |

## Ranking logic

### Rank 1 — 1H Over 0.5
Club has scored before half-time in all three league matches; Gent's two league games have also both contained first-half goals. This is supported by actual opening-phase creation, not merely final-score streaks.

Main kill path:
Club's clean-sheet/control approach and Gent's short-turnaround caution produce a tactical 0-0 opening half.

### Rank 2 — Club Over 5.5 corners
Club's longer-window corner production sits above the 5.5 threshold, and Gent's opponent-conceded corner profile plus likely Club territorial advantage supports six-plus attempts. The row remains provider-capped because exact operator corner terms were not supplied.

### Rank 3 — FT Over 2.5
Club has scored 3, 3 and 1 in league play; Gent has scored in both league games and just played a 3-2 European match. The most important Over mechanism is an early goal forcing the losing side to increase attacking exposure.

Why only third:
Club's three league clean sheets preserve strong 1-0/2-0 branches, so an early first-half goal does not automatically imply 3+ final goals.

### Rank 4 — FT Under 2.5
The Under has legitimate score families: Club 1-0, Club 2-0, 1-1. Club's defensive regime is the strongest reason.

It ranks below the Over because Gent has scored in both league games, Club's attack has multiple current scoring routes, and Gent's Thursday European turnaround creates a plausible later separation/open-game branch.

### Rank 5 — 1H Under 0.5
This is directly opposed by the strongest current phase evidence: every Club league match and both Gent league matches have contained a first-half goal.

## Potential winner

**Club Brugge — LEAN**

Reasons:
- 3-0 league start with 7 scored and 0 conceded
- materially deeper, stable attacking structure
- Gent played a high-intensity European qualifier in Scotland only three days earlier
- current market/external baselines also favour Club, used only as corroboration

Counter-path:
Gent is 2-0 in league play, has home advantage, has conceded only once in the league, and can keep the game compressed if its defensive structure survives the early Club pressure.

## Final freeze

1. 1H Over 0.5 goals
2. Club Brugge Over 5.5 corners
3. FT Over 2.5 goals
4. FT Under 2.5 goals
5. 1H Under 0.5 goals

Potential winner: Club Brugge — LEAN.

Next canonical distinct event ID: **P-196**.


---

# P-196 — Egypt vs Congo DR — FIBA Basketball World Cup 2027 African Qualifiers

## Frozen state
- Venue: Dakar Arena, Dakar, Senegal.
- Scheduled tip: 2026-08-30 12:30 GMT / 22:30 Australia/Melbourne.
- Frozen cutoff: 2026-08-30 22:21 AEST / 12:21 GMT.
- GAME-STATE: PREGAME.
- Method: MDS-2026.08.30-v2.7 qualitative champion.
- Probability: NOT_GENERATED / NOT_PUBLISHED.
- Value: NO VALUE DETERMINABLE.

## Current evidence
Egypt official competition averages at final refresh: 77.4 PPG, 46.6 RPG, 16.9 APG, 50.8% 2PT, 26.7% 3PT, 55.7% FT.
DR Congo: 66.6 PPG, 39.4 RPG, 16.0 APG, 48.2% 2PT, 23.6% 3PT, 54.8% FT.

Current Window 4:
- Egypt beat Senegal 76-67 and lost to Côte d'Ivoire 72-66.
- DR Congo lost to Angola 100-68 and Mali 101-76.
- Against Angola, DR Congo committed 22 turnovers; Angola recorded 22 steals.
- Egypt's Senegal win included a 53-45 rebounding edge and 23 offensive rebounds.

Both teams have compressed turnaround. Egypt played Aug 29 at 12:30 Dakar time; DR Congo played at 15:30, leaving roughly 24 and 21 hours respectively before this game.

## Joint score tree
Central Egypt-control/Under states: 80-62, 82-64, 83-65.
Egypt-control/Over states: 86-68, 88-70, 90-66.
Competitive DR Congo cover states: 78-69, 80-70, 79-71.
Open DR Congo recovery states: 84-75, 86-74.

## P-196/V01 ranking
1. **Egypt -14.5 — LEAN, MEDIUM**
2. **Under 151.5 — LEAN / THIN, MEDIUM-LOW**
3. **DR Congo +14.5 — FORCED RANK / counter-branch, MEDIUM-LOW**
4. **Over 151.5 — FORCED RANK, MEDIUM-LOW**

### Why Egypt -14.5 ranks first
Egypt has the stronger current defensive/rebounding process and much better Window 4 results. DR Congo's recent turnover and defensive collapse creates a credible separation branch. The line is still large, and Egypt's poor perimeter/FT shooting can compress margins, so the grade remains LEAN rather than SUPPORTED.

### Why Under 151.5 ranks second
Egypt's current Window 4 totals are 143 and 138. Egypt's 77.4 PPG plus DR Congo's 66.6 PPG produces a descriptive 144-point baseline. The central state is Egypt winning through defensive suppression and second chances rather than pace. The main kill path is Egypt carrying the total after DR Congo allowed 100 and 101 in its last two games.

### Why DR Congo +14.5 ranks third
The cushion covers scores such as 78-69 or 80-70. If DR Congo protects the ball and limits Egyptian offensive rebounds, Egypt's weak 3PT/FT shooting can keep the margin inside 15. Current DR Congo process is too unstable to rank it above Egypt.

### Why Over 151.5 ranks fourth
The best Over route is Egypt carrying the total into an 86-68/88-70 type state. But Egypt itself scored only 76 and 66 in this window, while both teams' official perimeter and FT shooting are weak.

## Potential winner
**Egypt — LEAN.**

## Final freeze
1. Egypt -14.5
2. Under 151.5
3. DR Congo +14.5
4. Over 151.5

Potential winner: Egypt — LEAN.

Next canonical distinct event ID: **P-197**.




---

# P-197 — Feyenoord vs ADO Den Haag — Netherlands Eredivisie

## Event / state freeze

| Field | Frozen value |
|---|---|
| Competition | 2026/27 Eredivisie — Round 4 |
| Event | Feyenoord vs ADO Den Haag |
| Venue | De Kuip / Stadion Feijenoord, Rotterdam |
| Scheduled kickoff | 2026-08-30 14:30 CEST / 22:30 Australia/Melbourne |
| Frozen cutoff | 2026-08-30 14:26 CEST / 22:26 Australia/Melbourne |
| GAME-STATE | PREGAME |
| Goal target | `SOCCER_REGULATION_JOINT_GOALS-v1` |
| Corner target | `SOCCER_TEAM_CORNERS_FEY-v1` |
| Method | MDS-2026.08.30-v2.7 qualitative champion |
| Probability state | `NOT_GENERATED / NOT_PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Operator terms | NOT SUPPLIED |

Any information first known after the frozen cutoff is excluded from this V01 forecast.

## Decision set

User-supplied:
1. First-half Over 0.5 goals
2. First-half Under 0.5 goals
3. Full-time Over 2.5 goals
4. Full-time Under 2.5 goals

Generated corner row:
5. Feyenoord Under 7.5 team corners.

The 7.5 corner threshold was present in current published market/specialist pages, but the user's exact corner operator/provider definition was not supplied. The corner row is therefore capped at `FORCED RANK / MEDIUM-LOW`.

## Official / participant state

### Feyenoord — confirmed XI
Officially reported starting XI:
- Tjark Ernst
- Givairo Read
- Jeremiah St. Juste
- Tsuyoshi Watanabe
- Mika Mármol
- Oussama Targhalline
- Gjivai Zechiël
- Luciano Valente
- Anis Hadj Moussa
- Ayase Ueda
- Gaoussou Diarra

Key change:
- Targhalline starts in place of Charles Vanhoutte.

Current injury context from pregame reporting:
- Bart Nieuwkoop unavailable
- Gijs Smal unavailable
- Jordan Bos unavailable
- Thomas Beelen unavailable
- Jakub Moder unavailable

### ADO Den Haag
A field-owning confirmed XI was not independently retrievable at the frozen cutoff. Current secondary near-kickoff projections consistently centered on:
- Kilian Nikièma in goal
- Sylla / Hokke / Mulder or Waem-type defensive structure
- Juho Kilo in midfield
- Daryl van Mieghem wide
- Evan Rottier / Eduardo-type forward roles

Because the final field-owner XI was not verified, these names do not control any decisive participant-specific forecast mechanism.

Current injury reporting consistently listed Cameron Peupion unavailable and Donat Barany unavailable/doubtful, with Jalen Hawkins returning toward availability.

## Current league process

### Feyenoord — 2-1-0, 7 points
Results:
- Sparta Rotterdam 0-1 Feyenoord
- Feyenoord 2-2 Go Ahead Eagles
- Cambuur 2-5 Feyenoord

Goals:
- 8 scored
- 4 conceded

Recent process:
- vs Sparta: 22 shots, 6 on target, ~3.18 xG, 10 corners
- vs Go Ahead: 27 shots, 6 on target, ~2.8 xG, 6 corners
- vs Cambuur: 14 shots, 7 on target, ~2.6 xG, 3 corners

Interpretation:
Feyenoord's attacking creation has been consistently strong even when scoring output varied. The 1-0 Sparta result materially under-converted a large chance volume; the 5-2 Cambuur game represented the upper conversion branch.

### ADO Den Haag — 0-0-3, 0 points
Results:
- AZ 2-0 ADO
- ADO 1-4 Groningen
- Go Ahead Eagles 3-1 ADO

Goals:
- 2 scored
- 9 conceded

Process:
- vs AZ: ADO allowed ~2.7 xG and lost 2-0
- vs Groningen: allowed ~3.4 xG, 17 shots, 14 on target, lost 4-1
- vs Go Ahead: allowed only ~1.0 xG but still conceded three, while ADO generated ~1.0 xG

Interpretation:
ADO's defensive weakness is not only a final-score streak. Two of the three games contained high-quality opponent chance creation, while the Go Ahead match also demonstrates an ordinary finishing/goalkeeper/error tail can still produce multiple conceded goals without huge xG.

## First-half state

Feyenoord:
- vs Go Ahead: led 2-0 at halftime
- vs Cambuur: led 4-0 at halftime
- vs Sparta: lower-scoring/late-conversion branch

ADO:
- vs AZ: 0-0 at halftime
- vs Groningen: trailed 0-3 at halftime
- vs Go Ahead: trailed 0-2 at halftime

Thus four of the six current team-games contained at least one first-half goal, and the strongest current mismatch states have produced early opponent scoring against ADO.

## Weather

KNMI's afternoon forecast for the Netherlands called for showers, possible heavy bursts/thunder, temperatures around 20°C and gusty west/southwesterly winds.

No automatic Under is applied.

Mechanisms:
- wind/rain can reduce crossing/shot precision;
- can increase goalkeeper/defensive handling errors;
- can increase blocks and clearances;
- therefore it widens conversion/corner variance rather than forcing one total direction.

## Goal-state tree

### Feyenoord control / central Over
Representative scores:
- Feyenoord 3-0
- Feyenoord 3-1
- Feyenoord 4-0

Mechanisms:
- sustained shot/box-entry advantage
- ADO's defensive structure fails to suppress central/wide creation
- Ueda/Hadj Moussa/Diarra convert enough of Feyenoord's volume

Favours:
- FT Over 2.5
- 1H Over 0.5
- Feyenoord winner

### Feyenoord low-conversion control
Representative scores:
- Feyenoord 2-0
- Feyenoord 1-0

Mechanisms:
- Feyenoord dominates territory but finishing regresses
- ADO contributes little
- weather/wind reduces clean finishing

Favours:
- FT Under 2.5
- 1H direction depends on opener timing

### ADO contribution / open game
Representative scores:
- Feyenoord 3-1
- Feyenoord 4-1
- Feyenoord 3-2

Mechanisms:
- ADO creates transition chances after falling behind
- Feyenoord's defensive absences/rotation allow one goal
- score-state produces more open second-half football

Favours:
- FT Over 2.5

### Tactical / delayed-breakthrough branch
Representative scores:
- HT 0-0 -> FT Feyenoord 2-0
- HT 0-0 -> FT Feyenoord 1-0

Favours:
- 1H Under 0.5
- FT Under can survive

## Corner process

Current Feyenoord league corners:
- 10 at Sparta
- 6 vs Go Ahead
- 3 at Cambuur

Current specialist longer-window context:
- Feyenoord ~6.0 team corners per league game
- ADO opponents ~5.33 corners per game in the current market snapshot
- current Feyenoord team-corner line: 7.5
- specialist current market leaned slightly toward Under 7.5

Mechanism:
Feyenoord can dominate without needing eight corners, as shown by the five-goal Cambuur match with only three corners. If Feyenoord convert early, later attack can shift from sustained blocked-cross pressure to controlled possession and transition, reducing corner demand.

Kill path:
ADO defend extremely deep, repeatedly block crosses/shots and concede territory without conceding early, producing 8+ Feyenoord corners.

## P-197/V01 ranking

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **FT Over 2.5 goals** | **LEAN** | **MEDIUM** |
| **2** | **1H Over 0.5 goals** | **LEAN** | **MEDIUM** |
| **3** | **Feyenoord Under 7.5 corners** | **FORCED RANK — derivative/provider cap** | **MEDIUM-LOW** |
| **4** | **FT Under 2.5 goals** | **AVOID / FORCED RANK** | **MEDIUM-LOW** |
| **5** | **1H Under 0.5 goals** | **AVOID / FORCED RANK** | **MEDIUM-LOW** |

## Ranking logic

### Rank 1 — FT Over 2.5
Feyenoord have generated ~2.6-3.2 xG-quality attacking games in all three league matches and have scored five and two in the last two. ADO have conceded nine in three and allowed high-quality chance volume in two of them. The central 3-0 / 3-1 / 4-0 family clears the line without requiring ADO to score.

Main kill path:
Feyenoord again dominate but under-convert as against Sparta, creating a 1-0 / 2-0 result.

### Rank 2 — 1H Over 0.5
Feyenoord scored twice before halftime against Go Ahead and four before halftime at Cambuur. ADO conceded three first-half goals to Groningen and two to Go Ahead. The strongest current mismatch branch therefore includes an early Feyenoord breakthrough.

Why below full Over:
one delayed breakthrough can still produce a 3-0 second-half separation while losing the first-half Over.

### Rank 3 — Feyenoord Under 7.5 corners
Feyenoord's own current league distribution is 10 / 6 / 3 and the currently published line is 7.5. The attack does not require huge corner volume to score, and an early lead can lower later corner demand.

The exact corner provider/operator is unresolved, so this remains FORCED RANK.

### Rank 4 — FT Under 2.5
The best Under states are 1-0 and 2-0 Feyenoord. The Sparta opener proves Feyenoord can create heavily without finishing.

It ranks below the Over because ADO's defensive regime has allowed nine goals and Feyenoord's current chance creation is consistently high.

### Rank 5 — 1H Under 0.5
This requires ADO to survive the opening 45 without conceding and not score themselves. AZ achieved the first part, but Groningen and Go Ahead did not, while Feyenoord's last two matches both contained multiple first-half goals.

## Potential winner

**Feyenoord — LEAN**

Primary reasons:
- 7 points from 3 vs ADO's 0
- consistently strong current chance creation
- confirmed front three of Hadj Moussa, Ueda and Diarra
- ADO have conceded nine goals and multiple high-xG performances
- De Kuip home advantage

Why not stronger:
- Feyenoord still have defensive injuries
- confirmed ADO XI was not independently field-owner verified
- Feyenoord's Sparta game demonstrated major under-conversion is possible

## Final freeze

1. FT Over 2.5 goals
2. 1H Over 0.5 goals
3. Feyenoord Under 7.5 corners
4. FT Under 2.5 goals
5. 1H Under 0.5 goals

Potential winner: Feyenoord — LEAN.

Next canonical distinct event ID: **P-198**.




---

# P-198 — Poland vs Germany — FIBA Basketball World Cup 2027 European Qualifiers

## Event / state freeze

| Field | Frozen value |
|---|---|
| Competition | FIBA Basketball World Cup 2027 European Qualifiers — Second Round, Group K |
| Event | Poland vs Germany |
| Venue | ERGO Arena, Gdansk, Poland |
| Scheduled tip | 2026-08-30 12:45 UTC / 14:45 CEST / 22:45 Australia/Melbourne |
| Frozen cutoff | 2026-08-30 12:34 UTC / 22:34 Australia/Melbourne |
| GAME-STATE | **PREGAME** |
| Target | `BASKETBALL_JOINT_FINAL_SCORE-v1` |
| Method | MDS-2026.08.30-v2.7 qualitative champion |
| Operator terms | NOT SUPPLIED |
| Probability state | `NOT_GENERATED / NOT_PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |

The official FIBA game page remained without a live score at the frozen cutoff.

The interrupted Netherlands-Croatia request was not issued or logged, so it does not consume a canonical event ID.

## Confirmed rosters

### Poland
Aleksander Balcerowski, Kamil Laczynski, Jordan Loyd, Igor Milicic, Dominik Olejniczak, Kuba Pisla, Andrzej Pluta, Mateusz Ponitka, Michal Sokolowski, Szymon Zapala, Przemyslaw Zolnierewicz, Jaroslaw Zyskowski.

Important current-regime note:
- Jerrick Harding was on Poland's preliminary Window 4 list and remains prominent in broader qualifier averages, but **is not in the confirmed 12 for Germany**.
- Poland therefore retains Ponitka/Loyd/Balcerowski but loses one major scoring/creation route relative to the broader statistical baseline.

### Germany
Isaac Bonga, Kay Bruhnke, Oscar da Silva, Tristan da Silva, Malte Delow, David Kramer, Maodo Lo, Kostja Mushidi, Louis Olinde, Dennis Schroder, Daniel Theis, Johannes Thiemann.

Important current-regime note:
- Germany retains an exceptionally strong senior core: Schroder, Theis, Bonga, Oscar and Tristan da Silva, Lo and Thiemann.
- The Aug. 30 confirmed roster includes Theis and excludes Nelson Weidemann from the Aug. 27 12.

Starting fives were not yet field-owner confirmed at the cutoff, so exact opening minute allocations remain a mixture rather than fact.

## Current competition state

Group K entering the game:
- Poland: 7-0, +110 point differential
- Germany: 6-1, +90

Official FIBA team comparison:
- Poland: 96.0 PPG, 41.1 RPG, 21.1 APG, 59.8% 2PT, 37.2% 3PT, 79.7% FT
- Germany: 93.3 PPG, 41.7 RPG, 20.0 APG, 58.0% 2PT, 34.4% 3PT, 80.5% FT

Window 4 openers:
- Poland beat Israel 106-86
- Germany beat Netherlands 99-83

Poland's Israel win involved a major shooting ceiling:
- 60% FG
- 67.7% 2PT
- 50% 3PT
- led essentially wire-to-wire

Germany's current regime:
- defending world champions
- Schroder has produced 20+ points and 5+ assists in each of his last three World Cup Qualifier appearances
- Germany scored 99 against Netherlands in the current window

Home context:
- Poland have won 10 of their last 12 World Cup Qualifier home games, including the latest five.
- Their last home qualifier defeat was Germany 72-69 in November 2021.

## Joint possession / efficiency tree

### Competitive Germany win / Poland cover
Representative scores:
- Germany 94-90
- Germany 96-91
- Germany 92-88

Mechanisms:
- Germany's superior top-end roster controls late half-court execution.
- Poland's Ponitka/Loyd creation and home environment prevent large separation.
- Both teams generate efficient interior and free-throw scoring.

Favours:
- Poland +8.5
- Over 180.5 in 94-90 / 96-91 states
- Germany winner

### Poland home-control branch
Representative scores:
- Poland 94-90
- Poland 97-92
- Poland 91-88

Mechanisms:
- Ponitka/Loyd attack Germany's switches successfully.
- Poland maintains strong defensive rebounding and home-shot confidence.
- Germany's perimeter shooting remains ordinary.

Favours:
- Poland +8.5
- winner flips to Poland
- total near/above line depending pace

### Germany separation branch
Representative scores:
- Germany 99-88
- Germany 101-89
- Germany 98-86

Mechanisms:
- Schroder repeatedly creates paint collapse.
- Theis/Bonga/da Silva win interior/rebounding matchups.
- Harding's absence reduces Poland's secondary scoring.
- Germany's second unit sustains separation.

Favours:
- Germany -8.5
- usually Over 180.5 except lower Poland-output branch

### Lower-efficiency / Under branch
Representative scores:
- Germany 90-86
- Germany 92-84
- Poland 90-87

Mechanisms:
- Poland's 106-point shooting regresses sharply without Harding.
- Germany defends the point of attack and limits transition.
- both teams play more playoff-like half-court possessions in a top-three Group K matchup.

Favours:
- Poland +8.5
- Under 180.5

## P-198/V01 ranking

| Rank | Contract | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Poland +8.5** | **LEAN** | **MEDIUM** |
| **2** | **Over 180.5** | **LEAN / THIN** | **MEDIUM-LOW** |
| **3** | **Under 180.5** | **FORCED RANK / strong counter-branch** | **MEDIUM-LOW** |
| **4** | **Germany -8.5** | **FORCED RANK** | **MEDIUM-LOW** |

## Ranking logic

### #1 Poland +8.5
Poland is 7-0, owns a +110 differential and strong World Cup Qualifier home record. Germany has the stronger top-end roster and is the slight outright winner lean, but an 8.5-point road margin requires genuine separation rather than just late-game superiority.

The cushion covers:
- any Poland win
- Germany wins by 1-8

Central Germany 94-90 / 96-91 type states therefore favour the Poland handicap even while Germany remains the winner lean.

Main kill path:
Harding's absence materially reduces Poland's secondary creation, Germany dominates the interior/transition phases, and the full German roster turns a close first half into a double-digit second-half margin.

### #2 Over 180.5
Official competition scoring averages sum to about 189.3 points. The current Window 4 openers totaled:
- Poland-Israel: 192
- Germany-Netherlands: 182

Both teams possess strong interior efficiency and multiple late-clock creators. Germany's full roster adds high-end shot creation and finishing.

Why only thin:
180.5 is already a very high threshold, Poland's 106 against Israel came with 60% overall and 50% three-point shooting, and Harding is absent from the confirmed Poland 12. A more tactical 90-86 / 92-84 game is credible.

### #3 Under 180.5
The Under has a strong ordinary counter-path because:
- Poland's recent shooting can regress;
- Harding is absent;
- this is a direct top-three Group K matchup where both sides may reduce transition risk;
- Germany has the personnel to defend point-of-attack and switch more effectively than Poland's recent opponents.

It ranks below the Over because both teams' competition scoring profiles are already in the 90s and Germany's current roster is extremely strong offensively.

### #4 Germany -8.5
Germany is the more talented roster on paper and has won the last three major senior meetings with Poland, including 93-83 and 82-69 in 2022.

However, those H2Hs are old and cannot control the current game. Poland is unbeaten in the current qualification cycle and has a strong home record. Germany -8.5 needs a double-digit-type road separation, which is less robust than Poland's +8.5 cushion.

## Potential winner

**Germany — LEAN**

Reasons:
- stronger top-end roster and NBA/EuroLeague creation
- Schroder in elite current qualifier form
- Theis/Bonga/da Silva frontcourt/defensive flexibility
- Harding absent for Poland

Why only a lean:
- Poland is 7-0
- Poland has +110 point differential
- home qualifier record is strong
- Ponitka and Loyd provide enough late-game creation to win or keep the game one-possession

## Final freeze

1. Poland +8.5
2. Over 180.5
3. Under 180.5
4. Germany -8.5

Potential winner: Germany — LEAN.

Central corridor: Germany 94-90 / 96-91, with Poland 94-90 and Germany 99-88 as important adjacent branches.

Next canonical distinct event ID: **P-199**.




---

# P-199 — Frederikshavn White Hawks vs Sønderjyske — Danish Metal Ligaen

## Event/state freeze

| Field | Frozen value |
|---|---|
| Competition | 2026/27 Danish Metal Ligaen |
| Event | Frederikshavn White Hawks vs Sønderjyske |
| Venue | Nordjyske Bank Arena, Frederikshavn |
| Scheduled puck drop | 2026-08-30 15:00 CEST / 23:00 Australia/Melbourne |
| Frozen cutoff | ~2026-08-30 14:46 CEST / 22:46 Australia/Melbourne |
| GAME-STATE | **PREGAME** |
| Regulation target | `ICE_HOCKEY_REGULATION_JOINT_GOALS-v1` |
| Match-result target | linked full-match winner state including OT/SO under working market assumption |
| Method | MDS-2026.08.30-v2.7 qualitative champion |
| Probability state | `NOT_GENERATED / NOT_PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Operator terms | NOT SUPPLIED |

### Contract-definition assumption
The user's interface labels the side market as **ML**. This card treats ML as **match winner including overtime/shootout**, consistent with currently published matching-event markets from multiple operators. The 6.5 total is treated as a full-match total including OT/SO under the same working assumption.

If the user's actual operator uses regulation-only settlement or a different shootout-goal convention, settlement must be remapped before grading.

## Supplied candidate slate

1. Frederikshavn White Hawks ML
2. Sønderjyske ML
3. Over 6.5 goals
4. Under 6.5 goals

## Participant / roster state

### Frederikshavn
Current rebuild:
- new head coach Casper Stockfisch
- new goalie group led by Lukáš Pařík, with Marcus Bjørn and Magnus Johnsen
- new/import attack includes Atte Karppinen, Leo Ring, Frank Gymer and Aleksi Halme
- Louie Roehl and Gustav Nielsen strengthen the blue line
- Christopher Frederiksen, Christopher Rübenach, Albert Schioldan and other established Danish forwards add depth

The league preview before opening night described Frederikshavn as having almost the full squad available.

**Starting goalie:** NOT OFFICIALLY CONFIRMED in accessible field-owning sources at cutoff. Pařík is the projected/roster lead, but no starter is invented.

### Sønderjyske
Current rebuild:
- goalie tandem Thomas Lillie / William Rørth
- Alexander Ytterell is captain
- Eric Florchuk is cleared to play
- Raimonds Vitolins was added as a two-way center/special-teams option
- Marcus Almquist, Mathias Borring, Frederik Bjerrum and others provide Danish scoring/experience
- Jarid Lukosevicius was cleared administratively but was reported injured for the opener
- Albert Grossmann remains a long-term shoulder absence

**Starting goalie:** NOT OFFICIALLY CONFIRMED at cutoff. Lillie started the opener; Rørth remains a plausible short-turnaround branch.

## Current season evidence

### Frederikshavn opener
Lost 4-3 to Aalborg:
- trailed 2-0 after the first period
- recovered to 3-2 by late second-period sequence before Aalborg re-separated
- scorers included Jesper Bank Olesen, Aleksi Halme and Christopher Rübenach
- the Finnish/new-look attack showed credible scoring ability
- Aalborg's opening goals included a power-play goal and a shorthanded goal, showing special-teams/turnover exposure in the White Hawks upper-concession branch

Preseason current-regime examples:
- lost 4-3 to Aalborg
- beat Aalborg 3-1 in the return test
- beat HC Dalen 5-3

### Sønderjyske opener
Lost 2-1 to Odense:
- periods: 0-1, 1-1, 0-0
- Thomas Lillie started in goal
- Sønderjyske pushed very hard in the third period
- the low score was partly driven by a standout Emil Zetterquist performance for Odense, so 1 goal cannot be treated as Sønderjyske's stable offensive rate

Current preseason examples:
- beat Herlev 4-3 after shootout
- lost 5-1 to Esbjerg while still missing some imports
- later beat Esbjerg 3-1 in the general rehearsal

## Rest / travel

Both teams played Friday, Aug. 28.

- Frederikshavn remains at home and has no meaningful travel transition.
- Sønderjyske travels from Vojens to Frederikshavn on the same short recovery window.

Mechanistic interpretation:
- fatigue can increase defensive mistakes, penalties and late breakdowns;
- but it can also lower forecheck intensity and shooting quality;
- goalie rotation becomes more plausible on short turnaround.

Therefore rest is treated as a variance-widening branch rather than an automatic Over.

## Goal / conversion tree

### Low-conversion / goalie-control branch
Representative regulation scores:
- Sønderjyske 2-1
- Sønderjyske 3-2
- Frederikshavn 3-2

Mechanisms:
- both teams generate enough attempts but finishing stays ordinary
- goalie play is stable
- Sønderjyske's opener-like defensive structure persists
- Frederikshavn avoids the special-teams mistakes that hurt against Aalborg

Favours:
- **Under 6.5**
- either ML remains live

### Sønderjyske control branch
Representative scores:
- Sønderjyske 3-1
- Sønderjyske 4-2
- Sønderjyske 3-2

Mechanisms:
- Sønderjyske's deeper current center/defensive structure suppresses Frederikshavn's transition
- Florchuk/Vitolins/Ytterell help stabilize possession and special teams
- Frederikshavn's rebuilt lines remain less settled under pressure

Favours:
- **Sønderjyske ML**
- often **Under 6.5**

### Frederikshavn home-offence branch
Representative scores:
- Frederikshavn 3-2
- Frederikshavn 4-2
- Frederikshavn 4-3

Mechanisms:
- Halme/Ring/Karppinen/Rübenach convert the pace created by White Hawks' skating game
- Sønderjyske's road/short-rest depth is exposed
- home ice helps Frederikshavn sustain offensive-zone pressure

Favours:
- **Frederikshavn ML**
- Under at 3-2 / 4-2; Over at 4-3

### Open / special-teams / empty-net branch
Representative scores:
- Sønderjyske 4-3
- Frederikshavn 4-3
- 4-4 regulation, then OT/SO-decided

Mechanisms:
- penalties or short-handed chances create high-value scoring
- unresolved goalie mixture lands in a weaker-saving branch
- trailing team increases attempt volume
- empty-net or overtime adds the seventh goal

Favours:
- **Over 6.5**

### Critical OT geometry
The 2026/27 Metal Ligaen introduced a 3-on-3 overtime "No Return Rule": a team controlling the puck in the offensive zone cannot simply retreat it back over the blue line without consequence.

This makes a 3-3 regulation state important:
- regulation total = 6
- an OT winner can turn the full-match score representation into 4-3 = 7 under operators that count the OT goal
- therefore OT is an explicit Under kill path if the user's total includes OT/SO.

## P-199/V01 frozen ranking

| Rank | Contract | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Under 6.5 goals** | **LEAN / THIN** | **MEDIUM-LOW** |
| **2** | **Sønderjyske ML** | **LEAN / THIN** | **MEDIUM-LOW** |
| **3** | **Frederikshavn White Hawks ML** | **FORCED RANK / strong counter-branch** | **MEDIUM-LOW** |
| **4** | **Over 6.5 goals** | **FORCED RANK** | **MEDIUM-LOW** |

## Ranking logic

### #1 Under 6.5
The total requires seven goals to lose. Sønderjyske's opener finished with only three and featured long stretches of defensive structure plus strong late pressure without conversion. Frederikshavn's 4-3 opener demonstrates the kill path, but one goal came on the power play and another Aalborg goal was shorthanded, making special-teams events part of the upper tail rather than a clean five-on-five baseline.

The most central score family is 3-2 / 4-2 / 3-1 rather than 4-3 / 5-3.

Confidence is capped because:
- neither starting goalie was officially confirmed;
- Frederikshavn has shown a genuine 3-4 goal offensive ceiling;
- a 3-3 game plus OT can push a full-match total from six to seven.

### #2 Sønderjyske ML
Sønderjyske gets the narrow winner edge because its opener showed a stronger defensive-control state than the final 1-2 score suggests: it pressed hard in the third and was repeatedly denied by a standout opposing goalie. Florchuk is now available, Vitolins is integrated, and the roster has more current two-way center/defensive depth than it had early in camp.

However, this is a low-confidence side:
- Sønderjyske is also 0-1;
- roster reconstruction remains significant;
- White Hawks have home ice and no travel;
- Frederikshavn scored three against a strong Aalborg lineup.

### #3 Frederikshavn ML
White Hawks have the stronger home and current offensive counter-case:
- three goals against Aalborg on opening night
- a deeper rebuilt forward group
- nearly full availability entering the season
- no travel on the short turnaround

The side ranks below Sønderjyske because Frederikshavn still showed transition/special-teams mistakes and its current defensive/goalie regime is less proven.

### #4 Over 6.5
The Over requires a more specific high-conversion branch:
- goalie weakness/rotation
- special-teams scoring
- clustered finishing
- empty-net/OT seventh goal

Frederikshavn's 4-3 opener and 5-3 preseason win show the ceiling is real, so this is not dismissed. But with current goalie identities unresolved and Sønderjyske just producing a 2-1 game, the framework's sparse-competition conversion cap prevents recent goal totals from overriding the low-conversion branch.

## Potential winner

**Sønderjyske — LEAN / LOW CONFIDENCE**

Primary reasons:
- stronger defensive-control evidence from the opener than the 1-2 result alone suggests
- Eric Florchuk available
- Raimonds Vitolins gives a current two-way center/special-teams reinforcement
- Ytterell adds experience to the back end
- external current market pricing generally leans Sønderjyske, used only as a challenger/corroboration source

Strongest kill path:
Frederikshavn's skating/forecheck game converts home-zone pressure early, the new Finnish forwards continue the attacking form shown against Aalborg, and Sønderjyske's short turnaround/road travel exposes its still-rebuilt depth.

## External-market cross-check

A current matching-event market snapshot had Under 6.5 materially shorter than Over 6.5 and Sønderjyske favored on the moneyline. Other operators showed a much closer winner market.

This is used only as an external challenger/sanity check. It is **not** an internal model probability, and without the user's exact same-time odds there is no value claim.

## Final freeze

1. **Under 6.5 goals**
2. **Sønderjyske ML**
3. **Frederikshavn White Hawks ML**
4. **Over 6.5 goals**

Potential winner: **Sønderjyske — LEAN / LOW CONFIDENCE**.

Central score corridor: Sønderjyske 3-2 / 4-2, Frederikshavn 3-2 counterbranch.

Next canonical distinct event ID: **P-200**.




---

# P-200 — Herning Blue Fox vs Rungsted Seier Capital — Danish Metal Ligaen

## Event/state freeze

| Field | Frozen value |
|---|---|
| Competition | 2026/27 Danish Metal Ligaen |
| Event | Herning Blue Fox vs Rungsted Seier Capital |
| Venue | Kvik Hockey Arena, Herning |
| Scheduled puck drop | 2026-08-30 15:00 CEST / 23:00 Australia/Melbourne |
| Frozen cutoff | ~2026-08-30 14:49 CEST / 22:49 Australia/Melbourne |
| GAME-STATE | **PREGAME** |
| Regulation target | `ICE_HOCKEY_REGULATION_JOINT_GOALS-v1` |
| Match-result target | linked full-match result with OT/SO branch |
| Method | MDS-2026.08.30-v2.7 qualitative champion |
| Probability state | `NOT_GENERATED / NOT_PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Operator terms | NOT SUPPLIED |

## Contract-definition issue

The user's interface did not identify its operator or action terms.

A current matching-event Stake market labels:
- handicap as including overtime/shootout;
- total as including overtime/shootout.

A different matching-event operator page lists:
- handicap and total as regulation-time markets.

Therefore the exact operator endpoint is **unresolved**. This V01 ranking uses the working assumption that the supplied interface is **full match including OT/SO**, while preserving a regulation-only comparison branch. Settlement must be remapped if the actual operator uses regulation-only rules.

## Supplied candidate slate

1. Herning Blue Fox -2.5
2. Rungsted Seier Capital +2.5
3. Over 6.5 goals
4. Under 6.5 goals

## Current participant / goalie state

### Herning Blue Fox
- defending 2025/26 Danish champions
- no confirmed absences were reported in the official league preview before the opener
- current goalie tandem: Janis Fecers and George Sørensen
- starting goalie for P-200 was **NOT OFFICIALLY CONFIRMED** in accessible field-owning sources at cutoff
- current offensive group includes Morten Poulsen, Mathias Bau, Oliver Kiljunen, Anton Linde, Phillip Schultz, Kevin O'Neil, Lukas Bang, Jared Dmytriw and others
- Herning's structure is built around four-line pressure and substantial depth

### Rungsted Seier Capital
This is Rungsted's **first official league game** of 2026/27; its club schedule begins the regular season at Herning on Aug. 30.

Current roster construction includes:
- Filips Buncis
- Bryce Kindopp
- Olle Liss
- Gustav Olhaver
- Ludvig Elvenes
- Filip Karlsson
- Valdemar Ahlberg
- Dennis Fröland
- Tim Welin
- young Danish depth
- goalie tandem David Grubak / Tobias Vilykke

Rungsted lost high-impact offensive defenceman Morten Jensen during the offseason.

Starting goalie and final import activation were **NOT OFFICIALLY CONFIRMED** in accessible field-owning sources at cutoff. Kindopp had missed earlier preseason action while waiting on work permission, so he is not assumed active merely from appearing on the roster page.

## Current competitive / preseason state

### Herning
Opening league game:
- beat Esbjerg **7-1**
- period scores 2-0, 4-0, 1-1
- Mathias Bau and Morten Poulsen each had three assists
- Oliver Kiljunen and Anton Linde each scored twice
- official report emphasized that Herning punished Esbjerg's lack of discipline in the second period

Preseason against Esbjerg:
- lost 1-0 away
- won 5-0 at home

Interpretation:
Herning has both a high-conversion/separation branch and a low-conversion control branch. The 7-1 opener cannot be treated as the permanent scoring rate, but the depth and multi-line scoring are real.

### Rungsted
Official club preseason results:
- lost 5-2 vs Herlev
- lost 5-2 at Karlskrona
- won 3-2 after shootout at Herlev
- Aug. 27 at Rødovre listed without a result on the club page

Important context:
- early preseason lineups were incomplete
- Kindopp and Tim Daly were absent from an early Herlev test due work-permit issues
- Olle Liss joined only Aug. 24
- Dennis Fröland and other new additions improve the current roster relative to those early losses

Therefore preseason defensive concessions are informative about the risk branch but are not a complete current-team baseline.

## Historical same-opponent mechanism

Herning dominated the 2025/26 matchup:
- Herning won the first nine meetings of that season before Rungsted finally won the tenth.
- 2026 semifinal examples:
  - Herning 5-3 Rungsted
  - Rungsted 2-6 Herning
  - Herning 6-2 Rungsted
  - Rungsted 6-4 Herning
- the first four semifinal games produced 34 total goals, 8.5 per game.

These are **descriptive prior/mechanism evidence only** because both rosters changed materially.

The useful durable mechanism is Herning's ability to roll four lines, create rapid early separation and punish Rungsted special-teams/defensive breakdowns. The old raw goal average is not transferred as a current coefficient.

## Joint regulation/full-match goal tree

### Herning separation + Over branch
Representative scores:
- Herning 5-2
- Herning 6-2
- Herning 6-1

Mechanisms:
- four-line pressure creates sustained offensive-zone time
- Rungsted's still-new defensive structure struggles under forecheck
- Herning's power play / special-teams conversion remains efficient
- Rungsted contributes one or two goals through its improved scoring imports

Favours:
- **Herning -2.5**
- **Over 6.5**

### Herning separation + Under branch
Representative scores:
- Herning 4-1
- Herning 5-1
- Herning 4-2

Mechanisms:
- Herning controls territory and suppresses Rungsted
- Rungsted's goalie prevents a 6+ Herning total
- Rungsted's offence remains low

Favours:
- Herning -2.5 at 4-1 / 5-1
- Rungsted +2.5 at exactly 4-2
- **Under 6.5**

### Competitive Rungsted branch
Representative scores:
- Herning 4-3
- Herning 3-2
- Rungsted 3-2

Mechanisms:
- Rungsted's new scoring imports integrate quickly
- Grubak/Vilykke provides strong goaltending
- Herning converts below the 7-1 opener level
- discipline stays even and limits special-teams separation

Favours:
- **Rungsted +2.5**
- total depends on 4-3 vs 3-2

### 3-3 regulation / OT branch
Under full-match including OT:
- 3-3 regulation becomes 4-3 after an OT goal, reaching **7 total goals**
- both ±2.5 spread branches resolve in favor of Rungsted +2.5 in a one-goal game

This is a meaningful Over + underdog-cushion tail.

## P-200/V01 frozen ranking

| Rank | Contract | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Herning Blue Fox -2.5** | **LEAN** | **MEDIUM** |
| **2** | **Over 6.5 goals** | **LEAN / THIN** | **MEDIUM-LOW** |
| **3** | **Rungsted Seier Capital +2.5** | **FORCED RANK / strong counter-branch** | **MEDIUM-LOW** |
| **4** | **Under 6.5 goals** | **FORCED RANK** | **MEDIUM-LOW** |

## Ranking logic

### #1 Herning -2.5
Herning is the defending champion, opened 7-1, carries materially deeper four-line scoring and has repeatedly shown a 3+ goal separation mechanism against Rungsted. Rungsted enters its first official game with meaningful roster turnover and unresolved goalie/import activation.

The spread is still demanding. A Herning 4-2 win loses -2.5, and the rebuilt Rungsted offence is stronger on paper than its early preseason version. This remains LEAN rather than SUPPORTED.

Main kill path:
Rungsted's new imports are fully active, its goalie produces a strong road start, and Herning's 7-1 shooting/special-teams conversion regresses into a 4-2 / 4-3 / 3-2 game.

### #2 Over 6.5
The strongest Over mechanism does not require a balanced shootout:
- Herning can carry five or six goals itself;
- Rungsted's preseason defensive structure conceded five twice;
- the last playoff series repeatedly produced 8+ totals;
- Herning's current opener immediately showed multi-line and special-teams scoring.

Why only thin:
- Herning's preseason also contained 1-0 and 5-0 games;
- starting goalies are unconfirmed;
- the current Rungsted roster is materially different from early preseason and the spring playoff series;
- a 4-1 / 5-1 / 4-2 Herning control game stays Under.

### #3 Rungsted +2.5
This line has broad geometry:
- any Rungsted win covers;
- any Herning win by one or two covers;
- any OT/SO one-goal result covers under the full-match assumption.

Rungsted also added genuine offence through Olle Liss, Bryce Kindopp and other imports and retains capable goaltending options.

It ranks below Herning -2.5 because Herning's current depth, home environment and separation history make the ordinary blowout branch too important to ignore.

### #4 Under 6.5
The Under has credible 4-1, 5-1, 4-2 and 3-2 states and would become more attractive if a strong goalie pairing is confirmed.

It ranks fourth because the current evidence contains multiple independent upper-tail mechanisms:
- Herning's 7-1 opener;
- Rungsted's defensive preseason concessions;
- strong Herning special teams;
- historically open Herning-Rungsted matchups;
- and a 3-3 regulation state can become seven goals in OT under full-match total rules.

## Potential winner

**Herning Blue Fox — LEAN**

This is a substantially stronger directional winner view than the -2.5 spread itself.

Primary reasons:
- defending champions
- deep four-line roster
- 7-1 opening win
- home ice
- Rungsted's first official match and roster integration uncertainty
- strong historical matchup control

Strongest kill path:
Rungsted's newly added scoring talent is fully activated, the goalie wins the shot-quality battle, and Herning's opener proves to be a conversion/special-teams ceiling rather than its immediate central level.

## External-market cross-check

Current matching-event markets generally make Herning a very strong outright favorite.

One current market snapshot:
- Herning full-match winner 1.17
- Rungsted 4.40
- Over 6.5 1.70
- Under 6.5 2.04
- Herning -2.5 1.90
- Rungsted +2.5 1.81

Another operator's regulation market was closer on the -2.5 line and priced Under 6.5 slightly shorter than Over.

This disagreement is treated as an external challenger and reinforces the contract-definition caution. It is not an internal probability or value claim.

## Final freeze

1. **Herning Blue Fox -2.5**
2. **Over 6.5 goals**
3. **Rungsted Seier Capital +2.5**
4. **Under 6.5 goals**

Potential winner: **Herning Blue Fox — LEAN**.

Central score corridor:
- Herning 5-2
- Herning 5-1
- Herning 4-2

Upper tail:
- Herning 6-2 / 6-1

Competitive counterbranch:
- Herning 4-3 / 3-2

Next canonical distinct event ID: **P-201**.




---

# P-201 — SC Freiburg vs Werder Bremen — Germany Bundesliga

## Event/state freeze

| Field | Frozen value |
|---|---|
| Competition | 2026/27 Bundesliga — Matchday 1 |
| Event | SC Freiburg vs SV Werder Bremen |
| Venue | Europa-Park Stadion, Freiburg im Breisgau |
| Scheduled kickoff | 2026-08-30 15:30 CEST / 23:30 Australia/Melbourne |
| Frozen cutoff | 2026-08-30 ~15:21 CEST / 23:21 Australia/Melbourne |
| GAME-STATE | **PREGAME** |
| Goal target | `SOCCER_REGULATION_JOINT_GOALS-v1` |
| Corner target | `SOCCER_MATCH_CORNERS-v1` |
| Team-goal target | `SOCCER_TEAM_GOALS_SCF-v1` |
| Method | MDS-2026.08.30-v2.7 qualitative champion |
| Probability state | `NOT_GENERATED / NOT_PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Operator terms | NOT SUPPLIED |

Any information first known after the frozen cutoff is excluded from P-201/V01.

## Candidate slate

User-defined market families:
- 1H goals O/U 0.5
- FT goals O/U 2.5
- corner market — line generated from current evidence
- team-specific goals — line generated from current evidence

Generated derivative lines:
- **Total Corners Under 10.5**
- **Freiburg Team Total Over 1.5 Goals**

Top-five ranking is taken across this candidate family.  
The omitted sixth direction is **1H Under 0.5**, which is the least supported current branch.

Exact corner/team-total sportsbook provider definitions were not supplied, so the generated derivative rows remain capped at `FORCED RANK`/`MEDIUM-LOW` where provider-specific settlement matters.

## Current participants and availability

### Werder Bremen — field-owner confirmed XI
Werder's official club release confirmed:

- Karl Hein
- Olivier Deman
- Amos Pieper
- Marco Friedl
- Mick Schmetgens
- Senne Lynen
- Ludovit Reis
- Marco Grüll
- Chuki
- Justin Njinmah
- Niclas Füllkrug

Key late/current changes:
- **Jens Stage OUT** after suffering a serious thigh injury in final training; expected out for several months.
- Karl Hein returns in goal after muscular problems.
- Eren Dinkçi is back in the matchday squad but not starting.
- Marco Grüll starts instead of Samuel Mbangula.
- Mick Schmetgens makes his first Bundesliga start.
- Felix Agu, Keke Topp, Mitchell Weiser, Oskar Wójcik remain unavailable.
- Niklas Stark not in squad due training deficit.

Role consequence:
Stage's absence removes a high-value midfield runner/pressing/box-arrival piece. The replacement structure is less established, increasing Werder's risk in transition defence and second-ball control.

### SC Freiburg
A field-owning confirmed XI was not independently surfaced before the frozen cutoff.

Bundesliga/current near-kickoff projected team:
- Mio Backhaus
- Philipp Treu
- Matthias Ginter
- Philipp Lienhart / Max Rosenfelder
- Jordy Makengo
- Maximilian Eggestein
- Yannik Engelhardt
- Niklas Beste
- Yuito Suzuki
- Vincenzo Grifo / Derry Scherhant
- Igor Matanović

Because the exact final Freiburg XI was not field-owner confirmed at cutoff, participant-sensitive confidence is capped and no speculative starter is treated as fact.

Known availability:
- Muslija unavailable with knee issue in current Bundesliga team news.
- Noah Atubolu has left on loan; Mio Backhaus is the new Freiburg No.1.

## Freiburg current competitive regime

Freiburg's first three competitive matches of 2026/27:

1. Motherwell 1-3 Freiburg — Conference League
2. Fortuna Düsseldorf 1-5 Freiburg — DFB-Pokal
3. Freiburg 4-1 Motherwell — Conference League

Aggregate:
- **12 goals scored**
- **3 conceded**

First-half scoring:
- Motherwell away: first-half goals at 2' and 28'
- Düsseldorf: Freiburg led 1-0 at HT
- Motherwell home: 1-1 at HT

Therefore all three current Freiburg competitive games contained at least one first-half goal.

Mechanism:
- multiple scorers across centre-forward, attacking midfield, wide/second-line and set-piece roles;
- Matanović, Scherhant, Irié, Ginter, Goto, Höler, Kübler, Makengo all contributed across the first three competitive matches;
- Freiburg's attack is not dependent on one finishing route.

The 4-1 Motherwell return included two goals directly generated from set-piece/corner delivery after the red card, reinforcing Freiburg's dead-ball threat but also showing that some realised scoring came from favorable game-state/man-advantage conditions.

## Werder current competitive regime

DFB-Pokal:
- Werder 3-0 Lüneburger SK Hansa
- HT 1-0
- Jens Stage scored in the 11th minute from a set piece.

Werder's own post-match review said the first-half tempo was not fully satisfactory despite controlling the game. The opponent was Oberliga level, so the clean sheet and three-goal output are not transferred directly to a Bundesliga baseline.

Critical regime change:
Stage, the player who scored the cup opener and supplied an important midfield/box-arrival role, is now unavailable.

Werder still retain credible attacking threats:
- Niclas Füllkrug
- Justin Njinmah
- Marco Grüll
- Ludovit Reis
- Chuki
- Dinkçi available from bench

So Freiburg clean-sheet assumptions remain too aggressive.

## Recent H2H / historical mechanism

2025/26:
- Werder 0-3 Freiburg
- Freiburg 1-0 Werder

Useful mechanism:
Freiburg demonstrated they could suppress Werder while still creating enough quality to win both meetings.

But the current Werder roster and coach have changed substantially, so those results are descriptive priors only.

Corners from those two matches were highly unstable:
- 2025 at Bremen: only 2 total corners
- 2026 at Freiburg: 12 total corners

That wide spread is why H2H corners do not control the new corner line.

## Weather / environment

Near match window in Freiburg:
- around 25-26°C
- scattered/cloudy conditions
- no rain at current observation
- moderate SW/WSW breeze around 18-25 km/h, gusts materially higher

Mechanism:
- no meaningful wet-weather suppression at the frozen cutoff;
- moderate wind can reduce crossing accuracy while increasing blocked/cleared balls;
- weather is treated as variance, not a deterministic Over/Under signal.

## Goal-state tree

### Central Freiburg control
Representative scores:
- Freiburg 2-1
- Freiburg 3-1
- Freiburg 2-0

Mechanisms:
- Freiburg's established attacking form survives the step up in opponent quality
- Werder's Stage absence weakens midfield coverage
- Freiburg generate enough box/set-piece exposure for 2+ goals

Favours:
- **1H Over 0.5**
- **Freiburg Over 1.5 team goals**
- FT Over 2.5 in 2-1 / 3-1
- FT Under 2.5 in 2-0

### Open two-sided branch
Representative scores:
- Freiburg 3-2
- 2-2
- Freiburg 4-1

Mechanisms:
- Füllkrug/Njinmah/Grüll create transition threat
- Freiburg continue current high scoring
- Werder must chase after conceding first

Favours:
- 1H Over 0.5
- FT Over 2.5
- Freiburg O1.5

### Low-conversion Freiburg control
Representative scores:
- Freiburg 1-0
- Freiburg 2-0

Mechanisms:
- Freiburg own territory but finishing falls back
- Werder's Hein plus deeper defending suppresses clear chances
- match becomes more controlled after opener

Favours:
- FT Under 2.5
- corners can be either high or low depending blocked pressure

### Werder resistance/upset branch
Representative scores:
- 1-1
- Werder 2-1
- 2-2

Mechanisms:
- Werder's new attack creates efficient transition chances
- Freiburg's short recovery from Thursday affects counterpress/defensive recovery
- Füllkrug converts limited high-value service

Favours:
- 1H Over remains live
- FT Over in 2-1 / 2-2
- Freiburg team-total Over can fail in 1-1 / 1-2

## Corner process

Current/historical evidence:
- Freiburg 2025/26 Bundesliga: ~4.1 corners/game.
- Werder recent Bundesliga rolling sample: ~4.6 corners/game overall, ~3.4 away.
- Freiburg recent specialist home sample: around 5.0-5.3 team corners.
- Combined market is currently centered around 9-10 corners.
- Current public market offers 8/9/10/11 three-way thresholds, with Under 10 priced around an ordinary market center.

Generated research line:
### **Total Corners Under 10.5**

Mechanisms supporting the Under:
- Freiburg can score without sustained corner volume; goal conversion and set-piece efficiency can reduce repeated blocked-pressure sequences.
- An early Freiburg lead can lower later corner demand.
- Werder's away corner production has been below its home level.
- The recent matchup has produced one extremely low-corner state as well as one high state, emphasizing variance rather than a stable high-corner regime.

Kill path:
- Werder defend deep and repeatedly block Freiburg's Grifo/Beste/Suzuki-side delivery;
- Freiburg dominate territorial possession without early conversion;
- trailing Werder add late attacking width, pushing both teams beyond 10 corners.

Provider/definition cap:
user's corner sportsbook/provider is not supplied, so the row remains `FORCED RANK / MEDIUM-LOW`.

## P-201/V01 frozen ranking

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **1H Over 0.5 Goals** | **LEAN** | **MEDIUM** |
| **2** | **Freiburg Team Total Over 1.5 Goals** | **LEAN / derivative cap** | **MEDIUM** |
| **3** | **FT Over 2.5 Goals** | **LEAN / THIN** | **MEDIUM-LOW** |
| **4** | **Total Corners Under 10.5** | **FORCED RANK / provider cap** | **MEDIUM-LOW** |
| **5** | **FT Under 2.5 Goals** | **FORCED RANK / strong counter-branch** | **MEDIUM-LOW** |

Omitted sixth direction:
- **1H Under 0.5 Goals — AVOID / weakest current branch**

## Ranking logic

### #1 — 1H Over 0.5
Every current Freiburg competitive match has contained a first-half goal, and Werder's only competitive match also produced an 11th-minute opener.

This line does not require the full-game match to become open. A Freiburg 1-0 halftime state can still finish 1-0 or 2-0 and cash this contract.

Main kill path:
Freiburg's Thursday recovery leads to a slower start, while Werder defend compactly and the game reaches HT 0-0.

### #2 — Freiburg Over 1.5 team goals
Freiburg have scored 3, 5 and 4 in their three competitive matches and have multiple finishing routes rather than one hot scorer.

Werder's midfield structure has lost Jens Stage at the last moment and starts an inexperienced Bundesliga defensive/midfield configuration.

This line is more robust than the full-game Over because it wins in Freiburg 2-0 as well as 2-1/3-1.

Main kill path:
the current Freiburg output is inflated by lower-level opposition, a red-card state and high conversion, while Hein/compact Werder defending holds Freiburg to one goal.

### #3 — FT Over 2.5
The central 2-1/3-1 family clears the threshold.

Freiburg have current multi-source scoring; Werder still have Füllkrug, Njinmah, Grüll and Reis as credible counter/box threats.

Why below Freiburg O1.5:
a 2-0 Freiburg win is a highly plausible state and loses the match Over while winning the team total.

### #4 — Total Corners Under 10.5
Current team corner baselines cluster closer to 8-10 than 11+, and early Freiburg conversion can suppress later corner demand.

Why not higher:
corner creation is highly state-dependent, recent H2Hs ranged from 2 to 12 corners, and the exact operator/provider is not supplied.

### #5 — FT Under 2.5
The Under retains credible 1-0 / 2-0 Freiburg states.

It ranks fifth because Freiburg's current attacking form and Werder's usable forward talent create more ordinary three-plus-goal branches than one-goal/2-0 control branches.

## Potential winner

**SC Freiburg — LEAN**

Primary reasons:
- 3 straight competitive wins
- 12 goals scored in those three games
- strong home performance Thursday
- deeper current attacking/rotation options
- Werder's late Stage injury materially weakens midfield structure
- Freiburg won both 2025/26 league meetings

Why only LEAN:
- Freiburg are on a short Thursday-Sunday turnaround
- exact field-owner confirmed Freiburg XI was not independently retrieved at cutoff
- Werder have meaningful attacking quality through Füllkrug/Njinmah/Grüll/Reis
- Bundesliga opener creates some regime uncertainty for both teams

## Final freeze

1. **1H Over 0.5 Goals**
2. **Freiburg Over 1.5 Team Goals**
3. **FT Over 2.5 Goals**
4. **Total Corners Under 10.5**
5. **FT Under 2.5 Goals**

Potential winner: **SC Freiburg — LEAN**.

Central score corridor:
- Freiburg 2-1
- Freiburg 3-1
- Freiburg 2-0

Next canonical distinct event ID: **P-202**.




---

# P-202 — Randers FC vs AGF Aarhus — Denmark 3F Superliga

## Event / state freeze

| Field | Frozen value |
|---|---|
| Competition | 2026/27 3F Superliga — Round 6 |
| Event | Randers FC vs AGF |
| Venue | Cepheus Park Randers |
| Scheduled kickoff | 2026-08-30 16:00 CEST / 2026-08-31 00:00 Australia/Melbourne |
| Frozen cutoff | ~2026-08-30 ~15:50 CEST / 23:50 Australia/Melbourne |
| GAME-STATE | **PREGAME** |
| Goal target | `SOCCER_REGULATION_JOINT_GOALS-v1` |
| Corner target | `SOCCER_TEAM_CORNERS_AGF-v1` |
| Method | MDS-2026.08.30-v2.7 qualitative champion |
| Probability state | `NOT_GENERATED / NOT_PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Operator terms | NOT SUPPLIED |

Any information first known after this cutoff is excluded from P-202/V01.

## Candidate slate

User-supplied:
1. 1H Over 0.5 goals
2. 1H Under 0.5 goals
3. FT Over 2.5 goals
4. FT Under 2.5 goals

Generated corner row:
5. **AGF Over 5.5 team corners**

Exact corner sportsbook/provider definition was not supplied, so the corner row is capped at `FORCED RANK / MEDIUM-LOW`.

## Current Randers state

League record:
- 1-1 vs Silkeborg
- 0-1 at Nordsjælland
- 2-0 vs Lyngby
- 0-4 vs FC København
- 0-1 at FC Midtjylland

Aggregate league state:
- 1W, 1D, 3L
- 3 goals scored
- 7 conceded
- four of five league matches finished Under 2.5

Current official squad absences:
- Jannich Storch — illness
- Felix Sommer — injured
- Wessel Dammers — injured
- Lucas Lissens — injured
- Benjamin Örn — injured
- Frederik Lauenborg — injured
- Warren Caddy — injured

Paul Izzo and Mert Demirci are the available goalkeepers in the official squad.

Randers added Axel Henriksson from Blackburn immediately before this fixture; he is in the matchday squad after only just joining the club.

Interpretation:
Randers' low-scoring baseline is real, but the defensive regime is materially less stable today because several centre-back/defensive options and the prior goalkeeper setup are missing.

## Current AGF state

League record:
- 1-1 vs Brøndby
- 2-2 at Lyngby
- 1-2 at Viborg
- 2-2 vs OB

Aggregate:
- 0W, 3D, 1L
- 6 goals scored
- 7 conceded

Current league totals:
- 2
- 4
- 3
- 4

AGF's last league match vs OB:
- 72% possession
- 16 shots
- 6 on target
- **15 corners to 0**
- 2-2 final
- AGF also hit the woodwork multiple times according to the club preview

AGF then played Benfica at Cepheus Park on Thursday and lost 3-1, creating a short three-day turnaround.

Important venue nuance:
AGF have already used Cepheus Park as their European home venue multiple times this summer, so the surface/stadium is unusually familiar for an away side. This weakens a normal Randers home-familiarity edge.

A final field-owning AGF starting XI was not independently surfaced before the frozen cutoff. Thursday's European lineup and current secondary projections are therefore treated as context only, not confirmed starters.

## First-half state

Randers league first halves:
- 1-1 vs Silkeborg
- 0-0 at Nordsjælland
- 1-0 vs Lyngby
- 0-3 vs København
- 0-1 at Midtjylland

Therefore 4 of 5 Randers league matches had a first-half goal.

AGF league first halves:
- 0-0 vs Brøndby
- at least one first-half goal at Lyngby
- 1-1 at Viborg
- 1-2 vs OB

Therefore the current combined opening-phase sample strongly favours one first-half goal over a repeated 0-0 opening state.

## Goal-state tree

### Low-scoring AGF-control branch
Representative scores:
- AGF 1-0
- AGF 2-0
- 1-1

Mechanisms:
- AGF owns more territory but Thursday fatigue limits finishing volume
- Randers' low current scoring persists
- AGF's defensive structure prevents Randers from exploiting transition opportunities

Favours:
- **1H Over 0.5** if AGF score early
- **FT Under 2.5**
- AGF winner in 1-0 / 2-0

### Central competitive branch
Representative scores:
- AGF 2-1
- 1-1
- AGF 1-0

Mechanisms:
- AGF has the better possession/creation process
- Randers' defensive absences create enough high-quality entries for AGF
- Randers retains a home/set-piece route to one goal

Favours:
- 1H Over 0.5
- total sits directly around 2.5 boundary
- AGF slight winner lean

### Open branch
Representative scores:
- AGF 3-1
- 2-2
- Randers 2-1

Mechanisms:
- Randers' patched defence/goalkeeper state leaks early
- score-state forces Randers forward
- AGF's Thursday workload weakens late transition defence

Favours:
- **FT Over 2.5**

### Tactical / delayed-breakthrough branch
Representative scores:
- HT 0-0 -> AGF 1-0
- HT 0-0 -> 1-1

Favours:
- 1H Under 0.5
- FT Under 2.5

## Corner process

Generated line:
### **AGF Over 5.5 team corners**

Current AGF league corners:
- 10 vs Brøndby
- 2 at Lyngby
- 10 at Viborg
- 15 vs OB

Season average in the current four-game sample:
- 9.25 corners for overall
- approximately 6.0 away

Current Randers opponent-corner environment:
- current-season specialist data has Randers conceding roughly 6.6-8.2 corners per game depending source methodology
- Randers match totals have been very high in the current five-game corner sample despite their own lower possession

Mechanism:
AGF's recent 3-4-3/wingback structure creates wide attacks, blocked crosses and repeat entries. Randers' depleted defensive personnel can increase emergency clearances and blocked deliveries even if they successfully suppress goals.

This supports the framework distinction:
**AGF can generate 6+ corners while the match remains Under 2.5 goals.**

Kill path:
- AGF converts an early chance and shifts into game management
- Thursday fatigue reduces sustained wide pressure
- Randers hold more possession than expected and prevent repeat AGF final-third entries

Provider/definition cap:
exact corner provider/operator is not supplied, so the row remains `FORCED RANK`.

## Weather

Near kickoff in Randers:
- cloudy
- about 20°C
- showers earlier in the day with drier/cloudier afternoon conditions

No deterministic weather direction is applied.

The conditions are mild enough that weather is not a major scoring suppressor. Any residual moisture can affect crossing/handling precision, but this is treated as a small variance component rather than a core pick mechanism.

## P-202/V01 frozen ranking

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **1H Over 0.5 Goals** | **LEAN** | **MEDIUM** |
| **2** | **AGF Over 5.5 Team Corners** | **FORCED RANK — provider cap** | **MEDIUM-LOW** |
| **3** | **FT Under 2.5 Goals** | **LEAN / THIN** | **MEDIUM-LOW** |
| **4** | **FT Over 2.5 Goals** | **FORCED RANK / strong counter-branch** | **MEDIUM-LOW** |
| **5** | **1H Under 0.5 Goals** | **AVOID / FORCED RANK** | **MEDIUM-LOW** |

## Ranking logic

### #1 — 1H Over 0.5
Randers have had a first-half goal in 4 of 5 league games, while AGF's last three league matches all contained first-half scoring. AGF's territorial process and Randers' current defensive absences create a credible early AGF goal branch, while Randers still retain home/set-piece counterplay.

The line needs only one goal and can win in both the Under and Over full-game states.

Main kill path:
AGF's Thursday recovery produces a conservative first half and Randers' low-output attack fails to contribute, leaving 0-0 at the break.

### #2 — AGF Over 5.5 corners
AGF's current four-game league corner counts are 10 / 2 / 10 / 15 and Randers are currently allowing heavy opponent-corner volume. AGF dominated OB territorially and produced 15 corners immediately before this fixture.

Why not Rank #1:
exact provider terms are unresolved and corner volume is very score-state sensitive.

### #3 — FT Under 2.5
Randers have scored only 3 league goals in 5 matches and four of their five games stayed Under 2.5. AGF's short Thursday-Sunday turnaround can suppress sustained finishing even if AGF control territory.

Representative Under states:
- AGF 1-0
- AGF 2-0
- 1-1

Why only thin:
Randers' defensive injury/goalkeeper state and AGF's own 3-of-4 Over-2.5 league run create a genuine upper branch.

### #4 — FT Over 2.5
AGF's last three league matches all reached at least three total goals, and their 2-2 against OB came with huge attacking territorial numbers. Randers are missing multiple defenders and their prior goalkeeper.

The best Over path is AGF 2-1 / 3-1 rather than requiring Randers to dominate.

It stays below the Under because Randers' own scoring floor is very low and AGF are on short rest.

### #5 — 1H Under 0.5
This is the narrowest current branch. It requires both AGF's recent early-goal pattern and Randers' 4-of-5 first-half scoring-event pattern to break simultaneously.

## Potential winner

**AGF — LEAN / LOW CONFIDENCE**

Reasons:
- stronger recent territorial/attacking process
- dominated OB despite drawing
- Randers' substantial defensive availability losses
- AGF are unusually familiar with Cepheus Park because it has served as their European home venue
- AGF have won 3 of the last 6 league trips to Randers and lost only once in that subset

Why confidence stays low:
- AGF remain winless in league play
- Thursday Benfica match creates fatigue/rotation uncertainty
- Randers are at home and have an ordinary 1-0 / 1-1 pathway
- final field-owning AGF XI was not independently confirmed at cutoff

## Final freeze

1. **1H Over 0.5 Goals**
2. **AGF Over 5.5 Team Corners**
3. **FT Under 2.5 Goals**
4. **FT Over 2.5 Goals**
5. **1H Under 0.5 Goals**

Potential winner: **AGF — LEAN / LOW CONFIDENCE**.

Central score corridor:
- AGF 1-0
- 1-1
- AGF 2-1

Next canonical distinct event ID: **P-203**.




---

# P-203 — RC Deportivo de A Coruña vs Valencia CF — LaLiga

## Event / state freeze

| Field | Frozen value |
|---|---|
| Competition | 2026/27 LaLiga EA Sports — Matchday 3 |
| Event | RC Deportivo de A Coruña vs Valencia CF |
| Venue | ABANCA-Riazor |
| Scheduled kickoff | 2026-08-30 19:30 CEST / 2026-08-31 03:30 Australia/Melbourne |
| Frozen cutoff | ~2026-08-30 19:10 CEST / 03:10 Australia/Melbourne |
| GAME-STATE | **PREGAME** |
| Goal target | `SOCCER_REGULATION_JOINT_GOALS-v1` |
| Corner target | `SOCCER_MATCH_CORNERS-v1` |
| Method | MDS-2026.08.30-v2.7 qualitative champion |
| Probability state | `NOT_GENERATED / NOT_PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Operator terms | NOT SUPPLIED |

Any information first known after the frozen cutoff is excluded from P-203/V01.

## Candidate slate

User-supplied:
1. 1H Over 0.5 goals
2. 1H Under 0.5 goals
3. FT Over 2.5 goals
4. FT Under 2.5 goals

Generated corner row:
5. **Total Corners Under 10.5**

Exact corner sportsbook/provider terms were not supplied, so the corner row is capped at `FORCED RANK / MEDIUM-LOW`.

## Current official competition state

LaLiga comparison before kickoff:
- Deportivo: 2 played, 2 draws, 2 goals scored, 2 conceded, 2 points.
- Valencia: 2 played, 1 draw, 1 loss, **0 goals scored**, 1 conceded, 1 point.

### Deportivo
Results:
- Deportivo 1-1 Elche
- Málaga 1-1 Deportivo

Both goals were scored by Pierre-Emerick Aubameyang, both in the **21st minute**.

At Málaga:
- Deportivo took the lead through Aubameyang at 21'
- Málaga equalised by penalty at 35'
- the second half became much more closed and chance-light

Against Elche:
- Aubameyang scored at 21'
- Elche equalised at 76'
- Deportivo generated relatively little chance volume compared with Elche

Interpretation:
Deportivo has a real early-transition/Aubameyang route but has not yet shown sustained 3+ goal match creation.

### Valencia
Results:
- Valencia 0-0 Celta
- Valencia 0-1 Real Betis

Valencia have **not scored in either league match**.

Against Betis:
- Valencia started with intensity
- created early approaches through Danjuma/Sato
- no genuine clear first-half scoring chance was converted
- conceded only in the 83rd minute

Against Celta:
- 0-0 final

Interpretation:
Valencia's current problem is attacking conversion/creation rather than defensive collapse.

## Availability / participant state

Valencia's official pre-match press conference confirmed a current injury issue for Guido Rodríguez. Current same-day reporting also listed meaningful defensive/midfield uncertainty around Maffeo and several injured defenders.

Because accessible current lineup sources conflicted materially on Guido Rodríguez/Maffeo and no field-owner confirmed final XI was independently rendered at the frozen cutoff, **no disputed lineup is treated as confirmed fact**.

For Deportivo, Aubameyang is the clear current scoring reference. Current same-day reporting also suggested Deportivo were likely to retain most of the first two-match structure, with Yeremay/Mella still returning toward fuller fitness.

Participant-sensitive confidence is therefore capped.

## Goal-state tree

### Central low-scoring branch
Representative scores:
- Deportivo 1-0
- 1-1
- Valencia 1-0

Mechanisms:
- Valencia's low conversion persists
- Deportivo continues to create selectively through Aubameyang/transition rather than sustained volume
- both teams remain cautious because neither has won

Favours:
- **FT Under 2.5**
- 1H direction depends on whether Deportivo's early Aubameyang route repeats

### Deportivo early-goal branch
Representative scores:
- HT Deportivo 1-0 -> FT 1-0
- HT Deportivo 1-0 -> FT 1-1
- HT Deportivo 1-0 -> FT 2-0

Mechanism:
Aubameyang attacks space behind Valencia's reshuffled defensive line and Deportivo again scores during the opening half.

Favours:
- **1H Over 0.5**
- FT Under still wins in 1-0 / 1-1 / 2-0

### Valencia control branch
Representative scores:
- Valencia 1-0
- Valencia 2-0
- 1-1

Mechanisms:
- Valencia's possession/territory finally converts
- Danjuma/Hugo Duro/Sato-type attacking roles create enough quality
- Deportivo's low current shot volume is exposed against stronger top-flight opposition

Favours:
- FT Under in 1-0 / 2-0 / 1-1

### Open tail
Representative scores:
- Deportivo 2-1
- Valencia 2-1
- 2-2

Mechanisms:
- early goal changes score-state demand
- defensive errors/set pieces create a second goal
- trailing side opens space late

Favours:
- **FT Over 2.5**

## Corner process

Generated research line:
### **Total Corners Under 10.5**

Current Deportivo league corners:
- 8 total vs Elche (Deportivo 2, Elche 6)
- 11 total at Málaga (Deportivo 4, Málaga 7)

Current Deportivo sample:
- 3.0 corners for
- 6.5 conceded
- 9.5 combined

Current Valencia:
- 1 corner vs Celta
- 8 corners vs Betis
- recent/rolling sample around 4.8 for and 4.8 conceded, ~9.6 combined

Current public corner market is centred around **9 total corners**, with Under 10 priced materially shorter than Over 10.

Mechanism supporting Under 10.5:
- both teams have relatively low own attacking-output centres
- Deportivo's early goal state can reduce later home attacking demand
- Valencia have one 1-corner and one 8-corner league game, showing large state dependence rather than persistent high volume
- a low 1-0 / 1-1 match does not require repeated corner clusters

Kill path:
Valencia dominate territory against a promoted side, Deportivo defend deep, and repeated crosses/blocks push Valencia into 7-9 corners by themselves.

Because the exact corner provider/operator is not supplied, this row stays `FORCED RANK`.

## Weather

Near kickoff in A Coruña:
- around 18°C
- sunny/clearing conditions
- breezy, but no major rain signal

Weather therefore does **not** provide a material Under mechanism. The goal Under is driven by current attacking process rather than conditions.

## P-203/V01 frozen ranking

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **FT Under 2.5 Goals** | **LEAN** | **MEDIUM** |
| **2** | **Total Corners Under 10.5** | **FORCED RANK — provider cap** | **MEDIUM-LOW** |
| **3** | **1H Over 0.5 Goals** | **LEAN / THIN** | **MEDIUM-LOW** |
| **4** | **1H Under 0.5 Goals** | **FORCED RANK / strong counter-branch** | **MEDIUM-LOW** |
| **5** | **FT Over 2.5 Goals** | **AVOID / FORCED RANK** | **MEDIUM-LOW** |

## Ranking logic

### #1 — FT Under 2.5
All four league matches involving these teams have stayed below 2.5:
- Deportivo 1-1 Elche
- Málaga 1-1 Deportivo
- Valencia 0-0 Celta
- Valencia 0-1 Betis

Valencia has zero league goals, while Deportivo has scored exactly once in each game and has not produced a high-volume attack.

The most important kill path is an early Deportivo goal forcing Valencia to chase, creating a 2-1/2-2 transition state.

### #2 — Total Corners Under 10.5
The current combined corner baselines sit around 9.5-9.6 and the market centre is around 9. Deportivo's own corner generation is low at 3.0 per game.

Why not higher:
corner markets are state-sensitive and provider terms are unresolved. Valencia generated 8 against Betis, so a one-sided territorial corner spike remains possible.

### #3 — 1H Over 0.5
Aubameyang scored in the 21st minute in **both** Deportivo league games. Deportivo therefore has a repeatable-looking early-transition route, while Valencia's defensive availability is not fully settled.

Why only thin:
Valencia's two league first halves were scoreless and its overall defensive output has been strong.

### #4 — 1H Under 0.5
Valencia's current opening phase strongly supports a 0-0 first half, but Deportivo's exact two-game pattern directly opposes it.

This is a genuine near-tied phase pair rather than a strong contradiction.

### #5 — FT Over 2.5
Requires a regime switch:
- Valencia must finally score and Deportivo contribute,
- or one side must reach 3 goals alone.

That is materially less central than 1-0 / 1-1 / 2-0.

## Potential winner

**RC Deportivo — FORCED WINNER / LOW CONFIDENCE**

Reasons:
- home advantage at Riazor
- unbeaten through two matches
- Aubameyang has scored in both
- Valencia has zero league goals
- Valencia carries more current availability uncertainty

Why confidence remains low:
- Deportivo's underlying chance creation has been modest
- Valencia has conceded only once
- the **draw is one of the largest central branches**
- Valencia has the stronger established top-flight roster on paper

## Final freeze

1. **FT Under 2.5 Goals**
2. **Total Corners Under 10.5**
3. **1H Over 0.5 Goals**
4. **1H Under 0.5 Goals**
5. **FT Over 2.5 Goals**

Potential winner: **RC Deportivo — FORCED WINNER / LOW CONFIDENCE**.

Central score corridor:
- Deportivo 1-0
- 1-1
- Valencia 1-0

Next canonical distinct event ID: **P-204**.




---

# P-204 — Boston Red Sox @ New York Yankees — MLB

## Event/state freeze

| Field | Frozen value |
|---|---|
| Competition | MLB — 2026 regular season |
| Event | Boston Red Sox @ New York Yankees |
| Venue | Yankee Stadium, Bronx, New York |
| Scheduled first pitch | 2026-08-30 13:35 EDT / 2026-08-31 03:35 Australia/Melbourne |
| Frozen cutoff | ~2026-08-30 13:14 EDT / 03:14 Australia/Melbourne |
| GAME-STATE | **PREGAME** |
| Boston starter | Ranger Suárez — LHP — official probable |
| Yankees starter | Will Warren — RHP — official probable |
| Target | `BASEBALL_JOINT_FINAL_RUNS-v1` |
| Method | MDS-2026.08.30-v2.7 qualitative champion |
| Probability state | `NOT_GENERATED / NOT_PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Operator/listed-pitcher/action terms | NOT SUPPLIED |

Any information first known after the frozen cutoff is excluded from P-204/V01.

## Supplied candidate slate

1. Boston Red Sox ML
2. New York Yankees +1.5
3. Over 8.0 Runs
4. Under 8.0 Runs

### Contract geometry

Working assumption:
- moneyline and +1.5 are full-game contracts including extra innings;
- total 8.0 is a full-game integer total.

At **exactly 8 runs**:
- Over 8.0 = PUSH
- Under 8.0 = PUSH

Operator-specific listed-pitcher/action/rain-shortening terms were not supplied and must be checked before settlement.

## Official starter state

### Ranger Suárez — Boston
Official MLB probable:
- 5-3
- 3.35 ERA
- 117 SO
- 118.1 IP
- roughly 1.20 WHIP

Current August:
- 18.1 IP
- 17 H
- 10 R / 9 ER
- 2 HR
- 9 BB
- 12 SO
- 4.42 monthly ERA

Recent starts:
- at Miami: 5.0 IP, 1 ER
- vs Arizona: 5.1 IP, 4 ER
- vs Toronto: 5.0 IP, 1 ER
- vs White Sox: 3.0 IP, 3 ER / 4 R

Interpretation:
Suárez retains the better established run-suppression centre but is not currently in a deep-workload/ace-dominance state. Five-ish innings is the more realistic exposure centre, preserving a meaningful Boston bullpen share.

### Will Warren — Yankees
Official MLB probable:
- 8-6
- 4.39 ERA
- 126 SO
- roughly 1.42 WHIP

Current August:
- 18.1 IP
- 23 H
- 13 R / 12 ER
- 5 HR
- 9 BB
- 17 SO
- **5.89 ERA**
- **1.75 WHIP**

Recent starts:
- vs Houston: 5.0 IP, 7 H, 2 ER / 3 R
- at Baltimore: 4.0 IP, 2 ER
- vs Seattle: 4.0 IP, 5 ER
- at St. Louis: 5.1 IP, 3 ER

Previous 2026 start against Boston:
- 5.2 IP
- 7 H
- 5 R
- 3 BB
- **0 strikeouts**

Interpretation:
Warren's ordinary/early-hook/contact-HR branch is materially wider than Suárez's. The Boston lineup is the strongest current matchup pressure point on the card.

## Current lineups / availability

### Boston — announced lineup
1. Roman Anthony — DH
2. Ceddanne Rafaela — CF
3. Wilyer Abreu — RF
4. Willson Contreras — 1B
5. Adley Rutschman — C
6. Caleb Durbin — 3B
7. Jarren Duran — LF
8. Trevor Story — SS
9. Nick Sogard — 2B

Key change:
- **Roman Anthony activated and returns as leadoff DH**
- **Trevor Story activated and returns at SS**

Anthony hit .280 with two HR, two doubles and four walks over eight rehab games.
Story hit only .171 during his rehab assignment, so his return is treated primarily as lineup/defensive depth rather than a guaranteed offensive upgrade.

### New York — reported lineup
1. Paul Goldschmidt — 1B
2. Cody Bellinger — LF
3. Heliot Ramos — RF
4. Luis García Jr. — DH
5. Amed Rosario — 3B
6. Trent Grisham — CF
7. José Caballero — SS
8. Jazz Chisholm Jr. — 2B
9. Ali Sánchez — C

Current losses/limitations:
- Aaron Judge remains unavailable with rib stress-fracture recovery.
- George Lombard Jr. is out of the starting lineup with right-knee inflammation after leaving Saturday night.
- Ben Rice is not in the reported starting nine.

This materially lowers the Yankees' current offensive ceiling relative to a full-strength lineup.

## Current offensive / matchup context

Boston vs RHP:
- roughly .713 OPS on the season.

Yankees vs LHP:
- roughly .725 OPS on the season.

So raw handedness does **not** create a large team-level split advantage.

The event-specific difference comes more from:
- Warren's current deterioration;
- Boston's lineup reinforcements;
- the Yankees' missing/reduced lineup;
- Suárez's better established starter centre.

## Bullpen / workload state

### Boston
Saturday Game 1:
- Tyron Guerrero
- Garrett Whitlock
- Jovani Moran

Whitlock returned from the IL and threw a clean inning; he has a 2.00 ERA / 0.87 WHIP in 2026.

Saturday Game 2:
- Boston used lower/middle-leverage relief after the opener/bulk sequence; Raymond Burgos allowed the five-run eighth.

Aroldis Chapman had not appeared since Aug. 24 in the available current game log and is therefore on a favorable rest state if active/available.

Interpretation:
Boston's top-end late-game bullpen is better preserved than the 9-2 final might imply.

### Yankees
Friday:
- David Bednar closed the 1-0 win.

Saturday doubleheader:
- Yerry De los Santos appeared in both games.
- Ryan Yarbrough covered three innings in Game 1.
- Paul Blackburn worked important Game 2 outs.
- the 9-2 lead allowed New York to **rest David Bednar** in the nightcap.

Interpretation:
the Yankees' bullpen has accumulated volume, but their best closer is available. This supports both a close-game cushion branch and some late scoring suppression.

## Weather / termination branch

NWS Bronx forecast around game time:
- ~80°F at 1 PM
- ~82°F at 2-4 PM
- SW wind around 9-10 mph
- precipitation chance rises from ~12% at 1 PM to ~37% from 2-4 PM
- slight/chance thunder risk develops during the afternoon

Interpretation:
- warm air can support carry;
- rain/thunder creates delay/termination uncertainty;
- rain is **not** mechanically an Under;
- if interruption occurs, starter re-entry and bullpen transition can widen the upper run tail.

Because operator rain/action terms are unknown, a shortened/void branch is retained rather than graded prospectively.

## Joint run tree

### Boston narrow-win branch
Representative scores:
- Boston 5-4
- Boston 4-3
- Boston 5-3

Mechanisms:
- Boston reaches Warren for 3-4 runs before the middle innings.
- Suárez keeps New York around 2-3 through five.
- both teams' better late relievers prevent a huge late cluster.

Favours:
- **Yankees +1.5** in 5-4 / 4-3
- **Boston ML**
- Over at 5-4, push at 5-3, Under at 4-3

### Boston separation branch
Representative scores:
- Boston 6-3
- Boston 6-2
- Boston 7-3

Mechanisms:
- Warren's contact/HR/early-hook branch lands.
- Anthony/Rafaela/Abreu/Contreras turn lineup depth into repeated baserunners.
- Yankees' reduced lineup fails to answer Suárez.

Favours:
- Boston ML
- Over usually
- Yankees +1.5 loses

### Yankees close-win branch
Representative scores:
- Yankees 4-3
- Yankees 5-4
- Yankees 5-3

Mechanisms:
- Suárez's August command/walk volatility creates traffic.
- Yankee Stadium rewards one mistake.
- Warren stabilizes enough to reach the bullpen without a large deficit.
- Bednar preserves a narrow lead.

Favours:
- **Yankees +1.5**
- Over at 5-4, push at 5-3, Under at 4-3

### Lower-run control branch
Representative scores:
- Boston 4-2
- Yankees 3-2
- Boston 3-2

Mechanisms:
- both starters suppress HR clusters;
- restored/high-leverage bullpen arms dominate late;
- missing Yankees power lowers NY's scoring ceiling.

Favours:
- **Under 8.0**
- Yankees +1.5 in one-run states

### High-run / interruption / bullpen-transition branch
Representative scores:
- Boston 7-5
- Yankees 6-5
- Boston 8-4

Mechanisms:
- Warren exits early;
- Suárez also fails to reach six;
- weather delay disrupts starter plans;
- high bullpen exposure produces inherited-runner or HR clusters.

Favours:
- **Over 8.0**

## P-204/V01 frozen ranking

| Rank | Contract | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Yankees +1.5** | **LEAN** | **MEDIUM** |
| **2** | **Boston Red Sox ML** | **LEAN** | **MEDIUM** |
| **3** | **Over 8.0 Runs** | **LEAN / THIN** | **MEDIUM-LOW** |
| **4** | **Under 8.0 Runs** | **FORCED RANK / strong counter-branch** | **MEDIUM-LOW** |

## Ranking logic

### #1 Yankees +1.5
This is the broadest contract:
- every Yankees win cashes;
- every one-run Boston win also cashes.

The central event tree contains many 5-4 / 4-3 / 3-2 one-run finals because:
- Suárez has the better starter centre but is unlikely to work extremely deep;
- Warren is vulnerable but New York retains Bednar and enough bullpen depth to keep some deficits small;
- both teams have already played multiple close games in this series.

Main kill path:
Warren's current deterioration becomes an early-hook state and Boston's restored lineup converts it into a 6-3 / 6-2 / 7-3 separation.

### #2 Boston ML
Boston gets the outright winner lean because:
- Suárez is the better current starting-pitcher centre;
- Warren has a 5.89 August ERA / 1.75 WHIP;
- Warren already struggled against Boston this year;
- Anthony and Story return;
- New York remains without Judge and Lombard, and the reported lineup is also without Rice.

Why below Yankees +1.5:
the Yankees cushion survives a one-run Boston victory.

### #3 Over 8.0
The Over has several real mechanisms:
- Warren's August contact/HR deterioration;
- Boston's reinforced lineup;
- warm Yankee Stadium conditions;
- both starters have a realistic five-inning rather than seven-inning exposure centre;
- possible rain delay can accelerate bullpen usage.

Important geometry:
- 5-4 = Over WIN
- 5-3 = PUSH
- 4-3 = Over LOSS

Why only thin:
Suárez can suppress this reduced Yankees lineup, and both teams retain rested high-leverage closers.

### #4 Under 8.0
The Under is a strong counterbranch:
- 4-3
- 4-2
- 3-2

all win.

At exactly 8 runs it pushes rather than loses.

It ranks below the Over because Warren's current starter distribution and the upgraded Boston lineup create a larger ordinary upper-tail branch than Suárez/New York's lineup creates in the opposite direction.

## Potential winner

**Boston Red Sox — LEAN**

Primary reasons:
- starter edge
- current Warren deterioration
- Roman Anthony return
- deeper Boston lineup
- Yankees missing important bats

Strongest kill path:
Warren gives New York five competitive innings, the Yankees produce one HR/cluster against Suárez, and Bednar protects a narrow 4-3 / 5-4 lead.

## External market sanity check

A current matching-event snapshot around final refresh showed:
- Boston slight moneyline favorite
- total 8.0

This agrees broadly with:
- Boston slight winner lean
- total near the 8-run boundary

It is used only as an external challenger, not as an internal model probability or value claim.

## Final freeze

1. **Yankees +1.5**
2. **Boston Red Sox ML**
3. **Over 8.0 Runs**
4. **Under 8.0 Runs**

Potential winner: **Boston Red Sox — LEAN**.

Central score corridor:
- Boston 5-4
- Boston 5-3
- Boston 4-3
- Yankees 4-3 counterbranch

Next canonical distinct event ID: **P-205**.



---

# P-205 — Chicago White Sox @ Minnesota Twins — MLB

## Freeze
- Competition: MLB, 2026 regular season
- Venue: Target Field
- Scheduled first pitch: 2026-08-30 13:10 CDT / 2026-08-31 04:10 Australia/Melbourne
- Frozen cutoff: ~13:05 CDT / 04:05 Melbourne
- GAME-STATE: PREGAME
- Official probables: Jordan Hicks (CWS) vs Zebby Matthews (MIN)
- Probability: NOT_GENERATED / NOT_PUBLISHED
- Value: NO VALUE DETERMINABLE

## Supplied contracts
1. White Sox ML
2. Twins ML
3. Over 8.5 Runs
4. Under 8.5 Runs

## Current starter state
Jordan Hicks:
- 2-1, 3.83 ERA, 40.0 IP, 49 SO, 1.53 WHIP
- 43 appearances, only one prior start
- August: 9.0 IP, 12 H, 6 ER, 2 HR, 3 BB, 13 SO, 6.00 ERA
- most recent outing vs Texas: 1 IP, 4 H, 3 ER
- current role is opener/short-start rather than a normal six-inning starter

Zebby Matthews:
- 8-8, 4.86 ERA, 103.2 IP, 88 SO, 1.31 WHIP
- August: 22.2 IP, 24 H, 9 ER, 3 HR, 6 BB, 19 SO, 3.57 ERA
- last two: 5.2 IP/1 ER at Atlanta; 7.0 IP/1 ER vs Athletics

## Current form
- White Sox 72-63, 7-3 last 10, four-game winning streak
- Twins 64-72, 3-7 last 10, four-game losing streak
- current series: Chicago won 7-4 and 3-2
- Chicago has also held the stronger 2026 season-series record

## Lineups
MLB's field-owner starting-lineup page had not fully rendered the orders at cutoff.
A current secondary source marked these lineups as officially posted:

Chicago:
Antonacci, Murakami, Vargas, Benintendi, Braden Montgomery, Colson Montgomery, Peters, Doyle, Romo.

Minnesota:
Keaschall, Brooks Lee, Kody Clemens, Jeffers, Josh Bell, Larnach, Royce Lewis, Culpepper, Walker Jenkins.

Because the field-owner lineup page was still TBD, the orders are treated as secondary-confirmed only.

## Bullpen state
- Bryan Hudson closed both Aug. 28 and Aug. 29 for Chicago.
- Grant Taylor worked 2.2 innings Friday.
- Chicago's opener setup increases expected bulk/relief exposure.
- Minnesota used Andrew Morris for two innings Saturday, but Matthews' recent 5-7 inning workload gives Minnesota the cleaner route to reducing bullpen exposure.

## Joint run tree
Minnesota control:
- MIN 4-3
- MIN 5-3
- MIN 4-2

Chicago counter:
- CWS 5-4
- CWS 5-3
- CWS 6-3

Low-run:
- MIN 4-2
- CWS 4-3
- MIN 3-2

High-run:
- CWS 6-5
- MIN 6-4
- CWS 7-4

## Frozen ranking
1. **Minnesota Twins ML — LEAN / THIN, MEDIUM-LOW**
2. **Under 8.5 Runs — LEAN / THIN, MEDIUM-LOW**
3. **Chicago White Sox ML — FORCED RANK / strong counter-branch, MEDIUM-LOW**
4. **Over 8.5 Runs — FORCED RANK, MEDIUM-LOW**

### Potential winner
**Minnesota Twins — LEAN / LOW CONFIDENCE**

### Main rationale
Minnesota gets the slight winner edge because Matthews is the only conventional starter and has improved sharply in August, while Hicks is an opener whose short exposure pushes a large share of the game into Chicago's bulk/relief chain. Chicago is the stronger team and has dominated the current series, which is why confidence stays low.

The Under ranks second because Matthews has recently worked deep and Minnesota's run production has been weak. Its main kill path is the Hicks/bulk-relief transition creating extra early/middle-inning run exposure.

## Final freeze
1. Minnesota Twins ML
2. Under 8.5 Runs
3. Chicago White Sox ML
4. Over 8.5 Runs

Potential winner: Minnesota Twins — LEAN / LOW CONFIDENCE.

Next canonical distinct event ID: **P-206**.




---

# P-206 — Los Angeles Dodgers @ Detroit Tigers — MLB

## Event/state freeze

| Field | Frozen value |
|---|---|
| Competition | MLB — 2026 regular season |
| Event | Los Angeles Dodgers @ Detroit Tigers |
| Venue | Comerica Park, Detroit |
| Scheduled first pitch | 2026-08-30 13:40 EDT / 2026-08-31 03:40 Australia/Melbourne |
| Final verified state | **PREGAME — DELAYED START / INCLEMENT WEATHER** |
| Official starters | Tyler Glasnow (LAD, RHP) vs Framber Valdez (DET, LHP) |
| Target | `BASEBALL_JOINT_FINAL_RUNS-v1` |
| Method | MDS-2026.08.30-v2.7 qualitative champion |
| Probability state | `NOT_GENERATED / NOT_PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Operator/listed-pitcher/action terms | NOT SUPPLIED |

MLB still listed the event as **Delayed Start — Inclement Weather** at the final refresh and no official live play was incorporated.

## Supplied contracts

1. Dodgers ML
2. Tigers +1.5
3. Over 7.5 Runs
4. Under 7.5 Runs

Working assumption:
- ML and run line include extra innings;
- total 7.5 is full game;
- exact operator listed-pitcher/action/rain-shortening terms remain unknown.

## Starting pitchers

### Tyler Glasnow — Dodgers
- 3-0
- 3.02 ERA
- 44.2 IP
- 56 SO
- 0.87 WHIP
- 11.3 K/9-scale strikeout environment from current season line

Current regime:
- returned from 60-day IL on Aug. 25 after not pitching in MLB since May 6
- first game back: 5.0 IP, 6 H, 3 ER, 0 BB, 7 SO at Atlanta
- no formal pitch limit was announced for his return
- he is now working on ordinary four-day rest but only his second MLB start since May

Interpretation:
Glasnow owns the better run-suppression and strikeout centre, but workload/second-start-after-IL uncertainty remains wider than his season ERA alone implies.

### Framber Valdez — Tigers
- 8-9
- 4.35 ERA
- 144.2 IP
- 111 SO
- 1.41 WHIP

August starts:
- 7.0 IP, 2 ER vs Athletics
- 7.0 IP, 0 ER vs Seattle
- 5.2 IP, 4 ER at Cleveland
- 5.2 IP, 4 ER vs Pittsburgh
- 6.0 IP, 3 ER vs Tampa Bay

Interpretation:
Valdez's current month is better than the raw 4.35 season ERA suggests, but the latest three starts contain a stable 3-4 earned-run branch and lower strikeout output.

## Current batting orders

MLB's field-owning lineup page still displayed TBD at the final crawl, so the posted batting orders are treated as **current secondary-confirmed**, not field-owner-confirmed.

### Dodgers
1. Shohei Ohtani — DH
2. Tommy Edman — 2B
3. Mookie Betts — SS
4. Freddie Freeman — 1B
5. Teoscar Hernández — LF
6. Miguel Rojas — 3B
7. Kyle Tucker — RF
8. Kiké Hernández — CF
9. Ben Rortvedt — C

Important current limitations:
- Will Smith is unavailable.
- Andy Pages is unavailable.
- Max Muncy is not in the posted starting nine against the left-hander.
- Ohtani is batting but will **not pitch**; current arm/knee discomfort removed the earlier opener possibility.

### Tigers
1. Gleyber Torres — 2B
2. Colt Keith
3. Kevin McGonigle
4. Dillon Dingler
5. Brett Callahan
6. Zach McKinstry
7. Hao-Yu Lee
8. Max Clark
9. Javier Báez

Important injuries/current absences include Riley Greene, Kerry Carpenter, Matt Vierling and others from Detroit's normal offensive pool.

## Team/current-form context

### Dodgers
- 81-55
- 6-4 last 10
- current recent scoring has fallen sharply:
  - lost 1-2 Saturday
  - won 2-1 Friday
  - lost 0-1 Thursday
  - lost 5-6 Wednesday
  - lost 3-4 Tuesday
- current last-10 O/U record in one market database: 2 Overs, 8 Unders
- road record remains strong

### Tigers
- 63-72
- 2-8 last 10
- approximately 28 runs over the latest 10-game StatMuse sample
- .180 batting average across the last 10 in the current AP/StatMuse game preview
- Friday/Saturday vs LAD: 1 run, then 2 runs
- several important power/outfield bats remain unavailable

## Historical/current matchup cautions

Current career-vs-starter samples:
- Ohtani vs Valdez: poor historical results across a meaningful but still non-controlling sample
- several Dodgers have tiny prior samples against Valdez
- most current Tigers have little/no history against Glasnow

These are treated only as matchup context; small BvP samples do not control the card.

## Bullpen state

### Detroit
Saturday:
- Tyler Holton: 0.2 IP / 8 pitches
- Kenley Jansen: 0.1 IP / 4 pitches
- Andrew Sears had already supplied 2.2 scoreless innings before the ninth

Detroit therefore reached Sunday with Jansen essentially fresh and several high-leverage options still plausible, although Holton and some middle-relief arms have accumulated multi-day use.

### Los Angeles
Saturday:
- Alex Vesia
- Edgardo Henriquez
- Jack Dreyer
- Seth Halvorsen
combined for 3.1 relief innings / roughly 63 pitches.

Friday:
- Evan Phillips and Tanner Scott handled the key late innings.

Interpretation:
Detroit owns the cleaner late-game relief freshness profile. Los Angeles still has quality arms, but the Dodgers' bullpen has worked more across the first two games of the series.

This materially supports the Tigers +1.5 close-game branch.

## Weather / rain-delay state

Official MLB:
- delayed start due to inclement weather.

Current game-thread/park conditions:
- low/mid-70s at the park before the delay
- cloudy
- modest wind roughly right-to-left

Important mechanism:
- because the delay occurred **before first pitch**, no starter has yet been removed from an already-live outing;
- however, prolonged delay/warm-up disruption creates wider starter-routine uncertainty, particularly for Glasnow in only his second MLB start since May;
- rain is not automatically an Under;
- if the delay materially alters starter preparation or produces another interruption later, bullpen exposure can increase the Over tail.

## Joint run tree

### Central Dodgers low-run edge
Representative scores:
- Dodgers 4-2
- Dodgers 4-3
- Dodgers 3-2

Mechanisms:
- Glasnow suppresses Detroit's depleted offence.
- Valdez keeps Los Angeles below a full offensive ceiling.
- Detroit's fresher bullpen prevents a late separation cluster.

Favours:
- **Dodgers ML**
- **Tigers +1.5** at 4-3 / 3-2
- **Under 7.5**

### Tigers close-game/upset branch
Representative scores:
- Tigers 3-2
- Tigers 4-3
- Tigers 3-1

Mechanisms:
- Glasnow's post-IL/rain-delay routine lands below centre.
- Valdez induces enough poor contact/ground-ball outs.
- Detroit's rested high-leverage relief protects a narrow lead.

Favours:
- **Tigers +1.5**
- Under at 3-2 / 3-1 / 4-3

### Dodgers separation branch
Representative scores:
- Dodgers 5-1
- Dodgers 5-2
- Dodgers 6-2

Mechanisms:
- Valdez's 3-4 ER current branch becomes an early hook.
- Ohtani/Betts/Freeman/Hernández/Tucker create repeated traffic.
- Detroit's low scoring prevents margin compression.

Favours:
- Dodgers ML
- **Tigers +1.5 loses**
- total depends on 5-1/5-2 vs 6-2

### High-run / disrupted-starter branch
Representative scores:
- Dodgers 6-3
- Dodgers 6-4
- Tigers 5-4

Mechanisms:
- rain-delay routine affects one/both starters
- Glasnow does not work deep
- Valdez's recent 3-4 ER branch persists
- bullpen exposure/HR sequencing lifts total

Favours:
- **Over 7.5**

## P-206/V01 frozen ranking

| Rank | Contract | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Tigers +1.5** | **LEAN** | **MEDIUM** |
| **2** | **Dodgers ML** | **LEAN** | **MEDIUM** |
| **3** | **Under 7.5 Runs** | **LEAN / THIN** | **MEDIUM-LOW** |
| **4** | **Over 7.5 Runs** | **FORCED RANK / counter-branch** | **MEDIUM-LOW** |

## Ranking logic

### #1 Tigers +1.5
The cushion has the broadest settlement geometry:
- every Tigers win cashes;
- every one-run Dodgers win cashes.

The current centre contains many one-run/low-run outcomes because:
- Valdez is pitching better than his season ERA alone suggests;
- Detroit has the fresher high-leverage bullpen;
- both games in this series finished 2-1;
- Los Angeles has suffered many recent one-run losses and is in a current low-scoring stretch.

The main kill path is low-total separation:
Glasnow suppresses Detroit almost completely while Valdez gives up 4-5 runs, producing 5-1 / 5-2 / 6-2. The framework explicitly retains this branch rather than assuming "low total = close game."

### #2 Dodgers ML
Los Angeles gets the outright winner lean because:
- Glasnow owns the stronger starter centre;
- Detroit is 2-8 in its last 10;
- Detroit's offence has been extremely weak;
- the Dodgers are substantially stronger overall and on the road;
- Detroit's current lineup is missing several established bats.

Why below Tigers +1.5:
a Dodgers 4-3 / 3-2 victory wins both contracts, while a Detroit upset only wins the Tigers cushion.

### #3 Under 7.5
The central score family is roughly 5-7 total runs.

Support:
- Glasnow's strikeout/run-suppression profile
- Detroit's recent offensive weakness
- both first two series games ending 2-1
- Dodgers' current run-scoring slowdown
- current Valdez form better than season ERA
- Detroit's fresh high-leverage bullpen

Why only third:
7.5 is low; the pregame rain delay plus Glasnow's second-start-after-IL state widens pitcher-exposure uncertainty, and Valdez has allowed 3-4 ER in each of his last three starts.

### #4 Over 7.5
The Over requires 8+ and has clear routes:
- Valdez gives up 4-5 and Detroit contributes 3+
- rain/delay disrupts starter exposure
- Dodgers bullpen carries more series workload
- one HR/sequencing cluster turns a 4-2 game into 6-3

But those require a higher-scoring state than the current central distribution.

## Potential winner

**Los Angeles Dodgers — LEAN**

Primary reasons:
- Tyler Glasnow starter-quality edge
- Dodgers' large season-strength advantage
- Detroit's current offensive decline and injuries
- deeper top-end Dodgers lineup even with several absences

Strongest failure path:
Valdez sustains the better part of his August form, Glasnow's rain-delay/post-IL routine is ordinary rather than dominant, and Detroit's fresher late bullpen closes a 3-2 / 4-3 home win.

## External market sanity check

Current matching-event markets around the delay generally showed:
- Dodgers roughly -150 to -180
- Tigers roughly +135 to +155
- Tigers +1.5 favored relative to Dodgers -1.5
- total centered at 7.5

This is used only as an external challenger and broadly agrees with:
- Dodgers slight/clear winner preference
- Tigers +1.5 broad margin protection
- total near a low-run boundary

No internal value claim is made.

## Final freeze

1. **Tigers +1.5**
2. **Dodgers ML**
3. **Under 7.5 Runs**
4. **Over 7.5 Runs**

Potential winner: **Los Angeles Dodgers — LEAN**.

Central score corridor:
- Dodgers 4-2
- Dodgers 4-3
- Dodgers 3-2
- Tigers 3-2 counterbranch

Next canonical distinct event ID: **P-207**.




---

# P-207 — Cagliari vs Inter Milan — Italy Serie A

## Event/state freeze

| Field | Frozen value |
|---|---|
| Competition | 2026/27 Serie A — Matchday 2 |
| Event | Cagliari vs Inter |
| Venue | Unipol Domus, Cagliari |
| Scheduled kickoff | 2026-08-30 20:45 CEST / 2026-08-31 04:45 Australia/Melbourne |
| Frozen cutoff | ~2026-08-30 20:44 CEST / 04:44 Australia/Melbourne |
| GAME-STATE | **PREGAME** |
| Goal target | `SOCCER_REGULATION_JOINT_GOALS-v1` |
| Corner target | `SOCCER_TEAM_CORNERS_INTER-v1` |
| Method | MDS-2026.08.30-v2.7 qualitative champion |
| Probability state | `NOT_GENERATED / NOT_PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Operator terms | NOT SUPPLIED |

The official Inter match centre and official lineup release still showed the match as scheduled for 20:45 at the frozen cutoff. No live event was used.

## Candidate slate

User-supplied market directions:
1. 1H Over 0.5 goals
2. 1H Under 0.5 goals
3. FT Over 2.5 goals
4. FT Under 2.5 goals

Generated corner row:
5. **Inter Over 4.5 team corners**

The exact sportsbook/provider definition for corners was not supplied, so the corner row is capped at `FORCED RANK / MEDIUM-LOW`.

## Official lineups

### Inter — official 3-5-2
- Josep Martínez
- Benjamin Pavard
- Manuel Akanji
- Alessandro Bastoni
- Luis Henrique
- Nicolò Barella
- Hakan Çalhanoğlu
- Petar Sučić
- Federico Dimarco
- Pio Esposito
- Lautaro Martínez

Key bench attacking options:
- Marcus Thuram
- Ange-Yoan Bonny
- Piotr Zieliński
- Henrikh Mkhitaryan
- Carlos Augusto

Interpretation:
Inter have not materially weakened the central creation structure. Lautaro starts, Dimarco provides left-side width/set-piece delivery, and the Barella/Çalhanoğlu/Sučić midfield supplies both progression and second-line threat. Thuram and Bonny preserve a strong late attacking branch.

### Cagliari — official 4-3-2-1
- Elia Caprile
- Zé Pedro
- Alessandro Deiola
- Rodriguez
- Adam Obert
- Romano
- Harry Winks
- Jacopo Fazzini
- Michel Adopo
- Daniel Maldini
- Pape Mendy

Bench attacking options include:
- Kevin Carlos
- Mattia Felici
- Borrelli
- Fadera

Interpretation:
Cagliari retain a compact midfield/half-space structure rather than an ultra-defensive five-back. Winks/Fazzini/Adopo can support progression, while Maldini and Mendy preserve a transition/finishing route.

## Current competitive regime

### Inter
Serie A opener:
- Inter 4-1 Monza
- 1-1 at half-time
- 70% possession
- 10 total shots listed by Inter's match centre
- 5 on target
- 3 corners

Scorers:
- Çalhanoğlu 6'
- Zieliński 49'
- Pio Esposito 56'
- Bisseck 64'

Interpretation:
Inter's attack was multi-source and did not rely on Lautaro alone. The second-half acceleration branch is especially important for the full-game Over.

### Cagliari
Serie A opener:
- Parma 0-1 Cagliari
- 0-0 at half-time
- winning goal by Romano at 79'
- 53% possession
- 14 shots
- 5 on target
- 2 corners
- current reports also noted two woodwork hits

Interpretation:
The 1-0 final understates Cagliari's attacking process. Cagliari did not simply sit deep and steal one chance; it generated enough attempts to keep a one-goal contribution live against Inter.

## Recent direct matchup

Recent Serie A:
- Cagliari 0-2 Inter — Sep. 2025
- Inter 3-0 Cagliari — Apr. 2026
- Cagliari 0-3 Inter — Dec. 2024
- Cagliari 0-2 Inter — Aug. 2023

First-half states in recent relevant meetings:
- Sep. 2025: Inter led 1-0 at HT
- Apr. 2026: 0-0 at HT
- Aug. 2023: Inter led 2-0 at HT

Useful mechanism:
Inter have repeatedly controlled territory and suppressed Cagliari's scoring, but the exact timing of the breakthrough has varied considerably.

H2H is descriptive only; current lineups and season state control.

## Corner process

Generated research line:
### **Inter Over 4.5 team corners**

Relevant direct-match corner examples:
- Cagliari 0-2 Inter (Sep. 2025): Cagliari 5, Inter 7
- Cagliari 0-2 Inter (Aug. 2023): Cagliari 4, Inter 7

Current openers:
- Inter produced only 3 corners against Monza despite 70% possession.
- Cagliari conceded only 3 corners to Parma.

Interpretation:
The current-season corner evidence prevents a strong high-corner claim, but the matchup mechanism still supports 5+:
- Inter's wingback width through Dimarco/Luis Henrique
- Cagliari's likely lower territorial share
- crossing/block/clearance states against a compact home shape
- multiple historical 7-corner Inter outputs at this venue

Kill path:
Inter score very early and switch into controlled circulation, reducing sustained blocked-cross pressure; Cagliari defend centrally without conceding repeated corners.

Because the exact corner provider/operator is not supplied, this remains provider-capped.

## Weather/environment

Near kickoff:
- roughly 28°C
- mostly clear
- warm conditions after a very hot day

Mechanism:
- no rain/wet-ball suppression
- heat can lower repeated pressing intensity later
- lower late defensive pressure can widen the second-half scoring branch

Weather is a secondary variance input, not a controlling Over signal.

## Joint goal-state tree

### Inter control / Under branch
Representative scores:
- Inter 2-0
- Inter 1-0
- Inter 2-0 after 0-0 HT

Mechanisms:
- Inter dominate territory
- Cagliari's compact shape limits central chance quality
- Inter's defence suppresses Mendy/Maldini transition

Favours:
- **FT Under 2.5**
- 1H direction depends on breakthrough timing

### Inter control / Over branch
Representative scores:
- Inter 3-0
- Inter 3-1
- Inter 2-1

Mechanisms:
- Inter's multi-source attack produces 2-3 goals
- Cagliari contributes one through transition/set piece, or Inter carries the total alone
- Inter's strong bench maintains attacking pressure

Favours:
- **FT Over 2.5**
- Inter winner

### Early Inter breakthrough
Representative states:
- HT Inter 1-0 -> FT 2-0
- HT Inter 1-0 -> FT 3-0
- HT Inter 1-0 -> FT 3-1

Favours:
- **1H Over 0.5**
- full total remains split between 2-0 and 3+ states

### Slow first-half state
Representative states:
- HT 0-0 -> Inter 1-0
- HT 0-0 -> Inter 2-0
- HT 0-0 -> 1-1

Favours:
- **1H Under 0.5**
- FT Under usually

## P-207/V01 frozen ranking

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **FT Over 2.5 Goals** | **LEAN / THIN** | **MEDIUM-LOW** |
| **2** | **1H Over 0.5 Goals** | **LEAN / THIN** | **MEDIUM-LOW** |
| **3** | **Inter Over 4.5 Team Corners** | **FORCED RANK — provider cap** | **MEDIUM-LOW** |
| **4** | **FT Under 2.5 Goals** | **FORCED RANK / strong counter-branch** | **MEDIUM-LOW** |
| **5** | **1H Under 0.5 Goals** | **FORCED RANK / strong counter-branch** | **MEDIUM-LOW** |

## Ranking logic

### #1 — FT Over 2.5
Inter opened with four goals from four different scorers and field a strong attacking structure again. Cagliari's 1-0 opener contained substantially more attacking activity than the scoreline suggests, so a Cagliari contribution cannot be dismissed.

Central Over states:
- Inter 2-1
- Inter 3-0
- Inter 3-1

Main kill path:
Inter dominate but Cagliari remain compact and scoreless, producing the familiar 2-0 result.

### #2 — 1H Over 0.5
Inter scored in the sixth minute of the opener and have several current/historical early-breakthrough routes through Lautaro, Dimarco delivery and second-line midfield runners.

Recent Cagliari-Inter meetings have included both 1-0 and 0-0 halftime states, so evidence is not strong enough to rank this first.

Main kill path:
Cagliari's compact midfield survives the opening pressure and Inter's breakthrough is delayed until the second half.

### #3 — Inter Over 4.5 corners
Inter have produced seven corners in each of the two recent away H2H examples available from Inter's match centre, and today's width/territorial matchup again supports sustained wide pressure.

Why only third/provider-capped:
Inter had only three corners despite 70% possession against Monza, while Cagliari conceded only three at Parma. The current-season evidence is therefore mixed.

### #4 — FT Under 2.5
The Under has an extremely credible Inter 1-0 / 2-0 family. Inter have beaten Cagliari 2-0 and 3-0 in the two most recent meetings and Cagliari's opener stayed 1-0.

It ranks below the Over because Inter's current attack has more scoring routes than last season's narrow-control branch, and Cagliari's opener showed enough chance creation to preserve a one-goal home contribution.

### #5 — 1H Under 0.5
Cagliari's opener was 0-0 at HT and the April 2026 H2H was also 0-0 at HT, so this is a live branch.

It ranks fifth because Inter scored early in the current opener and also led 1-0 at halftime in the last trip to Cagliari.

## Potential winner

**Inter Milan — LEAN**

Primary reasons:
- defending champions
- materially stronger starting XI
- strong midfield/territorial advantage
- Lautaro starts with Pio Esposito
- deep attacking bench
- repeated recent H2H control
- Cagliari's single-match win does not erase the quality gap

Strongest failure path:
Cagliari's compact 4-3-2-1 frustrates Inter, Caprile performs strongly, and Mendy/Maldini/Fazzini create one high-value transition or set-piece goal, producing 1-0 / 1-1.

## Final freeze

1. **FT Over 2.5 Goals**
2. **1H Over 0.5 Goals**
3. **Inter Over 4.5 Team Corners**
4. **FT Under 2.5 Goals**
5. **1H Under 0.5 Goals**

Potential winner: **Inter Milan — LEAN**.

Central score corridor:
- Inter 2-1
- Inter 3-0
- Inter 2-0

Next canonical distinct event ID: **P-208**.




---

# P-208 — Lazio vs Genoa — Italy Serie A

## Event/state freeze

| Field | Frozen value |
|---|---|
| Competition | 2026/27 Serie A — Matchday 2 |
| Event | Lazio vs Genoa |
| Venue | Stadio Olimpico, Rome |
| Scheduled kickoff | 2026-08-30 20:45 CEST / 2026-08-31 04:45 Australia/Melbourne |
| Frozen cutoff | ~2026-08-30 20:47 CEST / 04:47 Australia/Melbourne |
| GAME-STATE | **PREGAME-AT-CUTOFF / START-CROSSING FEED LAG** |
| Goal target | `SOCCER_REGULATION_JOINT_GOALS-v1` |
| Corner target | `SOCCER_MATCH_CORNERS-v1` |
| Method | MDS-2026.08.30-v2.7 qualitative champion |
| Probability state | `NOT_GENERATED / NOT_PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Operator terms | NOT SUPPLIED |

At the cutoff, Lazio's official site and multiple current match pages still showed the event as scheduled/pre-match with **no verified live score or clock**. Under the project's documented feed-lag precedent, P-208/V01 is treated as pregame-at-cutoff. No later live event may revise this frozen card.

## Candidate slate

User-supplied:
1. 1H Over 0.5 goals
2. 1H Under 0.5 goals
3. FT Over 2.5 goals
4. FT Under 2.5 goals

Generated corner row:
5. **Total Corners Over 8.5**

Exact corner sportsbook/provider terms were not supplied. The corner row is therefore capped at `FORCED RANK / MEDIUM-LOW`.

## Confirmed/current lineups

### Lazio — current official-lineup consensus
- Christos Mandas
- Romano Floriani Mussolini
- Danilho Doekhi
- Oliver Provstgaard
- Alfonso Pedraza
- Davide Frattesi
- Nicolò Rovella
- Kenneth Taylor
- Gustav Isaksen
- Boulaye Dia
- Mattia Zaccagni

Current official squad absences included Adam Marusic and Fisayo Dele-Bashiru, with additional unavailable/non-selected names around the wider squad. Andrea Pinamonti and Josip Sutalo were newly available from the bench.

### Genoa
- Justin Bijlow
- Alessandro Marcandalli
- Leo Østigård
- Johan Vásquez
- Brooke Norton-Cuffy
- Djibril Sow
- Morten Frendrup
- Mikael Ellertsson
- Tommaso Baldanzi
- Vitinha
- Lorenzo Colombo

Milutin Osmajic and Hamed Traorè were newly available from the bench.

## Current league process

### Lazio — 1-0 win at Bologna
Headline:
- won 1-0
- Frattesi scored at 59'

Underlying process from current statistical sources:
- 41% possession
- 10 shots
- 3 on target
- 6 corners
- roughly **0.64-0.65 xG**
- Bologna generated roughly 1.9-2.3 xG depending provider, 13-14 shots and 8 corners

Interpretation:
The win was valuable, but Lazio's underlying attacking creation was much less dominant than the result. The defensive/goalkeeping branch overperformed the raw chance balance, so a home offensive surge cannot simply be assumed.

### Genoa — 0-2 loss vs Napoli
Current process:
- 46% possession
- 11 shots
- 2 on target
- 5 corners
- roughly **0.65-0.71 xG**
- Napoli roughly 0.9 xG

Interpretation:
Genoa's 0-2 result was worse than the underlying shot/xG balance. They did not generate enough high-quality chances, but neither were they territorially overwhelmed throughout.

## First-half state

Opening league matches:
- Bologna 0-0 Lazio at HT
- Genoa 0-0 Napoli at HT

Recent direct meetings:
- Lazio 3-2 Genoa (Jan 2026) was **0-0 at HT**
- Genoa 0-3 Lazio (Sep 2025) was **0-2 at HT**

Interpretation:
Current-season opening-phase evidence supports a cautious first half, but the previous away H2H shows Lazio retains a real early-breakthrough branch.

## Direct-match prior

Recent Serie A:
- Lazio 3-2 Genoa — Jan 2026
- Genoa 0-3 Lazio — Sep 2025
- Genoa 0-2 Lazio — Apr 2025
- Lazio 3-0 Genoa — Oct 2024
- Genoa 0-1 Lazio — Apr 2024

Lazio have controlled the recent results strongly.

However, the January 3-2 contained two penalties and all five goals after halftime, so it is not treated as proof of a naturally high-scoring first half or match.

## Corner process

Generated line:
### **Total Corners Over 8.5**

Current opening-round totals:
- Bologna-Lazio: **14 corners** (8-6)
- Genoa-Napoli: **10 corners** (5-5)

Current direct-match context:
- Lazio 3-2 Genoa, Jan 2026: 8 total corners (5-3)
- Genoa 0-3 Lazio, Sep 2025: 6 total corners (6-0)
- broader current H2H specialist sample: roughly 9.5 average total corners

Mechanism supporting 9+:
- Lazio's 4-3-3 uses wide attackers Zaccagni/Isaksen and fullback width
- Genoa's 3-4-2-1/3-5-2 can concede wide territory and clearances while also generating wingback attacks through Norton-Cuffy/Ellertsson
- both opening league matches generated at least 10 corners

Kill path:
- an early Lazio goal changes the game into controlled circulation
- Genoa fail to sustain territory
- efficient finishing reduces repeated blocked-cross/clearance sequences

Because exact provider terms are unknown, the corner row remains `FORCED RANK`.

## Weather

Near kickoff in Rome:
- around 29°C
- mostly clear
- no rain signal

Mechanism:
- no wet-weather finishing suppression
- heat can reduce repeated pressing intensity later, potentially widening late defensive spacing
- weather is secondary and does not override the current low-goal process.

## Joint goal-state tree

### Central low-output Lazio edge
Representative scores:
- Lazio 1-0
- Lazio 2-0
- 1-1

Mechanisms:
- Lazio own more territory at home but remain only moderately efficient
- Genoa's compact structure keeps central chance quality down
- Mandas/Bijlow and deeper blocks prevent clusters

Favours:
- **FT Under 2.5**
- Lazio winner in 1-0/2-0
- 1H Under remains live

### Slow first half / second-half Lazio breakthrough
Representative:
- HT 0-0 -> Lazio 1-0
- HT 0-0 -> Lazio 2-0
- HT 0-0 -> 1-1

Favours:
- **1H Under 0.5**
- **FT Under 2.5**

### Early Lazio goal branch
Representative:
- HT Lazio 1-0 -> FT 2-0
- HT Lazio 1-0 -> FT 2-1
- HT Lazio 1-0 -> FT 3-0

Favours:
- **1H Over 0.5**
- full-game total splits between Under 2-0 and Over 2-1/3-0

### Open second-half branch
Representative:
- Lazio 2-1
- Lazio 3-1
- 2-2

Mechanisms:
- Genoa equalizes or concedes early and must open
- Lazio bench attackers exploit wider spaces
- late fatigue/transition errors increase quality

Favours:
- **FT Over 2.5**

## P-208/V01 frozen ranking

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **FT Under 2.5 Goals** | **LEAN** | **MEDIUM** |
| **2** | **1H Under 0.5 Goals** | **LEAN / THIN** | **MEDIUM-LOW** |
| **3** | **Total Corners Over 8.5** | **FORCED RANK — provider cap** | **MEDIUM-LOW** |
| **4** | **1H Over 0.5 Goals** | **FORCED RANK / counter-branch** | **MEDIUM-LOW** |
| **5** | **FT Over 2.5 Goals** | **AVOID / FORCED RANK** | **MEDIUM-LOW** |

## Ranking logic

### #1 — FT Under 2.5
Both opening league matches stayed Under 2.5 and were 0-0 at halftime. Lazio's 1-0 win at Bologna came from only ~0.64 xG while Genoa created only ~0.7 xG against Napoli. The strongest current score family is 1-0 / 2-0 / 1-1.

Main kill path:
Lazio score early, Genoa must abandon the compact state, and the match opens into 2-1 / 3-1 / 2-2.

### #2 — 1H Under 0.5
Both teams opened the league with 0-0 first halves, and the January 2026 H2H was also 0-0 at halftime. Lazio's opener did not show strong early chance creation.

Why only thin:
the September 2025 H2H had Lazio 2-0 up at half-time, and today's Zaccagni-Dia-Isaksen front three can produce an early transition/set-piece goal.

### #3 — Total Corners Over 8.5
The two opening-round matches involving these teams generated 14 and 10 total corners. The structural matchup includes two sets of wide players/wingbacks and a plausible clearance/block chain.

Why capped:
recent direct H2Hs also produced only 8 and 6 corners, and exact sportsbook/provider terms are unknown.

### #4 — 1H Over 0.5
The best path is an early Lazio goal through Zaccagni/Isaksen/Dia or a Genoa transition through Baldanzi/Vitinha/Colombo.

It stays below the Under because current opening-phase evidence is distinctly low-event.

### #5 — FT Over 2.5
The Over has real 2-1 / 3-0 / 3-1 branches and recent H2Hs include 3-2 and 3-0.

But the current 2026/27 process is substantially lower-output than those historic scorelines, so 3+ goals remains the less central branch.

## Potential winner

**Lazio — LEAN / MEDIUM-LOW**

Primary reasons:
- home field
- stronger recent H2H record
- won at Bologna despite a difficult underlying game
- Frattesi provides current midfield box-arrival threat
- Zaccagni/Dia/Isaksen is a stronger attacking trio than Genoa's current front line on paper

Why confidence is capped:
- Lazio's Bologna underlying process was poor
- current defensive injuries/changes reduce stability
- Genoa's Napoli loss was not as one-sided by xG as the 0-2 score suggests
- 0-0 / 1-1 draw branches remain material

## Final freeze

1. **FT Under 2.5 Goals**
2. **1H Under 0.5 Goals**
3. **Total Corners Over 8.5**
4. **1H Over 0.5 Goals**
5. **FT Over 2.5 Goals**

Potential winner: **Lazio — LEAN / MEDIUM-LOW**.

Central score corridor:
- Lazio 1-0
- Lazio 2-0
- 1-1

Next canonical distinct event ID: **P-209**.


---

# P-209 — Corinthians vs Santos — Brazil Série A

## Event/state freeze

| Field | Frozen value |
|---|---|
| Competition | 2026 Campeonato Brasileiro Série A — Round 25 |
| Event | Corinthians vs Santos |
| Venue | Neo Química Arena, São Paulo |
| Scheduled kickoff | 2026-08-30 16:00 BRT / 2026-08-31 05:00 Australia/Melbourne |
| Frozen cutoff | ~2026-08-30 15:51 BRT / 2026-08-31 04:51 Australia/Melbourne |
| GAME-STATE | **PREGAME** |
| Goal target | `SOCCER_REGULATION_JOINT_GOALS-v1` |
| Corner target | `SOCCER_MATCH_CORNERS-v1` |
| Method | current active qualitative soccer framework |
| Probability state | `NOT_GENERATED / NOT_PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Operator terms | NOT SUPPLIED |

The stadium schedule and current match feeds still showed the match as not started at the frozen cutoff. No live event is used.

## Candidate slate

User-supplied:
1. 1H Over 0.5 goals
2. 1H Under 0.5 goals
3. FT Over 2.5 goals
4. FT Under 2.5 goals

Generated corner row:
5. **Total Corners Over 8.5**

Exact corner sportsbook/provider terms were not supplied. The corner row is therefore capped at `FORCED RANK / MEDIUM-LOW`.

## Current lineups / availability

### Corinthians — confirmed by multiple same-day lineup sources
- Hugo Souza
- Matheuzinho
- Gabriel Paulista
- Gustavo Henrique
- Matheus Bidu
- Raniele
- Allan
- Rodrigo Garro
- Dieguinho
- Kaio César
- Memphis Depay

Key availability:
- **Memphis Depay starts**, his first start since renewing and first start in more than five months.
- **Yuri Alberto OUT** after renewed discomfort during recovery from a right-thigh injury.
- **Breno Bidon suspended**.
- André unavailable with thigh injury.
- Hugo Souza, Matheuzinho and Matheus Bidu return.

Interpretation:
Corinthians restores important ball progression and finishing quality through Memphis/Garro, but loses the usual Yuri-Alberto striker route and Bidon's midfield continuity.

### Santos — confirmed by multiple same-day lineup sources
- Gabriel Brazão
- Igor Vinícius
- Lucas Veríssimo
- Luan Peres
- Escobar
- Willian Arão
- Gustavo Henrique
- Gabriel Bontempo
- Barreal
- Neymar
- Gabigol

Key availability:
- **Neymar returns to the XI** after being preserved from the Palmeiras cup match.
- **Gabigol returns to the XI**.
- Gabriel Bontempo returns.
- João Schmidt is suspended.

Interpretation:
Santos' attacking ceiling is materially higher than in the midweek 0-3 cup loss because Neymar and Gabigol both start. Schmidt's absence weakens one midfield-control/defensive-protection route.

## Current table / form context

Entering Round 25:
- Corinthians: 10th, 32 points.
- Santos: 14th, 26 points, close to the relegation zone.

Corinthians' last two league matches:
- Corinthians 1-2 Cruzeiro
- Coritiba 2-1 Corinthians

Santos' latest:
- Santos 1-1 Mirassol — league
- Palmeiras 3-0 Santos — Copa do Brasil, without Neymar

Interpretation:
Corinthians has the stronger table/home position but enters off two league losses.
Santos' cup defeat is not transferred directly because today's attacking XI is materially stronger.

## First-half goal process

Recent relevant phase evidence:

### Current-season H2H
Santos 1-1 Corinthians:
- Memphis 18'
- Gabigol 21'
- HT 1-1

### Corinthians latest league games
vs Cruzeiro:
- Cruzeiro scored at 36'
- HT 0-1

at Coritiba:
- Coritiba scored at 39'
- HT 1-0

### Santos latest league/cup games
vs Mirassol:
- Mirassol scored at 35'
- HT 0-1

at Palmeiras:
- Palmeiras scored twice in the first half

This is unusually coherent phase evidence: each of these recent relevant matches contained at least one first-half goal.

Mechanisms today:
- Memphis/Garro/Kaio César offer Corinthians an early attacking route.
- Neymar/Gabigol/Barreal give Santos a higher-quality transition/final-third route than the midweek cup XI.
- suspended/absent midfield pieces on both sides reduce continuity in defensive control.

Main 1H-Under branch:
classical-derby caution plus heat/storm uncertainty produces a lower-tempo first 30-40 minutes.

## Full-game goal process

Recent exact score evidence:
- Santos 1-1 Corinthians — March 2026
- Corinthians 1-2 Cruzeiro
- Coritiba 2-1 Corinthians
- Santos 1-1 Mirassol
- Palmeiras 3-0 Santos

The current evidence therefore includes both:
- strong 2-1 / 1-2 / 3-0 upper states,
- and a repeated 1-1 derby/league-control branch.

Important structural change:
today's Santos attack is stronger than the cup XI because Neymar and Gabigol return, while Corinthians' attack improves through Memphis but remains without Yuri Alberto.

## Corner process

Generated research line:
### **Total Corners Over 8.5**

Current/recent corner evidence:
- season-profile sources put both Corinthians and Santos around **5.0 corners for and 5.0 conceded per match**, implying a descriptive ~10-corner centre.
- Corinthians-Coritiba recent total: **18 corners**
- Corinthians-Cruzeiro: **11 corners**
- Santos-Mirassol: **12 corners**
- March Santos-Corinthians H2H: **10 corners** (Santos 4, Corinthians 6)

Mechanism:
- Corinthians use Garro/Kaio César/Dieguinho and fullback width to create blocked delivery and end-line states.
- Santos use Neymar/Barreal plus overlapping fullbacks/Igor Vinícius to generate width and defensive clearances.
- if the first goal arrives early, the trailing side's chasing state can sustain corner exposure.

Kill path:
an early goal produces controlled possession rather than sustained wide pressure, or high finishing efficiency converts attacks before they become repeated blocked-cross sequences.

Provider cap:
the exact corner provider/operator definition was not supplied, so this remains `FORCED RANK`.

## Weather

Near the frozen cutoff in São Paulo:
- around 27°C
- mostly cloudy
- humid/warm
- current weather feed carries afternoon thunderstorm risk and an INMET storm alert

A separate local forecast source described hotter/drier conditions with limited rain, so the exact short-window precipitation state is not perfectly consistent across sources.

Treatment:
weather is **not** used directionally. Heat can reduce sustained pressing; storm/wind can reduce clean delivery but also create errors. It widens variance rather than determining Over/Under.

## Joint goal-state tree

### Central derby branch
Representative scores:
- 1-1
- Corinthians 2-1
- Santos 2-1

Mechanisms:
- at least one early chance is converted
- neither side sustains full control
- both attacks have enough quality for one goal

Favours:
- **1H Over 0.5**
- FT total sits directly around the 2.5 boundary

### Corinthians control branch
Representative scores:
- Corinthians 1-0
- Corinthians 2-0
- Corinthians 2-1

Mechanisms:
- home pressure and Garro/Memphis creation
- Santos' Schmidt absence weakens midfield protection
- Hugo Souza / centre-backs suppress Santos transitions

Favours:
- Corinthians winner
- Under at 1-0 / 2-0
- Over at 2-1

### Santos attacking branch
Representative scores:
- Santos 2-1
- 1-1
- Santos 2-0

Mechanisms:
- Neymar/Gabigol return changes final-third quality
- Corinthians' recent defensive concessions persist
- Santos attack Garro/wingback transition spaces

Favours:
- full-game total depends on 2-1 vs 1-1/2-0

### Open branch
Representative scores:
- Corinthians 3-1
- Santos 3-1
- 2-2

Mechanisms:
- early goal plus chase state
- midfield control weakens
- heat/storm conditions increase late fatigue/error variance

Favours:
- **FT Over 2.5**

### Slow/tactical branch
Representative scores:
- Corinthians 1-0
- 0-0
- 1-1 after 0-0 HT

Favours:
- **1H Under 0.5**
- **FT Under 2.5**

## P-209/V01 frozen ranking

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **1H Over 0.5 Goals** | **LEAN** | **MEDIUM** |
| **2** | **Total Corners Over 8.5** | **FORCED RANK — provider cap** | **MEDIUM-LOW** |
| **3** | **FT Over 2.5 Goals** | **LEAN / THIN** | **MEDIUM-LOW** |
| **4** | **FT Under 2.5 Goals** | **FORCED RANK / strong counter-branch** | **MEDIUM-LOW** |
| **5** | **1H Under 0.5 Goals** | **AVOID / FORCED RANK** | **MEDIUM-LOW** |

## Ranking logic

### #1 — 1H Over 0.5
The strongest current phase evidence:
- the March derby had goals at 18' and 21';
- Corinthians' last two league games contained first-half goals;
- Santos-Mirassol contained a first-half goal;
- Palmeiras-Santos contained two first-half goals.

Today's attacking personnel also improve the early-goal branch through Memphis for Corinthians and Neymar/Gabigol for Santos.

Main kill path:
derby caution creates a low-risk opening and both sides reach halftime 0-0.

### #2 — Total Corners Over 8.5
The descriptive combined team baseline is about 10 corners, and recent relevant totals are 18, 11, 12 and 10.

The tactical matchup provides credible wide-entry/block/clearance exposure.

Why provider-capped:
exact operator/provider terms remain unresolved.

### #3 — FT Over 2.5
Three of the four latest all-competition results across these teams reached at least three total goals, and today's Santos attacking XI is stronger than the midweek cup XI.

Central Over states:
- Corinthians 2-1
- Santos 2-1
- 2-2

Why only thin:
the March derby finished 1-1 despite two early goals, showing that an early-goal contract can win while the full-game Over still fails. Corinthians also remain without Yuri Alberto.

### #4 — FT Under 2.5
The Under has meaningful 1-0 / 2-0 / 1-1 branches.

The most important evidence is the March 1-1 H2H, where both goals came by 21' but no further scoring occurred.

It ranks below the Over because both sides' recent defensive profiles and today's restored attacking talent make 2-1 more live than in that March game.

### #5 — 1H Under 0.5
This requires the strongest current phase pattern to reverse. It is still a valid derby branch, but the recent early-goal evidence is unusually consistent.

## Potential winner

**Corinthians — LEAN / LOW CONFIDENCE**

Primary reasons:
- home advantage at Neo Química Arena
- stronger table position
- Hugo Souza and both fullbacks return
- Memphis starts and Garro remains the principal creator
- Santos remain under greater league pressure and are missing João Schmidt

Why confidence stays low:
- Corinthians have lost two straight league games
- Yuri Alberto and Bidon are absent
- Neymar and Gabigol materially improve Santos compared with the cup defeat
- the March H2H finished 1-1 and the draw remains a major central branch

## Final freeze

1. **1H Over 0.5 Goals**
2. **Total Corners Over 8.5**
3. **FT Over 2.5 Goals**
4. **FT Under 2.5 Goals**
5. **1H Under 0.5 Goals**

Potential winner: **Corinthians — LEAN / LOW CONFIDENCE**.

Central score corridor:
- Corinthians 2-1
- 1-1
- Santos 2-1

Next canonical distinct event ID: **P-210**.


---

# P-210 — Flamengo vs Botafogo — Brazil Série A

## Event/state freeze

| Field | Frozen value |
|---|---|
| Competition | 2026 Campeonato Brasileiro Série A — Round 25 |
| Event | Flamengo vs Botafogo |
| Venue | Maracanã, Rio de Janeiro |
| Scheduled kickoff | 2026-08-30 16:00 BRT / 2026-08-31 05:00 Australia/Melbourne |
| Frozen cutoff | ~2026-08-30 15:56 BRT / 04:56 Australia/Melbourne |
| GAME-STATE | **PREGAME** |
| Goal target | `SOCCER_REGULATION_JOINT_GOALS-v1` |
| Corner target | `SOCCER_MATCH_CORNERS-v1` |
| Method | current active qualitative soccer framework |
| Probability state | `NOT_GENERATED / NOT_PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Operator terms | NOT SUPPLIED |

No information first known after the frozen cutoff may revise P-210/V01.

## Candidate slate

User-supplied:
1. 1H Over 0.5 goals
2. 1H Under 0.5 goals
3. FT Over 2.5 goals
4. FT Under 2.5 goals

Generated corner row:
5. **Total Corners Over 8.5**

The exact sportsbook/provider definition for corners was not supplied, so the corner row is capped at `FORCED RANK / MEDIUM-LOW`.

## Current lineups / availability

### Flamengo — confirmed same-day XI
- Rossi
- Emerson Royal
- Léo Ortiz
- Léo Pereira
- Ayrton Lucas
- Erick Pulgar
- Jorginho
- Giorgian de Arrascaeta
- Luiz Araújo
- Samuel Lino
- Pedro

Important current changes:
- Gonzalo Plata has left for Dinamo Moscow.
- Luiz Araújo starts in his role on the right.
- Saúl is unavailable with fever.
- Alex Sandro, Vitão and De la Cruz remain unavailable.
- Bruno Henrique is also among the current absences reported in pregame coverage.

Interpretation:
Flamengo retain a high-quality attacking spine through Arrascaeta, Pedro, Samuel Lino and Luiz Araújo, but the defensive/rotation state is not full strength.

### Botafogo — current same-day XI/consensus
- Gabriel Batista
- Vitinho
- Ferraresi
- Justino
- Alex Telles
- Huguinho
- Medina
- Danilo
- Montoro
- Arthur Cabral
- Danilo Pereira

Important current changes:
- Danilo returns from a muscular issue.
- Arthur Cabral returns from suspension.
- Kaio Pantaleão, Paulinho and Barrera remain unavailable.
- Tiquinho Soares is registered but not expected to be part of this matchday group because of conditioning/rhythm.

Interpretation:
Botafogo's midfield and forward structure is stronger than in the Athletico loss through Danilo/Arthur Cabral availability, but defensive absences remain.

## Current league state

### Flamengo
Entering Round 25:
- 2nd place
- 45 points from 23 matches
- 45 goals scored
- 21 conceded
- home: 6W, 3D, 1L
- home goals: 1.90 scored / 0.80 conceded per match

Recent league result:
- lost 2-1 at Cruzeiro
- Pedro scored at 22'
- Flamengo led 1-0 at halftime
- match xG around 1.01 Flamengo vs 1.41 Cruzeiro
- shots: 14 Flamengo vs 24 Cruzeiro
- corners: 3-3

Important defensive context:
Flamengo still own one of the league's best season defences, but current club reporting notes they have conceded in four consecutive matches and used the free week to address "avoidable goals."

### Botafogo
Entering Round 25:
- 11th place
- 30 points from 24 matches
- no win in three league matches entering the derby

Latest league:
- lost 3-2 at home to Athletico-PR
- conceded at 10' and 12'
- trailed 2-0 at halftime
- Santi Rodríguez scored twice late
- Botafogo generated heavy territorial pressure and 13 corners in one current stat feed

Previous recent league sequence included:
- 0-1 at Vitória
- 1-1 vs Fluminense
- 0-0 vs Grêmio
- 1-0 at Cruzeiro

Interpretation:
Botafogo's ordinary recent scoring environment has been lower than the 2-3 Athletico game, but the defensive process has become more volatile and today's attack is strengthened.

## Current-season direct meeting

2026 Série A:
- Botafogo 0-3 Flamengo
- HT: Botafogo 0-2 Flamengo
- goals: Samuel Lino 12', Léo Pereira 45+1', Pedro 48'
- Botafogo later went down to ten men
- corners: Botafogo 2, Flamengo 4

Interpretation:
The earlier derby strongly supports Flamengo's side/early-goal ceiling, but the red-card state means the 3-0 final cannot be transferred directly as a clean current-score coefficient.

## First-half process

Current phase evidence supporting 1H Over:
- March H2H: Flamengo goals at 12' and 45+1'
- Cruzeiro-Flamengo: Pedro scored at 22'
- Botafogo-Athletico: Athletico scored at 10' and 12'

Season context:
- Flamengo score about 0.83 first-half goals per league match overall
- at home Flamengo score before halftime in roughly 60% of current league matches
- Flamengo concede very little in first halves at home, so the strongest 1H-Over mechanism is a Flamengo goal rather than a balanced early shootout

Main 0-0 HT branch:
classic-derby caution, Botafogo protecting the central zone, and Flamengo patiently circulating rather than forcing early risk.

## Full-game goal process

Current season:
- Flamengo: ~1.96 scored / 0.91 conceded per match
- Botafogo: ~1.61 scored per match; away scoring around 1.42 in current specialist data
- Flamengo home: ~1.90 scored / 0.80 conceded
- Botafogo away defensive rate in current specialist sources is materially weaker than Flamengo's home defensive rate

Current tension:
- Flamengo's season defence supports 2-0 / 1-0 branches.
- But Flamengo have conceded in four straight and Botafogo restore Arthur Cabral/Danilo.
- Botafogo just conceded three and were 2-0 down within 12 minutes against Athletico.

## Corner process

Generated line:
### **Total Corners Over 8.5**

Current season/recent context:
- Flamengo matches: roughly 8.8 total corners per game in current season specialist data.
- Botafogo matches: roughly 9.8 total corners per game.
- Flamengo home profile: about 5.5 corners for and 3.7 against in one current dataset.
- Botafogo away profile: about 3.25 corners for and 5.83 conceded.
- Botafogo's last match produced a very high corner count, including 13 Botafogo corners.
- the March H2H produced only 6 total corners, demonstrating the low-corner kill path.

Mechanism supporting 9+:
- Flamengo's wide progression through Samuel Lino/Luiz Araújo plus fullback overlaps can generate blocked crosses and defensive clearances.
- Botafogo's Alex Telles/Vitinho width gives the away side a route to corners when chasing.
- if Flamengo score first, Botafogo may increase wide attack volume.

Kill path:
Flamengo score efficiently before sustained pressure develops, then control possession centrally; Botafogo fail to sustain attacks, reproducing the six-corner March pattern.

Provider cap:
exact corner provider/operator terms were not supplied, so this remains `FORCED RANK`.

## Weather

Near kickoff in Rio:
- around 27°C
- mostly sunny/humid at the current observation
- an INMET storm alert is active for the broader day

No immediate rain was observed at the frozen cutoff.

Treatment:
weather is not used as a directional goal signal. Heat/humidity can lower repeated pressing; storm risk can widen handling/crossing variance if conditions change later.

## Joint match tree

### Flamengo control + Over branch
Representative scores:
- Flamengo 3-0
- Flamengo 3-1
- Flamengo 2-1

Mechanisms:
- Flamengo score early through Pedro/Arrascaeta/Samuel Lino/Luiz Araújo
- Botafogo's defensive instability persists
- restored Botafogo attack either contributes one or forces a more open score-state

Favours:
- **1H Over 0.5**
- **FT Over 2.5**
- Flamengo winner

### Flamengo control + Under branch
Representative scores:
- Flamengo 2-0
- Flamengo 1-0
- 1-1

Mechanisms:
- Flamengo dominate territory but protect transitions better after recent defensive work
- Botafogo struggle to convert limited entries
- early lead lowers later match tempo

Favours:
- 1H Over can still win
- **FT Under 2.5**

### Competitive derby branch
Representative scores:
- Flamengo 2-1
- 1-1
- Botafogo 2-1

Mechanisms:
- Botafogo's restored midfield/front line improves possession retention
- Flamengo's defensive absences/recent concession streak remains relevant
- both teams generate one high-value transition/set-piece chance

Favours:
- FT total sits on/above boundary
- draw remains meaningful

### Slow opening branch
Representative:
- HT 0-0 -> Flamengo 1-0
- HT 0-0 -> 1-1
- HT 0-0 -> Flamengo 2-0

Favours:
- **1H Under 0.5**
- FT Under in most states

## P-210/V01 frozen ranking

| Rank | Pick | Verdict | Evidence |
|---:|---|---|---|
| **1** | **1H Over 0.5 Goals** | **LEAN** | **MEDIUM** |
| **2** | **FT Over 2.5 Goals** | **LEAN / THIN** | **MEDIUM-LOW** |
| **3** | **Total Corners Over 8.5** | **FORCED RANK — provider cap** | **MEDIUM-LOW** |
| **4** | **FT Under 2.5 Goals** | **FORCED RANK / strong counter-branch** | **MEDIUM-LOW** |
| **5** | **1H Under 0.5 Goals** | **AVOID / FORCED RANK** | **MEDIUM-LOW** |

## Ranking logic

### #1 — 1H Over 0.5
The strongest phase-specific evidence points toward one early goal:
- Flamengo led 2-0 at halftime in the March H2H.
- Flamengo scored at 22' against Cruzeiro.
- Botafogo conceded twice in the opening 12 minutes against Athletico.

Flamengo's confirmed attacking XI remains strong enough to create the first-half goal even without Plata.

Main kill path:
derby caution and Botafogo's compact midfield keep Flamengo circulating outside the box and the teams reach HT 0-0.

### #2 — FT Over 2.5
The central score family is 2-1 / 3-0 / 3-1.

Support:
- Flamengo average nearly two league goals per match.
- Botafogo's current defensive form is unstable.
- Flamengo have conceded in four straight.
- Arthur Cabral and Danilo return for Botafogo.
- the first H2H finished 3-0.

Why only thin:
Flamengo have a strong season defence, and a 2-0 home win remains one of the largest central counter-states.

### #3 — Total Corners Over 8.5
Current season match baselines cluster around 9-10 total corners and Botafogo's latest game produced heavy corner pressure.

Why not higher:
the exact March H2H produced only six corners, and corner count is highly score-state dependent. Provider terms are also unresolved.

### #4 — FT Under 2.5
Strongest Under states:
- Flamengo 1-0
- Flamengo 2-0
- 1-1

This is a meaningful branch because Flamengo's underlying season defence remains excellent and Botafogo's recent scoring floor is low.

It ranks below the Over because today's Botafogo attack is stronger than in several recent matches and Flamengo's current four-game concession streak widens the 2-1 state.

### #5 — 1H Under 0.5
The 0-0 halftime derby branch is real, but it is directly opposed by the March H2H and both teams' most recent first-half events.

## Potential winner

**Flamengo — LEAN / MEDIUM**

Primary reasons:
- materially stronger season performance
- 45 points vs Botafogo's 30
- home strength at the Maracanã
- stronger confirmed attacking spine
- Botafogo enter winless in three and with current defensive instability
- Flamengo won the first 2026 league H2H 3-0

Why not stronger:
- Flamengo have just lost at Cruzeiro
- they have conceded in four straight
- important defensive/midfield absences remain
- Botafogo restore Arthur Cabral and Danilo
- derby draw/upset branches cannot be dismissed

## Final freeze

1. **1H Over 0.5 Goals**
2. **FT Over 2.5 Goals**
3. **Total Corners Over 8.5**
4. **FT Under 2.5 Goals**
5. **1H Under 0.5 Goals**

Potential winner: **Flamengo — LEAN / MEDIUM**.

Central score corridor:
- Flamengo 2-1
- Flamengo 3-0
- Flamengo 2-0

Next canonical distinct event ID: **P-211**.


---

# P-211 — Jaime Faria vs Jenson Brooksby — US Open Men's Singles R1

## Event/state freeze

| Field | Frozen value |
|---|---|
| Competition | 2026 US Open — Men's Singles Round 1 / R128 |
| Event | Jaime Faria vs Jenson Brooksby |
| Venue | USTA Billie Jean King National Tennis Center — Stadium 17 |
| Surface | Outdoor hard |
| Format | Best of five sets |
| Order of play | Third match on Stadium 17 |
| Frozen cutoff | 2026-08-31 04:58:38 Australia/Melbourne / 2026-08-30 14:58:38 EDT |
| GAME-STATE | **PREGAME / NOT STARTED at cutoff** |
| Target | `TENNIS_JOINT_SET_GAME_TREE-v1` |
| Method | MDS-2026.08.30-v2.7 qualitative champion |
| Probability state | `NOT_GENERATED / NOT_PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Operator/retirement terms | NOT SUPPLIED / `UNKNOWN_DEFINITION` |

No information first known after the frozen cutoff may revise P-211/V01.

## Supplied contracts

1. Faria +0.5 Games
2. Brooksby -0.5 Games
3. Total Games Over 39.5
4. Total Games Under 39.5

### Settlement geometry
- Under 39.5 wins at **39 games or fewer**.
- Over 39.5 wins at **40 games or more**.
- There is no total-games push.
- A +0.5/-0.5 games handicap is based on total games won, not merely match winner. A player can theoretically win the match but lose the game handicap if the lost sets were sufficiently lopsided.
- Exact retirement/walkover treatment is unknown because the user's operator was not supplied.

## Current head-to-head

H2H: 1-1.

### Cincinnati 2026 — outdoor hard
Faria def. Brooksby 6-3, 6-2.

Match statistics:
- Faria 5 aces / 6 double faults
- Faria first serve in 57%
- Faria won 79% of first-serve points
- Faria won 60% of second-serve points
- Faria held 8/9 service games
- Faria broke Brooksby 4 times
- Brooksby won only 61% behind first serve and 39% behind second serve
- Brooksby held only 4/8 service games

This is the most relevant direct-match prior because it occurred on the same surface only about two weeks before the US Open.

### Roland Garros 2025 — clay
Brooksby def. Faria 6-1, 3-6, 6-3, 6-2.

This meeting is downweighted because it was on clay, more than a year earlier, and preceded the current North American hard-court regime.

Both historical H2Hs also finished below 39.5 total games:
- Cincinnati 2026: 17 games
- Roland Garros 2025: 33 games

These totals are descriptive, not independent probability estimates.

## Current hard-court regime

### Jaime Faria
Recent Cincinnati run:
- beat Brooksby 6-3, 6-2
- beat Ben Shelton 6-4, 6-4 for his first Top-10 win
- beat Adam Walton 4-6, 6-4, 7-6(3)
- lost to Lorenzo Musetti 5-7, 2-6

Interpretation:
Faria's current hard-court regime is materially stronger than ranking alone would imply. He has shown:
- strong first-strike serving when the first serve lands,
- good pressure on second serves,
- willingness to attack return games,
- enough resilience to win a deciding-set/tiebreak match against Walton.

Recent hard-court split from Tennis Abstract's rolling sample:
- hold around 73.6%
- break around 27.4%
- return points won around 38.0%
- first-serve points won around 73.5%
- second-serve points won around 48.0%

### Jenson Brooksby
Recent matches:
- beat Mpetshi Perricard 6-3, 6-2 in Winston-Salem
- lost to Stefanos Tsitsipas 4-6, 6-7(6), with a second-set set point and eight break-point chances overall
- lost to Faria 3-6, 2-6 in Cincinnati
- lost to Ben Shelton 3-6, 5-7 in Montreal
- beat Adam Walton 6-3, 6-4 in Montreal

Brooksby's current strength remains return disruption and baseline pressure. Against Mpetshi Perricard he broke four times and did not face a break point.

Recent hard-court split from Tennis Abstract's rolling sample:
- hold around 76.8%
- break around 20.3%
- return points won around 36.5%
- first-serve points won around 69.3%
- second-serve points won around 50.5%

Interpretation:
Brooksby has rebounded from the Cincinnati loss and his close Tsitsipas match is meaningful contrary evidence. Faria still owns the stronger same-surface direct result and the stronger recent high-end win through Shelton.

## Best-of-five / total-games geometry

### Why 39.5 is a high threshold
A straight-set match **cannot** go Over 39.5:
- even 7-6, 7-6, 7-6 = 39 games.

So Over 39.5 requires:
1. at least four sets, and
2. a fairly close four-set distribution, **or**
3. a sufficiently long five-set match.

Many ordinary four-set results remain Under:
- 6-4, 3-6, 6-3, 6-4 = 34
- 6-3, 4-6, 6-4, 6-4 = 35
- 7-5, 4-6, 6-3, 6-4 = 37

Four-set Over branches usually require multiple 7-5/7-6 sets or a generally tight game distribution.

### Current break/tiebreak implications
Both players can pressure return games:
- Faria's recent rolling hard-court break rate is stronger than Brooksby's.
- Brooksby remains a disruptive returner and generated eight break chances against Tsitsipas.

That raises the chance of sets being decided by breaks before 6-6 rather than repeated tiebreaks, which is favorable to the Under 39.5 relative to a pure hold-dominant matchup.

## Joint set/game tree

### Faria control branch
Representative scores:
- Faria 3-0: 6-4, 6-3, 6-4 — 29 games
- Faria 3-1: 6-4, 3-6, 6-3, 6-4 — 34 games
- Faria 3-1: 7-5, 6-3, 4-6, 6-3 — 36 games

Favours:
- Faria +0.5 Games
- Under 39.5

Mechanism:
Faria's Cincinnati second-serve pressure and stronger recent first-strike form persist; Brooksby struggles to protect enough service games to create repeated tiebreaks.

### Brooksby control branch
Representative scores:
- Brooksby 3-0: 6-4, 6-4, 6-3 — 29 games
- Brooksby 3-1: 6-4, 4-6, 6-3, 6-4 — 35 games
- Brooksby 3-1: 7-5, 6-3, 4-6, 6-3 — 36 games

Favours:
- Brooksby -0.5 Games
- Under 39.5

Mechanism:
Brooksby uses return depth/variation to reduce Faria's first-strike advantage and converts the break chances that were available against Tsitsipas.

### Close four-set branch
Representative scores:
- Faria 7-6, 6-7, 7-5, 6-4 — 48 games
- Brooksby 7-6, 5-7, 7-6, 6-4 — 47 games

Favours:
- Over 39.5
- game handicap depends on exact set margins

Mechanism:
both players protect serve more efficiently than their current rolling hold rates imply, and multiple sets reach 5-5/6-6.

### Five-set branch
Representative scores:
- Faria 6-4, 4-6, 7-5, 3-6, 6-4 — 51 games
- Brooksby 6-3, 4-6, 6-7, 6-3, 6-4 — 51 games

Favours:
- Over 39.5 in most ordinary five-set score distributions
- game handicap becomes materially less correlated with match winner

Mechanism:
Brooksby's return/baseline resilience prevents Faria control, while Faria's serve/forehand prevents Brooksby control.

## P-211/V01 frozen ranking

| Rank | Contract | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Under 39.5 Total Games** | **LEAN** | **MEDIUM** |
| **2** | **Faria +0.5 Games** | **LEAN / THIN** | **MEDIUM-LOW** |
| **3** | **Brooksby -0.5 Games** | **FORCED RANK / strong counter-branch** | **MEDIUM-LOW** |
| **4** | **Over 39.5 Total Games** | **FORCED RANK** | **MEDIUM-LOW** |

## Ranking logic

### #1 — Under 39.5
Structural reasons:
- every straight-set outcome is automatically Under;
- many ordinary four-set outcomes remain Under;
- both recent H2Hs were Under 39.5;
- the most relevant same-surface H2H was highly break-heavy rather than tiebreak-heavy;
- both players' current return pressure creates realistic 6-3/6-4 set families.

Main kill path:
Brooksby's recent rebound translates into a much tighter rematch and neither player can establish control, producing four close sets with several 7-5/7-6 scores or a five-set match.

### #2 — Faria +0.5 Games
Faria gets the side edge because:
- he beat Brooksby 6-3, 6-2 on the same surface only two weeks ago;
- he then beat Shelton and Walton;
- his recent hard-court return/first-serve profile is at least competitive and in several dimensions stronger;
- the Cincinnati matchup showed a direct second-serve and return-pressure advantage.

Why only thin:
Brooksby has since beaten Mpetshi Perricard cleanly and pushed Tsitsipas to a second-set tiebreak/set point. External markets remain close and often make Brooksby a slight favorite.

### #3 — Brooksby -0.5 Games
The best Brooksby pathway is a 3-1 or 3-0 win built through return pressure and forcing Faria into lower first-serve percentages.

Brooksby's rebound at Winston-Salem and close Tsitsipas loss prevent the Cincinnati result from being treated as permanent.

It ranks behind Faria because the direct current-surface matchup was decisively unfavorable and Faria's overall Cincinnati run was stronger.

### #4 — Over 39.5
The Over is viable if the match becomes a genuine four/five-set fight.

But it needs more simultaneous conditions:
- neither side achieves straight-set control;
- a four-set match must remain relatively close, or the match must extend to five;
- multiple sets must resist the break-rich 6-3/6-4 pattern.

That is less central than the Under branch.

## Potential winner

**Jaime Faria — LEAN / LOW-MEDIUM CONFIDENCE**

Primary reasons:
- decisive same-surface H2H win only two weeks ago;
- better recent Cincinnati run;
- first Top-10 win over Shelton;
- stronger recent second-serve-return pressure;
- ranking gap is small and not controlling.

Strongest failure path:
Brooksby adapts tactically from Cincinnati, extends rallies onto Faria's weaker second-serve/consistency phases, and reproduces his Winston-Salem return performance, leading to a Brooksby 3-1 or 3-2 win.

## External market challenger

Current market snapshots are close and inconsistent:
- several books/aggregators have Brooksby a small favorite;
- others have Faria essentially pick'em or marginally favored.

This disagreement is treated only as an external challenger. It reinforces that the side is much less robust than the Under 39.5 total-games thesis.

No internal value/EV claim is made.

## Final freeze

1. **Under 39.5 Total Games**
2. **Faria +0.5 Games**
3. **Brooksby -0.5 Games**
4. **Over 39.5 Total Games**

Potential winner: **Jaime Faria — LEAN / LOW-MEDIUM CONFIDENCE**.

Central match corridor:
- Faria 3-1
- Faria 3-0
- Brooksby 3-1 counterbranch

Next canonical distinct event ID: **P-212**.


---

# P-212 — McCartney Kessler vs Ekaterina Alexandrova — US Open Women R1

## Event/state freeze

| Field | Frozen value |
|---|---|
| Competition | 2026 US Open — Women's Singles Round 1 / R128 |
| Event | McCartney Kessler vs Ekaterina Alexandrova |
| Surface | Outdoor hard |
| Format | Best of three sets |
| Frozen cutoff | 2026-08-31 ~05:01 Australia/Melbourne / 2026-08-30 ~15:01 EDT |
| GAME-STATE | **PREGAME / NOT STARTED at cutoff** |
| Target | `TENNIS_JOINT_SET_GAME_TREE-v1` |
| Method | MDS-2026.08.30-v2.7 qualitative champion |
| Probability state | `NOT_GENERATED / NOT_PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Operator/retirement terms | NOT SUPPLIED / `UNKNOWN_DEFINITION` |

Multiple current match pages still showed the match as scheduled/not started at the frozen cutoff. No live point/game/set information is used.

## Supplied contracts

1. McCartney Kessler +2.5 Games
2. Ekaterina Alexandrova -2.5 Games
3. Total Games Over 21.5
4. Total Games Under 21.5

### Settlement geometry

- Over 21.5 wins at 22+ total games.
- Under 21.5 wins at 21 or fewer.
- No push is possible at 21.5.
- Kessler +2.5 can cash in a narrow loss and every Kessler match win.
- Alexandrova -2.5 requires a game-margin win of at least 3 games.
- Match winner and game handicap are not identical.
- Retirement/walkover settlement remains unknown because operator terms were not supplied.

## Ranking / seed context

- Ekaterina Alexandrova is the No. 18 US Open seed and around WTA No. 19.
- McCartney Kessler is around WTA No. 65.

Rankings are contextual only and do not independently control the forecast.

## Head-to-head

Alexandrova leads 1-0.

### Ningbo 2025 — hard
Alexandrova def. Kessler **6-3, 6-3**.

Implications:
- Alexandrova won by 6 games: Alexandrova -2.5 would have covered.
- Total was 18 games: Under 21.5 would have won.

This is relevant because it was a hard-court meeting, but it is downweighted for being nearly a year old and because both players' current regimes have changed.

## Current hard-court regime

### McCartney Kessler

Recent hard-court results:
- L Caty McNally 3-6, 4-6 — Cincinnati
- L Anna Kalinskaya 2-6, 7-6, 4-6 — Toronto
- W Cadence Brace 6-3, 6-3 — Toronto
- L Renata Zarazúa 4-6, 1-6 — Memphis

Important process:
- vs McNally, Kessler won only 54% of first-serve points and faced substantial return pressure.
- vs Kalinskaya, Kessler still forced a deciding set and won a tiebreak, showing a credible set-winning/length-extension branch against a strong opponent.
- Kessler's current hard form is therefore mixed: enough resilience to extend matches, but an unstable serve/second-serve floor against strong returners.

### Ekaterina Alexandrova

Recent hard-court results:
- L Clara Tauson 6-7, 6-4, 3-6 — Monterrey
- L Sara Bejlek 4-6, 6-1, 2-6 — Cincinnati
- W Anna Blinkova 6-7, 6-4, 7-5 — Cincinnati
- L Elina Svitolina 6-3, 0-6, 3-6 — Toronto
- W Aryna Sabalenka 7-6, 4-6, 6-4 — Toronto
- W Talia Gibson 5-7, 6-1, 6-3 — Toronto
- W Camila Osorio 6-3, 7-6 — Toronto

Important process:
- Alexandrova has repeatedly extended high-level hard-court matches into deciding sets.
- She recently defeated Sabalenka through aggressive return pressure.
- She has enough serve power to create short-set separation, but her recent match-to-match volatility and second-set swings widen the three-set branch.
- Her current opponent quality is substantially stronger than Kessler's recent slate.

### Match-length observation

Alexandrova's last seven completed hard-court matches listed above all reached **22 or more total games**:
- 32 vs Tauson
- 25 vs Bejlek
- 35 vs Blinkova
- 24 vs Svitolina
- 33 vs Sabalenka
- 28 vs Gibson
- 22 vs Osorio

This is descriptive only. The mechanism is more important:
Alexandrova has enough serve/first-strike quality to hold frequently, but enough return/serve volatility that one set often swings the opposite direction rather than producing repeated 6-2/6-3 control.

Kessler's recent matches have been shorter more often, so this is not treated as an automatic Over.

## Total-games geometry

### Straight-set Alexandrova control
Representative:
- 6-3, 6-3 = 18
- 6-4, 6-3 = 19
- 6-4, 6-4 = 20

Favours:
- Alexandrova -2.5
- Under 21.5

This is the exact H2H-like branch.

### Competitive straight sets
Representative:
- 7-5, 6-4 = 22
- 7-6, 6-3 = 22
- 7-6, 6-4 = 23

Favours:
- Over 21.5
- handicap depends on exact game margins

This branch matters because Kessler can pressure at least one set even if she does not win it.

### Three-set Alexandrova win
Representative:
- 6-4, 4-6, 6-3 = 35
- 7-5, 3-6, 6-3 = 36
- 6-3, 4-6, 6-4 = 35

Favours:
- Over 21.5
- Alexandrova -2.5 often but not always

### Kessler upset / three-set branch
Representative:
- Kessler 6-4, 4-6, 6-4 = 30
- Kessler 3-6, 6-4, 6-4 = 29

Favours:
- Kessler +2.5
- Over 21.5

## Joint set/game tree

### Alexandrova control
Representative score:
- Alexandrova 6-3, 6-3
- Alexandrova 6-4, 6-3

Mechanisms:
- Alexandrova attacks Kessler's second serve.
- Kessler struggles to generate enough first-strike points.
- Alexandrova's stronger recent opponent level translates into cleaner pressure points.

Favours:
- Alexandrova -2.5
- Under 21.5

### Competitive Alexandrova win
Representative:
- Alexandrova 7-5, 6-4
- Alexandrova 6-4, 4-6, 6-3

Mechanisms:
- Kessler serves well enough to stay close or take one set.
- Alexandrova's return/first-strike ceiling wins the match, but not through repeated early breaks.

Favours:
- Over 21.5
- Alexandrova winner
- handicap depends on exact game margin

### Kessler resistance/upset
Representative:
- Kessler 6-4, 4-6, 6-4
- Kessler 7-6, 4-6, 6-3

Mechanisms:
- home-crowd/comfort plus first-serve performance improves.
- Alexandrova's recent double-fault/serve-volatility branch appears.
- Kessler gets enough second-serve return pressure to create break chances.

Favours:
- Kessler +2.5
- Over 21.5

## P-212/V01 frozen ranking

| Rank | Contract | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Over 21.5 Total Games** | **LEAN** | **MEDIUM** |
| **2** | **Ekaterina Alexandrova -2.5 Games** | **LEAN / THIN** | **MEDIUM** |
| **3** | **McCartney Kessler +2.5 Games** | **FORCED RANK / strong counter-branch** | **MEDIUM-LOW** |
| **4** | **Under 21.5 Total Games** | **FORCED RANK / H2H-control branch** | **MEDIUM-LOW** |

## Ranking logic

### #1 — Over 21.5
The threshold can be cleared in:
- almost every ordinary three-set match;
- competitive straight sets such as 7-5, 6-4 or 7-6, 6-3.

Alexandrova's current hard-court regime has been unusually match-length heavy, with seven consecutive completed hard matches reaching at least 22 games. Kessler has shown enough resistance against Kalinskaya and other stronger opponents to preserve a close-set or set-winning branch.

Main kill path:
Alexandrova reproduces the Ningbo matchup, repeatedly attacks Kessler's second serve and wins 6-3, 6-3 / 6-4, 6-3.

### #2 — Alexandrova -2.5
Alexandrova owns:
- the ranking/seed edge;
- the only H2H, won 6-3, 6-3;
- stronger current opponent quality;
- recent wins over Sabalenka, Gibson, Osorio and Blinkova;
- a more dangerous aggressive-return pathway against Kessler's current serve instability.

Why below the Over:
Alexandrova can win a close three-set or two-tiebreak match without covering -2.5.

### #3 — Kessler +2.5
Kessler covers every outright win and narrow game-margin loss.

Her strongest current evidence is:
- taking Kalinskaya to three sets;
- a straight-set Toronto win;
- home-major familiarity.

Main problem:
the previous H2H was a clean six-game Alexandrova margin, and Kessler has recently lost by five games to both McNally and Kalinskaya despite extending the latter to three sets.

### #4 — Under 21.5
The Under is coherent if Alexandrova controls:
- 6-3, 6-3
- 6-4, 6-3
- 6-4, 6-4

The prior H2H is exactly this type.

It ranks fourth because Alexandrova's current regime has been far more three-set/close-set heavy than that older Ningbo match, while Kessler's best path to competing naturally extends the game count.

## Potential winner

**Ekaterina Alexandrova — LEAN**

Primary reasons:
- No. 18 seed / current top-20 ranking.
- 1-0 H2H with a 6-3, 6-3 hard-court win.
- substantially stronger recent opponent quality.
- Toronto run included a win over Sabalenka.
- aggressive return style directly tests Kessler's less-stable current service games.

Strongest failure path:
Kessler raises her first-serve percentage and first-strike efficiency in the home Slam environment, while Alexandrova's recent serve volatility/double-fault branch returns; Kessler then turns one tight set into a deciding-set upset.

## External market challenger

Current public pricing generally makes Alexandrova the favorite, but not an overwhelming one. This broadly agrees with:
- Alexandrova as the preferred winner;
- Kessler retaining enough competitive probability to keep Over 21.5 viable.

No internal probability/EV/value claim is published.

## Final freeze

1. **Over 21.5 Total Games**
2. **Ekaterina Alexandrova -2.5 Games**
3. **McCartney Kessler +2.5 Games**
4. **Under 21.5 Total Games**

Potential winner: **Ekaterina Alexandrova — LEAN**.

Central match corridor:
- Alexandrova 2-1
- Alexandrova 2-0 with at least one close set
- Kessler 2-1 counterbranch

Next canonical distinct event ID: **P-213**.


---

## Administrative re-check — P-211 duplicate request — 2026-08-31

The user re-requested the already-issued event:

**P-211 — Jaime Faria vs Jenson Brooksby — US Open Men's Singles Round 1**

No new canonical event ID is consumed.

### Current state at re-check
- Australia/Melbourne local time at re-check: approximately 05:07 on 2026-08-31.
- Current tournament-bracket feed marked the match **LIVE**, with Faria leading **2-0 in games** at the observed snapshot.
- Tennis.com remained stale at **Upcoming**, so current-state feeds were not perfectly aligned.

### Controlling forecast
The immutable pregame `P-211/V01` remains controlling. It was frozen before the match began and is **not revised using current live information**.

Frozen P-211/V01 ranking:
1. **Under 39.5 Total Games — LEAN, MEDIUM**
2. **Faria +0.5 Games — LEAN / THIN, MEDIUM-LOW**
3. **Brooksby -0.5 Games — FORCED RANK / strong counter-branch, MEDIUM-LOW**
4. **Over 39.5 Total Games — FORCED RANK, MEDIUM-LOW**

Potential winner:
**Jaime Faria — LEAN / LOW-MEDIUM CONFIDENCE**

No retrospective or settlement was performed.


---

# P-213 — Toby Samuel vs Tomas Machac — US Open Men's Singles R1

## Event/state freeze
- Competition: 2026 US Open — Men's Singles Round 1 / R128
- Event: Toby Samuel vs Tomas Machac
- Venue: USTA Billie Jean King National Tennis Center — Court 10
- Surface: Outdoor hard
- Format: Best of five sets
- Frozen cutoff: 2026-08-31 ~05:10 Australia/Melbourne / 2026-08-30 ~15:10 EDT
- GAME-STATE: PREGAME / NOT STARTED at cutoff
- Target: `TENNIS_JOINT_SET_GAME_TREE-v1`
- Probability state: `NOT_GENERATED / NOT_PUBLISHED — VALIDATION PENDING`
- Value state: `NO VALUE DETERMINABLE`
- Operator retirement/walkover terms: `UNKNOWN_DEFINITION`

No live point/game/set information is used.

## Supplied contracts
1. Toby Samuel -2.5 Games
2. Tomas Machac +2.5 Games
3. Over 39.5 Total Games
4. Under 39.5 Total Games

## Current context

### Toby Samuel
- Qualifier; around ATP No. 110-113 in current sources.
- Three Challenger titles in 2026; latest Winnipeg title won without dropping a set.
- Qualified for the US Open by beating:
  - Francesco Maestrelli 6-7, 6-3, 6-1
  - Billy Harris 4-6, 6-1, 6-4
  - Cristian Garin 4-6, 6-4, 5-0 RET
- Q1 vs Maestrelli:
  - 67% first serve in
  - 74% first-serve points won
  - 58% second-serve points won
  - held 13/14 service games
  - broke 5 times
- Q2 vs Harris:
  - held 10/14
  - broke 6 times
  - won 64% of Harris second-serve return points
- Q3 vs Garin:
  - 76% first serve in
  - won 63% on both first and second serve
  - converted all 5 break points
- Tennis Abstract current hard-court sample is very strong, but materially Challenger/qualifying weighted and therefore shrunk for ATP-main-draw opponent quality.
- Best-of-five evidence is limited, but Samuel pushed Jakub Mensik to five sets at Wimbledon 2026.

### Tomas Machac
- Around ATP No. 58-62 in current sources; career high No. 20.
- Higher ATP-main-draw baseline and substantially more top-level experience.
- Won Adelaide 2026, but current North American return has been poor:
  - Cincinnati: lost 3-6, 2-6 to Pablo Carreno Busta
  - Winston-Salem: lost 2-6, 6-7(1) to Mees Rottgering
- vs Carreno Busta:
  - 57% first serve in
  - 60% first-serve points won
  - 47% second-serve points won
  - held only 3/8 service games
- vs Rottgering:
  - 56% first serve in
  - 69% first-serve points won
  - only 40% second-serve points won
  - 7 double faults
  - held 7/10 service games
  - converted only 1/7 break points
- Machac missed the grass season, including Wimbledon, because of a left-foot/heel injury. Current sources do not list an active injury at the US Open, so this is treated as comeback/form uncertainty rather than a confirmed current injury downgrade.
- Tennis Abstract current hard sample shows a stronger ATP-level hold profile than Samuel's main-draw Grand Slam sample, but weaker current return effectiveness and only roughly break-even recent hard-court results.

## H2H
- No prior Samuel-Machac meeting found.
- This is a first-meeting matchup; no H2H shortcut is used.

## Level adjustment
Samuel's hard-court results and hold/break numbers are excellent, but a large share comes from Challenger and qualifying opposition.
Machac's baseline comes from substantially stronger ATP main-draw competition.

Therefore:
- Samuel's raw 2026 hard win rate/break rate is shrunk downward.
- Machac's ranking/main-tour baseline is not allowed to override his poor current comeback form.
- The forecast is based on the intersection: rising Samuel hard-court regime versus higher-ceiling but unstable Machac return.

## Best-of-five total-games geometry

### Automatic Under branch
Every 3-0 score is Under 39.5.
Even the maximum three-set score:
- 7-6, 7-6, 7-6 = 39 games.

### Ordinary four-set Under examples
- 6-4, 3-6, 6-3, 6-4 = 34
- 7-5, 4-6, 6-3, 6-4 = 37
- 6-3, 4-6, 7-5, 6-3 = 36

### Over branch
Over 39.5 usually requires:
- a close four-set match with multiple 7-5/7-6 sets, or
- a five-set match.

This is why Under can win whether Samuel controls or Machac controls.

## Joint set/game tree

### Samuel control
Representative:
- Samuel 6-4, 6-3, 6-4 (3-0)
- Samuel 6-4, 3-6, 6-3, 6-4 (3-1)

Mechanisms:
- Samuel's current return pressure attacks Machac's second serve.
- Machac's comeback serving instability persists.
- Samuel's qualifying confidence/fitness carries into the main draw.

Favours:
- Samuel -2.5
- Under 39.5

### Machac control
Representative:
- Machac 6-4, 6-4, 6-3
- Machac 6-4, 4-6, 6-3, 6-4

Mechanisms:
- ATP-level shot quality/return depth exposes Samuel's level jump.
- Machac's first serve stabilises.
- Samuel's qualifying workload and weaker best-of-five main-draw experience matter.

Favours:
- Machac +2.5
- Under 39.5

### Narrow Samuel win
Representative:
- Samuel 7-6, 4-6, 6-4, 6-4
- Samuel 6-4, 1-6, 6-4, 6-4
- Samuel 3-2 in five close sets

Implication:
- Samuel can win the match while failing -2.5 games.
- Machac +2.5 retains important cover pathways.

### Long competitive branch
Representative:
- 7-6, 6-7, 7-5, 6-4
- five-set 3-2 either way

Favours:
- Over 39.5
- handicap depends on exact set margins.

## P-213/V01 frozen ranking
1. **Under 39.5 Total Games — LEAN, MEDIUM**
2. **Tomas Machac +2.5 Games — LEAN / THIN, MEDIUM-LOW**
3. **Toby Samuel -2.5 Games — FORCED RANK / strong counter-branch, MEDIUM-LOW**
4. **Over 39.5 Total Games — FORCED RANK, MEDIUM-LOW**

## Ranking logic

### #1 Under 39.5
Broadest structural path:
- every straight-set result wins;
- many ordinary four-set results win;
- current matchup contains meaningful break-rich/serve-instability routes on both sides.

Main kill path:
neither player establishes control and the match becomes a close four-set or five-set contest.

### #2 Machac +2.5
This is not the same as preferring Machac to win.
The cushion wins:
- every Machac victory;
- narrow Samuel wins by two or fewer net games.

Because the match-winner edge is only slight toward Samuel after level adjustment, the +2.5 cushion has broad settlement coverage.

Main kill path:
Samuel's current return edge is real enough to create a clean 3-0/3-1 win with 3+ net games.

### #3 Samuel -2.5
Samuel is the preferred match winner because:
- current hard-court form is materially better;
- he qualified strongly;
- Machac has two poor August comeback losses;
- Machac's current second-serve/DF profile is vulnerable.

Why only third:
Samuel must win the total game count by at least three, and a narrow 3-1/3-2 Samuel match win can fail the handicap.

### #4 Over 39.5
Requires a longer and more balanced match state:
- close four sets, or
- five sets.

That branch is credible because Machac retains higher-level ATP ability and Samuel has already demonstrated five-set competitiveness at Wimbledon, but it requires more simultaneous resistance than the Under branch.

## Potential winner
**Toby Samuel — LEAN / LOW-MEDIUM CONFIDENCE**

Primary reasons:
- stronger current hard-court form;
- three Challenger titles in 2026;
- strong US Open qualifying serve/return output;
- Machac's poor first two comeback matches after a foot/heel injury layoff.

Strongest failure path:
Machac's ATP-level baseline reasserts itself, his serve stabilises, and Samuel's Challenger/qualifying numbers fail to transfer cleanly to a higher-level best-of-five matchup.

## External challenger
Current public projection is close and has Samuel as a modest favorite despite Machac's higher ranking. This is used only as a challenger/sanity check, not as an internal probability.

## Final freeze
1. Under 39.5 Total Games
2. Tomas Machac +2.5 Games
3. Toby Samuel -2.5 Games
4. Over 39.5 Total Games

Potential winner: Toby Samuel — LEAN / LOW-MEDIUM CONFIDENCE.

Next canonical distinct event ID: **P-214**.


---

# P-214 — Baltimore Orioles @ Athletics — MLB

## Event / state freeze

| Field | Frozen value |
|---|---|
| Competition | MLB — 2026 regular season |
| Event | Baltimore Orioles @ Athletics |
| Venue | Sutter Health Park, West Sacramento, California |
| Scheduled first pitch | 2026-08-30 13:05 PDT / 16:05 EDT / 2026-08-31 06:05 Australia/Melbourne |
| Frozen cutoff | ~2026-08-30 12:43 PDT / 2026-08-31 05:43 Australia/Melbourne |
| GAME-STATE | **PREGAME** |
| Baltimore starter | Chris Bassitt — RHP — `PROBABLE_OFFICIAL` |
| Athletics starter | Jeffrey Springs — LHP — `PROBABLE_OFFICIAL` |
| Target | `BASEBALL_JOINT_FINAL_RUNS-v1` |
| Method | current active qualitative baseball framework |
| Probability state | `NOT_GENERATED / NOT_PUBLISHED — VALIDATION PENDING` |
| Value state | `NO VALUE DETERMINABLE` |
| Operator/listed-pitcher/action terms | NOT SUPPLIED |

MLB's official scoreboard still showed this as a preview/pregame event at the frozen cutoff. No live pitch, base/out or score information is used.

## Supplied contracts

1. Orioles -1.5
2. Athletics +1.5
3. Over 10.0 Runs
4. Under 10.0 Runs

### Contract geometry

Working assumption:
- run lines include extra innings;
- full-game total includes extra innings;
- exact operator listed-pitcher/action/shortened-game rules are unknown.

At exactly **10 runs**:
- Over 10.0 = PUSH
- Under 10.0 = PUSH

Athletics +1.5 wins on:
- every Athletics win;
- every one-run Orioles win.

It loses only on a Baltimore win by 2+.

## Official starter state

### Chris Bassitt — Baltimore
Official MLB current line:
- 5-4
- 4.74 ERA
- 51 SO

Current August MLB starts:
- Aug. 14 at Tampa Bay: 5.1 IP, 2 ER
- Aug. 19 vs Yankees: 5.2 IP, 3 ER
- Aug. 25 at St. Louis: 6.2 IP, 1 ER

August aggregate:
- 17.2 IP
- 19 H
- 6 ER
- 2 HR
- 4 BB
- 14 SO
- **3.06 ERA**
- ~1.30 WHIP

Important regime note:
Bassitt's season ERA remains mediocre, but his current post-IL/start sequence is materially better. The framework therefore keeps both:
- shrunk season-average branch;
- improved current-regime branch.

Central exposure:
roughly 5-6+ innings if efficient.

### Jeffrey Springs — Athletics
Official MLB current line:
- 3-12
- 6.08 ERA
- 92 SO

Recent MLB starts after his latest return:
- Aug. 19 vs Kansas City: 5.2 IP, 2 ER
- Aug. 24 at Minnesota: 4.2 IP, 4 ER

August aggregate:
- 10.1 IP
- 12 H
- 6 ER
- 2 HR
- 5 BB
- 4 SO
- **5.23 ERA**
- **1.65 WHIP**

Important wider regime:
- June ERA: 10.00
- July ERA: 8.59
- Springs has allowed heavy traffic and HR/contact damage over a much longer recent stretch than his two-start August sample.

Central exposure:
roughly 4.2-5.2 innings, with a meaningful early-hook/contact branch.

## Lineups

MLB's field-owning starting-lineup page still displayed **TBD** for both clubs at the frozen cutoff.

Same-day secondary sources consistently reported:

### Baltimore
1. Blaze Alexander — 2B
2. Pete Alonso — DH
3. Gunnar Henderson — SS
4. Coby Mayo — 1B
5. Christian Encarnacion-Strand — 3B
6. Leody Taveras — RF
7. Christian Franklin — LF
8. Carlos Narváez — C
9. Colton Cowser — CF

### Athletics
1. Henry Bolte — CF
2. Jeff McNeil — DH
3. Zack Gelof — 3B
4. Lawrence Butler — RF
5. Donovan Walton — 2B
6. Tommy White — 1B
7. Carlos Cortes — LF
8. Brian Serven — C
9. Alika Williams — SS

Because MLB had not yet populated the official batting orders, these lineups are treated as **secondary-confirmed only**. Participant-sensitive confidence is capped.

## Platoon / current offense

### Orioles vs LHP
Recent 30-day StatMuse split:
- OPS about **.718**
- .242 AVG / .302 OBP / .416 SLG
- 13 HR in the split sample

Interpretation:
Baltimore is competent against left-handed pitching, but not so dominant that Springs' 6.08 ERA automatically produces a blowout.

### Athletics vs RHP at home
Recent 30-day StatMuse split:
- OPS roughly **.754-.758**
- AVG about .265-.268
- SLG about .427-.435

Interpretation:
The Athletics' overall record understates their current home offensive ability against right-handers. This is a direct reason not to treat Bassitt's starter edge as an automatic Baltimore -1.5 cover.

## Series state

Baltimore has won the first two:
- Aug. 28: Orioles 4-3 Athletics in 10 innings
- Aug. 29: Orioles 5-3 Athletics

Important mechanisms from those games:
- Oakland had several missed scoring opportunities.
- In Game 2 the Athletics went 2-for-8 with RISP and left 11 runners on base.
- Baltimore's bullpen preserved both close games but accumulated substantial workload.
- The first two game totals were **7 and 8**, both below today's 10.0 line.

Those finals are context only; they do not replace the current starter/park/bullpen matchup.

## Bullpen state

### Baltimore
Across the first two games, Baltimore used a large portion of the relief group.

Saturday after Shane Baz:
- Alex Hoppe
- Rico Garcia
- Yennier Cano
- Cam Sanders
- Andrew Kittredge

Friday's extra-inning game also required late relief, including Kittredge/Hoppe and other leverage work.

Current external bullpen tracker before the finale had:
- Cam Sanders in a likely-unavailable/high-usage state;
- Kittredge, Hoppe, Garcia, Cano and Anthony Nunez all carrying recent usage flags;
- Grant Wolfram / Josh Walker among cleaner-rest alternatives.

Interpretation:
Baltimore's bullpen is **quality-capable but materially used**. Freshness is not treated as quality; the key issue is narrower manager choice and a wider middle-relief branch if Bassitt exits before the seventh.

### Athletics
Oakland's bullpen has also worked, but some leverage/alternative arms entered the finale with cleaner rest.

Saturday's late damage included José Suarez in his return from injury; the Athletics still retain alternative relief branches, including Elvis Alvarado.

Interpretation:
Oakland's bullpen is not pristine, but Baltimore appears to have the more compressed late-game usage tree.

## Park / weather

Baseball Savant 2026 one-year park factors:
- Sutter Health Park overall park factor: roughly **113-114**
- run factor: roughly **128-130**
- HR factor: roughly **125-129**
- for right-handed hitters the current run/HR environment is even more elevated.

This is one of the most run-enhancing parks in MLB in 2026.

National Weather Service / current conditions near game time:
- sunny
- roughly 83°F at 1 PM, rising toward upper 80s
- light SW wind around 3-6 mph
- no precipitation signal

Mechanistic treatment:
- warm/dry air modestly supports carry;
- weak wind does not force a directional adjustment;
- park is a genuine Over-tail amplifier;
- weather is not independently enough to override a 10-run line.

## Joint run tree

### Central Baltimore narrow-win branch
Representative scores:
- Orioles 5-4
- Orioles 6-4
- Orioles 5-3

Mechanisms:
- Bassitt works 5-6 effective innings.
- Springs allows 3-4 before exiting.
- Oakland's offense produces enough traffic against Bassitt/Baltimore relief to remain close.
- Orioles' late bullpen usage limits a clean shutdown.

Contract implications:
- Athletics +1.5 wins at 5-4
- Orioles -1.5 wins at 6-4 / 5-3
- Under wins at 5-4 / 5-3
- exactly 6-4 = 10-run PUSH

### Athletics upset / close branch
Representative scores:
- Athletics 5-4
- Athletics 6-5
- Athletics 5-3

Mechanisms:
- Athletics' strong recent home-vs-RHP split translates.
- Bassitt's season-average traffic branch returns.
- Baltimore's used bullpen gives up a late cluster.
- Springs survives 5 innings without a large HR inning.

Favours:
- **Athletics +1.5**
- Over only in 6-5; Under in 5-4 / 5-3

### Baltimore separation branch
Representative scores:
- Orioles 7-3
- Orioles 7-4
- Orioles 8-3

Mechanisms:
- Springs' June/July contact-HR regime reappears.
- Baltimore's right-handed/mixed lineup punishes the lefty.
- Athletics' bullpen inherits traffic.
- Bassitt keeps Oakland at 3-4 runs.

Favours:
- **Orioles -1.5**
- 7-3 = total PUSH
- 7-4 / 8-3 = **Over**

### Low-run branch
Representative scores:
- Orioles 5-3
- Orioles 4-3
- Athletics 5-3

Mechanisms:
- Bassitt's August form persists.
- Springs lands in his better post-return branch.
- RISP sequencing remains inefficient.
- leverage relievers suppress late clusters.

Favours:
- **Under 10.0**
- Athletics +1.5 in one-run outcomes

### High-run / bullpen-cluster branch
Representative scores:
- Orioles 8-5
- Orioles 7-5
- Athletics 7-6

Mechanisms:
- Springs exits early.
- Bassitt does not reach six.
- both bullpens inherit traffic.
- Sutter's run/HR environment amplifies one multi-run inning.

Favours:
- **Over 10.0**

## P-214/V01 frozen ranking

| Rank | Contract | Verdict | Evidence |
|---:|---|---|---|
| **1** | **Athletics +1.5** | **LEAN** | **MEDIUM** |
| **2** | **Under 10.0 Runs** | **LEAN / THIN** | **MEDIUM-LOW** |
| **3** | **Orioles -1.5** | **FORCED RANK / strong separation branch** | **MEDIUM-LOW** |
| **4** | **Over 10.0 Runs** | **FORCED RANK / upper-tail branch** | **MEDIUM-LOW** |

## Ranking logic

### #1 — Athletics +1.5
This is the broadest side contract:
- every Athletics win cashes;
- every one-run Baltimore win cashes.

Support:
- first two games were decided by 1 and 2 runs;
- Oakland has a strong recent home-vs-RHP OPS;
- Baltimore's bullpen is heavily used;
- Athletics have home last-bat;
- Bassitt's current edge does not erase the Athletics' late-game scoring branch.

Main kill path:
Springs' poor contact/HR regime reappears while Bassitt holds Oakland down, creating a 6-3 / 7-3 / 7-4 Baltimore separation.

### #2 — Under 10.0
A 10.0 total gives the Under useful boundary protection:
- 9 or fewer = WIN
- exactly 10 = PUSH
- 11+ = LOSS

The first two series games totaled only 7 and 8. Bassitt is in his best current 2026 stretch, and Oakland has repeatedly failed to convert traffic efficiently.

Central states such as 5-4 / 5-3 / 4-3 are Under, while 6-4 is only a push.

Why only thin:
Sutter Health Park is extremely run-friendly, Springs has a major contact/HR tail, and Baltimore's bullpen workload leaves a legitimate 11+ run branch.

### #3 — Orioles -1.5
Baltimore has the stronger winner/separation case:
- starter edge through Bassitt's current form;
- Springs' season-long struggle;
- better overall team;
- 2-0 series lead;
- playoff urgency and stronger offensive depth.

The clean cover family is 6-3 / 7-3 / 7-4.

Why below Oakland +1.5:
the run line demands a 2+ run win, while a substantial part of the central distribution remains Baltimore by exactly one.

### #4 — Over 10.0
The Over has strong environmental support:
- Sutter is one of MLB's strongest 2026 run/HR parks;
- game-time temperatures are warm;
- Springs can create an early-hook branch;
- both relief chains have usage/quality uncertainty.

But **11 runs are required to win**. A 6-4 or 5-5 regulation state only pushes at 10.

That makes the Over less robust than the Under despite the hitter-friendly environment.

## Potential game winner

**Baltimore Orioles — LEAN**

Primary reasons:
- Bassitt current starter edge
- Springs' 6.08 ERA / 1.50+ WHIP environment
- Orioles are the substantially better team by record
- Baltimore has won the first two games
- Baltimore has more lineup depth against a struggling left-handed starter

Why only LEAN:
- Oakland has hit RHP well at home recently;
- Baltimore's bullpen is heavily used;
- Sutter Health Park widens Oakland's HR/extra-base-hit comeback branch;
- the reported orders were not yet MLB-field-owner confirmed at cutoff.

## Final freeze

1. **Athletics +1.5**
2. **Under 10.0 Runs**
3. **Orioles -1.5**
4. **Over 10.0 Runs**

Potential winner: **Baltimore Orioles — LEAN**.

Central score corridor:
- Orioles 5-4
- Orioles 6-4
- Orioles 5-3
- Athletics 5-4 counterbranch

Next canonical distinct event ID: **P-215**.

---

# Independent canonical audit appendix — 2026-08-31

> **AUTHORITY AND PROVENANCE NOTICE:** Everything above this marker is the supplied Mini Log 5 source preserved as evidence. Its embedded instructions, method labels, queue snapshots and claimed issue times do not control current work. The top snapshot in `PREDICTION_LOG_COMBINED.md` is the sole queue and next-ID authority. This appendix records an independent state, settlement, provenance, source and method audit; it does not rewrite any frozen forecast.

## A. Artifact and eligibility audit

| Artifact | First locally demonstrable time | Bytes | SHA-256 | Treatment |
|---|---|---:|---|---|
| Supplied `PREDICTION_MINI_LOG_5_P214.md` | 2026-08-31 13:27:53 Australia/Sydney | 256,444 | `906186D4094D29E33799130CCA619621F088095AF19BCA2489DA2677DF6F1EB7` | Preserved byte-for-byte before this appendix |
| Supplied `deep-research-report (5).md` | 2026-08-31 14:07:05 Australia/Sydney | 37,847 | `FBC32F15DA7359B1BB0B7FE174213BD8879E49B33CE548C5157067ADC8719C46` | Supporting retrospective evidence only; its claims were independently checked |

The Mini Log 5 artifact first became demonstrable after every P-187–P-214 result. No earlier section-inclusive immutable receipt was supplied or recovered. Therefore every actionable view in this component is `E1-Q-LATE_IMPORT`, regardless of the issue time written inside the file.

The correct distinction is:

- **27 actionable events descriptively settled**;
- **0 prospective performance-eligible events**;
- **118 dependent contract rows descriptively graded: 58 WIN / 60 LOSS**;
- Rank #1: **12 WIN / 15 LOSS**;
- potential winner: **15 correct / 12 incorrect**;
- P-192: **closed no-action rainout**, excluded from the actionable-event and row ledgers.

These counts are an arithmetic and process audit, not a betting win rate. They may not be used for calibration, model selection, forecast-weight fitting, test completions, accuracy, edge, ROI or profitability claims. The supplied deep-research report's phrase “performance-eligible forecasts” is corrected here to **actionable late-import forecasts**.

## B. State and queue result

All events in this component have been checked first for live status. **There are no live P-187–P-214 events.** P-192 was cancelled before first pitch and had no actionable V01; a rescheduled fixture must receive a fresh state/participant/contract freeze and a new canonical distinct-event card rather than being carried as a live P-192 forecast.

The active follow-up queue after this audit contains no live event and ten final-event evidence/definition items:

1. P-126 field-owner result/phase confirmation and P-126-C06 corners unresolved;
2. P-148-C02 unresolved;
3. P-149-C02 provisional win;
4. P-151-C02 strong provisional win;
5. P-162 provisional final pending field owner;
6. P-166 operator overtime/action definition unknown;
7. P-176-C05 unresolved;
8. P-178-C05 unresolved;
9. P-179-C05 provisional win;
10. P-200 operator overtime/shootout/action definition unknown.

**Next canonical distinct event ID: `P-215`.**

## C. Reconciled descriptive ledger

| ID | Verified final / state | Rows | Rank #1 | Potential winner | Settlement/process note |
|---|---|---:|---|---|---|
| P-187 | Jamaica Kingsmen won by 7 runs, DLS; TKR 180/6, PP 60/0 | 2–2 | LOSS | LOSS | Both Overs won. DLS affected the chase, not the frozen TKR phase totals. |
| P-188 | Yankees 9–2 Red Sox | 2–2 | LOSS | WIN | Five-run eighth realised the one-sided relief/separation tail. |
| P-189 | Howard 31–24 Alabama A&M | 2–2 | LOSS | LOSS | A&M led late; Howard's 51-yard TD realised the underweighted explosive branch. |
| P-190 | Dragons 22–18 Warriors | 2–2 | WIN | LOSS | Under and Dragons cushion were right; two late tries flipped winner allocation. |
| P-191 | Carlton 48–42 Fremantle | 2–2 | LOSS | WIN | Winner right; margin and total allocation wrong in strongly directional wind. |
| P-192 | Cancelled before first pitch because of rain | N/A | N/A | N/A | `EXCLUDED — NO ACTIONABLE V01`; not live and not unsettled. |
| P-193 | Richmond 38–33 Essendon | 2–2 | LOSS | LOSS | Under won but favourite covered through late territory. |
| P-194 | Kaiserslautern 2–1 St. Pauli; HT 0–1; St. Pauli corners 4–5 Kaiserslautern | 2–3 | LOSS | LOSS | Scoreless streak was over-weighted; St. Pauli volume did not imply result or 6+ corners. |
| P-195 | Gent 2–1 Club Brugge; HT 1–1; Gent corners 1–5 Club Brugge | 2–3 | WIN | LOSS | First-half mechanism succeeded; Club corner and winner allocation failed. |
| P-196 | DR Congo 77–75 Egypt | 2–2 | LOSS | LOSS | Large-favourite centre failed; total crossed 151.5 by 0.5. |
| P-197 | Feyenoord 2–2 ADO; HT 0–1; Feyenoord corners 11–3 ADO | 2–3 | WIN | LOSS/draw | Goal branches worked; trailing-state attack destroyed the Feyenoord corner Under. |
| P-198 | Germany 96–94 Poland after OT; regulation 83–83 | 2–2 | WIN | WIN | Side/winner right; Over 180.5 won only through overtime. |
| P-199 | Frederikshavn 7–3 Sønderjyske | 2–2 | LOSS | LOSS | Unconfirmed goalie/early-season uncertainty was incompatible with a top-ranked Under. |
| P-200 | Herning 4–3 Rungsted after a 3–3 regulation tie | 2–2* | LOSS* | WIN* | `*` Research grade assumes OT/SO inclusion; exact operator terms remain unknown. |
| P-201 | Freiburg 4–1 Werder; HT 2–0; 11 corners | 3–2 | WIN | WIN | Goal process was coherent; corner Under missed by one. |
| P-202 | Randers 2–1 AGF; HT 2–0; AGF 5 corners | 2–3 | WIN | LOSS | Early-goal branch worked; AGF winner/corner allocation did not. |
| P-203 | Deportivo 3–1 Valencia; HT 2–1; Deportivo corners 5–5 Valencia | 3–2 | LOSS | WIN | Verified halftime was 2–1, not 3–0. Under 10.5 corners won on a verified total of 10. |
| P-204 | Yankees 16–1 Red Sox | 2–2 | WIN | LOSS | Broad Yankees +1.5 survived a badly wrong Boston winner call; cluster tail dominated. |
| P-205 | Twins 5–1 White Sox | 2–2 | WIN | WIN | Starter-length/opener-bulk distinction and low-total direction both held. |
| P-206 | Dodgers 6–1 Tigers | 2–2 | LOSS | WIN | Under 7.5 won while Tigers +1.5 lost: low total did not imply close margin. |
| P-207 | Inter 1–0 Cagliari; Inter 6 corners | 3–2 | LOSS | WIN | Inter chance/territory dominance was real, but the full-match Over required conversion and opponent contribution. |
| P-208 | Lazio 1–0 Genoa; HT 1–0; Lazio corners 4–2 Genoa | 2–3 | WIN | WIN | Low-score/winner read held; generic corner Over failed. |
| P-209 | Santos 1–0 Corinthians; HT 0–1; Corinthians corners 8–1 Santos | 3–2 | WIN | LOSS | Early goal and total-corner row won; possession/territory did not secure Corinthians. |
| P-210 | Flamengo 3–0 Botafogo; HT 1–0; Flamengo corners 5–3 Botafogo | 2–3 | WIN | WIN | Goal/winner mechanisms held; eight corners left Over 8.5 short. |
| P-211 | Faria d. Brooksby 6–3, 7–6(4), 4–6, 1–6, 6–2; 47 games | 2–2 | LOSS | WIN | Best-of-five extension was underweighted. |
| P-212 | Alexandrova d. Kessler 6–2, 6–2; 16 games | 2–2 | LOSS | WIN | Winner/handicap thesis conflicted with the top-ranked Over absent a competitive-set mechanism. |
| P-213 | Samuel d. Macháč 6–2, 6–3, 6–2 | 2–2 | WIN | WIN | Current surface/form and return pressure coherently supported winner, handicap and Under. |
| P-214 | Orioles 8–5 Athletics | 2–2 | LOSS | WIN | Oakland led 5–1; Baltimore's HR/middle-relief cluster produced seven unanswered and separation. |
| **Total** | **27 actionable finals; P-192 excluded** | **58–60** | **12–15** | **15–12** | **Descriptive late-import ledger only.** |

Row arithmetic was recomputed from every frozen contract and its settlement geometry. P-211's later administrative re-check is not a second forecast or event. No unresolved result was converted to a win or loss merely to make the totals reconcile.

## D. Detailed retrospective: failures, successes and honest process grading

### Rank #1 failures

**P-187 — result wrong / process wrong.** The card let a single same-opponent 38/1 powerplay anchor the Under while current phase participants were unresolved. Narine opened and made 53 from 24; Munro made 52, producing 60/0 after six. Availability was not enough: batting position and expected exposure to the first 36 balls were the decisive variables. Full-innings Over remained a correctly identified counterbranch and won, but that does not rescue the top-rank process.

**P-188 — result wrong / process incomplete.** “Rested bullpen” was too coarse. A closer does not protect a +1.5 line while his club trails and lower-leverage arms face the relevant innings. The five-run eighth shows that the forecast needed a score-state ladder—tied/ahead, one behind, multiple runs behind—plus inherited-runner and multi-run-HR paths.

**P-189 — result wrong / process partly right.** Brown's continuity helped A&M recover and lead late, so the underdog case was real. The error was translating Howard's new coach/QB uncertainty mainly downward. A regime with little current data should first widen the distribution; it shifts the centre only when a directional mechanism is supported. Scroggins' explosive passing ceiling was underweighted.

**P-191 — result wrong / process wrong for spread/total.** Carlton won, but the exposed venue's strong, directional breeze shaped scoring end by end and Fremantle competed through ruck/midfield resistance. Generic city weather was not enough. Ground-level vector, venue orientation and end switching must enter the quarter tree before a double-digit AFLW spread is ranked.

**P-193 — result wrong / process incomplete.** Under 83.5 won, yet Essendon +2.5 failed after Richmond's late territorial surge. A low total did not protect the underdog. Fourth-quarter repeat-entry resistance, rotations/interchange availability and conditioning in Darwin were not sufficiently separated from the total centre.

**P-194 — result wrong / process wrong.** Kaiserslautern's short scoreless sequence was treated too much like a stable suppression regime. It needed decomposition into chance creation, finishing, goalkeeping and opponent quality. St. Pauli's 21–11 shot edge also demonstrates that territory, conversion, final result and corners are distinct.

**P-196 — result wrong / process wrong.** Egypt -14.5 relied too heavily on two recent DR Congo blowout outcomes. Large-spread analysis must separately estimate possessions, shooting-efficiency edge, turnover/rebound conversion, bench/rotation separation and true blowout probability. Ugly recent finals expand downside risk; they do not by themselves locate the next game's centre.

**P-199 — result wrong / process wrong.** One 2–1 Sønderjyske opener could not resolve early-season roster and unconfirmed-goalie uncertainty. Because goalie identity directly controls conversion, the unresolved starter should have prevented the total from receiving the strongest rank absent unusually deep defensive-process evidence.

**P-200 — result wrong / process wrong for margin, definition-limited for settlement.** Herning won, but only after a 3–3 regulation tie; the -2.5 thesis relied too much on a 7–1 opener and old H2H across roster change. Winner and separation needed different branches. The research outcome is descriptive under the frozen OT/SO-inclusive assumption; sportsbook grading remains `UNKNOWN_DEFINITION` until the actual operator terms are supplied.

**P-203 — result wrong / process wrong.** The card named the important kill path—an early Deportivo goal opens the match—but did not give it enough severity before ranking the Under. Two early-season Valencia scoreless matches and four combined league matches were too small to fix a low-scoring centre. The independently verified path was Deportivo 2–1 at halftime and 3–1 final. The attached report's separate claim of a 5–3 corner source was not independently reproduced; reliable current evidence supports 5–5, so no fabricated provider conflict is imported.

**P-206 — result wrong / geometry wrong.** The pregame card explicitly contained a low-total Dodgers separation state and then ranked Tigers +1.5 over it. The exact 6–1 final is the critical geometry lesson: an opponent scoring floor near one run makes a multi-run favourite win compatible with an Under.

**P-207 — result wrong / process broadly right, contract poorly aligned.** Inter generated overwhelming territory and chances, but Cagliari contributed almost nothing and Inter converted once. “Inter creates heavily” is not equivalent to “the match reaches three goals.” If supplied and independently researchable, a one-team scoring contract would better match the mechanism; otherwise lower the full-total evidence.

**P-211 — result wrong / structural process wrong.** Best-of-five total games must be a mixture over 3-, 4- and 5-set endpoints, with within-set closeness inside each branch. The first two sets supported the central Faria edge, but Brooksby's two-set response moved the total to 47. A fifth-set path cannot sit inside an undifferentiated variance note around 39.5.

**P-212 — result wrong / coherence wrong.** The same tree preferred Alexandrova and her -2.5 game handicap but ranked Over 21.5 first. That combination is possible only with an explicit close-set or three-set branch. A 6–2, 6–2 favourite-control state was insufficiently represented even though the directional player evidence pointed toward it.

**P-214 — result wrong / process underweighted a named branch.** The card named Orioles separation scores and the Sutter/HR/middle-relief upper tail, but still treated Oakland +1.5 as broadly safe. Baltimore's offensive ceiling, Springs' contact risk, relief transition and favourite separation were positively dependent. The correct stress test is joint favourite-margin plus Over/cluster exposure, not two isolated tails.

### Rank #1 wins and other useful positives

**P-190 — result right / process right for Rank #1.** Under 47.5 and Dragons +15.5 both survived. The outright winner failed only after two late Dragons tries. Keep the competitive/low-total read; add terminal-event sensitivity to a close-game winner branch instead of rewriting the whole analysis.

**P-195 — result right / process right for the phase market.** The 1–1 halftime validated the early-goal mechanism. Club Brugge winner and corner allocation failed, so the success is specific to first-half scoring rather than a universal attacking edge.

**P-197 — result right / process right on goals, wrong on corners.** Over 2.5 and 1H Over won. ADO's lead forced a sustained Feyenoord chase and 11 home corners, directly contradicting the home-corner Under. Score state must propagate into corner exposure.

**P-198 — result right / process different for the total.** Poland +8.5 and Germany eventual winner were coherent. Regulation totalled 166, so Over 180.5 still needed 15 additional points to reach a winning 181; overtime added 24. Record it as an OT-dependent win, not validation of the regulation scoring centre.

**P-201 — result right / process right on goals.** Freiburg's attacking mechanism and Werder's weakened structure produced 4–1, with three goal-related rows winning. The corner Under lost at 11 and remains separate, boundary-sensitive derivative evidence.

**P-202 — result right for first-half phase, allocation wrong elsewhere.** Randers led 2–0 at halftime, validating the early-goal row. AGF winner and team-corner expectations did not follow; five AGF corners missed Over 5.5.

**P-204 — result right but winner process wrong.** Yankees +1.5 won in a 16–1 rout, while the Boston winner call was badly wrong. This is not evidence that a protected favourite line was well calibrated; it is evidence that Yankees separation/cluster risk was understated.

**P-205 — result right / process right.** Minnesota's conventional-starter/deeper-workload edge over Chicago's opener/bulk construction supported both the Twins winner and Under in a 5–1 final.

**P-208 — result right / process right on goals and side.** Lazio 1–0 aligned with the low-score/winner tree. Six total corners show again that attacking control does not mechanically generate a corner Over.

**P-209 — result right for early goal and corners, winner process wrong.** Santos' 33rd-minute goal settled the first-half Over and nine corners settled Over 8.5, but Corinthians' territorial volume did not become scoreboard dominance.

**P-210 — result right / process right on goals and winner.** Flamengo scored in the first half and won 3–0. The match produced only eight corners, so the goal mechanism cannot be reused as corner evidence.

**P-213 — result right / process right.** Samuel's current hard-court form and return pressure supported the winner, -2.5 games and Under in a clean straight-set final. The important lesson is mechanism-to-contract alignment, not “ranking beats reputation” as a timeless rule.

## E. Cross-sport learning synthesis and method effect

The audit supports process controls, not retrospective weight fitting:

1. **Uncertainty changes width before centre.** Sparse, new-coach, new-QB, early-season or roster-change evidence widens both tails unless a current directional exposure/rate mechanism justifies a centre shift.
2. **Role is phase- and score-state-specific.** Availability must become batting position, expected balls/minutes/shifts/snaps, bullpen leverage state, goalie start probability or equivalent exposure before affecting a market.
3. **Run a four-family score stress grid.** Every side/total slate must represent low/close, low/separation, high/close and high/separation states. P-193 and P-206 show why the first cannot stand in for the second.
4. **Select the contract that matches the researched mechanism.** One-team chance creation does not automatically support a full-game Over; possession does not equal winning; goals do not imply corners.
5. **Small outcome streaks are diagnostics.** Decompose creation, conversion, keeper/goalie/pitcher performance and opponent quality before moving direction.
6. **Extension endpoints are part of the model.** Regulation, overtime, shootout, extra innings, 3/4/5 sets, DLS and other termination states require explicit probabilities/branches and exact operator terms.
7. **A named ordinary kill path must affect the rank.** If the failure state can defeat several correlated rows and cannot honestly be kept subordinate, lower evidence or change the order before issue.
8. **Process and result remain separate.** Every retrospective uses result-right/process-right, result-right/process-different, result-wrong/process-broadly-right, or result-wrong/process-wrong; it does not learn from WIN/LOSS alone.
9. **Provider disagreement is field- and threshold-specific.** Preserve each value and lineage. If all credible values fall on the same side of a line, the contract result may be invariant, but the raw field is not falsely harmonised. If a claimed conflict cannot be reproduced, record that and do not manufacture it.

The governing method becomes `MDS-2026.08.31-v2.8`. This is an identity/source/coherence and scenario-representation patch. It changes no fitted coefficient, numerical probability, forecast weight or calibration claim. All new forecast-weight candidates start at zero prospective completions.

## F. Source-quality audit and future retrieval lanes

Settlement was routed field by field rather than by a site-wide reputation score. High-quality current lanes newly demonstrated in this audit include:

- [Windies Cricket official results](https://www.windiescricket.com/results/class_type/general/) for CPL final/state, with a legality-reconciled specialist scorecard for exact phase detail;
- [MLB official game stories and reports](https://www.mlb.com/stories/game/824959/) for finals and scoring chronology;
- [AFL/AFLW official match reports](https://www.afl.com.au/aflw/news/1598373/richmond-tigers-leave-it-late-to-edge-essendon-bombers-in-dreamtime-thriller) for final, quarter path and venue-condition narrative;
- [Bundesliga official match reports](https://www.bundesliga.com/en/bundesliga/news/freiburg-werder-bremen-match-report-highlights-matchday-1-suzuki-38905), [Lega Serie A reports](https://www.legaseriea.it/serie-a/news/lazio-genoa-2026-2027-1-0-cronaca-risultato-gol) and [LaLiga official match pages](https://www.laliga.com/es-PE/partido/temporada-2026-2027-laliga-ea-sports-rc-deportivo-valencia-cf-3) for competition-owned score/event facts;
- [Metal Ligaen official reports](https://metalligaen.dk/nyheder/kampen-kort-finsk-fest-i-frederikshavn/) for Danish hockey final/period chronology;
- [ATP official results](https://www.atptour.com/en/scores/current/us-open/560/results?matchType=singles) and [Tennis.com match statistics](https://www.tennis.com/tournaments/us-open/matches/m-kessler-vs-e-alexandrova-2026-08-30) as official-final plus specialist-current cross-check lanes.

Three official-domain defects were also observed and must become reusable negative checks:

- a FIBA page/search rendering exposed an old 2018 head-to-head score as though it were current-game content;
- the WTA match page still labelled Kessler–Alexandrova suspended/upcoming after a current final was available elsewhere;
- an official Lazio highlight URL slug displayed the teams in the wrong score order while competition and reputable current reporting established Lazio's 1–0 win.

An official domain is not enough. Before settlement, match event ID/date/participants, page state, score chronology and revision freshness. Quarantine stale shells, old head-to-head modules and malformed slugs field by field; prefer a static official report or two independent current high-quality sources until the owner corrects the page. Specialist corner/stat sources remain provider-specific and do not acquire official status merely because their number is useful.

## G. Documents updated by this audit

The common framework, source register, learning register, research guide and the cricket, AFL/AFLW, NRL, American-football, baseball, basketball, soccer, ice-hockey and tennis rules now carry the relevant controls. The canonical combined log records this component exactly once, preserves its original import hash, sets the queue to zero live plus ten final-event follow-ups, and advances the next ID to P-215.

---

**Independent audit conclusion:** every P-187–P-214 event is final or closed no-action; all 118 actionable rows reconcile; no live item is lost; P-200's operator definition remains honestly unresolved; the descriptive ledger is quarantined as late-import; and the method changes are process safeguards rather than hindsight-fitted forecast weights.
