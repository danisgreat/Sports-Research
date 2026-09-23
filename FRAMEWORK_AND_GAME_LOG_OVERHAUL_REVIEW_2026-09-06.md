# Comprehensive game-log and framework overhaul review — 2026-09-06

> **Implemented in full the same day.** Every recommendation below was carried out. See `AUDIT_CHANGELOG_2026-09-06_OVERHAUL.md` for the complete implementation record, `METHOD.md`/`CONTROLS.md`/`SOURCES.md`/`NUMERICAL_PROGRAM.md` for the new primary documents, and `PREDICTION_LOG_COMBINED_2.md` §"2026-09-06(e)" for the `P-306`–`P-317` ledger reconciliation this review's Finding 3 identified. This document is preserved unedited below as the original findings record — it is evidence, not an updated live status.

Status: **REVIEW DOCUMENT (ORIGINAL, UNEDITED) — findings and recommendations; see the implementation record above for what was done with them.**

Scope: every canonical record from `P-001` to `P-317`, all 38 root-level Markdown documents, the 18 component logs in `prediction logs/`, and the two independently supplied 2026-09-06 blind-spot reviews.

Figures marked **[recomputed]** were derived in this pass from the log text. Figures marked **[quoted]** are the framework's own recorded numbers, reproduced so they can be checked.

---

## 0. Headline verdict

The framework is an outstanding **audit and honesty system** and a **failing forecasting system**. Those are separable, and conflating them is the single biggest reason the problem has persisted.

Three findings dominate everything else in this document.

**Finding 1 — The ranking has no demonstrated discriminative power, and the framework's own numbers show it.** Across every cohort that recorded rank-level outcomes, Rank #1 wins about **59.2%** of the time [recomputed] — but Rank #4, the slot the rules explicitly forbid treating as a fade, wins at a statistically indistinguishable rate and in several cohorts wins *more often* than Rank #1. In the most recent matched 15-card cohort, Rank #1 went **7-8 (46.7%)** while Rank #2 went **10-5 (66.7%)** [quoted]. The ordinal ranking — the framework's primary output, and the object of hundreds of pages of governance — is not currently distinguishable from noise.

**Finding 2 — The mandatory process is not executed, and execution is getting worse as the rulebook grows.** The 28-line mandatory card checklist (`RULES_GENERAL.md` §11.9) is satisfied at rates between 0% and 28% depending on the item, measured across 238 parsed card blocks [recomputed]. The full L5/L10/L15/L20 retrieval that `G13.1` calls "mandatory" appears on 26% of cards in the oldest log, 9% in the active log, and **0% in the newest log**. Component-budget arithmetic — mandatory for every aggregate line since v3.0 — appears on 3%. `REFERENCE_BASE_RATE`, mandatory for every supplied contract, appears on **1 of 238 cards**. The rules are not being broken through carelessness; there is more mandatory process than any single session can physically perform.

**Finding 3 — Twelve issued forecasts are off the books entirely.** `P-306` through `P-317` exist only in `PREDICTION_MINI_RUNNING_LOG_P317.md`. They appear in no canonical log, no status index, no ledger, and no README. All 24 cards in that file are marked `UNSETTLED`, several for events that finished over a day ago — while the controlling snapshot of the active log states *"Nothing is `DEFERRED` — no event in the log is awaiting a result."* That statement is false, and the file that falsifies it is the most recently modified file in the repository.

The rest of this document supports these three findings and sets out what to do.

---

## 1. What I did

1. Read the complete active rule set: `AGENT_ROLE_AND_TASK.md`, `RULES_GENERAL.md` (all 15 sections, 48 gates, the `GFA-2` algorithm, the 28-line card checklist), `README.md`, `MODEL_AND_DATA_SPEC.md`, `UPCOMING_GAME_RESEARCH_GUIDE.md`, `LEARNING_REGISTER.md`, `DATA_SOURCE_REGISTER.md`, `IMPROVEMENT_PLAN_2026-09-06.md`, `PERFORMANCE_ELIGIBILITY_POLICY.md`, and the sport-file pattern via `RULES_BASEBALL.md`.
2. Indexed and parsed all three prediction logs into **238 individual card blocks** and ran automated gate-compliance measurement against the mandatory checklist.
3. Extracted every recorded cohort performance ledger from `P-001` to `P-305` and assembled them into the all-history aggregate that the framework repeatedly notes has never been computed.
4. Independently re-derived the rank-by-outcome distribution from the one fully explicit settlement matrix in the corpus (`P-103`–`P-123`), and cross-checked it against the recorded cohort figures.
5. Deep-read individual cards spanning the whole history: the first settled card (`P-001`), mid-era cards, the `P-294`–`P-305` cohort, and every one of the never-audited `P-306`–`P-317` cards.
6. Ran an internal-consistency audit across the active document set — version declarations, gate vocabulary, cross-references to withdrawn gates, ledger reconciliation.

---

## 2. The empirical record — what 317 cards actually show

### 2.1 The all-history Rank #1 aggregate, computed for the first time

`README.md` states that the all-history recomputation "is a mechanical aggregation task, not yet performed." Here it is, assembled from the framework's own recorded cohort ledgers, with overlapping cohorts resolved so no event is double-counted.

