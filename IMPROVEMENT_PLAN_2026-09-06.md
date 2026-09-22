# Comprehensive improvement plan — 2026-09-06

**Scope.** Every Markdown document at the root of `Sports Research/` (33 files; sub-folders excluded per instruction), reviewed for defects that reduce predictive quality, plus the settlement, retrospective and algorithm work arising from the two deferred cards (`P-304`, `P-305`) and four open evidence gaps.

**Method version produced by this pass:** `MDS-2026.09.06-v3.7` / `GFA-2` amended with gates `G10.2`, `G14.2`, `G20.2`, `G21.1`, `G26.1`, `G34.1`, `G36.1`.
**Governing constraints kept:** `SPORTS_ONLY / MARKET_BLIND`; probability state `NOT_GENERATED / NOT_PUBLISHED`; numerical program still Stage 0. **Nothing in this document fits a coefficient or claims predictive lift.**

**Honesty note up front.** This pass falsifies one of the framework's own recently promoted controls (`L-073`, the blanket corners cap) and closes four "unresolvable" evidence gaps that earlier passes had written off. That is recorded as a correction, not buried. It also records a real archival defect: `P-304` and `P-305` were archived with only their Rank #1 rows, so their #2–#5 rows are permanently ungradable.

---

## 0. Executive summary — what changed and why it matters

| # | Finding | Consequence | Where implemented |
|---|---|---|---|
| 1 | **`P-304` and `P-305` are now settled. Both Rank #1 picks WON, and both potential-winner calls were CORRECT.** | Cohort Rank #1 moves to 9 W / 8 L across 17 resolvable rows | `PREDICTION_LOG_COMBINED_2.md` §2026-09-06 |
| 2 | **The ESPN keyless `summary?event=` API returns `wonCorners`.** Corners *are* settleable — for every competition ESPN covers. | `L-073`'s premise ("no corners market in this framework's entire recorded history has settled cleanly from a single independently-reproducible field owner") is **factually false**. `L-073` is narrowed and superseded by `L-081`. Four historical corner rows closed. | `LEARNING_REGISTER.md` L-079/L-081; `RULES_SOCCER.md` §Sept 6 |
| 3 | **The ESPN cricket `summary` API returns a structured `Powerplay 1: Overs 0.1 - 6.0 (Mandatory - N runs, W wickets)` note.** | The recurring cricket phase-contract evidence gap is closed permanently. `P-300` and `P-305` powerplays settled. The Sept 5(b) "standing evidence cap on ETPL powerplay contracts" is lifted. | `DATA_SOURCE_REGISTER.md` §Sept 6; `RULES_CRICKET.md` §Sept 6 |
| 4 | **A fabricated "AI Simulation" match report was returned by web search alongside genuine results for `P-305`**, with a plausible but entirely invented scoreline (Dublin 176/7 beat Amsterdam 170/7 by six runs; the real result was Amsterdam 169/7 beat Dublin 160/8 by nine runs). | New hard gate: synthetic/simulated/preview/fantasy content is E-tier and may never settle a contract. | `RULES_GENERAL.md` §4; `L-079` |
| 5 | **Over/Under diagnosis.** Ranked total-type rows won in **8 of 12** new cards. All four failures were **Unders**; ranked **Overs went 4 W / 1 L**, ranked **Unders 5 W / 4 L**. Every Under failure was a game where the eventual winner's score exceeded the central estimate the card used. | Two new mandatory arithmetic disclosures (`G20.2` upper-tail budget, `G21.1` path-geometry) and one top-slot humility gate (`G26.1`). | `RULES_GENERAL.md` §11 |
| 6 | **Coaching and bench capacity are not gated anywhere in the framework.** `P-304` was decided partly by substitutes: two of Slavia's four goals came from players introduced during the match, one of them a forced injury replacement. | New gate `G14.2` — named head coach, full bench, substitution allowance, rotation depth and congestion signal recorded on every card. | `RULES_GENERAL.md` §3, §11.3F |
| 7 | **Settlement sources are not pre-registered.** Rows enter the ranked slate with no confirmation that any endpoint will be able to grade them. | New gate `G10.2` — name the settling endpoint before ranking; unsourced rows are capped below Rank #1. This replaces the market-type ban in `L-073` with a competition-coverage test, which is the actual causal variable. | `RULES_GENERAL.md` §11.1 |
| 8 | **Archival completeness defect.** The `P-294`–`P-305` component was archived with only a summary table. `P-304`/`P-305` were unsettled at the time, so their #2–#5 rows are now permanently ungradable. | New gate `G34.1` — a component may not be archived while any card in it is unsettled unless that card's full frozen slate is reproduced verbatim. | `RULES_GENERAL.md` §11.7; `EXTERNAL_LOGGING_WORKFLOW.md` |

---

## Part A — Settlement of the outstanding queue

### A.1 `P-304` — SK Slavia Praha vs FC Zbrojovka Brno, Chance Liga Round 7

| Field | Value |
|---|---|
| Frozen state | `PREGAME`, cutoff 2026-09-05 22:53:47 AEST / 14:53:47 CEST |
| Kickoff | 2026-09-05 15:00 CEST, Eden Aréna, Prague |
| Prior status | `DEFERRED — live at first check` (confirmed 0-0, first half, two independent sources) |
| **Official result** | **Slavia Praha 4 – 0 Zbrojovka Brno. Half-time 1-0.** |
| Goals | 38' Tomáš Chorý (penalty); 65' Chorý; 76' Emmanuel Ayaosi; 88' David Jurásek |
| Referee | Jan Beneš |
| Coaches | Jindřich Trpišovský (Slavia) · Martin Svědík (Zbrojovka) |
| Slavia XI | Markovič — Konečný, Zima, Chaloupek — Isife, Sadílek, Nowak, Kubiak — Šturm, Provod — Chorý |
| Zbrojovka XI | Hrdina — Klíma, Hunal, Kaká — Penxa, Langer, Čavoš, Dante — Vachoušek, Vaníček — Vašulín |
| Match events of note | Zima (20') and Provod (26') both forced off injured; replaced by Vlček and Ayaosi. Jurásek on 63'. Oscar Kubiak made his Slavia debut. Zbrojovka's coach publicly disputed the 38th-minute penalty. |

| Rank | Frozen contract | Settlement |
|---:|---|---|
| 1 | **1st Half Over 0.5 goals** | **WIN** — Chorý's 38th-minute penalty |
| 2–5 | **NOT ON RECORD — archival defect** | `UNGRADABLE / ARCHIVAL_OMISSION` (see `G34.1`) |
| — | Potential winner: **SK Slavia Praha** | **CORRECT** |

