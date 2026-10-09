# Card and log templates

**Formats: `mini-log-4` (new minis), `mini-settlement-3`, canonical entry format `canonical-md-1`.** Authority: [CURRENT_RULES.md](CURRENT_RULES.md), MDS-2026.10.09-v9.0 / CR-2026.10.09-R5. The pre-rewrite template page, including the certified-issuer protocol, is kept in [archive/superseded_2026-10-09/CARD_AND_LOG_TEMPLATES.md](archive/superseded_2026-10-09/CARD_AND_LOG_TEMPLATES.md).

There is no validator program. The agent that writes a card, a settlement or an import **audits it by hand** with the checklists in sections 7 and 9 and prints each check with its evidence. A check that is listed but not shown is treated as not done.

## 1. What changed from `mini-log-3`

`mini-log-4` is `mini-log-3` with the code and hash dependencies removed and the reading and archive discipline added. Minis already started in `mini-log-3` or `mini-log-2` stay valid and are finished in their own format; their legacy examples are in `archive/superseded_2026-10-09/prompts/examples/` and `research/prompts/examples/legacy_mini_log_2/`.

| Item | `mini-log-3` | `mini-log-4` |
|---|---|---|
| First line tag | `<!-- MINI-LOG-FORMAT: mini-log-3 -->` | `<!-- MINI-LOG-FORMAT: mini-log-4 -->` |
| Authority table | Row `Active manifest` | Row `Reading receipt` replaces it (documents read at the HEAD SHA) |
| Card bullet `Evidence snapshots` | `sha256:<hash>@<time>` tokens | **`Evidence quotes`**: `<source> @ <ISO time> — "<verbatim excerpt>"` items, or `NONE` |
| New card bullets | | **`Rules read`** and **`Archive check`** (both required) |
| Settlement header | `Frozen original SHA-256` | `Frozen original check` and `Rules read` |
| Settlement tag | `mini-settlement-2` | `mini-settlement-3` |
| Settlement folder file | `SETTLEMENT_MANIFEST.json` | `SETTLEMENT_MANIFEST.md` |
| Validation | `mini_log verify` and friends | Self-audit checklists (sections 7 and 9) |

## 2. The mini file

**Path.** `Mini Prediction Log - <FIRST> onward - <YYYY-MM-DD>/PREDICTION_MINI_RUNNING_LOG_<FIRST>_ONWARD.md`.

**Layout, in order:**

1. First line `<!-- MINI-LOG-FORMAT: mini-log-4 -->`.
2. `# Prediction Mini Running Log — <FIRST> onward`.
3. `## A. Authority snapshot`: a two-column table with every field below filled with a real value (no `<…>` left):

| Field | Value |
|---|---|
| Repository | `https://github.com/danisgreat/Sports-Research` |
| Branch | `main` |
| GitHub HEAD SHA | the 40-hex commit you read |
| Method | `MDS-2026.10.09-v9.0` (read it from CURRENT_STATE) |
| Control revision | `CR-2026.10.09-R5` |
| Scoring version | `SCV-2026.10.09-v5` |
| Active Combined Log | `prediction logs/PREDICTION_LOG_COMBINED_7.md` (read it from CURRENT_STATE) |
| Highest committed repository P-ID | from CURRENT_STATE |
| Repository next-ID snapshot | from CURRENT_STATE, equal to GAME_LOG_STATUS_CURRENT |
| Highest local working P-ID before creation | the previous mini's highest, or `NONE` |
| First working P-ID for this mini | max(next-ID snapshot, previous highest + 1) |
| Reading receipt | the documents read in full, with the HEAD SHA and the time |
| Mini opened | ISO 8601 with UTC offset |
| Mode | `LOCAL_MINI_STAGING` |

   Then the line `SPORTS_ONLY / MARKET_BLIND · PERFORMANCE_ELIGIBILITY: NOT_CERTIFIED · CANONICAL_IMPORT_STATUS: PENDING`.
4. `## B. Local ID rules`: five bullets (creating the mini consumes no ID; one event = one working ID; a working ID advances only after a complete card is written and audited; addenda, corrections, duplicates and aliases keep the original ID; working IDs never change and canonical import keeps them or stops on a collision).
5. `## C. Active carryover`: carryover blocks, or `None.`
6. `# NEW LOCAL EVENT CARDS`: empty at creation. Never create a placeholder card.
7. `# RUNNING FOOTER`, with the table between `<!-- BEGIN FOOTER -->` and `<!-- END FOOTER -->`:

