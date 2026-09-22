# Prediction Mini Running Log — P-345 Continuation

**Status:** ACTIVE LOCAL APPEND-ONLY CONTINUATION — P-345–P-357 SETTLEMENT/RETROSPECTIVE PASS COMPLETE EXCEPT THREE DERIVATIVE ROWS  
**Initialised:** 2026-09-09 01:41 Australia/Melbourne  
**Google Drive:** READ ONLY  
**Local next forecast slot:** **P-358** — P-345–P-357 have now been state-checked; three derivative rows remain open  
**Current method:** **MDS-2026.09.06-v4.0**  
**Forecast mode:** **SPORTS_ONLY / MARKET_BLIND**  
**Numerical program:** **Stage S0 — design only / no validated model built**  
**Probability tier:** **UNVALIDATED_SUBJECTIVE — mandatory on every ranked row; not calibrated**  
**Value state:** **NO VALUE/EDGE CLAIM WITHOUT VALIDATED CALIBRATION + SAME-TIME PRICE**
**Settlement / retrospective pass:** **2026-09-10 Australia/Melbourne**
**Current Drive canonical check:** `PREDICTION_LOG_COMBINED_3.md` now ends at **P-344** and reports **P-345** as the next canonical ID; therefore this local P-345–P-357 sequence has **no current canonical-ID collision**.

> This file is a new external/local continuation beginning at P-345.
> Google Drive remains read-only. No Drive file is edited, uploaded, renamed, moved, or deleted by this workflow.
> The latest Drive `PREDICTION_LOG_COMBINED_3.md` snapshot observed at initialization still states P-333 as its next canonical ID; this log does not rewrite that Drive snapshot.
> P-345 is used because the user explicitly directed the new local continuation to start at P-345. Earlier locally issued P-333–P-344 records remain predecessor history and are not reconstructed, renumbered, or retrospectively altered here.
> Every new card is appended in strict local-ID order and returned to the user as an updated Markdown file after the query.

---

# 0. UNSETTLED / INCOMPLETE QUEUE

**Current state after the 2026-09-10 settlement pass:** all parent events `P-345`–`P-357` are FINAL.  
**Three derivative rows remain open because the exact frozen settlement field/provider is not yet recoverable to the required standard.** Every other ranked row and ordinary score/side/total contract in this continuation is settled.

| Tracking handle | Parent / rank | Frozen contract | Current evidence | Current disposition |
|---|---|---|---|---|
| **TMP-OPEN-20260910-01** | `P-345` Rank #3 | Club Brugge Over 3.5 team corners | Guardian reports Club Brugge **4** corners; VI reports **3**. The difference changes the grade. Opta Analyst exposes an official Opta match centre but the crawlable page does not expose the corner field itself. | **FINAL / PARTIAL — CORNER FIELD CONFLICTING / UNRESOLVED. No W/L or Brier booked.** |
| **TMP-OPEN-20260910-02** | `P-346` Rank #5 | AEK–LASK total corners Over 7.5 | Guardian reports **AEK 7–4 LASK = 11**; OFStats event timeline is consistent with a high-corner AEK game, but the card froze UEFA official match statistics as the intended owner. | **PROVISIONAL RESEARCH WIN — no final W/L/Brier until frozen owner/provider is recovered or the framework explicitly accepts the fallback.** |
| **TMP-OPEN-20260910-03** | `P-355` Rank #5 | Sydney FC–Melbourne Victory total corners Over 8.5, regulation | Multiple secondary displays report **Sydney 5–4 Victory = 9**; Sydney's official report confirms multiple corner events, but the frozen Opta/FotMob aggregate was not recovered. | **PROVISIONAL RESEARCH WIN — no final W/L/Brier booked.** |

**No whole-card P-345–P-357 event remains live or awaiting a final score.** These three handles are derivative-field tracking labels only; they are **not canonical prediction IDs**.

### Predecessor boundary

- This new continuation begins at **P-345** by explicit user instruction.
- Earlier P-333–P-344 local records are predecessor history and are not silently copied or reconstructed here.
- A prior accessible local continuation independently records P-333, P-334 and P-335 as issued/unsettled at its then-current snapshot; their later disposition is not inferred here.
- Fresh Drive reconciliation on 2026-09-10 shows `PREDICTION_LOG_COMBINED_3.md` has imported/settled `P-333`–`P-344` and now reports **P-345** as the next canonical ID. The local P-345–P-357 sequence therefore has no current canonical collision. Drive remains read-only.

---

# 1. CURRENT GOVERNANCE REFRESH — 2026-09-09

## 1.1 Authority order for this local continuation

1. Current user directive.
2. `METHOD.md` — active operational method, **MDS-2026.09.06-v4.0**.
3. `RULES_GENERAL.md` §16 — controlling gate classification and mandatory-card requirements.
4. Relevant `RULES_<SPORT>.md` and league-rules companion for the requested event.
5. `CONTROLS.md` — active quick-reference controls.
6. `SOURCES.md` — source ownership and research/settlement lanes.
7. `LEARNING_REGISTER.md` only where a specific promoted/candidate/test item is materially relevant.
8. Active/local log state and immutable prior issued cards.

## 1.2 Mandatory forecast cycle

For every P-345+ request:

1. Freeze event identity, competition/rules era, venue, participants, exact target, contract, line, phase/horizon, scheduled start and game state.
2. Verify decisive facts with exact source record, claim owner, access state/time.
3. Exclude synthetic, simulated, projected, AI-generated and tipster content from event-fact and settlement evidence.
4. Build L5/L10/L15/L20 + trend tests for both sides and relevant H2H, subject to continuity.
5. Model sport-native exposure, role-specific deficits, replacements, bench/coaching/rotation and availability.
6. For outdoor/open-roof events, obtain a venue-coordinate hourly forecast for the event window. If the hard environment gate cannot be met, fail closed rather than inventing an actionable forecast.
7. Build one coherent joint event object using explicit arithmetic:
   - stated prior/baseline;
   - signed weighted adjustments;
   - resulting centre;
   - explicit width/uncertainty;
   - each supplied line located against that centre/width.
8. For totals, show a component budget. For margins/handicaps, show a separation budget.
9. Run bidirectional-sign audit for mechanisms that may help and hurt the same contract.
10. Refresh volatile facts immediately before issue.
11. Assign an explicit **UNVALIDATED_SUBJECTIVE** probability to every ranked row; derive ordering from the probability set plus robustness.
12. Name the intended settlement source/field owner before ranking.

## 1.3 Population status

**PRIMARY_SCORED**
- MLB
- EPL
- NRL
- AFL / AFLW

**EXPLORATORY — NOT PRIMARY_SCORED**
- All other competitions unless formally promoted by the governing framework.

## 1.4 Hard behavioural constraints

- No bookmaker odds, implied probabilities, line movement, consensus, bookmaker previews, affiliates or tipster analysis may drive the forecast.
- No guarantee, lock, safe-bet, certainty, ROI, edge or calibrated-probability claim.
- Do not invent lineups, injuries, starters, roles, weather, scores, rules, statistics, results or probabilities.
- Conflicting or unavailable decisive facts remain explicitly conflicting/unavailable and reduce evidence quality.
- A streak carries no directional weight without an active mechanism.
- Potential-winner aliases are not duplicate observations.
- Research grade and operator action remain separate settlement fields where operator-specific terms are unavailable.
- One-session findings may be recorded as observations/candidates but do not become new predictive weights without prospective evidence.

---

# 2. SOURCE GOVERNANCE

## 2.1 Primary source principles

- Prefer field-owning official records and structured endpoints before narrative pages.
- Every decisive fact must retain the exact source, field/claim ownership and access time.
- Search-result summaries are discovery aids, not source records.
- Synthetic/simulated/AI-generated content is prohibited as a settlement source.
- Two weak sources do not become one strong source by agreement.
- Native-language sourcing remains important for non-English-primary competitions where the framework requires it.

## 2.2 Current high-value structured lanes

- ESPN Site API structured event/summary lanes where competition coverage is verified.
- Official league/team/event match centres.
- MLB StatsAPI for MLB event, umpire and environment-relevant structured data.
- Government weather source for venue-local outdoor/open-roof event windows.
- Sport-specific official scorecards/statistics endpoints.

## 2.3 Governing Drive files read at initialization

- `README.md`
- `METHOD.md`
- `RULES_GENERAL.md` §16
- `CONTROLS.md`
- `SOURCES.md`
- `PREDICTION_LOG_COMBINED_3.md`

Relevant sport-specific files will be read fresh when each event is requested.

---

# 3. RUNNING SOURCE REGISTER

This section accumulates the exact research sources used by each P-345+ card. Each event card also retains its own source register.

| ID | Source | Claim/field owner | Access state/time | Used for |
|---|---|---|---|---|
| INITIALIZATION | Google Drive `README.md` | Framework/active-log provenance | 2026-09-09 | v4.0 framework and Part 3 status |
| INITIALIZATION | Google Drive `METHOD.md` | Operational method | 2026-09-09 | MDS-2026.09.06-v4.0 lifecycle, probability mandate, settlement rules |
| INITIALIZATION | Google Drive `RULES_GENERAL.md` §16 | Gate classification | 2026-09-09 | blocking/required-analysis controls and explicit arithmetic |
| INITIALIZATION | Google Drive `CONTROLS.md` | Active control summary | 2026-09-09 | hard controls/candidate firewall |
| INITIALIZATION | Google Drive `SOURCES.md` | Source-lane governance | 2026-09-09 | source ownership, structured lanes, synthetic exclusion |
| INITIALIZATION | Google Drive `PREDICTION_LOG_COMBINED_3.md` | Drive queue/ID provenance | 2026-09-09 | Drive snapshot remains at P-333 |
| INITIALIZATION | Prior local `PREDICTION_MINI_RUNNING_LOG_P332_CONTINUATION.md` | Local predecessor provenance | 2026-09-09 | independently confirms local continuation activity after P-332 |

---

# 4. SETTLED / CHRONOLOGICAL P-345+ RECORDS

**Settlement pass:** 2026-09-10 Australia/Melbourne. Issued forecasts below remain immutable; settlement/retrospective addenda are appended to each card.

| ID | Final | Ranked rows finally graded | Ranked W-L | Rank #1 | Potential winner | Current status |
|---|---|---:|---:|---|---|---|
| `P-345` | Aston Villa 3–2 Club Brugge (HT 3–1 Villa) | 4/5 | 2-2 | **LOSS** | Club Brugge — **LOSS** | **FINAL / PARTIAL** — corner Rank #3 unresolved |
| `P-346` | AEK Athens 1–0 LASK (HT 1–0) | 4/5 | 4-0 | **WIN** | AEK — **WIN** | **FINAL / PARTIAL** — corner Rank #5 provisional |
| `P-347` | Texas Rangers 10–5 Seattle Mariners | 4/4 | 2-2 | **WIN** | Texas — **WIN** | **FINAL / SETTLED** |
| `P-348` | Toronto Blue Jays 4–2 Athletics | 4/4 | 1-3 | **WIN** | Toronto — **WIN** | **FINAL / SETTLED** |
| `P-349` | San Francisco Giants 2–1 St. Louis Cardinals | 4/4 | 4-0 | **WIN** | St. Louis — **LOSS** | **FINAL / SETTLED** |
| `P-350` | Ben Shelton def. Carlos Alcaraz 6-7(5), 6-1, 6-3, 1-6, 7-6(7) | 4/4 | 3-1 | **LOSS** | Alcaraz — **LOSS** | **FINAL / SETTLED** |
| `P-351` | Los Angeles Dodgers 3–2 Cincinnati Reds | 4/4 | 2-2 | **WIN** | Dodgers — **WIN** | **FINAL / SETTLED** |
| `P-352` | South Africa 348/6; Namibia 162/8 (31); South Africa won by 99 runs DLS | 4/4 | 3-1 | **LOSS** | South Africa — **WIN** | **FINAL / SETTLED** |
| `P-353` | Yomiuri Giants 5–1 Chunichi Dragons | 4/4 | 2-2 | **WIN** | Chunichi — **LOSS** | **FINAL / SETTLED** |
| `P-354` | Hiroshima Carp 3–1 Hanshin Tigers | 4/4 | 2-2 | **WIN** | Hanshin — **LOSS** | **FINAL / SETTLED** |
| `P-355` | Melbourne Victory 2–0 Sydney FC (HT 1–0) | 4/5 | 3-1 | **WIN** | Sydney — **LOSS** | **FINAL / PARTIAL** — corner Rank #5 provisional |
| `P-356` | KT Wiz 2–0 Samsung Lions | 4/4 | 3-1 | **LOSS** | Samsung — **LOSS** | **FINAL / SETTLED** |
| `P-357` | Belfast Wolves 107 all out; Dublin Guardians 111/2 (14.3); Dublin won by 8 wickets | 4/4 | 2-2 | **LOSS** | Belfast — **LOSS** | **FINAL / SETTLED** |

---


# P-345 — Club Brugge vs Aston Villa — UEFA Champions League

**Issued view:** PREGAME  
**Competition:** UEFA Champions League 2026/27, League Phase, Matchday 1  
**Venue:** Jan Breydelstadion, Bruges, Belgium  
**Scheduled kickoff:** 2026-09-08 18:45 CEST / 2026-09-09 02:45 AEST  
**Final volatile refresh:** 2026-09-08 18:25 CEST / 2026-09-09 02:25 AEST  
**Method:** `MDS-2026.09.06-v4.0`  
**Population:** `SOCCER — UEFA CHAMPIONS LEAGUE — EXPLORATORY / NOT PRIMARY_SCORED`  
**Mode:** `SPORTS_ONLY / MARKET_BLIND`  
**Probability tier:** `UNVALIDATED_SUBJECTIVE` — analyst judgment, not calibrated  
**Value/edge state:** `NO VALUE DETERMINABLE`  
**Retrospective:** **DEFERRED BY USER**

## A. Identity / competition / settlement freeze

UEFA's 2026/27 regulations confirm the 36-club league phase, with each club playing eight single-leg league-phase matches, four home and four away. League-phase matches are ordinary regulation matches: 3 points for a win, 1 for a draw, 0 for a loss. This P-345 view therefore treats any winner/1X proposition as a **90-minute regulation endpoint including stoppage time, excluding any hypothetical extra time/penalties**.

Supplied contracts:
- First-half goals Over 0.5
- First-half goals Under 0.5
- Full-match combined goals Over 2.5
- Full-match combined goals Under 2.5

Additional analyst-selected contracts:
- Club Brugge +0.5 / Double Chance 1X, regulation
- Club Brugge team total Over 0.5 goals, regulation
- Club Brugge Over 3.5 team corners, regulation + stoppage time

Intended settlement owner: **UEFA official match centre / UEFA official match statistics**. Operator-specific void/action terms were not supplied; at settlement, `RESEARCH_GRADE` and `OPERATOR_ACTION` must remain distinct where required.

## B. Confirmed starting XIs and matchday benches

### Club Brugge — 4-2-3-1

**XI:** Yann Sommer; Kyriani Sabbe, Han-beom Lee, Brandon Mechele, Joaquin Seys; Hugo Vetlesen, Freddie Potts; Carlos Forbs, Hans Vanaken, Jan Virgili; Nicolò Tresoldi.

**Bench:** Nordin Jackers, Argus Vanden Driessche, Cheveyo Tsawa, Romeo Vermant, Wisdom Mike, Hugo Siquet, Samba Coulibaly, Jorne Spileers, Lynnt Audoor, Mamadou Diakhon, Andrej Vasović, Félix Lemaréchal.

**Coach:** Ivan Leko.

### Aston Villa — 4-2-3-1

**XI:** Zion Suzuki; Aaron Wan-Bissaka, Victor Lindelöf, Pau Torres, Ian Maatsen; João Gomes, Boubacar Kamara; John McGinn, Emiliano Buendía, George Hemmings; Nicolas Jackson.

**Bench:** Marco Bizot, James Wright, Tyrone Mings, Ross Barkley, Matteo Ruggeri, Alejandro Garnacho, Tammy Abraham, Ibrahim Mbaye, Lamare Bogarde, Alysson.

**Coach:** Unai Emery.

### Availability / changes

- UEFA's pre-match availability report listed **Club Brugge defender Joel Ordóñez out with a foot injury** and no other Club Brugge doubt.
- UEFA listed **Aston Villa midfielder Johan Manzambi out with a knee injury** and no other Villa doubt in that report.
- The confirmed matchday team sheet then showed **João Gomes returning from suspension**, with Pau Torres and Aaron Wan-Bissaka coming into Villa's XI; current live reporting identified **Matty Cash as injured**.
- **George Hemmings starts on his Champions League debut.**
- Leon Goretzka is absent from Villa's confirmed matchday squad. No sufficiently strong current source retrieved in this pass established an exact injury diagnosis, so this log does **not** invent one.

Bench-depth continuity is complicated by heavy summer roster turnover, especially at Aston Villa. Full benches are retrieved, but a clean same-roster `>=40% of last 10 starts` bench-depth integer is not treated as fully comparable across the summer break. This is recorded as a continuity limitation rather than silently fabricated.

## C. Competition / H2H / European context

UEFA records this as the fourth meeting between these clubs. In 2024/25:
- Club Brugge won 1-0 at home in the league phase.
- Aston Villa later won 3-1 away and 3-0 at home in the Round of 16.

The current squads have changed enough that H2H is descriptive rather than a direct predictive weight.

UEFA also reports:
- Club Brugge have lost only **3 of their last 22 UEFA home matches** (`W13 D6 L3`) and scored 3+ in six of their last seven UEFA home matches.
- Aston Villa won **13 of 15** matches in last season's Europa League title run.
- Villa have lost only **3 of their last 21** UEFA group/league-phase matches and kept 9 clean sheets in their last 16 European games.

Those records cut both ways: Brugge's home-European resistance supports 1X, while Villa's European record prevents a strong anti-Villa conclusion from their three-match Premier League scoring drought.

## D. L5 / L10 / L15 / L20 form and continuity test

### Club Brugge — domestic competitive results

| Window | W-D-L | GF-GA | GF/game | GA/game | Over 2.5 count |
|---|---:|---:|---:|---:|---:|
| L5 | 4-0-1 | 9-2 | 1.80 | 0.40 | 3/5 |
| L10 | 8-1-1 | 26-5 | 2.60 | 0.50 | 7/10 |
| L15 | 12-1-2 | 41-11 | 2.73 | 0.73 | 11/15 |
| L20 | 16-2-2 | 53-17 | 2.65 | 0.85 | 16/20 |

Current 2026/27 league sample: 4-0-1, 9 scored, 2 conceded. FBref records **84 shots / 27 shots on target for Brugge** and **56 shots / 18 on target against** across those five league matches. The 2 goals conceded are therefore not treated as proof of a permanently elite 0.40-GA defensive rate; goalkeeper/finishing variance is explicitly allowed to regress.

### Aston Villa — Premier League continuity window

| Window | W-D-L | GF-GA | GF/game | GA/game |
|---|---:|---:|---:|---:|
| L5 | 2-1-2 | 6-8 | 1.20 | 1.60 |
| L10 | 3-3-4 | 14-17 | 1.40 | 1.70 |
| L15 | 4-4-7 | 19-27 | 1.27 | 1.80 |
| L20 | 6-5-9 | 23-30 | 1.15 | 1.50 |

The most relevant current regime is materially worse in attack: Villa opened the 2026/27 Premier League with **0-4 at Brighton, 0-1 vs Arsenal, 0-0 at Hull**, taking only **one shot on target across those three league matches**. They did score once in a 2-1 UEFA Super Cup loss to PSG before the league began.

**Continuity gate:** the longer Villa windows are strongly downweighted because six starters from last season's Europa League final XI are no longer in the side and the attack has been rebuilt. They are used as a prior/variance reference, not as a claim that the old Villa attack remains intact.

## E. Current attacking / defensive mechanism

### Club Brugge

Current mechanism is more persuasive than the raw win streak alone:
- 84 shots and 27 SoT in five league matches.
- Vanaken remains the central connector.
- Forbs + Virgili provide width around Tresoldi.
- Sabbe and Seys give overlapping/wide support.
- Brugge have scored in every one of the reconstructed last 20 domestic league matches.

Primary kill path: step-up in opponent quality. Last season Brugge averaged only **3.0 corners per Champions League match**, and their current domestic dominance cannot be transferred one-for-one to Villa.

### Aston Villa

Villa's current attacking problem is not just a no-goal streak:
- 26 shots but only one SoT across their first three league matches.
- Against Hull they had 74% possession and 13 shots but only one on target.
- João Gomes returning beside Kamara should improve midfield ball-winning and progression.
- Jackson gives direct central threat.
- Hemmings is talented but is making a Champions League debut.
- Garnacho, Abraham, Mbaye and Alysson create a stronger second-half attacking bench than the starting XI's current scoring record suggests.

That bench is a major reason not to make Under 2.5 a high-confidence selection.

## F. Outdoor environment / surface gate

Venue-specific structured weather check for **Jan Breydel Stadium** at 18:21 CEST:
- current condition: **light rain**
- temperature: **16°C**
- 19:00 local precipitation probability: **84%**
- rain expected around kickoff, easing toward 20:00–21:00.

Mechanism audit:
- wet conditions can reduce clean combination/finishing quality;
- the same conditions can increase skids, blocked actions, defensive errors and corner-producing deflections;
- therefore weather receives only a small negative centre adjustment for finishing and a **wider tail**, not a mechanical Under signal.

`G15.1` environment gate: **PASSED**.

## G. Goal event object — explicit arithmetic

This is qualitative arithmetic under v4.0, **not a fitted or calibrated goal model**.

### Full-match total centre

Long-window contest starting point:
- Club Brugge L20 domestic match total = `(53 GF + 17 GA) / 20 = 3.50`
- Aston Villa L20 league match total = `(23 GF + 30 GA) / 20 = 2.65`
- simple midpoint prior = `(3.50 + 2.65) / 2 = 3.08`

Signed current-regime adjustments:
- `-0.35` — early-season current-state shrink: Brugge's first five league matches average 2.20 total goals; Villa's four current all-competition matches sit around 2.0 total goals.
- `-0.20` — Villa's current shot-on-target/finishing collapse, partially shrunk because the sample is only three league games.
- `-0.10` — Brugge's current defensive suppression, also shrunk because 18 opposition SoT have produced only 2 goals.
- `+0.12` — Brugge home/European attacking-tail allowance plus current wide attacking XI.
- `0.00 centre / +width` — Villa's deep attacking bench: more late upside but not enough evidence for a clean signed centre lift.
- `-0.05` — light rain / wet-surface finishing adjustment; widened variance offsets any stronger directional claim.

**Resulting centre:** `3.08 - 0.35 - 0.20 - 0.10 + 0.12 - 0.05 = 2.50 goals`

**Explicit width:** approximately **±1.35 goals** around the centre, widened for cross-league translation, early-season roster turnover, wet conditions and high-quality benches.

### Team component budget

- Club Brugge goal component centre: **1.50**
- Aston Villa goal component centre: **1.00**
- Combined: **2.50**

### First-half component

First-half qualitative centre:
- neutral first-half prior: `0.95`
- Club home early-pressure mechanism: `+0.05`
- Villa double-pivot/low-current finishing: `-0.10`
- rain/wet finishing: `-0.05`
- **first-half centre ≈ 0.85 goals**

This produces a modest lean toward at least one first-half goal, not a high-confidence early-goal call.

## H. Separation budget / winner object

Goal-component separation:
- Brugge centre `1.50`
- Villa centre `1.00`
- regulation margin centre: **Brugge +0.50**
- margin width: roughly **±1.5 goals**

Qualitative 1X2 state:
- **Club Brugge win: 44%**
- **Draw: 27%**
- **Aston Villa win: 29%**

Thus Club Brugge +0.5 / 1X is assigned **71% UNVALIDATED_SUBJECTIVE**. This is not a price/value claim.

## I. Corner process

Direct corner evidence is deliberately separated from goals:
- Club Brugge's 2026 last-20 all-competition corner sample: **6.85 corners/game**, **7.7 home**, **9.0 over the last five**.
- Their most recent match at Lommel produced **9 Club Brugge corners**.
- But their 2025/26 Champions League average was only **3.0 corners/game**, so domestic corner volume is aggressively competition-shrunk.
- Villa's current league opponents produced **5 corners (Brighton), 4 (Arsenal), 3 (Hull)**, average **4.0**.
- Current Brugge width comes directly from Forbs/Virgili plus Sabbe/Seys rather than possession as a proxy.
- Rain has a bidirectional corner sign: more blocks/deflections possible, but less clean end-line execution.

Explicit corner centre:
- domestic baseline `6.85`
- 55% shrink toward prior UCL rate `3.00`: `6.85 + 0.55*(3.00 - 6.85) = 4.73`
- Villa current opponent-corner environment: `-0.20`
- current wide XI: `+0.15`
- rain: `0.00 centre, +width`
- **Club Brugge corner centre ≈ 4.68; width ≈ ±2.5**

Because the competition shift is large and the current UCL sample is zero matches, the final probability is intentionally below a naïve count-model conversion.

Intended corner settlement: UEFA official match statistics, regulation + stoppage time.

## J. Bidirectional-sign audit / kill paths

| Mechanism | Helps | Hurts |
|---|---|---|
| Villa's current 0-goal league start | Brugge 1X, Under 2.5 | Sample is tiny; Jackson + Gomes + attacking bench can reverse it |
| Brugge domestic attacking volume | Brugge goal, Brugge corners | Belgian league dominance may not transfer to Champions League level |
| Brugge current 2 GA in 5 | Brugge 1X, Under | 18 SoT against indicate some goalkeeper/finishing regression risk |
| Wet weather | Can suppress clean finishing | Can increase errors, skids, blocks and corner deflections |
| Villa bench | Protects Villa late / raises goal tail | Starting attack still contains Hemmings debut and current low SoT output |
| Ordóñez absence | Helps Villa scoring branch | Han-beom Lee starts in a settled 4-2-3-1 and Brugge retain home structure |
| João Gomes return | Helps Villa midfield control and defense | Does not itself solve the current final-third/SoT problem |

## K. Ranked five — probability order

| Rank | Selection | UNVALIDATED_SUBJECTIVE | Evidence | Reason |
|---:|---|---:|---|---|
| **1** | **Club Brugge +0.5 / Double Chance 1X (90 min)** | **71%** | `SUPPORTED / MEDIUM-HIGH` | Confirmed XI, strong current home-side process, Club's UEFA home non-loss history, Villa's current attacking transition; draw protection materially reduces the outright-winner tail. |
| **2** | **Club Brugge team total Over 0.5 goals** | **70%** | `SUPPORTED / MEDIUM` | Brugge current shot volume + wide XI + home European attacking history. Villa remain capable defensively, so this is not pushed into the high-70s. |
| **3** | **Club Brugge Over 3.5 team corners** | **60%** | `LEAN / MEDIUM` | 6.85 domestic L20 corner rate and current wide route, but heavily shrunk because last UCL campaign was only 3.0/game. |
| **4** | **1st Half Over 0.5 goals** | **58%** | `LEAN / MEDIUM` | First-half centre ≈0.85; Brugge home pressure outweighs Villa's low-current attack, but rain and Villa's double pivot keep the edge modest. |
| **5** | **Combined Total Under 2.5 goals** | **55%** | `LEAN / MEDIUM-LOW` | Full centre ≈2.50 exactly around the threshold. Villa's current attack and Brugge defense pull Under; Brugge's UEFA scoring tail and Villa bench are the principal kill paths. |

### Supplied-line complementary audit

| Supplied row | Probability |
|---|---:|
| **1H Over 0.5** | **58%** |
| 1H Under 0.5 | 42% |
| **Under 2.5 full match** | **55%** |
| Over 2.5 full match | 45% |

Half-point complements are internally coherent: each pair sums to 100%.

## L. Potential winner

**Potential regulation winner: Club Brugge — 44% UNVALIDATED_SUBJECTIVE.**

This is a **narrow winner lean**, not the strongest selection. The stronger side expression is **Club Brugge +0.5 / 1X**, because the draw remains a substantial branch.

Central score family: **1-0, 1-1, 2-0**, with **2-1** the most relevant Over-2.5 tail.

## M. Source register — P-345

