# PROMPT 3 — SETTLE THE ACTIVE LOCAL MINI AND WRITE THE RETROSPECTIVES

**Run by:** external chat agent · **GitHub:** read only · **Output:** a local settlement folder · **Mode:** `LOCAL_MINI_SETTLEMENT` · **Format:** `mini-settlement-3`

Use only the current `main` branch of `https://github.com/danisgreat/Sports-Research` as authority for method and rules. The active local mini and its working P-IDs hold the forecasts. Never renumber them because GitHub is behind. Nothing here needs code.

This task settles, grades and reviews. It does **not** import, allocate canonical IDs, change methodology, write new predictions or write to GitHub.

---

## 0. Reading gate

Print the **reading receipt** ([research/prompts/README.md](README.md)) after opening the documents in section 1. If any cannot be opened, say so and stop.

## 1. Read the authority

Record the `main` HEAD SHA and the time, then read:

1. [METHOD.md](../../METHOD.md) and [CURRENT_RULES.md](../../CURRENT_RULES.md): Rules **T2** (only Rank 1 and Rank 2 count as wins), **R1** (a Rank-1 failure needs the eight-part deep retrospection), §5 (evidence and sources) and §8 (the lifecycle).
2. [SELECTION_RULES.md](../../SELECTION_RULES.md): §7 (grades, evidence codes, card classes, the settlement allowance) and §8 (failure classes).
3. [SCORING_AND_VALIDATION.md](../../SCORING_AND_VALIDATION.md): top-two counting, NDCG@2, PUSH and VOID handling.
4. [CARD_AND_LOG_TEMPLATES.md](../../CARD_AND_LOG_TEMPLATES.md) §6 (the settled mini) and §9 (the settlement self-audit). A `mini-log-3` or `mini-log-2` mini is settled the same way.
5. [research/prompts/examples/EXAMPLE_SETTLED_MINI.md](examples/EXAMPLE_SETTLED_MINI.md): the exact settlement structure to copy.
6. [CURRENT_STATE.md](../../CURRENT_STATE.md) and [GAME_LOG_STATUS_CURRENT.md](../../GAME_LOG_STATUS_CURRENT.md): the repository's `Next canonical ID`, for the report.
7. The `RULES_*.md` file for each sport in the mini (endpoint, overtime and extra-time, retirement and abandonment rules), and the settlement routes in [SOURCES.md](../../SOURCES.md) for each sport.
8. [ARCHIVE_USE_GUIDE.md](../../ARCHIVE_USE_GUIDE.md) §6.

Then read the **active local mini** in full, including every card, carryover and addendum.

## 2. Freeze the mini before you write anything

1. Save an exact, unedited copy of the active mini as `ORIGINAL_MINI/<original file name>`. Do not reformat, re-save through an editor that changes line endings, or fix typos. These bytes are the forecast custody.
2. Record the **frozen original check**: the number of lines, the first and last card IDs, and the exact footer line `Next local working P-ID | P-NNN`. (No hash exists; a hash is `NOT_COMPUTED`. The repository agent confirms the prefix with a byte comparison at import.)
3. Record the card count, the carryover count and the addendum count.

The settled mini is the frozen bytes **followed by** the appended settlement section. Never edit, reorder or delete anything above the footer, including the footer itself.

## 3. Inventory and classify every record

For every block in the mini, record the ID, event key, native event ID, sport and league, event, research time, timing state and classification:

| Classification | Meaning | Settled here? |
|---|---|---|
| `LOCAL_UNIMPORTED_EVENT` | A card written in this mini | Yes |
| `ALREADY_CANONICAL_REFERENCE` | A carryover: already canonical, waiting for its event | Yes, if now terminal |
| `DATED_ADDENDUM` | A correction or late news under an existing ID | No; it consumes no ID and is never graded |

Mapping rule: every card keeps its working ID and reads `CANONICAL_MAPPING: PENDING_IMPORT`. Carryovers keep their canonical ID. Do not allocate or change any canonical ID here.

## 4. Research the results

For each event, research the final result from these sources, in order: (1) the official competition or field owner; (2) the official team or participant; (3) an official structured statistics provider; (4) independent high-quality corroboration. Use the route and fallback in the sport's SOURCES table and say which route decided each row. Settle from official scorecards and structured results; **narrative match reports, including machine-written ones, are not sources** and have decided the wrong winner before.

**Settlement SLA.** Settle each card within **72 hours** of its final (the clock starts at the scheduled start plus the allowance in SELECTION_RULES §7). Open carryover must stay at or below 5. List any breach in the report. A `mini-log-3` or `mini-log-4` card names its exact settlement fields and provider (`Settlement fields`) and a `Capture due` time: capture those pages first, because corners, half-time, period and player pages rot within days. Record in the Basis cell the page, the field and the time you read it; there are no stored bodies or hashes, so the quote and the time are the audit trail.

Verify the identity and date, the final state, the score, regulation versus overtime, extra time, extra innings or shootout, the period, half, set or innings splits, and any statistic a proposition needs. Check retirement, abandonment, rain and DLS where relevant. Do not infer a missing statistic from the final score alone. If you can only bound it, use evidence grade **E** and state your confidence.

