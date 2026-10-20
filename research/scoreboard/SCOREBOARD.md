# Scoreboard: current measurement and preserved historical results

## Cohort retrospective 2026-10-21 (P-601–P-622; descriptive, grades unchanged)

[Report](../verification/retrospective_2026-10-21/RETROSPECTIVE_REPORT.md) · [tables](../verification/retrospective_2026-10-21/COHORT_TABLES.md). Two ISO weeks, outcome-exposed, `INSUFFICIENT_EVIDENCE`.
- **ANALYST_PRIMARY_V1 (P-612–P-622, 11 cards).** Rank 1 6W/5L (54.5%, 28.0–78.7), Rank 2 5W/5L/1P; Hit@2 8/11; 0 covering pairs. Brier 0.2041 / log loss 0.5907 on 21 decisive slot rows; 11 wins against 12.86 expected.
- **Rank 1 by stated p.** 5W/0L at p ≥ 0.60; 1W/5L below, all five losses under the 0.62 gate.
- **Frozen BASELINE_P.** 8 of 50 rows (P-612, P-621): card − baseline Brier +0.0244.
- **Research-only P-601–P-611.** 25W/25L/2U, NOT_PRIMARY (analyst MSE 0.2429 on 44 rows).
- **Card-history on the refreshed committed rank log (through P-600).** Rank 1 342–201 (63.0%), Rank 2 293–219 (57.2%). This supersedes the 2026-10-16 tool figures because collided aliases are now graded UNRESOLVED; no grade changed.
- **Not yet in these figures.** P-606's settlement score (117–98 recorded, 116–98 actual; grades unaffected) and the unresolved P-604 corners await settlement revisions.

## Full-history retrospective 2026-10-16 (P-001–P-600; descriptive, grades unchanged)

[Report](../verification/retrospective_2026-10-16-full/RETROSPECTIVE_REPORT.md) · generated tables in `HISTORY/`. 599 card records (P-584 pending), 562 with graded counted slots: Rank 1 352–207 (63.0%, 58.9–66.9), Rank 2 298–229 (56.5%, 52.3–60.7), Ranks 3–4 572–457 (55.6%). 837 stated-p rows: Brier 0.2247 against in-sample climatology 0.2410, calibration slope 0.82; Rank 1 mildly overconfident (−4.6 points). Frozen same-row baselines on 4 events only; no model-priced card in the history. In-sample figures are descriptive, not skill against a baseline; every earlier section below is unchanged.

## Cohort retrospective 2026-10-16 (P-577–P-600; descriptive, grades unchanged)

[Report](../verification/retrospective_2026-10-16/RETROSPECTIVE_REPORT.md). Counted cohorts (policies kept separate): C1 pre-v10 P-577–P-579 and C2 v10 P-580–P-582, primary 10W/2L (83.3%, 55.2–95.3%) against 10.53 expected, Brier 0.1367; C3 SUPPLIED_FIRST_V1 P-585–P-589, primary 5W/5L (50.0%, 23.7–76.3%) against 5.72 expected, Brier 0.2364. Frozen same-row baseline on 8 primary rows / 4 events / 2 weeks: card − baseline Brier +0.0107, `INSUFFICIENT_EVIDENCE`. Legacy P-590–P-600 analyst diagnostics (NOT_PRIMARY): 37 rows, MSE 0.2861. PRIMARY_HEDGE_MIX_V3 executions 0 of 24; LEARN-v1 counters 0. No skill, calibration or model qualification is claimed; every earlier section below is unchanged.

## Current legacy settlement import — 2026-10-16T15:18:45+11:00

Highest canonical **P-600**; next **P-601**; active Combined Log remains Part 7. Inventory **116 retained research records = 115 terminal sporting-result reviews + 1 legacy pending P-584** (104 prior terminal + eleven P-590-P-600 result reviews). Four originals P-597-P-600 added; seven existing originals P-590-P-596 skipped; one P-590 reconciliation addendum and eleven revision-1 settlements retained. [Complete import/readback](../verification/mini_import_P-590_P-600_2026-10-16-1/CANONICAL_IMPORT_REPORT.md).

