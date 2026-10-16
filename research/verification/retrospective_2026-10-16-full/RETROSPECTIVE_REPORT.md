# Full-history retrospective 2026-10-16 (P-001 to P-600)

Mode `COHORT_RETROSPECTIVE` (prompt 6) across every card, then the changes the findings make necessary (prompt 8, [IMPLEMENTATION.md](IMPLEMENTATION.md)). The review itself changes no rule, forecast, grade or ID. All records are `RESEARCH_ONLY_NOT_CERTIFIED`, and every probability is an uncalibrated analyst number: no fitted model priced any card in the history.

## 1. Scope

Full scope, reading receipt and construction checks: [DATA_INVENTORY.md](DATA_INVENTORY.md). Every row and generated table: [HISTORY/CARD_ROWS.csv](HISTORY/CARD_ROWS.csv) and [HISTORY/CARD_HISTORY.md](HISTORY/CARD_HISTORY.md), produced by `python -m ml card-history` with an input/code receipt.

| Item | Value |
|---|---|
| Cards | 599 records P-001–P-600 (P-584 pending, excluded); 570 graded; 562 with graded counted slots; 29 with no gradable row |
| Rows | 2,311 card × rank rows; 837 graded rows with a stated p (214 cards) |
| Dates / weeks | 2026-07-29 to 2026-10-16; 12 ISO weeks (W31–W42) carry graded Rank-1 rows |
| Eras | E1a ≤ 09-08 · E1b 09-09–09-24 · E2 09-25–10-08 · E3 10-09–10-11 · E4 ≥ 10-12 |
| Trigger / level | User request; counters `NOT_DUE` (empty store); content COMPREHENSIVE |
| Rank log used | The committed blob at `b86f89d37`. An uncommitted refresh by another session was not used |

## 2. Executive summary

**Findings**

1. **Rank 1 carries a modest, real signal; Rank 2 does not.**
   - Rank 1 won 352–207 (63.0%, 58.9–66.9%), Rank 2 298–229 (56.5%, 52.3–60.7%) and Ranks 3–4 572–457 (55.6%, 52.5–58.6%).
   - Within the same card, Rank 1 beat the card's own Ranks 3–4 by +7.7 points (card-weighted; week-cluster bootstrap +1.7 to +12.5). The week-mean t-interval is −0.8 to +28.1, so the direction is supported but the size is imprecise.
   - Excluding the 21 colliding IDs changes nothing: Rank 1 62.8%, Rank 2 57.2%. Settling every unresolved or conflicted row either way moves Rank 1 only within 62.6–63.2%.
2. **The cards are mildly overconfident at Rank 1, and recalibration does not fix it out of sample.**
   - **Rank 1:** where a stated p exists, Rank 1 won 130 of 206 against 139.6 expected (−4.6 points; week-cluster bootstrap −10.0 to −0.7).
   - **All 837 rows:** slope 0.82 (SE 0.11), ECE 3.6 points, Brier 0.2247 against in-sample climatology 0.2410 and a coin 0.25. The 0.6–0.7 bin realised 59.2% against 63.9% stated; the 0.8–0.9 Rank-1 band realised 79.5% against 87.3%.
   - **Chronological study:** fitted on rows before 2026-09-14 and tuned on 09-14 to 09-25, it selected IDENTITY. On the 227 later rows a Platt refit would have changed Brier only from 0.2072 to 0.2063. Disposition: no calibration change.
3. **Skill against a strong baseline is still unmeasurable, because baselines were almost never frozen.** Four events in 600 carry a same-row BASELINE_P. Every skill figure above is against in-sample climatology, which is descriptive only.
4. **No model ever priced a card.** The history holds no V1/V2/V3 bundles, no frozen model shadows and no Hedge feedback, and the learning store is empty. Seven V3-era cards record `No module named ml`. The model lane is built but disconnected from the cards.
5. **Where cards did well and badly, by sport:**
   - **Strong:** soccer Rank 1 103–32 (76.3%, 68.5–82.7%), and baseball 118–67 (63.8%).
   - **Weak:** American football 7–12 (36.8%), Australian rules 13–14 (48.1%), rugby league 9–10 (47.4%), tennis 24–16 (60%) but 0–2 in the latest cohort.
   - **In-sample Brier skill** (descriptive): basketball +0.17, cricket +0.17, soccer +0.10; tennis −0.16, AFL −0.43, American football −0.12.
   - **Families at Rank 1:** winner 70.2%, period 67.9% (mostly first-half Over 0.5), total 64.2%, handicap 60.1%.
