# Cohort retrospective — 21 October 2026, P-601 to P-622

Prompt 6 (`P-2026.10.17-v22.2 · COHORT_RETROSPECTIVE · LOCAL_WORKING_TREE`), ML/RL review under MLSCOPE-v1 and LEARN-v1 §§6–8. **User-requested, outcome-exposed**, below every review threshold. Scope, receipts and the per-ID inventory are in [DATA_INVENTORY.md](DATA_INVENTORY.md). Tables are in [COHORT_TABLES.md](COHORT_TABLES.md) and [COHORT_ROWS.csv](COHORT_ROWS.csv), with full-history context in [HISTORY/](HISTORY/CARD_HISTORY.md).

No original log, grade, forecast, ID, active rule, prompt, model, registry entry or previous report was changed. The decision lab was not read.

## Summary

- **22 cards, 2 ISO weeks.** 11 research-only events (no primary probability) and 11 ANALYST_PRIMARY_V1 cards. Primary Rank 1 went 6W/5L and Rank 2 5W/5L/1P; Hit@2 was 8/11. Brier on 21 decisive primary rows was 0.2041, with 11 wins against 12.86 expected. With fewer than eight weeks this is **INSUFFICIENT_EVIDENCE** for any skill or calibration claim.
- **Rank 1 split cleanly on stated p.** At p ≥ 0.60 it went 5W/0L. Below 0.60 it went 1W/5L, and all five losses were below the 0.62 gate, so they were issued as unqualified near-coin-flips. This is consistent with the full-history band table (Rank 1 realised 54–56% in the 0.55–0.65 bands), but n = 11.
- **Same-row baseline coverage is 8 of 50 primary-cohort rows** (2 events): card − baseline Brier +0.0244. The P-612 card lost to a stale league baseline by +0.06.
- **Learning store.** It now holds these settlement outcomes: 21 events with reviewed captures, 4 corroborating second sources, 8 corner statistics and 0 quarantined. There are 22 research-only label candidates (136 labels). The cards' own prior-game tables were **not** ingested, because they have no captures or known-at times (F-10).
- **Data defects found by recapture.** P-606's settlement score is wrong (117–98 recorded, 116–98 actual; no grade changes) (F-01). The unresolved P-604 corners now have a candidate single source, 8–5 = 13, which would grade Over 10.5 a WIN; the grade is unchanged here (F-02).
- **One frozen model shadow** exists near this cohort, a HEDGE_MIX_V3 bundle for an A-League match that has no card. It was settled descriptively and is not paired with any card (§3).

## 1. Scope and coverage

See DATA_INVENTORY. Cohorts are kept separate throughout:
- RESEARCH_ONLY_NO_MODEL P-601–P-611: 52 rows, 25W/25L/2U, analyst values NOT_PRIMARY.
- ANALYST_PRIMARY_V1 P-612–P-622: 50 rows, 25W/23L/2P. P-612–P-618 are owner-saved NOT_ISSUED drafts and are reported in their own stratum.

Issue and timing:
- No card has a verified pre-start issue.
- Five cards are verified POST_START from owner feed clocks: P-610, P-613, P-615, P-618, P-622.
- There is no CLEAN_PRE_START_INPUTS cohort.

