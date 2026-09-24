# Sports Research Audit Reconciliation and Cricket Toss/Pitch Source Protocol

> **Implementation status — 2026-09-21:** the accepted findings in this audit have now been implemented prospectively in the root authority under **MDS-2026.09.19-v4.3 / CR-2026.09.21-1**. `AUDIT_IMPLEMENTATION_2026-09-21.md` is the implementation/disposition ledger and `CONTROL_MANIFEST_2026-09-21.md` is the post-write receipt. Any wording below that describes changes as future/pending is preserved as the pre-implementation audit record and is superseded on implementation status by those two files.

**Date:** 2026-09-21  
**Scope:** Reconcile still-valid prior-audit findings against the current Google Drive authority; repair cricket toss/pitch-source methodology; document implementation-ready changes without modifying the read-only Google Drive.  
**Drive authority reviewed:** current root Markdown set in `Sports Research`, including `METHOD.md`, `RULES_CRICKET.md`, `DATA_SOURCE_REGISTER.md`, `SOURCES.md`, `UPCOMING_GAME_RESEARCH_GUIDE.md`, `AUDIT_IMPLEMENTATION_2026-09-19.md`, prior audits, and the current mini log.  
**Repository source also reviewed:** `danisgreat/Sports-Research` on GitHub. The GitHub copy is materially older than the current Drive authority, so it must not silently supersede the Drive version.

---

## 1. Audit reconciliation

### 1.1 Keep — correct and already substantially implemented

The following earlier findings remain valid and should continue unchanged:

1. **Market-independent forecast before line comparison.**  
   User-supplied totals/spreads are contract metadata only until the sporting forecast/distribution has been frozen. Odds, market consensus, betting previews, picks, tips and fantasy/DFS content do not drive the sporting forecast.

2. **Source-lineage accounting.**  
   Multiple websites displaying the same upstream feed are one lineage, not independent confirmation. Search snippets are discovery only.

3. **Point-in-time evidence.**  
   Decision-driving evidence must satisfy `known_at <= cutoff_at`. Post-match reporting cannot be backfilled into a pre-game card unless it can be shown that the information was already available before the cutoff.

4. **Three independent reliable lineages for a new event and terminal settlement.**  
   Mirrors, syndicated copies and multiple pages from one feed do not satisfy the requirement.

5. **Exact-match strip report is distinct from weather and venue history.**  
   Weather cannot be used to invent grass, hardness, pace, seam, turn or deterioration.

6. **Toss decision is only weak circumstantial context.**  
   A decision to bat/bowl can inform a conditions branch, but it is not itself a pitch report and cannot independently create a signed Over/Under or winner lean.

7. **Previous same-venue match is a different strip unless same-strip reuse is explicitly confirmed.**  
   It can inform ground/competition context, but must not be treated as today's strip.

8. **Debutant gate.**  
   Where the ESPN cricket summary identifies a debutant, treat the player as `NO_PRIOR_FORMAT_RECORD`; do not fabricate a phase contribution from unavailable history.

9. **No mechanical rebound/bounce-back rule.**  
   Recent high/low outcomes do not create a “due” adjustment. Recency only moves the forecast through an identified mechanism, regime change or time-ordered model.

10. **No additive cricket-tail shortcut.**  
    Do not add a batting high to an opponent concession statistic and call the result a plausible joint tail. Build one conditional innings/phase process and avoid double-counting the same run quantity.

### 1.2 Keep, but repair the implementation

The following ideas were correct but are only partially or inconsistently implemented:

#### A. Pitch ladder drift
`RULES_CRICKET.md` contains a later addendum describing **Rung 7** (preceding same-venue match) and **Rung 8** (toss broadcast), while earlier sections, `SOURCES.md`, and `UPCOMING_GAME_RESEARCH_GUIDE.md` still refer to a **six-rung** ladder.

**Repair:** replace the ambiguous “six vs eight” wording with the two-ladder protocol in Section 2 below:
- a dedicated **TOSS FACT ladder**;
- a dedicated **STRIP/PITCH EVIDENCE ladder**.

