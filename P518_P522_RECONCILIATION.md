# Current custody reconciliation - 2026-10-01

P-518-P-522 remain **reserved / LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**. The dated 2026-09-30 append after the frozen source marker in [Part 6](prediction%20logs/PREDICTION_LOG_COMBINED_6.md) records learning-only settlements for P-518 (Mets 7-1 Nationals, issued gamePk 822678) and P-522 (Tenerife 80-81 Zaragoza, issued ACB 105380). Those two are no longer awaiting that learning settlement append. This acknowledges the existing sourced append; it does not certify prospective issue timing, canonical import, baseline eligibility or future skill.

P-519/P-520/P-521 retain open field/identity/process/independent-lineage reconciliation requirements. Earlier all-five-unsettled or all-five-certified language is superseded by this split state. The original 141,740-byte source block and every issued p/q/baseline literal remain unchanged. P-523 is the next new issue ID in Part 6; no implementation/shadow/empty mini-log consumes it.

The historical reconciliation record below explains the original defects. Corrections remain append-only and cannot lift historical performance exclusion.

---

# P-518–P-522 custody and source reconciliation

**Audit date:** 2026-09-28. **State:** OPEN. Part 5 is canonical through P-517. P-518–P-522 are reserved claims in the original source block embedded in [Part 6](prediction%20logs/PREDICTION_LOG_COMBINED_6.md), not certified canonical imports. The embedded original block's raw-byte SHA-256 is `c4d497bf339010eae2ff5df23a2d76290983585671666e74791618342565cf30`; its original issue text and settlement text remain unchanged. The former mini-log path was removed during six-part consolidation; Git `753f0a9` retains that file. All five remain **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**. The user has independently directed the new prediction sequence to continue at **P-523** in Part 6; that does not resolve these five records.

This record transcribes the removed reconciliation CSV and source readback from Git parent `3fbf0c981b40a1d0e3ffff9725dcc8e383ff05fa`, then adds exact issue-versus-settlement baseline comparisons. The parent files are `reviews/2026-09-28/P518_P522_RECONCILIATION_REGISTER.csv` and `reviews/2026-09-28/P518_P522_EXTERNAL_SOURCE_READBACK.md`. This is an audit of preserved evidence, not a new issue or corrected settlement.

