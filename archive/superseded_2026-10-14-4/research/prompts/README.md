# Operator prompts 1–8

**P-2026.10.14-v11.1 · Markdown/CSV/text only** (v11.1, PROCEDURE: prompts 1–3 never read `research/model_shadow/` or `ml/` before their own freeze; prompt 8 may change `ml/` under CURRENT_RULES §0). Revision class: FORMAT + PROCEDURE (mini-log-7 / mini-settlement-6, authority mode, form windows, mixture pricing, lifecycle and custody controls; CURRENT_RULES §11 explains the classes). Previous suite: [P-2026.10.11-v10](../../archive/superseded_2026-10-12/research/prompts/README.md). Use each complete task below; prompt 1 now contains its own common core and sport instructions. [Current rules](../../CURRENT_RULES.md) and [templates](../../CARD_AND_LOG_TEMPLATES.md) are required companions. No real ID, log part, league fact or retrospective figure is hard-coded in these prompts: they cover any sport and competition, and league-specific facts come from the rules files, [league profiles](../../LEAGUE_PROFILES.md), [SOURCES](../../SOURCES.md) and the archive.

| # | Task | Writes |
|---|---|---|
| [1](1_GAME_CARD.md) | One individual game card | Active local mini and its permitted evidence appendix |
| [2](2_START_LOCAL_MINI.md) | Start local mini | New mini only |
| [3](3_SETTLE_LOCAL_MINI.md) | Freeze, settle, retrospect | New local settlement package |
| [4](4_CANONICAL_IMPORT.md) | Canonical import | Active log suffix, status/state/scoreboard, new import report |
| [5](5_START_THE_NEXT_COMBINED_LOG.md) | Rollover | Old log closure, new part, current pointers, changelog/report |
| [6](6_COMBINED_LOG_RETROSPECTIVE.md) | Cohort review | New report, scoreboard/state, dated hypotheses/changelog |
| [7](7_EXPAND_PREVIOUS_RESULTS.md) | Archive repair | Declared CSV/source/coverage/profile paths |
| [8](8_IMPROVE_THE_FRAMEWORK.md) | Framework improvement | Declared operating documents, archive copies, examples/report |

Order: **2 → 1 for each event → 3 → 4**, then next mini; 5–8 as needed. Prompts 1–3 refer to the GitHub repository (`main` branch) in read-only mode and never publish or edit canonical logs. Prompts 4–8 publish only when the invocation authorizes it; their Publish steps are explicit instructions when the complete prompt is invoked. A review-only or local-only user request overrides publication.

## Reading receipt

**Exclusion (CR-2026.10.14-R1).** Prompts 1–3 do not open, search or cite `research/model_shadow/` or `ml/` before their own card is frozen; a receipt that lists either is invalid for a card.

Before dependent work, open actual files and print:

```text
READING RECEIPT
Authority mode: PUBLISHED_MAIN_PINNED <full SHA> OR LOCAL_WORKING_TREE <branch/HEAD>
Repository / branch / HEAD / read time with timezone:
Relevant working differences (control files that differ between published and local, and which version this run applied):
Read in full: <actual files>
Sections read: <actual paths/sections>
Current method / control / scoring / selection / formats:
Task scope / allowed writes / publication instruction:
Sport/source/archive inputs read: <actual paths and coverage, or task N/A>
Required unavailable files / contradictions / dependent steps blocked:
```

**One mode per run (CURRENT_RULES §0).**
- Prompts 1–3 and every agent outside the repository use `PUBLISHED_MAIN_PINNED`: all controls come from one printed commit of `origin/main`.
- Prompts 4–8, and a local run whose user asks for local controls, use `LOCAL_WORKING_TREE`: print HEAD and every uncommitted control difference, and say which version governed.

Do not pretend dirty working files equal HEAD, and never mix revisions inside one run. Read archived issued cards under their original versions. An opening log header is historical; derive current allocation from state/status and canonical entries, including latest dated addenda. Stop allocation on genuine current disagreement, not merely an old opening snapshot.

Common requirements: no fabricated data or execution claims; explicit missingness; market blindness; frozen original cards; append-only corrections; one event/one permanent ID; unresolved evidence retained; full write/readback. If files cannot be written, return READ_ONLY_DRAFT / NOT_ISSUED complete artifacts and make no claim that IDs advanced or a mini changed.

## Release and compatibility

New minis use mini-log-7 and settlement mini-settlement-6. Existing mini-log-2 through -6 and settlement -2 through -5 stay in their original formats. New process checks expose gaps through dated addenda; they never insert absent pregame values. Historical rank/p/contract/timestamp bytes and grades remain unchanged. Implementation maps [2026-10-12-1](../verification/framework_change_2026-10-12-1/IMPLEMENTATION.md) (current) and [2026-10-11-1](../verification/framework_change_2026-10-11-1/IMPLEMENTATION.md) distinguish current controls from untested experiments and pending data work.
