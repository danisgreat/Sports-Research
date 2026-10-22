# Operator prompts 1–8

**Local keys until settlement; updated mini after every game (MINI-v2).** Defined in [MINI_LOG_IDENTITY_PROTOCOL](../../MINI_LOG_IDENTITY_PROTOCOL.md); summarised in [CORE](../../CORE.md) §2.

**Persistent research and corroboration (EXH-v1).** Defined in [RESEARCH_EXHAUSTIVENESS_PROTOCOL](../../RESEARCH_EXHAUSTIVENESS_PROTOCOL.md); summarised in [CORE](../../CORE.md) §5.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** Defined in [HISTORICAL_SOURCE_PROTOCOL](../../HISTORICAL_SOURCE_PROTOCOL.md); summarised in [CORE](../../CORE.md) §5.

**Required repository fallback (REF-v1).** Defined in [GITHUB_REFERENCE_PROTOCOL](../../GITHUB_REFERENCE_PROTOCOL.md); summarised in [CORE](../../CORE.md) §1.

**Historical v11.3 PROCEDURE release:** all eight prompts use [COMMON_OPERATING_PROTOCOL](COMMON_OPERATING_PROTOCOL.md). Prompt 1 has eleven separate sport/general sections, each with its own Upcoming game input block; rugby league and union are independent. The workflow preserves manual-card independence, availability research, qualified shadow evidence, source admission and verified publication. Earlier v11.1/v11.2 controls remain in force unless explicitly superseded.

The root supplied-first extended prompt is a preserved proposal, not an active replacement for P4. Use the numbered suite below.

**Historical v11.2 PROCEDURE update:** prompt 1 applies [ROSTER_AVAILABILITY_PROTOCOL](../../ROSTER_AVAILABILITY_PROTOCOL.md) to both sides and every applicable starter/bench/absence field, including local-language discovery and a final late-change check. Evidence stays in existing card fields/A3/A8/C20; mini-log-7 and earlier issued records retain their formats. The v11.1 workshop reading exclusion remains in force.

