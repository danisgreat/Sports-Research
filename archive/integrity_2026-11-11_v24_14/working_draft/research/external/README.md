# Files for the external research chats (v24.13)

Rules: [EXTERNAL_RESEARCH_PROTOCOL](../../EXTERNAL_RESEARCH_PROTOCOL.md) (EXT-v1). Every file a chat uploads carries the version in its name, so an old copy left in a chat is easy to spot. Replace all of them together when the version changes.

## Upload to every chat (or once to a ChatGPT Project)

| File | What it is |
|---|---|
| [EXTERNAL_PROFILE_v24.13.md](EXTERNAL_PROFILE_v24.13.md) | The one page every chat reads first |
| [LANE_BRIEFS_v24.13.md](LANE_BRIEFS_v24.13.md) | The five lane briefs and the return block; paste one brief per chat |
| [`ml/kit/sr_kit.py`](../../ml/kit/sr_kit.py) | The calculation kit (version SR-KIT-v24.13 inside the file); numpy and scipy only |
| [kit/KIT_PARAMETERS_v24.13.csv](kit/KIT_PARAMETERS_v24.13.csv) | Competition rows for the kit: league numbers, widths, tie rules, first-half share, overtime share, dispersion, cricket and tennis rows |
| [kit/KIT_CRICKET_PHASES_v24.13.csv](kit/KIT_CRICKET_PHASES_v24.13.csv) | Per-over ball outcome tables for T20 and ODI, men and women, with each group's innings shock |
| [access/CHATGPT_DO_NOT_OPEN_v24.13.csv](access/CHATGPT_DO_NOT_OPEN_v24.13.csv) | Hosts a chat never opens (blocked for ChatGPT-User at the root, or rules unreadable), with what to use instead where known; valid to the `valid_until` date |
| `sources/PREGAME_SOURCES_<SPORT>_v24.13.csv` | The permitted pregame sources for the game's sport only ([sources/](sources/README.md)) |

## Kept here, not uploaded

| File | What it is |
|---|---|
| [access/READER_ACCESS_v24.13.csv](access/READER_ACCESS_v24.13.csv) | Every audited host, judged for each reader (Claude agent, ChatGPT browsing, repository scripts), with the blocked paths of partly blocked hosts |

## Refreshing (weekly, or before a batch when a list is past its `valid_until`)

```text
python -m ml source-audit --lists <new folder> --hosts-from research/source_routes/SOURCE_ACCESS_AUDIT.csv --hosts-from research/source_routes/PREGAME_SOURCES.csv --hosts-from research/source_routes/COMPETITION_ROUTES.csv --hosts-from research/source_routes/PREGAME_SOURCE_REJECTIONS.csv --use-instead research/source_routes/PREGAME_SOURCE_REJECTIONS.csv --version <version>
python -m ml source-audit --sport-slices <new folder> --reader-access <new folder>/READER_ACCESS_<version>.csv --version <version>
python -m ml kit params --soccer-study <study folder> --sim-checks <checks folder>
```

A refresh that changes a file's contents is a new round of changes: it takes the next version number in every changed file name (the owner's version rule).

## Checked on 11 November 2026

1,179 hosts were re-checked: ChatGPT-User was blocked at the root on 91, partly blocked on 545 (usually admin or search paths only), allowed on 289, with no rules file on 83 and unreadable rules on 171. The Claude agent was blocked at the root on 60. The repository's own scripts, which keep the strict eight-name rule, are blocked on 231. These are dated observations, not permission for every page: the chat still checks a page's path against the host's rules (EXTERNAL_PROFILE §3).