6. **Each policy era produced the hit rate its line levels implied.**

   | Era | Rank 1 | Rank 2 | ALL_LOST cards |
   |---|---|---|---|
   | E1a | 62.2% | 50.9% | 49 of 264 |
   | E1b | 63.5% | 60.4% | 32 of 187 |
   | E2 (q-ranking) | 56.4% | 56.4% | 9 of 39 |
   | E3 (ceiling ladder, ~87% lines) | 75.0% | 92.9% | 0 of 28 |
   | E4 | 62.5% (5–3) | 28.6% (2–5) | 2 of 7 |

   In-sample skill stayed between −0.08 and +0.06 in every era with stated probabilities.
7. **Data integrity needs repair before the history can train anything.**
   - **ID collisions:** 21 IDs carry two different events, including a shifted block P-139–P-153.
   - **Unrecorded probabilities:** 62% of graded cards (mostly E1a) record no stated p.
   - **Unsettled rows:** 47 rows are UNRESOLVED and 11 CONFLICT.
   - **Rank-log lag:** the committed rank log stops at P-583 and disagrees with the effective final settlement on 10 rows.

**Implemented now** ([IMPLEMENTATION.md](IMPLEMENTATION.md), P-2026.10.16-v19.2 / CR-R6 / LEARN-v1.1):
- `python -m ml capability`: the runtime receipt required before any ML_NOT_RUN.
- `python -m ml baseline`: a standalone same-line BASELINE_LEAGUE_V1, tested equal to V3's league expert.
- Shadow-ledger adapters for V3 and tennis bundles.
- `python -m ml card-history`: this review's reproducible tables.
- Prompt 1: one identical runtime/baseline/contract-definition paragraph in all eleven workflows (Upcoming blocks byte-identical) and the tennis prospective-shadow step.
- Prompt 6: uses the history tool.

**Still to do** (`PROPOSED_NOT_TESTED`, §9): RET-14 repair the ID collisions (prompt 7); RET-15 backfill the history into the learning store (extends RET-09); RET-16 a sport-cell monitoring test for American football, AFL and rugby league.

## 3. Quantitative analysis

### 3.1 Slots and the 2026-10-09 baseline

| Scope | Cards | Rank 1 | Rank 2 | Ranks 3–4 | Ranks 5+ |
|---|---:|---|---|---|---|
| All history | 562 | 352–207 (63.0%, 58.9–66.9) | 298–229 (56.5%, 52.3–60.7) | 572–457 (55.6%, 52.5–58.6) | 45–41 (52.3%) |
| Excluding 21 colliding IDs | 544 | 340–201 (62.8%) | 291–218 (57.2%) | 552–441 (55.6%) | 43–38 (53.1%) |
| P-001–P-522 (this table) | 496 | 307–186 (62.3%) | 253–209 (54.8%) | 491–409 (54.6%) | — |
| 2026-10-09 full history (P-001–P-522) | 522 | 304–187 (61.9%) | 251–211 (54.3%) | 491–414 (54.3%) | — |

The two P-001–P-522 lines differ only by the ten effective-grade corrections (P-217, P-265 and P-401 Rank 1 resolved; P-407 and P-409 PUSH literals graded). Since 2026-10-09, P-523–P-600 added 45–21 at Rank 1 and 45–20 at Rank 2. That increase comes mostly from the E3 ceiling ladder.

### 3.2 Dependence-aware Rank-1 tests (rows → card → ISO week)

| Test | Weeks | Cards | Week-mean (95% t) | Card-weighted mean (week-cluster bootstrap 95%) |
|---|---:|---:|---|---|
| Rank 1 realised − stated p | 8 | 206 | +0.018 (−0.233 to +0.268) | **−0.046 (−0.100 to −0.007)** |
| Rank 1 win − same card's Ranks 3–4 mean | 12 | 526 | +0.136 (−0.008 to +0.281) | **+0.077 (+0.017 to +0.125)** |