**P-2026.10.22-v24.0 · Markdown/CSV/text controls** (all prompts run in this repository under ENV-v2; prompt 1 freezes the declared reference, prices the card from it and freezes the card's final p, prompt 3 settles them, prompt 6 scores the ledger and prompt 8 owns references and releases under MLSCOPE-v3; the decision lab stays excluded from cards; prompt 8 may change ml/ under CURRENT_RULES §0). Previous v17.1 revision class: PROCEDURE + DATA RETIREMENT (mandatory online history and confirmed-player research; no format change). Prior RETAIN-v1 revision class: FORMAT + PROCEDURE (mini-log-9 / mini-settlement-8, model-independent research retention and honest C21/S16 dispositions; old EXEC-v1 execution prerequisite superseded). Original v11.0 revision class: FORMAT + PROCEDURE (mini-log-7 / mini-settlement-6, authority mode, form windows, mixture pricing, lifecycle and custody controls; CURRENT_RULES §11 explains the classes). Previous suite: [P-2026.10.11-v10](../../archive/superseded_2026-10-12/research/prompts/README.md). Use each complete task below; prompt 1 now contains its own common core and sport instructions. [Current rules](../../CURRENT_RULES.md) and [templates](../../CARD_AND_LOG_TEMPLATES.md) are required companions. No real ID, log part, league fact or retrospective figure is hard-coded in these prompts: they cover any sport and competition, and league-specific facts come from the rules files, [league profiles](../../LEAGUE_PROFILES.md), [SOURCES](../../SOURCES.md) and independently verified online history.

**ML/RL scope (MLSCOPE-v3).** Defined in [FORECAST_CYCLE_PROTOCOL](../../FORECAST_CYCLE_PROTOCOL.md); summarised in [CORE](../../CORE.md) §7.

**Execution environment (ENV-v2).** Defined in [EXECUTION_ENVIRONMENT_PROTOCOL](../../EXECUTION_ENVIRONMENT_PROTOCOL.md); summarised in [CORE](../../CORE.md) §1.

| # | Task | Writes |
|---|---|---|
| [1](1_GAME_CARD.md) + [sport file](1_sports/) | One individual game card (core plus one sport file) | Card, intake row and footer in the active mini; pregame model-shadow receipt and frozen rows; commit and push |
| [2](2_START_LOCAL_MINI.md) | Start local mini | One new mini in `research/active_minis/` and the active-mini pointer; commit and push |
| [3](3_SETTLE_LOCAL_MINI.md) | Freeze, settle, retrospect, then import | Settlement document, model-shadow settlements, then the prompt-4 import (canonical IDs assigned in this settlement phase); commit and push |
| [4](4_CANONICAL_IMPORT.md) | Canonical import (run by prompt 3, or alone on supplied packages) | Assign canonical P-IDs, active log suffix, mapping, status/state/scoreboard, new import report |
| [5](5_START_THE_NEXT_COMBINED_LOG.md) | Rollover | Old log closure, new part, current pointers, changelog/report |
| [6](6_COMBINED_LOG_RETROSPECTIVE.md) | Cohort review | New report, scoreboard/state, dated hypotheses/changelog |
| [7](7_EXPAND_PREVIOUS_RESULTS.md) | Scoped online-history rebuild | Declared CSV/source/coverage/profile paths |
| [8](8_IMPROVE_THE_FRAMEWORK.md) | Framework improvement | Declared operating documents, archive copies, examples/report |

Order: **2 → 1 for each event → 3 (which runs 4)**, then next mini; 5–8 as needed. Every prompt runs in this repository as the repository agent with internet access (ENV-v2) and ends with a commit and push of the paths it changed. Prompt 4 can still take in owner-supplied material produced elsewhere, including legacy external-chat output. A review-only or local-only user request overrides publication.

## Completion-based research timing

[TIMING-2026.10.15-v1](../../TIMING_RESEARCH_PROTOCOL.md) removes fixed manual research/freeze lead targets. Every sport continues until comprehensive research is complete, including after start. Independently evidenced CLEAN_PRE_START_INPUTS and actual POST_START_ISSUE are separate labels and a separate research score cohort; clean pre-start-issued prospective/model criteria are not backdated or relaxed. v12.0 is a STATISTICAL/measurement-policy + PROCEDURE release; score formulas, selection and mini formats unchanged. Earlier v11 release paragraphs above are historical.

## Primary ML/RL lane

Under MLSCOPE-v3 (v24.0) the declared reference is frozen before each card and the forecast cycle freezes the card's own p after it, on competitions with an active release; [the primary lane](../../PRIMARY_PREDICTION_PROTOCOL.md) stays a workshop model. Prompt 1 cards are ANALYST_PRIMARY_V1: the frozen reference plus logged adjustments. Old DATA_HOLD/shadow forecasts and the market decision lab remain excluded from cards.

## Reading receipt

**External-chat game requests (REQ-v2):** paste-ready prompt-1 requests per sport for a research chat outside the repository are in [external_requests/](external_requests/README.md); the repository agent takes their CARD_DELTA in, lints, ledgers and freezes it.

**Current model gate (MLSCOPE-v3):** prompt 1 reads model output only through the reference stage it runs before the card and, after the card is written and read back, the freeze block; the freeze never changes the card and the reference is never edited. Prompts 3, 6 and 8 settle, evaluate and release models. The market decision lab stays excluded from cards.

Before dependent work, open actual files and print:

```text
READING RECEIPT
Environment: REPOSITORY_AGENT (all prompts, ENV-v2)
Authority mode: LOCAL_WORKING_TREE <branch/HEAD> (PUBLISHED_MAIN_PINNED only for an agent outside the repository)
Repository / branch / HEAD / read time with timezone:
Relevant working differences (control files that differ between published and local, and which version this run applied):
Read in full: <actual files>
Sections read: <actual paths/sections>
Current method / control / scoring / selection / formats:
Task scope / allowed writes / publication instruction:
Sport/source/archive inputs read: <actual paths and coverage, or task N/A>
Required unavailable files / contradictions / dependent steps blocked (include local read failures and exact GitHub fallback URL/path/SHA/read time/result):
```

**One mode per run (CURRENT_RULES §0).**
- Every prompt run in this repository uses `LOCAL_WORKING_TREE` (ENV-v2): print HEAD and every uncommitted control difference, and say which version governed.
- An agent outside the repository (legacy ENV-v1 route) uses `PUBLISHED_MAIN_PINNED`: all controls come from one printed commit of `origin/main`.

Do not pretend dirty working files equal HEAD, and never mix revisions inside one run. Read archived issued cards under their original versions. An opening log header is historical; derive current allocation from state/status and canonical entries, including latest dated addenda. Stop allocation on genuine current disagreement, not merely an old opening snapshot.

Common requirements: no fabricated data or execution claims; explicit missingness; market blindness; frozen original cards; append-only corrections; one event/one stable local key and one mapped canonical ID after import; unresolved evidence retained; full write/readback. If files cannot be written, return READ_ONLY_DRAFT / NOT_ISSUED complete artifacts and make no claim that IDs advanced or a mini changed.

## Release and compatibility

New minis use mini-log-10 and settlement mini-settlement-10. Existing mini-log-2 through -9 and settlement -2 through -9 stay in their original formats. New local-key research cards appended to an older active mini retain their own manifest/attempt fields; earlier cores are not migrated. New process checks expose gaps through dated addenda; they never insert absent pregame values. Historical rank/p/contract/timestamp bytes and grades remain unchanged. Implementation maps [2026-10-12-1](../verification/framework_change_2026-10-12-1/IMPLEMENTATION.md) (current) and [2026-10-11-1](../verification/framework_change_2026-10-11-1/IMPLEMENTATION.md) distinguish current controls from untested experiments and pending data work.

**Current V3 review:** [review](../verification/framework_change_2026-10-15-4/REVIEW.md), [protocol](../../PRIMARY_PREDICTION_PROTOCOL.md). Numbered task text is now directly aligned with mixture/ledger/η fields. Previous companion reinterpretations of bandit/propensity wording are historical. A learning algorithm and a passing test suite do not prove predictive improvement.

**All-sport historical source recovery:** [HISTORICAL_SOURCE_PROTOCOL](../../HISTORICAL_SOURCE_PROTOCOL.md) makes verified online research the first recovery for missing, incomplete or incorrect local history. All eleven game sections apply it directly; prompt7 handles separate permanent archive repairs.

**Strict research completion:** [RESEARCH_COMPLETION_PROTOCOL](../../RESEARCH_COMPLETION_PROTOCOL.md) requires full research, all applicable sport procedures and every requested contract assessment irrespective of model calibration/runtime, data/lineup gaps, kickoff or mini/write blockers. Supported automatic analyst comparisons stay NOT_PRIMARY; missing numerical ML never means stop research. The A9 evidence matrix is mandatory.

**Research retention (RETAIN-v3).** Retain every identified researched event under its stable local event key. Prompts 1–3 neither assign nor reserve canonical P-IDs. Prompt 1 returns the full research card with its hand-derived probabilities, intake row and footer (and the full mini when it fits, ENV-v1) after every game request. Prompt 4 alone reconciles duplicates and assigns canonical P-IDs at import, preserving local originals and a local-to-canonical map. Verified outcomes become learning candidates in prompt 6. Identity/custody/write conflicts remain real blockers. See RESEARCH_RETENTION_PROTOCOL and MINI_LOG_IDENTITY_PROTOCOL.

**Local research record and updated-document delivery (owner update, 16 October 2026).** Defined in [MINI_LOG_IDENTITY_PROTOCOL](../../MINI_LOG_IDENTITY_PROTOCOL.md); summarised in [CORE](../../CORE.md) §2.

## Legacy records and populated prompt inputs

v19.0 retains EXH-v1 all-field sourcing, independent corroboration and information-closure controls for new research. Settlement/import retains older originals under their own actual policies and explicit evidence limits, without backfilled compliance or model promotion. Prompt 1 may contain owner-entered game details; an instruction-only alignment preserves every Upcoming block exactly through the first Read paragraph.

## Persistent sourcing and information closure (EXH-v1)

Release P-2026.10.16-v19.0 was FORMAT + PROCEDURE: persistent all-field research/corroboration under EXH-v1 and a new mini-settlement-10 source-discovery/reuse section with three CSV sidecars and S17. Mini-log-10 adds local event keys and cumulative .md delivery after each request; prompt 4 alone assigns canonical IDs. Scoring11/selection3 are unchanged. Existing settlement-9/earlier packages retain their original formats. Use RESEARCH_SOURCE_REGISTER plus prior package registers, open the actual routes, and record fields/attempts/limits; open requirements prevent information completion. The filled Upcoming game blocks remain unchanged.

## Current local identity and delivery example

Use [MINI_LOG_IDENTITY_PROTOCOL](../../MINI_LOG_IDENTITY_PROTOCOL.md) and the [synthetic two-request cumulative-document example](examples/EXAMPLE_LOCAL_MINI_DELIVERY_10.md). Canonical assignment occurs only in prompt 4; every prompt-1 request returns the complete updated mini .md. C22/S18 are additional to the existing research/source checks. Historical format-9 examples retain their original scope.

## Learning pipeline (LEARN-v1, P-2026.10.16-v19.1)

Release P-2026.10.16-v19.1 was PROCEDURE: prompt 1 adds the structured research export (each sport workflow, before the mandatory output paragraph); prompt 3 adds learning accounting and mini-level diagnostics; prompt 4 adds the training-data handoff into the learning store; prompt 6 adds evidence-aware interim (about 100) and comprehensive (about 300) review levels with per-sport and per-competition clocks and recorded dispositions; prompt 8 adds the data → release → chronological study → prospective shadow → owner decision → registry gates. Card, mini and settlement formats, selection, scoring and the primary model are unchanged. Every owner-entered Upcoming game block in prompt 1 is byte-identical. Which controls each prompt reads: [DEPENDENCY_MAP](DEPENDENCY_MAP.md), checked by `ml/tests/test_prompt_consistency.py`. Details: [LEARNING_PIPELINE_PROTOCOL](../../LEARNING_PIPELINE_PROTOCOL.md).

## Runtime receipt, baseline and definitions (current P-2026.10.16-v19.2)

Current release P-2026.10.16-v19.2 is PROCEDURE, following the full-history retrospective. Every prompt-1 sport workflow adds one identical **Runtime, baseline and contract definitions** paragraph (capability receipt and bootstrap before any ML_NOT_RUN, a standalone same-line `python -m ml baseline` comparator, and a unit/period/action definition gate); the tennis workflow adds the TENNIS_EXPERIMENTAL_HEDGE_V1 prospective shadow freeze; prompt 6 builds its tables with `python -m ml card-history`. Card, mini and settlement formats, selection, scoring and the primary model are unchanged; every owner-entered Upcoming game block is byte-identical.

## P-2026.10.16-v20.0 — executable forecast cycle

All sports now route through actual attempt/bundle verification under [FORECAST_CYCLE_PROTOCOL](../../FORECAST_CYCLE_PROTOCOL.md). Contextual final-score models, source-addressed identity repair, online verified backfill, settlement feedback and frozen baseline-paired evaluation are connected; qualification still requires future evidence. Owner-entered game blocks and prompt-4-only canonical allocation are preserved.

## P-2026.10.17-v20.1 — browser-chat execution (CHAT-EXEC-v1)

A web chat's read-only GitHub connector cannot run `ml`. Prompt 1 now tells a chat with a Python sandbox to use the owner's runtime pack (`python -m ml.chat pack`), run `python -m ml.chat run` from two small CSVs and a source capture, copy the verified `p_card`/`baseline_p` unchanged and return the upload zip; the owner then runs `python -m ml.chat accept` and commits before the start. Refusals keep rows RESEARCH_ONLY_NO_MODEL. Details: [FORECAST_CYCLE_PROTOCOL](../../FORECAST_CYCLE_PROTOCOL.md). Owner-entered game blocks and prompt-4-only canonical allocation are preserved.

## P-2026.10.17-v20.2 — Google Drive exchange (DRIVE-v1)

Prompts 1 and 2 may use the owner's Google Drive folder under [GOOGLE_DRIVE_EXCHANGE_PROTOCOL](../../GOOGLE_DRIVE_EXCHANGE_PROTOCOL.md). Controls still come from the pinned GitHub commit; a Drive mirror copy counts only when `DRIVE_SYNC_RECEIPT.md` lists it as current. A chat that cannot write the repository uploads the complete updated mini (and, in prompt 1, the RESEARCH_EXPORT CSVs and any CHAT-EXEC upload zip) to `uploads/<date>/<key>_<tool>/` with an `UPLOAD_MANIFEST.md`, and still returns the complete mini in its reply. An upload is not publication; the owner imports it through the normal gates. v21.0 withdrew the Drive mirror requirement (DRIVE-v2: optional drop box only). Owner-entered game blocks are unchanged.

## P-2026.10.17-v21.0 — no-code game research (MLSCOPE-v1 / NOCODE-v1)

STATISTICAL + PROCEDURE. ML/RL leaves game research. Prompt 1 runs no code in any chat: it researches the event and derives every p_card by hand from one coherent distribution (ANALYST_PRIMARY_V1) with [PROBABILITY_TOOLKIT](../../PROBABILITY_TOOLKIT.md) arithmetic shown step by step, records its learning rows as Markdown tables and computes the league-only BASELINE_P by hand. Prompts 1 and 2 read the latest `main` branch on GitHub. Prompts 2–5 drop the execution manifest, runtime, feedback and learning-store commands. Prompt 6 gains the ML/RL review (ingest, feedback, shadows, comparisons) and prompt 8 owns workshop changes; their findings reach cards only as Markdown changes. Google Drive is an optional drop box with no push or mirror requirement (DRIVE-v2). Owner-entered game blocks are unchanged.

## P-2026.10.17-v22.0 — execution environments (ENV-v1)

FORMAT + PROCEDURE. Prompts 1–3 run in an external chat with internet access and read-only GitHub at the latest `main` commit, with a section-level reading budget, no code, no writes and no hashes. Prompt 1 returns the new card, intake row and replacement footer (the full mini only when it fits without truncation); prompt 2 returns the new mini; prompt 3 returns a settlement document that names the frozen mini instead of reproducing it. Prompts 4–8 run in this repository; prompt 4 gains an intake step that assembles card deltas, computes byte counts and SHA-256, checks structure and joins settlements. Details: [EXECUTION_ENVIRONMENT_PROTOCOL](../../EXECUTION_ENVIRONMENT_PROTOCOL.md). Owner-entered game blocks are unchanged.

## P-2026.10.17-v22.1 — prompt 1 core and sport files

PROCEDURE. Prompt 1 is split into a core file (`1_GAME_CARD.md`: shared rules, no code, external chat, latest `main`, delivery) and eleven sport files in `1_sports/`, each holding that sport's complete seven-step workflow and its own Upcoming game block, moved byte-for-byte (only relative links changed for the new folder). An external chat reads the core and one sport file. Requirements, outputs and probabilities are unchanged.

## P-2026.10.17-v22.2 — shared sport rules moved into the prompt 1 core

PROCEDURE. The 19 paragraphs that were identical in all eleven sport files now appear once, in the prompt 1 core under **Shared steps for every sport**. Each sport file keeps its step headings, its own instructions and its Upcoming game block, and each affected step points to the core. The wording of every moved paragraph is unchanged except one cross-reference (the analyst method now points to the sport file's step-4 distribution family). Requirements, outputs and probabilities are unchanged.

## P-2026.10.22-v23.0 (superseded by v24.0) — everything runs here; model shadow after the card (ENV-v2 / MLSCOPE-v2 / MINI-v2)

STATISTICAL + PROCEDURE, owner instruction 22 October 2026. All eight prompts run in this repository with internet access; the external-chat route is retired for new work. Prompt 1 still prices every card itself (ANALYST_PRIMARY_V1; code may do the arithmetic) and reads no model output before the card is written; then it runs `python -m ml pregame run`, which freezes the model, the league baseline and the card's own p_card on identical contracts, or records why it could not run. Prompt 3 settles the card, then the shadow (`cycle settle`), then runs the prompt-4 import, so canonical IDs are assigned only in the settlement phase. A model is judged only after 8 weeks and 50 paired games; a progress review is due at whichever comes first. Releases now freeze only the forecast cycle's import closure. Details: [EXECUTION_ENVIRONMENT_PROTOCOL](../../EXECUTION_ENVIRONMENT_PROTOCOL.md), [FORECAST_CYCLE_PROTOCOL](../../FORECAST_CYCLE_PROTOCOL.md) and the [implementation](../verification/framework_change_2026-10-22-1/IMPLEMENTATION.md).

## P-2026.10.22-v24.0 — reference-first cards, ledger, linted picks, tiers, league lane (REFMODEL-v1 / LEDGER-v1 / PICKS-v2 / MLSCOPE-v3 / STATFREEZE-v1)

Owner instruction, 22 October 2026, implementing the [framework revamp review](../verification/review_2026-10-22_framework_revamp/REPORT.md) ([implementation](../verification/framework_change_2026-10-22-2/IMPLEMENTATION.md)). STATISTICAL + FORMAT + PROCEDURE, so the prompt major version moves. What changes for the operator:

- **Prompt 1** reads [CORE](../../CORE.md) (about 16 KB) instead of the old reading list. It prints the tier, freezes the reference **before** typing a probability, builds p_card as reference plus ledger adjustments, writes a linted `PICKS_V2` block, freezes the card's final p beside the reference and ledgers the rows. Late requests get a fast card first.
- **Prompt 3** also writes RESULTS.csv and ACTUALS.csv for the ledger and settles league-day events; benchmarks only if the owner supplies them.
- **Prompt 6** adds ledger scoring, width coverage, external comparators and a monthly dashboard.
- **Prompt 7** builds the data the reference lane runs on: two-lineage finals, line-up snapshots, parameter rows, effect-table rows.
- **Prompt 8** owns reference choices and statistical changes, applies the season freeze and runs the release gate first.
- Prompts 2, 4 and 5 are unchanged in behaviour; prompt 4 carries the picks block and ledger pointers.
- The statistical rules that cards before v24.0 followed stay as written for those cards.
