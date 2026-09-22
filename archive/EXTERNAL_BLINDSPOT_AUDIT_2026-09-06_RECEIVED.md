<!-- PROVENANCE HEADER — added by this repository on receipt, 2026-09-06. Everything below the horizontal rule is the externally supplied document, preserved as received. -->

# Received document: external blindspot audit (Google Drive read-only pass)

**Received:** 2026-09-06, pasted into conversation by the user.
**Original filename (as supplied):** `SPORTS_RESEARCH_FULL_BLINDSPOT_AUDIT_P001_P305_2026-09-06.md`
**Producing session:** a separate session operating in Google Drive READ-ONLY mode against a Drive snapshot of this repository, using **no external web research** — an internal-record audit only, distinct from the live-web settlement work this repository's own sessions perform.
**Disposition:** the fifteen blindspots (`B-01`–`B-15`) it identifies are extracted and dispositioned in `LEARNING_REGISTER.md` §"2026-09-06(c) external blindspot audit disposition", with resulting rule changes in `RULES_GENERAL.md` §14, `PERFORMANCE_ELIGIBILITY_POLICY.md`, `AGENT_ROLE_AND_TASK.md` and `UPCOMING_GAME_RESEARCH_GUIDE.md`. This file preserves the received document itself as source evidence, per the standing practice of preserving supplied external content rather than only summarising it.

## Known discrepancy with this repository's own canonical state — read before using this document as a settlement reference

This document's cohort table, executive conclusion and event-by-event appendix all state that **`P-304` and `P-305` were still live/deferred** in the Drive snapshot it reviewed, and explicitly exclude them from outcome-based conclusions on that basis. **That is no longer this repository's canonical state.** In this repository's own 2026-09-06 settlement pass (`PREDICTION_LOG_COMBINED_2.md` §"2026-09-06 — settlement, evidence-gap closure and the v3.7 algorithm patch", predating receipt of this document), both cards were settled: `P-304`'s Rank #1 (`1st Half Over 0.5 goals`) **WON**, and `P-305`'s Rank #1 (`Flames PP Over 51.5`) **WON**; both potential-winner calls were **CORRECT**. Rows #2–#5 of both cards remain `UNGRADABLE / ARCHIVAL_OMISSION` per `L-086`. This is not a contradiction requiring correction of either document — it reflects the two sessions working from snapshots taken at different times, exactly as `RULES_GENERAL.md`'s provenance controls anticipate. This document's own findings about the *four evidence-closure cards* (`P-151`, `P-273`, `P-300`, `P-302`) and its broader governance analysis (`B-01`–`B-15`) are unaffected by this discrepancy and are dispositioned on their own merits below.

## Character-encoding note

The received text contains character-encoding corruption consistent with UTF-8 content having passed through at least one non-UTF-8-aware decoding step before reaching this repository — visible as a bare "â" standing in for an em dash in many places, and two-character sequences such as "Ã©", "Ã³", "Ã¸" standing in for accented Latin characters (é, ó, ø) in non-English names and terms. **This is preserved exactly as received rather than algorithmically "corrected", because a confident, verified byte-level reversal was not available and an incorrect guess would silently introduce fabricated text into an evidentiary record.** Where a corrupted name or word is unclear, cross-check the entity against the corresponding canonical card in `PREDICTION_LOG_COMBINED.md` / `PREDICTION_LOG_COMBINED_2.md` rather than trusting this file's rendering.

---

# Sports Research – Full Game-Log, Results, Retrospective & Rules Blindspot Audit

