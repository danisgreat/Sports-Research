> **Primary ML/RL owner amendment (15 October 2026):** [PRIMARY_PREDICTION_PROTOCOL](PRIMARY_PREDICTION_PROTOCOL.md) permits the separate receipt-bound primary runtime and its full-information sporting mixture (PRIMARY_HEDGE_MIX_V2, which replaced the Exp3 bandit on 15 October 2026). Older statements below barring all model card inputs describe the prior independent-manual lane and are superseded for this new named lane. Existing historical artifacts remain unqualified; market/decision-lab outputs stay excluded.

# Machine-learning and reinforcement-learning implementation framework

**Prepared:** 14 October 2026, Australia/Sydney. **Status:** written as a PROPOSAL; partly implemented later the same day by framework change [2026-10-14-3](research/verification/framework_change_2026-10-14-3/IMPLEMENTATION.md) under the owner's instructions (see §0). §1–§13 are kept as written, apart from the R4 rows added to §4; where they describe the repository, they describe the base revision. **Base revision:** `main` at `941c5abd3`, authority mode `LOCAL_WORKING_TREE`. The one uncommitted file, `PROMPT_1_SUPPLIED_FIRST_EXTENDED_2026-10-14.md`, is not a control file and was not applied.

**Inputs:**
- three supplied research reports, referred to here as **R1**, **R2** and **R3**:
  - **R1:** "Adding Machine Learning and Reinforcement Learning to the MDS Sports-Research Framework";
  - **R2:** the "deep-research-report" executive plan;
  - **R3:** "Comprehensive Implementation Blueprint … 1.0.0-PROD";
  - **R4** (added 14 October, after the first draft): "Calibration in Sports-Research Models";
- [MODEL_PROBABILITY_ML_RECOMMENDATIONS_2026-10-12.md](MODEL_PROBABILITY_ML_RECOMMENDATIONS_2026-10-12.md), cited below by its item IDs (P01–P07, M01–M05, ML01–ML05, C01–C04, E01–E05). Its arguments are not repeated here.

**How to use this document.**
- **The owner:** read §1, then decide §5 (D1–D5). Nothing in §6–§11 can start before those decisions.
- **An implementing agent:** §11 is the work-package plan, and each package names the prompt (7 or 8) it runs under. §12 is the check catalogue. Every claim about the repository in this document has an evidence pointer; recheck it against the current HEAD before acting.

---

<<STATUS_SECTION>>

---

## 1. Bottom line

1. **The modelling core of all three reports is sound, and the repository already holds it.** All three agree on one event distribution per game, contracts priced from it, strong baselines, chronological validation, and calibration on separate data. That is Rule P4, CURRENT_RULES §7 and the October 12 recommendations. This framework adopts it and does not re-argue it.
2. **The reports are wrong or stale where implementation actually starts:**
   - **Restoring commit `37203fc2b`, as R1 advises, would restore unrepaired code.** It is the last *committed* runtime. The October 9 repair report says v1 league profiles leaked test-season data, among nine other defects. Its repairs and `runtime_h0_v2` receipts appear in none of the 12 local refs (§3, F05).
   - **The archive is not training-ready by its own admission rule.** The canonical export admits 84,486 of 407,796 rows, and almost all of them are MLB and the AFL family. NBA, NHL, NRL, NBL, WNBA, IPL and county cricket have **zero** admitted labels, and the export predates the 12 and 14 October archive repairs (F10).
   - **The betting layer conflicts with the current rules.** That layer is CLV, Kelly staking and RL bet sizing. CURRENT_RULES §5 says *"Do not claim value, edge or staking advice from this framework"*, and MARKET_BLIND excludes odds from research. CLV also needs a price taken at decision time, which a market-blind process never has (F02, §10).
3. **Five owner decisions gate the work (§5).** The recommendations:
   - code runs in a **separate workshop repository**, and only CSV and Markdown outputs with receipts enter this one;
   - model outputs start as **SHADOW only**;
   - market data is used **at most as a post-settlement benchmark**;
   - **no staking or RL inside this repository**.
4. **Expect modest gains, mostly in coherence and honest measurement.**
   - The hand team baseline TB-1-MD already matches the old tool within ±0.005 Brier (PROBABILITY_TOOLKIT §4.4). The cards already roughly match a fitted model: 0.2438 against 0.2505, not significant (F07).
   - The realistic value of fitted models is coherent, reproducible prices for every contract at once; correct widths and dispersion; and paired measurement against baselines.
   - Large accuracy gains are not likely. MLB, NHL and most totals show little resolution, and cricket first-innings skill is undemonstrated.
5. **RL has no forecasting role here.** Outcomes do not depend on the forecaster's actions. RL could only size or time bets, and that is outside this framework unless the owner decides otherwise (D3).
6. **Timing.**
   - **Leagues that can start a shadow lane now:** NBL, EPL, NHL and NFL are in season. The NBA starts in late October. The BBL starts in December. AFL, NRL and IPL start in March 2027. Check every schedule before relying on it.
   - **Under the register's two-stage design**, a confirmatory result needs at least an 8-week pilot plus an 8-week stage 2, so at least 16 weeks after a shadow lane starts. It is `INFEASIBLE_AT_THIS_EFFECT` if the sized stage 2 exceeds 52 weeks (HYPOTHESIS_REGISTER, October 12 v3 amendment).

---

## 2. Reading receipt

Mode `LOCAL_WORKING_TREE`, branch `main`, HEAD `941c5abd3`, read 14 October 2026 (+11:00). No control file had uncommitted differences.

| Read in full | Read in part (sections named) |
|---|---|
| CURRENT_STATE, METHOD, CURRENT_RULES, SCORING_AND_VALIDATION, CONTRIBUTING, README, `research/prompts/8_IMPROVE_THE_FRAMEWORK.md`, `runtime/README.md`, MODEL_PROBABILITY_ML_RECOMMENDATIONS_2026-10-12, archived NUMERICAL_MODEL_REGISTER, H0_DATASET_CARD, MARKET_BENCHMARK_LEDGER, `research/verification/prediction_repairs_2026-10-09/REPORT.md`, `Previous Sports Results/_canonical/README.md`, LICENSE | SELECTION_RULES (outline, §9); HYPOTHESIS_REGISTER (outline, Oct 11 and Oct 12 amendments, XCARD, RET tables, "How a hypothesis is tested without code"); PROBABILITY_TOOLKIT (§4, §7, §8, outline); RULES_CRICKET (§0); ARCHIVE_USE_GUIDE (keyword search, §8 table); SOURCES (keyword search for data, odds and licence routes); VERIFICATION_PROTOCOL (§6, §7); BASE_RATES_REGISTER §7.6, §7.8; ACTIVE_FILE_INDEX §1–§2 head; archived FRAMEWORK_RETROSPECTIVE_2026-10-09 (keyword search); CHANGELOG headings; LEARNING_REGISTER L-20260926-28 |

**Not read:** CARD_AND_LOG_TEMPLATES, the sport rule files other than cricket §0, LEAGUE_PROFILES, the Combined Logs. These need a full read before any prompt-8 change that touches card formats (WP-01).

**Tools used outside the repository, as CURRENT_RULES §0 requires to be disclosed:**
- `git` queries.
- Two read-only Python summaries of the local-only `_canonical/events.csv`. They were run from the session scratchpad, not stored in the repository. Each counted rows, `training_eligible` and `exclusion_reasons` per `competition_id` with Python's standard `csv` module.
- One web fetch of the Cricsheet register page.
- One web search on Australian in-play betting law.

---

## 3. Verified state of the repository

