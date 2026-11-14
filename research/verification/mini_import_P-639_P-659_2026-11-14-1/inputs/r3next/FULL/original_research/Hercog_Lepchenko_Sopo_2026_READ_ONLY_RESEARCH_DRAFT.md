# READ_ONLY_DRAFT — Polona Hercog vs Varvara Lepchenko, Sopó WTA 125

**Status:** NOT_ISSUED · NOT_FROZEN · NOT_COMMITTED · NOT_PUSHED · NO CANONICAL ID · NO LOCAL EVENT ID ALLOCATED  
**Repository reference (read-only):** `danisgreat/Sports-Research`, published branch `main` at `f79559b45183ca63a2ce5fc2611321975bae744f`. Current published active mini: `research/active_minis/20261109R3NEXT.md`; its unallocated next-local-key field is `LOCAL-20261109R3NEXT-G0001`. Existing writer lease belongs to repository agent.  
**Framework:** MDS-2026.11.10-v24.12, P-2026.11.10-v24.10, SEL-2026.10.22-v4; Tennis SFA-TENNIS; research-only, no market input.  
**Research point-in-time:** 10 November 2026 (Australia/Melbourne). Web results were observed during this chat. Source-publication, page-refresh and capture times are not always independently verifiable.

## A1. Identity, state, timing
- Players: Polona Hercog (Slovenia, right-handed) vs Varvara Lepchenko (United States, left-handed).
- WTA 125 Cundinamarca Open / DIRECTV Open Presentado por Compesar, Sopó, Colombia; round of 32 / round 1; outdoor clay; best-of-three singles.
- Scheduled 9 November 2026 15:00 UTC = 9 November 10:00 COT (UTC-05) = 10 November 02:00 AEDT (UTC+11), Court 2. Estimated match-specific actual start and first-play time: NOT_VERIFIED.
- WTA tournament status: IN PROGRESS (tournament-level, not match-level). WTA-associated schedule lists the exact match as scheduled. TennisTemple lists all 9 November matches as 'Postponed Suspended'; conflicting source UI and no specific official postponement verified. Do not treat either as proof of actual first play.
- Native event identifier: NOT_VERIFIED. Data sources: https://www.wtatennis.com/tournaments/1181/sopo-125/2026 ; https://www.wtaschedule.com/wta-matches-today ; https://en.tennistemple.com/competitions/sopo-2026/128051/orderofplay .

## A2. Frozen request and contract universe (as text only; NOT a frozen issued card)
- Hercog ML / Lepchenko ML: best-of-three match winner, subject to operator's withdrawal/retirement convention (not supplied).
- Hercog **-1.5 games**: total games Hercog - total games Lepchenko >= 2. Not a set handicap.
- Lepchenko **+1.5 games**: total games Hercog - total games Lepchenko <= 1. Complement of Hercog -1.5 on completed integer-scored matches; treatment at retirement unknown.
- Combined **Over 21.5 games**: completed-match total >= 22.
- Combined **Under 21.5 games**: completed-match total <= 21. These two are complements on completed games-only matches; retirement handling unknown.
- Market or price inputs: NOT USED. No other contracts were requested.

## A3. Research, form and history
**Latest published player level:** TennisExplorer reports 2026 clay 23–19 Hercog and 9–11 Lepchenko, with differences in covered competition levels and qualifying potentially material. WTA current singles rankings near 201 and 199, respectively. Do not equate unadjusted clay records with match probabilities.

**Recent form (source-covered, provisional):** Manual reading of dated match entries (TennisTemple player pages and TennisDB for Lepchenko). Retired and walkover matches excluded from the completed-match counts; match-score parsing and exhaustive competition harmonisation have not been independently audited.

| Window | Hercog W-L | Lepchenko W-L |
|---|---:|---:|
| L5 completed | 2–3 | 2–3 |
| L10 completed | 5–5 | 3–7 |
| L15 completed | 7–8 | 5–10 |
| L20 completed | 10–10 (provisional) | 6–14 (provisional) |

Hercog recorded a heavy 0–6, 1–6 loss to Leyre Romero Gormaz on 2 Nov, after 6–0, 6–0 qualifying win on 1 Nov, and a loss to Valeriya Strakhova on 29 Oct. Lepchenko's recent listed defeats include Renata Zarazua on 27 Oct and Julieta Pareja on 16 Oct; a 20 Oct Austin walkover is excluded as a completed sporting result. The players' opponent levels, older WTA 125 results and lower ITF events are not interchangeable without adjustment. Sources: https://en.tennistemple.com/player/polona-hercog/results ; https://en.tennistemple.com/player/varvara-lepchenko/results ; https://tennis-db.com/wta/players/balldontlie_wta:304/varvara-lepchenko/matches .

