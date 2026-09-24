# Implementation ledger — 17 September 2026

**Status: the record of what the [model review](MODEL_REVIEW_2026-09-17.md) actually changed, and what it deliberately did not.**

This document was referenced by `METHOD.md`, `README.md`, `PREDICTION_LOG_COMBINED.md`, `PREDICTION_LOG_COMBINED_3.md`, `PREDICTION_LOG_COMBINED_4.md` and `audit_2026-09-17_implementation/SCORE_AND_SETTLEMENT_CORRECTIONS.md`, but **was never created** — six dangling links, and the one failing assertion in the implementation validation. It is reconstructed here from the surviving artefacts, which are complete: the [review](MODEL_REVIEW_2026-09-17.md) and its [evidence](audit_2026-09-17_models/REVIEW_EVIDENCE.md), the [pre-edit baseline](audit_2026-09-17_implementation/BASELINE.md), the [corrections record](audit_2026-09-17_implementation/SCORE_AND_SETTLEMENT_CORRECTIONS.md), the [validation script](audit_2026-09-17_implementation/VALIDATION.md) and the untouched [`before/` snapshot](audit_2026-09-17_implementation/before). Nothing here is inferred beyond those sources.

**Scope limit, stated once.** This was a Markdown and reference-mathematics implementation. No sporting result was re-verified, no model was fitted, no dataset was built, no forecast, rank, probability or canonical ID was altered, and no performance claim was created. All logs remain `LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE`.

---

## 1. What changed, against the review's own priority table

| Priority | Change | Where it landed | Verified by |
|---|---|---|---|
| **1 — correctness** | One operational scoring definition covering binary, push and action-conditional outputs; conflicting normalised-edge wording removed | `SCORING_AND_VALIDATION.md` (new, `SCV-2026.09.17-v1`), `METHOD.md` §5, `MODEL_IMPLEMENTATION_RECIPES.md` (new) | 66 executable checks |
| **1 — correctness** | **Universal MLB −1.5 ceiling withdrawn**; **12% push ceiling withdrawn**; **tie-on-line extras identity corrected**; league frequencies retained as contextual priors only | `RULES_GENERAL.md` §16.13(e), `RULES_BASEBALL.md`, `BASE_RATES_REGISTER.md`, `CONTROLS.md` | doc inspection + `before/` diff |
| **1 — label integrity** | `P-255-C05` and `P-256-C05` reclassified **`UNRESOLVED_PERIOD`**; handles `TMP-AUDIT-20260912-03`/`-04` reopened; documentary queue restored to **5**, primary queue unchanged at **23** | `RULES_GENERAL.md`, Part 4 Appendix A, `GAME_LOG_STATUS_CURRENT.md` | `SCORE_AND_SETTLEMENT_CORRECTIONS.md` |
| **2 — measurement** | **P-344 aggregation error corrected** (four cells mean **0.283425**, not the printed 0.3334). Full cumulative series rebuilt from rows | Parts 3/4, `README.md` | row-receipt re-sum |
| **2 — validation** | `C-OU-GEOMETRY` reclassified: **zero verified prospective cards**. `P-425`/`P-426`/`P-427`/`P-429` predate the 16 Sep manifest; import date is not issue date | `LEARNING_REGISTER.md`, `CONTROLS.md`, Part 4 | timestamp joins |
| **2 — operational clarity** | Repeating overlays consolidated into the **six-field compact forecast object**; overlapping-window trend test demoted to descriptive; uncertainty expressed through a declared model | `METHOD.md` §4, `RULES_GENERAL.md` §16.14, all ten sport files | `'a trend exists only when L5' not in text` across `RULES_*.md` |
| **3 — model scope** | MLB A0/A1 pilot prioritised; advanced candidates dormant; **tennis and rugby-union scopes registered** (`TEN-A0`, `TEN-A1`, `RU-A0`, `RU-A1`); **M0/M1 marked RETIRED** | `NUMERICAL_PROGRAM.md`, `NUMERICAL_MODEL_REGISTER.md`, `NUMERICAL_TRAINING_SPEC.md` | register assertions |
| **3 — dependencies** | **`H0_DATASET_CARD.md` restored** to the repository root after being found missing while repeatedly referenced | root | existence assertion |

### The corrected cumulative series

From `SCORE_AND_SETTLEMENT_CORRECTIONS.md`, recomputed from canonical rows rather than carried forward:

| Through | Rows | Mean legacy Brier |
|---|---:|---:|
| P-333–P-344 | 39 | 0.2601307692 |
| P-344 | 72 | 0.2408763889 |
| P-371 | 177 | 0.2423966102 |
| P-423 | 373 | 0.2341018767 |
| P-437 | 425 | 0.2286134118 |
| **P-451** | **477** (273 W / 204 L) | **0.2265475891** |
| `PRIMARY_SCORED` | 136 rows / 33 cards (71 W / 65 L) | 0.246825 |

These are cumulative-by-ID reconstructions from the current record, **not** claims about what was settled at each historical snapshot date. Legacy binary scores retain their original conditioning defect and are labelled `LEGACY_MIXED_DIAGNOSTIC`.

## 2. What was deliberately not done

- No sporting final was re-fetched; canonical outcomes were checked against local records only.
- No model was fitted, no calibrator trained, no dataset built, no untouched TEST opened.
- No issued probability, rank, contract or canonical ID was altered. Corrections are appended and dated.
- No historical card was re-ranked or re-settled on the withdrawn ceilings — withdrawal removes a forward constraint, it does not retroactively change a past card.
- The ~86 `LEARNING_REGISTER.md` rows predating `L-095`'s control taxonomy were not retro-tagged (carried forward from the 2026-09-06 deferral; **resolved 2026-09-19** — see the [next ledger](AUDIT_IMPLEMENTATION_2026-09-19.md)).

## 3. Validation

`audit_2026-09-17_implementation/VALIDATION.md` carries a standard-library Python block that extracts the reference algorithms from `MODEL_IMPLEMENTATION_RECIPES.md`, checks them against analytical and synthetic cases, re-sums the saved row receipts, verifies canonical probability tuples and unchanged historical files, and checks that newly introduced local links resolve. It writes `audit_2026-09-17_implementation/RESULTS.md`.

**On 2026-09-19 that script was re-run and reported 66 passes and one failure — the missing document this file now supplies.** With this file present the link assertion resolves. Two provenance notes belonging to that re-run are recorded in the [2026-09-19 ledger](AUDIT_IMPLEMENTATION_2026-09-19.md) §3 rather than here, because they concern the later revision.

## 4. Known limits of this reconstruction

This ledger was written on **2026-09-19**, two days after the work it describes, from the surviving artefacts listed at the top. Where those artefacts are specific, this document is specific and quotes them. It does **not** attempt to reconstruct any figure, hash or decision that the artefacts do not contain — in particular the original `CR-2026.09.17-1` control-manifest hash value, which is discussed in the [2026-09-19 ledger](AUDIT_IMPLEMENTATION_2026-09-19.md) §3.
