# Prediction mini log 12 — `P-304` / `P-305` settlement and evidence-gap closure

**Status:** `ARCHIVED COMPONENT — SETTLEMENT PASS`
**Pass date:** 2026-09-06 Australia/Sydney
**Canonical authority:** `PREDICTION_LOG_COMBINED_2.md` (its top snapshot controls queue state and next ID; this file does not)
**Method at settlement:** `MDS-2026.09.06-v3.7 — SPORTS_ONLY / MARKET_BLIND`
**Executable process:** `GFA-2` (as amended this pass) + relevant `SFA-<SPORT>`
**Numerical state:** `NTS-2026.09.02-v0.3 — Stage 0 all-sports design / pre-fit`
**Probability state:** `NOT_GENERATED / NOT_PUBLISHED — VALIDATION PENDING`
**Value state:** `NO VALUE DETERMINABLE`
**Next canonical forecast ID (unchanged by this pass):** `P-306`

> This is a **settlement/retrospective component**, not an issuance component. No new forecast was issued in this pass. It is filed in `archive/` per the user's standing instruction that the running mini log be archived here.

---

## 1. What this pass settled

| ID | Event | Prior status | New status |
|---|---|---|---|
| `P-304` | SK Slavia Praha vs FC Zbrojovka Brno — Chance Liga R7 | `DEFERRED — live at first check` | **`FINAL / SETTLED`** |
| `P-305` | Dublin Guardians vs Amsterdam Flames — ETPL Match 15 | `DEFERRED — live at first check` | **`FINAL / SETTLED`** |
| `P-300` | Rotterdam Dockers vs Edinburgh Castle Rockers — ETPL M14 | `FINAL / PARTIAL` — powerplay rows `EVIDENCE GAP` | **`FINAL / SETTLED`** — powerplay rows closed |
| `P-302` | Newcastle United vs AFC Bournemouth — EPL MW3 | `FINAL / PARTIAL` — corners row `EVIDENCE GAP` | **`FINAL / SETTLED`** — corners row closed |
| `P-273` | Palermo vs Mantova — Coppa Italia R32 | `FINAL / RESEARCH SETTLED` — corners provisional | **`FINAL / SETTLED`** — corners confirmed |
| `P-151` | Boca Juniors vs Lanús — Liga Profesional Fecha 7 | `FINAL / PARTIAL` — corners strong provisional | **`FINAL / SETTLED`** — corners confirmed |

---

## 2. `P-304` — SK Slavia Praha vs FC Zbrojovka Brno

**Frozen card fields (as issued, unaltered):** `PREGAME`, cutoff `2026-09-05 22:53:47 AEST / 14:53:47 CEST`; Rank #1 `1st Half Over 0.5 goals`; potential winner `SK Slavia Praha`.

**Live-state history.** At the 2026-09-05(b) settlement check this fixture was confirmed genuinely in progress (0-0, first half) across two independent Czech-language live sources plus a Sofascore fetch, and was correctly deferred rather than settled. That deferral was the right call and is recorded as compliant process.

**Official result.** **Slavia Praha 4 – 0 Zbrojovka Brno.** Half-time **1-0**.

| Min | Scorer | Note |
|---:|---|---|
| 38' | Tomáš Chorý | Penalty; disputed by the Zbrojovka coach post-match |
| 65' | Tomáš Chorý | |
| 76' | Emmanuel Ayaosi | **Substitute** — introduced 26' as a forced injury replacement for Provod |
| 88' | David Jurásek | **Substitute** — introduced 63' |

**Participants.**
- Slavia XI: Markovič — Konečný, Zima, Chaloupek — Isife, Sadílek, Nowak, Kubiak — Šturm, Provod — Chorý. Oscar Kubiak debut.
- Zbrojovka XI: Hrdina — Klíma, Hunal, Kaká — Penxa, Langer, Čavoš, Dante — Vachoušek, Vaníček — Vašulín.
- Forced substitutions: Zima off 20' (Vlček on); Provod off 26' (Ayaosi on).
- Head coaches: **Jindřich Trpišovský** (Slavia) · **Martin Svědík** (Zbrojovka).
- Referee: **Jan Beneš**.

