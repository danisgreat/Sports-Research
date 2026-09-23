# Audit changes, instructions and implementation record — September 5, 2026

**Current method: MDS-2026.09.05-v3.6.** This Markdown record consolidates the settlement sweep, adopted learnings, rule amendments and subsequent user-confirmed eligibility correction. Original forecast text/ranks are preserved. All substantive decisions are recorded in Markdown; machine-readable files are companions.

## 2026-09-06 addendum — settlement-only performance eligibility

The user's instruction:

> change the performance elgible rule to any log that has been settled being able to be counted for it

**Implemented as `PERFORMANCE_ELIGIBILITY_POLICY.md` `EP-2026.09.06-v2` and `LEARNING_REGISTER.md` L-078.** Performance eligibility no longer depends on pre-game/live-issued issuance horizon, local-import timing, or git/local-timestamp provenance (`E1-Q-LATE_IMPORT`). The sole gate is now whether a row has reached a final, graded result. This is a strictly broader rule than the 2026-09-05 `USER_CONFIRMED_PREGAME_FREEZE` correction below: that correction reached "eligible" for non-live cards through a pre-game-freeze provenance argument but still excluded `LIVE_ISSUED` cards as a `SEPARATE LIVE COHORT`; the 2026-09-06 directive removes that exclusion unconditionally for any settled row.

**What changed, file by file:**

| File | Change |
|---|---|
| `PERFORMANCE_ELIGIBILITY_POLICY.md` | New controlling section added above the retained 2026-09-05 text; version bumped to `EP-2026.09.06-v2` |
| `RULES_GENERAL.md` | New "September 6 user directive" section added before the September 5 section; §12 O/U diagnostic language updated |
| `PREDICTION_LOG_COMBINED_2.md` | Snapshot table's "Clean-unit count toward that checkpoint" field replaced with a performance-eligibility field pointing to the new policy; item 6 of "How this file is used" updated; three historical "not performance-eligible"/"non-performance-eligible" statements (P-272–P-279 and P-280–P-293 component-import sections, plus the P-294–P-305 fingerprint table) corrected in place with dated notes, original text retained |
| `PREDICTION_LOG_COMBINED.md` | One new controlling correction note added at the top of the closed archive, superseding every `E1-Q-LATE_IMPORT`/"not prospective performance evidence" exclusion-of-eligibility statement in the ~70,000-line file without editing each one individually; underlying provenance facts (hashes, first-demonstrable times) are untouched |
| `LEARNING_REGISTER.md` | New L-078 promoted-process entry; new "2026-09-06 audit disposition" section; two existing `P-272`–`P-279`/`P-288`–`P-305` "Eligibility" rows updated with dated notes |
| `GAME_LOG_STATUS_INDEX_2026-09-05.md` | New "USER DIRECTIVE 2026-09-06" block added after the existing freeze-confirmation block |
| `PREGAME_ELIGIBILITY_REGISTER_2026-09-05.md` | New header amendment added; the 294-row table is left as originally written (a full per-row rewrite was judged not worth the risk of transcription error for a change the header amendment already states unconditionally) |
| `README.md` | New directive block added near the top; "Track A — historical qualitative ranking performance" section rewritten to state the settlement-only rule and the ~291-of-306 performance-eligible count; "Track B" (numerical/calibrated-probability eligibility) explicitly noted as unaffected |
| `COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md` | New correction note added after the existing freeze-confirmation block |

**What did not change:** no-forecast/no-action/administrative-closure records still contribute nothing; unresolved/void/partial/evidence-gap rows stay outside the count until graded; process grade and outcome grade remain separately tracked (a process-defective win still counts as a win); no issued forecast, rank or settlement text was rewritten — every correction is an appended, dated note; the numerical model program (`NTS-2026.09.02-v0.3`, Stage 0, no fitted model) and its own `E1-P` shadow-probability cohort are unaffected and remain gated by their own frozen-manifest procedure in `ALGORITHM_PORTFOLIO_AND_EVALUATION.md`/`NUMERICAL_TRAINING_SPEC.md`; candidate-to-forecast-weight promotion still requires each candidate's own v2 test manifest per `LEARNING_REGISTER.md` §5. A full recomputation of the all-history performance scorecard across the now-larger eligible pool has not been performed in this pass — it is a mechanical aggregation task noted as outstanding in `LEARNING_REGISTER.md`'s 2026-09-06 disposition, not assumed here.

