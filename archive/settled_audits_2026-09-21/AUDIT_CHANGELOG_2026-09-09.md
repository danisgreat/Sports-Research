# Audit changelog — 2026-09-09

**Pass type:** settlement + deep retrospective + cross-sport algorithm improvement + ledger completion. **No forecast was issued.** Method: `MDS-2026.09.06-v4.0` (unchanged — no method-version bump). Google Drive not touched; local repository only.

**Scope.** Reconcile the external running log `PREDICTION_MINI_RUNNING_LOG_P344_RETROSPECTIVE_UPDATED.md` (`P-333`–`P-344`) into the active canonical log, settle every finished event, complete deep retrospectives on every Rank-#1 loss, extract cross-sport learnings into the sport algorithms, answer the standing over/under directive with research rather than assertion, and make every unsettled row individually trackable.

---

## 1. Live-state check — the first required step

Every `P-333`–`P-344` event was checked for live status before anything else. All twelve were **final** (scheduled 2026-09-07 / 2026-09-08; pass run 2026-09-09). **No event required carrying forward as live.** Every final was then independently re-verified against a public source *outside* the mini-log's own register — ESPN, SI, WTA, FIBA/TSN, SBS English, Sportnet, Kawowo/GHANAsoccernet, ESPNcricinfo, matchcalendar.football — and all twelve confirmed.

## 2. Settlement

