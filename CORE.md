# CORE: what every card reads (CORE-v1)

**MDS-2026.10.22-v24.0 · CR-2026.10.22-R2 · P-2026.10.22-v24.0 · SCV-2026.10.22-v12 · SEL-2026.10.22-v4.** The one document a game card must read in full before research, with the [prompt 1 core](research/prompts/1_GAME_CARD.md) and the one [sport file](research/prompts/1_sports/). It condenses the rules that decide a card; everything else is reference, read when the card touches that topic. Where this page and a long-form protocol differ in wording, the protocol governs and the difference is a defect to report (GOV-v2). Where a pre-v24 sentence anywhere contradicts this page, this page governs for cards under P-2026.10.22-v24.0 and later; earlier cards keep their own method.

**Reading receipt.** Print branch, HEAD SHA, read time with offset, every uncommitted control difference, and the files actually read: this page, the prompt 1 core, the sport file and whatever the card opened. Never claim a file was read in full from an excerpt.

## 1. Honesty and custody

- Everything is Markdown, CSV and text. Code lives only under `ml/` and is run, never described. Do not claim a grid, simulation, fit, calculation, file write, readback, commit or push that did not happen; report the exact error if one failed.
- Labels are literal. The analyst's own final probability is `ANALYST_PRIMARY_V1 / UNCALIBRATED_ANALYST_PRIMARY`, built from a frozen reference plus logged adjustments from P-2026.10.22-v24.0; cards before it keep their method. Nothing is certified; a model is `EXPERIMENTAL_NOT_QUALIFIED`.
- Missing is not zero. Use `NOT_COMPUTED`, `NOT_ESTIMATED`, `NOT_VERIFIED`, `UNKNOWN_DEFINITION`, `N/A` exactly. Missing evidence is `UNRESOLVED`, never VOID, a loss, a healthy player or a clean sheet. Never invent a source, time, probability, baseline, lineup or score.
- Issued cards, settled originals, previous log parts and dated reports are immutable. A correction is a dated addendum with its parent, reason and affected keys. A card's frozen reference and picks are never edited after issue.
- **SPORTS_ONLY / MARKET_BLIND.** No odds, line movement, tips, previews, prediction markets or fantasy inputs in research, the reference, adjustments or any card. A supplied line is contract metadata. The only market-adjacent items are the line-implied 0.5 written into supplied two-way rows and the hand-entered post-settlement benchmarks ([BENCHMARK_PROTOCOL](BENCHMARK_PROTOCOL.md)); neither is read before settlement. The decision lab stays firewalled (CURRENT_RULES section 5a); no staking, edge or value claim; no in-play automation.
- Every run that changes files ends with a commit and push by exact path, no force, then a check that `HEAD` equals `origin/main`. Never stage the whole tree.

## 2. Identity, the mini and IDs

- A game card is appended to the active mini (`research/active_minis/`) before the footer, with its intake row and footer updated, read back and committed. One issuing writer per mini; only the lease holder appends; a frozen mini accepts nothing.
- Events use a stable **local key** `LOCAL-<MINI_KEY>-G####`. No canonical P-ID is assigned or reserved before settlement; prompt 3 settles the event and runs the prompt-4 import, which assigns the ID and records the local-to-canonical map. P-518 to P-522 are never reused.
- Search every mini and log by native ID, aliases and participants before writing; an existing event gets a dated addendum, not a second card. A doubleheader needs its game number or native ID.
- Preserve line endings and every earlier byte; compare the destination prefix after the append. Re-read HEAD and the destination's byte count and tail immediately before each write.

## 3. A card, step by step (v24)

