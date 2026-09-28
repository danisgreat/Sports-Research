# Australian rules football analysis rules — dated history to 2026-09-28

**Archived 2026-09-28 (md-only restructure).** These are the dated sections that followed the competition-rules section of `RULES_AFL.md`, moved verbatim. They are the evidence record. The live rules are §0 of `RULES_AFL.md`, and nothing here reinstates a rule that §0 or `CURRENT_RULES.md` §I withdraws.

## September 5 settlement learning — prospective SFA amendment


At the territory→inside-50→chance→conversion chain, distinguish goals+behinds (scoring shots) from all attempted shots, rushed behinds, entry volume and chance quality. Opponent-adjust small current-season samples before treating scoring-shot differential as territorial superiority. AFL men's and AFLW evidence stay separate; a North Melbourne opponent and a Euro-Yroke opponent are not interchangeable exposure tests.


At G20/G20.1, cross high/low opportunity volume with ordinary/poor/hot conversion **for each team** and carry a final-quarter scoring-allocation branch. Geelong's 37 scoring shots overcame poor conversion; Bulldogs–Sydney changed from Sydney +4 after three to Bulldogs +27. Wind/precipitation may change opportunity generation and conversion in opposite directions. A modest Under lean still needs a conditional budget; no generic weather sign overrides it.


A Bulldogs/other opponent win in prose is insufficient if every printed score example has the selected favourite ahead. Include the opposite win/separation family without forcing arbitrary equal weights. Returning forwards receive play/limited/withdrawn states until the final warm-up check; unknown publication time is not proof of an ignored pre-cutoff withdrawal (Taylor Smith, P-289). Candidate C-P293-AFL-VOLUME is untested; no inferred wind or opposition-adjustment coefficient is promoted.


Match identifiers are host-qualified: this audit's Bulldogs–Sydney is AFL `/aflw/matches/8905` but Sydney club `/matches/8907`. AFL `/aflw/matches/8907` is Euro-Yroke–North; AFL `/aflw/matches/8910` is Yartapuulti–Gold Coast. Verify date/participants before reusing any host/ID pairing.




Full evidence and frozen-card comparisons: [September 5 audit](archive/audit_documents_implemented_2026-09-25/COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md).


## September 5(b) settlement learning — P-294–P-305 second continuation


Four AFLW cards settled this pass (`P-292`, `P-293`, `P-298`, plus carried-forward context): three different score textures in one round confirm that AFLW margins cannot be treated as a single distribution shape.


**`P-292` (St Kilda/Euro-Yroke vs North Melbourne) — extreme blowout.** North Melbourne 99, St Kilda 7 (92-point margin), against an Under 89.5 total pick — the total lost by 16.5 points because North Melbourne alone produced a score above the entire combined line. This is the AFLW-specific instance of the favourite-only-blowout branch already named in RULES_NRL_RUGBY.md's kill-path library, now with a second-code confirmation: extends `C-P293-AFL-VOLUME` (opponent-adjusted opportunities versus raw shot differential) with a case where the raw mismatch (undefeated top side vs a struggling bottom side) was itself sufficient signal that was still under-weighted relative to a season-average total line.


**`P-293` (Port Adelaide vs Gold Coast) — extreme low-scoring competitive game.** Gold Coast won 2.5 (17) to 1.8 (14) — a combined total of only 31 points in difficult conditions at Alberton Oval, with the underdog cushion (`Gold Coast +13.5`) covering by winning outright. This is the AFLW mirror of `P-299`/`P-303`'s large-cushion success in FIBA (see `C-PL15-BSK-CUSHION-VS-SPREAD` in LEARNING_REGISTER.md and RULES_BASKETBALL.md) and confirms L-054's conditions-widening treatment: the card's own "difficult conditions" note was correctly not converted into a one-sign automatic total adjustment, and a genuinely low-event game occurred inside the range that treatment allowed.