| Source | Owner / field | Access state / time | Use |
|---|---|---|---|
| Google Drive `METHOD.md` | Sports Research method | Fresh-read 2026-09-09 | v4.0 lifecycle, probability mandate |
| Google Drive `RULES_GENERAL.md` §16 | Sports Research gate authority | Fresh-read 2026-09-09 | blocking/required gates, arithmetic |
| Google Drive `RULES_SOCCER.md` | Sport-specific framework | Fresh-read 2026-09-09 | goal/corner/participant process |
| Google Drive `CONTROLS.md` | Active controls | Fresh-read 2026-09-09 | source/bench/environment controls |
| Google Drive `LEAGUE_RULES_SOCCER.md` | Competition-law reference | Fresh-read 2026-09-09 | rules-currency check; UCL gap identified |
| UEFA 2026/27 Champions League Regulations, Article 17 | Official competition rules | 2026-09-09 pregame | 36-team league phase, 8 single matches, points |
| UEFA 2026/27 Regulations, Article 25 | Official kickoff rules | 2026-09-09 pregame | league-phase kickoff structure |
| UEFA Champions League fixtures / kickoff article | Official schedule | 2026-09-09 pregame | Club Brugge–Villa 18:45 CEST identity/time |
| UEFA Matchday 1 starting line-ups page | Official competition lineup report | 2026-09-09 pregame | confirmed XIs |
| UEFA Club Brugge–Aston Villa line-ups / squad page | Official squad register | 2026-09-09 pregame | registered players/coaches |
| UEFA Matchday 1 predicted lineups/injury report (7 Sep snapshot) | Official UEFA availability report | retrieved pregame | Ordóñez foot; Manzambi knee |
| UEFA Matchday 1 key-stats pack | Official European competition history | 2026-09-09 pregame | H2H; Brugge UEFA home; Villa Europe |
| The Guardian live match page | Reputable live team-sheet cross-check | final refresh 02:25 AEST | confirmed formations, benches, Cash injury, Gomes return |
| FBref Club Brugge 2026/27 scores/shooting | Structured statistical record | current as of 2026-09-09 | current results, shots/SoT |
| FBref Club Brugge 2025/26 results | Structured statistical record | current archive | L10/L15/L20 reconstruction |
| StatMuse Aston Villa last-20 Premier League matches | Structured historical record | current as of 2026-09-09 | L5/L10/L15/L20 Villa trend |
| FBref Aston Villa 2026/27 fixtures/results | Structured current record | current as of 2026-09-09 | current 0-1-2 PL start + Super Cup context |
| Guardian Hull–Villa, Brighton–Villa, Villa–Arsenal match stats | Defined match statistics | current archive | shots, SoT, opponent corners |
| Statof Club Brugge corners | Specialist corner dataset | current as of 2026-09-09 | Club 2026 L20/home/L5 corners |
| StatMuse Club Brugge Champions League corners | Specialist structured historical record | current as of 2026-09-09 | 2025/26 UCL 3.0 corners/game |
| Structured weather forecast, Jan Breydel Stadium | Venue-specific weather source | 18:21 CEST / 02:21 AEST | current light rain, 16°C, 19:00 rain probability |
| Live structured soccer schedule state | Current game-state source | 02:25 AEST | scheduled / not started |

### Exact public source URLs

- https://www.uefa.com/uefachampionsleague/news/02a9-217ead601a03-116df4b8238f-1000--what-time-do-the-champions-league-league-phase-matches-kic/
- https://www.uefa.com/uefachampionsleague/news/02a8-215821715a96-9a3b43fad585-1000--uefa-champions-league-league-phase-draw/
- https://documents.uefa.com/r/Regulations-of-the-UEFA-Champions-League-2026/27/Article-25-Stadium-announcements-and-kick-off-times-Online
- https://www.uefa.com/uefachampionsleague/match/2049556--club-brugge-vs-aston-villa/lineups/
- https://www.uefa.com/uefachampionsleague/news/02a9-2188cf675017-df8325ec95c3-1000--champions-league-predicted-line-ups-matchday-1-team-news-/
- https://www.uefa.com/uefachampionsleague/news/02a9-2180c6b55c39-54a55373de68-1000--champions-league-matchday-1-key-stats-and-what-to-look-o/
- https://www.theguardian.com/football/live/2026/sep/08/club-brugge-v-aston-villa-champions-league-live
- https://fbref.com/en/squads/f1e6c5f1/2026-2027/matchlogs/all_comps/schedule/Club-Brugge-Scores-and-Fixtures-All-Competitions
- https://fbref.com/en/squads/f1e6c5f1/2026-2027/matchlogs/c37/shooting/Club-Brugge-Match-Logs-Belgian-Pro-League
- https://fbref.com/en/squads/8602292d/2026-2027/matchlogs/all_comps/schedule/Aston-Villa-Scores-and-Fixtures-All-Competitions
- https://www.statmuse.com/fc/ask/aston-villa-last-20-matches?l=pl
- https://statof.com/team/2347-club-brugge/stats/corners
- https://www.statmuse.com/fc/ask/club-brugge-average-corners-per-game-this-season
- https://www.theguardian.com/football/2026/sep/05/hull-city-aston-villa-premier-league-match-report
- https://www.theguardian.com/football/match/2026/aug/23/brightonfootball-v-aston-villa
- https://www.theguardian.com/football/match/2026/aug/31/aston-villa-v-arsenal

**Explicit exclusions:** bookmaker odds, implied probabilities, line movement, tipster/model picks, betting previews and synthetic predictions were not used as predictive evidence.

**P-345 STATUS:** `PREGAME — UNSETTLED`  
**Next local forecast slot:** **P-346**


### Settlement / retrospective addendum — 2026-09-10

**Current status:** `FINAL / PARTIAL` — all goal/side rows settled; Rank #3 corner row remains `TMP-OPEN-20260910-01`.

**Verified final:** Aston Villa beat Club Brugge **3–2**, leading **3–1 at half-time**. Villa scored through John McGinn (11'), Emiliano Buendía (22') and Nicolas Jackson (43'); Brugge scored through Hugo Vetlesen (19') and Nicolò Tresoldi (61' pen). Opta Analyst's post-match report records **Villa 21 shots to Brugge 14 and 3.00 xG to 1.46**, a decisive reversal of Villa's pregame domestic finishing narrative.

| Contract | Issued probability | Result |
|---|---:|---|
| Rank #1 Club Brugge +0.5 / 1X | 71% | **LOSS** |
| Rank #2 Club Brugge TT Over 0.5 | 70% | **WIN** — Brugge 2 |
| Rank #3 Club Brugge Over 3.5 corners | 60% | **UNRESOLVED** — Guardian 4, VI 3; threshold-changing conflict |
| Rank #4 1H Over 0.5 goals | 58% | **WIN** — four first-half goals |
| Rank #5 Under 2.5 goals | 55% | **LOSS** — five goals |
| Supplied 1H Under 0.5 | 42% | **LOSS** |
| Supplied Over 2.5 | 45% | **WIN** |
| Potential regulation winner: Club Brugge | 44% | **LOSS** |

**Brier, finalized ranked rows only:** `(0.71-0)^2 + (0.70-1)^2 + (0.58-1)^2 + (0.55-0)^2 = 1.0730`; mean **0.2683** over 4 rows. Rank #3 is deliberately excluded pending a defensible corner field.

**Retrospective Q1 — what did the score actually turn on?** Villa's rebuilt attack produced a real high-quality first-half burst rather than extending the three-match Premier League scoring drought. The match had three Villa goals by 43 minutes and a post-match Opta shot/xG profile that supports genuine attacking creation, not merely three freak finishes.

**Q2 — was that driver knowable and was it in the card?** **Partly yes.** The card already identified João Gomes' return, Jackson's central threat, Hemmings plus a deep attacking bench, and the important fact that Villa's drought came from a tiny sample. It nevertheless gave a signed `-0.20` adjustment for the current SoT/finishing collapse and `-0.10` for Brugge's defensive suppression. The actual result shows that **shot volume/creation and finishing/SoT conversion were not sufficiently separated**. The card even noted 26 Villa shots despite one SoT across the domestic sample.

**Q3 — smallest research-routine change:** enforce the existing early-season shrinkage rule literally: when shots/territory remain present but SoT/goals are abnormally low over only 2–3 matches, treat most of the uncertainty as **conversion/shot-quality width**, not a large persistent negative attacking-centre adjustment.

**Deep Rank-#1 review.** What went right: Brugge's attack did score twice; Rank #2 and the first-half Over won. What went wrong: 1X and the preferred Under both relied on Villa's poor current scoring state persisting more than the evidence justified. The kill path was printed but underweighted. This is primarily an **application failure of existing `RULES_SOCCER` early-season drought/shrinkage and `G-L2` width-vs-direction controls**, not evidence for a new hard rule.

**Card learning / recommended destination if canonical files are later updated:** reinforce `RULES_SOCCER.md` control on early-season droughts; record this as an `OBSERVATION` in `LEARNING_REGISTER.md`, not `PROMOTED`. Corner-source conflict belongs under `SOURCES.md` / `DATA_SOURCE_REGISTER.md` provider-definition coverage.

**Settlement sources:**
- Opta Analyst: https://theanalyst.com/articles/club-brugge-vs-aston-villa-stats-champions-league-09-2026
- Guardian match record: https://www.theguardian.com/football/match/2026/sep/08/clubbrugge-v-aston-villa
- Guardian live/report: https://www.theguardian.com/football/live/2026/sep/08/club-brugge-v-aston-villa-champions-league-live
- VI secondary stat display (corner-conflict evidence): https://www.vi.nl/wedstrijden/2026-09-08/club-brugge-vs-aston-villa

---


# P-346 — AEK Athens vs LASK — UEFA Champions League

**Issued view:** PREGAME  
**Event identity resolved from user's abbreviated request:** AEK Athens vs **LASK**  
**Competition:** UEFA Champions League 2026/27 — League Phase, Matchday 1  
**Venue:** Allwyn / OPAP Arena (Agia Sophia Stadium), Nea Filadelfeia, Athens, Greece  
**Venue coordinates used for environment identity:** approximately **38.0371, 23.7416**  
**Scheduled kickoff:** 2026-09-08 19:45 EEST / 2026-09-09 02:45 AEST  
**Final volatile refresh:** 2026-09-08 19:38:25 EEST / 2026-09-09 02:38:25 AEST  
**State at freeze:** **PREGAME — scheduled start had not been reached; no play incorporated**  
**Method:** `MDS-2026.09.06-v4.0`  
**Population:** `SOCCER — UEFA CHAMPIONS LEAGUE — EXPLORATORY / NOT PRIMARY_SCORED`  
**Mode:** `SPORTS_ONLY / MARKET_BLIND`  
**Probability tier:** `UNVALIDATED_SUBJECTIVE` — analyst judgment, not calibrated  
**Value/edge state:** `NO VALUE DETERMINABLE`  
**Retrospective:** **DEFERRED BY USER**

## A. Queue / predecessor state check

P-345 (Club Brugge vs Aston Villa) had the same scheduled 02:45 AEST kickoff. The current query arrived before that scheduled start and the latest structured schedule state remained pregame/scheduled. P-345 therefore remains **OPEN / UNSETTLED**. Per the user's explicit instruction, **no retrospective was performed**.

## B. Competition / contract / settlement freeze

UEFA confirms AEK Athens vs LASK as a Matchday 1 fixture in the 2026/27 36-club Champions League league phase. It is a single regulation match, not a two-leg tie. Standard goal, corner and regulation-winner targets therefore settle over **90 minutes plus stoppage time**; extra time and penalties are not part of this league-phase fixture.

User-supplied contracts:
- First-half goals Over 0.5
- First-half goals Under 0.5
- Full-match combined goals Over 2.5
- Full-match combined goals Under 2.5

Analyst-selected additional contracts:
- AEK Athens +0.5 / Double Chance 1X — 90-minute regulation
- AEK Athens team total Over 0.5 goals — regulation
- Combined total Under 4.5 goals — regulation
- Total match corners Over 7.5 — regulation + stoppage time

**Intended settlement owner:** UEFA official match centre / UEFA official match statistics. Operator-specific void/action rules were not supplied; if relevant at settlement, `RESEARCH_GRADE` and `OPERATOR_ACTION` remain separate.

## C. Confirmed starting XIs / coaches

UEFA's Matchday 1 starting-lineup update supersedes its earlier predicted-lineup article.

### AEK Athens — confirmed 4-4-2

**XI:** Alberto Brignoli; Lazaros Rota, Harold Moukoudi, Filipe Relvas, Stavros Pilios; Lovro Majer, Răzvan Marin, Milán Vitális, Aboubakary Koita; Luka Jović, Barnabás Varga.

**Coach:** Marko Nikolić.

### LASK — confirmed 5-3-2 / back-five structure

**XI:** Lukas Jungwirth; Kasper Jørgensen, Xavier Mbuyamba, João Victor Tornich (Alemão), Andrés Andrade, George Bello; Robert Ljubičić, Melayro Bogarde, Sascha Horvath; Christoph Lang, Moses Usor.

**Coach:** Dietmar Kühbauer.

### Current secondary bench retrieval

UEFA's indexed public match page exposed the registered squad and confirmed XI article, but not a complete field-owning bench list in the retrieved record. A current secondary lineup feed supplied:

**AEK reserves:** Oleksandr Zubkov, Marios Balamotis, Zini, Kervin Arriaga, Domagoj Vida, Petros Mantalos, Kaan Kairinen, Mijat Gaćinović, Charalampos Lykogiannis, João Mário.

**LASK reserves:** Kryštof Daněk, Nael Kane, Manoël Verhaeghe, Miguel Freckleton, Daniel Elfadli, Fabian Schillinger, Yvan Dibango, Sasa Kalajdžić, Florian Flecker, Tobias Schützenauer, Alessandro Schöpf.

Bench source status is therefore **SECONDARY_ONLY**, not official-confirmed. The 40%-of-last-10 bench-depth integer is **not cleanly comparable across the summer roster/season boundary** and is not fabricated. This is carried as a G14.2 continuity limitation and caps bench-sensitive conclusions at **MEDIUM** evidence.

## D. Availability / injury / rest / rotation

### AEK

- UEFA's earlier Matchday 1 team-news snapshot listed **no AEK absences or doubts**.
- That snapshot was superseded late: current Greek reporting says **Thomas Strakosha missed the final training session and is out**, with **Alberto Brignoli starting**.
- The exact Strakosha diagnosis was not published in the retrieved report; this log records **OUT — UNSPECIFIED LATE ISSUE**, not an invented injury.
- Koita starts instead of the earlier UEFA-predicted Gaćinović.
- AEK played Aris on 5 September. Current starters Varga and Jović played substantial minutes, so there is a normal short Champions League turnaround.

### LASK

- UEFA's earlier official team-news report listed **Sasa Kalajdžić out for fitness** and **Samuel Adeniran doubtful with a facial issue**.
- The confirmed UEFA XI contains neither player. The current secondary bench feed places **Kalajdžić on the bench** and omits **Adeniran** entirely.
- Therefore the only field-owning fact used directionally is: **Adeniran does not start; LASK start Lang + Usor**. Kalajdžić's reserve availability remains `SECONDARY_ONLY`.
- LASK also played on 5 September but their official cup report explicitly says Kühbauer **rotated several positions** in the 6-1 win at Deutschlandsberg, giving the visitors a small freshness advantage relative to a simple three-day-rest count.

## E. L5 / L10 / L15 / L20 form reconstruction

Friendlies are excluded. For LASK's 25 August Celtic match, the trend window uses the **4-1 score after 90 minutes**, not the eventual 5-1 after extra time.

| Window | AEK W-D-L | AEK GF-GA | LASK W-D-L | LASK GF-GA |
|---|---:|---:|---:|---:|
| **L5** | **4-1-0** | **16-1** | **4-0-1** | **16-6** |
| **L10** | **5-5-0** | **22-6** | **9-0-1** | **35-7** |
| **L15** | **8-6-1** | **29-10** | **13-1-1** | **50-13** |
| **L20** | **11-7-2** | **39-14** | **16-2-2** | **62-22** |

### Continuity interpretation

These raw records are **not** used literally:
- AEK's longer windows cross a summer roster break and multiple competitions.
- LASK's longer windows contain Austrian league/cup matches against weaker opposition and therefore exaggerate the scoring level relative to a Champions League away match.
- Recent scoring streaks receive no directional weight by themselves. The ranking uses current lineup, shot/chance mechanisms, opponent quality, venue and European match state.

## F. Current goal / chance-creation mechanisms

### AEK attacking chain

The current home mechanism is concrete:
- AEK beat Iraklis **4-0**, Levski Sofia **4-0** and Aris **5-0** in their latest major home competitive games.
- Against Levski they generated **18 shots, 7 on target, 2.75 xG and 6 corners**, with Jović scoring at 7' and Varga at 12' and 29'.
- Varga's recent starting minutes / shot record:
  - Iraklis: 71 min, 3 shots, 1 SoT, 1 goal
  - Levski: 80 min, 2 shots, 2 SoT, 2 goals
  - Kifisia: 81 min, 2 shots, 2 SoT, 1 goal
  - Aris: 79 min, 3 shots, 2 SoT, 2 goals
- Jović remains a second central penalty-area presence, while Majer and Koita supply width/creation around the front pair.

This supports **AEK scoring at least once** and a live early-goal branch. It does not prove the same conversion rate persists at Champions League league-phase level.

### AEK defensive chain

AEK's recent defensive record is strong, but the goalkeeper late change matters:
- the club has conceded only one goal across its most recent five competitive matches;
- Moukoudi/Relvas/Rota/Pilios retain back-line continuity;
- but Brignoli replaces Strakosha shortly before kickoff.

That goalkeeper swap is treated primarily as **extra uncertainty**, not an automatic negative coefficient.

### LASK attacking chain

LASK's scoreline run is also supported by chance volume:
- official LASK results: 6-1 at Deutschlandsberg, 3-1 at Wolfsberger, 3-0 vs Altach;
- against Altach they produced roughly **21-22 shots, 10-11 on target and 4 corners**;
- even in the 0-3 first-leg loss at Celtic, LASK generated substantial shot volume;
- in the home return against Celtic, LASK were **4-1 after 90 minutes**, with Flecker's 90th-minute goal forcing extra time. The match generated a very high corner/shot environment.

The major current change is that **Adeniran is not in the starting attack**. Lang and Usor offer mobility and transition threat, but less of the same direct box/hold-up profile. This reduces LASK's central finishing component slightly rather than erasing their scoring threat.

## G. H2H / competition continuity

UEFA states:
- this is the **first-ever meeting** between AEK and LASK;
- it is also LASK's first match against a Greek club;
- AEK are unbeaten in their last three matches against Austrian teams (W1 D2).

No direct H2H mechanism exists, so this receives descriptive weight only.

## H. Environment / playing surface gate

The match is at Allwyn / OPAP Arena in Nea Filadelfeia. Venue identity was reconciled to approximately **38.0371 N, 23.7416 E**.

The venue-neighbourhood hourly forecast around kickoff is:
- **clear / dry**
- approximately **26°C around 20:00 local**, easing toward the mid-20s later
- no meaningful rain signal
- mild breeze rather than extreme wind.

Mechanism:
- no rain-driven passing/finishing suppression;
- warm conditions may modestly increase later fatigue/substitution value;
- no strong signed total adjustment is justified.

`G15.1`: **PASSED** using exact venue identity plus Nea Filadelfeia / stadium-location hourly weather evidence.

## I. Goal event object — explicit arithmetic

This is **qualitative v4.0 arithmetic, not a fitted/calibrated model**.

### Long-window starting point

- AEK L20 match-goal rate: `(39 GF + 14 GA) / 20 = 2.65`
- LASK L20 match-goal rate: `(62 GF + 22 GA) / 20 = 4.20`
- simple midpoint prior: `(2.65 + 4.20) / 2 = 3.425`

### Signed adjustments

`3.425`
- `0.40` — domestic/cup scoring inflation and opponent-strength translation into Champions League league phase  
- `0.20` — AEK current defensive-control signal, aggressively shrunk rather than copied literally  
- `0.15` — LASK starting without Adeniran / reduced direct central box profile  
+ `0.20` — AEK current home attacking process with Varga + Jović + Majer + Koita  
+ `0.10` — LASK underlying chance volume survives stronger opposition better than raw domestic scorelines alone  
+ `0.05` — relative LASK freshness after explicit cup rotation / possible late-space benefit  
+ `0.00` — dry, warm weather: no justified net directional total sign  
= **3.03 goals**

**Final qualitative centre:** approximately **3.0 goals**  
**Width:** approximately **±1.5 goals**, widened for cross-league translation, Matchday 1 uncertainty, goalkeeper change and bench-source limitations.

### Team component budget

- **AEK:** ~**1.80**
- **LASK:** ~**1.20**
- Combined: **~3.00**

### Supplied 2.5-goal line

The supplied 2.5 line sits slightly below the 3.0 centre but well inside the uncertainty width:
- **Over 2.5: 58% UNVALIDATED_SUBJECTIVE**
- **Under 2.5: 42%**

The Over is the preferred side, but only modestly.

## J. First-half object

First-half qualitative centre:

`1.18` neutral/current contest first-half prior  
`+0.10` AEK's current early home route (2-0 HT vs Iraklis; 3-0 HT vs Levski; Varga 11' vs Aris)  
`+0.07` LASK's own early-event capacity (e.g. Lang 3' and 19' vs Altach; both Celtic qualifying legs produced first-half goals)  
`-0.08` Champions League Matchday 1 / opponent-strength translation  
`= ~1.27 first-half goals`

After uncertainty shrink:
- **1H Over 0.5: 68%**
- **1H Under 0.5: 32%**

The Over is supported by current attacking mechanisms on both sides, not by the streak alone.

## K. Separation / winner budget

Team components:
- AEK 1.80
- LASK 1.20

Regulation margin centre:
`1.80 - 1.20 = AEK +0.60 goals`

Margin width: roughly **±1.7 goals**.

Subjective 90-minute 1X2:
- **AEK win: 53%**
- **Draw: 26%**
- **LASK win: 21%**

Thus:
- **AEK +0.5 / 1X = 79% UNVALIDATED_SUBJECTIVE**

The large uncertainty width is why the protected non-loss expression is much stronger than the outright winner.

## L. Corner object

Corner evidence is treated separately from goals.

### Available recent evidence

AEK's known recent team-corner counts include approximately:
- 5 vs Iraklis
- 6 vs Levski
- 2 vs Kifisia
- 3 vs Nestos
- 2 vs Aris

Known five-match mean: roughly **3.6 AEK corners**.

LASK's recent evidence:
- 3 at Celtic in the first leg
- approximately 11 by the end of regulation/stoppage in the Celtic return
- 4 vs Altach
- 14 at Wolfsberger, but that match had an opponent red card in the opening minutes and is therefore **disrupted-match evidence** and heavily downweighted.

### Direct mechanism

- AEK: Koita/Majer wide supply plus Rota/Pilios overlap; if trailing, the home side can increase crossing/end-line pressure.
- LASK: Jørgensen/Bello wing-back structure; if trailing, the back-five system can become a high-width chasing shape.
- Either team's early goal can increase the other side's corner demand.

### Explicit corner centre

AEK recent baseline `3.6`
+ home/width branch `0.3`
= **3.9**

LASK non-disrupted recent/European baseline approximately `6.0`
- stronger-away-opponent/AEK-control shrink `1.3`
= **4.7**

Combined centre ≈ **8.6 total corners**, width roughly **±4.0**.

**Total corners Over 7.5: 60% UNVALIDATED_SUBJECTIVE.**

Important evidence cap: granular current cross / blocked-cross / end-line / clearance rates were not fully available from a field-owning feed. Under `SFA-SOCCER`, this corner row is therefore **FORCED RANK / MEDIUM-LOW**, even though the directional estimate is above 50%. Settlement owner is UEFA official match statistics.

## M. Bidirectional-sign audit / kill paths

| Mechanism | Helps selections | Kill path |
|---|---|---|
| AEK's Varga/Jović front two and current home scoring | AEK O0.5, 1H O0.5, AEK 1X | Champions League step-up can compress domestic conversion |
| Brignoli replacing Strakosha | Can be neutral if experienced replacement performs normally | Raises LASK scoring/keeper uncertainty |
| LASK without Adeniran in XI | AEK 1X, Under 4.5 | Lang/Usor mobility can create transition chances instead |
| LASK high recent scoring | Over 2.5 / corners | Domestic/cup schedule and early-red match inflate raw figures |
| LASK rotated in cup | LASK late attack / Over tail | AEK's home control can prevent that freshness from becoming chances |
| Dry warm weather | Clean technical conditions | Heat can slow tempo before later fatigue opens space |
| AEK early scoring pattern | 1H Over 0.5 | A single 0-0 control state remains meaningful at Matchday 1 |
| Back-five LASK width | Total corners Over | If AEK controls possession without forcing LASK to chase, width may remain conservative |

## N. Ranked five — probability order

| Rank | Selection | UNVALIDATED_SUBJECTIVE | Evidence | Why |
|---:|---|---:|---|---|
| **1** | **AEK Athens +0.5 / Double Chance 1X (90 min)** | **79%** | `SUPPORTED / MEDIUM` | AEK home attacking/defensive process plus draw protection; LASK remain dangerous enough that outright AEK is materially weaker. |
| **2** | **AEK Athens team total Over 0.5 goals** | **78%** | `SUPPORTED / MEDIUM` | Confirmed Varga-Jović pairing, Majer/Koita supply, strong current home shot/goal route; UCL opponent-strength shrink prevents a higher number. |
| **3** | **Combined Total Under 4.5 goals** | **77%** | `SUPPORTED / MEDIUM` | Centre near 3.0 with wide uncertainty; five-goal-plus outcome requires a more extreme conversion/disruption branch. |
| **4** | **1st Half Over 0.5 goals** | **68%** | `LEAN / MEDIUM` | Both confirmed XIs retain genuine early creation/finishing routes; current first-half evidence survives opponent-strength shrink. |
| **5** | **Total Match Corners Over 7.5** | **60%** | `FORCED RANK / MEDIUM-LOW` | Combined corner centre ~8.6 and both teams retain width/chasing routes, but direct cross/end-line event layers are incomplete. |

## O. Supplied-line audit

| Supplied market | Over | Under | Preferred |
|---|---:|---:|---|
| **1H goals 0.5** | **68%** | 32% | **Over 0.5** |
| **Full-match goals 2.5** | **58%** | 42% | **Over 2.5** |

The full-match Over 2.5 is directionally preferred but sits outside the top five because several alternate/protected contracts have materially higher estimated settlement probability.

## P. Potential winner

**Potential 90-minute regulation winner: AEK Athens — 53% UNVALIDATED_SUBJECTIVE.**

- AEK: **53%**
- Draw: **26%**
- LASK: **21%**

This is a **moderate winner lean**, not a lock. The strongest side expression is **AEK +0.5 / 1X**.

Central score family:
- **2-1 AEK**
- **2-0 AEK**
- **1-1**
- secondary tail: **1-0 AEK / 2-2**

## Q. Source register — P-346

### Governing Drive sources
- Google Drive `METHOD.md` — active `MDS-2026.09.06-v4.0`
- Google Drive `RULES_GENERAL.md` §16 — controlling gate classification / explicit arithmetic
- Google Drive `RULES_SOCCER.md` — `SFA-SOCCER`
- Google Drive `CONTROLS.md`
- Google Drive `SOURCES.md`
- Google Drive `LEAGUE_RULES_SOCCER.md` — general soccer/competition-law companion
- Local `PREDICTION_MINI_RUNNING_LOG_P345.md` — queue/ID authority for this external continuation

### Event / lineup / competition sources
- UEFA — AEK Athens vs LASK official squad/match page:
  https://www.uefa.com/uefachampionsleague/match/2049558--aek-athens-vs-lask/lineups/
- UEFA — Matchday 1 starting and predicted line-ups / team news:
  https://www.uefa.com/uefachampionsleague/news/02a9-2188cf675017-df8325ec95c3-1000--champions-league-starting-and-predicted-line-ups-matchday-1-/
- UEFA — 2026/27 league-phase fixtures / kickoff:
  https://www.uefa.com/uefachampionsleague/news/02a9-217ead601a03-116df4b8238f-1000--what-time-do-the-champions-league-league-phase-matches-kic/
- UEFA — AEK vs LASK Matchday 1 facts:
  https://www.uefa.com/uefachampionsleague/news/02a9-2182e063aa24-6dacad176bbc-1000--champions-league-matchday-1-aek-athens-vs-lask-facts/
- UEFA — Matchday 1 referee appointments:
  https://www.uefa.com/uefachampionsleague/news/02a9-218880e7a2aa-96adf63aa534-1000--who-is-the-referee-which-officials-are-in-charge-of-the-uefa/
- Gazzetta Greece — late AEK lineup / Strakosha out:
  https://www.gazzetta.gr/football/champions-league/2567529/aek-lask-me-mprinioli-i-endekada-toy-nikolits
- Current secondary lineup/bench cross-check:
  https://www.oddschecker.com/insight/football/20260908-aek-athens-vs-lask-confirmed-lineups
  **Only lineup/bench metadata was used; odds, tips and predictions were excluded.**

### Form / process sources
- AEK Athens FBref 2026/27 scores and fixtures:
  https://fbref.com/en/squads/d5348c80/2026-2027/matchlogs/all_comps/schedule/AEK-Athens-Scores-and-Fixtures-All-Competitions
- AEK Athens FBref goal logs:
  https://fbref.com/en/squads/d5348c80/2026-2027/goallogs/all_comps/AEK-Athens-Goal-Logs-All-Competitions
- Barnabás Varga FBref 2026 match logs:
  https://fbref.com/en/players/078a52fe/matchlogs/2026/Barnabas-Varga-Match-Logs
- Luka Jović FBref 2026 match logs:
  https://fbref.com/en/players/4d8cd038/matchlogs/2026/summary/Luka-Jovic-Match-Logs
- AEK 4-0 Levski detailed match stats:
  https://www.soccerzz.com/live/2026-08-26-aek-levski-sofia/12378104
- AEK full result archive:
  https://www.besoccer.com/team/matches/aek-athens
- LASK official 2026/27 fixtures/results:
  https://www.lask.at/en/w/matches/pros/fixtures/2026-2027
- LASK official 6-1 Deutschlandsberg report / rotation:
  https://www.lask.at/de/m/news/herren-dsc-lask-2-runde-oefb-cup-spielbericht
- LASK full result archive:
  https://www.besoccer.com/team/matches/lask-linz
- LASK 3-0 Altach detailed stats:
  https://www.telefootball.net/GB/LASK-Linz-SCR-Altach-2026-08-29-665336.html
- LASK vs Celtic 25 Aug match event/stat record:
  https://ofstats.com/matches/view/lask-linz-celtic-2026-08-25

### Venue / environment
- Allwyn / OPAP Arena venue identity and coordinates:
  https://www.thesportsdb.com/venue/26734-opap-arena