## User instructions and controlling correction

The user first requested a comprehensive settlement and retrospective sweep, with live events deferred at their first check, all settled/pending IDs listed, deep investigation of failed #1/#2 picks, attention to successful mechanisms and preferred over/under choices, reliable sources, sport-specific rule updates and general lessons recorded in the existing documents.

The later clarification supersedes the initial instruction to keep blanket non-performance-eligibility:

> all the game logs except for the ones labelled "live" are strictly pre-game frozen, so implement the improvements accordingly

The final recording instruction is:

> i need all the audit changes and updates and learnings and rule changes and instructions and logs to be logged into the md documents,

**Standing user instruction:** all audit changes, updates, learnings, rule changes, instructions and logs must be recorded in the Markdown documents. The `.md` set is the complete human-readable authority. Scripts, JSON and CSV are validation/data companions, not the only record of a decision.

For each future change, update the active prediction log, the specific sport rule document or RULES_GENERAL for cross-sport controls, LEARNING_REGISTER for disposition, and relevant method/source/workflow documents in the same pass. Append a dated, source-linked retrospective with original ranks, results, what went right/wrong, knowability, prior lessons and the exact adopted change. Record pending fields and live-at-first-check deferrals in the active queue. Preserve original issued cards and label superseding corrections. Document validation and link the changed Markdown files in the audit change log before delivery.

Freeze confirmation was recorded at **2026-09-05T05:39:53.956324+00:00**. Provenance basis: **USER_CONFIRMED_PREGAME_FREEZE**. This is the time the confirmation was recorded, not an invented historical forecast timestamp. [Full controlling policy](PERFORMANCE_ELIGIBILITY_POLICY.md).

## Completed settlement work

| Item | Recorded result / scope | Complete Markdown record |
|---|---|---|
| Mini-log intake | Raw 229,310-byte source imported before research; SHA-256 1a362414ca1274c5f405d76e81079acbb9a49fa319bb5251119a14f8f95f0e35; original ranks retained | [Active combined log](PREDICTION_LOG_COMBINED_2.md) |
| Identity repair | Geelong's source-local P-272 retained as LOCAL-GEELONG-20260904; canonical P-272 Osaka–Siniakova untouched; P-283 final pre-game toss refresh counted once | [Audit intake and tables](COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md) |
| Newly settled events | LOCAL-GEELONG-20260904, P-280, P-281, P-282, P-283, P-284, P-285, P-286, P-287, P-289 | [Exact rank/contract/outcome/process tables and detailed retrospectives](COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md) |
| Ten-card historical pre-game performance | #1: 4/10; #2: 4/10; both top two: 0/10; winner annotations: 6/10. Preferred O/U: 3/10 events, or 4/12 distinct total/phase targets. Include process-defective outcomes | [Corrected audit](COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md) |
| Complement geometry | 20 WIN / 20 LOSS across 40 supplied rows is mechanically forced by two complementary pairs per completed card. It does not demonstrate useful total-direction selection | [Audit explanation and arithmetic](COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md) |
| Older settled fields | P-233–P-235: twelve goal/half rows upgraded, 7 WIN / 5 LOSS; three corner rows remain provisional | [China FA Cup review and source records](COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md) |
| First-check live deferrals | P-288, P-290, P-291, P-292, P-293. These are user-confirmed pre-game forecasts awaiting final settlement; their live status was observed during the sweep | [Deferred queue and sources](COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md) |
| Evidence/action follow-ups | P-126, P-148, P-149, P-151, P-166, P-176, P-178, P-179, P-200, P-217, P-233, P-234, P-235, P-273, P-274. Each remains open only for its stated field/action requirement | [Detailed remaining requirements](COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md) |
| Every historical ID | P-001–P-293 and the separate Geelong record; administrative closures, partial fields and live deferrals distinguished | [Full status list](GAME_LOG_STATUS_INDEX_2026-09-05.md) and [eligibility register](PREGAME_ELIGIBILITY_REGISTER_2026-09-05.md) |

