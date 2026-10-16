# PROMPT 1 — Supplied-first individual game-card research and local-mini append

**Extended edition · 14 October 2026 · prompt revision SF-2 · selection policy `SUPPLIED_FIRST_V1`.**

Research the requested event thoroughly. Assess **every exact user-supplied proposition**, show which is most likely to succeed under its frozen definition, and retain reproducible issue-time records. Preserve the complete sport-specific workflow below. Unsupported facts or probabilities remain explicitly missing.

This is a reusable prompt, not a forecast request. Placeholder event blocks are inactive until the user populates or explicitly invokes them. This revision does not claim publication, calibration, predictive improvement or execution of a game-card run.

## 0. Run contract and instruction precedence

| Setting | Required behaviour |
|---|---|
| Mode | `LOCAL_MINI_STAGING` |
| Control authority | `PUBLISHED_MAIN_PINNED`, one actually verified full `main` commit SHA |
| Repository | `https://github.com/danisgreat/Sports-Research` |
| Primary candidate universe | Exact distinct user-supplied contracts only |
| Derived contracts | Optional, separately frozen `NOT_PRIMARY` shadows |
| Default probability status | `UNCALIBRATED_ANALYST_SCENARIO`; qualification requires separate evidence |
| Continue if late | `YES`; research fully and classify timing honestly |
| Permitted writes | Existing authorised local mini, its permitted evidence/compatibility appendix, intake/footer and verification receipt |
| Settlement / canonical import | `NOT_PERFORMED` / `NOT_PERFORMED` |
| GitHub writes / new canonical IDs | `NO` / `0` |

Use this precedence:

1. The user's actual request, scope and explicit write boundaries.
2. Freshly pinned published controls for arithmetic, definitions, source custody, timing, lifecycle and scoring.
3. The explicit supplied-first candidate-scope override in SF1–SF12.
4. This prompt's implementation details where consistent with those controls.
5. Sport files, historical examples and archived notes; current controls take precedence over incompatible older instructions.

**Resolve a material conflict explicitly.** State the affected rule, version, chosen interpretation and consequence. Do not mix authority modes, silently amend published rules or invent a compliant label. A conflicting calculation or selection becomes draft/unresolved until resolved; independent research continues.

The pasted predecessor referenced the 2026-10-12 v11 suite and `mini-log-7`. Those are reference versions, not claims about the current remote. Discover actual versions from the pinned files on each run. New minis use the then-current format through their own creation workflow; already active minis keep their original format. Prompt 1 does not create an unauthorised mini or extend a writer lease.

### 0.1 Execution order

1. Parse the request and freeze its literal supplied universe.
2. Read controls, the complete active mini and relevant event/ID state; print the reading receipt.
3. Establish identity, duplicates, timing, outcome exposure and allowed writes.
4. Complete the relevant sport's seven steps, including evidence and rolling form.
5. Execute and verify supported distributions, baselines, scenario mixtures and sensitivities.
6. Rank the supplied ledger, select eligible supplied rows, compute gates and dependence, then optional shadows.
7. Recheck state, source changes, writer lease, mini freeze and ID continuity; reprice changed admissible inputs before issue.
8. Append/read back within scope or return a complete non-issued draft. Return all required tables and evidence-backed audits.

Do useful independent work while resolving a material missing input. Locate accessible files before asking. Ask only when uncertainty changes event identity, contract truth conditions, authority or write destination and cannot be resolved from the actual request/files. Do not ask for permission already supplied by the invocation.

### 0.2 Reading receipt and control manifest

Read `README.md`, `CURRENT_STATE.md`, `METHOD.md`, `CURRENT_RULES.md`, `SELECTION_RULES.md`, `CARD_AND_LOG_TEMPLATES.md`, `SCORING_AND_VALIDATION.md`, `PROBABILITY_TOOLKIT.md`, `VERIFICATION_PROTOCOL.md`, `SOURCES.md`, `ARCHIVE_USE_GUIDE.md`, `BASE_RATES_REGISTER.md`, `research/prompts/README.md`, `research/prompts/1_GAME_CARD.md`, applicable sport/competition rules and league profiles. Read this supplied prompt, the **complete** active mini, current game-log status, the pointer to the active combined log, relevant canonical entries and local carryovers. Resolve actual paths from the repository; report absent files instead of assuming them.

Published controls all come from **one full pinned commit**, not mixed branch tips or dirty local copies. Local mini/evidence files are staging inputs; local archives are evidence inputs requiring their own provenance checks, not an alternative rule authority. Disclose applicable local control differences without applying them silently. Record actual section coverage; opening a filename is not a full read.

```text
READING RECEIPT
Authority: PUBLISHED_MAIN_PINNED
Repository / branch / full verified SHA:
Read time: <ISO 8601 with UTC offset>
Method / control / selection / scoring / template versions:
Prompt revision: SF-2; primary policy: SUPPLIED_FIRST_V1
Policy deviation: supplied-only primary universe versus published policy <actual version>
Read in full: <actual files and versions>
Sections read: <actual partial reads>
Relevant local differences and which authority governed:
Active mini: <exact path / format / writer / lease / freeze status>
Canonical event/status inputs and active-log pointer:
Allowed writes / prohibited operations:
Sport/source/archive inputs and actual coverage:
Unavailable files / conflicts / affected operations:
```

If required controls, original mini or ID/lease state cannot be verified, produce `READ_ONLY_DRAFT / NOT_ISSUED`; do not claim allocation or an append. Missing sporting data may still support a retained qualitative or numeric partial card, with explicit limitations.

### 0.3 Separate status dimensions

Never use one label to stand in for all of these:

| Dimension | Values / requirement |
|---|---|
| Write status | `ISSUED_LOCAL`, `READ_ONLY_DRAFT / NOT_ISSUED`, or a verified compatible legacy status |
| Analysis status | `UNCALIBRATED_ANALYST_SCENARIO`, `UNCALIBRATED_QUALITATIVE`, `NO_FORECAST` |
| Timing | `PREGAME`, `LATE_START_UNVERIFIED`, `LIVE_OBSERVED`, `HISTORICAL_DIAGNOSTIC` |
| Selection status | 0–4 numeric formal rows; `NO_ELIGIBLE_PRIMARY` if none; qualitative ordering separately labelled |
| Definition | `OPERATOR_VERIFIED`, `FROZEN_FRAMEWORK_CONVENTION`, `UNKNOWN_DEFINITION`, `N/A` |
| Known-at | Verified available by cutoff, or `KNOWN_AT_UNVERIFIED` |
| Calibration / skill | Exact scope and artifact if established; otherwise uncalibrated / `NOT_CERTIFIED` |

Use `NOT_ESTIMATED` for unsupported probabilities, `NOT_COMPUTED` for an unexecuted/unsupported calculation, `NOT_VERIFIED` for an unverified fact, `UNKNOWN_DEFINITION` for undefined truth conditions, `N/A` for structural irrelevance, and numeric `0` only when actually supported. A missing baseline does not mean a missing card. Zero eligible picks does not mean zero research.

## GLOBAL RULE FR-5/10/15/20 — Mandatory cutoff-safe historical form

### FR1. Build the four windows for each participant

Investigate the latest **5, 10, 15 and 20 eligible completed contests separately for each team/player**. These cumulative windows overlap and constitute one body of evidence. Also expose non-overlapping blocks 1–5, 6–10, 11–15 and 16–20 where available, without relabelling partial blocks as complete.

Use unique event identities and verified completion order. Store the event trace in chronological order and identify which rows enter each latest-first window. Exclude the requested event, future/unfinished games, duplicate rows and invalid outcomes according to the metric. Date-only same-day results do not prove cutoff-safe finality. If completion time is absent, use only safely earlier-date completed events **and separately check availability of the required fields**; an earlier game date alone does not prove publication before cutoff.

Inspect actual records in `Previous Sports Results/<sport>/<competition>/<season>/`, relevant research histories and registered official/provider routes. Report files/URLs, logical rows examined, filters, exclusions, latest eligible final, capture date and field coverage. A folder, header, filename or placeholder column is not a populated, measured dataset. Apply archive integrity and point-in-time rules before using numeric features.

Track both **event coverage** and **metric coverage**. First choose the latest eligible contests, then report missing fields within them; do not silently skip a missing metric to construct a more favourable window. An alternative latest-N-with-observed-metric cohort must be separately labelled with dates and selection rule.

### FR2. Keep cohorts and denominators comparable

Default to the same competition, code, comparable format, endpoint and rules era. Identify season/stage, playoffs/cups/friendlies, home/away/neutral venue, opponent quality, surface, roster discontinuity, promotion/relegation, rest/travel and overtime/extras. Cross-competition, cross-surface and older-regime evidence belongs in a separate supplementary cohort unless an explicit supported pooling method is declared before pricing.

Calculate only supported fields: W–D–L/W–L/ties, scored/conceded means, margin, totals, exact-line empirical frequencies and applicable sport statistics. Every statistic has its own observed denominator. Report exact-line frequencies as W/P/L/V counts where definitions support them, not as calibrated matchup probabilities. Never replace missing opponent adjustment with zero; use `OPPONENT_ADJUSTMENT_UNAVAILABLE`.

Keep raw form, opponent-adjusted estimates, shrinkage and analyst assumptions distinct. Do not portray a raw hot streak or an unexplained bounce-back as a measured strength shift.

### FR3. Required participant tables and trace

Provide one table per participant in `A3-FORM`; adapt scoring columns for individual sports without suppressing coverage.

| Window | Eligible events n / target | Metric observations n | W–D–L / W–L / ties | Scored / conceded or sport metric | Margin / total | Venue split (n) | Opponent context | Last eligible final / source / missingness |
|---|---|---|---|---|---|---|---|---|
| L5 | <n/5> | <per field> | <...> | <...> | <...> | <...> | <...> | <...> |
| L10 | <n/10> | <per field> | <...> | <...> | <...> | <...> | <...> | <...> |
| L15 | <n/15> | <per field> | <...> | <...> | <...> | <...> | <...> | <...> |
| L20 | <n/20> | <per field> | <...> | <...> | <...> | <...> | <...> | <...> |
| Season to cutoff | <actual n> | <per field> | <...> | <...> | <...> | <...> | <...> | <...> |
| League / format reference | <actual n> | <per field> | <N/A if appropriate> | <...> | <...> | <...> | <...> | <...> |

Provide the event-level trace in the appendix: native ID/stable surrogate, date and completion time/status, opponent, venue orientation, score/result, endpoint, metric fields, field availability time/status, source/evidence ID and eligibility/exclusion. Each aggregate must be traceable to its actual rows. Report low coverage with actual n, never padded results. Include non-overlapping block/trend observations, definition changes and missingness.

### FR4. Integrate once, then test window sensitivity

Follow the pinned toolkit/archive recipe. Where applicable, choose the longer comparable L20 or same-regime season cohort **before looking at candidate probabilities**, print the chosen cohort and compute:

```text
r_shrunk = (n × r + k × LM) / (n + k)
```

Here `r` is the observed rate, `n` its actual metric denominator, `LM` the supported matching league level, and `k` the pinned sport/league constant. Use the stated `k=2` fallback only where the applicable pinned recipe permits it, and label it. Print scored/conceded inputs separately, original and shrunk values, the unadjusted distribution and all adjustments. Missing LM does not license invented shrinkage.

The diagnostic `B=(L5+L10+L15+L20)/4` is a predeclared **shadow**, not four independent priors or an extra strength term. If a window is absent, do not substitute another window into B without renaming/documenting the alternate recipe. For partial windows show actual denominators and label the comparison partial. If recency weighting is authorised, use one documented per-game decay or non-overlapping block weights summing to one; do not claim arbitrary weights are optimal.

Only a documented current mechanism can support a short-window centre shift under the controls. Keep adjustments separate and avoid counting roster, opponent or venue effects twice. Starter/goalie/QB histories and team histories are overlapping evidence, not independent confirmations.

Compare supported L5/L10/L15/L20 parameter scenarios with the **same contract universe and all other inputs fixed**. Print expected-score changes, each supplied probability, top-two changes and gates. Mark `FORM_WINDOW_SENSITIVE` when order changes; use `WINDOW_SENSITIVITY_NOT_COMPUTABLE:<reason>` where necessary. Do not choose the best window after outcomes. Freeze the recipe, cutoff, cohort, constants, feature/source versions and sensitivities at issue.

### FR5. Confirm lineups or price supported uncertainty

Investigate official starters, usable bench/substitutes/reserves and key inactives before lineup-dependent pricing and final issue. Record exact names, source/publication time where known, retrieval time, lineup completeness and availability at cutoff. A probable lineup, injury report or current roster does not equal a confirmed matchday sheet.

Use `LINEUP_GATE: CONFIRMED / PARTIALLY_CONFIRMED / UNCONFIRMED / NOT_APPLICABLE`. Record starters, bench and relevant specialist positions separately; confirmed starters do not prove a confirmed active bench. Singles tennis uses participation/withdrawal verification and `NOT_APPLICABLE` for a team lineup.

Unconfirmed personnel alone does not force `NO_FORECAST`. Where credible participant/rotation alternatives and numeric effects exist, freeze named low/base/high or categorical scenarios **before pricing** and mix their event distributions. If the pinned rule uses 0.25/0.50/0.25, disclose these as provisional analyst weights unless independently supported. Named alternatives need coherent dependencies; do not combine mutually exclusive player configurations. Unsupported scenario magnitudes remain qualitative.

Basketball: five plus active rotation; soccer: XI, keeper, substitutes; cricket: playing XI and announced toss/impact-player eligibility; baseball: pitchers, batting order, bullpen availability; hockey: goalie, lines, scratches; rugby: starters, bench, late changes; AFL/AFLW: selected side, interchange/substitute rules and late outs; American football: QB, inactives, active relevant starters. Verify the exact competition's announcement practice.

Follow the published two-step target where available: substantive research around T−60, then official lineup/state check and repricing before freeze, aiming for T−5. A late request still receives complete research. These are schedule targets, not retrospective timestamps or reasons to discard events. No automatic future refresh exists unless a real job was created within scope.

### FR6. Evidence-backed form audit

In A3 include `A3-FORM` and `A3-LINEUPS`; in A4 show feature arithmetic, mixture and window sensitivities; in A6 show adjustments; in A7 show lineup/window flags and family checks; in A8 list unresolved tasks; in A9 audit FR1–FR6 with evidence pointers and `PASS / PARTIAL / NOT_VERIFIED / FAIL`.

Mandatory investigation does not mean mandatory invented numbers. Supported partial estimates keep actual n. Qualitative research keeps all supplied rows. `NO_FORECAST` is reserved for an event/evidence situation that cannot support a responsible sporting direction. Preserve the original event ID and issue-time values in later addenda.

## GLOBAL POLICY SF1–SF12 — Supplied-only primary ranking and immutable records

### SF1. Explicit policy scope

`SUPPLIED_FIRST_V1` changes **primary candidate eligibility** to user-supplied contracts only. Disclose the deviation from the actual pinned published policy; the predecessor's comparator was `P_ORDER_V2`. All other supported controls apply. Do not call a supplied-only gate the published full-universe gate or merge their evaluation cohorts.

Keep `PROMPT_REVISION=SF-2`, selection-policy version, model/parameter version and actual execution versions distinct. A prompt rewrite is not retroactive authority to alter issued cards. Canonical import must explicitly recognise the local policy and format extension before treating it as comparable to another selection policy.

### SF2. Freeze the literal user universe before modelling

Any **nonempty number** of supplied contracts is valid. Preserve order, verbatim text and one `RAW_INPUT_INDEX` per literal occurrence. Define a stable contract key using event identity, quantity, participant orientation, direction, exact threshold and units, period/phase, endpoint and action/void convention. Record the key schema and actual identity/definition fields, not just a hash.

Deduplicate **identical resolved keys**, retaining every raw-input mapping. Opposite sides and alternate thresholds remain distinct. An apparent repeated Over is not an Under unless the user corrects it. User-defined propositions need not have been bookmaker offers; supplied thresholds are metadata, not odds/model inputs.

Resolve material ambiguity before numeric pricing. If an operator contract is intended but its terms are unavailable, retain `UNKNOWN_DEFINITION`; do not silently replace it with a house convention. A framework convention may be frozen only where authorised and must be labelled. Unresolved rows remain visible while other rows are researched.

Freeze `SUPPLIED_UNIVERSE_ID`, ordered raw ledger, deduplicated keys, key schema, definitions and counts. Use a real manifest/hash when tools permit; never invent one. Later supplied lines receive a dated addendum/new analysis under the same event identity, labelled `NOT_PRIMARY` relative to the original slate. They cannot replace its original training targets.

### SF3. Price every supported distinct supplied row

For each supported row derive **unconditional** masses from its actual compatible event model:

```text
W + P + L + V = 1  (within declared numerical tolerance)
decisive_mass = W + L
p_card = W / (W + L), when decisive_mass > 0
outright_win_probability = W
```

Print both `p_card` and decisive mass so a large push/void share is visible. The requested ranking follows published conditional `p_card` arithmetic; make clear that it ranks success **among decisive outcomes**, not necessarily unconditional outright wins. An unconditional-W ordering may be a separately labelled shadow if useful.

Draw/tie is a sporting state whose W/P/L/V mapping depends on the frozen row. Unknown abandonment/retirement probability does not become a claimed measured zero. If the model is conditional on a valid completed event, state that conditioning and do not present its W/P/L/V as a complete all-event forecast. Retain action exceptions and the unsupported all-event void probability explicitly; apply the pinned contract/selection rules to eligibility.

Report `p_base` from the base scenario and `BASELINE_P` from independent league-only inputs. Neither is a synonym for `p_card` or the other. Keep true probabilities above 90% and below 50%; never clip, pad with 0.5 or omit unfavourable supplied rows.

Quarter/split lines and multi-leg propositions need their own supported action/payoff mapping. Do not force half-win/half-loss states into binary W/P/L/V, silently split one user proposition into two primary rows or multiply leg probabilities. If the pinned toolkit lacks compatible arithmetic, retain the literal row as `NOT_ESTIMATED: UNSUPPORTED_ACTION_STRUCTURE` or separately labelled diagnostic components.

### SF4. Deterministic complete ranking and formal selection

