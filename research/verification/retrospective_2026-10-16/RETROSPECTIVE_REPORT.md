# Cohort retrospective 2026-10-16 (P-577 to P-600)

Mode `COHORT_RETROSPECTIVE` (prompt 6, P-2026.10.16-v19.1, LEARN-v1 §§6–8). This report measures, explains and recommends. It changes no rule, model, forecast, grade, ID or prompt. Every recommendation is `PROPOSED_NOT_TESTED`. All records are `RESEARCH_ONLY_NOT_CERTIFIED`, and every probability is an uncalibrated analyst scenario; no fitted primary model priced any card in this cohort.

## 1. Scope

Full scope, reading receipt, exposure and per-ID sources: [DATA_INVENTORY.md](DATA_INVENTORY.md). All inputs and tables: [COHORT_TABLES.md](COHORT_TABLES.md).

| Item | Value |
|---|---|
| HEAD | `bd813b5ab` (equal to `origin/main`) |
| Trigger | User request. LEARN-v1 counters give INTERIM/COMPREHENSIVE `NOT_DUE` because the learning store is empty; 22 newly terminal cards |
| Counted cohorts | C1 pre-v10 carryovers P-577–P-579 (3 cards); C2 v10 P-580–P-582 (3); C3 SUPPLIED_FIRST_V1 P-585–P-589 (5). 11 cards, 22 primary rows, events 2026-10-11 to 2026-10-14, ISO weeks W41–W42 |
| Separate cohort | Legacy retained research P-590–P-600: 11 events, 46 supplied propositions, analyst diagnostics only (`NOT_PRIMARY`), events 2026-10-14 to 2026-10-16 |
| Qualitative / excluded | P-583 `NO_FORECAST` (terminal). P-584 `PENDING_EVENT`, excluded |
| Comparison | 2026-10-11 cohorts: P-557–P-576 (34/40 counted, 85.0%) and P-126–P-556 (79/134, 59.0%) |
| Outcome exposure | Retrospective: import totals had been read before this run; they were reproduced independently from the row inventories |

## 2. Executive summary

**Findings**

1. **No fitted model touched this cohort, and the learning layer cannot see it.** PRIMARY_HEDGE_MIX_V3 executed on 0 of 24 cards. Of the 11 cards issued after primary ML was authorised (P-590–P-600):
   - 7 document the same capability failure, `No module named ml`, in the operator's environment;
   - 1 is tennis (`NOT_IMPLEMENTED`);
   - 3 record no attempt.

   Ten of those eleven had at least one family the runtime supports. No cohort card carried a RESEARCH_EXPORT, so `python -m ml learning-status` reports 0 settled, 0 admissible, 0 forecast, 0 feedback and 0 prospective games. The binding constraint is runtime reachability and data flow, not model design.
2. **The counted rate again reflects line choice.** C1+C2 cards ranked ladder lines near the 90% ceiling: 10/12 = 83.3% (55.2–95.3%) against 10.53 expected, z −0.47, Brier skill +0.02 against in-sample climatology. C3 supplied-first cards ranked the user's lines near 50%: 5/10 = 50.0% (23.7–76.3%) against 5.72 expected, z −0.46, skill +0.05. Both cohorts won about what their own probabilities said, and neither shows skill.
3. **Where a frozen baseline exists, the cards did not beat it.** Eight primary rows on 4 events carry a numeric BASELINE_P. Card Brier 0.2195 against baseline 0.2088, an event-then-week difference of +0.0107 (card worse), over 2 ISO weeks: `INSUFFICIENT_EVIDENCE`. Baseline coverage is 8/22 primary rows; FC10-BASELINE has 4 of its 40 events.
4. **Calibration: nothing established; margins may be too narrow.** The 80–90% bin realised 85.7% against 87.4% stated (n = 21), and the logistic slope is 1.09 (SE 0.42). Totals look correctly wide (mean |z| 0.89, 7/10 inside the 80% band). Margins do not: mean |z| 1.05, and only 2 of 10 inside the central 50% band (chance 0.055). Winner calls were right on 5 of 11. This is a warning, not a finding.
5. **Rank 1 performed at expectation; supplied-first Rank 2 did not.** All counted Rank 1 rows: 8–3 against 8.24 expected (z −0.18). The three losses split two tennis cards (P-577 at 89.9%, P-585 at 52.5%) and one soccer total (P-581, z +2.36). C3 Rank 2 went 1–4 against 2.78 expected.
6. **Legacy analyst diagnostics leaned the wrong way, and their extra-time frequency is anomalous.** The highest-probability analyst row won on 3 of 9 events (mean stated 61.7%). Rows stated at 50–70% realised 38.9%, and rows below 50% realised 66.7%. Four of the seven basketball/NFL legacy events went to overtime (P-592, P-597, P-598, P-599). That would happen about 4 times in 10,000 at a 6% per-game rate (27 in 10,000 at 10%). These rows are not primary and change no grade, but every extra-time result must be re-verified at its field owner before any training admission.
7. **Process limits persist.**
   - **Timing:** only 7 of 24 cards were written before their scheduled or estimated start, and none has a verified actual start.
   - **Lineups:** both sides' line-ups were confirmed from official sources on 1 card (P-581).
   - **Contract definitions:** three events carried an ambiguous definition (P-577 handicap unit, P-596 regulation versus shootout moneyline, P-598 "−8.5 ML").
   - **Settlement checks:** operator terms and final wall-clock times are unknown everywhere, so the 72-hour SLA cannot be verified.

