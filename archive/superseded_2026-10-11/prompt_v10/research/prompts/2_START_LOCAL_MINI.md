# PROMPT 2 — START A NEW LOCAL MINI RUNNING LOG

**Run by:** external chat agent · **GitHub:** read only · **Output:** one new local Markdown file · **Mode:** `LOCAL_MINI_STAGING` · **Format:** `mini-log-5`

Use only the current `main` branch of `https://github.com/danisgreat/Sports-Research` as authority. Do not use Google Drive, stale downloads, older chat assumptions, other branches or superseded rules. Nothing in this task needs code: read documents, copy structure, fill fields.

This task creates an empty mini. It performs **no** research, prediction, settlement, grading, retrospective, rule change or GitHub write.

---

## 0. Reading gate

Open the documents in section 1 and print the **reading receipt** ([research/prompts/README.md](README.md), "The reading gate") before anything else. If any document cannot be opened, report which and stop.

## 1. Read the current authority

Record the HEAD commit SHA of `main` and the time you read, then read:

1. [CURRENT_STATE.md](../../CURRENT_STATE.md): method, control revision, scoring version, **next canonical ID**, highest committed ID, active Combined Log, mini-log format.
2. [METHOD.md](../../METHOD.md): confirms the method, control revision and scoring version that CURRENT_STATE states.
3. [CURRENT_RULES.md](../../CURRENT_RULES.md): Rules T2, R1 and P4, the reading gate (§1) and the local-mini lifecycle (§8).
4. [SELECTION_RULES.md](../../SELECTION_RULES.md): the constants the cards will use.
5. [CARD_AND_LOG_TEMPLATES.md](../../CARD_AND_LOG_TEMPLATES.md) §2 (the mini file) and §3 (the card).
6. [GAME_LOG_STATUS_CURRENT.md](../../GAME_LOG_STATUS_CURRENT.md): the line `Next canonical ID: P-NNN` (it must equal CURRENT_STATE).
7. The header of the active Combined Log named in CURRENT_STATE (everything above `<!-- END ACTIVE COMBINED LOG HEADER -->`): its status, highest committed ID and next ID must agree with CURRENT_STATE.
8. [research/prompts/examples/EXAMPLE_ACTIVE_MINI.md](examples/EXAMPLE_ACTIVE_MINI.md): the exact structure to copy.

If these sources disagree with each other, report the disagreement and stop.

## 2. Read the previous local mini

Ask the user for (or locate) the most recent **settled** mini folder (`Mini Settlement - <FIRST> to <LAST> - <date>/`), and read in full:

- `PREDICTION_MINI_SETTLED_<FIRST>_<LAST>.md`;
- `UNRESOLVED_CARRYOVER.md`, which lists the `PENDING_EVENT` cards.

If there is no previous mini, record `Highest local working P-ID before creation: NONE` and `Active carryover: None.`

## 3. Choose the first working ID

```text
REPOSITORY_NEXT_ID_SNAPSHOT = <Next canonical ID from CURRENT_STATE.md, equal to GAME_LOG_STATUS_CURRENT.md>
PREVIOUS_LOCAL_HIGHEST      = <highest card ID in the previous mini, or NONE>
FIRST_WORKING_ID            = max(REPOSITORY_NEXT_ID_SNAPSHOT, PREVIOUS_LOCAL_HIGHEST + 1)
```

- Never move backwards, never reuse an ID that appears in any mini or canonical record, and never renumber issued cards.
- Normally the previous mini has already been imported, so both numbers agree.
- If the local sequence is ahead (an earlier mini is not yet imported), continue locally and record that the import of that mini is still outstanding. The import step stops rather than renumber if the two sequences collide.
- Creating the mini consumes no ID.

## 4. Carry forward only genuinely open events