1. **Read** this page, the prompt 1 core, the sport file; print the receipt. Resolve the event: competition, season, stage, participants, venue, native ID, scheduled start in venue zone, UTC and Australia/Sydney; the endpoint and settlement conventions (overtime, extra time, shootout, retirement).
2. **Tier.** `python -m ml reference tier --competition C` (A, B or C; [REFERENCE_MODEL_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md)). Print it.
3. **Reference, before any probability is typed.** Tier A with a release as its declared reference: `python -m ml pregame reference …`. TB-2-MD or TB-1-MD: `python -m ml reference standings …` then `python -m ml reference run …`. Baseline only: `reference run` without standings. Tier A competitions whose declared reference is not the release also run `pregame reference` for the challenger. Paste the Reference block into the card. If the request is too late for the full card to finish before the start, issue the **fast card** first (FASTCARD-v1) and the full card after as an addendum.
4. **Research** by the sport's value-ranked checklist ([RESEARCH_CHECKLISTS](RESEARCH_CHECKLISTS.md)): availability and starters first, timed to when they are published, then history windows, conditions, rules. Decisive facts need a source, a publication time, a retrieval time and a second independent source; a projection is not a confirmation. Search all of it until the horizon, record every attempt.
5. **Adjust.** One ledger row per confirmed fact with its [effect-table](EFFECT_TABLES.md) row and entry size ([ADJUSTMENT_LEDGER_PROTOCOL](ADJUSTMENT_LEDGER_PROTOCOL.md) section 1). Apply them to the reference centre, recompute one score grid, read every supplied contract from it. Width never below the [floor](COMPETITION_PARAMETERS.md).
6. **Picks block.** `PICKS_V2` for every priced contract ([CARD_AND_LOG_TEMPLATES](CARD_AND_LOG_TEMPLATES.md) section 3c); then `python -m ml card lint --mini M --key K` until it passes; then `python -m ml ledger add …`.
7. **Write** the card (decision block, picks block, adjustment table, appendix A1-A9), update intake and footer, read the file back, run `python -m ml pregame run …` (freezes the card's own p on the reference's contracts), commit and push before the scheduled start whenever possible.
8. **Return** the picks, the winner, the reasons and sources, the reference, the adjustments with their sizes, the abstain flag, the gaps, the local key, timing and the commit.

**What a card says.** A probability for every supplied contract; the winner for both sides (with a draw where allowed); a most-likely list of up to four rows with each row's distance from the centre; an information list (rows moved at least 0.03 from the reference); and `no strong pick` when no ranked row reaches 0.65 and no row moved. Rule T2 is a descriptive count; the headline is the paired proper score. A pair that covers itself counts as one pick.

## 4. Contracts, masses and settlement vocabulary

- State each contract's unit, period and action (regulation, overtime, extras, push, void, retirement) before pricing. An ambiguous text is priced under every reading, frozen with both, and queued; never resolved silently.
- All contracts come from **one** coherent distribution. Keep W, P (push) and L masses; `p = W/(W+L)`; masses sum to one. A winner row in a competition with draws loses on a draw unless the contract says otherwise. Complementary rows agree. Apply a key-number, push or tie adjustment to the whole normalised distribution, never to one row. Do not clip a probability; a ranked row is at or below the 0.90 selection ceiling and a higher true value is kept outside the ranked list.
- Family rules (SELECTION_RULES section 4) apply unchanged: soccer first-half Over 0.5 needs a half-specific model, baseball +1.5 at rank 1 needs p at least 0.65, tennis games come from the complete set-score states, corners need a named provider and a count model, period and player rows need exact definitions and a source.
- Grades: WIN, LOSS, PUSH, VOID (only under a frozen void rule), UNRESOLVED. Evidence: A official field owner for the exact target; B structured provider with lineage disclosed; C single secondary; E a bound that grades only if every feasible value agrees; X none. Settle from a box score or linescore with a sum check, never from a headline, recap title or narrative article. Corrections append revisions with parents; a conflict leaves keys UNRESOLVED.
- Every open item has an actor, a route, a due time with timezone, a final-time basis, a last attempt, and a scheduled-automation status (R38). Nothing is automated unless it is.

## 5. Evidence and timing