This preserves the useful earlier audit findings without double-counting the toss broadcast.

#### B. Rung 6 contradiction
`DATA_SOURCE_REGISTER.md` correctly states in a later correction that a same-format venue baseline can be unavailable, but its ladder table still says the venue baseline is “always computable.”

**Repair:** `RUNG_6_NOT_AVAILABLE` / `INSUFFICIENT_VENUE_HISTORY` is a legitimate outcome. Use a broader comparable prior only if its population is stated; widen uncertainty rather than inventing a same-venue sample.

#### C. Toss-broadcast duplication
The older ladder already places a toss-time broadcast pitch report at the top, while the later audit also adds the toss broadcast as “Rung 8.”

**Repair:** the toss broadcast is not two independent rungs. It is:
- a primary toss source in the TOSS ladder; and
- a primary exact-match pitch source in the STRIP ladder when a named pitch assessment is actually given.

#### D. Late-source latency
The current `P-482` card still had unverified toss/XI/strip close to the scheduled start. That is a retrieval-latency problem, not permission to guess.

**Repair:** add the late refresh sequence in Section 4 and explicitly query official video/broadcast and specialist live-commentary transcript lanes during the toss window.

### 1.3 Do not reintroduce — contradicted or superseded

The following older ideas should remain rejected:

- treating “at least one of Over/Under won” as meaningful forecast performance when both complementary sides were selected;
- treating second-highest/second-lowest innings as “modes”;
- assuming a venue-history rung must exist;
- counting front ends with the same upstream feed as independent sources;
- treating a generic automated “Pitch Condition” block as a named observed strip report;
- treating a captain's toss decision as proof that the pitch is good/bad for batting;
- using generic fantasy/tipping/prediction pages as pitch evidence;
- using market lines, betting picks or fantasy projections as sporting evidence;
- forcing a permanent model rule from one unusual match without mechanism-level justification.

---

# 2. Cricket source protocol — separate TOSS and STRIP ladders

## 2.1 TOSS FACT ladder

The toss is a factual field. Search in this order and stop only after the material field is verified or the ladder is exhausted.

| Rank | Source lane | Use | Notes |
|---|---|---|---|
| T1 | **Official competition/national-board exact-match centre or board-branded scorecard** | Toss winner, bat/bowl decision, XIs | Preferred field-owner route |
| T2 | **Official competition/board verified video or rights-holder broadcast** | Toss, captain interview, team news | Capture timestamp and exact match |
| T3 | **Official team/competition live blog or timestamped official post** | Toss/XI corroboration | Must be directly opened; search snippet alone is not evidence |
| T4 | **Structured cricket endpoint already admitted in the source register** (for example the ESPN cricket summary route where covered) | Toss note, XIs, innings state | ESPN/ESPNcricinfo variants are one lineage |
| T5 | **High-quality exact-match specialist scorecard/commentary** | Toss corroboration | Examples: Cricbuzz, ESPNcricinfo, board-branded CricketArchive/NV Play surfaces where applicable |
| T6 | **Reputable independent match reporting** | Fallback/corroboration | Match identity/date/venue must match exactly |

If the ladder does not verify the toss, record:

`TOSS_STATUS = NOT_VERIFIED_AFTER_SEARCH`

Do **not** infer the toss winner merely from which side bats first.

## 2.2 STRIP/PITCH EVIDENCE ladder

Only Rungs P1–P5 can establish a current exact-match strip observation/report. Rungs P6–P8 are context only.