1. Build `U_supplied` from resolved unique supplied keys. Unresolved raw inputs remain in the ledger with provisional identifiers, never merged by assumption.
2. Calculate supported rows from compatible distributions. Numeric rows sort by **unrounded p_card descending**, then stable key for exact ties. Unsupported rows follow in raw-input order, with no numeric rank/probability. Near ties retain the calculated order and a precision warning; do not treat unequal values as exact ties.
3. The first user-visible selection table is `SUPPLIED_CONTRACT_RANKING`, containing **all distinct supplied rows**, including excluded and unsupported ones. It contains no derived contracts.
4. Apply hard support/definition/known-at requirements and the pinned 90% selection ceiling. Retain true above-ceiling p with `EXCLUDED: ABOVE_SELECTION_CEILING`; equality is allowed when precision resolves it. A boundary unresolved at actual precision receives `ELIGIBILITY_UNRESOLVED_PRECISION`, with its numeric evidence retained.
5. Apply sport/family prerequisites. Where a published restriction concerns **would-be Rank 1 only**, test the current highest eligible row, remove it from the formal set if inadmissible, record the reason and repeat. Do not apply a Rank-1-only test as a blanket exclusion of every lower row or quietly demote an inadmissible row in a supposedly sorted table.
6. The first up to **four** remaining numeric rows become `PRIMARY_RANKS`. Ranks 1–2 are `PICK`; 3–4 are `INFORMATIONAL`. All additional supplied rows remain in the complete ranking and ledger. No fifth primary pick is silently counted.
7. The general 0.62/0.04 Rank-1 gate and 0.58 Rank-2 floor are **disclosed diagnostics**, not automatic row replacements. A lower general floor is flagged, not erased. Distinguish these from mandatory sport/family eligibility checks. Report 0 or 1 pick honestly; do not invent Rank 2 or promote a derived row.

If no numeric formal row survives, use `NO_ELIGIBLE_PRIMARY` while returning the full research and numeric/qualitative ledger. A supported qualitative ordering is separate, has no numeric PASS/proper score and never displaces numeric picks by an invented probability.

### SF5. Gate scope and numerical precision

Calculate `SUPPLIED_SCOPE_GATE` against the best eligible **non-complementary alternative in the complete eligible supplied universe**, not just the four displayed formal rows. Another threshold on the same quantity is still an alternative. Identify the alternative key/p, gap, provisional floors, family prerequisites and actual numerical error epsilon. If no valid alternative exists, use `NOT_ASSESSABLE`; one row or an exact complementary pair cannot manufacture a gate pass.

Apply the pinned precision rule using the calculation actually performed. The reference v11 rule uses `GATE_UNRESOLVED_PRECISION` around 0.62 within epsilon and 0.04 within 2epsilon, and `PRECISION_TIE` for probabilities within 2epsilon. A 2-decimal normal-table interpolation has its stated approximation error; executed code uses its own integration/truncation/sampling limits. Treat the ceiling and sport/floor boundaries consistently. Round for display only. A simulated estimate requires seed, sample size and its numerical sampling uncertainty.

Report `PASS / RANK1_UNSTABLE / GATE_UNRESOLVED_PRECISION / NOT_ASSESSABLE` with evidence. A supplied-scope PASS does not establish accuracy, calibration or a canonical full-universe PASS.

**Reference sport/family tests to verify against the pinned controls:**

| Would-be Rank-1 family | Reference v11 prerequisite | Interpretation |
|---|---|---|
| Soccer first-half Over 0.5 goals | Supported half-specific rate/model; p_card ≥ 0.72; lead ≥ 0.05 over the best eligible non-complementary supplied alternative | Full-time goal intensity is insufficient. Apply the stronger test only to the proposed top row; an unavailable comparator is not a PASS. |
| Baseball selected team +1.5 runs | p_card ≥ 0.65; supported directional win/tie/action and exactly-one-run-loss states | League absolute one-run frequency is insufficient. The general supplied-scope lead diagnostic still applies. |
| Tennis game totals/handicaps | Reproducible compatible point/set/match construction or authorised supported approximation, with format/form sensitivity | A match-winner probability alone does not price games; retain match-losing terminal states. |
| Corners / period / player lines | Exact provider-backed field, compatible model, endpoint/action definition and capture plan | Other quantities cannot supply the absent statistic. Cross-family joint loss needs its own construction. |

These are reference rules, not permanently fixed facts. Print any difference in the actual pinned version and apply that version. If a required top-row family test is unresolved, retain the row's estimate but do not label it an eligible Rank-1 PASS; use the prescribed exclusion/unresolved disposition and disclose any effect on the formal slate.

### SF6. Optional shadows have declared universes

Only after the supplied universe is frozen may a bounded supported derived ladder be declared **before its own pricing**. Record range/step/quantity/endpoint, exclusions and actual enumerated keys. Do not search until an easy line passes or call a limited ladder exhaustive. Deduplicate supplied keys appearing in the ladder and retain their supplied provenance.

Where computable freeze `SHADOW_MAIN_P_ORDER_V2` or the correctly named current published-policy comparator, plus `SHADOW_MAIN_POLICY_GATE`, over its declared combined universe. A partial universe is explicitly partial. Lack of a defensible shadow never stops supplied research.

For supplied-scope diagnostics freeze the supported published shadows: `SHADOW_GATE_RET03`, `SHADOW_R2_RET04`, `SHADOW_R2_XCARD6`, `SHADOW_RANK_DELTA`, `SHADOW_BASE_ONLY`. Print each one's universe, eligibility, recipe, actual outputs or `NOT_COMPUTED:<reason>`. They remain `NOT_PRIMARY`, consume no event ID and cannot repair original picks or grades.

### SF7. Dependence, complements and mechanical protection

Identify underlying quantity keys. Reversing margin sign does not create a different quantity. Distinct families/players may share pace, score state, personnel or other drivers.

For unconditional loss masses `l1=L1`, `l2=L2`:

```text
Exact joint loss = sum of shared states where both frozen contracts lose.
Absent a justified joint model:
max(0, l1+l2-1) <= P(both lose) <= min(l1,l2).
```

Nested loss sets give the smaller loss mass; disjoint losing sets give zero. Use neither `(1-p1)(1-p2)` nor independence without a justified construction. Cross-family goal/corner or score/player joints need a genuine joint model; otherwise show bounds or unavailable status. A conditional-on-both-decisive joint requires the **joint** denominator `P(both decisive)`, not marginal conditioning or a fabricated point estimate from bounds.

Same-line opposite half-point sides may be `COMPLEMENTARY_PAIR / MECHANICALLY_PROTECTED` only under matching definitions and endpoint. Integer pushes, voids, draws, abandonments and differing endpoints require their actual structure. `P(both lose)=0` does not imply guaranteed at least one win: pushes/voids may prevent any decisive result. Report both-loss and at-least-one-win separately where supported.

Disclose the pinned provisional joint-risk targets/warnings (reference v11: 0.30/0.35); they do not silently reorder probability-sorted primary ranks. Mechanically protected Hit@2 is a construction diagnostic, not predictive skill.

### SF8. Freeze issue-time records; defer outcomes

For every supplied row retain event key/native ID, working ID or `NOT_ALLOCATED`, universe ID, raw indices/verbatim text, key/definition schema, original `p_card`, `p_base`, `BASELINE_P`, W/P/L/V and conditioning, numeric rank, eligibility/exclusion, primary role, line difficulty, model/parameter/recipe IDs, scenario weights, cutoff/issue times, known-at/evidence coverage, timing/exposure, policy/prompt versions and calibration status.

These are **candidate research records**, not automatically qualified training observations. Preserve unpriced/excluded/late records; freeze their eligibility/missingness labels. Do not assume unknown lineage, known-at or policy recognition is a passed training gate. Hashes establish byte custody, not source truth.

Prompt 1 neither settles nor trains a model. A later authorised settlement appends verified sporting fields and frozen-definition `WIN / LOSS / PUSH / VOID / UNRESOLVED` with evidence/time, preserving every issue-time value. Unknown evidence is not VOID. Historical/live analyses remain outside the prospective pregame cohort.

Later proper scores apply only to supported **decisive** binary actions: Brier `(p-y)^2`; log loss `-[y ln(p)+(1-y) ln(1-p)]`. Print PUSH/VOID/unresolved exclusions and denominators. Do not silently clip p=0/1: an impossible assigned outcome has infinite log loss, or a predeclared evaluation convention is reported separately. Quarter/multiclass outcomes require compatible scoring rules.

Pair candidate/baseline scores only at the **same frozen line, endpoint, action convention and observation**. Missing baselines remain missing. Group dependent rows by event, then calendar/time blocks; split chronologically with no match/feature leakage. Stratify by sport, competition, format, contract family, timing, policy, model recipe, evidence and protection. A changing supplied-contract mix changes difficulty.

Future reports should retain coverage, Rank-1/Rank-2 decisive rates and proper scores, complete supplied-row scores/calibration with n, paired baseline skill, event-level joint outcomes, protection flags and separate shadows. Calibration requires its own held-out evidence; a prompt, arithmetic check or single successful event cannot establish it.

### SF9. Honest partial research

Research all supplied families, but price only those with resolved definitions and source-supported model inputs. Period/player/corner rows need their actual fields/model; a match final cannot produce absent half, corner or player statistics. A unsupported row never receives a fabricated zero, 50%, confidence grade or convenient replacement line.

If a simple approximation is defensible, name it, compute it and report limitations. Otherwise retain a specific evidence-backed qualitative assessment with `NOT_ESTIMATED`. If neither event identity nor evidence supports a responsible sporting direction, use `NO_FORECAST` and record the concrete missing inputs.

### SF10. Timing and outcome exposure remain separate

Maintain request time, analysis cutoff, source publication/update time where known, retrieval times, research completion, final state recheck and actual issue time separately. Use ISO 8601 with offsets plus venue zone, UTC and `Australia/Sydney`; derive daylight saving from the event date, never assume a permanent AEDT/AEST offset.

| Timing class | Required meaning |
|---|---|
| `PREGAME` | Credible explicit not-started evidence at actual issue; inputs available by cutoff |
| `LATE_START_UNVERIFIED` | Scheduled start passed; reliable not-started/live status unavailable |
| `LIVE_OBSERVED` | Event underway or in-game state exposed; declare conditioning and remaining horizon |
| `HISTORICAL_DIAGNOSTIC` | Final known/outcome exposed or historical reconstruction; no prospective credit |

Also record `OUTCOME_EXPOSURE: NONE_OBSERVED / LIVE_SCORE / FINAL_KNOWN / UNVERIFIED`, first exposure time/source and whether it influenced research. An old cutoff does not remove later outcome exposure. A stale 0–0 does not prove not-started. Scheduled lateness alone does not prove the event began; a verified delayed not-started event can remain PREGAME, with the delay disclosed.

Freeze cutoff at the final admissible input snapshot. Pre-issue updates require a dated snapshot/repricing receipt with a revised declared cutoff; do not silently keep an older cutoff while using later lineups. After issue, new information is an addendum/shadow, never an overwrite. Retrieved-after-cutoff data need evidence of actual earlier availability; retrieval time alone neither proves nor disproves that availability.

`CONTINUE_IF_LATE=YES`: never rush, drop a requested event solely for lateness or auto-settle. Complete supported research in its honest cohort. An unsupported live-conditioning model is not a pregame model reused as an exact live forecast.

### SF11. Writer, ID, format and append custody

Read the full mini, its lease/handover, freeze/settlement status and authoritative current sequence. Only its authorised unexpired writer appends. A frozen mini remains frozen; use another already authorised destination only when the invocation and controls permit, otherwise return a draft. Log intake for every requested event, including duplicates, qualitative and NO_FORECAST outcomes, **only when that intake write is authorised**; otherwise include a proposed draft intake row.

Search relevant mini/carryover and canonical **bodies**, aliases and status records. Same event means a dated addendum under the original working ID; postponed games are alias/state changes unless verified as genuinely distinct. Doubleheaders require native IDs/game numbers. New-event allocation must reconcile current state and outstanding local sequence; genuine disagreement blocks allocation, not research. Do not treat an old log-opening snapshot as current conflicting state.

Before mutation, retain the real byte/hash/block inventory required by the verification protocol, then recheck the mini has not changed since read, writer/lease remains valid and freeze status permits append. Use the allowed append/footer mechanism; preserve earlier issued blocks byte-for-byte and avoid newline/encoding normalisation of historical content. Add local-policy fields in a compatible appendix/extension, not by rewriting old cards. Do not mark a receipt complete before the checks it describes occur.

Append one complete new card before the footer, or one dated addendum for an existing event. Update only permitted intake/footer/ID totals. Only a complete written/read-back new card advances the local footer; addenda do not consume IDs. Canonical IDs remain unconsumed until the authorised import workflow. A failed/incomplete write is not an issued card; disclose exact state and repair only the authorised operation.

Read back the actual files, confirm earlier block hashes, new row/key counts, probabilities/times, exact ID and footer continuity. Run available applicable structural checks within scope. If an optional checker is absent, mark it absent; do not fabricate its result. Where full append integrity cannot be verified, report `ISSUANCE_NOT_VERIFIED` or the compatible draft status instead of claiming success.

### SF12. Output order and self-audit

Start with event identity, timing/analysis/write status and numeric coverage. Then print **all supplied contracts in `SUPPLIED_CONTRACT_RANKING` as the first selection table**, followed by formal supplied-only picks, gate/dependence, supplemental sporting conclusion, evidence/form/lineup details, sensitivities, optional shadows, missing tasks and custody/footer receipt.

Keep the decision block near the pinned template's limit (reference v11: about 650 words); put full literal ledger, calculation, form and evidence tables in A1–A9. Length control never permits omitted supplied rows: a long complete table may live in A5 and be linked accurately from the decision block. Return the full new card/addendum, or a complete non-issued draft; do not substitute a summary for the retained artifact.

Audit `SF-A1…SF-A12` in A9:

| Check | Required evidence |
|---|---|
| SF-A1 | Ordered literal ledger complete; raw-to-distinct mapping and counts reconcile |
| SF-A2 | Identity/orientation/period/endpoint/action definitions resolved or explicitly missing |
| SF-A3 | Every distinct supplied row priced from supported inputs or reason retained |
| SF-A4 | Full numeric ranking follows unrounded p and deterministic exact ties |
| SF-A5 | Every formal primary key was literally supplied; no derived substitutions |
| SF-A6 | Hard eligibility, ceiling and Rank-1-only family filtering applied transparently |
| SF-A7 | General diagnostics, family gates, competitor scope and numerical precision correct |
| SF-A8 | Shared losing states/bounds, complements and protection honestly labelled |
| SF-A9 | All shadows have declared universes and remain NOT_PRIMARY |
| SF-A10 | Original parameters, masses, probabilities, baselines, inputs and times frozen |
| SF-A11 | Known-at, timing, cutoff revisions and outcome exposure preserve cohort separation |
| SF-A12 | Correct format/ID/lease/freeze/intake/footer/readback; prior bytes preserved; no GitHub write |

Print `PASS / PARTIAL / NOT_VERIFIED / FAIL` with the actual evidence pointer or defect for each. Apply the current mini's own checklist too (reference `mini-log-7`: C1–C20); legacy formats keep their original checks plus dated compatibility notes. A checklist printed without evidence is not a passed audit.

## QUANTITATIVE IMPLEMENTATION — Apply in every sport's Step 4

### Q1. One coherent event construction per compatible family

Freeze the model family, parameters, data snapshot, endpoint, orientation, scenario recipe and numerical method before selection. Winner, total, handicap and team scores must be marginals/functions of compatible event states. Auxiliary families may use separately supported models, clearly labelled; an absent cross-family joint remains absent.

Print parameter values/units, source or analyst basis, formulas, normalization, tail support, transition rules, integration/truncation error and covariance. A declared model name does not prove its execution. Record command/script/notebook, relevant versions, seed and sample size when actually used. Prefer supported executable arithmetic over hand-waved calculations; do not create unrequested dependencies or claim a simulation that did not run.

For team scores X and Y, where the endpoint makes them meaningful:

```text
T = X + Y; M = X - Y  (freeze which participant is X)
E[T] = E[X] + E[Y]; E[M] = E[X] - E[Y]
Var(T) = Var(X) + Var(Y) + 2 Cov(X,Y)
Var(M) = Var(X) + Var(Y) - 2 Cov(X,Y)
```

Use a valid joint distribution/covariance matrix. These identities do not identify unknown SDs/covariance. A continuous approximation has zero exact integer-tie/push mass; it cannot support discrete action rules without a documented compatible discretisation or discrete model. Correct key-number/low-score/tie mass on the common distribution, renormalise and rederive every affected row.

Evaluate exact signed thresholds from the frozen contract. For participant X with signed handicap h, the adjusted margin is `X-Y+h`: positive wins and negative loses; equality is a push only under that row's frozen action rule. For an ordinary total q, Over wins at `T>q`, Under wins at `T<q`, with equality mapped by its actual convention. Half-point thresholds on integer quantities have no equality state; integer and split thresholds do. Mirror the orientation correctly for participant Y. Do not infer draw/retirement action from these inequalities alone.

### Q2. Mix state probabilities before conditioning

When uncertainty scenarios are required, give named coherent scenarios s and nonnegative frozen weights w_s summing to one. The event distribution is `P(state)=sum_s w_s P(state|s)`. For each contract:

```text
W_mix = sum_s w_s W_s; P_mix = sum_s w_s P_s
L_mix = sum_s w_s L_s; V_mix = sum_s w_s V_s
p_card = W_mix / (W_mix + L_mix)
p_base = W_base / (W_base + L_base)
```

**Do not average scenario p values when decisive masses differ.** Do not add the base distribution again on top of the mixture or average SDs. Mixture moments obey `mu_mix=sum_s w_s mu_s` and `Var_mix=sum_s w_s[Var_s+(mu_s-mu_mix)^2]`; covariance includes between-scenario movement too.

Weights are analyst assumptions unless measured/estimated with documented evidence. Scenarios represent coherent joint alternatives, not an unexamined Cartesian product of overlapping adjustments. Print each scenario's inputs, masses, p, score moments, ranking and gate; ranges are sensitivity ranges, not confidence intervals. Keep required form-window comparisons distinct from personnel/weather scenarios; do not automatically mix all alternative models into one extra distribution.

