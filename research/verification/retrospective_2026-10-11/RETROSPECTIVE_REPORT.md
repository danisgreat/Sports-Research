# Cohort retrospective 2026-10-11 (P-557 to P-576)

Mode `COHORT_RETROSPECTIVE` (prompt 6). This report measures, explains and recommends. It changes no rule, model, forecast, grade or prompt; every recommendation is `PROPOSED_NOT_TESTED`. All records are `RESEARCH_ONLY_NOT_CERTIFIED`; every probability is an `UNCALIBRATED_ANALYST_SCENARIO`.

## 1. Scope, ranges, HEAD and data sources

| Item | Value |
|---|---|
| Repository / branch / HEAD | `danisgreat/Sports-Research` · `main` · `df111ce71f64a211b29bf3bddca92860f2321b72` (equal to `origin/main`, clean) |
| Authority | MDS-2026.10.09-v9.0 · CR-2026.10.09-R5 · SCV-2026.10.09-v5 · SEL-2026.10.09-v1 (provisional) |
| Scope written | 2026-10-11T22:37+11:00, before the tables ([DATA_INVENTORY.md](DATA_INVENTORY.md) §1) |
| Last retrospective | 2026-10-09 ([FRAMEWORK_RETROSPECTIVE_2026-10-09.md](../../../FRAMEWORK_RETROSPECTIVE_2026-10-09.md) with the [final settlement](../final_settlement_2026-10-09/REPORT.md) through P-556); no earlier `retrospective_*` folder |
| New cohort | **P-557 to P-576**, 20 settled cards (KBO 6, basketball 8, soccer 3, ice hockey 3), events 2026-10-09 to 2026-10-11 (one ISO week, 2026-W41); all `RANK1_UNSTABLE` |
| Comparison cohort | **P-126 to P-556**, 71 forecast cards (P-532 `NO_FORECAST` excluded), all `UNKNOWN_GATE` |
| Excluded | P-577, P-578, P-579 (`PENDING_EVENT`) |
| Threshold | 20 new cards, below the 30-card trigger; run at the user's request |
| Data | [DATA_INVENTORY.md](DATA_INVENTORY.md) (file and line of every settlement block used), [COHORT_TABLES.md](COHORT_TABLES.md) (every input row and every table) |

Reading receipt (printed before the work):

```text
READING RECEIPT
Repository / branch / HEAD SHA: danisgreat/Sports-Research · main · df111ce71f64a211b29bf3bddca92860f2321b72 · read 2026-10-11T22:37+11:00
Read in full: CURRENT_STATE · METHOD · CURRENT_RULES (T2, R1, P4) · SELECTION_RULES · SCORING_AND_VALIDATION · HYPOTHESIS_REGISTER · CARD_AND_LOG_TEMPLATES · VERIFICATION_PROTOCOL · research/prompts/6_COMBINED_LOG_RETROSPECTIVE.md · research/prompts/README.md
Also read: FRAMEWORK_RETROSPECTIVE_2026-10-09 (§3.3 failure-class baseline, §5 register, §5.8 status table, §6–§7) · LEAGUE_PROFILES (all) · ARCHIVE_USE_GUIDE §5–§6 · BASE_RATES_REGISTER §7.1 · research/scoreboard/SCOREBOARD.md · final_settlement_2026-10-09/REPORT.md
Sources: SOURCES §E–§F (exclusions, reachability) for the source-route checks
Past results: LEAGUE_PROFILES rows KBO, NBL, NHL; no Previous Sports Results CSV opened (no 2026 season file exists for any league in the cohort)
Not read or unavailable: no earlier research/verification/retrospective_* folder exists
```

## 2. Executive summary

**Findings**

1. **The high counted rate is produced by line choice, not by forecasting.** New cohort 34/40 = **85.0% (70.9–92.9%)** against 79/134 = **59.0% (50.5–66.9%)** in the comparison cohort. Every new card paired two rows whose losing events cannot happen together (stated P(both lose) 0.0% on 20/20; realised `TOP2_ALL_LOST` 0/20, 0–16.1%), each priced at a mean 87.0%. Against its own stated probabilities the top two won 34 where 34.8 were expected; Brier 0.131 against climatology 0.128, **skill −0.03**.
2. **Ranking does not separate propositions.** Rank 1 80.0% (58.4–91.9%) < Rank 2 90.0% (69.9–97.2%); ranks 3–4 77.5% (62.5–87.7%). The comparison cohort shows the same: Rank 1 58.8%, Rank 2 59.1%, ranks 3–4 56.4%.
3. **Calibration: no over-confidence established, and no skill.** In the 80–90% bin the stated 86.9% met a realised 86.4% (76.1–92.7%, n = 66). Rank 1 (mean stated 88.7%) won 80.0%, 16 against 17.75 expected (z −1.24): `INSUFFICIENT_EVIDENCE`, about 80 Rank-1 rows needed. All four Rank-1 losses are `OVERCONFIDENT_PROBABILITY` at 88.0–90.0%, each a 10–12% tail of the card's own distribution. Expected-score widths look honest: total |z| averaged 0.72 over 16 cards and 0 of 16 exceeded 2.
4. **The Rank-1 gate cannot be passed as cards are now built.** 20 of 20 cards were `RANK1_UNSTABLE`, with margins of 0.06 to 2.5 points, because several ladder lines always sit just under the 90% ceiling. The `COUNTED` cohort is empty, and SEL-1 (8 week-blocks of PASS against UNSTABLE) cannot start.
5. **Process is deficient on every card, and the results do not depend on it.** R9 reads `Process: DEFICIENT` on 20 of 20 cards. Twelve cards were completed after the scheduled start (13 labelled `LATE_START_UNVERIFIED`). A quarter of rows were settled on evidence C, and no KBO card reached A. Only 4 of 16 cards read archive rows. Excluding C rows changes nothing (86.7%, 70.3–94.7%). NBL expected totals ran low on 3 of 3 cards, mean +16.8 points (−2.0 to +35.6), against a profile row two seasons old.

