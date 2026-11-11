# External research lanes (EXT-v1)

**MDS-2026.11.11-v24.13 · CR-2026.11.11-R1 · P-2026.11.11-v24.11.** Owner instruction, 11 November 2026: implement the review's recommendations for the owner's parallel ChatGPT research chats. This page **reinstates the external route** (it supersedes REQ-v3's retirement of 8 November 2026 for research, not for issuing cards) in a form whose output can be checked, merged and scored. The card itself is still made, linted, ledgered and frozen in this repository (CORE §§2–3). Related: [GAME_REQUEST_TEMPLATE](GAME_REQUEST_TEMPLATE.md) (REQ-v5), [SOURCES](SOURCES.md) SRC-ALT-v3, SOCIAL-v2 and OWNER-CAPTURE-v1, [SIMULATION_PROTOCOL](SIMULATION_PROTOCOL.md) KIT-v1.

## 1. Why the route was retired, and what changed

On 8 November the chats lost the evidence test: their cards tied or lost to the league baseline, none had a checkable pre-start time, their research could not be captured, and their references were hand-computed. Each of those is now fixed by a rule below, not by trust:

| Failure on 8 November | Fix in EXT-v1 |
|---|---|
| Five chats repeated the same search and the same mistakes | Five **lanes** with different jobs (§2) |
| Chats read different versions of the rules | Every request names one **commit SHA**; every return repeats it (§3) |
| Hand-computed references and "simulations" that were never run | The **kit** does every number and prints a receipt; the repository re-runs it (§5) |
| Research could not be captured | One fixed **LANE_RETURN** block per chat, saved byte for byte and merged by code (§4) |
| No checkable pre-start time | The card is frozen and pushed **here** (§6) |
| Chats opened sites that refuse AI readers | A per-reader **do-not-open list** and robots-first rule (§7) |
| About 400 KB of reading per card | One-page **external profile** plus the sport's lane brief (§3) |

## 2. The lanes

One request, up to five chats, each with one lane. The owner may run fewer; L1 and L5 are the minimum useful pair.

| Lane | Job | Returns |
|---|---|---|
| **L1** Availability | Both sides' confirmed starters, bench, injuries, illness, suspensions and late changes, at their publication windows (ROSTER_AVAILABILITY_PROTOCOL); goalie, pitcher or quarterback where the sport has one | EVIDENCE |
| **L2** Results and form | Both sides' games after the date the repository's history pack runs to, then L5/L10/L15/L20 and season with true n (HISTORICAL_SOURCE_PROTOCOL) | EVIDENCE |
| **L3** Conditions and rules | Venue, weather in the match window, officials, rest and travel, stage, endpoint and settlement rules (overtime, extra time, ties, retirement, DLS) | EVIDENCE |
| **L4** Re-check | L1's decisive facts again, from **different registrable domains** than L1 used, including local-language and official social sources (SOCIAL-v2) | EVIDENCE |
| **L5** Pricing | Starts from the repository's frozen Reference block, applies only effect-table sizes for facts in the merged evidence, prices every supplied line with the kit | PROBABILITIES with kit receipts |
| **FULL** | The owner's older one-chat-does-everything run, still accepted | EVIDENCE and PROBABILITIES |

The repository agent may itself do L5 after the merge (preferred: it runs the same kit and needs no receipt check).

## 3. What the owner sends

1. **Start the mini here first** (prompt 2) or name the active mini. The agent prints the commit SHA to use.
2. **Ask here for the reference and the packs:** "reference and packs for <game>". The agent runs `python -m ml reference tier`, the reference stage, and `python -m ml history-pack` for both sides, and pastes back a short block: the Reference block, the pack windows, the shared **event key** (`python -m ml external event-key`) and the commit SHA.
3. **Paste into each chat:** the filled REQ-v5 request (one game per message), the lane line ("Lane: L1"), the block from step 2, and the instruction to read the [external profile](research/external/EXTERNAL_PROFILE_v24.13.md) and the lane brief. Upload the kit files listed in [research/external/README](research/external/README.md) to each chat (or once to a ChatGPT Project).
4. **Bring each chat's LANE_RETURN block back** and paste it here: "intake returns for <event key>".

The **event key** is `EV-YYYYMMDD-SPORT-A-B`: the AEDT date of the request's estimated start and the two sides in request order, so every chat derives the same key without looking anything up (`ml.external.event_key`). It links the five chats' minis to one event; only the merged card is scored. A chat that keeps its own notes uses its own mini key, never a canonical ID.

## 4. The return block and the merge

Every chat ends with exactly one block, in this shape (columns are fixed; `python -m ml external check` enforces them):

```text
<!-- BEGIN LANE_RETURN -->
event_key: EV-20261110-BKB-CHIBAJETS-OSAKAEVESS
lane: L1
chat_label: CHAT-1
profile_version: v24.13
commit: <the 40-character commit the chat read>
reader: CHATGPT_BROWSING
started_at: 2026-11-10T08:00:00+11:00
completed_at: 2026-11-10T08:40:00+11:00

[EVIDENCE]
side,field,value,source_url,source_class,published_at,retrieved_at,confirmation,notes
[PROBABILITIES]
label,family,side,line,line_source,w,p,l,final_p,kit_receipt_sha256
[ACCESS_LOG]
url,result,checked_at,notes
<!-- END LANE_RETURN -->
```

- `side` is HOME, AWAY or EVENT. `field` names one fact; a player's status is `status:<Player Name>`. Single-valued fields (venue, start, starting goalie or pitcher, referee, toss, weather, lineup status, surface) and every `status:` field are checked for conflicts.
- `source_class`: FIELD_OWNER, LEAGUE, CLUB, OFFICIAL_SOCIAL, PROVIDER, MEDIA, REPORTER_SOCIAL or OWNER_CAPTURE. `confirmation`: OFFICIAL_CONFIRMED, REPORTED, PROJECTED or NOT_APPLICABLE. Projected is never confirmed.
- `published_at` is the source's own time, or UNKNOWN; `retrieved_at` is when the chat read it. Unknown facts stay out of EVIDENCE: a missing field is not a fact.
- Probabilities come only from a kit receipt (`kit_receipt_sha256`); a hand number is refused.
- `ACCESS_LOG.result`: OPENED, BLOCKED_BY_RULES, RULES_UNKNOWN, ON_DO_NOT_OPEN_LIST, TECHNICAL_FAILURE or NOT_FOUND.
- Market terms anywhere are refused (MARKET_BLIND).

**Intake here (prompt 1):** save each return byte for byte under `research/active_minis/received/<event key>/`, run `python -m ml external check` on each, then `python -m ml external merge --event-key K --returns research/active_minis/received/<K>/ --out <new folder> --do-not-open research/external/access/CHATGPT_DO_NOT_OPEN_v24.13.csv`. The merge:

- pools facts by side, field and value; a fact is **CORROBORATED** only with two different registrable domains (two pages of one site, or a copied feed, are one source);
- lists **CONFLICTS** (a single-valued field with two values): the card resolves them at the field owner or prices them as a declared scenario mixture, never by majority;
- pools pricing runs per contract: median, minimum, maximum, spread; a contract is **EXTERNAL_DISAGREEMENT** when the runs fall on both sides of 0.5 or spread more than 0.10;
- writes the access log, so chat-side blocks and failures are kept by reader (§7);
- refuses a return that fails its check, and says why.

## 5. Pricing (one coherent distribution, then a consensus check)

The card's final probabilities come from **one** pricing of the **merged** evidence: the frozen reference, plus one ledger row per confirmed fact with its effect-table size (ADJUSTMENT_LEDGER_PROTOCOL), priced by the kit or by `ml.reference` here. Averaging five independently guessed probabilities is not the method: it would break the adjustment ledger, whose counterfactuals score each fact.

Replicate pricing runs (several L5 or FULL returns) are a **consensus check**. Where they disagree on a supplied contract (EXTERNAL_DISAGREEMENT), that contract is written in the picks header `external_disagreement:` and may not be ranked (the linter refuses it), whatever its probability. This is a pre-registered abstention rule (EXT-H1 in the [hypothesis register](HYPOTHESIS_REGISTER.md)); it is kept only if it improves the paired score.

Every pricing return's receipts are re-run with `python -m ml kit verify --receipt FILE`; a receipt that does not reproduce is not used, and the agent re-prices here.

## 6. Freeze and scoring

The merged card is written into the active mini here, linted (`rank_scope`, `event_key`, `external_runs`, `external_disagreement` headers), ledgered, frozen by `python -m ml pregame run`, logged (LEARNLOG-v1, availability for both sides) and pushed. Only the pushed commit makes it a checkable pre-start forecast. The chats' own notes are research inputs, never issued cards. Scoring is unchanged: paired proper scores against the reference, the league baseline and the line-implied 0.5, within strata.

## 7. Sources, blocks and social media in the chats

- **Check first, then open.** A chat opens a site only when it is on its sport's permitted list ([research/external/sources/](research/external/sources/README.md)), or after reading that site's `robots.txt` itself and finding the ChatGPT-User group (or, if none, the `*` group) allows the path. Opening a page to find out whether it is blocked is not allowed: by then it has been read.
- **Never** open a host on [CHATGPT_DO_NOT_OPEN_v24.13.csv](research/external/access/CHATGPT_DO_NOT_OPEN_v24.13.csv), and never reach one another way (mirror, cache, reader service, embed, archive, translation proxy). Use the `use_instead` column or find a permitted alternate (SRC-ALT-v3).
- **Technical failures** (403, script-only page, timeout) on an allowed site are logged as TECHNICAL_FAILURE and the chat moves on; it never retries through another route.
- The lists are re-checked **weekly** (`valid_until`); a list past its date is refreshed here before the next batch (`python -m ml source-audit --lists`).
- **Social media** (SOCIAL-v2, SOURCES §1.8): official club, league and federation accounts count as the field owner; a reporter counts as one secondary source needing a second domain. Use them in this order: the club's or league's own site and match centre; the reporter's outlet article; permitted platforms (Bluesky, YouTube, public Telegram channels the club's site links); and, for X, Instagram and Facebook (all refuse AI readers), an **owner capture**.
- **Owner capture (OWNER-CAPTURE-v1).** The owner opens a post or page in their own browser and pastes its exact text, link, account and the post's own time into a file under `research/active_minis/received/<event key>/OWNER_CAPTURE_<n>.md`. It enters EVIDENCE with source_class OWNER_CAPTURE, counts as one source, and still needs corroboration for a decisive fact. The owner is responsible for the platform's own terms; no agent opens the page.

## 8. Limits

- The kit and the lists are tested here; a ChatGPT sandbox or browser can behave differently (package versions, blocked fetches). Failures are logged, not hidden.
- A chat's commit, times and statements are its own claims until the repository re-checks them. Only facts the merge admits, and numbers the kit receipt reproduces, are used.
- EXT-H1 (abstain on disagreement) and the lanes' value are unproven; they are scored like every other component and dropped if they do not help (owner decision, 8 November 2026).
