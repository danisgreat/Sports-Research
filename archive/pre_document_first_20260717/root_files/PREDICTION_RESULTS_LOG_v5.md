# Prediction results log v5

Status: GENERATED, COPY-FRIENDLY VIEW

This document contains every recorded decision packet and every recorded qualitative live analysis. The verified append-only journal remains the machine source of truth; regenerate this file instead of hand-editing it.

## Current verified state

- Journal records: 8
- Decision packets: 5
- Qualitative live analyses: 0
- Structured user-facing publications: 3
- Quantitative ISSUE records: 0
- Settlements: 0
- Evaluations: 0
- Journal head: `ef3421feaea939cb5761c381b3fea90b2aa4756bdb17ed766e201710ee7c1678`

## Copy-and-paste entries

## Entry 1 — West Indies Men v New Zealand Men, 4th ODI

```text
JOURNAL SEQUENCE: 1
RECORDED UTC: 2026-07-16T18:50:06.117Z
SPORT / COMPETITION: Cricket / ICC_ODI
EVENT: West Indies Men v New Zealand Men, 4th ODI
EVENT START UTC: 2026-07-19T14:00:00.000Z
MARKET: team innings totals and match winner (WI_TEAM_INNINGS_TOTALS_ODI4)
STATE / CUTOFF UTC: PREGAME_PROJECTED / 2026-07-16T18:47:02.447Z
USER REQUEST: Upcoming Cricket Match: West Indies vs New Zealand. Provide the best 4 picks from West Indies team-innings 50-over Over 212.5, Under 272.5, 10-over Over 39.5 and Under 49.5, plus a potential game winner; research the previous log, ignore any previous game still live, and be honest without hallucinations.
PRIMARY QUESTION: Which of the four supplied West Indies team-innings totals are supportable for the fourth ODI against New Zealand, and which team is the qualitative winner lean?
DECISION: PASS / CONTRACT_UNRESOLVED
FORMAL SELECTION: NONE — abstained
RECORDED USER-FACING RANKING: NOT CAPTURED IN A STRUCTURED PUBLICATION RECORD
RESEARCH / PICKS NOTE: Fourth ODI identified because the third ODI was live at cutoff and was excluded under the user's rule. Official CWI series page showed the third ODI live and the fourth at Kensington Oval on July 19. Cricbuzz listed the fourth ODI at 14:00 UTC. Venue summary: 53 ODIs, historic first-innings average 226. Current completed series results before the live third ODI: West Indies chased 268/3 to beat New Zealand, then were dismissed for 138 batting first; West Indies were 58/0 after 10 overs in the second ODI. The final fourth-ODI squad, XI, toss, pitch report and bookmaker settlement rules were unavailable at cutoff. The preceding England v India second-ODI PASS remained live and was not retrospectively settled. This is a non-quantitative research record and not a prediction-ledger ISSUE.
RESULT: PENDING OR NOT ELIGIBLE
EVALUATION: NOT AVAILABLE
REQUEST ID: REQ-86976b6f-54ad-4e49-8388-077f537e4dbc
SNAPSHOT ID: SNAP-dcdc5469-d453-4b10-9b0e-c8ec2caff7a9
PREDICTION ID: N/A
RECORD HASH: bc66b746960073b8693e224a9b350144c32768417753c936a909eacd6f14d84e
```

## Entry 2 — Bradford Bulls v Wakefield Trinity, Round 19

