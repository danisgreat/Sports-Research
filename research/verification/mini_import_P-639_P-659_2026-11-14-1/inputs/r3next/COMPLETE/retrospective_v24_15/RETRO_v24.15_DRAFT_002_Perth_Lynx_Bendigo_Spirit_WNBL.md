# RETROSPECTIVE v24.15 — DRAFT-002: Perth Lynx (W) vs Bendigo Spirit (W)

**Record class:** `RETROSPECTIVE_FORMAT_CONVERSION / RESEARCH_ONLY / NOT_ISSUED / NOT_FROZEN / NOT_SETTLED / NOT_PERFORMANCE_ELIGIBLE`. This is a newly prepared v24.15-formatted record of an earlier qualitative directional forecast. It is NOT an official v24.15 pregame forecast and is NOT an admitted EXT-v3 `LANE_RETURN`. It preserves all source claims verbatim in the original note appended below.

**Conversion created UTC:** `2026-11-11T08:44:21+00:00` (actual working-container clock, not event-time or publication).  **Current main (read-only):** `4d8bd1771d20974bcbfc7c694a009cd44e95a693`.  **Current controlling release:** `MDS-2026.11.11-v24.15 / CR-2026.11.11-R3 / P-2026.11.11-v24.13 / EXT-v3 / REQ-v5 / SR-KIT-v24.15`.

**Original research note:** `Perth_Lynx_Bendigo_Spirit_WNBL_2026-11-10_READ_ONLY_DRAFT.md` · SHA-256 `b622817ec9c565ecc44b54e25699ba1b5ec9f7f242ec9cd723f8734fb7ca2e69`.  **Staging label:** `DRAFT-002` · suggested `LOCAL-20261109R3NEXT-G0002` **UNALLOCATED**; EV2 key `NOT_CREATED`, canonical P-ID `NOT_ASSIGNED`.

## A1. Event identity and temporal admission

- **Competition:** Australia WNBL 2026–27 Round 4 (Basketball).
- **Home:** Perth Lynx (W). **Away:** Bendigo Spirit (W). **Venue / conditions:** Perth High Performance Centre, Western Australia.
- **Native event identity:** NOT_VERIFIED.
- **Owner's estimated start:** 2026-11-10 21:00 AEDT. **Official/reference scheduled start from the original note:** 2026-11-10 21:00 AEDT / 18:00 AWST; actual tip NOT_VERIFIED.
- **Original timing claim:** Original source research recorded about 20:53 AEDT, before scheduled 21:00; no freeze/issue proof. **Time gate:** `SOURCE_RESEARCH_BEFORE_SCHEDULE; PRESTART_ISSUANCE_NOT_CERTIFIED`. An original timestamp is not a verified pregame issuance receipt; actual first play has not been independently audited for this conversion.
- **Outcome:** `NOT_QUERIED` in this conversion; no outcome, final score, grading, result-based update or settlement lookup was performed. No claim that historical evidence was available before the horizon beyond what the original note supports.

## A2. REQ-v5 exact supplied contract reconstruction

**Rank scope:** `SUPPLIED_ONLY` (default; no new derived lines). Sports-only, market-blind; supplied point/goal/game thresholds are contract metadata. `OPERATOR_TERMS` remain `UNKNOWN_DEFINITION` where the original research note does not identify them.

| Requested contract | Family / side | Period / unit | Action and success condition | Original qualitative assessment | v24.15 disposition |
|---|---|---|---|---|---|
| Perth Lynx -10.5 | SPREAD / Perth | FULL_GAME_OT_INCLUDED / points | Perth final margin >=11; no push | Slight Perth | `UNPRICED: UNAVAILABLE` |
| Bendigo Spirit +10.5 | SPREAD / Bendigo | FULL_GAME_OT_INCLUDED / points | Bendigo wins or loses by <=10; no push | Plausible opposing cushion | `UNPRICED: UNAVAILABLE` |
| Over 167.5 points | TOTAL / OVER | FULL_GAME_OT_INCLUDED / points | combined >=168; no push | Slight Over | `UNPRICED: UNAVAILABLE` |
| Under 167.5 points | TOTAL / UNDER | FULL_GAME_OT_INCLUDED / points | combined <=167; no push | Plausible older H2H Under | `UNPRICED: UNAVAILABLE` |

