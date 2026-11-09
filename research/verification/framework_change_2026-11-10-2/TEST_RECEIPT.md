# Test receipt — framework change 2026-11-10-2

- `python -m pytest ml/tests -q`, first run after the edits: **775 passed, 1 failed**, 499.21 s. `test_dependency_map_covers_every_prompt_in_both_directions` found that the AFL/AFLW sport file now names GAME_REQUEST_TEMPLATE but [DEPENDENCY_MAP](../../prompts/DEPENDENCY_MAP.md) did not list it.
- Fix: GAME_REQUEST_TEMPLATE added to the AFL/AFLW row, matching the other sport files.
- `python -m pytest ml/tests -q`, after the fix: **776 passed**, 448.53 s, exit code 0.
- `python -m pytest ml/tests -q`, after AFL-ET-1 was added: **776 passed**, 516.66 s, exit code 0.

These confirm the implemented checks. They say nothing about sporting accuracy or predictive skill.
