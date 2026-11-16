# Current runbook: one chat per game (v27.0)

Authority for ONECHAT_V1 cards: this runbook, CORE and [EVALUATION_PLAN_v27.0](../external/EVALUATION_PLAN_v27.0.md). The reference-first PICKS_V2 and five-lane documents describe separate retained workflows and are not extra prerequisites for a one-chat card. One writer publishes each request/card. Historical records keep their original rules.

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

Period, endpoint, units and action/retirement/overtime rules are explicit. The request excerpt is an exact substring of the original message. Do not add, omit or change a supplied line. Empty line values apply only to winner/yes-no contracts. A required winner output must also be explicitly included in the retained request. A sporting-data-only baseline may be generated centrally with `python -m ml baseline` from admitted pregame history (see ml/league_baseline.py); freeze its probability and recipe/history/code provenance in these rows before research. If no compatible baseline exists, leave baseline_p empty and put `UNAVAILABLE:<reason>` in baseline_id. Never fill it from a later result or a price.

```text
python -m ml one-chat register-request --source REQUEST.txt --event EVENT.csv --contracts CONTRACTS.csv --card-key <MINI_KEY>-G0001
```

This preserves exact source bytes in Git staging storage and publishes only the registered request data to `forecast-seals`. It never changes or pushes code on main. Keep the original external request. A different request under an existing key is refused. Seal requires an independently published request-index entry before research starts; local staging after a failed publication is insufficient.

## 2. Research and write the card

Give the chat [ONE_CHAT_BRIEF_v27.0](../external/ONE_CHAT_BRIEF_v27.0.md), the kit, the sport's current permitted-source list and do-not-open list. Price both sides of each exact requested contract or retain UNPRICED. Supply the ONECHAT_V1 block, offset-aware research clocks and sport-specific FACTS rows. Keep missing values with their real reasons. No unsupported probability, absence effect, source or model execution is invented.

Capture L5/L10/L20 history, opponent strength, venue, rest/travel, availability/lineup status and adjustment evidence where available. Use the existing LEARNLOG PRIOR_GAMES.csv and AVAILABILITY.csv schemas for raw histories/player rows; retained aggregates are not substitutes for raw game-level lineage. The feature builder preserves missingness and rejects incompatible types. Sources with prices may supply sporting fields only; retain access restrictions and exclude price/tip data from research.

## 3. Seal before first play

```text
python -m ml one-chat seal --card CARD.md
```

The command publishes exact card/request blobs on `forecast-seals` through an isolated Git index. HEAD, the user's index and main are untouched; unrelated work is never published. A failed/non-fast-forward data push is refused without force. Retry only after refreshing and reconciling the append-only registry. Seal refusal or late delivery retains research but provides no prospective qualification. Never overwrite an earlier sealed card; retain corrections as separately identified records and keep the first forecast of record.

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
