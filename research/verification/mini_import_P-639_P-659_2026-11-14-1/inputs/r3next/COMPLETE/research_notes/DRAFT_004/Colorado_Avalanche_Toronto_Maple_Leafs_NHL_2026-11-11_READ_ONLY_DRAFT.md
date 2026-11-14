# READ_ONLY_DRAFT / NOT_ISSUED — Colorado Avalanche @ Toronto Maple Leafs, NHL 10 Nov 2026 ET

**Research receipt:** 2026-11-11T11:04:30+11:00 · Australia/Melbourne. **Repository authority:** `danisgreat/Sports-Research`, published GitHub `main` at `f79559b45183ca63a2ce5fc2611321975bae744f`. Governing method `MDS-2026.11.10-v24.12`, control `CR-2026.11.10-R2`, prompt `P-2026.11.10-v24.10`; selection `SEL-2026.10.22-v4`. Read-only reference included CORE.md, CURRENT_STATE.md, research/prompts/1_GAME_CARD.md, research/prompts/1_sports/ICE_HOCKEY.md, and active mini footer. No writable local repository, source audit, reference model, formal simulation, freeze, linter or writer-authorised issue was available. **Status: RESEARCH_PARTIAL / UNCALIBRATED_QUALITATIVE / NO_STRONG_PICK / NOT_ISSUED**.

## A1. Exact event, timing, rules and identity

- Fixture: NHL regular season 2026–27, Colorado Avalanche at Toronto Maple Leafs, Scotiabank Arena, Toronto, Ontario, Canada. Public NHL fixture shows Tuesday 10 November 2026 at 7:00 PM EST (`2026-11-11T00:00:00Z`), which is **11:00 AM AEDT**, 11 November. Owner estimated 11:07 AM AEDT, likely actual faceoff versus schedule, but actual first puck not verified.
- Reported pregame NHL records Colorado **10–6–2** and Toronto **8–9–2**. NHL official match preview: https://www.nhl.com/news/colorado-avalanche-toronto-maple-leafs-game-preview-november-10-2026 and official Colorado team preview https://www.nhl.com/avalanche/news/game-preview-11-10-26 . Venue: https://www.scotiabankarena.com/events/detail/toronto-maple-leafs-vs-colorado-avalanche-3
- Match winner/ML includes overtime and shootout on the standard NHL final-result interpretation; 60-minute regulation, potential five-minute 3v3 overtime and shootout; **exact operator terms NOT_VERIFIED**. Toronto +1.5 is the final-game margin inclusive of a shootout's one-goal result, subject to operator terms; Colorado two-or-more-goal wins defeat the cushion. Total 6.5 is match goals on final score including any OT goal (a shootout award changes the final official score by one goal but separate treatment may differ by operator). Do not silently assume all operators grade identically.
- Game/source capture before actual puck **NOT_INDEPENDENTLY_VERIFIED**; no in-play data consulted for this draft. Do not represent draft as prospective frozen card. This is a candidate for the next authorized local mini import only after collision and known-at checks.

## A2. Requested contracts — qualitative assessment

| Exact supplied market | Directional read | Status and reason |
|---|---|---|
| Avalanche ML | **Colorado win** | Preferred direction; stronger record, deeper top-six attack, Blackwood confirmed and better season goalie profile; prior 6–3 H2H loss and road split are material risks. |
| Maple Leafs +1.5 goals | **Toronto +1.5** is viable, but not preferred over Colorado ML | Toronto covers with outright win or one-goal loss. Historically seven covers in Toronto's latest ten games, but Colorado's last five wins in its latest ten were all by 3+; empty-net goal tail matters. |
| Over 6.5 goals | **Slight Over lean** | Season cross-match scoring near seven goals; weaker Bobrovsky save record and Colorado scoring depth. Sensitivity to Blackwood suppressing Toronto's contribution. |
| Under 6.5 goals | Credible competing scenario | TOR L5 offense 2.4 goals/game, Blackwood recent shutout; low-event possibility. No strong Under justification. |

**Single directional preference:** Colorado Avalanche ML, **moderate-to-low qualitative confidence**. **Official decision:** `NO_STRONG_PICK / ABSTAIN`; absent reference run and validated probability grid no `p_card` number, no rank ordering by probability, no evidence of calibrated advantage. All `p_card`, model reference, league baseline, score-grid margin and total probabilities = `NOT_COMPUTED`.

## A3. Both teams' prior games, true n and research gaps

