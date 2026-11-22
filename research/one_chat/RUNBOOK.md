# Current runbook: one chat per game (v29.2)

Authority for ONECHAT_V1 cards: this runbook, CORE and [EVALUATION_PLAN_v29.0](../external/EVALUATION_PLAN_v29.0.md). The reference-first PICKS_V2 and five-lane documents describe separate retained workflows and are not extra prerequisites for a one-chat card. One writer publishes each request/card. Historical records keep their original rules.

## 1. Preserve and register the original request

Keep the owner's original message as a UTF-8 text file. Prepare one EVENT.csv row with:

```text
event_id,sport,competition,home,away,scheduled_start,schedule_source
```

Use the official competition's native ID with its namespace, e.g. `NBA:0022600123`, and the exact official schedule page. A doubleheader needs its actual game identity, not just the teams/date.

Prepare CONTRACTS.csv, one row per side of every requested contract:

```text
label,family,side,line,period,endpoint,action,unit,request_excerpt,baseline_p,baseline_id
```

Period, endpoint, units and action/retirement/overtime rules are explicit. The request excerpt is an exact substring of the original message. Do not add, omit or change a supplied line. Empty line values apply only to winner/yes-no contracts. Registration (v29.2) runs the card's own line rules, so a request that registers can always be carded: every label carries all its sides (HOME/AWAY, OVER/UNDER, YES/NO), a winner row's line is empty (`ML` only in the excerpt), and one contract is registered once. Where no draw is possible (basketball; ice hockey including the shootout; baseball including extras; tennis), a moneyline and either side's ±0.5 are the same winner contract: one WINNER label, each row keeping its own excerpt. An identical earlier registration is still recognised; sealed requests keep the rules they were registered under. A required winner output must also be explicitly included in the retained request. A sporting-data-only baseline may be generated centrally with `python -m ml baseline` from admitted pregame history (see ml/league_baseline.py); freeze its probability and recipe/history/code provenance in these rows before research. If no compatible baseline exists, leave baseline_p empty and put `UNAVAILABLE:<reason>` in baseline_id. Never fill it from a later result or a price.

```text
python -m ml one-chat register-request --source REQUEST.txt --event EVENT.csv --contracts CONTRACTS.csv --card-key <MINI_KEY>-G0001
```

This preserves exact source bytes in Git staging storage and publishes only the registered request data to `forecast-seals`. It never changes or pushes code on main. Keep the original external request. A different request under an existing key is refused. Seal requires an independently published request-index entry before research starts; local staging after a failed publication is insufficient.

## 2. Research and write the card

Give the chat [ONE_CHAT_BRIEF_v29.2](../external/ONE_CHAT_BRIEF_v29.2.md), the kit, the sport's current permitted-source list and do-not-open list. Price both sides of each exact requested contract or retain UNPRICED. Supply the ONECHAT_V1 block, offset-aware research clocks and sport-specific FACTS rows. Keep missing values with their real reasons. No unsupported probability, absence effect, source or model execution is invented.

Capture L5/L10/L20 history, opponent strength, venue, rest/travel, availability/lineup status and adjustment evidence where available. Use the existing LEARNLOG PRIOR_GAMES.csv and AVAILABILITY.csv schemas for raw histories/player rows; retained aggregates are not substitutes for raw game-level lineage. The feature builder preserves missingness and rejects incompatible types. Sources with prices may supply sporting fields only; retain access restrictions and exclude price/tip data from research.

## 3. Seal before first play

```text
python -m ml one-chat seal --card CARD.md
```

The command publishes exact card/request blobs on `forecast-seals` through an isolated Git index. HEAD, the user's index and main are untouched; unrelated work is never published. A failed/non-fast-forward data push is refused without force. Retry only after refreshing and reconciling the append-only registry. Seal refusal or late delivery retains research but provides no prospective qualification. Never overwrite an earlier sealed card; retain corrections as separately identified records and keep the first forecast of record.

### 3a. Sealing from a chat that can only push files (DROP-SEAL-v1)

