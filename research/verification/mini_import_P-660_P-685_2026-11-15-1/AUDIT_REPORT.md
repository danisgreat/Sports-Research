# Audit · owner drop OWNER_DROP_2026-11-15 · 75 chat cards on 26 games

Written for the owner and for prompt 6. Framework: MDS-2026.11.15-v24.20, AUDIT-v1, TIMING-v3, SRC-ALT-v3, ENV-v2, ML-SEP-v1, DEEPLOSS-v1. Base HEAD `9934e37cef4ca179a7437a33e265de46cc9b5763`.

## 1. What was received

The folder `Mini logs and stuff - to be settled/` held 53 files, copied byte-identically to `research/active_minis/received/OWNER_DROP_2026-11-15/` (SHA-256 of every file compared: identical).

| Mini | Cards | Games | Format and custody |
|---|---:|---|---|
| `20261114B4496A3F` | 10 | 14 Nov set | mini-log-10 with BEGIN/END CARD markers; the bundled zip holds a byte-identical copy plus 16 reference-input and model-result files |
| `CHAT20261114DDA525E495` | 10 | 14 Nov set | heading-bounded; four earlier snapshots are byte-consistent prefixes |
| `202611148A011BE83FCC` | 10 | 14 Nov set | heading-bounded (`## Event Gnnnn`) |
| `202611148C6C0822` | 10 | 14 Nov set | heading-bounded; one staged snapshot byte-consistent |
| `20261114CHAT2988664A` | 10 | 14 Nov set | heading-bounded (`## CARD Gnnnn`) |
| `20261114EA6B2758F0` | 9 | 14 Nov set (no Hobart card) | heading-bounded; two earlier states byte-consistent |
| `20261115CHAT48A8D395742B` | 16 | 16 distinct games, 14–15 Nov | complete export: marker-bounded mini, per-card extracts, MANIFEST, SHA256SUMS |

Six chats carded the same ten 14 November games (59 cards); the export carded sixteen further games once each. No card is missing and no snapshot shows a rewritten card. Each 14 November footer reserves an unused next key; those are not cards. The owner has said future drops will use one chat per game.

## 2. Framework compliance