- Nea Filadelfeia hourly weather:
  https://www.worldweatheronline.com/nea-filadelfeia-weather/attica/gr.aspx

### Source exclusions
Bookmaker odds, implied probabilities, line movement, betting consensus, tipster/model picks and synthetic/AI-generated predictions were excluded from predictive evidence. The secondary lineup site was used **only** for current bench metadata after the official UEFA XI was independently confirmed.

**P-346 STATUS:** `PREGAME — UNSETTLED`  
**Retrospective:** deferred  
**Next local forecast slot:** **P-347**


### Settlement / retrospective addendum — 2026-09-10

**Current status:** `FINAL / PARTIAL` — ordinary score/side/total rows settled; corner Rank #5 is `TMP-OPEN-20260910-02 / PROVISIONAL RESEARCH WIN`.

**Verified final:** AEK Athens beat LASK **1–0**, half-time **1–0**, through Răzvan Marin's 21st-minute free kick. Guardian records AEK **18 goal attempts** (15 off, 3 on) to LASK 11 and **7–4 corners**.

| Contract | Issued probability | Result |
|---|---:|---|
| Rank #1 AEK +0.5 / 1X | 79% | **WIN** |
| Rank #2 AEK TT Over 0.5 | 78% | **WIN** |
| Rank #3 Under 4.5 goals | 77% | **WIN** |
| Rank #4 1H Over 0.5 | 68% | **WIN** |
| Rank #5 Total corners Over 7.5 | 60% | **PROVISIONAL WIN** — 11 reported; frozen UEFA owner not directly recovered |
| Supplied full Over 2.5 | 58% | **LOSS** |
| Supplied full Under 2.5 | 42% | **WIN** |
| Supplied 1H Under 0.5 | 32% | **LOSS** |
| Potential winner: AEK | 53% | **WIN** |

**Brier, finalized ranked rows only:** mean **0.0620** over 4 rows. The provisional corner row is excluded.

**Q1 — actual driver:** one first-half set-piece conversion plus sustained AEK territorial pressure, followed by enough defensive control to prevent a LASK goal.

**Q2 — knowable?** **Yes at the mechanism level.** The card explicitly identified AEK's home attacking route, the Varga/Jović central pairing, Majer/Koita supply, LASK's reduced direct-box profile without Adeniran starting, and an early-goal branch. The precise Marin free-kick goal was not predictable, but the broad state was.

**Q3 — smallest change:** **none required from this event.** Preserve the set-piece/first-half branch and opponent-strength shrinkage. Do not turn a single clean outcome into a stronger coefficient.

**Card learning / destination:** no new rule. Keep as supporting evidence for the current `RULES_SOCCER.md` state-family approach. The only process action is source-side: a UEFA derivative field needs a directly reachable defined provider before final grading.

**Settlement sources:**
- Reuters combined UCL report: https://www.reuters.com/sports/soccer/torres-helps-villa-hold-off-brugge-marin-fires-aek-victory-2026-09-08/
- Guardian match record: https://www.theguardian.com/football/match/2026/sep/08/aekathens-v-lask
- DFB data-center match record: https://datencenter.dfb.de/en/data-center/champions-league/2026-2027/matchday/2429644
- OFStats event timeline: https://ofstats.com/matches/view/aek-athens-lask-linz-2026-09-08

---


# P-347 — Texas Rangers (Cal Quantrill) @ Seattle Mariners (Bryce Miller) — MLB

**Issued view:** PREGAME  
**Competition:** MLB 2026 regular season  
**Venue:** T-Mobile Park, Seattle, Washington  
**Official scheduled first pitch:** 2026-09-08 18:40 PDT / 2026-09-09 11:40 AEST  
**User-estimated start:** 2026-09-08 19:30 AEST — **superseded by official schedule**  
**Final volatile refresh:** 2026-09-08 18:26:54 PDT / 2026-09-09 11:26:54 AEST  
**State at freeze:** **PREGAME — no play observed; scheduled start not yet reached**  
**Method:** `MDS-2026.09.06-v4.0`  
**Population:** `MLB — PRIMARY_SCORED`  
**Mode:** `SPORTS_ONLY / MARKET_BLIND`  
**Probability tier:** `UNVALIDATED_SUBJECTIVE` — not calibrated  
**Value/edge state:** `NO VALUE DETERMINABLE`  
**Retrospective:** **DEFERRED BY USER**

## A. Queue / state integrity

P-345 and P-346 remain unsettled. Their retrospectives are deferred per explicit user instruction.

The user's estimated time was materially wrong. Current MLB schedule ownership resolves this exact matchup to **18:40 PDT on 8 Sep / 11:40 AEST on 9 Sep**. The forecast freeze at 11:26:54 AEST is therefore legitimately pregame.

## B. Contract / rules freeze

User-supplied:
- Seattle Mariners -1.5
- Texas Rangers +1.5
- Combined total Over 7.5
- Combined total Under 7.5

Additional research-only contracts selected for ranking:
- Seattle team total Under 4.5
- Texas team total Over 2.5

Standard MLB scheduled-nine-inning target with Seattle as home side and home-last-bat entitlement. Extra innings, if tied after nine, use the current MLB placed-runner environment and are included in ordinary eventual winner/run-line settlement subject to operator terms. Exact operator listed-pitcher/action/void wording was not supplied, so `OPERATOR_ACTION = UNKNOWN_DEFINITION` until a provider rule is supplied.

Settlement owner: MLB official game/box score.

## C. Participant handshake

### Starting pitchers
- **Texas: Cal Quantrill, RHP — PROBABLE_OFFICIAL**
- **Seattle: Bryce Miller, RHP — PROBABLE_OFFICIAL**

MLB/Mariners probable-pitcher records and current independent game records agree on Quantrill vs Miller.

### Current batting orders
A current secondary game tracker and lineup feed agree on:

**Texas:** Joc Pederson DH; Corey Seager SS; Ezequiel Duran 3B; Brandon Nimmo RF; Wyatt Langford LF; Evan Carter CF; Jake Burger 1B; Nicky Lopez 2B; Danny Jansen C.

**Seattle:** Randy Arozarena LF; Dominic Canzone RF/DH; Julio Rodríguez CF; Cal Raleigh C; J.P. Crawford SS; Josh Naylor 1B; Cole Young 2B; Lazaro Montes DH/RF; Brock Rodden 3B.

MLB's crawl-visible lineup page had not refreshed to a field-owning posted order before freeze. Therefore batting orders are recorded `SECONDARY_ONLY`, not falsely labelled official-confirmed. Team-level rows are retained; player-prop rows are not promoted.

## D. Availability / bullpen / roster context

### Texas
- Kyle Higashioka remains out with a right flexor strain; Danny Jansen is the current catcher in the secondary posted order.
- Josh Jung remains on the IL with a left calf strain.
- Nathan Eovaldi is unavailable with right posterior elbow inflammation.
- Robert Garcia was activated from the 60-day IL on 7 Sep; his immediate leverage role after the long absence is treated as uncertain.
- Current late-inning alternatives include Jacob Latz, Tyler Alexander and Jakob Junis; Junis worked Sep 3/5/6 but both teams had the Sep 7 off-day.

### Seattle
- Matt Brash is out for the season with a Grade 1 right lat strain, reducing ideal high-leverage bullpen depth.
- Nick Davila is on the 60-day IL.
- Brendan Donovan remains unavailable following concussion symptoms.
- Lazaro Montes had recent hip soreness but appears in the current secondary batting order at DH, reducing the defensive exposure of that issue.
- Andrés Muñoz remains the primary late leverage/closer option.

## E. L5 / L10 / L15 / L20 trend audit

| Window | Texas | Seattle | Interpretation |
|---|---:|---:|---|
| **L5** | **2-3**, 25 RS / 28 RA | **2-3**, 22 RS / 23 RA | Both volatile; no streak ownership |
| **L10** | **5-5** | **3-7** | Texas modestly stronger current results |
| **L15** | approximately **7-8** | approximately **7-8** | No stable directional streak |
| **L20** | **10-10** | **9-11** | Similar broad recent record |

Season snapshot before this game:
- Texas **71-73**, 595 RS / 639 RA, road 31-41.
- Seattle **67-77**, 569 RS / 640 RA, home 38-34.

Trend use is mechanism-limited. No direction is assigned merely because Texas leads recent/H2H records.

## F. Series / H2H continuity

The first ten 2026 meetings before this game produced a **7-3 Texas** season-series lead and a combined **70 runs, 7.0/game**. Because the starting pitchers, roster availability and bullpen state differ game to game, this is descriptive context only, not a predictive coefficient.

## G. Starter exposure chain

### Cal Quantrill
Season:
- 7-5
- **2.79 ERA**
- 96.2 IP
- 1.07 WHIP
- 73 K / 24 BB
- **3.96 FIP**

His run prevention has therefore materially outperformed the defence-independent FIP signal, so the 2.79 ERA is regressed.

Most recent start vs Tampa Bay:
- **7.0 IP, 2 H, 0 R, 2 BB, 5 K**

Recent five-start state is much stronger than the season prior, but that state is retained as a branch rather than copied literally. The key upside is efficient contact suppression; the key kill path is ERA/FIP regression plus Seattle's left-handed/switch-heavy lineup, which attacks Quantrill's relatively weaker platoon side.

### Bryce Miller
Season:
- 4-8
- **4.01 ERA**
- 98.2 IP
- 1.11 WHIP
- 95 K / 26 BB
- **4.22 FIP**
- 17 HR / 1.55 HR per nine

Recent starts show a wide hook/contact distribution:
- Sep 2 @ Boston: 4.2 IP, 7 H, 1 ER, 1 BB, 3 K
- Aug 23 vs Cubs: 4.1 IP, 2 H, 6 ER, **7 BB**, 2 HR, 5 K
- Aug 18 @ Milwaukee: 4.2 IP, 7 H, 5 ER
- Aug 12 @ Yankees: 6.0 IP, 8 H, 5 ER

The rebound at Boston prevents an automatic anti-Miller direction, but the early-hook and clustered-run tail remains materially wider than Quantrill's.

## H. Lineup / platoon interaction

Texas' secondary posted order places left-handed Joc Pederson and Corey Seager near the top, with Brandon Nimmo and Evan Carter also giving left-handed exposure against Miller. Miller's season contact/HR shape has been less comfortable against left-handed hitters than his right-handed split.

Seattle also has a legitimate counter-route: Canzone, Crawford, Naylor, Young and Montes are left-handed, while Raleigh/Rodden can switch, and Quantrill's season split has been weaker against left-handed bats than against right-handed bats.

Therefore the starter advantage favors Texas but does **not** justify a shutout-style Seattle projection.

## I. Bullpen branch

Both clubs had an off-day on Sep 7, so general bullpen freshness is favorable. Freshness is not equated with quality.

Texas' late chain is aided by Latz/Alexander/Junis and the return of Garcia, but Garcia's immediate role after a 60-day absence is uncertain.

Seattle still has Muñoz, Bazardo, Ferrer and Speier, but Brash's season-ending injury removes one high-leverage option. Miller's recent short-start history makes Seattle's middle-to-late relief exposure more important than a simple closer comparison.

## J. Park / weather / roof

T-Mobile Park is an open-air park even when its retractable roof covers the field. MLB's own ballpark guide identifies it as one of MLB's most pitcher-friendly environments.

Current exact-venue weather shortly before first pitch:
- sunny/clear
- approximately 68-71°F / 20-22°C
- no meaningful precipitation threat
- light wind, with independent game-weather reporting around 6-8 mph generally in/cross-in.

Current Seattle-area "Mariners Roof Report" states **roof open** for the 6:40 PM Rangers game. Official Mariners ballpark information confirms the roof covers rather than encloses the park.

Environment direction:
- pitcher-friendly park: negative run adjustment
- mild temperature: near-neutral
- light in/cross-in wind: small negative HR/run adjustment
- roof open: outdoor environment retained

`G15.1 / BB-P3 environment gate`: **PASSED**, with roof status source quality noted as reputable local current report rather than a crawl-visible MLB game-field flag.

## K. Joint run object — explicit arithmetic

This is qualitative v4.0 arithmetic, **not a fitted numerical model**.

### Starting total prior
Season scoring rates:
- Texas: `595 / 144 = 4.13 runs/game`
- Seattle: `569 / 144 = 3.95 runs/game`

Neutral team-score sum:
`4.13 + 3.95 = 8.08`

Signed adjustments:
- `-0.35` T-Mobile Park / open-air pitcher-friendly environment
- `-0.30` Quantrill current starter branch, after regressing 2.79 ERA toward 3.96 FIP
- `+0.25` Miller recent short-hook / walk / HR-cluster tail
- `+0.10` both lineups have useful opposite-handed routes against the starters
- `-0.10` both bullpens enter from an off-day rather than heavy prior-day workload
- `-0.08` light in/cross-in wind / no warm offensive weather boost

**Resulting centre:** `8.08 - 0.35 - 0.30 + 0.25 + 0.10 - 0.10 - 0.08 = 7.60 runs`

**Width:** approximately **±3.3 runs**, widened for MLB run clustering, Miller's hook tail, relief transitions, one-inning HR sequencing and extra-inning placed-runner risk.

### Team component budget
- **Texas: 4.25**
- **Seattle: 3.35**
- Combined: **7.60**

## L. Separation / run-line budget

Team components imply:
`Texas 4.25 - Seattle 3.35 = Texas +0.90 run central separation`

But run-line probability is not read directly from the mean:
- Seattle 2+ win requires the Mariners to overcome the Texas starter edge and then separate.
- Texas +1.5 survives a Texas win, a one-run Texas loss, and most tie-after-nine branches unless extras create 2+ separation.
- MLB extra innings increase the tail of two-run separation because a runner begins in scoring position, so the Texas +1.5 probability is reduced from a naive regulation-only score-grid estimate.

Final subjective run-line split:
- **Texas +1.5: 76%**
- **Seattle -1.5: 24%**

## M. Total-line budget / upper-tail audit

The 7.5 line lies almost exactly on the 7.60 centre.

Under mechanisms:
- T-Mobile Park
- Quantrill central branch
- off-day bullpen freshness
- light in/cross-in wind

Over mechanisms:
- Miller's recent short-hook/walk/HR tail
- Texas' left-handed top-order route
- Seattle's left-handed route against Quantrill
- sequencing, errors, inherited runners
- extra-inning placed runner if tied after nine

Because the upper tail remains material, **Under 7.5 is only a small lean**, not a top-confidence total:
- **Under 7.5: 54%**
- **Over 7.5: 46%**

## N. Alternate component contracts

### Seattle team total Under 4.5
Seattle component centre ≈3.35. It requires Seattle to reach five runs, which generally needs either Quantrill regression plus successful platoon conversion, an early hook, or a bullpen/HR cluster.

**Probability: 71% UNVALIDATED_SUBJECTIVE.**

### Texas team total Over 2.5
Texas component centre ≈4.25. The principal support is Miller's current exit/cluster distribution plus the left-handed lineup route. Kill paths are T-Mobile Park and Miller's Sep 2 rebound.

**Probability: 69% UNVALIDATED_SUBJECTIVE.**

## O. Mandatory branches / bidirectional-sign audit

| Branch | Effect |
|---|---|
| Both starters central | Texas modest edge; total around 6-8 |
| Quantrill early regression/hook | Seattle scoring and Over tail rise sharply |
| Miller early hook | Texas TT Over and Rangers side strengthen; could still be Under if Seattle is suppressed |
| HR/sequencing cluster | Raises Over and can create 2+ margin |
| One-sided 3-0 / 4-1 Texas | Supports Rangers side while still supporting Under |
| One-run Seattle win | Rangers +1.5 still wins |
| Seattle 2+ win | Only direct Rangers +1.5 loss path |
| Tie after nine | Extra-inning placed runner raises both total and 2-run-separation tails |
| Bullpens from off-day | Small Under support, but score-state determines which arms actually appear |

## P. Ranked four

| Rank | Selection | UNVALIDATED_SUBJECTIVE | Evidence |
|---:|---|---:|---|
| **1** | **Texas Rangers +1.5** | **76%** | `SUPPORTED / MEDIUM-HIGH` |
| **2** | **Seattle Mariners team total Under 4.5** | **71%** | `SUPPORTED / MEDIUM` |
| **3** | **Texas Rangers team total Over 2.5** | **69%** | `SUPPORTED / MEDIUM` |
| **4** | **Combined Total Under 7.5** | **54%** | `LEAN / MEDIUM-LOW` |

## Q. Supplied-line coherence audit

| Supplied row | Probability |
|---|---:|
| **Rangers +1.5** | **76%** |
| Mariners -1.5 | **24%** |
| **Under 7.5** | **54%** |
| Over 7.5 | **46%** |

Both half-run complementary pairs sum to 100%.

## R. Potential winner

**Potential eventual game winner: Texas Rangers — 55% UNVALIDATED_SUBJECTIVE.**

Seattle: **45%**.

This is a modest winner lean, not a strong moneyline view. The safer side expression is **Texas +1.5**.

Central score family:
- **Texas 4-3**
- **Texas 4-2**
- **Texas 5-3**
- **Seattle 4-3** as the main opposing branch.

## S. Source register — P-347

### Drive / method
- Google Drive `METHOD.md` — `MDS-2026.09.06-v4.0`
- Google Drive `RULES_GENERAL.md` §16
- Google Drive `CONTROLS.md`
- Google Drive `SOURCES.md`
- Google Drive `RULES_BASEBALL.md` — `SFA-BASEBALL`, 2026 MLB ABS/rules environment
- Local `PREDICTION_MINI_RUNNING_LOG_P345.md`

### Official / primary baseball sources
- MLB / Mariners 2026 standings:
  https://www.mlb.com/mariners/standings
- Seattle Mariners T-Mobile Park facts / roof:
  https://www.mlb.com/mariners/ballpark/ground-rules
- MLB / Mariners Bryce Miller game report:
  https://www.mlb.com/mariners/news/bryce-miller-struggles-again-in-mariners-loss-to-cubs
- Official Rangers/Mariners injury and transaction pages consulted during the current pregame pass.
- MLB official schedule / probable-pitcher structured records used for exact start time and Quantrill/Miller identity.

### Current statistical / reporting sources
- Baseball-Reference — Texas 2026 pitching:
  https://www.baseball-reference.com/teams/TEX/2026.shtml
- StatMuse — Cal Quantrill 2026 / FIP:
  https://www.statmuse.com/mlb/ask/cal-quantrill-fip
- StatMuse — Bryce Miller 2026:
  https://www.statmuse.com/mlb/ask/bryce-miller-2026
- CBS Sports — Bryce Miller 2026 game log:
  https://www.cbssports.com/mlb/players/26911810/bryce-miller/game-log/
- Reuters — Quantrill seven shutout innings vs Tampa Bay:
  https://www.reuters.com/sports/baseball/cal-quantrill-tosses-seven-shutout-innings-rangers-blank-rays--flm-2026-09-04/
- Reuters — Miller one-run outing at Boston:
  https://www.reuters.com/sports/baseball/jp-crawford-helps-mariners-sail-past-red-sox--flm-2026-09-02/
- CBS current game tracker — current secondary batting orders:
  https://www.cbssports.com/mlb/gametracker/preview/MLB_20260908_TEX@SEA/
- PitcherStat current lineup page — secondary corroboration only; starter-label swap on that page was explicitly ignored:
  https://pitcherstat.com/matchup/texas-rangers-vs-seattle-mariners-2026-09-08/lineup
- Seattle Sports / MyNorthwest — current Mariners Roof Report:
  https://sports.mynorthwest.com/seattle-mariners

### Environment
- Exact T-Mobile Park structured weather feed: sunny, approximately 71°F shortly before first pitch.
- T-Mobile Park current game weather reporting: clear, upper 60s, light in/cross-in wind.
- Official Mariners ground rules confirm the roof's cover-not-enclose design and field characteristics.

### Explicit exclusions
No bookmaker odds, implied probabilities, consensus, line movement, tipster picks or synthetic predictions were used as predictive evidence. A secondary page that displayed odds was used only for batting-order metadata after the predictive market fields were excluded.

**P-347 STATUS:** `PREGAME — UNSETTLED`  
**Retrospective:** deferred  
**Next local forecast slot:** **P-348**


### Settlement / retrospective addendum — 2026-09-10

**Current status:** `FINAL / SETTLED`.

**Official final:** Texas Rangers **10–5** Seattle Mariners. MLB's game record shows Bryce Miller lasted **3.2 IP and allowed 4 ER**; Texas then produced a five-run fifth inning. Cal Quantrill went **6.0 IP, 3 ER**.

| Contract | Issued probability | Result |
|---|---:|---|
| Rank #1 Rangers +1.5 | 76% | **WIN** |
| Rank #2 Seattle TT Under 4.5 | 71% | **LOSS** — Seattle 5 |
| Rank #3 Texas TT Over 2.5 | 69% | **WIN** — Texas 10 |
| Rank #4 Under 7.5 | 54% | **LOSS** — total 15 |
| Supplied Seattle -1.5 | 24% | **LOSS** |
| Supplied Over 7.5 | 46% | **WIN** |
| Potential winner: Texas | 55% | **WIN** |

**Brier:** mean **0.2374** over 4 ranked rows.

**Q1 — actual driver:** Miller's short-start branch materialized, and the first relief transition failed to stop the run cluster. Seattle simultaneously hit the Rangers for a three-run fourth-inning homer and later added two runs, taking its team total to five.

**Q2 — knowable?** **Yes.** The card explicitly listed Miller's “short-hook / walk / HR-cluster tail,” Texas' left-handed route, inherited-runner/sequencing risk, and a material upper-total tail. It still placed the joint centre at only 7.60 and made Seattle Under 4.5 a 71% Rank #2.

**Q3 — smallest change:** under existing `G-L1` / `BB-B2` / `BB-B3`, translate a named starter-hook/HR-cluster kill path into explicit probability mass **before** granting a high-confidence opponent team Under. Do not let the centre conceal the branch already identified as dangerous.

**Deep review.** What went right: Texas side and Texas team-over mechanisms were correct; Rank #1 won. What went wrong: two Under-type rows lost because the same wide upper-tail mechanism was acknowledged but underweighted. Seattle Under 4.5 missed by only **0.5 run**, adding another observation to the existing distance-to-line watch. No new hard rule is warranted; this is enforcement of existing state-family geometry.

**Recommended destination:** `RULES_BASEBALL.md` state-family/relief-transition implementation note; `LEARNING_REGISTER.md` observation under existing distance-to-line and cluster-tail candidates.

**Settlement source:** MLB official Film Room/game summary: https://www.mlb.com/video/game/823092

---


# P-348 — Toronto Blue Jays (José Soriano) @ Athletics (Jack Perkins) — MLB

**Issued view:** PREGAME  
**Competition:** MLB 2026 regular season  
**Venue:** Sutter Health Park, West Sacramento, California  
**Official scheduled first pitch:** 2026-09-08 18:40 PDT / 2026-09-09 11:40 AEST  
**Final volatile refresh:** 2026-09-08 18:32:53 PDT / 2026-09-09 11:32:53 AEST  
**State at freeze:** **PREGAME — scheduled start not reached; no play incorporated**  
**Method:** `MDS-2026.09.06-v4.0`  
**Population:** `MLB — PRIMARY_SCORED`  
**Mode:** `SPORTS_ONLY / MARKET_BLIND`  
**Probability tier:** `UNVALIDATED_SUBJECTIVE` — not calibrated  
**Value/edge state:** `NO VALUE DETERMINABLE`  
**Retrospective:** **DEFERRED BY USER**

## A. Identity / starter / contract freeze

Official Athletics probable-pitcher record:
- Toronto: **José Soriano, RHP — PROBABLE_OFFICIAL**, 11-7, 3.52 ERA, 151 SO.
- Athletics: **Jack Perkins, RHP — PROBABLE_OFFICIAL**, 3-10, 6.50 ERA, 116 SO.

User-supplied contracts:
- Toronto Blue Jays -1.5
- Athletics +1.5
- Combined total Over 9.0
- Combined total Under 9.0

Additional research-only contracts:
- Toronto team total Over 3.5 runs
- Athletics team total Over 3.5 runs

Standard MLB scheduled-nine-inning target. Athletics own home-last-bat entitlement. Extra innings retain the current placed-runner scoring regime. Exact operator listed-pitcher/action/void terms were not supplied, so `OPERATOR_ACTION = UNKNOWN_DEFINITION` where relevant.

Settlement owner: MLB official game/box score.

## B. Current batting orders / availability

MLB's crawl-visible starting-lineup page still displayed `TBD` at the research cutoff, so the batting orders are **not falsely labelled CONFIRMED_OFFICIAL**. Multiple current reports, including a game thread quoting the official Blue Jays team post, agree on:

**Toronto**
1. Brett Bateman CF
2. Nathan Lukes RF
3. Vladimir Guerrero Jr. 1B
4. Alejandro Kirk C
5. Josh Smith LF
6. Kazuma Okamoto 3B
7. Andrés Giménez SS
8. Jesús Sánchez DH
9. Ernie Clement 2B

**Athletics**
1. Henry Bolte CF
2. Jeff McNeil 1B
3. Zack Gelof 3B
4. Lawrence Butler RF
5. Carlos Cortes LF
6. Tommy White DH
7. Donovan Walton 2B
8. Alika Williams SS
9. Jonah Heim C

**Lineup status:** `SECONDARY_ONLY / CURRENT-CONCORDANT`, with team-level rows retained and player props not promoted.

Availability notes:
- George Springer is not in Toronto's current starting order. No injury diagnosis is assigned without a current field-owning report.
- Athletics official injury updates: J.T. Ginn is on the 15-day IL with a right elbow impingement; Perkins was recalled after Ginn's IL placement.
- Athletics catcher Shea Langeliers remains on the IL with a torn right meniscus.
- The Athletics have multiple longer-term injured bats/players; current starting nine above is used rather than old expected lineups.
- Toronto's Jameson Taillon is on the IL with right elbow inflammation, relevant to rotation depth but not directly to tonight's starting role.

## C. Trend / form audit

### Toronto
Current season snapshot entering the series: 72-73 after the opener; approximately 580 RS and 618 RA through the preceding completed-game snapshot.

Recent run production:
- last five completed games before tonight: **25 runs**, including 9, 6, 5 and 4-run outputs.
- recent sequence includes an 11-0 win at Cleveland on Sep 2 and 9-2 at Kansas City on Sep 4.
- the prior game at Sutter Health Park ended in a 6-5 Athletics win.

### Athletics
Current season snapshot: **58-87, 637 RS, 824 RA**, run differential -187.
Recent offense:
- **26 runs in the last five games**.
- recent outputs: 7, 7, 6, 0, 6.
- the prior game against Toronto produced six runs despite only six hits, with aggressive baserunning and Toronto defensive miscues.

**L5/L10/L15/L20 use:** recent windows are treated as mechanism diagnostics, not streak weights. The Athletics' recent scoring is supported by actual HR/extra-base and baserunning events, while Toronto's recent scoring has been volatile but capable of multi-run clusters.

## D. H2H / series-state continuity

The Athletics won the series opener **6-5**. That result itself carries no directional weight.

Knowable carryover mechanisms:
- Athletics relievers Luis Medina and Hogan Harris were used in the opener and allowed Toronto to erase a late deficit before Oakland walked it off.
- Toronto's bullpen was also exposed in a tight late game.
- Soriano has a poor career record against the Athletics (1-3, 7.52 ERA in 10 appearances), but his two starts against them earlier in 2026 were materially better (~3.86 ERA). Old H2H is therefore descriptive only.

## E. Starter object

### José Soriano
- Season: 11-7, 3.52 ERA, 151 K in roughly 156 IP.
- Since joining Toronto: reported **4.36 ERA** across eight games / six starts.
- Most recent outing: 4.2 IP, 6 H, 3 ER.
- Current Toronto form therefore does not justify treating him as a 3.52-ERA automatic stopper.
- Main strength branch: established innings volume / better season run prevention than Perkins.
- Kill paths: Athletics' current right/left balance, Sutter run environment, and Soriano's less dominant post-trade results.

### Jack Perkins
- Season: 3-10, **6.50 ERA**, 1.54 WHIP.
- Statcast 2026: approximately **4.04 xERA**, .310 xwOBA, 25.7% K, 10.4% BB, 37.5% hard-hit.
- The ERA therefore materially overstates the quality implied by his contact indicators, but his command remains weak and creates early-hook / free-pass / inherited-runner risk.
- Recent seven-outing report: ~6.60 ERA, 1.93 WHIP, 38 H and 20 BB in 30 IP.
- Latest start: only three innings, five walks, one hit batter, three runs.

This is a **wide exit-distribution starter**, not simply a 6.50 ERA deterministic Toronto-over switch.

## F. Park / weather / current surface

Baseball Savant 2026 Sutter Health Park:
- overall park factor **113**
- runs factor approximately **128**
- HR factor approximately **127**
- observed as one of MLB's strongest run/HR amplifiers in 2026.

Venue weather near first pitch:
- approximately **91°F / 33°C**
- dry / partly sunny
- no rain threat.

Mechanism:
- warm air plus current park geometry materially expands the HR/extra-base/cluster tail.
- heat is not treated as a fixed coefficient, but the direction aligns with the observed Sutter park environment.

`G15.1`: **PASSED** with exact-venue hourly forecast.

## G. Bullpen / relief-chain branch

Athletics pitching has been the weakest staff environment in MLB by season results, including a reported **6.33 home ERA**. Recent bullpen results have improved, but the prior Toronto game again showed late leakage.