| | |
|---|---|
| Issued cards settled | **9** (`P-335`–`P-342`, `P-344`) — 2 partial on a derivative corner row |
| Administrative no-forecast closures | **3** (`P-333`, `P-334`, `P-343`) — start-crossing / `CR-P3` fail-closed, correct behaviour, non-scorable |
| Ranked rows settled | **20 W / 19 L** |
| Rank #1 | **6 W / 3 L** (`P-339`, `P-342`, `P-344` lost — all three received deep retrospectives) |
| Top two both won | **3 of 9** (`P-336`, `P-338`, `P-340`) |
| Potential winners | **8 / 9** (`P-337` the miss, a 0–0 draw) |
| Preferred full-match total O/U | **4 W / 5 L** |
| Arithmetic correction | `P-344` card mean Brier **0.2834 → 0.3334** (the mini-log's four per-row Brier values were correct; their stated mean was not). No row result changed. |

Running Brier after this cohort: mixed **72 rows, mean 0.2436** vs a 0.2500 trivial baseline; `PRIMARY_SCORED` **18 rows, mean 0.2466**, card count **4** of 25. The cohort's `EXPLORATORY` subset came in at **0.2665 — worse than baseline**, recorded rather than smoothed.

## 3. The finding that reorganised the whole pass

The first reading of this cohort diagnosed three separate weighting errors. Opening the underlying records showed **all three Rank-#1 losses were one retrieval failure**: an aggregate stood in for a disaggregated record that was available **from a source already listed in the card's own register**, and in every case the disaggregated record pointed the other way.

| Card | Aggregate used | Disaggregated record | What it showed |
|---|---|---|---|
| `P-339` | "Ryu 0–3, 7.31 ERA over 7 starts" | KBO official English player-page **game log** | `7 ER/3⅓ (2 BB) → 4 ER/6.0 (0 BB) → 0 ER/5.0, 7 K, 0 BB → 3 ER/5.0 (1 BB)`. Slump **front-loaded**, worst start three weeks old; most recent evidence a **scoreless 7-K start**; **command intact** (~1.2 BB/9; 17 BB in 125⅔ IP). A noisy-outcome slump, not skill decline. He threw 6.0 IP / 1 ER. |
| `P-335` | "4.1 innings at Triple-A El Paso" (innings only) | MLB/MiLB **rehab pitch-count ladder** | `14 → 47 → 64 pitches`, the last **4⅓ scoreless, 7 K, 44 strikes**. Forecasts a ~5-inning MLB ceiling. He threw **63 pitches / 5.0 scoreless** — directly contradicting the `+0.20` short-start Over adjustment. |
| `P-344` | "leaders include Juhász (17.0), Takács-Kiss (13.0), **Lelik** and Studer" | FIBA official **player profiles** | Lelik was Hungary's **third-highest scorer, 8.7 PPG (8/14/4), ~26.3 min**, 4.3 RPG, 3.5 APG — the only one of the top three carried without a number. **A blowout needs a third scorer; the margin distribution had none.** She scored 23. |

Promoted as **`G-L7` (`RULES_GENERAL.md` §16.5(c))**. Cheap, checkable, requires no new source, and would have touched all three losses — the highest-value output of the pass.

## 4. Rule changes — four disclosure/retrieval requirements, no fitted weight

All four are additions to `RULES_GENERAL.md` §16.5, of the same class as its original "show the arithmetic" rule. **No new numbered gate, no fitted coefficient, no ordinal bar** (`L-087` firewall; `G23.1` direct-marginal-likelihood ordering continues to govern).

| ID | Requirement | Origin |
|---|---|---|
| `G-L1` §16.5(a) | Enumerate outcome-state families with **explicit probability mass**; every current-evidence `G22` kill path becomes a **weighted branch**, not a prose sentence; write one representative Rank-#1 outcome in every other supplied row's settlement unit | `P-340` ("2–1 is an Under kill state" → finished 2–1), `P-342` ("1–0/2–0 control" → finished 0–2), `P-344`. Positive model: `P-338` |
| `G-L2` §16.5(b) | Unit-performance uncertainty is **distribution width** around the shrunk skill prior, not a signed total lean; a net signed adjustment needs a named *directional* mechanism | `P-335`, `P-339`, `P-342` — all three converted uncertainty into an Over lean, all three came Under |
| `G-L7` §16.5(c) | **Aggregate-to-disaggregate retrieval** (§3 above); otherwise `AGGREGATE_ONLY` and the dependent row cannot reach `LEAN`/`SUPPORTED` | All three Rank-#1 losses |
| `G-L8` §16.5(d) | **Total-probability coherence** — probability must be a monotone function of the row's own normalised edge `\|centre − line\| / width`, printed beside it | `P-335` had the largest edge (0.34) and the lowest probability (0.52); `P-336` the smallest (0.07) and nearly the highest (0.60) |

**Honest counter-check recorded against `G-L8`:** re-scoring the eight preferred-total rows at normal-CDF-coherent probabilities yields mean Brier **0.2614 vs the issued 0.2538** — on n=8, mechanical coherence would have been *slightly worse*. `G-L8` is justified on `METHOD.md` §5's "derived from" consistency grounds **only**, explicitly not as a demonstrated accuracy improvement.

Also carried: **`G-L3`** (tier/promotion translation) as a candidate-watch item; **`G-L4`/`G-L5`/`G-L6`** as reinforcements of existing controls.

## 5. Sport-file updates — all ten

Every sport file received a §"2026-09-09" section, including the five with no card in this cohort.

| File | Change |
|---|---|
| `RULES_BASEBALL.md` | **New controls 24–25** — the starter's game log outranks any multi-start aggregate (print IP/ER/SO/**BB** per start, state front/back-loaded and whether command held); a returning starter's workload ceiling comes from the **rehab pitch-count ladder**, not innings. Kill-path and §8.7 checklist additions |
| `RULES_BASKETBALL.md` | **New controls 20–21** — quantify **every top-three scorer and every ~20+-minute player** on both sides, a bare name in a "leaders include…" phrase is `AGGREGATE_ONLY`; secondary-scorer usage transfer in a mismatch, and a volatile perimeter offence's **floor is its worst recent same-regime games**, not its average. Kill-path and checklist additions |
| `RULES_SOCCER.md` | Measured centre-precision table (**mean signed error −0.20 goals, MAE 1.49**); three-cohort phase-vs-full-total record; `G-L7`/`G-L8` instantiation; control 20/27 reinforcement; §8.6 override 6; §8.7 item 18; four kill-path additions |
| `RULES_TENNIS.md` | Positive-model note — `P-338` is the template `G-L1` exports; `G-L2`/`G-L7`/`G-L8` instantiated (`G-L1` already satisfied by §4 and control 12) |
| `RULES_CRICKET.md` | Operational toss-handshake note (`CR-P3` worked as designed on `P-333`/`P-343`); four-control instantiation table; `P-333`'s printed L5 innings cited as a positive `G-L7` example |
| `RULES_AFL.md`, `RULES_AMERICAN_FOOTBALL.md`, `RULES_ICE_HOCKEY.md`, `RULES_NRL_RUGBY.md`, `RULES_RUGBY_UNION.md` | Sport-native instantiation of all four controls despite no card in the cohort — margin/total family enumeration in native scoring units, the sport's analogue of the rehab ladder (practice-participation ladder, goaltender per-start log, reserve-grade minutes, bench-minutes progression), and the quantised-scoring caveat on normalised edge |

## 6. Researched answer to the standing over/under directive

- **"At least one O/U row won" is discarded as a measure.** It was true on 9 of 9 cards here and is mechanically ~always true for complementary half-point pairs (`L-055`). This repository already caught itself reporting on that basis in the 2026-09-06(d) correction; the honest measure is **highest-ranked O/U selection accuracy** — 6/9 this cohort, 4/9 for the full-match total specifically.
- **The centres are unbiased but imprecise.** Soccer full-match goal centres: mean signed error **−0.20 goals**, **MAE 1.49 goals**, against stated widths of ±1.55–1.8 — so the widths were honest and there is **no directional correction to apply**. The supplied line sat only **0.05–0.50 goals** from the centre in every case; that is a coin flip no research converts into an edge.
- **The record supports ranking the total honestly rather than picking it better:** full-match total went **2/2 as Rank #1** (`P-336`, `P-337` — both persistent multi-window low-output `Under`s, and the two largest normalised edges) and **1/5 as Rank #2**.
- **First formal `CANDIDATE` opened — `C-PHASE-VS-FULL-TOTAL`**, on three cohorts of agreement (1H totals **8 W / 4 L** vs full-match soccer **8 W / 6 L**). Its manifest requires the advantage to **survive stratification by normalised edge** — the null being that phase rows merely carry larger edges. **Not an ordinal bar**, and explicitly forbidden meanwhile from promoting a phase row above a better-evidenced full-match row.
- **Standing constraint restated:** never promote an opposite pick solely to manufacture an O/U win.

## 7. Fresh settlement attempt on the two open derivative rows

The first pass declared both corner rows unsettleable without testing the framework's **primary** structured lane on those competitions — a `G10.2` gap, now closed. Method: direct `curl` to `site.api.espn.com` with `soccer/eng.1` as a positive control (HTTP 200).

| Probe | Result |
|---|---|
| `soccer/uga.1/scoreboard?dates=20260908` | **HTTP 200**, resolves as "Ugandan Premier League" — competition **is** carried |
| `uga.1` events on 2026-09-08, and across 2026-09-01→15 | **0 events** |
| `uga.1` season/calendar state | **season 2025, "2025-26", 97 calendar entries, newest event 2026-05-23** |
| 10 Slovak slug forms (`svk.1`, `svk.2`, `svk.cup`, `svk.slovnaft_cup`, `svk.slovak_cup`, `svk.slovakia_cup`, `svk.fortuna_liga`, `svk.super_liga`, `slk.1`, `slovak.1`) | **HTTP 400 on all ten** |
| `sports.core.api.espn.com/v2/sports/soccer/leagues?limit=1000` | 218 leagues (`count` = 218, complete). **No Slovak competition. No `uga.1` either.** Only sub-Saharan African entry: `rsa.1` |

**Two source-lane findings, both folded into `SOURCES.md` §2 and `DATA_SOURCE_REGISTER.md`:**

1. **`P-341-C03` is a season-rollover gap, not absent coverage** — which converts a vague "retry later" into a concrete retry trigger: re-query `uga.1` once the feed advances to 2026-27. The row correctly stays `UNSETTLEABLE` today.
2. **The ESPN core league directory is not authoritative for what the site API serves.** `uga.1` returns 200 on the site API while being absent from the 218-league directory; treating the directory as the coverage test would have wrongly written Uganda off. Use it only as corroboration — Slovakia fails **both** tests, which is why that non-coverage finding is solid.

Neither row's disposition changed: `P-341-C03` remains `UNSETTLEABLE`, `P-342-C03` remains `PROVISIONAL RESEARCH WIN`. No W/L or Brier booked for either (`G10.2`/`L-081`).

## 8. Ledger completion

- **`GAME_LOG_STATUS_INDEX_2026-09-05.md` extended `P-317` → `P-344`.** It is now the complete per-ID enumeration of every game log settled and yet to be settled, from `P-001`: 344 canonical records plus `LOCAL-GEELONG-20260904`.
- **New temporary-ID namespace `TMP-OPEN-<YYYYMMDD>-<seq>`**, defined in `EXTERNAL_LOGGING_WORKFLOW.md` alongside the existing `TMP-SETTLED-*`. The two solve opposite problems and must never be confused: `TMP-SETTLED-*` is an **ID collision on a settled event** (still never encountered); `TMP-OPEN-*` is an **unsettled row on a correctly-numbered event**. A handle is not a canonical ID, never enters the scorecard, carries a concrete retry trigger, and retires on settlement.
- **11 handles issued** — `-01`/`-02` for the two new `P-333`+ corner rows, `-03`…`-11` indexing the nine still-open Part-2 appendix rows **for visibility only; custody remains with Part 2.**
- **Part-2 appendix update (dated, non-destructive):** `P-178-C05` **`UNRESOLVED → PROVISIONAL LOSS`** (leballonrond + Forebet independently show Cannes 8 – Le Puy 8 = 16, defeating Under 10.5); `P-176-C05` strengthened (APWin/Football365/TotalCorner consistent at 5–3 = 8). Neither promoted to field-owner grade — the provider was never frozen. No new or temporary canonical ID.

## 9. New information sources

Field owners newly exercised: **Asian Cricket Council** (`asiancricket.org`), **FIBA game-center reports + player profiles**, **KBO Korean + `koreabaseball.com`** with **SBS English** as an accurate English rung (reinforces `L-067`). Research-only cross-check tier: **Kawowo Sports**, **GHANAsoccernet**, the **PlaymakerStats / zerozero / ceroacero / leballonrond** family, **Futbol24**, **Forebet**, **matchcalendar.football**, and **ESPN public web box scores** including the `fiba` route. Route-specific access note: `ceroacero.es`, `forebet.com` and `sofascore.com` match pages returned **HTTP 403** to `WebFetch` but were readable via search snippets. **None reaches `APPROVED FOR FEATURE`**; none upgraded a niche corner field.

## 10. Performance-eligibility carve-out

Per current user directive — which outranks standing policy under `METHOD.md` §9 — the `P-333`–`P-344` cohort is **learning-only, not performance-eligible evidence**. Its rows are folded into the running scorecard for ledger continuity, but **no accuracy, calibration, discrimination or improvement verdict may be drawn from them**. Recorded in `PERFORMANCE_ELIGIBILITY_POLICY.md` §"2026-09-09", `PREDICTION_LOG_COMBINED_3.md`'s snapshot and `METHOD.md`. `EP-2026.09.06-v2` is otherwise unchanged for all other cohorts.

## 11. Files changed

**Updated:** `PREDICTION_LOG_COMBINED_3.md` (settlement section, deep retrospectives, over/under research, open queue with tracking IDs, snapshot, Brier scorecard), `PREDICTION_LOG_COMBINED_2.md` (dated appendix update), `RULES_GENERAL.md` (§§16.5(a)–(d) + dated section), `METHOD.md` (§4 item 7 + dated addendum), `CONTROLS.md`, `LEARNING_REGISTER.md` (dated disposition + `C-PHASE-VS-FULL-TOTAL` manifest), `SOURCES.md`, `DATA_SOURCE_REGISTER.md`, `PERFORMANCE_ELIGIBILITY_POLICY.md`, `EXTERNAL_LOGGING_WORKFLOW.md`, `GAME_LOG_STATUS_INDEX_2026-09-05.md`, `README.md`, and all ten `RULES_<SPORT>.md` files.

**New:** `archive/mini_logs/PREDICTION_MINI_RUNNING_LOG_P344.md` (byte-preserved component with a provenance note recording that it arrived as an inline attachment, so a fresh hash will not match an original), and this changelog.

**Unchanged:** every issued rank, probability, target, source set, cutoff and participant state. No settled contract outcome was altered. No probability was minted retroactively. No method-version bump.
