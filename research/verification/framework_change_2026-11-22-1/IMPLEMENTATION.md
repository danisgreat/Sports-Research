# Implementation · v29.2 / CR-2026.11.22-R1 · 22 November 2026

Prompt 8, branch `fix/v29.2-request-shape-rules`, stacked on the settlement branch `settle-mini-2026-11-22-p686-p696`
(PR #11, `b85770780`). Owner question: why do card drops fail on GitHub? Classification: procedure (request
registration checks, refusal wording, chat instructions). The plan, scoring, the card format and every registered
request and sealed card are unchanged.

## The six refused drops

| Run (UTC) | Drop | Reason given | Cause | v29.2 |
|---|---|---|---|---|
| 18 Nov 01:00 | NBA POR @ MIN card `20261118DA6D9F6251746B979F5895FA-G0001` | FACTS `travel_km`, `adjustment_basis`: "an observed value needs its source page" | prose before the address in `source` | reason now says: only the address, or `MISSING` with the reason; brief checklist item 1 |
| 18 Nov 23:45 | AHL ROC @ SYR request `…-G0004` | "could not convert string to float: 'ML'" | `ML` in the `line` column | reason: "a moneyline is a WINNER line with the line left empty" |
| 20 Nov 11:48 | CSL soccer card `20261120-495CEEB69E9540938CF6A7DAA7B546B4-G0002` | missing `not_started_observed_at`; `not_started_source` not a page | research began after kick-off; no not-started page | correct refusal; reason now says the card has no pre-start proof; checklist item 4 |
| 22 Nov 00:11 | NHL CBJ @ TOR card `…-G0004` | PICKS L1, L2: both sides required | the request was registered with one side per label, and the card must match the request exactly: no card could pass | registration now refuses a one-sided label |
| 22 Nov 05:56 | NBL Brisbane v Sydney card `…-G0005` | FACTS AWAY `adjustment_basis`: needs its source page | `ANALYST_UNMEASURED_SCENARIO` as the source | as for the first row |
| 22 Nov 08:00 | Jastar U20 Aktobe v Torpedo card `…-G0006` | PICKS L1: handicap lines not equal and opposite (plus availability_basis and a 1.109 probability sum) | the request was registered with "Aktobe +4.5" and "Torpedo -3.5" as one label: no card could pass | registration refuses it; two spreads are two labels (brief) |

A sixth problem registered without an error: the AHL request was re-registered as `…-G0005` with
`Americans -0.5 / Crunch +0.5` and `Crunch -0.5 / Americans +0.5`. With overtime and the shootout included these are one
contract, and P-689 counted one result twice (46-row totals, CARD-TRAIN admitted rows). That sealed record is left
as it is; v29.2 stops new ones.

## Changes

- `ml/forecast_integrity.py`: `line_shape_problems` (one rule set for a requested line, used at registration and by
  `one_chat.check`), `no_draw`, `contract_problems` (shape and one-contract-once, run by `register_request` only for a
  request not already registered identically), and `line_value` so a text line or probability gives a reason, never a
  crash. `request_problems`, which also runs at seal and intake time, keeps its rules apart from that.
- `ml/one_chat.py`: the card's line checks call the shared rule; the FACTS-source and not-started reasons say how to fix them.
- `ml/one_chat_ops.py`: `prepare` reads half-point spreads in no-draw sports as the winner contract and runs `contract_problems`.
- `ml/drop_seal.py`: run-summary detail kept to 3,000 characters (400 cut the second of several reasons).
- Documents: [ONE_CHAT_BRIEF_v29.2](../../external/ONE_CHAT_BRIEF_v29.2.md) (v29.0 retained),
  [drops/README.md](../../../drops/README.md), [RUNBOOK](../../one_chat/RUNBOOK.md) §1 and §7a, prompt 1, prompt stamps, versions.

## Second round (same day, owner review)

- **Unequal spreads.** The owner confirmed "Aktobe +4.5 / Torpedo -3.5" was on purpose. `prepare` registers two
  different spreads as two contracts, each priced on both sides. Both sides of one line written out stay one contract.
  The v29.0 test that expected a refusal was removed.
- **Check drops.** `drops/check/<name>.md` → `one_chat.preflight`, which runs `_block_refusal`, the single home of the
  seal checks (moved out of `_seal_once`). The result is `CHECK_PASSED` or `CHECK_FAILED`, and nothing is published.
- **Fix before first play.** A refused card was never sealed, so a corrected card under a new file name is sealed by the
  unchanged code. This is now documented for chats (`drops/README.md`, brief checklist).
- **Seal margin.** A sealed drop's summary states the minutes before (or after) the scheduled start.
- **Full reasons.** `_seal_once` no longer cuts refusal reasons at 300 characters.
- **Cleanup.** 16 superseded `research/external/` files moved unchanged to `archive/superseded_2026-11-22/` with
  `RELOCATIONS.csv`. v24.19 plan, v24.15 profile/lane briefs and `AUDIT_CHAT_BRIEF_v1` stay because code or tests read
  them. Live links were repointed, and the seven dead `EXTERNAL_RESEARCH_PROTOCOL_V3.md` links and the removed-command
  notes left by the 19 November pruning now point at the `cb97bbc2a` permalinks.
- Tests: `ml/tests/test_v29_2_drops.py` (check drop, fix-then-seal, margin, full reasons), and unequal spreads in
  `test_v29_2_request_shape.py`.

## Third round (two external reviews)

Findings checked first, then acted on: [triage](../external_reviews_2026-11-22/TRIAGE.md).
- `forecast_integrity.winner_by_margin`: ±0.5 equals the winner only on the deciding score (points, goals with the
  shootout goal, runs). This fixes `PlayerX Games -0.5` being read as the tennis match winner.
- `one_chat.incoherent_labels` → `INCOHERENT_ACROSS_LINES` flag, a score report row and a check-drop warning. Never a refusal.
- `one_chat_ops.kit_row_note`: the chat packet names the kit row and any fallback. `sr_kit.py` (frozen identity) is unchanged.
- `one_chat.score`: `as_of` excludes later seals (`SEALED_AFTER_AS_OF`) and later settlements; `timing_label` is
  strict at first play.
- `ml/selection_shadow.py` and SELECTION_SHADOW_PLAN_v1: the registered shadow top-two comparison.
- Small fixes: the scoreboard's v27.0 snapshot is dated; the learning-store protocol link is repointed.
- Tests: `ml/tests/test_v29_2_review_fixes.py` (12).

## Tests

`ml/tests/test_v29_2_request_shape.py` uses the owner's real drops: the `ML` request gets a reason and no crash; the
one-sided NHL request is refused at registration (and is still accepted by the seal-time check, as it was); the AHL
double contract is refused and the single winner label registers; half-point handicaps stay two contracts where a draw
is possible (soccer; hockey on regulation time); an identical earlier registration is still `ALREADY_REGISTERED`;
two different spreads under one label (`Aktobe +4.5 / Torpedo -3.5`) are refused and two labels register;
`prepare` turns `Americans -0.5 / Crunch -0.5` and `Blue Jackets +0.5 / Maple Leafs +0.5` into one winner label and
keeps `Americans -1.5` a handicap; the card reasons name the fix.

## After merging

The `seal-drops` workflow takes its code from `main`, so these checks apply to drops once this and PR #11 are merged.
The copy of `drops/README.md` on `card-drops`, which the chats read, needs the same update pushed there.
