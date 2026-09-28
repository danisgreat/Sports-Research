# American football analysis rules — dated history to 2026-09-28

**Archived 2026-09-28 (md-only restructure).** These are the dated sections that followed the competition-rules section of `RULES_AMERICAN_FOOTBALL.md`, moved verbatim. They are the evidence record. The live rules are §0 of `RULES_AMERICAN_FOOTBALL.md`, and nothing here reinstates a rule that §0 or `CURRENT_RULES.md` §I withdraws.

## September 5 cross-sport process inheritance


L-068–L-071 in RULES_GENERAL §12 apply to this SFA through quarter/drive score budgets, actual personnel snaps and special-team scoring. Validate arithmetic, propagate failed evidence caps, make both sides’ material winning states evaluable and keep source identity/field definitions explicit. No new completed game in this sport was available in the current cohort; no sport-specific empirical improvement or parameter change is claimed.


## September 6 settlement learning — cross-sport gates instantiated


No American-football card was settled in the `P-294`–`P-305` cohort. The v3.7 gates are instantiated here so that NFL, college, UFL and CFL cards carry the same disclosures.


**Sport-native tail example.** An American-football total is a **drive-count × points-per-drive** product, and the two terms move in opposite directions in the two states that matter most: a run-heavy blowout *reduces* drive count while raising points-per-drive, and a shootout raises both. **Define "drive" and "drives allowed" consistently first** (a possession that starts on a turnover or a short field is a different scoring-rate environment than one starting after a punt from your own 20; use the same definition for both sides' L10 figures, and record it). The tail budget is computed on both terms, not on a points total: hold each side's second-highest L10 points-per-drive against the opponent's median drives allowed, then repeat with the drive counts swapped, and print both. **Correction, 2026-09-06(d):** the original QB-only framing for `G14.2`'s bench analogue was too narrow — offensive- and defensive-line rotation and unit-level substitution matter for drive count and points-per-drive at least as much as the backup quarterback; record both. The historical CFL failure recorded at `P-150` (Montreal `-6.5` and `Under 60.5` both lost to a 44–28 Winnipeg possession-control win) is the origin case for treating possession share as a scoring-rate input rather than a game-script narrative.


**Special-teams and defensive scoring** are a separate additive term with their own rate and belong in the tail budget explicitly — a defensive/special-teams touchdown adds points without consuming a drive, so it breaks the drive-count model and is the single most common way a well-reasoned `Under` fails.


**Path geometry.** A first-quarter or first-half `Over` at a low threshold is `UNION_LOW_THRESHOLD` with `N` = expected drives in the interval. A full-game `Under` is `INTERSECTION_CONSTRAINT` across four quarters plus the overtime branch, which in NCAA and NFL formats carries a materially different scoring rate under `G22`.




### Cross-sport gates instantiated here (v3.7)


| Gate | Sport-native instantiation |
|---|---|
| `G10.2` settlement-source pre-registration | NFL and NCAA settle from the official league/NCAA box score; ESPN's `football/<league>/summary` is the structured corroboration lane. UFL/CFL need their own named official endpoint. |
| `G14.2` coaching / bench / rotation record | Record the head coach and coordinators where a change has occurred inside five games, the inactives list, and the QB depth chart — the bench-depth analogue in this sport is almost entirely the backup quarterback. 90-minute inactives, starter notices, and workload limits verified across accredited beat reporters or official team media releases under Control `S-1 Rev 2` qualify as `PROJECTED_BEAT_VERIFIED`, satisfy `G14.2`, and do not block Rank #1. |
| `G20.2` distributional tail audit | Derive tail and boundary mass from the **same frozen American-football joint score distribution**, including drive/play opportunity, QB/offensive-line/skill availability, EPA/success, turnover and field-position branches, pace/game state and overtime/rules era. Historical order-statistic stress sums are superseded as active gates. |
| `G21.1` exact target geometry | Map every supplied target to its exact settlement event and derive WIN/PUSH/LOSS from the same frozen sport-native PMF/CDF or coherent branch mixture. Historical path-count/category labels have no mandatory ordinal effect. |
| `G26.1` no universal separation floor | Reference rates and `rank_gap` are descriptive only. **No 40–60% or other pooled probability band can disqualify Rank #1.** Rank from exact marginal likelihood plus robustness/evidence uncertainty. |


**Pre-issue checklist additions (this sport):** settlement endpoint named per row; coaching/bench/rotation record for both sides with missingness codes; tail-budget sums printed against every total line; path-geometry class and `N` printed for every total and phase-total row; separation-floor result stated for Rank #1.


Full narrative and evidence: [`archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md`](archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md). Controlling gate text: [`RULES_GENERAL.md` §13](RULES_GENERAL.md).


## September 5 implementation after freeze confirmation


**ACTIVE REQUIRED PROCESS — MDS-2026.09.05-v3.6 / L-068–L-072.** Apply the shared native-score arithmetic, final-role/exposure gate, both-side score/separation budgets and source-field checks to drives, possessions and quarterback/line roles. This audit supplies no new American-football-specific coefficient evidence.


At final delivery, record the preferred total direction for each exact target, the strongest evidenced failure path for ranks #1 and #2, and whether both can win under the stated joint scenario. Rank by supported marginal likelihood; do not promote an opposite pick solely to manufacture one O/U win. At settlement, keep all issued wins/losses, including defective reasoning, in the applicable historical scorecard and review failed #1/#2 and preferred totals.


[Eligibility policy](PERFORMANCE_ELIGIBILITY_POLICY.md): non-live history is user-confirmed frozen pre-game; explicit live-issued views stay separate. These process repairs are implemented now. Numerical weights and predictive-lift claims need a later frozen comparison; historical origin games do not supply those completions.


## 2026-09-06(f) — settlement and retrospective addendum


P-309 Under won although both printed team-score corridors missed low. Separate offensive yards/drives, non-offensive touchdowns, field position and finishing. Gardner-Webb had 438 yards despite scoring 13; do not label the offence ineffective solely from points. The recorded storm risk was knowable, its exact delay and late interception were not. No weather coefficient or universal Under rule.


Full frozen ranks, actual drivers, knowability and smallest fixes: [PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md). Reinforcement only; METHOD v4.0 remains controlling and no new predictive weighting is promoted.


## 2026-09-09 — cross-sport controls instantiated here (`G-L1`, `G-L2`, `G-L7`, `G-L8`)


No American-football card was issued in the `P-333`–`P-344` cohort. The four cross-sport requirements adopted from it (`RULES_GENERAL.md` §§16.5(a)–(d), full evidence in `PREDICTION_LOG_COMBINED_3.md` §"2026-09-09") apply to this sport from the next card. All four are **disclosure/retrieval requirements — no fitted weight, no ordinal bar** (`L-087`).


| Cross-sport control | American-football instantiation |
|---|---|
| **`G-L1` §16.5(a)** — enumerate outcome-state families with explicit mass | Enumerate the **margin families** (favourite by 17+ / 9–16 / 4–8 / within a field goal / underdog win) and the **total families** in points, each with an explicit mass summing to 1. Because scoring is quantised in 3s and 7s, state the families as **drive-count × points-per-drive** combinations rather than a smooth corridor, and locate the supplied line against the modal family. Every current-evidence §8.5 kill path — including **non-offensive touchdowns, special-teams scores and turnover-driven short fields**, which `P-309` showed can decouple points from yardage — must appear as a weighted branch, not a sentence. Print a representative Rank-#1 final score and check it against the spread, the total and any team-total row. |
| **`G-L2` — declared uncertainty model** | State the prior and scenario probabilities. Symmetric uncertainty around an unchanged prior affects width; hierarchical shrinkage or asymmetric scenarios may change both mean and variance. Regenerate all dependent probabilities; unsupported directional adjustments remain prohibited. SCORING_AND_VALIDATION section 5 controls. |
| **`G-L7` §16.5(c)** — aggregate-to-disaggregate retrieval | Do not let a season passer rating, a yards-per-game figure or a "last N games" summary carry directional weight while the **game log and snap counts** are available. Print the **per-game log** for the decision-relevant window and state whether a run is front-loaded, back-loaded or uniform. For a returning player, print the **practice-participation ladder** (DNP / limited / full, by day) — the direct analogue of the rehab pitch-count ladder that decided `P-335`. Quantify **every skill player above roughly 50% offensive snaps**; a name in a "leaders include…" phrase without a number is `AGGREGATE_ONLY` and caps the dependent total/margin rows. |
| **`G-L8` — distribution coherence** | Derive each total/spread probability from the exact joint PMF/CDF and settlement endpoint, with push mass. Absolute normalised distance does not order probabilities across different distributions. No missing width or realised result justifies an invented probability. |


## 2026-09-11 — cross-sport controls instantiated here (`G-L9`, `G-L10`, `G-L11`, §16.8)


No American-football card in the `P-345`–`P-371` import. From the next card ([`RULES_GENERAL.md` §§16.5(e)–(g), §16.8](RULES_GENERAL.md)):


| Control | American-football instantiation |
|---|---|
| `G-L9` §16.5(e) | Itemise the complement of a spread across the key-number families (a field goal, a touchdown, 10) and the named paths — turnover margin, a backup quarterback, special-teams scores, late garbage-time touchdowns. |
| `G-L10` §16.5(f) | A favourite spread + Over pair is positively coupled when the favourite's offence creates the margin; an underdog spread + Under pair is positively coupled through a slow, defensive game. Print the sign. |
| `G-L11` §16.5(g) | Red-zone touchdown rate, third-down conversion and turnover rates over three or four games are small samples; print their standard error before they carry direction. |
| §16.8 | Inactive lists are published before kick-off; `NOT_RETRIEVED` after publication is a `RETRIEVAL_MISS`. |




## 2026-09-12 algorithm corrections and retrospective integration


Apply section 16.9 to joint possessions, touchdowns/field goals, team totals, margins and overtime scope. Garbage-time pace, late stops and trailing-team aggression can change dependence in either direction. Record active/inactive lists, projected versus confirmed starters, depth/reserves and coaches separately. Completion percentage has attempt exposure; points per drive and yards per play need different uncertainty models. No new American-football result was settled in this pass; validate any predictive weighting prospectively.


For every supplied row, use exact target probabilities from a coherent joint distribution; handle push/void/censoring explicitly, avoid overlapping adverse-state counts, and report JOINT_UNQUANTIFIED with bounds if the dependence is not specified. Separate issued-time participant capture, later recovered evidence, source accuracy by field, observed mechanism, and unverified causal interpretation. Keep one preferred O/U direction per distinct target and report the top-two denominator honestly. Shared correction and methodology sources (`audit_2026-09-12/rule_corrections.md`, not present in this repository). All current log observations remain learning-only and not performance-eligible.




## 2026-09-15(b) settlement learning — `P-373`–`P-423` import


Learning-only; disclosure/process changes only — no coefficient or ordinal bar (`L-087`). Evidence and tables: [`PREDICTION_LOG_COMBINED_3.md` §"2026-09-15(b)"](PREDICTION_LOG_COMBINED_3.md). Cross-sport rule: `RULES_GENERAL.md` §16.10 (`G-L12` margin centre/width; fixture identity; official-record derivative settlement).


**Cards:** P-376 (49ers +3.5 WIN, won 27–7), P-412 (Falcons +6.5 LOSS by exactly 7), P-413 (Colts +3.0 and Under 48.5 LOSS, Ravens 41–23), P-414 (Texans +1.5 and Under 44.5 LOSS, Bills 36–31), P-422 (Broncos +2.5 LOSS, Chiefs 31–10). Potential winners 4 of 5. Rank #1 1 W / 4 L — every loss an underdog cushion whose favourite won by 5–21.


### What went right (keep it)
- Winner identification (4 / 5) and the injury/inactive ladders (P-413, P-414, P-422).
- P-413 printed the push mass at exactly 3 (8%).


### What went wrong, linked to earlier lessons
1. **Uncertainty put into the centre.** Control 16 ("new-regime uncertainty is two-sided") was cited, but P-413 (BAL +1.3), P-414 (BUF +0.7) and P-422 (KC +1.0) all centred within ~1 point of pick'em beside 53–56% winner labels. Actual margins +18, +5, +21 → `G-L12`.
2. **Margin width too narrow.** ~10.5 points against a published NFL spread-to-result SD of about 13.9 (Stern 1991) — both tails under-massed.
3. **A hand-picked window as the prior.** P-413 used the Colts' first 10 games of 2025 with a healthy quarterback (57.6% scoring possessions) — `L-011`/`G17`.
4. **One thesis, two rows.** P-413 and P-414 ranked an underdog cushion and an Under on the same "controlled, defensive game" idea; both pairs lost together (`G-L10`).
5. **No margin table at all** on P-412 (23-line card), which then lost at exactly 7.


### Structural control additions
17. **Margin prior and width.** Print the margin prior (prior-season point differential adjusted for quarterback status) and a width no narrower than the published residual SD unless the card shows why; Week 1 widens, it does not centre toward zero (`G-L12`).
18. **Key numbers.** Every NFL handicap row prints the exact masses at 3 and 7 from its margin table; a card without a margin table caps its handicap rows at `FORCED RANK`.
19. **Prior-season unit ratings in a new season are width.** A defence's prior-season rating may not set both a margin compressor and a total suppressor without current-season evidence (P-414: 67 points).


### Kill-path additions
| Kill path | Defeats | Origin |
|---|---|---|
| Favourite separation after a near-pick'em centre (new QB/HC/OC held as centre shift) | Small underdog cushions | P-413, P-414, P-422 |
| Exactly-7 result | +6.5 cushions | P-412 |


## 2026-09-16 settlement learning — external variant C′ facts verified (`P-412`, `P-413`, `P-414`, `P-422`)


Learning-only; disclosure only (`L-087`). Cross-sport rules: `RULES_GENERAL.md` §16.11. Facts verified at the ESPN `football/nfl` summaries on 2026-09-16.


### What the verified box scores add
- **P-412 (Steelers 20–13 Falcons).** T.J. Watt's **35-yard interception-return TD at Q4 14:05** turned 13–10 into 20–10; Atlanta's later field goal left the final margin at exactly 7. Cooper Rush went 12/22 for 143 yards with **2 INT and 4 sacks**. The +6.5 was decided by a non-offensive score under a backup quarterback.
- **P-413 (Ravens 41–23 Colts).** Baltimore gained 506 yards at 7.9 a play. Jackson went 17/25 for 324 yards; Henry ran 24 times for 144 yards and 3 TD; Flowers scored on a 54-yard catch. This was the intact-star explosive branch.
- **P-414 (Bills 36–31 Texans).** Buffalo gained 409 yards on 52 plays (7.9 a play) with 0 turnovers; Houston committed 2.
- **P-422 (Chiefs 31–10 Broncos).** Denver gained 176 yards at 3.7 a play; Nix went 17/28 for 131 yards with 1 INT and 4 sacks. Walker ran 23 times for 173 yards, including a 60-yard TD. A 21-point cover inside a 41-point Under.


### 2025 regular-season reference base rates (`REFERENCE_BASE_RATE`, descriptive)
Computed 2026-09-16 from ESPN `scoreboard?dates=2025&seasontype=2&week=1…18` plus `summary` `scoringPlays` (272 completed games; 14 overtime games; 1 tie).


| Quantity | Value |
|---|---|
| Final margin exactly 3 | 15.1 % |
| Final margin exactly 7 | 9.6 % |
| Margin 0–6 / 7–13 / 14+ | 40.1 % / 24.6 % / 35.3 % |
| Mean / median absolute margin | 11.15 / 8 |
| Mean total points (SD) | 46.0 (13.8) |
| Non-offensive TDs (interception, fumble, punt, kickoff and blocked-kick returns) | 59 — **0.217 a game; at least one in 18.8 % of games** |


Definitions follow ESPN `scoringPlays[].type.text`; "Sack Opp Fumble Recovery" (12) and safeties (10) are excluded. These are league-wide unconditional rates. A card still conditions on its own game (quarterback, turnover and sack rates), and the rates are width references, not coefficients.


### Structural control additions
20. **Non-offensive score branch.** Any handicap row within one score of the printed centre carries "defensive or special-teams TD" as an explicit branch mass. Anchor it on the reference rate above, and adjust only with named evidence (backup quarterback, sack or turnover rates). Origin: P-412; C′ candidate `C-P407-23-AF-NONOFFENSIVE-SPREAD`.
21. **Favourite covers inside the Under.** When a handicap and a total are both in the top two, print P(favourite covers ∧ Under) and P(underdog covers ∧ Over) from the joint margin × total table. Origin: P-422 (KC by 21, total 41) and P-412 (PIT by 7, total 33); C′ candidate `C-P407-23-AF-FAVOURITE-UNDER-SEPARATION`.


Control 18 now cites the reference key-number masses above as its default when no current-season table exists.


### Kill-path additions
| Kill path | Defeats | Origin |
|---|---|---|
| Backup-QB interception returned for a TD | Underdog cushion at 6.5–7.5 | P-412 |
| Favourite run game + opponent offence under 4 yards a play | Underdog cushion, while the Under also wins | P-422 |


## 2026-09-17 — cross-sport controls instantiated here (`G-L17`–`G-L20`)


No American-football card in this import. **`G-L17`:** `P-413` and `P-414` are the origin recurrences — an underdog cushion and an Under built on one 'controlled game' thesis; print `P(¬R1 ∧ ¬R2)` and name the state, alongside control 21's favourite-covers-inside-the-Under branch. **`G-L18`:** print each side's own points marginal before ranking a game total. **`G-L19`:** regular-season ties are possible (one occurred in the 2025 reference season, 272 games); a winner family that sums to 1 over two teams is incomplete. **`G-L20`:** a current-regime same-venue comparable that already cleared the line gets explicit mass.


Evidence and cohort audit: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17"](PREDICTION_LOG_COMBINED_4.md); rules in `RULES_GENERAL.md` §16.12.


## 2026-09-17(b) — cross-sport controls instantiated here (`G-L21`–`G-L24`)


**G-L24 in AMERICAN FOOTBALL:** derive the exact signed-margin distribution under the competition endpoint, including draw, key-value and push masses. Pooled league bands are uncertain references, not mandatory matchup probabilities or rank prohibitions. Missing pooled bands do not invalidate a complete conditional joint distribution. NFL 13.9 is a historical residual benchmark, not a width floor. **`G-L21`:** `P-413`/`P-414` are already the origin recurrences; extend the printed failure mass past the top two whenever a cushion, an Under and a team total all rest on one 'controlled game' thesis. **`G-L22`:** the supplied NFL slate is almost always two forced pairs (spread and total), so the row tally is arithmetic — report the preferred side of each pair as the trial, and derive the push mass at whole-number spreads and totals rather than asserting it. **`G-L23`:** settle from a feed carrying drive charts, turnovers and player exits with the game clock, not a recap.


Evidence and cohort audit: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17(b)"](PREDICTION_LOG_COMBINED_4.md); rules in `RULES_GENERAL.md` §16.13; bands and base rates in [`BASE_RATES_REGISTER.md`](BASE_RATES_REGISTER.md).


## 2026-09-19 — recency/rebound, social sources and the top-O/U review


`R-1` ([`RECENCY_AND_REBOUND.md`](RECENCY_AND_REBOUND.md)) applies: recent results revise an estimated **rate** through a named mechanism, never forecast a **deviation**. No rebound and no hangover adjustment is permitted in either direction. This sport's magnitudes are **`NOT_YET_DERIVED`** — the MLB figures are not transferable and must not be imported; derive them from this competition's own record before any recent-form weighting.


Source controls `S-1` (social identity: X and Reddit return no usable content; Bluesky sports handles failed identity verification 6/6) and `S-2` (press conferences are availability/role evidence, never a signed adjustment to a modelled rate) apply — `SOURCES.md` §"2026-09-19".


A loss **or push** on the card's highest-ranked over/under now triggers the same enhanced failure review as a Rank #1 loss (`METHOD.md` §7).


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — market-independent totals/line addendum


**Source priority:** NFL/competition official gamebooks, injury/practice reports, transactions and tracking/stat products; nflverse sports-statistical lanes may support historical research with lineage checks. Sportsbook/fantasy/DFS projections are prohibited.


Use drive/possession scoring distributions with QB/offense/defence/special-teams state, participant availability, rest/travel, weather and turnover uncertainty. Preseason and regular-season populations stay separate. Totals/spreads are queried only after the score/margin distribution is frozen.




<!-- ALL-SPORTS-AUDIT-LIVE-RULE-CLEANUP-2026-09-21-CR3 -->
## 2026-09-21 — all-sports audit live-rule cleanup — CR-2026.09.21-3


Current prospective override. Retain drive/play opportunity, QB/offensive-line/skill availability, EPA/success/turnover/field-position branches, pace/game state and overtime/rules era. Withdraw pseudo-tail order-statistic constructions, path-count ranking shortcuts, universal probability-band top-slot rules, one-score “due” logic and generic recent-score trend adjustments. Build one coherent American-football joint outcome distribution before querying targets.

<!-- SETTLED-ROW-REVIEW-2026-09-25D -->
## 2026-09-25(d) — track record from the full settled-row review

**Track record (`C-TRACK-RECORD`).** 12 NFL/NCAA decisions from 6 cards: won **25%** at a mean stated 0.544. The gap is −0.29, with a card-cluster interval of [−0.47, −0.12]: **over-confident**. These cards are labelled **`NO_DEMONSTRATED_SKILL`**.

- **Underdog cushions (+k.5): 1/6** at 0.554. `C-PLUS-CUSHION` applies.
- **Required on every margin row:** the G-L12 residual benchmark (about 13.9 points), and key-number masses at 3 and 7, which are `NOT_YET_DERIVED`, so they are derived before the next NFL handicap card.

Source: `research/settled_rows_2026-09-25/README.md`. The figures are hindsight on the framework's own cards, descriptive, and use card-cluster intervals. None is a coefficient (`L-087`). Controls: `RULES_GENERAL.md` §"2026-09-25(d)".


<!-- RANK-MODEL-2026-09-25E -->
## 2026-09-25(e) — the first NFL population reference, key numbers, the team baseline and the ranking model

Controls: `RULES_GENERAL.md` §"2026-09-25(e)". Evidence: `research/team_baseline_2026-09-25e/README.md`; `BASE_RATES_REGISTER.md` §7.7.

**Record.** NFL/NCAA stays `NO_DEMONSTRATED_SKILL`: 3/12 at 0.544; cushions 1/6. The losses at Rank 1 were five underdog cushions of +1.5 to +6.5 (P-412, P-413, P-414, P-422, P-472).

### (a) Sources

- **ESPN NFL scoreboard** (`…/football/nfl/scoreboard?dates=…`) and **team schedule** (`…/football/nfl/teams/{id}/schedule?seasontype=2`): the TB-1 lane (`--league nfl`).
- **NCAA:** no TB-1 lane (`NOT_COVERED`).

### (b) Reference rows (NFL 2024 / 2025, regular season, n = 272 each)

| Row | 2024 | 2025 |
|---|---:|---:|
| Home win | 0.524 | 0.536 |
| Total mean (SD) | 45.8 (13.1) | 46.0 (13.8) |
| Home margin | +1.7 | +2.2 |
| Margin SD | 14.5 | 14.2 |
| TB-1 residual width, total / margin | 13.1 / 13.7 | 13.4 / 13.6 |

**Key numbers** (previously `NOT_YET_DERIVED`; this is the G-L12 residual benchmark):

| Margin | 2024 | 2025 |
|---|---:|---:|
| P(\|margin\| = 3) | 0.136 | 0.151 |
| P(\|margin\| = 7) | 0.074 | 0.096 |
| P(\|margin\| ≤ 3) | 0.24 | 0.27 |
| P(\|margin\| ≤ 7) | 0.52 | 0.50 |

### (c) Reasoning

1. **TB-1 is the anchor.**
   - Sides: 0.231 v 0.252.
   - Totals: 0.246 v 0.254, which is marginal. **Corrected 2026-09-26(e):** the 2025 interval is [−0.018, +0.002] and 2021–2025 gave 0.2403 v 0.2423, so totals anchor on the population (`TB1_NO_RESOLUTION:total`); §0.2 governs.
   - Early season (Weeks 1–3) is flagged `TB1_EARLY_SEASON`. Its early-season result still beat the base rate (0.246 v 0.253).
2. **Cushions at their population rate.** The TB-1 underdog covered:

   | Cushion | Cover rate |
   |---|---|
   | +1.5 | 0.35–0.42 |
   | +2.5 | 0.38–0.46 |
   | +3.5 | 0.45–0.54 |
   | +6.5 | 0.57–0.60 |
   | +7.5 | 0.61–0.66 |

   Every Rank-1 cushion that lost sat in the +1.5 to +6.5 range and was stated at 0.53–0.58. That is at or above the population rate, with no receipted mechanism. Such a row is now `PLUS_CUSHION_UNSUPPORTED`, and RM-1 flips it.
3. **Key numbers.** A +2.5 or +3.5 row prints the mass at 3 (0.14–0.15). A +6.5 or +7.5 row prints the mass at 7 (0.07–0.10). These are the only places the half-point matters.
