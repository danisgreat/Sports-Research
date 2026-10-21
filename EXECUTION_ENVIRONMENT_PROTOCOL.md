# Execution environment: every prompt runs in the repository (ENV-v2)

**ENV-2026.10.22-v2 · MDS-2026.10.22-v23.0 · CR-2026.10.22-R1 · P-2026.10.22-v23.0.** Owner instruction, 22 October 2026: the game logs are run here, not in an external chat. Every prompt, 1 to 8, is run in this repository by the repository agent (Claude Code on the owner's PC), with internet access for research. This supersedes ENV-v1 (17 October 2026), under which prompts 1–3 ran in an external chat; its text is archived in [archive/superseded_2026-10-22-1/](archive/superseded_2026-10-22-1/EXECUTION_ENVIRONMENT_PROTOCOL.md). Probabilities, selection, scoring and issued records are unchanged; delivery, model-shadow timing and the canonical assignment stage change (sections 3–5).

## 1. Who runs what

| Prompt | Environment | Authority | Writes | Model work (MLSCOPE-v2) |
|---|---|---|---|---|
| 1 Game card | REPOSITORY_AGENT, internet research | `LOCAL_WORKING_TREE` | Card, intake row and footer in the active mini; pregame receipt and frozen shadow rows; commit and push | After the card is written: `python -m ml pregame run` |
| 2 Start mini | REPOSITORY_AGENT | `LOCAL_WORKING_TREE` | New mini, active-mini pointer; commit and push | None |
| 3 Settle mini | REPOSITORY_AGENT, internet research | `LOCAL_WORKING_TREE` | Frozen-source identity, settlement document, shadow settlements, then the prompt-4 import; commit and push | `python -m ml cycle settle` for shadowed events |
| 4 Import | REPOSITORY_AGENT | `LOCAL_WORKING_TREE` | Canonical suffix, mapping, state; run by prompt 3 or alone | None |
| 5–8 | REPOSITORY_AGENT | `LOCAL_WORKING_TREE` | As each prompt declares | 6 evaluates (`pregame status`, `cycle evaluate`, `pregame compare-card`); 8 releases |

`PUBLISHED_MAIN_PINNED` remains valid only for an agent working outside the repository (the retired ENV-v1 route). Its outputs are taken in through prompt 4's intake, unchanged.

## 2. Reading

Read controls from the working tree. Print branch, HEAD SHA, read time with offset and every uncommitted control difference in the reading receipt (CURRENT_RULES §0). The section-level reading budget of ENV-v1 no longer applies: read what the prompt names, in full where it says so. GitHub `main` is the published copy and the fallback for an unreadable local file (REF-v1).

Research is done on the internet with the agent's own tools, from verifiable sources that carry comprehensive, accurate data for the exact game: competition and team field owners, official injury and line-up publications, league match centres and box scores, and the permitted structured providers in [SOURCES](SOURCES.md). Open each source; record its URL, the field used, publication and retrieval times, and an independent corroboration for every material fact (HISTORICAL_SOURCE_PROTOCOL, ROSTER_AVAILABILITY_PROTOCOL, RESEARCH_EXHAUSTIVENESS_PROTOCOL). A search snippet is not an opened source. Odds, tips, previews and fantasy content are never inputs.

## 3. Prompt 1 and 2 delivery

- **Prompt 2** writes the new mini to `research/active_minis/<MINI_KEY>.md`, points CURRENT_STATE at it and commits and pushes.
- **Prompt 1** appends the complete card immediately before the active mini's footer, updates intake and footer, reads the whole file back, then runs the pregame model shadow and adds its block to the card. It commits and pushes the mini, the receipt and the frozen rows, before the scheduled start whenever possible: the pushed commit is the externally checkable freeze. The reply summarises the picks, the likely winner, the reasons and sources, the shadow disposition and the commit.
- Owner material produced elsewhere (an attached mini, a pasted card) is first copied byte-for-byte under `research/active_minis/received/` and then used; it is never retyped into a frozen source.
- Never claim a write, commit or push that did not happen. A failed write or push is reported with its exact error, and the research is kept.

## 4. Prompt 3 delivery and canonical assignment

- Prompt 3 freezes the mini and records its byte count and SHA-256 itself; FROZEN_SOURCE is no longer PENDING_PROMPT_4.
- It writes the settlement document, settles the model shadows of shadowed events and then runs prompt 4 on the frozen mini and settlement in the same session. **Canonical IDs are assigned only in this settlement phase** (MINI-v2): settled events receive their IDs; pending events stay in the carryover with canonical ID NOT_ASSIGNED and move to the next mini.

## 5. Model shadow timing (MLSCOPE-v2)

The card is priced before any model output is read. The pregame command refuses to run unless the card's BEGIN and END markers are already in the mini, and it refuses a `card_p` value that is not printed in that card. The card's own p_card is frozen beside the model and the league baseline on identical contracts, so the three can be compared prospectively. Details: [FORECAST_CYCLE_PROTOCOL](FORECAST_CYCLE_PROTOCOL.md).

## 6. Limits

- Agent arithmetic can still be wrong. Printed inputs and steps, the toolkit §11 checks and readback are the controls.
- A pushed commit time proves when bytes were published, not when a source was published; source times are recorded separately and an unverifiable time is labelled, never assumed.
- Drive (DRIVE-v2) remains an optional drop box for owner material; it is never a control.
