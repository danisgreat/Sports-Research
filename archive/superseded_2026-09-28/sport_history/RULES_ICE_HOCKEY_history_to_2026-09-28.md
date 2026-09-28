# Ice hockey analysis rules — dated history to 2026-09-28

**Archived 2026-09-28 (md-only restructure).** These are the dated sections that followed the competition-rules section of `RULES_ICE_HOCKEY.md`, moved verbatim. They are the evidence record. The live rules are §0 of `RULES_ICE_HOCKEY.md`, and nothing here reinstates a rule that §0 or `CURRENT_RULES.md` §I withdraws.

## September 5 settlement learning — prospective SFA amendment


P-166 and P-200 remain completed-event **research** settlements with unresolved operator endpoints. Maintain regulation score, OT score and any shootout accounting as separate fields. A corroborated final is not evidence of what an unnamed operator includes. P-200's regulation total six versus final seven crosses 6.5; do not invent an action rule. P-166's final 5–4 versus regulation 4–4 likewise requires row-level endpoint comparison.


L-068–L-071 apply at this SFA's identity/goalie-exposure/period-to-OT/settlement stages. They repair arithmetic, gate propagation, two-sided phases and field semantics; this pass introduces no hockey scoring-rate or goalie coefficient.




Full evidence and frozen-card comparisons: [September 5 audit](archive/audit_documents_implemented_2026-09-25/COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md).


## September 6 settlement learning — cross-sport gates instantiated, and the overtime-terms closure route


No ice-hockey card was settled in the `P-294`–`P-305` cohort. Two inherited follow-ups (`P-166` Melbourne Mustangs v Canberra Brave, AIHL; `P-200` Herning Blue Fox v Rungsted, Metal Ligaen) have sat `FINAL / RESEARCH SETTLED — operator OT/action unresolved` for weeks. Both are cases where the *game result is known and undisputed* (Canberra 5–4 in overtime, regulation 4–4; Herning 4–3 in overtime, regulation 3–3) and the only obstacle is that no operator terms were supplied to say whether the contract settles on regulation or on the final including overtime.


**New gate `G36.1` supplies the route to close them:** grade under stated standard rules, with the standard-rules assumption written down beside the grade. The governing price-independence rule already says a missing price or missing operator wording never justifies leaving a finished event ungraded. Both cards are therefore flagged for closure under `G36.1` at the next settlement pass rather than carried indefinitely. **They are not regraded in this pass**, because regrading a historical settlement is a decision that should be taken deliberately rather than as a side effect of a rule change.


**Ice-hockey-native tail example.** A total-goals `Under` is exposed to the empty-net tail: a one-goal game in the final two minutes has a materially higher scoring rate than the preceding 58, and a 5-on-6 empty-net situation can add two goals in under a minute. Hold the final-two-minutes window as its own term in the tail budget, exactly as `G20.1` already requires the scoring-allocation phases to be split for margins. Overtime and the shootout are separate branches with their own rate environments under `G22`.




### Cross-sport gates instantiated here (v3.7)


| Gate | Sport-native instantiation |
|---|---|
| `G10.2` settlement-source pre-registration | NHL settles from the official NHL game summary; AIHL, Metal Ligaen and comparable leagues need their own named official endpoint. Where overtime/shootout action terms are unsupplied, `G36.1` governs: grade under standard rules with the assumption stated. |
| `G14.2` coaching / bench / rotation record | Record the head coach, the confirmed starting goaltender (the single highest-leverage participant in this sport), the scratches, and back-to-back/travel signals. Where official NHL feeds lag, morning skate line combinations, starting goaltender off-the-ice cues, and scratch reports verified across accredited beat reporters or official team media releases under Control `S-1 Rev 2` qualify as `PROJECTED_BEAT_VERIFIED`, satisfy `G14.2` personnel modeling, and do not block Rank #1. |
| `G20.2` distributional tail audit | Derive tail and boundary mass from the **same frozen ice-hockey joint score distribution**, including confirmed goalie state, 5v5 shot/xG process, special teams, score effects, empty-net and overtime branches, with travel/rest used only through a named mechanism. Historical order-statistic stress sums are superseded as active gates. |
| `G21.1` exact target geometry | Map every supplied target to its exact settlement event and derive WIN/PUSH/LOSS from the same frozen sport-native PMF/CDF or coherent branch mixture. Historical path-count/category labels have no mandatory ordinal effect. |
| `G26.1` no universal separation floor | Reference rates and `rank_gap` are descriptive only. **No 40–60% or other pooled probability band can disqualify Rank #1.** Rank from exact marginal likelihood plus robustness/evidence uncertainty. |