**Recommendations** (all `PROPOSED_NOT_TESTED`; §9)

- **RET-08 (P1):** make the primary runtime reachable from where cards are written, or route model execution to a maintainer executor, with a capability receipt on every card.
- **RET-09 (P1):** backfill structured exports for this cohort into the learning store through an authorised prompt 7/8 change. Re-verify the legacy extra-time results at field owners first.
- **RET-10 (P1):** require a same-line league BASELINE_P on supplied-first cards, as P-587 and P-589 already did.
- **RET-11 (P2):** freeze TENNIS_EXPERIMENTAL_HEDGE_V1 as a prospective shadow on every tennis request.
- **RET-12 (P2):** monitor margin-width coverage on the next 40 cards.
- **RET-13 (P2):** add a contract-definition gate to prompt 1, so a unit or action ambiguity is resolved or explicitly frozen before pricing.

## 3. Quantitative analysis

### 3.1 Headline

| Cohort | Cards | Primary W–L | Rate (95% CI) | Mean stated | Expected | z | Brier | Skill vs in-sample climatology |
|---|---:|---|---|---:|---:|---:|---:|---:|
| C1 pre-v10 | 3 | 5–1 | 83.3% (43.6–97.0) | 89.6% | 5.38 | −0.51 | 0.1437 | −0.03 |
| C2 v10 | 3 | 5–1 | 83.3% (43.6–97.0) | 85.8% | 5.15 | −0.18 | 0.1296 | +0.07 |
| C3 supplied-first | 5 | 5–5 | 50.0% (23.7–76.3) | 57.2% | 5.72 | −0.46 | 0.2364 | +0.05 |
| All counted | 11 | 15–7 | 68.2% (47.3–83.6) | 73.9% | 16.25 | −0.65 | 0.1820 | +0.16 |
| 2026-10-11 new cohort | 20 | 34–6 | 85.0% (70.9–92.9) | 87.0% | 34.8 | — | 0.131 | −0.03 |

The pooled "+0.16 skill" is an artefact of mixing two cohorts with very different base rates, so the in-sample climatology mean is not a fair comparator. Within each cohort, skill is −0.03 to +0.07. The like-for-like test is the frozen baseline (§3.6). Policies stay separate. C3 used a user-local selection scope (`SUPPLIED_FIRST_V1`) that must never be pooled with P_ORDER_V2. **Sample needed:** 8 week-blocks and 40 events with a same-row baseline (FC10-BASELINE-v1), of which 4 events in 2 weeks exist.

### 3.2 Slots

| Cohort | Rank 1 | Rank 2 | Ranks 3–4 (PUSH excluded) |
|---|---|---|---|
| C1+C2 | 4–2 (30.0–90.3%) | 6–0 (61.0–100%) | 10–2 (55.2–95.3%) |
| C3 | 4–1 (37.6–96.4%) | 1–4 (3.6–62.4%) | 4–4 (21.5–78.5%) |
| All counted | 8–3 (43.4–90.3%) | 7–4 (35.4–84.8%) | 14–6 (48.1–85.5%) |