### Q3. Independent fixed same-line baseline

Attempt `BASELINE_LEAGUE_V1` at every supported supplied proposition's exact threshold, orientation, period, endpoint and conditioning. Use its **own league-only** data and frozen recipe, excluding matchup/team/lineup/form/outcome inputs. Shared original data sources may overlap with feature data; independence here concerns the recipe's exclusion of matchup information, not a fabricated independent collector/sample claim.

Use a supported league distribution or the authorised empirical W/P/L/V cohort. Print baseline ID/version, fields, parameters/counts, seasons, exclusions, n, latest eligible event, capture/known-at, and decisive denominator. A mean/SD alone does not identify a discrete, extras, tennis or phase baseline. Team-model aids such as TB-1-MD are not automatically league-only baselines. Never retune the baseline after comparing it with candidate p or backfill it after outcomes.

For missing baselines use the pinned reason vocabulary (reference v11: `NO_LEAGUE_PROFILE`, `PROFILE_LACKS_ENDPOINT`, `DISCRETE_FAMILY_UNSUPPORTED`, `NEW_FORMAT_NO_PRIOR`, `SOURCE_UNREACHABLE`, `OTHER:<reason>`), with attempt/source/time and next task. Print coverage for **all numeric supplied rows** and separately for **numeric formal rows**, so neither denominator is hidden.

### Q4. Arithmetic and selection checks

Verify before issue:

- State/mass normalization within a declared tolerance; residual truncated tail reported, not silently erased.
- Nonnegative W/P/L/V, bounded p, valid decisive denominators and matching baseline conditioning.
- Score/margin/total moment identities where applicable, correct participant signs, discrete thresholds and exact-line push rules.
- Monotonicity across alternate lines of the same quantity and action convention; compatible complements/multiway winner masses.
- Mixture arithmetic before conditioning; scenario weights and moments correct.
- Complete literal/unique row counts, supported/unpriced disposition, correct unrounded ranking and eligibility/gate comparisons.
- Joint-loss claims supported by common states or valid bounds and clearly defined conditioning.

Document an actual failed check and resolve it before numeric issue; retain independent research and draft outputs. Computational correctness does not establish source truth, calibration or predictive skill.

## EXTENDED SPORT WORKFLOWS

Use the common rules above **and all seven steps of the relevant section below**. Do not replace a sport section with a generic summary. For multiple requested events, execute the workflow for each event; retain each supplied ledger and report all outcomes, including incomplete research. Source suggestions are routes to verify, not claims that a provider presently exposes every field.

---

## BASKETBALL

### Event input — fill before executing this sport's seven steps

```text
Upcoming Basketball Game: <participants; exact competition; season/stage/format; date/time/timezone>
Native event ID / game number / official URL: <if supplied; otherwise verify>
Venue / home-away orientation: <if supplied; otherwise verify>
Active mini: <exact existing authorised local path, or identify from accessible files>
Supplied contracts (one literal proposition per line):
1. <exact user text>
2. <exact user text; optional>
3. <additional exact user text; optional>
Contract period / endpoint / action terms: <explicit supplied terms; resolve missing material definitions>
Requested primary ranking: SUPPLIED CONTRACTS ONLY
Optional derived shadows: <requested / useful supported diagnostics only>
Research: Confirmed starting five and active rotation; injuries/minutes; pace/efficiency; L5/L10/L15/L20; regulation and overtime endpoint.
CONTINUE_IF_LATE: YES
GitHub main: READ ONLY; settlement/import: NOT_PERFORMED
```

Any nonempty number of supplied contracts is valid. Remove unused placeholders; do not treat them as propositions or populate them with invented examples.

### 1. Read and establish authority

Complete 0.2 from one verified full published SHA. Read the applicable sport/competition rules, SOURCES routes, league/tour profiles, archive guide/defect notes and base-rate register as well as the full active mini and relevant canonical records. Locate actual filenames/sections; do not invent a sport rules file or use an outdated league constant without disclosure. Print the reading receipt, actual versions, authority differences, permitted writes and unavailable dependencies.

Current controls govern over historical engine notes. If authority/custody inputs needed for issuance are inaccessible, complete the research as `READ_ONLY_DRAFT / NOT_ISSUED`.

### 2. Identity, duplicate and timing gate

Verify participants, competition/league (NBA, WNBA, NBL, B.League, ACB, EuroLeague, FIBA, etc.), season, stage, venue, native ID/game number, official scheduled start, venue zone, UTC and Australia/Sydney time.

Apply SF10/SF11: search all relevant local mini/carryover and canonical bodies/status by native ID, event key and aliases. Doubleheaders, resumed events and postponements need explicit identity handling. A duplicate receives an addendum under its existing ID. Log authorised intake whatever the research outcome; otherwise include a draft intake row.

Verify the named mini, format, writer/lease, freeze status, current canonical allocation and outstanding local sequence. Do not reserve, skip, collide, renumber or consume a canonical ID. Keep analysis cutoff, research completion, actual issue and state recheck separate. Complete the two-step lineup/repricing target when timing permits; research comprehensively if late. Recheck actual state immediately before issue. Outcome exposure prevents prospective pregame credit, even with a reconstructed earlier cutoff.

### 3. Evidence, roster and archive

Follow official field-owner (league match centre / box score) → structured provider (RealGM, ESPN, etc.) → quality corroboration routes. For each decisive claim retain URL, exact field/value or brief extract, source publication/update time when known, retrieval time and provenance/lineage. Log inaccessible/stale/conflicting sources. Three domains are not three independent collectors. No odds/tips/previews/fantasy inputs.

Verify rotation, minutes, injuries, rest/travel, and especially **confirmed starting fives and active bench/reserve availability**; probable is not confirmed. Distinguish fact, historical estimate and analyst assumption. Inspect actual archive contents under `Previous Sports Results/Basketball/<league>/...` and print files, logical rows read, season/endpoint filters, latest usable date and missingness. Use only results known before cutoff; a date alone does not prove a same-day game had finished. Do not use postgame narrative or full-season aggregates from after cutoff. Check profile freshness against the pinned recipe and competition/rules era; where the applicable rule flags STALE_PROFILE, investigate current sources and price supported sensitivity. Missing replacement data does not justify a fabricated refresh.

#### Mandatory historical-form implementation for this sport (FR1–FR6)

Use points for/against, estimated pace/possessions and ORtg/DRtg **only if real possession/efficiency fields exist**; track regulation/OT scoring, home/away splits, rotation minutes and opponent defensive quality. Do not transfer NBA 48-minute scoring to FIBA/NBL 40-minute leagues. The last 5/10/15/20 rows must be traced for both teams. Check the official matchday starting five and active bench; where unconfirmed, apply supported low/base/high lineup scenarios (or report missing numeric support). Follow the GLOBAL RULE above for both participants; place the required four-window tables, event-level trace, missingness, non-overlap trend, opponent adjustments and official lineup gate in A3; propagate supported numbers to A4 and disclose window-choice sensitivity in A7/A9. Never treat these historical summaries as a fitted/calibrated model.

### 4. Distribution, expected score and comparator

Build the simplest defensible coherent basketball distribution you can actually calculate: calculate possessions × efficiency centres (ORtg/DRtg per 100 possessions), team covariance, total/margin normal or compound widths, and supported explicit regulation-tie/overtime transitions (or a labelled approximation). Print every parameter and its basis, formula/table, normalization, tail treatment, covariance and endpoint transitions. A named family is not evidence that a grid or exact simulation was computed. If the required calculation cannot be done, report a supported approximation with limitations, or qualitative research with NOT_ESTIMATED probabilities.

Produce expected score terms from CARD_AND_LOG_TEMPLATES §3a: team points (means & SDs), total points (mean & SD), and signed margin (mean & SD). Keep zeros; mark missing or irrelevant terms. Print all winner/draw/tie masses. For **every distinct user-supplied contract** retain unconditional W/P/L/V and p_card=W/(W+L), with denominator and action convention; all other priced candidates are separate NOT_PRIMARY shadows.

Attempt BASELINE_LEAGUE_V1 on **each supported supplied contract's exact same line and endpoint** from independent league-only inputs, frozen before issue. Print recipe, source cohort/n/cutoff and parameters separately from the team model. No 0.5 placeholder or retrospective baseline fill. Missing baseline does not stop the card; it limits later skill measurement.

If inputs are unfitted/stale/early-season/unconfirmed, price the **declared low/base/high mixture** (default 0.25/0.50/0.25, frozen before ranking) and show `p_base` and p_card for every supplied line. Show an adjustment table (home venue, rest/travel, availability/minutes), unadjusted distribution/pair and low/base/high sensitivity on material uncertain inputs. Any adjustment-driven pair change is ADJUSTMENT_DEPENDENT, even below 0.25 SD. Report plausible probability ranges as sensitivity, not confidence intervals. Do not move individual probabilities outside the shared model.

**Basketball implementation safeguards.** If supported, use a frozen matchup-efficiency recipe with `expected points = expected possessions × points per 100 possessions / 100`, correctly aligned for both teams. A score-history fallback is `SCORE_BASED_APPROXIMATION`, not a fitted pace/efficiency model. Do not derive exact possession counts from scores alone. Player scoring requires minutes/usage/efficiency and a compatible team/player construction, not allocation of the team mean by guesswork. Quarter/half features require observed period fields and reconciliation with regulation/OT totals. A continuous normal model alone has no integer tie mass; overtime probability and integer pushes require a compatible discrete/tie construction. Use supported league-specific OT transitions, including repeated OT where relevant; Poisson OT scoring is an optional disclosed approximation, not a compulsory exact simulator.

**Required execution for this section:** apply Q1–Q4, SF3 and FR4/FR5. Mix unconditional masses before conditioning; print p_base separately. Preserve action/definition/known-at limits, score moments, exact supplied-line baseline coverage, numerical error, adjustment table, unadjusted pair and scenario/window rank changes. An absent supported field or calculation stays missing.

### 5. Supplied ranking, eligibility, gates and dependence

Freeze the literal deduplicated user-supplied universe and definitions before modelling. Price all supported supplied keys from the actual compatible distributions; keep every unresolved/unpriced/excluded row visible. Follow SF4 for the complete probability-sorted `SUPPLIED_CONTRACT_RANKING`, 90% selection ceiling, known-at/definition support and any would-be-Rank-1-only family filtering. Select 0–4 actual numeric supplied rows; only Ranks 1–2 are primary picks. The general 0.62/0.04 gate and Rank-2 0.58 floor are transparent diagnostics; specific mandatory family prerequisites remain eligibility tests. Never pad or substitute a derived contract.

Show `SUPPLIED_SCOPE_GATE`, competitor key/p/gap, precision error, floor/family status and the best supported non-complementary supplied alternative. Show line difficulty in units and z where SD is supported. Compute exact joint losing-state mass, valid Fr?chet bounds or an explicit unavailable result under SF7; show both-decisive conditioning only with a genuine joint denominator. Flag complements and mechanical protection. Do not reorder primary picks to hide dependence or call protected Hit@2 predictive skill.

Optional derived ladders and published-policy comparators have separately predeclared universes. Freeze supported RET03/RET04/XCARD6, rank-delta and base-only shadows with their correct names and scopes, or state why not computed. All are NOT_PRIMARY and cannot change the original supplied slate, ID or grade. Retain every supplied row as a candidate research record with its separate future training eligibility.

### 6. Playing conditions and frozen action rules

Verify the exact competition/season/stage regulation duration, quarter length, foul-out and bonus rules, overtime length/repetition and final-score convention. NBA, WNBA, FIBA, national and collegiate rules are not interchangeable. Freeze whether each row includes OT; player/period actions need their actual participation and endpoint terms. A stale/missing profile is disclosed and tested, not silently replaced with NBA defaults.

### 7. Write, audit and return

Use the mini's own applicable CARD_AND_LOG_TEMPLATES format; retain the near-650-word decision target where prescribed and full A1–A9 evidence. Record literal/normalised contracts, common-distribution calculations, baseline coverage, full supplied ranking, formal picks, all missingness, source receipts and original model/scenario/recipe versions. Freeze the exact later settlement fields, action definitions and capture plan without performing settlement.

Apply SF11's pre-write concurrency/lease/freeze/ID checks and original-block custody. Append one complete card before the footer for a genuinely new event, or one dated addendum for an existing event; update only authorised intake/footer totals. Preserve all earlier issued bytes. Read back the actual write, reconcile keys/counts/probabilities/timestamps/footer and verify prior blocks. A draft or failed verification cannot claim a successful append/ID advance.

In A9 complete the mini's actual checklist (C1–C20 for reference mini-log-7, or the original legacy checklist plus dated compatibility gaps), FR1–FR6, SF-A1–SF-A12 and Q4 calculation checks with specific evidence/status. Return the full new card/addendum or complete non-issued draft, exact path, working ID/status, timing/exposure, all supplied probabilities, supplied-only formal picks or precise no-pick reason, gate/joint/sensitivity/baseline results and updated footer/readback receipt. Explicitly state settlement NOT_PERFORMED, canonical import NOT_PERFORMED, GitHub writes NO and new canonical IDs 0. Make no success guarantee.

---

## CRICKET

### Event input — fill before executing this sport's seven steps

```text
Upcoming Cricket Match: <participants; exact competition; season/stage/format; date/time/timezone>
Native event ID / game number / official URL: <if supplied; otherwise verify>
Venue / home-away orientation: <if supplied; otherwise verify>
Active mini: <exact existing authorised local path, or identify from accessible files>
Supplied contracts (one literal proposition per line):
1. <exact user text>
2. <exact user text; optional>
3. <additional exact user text; optional>
Contract period / endpoint / action terms: <explicit supplied terms; resolve missing material definitions>
Requested primary ranking: SUPPLIED CONTRACTS ONLY
Optional derived shadows: <requested / useful supported diagnostics only>
Research: Playing XI and toss availability; format/venue/pitch; phase/wicket/run evidence; weather/resources; L5/L10/L15/L20 within format.
CONTINUE_IF_LATE: YES
GitHub main: READ ONLY; settlement/import: NOT_PERFORMED
```

Any nonempty number of supplied contracts is valid. Remove unused placeholders; do not treat them as propositions or populate them with invented examples.

### 1. Read and establish authority

Complete 0.2 from one verified full published SHA. Read the applicable sport/competition rules, SOURCES routes, league/tour profiles, archive guide/defect notes and base-rate register as well as the full active mini and relevant canonical records. Locate actual filenames/sections; do not invent a sport rules file or use an outdated league constant without disclosure. Print the reading receipt, actual versions, authority differences, permitted writes and unavailable dependencies.

Current controls govern over historical engine notes. If authority/custody inputs needed for issuance are inaccessible, complete the research as `READ_ONLY_DRAFT / NOT_ISSUED`.

### 2. Identity, duplicate and timing gate

Verify teams, competition/tournament, format (Test, ODI, T20, The Hundred), match number, venue, pitch conditions, scheduled start, weather forecast, reserve days, venue zone, UTC and Australia/Sydney time.

Apply SF10/SF11: search all relevant local mini/carryover and canonical bodies/status by native ID, event key and aliases. Doubleheaders, resumed events and postponements need explicit identity handling. A duplicate receives an addendum under its existing ID. Log authorised intake whatever the research outcome; otherwise include a draft intake row.

Verify the named mini, format, writer/lease, freeze status, current canonical allocation and outstanding local sequence. Do not reserve, skip, collide, renumber or consume a canonical ID. Keep analysis cutoff, research completion, actual issue and state recheck separate. Complete the two-step lineup/repricing target when timing permits; research comprehensively if late. Recheck actual state immediately before issue. Outcome exposure prevents prospective pregame credit, even with a reconstructed earlier cutoff.

### 3. Evidence, XI and archive

Follow official board/ICC match center → ESPNcricinfo/structured provider → quality corroboration routes. For each decisive claim retain URL, exact field/value or brief extract, source publication/update time when known, retrieval time and provenance/lineage. Log inaccessible/stale/conflicting sources. Three domains are not three independent collectors. No odds/tips/previews/fantasy inputs.

Confirm playing XI, toss result, batting order, bowling allocations/quotas, pitch report, weather/dew and rain resources; probable is not confirmed. Distinguish fact, historical estimate and analyst assumption. Inspect actual archive contents under `Previous Sports Results/Cricket/...` and print files, logical rows read, format/tournament filters, latest usable date and missingness. Use only results known before cutoff. Do not use postgame narrative or full-season aggregates from after cutoff.

#### Mandatory historical-form implementation for this sport (FR1–FR6)

For both teams use last 5/10/15/20 eligible matches **within the same format** (T20/ODI/Test/The Hundred separated): batting runs per innings/over, wickets, powerplay/middle/death phases, chase/defend results and bowler workloads where sourced. In multi-day cricket, do not reduce innings/draws to T20-type totals; toss/XI/venue conditions stay scenario branches if unknown. Verify announced XI and substitutes/impact-player rules if relevant. Follow the GLOBAL RULE above for both participants; place the required four-window tables, event-level trace, missingness, non-overlap trend, opponent adjustments and official lineup gate in A3; propagate supported numbers to A4 and disclose window-choice sensitivity in A7/A9. Never treat these historical summaries as a fitted/calibrated model.

### 4. Distribution, expected score and comparator

Build the simplest defensible coherent cricket distribution: model innings/phase/wicket dependence with explicit toss and rain branches. Account for chase dynamics: a chase ends on the winning delivery and can legally overshoot the target; do not simply cap every total at the target. Print every parameter and its basis, formula/table, normalization, tail treatment, covariance and endpoint transitions. If the required calculation cannot be done, report a supported approximation with limitations, or qualitative research with NOT_ESTIMATED probabilities.

Produce expected score terms from CARD_AND_LOG_TEMPLATES §3a: format/innings-specific runs and wickets where supported (common cross-team margin is often N/A in chases). Keep zeros; mark missing or irrelevant terms. Print all winner/draw/tie masses. For **every distinct user-supplied contract** retain unconditional W/P/L/V and p_card=W/(W+L), with denominator and action convention; all other priced candidates are separate NOT_PRIMARY shadows.