The key structural point:
- Perkins' short-start risk creates large middle-relief exposure.
- Toronto's highest-leverage path is therefore not only "score off Perkins", but "force a short Perkins outing and attack the home relief chain".
- Athletics' offense also has a live Toronto-middle-relief path if Soriano exits around 5 innings.

Freshness is kept separate from quality.

## H. Joint run object — explicit arithmetic

Season scoring baseline:
- Toronto: `580 / 144 ≈ 4.03`
- Athletics: `637 / 145 ≈ 4.39`
- neutral sum: **8.42**

Signed adjustments:
- `+0.60` Sutter Health Park 2026 run/HR environment, heavily shrunk from raw park-factor magnitude
- `+0.30` 91°F / warm dry conditions increasing carry and late fatigue
- `+0.45` Perkins command / short-hook / relief-transition branch after regressing 6.50 ERA toward 4.04 xERA
- `+0.20` Athletics current scoring mechanism plus Soriano's less dominant Toronto stint
- `-0.20` George Springer absent from Toronto's starting order
- `+0.10` prior-game bullpen/late-inning exposure and Athletics home staff fragility

**Resulting centre:** `8.42 + 0.60 + 0.30 + 0.45 + 0.20 - 0.20 + 0.10 = 9.87 runs`

Rounded working centre: **~9.9 runs**  
Width: approximately **±4.0 runs**, widened for Perkins hook risk, Sutter HR clusters, Athletics defensive volatility, bullpen transitions and MLB extra-inning scoring.

Team components:
- **Toronto ~5.45**
- **Athletics ~4.45**
- Combined **~9.90**

## I. Separation / run-line budget

Central team difference:
`Toronto 5.45 - Athletics 4.45 = Toronto +1.00`

Subjective eventual winner:
- Toronto **60%**
- Athletics **40%**

Run-line decomposition:
- Athletics +1.5 wins through any Oakland win or exactly-one-run Toronto win.
- Toronto -1.5 requires Toronto to win by two or more.
- The same Perkins/relief cluster that creates Toronto upside also creates the Toronto multi-run-win branch.
- The same hot park and Athletics scoring route that supports the Over protects Athletics +1.5 against a large share of Toronto wins.

Final:
- **Athletics +1.5: 61%**
- **Toronto -1.5: 39%**

## J. Integer total 9.0 settlement audit

Because 9.0 is an integer:
- Over wins at **10+**
- Push at **exactly 9**
- Under wins at **8 or fewer**

Final subjective mass:
- **Over 9.0 WIN: 54%**
- **PUSH: 10%**
- **Under 9.0 WIN: 36%**

The Over direction is supported, but the integer push mass prevents it from outranking the safer team-total thresholds.

## K. Additional component contracts

### Toronto team total Over 3.5
Centre ≈5.45. Support:
- Perkins walk/hook volatility
- Athletics season/home run prevention
- Sutter heat/park factor
- Toronto still retains Guerrero/Kirk/Okamoto/Giménez despite Springer sitting

**Probability: 73% UNVALIDATED_SUBJECTIVE.**

### Athletics team total Over 3.5
Centre ≈4.45. Support:
- 26 runs in last five
- Sutter environment
- Soriano's Toronto stint less dominant than full-season ERA
- home ninth-inning entitlement

**Probability: 62% UNVALIDATED_SUBJECTIVE.**

## L. Ranked four

| Rank | Selection | UNVALIDATED_SUBJECTIVE | Evidence |
|---:|---|---:|---|
| **1** | **Toronto Blue Jays team total Over 3.5 runs** | **73%** | `SUPPORTED / MEDIUM` |
| **2** | **Athletics team total Over 3.5 runs** | **62%** | `SUPPORTED / MEDIUM` |
| **3** | **Athletics +1.5** | **61%** | `LEAN / MEDIUM` |
| **4** | **Combined Total Over 9.0 runs** | **54% win / 10% push / 36% loss** | `LEAN / MEDIUM` |

## M. Supplied-line audit

| Supplied row | Probability |
|---|---:|
| Blue Jays -1.5 | **39%** |
| **Athletics +1.5** | **61%** |
| **Over 9.0** | **54% win / 10% push** |
| Under 9.0 | **36% win / 10% push** |

## N. Potential winner

**Toronto Blue Jays — 60% eventual-game-win probability (`UNVALIDATED_SUBJECTIVE`).**

Central score family:
- **Toronto 6-5**
- **Toronto 6-4**
- **Toronto 7-5**
- **Athletics 6-5** as the primary opposing branch.

This is a winner lean, not a strong run-line endorsement.

## O. Source register — P-348

### Drive
- Google Drive `RULES_BASEBALL.md` — fresh read; SFA-BASEBALL / participant, hook, relief, park, extras and run-line controls.
- Existing current-session `METHOD.md`, `RULES_GENERAL.md`, `CONTROLS.md` governing v4.0 workflow.
- Local continuation `PREDICTION_MINI_RUNNING_LOG_P347.md`.

### Official / primary
- MLB Athletics probable pitchers:
  https://www.mlb.com/athletics/roster/probable-pitchers/1000
- MLB Athletics starting-lineup page:
  https://www.mlb.com/athletics/roster/starting-lineups/1000
- MLB Blue Jays starting-lineup page:
  https://www.mlb.com/bluejays/roster/starting-lineups
- MLB Athletics injury / transaction updates:
  https://www.mlb.com/athletics/news
- MLB Athletics injuries / roster moves:
  https://www.mlb.com/athletics/news/athletics-injuries-and-roster-moves
- MLB Blue Jays news / injury updates:
  https://www.mlb.com/bluejays/news
- MLB standings:
  https://www.mlb.com/standings/mlb
- Baseball Savant 2026 Sutter Health Park factors:
  https://baseballsavant.mlb.com/leaderboard/statcast-park-factors?condition=All&parks=mlb&rolling=1&stat=index_wOBA&type=year&year=2026
- Baseball Savant Jack Perkins 2026:
  https://baseballsavant.mlb.com/savant-player/jack-perkins-678022?season=2026

### Current secondary / reporting
- Blue Jays Nation current game-day lineup report:
  https://bluejaysnation.com/news/september-8-gameday-jose-soriano-gets-the-ball-as-toronto-blue-jays-look-to-bounce-back-against-athletics
- Athletics Nation current game thread / current lineup and matchup context:
  https://www.athleticsnation.com/athletics-game-information/109463/game-146-as-vs-blue-jays-game-thread
- Athletics Nation prior-game recap:
  https://www.athleticsnation.com/athletics-scores-and-standings/109403/as-walk-off-blue-jays-6-5
- Reuters Sep 8 MLB roundup (prior-game result):
  https://www.reuters.com/sports/mlb-roundup-jesus-luzardo-blanks-braves-phillies-earn-series-split--flm-2026-09-08/
- StatMuse recent team game/run logs for Toronto and Athletics.
- Structured exact-venue weather feed for Sutter Health Park / West Sacramento.

### Explicit exclusions
Bookmaker odds, implied probabilities, market movement, betting consensus, tipster picks and synthetic predictions were excluded. A betting-adjacent lineup source found during research was not used for predictive market information.

**P-348 STATUS:** `PREGAME — UNSETTLED`  
**Retrospective:** deferred  
**Next local forecast slot:** **P-349**


### Settlement / retrospective addendum — 2026-09-10

**Current status:** `FINAL / SETTLED`.

**Official final:** Toronto Blue Jays **4–2** Athletics. José Soriano went **7.0 IP, 2 ER**; Jack Perkins went **5.0 IP, 4 ER**.

| Contract | Issued probability | Result |
|---|---:|---|
| Rank #1 Toronto TT Over 3.5 | 73% | **WIN** — exactly 4 |
| Rank #2 Athletics TT Over 3.5 | 62% | **LOSS** — 2 |
| Rank #3 Athletics +1.5 | 61% | **LOSS** — Toronto won by 2 |
| Rank #4 Over 9.0 | 54% win / 10% push | **LOSS** — total 6 |
| Supplied Toronto -1.5 | 39% | **WIN** |
| Supplied Under 9.0 | 36% win / 10% push | **WIN** |
| Potential winner: Toronto | 60% | **WIN** |

**Brier:** mean **0.2803** over 4 ranked rows.

**Q1 — actual driver:** Toronto did enough to cross its 3.5 team line, but Soriano suppressed Oakland for seven innings and the hot Sutter environment did not produce the expected two-sided run cluster.

**Q2 — knowable?** **Partly.** The card correctly regressed Perkins' 6.50 ERA toward stronger contact indicators and acknowledged Soriano's established starter branch. But the total arithmetic stacked `+0.60` park, `+0.30` heat, `+0.20` Athletics current scoring and additional relief/fragility terms. Several may have represented overlapping manifestations of the same run-amplifying environment.

**Q3 — smallest change:** add an explicit **mechanism-overlap check** inside the existing bidirectional/double-count audit: park factor, same-park recent scoring, hot-weather carry and bullpen run environment cannot each receive independent full signed increments unless their incremental evidence is separable.

**Deep review.** The supplied Blue Jays -1.5 and Under 9.0 both won even though the ranked card preferred Athletics +1.5 and Over 9.0. This was not just variance around the centre; the side/total state tree over-allocated the “both teams score in Sutter” branch. Rank #1 barely won by 0.5 run, so the card as a whole should not be treated as strongly validated.

**Recommended destination:** `RULES_GENERAL.md` G22/G-L1 implementation note and `RULES_BASEBALL.md` environment arithmetic. Record as `OBSERVATION/CANDIDATE`, not a new hard rule pending recurrence.

**Settlement sources:**
- MLB official Film Room/game summary: https://www.mlb.com/video/game/824957
- MLB official game story: https://www.mlb.com/stories/game/824957/

---


# P-349 — St. Louis Cardinals (Quinn Mathews) @ San Francisco Giants (Landen Roupp) — MLB

**Issued view:** PREGAME  
**Competition:** MLB 2026 regular season  
**Venue:** Oracle Park, San Francisco, California  
**Official first pitch:** 2026-09-08 18:45 PDT / 2026-09-09 11:45 AEST  
**Final volatile refresh:** 2026-09-08 18:42:28 PDT / 2026-09-09 11:42:28 AEST  
**State at freeze:** **PREGAME — scheduled start not reached; no live play incorporated**  
**Method:** `MDS-2026.09.06-v4.0`  
**Population:** `MLB — PRIMARY_SCORED`  
**Mode:** `SPORTS_ONLY / MARKET_BLIND`  
**Probability tier:** `UNVALIDATED_SUBJECTIVE`  
**Retrospective:** **DEFERRED BY USER**

## Identity / contracts / starter handshake

Official MLB pages and current game records agree:
- STL: **Quinn Mathews, LHP — PROBABLE_OFFICIAL**, 1-2, 4.38 ERA, 24 SO in 24.2 IP.
- SF: **Landen Roupp, RHP — PROBABLE_OFFICIAL**, 8-13, 4.17 ERA, 137 SO in 144.2 IP.

Supplied:
- Cardinals -1.5
- Giants +1.5
- Over 7.5
- Under 7.5

Additional team contracts selected:
- Giants team total Under 4.5
- Cardinals team total Under 4.5

Standard scheduled-nine-inning MLB target, SF home-last-bat, current placed-runner extra-inning regime. Operator listed-pitcher/action terms not supplied.

## Lineup / availability state

MLB's official starting-lineup pages still displayed `TBD` at the pregame cutoff. Therefore:
- full batting orders = **OVERDUE_NOT_RELEASED / field-owner crawl**
- current secondary lineup data = **SECONDARY_ONLY**
- no player prop promoted
- all lineup-sensitive team rows capped below high confidence.

Current official transaction:
- **Masyn Winn activated from the IL on Sep 8**; César Prieto optioned.
Cardinals injuries still include Peter Strzelecki (forearm extensor inflammation), Hunter Dobbins (UCL/flexor surgery), and JJ Wetherholt (wrist tendinitis).
Giants are without major pieces including **Willy Adames** (left elbow sprain), **Matt Chapman** (60-day IL), **Casey Schmitt** (60-day IL), **Keaton Winn** (60-day IL), and **Sam Hentges** (forearm strain). SF recalled Brett Harris on Sep 8.

## Form windows

Baseball-Reference current snapshot:
- STL: L10 **5-5**, L20 **8-12**
- SF: L10 **5-5**, L20 **9-11**

Recent run production:
- STL last 20: **103 runs = 5.15/game**
- SF last 20: **67 runs = 3.35/game**
- STL last 10: **61 runs = 6.1/game**
- SF latest 5: **24 runs = 4.8/game**

Recent scoring is treated as diagnostic only, not a streak weight.

## Starter exposure

### Quinn Mathews
- 5 MLB starts, 24.2 IP, 4.38 ERA, **1.58 WHIP**
- 27 H, 12 BB, 24 K, only 1 HR allowed
- has allowed 2 runs or fewer in 4 of 5 starts
- latest: 5 IP, 1 R vs LAD

Small-sample rule applies. His good-start branch is real, but 12 walks in 24.2 IP and only five MLB starts keep an ordinary/early-hook tail wide.

### Landen Roupp
- 144.2 IP, 4.17 ERA, 1.29 WHIP
- Statcast: **3.75 xERA**, .300 xwOBA, 29.3% hard-hit, 4.8% barrel, 22.6% K, 11.1% BB
- latest: 5 IP, 1 R vs PIT

Roupp's contact quality is materially better than his ERA alone suggests, but the 11.1% walk rate preserves free-pass/sequencing risk.

## Platoon / lineup mixture

The last field-owning MLB lineup available before tonight showed STL carrying multiple dangerous left-handed bats (Burleson, Gorman, Church) against Roupp, while SF's recent core includes Devers, Eldridge and Jung Hoo Lee from the left side against Mathews.

That matters because Mathews' handedness can suppress part of SF's best left-handed power route, while Roupp faces meaningful left-handed exposure from STL. The exact orders were unresolved, so this is modeled as a lineup mixture rather than a claimed confirmed matchup.

## Prior-game / bullpen state

Series opener: SF won **5-4 in 11 innings**.
- both clubs required extra-inning bullpen exposure
- SF's Jason Foley worked the 11th
- the prior result itself gets zero directional weight
- the only carryover is additional relief workload and possible leverage-arm availability constraints.

## Park / weather

Oracle Park remains a run-suppressing venue relative to a neutral MLB environment, especially for non-pulled fly-ball power.

Game-window weather sources around first pitch:
- approximately **70°F / 21°C**
- dry, no meaningful rain threat
- roughly **6-8 mph breeze**, with one game-specific source reporting it out toward left-center.

The wind slightly offsets the park's run suppression but does not reverse it.

## Joint run object

Recent-offense starting prior:
- STL L20: 5.15
- SF L20: 3.35
- combined = **8.50**

Signed adjustments:
- `-0.55` Oracle Park run suppression
- `-0.40` Roupp contact-quality/xERA branch
- `-0.25` Mathews good-start / low-HR branch, aggressively shrunk for five-start sample
- `+0.30` Mathews walk / early-hook uncertainty
- `+0.20` both bullpens exposed in an 11-inning opener
- `+0.10` mild warm/wind-out weather
- `-0.20` SF left-handed core facing LHP Mathews

**Centre: 7.70 runs**  
**Width: approximately ±3.3 runs**

Team components:
- **STL 4.05**
- **SF 3.65**

## Separation

Central difference:
`STL 4.05 - SF 3.65 = STL +0.40`

Home-last-bat and Roupp's stronger established starter profile keep the outright result close despite STL's stronger recent offense.

Subjective eventual winner:
- **STL 52%**
- **SF 48%**

Run-line:
- **Giants +1.5: 68%**
- **Cardinals -1.5: 32%**

## Total 7.5

The 7.5 line is just below the 7.70 centre, but Oracle/Roupp/Mathews-good-start branches compete against the rookie-walk/bullpen/extra-inning upper tail.

Final:
- **Under 7.5: 53%**
- **Over 7.5: 47%**

This is intentionally a weak total lean.

## Ranked four

| Rank | Selection | UNVALIDATED_SUBJECTIVE | Evidence |
|---:|---|---:|---|
| **1** | **San Francisco Giants +1.5** | **68%** | `SUPPORTED / MEDIUM` |
| **2** | **Giants team total Under 4.5** | **66%** | `SUPPORTED / MEDIUM-LOW` |
| **3** | **Cardinals team total Under 4.5** | **63%** | `LEAN / MEDIUM-LOW` |
| **4** | **Combined Total Under 7.5** | **53%** | `LEAN / LOW-MEDIUM` |

## Supplied-line audit

| Supplied row | Probability |
|---|---:|
| Cardinals -1.5 | **32%** |
| **Giants +1.5** | **68%** |
| Over 7.5 | **47%** |
| **Under 7.5** | **53%** |

## Potential winner

**St. Louis Cardinals — 52% eventual-game-win probability.**

This is essentially a near-coin-flip winner lean; the protected **Giants +1.5** is materially stronger than either outright side.

Central score family:
- STL 4-3
- STL 4-2
- SF 4-3
- STL 3-2

## Source register

Drive:
- `METHOD.md` — `MDS-2026.09.06-v4.0`
- `RULES_BASEBALL.md` — fresh read, `SFA-BASEBALL`
- current local running-log continuation

Official / primary:
- MLB Giants / Cardinals starting-lineup pages (official starter identity; batting orders still TBD at cutoff)
- MLB Quinn Mathews player page
- MLB Landen Roupp player page
- Baseball Savant Mathews/Roupp pages
- MLB Sep 8 transactions
- MLB Cardinals injuries / roster moves
- MLB Giants injuries / roster moves
- MLB game preview

Current reporting / statistical:
- Reuters Sep 8 Giants 5-4 Cardinals 11-inning opener recap
- Baseball-Reference Sep 8 game preview / team L10/L20
- StatMuse STL/SF recent run logs
- McCovey Chronicles Sep 8 game thread
- San Francisco game-window weather sources

Market odds, bookmaker implied probabilities, line movement and tipster picks were excluded.

**P-349 STATUS:** `PREGAME — UNSETTLED`  
**Retrospective:** deferred  
**Next local forecast slot:** **P-350**


### Settlement / retrospective addendum — 2026-09-10

**Current status:** `FINAL / SETTLED`.

**Official final:** San Francisco Giants **2–1** St. Louis Cardinals. Landen Roupp threw **6.0 scoreless innings**; Quinn Mathews allowed **2 ER in 6.0 innings**. St. Louis scored only in the ninth.

| Contract | Issued probability | Result |
|---|---:|---|
| Rank #1 Giants +1.5 | 68% | **WIN** |
| Rank #2 Giants TT Under 4.5 | 66% | **WIN** |
| Rank #3 Cardinals TT Under 4.5 | 63% | **WIN** |
| Rank #4 Under 7.5 | 53% | **WIN** |
| Supplied Cardinals -1.5 | 32% | **LOSS** |
| Supplied Over 7.5 | 47% | **LOSS** |
| Potential winner: St. Louis | 52% | **LOSS** |

**Brier:** mean **0.1440** over 4 ranked rows.

**Q1 — actual driver:** both starters controlled run scoring, while San Francisco got just enough early separation and protected it. The low-scoring environment made the +1.5 cushion robust but did not determine the outright winner.

**Q2 — knowable?** **Yes in broad form.** Oracle suppression, Roupp's contact-quality branch, Mathews' low-HR/good-start branch and bullpen uncertainty were all present. The exact 2–1 allocation was not.

**Q3 — smallest change:** none. Preserve the distinction between a high-probability protected side and a near-coin-flip winner. The wrong 52% potential-winner call does not invalidate the correctly specified +1.5/Under structure.

**Recommended destination:** no rule change. Keep as an example in `LEARNING_REGISTER.md` only if a future review needs evidence that low totals do not uniquely determine the outright side.

**Settlement source:** MLB official Film Room/game summary: https://www.mlb.com/video/game/823174

---


# P-350 — Ben Shelton vs Carlos Alcaraz — US Open Men's Singles Quarterfinal

**Issued view:** PREGAME  
**Competition:** 2026 US Open — Men's Singles Quarterfinal  
**Venue:** Arthur Ashe Stadium, USTA Billie Jean King National Tennis Center, Flushing Meadows, New York  
**Surface:** Outdoor hard court; retractable-roof venue  
**Format:** Best of five sets; final-set match tiebreak at 6-6 under current Grand Slam rules  
**Structured scheduled start:** 2026-09-09 02:10 UTC / 2026-09-09 12:10 AEST / 2026-09-08 22:10 EDT  
**User-estimated start:** 12:00 AEST — superseded by current structured tournament schedule  
**Final volatile refresh:** 2026-09-09 11:49:54 AEST / 2026-09-08 21:49:54 EDT  
**State at freeze:** **PREGAME / NOT_STARTED**  
**Method:** `MDS-2026.09.06-v4.0`  
**Algorithm:** `SFA-TENNIS`  
**Population:** `US OPEN MEN'S SINGLES — EXPLORATORY / NOT PRIMARY_SCORED`  
**Mode:** `SPORTS_ONLY / MARKET_BLIND`  
**Probability tier:** `UNVALIDATED_SUBJECTIVE` — not calibrated  
**Retirement / walkover operator terms:** `UNKNOWN_DEFINITION`; research probabilities assume normal match completion under US Open scoring, while operator action remains unknown if retirement/walkover occurs  
**Retrospective:** **DEFERRED BY USER**

## A. Identity / participant freeze

- **Ben Shelton:** USA, left-handed, 23, US Open seed No. 8 / current structured rank No. 9.
- **Carlos Alcaraz:** Spain, right-handed, 23, US Open seed No. 2 / current structured rank No. 3.
- Tournament bracket confirms a men's singles **quarterfinal**, Shelton vs Alcaraz, current status `not_started`.
- H2H before this match: **Alcaraz 3-0**, but only one prior meeting was best-of-five and it was on clay; H2H is continuity context, not a raw streak weight.

## B. Current health / workload / rest

### Alcaraz
- Entered the US Open after roughly a four-and-a-half to five-month competitive layoff caused by a right-wrist issue.
- Official US Open reporting says the wrist/body has responded well and Alcaraz has felt progressively better.
- Through four rounds: **12 sets won, 1 lost; 9h43 on court; 29,696 ft tracked distance**.
- Round of 16: beat Tommy Paul **6-4, 6-3, 6-4** in 2h21.
- Current verified state: no withdrawal or active medical limitation reported.
- Alcaraz chose rest rather than an extra on-site practice day after the Paul match, lowering immediate workload relative to Shelton.

### Shelton
- Through four rounds: **12 sets won, 3 lost; 11h13 on court; 30,830 ft tracked distance**.
- R4 vs Tsitsipas: **6-2, 6-3, 6-4**, 11 aces, 83% first-serve points won, **zero break points faced**.
- Shelton had managed prior-session practice load because of late finishes, then practised after the Tsitsipas match.
- No current verified injury/withdrawal found.
- Pre-US Open hard-court form includes a Montreal title won **without dropping a set across six matches**.

Workload direction:
- Alcaraz has approximately **1h30 less match time** through four rounds.
- Shelton has more accumulated set/game exposure, but recent serve efficiency can shorten points.
- No deterministic fatigue sign is applied; it slightly widens Shelton's late-match tail rather than forcing a negative adjustment.

## C. L5 / L10 / L15 / L20 trend audit

Results are descriptive diagnostics only. Exhibitions are excluded.

### Carlos Alcaraz
- **L5: 5-0**
- **L10: 9-1**
- **L15: 12-3**
- **L20: 17-3**

Current US Open:
- Safiullin W 6-4 6-4 6-4
- Faria W 4-6 6-0 6-3 6-2
- Wu W 6-3 6-4 6-1
- Paul W 6-4 6-3 6-4

### Ben Shelton
- **L5: 4-1**
- **L10: 9-1**
- **L15: 12-3**
- **L20: 16-4**

Current US Open:
- Griekspoor W 1-6 6-1 7-6 6-2
- Hurkacz W 6-3 5-7 7-6 7-5
- Shapovalov W 7-6 6-7 6-3 6-4
- Tsitsipas W 6-2 6-3 6-4

Trend test:
- Both are genuinely strong current players.
- Alcaraz's cleaner set record receives mechanism support from return quality and point dominance, not from the win streak itself.
- Shelton's recent match-length pattern receives mechanism support from elite hold/ace pressure, not from an assumed "always four sets" rule.

## D. Serve / return priors

Specialist 2026 baseline, used with shrinkage:

### Alcaraz
- First serve in: ~67.7%
- First-serve points won: ~73.7%
- Second-serve points won: ~57.0%
- Hold: ~89.4%
- Break: ~31.3%
- Return points won: ~41.9%
- Last-52 hard-court: hold ~90.6%, break ~30.0%

### Shelton
- First serve in: ~67.6%
- First-serve points won: ~76.9%
- Second-serve points won: ~59.5%
- Hold: ~91.7%
- Break: ~11.6%
- Return points won: ~31.5%
- Last-52 hard-court: hold ~89.5%, break ~16.0%
- Against Top-10 opposition in the available sample: hold falls to ~83.8%, break ~10.4%, return points won ~27.4%.

Interpretation:
- Shelton's serve is strong enough to protect many games and create tiebreak/close-set branches.
- Alcaraz's return process is the largest matchup advantage: his broad break rate is roughly two to three times Shelton's.
- This is the main reason **Alcaraz winner** grades much stronger than **Alcaraz -4.5 games**.

## E. H2H continuity

Alcaraz leads **3-0**:
- 2023 Canada hard: 6-3, 7-6 Alcaraz
- 2024 Laver Cup hard: 6-4, 6-4 Alcaraz
- 2025 Roland Garros clay: 7-6, 6-3, 4-6, 6-4 Alcaraz

The 2025 best-of-five meeting totaled **42 games** with Alcaraz winning aggregate games **23-19 (+4)**:
- Alcaraz won the match.
- Shelton +4.5 games would have covered.
- Over 38.5 would have won.

This is descriptive evidence only. Surface and current serve/return regimes differ.

## F. Environment / roof state

Exact Arthur Ashe venue-area forecast around the match:
- approximately **22-23°C**
- mostly clear / partly cloudy
- no meaningful precipitation signal in the immediate window.

Arthur Ashe has a retractable roof, but **official roof state was not independently confirmed at cutoff**. With dry conditions, no signed weather adjustment is applied. The environment is treated as near-neutral hard-court conditions, with roof-state uncertainty retained.

## G. Joint best-of-five match tree

This is a qualitative probability tree, not a fitted model.

### Prior
Start from current surface/class prior:
- Alcaraz superior return and all-court baseline.
- Shelton elite first-strike serve and home-crowd familiarity.
- Alcaraz current wrist return has survived four matches without a verified setback.

Signed probability-mass adjustments to the winner prior:
- Alcaraz base elite-hard / return-class prior: **72%**
- `+5%` current US Open return/control evidence: 12-1 sets and only 9h43 on court
- `+2%` rest/workload advantage
- `-4%` Shelton current serve regime / Montreal + Tsitsipas evidence
- `+1%` H2H technical continuity, heavily shrunk
- `0%` weather / roof centre
= **76% Alcaraz winner**

### Explicit scoreline branch weights

| Branch | Probability |
|---|---:|
| **Alcaraz 3-0** | **30%** |
| **Alcaraz 3-1** | **31%** |
| **Alcaraz 3-2** | **15%** |
| Shelton 3-0 | 4% |
| Shelton 3-1 | 8% |
| Shelton 3-2 | 12% |

Checks:
- Alcaraz winner = **76%**
- Shelton winner = **24%**
- 3 sets = **34%**
- 4 sets = **39%**
- 5 sets = **27%**
- Match reaches 4+ sets = **66%**

Central branch: **Alcaraz 3-1**.

Representative coherent scorelines:
- Alcaraz 6-4, 6-7, 6-3, 6-4 = **42 games**, Alcaraz +6 games
- Alcaraz 6-4, 7-6, 4-6, 6-4 = **43 games**, Alcaraz +3 games
- Alcaraz 7-6, 6-4, 6-7, 6-4 = **42 games**, Alcaraz +4 games

These show why Alcaraz can be the strong winner while Shelton +4.5 and the Over remain live.

## H. Total-games object — 38.5

Current tournament ordinary games-per-set:
- Alcaraz: **118 games / 13 sets = 9.08 games/set**
- Shelton: **153 / 15 = 10.20 games/set**

The difference is driven substantially by Shelton's tiebreak/hold-heavy path.

Set-count mixture:
- 3 sets: 34%
- 4 sets: 39%
- 5 sets: 27%

38.5 mechanism:
- Three-set branches are overwhelmingly Under unless all three sets are extremely extended.
- Four-set branches split around the line; close/tiebreak four-setters frequently go Over.
- Five-set branches are overwhelmingly Over.

After within-set closeness:
- **Over 38.5 = 60%**
- **Under 38.5 = 40%**

## I. Game-handicap object — ±4.5

Aggregate-game handicap is independent of match winner.

Shelton +4.5 covers through:
- every Shelton win except unusually lopsided aggregate-game anomalies,
- many Alcaraz 3-2 wins,
- many close Alcaraz 3-1 wins,
- some tiebreak-heavy Alcaraz 3-0 wins.

Alcaraz -4.5 requires meaningful aggregate separation and loses in many narrow Alcaraz wins.

Final:
- **Shelton +4.5 games = 58%**
- **Alcaraz -4.5 games = 42%**

Kill path for Shelton +4.5:
- Alcaraz's return pressure produces repeated 6-3 / 6-2 sets and a short 3-0 or comfortable 3-1.

Kill path for Alcaraz -4.5:
- Shelton holds at elite rates and steals a tiebreak/set while Alcaraz still wins the match.

## J. Bidirectional-sign / dependence audit

