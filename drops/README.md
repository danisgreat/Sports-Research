# Drop folder (DROP-SEAL-v1)

A research chat that can push to GitHub but cannot run this repository's commands uses this folder on the
**`card-drops`** branch. Never push to `main` or `forecast-seals`. Every push here runs the `seal-drops` workflow,
which registers requests and seals cards with the unchanged ONE-CHAT-v3 code
([runbook](../research/one_chat/RUNBOOK.md)). Rehearsals use a branch named `test-card-drops…`; they seal to
`test-forecast-seals` and are never counted.

## 1. Register the request, before any research

Push the three files for one game in one commit:

```text
drops/requests/<CARD_KEY>/REQUEST.txt     the owner's original message, unchanged (UTF-8)
drops/requests/<CARD_KEY>/EVENT.csv       event_id,sport,competition,home,away,scheduled_start,schedule_source
drops/requests/<CARD_KEY>/CONTRACTS.csv   label,family,side,line,period,endpoint,action,unit,request_excerpt,baseline_p,baseline_id
```

`<CARD_KEY>` is `<MINI_KEY>-G0001`, `-G0002`… (letters, digits, `_` and `-` only) and must equal the `card_key` in
the card. Column rules are in the [runbook](../research/one_chat/RUNBOOK.md) §1.

**Wait for the green `seal-drops` check on that commit before starting research.** The card's `research_start_at`
must be later than the time GitHub published the registration; research started earlier makes the card unsealable.
A request pushed in the same commit as its card is always refused for this reason.

## 2. Seal the card, before first play

Push the finished card, byte for byte as written, as one file:

```text
drops/cards/<CARD_KEY>.md
```

It must contain the `ONECHAT_V1` block for the registered key. A green check means it was sealed; GitHub's push time
on `forecast-seals` is the timing evidence, not the drop time. Push at least 30 minutes before the scheduled start.
A red check means it was **not** sealed: the run summary gives the reason.

## Rules

- A registered request and a sealed card are permanent. Re-pushing different numbers for a sealed key is refused.
- Do not edit or delete earlier drops; push a new file instead.
- Other files in `drops/` are ignored and reported.