**Recommendations** (all `PROPOSED_NOT_TESTED`; §7)

1. **RET-02 (P1):** print a league-only baseline probability (`BASELINE_P`) beside every ranked row, and judge the cards by Brier skill against it instead of by hit rate.
2. **RET-03 (P1):** shadow-test a gate whose alternative excludes other lines on the same quantity, alongside SEL-1, so that the gate can return PASS.
3. **RET-04 (P1):** require Rank 2 to be on a different quantity from Rank 1, so that Hit@2 is no longer guaranteed by construction.
4. **RET-01 (P1):** recompute the NBL league level from 2025-26 and 2026-27 games, and print the recomputed level when a profile row is more than one season old.
5. **RET-05 (P1):** score cards completed after the scheduled start in their own sub-cohort, with a target of 90% `PREGAME`.

## 3. Quantitative analysis

### 3.1 Headline

| Cohort | Counted | Rate | 95% CI | Rank 1 | Rank 2 |
|---|---|---:|---|---|---|
| New | 34/40 | 85.0% | 70.9–92.9% | 16–4, 80.0% (58.4–91.9) | 18–2, 90.0% (69.9–97.2) |
| Comparison | 79/134 | 59.0% | 50.5–66.9% | 40–28, 58.8% (47.0–69.7) | 39–27, 59.1% (47.0–70.1) |

Against the 2026-10-09 baseline, Rank 1 (80.0%) is above 58.8%, but its interval (58.4–91.9) reaches below the baseline. Rank 2's interval (69.9–97.2) excludes 59.1%. Neither difference counts as established. The new cohort spans one ISO week, and the week-block comparison (SCORING_AND_VALIDATION §5) needs at least 8, so both are `INSUFFICIENT_EVIDENCE`. Even with 8 weeks, the cohorts would not be comparable. The new cards priced their picks at a mean of 87.0%. The comparison cards ranked mixed propositions under older conventions, such as first-half Over 0.5 and +1.5 cushions near 60%. A higher hit rate on easier propositions is not an improvement. The like-for-like test is skill against a baseline on the same rows (recommendation RET-02). **Sample needed:** 8 week-blocks of cards that print a baseline probability.

### 3.2 Does each slot carry information?

| Slot | New | Comparison | All |
|---|---|---|---|
| Rank 1 | 80.0% (58.4–91.9) | 58.8% (47.0–69.7) | 63.6% (53.2–72.9) |
| Rank 2 | 90.0% (69.9–97.2) | 59.1% (47.0–70.1) | 66.3% (55.8–75.4) |
| Ranks 3–4 | 77.5% (62.5–87.7) | 56.4% (47.9–64.5) | 61.3% (53.8–68.2) |

**Ranking is not separating propositions.** Rank 1 does not beat Rank 2 in any cohort, and in each cohort the intervals for Ranks 1–2 and Ranks 3–4 overlap. In the new cohort this follows from how the cards are built. Rank 1 leads Rank 2 by a median of 1.75 points (range 0.1–14.5), and on 11 of 20 cards Rank 3 sits within 5 points of Rank 1. The stated differences are too small to show up in 20 events. Detecting a 10-point Rank-1 advantage would take about 200 cards.

### 3.3 Calibration

| Stated p bin | n | Mean stated | Win rate | 95% CI |
|---|---:|---:|---:|---|
| 50–59% | 1 | 57.9% | 100% | 20.7–100% |
| 60–69% | 3 | 64.4% | 66.7% | 20.8–93.9% |
| 70–79% | 10 | 75.0% | 50.0% | 23.7–76.3% |
| 80–90% | 66 | 86.9% | 86.4% | 76.1–92.7% |

- **Main finding.** The high bin did **not** under-perform: 86.4% realised against 86.9% stated. The pattern is the absence of skill, not over-confidence. Brier was 0.148 on all 80 rows against climatology 0.152, a skill of +0.03. On the top two it was 0.131 against 0.128 (skill −0.03), and on Rank 1 0.169 against 0.160 (skill −0.06). Here climatology means the realised in-sample win rate, which already gives it a slight advantage. A constant 85% would have scored as well as the cards on the rows that count.
- **Rank 1 specifically.** Mean stated 88.7%, realised 80.0%, so 16 wins against 17.75 expected (SD 1.41, z −1.24). At a constant 11.3% loss rate, four or more losses in 20 has probability 0.18. Result: `INSUFFICIENT_EVIDENCE`. Showing an 8.7-point shortfall would need about 81 Rank-1 rows across at least 8 week-blocks.
- **70–79% bin.** 5 of 10 won against 75.0% stated (23.7–76.3%). The bin holds only ranks 2–4 and is the one to watch. The stated mean sits at the very edge of the interval.
- **Comparison cohort.** `NOT_COMPUTABLE`: its settlement tables carry no `p_card`.

### 3.4 Joint failure

| Cohort | Mean stated P(both lose) | Realised `TOP2_ALL_LOST` |
|---|---|---|
| New | 0.0% (20/20 "by construction") | 0/20 = 0.0% (0.0–16.1%) |
| Comparison | `NOT_COMPUTABLE` (not recorded) | 15/68 = 22.1% (13.8–33.3%) |

`TOP2_ALL_LOST` did not occur more often than stated. The drop from 22.1% to 0% is mechanical. SELECTION_RULES §3 tells the card to choose the Rank 2 that minimises P(both lose), and the minimum is always a row whose losing region is disjoint from Rank 1's: 12 bracketing match totals, 1 bracketing team total, 1 pair of opposite handicaps, and 6 handicaps or team totals covered by a total. Under this rule Hit@2 is 100% by construction and stops measuring anything (§8). Recommendation RET-04.