| Field | Value |
|---|---|
| Highest local working P-ID actually used | `NONE` at creation |
| Next local working P-ID | the first working ID |
| Repository next-ID snapshot when mini opened | the snapshot |
| Active carryovers | count |
| New event cards | `0` at creation |
| Local mini status | `ACTIVE` |
| Canonical import | `PENDING` |
| GitHub writes performed | `NO` |

**IDs.** The first working ID is the larger of the repository's next canonical ID and the previous mini's highest working ID + 1. One sporting event is one ID, issued in increasing order; IDs never change. Creating a mini, an addendum, a carryover or a settlement consumes no ID.

**Blocks.** Every unit sits between exact markers. No heading inside a block may start with a P-ID (`## P-…`), because the import step would read it as a new card.

| Block | Markers | First line | Where |
|---|---|---|---|
| Card | `<!-- BEGIN CARD P-NNN -->` … `<!-- END CARD P-NNN -->` | `## Card · P-NNN · SPORT / LEAGUE · Event · YYYY-MM-DD` | After `# NEW LOCAL EVENT CARDS`, before the footer, increasing ID |
| Carryover | `<!-- BEGIN CARRYOVER P-NNN -->` … `<!-- END CARRYOVER P-NNN -->` | `### Carryover · P-NNN · …` | Section C; ID below every new card |
| Addendum | `<!-- BEGIN ADDENDUM P-NNN -->` … `<!-- END ADDENDUM P-NNN -->` | `### Addendum · P-NNN · <ISO 8601 with offset>` | After the card it amends, before the footer |
| Settlement | `<!-- BEGIN SETTLEMENT P-NNN -->` … `<!-- END SETTLEMENT P-NNN -->` | `### Settlement · P-NNN · Event` | Only in the appended settlement section |

**Carryover block.**

```markdown
<!-- BEGIN CARRYOVER P-NNN -->
### Carryover · P-NNN · <SPORT / LEAGUE> · <Event> · <YYYY-MM-DD>

- **Canonical ID:** `P-NNN` (canonical since import <date>; confirm in GAME_LOG_STATUS_CURRENT.md)
- **Event key:** `<identical to the original card>`
- **Sport:** `<…>`
- **League:** `<…>`
- **Carryover class:** `ACTIVE_SPORTING_CARRYOVER`
- **Remaining requirement:** <why it is not terminal, and the new scheduled date if known; settle within 72 h of its final>

<the original card's pick table, copied byte for byte: header, separator and four rows>

DO NOT SETTLE UNTIL THE EVENT IS TERMINAL.
<!-- END CARRYOVER P-NNN -->
```

## 3. The card

Insert the card **immediately before `# RUNNING FOOTER`**. Fill every `<…>`; `N/A`, `NONE` and `FRAMEWORK_DEFAULT:` are explicit values, never blanks.