**Pre-issue checklist additions (this sport):** settlement endpoint named per row; coaching/bench/rotation record for both sides with missingness codes; tail-budget sums printed against every total line; path-geometry class and `N` printed for every total and phase-total row; separation-floor result stated for Rank #1.


Full narrative and evidence: [`archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md`](archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md). Controlling gate text: [`RULES_GENERAL.md` §13](RULES_GENERAL.md).


## September 5 implementation after freeze confirmation


**ACTIVE REQUIRED PROCESS — MDS-2026.09.05-v3.6 / L-068–L-072.** Keep regulation and overtime/shootout endpoints explicit in total and margin calculations. An unknown operator endpoint is a contract-specific follow-up; it does not invalidate an otherwise frozen pre-game card or justify a new scoring coefficient.


At final delivery, record the preferred total direction for each exact target, the strongest evidenced failure path for ranks #1 and #2, and whether both can win under the stated joint scenario. Rank by supported marginal likelihood; do not promote an opposite pick solely to manufacture one O/U win. At settlement, keep all issued wins/losses, including defective reasoning, in the applicable historical scorecard and review failed #1/#2 and preferred totals.


[Eligibility policy](PERFORMANCE_ELIGIBILITY_POLICY.md): non-live history is user-confirmed frozen pre-game; explicit live-issued views stay separate. These process repairs are implemented now. Numerical weights and predictive-lift claims need a later frozen comparison; historical origin games do not supply those completions.


## 2026-09-06(f) — settlement and retrospective addendum


P-166/P-200 retain regulation and completed-match scores side by side. P-166 all four ranked rows are invariant across 4–4 regulation and 5–4 OT; P-200 6.5 totals reverse between 3–3 regulation and 4–3 OT. Research uses the stated full-match convention, with unknown operator action separate. Competitive wins do not establish multi-goal separation; no goalie/fatigue mechanism is invented from final scores.


Full frozen ranks, actual drivers, knowability and smallest fixes: [PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md). Reinforcement only; METHOD v4.0 remains controlling and no new predictive weighting is promoted.


## 2026-09-09 — cross-sport controls instantiated here (`G-L1`, `G-L2`, `G-L7`, `G-L8`)


No ice-hockey card was issued in the `P-333`–`P-344` cohort. The four cross-sport requirements adopted from it (`RULES_GENERAL.md` §§16.5(a)–(d), full evidence in `PREDICTION_LOG_COMBINED_3.md` §"2026-09-09") apply to this sport from the next card. All four are **disclosure/retrieval requirements — no fitted weight, no ordinal bar** (`L-087`).


