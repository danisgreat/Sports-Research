# PROMPT 3 — SETTLE THE ACTIVE LOCAL MINI AND WRITE THE RETROSPECTIVES

**Run by:** external chat agent · **GitHub:** read only · **Output:** a local settlement folder · **Mode:** `LOCAL_MINI_SETTLEMENT`

Use only the current `main` branch of `https://github.com/danisgreat/Sports-Research` as authority for method and rules. The active local mini and its working P-IDs hold the forecasts. Never renumber them because GitHub is behind.

This task settles, grades and reviews. It does **not** import, allocate canonical IDs, change methodology, write new predictions or write to GitHub.

---

## 1. Read the authority

Record the `main` HEAD SHA, then read:

1. `METHOD.md` and `CURRENT_RULES.md`: Rules **T2** (only Rank 1 and Rank 2 count as wins), **R1** (a Rank-1 failure needs the eight-part deep retrospection) and the local-mini lifecycle.
2. `SCORING_AND_VALIDATION.md` (SCV-2026.10.09-v4): top-two counting, evidence grades, PUSH/VOID handling.
3. `CARD_AND_LOG_TEMPLATES.md`, section **Local mini format `mini-log-3`** (a `mini-log-2` mini is settled the same way; v3 cards add the fields used in sections 4 and 5 below).
4. `research/prompts/examples/EXAMPLE_SETTLED_MINI.md`: the exact settlement structure to copy.
5. `CURRENT_STATE.md` and `GAME_LOG_STATUS_CURRENT.md`: the repository's `Next canonical ID`, for the report.
6. The `RULES_*.md` file for each sport in the mini (endpoint, OT/extra-time, retirement and abandonment rules).

Then read the **active local mini** in full, including every card, carryover and addendum.

## 2. Freeze the mini before you write anything

1. Save an exact, unedited copy of the active mini as `ORIGINAL_MINI/<original file name>`. Do not reformat, re-save through an editor that changes line endings, or fix typos. These bytes are the forecast custody.
2. Record its byte length and SHA-256. If you cannot compute a hash, write `NOT_COMPUTED`. The local `join` tool or the importer fills in the true value.
3. Record the first and last card IDs, the card count, the carryover count and the addendum count.

The settled mini is the frozen bytes **followed by** the appended settlement section. Never edit, reorder or delete anything above the footer, including the footer itself.

## 3. Inventory and classify every record

For every block in the mini, record the ID, event key, native event ID, sport/league, event, research time, timing state and classification:

| Classification | Meaning | Settled here? |
|---|---|---|
| `LOCAL_UNIMPORTED_EVENT` | A card written in this mini | Yes |
| `ALREADY_CANONICAL_REFERENCE` | A carryover: already canonical, waiting for its event | Yes, if now terminal |
| `DATED_ADDENDUM` | A correction or late news under an existing ID | No; it consumes no ID and is never graded |

Mapping rule: every card keeps its working ID and reads `CANONICAL_MAPPING: PENDING_IMPORT`. Carryovers keep their canonical ID. Do not allocate or change any canonical ID here.

## 4. Research the results

For each event, research the final result from these sources, in order:
1. the official competition or field owner;
2. the official team or participant;
3. an official structured statistics provider;
4. independent high-quality corroboration.

**Settlement SLA.** Settle each card within **72 hours** of its final. Open carryover must stay at or below 5 (`python -B -m research.operations.settlement_sla <mini>.md` reports breaches). A `mini-log-3` card names its exact settlement fields and provider (`Settlement fields`) and a `Capture due` time: capture those pages first, because corners, half-time, period and player pages rot within days. Retain what you capture (`python -B -m research.operations.evidence_snapshot store --kind capture --key P-NNN-<field> --file page.html --url <https url>`), or say in the Basis cell which page decided the row.

Verify the identity and date, the final state, the score, regulation versus OT/ET/extras/shootout, the period/half/set/innings splits, and any statistic a proposition needs. Check retirement, abandonment, rain and DLS where relevant. Do not infer a missing statistic from the final score alone. If you can only bound it, use evidence grade **E** and state your confidence.

## 5. Settle every issued row (settle anyway)

Settle the **literal proposition as issued**, on the card's own endpoint. Each row receives exactly one grade and one evidence code.

**Grades:** `WIN`, `LOSS`, `PUSH` (an exact integer line, or a void-on-tie rule), or `VOID` (no admissible data, abandoned or cancelled with no result, or a market voided by rule).

**Evidence codes:**