```markdown
<!-- BEGIN CARD P-NNN -->
## Card · P-NNN · <SPORT / LEAGUE> · <Away @ Home | Player A vs Player B> · <YYYY-MM-DD>

- **Working ID:** `P-NNN — LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT`
- **Event key:** `<LEAGUE>:<SEASON>:<native-or-surrogate>:<YYYY-MM-DD>`
- **Native event ID:** `<id>` or `NOT_VERIFIED`
- **Sport:** `<Baseball | Cricket | Basketball | Ice hockey | Tennis | Soccer | Rugby league | Rugby union | Australian rules | American football>`
- **League:** `<league>`
- **Tracking alias:** `LOCAL-<YYYYMMDD>-P-NNN-<LEAGUE>-<AWAY>-<HOME>`
- **Analysis status:** `UNCALIBRATED_ANALYST_SCENARIO`
- **Timing state:** `PREGAME | LATE_START_UNVERIFIED | LIVE_OBSERVED`
- **Research completed:** `<ISO 8601 with offset>`
- **Scheduled start:** `<ISO 8601 with offset>`
- **Endpoint:** `<exact endpoint, incl. OT/SO/extras/retirement convention>`
- **Distribution object:** `<family>_<method>_v<n> — <parameters, one line>`
- **Regime flags:** `NONE` or a comma-separated list
- **Retirement rule:** `N/A | FRAMEWORK_DEFAULT: … | OPERATOR: <name>: …`
- **Listed-pitcher rule:** `N/A | FRAMEWORK_DEFAULT: … | OPERATOR: <name>: …`
- **Abandonment rule:** `N/A | FRAMEWORK_DEFAULT: … | OPERATOR: <name>: …`
- **Settlement fields:** `<field> (provider: <name>)`
- **Capture due:** `<ISO 8601 with offset, after the start and within 36 h of it>`
- **Rules read:** `<documents and sections actually applied, e.g. RULES_BASEBALL §3 §8; SELECTION_RULES §2-§4; SOURCES §3 KBO; BASE_RATES §5>`
- **Archive check:** `<file(s) · rows read · date range · recipes · finding>` or `ARCHIVE_PARTIAL: …` or `ARCHIVE_UNAVAILABLE: <exact reason>`
- **Evidence quotes:** `<source> @ <ISO time> — "<verbatim excerpt up to 200 characters>"; …` or `NONE`

### Decision block

**Distribution:** `<id>` — <parameters>; <how the ladder was priced>.

| Rank | Role | Tag | Proposition | p_card | Probability status | Evidence | Failure route |
|---|---|---|---|---|---|---|---|
| 1 | PICK | SUPPLIED or ANALYST_DERIVED (replaces …) | <exact proposition, line, period, endpoint> | <xx.x%> | FROM_DISTRIBUTION:<id> | <key evidence> | <main failure route> |
| 2 | PICK | … | … | … | FROM_DISTRIBUTION:<id> | … | … |
| 3 | INFORMATIONAL | … | … | … | FROM_DISTRIBUTION:<id> | … | … |
| 4 | INFORMATIONAL | … | … | … | FROM_DISTRIBUTION:<id> | … | … |

**P(Rank 1 and Rank 2 both lose):** <xx.x%>
**Rank 1 − Rank 2 gap:** <x.x points>
**Rank-1 gate:** PASS | RANK1_UNSTABLE — p_card <xx.x%>; best non-complementary alternative <xx.x%>; margin <x.x points>
**Adjustment dependence:** NONE | ADJUSTMENT_DEPENDENT
**Supplied rows not selected:** <each with its p_card from the same distribution>
**Potential winner:** <name> — <xx.x%> (<endpoint>)

### Appendix

#### A1. Identity, timing and state
#### A2. Supplied contracts (reference only, Rule P4)
#### A3. Evidence summary
#### A4. Event distribution
#### A5. Priced ladder (excerpt)
#### A6. Adjustments
**Adjustments:** NONE   (or the table | Name | Target | Size | SD units | Prior basis |, then `**Unadjusted top two:** …` when any adjustment exceeds 0.25 SD)
#### A7. Family checks
#### A8. Sources
#### A9. Integrity receipt
`SPORTS_ONLY_MARKET_BLIND: PASS` · `OBSERVED_IN_GAME_OUTCOME_USED: NO` · `SETTLEMENT: NOT_PERFORMED`
<!-- END CARD P-NNN -->
```

**What each part must contain**

- **Decision block:** the page you would act on, about 650 words at most. The distribution line, the pick table and the six bold lines only.
- **A1:** native event, fixture state, source update time, the statement that no in-game information was used.
- **A3 Evidence summary:** every decisive claim with its source and the time you read it. The numbers taken from the archive and the profile row ([LEAGUE_PROFILES.md](LEAGUE_PROFILES.md)) appear here.
- **A4 Event distribution:** the family, every parameter, the arithmetic from the inputs to the grid (formula, table section used), the endpoint resolution, the sensitivity case and how the top two moved.
- **A5 Priced ladder:** at least the four candidates and the lines either side of each; the complement of each priced line.
- **A7 Family checks:** the result of every applicable check in [SELECTION_RULES.md](SELECTION_RULES.md) §4 and of the sport block.
- **A8 Sources:** each source with what it supported and the time read; `(fallback: <source>)` where a fallback route was used.

**Pick table rules.** The header exactly as shown; exactly **four** data rows; roles `PICK, PICK, INFORMATIONAL, INFORMATIONAL`; a tag starting `SUPPLIED` or `ANALYST_DERIVED`; every `p_card` a percentage in (0%, 90%]; non-increasing down the table; `Probability status` reads `FROM_DISTRIBUTION:` followed by the id in `Distribution object`; no `q` column; no `TO_FILL` placeholder anywhere. The bold lines are spelled exactly as shown. The gate label must agree with the numbers on its line.