Carry forward every card that the previous settlement left as `PENDING_EVENT`: postponed, suspended or not yet terminal. Copy each into section C as a carryover block exactly as in [CARD_AND_LOG_TEMPLATES.md](../../CARD_AND_LOG_TEMPLATES.md) §2 (the original card's pick table copied byte for byte, then `DO NOT SETTLE UNTIL THE EVENT IS TERMINAL.`).

Everything else from the previous mini is closed. Do not re-carry settled records, certification gaps or aliases. Open carryover must stay at or below **5** (CURRENT_RULES §8); if the previous settlement left more, say so in the return block rather than silently carrying them.

## 5. Create the file

Path: `Mini Prediction Log - <FIRST_WORKING_ID> onward - <YYYY-MM-DD>/PREDICTION_MINI_RUNNING_LOG_<FIRST_WORKING_ID>_ONWARD.md`

Copy the structure of `EXAMPLE_ACTIVE_MINI.md` exactly, without its cards and without its "FORMAT EXAMPLE" note:

1. First line: `<!-- MINI-LOG-FORMAT: mini-log-5 -->`
2. `# Prediction Mini Running Log — <FIRST_WORKING_ID> onward`
3. `## A. Authority snapshot`: the two-column table with **every** field below, real values only: `Repository`, `Branch`, `GitHub HEAD SHA`, `Method`, `Control revision`, `Scoring version`, `Active Combined Log`, `Highest committed repository P-ID`, `Repository next-ID snapshot`, `Highest local working P-ID before creation`, `First working P-ID for this mini`, `Reading receipt` (the documents read in full, with the HEAD SHA and the time), `Mini opened` (ISO 8601 with UTC offset), `Mode` = `LOCAL_MINI_STAGING`. Then the line `SPORTS_ONLY / MARKET_BLIND · PERFORMANCE_ELIGIBILITY: NOT_CERTIFIED · CANONICAL_IMPORT_STATUS: PENDING`.
4. `## B. Local ID rules`: the five bullets from the example.
5. `## C. Active carryover`: the carryover blocks, or `None.`
6. `# NEW LOCAL EVENT CARDS`: empty. Never create a placeholder card.
7. `# RUNNING FOOTER` with the footer table between `<!-- BEGIN FOOTER -->` and `<!-- END FOOTER -->`:

| Field | Value |
|---|---|
| Highest local working P-ID actually used | `NONE` |
| Next local working P-ID | `<FIRST_WORKING_ID>` |
| Repository next-ID snapshot when mini opened | `<REPOSITORY_NEXT_ID_SNAPSHOT>` |
| Active carryovers | `<count>` |
| New event cards | `0` |
| Local mini status | `ACTIVE` |
| Canonical import | `PENDING` |
| GitHub writes performed | `NO` |

## 6. Check before returning (print each with its evidence)

- Every field is filled with a real value; search the file for `<` and `TO_FILL` and report that none is left.
- The `First working P-ID for this mini` equals the footer's `Next local working P-ID`.
- The carryover count in the footer equals the number of carryover blocks in section C; each carryover table is a verbatim copy of the original.
- The Active Combined Log named in the table equals the one in CURRENT_STATE.

## 7. Return

1. The complete mini file content.
2. Its exact path.
3. This verification block:

```text
GitHub HEAD read:
Reading receipt: <documents read in full>
Repository next-ID snapshot:
Previous highest local working P-ID:
First working ID:
Next working ID:
Active carryovers:
New cards: 0
Settlements: 0 · Retrospectives: 0 · GitHub writes: 0
```

---

*Operator note: this common core belongs to prompt 1 (the game card). It is pasted with one sport block from 1_GAME_CARD.md. Prompt 2 does not run it.*

## PART A — COMMON CORE (paste with every sport)

**Scope.** Research and write one card. Do **not** settle, grade, run a retrospective, change methodology or write to GitHub.

### A0. Reading gate (before any research)

Use only current `main` of `https://github.com/danisgreat/Sports-Research`. Print the **reading receipt** ([research/prompts/README.md](README.md)) after opening, in full:

- [CURRENT_STATE.md](../../CURRENT_STATE.md) (method, control revision, next canonical ID, active Combined Log), [METHOD.md](../../METHOD.md), [CURRENT_RULES.md](../../CURRENT_RULES.md) (Rules T2, R1, P4; reading gate §1), [SELECTION_RULES.md](../../SELECTION_RULES.md) (gate §2, top two §3, families §4, ladders §5, regimes §6, codes §7, failure classes §8), [CARD_AND_LOG_TEMPLATES.md](../../CARD_AND_LOG_TEMPLATES.md) (the `mini-log-5` card §3, the expected-score terms §3a and the card self-audit §7);
- the sport's rules file named in the sport block, and the sections of [PROBABILITY_TOOLKIT.md](../../PROBABILITY_TOOLKIT.md), [BASE_RATES_REGISTER.md](../../BASE_RATES_REGISTER.md) and [LEAGUE_PROFILES.md](../../LEAGUE_PROFILES.md) the sport block names;
- the sport's table in [SOURCES.md](../../SOURCES.md) and its reachability matrix, §1.3 (freshness), §1.4 (the firewall) and §1.5 (lineups and late news);
- [ARCHIVE_USE_GUIDE.md](../../ARCHIVE_USE_GUIDE.md);
- [GAME_LOG_STATUS_CURRENT.md](../../GAME_LOG_STATUS_CURRENT.md) (existing canonical events) and [research/prompts/examples/EXAMPLE_ACTIVE_MINI.md](examples/EXAMPLE_ACTIVE_MINI.md) (exact card structure);
- then the **active local mini** in full.

A mini that carries `<!-- MINI-LOG-FORMAT: mini-log-4 -->`, `mini-log-3` or `mini-log-2` is still valid: write the card in that mini's own format ([CARD_AND_LOG_TEMPLATES.md](../../CARD_AND_LOG_TEMPLATES.md) §1 lists the differences; legacy examples are in `research/prompts/examples/legacy_mini_log_2/` and the archived prompt examples) and tell the user that new minis use `mini-log-5`, and that only `mini-log-5` cards carry the expected score. If a document cannot be opened, say so and stop.

### A1. Identity and ID gate

1. Confirm the exact event: competition, season, stage or round, teams or players, venue, scheduled start (official source, with its time zone and update time), and the native event ID where one exists.
2. Build the event key: `<LEAGUE>:<SEASON>:<native-id or a stable surrogate>:<YYYY-MM-DD local event date>`.
3. **Duplicate check.** Search the active mini (cards and carryovers), [GAME_LOG_STATUS_CURRENT.md](../../GAME_LOG_STATUS_CURRENT.md) and the active Combined Log header for the event key and the team names. If the event already appears, do not create a card. Write a dated addendum under the existing ID instead (A8).
4. **ID.** Use the mini footer's `Next local working P-ID`. If the repository's next canonical ID in CURRENT_STATE is now **above** that number, stop and tell the user: a canonical card was written outside the mini lifecycle and must be reconciled first. Never invent, skip or reuse an ID.

### A2. Research and retained evidence

- Use official league, team and statistical sources first, then independent high-quality sources, following the route and fallback in the sport's SOURCES table. Record each source with what it supported and when it was read. When the first-choice route is unreachable, use the listed fallback and write `(fallback: <source>)` in the Evidence cell.
- Research as close to the start as practical. Lineups, starters, goalies, quarterbacks and late scratches change forecasts (SOURCES §1.5).
- **SPORTS_ONLY / MARKET_BLIND** (SOURCES §1.4). No odds, line movement, tips, betting previews, prediction markets or fantasy data in research, ranking or probabilities. Supplied lines are only contract thresholds.
- **Timing state:** `PREGAME` (state verified as not started at research completion), `LATE_START_UNVERIFIED` (scheduled start passed or state unknown), or `LIVE_OBSERVED`. If the event has started, never use observed scores, events or statistics as inputs, and say so.
- Make no unsupported claims. Mark every unverified item ("probable, not confirmed") and model the uncertainty instead of assuming the favourable case.
- **Evidence quotes (`Evidence quotes` bullet).** For each lineup, goalie, starter, injury or weather page the card relies on, record `<source> @ <ISO time you read it, with offset> — "<verbatim excerpt of up to 200 characters>"`. The quote is the audit trail; hashes no longer exist. A card whose Rank 1 rests on a lineup or goalie claim cannot be written with `NONE`.
- **Settlement fields and capture time.** Name the exact field each pick settles on and the provider that publishes it (`Final score including OT/SO (provider: <name>)`). A corners, half-time, period or player row is allowed only with `provider: <name>` and a `Capture due` time within 36 hours after the scheduled start, so the page is captured before it rots.
- **Contract definitions.** Fill `Retirement rule`, `Listed-pitcher rule` and `Abandonment rule` with `N/A`, `FRAMEWORK_DEFAULT: <rule>` or `OPERATOR: <name>: <rule>`. Never guess a definition the operator has not supplied.
- **Regime flags.** Set `Regime flags` from the regime table in BASE_RATES_REGISTER (SELECTION_RULES §6). Apply the table's `Recommended` multiplier only; where it reads 1.000, do not shift the distribution.
- **Expected score (CARD_AND_LOG_TEMPLATES §3a).** Compute the mean of each scoring term that your sport block lists, from the distribution's parameters, before the result is known. Give the endpoint, each team's mean and SD, the total with its SD, and the margin with its SD. Show the arithmetic in A4 (for example the OT or shootout share and how each SD is obtained). Never take a number from a price, a line, a preview or outside the card.

### A3. The archive check (past results)

Open the files the sport block names under `Previous Sports Results/` and the league's row in [LEAGUE_PROFILES.md](../../LEAGUE_PROFILES.md), and do the recipes in [ARCHIVE_USE_GUIDE.md](../../ARCHIVE_USE_GUIDE.md) §4 that bear on this event: league level (R1), both teams' form before the date (R2), line frequency for the lines you will price (R5), rest (R6), venue and home edge (R7), extras and tails (R8). Use only rows dated before your research time (§3 there). Print the numbers in appendix A3 and A4 and fill the `Archive check` bullet. If the files are header-only or missing, write `ARCHIVE_UNAVAILABLE: <exact reason>` and use the fallback the guide names. The archive never replaces confirmed lineups, starters, goalies and weather.

### A4. Build one event distribution (probabilities are mandatory)

- Build **one** joint distribution of the sporting outcome for the stated endpoint, using the sport block's method and the tables in PROBABILITY_TOOLKIT. Name it in `Distribution object` as `<family>_<method>_v<n>` followed by its parameters (for example `hockey_poisson_ot_v1 — λ 3.10 / 2.70, OT home 52%`). Every probability in the pick table is read from that grid, and each row's `Probability status` reads `FROM_DISTRIBUTION:<that id>`.
- No fitted model exists. Set `Analysis status` to `UNCALIBRATED_ANALYST_SCENARIO`. It is still mandatory and must be explicit, reproducible and honest about uncertainty. Never call it validated.
- Resolve the contract endpoint inside the distribution: regulation versus OT, shootout, extra innings or extra time, ties, retirement and abandonment conventions. A full-game row must not leave a draw unresolved.
- **Adjustments are parameters, not nudges.** Any analyst change to a distribution input is listed in the adjustments table of the appendix (name, target, size, size in SD units, basis `fitted | archive_estimate | analyst_judgement`). If an adjustment above 0.25 SD changes which two propositions are Rank 1 and Rank 2, print `**Unadjusted top two:** <rank 1>; <rank 2>` and label the card `ADJUSTMENT_DEPENDENT`. Otherwise label it `NONE`.
- Run at least one sensitivity case on the most uncertain input (goalie, starter, pace, lineup) and report how the top two move.
- Show the arithmetic: the inputs, the formula or table section used, and the grid or the key cells, so a reader can reproduce each priced line.

### A5. Candidates and the top two (Rule P4, SELECTION_RULES §2 to §5)

1. Price every **supplied** contract from the distribution. Supplied contracts are reference only: use one only if it is among the best-suited or most likely once ranked.
2. Price the strongest **analyst-derived** propositions from the same distribution: winner or double chance, handicap or spread, match total, team total and period total, on the sport's standard ladder (SELECTION_RULES §5). Exclude degenerate rows above **90%**. `p_card` is win ÷ (win + loss); a push leaves the denominator.
3. Choose **exactly four candidates** and **rank them by `p_card`**, highest first. Never rank by q, edge or narrative.
4. **Rank 1 and Rank 2 are the picks** (only they can count as wins, Rule T2). Ranks 3 and 4 are informational.
5. **Rank-1 gate.** Rank 1 passes when `p_card` is at least **62%** and it leads the best non-complementary alternative (not the opposite side of the same line) by at least **4 points**. Print `**Rank-1 gate:** PASS` or `RANK1_UNSTABLE` with the numbers, recomputed. A failing gate is not an error: the card is scored in its own cohort, and you say why no stronger proposition exists.
6. **Rank 2** is the remaining row with `p_card` of at least **58%** that minimises P(Rank 1 and Rank 2 both lose), computed from the joint grid by the case in SELECTION_RULES §3 (never assumed independent). Print that probability. If it exceeds **35%** the two picks share one driver: replace the weaker pick with the best less-correlated candidate, re-rank by `p_card`, and say what changed. Rows from different outcome spaces have no exact joint: use the conservative bound min(P(lose 1), P(lose 2)) and say so.
7. Apply the sport block's **family checks** and the family rules in SELECTION_RULES §4, and record the result of each in appendix A7.

### A6. Write the card in exact `mini-log-5` form

The card has two parts. The **decision block** is the page you would act on (about 650 words at most): the distribution line, the pick table, the six bold lines. Everything else goes in the **appendix**. Insert the card **immediately before `# RUNNING FOOTER`**. The master template is [CARD_AND_LOG_TEMPLATES.md](../../CARD_AND_LOG_TEMPLATES.md) §3; this copy is for pasting, and the template page controls if they differ.

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
- **Distribution object:** `<id> — <parameters, one line>`
- **Expected score:** `<unit>, <endpoint>; SDs on <basis> — <Team A> <x.x> (SD <x.x>) · <Team B> <x.x> (SD <x.x>) · total <x.x> (SD <x.x>) · margin <Team A − Team B> <±x.x> (SD <x.x>)`
- **Regime flags:** `NONE` or a comma-separated list
- **Retirement rule:** `N/A | FRAMEWORK_DEFAULT: … | OPERATOR: <name>: …`
- **Listed-pitcher rule:** `N/A | FRAMEWORK_DEFAULT: … | OPERATOR: <name>: …`
- **Abandonment rule:** `N/A | FRAMEWORK_DEFAULT: … | OPERATOR: <name>: …`
- **Settlement fields:** `<field> (provider: <name>)`
- **Capture due:** `<ISO 8601 with offset, after the start and within 36 h of it>`
- **Rules read:** `<documents and sections applied, e.g. RULES_BASEBALL §3 §8; SELECTION_RULES §2-§4; SOURCES §3.1; BASE_RATES §5>`
- **Archive check:** `<file(s) · rows read · date range · recipes · finding>` or `ARCHIVE_PARTIAL: …` or `ARCHIVE_UNAVAILABLE: <exact reason>`
- **Evidence quotes:** `<source> @ <ISO time> — "<verbatim excerpt>"; …` or `NONE`

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

Format rules checked in the self-audit:

- Keep the pick-table header exactly as shown, with **four** data rows, roles `PICK, PICK, INFORMATIONAL, INFORMATIONAL`, every `p_card` a percentage, non-increasing order, no `q` column, and no `TO_FILL` placeholder in any cell.
- The pick table sits inside the decision block, which ends at `### Appendix`.
- No heading inside the card may start with a P-ID (`## P-…`), because the import step would read it as a new card.
- The bold lines are spelled exactly as shown. The gate's state must agree with the numbers it states.
- The `Expected score` bullet sits directly after `Distribution object`, uses the unit of the sport block below, and every term is numeric. The total mean is the centre the total rows were priced from.

### A7. Update the footer and audit

Replace the footer table: `Highest local working P-ID actually used` = this card's ID; `Next local working P-ID` = this ID + 1; `New event cards` + 1. Leave every earlier byte of the mini unchanged.

Then run the **card self-audit C1 to C21** ([CARD_AND_LOG_TEMPLATES.md](../../CARD_AND_LOG_TEMPLATES.md) §7) and print the table `| Check | Result | Evidence |`, with the number, quote or search result for each check. Fix every failure before returning. If you cannot edit the mini document in place, return the complete updated mini.

### A8. Corrections, late news and re-forecasts (no new ID)

To correct a non-substantive error, or to record material news before the start, append after the card (before the footer):

```markdown
<!-- BEGIN ADDENDUM P-NNN -->
### Addendum · P-NNN · <ISO 8601 time with offset>
<what changed, why, and whether the original ranking would change; the original card stays unchanged and is what gets graded>
<!-- END ADDENDUM P-NNN -->
```

- Place it after the card it amends and immediately before `# RUNNING FOOTER`. Leave the footer unchanged.
- The ID is the amended card's own ID. For a canonical event outside this mini (found in the duplicate check), use its canonical ID. The import step attaches the addendum to that card, or stops if none exists.
- The time must be ISO 8601 with a UTC offset. The body must not contain a new pick table or a heading that starts with a P-ID.
- An addendum never consumes an ID and never edits the original card. Settlement grades the original card only.
- **Re-forecast trigger.** A confirmed starter, goalie or quarterback change (or a lineup change large enough to move the ranks) that becomes public after your research time and before the start makes the card's ranks stale. A change qualifies when it moves a distribution input by more than 0.25 SD or reorders the top two. Write an addendum with the trigger, its source and time, and a re-priced table headed `| Rank | Proposition | p_reforecast |` (deliberately not the pick-table header). The original card is still what is graded.

### A9. Return

The complete card, the updated footer, the self-audit table, and:

```text
READING RECEIPT: <as printed in A0>
Working ID: P-NNN (LOCAL_WORKING_ID — PENDING_CANONICAL_IMPORT)
Repository next-ID snapshot read:
Duplicate check: none found / existing ID P-…
Timing state:
Distribution object:
Rank 1 / Rank 2 (p_card):
Rank-1 gate: PASS / RANK1_UNSTABLE
P(both picks lose):
Adjustment dependence: NONE / ADJUSTMENT_DEPENDENT
Potential winner:
Settlement fields and capture due:
Archive check: <files · rows · finding> / ARCHIVE_UNAVAILABLE: <reason>
Evidence quotes: <n> recorded / NONE
Expected score: <unit> · <Team A> <x.x> (SD <x.x>) · <Team B> <x.x> (SD <x.x>) · total <x.x> (SD <x.x>) · margin <±x.x> (SD <x.x>)
Self-audit C1-C21: all PASS / failures fixed: <list>
Settlement: NOT_PERFORMED · GitHub writes: NO
```

---