| Cross-sport control | Ice-hockey instantiation |
|---|---|
| **`G-L1` §16.5(a)** — enumerate outcome-state families with explicit mass | Enumerate the **goal-total families** (≤3 / 4 / 5 / 6 / 7+) and the **margin families** (regulation blowout 3+ / regulation 2 / regulation 1 / tied-after-60 → OT/SO), each with an explicit mass summing to 1. The **tied-after-regulation branch must carry its own stated mass** and its own empty-net/OT/shootout scoring rate — `P-166` and `P-200` both settled differently at the regulation and completed-game endpoints, so the family enumeration must be produced **once per endpoint** and the invariant rows identified. Every current-evidence §8.5 kill path, including the **empty-net goal** and the **late push**, appears as a weighted branch. Print a representative Rank-#1 final score and check it against the line, the total and the endpoint convention. |
| **`G-L2` — declared uncertainty model** | State the prior and scenario probabilities. Symmetric uncertainty around an unchanged prior affects width; hierarchical shrinkage or asymmetric scenarios may change both mean and variance. Regenerate all dependent probabilities; unsupported directional adjustments remain prohibited. SCORING_AND_VALIDATION section 5 controls. |
| **`G-L7` §16.5(c)** — aggregate-to-disaggregate retrieval | Do not let a season save percentage, a goals-against average or a "last N" summary carry directional weight while the **per-start log** is available. Print the goaltender's **start-by-start record** (shots faced, saves, goals against, save percentage) for the decision-relevant window and state whether a slump is front-loaded, back-loaded or uniform, and whether the **underlying workload/shot-quality held** — the direct analogue of the walk-rate check that decided `P-339`. Quantify **every forward line's recent goal/assist output and every goaltender's per-start line**; a name in a "leaders include…" phrase without a number is `AGGREGATE_ONLY` and caps the dependent total/margin rows. |
| **`G-L8` — distribution coherence** | Derive each total/spread probability from the exact joint PMF/CDF and settlement endpoint, with push mass. Absolute normalised distance does not order probabilities across different distributions. No missing width or realised result justifies an invented probability. |


## 2026-09-11 — cross-sport controls instantiated here (`G-L9`, `G-L10`, `G-L11`, §16.8)


No ice-hockey card in the `P-345`–`P-371` import. From the next card ([`RULES_GENERAL.md` §§16.5(e)–(g), §16.8](RULES_GENERAL.md)):


| Control | Ice-hockey instantiation |
|---|---|
| `G-L9` §16.5(e) | Itemise the complement of an Under or a +1.5 puck line across the named paths — empty-net goals, a power-play cluster, a backup goaltender, overtime. |
| `G-L10` §16.5(f) | A favourite −1.5 and an Over are positively coupled through empty-net goals; an underdog +1.5 and an Under are positively coupled through a tight, goaltender-driven game. Print the sign. |
| `G-L11` §16.5(g) | A goaltender's save percentage over a few starts is a proportion over shots faced — print its standard error before it moves the centre. |
| §16.8 | The starting goaltender is confirmed before puck drop; `NOT_RETRIEVED` after confirmation is a `RETRIEVAL_MISS`. |




## 2026-09-12 algorithm corrections and retrospective integration


Apply section 16.9 to joint regulation goals and the overtime/shootout contract. Confirm starting goalies separately from roster membership, skater lines, scratches, reserves and coaches. Empty-net and power-play states can alter total/margin dependence; include them once in exclusive outcome branches. Shot/save rates use actual attempts and quality/context, not invented denominators. No new hockey result was settled in this pass; transferred controls repair arithmetic/provenance only.


For every supplied row, use exact target probabilities from a coherent joint distribution; handle push/void/censoring explicitly, avoid overlapping adverse-state counts, and report JOINT_UNQUANTIFIED with bounds if the dependence is not specified. Separate issued-time participant capture, later recovered evidence, source accuracy by field, observed mechanism, and unverified causal interpretation. Keep one preferred O/U direction per distinct target and report the top-two denominator honestly. Shared correction and methodology sources (`audit_2026-09-12/rule_corrections.md`, not present in this repository). All current log observations remain learning-only and not performance-eligible.




## 2026-09-15(b) settlement learning — `P-373`–`P-423` import


Learning-only; disclosure/process changes only — no coefficient or ordinal bar (`L-087`). Evidence and tables: [`PREDICTION_LOG_COMBINED_3.md` §"2026-09-15(b)"](PREDICTION_LOG_COMBINED_3.md). Cross-sport rule: `RULES_GENERAL.md` §16.10 (`G-L12` margin centre/width; fixture identity; official-record derivative settlement).