| Cohort | Events | Rank #1 W-L | Rate |
|---|---:|---:|---:|
| `P-001`–`P-060` | 59 | *no rank-level ledger kept* | — |
| `P-061`–`P-063` | 3 | 3-0 | 100.0% |
| `P-064`–`P-087` (clean 20) | 20 | 14-6 | 70.0% |
| `P-088`–`P-099` | 12 | 8-4 | 66.7% |
| `P-103`–`P-123` | 21 | 14-7 | 66.7% |
| `P-124`–`P-136` | 10 | 6-4 | 60.0% |
| `P-137`–`P-163` | 26 | 16-10 | 61.5% |
| `P-165`–`P-186` | 22 | 14-8 | 63.6% |
| `P-187`–`P-214` | 27 | 12-15 | **44.4%** |
| `P-215`–`P-238` | 24 | 11-9 | 55.0% |
| `P-239`–`P-248` (excl. 241–243) | 6 | 5-1 | 83.3% |
| `P-241`–`P-243`, `P-250`–`P-267` | 21 | 13-8 | 61.9% |
| `P-268`–`P-271` | 3 | 2-1 | 66.7% |
| `P-272`–`P-279` | 7 | 3-4 | **42.9%** |
| `P-280`–`P-287`, `P-289` | 10 | 4-6 | **40.0%** |
| `P-288`, `P-290`–`P-305` | 15 | 7-8 | **46.7%** |
| **TOTAL (non-overlapping)** | **227** | **132-91** | **59.2%** |