## Adopted learnings and rule changes

| Lesson / status | Exact implemented change | Governing Markdown documents |
|---|---|---|
| L-068 — ACTIVE / PROMOTED_PROCESS | Independently compute native-score totals, signed margins and every illustrative contract outcome. Correct the false tennis assumption that a positive games handicap covers every match win; derive set count, games total and games margin jointly | [General rules](RULES_GENERAL.md), [tennis rules](RULES_TENNIS.md), [learning register](LEARNING_REGISTER.md) |
| L-069 — ACTIVE / PROMOTED_PROCESS | Refresh final teams and actual phase-specific roles; carry failed role/XI checks and LOW caps through the final rank table; timestamp late news and retain unknown knowability | [General rules](RULES_GENERAL.md), [NRL](RULES_NRL_RUGBY.md), [cricket](RULES_CRICKET.md), [AFL](RULES_AFL.md) |
| L-070 — ACTIVE / PROMOTED_PROCESS | Make each competitor's supported winning/separation scenarios contract-evaluable; propagate phase resources; include early-Over/full-Under and early-Under/full-Over where supported | [General](RULES_GENERAL.md), [baseball](RULES_BASEBALL.md), [cricket](RULES_CRICKET.md), [basketball](RULES_BASKETBALL.md), [AFL](RULES_AFL.md) |
| L-071 — ACTIVE / PROMOTED_PROCESS | Qualify event IDs by host, participants and date; preserve definitions for legal balls versus delivery ordinals, efficiency versus points, scoring shots versus attempts, and final-score fields | [Source register](DATA_SOURCE_REGISTER.md), [general rules](RULES_GENERAL.md), relevant sport rules |
| L-064 — NARROWED | Replace automatic knockout-scoring suppression with competition/round/leg/aggregate-specific evidence; separate red-card and post-goal regimes from the pre-game baseline | [Soccer rules](RULES_SOCCER.md), [learning register](LEARNING_REGISTER.md) |
| L-072 — ACTIVE_PROCESS; L-022 narrowed | Accept user-confirmed frozen pre-game history. Remove blanket late-import exclusions. Separate issue horizon, later event state, provenance basis and endpoint settlement | [Eligibility policy](PERFORMANCE_ELIGIBILITY_POLICY.md), [general rules](RULES_GENERAL.md), [model specification](MODEL_AND_DATA_SPEC.md), [learning register](LEARNING_REGISTER.md) |
| L-028 — NARROWED | Keep identifiable issued process-defective wins and losses in headline historical ranking results; show compliance separately. Do not improve results by deleting mistakes retrospectively | [General rules](RULES_GENERAL.md), [evaluation protocol](ALGORITHM_PORTFOLIO_AND_EVALUATION.md), [learning register](LEARNING_REGISTER.md) |
| Preferred O/U and top-two review — ACTIVE | Record the preferred direction per exact total/phase target; test strongest supported #1/#2 failure paths and joint compatibility; retain marginal-likelihood ranking without inserting opposites merely to manufacture coverage | All sport-rule implementation amendments and [operational guide](UPCOMING_GAME_RESEARCH_GUIDE.md) |

## Sport implementation map

