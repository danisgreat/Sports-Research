# Implementation — shared sport rules moved into the prompt 1 core

**MDS-2026.10.17-v22.2 · CR-2026.10.17-R6 · P-2026.10.17-v22.2 · PROCEDURE.** Owner instruction, 17 October 2026: "move them into the core", meaning the paragraphs that were repeated in every prompt-1 sport file after the v22.1 split. Read at HEAD `7a2c78a3c` (equal to origin/main, clean tree).

## What moved

A one-off helper outside the repository split every sport file into blank-line-separated paragraphs, tagged each with its step, and found 26 paragraphs identical in all eleven files, in the same order everywhere.

**Kept in the sport files (7):**
- the five step headings that happened to be identical (steps 1, 2, 4, 5 and 7), so every sport file keeps steps 1–7;
- the `Read [COMMON_OPERATING_PROTOCOL]…` line, which marks the end of the owner's game block;
- the file intro, which was rewritten.

**Moved to the core (19),** under **Shared steps for every sport**:

| Core section | Paragraphs |
|---|---|
| Before step 1 — evidence standard | Current evidence requirement (EXH) |
| Step 1 — Read and establish authority | REF-v1; inaccessible-control draft rule; strict research completion |
| Step 3 — Evidence, line-ups and online history | mandatory history and players; mandatory online history; form windows and known-at |
| Step 4 — Distribution, expected score and comparator | RETAIN-v3; local research record; ANALYST_PRIMARY_V1; pricing basis (PR-03) |
| Step 5 — Candidate selection and dependence | family eligibility and order; RET04/XCARD6 and shadows |
| Step 7 — Write, audit and return | templates and append; A9 completion; duplicate/addendum; learning record (LEARN-v2); contract definitions and comparator; mandatory output |

**Wording.** Moved paragraphs keep their exact wording, with one `../` removed from relative links because the core sits one folder up. One cross-reference changed: the analyst method's "use the sport family below" now reads "use the sport file's step-4 distribution family".

**Pointers.** Each sport file now says, after the Read line and under steps 1, 3, 4, 5 and 7, to also apply the matching core section.

## Sizes

- **Core:** 22,378 bytes (was 7,354).
- **Basketball file:** 9,875 bytes (was 23,446); the other sport files are similar.
- **Per game:** an external chat reads core plus one sport file, about 32 KB.
- **Total prompt 1 text:** down from about 265 KB to about 130 KB.

## Verification

See [VERIFICATION_CHECKS.csv](VERIFICATION_CHECKS.csv).

## Other updates

- Suite version in every prompt; COMMON control revision R6.
- CURRENT_RULES §1 lifecycle, CURRENT_STATE, README, PROMPTS and the prompt index note.
- DEPENDENCY_MAP regenerated.
- `ml/tests/test_prompt_consistency.py`:
  - the core holds each shared rule exactly once, under the six shared-step headings;
  - no sport file repeats one;
  - each sport file keeps steps 1–7, one Upcoming block, the Read line and five pointers to the core.

## Limits

When the core's shared rule and a sport file's own instruction overlap, the core tells the chat to follow the sport file where it is more specific. No conflicting pair was found: the moved paragraphs were identical across all sports, so none of them is sport-specific.
