# Files for the external research chats (v26.0)

## Current operation: one chat per game (ONE-CHAT-v2, 16 November 2026)

Upload to each chat (or once to a ChatGPT Project):

| File | What it is |
|---|---|
| [ONE_CHAT_BRIEF_v26.0.md](ONE_CHAT_BRIEF_v26.0.md) | The one brief: what the chat does and the `ONECHAT_V1` block that ends every card (v25.0 is retained; do not upload it) |
| [`ml/kit/sr_kit.py`](../../ml/kit/sr_kit.py) and the kit parameter files below | The calculation kit (unchanged, v24.15) |
| The current do-not-open list and `sources/PREGAME_SOURCES_<SPORT>_v24.15.csv` | Where the chat may read (unchanged) |

**Owner step before play:** save the finished card file and run `python -m ml one-chat seal --card "<file>"`. It commits the file, pushes it and records GitHub's push time; a card sealed after the game starts is kept but never counts.

Assessment: [EVALUATION_PLAN_v26.0.md](EVALUATION_PLAN_v26.0.md) (supersedes v25.0, under which no game was scored). The profile, the lane briefs and the audit supplement described below belong to the five-lane route (EXT-v3). They are retained and are not uploaded for new games.

## Five-lane package (v24.15, retained; takes no new game)

**Current source observation:** [CURRENT_ACCESS.csv](access/CURRENT_ACCESS.csv) selects v24.15-OBS20261116R1. Only 16 touched hosts were freshly checked; all 1,168 other observation/expiry clocks remain unchanged. This is a source-only refresh, not a new statistical profile. For settlement also supply [SETTLEMENT_SOURCES.csv](../source_routes/SETTLEMENT_SOURCES.csv); its hand-reader-only routes must not be bulk-fetched.

**Required operational supplement:** upload [AUDIT_CHAT_BRIEF_v1.md](AUDIT_CHAT_BRIEF_v1.md) with the unchanged v24.15 statistical files, and read [AUDIT_REVIEW_PROTOCOL](../../AUDIT_REVIEW_PROTOCOL.md) at the event commit. Each generated packet now includes the effective actual-reader access rows and pinned audit controls. A versioned exclusion list alone is insufficient for path-specific permission.

Rules: [EXTERNAL_RESEARCH_PROTOCOL](../../EXTERNAL_RESEARCH_PROTOCOL.md) (EXT-v3). Every file a chat uploads carries the version in its name, so an old copy left in a chat is easy to spot. Replace all of them together when the version changes.

## Upload to every chat (or once to a ChatGPT Project)

| File | What it is |
|---|---|
| [EXTERNAL_PROFILE_v24.15.md](EXTERNAL_PROFILE_v24.15.md) | The one page every chat reads first |
| [LANE_BRIEFS_v24.15.md](LANE_BRIEFS_v24.15.md) | The five lane briefs and the return block; paste one brief per chat |
| [`ml/kit/sr_kit.py`](../../ml/kit/sr_kit.py) | The calculation kit (version SR-KIT-v24.15 inside the file); numpy and scipy only |
| [kit/v24.15/KIT_PARAMETERS_v24.15.csv](kit/v24.15/KIT_PARAMETERS_v24.15.csv) | Competition rows for the kit: league numbers, widths, tie rules, first-half share, overtime share, dispersion, cricket and tennis rows |
| [kit/v24.15/KIT_CRICKET_PHASES_v24.15.csv](kit/v24.15/KIT_CRICKET_PHASES_v24.15.csv) | Per-over ball outcome tables for T20 and ODI, men and women, with each group's innings shock |
| [access/observations_20261116R1/CHATGPT_DO_NOT_OPEN_v24.15-OBS20261116R1.csv](access/observations_20261116R1/CHATGPT_DO_NOT_OPEN_v24.15-OBS20261116R1.csv) | Hosts a chat never opens (blocked for ChatGPT-User at the root, or rules unreadable), with what to use instead where known; valid to the `valid_until` date |
| `sources/PREGAME_SOURCES_<SPORT>_v24.15.csv` | The permitted pregame sources for the game's sport only ([sources/](sources/README.md)) |