**Head-to-head:** Seven known encounters, Hercog 4 wins and Lepchenko 3 wins, corroborated by TennisExplorer/Tennis Insight and Tennis Abstract's draw record. Clay H2H 3–0 Hercog (2009 Cuneo, 2012 Charleston, 2023 Montevideo). Most meetings are too old to serve as fresh form; the 2016 match included a retirement. Latest completed meeting: Hercog d. Lepchenko 7–6(2), 6–2 in Montevideo in December 2023. https://www.tennisexplorer.com/match-detail/?id=3373803 ; https://www.tennisabstract.com/current/2026WTASopo125.html .

**Availability/workload:** Both named in current draw. No primary, independently corroborated match-specific medical/withdrawal bulletin or player condition attestation recovered. Fitness NOT_VERIFIED (not assumed healthy). Hercog competed 1/2 Nov in Cali after October WTA 125 activity; Lepchenko had a tournament entry in late October; exact travel/altitude adaptation and actual late practice status NOT_VERIFIED. Weather forecasts and event-status providers differ; no measured court-level conditions established. Official venue: outdoor clay; court-level wind and moisture NOT_VERIFIED.

## A4. Numerical method and sensitivity
**Verified benchmark source:** Tennis Abstract WTA Elo, updated 9 November 2026: Hercog overall Elo 1528.3 and cElo 1510.8; Lepchenko overall Elo 1547.9 and cElo 1515.3. Under PROBABILITY_TOOLKIT §6, blended surface ratings are 1519.55 Hercog and 1531.60 Lepchenko. Hence 

`p_ELO(Hercog) = 1 / (1 + 10^((1531.60-1519.55)/400)) = 0.4826656059`;
`p_ELO(Lepchenko) = 0.5173343941`.

**Critical distinction:** These are a rating-reference calculation only, **not** a frozen, issued `ANALYST_PRIMARY_V1` match probability, and not a coherent score-distribution output. Tennis Abstract's separately published tournament-draw benchmark indicates 50.6% Hercog and 49.4% Lepchenko, reinforcing that both ratings/benchmark mechanisms are effectively a coin flip rather than demonstrating a meaningful edge. Do not use independent predictors as features in the card. https://tennisabstract.com/reports/wta_elo_ratings.html ; https://www.tennisabstract.com/current/2026WTASopo125.html .

**Point-to-match / set-score tree:** NOT_COMPUTED. Current surface-, opponent- and event-level numerators and denominators for each player's serve and return points and validated opponent-adjusted hold rates are not available in comparable form. Official WTA site has some Lepchenko cumulative stats but Hercog 2026 match-level stats are unavailable there. A fabricated per-game hold, fitted shock width, or hard-coded set-score branch is prohibited. Tier C: reference NONE. League baseline at exact handicaps/totals: BASELINE_UNAVAILABLE. Adjustments: none numerically entered. Sensitivity: Hercog's better clay and recent record may exceed Lepchenko's small Elo edge; unverified physical condition or atypical altitude could reverse either qualitative direction. No numerical confidence interval is asserted.

Expected games Hercog/Lepchenko, expected total games, standard deviations, match game margin and probability of 3 sets: NOT_ESTIMATED. A benchmark winner-only number cannot identify any of these.

## A5. Every supplied contract assessed

| Contract | Numeric p_card | Qualitative directional assessment | Important invalid shortcut |
|---|---|---|---|
| Hercog ML | NOT_ESTIMATED | Claimed recent clay/H2H evidence favours Hercog, while rating reference narrowly opposes her; no confident preference | Treating old H2H as calibrated win probability |
| Lepchenko ML | NOT_ESTIMATED | Elo-only reference 51.7%, not a primary forecast; Lepchenko form weaker | Calling Elo reference an issued forecast |
| Hercog -1.5 games | NOT_ESTIMATED | Could cover by a routine straight-sets win; also sometimes while losing in three | Replacing games handicap with set handicap or ML |
| Lepchenko +1.5 games | NOT_ESTIMATED | The narrow cushion may benefit close or split-set games margins, but straight-sets Hercog control defeats it | Assuming a +1.5 game cushion is automatically 'safe' |
| Over 21.5 games | NOT_ESTIMATED | Long two-set scores (7–5, 6–4) or most three-set outcomes can clear 22 games | Treating three sets as the sole Over path |
| Under 21.5 games | NOT_ESTIMATED | Ordinary 6–3, 6–4 or 6–2, 6–4 straight sets stay Under | Ignoring long straight sets and deciders |