| ID | Fact | Evidence |
|---|---|---|
| F01 | Authority is MDS-2026.10.12-v11.0 · CR-2026.10.12-R2 · SCV-2026.10.12-v7 · SEL-2026.10.12-v3. R1 targets v9.0, which is stale. | METHOD, CURRENT_STATE |
| F02 | **Rules that bind this programme:**<br>• no code, JSON, notebooks or workflows in the repository; outside helpers are disclosed and their rules written in prose (CURRENT_RULES §0; CONTRIBUTING R07);<br>• SPORTS_ONLY / MARKET_BLIND, with *"Do not claim value, edge or staking advice"* (CURRENT_RULES §5);<br>• *"no retired runtime is restored"* (VERIFICATION_PROTOCOL §6);<br>• restoring the runtime needs an explicit user instruction through prompt 8 (`runtime/README.md`).<br>Prompt 8 itself writes "No code, JSON, notebooks, workflows or fitted-model claims". | the files named |
| F03 | No fitted model exists. Every numeric card is an `UNCALIBRATED_ANALYST_SCENARIO`. | CURRENT_STATE "Models" |
| F04 | The runtime removed on 9 October is intact in `37203fc2b` (parent of removal commit `a64675cf7`). It is 105 files and 584,315 bytes:<br>• 24 shared modules (`dixon_coles`, `ratings`, `calibration`, `distributional`, `stacking`, `splits`, `evaluation`, `endpoints`, `contracts` and others);<br>• 9 sport engines;<br>• 45 test files across `runtime/tests` and `research/tests`;<br>• the archive builder `research/src/archive.py` and Cricsheet parsers. | `git ls-tree 37203fc2b` |
| F05 | **The 9 October repairs were never committed.**<br>• The repair report lists ten defects. Among them: league profiles leaking test-season data; draws excluded inconsistently; fitted artifacts not loaded by the card generator; NHL OT/SO goals used as regulation goals; MLB doubleheaders collapsed; zero probabilities dropped.<br>• It cites corrected receipts in `research/model_builds/runtime_h0_v2/`. Yet it states "Build measurements and validation results are being completed before this report is finalized", and it was committed only after the code was removed (`49577fbc6`).<br>• None of `IDENTITY_INSUFFICIENT_CAL`, `runtime_h0_v2` or the repair code appears in any of the 12 local refs. Those include `main`, `backup/local-work-2026-10-09`, `session/2026-10-09-rules-settlement-review`, `origin/claude/dreamy-heisenberg-wd4bjb` and six Codex checkpoint trees.<br>• The local `research/model_builds/runtime_h0*` folders are empty.<br>• Whether a copy exists outside git is unknown.<br>**Consequence:** `runtime/README.md`'s "Last working state: `37203fc2b`" is accurate only as the last *committed* state. | `git log --all`, `git grep` per ref; report text |
| F06 | **The v1 receipts at `37203fc2b`:**<br>• 7 leagues, 300 test predictions each.<br>• Home-win interval below zero: AFL and EPL only. Margin cover: AFL, EPL and MLB. Totals: none.<br>• Boosted challenger: acceptance `met: false`, 0 of 4 sports.<br>• These receipts used the profiles F05 calls leaky, so they are optimistic, not conservative. | retrospective §5.8 ML-03; `runtime_h0/challenger/INDEX.json` at `37203fc2b` |
| F07 | **The September tools lineage** (TB-1, A1, RM-1; removed with `tools/`):<br>• On 98 contracts from 54 cards: card 0.2438, A1 0.2505, population 0.2680. Card − A1 = −0.007 [−0.025, +0.011].<br>• TB-1-MD is now a team comparator printed as `TEAM_BASELINE_P`, never `BASELINE_P`.<br>• Its hand-versus-tool validation is historical, and "independent game-level replication is still needed". | LEARNING_REGISTER L-20260926-28; PROBABILITY_TOOLKIT §4 and §4.4 |
| F08 | **Predictability map**, the share of games with a favourite ≥ 0.70 and how often it won:<br>• AFL: 39% of games, 90.6% won;<br>• basketball: 26–29% of games, 80–84% won;<br>• NFL: 27% of games, 73.1% won;<br>• NRL: 19% of games, 68.3% won;<br>• NHL: 6% of games;<br>• MLB: 0% of games.<br>Totals rarely reach 0.70. | BASE_RATES_REGISTER §7.8 |
| F09 | **Prospective evidence is minimal:**<br>• v10/v11 has 4 retained events, with paired Brier card 0.18742 against baseline 0.18813: `INSUFFICIENT_EVIDENCE`.<br>• FC10/FC11 designs are registered at `STAGE_1_PENDING`. | CURRENT_STATE; HYPOTHESIS_REGISTER |
| F10 | **Canonical export** (`Previous Sports Results/_canonical/events.csv`; local-only, git-excluded, built 2026-10-05):<br>• 407,796 rows; 84,486 `training_eligible = true`.<br>• Eligible rows: MLB 65,008 · AFL 16,637 · VFL 905 · AFLW 708 · VFLW 459 · SANFL 384 · WAFL 384 · NFL 1.<br>• **Zero** eligible rows for NBA, NHL, NRL, NBL, WNBA, KBO, NPB, IPL and county cricket. The dominant reason is `missing_exact_result_source`. NHL also has `invalid_source_start_time`; IPL and county also have `missing_numeric_team_scores`.<br>• The export predates the EPL/Czech rebuild (12 Oct) and the basketball rebuild (14 Oct).<br>• It still contains Austrian and Greek basketball, now flagged `SUSPECTED_DEFAULT` for start times.<br>• Its builder was removed, so it cannot be rebuilt inside the repository. | read-only summary (§2); canonical README; ARCHIVE_USE_GUIDE §8 |
| F11 | **Raw archive:**<br>• 40 of 172 competition folders hold rows: 522,048 logical rows, or 500,328 excluding alias copies.<br>• Tennis, rugby union and the soccer leagues other than the EPL are header-only. | ACTIVE_FILE_INDEX §2; ARCHIVE_USE_GUIDE |
| F12 | **Cricket data:**<br>• The archive holds scorecard-level rows for IPL, ODI internationals and the County Championship. IPL has toss winner and decision, innings runs, wickets and overs, target and method.<br>• **No ball-by-ball data is local.** `research/data/cricsheet_odi/` holds a README only.<br>• Cricsheet routes are registered (SOURCES lines 414, 1044, 1095, 1232).<br>**Track record:**<br>• 34 decisions won 64.7% at 0.630, reliability 0.022, the worst of any sport with n ≥ 30;<br>• an IPL team-strength model scored Brier 0.254 against 0.250 for a coin flip;<br>• the A1 v1 model was worse than the format mean on totals.<br>The chase censoring rule was corrected on 2026-10-12. | RULES_CRICKET §0.4 and shadow note; PROBABILITY_TOOLKIT §7 |
| F13 | **Odds-bearing files sit inside the repository folder:**<br>• `research/data/benchmark/football_data/2019-20.csv` … `2026-27.csv`: 8 files, 120 columns, including Bet365, Pinnacle, Betfair, maximum, average and closing prices.<br>• They are untracked and git-excluded (`.git/info/exclude` line 27).<br>• SOURCES allows football-data only as a "post-settlement closing benchmark … in the quarantined research workspace … local-only". CONTRIBUTING R07 says such captures "stay **outside** the repository folder".<br>• The two documents disagree on location. Nothing is at risk of commit today only because of a machine-local exclude. | `git check-ignore`; SOURCES §1320; CONTRIBUTING |
| F14 | **The market benchmark ledger is archived:**<br>• archived 2026-10-14, with zero rows;<br>• status LEARNING_ONLY;<br>• firewall: entered by hand after settlement, no-vig probability only, outside the reading gate, and may not influence any rule. | archived MARKET_BENCHMARK_LEDGER |
| F15 | **Licence error:** SOURCES line 63 lists Cricsheet as "ODbL 1.0". Cricsheet's register page states the **Open Data Commons Attribution License** (ODC-By). This matters because ODbL is share-alike and ODC-By is not. | SOURCES; cricsheet.org/register |
| F16 | **Prospective card volume is small.** The register's feasibility notes assume about 20 cards a week, and several XCARD designs are "not feasible within 26 weeks". Card-only evaluation of a model is therefore slow. A full-league shadow, where every fixture is priced, is the only feasible route to power. | HYPOTHESIS_REGISTER XCARD table |

---

## 4. Assessment of the three supplied reports

Verdicts: **CONFIRMED** · **CONFIRMED_WITH_CAVEAT** · **STALE** · **INCORRECT** · **CONFLICTS_WITH_RULES** · **UNSUPPORTED** (no evidence offered) · **UNVERIFIED** (not checked in this pass; not load-bearing unless stated).