No research early exits occurred. Every card completed hand research and stated probabilities (P-601's analyst values are NOT_ESTIMATED by design). No card used a model, runtime or manifest (MLSCOPE-v1).

Open queues carried from the import (unchanged; U-numbers refer to [UNRESOLVED_POST_IMPORT.md](../mini_import_P-601_P-622_2026-10-21-1/UNRESOLVED_POST_IMPORT.md)):
- U-601 operator terms for all events.
- U-602 P-604 corners (see F-02).
- U-603 P-616 overtime definition (grade-changing).
- U-604 P-620 Test result, due 23 Oct.
- U-605/U-607 corroboration.
- U-606 Machida corner conflict.
- U-608 held MELILL01-G0004.
- U-609 draft custody.
- U-610 unimported package.
- U-611 final wall-clock times.

## 2. Prediction assessment

Main results are in COHORT_TABLES §§2–7. Interpretation, given dependence, multiplicity and small n:

- **Ranks.** Rank 1 54.5% (Wilson 28–79%) and Rank 2 50.0% (24–76%) cannot be told apart from each other or from the full-history 63.0% / 57.2%. Every competition stratum has a single card.
- **Proper score.** 0.2041 on 21 rows from 11 events in 2 weeks. Rows within a card are dependent, so the effective n is closer to 11. No bootstrap is reported.
- **Reliability.** The [0.50, 0.60) band realised 3/12 against a mean p of 0.54. The [0.60, 1.0] band realised 8/9 against 0.68. Both cells have wide intervals. This is direction-consistent with the full-history finding that skill shows only at higher stated p (calibration slope 0.79 in [HISTORY](HISTORY/CARD_HISTORY.md)), but it is not evidence on its own.
- **Width.** The cards' own σ looks too wide for totals and too narrow for margins:

  | Target | n | z RMS | Beyond ±1 | Beyond ±2 |
  |---|---:|---:|---:|---:|
  | Totals / innings | 10 | 0.48 | 0 | 0 |
  | Margins | 6 | 1.46 | 3 | 2 (P-614 −2.31, P-618 +2.42) |

  The margin result repeats RET-12's 2026-10-16 observation (mean |z| 1.05).
- **Gate and selection.** All five Rank-1 losses had p between 0.524 and 0.568. In each case the card had already flagged the pick as below its 0.62 gate. Hit@2 was 8/11 with 0 mechanically protected pairs, so this Hit@2 is not inflated by covering pairs. No RET03/RET04/XCARD6/RANK_DELTA/BASE_ONLY frozen comparisons exist for this cohort: no shadows were frozen beside these cards.
- **Joint losses.** Two of 11 cards lost both primary slots (P-615, P-621). This review did not re-derive the cards' stated joint-loss values, so there is no comparison of joint-loss frequency against stated probabilities.
- **Rank-1 loss reviews (5/5 present in the settlement records).**
  - P-615: variance, plus a Sunday starting five that was not knowable at issue.
  - P-616: the loss came entirely through the overtime branch. OT occurrence was not knowable; the endpoint convention was declared.
  - P-618: variance, a +0.9σ total.
  - P-620: LOWER-ORDER RECOVERY (97/5 → ≥ 324/7), a tail the scenario mixture under-weighted.
  - P-621: Milano's active five was unknown at issue.

  In every case the mechanism is post-event explanation, not a fact known at issue that was missed. None of these losses is calibration proof.
- **Research-only diagnostics.** MSE 0.2429 on 44 rows. Analyst A1 went 6W/4L. Not primary.

## 3. Sporting shadows (audited separately)

**This cohort.** No frozen model shadow, cycle bundle or prospective-ledger row exists for any of the 22 events.
- P-601–P-611's R1 package records that all 11 execution paths are empty (NOT_APPLICABLE_NO_MODEL).
- P-612–P-622 are no-code ANALYST_PRIMARY_V1 cards.
- The 29 `research/model_shadow/*-r1` folders are HISTORICAL_DEVELOPMENT predictions whose latest dates are 2022-09 to 2026-09-27. None covers 16–20 Oct 2026.
- `research/prospective/` has no SHADOW_LEDGER.csv.
- Consequences: `cycle settle` and `cycle evaluate` are **NOT_APPLICABLE** (only MLB/NHL cycle releases exist, and no bundle exists for P-607). `prospective evaluate` is **NOT_APPLICABLE** (no ledger, no preregistered delta). No paired card–model comparison is possible.

**Nearby frozen shadow (unpaired).** The owner's working folder `Downloads/SPORTS_MINI_2026101710538263F6ED_G0001_2026-10-17/` (empty mini 10538, 0 cards) holds a real frozen bundle for **ESPN 401892159, A-League Men, Central Coast Mariners v Newcastle Jets, 17 Oct**.

| Item | Value |
|---|---|
| Issue / scheduled start | issued 08:22:33Z (EXECUTION EXECUTED 08:23:16Z), scheduled start 08:40Z |
| Timing and qualification labels | `TIMING_UNVERIFIED`, `EXPERIMENTAL_PRIMARY_NOT_CERTIFIED` |
| Bundle SHA-256 | `7b0d3807…5a85b` |
| Ledger | `mini_shadow_ledger.csv` (SHA-256 `6604c7d9…1753`), 54 rows: PRIMARY_HEDGE_MIX_V3 CANDIDATE + BASELINE_LEAGUE_V1 CHAMPION; `prospective verify` reports chain intact |
| Final | 2–2 (ESPN summary capture `0ad9e136…890a`) |
| `primary settle` result | [SHADOW_SETTLEMENT/ESPN_401892159_PRIMARY_SETTLE.csv](SHADOW_SETTLEMENT/ESPN_401892159_PRIMARY_SETTLE.csv): expert losses RATINGS_FAST 0.2392, RATINGS_SLOW 0.1861, LEAGUE_BASELINE 0.3166; model top-two Brier 0.0190 (Under 5.5 and Away +1.5 both won) |
| Same rows v frozen baseline | 27 dependent decisive contracts: model Brier 0.1064 v baseline 0.1136 (d −0.0071), graded with the repository's `price` function |

Classification: **UNVERIFIED_LOCAL_SHADOW**.
- The ledger rows self-label PRE_START_VERIFIED, but the ledger was never committed before the start, sits outside the repository and has unverified issue timing.
- It is not a PROSPECTIVE_SHADOW and does not count toward any shadow n.
- No card exists on the event, so it offsets nothing.
- One event with dependent rows is **INSUFFICIENT_EVIDENCE**.

`python -m ml primary verify-execution` on this attempt fails with `KeyError: 'baseline_dependency'`. The bundle predates a schema change, so the current verifier cannot check older attempts (F-04). `primary settle` itself verified the bundle receipt.

## 4. ML/RL review

**Step 1 — ingest.**
- Settlement outcomes were transcribed to the §2 export columns: [LEARN_EXPORT/EXPORT/](LEARN_EXPORT/EXPORT/) GAME_OBSERVATIONS (25 rows) and TEAM_GAME_STATS (8 corner rows).
- Capture provenance: 24 captures, retrieved 2026-10-20 13:24–14:25Z, stored outside the repository, hashes in [CAPTURE_INVENTORY.csv](LEARN_EXPORT/CAPTURE_INVENTORY.csv).
- Timestamps:
  - known_at = retrieval time (earliest demonstrated public time).
  - final_at = captured end time where one exists (Liiga, KBO, B.League last PBP), otherwise the retrieval time as an upper bound.
- Exclusions:
  - P-620 is not final.
  - P-619 corners are excluded because providers disagree.
  - The P-606 score uses the captures (116), not the settlement (117).
- Dry run on a store copy, then `python -m ml ingest add`: **ingest_seq 7**, export `af6e90e3…f358`, code `0fa412d3…0a49`, observations 33, new events 21, new results 21, corroborating 4, corrections 0, **quarantined 0**, duplicates 0.
- An exact re-ingest on a copy adds nothing (33 exact duplicates).
- As-of check: NHL primary HISTORY as of 2026-10-16T23:00Z is byte-identical before and after the ingest (`d4ccce64…`, 1,312 rows). It gains P-607 only once the horizon passes its final.
- Not transcribed: the cards' Markdown prior-game and availability tables (LEARN-v2). Every card marks them QUARANTINED or LEARN_RECORD_INCOMPLETE with no capture hash or known-at. External chats cannot hash (ENV-v1), so every row would quarantine. Status: `LEARN_EXPORT_NOT_WRITTEN (history rows)` (F-10).

**Step 2 — labels, settlement, review log.**
- `ml.research_learning retain`: 22 candidates under `research/training_candidates/P-6NN/<revision>`, all `LABELS_RETAINED_NOT_MODEL_FEEDBACK`, all pass `verify`. Plan and exclusions are in [TRAINING_CANDIDATES.csv](TRAINING_CANDIDATES.csv): P-604 revision-2 (corners UNRESOLVED), P-620 (pending), P-616 contract outcomes (definition unresolved; score labels kept).
- Each candidate is labelled `FROZEN_FRAMEWORK_CONVENTION` / `FEATURES_NOT_VERIFIED`. Expert feedback is NOT_APPLICABLE_NO_MODEL for all 22. No expert loss was manufactured.
- `primary settle` ran on the one frozen bundle (§3). `cycle settle` is not applicable.
- Review rows were appended to REVIEW_LOG (§6).
- [LEARNING_STATUS/](LEARNING_STATUS/LEARNING_STATUS.md) after ingest: store view 7; 21 settled since the last review; INTERIM 21/100, COMPREHENSIVE 21/300, sport and competition clocks all NOT_DUE.

**Step 3 — comparisons.** `card-history` ran on the committed rank log (§5). `cycle evaluate` and `prospective evaluate` are not applicable (§3). Paired card v BASELINE_P is in COHORT_TABLES §6.

**Step 4.** No model finding edits an issued card. The proposals below go to prompt 8.

**Level and dispositions.**

| Scope | Disposition | Evidence |
|---|---|---|
| ALL (this review) | **DATA_REPAIR_REQUIRED** | F-01 P-606 score; F-02 P-604 corners; F-03 card-history coverage; F-04 verifier schema drift; F-10 history rows not ingestible |
| Basketball | INSUFFICIENT_EVIDENCE | 5 primary cards, 2 baseline-paired events; r1 development models remain DATA_HOLD; no frozen shadow |
| Soccer | INSUFFICIENT_EVIDENCE | 2 primary + 4 research-only events; no frozen shadow on any carded event |
| Soccer/A-League Men | INSUFFICIENT_EVIDENCE | 1 unverified local HEDGE_MIX_V3 shadow, settled, unpaired |
| Ice Hockey | INSUFFICIENT_EVIDENCE | 2 research-only events; the NHL-CYCLE-3 release had no bundle for P-607 |
| Baseball | INSUFFICIENT_EVIDENCE | 1 primary card (KBO); KBO r1 development model only |

Rugby union and the cricket formats have no model, so no model disposition applies. Cricket T20 has an IPL development model, but no women's T20I scope.

## 5. Full-history context (card-history)

`python -m ml card-history --rank-log GAME_PREDICTION_RANK_LOG.csv --out HISTORY` ran on the committed rank log:
- Working-copy SHA-256 `cb2820f0…4f76` (CRLF); committed blob SHA-256 `49e3fd8d…b981199`; last changed in `d066b489`.
- Code `0fa412d3…0a49`.
- Output: 2,322 rows, 599 cards (through P-600).

Full history: Rank 1 342–201 (63.0%, 58.8–66.9), Rank 2 293–219 (57.2%), Ranks 3–4 557–442 (55.8%); 862 stated-p rows, Brier 0.2269 v climatology 0.2414, slope 0.79 (SE 0.11).

These differ from the 2026-10-16 full-history report (352–207, 2,311 rows) for two reasons, and no grade changed:
- That run used an external pre-refresh rank-log head.
- The card-history code since `ca03fdf8` grades the 21 colliding aliases UNRESOLVED in the main table, so the "excluding collisions" sensitivity now equals the headline.

The tool does not read the P-601–P-622 inventory (F-03).

## 6. Findings and proposals

| ID | Finding (evidence) | Mechanism | Proposed change / files | Owner / prompt | Status | Acceptance / rollback |
|---|---|---|---|---|---|---|
| F-01 | P-606 settlement records **117–98** (total 215, residual −7.50). ESPN scoreboard and summary, the NBA.com game page final and the ESPN box (37 FG, 14 3PT, 28 FT = 116) give **116–98**. Grades unchanged (Under 229.5 W, MEM −2.5 W). | Score read from a recap-video title; NBA.com's linescore shows Q3 30 (sums to 117) beside its final 116 | Prompt-3 settlement revision-2 for P-606 score fields only, imported by prompt 4 (addendum; never edit the original); the store and labels already use 116. Settlement checklist: final score from a box/linescore with a sum check, never a headline | Owner → prompts 3/4; checklist via prompt 8 (RET-18) | OPEN | Revision imported; next 40 settlements show 0 score mismatches on recapture |
| F-02 | P-604 corners (U-602): Futbol24 match page (via r.jina.ai) shows **Akbou 8 – Ben Aknoun 5 = 13** | New route; single aggregator (would be evidence C) | Seek a second source (LFP sheet, Goaloo); then a prompt-3 revision-3 for the two corner keys (Over 10.5 WIN / Under LOSS if confirmed). Grades stay UNRESOLVED until then | Settlement reviewer → prompts 3/4 | OPEN (candidate evidence) | Two independent sources agree, or remains UNRESOLVED |
| F-03 | `card-history` stops at P-600: the rank log is not refreshed past P-600, and inventories are hard-coded to the 2026-10-13/14/16 imports | Tool and rank-log coverage gap | Read every `mini_import_*/EFFECTIVE_SETTLEMENT_ROWS.csv`; refresh `GAME_PREDICTION_RANK_LOG.csv` through P-622 in a dedicated task | Prompt 8 (code), rank-log refresh task | PROPOSED (RET-17) | card-history reproduces COHORT_ROWS for P-612–P-622 exactly |
| F-04 | `primary verify-execution` raises `KeyError: 'baseline_dependency'` on a 17-Oct attempt | Bundle schema drift without a version gate | Version field or backward-compatible reader; test on the retained attempt | Prompt 8 | PROPOSED (RET-20) | Verifier passes or rejects old attempts with an explicit version error |
| F-05 | Rank 1 at p < 0.60: 1W/5L; at ≥ 0.60: 5W/0L (n = 11) | Near-coin-flip Rank 1s issued below the 0.62 gate | None now. Keep under existing full-history monitoring; no selection change from 11 cards | — | MONITOR | — |
| F-06 | Totals z RMS 0.48 (n = 10); margins RMS 1.46 (n = 6, 2 beyond ±2) | Totals σ too wide, margins too narrow (descriptive) | Extend RET-12 to totals; consider PROBABILITY_TOOLKIT σ constants only after 40 cards per family | Prompt 8 after data | PROPOSED (RET-19) | Coverage of central 50%/80% bands within interval at 40 cards |
| F-07 | BASELINE_P on 8/50 rows (2 events) | Baselines not printed beside most supplied lines | RET-10 unchanged: its acceptance (≥ 80% on 40 cards) is failing on this cohort | Prompt 1 practice | RET-10 FAILING | — |
| F-08 | 0/11 primary cards with verified pre-start issue; 7 NOT_ISSUED drafts | External-chat delivery clocks not captured | None new. Prompt 1 already requires an actual delivery time; drafts stay their own stratum | — | NOTED | — |
| F-09 | One unpaired local HEDGE_MIX_V3 shadow with an intact ledger, outside the repository | Owner working folder | Owner decides whether to bring the ledger into custody (it cannot become PROSPECTIVE_SHADOW retroactively) | Owner / prompt 8 | NOTED | — |
| F-10 | Card prior-game/availability tables not ingestible (no captures/known-at) | ENV-v1 chats cannot hash or save captures | Prompt 7/8 recapture of prior-game rows from keyless field-owner routes for imported events, or a registered "card-table transcription → quarantine" path | Prompt 7 / 8 | PROPOSED (RET-21) | ≥ 80% of the next cohort's history rows admitted, or a documented quarantine reason for each |

Separation of status: no control was implemented here, no experiment was registered or run, and no release occurred. The data repairs (F-01, F-02) require settlement revisions. Power inputs for RET-17–RET-21 are unknown: **BLOCKED_DESIGN / SAMPLE_SIZE_NOT_ESTIMATED**, except where a fixed card count is stated.

**Test priorities:** F-01 revision (cheap, already verified) → F-03 card-history coverage → F-02 second corner source → F-04 verifier → F-10 history recapture design.

## 7. Reconciliation and checks

- **Row totals.** 102 = 52 + 50.
  - Research-only: 25 + 25 + 2 = 52.
  - Primary cohort: 25 + 23 + 2 = 50.
  - Slots: 11 + 10 + 1 = 22 = 2 × 11 cards.
  - Label candidates: 136 labels = 8+8+6+2+6+6+6+6+6+6+6+6+6+6+6+4+8+6+10+6+6.
- **Representative arithmetic, checked by hand.**
  - P-612 Rank 1: (0.709 − 1)² = 0.0847.
  - P-612 baseline: (0.845 − 1)² = 0.0240.
  - P-606: 2×37 + 14 + 28 = 116.
  - Expected primary wins: Σp over the 21 decisive slot rows = 12.86.
- **Store.** The INGEST_RECEIPTS row 7 counts equal the dry run. Quarantine is empty. The `git diff` is append-only (+84 lines).
- **Tests.** `python -m pytest ml/tests -q` result: see [IMPLEMENTATION_CHECKS.md](IMPLEMENTATION_CHECKS.md).
- **Registry.** `python -m ml registry verify`: chain intact (16 entries).