**Ranking:** NO_RANKED_ROWS / ABSTAIN. No row verified at >=0.65; published `p_card` cannot be supplied. Do not invent a top-ranked pick or model-claimed probability. Tournament status and retirement action terms unresolved.

## A6. Adjustment ledger, counterfactual and regimes
- Confirmed source context: outdoor clay; historical H2H 4–3, clay H2H 3–0; Elo reference indicates near parity; disparate 2026 clay win percentages and a weaker recent losing streak for Lepchenko.
- Adjustment ledger with effect-table coefficient: NONE ACTUALLY COMPUTED. No unadjusted and adjusted full-game distributions exist, so no fabricated numerical deltas or covariances.
- Low/base/high scenarios (qualitative only): Hercog control yields low games total and beats Lepchenko +1.5; close split sets support a late decider and Over; left-handed opponent return/spin and serve changes could shift the games margin either way. Weather-specific quantified adjustment NOT_ESTIMATED.

## A7. Family checks and model shadow
- Complement checks require a normalized completed match-state tree and settlement conventions. No tree executed; no invalid normalization claim.
- Tennis games spread can be won by a match loser. No unjustified `P(-1.5) <= P(ML)` constraint is applied.
- Model release/shadow: NOT_RUN_NO_VERIFIED_LOCAL_RELEASE; no external or repository code executed. No claims of Monte Carlo, training, freeze, push, verified pre-start issue or future settlement.

## A8. Sources and unresolved-field routes
1. Official WTA event surface, grade and timing: https://www.wtatennis.com/tournaments/1181/sopo-125/2026 .
2. Scheduled match and court: https://www.wtaschedule.com/wta-matches-today .
3. Tournament draw/current H2H/independent benchmark: https://www.tennisabstract.com/current/2026WTASopo125.html .
4. Elo (9 Nov update): https://tennisabstract.com/reports/wta_elo_ratings.html .
5. Prior meeting scores: https://www.tennisexplorer.com/match-detail/?id=3373803 .
6. Recent records: https://en.tennistemple.com/player/polona-hercog/results ; https://en.tennistemple.com/player/varvara-lepchenko/results ; https://tennis-db.com/wta/players/balldontlie_wta:304/varvara-lepchenko/matches .
7. Schedule-status conflict: https://en.tennistemple.com/competitions/sopo-2026/128051/orderofplay .
8. WTA player statistics: https://www.wtatennis.com/players/120420/varvara-lepchenko/stats ; https://www.wtatennis.com/players/313968/polona-hercog/stats .

**Missing/recheck:** (a) official match-specific status/actual first play and whether session was delayed, (b) final 2026 match-level serve/return and hold numbers for both on comparable clay opposition, (c) current fitness, (d) exact tournament tiebreak and betting operator retirement/walkover rules, (e) an eligible tour-specific baseline at +1.5/-1.5 and 21.5, (f) line/score-tree calculation and integrity checks, (g) proper source-audit on local repository runtime. Source-audit was not run in this chat and access-permission closure is therefore unverified; do not claim it was performed. No automation scheduled.

## A9. Integrity and delivery receipt
| Gate | Result |
|---|---|
| Current repository authority | Read-only GitHub `main` HEAD verified as above; local working tree and uncommitted changes unavailable |
| Match/tournament identity | Verified from WTA and schedule listings |
| Match actual start and fitness | NOT_VERIFIED |
| H2H and high-level 2026 form | Partially corroborated; L15/L20 provisional |
| Full pre-event source/field closure | INFORMATION_INCOMPLETE |
| Exact requested contract parsing | COMPLETE for listed textual game lines |
| Tennis point/set/game tree | NOT_COMPUTED |
| Primary probabilities, ranked bets and expected totals | NOT_ESTIMATED / ABSTAIN |
| Forecast model execution or shadow | NOT_PERFORMED |
| Issued card / new MINI_KEY or local event key | NOT_PERFORMED / NONE ALLOCATED |
| Original active mini altered | NO |
| Readback/commit/push | NOT_PERFORMED; repository remains read-only |
| Settlement / canonical import | NOT_PERFORMED |

**Disposition:** Research-only, no-ID, non-issued A1–A9 draft. It is not a substitute for the repository agent's current Prompt 1 reference freeze, correct source-audit, mini write and push. Any user action should await event state, selected operator settlement terms and actual comparable same-event tennis inputs. No strong selection is justified by the verified record.
