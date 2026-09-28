# Basketball analysis rules — dated history to 2026-09-28

**Archived 2026-09-28 (md-only restructure).** These are the dated sections that followed the competition-rules section of `RULES_BASKETBALL.md`, moved verbatim. They are the evidence record. The live rules are §0 of `RULES_BASKETBALL.md`, and nothing here reinstates a rule that §0 or `CURRENT_RULES.md` §I withdraws.

## September 5 settlement learning — prospective SFA amendment


At possession/shot-mix, availability and G20.1 terminal-allocation steps, separate (a) opponent scoring suppression, (b) favourite scoring opportunities and (c) margin continuation/compression. Injury to a rim protector can improve the opponent's paint efficiency without proving a low team total for the injured player's team. Map replacement minutes and perimeter volume; do not import world rank or raw warm-up scores as a possession forecast.


P-284 had Under plus USA cover; China's +29.5 failed even at 61 points. At USA 94, the China-cover boundary is 65 and the Under boundary 67. Use exact algebra rather than “below 60” as the only cover-failure path. Bench participation does not imply margin compression: last-quarter scoring belongs to both teams.


P-285's printed score families all had Nigeria ahead despite a Korean scoring/upset route in prose. Both teams must have contract-evaluable ordinary win/separation branches when supported, under L-070. Record three-point **attempt volume and conversion** separately; do not infer fast pace solely from the final 180 or treat FIBA efficiency 31 as 31 points. Candidate C-P293-BK-ALLOCATION remains untested; no national-team or injury coefficient changes.




Full evidence and frozen-card comparisons: [September 5 audit](archive/audit_documents_implemented_2026-09-25/COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md).


## September 5(b) settlement learning — P-294–P-305 second continuation


Two FIBA Women's World Cup group-stage cards settled this pass with opposite outcomes from opposite framings, plus one AFLW-style large-cushion confirmation carried over from `RULES_AFL.md`'s own cohort (`P-293` Gold Coast +13.5).