| Mechanism | Helps | Hurts |
|---|---|---|
| Shelton elite serve / tiebreak pressure | Shelton +4.5, Over 38.5, Over 3.5 sets | Alcaraz -4.5 |
| Alcaraz return superiority | Alcaraz winner, Alcaraz -4.5 | Shelton +4.5, Over if it creates a 3-0 |
| Alcaraz wrist return currently stable | Alcaraz winner | Any late physical recurrence widens Shelton and Over branches |
| Shelton greater workload | Alcaraz late-match branches | Strong serving can shorten points and blunt fatigue |
| Four/five-set extension | Over 38.5, Shelton +4.5 | Straight-set Alcaraz branch |
| Dry mild environment | Neutral/serve-friendly continuity | No weather-driven directional edge |

All four ranked rows come from the **same match tree** and are therefore dependent, not four independent edges.

## K. Ranked four

| Rank | Selection | UNVALIDATED_SUBJECTIVE | Evidence |
|---:|---|---:|---|
| **1** | **Carlos Alcaraz match winner** | **76%** | `SUPPORTED / MEDIUM-HIGH` |
| **2** | **Over 3.5 sets** | **66%** | `SUPPORTED / MEDIUM` |
| **3** | **Total Games Over 38.5** | **60%** | `LEAN / MEDIUM` |
| **4** | **Ben Shelton +4.5 Games** | **58%** | `LEAN / MEDIUM` |

## L. Supplied-line audit

| Supplied row | Probability |
|---|---:|
| **Shelton +4.5 games** | **58%** |
| Alcaraz -4.5 games | **42%** |
| **Over 38.5 games** | **60%** |
| Under 38.5 games | **40%** |

## M. Potential winner

**Carlos Alcaraz — 76% UNVALIDATED_SUBJECTIVE match winner.**

This is the same canonical winner endpoint as Rank #1, **not a second observation**.

Most representative score family:
- **Alcaraz 3-1**
- Alcaraz 3-0
- Alcaraz 3-2
- Shelton 3-2 as the main upset tail.

## N. Source register — P-350

### Governing Drive
- Google Drive `METHOD.md` — `MDS-2026.09.06-v4.0`
- Google Drive `RULES_TENNIS.md` — fresh read; `SFA-TENNIS`
- current local mini-running-log continuation

### Official / governing event sources
- US Open 2026 men's quarterfinal breakdown:
  https://www.usopen.org/en_US/news/articles/2026-09-08/2026_us_open_mens_quarterfinals_breakdown.html
- US Open Shelton-Tsitsipas R4 report:
  https://www.usopen.org/en_US/news/articles/2026-09-06/shelton_dominates_tsitsipas_sets_alcaraz_clash_in_2026_us_open_quarterfinals.html
- US Open Alcaraz-Paul R4 report:
  https://www.usopen.org/en_US/news/articles/2026-09-06/carlos_alcaraz_sweeps_past_tommy_paul_to_reach_2026_us_open_quarterfinals.html
- US Open official event schedule:
  https://www.usopen.org/en_US/about/eventschedule.html
- Structured tournament bracket/status feed used for exact `not_started` state and 02:10 UTC start.

### ATP / specialist
- ATP Shelton Montreal title:
  https://www.atptour.com/en/news/shelton-nakashima-montreal-2026-thursday-final
- Tennis Abstract Alcaraz 2026 serve/return profile:
  https://www.tennisabstract.com/cgi-bin/player-classic.cgi?f=A2026qq&p=207989%2FCarlos-Alcaraz
- Tennis Abstract Shelton 2026 serve/return profile:
  https://www.tennisabstract.com/cgi-bin/player-classic.cgi?f=A2026qq&p=210097%2FBen-Shelton
- Roland Garros official 2025 Alcaraz-Shelton match:
  https://www.rolandgarros.com/en-us/article/alcaraz-hangs-tough-to-surpass-shelton
- Reuters current US Open reports for Shelton-Tsitsipas and Alcaraz-Paul.
- Exact Arthur Ashe / Flushing venue weather feed.

### Exclusions
Bookmaker prices, implied probabilities, market movement, consensus picks and tipster/model forecasts were excluded. Exact operator retirement/walkover rules were not provided and remain `UNKNOWN_DEFINITION`.

**P-350 STATUS:** `PREGAME — UNSETTLED`  
**Retrospective:** deferred  
**Next local forecast slot:** **P-351**


### Settlement / retrospective addendum — 2026-09-10

**Current status:** `FINAL / SETTLED`.

**Official final:** Ben Shelton defeated Carlos Alcaraz **6-7(5), 6-1, 6-3, 1-6, 7-6(7)** in **4h28**. Total games = **49**; aggregate games Shelton **26**, Alcaraz **23**. US Open reports Shelton converted **5 break points** to Alcaraz's 3.

| Contract | Issued probability | Result |
|---|---:|---|
| Rank #1 Alcaraz match winner | 76% | **LOSS** |
| Rank #2 Over 3.5 sets | 66% | **WIN** — 5 sets |
| Rank #3 Over 38.5 games | 60% | **WIN** — 49 |
| Rank #4 Shelton +4.5 games | 58% | **WIN** |
| Supplied Alcaraz -4.5 | 42% | **LOSS** |
| Supplied Under 38.5 | 40% | **LOSS** |
| Potential winner: Alcaraz | same Rank #1 | **LOSS — no duplicate observation** |

**Brier:** mean **0.2574** over 4 ranked rows.

**Q1 — actual driver:** the match-length/cushion branch was correctly identified, but Shelton did more than merely hold serve: his return game produced enough break pressure to win the match. US Open's report specifically highlights his serving, returns and angled groundstrokes, and the official numbers show five converted breaks.

**Q2 — knowable?** **Partly.** Shelton's current serving level, Montreal title and difficult US Open draw were known. The card leaned heavily on his broad 2026/Top-10 return weakness when setting only 24% upset mass. His current-tournament return/groundstroke improvement against strong opponents was not developed with comparable granularity.

**Q3 — smallest change:** for Slam match-winner branches, retrieve and compare **current-event return pressure/break creation against opponent quality** alongside all-season/Top-10 baselines. Broad historical return weakness should remain a prior, not silently dominate the live current-tournament regime.

**Deep Rank-#1 review.** Three subordinate rows were right, which means the shared score tree successfully anticipated extension and Shelton's game resistance but assigned too little of that same competitive state to **Shelton actually winning**. The improvement is therefore branch-allocation coherence, not a new “underdog in long match” rule.

**Recommended destination:** `RULES_TENNIS.md` current-regime serve/return section and `LEARNING_REGISTER.md` as an exploratory observation. No promotion from one event.

**Settlement sources:**
- US Open official match report: https://www.usopen.org/en_US/news/articles/2026-09-09/shelton_ends_alcarazs_us_open_title_defense_in_late-night_five-setter.html
- US Open official by-the-numbers: https://www.usopen.org/en_US/news/articles/2026-09-09/by_the_numbers_facts_and_figures_from_the_epic_tuesday_at_the_2026_us_open.html

---


# P-351 — Cincinnati Reds (Nick Lodolo) @ Los Angeles Dodgers (Tarik Skubal) — MLB

**Issued view:** PREGAME  
**Competition:** MLB 2026 regular season — PRIMARY_SCORED  
**Venue:** UNIQLO Field at Dodger Stadium, Los Angeles  
**Official first pitch:** 2026-09-08 19:10 PDT / 2026-09-09 12:10 AEST  
**Final volatile refresh:** 2026-09-08 19:07:59 PDT / 2026-09-09 12:07:59 AEST  
**State:** PRE-GAME; no live play incorporated  
**Method:** MDS-2026.09.06-v4.0 / SFA-BASEBALL  
**Mode:** SPORTS_ONLY / MARKET_BLIND  
**Probability tier:** UNVALIDATED_SUBJECTIVE  
**Operator action/listed-pitcher/shortening terms:** UNKNOWN_DEFINITION  
**Retrospective:** DEFERRED BY USER

## Identity / participants
Official MLB probable pitchers: Nick Lodolo LHP (3-3, 5.08 ERA, 69 SO) vs Tarik Skubal LHP (8-7, 2.86 ERA, 159 SO). MLB official starting-lineup page remained TBD at cutoff, so current batting orders are SECONDARY_ONLY and player props are not promoted.

Current late secondary lineups:
CIN — Dane Myers; Elly De La Cruz; Sal Stewart; Tyler Stephenson; Eugenio Suárez; JJ Bleday; Matt McLain/Juan Brito middle-infield branch; Héctor Rodríguez, with exact bottom-order configuration source-dependent.
LAD — Tommy Edman; Mookie Betts; Will Smith; Freddie Freeman; Teoscar Hernández; Miguel Rojas; Alex Call; Max Muncy; Kiké Hernández.

Shohei Ohtani is not starting; current team reporting says he remains available for key in-game moments. Kyle Tucker is also absent from the latest posted Dodgers lineup; no injury reason is assigned without verified evidence.

## Availability
CIN: Ke'Bryan Hayes activated Sep 7 after groin IL; Graham Ashcraft activated Sep 6; Hunter Greene remains out after UCL surgery; Michael Toglia on 60-day IL.
LAD: Ohtani managed for knee/biceps/neck issues and not starting tonight; Dalton Rushing on 10-day IL (right elbow); Edwin Díaz on rehab assignment for neck inflammation and not part of the normal major-league relief chain tonight.

## Trend audit
CIN: L5 3-2; L10 6-4; recent offense has produced 60 runs over the last 10 in the current StatMuse snapshot, but tonight's Skubal matchup receives far greater weight than the streak.
LAD: L5 5-0; official pre-opener L10 6-4 and current 15-game snapshot 9-6; current 20-game Baseball-Reference snapshot 12-8. Streak direction itself receives zero weight; mechanisms are pitching, lineup, contact/HR profile and bullpen/park context.
H2H: LAD won the Sep 7 opener 6-3. Result itself has no directional weight; only bullpen use/lineup consequences carry forward.

## Starters
### Tarik Skubal
2026: 22 GS, 132.1 IP, 2.86 ERA, 0.98 WHIP, 159 K, 22 BB, 12 HR; ~2.48 FIP, 30.5% K, 4.2% BB. Recent six-start run has remained stable around 5-7 IP and mostly 1-3 ER. Sep 3 vs STL: 5.2 IP, 10 H, 2 ER, 1 BB, 6 K. Starting on four days' rest as part of the Dodgers' rotation alignment; no automatic fatigue penalty.

### Nick Lodolo
2026: 17 GS, 85 IP, 5.08 ERA, 1.52 WHIP, 69 K, 35 BB, 16 HR; ~5.57 FIP, 1.69 HR/9. Activated from IL Aug 11. Five starts since return: 22.1 IP, 16 ER (~6.45 ERA), 7 HR, but latest start was 6 IP / 2 ER vs SD. Current regime therefore remains wide: good-start branch retained, but HR/walk/early-hook tail remains materially larger than Skubal's.

## Prior-game / bullpen
Sep 7 LAD won 6-3. Emmet Sheehan went 5.2 IP; Evan Phillips worked a clean ninth. Cincinnati's planned Burns/Williamson structure absorbed most innings. Neither bullpen is treated as exhausted. Dodgers retain normal leverage depth except Edwin Díaz is unavailable from the active MLB chain; Reds closer Emilio Pagán had worked Sep5-6 but had Sep7 off and is likely available.

## Environment
Exact Dodger Stadium feed near first pitch: ~89°F / 32°C, mostly clear/clearing, falling toward 29°C by 8 PM. Current field report: ~86°F, clear, wind ~7 mph out to RF. No rain threat. Heat plus light outflow modestly expands carry/HR tail, especially against Lodolo's current HR profile; it is not treated as an automatic Over.

## Joint run object
Season scoring priors:
- CIN ~4.22 runs/game
- LAD ~4.94 runs/game
Raw sum = **9.16**

CIN component:
4.22
-1.10 Skubal elite run-prevention/FIP branch
-0.20 Skubal K-BB/expected-length advantage
+0.10 current CIN power route
+0.10 warm/wind-out environment
= **3.12**

LAD component:
4.94
+0.35 Lodolo ERA/FIP/HR/short-hook branch
+0.15 right-heavy LAD matchup route vs LHP
-0.40 Ohtani absent from starting lineup
+0.20 heat/light wind-out carry
= **5.24**

Joint centre = **8.36 runs**
Working width = **±4.0 runs**, retaining sequencing, multi-HR, early-hook, inherited-runner, home-ninth and extra-inning tails.

Separation = 5.24 - 3.12 = **LAD +2.12 runs**.

## Supplied lines
- Dodgers -1.5: **59%**
- Reds +1.5: **41%**
- Over 8.0: **49% win / 10% push**
- Under 8.0: **41% win / 10% push**

## Ranked four
1. **Reds team total Under 4.5 runs — 74% UNVALIDATED_SUBJECTIVE — SUPPORTED / MEDIUM-HIGH**
2. **Los Angeles Dodgers match winner — 72% — SUPPORTED / MEDIUM-HIGH**
3. **Dodgers team total Over 3.5 runs — 70% — SUPPORTED / MEDIUM**
4. **Dodgers -1.5 — 59% — LEAN / MEDIUM**

Potential winner: **Los Angeles Dodgers — 72%**.
Central score family: LAD 5-3, LAD 5-2, LAD 4-2; opposing branch CIN 4-3.

## Source register
Drive: METHOD.md; RULES_BASEBALL.md; current local running log.
Official/current: MLB Dodgers/Reds probable pitchers; MLB starting-lineup pages (TBD at cutoff); MLB transaction/injury pages; Baseball Savant/StatMuse starter metrics; Baseball-Reference current matchup/trend snapshot; True Blue LA current Ohtani and rotation reports; Dodgers Nation late lineup; Reuters Sep7 series-opener recap and Ohtani health report; current Reds game-day thread linked to MLB Gameday; exact Dodger Stadium hourly weather feed.
Excluded: bookmaker odds, implied probabilities, line movement, consensus and tipster/model forecasts.

**P-351 STATUS:** PREGAME — UNSETTLED  
**Retrospective:** deferred  
**Next local forecast slot:** **P-352**


### Settlement / retrospective addendum — 2026-09-10

**Current status:** `FINAL / SETTLED`.

**Official final:** Los Angeles Dodgers **3–2** Cincinnati Reds. Will Smith homered in the first; Elly De La Cruz tied it 2–2 with a two-run homer; Teoscar Hernández supplied the go-ahead RBI in the fifth.

| Contract | Issued probability | Result |
|---|---:|---|
| Rank #1 Reds TT Under 4.5 | 74% | **WIN** — Reds 2 |
| Rank #2 Dodgers winner | 72% | **WIN** |
| Rank #3 Dodgers TT Over 3.5 | 70% | **LOSS** — Dodgers 3 |
| Rank #4 Dodgers -1.5 | 59% | **LOSS** — won by 1 |
| Supplied Reds +1.5 | 41% | **WIN** |
| Supplied Over 8.0 | 49% win / 10% push | **LOSS** — total 5 |
| Supplied Under 8.0 | 41% win / 10% push | **WIN** |
| Potential winner: Dodgers | 72% | **WIN** |

**Brier:** mean **0.2460** over 4 ranked rows.

**Q1 — actual driver:** the expected pitching asymmetry was sufficient for a Dodgers win and Reds suppression, but not for a four-run Dodgers team total or two-run separation. Los Angeles' Ohtani-less starting lineup never generated the projected 5.24-run central component.

**Q2 — knowable?** **Yes.** The card explicitly knew Ohtani was not starting and applied `-0.40`, yet still left a 5.24 Dodgers centre and 70% Over 3.5. The missing elite bat was treated as one scalar rather than as a change to PA allocation, HR/cluster probability and late-game separation.

**Q3 — smallest change:** when a decision-driving elite hitter is absent, rebuild the **lineup PA/cluster state** and re-query team total and run line from it; do not rely on a single additive run subtraction.

**Deep review.** Rank #1 and winner were sound; Rank #3/#4 failed together because both depended on the same Dodgers multi-run-scoring branch. This is a dependence/coherence failure already addressed by `BB-S1`, `G-L1` and the single joint-run-object rule.

**Recommended destination:** `RULES_BASEBALL.md` lineup exposure / team-total derivation; `LEARNING_REGISTER.md` as reinforcement, not a new rule.

**Settlement source:** MLB official game story: https://www.mlb.com/stories/game/823901/

---


# P-352 — Namibia vs South Africa — 1st ODI

**Issued state:** PRESTART / TOSS COMPLETE  
**Venue:** FNB Namibia Cricket Ground, Windhoek  
**Toss:** Namibia won the toss and elected to field  
**First innings:** South Africa batting first  
**Final volatile refresh:** 2026-09-09 17:34:10 AEST / 09:34:10 local  
**No live ball/score incorporated at freeze**  
**Method:** MDS-2026.09.06-v4.0 / SFA-CRICKET  
**Population:** EXPLORATORY — NOT PRIMARY_SCORED  
**Mode:** SPORTS_ONLY / MARKET_BLIND  
**Probability tier:** UNVALIDATED_SUBJECTIVE  
**Operator action/DLS/shortening terms:** UNKNOWN_DEFINITION  
**Retrospective:** DEFERRED BY USER

## Confirmed XIs
Namibia: Malan Kruger, Louren Steenkamp, Alexander Volschenk, Jan Frylinck, Gerhard Erasmus (c), Zane Green (wk), Jan Balt, Ruben Trumpelmann, Jack Brassell, Max Heingo, Bernard Scholtz.

South Africa: Jordan Hermann, Connor Esterhuizen, Tony de Zorzi, Dewald Brevis, Rubin Hermann (wk), Jason Smith, Corbin Bosch, Duan Jansen, Bjorn Fortuin (c), Prenelan Subrayen, Kwena Maphaka.

Availability:
- South Africa: Lhuan-dre Pretorius out; Andile Simelane out. Matthew Breetzke and Corbin Bosch were called as replacements; Breetzke is not in the XI, Bosch is.
- South Africa's senior Australia-bound core is largely absent: Bavuma, de Kock, Rickelton, Markram, Stubbs, Miller, Marco Jansen, Maharaj, Ngidi.
- Namibia: Michael van Lingen was expected unavailable and is not in the XI.

## Exact-match strip / conditions
STRIP STATUS: OBSERVED.
Pitch No. 5 from the eastern side. Straight boundaries ~65m; east ~75m; west ~68m. Visible grass covering, no cracks, consistent bounce expected for seamers, little turn expected, moisture around the facility after watering. Broadcast assessment expected plenty of runs once batters are in, but a new-ball advantage for the side bowling first.

MATCH CONDITIONS STATUS: OBSERVED.
Weather around 09:30-15:00 local: hazy/cloudy, ~17C rising toward 27-28C, negligible rain threat.

Conditions ladder:
1. Exact toss/broadcast commentary — FOUND: exact-match pitch report and toss.
2. Venue/curator query — ATTEMPTED: Cricket Namibia curator profile found; historical/context only.
3. Specialist exact-match preview — FOUND: Cricbuzz exact ODI preview; five prior men's ODIs at this ground in April, highest totals 268/7 and 274/7.
4. ICC pitch-rating lane — ATTEMPTED: ICC rating framework/current files found; no match-specific pregame strip rating applicable.
5. Independent current conditions reporting — FOUND: current weather/conditions reporting broadly agrees on dry conditions; no independent strip observation given decisive weight over the broadcast.
6. Venue-format baseline — COMPUTED WITH SMALL-SAMPLE WARNING: only five prior men's ODIs cited by exact-match specialist preview; do not mix T20 scoring into the ODI baseline.

## Current form / continuity
Namibia's recent ODI record includes wins over Netherlands and Nepal, plus a 297/5 List A innings against Vidarbha. South Africa's exact XI has little current ODI continuity together, but its T20I tour form at the same venue showed high power ceiling: 228/4 vs Namibia and 205/5 vs Zimbabwe in the final. T20 scoring is not transferred directly into ODI rates.

Direct ODI H2H: first ever ODI between the sides.

## Phase object — South Africa first 5 overs
Starting qualitative neutral full-member/associate ODI phase prior: **27 runs**
-3.0 exact-match moisture + grass/new-ball seam branch
+0.5 Jordan Hermann/Esterhuizen positive intent and short straight boundaries
= **24.5-run centre**

Width: ~±10 runs, driven by boundary clusters and early wickets.

Supplied 25.5:
- Under 25.5: **58%**
- Over 25.5: **42%**

## South Africa first-innings object
Starting qualitative South Africa second-string-vs-associate ODI prior: **285**
-8 exact-match new-ball/grass/moisture + Namibia choosing to field
-7 missing elite senior SA batting core / inexperienced ODI XI
+6 current batting-depth/power ceiling through de Zorzi, Brevis, Smith, Bosch, Jansen
+2 consistent bounce + short straight boundary access after settling
= **278-run centre**

Width: ~±48 runs.

Phase-resource link:
- 5-over central state ~24-27 with 0-1 wicket still leaves 275-300 available through middle/death acceleration.
- 2+ early wickets shifts the innings strongly toward 230-270.
- wicket-light first 15 overs plus Brevis/de Zorzi/Bosch late resources creates the 305+ branch.

Supplied 305.5:
- Under 305.5: **68%**
- Over 305.5: **32%**

Additional threshold:
- South Africa 250+ first innings / Over 249.5 equivalent: **66%**

## Winner object
South Africa remain the stronger side by batting depth and bowling pace/variety, but this is a developmental XI and Namibia have home familiarity plus a recent T20 win over them. Toss gives Namibia the preferred chase/conditions sequence.

South Africa winner: **67%**
Namibia winner: **33%**

## Ranked four
1. **South Africa 1st innings Under 305.5 — 68% UNVALIDATED_SUBJECTIVE — SUPPORTED / MEDIUM**
2. **South Africa match winner — 67% — SUPPORTED / MEDIUM**
3. **South Africa 1st innings 250+ runs / Over 249.5 — 66% — LEAN / MEDIUM**
4. **South Africa first 5 overs Under 25.5 — 58% — LEAN / MEDIUM-LOW**

Central first-innings score family: **268-292**, midpoint ~278.
Potential winner: **South Africa 67%**.

## Source register
Drive: METHOD.md; RULES_CRICKET.md; DATA_SOURCE_REGISTER.md §6A; current local running log.
Current external:
- Cricbuzz exact match commentary/score centre: toss, XIs, exact-match pitch report, preview and venue ODI context.
- Cricket South Africa official tour release: schedule and squad/captain context.
- Cricket Namibia official venue/ticketing and curator material: venue/date and curator context.
- ICC current tri-series reporting: recent South Africa/Namibia form context.
- Cricket.com.au current series page: fixture cross-check.
- Exact Namibia Cricket Ground structured weather feed.
- Cricbuzz/NDTV current player/team match records for recent ODI/T20 context.
Excluded: fantasy/tipster predictions, bookmaker odds, implied probabilities, market movement and consensus.

**P-352 STATUS:** PRESTART / TOSS COMPLETE — UNSETTLED  
**Retrospective:** deferred  
**Next local forecast slot:** P-353


### Settlement / retrospective addendum — 2026-09-10

**Current status:** `FINAL / SETTLED`.

**Verified final:** South Africa made **348/6 in 50 overs**. Namibia reached **162/8 in 31 overs**; South Africa won by **99 runs (DLS)**. Jordan Hermann scored **150**, Tony de Zorzi 72 and Corbin Bosch 39*. The exact first-five-over state was **South Africa 18/0**.

| Contract | Issued probability | Result |
|---|---:|---|
| Rank #1 SA 1st innings Under 305.5 | 68% | **LOSS** — 348 |
| Rank #2 South Africa winner | 67% | **WIN** |
| Rank #3 SA 250+ / Over 249.5 | 66% | **WIN** |
| Rank #4 First 5 overs Under 25.5 | 58% | **WIN** — 18/0 |
| Supplied 1st innings Over 305.5 | 32% | **WIN** |
| Supplied first-5 Over 25.5 | 42% | **LOSS** |
| Potential winner: South Africa | 67% | **WIN** |

**Brier:** mean **0.2158** over 4 ranked rows.

**Q1 — actual driver:** the new-ball phase was slow exactly as projected, but **wicket preservation** mattered more than the run rate. At 18/0 after five, South Africa retained full batting resources; Hermann/de Zorzi then built the innings before the lower order accelerated to 348.

**Q2 — knowable?** **Yes.** The exact-match pitch report in the issued card explicitly said new-ball help but **consistent bounce/plenty of runs once batters were in**, and the card itself described a wicket-light first 15 overs as the route to 305+. The Rank #1 Under did not allocate enough mass to that branch.

**Q3 — smallest change:** enforce `RULES_CRICKET`'s existing phase-to-innings control by conditioning the full-innings distribution on **runs + wickets/resources**, not phase runs alone. A slow 18/0 is fundamentally different from 18/2 or 18/3.

**Deep Rank-#1 review.** The first-five Under and South Africa winner both won, showing the phase and class read were not wholly wrong. The failure was translating a low early run rate into too much full-innings downside despite preserved wickets and an explicitly identified middle/death ceiling.

**Recommended destination:** `RULES_CRICKET.md` control 16 / phase-resource transition; `LEARNING_REGISTER.md` as confirmation of an existing rule. No new control needed.

**Settlement sources:**
- Result/scorecard: https://sports.ndtv.com/cricket/results/odi-match
- Detailed scorecard: https://www.mykhel.com/cricket/namibia-vs-south-africa-2026-1st-odi-scorecard-m273847/
- First-five commentary: https://www.cricketworld.com/cricket/namibia-vs-south-africa/match/commentary/98359

---


# P-353 — Chunichi Dragons @ Yomiuri Giants — NPB Central League

**Issued view:** PREGAME  
**Venue:** Tokyo Dome, Tokyo  
**Official first pitch:** 2026-09-09 18:00 JST / 19:00 AEST  
**Final volatile refresh:** 2026-09-09 17:47:48 JST / 18:47:48 AEST  
**State:** PREGAME; posted lineups available; no live play incorporated  
**Method:** `MDS-2026.09.06-v4.0` / `SFA-BASEBALL`  
**Population:** `EXPLORATORY — NOT PRIMARY_SCORED`  
**Mode:** `SPORTS_ONLY / MARKET_BLIND`  
**Probability tier:** `UNVALIDATED_SUBJECTIVE`  
**Operator action/listed-pitcher terms:** `UNKNOWN_DEFINITION`  
**Retrospective:** DEFERRED BY USER

## Identity / NPB rules

Official NPB schedule: Chunichi Dragons at Yomiuri Giants, Tokyo Dome, 18:00 JST.  
Official announced starters:
- **Yomiuri — Bryan Mata, RHP**
- **Chunichi — Yudai Ohno, LHP**

2026 Central League rule state:
- scheduled nine innings
- **no DH in the Central League in 2026; pitcher bats**
- regular-season games may continue through 12 innings and can finish tied
- no automatic runner
- Yomiuri owns home-last-bat entitlement.

For the user-supplied `Giants -0.5 / Dragons +0.5`, under the research-grade standard final-score interpretation:
- Giants -0.5 wins only if Yomiuri wins.
- Dragons +0.5 wins if Chunichi wins **or the official game finishes tied**.
Exact operator action/void language was not supplied.

## Posted starting lineups

### Yomiuri Giants
1. Shunsuke Urata — 2B — L
2. Trey Cabbage — CF — L
3. Bobby Dalbec — 1B — R
4. Takumi Ohshiro — C — L
5. Yoshihiro Maru — LF — L
6. Yuta Izuguchi — SS — L
7. Go Matsumoto — RF — R
8. Yusei Ishizuka — 3B — R
9. Bryan Mata — P — R

### Chunichi Dragons
1. Hiroki Fukunaga — 2B — R
2. Kaito Muramatsu — SS — L
3. Shuhei Takahashi — 3B — L
4. Miguel Sano — 1B — R
5. Seiji Uebayashi — RF — L
6. Seiya Hosokawa — LF — R
7. Yuki Okabayashi — CF — L
8. Yuta Ishii — C — R
9. Yudai Ohno — P — L

Lineup implication: **five of Yomiuri's first six hitters bat left-handed against left-hander Ohno**, materially strengthening Ohno's matchup branch. Chunichi's lineup is more balanced against right-hander Mata.

Managers:
- Yomiuri — Shinnosuke Abe
- Chunichi — Kazuki Inoue

## Availability / roster movement / bench

Yomiuri registered **Bryan Mata** to the first-team roster on Sep 9 and deregistered outfielder **Julian Tima**. No Chunichi Sep-9 first-team registration change was found in the current notice.

Current Yomiuri bench includes Kai, Kobayashi, Kadowaki, Sakamoto, Masuda, Nakayama, Sasaki and Suzuki. Current relief options include Daiki, Norimoto, Eito Tanaka, Morita, Funabasama, Izumi, Heinai, Hotta and **Raidel Martinez**.

Current Chunichi bench includes Kinoshita, Kato, Mikiya Tanaka, Ishikawa, Abe, Higuchi, Vosler, Fukumoto and Hanada. Current relief options include Hashimoto, Kusaka, Abreu, Sugiura, Yoshida, Saito, H. Mori and **Shinya Matsuyama**.

Series-opener workload:
- Chunichi used Yanagi for 7 scoreless, then **Seiya Yoshida and Shinya Matsuyama**; Matsuyama recorded the save.
- Yomiuri used Togo plus **Yuhi Nishidate** only.
- Yomiuri closer Raidel Martinez was not required.
Thus both bullpens are broadly available, but Chunichi's closer carries a modest back-to-back workload branch.

## Season team baselines