Attempt BASELINE_LEAGUE_V1 on **each supported supplied contract's exact same line and endpoint** from independent league-only inputs, frozen before issue. Print recipe, source cohort/n/cutoff and parameters separately from the team model. No 0.5 placeholder or retrospective baseline fill. Missing baseline does not stop the card; it limits later skill measurement.

If inputs are unfitted/stale/early-season/unconfirmed, price the **declared low/base/high mixture** (default 0.25/0.50/0.25, frozen before ranking) and show `p_base` and p_card for every supplied line. Show an adjustment table (pitch, weather/rain, toss, XI selection), unadjusted distribution/pair and low/base/high sensitivity on material uncertain inputs. Any adjustment-driven pair change is ADJUSTMENT_DEPENDENT, even below 0.25 SD. Report plausible probability ranges as sensitivity, not confidence intervals. Do not move individual probabilities outside the shared model.

**Cricket implementation safeguards.** Fix format, innings, phase and balls/overs units. Overs notation such as 17.3 means 17 overs and 3 balls under a six-ball-over format, not 17.3 decimal overs; The Hundred uses its own ball/set definitions. Define legal deliveries, extras, wickets and whether a phase exists. Run/wicket/phase totals share innings and stopping constraints. Unknown toss requires supported bat-first/chase branches frozen before pricing. Rain scenarios require supported resource assumptions and current playing conditions; do not claim an exact DLS target without the needed calculation/resources. Chase truncation must allow legal winning-delivery overshoot. Test/multi-day results require draw/time/weather and innings structure; an unsupported match-winner model does not price exact innings totals. Retirements, declarations, forfeits and no-results need explicit field/action conventions.

**Required execution for this section:** apply Q1–Q4, SF3 and FR4/FR5. Mix unconditional masses before conditioning; print p_base separately. Preserve action/definition/known-at limits, score moments, exact supplied-line baseline coverage, numerical error, adjustment table, unadjusted pair and scenario/window rank changes. An absent supported field or calculation stays missing.

### 5. Supplied ranking, eligibility, gates and dependence

Freeze the literal deduplicated user-supplied universe and definitions before modelling. Price all supported supplied keys from the actual compatible distributions; keep every unresolved/unpriced/excluded row visible. Follow SF4 for the complete probability-sorted `SUPPLIED_CONTRACT_RANKING`, 90% selection ceiling, known-at/definition support and any would-be-Rank-1-only family filtering. Select 0–4 actual numeric supplied rows; only Ranks 1–2 are primary picks. The general 0.62/0.04 gate and Rank-2 0.58 floor are transparent diagnostics; specific mandatory family prerequisites remain eligibility tests. Never pad or substitute a derived contract.

Show `SUPPLIED_SCOPE_GATE`, competitor key/p/gap, precision error, floor/family status and the best supported non-complementary supplied alternative. Show line difficulty in units and z where SD is supported. Compute exact joint losing-state mass, valid Fr?chet bounds or an explicit unavailable result under SF7; show both-decisive conditioning only with a genuine joint denominator. Flag complements and mechanical protection. Do not reorder primary picks to hide dependence or call protected Hit@2 predictive skill.

Optional derived ladders and published-policy comparators have separately predeclared universes. Freeze supported RET03/RET04/XCARD6, rank-delta and base-only shadows with their correct names and scopes, or state why not computed. All are NOT_PRIMARY and cannot change the original supplied slate, ID or grade. Retain every supplied row as a candidate research record with its separate future training eligibility.

### 6. Playing conditions and frozen action rules

Verify format/overs or ball limits, phase definitions, bowler allocations, substitutes/impact-player conditions, reserve days, reduced-match/DLS resources, tie/super-over/no-result and multi-day draw conventions. Distinguish an announced toss from an assumption. Freeze whether a proposition includes super-over runs or an innings/phase that may not occur. Use the applicable season/tournament playing conditions, not a sport-wide default.

### 7. Write, audit and return

Use the mini's own applicable CARD_AND_LOG_TEMPLATES format; retain the near-650-word decision target where prescribed and full A1–A9 evidence. Record literal/normalised contracts, common-distribution calculations, baseline coverage, full supplied ranking, formal picks, all missingness, source receipts and original model/scenario/recipe versions. Freeze the exact later settlement fields, action definitions and capture plan without performing settlement.

Apply SF11's pre-write concurrency/lease/freeze/ID checks and original-block custody. Append one complete card before the footer for a genuinely new event, or one dated addendum for an existing event; update only authorised intake/footer totals. Preserve all earlier issued bytes. Read back the actual write, reconcile keys/counts/probabilities/timestamps/footer and verify prior blocks. A draft or failed verification cannot claim a successful append/ID advance.

In A9 complete the mini's actual checklist (C1–C20 for reference mini-log-7, or the original legacy checklist plus dated compatibility gaps), FR1–FR6, SF-A1–SF-A12 and Q4 calculation checks with specific evidence/status. Return the full new card/addendum or complete non-issued draft, exact path, working ID/status, timing/exposure, all supplied probabilities, supplied-only formal picks or precise no-pick reason, gate/joint/sensitivity/baseline results and updated footer/readback receipt. Explicitly state settlement NOT_PERFORMED, canonical import NOT_PERFORMED, GitHub writes NO and new canonical IDs 0. Make no success guarantee.

---

## BASEBALL

### Event input — fill before executing this sport's seven steps

```text
Upcoming Baseball Game: <participants; exact competition; season/stage/format; date/time/timezone>
Native event ID / game number / official URL: <if supplied; otherwise verify>
Venue / home-away orientation: <if supplied; otherwise verify>
Active mini: <exact existing authorised local path, or identify from accessible files>
Supplied contracts (one literal proposition per line):
1. <exact user text>
2. <exact user text; optional>
3. <additional exact user text; optional>
Contract period / endpoint / action terms: <explicit supplied terms; resolve missing material definitions>
Requested primary ranking: SUPPLIED CONTRACTS ONLY
Optional derived shadows: <requested / useful supported diagnostics only>
Research: Starting pitchers/workloads; batting order; bullpen availability; park/weather; L5/L10/L15/L20; innings/extras/tie endpoint.
CONTINUE_IF_LATE: YES
GitHub main: READ ONLY; settlement/import: NOT_PERFORMED
```

Any nonempty number of supplied contracts is valid. Remove unused placeholders; do not treat them as propositions or populate them with invented examples.

### 1. Read and establish authority

Complete 0.2 from one verified full published SHA. Read the applicable sport/competition rules, SOURCES routes, league/tour profiles, archive guide/defect notes and base-rate register as well as the full active mini and relevant canonical records. Locate actual filenames/sections; do not invent a sport rules file or use an outdated league constant without disclosure. Print the reading receipt, actual versions, authority differences, permitted writes and unavailable dependencies.

Current controls govern over historical engine notes. If authority/custody inputs needed for issuance are inaccessible, complete the research as `READ_ONLY_DRAFT / NOT_ISSUED`.

### 2. Identity, duplicate and timing gate

Verify participants, league/competition, season, game number (single game vs doubleheader G1/G2), venue, native ID, official scheduled first pitch, venue zone, UTC and Australia/Sydney time.

Apply SF10/SF11: search all relevant local mini/carryover and canonical bodies/status by native ID, event key and aliases. Doubleheaders, resumed events and postponements need explicit identity handling. A duplicate receives an addendum under its existing ID. Log authorised intake whatever the research outcome; otherwise include a draft intake row.

Verify the named mini, format, writer/lease, freeze status, current canonical allocation and outstanding local sequence. Do not reserve, skip, collide, renumber or consume a canonical ID. Keep analysis cutoff, research completion, actual issue and state recheck separate. Complete the two-step lineup/repricing target when timing permits; research comprehensively if late. Recheck actual state immediately before issue. Outcome exposure prevents prospective pregame credit, even with a reconstructed earlier cutoff.

### 3. Evidence, starters and archive

Follow official league scoreboard (MLB Gameday, KBO, NPB official, etc.) → structured provider (MyKBO, etc.) → quality corroboration routes. For each decisive claim retain URL, exact field/value or brief extract, source publication/update time when known, retrieval time and provenance/lineage. Log inaccessible/stale/conflicting sources. Three domains are not three independent collectors. No odds/tips/previews/fantasy inputs.

Verify starting pitcher identity and expected workload, confirmed batting lineup/platoon, bullpen availability, park factors, weather and rest; probable is not confirmed. Unknown pitcher weights stay assumptions, not facts. Inspect actual archive contents under `Previous Sports Results/Baseball/<league>/...` and print files, logical rows read, season/endpoint filters, latest usable date and missingness. Use only results known before cutoff. Do not use postgame narrative or full-season aggregates from after cutoff.

#### Mandatory historical-form implementation for this sport (FR1–FR6)

For both teams use last 5/10/15/20 verified games: runs scored/allowed, starter/bullpen segments if sourced, park-adjusted production, team-specific one-run results, home/road splits and extras with measured status (KBO/NPB placeholder columns are NOT measured). Also show separately the named probable/confirmed starting pitcher’s last 5/10/15/20 **starts where eligible**, with available n and inning/pitch/workload records; do not treat pitcher and team windows as independent. Follow the GLOBAL RULE above for both participants; place the required four-window tables, event-level trace, missingness, non-overlap trend, opponent adjustments and official lineup gate in A3; propagate supported numbers to A4 and disclose window-choice sensitivity in A7/A9. Never treat these historical summaries as a fitted/calibrated model.

### 4. Distribution, expected score and comparator

Build the simplest defensible coherent baseball distribution: use supported overdispersed team-run scenarios with shared environment, starter/bullpen segments and correct home last-inning/extras handling. Print every parameter and its basis, formula/table, normalization, tail treatment, covariance and endpoint transitions. If the required calculation cannot be done, report a supported approximation with limitations, or qualitative research with NOT_ESTIMATED probabilities.

Produce expected score terms from CARD_AND_LOG_TEMPLATES §3a: team runs (means & SDs), total runs (mean & SD), signed margin (mean & SD) over exact innings/extras endpoint. +1.5 needs team-directional win and exactly-one-run-loss mass, with tie/action treatment. Keep zeros; mark missing or irrelevant terms. Print all winner/draw/tie masses. For **every distinct user-supplied contract** retain unconditional W/P/L/V and p_card=W/(W+L), with denominator and action convention; all other priced candidates are separate NOT_PRIMARY shadows.

Attempt BASELINE_LEAGUE_V1 on **each supported supplied contract's exact same line and endpoint** from independent league-only inputs, frozen before issue. Print recipe, source cohort/n/cutoff and parameters separately from the team model. No 0.5 placeholder or retrospective baseline fill. Missing baseline does not stop the card; it limits later skill measurement.

If inputs are unfitted/stale/early-season/unconfirmed, price the **declared low/base/high mixture** (default 0.25/0.50/0.25, frozen before ranking) and show `p_base` and p_card for every supplied line. Show an adjustment table (starting pitcher, bullpen, park, weather), unadjusted distribution/pair and low/base/high sensitivity on material uncertain inputs. Any adjustment-driven pair change is ADJUSTMENT_DEPENDENT, even below 0.25 SD. Report plausible probability ranges as sensitivity, not confidence intervals. Do not move individual probabilities outside the shared model.

**Baseball implementation safeguards.** Confirm game number, starter and pitcher-change policy. Model directional team runs under a compatible shared environment; estimate dispersion only from actual fields or disclose its assumption. Home last-inning/walk-off stopping changes totals and margin tails; do not equate two independent complete-innings counts with an exact game simulator. Treat named starter contributions, bullpen workload and lineup shifts once. Separate first-five/shortened/regulation/final-extras fields. For the selected team, +1.5 coverage comes from its win, tie where applicable under the contract, and exactly-one-run-loss states; it is not the league's absolute one-run frequency. Freeze extra-inning runner/tie/innings-limit rules for the actual season and stage.

**Required execution for this section:** apply Q1–Q4, SF3 and FR4/FR5. Mix unconditional masses before conditioning; print p_base separately. Preserve action/definition/known-at limits, score moments, exact supplied-line baseline coverage, numerical error, adjustment table, unadjusted pair and scenario/window rank changes. An absent supported field or calculation stays missing.

### 5. Supplied ranking, eligibility, gates and dependence

Freeze the literal deduplicated user-supplied universe and definitions before modelling. Price all supported supplied keys from the actual compatible distributions; keep every unresolved/unpriced/excluded row visible. Follow SF4 for the complete probability-sorted `SUPPLIED_CONTRACT_RANKING`, 90% selection ceiling, known-at/definition support and any would-be-Rank-1-only family filtering. Select 0–4 actual numeric supplied rows; only Ranks 1–2 are primary picks. The general 0.62/0.04 gate and Rank-2 0.58 floor are transparent diagnostics; specific mandatory family prerequisites remain eligibility tests. Never pad or substitute a derived contract.

Show `SUPPLIED_SCOPE_GATE`, competitor key/p/gap, precision error, floor/family status and the best supported non-complementary supplied alternative. Show line difficulty in units and z where SD is supported. Compute exact joint losing-state mass, valid Fr?chet bounds or an explicit unavailable result under SF7; show both-decisive conditioning only with a genuine joint denominator. Flag complements and mechanical protection. Do not reorder primary picks to hide dependence or call protected Hit@2 predictive skill.

Optional derived ladders and published-policy comparators have separately predeclared universes. Freeze supported RET03/RET04/XCARD6, rank-delta and base-only shadows with their correct names and scopes, or state why not computed. All are NOT_PRIMARY and cannot change the original supplied slate, ID or grade. Retain every supplied row as a candidate research record with its separate future training eligibility.

### 6. Playing conditions and frozen action rules

Verify scheduled innings, doubleheader/shortened-game rules, extra-inning runner rules, innings limits/ties, mercy rules, suspended/resumed-game treatment and cancellation action. Do not hard-code a KBO/NPB innings cap or transfer MLB regular-season extra-inning rules to another league/stage. Freeze full-game versus first-five/regulation endpoint and pitcher-change/participation action terms where relevant.

### 7. Write, audit and return

Use the mini's own applicable CARD_AND_LOG_TEMPLATES format; retain the near-650-word decision target where prescribed and full A1–A9 evidence. Record literal/normalised contracts, common-distribution calculations, baseline coverage, full supplied ranking, formal picks, all missingness, source receipts and original model/scenario/recipe versions. Freeze the exact later settlement fields, action definitions and capture plan without performing settlement.

Apply SF11's pre-write concurrency/lease/freeze/ID checks and original-block custody. Append one complete card before the footer for a genuinely new event, or one dated addendum for an existing event; update only authorised intake/footer totals. Preserve all earlier issued bytes. Read back the actual write, reconcile keys/counts/probabilities/timestamps/footer and verify prior blocks. A draft or failed verification cannot claim a successful append/ID advance.

In A9 complete the mini's actual checklist (C1–C20 for reference mini-log-7, or the original legacy checklist plus dated compatibility gaps), FR1–FR6, SF-A1–SF-A12 and Q4 calculation checks with specific evidence/status. Return the full new card/addendum or complete non-issued draft, exact path, working ID/status, timing/exposure, all supplied probabilities, supplied-only formal picks or precise no-pick reason, gate/joint/sensitivity/baseline results and updated footer/readback receipt. Explicitly state settlement NOT_PERFORMED, canonical import NOT_PERFORMED, GitHub writes NO and new canonical IDs 0. Make no success guarantee.

---

## SOCCER

### Event input — fill before executing this sport's seven steps

```text
Upcoming Soccer Match: <participants; exact competition; season/stage/format; date/time/timezone>
Native event ID / game number / official URL: <if supplied; otherwise verify>
Venue / home-away orientation: <if supplied; otherwise verify>
Active mini: <exact existing authorised local path, or identify from accessible files>
Supplied contracts (one literal proposition per line):
1. <exact user text>
2. <exact user text; optional>
3. <additional exact user text; optional>
Contract period / endpoint / action terms: <explicit supplied terms; resolve missing material definitions>
Requested primary ranking: SUPPLIED CONTRACTS ONLY
Optional derived shadows: <requested / useful supported diagnostics only>
Research: Starting XI/keeper/substitutes; goals/xG where measured; period/corner-specific fields; L5/L10/L15/L20; regulation/qualification endpoint.
CONTINUE_IF_LATE: YES
GitHub main: READ ONLY; settlement/import: NOT_PERFORMED
```

Any nonempty number of supplied contracts is valid. Remove unused placeholders; do not treat them as propositions or populate them with invented examples.

### 1. Read and establish authority

Complete 0.2 from one verified full published SHA. Read the applicable sport/competition rules, SOURCES routes, league/tour profiles, archive guide/defect notes and base-rate register as well as the full active mini and relevant canonical records. Locate actual filenames/sections; do not invent a sport rules file or use an outdated league constant without disclosure. Print the reading receipt, actual versions, authority differences, permitted writes and unavailable dependencies.

Current controls govern over historical engine notes. If authority/custody inputs needed for issuance are inaccessible, complete the research as `READ_ONLY_DRAFT / NOT_ISSUED`.

### 2. Identity, duplicate and timing gate

Verify clubs/national teams, competition, stage, venue, native ID, official scheduled kickoff, venue zone, UTC and Australia/Sydney time.

Apply SF10/SF11: search all relevant local mini/carryover and canonical bodies/status by native ID, event key and aliases. Doubleheaders, resumed events and postponements need explicit identity handling. A duplicate receives an addendum under its existing ID. Log authorised intake whatever the research outcome; otherwise include a draft intake row.

Verify the named mini, format, writer/lease, freeze status, current canonical allocation and outstanding local sequence. Do not reserve, skip, collide, renumber or consume a canonical ID. Keep analysis cutoff, research completion, actual issue and state recheck separate. Complete the two-step lineup/repricing target when timing permits; research comprehensively if late. Recheck actual state immediately before issue. Outcome exposure prevents prospective pregame credit, even with a reconstructed earlier cutoff.

### 3. Evidence, XI and archive

Follow official field-owner / federation match center → structured provider (FBref, official club reporting, etc.) → quality corroboration routes. For each decisive claim retain URL, exact field/value or brief extract, source publication/update time when known, retrieval time and provenance/lineage. Log inaccessible/stale/conflicting sources. Three domains are not three independent collectors. No odds/tips/previews/fantasy inputs.