As in every earlier cohort, the slots do not separate propositions. Rank 1 won 8 of 11 where its own probabilities expected 8.24 (SD 1.35, z −0.18). C3 Rank 2 is the weakest cell, 1–4 against 2.78 expected. On five events that is `INSUFFICIENT_EVIDENCE`. Supplied-first Rank 2 rows sat at 51.6–62.3%, so one win or fewer in five has a probability of 0.12 under the stated values.

### 3.3 Calibration

| Stated p | Rows | Mean stated | Realised | Wilson 95% |
|---|---:|---:|---:|---|
| < 50% | 8 | 44.1% | 50.0% | 21.5–78.5% |
| 50–59% | 7 | 55.1% | 42.9% | 15.8–75.0% |
| 60–69% | 4 | 63.0% | 50.0% | 15.0–85.0% |
| 70–79% | 2 | 77.4% | 100% | 34.2–100% |
| 80–89% | 21 | 87.4% | 85.7% | 65.4–95.0% |
| ≥ 90% | 0 | — | — | — |

All 42 decisive numeric rows of C1–C3: logistic intercept −0.17 (SE 0.48), slope 1.09 (SE 0.42), calibration-in-the-large +1.9 points, ECE 8.2 points. The high bin matches its stated level again, as on 2026-10-11 (86.4% against 86.9%). The rows are dependent (four per event, complementary pairs), so the SEs are optimistic. Result: `INSUFFICIENT_EVIDENCE`, no recalibration indicated. The calibration study tool (`python -m ml calibration`) needs out-of-sample model predictions, which this cohort does not have.

### 3.4 Joint failure and Hit@2

| Group | Cards | Stated P(both lose) | Realised `ALL_LOST` |
|---|---:|---|---|
| Mechanically protected (P-577, P-578, P-579, P-581, P-587) | 5 | 0% by construction | 0/5 |
| Not protected (P-580, P-582, P-585, P-586, P-588, P-589) | 6 | mean 12.56% (1.86–19.59%); expected 0.75 | 1/6 (P-585) |

Hit@2 is 10/11 cards, but 5 of those 10 are guaranteed by construction. The unprotected cards realised 1 `ALL_LOST` against 0.75 expected, consistent with their stated joint probabilities. C3 cards priced actual joint masses from common score states (P-586 19.59%, P-588 18.06%, P-589 17.83%). That is the correctly conditioned behaviour RET-04 asked for, and it is what makes Hit@2 informative again.

### 3.5 Gates and frozen shadows

- **Gate.** No counted card passed. C1/C2: 6/6 `RANK1_UNSTABLE` (margins 0.1–3.2 points). C3 supplied-scope gate: 4 `RANK1_UNSTABLE` and 1 `FAIL_FLOOR` (P-586, 58.4% < 62%). SEL-1 now has 2 of 8 week-blocks with 0 PASS cards. The gate stays provisional and unchanged.
- **RET03 shadow gate** (printed on C2 only): P-580 UNSTABLE, P-581 shadow PASS (its Rank 1 lost), P-582 UNSTABLE. That is 3 events toward FC10-GATE-v1's 8 weeks and 30 shadow-PASS cards.
- **RET04 and XCARD6 shadow Rank 2** (C2 only), graded from the finals:
  - RET04: P-580 Under 8.5 W, P-581 "either team wins in regulation" W, P-582 1H Under 2.5 W.
  - XCARD6: P-580 Motor +2.5 W, P-581 Over 1.5 W, P-582 FT Over 1.5 W (mechanically protected).

  Three events toward FC10-PAIR-v1's 40. These are shadows; they never replace the original Rank 2.
- **C3 shadows.** `SHADOW_BASE_ONLY` on all five cards: 10 rows 5–5, Brier 0.2339 against the card's 0.2364, a base-only scenario marginally better. `SHADOW_RANK_DELTA` only on P-587 (Ducks ML L / Flames +1.5 W). RET03/RET04/XCARD6 were `NOT_COMPUTED` under the supplied-only scope. C1 cards predate these fields; nothing was backfilled.