Official Central League team batting through Sep 8:
- Yomiuri: **426 runs / 125 games = 3.41 runs/game**, .235 AVG, .295 OBP, .349 SLG, 91 HR.
- Chunichi: **422 / 127 = 3.32 runs/game**, .229 AVG, .301 OBP, .352 SLG, 108 HR.

Official team pitching:
- Yomiuri: **393 runs allowed / 125 = 3.14/game**, team ERA **2.87**.
- Chunichi: **429 / 127 = 3.38/game**, team ERA **3.22**.

## L5 / L10 / L15 / L20 audit

Reconstructed from official/current schedules; streak itself receives no directional weight.

| Window | Yomiuri | Chunichi |
|---|---|---|
| L5 | **3-2**, 18 RS / 11 RA | **3-1-1**, 19 / 14 |
| L10 | **5-5**, 34 / 27 | **3-6-1**, 28 / 32 |
| L15 | **9-6**, 56 / 39 | **8-6-1**, 47 / 40 |
| L20 | **11-9**, 78 / 58 | **9-10-1**, 64 / 70 |

Trend mechanism:
- Yomiuri's recent run prevention is strong and supported by overall 2.87 team ERA.
- Chunichi's L5 offense has improved, but that is not treated as momentum.
- Both recent paths remain compatible with a low-to-moderate run environment.

## H2H continuity

2026 series through Sep 8:
- Yomiuri **11-10**
- Yomiuri scored **65**
- Chunichi scored **60**
- Combined **125 runs / 21 games = 5.95 runs/game**

Recent H2H contains extreme tails (11-0 Yomiuri, 11-2 Chunichi) as well as the Sep-8 3-0 Chunichi win. The prior result itself carries zero directional weight.

Ohno's current direct split is much more relevant than generic H2H:
- **0.49 ERA in five 2026 starts vs Yomiuri, 3-1**

This is shrunk rather than treated as ownership.

## Starter object

### Yudai Ohno
Official 2026:
- **19 starts**
- **9-5**
- **125.2 IP**
- **2.08 ERA**
- 92 H
- 12 HR
- 34 BB
- 84 K
- 2 complete games

Recent starts:
- Sep 1 vs Hiroshima: 6.2 IP, 2 R
- Aug 25 vs Hanshin: 7 IP, 1 R
- Aug 18 vs Hiroshima: 5 IP, 2 R
- Aug 11 vs DeNA: 6 IP, 2 R

Key advantage: established innings/run suppression plus the left-heavy Yomiuri order.

### Bryan Mata
Official 2026:
- **6 starts**
- **2-1**
- **31.0 IP**
- **2.90 ERA**
- 21 H
- **0 HR**
- **20 BB + 5 HBP**
- 33 K
- 10 ER

Recent first-team:
- Aug 27 vs Yakult: **6.2 IP, 3 H, 6 K, 1 R**, 116 pitches
- Aug 20 vs DeNA: **5 IP, 5 H, 7 K, 3 R**
Farm tune Sep 3: 2 IP, 25 pitches, 0 H, 0 R.

Small-sample control:
Mata's ERA/K/contact branch is genuinely positive, but **20 walks in 31 innings** plus only six starts means his ordinary/early-hook/inherited-runner tail remains wide. His zero-HR record is not assumed to be a durable zero-HR skill.

## Park / environment

Tokyo Dome is an indoor controlled venue; outdoor rain/wind is **not** used as a game-condition input.

Current 2026 Tokyo Dome park factors:
- HR factor ~**1.29**
- run factor ~**0.94** within the Central League / ~**0.97** all games.

Interpretation: the venue preserves a meaningful home-run cluster tail but has **not** produced an overall high-run environment in 2026. No weather-termination branch is applied.

## Joint run object

### Raw team-score prior
Yomiuri:
`(Yomiuri offense 3.41 + Chunichi runs allowed 3.38) / 2 = 3.40`

Chunichi:
`(Chunichi offense 3.32 + Yomiuri runs allowed 3.14) / 2 = 3.23`

Raw total:
`3.40 + 3.23 = 6.63`

### Yomiuri adjustments
`3.40`
- `0.55` Ohno established starter/run-prevention branch
- `0.20` five-left-handers-in-top-six matchup concentration
+ `0.08` Matsuyama back-to-back availability uncertainty
+ `0.02` Tokyo Dome HR-tail allowance after net run-factor suppression

= **2.75 Yomiuri runs**

### Chunichi adjustments
`3.23`
+ `0.20` Mata walk/HBP/early-hook uncertainty
- `0.10` Mata strikeout/contact-suppression good-start branch
- `0.07` fresh Yomiuri relief/leverage depth
+ `0.02` Tokyo Dome HR-tail allowance

= **3.28 Chunichi runs**

### Joint centre
**6.03 runs**

Working width: approximately **±3.0 runs**, retaining:
- Mata walk/traffic cluster
- Tokyo Dome multi-HR inning
- Ohno regression / sequencing
- Matsuyama back-to-back relief branch
- home-last-bat
- tie-after-nine and 10th-12th inning scoring without an automatic runner.

Separation:
`Chunichi 3.28 - Yomiuri 2.75 = Chunichi +0.53 runs`

## Supplied market probabilities

- **Dragons +0.5: 58%**
- Giants -0.5: **42%**
- **Under 6.5: 62%**
- Over 6.5: **38%**

The +0.5 split includes the live NPB tie state; the total 6.5 has no push.

## Additional team-total contracts

- **Chunichi team total Under 4.5: 75%**
  - centre 3.28
  - Mata's walk tail is the main kill path.
- **Yomiuri team total Under 3.5: 69%**
  - centre 2.75
  - Ohno/platoon/lineup geometry supports it; Tokyo Dome HR clustering is the main kill path.

## Final ranked four

| Rank | Selection | UNVALIDATED_SUBJECTIVE | Evidence |
|---:|---|---:|---|
| **1** | **Chunichi Dragons team total Under 4.5** | **75%** | `SUPPORTED / MEDIUM-HIGH` |
| **2** | **Yomiuri Giants team total Under 3.5** | **69%** | `SUPPORTED / MEDIUM` |
| **3** | **Combined Total Under 6.5** | **62%** | `SUPPORTED / MEDIUM` |
| **4** | **Chunichi Dragons +0.5** | **58%** | `LEAN / MEDIUM` |

## Potential winner

Three-way NPB final-state view:
- **Chunichi Dragons win: 51%**
- Yomiuri Giants win: **42%**
- Official tie after 12: **7%**

**Potential winner: Chunichi Dragons.**

Central score family:
- Chunichi 3-2
- Chunichi 3-1
- 2-2 tie branch
- Yomiuri 3-2 opposing branch.

## Source register

### Governing Drive
- `METHOD.md` — MDS-2026.09.06-v4.0
- `RULES_BASEBALL.md` — SFA-BASEBALL and 2026 NPB rules
- current local running log.

### Official / primary
- NPB Sep 9 schedule and announced starters.
- NPB 2026 Central League standings.
- NPB 2026 Central League team batting.
- NPB 2026 Central League team pitching.
- NPB Bryan Mata player record.
- NPB Yudai Ohno player record.
- NPB Sep 9 roster registration notice.
- NPB 2026 team/manager rosters.
- NPB official Sep 8 Giants-Dragons game record.

### Current secondary / specialist
- SportsNavi exact Sep 9 game page: current posted lineups, bench, starter recent starts, Ohno-vs-Yomiuri split, H2H.
- Baseball Chronicle 2026 Tokyo Dome park factors.
- Current Japanese registration reporting used only as corroboration.

### Exclusions
Bookmaker odds, implied probabilities, line movement, market consensus, tipster picks and synthetic predictions were excluded.

**P-353 STATUS:** PREGAME — UNSETTLED  
**Retrospective:** deferred  
**Next local forecast slot:** **P-354**


### Settlement / retrospective addendum — 2026-09-10

**Current status:** `FINAL / SETTLED`.

**Official NPB final:** Yomiuri Giants **5–1** Chunichi Dragons. Bobby Dalbec homered off Yudai Ohno in the third. Ohno allowed 2 ER in 5.0 IP; Bryan Mata threw 3.0 scoreless innings and Yomiuri's bullpen completed the game.

| Contract | Issued probability | Result |
|---|---:|---|
| Rank #1 Chunichi TT Under 4.5 | 75% | **WIN** — 1 |
| Rank #2 Yomiuri TT Under 3.5 | 69% | **LOSS** — 5 |
| Rank #3 Under 6.5 | 62% | **WIN** — total 6 |
| Rank #4 Chunichi +0.5 | 58% | **LOSS** |
| Supplied Giants -0.5 | 42% | **WIN** |
| Supplied Over 6.5 | 38% | **LOSS** |
| Potential winner: Chunichi | 51% | **LOSS** |

**Brier:** mean **0.2549** over 4 ranked rows.

**Q1 — actual driver:** Yomiuri scored enough through a concentrated group of productive plate appearances — Dalbec, Ohshiro and Maru — while its pitching chain held Chunichi to one.

**Q2 — knowable?** **Yes in structure.** The card gave a `-0.20` Yomiuri adjustment because five of the first six hitters were left-handed against LHP Ohno. That raw hitter-count view underweighted the high-leverage right-handed Dalbec PA and did not sufficiently weight lineup slot/power/expected PA.

**Q3 — smallest change:** make platoon adjustment **PA- and role-weighted** (slot, expected PA, power/contact value, pinch-hit/substitution paths), not a count of same-handed hitters.

**Deep review.** The total centre was close — 6.03 vs actual 6 — yet the allocation between teams was wrong enough to lose Yomiuri Under 3.5 and Chunichi +0.5. This is a team-component/separation issue, not a total-process failure.

**Recommended destination:** `RULES_BASEBALL.md` `BB-S1/BB-S3` lineup/platoon exposure. Record as observation; do not create a universal handedness coefficient.

**Settlement source:** NPB official English BIS: https://npb.jp/bis/eng/2026/games/s2026090901424.html

---


# P-354 — Hiroshima Carp @ Hanshin Tigers — NPB Central League

**Issued view:** `PREGAME / START-DELAY ANNOUNCED`  
**Venue:** Hanshin Koshien Stadium, Nishinomiya  
**Scheduled first pitch:** 2026-09-09 18:00 JST / 19:00 AEST  
**Final volatile refresh:** 2026-09-09 17:58:31 JST / 18:58:31 AEST  
**State at cutoff:** SportsNavi displayed `開始遅延 / 降雨のため`; posted lineups were available; **no pitch or live score was incorporated**  
**Method:** `MDS-2026.09.06-v4.0 / SFA-BASEBALL`  
**Population:** `EXPLORATORY — NOT PRIMARY_SCORED`  
**Mode:** `SPORTS_ONLY / MARKET_BLIND`  
**Probability tier:** `UNVALIDATED_SUBJECTIVE`  
**Operator rain/suspension/action/listed-pitcher terms:** `UNKNOWN_DEFINITION`  
**Retrospective:** DEFERRED BY USER

## NPB contract/rules state
- 2026 Central League; no DH, both pitchers bat.
- Scheduled nine innings; regular-season tie remains possible after 12 innings; no automatic runner.
- Hanshin bats last.
- User slate: Hanshin -1.5; Hiroshima +1.5; O/U 5.5.
- Research probabilities below refer to the official-game final-state event if the game proceeds. Operator void/suspension treatment is unknown.

## Posted lineups
Hanshin:
1 Chikamoto CF L; 2 Nakano 2B L; 3 Morishita RF R; 4 Teruaki Sato 3B L; 5 Oyama 1B R; 6 Maegawa LF L; 7 Fushimi C R; 8 Motoyama SS L; 9 Haruto Takahashi P L.

Hiroshima:
1 Omori CF L; 2 Kikuchi 2B R; 3 Shosei Nakamura LF R; 4 Sakakura 3B L; 5 Tai Sasaki RF R; 6 Keisuke Sato 1B L; 7 Mochimaru C L; 8 Katsuda SS L; 9 Hiroki Tokoda P L.

Availability note: Kaito Kozono remains outside the first-team lineup after his Aug-18 demotion for re-adjustment; this is not labelled an injury. Hiroshima's lower third is weak by current batting average and the pitcher bats ninth.

## Starting pitchers
### Haruto Takahashi
2026 official: 19 G/GS, **13-2, 1.90 ERA, 132.2 IP, 101 H, 8 HR, 16 BB, 123 K**, five complete games/four shutouts.
Current matchup page: 1-0, 3.00 ERA in two 2026 starts vs Hiroshima.
Recent: Sep1 6.1 IP/2 R; Aug23 5 IP/1 R; Aug12 6 IP/1 R; Aug5 4 IP/6 R.
Mechanism: elite K-BB/control and length; one poor-start tail remains.

### Hiroki Tokoda
2026 official: 19 GS, **6-4, 2.86 ERA, 116.1 IP, 119 H, 11 HR, 31 BB, 73 K**.
Current matchup page: 0-2, 3.00 ERA in three starts vs Hanshin.
Recent: Sep1 8 IP/1 R; Aug25 5 IP/6 R; Aug18 5 IP/3 R; Jul31 7 IP/1 R.
Tokoda was moved one day by the Sep8 rainout; routine disruption is modest, not a fatigue penalty.

## Season baselines
Hanshin offense: 453 runs / 122 = **3.71/game**; .247/.317/.372, 110 HR.
Hiroshima offense: 360 / 120 = **3.00/game**; .225/.289/.324, 77 HR.
Hanshin pitching: 381 RA / 122 = **3.12/game**, team ERA 2.86.
Hiroshima pitching: 443 / 120 = **3.69/game**, team ERA 3.42.

## L5/L10/L15/L20 diagnostic
Hanshin:
- L5 2-3, 19 RS/18 RA
- L10 6-4, 34/28
- L15 9-6, 48/41
- L20 12-8, 65/57

Hiroshima:
- L5 1-4, 15/24
- L10 3-7, 28/44
- L15 6-9, 42/62
- L20 10-10, 65/78

No momentum weight is assigned; current starter/lineup/park/bullpen mechanisms own the forecast.

## H2H
2026: Hanshin 9-8-1, 59 runs; Hiroshima 8-9-1, 48 runs. Combined 107 runs / 18 = **5.94/game**.
H2H is descriptive only; direct current starter and lineup evidence receives priority.

## Bullpen / rest
Sep8 was rained out and Sep7 was an off-day, so Hanshin's relief group is highly available. Current bench includes Iwazaki, Oyokawa, Kudo, Kinoshita, Okadome, Ishii, Jingu, Severino and Dolis.
Hiroshima's current relief list includes Moriura, Taka, Yasuki Kudo, Horie, Kenta Suzuki, Tarnok and Endo. Manager Arai explicitly moved Kenta Suzuki to relief after the rainout because the bullpen had been carrying cumulative burden. Freshness is kept distinct from quality.

## Koshien / weather
2026 Koshien park factors:
- HR PF **0.61** (Central League)
- run PF **0.73**
This is a major run-suppression mechanism, but not a guarantee.

Exact venue weather at the final research window:
- current ~22C/cloudy
- high precipitation risk through the opening window
- JMA gale/thunderstorm advisories in force around the scheduled start.
Current game page explicitly says start delayed due to rain.

Rain is modelled as an **event-order/variance branch**, not an automatic Under:
1. delay then full game;
2. wet-field/command/defence effects;
3. interruption causing starter removal and bullpen exposure;
4. suspension/no-game/operator-void branch.
The centre receives no simplistic rain deduction; uncertainty width increases.

## Joint run object
Raw Hanshin component:
`(Hanshin offense 3.71 + Hiroshima RA 3.69)/2 = 3.70`
Adjust:
-0.35 Tokoda established starter branch
-0.20 Koshien run/HR suppression
+0.10 Hanshin intact top-five core + home-last-bat
+0.05 Hiroshima relief-chain cumulative burden
+0.00 rain centre sign (variance only)
= **3.30**

Raw Hiroshima component:
`(Hiroshima offense 3.00 + Hanshin RA 3.12)/2 = 3.06`
Adjust:
-0.65 Takahashi elite 1.90 ERA / K-BB / length branch
-0.20 Koshien suppression
-0.15 Kozono absent + weak lower-order/pitcher-batting structure
+0.10 right-handed middle-order counter-route vs LHP
+0.05 interruption/early-hook upper-tail allowance
= **2.21**

**Joint centre = 5.51 runs.**
Working width: **±3.1 runs**, widened for rain interruption, wet-ball/field effects, starter-hook uncertainty, HR/sequencing clusters, home ninth, and 10th-12th innings.

## Separation / winner
Central separation:
`Hanshin 3.30 - Hiroshima 2.21 = Hanshin +1.09`.

Three-way final-state subjective view:
- **Hanshin win 63%**
- Hiroshima win 31%
- tie after 12 innings 6%

Run-line:
- **Hiroshima +1.5: 57%**
- Hanshin -1.5: 43%

## Total 5.5
- **Under 5.5: 54%**
- Over 5.5: 46%

The line is extremely close to the 5.51 centre. Rain increases width rather than providing a clean Under sign, so neither total side is high confidence.

## Additional team-total contracts
- **Hiroshima team total Under 3.5: 76%**
- **Hanshin team total Over 1.5: 74%**

## Ranked four
1. **Hiroshima team total Under 3.5 — 76% UNVALIDATED_SUBJECTIVE — SUPPORTED / MEDIUM-HIGH**
2. **Hanshin team total Over 1.5 — 74% — SUPPORTED / MEDIUM**
3. **Hanshin match winner — 63% — SUPPORTED / MEDIUM**
4. **Hiroshima +1.5 — 57% — LEAN / MEDIUM-LOW**

## Supplied-line audit
- Tigers -1.5: **43%**
- **Carp +1.5: 57%**
- Over 5.5: **46%**
- **Under 5.5: 54%**

## Potential winner
**Hanshin Tigers — 63% win probability.**
Hiroshima 31%; official tie 6%.

Central score family: **Hanshin 3-2, Hanshin 3-1, Hanshin 2-1**; Hiroshima 3-2 is the main opposing branch.

## Sources
Drive: `METHOD.md`; `RULES_BASEBALL.md`; current local running log.
Official/current:
- NPB Sep9 schedule / announced starters.
- NPB 2026 Central League team batting, pitching and standings.
- NPB Haruto Takahashi and Hiroki Tokoda official pitching records.
- SportsNavi exact Sep9 game page: posted lineups, bench, start-delay state, recent starter form, H2H.
- Nikkansports Sep8: Tokoda slide start and Kenta Suzuki bullpen move.
- Baseball Chronicle: 2026 Koshien park factors.
- Exact Koshien hourly weather/JMA alert feed.
- Current reporting on Kozono's Aug18 demotion.
One NPB homepage rendering that displayed impossible later-day finals before the local cutoff was quarantined as time-inconsistent and not used for prediction-time state.

Bookmaker odds, implied probabilities, line movement, consensus and tipster/model predictions were excluded.

**P-354 STATUS:** `PREGAME / START-DELAY ANNOUNCED — UNSETTLED`  
**Retrospective:** deferred  
**Next local forecast slot:** **P-355**


### Settlement / retrospective addendum — 2026-09-10

**Current status:** `FINAL / SETTLED`.

**Official NPB final:** Hiroshima Carp **3–1** Hanshin Tigers. Rain delayed first pitch to **18:31 JST**. Hiroki Tokoda threw **8 scoreless innings**; Hanshin's only run was a ninth-inning solo homer. Hiroshima scored all three runs in the seventh.

| Contract | Issued probability | Result |
|---|---:|---|
| Rank #1 Hiroshima TT Under 3.5 | 76% | **WIN** — exactly 3 |
| Rank #2 Hanshin TT Over 1.5 | 74% | **LOSS** — 1 |
| Rank #3 Hanshin winner | 63% | **LOSS** |
| Rank #4 Hiroshima +1.5 | 57% | **WIN** |
| Supplied Hanshin -1.5 | 43% | **LOSS** |
| Supplied Under 5.5 | 54% | **WIN** — total 4 |
| Potential winner: Hanshin | 63% | **LOSS** |

**Brier:** mean **0.2968** over 4 ranked rows.

**Q1 — actual driver:** Tokoda's length/control suppressed Hanshin through eight innings, while Hiroshima's decisive scoring came in one seventh-inning starter-to-relief transition.

**Q2 — knowable?** **Yes.** The card explicitly gave Tokoda an established-starter negative adjustment, Koshien was strongly run suppressing, and the total centre was only 5.51. Despite that, Hanshin Over 1.5 was assigned 74% and Hanshin winner 63%.

**Q3 — smallest change:** before placing a high-probability favourite team Over/winner in a low-centre game, explicitly assign mass to the **opponent starter long-start/zero-or-one-run branch** and re-query both contracts from the same state family.

**Deep review.** Rank #1 and the supplied Under were consistent with the actual low-scoring environment; Rank #2/#3 were not. The card therefore had a **cross-contract coherence problem**, not a broad inability to see the low total.

**Recommended destination:** `RULES_BASEBALL.md` starter-length and low-total separation controls; reinforce `G-L1`. No new gate.

**Settlement source:** NPB official English BIS: https://npb.jp/bis/eng/2026/games/s2026090901426.html

---


# P-355 — Sydney FC vs Melbourne Victory — Australia Cup Semi-final

**Issued view:** `PREGAME`  
**Competition:** Hahn Australia Cup 2026 — Semi-final, single-leg knockout  
**Venue:** St George Venues Jubilee Stadium, Kogarah, NSW  
**Official kickoff:** 2026-09-09 19:30 AEST  
**Final volatile refresh:** 2026-09-09 19:15:34 AEST  
**State at cutoff:** structured tournament feed `Scheduled`; no live play incorporated  
**Method:** `MDS-2026.09.06-v4.0 / SFA-SOCCER`  
**Population:** `EXPLORATORY — NOT PRIMARY_SCORED`  
**Mode:** `SPORTS_ONLY / MARKET_BLIND`  
**Probability tier:** `UNVALIDATED_SUBJECTIVE`  
**Retrospective:** DEFERRED BY USER

## A. Competition / endpoint freeze

Football Australia's Australia Cup rules state every tie must be decided on the day: if level after 90 minutes, extra time is played, then penalties if still level.

Research endpoints:
- 1H goal markets: first 45 minutes + first-half stoppage.
- Full goal totals: regulation 90 minutes + stoppage only.
- Side/double chance: regulation only unless explicitly labelled `to advance`.
- Corner contract below: **regulation-only Opta/FotMob corner count; extra time excluded**.
- Potential regulation winner and `to advance` are shown separately.

Operator-specific corner/extra-time/action terms were not supplied; `OPERATOR_ACTION = UNKNOWN_DEFINITION`.

## B. Participant / lineup gate

### Official/current availability
**Sydney FC**
- Head coach: Patrick Kisnorbo.
- A-Leagues' current Sep 8 preview reports Kisnorbo has a **fully fit squad**.
- New RB James Overy is fit and available for a possible debut.
- Oriola Sunday may make his club debut.
- Jake Hollman may return after the hamstring issue.
- Akol Akon returned from a calf issue in the quarter-final and is still building match fitness.

**Melbourne Victory**
- Head coach: Giovanni Savarese.
- Official Sep 8 semi-final squad: Louis D'Arrigo, Jason Davidson, Jack Duncan, Denis Genreau, Michael Ghossaini, Matthew Grimaldi, Brendan Hamill, Joshua Inserra, Keegan Jelacic, Franco Lino, Tom Lockyer, Charles Nduka, Malik Olukhale, Santos, Harrison Sawyer, Harrison Shillington, Xavier Stella, Jordi Valadon, Jack Warshawsky, Philipp Ziereis.
- Genreau has returned from a viral illness and played 45 minutes vs Oakleigh.
- Lockyer completed 90 minutes vs Oakleigh.
- No current major Victory absence was announced in the official semi-final squad.

### XI/GK conflict
No field-owning Sydney FC / Melbourne Victory / Australia Cup webpage exposed a complete official starting XI and bench by the 19:15:34 cutoff.

A current secondary lineup feed was **quarantined** because its Victory XI included Ibrahim Rachidi, a player absent from Melbourne Victory's official semi-final squad. Per the source-conflict rule, the feed cannot promote the XI/GK state to `CONFIRMED_OFFICIAL`.

Latest role priors:
- Sydney's quarter-final cup keeper was Gus Hoefsloot.
- Victory's cup keeper has been Jack Duncan.
- These are role priors, **not claimed confirmed starters**.

`SO-P2 participant gate`: **NOT FULLY PASSED**.  
Consequence: any side/double-chance/handicap row is capped `FORCED RANK / MEDIUM-LOW`. Player props are not promoted.

Bench-depth integer: **UNRESOLVED** because official XI/bench allocation is not available and both rosters have meaningful offseason turnover. Bench expected-minute branches are retained qualitatively.

## C. Latest cup paths / current competitive state

### Sydney FC — 2026 Australia Cup
- Bayswater City 1-5 Sydney
- Brisbane Roar 2-4 Sydney
- SD Raiders 0-1 Sydney

Mechanisms:
- Takahiro Sekine scored at 2' vs Brisbane and 33' vs SD Raiders.
- Tiago Quintal has four Cup goals.
- Sydney created several first-half chances against SD Raiders, with efforts cleared off the line.
- Gus Hoefsloot was highlighted by Australia Cup reporting for seven saves in the quarter-final.

### Melbourne Victory — 2026 Australia Cup
- Kingborough Lions 0-4 Victory
- Western Sydney Wanderers 0-0 at 90 (1-1 AET; Victory won pens)
- APIA Leichhardt 0-0 at 90 (Victory won 1-0 AET)

Mechanisms:
- Victory have **not conceded a regulation-time goal in three Cup ties**.
- Their last two Cup ties were 0-0 after 90.
- APIA quarter-final was low-event for long periods; late Jelacic/Grimaldi attempts were blocked.
- Harry Sawyer scored in extra time in both the WSW and APIA ties, giving Victory a genuine late bench/extra-time threat.
- Jack Duncan has supplied high-value cup goalkeeping, including three shootout saves vs WSW.

## D. L5 / L10 / L15 / L20 audit

Competitive matches only; Cup entries are regulation-oriented for the 90-minute goal target. Friendlies are excluded from the record window.

| Window | Sydney FC | Melbourne Victory |
|---|---|---|
| **L5** | **3-1-1**, 11 GF / 5 GA | **2-2-1**, 6 / 1 |
| **L10** | **5-4-1**, 17 / 8 | **4-4-2**, 18 / 8 |
| **L15** | **6-6-3**, 21 / 13 | **6-7-2**, 28 / 15 |
| **L20** | **8-7-5**, 28 / 18 | **8-7-5**, 36 / 21 |

No streak receives directional weight by itself. The relevant mechanisms are current chance creation, defensive structure, goalkeeper state, roster changes and knockout incentives.

## E. Inherited 2025/26 A-League process prior

FBref 2025/26 league shooting:
- Sydney: **33 goals, 400 shots, 134 SOT** in 26 matches = 1.27 goals, 15.38 shots, 5.15 SOT per 90.
- Victory: **43 goals, 451 shots, 147 SOT** = 1.65 goals, 17.35 shots, 5.65 SOT per 90.
- Opponents vs Sydney: 24 goals, 371 shots, 126 SOT.
- Opponents vs Victory: 32 goals, 299 shots, 96 SOT.

These are **inherited priors**, not the current Cup regime: both clubs have undergone material offseason roster/coach changes.

## F. Direct H2H process

### 2 May 2026: Melbourne Victory 0-1 Sydney
Opta/FotMob / 365Scores:
- possession 51-49 Victory
- xG 1.29-0.69 Victory
- shots 16-6 Victory
- SOT 6-2 Victory
- opposition-box touches 27-11 Victory
- corners **10-6 Victory**
- Sydney won via Patrick Wood at 80'.

Interpretation: Sydney's win does **not** prove process dominance; Victory generated more territory and chances but failed to convert. It is particularly useful for the corner and draw-band branches.

### 7 Mar 2026: Sydney 2-2 Victory
- 35 total shots (18-17)
- current Opta/FotMob record: Sydney xG 2.56, Victory 1.42
- corners **12-7 Sydney** in the recorded match stats
- HT 0-1.

The two most recent Big Blues therefore produced **16 and 19 total corners** while showing that territory and scoreboard result can diverge.

## G. Goal event object

### League-process starting components

Sydney:
`(Sydney attack 33/26 = 1.27 + Victory conceded 32/26 = 1.23) / 2`
= **1.25**

Victory:
`(Victory attack 43/26 = 1.65 + Sydney conceded 24/26 = 0.92) / 2`
= **1.285**

Raw total prior = **2.535 goals**

### Signed current-regime adjustments

Sydney component:
- `+0.10` home/Jubilee regulation exposure
- `+0.10` current Cup attacking personnel: Sekine/Quintal/Akon plus fully-fit/new-option branch
- `-0.10` Victory's current Cup regulation defensive/keeper control
= **1.35**

Victory component:
- `-0.15` last-two-Cup regulation attack has been contained to 0-0, supported by low-event APIA process rather than result alone
- `-0.10` Sydney current Cup defensive/keeper branch
- `+0.05` Victory's improved bench/freshness after Genreau/Lockyer return and Sawyer impact role
- `-0.05` away/home-field separation
= **1.04**, rounded **1.05**

Weather: `0.00` signed centre; wind is carried in width.

### Joint centre
- **Sydney 1.35**
- **Victory 1.05**
- **Combined centre ≈ 2.40 goals**
- Width: **±1.65 goals**, widened for unresolved XI/GK sheet, finishing/keeper variance, set plays, red-card tail and knockout score-state changes.