- **Horizon.** The game-log scheduled start, unless an earlier actual issue or verified first play. Research may finish after the start; label the card `PREGAME`, `POST_START_ISSUE` or `TIMING_UNVERIFIED`, and `CLEAN_PRE_START_INPUTS` only with proof that no outcome was seen. A late page is never pre-start evidence by itself. Record the horizon, retrieval, completion, last availability check and actual issue separately.
- **Availability.** Starters and roles, selected bench, injuries, illness, suspensions and late changes for **both** sides, from the official match record, both clubs, medical or eligibility sources and permitted structured providers, with local-language discovery for obscure competitions. A failed extraction is not non-publication. "No injuries found" is not "none".
- **History.** Each side's L5, L10, L15 and L20, season and league from dated games before the horizon, with true n, opened sources and exclusions of duplicates, awards and forfeits. The windows overlap and are one piece of evidence; a short-window swing is width, not a lean, unless a named current mechanism explains it. The framework found no bounce-back or streak effect in six leagues.
- **Corroboration** (EXH-v1): any missing, partial, stale or conflicting required field is pursued through alternative sources before it is called a gap; domain count is not independent-source count.
- **Weather** for outdoor play: the venue-local forecast for the match window (the 30-60 minutes around the start, during and after), not a morning forecast. Downgrade only for weather in the window.
- **Known-at.** A historical row's date is not its availability time; an input whose availability before the horizon cannot be shown is `KNOWN_AT_UNVERIFIED` and may not decide a ranked row.

## 6. Probability

- Start from the reference. A departure needs a ledger row; a feeling is not a row. Do not count an effect already in a rating. The reference and the league-only `BASELINE_P` (SELECTION_RULES section 9) are printed beside every number; a missing baseline uses an enumerated reason.
- **Widths** are never below the competition's floor without a written exception. Early season, stale profiles and unconfirmed lineups widen or mix, they do not narrow. A lineup uncertainty is a declared mixture with weights frozen before pricing.
- **Structure.** NFL margins of 3 and 7, hockey one-goal finishes and empty nets, baseball extras and walk-offs, cricket collapses and tennis match-level form shocks are handled explicitly ([SIMULATION_PROTOCOL](SIMULATION_PROTOCOL.md)). Simulate only where its table says, in code, with seed, N and Monte Carlo error printed. The exact method is the default.
- **Easy lines.** Report each ranked row's distance from the centre. A near-certain analyst-chosen alternative line is label-only evidence. A hit rate is not skill; the line-implied 0.5, the baseline, the reference and any benchmark are the comparators.
- **Abstain** below 0.65 with nothing moved. Stated probabilities between 0.40 and 0.65 have not separated winners from losers in the card record (slope 0.15, SE 0.31, 525 rows).

## 7. Models and learning

- **MLSCOPE-v3.** Models run where they are needed. Tier A: the release's model is frozen before the card as the declared reference, or as the challenger when another reference is declared; the card then starts from the frozen reference and its departures are scored. A model is judged only on frozen, pushed, pre-start rows, after at least 8 settled weeks and 50 settled paired games, against the reference on identical rows. A release is frozen for a season; edits outside the cycle's import closure never retire it. Prompt 8 owns every `ml/` change and every promotion.
- **No reinforcement learning in forecasting.** Outcomes do not depend on a forecast. The online expert weighting at settlement is called online learning.
- Prompt 3 settles the card, then the shadows, then runs the import. Prompt 6 ingests verified outcomes and evaluates; prompt 7 builds data; prompt 8 changes things. The league-day lane freezes every fixture of a competition with a release, card or not.
- Learning data are verified finals with sources and known-at times; a fact captured today is known today, never retroactively.

## 8. Change control (GOV-v2 / STATFREEZE-v1)

- **Statistical rules are frozen for a season.** A change to a probability method, a width, a selection constant, a reference or a release happens at a season boundary or through a new, separately scored lane. Bug fixes that change no output may happen at any time. Procedure changes are batched monthly. Editorial changes may happen at any time.
- **Every new rule names the rule it replaces** and the document that held it, and archives the replaced text byte for byte. No new paragraph is copied into a second document: others link to the one definition.
- Prompt versions: major for a format or statistical change, minor for a procedure change; wording keeps the version. The checks that can be code are code (`card lint`, `release-gate`, the tests); a hand-ticked checklist is for judgement only.
- Behavioural hypotheses are registered with a design, a metric and a stop rule before data ([HYPOTHESIS_REGISTER](HYPOTHESIS_REGISTER.md)); a favourable seed, a small sample or an exposed retrospective is not a test.