**`P-298` (Brisbane Lions vs GWS GIANTS) — L-077.** Brisbane, missing 5-6 rotation players including a recognised on-baller (Ally Anderson) and fielding two debutants, still won by 31 points (55-24), clearing `Brisbane -29.5` while `GWS +29.5` was ranked #1 and lost. Brisbane's absence list was real and correctly documented, but the discount applied to Brisbane's ceiling did not condition on GWS's own materially lesser roster depth (GWS themselves missing Goldsworthy and Srhoj, and fielding their own debutant). **New rule:** state the opponent's own roster quality in the same sentence as any personnel-loss discount — a depleted favourite against a weaker opponent is a different state from a depleted favourite against a comparable or stronger one, and the same absence list cannot receive the same numeric discount in both cases without that comparison being made explicit.


**Kill-path library addition (§8.5):**


| Kill path | Defeats | Evidence origin |
|---|---|---|
| A personnel-loss discount applied without comparing the opponent's own roster quality | An underdog cushion ranked above a quality favourite's spread purely on the favourite's absence list | `P-298`; L-077 |
| A raw top-vs-bottom AFLW mismatch (undefeated leader vs struggling/winless side) treated as ordinary variance around a season-average total | A total line set near the season-average combined score in an extreme-mismatch fixture | `P-292` |