**UNPRICED coverage (structured contract disposition, NOT a valid L5 lane return):**

```csv
label,status,reason
"Perth Lynx -10.5",UNAVAILABLE,"No pre-start v24.15 committed event/manifest, frozen reference, complete critical inputs, admission-reviewed source snapshot, KIT_RECEIPT or independent issuer confirmation"
"Bendigo Spirit +10.5",UNAVAILABLE,"No pre-start v24.15 committed event/manifest, frozen reference, complete critical inputs, admission-reviewed source snapshot, KIT_RECEIPT or independent issuer confirmation"
"Over 167.5 points",UNAVAILABLE,"No pre-start v24.15 committed event/manifest, frozen reference, complete critical inputs, admission-reviewed source snapshot, KIT_RECEIPT or independent issuer confirmation"
"Under 167.5 points",UNAVAILABLE,"No pre-start v24.15 committed event/manifest, frozen reference, complete critical inputs, admission-reviewed source snapshot, KIT_RECEIPT or independent issuer confirmation"
```

## A3. Original forecast and research decision — unchanged

- **Original single directional preference:** **Perth Lynx -10.5 points**. Retrospectively preserved, not recalculated from outcomes.
- **Original additional directional reading:** Over 167.5 points — slight original secondary lean.
- **Original official decision:** `NO_STRONG_PICK / ABSTAIN`. Qualitative suggestions do not become a v24.15 `PICKS_V2` rank. No estimated probability, confidence threshold or verified baseline is supplied.
- **Numeric outputs:** `p_card NOT_COMPUTED`; league reference `NOT_COMPUTED`; adjustment ledger `NOT_EXECUTED`; score grid and W/P/L/V `NOT_COMPUTED`; KIT receipt `NOT_EXECUTED`; Monte Carlo `NOT_EXECUTED`. `PICKS_V2` intentionally absent. No placeholder 0.5.

## A4. Rosters and availability

Significant reported Bendigo player absences; Abbey Wehrung reporting contradicted by recent recap; confirmed five/bench absent.

**EXT-v3 L1 status:** `HISTORICAL_PARTIAL` from the original narrative; no genuine, packet-bound L1 assignment, signed return or confirmed complete match-day lineup.

## A5. History and opponent context

Perth current-season n=3 and Bendigo n=4, complete opening-round results; no full cross-season L20 with current regime.

Perth 2–1 vs Bendigo 0–4; major roster depth gap; Perth H2H advantages from older roster.

**EXT-v3 L2 status:** historical source note retained, but original per-source date/access/collector fields were not admitted under v24.15; dated L5/L10/L15/L20 values are not four independent samples.

## A6. Timing, rules and independent corroboration

**EXT-v3 L3/L4:** original venue/time and action convention are documented where available; no central event bundle or assigned source review; confirmation and independent original collector mapping remain incomplete. `published_at: UNKNOWN` where the original did not record a date. This conversion does not refetch historical pages or change publication-time claims.

## A7. Scoring, parameter and uncertainty review

**Main losing/counter scenario:** Large double-digit spread, Perth own 2026 wins not exceeding 10-point margin; depleted Bendigo offence suppresses Over.

**Unresolved critical fields:** No admitted WNBL reference, starters/bench confirmation, pace/ORtg/DRtg adjustment, OT grid or SR-KIT receipt.

**EXT-v3 L5:** NOT_ATTEMPTED as an admitted lane. A new retrospective numeric model might be an explicitly labelled shadow diagnostic, but cannot retroactively supply an actual pre-exposure SINGLE receipt, historical five-lane return or original issued prediction.

## A8. Evidence and custody audit