| # | Source | Claim | Verdict | Evidence and disposition |
|---|---|---|---|---|
| A01 | R1 | Method v9.0 / CR-R5 / SCV v5 | STALE | Now v11.0 / R2 / v7 (F01). |
| A02 | R1 | "Restore code … from commit `37203fc2b` as a starting point" | INCORRECT as stated | It restores v1 with known leakage, and the repairs are missing (F05). Port selectively, re-implement each repair with a regression test (Appendix A), and re-run every receipt. |
| A03 | R1 | TB-1 improved side Brier by 5–19% in NBA…EPL, with nothing in MLB/NHL | CONFIRMED_WITH_CAVEAT | Historical tool-era result:<br>• NRL sides were later withdrawn (interval crossed 0);<br>• TB-1 was *worse* than the population on EPL totals;<br>• TB-1-MD is a comparator, never `BASELINE_P` (F07). |
| A04 | R1 | Card 0.2438 / A1 0.2505 / population 0.2680 | CONFIRMED | L-20260926-28. |
| A05 | R1 | IPL model has "no demonstrated skill" | CONFIRMED | RULES_CRICKET §0 shadow note. |
| A06 | R1 | Predictability map figures | CONFIRMED | BASE_RATES §7.8 (F08). |
| A07 | R1 | RM-1 lifted held-out Rank 1 from 64.2% to 68.9%; stack analyst p with model output | UNVERIFIED and CONFLICTS | Not re-verified in the current tree. SCORING §1 states *"q is never an event probability"*, so RM-1 q cannot enter a probability stack. Analyst p_card can be a stack input only on rows where it was frozen before the event. |
| A08 | R1 | MARKET_BENCHMARK_LEDGER records closing prices after settlement | CONFIRMED_WITH_CAVEAT | Archived; zero rows; it stores no-vig probabilities, not prices (F14). |
| A09 | R1 | New rule "M1 Market Layer": read odds after the freeze for CLV and staking | CONFLICTS_WITH_RULES | CURRENT_RULES §5 forbids staking advice. CLV needs a price taken at a decision. The only compatible part is the post-settlement scoring comparison (D3 option ii). |
| A10 | R1 | Cricsheet JSON is the maintained format; coverage counts | CONFIRMED_WITH_CAVEAT | Format claim is plausible. The licence is ODC-By (F15). Coverage counts are UNVERIFIED and not needed. |
| A11 | R1 | Walsh & Joshi corrigendum ROI; KellyBench (April 2026); Moskowitz (2021); Kaunitz et al.; BetStop and ACMA figures; credit-card ban date | UNVERIFIED | None is load-bearing. Only the decision project (§10) would rely on any of them, so verify there. |
| A12 | R1 | Online in-play betting is restricted under the IGA | CONFIRMED | ACMA enforcement reports and trade coverage, 2021–2026 (Appendix C). Exceptions: phone and place-based. |
| A13 | R1 | Dixon–Coles code with a per-match loop inside L-BFGS-B | CONFIRMED_WITH_CAVEAT | The 9 October retrospective (F-ML-3) found exactly this pattern impractical for multi-season fits. Vectorise; analytic gradients; no silent fallback (F-ML-2). |
| A14 | R2 | "Previous Sports Results" probably contains market odds for training | INCORRECT | The archive holds sporting fields. Odds-bearing files are local-only benchmark captures (F13) and must never be features. |
| A15 | R2 | Implied probabilities, opening/live lines and liquidity as model features; "use odds at game start (not … closing odds)" | CONFLICTS_WITH_RULES and INCORRECT | MARKET_BLIND forbids it. The phrase is also self-contradictory: odds at game start *are* the closing odds. |
| A16 | R2 | Spread as its own binary classifier; total as its own regression | CONFLICTS_WITH_RULES | P4 and CURRENT_RULES §7 require compatible joint constructions. Separate models need joint reconstruction (P03). |
| A17 | R2 | L5/L10/L20 rolling features | CONFIRMED_WITH_CAVEAT | v11 reads them as one shrunk rate (PR-01; FC11-FORM-v1 registered). The windows overlap. Repository evidence shows no bounce-back and the last game as the worst predictor. As ML features: regularise, and test their incremental value. |
| A18 | R2 | Kelly "edge = p − (1−p)/odds; fraction = Kelly × edge" | INCORRECT | Correct full Kelly for decimal odds o: f\* = (p·o − 1)/(o − 1). See Appendix B for the push case. |
| A19 | R2 | DQN/policy-gradient staking in 5–7 days; REST API; Feast store; pickle artifacts | UNSUPPORTED and CONFLICTS | Pickle was flagged unsafe (F-ML-6). An API or feature store contradicts the user's reason for MD-only (cards run in chat). RL timing is unrealistic (§10). |
| A20 | R3 | Cricket reliability penalty 0.022 on 34 rows | CONFIRMED | RULES_CRICKET §0.4. |
| A21 | R3 | IPL v1 Brier 0.254 against 0.250 | CONFIRMED | RULES_CRICKET §0. |
| A22 | R3 | Coherence identities: T ≥ \|M\|, T ≡ M (mod 2), Var(T)+Var(M) = 2[Var(H)+Var(A)] | CONFIRMED | Algebra. Already P03. |
| A23 | R3 | Chase total within [target, target + 5] | CONFIRMED_WITH_CAVEAT | The direction is the 2026-10-12 correction (PROBABILITY_TOOLKIT §7). Derive the upper bound from the competition's playing conditions for the winning delivery (extras, boundary); do not hard-code it. |
| A24 | R3 | Event-level reweighting calibrator "preserves monotonicity across all handicap and total ladders" | CONFIRMED_WITH_CAVEAT | It preserves normalisation and monotonicity, but it **changes** total and handicap probabilities. C03's example moves Over 1.5 from 0.55 to 0.536. Evaluate every derived family after calibration. |
| A25 | R3 | Soil type, Hawk-Eye seam and spin degrees, strip-use count, turf species, air density, boundary-axis wind; dew factor index | INCORRECT / not available | Hawk-Eye data is proprietary. Soil and strip data are rarely published and almost never timestamped, so they fail the known-at rule (R28). The DFI formula is inverted: a larger T − T_dew means drier air and *less* dew. "0.8–1.5 runs per over" and "+14.2% sixes" are unsourced: register them as hypotheses at most. |
| A26 | R3 | `CricketFirstInningsEngine` labelled production | INCORRECT label | Defects:<br>• hand-set, unfitted transition probabilities;<br>• bowlers rotated by index, ignoring the spell quota the text claims;<br>• wides and no-balls treated identically, with no free hit;<br>• global, unseeded random state;<br>• independent balls, which under-disperse totals. |
| A27 | R3 | "Why fractional Kelly fails and RL succeeds" | UNSUPPORTED | Shrunk fractional Kelly is the published answer to estimation risk (Baker & McHale 2013, cited in R1). R3 offers no evidence that RL beats it. R1's two RL examples did not generalise. |
| A28 | R3 | Gymnasium staking environment | INCORRECT design | Defects:<br>• CLV from raw, un-de-vigged prices;<br>• CLV and settled P&L both rewarded for the same bet in the same step;<br>• the "CVaR penalty" is a linear drawdown penalty, not CVaR;<br>• caps of 5% per contract and 20% per slate (R1 uses 2% and 10%);<br>• "covariance" is claimed but no correlation is modelled. |
| A29 | R3 | Acceptance gates: reliability < 0.005; CLV ≥ 1.5% at p < 0.01 over N ≥ 250; Calmar > 2 | UNSUPPORTED | Not sized and not tied to bins or n. SCORING §4–§5 require predeclared tolerances and sized samples. |
| A30 | R3 | Purged walk-forward with same-strip/48-hour embargo | CONFIRMED_WITH_CAVEAT | Chronological folds, yes. The real control is the availability audit (E02). An arbitrary embargo does not substitute for it. |
| A31 | R3 | "Post-Audit v11"; overshoot "corrected 2026-10-12" | CONFIRMED | F01; PROBABILITY_TOOLKIT §7. |
| A32 | R4 | The repository holds calibration artifacts: freeze receipts, shadow forecasts, `calibration.yml`, `pipeline.py` | INCORRECT | At the base revision none existed. Freeze receipts and shadow forecasts appeared only in the fabricated, reverted commit `0e5685e57`. No YAML or pipeline file exists, and JSON/YAML are not allowed. Genuine files are now produced by `ml/` with real receipts. |
| A33 | R4 | "No systematic calibration step documented in the code" | CONFIRMED (at base) | Implemented: coherent winner reweighting (`ScoreGrid.reweight_winner`) and a previous-season-only logistic recalibration experiment for every model (ML-CAL-WIN). |
| A34 | R4 | Use reliability diagrams, Brier, CRPS, calibration-in-the-large, slope and confidence intervals on chronological splits | CONFIRMED | Implemented in `ml/core/metrics.py` and applied to every model and to the cards' own history (`research/model_shadow/CARD_CALIBRATION/REPORT.md`). |
| A35 | R4 | "Moneyline H/A/D sum > 1 due to vigorish"; home win and draw "should adjust together" | INCORRECT / conflated | A model's outcome probabilities sum to exactly 1; only market-implied probabilities exceed 1 (the overround). Joint adjustment is what the class reweighting already does. |
| A36 | R4 | Isotonic or Platt on rolling windows; "at least several hundred cases per market"; Hosmer–Lemeshow, Diebold–Mariano, BBQ | CONFIRMED_WITH_CAVEAT | A sample-size rule does not guarantee calibration (C02), and Hosmer–Lemeshow depends on the binning. The 200-game floor in the experiment is a pragmatic guard, not a guarantee. Acceptance stays with the register's two-stage design. |
| A37 | R4 | Example calibration table; Mermaid timeline | ILLUSTRATIVE ONLY | The table's numbers are the report's own invented examples and must never be cited as results. The timeline is not adopted. |
| A38 | R4 | Pinnacle/Betfair closing odds and Sportradar/Opta as priority sources | CONFLICTS_WITH_RULES (odds) | Odds enter only post-settlement or in the firewalled decision lab (CURRENT_RULES §5a); results come from SOURCES routes. |
| A39 | R4 | scikit-learn code (`calibration_curve`, `IsotonicRegression`) | NOTE | Not used. Dependencies are kept to numpy, scipy and pandas; the equivalent functions are implemented and tested. |

**Net (R4 added later):** R4's diagnostic recommendations are sound, but it assumes artifacts that never existed. R1 is the most accurate and self-limiting of the first three, apart from A02 and its market and staking layer. R2 is generic and assumes code and odds that do not exist here. R3 has correct mathematics in §1 but adds unavailable data, untested constants and an RL design with material defects.

---

## 5. Decisions the owner must make

Each decision is a user instruction that prompt 8 then implements. None is made by this document.

### D1. Where model code runs

| Option | What it means | Consequences |
|---|---|---|
| A. Hand-only (status quo) | No fitted model. ML is limited to tables an agent can apply by hand. | Possible now: data readiness, design registration, TB-1-MD. ML and RL as the reports describe them are not possible. |
| **B. External workshop (recommended)** | Code, environments and tests live in a **separate private repository outside this folder**. Only CSV and Markdown outputs with receipts enter this repository (§6). Cards never depend on code. | Fits CURRENT_RULES §0 and CONTRIBUTING R07 literally. It keeps the user's 2026-09-28 reason (cards run in chat) intact. It still needs prompt 8 to define the shadow lane, its folder and its reading-gate exclusion. Opaque models (GBMs, simulators) can never be reproduced by hand (§6.7). |
| C. Restore code here | Reverse the Markdown-only rule and bring back `runtime/`, CI and validators. | Reverses CURRENT_RULES §0, CONTRIBUTING, VERIFICATION_PROTOCOL §6 and prompt 8. It also brings back the maintenance burden the 9 October retrospective documented: 13 manifests, snapshot-coupled verifiers and a broken import that blocked CI. **Not recommended.** |

### D2. What a model output may do

| Status | Meaning | Required before entering |
|---|---|---|
| **SHADOW (recommended start)** | Frozen independently before the event. Card writers must not read it before their own freeze. Scored on its own. | D1 = B, plus a prompt-8 change defining the lane (WP-01). |
| REFERENCE | May be printed on a card as `MODEL_P` beside `p_card`. Because it can move p_card, it changes how p is produced. | Owner order, plus the §9.5 bar. |
| ANCHOR | `p_card` starts from `MODEL_P`; analyst changes are logged as deltas in the adjustment table. | Owner order, plus the §9.5 bar on identical card rows. |

The owner's standing rule (2026-09-27) is to make a model change only if it is "absolutely going to make it better". Every promotion is therefore a separate MODEL_CHANGE, per model and per endpoint.

### D3. Market data

| Option | Compatible with current rules? | Recommendation |
|---|---|---|
| i. None (status quo) | Yes | Acceptable. |
| **ii. Post-settlement benchmark only** | Yes, under the archived ledger's firewall: entered after settlement, no-vig probability only, outside the reading gate, never cited by a rule | **Recommended if** the owner wants to know whether the cards or models beat the closing market. Restoring the ledger is a prompt-8 change (WP-14). |
| iii. Pre-decision prices, CLV, staking, RL | **No**: CURRENT_RULES §5 and the LICENSE notice ("Nothing in this repository is betting advice") | Not in this repository. If wanted, a separate decision project with the prerequisites and legal constraints in §10. |

