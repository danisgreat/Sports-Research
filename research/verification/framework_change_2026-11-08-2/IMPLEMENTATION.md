# Framework change 2026-11-08-2 — enforced integrity (v24.5 / CR-2026.11.08-R2)

**Owner instruction, 8 November 2026:** "implement these recommendations thoroughly where possible". This refers to a review of v24.4 (`33d92422d`). Its priority: the code must enforce the rules, and the forecast → settlement → evaluation cycle must be completed.

**Class.** INTEGRITY + PROCEDURE + STATISTICAL:
- four regime rows are re-statused;
- the forecast-path code changed, so the releases must be re-frozen.

No issued card, grade, ID or settled record is changed. Versions: method **MDS-2026.11.08-v24.5**, control **CR-2026.11.08-R2**, prompts **P-2026.11.08-v24.3**.

**Standard of completion.** Each repair is proven by a test that now rejects the invalid record. The review reproduced each failure in isolation; the tests are the same kind of reproduction, run against the code.

## 1. Bind every forecast to the exact event, contract and probability (BIND-v1)

| Gap found by the review | Repair | Test |
|---|---|---|
| A reused reference froze the old event and line | `pregame.bind_reference`: the frozen bundle must verify, and its request must match the native ID, competition, teams and scheduled start; every LINES row must match a frozen contract by label, family, side and line; a dropped contract is refused | `test_pregame.py::test_a_reused_reference_must_be_for_the_same_event_and_contracts` |
| A probability printed elsewhere in the card was accepted | `pregame.bind_card`: each `card_p` must equal the `final_p` on the same label's PICKS_V2 row, with the same family, side and line | `test_card_probability_must_be_attached_to_the_same_contract` |
| Comparator p of 9, 1.2 and −2; invalid dates; an invalid side | The linter bounds `reference_p`, `baseline_p` and `model_p` to [0, 1]. Times must be ISO 8601 with an offset. Side vocabularies are checked per family | `test_picks_ledger.py::test_comparators_and_sides_are_bounded`, `test_dates_and_timing_follow_the_evidence` |
| A post-start issue was labelled PREGAME and was ledgered | Lint refuses PREGAME when `issued_at` ≥ start, a reference frozen after issue, and malformed `issue_evidence`. `ledger.derive_timing` records PREGAME only with a matching pregame receipt or a pre-start commit holding the exact card; otherwise TIMING_UNVERIFIED, keeping the claim in `timing_claimed` | `test_a_late_card_labelled_pregame_is_refused_and_a_receipt_verifies_timing` |

## 2. Point-in-time admission (PIT-v2)

