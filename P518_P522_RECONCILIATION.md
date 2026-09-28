# P-518–P-522 custody and source reconciliation

**Audit date:** 2026-09-28. **State:** OPEN. Part 5 is canonical through P-517. P-518–P-522 are reserved claims in the [frozen working mini log](prediction%20logs/PREDICTION_MINI_RUNNING_LOG_P518_ONWARD.md), not canonical imports. The mini log's SHA-256 is `c4d497bf339010eae2ff5df23a2d76290983585671666e74791618342565cf30`; its original issue text and settlement text have not been changed in this repair. All five remain **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE**. The next canonical ID remains **HOLD**.

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

For each card, retain the original issue bytes, identify its exact event and contract, prove the issue cutoff and event state, append a sourced correction for every wrong settlement field, and attach the required independent terminal result lineages. Only then may a documented canonical import be considered. A separate prospective-baseline decision is required for each row. Until all five ID collisions are resolved, `P-523` is **not** an authorized next ID; use a TMP ID for new work.