- **Source original note hash:** `b622817ec9c565ecc44b54e25699ba1b5ec9f7f242ec9cd723f8734fb7ca2e69`; original A1–A9 record follows unchanged below. Its URLs, quotes and source timing are historical references only and were **not re-opened** or source-audited in this conversion.
- **Current controlling commit:** `4d8bd1771d20974bcbfc7c694a009cd44e95a693`; original framework revision is preserved in the source note and not silently overwritten.
- **No v24.15 `EVENT.csv`, `CONTRACTS.csv`, `REQUIREMENTS.csv`, `ARTIFACTS.csv`, `POLICY.csv`, EV2 manifest digest, lane packet hash or source-review signature existed for these past messages.** None was invented. An EV2 event identity would have to be minted and admitted by the authorized repository writer; no such ID is asserted here.
- **Mode/custody:** independent `SINGLE_CHAT_LEGACY` source evidence, **not** `FULL_FIVE`, `FULL_SIX`, or `REDUCED` EXT-v3 (no actual role-package execution). No multi-chat comparison, freezes, ledger mutations or GitHub writes.

## A9. Audit and non-settlement gate

| v24.15 requirement | Retrospective status |
|---|---|
| Original directional decision retained | `DONE / VERBATIM_SOURCE_NOTE_BELOW` |
| Exact supplied contracts enumerated | `DONE / LEGACY_SOURCE_RECONSTRUCTION` |
| Home, away, competition, time, sport endpoint | `PARTIAL / SOURCE_NOTE_ONLY` |
| Current reader-permission audit and independent collector review | `NOT_EXECUTED` |
| Event manifest and assigned independent lanes | `NOT_CREATED` |
| Verified competition-specific reference and effect ledger | `NOT_EXECUTED` |
| Complete primary KIT_RECEIPT and normalized contract masses | `NOT_EXECUTED` |
| Pre-start freeze, external/public issue proof | `NOT_AVAILABLE` |
| Writer lease, mini append, lint, learning-log, bind | `NOT_EXECUTED` |
| Settlement, outcome query, grade, score, P-ID assignment | `NOT_PERFORMED` |
| v24.15 performance/comparison eligibility | `INELIGIBLE / RETROSPECTIVE_ONLY` |

**Conclusion:** historical qualitative forecast preserved and recast for v24.15 research retention; **0 numeric contracts priced**, no `p_card` or formal rank, no settlement. This historical record remains available for honest non-scored review and any later expressly authorized outcome audit, without retroactively altering its original claims.

<!-- BEGIN VERBATIM_ORIGINAL_NOTE: Perth_Lynx_Bendigo_Spirit_WNBL_2026-11-10_READ_ONLY_DRAFT.md SHA256=b622817ec9c565ecc44b54e25699ba1b5ec9f7f242ec9cd723f8734fb7ca2e69 -->
# READ_ONLY_DRAFT / NOT_ISSUED — Perth Lynx (W) vs Bendigo Spirit (W)

**Research as of:** 10 November 2026, approximately 20:53 AEDT (UTC+11); scheduled tip-off 21:00 AEDT / 18:00 AWST.  
**Competition:** Australia WNBL, 2026–27, Round 4. **Venue:** Perth High Performance Centre, Western Australia.  
**Repository authority:** `danisgreat/Sports-Research`, read-only connected GitHub `main` pinned at `f79559b45183ca63a2ce5fc2611321975bae744f`. **Current controls:** MDS-2026.11.10-v24.12; CR-2026.11.10-R2; P-2026.11.10-v24.10; SCV-2026.10.22-v12; SEL-2026.10.22-v4.  
**Custody:** External-chat read-only research note, NOT a registered mini card. The published active mini remains `research/active_minis/20261109R3NEXT.md` with last local event `NONE` and next local key `LOCAL-20261109R3NEXT-G0001` as an UNCONSUMED snapshot. No local key or canonical P-ID has been assigned. No write, freeze, linter, ledger entry, model, source-audit command, GitHub commit, or push was performed. This document is not a pre-game issued card.

## A1 — Fixture, event phase, settlement