The supplied package reports **23 conditional sporting WIN / 21 LOSS / 2 UNRESOLVED** across 46 dependent supplied-contract rows; all eleven events still lack complete operator-action terms and exact final-at/SLA evidence. P-596 Saryarka ML and P-598 Huima −8.5 ML remain UNKNOWN_DEFINITION. These grades retain original rules and analyst roles; no current online-history/lineup compliance, fitted primary model, certified performance or pregame availability is backfilled. Model primary/baseline paired scores remain NOT_COMPUTABLE for this cohort; 37 descriptive analyst rows remain NOT_PRIMARY. Prior score cohorts retain their original figures. Raw carryover: 17 items, 2 closed by canonical-core/owner-result capture, 15 open; older P-581-P-584 and prior operator/time/custody queues remain. No automation scheduled.

Descriptive analyst diagnostics only: 37 rows (19 sporting wins, 18 losses), mean squared error 0.2860831243, mean log loss 0.7704050973, recomputed against original package analyst probabilities. This is not fitted-model Brier/calibration, not an independent 37-event sample and not a same-row baseline comparison. Original P-590-P-592 descriptive rank-1 1W/2L; row-2 1W/2L includes an explicitly informational P-590 row, so it is not promoted into a model T2 denominator. No verified new model feedback is generated.


## Research retention import - 2026-10-16T01:29:27+11:00
Seven retained records P-590-P-596 added for future source-backed settlement/development; tracked inventory 112: 104 prior terminal, legacy pending P-584, 7 awaiting outcome review. New source cohorts: 3 historical manual numeric originals P-590-P-592, 3 source NO_FORECAST originals P-593-P-595 and 1 RESEARCH_ONLY_NO_MODEL P-596. No model-assisted card or verified terminal label is added by this import. No new W/L/PUSH/VOID, T2, Brier/calibration/baseline score or prospective eligibility is inferred. Preserve every original rank/probability/status and actual timing; P-596 source-reported analyst probabilities are NOT_PRIMARY. [Complete import](../verification/framework_change_2026-10-16-1/CANONICAL_IMPORT_REPORT.md). Earlier dated scoreboard snapshots below are unchanged.

## Current import measurement - 14 October 2026 (SCV-2026.10.12-v7)

**Separate declared SUPPLIED_FIRST_V1 / SF-2 cohort P-585-P-589:** paired frozen same-row coverage **4/10 primary rows, 2/5 events, 1 ISO event week (2026-W42)**. Paired card Brier 0.251668318, baseline 0.229513269, difference **+0.022155049**; paired card log loss 0.696473369, baseline 0.648152595, difference +0.048320774. Event-equal and week-equal differences equal these row-equal differences because both paired events contribute two rows in the same week. **INSUFFICIENT_EVIDENCE**: one week, timing/known-at/lineage unverified, uncalibrated scenarios, no prospective certification or model promotion. This package's declared user-supplement policy is preserved, not adopted as current P_ORDER_V2 or pooled with its gate cohort.

Five original numeric research cards, 5/5 retained intake requests, zero no-card/qualitative/NO_FORECAST requests, zero pending new events; four inherited canonical references do not enlarge that denominator. Twenty original rows **9W/9L/2PUSH**, primary **5W/5L/0PUSH/0VOID/0UNRESOLVED** (50% decisive), Rank 1 **4W/1L**, Rank 2 **1W/4L**. Original primary Brier 0.236405693, log loss 0.665503988; all eighteen decisive rows (informational included, not extra primary wins) Brier 0.233534922, log loss 0.659649607. Frozen full-row baseline coverage 8/20; decisive baseline coverage 6/18. Three missing event baselines remain unavailable; no backfill. Rows use literal issued precision, including percentage-rounded P-585/P-586, not newly reconstructed probabilities.