No ice-hockey card in this import. **`G-L12` instantiation:** for any puck line in the top two, print P(favourite by 2+) from the goal-margin families, including the empty-net branch for one-goal games; goalie uncertainty (control 14) widens, it does not move the centre toward a one-goal game.


## 2026-09-16 — cross-sport controls instantiated here (`G-L13`, `G-L14`, `G-L15`, disruption facts)


No ice-hockey card was settled this pass. Rules: `RULES_GENERAL.md` §16.11.
- **`G-L13`:** the starting goalie is confirmed from a raw league or team record, not a summary.
- **`G-L14`:** period totals and shots-on-goal rows name their settling record at issue; the operator's overtime and shootout terms are recorded separately (`G36.1`).
- **`G-L15`:** label total rows forced-pair or free.
- **Disruption facts:** record major penalties, match penalties, goalie changes and empty-net goals with the game clock and score.


## 2026-09-17 — cross-sport controls instantiated here (`G-L17`–`G-L20`)


No ice-hockey card in this import. **`G-L17`:** a puck line and an Under commonly share one low-event state — print the joint failure mass and name it. **`G-L18`:** print each side's goal marginal before a game total. **`G-L19`:** the end-state family must distinguish regulation win, overtime win and shoot-out win, and must match the operator's stated endpoint (`G36.1`); a two-outcome label is invalid where the competition records regulation ties. **`G-L20`:** a recent same-venue meeting that cleared the total gets explicit mass.


Evidence and cohort audit: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17"](PREDICTION_LOG_COMBINED_4.md); rules in `RULES_GENERAL.md` §16.12.


## 2026-09-17(b) — cross-sport controls instantiated here (`G-L21`–`G-L24`)


**G-L24 in ICE HOCKEY:** derive the exact signed-margin distribution under the competition endpoint, including draw, key-value and push masses. Pooled league bands are uncertain references, not mandatory matchup probabilities or rank prohibitions. Missing pooled bands do not invalidate a complete conditional joint distribution. **`G-L21`:** 'goaltender steals it' carries an Under, a dog line and a team total together — print `P(all fail)`. **`G-L22`:** puck line and total are forced pairs. **`G-L23`:** shots, high-danger chances, goaltender changes and **the empty-net timestamp** are the process record; a goal scored into an empty net is an endpoint artefact, not evidence about the run of play.


Evidence and cohort audit: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17(b)"](PREDICTION_LOG_COMBINED_4.md); rules in `RULES_GENERAL.md` §16.13; bands and base rates in [`BASE_RATES_REGISTER.md`](BASE_RATES_REGISTER.md).


## Current model implementation — 2026-09-17


Use METHOD v4.2's six-field object and SCORING_AND_VALIDATION for exact outcome/push scoring, event-level comparison, descriptive recency and declared hierarchical uncertainty. MODEL_IMPLEMENTATION_RECIPES supplies this sport's retained model scope and endpoint design. Forecast probabilities come from the joint model; pooled base rates are uncertain context, not universal limits. Numeric row caps disconnected from that model, absolute-distance probability ordering and retrospective tail reweighting are withdrawn. No fitted coefficient or predictive improvement is claimed. New cards freeze the method/control hash; existing cards keep their issued versions.


## 2026-09-19 — recency/rebound, social sources and the top-O/U review


`R-1` ([`RECENCY_AND_REBOUND.md`](RECENCY_AND_REBOUND.md)) applies: recent results revise an estimated **rate** through a named mechanism, never forecast a **deviation**. No rebound and no hangover adjustment is permitted in either direction. This sport's magnitudes are **`NOT_YET_DERIVED`** — the MLB figures are not transferable and must not be imported; derive them from this competition's own record before any recent-form weighting.


Source controls `S-1` (social identity: X and Reddit return no usable content; Bluesky sports handles failed identity verification 6/6) and `S-2` (press conferences are availability/role evidence, never a signed adjustment to a modelled rate) apply — `SOURCES.md` §"2026-09-19".


