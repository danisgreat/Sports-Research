# Identity conflict research intake — Urawa Red Diamonds vs Kashima Antlers

**Receipt:** `LOCAL-INTAKE-09-IDENTITY-CONFLICT` (chat-local tracking label only; **not** an official `LOCAL-...-G####` key).  
**Method/reference:** MDS-2026.11.11-v24.15 / CR-2026.11.11-R3 / P-2026.11.11-v24.13; GitHub main `4d8bd1771d20974bcbfc7c694a009cd44e95a693` accessed strictly READ-ONLY.  
**Document created UTC:** `2026-11-11T10:18:16+00:00`.  
**Status:** `FIXTURE_IDENTITY_CONFLICT / RESEARCH_ONLY / NO_FORECAST / NOT_ISSUED / UNSETTLED / NOT_GRADED`.

## A1. Original event request and identity gate

- Owner-supplied: **Urawa Red Diamonds vs Kashima Antlers**, **2026 Japan J.League Cup**, **11 November 2026, 21:30 AEDT**, estimated and subject to delays.
- Official J.League Cup quarter-final first leg at **19:30 JST = 21:30 AEDT**: **Urawa Red Diamonds vs Cerezo Osaka**, **Saitama Stadium 2002**. Official J.League match: https://www.jleague.jp/match/leaguecup/2026/111102/ ; also host club https://www.urawa-reds.co.jp/en/ .
- Official J.League Cup quarter-final first leg at **19:00 JST = 21:00 AEDT**: **Yokohama F. Marinos vs Kashima Antlers**, **Nissan Stadium**. Official J.League match: https://www.jleague.jp/match/leaguecup/2026/111103/ ; also Kashima club https://www.antlers.co.jp/en/ .
- League schedule corroboration: https://www.jleague.jp/en/leaguecup/match/ and https://www.jleague.jp/leaguecup/match/ .
- **Conclusion:** no official same-event pairing Urawa vs Kashima at the requested date and time. This is an **identity mismatch**, not evidence of a cancelled, postponed or void fixture. Native event ID cannot be assigned to the requested pairing.

## A2. Exact supplied contracts and disposition

The six requested directions are preserved literally. **No number is calculated or published** because the contract's event does not exist in the verified schedule.

| Supplied contract | Method category | Price/disposition |
|---|---|---|
| First half Over 0.5 goals | PERIOD / first half, regulation | `UNPRICED / UNSUPPORTED: EVENT_IDENTITY_CONFLICT` |
| First half Under 0.5 goals | PERIOD / first half, regulation | `UNPRICED / UNSUPPORTED: EVENT_IDENTITY_CONFLICT` |
| Full time Over 2.5 goals | TOTAL / 90min + stoppage | `UNPRICED / UNSUPPORTED: EVENT_IDENTITY_CONFLICT` |
| Full time Under 2.5 goals | TOTAL / 90min + stoppage | `UNPRICED / UNSUPPORTED: EVENT_IDENTITY_CONFLICT` |
| Full time Over 10.5 corners | CORNERS / 90min + stoppage, provider count unknown | `UNPRICED / UNSUPPORTED: EVENT_IDENTITY_CONFLICT` |
| Full time Under 10.5 corners | CORNERS / 90min + stoppage, provider count unknown | `UNPRICED / UNSUPPORTED: EVENT_IDENTITY_CONFLICT` |

No reference, Poisson/Dixon-Coles grid, lineup adjustment, corners count model, price, or Monte Carlo simulation was run for this incorrect event. No alternative pairing or supplied line has been silently substituted. No outcome information was used or settlement performed.

## A3. Evidence intake, limitations and required correction

- Independently consistent original field-owner descriptions: J.League fixtures, Urawa club and Kashima club.
- Discovery and page content were accessed through search/browser; a same-time executable `ml source-audit --reader ChatGPT-User` and immutable original-retrieval capture were **not** performed. This is a chat-local identity-intake record, not a conforming admitted EXT-v3 source packet.
- Exact original first-play time for either real fixture: `NOT_VERIFIED`. User's estimated local kickoff pertains to Urawa–Cerezo.
- To resume **fresh** research, select one actual match (Urawa–Cerezo or Yokohama FM–Kashima), retaining original contract thresholds only on explicit owner confirmation. Each game then requires its own historical/availability/lineup/corner evidence and an actual time-qualified forecast protocol.
- A hypothetical Urawa–Kashima match requires a different separately verified date, competition and native fixture identity.

## A4–A9. Completion/gate matrix and custody

| Gate | Status |
|---|---|
| Competition and date | VERIFIED |
| Requested participants as one native fixture | **FAILED** |
| Alternative fixtures identified | VERIFIED from official sources |
| Exact supplied rows preserved | YES (6 directions) |
| Pre-match scores/lineups/H2H/pace/corner research | NOT_APPLICABLE until identity resolved |
| Starting lineup availability | NOT_VERIFIED |
| Reference, distribution, p_card, PICKSV2 and kit receipt | NOT_COMPUTED |
| Formal issue / freeze / commit / canonical ID | NONE |
| Results, settlement, grade | **NOT_PERFORMED** |
| GitHub mutations | **NONE** |
| Local note status | `LOCAL_INTAKE_ONLY / NO_FORECAST / UNSETTLED` |

**No claim of a successfully published 2026-11-11 pre-start prediction is made.** Preserve existing mini receipts and footer; do not allocate event keys or count this as a prospective scored match.
