# Implementation — prompt 1 core and sport files

**MDS-2026.10.17-v22.1 · CR-2026.10.17-R5 · P-2026.10.17-v22.1 · PROCEDURE.** The owner approved splitting prompt 1 ("yes do that, and push all changes to git after making the changes"), after the ENV-v1 release noted that one 254 KB file holding eleven sport workflows was more than an external chat needs. Read at HEAD `9e88cd54e` (equal to origin/main, clean tree).

## Layout

| File | Holds | Size |
|---|---|---|
| [1_GAME_CARD.md](../../prompts/1_GAME_CARD.md) | Core: identity/retention banners, learning record, mode (EXTERNAL_CHAT), inputs, NOCODE-v1, ENV-v1, latest-`main` reference, sport-file index | 7,354 bytes |
| [1_sports/](../../prompts/1_sports/) | Eleven sport files (BASKETBALL, CRICKET, BASEBALL, SOCCER, ICE_HOCKEY, TENNIS, RUGBY_LEAGUE, RUGBY_UNION, AFL_AFLW, AMERICAN_FOOTBALL, OTHER_SPORTS): a two-line intro pointing to the core, then the sport's complete original section, including its Upcoming game block and steps 1–7 | 22.6–24.2 KB each |

An external chat now reads the core plus one sport file, about 31 KB (roughly 8,000 tokens), instead of 254 KB.

## Method

A one-off helper outside the repository did the split. Its rules:
- Sections start at each sport title line followed by a dash rule; the header is everything before the first title.
- Each section is copied unchanged. Every relative Markdown link gains one `../` because the file moved one folder down; absolute and anchor links are unchanged.
- In the core, two sentences now say "core plus one sport file", and an index table and usage paragraph are appended.

## Verification

See [VERIFICATION_CHECKS.csv](VERIFICATION_CHECKS.csv).

## Other updates

- **Layout descriptions.** CURRENT_RULES §1 lifecycle, the COMMON version paragraph, ENV-v1 reading budget row 1 and the not-read list, PROMPTS (active suite, table, usage line), README (sports section and the 14 October links), ACTIVE_FILE_INDEX, the prompt index (row 1 and a release note) and prompt 8's owner-block rule all describe the core plus sport files.
- **Dependency map.** DEPENDENCY_MAP is regenerated with one row per sport file.
- **Tests.** `ml/tests/test_prompt_consistency.py` now covers the sport files: version, links relative to each file's folder, dependency map, exactly one Upcoming block, identical shared paragraphs (now including the mandatory-output paragraph), no command instructions and no local-authority or file-write phrases. It also checks that the core links all eleven and holds no game block.
- **Archive.** Originals are in `archive/superseded_2026-10-17-5/` (18 Markdown files, ARCHIVE_HASHES.csv). The previous test file is not archived there, because Python may live only under `ml/`; git history keeps it.

## Limits

- **Duplication remains.** The shared sport paragraphs are still repeated in every sport file, as they were inside one file before. The test keeps them identical; factoring them into the core would change each workflow's wording and is a separate decision.
- **Game blocks.** Owner-entered game details now live in `1_sports/<SPORT>.md`. Edit the block in the sport file you will use.
