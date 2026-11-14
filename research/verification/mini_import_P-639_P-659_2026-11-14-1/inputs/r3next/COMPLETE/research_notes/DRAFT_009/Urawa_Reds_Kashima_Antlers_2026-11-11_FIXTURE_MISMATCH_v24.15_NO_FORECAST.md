# Urawa Red Diamonds vs Kashima Antlers — requested 11 November 2026

## v24.15 local research record / INVALID FIXTURE / NO_FORECAST

- Created UTC: `2026-11-11T10:18:11+00:00` (actual local file capture; does not establish original public source publication).
- Read-only repository: `danisgreat/Sports-Research` HEAD `4d8bd1771d20974bcbfc7c694a009cd44e95a693`.
- User-specified: J.League Cup, Wednesday 11 November 2026 at 21:30 AEDT = 19:30 JST; Urawa vs Kashima; combined first-half goals O/U 0.5; full-time goals O/U 2.5; full-time corners O/U 10.5.
- Research disposition: `EVENT_IDENTITY_CONFLICT / NO_FORECAST / RESEARCH_DRAFT_ONLY / NOT_ISSUED / NOT_SETTLED / NOT_PERFORMANCE_ELIGIBLE`.
- No valid EV2 key, issuer local key, game-native ID, numerical prices, official forecast receipt, result or grade.

## A1. Exact-event identity — FAIL (critical)

The **official 2026–27 J.League YBC Levain Cup quarter-final first-leg schedule** does not contain a Urawa Reds–Kashima Antlers match on 11 November 2026. It specifies these distinct games:

| Verified real fixture | Kickoff JST | Kickoff AEDT | Venue |
|---|---|---|---|
| **Urawa Red Diamonds vs Cerezo Osaka** | 11 Nov 19:30 | 11 Nov 21:30 | Saitama Stadium 2002 |
| **Yokohama F. Marinos vs Kashima Antlers** | 11 Nov 19:00 | 11 Nov 21:00 | Nissan Stadium, Yokohama |

The user's stated kickoff aligns with the actual Urawa–Cerezo match, but the named away side matches the actual Yokohama–Kashima match. These facts do not uniquely specify which real event was intended. No automatic substitution is allowed.

**Official evidence (pregame schedules, not target-game results):**
- J.League official Levain Cup schedule: https://www.jleague.jp/en/leaguecup/match/
- J.League official archive for Nov 11: https://data.j-league.or.jp/SFMS01/search?competition_years=2026&section_months=11
- Urawa club fixture information: https://www.urawa-reds.co.jp/game/info/000052.html
- Kashima club fixture schedule: https://www.antlers.co.jp/pages/games
- Urawa–Cerezo event page: https://www.jleague.jp/match/leaguecup/2026/111102/

## A2. All exact requested directions — no numerical price

| Original proposed directional contract | v24.15 status | Exact reason |
|---|---|---|
| First half goals Over 0.5 | `UNPRICED / UNSUPPORTED` | No verified Urawa–Kashima fixture at supplied date/competition; cannot attach a distribution to a non-identified event. |
| First half goals Under 0.5 | `UNPRICED / UNSUPPORTED` | No verified Urawa–Kashima fixture at supplied date/competition; cannot attach a distribution to a non-identified event. |
| Full-time goals Over 2.5 | `UNPRICED / UNSUPPORTED` | No verified Urawa–Kashima fixture at supplied date/competition; cannot attach a distribution to a non-identified event. |
| Full-time goals Under 2.5 | `UNPRICED / UNSUPPORTED` | No verified Urawa–Kashima fixture at supplied date/competition; cannot attach a distribution to a non-identified event. |
| Full-time corners Over 10.5 | `UNPRICED / UNSUPPORTED` | No verified Urawa–Kashima fixture at supplied date/competition; cannot attach a distribution to a non-identified event. |
| Full-time corners Under 10.5 | `UNPRICED / UNSUPPORTED` | No verified Urawa–Kashima fixture at supplied date/competition; cannot attach a distribution to a non-identified event. |