### 3.6 Frozen same-row baselines

| Card | Primary rows | Card Brier | Baseline Brier | Card − baseline |
|---|---|---:|---:|---:|
| P-581 (Danish Superliga, league-only Poisson) | R1 L, R2 W | 0.3615 | 0.3674 | −0.0060 |
| P-582 (EPL 2025–26 league-only) | R1 W, R2 W | 0.0134 | 0.0089 | +0.0045 |
| P-587 (NHL 2025–26 empirical, 1,312 games) | R1 W, R2 L | 0.2622 | 0.1816 | +0.0807 |
| P-589 (NHL 2025–26 empirical) | R1 W, R2 L | 0.2411 | 0.2774 | −0.0363 |

Event means averaged within ISO week, then across 2 weeks: **+0.0107** (card worse). With k = 2 weeks this is `INSUFFICIENT_EVIDENCE`; no interval is meaningful. Adding the four informational rows that carry a baseline gives +0.0075 on 12 rows. The 2026-10-11 cohort had no baseline at all, so this is the first paired evidence. It does not establish incremental skill, and it does not establish its absence.

### 3.7 Expected score against final

| Term | Cards with SD | Mean z | Mean \|z\| | \|z\| > 2 | Inside central 50% | Inside central 80% |
|---|---:|---:|---:|---|---|---|
| Total | 10 | +0.43 | 0.89 | 1 (P-581, +2.36) | 5/10 | 7/10 |
| Margin | 10 | +0.07 | 1.05 | 0 | 2/10 | 8/10 |

A correct normal width gives a mean |z| of about 0.80, half the outcomes inside the 50% band and 80% inside the 80% band.
- **Totals.** They look right, with a slight high bias (+0.43 mean z: P-577 +1.72 tennis, P-581 +2.36, P-589 +1.15). Basketball totals ranged from −32.1 (P-588, NBA preseason) to +18.6 (P-578, NBA preseason). Preseason rotations widen both tails.
- **Margins.** They cluster in the shoulders: 6 of 10 beyond 1 SD (about 3.2 expected) and 2 of 10 inside the 50% band (chance 0.055). Winner calls were right on 5 of 11.

This is the one distributional signal in the cohort, and it is `INSUFFICIENT_EVIDENCE` on 10 cards. RET-12 proposes the monitoring test. It matters because handicap rows are priced from these margins.

### 3.8 Timing, evidence and sport

| Stratum | Cards | Primary W–L | Brier |
|---|---:|---|---:|
| Written after the scheduled start (`LATE_START_UNVERIFIED`) | 8 | 12–4 | 0.1635 |
| Written before an estimated start, actual unverified (P-577, P-585, both tennis) | 2 | 1–3 | 0.3402 |
| Written before the scheduled start, actual unverified (P-582) | 1 | 2–0 | 0.0134 |
| Evidence A / B | 6 / 5 | 10–2 / 5–5 | — |

No cohort card is a certified pre-start issue, and the timing strata confound sport and policy. The two pre-estimate cards are the two tennis cards, so the timing rows cannot be read as a timing effect. Under TIMING-2026.10.15-v2 there is no fixed deadline. TIMING-COMPLETE-v1 monitoring records 7 of 24 cards written before their scheduled or estimated start, 15 after and 2 unverified. By sport, Rank 1 went basketball 4–0, ice hockey 3–0, soccer 1–1 and tennis 0–2. Every cell is far below any registered sample.

### 3.9 Legacy retained cohort P-590–P-600 (separate, NOT_PRIMARY)

