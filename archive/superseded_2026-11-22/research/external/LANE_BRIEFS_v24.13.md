# Lane briefs v24.13 (paste one under the request in each chat)

Each brief is self-contained apart from the [external profile](EXTERNAL_PROFILE_v24.13.md), which every chat reads first. The owner pastes, in one message: the filled request (one game), the block the repository agent printed (commit SHA, event key, Reference block, history-pack windows), and one brief below. Every lane ends with one LANE_RETURN block:

```text
<!-- BEGIN LANE_RETURN -->
event_key: <event key>
lane: <L1|L2|L3|L4|L5|FULL>
chat_label: <CHAT-1 .. CHAT-5, as the owner names the chat>
profile_version: v24.13
commit: <the 40-character SHA from the owner's block>
reader: CHATGPT_BROWSING
started_at: <ISO time with offset>
completed_at: <ISO time with offset>

[EVIDENCE]
side,field,value,source_url,source_class,published_at,retrieved_at,confirmation,notes
[PROBABILITIES]
label,family,side,line,line_source,w,p,l,final_p,kit_receipt_sha256
[ACCESS_LOG]
url,result,checked_at,notes
<!-- END LANE_RETURN -->
```

Vocabulary: side HOME/AWAY/EVENT; source_class FIELD_OWNER, LEAGUE, CLUB, OFFICIAL_SOCIAL, PROVIDER, MEDIA, REPORTER_SOCIAL, OWNER_CAPTURE; confirmation OFFICIAL_CONFIRMED, REPORTED, PROJECTED, NOT_APPLICABLE; access result OPENED, BLOCKED_BY_RULES, RULES_UNKNOWN, ON_DO_NOT_OPEN_LIST, TECHNICAL_FAILURE, NOT_FOUND. Values containing commas go in double quotes.

---

## L1 Availability

```text
LANE L1 (availability). Find, for BOTH sides: confirmed starters and starting roles; the selected bench or replacements;
every player confirmed out, doubtful or questionable, with the reason; suspensions; late changes; and the starting goalie,
pitcher or quarterback where the sport has one. Check each at its publication window (team announcement, official injury
report, toss in cricket) and again close to the start. Sources in order: the competition's match centre or official report;
both clubs' sites; official social accounts the club's own site links; permitted structured providers; reputable media and
reporters (one source each). One EVIDENCE row per fact: field "status:<Player Name>" with value OUT, DOUBTFUL, QUESTIONABLE,
PROBABLE, ACTIVE or STARTING; field "starter" for each confirmed starter; "lineup_status" CONFIRMED or NOT_PUBLISHED.
Projected line-ups are PROJECTED, never OFFICIAL_CONFIRMED. If X, Instagram or Facebook holds the only report, ask the owner
for an owner capture. No PROBABILITIES.
```

## L2 Results and form

```text
LANE L2 (results and form). The owner's block gives each side's history pack and the date it runs to. Find every game each
side played AFTER that date and before the request day, from the competition's official results or a permitted provider:
date, opponent, home or away, final score (and half-time in soccer, first-innings and over-6/5 score in cricket). One EVIDENCE
row per game: field "game:<YYYY-MM-DD>:<opponent>", value "<for>-<against> <H|A>". Then one row each for L5, L10, L15, L20 and
season: field "window:L5" etc., value "n=<true n>; for=<per game>; against=<per game>". True n is the number of games actually
found: never pad a window. Exclude duplicates, awarded results, forfeits and abandoned games and say so in notes.
No PROBABILITIES.
```

## L3 Conditions and rules

```text
LANE L3 (conditions and rules). Find: the official scheduled start in venue time and UTC; the venue and whether it is
neutral; for outdoor play the venue-local forecast for the match window (temperature, wind, rain probability) from a
permitted weather source, read within 3 hours of the start where possible; officials if published; each side's rest days
and travel since its last game; the stage (regular season, finals, cup) and the exact settlement rules of every supplied
line: overtime or extra time, ties and draws, shootouts, retirement (tennis), reduced overs and DLS (cricket). Fields:
"scheduled_start", "venue", "neutral_venue", "temperature_c", "wind_kph", "rain_probability_pct", "referee", "rest_days",
"travel", "stage", "endpoint_rule". No PROBABILITIES.
```

## L4 Re-check

```text
LANE L4 (independent re-check). Re-check every decisive availability fact (starters, players out, the starting goalie,
pitcher or quarterback) using DIFFERENT websites from the ones a lane-1 chat would use first: the other club's site, the
league's own report, local-language media, official social accounts the club's site links. Two pages of one site, or a
story copied from the same feed, are one source. Report each fact you could confirm or contradict, with its own source,
in the same field names as L1. Report contradictions plainly; never pick a side by majority. No PROBABILITIES.
```

## L5 Pricing

```text
LANE L5 (pricing). Upload sr_kit.py, KIT_PARAMETERS_v24.13.csv and KIT_CRICKET_PHASES_v24.13.csv. Start from the Reference
block in the owner's message: its centre (total and margin, or the goal or run means) is the starting point and is never
edited. The owner will paste the merged evidence when the research lanes are done (or tell you to use the facts in this
chat). For each confirmed fact the reference cannot know, apply only a size from the repository's effect tables
(research/effect_tables/EFFECT_TABLES.csv at the commit): a MEASURED_CONFIRMED row at full size, a MEASURED_NOT_CONFIRMED or
LITERATURE_START row at half size; a fact with no row is a declared low/base/high scenario mixture with weights fixed before
pricing. Widths never below the competition's row. Price every supplied line, both sides, and the winner for both sides
with K.run(...); print every receipt. PROBABILITIES rows: one per contract, final_p = w / (w + l), kit_receipt_sha256 = the
SHA-256 of the receipt text you printed. Paste the receipts above the LANE_RETURN block.
```

## FULL (one chat does everything)

```text
LANE FULL. Do L1, L2 and L3 yourself, then L5. Return all evidence and all prices in one LANE_RETURN block with lane FULL.
Your prices are used as a consensus check against the merged card, not as the card.
```
