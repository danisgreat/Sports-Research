# The measured-card assessment (ONE-CHAT-v1 / EVAL-ONECHAT-v1 / AUDIT-ANYTIME-v1)

Owner order, 16 November 2026 (CR-2026.11.16-R2, MDS-2026.11.16-v25.0). Registered before any game of the cohort. This plan supersedes [EVALUATION_PLAN_v24.19](EVALUATION_PLAN_v24.19.md) for new games: the FIVE_LANES against SINGLE_RESEARCH comparison never ran on a real game and no longer matches how the owner works (one chat per game). Its registration, and every earlier plan, stay on file unchanged; no game was ever admitted to them.

## What is measured

One research chat writes one card per game under [ONE_CHAT_BRIEF_v25.0](ONE_CHAT_BRIEF_v25.0.md). The card ends with an `ONECHAT_V1` block. `python -m ml one-chat intake` reads the block as written; `python -m ml one-chat score` joins the settled grades.

- **Forecast identity:** ONE_CHAT:v25.0 — the probabilities in the card's PICKS table, unchanged.
- **Comparator:** the constant 0.5 on every supplied line that has a line value (handicaps, totals, team totals, period and corner lines). It is computed here, never by the chat. A Brier score of 0.25 is what 0.5 earns.
- **Primary measure:** for each game, the mean Brier score of the card's priced, decisive rows on those lines, minus 0.25. Games are averaged equally. The 95% interval is a t interval over games.
- **Registered criterion:** the mean is -0.01 or lower and the whole interval is below zero. The report says MEETS_REGISTERED_CRITERION or DOES_NOT_MEET_REGISTERED_CRITERION; either is a finding, not a promotion.
- **Secondary, reported beside it:** calibration by band and the calibration slope; Rank 1 and Rank 2 results (rank is the card's own highest stated numbers, one side per line); winner rows; the card against a league base rate on the rows where one was frozen at import (`--baseline`); results by sport, contract family and timing; the share of supplied lines that carry a number.

## Which games count

A game is eligible when all of these hold:

1. Its card was ADMITTED by the intake (complete block, both sides of every line, coherent numbers, sporting fields only). When two cards cover one game, the earliest saved file is the card of record.
2. Every supplied line with a line value carries a number. A card with an UNPRICED supplied line is kept and reported, and is not in the cohort.
3. Timing (TIMING-v3): the research began, and the not-started observation was made, at or before the official first play, and `outcome_exposure` is NONE. The saved time of the file is reported as a stratum (PRE_START_SAVED or PRE_START_RESEARCH_SAVED_LATER); it does not exclude a game, because research is never hurried to beat a start.
4. Every row is terminally settled (WIN, LOSS, PUSH or VOID) from a result page whose saved capture is recorded by SHA-256, and at least one priced lined row is decisive.

Count games, not picks, chats or files.

## The cohort and when it is assessed

- The cohort is the **first 100 eligible games in order of settlement** (the time the game's last row was settled; card key breaks ties). No calendar minimum and no wait for a week to finish.
- Before 100, the command reports PROGRESS with the counts and the running figures.
- At 100 it reports READY, writes COHORT.csv and gives the finding. Later runs reuse that file with `--cohort`. The cohort is not enlarged or replaced to change the answer.
- **On request at any count (AUDIT-ANYTIME-v1):** `--on-request` scores every eligible game to date with status AUDITED_ON_REQUEST and finding NOT_ASSESSED. It never decides the assessment.

## Hypotheses tested on this cohort

Registered on 16 November 2026 from the [audit of P-001 to P-685](../verification/retrospective_2026-11-16-1/RETROSPECTIVE_REPORT.md), before any cohort game. The intake flags each pattern on the favoured side of a line without changing the card; the score report prints flagged against unflagged results.

| ID | Flag | Question |
|---|---|---|
| H-NODIR | NO_DIRECTION (stated p within 5 points of 0.5) | Do these rows win at a rate different from 50%, and does Rank 1 improve without them? |
| H-BAND | band 0.60 to 0.65 | Does the band still win about 10 points below its stated rate? |
| H-AVAIL-CHAT | UNMEASURED_AVAILABILITY_PRICED | Do priced lines resting on an unmeasured absence do worse than the rest? |
| H-OWN-EVIDENCE | CONTRADICTS_OWN_CENTRE | Do numbers on the wrong side of the card's own centre do worse? |
| H-SPORT | by sport | Are tennis, American football and Australian rules numbers worse than 0.5? |
| H-PERIOD | by family and side | Do period and corner Overs win more than Unders? |

No hypothesis changes a card or a rank during the cohort. After the assessment, one release may adopt what passed.

## The freeze

FREEZE-v1 now runs to this assessment: no statistical, selection or format change to the card until the first 100 eligible games are assessed. Bug fixes that change no output, source refreshes, data collection, records and shadow studies continue.

## Limits stated in advance

The interval treats games as independent; games on the same day, with the same teams or in the same competition are not, so it is optimistic. The comparator 0.5 measures skill on the supplied line, not against any market, and nothing here uses a price. File saved times are the owner's custody evidence, not proof of publication. A finding on 100 games across many sports says little about any one sport.

## Commands

```text
python -m ml one-chat intake --drop "<owner drop folder>" --out research/one_chat/intake/<YYYY-MM-DD-n>
python -m ml one-chat score --intake research/one_chat/intake/* --outcomes <package>/OUTCOMES.csv --out research/one_chat/scores/<YYYY-MM-DD-n> [--on-request]
python -m ml one-chat score ... --cohort research/one_chat/scores/<first READY run>/COHORT.csv --out <later audit>
```