### Goal-family mass
- **0-1 goals:** 30%
- **exactly 2:** 27%
- **exactly 3:** 22%
- **4+ goals:** 21%

Derived:
- **Under 2.5: 57%**
- Over 2.5: 43%
- **Under 3.5: 79%**
- **Over 1.5: 70%**

`G-L8` total-line geometry:
- 2.5 is very near the 2.40 centre -> only a modest Under.
- 3.5 is materially above centre -> stronger Under.
- 1.5 is materially below centre -> stronger Over.

## H. First-half object

First-half centre: **~0.80 goals**.

Mechanisms supporting early scoring:
- Sydney scored inside 2' vs Brisbane and at 33' vs SD Raiders.
- Sekine/Quintal/Garuccio have direct first-half Cup creation.
- Victory scored inside 15' vs Kingborough.

Mechanisms suppressing:
- Victory's last two Cup ties were 0-0 at 90, including a largely quiet opening half hour vs APIA.
- May Big Blue was 0-0 HT.
- Semi-final downside risk from conceding first is meaningful.

First-half state mass:
- **0 goals:** 44%
- **exactly 1:** 38%
- **2+ goals:** 18%

Therefore:
- **1H Over 0.5: 56%**
- 1H Under 0.5: 44%
- **1H Under 1.5: 82%**

The supplied O0.5 is preferred, but only modestly.

## I. Regulation winner / separation object

90-minute:
- **Sydney win 42%**
- **Draw 28%**
- Victory win 30%

Thus:
- **Sydney +0.5 / 1X = 70%**, but `FORCED RANK / MEDIUM-LOW` because `SO-P2` official XI/GK gate is unresolved.

Potential regulation winner: **Sydney FC, 42%**.

`To advance` branch:
- Sydney **57%**
- Victory 43%

The draw branch remains important. Victory's Jack Duncan has real cup shootout evidence, but one shootout is aggressively shrunk and does not erase Sydney's home/regulation edge.

## J. Corner process

Research settlement definition:
**regulation-only corners, Opta/FotMob definition; extra time excluded.**

2025/26 A-League inherited corner priors:
- Sydney: **4.73 for / 5.31 against / 10.04 match total**
- Victory: **6.19 for / 4.69 against / 10.88 total**
- league average ~10.2.

Direct process:
- May Big Blue: **Victory 10-6 Sydney** corners, with Victory 16 shots, 27 box touches and repeated defensive clearances/crossing.
- March Big Blue: **Sydney 12-7 Victory** corners.
- Victory's Cup quarter-final included Davidson wide delivery, Sawyer aerial threat and blocked late Jelacic/Grimaldi attempts.
- Sydney's Cup path includes Garuccio/Sekine/Akon width and set-piece/cross routes.

Corner arithmetic:
`(10.04 + 10.88)/2 = 10.46`
`+0.35` Victory high direct corner generation
`+0.25` recent H2H width/block/clearance continuity
`-0.20` Victory's recent Cup low-event regulation control
`+0.00` strong southerly wind sign unresolved; widen variance rather than force direction

**Corner centre ≈ 10.86**
Width: **±4.2 corners**

State family:
- 0-7: 22%
- exactly 8: 11%
- 9-11: 37%
- 12+: 30%

**Total corners Over 8.5 = 67%**
Evidence: `SUPPORTED / MEDIUM`.

Kill path: an early goal creating prolonged control rather than chase, plus fewer wide/block sequences than the recent H2Hs.

## K. Bench / substitution phase

Sydney's full-fit branch creates meaningful second-half options:
- Al Hassan Toure
- Wataru Kamijo
- Gabriel Popovic
- Oriola Sunday / Jake Hollman / James Overy depending on XI allocation.

Victory's official squad provides:
- Harry Sawyer as a proven late Cup scorer
- Denis Genreau, now back
- Tom Lockyer
- Harry Shillington
- Michael Ghossaini / Malik Olukhale.

This is why the full-match **Over 1.5** remains stronger than the supplied Over 2.5: both teams retain late attacking/substitution routes even if the first half is controlled.

## L. Venue / weather

Exact Kogarah/Jubilee Stadium weather:
- around **15-16°C** near kickoff
- BOM rain probability only ~5% around 19:00 and ~10% around 22:00
- strong southerly winds were forecast in the Sydney area during the day, around 30-45 km/h.

Rain is not a meaningful game-risk branch. Wind can alter crosses, long balls, shooting and set-pieces in both directions; without a reliable pitch-orientation/game-time wind observation, **no signed goal or corner adjustment is applied**, but event width is slightly widened.

## M. Ranked five

| Rank | Selection | UNVALIDATED_SUBJECTIVE | Evidence |
|---:|---|---:|---|
| **1** | **1st Half Under 1.5 Goals** | **82%** | `SUPPORTED / MEDIUM` |
| **2** | **Combined Total Under 3.5 Goals** | **79%** | `SUPPORTED / MEDIUM` |
| **3** | **Sydney FC +0.5 / Double Chance 1X (90 min)** | **70%** | `FORCED RANK / MEDIUM-LOW — official XI/GK unresolved` |
| **4** | **Combined Total Over 1.5 Goals** | **70%** | `SUPPORTED / MEDIUM` |
| **5** | **Total Match Corners Over 8.5 (90 min, Opta/FotMob)** | **67%** | `SUPPORTED / MEDIUM` |

Tie-break between Rank 3 and Rank 4: 1X has the slightly more protected probability mass but carries the mandatory participant-confidence cap; Over 1.5 is cleaner evidentially.

## N. Supplied-line audit

| Supplied market | Probability |
|---|---:|
| **1H Over 0.5** | **56%** |
| 1H Under 0.5 | 44% |
| Over 2.5 | 43% |
| **Under 2.5** | **57%** |

## O. Potential winner

**Potential regulation winner: Sydney FC — 42%.**  
Draw: **28%**.  
Melbourne Victory: **30%**.

**To advance:** Sydney FC **57%**, Melbourne Victory **43%**.

Central regulation score family:
- Sydney **1-0**
- **1-1**
- Sydney **2-1**
- Victory **1-0** opposing branch.

## P. Source register

### Governing Drive
- `METHOD.md` — MDS-2026.09.06-v4.0.
- `RULES_SOCCER.md` — SFA-SOCCER.
- `LEAGUE_RULES_SOCCER.md` — shared knockout/endpoint rules; no current Australia Cup-specific subsection found.
- Current local running log.

### Official / club / competition
- Football Australia / Australia Cup: official Sep 9 semi-final schedule and current semifinal preview.
- Australia Cup `About the Competition`: every tie decided on the day with ET + penalties if level after 90.
- Sydney FC gameday guide and Sep 7 semifinal preview.
- Sydney FC official QF/R16/R32 reports.
- Melbourne Victory official Sep 8 semifinal preview and 19-man squad.
- Melbourne Victory official QF/R16/R32 reports.
- Melbourne Victory Sep 3 Oakleigh friendly report for Genreau/Lockyer current minutes.
- Jubilee Stadium official event page.
- Bureau of Meteorology Kogarah forecast/detailed forecast.

### Process / statistics
- FBref 2025/26 A-League shooting and opponent-shooting tables.
- SoccerStats / FootyMetrics 2025/26 A-League corner rates.
- FotMob/Opta May 2 Big Blue xG/shots/box-touch record.
- 365Scores May 2 corners/shot detail.
- FotMob March 7 Big Blue process record.
- BeSoccer current competitive result histories for L5/L10/L15/L20 reconstruction.

### Participant conflict
- A current secondary lineup page was inspected but **quarantined** for the current XI because its Victory XI included Ibrahim Rachidi, absent from Victory's official Sep 8 semifinal squad. Its lineups are not used as `CONFIRMED_OFFICIAL`.

### Exclusions
Bookmaker odds, implied probabilities, line movement, consensus, tipster picks and synthetic predictive models were excluded.

**P-355 STATUS:** `PREGAME — UNSETTLED`  
**Retrospective:** deferred  
**Next local forecast slot:** **P-356**


### Settlement / retrospective addendum — 2026-09-10

**Current status:** `FINAL / PARTIAL` — score/side/goal rows settled; corner Rank #5 remains `TMP-OPEN-20260910-03 / PROVISIONAL RESEARCH WIN`.

**Verified final:** Melbourne Victory beat Sydney FC **2–0**, half-time **1–0**. Keegan Jelacic scored in the 2nd minute after Sydney lost possession; Jordan Courtney-Perkins scored an own goal at 61'. Sydney's official report describes sustained possession/territory but difficulty turning it into clear chances.

| Contract | Issued probability | Result |
|---|---:|---|
| Rank #1 1H Under 1.5 | 82% | **WIN** — one first-half goal |
| Rank #2 Under 3.5 | 79% | **WIN** — total 2 |
| Rank #3 Sydney +0.5 / 1X | 70% | **LOSS** |
| Rank #4 Over 1.5 | 70% | **WIN** — exactly 2 |
| Rank #5 Corners Over 8.5 | 67% | **PROVISIONAL WIN** — secondary displays 5–4 = 9 |
| Supplied 1H Over 0.5 | 56% | **WIN** |
| Supplied Under 2.5 | 57% | **WIN** |
| Potential regulation winner: Sydney | 42% | **LOSS** |
| Sydney to advance | 57% | **LOSS** |

**Brier, finalized ranked rows only:** mean **0.1641** over 4 rows.

**Q1 — actual driver:** Victory converted a very early Sydney turnover and then defended the lead. Sydney accumulated territory but did not convert it into adequate shot-on-target quality; the second goal was an own goal.

**Q2 — knowable?** **Partly.** Victory's current Cup defensive/keeper control and Sydney's unresolved official XI/GK were in the card; the Sydney side was correctly capped `FORCED RANK / MEDIUM-LOW`. The exact second-minute error was not knowable.

**Q3 — smallest change:** no new rule. Continue separating **territory/possession from shot quality**, and retain the participant confidence cap when the official XI/GK is unresolved.

**Additional source lesson:** the card correctly froze an exact corner provider/definition. Because that aggregate has not been recovered directly, the 5–4 secondary consensus is only provisional even though it clears Over 8.5 by one corner.

**Recommended destination:** `RULES_SOCCER.md` territory-vs-chance-quality examples; `SOURCES.md` derivative-provider coverage. No predictive rule promotion.

**Settlement sources:**
- Sydney FC official report: https://sydneyfc.com/news/brave-sydney-fc-bow-out-after-dominant-semi-final-display/
- A-Leagues report: https://aleagues.com.au/news/australia-cup-aleague-men-sydney-melbourne-victory-goals-match-report/
- Secondary corner display: https://www.totalcorner.com/team/view/3580

---


# P-356 — KT Wiz @ Samsung Lions — KBO

**Issued view:** PREGAME  
**Competition:** 2026 KBO League regular season  
**Venue:** Daegu Samsung Lions Park, Daegu  
**Official first pitch:** 2026-09-09 18:30 KST / 19:30 AEST  
**Final volatile refresh:** 2026-09-09 18:26:22 KST / 19:26:22 AEST  
**State:** PREGAME — no live play incorporated  
**Method:** `MDS-2026.09.06-v4.0 / SFA-BASEBALL`  
**Population:** `EXPLORATORY — NOT PRIMARY_SCORED`  
**Mode:** `SPORTS_ONLY / MARKET_BLIND`  
**Probability tier:** `UNVALIDATED_SUBJECTIVE`  
**Operator action/listed-pitcher/shortening terms:** `UNKNOWN_DEFINITION`  
**Retrospective:** DEFERRED BY USER

## A. KBO contract/rules freeze

- KBO regular season; universal DH.
- Scheduled nine innings.
- 2026 regular-season games can end tied after the 11th inning.
- No MLB-style automatic runner is assumed.
- Samsung owns home-last-bat entitlement.
- User slate: Samsung -1.5; KT +1.5; O/U 10.5.
- Under research-grade standard settlement, KT +1.5 covers a KT win, a one-run Samsung win, or an official tie; Samsung -1.5 requires a Samsung win by 2+.

## B. Starter identity

Current KBO/current schedule sources agree:
- **KT: Ko Young-pyo (RHP/submarine), 10-6, 4.00 ERA**
- **Samsung: Won Tae-in (RHP), 7-6, 4.26 ERA**

## C. Participant / lineup state

### Samsung — current posted lineup
1. Kim Ji-chan CF
2. Kim Sung-yoon RF
3. Koo Ja-wook LF
4. Choi Hyung-woo DH
5. Ryu Ji-hyuk 2B
6. Jeon Byeong-woo 3B
7. Lewin Díaz 1B
8. Kang Min-ho C
9. Lee Jae-hyun SS

Availability notes:
- Ryu Ji-hyuk was hit on the left knee by a foul ball Sep 8, but current reporting says it was a simple contusion and he is starting.
- Kim Young-woong is not in the starting lineup; Jeon Byeong-woo starts at 3B.
- Park Seung-kyu is also replaced by Kim Sung-yoon in RF.

### KT
A current field-owning Sep-9 complete batting order was not independently recovered before cutoff. Therefore:
- exact order = **UNRESOLVED / SECONDARY_ONLY**
- no player prop promoted
- team-level rows retain current roster mixture.

Most recent confirmed Sep-8 order:
Choi Won-jun, Kim Sang-su, Ahn Hyun-min, Sam Hilliard, Kim Hyun-soo, Heo Kyoung-min, Oh Yoon-suk, Cho Dae-hyun, Jang Jun-won.

The current roster still contains the key offensive core; no same-day report found a material injury to Choi Won-jun, Ahn Hyun-min or Hilliard.

## D. Current standings / season team process

Official KBO standings through Sep 8:
- Samsung: **73-46-3, 1st, .613**
- KT: **70-46-3, 2nd, .603**

Official team offense:
- Samsung: **708 runs / 122 = 5.80 per game**, .279 AVG, .369 OBP, .417 SLG, .786 OPS, 112 HR.
- KT: **651 / 119 = 5.47**, .280 AVG, .363 OBP, .399 SLG, .762 OPS, 90 HR.

Official team pitching:
- Samsung: **545 RA / 122 = 4.47**, team ERA **4.12**, WHIP 1.36.
- KT: **558 / 119 = 4.69**, team ERA **4.37**, WHIP 1.42.

## E. L5 / L10 / L15 / L20 audit

Reconstructed from current schedule results; no streak gets independent weight.

| Window | Samsung | KT |
|---|---|---|
| **L5** | **3-2**, 25 RS / 18 RA | **2-3**, 25 / 30 |
| **L10** | **8-2**, 67 / 29 | **6-4**, 52 / 49 |
| **L15** | **10-1-4**, 86 / 48 | **8-1-6**, 75 / 61 |
| **L20** | **14-1-5**, 136 / 76 | **10-1-9**, 100 / 91 |

Samsung's recent surge is supported by strong offense and the better season run-prevention profile, not by "momentum" itself. KT's wider total distribution includes a 13-11 game but also multiple 3-run outputs; opponent/start context owns tonight's direction.

## F. H2H

Samsung lead the 2026 season series **9-3** before this game.
Recent current meeting: Samsung won **4-2 on Aug 29**.

The H2H result itself receives zero directional weight. Matchup-specific starter data and current lineups are the useful continuity:
- Won vs KT: 3 starts, **3.24 ERA**, 16.2 IP, 20 H, 6 BB, 16 K, 6 ER.
- Ko vs Samsung: 2 starts, **4.50 ERA**, 12 IP, 10 H, 0 BB, 10 K, 6 ER.

## G. Starter exposure

### Ko Young-pyo
2026:
- 23 starts
- **10-6, 4.00 ERA**
- 132.2 IP
- 138 H
- 14 HR
- **20 BB**
- **144 K**
- road ERA **4.30**
- second-half ERA **3.05**

Recent:
- Aug14 vs Kiwoom: 5.1 IP, 3 R
- Aug20 @ LG: 6 IP, 3 R
- Aug27 vs Doosan: 7 IP, 1 R
- **Sep3 vs Hanwha: 3 IP, 9 H, 7 ER, 2 BB, 5 K**

Interpretation:
Ko's excellent command and strong second-half branch remain decision-driving. The Sep3 blow-up is a genuine current-regime warning, but one start does not override the 41.1-inning second-half body of work.

### Won Tae-in
2026:
- 21 starts
- **7-6, 4.26 ERA**
- 120.1 IP
- 138 H
- only **5 HR**
- **25 BB**
- 101 K
- home ERA **3.58**

Recent 10 starts:
- 57.1 IP, **5.02 ERA**
- 71 H, 9 BB, 47 K
- only 2 HR

Most recent:
- Sep3 vs Lotte: **6 IP, 7 H, 2 ER, 0 BB, 7 K**

Interpretation:
Won's contact rate is not dominant, but his walk and HR suppression meaningfully reduces the multi-run cluster route. His 3.24 ERA vs KT is retained as current matchup continuity, not treated as ownership.

## H. Bullpen / prior-day workload

KT Sep8:
- So Hyeong-jun 7 IP, 1 R
- Son Dong-hyun 1 scoreless inning
- closer Park Young-hyun 1 scoreless inning, season save No. 25

KT therefore avoided broad bullpen exposure, but Son/Park carry normal back-to-back availability uncertainty.

Samsung Sep8:
- starter Choi Won-tae covered 5 IP in a 6-4 win over KIA, leaving four relief innings.
- Samsung's season relief structure has been one of its strengths; Kim Jae-yoon is the established closer, with Lee Seung-min and other bridge arms forming a strong season chain.
- more relief innings were required than KT the previous day, so Samsung receives no generic freshness bonus.

## I. Park / weather

Daegu Samsung Lions Park is hitter-friendly in current secondary park-factor reporting (~1.05 overall run environment), so the HR/extra-base cluster tail remains meaningful.

Exact venue weather:
- around **21°C** near first pitch
- partly cloudy to clear
- **0% precipitation** in the main game window.

Weather contributes no rain/termination branch and no major signed run adjustment.

## J. Joint run object

### KT component prior
`(KT offense 5.47 + Samsung RA 4.47) / 2 = 4.97`

Adjust:
- `-0.35` Won home/KT-specific run-suppression branch
- `-0.12` Samsung stronger season pitching/relief depth
+ `0.12` KT top-order OBP/power route
+ `0.05` Daegu hitter-friendly environment
= **4.67 KT runs**

### Samsung component prior
`(Samsung offense 5.80 + KT RA 4.69) / 2 = 5.245`

Adjust:
- `-0.25` Ko second-half command/run-prevention branch
+ `0.25` Ko Sep3 early-hook/contact-cluster warning
+ `0.12` Samsung home power / Daegu environment
- `0.08` Kim Young-woong absent from starting lineup
+ `0.03` KT back-end worked Sep8
= **5.32 Samsung runs**

### Joint centre
**9.99 runs**

Working width: **±4.2 runs**, retaining:
- Ko early-hook branch
- Won contact/sequencing branch
- Daegu HR clusters
- both teams' strong top-order scoring ability
- bullpen score-state
- home ninth
- KBO tie/10th-11th inning branches.

Separation:
`Samsung 5.32 - KT 4.67 = Samsung +0.65`.

## K. Outcome-state family

Approximate final-state mass:
- Samsung win by 2+: **41%**
- Samsung win by exactly 1: **17%**
- KT win: **38%**
- official tie after 11: **4%**

Therefore:
- **Samsung win: 58%**
- **KT +1.5: 59%**
- **Samsung -1.5: 41%**

Representative Rank-1 state:
Samsung 5-4 or 6-4 still cashes Samsung TT Over 3.5; KT +1.5 cashes in the 5-4 state, while Under 10.5 wins at 5-4 and loses at 6-5/7-4 type branches.

## L. Total 10.5

Centre = **9.99**, width = **4.2**
Normalised line distance:
`|10.5 - 9.99| / 4.2 = 0.12`

This is a small edge, so the total cannot receive a high probability.

Final:
- **Under 10.5: 56%**
- Over 10.5: **44%**

Under mechanisms:
- both starters' control
- Won HR suppression
- Ko's broader second-half recovery
- no hot/rain-driven offensive environment.

Over mechanisms:
- both offenses rank at/near the top of KBO scoring
- Daegu park
- Ko's Sep3 short-start tail
- Samsung's recent scoring ceiling
- extra innings if tied.

## M. Additional team-total contracts

### Samsung team total Over 3.5
Centre 5.32.
Support: top-tier offense, home park, Ko's current contact/early-hook tail, Koo/Choi/Díaz depth despite Kim Young-woong sitting.

**70% UNVALIDATED_SUBJECTIVE.**

### KT team total Under 5.5
Centre 4.67.
Support: Won's home/KT split, strong HR suppression, Samsung's superior season pitching chain.

**66% UNVALIDATED_SUBJECTIVE.**

## N. Ranked four

| Rank | Selection | UNVALIDATED_SUBJECTIVE | Evidence |
|---:|---|---:|---|
| **1** | **Samsung Lions team total Over 3.5** | **70%** | `SUPPORTED / MEDIUM` |
| **2** | **KT Wiz team total Under 5.5** | **66%** | `SUPPORTED / MEDIUM` |
| **3** | **KT Wiz +1.5** | **59%** | `LEAN / MEDIUM` |
| **4** | **Combined Total Under 10.5** | **56%** | `LEAN / MEDIUM-LOW` |

## O. Supplied-line audit

| Supplied row | Probability |
|---|---:|
| Lions -1.5 | **41%** |
| **Wiz +1.5** | **59%** |
| Over 10.5 | **44%** |
| **Under 10.5** | **56%** |

## P. Potential winner

Three-way official-final view:
- **Samsung Lions win: 58%**
- KT Wiz win: 38%
- tie: 4%

**Potential winner: Samsung Lions.**

Central score family:
- Samsung **5-4**
- Samsung **6-4**
- KT **5-4**
- 5-5 / tie-extension branch.

## Q. Source register

### Drive
- `METHOD.md` — MDS-2026.09.06-v4.0
- `RULES_BASEBALL.md` — SFA-BASEBALL and KBO rules
- current local running-log continuation

### Official / primary
- KBO official 2026 standings
- KBO official team batting tables
- KBO official team pitching tables
- KBO official Ko Young-pyo game/split/daily records
- KBO official Won Tae-in basic/game/daily records
- KBO current news / Sep8 KT-Samsung race context

### Current reporting / secondary
- current Samsung lineup report (Sep9)
- Newsis/current daily starter listing
- Sep8 KT 3-1 SSG recap for bullpen usage and current order
- Sep8 Samsung 6-4 KIA recap
- current schedule/results database for L5/L10/L15/L20 reconstruction
- current Daegu park-factor reporting
- exact Daegu Samsung Lions Park hourly weather feed

### Exclusions
Bookmaker odds, implied probabilities, market movement, betting consensus and prediction/tipster outputs were excluded. An AI-labelled preview and betting-analysis pages returned during search were not used as predictive evidence.

**P-356 STATUS:** `PREGAME — UNSETTLED`  
**Retrospective:** deferred  
**Next local forecast slot:** **P-357**


### Settlement / retrospective addendum — 2026-09-10

**Current status:** `FINAL / SETTLED`.

**Official KBO final:** KT Wiz **2–0** Samsung Lions. Ko Young-pyo threw **7 scoreless innings**; the only scoring came from Kim Hyun-soo's two-run homer in the sixth. Samsung finished with four hits.

| Contract | Issued probability | Result |
|---|---:|---|
| Rank #1 Samsung TT Over 3.5 | 70% | **LOSS** — 0 |
| Rank #2 KT TT Under 5.5 | 66% | **WIN** — 2 |
| Rank #3 KT +1.5 | 59% | **WIN** |
| Rank #4 Under 10.5 | 56% | **WIN** — total 2 |
| Supplied Samsung -1.5 | 41% | **LOSS** |
| Supplied Over 10.5 | 44% | **LOSS** |
| Potential winner: Samsung | 58% | **LOSS** |

**Brier:** mean **0.2418** over 4 ranked rows.

**Q1 — actual driver:** Ko's strong command/current-regime branch dominated. He kept Samsung scoreless for seven, while Won Tae-in also limited KT; a single two-run homer determined the game.

**Q2 — knowable?** **Yes.** The issued card explicitly documented Ko's **3.05 second-half ERA**, excellent command and several strong recent starts. It then applied `-0.25` for that branch but `+0.25` for one Sep-3 blow-up, effectively cancelling the broader current-regime evidence before adding further Samsung-positive terms.

**Q3 — smallest change:** translate starter quality through **expected innings/batters-faced exposure**. One recent blow-up should mostly widen the early-hook/contact tail unless a persistent directional mechanism is identified; it should not automatically receive an equal-and-opposite centre term to a much larger current-regime sample.

**Deep Rank-#1 review.** Three subordinate rows correctly captured low scoring / KT protection, yet Rank #1 projected Samsung to score 4+ at 70%. That contradiction is evidence of team-component arithmetic misallocation, not merely an unpredictable shutout.

**Recommended destination:** `RULES_BASEBALL.md` `BB-S2/BB-S8` starter exposure and `G-L2` width-vs-direction implementation; `LEARNING_REGISTER.md` observation only.

**Settlement sources:**
- KBO official English scoreboard: https://eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=2026-09-09
- MyKBO detailed box score: https://mykbostats.com/games/13927-KT-vs-Samsung-20260909

---


# P-357 — Dublin Guardians vs Belfast Wolves — ETPL

**Issued state:** PRESTART / TOSS COMPLETE
**Venue:** The Village, Malahide Cricket Club Ground — Pitch 1
**Official start:** 23:15 AEST / 14:15 Irish local
**Forecast freeze:** 23:10:18 AEST
**Toss:** Dublin Guardians won the toss and elected to field
**First innings:** Belfast Wolves batting first
**XI state:** UNRESOLVED at cutoff; team-level participant mixture only
**Method:** MDS-2026.09.06-v4.0 / SFA-CRICKET
**Population:** EXPLORATORY — NOT PRIMARY_SCORED
**Probability tier:** UNVALIDATED_SUBJECTIVE
**Retrospective:** deferred by user

## Conditions
**STRIP STATUS:** NOT FOUND AFTER SEARCH.
**MATCH CONDITIONS STATUS:** OBSERVED.

Six-rung search:
1. Official/broadcast toss commentary: toss found; no exact strip description.
2. Venue/curator: Malahide fixture confirms Pitch 1; no dated curator assessment found.
3. Exact-match specialist previews: general reliable-bounce / early-movement expectation only; not treated as observed strip.
4. ICC pitch-rating lane: attempted; no match-specific pregame rating found.
5. Current conditions: ~17C, cloudy, 0% rain through main match window.
6. Venue-format baseline: historical T20 first-innings references cluster broadly in the mid-150s to low-160s, with much higher tails; no prior completed ETPL match at Malahide before today.

## Current form
Belfast: 3 wins, 1 loss, 1 no-result; 7 points, NRR +0.58.
Dublin: 0 wins, 5 losses; NRR -1.65.

Direct Aug-27 H2H: Belfast 184/7, powerplay 52/3; Dublin 132/9. Belfast won by 52 runs.

Comparable Belfast six-over states: 52/3, 46/1, 51/4, 54/2; mean 50.75.
Recent Belfast ceiling includes 146/3 in 12 overs, with Mark Chapman 71* and David Miller 23*.

## Six-over object
Prior 50.75
-2.0 Malahide new-ball/cool-cloudy branch
+1.0 Belfast aggressive top-order ceiling
+0.0 toss (context only)
= **49.75 centre**, width ~15.

- Under 52.5: **58%**
- Over 52.5: **42%**

## Full-innings object
Two completed Belfast 20-over first innings: 184 and 156; mean 170.
Shrink toward broad Malahide venue prior -> 165.
+5 Dublin tournament bowling fragility / 184 direct H2H concession
+4 Belfast middle/death ceiling
-3 Malahide early-movement/cool-cloudy branch
= **171 centre**, width ~34.

G-L8: |177.5-171|/34 = **0.19**, so only a modest threshold lean.

- Under 177.5: **56%**
- Over 177.5: **44%**
- Belfast 150+ / Over 149.5: **72%**

Central first-innings corridor: **155-185**, modal region roughly **165-178**.

## Winner
Conditional on a completed result:
- **Belfast Wolves 68%**
- Dublin Guardians 32%

Dublin remain live because James Vince has recent 95* and 73 innings and the home bowling pool includes Ashwin/Little/Wood/Dockrell depending on XI.

## Ranked four
1. **Belfast 1st innings 150+ / Over 149.5 — 72% — FORCED RANK / MEDIUM-LOW (XI unresolved)**
2. **Belfast Wolves match winner — 68% — FORCED RANK / MEDIUM-LOW**
3. **Belfast first 6 overs Under 52.5 — 58% — LEAN / MEDIUM-LOW**
4. **Belfast 1st innings Under 177.5 — 56% — LEAN / MEDIUM-LOW**

## Supplied-line audit
- Over 177.5: 44%
- **Under 177.5: 56%**
- Over 52.5: 42%
- **Under 52.5: 58%**

## Sources
Drive: METHOD.md; RULES_CRICKET.md; LEAGUE_RULES_CRICKET.md; DATA_SOURCE_REGISTER.md §6A.
External/current: ETPL official Match 18 and team pages; Malahide Cricket Club fixture page; Cricbuzz current toss page; CricketEurope standings/results; Cricket Ireland-branded Aug-27 scorecard; current Malahide weather.
Market/tipster odds and predictions excluded.

**P-357 STATUS:** PRESTART / TOSS COMPLETE — UNSETTLED
**Next local forecast slot:** P-358


### Settlement / retrospective addendum — 2026-09-10

**Current status:** `FINAL / SETTLED`.