Full evidence: [PREDICTION_LOG_COMBINED_2.md, 2026-09-05(b) section](PREDICTION_LOG_COMBINED_2.md#component-import--p-294p-305-second-continuation--2026-09-05b).


## September 6 settlement learning — separate the scoring-shot count from the conversion rate


`P-292` (North Melbourne 14.15 (99) d. St Kilda 1.1 (7); `Under 89.5` **LOSS** at rank #1, total 106) is the AFL/AFLW instance of the same defect that produced `P-294` in rugby league: the total was budgeted as a points figure rather than as **scoring shots × conversion**.


North Melbourne recorded **29 scoring shots** (14 goals, 15 behinds). At a league-typical conversion that is a ~100-point game on its own; St Kilda's 2 scoring shots were almost irrelevant to whether 89.5 was cleared. A card that budgeted only "St Kilda are a low-scoring side, so the total should stay down" was measuring the wrong side of the equation. Under `G20.2` this row is `TAIL_EXPOSED` on North Melbourne's own upper output before St Kilda's floor is considered at all.


**Required from now on, `SFA-AFL`:**


1. **Budget scoring shots and conversion rate as two separate terms.** Never carry a points total forward as a single number. AFLW in particular has a wide conversion band, so a 29-shot game can land anywhere from ~75 to ~115 points.
2. For the tail budget, hold each side's **scoring-shot count** (`S`, goals+behinds) at its second-highest L10 value and its **conversion rate** (`p` = goals/`S`) at its own L10 rate, then convert to **points**, not shots: `points = 6×goals + 1×behinds = S×(1 + 5p)`. **Correction, 2026-09-06(d):** the original wording here ("conversion rate ... print the implied total") never converted shot count to points, which silently drops behinds — applied to `P-292`'s actual 29 shots (14 goals, 15 behinds), a shots-only or naive shots-times-conversion reading understates the total; the correct formula, `29×(1+5×14/29) = 99`, matches the real total exactly.
3. A one-sided AFLW fixture is *more* dangerous for an `Under`, not less: the dominant side's inside-50 count compounds while the weaker side's floor is already near zero and cannot compress further. State this asymmetry explicitly whenever the expected margin exceeds ~40 points.


`P-298` (Brisbane 7.13 (55) d. GWS 3.6 (24); `Under 95.5` **WIN** at rank #2, `GWS +29.5` **LOSS** at rank #1) is the contrasting case and the origin of `L-077`. Brisbane's 20 scoring shots converted at 7/20 — a *low* conversion rate — which is precisely why the total stayed under despite a 31-point margin. Same structure as `P-292`, opposite conversion outcome. That is the argument for splitting the terms rather than modelling points directly.


### Kill-path library addition (§8.5)


| Kill path | Defeats | Evidence origin |
|---|---|---|
| **Scoring-shot compounding in a mismatch** — the dominant side's inside-50 and shot count rise together while the weaker side is already at its floor | A full-game `Under` justified by the weaker side's low scoring | `P-292` (106 against `Under 89.5`) |
| **Low-conversion suppression** — a high scoring-shot count converts poorly and holds the total down despite a comfortable margin | An `Over` justified by territory/inside-50 dominance alone | `P-298` (7.13 — 20 shots, 55 points) |




### Cross-sport gates instantiated here (v3.7)


| Gate | Sport-native instantiation |
|---|---|
| `G10.2` settlement-source pre-registration | AFL/AFLW settle from the AFL official match report and its host-qualified event ID per `L-071`; name the exact match record at freeze. |
| `G14.2` coaching / bench / rotation record | Record the senior coach, the named emergencies/medical substitute, and the AFL/AFLW substitution provision from §9, plus any confirmed managed-rest signal. Official club team announcements (released 60 minutes pre-bounce) or accredited AFL Media reporting verified under Control `S-1 Rev 2` qualify as `PROJECTED_BEAT_VERIFIED`, satisfy `G14.2`, and do not block Rank #1. |
| `G20.2` distributional tail audit | Derive tail and boundary mass from the **same frozen AFL/AFLW scoring distribution**, explicitly separating scoring-shot opportunity from conversion and conditioning on role/selection/bench, venue/weather and quarter-state exposure. Historical second-highest-L10 scoring-shot constructions are superseded as active gates. |
| `G21.1` exact target geometry | Map every supplied target to its exact settlement event and derive WIN/PUSH/LOSS from the same frozen sport-native PMF/CDF or coherent branch mixture. Historical path-count/category labels have no mandatory ordinal effect. |
| `G26.1` no universal separation floor | Reference rates and `rank_gap` are descriptive only. **No 40–60% or other pooled probability band can disqualify Rank #1.** Rank from exact marginal likelihood plus robustness/evidence uncertainty. |


**Pre-issue checklist additions (this sport):** settlement endpoint named per row; coaching/bench/rotation record for both sides with missingness codes; tail-budget sums printed against every total line; path-geometry class and `N` printed for every total and phase-total row; separation-floor result stated for Rank #1.


Full narrative and evidence: [`archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md`](archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md). Controlling gate text: [`RULES_GENERAL.md` §13](RULES_GENERAL.md).


## September 5 implementation after freeze confirmation


**ACTIVE REQUIRED PROCESS — MDS-2026.09.05-v3.6 / L-068–L-072.** Separate opportunity volume from conversion, adjust short windows for opponents, and evaluate each side’s final-quarter separation path. Weather informs the opportunity/conversion chain rather than applying a blanket Under adjustment. Recheck final warm-up availability and preserve its publication timing.


At final delivery, record the preferred total direction for each exact target, the strongest evidenced failure path for ranks #1 and #2, and whether both can win under the stated joint scenario. Rank by supported marginal likelihood; do not promote an opposite pick solely to manufacture one O/U win. At settlement, keep all issued wins/losses, including defective reasoning, in the applicable historical scorecard and review failed #1/#2 and preferred totals.


[Eligibility policy](PERFORMANCE_ELIGIBILITY_POLICY.md): non-live history is user-confirmed frozen pre-game; explicit live-issued views stay separate. These process repairs are implemented now. Numerical weights and predictive-lift claims need a later frozen comparison; historical origin games do not supply those completions.


## 2026-09-06(f) — settlement and retrospective addendum


P-292/P-294 cross-sport contrast and P-315 reinforce a favourite-driven high-total path even when the opponent is weak. P-298/P-315 require role/replacement and opponent context for absences, not a flat injury discount. P-315 territory reversed by quarter; no unverified wind-to-end cause is asserted. Preserve points = scoring shots + 5 × goals, and audit winning thresholds separately from inaccurate score corridors. These are existing analytical controls, not new ordinal weights.


Full frozen ranks, actual drivers, knowability and smallest fixes: [PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md). Reinforcement only; METHOD v4.0 remains controlling and no new predictive weighting is promoted.


## 2026-09-09 — cross-sport controls instantiated here (`G-L1`, `G-L2`, `G-L7`, `G-L8`)


No AFL/AFLW card was issued in the `P-333`–`P-344` cohort. The four cross-sport requirements adopted from it (`RULES_GENERAL.md` §§16.5(a)–(d), full evidence in `PREDICTION_LOG_COMBINED_3.md` §"2026-09-09") apply to this sport from the next card, instantiated as follows. All four are **disclosure/retrieval requirements — no fitted weight, no ordinal bar** (`L-087`).


| Cross-sport control | AFL/AFLW instantiation |
|---|---|
| **`G-L1` §16.5(a)** — enumerate outcome-state families with explicit mass | Enumerate the **margin families** in native units (favourite by 40+ / 20–39 / 6–19 / within a goal / underdog win) and the **total families** in points, each with a probability mass summing to 1. Every kill path in the §8.5 library that has current specific evidence must appear as one of those weighted branches. Print a **representative Rank-#1 final score** in points and check it simultaneously against the line, the total and any team-total row — remembering `points = scoring shots + 5 × goals`, so a representative score must be stated as a goals/behinds pair, not a bare number. |
| **`G-L2` — declared uncertainty model** | State the prior and scenario probabilities. Symmetric uncertainty around an unchanged prior affects width; hierarchical shrinkage or asymmetric scenarios may change both mean and variance. Regenerate all dependent probabilities; unsupported directional adjustments remain prohibited. SCORING_AND_VALIDATION section 5 controls. |
| **`G-L7` §16.5(c)** — aggregate-to-disaggregate retrieval | Do not let a season average or a "last N" summary carry directional weight while the **per-game log** is available. Print the **round-by-round record** for the decision-relevant window — score, scoring shots, goals/behinds split, and for the decision-driving players their **game time and goal/disposal output per match** — and state whether a run of poor or strong results is front-loaded, back-loaded or uniform. Quantify **every top-three goalkicker and every player above roughly 75% game time on both sides**; a player carried as a bare name in a "leaders include…" phrase is `AGGREGATE_ONLY` and the margin/total rows that depend on the team's scoring ceiling are capped. |
| **`G-L8` — distribution coherence** | Derive each total/spread probability from the exact joint PMF/CDF and settlement endpoint, with push mass. Absolute normalised distance does not order probabilities across different distributions. No missing width or realised result justifies an invented probability. |


## 2026-09-11 — cross-sport controls instantiated here (`G-L9`, `G-L10`, `G-L11`, §16.8)


No AFL/AFLW card in the `P-345`–`P-371` import. The three disclosure requirements and the completeness block adopted from it ([`RULES_GENERAL.md` §§16.5(e)–(g), §16.8](RULES_GENERAL.md)) apply from the next card. AFL is `PRIMARY_SCORED`, so this is where they will first count.


| Control | AFL / AFLW instantiation |
|---|---|
| `G-L9` §16.5(e) | A 0.70 line or total row itemises its 0.30 across the named paths — goal-kicking inaccuracy (goals v behinds), a late key-position out, wet-weather low scoring, the underdog winning the clearance battle. |
| `G-L10` §16.5(f) | A favourite line + Over pair is positively coupled when the favourite's scoring drives the margin; an underdog line + Under pair is positively coupled through a contested, low-possession game. Print the sign. |
| `G-L11` §16.5(g) | Goal-kicking accuracy over a few matches (goals ÷ scoring shots) is a small-sample proportion — print its standard error before it moves a centre. |
| §16.8 | Teams are named before the match and finalised before the bounce; `NOT_RETRIEVED` after publication is a `RETRIEVAL_MISS`. |




## 2026-09-12 algorithm corrections and retrospective integration


Apply section 16.9 to joint goals/behinds, total points, margins and quarter targets. A high-scoring favourite separation and a slow close contest both remain possible. Confirm both selected sides, interchange/substitute rules for the competition and season, late changes and coaches. No new AFL result was settled in this pass: these are transferable arithmetic/provenance repairs, not an AFL-specific empirical improvement. Count event clusters for any future total-family comparison.


For every supplied row, use exact target probabilities from a coherent joint distribution; handle push/void/censoring explicitly, avoid overlapping adverse-state counts, and report JOINT_UNQUANTIFIED with bounds if the dependence is not specified. Separate issued-time participant capture, later recovered evidence, source accuracy by field, observed mechanism, and unverified causal interpretation. Keep one preferred O/U direction per distinct target and report the top-two denominator honestly. Shared correction and methodology sources (`audit_2026-09-12/rule_corrections.md`, not present in this repository). All current log observations remain learning-only and not performance-eligible.




## 2026-09-15(b) settlement learning — `P-373`–`P-423` import


Learning-only; disclosure/process changes only — no coefficient or ordinal bar (`L-087`). Evidence and tables: [`PREDICTION_LOG_COMBINED_3.md` §"2026-09-15(b)"](PREDICTION_LOG_COMBINED_3.md). Cross-sport rule: `RULES_GENERAL.md` §16.10 (`G-L12` margin centre/width; fixture identity; official-record derivative settlement).


**Cards:** P-388 (Fremantle 120–106 Geelong; Geelong +11.5 LOST), P-396 (Brisbane 144–91 Adelaide; Adelaide +21.5 and Under 188.5 LOST). Finals re-verified at ESPN `australian-football/afl`.


- **P-396:** 65 scoring shots against a central ~50 — the miss was shot volume, not conversion; the high-shot branch (`AF-B4`, control 9) existed but carried too little mass, and it killed both top rows together (`G-L10`).
- **P-388:** the high-shot / upper-conversion family was printed and under-massed (`G-L9`).
- **`G-L12` instantiation:** finals margins take their centre from the scoring-shot differential chain, not from a shrink toward a close game; print P(favourite by more than the line) from the shot × conversion families.


## 2026-09-16 — cross-sport controls instantiated here (`G-L13`, `G-L14`, `G-L15`, disruption facts)


No AFL card was settled this pass. Rules: `RULES_GENERAL.md` §16.11.
- **`G-L13`:** quarter scores, scoring shots and team selections come from the raw AFL match centre or ESPN `australian-football/afl` JSON, never from a summary.
- **`G-L14`:** a quarter or half target names its settling record. ESPN quarter line scores were verified for finals in 2026-09-15(b).
- **`G-L15`:** label total rows forced-pair or free. Rugby league/AFL forced-pair preferred sides went 2 of 3 in `P-345`–`P-423`.
- **Disruption facts:** record medical-substitute activations and concussion withdrawals, with the quarter and the margin at the time.


## 2026-09-17 — cross-sport controls instantiated here (`G-L17`–`G-L20`)


No AFL card in this import. **`G-L17`:** when a margin row and a total row share one game-shape thesis, print `P(¬R1 ∧ ¬R2)` and name the state (usually a scoring-shot surge that breaks the margin and the total together). **`G-L18`:** print each side's own score marginal before ranking a match total. **`G-L19`:** AFL permits a drawn home-and-away match — a winner family must carry draw mass. **`G-L20`:** a current-season same-venue meeting that already cleared a line gets explicit mass.


Evidence and cohort audit: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17"](PREDICTION_LOG_COMBINED_4.md); rules in `RULES_GENERAL.md` §16.12.


## 2026-09-17(b) — cross-sport controls instantiated here (`G-L21`–`G-L24`)


**G-L24 in AFL:** derive the exact signed-margin distribution under the competition endpoint, including draw, key-value and push masses. Pooled league bands are uncertain references, not mandatory matchup probabilities or rank prohibitions. Missing pooled bands do not invalidate a complete conditional joint distribution. **`G-L21`:** a 'wet weather, low-scoring, favourite controls it' thesis routinely carries a line, an Under and a team total at once — print `P(all fail)` with bounds. **`G-L22`:** line and total arrive as forced pairs; report preferred sides. **`G-L23`:** inside-50s, clearances and the quarter-by-quarter record are the process fields; sub/injury exits with the clock are the disruption facts.


Evidence and cohort audit: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17(b)"](PREDICTION_LOG_COMBINED_4.md); rules in `RULES_GENERAL.md` §16.13; bands and base rates in [`BASE_RATES_REGISTER.md`](BASE_RATES_REGISTER.md).


## Current model implementation — 2026-09-17


Use METHOD v4.2's six-field object and SCORING_AND_VALIDATION for exact outcome/push scoring, event-level comparison, descriptive recency and declared hierarchical uncertainty. MODEL_IMPLEMENTATION_RECIPES supplies this sport's retained model scope and endpoint design. Forecast probabilities come from the joint model; pooled base rates are uncertain context, not universal limits. Numeric row caps disconnected from that model, absolute-distance probability ordering and retrospective tail reweighting are withdrawn. No fitted coefficient or predictive improvement is claimed. New cards freeze the method/control hash; existing cards keep their issued versions.


## 2026-09-19 — recency/rebound evidence, debutant gate and the top-O/U review


Cross-sport: [`RECENCY_AND_REBOUND.md`](RECENCY_AND_REBOUND.md) control `R-1`; source controls `S-1` (social identity) and `S-2` (press conferences) in `SOURCES.md` §"2026-09-19"; enhanced-failure trigger in `METHOD.md` §7.


**`R-1` applies qualitatively; AFL magnitudes are `NOT_YET_DERIVED`.** Note the finals-specific caution already recorded: `P-459` carried a total centre near 184 into a game that produced 154, in dry conditions with no weather mechanism. Home-and-away scoring rates are a poor prior for finals.


**Press-conference and selection material (`S-2`).** AFL clubs publish selected teams, ins/outs and coach commentary on official domains, and `P-459` used them correctly — it is the only card in that cohort with confirmed participants for both sides. Continue treating stated tactical intent as branch-motivating, not centre-moving.


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — market-independent totals/line addendum


**Source priority:** AFL official match centre/team sheets/injury information, club releases and BOM/appropriate government weather. Betting/fantasy content is prohibited predictive evidence.


Use a joint team-score/margin distribution driven by current personnel, venue dimensions/home state, weather, rest/travel and stable process statistics such as scoring opportunities/inside-50/clearance/shot-conversion components when sourced and definition-stable. Supplied totals/lines cannot anchor the score centre.




<!-- ALL-SPORTS-AUDIT-LIVE-RULE-CLEANUP-2026-09-21-CR3 -->
## 2026-09-21 — all-sports audit live-rule cleanup — CR-2026.09.21-3


Current prospective override. Retain scoring-shot opportunity versus conversion, role/selection/bench, venue/weather, quarter-state exposure and three-source finality. Withdraw pseudo-tail order-statistic constructions, path-count ranking shortcuts, universal probability-band top-slot rules, normalized-distance ordering and one-result response rules. Build one coherent AFL/AFLW joint outcome distribution before querying targets; do not invent precise probabilities without a fitted/calibrated distribution.

<!-- SETTLED-ROW-REVIEW-2026-09-25D -->
## 2026-09-25(d) — track record from the full settled-row review

**Track record (`C-TRACK-RECORD`).** 10 decisions from 4 cards: won **30%** at a mean stated 0.662. The gap is −0.36, with a card-cluster interval of [−0.60, −0.10]: **over-confident**. AFL cards are labelled **`NO_DEMONSTRATED_SKILL`**: the evidence grade is capped at LOW and the departure ledger is required.

- **Underdog cushions (+k.5): 0/3.** `C-PLUS-CUSHION` applies.
- **Missing reference.** There is no AFL population reference yet (`BASELINE_P: NOT_YET_DERIVED`). Deriving an AFL margin and total population from the field owner is the first step to an honest baseline.

Source: `research/settled_rows_2026-09-25/README.md`. The figures are hindsight on the framework's own cards, descriptive, and use card-cluster intervals. None is a coefficient (`L-087`). Controls: `RULES_GENERAL.md` §"2026-09-25(d)".


<!-- RANK-MODEL-2026-09-25E -->
## 2026-09-25(e) — the first AFL population reference, the team baseline and the ranking model

Controls: `RULES_GENERAL.md` §"2026-09-25(e)". Evidence: `research/team_baseline_2026-09-25e/README.md`; `BASE_RATES_REGISTER.md` §7.7.

This implements the 2026-09-25(d) to-do ("deriving an AFL margin and total population from the field owner is the first step").

**Record at Rank 1/2, NFL, AFL and NRL together: 12 W / 20 L,** the worst of any group. The losses were mostly underdog cushions and totals. AFL stays `NO_DEMONSTRATED_SKILL`.

### (a) Sources

- **ESPN AFL scoreboard** `…/australian-football/afl/scoreboard?dates=YYYYMMDD`: one date per call; season type 2 = home-and-away.
- **ESPN team schedule** `…/australian-football/afl/teams/{id}/schedule?seasontype=2`: the TB-1 lane (`python tools/team_baseline.py predict --league afl …`).
- **Unchanged:** the settlement sources.

### (b) Reference rows (AFL 2025 / 2026, n = 207 each)

| Row | 2025 | 2026 |
|---|---:|---:|
| Home win | 0.565 | 0.585 |
| Draw | 0.005 | 0.015 |
| Total mean (SD) | 168.6 (29.8) | 178.2 (29.1) |
| Total, 10th / 50th / 90th percentile | 132 / 168 / 208 | 142 / 181 / 216 |
| Home margin | +6.0 | +7.1 |
| Margin SD | 42.5 | 40.8 |
| P(\|m\| ≤ 12) | 0.30 | 0.28 |
| P(\|m\| ≤ 24) | 0.48 | 0.47 |
| TB-1 residual width, total / margin | 29.8 / 36.9 | 29.1 / 36.7 |

These replace `NOT_YET_DERIVED` for `BASELINE_P`, the reference row and the reference width.

### (c) Reasoning

1. **TB-1 is the anchor for sides and margins.**
   - It has the strongest resolution of any league: P(home win) Brier 0.202 against 0.249 (2026, chosen on 2025).
   - **Totals have no resolution** (0.248 v 0.255, below the 3% bar). Totals anchor on the 2026 population row.
2. **Cushions.** The TB-1 underdog covered:

   | Cushion | Cover rate (2025–26) |
   |---|---|
   | +6.5 | 0.38–0.43 |
   | +12.5 | 0.48–0.51 |
   | +18.5 | 0.56–0.59 |
   | +24.5 | 0.60–0.62 |

   A cushion stated above its rate by more than 0.05 needs a receipted mechanism on the favourite's side (`C-PLUS-CUSHION`). Otherwise RM-1 flips it. The record's AFL cushions were 0/3.
3. **Finals.** TB-1 is a regular-season model. For finals, print `TB1_FINALS_CONTEXT` and name the finals-specific departures: venue, rest days, and the weather at the ground.
