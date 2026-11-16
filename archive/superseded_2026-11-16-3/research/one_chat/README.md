# One-chat intakes and scores (ONE-CHAT-v1)

- `intake/<YYYY-MM-DD-n>/` — one immutable run of `python -m ml one-chat intake` on an owner drop: CARDS.csv (every file and block with its status, hashes, saved time and timing header), PICKS.csv (the card's own numbers with favoured side, rank and flags), FACTS.csv and INTAKE_RECEIPT.csv.
- `scores/<YYYY-MM-DD-n>/` — one immutable run of `python -m ml one-chat score`: SUMMARY.csv, COVERAGE.csv (every admitted card with its eligibility or exclusion), TABLES.csv, GAME_SCORES.csv and, at the first READY run, COHORT.csv.

Rules: [RULES_REFERENCE](../../RULES_REFERENCE.md) "One chat per game". Plan: [EVALUATION_PLAN_v25.0](../external/EVALUATION_PLAN_v25.0.md). Brief for the chats: [ONE_CHAT_BRIEF_v25.0](../external/ONE_CHAT_BRIEF_v25.0.md). No run existed at release: the cohort starts with the first card that carries the block.