```text
JOURNAL SEQUENCE: 2
RECORDED UTC: 2026-07-16T18:58:07.324Z
SPORT / COMPETITION: Rugby league / SUPER_LEAGUE
EVENT: Bradford Bulls v Wakefield Trinity, Round 19
EVENT START UTC: 2026-07-16T19:00:00.000Z
MARKET: match handicap, combined total and match winner (BRADFORD_WAKEFIELD_HANDICAPS_AND_TOTAL_42)
STATE / CUTOFF UTC: PREGAME_PROJECTED / 2026-07-16T18:53:14.674Z
USER REQUEST: Upcoming Rugby Game: Bradford bulls vs Wakefield Trophy. Provide the best four picks from Bulls +18.0, Trinity -6, combined total Over 42.0 and combined total Under 42.0, plus a potential game winner; research the previous log, ignore any previous game still live, and be honest without hallucinations.
PRIMARY QUESTION: Which supplied handicap and total outcomes are supportable for Bradford Bulls v Wakefield Trinity, and which team is the qualitative winner lean?
DECISION: PASS / CONTRACT_UNRESOLVED
FORMAL SELECTION: NONE — abstained
RECORDED USER-FACING RANKING: NOT CAPTURED IN A STRUCTURED PUBLICATION RECORD
RESEARCH / PICKS NOTE: The event was identified as Bradford Bulls v Wakefield Trinity in Super League Round 19, scheduled for 20:00 BST at Odsal. Official Super League material showed Wakefield in stronger current form and recorded a 52-12 Wakefield win in the reverse fixture. Across the six form results displayed for each team, eleven of twelve match totals exceeded 42 points. Round 18 season data listed Wakefield at 457 points for and 308 against through 17 matches, and Bradford at 312 for and 507 against. The supplied total outcomes are complementary branches, while Bulls plus 18 and Trinity minus 6 overlap when Wakefield wins by 7 to 17 points. Exact bookmaker settlement rules and a registered Super League model contract were unavailable. The prior West Indies v New Zealand fourth-ODI research record remains upcoming, and the third ODI was live, so neither was graded. This is a non-quantitative research record and not a prediction-ledger ISSUE.
RESULT: PENDING OR NOT ELIGIBLE
EVALUATION: NOT AVAILABLE
REQUEST ID: REQ-d4530a0b-23ac-48be-a4ad-071c335011be
SNAPSHOT ID: SNAP-301a5471-f9b6-4917-a72e-a7b607b53649
PREDICTION ID: N/A
RECORD HASH: 6aa7e97e990e9bd3d4ee186967fa94c066bd53b5ab523f9dccf42674a8415bf3
```

## Entry 3 — Diablos Rojos del Mexico at Tigres de Quintana Roo, Game 3

```text
JOURNAL SEQUENCE: 3
RECORDED UTC: 2026-07-17T01:50:13.438Z
SPORT / COMPETITION: Baseball / LMB
EVENT: Diablos Rojos del Mexico at Tigres de Quintana Roo, Game 3
EVENT START UTC: 2026-07-17T00:30:00.000Z
MARKET: live alternate run lines, live combined totals and winner (DIABLOS_TIGRES_LIVE_ALT_RUN_LINES_AND_TOTALS)
STATE / CUTOFF UTC: LIVE / 2026-07-17T01:49:32.612Z
USER REQUEST: Live Baseball Game: Mexico City at Quintana Roo. Assess Mexico City -8.5, Quintana Roo +7.5, combined total Over 17.5 and Under 18.5, add a potential winner, research the previous log, ignore a previous game if it remains live, and be honest without hallucinations.
PRIMARY QUESTION: Which supplied live run-line and total outcomes are supportable for Diablos Rojos del Mexico at Tigres de Quintana Roo, and which team is the qualitative winner lean?
DECISION: PASS / CONTRACT_UNRESOLVED
FORMAL SELECTION: NONE — abstained
PUBLICATION: Diablos Rojos del Mexico at Tigres de Quintana Roo live ranked selections
PICK 1: Combined Total Over 17.5 runs — SUPPORTED — The observed live feed already showed 15 runs after two and a half innings, so three additional runs were required.
PICK 2: Mexico City -8.5 — LEAN — Diablos led by nine at the cutoff, so the supplied line was narrowly covering with substantial game time remaining.
PICK 3: Quintana Roo +7.5 — AVOID — Tigres needed to improve the observed nine-run deficit by at least two runs; an eight-run final margin would lose both supplied run lines.
PICK 4: Combined Total Under 18.5 runs — AVOID — The under allowed no more than three additional runs across the remaining six and a half innings.
POTENTIAL WINNER: Diablos Rojos del Mexico
PUBLIC SUMMARY: At the 2026-07-17T01:49:32.612Z cutoff, the live feed showed Diablos leading 12-3 midway through the third. Over 17.5 ranked first, Mexico City -8.5 was a secondary lean, Quintana Roo +7.5 and Under 18.5 were avoids, and Diablos were the potential winner. The formal framework decision remained PASS because LMB was outside registered live-model coverage and the supplied settlement contract was unresolved.
PUBLICATION ID: PUB-BASEBALL-LMB-20260716-DIABLOS-TIGRES-G3-001
RESEARCH / PICKS NOTE: The exact live market feed showed Diablos Rojos del Mexico leading Tigres de Quintana Roo 12-3 at the middle of the third inning, with 15 runs already scored and Tigres due to bat. The same feed had moved its main live run line to Diablos minus 9.5 and its main total to 20.5, so the user-supplied minus 8.5, plus 7.5, 17.5 and 18.5 lines were no longer the displayed main market and require availability confirmation. Over 17.5 needed at least three additional runs, while Under 18.5 allowed no more than three; both could settle as wins only on an 18-run final. Diablos minus 8.5 required a final margin of at least nine and Tigres plus 7.5 required a margin of no more than seven, leaving an eight-run margin where both supplied run lines lose. Official schedule and completed-game records confirmed the matchup and that Diablos won the first two games of the series 3-1 and 6-0. The previous Bradford Bulls v Wakefield Trinity record was still live and was not graded. LMB live markets are outside the registered baseball model coverage, and the exact settlement rules for the supplied lines were unavailable. This is a qualitative research record and not a prediction-ledger ISSUE.
RESULT: PENDING OR NOT ELIGIBLE
EVALUATION: NOT AVAILABLE
REQUEST ID: REQ-042a3fab-fd17-4fc1-aa15-84022facd354
SNAPSHOT ID: SNAP-eb879e9f-98e3-4ddb-8909-38d90b2e934f
PREDICTION ID: N/A
RECORD HASH: e84ed8dae7f392082674b0de3c9e04bc3cd5f466664ede79093cd3fb4b030d58
```