Confirm starting XI, goalkeeper, bench/rotation, injuries, schedule congestion; probable is not confirmed. Inspect actual archive contents under `Previous Sports Results/Soccer/<league>/...` and print files, logical rows read, season/endpoint filters, latest usable date and missingness. Use only results known before cutoff. Do not use postgame narrative or full-season aggregates from after cutoff.

#### Mandatory historical-form implementation for this sport (FR1–FR6)

For both sides use last 5/10/15/20 comparable regulation matches: goals for/against, expected goals/xGA **only where actual trusted xG data exist**, shots, first-half goals, clean sheets, BTTS, venue split, opponent quality, rest. Build first-half and corners-specific windows **only when these exact fields were captured**, and report their separate coverage; total goals cannot substitute for corners or first-half measurements. Confirm starting XI, substitutes and keepers. Follow the GLOBAL RULE above for both participants; place the required four-window tables, event-level trace, missingness, non-overlap trend, opponent adjustments and official lineup gate in A3; propagate supported numbers to A4 and disclose window-choice sensitivity in A7/A9. Never treat these historical summaries as a fitted/calibrated model.

### 4. Distribution, expected score and comparator

Build the simplest defensible coherent soccer distribution: use a coherent regulation score model with explicit draw, opponent-adjusted xG/shot process, supported half split for phase rows, and a low-score correction only where its parameters are supported or a clearly disclosed authorised scenario is used. Separate provider-backed corner count models (corners need their own supported count/provider model and joint dependence; goal counts never generate corner probabilities). Print every parameter and its basis, formula/table, normalization, tail treatment, covariance and endpoint transitions. If the required calculation cannot be done, report a supported approximation with limitations, or qualitative research with NOT_ESTIMATED probabilities.

Produce expected score terms from CARD_AND_LOG_TEMPLATES §3a: regulation goals per team/total/margin, supported half goals, and separate provider-backed corner counts. Keep zeros; mark missing or irrelevant terms. Print all winner/draw/tie masses. For **every distinct user-supplied contract** retain unconditional W/P/L/V and p_card=W/(W+L), with denominator and action convention; all other priced candidates are separate NOT_PRIMARY shadows.

Attempt BASELINE_LEAGUE_V1 on **each supported supplied contract's exact same line and endpoint** from independent league-only inputs, frozen before issue. Print recipe, source cohort/n/cutoff and parameters separately from the team model. No 0.5 placeholder or retrospective baseline fill. Missing baseline does not stop the card; it limits later skill measurement.

If inputs are unfitted/stale/early-season/unconfirmed, price the **declared low/base/high mixture** (default 0.25/0.50/0.25, frozen before ranking) and show `p_base` and p_card for every supplied line. Show an adjustment table (home venue, rotation/XI, rest, weather), unadjusted distribution/pair and low/base/high sensitivity on material uncertain inputs. Any adjustment-driven pair change is ADJUSTMENT_DEPENDENT, even below 0.25 SD. Report plausible probability ranges as sensitivity, not confidence intervals. Do not move individual probabilities outside the shared model.

**Soccer implementation safeguards.** Distinguish regulation result, extra-time result and qualification; model each supplied endpoint separately or through justified transitions. Full-time and half-time goals must be compatible, but half rates need measured half data; do not assume a universal half-of-full-time split. A low-score correction is applied only with supported parameters or a disclosed authorised scenario, never invented as a measured fit. Corners require provider definition, own count mean/dispersion and field coverage; do not invent a negative-binomial dispersion or an exact goals/corners joint. Goalkeeper/XI and red-card assumptions must be dated and not outcome-aware. Freeze BTTS, team-to-score, handicap and stoppage conventions; quarter Asian lines follow SF3's action-structure safeguard.

**Required execution for this section:** apply Q1–Q4, SF3 and FR4/FR5. Mix unconditional masses before conditioning; print p_base separately. Preserve action/definition/known-at limits, score moments, exact supplied-line baseline coverage, numerical error, adjustment table, unadjusted pair and scenario/window rank changes. An absent supported field or calculation stays missing.

### 5. Supplied ranking, eligibility, gates and dependence

Freeze the literal deduplicated user-supplied universe and definitions before modelling. Price all supported supplied keys from the actual compatible distributions; keep every unresolved/unpriced/excluded row visible. Follow SF4 for the complete probability-sorted `SUPPLIED_CONTRACT_RANKING`, 90% selection ceiling, known-at/definition support and any would-be-Rank-1-only family filtering. Select 0–4 actual numeric supplied rows; only Ranks 1–2 are primary picks. The general 0.62/0.04 gate and Rank-2 0.58 floor are transparent diagnostics; specific mandatory family prerequisites remain eligibility tests. Never pad or substitute a derived contract.

Show `SUPPLIED_SCOPE_GATE`, competitor key/p/gap, precision error, floor/family status and the best supported non-complementary supplied alternative. Show line difficulty in units and z where SD is supported. Compute exact joint losing-state mass, valid Fr?chet bounds or an explicit unavailable result under SF7; show both-decisive conditioning only with a genuine joint denominator. Flag complements and mechanical protection. Do not reorder primary picks to hide dependence or call protected Hit@2 predictive skill.

Optional derived ladders and published-policy comparators have separately predeclared universes. Freeze supported RET03/RET04/XCARD6, rank-delta and base-only shadows with their correct names and scopes, or state why not computed. All are NOT_PRIMARY and cannot change the original supplied slate, ID or grade. Retain every supplied row as a candidate research record with its separate future training eligibility.

### 6. Playing conditions and frozen action rules

Verify regulation duration plus stoppage, period boundary conventions, extra-time and penalty-shootout treatment, and whether winner means regulation winner or qualification. Confirm aggregate/two-leg context and applicable competition-season tie rules. Do not include shootout kicks as match goals or infer period/corner/player action from a full-time result.

### 7. Write, audit and return

Use the mini's own applicable CARD_AND_LOG_TEMPLATES format; retain the near-650-word decision target where prescribed and full A1–A9 evidence. Record literal/normalised contracts, common-distribution calculations, baseline coverage, full supplied ranking, formal picks, all missingness, source receipts and original model/scenario/recipe versions. Freeze the exact later settlement fields, action definitions and capture plan without performing settlement.

Apply SF11's pre-write concurrency/lease/freeze/ID checks and original-block custody. Append one complete card before the footer for a genuinely new event, or one dated addendum for an existing event; update only authorised intake/footer totals. Preserve all earlier issued bytes. Read back the actual write, reconcile keys/counts/probabilities/timestamps/footer and verify prior blocks. A draft or failed verification cannot claim a successful append/ID advance.

In A9 complete the mini's actual checklist (C1–C20 for reference mini-log-7, or the original legacy checklist plus dated compatibility gaps), FR1–FR6, SF-A1–SF-A12 and Q4 calculation checks with specific evidence/status. Return the full new card/addendum or complete non-issued draft, exact path, working ID/status, timing/exposure, all supplied probabilities, supplied-only formal picks or precise no-pick reason, gate/joint/sensitivity/baseline results and updated footer/readback receipt. Explicitly state settlement NOT_PERFORMED, canonical import NOT_PERFORMED, GitHub writes NO and new canonical IDs 0. Make no success guarantee.

---

## ICE HOCKEY

### Event input — fill before executing this sport's seven steps

```text
Upcoming Ice Hockey Game: <participants; exact competition; season/stage/format; date/time/timezone>
Native event ID / game number / official URL: <if supplied; otherwise verify>
Venue / home-away orientation: <if supplied; otherwise verify>
Active mini: <exact existing authorised local path, or identify from accessible files>
Supplied contracts (one literal proposition per line):
1. <exact user text>
2. <exact user text; optional>
3. <additional exact user text; optional>
Contract period / endpoint / action terms: <explicit supplied terms; resolve missing material definitions>
Requested primary ranking: SUPPLIED CONTRACTS ONLY
Optional derived shadows: <requested / useful supported diagnostics only>
Research: Starting goalie; lines/scratches; 5v5/special teams; shots/quality where measured; L5/L10/L15/L20; regulation/OT/shootout endpoint.
CONTINUE_IF_LATE: YES
GitHub main: READ ONLY; settlement/import: NOT_PERFORMED
```

Any nonempty number of supplied contracts is valid. Remove unused placeholders; do not treat them as propositions or populate them with invented examples.

### 1. Read and establish authority

Complete 0.2 from one verified full published SHA. Read the applicable sport/competition rules, SOURCES routes, league/tour profiles, archive guide/defect notes and base-rate register as well as the full active mini and relevant canonical records. Locate actual filenames/sections; do not invent a sport rules file or use an outdated league constant without disclosure. Print the reading receipt, actual versions, authority differences, permitted writes and unavailable dependencies.

Current controls govern over historical engine notes. If authority/custody inputs needed for issuance are inaccessible, complete the research as `READ_ONLY_DRAFT / NOT_ISSUED`.

### 2. Identity, duplicate and timing gate

Verify teams, league (NHL, Tipsport Extraliga, Liiga, SHL, etc.), season, venue, native ID, official scheduled puck drop, venue zone, UTC and Australia/Sydney time.

Apply SF10/SF11: search all relevant local mini/carryover and canonical bodies/status by native ID, event key and aliases. Doubleheaders, resumed events and postponements need explicit identity handling. A duplicate receives an addendum under its existing ID. Log authorised intake whatever the research outcome; otherwise include a draft intake row.

Verify the named mini, format, writer/lease, freeze status, current canonical allocation and outstanding local sequence. Do not reserve, skip, collide, renumber or consume a canonical ID. Keep analysis cutoff, research completion, actual issue and state recheck separate. Complete the two-step lineup/repricing target when timing permits; research comprehensively if late. Recheck actual state immediately before issue. Outcome exposure prevents prospective pregame credit, even with a reconstructed earlier cutoff.

### 3. Evidence, goalies and archive

Follow official league game sheet / match reports → structured provider → quality corroboration routes. For each decisive claim retain URL, exact field/value or brief extract, source publication/update time when known, retrieval time and provenance/lineage. Log inaccessible/stale/conflicting sources. Three domains are not three independent collectors. No odds/tips/previews/fantasy inputs.

Confirm starting goalies or supported mixture, lines/scratches, special teams, rest and travel; probable is not confirmed. Unconfirmed goalie sensitivity must reach totals/ranks. Inspect actual archive contents under `Previous Sports Results/Ice Hockey/<league>/...` and print files, logical rows read, season/endpoint filters, latest usable date and missingness. Use only results known before cutoff. Do not use postgame narrative or full-season aggregates from after cutoff.

#### Mandatory historical-form implementation for this sport (FR1–FR6)

For both teams last 5/10/15/20: regulation goals for/against, shots/xG/high-danger chances where supported, 5v5 strength, power-play/penalty-kill rate with denominators, goalie-specific start histories, venue/rest; separate full-game SO credit from actual goals. Also show starting goalies’ last 5/10/15/20 eligible starts where supported, and backup/wear sensitivity. A probable goalie is not a confirmed starter. Follow the GLOBAL RULE above for both participants; place the required four-window tables, event-level trace, missingness, non-overlap trend, opponent adjustments and official lineup gate in A3; propagate supported numbers to A4 and disclose window-choice sensitivity in A7/A9. Never treat these historical summaries as a fitted/calibrated model.

### 4. Distribution, expected score and comparator

Build the simplest defensible coherent ice hockey distribution: 5v5 creation/suppression, special teams, rest/travel, and explicit empty-net tails. Separate regulation draw from full-game OT/SO and final-score convention. Print directional handicap mass, not unconditional league absolute-margin frequency. Print every parameter and its basis, formula/table, normalization, tail treatment, covariance and endpoint transitions. If the required calculation cannot be done, report a supported approximation with limitations, or qualitative research with NOT_ESTIMATED probabilities.

Produce expected score terms from CARD_AND_LOG_TEMPLATES §3a: regulation and/or full-game goals with OT/SO accounting, total, signed margin and supported SDs. Keep zeros; mark missing or irrelevant terms. Print all winner/draw/tie masses. For **every distinct user-supplied contract** retain unconditional W/P/L/V and p_card=W/(W+L), with denominator and action convention; all other priced candidates are separate NOT_PRIMARY shadows.

Attempt BASELINE_LEAGUE_V1 on **each supported supplied contract's exact same line and endpoint** from independent league-only inputs, frozen before issue. Print recipe, source cohort/n/cutoff and parameters separately from the team model. No 0.5 placeholder or retrospective baseline fill. Missing baseline does not stop the card; it limits later skill measurement.

If inputs are unfitted/stale/early-season/unconfirmed, price the **declared low/base/high mixture** (default 0.25/0.50/0.25, frozen before ranking) and show `p_base` and p_card for every supplied line. Show an adjustment table (goalie mixture, special teams, rest/travel), unadjusted distribution/pair and low/base/high sensitivity on material uncertain inputs. Any adjustment-driven pair change is ADJUSTMENT_DEPENDENT, even below 0.25 SD. Report plausible probability ranges as sensitivity, not confidence intervals. Do not move individual probabilities outside the shared model.

**Hockey implementation safeguards.** Separate regulation goals, overtime goals, shootout result and the official credited final-score convention. A shootout decision is not an observed scored regulation goal. Price each supplied row on its frozen endpoint; two-way winner and three-way regulation result have different state mappings. Starting-goalie alternatives must propagate through goal distributions/totals/handicaps, with supported uncertainty rather than assumed official confirmation. Empty-net tails need score/time-state support or a labelled approximation. Power-play/penalty-kill evidence needs opportunity denominators and comparable era/competition. Do not add a goalie adjustment twice through both historical team prevention and a separate specialist term.

**Required execution for this section:** apply Q1–Q4, SF3 and FR4/FR5. Mix unconditional masses before conditioning; print p_base separately. Preserve action/definition/known-at limits, score moments, exact supplied-line baseline coverage, numerical error, adjustment table, unadjusted pair and scenario/window rank changes. An absent supported field or calculation stays missing.

### 5. Supplied ranking, eligibility, gates and dependence

Freeze the literal deduplicated user-supplied universe and definitions before modelling. Price all supported supplied keys from the actual compatible distributions; keep every unresolved/unpriced/excluded row visible. Follow SF4 for the complete probability-sorted `SUPPLIED_CONTRACT_RANKING`, 90% selection ceiling, known-at/definition support and any would-be-Rank-1-only family filtering. Select 0–4 actual numeric supplied rows; only Ranks 1–2 are primary picks. The general 0.62/0.04 gate and Rank-2 0.58 floor are transparent diagnostics; specific mandatory family prerequisites remain eligibility tests. Never pad or substitute a derived contract.

Show `SUPPLIED_SCOPE_GATE`, competitor key/p/gap, precision error, floor/family status and the best supported non-complementary supplied alternative. Show line difficulty in units and z where SD is supported. Compute exact joint losing-state mass, valid Fr?chet bounds or an explicit unavailable result under SF7; show both-decisive conditioning only with a genuine joint denominator. Flag complements and mechanical protection. Do not reorder primary picks to hide dependence or call protected Hit@2 predictive skill.

Optional derived ladders and published-policy comparators have separately predeclared universes. Freeze supported RET03/RET04/XCARD6, rank-delta and base-only shadows with their correct names and scopes, or state why not computed. All are NOT_PRIMARY and cannot change the original supplied slate, ID or grade. Retain every supplied row as a candidate research record with its separate future training eligibility.

### 6. Playing conditions and frozen action rules

Verify regulation length, overtime format/duration/repetition, shootout rules and playoff versus regular-season treatment for the exact league/season. Freeze regulation-only versus OT/SO inclusion and official shootout-score credit by contract family. Empty-net goals are actual game goals; shootout decisions have their own accounting. Do not transplant NHL defaults to other leagues.

### 7. Write, audit and return

Use the mini's own applicable CARD_AND_LOG_TEMPLATES format; retain the near-650-word decision target where prescribed and full A1–A9 evidence. Record literal/normalised contracts, common-distribution calculations, baseline coverage, full supplied ranking, formal picks, all missingness, source receipts and original model/scenario/recipe versions. Freeze the exact later settlement fields, action definitions and capture plan without performing settlement.

Apply SF11's pre-write concurrency/lease/freeze/ID checks and original-block custody. Append one complete card before the footer for a genuinely new event, or one dated addendum for an existing event; update only authorised intake/footer totals. Preserve all earlier issued bytes. Read back the actual write, reconcile keys/counts/probabilities/timestamps/footer and verify prior blocks. A draft or failed verification cannot claim a successful append/ID advance.

In A9 complete the mini's actual checklist (C1–C20 for reference mini-log-7, or the original legacy checklist plus dated compatibility gaps), FR1–FR6, SF-A1–SF-A12 and Q4 calculation checks with specific evidence/status. Return the full new card/addendum or complete non-issued draft, exact path, working ID/status, timing/exposure, all supplied probabilities, supplied-only formal picks or precise no-pick reason, gate/joint/sensitivity/baseline results and updated footer/readback receipt. Explicitly state settlement NOT_PERFORMED, canonical import NOT_PERFORMED, GitHub writes NO and new canonical IDs 0. Make no success guarantee.

---

## TENNIS

### Event input — fill before executing this sport's seven steps

```text
Upcoming Tennis Match: <participants; exact competition; season/stage/format; date/time/timezone>
Native event ID / game number / official URL: <if supplied; otherwise verify>
Venue / home-away orientation: <if supplied; otherwise verify>
Active mini: <exact existing authorised local path, or identify from accessible files>
Supplied contracts (one literal proposition per line):
1. <exact user text>
2. <exact user text; optional>
3. <additional exact user text; optional>
Contract period / endpoint / action terms: <explicit supplied terms; resolve missing material definitions>
Requested primary ranking: SUPPLIED CONTRACTS ONLY
Optional derived shadows: <requested / useful supported diagnostics only>
Research: Participation/fitness; tour/round/surface/format; serve/return; L5/L10/L15/L20; set/tiebreak rules; retirement/walkover convention.
CONTINUE_IF_LATE: YES
GitHub main: READ ONLY; settlement/import: NOT_PERFORMED
```

Any nonempty number of supplied contracts is valid. Remove unused placeholders; do not treat them as propositions or populate them with invented examples.