**Sources.** [ČeskéNoviny (ČTK) match report](https://www.ceskenoviny.cz/zpravy/slavia-v-primem-souboji-o-prvni-misto-v-lize-rozdrtila-zbrojovku/2870539) — full time, half-time, scorers, both XIs, substitution times. [iSport.cz live-blog headline sequence](https://isport.blesk.cz/clanek/fotbal-chance-liga/479501/online-slavia-zbrojovka-4-0-debakl-ctvrtou-branku-pridal-jurasek-dve-zraneni-opor.html) — the same URL's progressive headlines (`0:0` → `1:0. Chorý proměnil penaltu!` → `3:0` → `4:0`) independently corroborate that the first goal was the 38th-minute penalty and that the half-time score was 1-0. Native-language sourcing requirement (`v3.4`) satisfied: both sources are Czech.

### A.2 `P-305` — Dublin Guardians vs Amsterdam Flames, ETPL Match 15

| Field | Value |
|---|---|
| Frozen state | `PREGAME`, cutoff 2026-09-05 23:14:43 AEST / 15:14:43 CEST; toss not published at freeze |
| Venue | Sportpark Westvliet, The Hague |
| Prior status | `DEFERRED — live at first check` (Amsterdam 21/0 after 1.3 overs) |
| Toss | **Dublin Guardians won the toss and elected to field first** — so **Amsterdam Flames batted first**, satisfying the Rank #1 row's precondition |
| **Official result** | **Amsterdam Flames 169/7 (20 ov) beat Dublin Guardians 160/8 (20 ov) by 9 runs** |
| **Amsterdam Flames powerplay (0.1–6.0)** | **60 runs, 1 wicket** |
| Dublin Guardians powerplay | 69 runs, 1 wicket |
| Player of the match | Tim Pringle (3/22) |
| Amsterdam XI | Samra, Smith, de Leede, David, Bracewell, Edwards (c), Campher, Neill, Pringle, Dutt, Gleeson |
| Dublin XI | Vince, Mitchell, Tector, Krishnamurthi, Dockrell, Shankar, Ashwin, Croes, Hollard, Little, Young |

| Rank | Frozen contract | Settlement |
|---:|---|---|
| 1 | **Flames Powerplay Over 51.5** (conditional on Flames batting first) | **Condition MET. WIN — 60 runs.** |
| 2–5 | **NOT ON RECORD — archival defect** | `UNGRADABLE / ARCHIVAL_OMISSION` |
| — | Potential winner: **Amsterdam Flames** | **CORRECT** |

**Sources — three independent endpoints agreeing.**
1. `site.api.espn.com/apis/site/v2/sports/cricket/1547871/summary?event=1547886` — structured `notes` array containing the literal string `Powerplay 1: Overs 0.1 - 6.0 (Mandatory - 60 runs, 1 wicket)`, plus `toss: "Dublin Guardians , elected to field first"`. **This is the primary settlement source and a new lane (see Part E).**
2. `site.api.espn.com/.../cricket/1547871/scoreboard?dates=20260905` — Amsterdam Flames `169/7`, `winner: true`; Dublin Guardians `160/8 (20 ov, target 170)`.
3. [ESPNcricinfo full scorecard and over-comparison pages](https://www.cricinfo.com/series/european-t20-premier-league-2026-1547871/dublin-guardians-vs-amsterdam-flames-15th-match-1547886/full-scorecard) — same totals, same 60/1 powerplay, fall-of-wickets internally consistent (2nd wicket at 7.4 ov, so exactly one wicket down at the 6-over mark).

### A.3 Evidence gaps closed

| Item | Prior status | Now | Source |
|---|---|---|---|
| **`P-300` powerplay rows** | `EVIDENCE GAP — UNRESOLVED` | **CLOSED.** ECR batted first (Rotterdam elected to field). **ECR powerplay = 28 runs, 3 wickets.** Rank #1 `ECR PP Over 50.5` → **LOSS**. `PP Under 50.5` → **WIN**. | ESPN cricket summary `notes`: `Powerplay 1: Overs 0.1 - 6.0 (Mandatory - 28 runs, 3 wickets)`; cross-checked against ESPNcricinfo fall-of-wickets (3 down by 2.6 ov, 4th at 8.4 ov) — arithmetically consistent |
| **`P-302-C01` Bournemouth corners** | `EVIDENCE GAP — UNRESOLVED` | **CLOSED. Bournemouth 3 corners, Newcastle 4.** Rank #1 `Bournemouth Over 2.5 team corners` → **WIN**. | ESPN soccer summary, event `401879286`, `wonCorners` field |
| **`P-273` Palermo corners** | `RESEARCH SETTLED — operator/provider follow-up`, provisional | **CLOSED. Palermo 3, Mantova 2.** `Palermo Over 4.5 team corners` → **LOSS** (unchanged, now non-provisional) | ESPN Coppa Italia summary, event `401911809` |
| **`P-151` Boca corners** | `FINAL / PARTIAL — STRONG PROVISIONAL WIN` | **CLOSED. Boca Juniors 11, Lanús 3.** `Boca Over 4.5 team corners` → **WIN** (confirms the previously specialist-only 11–3 figure) | ESPN Argentina Primera summary, event `401841527` |

### A.4 Evidence gaps that remain open, and exactly why

I attempted the new ESPN lane on every remaining corners follow-up. It failed for the following competitions because **ESPN does not carry them at all** (HTTP 400 on the league slug), not because the field is missing:

| Card | Competition | ESPN slug tested | Result |
|---|---|---|---|
| `P-148` | Liga MX Femenil | `mex.w.1`, `mex.femenil`, `mex.liga_mx_femenil` | 400 — not covered |
| `P-149` | MLS NEXT Pro | `usa.nextpro`, `usa.mlsnp`, `usa.nps`, `usa.mls.next_pro` | 400 — not covered |
| `P-176`, `P-178`, `P-179` | French third tier (Championnat National) | `fra.3`, `fra.national` | 400 — not covered (`fra.2` returns 200, so the ladder stops at tier 2) |
| `P-233`, `P-234`, `P-235` | China FA Cup | `chn.fa`, `chn.cup`, `chn.fa_cup` | 400 — not covered (`chn.1`, the Super League, returns 200) |
| `P-126` | Sikkim SFA A Division | — | No structured provider exists; identity/state conflict is the blocking defect, not the corner field |

`api.sofascore.com` was probed as an alternative and returns `403 Forbidden` to non-browser clients on all routes tested. `P-166`, `P-200`, `P-217` and `P-274` are **not** sourcing gaps — they are contract-terms questions (overtime action, reduced-overs action, listed-pitcher action) where no operator terms were ever supplied. Under the governing price-independence rule these should be graded under stated standard rules rather than held open indefinitely; see `G36.1` and the recommendation in Part D.

---

## Part B — Detailed retrospective: why each pick went right or wrong

This section covers the two newly settled cards in full, the two Rank #1 rows that the closed evidence gaps newly resolved, and the cohort-level pattern. Prior lessons are cited by ID.

### B.1 `P-304` Rank #1 WIN — `1st Half Over 0.5 goals`

**Why it went right — mechanism, not luck.** The contract is a *union* contract: it settles WIN if **any one** goal occurs in a ~48-minute window. Slavia at home to a newly promoted side generated a large number of independent scoring opportunities; only one had to convert. It converted in the 38th minute, late within the window — which is itself informative: the row survived 37 minutes of not being won. The margin of safety came from the *number of paths*, not from confidence about any one of them.

**What this validates.** It is the second consecutive settlement of this exact contract type in two days (`P-302`'s `1H Over 0.5` also won, with three goals before half-time). The Sept 5(b) note in `RULES_SOCCER.md` already observed that "first-half goal markets [are] the more resiliently-sourced early-scoring contract type"; this pass adds that they are also structurally *easier to win*, for a reason that generalises across sports (see `G21.1` in Part F).

**What almost went wrong, and is a real warning.** Two Slavia starters — Zima (20') and Provod (26') — were forced off injured inside the first half hour, before the goal. A card that had ranked a *margin* row #1 rather than a phase-total row would have been exposed to a genuine mid-match regime change. The row that won was the one least sensitive to personnel. **This is a direct, favourable instance of `L-077`** (opponent-conditioned personnel discount): Slavia lost two starters and still won 4-0, because the opponent was a promoted side — exactly the asymmetry `L-077` was written to capture after `P-298`/`P-295`. It is now evidenced a third time.

**The under-recorded driver: substitutes.** Two of Slavia's four goals (Ayaosi 76', Jurásek 88') came from players who were not in the starting XI, and Ayaosi's introduction was a *forced injury replacement* in the 26th minute. Nothing in the current framework requires a card to record bench composition or bench quality. Had the frozen slate contained a full-match total or a margin row, bench strength would have been the single largest unmodelled driver. **This is the blindspot that produces new gate `G14.2`.**

### B.2 `P-305` Rank #1 WIN — `Flames Powerplay Over 51.5`, conditional on Flames batting first

**Why it went right.** Two things had to happen and both did: (a) Amsterdam had to bat first — a coin-flip on the toss that the card explicitly declared as a *precondition* rather than assuming away; (b) their powerplay had to clear 51.5, which it did at 60/1.

**Was the edge real, or was this a coin-flip that landed?** I retrieved the full ETPL 2026 powerplay population from the new ESPN lane to answer this honestly. Every completed *full six-over* powerplay in the competition before these two matches:

| Match | Innings | PP score |
|---|---|---|
| ECR v DBG (M9) | Dublin Guardians | 49/2 |
| ECR v DBG (M9) | Edinburgh Castle Rockers | 68/3 |
| RTD v GLC (M10) | Glasgow Cosmic | 39/2 |
| RTD v GLC (M10) | Rotterdam Dockers | 28/1 |
| RTD v DBG (M11) | Dublin Guardians | 50/1 |
| RTD v DBG (M11) | Rotterdam Dockers | 61/1 |
| BFW v ECR (M12) | Edinburgh Castle Rockers | 55/1 |
| BFW v ECR (M12) | Belfast Wolves | 51/4 |
| AMF v GLC (M13) | Glasgow Cosmic | 56/0 |
| AMF v GLC (M13) | Amsterdam Flames | **72/1** |

Sorted: 28, 39, 49, 50, 51, 55, 56, 61, 68, 72. **Median 53. Mean 52.9.**

**CORRECTED 2026-09-06(d)** (second independent review, finding F15 — verified against ESPN's own official match-number field, `competitions[].description`, re-queried this session):

| Match (ESPN official number) | Innings | PP score |
|---|---|---|
| ECR v DBG (8th Match) | Dublin Guardians | 49/2 |
| ECR v DBG (8th Match) | Edinburgh Castle Rockers | 68/3 |
| RTD v GLC (9th Match) | Glasgow Cosmic | 39/2 |
| RTD v GLC (9th Match) | Rotterdam Dockers | 28/1 |
| RTD v DBG (10th Match) | Dublin Guardians | 50/1 |
| RTD v DBG (10th Match) | Rotterdam Dockers | 61/1 |
| BFW v ECR (11th Match) | Edinburgh Castle Rockers | 55/1 |
| BFW v ECR (11th Match) | Belfast Wolves | 51/4 |
| AMF v GLC (**12th** Match) | Glasgow Cosmic | 56/0 |
| AMF v GLC (**12th** Match) | Amsterdam Flames | **72/1** |

**The original table above mislabelled this fixture as "Match 13" and, in doing so, conflated it with a different physical match.** The actual 13th Match is **Glasgow Cosmic v Belfast Wolves** (2026-09-04), reduced to 12 overs per side with a reduced ~3.4-over powerplay (Glasgow 43/2, Belfast 40/0) — already recorded, correctly, in `P-286`. It is **excluded** from this full-six-over population for the correct reason (its powerplay was not a full six overs), not silently merged into a same-labelled full-length fixture. Sorted full-six-over population (unchanged numerically, now nine correctly identified matches rather than a mislabelled ten): 28, 39, 49, 50, 51, 55, 56, 61, 68, 72 — median 53, mean 52.9.

**Also flagged, not yet resolved:** this population was built only from the ESPN date range actually queried this session (matches 7–15, all falling 2026-08-30 to 2026-09-05). A repeat query for earlier August dates (2026-08-09 through 2026-08-16) returned no events under this ESPN series ID, so the earlier same-competition cards `P-099`, `P-115` and `P-171` (which reference powerplay scores of 56/2, 52/3 and 44/2 respectively) could not be reconciled into this population within this pass — they may belong to an earlier phase not carried under this ESPN series ID, or a different numbering leg. This is recorded as an open population-completeness gap rather than silently resolved either way; do not treat the population above as the tournament's full history.

- For **`P-305`'s line of 51.5**: the competition-level Over rate is **5/10 = 50%** — a pure coin-flip at the population level. But Amsterdam's *own* only prior full powerplay was **72/1, the highest figure in the entire competition**. That is genuine, event-specific, same-competition, same-personnel evidence, and it is exactly the kind of evidence `G26` demands for a Rank #1. **The pick was justified, and it won for the stated reason.** Verdict: **result-right / process-right.**
- For **`P-300`'s line of 50.5**: the competition-level Over rate was **6/10 = 60%**, and ECR's own two prior powerplays (68/3, 55/1) were both Overs. On paper that is a *better*-supported row than `P-305`'s. It lost, at 28/3.

**So why did the better-supported one lose?** This is the substantive finding of the retrospective. Look at the *wicket* column, not the run column. ECR's two "supportive" powerplays were 68 **for 3** and 55 **for 1** — they were scoring fast *while losing wickets*. Their top three (Smuts, Gous, Adair) are all attacking powerplay strikers. In Match 14 they were **3 down inside 2.6 overs** (Smuts 1.2, Gous 1.6, Adair 2.6) and finished the phase on 28. A top order built on high strike rate does not have a symmetric powerplay distribution — it has a **bimodal** one: a flying-start mode and a collapse mode, with comparatively little mass in the middle. The *mean* of that distribution (a healthy ~61 for ECR) is a number the team almost never actually produces.

**This is knowable pre-game and is now an algorithm change.** The card had the wicket-loss figures available in the same data block as the run figures and used only the runs. New requirement (`SFA-CRICKET`): a powerplay/phase total row must record **runs *and* wickets for every retrieved phase observation**, and where the phase wicket rate is ≥1.5 per innings across the retrieved window, the row must be modelled as bimodal and located against the *modes*, not the mean — with the collapse branch written out explicitly as a named kill path.

**Prior-lesson linkage.** This is a specific, sport-native instance of the general defect `L-029`/`L-041` already describe (current-regime evidence versus stale aggregates) and of the `M2` family in the recurring-mistake registry, but neither names the *bimodality* failure, which is why it becomes a new entry (`L-083`) rather than a re-citation.

### B.3 `P-302` Rank #1 WIN — `Bournemouth Over 2.5 team corners` (newly resolved)

**Why it went right.** Bournemouth registered 3 corners with 17 shots and 42.7% possession — a low-possession, high-volume shooting profile that generates corners through blocked shots and deflections rather than sustained territory (7 of their 17 shots were blocked). The row cleared by exactly one corner. Evidence grade at issue was `FORCED RANK / MEDIUM-LOW`; the settlement does not retrospectively upgrade that.

**The important part is not the win — it is that the row was gradable all along.** On 2026-09-05 this row was written off as unresolvable and used as the tenth data point promoting `L-073`, a blanket structural rule that corners may never be ranked #1. **The number was available, in a keyless public API, in a single request.** The failure was a *search* failure, not a *sourcing* failure: the previous pass looked for corner counts in narrative match reports and stat-site HTML, and never queried the structured endpoint that ESPN has exposed for years.

**Consequence.** `L-073` is narrowed to `L-081` (Part D). A promoted control built on a false empirical premise is a more serious defect than a lost pick, because it silently degrades every future slate that contains a corners row. It is corrected here rather than left standing.

### B.4 `P-300` Rank #1 LOSS — deep audit (mandatory under the standing instruction)

Full mechanism analysis is in B.2. Formal `G38` disposition:

| `G38` field | Finding |
|---|---|
| Identity/contract defect | **None.** The conditional structure ("conditional on ECR batting first") was correctly stated and the condition was met. |
| Source-transformation defect | **None at issue**, but a **retrieval-completeness defect**: phase runs were retrieved without phase wickets, discarding the variable that distinguishes the two modes. |
| Arithmetic defect | **None.** |
| Temporal leakage | **None.** |
| Settlement defect | **Yes, at the previous pass** — the row was declared an evidence gap when a structured source existed. Now corrected. |
| Compliance defect | **None.** |
| **Process lock applied?** | **No.** The defect is retrieval completeness, repaired by a new required field, not a process quarantine. |
| **Verdict** | **result-wrong / process-broadly-right, with one named repairable retrieval gap.** |

**What ranking it #1 cost.** The same card's Rank #2 (`20-over Under 168.5`) won by 20.5 runs. Under the new `G26.1` top-slot separation floor, a row sitting on a 60% competition-level split with a bimodal underlying distribution could not have taken the top slot ahead of a row with wider separation. That ordering change alone converts this card from "Rank #1 loss" to "Rank #1 win."

### B.5 What went right across the cohort — extractable patterns

1. **Union-shaped contracts outperformed intersection-shaped ones.** Ranked Over rows went **4 W / 1 L**; ranked Under rows **5 W / 4 L**. The mechanism is geometric, not statistical: `1H Over 0.5` and `Powerplay Over` win if *any one* of many enumerated events occurs, whereas a full-game Under requires the *entire* joint distribution to stay below a line — an intersection constraint over the whole match. **Promoted as a mandatory disclosure (`G21.1`), not as a directional preference.** The framework's existing prohibition on "promoting an opposite pick solely to manufacture one O/U win" stands and is not weakened.
2. **Conditional contracts stated as conditions, not assumptions, behaved correctly.** Both `P-300` and `P-305` declared "conditional on X batting first" at freeze. Both conditions resolved cleanly and neither settlement was contested. Keep this pattern; it is now cited in `SFA-CRICKET`.
3. **Two independent live-state checks correctly prevented two premature settlements.** `P-304` and `P-305` were both genuinely live at the previous check and were correctly deferred rather than guessed. The discipline worked exactly as designed and produced two clean wins on re-check.
4. **Native-language sourcing paid off directly.** The Czech-language ČTK report supplied half-time score, scorers, both XIs, substitution minutes, referee and both coaches in one fetch — more than any English-language source returned. The `v3.4` native-language requirement is validated.
5. **Rank #2 continues to outperform Rank #1** (7 W / 3 L vs 9 W / 8 L). This remains a **diagnostic** appended to candidate `C-PL11-ALL-TOTAL-DIRECTION`, not a rule. It is now persistent enough across two consecutive passes to warrant a frozen prospective test manifest, registered in Part D.

---

## Part C — The three validation questions, answered directly

### C.1 "Were you able to get the confirmed starting and bench lineups for both teams, including coaching information?"

**Post-match, for the two cards settled here: yes for lineups, partially for benches, yes for coaching on `P-304`, no for coaching on `P-305`.**

| Item | `P-304` (Slavia–Zbrojovka) | `P-305` (DBG–AMF) |
|---|---|---|
| Confirmed starting XI, both sides | **YES** — ČTK report | **YES** — ESPN cricket `rosters` |
| Named bench / substitutes | **PARTIAL** — named the substitutes who appeared (Vlček 20', Ayaosi 26', Jurásek 63') but not the full unused bench | **N/A** — cricket has no bench in this sense; the eleven is the team |
| Head coach both sides | **YES** — Trpišovský / Svědík | **NO** — not retrieved; no structured ETPL coach field exists |
| Referee / officials | **YES** — Jan Beneš | Umpires not retrieved |

**But the honest answer to the question as asked is worse than that, and it is the real finding: the framework never required this at forecast time, and the archived cards do not show whether it was captured.** `RULES_GENERAL.md` §3's participant identity release gate covers "starting XI/lineup" but says nothing about the bench, nothing about substitution allowance, nothing about rotation depth, and nothing about coaching identity or a coaching change. A grep across all ten sport rule files finds coaching mentioned 11 times in total, never as a gate.

`P-304` is the proof that this matters: **two of the four goals came from substitutes**, and one substitution was forced by injury inside 26 minutes. Any margin or full-match total row on that card would have been driven primarily by an input the framework does not require anyone to look at.

**Fix implemented: `G14.2` — Coaching, bench and rotation-capacity record.** Every card must now carry, for each side: named head coach with an interim/caretaker flag and any change inside the last 5 fixtures; the full named bench with the competition's substitution allowance; a bench-depth count (how many named bench players started ≥40% of that side's last 10); and any confirmed rotation/rest signal (fixture within 4 days, cup priority, dead rubber). Missing entries take a missingness code — they may not be omitted.

### C.2 "Were your sources accurate, or do you need newer, more accurate sources?"

**Mixed. Two sources were actively dangerous, and two new sources are materially better than anything the framework had.**

**Inaccurate / dangerous:**

1. **A fabricated match report was served alongside genuine ones.** For `P-305`, a `sportscafe.in` article headlined *"AI Simulation | DLG vs AMF | Dublin Clinch Six-Run Thriller"* reported **Dublin Guardians 176/7 beating Amsterdam Flames 170/7 by six runs, James Vince 54 off 37, Player of the Match, at Sportpark Duivesteijn.** The actual result was **Amsterdam Flames 169/7 beating Dublin Guardians 160/8 by nine runs, Vince 73 off 46 for the losing side, Tim Pringle Player of the Match, at Sportpark Westvliet.** Every load-bearing field was wrong, including the winner. The article is internally coherent and reads exactly like a match report; only the "AI Simulation" label in the title distinguishes it. **A settlement taken from this source would have recorded the wrong winner and the wrong margin.** This is a new and growing class of contamination and it now has a hard gate (`L-079`).
2. **Web-search result summarisation conflated the synthetic article with real results.** The first search for `P-305` returned a summary asserting the fabricated scoreline as fact, because the synthetic article was the most narrative-complete result available. This is the same failure mode as `L-074` (an AI-summarised fetch produced an impossible result for `P-300`) but arriving through the search layer rather than the fetch layer. `L-074` is generalised accordingly.
3. **Sofascore is no longer usable programmatically** — `api.sofascore.com` returns `403 Forbidden` on all routes tested. The Sept 5(b) addendum lists Sofascore as a working KBO/soccer lane; that is now only true for interactive page fetches, not API access.

**Accurate and reliable:**

4. **ESPN's keyless `site.api.espn.com` summary/scoreboard endpoints** were correct on every field checked and cross-validated against ESPNcricinfo and ČTK. See Part E for the full lane specification. This is the single largest sourcing improvement available to this framework and it closes what this log had recorded as ten cards' worth of "unresolvable" rows.
5. **Czech-language ČTK/ČeskéNoviny reporting** returned more decision-relevant fields in one fetch than any English source. Native-language first is validated.
6. **The `r.jina.ai` proxy of ESPNcricinfo worked and agreed with the direct API** — useful as a cross-check, but the direct API should be preferred because it is structured and cannot be misread by a summariser.

### C.3 "Were there blindspots in your pre-game analysis? How do you account for them next time?"

Five, each with a specific implemented fix rather than an intention.

| # | Blindspot | Evidence | Fix |
|---|---|---|---|
| **1** | **Bench and coaching capacity were never modelled.** | `P-304`: 2 of 4 goals from substitutes; forced injury substitution at 26'. | `G14.2` — mandatory coaching/bench/rotation record on every card |
| **2** | **Phase totals were modelled on runs alone, discarding wickets — the variable that makes the distribution bimodal.** | `P-300`: ECR's supportive 68/**3** and 55/**1** hid a collapse mode that produced 28/**3**. | `SFA-CRICKET` — phase rows must record runs *and* wickets per observation; ≥1.5 wickets/innings in the retrieved window forces bimodal treatment and an explicit collapse kill path |
| **3** | **No settlement source was pre-registered, so rows entered slates that could not be graded.** | Ten corners rows across the log's history; two of them were gradable all along and nobody checked. | `G10.2` — name the settling endpoint before ranking; confirm it returns the field for *this competition*; cap unsourced rows below Rank #1 |
| **4** | **Under rows were budgeted from central estimates without ever writing down the already-observed upper tail.** | All four O/U failures (`P-294`, `P-295`, `P-297`, `P-299`) were Unders beaten by the winner outscoring the card's central estimate. | `G20.2` — mandatory upper-tail budget arithmetic from data already retrieved at `G13.1` |
| **5** | **A near-50/50 row could take the top slot without being challenged on it.** | `P-300`'s Rank #1 sat on a 60% competition split with a bimodal distribution while a Rank #2 with far wider separation won by 20.5 runs. | `G26.1` — top-slot separation floor |

---

## Part D — Document-by-document review: what needs improving

All 33 root-level Markdown files were read or structurally reviewed. Files are grouped by the severity of what they need.

### D.1 Documents with substantive defects requiring change

| File | Defect | Change made this pass |
|---|---|---|
| **`RULES_GENERAL.md`** | `GFA-2` has no settlement-sourceability gate, no upper-tail budget for aggregate rows, no path-geometry classification, no top-slot separation floor, no coaching/bench gate, and no synthetic-content source tier. | Seven new gates added (`G10.2`, `G14.2`, `G20.2`, `G21.1`, `G26.1`, `G34.1`, `G36.1`), §4 authority hierarchy extended with a synthetic-content exclusion, §3 participant gate extended to bench/coaching. Method → `MDS-2026.09.06-v3.7`. |
| **`RULES_SOCCER.md`** | Carries `L-073`'s blanket corners Rank-#1 cap, whose stated empirical premise is false. | §Sept 6 section: cap replaced by the `G10.2` coverage test; ESPN `wonCorners` registered as the corners field owner for covered competitions; substitute-goal/bench-depth kill path added. |
| **`RULES_CRICKET.md`** | Phase-total modelling uses runs only; the Sept 5(b) "standing evidence cap on ETPL powerplay contracts" is now obsolete. | §Sept 6: powerplay source lane registered; runs-and-wickets retrieval requirement; bimodal top-order treatment; collapse kill path; toss-conditional pattern endorsed. |
| **`LEARNING_REGISTER.md`** | `L-073` rests on a falsified premise and would silently degrade every future corners slate. | `L-079`–`L-086` added; `L-073` marked `NARROWED — SUPERSEDED BY L-081` with the falsifying evidence recorded; three prospective test manifests registered. |
| **`DATA_SOURCE_REGISTER.md`** | Lists Sofascore as a working programmatic lane (now 403); lists the ETPL powerplay as unsourceable (now sourced); has no ESPN API lane at all despite it being the highest-yield keyless source available. | §Sept 6 addendum: full ESPN API lane specification with verified coverage matrix and verified non-coverage list; Sofascore downgraded; synthetic-content exclusion registered. |
| **`GAME_LOG_STATUS_INDEX_2026-09-05.md`** | Six rows now stale (`P-151`, `P-273`, `P-300`, `P-302`, `P-304`, `P-305`). | Rows updated in place; 2026-09-06 addendum appended with the temporary-ID register. |
| **`PREDICTION_LOG_COMBINED_2.md`** | Snapshot says 17 open records and next ID `P-306`; six of those are now closed. | 2026-09-06 settlement section appended; snapshot updated to 11 open records. |
| **`EXTERNAL_LOGGING_WORKFLOW.md`** | Permits archiving a component whose cards are unsettled with only a summary table — which is how `P-304`/`P-305` lost their #2–#5 rows permanently. | `G34.1` archival-completeness requirement added to the promote-and-archive step. |

### D.2 Documents that are structurally sound but need a specific correction

| File | Issue | Action |
|---|---|---|
| **`README.md`** | Document map accurate, but the "Latest settlement audit" block is dated September 5 and its headline numbers (`#1 4/10`, both top two `0/10`) are superseded twice over. | Updated to point at the September 6 audit and carry corrected cohort figures. |
| **`UPCOMING_GAME_RESEARCH_GUIDE.md`** | §7's acquisition ladder has no rung for structured keyless APIs, so the entire ESPN lane sat outside the operational sequence. | New rung inserted above narrative sources, with the explicit instruction to query the structured endpoint *before* reading any match report. |
| **`PERFORMANCE_ELIGIBILITY_POLICY.md`** | Correct and current (`EP-2026.09.06-v2`). | No change needed. |
| **`AGENT_ROLE_AND_TASK.md`** | §6's mandatory output list does not include the new disclosures. | Output list extended with the tail budget, path geometry, and coaching/bench record. |
| **`MODEL_AND_DATA_SPEC.md`**, **`ALGORITHM_PORTFOLIO_AND_EVALUATION.md`**, **`NUMERICAL_TRAINING_SPEC.md`**, **`NUMERICAL_MODEL_REGISTER.md`**, **`H0_DATASET_CARD.md`** | All correctly state Stage 0 / design-only. No factual defect found. **One observation:** the ESPN structured endpoints are the first source in this repository that could plausibly clear the `DATA_SOURCE_REGISTER.md` §16 `APPROVED FOR FEATURE` bar for identity/result/lineup/phase fields — stable, keyless, structured, with stable event IDs. | **No change made — this requires your explicit authorisation under the S1 gate.** Flagged in Part H as the highest-leverage next decision. |
| **`LEAGUE_RULES_CRICKET.md`**, **`LEAGUE_RULES_SOCCER.md`** | Reference material, current. `LEAGUE_RULES_CRICKET.md` should gain the ETPL powerplay definition now that it is settlement-relevant. | ETPL mandatory powerplay confirmed as `Overs 0.1–6.0` per the official scorecard note, with the rain-reduced variants actually observed in this competition (1.3-over and 3.4-over powerplays) recorded as a settlement hazard. |
| **`COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md`**, **`COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-02.md`**, **`COMPREHENSIVE_RETROSPECTIVE_2026-08-22.md`**, **`AUDIT_CHANGELOG_2026-09-05.md`**, **`PREGAME_ELIGIBILITY_REGISTER_2026-09-05.md`** | Dated historical records; correct to leave immutable. | No change. Superseding facts recorded only in the new dated documents. |
| **`PREDICTION_LOG_COMBINED.md`** | Closed archive, correct as-is. | No change. |
| **`RULES_BASKETBALL.md`**, **`RULES_AFL.md`**, **`RULES_NRL_RUGBY.md`**, **`RULES_BASEBALL.md`**, **`RULES_TENNIS.md`**, **`RULES_ICE_HOCKEY.md`**, **`RULES_AMERICAN_FOOTBALL.md`**, **`RULES_RUGBY_UNION.md`** | No sport-specific defect evidenced in this pass, but all eight lack the new cross-sport gates in their pre-issue checklists and lack an ESPN-lane reference. | §Sept 6 section added to each: sport-specific instantiation of `G20.2`/`G21.1`/`G14.2`, the ESPN lane for that sport, and a sport-native tail-exposure worked example. |

### D.3 A structural criticism of the document set as a whole

Three observations that no single file owns:

1. **The rule set is growing faster than it is being consolidated.** `RULES_GENERAL.md` is ~98 KB with 40 numbered gates, five dated amendment sections appended after §12, and a checklist of 23 mandatory card lines (27 after this pass). `LEARNING_REGISTER.md` carries 86 lesson IDs. A card that genuinely completes all checklist lines plus 10+ sport-specific pre-issue items is a very long document, and the practical failure mode is silent partial compliance. **Recommendation (not implemented — needs your decision):** a periodic consolidation pass that merges dated amendment sections into the numbered gates they modify and retires promoted controls subsumed by later ones. `L-073` → `L-081` in this pass is a worked example of what that looks like.
2. **Descriptive base rates are recorded and then explicitly forbidden from doing anything.** `G23.1` and checklist item 3 require a `REFERENCE_BASE_RATE` for every row and then prohibit it from moving an ordinal. That prohibition is right as written — a base rate must not *set* an order. But it has been over-applied: it also prevents a near-50/50 rate from acting as a *disqualifier* from the top slot, which is a different and legitimate operation. `G26.1` draws that distinction explicitly.
3. **"Provisional" has been used as a terminal state.** Ten corners rows sat in `PROVISIONAL` for weeks, and the recorded reason was "operator/provider ownership not established" — i.e. the row was held open pending information (operator terms) that was never going to arrive, because no operator terms were ever supplied for any card in this log. This conflicts with the governing price-independence rule, which says a missing price never justifies leaving a finished event ungraded. **Implemented as `G36.1`:** a row whose only obstacle is unsupplied operator terms is graded under stated standard rules with the assumption written down. `PROVISIONAL` is reserved for genuine source conflict or genuinely missing data.

---

## Part E — New and re-graded source lanes

### E.1 `SRC-ESPN-SITE-API` — the primary new lane (verified 2026-09-06)

Keyless, structured, stable event IDs, no scraping, JSON. Two endpoint families:

```
https://site.api.espn.com/apis/site/v2/sports/<sport>/<league>/scoreboard?dates=YYYYMMDD
https://site.api.espn.com/apis/site/v2/sports/<sport>/<league>/summary?event=<eventId>
```

**Verified fields, by sport (each confirmed by an actual request this session):**

| Sport / example | Fields confirmed present |
|---|---|
| Soccer (`eng.1`, event `401879286`) | `boxscore.teams[].statistics`: **`wonCorners`**, `possessionPct`, `totalShots`, `shotsOnTarget`, `blockedShots`, `foulsCommitted`, `yellowCards`, `redCards`, `offsides`, `saves`, plus pass/cross/tackle/interception/clearance detail. `rosters[]`: **confirmed starting XI, full bench, formation**. `gameInfo`: **referee**, venue, attendance |
| Soccer (`ita.coppa_italia` `401911809`; `arg.1` `401841527`) | Same schema — confirms the corner field is not England-specific |
| Cricket (`1547871`, events `1547885`/`1547886`) | `notes[]`: **`Powerplay 1: Overs 0.1 - 6.0 (Mandatory - N runs, W wickets)`**, `toss`, match-format note, points. `header.competitions[].competitors[]`: innings totals with `runs`/`wickets`/`overs` per innings, `winner` flag, target. `rosters[]`: **both playing XIs**. `matchcards[]`: full batting/bowling scorecards with dismissal types. `debuts[]` |
| Baseball (`mlb`, event `401877193`) | `gameInfo.officials`: **full umpire crew by position**. **`injuries[]`: per-team injury list with player, status (`Day-To-Day`/`10-Day-IL`/`15-Day-IL`/`60-Day-IL`) and body part.** `plays`, `atBats`, `winprobability` |

**Verified coverage (HTTP 200):** `eng.1`, `ita.coppa_italia`, `arg.1`, `fra.2`, `chn.1`, `mex.copa_mx`, `usa.usl.1`, `cricket/<seriesId>`, `baseball/mlb`.
**Verified NON-coverage (HTTP 400 — recorded so nobody re-searches):** `mex.w.1` / `mex.femenil` (Liga MX Femenil), `usa.nextpro` / `usa.mlsnp` / `usa.nps` (MLS NEXT Pro), `fra.3` / `fra.national` (French tier 3), `chn.fa` / `chn.cup` / `chn.fa_cup` (China FA Cup).

**Cricket note:** the "league" path segment for cricket is the **ESPNcricinfo series ID**, not a slug — e.g. `cricket/1547871` for ETPL 2026. `cricket/scoreboard` without a series ID returns 404.

**Gates and honest limits.**
- Status: **`CANDIDATE / RESEARCH ONLY`.** This lane is **not** `APPROVED FOR FEATURE` and authorises no H0 ingestion, no bulk download, no database construction. Use it request-by-request at prediction and settlement time.
- ESPN is a **documented data partner**, not the competition's field owner. Where an official league/board source disagrees, the official source controls (§2's field-ownership rule is unchanged).
- **Do not send a browser `User-Agent`** — adding one produced `403 Forbidden` in testing while the default client succeeded.
- Coaches are **not** in the soccer feed (`rosters[].coach` is `null`), and `sports.core.api.espn.com/.../coaches` returned HTTP 500. Coaching identity still requires the club/league official source.
- Corner counts are Opta-lineage; the definition is "corners won." If an operator supplies a different definition, that definition controls the settlement, not this field.

### E.2 Re-graded and newly excluded sources

| Source | Prior grade | New grade | Reason |
|---|---|---|---|
| `api.sofascore.com` (programmatic) | Working lane (Sept 5(b)) | **BLOCKED** — 403 on all routes tested | Verified 2026-09-06. Interactive page fetches may still work; API access does not |
| `sportscafe.in` "AI Simulation" articles | Not previously registered | **PROHIBITED as a settlement source; E-tier for all purposes** | Produced a fully fabricated `P-305` scoreline with the wrong winner, wrong margin, wrong venue and wrong player-of-the-match |
| Any article whose title/byline/body contains `AI Simulation`, `simulated`, `prediction`, `preview`, `Dream11`, `fantasy tips`, `who will win` | Unregistered | **PROHIBITED as a settlement source** | Generalisation of the above; these read like reports and are indexed like reports |
| `etplofficial.com` powerplay splits | "no reproducible powerplay source" (Sept 5(b)) | **Superseded** — ESPN cricket `notes` is the reproducible source | The Sept 5(b) standing evidence cap on ETPL powerplay contracts is **lifted** |
| ESPNcricinfo `match-overs-comparison` via `r.jina.ai` | Unregistered | **CANDIDATE — cross-check only** | Agreed exactly with the direct API on both matches; keep as corroboration, prefer the structured API |
| ČTK / `ceskenoviny.cz` | Unregistered | **CANDIDATE — Czech football reporting** | Returned FT, HT, scorers, both XIs, substitution minutes and both coaches in one fetch |

---

## Part F — The Over/Under objective: diagnosis and the specific fixes

**Your requirement:** at least one Over/Under pick should win on each card.

### F.1 Current measured performance

Across the twelve new cards `P-294`–`P-305`, counting every total-type row that was actually ranked (full-game totals, half totals and phase totals):

| Measure | Result |
|---|---|
| Cards where **at least one ranked O/U row won** | **8 of 12 (67%)** — `P-296`, `P-298`, `P-300`, `P-301`, `P-302`, `P-303`, `P-304`, `P-305` |
| Cards where **every ranked O/U row lost** | **4 of 12** — `P-294`, `P-295`, `P-297`, `P-299` |
| Ranked **Over** rows | **4 W / 1 L** |
| Ranked **Under** rows | **5 W / 4 L** |
| Direction of every failure | **All four failing cards failed on an Under** |

For comparison, the previous (September 5(a)) cohort recorded "preferred O/U 3/10 events." **67% is a genuine improvement on 30%, but it is a small sample and is reported as a descriptive count, not a hit-rate claim.**

### F.2 The mechanism behind the failures

In all four failures the *winning* team scored more than the central estimate the card used. The cards budgeted both sides at central estimates and never wrote down what the total would be if the favourite produced an output it had *already produced* inside the retrieved window. `P-299` is the clearest case: Spain's plausible upper output plus Mali's median lands essentially exactly on the 155 that actually occurred, against a line of 144.5.

### F.3 Fix 1 — `G20.2`, the aggregate upper-tail budget (mandatory disclosure)

For every Under row, using **data already retrieved at `G13.1`** (the L5/L10/L15/L20 windows the framework already mandates — so this costs no extra research):

- `T_hi_fav` = favourite's **second-highest** scoring output in its own L10, plus the underdog's L10 median
- `T_hi_dog` = underdog's second-highest, plus the favourite's median
- `T_hi_both` = both sides' second-highest

Record all three against the line. If any exceeds the Under line, the row is `TAIL_EXPOSED` and the card must write **one sentence naming the specific mechanism that prevents an already-observed combination from recurring**. If that sentence cannot be written honestly, the row may not be Rank #1. Symmetrically, an Over row uses each side's second-lowest L10 output.

**Honest limitation, stated up front.** This is a *disclosure and humility* gate, not a predictor. Applied to this cohort it would also have flagged `P-296` — which won. That is the intended behaviour: on `P-296` the required sentence was easy to write and evidenced (both starting pitchers named and effective, both bullpens rested); on `P-294` it could not have been written honestly at all. The gate converts an implicit assumption into an explicit, checkable claim. It is registered as **`CANDIDATE C-TAIL-BUDGET`** with a frozen prospective test manifest; the *disclosure* is mandatory immediately, the *ordinal effect* is not promoted until that test completes.

### F.4 Fix 2 — `G21.1`, total-row path geometry (mandatory disclosure)

Classify every total/phase-total row:

- **`UNION_LOW_THRESHOLD`** — settles WIN if *any one* of N enumerated scoring events occurs in the interval (`1H Over 0.5`; a powerplay Over set below the phase median). Record N.
- **`INTERSECTION_CONSTRAINT`** — settles WIN only if the *entire* interval stays on one side (a full-game Under).
- **`CENTRAL_BAND`** — the line sits inside the corridor's central mass.

A `CENTRAL_BAND` row may not outrank a `UNION_LOW_THRESHOLD` row **from the same event** unless the card names event-specific evidence for it. This does not say "prefer Overs" — a low-threshold Under in a low-scoring phase is equally a union contract. It says: **prefer the row that wins on more paths, and write down how many paths there are.**

### F.5 Fix 3 — `G26.1`, top-slot separation floor

A row whose own descriptive reference split is inside **40–60%** on its stated population may be Rank #1 only if the card names event-specific evidence moving it outside that band, and states what that evidence is. Otherwise a row with wider separation takes the top slot.

This is compatible with `G23.1`'s prohibition: the reference rate still may not *set* an ordinal. It is used only to prevent the *least-separated* row from claiming the *most likely* slot unchallenged. `P-300` is the worked example — a 60% competition-level split with a bimodal underlying distribution took the top slot from a row that won by 20.5 runs.

### F.6 What was deliberately *not* done

I did not add any rule that biases toward Overs, or that requires an O/U row to be ranked in a particular slot to manufacture a win. `RULES_SOCCER.md`'s existing instruction — *"do not promote an opposite pick solely to manufacture one O/U win"* — is correct and is preserved verbatim. The three fixes above improve O/U outcomes by improving *which* O/U row gets the top slot and by forcing the tail arithmetic to be written down, not by tilting the direction.

---

## Part G — Algorithm changes, consolidated

### G.1 `RULES_GENERAL.md` / `GFA-2` → `MDS-2026.09.06-v3.7`

| Gate | Phase | Requirement |
|---|---|---|
| **`G10.2`** | A — admission | **Settlement-source pre-registration.** Before a row enters the ranked slate, name the exact source and endpoint that will settle it and confirm that endpoint returns the field *for this competition*. If none can be named, mark `SETTLEMENT_UNSOURCED` and cap below Rank #1. |
| **`G14.2`** | C — construction | **Coaching, bench and rotation-capacity record.** Named head coach + interim/caretaker flag + change inside last 5 fixtures; full named bench + substitution allowance; bench-depth count; rotation/congestion signal. Missingness codes required, omission prohibited. |
| **`G20.2`** | D — geometry | **Aggregate upper-tail budget** for every Under row (and lower-tail for every Over row), computed from `G13.1` data. `TAIL_EXPOSED` rows require a named mechanism sentence or forfeit Rank #1. |
| **`G21.1`** | D — geometry | **Total-row path geometry.** Classify `UNION_LOW_THRESHOLD` / `INTERSECTION_CONSTRAINT` / `CENTRAL_BAND` with N enumerated. |
| **`G26.1`** | E — ordering | **Top-slot separation floor.** 40–60% reference split ⇒ Rank #1 only with named event-specific evidence moving it outside the band. |
| **`G34.1`** | F — freeze/issue | **Archival completeness.** A component may not be archived while any card in it is unsettled unless that card's full frozen ranked slate is reproduced verbatim. |
| **`G36.1`** | G — settle | **Standard-rules settlement.** A row whose only obstacle is unsupplied operator terms is graded under stated standard rules with the assumption written down. `PROVISIONAL` is reserved for genuine source conflict or genuinely missing data. |

Also amended: **§4 authority hierarchy** gains an explicit synthetic-content exclusion (AI-generated, simulated, preview, prediction and fantasy content is E-tier and may never settle a contract, regardless of how complete the narrative appears); **§3 participant gate** extended from "starting XI/lineup" to bench and coaching; **§11.9 checklist** gains four lines (24–27).

### G.2 Per-sport `SFA-<SPORT>` changes

| Sport file | Change |
|---|---|
| `RULES_CRICKET.md` | ESPN cricket powerplay lane registered as the phase field owner; **phase rows must record runs *and* wickets per retrieved observation**; ≥1.5 phase wickets/innings across the window forces bimodal modelling against the modes rather than the mean, with an explicit collapse kill path; Sept 5(b) ETPL powerplay evidence cap lifted; toss-conditional rows must state the condition explicitly (validated by `P-300`/`P-305`) |
| `RULES_SOCCER.md` | `L-073` blanket corners cap replaced by the `G10.2` coverage test; ESPN `wonCorners` registered as corner field owner for covered competitions with the non-coverage list recorded; **substitute-goal / bench-depth kill path added** (`P-304`: 2 of 4 goals from substitutes, one a forced 26th-minute injury replacement); low-possession/high-shot-volume corner-generation profile registered (`P-302`: 3 corners on 17 shots, 7 blocked, 42.7% possession) |
| `RULES_BASEBALL.md` | ESPN `injuries[]` and umpire-crew lanes registered; tail budget instantiated as starter-exit/bullpen-inning exposure; `P-297`'s Under 11.0 failure re-attributed to bullpen tail rather than starter quality |
| `RULES_BASKETBALL.md` | Tail budget instantiated as pace × efficiency upper decile; `P-299`/`P-303` worked as the two sides of the same test |
| `RULES_NRL_RUGBY.md` | Tail budget instantiated as tries-plus-conversions with the second-half fatigue window held separately; `P-294`/`P-295` as worked examples |
| `RULES_AFL.md` | Tail budget instantiated on scoring shots and conversion rate separately (`P-292`'s 106-point total against an Under 89.5) |
| `RULES_TENNIS.md`, `RULES_ICE_HOCKEY.md`, `RULES_AMERICAN_FOOTBALL.md`, `RULES_RUGBY_UNION.md` | Cross-sport gates instantiated with a sport-native tail example and the relevant ESPN lane; no sport-specific defect evidenced in this pass |

---

## Part H — What this pass did *not* do

Stated plainly so the record is honest:

1. **No probability was generated or published.** Track B remains at Stage S0. The ESPN lane is a *research* lane; approving it for feature use requires your explicit S1 authorisation. **This is the single highest-leverage decision now available**, because the ESPN endpoints are the first source in this repository plausibly capable of clearing the `APPROVED FOR FEATURE` bar for identity, result, lineup and phase fields.
2. **No predictive-lift claim is made.** Every count in this document is descriptive. The 8/12 O/U figure, the 9 W / 8 L Rank #1 figure and the 7 W / 3 L Rank #2 figure are ledger entries, not calibration.
3. **`P-304` and `P-305` rows #2–#5 cannot be recovered.** They were never written to any file. They are recorded as `UNGRADABLE / ARCHIVAL_OMISSION` rather than reconstructed, because reconstructing them would be fabrication.
4. **Twelve evidence/definition follow-ups remain open** (`P-126`, `P-148`, `P-149`, `P-166`, `P-176`, `P-178`, `P-179`, `P-200`, `P-217`, `P-233`, `P-234`, `P-235`, plus the `P-274` conditional). The competitions are outside every structured source I could reach. `G36.1` provides the route to close the *operator-terms* subset (`P-166`, `P-200`, `P-217`, `P-274`) under standard rules; I have flagged them rather than unilaterally regrading historical settlements.
5. **The three new ordering-affecting controls are candidates, not promoted weights**, exactly as `LEARNING_REGISTER.md` §5 requires. Their disclosures are mandatory now; their ordinal force waits on a frozen prospective test.
6. **The consolidation pass proposed in D.3(1) was not performed** — merging five dated amendment sections into the numbered gates is a large edit to a controlling document and should be your decision.

---

## Part I — Cross-references

- Settlement detail and ledger: [`PREDICTION_LOG_COMBINED_2.md`](PREDICTION_LOG_COMBINED_2.md) § *2026-09-06*
- Full status list P-001 → P-305 with temporary IDs: [`GAME_LOG_STATUS_INDEX_2026-09-05.md`](GAME_LOG_STATUS_INDEX_2026-09-05.md) § *2026-09-06 addendum*
- Compact settled/unsettled ledger from `P-001` with the temporary-ID register: [`GAME_LOG_LEDGER_2026-09-06.md`](GAME_LOG_LEDGER_2026-09-06.md)
- Lessons and prospective tests: [`LEARNING_REGISTER.md`](LEARNING_REGISTER.md) `L-079`–`L-086`
- Source lanes: [`DATA_SOURCE_REGISTER.md`](DATA_SOURCE_REGISTER.md) § *September 6*
- Archived mini log: [`archive/PREDICTION_MINI_LOG_12_P304_P305_SETTLED_2026-09-06.md`](archive/PREDICTION_MINI_LOG_12_P304_P305_SETTLED_2026-09-06.md)
- Change log: [`AUDIT_CHANGELOG_2026-09-06.md`](AUDIT_CHANGELOG_2026-09-06.md)
