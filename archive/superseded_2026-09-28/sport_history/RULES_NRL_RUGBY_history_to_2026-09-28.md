# Rugby league / NRL analysis rules — dated history to 2026-09-28

**Archived 2026-09-28 (md-only restructure).** These are the dated sections that followed the competition-rules section of `RULES_NRL_RUGBY.md`, moved verbatim. They are the evidence record. The live rules are §0 of `RULES_NRL_RUGBY.md`, and nothing here reinstates a rule that §0 or `CURRENT_RULES.md` §I withdraws.

## September 5 settlement learning — prospective SFA amendment


P-280 reinforces L-038/L-042 and adds the operational L-069 check at the final team refresh. Map expected spine **playing minutes and entry time**, not just the printed jersey position. Arrow's ceremonial start did not remove Walker for an ordinary opening phase. Remove a withdrawn player from every exposure chain before using the remaining middle to justify a cushion. The timestamped NRL preview placed Collins' withdrawal before the frozen cutoff.


At `SFA` possession/field-position and G20.1 separation steps, run both depleted-side attack suppression and opponent repeated-opportunity scoring. A weak attack can coexist with an Over driven mostly by its opponent. Use scoring chronology to distinguish the threshold-crossing mechanism from later sin bins: the P-280 total had crossed before the paired 72nd-minute bins. Actual 50–20 is a case for the library, not a new blowout prior. Candidate C-P293-NRL-ROLE remains at zero prospective completions.




Full evidence and frozen-card comparisons: [September 5 audit](archive/audit_documents_implemented_2026-09-25/COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md).


## September 5(b) settlement learning — P-294–P-305 second continuation


Three NRL/NRLW cards settled this pass (`P-294`, `P-295`, `P-301`); the total (Under) was ranked #1 in all three and lost all three, while the spread/moneyline row ranked #2 won twice and lost once. Full driver analysis is in `PREDICTION_LOG_COMBINED_2.md`'s 2026-09-05(b) section; the load-bearing findings are recorded here.


**`P-295` (North Queensland Cowboys vs Canberra Raiders) — L-075.** Canberra debutant halfback Coby Black scored a premiership-record 26 points (2 tries, 9/9 goals) in a 50-30 Raiders win. The card's own research had already retrieved Black's NSW Cup rate stats (77 goals at 77% conversion, 17 try assists, 362.8 average kicking metres across 19 appearances) and explicitly called him "capable rather than replacement-level" — but `Cowboys -5.5` was still ranked #2 above `Raiders +5.5` at #3. **New rule:** when a reserve-grade or debutant player's own retrieved rate production materially exceeds a "replacement level" framing, write one explicit sentence stating the ranking consequence of that production before finalising the order — do not let the number sit in the availability paragraph while the rank proceeds as if a generic replacement were starting.


**`P-294` (Newcastle Knights (W) vs Canterbury-Bankstown Bulldogs (W)) and `P-297`-adjacent reasoning.** Newcastle won 56-22 (total 78, comfortably clearing 48.5) by carrying almost the entire total alone against a Bulldogs side whose recent defensive collapse (30, 48, 44 conceded in the three prior games) was **already the card's own primary evidence for ranking the Under #1** — the same underlying fact that should have flagged the favourite-only-blowout branch (`RL-B2`, kill-path library §8.5) as the more central state, not a tail risk to the Under. Confirms and extends `C-PL6-RL-FAVOURITE-ONLY-TOTAL` with a fourth data point.


**`P-301` (Cronulla Sharks vs Melbourne Storm).** Melbourne won by a last-second try, 24-20 — a final margin of 4, well inside the 8.5 line, and the exact "competitive game" branch (`RL-B5`/terminal-sequence branch) the card itself had named as live given Cronulla's strong record at Ocean Protect Stadium (won 6 of previous 7 there) and Melbourne's poor recent record at the venue (no win since 2017). The venue/recent-record evidence was recorded but again did not move the spread off Rank #1.


