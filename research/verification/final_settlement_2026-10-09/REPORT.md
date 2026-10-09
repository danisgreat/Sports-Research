# Final settlement of all pending records — 2026-10-09

**Directive (user, 2026-10-09).** Settle every pending log. Where details cannot be found, settle anyway. Any record holding only a temporary ID takes the next canonical ID in chronological order. Only the top two ranked picks can count as a win, and a Rank-1 failure requires a deep, thorough retrospection.

## Outcome

- **Records settled:** 72: the 65 records of the 2026-10-08 carryover register plus P-550–P-556. No sporting settlement obligation remains open.
- **IDs:** none consumed. Every `TMP-`/`LOCAL-` alias in the repository already maps to a canonical P-ID, so no record needed a new one. Next canonical ID before and after: **P-557 → P-557**.
- **Log writes:** `prediction logs/PREDICTION_LOG_COMBINED_7.md` grew 491,009 → 646,033 bytes, append-only (the prefix was verified byte-identical). One consolidated block holds 50 records: P-126–P-522, which have no ledger parent, and P-538–P-549, whose rollover verifier pins exactly twelve ledger addenda. The other 22 ledger cards (P-523–P-537, P-550–P-556) each received a dated addendum through `research.operations.log_card`, adding 44 ledger records.
- **Top-two result (71 forecast cards):** 79 counted wins from 134 live top-two rows (59.0%). Rank 1: 40 W / 28 L / 3 VOID. Rank 2: 39 W / 27 L / 5 VOID. Card classes: 27 all won, 26 split, 15 all lost, 3 void. Hit@2 53/68.
- **Deep Rank-1 retrospections:** 28, one in each failed record's settlement.
- **Evidence grades (313 rows):** A 168, B 107, C 13, E 2, OP 16, X 7.
- **Certification:** unchanged. Every record remains `NOT_CERTIFIED` and performance-ineligible. This is a research-ledger closure, not operator certification.

## Settle-anyway evidence hierarchy

| Code | Meaning |
|---|---|
| A | Official / field-owner terminal record for the target field |
| B | Structured provider (ESPN, FotMob, league data partner) or multi-source agreement for the target field; official score |
| C | Best-available single-secondary, conflicted or provisional evidence adopted as final under the settle-anyway directive |
| E | Estimated from a partial measurement that bounds the target field; confidence stated in the basis |
| OP | Sporting endpoint known; operator rule absent; framework default or the card's own frozen working assumption applied |
| X | No admissible data; row settled VOID |

Framework defaults applied under OP: a missing operator definition does not block sporting settlement (CURRENT_RULES); a tennis retirement voids games rows (RULES_TENNIS); runs scored before a stop count (RULES_CRICKET); the card's own frozen full-match working assumption for hockey totals (P-200).

## Corrections found while settling

- **Rank-index `P` literal.** Five rows coded `P` (push) in `GAME_PREDICTION_RANK_LOG.csv` are blank-contract corner rows, not pushes: P-407 R1 (WIN), P-409 R2 (WIN), P-410 R5 (WIN), P-419 R5 (LOSS), P-430 R5 (LOSS). They are settled from their original settlement tables. The CSV itself is unchanged (it is a frozen learning artefact).
- **Copied R1 blocks.** The Part 6 settlement-refresh "R1. Original prediction" text for P-539–P-545 repeats P-538's ranking. Each card's own rank table governs; the final settlement uses each card's actual ranks.
- **P-519.** The original 50–22 settlement was fabricated. The AFLW owner final is 69–39 (total 108), so Rank 1 (Under 89.5) is a LOSS.
- **P-136 and P-540.** Both retired mid-match. All game rows are VOID under the framework retirement convention, and both winner calls are correct.
- **P-418.** The original ranked contracts are not preserved anywhere in the repository or its history, so the card is VOID. The single-secondary final, Drukpa 1–3 RTC, is recorded.
- **Stale reservation.** The 2026-10-08 register still lists P-550 as `LOCAL_ONLY_PENDING_IMPORT`. It was imported on 2026-10-09; `register.json` here records it as resolved.

## Register pointer