| Rank | Source lane | Evidence class | Can set `STRIP_STATUS=OBSERVED`? |
|---|---|---|---|
| P1 | **Named current-match broadcast pitch report** by presenter, curator/groundsman or captain; official video/live feed/transcript | `EXACT_MATCH_OBSERVED` | Yes |
| P2 | **Current curator/groundsman/venue/board statement** about the exact strip | `EXACT_MATCH_OBSERVED` | Yes |
| P3 | **Official board/competition toss report or preview** quoting a captain/coach/curator on the wicket/strip | `EXACT_MATCH_REPORTED` | Yes |
| P4 | **Specialist live commentary explicitly transcribing a named broadcast pitch report** | `EXACT_MATCH_REPORTED` | Yes, but lineage-tag to the broadcast |
| P5 | **Named reputable journalist/reporting outlet** with match-specific observed/quoted strip information | `EXACT_MATCH_REPORTED` | Yes |
| P6 | Immediately preceding same-venue match in the same series/tournament | `DIFFERENT_STRIP_CONTEXT` | No, unless same-strip reuse is explicitly confirmed |
| P7 | Same-venue, same-format/rules-era historical scoring and phase baseline | `VENUE_HISTORY` | No |
| P8 | ICC post-match pitch rating / explicitly quoted CricViz PitchViz / similar approved historical surface metric | `VENUE_REPUTATION_CONTEXT` | No |

### Required strip status

Use exactly one:

- `OBSERVED`
- `NOT_FOUND_AFTER_SEARCH`
- `CONFLICTING`
- `STALE_ONLY`

A current strip is **not** “observed” merely because venue history exists.

---

# 3. New source lanes and retrieval techniques

These are source-discovery improvements, not automatic numerical-feature approval.

## 3.1 Official video is a first-class toss/pitch lane

Search verified official channels because boards and ICC often publish the toss/pitch segment separately.

Examples verified during this audit:
- ICC hosts dedicated **“Toss, Pitch Report”** video pages.
- Pakistan Cricket's verified YouTube channel published **“Toss & Pitch Report | Pakistan vs Australia | Match 02 | T20I Series 2026.”**

Operational query:
- `site:youtube.com "<Team A>" "<Team B>" "Toss & Pitch Report" "<competition/board>"`
- then verify the channel is the official board/competition/rights-holder account.

Do not treat an unrelated cricket channel as official merely because its title contains “pitch report.”

## 3.2 Official match centres remain the preferred toss source

Cricket Australia's Match Centre, for example, exposes the toss and teams on exact-match pages. Other boards/competitions may use their own match centre, NV Play, Play-Cricket, CricketArchive-branded pages or another official scoring partner.

Record the **field owner**, not just the hostname. A scoring platform embedded by the competition can be stronger than a random third-party page, but only for fields it actually carries.

## 3.3 Official board “Toss Report” pages can contain wicket comments

Some boards publish a dedicated toss article including:
- toss winner and decision;
- confirmed XIs;
- captain comments on the wicket.

When available, this is substantially more useful than a generic venue pitch profile.

## 3.4 Cricbuzz live commentary can recover a named broadcast pitch report

Cricbuzz 2026 commentary pages have carried named pitch reports such as:
- presenter names;
- pitch number;
- visible grass/dryness;
- expected seam/turn/bounce;
- weather context;
- captain comments and confirmed XIs.

Classify this as a **transcript/access route to the broadcast lineage**, not an independent second pitch source when it is clearly transcribing that broadcast.

## 3.5 NV Play is a useful official-scoring route for domestic/associate cricket

NV Play documentation shows the scorer records the toss and uploads live match data to Match Centre. When a national board/competition officially uses NV Play, search the board's public Match Centre or embedded scorecard before resorting to generic aggregators.

This is particularly useful for:
- associate internationals;
- domestic competitions;
- smaller European competitions;
- board-managed club/regional events.

## 3.6 Board/competition-specific specialist routes

For sparse competitions, explicitly search:
1. competition official site;
2. national board site;
3. official scorecard provider linked by the board;
4. official verified video channel;
5. official rights-holder;
6. specialist exact-match commentary/scorecard;
7. local reputable cricket press.

For European/Irish events, current evidence shows useful routes can include the competition site, Cricket Ireland-branded scorecard infrastructure, CricketEurope, and an official NV Play-linked match centre.

---

# 4. Mandatory search sequence for every cricket card

## Stage A — identity and official routing
1. Resolve exact event, competition, venue, local date/time and official match ID.
2. Identify the field owner: ICC, national board, league/competition, or sanctioned scoring partner.
3. Open the exact official event page.
4. Identify any official “Watch”, broadcaster, stream, or video link.