*(`P-001`–`P-060` kept no Rank #1 ledger; its closest analogue is "higher-ranked exact pairs 24/36 = 66.7%". All cohort rows [quoted]; the total is [recomputed]. 227 events carry a Rank #1 row; **223** of those reached a definite WIN/LOSS grade — the 4-event difference is the provisional and unresolved rows in the `P-215`–`P-238` cohort. The 59.2% is 132/223 definite grades.)*

**Read this table by time, not by total.** The first two-thirds of the history runs 60–70%. The last four cohorts — 35 events under methods v3.3 through v3.7, the most heavily governed cards ever produced — run **42.9%, 40.0%, 46.7%**, with a 44.4% patch earlier at `P-187`–`P-214`. The last 32 consecutive events give Rank #1 at **14-18 (43.8%)** [recomputed].

That is the opposite of what a maturing method should do. Either the early figures were flattered by favourable slate geometry and event selection, or the accumulating rulebook is actively degrading the forecast. Both are plausible; §5 argues both are true.

### 2.2 The ordinal ranking does not order anything

I re-derived the full rank-by-outcome distribution from the `P-103`–`P-123` settlement matrix — the only place in the corpus where all four ranks are recorded per card in machine-readable form [recomputed]:

| Rank | W-L | Rate |
|---|---:|---:|
| Rank 1 | 14-7 | 66.7% |
| Rank 2 | 12-9 | 57.1% |
| Rank 3 | 11-10 | 52.4% |
| **Rank 4** | **12-4** | **75.0%** |

A broader automated parse of every settlement-style table row across all three logs (177 rows) gives Rank 1 67.4%, Rank 2 51.2%, Rank 3 65.0%, **Rank 4 69.2%** [recomputed]. The framework's own earlier audits found the same thing and said so plainly — *"rank #2 won 50%, below the observed rank #3/#4 win counts"* and *"demonstrates why rank #4 cannot be treated as a fade"* [quoted].

Four of the 21 cards in that matrix (`P-114`, `P-115`, `P-116`, `P-122`) settled as **`LLWW`** — perfectly inverted, both top rows losing and both bottom rows winning. At ~19% that is not a tail; it is a mode.

**The implication needs stating directly.** `RULES_GENERAL.md` §11.6 requires a unique ordinal for every row, and `G27` forbids using rank-4 history as a fade prior — a prohibition that is correct as an anti-superstition rule, but which has had the side effect of preventing anyone noticing that the bottom slot outperforms. The entire apparatus of `G23` robustness records, `G23.1` marginal-likelihood comparison, `G24` extra-condition audits, `G25`/`G25.1` coherence gates, `G26`/`G26.1` top-row tests and `G27` swap tests exists to produce an ordering that, over 223 events, does not order.

### 2.3 The contract-row ledger is mathematically incapable of measuring anything

The framework reports raw contract ledgers everywhere — "58 WIN / 51 LOSS", "54 WIN / 42 LOSS", "20 WIN / 20 LOSS". These are the most-quoted numbers in the repository and they are **structurally pinned near 50% regardless of forecast quality**.

The active log admits this in exactly one place: *"The new 40-row cohort has 20 WIN and 20 LOSS, **mechanically forced by two complementary pairs per card** on these completed half-point endpoints"* [quoted]. A typical slate is `Under X / Team A −Y / Team B +Y / Over X`. Exactly one of each pair wins. Four rows, two wins, always, whatever the analyst does.

My parse of the `P-103`–`P-123` matrix confirms it: **10 of 21 cards settled at exactly 2 wins**, mean 2.33 wins per card [recomputed]. The excess above 2.0 comes entirely from cards whose supplied slate happened not to be two clean complements.

Every raw-row ledger in the corpus should be deleted or relabelled as slate geometry. They have consumed enormous audit effort while carrying close to zero information.

### 2.4 The system is spread far too thin to ever be measurable

Classifying the 305 indexed records by sport [recomputed, approximate]: Baseball ~29%, Soccer ~17%+ (much of the ~22% unclassified residue is also soccer), Cricket ~13%, AFL/AFLW ~6%, Tennis ~4%, Basketball ~3%, Rugby league ~3%, American football ~2%, plus ice hockey and rugby union.

That is ~11 sports across an estimated 60+ distinct competitions in 317 events. `LEAGUE_RULES_SOCCER.md` alone documents **about 35 soccer competitions**. The largest single homogeneous population in the entire history is MLB, at perhaps 50–60 events.

**No population in this repository has enough events to fit, validate, or even reliably measure anything.** `README.md`'s Track B correctly says the numerical program needs "hundreds of eligible events per population at minimum." At the current rate of a new sport-competition every few cards, that threshold will never be reached for any population. This is the largest structural obstacle to the stated goal, and no rule in the framework addresses it.

### 2.5 Where the Over/Under objective actually stands

The `2026-09-06(d)` review's recomputation, which I verified against the underlying settlement table, gives for the 12 newest settled cards: **highest-ranked O/U selection 7 W / 5 L**, all available total rows 14 W / 12 L [quoted, verified]. The earlier "at least one ranked O/U row won in 8 of 12" framing in `IMPROVEMENT_PLAN_2026-09-06.md` is coverage, not skill — with complementary pairs supplied, "at least one won" is near-automatic and tends toward 12/12.

The honest reading: **on totals, the system is at a coin flip.**

---

## 3. The compliance collapse — measured

I parsed all three logs into card blocks (238 blocks over 1.5 KB) and tested each against the mandatory checklist. This has never been measured before. All figures [recomputed].

| Mandatory item (gate) | `P-001`–`P-271` | `P-272`–`P-305` | `P-294`–`P-317` |
|---|---:|---:|---:|
| `REFERENCE_BASE_RATE` for every contract (`G12.1`, chk 3) | **0.5%** | 0% | 0% |
| Full L5+L10+L15+L20 retrieval (`G13.1`, chk 6) | 26% | 9% | **0%** |
| Component-budget arithmetic (`G20`, chk 11) | **3%** | 0% | 0% |
| Separation-budget arithmetic (`G20.1`, chk 12) | 0% | 14% | 9% |
| Swap test on the bottom row (`G27`, chk 18) | 18% | **0%** | **0%** |
| Bidirectional-sign audit (`G22`, chk 13) | 2% | 9% | 17% |
| Slate geometry disclosure (`G4.1`, chk 2) | 28% | 5% | **0%** |
| Named head coach (`G14.2`, chk 25) | 13% | 14% | **4%** |
| Bench / rotation record (`G14.2`, chk 25) | 0% | 5% | **0%** |
| Hourly venue-coordinate forecast (`G15.1`) | 14% | 9% | **4%** |
| Dew point — a mandatory weather field (§11.3C) | 3% | 0% | 0% |
| Wind resolved to a direction, not a speed (§11.3C) | 7% | 9% | 17% |
| Any exact URL in the source register (`G8`) | 42% | 68% | 65% |
| `rank_gap` ordering strength (`G23`) | 0% | 0% | 0% |
| Settlement-source pre-registration (`G10.2`, chk 24) | 0% | 5% | 0% |
| Aggregate tail budget (`G20.2`, chk 26) | 0% | 5% | 0% |
| Path geometry (`G21.1`, chk 27) | 0% | 5% | 0% |
| Kill path named (`G19`/`G23`) | 74% | 91% | 87% |
| Some weather content present | 93% | 100% | 96% |

Three things follow.

**3.1 The `GATE-ENVIRONMENT` hard gate has been failed on roughly 90% of outdoor cards, and the cards were issued anyway.** §11.3C is unambiguous: an outdoor or open-roof event with no venue-coordinate hourly forecast records `WEATHER_NOT_AVAILABLE` and **"no actionable forecast or rank is issued."** Cards carry weather content 93–100% of the time but a qualified venue-coordinate hourly packet 4–14% of the time. `P-309` (Gardner-Webb @ Wofford) is typical: it cites a National Weather Service forecast *for Spartanburg* — a city forecast, which §11.3C explicitly says "does not satisfy this step" — with no hourly table, no wind vector, no dew point, and no near-start observation. It was then issued with a full four-row ranking and a Rank #1 full-game total.

**3.2 Gates adopted on 2026-09-06 have never once been executed.** `G20.2`, `G21.1`, `G10.2`, `G14.2` and `rank_gap` appear on at most one card each, and on **zero** of the twelve cards issued *after* they were adopted. All of `P-306`–`P-317` were written against `MDS-2026.09.05-v3.6` — three method versions stale — which is precisely the `G0` `GATE-READ` failure the framework created after catching `P-268`/`P-270`/`P-271` doing the same thing. **The control did not prevent its own recurrence.**

**3.3 The cause is arithmetic, not attitude.** The `G0`/§1 mandatory pre-research read is:

| File | Bytes |
|---|---:|
| `AGENT_ROLE_AND_TASK.md` | 18,265 |
| `RULES_GENERAL.md` | 135,947 |
| `MODEL_AND_DATA_SPEC.md` | 59,594 |
| `ALGORITHM_PORTFOLIO_AND_EVALUATION.md` | 46,676 |
| `NUMERICAL_TRAINING_SPEC.md` | 26,539 |
| `UPCOMING_GAME_RESEARCH_GUIDE.md` | 45,153 |
| `LEARNING_REGISTER.md` | 176,761 |
| one sport file (`RULES_BASEBALL.md`) | 61,323 |
| **Total** | **570,258 (~143,000 tokens)** |

Plus `DATA_SOURCE_REGISTER.md` (95 KB), the active log's controlling snapshot, and "the newest relevant same-sport retrospectives" — roughly **165,000 tokens of mandatory reading before a single stats source may be opened**, on every card, followed by 28 checklist lines plus 10+ sport-specific pre-issue items. Then the actual research. Then the ranking.

A process this expensive is not skipped through negligence. It is skipped because it cannot be completed, and what gets skipped is whatever is least visible in the output — which is exactly the analytical work (budgets, base rates, recency windows, swap tests) rather than the ceremonial work (declarations, disclaimers, source lists).

---

## 4. What is genuinely right — and must survive any overhaul

This is not a bad system. Several things in it are better than most professional practice and should be protected.

1. **The honesty boundary has held for 317 events.** No fabricated probability, no invented ROI, no claimed edge, no "lock." When the framework does not know something, it says so. Across a corpus this size that is genuinely rare, and it is the reason the record is diagnosable at all.
2. **Outcome and process are separated, and the separation is real.** `P-085` had two winning top rows and was still correctly rejected because the live input state was impossible. `G37.1`'s two-pass result-blind grading is the right design.
3. **Identity and contract discipline is excellent.** Target-versus-threshold separation, push-mass preservation, Asian quarter-line splitting into child contracts, alias mapping, `SETTLED_AT_ISSUE` handling. These are the things most amateur systems get wrong and this one gets right.
4. **The self-correction record is exceptional.** `L-073` was promoted on a stated empirical premise, that premise was tested the next day, found false, and the control was narrowed with the falsifying evidence recorded. The `2026-09-06(d)` review then caught the framework doing the *same thing to itself* with `G20.2`/`G21.1`/`G26.1` and withdrew all three. Very few systems audit their own same-day work this hard.
5. **The synthetic-content exclusion (`L-079`) is a first-rate catch.** An AI-generated match report with the wrong winner, ranked alongside real scorecards. That problem will only grow, and the rule — settle from scorecards, never narratives; a search summary is not a source — is exactly right.
6. **The structured keyless-endpoint lane (`G10.1`, ESPN site API) is the highest-value operational discovery in the repository.** It immediately closed four evidence gaps that had been open for weeks.
7. **The bench/coaching blindspot (`G14.2`) was correctly diagnosed.** `P-304` — two of four goals from substitutes, two starters lost inside 26 minutes — is a genuine, generalisable, under-modelled driver.
8. **Price independence is coherently reasoned.** The `L-100` clarification that `MARKET_BLIND` means price-blind, not market-independent (the supplied slate is itself a market object, so accuracy is conditional on thresholds the market chose), is a subtle and honest point most systems never reach.

**Every one of these is an integrity control. Not one is a forecasting improvement.** That asymmetry is the diagnosis.

---

## 5. What is wrong — structural defects

### 5.1 The governance inversion

The current apparatus: **48 gates**, **28 mandatory card lines**, **121 lessons**, **130 `PROMOTED_PROCESS` status entries**, **~1.4 MB of active rule text**. Against that: **2 lessons ever `RETIRED`**.

Rules only accumulate. There is a promotion pathway and effectively no retirement pathway. `L-096` (periodic control-effectiveness review) was added on 2026-09-06 and has never run.

The result is a system where compliance cost grows monotonically while accuracy declines, and where — critically — **no gate in the framework can ever be shown to have improved a forecast**, because every one is defined as a "validity, provenance or disclosure control" that explicitly "claims no predictive lift." §11.10 states it outright: *"Completing GFA-2 is not evidence of predictive lift."*

The framework has therefore built an elaborate apparatus that it has, by its own construction, made **unfalsifiable**. That is not a criticism of any individual rule's honesty — it is a criticism of the portfolio. Forty-eight gates, none of which can be evaluated, is not a method.

### 5.2 The predictive-weighting firewall has become a prohibition on learning

`L-087`'s firewall — one session's evidence may motivate a disclosure but never an ordinal rule — is *correct in principle*, and was correctly applied to the framework's own same-day gates. But combined with the near-total absence of any mechanism for accumulating evidence *toward* promotion, its practical effect is that **nothing can ever change the forecast**.

The pattern is consistent: `G20.2` → disclosure only, ordinal effect deferred to `C-TAIL-BUDGET`. `G21.1` → disclosure only, deferred to `C-PATH-GEOMETRY`. `G26.1` → withdrawn to `C-SEPARATION-FLOOR`. `L-075`–`L-077` → split, magnitude deferred to `C-WEIGHT-PROPAGATION`. There are **90 `CANDIDATE` and 25 `TESTING` entries**, and the register states plainly: *"No test below currently qualifies as a promoted forecast-weight rule."*

Zero forecast-weight promotions in 317 events. The firewall has no gate on the other side.

### 5.3 Version and reference chaos — `G0` is unsatisfiable as written

`G0` requires each card to declare the method version "found in that fresh read." Here is what a fresh read actually finds today [recomputed]:

| File | Declared method version |
|---|---|
| `AGENT_ROLE_AND_TASK.md` | `MDS-2026.09.05-v3.6` |
| `RULES_GENERAL.md` (header) | `MDS-2026.09.05-v3.6` |
| `RULES_GENERAL.md` §11 (`GFA-2`) | **`MDS-2026.09.06-v3.9`** |
| `README.md` | `MDS-2026.09.06-v3.8` |
| `MODEL_AND_DATA_SPEC.md` | `MDS-2026.09.05-v3.6` |
| `LEARNING_REGISTER.md` | `MDS-2026.09.05-v3.6` |
| `UPCOMING_GAME_RESEARCH_GUIDE.md` | `MDS-2026.09.05-v3.6` |
| `PERFORMANCE_ELIGIBILITY_POLICY.md` | `MDS-2026.09.05-v3.6` |
| all seven `RULES_<SPORT>.md` headers | `MDS-2026.09.05-v3.6` |
| `PREDICTION_MINI_RUNNING_LOG_P317.md` | `MDS-2026.09.05-v3.6` |

Fourteen of fifteen active documents say v3.6; the algorithm section says v3.9; the README says v3.8. **There is no single authoritative statement of the current method version.** A card cannot pass `G0` because `G0` has no determinate answer. The three sessions that "failed" this gate were reading the header — which is what a header is for.

Related live defects:

- **A withdrawn gate is still mandated.** `G26.1`'s hard bar was withdrawn on 2026-09-06(d), yet `AGENT_ROLE_AND_TASK.md` §6 item 12 still requires "the `G26.1` top-slot separation-floor result for Rank #1" as mandatory user-facing output, and card-checklist item 27 still demands it.
- **Gate vocabulary mismatch.** `G21.1` was corrected to `TRUE_UNION` / `LOW_BAR_CUMULATIVE` / `CENTRAL_BAND`. Checklist item 27 and `L-085` still specify the *superseded and category-erroneous* `UNION_LOW_THRESHOLD` / `INTERSECTION_CONSTRAINT` / `CENTRAL_BAND`. A card following the checklist would reintroduce the exact error §15 corrected.
- **Broken README link.** The document map links `PREDICTION_LOG_COMBINED_P267_SETTLED_2026-09-03.md`, which the active log's own snapshot notes "is absent from this checkout."
- **Duplicated policy blocks.** The "September 5 user confirmation" text is reproduced verbatim in at least five files; the "Complete Markdown recording requirement" in at least three; the settlement-only eligibility directive in at least four. Each copy is an independent opportunity for divergence — and they have already diverged, on the version numbers above.

### 5.4 Ledger integrity — the off-book cards

| Claim | Reality |
|---|---|
| `PREDICTION_LOG_COMBINED_2.md`: "Next canonical ID `P-306`" | `P-306`–`P-317` already issued |
| `PREDICTION_LOG_COMBINED_2.md`: "**Nothing is `DEFERRED` — no event in the log is awaiting a result**" | 24 cards marked `UNSETTLED`, including finished 2026-09-05 events |
| `README.md`: "No event in the log is awaiting a result" | same |
| `PREDICTION_MINI_RUNNING_LOG_P317.md` header: "Next canonical forecast ID: **`P-294`**" | the same file contains `P-317` |
| `GAME_LOG_STATUS_INDEX`, `GAME_LOG_LEDGER` | stop at `P-305`; `P-306`–`P-317` appear in neither |

Twelve issued forecasts sit outside every canonical record. `G34.1` (archival completeness) and `G1` (`GATE-LEDGER`) were both written to prevent exactly this and neither fired, because both govern *archiving* and *appending* — not the existence of a parallel unregistered running log. `EXTERNAL_LOGGING_WORKFLOW.md` sanctions the external-session running-log pattern but sets no reconciliation deadline.

There is also a same-event double-issue: `P-316` and `P-317` are both Doosan Bears @ SSG Landers, `P-317` being a "same-event pregame revision." The card correctly flags "do not double-count" — good discipline — but nothing in the ledger enforces it, and the canonical ID space now holds two IDs for one event.

### 5.5 Analytical defects visible in the cards themselves

Beyond compliance, reading the cards reveals recurring *reasoning* problems the gates do not catch.

- **Corridors are stated but never solved.** Cards routinely print "central corridor: Wofford 27–34, Gardner-Webb 14–21" and then locate a 50.5 line against it by inspection. But `27+14 = 41` to `34+21 = 55` **straddles 50.5** — which under §11.5's own evidence-ceiling table caps the row at `LOW` evidence and forbids a `LEAN`. `P-309` ranks it `LEAN` at Rank #1. This pattern — corridor straddles the line, row ranked anyway — is common, and is the mechanical explanation for the coin-flip totals record.
- **"Kill path" has become a ritual phrase.** It appears on 74–91% of cards, the highest compliance of any item. But naming a kill path is not weighing it. Cards name the path that defeats Rank #1 and then rank it #1 anyway, with no statement of why the path is subordinate. `G13`'s regime-dominance reconciliation requires exactly that statement and it is almost never written.
- **Recency is asserted, not retrieved.** Where cards carry form at all, it is usually "last five results" prose, not the L5/L10/L15/L20 table with the dispersion-based trend test that §11.3B specifies. The trend test — the entire stated reason four windows are retrieved — appears essentially nowhere.
- **Shrinkage is verbal.** `P-309` says Wofford's 42-point opener "requires shrinkage" and then uses a 27–34 corridor. How much shrinkage, from what prior, at what weight? Unstated. Every card does this. It is the single most important quantitative operation in forecasting and it is being done by adjective.
- **Opponent adjustment is named but not applied.** Cards correctly note "Gardner-Webb faced ranked Austin Peay while Wofford faced The Citadel" — and then compare the raw numbers anyway.

---

## 6. What needs comprehensive overhaul

This section is the actual recommendation. It is deliberately aggressive, per the brief.

### 6.1 Change the objective function — stop producing bare rank orderings

**The problem:** a forced unique ordinal over four supplied contracts is an objective that (a) the evidence shows is not being achieved, (b) has no natural scoring rule, and (c) forces a decision on rows where the honest answer is "indistinguishable." `G23.1` already concedes this with `NEAR_TIED`, and `rank_gap` was added to record how forced the choice was — but the forced choice is still made and still reported as the headline.

**The change:**

1. **Issue an explicit probability for every row.** Not a calibrated, validated, publishable probability — an explicit *stated subjective* probability, labelled `UNVALIDATED_SUBJECTIVE`, kept formally distinct from `PUBLISHED`. The framework currently forbids this on the grounds that only a validated model may publish probabilities. That is the correct rule for a *model* output. It is the wrong rule for an *analyst* output, and it has cost the system its only route to measurement: **you cannot compute a Brier score on an ordinal.**
2. **Derive rank from the probabilities**, rather than asserting it. Two rows at 0.52 and 0.51 produce an order *and* an honest statement that the order carries almost no information.
3. **Score everything with Brier score and a calibration curve from day one**, against the trivial baseline of 0.5 on every row. That single change makes every subsequent claim about the method testable. It requires no data pipeline, no code, no source approval — just a number on the card.

This is the highest-leverage change in this document. Everything else is second-order.

### 6.2 Collapse the sport and competition portfolio

The system cannot be good at 11 sports and 60 competitions. Nothing can.

**The change:** designate **two or three primary scored populations** — deepest structured data, highest event frequency, stable rules era. On this repository's own evidence the obvious candidates are **MLB** (already ~29% of the log; the best structured data in sport; `statsapi` supplies field-relative wind and umpires), **one soccer competition** (EPL — the ESPN lane covers it, including `wonCorners`), and optionally **NRL or AFL** (already well-instrumented in the sport files, and aligned to the user's timezone).