| Code | Use when |
|---|---|
| `A` | An official or field-owner terminal record covers the target field |
| `B` | A structured provider or multi-source agreement covers the target field, with an official score |
| `C` | The best available evidence is a single secondary, conflicted or provisional source, adopted as final |
| `E` | The value is estimated from a partial measurement that bounds the target field; state your confidence |
| `OP` | The sporting endpoint is known but the operator rule is not; the card's frozen assumption or the framework default applies |
| `X` | No admissible data exists; the row **must** be `VOID` |

- **Settle anyway.** If details are missing, settle on the best evidence code above. Do not leave a terminal event unsettled.
- **Contract definitions come from the card.** Where the sporting endpoint is known but the contract rule is not (retirement, listed pitcher, abandonment), apply the card's `Retirement rule`, `Listed-pitcher rule` or `Abandonment rule`. `FRAMEWORK_DEFAULT:` and `OPERATOR:` rules are applied as written and graded `OP`; `N/A` means the field cannot arise. Never invent a definition after the result is known, and never settle a row differently to make a pick look better.
- **Only a non-terminal event stays open.** If the event is postponed, suspended or not yet played, write `**Card state:** PENDING_EVENT` and carry it forward. That status is reserved for events that have not finished. It is not for missing statistics.
- Complementary rows (e.g. Over 5.5 and Under 7.5) are dependent outcomes of one event, not independent trials.

**Counting (Rule T2):**
- Only Rank 1 and Rank 2 can count as wins. Ranks 3–4 are graded for calibration only.
- `PUSH` and `VOID` leave the denominator and are never losses.

Card classes:
- `TOP2_ALL_WON`: every live top-two row won.
- `TOP2_SPLIT`: one live top-two row won and one lost.
- `TOP2_ALL_LOST`: every live top-two row lost.
- `VOID`: no live top-two row.

The `Counts toward wins` column reads:
- `YES` only for a Rank 1 or Rank 2 `WIN`;
- otherwise `NO (loss)`, `NO (push)`, `NO (void)` or `NO (rank 3+ informational)`.

## 6. Keep the result separate from the process

A winning pick can have poor process, and a losing pick can have sound process. Assess both layers for every card:
- **Result layer:** what happened to each row.
- **Process layer:** identity, timing state, source quality and independence, lineups and availability, point-in-time integrity, endpoint and contract definition, distribution and probability, and any addendum's late news.

Record the process verdict in R9 and R10 as `Process: SOUND` or `Process: DEFICIENT — <what>`.

For a `mini-log-3` card also check, and write in R9: whether the `Rank-1 gate` was `PASS` or `RANK1_UNSTABLE` (an unstable card is scored in its own cohort, and its Rank-1 loss still gets the deep retrospection); whether `Adjustment dependence` was `ADJUSTMENT_DEPENDENT` and the adjusted or unadjusted top two would have won; whether a `Regime flag` was set, applied by the register's multiplier, or ignored (`REGIME_IGNORED`); and whether the `Evidence snapshots` retained show what was knowable at the research time.

## 7. Write the settlement section

Append after the footer, exactly in this form (see the golden example):

```markdown

# SETTLEMENT AND RETROSPECTIVES
<!-- SETTLEMENT-FORMAT: mini-settlement-2 -->

| Field | Value |
|---|---|
| Settled at | <ISO 8601 with offset> |
| GitHub HEAD SHA read | `<sha>` |
| Frozen original SHA-256 | `<sha256 of ORIGINAL_MINI file, or NOT_COMPUTED>` |
| Settlement directive | Settle every terminal event; missing details are settled on the A/B/C/E/OP/X evidence hierarchy |
```

Then write **one settlement block per card and per carryover**, carryovers first, then cards in ID order:

