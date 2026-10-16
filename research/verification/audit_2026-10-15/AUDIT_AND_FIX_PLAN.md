# Framework, ML/RL and prediction audit — 15 October 2026

**Status: AUDIT ONLY. Nothing below is implemented.** No control, code, log, archive file or ID was changed. This file is a proposal for a later prompt-8 change. Every fix needs its own owner approval, implementation and verification.

**Audited state:** `main` at `0ce4fb4cb` (MDS-2026.10.15-v16.0 · CR-2026.10.15-R7 · PRIMARY-v3.2 · SCV-v10 · SEL-v3 · P-v16.0), plus one uncommitted edit to `research/prompts/1_GAME_CARD.md` (left untouched).

**What was done:**
- Read the authority documents: README, CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION_RULES, SCORING_AND_VALIDATION, PRIMARY_PREDICTION_PROTOCOL, ML_EXECUTION_PROTOCOL, RESEARCH_COMPLETION_PROTOCOL and HISTORICAL_SOURCE_PROTOCOL.
- Read all of the primary runtime (`ml/primary.py`, `ml/execution.py`), the model engines (`gaussian`, `count`, `baseline`, `common`, `cricket`), `core/distributions.py`, `config.py`, the loader and the replay.
- Read every development result, the policy replay, the decision lab, the card-calibration report, the model status table and a sample of recent cards.
- Ran the `ml` test suite: **267 passed**. Ran two read-only checks on the archive (baseball run means, extras handling).

**Scope note:** the repository has no esports data, rules or models. "Each of the esports" is read as "each of the sports, leagues and competitions". If you meant esports (CS2, LoL, Valorant…), that would be a new sport area with no existing coverage.

Severity: **CRITICAL** = produces wrong probabilities or makes the method unusable as written. **HIGH** = materially biases results or blocks evaluation. **MEDIUM** = correctness or coverage gap with bounded impact. **LOW** = hygiene.

---

## 1. Executive summary — the ten things that matter most

1. **The mandatory primary ML cannot actually run in your operating model.** Prompts 1–3 are run by an external chat agent with read-only GitHub access (`PUBLISHED_MAIN_PINNED`). The rules nonetheless require a per-event Python execution with hash-bound receipts. No primary bundle, execution attempt, η admission or feedback row exists anywhere in the repository. (ML-07)
2. **Its input contract is practically impossible to satisfy honestly.** Every training row needs `final_at`, `available_at`, an HTTPS source and an evidence capture with SHA-256. That is roughly 7,000 rows for one MLB forecast, and no tool exports the archive into that format. Where publication time can't be shown, rows get today's capture time. The warm start then has zero games, so the mixture falls back to equal weights, including one-third on a team-blind baseline. (ML-06)
3. **Baseball has a structural home-team bias.** MLB home teams win 52.9% of games while scoring only 4.457 v 4.432 runs, because the home side skips or truncates the bottom of the 9th. The independent run model treats both sides as batting nine full innings, so it under-predicts home wins. All four baseball development models show it: calibration-in-the-large −0.030 (MLB), −0.041 (NPB), −0.022 (KBO), −0.027 (Minors). This also misprices the baseball ±1.5 run line that the framework gates specially. (ML-01)
4. **"Regulation" scores are final scores for every sport except hockey.** In 100% of MLB, NPB and KBO extra-innings rows, `reg_hs`/`reg_as` equal the final score. The same holds for basketball, NFL and NRL overtime. The runtime then adds an extra-time branch on top of scores that already include extra time. (ML-02)
5. **The primary runtime is not the model that was evaluated.** Primary uses fixed half-lives of 90/365 days, ridge 8 and inflation 1.1 for every sport. Development tuned values such as MLB ridge 128 / half-life 180, NHL ridge 32, EPL ridge 16 / 365 days, NBA half-life 45 and AFL ridge 2 / inflation 1.2. No development or replay evidence applies to V3 as configured, and the V3 replay output was never generated. (ML-03, ML-16)
6. **The "RL" learning loop is mathematically inert.** η = 2 (an untuned default) on summed losses from about 1,000–2,400 warm games is follow-the-leader. In the NBA the losing expert's weight is about e^−12. Even once card feedback exists, a handful of settled cards cannot move weights built from thousands of warm games. Nothing currently learns from your settled results. (ML-04, ML-05)
7. **The model ignores what the research collects.** Its only features are team identity, prior scores and time decay. It has no starting pitcher, goalie, lineup, injury, rest, travel or neutral-venue input. Your own rule (CURRENT_RULES §7) says material unfitted lineup effects mean qualitative/NO_FORECAST, which would make almost every MLB card NO_FORECAST. (ML-08)
8. **Coverage doesn't match what you request.** Only 1 of 31 soccer folders has data (EPL), 0 of 14 rugby union, 0 of 2 tennis, 1 of 12 T20, 0 of 7 field hockey. Phase/period rows (~13% of logged ranked rows), corners (~4%), tennis (~5% of cards) and props have no adapter. Today's four supplied games (KBL, India v WI T20I, MLS, WTA) give the ML at most 1 of 4 events (KBL) and 3 of 11 supplied contracts. (ML-18, DATA-01)
9. **Governance churn makes evaluation impossible.** There were seven framework changes on 15 October alone, and the primary method was replaced three times within one hour (V1 11:11, V2 11:45, V3 12:05). The prompt suite went from v11.3 to v16.0 in two days. Every version is its own cohort, and fewer than 8 weeks counts as INSUFFICIENT_EVIDENCE. So no version can ever be evaluated, and no hypothesis has ever been accepted (21 proposed-not-tested, 8 blocked-design, 0 accepted). (GOV-01, RES-05)
10. **The documentation is beyond what an operator can read.** The mandatory reading set is about 1.0 MB (about 250k tokens), more than a chat agent's context window. Rules are duplicated across six or more files with stale version stamps and contradictions. The recent P-585–P-589 cards were issued under an un-adopted policy (`SUPPLIED_FIRST_V1`), which is the predictable result. (GOV-02, GOV-03, GOV-05)

**What is sound:** the score-grid mathematics (one coherent distribution, exact W/P/L masses, tie resolution that conserves mass), receipt/hash custody, chronological fitting with leakage guards, the honest labelling culture, the scoring definitions and the integrity gate on archive rows. The 267 passing tests confirm the mechanics; they do not test the modelling issues above.

---

## 2. Primary ML / online-weighting runtime findings

### ML-01 · CRITICAL · Baseball walk-off truncation biases every baseball model against the home team

- **Evidence:**
  - Archive (2022+, regular season): MLB home win 0.529, mean runs home 4.457 / away 4.432. NPB 0.525, 3.465 / 3.373.
  - Development calibration-in-the-large: MLB −0.0297 (intercept +0.121, SE 0.024), NPB −0.0414 (+0.165), KBO −0.0222, Minors −0.0266.
  - In every MLB reliability bin, the hit rate is above the mean p by 1–6 points.