**Verified final:** Belfast Wolves were bowled out for **107 in 19.4 overs**; Dublin Guardians chased **111/2 in 14.3** and won by **8 wickets**. Belfast's six-over powerplay was **43/3**. Craig Young took five wickets and was Player of the Match.

| Contract | Issued probability | Result |
|---|---:|---|
| Rank #1 Belfast 150+ / Over 149.5 | 72% | **LOSS** — 107 |
| Rank #2 Belfast winner | 68% | **LOSS** |
| Rank #3 Belfast first 6 Under 52.5 | 58% | **WIN** — 43/3 |
| Rank #4 Belfast innings Under 177.5 | 56% | **WIN** |
| Supplied first-6 Over 52.5 | 42% | **LOSS** |
| Supplied innings Over 177.5 | 44% | **LOSS** |
| Potential winner: Belfast | 68% | **LOSS** |

**Brier:** mean **0.3377** over 4 ranked rows.

**Q1 — actual driver:** an early and continuing wicket cluster destroyed Belfast's resource base. The eventual Dublin XI contained a high-impact attack including Craig Young, David Willey, Josh Little, Matt Hollard and Ravichandran Ashwin; Belfast was already 43/3 at the powerplay and never rebuilt.

**Q2 — knowable?** **The exact XI was not known at issue, but the uncertainty was known.** The card explicitly said XI unresolved and even named Ashwin/Little/Wood/Dockrell as possible Dublin bowling resources. Despite that, it still assigned 72% to Belfast 150+ and 68% to Belfast winner. The missing-participant uncertainty was therefore disclosed but insufficiently propagated into probabilities.

**Q3 — smallest change:** after toss but before start, if XI remains unresolved, build an explicit **opponent-bowling-XI mixture** over the named high-impact combinations and perform one last field-owner/scorecard refresh. Concentrated probabilities should fall naturally if strong attack branches remain live.

**Deep Rank-#1 review.** The two Unders won; the Belfast scoring/winner thesis failed. This is not a lesson that Belfast's prior form was meaningless. It is a participant-resolution and wicket-resource problem: the exact attack mattered more than the small historical Belfast innings sample.

**New-source observation:** the Cricket Ireland-branded CricketArchive scorecard exposes toss, result, full scorecard, officials and innings details and is a strong **candidate ETPL settlement lane**. The ETPL official page identified NV Play as its live-scoring provider but remained stale as `UPCOMING` in the crawl after the match, so a stale official shell must not override a completed scorecard.

**Recommended destination:** `RULES_CRICKET.md` participant/XI refresh and wicket-cluster controls; `DATA_SOURCE_REGISTER.md`/`SOURCES.md` for an ETPL CricketArchive/NV Play lineage audit. Do not promote the source until ownership/lineage is explicitly verified.

**Settlement sources:**
- Cricket Ireland-branded CricketArchive scorecard: https://www.cricketarchive.com/CricketIreland/Scorecards/1458/1458971.html
- CricketWorld scorecard / powerplay field: https://www.cricketworld.com/cricket/dublin-guardians-vs-belfast-wolves/match/scorecard/98341
- ETPL official event shell (provider-lineage/staleness evidence): https://www.etplofficial.com/matches/6a688c61b30844b0969df8b4

---

# 5. NEXT-ID CONTROL

| Field | Value |
|---|---|
| Last P-345+ issued ID | **P-357** |
| Next local forecast ID | **P-358** |
| P-345+ unsettled queue | **Only three derivative fields:** `TMP-OPEN-20260910-01` (P-345 corners), `-02` (P-346 corners), `-03` (P-355 corners). All parent events FINAL. |
| Drive write policy | **READ ONLY** |
| Fresh Drive canonical state | **P-333–P-344 occupied; next canonical P-345. No collision with local P-345–P-357 at the time of this pass.** |
| Automatic retrospective | Only when required by the user's current query/workflow; no hindsight rewriting |
| Updated log returned after each new query | **YES** |

---

# 6. APPEND-ONLY CHANGELOG

## 2026-09-09 01:41 Australia/Melbourne — INITIALIZATION

- New local continuation created.
- User-directed start ID fixed at **P-345**.
- Drive kept read-only.
- Current v4.0 governing documents refreshed.
- Dedicated unsettled/incomplete queue created at the top.
- Full per-card source-register requirement preserved.
- No P-345 forecast issued yet.

## 2026-09-09 — P-345 ISSUED

- P-345 appended before delivery.
- Event: Club Brugge vs Aston Villa, UEFA Champions League.
- Confirmed starting XIs and full benches retrieved before issue.
- Venue-specific weather gate passed.
- Ranked five and all supplied O/U complements assigned `UNVALIDATED_SUBJECTIVE` probabilities.
- P-345 retained in the unsettled queue at the top.
- Retrospective explicitly deferred by user.
- Next local slot advanced to P-346.

## 2026-09-09 — P-346 ISSUED

- Opponent omitted in user wording; official UEFA schedule resolved event identity to **AEK Athens vs LASK**.
- P-345 state-checked before scheduled start and left unsettled; no retrospective performed.
- UEFA confirmed both starting XIs before P-346 freeze.
- Late Strakosha absence recorded; no diagnosis invented.
- LASK's starting attack confirmed as Lang + Usor; Adeniran not in XI.
- Current full benches retrieved from a secondary lineup source and explicitly marked `SECONDARY_ONLY`.
- L5/L10/L15/L20 form reconstructed with friendlies excluded and LASK-Celtic 25 Aug frozen at 90-minute 4-1 for trend purposes.
- Venue/environment identity reconciled to Allwyn/OPAP Arena, Nea Filadelfeia.
- Goal, separation, first-half and corner objects recorded with explicit arithmetic and uncertainty widths.
- Corner row capped `FORCED RANK / MEDIUM-LOW` because direct cross/end-line event layers were incomplete.
- P-346 appended before delivery and retained at the top unsettled queue.
- Retrospective explicitly deferred.
- Next local slot advanced to **P-347**.

## 2026-09-09 — P-347 ISSUED

- User's estimated start time was corrected from 8 Sep 19:30 AEST to the official **9 Sep 11:40 AEST / 8 Sep 18:40 PDT** first pitch.
- P-347 was frozen pregame at 11:26:54 AEST.
- Fresh `RULES_BASEBALL.md` read and `SFA-BASEBALL` applied.
- Quantrill/Miller starter identity handshaken against current MLB/Mariners schedule/probable records.
- Current batting orders were available only through concordant secondary feeds at freeze and explicitly marked `SECONDARY_ONLY`.
- T-Mobile Park environment and roof state were retrieved; roof reported open, weather clear/mild.
- L5/L10/L15/L20 trend, starter, bullpen, platoon, park, extras and run-cluster branches recorded.
- Explicit joint total centre **7.60** and Texas separation centre **+0.90** recorded.
- Ranked four published with `UNVALIDATED_SUBJECTIVE` probabilities.
- P-347 retained in unsettled queue; retrospective deferred.
- Next local slot advanced to **P-348**.

## 2026-09-09 — P-348 ISSUED

- Final state refresh passed at 11:34:49 AEST, before official 11:40 AEST first pitch.
- Fresh `RULES_BASEBALL.md` read from Google Drive; Drive remained read-only.
- Official probable starters confirmed as José Soriano and Jack Perkins.
- MLB crawl-visible lineup page still showed TBD; current concordant batting orders were retrieved from current reporting quoting team releases and explicitly classified `SECONDARY_ONLY`.
- Springer absence recorded without inventing an injury diagnosis.
- Sutter Health Park environment gate passed: ~91°F and 2026 Statcast park factor 113 / run factor ~128 / HR factor ~127.
- Perkins' 6.50 ERA was regressed toward ~4.04 xERA rather than treated literally; command and early-hook risk retained.
- Soriano's 3.52 season ERA was reconciled with a weaker ~4.36 Toronto stint.
- Joint run centre logged at ~9.9 runs with ±4.0 width.
- Integer 9.0 total push mass preserved.
- Ranked four and potential winner appended before delivery.
- P-348 remains unsettled; retrospective deferred.
- Next local slot advanced to P-349.

## 2026-09-09 — P-349 ISSUED

- Official first pitch confirmed as 11:45 AEST / 18:45 PDT.
- Final pregame freeze at 11:42:28 AEST.
- Fresh `METHOD.md` and `RULES_BASEBALL.md` read from Google Drive; Drive remained read-only.
- Mathews/Roupp official probable-starter identities confirmed.
- MLB lineup pages still showed TBD at cutoff; participant uncertainty explicitly retained and player props avoided.
- Masyn Winn's Sep 8 activation incorporated.
- Major SF/Cardinals injuries and roster moves incorporated.
- Oracle Park weather / park mechanism recorded.
- Starter small-sample branch applied to Mathews; Roupp Statcast xERA/contact profile reconciled with ERA.
- Prior 11-inning bullpen exposure recorded without using prior-game result as a predictive streak.
- Joint centre 7.70 runs and STL +0.40 separation recorded.
- P-349 appended before delivery; next slot P-350.

## 2026-09-09 — P-350 ISSUED

- Event identity confirmed as Ben Shelton vs Carlos Alcaraz, US Open men's singles quarterfinal.
- User 12:00 AEST estimate reconciled to current structured schedule 12:10 AEST.
- Final volatile refresh at 11:49:54 AEST: match remained NOT_STARTED.
- Fresh `RULES_TENNIS.md` read from Google Drive; Drive remained read-only.
- Best-of-five / hard-court / retirement-term state frozen.
- Current workload, wrist-return status, Montreal form, current US Open set counts and R4 serve performance reconciled.
- L5/L10/L15/L20 trend windows recorded without streak weighting.
- 2026 serve/return baseline and Top-10 Shelton return suppression incorporated with shrinkage.
- H2H 0-3 recorded as continuity context only.
- Explicit 3/4/5-set branch tree produced Alcaraz 76% winner, 66% 4+ sets.
- Total 38.5 and ±4.5 game handicap derived from the same score tree.
- P-350 appended before delivery; retrospective deferred.
- Next local slot advanced to P-351.

## 2026-09-09 — P-353 ISSUED

- NPB event and 19:00 AEST / 18:00 JST first pitch verified.
- Fresh Drive `RULES_BASEBALL.md` applied; NPB 2026 no-DH Central League and 12-inning tie rules recorded.
- NPB starter identity handshake: Bryan Mata vs Yudai Ohno.
- Current posted lineups and benches retrieved before issue.
- Mata Sep-9 registration / Tima deregistration recorded.
- Official team batting/pitching rates and L5/L10/L15/L20 windows recorded.
- Ohno's 0.49 2026 ERA vs Yomiuri shrunk as direct continuity evidence.
- Tokyo Dome 2026 HR/run factors reconciled rather than assuming dome = high scoring.
- Joint centre 6.03, Chunichi separation +0.53 and NPB tie branch recorded.
- Ranked four and three-way potential-winner view appended.
- Retrospective deferred; next slot P-354.

## 2026-09-09 — P-354 ISSUED
- Final cutoff 18:58:31 AEST / 17:58:31 JST, before nominal 18:00 JST start.
- SportsNavi already flagged `開始遅延` due to rain; no pitch/live score used.
- Fresh Drive METHOD and RULES_BASEBALL applied; NPB tie/no-DH rules retained.
- Official starters, posted lineups, bench, Kozono absence, Tokoda slide start, and Hiroshima relief-chain adjustment recorded.
- Koshien PF and exact venue rain/JMA warnings incorporated as event-order uncertainty, not automatic Under.
- One time-inconsistent NPB homepage rendering showing later-day finals was quarantined from prediction-time state.
- Joint centre 5.51; Hanshin separation +1.09; three-way winner/tie branch recorded.
- P-354 appended before delivery; retrospective deferred; next slot P-355.

## 2026-09-09 — P-355 ISSUED

- Official Australia Cup semi-final identity, 19:30 AEST kickoff and single-leg ET/penalty endpoint verified.
- Final state refresh at 19:15:34 AEST: structured event remained Scheduled.
- Fresh Drive METHOD, RULES_SOCCER and league-rule references applied; Drive remained read-only.
- Current Sydney full-fit availability and Victory 19-man semi-final squad refreshed.
- One secondary current lineup feed failed the participant cross-check and was quarantined; official XI/GK remained unresolved, triggering the SO-P2 side confidence cap.
- L5/L10/L15/L20 competitive windows reconstructed with Cup results treated at regulation for the 90-minute target.
- Goal centre 2.40 with 1H centre ~0.80 and explicit state-family mass recorded.
- Separate corner centre 10.86 built from team for/against rates plus direct width/block/clearance H2H evidence.
- Exact Kogarah weather/BOM conditions incorporated without forcing a wind sign.
- Five ranked rows, supplied-line probabilities, regulation winner and to-advance probabilities appended.
- Retrospective deferred; next slot P-356.

## 2026-09-09 — P-356 ISSUED

- Final pregame refresh 19:26:22 AEST / 18:26:22 KST, four minutes before scheduled first pitch.
- Fresh Drive `RULES_BASEBALL.md` applied; KBO universal-DH, 11-inning tie and no-automatic-runner state retained.
- Ko Young-pyo and Won Tae-in starter identities handshaken against current KBO/current schedule sources.
- Current Samsung batting order and Ryu Ji-hyuk knee-contusion return incorporated.
- Exact current KT Sep-9 order not independently field-owner confirmed; player props omitted and team-level mixture retained.
- Official team batting/pitching/standings and starter splits incorporated.
- L5/L10/L15/L20 reconstructed from current game logs.
- Sep8 bullpen usage incorporated without equating freshness with quality.
- Daegu exact weather gate passed; park upper-tail branch retained.
- Joint run centre 9.99, Samsung separation +0.65, KBO tie branch and 10.5 normalised edge disclosed.
- Ranked four appended before delivery; next local slot P-357.

# 7. 2026-09-10 COHORT RETROSPECTIVE SUMMARY

## 7.1 Ranked-row results and Brier diagnostics

Only **finally graded ranked rows** are included below. The three open/provisional corner rows (`P-345` R3, `P-346` R5, `P-355` R5) are excluded from W-L and Brier until their frozen settlement field is resolved.

| ID | Finalized ranked rows | W-L | Mean Brier |
|---|---:|---:|---:|
| P-345 | 4 | 2-2 | 0.2683 |
| P-346 | 4 | 4-0 | 0.0620 |
| P-347 | 4 | 2-2 | 0.2374 |
| P-348 | 4 | 1-3 | 0.2803 |
| P-349 | 4 | 4-0 | 0.1440 |
| P-350 | 4 | 3-1 | 0.2574 |
| P-351 | 4 | 2-2 | 0.2460 |
| P-352 | 4 | 3-1 | 0.2158 |
| P-353 | 4 | 2-2 | 0.2549 |
| P-354 | 4 | 2-2 | 0.2968 |
| P-355 | 4 | 3-1 | 0.1641 |
| P-356 | 4 | 3-1 | 0.2418 |
| P-357 | 4 | 2-2 | 0.3377 |
| **Cohort finalized** | **52** | **33-19** | **0.2313** |

Trivial 0.5 Brier baseline = **0.2500**. The 0.2313 cohort figure is a **descriptive diagnostic only**, not calibration, edge, value or proof of predictive superiority. The cohort mixes sports and populations and includes only 52 finalized ranked rows.

**Rank #1:** **8 W / 5 L (13 cards)**.  
**Rank #2:** **8 W / 5 L**.  
**Both Rank #1 and Rank #2 won:** **4 / 13 cards**.  
**Potential-winner calls:** **5 / 13 correct**, with `P-350`'s winner alias counted once, not as a second observation.

## 7.2 PRIMARY_SCORED local projection

The only `PRIMARY_SCORED` population represented in P-345–P-357 is **MLB** (`P-347`, `P-348`, `P-349`, `P-351`).

- New MLB ranked rows: **16**
- New MLB W-L: **9-7**
- New MLB mean Brier: **0.2269**
- Drive's pre-cohort PRIMARY_SCORED snapshot: **18 rows, 9-9, mean Brier 0.2466**
- If this local cohort is later canonicalized unchanged, projected PRIMARY_SCORED total: **34 rows, 18-16, mean Brier ≈0.2373**
- Projected MLB-only total from the Drive's prior MLB line: **24 rows, 13-11, mean Brier ≈0.2252**
- Projected PRIMARY_SCORED card count: **8**, still far below the 25-card pattern-review cadence.

These are **local reconciliation projections only**. Google Drive was not modified.

# 8. GENERAL LEARNINGS, OBSERVATIONS, AND RULE-CHANGE DECISIONS

## 8.1 Recurrent mechanism: printed kill path, insufficient branch mass

This is the strongest cross-card pattern in the cohort.

- `P-347`: Miller short-hook / HR-cluster tail was printed, yet Seattle U4.5 was 71% and game Under 7.5 remained preferred.
- `P-351`: Ohtani absence was printed, yet Dodgers TT O3.5 remained 70% and -1.5 59%.
- `P-352`: wicket-light start / “runs once set” branch was printed, yet SA U305.5 was Rank #1 at 68%.
- `P-354`: Tokoda long-start suppression was printed, yet Hanshin TT O1.5 was 74% and winner 63%.
- `P-356`: Ko's second-half command was printed, but one Sep-3 blow-up was given an equal-and-opposite signed term.
- `P-357`: Dublin's potentially elite bowling resources were explicitly named while XI unresolved, yet Belfast 150+ remained 72%.

**Decision:** this does **not** justify a new hard rule. It is repeated evidence that existing `G-L1` state-family enumeration and `G-L2` width-vs-direction requirements must be applied more strictly. The smallest operational change is to require every already-identified kill path to receive visible probability mass before a high-probability row is frozen.

**Recommended destination:** clarify implementation examples in `RULES_GENERAL.md` §16.5 and relevant sport files; log the recurrence in `LEARNING_REGISTER.md`. Do not promote a new weight.

## 8.2 Exposure-weighting matters more than scalar adjustments

Three distinct misses had the same structural shape:

- `P-351`: an elite hitter absence affected lineup PA distribution and cluster probability, not merely “-0.40 runs.”
- `P-353`: five left-handed hitters versus a LHP was treated too much like a raw count rather than PA/slot/power exposure.
- `P-356`: Ko's starter quality was not translated through expected innings/batters faced strongly enough.

**Decision:** reinforce sport-native exposure mapping (`G14`, `BB-S1`, `BB-S2`, `BB-S3`). No new rule.

## 8.3 Phase score is not resource state — cricket

`P-352` is a particularly clean lesson: **18/0 after five overs** won the first-five Under but preserved every wicket, and the innings still reached 348. A low run-rate phase cannot be passed into the full-innings distribution without wickets/batters/resources.

`P-357` shows the opposite: **43/3 after six** is not merely “43 runs”; the three wickets materially damaged the innings and it ended at 107.

**Decision:** `RULES_CRICKET.md`'s existing phase-to-innings transition control is strongly supported. Add these as worked examples if the sport file is later updated; no new control needed.

## 8.4 Early-season outcome droughts versus creation process — soccer

`P-345` shows why three games of zero goals / tiny SoT can be dangerous when the underlying team is new and shot volume remains non-zero. Villa immediately generated 21 shots and 3.00 xG in the new competition and scored three before half-time.

**Decision:** reinforce the existing soccer early-season shrinkage control. Do not create a “drought reversal” rule; the point is to separate chance creation, shot quality and finishing variance.

## 8.5 Current-event return performance versus broad priors — tennis

`P-350`'s tree correctly anticipated a long competitive match but under-allocated Shelton-win probability. His return performance was materially better than the broad Top-10 return prior implied.

**Decision:** add a candidate observation to compare current-event break creation/return pressure against broad season/top-opponent priors before setting a Slam winner branch. Exploratory evidence only.

## 8.6 Territory does not equal finishing quality — soccer

`P-355`: Sydney controlled long spells yet lost 0–2 and current post-match displays report zero shots on target. This is consistent with the existing separation between possession/territory, shot creation and conversion.

**Decision:** no new rule; retain as a mechanism example.

## 8.7 Distance-to-line watch strengthened

Near-boundary outcomes in this batch include:
- `P-347` Seattle U4.5 **lost by 0.5 run**.
- `P-348` Toronto O3.5 **won by 0.5 run**.
- `P-348` Athletics +1.5 **lost by 0.5 run**.
- `P-354` Hiroshima U3.5 **won by 0.5 run**.
- `P-355` provisional corner Over 8.5 would win by exactly **0.5 corner** if 5–4 is field-owner confirmed.

**Decision:** append to the existing distance-to-line candidate watch. Do not convert boundary frequency into a directional rule.

## 8.8 Potential-winner calls were weak in this cohort

Only **5 of 13** potential-winner calls were correct. Several cards were much better at protected sides or totals than outright winner allocation (`P-349`, `P-353`, `P-354`, `P-356`).

**Decision:** observation only. Do **not** conclude that winner markets should be systematically downgraded from one mixed/exploratory cohort. Review again only at the prescribed population cadence.

## 8.9 Rule changes promoted this pass

**None.**

Reason: `L-087` prohibits converting same-session retrospective observations into predictive weights/ordinal rules without prospective evidence. Existing controls explain the principal failures. The PRIMARY_SCORED card count remains well below the 25-card pattern-review trigger.

# 9. SOURCE ADDITIONS / SOURCE-QUALITY OBSERVATIONS

| Source / lane | Evidence from this pass | Proposed status if Drive is later updated | Destination |
|---|---|---|---|
| MLB official Film Room / Stories | Clean final, innings, starter line and scoring sequence for P-347/P-348/P-349/P-351 | **FIELD-OWNER / PREFERRED MLB settlement lane** if not already registered | `SOURCES.md`, `DATA_SOURCE_REGISTER.md` |
| NPB English BIS (`npb.jp/bis/eng`) | Complete official boxes for P-353/P-354 incl. innings, HR, pitcher lines | **FIELD-OWNER / PREFERRED NPB settlement lane** | `SOURCES.md` |
| KBO English Scoreboard | Official P-356 final and inning table | **FIELD-OWNER / PREFERRED KBO settlement lane** | `SOURCES.md` |
| USOpen.org official reports | Exact set scores, duration and break-point facts for P-350 | **FIELD-OWNER / PREFERRED tennis final lane** | `SOURCES.md` |
| Cricket Ireland-branded CricketArchive path | Full ETPL P-357 scorecard, toss, officials, innings detail | **CANDIDATE — verify ownership/upstream lineage before promotion** | `DATA_SOURCE_REGISTER.md`, `SOURCES.md` |
| ETPL official event shell / NV Play | Official page names live-scoring provider but remained crawl-stale as `UPCOMING` after final | **Provider-lineage clue, not settlement final by itself** | `DATA_SOURCE_REGISTER.md` |
| Opta Analyst match centre | Strong post-match UCL process stats, but iframe hides some derivative fields from this tool | **High-quality process source; derivative reachability needs explicit test** | `SOURCES.md` |
| Guardian / VI UCL stats | P-345 corner field conflicts 4 vs 3 | **Cross-check only when threshold could flip; never auto-settle conflict** | `SOURCES.md` |
| TotalCorner / general secondary soccer displays | P-355 5–4 corner count agreement but not frozen provider | **Secondary/provisional only** | `DATA_SOURCE_REGISTER.md` |

**Important source rule reinforced:** a formally “official” event shell can be stale, while a detailed scorecard can be current. Source authority and **current field correctness** must both be checked. Conversely, two secondary displays can agree because they share an upstream feed; agreement alone does not establish independence.

# 10. DRIVE-INHERITED OPEN ROWS — 2026-09-10 FRESH MAXIMUM RECHECK

Fresh Drive status reconciliation found **11 pre-existing open rows** across Parts 2 and 3. A new settlement search was attempted. **No additional row reached the frozen field-owner standard in this pass**, so no historical W/L was fabricated and no Drive file was edited.

| Tracking ID | Canonical row | Frozen open field | 2026-09-10 disposition |
|---|---|---|---|
| `TMP-OPEN-20260909-01` | `P-341-C03` | Over 7.5 total corners | **UNCHANGED — UNSETTLEABLE to frozen field-owner standard** |
| `TMP-OPEN-20260909-02` | `P-342-C03` | Over 8.5 total corners | **UNCHANGED — PROVISIONAL RESEARCH WIN (16 reported), no frozen provider** |
| `TMP-OPEN-20260909-03` | `P-126` | event identity + O7.5 corners | **UNCHANGED — IDENTITY_STATE_CONFLICT / UNRESOLVED** |
| `TMP-OPEN-20260909-04` | `P-148-C02` | Toluca team corners | **UNCHANGED — PROVISIONAL LOSS** |
| `TMP-OPEN-20260909-05` | `P-149-C02` | Ventura team corners | **UNCHANGED — PROVISIONAL WIN** |
| `TMP-OPEN-20260909-06` | `P-176-C05` | Amiens–Versailles U10.5 corners | **UNCHANGED — PROVISIONAL WIN; prior 5–3 = 8 evidence remains best available** |
| `TMP-OPEN-20260909-07` | `P-178-C05` | Cannes–Le Puy U10.5 corners | **UNCHANGED — PROVISIONAL LOSS; prior 8–8 = 16 evidence remains best available** |
| `TMP-OPEN-20260909-08` | `P-179-C05` | Thionville–Paris 13 U10.5 corners | **UNCHANGED — PROVISIONAL WIN (8–1 = 9 reported)** |
| `TMP-OPEN-20260909-09` | `P-233` | Beijing–Lanzhou O8.5 corners | **UNCHANGED — PROVISIONAL WIN (13 secondary)** |
| `TMP-OPEN-20260909-10` | `P-234-C03` | Dalian–Shenhua O8.5 corners | **UNCHANGED — PROVISIONAL WIN (10 secondary; disrupted match)** |
| `TMP-OPEN-20260909-11` | `P-235` | Shandong–Shanghai Port O8.5 corners | **UNCHANGED — PROVISIONAL WIN (14 secondary)** |

These remain in their original canonical custody. This mini-log records the fresh recheck for visibility only.

# 11. CANONICAL-ID RECONCILIATION / TEMPORARY-ID DECISION

Fresh Drive state at the beginning of this pass:

- `PREDICTION_LOG_COMBINED_3.md` contains canonical `P-333`–`P-344`.
- Drive's **Next canonical ID = P-345**.
- The uploaded local continuation is exactly `P-345`–`P-357`.

**Conclusion:** there is **no current canonical-ID collision**, so **no newly settled whole-card record receives a temporary replacement ID**.

The three `TMP-OPEN-20260910-01`…`-03` labels above are **derivative-field tracking handles only**, not replacement prediction IDs. If Drive's canonical ledger changes before a future import/reconciliation, the canonical range must be re-read at that future time; only then should a conflicting whole card be assigned a temporary reconciliation ID.

# 12. WHERE THESE UPDATES SHOULD GO IF THE DRIVE IS LATER CANONICALIZED

No Drive changes are implemented in this pass. No new Markdown document is required.

| Material | Existing destination |
|---|---|
| P-345–P-357 forecast text + settlement/retrospective addenda | `PREDICTION_LOG_COMBINED_3.md` |
| Current per-ID status / open derivative handles | `GAME_LOG_STATUS_INDEX_2026-09-05.md` (or its current successor if renamed) |
| Recurrent retrospective observations / candidates | `LEARNING_REGISTER.md` |
| Any actually promoted controls after prospective evidence | `CONTROLS.md` + relevant `RULES_<SPORT>.md` |
| Baseball exposure / starter / lineup examples | `RULES_BASEBALL.md` |
| Cricket phase-resource and unresolved-XI examples | `RULES_CRICKET.md` |
| Soccer early-drought / territory-quality examples | `RULES_SOCCER.md` |
| Tennis current-event return-regime observation | `RULES_TENNIS.md` |
| New/changed settlement lanes and provider lineage | `SOURCES.md` + `DATA_SOURCE_REGISTER.md` |
| Running Brier/calibration snapshot | active canonical log's controlling snapshot |

**No new MD file is necessary:** the existing governance, learning, source and sport-rule documents have clear homes for every finding above.

# 13. APPEND-ONLY CHANGELOG — SETTLEMENT PASS

## 2026-09-10 — P-345–P-357 settlement / retrospective audit

- Fresh Drive canonical state reconciled: P-333–P-344 occupied; next canonical P-345; **no collision** with this continuation.
- All thirteen parent events verified FINAL.
- All ordinary score/side/total rows settled.
- Three derivative corner rows retained open/provisional rather than forcing a grade.
- Three-question retrospective completed for every card.
- Deep review completed wherever Rank #1 lost or multiple ranked rows lost.
- 52 finalized ranked rows: **33 W / 19 L**, mean Brier **0.2313**.
- PRIMARY_SCORED MLB subset: **9 W / 7 L**, mean Brier **0.2269**.
- Eleven pre-existing Drive open rows rechecked; **no new field-owner resolution** this pass.
- No new hard rule promoted under the `L-087` firewall.
- Source-register additions and recommended destination files recorded above.
- Google Drive remained **READ ONLY** throughout.

# 14. LOCAL ARTIFACT INTEGRITY

- Source file: `PREDICTION_MINI_RUNNING_LOG_P357(1).md`
- Source SHA-256: `330b74a626748aecade8abf02c76f10412158fb0d2cd60af8a56585db533285b`
- Updated file: `PREDICTION_MINI_RUNNING_LOG_P357_RETROSPECTIVE_SETTLED_2026-09-10.md`
- Updated-content SHA-256 before this integrity footer: `83a58623ac31efe264b22bb8ff6246a1aeb24bcbaf8be6f736e8c9af61ff431e`
- Drive mutation: **NONE**
- Canonical-ID collision at audit time: **NONE**
