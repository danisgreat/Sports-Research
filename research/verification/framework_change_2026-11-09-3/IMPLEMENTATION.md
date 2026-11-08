# Framework integrity, settlement and source implementation

Owner instruction: implement the comprehensive review, settle outstanding logs under the framework, and add accurate sources that agents can access. Base main `9a07a556643c8a9dfe48db9938faf7dca01c7141`. Release **MDS v24.8 / CR-2026.11.09-R3 / P-2026.11.09-v24.6**. Original numerical methods, probabilities, ranks, issue phases and older source packages are preserved.

## Implemented code changes

| Review defect | Change and meaningful verification |
|---|---|
| Wrong teams and post-start standings accepted | Exact HOME/AWAY/LEAGUE identity/competition, finite nonnegative totals, integer game counts and aware provenance clocks are mandatory. Known/snapshot must respect the information horizon; no historical backfill from current standings. Adversarial wrong-team, competition, future and missing-evidence tests. |
| Impossible nested totals accepted | Unconditional W/L nesting for totals, scoped team totals and handicaps, including pushes. Complements checked in the same scope. Team-total headers identify team/period; separate teams are not compared. Ledger admission reproduces and rejects the old Over170.5=.52 / Over190.5=.60 case. |
| Wrong effect competition, target and units admitted | Scope/target/unit compatibility and finite sizes enforced; each moved row needs a named adjustment counterfactual. This is declared-input validation, not proof of causal truth or numerical impact for arbitrary distributions. |
| General evaluator could promote32 games over8 weeks |50 unique paired events now required by the general evaluator as well as the cycle wrapper; existing8week/effect-size/calibration rules retained. Synthetic32game/eightweek reproduction cannot promote. |
| HTTP clients bypassed source audit | `ml.source_access` gates every sporting HTTP fetch and redirect destination. Both OpenAI and Anthropic token families checked. Unknown/blocked policies stop before network content fetch; offline tests assert it. |
| Live evaluation failed on different interval schemas | Preserve the union of Brier/log-loss export fields, including infinite-loss counters; regression test plus real frozen-NBA rerun. The failed partial export is retained and labelled. |

The NBA standings route has a tested permitted Fox fallback. Its PPG×games totals are a **rounded proxy**, labelled in input/receipt, with maximum rounding error .05 per team per game. Exact totals remain distinct. Other unsupported competitions require a reviewed provenance-complete CSV. `league-day freeze --fixtures` admits reviewed capture-bound non-ESPN slates; no unattended scheduler was created.

## Settlement and custody

- Six active cards imported as P-623–P-628:24 ranked rows and232 separately printed contract assessments. The tennis draft stays NOT_ISSUED/NOT_PRIMARY. Original probabilities and old methods are literal, not upgraded to current-method compliance.
- Eight old package events retained as P-629–P-636:44 supplied/diagnostic rows. The owner explicitly selected MLB native849817, Game5, Rays3–1Guardians; the erroneous original Game4 wording/features remain visible and are not relabelled valid Game5 pregame inputs. Two Be1–Neptunas corner directions remain UNRESOLVED.
- Held Beijing draft retained as P-637 after inserting only its known missing BEGIN boundary into a separate intake copy. Every original body byte retained. Current structured final/half/corner fields agree with the old values, evidenceC with independent feed provenance unproved.
- Existing P-584 settled under its original ID: Dragones5–1Guerreros, halftime2–0;4 diagnostic rows2W/2L. Its separate contemporaneous FROZEN_SOURCE receipt was missing; FREEZE_CUSTODY.csv records that procedural limitation instead of inventing an earlier receipt.
- Two actual October NBA-CYCLE-1 frozen bundles now have verified settlement/expert losses. Their12 ledger rows remain unchanged and are never added to card wins. Learning-store views13–15 append2results and3corroborating observations; no quarantine or historical known-at rewrite.

Across the16 card settlements: **76 new effective contract rows,74 graded and2 UNRESOLVED**. R1–R12 and the required14-section losing-trigger reviews are in the package SETTLEMENT documents. Operator definitions, source independence and historical cutoff proof remain distinct from sporting grades. Legacy primary p_card NOT_ESTIMATED stays missing; analyst W is not substituted for conditional p_card.

All15 canonical cores were read back and matched their source hashes; IDs are contiguous P-623–P-637, next P-638, reservedP-518–P-522 untouched. Part9 preserves its full prior prefix; Parts1–8 and original dataset prefixes remain unchanged. New empty mini `20261109R3NEXT` has zero cards, nextlocal G0001. Base originals are archived byte-for-byte under archive/integrity_2026-11-09_r3/. See CANONICAL_READBACK.csv, LOG_CUSTODY.csv and final custody verification.

## Sources and older backlog

[Source catalogue](../../source_routes/README.md):209 explicit competition/scope rows across ten named sports, OTHER_SPORTS onboarding and venue weather, with exact-URL access checks, official-owner routes, actual captures and honest field limits. All primary catalogue routes meet the dated configured agent policy. Many minor competitions still have discovery-only coverage; neither universal absence of technical filtering nor accuracy of every field is certified. Recheck the exact event URL immediately before use.

Actual successful routes include NBA official PDFs, Fox standings, NBL match/club schedule, EuroLeague XML, AHL JSON, MLB live feeds, MyKBO innings, NPB statistics, official LFF goal times, permitted tennis set scores, AFLTables and sport-owner indexes. Blocked OpenAI paths now supersede the earlier Anthropic-only access claims; ATP-root permission does not authorise its blocked archive. No proxy/mirror/agent spoofing bypass is used; only sporting statistics are admitted from mixed pages.

[Backlog review](BACKLOG_REVIEW.md) accounts for every generated unresolved row, all 40 older hand flags, fresh source queries and newly recovered fields. Blank administrative slots, no-action/no-forecast records and collided aliases are not invented forecasts. Actual remaining gaps are listed in [UNRESOLVED_POST_IMPORT.csv](UNRESOLVED_POST_IMPORT.csv), including Be1 corners, P-596/P-598 definitions, P-126 identity/state, historical field-owner/period/custody gaps and old source/issue proof. This task **does not claim every historical log fully settled or certified** where the required evidence remains unavailable.

## Release and predictive limits

NBA-CYCLE-4 and NHL-CYCLE-6 are integrity refreezes, same recipes, on real passed current GATE-v2 receipts. Earlier unpublished NBA-CYCLE-3/NHL-CYCLE-5 refreezes became stale when the newly discovered export bug was fixed; they remain retained rather than restamped. MLB remains blocked:374 finals cover one season and fail G1. G4's domain/capture checks are a structural lineage heuristic; they do not prove that distinct publishers independently collected every observation.

The new fixed NBA experiment is preregistered under research/prospective/NBA_R3_EXPERIMENT.md. Future50 paired games and 8 settled weeks cannot be manufactured retrospectively; no predictive promotion or new future fixture is claimed. AUTOMATION: NOT_SCHEDULED. The two old-version frozen events are evaluated separately and remain insufficient evidence.

## Verification and publication

The final test receipt and scoped custody/source validation are recorded alongside this report. The verified Git commit and remote SHA are returned to the owner separately. A green suite supports implementation consistency; it does not establish source truth, historical forecast eligibility or predictive advantage.


**Final validation:** see TEST_RESULTS.md and TEST_RECEIPT.csv (723distinct cases via fullrun plus scopedrechecks), CUSTODY_AND_VALIDATION.csv, NEW_SETTLEMENT_INVENTORY.csv and card_history_verified/CARD_HISTORY.md.