The following dated results are 10 most recent **completed** games prior to this fixture, as exposed by search result tables from StatMuse and corroborated where available with Colorado team recaps. Dates in North American venue timezone. Score shown from named team viewpoint. Sources:
- Colorado: https://www.statmuse.com/nhl/ask/colorado-avalanche-last-10-games-goals-against ; Colorado team recent recaps linked at https://www.nhl.com/avalanche/news/game-preview-11-10-26
- Toronto: https://www.statmuse.com/nhl/ask/toronto-maple-leafs-game-log-last-10-games ; NHL team preview and official NHL projected lineup page.
- **Data limitation:** Some dynamically opened StatMuse pages returned stale cached snapshots even when current search result tables had through-8-Nov results. The table below uses latest dated search-result rows and does not claim a two-independent-source complete verification of every row.

| Date ET | COL opponent | COL GF–GA | TOR opponent | TOR GF–GA |
|---|---|---|---|---|
| Latest 1 | 07 Nov DET | 4–0 | 08 Nov NJD | 0–4 |
| Latest 2 | 05 Nov NSH | 2–3 OT | 07 Nov MTL | 2–4 |
| Latest 3 | 03 Nov CBJ | 2–7 | 03 Nov UTA | 2–3 |
| Latest 4 | 02 Nov CHI | 5–2 | 31 Oct VAN | 4–2 |
| Latest 5 | 31 Oct CGY | 5–2 | 28 Oct SEA | 4–5 |
| Latest 6 | 28 Oct NJD | 5–2 | 26 Oct CGY | 2–5 |
| Latest 7 | 25 Oct NSH | 2–6 | 24 Oct EDM | 7–2 |
| Latest 8 | 23 Oct TBL | 6–3 | 22 Oct NYR | 5–4 |
| Latest 9 | 20 Oct NJD | 3–4 | 20 Oct CBJ | 6–2 |
| Latest 10 | 19 Oct PHI | 2–3 | 19 Oct SJS | 3–1 |

| Window | Colorado GF | Colorado GA | Toronto GF | Toronto GA | True n |
|---|---:|---:|---:|---:|---|
| L5 | 18 / 5 = 3.60 | 14 / 5 = 2.80 | 12 / 5 = 2.40 | 18 / 5 = 3.60 | 5 each |
| L10 | 36 / 10 = 3.60 | 32 / 10 = 3.20 | 35 / 10 = 3.50 | 32 / 10 = 3.20 | 10 each |
| L15 | NOT_VERIFIED | NOT_VERIFIED | NOT_VERIFIED | NOT_VERIFIED | 0 verified complete windows |
| L20 | Season COL has only 18; TOR 19 prior to puck | NOT_VERIFIED | NOT_VERIFIED | NOT_VERIFIED | 18 / 19 maximum |
| Season through pregame | ~4.0 GF/g | ~3.1 GA/g | ~3.4 GF/g | ~3.3 GA/g | 18 COL; 19 TOR |

Descriptive L10 combined totals COL 6.80, TOR 6.70; L5 COL 6.40, TOR 6.00. L10 scoring rates are overlapping with season and not treated as independent evidence. Opponent adjusted xG/shot danger, shot quality, goals saved above expected and venue-adjusted expected goals remain `NOT_COMPUTED`.

## A4. Goalies, roster and personnel status

**Starting goaltenders confirmed**, as of the 10 November reported lineup updates: Mackenzie Blackwood COL (9–3–1; 2.60 GAA, .901 SV%), Sergei Bobrovsky TOR (3–7–2; 3.34 GAA, .886 SV%). Confirmation timestamps on DailyFaceoff were 2026-11-10 18:20:53Z and 15:33:58Z respectively, published prior to this request; confirmed on https://www.dailyfaceoff.com/starting-goalies/2026-11-10 and supported by https://coloradohockeynow.com/avalanche-maple-leafs-game-preview-lines-how-to-watch/ . Blackwood made 27 saves in the 4–0 shutout versus Detroit 7 Nov.

**Colorado projected starting forward lines:** Lehkonen–MacKinnon–Necas; Landeskog–Kadri–Roy; Schwartz–Nelson–T.J. Hughes; Kelly–Svechkov–O'Connor. Defence Kulak–Makar; Toews–Malinski; Juulsen–Burns. No confirmed skater dressed-state receipt. **Colorado injuries:** Josh Manson lower body/ankle, Zachary L'Heureux upper body. Cale Makar expected to play despite a precautionary early practice departure.