### 3.5 Stability gates

- **PASS against `RANK1_UNSTABLE`.** There are 0 PASS cards and 20 `RANK1_UNSTABLE` cards (Rank 1 16–4), so no comparison exists. Every Rank 1 cleared the 62% floor (lowest 84.3%), and every card failed the 4-point margin. The margins were 0.06, 0.1, 0.2, 0.2, 0.3, 0.3, 0.30, 0.31, 0.4, 0.71, 0.8, 0.8, 0.89, 0.9, 1.3, 1.5, 1.6, 2.4 and ~2.5 points; P-572 printed no number.
- **Why.** The ladder spans ±2.5 SD on every quantity, so each quantity offers a line priced just under the 90% ceiling. The best non-complementary alternative is then usually another line on the same total, or the opposite bracket, priced within a point of Rank 1. In SD units every Rank 1 sat 1.16 to 1.34 SD from its centre.
- **Legacy cut.** The comparison cards carry no recorded gate, so none of them is `LEGACY_P_ONLY` under the 60% cut either.
- **Keep, tighten or relax?** The data supports none of the three. **SEL-1 is not complete**: 1 of 8 week-blocks has elapsed (the gate dates from 2026-10-09) and there are 0 PASS cards. The gate stays provisional and unchanged. The structural finding goes to prompt 8 as RET-03.

### 3.6 By sport and family

No sport × family cell is reliably below or above 50% at Rank 1. Every interval crosses 50%.

| Cell (Rank 1, all cohorts) | W–L | Rate (CI) |
|---|---|---|
| Basketball × match total | 6–6 | 50.0% (25.4–74.6) |
| Tennis × all | 2–3 | 40.0% (11.8–76.9) |
| Baseball × handicap | 7–4 | 63.6% (35.4–84.8) |
| Soccer × first-half period total | 10–5 | 66.7% (41.7–84.8) |
| Soccer × team total | 5–2 | 71.4% (35.9–91.8) |
| Baseball × match total | 6–1 | 85.7% (48.7–97.4) |

The weakest well-populated cells are basketball match totals and tennis. The strongest is baseball match totals, which won 5–1 in the new cohort, all at about 89% bracket lines. Confirming that a cell is below 50% when its true rate is 40% takes about 93 Rank-1 rows in that cell, so every cell is `INSUFFICIENT_EVIDENCE`.

### 3.7 Failure classes

| Class (SELECTION_RULES §8) | Baseline (2026-10-09, §3.3) | Comparison, primary class | New |
|---|---:|---:|---:|
| `FIRST_HALF_GOAL_OVERSELECTION` | 5 | 5 | 0 |
| `RUNLINE_CUSHION_CEILING` | 4 | 4 | 0 |
| `BASKETBALL_TOTAL_WITHOUT_PACE_MODEL` | 3 | 2 | 0 |
| `TENNIS_IID_UNDERDISPERSION` | 3 | 2 | 0 |
| `RANK_BY_Q_NOT_P` | 3 | 3 | 0 |
| `SHARED_DRIVER_TOP_TWO` | 5 | 3 | 0 |
| `OVERCONFIDENT_PROBABILITY` | (in "other") | 1 | **4** |
| other classes | 7 | 8 | 0 |
| Rank-1 losses | 28 | 28 | 4 |

None of the six named classes recurred. For five of them the cards had almost no exposure:
- no first-half Over 0.5 at Rank 1;
- no +1.5 run line at Rank 1 (the two +1.5 cushions on the slate were informational rows, P-558 R4 at 79.3% and P-559 R4 at 75.5%, and both lost);
- no tennis card;
- q ranking is excluded by self-audit C3;
- shared drivers are excluded by disjoint pairs.