## 9. Where the long form lives

| Topic | Document |
|---|---|
| Rules in force, sources, times, custody | [CURRENT_RULES](CURRENT_RULES.md) · [METHOD](METHOD.md) · [CURRENT_STATE](CURRENT_STATE.md) |
| Tiers, reference, model lane, fast card | [REFERENCE_MODEL_PROTOCOL](REFERENCE_MODEL_PROTOCOL.md) · [FORECAST_CYCLE_PROTOCOL](FORECAST_CYCLE_PROTOCOL.md) |
| Adjustments, picks block, abstain, scoring | [ADJUSTMENT_LEDGER_PROTOCOL](ADJUSTMENT_LEDGER_PROTOCOL.md) · [EFFECT_TABLES](EFFECT_TABLES.md) |
| Benchmarks and the market firewall | [BENCHMARK_PROTOCOL](BENCHMARK_PROTOCOL.md) |
| League numbers, widths | [COMPETITION_PARAMETERS](COMPETITION_PARAMETERS.md) · [LEAGUE_PROFILES](LEAGUE_PROFILES.md) · [BASE_RATES_REGISTER](BASE_RATES_REGISTER.md) |
| Probability tables, TB-1-MD | [PROBABILITY_TOOLKIT](PROBABILITY_TOOLKIT.md) |
| Selection families, grades, baseline | [SELECTION_RULES](SELECTION_RULES.md) · [SCORING_AND_VALIDATION](SCORING_AND_VALIDATION.md) |
| Research inputs by sport and where | [RESEARCH_CHECKLISTS](RESEARCH_CHECKLISTS.md) · [SOURCES](SOURCES.md) · [ROSTER_AVAILABILITY_PROTOCOL](ROSTER_AVAILABILITY_PROTOCOL.md) · [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md) · [RESEARCH_EXHAUSTIVENESS_PROTOCOL](RESEARCH_EXHAUSTIVENESS_PROTOCOL.md) · [TIMING_RESEARCH_PROTOCOL](TIMING_RESEARCH_PROTOCOL.md) |
| Simulation | [SIMULATION_PROTOCOL](SIMULATION_PROTOCOL.md) |
| Mini, identity, retention, delivery | [MINI_LOG_IDENTITY_PROTOCOL](MINI_LOG_IDENTITY_PROTOCOL.md) · [RESEARCH_RETENTION_PROTOCOL](RESEARCH_RETENTION_PROTOCOL.md) · [EXECUTION_ENVIRONMENT_PROTOCOL](EXECUTION_ENVIRONMENT_PROTOCOL.md) · [GITHUB_REFERENCE_PROTOCOL](GITHUB_REFERENCE_PROTOCOL.md) · [GOOGLE_DRIVE_EXCHANGE_PROTOCOL](GOOGLE_DRIVE_EXCHANGE_PROTOCOL.md) |
| Formats, self-audit | [CARD_AND_LOG_TEMPLATES](CARD_AND_LOG_TEMPLATES.md) |
| Requests | [GAME_REQUEST_TEMPLATE](GAME_REQUEST_TEMPLATE.md) |
| Sport rules | `RULES_<SPORT>.md`, [LEAGUE_RULES_SOCCER](LEAGUE_RULES_SOCCER.md), [LEAGUE_RULES_CRICKET](LEAGUE_RULES_CRICKET.md) |
| Learning pipeline, models, registry | [LEARNING_PIPELINE_PROTOCOL](LEARNING_PIPELINE_PROTOCOL.md) · [ML_EXECUTION_PROTOCOL](ML_EXECUTION_PROTOCOL.md) · [`ml/README.md`](ml/README.md) |
| Prompts | [research/prompts/](research/prompts/README.md) |