- WNBL's Round 4 schedule and Perth venue confirm Perth v Bendigo on 10 November 2026, 6pm AWST = 9pm AEDT. [WNBL Round 4 schedule](https://www.wnbl.com.au/news/crunch-time-the-key-storylines-leading-into-round-4); [venue listing](https://www.perthhpc.com.au/events/upcoming-events/perth-lynx-v-bendigo-spirit-26).
- Official match game-center/native event ID: **NOT_VERIFIED**. Scheduled tip, not an independently checked actual first-play time. No live or final data was used in this research.
- Four 10-minute regulation quarters under WNBL/FIBA rules, overtime when tied. Under the user's BK-OT-1 convention, all supplied full-game lines include all overtime; a terminal push is impossible for the supplied half-point spreads/totals. Settlement is conditional on completion and any officially defined exceptions.
- No confirmed starting fives or actual participating bench were obtained. The league-published depth charts are EXPECTED, not CONFIRMED.

## A2 — Every exact user-supplied contract

| Contract | Unit | Endpoint | Research-only qualitative reading | Uncertainty |
|---|---|---|---|---|
| Perth Lynx −10.5 | Points margin | Final including OT | **Slight Perth lean**, on a severe Bendigo roster shortage and Perth home/rest advantages; large spread remains volatile | Low confidence |
| Bendigo Spirit +10.5 | Points margin | Final including OT | Live underdog cushion; Bendigo's current scoring deficit, road travel and reduced depth challenge its ability to stay inside eleven | Low confidence |
| Over 167.5 | Combined points | Final including OT | **Slight Over lean** from seven 2026–27 game observations and scoring crossmatch; not independently paced/efficiency calibrated | Low confidence |
| Under 167.5 | Combined points | Final including OT | Supported by last season's four H2Hs and two recent low Bendigo totals, but those rosters and regimes differ | Low confidence |

**Recommended single direction:** Perth Lynx −10.5 (**LOW confidence, NOT a qualified numerical probability**). **Official framework disposition:** NO_STRONG_PICK / ABSTAIN given no frozen numeric reference and no confirmed game-day fives. An alternative qualitative lean is Over 167.5, which depends on Bendigo's depleted attack contributing enough points. No combination or independence claim is made.

## A3 — Current season complete game history (prior to tip-off)

### Perth: 2026–27 regular season (3 matches, 2W/1L)

| Date AEDT | Match | Score, Perth first | Total | Perth margin |
|---|---|---:|---:|---:|
| 17 Oct | Perth vs Townsville | 86–83 | 169 | +3 |
| 24 Oct | Perth at Adelaide | 90–82 | 172 | +8 |
| 3 Nov | Perth at Townsville | 86–99 | 185 | −13 |

**Perth 2026–27:** 87.33 points scored, 88.00 conceded, 175.33 total/game, −0.67 margin/game. 3/3 completed games Over 167.5. Valid current-season sample `n=3`: L5/L10/L15/L20 *within season* all have `n=3` rather than the nominal window; the prior-season backfill needed for full cross-season L5/10/15/20 has not been completely reconstructed and is **NOT_VERIFIED**. Preseason matches are separately classified and excluded from season form.

### Bendigo: 2026–27 regular season (4 matches, 0W/4L)

| Date AEDT | Match | Score, Bendigo first | Total | Bendigo margin |
|---|---|---:|---:|---:|
| 17 Oct | Bendigo at Canberra | 92–94 | 186 | −2 |
| 27 Oct | Bendigo vs Townsville | 68–91 | 159 | −23 |
| 2 Nov | Bendigo vs Geelong | 70–77 | 147 | −7 |
| 7 Nov | Bendigo vs Canberra | 83–97 | 180 | −14 |

**Bendigo 2026–27:** 78.25 points scored, 89.75 conceded, 168.00 total/game, −11.50 margin/game. 2/4 games Over 167.5. Valid current-season sample `n=4`: L5/L10/L15/L20 *within season* all have `n=4`; prior-season backfill is **NOT_VERIFIED**. Note all four prior Bendigo matches were played in Victoria/ACT, not at Perth.