### D4. Which historical labels may train a model

| Option | Effect |
|---|---|
| Strict | Only `training_eligible` rows (F10): MLB and the AFL family today. Other leagues wait for WP-04, receipt verification. |
| **Tiered (recommended)** | **LABEL_A** = receipt-verified. **LABEL_B** = observed-field archive rows that pass their `DATA_PROVENANCE.md` and ARCHIVE_USE_GUIDE §8–§9 checks. LABEL_B may train development models, with the label printed on every model card. Promotion evidence comes only from prospective, feed-settled shadows (§9). |

### D5. Scope and order

Recommended first wave:
- **EPL, NBA and NBL** (in season or about to start; TB-1-MD has resolution there).
- **AFL and IPL first-innings** in development now, for a March 2027 shadow start.
- **MLB** as a pipeline test bed only, because it has the most LABEL_A data and the least expected gain.

Defer NHL, NRL, the soccer leagues outside the EPL (they need football-data sporting fields captured with odds columns stripped) and KBO/NPB. Defer tennis and rugby union until a data route exists (§7.2).

---

## 6. Target architecture (assuming D1 = B, D2 = SHADOW)

### 6.1 Data flow

```text
 THIS REPOSITORY (Markdown / CSV / text)                 MODEL WORKSHOP (separate private repository, outside this folder)
 ─────────────────────────────────────────               ───────────────────────────────────────────────────────────────────
 Previous Sports Results/  ── read at a pinned SHA ──►   ingest ─► label admission (A/B) ─► features (as_of cutoff)
 SOURCES.md routes          ── captures stay outside ─►        ─► fit (train) ─► tune (tune block) ─► calibrate (cal block)
                                                                ─► price every contract from ONE event distribution
                                                                ─► freeze: write CSV, SHA-256 it
 research/model_shadow/<model_id>/                                         │
   MODEL_CARD.md, PARAMETERS.md            ◄── Markdown ───────────────────┤
   FREEZE_RECEIPTS.md   ◄── hash committed BEFORE the scheduled start ─────┤
   SHADOW_FORECASTS_<yyyy-ww>.csv  ◄── contents committed AFTER the start ─┘
   SHADOW_SETTLEMENTS.csv  ◄── settled from the feed (evidence A/B), revision chains as CURRENT_RULES §8
 Prompts 1–3 (cards): never read research/model_shadow/ before their own freeze
 Prompts 3, 6 (settle, retrospective): score shadow rows against BASELINE_P, TEAM_BASELINE_P and p_card on identical rows
```

**Commit, then reveal.** Prompts 1–3 read published `main`. A shadow forecast published before the event could therefore anchor a card writer. So the SHA-256 of the frozen file is committed before the first scheduled start in the file, and the contents only after it. This is a contamination control, not proof of freeze time: a git SHA and commit time do not prove issue time (CURRENT_RULES §9). Record the push time from the remote as well, and disclose that limit.

### 6.2 Boundary contract

| May cross into this repository | Must never cross |
|---|---|
| CSV forecast and settlement rows (§6.4–§6.5) | Code, notebooks, JSON, YAML, pickles, binaries |
| Markdown model cards and parameter tables | Raw source captures, API dumps, HTML |
| Receipts: workshop commit SHA, input file SHA-256s, archive commit, fit window, cutoff | Any column carrying a price, line movement or market-derived probability (except under D3-ii, in the firewalled benchmark file only) |
| Derived archive tables (for example IPL innings and phase totals) with a `DATA_PROVENANCE.md` written in prose | Fitted parameters with no model card; unversioned outputs |

### 6.3 Repository layout added by WP-01

```text
research/model_shadow/
  README.md                      lane rules, reading-gate exclusion, status table of every model
  <model_id>/                    e.g. EPL-DC-v1, NBA-JOINT-v1, IPL-FI-C1-v1
    MODEL_CARD.md                §6.6
    PARAMETERS.md                hand-applicable parameter tables (HAND_APPLICABLE models only)
    DEVELOPMENT_RESULTS.md       labelled HISTORICAL_DEVELOPMENT
    FREEZE_RECEIPTS.md           one line per frozen file: path, bytes, SHA-256, first scheduled start, commit, push time
    SHADOW_FORECASTS_<yyyy-ww>.csv
    SHADOW_SETTLEMENTS.csv
```

### 6.4 Shadow forecast row (CSV columns)

| Column | Content |
|---|---|
| `shadow_row_id` | `<model_id>:<event_key>:<contract_key>`, unique and never reused |
| `model_id`, `model_version` | e.g. `EPL-DC-v1`, `1.0.0` |
| `event_key` | Competition / season / native ID or labelled surrogate / date (CURRENT_RULES §5) |
| `competition`, `season`, `stage` | as in the archive |
| `scheduled_start_utc`, `cutoff_utc`, `frozen_utc` | ISO 8601 UTC; `frozen_utc < scheduled_start_utc` for PREGAME |
| `endpoint` | e.g. `REGULATION_90`, `FULL_GAME_INCL_OT`, `REGULATION_60`, `FIRST_INNINGS_FULL_LENGTH` |
| `family`, `orientation`, `line` | `MONEYLINE_3WAY` / `MONEYLINE_2WAY` / `HANDICAP` / `TOTAL` / `TEAM_TOTAL` / `FIRST_INNINGS_TOTAL`; `HOME` / `AWAY` / `DRAW` / `OVER` / `UNDER` / `BAT_FIRST`; numeric line or `N/A` |
| `mass_win`, `mass_push`, `mass_loss`, `mass_void` | unconditional masses; void `NOT_ESTIMATED` when not modelled |
| `p_decisive` | W/(W+L); `NOT_COMPUTED` when W+L = 0 |
| `mean_home`, `mean_away`, `sd_margin`, `sd_total`, `cov_home_away` | distribution summary; `N/A` where not meaningful |
| `baseline_p`, `baseline_id` | `BASELINE_LEAGUE_V1` on the identical row (SELECTION_RULES §9), or a precise missing reason |
| `team_baseline_p` | TB-1 on the identical row, or a missing reason |
| `calibration` | `IDENTITY_INSUFFICIENT_CAL` or `<method>:<calibrator_id>` |
| `inputs_status` | lineup `CONFIRMED` / `UNCONFIRMED_MIXTURE` / `NOT_USED`; toss `PRE_TOSS_MIXTURE` / `POST_TOSS`; weather forecast issue time or `NOT_USED` |
| `label_tier_trained_on` | `A`, `B` or `A+B` |
| `workshop_commit`, `data_snapshot_sha256`, `archive_commit` | receipts |
| `status` | `FROZEN`, or `NOT_ISSUED:<reason>` (unknown team, missing input, fit failure). Never a default number |

### 6.5 Shadow settlement row

`shadow_row_id`, `revision`, `parent_revision`, `effective_utc`, `result` (`WIN`/`PUSH`/`LOSS`/`VOID`/`UNRESOLVED`), `observed_value`, `evidence_grade` (SELECTION_RULES §7), `source_url`, `field`, `retrieved_utc`, `reason`. The revision-chain semantics are CURRENT_RULES §8 (R17), unchanged.

### 6.6 Model card: required headings

1. Identity: ID, version, owner, status (SHADOW / REFERENCE / ANCHOR), date.
2. Endpoint and contracts priced, with the WIN/PUSH/LOSS/VOID sets.
3. Population: competitions, seasons, stages, exclusions, label tier.
4. Inputs, each with its known-at rule (§7.3).
5. Method in prose: enough for a reader to check by hand (CONTRIBUTING R07). For HAND_APPLICABLE models, a worked example that reproduces one frozen row with PROBABILITY_TOOLKIT arithmetic.
6. Fitting: folds and dates, tuning choices and the data they used, and the failure behaviour (refuse, never default).
7. Calibration: method, CAL dates, status.
8. Development results (`HISTORICAL_DEVELOPMENT`) against both comparators, with intervals.
9. Prospective results so far, with the stage of the registered test.
10. Known limits, and every check in §12 with its last pass date.

### 6.7 Hand-applicability classes

| Class | Examples | What a chat-run card can do with it |
|---|---|---|
| `HAND_APPLICABLE` | Rating tables (Elo/Glicko); Dixonâ€“Coles attack, defence, home and Ï per team; NB mean and dispersion per team; joint-normal means, SDs and covariance by league | Reproduce any price by hand from `PARAMETERS.md` with PROBABILITY_TOOLKIT Â§1â€“Â§3. This is the only kind of fitted model compatible with the user's reason for Markdown-only operation, if it is ever promoted. |
| `SHADOW_ONLY_OPAQUE` | Gradient boosting, NGBoost, ball-by-ball simulators, stacks | Cannot be reproduced by hand. Usable only as frozen CSV numbers. Promotion beyond REFERENCE needs the owner to accept that a card would depend on a number it cannot recompute. |

---

## 7. Data framework

### 7.1 Label tiers

| Tier | Definition | Use |
|---|---|---|
| LABEL_A | Canonical `training_eligible = true` (receipt-verified result) after the WP-03 rebuild | Training and development; preferred for any published development claim |
| LABEL_B | Observed-field archive rows that pass `DATA_PROVENANCE.md`; `SUSPECTED_DEFAULT` fields, quarantined builds, alias copies and placeholder years excluded | Development training only, labelled; sensitivity check against LABEL_A wherever both exist |
| PROSPECTIVE_SETTLED | Shadow rows settled from the feed with evidence A or B | **The only evidence for promotion** |
| EXCLUDED | Fabricated or quarantined builds; rows with conflicting identity; header-only files | Never |

### 7.2 Readiness by league

