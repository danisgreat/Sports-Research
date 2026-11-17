# Implementation · v29.0 / CR-2026.11.18-R1 · 18 November 2026

Prompt 8, branch `feature/v29-parallel-chats` from main `c04b5ddc2`, merged through a pull request with the required checks. Owner order: run about 30–40 games a day across four chats with up to ten games each, and expedite it. Classification: population rules registered before any real game, plus operations; statistical constants unchanged. Versions: MDS-2026.11.18-v29.0 / P-2026.11.18-v29.0 / SCV-2026.11.18-v20.

## Reproduced before the change (v28.0, a ten-game mini)

| Situation | v28.0 result | v29.0 |
|---|---|---|
| Mini sealed after game 3 and after game 10 | All 10 sealed and counted | Unchanged |
| Intake of the chat's later copy with one reformatted earlier card | Whole run NOT_ASSESSABLE | `intake --from-seals` scores the first sealed copies; a changed card is refused at seal and reported |
| Game 3 never settled | Games 4–10 held back indefinitely | Held back for 14 days after its scheduled start; then its unsettled rows are dropped by rule, with a worst-case sensitivity |
| Game 5 without a first-play capture | Whole scoring run stopped | Game excluded (FIRST_PLAY_UNVERIFIED); the run completes |
| One unfinished card in a mini | Whole file refused at seal | Card refused on its own; the mini's other cards sealed |

## Added

`ml/one_chat_ops.py`:
- `prepare`: REQ-v5 messages to REQUEST.txt, EVENT.csv, CONTRACTS.csv, SKELETON.md and CHAT_PACKET.md, with a refusal report.
- `register_folder`: one publication per mini.
- `intake_from_seals`.
- `watch`: the sealing loop.
- `write_templates`: per-sport templates in `research/external/templates/`.

`ml/one_chat.py`:
- card-by-card `seal` with retries;
- robust `_read_outcomes`;
- the settlement deadline (`--as-of`), worst-case fields and new commands.

`ml/drop_seal.py` reports refused cards.

## Tests

`ml/tests/test_v29_parallel.py`, 13 tests:
- drafting four sports, plus six refusal cases;
- a growing mini sealed card by card and scored from sealed copies;
- a retry after a concurrent publication;
- the deadline before and after, and a partly settled game;
- the committed templates.

Updated: four existing tests whose expected error became a refusal or a recorded problem. The Windows job also runs the new file.

## Not changed

The statistical constants (lambdas 0.5, 0.7, 0.9; horizon 600; alpha 0.05; practical mean 0.01), custody, the comparator and the card format are unchanged. No real request or seal existed on `forecast-seals` at registration.