## Stage B — pre-toss pitch search
Run:
- `"<Team A>" "<Team B>" "pitch report"`
- `"<venue>" "pitch report" cricket`
- `"<venue>" curator cricket`
- `"<venue>" groundsman cricket`
- `site:<official-domain> "<Team A>" "<Team B>" pitch`
- `site:espncricinfo.com "<Team A>" "<Team B>" "pitch and conditions"`
- `site:cricbuzz.com "<Team A>" "<Team B>" "Pitch Report"`
- `site:wisden.com "<Team A>" "<Team B>" pitch`

Use dated venue profiles only as `HISTORICAL_VENUE_TENDENCY`.

## Stage C — official video/broadcast search
Run:
- `site:youtube.com "<Team A>" "<Team B>" "Toss & Pitch Report" "<board/competition>"`
- `site:youtube.com "<competition>" "<Team A>" "<Team B>" toss`
- exact-match search on the broadcaster/rights-holder site if identified.

Verify channel/account identity.

## Stage D — toss-window refresh
At the competition's actual toss window:
1. refresh official match centre;
2. refresh official board/competition video/live feed;
3. query structured toss/XI endpoint if available;
4. open specialist live commentary;
5. refresh official team/competition post/live blog;
6. record toss winner, decision, XI status and strip evidence separately.

A common toss timing is roughly 15–30 minutes before scheduled play, but the competition's own playing conditions control.

## Stage E — final pre-issue refresh
Immediately before issue:
- event state;
- toss;
- confirmed XIs;
- late withdrawals/substitutes;
- exact strip report;
- local weather/radar;
- source conflicts/staleness.

If scheduled start has passed, do not pretend the card is still pre-game. Reclassify state first.

---

# 5. Source-lineage fingerprinting — new hard rule

A new operational rule is required because several cricket sites can expose the **same structured feed text**.

### Rule

If two or more sites show identical or near-identical unusual structured fields, for example:

- `Pitch Condition - Spinning Pitch`
- `Batting Condition - Average`
- `Pace Bowling Condition - Swing Favourable`
- `Spin Bowling Condition - Sharp Turn`

treat them as **one suspected upstream lineage** until provenance proves independence.

### Why

The ETPL audit found the same pitch/weather/umpire-style blocks on multiple front ends. The same labels can appear before play and after play, indicating a shared data template/feed rather than separate human pitch inspections.

### Classification

Without a named observer/source:
- `CLAIM_TYPE = AUTOMATED_PITCH_METADATA`
- `STRIP_OBSERVATION = NO`
- `INDEPENDENT_PITCH_SOURCE = NO` unless upstream independence is established

The data can be retained as a weak supporting signal, but it cannot by itself satisfy the exact-strip gate.

---

# 6. Official-page staleness rule — new hard rule

Official does not mean automatically current.

If an official dynamic event page remains `UPCOMING` while other reliable sources show that the match is completed or live:

1. mark that page/field `STALE`;
2. do not allow it to control current event state;
3. retrieve another official/static result or sanctioned scoring route;
4. reconcile with independent high-quality sources;
5. preserve the stale-source incident in the source audit.

This is field-specific: an official page can still be useful for identity/venue while stale for state.

---

# 7. Claim schema for toss and pitch evidence

Every material toss/pitch record should store:

