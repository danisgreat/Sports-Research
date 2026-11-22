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
the card. Column rules are in the [runbook](../research/one_chat/RUNBOOK.md) §1. A request is refused (v29.2) if:

- a label has only one side: every line needs both rows (HOME and AWAY, OVER and UNDER, YES and NO);
- `line` holds text such as `ML`: a moneyline is `WINNER` with `line` empty (`ML` belongs in `request_excerpt`);
- a handicap label's two lines are not equal and opposite: two different spreads ("A +4.5", "B -3.5") are two
  labels, each with both sides;
- two labels are one contract. Where no draw is possible (basketball; ice hockey with overtime and shootout;
  baseball with extra innings; tennis), "A ML", "A -0.5" and "B +0.5" all mean "A wins": register one `WINNER`
  label, one row per side, each row keeping its own excerpt.

Examples and the reasons: [ONE_CHAT_BRIEF_v29.2](../research/external/ONE_CHAT_BRIEF_v29.2.md#if-you-register-the-request-yourself-drops-v292).

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

Before pushing, run the [checklist](../research/external/ONE_CHAT_BRIEF_v29.2.md#before-you-hand-over-a-card-v292).
The usual refusals: a FACTS `source` that is not one bare `https://` address (write `MISSING` and the reason
instead), a PICKS label with one side, and a `not_started_source` that is `NONE_FOUND` or not filled in.

## Rules

- A registered request and a sealed card are permanent. Re-pushing different numbers for a sealed key is refused.
- Do not edit or delete earlier drops; push a new file instead.
- Other files in `drops/` are ignored and reported.