### 1. Read and establish authority

Complete 0.2 from one verified full published SHA. Read the applicable sport/competition rules, SOURCES routes, league/tour profiles, archive guide/defect notes and base-rate register as well as the full active mini and relevant canonical records. Locate actual filenames/sections; do not invent a sport rules file or use an outdated league constant without disclosure. Print the reading receipt, actual versions, authority differences, permitted writes and unavailable dependencies.

Current controls govern over historical engine notes. If authority/custody inputs needed for issuance are inaccessible, complete the research as `READ_ONLY_DRAFT / NOT_ISSUED`.

### 2. Identity, duplicate and timing gate

Verify players, tournament, tour (ATP, WTA, Challenger), round, court/surface, match order on court, scheduled time, venue zone, UTC and Australia/Sydney time.

Apply SF10/SF11: search all relevant local mini/carryover and canonical bodies/status by native ID, event key and aliases. Doubleheaders, resumed events and postponements need explicit identity handling. A duplicate receives an addendum under its existing ID. Log authorised intake whatever the research outcome; otherwise include a draft intake row.

Verify the named mini, format, writer/lease, freeze status, current canonical allocation and outstanding local sequence. Do not reserve, skip, collide, renumber or consume a canonical ID. Keep analysis cutoff, research completion, actual issue and state recheck separate. Complete the two-step lineup/repricing target when timing permits; research comprehensively if late. Recheck actual state immediately before issue. Outcome exposure prevents prospective pregame credit, even with a reconstructed earlier cutoff.

### 3. Evidence, fitness and archive

Follow official tour match center (ATP / WTA) → structured provider → quality corroboration routes. For each decisive claim retain URL, exact field/value or brief extract, source publication/update time when known, retrieval time and provenance/lineage. Log inaccessible/stale/conflicting sources. Three domains are not three independent collectors. No odds/tips/previews/fantasy inputs.

Verify event/player identity, round, tour, surface, best-of format, tiebreak rules, fitness, workload, serve/return data and appropriate benchmark; probable is not confirmed. Inspect current tennis archive/provider coverage rather than assuming it is empty. Use only results known before cutoff. Do not use postgame narrative or full-season aggregates from after cutoff.

#### Mandatory historical-form implementation for this sport (FR1–FR6)

For each player use last 5/10/15/20 completed matches on the same surface and in the same tour/format where sufficient; if limited, show exact n then a **separate** cross-surface/tour supplementary cohort. Record serve-hold/break/first-serve and return-point statistics only if sourced, sets/games, opponent rank/strength, match workload and retirement/walkover exclusion conventions. No team starting-XI/bench requirement applies to singles; verify player participation/withdrawal state instead. Follow the GLOBAL RULE above for both participants; place the required four-window tables, event-level trace, missingness, non-overlap trend, opponent adjustments and official lineup gate in A3; propagate supported numbers to A4 and disclose window-choice sensitivity in A7/A9. Never treat these historical summaries as a fitted/calibrated model.

### 4. Distribution, expected score and comparator

Build the simplest defensible coherent tennis distribution: games/sets/winner come from compatible point-to-match construction with a supported form mixture; show calculation or label the approximation. Compare deciding-set mass with relevant tour/surface/format data, never force a global reference rate. Print every parameter and its basis, formula/table, normalization, tail treatment, covariance and endpoint transitions. If the required calculation cannot be done, report a supported approximation with limitations, or qualitative research with NOT_ESTIMATED probabilities.

Produce expected score terms from CARD_AND_LOG_TEMPLATES §3a: games per player/total/margin, expected sets and deciding-set probability for exact format. Keep zeros; mark missing or irrelevant terms. Print all winner/draw/tie masses. For **every distinct user-supplied contract** retain unconditional W/P/L/V and p_card=W/(W+L), with denominator and action convention; all other priced candidates are separate NOT_PRIMARY shadows.

Attempt BASELINE_LEAGUE_V1 on **each supported supplied contract's exact same line and endpoint** from independent tour-only inputs, frozen before issue. Print recipe, source cohort/n/cutoff and parameters separately from the player model. No 0.5 placeholder or retrospective baseline fill. Missing baseline does not stop the card; it limits later skill measurement.

If inputs are unfitted/stale/early-season/unconfirmed, price the **declared low/base/high mixture** (default 0.25/0.50/0.25, frozen before ranking) and show `p_base` and p_card for every supplied line. Show an adjustment table (surface, fatigue/workload, form), unadjusted distribution/pair and low/base/high sensitivity on material uncertain inputs. Any adjustment-driven pair change is ADJUSTMENT_DEPENDENT, even below 0.25 SD. Report plausible probability ranges as sensitivity, not confidence intervals. Do not move individual probabilities outside the shared model.

**Tennis implementation safeguards.** A compatible point/game/set/match construction needs serve order, surface-specific serve/return inputs, advantage/no-ad rules, ordinary and deciding tiebreak rules, and the exact match format. If used, a stationary iid point model is a disclosed approximation with match-form variability sensitivity, not calibrated precision. Total games and game handicaps use all terminal set-score states, including match-losing states; covering a game handicap does not imply winning. Set handicaps are a different quantity. A deciding match tiebreak may have a contract-specific game-count convention. Retirement/walkover sporting advancement and action settlement differ; do not infer one from the other. A match-winner-only rating does not by itself price game/set lines. For doubles, model pair identities/serve order and rules; singles data alone cannot justify pair-level probabilities.

**Required execution for this section:** apply Q1–Q4, SF3 and FR4/FR5. Mix unconditional masses before conditioning; print p_base separately. Preserve action/definition/known-at limits, score moments, exact supplied-line baseline coverage, numerical error, adjustment table, unadjusted pair and scenario/window rank changes. An absent supported field or calculation stays missing.

### 5. Supplied ranking, eligibility, gates and dependence

Freeze the literal deduplicated user-supplied universe and definitions before modelling. Price all supported supplied keys from the actual compatible distributions; keep every unresolved/unpriced/excluded row visible. Follow SF4 for the complete probability-sorted `SUPPLIED_CONTRACT_RANKING`, 90% selection ceiling, known-at/definition support and any would-be-Rank-1-only family filtering. Select 0–4 actual numeric supplied rows; only Ranks 1–2 are primary picks. The general 0.62/0.04 gate and Rank-2 0.58 floor are transparent diagnostics; specific mandatory family prerequisites remain eligibility tests. Never pad or substitute a derived contract.

Show `SUPPLIED_SCOPE_GATE`, competitor key/p/gap, precision error, floor/family status and the best supported non-complementary supplied alternative. Show line difficulty in units and z where SD is supported. Compute exact joint losing-state mass, valid Fr?chet bounds or an explicit unavailable result under SF7; show both-decisive conditioning only with a genuine joint denominator. Flag complements and mechanical protection. Do not reorder primary picks to hide dependence or call protected Hit@2 predictive skill.

Optional derived ladders and published-policy comparators have separately predeclared universes. Freeze supported RET03/RET04/XCARD6, rank-delta and base-only shadows with their correct names and scopes, or state why not computed. All are NOT_PRIMARY and cannot change the original supplied slate, ID or grade. Retain every supplied row as a candidate research record with its separate future training eligibility.

### 6. Playing conditions and frozen action rules

Verify singles/doubles, best-of format, advantage/no-ad games, ordinary/final-set tiebreak triggers and target, and match-tiebreak game-count treatment. Check tournament/round-specific rules and participant identity. Freeze retirement, walkover, withdrawal, suspension/resumption and minimum-play action terms. Sporting advancement alone does not establish the contract grade.

### 7. Write, audit and return

Use the mini's own applicable CARD_AND_LOG_TEMPLATES format; retain the near-650-word decision target where prescribed and full A1–A9 evidence. Record literal/normalised contracts, common-distribution calculations, baseline coverage, full supplied ranking, formal picks, all missingness, source receipts and original model/scenario/recipe versions. Freeze the exact later settlement fields, action definitions and capture plan without performing settlement.

Apply SF11's pre-write concurrency/lease/freeze/ID checks and original-block custody. Append one complete card before the footer for a genuinely new event, or one dated addendum for an existing event; update only authorised intake/footer totals. Preserve all earlier issued bytes. Read back the actual write, reconcile keys/counts/probabilities/timestamps/footer and verify prior blocks. A draft or failed verification cannot claim a successful append/ID advance.

In A9 complete the mini's actual checklist (C1–C20 for reference mini-log-7, or the original legacy checklist plus dated compatibility gaps), FR1–FR6, SF-A1–SF-A12 and Q4 calculation checks with specific evidence/status. Return the full new card/addendum or complete non-issued draft, exact path, working ID/status, timing/exposure, all supplied probabilities, supplied-only formal picks or precise no-pick reason, gate/joint/sensitivity/baseline results and updated footer/readback receipt. Explicitly state settlement NOT_PERFORMED, canonical import NOT_PERFORMED, GitHub writes NO and new canonical IDs 0. Make no success guarantee.

---

## RUGBY LEAGUE / UNION

### Event input — fill before executing this sport's seven steps

```text
Upcoming Rugby League / Union Match: <participants; exact competition; season/stage/format; date/time/timezone>
Native event ID / game number / official URL: <if supplied; otherwise verify>
Venue / home-away orientation: <if supplied; otherwise verify>
Active mini: <exact existing authorised local path, or identify from accessible files>
Supplied contracts (one literal proposition per line):
1. <exact user text>
2. <exact user text; optional>
3. <additional exact user text; optional>
Contract period / endpoint / action terms: <explicit supplied terms; resolve missing material definitions>
Requested primary ranking: SUPPLIED CONTRACTS ONLY
Optional derived shadows: <requested / useful supported diagnostics only>
Research: Exact rugby code; starters/bench/spine/kicker; scoring/discipline/territory; L5/L10/L15/L20; draw/golden-point/extra-time endpoint.
CONTINUE_IF_LATE: YES
GitHub main: READ ONLY; settlement/import: NOT_PERFORMED
```

Any nonempty number of supplied contracts is valid. Remove unused placeholders; do not treat them as propositions or populate them with invented examples.

### 1. Read and establish authority

Complete 0.2 from one verified full published SHA. Read the applicable sport/competition rules, SOURCES routes, league/tour profiles, archive guide/defect notes and base-rate register as well as the full active mini and relevant canonical records. Locate actual filenames/sections; do not invent a sport rules file or use an outdated league constant without disclosure. Print the reading receipt, actual versions, authority differences, permitted writes and unavailable dependencies.

Current controls govern over historical engine notes. If authority/custody inputs needed for issuance are inaccessible, complete the research as `READ_ONLY_DRAFT / NOT_ISSUED`.

### 2. Identity, duplicate and timing gate

Verify teams, competition (NRL, Super League, Rugby Championship, Six Nations, etc.), round/stage, venue, native ID, official scheduled kickoff, venue zone, UTC and Australia/Sydney time.

Apply SF10/SF11: search all relevant local mini/carryover and canonical bodies/status by native ID, event key and aliases. Doubleheaders, resumed events and postponements need explicit identity handling. A duplicate receives an addendum under its existing ID. Log authorised intake whatever the research outcome; otherwise include a draft intake row.

Verify the named mini, format, writer/lease, freeze status, current canonical allocation and outstanding local sequence. Do not reserve, skip, collide, renumber or consume a canonical ID. Keep analysis cutoff, research completion, actual issue and state recheck separate. Complete the two-step lineup/repricing target when timing permits; research comprehensively if late. Recheck actual state immediately before issue. Outcome exposure prevents prospective pregame credit, even with a reconstructed earlier cutoff.

### 3. Evidence, team sheet and archive

Follow official league match center → structured provider → quality corroboration routes. For each decisive claim retain URL, exact field/value or brief extract, source publication/update time when known, retrieval time and provenance/lineage. Log inaccessible/stale/conflicting sources. Three domains are not three independent collectors. No odds/tips/previews/fantasy inputs.

Verify team/bench/spine or halves/front row, kicking, possession/territory, discipline, workload and weather; probable is not confirmed. Inspect actual archive contents under `Previous Sports Results/Rugby/...` and print files, logical rows read, competition/stage filters, latest usable date and missingness. Use only results known before cutoff. Do not use postgame narrative or full-season aggregates from after cutoff.

#### Mandatory historical-form implementation for this sport (FR1–FR6)

For both teams last 5/10/15/20 within their own code and competition: points for/against, tries, conversions, goal-kicking, possession/territory, sets/ruck or lineouts/rucks by code where sourced, discipline, stage, venue and opponent strength. Never pool league and union scoring. Confirm starting squad, bench, late replacements and specialist spine/halves/kicker availability. Follow the GLOBAL RULE above for both participants; place the required four-window tables, event-level trace, missingness, non-overlap trend, opponent adjustments and official lineup gate in A3; propagate supported numbers to A4 and disclose window-choice sensitivity in A7/A9. Never treat these historical summaries as a fitted/calibrated model.

### 4. Distribution, expected score and comparator

Build the simplest defensible coherent rugby distribution: model the appropriate score events (tries, conversions, penalties, field goals) and key margins; league and union scoring systems differ. Use only applicable measured regime effects; finals need not always reduce the mean. Print every parameter and its basis, formula/table, normalization, tail treatment, covariance and endpoint transitions. If the required calculation cannot be done, report a supported approximation with limitations, or qualitative research with NOT_ESTIMATED probabilities.

Produce expected score terms from CARD_AND_LOG_TEMPLATES §3a: team points, total, signed margin and supported SDs. Keep zeros; mark missing or irrelevant terms. Print all winner/draw/tie masses. For **every distinct user-supplied contract** retain unconditional W/P/L/V and p_card=W/(W+L), with denominator and action convention; all other priced candidates are separate NOT_PRIMARY shadows.

Attempt BASELINE_LEAGUE_V1 on **each supported supplied contract's exact same line and endpoint** from independent league-only inputs, frozen before issue. Print recipe, source cohort/n/cutoff and parameters separately from the team model. No 0.5 placeholder or retrospective baseline fill. Missing baseline does not stop the card; it limits later skill measurement.

If inputs are unfitted/stale/early-season/unconfirmed, price the **declared low/base/high mixture** (default 0.25/0.50/0.25, frozen before ranking) and show `p_base` and p_card for every supplied line. Show an adjustment table (venue, lineup, spine availability, rest/travel), unadjusted distribution/pair and low/base/high sensitivity on material uncertain inputs. Any adjustment-driven pair change is ADJUSTMENT_DEPENDENT, even below 0.25 SD. Report plausible probability ranges as sensitivity, not confidence intervals. Do not move individual probabilities outside the shared model.

**Rugby implementation safeguards.** Keep league and union models/cohorts separate. Freeze the competition-season point values, scoring-event opportunities and dependencies: conversions follow eligible tries, not independent free scoring counts. Use a supported discrete compound score model or clearly labelled approximation; respect key-margin and push masses. Golden-point/extra-time winner mapping differs from regulation draw probability. Personnel impact must distinguish spine/halves/kicker and forwards/interchange where evidence supports it; avoid assigning invented causal point values. Finals effects require a matching measured profile or explicitly assumed scenarios; a final does not automatically imply lower scoring.

**Required execution for this section:** apply Q1–Q4, SF3 and FR4/FR5. Mix unconditional masses before conditioning; print p_base separately. Preserve action/definition/known-at limits, score moments, exact supplied-line baseline coverage, numerical error, adjustment table, unadjusted pair and scenario/window rank changes. An absent supported field or calculation stays missing.

### 5. Supplied ranking, eligibility, gates and dependence

Freeze the literal deduplicated user-supplied universe and definitions before modelling. Price all supported supplied keys from the actual compatible distributions; keep every unresolved/unpriced/excluded row visible. Follow SF4 for the complete probability-sorted `SUPPLIED_CONTRACT_RANKING`, 90% selection ceiling, known-at/definition support and any would-be-Rank-1-only family filtering. Select 0–4 actual numeric supplied rows; only Ranks 1–2 are primary picks. The general 0.62/0.04 gate and Rank-2 0.58 floor are transparent diagnostics; specific mandatory family prerequisites remain eligibility tests. Never pad or substitute a derived contract.

Show `SUPPLIED_SCOPE_GATE`, competitor key/p/gap, precision error, floor/family status and the best supported non-complementary supplied alternative. Show line difficulty in units and z where SD is supported. Compute exact joint losing-state mass, valid Fr?chet bounds or an explicit unavailable result under SF7; show both-decisive conditioning only with a genuine joint denominator. Flag complements and mechanical protection. Do not reorder primary picks to hide dependence or call protected Hit@2 predictive skill.

Optional derived ladders and published-policy comparators have separately predeclared universes. Freeze supported RET03/RET04/XCARD6, rank-delta and base-only shadows with their correct names and scopes, or state why not computed. All are NOT_PRIMARY and cannot change the original supplied slate, ID or grade. Retain every supplied row as a candidate research record with its separate future training eligibility.

### 6. Playing conditions and frozen action rules

Verify code, regulation duration, scoring values, interchange/substitution rules, regular-season draw/golden-point treatment, finals/knockout extra time and competition-season variations. Do not infer NRL, Super League or union behaviour from another code/competition. Freeze regulation versus full-result action and any cancelled/shortened-match conventions.

### 7. Write, audit and return

Use the mini's own applicable CARD_AND_LOG_TEMPLATES format; retain the near-650-word decision target where prescribed and full A1–A9 evidence. Record literal/normalised contracts, common-distribution calculations, baseline coverage, full supplied ranking, formal picks, all missingness, source receipts and original model/scenario/recipe versions. Freeze the exact later settlement fields, action definitions and capture plan without performing settlement.

Apply SF11's pre-write concurrency/lease/freeze/ID checks and original-block custody. Append one complete card before the footer for a genuinely new event, or one dated addendum for an existing event; update only authorised intake/footer totals. Preserve all earlier issued bytes. Read back the actual write, reconcile keys/counts/probabilities/timestamps/footer and verify prior blocks. A draft or failed verification cannot claim a successful append/ID advance.