| Field | Required |
|---|---|
| `event_id` | Exact event |
| `claim_type` | `TOSS_FACT`, `XI_FACT`, `STRIP_OBSERVATION`, `STRIP_REPORT`, `AUTOMATED_PITCH_METADATA`, `VENUE_HISTORY`, `WEATHER` |
| `source_id` | Exact source record |
| `source_class` | Official / rights-holder / structured / specialist / reporting / historical |
| `field_owner` | Who owns the field |
| `upstream_lineage_id` | Shared-feed identifier where known/suspected |
| `published_at` / `first_known_at` | Point-in-time control |
| `retrieved_at` | Retrieval timestamp |
| `cutoff_at` | Forecast cutoff |
| `speaker_or_author` | Required for named strip reports when available |
| `exact_wording_summary` | Do not strengthen the source's language |
| `toss_winner` / `decision` | Separate fields |
| `xi_status` | Confirmed / expected / unavailable |
| `strip_number` | If stated |
| `same_strip_confirmed` | Yes / No / Unknown |
| `freshness_status` | Fresh / stale / conflicting |
| `independence_status` | Independent / same lineage / unknown |
| `evidence_class` | Exact-match observed/reported vs historical/context |

---

# 8. Conflict-resolution rules

Do not majority-vote pitch descriptions.

Priority:
1. exact-match curator/groundsman statement;
2. named on-site current broadcast inspection;
3. official exact-match captain/coach comment;
4. named specialist transcript/report of that evidence;
5. historical/context sources.

If two credible exact-match reports conflict:
- record `STRIP_STATUS = CONFLICTING`;
- keep both reports and timestamps;
- prefer the later/more direct observation only when there is a defensible freshness/field-owner reason;
- widen the conditions branch rather than invent certainty.

---

# 9. What does and does not count as independent evidence

## Counts when genuinely independent
- official competition match centre;
- independent national-board/team release that is not merely reproducing the same feed;
- rights-holder broadcast's own on-site observation;
- independent named journalist's original reporting;
- separate government weather service for weather only.

## Does not create a second lineage
- ESPN and ESPNcricinfo if they are using the same upstream record;
- two sites embedding the same NV Play or Stats Perform feed;
- a Cricbuzz transcription of the exact same rights-holder pitch report plus the original broadcast;
- syndicated wire copies;
- search snippets pointing to the same page;
- identical templated pitch-condition blocks across multiple aggregators.

---

# 10. Exclusion rules

Do not use as predictive pitch/toss evidence:
- betting previews/picks;
- odds or market movement;
- “toss prediction” pages;
- fantasy/Dream11/DFS pages;
- generic formulaic “pitch report” sites without attributable observation;
- AI-generated/simulated match reports;
- community comments as decision-driving evidence.

Existing excluded-domain examples in the Drive source register remain excluded.

---

# 11. Required output block for future cricket cards

```text
TOSS STATUS:
- Status:
- Winner:
- Decision:
- XI status:
- Source:
- Upstream lineage:
- Retrieved at:
- Pre/post toss:

STRIP STATUS:
- Status: OBSERVED / NOT_FOUND_AFTER_SEARCH / CONFLICTING / STALE_ONLY
- Exact-match source(s):
- Speaker/author:
- Observation/report:
- Strip number if known:
- Same-strip reuse confirmed?:
- Automated metadata present?:
- Context-only evidence:
- Search ladder attempted:
- Missingness/conflicts:

MATCH CONDITIONS STATUS:
- Weather source:
- Match-window weather:
- Interruption/DLS risk:
- Dew/light only if evidenced:
- Conditions signals and independence:

SOURCE-LINEAGE CHECK:
- Qualifying event lineages:
- Pitch lineages:
- Suspected duplicate feeds:
- Search snippets used as evidence? NO
```

A prediction may proceed with `NOT_FOUND_AFTER_SEARCH` only after the search is actually shown. Missing strip information must lower confidence/widen uncertainty; it must never be replaced by invented conditions.

---

# 12. Current-document repairs to apply when the authoritative Drive becomes writable

Because the Drive is read-only in this environment, these are documented as precise future edits rather than silently claimed as completed.

### `RULES_CRICKET.md`
- Replace all “full six-rung” references with the two-ladder TOSS/STRIP protocol.
- Remove duplicated “Rung 8 toss broadcast” semantics by placing the broadcast in T2/P1.
- Preserve preceding same-venue match as different-strip context.
- Replace “rung 6 always computed” language with `INSUFFICIENT_VENUE_HISTORY` handling.
- Add source-lineage fingerprint and automated-pitch-metadata classifications.
- Add official-page staleness rule.