## 4. Adjustments, regimes and family rules

- **Adjustments table:** `| Name | Target | Size | SD units | Prior basis |`, basis `fitted`, `archive_estimate` or `analyst_judgement`. If any adjustment exceeds 0.25 SD, print `**Unadjusted top two:** <rank 1>; <rank 2>` in A6 and set `**Adjustment dependence:**` to `ADJUSTMENT_DEPENDENT` exactly when that pair differs from the picks.
- **Regime flags:** from the table in BASE_RATES_REGISTER ([SELECTION_RULES.md](SELECTION_RULES.md) §6).
- **Family rules:** [SELECTION_RULES.md](SELECTION_RULES.md) §4.

## 5. Addenda and re-forecasts (no new ID)

```markdown
<!-- BEGIN ADDENDUM P-NNN -->
### Addendum · P-NNN · <ISO 8601 time with offset>
<what changed, why, and whether the original ranking would change; the original card stays unchanged and is what gets graded>
<!-- END ADDENDUM P-NNN -->
```

Place it after the card it amends and before `# RUNNING FOOTER`; leave the footer unchanged. The ID is the amended card's own ID, or the canonical ID of an earlier card found by the duplicate check. The time is ISO 8601 with an offset. An addendum contains no pick table and no heading that starts with a P-ID, never consumes an ID and never edits the original card. Settlement grades the original card only.

**Re-forecast trigger.** A confirmed starter, goalie or quarterback change, or a lineup change large enough to move the ranks, that becomes public after the research time and before the start makes the ranks stale. Write an addendum with the trigger, its source and time, and a re-priced table headed `| Rank | Proposition | p_reforecast |` (deliberately not the pick-table header, so it cannot be read as a second pick table). A change qualifies when it alters a distribution input by more than 0.25 SD or reorders the top two; say which. The original card is still what is graded.

## 6. The settled mini (`mini-settlement-3`)

The settled mini is the frozen mini's exact bytes **followed by** the appended settlement section. Nothing above the footer, including the footer, is edited.

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

One settlement block per carryover (first) and per card (in ID order):

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

**R1. Original prediction.** Copy THIS card's Rank 1 and Rank 2 propositions and p_card verbatim.
**R2. Final event.** …
**R3. Contract settlement.** …
**R4. Rank diagnostics.** Rank 1 <grade>; Rank 2 <grade>; Hit@2 <0|1>; counted <w>/<n>; NDCG@2 <value, or n/a if any row is PUSH/VOID>.
**R5. Winner call.** …
**R6. Spread/total/line assessment.** How far the outcome landed from each line, in units and in SDs of the card's own distribution.
**R7. Expected vs realised mechanism.** …
**R8. Missed mechanism.** …
**R9. Source/timing review.** What was knowable at the forecast time; any addendum; which SOURCES route and which archive file were used or missed; `Process: SOUND|DEFICIENT — …`.
**R10. Error/process classification.** One or more of identity, source, latency, timing, contract, endpoint, availability, feature, model, variance, calibration, ranking, qualitative adjustment, true randomness.
**R11. Learning hypothesis.** A testable hypothesis only, with the test. `PROPOSED_NOT_TESTED`.
**R12. Disposition.** `NO_CHANGE | MONITOR | PROPOSE_EXPERIMENT | SOURCE_PROCESS_CHANGE_CANDIDATE | MODEL_CHANGE_CANDIDATE | RULE_CHANGE_CANDIDATE`.

<If Rank 1 won:> **Rank 1 won**, so no deep retrospection is triggered.
<!-- END SETTLEMENT P-NNN -->
```

A non-terminal event: the block holds only `**Card state:** \`PENDING_EVENT\`` and the reason and new date.

When Rank 1 lost, add immediately before `<!-- END SETTLEMENT P-NNN -->`:

```markdown
**Deep Rank-1 retrospection (mandatory: Rank 1 failed).**

**Claim.** …
**What happened.** …
**Distribution check.** …
**Knowability.** …
**Verdict.** …
**Own-top-two counterfactual.** …
**Failure class.** `<one class from SELECTION_RULES §8>`
**Proposed correction.** … `PROPOSED_NOT_TESTED`.
```

