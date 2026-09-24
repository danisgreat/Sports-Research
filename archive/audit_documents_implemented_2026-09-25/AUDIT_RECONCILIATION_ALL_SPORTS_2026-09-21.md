# All-sports audit reconciliation and implementation ledger — 2026-09-21

Status: **CURRENT RECONCILIATION RECEIPT — CR-2026.09.21-2**  
Method semantics: **MDS-2026.09.19-v4.3** (unchanged)  
Scope: historical methodology, settlement, blind-spot, source, model and implementation audits across every supported sport through 2026-09-21.

## 1. Purpose and precedence rule

This ledger prevents an older audit finding from being reintroduced after a later audit has disproved, narrowed or superseded it. Audit date alone is not enough to control. For every finding, use this order:

1. **REJECTED / INCORRECT** — evidence later showed the premise or arithmetic was wrong. Never apply it.
2. **SUPERSEDED / NARROWED** — a later rule replaces or limits it. Apply only the later rule.
3. **ACTIVE / RETAINED** — still compatible with the current method and evidence; keep it.
4. **ALREADY IMPLEMENTED / DUPLICATE** — do not restate it as a new rule or double-weight it.
5. **EMPIRICAL WORK REQUIRED** — do not convert a research task into prose-only “implementation.” It remains pending until the required dataset/test exists.

Historical issued cards and audit documents remain evidence. They do not override the current authority files. A single retrospective result never creates a coefficient, probability cap, directional bias, rebound/hangover rule or ranking adjustment.

## 2. Cross-audit disposition