## Available in every generated packet (also upload directly if packets are unavailable)

| File | What it is |
|---|---|
| [access/observations_20261116R1/READER_ACCESS_v24.15-OBS20261116R1.csv](access/observations_20261116R1/READER_ACCESS_v24.15-OBS20261116R1.csv) | Every audited host, judged for each reader (Claude agent, ChatGPT browsing, repository scripts), with the blocked paths of partly blocked hosts |

## Refreshing (weekly, or before a batch when a list is past its `valid_until`)

```text
python -m ml source-audit --lists <new folder> --hosts-from research/source_routes/SOURCE_ACCESS_AUDIT.csv --hosts-from research/source_routes/PREGAME_SOURCES.csv --hosts-from research/source_routes/COMPETITION_ROUTES.csv --hosts-from research/source_routes/PREGAME_SOURCE_REJECTIONS.csv --use-instead research/source_routes/PREGAME_SOURCE_REJECTIONS.csv --version <version>
python -m ml source-audit --sport-slices <new folder> --reader-access <new folder>/READER_ACCESS_<version>.csv --version <version>
python -m ml kit params --soccer-study <study folder> --sim-checks <checks folder>
```

A refresh that changes a file's contents is a new round of changes: it takes the next version number in every changed file name (the owner's version rule).

## Checked on 11 November 2026

1,179 hosts were re-checked: ChatGPT-User was blocked at the root on 91, partly blocked on 545 (usually admin or search paths only), allowed on 289, with no rules file on 83 and unreadable rules on 171. The Claude agent was blocked at the root on 60. The repository's own scripts, which keep the strict eight-name rule, are blocked on 231. These are dated observations, not permission for every page: the chat still checks a page's path against the host's rules (EXTERNAL_PROFILE §3).


## Admission and release status

The current definition is ../../EXTERNAL_RESEARCH_PROTOCOL_V3.md. Run external package-check after installing the whole version. Initialize an immutable event manifest only after its exact artifacts are committed; L4 and L5 receive dependency-bound packets. All source observations retain their actual checked_at/valid_until dates: the v24.15 copies are byte-identical snapshots, not a fresh network audit. The parameter package is uncalibrated development/reference arithmetic, not model promotion. Cricket simulation and tennis form shock are sensitivity-only.

The builder writes versioned upload files and supporting evidence. The separate owner-authorized v24.15 release installs 32 measured soccer rows into the shared reference table. Existing output versions cannot be overwritten. See EVALUATION_PLAN_v24.16.md for the current count-based paired assessment. No model has been promoted, and historical availability has not been fabricated.


## Current versus superseded packages

Only v24.15 is current. v24.13 and v24.14 profiles/briefs/kit files are retained originals and must not be mixed into a current chat. The standalone kit header now names v24.15. Source-only snapshots use their own date-based versions; CURRENT_ACCESS.csv identifies the current reader/access pair with canonical-LF hashes. The initial v24.15 access copies retain the original 10 November observation/17 November UTC expiry; copying is not a fresh audit. Update the pointer after an actual audit without bumping the statistical method.

Use [EXT-v3](../../EXTERNAL_RESEARCH_PROTOCOL_V3.md) for the shorter packet/batch flow, reduced/six roles, partial pricing, delay amendments, SINGLE freezing and fact scorecards. Live pilot remains PENDING actual event/lines and genuine chat returns.


**Current assessment plan v24.19:** [EXT-EVAL-v2 with on-request audits](EVALUATION_PLAN_v24.19.md) audits on owner request at any count (AUDIT-ANYTIME-v1); the frozen assessment still runs at the first 100 eligible fully settled games without waiting for any number of weeks. Upload kit/profile/briefs stay v24.15; forecast values and identities have not changed. Prior evaluation plans are retained registrations, superseded for the unstarted current experiment by the owner amendment.
