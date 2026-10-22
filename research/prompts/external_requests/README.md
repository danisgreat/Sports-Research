# External-chat game requests, one per sport

**P-2026.10.22-v24.0 · REQ-v2.** Paste-ready prompt-1 requests for a research chat outside the repository (the `PUBLISHED_MAIN_PINNED` route of [EXECUTION_ENVIRONMENT_PROTOCOL](../../../EXECUTION_ENVIRONMENT_PROTOCOL.md)). They replace the free-text request quoted in [GAME_REQUEST_TEMPLATE](../../../GAME_REQUEST_TEMPLATE.md) for that route. Each file is self-contained on purpose, so it can be pasted alone; the rules it repeats are defined in [CORE](../../../CORE.md) and the protocols it links, which govern if the wording ever differs.

| # | Sport file | Request |
|---|---|---|
| 01 | [BASKETBALL](../1_sports/BASKETBALL.md) | [01_BASKETBALL.md](01_BASKETBALL.md) |
| 02 | [BASEBALL](../1_sports/BASEBALL.md) | [02_BASEBALL.md](02_BASEBALL.md) |
| 03 | [ICE_HOCKEY](../1_sports/ICE_HOCKEY.md) | [03_ICE_HOCKEY.md](03_ICE_HOCKEY.md) |
| 04 | [SOCCER](../1_sports/SOCCER.md) | [04_SOCCER.md](04_SOCCER.md) |
| 05 | [AFL_AFLW](../1_sports/AFL_AFLW.md) | [05_AFL_AFLW.md](05_AFL_AFLW.md) |
| 06 | [RUGBY_LEAGUE](../1_sports/RUGBY_LEAGUE.md) | [06_RUGBY_LEAGUE.md](06_RUGBY_LEAGUE.md) |
| 07 | [RUGBY_UNION](../1_sports/RUGBY_UNION.md) | [07_RUGBY_UNION.md](07_RUGBY_UNION.md) |
| 08 | [AMERICAN_FOOTBALL](../1_sports/AMERICAN_FOOTBALL.md) | [08_AMERICAN_FOOTBALL.md](08_AMERICAN_FOOTBALL.md) |
| 09 | [CRICKET](../1_sports/CRICKET.md) | [09_CRICKET.md](09_CRICKET.md) |
| 10 | [TENNIS](../1_sports/TENNIS.md) | [10_TENNIS.md](10_TENNIS.md) |
| 11 | [OTHER_SPORTS](../1_sports/OTHER_SPORTS.md) | [11_OTHER_SPORTS.md](11_OTHER_SPORTS.md) |

## How to use one

1. **Optional but best: run the reference here first.** Ask the repository agent "run the reference stage for <game>" (it runs `python -m ml reference tier`, then `python -m ml pregame reference` for NHL and MLB or `python -m ml reference standings` and `reference run` for TB-2-MD and baseline competitions) and paste the printed Reference block into section A. Then the chat starts from the same frozen number the repository scores against. Without it, the chat computes the reference by hand and marks it `:HAND`.
2. **Fill in section A** of the sport's file and paste everything below its line into the chat. Send it as early as the line-up or injury news allows; a request close to the start gets a fast card first.
3. **Bring the answer back before the start.** Paste the chat's CARD_DELTA here and ask the repository agent to take it in: it saves the text byte for byte under `research/active_minis/received/`, inserts the card before the active mini's footer, runs `python -m ml card lint`, `python -m ml ledger add` and `python -m ml pregame run` (which freezes the card beside the reference and, for NBA, NHL and MLB, the release model), re-runs the reference if the chat's was `:HAND` and records any difference, then commits and pushes. Only the pushed commit makes the card a checkable pre-start forecast.

## What changed from the old free-text request, and why

| Old request said | These prompts do | Why |
|---|---|---|
| "Provide the best 4 picks" | A probability for every supplied contract, the most-likely four with each line's distance from the centre, an information list and an abstain flag | A hit rate on self-chosen lines measures line choice, not forecasting; probabilities between 0.40 and 0.65 have shown no skill (SELECTION_RULES §0) |
| "Do as many simulations as possible" | Exact calculation; a simulation only where the path matters, with seed, N and error, and only as a sensitivity | A chat that has not run code has not simulated; N = 1,000 has an error as large as the effects measured (SIMULATION_PROTOCOL) |
| "Refer to the local files" | Raw links to the exact files and sections on `main`, with a reading receipt and the commit SHA | An external chat cannot see the owner's PC; `main` is the published copy |
| General research | A value-ranked list per sport with publication times and verified routes | Availability and starters move probabilities by several points; most other inputs move them by one to three or less (RESEARCH_CHECKLISTS) |
| (none) | The reference first, then logged adjustments sized from effect tables | The record showed cards losing to simple baselines; starting from the reference and scoring each departure is how the research can show its value (REFERENCE_MODEL_PROTOCOL) |

## Limits

- The chat cannot run the repository's models, the linter or the freeze; the repository agent does that at intake, and the card is not a frozen forecast until the commit is pushed.
- A hand-computed reference can differ from the repository's by rounding or by a different standings snapshot; the intake records both.
- The source routes were tested from this machine on the dates in SOURCES; an external chat may be blocked where this machine was not, and the reverse.