**Form sources:** [Official Perth 90–82 Adelaide report](https://www.wnbl.com.au/news/perth-lynx-pounce-to-hand-adelaide-lightning-third-straight-defeat); [Perth 86–99 Townsville report](https://perthlynx.wnbl.com.au/news/townsville-fire-end-lynxs-unbeaten-wnbl-start); [official Bendigo 83–97 Canberra report](https://www.wnbl.com.au/news/puoch-celebrates-100th-game-in-capitals-victory-over-spirit); [WNBL season score compilation](https://api.thesportsdb.com/season/5113-australian-wnbl/2026-2027); [additional independent dated results](https://stadiro.com/leagues/basketball/australia/wnbl-women/results/).

### Prior head-to-head, January–February 2026 (different roster regime)

| Date | Winner | Score | Combined |
|---|---|---|---:|
| 15 Jan | Perth | 85–81 | 166 |
| 1 Feb | Perth | 88–64 | 152 |
| 14 Feb | Perth | 86–76 | 162 |
| 17 Feb | Perth | 81–75 | 156 |

Historical H2H Perth 4/4 wins; average Perth winning margin +11.0; total mean 159.0; all four Under 167.5. **Weak comparability:** Perth changed several high-minutes starters, while Bendigo's roster has a different availability regime. Results must not be treated as four independent samples of the current matchup. Sources: [15 Jan](https://www.wnbl.com.au/news/lynx-claw-their-way-back-for-a-hometown-victory); [14 Feb](https://www.wnbl.com.au/news/perth-pounces-early-to-take-game-one-over-bendigo); [17 Feb](https://www.wnbl.com.au/news/perth-punch-their-ticket-to-the-wnbl26-championships-series); [2026 historical results listing](https://www.austadiums.com/sport/teams/perth-lynx).

## A4 — Lineups, injuries, late news, travel/rest

The league's **10 November expected depth charts** are:
- **Perth:** PG Georgia Amoore / Ashby; SG Ciabattoni / Gorman / Weir; SF Haley Peters / Hodges / Anticevic; PF Anneli Maley / Malone; C Teonni Key / Morrell. The league states no injuries listed. Actual starts and bench unverified.
- **Bendigo:** PG Jade Melbourne / Mia Harvey / Kelly Wilson (listed out); SG Georgia Booth / Olivia Olechnowicz / Isobel Borlase (out) / Abbey Wehrung (listed out); SF Casey Samuels / Catherine MacGregor (out); PF Kelsey Griffin / Olivia Pollerd; C Marianna Tolo / Kelsey Rees (out). Actual starts and bench unverified.

**League-reported Bendigo absences:** Borlase (WNBA commitments, Round 5 indicated); MacGregor (knee, season); Rees (ankle, Round 8; replaced by Harvey); Wehrung (listed pregnancy policy, season); Wilson (personal reasons, Round 5). Tolo is returning from Achilles injury and may have managed minutes. Olechnowicz in the 10 Nov projected depth chart, but her return from a back complaint was not confirmed. [WNBL same-day preview](https://www.wnbl.com.au/news/how-to-watch-talking-points-perth-v-bendigo) and [WNBL league injury register](https://www.wnbl.com.au/news/wnbl27-the-latest-injury-updates?964d7745_page=1).

**Conflict requiring resolution:** An official 7 Nov Bendigo–Canberra recap says **Abbey Wehrung hit three fourth-quarter three-pointers**, yet the updated roster report for 10 Nov marks her out under pregnancy policy. She could have changed status between fixtures, but participation/medical facts are not inferred. [7 Nov game recap](https://www.wnbl.com.au/news/puoch-celebrates-100th-game-in-capitals-victory-over-spirit).

**Influential verified player performance:** Perth's Anneli Maley 19 pts/11 reb and Georgia Amoore 20 pts/8 ast vs Townsville on 3 Nov; Bendigo's Jade Melbourne 24 pts/6 reb/6 ast and Olivia Pollerd 16 pts/7 reb vs Canberra on 7 Nov. These are single-game observations and not season-wide player props. [Perth recap](https://perthlynx.wnbl.com.au/news/townsville-fire-end-lynxs-unbeaten-wnbl-start); [Bendigo recap](https://www.wnbl.com.au/news/puoch-celebrates-100th-game-in-capitals-victory-over-spirit).

**Rest & travel:** Perth last played 3 Nov; Bendigo last played 7 Nov. Perth has roughly six clear calendar rest days vs Bendigo two, with Bendigo travelling from eastern Australia to Perth across a three-hour time-zone difference. Actual flights, training, tactical changes and fatigue costs unverified. Foul trouble for Key/Peters in Perth's most recent loss provides an identified game-state sensitivity, not proof of a recurring tendency.

## A5 — Joint-score numerical reference attempt / scenario

**Model reference stage:** `NOT_RUN` — repo source exists on GitHub in read-only mode, but the operator's local working tree, current data snapshots, and required `python -m ml reference tier`, `reference run`, `card lint`, `pregame run` receipts are not present. No Monte Carlo, simulation, fitting, calibrated probability or issued p_card may be claimed.

**Descriptive, non-primary arithmetic only:**
- Perth current offense 262/3 = 87.33; defense 264/3 = 88.00.
- Bendigo current offense 313/4 = 78.25; defense 359/4 = 89.75.
- Naive equal-weight offense/opponent-defense crossmatch: Perth = (87.33 + 89.75)/2 = **88.54**; Bendigo = (78.25 + 88.00)/2 = **83.13**; total = **171.67**; margin = **Perth +5.42**. This diagnostic lacks league normalization, opponent adjustment, home strength, current availability-mixture coefficients, pace, possessions, covariance, overtime, and a reference width. It must NOT be promoted to a forecast or read as the p_card anchor.
- Alternative qualitative routes: (i) depleted Bendigo halfcourt scoring and slow pace => Under and a potentially large Perth margin; (ii) Perth transition success versus short Bendigo bench => higher Perth points, Perth cover/Over; (iii) Bendigo's Jade Melbourne offense sustaining competitive periods => +10.5 Bendigo and potentially Over; (iv) Perth early fouls/bench rotations => narrower margin regardless of total.
- No declared numeric scenario weights, SDs, expected scoring intervals, reference p, baseline p, or W/L probability masses could be evidenced. They remain `NOT_COMPUTED` / `NOT_ESTIMATED`, not 0.5. The supplied lines are contract descriptions, not odds or probabilities.

## A6 — Winner, spread, total and interdependence

- Winner direction: Perth (home, roster availability, rest, Bendigo 0–4), uncalibrated and not a supported probability.
- Perth −10.5: Requires winning by **11 or more**, including OT. Perth's 2026–27 wins were by 3 and 8, but over different opponents and split venues. Bendigo lost its four games by 2, 23, 7 and 14, all outside Perth. The large handicap does not follow merely from a likely Perth win.
- Bendigo +10.5: Covers on a Bendigo victory or a Perth win by 1–10. If Bendigo's shortened rotation sustains offense and defensive rebounding, this remains plausible. A decisive Perth run and thin Bendigo bench can break the cushion.
- Over 167.5: Current Perth games 169, 172, 185 (3/3 Over); Bendigo 186, 159, 147, 180 (2/4 Over). The naive unadjusted matchup arithmetic is 171.7. Both the historical head-to-head 159 average and Bendigo's low-scoring losses challenge that signal.
- Under 167.5: Supported by all four recent prior-season H2Hs and two Bendigo current games, but the large post-season changes to both teams preclude treating those results as a current pace model.
- Dependence: Perth −10.5 and the Under can both win through Bendigo offensive suppression; Perth −10.5 and Over can both win through Perth efficiency; Bendigo +10.5 and Over can coexist in a competitive high-scoring game. Multiple directions are NOT independent legs and are NOT recommended as a parlay.

## A7 — Coaching, format, season/league conditions, market exclusion

- Perth coach Ryan Petrik and his focus on the team's defence/foul issues confirmed in Perth's 4 Nov report. No verified game-day tactical scheme, minute allocation or confirmed pace forecast.
- 40-minute FIBA-style regulation, plus any OT under BK-OT-1 (framework rule); no confirmed referees or game-specific opening lineups.
- Supplied **−10.5 / +10.5 and 167.5** used only as exact contract thresholds. No external odds, prices, lines, betting-model or tips content has been used to set directions.
- Form windows, combined team pace, ORtg/DRtg and player minutes not separately confirmed with denominators. The seven recent games are not enough to estimate those reliably as a certification-grade numeric reference.

## A8 — Source register, discrepancies, known-at limits

| Claim | Sources consulted | Evidence quality / unresolved |
|---|---|---|
| Fixture/time/venue | WNBL Round 4 5 Nov; Perth venue current | Confirmed schedule, actual tip NOT_VERIFIED |
| 2026–27 results | WNBL club news + TheSportsDB + Stadiro/Austadiums | Dated completed results; publisher known-at and independent lineage not fully audited |
| Bendigo absent players | WNBL 10 Nov match-day article + 8 Nov injury register | Strong report but actual active participants and Wehrung contradiction NOT_VERIFIED |
| Perth depth | WNBL 10 Nov match-day article | Projected, not confirmed five/bench |
| Team performance | WNBL game reports for 3 and 7 Nov | Single-game stats; no full opponent-normalized dataset |
| H2H | WNBL 15 Jan/14 Feb/17 Feb articles + historical scores | Source-grounded, explicitly old-roster downweight |
| Reference/baseline | GitHub `CORE.md`, `RULES_BASKETBALL.md`, `research/prompts/1_GAME_CARD.md` and basketball sport file | Rules read; actual current-model execution and reference NOT_RUN |
| Pre-source audit | `python -m ml source-audit` not executable in this chat | NOT_RUN; source-admission gate remains open |

**Source timestamp caution:** the WNBL's 10 Nov preview has a stale internal line saying `Saturday, October 17` for this fixture even though its 10 Nov heading, Round 4 schedule and venue listing agree on Tuesday 10 Nov. Schedule controls the event date. The same preview has a potential discrepancy with Wehrung's recorded 7 Nov participation. Do not silently reconcile either artifact.

## A9 — Research completeness and execution disposition

| Gate | Status | Required next source/action |
|---|---|---|
| Official fixture & venue | DONE | Match centre native ID/recheck at first play remains open |
| Regular-season recent-game scores (available n=3/4) | DONE | True L5/10/15/20 cross-season sourced row reconstruction remains open |
| Confirmed fives & active bench | OPEN | WNBL game centre lineup / official matchday roster |
| Injury status/corroboration | PARTIAL | Confirm Wehrung, Olechnowicz, Borlase and Wilson game-specific active/inactive statuses |
| Opponent-adjusted per-possession offence, defence and pace | OPEN | Source current 2026–27 shot, rebound and possession denominators by game |
| Coaching/regime/rest/travel | PARTIAL | Full minutes/rotation plans and travel details not confirmed |
| H2H and roster continuity | PARTIAL | Four recent H2H verified, current regime not the same |
| OT and exact supplied contract definitions | DONE per BK-OT-1 | Operator-specific dispute/void rules not independently supplied |
| Numerical frozen reference/BASELINE_P/PICKS_V2 | NOT_RUN | Repository operator must perform current source audit and prescribed commands |
| Formal forecast publication, mini write, model shadow, receipt, commit | NOT_PERFORMED | Restricted by owner read-only GitHub instruction and repository-agent custody |
| Run classification | **RESEARCH_ONLY / READ_ONLY_DRAFT / NOT_ISSUED** | Do not score as pre-start-issued or consume any event/canonical ID |

**Summary:** Perth is the likely winner on the qualitative current roster/home/rest evidence. Perth −10.5 is a *weak* single-choice directional lean; Over 167.5 is the similarly weak total lean. No probability is published. The defensible framework decision remains **ABSTAIN / NO_STRONG_PICK**, not a certified pick.
<!-- END VERBATIM_ORIGINAL_NOTE: Perth_Lynx_Bendigo_Spirit_WNBL_2026-11-10_READ_ONLY_DRAFT.md -->