A research chat that cannot run these commands pushes to the `card-drops` branch instead: the request files to
`drops/requests/<CARD_KEY>/` before research, then the card to `drops/cards/<CARD_KEY>.md` before first play. The
`seal-drops` workflow runs `python -m ml.drop_seal`, which calls the same `register-request` and `seal` code with
`main`'s reviewed code, and marks the drop commit green (done) or red (not sealed, reason in the run summary).
Research may start only after the request's check is green. Rules and file formats: [drops/README.md](../../drops/README.md).
v29.2: a draft pushed to `drops/check/` runs the same checks as a seal (`one_chat.preflight`, sharing
`_block_refusal` with `seal`) and publishes nothing; a refused card, never sealed, may be corrected and pushed as a new
file before first play; each seal's summary states its margin before the scheduled start.
Rehearsals push to `test-card-drops…` and seal to `test-forecast-seals`, which is never scored; a local rehearsal (`ONE_CHAT_SEAL_BRANCH=test-forecast-seals…`) keeps its own staging and pending commits apart from the registered branch.

**Trust.** GitHub runs the copy of `seal-drops.yml` held in the pushed drop commit, with write access to the seal branches. Whoever can push to `card-drops` can therefore also change what that run does, exactly as they could push to `forecast-seals` directly. Neither can backdate anything: the only timing evidence is GitHub's own push time on `forecast-seals`, and `main` accepts changes only through a reviewed pull request. Give drop access only to a chat you would trust to push seals.

## 4. Settle and retain evidence

Settle every side from permitted sources. Save result pages outside the repository, re-hash them, verify definitions, and prefer independent corroboration where available. Record the actual first play from an official page with a retained capture and exact excerpt. If it cannot be established, leave timing unverified; do not substitute scheduled time silently.

OUTCOMES.csv columns are printed by `ml.one_chat.OUTCOME_FIELDS`: card_key, label, side, grade, event_id, actual_start, settled_at, final_source, final_capture_sha256, final_capture_path, first_play_source, first_play_capture_path, first_play_capture_sha256, first_play_excerpt, cancellation_at, cancellation_excerpt. Relative captures resolve under `../one_chat_captures` or an explicit `--captures` directory. For a game officially cancelled before any play, void every contract, leave actual_start empty and retain the official cancellation capture plus cancellation_at and its exact cancellation_excerpt. Do not invent first-play evidence; this terminal game is excluded without holding back later games. Hash checks verify bytes, not source truth; settlement remains an evidence-based review. Preserve originals and append corrections.

## 5. Intake, score and build training candidates

```text
python -m ml one-chat intake --drop <original drop> --out research/one_chat/intake/<run>
python -m ml one-chat receipts
```

Commit intakes, manifests and outcome files through a reviewed main-branch change. Scoring independently re-fetches GitHub activity and reconstructs forecast values from the exact published blobs. A locally edited push-receipt mirror cannot establish a server time. Fetch the `forecast-seals` branch before importing data from another checkout.

```text
python -m ml one-chat score --intake <ALL intake folders> --outcomes <ALL outcomes files> --out research/one_chat/scores/<run>
python -m ml.evidence_status --training research/card_training/<latest-run> --intake <ALL intake folders> --out research/verification/<new-evidence-run>
```

For an unsealed request that produces no forecast, publish an explicit terminal disposition with `python -m ml one-chat disposition --card-key <key> --status NO_FORECAST --reason "<real reason>"`. This cannot remove a sealed card.

Account for every registered request, including refused, unpriced, unsealed, late, unresolved and excluded records. Omitted sealed games make a run NOT_ASSESSABLE. Never select folders after inspecting wins/losses. An earlier pending game holds later games back. After the first 100 freeze, pass `--cohort <first run>/COHORT.csv`; it must equal the actual first 100. A secondary checkpoint is available at 100 immediately, with no eight-week requirement.

The evidence report accounts for every historical card, preserves its original cohort, copies historical study scores and builds typed feature candidates with source/time/unit/missingness checks. It does not manufacture missing historic research. Verify/ingest sporting finals through the existing LEARN-v1 procedure only when its lineage and endpoint gates pass. Report candidate, admitted and excluded data separately. CARD-TRAIN-v1 still runs after every canonical import; historical evidence and prospective certification have separate labels.

## 6. Publish framework changes safely

Changes to code/rules go through a branch/PR and the `framework-validation` required check. CI runs static checks, formatting on the new integrity modules, schema/custody end-to-end fixtures and the full regression suite. Main protection requires the check and blocks force pushes/deletion, including administrators. Forecast data seals use the separate branch and do not bypass code review.

Freeze this registered method until its declared verdict; a statistical change restarts the registration. Richer hierarchical or ML models remain shadow studies until point-in-time feature data, chronological/held-out-competition comparisons and prospective evidence justify use. Dataset creation or a passing test suite does not prove prediction skill.

## 7. Several chats a day (v29.0): four chats, up to ten games each