Equal week weighting gives single-card weeks (W35, W36, W40) the same weight as 68-card weeks, so the t-intervals are dominated by noise. The card-weighted means with week-cluster resampling are the better summary, and both point the same way: Rank 1 is better than the card's own lower rows and slightly worse than it claims.

### 3.3 Card classes

Of 526 cards with two decisive counted slots: ALL_WON 198 (37.6%), SPLIT 236 (44.9%), ALL_LOST 92 (17.5%). The ALL_LOST rate fell from 18.6% (E1a) and 17.1% (E1b) to 0% in E3. That is mechanical: E3 ranked complementary brackets, as shown on 2026-10-11. Mechanical protection was recorded explicitly only from P-557, so Hit@2 for earlier eras cannot be split into protected and unprotected pairs: `NOT_COMPUTABLE`.

### 3.4 Calibration

| Stated p | Rows | Cards | Mean stated | Realised | Wilson 95% |
|---|---:|---:|---:|---:|---|
| < 0.3 | 5 | 5 | 0.258 | 0.600 | 0.231–0.882 |
| 0.3–0.4 | 71 | 65 | 0.362 | 0.394 | 0.289–0.511 |
| 0.4–0.5 | 185 | 129 | 0.446 | 0.519 | 0.447–0.590 |
| 0.5–0.6 | 233 | 160 | 0.552 | 0.536 | 0.472–0.599 |
| 0.6–0.7 | 142 | 114 | 0.639 | 0.592 | 0.509–0.669 |
| 0.7–0.8 | 79 | 49 | 0.742 | 0.734 | 0.628–0.819 |
| 0.8–0.9 | 116 | 42 | 0.863 | 0.853 | 0.778–0.906 |
| ≥ 0.9 | 6 | 4 | 0.907 | 0.833 | 0.436–0.970 |

**Overall.** Logistic intercept +0.08 (SE 0.08), slope 0.82 (SE 0.11). The slope is 1.6 SE below 1, so mild overconfidence is suggested, not established. Rows are dependent: about four per card, often complementary pairs.

**Rank 1 by stated band:**

| Band | Rows | Realised | Stated |
|---|---:|---:|---:|
| 0.50–0.55 | 13 | 53.8% | 52.3% |
| 0.55–0.60 | 44 | 54.5% | 57.3% |
| 0.60–0.65 | 52 | 55.8% | 62.1% |
| 0.65–0.70 | 29 | 65.5% | 67.0% |
| 0.70–0.80 | 24 | 70.8% | 73.8% |
| 0.80–0.90 | 39 | 79.5% | 87.3% |

The shortfall concentrates at 0.60–0.65 and 0.80–0.90; below 0.60 Rank 1 rows behave like coin flips. The 2026-10-09 recommendation that Rank 1 come from rows at 0.65 or above is consistent with this.

**Chronological calibration study** ([CALIBRATION](CALIBRATION/CALIBRATION_RECEIPT.csv)). Windows were fixed before the results were seen: fit before 2026-09-14 (224 rows), tune 09-14 to 09-25, test from 09-26 (227 rows).
- **Tune-window Brier:** identity 0.2247, prior-shrunk Platt 0.2261, isotonic 0.2294. IDENTITY was selected.
- **Test window:** Brier 0.2072, slope 0.75.
- **Sensitivity only:** a Platt refit at the tune end would have scored 0.2063 on the test window.

Result `CALIBRATION_STUDY` → NO_CHANGE. Overconfidence is visible in sample, but a correction learned from earlier cards does not transfer to later ones, which used different line levels.

### 3.5 Eras (stated-p rows; skill is against in-sample climatology, descriptive)

| Era | Graded cards | Cards with p | Rows | Brier | Climatology | Skill | Rank 1 | Rank 2 |
|---|---:|---:|---:|---:|---:|---:|---|---|
| E1a | 297 | 9 | 30 | 0.2402 | 0.2489 | +0.035 | 183–111 (62.2%) | 135–130 (50.9%) |
| E1b | 189 | 144 | 564 | 0.2295 | 0.2447 | +0.062 | 120–69 (63.5%) | 113–74 (60.4%) |
| E2 | 39 | 26 | 105 | 0.2682 | 0.2482 | −0.081 | 22–17 (56.4%) | 22–17 (56.4%) |
| E3 | 28 | 27 | 108 | 0.1482 | 0.1566 | +0.054 | 21–7 (75.0%) | 26–2 (92.9%) |
| E4 | 16 | 14 | 30 | 0.2421 | 0.2500 | +0.032 | 5–3 (62.5%) | 2–5 (28.6%) |

