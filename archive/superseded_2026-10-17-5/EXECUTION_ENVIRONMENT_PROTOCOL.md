# Execution environments: external chat (prompts 1–3) and repository agent (prompts 4–8)

**ENV-2026.10.17-v1 · MDS-2026.10.17-v22.0 · CR-2026.10.17-R4 · P-2026.10.17-v22.0.** Owner instruction, 17 October 2026: prompts 1, 2 and 3 are run in an external chat that has internet access for game research and read access to the GitHub repository; prompts 4–8 are run here, in the repository, not by an external chatbot. FORMAT + PROCEDURE: delivery of prompt-1 cards and prompt-3 settlements changes (sections 4–5). Probabilities, selection, scoring, IDs and issued records are unchanged.

## 1. Who runs what

| Prompt | Environment | Authority | May | May not |
|---|---|---|---|---|
| 1 Game card, 2 Start mini, 3 Settle mini | **EXTERNAL_CHAT**: an external chatbot (for example ChatGPT) with web browsing and read access to the repository | `PUBLISHED_MAIN_PINNED`: the latest commit of `main`, resolved and printed at the start and used for the whole run | Browse the internet for sporting evidence; read repository files; read files the owner attaches or pastes; do written arithmetic | Run any code, code interpreter, notebook, script or command; write, commit or upload to the repository; compute or claim SHA-256 values, byte counts or file saves; use local controls; read model output (MLSCOPE-v1) |
| 4 Import, 5 Rollover, 6 Retrospective, 7 Results, 8 Framework | **REPOSITORY_AGENT**: Claude Code in this repository on the owner's PC | `LOCAL_WORKING_TREE` | Read and write the working tree; run git and the test suite; compute hashes; publish to GitHub when the task authorises it; run ML/RL in prompts 6 and 8 only | Be handed to an external chatbot |

Prompts 1–3 are never run with `LOCAL_WORKING_TREE`, and prompts 4–8 are never run by an external chat. Prompt 4 is the only intake point for anything an external chat produced.

## 2. Reading the repository from an external chat

1. **Resolve the latest commit.** Open `https://github.com/danisgreat/Sports-Research/commits/main` or `https://api.github.com/repos/danisgreat/Sports-Research/commits/main` and record the full SHA of the newest commit. Print it in the reading receipt as the authority, with the read time and timezone offset.
2. **Read files at that commit.** Use `https://raw.githubusercontent.com/danisgreat/Sports-Research/<SHA>/<path>` (spaces in paths become `%20`) or a connected GitHub app pinned to the same SHA. A folder listing, search snippet or summary is not a read. If a file is truncated, read it in parts or fetch the raw file again.
3. **Read only the budget in section 3.** The full control set is larger than a chat can hold, so a chat that claims to have read everything has not. Print exactly which files and sections were read. A section that could not be opened is listed as unread, never assumed.
4. **Owner material.** The active mini, a previous settlement or a carryover list may be attached or pasted by the owner, or committed in the repository. State what was received: file name, number of cards, first and last local key. If nothing was supplied and nothing is committed, say so; do not reconstruct it.

## 3. Reading budget for external chats

| Prompt | Read in full | Read only the named sections |
|---|---|---|
| 1 | Prompt 1's header (everything before the first sport heading) and the **one** sport workflow for this event; [COMMON_OPERATING_PROTOCOL](research/prompts/COMMON_OPERATING_PROTOCOL.md); [SELECTION_RULES](SELECTION_RULES.md); [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md); the active mini | [CURRENT_STATE](CURRENT_STATE.md) release paragraph and Item/Value table; [CURRENT_RULES](CURRENT_RULES.md) §0, §2, §4–§7; [CARD_AND_LOG_TEMPLATES](CARD_AND_LOG_TEMPLATES.md) §2 D and §3–§4, §7; `RULES_<SPORT>.md` §0 and the exact competition's league rules; [SOURCES](SOURCES.md) §1, the sport's §3 table, §3.11 and §3.13; [PROBABILITY_TOOLKIT](PROBABILITY_TOOLKIT.md) status table, the sport's family section (§1, §2, §3, §6 or §7), §4, §8 and §11; [BASE_RATES_REGISTER](BASE_RATES_REGISTER.md) the sport's §7 rows; [LEAGUE_PROFILES](LEAGUE_PROFILES.md) the competition row; [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md) §§1–6; [TIMING_RESEARCH_PROTOCOL](TIMING_RESEARCH_PROTOCOL.md) §1–§3; [GAME_LOG_STATUS_CURRENT](GAME_LOG_STATUS_CURRENT.md) the current section at the top, plus a search for this event's names and date |
| 2 | Prompt 2; COMMON_OPERATING_PROTOCOL; [MINI_LOG_IDENTITY_PROTOCOL](MINI_LOG_IDENTITY_PROTOCOL.md); the previous mini or settlement supplied | CURRENT_STATE release paragraph and table; CARD_AND_LOG_TEMPLATES §2; GAME_LOG_STATUS_CURRENT current section |
| 3 | Prompt 3; COMMON_OPERATING_PROTOCOL; the frozen mini supplied | [SCORING_AND_VALIDATION](SCORING_AND_VALIDATION.md) §1–§3 and §7; SELECTION_RULES §7–§8; CARD_AND_LOG_TEMPLATES §6 and §9; each sport's `RULES_<SPORT>.md` §0 and settlement section; SOURCES §1 and the sports' §3 tables; PROBABILITY_TOOLKIT §10 |

