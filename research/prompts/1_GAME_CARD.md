# PROMPT 1 — Research and append one individual game card

**Local keys until import; updated mini after every game (MINI-v1).** Apply [MINI_LOG_IDENTITY_PROTOCOL](../../MINI_LOG_IDENTITY_PROTOCOL.md). Prompts 1–3 use stable local event keys and never assign/reserve canonical P-IDs; prompt 4 alone assigns them during verified import. After each prompt-1 game request, return the new card with its intake row and footer, plus the full mini when it fits, for the owner to save (ENV-v1). Preserve every owner-entered Upcoming game block and all earlier issued bytes. New formats: mini-log-10 / mini-settlement-10; earlier records retain their original formats.

**Persistent research and corroboration (EXH-v1).** Apply [RESEARCH_EXHAUSTIVENESS_PROTOCOL](../../RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) to every required field in research, logging, settlement and verification. If a source is incomplete, open alternatives and verify material facts with another independent source; track every remaining field and attempt. Unresolved facts/corroboration never qualify as complete information. New settlements use mini-settlement-10 with a visible source-discovery/reuse section, three source/attempt/closure CSVs and S17; older originals retain their rules and bytes. Consult [RESEARCH_SOURCE_REGISTER](../../RESEARCH_SOURCE_REGISTER.md) and prior package registers, recheck actual coverage, and continue discovery beyond them.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** For every game, research both sides' L5/L10/L15/L20 online under [HISTORICAL_SOURCE_PROTOCOL](../../HISTORICAL_SOURCE_PROTOCOL.md), with opened sources, dated game rows and true n. Seek exact-game confirmed players, starting roles, bench/replacements and absences under [ROSTER_AVAILABILITY_PROTOCOL](../../ROSTER_AVAILABILITY_PROTOCOL.md); projected players remain unconfirmed. The retired local results store and its derived profiles are not required inputs or fallbacks. Earlier archive-first directions are superseded.

**Learning record (LEARN-v2).** Every game request records, inside the card, the prior-game rows and availability snapshots it used as Markdown tables (step 7). Prompt 6 later turns settled cards into learning data; this prompt writes no CSV export and runs nothing.

**Mode:** LOCAL_MINI_STAGING · **EXTERNAL_CHAT** (ENV-v1). **Writes:** nothing. The reply returns the complete new card, its intake row and the replacement footer (and the full mini when it fits) for the owner to save. **GitHub repository (latest `main` branch):** read-only. Authority mode `PUBLISHED_MAIN_PINNED` (CURRENT_RULES §0): resolve the latest `main` commit, print its full SHA and use that one commit for the whole run; this prompt never uses local controls. Read within the ENV-v1 reading budget: this core, the one sport file for the event and the named sections of larger files. Do not settle, retrospect, change rules or assign/reserve canonical P-IDs. Use local event keys; prompt 4 assigns canonical IDs at import. Prompt suite P-2026.10.17-v22.1 (ENV-v1 external chat; NOCODE-v1 hand-derived analyst probability; MLSCOPE-v1; contract-definition gate), new minis mini-log-10 (existing minis keep their original format).

Inputs: `Event: <participants, league/format, date/time/timezone or official event link>`; `Active mini: <attached file, pasted text or repository path>`; `Supplied contracts: <exact text/lines, or none>`; `Specific research constraints: <if any>`. Treat estimated starts as estimates until verified. Locate accessible inputs first; ask only for information essential to resolve ambiguity. This core plus the one matching sport file is the complete game prompt; nothing from prompt 2 needs to be pasted with it. Open the sport file listed below and follow its seven steps.

**No code in game research (NOCODE-v1, MLSCOPE-v1).** This prompt is a research and probability framework, not a program. In ChatGPT or any other external chat: run no Python or other code, code interpreter, notebook, script, runtime pack (`SR_RUNTIME_*.zip`), command-line tool or model package, and do not ask for one. Do not read, copy or wait for model, shadow, cycle or decision-lab output. Do the whole task with opened sources and written arithmetic: research the event (steps 1–3), then build one coherent distribution by hand (step 4) with [PROBABILITY_TOOLKIT](../../PROBABILITY_TOOLKIT.md) tables and formulas, writing every input, formula, intermediate value and result so a reader can check it with a calculator. Every p_card is ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY. ML/RL runs only in prompts 6 and 8.

**Execution environments (ENV-v1).** Prompts 1–3 run in an external chat with internet access and read-only access to the GitHub repository at the latest `main` commit: no code, no repository writes, no hashes, a section-level reading budget, and every output returned in the reply for the owner to save. Prompts 4–8 run in this repository as the repository agent (`LOCAL_WORKING_TREE`); prompt 4 is the only intake point for external-chat output and computes the byte counts and SHA-256 the chat cannot. Details: [EXECUTION_ENVIRONMENT_PROTOCOL](../../EXECUTION_ENVIRONMENT_PROTOCOL.md).

**Repository reference (latest `main`).** Read this prompt's controls from the latest commit of the `main` branch of [Sports Research on GitHub](https://github.com/danisgreat/Sports-Research/tree/main). At the start, resolve that commit's full SHA, print it in the reading receipt and use that one commit for the whole run ([GITHUB_REFERENCE_PROTOCOL](../../GITHUB_REFERENCE_PROTOCOL.md)); never use an older branch, a cached copy or a Drive file as the authority. Optional: when this chat cannot write the repository, it may upload the complete updated mini `.md` to the owner's [Google Drive folder](https://drive.google.com/drive/folders/1ChlwkiOvd8c4MTaLC5BvkLniWogrm8Lj?usp=drive_link) `uploads/` (DRIVE-v2, [GOOGLE_DRIVE_EXCHANGE_PROTOCOL](../../GOOGLE_DRIVE_EXCHANGE_PROTOCOL.md)); this is never required, and the complete mini is still returned in the reply.

## Sport files

Prompt 1 is this core plus one sport file. In the external chat, paste or attach this core and the one sport file for the event, with its Upcoming game block filled in. Each sport file holds that sport's complete workflow: 1 read and establish authority; 2 identity, duplicate and timing gate; 3 evidence, line-ups and online history; 4 distribution, expected score and comparator; 5 candidate selection and dependence; 6 playing conditions and rules; 7 write, audit and return.

| Sport | File |
|---|---|
| BASKETBALL | [1_sports/BASKETBALL.md](1_sports/BASKETBALL.md) |
| CRICKET | [1_sports/CRICKET.md](1_sports/CRICKET.md) |
| BASEBALL | [1_sports/BASEBALL.md](1_sports/BASEBALL.md) |
| SOCCER | [1_sports/SOCCER.md](1_sports/SOCCER.md) |
| ICE HOCKEY | [1_sports/ICE_HOCKEY.md](1_sports/ICE_HOCKEY.md) |
| TENNIS | [1_sports/TENNIS.md](1_sports/TENNIS.md) |
| RUGBY LEAGUE | [1_sports/RUGBY_LEAGUE.md](1_sports/RUGBY_LEAGUE.md) |
| RUGBY UNION | [1_sports/RUGBY_UNION.md](1_sports/RUGBY_UNION.md) |
| AFL / AFLW | [1_sports/AFL_AFLW.md](1_sports/AFL_AFLW.md) |
| AMERICAN FOOTBALL | [1_sports/AMERICAN_FOOTBALL.md](1_sports/AMERICAN_FOOTBALL.md) |
| OTHER SPORTS | [1_sports/OTHER_SPORTS.md](1_sports/OTHER_SPORTS.md) |