E2 (rank-by-q, Markdown-only) is the only era with negative in-sample skill. E3's hit rates came from line levels, as found on 2026-10-11. No era beats its own climatology by more than about 6%.

### 3.6 Sports (Rank 1 / Rank 2; Brier on stated-p rows)

| Sport | Cards | Rank 1 | Rank 2 | p rows | Brier | Skill |
|---|---:|---|---|---:|---:|---:|
| Soccer | 136 | 103–32 (76.3%, 68.5–82.7) | 80–44 (64.5%) | 210 | 0.2039 | +0.10 |
| Baseball | 186 | 118–67 (63.8%, 56.6–70.4) | 95–84 (53.1%) | 297 | 0.2391 | +0.03 |
| Basketball | 67 | 37–29 (56.1%) | 40–23 (63.5%) | 152 | 0.1925 | +0.17 |
| Cricket | 52 | 31–21 (59.6%) | 28–20 (58.3%) | 44 | 0.2052 | +0.17 |
| Tennis | 40 | 24–16 (60.0%) | 18–19 (48.6%) | 48 | 0.2900 | −0.16 |
| Australian rules | 27 | 13–14 (48.1%) | 13–11 (54.2%) | 14 | 0.3586 | −0.43 |
| American football | 19 | 7–12 (36.8%, 19.1–59.0) | 6–13 (31.6%) | 24 | 0.2797 | −0.12 |
| Rugby league | 19 | 9–10 (47.4%) | 8–11 (42.1%) | 24 | 0.2367 | +0.05 |
| Ice hockey | 9 | 6–3 (66.7%) | 5–2 (71.4%) | 24 | 0.1937 | +0.06 |
| Rugby union / unclassified | 2 / 5 | 1–1 / 3–2 | 2–0 / 3–2 | — | — | — |

Only soccer's Rank-1 interval clears the all-history 63%. American football's interval (19–59%) sits mostly below it. These are the only sport cells with any separation, and with 19 cards each, American football, AFL and rugby league are `INSUFFICIENT_EVIDENCE` for a rule change (RET-16 proposes the test).

### 3.7 Proposition families at Rank 1

| Family | Rank 1 |
|---|---|
| Winner (ML, double chance) | 40–17 (70.2%, 57.3–80.5) |
| Period (first half, powerplay, quarters) | 36–17 (67.9%, 54.5–78.9) |
| Total | 122–68 (64.2%, 57.2–70.7) |
| Handicap | 113–75 (60.1%, 53.0–66.8) |
| Other / no contract text | 33–27 (55.0%) |
| Corners / player | 5–2 / 3–1 |

The period cell is mostly soccer first-half Over 0.5. That family was restricted on 2026-10-09 (FIRST_HALF_GOAL_OVERSELECTION), because its losses clustered at Rank 1 although its rate looked high. A high rate is not evidence of value without the baseline it lacked.

### 3.8 Frozen baselines and paired evidence

Four events in the history carry a frozen same-row baseline: P-581, P-582, P-587 and P-589 (2026-10-16 cohort review: card − baseline Brier +0.0107 on 2 weeks). Paired skill for the other 595 cards is `NOT_COMPUTABLE`. That does not show the absence of skill; it shows that skill was never measured. The new `python -m ml baseline` command removes the technical barrier for supported sports.

### 3.9 Weekly drift

Rank 1 (stated-p rows) ran close to expectation in W37 (32 against 33.6), W38 (43 against 44.6) and W39 (20 against 20.9). It fell short in W41 (28 against 34.1), the ceiling-ladder week. Only 8 weeks have stated-p Rank-1 rows, and none shows a sustained trend.

### 3.10 Integrity

- **Identity collisions (21 IDs).**
  - **The shifted block P-139–P-153:** each ID is titled with one event in the first heading series and the previous ID's event in the second, for example P-140 "Red Sox @ Yankees" and "Astros @ Mets".
  - **Others:** P-155, P-156, P-160, P-272 (Osaka v Siniakova and Geelong v Carlton), and P-370/P-415 (closed administratively, later reused).

  Which event each rank-log grade belongs to cannot be settled without the prompt-7 repair. The headlines move by at most 0.7 points when these IDs are excluded.