| League | Labels today | Missing for first model | Route (SOURCES) | Readiness |
|---|---|---|---|---|
| EPL | LABEL_B (rebuilt from observed fields 2026-10-12, 1975–2026); not in the 10-05 export | Rebuild the export; receipt verification for A | archive; football-data **sporting fields only** | READY for development (B) |
| La Liga, Bundesliga, Serie A, Ligue 1 | Header-only archive | Capture sporting columns outside the repository, strip odds, write provenance | football-data (scores only) | DATA_PENDING |
| NBA / WNBA | LABEL_B; 0 eligible in export | Receipts for A (ESPN or league feeds) | archive; ESPN site API | READY for development (B) |
| NBL | LABEL_B; 2025 dates repaired; 2026 partial snapshot | Owner-sourced scores for 19 single-source 2026 games | archive; ESPN; NBL match API | READY (B), partial current season |
| AFL / AFLW | **LABEL_A** (AFL 16,637; AFLW 708) | AFLW widths `NOT_YET_DERIVED` | archive; fitzRoy route by hand | READY |
| NFL | LABEL_B; 1 eligible | Receipts; strip market columns from nflverse `games.csv` at capture (SOURCES says results columns only) | archive; nflverse | READY for development (B) |
| NRL | LABEL_B | Receipts | archive | READY for development (B), low priority |
| NHL | LABEL_B; start times invalid in export | Start-time repair; OT/SO flags for regulation training (repair report item) | archive; NHL api-web | DATA_PENDING (OT flags) |
| MLB | **LABEL_A** (65,008) | Doubleheader identities (repair report item) | archive; MLB statsapi | READY (test bed) |
| KBO / NPB | LABEL_B; extras `NOT_ESTIMABLE` before 2025 | Line scores; extras 2000–2024 | KBO/NPB owner routes | DATA_PENDING |
| IPL (first innings) | LABEL_B scorecards (≈1,213 rows); 0 eligible (numeric-score mapping) | Cricsheet ball-by-ball for phase models; numeric score mapping in the rebuilt export | Cricsheet IPL (ODC-By) | READY for C0–C2 (B); C3+ after WP-05 |
| BBL, other T20 | Header-only archive (BBL 2024 file empty) | Cricsheet capture | Cricsheet | DATA_PENDING |
| Tennis | Header-only; the Sackmann route returns 404 | A working serve/return data route | none working | NOT_READY |
| Rugby union | Header-only | Any results route | — | NOT_READY |

### 7.3 Known-at rules for features

| Feature | Known-at rule | Historical availability | Allowed use |
|---|---|---|---|
| Ratings and results from earlier games | Strictly earlier event dates; never another event on the forecast date (canonical README date-only contract) | Yes | Train and live |
| Rest days, back-to-backs, schedule density | From earlier dates and the scheduled date | Yes. Dates only in folders whose start times are `SUSPECTED_DEFAULT` | Train and live |
| Travel distance, time zones | Needs observed venue and city | Partial (venue often blank; `neutral_venue` often missing) | Development where observed |
| Home and neutral status | A designated home is not proof of home advantage (canonical README) | Partial | With explicit missingness |
| Regime flags (rule changes) | Known in advance | Yes (BASE_RATES regimes; league rules) | Train and live |
| Confirmed lineups, injuries, starting pitcher, goalie, QB, XI | Publication time required (R28) | **Not as pregame snapshots** (canonical README: actual starters are not historical pregame snapshots) | Prospective capture only. Until a season is captured, lineup effects enter only as declared scenario mixtures (CURRENT_RULES §7), not fitted features |
| Cricket toss and decision | Known at the toss | IPL archive has both columns | Post-toss branch; pre-toss mixture |
| Cricket XI | Announced at the toss | Cricsheet lists actual XIs | Post-toss models only |
| Weather | A forecast issued before the cutoff, never the observation | Depends on the archived-forecast depth of the route; check at capture | Development with archived forecasts only; live from issue-time capture |
| Pitch, strip and dew reports | Usually untimestamped text | Mostly unavailable | Categorical flags only if logged before the toss; prospective only |
| Any price, line, implied probability or market movement | — | — | **Never** (MARKET_BLIND) |

### 7.4 Prospective capture: the only route to lineup-aware models

At every shadow freeze, the workshop stores the inputs it used: lineup status with the source's publication time, the weather forecast with its issue time, and the toss. After a season this forms a training set with true known-at times. Before that, no fitted lineup feature can be validated honestly.

### 7.5 Market data (D3-ii only)

1. Hand entry after settlement only: the no-vig closing probability for the **exact** contract, with the method named. This is the archived ledger's rule set, restored unchanged by prompt 8.
2. A bulk historical comparison (for example EPL 2019-20 to 2025-26 closing prices from the local-only football-data files) is computed **outside the repository**. Only the paired score summary enters: Brier of the model against the no-vig close, by season, with intervals.
3. Raw odds and no-vig rows stay out of the reading gate. No rule, rank, width or learning disposition may cite them.
4. **Resolve F13 first:** either move the files outside the repository folder, as CONTRIBUTING R07 says, or amend R07 to name the excluded quarantine path. This is the owner's choice.

### 7.6 Data-quality controls

Each control is a §12 check:
- duplicate and alias identities;
- doubleheaders;
- score–margin–total arithmetic;
- OT/SO flags;
- stage labels;
- `SUSPECTED_DEFAULT` fields;
- placeholder years;
- two-source disagreement (the repository once graded 17 rows backwards);
- team-name alias collisions;
- market columns present in any file that crosses the boundary.

---

## 8. Modelling framework by contract

### 8.0 Common contract for every model

- **One state distribution.** Every model outputs the joint state distribution, or a seeded sample from it, at the declared endpoint. Contracts are deterministic functions of that state (P01). Store unconditional W/P/L/V masses and p_decisive (P02).
- **Invariants checked on every frozen file (§12):**
  - masses sum to 1;
  - structural zeros stay zero;
  - integer support with T ≥ |M| and T ≡ M (mod 2);
  - ladder monotonicity;
  - covering-pair consistency P(home +k) ≥ P(home win) for k ≥ 0, except in tennis games handicaps (P07);
  - exact push mass on whole lines.
- **Two comparators on every row:** `BASELINE_LEAGUE_V1` (league-only) and `TEAM_BASELINE_P` (TB-1). A fitted model that cannot beat TB-1, which a chat agent can compute by hand, adds code without benefit.
- **Fit failure or an unknown team yields `NOT_ISSUED`**, never a default. This removes the old 1.55/1.20/112 defaults and the silent optimiser fallbacks (F-DST-7, F-ML-2).

### 8.1 Moneylines (winner)

Fix the endpoint first. The examples below need checking against each league's rules file:
- soccer is regulation 1X2;
- NBA and NBL are full game including overtime;
- the NFL regular season allows ties;
- AFL draws and NRL golden-point draws exist;
- NHL is regulation three-way or full game including OT/SO;
- KBO/NPB ties are allowed.

| Level | Model | Role |
|---|---|---|
| L0 | `BASELINE_LEAGUE_V1`: league home/draw/away rates by regime | comparator |
| L1 | TB-1 (PROBABILITY_TOOLKIT §4) | comparator; also replicated in code to close the §4.4 replication gap |
| L2 | Dynamic rating: Elo with a margin-of-victory multiplier, or a time-decayed Bradley–Terry/Davidson (draw-aware), or Glicko-2 where schedules are sparse. Decay and K chosen on the earliest development seasons only | first fitted candidate |
| L3 | The winner masses of the joint score model (§8.2–§8.3) | **the published winner probability**: coherent with handicaps and totals |
| L4 | Challenger: gradient boosting on residuals, started from the L2 rating margin, with known-at features only (§7.3) | SHADOW_ONLY_OPAQUE |

If L2 or L4 beats L3 on winners, transfer the gain by **re-centring the joint margin**: a one-parameter shift so that P(M > 0) equals the better winner probability. Then re-derive handicaps and totals from the shifted joint and record the shift. Never publish a winner probability from one model with handicaps from another.

### 8.2 Handicaps

- **Pricing:** P(M + s > 0), with exact push mass P(M + s = 0) on whole lines. A quarter line is half of each adjacent line, but only when the frozen contract defines it that way.
- **Low-scoring sports:**
  - soccer: Dixon–Coles with time decay ξ chosen by rolling validation, and the τ correction for 0–0, 1–0, 0–1 and 1–1;
  - hockey: regulation bivariate Poisson or negative binomial, with OT/SO resolved separately and an empty-net challenger;
  - baseball: negative-binomial runs per team, with the home final half-inning stopping rule and an extras branch.
- **High-scoring sports:**
  - joint margin–total normal or Student-t, discretised on the integer lattice with parity;
  - basketball: tied regulation mass goes to an explicit overtime branch;
  - NFL: start from the empirical margin distribution of prior seasons, rescaled to the model mean and SD, and check push mass at 3, 7 and 10;
  - AFL: discretised normal first, with a goals-and-behinds (6G + B) challenger;
  - NRL: discretised normal with the golden-point regime.
- **Evaluation:** Brier at each standard ladder line, CRPS on the margin, and push-mass error at key numbers.

### 8.3 Totals

The total comes from the same joint. Width is the hard part, and the repository's own evidence points there:
- basketball total widths ran about 39% too narrow on a 2026-09-24 cohort (n = 7, descriptive; BASE_RATES §7.6);
- NBL totals ran +16.8 on 3 of 3 cards (RET-01).

In order:
1. League level by season, with stale-profile detection (FC10-PROFILE-v1 already registered).
2. Team attack and defence, as in TB-1.
3. Conditional dispersion challenger (P04): negative-binomial φ(x), an NGBoost Normal or NB head, or heteroscedastic regression.

Evaluate by CRPS, PIT histograms and interval coverage, not by Brier at a single line. Expect little: TB-1 total resolution existed only in NBA/WNBA/NBL and La Liga/Bundesliga, and TB-1 was worse than the population on EPL totals.

### 8.4 Cricket first-innings totals

**Contract.** Runs of the team batting first, in the full-length innings. Freeze the void or reduced-overs convention in the contract. When the convention voids reduced innings, model only the full-length branch. Otherwise add an overs-available branch.