**Toronto projected lines:** Cowan–Matthews–Roslovic; Tverberg–Tavares–Nylander; Joshua–Paul–McKenna; Duhaime–Blueger–MacEwen. Defence Ekman-Larsson–Tanev; McCabe–Raddysh; Mermis–Stecher. Injuries: Max Domi, Kirill Marchenko, Marshall Rifai, Nick Blankenburg, Morgan Rielly and Colton Sissons. **Jack Roslovic conflict:** NHL.com tags him injured but also projects him on the starting top line; contemporaneous reporter says returning. Treat playing status as `PROJECTED_RETURN / NOT_FINAL_CONFIRMED`, not absent and not confirmed dressed. Chris Tanev returning from load management. Official projected lineup is NOT a confirmed starting five in basketball terms; the relevant NHL equivalent is final dressed roster plus goalie confirmed.

## A5. H2H, venue, schedule and market dependence

- October 10 first meeting of 2026–27: **Toronto 6–3 Colorado** in Colorado; total 9 goals, Colorado ML lost, Toronto +1.5 covered, Over 6.5 won. This is one game under another goalie and roster regime, not a deterministic rule.
- Last known Colorado result DET shutout Nov 7; Toronto lost NJD 0–4 Nov 8 and entered on three straight defeats. Colorado starts a three-game Canadian road trip. Neither team on a back-to-back; Toronto has a little less rest but remains at home. Colorado home/away split before the game: road 3–5–0 and home 7–1–2 per available season stats, a caution against road favourite certainty.
- Colorado ML and Toronto +1.5 can **both win** on a one-goal Colorado victory. A Toronto outright win defeats Colorado ML but covers Toronto +1.5; a Colorado multi-goal win defeats the cushion. One-goal losses, 3v3 overtime, shootout, empty-net scores and trailing-goalie pull need joint-model treatment.
- Total Over 6.5 can be reached by 4–3, 5–2, 5–3 or 6–2; Under by 3–2, 4–2, 3–3 before OT resolution, etc. A high-event Toronto comeback might simultaneously favour Toronto cushion and Over; Colorado runaway can favour COL ML and Over or even Under if Toronto is suppressed. Empty net can add a late goal or wider margin. No independent-proposition assumption.

## A6. Descriptive scoring budgets (not forecast probabilities)

- Season cross-match arithmetic: COL point-rate midpoint `(COL GF~4.0 + TOR GA~3.3) / 2 ≈ 3.65`; TOR point-rate midpoint `(TOR GF~3.4 + COL GA~3.1) / 2 ≈ 3.25`; combined ≈**6.90**. This is a raw heuristic, **not** an NHL reference model and not a fitted or opponent-adjusted projection.
- L10 cross-match arithmetic: `(COL 3.6 + TOR conceded 3.2)/2 = 3.40`; `(TOR 3.5 + COL conceded 3.2)/2 = 3.35`; combined **6.75**.
- L5 cross-match arithmetic: `(COL 3.6 + TOR conceded 3.6)/2 = 3.60`; `(TOR 2.4 + COL conceded 2.8)/2 = 2.60`; combined **6.20**. Opposing regime direction warns against overstating the Over at 6.5.
- Reported goalies and unconfirmed forward rotations materially change tails. No true conditional hockey goal grid, correlation/covariance, Poisson rate calibrated to correct league reference, OT/SO branch, 6-on-5 empty-net branch, Monte Carlo, Poisson tail or 1-goal-margin mass was run; none is claimed.

## A7. Contract dispositions, kill paths and confidence

| Row | Directional assessment | What could invalidate it |
|---|---|---|
| Colorado ML | **Preferred low-to-moderate**; MacKinnon/Makar available, superior current goalie form (the earlier 3–6 defeat to Toronto is not dismissed) | Toronto's 6–3 prior H2H victory, home advantage, COL road record, Toronto power play and Matthews/Nylander response |
| Toronto +1.5 | Viable and potentially an even stronger cover frequency than straight winner, but ranking numerically NOT_COMPUTED | COL 5 latest wins in 10 were all by at least 3, Bobrovsky weak season save %, empty-net concession |
| Over 6.5 | Marginal tilt from season/L10 scoring budgets | Blackwood suppresses TOR scoring, TOR depleted attack, recent shutout, special teams stall |
| Under 6.5 | Viable alternate, especially if game played at 3–2 or 4–2 | COL top line creates 4+, Bobrovsky struggles, TOR PP penalty conversion, empty net |