| Sport | Implemented instruction | Markdown authority |
|---|---|---|
| Baseball | Two-sided contact/traffic/error stress, starter-to-bullpen transitions and inherited runners; total support distinct from cushion support | [RULES_BASEBALL.md](RULES_BASEBALL.md) |
| Cricket | Legal-ball/run-resource phase budgets, both early/full total split directions, XI-grade propagation and exact user phase versus regulatory powerplay | [RULES_CRICKET.md](RULES_CRICKET.md), [LEAGUE_RULES_CRICKET.md](LEAGUE_RULES_CRICKET.md) |
| Basketball | Two-team scoring allocation, supported opponent-win branches, rotations and closing-quarter separation; distinguish shooting efficiency from pace | [RULES_BASKETBALL.md](RULES_BASKETBALL.md) |
| AFL / AFLW | Opponent-adjusted opportunity volume versus conversion, two-sided final-quarter allocation, conditions and final warm-up roles; separate competitions | [RULES_AFL.md](RULES_AFL.md) |
| NRL | Actual roles/entry minutes after final team changes, and joint favourite-margin/opponent-scoring budgets | [RULES_NRL_RUGBY.md](RULES_NRL_RUGBY.md) |
| Tennis | Exact set-to-game arithmetic; joint winner, set count, games total and signed handicap; no automatic close/long or fatigue direction | [RULES_TENNIS.md](RULES_TENNIS.md) |
| Soccer | Competition-specific knockout baseline, opponent-win scenarios and field-defined corners; adequately sourced settlement fields | [RULES_SOCCER.md](RULES_SOCCER.md) |
| Ice hockey | Regulation versus overtime/shootout endpoints and contract-specific operator follow-ups | [RULES_ICE_HOCKEY.md](RULES_ICE_HOCKEY.md) |
| American football | Shared role/exposure, native-score, drive/possession and two-sided separation checks; no new sport-specific coefficient inferred | [RULES_AMERICAN_FOOTBALL.md](RULES_AMERICAN_FOOTBALL.md) |
| Rugby union | Shared role/exposure, native-score, territory/kicking/discipline and separation checks; no new sport-specific coefficient inferred | [RULES_RUGBY_UNION.md](RULES_RUGBY_UNION.md) |

## Source and pre-game error corrections

The detailed audit contains the source URLs, published/observed timing where captured, conflicting values and limits for every settled event. The source register now includes field-specific use of NRL final-team previews, official CPBL boxes and native-language reports, ETPL-linked NV Play, NDTV phase comparison, FIBA official fields, AFL host-qualified match IDs, US Open set/stat records and original Xinhua/Titan reporting. A stale page or mirrored scoring feed is not a second independent source. Unverified corners and operator terms remain explicit follow-ups. [Full research-source register](COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md#research-source-register) · [standing source instructions](DATA_SOURCE_REGISTER.md).

The per-game retrospectives retain both successful and failed mechanisms and distinguish known-at mistakes from unverified knowability. They address the Roosters final-team/role failure, both CPBL total failures, South Africa's correct early Over and failed full Under, USA/China's correct total but failed cushion, Korea/Nigeria's omitted opponent-win branch, Belfast's late acceleration after an early Under, tennis score/handicap errors, and AFL/AFLW volume/conversion and final-quarter errors. Earlier applicable lesson IDs are linked in those sections; original forecasts are not rewritten.

## Performance use, tests and remaining limitations

The existing non-live history is eligible for historical directional/ranking evaluation on the user-confirmed basis. The ten recent cards have complete original-rank/result joins and now count under their issued v3.4 method. This correction does not claim to have recomputed every earlier method's aggregate performance; those require original pre-game views, aliases and partial endpoints to be joined. The complete per-ID eligibility register applies the correction throughout the history.

L-068–L-071 and the sport implementations are active process controls. C-P293-BB-CLUSTERS, CR-RESOURCES, BK-ALLOCATION, AFL-VOLUME, NRL-ROLE and TEN-ALLOCATION remain candidate numerical comparisons. Existing T-P275-RECOVERY-LENGTH remains separate. Their later-test counts are zero because no executed frozen comparator has accrued later cases; that is not a claim that historical pre-game eligibility is zero. No fitted model, new probability, calibration, numerical weight or measured improvement is claimed. [Learning/test register](LEARNING_REGISTER.md) · [numerical model state](NUMERICAL_MODEL_REGISTER.md).

## Validation and preservation

Validation covers the original Downloads/component hash, byte-exact embedded new and older raw components, original ranks and outcomes, signed settlement calculations, phase/inning/quarter/set sums, full canonical ID sequence, deferred-event exclusion from settlement, corrected pre-game/live eligibility, process-failure inclusion, active rule versions and Markdown table structure. [Current Markdown validation results](audit_2026-09-05/VALIDATION.md).

Original source components remain unchanged; dated superseding notices control eligibility while preserving historical statements. Before-edit copies are retained under audit_2026-09-05. The scripts and JSON/CSV files support inspection and reproduction; no substantive instruction or decision depends on reading them.
