# Selection, baseline and settlement rules

**SEL-2026.10.11-v2 · primary policy P_ORDER_V2.** Numerical thresholds are PROVISIONAL, not proven accuracy guarantees. Applies to new v10 cards; old selections keep their original policy. [CURRENT_RULES](CURRENT_RULES.md) controls.

## 1. Constants and scope

| Item | Rule |
|---|---|
| Ranked numeric candidates | At most four supported rows; do not pad |
| Selection ceiling | p_card ≤ 0.90; retain true higher values outside the selected slate, never clip |
| Rank-1 gate | p_card ≥ 0.62 and lead ≥ 0.04 over best eligible non-complementary alternative |
| Rank-2 floor | 0.58, disclosed if unmet; no invented replacement |
| Joint failure | Report 0.30 target / 0.35 warning as historical provisional diagnostics, not a forced reordering rule |
| Large adjustment | Above 0.25 SD; any size that changes top two is ADJUSTMENT_DEPENDENT |
| Decision block | At most about 650 words, full evidence in appendix |
| Review target | Within 72 h of verified final; unknown final time is disclosed |
| Open event alert | More than five pending events; evidence backlog separately counted |
| Fragile-field capture | Normally within 36 h after scheduled start; real delays/multi-day events need explicit revised due time |

## 2. Primary order and Rank-1 gate

Freeze the candidate recipe and eligibility rules before pricing. Each contract key comprises quantity, participant orientation, line, direction, period, endpoint and action/void convention. Deduplicate identical keys. Rank numeric eligible rows by unrounded p_card descending; ties use ascending contract key. Retain the first four or fewer. Rank 1/2 are the primary picks; the rest are informational. A qualitative slate uses explained qualitative order, no numerical PASS, no numeric proper score.

Family rules apply to eligibility for the primary slate when they would prohibit its top row: remove the inadmissible would-be Rank 1 from primary selection, record its reason and keep it in the diagnostic ladder; repeat on the remaining set. Do not quietly demote it below a lower-p row in a table claimed to be probability-sorted. Unsupported rows are excluded independently of whether they would win.

Compute the original gate against the best non-complementary alternative in the full eligible priced universe, not just the displayed four. An exact opposite on the same line is complementary; another threshold on the same quantity is still an alternative. If no alternative exists, gate = NOT_ASSESSABLE. Print Rank-1 p, alternative key/p, gap, numerical floor result and PASS/RANK1_UNSTABLE. Do not round before comparing or remove competitors to manufacture a pass.

Also freeze `SHADOW_GATE_RET03`: exclude other lines on Rank 1's quantity, keep 0.62 and 0.04, and print the alternative and result or NOT_ASSESSABLE. It does not replace the original gate or enter its cohort. Equal and nearby tail probabilities can keep the gate unstable; this is an observed property, not permission to tune constants after seeing outcomes.

<a id="3-rank-2-and-the-joint-failure-probability"></a>

## 3. Rank 2, dependence and shadows

Primary Rank 2 is the second row in probability order. Report floor failure and dependence without changing the primary order. This resolves the v9 conflict between probability ordering and minimising joint failure; label the policy change on every new card.