No demonstrated ≥0.65 `p_card`, no confidence interval, no independent qualification. All supplied contracts assessed, **no official ranked pick**. Scoreline examples are scenarios, not predictive modes: COL 4–3 TOR yields Colorado ML + Toronto cushion + Over; COL 4–2 TOR yields Colorado ML and Under, but no Toronto cushion; TOR 4–3 COL yields Toronto cushion and Over, Colorado ML loses. Scores must obey OT / shootout official final goals and operator rules.

## A8. Provenance, timing and failed checks

| Field | Evidence route | Quality / missing |
|---|---|---|
| Fixture and venue | NHL official 10 Nov preview, Scotiabank Arena | SCHEDULE_VERIFIED, actual first play NOT_VERIFIED |
| Goalies | Daily Faceoff 10 Nov confirmed status and times, Colorado Hockey Now local report | GOALIES_CONFIRMED at report time, not official on-ice identification |
| Injury and projected skaters | NHL official projected 10 Nov, Colorado Hockey Now and Leafs Hotstove | Partly corroborated; Roslovic contradictory, exact dressed lines unverified |
| L5 / L10 goal histories | Latest StatMuse dated discovery extracts; NHL team articles last three | Recent rows computed, no separate complete independent event-by-event second inventory; cached open results had stale snapshots |
| H2H and team context | Official Colorado 10 Nov 2026 preview | Verified Oct 10 6–3 game and current team records |
| Future actions | Pre-puck official warmup/dressed sheets, source-audit and model reference | Not scheduled or executed |

Available source URLs: https://www.nhl.com/news/colorado-avalanche-toronto-maple-leafs-game-preview-november-10-2026 ; https://www.nhl.com/avalanche/news/game-preview-11-10-26 ; https://www.dailyfaceoff.com/starting-goalies/2026-11-10 ; https://coloradohockeynow.com/avalanche-maple-leafs-game-preview-lines-how-to-watch/ ; https://mapleleafshotstove.com/2026/11/10/toronto-maple-leafs-vs-colorado-avalanche-game-20-projected-lines-preview-tv-info/ ; https://www.statmuse.com/nhl/ask/colorado-avalanche-last-10-games-goals-against ; https://www.statmuse.com/nhl/ask/toronto-maple-leafs-game-log-last-10-games . NHL official and team websites are independently authoritative for club/league claims; website page publication times are shown as 10 Nov but precise minute not reported; retrieval captured approximately at the timestamp of this receipt. **Repository `python -m ml source-audit --url` not run**, do not claim `ALLOWED` or `NO_RULES_FILE` verdicts. Hockey-Reference pages returned 403 when opened and were not accessed further. No betting prices, line movement, market forecasts or third-party betting recommendations used as analytic inputs.

## A9. Research and issuance completion matrix

| Required gate | Result |
|---|---|
| Identity/venue/time and teams | VERIFIED scheduled game, actual first play NOT_VERIFIED |
| Both goalies | Confirmed by independent lineup tracker (not official goalie in-net inspection) |
| Both starting lines/full scratches/absence | Projections supported; final dressed list NOT_VERIFIED |
| L5 and L10 | Dated results summarized; incomplete independent row cross-check |
| L15/L20 | NOT_COMPLETED; 18/19 season-game ceilings noted |
| H2H, pace, rest, home/away | H2H verified, rest and venue known, xG/shot pace incomplete |
| Exact 3 supplied contract families | All directions assessed, ML / +1.5 / O-U6.5, hypothetical action conventions |
| Operational source audit and approved route test | NOT_EXECUTED |
| League reference model tier/frozen release, adjustments | NOT_EXECUTED |
| Joint Poisson / OT/SO / empty-net score process | NOT_COMPUTED |
| `PICKS_V2`, lint, learning log, pregame receipt | NOT_EXECUTED |
| Official local card ID, mini writer lease, commit/push | NONE; only local read-only draft |
| Numerical prediction | NO_FORECAST; qualitative unsupported certification |
| Overall | **RESEARCH_PARTIAL / READ_ONLY_DRAFT / NOT_ISSUED** |

**Custody note:** Original GitHub mini is ACTIVE / EMPTY (published footer 0 cards, next LOCAL-20261109R3NEXT-G0001). This case is a **local research stage only**; if prior draft slots G0001–G0003 reconcile without collisions, candidate slot G0004 is available to the authorized repository agent, but **not allocated or consumed** here.