**Audit date:** 2026-09-06 (Australia/Melbourne)
**Drive mode:** READ-ONLY. No Google Drive file was edited, renamed, moved, commented on, or rewritten.
**Output:** separate local Markdown audit only.
**Canonical event coverage:** P-001 through P-305. P-304 and P-305 were still live/deferred in the latest reviewed Drive settlement snapshot, so they have no final outcome retrospective in this audit. *(See the discrepancy note above — this repository's own record has since settled both.)*

---

## 1. Scope and audit method

This audit uses the canonical combined archives as the event spine, then cross-checks them against the status index, comprehensive retrospectives/settlement audits, the learning register, the current general rules, every represented sport rulebook, and the model/evaluation governance documents. The purpose is not to re-predict old games. It is to determine whether the historical failure modes are (a) already closed by current rules, (b) still recurring because of implementation drift, or (c) genuine rule/governance blindspots.

### Controlling source set reviewed

- `PREDICTION_LOG_COMBINED.md` – closed canonical archive through P-271.
- `PREDICTION_LOG_COMBINED_2.md` – active canonical continuation P-272 onward, through P-305 in the reviewed snapshot.
- `GAME_LOG_STATUS_INDEX_2026-09-05.md` – one row for every canonical P-001–P-305.
- `COMPREHENSIVE_RETROSPECTIVE_2026-08-22.md` – P-001–P-060 event-by-event retrospective.
- `COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-02.md` and `COMPREHENSIVE_SETTLEMENT_AUDIT_2026-09-05.md` – later settlement/process audits.
- `LEARNING_REGISTER.md`, `RULES_GENERAL.md`, all represented `RULES_<SPORT>.md` files, `UPCOMING_GAME_RESEARCH_GUIDE.md`, `MODEL_AND_DATA_SPEC.md`, `ALGORITHM_PORTFOLIO_AND_EVALUATION.md`, `AGENT_ROLE_AND_TASK.md`, and `PERFORMANCE_ELIGIBILITY_POLICY.md`.

### Source-log lineage checked

The combined archive records the component lineage as `PREDICTION_LOG.md` → `PREDICTION_LOG_2.md` → `PREDICTION_LOG_3.md` → `PREDICTION_LOG_4.md` → historical `PREDICTION_LOG_6.md` (P-103–P-123) → `PREDICTION_LOG_5_SETTLED_2026-08-29.md` (P-124–P-136) → mini logs P-137–P-214 → P-215/P-216 and running P-217–P-238 → P-239–P-248 → overlapping raw P-241–P-267 continuation and its folded settlement summary → P-268–P-271 → active combined continuation P-272–P-305. Duplicate-storage/alias records are not treated as new events.

### Important audit discipline

1. A historical loss is not automatically a process defect; a supported ordinary tail can beat a compliant forecast.
2. A historical win does not validate defective reasoning.
3. Old cards are distinguished from later rules: an issue-time compliance failure is different from a current-rule gap.
4. Raw row W/L counts are not treated as independent trials because many cards contain complements, alternates, nested phases or shared-thesis rows.
5. The 2026-09-06 user directive is respected: once settled, a row is eligible for the historical performance scorecard. That does not make it valid numerical-model training/calibration evidence.

---

## 2. Executive conclusion

The current Sports Research framework is materially stronger than the earliest logs. Most of the obvious historical failure modes are now explicitly named in the rules: identity/contract freeze, state freshness, source ownership, one coherent event distribution, phase-state propagation, component/separation budgets, winner/cushion reconciliation, two-sided kill paths, dependence de-duplication, operator definitions, and retrospective anti-overfitting.

However, the audit still finds **five major open structural risks**:

1. **Predictive weighting is leaking into `PROMOTED_PROCESS` lessons**, particularly L-075–L-077, even though the governing rules say forecast weights need prospective testing.
2. **The system forces a precise ordinal ranking without recording how close the ranks actually are.** Historical Rank #1 versus Rank #2 performance changes sharply by cohort, so an unqualified #1/#2 order can overstate certainty.
3. **Retrospective process grading is not blinded to the result.** The framework separates outcome and process conceptually, but it does not require a result-blind compliance pass first.
4. **The new settlement-only performance rule can create a misleading pooled scorecard** unless method, horizon, sport, target family and dependence are always stratified.
5. **Settleability/source quality remains a predictive-system input that is only partly formalised.** Corners now have a specific cap, but the same problem appears in powerplay, reduced-overs and operator-defined OT/action markets.

The most important pattern is therefore **not** 'the model should prefer Overs', 'Rank #2 is better than Rank #1', or any other simple directional flip. The stronger conclusion is that the framework is good at discovering mechanisms but still inconsistently converts those mechanisms into **relative rank weights** and **tail/separation mass**. That is a ranking/governance problem, not evidence for a universal directional betting rule.

---

## 3. Historical progression by cohort

| Cohort | Audit basis | What the record shows | Main blindspot signal |
|---|---|---|---|
| P-001–P-060 | Comprehensive Aug 22 retrospective | 59 forecast events; P-021 no forecast. P-001–34 legacy mixed ledger and P-035–60 raw ledger are not directly combinable. | Dependence stacking, phase leakage, proxy-to-target substitution, winner/handicap mismatch, bullpen/HR tails, small-sample and boundary errors. |
| P-064–P-084 | Independent MDS-v2.1 review | 20-event historical clean cohort under the then-current provenance rule: Rank #1 14/20; Rank #2 10/20; lower slots not monotone. | Ranking order was not proven even when Rank #1 looked strong; P-085 showed a process-defective live state can still produce winning rows. |
| P-089–P-136 | Combined component audits | Settled/closed across mixed sports, with queue and source-state corrections. | Continued adverse-branch, state freshness, source ownership and dependence lessons; no defensible fitted probabilities. |
| P-137–P-163 | Independent event-level audit | 26 actionable settled events: Rank #1 16–10; Rank #2 12–13–1 unresolved; Rank #4 15–11; winner calls 20–6. | Strong warning against interpreting rank slot as stable skill. Adverse branches were often named but left decorative. |
| P-165–P-186 | Independent audit | Rank #1 14–8; top-two coverage 18/22; 54–42 definite row ledger plus unresolved/provisional niche rows. | Volume/allocation/margin conflation, phase propagation, starter-vs-full-event exposure, small early-season samples, kill paths not affecting rank. |
| P-187–P-214 | Independent audit | 27 actionable finals: Rank #1 12–15; potential winners 15–12; P-192 no action. | Uncertainty often moved the centre instead of width; role needed score/phase exposure; extension endpoints and named kill paths were under-modelled. |
| P-215–P-238 | Sept 2 settlement audit | Event-by-event process grades, with several compliant cases and many explicit process defects; P-217 definition-limited. | Start-state freshness, death-resource tails, winner coherence, separation, sparse phase evidence and operator definitions. |
| P-239–P-248 | Framework review | Six settled events in review: Rank #1 5–1, Rank #2 2–4, Rank #4 5–1; higher-ranked total direction lost 5/6. | Rank-slot counts were explicitly rejected as a rule. Cross-row coherence, separation budgets and attribution asymmetry drove the patch. |
| P-241–P-267 | Controlling folded settlement summary | 21 actionable events: Rank #1 13–8; 46–42–2 row ledger; eight deep Rank-1 losses. | L-061–L-064 emerged, but the standalone full audit referenced by the archive is absent from the current checkout, reducing granular reproducibility. |
| P-268–P-271 | Sept 4 settlement | Rank #1 2–1 across three cards; P-269 no action. | Fresh-method read failure (L-065); recent H2H/regime reconciliation (L-066); winner/cushion mismatch persisted. |
| P-272–P-279 | Sept 4 promote/archive audit | 29 settled contract rows: 14–15; Rank #1 3–4; Rank #2 4–3; named winners 6–1; P-272 no forecast. | Several results were right with defective process; separation/component budgets and source/state compliance still failed. |
| P-280–P-303 | Sept 5 + 5(b) audits | Recent settled subset showed Rank #1 6–7 across 13 resolvable rank-1 rows in the 5(b) pass, Rank #2 7–3; both top-two right 2/8 and both wrong 2/8 in eligible multirow cases. | Recent concentration of Rank-1 total/Under failures, personnel/role propagation defects, core-absent friendly anchoring, corners/powerplay settlement gaps. |
| P-304–P-305 | Latest Drive snapshot | Both were still live/deferred at the latest reviewed settlement pass. | No final retrospective exists in the Drive snapshot; they are excluded from outcome-based blindspot conclusions. |

### What this chronology means

The ordinal problem is persistent rather than a one-off. There are cohorts where Rank #1 looks strong and cohorts where it is weak, while lower ranks sometimes equal or outperform it. Because the candidate slate is user-selected and often contains exact complements, those slot records cannot be read as calibration. They do show that **the current qualitative ranking function has no measured rank-gap or pairwise confidence layer**, which is why B-02 is classified HIGH.

---

## 4. Blindspot register

| ID | Severity | Status | Blindspot | Evidence from logs/rules | Observation / proposed control |
|---|---|---|---|---|---|
| B-01 | HIGH | Open governance inconsistency | Process controls are beginning to change forecast weighting without being governed like forecast-weight changes. | RULES_GENERAL §9 says one event creates a candidate and forecast weighting needs preregistered prospective scoring. L-075 explicitly requires reserve/debutant production to affect the final ranking weight; L-076 discounts core-absent friendlies in the reference corridor; L-077 conditions a personnel-loss discount. Those are sensible ideas, but they are directional/weighting instructions promoted from same-session outcomes. | Split lessons into (a) integrity/process controls that can promote immediately because they enforce identity, arithmetic, state or coherence, and (b) predictive weighting rules that remain CANDIDATE/TESTING until prospective evidence. Do not use the label PROMOTED_PROCESS to bypass the forecast-weight firewall. |
| B-02 | HIGH | Open | Forced unique ordinal ranks create spurious precision when two rows are genuinely near-tied. | The rules require a unique rank even with LOW evidence and say near-tied branches should remain near-tied in language, but there is no structured RANK_GAP/ORDERING_STRENGTH field. Historical slot performance is unstable: P-064–84 Rank1 70% vs Rank2 50%; P-137–163 Rank1 16–10 but Rank4 15–11; P-187–214 Rank1 12–15; Sept5(b) Rank1 6–7 vs Rank2 7–3. | Keep the required ordinal order, but record NEAR_TIE / SMALL / MODERATE / LARGE pairwise rank gap and the exact evidence that makes #1 outrank #2. This makes Rank-1 diagnostics interpretable without inventing probabilities. |
| B-03 | HIGH | Open | Retrospectives are outcome-aware from the start, so process grading can suffer hindsight contamination. | Current rules correctly separate outcome, process, defect, knowability and lesson, but they do not require a blind compliance pass before reading the final driver. Many retrospectives infer that a named branch was 'underweighted' after that branch happens. | Use two-pass retrospective logic: first audit the frozen card against issue-time rules/evidence without the result; then reveal the result and perform driver/knowability analysis. Preserve both grades. This distinguishes a genuine preissue omission from ordinary supported-tail realisation. |
| B-04 | HIGH | Open reporting risk under user directive | Settlement-only performance eligibility pools fundamentally different horizons, methods and provenance states. | EP-2026.09.06-v2 correctly follows the user's instruction that every settled row counts. But pooling pregame, live, late-import, multiple method versions and correlated rows into one headline percentage would be statistically uninterpretable. | Keep settlement as the eligibility gate, but always stratify descriptive performance by issued method/version, pregame/live horizon, sport/competition, target family, selection origin and performance role; use event/decision-set weighting so multirow cards do not dominate. |
| B-05 | HIGH | Covered in rules, still an implementation/reporting hazard | Complement-heavy and user-selected slates make raw row win rates structurally misleading. | Many cards contain both Over and Under or both sides of a spread, so one side often wins mechanically. RULES_GENERAL §8 and ALGORITHM_PORTFOLIO already warn that user slates are selected and dependent, yet historical summaries still prominently display raw W-L totals. | Foreground event-level Rank1, exact-pair ordering, Wins@2/NDCG-style diagnostics and dependence-normalised counts. Raw contract W-L belongs as descriptive ledger only, never the leading performance claim. |
| B-06 | HIGH | Partially closed, still open cross-market | Preissue settleability is not yet a universal actionability gate for niche statistics. | Corners generated repeated provisional/unresolved outcomes and L-073 now caps corners Rank #1. P-300 powerplay and P-302 corners still had evidence gaps; hockey/MLB rows also retained operator-definition ambiguity. | Generalise the concept: before ranking any niche-stat or operator-sensitive contract highly, demonstrate a plausible field-owner/provider settlement lane and exact action/OT/DLS terms. If the lane is unavailable, cap actionability/evidence regardless of predictive appeal. |
| B-07 | MED-HIGH | Open | Unresolved/provisional rows are not missing at random. | The outstanding queue is concentrated in corners, sparse competitions, reduced-overs action and operator-definition markets. These are precisely the markets with weaker source infrastructure. | Track unresolved-rate by sport/market/source tier. Do not treat the settled subset as representative of all issued contracts; settlement missingness itself is a quality signal. |
| B-08 | MED-HIGH | Partially handled | Historical compliance can be judged against the wrong rule version unless dual grading is explicit. | P-268/P-270/P-271 were honestly graded against their declared v2.9 while also flagging that v3.x already existed. Other old cards are often discussed through current-rule language. | For every historical audit carry two fields: ISSUE-TIME COMPLIANCE and CURRENT-RULE GAP. Never call an old card defective solely because a later control did not yet exist; separately flag implementation drift when the newer rule actually predated issue. |
| B-09 | MED-HIGH | Open operational risk | The process-control set has accreted into a very large checklist, raising omission risk and diluting attention. | The learning register now contains dozens of promoted controls plus sport-specific gates; P-268–271's stale-method read and P-273/P-275/P-276 compliance misses show that having a rule is not the same as executing it. | Classify controls into blocking integrity gates, mechanism-required gates, and context/materiality checks. Audit completion mechanically from the frozen card. Retire/merge duplicates when one general control subsumes several case-specific formulations. |
| B-10 | MED | Open | There is no routine effectiveness audit for promoted process controls. | Integrity controls need not prove predictive lift, but a control that adds burden should still show it reduces the defect it targets. Several historical defects recur after formal controls exist, especially cross-row coherence, separation budgets and participant-state propagation. | Track recurrence rate of each defect class before/after a control's effective date and record compliance burden/failure frequency. For predictive-ish controls, require prospective outcome evaluation separately. |
| B-11 | MED-HIGH | Open implementation drift, not a proven directional rule | Totals, especially Rank-1 Unders, repeatedly fail through upper-tail or separation states. | Examples span P-009, P-018, P-027, P-059, P-171, P-187, P-194/P-196/P-199, P-240/P-244/P-245/P-248, P-270, P-277/P-279, P-292/P-294/P-295/P-297. The recent Sept5(b) pass itself notes the 'total #1 loses, side/spread #2 wins' pattern. | Do not install an Over bias. Treat this as a branch-completeness/mixture diagnostic: require explicit probability-free branch mass language for the upper-tail path and track total-direction rank results by sport and threshold position. Existing C-PL11 is the right governance vehicle. |
| B-12 | MED-HIGH | Covered on paper, recurring in execution | Winner, handicap and total are still being ranked from partially inconsistent states. | P-010, P-060, P-170/P-177/P-178/P-181/P-186, P-223/P-230, P-244/P-248, P-271, P-285/P-289 and P-301 show variants of the same failure. Current G25.1/G30.1 and separation-budget rules directly address it. | Treat every top-ranked state as a constraint and mechanically map it into every other contract's units before ordering. A documented coherence check should be a required field, not merely narrative. |
| B-13 | MED | Open evidence limitation | Sport-specific conclusions are too sparse in several sports. | Rugby union, ice hockey and American football have far fewer historical events than baseball/soccer/cricket; even rugby league has only modest sample depth. Detailed sport rules can therefore look more empirically mature than their evidence base. | Label every sport-specific lesson with evidence density and avoid direction/weight claims in sparse sports. Process controls can remain; predictive emphasis should stay generic until prospective sport-specific samples accumulate. |
| B-14 | MED | Open semantic/evaluation issue | MARKET_BLIND is not equivalent to market-independent. | Prices, movement and consensus are excluded, but the user-supplied thresholds and candidate slate are themselves market-produced objects. Threshold placement changes difficulty and makes the evaluation conditional on what the market offered. | Use 'price-blind / market-analysis-blind' in interpretation and state that observed accuracy is conditional on supplied market thresholds. Do not present it as independent predictive lift over the market. |
| B-15 | MED-HIGH | Open reproducibility gap | The detailed P-241–P-267 settlement/retrospective artifact referenced by the archive is absent from the current Drive checkout. | The combined archive preserves the cohort totals, the eight Rank-1 loss IDs and the resulting L-061–L-064 lessons, but also explicitly says the standalone P267 audit previously described as present is absent. This limits event-level replay and source-verification depth for that cohort. | Treat the folded summary as controlling evidence, but mark this cohort REPRODUCIBILITY-LIMITED in future audits until the underlying artifact or equivalent per-event settlement/source tables are restored. Do not reconstruct missing detail from memory. |

---

## 5. What the current rules already cover well

These are **not** open blindspots unless execution fails:

- **Identity and exact contract geometry:** official event, participants, target definition, endpoint, push/action terms and state freeze are explicit hard gates. Historical P-003/P-017/P-225/P-274/P-287-type errors are now directly covered.
- **State freshness and start crossing:** P-070/P-085/P-272/P-276/P-280-style failures have explicit live/zero-snap/final-refresh controls.
- **One coherent distribution:** totals, team allocation, winner and margin must come from one joint scenario object. This directly addresses P-009/P-010/P-060 and many later cross-row inconsistencies.
- **Component and separation budgets:** current rules explicitly prohibit inferring a cushion from an Under or a blowout from an Over and require phase-wise floor/centre/high budgets.
- **Phase propagation:** cricket powerplay→middle→death, baseball starter→relief, halves/quarters/sets and extension endpoints are now formal state transitions.
- **Bidirectional mechanisms:** aggression, turnovers, weather and similar variables must model both signs rather than only the favourable causal path.
- **Dependence/de-duplication:** exact complements, aliases, phase/full targets and shared evidence units are tagged; one thesis cannot masquerade as several independent confirmations.
- **No probability invention:** the current qualitative method has no validated fitted model, so published probabilities, fair odds, ROI and edge claims remain prohibited.
- **Single-result anti-overfitting:** RULES_GENERAL §9 explicitly says one event creates a candidate and weight promotion needs prospective scoring.

The main problem is therefore **execution and governance around these controls**, not their absence.

---

## 6. Cross-sport recurring mechanisms

### 6.1 Named kill paths were often treated as disclosure instead of evidence

This is one of the strongest all-history patterns. Early cards frequently named the eventual failure state but still ranked as if it were negligible. Later examples include P-184, P-214, P-270, P-277, P-278, P-279, P-285, P-289 and P-295. Current rules say a named ordinary kill path must affect evidence/rank, but the history shows this is not reliably operationalised.

### 6.2 Low total was repeatedly confused with close margin

P-060, P-143, P-145, P-170, P-193, P-206, P-226, P-247, P-270, P-294 and P-301 illustrate variants. The current separation-budget rule closes the conceptual gap; repeated post-rule recurrences make it an implementation-control issue.

### 6.3 Phase/full-target leakage remains a recurring risk

Cricket and tennis supply the clearest examples: P-007/P-018/P-032, P-171/P-175/P-187, P-211/P-245/P-275 and P-286. Early state can point one way while retained resources or extension endpoints point the other. Current rules handle this correctly, but qualitative weighting still needs explicit state-transition mass rather than a narrative warning.

### 6.4 Source/settlement quality is not peripheral

P-003, P-126, P-148/P-149/P-151, P-166, P-176/P-178/P-179, P-200, P-217, P-233–P-235, P-273, P-300 and P-302 show that an otherwise attractive market can be hard to settle cleanly. This is why settleability should influence rank/actionability before issue, not only at settlement.

### 6.5 Winner calls are a separate model object

Numerous cards had a correct cushion or total while the potential winner was wrong, including P-010, P-029, P-053, P-058, P-179, P-190, P-204, P-223, P-230, P-271 and P-293. The current rules correctly separate winner from handicap/total. Historical reporting should continue to grade it separately rather than treating a correct Rank #1 as implied winner accuracy.

### 6.6 Recent total-direction misses are concentrated but not yet a weight rule

The September audits show a conspicuous cluster of Rank-1 Under/total failures, especially P-292, P-294 and P-295, with sides/spreads often doing better at Rank #2. That is useful evidence for `C-PL11-ALL-TOTAL-DIRECTION`, but it does not justify mechanically lifting Overs. The plausible causal issue is incomplete upper-tail/separation mixture construction.

---

## 7. Sport-specific observations

### Baseball

Historical failures repeatedly involve starter HR/contact tails, hook timing, bullpen leverage state, inherited runners, multi-run clusters, extra-inning rule environment and the false inference that a short/weak starter automatically implies a full-game Over. Current baseball rules now cover most of this. The remaining blindspot is **relative weighting**: one-sided relief failure or favourite separation can occur without a high total. P-240/P-247/P-248/P-274/P-277/P-278 show why the starter–relief state must be solved separately for each team's scoring distribution and margin.

### Cricket

The dominant historical failure is **phase transfer**: powerplay, middle and death states are linked but not exchangeable. Retained wickets/resources repeatedly defeated full-innings Unders after a correct early read. Current cricket rules are strong on resource-conditioned transitions. Residual risk remains in sparse competitions, XI/toss/strip uncertainty, reduced-overs operator terms and source quality, as seen in P-217/P-300.

### AFL / AFLW

The early logs overused clearances/hitouts/territory without fully converting them into scoring shots, shot quality and conversion. Later failures show the opposite problem: the opportunity-volume branch exists but extreme separation or conversion tails are too narrow. Current AFL rules explicitly model scoring-shot volume and conversion. Residual risk is opponent-conditioned personnel impact and extreme favourite blowout allocation, especially P-292/P-298.

### Soccer

Possession, shots and goals repeatedly failed as corner proxies. Lead state can suppress or explode corners independently of goals. L-073 now treats corners as a sourcing/reliability problem as well as a prediction problem. This is one of the clearest examples where **market settleability should be part of actionability**.

### Basketball

Q1/H1/full-game dependence, rotation/bench exposure and large-spread separation are recurring issues. P-196/P-215/P-285/P-299 show that one-sided blowout histories and preparation games can be especially misleading. L-076 is directionally plausible but, because it tells the model how much to discount a specific evidence class, it should be governed as predictive weighting rather than a pure process control.

### Rugby league / NRL / NRLW

Spine/bench availability, reserve/debutant production, fatigue and second-half separation are central. P-295 is especially important because the decisive pregame evidence was already found but did not move the final rank. That is a **ranking-weight propagation failure**, not a research acquisition failure.

### Tennis

Set-count mixture, net-game handicap arithmetic, tiebreak/close-set extension and recovery workload are the key issues. L-068 closes the arithmetic defect. Cushion evidence and long-match evidence must be reconciled, as P-245 and P-275 show. Recovery-length remains appropriately a prospective candidate rather than a promoted weight.

### American football

Preseason QB/unit rotation and new-regime uncertainty dominate the historical cases. Sparse samples mean current controls should remain process-oriented. Uncertainty should generally widen the state distribution before it shifts the centre.

### Ice hockey

Goalie identity and OT/SO/operator action definitions are critical. P-166/P-199/P-200 show that a research result can be clear while the actual betting contract remains definition-limited. This supports the universal settleability/actionability gate in B-06.

### Rugby union

The historical sample is too small for sport-specific predictive conclusions. Retain process controls, but treat any sport-specific directional learning as evidence-limited.

---

## 8. Recommended audit protocol for future retrospectives

This is an observation document only; nothing in Drive has been edited. The following protocol would close the open blindspots without changing historical forecasts:

1. **Pass A – result-blind compliance:** inspect the frozen card, cutoff evidence, exact contract, state, source fields, scenario tree, kill path, component/separation budgets and rule version without looking at the final.
2. **Pass B – outcome/driver:** then inspect the final, determine actual driver, knowability and whether the branch was ordinary or exceptional.
3. **Dual grade:** record `ISSUE_TIME_PROCESS_GRADE` and `CURRENT_RULE_GAP` separately.
4. **Rank-gap field:** retain unique ranks but add pairwise ordering strength and near-tie flag.
5. **Learning firewall:** pure integrity/coherence controls may promote immediately; any rule that changes a centre, corridor, discount, tail weight or final rank remains a prospective candidate.
6. **Settleability field:** record preissue `SETTLEMENT_LANE = VERIFIED / PARTIAL / UNKNOWN` and cap actionability for unknown niche markets.
7. **Performance stratification:** settlement still controls eligibility per L-078, but every scorecard is sliced by method, horizon, sport/target and dependence role.
8. **Control-effectiveness review:** periodically test whether promoted controls reduce recurrence of their target defect instead of only accumulating more checklist text.

---

## 9. Event-by-event audit appendix – P-001 through P-305

Every canonical ID is listed below. Where a comprehensive retrospective exists, the recorded result/driver/process finding is summarised. Where the controlling archive exposes only a cohort-level settlement summary, the appendix says so rather than inventing missing event-level detail. P-304/P-305 remain unresolved in the reviewed Drive snapshot *(superseded — see the discrepancy note at the top of this file)*.

*(The full per-ID appendix table, as supplied, is preserved in the conversation record that produced this repository state and is not re-transcribed a second time in this archive file, consistent with this repository's existing practice — see `README.md`'s "Complete Markdown recording requirement" and the equivalent note in `prediction logs/PREDICTION_MINI_LOG_11_P294_P305.md` — of keeping exceptionally long supplied tables in one place rather than duplicating them across files. The disposition of every distinct finding the appendix contains is captured structurally through `B-01`–`B-15` above, all of which cite specific IDs from this appendix as evidence, and through the cohort table in §3.)*

---

## 10. Final assessment

The historical logs show genuine improvement in research discipline. The framework has moved from many ad-hoc, outcome-led explanations toward explicit identity, state, source, transition, dependence and coherence controls. The largest remaining risk is no longer 'missing a basic rule'; it is **how the qualitative system turns a large rule set into a stable ordinal ranking without a validated probability layer**.

The best next improvement is therefore not another long list of sport-specific directional heuristics. It is stronger governance around ranking: result-blind compliance, rank-gap recording, universal settleability/actionability, strict separation of process controls from predictive weighting, and stratified decision-set evaluation. Those changes would make future retrospectives more falsifiable and would reduce the chance that a correct post-game story is mistaken for a validated pregame improvement.

### Source limitation

No external web research was used for this audit. It is intentionally a Google-Drive/internal-record audit. The event outcomes and retrospective claims are those already recorded in the canonical Drive materials. The missing standalone P-241–P-267 settlement artifact is therefore not reconstructed from outside sources.