- **Propositions.** 46 rows on 11 events: 23 W, 21 L, 2 UNRESOLVED (P-596 Saryarka ML, P-598 Huima −8.5 ML). The 37 numeric decisive analyst rows have mean squared error 0.2861 and log loss 0.7704, worse than a constant 0.5 (0.25 and 0.693). P-597 and P-598 are non-numeric. P-591's original Rank 1 (Under 172.5, 63.9%, `PASS_NUMERIC_UNCALIBRATED`) won. P-590 and P-592 original Rank 1 rows lost.
- **Highest analyst row per event.** It won 3 of 9 (12.1–64.6%), at a mean stated 61.7%. Totals leaned wrong on P-590 (Under, WI 247), P-592 (Under, 151 after OT), P-594 (Under, 179), P-599 (Over 40.5, 31 after OT) and P-600 (Over 227.5, 205).
- **Calibration.** The bins are inverted: rows stated 50–70% realised 38.9% (n = 18), and rows below 50% realised 66.7% (n = 18). Complementary pairs mirror each other, so these are the same facts counted twice.
- **What this does not license.** These are late, mostly outcome-exposed or post-start research diagnostics. They never enter T2, Brier, calibration, model feedback or prospective claims, and no ranking conclusion follows from 9 events.

### 3.10 Extra-time anomaly (data-integrity flag)

Four of the seven basketball/NFL legacy events went to overtime (P-592 68–68, P-597 96–96, P-598 74–74, P-599 Denver–Seattle). P-596 was 3–3 and decided by shootout. Under a 6% per-game overtime rate, four or more of seven has probability 0.00039; at 10%, 0.0027.
- **Corroborated:** P-599 (Seattle official game centre, Final/OT, plus ESPN), P-597 (official NKL recap) and P-592 (both clubs).
- **Not corroborated:** P-598 rests on two secondary results with field-owner confirmation open.

Nothing here shows an error. The cluster is improbable enough, given the repository's history with synthetic match reports, that every extra-time result must be re-confirmed at its field owner before any of these events enters the learning store (RET-09, `DATA_REPAIR_REQUIRED`).

## 4. Rank-1 losses and failure classes

| Card | Rank 1 (p) | Line vs centre | Outcome | Deep-review class (settlement) | Timing |
|---|---|---|---|---|---|
| P-577 tennis | Under 33.5 games (89.9%) | +1.48 SD (24.37, SD 6.18) | 35 games (two tie-break sets), z +1.72 | `TENNIS_IID_UNDERDISPERSION` (hypothesis) | before the user's estimated start |
| P-581 soccer | Under 4.5 goals (82.45%) | +0.90 SD (2.944, SD 1.716) | 7 goals, z +2.36 | `SMALL_SAMPLE_STRENGTH_OVERREACH` / `OVERCONFIDENT_PROBABILITY` (hypotheses; nine-match sample) | written 66 min after kickoff |
| P-585 tennis | Over 23.5 games (52.5%) | −0.33 SD (25.47, SD 6.03) | 23 games, z −0.41 | `MODEL_TAIL_REALISATION / WEAK_RANK1` | before the provider's estimate (1.5 min) |

All three eight-part reviews exist in the settlement revisions. Each refuses hindsight re-ranking and locates the outcome in the card's own distribution.
- **Tennis.** Both tennis Rank 1 rows lost, and the 2026-10-09 baseline already listed tennis as a weak cell (Rank 1 2–3). Tennis has no implemented primary adapter, and its cards use hand-built point/set trees. P-577 lost in the upper tail: a ceiling-priced Under at 1.48 SD, defeated by two tie-break sets. P-585 lost a near coin-flip by one game.
- **Soccer.** P-581 is the cohort's only |z| > 2 total. The centre came from nine league matches; the 3–0 half-time and 2–2 second half sit in the right tail.
- **Matched wins** (same construction):
  - P-578 and P-579: ceiling-ladder basketball brackets at 89.7%/89.66%, won with z +0.78 and −0.27.
  - P-580: Liberec +2.5 at 89.2%.
  - P-582: Under 5.5 at 88.9%.

  They differ from the losses only in where the result fell. Expected Rank-1 losses were 2.76 and observed 3.
- **What carries over from 2026-10-11.** The ceiling-pricing mechanism (`OVERCONFIDENT_PROBABILITY` there, four of four) recurs in P-577. The other two losses are not ceiling picks. No named failure class from SELECTION_RULES §8 recurred at Rank 1 apart from the tennis hypothesis.

## 5. Model lanes, learning and research completion