Everything else becomes explicitly `EXPLORATORY — NOT SCORED`: still forecast on request, still logged, but excluded from the primary performance record and exempt from the full checklist. This is not narrowing ambition — it is the only way to accumulate enough events per population for any claim to mean anything. At the current mixed rate the answer is never.

### 6.3 Cut the gate set by roughly two-thirds

Apply a hard test to all 48 gates: **name the specific card where this gate's absence caused a wrong forecast, and the specific card where its presence prevented one.** Gates that pass survive as gates. Gates that fail become an appendix of good practice.

My reading suggests the survivors are approximately:

**Keep as blocking (integrity — failure means the forecast is meaningless):** `G2` identity, `G3` target freeze, `G4` contract freeze, `G5` time/state, `G6` participant release, `G8` provenance (simplified to: exact URL + access time), `G31` final refresh, `G36` settlement from official record, `L-079` synthetic-content exclusion.

**Keep as required analysis (the actual forecasting work):** `G13.1` recency windows, `G14` exposure chain, `G14.1` deficit attribution, `G14.2` bench/coaching, `G15.1` environment, `G16` joint object, `G20` component budget, `G20.1` separation budget, `G22` bidirectional signs.

**Demote to guidance:** `G4.1`, `G9`, `G10`, `G17`, `G17.1`, `G19`, `G21`, `G23`, `G24`, `G25`, `G25.1`, `G26`, `G27`, `G28`, `G29`, `G30.1`. Every one is *sound advice*, and none has demonstrated it changes an outcome. They are currently consuming the budget that `G20` and `G13.1` should be getting.