### `DATA_SOURCE_REGISTER.md`
- Correct the table text that says the venue baseline is always computable.
- Add source cards for:
  - official board/competition verified toss/pitch video;
  - sanctioned NV Play/board-branded Match Centre;
  - named broadcast-transcript access route;
  - automated pitch metadata as weak/non-observed evidence.
- Add ETPL shared-feed fingerprint example.
- Preserve current exclusions for fantasy/tipping sites.

### `SOURCES.md`
- Replace “full conditions ladder (six-rung)” with the current two-ladder reference.
- Add official verified video and broadcast-transcript source lanes.
- State explicitly that a transcript and its original broadcast are one lineage.

### `UPCOMING_GAME_RESEARCH_GUIDE.md`
- Replace the six-rung checklist item.
- Add the toss-window/final-refresh query sequence.
- Require the output block in Section 11.
- Add `STALE_OFFICIAL_FIELD` and `AUTOMATED_PITCH_METADATA` dispositions.

### Audit/learning register
- Record this as an **enforcement/source-retrieval improvement**, not evidence that a predictive coefficient or probability has been validated.

---

# 13. Sources specifically validated during the 2026-09-21 research pass

These are evidence that the retrieval lanes exist; they are **not blanket approval for every competition or for automated ingestion**.

1. ICC official video pages publish dedicated “Toss, Pitch Report” content.  
   `https://www.icc-cricket.com/videos/toss-pitch-report-ire-vs-jer`

2. Pakistan Cricket verified YouTube channel publishes match-specific “Toss & Pitch Report” videos.  
   `https://www.youtube.com/watch?v=6rBRlkFJ5oQ`

3. Cricket Australia Match Centre exposes exact-match toss and teams.  
   Example: `https://www.cricket.com.au/matches/CA%3A40595?tab=scorecard`

4. BCCI has published dedicated Toss Report pages containing the decision, XIs and captain comments on the wicket.  
   `https://www.bcci.tv/news/article/toss-report-india-v-west-indies`

5. Cricbuzz live commentary can carry named broadcast pitch-report transcripts, including pitch number and surface observations.  
   Examples:
   - `https://www.cricbuzz.com/live-cricket-full-commentary/138600/ausu19-vs-wiu19-7th-match-super-six-group-1-ad-icc-under-19-world-cup-2026`
   - `https://www.cricbuzz.com/live-cricket-full-commentary/138653/indu19-vs-paku19-12th-match-super-six-group-2-bc-icc-under-19-world-cup-2026`

6. NV Play's official support documentation confirms toss details are explicitly recorded by live scorers and uploaded to Match Centre.  
   `https://support.nvplay.com/hc/en-gb/articles/17673349333017-Entering-a-Scorecard-or-Totals-Only-Match`

7. Windies Cricket provides an official results/Match Centre route for CPL and West Indies competitions.  
   `https://www.windiescricket.com/results/class_type/general/`

8. Current ETPL official pages declare their live scoring is supplied by NV Play, while one exact final page was observed stale as `UPCOMING` after independent sources had a final result. This supports the field-specific staleness rule.  
   `https://www.etplofficial.com/`

9. ETPL testing found identical structured pitch-condition text across multiple downstream sites. This supports the shared-lineage/automated-metadata rule rather than counting those front ends as independent observed strip reports.

---

# 14. Operational bottom line

For future cricket research:

- **Toss:** go official match centre -> official/rights-holder video -> official post/live blog -> structured endpoint -> specialist exact-match source -> independent reporting.
- **Pitch:** prioritize a named current-match observer/curator/captain; use specialist commentary as a transcript route; keep previous-match/venue/ICC ratings as context only.
- **Never count duplicate feeds twice.**
- **Never let generic automated pitch labels masquerade as a human strip report.**
- **Never assume venue history exists.**
- **Never infer strip properties from weather or the toss decision.**
- **Refresh during the toss window and again immediately before issue.**
- If the exact strip still cannot be recovered, say so explicitly and widen uncertainty instead of guessing.