Quantity keys identify the underlying random variable and endpoint: full match total; signed full margin (winner and either team's handicap share this quantity); each named team total; each phase total; each player's count. Merely reversing a margin sign or renaming a family does not create a different quantity.

Freeze two diagnostics when supported: (a) `SHADOW_R2_RET04`, highest-p eligible row with p≥0.58 on a different quantity from Rank 1; (b) `SHADOW_R2_XCARD6`, eligible remaining row with p≥0.58 minimising exact joint failure, ties by p then contract key. Report NONE when unavailable. They are never counted as primary wins. Different quantities can still be structurally dependent; evaluate actual losing sets.

For unconditional losing masses l1 and l2, exact joint = sum of common losing states from a shared model. For nested loss sets use min(l1,l2); for disjoint sets use 0 and label MECHANICALLY_PROTECTED. Otherwise, absent a computed joint, show Fréchet bounds `[max(0,l1+l2−1), min(l1,l2)]`, not a point estimate. Never multiply without justified conditional independence. Use W/P/L/V unconditional masses, not 1−p_card when pushes/voids exist. Record P(both decisive) where conditional comparison is required. Exact, bounded and unavailable joints remain separate in retrospective tables.

## 4. Family checks

| Family | Required support |
|---|---|
| Soccer first-half Over 0.5 at Rank 1 | Half-specific rate/model, p≥0.72 and 5-point lead over best eligible alternative; full-time intensity alone is insufficient |
| Baseball +1.5 at Rank 1 | p≥0.65, signed team-specific P(win)+P(lose by exactly one), with ties/actions treated explicitly |
| Tennis games | Reproducible point/set/match construction and supported match-form mixture; disclose approximation and deciding-set sensitivity; no invented exact enumeration |
| Corners | Named provider, supported count distribution and field definition; cross-score joint requires a joint model |
| Period/player rows | Exact phase/player definition, source field and capture plan; no inferred period score from match final |
| Unknown league/format | Explicit local evidence/prior and limitations; no silent transfer of NBA/NHL/MLB or another competition's rules |

Old league-wide absolute-margin or one-run rates are sanity checks, never a particular team's directional probability or universal ceiling. Older sport-file instructions that conflict with these controls are historical.

## 5. Candidate universe

Default recipe: supported supplied lines, winner/draw/double chance as appropriate, plus supported handicap, total, team-total and period families on the sport's declared standard ladder. State each quantity's line range/step before pricing; legacy default spans ±2.5 SD (cricket ±2 SD), half lines, with integer lines only when pushes are defined. Record the actual enumerated set; if only a subset can be computed, label PARTIAL_UNIVERSE and the gate as restricted-universe diagnostic.

Do not claim an exhaustive search from four hand-picked rows. Keep unselected supplied rows and relevant neighbouring lines. Analyst-derived lines may be easy by construction; report their p level, line distance from centre and baseline p. Neither a high hit rate nor zero joint failure proves a useful prediction. Baseline and candidate are scored at the exact same frozen lines.

## 6. Regimes and sensitivities

Use NONE, FINALS_COMPRESSION, EARLY_SEASON, CUP_ROTATION or RULE_CHANGE:<verified name>. Other context is prose, not an invented operative flag. Read current [BASE_RATES_REGISTER](BASE_RATES_REGISTER.md); use only a supported recommended multiplier in the matching league/era, once. A recommended 1.000 means no shift. Missing/unmeasured effects are scenarios with disclosed basis, never fabricated measured multipliers. Some named finals regimes increase scoring; do not assume every final compresses it.

Log adjustment target, before/after parameter, units/SD basis, source, analyst-versus-archive basis and overlap with other terms. Any top-two flip produces ADJUSTMENT_DEPENDENT. Publish the unadjusted pair, sensitivity probabilities and which assumptions drive the choice. Missing SD prevents an SD-size claim; it does not hide a rank flip.

## 7. Grades, evidence and queues

Grades: WIN, LOSS, PUSH, VOID, UNRESOLVED. VOID is a verified frozen void rule, never a synonym for no data. Card states: SETTLED, PARTIALLY_SETTLED, PENDING_EVENT, UNRESOLVED_EVIDENCE, NO_FORECAST. A cancelled event may be terminal with VOID rows under a frozen rule; unknown event state stays pending with uncertainty.

| Evidence | Meaning |
|---|---|
| A | Official field-owner terminal record for the exact target |
| B | Structured provider or supported agreement, with provenance/lineage disclosed |
| C | Single secondary/provisional evidence; limitations and conflicts retained |
| E | Valid bound on a partly observed value; definite grade only if the entire feasible set agrees |
| X | No sufficient evidence; UNRESOLVED |

Definition status is separate: OPERATOR_VERIFIED, FROZEN_FRAMEWORK_CONVENTION, UNKNOWN_DEFINITION or N/A. Retain legacy OP as a historical evidence label. Never apply a newly invented default after the result. Conflicting material sources cannot be adopted merely to close a record; record both and the unresolved field. Corrections carry original grade, new grade, source and reason.

## 8. Failure classes

Retain the legacy classes: FIRST_HALF_GOAL_OVERSELECTION, RUNLINE_CUSHION_CEILING, BASKETBALL_TOTAL_WITHOUT_PACE_MODEL, TENNIS_IID_UNDERDISPERSION, RANK_BY_Q_NOT_P, SHARED_DRIVER_TOP_TWO, HANDICAP_TAIL_OVERREACH, SMALL_SAMPLE_STRENGTH_OVERREACH, PHASE_INCOHERENCE, CORNER_ROW_WITHOUT_PROVIDER_OR_NB_MODEL, OVERCONFIDENT_PROBABILITY, WEAK_SLATE_FORCED_RANK, QUALITATIVE_RANKS_WITHOUT_DISTRIBUTION, REGIME_IGNORED, UNFITTED_ANALYST_ADJUSTMENT, LATE_INFORMATION, ENDPOINT_OR_CONTRACT, SOURCE_OR_IDENTITY, VARIANCE and OTHER.

Use aliases only with a printed mapping. Distinguish a suspected failure from an established error. Honest qualitative research is not itself misconduct; QUALITATIVE_RANKS_WITHOUT_DISTRIBUTION means numerical confidence was claimed without the supporting distribution. OVERCONFIDENT_PROBABILITY cannot be inferred solely from one high-p loss. OTHER and NOT_ASSESSABLE need an explanation. Keep multiple process faults without invented causal percentages.

## 9. Frozen league-only baseline (RET-02)

Use `BASELINE_LEAGUE_V1` for the same league, season regime, endpoint, orientation and line, with no team, lineup, recent-form or event-result inputs. Freeze the recipe and source window before the forecast. Prefer a vetted league distribution with all parameters supported; alternatively use a declared prior-only empirical event cohort with literal W/P/L/V counts for that exact line. Do not switch recipes after seeing which comparator is easier to beat.

Document distribution family, means/SDs/dispersion/covariance or empirical counts, seasons, exclusions, home/away orientation, sample size, data last-known time and source. Match the card's push/void conditioning. Empirical baseline p=W/(W+L); if denominator zero, NOT_COMPUTED. A profile with mean and SD alone does not determine a discrete/extras/tennis/phase distribution: unsupported families remain BASELINE_UNAVAILABLE.

Calculate the baseline from its own league-only inputs; do not reuse team-adjusted parameters as a baseline. Print BASELINE_P and its ID on every numeric row or a precise missing reason. A stale profile is labelled and tested, not silently refreshed with post-cutoff games. No historical backfilled baseline enters prospective paired evaluation.