**`P-299` (Mali vs Spain) — major upset; L-076.** Mali won 82-73, outscoring Spain 31-19 in the third quarter — the exact mechanism ("Mali's elite offensive rebounding and Koné/Sangaré/N'Diaye interior/creation keep Spain from finishing defensive possessions and compress the margin") the card itself had named as Spain -25.5's kill path. The reference corridor was still anchored close to Spain's Aug 29 friendly win margin (97-58, a 39-point win) despite the card explicitly recording that Spain were missing five eventual rotation players in that friendly and that **Sika Koné, Mali's best player, did not appear in the friendly's box score at all**. **New rule:** an exhibition/preparation-game margin must be excluded from anchoring the reference corridor whenever either side's core rotation is confirmed absent by name from that exhibition; a same-tournament data point for the affected team's current full roster (here, Mali's competitive 97-102 near-upset of Japan in the tournament opener, already on record) must be weighted above the stale friendly.


**`P-303` (Nigeria vs Hungary) — clean top-two win.** Nigeria won 81-53, landing almost exactly inside the card's own stated 136-149 total corridor and 72-78/64-71 team corridors. The card used a conservative framing — backing the stronger, higher-ranked side's floor via a +25.5 cushion rather than an aggressive spread-cover on the favourite — and both the cushion and the Under total won.


**Cross-card contrast — new candidate `C-PL15-BSK-CUSHION-VS-SPREAD`.** In the same session, three large-cushion "team getting points" rows were issued (`P-293` Gold Coast +13.5, `P-299` Mali +25.5, `P-303` Nigeria +25.5) and all three covered, while the one large-favourite-spread row issued (`P-299` Spain -25.5) lost. This is a three-and-one same-session sample, tracked as a candidate only — no automatic preference for cushion framing over spread framing is adopted from it, but it is a specific, falsifiable pattern worth testing prospectively per LEARNING_REGISTER.md.


**Kill-path library addition (§8.5):**


| Kill path | Defeats | Evidence origin |
|---|---|---|
| Either side's confirmed core-rotation absence from a cited preparation/exhibition game | A reference corridor anchored to that exhibition's margin | `P-299`; L-076 |
| A same-tournament data point for the affected team's current full roster outweighing a stale core-absent friendly | The same anchoring error, from the opposite evidentiary direction | `P-299`; L-076 |


Full evidence: [PREDICTION_LOG_COMBINED_2.md, 2026-09-05(b) section](PREDICTION_LOG_COMBINED_2.md#component-import--p-294p-305-second-continuation--2026-09-05b).


## September 6 settlement learning — the pace × efficiency tail, worked on both sides


`P-299` and `P-303` were issued the same day, in the same competition, with structurally identical slates — a large handicap at Rank #1 or #2 and a full-game total alongside it. One failed on both top rows; the other won both. Under `G20.2` they separate cleanly, and the separation is arithmetic that was available before either tip-off.


| Card | Line | Actual total | Tail-budget position |
|---|---|---|---|
| `P-299` Mali (W) v Spain (W) | `Under 144.5` (rank #2) | **155** | Spain's plausible upper output plus Mali's median lands essentially **on** the actual 155 — the row was `TAIL_EXPOSED` and the card had no mechanism sentence for why that combination could not recur |
| `P-303` Nigeria (W) v Hungary (W) | `Under 145.5` (rank #2) | **134** | Both sides' central outputs sat comfortably below the line with room to spare — not `TAIL_EXPOSED` |


**Required from now on, `SFA-BASKETBALL`:** the tail budget is computed as **pace × efficiency at the upper decile**, expressed in points, not possessions. Take each side's second-highest L10 possessions figure `Poss` and its second-highest L10 offensive rating `ORtg` (points per 100 possessions), and compute `points = Poss × ORtg / 100` — **the /100 normalisation is required and was omitted in the original wording (correction, 2026-09-06(d))**; without it the units do not resolve to points. Hold the opponent at its median defensive rating for the symmetric term. Print the implied total. **`TAIL_EXPOSED` is disclosure only per `RULES_GENERAL.md` §15 — the prior hard bar ("may not be Rank #1") is withdrawn and reclassified as `CANDIDATE`, pending its own prospective test.**


`P-299` also remains the origin case for `L-076` — a 39-point preparation-game margin against a Mali side missing five of its eventual finalists anchored the corridor. The tail budget and `L-076` are complementary: `L-076` says the anchor was wrong, `G20.2` says the anchor was also never stress-tested against Spain's own upper output.


### Kill-path library addition (§8.5)


| Kill path | Defeats | Evidence origin |
|---|---|---|
| **Upper-decile pace blowout** — the favourite's own high-tempo mode clears the total on its own, regardless of the underdog's scoring | A full-game `Under` ranked on the underdog's low offensive rating | `P-299` (155 against `Under 144.5`) |
| **Quarter-level regime break** — one quarter's swing (Mali 31-19 in Q3) inverts both the handicap and the winner in a single ten-minute window | A large handicap justified by season-long ratings without a quarter-level variance term | `P-299` — reinforces `L-070` |




### Cross-sport gates instantiated here (v3.7)


| Gate | Sport-native instantiation |
|---|---|
| `G10.2` settlement-source pre-registration | FIBA, WNBA and NBA events settle from the competition's official box score; ESPN's `basketball/<league>/summary` is the structured corroboration lane. LNBP and comparable leagues need their own named endpoint per `SRC-BB-LNBP-OFFICIAL`. |
| `G14.2` coaching / bench / rotation record | Record the head coach, the confirmed inactive list, and the rotation depth (how many bench players average ≥15 minutes across the L10). Where official feeds are `LINEUPS_NOT_YET_PUBLISHED`, shootaround line combinations and scratch reports verified across accredited beat reporters or official team media releases under Control `S-1 Rev 2` qualify as `PROJECTED_BEAT_VERIFIED`, satisfy `G14.2` personnel modeling, and do not block Rank #1. International tournaments rotate heavily in group play — record the qualification state as a rotation signal. |
| `G20.2` distributional tail audit | Derive tail and boundary mass from the **same frozen basketball joint score distribution**: possessions/opportunity, minutes and usage mixtures, lineup state, shot mix/efficiency with shrinkage and uncertainty, rebounding/turnovers, fouls/bonus, garbage-time and overtime branches. Historical second-highest/median or hand-built upper-decile stress sums are superseded as active ranking gates. |
| `G21.1` exact target geometry | Map every supplied total/phase-total to its exact settlement event and derive WIN/PUSH/LOSS (plus void/censoring where applicable) from the same frozen sport-native PMF/CDF or coherent branch mixture. Historical path-count/category labels have no mandatory ordinal effect and are not a substitute for the distribution. |
| `G26.1` no universal separation floor | Print any relevant reference base rate and `rank_gap` descriptively. **No 40–60% or other pooled probability band can disqualify Rank #1.** Rank by exact marginal likelihood from the frozen joint distribution plus robustness/evidence uncertainty; precise probabilities require the validated-model gate. |


**Pre-issue checklist additions (this sport):** settlement endpoint named per row; coaching/bench/rotation record for both sides with missingness codes; tail-budget sums printed against every total line; path-geometry class and `N` printed for every total and phase-total row; separation-floor result stated for Rank #1.


Full narrative and evidence: [`archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md`](archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md). Controlling gate text: [`RULES_GENERAL.md` §13](RULES_GENERAL.md).


## September 5 implementation after freeze confirmation


**ACTIVE REQUIRED PROCESS — MDS-2026.09.05-v3.6 / L-068–L-072.** Build both teams’ scoring allocation from available possessions, shot opportunities/quality and rotations. Include each side’s supported win/separation branch and late-quarter allocation. A missing player changes supported role/exposure inputs; it does not by itself justify an opponent scoring ceiling or a pace claim.


At final delivery, record the preferred total direction for each exact target, the strongest evidenced failure path for ranks #1 and #2, and whether both can win under the stated joint scenario. Rank by supported marginal likelihood; do not promote an opposite pick solely to manufacture one O/U win. At settlement, keep all issued wins/losses, including defective reasoning, in the applicable historical scorecard and review failed #1/#2 and preferred totals.


[Eligibility policy](PERFORMANCE_ELIGIBILITY_POLICY.md): non-live history is user-confirmed frozen pre-game; explicit live-issued views stay separate. These process repairs are implemented now. Numerical weights and predictive-lift claims need a later frozen comparison; historical origin games do not supply those completions.


## 2026-09-06(f) — settlement and retrospective addendum


P-299 roster labels are team-specific: Spain lacked five eventual Spain rotation players in the friendly, with Mali’s Koné separately absent. Reconcile current competitive evidence with the reference corridor; no universal zero-weight-for-friendlies rule is inferred. P-303 winning cushion/Under still missed both team-score corridors, total corridor and margin corridor. Audit winners as rigorously as losers; no automatic cushion preference.


Full frozen ranks, actual drivers, knowability and smallest fixes: [PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md). Reinforcement only; METHOD v4.0 remains controlling and no new predictive weighting is promoted.


## 2026-09-09 settlement learning — P-334 (no forecast), P-344


`P-334` (Germany 83–58 Mali) was an administrative no-forecast closure — live-state gate failed after tip; a draft ranking existed but was not delivered. No retrospective model weight from an unpublished draft (`L-117`).


**`P-344` — Hungary 84–63 Japan (FIBA W World Cup, Qualification to QF) — deep Rank-#1 retro.** Frozen card: R1 `Japan +3.0` (p0.56 win), R2 `Over 146.5` (p0.54), R3 `Under 146.5` (p0.46), R4 `Hungary -3.0` (p0.37 win); potential winner Hungary (54%). Result: **Hungary +21, total 147.** Rank #1 lost by a large margin; `Over 146.5` survived by 0.5 (a boundary escape, not validation of the 149.5 centre); potential winner correct.


*What went right:* the size/rebounding mismatch (Hungary 43.7 RPG vs Japan 31.7; paint edge through Juhász + Takács-Kiss) was correctly identified as the foundation, and Hungary was correctly the likelier winner (control 11, control 12).


*What went wrong — corrected on second-pass research (2026-09-09).* The first reading called Lelik's 23 points an under-weighted "breakout". Opening the FIBA official player profiles — **already listed in the card's own source register** — shows it was not a breakout at all, and that the real failure was a **participant-exposure retrieval gap**:


| Hungary scorer, pregame (3 group games) | PPG | Minutes | In the card as… |
|---|---:|---:|---|
| Dorka Juhász | 17.0 | — | quantified line |
| Virág Takács-Kiss | 13.0 | — | quantified line |
| **Réka Lelik** | **8.7** (8 / 14 / 4) | **~26.3** | **an unquantified name** |


Lelik was Hungary's **third-highest scorer**, playing starter-level minutes, with 4.3 RPG and 3.5 APG, and a pregame range that already included a 14-point game. The card printed quantified exposure for the two players above her and carried the third as a bare name in a list. **A blowout requires a third scorer, and the card's margin distribution contained no third scorer with a number in it** — which is mechanically why a symmetric ±10–12-point width around Hungary +0.5 was the output. Her 23 was an upside game (~2.6× her pregame mean), not a black swan; FIBA's own framing of Hungary as a "Twin Towers" side is precisely the shape that transfers usage to a third option when the defence collapses inside.


Two further items: Japan's perimeter *floor* was set by 11.1% and 23.3% three-point shooting in its two European group losses, not by a tournament average inflated by a record 20-three game against Mali. And Saki Hayashi's 9th-minute broken arm (8 minutes played) was a genuine in-game shock, **not** a pregame model miss (`L-117`) — it does not excuse the separately underweighted Hungary separation branch.


This is an instance of the cross-sport retrieval gate **`RULES_GENERAL.md` §16.5(c) / `G-L7`**: an aggregate ("the leaders are A, B, C and D") stood in for a per-player record that was available and would have changed the margin width.


### Structural control additions


20. **Quantify every rotation-level scorer, not just the two most-cited names.** `BK-S1` already requires expected minutes and usage "for every decision-driving player"; this control fixes the threshold so it cannot be satisfied by a leaders list. **Print a quantified exposure line — PPG, minutes, rebounds, assists over the retrieved window — for every player above roughly 20 minutes a game or in the team's top three scorers, on both sides.** A player carried as a bare name inside a phrase like "the leaders include A, B, C and D" is `AGGREGATE_ONLY` and the margin/total rows that depend on the team's scoring ceiling are capped (`RULES_GENERAL.md` §16.5(c)). *Origin:* `P-344` — Hungary's third-highest scorer (8.7 PPG on ~26 minutes) was the only one of the top three without a number on the card; she scored 23 and the margin distribution had no room for her.


21. **Secondary-scorer usage transfer in a mismatch.** When one team holds a clear structural advantage (size/rebounding/pace) and the opponent's defence must key on the favourite's primary option(s), model an explicit branch in which a **secondary or tertiary scorer** absorbs that usage and produces the blowout. A "twin towers"/interior-dominance identity is exactly the shape that transfers usage outward when the paint is collapsed on. Conversely, when the opponent's offence depends on volatile perimeter shooting, its **floor is set by its worst recent same-regime shooting games, not by a tournament average** inflated by one outlier game — `P-344`: Japan's 11.1% and 23.3% three-point games against European opposition were the relevant floor, not the average that included a record 20-three game against Mali. Carry both into the total and margin distribution.


### Applying G-L1 / G-L4 here


- **`RULES_GENERAL.md` §16.5(a) / `G-L1`:** the joint game object must enumerate the **margin families** (favourite blowout 15+, clear win 6–14, close 1–5 or push, underdog win) with explicit mass, and the **total families**, and place every §8.5 kill path as a weighted branch. A representative Rank-#1 final score is written and checked against the spread, the total and any team-total line. `P-344`'s symmetric ±10–12 width around +0.5 would not have survived this: the size mismatch plus Japan's perimeter volatility puts material mass on a 15+ Hungary margin.
- **`G-L4`:** winner and spread are separate answers from the same family set. A correct winner call with a badly compressed margin distribution (`P-344`) is a **margin-model failure**, recorded as such — not a partial success because the winner was right.


### Kill-path library addition (§8.5)


| Kill path | Defeats | Evidence origin |
|---|---|---|
| A secondary/tertiary scorer absorbing usage for a blowout while the defence keys on the primary star(s) — **especially one already in the team's top three who was carried on the card as a name without a number** | An underdog `+handicap` or an `Under` ranked on a compressed cross-opponent margin centre | `P-344` (Lelik, 8.7 PPG / ~26 min pregame → 23 points); controls 20, 21, 11; `G-L7` |
| An opponent's volatile perimeter offence reverting to its worst recent same-regime shooting rather than its tournament average | An `Over` or an underdog `+handicap` built on the opponent's average scoring | `P-344` (Japan 11.1% / 23.3% vs Europe, average inflated by a 20-three outlier); control 21 |


### Pre-issue checklist additions (this sport)


- **Quantified exposure line printed for every top-three scorer and every ~20+ minute player on both sides** (control 20); any such player left as a bare name is recorded `AGGREGATE_ONLY` and the dependent margin/total rows are capped.
- **Margin-family enumeration with explicit mass** — favourite blowout (15+), clear win (6–14), close (1–5 / push), underdog win — plus the total-family enumeration, with every §8.5 kill path placed as a weighted branch (`RULES_GENERAL.md` §16.5(a) / **`G-L1`**).
- **G-L2:** State the prior and scenario probabilities. Symmetric uncertainty around an unchanged prior affects width; hierarchical shrinkage or asymmetric scenarios may change both mean and variance. Regenerate all dependent probabilities; unsupported directional adjustments remain prohibited. SCORING_AND_VALIDATION section 5 controls.
- **G-L8:** Derive each total/spread probability from the exact joint PMF/CDF and settlement endpoint, with push mass. Absolute normalised distance does not order probabilities across different distributions. No missing width or realised result justifies an invented probability.
- Representative Rank-#1 final score written and checked against the spread, the total and any team-total line.


## 2026-09-11 settlement learning — `P-358`, `P-359`, `P-360`, `P-367`, `P-371`


Five FIBA and Asian Games cards ([`PREDICTION_LOG_COMBINED_3.md` §"2026-09-11"](PREDICTION_LOG_COMBINED_3.md)). Rank #1 **3 W / 2 L** (`P-358`, `P-371` lost). Top two both won only on `P-367`. Winners 3 / 5. The preferred total was an **Under on all five cards: 2 W / 3 L.** None of the five printed a numeric width, a normalised edge or a margin-family table, although the issuing session had declared `G-L8` and `G-L2` in force. Learning-only; no fitted weight or ordinal bar (`L-087`).


### Measured precision — six cards (incl. `P-344`)


| Card | Stated total centre | Actual | Error | Stated margin centre | Actual margin |
|---|---:|---:|---:|---|---|
| `P-344` | 149.5 | 147 | −2.5 | HUN +0.5 | HUN +21 |
| `P-358` | 137 | 147 | +10 | CHN +7 | CHN +3 |
| `P-359` | 156 | 163 | +7 | JOR +6 | **TPE +3** |
| `P-360` | 155 | 148 | −7 | KOR +11 | KOR +16 |
| `P-367` | 152 | 151 | −1 | FRA +26 | FRA +29 |
| `P-371` | 144 | 167 | +23 | BEL +10 | **GER +19** |


Total error: mean **+4.9**, mean absolute **8.4** points. The three total misses all came in **competitive or upset** games (`P-358`, `P-359`, `P-371`); the two hits came in favourite separations (`P-360`, `P-367`). That is the coupling written up as control 24. Six cards is a watch item, not a bias estimate.


### What went right (keep it)


- **`P-367` is the model:** centre 89–63 against an actual 90–61, derived from rest asymmetry, pressure and turnovers. France won by 29 while shooting *worse* than China (FG 44% v 46%; 3P 37.8% v 43.8%) — the possession-volume mechanism, correctly identified.
- **Availability research that mattered:** An Youngjun out and Choi Junyong not yet with the Korea squad (`P-360`, Korean-language sources, `L-067`); Li Yueru's passport absence from the China roster (`P-367`); a secondary preview's "full-strength rosters" claim correctly overridden.
- The margin read in `P-358` (Puerto Rico's pressure against China's turnovers) and in `P-359` (Chinese Taipei's guard core) was right — the cushions won.


### What went wrong, linked to earlier lessons


1. **Observed top-two splits (`P-358`, `P-359`, `P-360`); dependence not established.** Exactly one of the top two won on each card. Extends controls 11 and 15. → **control 24**; `RULES_GENERAL.md` §16.5(f).
2. **Small-sample shooting treated as direction (`P-371`, and `P-358` in reverse).** A three-game three-point gap (38.1% v 25.2%) was a Belgian mechanism — the later 1.7-SE calculation used unsupported equal attempt assumptions and is withdrawn — and reversed. Puerto Rico's cold 25.9% was used as a floor under the Under; they shot 38.9%. Repeats `G-L2` and control 21. → **control 22**; §16.5(g).
3. **Control 20 broken two days after adoption (`P-358`).** Puerto Rico's leaders were carried as names without numbers. Trinity San Antonio's 35 points came on a pre-game line of about **9.0 PPG** (derived from her 15.5 average over four games) — an aleatory magnitude (`G-L6`) — but her 5.0 steals a game was exactly the transition route that fed the Over.
4. **No underdog-separation family (`P-371`).** Four German mechanisms were listed; every German-positive branch was a close game; Germany won by 19. → **control 23**.
5. **No widths or normalised edges on any card** (`G-L8` declared, not executed). → `RULES_GENERAL.md` §16.8.


### Structural control additions


22. **Shooting uncertainty with actual denominators (corrected 2026-09-12).** Print attempts, makes, minutes and opponent/time windows for 2P/3P/FT inputs. Use a suitable interval and explicit prior/shrinkage sensitivity; do not invent n, assume identical shrinkage in both directions, or use a two-SE cutoff as proof of noise. Unknown attempts stay unknown. A worst observed game is not a physical lower bound. See corrected G-L11 and section 16.9.


23. **Spread family including either team separating.** Use exhaustive nonoverlapping margin ranges with explicit mass, respecting draw/OT conventions. Include a plausible underdog-separation state whenever the current evidence permits it; no arbitrary two-mechanism threshold or independence claim is required. Named rebounding, bench, crowd and rest factors may overlap. Representative scorelines cannot determine branch probabilities. P-371 and P-242 motivate this disclosure, not a fitted mass.


24. **Conditional margin-total coupling (corrected 2026-09-12).** Late fouls, rotation and transition can connect margin and total, but their signs depend on the matchup and realized scoring process. Close games can be low scoring; separation can be high scoring. Compute joint probability from one model or state JOINT_UNQUANTIFIED with bounds. Do not label underdog cushion plus Under intrinsically anti-coupled or infer correlation from a few split results. See corrected G-L10.


### Kill-path library additions (§8.5)


| Kill path | Defeats | Origin |
|---|---|---|
| A competitive underdog (the state that wins its cushion) lifting the total through late possessions, fouls and its own transition scoring | An Under paired with the underdog's handicap | `P-358`, `P-359`; control 24 |
| A small-sample shooting gap reverting on the night | A spread or total leaning on tournament 3P% over ≤4 games | `P-371`, `P-358`; control 22 |
| An underdog with two or more current mechanisms separating, not merely covering | A favourite spread whose family set has no "underdog by 7+" branch | `P-371`; control 23 |
| An unquantified secondary scorer or ball-pressure guard producing a ceiling game | An Under built on the opponent's average scoring | `P-358` (San Antonio); controls 20, 21 |


### Pre-issue checklist additions (this sport)


- Attempts and binomial standard error printed beside every tournament shooting rate that carries direction (control 22).
- Margin families per control 23, with mass; the "underdog by 7+" family populated when the underdog has two or more current mechanisms.
- `P(R1 ∧ R2)` and the coupling sign for any handicap + total pair (control 24, `G-L10`).
- Numeric width and normalised edge on every total and spread (§16.8 item 3).
- Quantified exposure line for every top-three / 20-minute player on both sides — no bare names (control 20).




## 2026-09-12 algorithm corrections and retrospective integration


Control 24 is corrected: a close game can add late fouls but can also have slow pace; separation can arise from either excellent offence or suppressed opposition. Derive dependence from joint possessions, efficiency, rotation and foul states. No fixed cushion-plus-Under sign. In P-371 the frozen tournament sample was Belgium three games versus Germany four; actual attempt denominators were not captured. Withdraw the equal-75-attempt/1.7-SE and mostly-noise claim. Keep shooting reversals as observations and sensitivity hypotheses. Record both starting fives separately from the twelve-player eligible rosters and coaches. Germany won each quarter but did not lead throughout.


For every supplied row, use exact target probabilities from a coherent joint distribution; handle push/void/censoring explicitly, avoid overlapping adverse-state counts, and report JOINT_UNQUANTIFIED with bounds if the dependence is not specified. Separate issued-time participant capture, later recovered evidence, source accuracy by field, observed mechanism, and unverified causal interpretation. Keep one preferred O/U direction per distinct target and report the top-two denominator honestly. Shared correction and methodology sources (`audit_2026-09-12/rule_corrections.md`, not present in this repository). All current log observations remain learning-only and not performance-eligible.




## 2026-09-15(b) settlement learning — `P-373`–`P-423` import


Learning-only; disclosure/process changes only — no coefficient or ordinal bar (`L-087`). Evidence and tables: [`PREDICTION_LOG_COMBINED_3.md` §"2026-09-15(b)"](PREDICTION_LOG_COMBINED_3.md). Cross-sport rule: `RULES_GENERAL.md` §16.10 (`G-L12` margin centre/width; fixture identity; official-record derivative settlement).


**Cards:** P-378 (Philippines v Bahrain — Under 163.5 and Bahrain −9.5 lost; late-added Oftana scored 31), P-411 (Spain 81–58 Germany — Germany +6.5 LOST, Under 147.5 WIN, winner Spain correct).


### What went wrong, linked to earlier lessons
1. **P-411 discarded current evidence.** The same-competition, same-roster meeting ten days earlier (Spain 83–53) was set aside as an extreme-shooting outlier and the margin centred at Spain +5.2. Spain won by 23 with a Q4 of 20–7. "Spain pressure recreates the opener's separation" was the card's first kill path.
2. **P-378:** a late-added high-usage player without a minutes/usage mixture (reinforces control 21).
3. **`C-UNDERDOG-SEPARATION` direction challenged.** It assumed underdog states were under-weighted (P-358, P-359, P-371); P-411 is a favourite-separation miss. Generalised to `C-MARGIN-TAIL-MASS` (both tails) — `LEARNING_REGISTER.md` §"2026-09-15(b)".


### Structural control additions
25. **A same-competition, same-roster meeting is current evidence.** Decompose it (shooting luck v possessions, turnovers, rebounds) and give the separation family explicit mass; do not discard it as an outlier (`G-L7`, `G-L12`). Origin P-411.


## 2026-09-16 — external variant C′ reconciliation (`P-411`)


Learning-only; cross-sport rules in `RULES_GENERAL.md` §16.11.


**Control 25 worked example (adopted from C′; no new control).** Before shrinking a same-tournament blowout's margin, print a **repeatable-v-variance table**, and move the prior margin only by the variance share:
- **(a) repeatable:** turnover creation, rim and paint attempts, offensive rebounding, matchup size;
- **(b) variance:** 3P% and FT% gaps, opponent illness and absences.


P-411's rematch reproduced the separation (Spain +23 after +30).


**`G-L15`.** P-411's Under 147.5 was the preferred side of a forced pair and won. Across `P-345`–`P-423`, basketball forced-pair preferred sides went 3 of 6 — a coin flip, consistent with the §"2026-09-11" centre-error measurements.


**Disruption facts (§16.11(o)).** Record player ejections, injury exits and illness withdrawals with the quarter and the score at that time.


## 2026-09-17 settlement learning — `P-427` (BCL qualification) — **Rank #1 LOSS**


Learning-only (`L-087`). Cross-sport rule: `RULES_GENERAL.md` §16.12(a) (`G-L17`). Evidence: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17"](PREDICTION_LOG_COMBINED_4.md).


**What happened.** Kolossos +2.5 (0.61) and Under 162.5 (0.58) were the top two, declared "mildly positively coupled" with `P(R1 ∧ R2) ≈ 39%`. Kolossos led 70–66 after three quarters — the central thesis was sound — and then Körfez won the fourth quarter **25–9** with 12/24 from three. The single state broke the cushion **and** lifted the game to 170. Both rows lost; this was the only Hit@2 failure in a twelve-card batch. No overtime was involved: regulation alone cleared the total.


**What went right.** The winner label was correctly called a coin flip (52/48) rather than overstating Kolossos, and the `G-L12` separation audit did print a 39% chance of Körfez winning by more than 2.5.


### Structural control addition
26. **Shared late-game kill state for coupled top-two rows.** When a cushion and an Under (or any two rows resting on the same close, low-possession regime) occupy the top two, print `P(¬R1 ∧ ¬R2)` and name the state — typically a fourth-quarter shooting or turnover run that produces separation and points together — separating it from the intentional-foul and overtime tails, which are distinct mechanisms. Origin `P-427`; cross-sport form `G-L17`. Reinforces controls on late-game, closing-lineup and foul/bonus branches, which existed and were stated but not quantified as a joint failure.


## 2026-09-17(b) settlement learning — `P-451` (LNBP Jornada 20) — **the fail-close held, and the result lane is now solved**


Learning-only (`L-087`). Cross-sport rules: `RULES_GENERAL.md` §16.13. Evidence: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17(b)"](PREDICTION_LOG_COMBINED_4.md).


**What happened.** Dorados de Chihuahua v El Calor de Cancún, the second game of a two-night series at the Gimnasio Manuel Bernardo Aguirre. The card ran the §9.5 onboarding check, found no current LNBP regulation packet, set **`BK-P1 = FAIL`**, and issued **no rank, probability, winner or direction**. Nothing enters any W/L, Brier, Rank-#1 or winner count.


**Three things to record.**


1. **The block was correct and it was costless.** The card listed four shortcuts it refused — home record → Dorados, a two-point first game → El Calor +4.5, a 180-point first game → Over, season scoring averages → Under. The final was **Dorados 97–86** (total 183, margin 11): two of those shortcuts would have won and two would have lost. A fail-close under `BK-P1` is not a forecast forgone; it is a coin flip declined.
2. **The block held under maximum collision pressure**, which is the harder test. Same opponents, consecutive nights, same venue, and a search surface saturated with the previous night's 91–89 Jornada 19 result. The card explicitly refused to use that score and wrote the warning into its own record. This is `§16.10(i)` fixture identity working exactly as intended in the sparse-competition case it was written for.
3. **`BK-P1` remains `FAIL`.** A fresh search for a 2026 LNBP competition-regulation packet in this pass again returned nothing: period length, foul-out/bonus, challenge, overtime resolution, roster activation, import eligibility and abandonment treatment are still unclosed. The unresolved-fields list in §9.5 is unchanged and the competition stays not forecastable.


### Source addition to §9.5 — the LNBP result lane is a rendering problem, not an access problem


The 2026-09-04 note in §9.5 records `https://lnbp.mx/` as returning HTTP 403 to the scripted route. That is now **out of date and was the wrong diagnosis**. The current state, verified 2026-09-17:


- `https://lnbp.mx/<Team>/team_results.html` (e.g. `/Dorados/`) returns **HTTP 200** to `curl`, but the payload is a ~16 KB JavaScript shell containing **no scores** — the results are injected client-side from a Summit/True Wisdom front end. Every text-fetch and proxy route therefore reports "no result found", which is what produced the mini log's `RESULT_NOT_RELIABLY_RECOVERED`.
- **Rendered in a browser, the same URL returns the per-Jornada finals directly**, with a Jornada selector. Selecting *Jornada 20* on the Dorados page returned **Dorados 97 — El Calor 86** immediately and unambiguously, distinct from the Jornada 19 game.
- `https://www.lnbp.mx/scores.html` is the league-level equivalent and needs the same rendering plus a Jornada selection.


**Operational consequence.** For LNBP results, escalate straight to the rendering rung of the §"web access rendering ladder" — do not spend the text-fetch rungs. A JS-only field owner is **reachable**, so a missing LNBP final is a `RETRIEVAL_MISS`, not unavailability. This lane settles **finals**; it does not close `BK-P1`, which needs a regulation document, and a regulations search on the same domain still returns nothing.


**Unchanged:** never upgrade this lane into a league-wide structured-stat source, and never pool an LNBP rate with a generic FIBA population. Recorded in `SOURCES.md` and `DATA_SOURCE_REGISTER.md` §"2026-09-17(b)".


### Structural control addition


27. **A JavaScript-only field owner is a rendering escalation, not a dead route.** When the competition's own site returns HTTP 200 with a shell that carries none of the wanted fields, record the state as **`JS_ONLY — RENDER REQUIRED`** rather than `NOT_AVAILABLE`, name the rung that will recover it, and treat a subsequent miss as a `RETRIEVAL_MISS` (§16.8 field 7). Distinguish this from a genuine 403/404, from a paywall and from a field the owner simply does not publish — the AFC corner field in soccer control 38 is the last kind, and no amount of rendering will produce it. Origin `P-451`; the same diagnosis applies to any league front end built on a client-side stats widget.


### `G-L24` in basketball (added 2026-09-17(b))


Basketball margins are near-continuous and the cushion band is **line-specific, not sport-specific** — there is no single `b_L` for the code. Derive it per competition and per line from that competition's own completed-season margin record; `BASE_RATES_REGISTER.md` §1 records basketball as `NOT_YET_DERIVED`. Two sport-specific cautions: **late intentional fouling** thickens the 3–6 point band in ways that differ by competition rules (control 26 already separates this from the shooting-run tail), and **overtime** removes the small-margin band entirely by construction, so derive over regulation-decided games and carry the OT branch separately (`G-L19`). `P-427` is the standing reminder that a cushion and an Under can die to one late state.


### `G-L21`–`G-L23` in basketball (added 2026-09-17(b))


**`G-L21`:** control 26 already requires `P(¬R1 ∧ ¬R2)` for a coupled cushion-and-Under top two, from `P-427`. Extend it past the top two: a 'slow, half-court, favourite controls it' thesis routinely carries a cushion, an Under **and** a team total, and one fourth-quarter shooting run kills all three together — `P-427`'s Q4 was 25–9. Print `P(all fail)` with Fréchet bounds, and check the **sign**: a low-possession game supports an Under while working *against* a favourite covering a spread, so those two are negatively coupled on pace even though both feel like control.


**`G-L22`:** basketball's forced pairs differ from baseball's in one way that matters. Spreads and totals are usually quoted on **half-points**, so the push branch is genuinely near zero and the two sides really do sum to ~1 — unlike an MLB integer total, where an inflated push is the standing defect. The counting rule still applies (one decision, not two rows), but the push-mass caution does **not** transfer; where a whole-number line *is* supplied, derive the push from the competition's own margin record rather than importing a figure from another sport.


**`G-L23`:** the process record is the **quarter-by-quarter score**, shooting splits and turnover counts; the disruption facts are **ejections, disqualifications and injury exits with the clock and score**. `P-427` is the reference: a 70–66 lead after three quarters becoming a 12-point loss is a fourth-quarter process fact, and a card amended from the final margin alone would have learned the wrong thing.


## Current model implementation — 2026-09-17


Use METHOD v4.2's six-field object and SCORING_AND_VALIDATION for exact outcome/push scoring, event-level comparison, descriptive recency and declared hierarchical uncertainty. MODEL_IMPLEMENTATION_RECIPES supplies this sport's retained model scope and endpoint design. Forecast probabilities come from the joint model; pooled base rates are uncertain context, not universal limits. Numeric row caps disconnected from that model, absolute-distance probability ordering and retrospective tail reweighting are withdrawn. No fitted coefficient or predictive improvement is claimed. New cards freeze the method/control hash; existing cards keep their issued versions.


## 2026-09-19 — recency/rebound evidence, debutant gate and the top-O/U review


Cross-sport: [`RECENCY_AND_REBOUND.md`](RECENCY_AND_REBOUND.md) control `R-1`; source controls `S-1` (social identity) and `S-2` (press conferences) in `SOURCES.md` §"2026-09-19"; enhanced-failure trigger in `METHOD.md` §7.


**`R-1` applies qualitatively; basketball magnitudes are `NOT_YET_DERIVED`.** Basketball's higher-count scoring target may well show different game-to-game autocorrelation than baseball's — derive it before any recent-form weighting, do not assume the MLB result transfers.


**Press-conference tempo claims (`S-2`).** A coach stating an intention to raise pace or tighten defence is **not** a pace or efficiency adjustment. It may motivate a named branch carrying its own mass, or widen the distribution; it may not move a possessions or efficiency centre. Stated intent and realised tempo are weakly related, and converting the former into the latter is the unsupported signed adjustment `G-L2` prohibits.


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — market-independent totals/line addendum


**Source priority:** NBA/FIBA/NBL/competition official stats, injury reports, rosters and team releases. Fantasy/DFS projections, ownership and optimizer outputs are prohibited.


Estimate possessions/pace and offensive/defensive efficiency independently of the line, with rotation/availability, rest/travel, venue and role uncertainty. Produce a joint score/margin distribution; combined total, team totals, spread and winner are post-forecast queries. Avoid additive narrative point adjustments that were not estimated in chronological data.




<!-- ALL-SPORTS-AUDIT-LIVE-RULE-CLEANUP-2026-09-21-CR3 -->
## 2026-09-21 — all-sports audit live-rule cleanup — CR-2026.09.21-3


Current prospective override. Retain the possession/opportunity model, minutes/usage mixtures, shooting shrinkage/uncertainty, foul/garbage-time/overtime tails and spread-total coupling. Withdraw pseudo-tail order-statistic constructions, path-count ranking shortcuts, universal probability-band top-slot rules, normalized-distance ordering, and one-result response rules. Build one coherent basketball joint outcome distribution before querying targets; without a fitted/calibrated distribution, do not invent precise probabilities.


<!-- CONSOLIDATED-MINI-LOG-IMPORT-2026-09-23 -->
## 2026-09-23 settlement learning — `TMP-20260923-NBL-CNS-TAS` (NBL) and `TMP-20260922-WNBA-DAL-PHX` (WNBA; body not carried)

Full records: [`PREDICTION_LOG_COMBINED_5.md` §"2026-09-23(c)"](PREDICTION_LOG_COMBINED_5.md). Learning-only.

**NBL — Cairns 93, Tasmania 87.** Rank #1 JackJumpers +2.5 **lost**; Under 186.5 won (on the card's reading of a prompt that said "18.5"); the winner call (Tasmania) lost.

- **The card executed none of this file's §7–§8 sequence.** It had no pace × efficiency joint, no probabilities and no margin distribution. This is **M15**.
- **Roster identity failed.**
  - The Cairns list omitted Jack McVeigh (starter, 17 points) and Kyrin Galloway (19 points off the bench).
  - "Galloway out" was Jaylin Galloway. The **official NBL expected depth chart**, published pregame, listed "PF: J.McVeigh / K.Galloway".
  - → **OBSERVATION `O-ROSTER-NAME-COLLISION`**: when an injury note names a player who shares a surname with an active teammate, print first names and the official active list. §7 step 2 already requires official availability before process history.
- **One-game recency as a rate** (R-1): "surrendered 111 in R1".
- **Travel fatigue given one sign only** (G-L2): it was applied to the total, not to the travelling side.
- **Home court unpriced** for an away-side winner call.
- **Tip lag.** The official NBL match feed's first live play-by-play event was 19:36:09 AEST against a 19:30 schedule. **OBSERVATION `O-START-MARKER`**: use the feed's first-event timestamp as the actual start in horizon audits.
- **Settlement sources.**
  - The NBL match-data endpoint (`schedule.nbl.com.au/api/calendar/match?match=<uuid>&league=NBL`) exposes `match_status`, scores, the play-by-play and a lead tracker. **It also contains `betting` and `odds` objects: parse it programmatically, skip those keys, and use it for settlement only.** It stays quarantined from forecast evidence.
  - ESPN `…/basketball/nbl/scoreboard?dates=YYYYMMDD` (no browser User-Agent) lagged "Final" by about 7 minutes.
  - Flashscore's NBL results page served as an independent third lineage.

**WNBA — Phoenix 87, Dallas 86** (P-487 claimant A). The surviving Rank #1, Mercury +5.5, won; the Dallas winner call lost on a last-second layup. The body is not carried, so **no process learning** is drawn.

**Follow-up, 2026-09-23 ~22:05 AEST — WNBA P-487 body recovered and settled** ([Part 5 §"2026-09-23(d)"](PREDICTION_LOG_COMBINED_5.md)):

- Mercury +5.5 (Rank #1) **won**: Phoenix 87–86 on Copper's layup with 2.4 s left.
- Over 174.5 **lost** at 173 (`TOP_OU_REVIEW`). The line sat at the card's centre, making it a coin flip that was correctly labelled LOW. **No totals rule.**
- Dallas winner call **lost**.
- The card's eight-branch mixture (BK-B1–B8, weights summing to 100%) reproduces its total probability (Over 52% at representative level). The spread and winner probabilities are not reproducible without a within-branch spread (G-L8), and `P(R1 ∧ R2)` was not printed (G-L10).
- **OBSERVATION `O-ANNOUNCED-MINUTES-PLAN`:** Dallas's reported minutes management did not bind in a close game (Shepard 36 min v 27 two days earlier). Treat such reports as intentions with a close-game restoration branch.
- **Horizon aid:** ESPN `summary` `plays[].wallclock` gives the actual tip (02:07:42Z here, v a 02:00Z schedule).

<!-- CONSOLIDATED-MINI-LOG-IMPORT-2026-09-24 -->
<!-- AUDIT-2026-09-24F -->
## 2026-09-24 settlement learning — P-497, P-498 (LKL), P-499 (EuroLeague Women), P-504 (WNBA), P-505 (El Salvador LMB), P-508 (NBL), corrected 2026-09-24(f)

**Full record:** `PREDICTION_LOG_COMBINED_5.md` §"2026-09-24(e)" (peer settlement, with its audit banner) and §"2026-09-24(f)" (verification audit). This is learning-only.

**What changed.** The peer version of this section (`cb95acd`) got P-498 wrong: it said "Rank-1 Lietkabelis −4.5 L; home-dog upset". The issued Rank 1 was **Under 171.5, and it won**. It also printed quarter lines that the field owner contradicts, and it promoted two rules that are withdrawn below. The table is copied from the issued cards. The quarter lines come from BasketNews, FIBA, xscores and ESPN.

| Card | Competition | Rank #1 (p) | Final (verified; quarters) | Top O/U (rank) | Centre → actual | Verified note |
|---|---|---|---|---|---|---|
| P-497 | LKL | Neptūnas −3.5 (0.530) **W** | 99–84 (18:16, 31:20, 28:20, 22:28) | Over 175.5 (#2) **W** | 176.9 → 183 | A near-tie row that landed. Coaches Petrauskas and Eglinskas (the card was right) |
| P-498 | LKL | Under 171.5 (0.654) **W** | 86–77 (26:20, 16:25, 22:20, 22:12) | Under 171.5 (#1) **W** | 167.3 → 163 | Lietkabelis led 65–64 after three; their +3.5 died in a 22–12 fourth quarter |
| P-499 | EWL qualifier | Under 149.5 (0.626) **L** | 101–81 (22-25-32-22 v 22-16-22-21) | Under 149.5 (#1) **L** | 144.8 → 182 | Brno's top scorer, Puckett (27), was **not in the card**. Carolo did not rest when 19+ ahead. Comparator: two games against a different club |
| P-504 | WNBA | Dream −4.5 (0.591) **W** | 83–65 (18-23-17-25 v 19-7-18-21) | Under 173.5 (#2) **W** | 171.4 → 148 | Stewart absent (the card was right). ATL: B. Jones, listed as a starter, was a coach's-decision DNP |
| P-505 | LMB (Clausura R1) | Under 154.5 (0.637) **W** | 77–71 (20-17-23-17 v 18-18-9-26) | Under 154.5 (#1) **W** | 149.3 → 148 | Best centre of the batch. Season opener |
| P-508 | NBL | Under 194.5 (0.691) **W** | 86–61 (16-29-24-17 v 14-21-22-4) | Under 194.5 (#1) **W** | 185.9 → 147 | PNX 24/88 FG and **4/41 from three**; 4 points in Q4. The card's PNX starter Hurt did not play; Foster, listed OUT, played |

### Withdrawn or demoted (not operative)

**`BASKETBALL-DERBY-TOTAL-SUPPRESSION` — REJECTED (L-20260924-F04).**
- It came from one game.
- The Under's 47.5-point margin came from Phoenix shooting 10% from three and scoring 4 points in the final quarter, a shooting-variance state and not a derby mechanism.
- "Totals routinely fall 15–30 below lines" has no source.
- The rule had already leaked into the P-509 card text ("half-court derby tempo") for Perth v Adelaide, which is not a derby.

**`FIBA-CLUB-QUALIFIER-PACE-ADJUSTMENT` (a mandatory +5.5 possessions) — REJECTED as a coefficient (L-20260924-F07).**
- It came from one game, and its "89 possessions" was never sourced.
- The P-499 miss traces to a roster retrieval failure (Puckett missing), comparator over-weighting (M13/M17) and an unevidenced "coach rests starters when ahead" branch (compare `O-ANNOUNCED-MINUTES-PLAN`, L-20260923-12).
- Replacement: **TESTING `T-BKB-SEASON-OPENER-WIDTH`.** For a team's first competitive game of a season (a qualifier or league opener), test whether |actual − centre|/width is larger than on concurrent non-opener cards. The response, if confirmed, is **width only, never a centre shift**. Test on the next 15 opener cards.
- Current evidence is mixed. P-499 missed by +37 (opener). P-505 missed by −1.3 (Clausura R1). P-497 and P-498 missed by +6 and −4 (early LKL season).

### Controls added (integrity and retrieval only)

**K-1. Official starters and roster at freeze (`C-LINEUP-DIFF`; G14.2; L-20260923-06 recurrence).**
- The card prints each side's starting five and active roster from the competition's official feed, with the fetch time: NBA/WNBA/NBL official preview or box; FIBA LiveStats or the game page; the LKL match centre.
- `PROJECTED_BEAT_VERIFIED` requires the S-1 Rev 2 receipt (outlet, reporter, timestamp, verbatim quote, two sources).
- At settlement, the card-listed starters are diffed against the box score.
- Evidence: P-499 (the top scorer absent from the card), P-504 (ATL 4/5, NY 3/5), P-508 (PNX 3/5; Foster's status wrong), and the 2026-09-23 NBL card. Recurrence: P-509 (2026-09-24(g): ADL 3/5 named starters; no receipt printed).

**K-2. Blowout, rest and shooting-variance states are width.**
- The two biggest Under wins, P-504 (−25.5 against the line) and P-508 (−47.5), and the biggest Under loss, P-499 (+32.5), all came from states outside the stated widths. The absolute residuals were 23.4, 38.9 and 37.2 against widths of 16–17.6.
- Keep reporting these wins as **result-right with the process unconfirmed**. They do not validate a centre.

**K-3. NBL actual start marker (confirmed 2026-09-25; `O-START-MARKER`).** In the NBL match feed the actual tip is the first `play_by_play` event with `action_type = jumpBall`. The earliest records are `fixture`/`period` placeholders. Two NBL games tipped about six minutes after schedule: TMP-NBL-CNS-TAS at 19:36:09 against 19:30, and P-509 at 21:36:13 against 21:30 AEST. A freeze inside that window is still pregame; horizon audits use the `jumpBall` timestamp.

<!-- RESEARCH-2026-09-25 -->
## 2026-09-25(b) — reference rates, width benchmarks, early-season windows and recency (research pass)

**Status.** Reference rates and disclosure controls (`C-PROMOTION-RECEIPT`: `REFERENCE` / `PROMOTED_PROCESS`). None is a coefficient or a floor. Sources: `BASE_RATES_REGISTER.md` §7.1 and `RECENCY_AND_REBOUND.md` §7. Regular seasons: NBA 2025-26 (n = 1,235), WNBA 2026 (327; plus 2024 and 2025), NBL 2025-26 (165; plus 2023-24 and 2024-25).

**K-4. Print the league reference (field BR).**
- **Totals:** the league mean and SD.
- **Handicaps:** the pooled P(\|margin\| ≤ k) band for the line. For example, NBA ≤ 5 is 0.246 and ≤ 10 is 0.479.
- **Phase rows:** the league's quarter shape.
  - NBA: Q4 averages **55.3**, against 57.6–58.7 in Q1–Q3.
  - NBL: the second half runs below the first (Q3/Q4 about 44.4 v Q1/Q2 about 46.2; first-half share 0.504–0.514 across three seasons).
  - WNBA: flat.
- **Overtime:** about 4–5.5% of games, adding about 25 points. A total within about 12 of the line keeps the overtime branch as explicit mass.

**K-5. `C-WIDTH-BENCHMARK` (RULES_GENERAL §"2026-09-25(b)"(a)).**

| League | Total residual SD | Margin residual SD | 0.85 × total | 0.85 × margin |
|---|---:|---:|---:|---:|
| NBA | 19.4 | 15.1 | 16.5 | 12.8 |
| WNBA 2026 | 19.5 | 13.3 | 16.6 | 11.3 |
| NBL | 18.7 | 15.2 | 15.9 | 12.9 |
| Narrowest derived benchmark (WNBA 2024) | 16.0 | 11.1 | 13.6 | 9.4 |

- A card width below the 0.85 figure names what the card knows beyond a season-to-date model.
- For leagues without a benchmark (LKL, EuroLeague and EuroLeague Women, LMB, FIBA windows), print `REFERENCE_WIDTH_NOT_YET_DERIVED`. The narrowest derived benchmark is the comparison: a width below 13.6 (total) or 9.4 (margin) needs the same written reason.
- **Evidence.** In the 2026-09-24 cohort, basketball total widths ran about 39% narrow (mean z² 1.93, n = 7). Both LKL cards used total widths of 12.1–12.9 and margin widths of 8.4–9.0.

**K-6. Early-season windows and the 2026 WNBA regime (RULES_GENERAL §"2026-09-25(b)"(d)).**
- **NBL.** Games where both teams have played fewer than 3 games ran **−8.5 points** against the rest of the season (95% CI −14.3 to −2.7). That is three seasons and 38 games, with the same sign each season. NBL scoring also rises through the season: a season-to-date predictor under-shoots by 4–9 points.
  - An NBL round 1–3 card prints the early-season reference beside its centre.
  - It does not centre on the previous season's full-season mean without saying so.
  - P-508 (147) and P-509 (195) were both in the 2026-27 early window.
- **WNBA.** The early window runs the other way: **+6.5** (+0.4, +12.6), n = 57. This is why no cross-league early-season rule exists.
- **WNBA 2026 scored 10.7 points per game more than 2024 and 2025** (174.4 v 163.7). A WNBA head-to-head or multi-season average that includes 2024 or 2025 is state-contaminated (M24). The card excludes those seasons or adjusts for the shift, and says which.

**K-7. Back-to-backs (named-mechanism size).**
- NBA: a team on a back-to-back against a rested opponent ran **−1.84** (−3.78, +0.11), n = 261. That is small against a margin SD of about 15. A margin centre moved for a back-to-back moves by about this much or less.
- Totals show no reliable fatigue effect: both teams on a back-to-back ran −3.6 (−8.5, +1.4), n = 65. A fatigue argument is width (G-L2), not a signed total adjustment.
- The WNBA (n = 19) and NBL (none among the scored games) are not derived.

**K-8. Recency (`R-1`; RECENCY §7.2).**
- In all three leagues, a single previous game is the worst predictor of a team's next score: **+18% to +36% RMSE** against the league constant.
- Adding the opponent's defence to date improves RMSE by **7–11%**, more than any recency window.
- A card's team-scoring input is the season rate (in the NBL, a last-10 rate is acceptable because scoring rises through the season) plus the opponent's defence. One recent game is a pointer to a mechanism, never a weight.

<!-- SETTLED-ROW-REVIEW-2026-09-25D -->
## 2026-09-25(d) — track record from the full settled-row review

**Track record (`C-TRACK-RECORD`).** 31 decisions from 17 cards: won **58.1%** at a mean stated 0.586. Brier 0.241, resolution **0.012**, which is near zero.

- **Underdog cushions (+k.5): 3/8** at 0.58. **Favourite handicaps (−k.5): 6/9** at 0.554. Unders 5/8 at 0.608.
- **K-9. `C-PLUS-CUSHION` applies to every +k.5 row.** The card prints:
  - the population margin band from `BASE_RATES_REGISTER.md` §7.1(a), e.g. NBL P(|margin| ≤ 2) is about 0.18 and NBA P(|margin| ≤ 5) is 0.246;
  - `BASELINE_P`;
  - P(underdog wins) + P(loses by ≤ k) from `python tools/card_math.py cover --dist normal --mean … --sd … --line +k --no-zero`;
  - the named reason the margin stays inside k.

  The recurrence is recorded under M32. Basketball margins can never be 0, so always use `--no-zero`.
- **K-10. Departure ledger.** With resolution near zero, every departure from `BASELINE_P` is itemised (`C-DEPARTURE-LEDGER`). The seed baseline check found the basketball rows no better than the population.

Source: `research/settled_rows_2026-09-25/README.md`. The figures are hindsight on the framework's own cards, descriptive, and use card-cluster intervals. None is a coefficient (`L-087`). Controls: `RULES_GENERAL.md` §"2026-09-25(d)".


<!-- RANK-MODEL-2026-09-25E -->
## 2026-09-25(e) — Rank 1 and Rank 2 in basketball: the team baseline, cushion population rates and the ranking model

Controls: `RULES_GENERAL.md` §"2026-09-25(e)". Evidence: `research/team_baseline_2026-09-25e/README.md`, `research/rank_model_2026-09-25e/README.md`.

**Record at Rank 1/2 (probability era): 18 W / 16 L.** Resolution is near zero. Underdog cushions won 2/9. P-514 (NBL): Under 188.5 lost; Hawks +1.5 lost; the complement Bullets −1.5 won.

### (a) Sources

- **TB-1 lane.** ESPN team schedules (`…/basketball/{nba,wnba,nbl}/teams/{id}/schedule?seasontype=2`), no browser User-Agent. `python tools/team_baseline.py predict --league nba|wnba|nbl …`.
- **Not covered:** FIBA, LKL, BCL, EuroLeague, LNBP and LMB have no TB-1 lane (`TEAM_BASELINE_P: NOT_COVERED`). `BASELINE_P` stays the anchor, and the §7.1 reference width applies.
- **Unchanged:** official starters, the NBL `jumpBall` tip marker, and the settlement diff from `receipts.py settle espn`.

### (b) Reasoning

- **K-11. TB-1 is the anchor for NBA, WNBA and NBL sides.**
  - Out of sample, P(home win) Brier: NBA 0.216 v 0.248; WNBA 0.216 v 0.256; NBL 0.223 v 0.255.
  - NBA and WNBA totals also have resolution (0.240 v 0.249; 0.232 v 0.258). **NBL totals do not.**
  - A departure of more than 0.10 from `TEAM_BASELINE_P` names a receipted mechanism: a confirmed absence, rest, travel, or the NBL early-season −8.5 on totals.
  - `TB1_EARLY_SEASON` applies below 3 games per team. In the WNBA, TB-1 carries last season forward (r = 0.75).
- **K-12. Small cushions at their population rate.** The TB-1 underdog covers:

  | Cushion | Population cover rate |
  |---|---|
  | +1.5 | 0.32–0.40 |
  | +2.5 | 0.35–0.43 |
  | +3.5 | 0.38–0.45 |
  | +5.5 | 0.44–0.51 |

  Sources: NBA 2025-26, WNBA 2025–26, NBL 2024-26 (`BASE_RATES_REGISTER.md` §7.7(c)).
  - A +k.5 row on the weaker team stated above its rate by more than 0.05 needs a receipted mechanism on the favourite's side. Otherwise it is `PLUS_CUSHION_UNSUPPORTED`, and **RM-1 flips the pair.** In P-514, Bullets −1.5 had RM-1 q ≈ 0.74; it won.
  - "The underdog keeps it close" is not a mechanism: P(|margin| ≤ 2) is only 7–12%.
- **K-13. Ranking.**
  - Rank by RM-1 q.
  - A flipped favourite handicap is capped at SUPPORTED. It may be overridden only if `TEAM_BASELINE_P` gives the stated cushion ≥ 0.55.
  - Basketball total widths still run narrow (M31), so an Under at Rank 1 needs its width at or above the reference.
- **Rejected (M27):** `C-ABSENCE-DEFENSIVE-PENALTY`, from two games (P-514, P-515). An absence widens the distribution (G-L2); it does not set a signed lean without a measured rate.