- **Mechanism:** `PoissonRatings` (count.py) and the negative-binomial grid treat home and away runs as independent nine-inning counts. The home team does not bat in the bottom of the 9th when it leads, and a walk-off ends the game at the winning run. Home run totals are therefore censored exactly in home wins. The fitted home edge is pushed towards zero, while home teams actually win about 53%.
- **Impact:**
  - P(home win) is under-stated by about 3 points.
  - Run lines are mispriced: home −1.5 is too low, and away +1.5 is too high, because home walk-off wins are mostly by 1.
  - Totals are biased low in home wins.
  - These are exactly the families (baseball +1.5, run line, totals) behind most baseball cards, and baseball is your largest sport (~175 of 583 logged cards).
- **Fix:**
  1. *Short term (one-line policy):* apply a coherent winner-class recalibration (`ScoreGrid.reweight_winner`, already implemented). Fit it on the prior season's home-win calibration for each baseball competition and record it as an admitted parameter.
  2. *Proper fix:* replace the nine-inning independent grid with an inning-level simulation.
     - Use per-half-inning run distributions with team offence/defence, and the bottom of the 9th played only if the home side is not ahead.
     - End a walk-off at the winning run (cap the margin by the runs needed plus the scoring-play size).
     - Add the extras rule (ghost runner in MLB from 2020).
     - Training data: MLB statsapi line scores (keyless, already in SOURCES); KBO/NPB 2025 line scores (repaired); earlier KBO/NPB seasons fall back to the step-1 calibration.
- **Acceptance:** held-out seasons show |calibration-in-the-large| ≤ 0.01 and calibration slope within 0.9–1.1, and run-line Brier does not get worse.

### ML-02 · HIGH · "Regulation" scores equal final scores outside hockey

- **Evidence:**
  - `ml/data/archive.py` lines 222–240 set `reg_hs, reg_as = hs, as_`, and only the hockey branch changes them.
  - The check found `reg==final` in 100% of extras rows for MLB, NPB and KBO.
  - `ml/primary.py::_fit_models` then fits "regulation" on those values when `tie_rule != "draw"`, and `apply_tie_rule` adds an extra-time branch again.
- **Impact:**
  - Extra-innings and overtime scoring is counted twice in the tie mass.
  - The model learns a no-tie final distribution and then invents a tie branch on top of it.
  - Extras margins are forced to exactly `winner_bonus=1`, whereas MLB ghost-runner extras often finish by 2+ when the away side wins.
  - The HISTORY.csv contract never defines what operators should put in `reg_hs`, so web-recovered rows will be inconsistent.
- **Fix:**
  - (a) Define `reg_hs/reg_as` precisely in PRIMARY_PREDICTION_PROTOCOL §2: the score at the end of scheduled regulation, or `NOT_OBSERVED`.
  - (b) Derive regulation scores from line scores or quarter scores where available: MLB statsapi, NBA/NBL/WNBA quarter fields, NFL/NRL period fields.
  - (c) Where they are not observed, exclude those games from the regulation likelihood (they still count for winner labels).
  - (d) Model the extra-time branch from the empirical margin distribution of extra-time games rather than a single bonus value.
- **Acceptance:** a unit test that a 5–4 eleven-inning game enters the fit as 3–3 (or is excluded); total CRPS on extras games not worse.

### ML-03 · HIGH · Primary experts use one untuned recipe for every sport