Write each chat's requests as one text file, one REQ-v5 message per game (add `Schedule: <official schedule URL>` to a message, or keep one row per competition in a schedules CSV with columns `competition,schedule_source`; an optional `Native ID: <id>` line gives the competition's own match ID).

```text
python -m ml one-chat prepare --message CHAT1.txt --mini MINI21 --out <prep folder>/MINI21 --schedules SCHEDULES.csv
python -m ml one-chat register-requests --folder <prep folder>/MINI21
```

**Timing (v29.2).** Send each request 30 to 60 minutes before its start. Between 18 and 22 November every request in
the live minis was registered within ten minutes of the start (one after it), research ran as short as 81 seconds,
and two seals landed after the scheduled start. Earlier requests leave time for confirmed lineups, a check drop and
a seal before first play. The packet names the kit row each game reaches (v29.2) and any family-prior fallback.

`prepare` reads every message exactly as written and writes, per game, REQUEST.txt (the message itself), EVENT.csv, CONTRACTS.csv and SKELETON.md, plus one CHAT_PACKET.md in start order; a message it cannot read is listed in PREPARE_REPORT.csv with the reason and is not registered. `register-requests` registers and publishes the whole mini in one push. Paste CHAT_PACKET.md and [ONE_CHAT_BRIEF_v29.2](../external/ONE_CHAT_BRIEF_v29.2.md) into the chat only after the publication shows on GitHub. Use a new mini key per chat per day (MINI21, MINI22, …); never give the same game to two chats.

Save each chat's cumulative mini into one folder (for example `C:/chat-minis/MINI21.md`) whenever the chat hands over a card, and leave the sealer running:

```text
python -m ml one-chat seal --watch C:/chat-minis
```

Each pass (every two minutes) seals every new finished card in every mini, card by card: an unfinished, changed or unregistered card is reported and skipped, and the mini's other cards are still sealed. A card must be sealed before its own game's first play; the earliest games come first in each packet for this reason.

After settlement, score from the sealed copies, never from the chats' later files. The registered rank's top two are
also compared with the separately registered shadow selection ([SELECTION_SHADOW_PLAN_v1](../external/SELECTION_SHADOW_PLAN_v1.md),
`python -m ml.selection_shadow score … --coverage <score>/COVERAGE.csv --registered-at <plan publication>`), which never
changes a card or the registered score:

```text
python -m ml one-chat intake --from-seals --out research/one_chat/intake/<run>
python -m ml one-chat score --intake research/one_chat/intake/<run> --outcomes <every OUTCOMES.csv> --out research/one_chat/scores/<run>
```

A row still unsettled 14 days after its scheduled start is dropped by rule; the run reports the worst case with every dropped line counted as lost. A game whose first play cannot be verified is excluded, and a capture problem is reported without stopping the run. [Plan](EVALUATION_PLAN_v29.0.md).

### 7a. Writing the requests (v29.1)

Write the requests as you always do, one `Upcoming …` message per game, separated by dashed lines if you like. `prepare` reads:
- short side names (`Dubai -12.5` for BC Dubai, `lakers HC +1.5` for Växjö Lakers HC); a name that fits both sides is refused;
- `Handicap Games Spread: -3.5` and similar wordings, with or without a colon;
- `Away @ Home` headers (the second name is the home side); with `vs` and no `Home side / venue` line, HOME and AWAY are the first- and second-named sides, and the chat prices them by name;
- a moneyline on one side and a spread on the other (`Redhawks ML`, `lakers HC +1.5`) as two contracts, each priced on both sides.
- (v29.2) two different spreads (`Aktobe +4.5`, `Torpedo -3.5`) as two contracts, each priced on both sides (both sides of one line, `A -3.5` and `B +3.5`, stay one contract);
- (v29.2) where no draw is possible, half-point spreads (`Americans -0.5`, `Crunch -0.5`; `Blue Jackets +0.5`) as the one winner contract they settle as, priced on both sides; a real spread (`Americans -1.5`) stays a handicap.

A message that still holds template placeholders (`Team A`, `X.X`, `Day Month Year`) is refused and nothing is guessed.

**Schedule pages, once per competition.** Every request needs its competition's official schedule page. Add a `Schedule: <url>` line to the message, or keep one row per competition in `research/one_chat/SCHEDULE_SOURCES.csv` (`competition,schedule_source`). A row also covers every competition that starts with it, so `Challenger` covers `Challenger Monastir - Semi Finals`. When pages are missing, `prepare` writes `SCHEDULES_NEEDED.csv` listing each competition once; fill it in, add the rows, and run `prepare` again.
