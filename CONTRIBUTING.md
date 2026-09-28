# Contributing to the Markdown repository

The published repository has one branch, `main`, and every file in its current tree ends in `.md`. Files live at the root or directly in `prediction logs/`. Git's internal data is outside that file rule.

## Before changing a record

1. Read `CURRENT_RULES.md`, the relevant sport file, `METHOD.md`, the canonical snapshot in `prediction logs/PREDICTION_LOG_COMBINED_5.md`, and the working custody note in `prediction logs/PREDICTION_LOG_COMBINED_6.md`.
2. Check `GAME_LOG_STATUS_CURRENT.md` and Part 6 for IDs, event state, and the freeze receipt.
3. Keep issued cards and probabilities intact. Append corrections and settlement evidence; do not rewrite the frozen issue.
4. Use official source records and preserve `SPORTS_ONLY / MARKET_BLIND`. Record missing evidence as missing.

## Before updating `main`

1. Run the [Markdown verification protocol](VERIFICATION_PROTOCOL.md). Review changed Markdown files and check current operating links. Historical removed targets are indexed in [Historical Link Index](HISTORICAL_LINK_INDEX.md).
2. Check Parts 5 and 6 and their ID/queue state against `GAME_LOG_STATUS_CURRENT.md`.
3. For governance edits, update the current Markdown control manifest with SHA-256 hashes of its listed files in CRLF form. Point `METHOD.md` to it and place its own SHA-256 in the current freeze receipt line of `GAME_LOG_STATUS_CURRENT.md`.
4. Check that the current file tree contains only root-level `.md` files and Markdown logs directly in `prediction logs/`.
5. Review the staged changes before committing and pushing `main`.

Retired files and prior executable checks remain in Git history. [Validation Evidence](VALIDATION_EVIDENCE.md) embeds historical outputs and code, but missing game-level data prevents full independent rerun. A historical test result does not certify later Markdown-only changes. The current forecasting procedures and hand calculations are in `CURRENT_RULES.md`, `PROBABILITY_TOOLKIT.md`, and `CARD_AND_LOG_TEMPLATES.md`.