Not read in external chats unless a step names them: other sport workflows, archive folders, old Combined Log parts (search them for the event instead), CHANGELOG, `ml/` and the ML/RL protocols (MLSCOPE-v1).

## 4. Prompt 1 and 2 delivery

An external chat writes no files. Everything is returned in the reply, and the owner saves it.

- **Prompt 2** returns the complete new mini (it is short) with the suggested name `research/active_minis/<MINI_KEY>.md`.
- **Prompt 1** returns:
  1. the complete new card, from `<!-- BEGIN CARD <local key> -->` to `<!-- END CARD <local key> -->`;
  2. the new intake row(s) and the complete replacement footer;
  3. one line saying where they go: the card immediately before the footer, and the old footer replaced.
- **Full mini.** When the whole updated mini (every earlier card plus this one) can be returned without truncation, about 40,000 characters or less, prompt 1 also returns it complete and labels delivery `FULL_MINI`. Otherwise it labels delivery `CARD_DELTA`.
- **Never** truncate silently, present part of a mini as the whole, or claim a file was saved, uploaded, committed or hashed. "Read back" means re-reading the returned text and checking markers, keys, intake and footer agree.
- **No mini.** When the active mini was not supplied, or cannot be read in full, prompt 1 returns the complete card as `READ_ONLY_DRAFT / NOT_ISSUED` with delivery `BLOCKED_NO_MINI`, and allocates no local key.

This replaces the earlier rule that every prompt-1 reply must contain the complete cumulative mini. A real 11-card mini was 321 KB (about 80,000 tokens), which no chat can return in one reply.

## 5. Prompt 3 delivery

- **Settlement document.** Prompt 3 returns one settlement document in mini-settlement-10 sections: settlement blocks and revisions per card, LOCAL_ID_MAPPING, UNRESOLVED_CARRYOVER, SETTLEMENT_MANIFEST, the source-discovery/attempt/closure tables as Markdown, and the learning and review rows. Suggested name: `research/active_minis/<MINI_KEY>_SETTLEMENT.md`.
- **Frozen cards are not reproduced.** The document names the frozen mini by file name and gives its complete block inventory (every card key, addendum and revision, in order), card count and freeze time.
- **Bytes and hashes.** FROZEN_SOURCE byte count and SHA-256 are recorded as `PENDING_PROMPT_4`.

## 6. Prompt 4 intake (repository agent)

Before importing anything produced by prompts 1–3:

1. **Place.** The owner saves each returned mini, card delta and settlement document under `research/active_minis/`, or gives their paths. A Drive upload (DRIVE-v2) is downloaded first into a new empty folder outside the repository.
2. **Assemble.** Insert each `CARD_DELTA` card before the footer in local-key order and replace the footer, keeping every returned block byte-for-byte. Stop on a missing ordinal, duplicate key or a footer that disagrees with the cards.
3. **Freeze and hash.** Compute the frozen mini's byte count and SHA-256, write them into the settlement's FROZEN_SOURCE, and build PREDICTION_MINI_SETTLED as the frozen mini followed by the settlement document.
4. **Check.** Run `python -m ml primary verify-log --mini <mini>` for the structure. Confirm the settlement inventory equals the mini's card list and every settled key exists. Save the Markdown source/closure tables as the CSV sidecars the package needs.
5. **Import.** Continue with prompt 4's verified import, canonical assignment, commit and push.

A defect found at intake is returned to the owner with the exact block and reason. It is never repaired by guessing.

## 7. Limits

- An external chat's arithmetic can be wrong. The written steps and PROBABILITY_TOOLKIT §11 checks are the control, and prompt 4 does not re-price cards.
- An external chat's clock and browsing can be wrong. Every source carries its retrieval time, and an unverifiable time is labelled, never assumed.
- Drive is optional (DRIVE-v2). GitHub `main` is the only authority.