Evidence A: P-587 four rows (1W/1L/2PUSH), primary 1W/1L; B: sixteen rows 8W/8L, primary 4W/4L. A/B headline equals A/B+C/E sensitivity; C/E/X new-grade contributions zero. Sporting definition FROZEN_FRAMEWORK_CONVENTION; operator action UNKNOWN separately. Five source winner calls 3 correct/2 incorrect remain winner diagnostics, never primary replacements.

Card classes 1 ALL_WON / 3 SPLIT / 1 ALL_LOST; Hit@2=4/5; both-loss 1/5. P-587 mechanically protected pair: separate construction diagnostic; excluding it Hit@2=3/4. P-585 actual first serve unverified and earliest estimated lead <=5 min; P-586-P-589 LATE_START_UNVERIFIED. Zero clean verified prospective cards. Supplied-scope gates retain source labels and are not current full-universe PASS cards. One mandatory Rank 1 loss review P-585; all five R1-R12 present.

Frozen BASE_ONLY shadow on the same ten keys: Brier 0.233933453, log loss 0.660276232, 5W/5L, NOT_PRIMARY. P-587 corrected RANK_DELTA orders Ducks ML LOSS / Flames+1.5 WIN (same underlying original keys); no extra event, no T2 win or model probability substituted. Prospective shadow eligibility NOT_VERIFIED.

Tracked research inventory increases from 100 to **105 records: 104 terminal / 1 pending (P-584)**. Inventory contains 102 numeric primary forecast cards under their differing original policies, two NO_FORECAST (P-532/P-583), one pending diagnostic-only (P-584). Historical pre-v10 and v10 tables below remain unchanged; current P_ORDER_V2 v11 eligible primary rows remain zero. P-581-P-584 have no effective new settlement revision; their evidence leads remain queued. Operators unknown on 13 events and final-time/SLA on 12 terminal records; custody missing five documents across two packages. Nothing is performance-certified.

[Import report](../verification/mini_import_P-585_P-589_2026-10-14-1/CANONICAL_IMPORT_REPORT.md), [complete original row inventory](../verification/mini_import_P-585_P-589_2026-10-14-1/IMPORTED_ROW_INVENTORY.csv), [current queue](../verification/mini_import_P-585_P-589_2026-10-14-1/UNRESOLVED_POST_IMPORT.md). No sporting sources were fetched by this import; grades/evidence are the supplied settlement's claims, with independent custody/contract arithmetic verification, not new field-owner certification.

## Current import measurement — 13 October 2026 (SCV-2026.10.12-v7)

**Paired baseline comparison:** 4 original primary rows on P-581/P-582, 2 v10 events, 1 ISO event week (2026-W41): card Brier 0.187418187, frozen baseline Brier 0.188131225, paired difference -0.000713038; card log loss 0.554631889, baseline log loss 0.550530220. Event-equal and week-equal Brier differences both -0.000713038 because each of the two events has two paired rows and both are in the same week. **INSUFFICIENT_EVIDENCE:** one week, below the framework's eight-week minimum; no validated incremental skill or clean prospective certification. Baseline provenance/known-at and actual-start gaps remain frozen.

| Original cohort | Retained events in this packet | Original numeric primary cards | Primary W / L / PUSH / VOID / UNRESOLVED | Primary Brier | Primary log loss | Paired baseline coverage |
|---|---:|---:|---|---:|---:|---|
| Pre-v10 carryovers P-577–P-579 | 3 | 3 | 5 / 1 / 0 / 0 / 0 | 0.143715020 | 0.473619130 | 0/6 primary rows |
| v10 P-580–P-583 | 4 | 3 | 5 / 1 / 0 / 0 / 0 | 0.129632290 | 0.411696198 | 4/6 primary rows; 2/3 numeric events |
| v11 P-584 | 1 | 0 | 0 / 0 / 0 / 0 / 0 | NOT_COMPUTABLE | NOT_COMPUTABLE | 0 eligible primary rows; pending diagnostic event |