**Toss.**
- Pre-toss price: P(A bats first) × F_A + P(B bats first) × F_B. The weights come from toss and decision tendencies, by league and venue, from **prior seasons only**. The archive's toss columns support this.
- Post-toss price: the realised branch only (PROBABILITY_TOOLKIT §7, control 21).

| Level | Model | Data | Gate to build the next level |
|---|---|---|---|
| C0 | `BASELINE_LEAGUE_V1`: empirical first-innings distribution by league and regime (for example IPL before and after the 2023 Impact Player rule), full-length innings, prior seasons | archive scorecards | — |
| C1 | C0 plus a shrunk venue effect (partial pooling; venue samples are small) | archive | C1 is the honest team-free comparator |
| C2 | Team model: negative-binomial, Gamma or discretised-normal regression with time-decayed, shrunk batting-team and bowling-team strengths, venue, regime and bat-first branch; conditional dispersion | archive (IPL 2008–2026) | Development CRPS gain over C1 in every held-out season |
| C3 | Phase model: powerplay, middle and death runs and wickets, joined coherently. Also prices phase contracts | Cricsheet, aggregated by phase (WP-05) | C2 passes |
| C4 | Ball-outcome simulator. Requirements:<br>• fitted multinomial outcomes (dot, 1, 2, 3, 4, 6, wicket, wide, no-ball with free hit, byes);<br>• conditioned on phase, wickets in hand and balls left;<br>• shrunk batter and bowler role ratings;<br>• bowler quotas;<br>• Impact Player substitutions;<br>• a **shared per-innings random effect**, without which independent balls under-disperse totals;<br>• a fixed seed per frozen file. | Cricsheet ball-by-ball | C3 passes **and** the owner accepts an opaque model |

**Realistic expectation.**
- The repository's IPL team model was a coin flip on results. A1 v1 was worse than the format mean on totals.
- R1 cites a public simulator with a correlation of about 0.3 with actual totals (UNVERIFIED).
- C0 or C1 may be the honest end state.
- An IPL season has about 74 matches over about 9–10 weeks. A stage-1 pilot (later of 8 weeks and 40 events) uses most of one season, so stage 2 needs the next season or more. **A confirmatory IPL answer is unlikely before 2028.**
- Pooling several T20 leagues through Cricsheet adds events but needs league-specific baselines. Register it explicitly as a pooled test.

**Second innings.** A chase total is censored at the target plus the winning delivery's legal overshoot, never capped at the target (§12 C-ML-14).

### 8.5 Calibration

This follows C01–C04 and the repair report's design:
- Winner temperature, or regularised Dirichlet calibration, is fitted on CAL predictions only and applied by **reweighting the joint state masses**.
- `IDENTITY_INSUFFICIENT_CAL` applies when CAL evidence is thin.
- Handicaps and totals are re-derived and evaluated, but are not claimed to be independently calibrated.
- The stack and the calibrator are never fitted on the same outcomes.

### 8.6 Challengers and stacking

Gradient-boosted residuals (ML02), NGBoost and quantile models (ML03) are challengers only, built after the L3 joint model of the same league is frozen. Stacking (ML04) uses constrained non-negative weights fitted on out-of-fold, time-ordered predictions. It is adopted only if it beats the best single component on a later held-out block.

Deep sequence models, transformers and possession or drive simulators are deferred (ML05). There is no ball-tracking, possession or play-by-play pipeline here, and the data volume does not justify them.

### 8.7 First model per league

| Priority | League | First fitted model | Why this order |
|---|---|---|---|
| 1 | EPL | Dixon–Coles with time decay; 1X2, totals and handicaps from one grid | TB-1-MD results resolution in 5 of 5 seasons; LABEL_B rebuilt; season under way |
| 1 | NBA, NBL (WNBA in 2027) | Joint margin–total discretised normal, fitted covariance, OT branch | TB-1 sides and totals resolution; STRONG rows on 26–29% of games; NBL totals bias (RET-01) |
| 1 (development now) | AFL | Joint discretised normal; 6G + B challenger | LABEL_A; 39% STRONG; shadow from March 2027 |
| 2 (development now) | IPL first innings | C0 → C1 → C2 | Weakest area; scorecards in hand; shadow from March 2027 |
| 2 | NFL | Key-number margin distribution plus total normal; QB scenario mixture | 27% STRONG; season under way |
| 3 | NRL, NHL | Joint normal; regulation Poisson with OT/SO | NRL sides withdrawn; NHL gain below materiality |
| Test bed | MLB | Negative-binomial runs with the stopping rule | Most LABEL_A data, 0% STRONG: useful for pipeline checks, not for skill |
| Not ready | Tennis, rugby union, KBO/NPB extras | — | No data route, or placeholder fields (§7.2) |

### 8.8 What not to build

| Item | Reason |
|---|---|
| Odds, lines or implied probabilities as features | MARKET_BLIND (CURRENT_RULES §5) |
| Separate spread or total classifiers with no joint reconstruction | P4; CURRENT_RULES §7 |
| A Gymnasium or RL staking environment in this repository | No staking advice (§5); §10 |
| Feature store, REST API, BigQuery, Docker service | Single-user, chat-run framework; BigQuery was the wrong model class (F-ML-5) |
| Pickled models | Unsafe and version-fragile (F-ML-6); use Markdown parameter tables |
| Hand-set transition probabilities presented as fitted | A26 |
| Unsourced physical constants (dew, altitude, sixes) | A25: register as hypotheses at most |
| Soil, Hawk-Eye and strip-count features | Not public; fail the known-at rule |
| Silent defaults and optimiser fallbacks | F-DST-7, F-ML-2 |

---

## 9. Evaluation and promotion

### 9.1 Two kinds of evidence, never pooled

| Class | What it is | What it can show |
|---|---|---|
| `HISTORICAL_DEVELOPMENT` | Rolling-origin results on archive data that has already been opened | Mechanics, coherence, plausibility, the variance inputs for sizing. **Not** prospective skill (SCORING §8) |
| `PROSPECTIVE_SHADOW` | Rows frozen before the start and settled from the feed | The only basis for promotion |

### 9.2 Development protocol

1. **Folds by season.** For each test season s, fit on seasons before s. Within s, refit at a fixed cadence (for example monthly) using games strictly before the refit date. League profiles, home edges and widths come from the training block only (repair report, item 1).
2. **Blocks.** TUNE uses the earliest development seasons, and its choices are frozen before later folds. Re-selected parameters are labelled "not independent". CAL uses the season before TEST. TEST is touched once per release.
3. **Events stay whole.** All contracts of an event share a fold. Paired differences are averaged within the event, then within the ISO week.
4. **Data repairs re-implemented with tests:** draws retained as non-wins (item 2); NHL deciding OT/SO goals removed from regulation training only with an explicit flag (item 7); native IDs keep doubleheaders apart (item 5); full precision for extras vectors (item 6); zeros kept distinct from missing (item 9).
5. **The current season is never used in development.** It is reserved for the prospective lane.

### 9.3 Prospective shadow protocol

- **Full-league shadow.** Price **every** fixture of the league in the window, not only carded events. This removes selection bias (E01) and is the only way to reach power (F16).
- **Card-row pairing.** Where a card exists, also pair the shadow row with the card's frozen `p_card` on the identical row.
- **Freeze and publication.** The freeze happens before the first scheduled start in the file. Commit, then reveal (§6.1). Late files are labelled `LATE_START` and leave the primary cohort.
- **Settlement.** Settle from the feed, with revision chains, the headline and sensitivity evidence views (SCORING §2a), and unresolved cases kept visible.

### 9.4 Metrics

| Family | Primary | Secondary and guardrails |
|---|---|---|
| Winner | Paired Brier difference against the comparator (half-sum Brier for three-way, labelled) | log loss; calibration bins (SCORING §4); calibration-in-the-large ≤ 0.05 |
| Handicap and total ladders | Paired Brier per standard line, averaged within the event | push-mass error at key numbers; monotonicity pass rate (must be 100%) |
| Score distributions (margin, total, first innings) | CRPS on the discrete distribution: Σ_t (F(t) − 1{y ≤ t})² | PIT histogram; central-interval coverage; mean error and z (SCORING §3) |
| Coherence | 100% pass on §12 checks | — |

### 9.5 Promotion bars

The owner's 2026-09-27 standard (a 95% interval below 0 in every independent window, on data that did not suggest the change, preregistered) is combined here with the register's two-stage design:

| Step | Requires |
|---|---|
| Develop → SHADOW | Model card complete. §12 checks pass. Development paired improvement over **both** comparators with the interval below 0 in **every** held-out season. Hypothesis registered by prompt 8 before the lane starts |
| SHADOW → REFERENCE | Full-league stage 2 (sized at the end of stage 1) shows superiority over **both** comparators (upper bound < −δ_min), guardrails hold, and the most-frequent-team sensitivity keeps its sign. Owner order |
| REFERENCE → ANCHOR | Card-row test on identical rows: model at least non-inferior to `p_card` (NI predeclared), plus full-league superiority still holding. Owner order. If the card-row test is `INFEASIBLE_AT_THIS_EFFECT` (likely at about 20 cards a week), say so; promotion does not proceed on full-league evidence alone without an explicit owner decision |

Failed results stay visible. A demotion is a forward revision, and past frozen rows never change.

### 9.6 Sizing

From the register:

  weeks = ⌈((1.960 + 0.842) × SD_w ÷ δ)²⌉, minimum 8; above 52 the test is `INFEASIBLE_AT_THIS_EFFECT`.

SD_w is the SD of week means of the paired difference, estimated in stage 1. **No sample size is stated here** because SD_w is unknown (SCORING §5: `SAMPLE_SIZE_NOT_ESTIMATED`). A full-league lane has many events per week (an NBA week holds dozens of games), so SD_w should be much smaller than for cards. That is exactly why §9.3 prices every fixture. Development folds can give a planning estimate, but the frozen size comes from stage 1.

### 9.7 Proposed registrations

