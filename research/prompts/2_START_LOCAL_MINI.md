# PROMPT 2 — START A NEW LOCAL MINI RUNNING LOG

**Run by:** external chat agent · **GitHub:** read only · **Output:** one new local Markdown file · **Mode:** `LOCAL_MINI_STAGING` · **Format:** `mini-log-4`

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

1. First line: `<!-- MINI-LOG-FORMAT: mini-log-4 -->`
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