Packet custody coverage: 8 events, 6 original numeric primary cards (12 primary rows), 1 NO_FORECAST (P-583), 1 numeric diagnostic-only card (P-584), 7 terminal records, 1 pending event. The source footer calls 4 of its 5 new cards numeric: 3 have original primary slates and the fourth is diagnostic-only. Request coverage is NOT_COMPUTABLE for the legacy mini-log-6 intake; do not infer 100% request retention. Full original row inventory: [IMPORTED_ROW_INVENTORY.csv](../verification/mini_import_P-577_P-584_2026-10-13-1/IMPORTED_ROW_INVENTORY.csv).

**Evidence/definitions:** primary A rows 10 (9 W/1 L), B rows 2 (1 W/1 L), C/E/X primary contributions 0. Headline A/B sporting view = sensitivity view, 10W/2L; all rows use their FROZEN_FRAMEWORK_CONVENTION and remain OPERATOR_UNKNOWN / NOT_CERTIFIED. This packet-only arithmetic is a reconciliation, never a pooled policy cohort. Informational original ranks 3–4: 10W/2L (pre-v10 5W/1L; v10 5W/1L); not primary wins. P-584's four ranked diagnostics, P-583's late numeric addendum and all other post-issue/shadow prices are excluded from primary scoring.

**Ranks and timing:** each three-card scored cohort has Rank 1 2W/1L and Rank 2 3W/0L; Hit@2 3/3 and both-loss frequency 0/3 in each. P-578/P-579 and P-581 have mechanically protected primary pairs (three of six); P-577/P-580/P-582 do not. All six source primary cards record RANK1_UNSTABLE; no PASS cohort is created. Pre-v10 P-577 retains its historical PREGAME label with estimated schedule/actual first ball unknown; P-578/P-579 are LATE_START_UNVERIFIED. V10 P-580/P-581 are late; P-582 is BUFFERED by scheduled lead but actual start remains NOT_VERIFIED. V10 P-583 is NO_FORECAST, with its timing correction LATE_START retained. V11 P-584 is LATE_START_UNVERIFIED and NOT_PRIMARY. No original label is upgraded by custody import.

**Historical reconciliation, preserving v5 literal conventions:** older 91 scored forecast cards through P-576 have 113W/61L plus 8 legacy VOID top-two slots. Effective newly settled pre-v10 P-577–P-579 add 5W/1L, so current historical pre-v10 inventory is **94 forecast cards, 118W/62L, 180 decisive rows (65.6%), 8 legacy VOID slots**. Rank 1 58W/33L/3V; Rank 2 60W/29L/5V. Historical RANK1_UNSTABLE cohort becomes 23 cards, 39W/7L, 46 decisive rows (84.8%); Rank 1 18W/5L, Rank 2 21W/2L; legacy classes 16 ALL_WON / 7 SPLIT / 0 ALL_LOST. UNKNOWN_GATE remains 71 cards, 79W/55L. Historical info ranks 3–4: prior 106W/67L + 5W/1L = 111W/68L. Original 2026-10-11 scoreboard snapshot below stays unchanged. Legacy VOID/no-evidence conventions, including P-418, remain literal and require a separate settlement-review task; no regrading or v7 headline recoding occurs here. [Historical primary reconciliation](../verification/mini_import_P-577_P-584_2026-10-13-1/HISTORICAL_PRIMARY_RECONCILIATION.csv) rebuilds every one of the older 182 primary slots; the old settled tables lack usable same-row frozen baselines/probabilities, so no historical proper score is invented.