**Delete outright:** `G20.2`, `G21.1`, `G26.1` — all three already reclassified to disclosure-only candidates by the framework's own review, all three never executed, all three imposing checklist cost for no effect. Let their candidate tests stand in the register; remove them from the live card.

Then set a standing rule: **the gate list is capped.** Adding one requires retiring one. The `L-096` effectiveness review runs on a schedule, and a control that has never fired in 50 cards is retired by default.

### 6.4 Replace prose shrinkage with explicit arithmetic

Every card currently does implicit Bayesian updating in adjectives. Make it explicit and it becomes checkable:

- **State the prior:** competition/venue baseline with sample size (already required by `G12`, and actually done reasonably often).
- **State each adjustment as a signed number with a weight:** *"Wofford opener 42 pts, but 14 from non-offensive/short-field scoring → offensive baseline 28; shrink 60% toward the 2025 season mean of 22.8 → 25.0."*
- **State the result as a centre and a width**, not a range of unspecified meaning. A corridor of "27–34" with no stated interpretation cannot be located against a line.
- **Then the component budget is arithmetic, not narrative** — which is what `G20` has asked for since v3.0 and gets 3% of the time.

This requires no fitted model, does not violate the Stage 0 boundary, and would immediately expose the straddled-corridor failure in §5.5.