| Check | Result |
|---|---|
| V3 executions (cards issued after the 2026-10-15 authorisation: P-590–P-600) | 0 of 11. 7 documented `No module named ml` (P-593, P-594, P-596–P-600); 1 `NOT_IMPLEMENTED` (P-595 tennis); 3 no attempt recorded (P-590–P-592, late drafts) |
| V3-supported family present | 10 of 11 events (all except P-595): first-innings total, basketball totals/handicaps, Kazakhstan ice hockey, MLS full-time goals, NFL |
| Cards before the authorisation (P-577–P-589) | Not applicable; no model lane existed |
| Frozen bundles / feedback rows / Hedge context coverage | 0 / 0 / 0. Warm/feedback and η admission: not exercised |
| Prospective model shadows | 0 frozen for any cohort event. Workshop `-r1` outputs remain `HISTORICAL_BACKTEST` (registry entry 7) |
| LEARN-v1 counters (`python -m ml learning-status`) | unique settled 0, ML-admissible 0, frozen forecasts 0, Hedge feedback 0, prospective 0. No cohort card has a RESEARCH_EXPORT; the store is empty until a prompt-4 ingest |
| EXEC-v1 / C21 honesty | Every legacy card states its no-model disposition truthfully with blank execution paths; none claims a run |
| Research completion (RC) | P-593, P-594 `COMPLETE_WITH_DOCUMENTED_GAPS`; P-599 `COMPLETE_NUMERICAL_ANALYST_COMPARISON_WITH_DOCUMENTED_MODEL_AND_SOURCE_GAPS`. P-596 retains only a retention narrative (its full A1–A9 draft was never supplied), so its research is `INCOMPLETE`. No early exit was caused by missing ML: each card continued its analyst work |
| Lineups | Official starting line-ups confirmed for both sides on 1 of 24 cards (P-581). Partial on P-582 (one side), P-587 and P-589 (projected goalies). Unconfirmed elsewhere |

The model lane exists in the repository but did not reach the cards. Three things are needed before V3 can produce evidence: an executable runtime where cards are written, reviewed HISTORY inputs (now automatable through `python -m ml ingest history` once the store holds data), and frozen bundles. This is a data and operations repair, not a model question.

## 6. Source closure (EXH-v1)

- **Field owners at settlement.** Evidence A on 6 of 11 counted cards (NBA, ACB, Czech federation, DBU, Liverpool official, NHL). B on 5: tennis providers ×2, EuroCup, NBA preseason, NHL secondary for P-589.
- **Legacy.** Two closures were recorded at import (P-596 canonical-core capture, P-599 owner result). 15 of 17 package rows remain open.
- **Open field tasks.** Corners for P-581 and P-582; P-583's box conflict; definitions for P-596 and P-598; owner confirmation for P-598 and P-600.
- **Unknown everywhere.** Operator action terms (24 events) and verified final wall-clock times. The 72-hour SLA is therefore `NOT_VERIFIED` for every record.
- **This review.** No source was re-fetched and no queue was closed. The extra-time re-verification (§3.10) is added to the queue.

## 7. Register status (Retrospective 2026-10-11 recommendations and FC10)

| ID | Registration | Status on this cohort |
|---|---|---|
| RET-01 / FC10-PROFILE-v1 | NBL profile refresh, 12 NBL events | 0 NBL cards; 0 events. `DATA_READY`, predictive acceptance `BLOCKED_DESIGN` (unchanged) |
| RET-02 / FC10-BASELINE-v1 | BASELINE_P, 40 events / 8 weeks | `RECORDING_ACTIVE`: 4 paired events (P-581, P-582, P-587, P-589), 2 weeks, mean +0.0107. Coverage 8/22 primary rows. Design inputs still unregistered |
| RET-03 / FC10-GATE-v1 | Shadow gate, 8 weeks / 30 shadow-PASS | 3 events (C2), 1 shadow PASS (P-581, Rank 1 lost). C3 not computable under the supplied scope |
| RET-04 / FC10-PAIR-v1 | Different-quantity Rank 2 shadows, 40 events / 4 weeks | 3 events graded (C2), RET04 3–0, XCARD6 3–0. C3 priced true joint masses on 4 of 5 cards |
| RET-05 | ≥ 90% buffered pregame | Superseded by TIMING-2026.10.15-v2. Descriptive: 7/24 written before the scheduled or estimated start |
| RET-06 | KBO evidence A on 8 of 10 | 1 KBO card (P-583, `NO_FORECAST`), settled B with a box conflict: 0/1 |
| RET-07 | Zero arithmetic/gate/vocabulary violations, 40 cards | Gate numbers printed on 11/11 counted cards; complements sum to 100% on every C3 card. Regime vocabulary not audited here. 11 of 40 cards observed |
| SEL-1 / XCARD-5 | Gate validation, 8 week-blocks | 2 of 8 blocks (W41, W42 for these cohorts), 0 PASS |