Expected-vs-final totals were independently recomputed in the import receipt on the exact sport endpoints: P-577 +10.63 games / +1.720 SD; P-578 +18.63 points / +0.781 SD; P-579 −5.31 points / −0.265 SD; P-580 +1.3333 goals / +0.571 SD; P-581 +4.056 goals / +2.364 SD; P-582 −0.246 goals / −0.137 SD. Units are heterogeneous and never averaged together. P-583 original expected scores NOT_COMPUTED; P-584 lacks a terminal final. Predictive interval coverage NOT_COMPUTABLE. No shadow result absent from the settlement is manufactured.

Queues: [UNRESOLVED_POST_IMPORT.md](../verification/mini_import_P-577_P-584_2026-10-13-1/UNRESOLVED_POST_IMPORT.md): 1 pending event, 3 terminal field tasks, operator definitions over 8 IDs, final-time/SLA evidence over 7 terminal records, 4 missing companion documents. No automation scheduled; no record is performance-certified.

## Preserved release and historical scoreboard snapshot

## v10 prospective measurement (SCV-2026.10.11-v6)

At the October 11 framework release: **0 v10 issued cards; 0 paired-baseline events; 0 evaluated weeks; paired Brier/log-loss skill NOT_COMPUTABLE.** No historical baseline, timing or shadow is backfilled. Future updates report baseline-relative proper scores, expected-score accuracy and requested/issued/numeric/qualitative/NO_FORECAST/pending/unresolved coverage by original policy, timing, gate and evidence. See [scoring definitions](../../SCORING_AND_VALIDATION.md) and [implementation status](../verification/framework_change_2026-10-11-1/IMPLEMENTATION.md).

The figures below remain the original **SCV-2026.10.09-v5 historical snapshot**. They are not a v10 cohort or proof of predictive skill. Their in-sample climatology reference is not a frozen pregame comparator; mechanically protected Hit@2 must not be treated as event-specific predictive success. No number below was recomputed by the prompt revision.

Maintained by hand from the settled tables ([SCORING_AND_VALIDATION.md](../../SCORING_AND_VALIDATION.md) §7); figures below were generated on 2026-10-09 from the final-settlement table, cards P-126–P-556 (71 with forecasts), and updated by hand on 2026-10-11 with the 20 settled cards imported from the P-556–P-579 mini (P-557–P-576; P-577–P-579 are `PENDING_EVENT` and not scored). Rebuilt and refined from the settlement blocks by the [cohort retrospective of 2026-10-11](../verification/retrospective_2026-10-11/RETROSPECTIVE_REPORT.md) (new cohort P-557–P-576, comparison P-126–P-556); every number below agreed with the rebuild. Update after each import (prompt 4) and each retrospective (prompt 6), and copy the headline into CURRENT_STATE.md.

## Counted cohort (Rank-1 gate passed)

| Group | Cards | Counted | Rate | 95% CI | R1 W–L | R2 W–L | Won/Split/Lost |
|---|---:|---|---:|---|---|---|---|
| All counted | 0 | 0/0 | n/a | n/a | 0–0 | 0–0 | 0/0/0 |

Rule T2: only Ranks 1–2 count; PUSH/VOID leave the denominators. Hit@2 0 of 0. Mean NDCG@2 n/a over 0 slates.

## Cohorts shown separately (EVL-05)

| Group | Cards | Counted | Rate | 95% CI | R1 W–L | R2 W–L | Won/Split/Lost |
|---|---:|---|---:|---|---|---|---|
| COUNTED (gate passed) | 0 | 0/0 | n/a | n/a | 0–0 | 0–0 | 0/0/0 |
| RANK1_UNSTABLE | 20 | 34/40 | 85.0% | 70.9–92.9% | 16–4 | 18–2 | 14/6/0 |
| LEGACY_P_ONLY (full gate unknown) | 0 | 0/0 | n/a | n/a | 0–0 | 0–0 | 0/0/0 |
| UNKNOWN_GATE (not a recorded PASS) | 71 | 79/134 | 59.0% | 50.5–66.9% | 40–28 | 39–27 | 27/26/15 |
| All forecast cards (historical diagnostic) | 91 | 113/174 | 64.9% | 57.6–71.6% | 56–32 | 57–29 | 41/32/15 |

