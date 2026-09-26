# Former root `scratch/` folder (archived 2026-09-26)

These two scripts lived in a root `scratch/` folder until 2026-09-26. They are kept as evidence, not as tools:

- `build_full_settlement.py` generated the P-510–P-515 settlement with **typed-in narrative strings** instead of fetched data. It produced false lineup diffs (P-510, P-511) and a wrong score (P-515). That is the M26 recurrence behind `C-SETTLEMENT-FROM-FEED` and audit field `10n` (`RULES_GENERAL.md` §"2026-09-25(e)"). **Do not reuse it.** Settlement facts come from `receipts.py settle …` or a fetched endpoint pasted with its URL.
- `tennis_sim.py` is an exploratory tennis set/game simulation with no tests and no registered use.

`scratch/` is now listed in `.gitignore`, so session scratch files are not committed again.