- **Evidence:**
  - `ml/primary.py` lines 244–251 fix half-life 90/365, ridge 8 and cov_inflation 1.1, and the receipt records this.
  - Development-tuned parameters differ (each league's `research/model_shadow/<model>/PARAMETERS.md`): MLB ridge **128**, half-life 180; NHL ridge **32**, 180; EPL ridge **16**, 365; NBA half-life **45**; AFL ridge **2**, inflation **1.2**; NFL half-life 180.
  - Ridge has different units in the Gaussian engine (points²-weighted) and the count engine (log-rate), so "8" means very different shrinkage across sports.
- **Impact:** MLB and NHL experts are under-regularised (noisy, overconfident team effects), while NBA uses a slower decay than tuned. None of the development verdicts or replay results describe the model that now produces primary p_card.
- **Fix:** add `research/primary_policy/EXPERT_PARAMETERS.csv`, admitted exactly like the η table (competition, policy, half-lives, ridge, inflation, tune_end, frozen_at, evidence).
  - Populate it from tune-season results only.
  - For a competition without a row, use a scale-free sport-family default (ridge proportional to the league's score variance and games per team).
  - Re-run the development backtest with the exact primary recipe.
- **Acceptance:** each competition's receipt names an admitted parameter row or `DEFAULT_SPORT_FAMILY`; the development report exists for that exact recipe.

### ML-04 · HIGH · η = 2 turns the "mixture" into follow-the-leader in high-volume leagues

- **Evidence:**
  - `research/primary_policy/ETA_ADMISSION.csv` does not exist, so every forecast uses `DEFAULT_ETA = 2.0` ("provisional, not tuned/validated").
  - Losses are summed over 30 game-weeks: about 1,000+ NBA games and about 2,400 MLB games.
  - NBA replay home-win Brier is FAST 0.2118 v SLOW 0.2230, a composite gap of about 0.0056 per game, or about 6 over a window. With η = 2 the SLOW weight is about e^−12. The textbook Hedge rate for T ≈ 1,200 and 3 experts is about √(8·ln3/T) ≈ 0.09.
  - The old replay picked a boundary η (0.5 or 50) in 16 of 28 competitions, so its grid was too narrow.
  - In the replay, Hedge never beat the best single expert anywhere. It was significantly worse for Greek basketball, and EQUAL_MIX was often equivalent.
- **Impact:** in high-volume leagues the "mixture" is just "use whichever decay won the last 30 weeks". In low-volume leagues it may mix, but with an arbitrary rate. Neither is validated.
- **Fix:**
  - (a) Use mean per-game loss (or exponentially discounted sums), so η has a fixed meaning across leagues.
  - (b) Better: replace Hedge with stacking. Fit convex expert weights by minimising the out-of-sample proper score on the warm window, with a weak Dirichlet prior towards equal weights. This is deterministic, uses the same data and directly targets accuracy.
  - (c) Admit the chosen rule through the parameter table, tuned before test seasons with an extended grid.
- **Acceptance:** a regenerated V3 replay shows mixture ≤ best single expert (non-inferior) in pooled and per-league views.

### ML-05 · HIGH · Feedback from settled cards cannot change anything — and has never run

- **Evidence:**
  - No `research/primary_predictions/` folder, no execution attempt and no feedback row exists.
  - `forecast()` combines the warm loss ledger (re-derived from history each time, sliding 30 weeks) with feedback losses (accumulating forever with no decay).
  - Five settled bundles against 1,200 warm games carry about 0.4% of the evidence.
- **Impact:** "learning from our own results" (the RL framing in README, CURRENT_STATE and prompts) has no measurable effect. The feedback ledgers are pure custody overhead.
- **Fix:** decide what the feedback loop is for.
  - **Option A (recommended):** drop the RL framing. Call it "out-of-sample expert weighting from history". Keep settlement feedback for **evaluation** only: a prospective score of mixture v each expert v baseline.
  - **Option B:** add a separate, small **calibration layer** learned from settled primary rows, per sport family. Use a logistic recalibration of p_card with a strong prior at identity, updated only after N ≥ 50 settled rows. That is where your own outcomes can genuinely help.
- **Acceptance:** the protocol states which option applies, and a test shows feedback changes the intended quantity by a documented amount.

### ML-06 · CRITICAL · The HISTORY input contract is infeasible and pushes operators toward fabricated known-at times

- **Evidence:**
  - `admit_history` requires, for every training row: `date ≤ final_at ≤ available_at ≤ horizon`, `status=FINAL`, `admission=RESEARCH_INPUT_REVIEWED`, an HTTPS `source_url`, and an evidence file with matching SHA-256.
  - No code in `ml/` produces rows in this format from the archive. A search for `ARCHIVE_REVIEWED` outside `primary.py` and its tests finds nothing.
  - HISTORICAL_SOURCE_PROTOCOL §3 says unproven publication times become "first defensible observed/capture availability time", which is today.
  - `warm_records` then admits only rows with `available_at <= Monday of each simulated week`, so it gets zero games.
- **Impact:**
  - Either nobody can run the model (the current reality), or rows are stamped with invented `available_at` values. The repository has a documented history of fabricated records (memory: synthetic content trap; peer commit 0e5685e57).
  - If run honestly with web rows, the weights are uniform: one-third on the team-blind LEAGUE_BASELINE, which flattens every probability towards the league average.
- **Fix:**
  1. Add `python -m ml primary export-history --competition <path> --through <date>`. It emits HISTORY.csv from reviewed archive seasons with **one evidence capture per season file** (the archive file's SHA as evidence) and `source_kind=ARCHIVE_REVIEWED`.
  2. Adopt a documented **historical known-at convention**. For results older than 7 days at the horizon, `available_at = final_at + 24h`, labelled `KNOWN_AT_CONVENTION_24H`; known-at only matters for very recent rows. Rows inside the last 7 days need a real capture.
  3. Make `warm_records` respect the convention (it already uses `available_at`).
  4. Amend CURRENT_RULES §5 R28 so convention-labelled archive results may decide Rank 1. The present rule forbids it, which contradicts using the ML at all.
- **Acceptance:** one command produces a valid HISTORY.csv for the 29 modelled competitions; a test shows warm coverage over 0 for archive history.

### ML-07 · CRITICAL · Mandatory execution contradicts who runs prompts 1–3

- **Evidence:**
  - README: "Prompts 1 to 3 are run by an external chat agent with GitHub read-only."
  - CURRENT_RULES §1 makes `PUBLISHED_MAIN_PINNED` the default for prompts 1–3, while ML_EXECUTION_PROTOCOL §1 requires `python -m ml primary execute` for every new game.
  - The latest cards (P-585–P-589) are hand-built `UNCALIBRATED_ANALYST_SCENARIO`s under `SUPPLIED_FIRST_V1`, one issued 4 minutes after the scheduled start (P-586).
- **Impact:** every compliant new card fails C21 (capability-blocked), or the operator fabricates receipts. The "primary" method exists on paper only.
- **Fix:** choose one operating model and write it into CURRENT_RULES §1.
  - **(Recommended) Pre-computed fixture grids.** A local Claude Code task (new prompt "1-ML") runs daily or on request. It runs `export-history` and `primary execute` for every scheduled fixture in the competitions you request. It commits the market-free bundles (PREDICTIONS/GRIDS/RECEIPT CSV) to `research/primary_predictions/<date>/`. The read-only chat agent then **reads** the committed bundle for its card. This preserves custody and fits the read-only operator.
  - **Alternative:** prompts 1–3 run in Claude Code locally (`LOCAL_WORKING_TREE`).
  - Either way, make ML **mandatory only where a supported adapter and history exist** and say so plainly. Elsewhere the analyst method is the declared primary, not a "NOT_PRIMARY comparison".
- **Acceptance:** at least one real executed bundle is consumed by a real card; C21 can pass.

### ML-08 · HIGH · The model has none of the inputs that decide games

- **Evidence:** receipt field `model_features = "team identity, prior scores, time decay; no fitted availability effects"`. CURRENT_RULES §7 says: "Unsupported material lineup/weather/regime effects mean qualitative/NO_FORECAST until a versioned scenario adapter actually runs."
- **Impact:**
  - MLB/KBO/NPB: the starting pitcher, the largest single pregame factor.
  - NHL: the starting goalie.
  - NBA/WNBA/NBL: star availability and rest.
  - Soccer: the XI.
  - Cricket: the toss and XI.
  - Without these, the model is a season-strength prior. Under your own rule nearly every baseball card should be NO_FORECAST, yet the method calls the model primary. Meanwhile the mandatory roster research changes nothing numerically.
- **Fix:** add a versioned **adjustment adapter** layer (`ml/adapters/`). It applies measured mean shifts to the expert grids before mixing, each estimated on history with chronological validation:
  1. **MLB/KBO/NPB starting pitcher:** shift the opponent's run rate by the pitcher's shrunk run-prevention rate (e.g. prior-season and to-date FIP/ERA blended toward league) times the expected innings share. Data: MLB statsapi probable and confirmed starters.
  2. **NHL starting goalie:** shrunk save % above replacement times expected shots.
  3. **Basketball availability:** minutes-weighted on/off or box-plus-minus proxy for confirmed absences, capped.
  4. **Soccer XI:** starters' share of season minutes as a strength multiplier (coarse).
  5. **Neutral venue / rest / travel:** see ML-09.

  Each adapter needs its own development test, receipt field and admission row. Until an adapter exists, keep the current rule but state its consequence honestly: research notes may not alter p.
- **Acceptance:** the MLB SP adapter improves held-out home-win Brier against the no-adapter model with a week-block interval below zero.

### ML-09 · MEDIUM · No neutral-venue handling anywhere

- **Evidence:** no `neutral` field in any model, config or request schema. A search for "neutral" in `ml/` finds nothing.
- **Impact:** finals and tournaments get a full home edge for whichever side is listed first. Affected: AFL/NRL Grand Finals, Super Bowl, EuroBasket and World Cups, cup finals, IPL playoffs at neutral grounds, T20Is in third countries.
- **Fix:**
  - Add an optional `neutral` column (Y/N) to HISTORY and REQUEST.
  - Gaussian engine: drop `mu_h − mu_a` to the league mean for neutral games. Count engine: drop the home term.
  - Estimate the home edge from non-neutral games only.
  - Archive loaders take the flag from venue versus home ground where available.
- **Acceptance:** a unit test where neutral pricing gives a symmetric P(home) for equal teams.

### ML-10 · MEDIUM · Systematic under-confidence in points sports; overconfidence in a few

- **Evidence (development logistic slope; above 1 means p too close to 50%):** NBA 1.368, NFL 1.326, ACB 1.332, EPL 1.243, EuroCup 1.265, EuroLeague 1.235, VFL 1.462, SANFL 1.810, Austria 1.284, Greek 1.302, NBL 1.205, Czech 1.244. Below 1 (overconfident): EuroBasket 0.622, VFLW 0.694, Danish 0.745 (CITL −0.076), Minors 0.765, KBO 0.818.
- **Impact:** Rank-1 probabilities in NBA/NFL/ACB/EPL are understated, so fewer rows clear the 0.62 gate. Mixing with the team-blind baseline worsens this. The cards' own historical calibration slope is 0.83 (overconfident), so model and analyst err in opposite directions.
- **Fix:**
  - Run the existing ML-CAL-WIN experiment (logistic map fitted on the previous season only) as a pre-registered shadow per competition.
  - If accepted, apply it coherently through `reweight_winner`, and for margins by scaling the margin SD.
  - Revisit `cov_inflation` (a fixed 1.1 inflates every margin SD by about 5%) and ridge (ML-03) first: much of the under-confidence is self-inflicted shrinkage.
- **Acceptance:** slope within 0.9–1.1 on the next test season.

### ML-11 · MEDIUM · Expert weights are learned on the wrong question

- **Evidence:** `expert_loss` is the mean of home-win Brier and over-the-league-median-line Brier. In soccer the winner question is binary home v not-home, ignoring the draw. Cricket scores the total only.
- **Impact:** issued rows are handicaps and totals at supplied lines (often far from the median) and three-way soccer results. An expert that is best at the median line can be worst in the tails being priced.
- **Fix:** score experts with full-distribution proper scores: margin CRPS + total CRPS (already implemented in `ScoreGrid`), and three-way RPS or half-sum multiclass Brier for soccer. These cover every line at once.
- **Acceptance:** a unit test plus a replay comparison.

### ML-12 · MEDIUM · The runtime ranks by p_card but leaves the gate, complements and families to the operator

- **Evidence:**
  - `forecast()` sorts eligible rows by p_card, applies only the baseball +1.5 floor, and writes "Gate/family/precision… remain required by the card operator".
  - SELECTION_RULES requires a gate against the best non-complementary alternative, quantity keys, line-distance z and three shadows.
- **Impact:** every operator re-derives these by hand, inconsistently. Supplied complementary pairs (e.g. Thunders +1.5 / Sakers −1.5, O/U 160.5) yield a mechanically split top two, and the gate has never passed (0/20 in the last retrospective).
- **Fix:** compute in the runtime and write to PREDICTIONS.csv:
  - quantity key and complement flag;
  - Rank-1 gate (PASS / RANK1_UNSTABLE / NOT_ASSESSABLE / GATE_UNRESOLVED_PRECISION, with ε = 0 for exact grids);
  - line distance and z;
  - BASELINE_P and Δ;
  - SHADOW_RANK_DELTA, SHADOW_R2_RET04 and XCARD6 selections;
  - the exact joint loss from the grid (available, because every row comes from one grid).

  The operator then copies rather than computes.
- **Acceptance:** a test reproduces SELECTION_RULES §2–3 on a fixture.

### ML-13 · MEDIUM · Any unseen team blocks the forecast

- **Evidence:** `fit_experts_and_line` raises "unseen participant: no silent prior". `promoted_prior` exists only for EPL in the count engine; the Gaussian engine uses 0.
- **Impact:** newly promoted or expansion clubs, renamed franchises missing an alias, international sides with sparse meetings and the first round of a new season all become NO_FORECAST.
- **Fix:** a labelled hierarchical prior. A new team gets the mean of last season's bottom-k (promoted) or the league mean, with an inflated rating variance carried into the grid. Flag it `NEW_TEAM_PRIOR` and allow it, but exclude it from Rank 1 unless p clears the gate even under the widened variance.
- **Acceptance:** a unit test plus a replay of the first round of a season.

### ML-14 · MEDIUM · Basketball overtime and period-length handling is crude

- **Evidence:**
  - `normal_extra` resolves overtime into one deterministic state (winner +w, both +b), so OT margins and totals have zero spread.
  - `config.py` decides 48 versus 40 minutes by searching for the substring "48" in the last season file's first 50 period-format values. A missing column means 40 minutes.
- **Impact:** small but systematic errors on handicaps and totals near ±3–6 and big totals in OT games. A competition without a period-format column is silently treated as 40 minutes.
- **Fix:** an explicit `period_minutes` per competition in `OVERRIDES` (fail if unknown); OT as a small normal distribution scaled by r = 5/48 or 5/40, discretised.
- **Acceptance:** tests plus OT-game total CRPS.

### ML-15 · LOW · NFL key numbers implemented but unused in primary

- **Evidence:** `GaussParams.key_numbers` defaults to False, primary never sets it, and the development `KEYNUM` variant exists in `run.py`.
- **Impact:** integer NFL handicaps (3, 7) get wrong push and win masses.
- **Fix:** enable it through the parameter table (ML-03) if its development variant is non-inferior.

### ML-16 · HIGH · Development evidence is stale and the verdict rule is too blunt to inform anything

- **Evidence:**
  - STATUS was generated at `980e60178` before the bug audit, and BUG_AUDIT_ADMISSION says outputs need regeneration.
  - The `PRIMARY_POLICY_REPLAY_V3` folder named in the replay code was never produced.
  - The verdict requires the 95% interval to be below zero against **both** comparators in **every** test season. MLB is labelled FAIL although it beats the league baseline every season (pooled −0.0057 [−0.0074, −0.0040]) and TB-1 pooled (−0.0025 [−0.0039, −0.0010]); one season merely spans zero.
- **Impact:** "25 of 29 FAIL" sounds like the models are worse than baselines. Most are better, just not significantly in every single season. Meanwhile nothing describes V3.
- **Fix:**
  - Regenerate all development outputs and the V3 replay on current code with the admitted primary recipe.
  - Replace the binary verdict with a graded one:
    - `SUPERIOR`: pooled interval below 0 and every season non-inferior within a margin, e.g. +0.002 Brier.
    - `NON_INFERIOR`.
    - `INFERIOR`.
- **Acceptance:** a STATUS row per competition at the current code SHA.

### ML-17 · MEDIUM · Cricket model scope

- **Evidence:**
  - Primary cricket needs an exact batting role, so it cannot price pre-toss.
  - Experts use 90/365-day decay, whereas the development grid searched 365–1,460 days. A 90-day half-life in a two-month annual league like the IPL effectively discards prior seasons.
  - Only the IPL has data; the ODI run is incomplete (exit 127).
  - Powerplay contracts (e.g. today's WI powerplay O/U 57.5) are unsupported.
- **Fix:**
  - Use the tuned decay.
  - Add the C2_PRE toss mixture as a supported request mode, with the toss-decision prior from each team's history.
  - Add a phase model: powerplay runs as a share of innings runs (beta regression on venue/era) feeding a coherent powerplay distribution.
  - Ingest Cricsheet for T20I, BBL, PSL, CPL, SA20 and The Hundred (a local Cricsheet ODI cache already exists).
  - Rerun the ODI model.

### ML-18 · HIGH · Request mix v adapter coverage

- **Evidence:**
  - Rough keyword classification of `GAME_PREDICTION_RANK_LOG.csv` (583 cards, 2,245 rows): baseball ~175 cards, soccer ~87, cricket ~45, basketball ~43, tennis ~27, AFL ~20, NRL ~15, NFL ~10, unclassified ~155.
  - Rows: totals ~982, handicaps ~527, winner/other ~429, **phase/period ~193, corners ~80, player props ~34**.
  - No adapter covers tennis, corners, halves/quarters/powerplays/F5, props or any soccer league except the EPL.
- **Fix (priority order, by request volume × feasibility):**
  1. **Soccer, all leagues:** the Dixon–Coles engine is generic, so the bottleneck is data (DATA-01). First-half goals: a half-split Poisson with the first-half share estimated per league (about 0.44–0.46).
  2. **Tennis:** a point-level Markov model (serve and return points won, shrunk by surface) producing match, set-score and game totals and handicaps, as PROBABILITY_TOOLKIT already specifies. Data: public ATP/WTA match archives.
  3. **MLB first 5 innings (F5):** comes from the inning-level simulation in ML-01.
  4. **Corners:** negative-binomial team corner rates from the provider routes already named (UEFA/PL APIs, ESPN `wonCorners`).
  5. **Basketball quarters/halves:** proportional splits of the full-game normal with period-specific correlation.
  6. Props stay out of scope.

### ML-19 · LOW · Naming and the firewalled benchmark

- **Evidence:**
  - Documents call the runtime "ML/RL" while each protocol concedes "no trained environment-control RL policy".
  - DECISION_LAB (firewalled, EPL 2023–25): model three-way Brier 0.2901 v no-vig close 0.2795. The model is worse by 0.0129 [0.0079, 0.0180], and better than TB-1 (−0.0099) and the league baseline (−0.0347).
- **Fix:**
  - Rename to "fitted score models with out-of-sample expert weighting".
  - Keep the market firewall, but record (in model documentation only, never in cards) that the sports-only EPL model is about 0.013 Brier short of an efficient benchmark. This sets realistic expectations for supplied balanced lines (RES-01).

---

## 3. Sport-by-sport and competition-by-competition

Development figures are the 14 October run (pre-bug-audit code, tuned development recipe, **not** the primary recipe; see ML-03 and ML-16). CITL = calibration-in-the-large (positive = over-predicts home); slope above 1 = under-confident. Replay = historical policy proxy (best single expert; Hedge never significantly better).

### Baseball

| Competition | Data / status | Development verdict and calibration | Specific issues | Fix |
|---|---|---|---|---|
| MLB | 2000–2026; DEVELOPMENT_ONLY | FAIL by rule, but beats league and TB-1 pooled; CITL −0.030, slope 1.14 | ML-01 walk-off bias; ML-02 extras = finals; ridge 128 tuned v 8 used; no starting pitcher | ML-01, ML-02, ML-03, ML-08 SP adapter first; F5 from the inning simulation |
| NPB | DEVELOPMENT_ONLY | FAIL; CITL −0.041, intercept +0.165 | Same as MLB; ties allowed (residual draw); extras share 2.9% in 2022+ looks low; innings placeholders before 2025 | Verify extras/tie flags against npb.jp; ML-01 step-1 calibration until line scores are repaired |
| KBO | DEVELOPMENT_ONLY | FAIL; CITL −0.022, slope 0.82 (overconfident) | Extras share 2.1% looks low; innings 2000–2024 placeholders; MyKBO innings wrong 2/70 | Repair from the KBO GetScoreBoardScroll JSON (route already known); then as MLB |
| Minor Leagues | DEVELOPMENT_ONLY | FAIL; CITL −0.027, slope 0.77 | Pooled levels/affiliates in one competition | Split by level, or drop from primary scope |
| ABL, CPBL, Mexican, Caribbean, WBC, Premier12, Olympics | Header-only | — | No data | DATA-01 queue by request frequency |

### Basketball

| Competition | Data / status | Development | Issues | Fix |
|---|---|---|---|---|
| NBA | DATA_HOLD (field owner unverified) | **PASS**; slope 1.37 (under-confident) | Tuned half-life 45 v primary 90/365; no availability/rest | ML-03, ML-10, availability adapter |
| WNBA | DEVELOPMENT_ONLY | FAIL v TB-1 only; slope 1.13 | Short season; FAST best | ML-03 |
| NBL | DEVELOPMENT_ONLY | FAIL; slope 1.21 | 29-game 2026-27 snapshot only for the current season | Keep the current season updated (prompt 7) |
| KBL (requested today) | DEVELOPMENT_ONLY; rebuilt 14 Oct observed-only | FAIL; CITL −0.016, slope 1.07 | Rebuilt; no profile in LEAGUE_PROFILES | Primary can run once ML-06/07 exist; add a profile row |
| B League | DATA_HOLD | **PASS**; well calibrated (slope 1.08) | Field-owner admission | Field-owner verification → admit |
| Liga ACB | DATA_HOLD | **PASS**; slope 1.33 | Under-confident | ML-10 |
| Greek Basket League | DATA_HOLD | **PASS** | OT field implausible 1/812; dispersion anomalies in 1977–85 and 2000–06; Hedge worse than SLOW | Repair the OT field; trim the fit window to clean seasons |
| EuroLeague | DEVELOPMENT_ONLY | FAIL v TB-1; slope 1.24 | **Current code flags OVERTIME_FIELD_IMPLAUSIBLE:0/1718**, so primary refuses EuroLeague (the STATUS table predates this) | Repair the OT field from the EuroLeague media API |
| EuroCup | DEVELOPMENT_ONLY; rebuilt 14 Oct | FAIL v TB-1; slope 1.27 | P-586 found 2025 header-only at its pinned SHA (pre-rebuild) | Confirm rebuild coverage; add a profile |
| NBA G League | DEVELOPMENT_ONLY | FAIL | Roster churn makes team identity weak | Shorter decay; probably keep out of primary |
| Austria Bundesliga (alias BSL) | DEVELOPMENT_ONLY | FAIL | OT field 0/909 implausible | Repair or quarantine |
| EuroBasket | DEVELOPMENT_ONLY | FAIL; slope 0.62 (overconfident) | Quadrennial, tiny n, neutral venues | ML-09 neutral; national-team prior |
| 16 other folders (ABA, BBL, CBA, LNB, PBA, VTB, WNBL, NBL1, FIBA events…) | Header-only | — | No data | DATA-01 |

### Ice hockey

| Competition | Status | Development | Issues | Fix |
|---|---|---|---|---|
| NHL | DEVELOPMENT_ONLY | FAIL; well calibrated (slope 0.94, CITL −0.006) | Tuned ridge 32 v 8; no goalie | ML-03, goalie adapter |
| Czech Extraliga | DEVELOPMENT_ONLY; rebuilt 12 Oct | FAIL; slope 1.24 | — | ML-03 |
| Danish Metal Ligaen (alias Metal Ligaen) | DEVELOPMENT_ONLY | FAIL; **CITL −0.076, intercept +0.56** | Large home under-prediction; possible data/decision issue | Audit the decision field and home-ice pattern before any use |
| AHL, KHL, SHL, Liiga, DEL, Swiss, PWHL, ECHL, AIHL, IIHF, Olympics | Header-only | — | — | DATA-01 |

### Soccer

| Competition | Status | Development | Issues | Fix |
|---|---|---|---|---|
| Premier League | DEVELOPMENT_ONLY | FAIL v TB-1 by rule; slope 1.24; market benchmark gap 0.013 | Winner loss ignores the draw (ML-11); no XI; halves and corners unsupported | ML-11, ML-18 half split, corners |
| **30 other folders** (MLS — requested today — La Liga, Serie A, Bundesliga, Ligue 1, A-League, UCL/UEL/UECL, World Cup, women's leagues…) | Header-only | — | The engine is generic; only data is missing | DATA-01 top priority: scores-only bulk import from keyless sources |

### Cricket

| Competition | Status | Issues | Fix |
|---|---|---|---|
| IPL (T20) | DEVELOPMENT_ONLY (C2 FAIL) | Pre-toss unsupported; 90-day decay; powerplay unsupported | ML-17 |
| ODI International | RUN_INCOMPLETE (exit 127) | Never completed | Rerun |
| County Championship (multi-day) | NOT_MODELLED | Declarations/follow-on need a separate model | Keep out of scope |
| T20I (requested today), BBL, WBBL, PSL, CPL, SA20, ILT20, MLC, Hundred, WPL, World Cups; Marsh, Vijay Hazare; Shield, Ranji, Plunket, Ashes | Header-only | No data | Cricsheet ingestion (ML-17) |

### Football codes, rugby, AFL

| Competition | Status | Development | Issues | Fix |
|---|---|---|---|---|
| NFL | DEVELOPMENT_ONLY | FAIL v TB-1; slope 1.33 | Key numbers off; OT residual draw | ML-15, ML-10 |
| College Football FBS | NOT_MODELLED | — | 304/783 dates on 01-01 (default dates); 1900–1960 fabricated stubs (memory) | Rebuild from observed data or quarantine |
| UFL, IFAF | Insufficient history | — | — | — |
| Super Bowl, AFL Grand Final | Single-game subsets | — | Neutral venue (ML-09) | ML-09 |
| CFL, Grey Cup, Vanier Cup, bowls, CFP | Header-only | — | — | DATA-01 |
| AFL | DEVELOPMENT_ONLY | FAIL v TB-1; best-calibrated model (slope 0.99) | Tuned ridge 2 / inflation 1.2 v primary 8 / 1.1; draws allowed | ML-03 |
| AFLW | DEVELOPMENT_ONLY | FAIL | Small seasons | ML-03 |
| SANFL, VFL, WAFL, VFLW | DEVELOPMENT_ONLY | FAIL; SANFL slope **1.81**, VFL 1.46 (very under-confident), VFLW 0.69 | Cancelled 2021 seasons (placeholder rows already dropped) | ML-10 |
| NRL | DEVELOPMENT_ONLY | FAIL; slope 0.90 | Golden-point residual draw | ML-03 |
| Super League, State of Origin, NRLW, RLWC, RFL | Header-only | — | — | DATA-01 |
| **Rugby union (all 14)** | Header-only | — | Engine exists (Gaussian) but no data | DATA-01 |

### Tennis and field hockey

| Sport | Status | Fix |
|---|---|---|
| Tennis (ATP, WTA; requested today: WTA Mallorca games handicap/total) | No engine, no data | ML-18 point-Markov adapter + match archive |
| Field hockey (7 folders) | No engine, no data | Low priority unless requested |

---

## 4. Framework and governance findings

### GOV-01 · HIGH · Change velocity prevents any evaluation

- **Evidence:**
  - 15 October: framework changes 2026-10-15-1 to -7, control revisions R1–R7, primary V1→V2→V3 between 11:11 and 12:05.
  - Prompt suite v11.3 → v16.0 within 14–15 October; 35 commits since 10 October.
  - SCORING §5 requires 8 or more ISO weeks per frozen cohort, and versions must not be pooled.
- **Impact:** no policy survives long enough to be scored, so every comparison is INSUFFICIENT_EVIDENCE forever. The register shows it: 21 PROPOSED_NOT_TESTED, 8 BLOCKED_DESIGN, 0 accepted.
- **Fix:** a release cadence written into CURRENT_RULES §11.
  - **Statistical/selection changes** ship only in numbered releases, at most once every 4 weeks. Each release freezes its policy for at least 8 weeks or 150 settled primary rows, whichever is later.
  - **Procedure/bug fixes** may ship anytime but must not change p or ranks.
  - An emergency change (fabrication or leakage) is allowed with a written reason.

### GOV-02 · HIGH · The mandatory reading set is unreadable

- **Evidence:**
  - Prompt 1's reading gate covers about 1.03 MB (about 250k tokens): CURRENT_STATE, METHOD, CURRENT_RULES, SELECTION, TEMPLATES, prompt 1 (936 lines), COMMON, five protocols, sport rules (~450–630 lines), PROBABILITY_TOOLKIT (777), BASE_RATES (505), LEAGUE_PROFILES, SOURCES (1,339), ARCHIVE_USE_GUIDE and GAME_LOG_STATUS.
  - CURRENT_RULES §1 says: "claim full reading only when full text was read."
  - The EXEC-v1 paragraph is pasted nearly verbatim into README, CURRENT_STATE, ml/README, CURRENT_RULES §6, SELECTION_RULES §9, RESEARCH_COMPLETION §3 and PRIMARY_PREDICTION_PROTOCOL.
- **Impact:** the operator cannot comply. Reading receipts become formulaic, and agents fall back to partial or remembered rules (GOV-05). Long cards follow (RES-06).
- **Fix:**
  - One **operator spec** per prompt, at most about 3,000 words, containing every *must*. Everything else is reference material, read on demand with a section pointer.
  - Each rule lives in exactly one file; others link to it.
  - Move dated history ("October 12 implementation status…") out of CURRENT_STATE and README into CHANGELOG.
  - CURRENT_STATE becomes the state table only.
  - Target: mandatory pre-research reading of at most 60k tokens.

### GOV-03 · MEDIUM · Stale and contradictory version stamps and claims

- **Evidence:**
  - README sections still cite "Control CR-2026.10.14-R3; suite P-2026.10.14-v11.3".
  - ml/README says "prompt suite v15.0"; HISTORICAL_SOURCE_PROTOCOL and RESEARCH_COMPLETION headers carry MDS v15.2 / CR-R6 / P-v15.0 (current v16.0 / R7).
  - CURRENT_STATE still says "Prompt v11.3 retains this procedure".
  - CURRENT_RULES §9 says the committed `.gitattributes` was deleted. One now exists, but it covers only six archive/model paths, not the logs and evidence folders §9 lists.
- **Fix:** a single `VERSIONS.md` manifest. Other documents say "see VERSIONS" instead of restating numbers. Add a lint check (a test under `ml/tests/`, which is allowed) that fails when a document names a superseded control as current.

### GOV-04 · HIGH · Rules that contradict each other

| Conflict | Where | Resolution |
|---|---|---|
| Archive rows are `KNOWN_AT_UNVERIFIED` and "kept out of anything that decides Rank 1", yet the ML that decides Rank 1 trains on them | CURRENT_RULES §5 R28 v PRIMARY protocol | ML-06 known-at convention; amend R28 |
| Read-only pinned operator v mandatory local execution | CURRENT_RULES §1 v ML_EXECUTION §1 | ML-07 |
| Analyst lane labelled `UNCALIBRATED_ANALYST_SCENARIO / NOT_PRIMARY`, but the template and `verify_log` accept only MODEL_ASSISTED_PRIMARY_V3, UNCALIBRATED_QUALITATIVE or NO_FORECAST | RESEARCH_COMPLETION §3B v CARD_AND_LOG_TEMPLATES line 95 / `execution.py` | Add `UNCALIBRATED_ANALYST_PRIMARY` as a valid status with its own cohort, or define how analyst p maps to card status |
| Most new cards will be analyst or qualitative (low ML coverage), but analyst p is "never T2 model wins" and qualitative ranks get no proper score | CURRENT_RULES §2/§7 | State plainly which numbers count. Recommendation: analyst p is primary where ML is unsupported, in its own cohort, with proper scores |
| "No freeze/no separate cutoff" v "recheck immediately before freeze" and freeze steps | TIMING v prompt 1 / CURRENT_RULES §5 workflow step 3 | Define "freeze" once as "issue-time snapshot" |
| Material unfitted lineup effects require NO_FORECAST, yet model-assisted primary is mandatory and has no lineup features | CURRENT_RULES §7 v PRIMARY §5 | ML-08, plus an explicit interim rule |

### GOV-05 · MEDIUM · Operators drift from the rules

- **Evidence:** P-585–P-589 were issued under `SUPPLIED_FIRST_V1 / SF-2`, a proposal (PROMPT_1_SUPPLIED_FIRST_EXTENDED_2026-10-14.md) that was not adopted. They were imported as a "separate descriptive cohort". P-586 was issued 3.98 minutes after the scheduled start.
- **Fix:**
  - A machine **card linter** (`python -m ml lint-card`, allowed under the `ml/` code exception). It checks required fields, allowed status values, current policy ID, timing class, the P-ID sequence and the absence of market fields.
  - Prompt 4 import runs it and reports violations before import.
  - Pair it with GOV-02: a short spec is followable.

### GOV-06 · MEDIUM · The controlled prompt file is being used as the request form

- **Evidence:** the uncommitted diff to `research/prompts/1_GAME_CARD.md` replaces the "## Upcoming game" headings and "Inactive template" guards with live event text. Today that is KBL, India v WI T20I, Real Salt Lake v San Jose and Zidanšek v Steur. It also drops "immediately before freeze".
- **Impact:** if committed, event data enters a controlled prompt and the section structure the prompt relies on breaks. Every edit also looks like a prompt version change.
- **Fix:** a separate `research/requests/REQUEST_<date>.md` (or a block pasted into chat) that prompt 1 reads. Keep 1_GAME_CARD.md immutable between releases. **You may want to revert or stash that diff before any commit.** This audit left it untouched.

---

## 5. Research and prediction process findings

### RES-01 · HIGH · Supplied lines are near 50/50 by construction; the method needs an abstain option and honest expectations

- **Evidence:**
  - P-586's supplied lines priced at 58.4% / 53.3% (Rank 1/2).
  - Last retrospective: the 85% counted rate was mechanical (covering pairs; skill −0.03); the Rank-1 gate passed 0/20.
  - Latest paired cohort: card Brier 0.2517 v baseline 0.2295 (n = 4 rows).
  - Card calibration overall: slope 0.83 (overconfident), resolution 0.018.
  - The EPL model is about 0.013 Brier short of an efficient benchmark (ML-19).
- **Impact:** when contracts are supplied as balanced pairs, a forecaster without an informational edge wins about 50–55% of top-two rows. Ranking "the most likely" of four balanced rows mostly picks noise. Headline hit rates are dominated by line construction.
- **Fix:**
  1. Make the Rank-1 gate an **abstain trigger**: no gate PASS means the card issues `NO_PICK` (research retained) rather than a counted low-confidence pick. Report gated and ungated cohorts separately.
  2. Make the headline metric paired Brier against a frozen baseline, with hit rate secondary.
  3. Add a registered **shrinkage shadow** for analyst p: p_shadow = BASELINE_P + 0.7 × (p − BASELINE_P), testing whether analyst conviction is over-extended (slope 0.83).

### RES-02 · HIGH · Research after the start invites hindsight

- **Evidence:** TIMING v2 and RESEARCH_COMPLETION allow research to continue after the scheduled or actual start; the T2 cohort still logs post-start issues (SCV §9). P-586 was issued after the scheduled tip with `LATE_START_UNVERIFIED`.
- **Fix:**
  - Headline T2 and proper-score cohorts count **only verified-PREGAME issues**.
  - Post-start issues are retained but excluded from every headline number and from any learning or feedback.
  - A clean-inputs label does not make a post-start issue count.
  - Add a soft research timebox (e.g. a 90-minute budget per card) to discourage late issuance; this is not a forced freeze.

### RES-03 · MEDIUM · Analyst cards use free-hand centres

- **Evidence:** P-586: "base subjective shrink to Bah 93, Man 83"; fixed 0.25/0.50/0.25 three-case mixtures; widths chosen by hand (SD 20 / 16).
- **Fix:** a deterministic analyst recipe for unsupported competitions.
  - Centre: TB-1-MD with the toolkit's k-shrinkage on recovered L5–L20 history.
  - Width: from the league table, or the nearest same-sport profile labelled UNVALIDATED.
  - Hand adjustments go only in the adjustment table, capped (e.g. ≤0.25 SD), and the unadjusted p is always printed and scored as a shadow (SHADOW_BASE_ONLY already exists).

### RES-04 · MEDIUM · Availability research is mandatory, exhaustive and numerically unused

- **Evidence:** AVAIL-v2 requires both sides' starters, bench and absences through a five-step escalation, including local-language searches for obscure leagues, on every card. No model or recipe consumes it (ML-08).
- **Fix:** tier the work by materiality.
  - Always confirm the decisive single inputs: starting pitcher, starting goalie, star players (top 2 by minutes or usage per side), the cricket XI and toss.
  - Run the full escalation only when a material absence is suspected.
  - Feed confirmed material absences into adapters (ML-08) or a capped analyst adjustment.

### RES-05 · MEDIUM · The learning system accumulates without closing

- **Evidence:** LEARNING_REGISTER has 356 lessons; HYPOTHESIS_REGISTER has 21 PROPOSED_NOT_TESTED and 8 BLOCKED_DESIGN; several rules trace back to single losses (R1 reviews).
- **Fix:**
  - Each lesson must map to (a) a registered test, (b) an implemented control, or (c) an archive entry with a reason.
  - Cap active hypotheses at about 5, each with a preregistered sample size from SCORING §5 inputs.
  - Run a quarterly pruning pass.

### RES-06 · MEDIUM · Card size and custody overhead

- **Evidence:** Combined Log Part 7 is 1.72 MB for about 33 cards (≈50 KB per card); the P-585 tennis card is about 37 KB; custody and receipt prose dominate.
- **Fix:**
  - Card core at most about 1,500 words: decision block, distribution, evidence summary, settlement capture.
  - Evidence and custody go to sidecar files or CSV manifests referenced by hash.
  - Combined Logs carry cores plus pointers.

### RES-07 · LOW · Settlement and source practice — keep

The settlement-from-feed rule, evidence grades A–X, revision chains and synthetic-content guard are good and should be preserved through any simplification.

---

## 6. Evaluation and statistics findings

### EVAL-01 · MEDIUM · The comparator sits inside the model

- **Evidence:** BASELINE_P is the LEAGUE_BASELINE expert, which is also one of the three mixed experts. For balanced supplied lines it is close to 0.5 and easy to beat on winners, uninformative on handicaps.
- **Fix:** keep BASELINE_LEAGUE_V1 as the floor, and add TB-1 (team, season-to-date) as the **primary comparator** for paired Brier. Value is shown by beating a simple team model, not a team-blind one.

### EVAL-02 · MEDIUM · Cohort fragmentation

- **Evidence:** cohorts are split by policy version × timing × gate × evidence × family, with at least 8 weeks per cohort.
- **Fix:** preregister one primary endpoint (paired Brier v TB-1, event-weighted, week-clustered) pooled across sports under one frozen release (GOV-01). Everything else is exploratory.

### EVAL-03 · LOW · Pooled replay interval

Already noted in the V3 review: competition-weeks were treated as independent. The fix is already designed (shared calendar-week clustering); it just needs the regenerated replay (ML-16).

---

## 7. Data and archive findings

### DATA-01 · HIGH · Archive coverage v requests

- **Folders with data (14 October status):** Soccer 1/31 · Rugby union 0/14 · Tennis 0/2 · Field hockey 0/7 · Cricket T20 1/12 · ODI 1/8 · Tests 1/6 · Ice hockey 3/16 · Basketball 12/28 · Baseball 4/11 · Rugby league 1/8 · College football 1/9 (unusable) · Canadian football 0/3 · AFL 3/3 · State AFL 4/9 · American football 4/5.
- **Fix:** drive prompt 7 from request frequency, not completeness.
  - Priority: MLS, A-League, top-5 European soccer leagues + UCL (scores only); T20I, BBL, The Hundred, PSL (Cricsheet); ATP/WTA (match archives); Super Rugby, URC, Premiership; Super League; KHL/SHL/AHL.
  - Import **observed fields only** (the 14 October rebuild standard), with the integrity gate and fingerprint scan, and never stage the whole tree.

### DATA-02 · MEDIUM · Known defects still in modelled data

| Defect | Status | Fix |
|---|---|---|
| KBO/NPB innings placeholders 2000–2024; KBO/NPB extras shares look low (2.1% / 2.9% in 2022+) | Partly repaired (2025) | Re-derive extras/tie flags from official box scores; until then use only 2025+ for extras parameters |
| EuroLeague OT field 0/1,718; Austria 0/909; Greek 1/812 | Flags fire in current code | Repair from field owners or quarantine |
| Greek dispersion anomalies (1977–85, 2000–06) | Flagged | Trim the fit window |
| College football FBS: 304/783 dates on 01-01; 1900–1960 fabricated stubs | NOT_MODELLED | Quarantine like the Czech/English builds; rebuild observed-only |
| Danish Metal Ligaen CITL −0.076 | Unexplained | Audit the decision and home fields |

### DATA-03 · LOW · Discovery quirks

- `config.py` takes column detection and period format from the **last** season file. A schema change across seasons can misread older seasons.
- Discovery is `lru_cache`d per process, so web-recovered rows added mid-session are not seen.
- **Fix:** detect per file (the loader already does), and clear the cache on new input.

---

## 8. Custody and repository hygiene

| ID | Finding | Fix |
|---|---|---|
| CUS-01 | `.gitattributes` protects only six paths. Combined Log Parts 6–8, GAME_LOG_STATUS_CURRENT, `research/verification/**`, `research/issued_research/**` and `archive/mini_logs/**` rely on this machine's local `.git/info/attributes` (CURRENT_RULES §9) | Owner decision: commit `-text` rules for those paths |
| CUS-02 | `settle()` writes `bundle=str(folder.resolve())`, an absolute `C:\Users\danie\…` path, and `feedback_losses` opens it as given. Not portable across machines or agents | Store repo-relative paths; resolve against the repo root |
| CUS-03 | Every bundle stores a full HISTORY.csv copy (thousands of rows per event), so the repository would grow quickly if bundles are committed (ML-07) | Store history once per competition-day; bundles reference it by SHA-256 |
| CUS-04 | Root `__pycache__/`, empty untracked `runtime/` subfolders | Delete locally (ignored already) |

---

## 9. Recommended order of work

**Phase 0 — owner decisions (no code):**
1. Operating model for ML execution (ML-07): pre-computed fixture bundles run locally, or prompts 1–3 local.
2. Whether ML stays *mandatory* while coverage is low, or *where supported* (recommended).
3. Release cadence and freeze (GOV-01).
4. Headline objective: paired Brier v TB-1, with gate-as-abstain (RES-01).
5. `.gitattributes` scope (CUS-01).
6. Revert or keep the uncommitted 1_GAME_CARD.md edit (GOV-06).

**Phase 1 — correctness (fixes that change probabilities; one release):**
1. ML-01 baseball, ML-02 regulation scores, ML-03 parameter table, ML-04 weighting rule, ML-09 neutral, ML-11 loss, ML-13 new-team prior.
2. ML-06 history export and known-at convention; GOV-04 R28 amendment.
3. ML-16 regenerate development outputs and the V3 replay on the final recipe. Freeze. Start the 8-week clock.

**Phase 2 — make it usable:**
- ML-07 fixture-bundle pipeline, ML-12 selection-in-runtime, GOV-05 card linter, CUS-02/03.

**Phase 3 — coverage by request volume:**
- DATA-01 imports (soccer leagues, T20, tennis), ML-18 adapters (tennis, soccer halves, F5, corners), ML-17 cricket, ML-08 adapters (MLB starting pitcher first, then NHL goalie, then basketball availability).

**Phase 4 — simplification (can run in parallel with 2–3):**
- GOV-02 operator specs and single-source rules, GOV-03 version manifest, RES-06 card size, RES-04 tiered availability, RES-05 register pruning.

**Phase 5 — evaluation:**
- EVAL-01/02 preregistered prospective protocol under the frozen release, ML-10 calibration shadow, RES-01 shrinkage shadow, ML-05 option B only after 50 or more settled rows.

Nothing in this plan certifies predictive skill. It removes known biases, makes the stated method executable, and makes a fair test possible.