- **Issue status (ENV-v2).** Every card is chat-local research: NOT_ISSUED, no repository reference stage, no freeze, no PICKS_V2 lint, no ledger rows, no learning log. Every graded row is ANALYST_NOT_PRIMARY; the primary denominator is zero. The 15 November export cards were written after AUDIT-v1 took effect; they are qualitative and say UNPRICED, which is consistent with AUDIT-v1 for chat research, but no hash-bound contract review exists because none is required for non-issued research.
- **Timing (TIMING-v3, diagnostic only).** [CARD_TIMING.csv](CARD_TIMING.csv): 41 cards last recorded before the scheduled start, 22 after it, 12 with no usable clock. Most post-start records are 1–13 minutes after the start (SHL, GBL, export cards); the six Forejtek–Moeller cards were last written 66–81 minutes after the earliest listed start, while a feed showed the match postponed or suspended. No card records a not-started observation with a URL and time, so none would qualify as PRE_START_RESEARCH if issued.
- **Source access (SRC-ALT-v3).** No chat ran the repository source audit; several cards say so. The cited-URL audit for the ChatGPT reader is in [CITED_URL_ACCESS_AUDIT_CHATGPT.csv](CITED_URL_ACCESS_AUDIT_CHATGPT.csv): 451 distinct cited URLs; for the ChatGPT reader 330 ALLOWED, 41 NO_RULES_FILE, 40 BLOCKED and 40 RULES_UNKNOWN, so 80 citations (18%) were pages that reader should not have opened or whose rules were unread. Blocked hosts include nba.com, sports.yahoo.com, abc.net.au, sofascore.com, shl.se, basketkorea.com, jumpball.co.kr, kbl.or.kr, cricbuzz.com, fbref.com and several club sites; the chats should have used permitted alternates (SRC-ALT-v3).
- **Market firewall (hard rule).** No card uses odds, lines, implied probabilities or market movement as an input; every market mention is a disclaimer. Under the owner's stats-only exception, the chats cited prediction or preview pages for statistics: cricketworld match-prediction pages (3), hockeypredicts.com (2), betimate.com, tennistonic.com prediction-preview, cricketwebs.com prediction, ahockeyreport.com/predictions. These are disclosed here; AUDIT-v1 prefers statistics-only sources and requires the exact fields used, which the cards did not record.
- **Availability (AUDIT-v1 §3).** Three cards leaned on unmeasured absences (Cleveland's starters, Memphis' Jerome and Pippen, Alabama's reported QB change). All three side leans and the two related total leans lost. AUDIT-v1 would require these contracts to be UNPRICED with the absence kept as a sensitivity.
- **Opponent strength (AUDIT-v1 §2).** Two plus-handicap leans ran against the card's own opponent-strength finding (Spartak +12.5 against an unbeaten Dubai; Chicago State +16.5 after a 50-point loss to its only strong opponent). Both lost.

## 3. Results

Rows: 325 (140 WIN, 135 LOSS, 50 UNRESOLVED). Numeric rows 78, mean Brier 0.2145 (constant 0.5 scores 0.2500); by mini: CHAT20261114DDA525E495 0.205 (33 rows), 20261114B4496A3F 0.218 (32), 20261114EA6B2758F0 0.231 (13). Dependent rows; descriptive only.

| Trigger | W | L | U |
|---|---:|---:|---:|
| Top side | 34 | 22 | 6 |
| Top total | 46 | 19 | 5 |
| Rank 1 / first lean | 43 | 23 | 9 |

Rank 1 by mini (W-L): CHAT2988664A 8-1, DDA525E495 6-2, 8A011BE83FCC 6-3, 8C6C0822 6-3, EA6B2758F0 5-2, B4496A3F 5-3, export CHAT48A8D395742B 7-9.

By lean type (rows, all minis): plus handicap 33-11, minus handicap 3-2, Under 28-7, Over 17-15, moneyline/winner leans 2-12. By game, plus-handicap leans won in 8 games and lost in 6. The 14 November consensus leans did well because six chats agreed on the same underdog cushions (Mažeikiai, Poruba, Växjö, Doxa, Moeller); that is one dependent read counted six times, not six confirmations.

## 4. Findings (honest summary)

1. **Unmeasured availability was the costliest error.** Dallas -8.5, Under 227.5, Nets +4.5, Under 224.5 and Vanderbilt +14.5 all rested on reported absences priced as an edge without a measured effect. AUDIT-v1 already forbids this for issued cards; the chats did it anyway.
2. **Leans against the card's own evidence.** Five losing leans contradicted data the same card printed: Adelaide Under 150.5, Georgia Tech-Clemson Over 47.5, England Under 282.5, Niigata Over 158.5, Spartak +12.5.
3. **Coin flips recorded as leans.** Nybro ML (0.526–0.528), Alytus–Mažeikiai Over 166.5 (centre within two points of the line; lost by half a point) and similar near-50% rows were labelled rank 1 or rank 2. A centre on the line is no direction.
4. **Moneyline favourites lost often (2-12 by row).** Nybro, Malmö, Laval and Forejtek leans lost; the samples are tiny and the rows dependent.
5. **What worked.** Unders (28-7 by row) and the 14 November underdog cushions. The cards' numeric rows were better than a constant 0.5 on average (0.2145), but every number is an uncalibrated chat scenario.
6. **Custody was good.** Every snapshot is a byte-consistent prefix of its final mini; the export included per-card extracts and hashes; no original is missing.
7. **Settlement gaps.** Tappara U20 v HPK U20 has no final on any permitted page (all 24 rows UNRESOLVED). Cricket phase scores (WBBL six-over, ODI five-over) and the Kashiwa corners are not on permitted pages. Twelve events rest on one permitted lineage (evidence C).

## 5. Proposals (PROPOSED_NOT_TESTED; no rule changes here)

- Treat a qualitative lean whose own printed centre sits within the line's noise as NO_DIRECTION, so it is never ranked. (Needs a registered definition before testing; FREEZE-v1 applies.)
- In chat briefs, repeat AUDIT-v1 §2–3 explicitly: absences and plus handicaps need measured evidence or the row stays UNPRICED.
- Ask chats to record the exact fields taken from any prediction or preview page, as AUDIT-v1 already requires.

## 6. What this audit cannot show

No predictive advantage is established. All 75 cards are research, so they enter CARD-TRAIN-v1 as ANALYST_NOT_PRIMARY rows and never as issued forecasts. ASSESS-100 eligibility from this drop is zero.