## Entry 5 — Diablos Rojos del Mexico at Tigres de Quintana Roo, Game 3

```text
JOURNAL SEQUENCE: 5
RECORDED UTC: 2026-07-17T03:25:59.099Z
SPORT / COMPETITION: Baseball / LMB
EVENT: Diablos Rojos del Mexico at Tigres de Quintana Roo, Game 3
EVENT START UTC: 2026-07-17T00:30:00.000Z
MARKET: live full-game combined total (DIABLOS_TIGRES_LIVE_TOTAL_OVER_19_5)
STATE / CUTOFF UTC: LIVE / 2026-07-17T03:24:47.216Z
USER REQUEST: Live check, Mexico City at Quintana Roo: how likely is Over 19.5 total runs? Be honest.
PRIMARY QUESTION: Is the live full-game total Over 19.5 supportable at the verified eighth-inning state?
DECISION: PASS / CONTRACT_UNRESOLVED
FORMAL SELECTION: NONE — abstained
PUBLICATION: Diablos Rojos del Mexico at Tigres de Quintana Roo live Over 19.5 check
PICK 1: Combined Total Over 19.5 runs — PASS — The total was 18 with two outs in the top of the eighth, so two more runs were required; scoring had cooled and the live market favored Under 19.5.
POTENTIAL WINNER: N/A
PUBLIC SUMMARY: Over 19.5 remained plausible but was less likely than not at the frozen state. It needed two more runs with roughly two innings remaining. The honest call was PASS on the over, not a supported play, because LMB totals are outside the active model and the exact live settlement contract was unresolved.
PUBLICATION ID: PUB-BASEBALL-LMB-20260716-DIABLOS-TIGRES-G3-OVER19-5-001
RESEARCH / PICKS NOTE: At the frozen live cutoff, both the market page and its linked Sportradar match centre showed Diablos leading 13-5 in the eighth inning. The market feed showed two outs in the top of the eighth with Diablos batting, so 18 runs had scored and Over 19.5 required at least two more. Only two combined runs had scored from the fourth inning through the current eighth, indicating that scoring had cooled sharply after the first three innings. The displayed alternate-total prices were Over 19.5 at plus 160 and Under 19.5 at minus 225, with the buttons temporarily suspended during live play. Late bullpen and blowout volatility leave a route to two runs, but the observed state and market both favor the under branch. LMB totals are outside registered model coverage and exact settlement terms were unavailable, so this is a qualitative PASS rather than an issued numeric forecast. The immediately preceding record is the same still-live event and therefore was not settled or retrospectively graded.
RESULT: PENDING OR NOT ELIGIBLE
EVALUATION: NOT AVAILABLE
REQUEST ID: REQ-a22b3aad-0f53-4871-8d0a-31fa2252c3a7
SNAPSHOT ID: SNAP-009b9c86-4f5e-465c-8134-28b921673835
PREDICTION ID: N/A
RECORD HASH: 17184d37b020473c5398c555b841f71bdaac1d42da7f0794cf8331c11f5c7677
```

