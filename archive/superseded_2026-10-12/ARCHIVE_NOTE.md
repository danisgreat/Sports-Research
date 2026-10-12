# Documents superseded on 2026-10-12

This folder holds originals from three changes made on 2026-10-12. They are historical references, not current instructions. Relative layout is preserved, so links inside them may point at the former layout.

| Subfolder | Change |
|---|---|
| [prompts_github_readonly/](prompts_github_readonly/ARCHIVE_NOTE.md) | Prompts 1–3 and the prompt index before the "GitHub main read-only" alignment (commit `8831556d0`) |
| [prompt1_per_sport/](prompt1_per_sport/ARCHIVE_NOTE.md) | Prompt 1 before the per-sport restructure (commit `eb1acf58b`) |
| This folder's top level, `Previous Sports Results/`, `research/` | Framework change [2026-10-12-1](../../research/verification/framework_change_2026-10-12-1/IMPLEMENTATION.md): base versions from main `eb1acf58bb7b8c794a2f6a473f737d921f2d5fae` (`git show eb1acf58b:<path>`), byte-identical to that commit, of every operating document the change edited |

**Archived by framework change 2026-10-12-1.** Each was compared with `cmp` against the base commit: 0 mismatches.
- **Root documents:** ARCHIVE_USE_GUIDE, CARD_AND_LOG_TEMPLATES, CHANGELOG, CONTRIBUTING, CURRENT_RULES, CURRENT_STATE, GAME_LOG_STATUS_CURRENT, HISTORICAL_LINK_INDEX, HYPOTHESIS_REGISTER, LEAGUE_PROFILES, LEARNINGS_INDEX, METHOD, PROBABILITY_TOOLKIT, PROMPTS, README, SCORING_AND_VALIDATION, SELECTION_RULES, SOURCES, VERIFICATION_PROTOCOL.
- **Sport rule files:** RULES_AFL, RULES_AMERICAN_FOOTBALL, RULES_BASEBALL, RULES_BASKETBALL, RULES_CRICKET, RULES_ICE_HOCKEY, RULES_NHL, RULES_NRL_RUGBY, RULES_RUGBY_UNION, RULES_SOCCER, RULES_TENNIS.
- **Archive README:** `Previous Sports Results/README.md`.
- **Prompts:** `research/prompts/README.md`, prompts 1–8, and the two v10 examples. The examples also remain unchanged in `research/prompts/examples/legacy_mini_log_6/`.

The reason is the user's instruction to implement the 38 recommendations of `AUDIT_RECOMMENDATIONS_2026-10-12.txt` and the ten prediction recommendations (PR-01 to PR-10), in order. Current entry point: [CURRENT_STATE](../../CURRENT_STATE.md).

The 102 yearly CSVs replaced in phase A were one-line, header-only placeholders. Their base versions remain in git history at `eb1acf58b` and are not copied here. The fabricated, unpublished working versions are preserved outside the repository (see the change folder's [DATA_REBUILD_RECEIPT](../../research/verification/framework_change_2026-10-12-1/DATA_REBUILD_RECEIPT.md)).