## 8. Review dispositions (appended to `research/learning_status/REVIEW_LOG.csv`)

Level: INTERIM, user-requested below the counter threshold. `through_at` is 2026-10-16T15:18:45+11:00, the latest settlement availability in the cohort. One disposition per reviewed scope with a model:

| Scope | Model lane(s) | Disposition | Evidence |
|---|---|---|---|
| ALL | V3 primary, LEARN-v1 pipeline | `DATA_REPAIR_REQUIRED` | 0/24 executions (7 capability failures); empty learning store; no exports; extra-time anomaly to verify |
| Basketball | V3 joint-normal; BKB-FEATURE-RIDGE-C1 (development) | `INSUFFICIENT_EVIDENCE` | 0 V3 forecasts on 10 basketball events; no release for an ablation |
| Ice Hockey | V3 count | `INSUFFICIENT_EVIDENCE` | 0 V3 forecasts on 4 events; 2 NHL cards carried an empirical league baseline |
| Soccer | V3 Dixon–Coles | `INSUFFICIENT_EVIDENCE` | 0 V3 forecasts on 3 terminal events; P-584 pending |
| Tennis | TENNIS_EXPERIMENTAL_HEDGE_V1 (development); primary `NOT_IMPLEMENTED` | `PROSPECTIVE_SHADOW` (recommendation) | Rank 1 0–2; the only path to tennis evidence is a frozen prospective shadow (RET-11). Nothing is promoted |
| Baseball | V3 count | `INSUFFICIENT_EVIDENCE` | 1 `NO_FORECAST` card |
| Cricket T20 | V3 first-innings | `INSUFFICIENT_EVIDENCE` | 1 legacy event (first-innings total supported, not run) |
| American Football | V3 joint-normal | `INSUFFICIENT_EVIDENCE` | 1 legacy event, not run |

No scope is `PROMOTION_ELIGIBLE`, and no registry entry changes.

## 9. New recommendations

Each recommendation is `PROPOSED_NOT_TESTED`, is copied to [HYPOTHESIS_REGISTER.md](../../../HYPOTHESIS_REGISTER.md) under "Retrospective 2026-10-16", and changes nothing until the owner authorises it through prompt 8. Order follows prompt 6: data and operations first, because no distribution or ranking question can be tested until the model and data reach the cards.