```markdown
<!-- BEGIN SETTLEMENT P-NNN -->
### Settlement · P-NNN · <Event>

**Card state:** `SETTLED`
**Final event:** <verified final, incl. regulation/OT/ET/extras and the statistic each row needs>
**Settlement sources:** <source — what it verified — evidence code>

| Rank | Proposition | p_card | Grade | Counts toward wins | Evidence | Basis |
|---|---|---|---|---|---|---|
| 1 | <proposition copied exactly from the card> | <p_card exactly as issued> | WIN | YES | A | <the fact that decided it> |
| 2 | … | … | LOSS | NO (loss) | … | … |
| 3 | … | … | … | NO (rank 3+ informational) | … | … |
| 4 | … | … | … | NO (rank 3+ informational) | … | … |

**Top-two result:** `<TOP2_ALL_WON|TOP2_SPLIT|TOP2_ALL_LOST|VOID>` — <w> counted win(s) of <n> live top-two row(s). Rank 1: <grade>; Rank 2: <grade>.
**Winner call:** <name from the card's Potential winner line>: `<CORRECT|INCORRECT|NOT_ISSUED|UNRESOLVED>`

**R1. Original prediction.** Copy THIS card's Rank 1 and Rank 2 propositions and p_card verbatim ("Rank 1 <proposition> p_card …; Rank 2 …"). `python -B -m research.operations.settlement_lint addenda <settled mini>.md` fails an R1 that describes another card's ranking or repeats the text of a different card (the P-539 to P-545 refresh blocks repeated P-538's).
**R2. Final event.** …
**R3. Contract settlement.** …
**R4. Rank diagnostics.** Rank 1 <grade>; Rank 2 <grade>; Hit@2 <0|1>; counted <w>/<n>; NDCG@2 <value, or n/a if any row is PUSH/VOID>.
**R5. Winner call.** …
**R6. Spread/total/line assessment.** How far the outcome landed from each line, in units and in SDs of the card's own distribution.
**R7. Expected vs realised mechanism.** …
**R8. Missed mechanism.** …
**R9. Source/timing review.** What was knowable at the forecast time; any addendum; `Process: SOUND|DEFICIENT — …`.
**R10. Error/process classification.** One or more of identity, source, latency, timing, contract, endpoint, availability, feature, model, variance, calibration, ranking, qualitative adjustment, true randomness.
**R11. Learning hypothesis.** A testable hypothesis only, with the test. `PROPOSED_NOT_TESTED`.
**R12. Disposition.** `NO_CHANGE | MONITOR | PROPOSE_EXPERIMENT | SOURCE_PROCESS_CHANGE_CANDIDATE | MODEL_CHANGE_CANDIDATE | RULE_CHANGE_CANDIDATE`.

<If Rank 1 won:> **Rank 1 won**, so no deep retrospection is triggered.
<!-- END SETTLEMENT P-NNN -->
```

For a non-terminal event the block is only:

```markdown
<!-- BEGIN SETTLEMENT P-NNN -->
### Settlement · P-NNN · <Event>

**Card state:** `PENDING_EVENT`
<why it is not terminal; new scheduled date if known>
<!-- END SETTLEMENT P-NNN -->
```

The validator checks these rules:
- Copy each proposition and `p_card` **exactly** from the card. Settle every ranked row exactly once.
- The `Top-two result` line must match the grades.
- Write the bold labels exactly as shown. Never start a heading with a P-ID.

## 8. Rank 1 lost: deep retrospection (Rule R1)

When Rank 1 is graded `LOSS`, add this immediately before `<!-- END SETTLEMENT P-NNN -->`:

```markdown
**Deep Rank-1 retrospection (mandatory: Rank 1 failed).**

**Claim.** The proposition, its p_card, the distribution parameters behind it and the gap to Rank 2.
**What happened.** The exact outcome against the line.
**Distribution check.** Where the outcome fell in the card's own distribution (z-score or tail probability). An ordinary miss, or a tail event?
**Knowability.** What information available before the cutoff pointed the other way, and whether it was used.
**Verdict.** VARIANCE, MODEL, PROCESS or a mix, with the share you assign to each.
**Own-top-two counterfactual.** Would a better process have chosen a different top two from the same distribution? Name the rows.
**Failure class.** `<one class from the list below>`
**Proposed correction.** A specific, testable change with its test. `PROPOSED_NOT_TESTED`.
```

**Failure classes** (use the closest one; use `OTHER` only with an explanation):

`FIRST_HALF_GOAL_OVERSELECTION` · `RUNLINE_CUSHION_CEILING` · `BASKETBALL_TOTAL_WITHOUT_PACE_MODEL` · `TENNIS_IID_UNDERDISPERSION` · `RANK_BY_Q_NOT_P` · `SHARED_DRIVER_TOP_TWO` · `HANDICAP_TAIL_OVERREACH` · `SMALL_SAMPLE_STRENGTH_OVERREACH` · `PHASE_INCOHERENCE` · `CORNER_ROW_WITHOUT_PROVIDER_OR_NB_MODEL` · `OVERCONFIDENT_PROBABILITY` · `WEAK_SLATE_FORCED_RANK` · `QUALITATIVE_RANKS_WITHOUT_DISTRIBUTION` · `REGIME_IGNORED` · `UNFITTED_ANALYST_ADJUSTMENT` · `LATE_INFORMATION` · `ENDPOINT_OR_CONTRACT` · `SOURCE_OR_IDENTITY` · `VARIANCE` · `OTHER`