These have status `PROPOSED_NOT_REGISTERED`. Each must be written into HYPOTHESIS_REGISTER by prompt 8 before its start trigger, with δ, NI and the start trigger frozen there.

| Proposed ID | Candidate → comparators | Families | Earliest start |
|---|---|---|---|
| ML-EPL-DC-v1 | Dixon–Coles → BASELINE_LEAGUE_V1, TB-1 | 1X2, totals ladder, handicap ladder; CRPS on goals | After WP-01 and WP-07 |
| ML-NBA-JOINT-v1 | Joint normal → both | winner (incl. OT), handicap and total ladders; CRPS | NBA 2026-27 season |
| ML-NBL-JOINT-v1 | Joint normal → both | as NBA; total bias (links RET-01 / FC10-PROFILE-v1) | in season |
| ML-AFL-JOINT-v1 | Joint normal → both | winner, handicap, totals; CRPS | AFL 2027 round 1 |
| ML-IPL-FI-C1-v1 / C2-v1 | C1 → C0; C2 → C1 | first-innings ladder; CRPS; PIT | IPL 2027 |
| ML-CAL-WIN-v1 | Reweighting calibrator → identity | winner, with every derived family re-checked | once a lane has CAL data |
| ML-GBM-RESID-v1 | Residual boosting → L3 joint | winner | after a lane's L3 is frozen |
| MKT-BENCH-v1 (D3-ii) | Card and model against the no-vig close | identical contracts, post-settlement | after the ledger is restored |

### 9.8 Monitoring and rollback

Track, per lane:
- rolling paired difference by week;
- calibration bins;
- PIT shape;
- coherence failures (any failure stops issuance of that file);
- input availability.

A refit or recalibration is a new `model_version`, starts its own stage 1 if it changes p, and never rewrites past rows.

---

## 10. Reinforcement learning and the decision layer

### 10.1 Position under the current rules

CURRENT_RULES §5 forbids value, edge or staking advice. The LICENSE says nothing here is betting advice. **No RL or staking component belongs in this repository** unless the owner changes those rules (D3-iii). That change goes beyond a prompt-8 process change: it alters the framework's stated purpose.

### 10.2 Where RL does not help