## Entry 7 — Diablos Rojos del Mexico at Tigres de Quintana Roo, Game 3

```text
JOURNAL SEQUENCE: 7
RECORDED UTC: 2026-07-17T03:27:24.218Z
SPORT / COMPETITION: Baseball / LMB
EVENT: Diablos Rojos del Mexico at Tigres de Quintana Roo, Game 3
EVENT START UTC: 2026-07-17T00:30:00.000Z
MARKET: live full-game combined total (DIABLOS_TIGRES_LIVE_TOTAL_OVER_19_5)
STATE / CUTOFF UTC: LIVE / 2026-07-17T03:26:35.404Z
USER REQUEST: Live check, Mexico City at Quintana Roo: how likely is Over 19.5 total runs? Be honest.
PRIMARY QUESTION: Is the live full-game total Over 19.5 supportable at the verified start-of-bottom-eighth state?
DECISION: PASS / CONTRACT_UNRESOLVED
FORMAL SELECTION: NONE — abstained
PUBLICATION: Diablos Rojos del Mexico at Tigres de Quintana Roo refreshed Over 19.5 check
PICK 1: Combined Total Over 19.5 runs — PASS — The total remained 18 after a scoreless top of the eighth, two runs were still required, and the refreshed live market moved farther toward Under 19.5.
POTENTIAL WINNER: N/A
PUBLIC SUMMARY: Over 19.5 was still possible but clearly less likely than not at the refreshed cutoff. It needed two runs over the remaining bottom of the eighth and ninth inning, while the recent scoring path and market both favored the under. The honest call remained PASS on the over rather than a supported play.
PUBLICATION ID: PUB-BASEBALL-LMB-20260716-DIABLOS-TIGRES-G3-OVER19-5-002
RESEARCH / PICKS NOTE: At the refreshed cutoff, the linked Sportradar match centre and market page still showed Diablos leading 13-5 in the eighth. The top of the eighth had ended scoreless and the feed showed the next half-inning beginning with no outs, leaving 18 total runs and two more required for Over 19.5. The game had produced only two combined runs from the fourth through the completed top of the eighth. The live alternate-total price had moved farther against the over, to Over 19.5 at plus 210 and Under 19.5 at minus 300. Two late runs remain possible through bullpen and blowout volatility, but the updated scoreboard, recent scoring path and market all favor the under branch. LMB totals remain outside registered model coverage and exact settlement terms were unavailable, so this is a qualitative PASS rather than an issued numeric forecast. The preceding entries are the same still-live event and were not settled or retrospectively graded.
RESULT: PENDING OR NOT ELIGIBLE
EVALUATION: NOT AVAILABLE
REQUEST ID: REQ-6a2ebc1a-d600-4b3b-af0a-0bbd6499ae8e
SNAPSHOT ID: SNAP-c5fb1f8a-ca0a-4a93-9256-42ff5ccaca21
PREDICTION ID: N/A
RECORD HASH: ad29fb2e83174876bdce8880a5a512e9bfeb428dda457ae0f1f5b41cb6e87b3e
```

## Historical boundary

Legacy v2–v4 rows remain historical and are not silently imported into this verified view. They may be consulted only as labelled retrospective evidence.