| Audit lineage / finding | Current disposition | Controlling implementation |
|---|---|---|
| 2026-07 methodology audit: retire custom top/bottom penalty scoring; use proper outcome scoring and event-clustered evaluation | **ACTIVE / RETAINED** | `SCORING_AND_VALIDATION.md`; current score/evaluation protocol |
| 2026-07 methodology audit: immutable cutoff-safe snapshots, explicit forecast mode/version and source timing | **ACTIVE / RETAINED** | `METHOD.md`, `RULES_GENERAL.md`, `CONTROLS.md`, `PF-3 KNOWN-AT` |
| 2026-07 methodology audit: precise probabilities require reproducible fitted/calibrated artifacts; otherwise do not invent precision | **ACTIVE / RETAINED** | `METHOD.md`, `NUMERICAL_PROGRAM.md`, `H0_DATASET_CARD.md`; current state remains no fitted champion |
| 2026-07 methodology audit: fact-specific source hierarchy rather than brand-first/StatMuse-first retrieval | **ACTIVE / RETAINED** | `SOURCES.md`, `DATA_SOURCE_REGISTER.md` |
| 2026-07 settlement audits: prices/odds may not be required for directional research or grading; missing price is not a reason to fabricate an ungraded outcome | **ACTIVE, NARROWED** | Market data remains quarantined metadata. Exact operator-specific action/void terms are still separate from research arithmetic. |
| 2026-07 settlement audit: `UNORDERED PAIR` for hard-to-separate complements | **SUPERSEDED** | Current user-facing workflow requires unique marginal-likelihood ranks for every valid supplied row; use `FORCED RANK / LOW`, not an unranked escape hatch. |
| 2026-07 settlement audit: a bowl-first cricket toss implies low scoring | **REJECTED / INCORRECT** | Toss choice is weak contextual intent only; it is not strip proof or a signed scoring adjustment. |
| 2026-07/08 one-game or tiny-sample directional rules | **SUPERSEDED / NARROWED** | `R-1`, small-sample shrinkage, explicit mechanism and preregistered prospective testing control. |
| 2026-09-05: native-score arithmetic, phase/end-point identity, current participant/role capture, process-vs-outcome separation | **ACTIVE / RETAINED** | `RULES_GENERAL.md`, all sport modules, settlement workflow |
| 2026-09-05 performance-eligibility expansion | **SUPERSEDED for current claims** | 2026-09-12+ controlling state is **LEARNING_ONLY / NOT PERFORMANCE_ELIGIBLE** for current historical logs; no lift claim follows from old eligibility labels. |
| 2026-09-06: ESPN/structured endpoint discovery, field-owner settlement, corners/powerplay source fixes | **ACTIVE / RETAINED** | `SOURCES.md`, `DATA_SOURCE_REGISTER.md`, soccer/cricket modules |
| 2026-09-06 `L-073` premise that corners lacked reproducible field-owner settlement | **REJECTED / SUPERSEDED** | `L-081` and later source registry control; coverage is competition/field specific. |
| 2026-09-06 guaranteed pitch-ladder fallback / assumed venue-history completion | **REJECTED / SUPERSEDED** | Exact current strip may be unavailable; use explicit missingness (`NOT_FOUND_AFTER_SEARCH`, `INSUFFICIENT_VENUE_HISTORY`) and widen uncertainty. |
| 2026-09-06 blind-spot: path counts, “second-highest + median” tail construction, universal 40–60% top-slot bands | **REJECTED / SUPERSEDED** | Use one coherent sport-native distribution and exact PMF/CDF/branch mass. No universal probability/rank ceiling. |
| 2026-09-06 blind-spot: cushion strength forces an underdog winner, tennis winner guarantees modest game handicap | **REJECTED** | Winner, handicap/cushion and total are separate queries of the same joint distribution. |
| 2026-09-06 control-taxonomy retro-tagging backlog | **CLOSED / NOT TO BE DONE** | 2026-09-19 corrected the unit: active controls are classified by consequence; historical lesson rows need not be retro-tagged. |
| 2026-09-09 `G-L7` aggregate-to-disaggregate retrieval | **ACTIVE / RETAINED** | Disaggregated event/participant record must be retrieved before an aggregate carries directional weight. |
| 2026-09-09 `G-L8` probability monotonic in absolute normalized edge across rows | **SUPERSEDED / CORRECTED** | Exact row probability comes from the row's own distribution/PMF/CDF; distance-to-line does not order probabilities across different distributions. |
| 2026-09-09 “at least one side of O/U won” as performance evidence | **REJECTED** | Score the preferred O/U decision and retain both contract rows only as correlated/complementary records. |
| 2026-09-11 mechanism-overlap, exposure, full lineup/bench/coaching, phase/full-total separation | **ACTIVE / RETAINED** | Sport modules + `G14.2`, `G-L10/17/21`, current research guide |
| 2026-09-11 cohort-specific “far-from-centre” or family hit rates as a ranking rule | **NOT PROMOTED / DIAGNOSTIC ONLY** | No permanent weighting without frozen prospective validation. |
| 2026-09-12 exact push/void/censoring arithmetic, dependence/joint bounds, source-accuracy-by-field, process-vs-causal interpretation | **ACTIVE / RETAINED** | `SCORING_AND_VALIDATION.md`, `RULES_GENERAL.md`, `SOURCES.md` |
| 2026-09-17 hard probability ceilings/floors and stale normalized-edge rules | **WITHDRAWN / SUPERSEDED** | Distribution-derived probabilities only when a validated model exists; otherwise no precise internal probability. |
| 2026-09-17 period-bound settlement corrections and event/row denominator split | **ACTIVE / RETAINED** | Settlement and scoring documents; historical corrections remain append-only. |
| 2026-09-17 H0 / A0-A1-first numerical program | **EMPIRICAL WORK REQUIRED** | H0 remains **NOT BUILT / NOT QUALITY-APPROVED**. Documentation cannot substitute for dataset construction, chronological fit/calibration/test and prospective shadow validation. |
| 2026-09-19 `R-1`: recent results revise rates only through a named mechanism; no rebound/hangover/due forecast | **ACTIVE / RETAINED** | `RECENCY_AND_REBOUND.md` + every sport module |
| 2026-09-19 source firewall: no sportsbook/tipster/fantasy/DFS-derived evidence | **ACTIVE / RETAINED** | `SOURCES.md`, `CONTROLS.md`, sport source addenda |
| 2026-09-19 line quarantine: supplied totals/spreads/alternate lines cannot shape the distribution before it is frozen | **ACTIVE / RETAINED** | `PF-2`, `RULES_GENERAL.md`, sport modules |
| 2026-09-19 `known_at <= cutoff_at`, source lineage de-duplication, raw/feature/forecast separation, no ad-hoc centre shifts | **ACTIVE / RETAINED** | `PF-3`, `PF-5`, `PF-8`, `PF-9` |
| 2026-09-19 three independent reliable event lineages, timezone/date rollover, immediate state refresh, three-lineage terminal settlement | **ACTIVE / RETAINED** | CR-4 controls preserved inside CR-2026.09.21-2 |
| 2026-09-19 top-ranked O/U loss **or push** receives the same enhanced retrospective scrutiny as a Rank #1 loss | **ACTIVE / RETAINED** | `METHOD.md`, `SCORING_AND_VALIDATION.md` |
| 2026-09-21 cricket toss/strip audit: separate toss, current strip and match conditions; lineage fingerprinting; stale-official handling; venue-history missingness | **ACTIVE / RETAINED** | `RULES_CRICKET.md`, `SOURCES.md`, `DATA_SOURCE_REGISTER.md`, cricket preflight controls |

## 3. Canonical all-sports controls after reconciliation

The following survive every audit and apply prospectively across sports unless a sport module adds a stricter rule:

1. Verify exact event identity, competition/rules era, venue, local time/timezone, Melbourne conversion and current state before analysis.
2. Use at least three genuinely independent reliable event lineages; syndicated mirrors count once. Search snippets and generated summaries are discovery only.
3. Freeze the complete supplied candidate slate and exact settlement endpoint. Supplied lines are **contract metadata**, not model evidence.
4. Reject betting picks, tipsters, prediction markets, fantasy/DFS projections and downstream analysis derived from them as predictive evidence.
5. Every predictive fact must be cutoff-safe (`known_at <= cutoff_at`) and field-current. Late/final data cannot backfill a pregame feature.
6. Retrieve current participants, starters/lineups, bench/reserves, role/exposure and key absences with missingness made explicit.
7. Prefer field-owning structured/raw evidence; use aggregate summaries only after the disaggregated record has been checked where available.
8. Build one sport-native joint event distribution/corridor before querying totals, lines, cushions and winners. Do not invent independent probabilities for related rows.
9. Model push, void, censoring, extra periods and terminal-state branches explicitly. Complementary rows are not independent decisions.
10. Recent form may change an estimated rate only through a named current mechanism. No bounce-back, hangover, “due”, correction-to-mean or continuation direction is automatic.
11. A single result may expose a process bug or create a testable hypothesis, but cannot create a permanent signed coefficient or ranking override.
12. Enhanced retrospectives are mandatory when Rank #1 or the highest-ranked O/U loses; a push on the highest-ranked O/U also triggers the review.
13. Settlement requires three independent reliable terminal-state/result lineages; any credible live-state conflict blocks settlement.
14. Performance/model promotion requires frozen chronological out-of-sample evidence, calibration where applicable and prospective shadow confirmation. Documentation compliance is not predictive lift.

## 4. Sport-specific retained audit package

| Sport | Retained sport-specific audit implementation | Older finding explicitly not revived |
|---|---|---|
| Baseball | PA/BF exposure, starter hook distribution, named bullpen chain, park/defence, base-out/HR sequencing, home-ninth entitlement, extra-inning state, debut/small-sample mixture | “bad last start means rebound” or “bad recent ERA means continuation”; one-start/one-series deterministic rules |
| Cricket | Legal-ball/resource phase mapping, XI/role continuity, toss/strip/conditions kept separate, exact current-strip evidence, venue-format baseline with missingness, DLS/reduced-overs branches | bowl-first = low score; generic venue history = current strip; automated metadata = observed strip |
| Soccer | regulation/extra-time endpoint, lineup/bench/coaching, shot/xG/process and set-piece/corner state, red-card/post-goal regimes, competition-specific corner settlement | automatic knockout Under, rotation = result reversal, aggregate corners without field-owner/disaggregate check |
| Basketball | possession/opportunity model, minutes/usage mixture, shooting shrinkage/uncertainty, foul/garbage-time/OT tails, spread-total coupling | one hot/cold shooting game as permanent rate shift; generic “competitive game” direction without mechanism |
| AFL/AFLW | scoring-shot/opportunity vs conversion split, role/selection/bench, venue/weather and quarter-state exposure, three-source finality | false-final/state-shell settlement; deterministic conversion regression after one match |
| Rugby league (NRL) | final team/role/bench, possession/field-position/set starts, ruck/play-the-ball and kicking/discipline, weather/venue, golden-point endpoint | named absence widening both teams symmetrically; automatic response/bounce-back |
| Rugby union / sevens | format-specific possession/territory, set-piece, discipline/cards, replacements, goal-kicking and extra-time/tiebreak rules with sparse-evidence widening | importing rugby-league rates or claiming precision from sparse samples |
| American football | drive/play opportunity, QB/OL/skill availability, EPA/success/turnover/field-position branches, pace/game-state, OT/rules era | one-score “due” logic, generic recent score trend as a signed adjustment |
| Ice hockey | confirmed goalie, 5v5 shot/xG process, special teams, score effects, empty-net/OT branch, travel/rest only with mechanism | goalie unknown treated as automatic Over/Under; recent finishing streak as permanent conversion change |
| Tennis | surface/format-specific serve-return state, hold/break tree, set-count mixture, scoreline coherence, retirement endpoint and rating benchmark as a check only | match winner automatically covers games; long match automatically means Over; tiny H2H as deterministic ownership |

## 5. Items deliberately left pending because they are empirical work, not missing prose

- **H0 dataset construction and quality approval.** Still not built/approved.
- **Chronological TRAIN/TUNE/CAL/TEST fitting and one-time held-out test** for authorized numerical candidates.
- **Prospective shadow evidence** before any numerical challenger can be promoted.
- **Non-MLB `R-1` magnitudes.** They remain `NOT_YET_DERIVED`; MLB estimates may not be imported to other sports/leagues.
- **Sport/competition source routes that have not been verified in-session.** Missing coverage is recorded as missingness, not filled with an invented source.
- **Historical documentary/settlement gaps** remain operational queue work and do not create forecast weights.

No file may describe any of these as completed merely because the requirement is documented.

## 6. Control-revision effect

This reconciliation does **not** change the qualitative method semantics and therefore keeps **MDS-2026.09.19-v4.3**. It does materially change the active control/document receipt because the audit precedence and all-sports supersession map are now explicit. The control revision therefore advances to **CR-2026.09.21-2**. Historical cards retain their issued method/control revisions.