In A9 complete the mini's actual checklist (C1–C20 for reference mini-log-7, or the original legacy checklist plus dated compatibility gaps), FR1–FR6, SF-A1–SF-A12 and Q4 calculation checks with specific evidence/status. Return the full new card/addendum or complete non-issued draft, exact path, working ID/status, timing/exposure, all supplied probabilities, supplied-only formal picks or precise no-pick reason, gate/joint/sensitivity/baseline results and updated footer/readback receipt. Explicitly state settlement NOT_PERFORMED, canonical import NOT_PERFORMED, GitHub writes NO and new canonical IDs 0. Make no success guarantee.

---

## AFL / AFLW

### Event input — fill before executing this sport's seven steps

```text
Upcoming AFL / AFLW Game: <participants; exact competition; season/stage/format; date/time/timezone>
Native event ID / game number / official URL: <if supplied; otherwise verify>
Venue / home-away orientation: <if supplied; otherwise verify>
Active mini: <exact existing authorised local path, or identify from accessible files>
Supplied contracts (one literal proposition per line):
1. <exact user text>
2. <exact user text; optional>
3. <additional exact user text; optional>
Contract period / endpoint / action terms: <explicit supplied terms; resolve missing material definitions>
Requested primary ranking: SUPPLIED CONTRACTS ONLY
Optional derived shadows: <requested / useful supported diagnostics only>
Research: Exact competition; selected side/interchange/late outs; scoring shots/accuracy; weather/venue; L5/L10/L15/L20; draw/finals endpoint.
CONTINUE_IF_LATE: YES
GitHub main: READ ONLY; settlement/import: NOT_PERFORMED
```

Any nonempty number of supplied contracts is valid. Remove unused placeholders; do not treat them as propositions or populate them with invented examples.

### 1. Read and establish authority

Complete 0.2 from one verified full published SHA. Read the applicable sport/competition rules, SOURCES routes, league/tour profiles, archive guide/defect notes and base-rate register as well as the full active mini and relevant canonical records. Locate actual filenames/sections; do not invent a sport rules file or use an outdated league constant without disclosure. Print the reading receipt, actual versions, authority differences, permitted writes and unavailable dependencies.

Current controls govern over historical engine notes. If authority/custody inputs needed for issuance are inaccessible, complete the research as `READ_ONLY_DRAFT / NOT_ISSUED`.

### 2. Identity, duplicate and timing gate

Verify clubs, competition (AFL men vs AFLW), round/finals stage, venue, native ID, official scheduled first bounce, venue zone, UTC and Australia/Sydney time.

Apply SF10/SF11: search all relevant local mini/carryover and canonical bodies/status by native ID, event key and aliases. Doubleheaders, resumed events and postponements need explicit identity handling. A duplicate receives an addendum under its existing ID. Log authorised intake whatever the research outcome; otherwise include a draft intake row.

Verify the named mini, format, writer/lease, freeze status, current canonical allocation and outstanding local sequence. Do not reserve, skip, collide, renumber or consume a canonical ID. Keep analysis cutoff, research completion, actual issue and state recheck separate. Complete the two-step lineup/repricing target when timing permits; research comprehensively if late. Recheck actual state immediately before issue. Outcome exposure prevents prospective pregame credit, even with a reconstructed earlier cutoff.

### 3. Evidence, lineup and archive

Follow official AFL match centre / AFLW app → structured provider → quality corroboration routes. For each decisive claim retain URL, exact field/value or brief extract, source publication/update time when known, retrieval time and provenance/lineage. Log inaccessible/stale/conflicting sources. Three domains are not three independent collectors. No odds/tips/previews/fantasy inputs.

Verify teams, ruck/midfield, clearances, inside-50/scoring-shot creation, conversion, defence, rest/venue/weather; probable is not confirmed. Inspect actual archive contents under `Previous Sports Results/AFL/...` and print files, logical rows read, competition/season filters, latest usable date and missingness. Use only results known before cutoff. Do not use postgame narrative or full-season aggregates from after cutoff.

#### Mandatory historical-form implementation for this sport (FR1–FR6)

For both clubs last 5/10/15/20 within AFL or AFLW separately: goals, behinds, scoring shots, accuracy, points for/against, inside-50/clearance measures where sourced, venue/wind, opponent strength and late selections. Do not mix AFL/AFLW quarter lengths, finals endpoints or historical rules. Confirm team sheet, interchange/substitute and late outs. Follow the GLOBAL RULE above for both participants; place the required four-window tables, event-level trace, missingness, non-overlap trend, opponent adjustments and official lineup gate in A3; propagate supported numbers to A4 and disclose window-choice sensitivity in A7/A9. Never treat these historical summaries as a fitted/calibrated model.

### 4. Distribution, expected score and comparator

Build the simplest defensible coherent Australian rules distribution: separate shots from accuracy; points = 6 × goals + behinds. Use competition-specific pace/length and draw/finals rules. Explain shrinkage of unusual conversion rather than assuming a rebound. Print every parameter and its basis, formula/table, normalization, tail treatment, covariance and endpoint transitions. If the required calculation cannot be done, report a supported approximation with limitations, or qualitative research with NOT_ESTIMATED probabilities.

Produce expected score terms from CARD_AND_LOG_TEMPLATES §3a: goals, behinds, team points (means & SDs), total points, signed margin and supported SDs for the correct competition. Keep zeros; mark missing or irrelevant terms. Print all winner/draw/tie masses. For **every distinct user-supplied contract** retain unconditional W/P/L/V and p_card=W/(W+L), with denominator and action convention; all other priced candidates are separate NOT_PRIMARY shadows.

Attempt BASELINE_LEAGUE_V1 on **each supported supplied contract's exact same line and endpoint** from independent league-only inputs, frozen before issue. Print recipe, source cohort/n/cutoff and parameters separately from the team model. No 0.5 placeholder or retrospective baseline fill. Missing baseline does not stop the card; it limits later skill measurement.

If inputs are unfitted/stale/early-season/unconfirmed, price the **declared low/base/high mixture** (default 0.25/0.50/0.25, frozen before ranking) and show `p_base` and p_card for every supplied line. Show an adjustment table (venue, rest, weather/wind, ruck/midfield matchups), unadjusted distribution/pair and low/base/high sensitivity on material uncertain inputs. Any adjustment-driven pair change is ADJUSTMENT_DEPENDENT, even below 0.25 SD. Report plausible probability ranges as sensitivity, not confidence intervals. Do not move individual probabilities outside the shared model.

**Australian rules implementation safeguards.** Where supported, model scoring shots and conversion jointly, with `points = 6×goals + behinds`; print goal/behind/points moments and the supported covariance. A score-only approximation does not provide exact scoring-shot or player-goal probabilities. Shrink unusual conversion under the frozen recipe without assuming inevitable rebound. Keep AFL and AFLW durations, rules eras and profiles separate. Venue dimensions, wind/rain, ruck/midfield and rotation effects need evidence and are counted once. Quarter totals require actual period fields and time-on conventions; finals extra-time endpoints need current competition-specific transitions.

**Required execution for this section:** apply Q1–Q4, SF3 and FR4/FR5. Mix unconditional masses before conditioning; print p_base separately. Preserve action/definition/known-at limits, score moments, exact supplied-line baseline coverage, numerical error, adjustment table, unadjusted pair and scenario/window rank changes. An absent supported field or calculation stays missing.

### 5. Supplied ranking, eligibility, gates and dependence

Freeze the literal deduplicated user-supplied universe and definitions before modelling. Price all supported supplied keys from the actual compatible distributions; keep every unresolved/unpriced/excluded row visible. Follow SF4 for the complete probability-sorted `SUPPLIED_CONTRACT_RANKING`, 90% selection ceiling, known-at/definition support and any would-be-Rank-1-only family filtering. Select 0–4 actual numeric supplied rows; only Ranks 1–2 are primary picks. The general 0.62/0.04 gate and Rank-2 0.58 floor are transparent diagnostics; specific mandatory family prerequisites remain eligibility tests. Never pad or substitute a derived contract.

Show `SUPPLIED_SCOPE_GATE`, competitor key/p/gap, precision error, floor/family status and the best supported non-complementary supplied alternative. Show line difficulty in units and z where SD is supported. Compute exact joint losing-state mass, valid Fr?chet bounds or an explicit unavailable result under SF7; show both-decisive conditioning only with a genuine joint denominator. Flag complements and mechanical protection. Do not reorder primary picks to hide dependence or call protected Hit@2 predictive skill.

Optional derived ladders and published-policy comparators have separately predeclared universes. Freeze supported RET03/RET04/XCARD6, rank-delta and base-only shadows with their correct names and scopes, or state why not computed. All are NOT_PRIMARY and cannot change the original supplied slate, ID or grade. Retain every supplied row as a candidate research record with its separate future training eligibility.

### 6. Playing conditions and frozen action rules

Verify the exact AFL/AFLW competition-season quarter duration and time-on, interchange/substitute rules, regular-season draws, finals extra time and shortened/cancelled-match rules. Do not hard-code an old AFLW quarter duration. Points, goals, behinds and scoring shots need distinct frozen definitions; quarter/finals action must match the captured source fields.

### 7. Write, audit and return

Use the mini's own applicable CARD_AND_LOG_TEMPLATES format; retain the near-650-word decision target where prescribed and full A1–A9 evidence. Record literal/normalised contracts, common-distribution calculations, baseline coverage, full supplied ranking, formal picks, all missingness, source receipts and original model/scenario/recipe versions. Freeze the exact later settlement fields, action definitions and capture plan without performing settlement.

Apply SF11's pre-write concurrency/lease/freeze/ID checks and original-block custody. Append one complete card before the footer for a genuinely new event, or one dated addendum for an existing event; update only authorised intake/footer totals. Preserve all earlier issued bytes. Read back the actual write, reconcile keys/counts/probabilities/timestamps/footer and verify prior blocks. A draft or failed verification cannot claim a successful append/ID advance.

In A9 complete the mini's actual checklist (C1–C20 for reference mini-log-7, or the original legacy checklist plus dated compatibility gaps), FR1–FR6, SF-A1–SF-A12 and Q4 calculation checks with specific evidence/status. Return the full new card/addendum or complete non-issued draft, exact path, working ID/status, timing/exposure, all supplied probabilities, supplied-only formal picks or precise no-pick reason, gate/joint/sensitivity/baseline results and updated footer/readback receipt. Explicitly state settlement NOT_PERFORMED, canonical import NOT_PERFORMED, GitHub writes NO and new canonical IDs 0. Make no success guarantee.

---

## AMERICAN FOOTBALL

### Event input — fill before executing this sport's seven steps

```text
Upcoming American Football Game: <participants; exact competition; season/stage/format; date/time/timezone>
Native event ID / game number / official URL: <if supplied; otherwise verify>
Venue / home-away orientation: <if supplied; otherwise verify>
Active mini: <exact existing authorised local path, or identify from accessible files>
Supplied contracts (one literal proposition per line):
1. <exact user text>
2. <exact user text; optional>
3. <additional exact user text; optional>
Contract period / endpoint / action terms: <explicit supplied terms; resolve missing material definitions>
Requested primary ranking: SUPPLIED CONTRACTS ONLY
Optional derived shadows: <requested / useful supported diagnostics only>
Research: QB/inactives/active personnel; drive/play efficiency; key margins; weather; L5/L10/L15/L20; competition-season overtime rules.
CONTINUE_IF_LATE: YES
GitHub main: READ ONLY; settlement/import: NOT_PERFORMED
```

Any nonempty number of supplied contracts is valid. Remove unused placeholders; do not treat them as propositions or populate them with invented examples.

### 1. Read and establish authority

Complete 0.2 from one verified full published SHA. Read the applicable sport/competition rules, SOURCES routes, league/tour profiles, archive guide/defect notes and base-rate register as well as the full active mini and relevant canonical records. Locate actual filenames/sections; do not invent a sport rules file or use an outdated league constant without disclosure. Print the reading receipt, actual versions, authority differences, permitted writes and unavailable dependencies.

Current controls govern over historical engine notes. If authority/custody inputs needed for issuance are inaccessible, complete the research as `READ_ONLY_DRAFT / NOT_ISSUED`.

### 2. Identity, duplicate and timing gate

Verify teams, league/competition (NFL, college/NCAA, etc.), week, venue, native ID, official scheduled kickoff, venue zone, UTC and Australia/Sydney time.

Apply SF10/SF11: search all relevant local mini/carryover and canonical bodies/status by native ID, event key and aliases. Doubleheaders, resumed events and postponements need explicit identity handling. A duplicate receives an addendum under its existing ID. Log authorised intake whatever the research outcome; otherwise include a draft intake row.

Verify the named mini, format, writer/lease, freeze status, current canonical allocation and outstanding local sequence. Do not reserve, skip, collide, renumber or consume a canonical ID. Keep analysis cutoff, research completion, actual issue and state recheck separate. Complete the two-step lineup/repricing target when timing permits; research comprehensively if late. Recheck actual state immediately before issue. Outcome exposure prevents prospective pregame credit, even with a reconstructed earlier cutoff.

### 3. Evidence, inactives and archive

Follow official NFL Game Center / college box score → structured provider → quality corroboration routes. For each decisive claim retain URL, exact field/value or brief extract, source publication/update time when known, retrieval time and provenance/lineage. Log inaccessible/stale/conflicting sources. Three domains are not three independent collectors. No odds/tips/previews/fantasy inputs.

Verify QB, line/skill/defensive availability, official pregame inactives list at the competition-specific announcement time, efficiency, drive/play pace, pressure, special teams, rest/weather; probable is not confirmed. Inspect actual archive contents under `Previous Sports Results/American Football/<league>/...` and print files, logical rows read, season/week filters, latest usable date and missingness. Use only results known before cutoff. Do not use postgame narrative or full-season aggregates from after cutoff.

#### Mandatory historical-form implementation for this sport (FR1–FR6)

For both teams last 5/10/15/20 comparable games (NFL versus NCAA separate): points/drive, EPA/play, offensive/defensive success, turnovers, red-zone scoring, key margin masses including 3 and 7, venue/rest and opponent strength **only if recorded**. Distinguish quarterback-specific game appearances and starters from team windows. Confirm QB, official game-day inactives, active offensive line and relevant defensive personnel. Follow the GLOBAL RULE above for both participants; place the required four-window tables, event-level trace, missingness, non-overlap trend, opponent adjustments and official lineup gate in A3; propagate supported numbers to A4 and disclose window-choice sensitivity in A7/A9. Never treat these historical summaries as a fitted/calibrated model.

### 4. Distribution, expected score and comparator

Build the simplest defensible coherent football distribution: use supported discrete score/drive structure or disclose an approximation; show push/key-margin mass near 3/7 and other relevant numbers. No claim to an exact drive model without its calculation. Print every parameter and its basis, formula/table, normalization, tail treatment, covariance and endpoint transitions. If the required calculation cannot be done, report a supported approximation with limitations, or qualitative research with NOT_ESTIMATED probabilities.

Produce expected score terms from CARD_AND_LOG_TEMPLATES §3a: team points, total, signed margin and supported SDs. Keep zeros; mark missing or irrelevant terms. Print all winner/draw/tie masses. For **every distinct user-supplied contract** retain unconditional W/P/L/V and p_card=W/(W+L), with denominator and action convention; all other priced candidates are separate NOT_PRIMARY shadows.

Attempt BASELINE_LEAGUE_V1 on **each supported supplied contract's exact same line and endpoint** from independent league-only inputs, frozen before issue. Print recipe, source cohort/n/cutoff and parameters separately from the team model. No 0.5 placeholder or retrospective baseline fill. Missing baseline does not stop the card; it limits later skill measurement.

If inputs are unfitted/stale/early-season/unconfirmed, price the **declared low/base/high mixture** (default 0.25/0.50/0.25, frozen before ranking) and show `p_base` and p_card for every supplied line. Show an adjustment table (QB/injuries, rest, weather/wind), unadjusted distribution/pair and low/base/high sensitivity on material uncertain inputs. Any adjustment-driven pair change is ADJUSTMENT_DEPENDENT, even below 0.25 SD. Report plausible probability ranges as sensitivity, not confidence intervals. Do not move individual probabilities outside the shared model.

**American football implementation safeguards.** Separate NFL/NCAA/other rules, season, stage and scoring/OT structure. Use observed drive/play denominators for efficiency; scores alone cannot produce measured EPA, pressure or red-zone rates. QB changes, active line/personnel, turnovers, weather and special teams need supported inputs/adjustment scenarios. Integer spreads/totals require common-distribution mass at relevant key values, including 3 and 7 when applicable; a smooth normal CDF alone gives no push mass. Quarter/half/player counts need actual fields and compatible opportunity models. Verify the current season's regular/postseason possession guarantees, period length, tie/alternating-possession rules; the predecessor's NFL summary is not an authority for another season.

**Required execution for this section:** apply Q1–Q4, SF3 and FR4/FR5. Mix unconditional masses before conditioning; print p_base separately. Preserve action/definition/known-at limits, score moments, exact supplied-line baseline coverage, numerical error, adjustment table, unadjusted pair and scenario/window rank changes. An absent supported field or calculation stays missing.

### 5. Supplied ranking, eligibility, gates and dependence

Freeze the literal deduplicated user-supplied universe and definitions before modelling. Price all supported supplied keys from the actual compatible distributions; keep every unresolved/unpriced/excluded row visible. Follow SF4 for the complete probability-sorted `SUPPLIED_CONTRACT_RANKING`, 90% selection ceiling, known-at/definition support and any would-be-Rank-1-only family filtering. Select 0–4 actual numeric supplied rows; only Ranks 1–2 are primary picks. The general 0.62/0.04 gate and Rank-2 0.58 floor are transparent diagnostics; specific mandatory family prerequisites remain eligibility tests. Never pad or substitute a derived contract.

Show `SUPPLIED_SCOPE_GATE`, competitor key/p/gap, precision error, floor/family status and the best supported non-complementary supplied alternative. Show line difficulty in units and z where SD is supported. Compute exact joint losing-state mass, valid Fr?chet bounds or an explicit unavailable result under SF7; show both-decisive conditioning only with a genuine joint denominator. Flag complements and mechanical protection. Do not reorder primary picks to hide dependence or call protected Hit@2 predictive skill.

