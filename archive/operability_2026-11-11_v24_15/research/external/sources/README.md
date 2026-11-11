# Permitted pregame sources for research chats, by sport (v24.14)

Each `PREGAME_SOURCES_<SPORT>_v24.14.csv` holds the rows of [PREGAME_SOURCES.csv](../../source_routes/PREGAME_SOURCES.csv) for that sport, plus the shared weather and news rows, that a ChatGPT research chat may open, judged by ChatGPT-User's own rules (SRC-ALT-v3, checked 11 November 2026). Two columns are added:

- `chatgpt_status`: ALLOWED, NO_RULES_FILE, or CHECK_PATH (the host blocks some paths for ChatGPT-User; the chat checks the page's path against `chatgpt_blocked_paths` and the host's robots.txt before opening it).
- `chatgpt_blocked_paths`: the Disallow paths that apply to ChatGPT-User on that host.

Hosts blocked at the root for ChatGPT-User, or with unreadable rules, are left out; they are in [CHATGPT_DO_NOT_OPEN_v24.14.csv](../access/CHATGPT_DO_NOT_OPEN_v24.14.csv). Read each source at its `when_to_check` time. `prices_on_page` YES_BLOCK means the page also shows prices: take only the statistic.

Regenerate with `python -m ml source-audit --sport-slices <folder> --reader-access <READER_ACCESS file> --version <version>`.
