# One-chat seals, intakes and scores (ONE-CHAT-v2)

- `sealed/` — card files sealed before play by `python -m ml one-chat seal`: each file under its SHA-256 prefix, `SEALS.csv` (card key, block hash, file hash, path, owner-clock time) and `PUSH_RECEIPTS.csv` (GitHub's server push times for main, refreshed with `python -m ml one-chat receipts`). Rows are appended, never edited.
- `intake/<YYYY-MM-DD-n>/` — one immutable run of `python -m ml one-chat intake` on an owner drop: CARDS.csv, PICKS.csv, FACTS.csv, INTAKE_RECEIPT.csv and MANIFEST.csv (the SHA-256 of each). Commit the folder before scoring.
- `scores/<YYYY-MM-DD-n>/` — one immutable run of `python -m ml one-chat score`: SUMMARY.csv (the verdict, e-value and lower bound), SEQUENCE.csv (every game in order with d, bet and e-value), COVERAGE.csv (every card with its timing, seal and exclusion), CUSTODY_PROBLEMS.csv, SPORT_EVIDENCE.csv, TABLES.csv and, once, COHORT.csv with COHORT_RECEIPT.csv.

Rules: [RULES_REFERENCE](../../RULES_REFERENCE.md) "Sealing, custody and the anytime test". Plan: [EVALUATION_PLAN_v26.0](../external/EVALUATION_PLAN_v26.0.md). Brief for the chats: [ONE_CHAT_BRIEF_v26.0](../external/ONE_CHAT_BRIEF_v26.0.md). No card had been sealed at release: the sequence starts with the first sealed card.