| ID | P | Addresses | Recommendation | Acceptance test (pre-registered) | Minimum sample | Rollback | Effort |
|---|---|---|---|---|---|---|---|
| RET-08 | P1 | Finding 1: 0/24 V3 runs; 7 `No module named ml` | Operations: give prompt 1 an executable route to the runtime. Either a pinned checkout plus `pip install -r ml/requirements.txt` in the operator environment, or a named maintainer executor that receives REQUEST/HISTORY/CONTRACTS and returns the verified bundle. Record a capability receipt (command, environment, exit status) on every card | ≥ 80% of the next 40 cards with a V3-supported family carry either an executed, verified bundle or a data/admission failure (not a capability failure) | 40 cards | None needed (an operational change); revert the executor route if it ever returns an unverified bundle | M |
| RET-09 | P1 | Finding 1, §3.10: learning store empty; extra-time anomaly | Data: under an authorised prompt 7/8 change, create RESEARCH_EXPORTs for P-577–P-600 from the retained research and settlements (prior-game rows actually cited, terminal results), after re-verifying every extra-time result at its field owner, and ingest them | `python -m ml learning-status` counts the cohort's terminal events; every quarantine has a reason; 0 extra-time results lack field-owner confirmation | 33 terminal events | Remove nothing: a failed backfill is quarantined, never edited | M |
| RET-10 | P1 | Finding 3: baseline coverage 8/22; C3 ≈ coin-flip | Measurement: supplied-first or otherwise, every supplied line prints a same-line `BASELINE_LEAGUE_V1` from the league's prior completed season (empirical frequency or league-only distribution), as P-587 and P-589 did for the NHL, or an enumerated reason | Baseline coverage ≥ 80% of primary rows on the next 40 cards; FC10-BASELINE reaches 8 weeks | 40 cards / 8 weeks | Drop if two independent recomputations differ by > 2 points on > 10% of rows | S |
| RET-11 | P2 | Tennis Rank 1 0–2; tennis primary `NOT_IMPLEMENTED` | Model evidence: on every tennis request, after the card is frozen and before the start, freeze TENNIS_EXPERIMENTAL_HEDGE_V1 rows in the prospective shadow ledger (`python -m ml prospective freeze`) for the supplied games/sets contracts it supports | Prospective evaluation against the card's analyst probabilities on identical contracts reaches its preregistered delta, or `INSUFFICIENT_EVIDENCE` is reported honestly | 8 weeks and the preregistered sample | Stop freezing if more than 20% of tennis requests cannot be priced by the model (coverage too low to be useful) | S |
| RET-12 | P2 | §3.7: margin \|z\| 1.05; 2/10 inside 50% | Distribution monitoring: report the share of realised margins inside the card's central 50% and 80% bands on the next 40 cards, by sport | Inside-50% share's 95% interval contains 50%, and inside-80% contains 80% | 40 cards | None (monitoring only) | S |
| RET-13 | P2 | P-577 handicap unit, P-596 regulation vs shootout ML, P-598 "−8.5 ML" | Card rule: before pricing, every supplied contract states its unit (sets/games/points/goals), period and action (regulation/OT/SO, push/void). An ambiguous supplied text is frozen with both readings and the operator definition queued, never silently chosen | 0 `UNKNOWN_DEFINITION` grades caused by an unrecorded definition on the next 40 cards | 40 cards | Revert if it blocks more than 10% of requested contracts from any numeric assessment | S |

## 10. What worked

- **Settlement and custody.** Every packet total reproduced exactly from the row inventories, with three independent recomputations agreeing to the last digit. Original ranks, probabilities and timing were copied literally, and no pending or ambiguous row was forced to a grade (P-584, P-596, P-598).
- **Honest model disposition.** No card invented a model run, receipt or `p_card`. Capability failures were recorded with their actual error.
- **C3 joint arithmetic.** Joint failure came from common score states (17.8–19.6%) instead of a 0% bracket, and the one `ALL_LOST` fell inside that stated risk.
- **Baselines where a league history existed.** The two NHL cards computed empirical baselines from 1,312 games, and the Danish and EPL cards from league-only Poisson. This is the pattern RET-10 extends.
- **Eight-part Rank-1 reviews.** All three are present, each locates the outcome in the card's own grid and refuses hindsight swaps.

**Keep:** the literal-original settlement chain, the shared joint-state arithmetic, the truthful `RESEARCH_ONLY_NO_MODEL` disposition and the deep-review format.

## 11. Limits

- **Sample size.** 11 counted cards (22 primary rows) over 2 ISO weeks, plus 11 legacy events. Every comparison is `INSUFFICIENT_EVIDENCE` unless stated otherwise. Eight weeks is a floor, not a power calculation.
- **Dependence.** Rows of a card share one event; complementary pairs mirror each other; teams repeat. Wilson intervals and logistic SEs understate uncertainty.
- **Mixed policies.** C1/C2 ceiling ladders, C3 supplied-first and legacy analyst rows answer different questions. Pooled numbers are shown only to reconcile totals.
- **Outcome exposure and timing.** This review saw all outcomes. No card in the cohort is a certified pre-start issue, and most were written after the scheduled start.
- **No sources re-fetched.** Grades rest on the committed settlement evidence and its stated grade. The extra-time anomaly is flagged, not resolved.
- **Arithmetic.** Computed by a helper outside the repository using `ml.core.metrics`; every input row is printed in COHORT_TABLES so the figures can be redone by hand.