A loss **or push** on the card's highest-ranked over/under now triggers the same enhanced failure review as a Rank #1 loss (`METHOD.md` §7).


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — market-independent totals/line addendum


**Source priority:** NHL/competition official Gamecenter/stats/EDGE and team roster/goalie releases; valid independent structured stats only with known lineage. Betting/fantasy projections are prohibited.


Model regulation/OT score states with confirmed/probabilistic goalie, lineup/lines, shot/quality process where definition-stable, special teams, rest/travel and venue state. Moneyline/puck-line/total queries must come from the same coherent distribution and correct competition end-state rules.




<!-- ALL-SPORTS-AUDIT-LIVE-RULE-CLEANUP-2026-09-21-CR3 -->
## 2026-09-21 — all-sports audit live-rule cleanup — CR-2026.09.21-3


Current prospective override. Retain confirmed goalie state, 5v5 shot/xG process, special teams, score effects, empty-net/overtime branches and travel/rest only with a named mechanism. Withdraw pseudo-tail order-statistic constructions, path-count ranking shortcuts, universal probability-band top-slot rules, automatic goalie-unknown total direction and recent-finishing-streak conversion shifts. Build one coherent ice-hockey joint outcome distribution before querying targets.
<!-- CONSOLIDATED-MINI-LOG-IMPORT-2026-09-24 -->
<!-- AUDIT-2026-09-24F -->
## 2026-09-24 settlement learning — P-503 (NHL pre-season: Minnesota Wild @ Dallas Stars), corrected 2026-09-24(f)

**Full record:** `PREDICTION_LOG_COMBINED_5.md` §"2026-09-24(f)". This is learning-only.