Missing gate results are never inferred to pass. Historical results remain visible independently of the prospective gate.
RANK1_UNSTABLE cohort (P-557–P-576, every card recorded `RANK1_UNSTABLE` before the event): Hit@2 20 of 20; mean NDCG@2 0.8387 over 20 slates. Most top-two pairs are bracketing totals or covering handicaps whose joint failure is 0% by construction, so the counted rate is not evidence of independent skill.
Informational ranks 3–4 (calibration only; never wins): 106–67 (61.3%, 95% CI 53.8–68.2%); in the RANK1_UNSTABLE cohort 31–9 (77.5%, 95% CI 62.5–87.7%), mean stated p 81.4%, Brier 0.164 (climatology 0.174). Historical cards: mean stated p n/a, Brier n/a.

## Does Rank 2 carry information?

| Slot | W–L | Rate | 95% CI |
|---|---|---:|---|
| Rank 1 | 56–32 | 63.6% | 53.2–72.9% |
| Rank 2 | 57–29 | 66.3% | 55.8–75.4% |
| Ranks 1–2 | 113–61 | 64.9% | 57.6–71.6% |
| Ranks 3–4 | 106–67 | 61.3% | 53.8–68.2% |

RANK1_UNSTABLE cohort only: Rank 1 16–4 (80.0%, 58.4–91.9%); Rank 2 18–2 (90.0%, 69.9–97.2%); Ranks 3–4 31–9 (77.5%, 62.5–87.7%).
UNKNOWN_GATE cohort only: Rank 1 40–28 (58.8%, 47.0–69.7%); Rank 2 39–27 (59.1%, 47.0–70.1%); Ranks 3–4 75–58 (56.4%, 47.9–64.5%); rank 5 (28 cards) 15–12.

Rank 1 does not beat Rank 2, and the intervals of Ranks 1–2 and Ranks 3–4 overlap heavily: the ranking is not separating propositions.

**Joint failure of the top two.** RANK1_UNSTABLE cohort: stated P(both lose) 0.0% by construction on 20 of 20 cards (disjoint losing events); realised `TOP2_ALL_LOST` 0/20 (0.0–16.1%). UNKNOWN_GATE cohort: stated value not recorded; realised 15/68 = 22.1% (13.8–33.3%). Because every RANK1_UNSTABLE pair covers itself, its Hit@2 of 20/20 is mechanical.

## By sport (counted cohort)

| Group | Cards | Counted | Rate | 95% CI | R1 W–L | R2 W–L | Won/Split/Lost |
|---|---:|---|---:|---|---|---|---|

## By month (counted cohort; month from the event key, else UNDATED)

| Group | Cards | Counted | Rate | 95% CI | R1 W–L | R2 W–L | Won/Split/Lost |
|---|---:|---|---:|---|---|---|---|

## Historical diagnostic by sport (all forecast cards)

| Group | Cards | Counted | Rate | 95% CI | R1 W–L | R2 W–L | Won/Split/Lost |
|---|---:|---|---:|---|---|---|---|
| Australian rules | 1 | 1/2 | 50.0% | 9.5–90.5% | 0–1 | 1–0 | 0/1/0 |
| Baseball | 20 | 26/40 | 65.0% | 49.5–77.9% | 13–7 | 13–7 | 7/12/1 |
| Basketball | 19 | 27/38 | 71.1% | 55.2–83.0% | 11–8 | 16–3 | 10/7/2 |
| Cricket | 1 | 0/2 | 0.0% | 0.0–65.8% | 0–1 | 0–1 | 0/0/1 |
| Ice hockey | 9 | 14/18 | 77.8% | 54.8–91.0% | 7–2 | 7–2 | 5/4/0 |
| Rugby league | 1 | 0/2 | 0.0% | 0.0–65.8% | 0–1 | 0–1 | 0/0/1 |
| Soccer | 33 | 42/62 | 67.7% | 55.4–78.0% | 23–9 | 19–11 | 18/7/7 |
| Tennis | 7 | 3/10 | 30.0% | 10.8–60.3% | 2–3 | 1–4 | 1/1/3 |

