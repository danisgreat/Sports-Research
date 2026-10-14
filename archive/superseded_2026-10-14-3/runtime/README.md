# runtime/ (removed)

The numerical runtime that lived here was removed on 2026-10-09 so that the framework is Markdown, CSV and text only (commits `a64675cf7` to `a93352c30`). It contained distribution engines for nine sports (baseball, basketball, soccer, ice hockey, American football, Australian rules, rugby league, cricket, tennis), calibration, stacking, uncertainty and selection modules, league configuration, R ingestion scripts for AFL and NRL, and tests.

- **Last working state:** git commit `37203fc2b` (`git show 37203fc2b:runtime/README.md` prints the old description of this folder).
- **The ideas that remain, as documents:** the event-first principle and the sport methods are in [../research/prompts/1_GAME_CARD.md](../research/prompts/1_GAME_CARD.md) (sport blocks) and [../PROBABILITY_TOOLKIT.md](../PROBABILITY_TOOLKIT.md); the league configuration is in [../LEAGUE_PROFILES.md](../LEAGUE_PROFILES.md); the selection rules are in [../SELECTION_RULES.md](../SELECTION_RULES.md); the design notes are in [../NUMERICAL_MODEL_REGISTER.md](../NUMERICAL_MODEL_REGISTER.md) and [../H0_DATASET_CARD.md](../H0_DATASET_CARD.md).
- **Pre-rewrite description of the runtime:** [../archive/superseded_2026-10-09/research_readmes/runtime_README.md](../archive/superseded_2026-10-09/research_readmes/runtime_README.md).
- **Not available now:** fitted models and calibrators, shadow forecasts, the `runtime_h0` and `runtime_h0_v2` build receipts, live qualification. Every card is a hand-built `UNCALIBRATED_ANALYST_SCENARIO`.

To bring any of this back, follow prompt 8 ([../research/prompts/8_IMPROVE_THE_FRAMEWORK.md](../research/prompts/8_IMPROVE_THE_FRAMEWORK.md)): it needs an explicit user instruction, because it reverses the Markdown-only rule.