### 6.5 Make retrospectives about mechanisms, not compliance

Current retrospectives are dominated by process-grade fields, defect classes, knowability tags, control-taxonomy classes and rule-gap fields. `F21` of the second review notes that winning cards get more generous narratives than losing ones — a sign the retrospective is grading the *card* rather than learning about the *sport*.

**The change:** every retrospective answers three questions and stops.

1. What did the score actually turn on? (The driver.)
2. Was that driver knowable before issue — and was it *in* the card?
3. What is the smallest change to the research routine that would have surfaced it?

Then, once per 25 events, a **pattern review** across those 25 answers. Per-card lesson generation is what produced 121 lessons from 317 events with 2 retirements: it generates a lesson per event because a lesson per event is what it is asked for.

### 6.6 Start Track B, scoped down to one population

`README.md` is right that Track B needs an explicit decision and is a large undertaking. But it frames Track B as all-or-nothing — S1 through S7, full H0, chronological folds, calibration blocks. That framing has kept the numerical program at Stage 0 since inception, and it is why "the most accurate sports prediction model" is not being approached.

A far smaller first step is available: **one population (MLB), one target (full-game runs), one baseline model (a Poisson / negative-binomial on park- and starter-adjusted run expectancy), scored head-to-head against the analyst's own subjective probabilities from §6.1.** That is a modest amount of work, uses the already-verified keyless `statsapi` lane, and answers the question the whole repository currently cannot: *is the qualitative process adding anything over a trivial statistical baseline?*

