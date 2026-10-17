# Implementation — execution environments (ENV-v1)

**MDS-2026.10.17-v22.0 · CR-2026.10.17-R4 · P-2026.10.17-v22.0 · ENV-2026.10.17-v1 · FORMAT + PROCEDURE.** Owner instruction, 17 October 2026: "I want prompt 1 and prompt 2 and prompt 3 to be done to an external chat that has access to the internet for research for the game log, and access to the github repo, and prompts 4-8 will be done here and not an external chatbot, so change the requirements accordingly." Read at HEAD `f145bf6f9` (equal to origin/main, clean tree).

## What made the old requirements impossible in an external chat

Measured before the change:
- **Reading.** The reading gate for one basketball card was 1,105,295 bytes (about 276,000 tokens) before the active mini. 68% of prompt 1 is repeated text, and a chat would have had to read all eleven sport workflows.
- **Returning the mini.** Prompt 1 required the complete cumulative mini in every reply. A real 11-card mini (P-590–P-600) was 321,284 bytes, about 80,000 tokens.
- **File operations.** Prompt 3 required a byte copy, a computed SHA-256, the whole frozen prefix re-output, and three CSV files. A chat that may not run code cannot compute a hash or write a file.
- **Authority.** Prompts 1–3 still offered `LOCAL_WORKING_TREE`, which an external chat cannot use.

## Changes

- **New control.** [EXECUTION_ENVIRONMENT_PROTOCOL](../../../EXECUTION_ENVIRONMENT_PROTOCOL.md) covers the environment table, how to resolve the latest `main` SHA and read raw files at it, the reading budget for prompts 1–3, delivery rules (sections 4–5) and prompt-4 intake (section 6).
- **Prompt 1.**
  - New EXTERNAL_CHAT mode line.
  - The active-mini input accepts an attached file, pasted text or a repository path.
  - Each workflow pins the latest `main` (no local option), reads within the budget, produces the card for insertion before the footer, and uses the new mandatory-output paragraph (FULL_MINI / CARD_DELTA / BLOCKED_NO_MINI).
  - The no-code paragraph is limited to external chats.
- **Prompt 2.** EXTERNAL_CHAT; returns the new mini with a suggested file name; owner-supplied or committed previous records; never claims a save.
- **Prompt 3.** EXTERNAL_CHAT. The freeze records name, inventory, card count and time, with bytes and SHA-256 marked PENDING_PROMPT_4. Returns one settlement document that names the frozen mini instead of reproducing it, with Markdown source/closure tables.
- **Prompt 4.** New "0. External-chat intake": place, assemble, freeze and hash, check, report.
- **All prompts.** ENV-v1 paragraph; the MINI-v1 banner, local-record and retention sentences now describe the ENV-v1 delivery; suite version updated.
- **COMMON.** Task table rows 1–3 are EXTERNAL_CHAT, rows 4–8 REPOSITORY_AGENT; control revision R4.
- **Prompt index.** Writes column, a new Environment line in the reading receipt, and a release note.
- **DEPENDENCY_MAP** regenerated.
- **Root documents.**
  - CURRENT_RULES: ENV-v1 paragraph, authority modes, reading gate and freezing.
  - CURRENT_STATE, README, PROMPTS and ACTIVE_FILE_INDEX: ENV-v1 paragraph and pointers.
  - CARD_AND_LOG_TEMPLATES: C22 is now the ENV-v1 delivery check.
  - MINI_LOG_IDENTITY_PROTOCOL: ENV-v1 paragraph.
- **Tests.** In `ml/tests/test_prompt_consistency.py`:
  - prompts 1–3 must name the protocol, EXTERNAL_CHAT and latest `main`;
  - they must not contain local-authority or file-write phrases;
  - prompt 4 must carry the intake section.
- **Originals.** `archive/superseded_2026-10-17-4/` (19 files, ARCHIVE_HASHES.csv).

## Verification

See [VERIFICATION_CHECKS.csv](VERIFICATION_CHECKS.csv).

## Limits

- The reading budget makes a chat's reading feasible; it does not make a chat's arithmetic or browsing reliable. Written steps, toolkit §11 checks and source retrieval times stay the controls.
- **Older wording.** Older documents still carry paragraphs that describe writing or reading back the full mini, notably the MINI-v1 banner copies in root files. ENV-v1 in CURRENT_RULES §0 supersedes them for prompts 1–3. Prompt 1 itself, the template C22 row and prompts 2–3 are updated directly.
- **Size of prompt 1.** Prompt 1 is still one file holding eleven workflows. The budget tells a chat to read only its sport. Splitting the file into a core plus sport annexes would shrink it further, but would move the owner-entered game blocks, so it is left for a separate owner decision.