No 1H goals, 90-minute goals or corners pick is issued. All six contract directions are explicitly retained without a probability or rank.

## A3. Pre-event form, recent windows, H2H

Not calculated for the alleged pairing because a live event with this identity cannot be verified. Team histories would belong to either of two different real games; mixing them to price the requested non-fixture is a scope error. No L5/L10/L15/L20, opponent adjustments or recent H2H rows are claimed here.

## A4. Starting lineups, bench, injuries and coaches

Not mapped to an eligible event. No official lineup or player-status confirmation is claimed for the fictitious pairing. Verified lineup/availability would have to attach to one actual cup quarter-final and an independently confirmed native event ID.

## A5. Venue, weather, rest, tie and tactics

Urawa at Saitama Stadium and Kashima away at Yokohama's Nissan Stadium belong to **different matches**. Any venue advantage, match-window weather, travel, cup tie-first-leg strategy and tactical mechanism must be determined for an identified actual fixture. None is priced against the user's combined pairing.

## A6. Rules and contracts

The intended markets are first-half goals O/U 0.5, full-time goals O/U 2.5, and full-time corners O/U 10.5. Standard 45/90-minute endpoints versus any operator-specific settlement rules remain assumptions, not a verified operator contract. This ambiguity is subordinate to the fatal fixture identity conflict. Corners also lack a confirmed exact-provider definition/count distribution. No simulation or Poisson/Dixon–Coles model run.

## A7. Model, probabilities, and selection disposition

- Active control: `MDS-2026.11.11-v24.15 / CR-2026.11.11-R3 / P-2026.11.11-v24.13 / EXT-v3`.
- No immutable manifest, reconciled event ID, calculation kit receipt, reference distribution or official pre-start forecast freeze exists for this non-fixture.
- Result: `NO_FORECAST`, not merely `NO_STRONG_PICK`; no favourite, most-likely total, spread or qualified ranking can be stated for the requested match.
- Exact six directional contracts are retained as `UNPRICED / UNSUPPORTED` in the local research record, **not** in the repository's official `PICKS_V2`.

## A8. Provenance, timing and evidence limitations

The public official schedule was accessed during the user's pre-event research conversation on 11 Nov 2026. This file uses a *current* file creation time and does not claim earlier official issue or publication. The official schedule corroborates the fixture mismatch, including home/away, competition and times; no target-game score, live statistics or outcome was used. No local `python -m ml source-audit`, repository source-collector review or v24.15 LANE_RETURN packet was executed for this research note. No result settlement attempted.

## A9. Research completion and custody matrix

| Requirement | Disposition |
|---|---|
| Verify exact requested competition/time | PARTIAL: competition/date/time exist, but opponent pairing invalid |
| Verify identity and native event | `FAILED_EVENT_IDENTITY` / NOT_AVAILABLE |
| Confirm candidate real match alternatives | DONE: official schedule and club sites |
| Supply all exact requested contract directions | DONE: 6 directions retained as unpriced |
| Compute result/scores, settle | **NOT_ATTEMPTED / NOT_SETTLED** |
| Use outcome for pregame evidence | NO |
| Run v24.15 distribution or primary simulation | NOT_EXECUTED (identity blocker) |
| Freeze, issue, assign local key/P-ID, commit | NOT_EXECUTED / NOT_AUTHORIZED |
| Update published GitHub mini | NO: read-only |
| Update independent local research mini | This record is appended as local DRAFT-009 only |

**Next valid research action:** identify whether the owner intends Urawa vs Cerezo Osaka or Yokohama F. Marinos vs Kashima Antlers, and confirm that any supplied contracts apply to that actual fixture. Do not infer an intended opponent solely from kick-off or team name. No settlement and no historical backdating.