Be honest: `VARIANCE` is right only when the outcome was an ordinary draw from a sound distribution with sound inputs.

## 9. Create the local settlement folder

```text
Mini Settlement - <FIRST-ID> to <LAST-ID> - <YYYY-MM-DD>/
├── ORIGINAL_MINI/<exact frozen copy of the active mini>.md
├── PREDICTION_MINI_SETTLED_<FIRST-ID>_<LAST-ID>.md   (frozen bytes + settlement section)
├── LOCAL_ID_MAPPING.md
├── UNRESOLVED_CARRYOVER.md
└── SETTLEMENT_MANIFEST.json
```

- `ORIGINAL_MINI/` holds exactly one file.
- `LOCAL_ID_MAPPING.md` has a table with columns `Local ID | Classification | Event key | Canonical mapping`:
  - cards: `PENDING_IMPORT`;
  - carryovers: their canonical ID;
  - addenda: listed under their parent ID.
- `UNRESOLVED_CARRYOVER.md` lists every `PENDING_EVENT` card with its event key, the reason and the new date, or `None.`. Prompt 2 carries these forward. Nothing else is carried.
- `SETTLEMENT_MANIFEST.json` contains:

```json
{
 "format": "mini-settlement-2",
 "mini_status": "CLOSED_LOCALLY",
 "github_head_read": "<sha>",
 "settled_at": "<ISO 8601>",
 "original": {"path": "ORIGINAL_MINI/<name>.md", "bytes": 0, "sha256": "<sha or NOT_COMPUTED>"},
 "settled": {"path": "PREDICTION_MINI_SETTLED_<FIRST>_<LAST>.md", "bytes": 0, "sha256": "<sha or NOT_COMPUTED>"},
 "first_id": "P-NNN", "last_id": "P-NNN",
 "cards": [], "carryovers": [], "addenda": [],
 "settled_ids": [], "pending_event_ids": [],
 "repository_next_id_snapshot": "P-NNN",
 "next_local_working_id": "P-NNN",
 "canonical_import": "PENDING",
 "writes": {"github": false, "combined_log": false, "canonical_ledger": false}
}
```

If you can write files only one at a time, write the settlement section as `SETTLEMENT_SECTION.md`. The user then builds the settled mini byte-exactly with the `join` command (section 10).

## 10. Verify

Check each of these:
- every working ID is preserved;
- every card and carryover has exactly one settlement block;
- the frozen bytes are an exact prefix of the settled mini;
- every proposition and `p_card` was copied exactly;
- the top-two lines match the grades;
- every Rank-1 loss has all eight deep parts and a listed failure class;
- the pending list matches `UNRESOLVED_CARRYOVER.md`;
- no GitHub write occurred.

With the repository available locally, the user can run (and `settlement_lint` is also run by CI on the active Combined Log):

```powershell
py -3.14 -B -m research.operations.mini_log join "ORIGINAL_MINI/<frozen>.md" "SETTLEMENT_SECTION.md" --out "PREDICTION_MINI_SETTLED_<FIRST>_<LAST>.md"
py -3.14 -B -m research.operations.mini_log verify-settled "ORIGINAL_MINI/<frozen>.md" "PREDICTION_MINI_SETTLED_<FIRST>_<LAST>.md" --out .
```

Both must report `"passed": true`. `verify-settled --out .` also writes `settlement_table.json`, which holds the machine-readable grades and the Rule T2 summary.

## 11. Report

```text
GitHub HEAD read:
Original mini / SHA-256 / bytes:
Settled mini / SHA-256 / bytes:
Cards: <n> · Carryovers: <n> · Addenda: <n>
Settled: <n> · PENDING_EVENT (carried forward): <ids or none>
Rows: WIN <n> · LOSS <n> · PUSH <n> · VOID <n> (evidence A <n>, B <n>, C <n>, E <n>, OP <n>, X <n>)
Counted (Rule T2): <wins>/<live top-two rows> = <x.x%>
Card classes: all won <n> · split <n> · all lost <n> · void <n> · Hit@2 <n>/<cards>
Rank 1: <W>–<L>–<V> · Rank 2: <W>–<L>–<V>
Mean NDCG@2 (fully graded slates): <x.xxxx>
Winner calls: <correct>/<issued>
Deep Rank-1 retrospections: <n> — failure classes: <class × n, …>
Next local working ID: <footer value> · Repository next-ID snapshot: <P-NNN>
Canonical mappings pending import: <ids>
GitHub writes: NO · Combined Log writes: NO · Ledger writes: NO
```

Provide every generated file in full, with its exact path.