| ID | Issued event / state | Result supported by field owner | Defect in working settlement | Required before canonical import |
|---|---|---|---|---|
| P-518 MLB | 822678; `LIVE_ISSUED` | Mets 7–1 Nationals; [MLB game page](https://www.mlb.com/gameday/mets-vs-nationals/2026/09/26/822678/final/summary/all) and [StatsAPI feed](https://statsapi.mlb.com/api/v1.1/game/822678/feed/live) | Official RHE is Mets 7–9–1, Nationals 1–3–1; Jonah Tong 5.0 IP, 9 K, 1 BB; Connelly Early 3.0 IP, 1 H, 0 BB, 1 K, 34 pitches; duration 2:43; attendance 27,284. Working process/date claims conflict. MLB pages and StatsAPI share an upstream lineage. | Append a field-level correction with issue cutoff and independent terminal lineages. Restore the issued baselines, not 0.500. |
| P-519 AFLW | 8942; `LIVE_ISSUED` | Gold Coast 69–39 St Kilda; [AFLW match 8942](https://www.afl.com.au/aflw/matches/8942) | Settlement cites 7412. The official match page records injuries to Annabel Kievit and Fiedler; the timing and effect need verification before a disruption claim. | Correct event reference in an appended settlement revision; check issue timing, injury assertions and independent lineages. |
| P-520 KBO | Stable game ID not preserved; working issue says `PREGAME` | Hanwha 6–2 Lotte, 27 September, Sajik 17:00 KST; [KBO scoreboard](https://eng.koreabaseball.com/Schedule/Scoreboard.aspx?searchDate=2026-09-27) and [KBO report](https://koreabaseball.com/MediaNews/News/BreakingNews/View.aspx?bdSe=62432) | The scoreboard route does not establish a durable game ID, issue cutoff, pitchers or full process. Both KBO pages are one publisher lineage. | Bind the exact fixture and cutoff, verify process fields and obtain independent terminal lineages. |
| P-521 ACB | 105378; `LIVE_ISSUED` | Río Breogán 110–104 Joventut; [ACB game 105378](https://live.acb.com/es/partidos/rio-breogan-vs-asisa-joventut-105378/resumen) | Process and stat claims lack a separate lineage audit. ACB's game and statistics views can share one feed. | Audit issue timing and process fields; obtain independent terminal lineages. Baseline remains `NOT_YET_DERIVED`. |
| P-522 ACB | 105380; `LIVE_ISSUED` | Tenerife 80–81 Zaragoza; [ACB game 105380](https://live.acb.com/es/partidos/la-laguna-tenerife-vs-casademont-zaragoza-105380/resumen) | Settlement cites 105379. Coach/roster narrative and timing are unverified. | Append correction to 105380; audit timing/process and independent lineages. Baseline remains `NOT_YET_DERIVED`. |

The official ACB quarters are 29–28, 27–21, 19–22, 35–33 for P-521 and 18–18, 20–26, 27–24, 15–13 for P-522. A result match alone does not certify an issue-time forecast or complete settlement. The historical MLB StatsAPI extraction recorded retrieval at `2026-09-27T14:47:22.350012+00:00` and response SHA-256 `a7e860f79cf0c80e1b2bec37fd4101aec0fd94ad1fb18d0e7acbdbc7955e222d`; that is one response, not a raw multi-source archive.

## Issued `BASELINE_P` versus working settlement

The issue table is the only authority for what was stated before the result. In every working settlement below the baseline column was replaced by `0.500`; that is not a valid transcription. The `q` values are RM-1 ordering scores, not coherent event probabilities. This table is a correction register, not a replacement forecast.

| Card | Rank | Issued contract | Issued p | Issued q | Issued baseline literal | Working settlement baseline |
|---|---:|---|---:|---:|---|---:|
| P-518 | 1 | Mets +1.5 | .640 | .668 | .638 | .500 |
| P-518 | 2 | Nationals +1.5 | .635 | .661 | .638 | .500 |
| P-518 | 3 | Over 8.5 | .590 | .593 | .491 | .500 |
| P-518 | 4 | Under 8.5 | .410 | .407 | .509 | .500 |
| P-519 | 1 | Under 89.5 | .719 | .780 | `NOT_YET_DERIVED (0.500)` | .500 |
| P-519 | 2 | Suns(W) -27.5 | .449 | .731 | `NOT_YET_DERIVED (0.500)` | .500 |
| P-519 | 3 | St Kidla(W) +27.5 (issued spelling) | .551 | .269 | `NOT_YET_DERIVED (0.500)` | .500 |
| P-519 | 4 | Over 89.5 | .281 | .220 | `NOT_YET_DERIVED (0.500)` | .500 |
| P-520 | 1 | Giants ML | .577 | .572 | .536 | .500 |
| P-520 | 2 | Eagles +1.5 | .520 | .484 | .638 | .500 |
| P-520 | 3 | Over 10.5 | .515 | .476 | .480 | .500 |
| P-520 | 4 | Under 10.5 | .485 | .524 | .520 | .500 |
| P-521 | 1 | Joventut -5.5 | .408 | .677 | `.5445 card diagnostic; ACB register NOT_YET_DERIVED` | .500 |
| P-521 | 2 | Over 179.5 | .538 | .513 | `.3922 card diagnostic; ACB register NOT_YET_DERIVED` | .500 |
| P-521 | 3 | Under 179.5 | .462 | .487 | `.6078 card diagnostic; ACB register NOT_YET_DERIVED` | .500 |
| P-521 | 4 | Breogán +5.5 | .592 | .323 | `.4555 card diagnostic; ACB register NOT_YET_DERIVED` | .500 |
| P-522 | 1 | Combined Total: Over 169.5 Points | .667 | .708 | `NOT_YET_DERIVED:acb` | .500 |
| P-522 | 2 | Tenerife -3.5 | .553 | .535 | `NOT_YET_DERIVED:acb` | .500 |
| P-522 | 3 | Combined Total: Over 179.5 Points | .457 | .480 | `NOT_YET_DERIVED:acb` | .500 |
| P-522 | 4 | Zaragoza +9.5 | .605 | .342 | `NOT_YET_DERIVED:acb` | .500 |

**Eligibility rule:** a diagnostic or `NOT_YET_DERIVED` literal is not a population baseline. Do not convert a parenthesized 0.500, card diagnostic, or settlement placeholder into an observed baseline. P-520's four numeric KBO baselines have no competition-specific population query in the current register, so their provenance is unresolved too. None of these 20 rows enters the prospective skill ledger. The issued p/q values remain frozen even where the baseline or event reference is wrong. P-520's printed ranks 3 and 4 are also reversed relative to their q values (.476 and .524); retain that issue-time ordering and record the conflict rather than silently re-ranking after the result.

## Release gate

**2026-09-29 formal performance exclusion.** P-518, P-519, P-520, P-521 and P-522 are expressly excluded from the historical and future pilot performance cohorts. Their original source claims remain reserved for custody; none is promoted by the 522-slot reconstruction. P-519's working settlement points to event 7412 although the issued event is 8942, and P-522's points to 105379 although the issued event is 105380. The corrected event references in the table above are audit findings, not silently substituted settlement receipts. P-518's process narrative conflicts with the MLB feed; P-520 lacks a stable event ID and has a q-order conflict; P-521 and P-522 need full independent terminal and issue-time checks. This exclusion may be lifted for custody only by a dated, source-backed append. It cannot retroactively make these cards prospective.

For each card, retain the original issue bytes, identify its exact event and contract, prove the issue cutoff and event state, append a sourced correction for every wrong settlement field, and attach the required independent terminal result lineages. Only then may a documented canonical import be considered. A separate prospective-baseline decision is required for each row. The user's later explicit instruction authorizes **P-523 onward for new predictions in Part 6** while these five earlier IDs remain reserved and unresolved; it does not promote them or their settlement claims.


<!-- SETTLEMENT-AUDIT-20261001 -->
## October1 reserved-card diagnostic update

AllfiveP518–P522 remain reserved and performance-ineligible. No canonical import or transaction is manufactured. Current owner final readbacks and exact frozen probabilities give the following learning diagnostics. Baselines retain the original table above and their provenance limits.

| Reserved identity | Exact final | Ranks | Mean Brier(p) | Revision | Certification gaps |
|---|---|---|---|---|---|
| P-518 | New York Mets 7–1 Washington Nationals, venue-local 2026-09-26 at Nationals Park; total 8, Mets margin +6. | WIN/LOSS/LOSS/WIN | 0.30725625 | HLR-20261001-P-518 | The official feed reconfirms the final, but independent terminal quorum, actual start and canonical issue transaction are absent. Original LIVE_ISSUED status stays excluded. |
| P-519 | Gold Coast 10.9 (69)–St Kilda 6.3 (39). Cumulative quarters GC 14,16,42,69 / SK 18,31,32,39; halftime 16–31; second half 53–8. | LOSS/WIN/LOSS/WIN | 0.41028100 | HLR-20261001-P-519 | Champion Data plus AAP original report are identifiable collections. Kimber is a distinct authored report, but independent collection of terminal facts versus the shared AFL stats feed remains unverified; do not promote it automatically as a third. Freeze 07:08:21Z follows scheduled 07:05Z; LIVE_ISSUED stays. Actual start, certified issue core and baseline lineage remain absent. |
| P-520 | Hanwha 6–2 Lotte, Sajik, September 27 17:00 KST schedule. Hanwha innings 3,0,0,0,0,1,1,0,1; Lotte 0,0,0,0,2,0,0,0,0; nine innings, total 8, Hanwha +4. | LOSS/WIN/LOSS/WIN | 0.27344475 | HLR-20261001-P-520 | Sports2i/KBO field-owner plus Kim Eun-jin/Khan original report and Newsis original reporting agree on6–2. Event-specific reporting supports three distinct terminal narratives, but formal registry independence stays UNKNOWN and actual-start evidence is absent. Missing canonical issue/source/baseline receipts forbid certification. Freeze07:58:28Z precedes scheduled08:00Z but this does not establish actual start. |
| P-521 | Río Breogán110–104Asisa Joventut in40 regulation minutes; quarter pairs29–28,27–21,19–22,35–33; HT56–49,3QT75–71; total214,Breogán+6. | LOSS/WIN/LOSS/WIN | 0.18995400 | HLR-20261001-P-521 | ACB native final plus EFE and original El Progreso terminal narratives agree; independently collected source status remains UNKNOWN in live registries. No actual-start field or canonical issue receipts; original LIVE_ISSUED remains excluded. ACB card-derived baseline rates are diagnostic, not approved population baselines. |
| P-522 | La Laguna Tenerife80–81Casademont Zaragoza; quarters18–18,20–26,27–24,15–13; HT38–44; total161,Tenerife−1. | LOSS/LOSS/LOSS/WIN | 0.27889300 | HLR-20261001-P-522 | Official ACB exact final is reconfirmed. Independent terminal quorum, actual-start semantics and canonical issue receipts remain missing; LIVE_ISSUED and missing approved baseline remain permanent exclusions. |

KBO gameId20260927HHLT0 is now bound by retained original request metadata and exact final reports; the old stable-ID-not-preserved label is superseded as a sporting identity gap only. Actual-start/cutoff, core and baseline custody are still open. P519owner ID8942 andP522ID105380 control their wrong-event working citations. See the Part6October1append and full audit report.

<!-- SETTLEMENT-READBACK-CORRECTION-20261001 -->
## Final readback correction — KBO native-ID custody

The earlier October 1 statement that KBO game ID `20260927HHLT0` was bound by retained request metadata is superseded. Readback of the actual retained `GetKboGameList` response (SHA `5f0a6c5e5345456410fcbc723872f67c673463b7446516ba35cfccdcd7b7c277`, retrieved 2026-09-30T08:35:42.562149+00:00) shows an HTML error page, with no returned game ID. The review route is also a shell; its query parameter is a candidate, not owner-confirmed identity. Require a returned field-owner game ID and certified actual-start evidence before closing those gaps. The official September 27 Sajik scoreboard still supports Hanwha 6–2 Lotte and the diagnostic L/W/L/W threshold grades; probabilities, ranks and scores are unchanged.

Correction revision: `HLR-20261001-P-520-NATIVE-ID-CORRECTION`. The original 116 review revisions remain unchanged; the separate learning chain now contains 117 revisions for 116 unique reviewed identities. No canonical settlement revision or prospective admission is created. The latest chain head is `b27ee8e0cf4f2ee8b62a62f5fe1261b2f46958b333b1a05d88af1ecfe7fa4fe1`.

The ledger also appends `CORR-20261001-P-520-native-id-comment-readback`, superseding the earlier comment's identity implication. Total historical ledger field revisions are now 50 across the same seven IDs. Diagnostic grades and scores are unchanged.