**Past results.** If the season file under `Previous Sports Results/` already holds the game, compare its score with the official source. Agreement is a corroboration; disagreement is a source flag for R9. Do not edit the archive.

## 5. Settle every issued row (settle anyway)

Settle the **literal proposition as issued**, on the card's own endpoint. Each row receives exactly one grade and one evidence code.

**Grades:** `WIN`, `LOSS`, `PUSH` (an exact integer line, or a void-on-tie rule) or `VOID` (no admissible data, abandoned or cancelled with no result, or voided by rule).

**Evidence codes** (SELECTION_RULES §7):

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
- Complementary rows (for example Over 5.5 and Under 7.5) are dependent outcomes of one event, not independent trials.

**Counting (Rule T2).** Only Rank 1 and Rank 2 can count as wins. Ranks 3 and 4 are graded for calibration only. `PUSH` and `VOID` leave the denominator and are never losses. Card classes: `TOP2_ALL_WON`, `TOP2_SPLIT`, `TOP2_ALL_LOST`, `VOID`. The `Counts toward wins` column reads `YES` only for a Rank 1 or Rank 2 `WIN`; otherwise `NO (loss)`, `NO (push)`, `NO (void)` or `NO (rank 3+ informational)`.

## 6. Keep the result separate from the process

A winning pick can have poor process, and a losing pick can have sound process. Assess both layers for every card:

- **Result layer:** what happened to each row.
- **Process layer:** identity, timing state, source quality and independence, lineups and availability, point-in-time integrity, endpoint and contract definition, distribution and probability, the reading and archive lines, and any addendum's late news.

Record the process verdict in R9 and R10 as `Process: SOUND` or `Process: DEFICIENT — <what>`. For a `mini-log-3` or `mini-log-4` card also check, and write in R9:

- whether the `Rank-1 gate` was `PASS` or `RANK1_UNSTABLE` (an unstable card is scored in its own cohort, and its Rank-1 loss still gets the deep retrospection);
- whether `Adjustment dependence` was `ADJUSTMENT_DEPENDENT`, and whether the adjusted or unadjusted top two would have won;
- whether a `Regime flag` was set, applied by the register's multiplier, or ignored (`REGIME_IGNORED`);
- whether the `Evidence quotes` show what was knowable at the research time;
- whether the `Rules read` and `Archive check` lines named the rules, sources and past-result files that mattered, and which rule, source or archive file that would have changed the outcome was missed.

## 7. Write the settlement section

Append after the footer, exactly in the form of [CARD_AND_LOG_TEMPLATES.md](../../CARD_AND_LOG_TEMPLATES.md) §6:

```markdown

# SETTLEMENT AND RETROSPECTIVES
<!-- SETTLEMENT-FORMAT: mini-settlement-3 -->

| Field | Value |
|---|---|
| Settled at | <ISO 8601 with offset> |
| GitHub HEAD SHA read | `<sha>` |
| Frozen original check | `<N lines; cards P-AAA to P-BBB; footer line "Next local working P-ID | P-NNN">` |
| Rules read | `<documents and sections applied>` |
| Settlement directive | Settle every terminal event; missing details settle on the A/B/C/E/OP/X evidence hierarchy |
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
| 1 | <proposition copied exactly from the card> | <p_card exactly as issued> | WIN | YES | A | <the fact that decided it, with the source field and time> |
| 2 | … | … | LOSS | NO (loss) | … | … |
| 3 | … | … | … | NO (rank 3+ informational) | … | … |
| 4 | … | … | … | NO (rank 3+ informational) | … | … |

**Top-two result:** `<TOP2_ALL_WON|TOP2_SPLIT|TOP2_ALL_LOST|VOID>` — <w> counted win(s) of <n> live top-two row(s). Rank 1: <grade>; Rank 2: <grade>.
**Winner call:** <name from the card's Potential winner line>: `<CORRECT|INCORRECT|NOT_ISSUED|UNRESOLVED>`

**R1. Original prediction.** Copy THIS card's Rank 1 and Rank 2 propositions and p_card verbatim ("Rank 1 <proposition> p_card …; Rank 2 …"). An R1 that describes another card's ranking, or repeats the text of a different card, fails the settlement self-audit (the P-539 to P-545 refresh blocks repeated P-538's).
**R2. Final event.** …
**R3. Contract settlement.** …
**R4. Rank diagnostics.** Rank 1 <grade>; Rank 2 <grade>; Hit@2 <0|1>; counted <w>/<n>; NDCG@2 <value, or n/a if any row is PUSH/VOID>.
**R5. Winner call.** …
**R6. Spread/total/line assessment.** How far the outcome landed from each line, in units and in SDs of the card's own distribution.
**R7. Expected vs realised mechanism.** …
**R8. Missed mechanism.** …
**R9. Source/timing review.** What was knowable at the forecast time; any addendum; the SOURCES route and archive file used or missed; `Process: SOUND|DEFICIENT — …`.
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

The self-audit (section 10) checks these rules: copy each proposition and `p_card` **exactly** from the card; settle every ranked row exactly once; the `Top-two result` line matches the grades; write the bold labels exactly as shown; never start a heading with a P-ID.

## 8. Rank 1 lost: deep retrospection (Rule R1)

When Rank 1 is graded `LOSS`, add this immediately before `<!-- END SETTLEMENT P-NNN -->`:

```markdown
**Deep Rank-1 retrospection (mandatory: Rank 1 failed).**