## By sport, RANK1_UNSTABLE and UNKNOWN_GATE cohorts

| Group | Cards | Counted | Rate | 95% CI | R1 W–L | R2 W–L | Won/Split/Lost |
|---|---:|---|---:|---|---|---|---|
| RANK1_UNSTABLE · Baseball | 6 | 10/12 | 83.3% | 55.2–95.3% | 5–1 | 5–1 | 4/2/0 |
| RANK1_UNSTABLE · Basketball | 8 | 14/16 | 87.5% | 64.0–96.5% | 6–2 | 8–0 | 6/2/0 |
| RANK1_UNSTABLE · Ice hockey | 3 | 4/6 | 66.7% | 30.0–90.3% | 2–1 | 2–1 | 1/2/0 |
| RANK1_UNSTABLE · Soccer | 3 | 6/6 | 100.0% | 61.0–100.0% | 3–0 | 3–0 | 3/0/0 |
| UNKNOWN_GATE · Baseball | 14 | 16/28 | 57.1% | 39.1–73.5% | 8–6 | 8–6 | 3/10/1 |
| UNKNOWN_GATE · Basketball | 11 | 13/22 | 59.1% | 38.7–76.7% | 5–6 | 8–3 | 4/5/2 |
| UNKNOWN_GATE · Ice hockey | 6 | 10/12 | 83.3% | 55.2–95.3% | 5–1 | 5–1 | 4/2/0 |
| UNKNOWN_GATE · Soccer | 30 | 36/56 | 64.3% | 51.2–75.5% | 20–9 | 16–11 | 15/7/7 (1 void) |
| UNKNOWN_GATE · Tennis | 7 | 3/10 | 30.0% | 10.8–60.3% | 2–3 | 1–4 | 1/1/3 (2 void) |
| UNKNOWN_GATE · Australian rules, cricket, rugby league | 3 | 1/6 | — | — | 0–3 | 1–2 | 0/1/2 |

## Historical diagnostic by month (all forecast cards)

| Group | Cards | Counted | Rate | 95% CI | R1 W–L | R2 W–L | Won/Split/Lost |
|---|---:|---|---:|---|---|---|---|
| 2026-10 | 39 | 53/76 | 69.7% | 58.7–78.9% | 26–12 | 27–11 | 19/15/4 |
| UNDATED | 52 | 60/98 | 61.2% | 51.3–70.3% | 30–20 | 30–18 | 22/17/11 |

## Rank 1 by proposition family

| Family | Counted W–L | 95% CI | RANK1_UNSTABLE W–L | UNKNOWN_GATE W–L |
|---|---|---|---|---|
| Match total | 0–0 | n/a | 9–3 | 6–6 |
| Handicap / spread | 0–0 | n/a | 4–1 | 11–10 |
| Team total | 0–0 | n/a | 2–0 | 5–3 |
| Period total (first half) | 0–0 | n/a | 1–0 | 9–5 |
| Winner / double chance | 0–0 | n/a | 0–0 | 5–2 |
| Corners | 0–0 | n/a | 0–0 | 4–1 |
| Player prop | 0–0 | n/a | 0–0 | 0–1 |

## Rank-1 failure classes (counted cohort)

| Class | Count |
|---|---:|