If it is, that is worth knowing. If it is not — which the 59.2% all-history and 43.8% recent Rank #1 records suggest is possible — that is worth knowing much more.

### 6.7 Fix the ledger, then keep it fixed

1. Reconcile `P-306`–`P-317` into `PREDICTION_LOG_COMBINED_2.md` immediately, settle every finished event, and correct the two "nothing is awaiting a result" statements.
2. Resolve the `P-316`/`P-317` same-event pair into one canonical ID with an alias, per `G1`.
3. **One log, one snapshot, one next-ID.** The current three-tier structure (closed archive → active combined → external mini-log → 18 frozen components) has produced exactly the divergence it was designed to prevent. If external sessions must produce running logs, the workflow needs a hard rule: *a running log not reconciled into the canonical log within 24 hours blocks the next forecast.*

---

## 7. Document consolidation plan

38 root-level Markdown files, ~1.4 MB of active rules, ~4.6 MB of logs. Target: **9 active documents.**

### 7.1 Merge

| New file | Absorbs | Rationale |
|---|---|---|
| **`METHOD.md`** | `AGENT_ROLE_AND_TASK.md` + `RULES_GENERAL.md` + `UPCOMING_GAME_RESEARCH_GUIDE.md` + `MODEL_AND_DATA_SPEC.md` §§3–8 + `PERFORMANCE_ELIGIBILITY_POLICY.md` | These describe **the same lifecycle four times**: `AGENT_ROLE` §3 as duties, `RULES_GENERAL` §11 as gates, `UPCOMING_GAME_RESEARCH_GUIDE` §§4–16 as an operational sequence, `MODEL_AND_DATA_SPEC` §3 as a pipeline. `AGENT_ROLE` §3.1 already concedes the conflict: *"where they are read differently, `GFA-2` controls."* One document, one statement, no precedence rule needed. Target **under 40 KB**. |
| **`NUMERICAL_PROGRAM.md`** | `ALGORITHM_PORTFOLIO_AND_EVALUATION.md` + `NUMERICAL_TRAINING_SPEC.md` + `NUMERICAL_MODEL_REGISTER.md` + `H0_DATASET_CARD.md` + `MODEL_AND_DATA_SPEC.md` §9 | 147 KB across four files describing a program at **Stage 0 with nothing built**. One document until something exists. |
| **`SOURCES.md`** | `DATA_SOURCE_REGISTER.md`, restructured | Currently 95 KB of per-sport prose lanes plus five dated session-access addenda. Convert to a **table**: source ID, sport/competition, fields owned, endpoint, keyless y/n, last verified, status. The addenda become rows, not sections. Target **under 30 KB**. |
| **`RULES_<SPORT>.md` ×7** | keep, but strip | Each is 36–61 KB carrying the sport module, the `SFA` algorithm, a full competition-rules reference *and* four to six dated amendment sections. Move competition rules into `LEAGUE_RULES_<SPORT>.md` companions — the pattern already exists for cricket and soccer; extend it to all seven. Fold dated amendments into the body. Target **under 20 KB each**. |
| **`CONTROLS.md` + `LESSON_ARCHIVE.md`** | `LEARNING_REGISTER.md`, split | 177 KB is unreadable at the point of use. `CONTROLS.md` holds the ~15 controls surviving §6.3 as a short table; `LESSON_ARCHIVE.md` holds the rest as historical evidence, not read per card. |
| **`LOG.md`** | `PREDICTION_LOG_COMBINED_2.md` + reconciled `P-306`–`P-317` | One active log, one controlling snapshot. |

### 7.2 Archive (move to `archive/`, stop treating as active)

`COMPREHENSIVE_RETROSPECTIVE_2026-08-22.md`, `COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-02.md`, `COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md`, `AUDIT_CHANGELOG_2026-09-05.md`, `AUDIT_CHANGELOG_2026-09-06.md`, `PREGAME_ELIGIBILITY_REGISTER_2026-09-05.md`, `GAME_LOG_STATUS_INDEX_2026-09-05.md`, `GAME_LOG_LEDGER_2026-09-06.md`, `GAME_LOG_BLINDSPOT_REVIEW_2026-09-06.md`, `IMPROVEMENT_PLAN_2026-09-06.md`, `EXTERNAL_LOGGING_WORKFLOW.md`, `PREDICTION_LOG_COMBINED.md`, and all 18 files in `prediction logs/`.

That is **~700 KB of dated audit material currently sitting in the active root** — including four near-duplicate status indexes of the same 305 records (`GAME_LOG_STATUS_INDEX`, `GAME_LOG_LEDGER`, `PREGAME_ELIGIBILITY_REGISTER`, and the status tables inside both settlement audits).

### 7.3 Delete the duplicated policy blocks