The two basketball total losses (P-560, P-576) came from possessions × points-per-possession models and are correctly not classed as missing a pace model. **Still recurring:** `OVERCONFIDENT_PROBABILITY`, the one class whose proposed correction (P-430's) was never adopted. It accounts for 4 of 4 new Rank-1 losses.

### 3.8 Evidence quality

| Cohort | C+E+OP+X share of rows | Counted, all rows | Counted, C and E excluded |
|---|---:|---|---|
| New | 20/80 = 25.0% (all C) | 34/40, 85.0% | 26/30, 86.7% (70.3–94.7) |
| Comparison | 38/309 = 12.3% | 79/134, 59.0% | 74/127, 58.3% (49.6–66.5); also without OP 72/123, 58.5% |

Excluding C and E rows does not change the result. The A/B share across all cohorts is 85.1%, against the 95% target. In the new cohort, all five C cards were KBO or NBL games settled from a single secondary source because the official scoreboard was stale or unreadable. KBO reached A on 0 of 6 cards.

Comparison-cohort evidence counts total 309 rows (A 164), excluding P-532's four shadow rows. The 2026-10-09 report's 313 rows (A 168) include them. This is a scope difference, not an error.

### 3.9 Process

Every new card is `Process: DEFICIENT` (20 of 20; `SOUND` 0).

| Deficiency named in R9 | Cards |
|---|---:|
| Lineups, starters, goalies or bench not verified from the official source | 20 |
| Distribution unvalidated or uncalibrated | 20 |
| No current-season archive file for the league | 20 |
| Late or unverified start (`LATE_START_UNVERIFIED`) | 13 |
| Single-secondary settlement source (evidence C) | 5 |
| Evidence custody: hash tokens without retained pages (`mini-log-3`) | 4 |
| Adjustment dependence or an unfitted adjustment (P-564, P-566, P-570; P-568 by counterfactual) | 4 |
| Probability-mass error (P-568 winner 67.8% + 30.2% = 98.0%) | 1 |

With no sound-process cards there is no comparison to make. By timing, `PREGAME` cards counted 13/14 (68.5–98.7%, Rank 1 6–1) and `LATE_START_UNVERIFIED` cards 21/26 (62.1–91.5%, Rank 1 10–3). The intervals overlap, so the difference is `INSUFFICIENT_EVIDENCE`.

### 3.10 New-format checks (P-557–P-576: `mini-log-3` ×4, `mini-log-5` ×16)

- **`ADJUSTMENT_DEPENDENT`:** 3 of 20 (15%): P-564, P-566, P-570. They counted 4/6 (Rank 1 2–1), against 30/34 (Rank 1 14–3) for the rest. P-568 is the gap case. Its adjustment (−1.80) is below 0.25 SD, so the flag reads `NONE`, but removing it changes the top two.
- **Regime flags:** 10 of 20 cards carry a flag. Seven use the §6 vocabulary and three use non-standard labels (P-569, P-570, P-576). A multiplier was applied once (P-571, NHL `EARLY_SEASON` 1.024), which is correct. Every other flag correctly applied no shift. `REGIME_IGNORED`: 0.
- **`Evidence quotes: NONE`:** 0 of 16. The four `mini-log-3` cards carry hash tokens with no retained pages.
- **Evidence mix by provider:** official or field-owner records on 8 cards (Bundesliga, easyCredit BBL, Liiga, B.LEAGUE ×2, NHL with CBS, a Czech club with Hokej.cz, a Go Ahead Eagles club page). Structured third-party or multi-source on 7 (MyKBO ×3, RealGM ×2, FBref with soccerzz, Sofascore with Score24). Single secondary on 5 (MyKBO ×2, Yonhap, Austadiums, an NBL news story).
- **SLA breaches:** 0. All 20 were settled within 72 hours, and open carryover is 3 (cap 5).
- **Family-rule classes after the rules took effect:** `TENNIS_IID_UNDERDISPERSION`, `FIRST_HALF_GOAL_OVERSELECTION` and `RUNLINE_CUSHION_CEILING` each recurred 0 times, but with almost no exposure (§3.7).

### 3.11 Rules, sources and past results used

- **`Rules read`:** present on 16 of 16 `mini-log-5` cards, each naming the sport file, the SELECTION_RULES sections and a SOURCES route (§3.1, §3.2, §3.4 or §3.9). The four `mini-log-3` cards predate the field.
- **`Archive check`:**

  | Archive check | Cards | Counted | Rank 1 |
  |---|---|---|---|
  | Real rows read | 4 of 16 (P-564 KBO 2025, 874 rows; P-565 and P-566 NBL 2025, 206 rows; P-571 NHL 2024–25 files) | 6/8 | 2–2 |
  | Headers and profile row only | 3 (P-572, P-573, P-575) | 6/6 | 3–0 |
  | `ARCHIVE_UNAVAILABLE` (exact reasons: header-only or missing league files) | 9 | 16/18 | 8–1 |

  The archive held no 2026 season file for any league in the cohort. Nothing here supports a claim that the archive check helps or hurts: `INSUFFICIENT_EVIDENCE`.

**Realised rates against the profiles** (ARCHIVE_USE_GUIDE §6; a gap is a finding about the cohort):

| League | Games | Home-win share | OT / extras | One-run | Total mean (SD) | Profile (seasons) | Gap |
|---|---:|---|---|---|---|---|---|
| KBO | 6 | 2/6 = 33% | 0/6 | 1/6 = 17% | 10.0 (5.22) | 9.77 (4.93); home win 51.5%; one-run 23.8% (2023–25) | none beyond noise |
| NBL | 4 | 1/4 = 25% | 0/4 | — | 207.8 (20.7) | 181.13 (19.53), 2022–24; BASE_RATES §7.1 2025-26: 182.5 (19.1), home win 50.3%, OT 5.5% | **+26.6 points; profile two seasons old** |
| NHL | 1 | 0/1 | 0/1 | — | 5 | 6.19 (2.31), 2023–25; OT 22.1% | n = 1 |
| CSL, Czech Extraliga, Korisliiga, Bundesliga, German BBL, Eredivisie, Liiga, B.LEAGUE PREMIER | 1–2 each | | | | | no profile row | not comparable |

**Profiles more than one season old:** NBL (2022–24 against a 2026-27 event). LEAGUE_PROFILES rule 3 requires a recompute (recommendation RET-01). The KBO profile shows an extra-innings share of 0.1% against MLB's 8.7%, which looks low for a league that plays to 11 innings. That is worth a prompt-7 check, though the cohort's 0 of 6 cannot test it.

### 3.12 Fitted models

**None exist** (CURRENT_STATE, Models). Rows against the HYPOTHESIS_REGISTER requirements, all within one week-block (2026-W41):

| Experiment | Status | Rows meeting the cohort rule (new cohort) | Paired rows (both methods priced) | Required rows / weeks |
|---|---|---:|---:|---|
| XCARD-1 soccer first-half goals | REGISTERED_NOT_RUN | 3 (P-561 R4, P-569 R1, P-569 R4) | 0 | 164 / 24 |
| XCARD-2 baseball ±1.5 run line | REGISTERED_NOT_RUN | 2 (P-558 R4, P-559 R4; both lost) | 0 | 170 / 22 |
| XCARD-3 basketball combined totals | REGISTERED_NOT_RUN (not feasible in 26 weeks) | 17 (15 won) | 0 | 214 / 36 |
| XCARD-4 tennis games | REGISTERED_NOT_RUN (not feasible) | 0 | 0 | 175 / 59 |
| XCARD-5 / SEL-1 gate | REGISTERED_NOT_RUN (not feasible) | 20 Rank-1 rows, 0 PASS | 0 | 6,633 / 332 |
| XCARD-6 Rank-2 diversification | REGISTERED_BLOCKED | 0 shadow rows graded (16 cards carry an A5 ladder) | 0 | 1,960 / 98 |

No card priced the baseline method beside the candidate method, so the paired comparison these experiments need is not being collected.

### 3.13 Expected-score accuracy (`mini-log-5`, P-561–P-576)

Error is final minus expected. The interval is mean ± t × s/√n. Full per-card values are in [COHORT_TABLES.md](COHORT_TABLES.md) §11.

| Sport | Term | n | Mean error | 95% interval | Mean \|z\| | \|z\| > 2 |
|---|---|---:|---:|---|---:|---|
| Basketball | total | 7 | +2.0 pts | −15.6 to +19.7 | 0.70 | 0/7 |
| Basketball | home / away / margin | 7 | +1.0 / +1.1 / −0.1 | all contain 0 | 0.50 / 0.74 / 0.53 | 0/7 each |
| Basketball, NBL | total | 3 | **+16.8** | −2.0 to +35.6 | 0.85 | 0/3 |
| Baseball (KBO) | total | 3 | +2.7 runs | −11.2 to +16.6 | 1.16 | 0/3 |
| Baseball (KBO) | home / away / margin | 3 | −0.8 / +3.5 / −4.3 | all contain 0 | 0.90 / 1.05 / 1.00 | away 1/3 (P-572 +2.19) |
| Ice hockey | total | 3 | +0.4 goals | −2.3 to +3.2 | 0.42 | 0/3 |
| Ice hockey | home / away / margin | 3 | +0.9 / −0.5 / +1.4 | all contain 0 | 1.37 / 0.79 / 1.51 | margin 1/3 (P-570 +2.28) |
| Soccer | total | 3 | +1.1 goals | −2.6 to +4.8 | 0.62 | 0/3 |
| Soccer | home / away / margin / first-half total | 3 | +0.2 / +0.9 / −0.7 / +0.1 | all contain 0 | 0.89 / 0.88 / 0.79 / 0.58 | 0/3 each |
| Soccer | second-half total | 2 | +2.1 | −11.8 to +15.9 | 1.51 | 1/2 (P-569 +2.32) |

- **Bias.** No bias in any total or team score is established. Every interval contains 0, so every cell is `INSUFFICIENT_EVIDENCE`.
- **Samples needed** to detect a bias, using the observed spread:
  - basketball total, 5 points: about 56 cards;
  - KBO total, 1 run: about 121;
  - soccer total, 0.3 goals: about 94;
  - ice hockey total, 0.5 goals (profile SD 2.31): about 82;
  - NBL total: about 3 more cards (6 in all), if the spread and the bias stay as observed.
- **Level against the profiles.**
  - **NBL:** expected levels were too low on 3 of 3 cards (P-565 +23.3, P-566 +8.5, P-575 +18.5). P-560's diagnostic centre (+46.6) makes it 4 of 4. Card centres of 175.5–191.5 sat close to the stale 181 profile, while the cohort's NBL games averaged 207.8.
  - **B.PREMIER:** one card high (P-576, −33.7) and one close (P-574, +6.4).
  - **KBO:** two totals high (P-564 +5.9 at Daejeon, P-572 +5.9) and one low (P-573 −3.8). KBO levels sat near the 9.77 profile, apart from P-564's park adjustment.
  - **Ice hockey:** totals matched (mean +0.4), but margins missed. Both large misses were goalie cases: P-570 +2.28 on a debutant starter, and P-571 −1.40 on an unconfirmed starter.
- **Widths.** Mean |z| on totals was 0.72 against about 0.80 for a correct normal width, with none beyond 2 SD. On this small sample the stated widths were not too narrow.

## 4. Failure-class and mechanism analysis

Every new-cohort Rank-1 loss belongs to one class, `OVERCONFIDENT_PROBABILITY` (4 cases), so it is analysed together.

| Card | Rank 1 (p) | Line distance from centre | Outcome | Width input behind the tail | Timing |
|---|---|---|---|---|---|
| P-560 NBL | Under 212.5 (90.0%) | +1.34 SD (centre 187.4, SD 18.7) | 234, z +2.49 | early-season NBL total SD, unfitted | completed 7.0 min after the start |
| P-564 KBO | Under 16.5 (88.0%) | +1.22 SD (11.07, 4.47) | 17, z +1.33 | park factor kept at 45% of the observed excess (`ADJUSTMENT_DEPENDENT`) | 3.2 min after |
| P-571 NHL | Florida +2.5 (88.4%) | −1.20 SD on the margin (+0.47, 2.48) | −3, z −1.40 | goalie mixture and empty-net tail, starter unconfirmed | 10.8 min after |
| P-576 B.PREMIER | Over 144.5 (89.9%) | −1.27 SD (171.66, 21.41) | 138, z −1.57 | new-format league, no profile row, SD not fitted | `PREGAME` (9.6 min before) |

**Shared mechanism.** Each card scanned a full ladder and placed Rank 1 on the line priced just under the 90% ceiling, about 1.2–1.3 SD from its own centre. That row loses only when the event lands in a single tail of roughly 10–12%. The tail width came from a parameter the card itself said was unfitted for that league or setting. In three of the four, lineups or goalies were unverified and the card was completed after the scheduled start.

**Knowable before the cutoff?** The width uncertainty was knowable, and every card disclosed it in A4 and in its sensitivity case. The specific outcome was not knowable: none of the four deep retrospections names a pre-cutoff catalyst, and each assigns 15–40% to variance. The z values (+2.49, +1.33, −1.40, −1.57) all lie inside 2.5 SD.

**What should have caught it.**
- **The A4 sensitivity case.** It is computed and then ignored. In P-564 the raw-park sensitivity would have moved the lines, yet the pick stayed at 88%.
- **The Rank-1 gate (SELECTION_RULES §2).** It flagged all four as `RANK1_UNSTABLE` but only labels the card; it does not change the pick.
- **LEAGUE_PROFILES.** P-576 had no row and P-560 had a stale row.
- **SOURCES lineup routes.** Lineups were unverified in three of the four.

None of these is a missed mechanism in the narrative sense. The class is a property of the selection rule: pricing at the ceiling turns any width or centre error directly into Rank-1 losses.

**Matched Rank-1 wins** (same sport, same family, same construction):
- **NBL totals** P-565, P-566 and P-575 sat 1.24–1.28 SD from centre. P-566 and P-575 were unverified starters completed after the start.
- **KBO totals** P-557, P-558 and P-573 sat at the same kind of line.
- **Ice hockey handicap** P-570 (HIFK +3.5) sat 1.16 SD out, also with a goalie adjustment.
- **B.PREMIER** P-574 (Over 139.5) sat 1.25 SD from centre against P-576's 1.27 SD.

The wins and the losses were built the same way and differ only in where the result fell. The four losses are about what the stated probabilities predict: 2.26 expected, 4 observed, P(4 or more) ≈ 0.18. **What works and must be kept** is the transparency that makes this analysis possible. Each card has one distribution, an expected score, the gate arithmetic and the joint-failure statement. Each deep retrospection computes the tail from the card's own grid and refuses hindsight re-ranking.

**Comparison cohort, for contrast.** Its 28 failures were dominated by selection and process faults that the current rules now block: first-half over-selection, run-line ceilings, q ranking, qualitative ranks and shared drivers (17 primary cases). What remains in the new cohort is the probability level itself.

## 5. What worked

- **One coherent distribution per card.** All 16 `mini-log-5` cards printed an expected score whose total is the centre the totals were priced from. The 80–90% bin realised 86.4% against 86.9% stated. Total |z| averaged 0.72, with 0 of 16 beyond 2 SD.
- **Endpoint handling.** OT, extras, three-way KBO ties and shootouts were resolved inside the grid on 20 of 20 cards, with no endpoint dispute at settlement. Of the 18 cards that printed both sides of the winner, 17 summed to 100%; the exception is P-568.
- **Settlement discipline.**
  - All 20 were settled within 72 hours.
  - Evidence codes were honest: C was used when the field owner was stale rather than claiming A.
  - Eight cards settled at A from field owners: Bundesliga, BBL, Liiga, B.LEAGUE, NHL, and two club official pages.
  - Settlements came from scorecards, not narratives.
- **Deep retrospections.** All four are complete in eight parts. Each locates the outcome in the card's own grid, separates variance from model and process, and refuses the hindsight swap to the winning alternative.
- **Regimes and family rules applied as written.** The NHL early-season 1.024 was applied. Unmeasured leagues were flagged without shifting the centre. No row fell in a forbidden family position at Rank 1.
- **Citation and evidence fields.** `Rules read` and `Evidence quotes` appear on 16 of 16 cards. All nine cards in leagues without a profile said that their numbers were their own (DST-13).

**Keep:**
- the one-distribution card, the expected score and the `Expected vs final` line;
- the gate and joint-failure lines printed with their numbers;
- the eight-part deep retrospection;
- the A/B/C evidence honesty;
- the 72-hour settlement SLA.

## 6. Recommendation register status

Source: [FRAMEWORK_RETROSPECTIVE_2026-10-09.md](../../../FRAMEWORK_RETROSPECTIVE_2026-10-09.md) §5 and §5.8. Its 2026-10-09 banner already marks the code-based items `SUSPENDED_MD_ONLY`. No later retrospective exists. Results are tested on the new cohort wherever the item's own acceptance test can be applied by hand.

| Status | Count | IDs |
|---|---:|---|
| `IMPLEMENTED` (documented hand rule) | 24 | SRC-02, SRC-08, PRD-01, PRD-02, PRD-03, PRD-05, PRD-06, PRD-07, PRD-08, PRD-09, DST-02, DST-07, DST-08, DST-09, DST-13, EVL-01, EVL-02, EVL-03, EVL-05, GOV-03, GOV-04, GOV-05, GOV-06, GOV-07 |
| `PARTLY_IMPLEMENTED` | 7 | SRC-07, DST-03, DST-04, DST-06, DST-10, DST-14, EVL-04 |
| `NOT_MET_OFFLINE` | 1 | SRC-04 |
| `SUPERSEDED` | 4 | SRC-03 (by `Evidence quotes`), SRC-06 (snapshot layout removed), GOV-01 (JSON pointer → CURRENT_STATE row), GOV-02 (hash custody → git custody and the numstat rule) |
| `SUSPENDED_MD_ONLY` | 21 | ENG-01, ENG-02, ENG-03, DST-01, ML-01, ML-02, SRC-01, SRC-05, PRD-04, DST-05, DST-11, DST-12, DST-15, ML-03, ML-04, ML-05, ML-06, ML-07, ML-08, ML-09, ML-10 |
| `NOT_IMPLEMENTED` | 0 | — |
| **Total** | **57** | |

**Implemented items against their acceptance tests:**

| ID | Where it lives now | Acceptance test (as registered) | Result on the new cohort |
|---|---|---|---|
| SRC-02 | CARD_AND_LOG_TEMPLATES §3 (`Settlement fields`, `Capture due`); SELECTION_RULES §1 | 0 no-provider VOIDs over 4 weeks | `INSUFFICIENT_EVIDENCE`: 0 VOIDs, but only 1 week |
| SRC-08 | SOURCES §E | registry lint passes | `MET` (by hand): no excluded or market source on 20/20; A9 `SPORTS_ONLY_MARKET_BLIND: PASS` |
| PRD-01 | CARD_AND_LOG_TEMPLATES §7 C3 | an inverted card is rejected | `MET`: 0/20 rank inversions, no q column |
| PRD-02 | SELECTION_RULES §3 | joint failure ≤ 0.30 on ≥ 80% of cards | `MET`, but degenerate: 20/20 at 0.0% by construction (§3.4) |
| PRD-03 | SELECTION_RULES §2 (provisional) | gated Rank 1 beats ungated by ≥ 5 points over 8+ weeks | `INSUFFICIENT_EVIDENCE`: 0 PASS cards, 1 week |
| PRD-05 | CURRENT_RULES §7.4; CARD_AND_LOG_TEMPLATES §4 | flag present on a replay of P-553 | `INSUFFICIENT_EVIDENCE`: no replay is possible. The flag appeared on all 3 cards where an adjustment above 0.25 SD changed the top two; P-568 shows a gap below the threshold |
| PRD-06 | CARD_AND_LOG_TEMPLATES §5 | addendum created for starter or goalie changes | `INSUFFICIENT_EVIDENCE`: no trigger inside the cohort (P-578's A8 addendum, outside it, shows use) |
| PRD-07 | SELECTION_RULES §6; BASE_RATES regime table | each flag has a fitted multiplier with CI in BASE_RATES | `MET` (the table exists). Use on cards was correct, with 3 non-standard labels |
| PRD-08 | SELECTION_RULES §1 (about 650 words) | median decision block ≤ 2.5 KB | `NOT_MET`: median 2,636 bytes (range 1,975–3,761). The 650-word limit was met on 20/20 (279–530 words) |
| PRD-09 | SELECTION_RULES §4 | failure classes removed | `INSUFFICIENT_EVIDENCE`: 0 recurrences, almost no exposure |
| DST-02 | CURRENT_RULES §7.3 | full-game P(home) + P(away) = 1 | `NOT_MET` on 1 of 18 cards with both sides printed (P-568: 98.0%) |
| DST-07 | SELECTION_RULES §4; PROBABILITY_TOOLKIT §2 | P(HT 0-0) within ±3 points per league | `INSUFFICIENT_EVIDENCE` (3 halves) |
| DST-08 | sport block (prompt 1) | one-run share by decile ±2 points | `INSUFFICIENT_EVIDENCE` (6 games) |
| DST-09 | sport block (prompt 1) | totals PIT flat; Over/Under within ±3 points | `INSUFFICIENT_EVIDENCE` (7 totals; mean \|z\| 0.70) |
| DST-13 | LEAGUE_PROFILES rule 4 | no silent default levels | `MET`: 9/9 cards in leagues without a profile stated their own numbers |
| EVL-01 | SCORING_AND_VALIDATION §7; SCOREBOARD | rebuilt from the settled tables | `MET`: this rebuild equals the import totals; spot check 5/5 |
| EVL-02 | SCORING_AND_VALIDATION §5 | week-block CI below 0 | `INSUFFICIENT_EVIDENCE`: no candidate method priced |
| EVL-03 | SCORING_AND_VALIDATION §5 | block structure honoured | `INSUFFICIENT_EVIDENCE`: k = 1 week |
| EVL-05 | SCORING_AND_VALIDATION §2 | cohorts shown separately | `MET` |
| GOV-03 | CARD_AND_LOG_TEMPLATES §9 S3, S6 | R1 blocks match their own card | `MET`: 20/20 |
| GOV-04 | card bullets | new cards carry all four contract fields | `MET`: 20/20 |
| GOV-05 | CURRENT_STATE (by hand) | README and CURRENT_RULES state no stale next ID | `MET` as written. Elsewhere, the Part 7 header (P-549/P-550) and GAME_LOG_STATUS_CURRENT lines 49–50 are stale |
| GOV-06 | Markdown-only tree | root holds documents and CSV only | `MET` (VERIFICATION_PROTOCOL §6.2 check) |
| GOV-07 | SELECTION_RULES §1; CURRENT_RULES §8 | open carryover ≤ 5 | `MET`: 3 open; 0 SLA breaches |

**Partly implemented items:**
- **SRC-07:** the matrix in SOURCES §F is a dated 2026-10-09 snapshot and has not been refreshed weekly, so `NOT_MET`. Cards do record their fallback routes.
- **DST-03:** basketball rows exist for 5 leagues, but 4 of 8 cohort basketball cards played in leagues without a row. The engine test does not apply by hand: `INSUFFICIENT_EVIDENCE`.
- **DST-04, DST-06, DST-10, DST-14, EVL-04:** `INSUFFICIENT_EVIDENCE`. There were no tennis, corners-ranked or NFL cards, only 3 hockey games, and no experiment run.

**Summary: implemented 24 (plus 7 partly), met 12, not met 3 (PRD-08, DST-02, SRC-07), insufficient evidence 16, suspended 21.**

## 7. New recommendations

Register format: `ID · Priority · Addresses · Recommendation · Acceptance test · Effort`. Each is `PROPOSED_NOT_TESTED`, is copied to [HYPOTHESIS_REGISTER.md](../../../HYPOTHESIS_REGISTER.md) under "Retrospective 2026-10-11", and changes nothing until the user approves it through prompt 8. Order of preference, per prompt 6: distribution method, then the candidate and ranking rule, then source and settlement.

| ID | P | Addresses | Recommendation | Acceptance test (pre-registered) | Minimum sample | Rollback condition | Effort |
|---|---|---|---|---|---|---|---|
| RET-01 | P1 | Finding 5; NBL expected totals low on 3/3 (+16.8); stale NBL profile (2022–24) | Distribution: recompute the NBL row of LEAGUE_PROFILES from 2025-26 and 2026-27 regular-season games (ARCHIVE_USE_GUIDE recipe R1, prompt 7). Require every card whose league row is more than one season old to print the recomputed level beside the stale one in A4. | On the next NBL cards, the mean `Expected vs final` total error has a 95% interval containing 0, and mean total \|z\| lies between 0.6 and 1.0 | 12 NBL cards over at least 4 week-blocks | Revert to the 2022–24 row if the mean error with the new row is larger in absolute value than +16.8 over the same 12 cards | S |
| RET-02 | P1 | Findings 1–3: hit rate measures line choice; Brier skill ≤ 0 | Ranking and measurement: every ranked row also prints `BASELINE_P`, the probability of the same row from the league row alone (LEAGUE_PROFILES or BASE_RATES, no team or lineup inputs; normal or Poisson tables from PROBABILITY_TOOLKIT). Settlement reports Brier(card) − Brier(baseline) for each row. The scoreboard headlines skill against baseline instead of the counted rate. | Cards add information on the rows they rank first: week-block mean of Brier(card) − Brier(baseline) over Rank 1 and Rank 2, with the 95% interval's upper bound below 0 | 8 week-blocks and at least 40 cards | Drop the field if two independent recomputations of `BASELINE_P` differ by more than 2 points on more than 10% of rows, which would mean the baseline cannot be priced consistently by hand | M |
| RET-03 | P1 | Finding 4: gate unreachable (0/20 PASS, margin ≤ 2.5) | Candidate rule: alongside the current gate, shadow-score a gate whose "best non-complementary alternative" excludes other lines on the same quantity. The 62% and 4-point values stay unchanged. Print both labels. Feeds SEL-1 instead of replacing it. | Under the shadow definition, PASS cards' Rank-1 win rate exceeds `RANK1_UNSTABLE` cards' by at least 5 points over 8+ week-blocks, and PASS-card calibration (stated against realised) stays within its Wilson interval | 8 week-blocks; at least 30 PASS cards under the shadow definition | Abandon the shadow gate if fewer than 20% of cards PASS under it after 4 weeks (it would be as unreachable as the current one), or if PASS cards win less often than UNSTABLE cards | S |
| RET-04 | P1 | §3.4: P(both lose) = 0 by construction on 20/20; Hit@2 mechanical | Ranking rule: Rank 2 must be on a different quantity from Rank 1 (not the same total or team total at another line, and not the opposite side of Rank 1's handicap). Joint failure is then computed from the grid cells (SELECTION_RULES §3). Until adopted, cards print the shadow Rank 2 under this rule, graded from the final (this also unblocks XCARD-6). | Realised `TOP2_ALL_LOST` stays within the Wilson interval of the mean stated P(both lose), and the shadow Rank 2's Brier skill against `BASELINE_P` is at least that of the current Rank 2 | 40 cards over at least 4 week-blocks | Revert if realised `TOP2_ALL_LOST` exceeds 35% with the Wilson lower bound above 30% (the SELECTION_RULES §1 warning) | S |
| RET-05 | P1 | Finding 5: 12/20 cards completed after the scheduled start | Source process: a card completed after the scheduled start, or within 5 minutes of it, is scored in a `LATE_START` sub-cohort shown separately on the scoreboard, in the way `RANK1_UNSTABLE` is | At least 90% of the next cards are `PREGAME` with research completed at least 5 minutes before the scheduled start | 40 cards | Return to label-only if the rule leaves more than 20% of requested events without a card | S |
| RET-06 | P2 | §3.8: KBO 0/6 at evidence A; 3/6 at C | Settlement: settle KBO from the official KBO box score at least 12 hours after the final, and record when the official scoreboard is stale. Keep MyKBO as the B corroboration. | At least 8 of the next 10 KBO cards settle at A | 10 KBO cards | Revert to MyKBO + Korean daily agreement (B) if the official route returns a non-terminal record for any settled game | S |
| RET-07 | P3 | §3.5, §3.10, §6: P-572 gate line without numbers; 3 non-standard regime labels; P-568 winner mass 98.0% | Card self-audit: C5 shows the gate numbers, C8 uses the §6 vocabulary (other context goes in A6), and C4 extends to the winner line, whose masses must sum to 100% | 0 violations of the three checks | the next 40 cards | none needed (an audit check, not a forecasting rule); drop any check that produces false positives on more than 2 of 40 cards | S |

## 8. Limits

- **Sample size.** The new cohort has 20 events from one ISO week (40 counted rows, 80 graded rows). Every comparison needs at least 8 week-blocks, so no conclusion here is established, and every comparative statement above is `INSUFFICIENT_EVIDENCE` unless an interval says otherwise.
- **Dependence between rows.** The four rows of a card share one event, and in this cohort Rank 1 and Rank 2 were complementary by construction. Wilson intervals on counted rows treat the rows as independent and understate uncertainty. Hit@2 and the counted rate describe the rank structure, not independent forecasting skill ([SELECTION_RULES §3](../../../SELECTION_RULES.md#3-rank-2-and-the-joint-failure-probability)).
- **Non-comparable cohorts.** The comparison cards used older formats, mixed proposition types, and some legacy rank orders and q scores. Their probabilities are not in the settlement tables, so their calibration, joint failure, process verdict and expected-score accuracy are `NOT_COMPUTABLE`.
- **Evidence-grade mix.** A quarter of new-cohort rows rest on single-secondary evidence (C); the result was unchanged without them. A/B share 85.1% overall against the 95% target.
- **What the cards are.** Uncalibrated analyst scenarios built by hand, often completed after the scheduled start and without official lineups. Nothing here is certified performance. A verified sporting result is not operator certification.
- **The analyst saw the new cohort's totals before this run.** The import report earlier the same day had already shown them. The scope follows mechanically from the prompt's rule, and no other window was analysed.
- **Arithmetic.** Wilson bounds, Brier sums and means were evaluated with a calculator from scratch copies outside the repository. Every input is printed in COHORT_TABLES so the figures can be redone by hand.