**Claim.** The proposition, its p_card, the distribution parameters behind it and the gap to Rank 2.
**What happened.** The exact outcome against the line.
**Distribution check.** Where the outcome fell in the card's own distribution (z-score or tail probability, recomputed by hand). An ordinary miss, or a tail event?
**Knowability.** What information available before the cutoff pointed the other way, and whether it was used. Name the rule, source or archive file that would have caught it.
**Verdict.** VARIANCE, MODEL, PROCESS or a mix, with the share you assign to each.
**Own-top-two counterfactual.** Would a better process have chosen a different top two from the same distribution? Name the rows.
**Failure class.** `<one class from SELECTION_RULES §8>`
**Proposed correction.** A specific, testable change with its test. `PROPOSED_NOT_TESTED`.
```

Be honest: `VARIANCE` is right only when the outcome was an ordinary draw from a sound distribution with sound inputs.

## 9. Create the local settlement folder

```text
Mini Settlement - <FIRST-ID> to <LAST-ID> - <YYYY-MM-DD>/
├── ORIGINAL_MINI/<exact frozen copy of the active mini>.md
├── PREDICTION_MINI_SETTLED_<FIRST-ID>_<LAST-ID>.md   (frozen bytes + settlement section)
├── LOCAL_ID_MAPPING.md
├── UNRESOLVED_CARRYOVER.md
└── SETTLEMENT_MANIFEST.md
```

- `ORIGINAL_MINI/` holds exactly one file.
- `LOCAL_ID_MAPPING.md` has a table with columns `Local ID | Classification | Event key | Canonical mapping`: cards `PENDING_IMPORT`; carryovers their canonical ID; addenda listed under their parent ID.
- `UNRESOLVED_CARRYOVER.md` lists every `PENDING_EVENT` card with its event key, the reason and the new date, or `None.`. Prompt 2 carries these forward. Nothing else is carried.
- `SETTLEMENT_MANIFEST.md` is the two-column table described in CARD_AND_LOG_TEMPLATES §6 (format, status `CLOSED_LOCALLY`, HEAD read, times, line counts, the frozen check, first and last ID, card, carryover, addendum, settled and pending IDs, next-ID snapshot, next local working ID, canonical import `PENDING`, writes none).

If you can write files only one at a time, write the settlement section as `SETTLEMENT_SECTION.md`. The repository agent then builds the settled mini by copying the frozen file and appending the section (prompt 4, step 3).

## 10. Settlement self-audit (print the table with evidence)

Run **S1 to S13** from [CARD_AND_LOG_TEMPLATES.md](../../CARD_AND_LOG_TEMPLATES.md) §9 and print `| Check | Result | Evidence |`: every working ID preserved; one block per card and carryover; the frozen file is the exact prefix; propositions and `p_card` copied exactly; grades, counts and the top-two line agree; every Basis cites the field, source and time; R1 describes this card; every Rank-1 loss has all eight parts and a failure class; the card's own contract rules applied; only non-terminal events pending; SLA and carryover cap; process verdicts; reading and archive lines reviewed; nothing written to GitHub or a log.

## 11. Report

```text
READING RECEIPT: <as printed>
GitHub HEAD read:
Original mini: <lines> · cards P-… to P-… · footer line
Settled mini: <lines>
Cards: <n> · Carryovers: <n> · Addenda: <n>
Settled: <n> · PENDING_EVENT (carried forward): <ids or none>
Rows: WIN <n> · LOSS <n> · PUSH <n> · VOID <n> (evidence A <n>, B <n>, C <n>, E <n>, OP <n>, X <n>)
Counted (Rule T2): <wins>/<live top-two rows> = <x.x%>
Card classes: all won <n> · split <n> · all lost <n> · void <n> · Hit@2 <n>/<cards>
Rank 1: <W>–<L>–<V> · Rank 2: <W>–<L>–<V>
Mean NDCG@2 (fully graded slates): <x.xxxx>
Winner calls: <correct>/<issued>
Deep Rank-1 retrospections: <n> — failure classes: <class × n, …>
SLA breaches: <ids or none> · Open carryover: <n>
Archive agreement checks: <n agree · n disagree · n not in archive>
Next local working ID: <footer value> · Repository next-ID snapshot: <P-NNN>
Canonical mappings pending import: <ids>
Self-audit S1-S13: all PASS / failures fixed: <list>
GitHub writes: NO · Combined Log writes: NO · Ledger writes: NO
```

Provide every generated file in full, with its exact path.
