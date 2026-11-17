# Implementation · v29.1 / CR-2026.11.18-R2 · 18 November 2026

Prompt 8, branch `fix/v29.1-owner-request-format` from main `4dd94523d`. Owner question: does the framework support the chats working from the owner's own per-game request template? Classification: procedure (request drafting only). The plan, the registration, scoring and the card format are unchanged.

## Before and after, on the owner's exact text

[Fixture](../../../ml/tests/fixtures/OWNER_REQUESTS_2026-11-18.txt): ten messages, six real games and four unfilled templates.

| Game | v29.0 | v29.1 |
|---|---|---|
| BC Dubai v Spartak Subotica (`Dubai -12.5`) | refused: short name | HANDICAP HOME −12.5, TOTAL 170.5 |
| Kashiwa v Kawasaki | refused: separator line read as a contract | PERIOD 0.5, TOTAL 2.5, CORNERS 10.5 |
| Forejtek v Moeller (`Handicap Games Spread: -3.5`) | refused: colon wording | HANDICAP HOME −3.5, TOTAL 22.5 |
| Malmö v Växjö (`Redhawks ML`, `lakers HC +1.5`) | refused: short names; mixed lines | WINNER, HANDICAP (AWAY +1.5), TOTAL 5.5 |
| Australia v New Zealand | refused: separator line | HANDICAP HOME −3.5, TOTAL 41.5 |
| Alabama @ Vanderbilt | refused: `@` header | Vanderbilt home: HANDICAP HOME +14.5, TOTAL 48.5 |
| Four templates (cricket, rugby union, baseball, Australian rules) | refused: unreadable start or header | refused: "template placeholders" |

All six real games also need an official schedule page. Without one, `prepare` lists the six competitions once in SCHEDULES_NEEDED.csv.

## Tests

Added to `ml/tests/test_v29_parallel.py`:
- an exact full name wins over a shorter name inside the other side's name (`Tennessee` v `Middle Tennessee`; Codex review);
- the owner's text parsed as above;
- the needed-schedules list;
- a short name that fits both sides is refused.

Three earlier tests were updated:
- the summary gained `schedules_needed`;
- a moneyline plus a spread is now two contracts, not a refusal;
- one test text still held the placeholder `Team A bats`.