Optional derived ladders and published-policy comparators have separately predeclared universes. Freeze supported RET03/RET04/XCARD6, rank-delta and base-only shadows with their correct names and scopes, or state why not computed. All are NOT_PRIMARY and cannot change the original supplied slate, ID or grade. Retain every supplied row as a candidate research record with its separate future training eligibility.

### 6. Playing conditions and frozen action rules

Verify regulation duration, scoring values, clock rules, regular-season/postseason overtime length, possession guarantees, tie possibility and any NCAA alternating-possession conversion rounds for the actual season. Rules can change; the old regular-season/postseason summary must not be treated as current without verification. Freeze regulation/full-game/period/player participation and postponed/shortened-game action terms.

### 7. Write, audit and return

Use the mini's own applicable CARD_AND_LOG_TEMPLATES format; retain the near-650-word decision target where prescribed and full A1–A9 evidence. Record literal/normalised contracts, common-distribution calculations, baseline coverage, full supplied ranking, formal picks, all missingness, source receipts and original model/scenario/recipe versions. Freeze the exact later settlement fields, action definitions and capture plan without performing settlement.

Apply SF11's pre-write concurrency/lease/freeze/ID checks and original-block custody. Append one complete card before the footer for a genuinely new event, or one dated addendum for an existing event; update only authorised intake/footer totals. Preserve all earlier issued bytes. Read back the actual write, reconcile keys/counts/probabilities/timestamps/footer and verify prior blocks. A draft or failed verification cannot claim a successful append/ID advance.

In A9 complete the mini's actual checklist (C1–C20 for reference mini-log-7, or the original legacy checklist plus dated compatibility gaps), FR1–FR6, SF-A1–SF-A12 and Q4 calculation checks with specific evidence/status. Return the full new card/addendum or complete non-issued draft, exact path, working ID/status, timing/exposure, all supplied probabilities, supplied-only formal picks or precise no-pick reason, gate/joint/sensitivity/baseline results and updated footer/readback receipt. Explicitly state settlement NOT_PERFORMED, canonical import NOT_PERFORMED, GitHub writes NO and new canonical IDs 0. Make no success guarantee.

---

## OTHER SPORTS

### Event input — fill before executing this sport's seven steps

```text
Upcoming Other Sports Event: <participants; exact competition; season/stage/format; date/time/timezone>
Native event ID / game number / official URL: <if supplied; otherwise verify>
Venue / home-away orientation: <if supplied; otherwise verify>
Active mini: <exact existing authorised local path, or identify from accessible files>
Supplied contracts (one literal proposition per line):
1. <exact user text>
2. <exact user text; optional>
3. <additional exact user text; optional>
Contract period / endpoint / action terms: <explicit supplied terms; resolve missing material definitions>
Requested primary ranking: SUPPLIED CONTRACTS ONLY
Optional derived shadows: <requested / useful supported diagnostics only>
Research: Exact participant/format/field definitions; readiness and conditions; comparable L5/L10/L15/L20; sport-specific outcome/action endpoint.
CONTINUE_IF_LATE: YES
GitHub main: READ ONLY; settlement/import: NOT_PERFORMED
```

Any nonempty number of supplied contracts is valid. Remove unused placeholders; do not treat them as propositions or populate them with invented examples.

### 1. Read and establish authority

Complete 0.2 from one verified full published SHA. Read the applicable sport/competition rules, SOURCES routes, league/tour profiles, archive guide/defect notes and base-rate register as well as the full active mini and relevant canonical records. Locate actual filenames/sections; do not invent a sport rules file or use an outdated league constant without disclosure. Print the reading receipt, actual versions, authority differences, permitted writes and unavailable dependencies.

Current controls govern over historical engine notes. If authority/custody inputs needed for issuance are inaccessible, complete the research as `READ_ONLY_DRAFT / NOT_ISSUED`.

### 2. Identity, duplicate and timing gate

Verify participants, competition, season, stage, venue, native ID, official scheduled start, venue zone, UTC and Australia/Sydney time.

Apply SF10/SF11: search all relevant local mini/carryover and canonical bodies/status by native ID, event key and aliases. Doubleheaders, resumed events and postponements need explicit identity handling. A duplicate receives an addendum under its existing ID. Log authorised intake whatever the research outcome; otherwise include a draft intake row.

Verify the named mini, format, writer/lease, freeze status, current canonical allocation and outstanding local sequence. Do not reserve, skip, collide, renumber or consume a canonical ID. Keep analysis cutoff, research completion, actual issue and state recheck separate. Complete the two-step lineup/repricing target when timing permits; research comprehensively if late. Recheck actual state immediately before issue. Outcome exposure prevents prospective pregame credit, even with a reconstructed earlier cutoff.

### 3. Evidence and archive

Follow official governing body / field owner match center → structured providers → quality corroboration routes. For each decisive claim retain URL, exact field/value or brief extract, source publication/update time when known, retrieval time and provenance/lineage. Log inaccessible/stale/conflicting sources. Three domains are not three independent collectors. No odds/tips/previews/fantasy inputs.

Verify confirmed participant readiness, lineups and availability; probable is not confirmed. Inspect archive if available. If sources cannot support numerical modelling, retain supported qualitative research; use NO_FORECAST only when a responsible sporting direction is unsupported.

#### Mandatory historical-form implementation for this sport (FR1–FR6)

For each named team/player, attempt last 5/10/15/20 completed comparable contests with correct match definition, sport-specific scoring, venue, opponent strength, roster status, verified dates/IDs and genuine missingness. Do not transfer another sport’s assumptions; choose `NO_FORECAST` if the event identity and responsible sporting direction are unsupported; otherwise retain qualitative research with explicit missing fields. Follow the GLOBAL RULE above for both participants; place the required four-window tables, event-level trace, missingness, non-overlap trend, opponent adjustments and official lineup gate in A3; propagate supported numbers to A4 and disclose window-choice sensitivity in A7/A9. Never treat these historical summaries as a fitted/calibrated model.

### 4. Distribution, expected score and comparator

Build the simplest defensible coherent sport distribution you can actually compute. Print every parameter and its basis, formula/table, normalization, tail treatment, covariance and endpoint transitions. If the required calculation cannot be done, report a supported approximation with limitations, or qualitative research with NOT_ESTIMATED probabilities.

Produce expected score terms from CARD_AND_LOG_TEMPLATES §3a where supported; otherwise mark NOT_COMPUTED. Keep zeros; mark missing or irrelevant terms. Print all winner/draw/tie masses. For **every distinct user-supplied contract** retain unconditional W/P/L/V and p_card=W/(W+L), with denominator and action convention; all other priced candidates are separate NOT_PRIMARY shadows.

Attempt BASELINE_LEAGUE_V1 on each supported supplied contract if independent league data exist. Show sensitivity on material uncertain inputs. Report plausible probability ranges as sensitivity, not confidence intervals. Do not move individual probabilities outside the shared model.

**Other-sport implementation safeguards.** First define the contest unit and scoring state: set, round, race, map, leg, distance/time, judged score or multi-participant finish. Participant rank, win, podium and head-to-head are different quantities. Verify completion, disqualification/withdrawal, dead-heat/tie and abandonment rules. Multi-participant win probabilities require a compatible field-wide construction and cannot be individually assigned to exceed total mass. Historical team-score distributions cannot price unrelated timing or rank outcomes. If no supported sport/format model exists, retain qualitative research and missing probabilities rather than copying another sport's formulas.

**Required execution for this section:** apply Q1–Q4, SF3 and FR4/FR5. Mix unconditional masses before conditioning; print p_base separately. Preserve action/definition/known-at limits, score moments, exact supplied-line baseline coverage, numerical error, adjustment table, unadjusted pair and scenario/window rank changes. An absent supported field or calculation stays missing.

### 5. Supplied ranking, eligibility, gates and dependence

Freeze the literal deduplicated user-supplied universe and definitions before modelling. Price all supported supplied keys from the actual compatible distributions; keep every unresolved/unpriced/excluded row visible. Follow SF4 for the complete probability-sorted `SUPPLIED_CONTRACT_RANKING`, 90% selection ceiling, known-at/definition support and any would-be-Rank-1-only family filtering. Select 0–4 actual numeric supplied rows; only Ranks 1–2 are primary picks. The general 0.62/0.04 gate and Rank-2 0.58 floor are transparent diagnostics; specific mandatory family prerequisites remain eligibility tests. Never pad or substitute a derived contract.

Show `SUPPLIED_SCOPE_GATE`, competitor key/p/gap, precision error, floor/family status and the best supported non-complementary supplied alternative. Show line difficulty in units and z where SD is supported. Compute exact joint losing-state mass, valid Fr?chet bounds or an explicit unavailable result under SF7; show both-decisive conditioning only with a genuine joint denominator. Flag complements and mechanical protection. Do not reorder primary picks to hide dependence or call protected Hit@2 predictive skill.

Optional derived ladders and published-policy comparators have separately predeclared universes. Freeze supported RET03/RET04/XCARD6, rank-delta and base-only shadows with their correct names and scopes, or state why not computed. All are NOT_PRIMARY and cannot change the original supplied slate, ID or grade. Retain every supplied row as a candidate research record with its separate future training eligibility.

### 6. Playing conditions and frozen action rules

Verify the governing body, exact competition/format, scoring/finish units, contest duration or termination, tie/dead-heat/tiebreak/overtime, disqualification/withdrawal and abandonment action. Multi-stage and multi-participant competitions require explicit scope and event identity. Never infer these rules or numerical priors from an unrelated sport.

### 7. Write, audit and return

Use the mini's own applicable CARD_AND_LOG_TEMPLATES format; retain the near-650-word decision target where prescribed and full A1–A9 evidence. Record literal/normalised contracts, common-distribution calculations, baseline coverage, full supplied ranking, formal picks, all missingness, source receipts and original model/scenario/recipe versions. Freeze the exact later settlement fields, action definitions and capture plan without performing settlement.

Apply SF11's pre-write concurrency/lease/freeze/ID checks and original-block custody. Append one complete card before the footer for a genuinely new event, or one dated addendum for an existing event; update only authorised intake/footer totals. Preserve all earlier issued bytes. Read back the actual write, reconcile keys/counts/probabilities/timestamps/footer and verify prior blocks. A draft or failed verification cannot claim a successful append/ID advance.

In A9 complete the mini's actual checklist (C1–C20 for reference mini-log-7, or the original legacy checklist plus dated compatibility gaps), FR1–FR6, SF-A1–SF-A12 and Q4 calculation checks with specific evidence/status. Return the full new card/addendum or complete non-issued draft, exact path, working ID/status, timing/exposure, all supplied probabilities, supplied-only formal picks or precise no-pick reason, gate/joint/sensitivity/baseline results and updated footer/readback receipt. Explicitly state settlement NOT_PERFORMED, canonical import NOT_PERFORMED, GitHub writes NO and new canonical IDs 0. Make no success guarantee.

---

## REQUIRED RESPONSE AND RETAINED CARD

### R1. Decision block and first selection table

Begin with exact event/participants/competition/endpoint; actual timing/exposure; analysis/write/selection status; supplied counts and coverage. The first **selection** table is the complete supplied ranking. A small identity/reading receipt is not a substitute for that ranking.

| Numeric supplied rank | Raw input # / literal proposition | Contract key / endpoint | p_card (conditional, uncalibrated) | Decisive mass W+L | p_base | BASELINE_P | W / P / L / V; conditioning | Formal eligibility / reason | Principal failure route / evidence quality |
|---|---|---|---|---|---|---|---|---|---|
| <1 or UNPRICED> | <exact user text / raw indices> | <key / endpoint> | <number or NOT_ESTIMATED: reason> | <...> | <...> | <...> | <masses or explicit limit> | <...> | <...> |

Every distinct supplied proposition appears once; all repeated raw inputs map to it through R3/A2. Numeric rows sort on unrounded p; unsupported rows retain input order and no fabricated numeric rank. Above-ceiling rows retain their true p and exclusion reason. Add numerical precision/line-difficulty fields in A5 if the decision table would become unwieldy.

### R2. Frozen formal supplied-only rows

| Formal rank | Literal supplied proposition / key | p_card | Role | Eligibility / gate or floor | Line distance / z | Main failure mechanism |
|---|---|---|---|---|---|---|
| <1, if eligible> | <exact supplied text> | <...> | PICK | <...> | <...> | <...> |
| <2, if eligible> | <exact supplied text> | <...> | PICK | <...> | <...> | <...> |
| <3–4, if available> | <exact supplied text> | <...> | INFORMATIONAL | <...> | <...> | <...> |

Print only actual supported eligible rows. With none, state `NO_ELIGIBLE_PRIMARY:<reason>` and retain R1; with one, do not populate Rank 2. Explicitly flag failed general floors/gates without silently deleting otherwise eligible rows. Give the complete eligible-universe competitor, family tests, precision, exact/bounded joint loss, both-decisive denominator if computed and mechanical-protection status.

Supplemental sporting conclusion: winner/draw/tie probabilities at the exact endpoint where supported, expected score/total/margin/SD/covariance, key conditions, lineup status, form coverage, baseline coverage and sensitivity. Winner is supplemental unless actually supplied. Expected score is a model mean, not a promised or most-likely exact final score. Use calibrated wording only if that exact scope/artifact is verified.

### R3. Frozen raw ledger and A1–A9 appendix

| Raw input # | Verbatim supplied text | Resolved key / provisional unresolved ID | Duplicate of | Period / endpoint / action convention | Definition status | Data/model availability |
|---|---|---|---|---|---|---|
| <1> | <literal> | <...> | <NONE or raw index> | <...> | <...> | <supported or missing reason> |

Use the mini's actual template. For the reference v11 mapping retain:

| Appendix | Contents |
|---|---|
| A1 | Identity/aliases, official state, all times, cutoff revisions and outcome exposure |
| A2 | Literal raw ledger, key schema, dedup mapping, frozen universe manifest and candidate recipe |
| A3 | Evidence/source receipts, known-at/lineage, inspected archives, A3-FORM tables/trace and A3-LINEUPS |
| A4 | Executed model/parameters, normalization/tails, score arithmetic, scenario mixture, baseline and window sensitivities |
| A5 | Every supplied row's W/P/L/V/p/conditioning, full ranking, eligibility, line difficulty and separate declared shadow universe |
| A6 | Regime/adjustment table, before/after parameters, source/assumption basis, unadjusted distribution/pair and overlap checks |
| A7 | Family gates, supplied-scope gate, precision, dependence/complements, lineup/window flags and actual shadow records |
| A8 | Source failures/conflicts, exact unresolved fields, capture/refresh tasks, owner/trigger/due time and job state |
| A9 | Applicable mini checklist, FR1–FR6, SF-A1–SF-A12, Q4 results, real custody/readback verification |

Each decisive evidence row includes claim, field/value/short extract, URL or local source path, source publication/update time if known, retrieval time, collector lineage or `UNKNOWN`, availability status and evidence ID. Repeated domains are not independent collectors. Record conflicting values and the unresolved effect; do not choose whichever value gives a preferred forecast.

Every unresolved task names its exact field/source, affected row or calculation, owner, trigger, ISO due time if real, and `NOT_SCHEDULED` unless an actual job exists. A future capture plan is not a receipt for evidence already retained. Do not invent a job ID, automatic update or promised review.

### R4. Reconciliation and coverage receipt

```text
Raw supplied inputs: <n>
Distinct resolved supplied keys: <n>; unresolved provisional rows: <n>
Duplicate raw occurrences: <n>
Numeric supplied rows: <n>; unpriced supplied rows: <n>
Numeric supplied exclusions: <by actual reason>
Formal numeric rows: <0–4>; primary PICK rows: <0–2>
Baseline coverage — all numeric supplied rows: <n>/<n>
Baseline coverage — numeric formal rows: <n>/<n>
Known-at / metric / lineup / evidence limitations:
Supplied-scope gate / published-policy shadow gate:
Joint loss: <exact / bounded / unavailable; conditioning>
Current mini format / working ID / writer / lease / freeze state:
Exact paths written: <actual paths or NONE>
Prior issued blocks preserved: <actual check or NOT_VERIFIED>
Readback: <actual result or NOT_PERFORMED>
Footer: <actual updated totals or proposed draft totals, clearly labelled>
```

Counts must reconcile without treating unresolved provisional rows as deduplicated known contracts. Numeric exclusions are a subset of numeric rows, not additional inputs. Baseline coverage is computed, not asserted from the existence of a league profile.

### R5. Final operational footer

```text
Prompt revision: SF-2
Selection policy: SUPPLIED_FIRST_V1 — local supplied-only override
Authority: PUBLISHED_MAIN_PINNED <actual verified full SHA, or NOT_VERIFIED>
Primary universe: exact user-supplied contracts ONLY
Derived/main-policy/shadow ranks: NOT_PRIMARY
Write / analysis / timing / exposure / selection status: <separate actual values>
Probabilities: UNCALIBRATED_ANALYST_SCENARIO unless exact qualification verified
Model performance: NOT_CERTIFIED unless exact independent evidence verified
Settlement: NOT_PERFORMED
Canonical import: NOT_PERFORMED; policy recognition required for later import
GitHub main writes: NO
New canonical IDs consumed: 0
```

### R6. Revision and preservation register

This edition preserves all ten extended sport sections and their seven-step workflows; supplied-only primary ranking; complete literal input coverage; L5/L10/L15/L20 research; source/lineage and archive checks; official lineup investigation; no odds; coherent score/phase/player distributions; fixed same-line baselines; sensitivity; append-only originals; local/canonical separation; writer/ID continuity; late continuation and honest outcome-exposure separation.

It clarifies instruction precedence; present-version discovery; separate status dimensions; event versus metric denominators; mixture-before-conditioning arithmetic; conditional p versus outright W; unknown void/action conditioning; quarter/split-line limits; hard eligibility versus diagnostic floors; Rank-1-only family filters; numerical ties and boundaries; coherent sport-specific endpoint construction; concurrent append/readback verification; and per-row future training eligibility. Historical/season-specific rule examples are replaced with explicit verification requirements. Markdown escapes/fences and inactive input placeholders are repaired.

These changes improve prompt clarity, reproducibility and evaluation discipline. They do not themselves establish better forecast accuracy, calibration, physical/source truth or an implemented trained model. Earlier issued cards remain governed by their original frozen policy, probabilities, definitions, timestamps and format.