`research/current_settlement_register.json` now selects this folder's `register.json` (kind `settled`, schema 2). The earlier 2026-10-08 carryover register is not lost: the pointer's `history` pins it by SHA-256, and `verify_carryover_review` and `verify_rollover` verify that snapshot through `settlement_register.pinned` and `in_lineage` instead of requiring it to be the current selection (GOV-01). A later settlement can therefore move the pointer again without touching a dated verifier.

## Per-record result

| ID | Event | R1 | R2 | Counted | Card class | Winner call | Deep R1 retro |
|---|---|:-:|:-:|---|---|---|:-:|
| P-126 | Sikkim Aakraman FC vs Sikkim Boys Club | W | V | 1/1 | TOP2_ALL_WON | CORRECT | — |
| P-136 | James Duckworth vs Arthur Fery | V | V | 0/0 | VOID | CORRECT | — |
| P-148 | Toluca Femenil vs Leon Femenil | L | L | 0/2 | TOP2_ALL_LOST | CORRECT | yes |
| P-149 | Colorado Rapids 2 vs Ventura County FC | W | W | 2/2 | TOP2_ALL_WON | CORRECT | — |
| P-166 | Melbourne Mustangs vs Canberra Brave | W | W | 2/2 | TOP2_ALL_WON | CORRECT | — |
| P-176 | Amiens SC vs FC Versailles | L | L | 0/2 | TOP2_ALL_LOST | INCORRECT | yes |
| P-178 | AS Cannes vs Le Puy-en-Velay | W | L | 1/2 | TOP2_SPLIT | CORRECT | — |
| P-179 | Thionville Lusitanos vs Paris 13 Atletico | W | L | 1/2 | TOP2_SPLIT | NOT_AUDITED | — |
| P-200 | Herning Blue Fox vs Rungsted Seier Capital | L | W | 1/2 | TOP2_SPLIT | CORRECT | yes |
| P-217 | Trinbago Knight Riders vs Guyana Amazon Warriors | L | L | 0/2 | TOP2_ALL_LOST | NOT_AUDITED | yes |
| P-233 | Beijing Guoan vs Lanzhou Longyuan Athletic | W | W | 2/2 | TOP2_ALL_WON | NOT_AUDITED | — |
| P-234 | Dalian Yingbo vs Shanghai Shenhua | L | W | 1/2 | TOP2_SPLIT | NOT_AUDITED | yes |
| P-235 | Shandong Taishan vs Shanghai Port | W | W | 2/2 | TOP2_ALL_WON | NOT_AUDITED | — |
| P-250 | Yunnan Yukun vs Chongqing Tonglianglong | L | V | 0/1 | TOP2_ALL_LOST | CORRECT | yes |
| P-251 | Sassuolo vs Frosinone | W | L | 1/2 | TOP2_SPLIT | NOT_AUDITED | — |
| P-255 | Inter Women vs VfL Wolfsburg Women | W | W | 2/2 | TOP2_ALL_WON | NOT_AUDITED | — |
| P-256 | Paris Saint-Germain Women vs Eintracht Frankfurt Women | W | W | 2/2 | TOP2_ALL_WON | NOT_AUDITED | — |
| P-265 | Toluca vs Club Leon | W | L | 1/2 | TOP2_SPLIT | NOT_AUDITED | — |
| P-274 | San Francisco Giants @ Pittsburgh Pirates | L | W | 1/2 | TOP2_SPLIT | NOT_AUDITED | yes |
| P-341 | BUL FC vs Ntugasaze FC | W | L | 1/2 | TOP2_SPLIT | CORRECT | — |
| P-342 | MSK Novohrad Lucenec vs KFC Komarno | L | L | 0/2 | TOP2_ALL_LOST | CORRECT | yes |
| P-368 | Al Jazira vs Al Nasr | W | W | 2/2 | TOP2_ALL_WON | NOT_AUDITED | — |
| P-369 | Dubai United vs Shabab Al Ahli | L | L | 0/2 | TOP2_ALL_LOST | NOT_AUDITED | yes |
| P-377 | Xelaju MC vs Coban Imperial | L | L | 0/2 | TOP2_ALL_LOST | NOT_AUDITED | yes |
| P-399 | Genoa vs Frosinone | W | W | 2/2 | TOP2_ALL_WON | NOT_AUDITED | — |
| P-401 | IFK Goteborg vs Halmstads BK | W | W | 2/2 | TOP2_ALL_WON | NOT_AUDITED | — |
| P-407 | Club Brugge vs Royal Antwerp | W | W | 2/2 | TOP2_ALL_WON | NOT_AUDITED | — |
| P-409 | Lille OSC vs ESTAC Troyes | W | W | 2/2 | TOP2_ALL_WON | CORRECT | — |
| P-410 | RB Leipzig vs Hamburger SV | W | W | 2/2 | TOP2_ALL_WON | NOT_AUDITED | — |
| P-418 | Drukpa FC vs Royal Thimphu College FC | V | V | 0/0 | VOID | NOT_AUDITED | — |
| P-419 | Djurgardens IF vs GAIS | W | W | 2/2 | TOP2_ALL_WON | CORRECT | — |
| P-430 | Al Ain vs Al Nassr | L | W | 1/2 | TOP2_SPLIT | INCORRECT | yes |
| P-492 | San Diego Padres @ Los Angeles Dodgers | L | L | 0/2 | TOP2_ALL_LOST | CORRECT | yes |
| P-518 | New York Mets @ Washington Nationals | W | L | 1/2 | TOP2_SPLIT | NOT_AUDITED | — |
| P-519 | Gold Coast Suns vs St Kilda (AFLW) | L | W | 1/2 | TOP2_SPLIT | NOT_AUDITED | yes |
| P-520 | Hanwha Eagles @ Lotte Giants | L | W | 1/2 | TOP2_SPLIT | NOT_AUDITED | yes |
| P-521 | Rio Breogan vs Joventut | L | W | 1/2 | TOP2_SPLIT | NOT_AUDITED | yes |
| P-522 | La Laguna Tenerife vs Casademont Zaragoza | L | L | 0/2 | TOP2_ALL_LOST | NOT_AUDITED | yes |
| P-523 | Oriente Petrolero vs The Strongest | W | W | 2/2 | TOP2_ALL_WON | INCORRECT | — |
| P-524 | KT Wiz @ Kia Tigers | L | W | 1/2 | TOP2_SPLIT | CORRECT | yes |
| P-525 | Chunichi Dragons @ Hiroshima Toyo Carp (G25) | W | L | 1/2 | TOP2_SPLIT | CORRECT | — |
| P-526 | Hanwha Eagles @ Samsung Lions | W | W | 2/2 | TOP2_ALL_WON | CORRECT | — |
| P-527 | Hapoel Tel Aviv vs Real Madrid | L | W | 1/2 | TOP2_SPLIT | INCORRECT | yes |
| P-528 | Grand Rapids Griffins @ Cleveland Monsters | W | W | 2/2 | TOP2_ALL_WON | CORRECT | — |
| P-529 | Philadelphia Flyers @ New Jersey Devils | W | W | 2/2 | TOP2_ALL_WON | CORRECT | — |
| P-530 | Philadelphia Phillies @ Atlanta Braves (NL WC G3) | W | W | 2/2 | TOP2_ALL_WON | CORRECT | — |
| P-531 | Indiana Fever @ Las Vegas Aces (R1 G3) | L | L | 0/2 | TOP2_ALL_LOST | CORRECT | yes |
| P-532 | Tasmania JackJumpers vs Melbourne United | L | W | 1/2 | NO_FORECAST | NOT_ISSUED | — |
| P-533 | KIA Tigers @ LG Twins | W | L | 1/2 | TOP2_SPLIT | CORRECT | — |
| P-534 | Sydney Roosters vs Newcastle Knights (Grand Final) | L | L | 0/2 | TOP2_ALL_LOST | CORRECT | yes |
| P-535 | Panathinaikos AKTOR vs Vikos Falcons | W | W | 2/2 | TOP2_ALL_WON | CORRECT | — |
| P-536 | FC Bayern Munchen vs EWE Baskets Oldenburg | W | W | 2/2 | TOP2_ALL_WON | CORRECT | — |
| P-537 | Kyrgyzstan vs Lebanon | W | W | 2/2 | TOP2_ALL_WON | INCORRECT | — |
| P-538 | Florida Panthers @ Los Angeles Kings | W | W | 2/2 | TOP2_ALL_WON | CORRECT | — |
| P-539 | Aleksandar Kovacevic vs Matteo Berrettini | W | L | 1/2 | TOP2_SPLIT | CORRECT | — |
| P-540 | Adrian Mannarino vs Nikoloz Basilashvili | V | V | 0/0 | VOID | CORRECT | — |
| P-541 | Mattia Bellucci vs Yi Zhou | L | L | 0/2 | TOP2_ALL_LOST | INCORRECT | yes |
| P-542 | Adelaide 36ers vs Melbourne United | W | W | 2/2 | TOP2_ALL_WON | CORRECT | — |
| P-543 | Hiroshima Toyo Carp @ Hanshin Tigers | W | W | 2/2 | TOP2_ALL_WON | CORRECT | — |
| P-544 | Doosan Bears @ LG Twins | L | W | 1/2 | TOP2_SPLIT | CORRECT | yes |
| P-545 | Hanwha Eagles @ Kiwoom Heroes | W | L | 1/2 | TOP2_SPLIT | INCORRECT | — |
| P-546 | Samsung Lions @ KT Wiz | W | L | 1/2 | TOP2_SPLIT | CORRECT | — |
| P-547 | NC Dinos @ SSG Landers | L | W | 1/2 | TOP2_SPLIT | CORRECT | yes |
| P-548 | Busan KCC Egis vs Daegu KOGAS Pegasus | L | W | 1/2 | TOP2_SPLIT | CORRECT | yes |
| P-549 | Foshan Nanshi vs Guangxi Hengchen | L | L | 0/2 | TOP2_ALL_LOST | INCORRECT | yes |
| P-550 | Edmonton Oilers @ Anaheim Ducks | W | L | 1/2 | TOP2_SPLIT | CORRECT | — |
| P-551 | Adolfo Daniel Vallejo vs Valentin Royer | L | L | 0/2 | TOP2_ALL_LOST | CORRECT | yes |
| P-552 | Cairns Taipans vs Brisbane Bullets | W | L | 1/2 | TOP2_SPLIT | CORRECT | — |
| P-553 | Kobe Storks vs Chiba Jets | L | W | 1/2 | TOP2_SPLIT | INCORRECT | yes |
| P-554 | Nagasaki Velca vs Shinshu Brave Warriors | W | W | 2/2 | TOP2_ALL_WON | INCORRECT | — |
| P-555 | Vit Kopriva vs Zizou Bergs | L | L | 0/2 | TOP2_ALL_LOST | CORRECT | yes |
| P-556 | Cameron Norrie vs Dalibor Svrcina | W | W | 2/2 | TOP2_ALL_WON | INCORRECT | — |

## Files

| File | Role |
|---|---|
| `settlement_table.json` | Every row: grade, evidence code and basis (the settlement source of truth) |
| `summary.json` | Derived diagnostics (`build/build_settlement.py`) |
| `register.json` | Final settlement register (all 72 closed; certification unchanged) |
| `apply_receipt.json` | Before/after hashes, ledger growth, next ID |
| `build/rank1_retrospectives.py` | The 28 deep Rank-1 retrospections |
| `build/tennis_overdispersion_check.py` | Reproduction of the P-551/P-555 tennis distributions with and without match-level variance |
| `build/build_addenda.py`, `build/apply_settlement.py`, `build/build_report.py` | Rendering, application and this report |
| `build/requests/`, `build/sources/`, `build/older_block.md` | Exact appended bodies (22 ledger addenda; 50-record consolidated block) |

Reproduce the analysis: `python -B research/verification/final_settlement_2026-10-09/build/build_settlement.py`, then `build_addenda.py` (rendering is deterministic). `apply_settlement.py` is the one-time writer and refuses to run unless the next ID is P-557 and no transaction is pending.