**Sport ordering override addition (§8.6):** before ranking a favourite's spread/handicap above a total in a two-sided NRL/NRLW slate, write one explicit sentence stating whether the favourite's own recently-recalled or in-form scoring capacity is already the evidence being used to justify the Under — if so, the same evidence supports a favourite-only-blowout branch at least as strongly as it supports the total, and the ranking order between them must be reconciled, not defaulted to "Under first."


**Kill-path library addition (§8.5):**


| Kill path | Defeats | Evidence origin |
|---|---|---|
| A reserve-grade or debutant player's own retrieved per-appearance production (goal-kicking %, assist rate, kicking/running metres) exceeds a "replacement level" framing used elsewhere in the same card | A favourite's spread/handicap ranked above the underdog's cushion on an unstated assumption of replacement-level opposition personnel | `P-295`; L-075 |


Full evidence: [PREDICTION_LOG_COMBINED_2.md, 2026-09-05(b) section](PREDICTION_LOG_COMBINED_2.md#component-import--p-294p-305-second-continuation--2026-09-05b).


## September 6 settlement learning — the tries-plus-conversions tail and the second-half window


`P-294` and `P-295` were the two clearest `TAIL_EXPOSED` failures in the whole `P-294`–`P-305` cohort, and both were rugby league.


| Card | Line | Actual | Why the tail budget would have flagged it |
|---|---|---|---|
| `P-294` Newcastle Knights (W) v Canterbury (W) | `Under 48.5` (rank #1) | **78** (56-22) | The Knights' own upper L10 output plus the Bulldogs' median already exceeds 48.5 before any variance is added. The complementary `Knights -15.5` at rank #2 **won** — the card's own margin read and its total read were pointing at incompatible totals, which `G25.1` should have caught and `G20.2` now makes arithmetic |
| `P-295` North Queensland v Canberra | `Under 56.5` (rank #1) | **80** (50-30 Raiders) | A genuine upset, but the Raiders were 30-12 up at half-time; a second-half exposure term held at the upper decile clears 56.5 on its own |


**Required from now on, `SFA-RUGBY-LEAGUE`:** the tail budget is computed on **tries, conversions and penalty/field goals as separate scoring components**, converted explicitly to points: `points = 4×tries + 2×conversions + 2×penalty_goals + 1×field_goals`, where `conversions = tries × goal-kicking%`. **Correction, 2026-09-06(d):** the original wording ("tries × kicking percentage") omitted the try points themselves and the penalty/field-goal terms — the formula above is the actual points total, not a proxy for it. Hold each side's try count at its second-highest L10 value and its goal-kicking percentage at its own L10 rate — not a generic 75%. Then hold the **second-half window separately**, because the fatigue and interchange regime after the 55th minute has its own scoring rate; `G20.1` already requires this split for margins, and it now applies to totals.


`P-295` is also the origin case for `L-075` (a debutant's own reserve-grade production must be carried into the ranking weight, not only the risk paragraph). Coby Black's 26-point debut record is exactly a goal-kicking-rate observation: the tail budget and `L-075` reinforce each other, because a debutant kicker with a strong NSW Cup goal-kicking percentage raises the conversion term directly.


### Kill-path library addition (§8.5)


| Kill path | Defeats | Evidence origin |
|---|---|---|
| **Conversion-rate compounding** — an ordinary try count converts at an upper-decile rate and clears an `Under` that the try count alone would not | A full-game `Under` budgeted on tries without a separate goal-kicking term | `P-294` (78 against `Under 48.5`), `P-295` (`L-075`) |
| **Half-time blowout state** — a 30-12 half-time score makes the second half a different scoring environment in both directions (garbage-time tries, or a shut-down) | A total budgeted from a single whole-game rate | `P-295` |
| **Own-margin/own-total incoherence** — the card's ranked margin row implies a total incompatible with its own ranked total row | Any slate carrying both, unreconciled | `P-294`: `Knights -15.5` won while `Under 48.5` lost — `G25.1` plus `G20.2` |




### Cross-sport gates instantiated here (v3.7)


| Gate | Sport-native instantiation |
|---|---|
| `G10.2` settlement-source pre-registration | NRL/NRLW finals settle from the ABC News Score Centre lane promoted on 2026-09-05(b); `nrl.com` remains behind a login wall for automated fetches. Name the exact Score Centre record at freeze. |
| `G14.2` coaching / bench / rotation record | Record the head coach, the named interchange bench (four in the NRL) and any 18th-man/concussion provision from §9, plus the rotation signal for a dead rubber or a finals-eve rest. Official club 24h cuts, 1h final team lists, or accredited rugby league beat reporting verified under Control `S-1 Rev 2` qualify as `PROJECTED_BEAT_VERIFIED`, satisfy `G14.2`, and do not block Rank #1. |
| `G20.2` distributional tail audit | Derive tail and boundary mass from the **same frozen rugby-league joint score distribution**, including final team/role/bench, possession and field position, set starts, ruck/play-the-ball, kicking/discipline, venue/weather and golden-point endpoint where applicable. Historical order-statistic stress sums are superseded as active gates. |
| `G21.1` exact target geometry | Map every supplied target to its exact settlement event and derive WIN/PUSH/LOSS from the same frozen sport-native PMF/CDF or coherent branch mixture. Historical path-count/category labels have no mandatory ordinal effect. |
| `G26.1` no universal separation floor | Reference rates and `rank_gap` are descriptive only. **No 40–60% or other pooled probability band can disqualify Rank #1.** Rank from exact marginal likelihood plus robustness/evidence uncertainty. |


**Pre-issue checklist additions (this sport):** settlement endpoint named per row; coaching/bench/rotation record for both sides with missingness codes; tail-budget sums printed against every total line; path-geometry class and `N` printed for every total and phase-total row; separation-floor result stated for Rank #1.


Full narrative and evidence: [`archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md`](archive/audit_documents_implemented_2026-09-25/IMPROVEMENT_PLAN_2026-09-06.md). Controlling gate text: [`RULES_GENERAL.md` §13](RULES_GENERAL.md).


## September 5 implementation after freeze confirmation


**ACTIVE REQUIRED PROCESS — MDS-2026.09.05-v3.6 / L-068–L-072.** Refresh final changes and expected actual roles/minutes immediately before issue, including ceremonial starting positions. Calculate favourite margin and opponent scoring jointly with repeat-set/territory exposure so a cushion and Under do not inherit the same unsupported resistance assumption.


At final delivery, record the preferred total direction for each exact target, the strongest evidenced failure path for ranks #1 and #2, and whether both can win under the stated joint scenario. Rank by supported marginal likelihood; do not promote an opposite pick solely to manufacture one O/U win. At settlement, keep all issued wins/losses, including defective reasoning, in the applicable historical scorecard and review failed #1/#2 and preferred totals.


[Eligibility policy](PERFORMANCE_ELIGIBILITY_POLICY.md): non-live history is user-confirmed frozen pre-game; explicit live-issued views stay separate. These process repairs are implemented now. Numerical weights and predictive-lift claims need a later frozen comparison; historical origin games do not supply those completions.


## 2026-09-06(f) — settlement and retrospective addendum


P-294 favourite scoring alone cleared the total; P-295 replacement-grade production was already knowable while the early sin-bin was not; P-301 a winning favourite did not cover the required margin. Reconcile two-team native-unit points and named replacement roles with the printed central/counter branches. Magnitudes and rank consequences remain candidates under METHOD v4. Preserve NRLW as a distinct competition in descriptive evaluation.


Full frozen ranks, actual drivers, knowability and smallest fixes: [PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md](archive/mini_logs/PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md). Reinforcement only; METHOD v4.0 remains controlling and no new predictive weighting is promoted.


## 2026-09-09 — cross-sport controls instantiated here (`G-L1`, `G-L2`, `G-L7`, `G-L8`)


No NRL/NRLW card was issued in the `P-333`–`P-344` cohort. The four cross-sport requirements adopted from it (`RULES_GENERAL.md` §§16.5(a)–(d), full evidence in `PREDICTION_LOG_COMBINED_3.md` §"2026-09-09") apply to this sport from the next card — and they bear directly on `P-301`, where a winning favourite did not cover the required margin. All four are **disclosure/retrieval requirements — no fitted weight, no ordinal bar** (`L-087`).


| Cross-sport control | NRL / rugby league instantiation |
|---|---|
| **`G-L1` §16.5(a)** — enumerate outcome-state families with explicit mass | Enumerate the **margin families** in native units (favourite by 25+ / 13–24 / 7–12 / 1–6 / draw / underdog win) and the **total families** in points, each with an explicit mass summing to 1. Because scoring is quantised in 4s and 6s plus 2-point conversions and 1-point field goals, state families as **try-count × conversion-rate** combinations rather than a smooth corridor. Every current-evidence §8.5 kill path — including a **sin-bin or send-off**, and the **late consolation try** that decides so many handicap rows — appears as a weighted branch. Print a representative Rank-#1 final score as a try/goal breakdown and check it against the line, the total and any team-total row. |
| **`G-L2` — declared uncertainty model** | State the prior and scenario probabilities. Symmetric uncertainty around an unchanged prior affects width; hierarchical shrinkage or asymmetric scenarios may change both mean and variance. Regenerate all dependent probabilities; unsupported directional adjustments remain prohibited. SCORING_AND_VALIDATION section 5 controls. |
| **`G-L7` §16.5(c)** — aggregate-to-disaggregate retrieval | Do not let a season points-per-game figure or a "last N" summary carry directional weight while the **round-by-round log** is available. Print the per-round record for the decision-relevant window — points for/against, tries, completion rate and the decision-driving players' **minutes and involvements per match** — and state whether a run is front-loaded, back-loaded or uniform. For a returning player, print the **reserve-grade / return-to-play minutes ladder**, the analogue of the rehab pitch-count ladder that decided `P-335`. Quantify **every player in the spine and every top-three try-scorer on both sides**; a bare name in a "leaders include…" phrase is `AGGREGATE_ONLY` and caps the dependent margin/total rows. |
| **`G-L8` — distribution coherence** | Derive each total/spread probability from the exact joint PMF/CDF and settlement endpoint, with push mass. Absolute normalised distance does not order probabilities across different distributions. No missing width or realised result justifies an invented probability. |


## 2026-09-11 settlement learning — `P-363` (NRLW) — a positive model


**`P-363` — Sydney Roosters (W) 42–12 Canterbury-Bankstown Bulldogs (W), NRLW Round 11** ([`PREDICTION_LOG_COMBINED_3.md` §"2026-09-11"](PREDICTION_LOG_COMBINED_3.md)). Frozen card: R1 Bulldogs +40.5 (0.61) **W**; R2 Under 59.5 (0.55) **W**; R3 Over 59.5 **L**; R4 Roosters −40.5 **L**; winner Roosters (~97%) correct. **Top two both won; card mean Brier 0.1773 — the best card of the `P-358`–`P-371` block.** NRLW is a separate population from NRL (`SFA-RUGBY-LEAGUE` preamble) and remains `EXPLORATORY`.


**Why it worked.** The NRL late mail confirmed both 1–17s with no late changes (spines and goal-kickers identified); the `RL-B1`–`RL-B8` branch set named both the favourite-only-scoring Over path and the low-total-separation path; and the card anchored the handicap on a verifiable base rate — the Roosters had cleared a 40.5-point margin in only 2 of 10 wins. Canterbury led at half-time and scored 12; the Roosters' second-half surge (six tries in 16 minutes) still stopped at +30.


**Gaps (presentational):** no numeric width, no family masses and no head coaches on the card. The branch set did the work a family table would have done; print the masses next time (`RULES_GENERAL.md` §16.8).


| Cross-sport control (2026-09-11) | Rugby-league instantiation |
|---|---|
| `G-L9` §16.5(e) | Itemise the complement across the `RL-B` branches — favourite-only blowout (`RL-B2`), low-total separation (`RL-B3`), second-half separation (`RL-B4`), sin-bin/send-off (`RL-B6`). |
| `G-L10` §16.5(f) | Underdog +handicap and Under are **positively** coupled through a competitive underdog that also slows the game — but anti-coupled through `RL-B3` (favourite suppresses the underdog and wins big in a low-scoring game). Print the sign from the branch masses. |
| `G-L11` §16.5(g) | Completion rate, goal-kicking percentage and try-scoring rates over three or four rounds are small samples; print their standard error before a signed adjustment. |
| §16.8 | Late mail is published before kick-off; `NOT_RETRIEVED` after it is a `RETRIEVAL_MISS`. |




## 2026-09-12 algorithm corrections and retrospective integration


Use the joint team-points and game-phase branches for handicap/total dependence. P-363 correctly captured a competitive first half; the actual sin bin at 48 minutes and Baxter HIA are post-issue disruptions, not pregame predictive credits. Preserve them as explanatory match facts with chronology and examine the original ordinary separation branch separately. Confirm both starting 13s, interchange/reserves, goal-kickers and coaches from dated late mail. Trial/attempt rates require real denominators and repeated-team/game dependence disclosure.


For every supplied row, use exact target probabilities from a coherent joint distribution; handle push/void/censoring explicitly, avoid overlapping adverse-state counts, and report JOINT_UNQUANTIFIED with bounds if the dependence is not specified. Separate issued-time participant capture, later recovered evidence, source accuracy by field, observed mechanism, and unverified causal interpretation. Keep one preferred O/U direction per distinct target and report the top-two denominator honestly. Shared correction and methodology sources (`audit_2026-09-12/rule_corrections.md`, not present in this repository). All current log observations remain learning-only and not performance-eligible.




## 2026-09-15(b) settlement learning — `P-373`–`P-423` import


Learning-only; disclosure/process changes only — no coefficient or ordinal bar (`L-087`). Evidence and tables: [`PREDICTION_LOG_COMBINED_3.md` §"2026-09-15(b)"](PREDICTION_LOG_COMBINED_3.md). Cross-sport rule: `RULES_GENERAL.md` §16.10 (`G-L12` margin centre/width; fixture identity; official-record derivative settlement).


**Cards:** P-380 (NRLW), P-386 (Souths v Knights), P-394 (NRLW), P-397 (Sharks v Cowboys). Finals re-verified at ESPN (`rugby-league/3`) for P-386/P-397.


- **Positive:** P-380 realised the printed low-total favourite-separation branch (Raiders 22–10: −6.5 and Under 46.5 both won); P-386 Knights +8.5 won outright 20–10; P-394 Cowboys +10.5 won in a high-total close game. Rugby-league underdog cushions went 3 / 0 at Rank #1 — the one sport where the cross-sport pattern did not appear.
- **Negative:** P-397 — Over 48.5 (Rank #1) and Cowboys +7.5 (Rank #2) both lost to the low-total favourite-cover state (26–16) that branch `RL-B3` had printed. Add P-397 as the worked example: when RL-B3 carries material mass, `P(R1 ∧ R2)` for an Over + underdog cushion must be printed (`G-L10`).
- **`G-L12` instantiation:** print the favourite's 7+ and 13+ margin families beside any cushion; finals intensity is width.


## 2026-09-16 — cross-sport controls instantiated here (`G-L13`, `G-L14`, `G-L15`, disruption facts)


No rugby-league card was settled this pass. Rules: `RULES_GENERAL.md` §16.11.
- **`G-L13`:** team lists and late mail come from the raw NRL match centre or club page, with its publication time; never from a summary.
- **`G-L14`:** a half-time or first-try row names its settling record (ESPN `rugby-league/3` line scores are verified for finals).
- **`G-L15`:** P-397's Over 48.5 and Cowboys +7.5 were **distinct targets** with a shared driver. Their joint loss is reported against `Σp − P(A ∧ B)`, not as "one O/U lost".
- **Disruption facts:** record sin bins, send-offs and HIA removals with the minute and the score. P-363's 48-minute sin bin is the model entry.


## 2026-09-17 — cross-sport controls instantiated here (`G-L17`–`G-L20`)


No rugby-league card in this import. **`G-L17`:** `P-397` (Over + underdog cushion, both lost to the low-total favourite-cover state) is the worked example — now print `P(¬R1 ∧ ¬R2)`, not only the joint win. **`G-L18`:** print each side's own points marginal before a match total. **`G-L19`:** NRL regular-season games can be drawn (golden point applies only where the competition's rules say so) — the winner family carries draw mass. **`G-L20`:** a current-season meeting that cleared the line gets explicit mass.


Evidence and cohort audit: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17"](PREDICTION_LOG_COMBINED_4.md); rules in `RULES_GENERAL.md` §16.12.


## 2026-09-17(b) — cross-sport controls instantiated here (`G-L21`–`G-L24`)


**G-L24 in NRL RUGBY:** derive the exact signed-margin distribution under the competition endpoint, including draw, key-value and push masses. Pooled league bands are uncertain references, not mandatory matchup probabilities or rank prohibitions. Missing pooled bands do not invalidate a complete conditional joint distribution. **`G-L21`:** the recurring NRL slate — favourite line, Under, favourite team total — is one thesis in three rows; print the joint failure mass. **`G-L22`:** forced pairs; report preferred sides and derive push mass at whole-number lines. **`G-L23`:** completion rate, errors, penalties and **sin bins and send-offs with the minute and score** are the process and disruption fields.


Evidence and cohort audit: [`PREDICTION_LOG_COMBINED_4.md` §"2026-09-17(b)"](PREDICTION_LOG_COMBINED_4.md); rules in `RULES_GENERAL.md` §16.13; bands and base rates in [`BASE_RATES_REGISTER.md`](BASE_RATES_REGISTER.md).


## Current model implementation — 2026-09-17


Use METHOD v4.2's six-field object and SCORING_AND_VALIDATION for exact outcome/push scoring, event-level comparison, descriptive recency and declared hierarchical uncertainty. MODEL_IMPLEMENTATION_RECIPES supplies this sport's retained model scope and endpoint design. Forecast probabilities come from the joint model; pooled base rates are uncertain context, not universal limits. Numeric row caps disconnected from that model, absolute-distance probability ordering and retrospective tail reweighting are withdrawn. No fitted coefficient or predictive improvement is claimed. New cards freeze the method/control hash; existing cards keep their issued versions.


## 2026-09-19 — recency/rebound, social sources and the top-O/U review


`R-1` ([`RECENCY_AND_REBOUND.md`](RECENCY_AND_REBOUND.md)) applies: recent results revise an estimated **rate** through a named mechanism, never forecast a **deviation**. No rebound and no hangover adjustment is permitted in either direction. This sport's magnitudes are **`NOT_YET_DERIVED`** — the MLB figures are not transferable and must not be imported; derive them from this competition's own record before any recent-form weighting.


Source controls `S-1` (social identity: X and Reddit return no usable content; Bluesky sports handles failed identity verification 6/6) and `S-2` (press conferences are availability/role evidence, never a signed adjustment to a modelled rate) apply — `SOURCES.md` §"2026-09-19".


A loss **or push** on the card's highest-ranked over/under now triggers the same enhanced failure review as a Rank #1 loss (`METHOD.md` §7).


<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — market-independent totals/line addendum


**Source priority:** NRL/competition official team lists, match centre, judiciary/availability, club releases and government weather. Betting/fantasy content is prohibited.


Totals and handicaps should arise from a joint scoring model using lineup/spine availability, possession/territory/completion and line-break/kicking process, interchange/bench state, venue/weather and rest. Do not convert recent wins/losses or the market line into an unexplained point adjustment.




<!-- ALL-SPORTS-AUDIT-LIVE-RULE-CLEANUP-2026-09-21-CR3 -->
## 2026-09-21 — all-sports audit live-rule cleanup — CR-2026.09.21-3


Current prospective override. Retain final team/role/bench, possession/field-position/set starts, ruck/play-the-ball, kicking/discipline, venue/weather and golden-point endpoint. Withdraw pseudo-tail order-statistic constructions, path-count ranking shortcuts, universal probability-band top-slot rules, normalized-distance ordering, symmetric widening from a one-sided absence without a named mechanism, and automatic rebound/response rules. Build one coherent rugby-league joint outcome distribution before querying targets.

<!-- RANK-MODEL-2026-09-25E -->
## 2026-09-25(e) — the first NRL population reference, the team baseline, P-515 and the ranking model

Controls: `RULES_GENERAL.md` §"2026-09-25(e)". Evidence: `research/team_baseline_2026-09-25e/README.md`; `BASE_RATES_REGISTER.md` §7.7.

### (a) Sources

1. **ESPN NRL scoreboard** `…/rugby-league/3/scoreboard?dates=YYYYMMDD`.
   - The NRL regular season is ESPN **season type 1**; finals are type 2.
   - `linescores` carry cumulative values: the half-time score, then the full-time score.
   - It is admitted as one settlement lineage and as the TB-1 lane (`--league nrl`). The NRL team-schedule endpoint returns HTTP 500, so the tool reads the scoreboard; the first run takes about 2 minutes, then it is cached.
2. **P-515 correction.** The settled log recorded the Preliminary Final as Roosters 36, Dolphins 14 (total 50). ESPN event 604843 gives **36–20** (half time 16–6; total 56).
   - The grades are unchanged: Under 45.5 lost; Roosters +2.5 won; Dolphins −2.5 lost.
   - The process "facts" in that retrospective (329 run metres, 14 errors) were unsourced and are struck (`C-SETTLEMENT-FROM-FEED`).
3. **The nrl.com match centre** returned no statistics through the proxy on 2026-09-25. Its figures are admissible only when fetched and pasted with a URL.

### (b) Reference rows (NRL 2025 / 2026, all completed games, n = 216 / 213)

| Row | 2025 | 2026 |
|---|---:|---:|
| Home win | 0.551 | 0.545 |
| Total mean (SD) | 46.1 (14.0) | 47.8 (13.9) |
| Total, 10th / 50th / 90th percentile | 29 / 44 / 64 | 30 / 48 / 66 |
| Home margin | +3.8 | +0.0 |
| Margin SD | 18.7 | 20.7 |
| P(\|m\| ≤ 2) | 0.13 | 0.15 |
| P(\|m\| ≤ 6) | 0.34 | 0.29 |
| TB-1 residual width, total / margin | 13.8 / 18.3 | 13.9 / 19.9 |

### (c) Reasoning

1. **TB-1 is the anchor for sides** (0.240 v 0.253). **Totals have no resolution:** TB-1's total RMSE is worse than the league mean. NRL totals therefore anchor on the population row: in 2026, 47.8 with SD 13.9.
   - P-515's Under 45.5 at 0.635 sat about 0.10 above that population, where P(total < 45.5) ≈ 0.43–0.48 (TB-1 gave 0.445). It rested on an unmeasured "bye rust / wet track" story. Under the departure ledger it now needs a receipted mechanism, such as a confirmed wet-track forecast for the match window.
2. **Early season.** TB-1 was worse than the base rate in the NRL's early rounds (0.284 v 0.271). Before Round 5, anchor on `BASELINE_P`.
3. **Cushions.** The TB-1 underdog covered:

   | Cushion | Cover rate (2025–26) |
   |---|---|
   | +1.5 | 0.41–0.43 |
   | +2.5 | 0.44–0.49 |
   | +4.5 | 0.51 |
   | +6.5 | 0.55–0.57 |
   | +8.5 | 0.62 |
   | +12.5 | 0.65–0.67 |

   `C-PLUS-CUSHION`, as amended, applies.
4. **Finals and byes.** `C-FINALS-BYE-RUST` is **TESTING, non-binding** (`T-NRL-BYE-RUST`): collect the first-half margins of NRL finals played after a bye, from the ESPN scoreboard, over at least 30 games. `C-NRL-SPINE-PEDIGREE-TOTAL-FLOOR` is **REJECTED** (one game, and an invented statistic).
