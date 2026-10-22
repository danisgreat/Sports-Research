# Game request template and how a request is read (REQ-v1)

**P-2026.10.22-v24.0 · CR-2026.10.22-R2.** Implements REV-21 and the request side of REV-15 of the [framework revamp review](research/verification/review_2026-10-22_framework_revamp/REPORT.md). The Upcoming game blocks in the prompt-1 sport files are owner-entered and are never edited by the framework; this page is how the agent reads them.

## 1. Template

```text
Upcoming game: <competition>, <home> v <away> (or <away> @ <home>)
Scheduled start: <date, time, timezone>   (send the request as early as the line-up or injury news allows)
Supplied contracts: <exact lines, or none>
Research constraints: <anything specific>
Return: the best four, most likely first; add the game winner.
Be exact and honest: every source, every time, every gap.
Use exact distributions; run code simulations only where SIMULATION_PROTOCOL requires them, and print the seed and N.
If research will not finish before the start, issue the fast card first and the full card after.
```

## 2. Reading a request

| A request says | The agent does |
|---|---|
| "Do as many simulations as possible" / "run simulations" | Uses the exact distribution; runs a code simulation only for the contracts in [SIMULATION_PROTOCOL](SIMULATION_PROTOCOL.md) section 2 and prints seed, N and Monte Carlo error; says plainly that no simulation was run where none was needed. Never writes a simulation count it did not execute |
| "Pick your own picks" | Prices every supplied contract and returns the picks block: probabilities, a most-likely list with line difficulty, an information list, and `no strong pick` when nothing reaches 0.65 and nothing moved from the reference |
| "Best 4 in order from most to least likely" | The most-likely list of up to four rows, ordered by final probability; labelled with each row's distance from the centre so that easy lines are visible as easy |
| "Add a potential game winner" | The winner probability for both sides, including a draw where the competition allows one |
| "Take as long as you need" | Research completes (CURRENT_RULES section 5), but a request that arrives close to the start gets the fast card first (FASTCARD-v1) so that something checkable exists before play |
| "Do a retrospective" / "do not do a retrospective" | Retrospectives are prompt 6 and are never part of a card |
| Supplied lines | Contract metadata only: they set the questions asked, not the probabilities answered. The line-implied benchmark (0.5) is written for supplied two-way lines |

## 3. Timing

The agent records the request time, the research start, every source retrieval time, the completion time and the actual issue time, and labels the card `PREGAME`, `POST_START_ISSUE` or `TIMING_UNVERIFIED`. A request sent after the scheduled start can still be researched with pre-start inputs, but it is scored in its own stratum and is not a forecast issued before play.
