# Prompt-suite release notes v19.1–v23.0 formerly in research/prompts/README.md

Moved verbatim from `research/prompts/README.md` on 2026-11-08 (CR-2026.11.08-R2) so that the live page holds only current instructions. Dated history; not current authority (precedence: RULES_REFERENCE Part A §0, PREC-v1).

## Learning pipeline (LEARN-v1, P-2026.10.16-v19.1)

Release P-2026.10.16-v19.1 was PROCEDURE: prompt 1 adds the structured research export (each sport workflow, before the mandatory output paragraph); prompt 3 adds learning accounting and mini-level diagnostics; prompt 4 adds the training-data handoff into the learning store; prompt 6 adds evidence-aware interim (about 100) and comprehensive (about 300) review levels with per-sport and per-competition clocks and recorded dispositions; prompt 8 adds the data → release → chronological study → prospective shadow → owner decision → registry gates. Card, mini and settlement formats, selection, scoring and the primary model are unchanged. Every owner-entered Upcoming game block in prompt 1 is byte-identical. Which controls each prompt reads: [DEPENDENCY_MAP](../prompts/DEPENDENCY_MAP.md), checked by `ml/tests/test_prompt_consistency.py`. Details: [LEARNING_PIPELINE_PROTOCOL](../../ML_PIPELINE.md#part-c-learning_pipeline_protocol).

## Runtime receipt, baseline and definitions (current P-2026.10.16-v19.2)

Current release P-2026.10.16-v19.2 is PROCEDURE, following the full-history retrospective. Every prompt-1 sport workflow adds one identical **Runtime, baseline and contract definitions** paragraph (capability receipt and bootstrap before any ML_NOT_RUN, a standalone same-line `python -m ml baseline` comparator, and a unit/period/action definition gate); the tennis workflow adds the TENNIS_EXPERIMENTAL_HEDGE_V1 prospective shadow freeze; prompt 6 builds its tables with `python -m ml card-history`. Card, mini and settlement formats, selection, scoring and the primary model are unchanged; every owner-entered Upcoming game block is byte-identical.

## P-2026.10.16-v20.0 — executable forecast cycle

All sports now route through actual attempt/bundle verification under [FORECAST_CYCLE_PROTOCOL](../../REFERENCE_MODEL_PROTOCOL.md#merged-forecast_cycle_protocol). Contextual final-score models, source-addressed identity repair, online verified backfill, settlement feedback and frozen baseline-paired evaluation are connected; qualification still requires future evidence. Owner-entered game blocks and prompt-4-only canonical allocation are preserved.

## P-2026.10.17-v20.1 — browser-chat execution (CHAT-EXEC-v1)

A web chat's read-only GitHub connector cannot run `ml`. Prompt 1 now tells a chat with a Python sandbox to use the owner's runtime pack (`python -m ml.chat pack`), run `python -m ml.chat run` from two small CSVs and a source capture, copy the verified `p_card`/`baseline_p` unchanged and return the upload zip; the owner then runs `python -m ml.chat accept` and commits before the start. Refusals keep rows RESEARCH_ONLY_NO_MODEL. Details: [FORECAST_CYCLE_PROTOCOL](../../REFERENCE_MODEL_PROTOCOL.md#merged-forecast_cycle_protocol). Owner-entered game blocks and prompt-4-only canonical allocation are preserved.

## P-2026.10.17-v20.2 — Google Drive exchange (DRIVE-v1)

Prompts 1 and 2 may use the owner's Google Drive folder under [GOOGLE_DRIVE_EXCHANGE_PROTOCOL](../../archive/retired_2026-11-08/GOOGLE_DRIVE_EXCHANGE_PROTOCOL.md) (retired 2026-11-08). Controls still come from the pinned GitHub commit; a Drive mirror copy counts only when `DRIVE_SYNC_RECEIPT.md` lists it as current. A chat that cannot write the repository uploads the complete updated mini (and, in prompt 1, the RESEARCH_EXPORT CSVs and any CHAT-EXEC upload zip) to `uploads/<date>/<key>_<tool>/` with an `UPLOAD_MANIFEST.md`, and still returns the complete mini in its reply. An upload is not publication; the owner imports it through the normal gates. v21.0 withdrew the Drive mirror requirement (DRIVE-v2: optional drop box only). Owner-entered game blocks are unchanged.

## P-2026.10.17-v21.0 — no-code game research (MLSCOPE-v1 / NOCODE-v1)

STATISTICAL + PROCEDURE. ML/RL leaves game research. Prompt 1 runs no code in any chat: it researches the event and derives every p_card by hand from one coherent distribution (ANALYST_PRIMARY_V1) with [PROBABILITY_TOOLKIT](../../PROBABILITY_TOOLKIT.md) arithmetic shown step by step, records its learning rows as Markdown tables and computes the league-only BASELINE_P by hand. Prompts 1 and 2 read the latest `main` branch on GitHub. Prompts 2–5 drop the execution manifest, runtime, feedback and learning-store commands. Prompt 6 gains the ML/RL review (ingest, feedback, shadows, comparisons) and prompt 8 owns workshop changes; their findings reach cards only as Markdown changes. Google Drive is an optional drop box with no push or mirror requirement (DRIVE-v2). Owner-entered game blocks are unchanged.

## P-2026.10.17-v22.0 — execution environments (ENV-v1)

FORMAT + PROCEDURE. Prompts 1–3 run in an external chat with internet access and read-only GitHub at the latest `main` commit, with a section-level reading budget, no code, no writes and no hashes. Prompt 1 returns the new card, intake row and replacement footer (the full mini only when it fits without truncation); prompt 2 returns the new mini; prompt 3 returns a settlement document that names the frozen mini instead of reproducing it. Prompts 4–8 run in this repository; prompt 4 gains an intake step that assembles card deltas, computes byte counts and SHA-256, checks structure and joins settlements. Details: [EXECUTION_ENVIRONMENT_PROTOCOL](../../WORKFLOW.md#part-a-execution_environment_protocol). Owner-entered game blocks are unchanged.

## P-2026.10.17-v22.1 — prompt 1 core and sport files

PROCEDURE. Prompt 1 is split into a core file (`1_GAME_CARD.md`: shared rules, no code, external chat, latest `main`, delivery) and eleven sport files in `1_sports/`, each holding that sport's complete seven-step workflow and its own Upcoming game block, moved byte-for-byte (only relative links changed for the new folder). An external chat reads the core and one sport file. Requirements, outputs and probabilities are unchanged.

## P-2026.10.17-v22.2 — shared sport rules moved into the prompt 1 core

PROCEDURE. The 19 paragraphs that were identical in all eleven sport files now appear once, in the prompt 1 core under **Shared steps for every sport**. Each sport file keeps its step headings, its own instructions and its Upcoming game block, and each affected step points to the core. The wording of every moved paragraph is unchanged except one cross-reference (the analyst method now points to the sport file's step-4 distribution family). Requirements, outputs and probabilities are unchanged.

## P-2026.10.22-v23.0 (superseded by v24.0) — everything runs here; model shadow after the card (ENV-v2 / MLSCOPE-v2 / MINI-v2)

STATISTICAL + PROCEDURE, owner instruction 22 October 2026. All eight prompts run in this repository with internet access; the external-chat route is retired for new work. Prompt 1 still prices every card itself (ANALYST_PRIMARY_V1; code may do the arithmetic) and reads no model output before the card is written; then it runs `python -m ml pregame run`, which freezes the model, the league baseline and the card's own p_card on identical contracts, or records why it could not run. Prompt 3 settles the card, then the shadow (`cycle settle`), then runs the prompt-4 import, so canonical IDs are assigned only in the settlement phase. A model is judged only after 8 weeks and 50 paired games; a progress review is due at whichever comes first. Releases now freeze only the forecast cycle's import closure. Details: [EXECUTION_ENVIRONMENT_PROTOCOL](../../WORKFLOW.md#part-a-execution_environment_protocol), [FORECAST_CYCLE_PROTOCOL](../../REFERENCE_MODEL_PROTOCOL.md#merged-forecast_cycle_protocol) and the [implementation](../verification/framework_change_2026-10-22-1/IMPLEMENTATION.md).