| Card | Rank #1 (p) | Final (verified: NHL api-web `2026010034`) | Top O/U (rank) | Verified process |
|---|---|---|---|---|
| P-503 | Stars ML (0.708) **W** | DAL 2–0, regulation | Under 5.5 (#2) **W** (2) | Goals: Seminoff P2 15:33 (even strength) and Lindell P3 10:39 (even strength); no empty-net modifier. **DAL goalie: Poirier, 59:29, 24/24. Oettinger, whom the card called "confirmed", did not play.** MIN goalie Wallstedt stopped 22 of 24. SOG 24–24 |

The peer version of this section (`cb95acd`) was wrong in four respects:
- it printed a short-handed goal and an empty-net goal;
- it credited Poirier and Oettinger with a combined shutout;
- it put the Under line at 6.0 (the issued line was 5.5);
- it listed a "Stars −1.5" row, which the card never had.

### Demoted: `NHL-PRESEASON-ROSTER-ASYMMETRY` → non-ranking disclosure plus TESTING (L-20260924-F08)

**Why demoted.** The roster read was right: Minnesota dressed a prospect squad (Stramel, Shaw, Pitlick, Heidt and others) while Dallas dressed Benn, Heiskanen, Lindell, Steel, Faksa and others. But it rests on one win, and the same card's highest-leverage participant claim, the goalie, was false. A rule that makes a roster-tier gap "promotable to Rank #1" is a predictive override from one game (§16.10 item 11).

**What remains operative (disclosure only).**
1. A pre-season card prints each side's roster tier: NHL regulars dressed, AHL/junior or try-out players dressed, and the named absentees. It has **no ranking effect**.
2. The pre-season starting goalie is `PROJECTED` until the official lineup or warm-up report. Pre-season goalies often split periods, and a projected goalie may not be printed as "confirmed" (`C-LINEUP-DIFF`).

**Test.** `T-NHL-PRESEASON-GOALIE`: record, over the next 10 pre-season cards, how often the projected starter plays the full game.

<!-- RESEARCH-2026-09-25 -->
## 2026-09-25(b) — NHL reference rates, empty-net structure, preseason and recency (research pass)

**Status.** Reference rates and disclosure (`C-PROMOTION-RECEIPT`: `REFERENCE` / `PROMOTED_PROCESS`). No coefficient. Source: `BASE_RATES_REGISTER.md` §7.2, from `api-web.nhle.com/v1/score/{date}` fetched with curl (n = 1,312 regular-season games, 2025-26), and `RECENCY_AND_REBOUND.md` §7.

**H-R1. Totals.**
- P(total ≤ 5) = 0.427 and P(total ≤ 6) = 0.531; mean 6.25, SD 2.30.
- 24.8% of games reach overtime (9.1% shoot-outs). An overtime or shoot-out winner adds exactly one goal to a regulation tie, so full-game totals of those games are **odd**: P(total = 5) is 0.233 but P(total = 6) is 0.104.
- Consequence: a 2–2 regulation tie always lands Under 5.5; a 3–3 tie always lands Over 6.5.
- A full-game 5.5 or 6.5 total prints the regulation-tie state's mass as its own branch. A regulation-only contract settles on the 60-minute score (`receipts.py settle nhl` prints it).

**H-R2. The puck line is an empty-net market.**
- P(margin ≥ 2) = **0.568** of all games (0.756 of games decided in regulation).
- **73%** of two-goal regulation wins contained an empty-net goal, which was scored in 34.6% of games.
- A −1.5 row names the empty-net branch (lead by one late, goalie pulled, empty-net goal) as explicit mass: it is the modal route to a two-goal margin.
- A +1.5 row names the same branch as its main kill path (G-L1; M10).

**H-R3. Preseason uses preseason rates.**
- 2025 preseason: total **5.68** (n = 104), P(total ≤ 5) 0.567.
- 2026 preseason to 24 Sep: **5.33** (n = 36).
- Both sit about 0.6–0.9 goals below the regular season.
- A preseason card prints the preseason reference, not 6.25. P-503 (DAL 2–0 MIN, Under 5.5 won) fits.

**H-R4. Recency and team scoring (RECENCY §7.2).**
- A team's season scoring rate predicts its next game no better than the league constant (RMSE 1.731 v 1.730). The last game is **40% worse**; half-shrinking to the league mean is best.
- A back-to-back against a rested opponent is −0.20 goals (−0.53, +0.12), n = 253: not distinguishable from zero.
- Team-scoring leans therefore need a named mechanism: goalie, injuries or special teams. Otherwise they belong in the width.

**H-R5. Width benchmark (`C-WIDTH-BENCHMARK`).** Total residual SD **2.29**; margin **2.57** (0.85×: 1.95 and 2.18). P-503's 2.68 and 2.74 were consistent with it.

**H-R6. Settlement and the goalie test.** `receipts.py settle nhl <gameId> --card-goalie-home X` prints:
- the goalies who played, with time on ice;
- the empty-net goals;
- the regulation score.

It supplies `T-NHL-PRESEASON-GOALIE`'s record directly. P-503 replays as "card Jake Oettinger → DID NOT PLAY; R. Poirier 59:29".


<!-- RANK-MODEL-2026-09-25E -->
## 2026-09-25(e) — Rank 1 and Rank 2 in ice hockey

Controls: `RULES_GENERAL.md` §"2026-09-25(e)".

- **TB-1 has no resolution in the NHL.** Out of sample, P(home win) Brier 0.2477 against 0.2503; totals 0.2490 against 0.2502. The anchor stays `BASELINE_P` and the §7.2 population, with goalies (H-R2) and the preseason regime as named departures. `python tools/team_baseline.py predict --league nhl …` prints `TB1_NO_RESOLUTION` for both targets.
- **RM-1 classes a +1.5 puck line with the low-scoring sports** (`hcp_plus_low`, like baseball). It carries **no cushion penalty**: one-goal games are common (§7.2), and the penalty's evidence holds a single hockey row.
- **The −1.5 empty-net branch (H-R3) is unchanged.**
- **Ranking:** by RM-1 q, with the `TOP2_QUALITY` line printed.