- **Effective grades.** Ten rank-log rows were stale against the effective final settlement; the effective grade was used (DATA_INVENTORY §3). An uncommitted refresh in another session addresses these and appends P-585–P-600. Once published, `card-history` reads it without double counting (tested).
- **Unresolved rows.** 47 UNRESOLVED and 11 CONFLICT rows. The Rank-1 bounds are 62.6–63.2% and the Rank-2 bounds 56.0–57.0%.
- **Missing probabilities and timing.** 62% of graded cards have no stated p, and issue timing is UNKNOWN for nearly all cards before 2026-10-09. Calibration and timing strata are `NOT_COMPUTABLE` for them.

## 4. Failure classes across the history

| Review | Rank-1 losses classed | Dominant classes |
|---|---:|---|
| 2026-10-09 (final-settlement cohort P-126–P-556) | 28 | First-half over-selection 5, run-line cushion ceiling 4, shared driver 5, basketball total without pace model 3, tennis IID underdispersion 3, rank by q 3 |
| 2026-10-11 (P-557–P-576) | 4 | `OVERCONFIDENT_PROBABILITY` 4 (ceiling lines 1.2–1.3 SD out) |
| 2026-10-16 (P-577–P-589) | 3 | Tennis underdispersion (hypothesis), small-sample overreach, weak Rank 1 |

The classes moved from selection faults (fixed by rules from 2026-10-09) to the probability level itself (ceiling pricing, overconfidence). That matches §3.4: the remaining loss mechanism is stated probabilities about 4–8 points too high at the top of the scale. Every deep review refused hindsight re-ranking, and none identified a missed pre-cutoff catalyst as the main cause.

## 5. Model lanes and the comprehensive-review components

| Component (LEARN-v1 §6–7) | Status | Reason |
|---|---|---|
| Immutable training release per scope | NOT_RUN | Learning store empty: no cohort card has a RESEARCH_EXPORT and no backfill exists |
| V3-equivalent backtest | NOT_RUN | No admitted reviewed history; the retired results store is not a source |
| Hedge schedule study | NOT_RUN | Needs a backtest ledger |
| Basketball challenger ablation | NOT_RUN | Needs a release |
| Prospective shadow evaluation | NOT_RUN | Shadow ledger empty (0 frozen rows ever) |
| Calibration study | **RUN** on card probabilities | IDENTITY selected; NO_CHANGE (§3.4) |
| Assisted cohorts V1/V2/V3 | None issued | 0 bundles, 0 warm/feedback, η never admitted |
| Workshop `-r1` outputs | HISTORICAL_DEVELOPMENT only | Not prospective, never matched to card issuance |

## 6. Research completion, sources and timing

Research-completion receipts exist only from 2026-10-15 (RC-v1). Older cards are not restamped. Their process verdicts stay as written: `DEFICIENT` on 20/20 in the 2026-10-11 cohort, with lineups unconfirmed on nearly all recent cards. Source closure is unchanged from the queues in the import reports (DATA_INVENTORY §4 of the 2026-10-16 cohort review). The history adds the identity-collision repair and the rank-log refresh to the open work. Operator terms and verified final times are unknown throughout, so no 72-hour SLA can be verified retrospectively.

## 7. Register status

| ID | Status after the full history |
|---|---|
| RET-01 / FC10-PROFILE | 0 NBL events since registration |
| RET-02 / FC10-BASELINE | 4 events in the whole history; the barrier is now addressed by `python -m ml baseline` |
| RET-03 / FC10-GATE | 3 shadow-gate events; SEL-1 0 PASS across 2 of 8 week-blocks (W41, W42) since the gate began |
| RET-04 / FC10-PAIR | 3 events; correctly conditioned joint masses now standard on supplied-first cards |
| RET-05 / TIMING-COMPLETE | Superseded; descriptive only (§3.10: timing unknown before 2026-10-09) |
| RET-06 | KBO evidence-A target 0/1 since registration |
| RET-07 | Monitoring continues |
| RET-08 runtime | **IMPLEMENTED (mechanism):** capability receipt and prompt-1 bootstrap; acceptance still to be measured on the next 40 cards |
| RET-09 backfill | Open; extended by RET-15 |
| RET-10 baseline | **IMPLEMENTED (mechanism):** standalone baseline and prompt-1 requirement; coverage to be measured |
| RET-11 tennis shadow | **IMPLEMENTED (mechanism):** adapter and prompt-1 tennis step |
| RET-12 margin coverage | Monitoring |
| RET-13 contract definitions | **IMPLEMENTED (procedure):** prompt-1 definition gate |