The "September 5 user confirmation" appears verbatim in ≥5 files; "Complete Markdown recording requirement" in ≥3; the settlement-only eligibility directive in ≥4. **State each once, in `METHOD.md`, and link to it.** These duplicates have already diverged — they are the mechanism by which the v3.6 / v3.8 / v3.9 confusion propagated.

### 7.4 Resulting active set

```
README.md              ~8 KB    map + current state + next ID, nothing else
METHOD.md             ~40 KB    role, gates, algorithm, settlement, eligibility
CONTROLS.md            ~8 KB    the surviving controls, as a table
SOURCES.md            ~30 KB    source table
NUMERICAL_PROGRAM.md  ~30 KB    Stage 0 design, one document
LOG.md                  live    one active log, one snapshot
RULES_<SPORT>.md ×7  ~20 KB ea  sport module + SFA only
LEAGUE_RULES_<SPORT>.md ×7      competition reference, consulted not read
```

**Mandatory per-card reading drops from ~570 KB to roughly ~90 KB** (`METHOD` + `CONTROLS` + one sport file + the snapshot). That is the change that makes the checklist executable — and therefore the change that makes every other rule real.

---

## 8. Priority order

| # | Action | Why in this position |
|---|---|---|
| 1 | Reconcile `P-306`–`P-317` into the canonical log; settle every finished event; correct the two false "nothing awaiting a result" statements | Ledger integrity underpins every other claim, and it is currently broken |
| 2 | Fix the version chaos: one authoritative method version in one place; remove the withdrawn-`G26.1` mandate from `AGENT_ROLE` §6 and checklist 27; correct the `G21.1` vocabulary in checklist 27 and `L-085` | Live, cheap, and currently causes cards to fail an unsatisfiable gate or reintroduce a corrected error |
| 3 | **Issue an explicit `UNVALIDATED_SUBJECTIVE` probability on every row and score it with Brier against a 0.5 baseline** | The only change that makes the system measurable; costs nothing; unlocks everything downstream |
| 4 | Execute the consolidation in §7 | Until the mandatory read fits in a session, no process rule is real |
| 5 | Cut the gate set per §6.3, with a hard cap and a default-retire rule | Frees budget for the analysis that actually predicts |
| 6 | Designate 2–3 primary scored populations; mark the rest exploratory | Only route to a population large enough to measure |
| 7 | Replace prose shrinkage with explicit prior + adjustment + width arithmetic | Directly attacks the straddled-corridor failure driving the coin-flip totals record |
| 8 | Rebuild retrospectives around the three mechanism questions; pattern-review every 25 events | Stops lesson inflation; starts sport-knowledge accumulation |
| 9 | Propose the scoped Track B pilot (MLB run totals vs. subjective probabilities) | Answers whether the qualitative process beats a trivial baseline |

---

## 9. The uncomfortable summary

Over 317 events this framework has produced: zero published probabilities, zero calibration measurements, zero forecast-weight promotions, zero gates retired for being useless, one all-history accuracy figure (**59.2%** on Rank #1, **43.8%** over the last 32 events) that was never computed until this review, and a headline contract ledger that is mathematically pinned near 50% by slate geometry.

In the same period it produced 48 gates, 28 checklist lines, 121 lessons, 130 promoted controls, and ~1.4 MB of active rule text — all of it explicitly disclaiming any predictive lift, and none of it executed on the twelve most recent cards.

The system has been optimising the thing it can measure — process compliance and honesty — and has become genuinely excellent at it. It has not been optimising the thing you actually want, because that thing was never made measurable.

**Making forecast accuracy measurable is the overhaul.** The rest of this document is implementation detail.

---

## Appendix A — Evidence index

| Claim | Where to verify |
|---|---|
| Rank #1 all-history 132-91 | cohort ledger rows, `PREDICTION_LOG_COMBINED.md` lines 27, 32–37, 133–135; `PREDICTION_LOG_COMBINED_2.md` lines 70, 1198, 6854, 7604 |
| Rank #4 outperforms Rank #1 | settlement matrix at `PREDICTION_LOG_COMBINED.md` line 20149; recomputed ledgers at lines 15372 and 20137 |
| "20 WIN / 20 LOSS mechanically forced by two complementary pairs" | `PREDICTION_LOG_COMBINED_2.md` line 6854 |
| Compliance percentages | automated parse of 238 card blocks across the three logs |
| Version disagreement | headers of all 15 active documents vs `RULES_GENERAL.md` line 442 |
| `G26.1` still mandated after withdrawal | `AGENT_ROLE_AND_TASK.md` §6 item 12; `RULES_GENERAL.md` line 770 vs line 698 |
| `G21.1` vocabulary mismatch | `RULES_GENERAL.md` line 635 vs lines 770 and 808 |
| `P-306`–`P-317` off-book | `PREDICTION_MINI_RUNNING_LOG_P317.md` vs `PREDICTION_LOG_COMBINED_2.md` line 21, `GAME_LOG_STATUS_INDEX_2026-09-05.md`, `GAME_LOG_LEDGER_2026-09-06.md` |
| Mandatory reading load 570 KB | byte counts of the eight files named in `RULES_GENERAL.md` §1 |
| 2 lessons ever retired | status-token counts across `LEARNING_REGISTER.md` |
| Straddled corridor at `P-309` | `PREDICTION_MINI_RUNNING_LOG_P317.md` §"Coherent score families" vs `RULES_GENERAL.md` §11.5 |