`Counts toward wins` reads `YES` only for a Rank 1 or Rank 2 `WIN`; otherwise `NO (loss)`, `NO (push)`, `NO (void)` or `NO (rank 3+ informational)`. Evidence `X` must be `VOID`.

**Settlement folder.**

```text
Mini Settlement - <FIRST> to <LAST> - <YYYY-MM-DD>/
├── ORIGINAL_MINI/<exact frozen copy>.md
├── PREDICTION_MINI_SETTLED_<FIRST>_<LAST>.md        (frozen bytes + settlement section)
├── LOCAL_ID_MAPPING.md                              (Local ID | Classification | Event key | Canonical mapping)
├── UNRESOLVED_CARRYOVER.md                          (every PENDING_EVENT card, or "None.")
└── SETTLEMENT_MANIFEST.md                           (table of the fields below)
```

`SETTLEMENT_MANIFEST.md` is a two-column table: format `mini-settlement-3`; mini status `CLOSED_LOCALLY`; GitHub HEAD read; settled at; original path and line count; settled path and line count; frozen check; first and last ID; card IDs; carryover IDs; addendum IDs; settled IDs; `PENDING_EVENT` IDs; repository next-ID snapshot; next local working ID; canonical import `PENDING`; writes `GitHub: no, Combined Log: no`.

## 7. Card self-audit (print this with evidence before returning a card)

Print a table `| Check | Result | Evidence |`. Evidence is the number, the quote or the grep result that shows the check, not the word "ok".

| # | Check |
|---|---|
| C1 | The heading ID equals the marker ID. No heading inside the card starts with a P-ID. |
| C2 | Every metadata bullet is present and non-blank. Working ID reads `P-NNN — LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT`. The event key ends `:YYYY-MM-DD`. Timing state is one of the three allowed values. |
| C3 | The pick table has the exact header, four rows, roles `PICK, PICK, INFORMATIONAL, INFORMATIONAL`, valid tags, `p_card` in (0%, 90%], non-increasing order, `FROM_DISTRIBUTION:<id>` equal to the id in `Distribution object`, no `q` column, no `TO_FILL`. |
| C4 | Complements add to 100% (win + push + loss) on every priced line printed in A5, and prices are monotone across lines. Show two examples. |
| C5 | Gate arithmetic recomputed: Rank 1 `p_card`, best non-complementary alternative, margin. The label (`PASS` / `RANK1_UNSTABLE`) agrees with the numbers ([SELECTION_RULES.md](SELECTION_RULES.md) §2). |
| C6 | Rank 2 meets the 58% floor (or the card says it did not) and P(both lose) is computed by the §3 case that applies. If above 35% the weaker pick was replaced and the change is stated. |
| C7 | Adjustments table matches the distribution parameters. Above 0.25 SD: `Unadjusted top two` printed and `Adjustment dependence` agrees. |
| C8 | `Regime flags` taken from the BASE_RATES regime table; the multiplier applied only where `Recommended` is not 1.000. |
| C9 | Every applicable family rule and the sport block's checks are answered in A7. |
| C10 | `Retirement rule`, `Listed-pitcher rule`, `Abandonment rule` filled. `Settlement fields` name a provider. Any corners, half-time, period or player row has a provider and `Capture due` within 36 h after the start. |
| C11 | Timing honest: the research time, the fixture state and its source update time are stated. No in-game information was used. |
| C12 | Market blind: no odds, line movement, tips, previews, prediction markets or fantasy data; supplied lines used only as thresholds. |
| C13 | `Evidence quotes` holds a verbatim excerpt for each decisive lineup, goalie, starter, injury or weather claim. `NONE` only if Rank 1 does not rest on such a claim. |
| C14 | `Archive check` is filled, with files, rows, dates, recipes and finding, or an exact `ARCHIVE_UNAVAILABLE` reason. The numbers it supplied are shown in A3 or A4. |
| C15 | `Rules read` names the sport file, the SELECTION_RULES sections, the SOURCES route and the BASE_RATES / LEAGUE_PROFILES rows actually applied. |
| C16 | A sensitivity case on the most uncertain input is reported with how the top two moved. |
| C17 | Decision block within about 650 words; appendix A1-A9 present; the six bold lines present and spelled exactly. |
| C18 | The card appears once; the ID and the event key are unique in the mini (search the mini); the duplicate check against the status register and the active Combined Log header found nothing. |
| C19 | The footer was updated: highest used = this ID, next = this ID + 1, new event cards + 1. Every earlier byte of the mini is unchanged. |
| C20 | Each source in A8 states what it supported and when it was read. |