- **Publication order.** `_check_source` now requires publication ≤ known_at ≤ retrieval. A result claimed known before it was published is quarantined (`KNOWN_BEFORE_PUBLICATION`) and never appears in an earlier historical view.
- **Correction chronology.** A statistic correction must be known after the revision it replaces (`CORRECTION_CHRONOLOGY`). Result corrections already required this.
- **Development study.** The loss scale is computed in each window from admissible history only (`context_study.loss_scale`). A test changes the last game's result and proves that every earlier Hedge prediction and weight is bit-identical. The same test fails on the old global scale (checked by temporarily restoring it).
- **Live data.** No publication-order violation was found in the live observation table (the review's own check); these are admission repairs, not evidence that past data used them.

Tests: `test_integrity_r2.py` (publication and correction) and `test_context_study.py::test_changing_a_future_result_cannot_change_an_earlier_prediction`.

## 3. One effective-settlement view (SETTLE-VIEW-v1)

`ml/evaluation/effective_settlement.py` reads every original inventory (`mini_import_*/EFFECTIVE_SETTLEMENT_ROWS.csv`, unchanged) and every revision file (`settlement_import_*/SETTLEMENT_REVISIONS.csv`). A revision applies only when its parent is the key's current effective revision. The following are refused:
- a revision for an unknown key;
- a mismatched local key;
- a repeated revision id;
- a broken or branching chain;
- an unknown grade;
- a missing source document.

`card_history` consumes the view and refuses to run when a revision matches no row. The 7 November revisions are now structured rows:
- P-604 corners: Over WIN, Under LOSS (revision-3);
- P-606: revision-2;
- P-616: revision-2 (BK-OT-1);
- P-620: revision-2 (evidence E → B).

A fresh history rebuild shows them; 102 effective rows, 0 UNRESOLVED. Command: `python -m ml settlement-view --out DIR`.

## 4. Evaluation and promotion

- **Promotion (PROMO-v2).** PROMOTION_ELIGIBLE needs a mean paired Brier improvement of at least the declared `delta`, no longer `delta / 2`. A 0.0064 gain under a 0.01 rule no longer passes.
- **Log loss.** Prospective scoring uses `ml.core.metrics` (one implementation, no hidden floor). A wrong literal 0 or 1 is an infinite loss and is reported, not clipped or dropped.
- **Ledger strata (SCORING §12).** Every score row names its stratum: timing, fast or full card, supplied or derived line, and reference executed or baseline only. Nothing pools strata, and λ is estimated within each stratum.

Tests: `test_learning_governance.py::test_promotion_needs_the_full_declared_improvement`, `test_a_wrong_literal_zero_has_infinite_log_loss`, `test_picks_ledger.py::test_score_never_pools_timing_card_or_line_strata`.

## 5. Executable release gates (GATE-v2)

**Gate changes:**
- G4 counts only observations of the effective revision, and counts lineage by registrable domain: `www.espn.com` and `site.api.espn.com` are one lineage. It also requires distinct captures.
- G5 requires both regulation scores.
- Every gate run writes a versioned receipt bound to a SHA-256 of the store snapshot (`research/release_gates/`).

**Release command.** `python -m ml cycle release` now requires `--gate-receipt`. It refuses a failed, wrong-scope, old-version or stale (store changed) receipt, and writes the binding beside the release (`<release>.GATE.csv`).

**Older releases.** Releases made before GATE-v2 are reported as `CARRIED_FORWARD_BEFORE_GATE_V2`, judged by the rules of their own time.

Tests: `test_releasegate.py` (5 new).

**Consequence (stated plainly).** These integrity repairs change files in the cycle's code closure:
- `cycle.py`
- `evaluation/prospective.py`
- `releasegate.py`
- `research_ingest.py`

The framework never restamps a release, so every current release is stale for the new code. The gate was run on the live store on 2026-11-08:

| Competition | Gate | Outcome |
|---|---|---|
| NBA | PASSED (3,693 finals, 3 seasons, every G check) | **NBA-CYCLE-2** frozen with a gate binding (challenger lane; the NBA reference is TB-2-MD and is unaffected) |
| NHL | FAILED G4: 1 final (the 2026-27 P-607 event) has one lineage | NHL-CYCLE-4 stays listed, STALE_FOR_CURRENT_CODE. The NHL reference stage records `NOT_RUN_STALE_RELEASE` until a second lineage for that final is ingested and NHL-CYCLE-5 is frozen through the gate |
| MLB | FAILED G1: 374 finals in one season | MLB-CYCLE-4 stays listed, STALE_FOR_CURRENT_CODE. MLB history must be ingested before March 2027 (two lineages per final) |

Every release had 0 prospective events, so no prospective evidence is lost.

## 6. Regime evidence (REGIME-v3)

`ml/studies/regime_eval.py` adds the chronological test: each season is fitted on earlier seasons only. The earlier leave-one-season-out test is kept and labelled exploratory. The review's NRL figure is reproduced exactly: Brier −0.00193 (−0.00491, +0.00193).

**New rows** (EFFECT_TABLES is append-only; the R1 rows are retired in `SUPERSEDED.csv`, which the ledger enforces):

| Row | Entry | Basis |
|---|---|---|
| `E-NBA-PLAYOFF-TOTAL-R2` | FULL, CONFIRMED | Chronological, 5 of 5 later seasons better |
| `E-MLB-POSTSEASON-TOTAL-R2` | HALF | Confirmed only on the proxy, not on MLB-CYCLE-4 |
| `E-NRL-EARLY-TOTAL-R2` | HALF | Chronological intervals cross zero |
| `E-AFL-FINALS-TOTAL-R2` | HALF | Not confirmed |

Each regime adjustment is now tested prospectively through its frozen counterfactual (section 7).

## 7. Structured adjustments (LEDGER-v2)

A card whose final p differs from its reference must carry an `ADJUSTMENTS_V1` block. `ledger add` checks each row:
- the effect row exists, is not superseded and is not `MEASURED_NULL`;
- the entry and size are right for its status;
- the source is a URL or a capture;
- published ≤ retrieved ≤ issued;
- the overlap check is filled in;
- the frozen counterfactual names real rows, with p in [0, 1].

`ledger add` then appends the rows to the hash-chained, immutable `research/adjustment_ledger/ADJUSTMENTS.csv`, keyed by card and effect-row version. `ledger score` writes `EFFECT_SCORES.csv` (final against counterfactual, per effect version and stratum) apart from the aggregate. The empty ledger's header was migrated to the LEDGER-v2 schema; it held no rows.

## 8. Operational backlog — measured, not yet cleared

The generated state block (`python -m ml state`; section 9) lists the backlog from the records:
- 6 open cards in the active mini;
- 2 frozen NBA league-day events without settlement;
- 0 ledger rows;
- 8 team-statistic and 0 player-availability rows in the store.

Clearing it is a prompt-3 settlement and prompt-4 import, each with source research and DEEPLOSS-v1 reviews. It is the next operational task, and nothing in this change pretends it is done. Recommended order:
1. Settle the six cards and the two league-day events.
2. Run one narrow prospective lane: NBA, TB-2-MD reference, card adjustments through ADJUSTMENTS_V1, frozen before the start and settled within a day.
3. Capture time-stamped availability at every freeze.

## 9. Generated current state (STATE-v1)

`python -m ml state --write` generates the CURRENT_STATE block from the records:
- the highest canonical ID from the import mappings;
- the active mini and its footer's next key;
- the store view and counts;
- open cards and league-day events;
- ledger and adjustment rows;
- the shadow ledger;
- the effective settlements;
- the release gate bindings.

`test_integrity_r2.py::test_the_committed_state_block_is_what_the_records_generate` fails when the committed block is stale. The stale hand values the review found (store view 7 instead of 12; next key G0002 instead of G0006) are replaced by pointers to the block.

## 10. Consistency, concurrency and cleanup

**Wording and precedence:**
- All eleven sport prompts: "Model output … never read" is now "Model output is read only through the reference stage and the card freeze".
- "No code" and Drive wording is removed from live pages.
- Precedence is defined once (PREC-v1, RULES_REFERENCE Part A §0).
- Every promoted lesson carries `applies: PRE_V24 | V24 | CHECKLIST`.

**Store lock (STORE-LOCK-v1).** Ingest takes an exclusive lock file. It then rechecks the store sequence before writing, so two writers can no longer both succeed with one sequence. Tests: `test_a_second_writer_is_refused_while_the_store_is_locked`, `test_a_writer_that_appended_meanwhile_stops_the_second_commit`.

**File treatment, following the review's table** (moves are recorded in HISTORICAL_LINK_INDEX):
- Release history from CURRENT_STATE, PROMPTS.md and the prompt README, and SOURCES Part D, moved verbatim to `research/history/`.
- PROMPTS.md is a compatibility pointer to the single operator index (`research/prompts/README.md`).
- GAME_LOG_STATUS_CURRENT points to the generated queue.
- The old engine and shadow sections of ten sport rules files are in `archive/historical_engine_sections_2026-11-08/`, with their headings kept so links resolve.
- The regime study code moved to `ml/studies/`.
- Large verified-history files are unchanged (the review says to move them only after restoration and every consumer are tested).

## 11. Verification

The full test suite and the link check run before the commit; results are in the commit message.