**Settlement.**

| Rank | Frozen contract | Outcome |
|---:|---|---|
| 1 | `1st Half Over 0.5 goals` | **WIN** (38' penalty) |
| 2–5 | **Not reproduced in any archived file** | **`UNGRADABLE / ARCHIVAL_OMISSION`** |
| — | Potential winner `SK Slavia Praha` | **CORRECT** |

**Sources.** ČTK / [ceskenoviny.cz match report](https://www.ceskenoviny.cz/zpravy/slavia-v-primem-souboji-o-prvni-misto-v-lize-rozdrtila-zbrojovku/2870539) (FT, HT, scorers, both XIs, substitution minutes); [iSport.cz progressive live-blog headline sequence on the identical article URL](https://isport.blesk.cz/clanek/fotbal-chance-liga/479501/online-slavia-zbrojovka-4-0-debakl-ctvrtou-branku-pridal-jurasek-dve-zraneni-opor.html) — `0:0` → `1:0. Chorý proměnil penaltu!` → `3:0` → `4:0`, independently establishing that the only first-half goal was the 38th-minute penalty. Both sources are native-language, satisfying the `v3.4` requirement.

---

## 3. `P-305` — Dublin Guardians vs Amsterdam Flames

**Frozen card fields (as issued, unaltered):** `PREGAME`, cutoff `2026-09-05 23:14:43 AEST / 15:14:43 CEST`, toss not published at freeze; Rank #1 `Flames Powerplay Over 51.5 — conditional on Flames batting first`; potential winner `Amsterdam Flames`.

**Toss.** `Dublin Guardians , elected to field first` → **Amsterdam Flames batted first. The Rank #1 precondition was met.**

**Official result.** **Amsterdam Flames 169/7 (20 ov) beat Dublin Guardians 160/8 (20 ov) by 9 runs.** Venue Sportpark Westvliet, The Hague. Player of the match Tim Pringle (3/22).

| Innings | Powerplay (0.1–6.0) | Final |
|---|---|---|
| Amsterdam Flames | **60 runs, 1 wicket** | 169/7 (20 ov) |
| Dublin Guardians | 69 runs, 1 wicket | 160/8 (20 ov, target 170) |

Fall of wickets (Amsterdam): 1-39 (Samra, 2.4), 2-73 (de Leede, 7.4), 3-93 (Smith, 10.4), 4-109 (Bracewell, 12.6), 5-118 (Edwards, 15.1), 6-137 (David, 16.6), 7-167 (Campher, 19.5) — one wicket down at the six-over mark, arithmetically consistent with the 60/1 powerplay note.

**Playing elevens.**
- Amsterdam Flames: Samra, Smith, de Leede, David, Bracewell, Edwards (c), Campher, Neill, Pringle, Dutt, Gleeson.
- Dublin Guardians: Vince, Mitchell, Tector, Krishnamurthi, Dockrell, Shankar, Ashwin, Croes, Hollard, Little, Young.

**Settlement.**

| Rank | Frozen contract | Outcome |
|---:|---|---|
| 1 | `Flames Powerplay Over 51.5` (cond. Flames bat first) | **Condition MET → WIN** (60 runs) |
| 2–5 | **Not reproduced in any archived file** | **`UNGRADABLE / ARCHIVAL_OMISSION`** |
| — | Potential winner `Amsterdam Flames` | **CORRECT** |

**Sources — three independent endpoints in agreement.**
1. `site.api.espn.com/apis/site/v2/sports/cricket/1547871/summary?event=1547886` → `notes[]` contains the literal `Powerplay 1: Overs 0.1 - 6.0 (Mandatory - 60 runs, 1 wicket)` and `toss: "Dublin Guardians , elected to field first"`.
2. `site.api.espn.com/apis/site/v2/sports/cricket/1547871/scoreboard?dates=20260905` → Amsterdam `169/7` `winner:true`; Dublin `160/8 (20 ov, target 170)`.
3. [ESPNcricinfo full scorecard](https://www.cricinfo.com/series/european-t20-premier-league-2026-1547871/dublin-guardians-vs-amsterdam-flames-15th-match-1547886/full-scorecard) and its over-comparison view.

**Source contamination warning recorded against this card.** A web search for this fixture returned `sportscafe.in`'s *"AI Simulation | DLG vs AMF | Dublin Clinch Six-Run Thriller"* — a fully fabricated report claiming **Dublin 176/7 beat Amsterdam 170/7 by six runs**, with James Vince as a 54-run player of the match at "Sportpark Duivesteijn". Every load-bearing field, including the winner, was wrong. See `L-079`.

---

## 4. Evidence-gap closures

### 4.1 `P-300` powerplay rows — CLOSED

`site.api.espn.com/apis/site/v2/sports/cricket/1547871/summary?event=1547885` → `toss: "Rotterdam Dockers , elected to field first"`; `Powerplay 1: Overs 0.1 - 6.0 (Mandatory - 28 runs, 3 wickets)` for the Edinburgh Castle Rockers innings, `37 runs, 4 wickets` for Rotterdam.

| Rank | Frozen contract | Outcome |
|---:|---|---|
| 1 | `ECR Powerplay Over 50.5` (cond. ECR bat first) | Condition MET → **LOSS** (28 runs) |
| 2 | `20-over Under 168.5` | **WIN** (148) — unchanged |
| 3 | `20-over Over 168.5` | **LOSS** — unchanged |
| 4 | `ECR Powerplay Under 50.5` | **WIN** |
| — | Potential winner `Edinburgh Castle Rockers` | **CORRECT** — unchanged |

Cross-check: ESPNcricinfo fall of wickets has ECR 3 down by 2.6 ov and the 4th wicket at 8.4 ov, so exactly 3 down at the six-over mark. Consistent.

### 4.2 `P-302-C01` Bournemouth corners — CLOSED

`site.api.espn.com/apis/site/v2/sports/soccer/eng.1/summary?event=401879286` → `boxscore.teams[].statistics.wonCorners`: **Newcastle United 4, AFC Bournemouth 3**. Supporting profile: Bournemouth 17 total shots (7 blocked), 5 on target, 42.7% possession, xG ~1.5.

| Rank | Frozen contract | Outcome |
|---:|---|---|
| 1 | `Bournemouth Over 2.5 team corners` | **WIN** (3) |
| 2 | `1st Half Over 0.5` | **WIN** — unchanged |
| 3 | `FT Over 2.5` | **WIN** — unchanged |
| 4/5 | `FT Under 2.5` / `1H Under 0.5` | **LOSS** — unchanged |
| — | Potential winner `Newcastle United` (slight lean) | **WRONG (drew 2-2)** — unchanged |

### 4.3 `P-273` Palermo corners — CLOSED

`.../soccer/ita.coppa_italia/summary?event=401911809` → **Palermo 3 corners, Mantova 2**; Palermo 13 shots, 43.3% possession; final Palermo 5-2. Confirms the previously provisional figure from two specialist feeds. `Palermo Over 4.5 team corners` → **LOSS** (unchanged outcome, now non-provisional).

### 4.4 `P-151` Boca corners — CLOSED

`.../soccer/arg.1/summary?event=401841527` → **Boca Juniors 11 corners, Lanús 3**; Boca 19 shots; final Boca 1-0. Confirms the previously specialist-only 11–3 figure from an independent field-owner-grade source. `Boca Over 4.5 team corners` → **WIN** (unchanged outcome, now non-provisional).

---

## 5. Gaps that could not be closed, and exactly why

ESPN league-slug probes returned HTTP 400 (competition not carried) for every remaining corners follow-up:

| Card | Competition | Slugs tested |
|---|---|---|
| `P-148` | Liga MX Femenil | `mex.w.1`, `mex.femenil`, `mex.liga_mx_femenil` |
| `P-149` | MLS NEXT Pro | `usa.nextpro`, `usa.mlsnp`, `usa.nps`, `usa.mls.next_pro` |
| `P-176`, `P-178`, `P-179` | Championnat National (FRA tier 3) | `fra.3`, `fra.national` |
| `P-233`, `P-234`, `P-235` | China FA Cup | `chn.fa`, `chn.cup`, `chn.fa_cup` |

`api.sofascore.com` returned `403 Forbidden` on every route tested as an alternative. `P-126` is blocked by an identity/state conflict, not a missing corner field.

`P-166`, `P-200`, `P-217` and `P-274` are **contract-terms** questions, not sourcing gaps — no operator terms were ever supplied. New gate `G36.1` provides the route to grade them under stated standard rules; that regrade is flagged for the next pass rather than applied unilaterally to historical settlements here.

---

## 6. Updated cohort ledger (descriptive only — not a calibration claim)

Cohort = `P-288`, `P-290`–`P-305` (17 events).

| Measure | Value |
|---|---|
| Rank #1 resolvable rows | **17** |
| Rank #1 | **9 WIN / 8 LOSS** |
| Rank #2 (where a distinct #2 exists on record; `P-304`/`P-305` excluded — archival omission) | **7 WIN / 3 LOSS** |
| Both top two simultaneously correct | **3 of 10** (`P-296`, `P-302`, `P-303`) |
| Both top two simultaneously wrong | **2 of 10** (`P-295`, `P-299`) |
| Cards (of the twelve new ones) with at least one ranked O/U row winning | **8 of 12** |
| Ranked Over rows | **4 W / 1 L** |
| Ranked Under rows | **5 W / 4 L** |

Rank #1 WINs: `P-290`, `P-291`, `P-293`, `P-296`, `P-297`, `P-302`, `P-303`, `P-304`, `P-305`.
Rank #1 LOSSes: `P-288`, `P-292`, `P-294`, `P-295`, `P-298`, `P-299`, `P-300`, `P-301`.

Forced complementary pairs mean raw row counts overstate information content (`L-055`). No calibration, edge, ROI or model-validation claim is made from these numbers.

---

## 7. Adopted rule changes arising from this pass

`L-079` synthetic-content settlement prohibition · `L-080` structured-API-first acquisition rung · `L-081` corners settlement-coverage test (narrows and supersedes `L-073`) · `L-082` coaching/bench/rotation record · `L-083` bimodal phase-total treatment · `L-084` aggregate upper-tail budget (candidate) · `L-085` total-row path geometry (candidate) · `L-086` archival completeness for unsettled cards.

Full wording: `LEARNING_REGISTER.md`. Algorithm text: `RULES_GENERAL.md` §11 and each `RULES_<SPORT>.md` "September 6" section. Full narrative: [`IMPROVEMENT_PLAN_2026-09-06.md`](../IMPROVEMENT_PLAN_2026-09-06.md).

---

## 8. Archival-completeness declaration (new `G34.1`)

This component records, for every card it touches, the complete frozen slate **as it exists in the repository record**. Where a slate row was never written to any file — `P-304` rows #2–#5 and `P-305` rows #2–#5 — that fact is stated as `UNGRADABLE / ARCHIVAL_OMISSION` rather than reconstructed. Reconstructing an unrecorded frozen row from memory or inference would be fabrication and is prohibited.

The defect originated in the 2026-09-05(b) archival of `prediction logs/PREDICTION_MINI_LOG_11_P294_P305.md`, which preserved only the mini-log's summary table while two of its cards were still unsettled. `G34.1` prevents recurrence.