## 8. Canonical entry format `canonical-md-1` (written by the import step)

The import step (prompt 4) appends to the active Combined Log, after its last block and never above it:

```markdown
<!-- BEGIN CANONICAL RESEARCH P-NNN -->
## P-NNN — <SPORT / LEAGUE> — <Event> — <YYYY-MM-DD>

Imported from the local mini `<mini file name>` on <date>; local working ID kept (identity mapping, no renumbering). Original card bytes follow unchanged except that the card's own heading line is replaced by the heading above.

<the card block's lines after its "## Card · …" heading, byte for byte, from "- **Working ID:**" to "SETTLEMENT: NOT_PERFORMED">
<!-- END CANONICAL RESEARCH P-NNN -->
```

Dated additions use `<!-- BEGIN RESEARCH ADDENDUM P-NNN <YYYYMMDD>-<k> -->` … `<!-- END RESEARCH ADDENDUM P-NNN <YYYYMMDD>-<k> -->`, where `<k>` counts that ID's additions that day. An imported addendum holds the addendum block verbatim; an imported settlement holds the settlement block verbatim under the heading `**Final settlement (<date>).**`. Earlier entries in the logs carry a 32-character token after the ID; the Markdown-only format omits it. The status register row for each new ID is `| **P-NNN** | <Event> | <Tracking alias> | <status> |`, and the register's `Next canonical ID` line moves to the highest imported ID + 1.

**Rollover.** The closing block appended to Part N is `<!-- BEGIN ROLLOVER CLOSURE PART N -->` … `<!-- END ROLLOVER CLOSURE PART N -->` and records the time, the main HEAD, the range of cards in the part, the highest committed ID and the unchanged next ID, and the line count of the part before the block. The new part's header states the status, opening time, method, control revision, previous part, highest and next ID with the note "creating this file consumes no ID", reserved IDs, carryover pointer, SPORTS_ONLY / MARKET_BLIND, the certification disclaimer, a continuity table of every earlier part and the logging rules, followed by `<!-- END ACTIVE COMBINED LOG HEADER -->`.

## 9. Settlement self-audit (print before returning a settlement)

| # | Check |
|---|---|
| S1 | Every working ID is preserved. Every card and every carryover has exactly one settlement block. |
| S2 | The frozen file is the exact prefix of the settled file (`cmp` or a line-by-line comparison of the first N lines), and the header's `Frozen original check` matches. |
| S3 | Every proposition and `p_card` is copied exactly from the card (compare cell by cell). |
| S4 | Grades, `Counts toward wins` and the `Top-two result` line agree. PUSH and VOID are not losses. Evidence `X` rows are VOID. |
| S5 | Each settled row's Basis cites the field, the source and the time read. Settlement is from the feed (official scorecard or structured result), not from a narrative report. |
| S6 | R1 describes THIS card's ranking, not another card's. R1-R12 are all present. |
| S7 | Every Rank-1 LOSS has all eight deep parts and a failure class from [SELECTION_RULES.md](SELECTION_RULES.md) §8. |
| S8 | The card's own `Retirement rule`, `Listed-pitcher rule` and `Abandonment rule` were applied as written, and the row graded `OP`. |
| S9 | Only non-terminal events are `PENDING_EVENT`; they match `UNRESOLVED_CARRYOVER.md`. |
| S10 | Open carryover is at or below 5, and each card was settled within 72 hours of its final (list any breach). |
| S11 | The process verdict (`SOUND` / `DEFICIENT`) is in R9 and R10, and the gate label, adjustment dependence, regime flag, and evidence quotes were reviewed. |
| S12 | `Rules read` and the archive agreement or disagreement are in the header and in R9. |
| S13 | Nothing was written to GitHub or a Combined Log; no ID was allocated. |

## 10. Experiments and canonical cards

Creating a hypothesis, a power plan or a measured result never allocates an ID or backfills a historical card ([HYPOTHESIS_REGISTER.md](HYPOTHESIS_REGISTER.md)). Requested game cards still go to the active Combined Log through the lifecycle. Retain the original `p`, ranking `q` and issued versions; `q` is not scored as an event probability.