## 8. Review dispositions (appended to `research/learning_status/REVIEW_LOG.csv`)

Level COMPREHENSIVE, scope ALL, plus every sport with a model lane. `through_at` is 2026-10-16T15:18:45+11:00 (latest settled availability).

| Scope | Disposition | Evidence |
|---|---|---|
| ALL | `DATA_REPAIR_REQUIRED` | No model output in 599 cards; empty store; 21 ID collisions; stale rank log |
| Baseball, Basketball, Soccer, Ice Hockey, American Football, AFL, Rugby League, Rugby Union, Cricket T20, Cricket One-Day Format (V3 lanes) | `INSUFFICIENT_EVIDENCE` | 0 V3 forecasts; analyst cards only; 4 baseline-paired events in total |
| Tennis (experimental lane) | `PROSPECTIVE_SHADOW` | Adapter now exists; the prompt-1 tennis step freezes shadows; tennis Rank 1 60% overall, 0–2 recently, skill −0.16 |

No scope is `PROMOTION_ELIGIBLE`, and no registry entry changes.

## 9. Recommendations still open (`PROPOSED_NOT_TESTED`)

| ID | P | Addresses | Recommendation | Acceptance test | Minimum sample | Rollback |
|---|---|---|---|---|---|---|
| RET-14 | P1 | 21 ID collisions | Prompt 7 identity repair: for each colliding ID, establish the original card/settlement pairing from the frozen original bodies and record a dated identity addendum. Never renumber issued cards | Every colliding ID has a single verified event mapping or an explicit UNRESOLVED_IDENTITY disposition; `card-history` collision list reconciles | 21 IDs | None (additive addenda) |
| RET-15 | P1 | Empty store; history unusable for learning | Extends RET-09: backfill RESEARCH_EXPORTs for settled historical cards in supported sports from their cited prior-game rows and terminal results, field-owner re-verifying each result, starting with E3–E4 | `learning-status` counts ≥ 80% of supported-sport terminal cards; every quarantine has a reason | Supported-sport cards P-001–P-600 | Quarantine, never edit, on failure |
| RET-16 | P2 | American football 7–12, AFL 13–14 and rugby league 9–10 at Rank 1 | Monitoring test per sport: frozen BASELINE_P (now available) beside every Rank 1 in these sports; compare paired Brier after 8 weeks | Paired card − baseline Brier interval per sport | 8 weeks and 30 events per sport | None (monitoring) |

RET-08, RET-10, RET-11 and RET-13 now have mechanisms. Their acceptance tests (registered 2026-10-16) start counting from the next cards.

## 10. What worked

- **Literal records made a reproducible history possible.** The table rebuilt the 2026-10-09 history to within ten documented corrections.
- **The deep-review format.** Three reviews over 35 classed Rank-1 losses, with no hindsight re-ranking.
- **Honest disposition.** Every V3-era card states its no-model disposition truthfully.
- **Rule-driven removal of selection faults after 2026-10-09.** Failure classes moved from selection to probability level.

## 11. Limits

- **Outcome exposure and dependence.** Every number is outcome-exposed and descriptive. The rows of a card share one event and are often complementary, and teams repeat. Only 8–12 ISO weeks carry the relevant rows.
- **Derived classification.** Sport, family, dates and eras come from documented rules over the records, audited by random samples, not from re-reading every card body.
- **Missing inputs.** Most early cards lack stated probabilities and timing, and almost none carry baselines. In-sample climatology is not a skill benchmark.
- **A timestamp error in the earlier review.** The 2026-10-16 cohort review's eight review-log rows state `recorded_at` 20:45 although their commit was made at 20:35:59. The value was pre-filled; the correction is recorded in [IMPLEMENTATION.md](IMPLEMENTATION.md) rather than by editing the append-only log.
- **The rank log.** The committed log stops at P-583, and its later cards come from the import inventories. A pending refresh by another writer will supersede the stale rows.