- **Forecasting.** Outcomes do not depend on the forecaster's actions. This is supervised learning, and RL only adds variance.
- **Learning stake size from profit and loss.** At even odds one bet's return has an SD of about 1 stake. Telling a 2% edge from zero at 2 SD needs about (2 × 1 / 0.02)² ≈ 10,000 bets, which is illustrative arithmetic. The cards produce a few hundred decisions a year.
- **Learning when to freeze.** The framework fixes this by rule (PR-04's two-step window), not by optimisation.

### 10.3 If the owner opens a separate decision project (D3-iii)

Run it in a separate repository, as paper decisions first. Prerequisites, in order; each must hold before the next starts:

1. A forecasting lane has passed §9.5 to at least REFERENCE.
2. MKT-BENCH-v1 shows the model is **not worse** than the no-vig close on its contracts. The archived ledger itself predicted that the market would usually be better calibrated, so this gate may never open.
3. At least one season of timestamped price capture, stored in that project only.
4. **Baseline policy:** fractional Kelly (¼) shrunk for estimation error (Baker & McHale), a hard per-bet cap (≤ 2%) and a per-slate cap (≤ 10%). Bets on the same event (winner and handicap) count as one position. This is paper-traded for a full season.
5. Only then a contextual bandit:
   - arms {pass, ¼ Kelly, ½ Kelly};
   - reward = CLV against a de-vigged close, with the method chosen by historical log loss (Appendix B);
   - logged propensities for off-policy evaluation;
   - adopted only if it beats step 4 out of sample on CLV and drawdown.
6. Deep RL (DQN, PPO, SAC) is not planned. The decision count cannot support it.

**Legal and harm-minimisation constraints (Australia):**
- Online in-play sports betting is prohibited under the Interactive Gambling Act 2001, apart from phone and place-based exceptions. ACMA has enforced this repeatedly (Appendix C). **No live or in-play automation.**
- Use only Australian-licensed providers.
- The credit-card ban, identity pre-verification and BetStop are cited by R1 but UNVERIFIED here; verify them before any real-money step.
- Build in a fixed separate bankroll, hard stake caps, a loss limit, an automatic pause on drawdown and a monthly review.
- None of this is legal advice.

### 10.4 Corrections to the reports' RL designs

| Report | Defect | Correction |
|---|---|---|
| R3 | Claims fractional Kelly fails and RL succeeds | Unsupported; shrunk fractional Kelly is the baseline any policy must beat |
| R3 | Reward adds CLV and settled log-wealth for the same bet | Choose one training reward (CLV, which is known before the result); report log-wealth as evaluation only |
| R3 | CLV from raw placed and closing odds | De-vig the close first (Appendix B) |
| R3 | "CVaR penalty" is max(0, drawdown − τ) | Call it a drawdown penalty, or estimate CVaR from the return distribution |
| R3 | Caps of 5% per contract and 20% per slate | ≤ 2% and ≤ 10%, with correlated positions merged |
| R2 | Garbled Kelly formula; DQN in 5–7 days | Appendix B; §10.3 sequence |
| R1 | Bandit reward on CLV requires a price taken at the decision | Correct for a decision project; incompatible with MARKET_BLIND, hence D3 |

---

## 11. Work packages

Effort: S ≤ 1 maintainer-day, M 2–5 days, L 1–3 weeks, XL more than 3 weeks. These are rough planning figures. Calendar start depends on season dates (verify each). Predictive outcomes cannot be scheduled.

| WP | What | Runs under | Writes | Depends on | Acceptance evidence | Effort |
|---|---|---|---|---|---|---|
| WP-00 | Owner decisions D1–D5 | owner | — | this document | decisions recorded verbatim in WP-01's CHANGE_PROPOSAL | S |
| WP-01 | Define the shadow lane | prompt 8 | archive copies; CURRENT_RULES (§0 boundary wording; §1 reading-gate exclusion of `research/model_shadow/` for prompts 1–3); SCORING (shadow view for model rows); CARD_AND_LOG_TEMPLATES (only if D2 > SHADOW); HYPOTHESIS_REGISTER (§9.7 entries); `research/model_shadow/README.md`; CHANGELOG | WP-00 (D1 = B, D2) | prompt 8 §5 checks; FIXTURES.md with a negative fixture and an edge case per new check (R35); versions bumped consistently | M |
| WP-02 | Source register corrections | prompt 8 (or 7) | SOURCES: Cricsheet licence ODbL → ODC-By (F15); nflverse market-column note; football-data location per D3 and F13 | — | links and lines checked; no rule change | S |
| WP-03 | Workshop bootstrap and archive rebuild | workshop | separate repository: pinned environment, tests, receipts; port `research/src/archive.py` from `37203fc2b`; rebuild the canonical export from **current** CSVs | D1 = B | row counts reconcile with ACTIVE_FILE_INDEX §2 (522,048 / 500,328); quarantined builds absent; the rebuild reproduces byte-identically from its receipt | M–L |
| WP-04 | Label admission for priority leagues | prompt 7 plus workshop | `DATA_PROVENANCE.md` updates; receipt files outside the repository with hashes recorded | WP-03, D4 | `missing_exact_result_source` cleared for NBA, NBL and EPL (or LABEL_B declared); counts published | L |
| WP-05 | Cricsheet capture (IPL first, then BBL and T20I) | prompt 7 plus workshop | derived innings and phase CSV with `DATA_PROVENANCE.md` (ODC-By attribution); raw JSON stays outside | WP-02 | match counts reconcile with the IPL scorecards; toss and result agree on every matched match | M |
| WP-06 | Baselines in code | workshop | `BASELINE_LEAGUE_V1` per league; TB-1 replication | WP-03 | TB-1 code equals TB-1-MD hand arithmetic to 3 dp on a random 20 games per league; `BASELINE_P` of settled v11 cards reproduced, or differences explained | M |
| WP-07 | Priority-1 development models (EPL, NBA, NBL, AFL) | workshop | model cards; `DEVELOPMENT_RESULTS.md` (`HISTORICAL_DEVELOPMENT`) | WP-06 | §9.2 protocol; §12 checks 100%; results against both comparators per held-out season, with intervals | L |
| WP-08 | Prospective shadow lanes (NBL, EPL now; NBA from tip-off; AFL and IPL March 2027) | workshop plus prompts 3/6 for scoring | weekly CSVs, freeze receipts, settlements | WP-01, WP-07 | every file hash committed before its first start; feed settlement; stage-1 SD_w recorded in the register | L, ongoing |
| WP-09 | IPL first-innings C0–C2 development (C3 after WP-05) | workshop | model cards | WP-05, WP-06 | the C-gates in §8.4 | L |
| WP-10 | Winner calibration layer | workshop | calibrator ID per lane | a lane with CAL data | C01/C03 checks; derived-family re-evaluation | M |
| WP-11 | Challengers (gradient-boosted residuals, NGBoost) | workshop | model cards | WP-07 frozen L3 | beats L3 in every held-out season, or is dropped | L |
| WP-12 | Stage-1 review and stage-2 sizing per lane | prompt 6 / prompt 8 | dated register entries | 8 weeks and 40 events per lane | size frozen before any stage-2 outcome; `INFEASIBLE_AT_THIS_EFFECT` recorded honestly | S–M |
| WP-13 | Promotion decisions | owner | prompt-8 change per promotion | WP-12 outcome | §9.5 | S |
| WP-14 | Optional market benchmark (D3-ii) | prompt 8, then hand entry | restore the archived ledger under its firewall; historical EPL comparison computed outside the repository | D3 = ii; F13 resolved | firewall rules verbatim; `Entered > Settled` on every row | M |
| WP-15 | Decision project (D3-iii only) | separate repository | — | §10.3 gates | §10.3 | XL; not scheduled |

**Effect on in-progress work.** No v11 card procedure changes until a promotion is ordered. FC10/FC11 tests continue unchanged. Shadow lanes are separate cohorts, never pooled with card cohorts.

---

## 12. Check catalogue

Prompt 8 (R35) requires one negative fixture and one legitimate edge case per check. In the workshop these are automated tests. In this repository they are manual walkthroughs, labelled as such.

| Check | Rule | Negative fixture (must be rejected) | Legitimate edge case (must pass) |
|---|---|---|---|
| C-ML-01 | W+P+L+V = 1 within declared tolerance | masses 0.55 / 0.10 / 0.30 / 0 | void `NOT_ESTIMATED` and W+P+L = 1, labelled |
| C-ML-02 | p_decisive = W/(W+L) | W 0.55, P 0.10, L 0.35, p_decisive 0.55 (should be 11/18) | W+L = 0 gives `NOT_COMPUTED` |
| C-ML-03 | Lattice support and parity | non-zero mass on T = 3, M = 0 | soccer 0–0 state |
| C-ML-04 | Ladder monotonicity | P(Over 2.5) > P(Over 1.5) | equal masses where no support lies between the lines |
| C-ML-05 | Covering pair P(home +k) ≥ P(home win), k ≥ 0 | +1.5 below the winner probability in basketball | tennis games handicap exempt (P07 counterexample 6–0, 4–6, 4–6) |
| C-ML-06 | Known-at: every feature is strictly earlier | rolling form that includes a same-date game | previous-day game included |
| C-ML-07 | No market columns cross the boundary | a column named `B365H`, `spread_line`, `PSCH` or `home_moneyline` | a `line` column holding the contract line |
| C-ML-08 | Frozen before the scheduled start | `frozen_utc` after the scheduled start in the primary cohort | a verified delayed start, labelled `LATE_START`, outside the primary cohort |
| C-ML-09 | Identical-row pairing | shadow Over 2.5 paired with card Over 3.0 | same line, opposite orientation, paired through the complement |
| C-ML-10 | Receipts complete | missing `data_snapshot_sha256` | — |
| C-ML-11 | No silent fallback | every attack/defence = 0 after a failed fit | `NOT_ISSUED:FIT_FAILED` row |
| C-ML-12 | Unknown team refused or explicitly primed | a default λ of 1.55/1.20 | promoted-team prior labelled with its source and width |
| C-ML-13 | CAL dates fully before TEST dates | overlapping CAL and TEST | CAL in the season before TEST |
| C-ML-14 | Chase censoring, not a cap | chase total capped exactly at the target | target plus overshoot from one delivery |
| C-ML-15 | Toss branch labelling | a post-toss row priced as a pre-toss mixture | pre-toss mixture weights summing to 1 |
| C-ML-16 | Settlement revision chain (R17) | two revisions with one parent and no resolver | partial revision changing only its listed keys |
| C-ML-17 | Commit, then reveal | contents committed before the first start | hash committed before, contents after |
| C-ML-18 | Market firewall (D3-ii) | `Entered` earlier than `Settled` | `Entered` after `Settled`, no-vig method named |

---

## 13. Risks, limits and what this document does not claim

- **Not claimed:** that any model will improve the cards; that the October 9 repairs exist anywhere; that any external figure marked UNVERIFIED is true; any sample size.
- **Biggest risks:**
  - The programme produces engineering without predictive gain. That is likely for totals, MLB, NHL and cricket, and the honest outcome is then to stop.
  - The full-league shadow becomes a backdoor anchor because card writers can read published files. Mitigation: reading-gate exclusion plus commit-then-reveal.
  - LABEL_B training data carries unknown errors. Mitigation: LABEL_A sensitivity checks; promotion only on prospective feed-settled rows.
  - Maintenance load returns through the workshop. Mitigation: the workshop never blocks a card, and a lane can stop without affecting the framework.
  - Scope drift towards betting. Mitigation: D3 is explicit, and §10 sits outside this repository.
- **Data:** archive dates are calendar cutoffs, not publication times. Historical lineups and weather are not pregame snapshots (§7.3).
- **This document:** written from the reads in §2. It was not adversarially reviewed and was not run through prompt 8. Before WP-01, an agent must read the files marked "not read" and recheck F01–F16 against the then-current HEAD.

---

## Appendix A. Port list from `37203fc2b`

Port a module only with a fresh test suite. "Repair" items come from the 9 October repair report, and none is present in the committed code (F05).

| Module (at `37203fc2b`) | Keep / rewrite / drop | Must fix or verify at port time |
|---|---|---|
| `research/src/archive.py`, `archive_std.py`, `archive_sources.py` | Keep (workshop) | Rebuild against current CSVs; respect quarantines and `SUSPECTED_DEFAULT`; exclusion reasons unchanged |
| `runtime/src/common/splits.py`, `evaluation.py`, `prospective.py` | Keep | Week-block intervals as in SCORING §5; no pass on an interval merely containing 0 |
| `common/ratings.py`, `strengths.py` | Keep | Decay and K chosen on development seasons only; fail on non-convergence |
| `common/dixon_coles.py` | Rewrite | Vectorised likelihood with analytic gradient (F-ML-3); no zero-parameter fallback (F-ML-2); ξ by rolling validation |
| `common/distributional.py`, `counts.py` | Keep | Lattice discretisation and parity; non-crossing quantiles |
| `common/calibration.py`, `calibration_layer.py` | Keep | **Repair:** joint reweighting with CAL-only fit; `IDENTITY_INSUFFICIENT_CAL` |
| `common/endpoints.py`, `contracts.py`, `selection.py` | Keep (pricing only) | W/P/L/V sets per endpoint; selection logic stays in Markdown (SELECTION_RULES), not code |
| `common/stacking.py`, `boosting.py` | Keep (challengers) | Out-of-fold only; adopted only if it beats the best single model |
| `common/artifacts.py`, `provenance.py`, `snapshots.py` | Rewrite | Markdown and CSV outputs per §6.2; no JSON or pickle crosses into this repository |
| `common/bigquery_ml.py` | Drop | F-ML-5 |
| `sports/*/engine.py` | Keep per sport when its lane starts | **Repairs:** train-only league profiles (item 1); draws as non-wins (2); NHL OT/SO goals (7); MLB doubleheaders (5); extras precision (6). No defaults (F-DST-7) |
| `sports/cricket/engine.py` | Rewrite | §8.4 C-ladder; innings random effect; chase censoring with overshoot |
| `sports/tennis/engine.py` | Defer | No data route (§7.2) |

## Appendix B. Formula reference

- **Decisive probability:** p = W/(W+L). Unconditional masses satisfy W+P+L+V = 1.
- **Score identities:** T = H + A, M = H − A; Var(T) + Var(M) = 2[Var(H) + Var(A)]; T ≥ |M|; T ≡ M (mod 2).
- **Winner reweighting calibrator:** for winner class c with original mass p_c > 0 and calibrated mass q_c, each state ω in c becomes p(ω)·q_c/p_c. Re-derive every other family afterwards.
- **Discrete CRPS:** Σ_t (F(t) − 1{y ≤ t})² over the integer support.
- **Sizing (register):** weeks = ⌈((1.960 + 0.842) × SD_w ÷ δ)²⌉, minimum 8, cap 52.

*Decision-project reference only (D3-iii), not operative in this repository:*
- **De-vig.** Let q_i = 1/o_i and S = Σ q_j.
  - Multiplicative: p_i = q_i / S.
  - Power: p_i = q_i^k, with k solving Σ p_i = 1.
  - Shin: p_i = [√(z² + 4(1 − z) q_i² / S) − z] / [2(1 − z)], with z solving Σ p_i = 1.
- **Kelly with a push outcome:**
  - With b = o − 1, f\* = (p_W·b − p_L) / (b·(p_W + p_L)).
  - Without pushes this is (p·o − 1)/(o − 1).
  - Shrink for estimation error: f\*·f\*² / (f\*² + Var(f̂)).
  - Then apply a fraction and a cap.
- **CLV** = o_taken × p_fair_close − 1.

## Appendix C. External sources checked in this pass

| Claim | Status | Source |
|---|---|---|
| Cricsheet data licence is the Open Data Commons Attribution License | VERIFIED 2026-10-14 | [Cricsheet register](https://cricsheet.org/register/) |
| Online in-play sports betting is prohibited for Australian customers under the IGA, with phone and place-based exceptions; ACMA enforcement 2021–2026 | VERIFIED from ACMA reports and trade coverage; the Act itself was not read | [ACMA formal warning to Tabcorp (2021)](https://acma.gov.au/articles/2021-11/acma-issues-formal-warning-tabcorp-online-play-betting) · [ACMA Tabcorp investigation report (2026)](https://www.acma.gov.au/sites/default/files/2026-02/Investigation%20Report%20-%20Tabcorp%20Holdings%20Limited.pdf) · [iGaming Business on the 2023 in-play breaches](https://igamingbusiness.com/legal-compliance/legal/acma-flags-gambling-giants-breaching-in-play-betting-rules/) · [AGB on ACMA clearing Tap in-play (2026)](https://agbrief.com/news/australia/24/02/2026/acma-clears-tabcorps-tap-in-play-service-under-interactive-gambling-laws/) |
| Everything else attributed to R1–R3 and not in this table | UNVERIFIED | the reports' own citations |

## Supplemental actual implementation status — release 2026-10-14-5

The [actual review](research/verification/framework_change_2026-10-14-5/ML_WORKSHOP_REVIEW.md) and [artifact admission](research/model_shadow/ARTIFACT_PROVENANCE.md) govern current implementation claims. The original framework-change-3 results section remains unfinished, not acceptance evidence. The present workshop is partial development implementation; advanced challengers, ball-by-ball cricket, source admission and prospective qualification remain outstanding. That historical release promoted no model. The owner-authorised 15 October primary runtime is a separate experimental primary lane, governed by PRIMARY_PREDICTION_PROTOCOL rather than this former exclusion.