RANK1_UNSTABLE cohort: `OVERCONFIDENT_PROBABILITY` × 4 (P-560, P-564, P-571, P-576), each with its eight-part deep retrospection.
UNKNOWN_GATE cohort (28 Rank-1 losses, primary class mapped to SELECTION_RULES §8): `FIRST_HALF_GOAL_OVERSELECTION` 5, `RUNLINE_CUSHION_CEILING` 4, `RANK_BY_Q_NOT_P` 3, `SHARED_DRIVER_TOP_TWO` 3, `BASKETBALL_TOTAL_WITHOUT_PACE_MODEL` 2, `TENNIS_IID_UNDERDISPERSION` 2, and one each of `SMALL_SAMPLE_STRENGTH_OVERREACH`, `HANDICAP_TAIL_OVERREACH`, `PHASE_INCOHERENCE`, `CORNER_ROW_WITHOUT_PROVIDER_OR_NB_MODEL`, `OVERCONFIDENT_PROBABILITY`, `WEAK_SLATE_FORCED_RANK`, `QUALITATIVE_RANKS_WITHOUT_DISTRIBUTION`, `REGIME_IGNORED`, `UNFITTED_ANALYST_ADJUSTMENT` (per-ID list in the retrospective's COHORT_TABLES §7).

## Evidence grades (all forecast cards)

A 196, B 135, C 33, E 2, OP 16, X 7; A/B share 85.1% (target 95%). By cohort: RANK1_UNSTABLE 80 rows, A 32, B 28, C 20; UNKNOWN_GATE 309 rows, A 164, B 107, C 13, E 2, OP 16, X 7 (the 2026-10-09 report's 313 rows and A 168 also include the four shadow rows of the no-forecast intake P-532).
Sensitivity (UNKNOWN_GATE cohort): excluding the seven live top-two rows settled on C or E, counted 74/127 = 58.3% (95% CI 49.6–66.5%).
Sensitivity (RANK1_UNSTABLE cohort): excluding the five cards settled only on evidence C (P-560, P-564, P-566, P-572, P-573), counted 26/30 = 86.7% (95% CI 70.3–94.7%).

## Calibration (RANK1_UNSTABLE cohort, frozen p_card against outcome)

80 graded rows (ranks 1–4, no PUSH or VOID): mean stated p 84.2%, win rate 81.2%, Brier 0.148 against climatology 0.152 (Brier skill +0.03). Ranks 1–2 only (40 rows): mean stated p 87.0%, win rate 85.0%, Brier 0.131 against climatology 0.128 (Brier skill −0.03). Rank 1 only (20 rows): mean stated p 88.7%, win rate 80.0%, 16 wins against 17.75 expected (z −1.24), Brier 0.169 against climatology 0.160 (Brier skill −0.06). Rank 2 only: mean stated 85.3%, win rate 90.0%, Brier 0.094 against 0.090.

| Stated p bin | n | Mean stated p | Win rate | 95% CI |
|---|---:|---:|---:|---|
| 50–59% | 1 | 57.9% | 100.0% | 20.7–100.0% |
| 60–69% | 3 | 64.4% | 66.7% | 20.8–93.9% |
| 70–79% | 10 | 75.0% | 50.0% | 23.7–76.3% |
| 80–90% | 66 | 86.9% | 86.4% | 76.1–92.7% |

Descriptive only (one cohort, 20 events, dependent rows). Each bin's mean stated p sits inside its win-rate interval; the 70–79% bin under-performs and is the one to watch. The historical cards have no usable frozen p_card/outcome pairs; their calibration is UNKNOWN. q scores are never substituted for probabilities.

## Legacy literal history (diagnostic only)

522 cards; literal logged_result W/L only; mixed grading eras.

| Rank | W–L | Rate | 95% CI |
|---|---|---:|---|
| 1 | 304–185 | 62.2% | 57.8–66.4% |
| 2 | 251–207 | 54.8% | 50.2–59.3% |
| 3 | 246–207 | 54.3% | 49.7–58.8% |
| 4 | 245–202 | 54.8% | 50.2–59.4% |

Learning diagnostics, not certified prospective skill. Complementary rows are dependent, not independent trials.
