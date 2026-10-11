# v10 verification record

Base revision: `2d6d86350ce4d6bd9f4ae0f34a42351e71ff0e4b`. Initial local main equalled fetched origin/main and was clean. The October 11 retrospective published during the earlier review was re-read before this implementation. No prior untracked draft was overwritten.

## Completed checks

| Check | Result and evidence |
|---|---|
| Eight workflows covered | All eight active prompt files contain scope/inputs, reading authority, execution, missingness/failure handling, readback and return requirements; 4–8 have explicit publication semantics |
| Authority consistency | MDS-2026.10.11-v10.0 / CR-2026.10.11-R1 / SCV-2026.10.11-v6 / SEL-2026.10.11-v2; mini-log-6 / mini-settlement-5; canonical-md-1 retained |
| Archive before/after identity | 32 preserved pre-change documents match their base Git blobs under repository text normalization; 0 mismatches. ARCHIVE_NOTE.md is the explanatory addition, not a replacement for the preserved root README |
| Frozen example prefix | Exact byte comparison PASS: active example 7,357 bytes is the unchanged prefix of settled example 11,859 bytes (before any Git checkout normalization); original footer retained |
| Arithmetic example | Four-state masses sum 1; primary p=.80/.80, baseline=.75/.75; A/B means 1.25/.30; total/margin 1.55/.95; variances .5875/.21/.2475/1.3475; primary paired Brier delta +.0775 and log-loss delta +.22314355 recomputed |
| Card checks C1–C16 | Worked numeric fixture satisfies arithmetic/order/gate/joint/sensitivity/format branches; live identity/authority/source/capture/pregame custody checks explicitly N/A synthetic, not claimed live PASS |
| Settlement checks S1–S12 | One literal card/core, four literal propositions/p/baselines, frozen prefix, correct all-loss counts, R1–R12 and eight deep sections; live-source/clock/real ID checks N/A synthetic |
| Edge cases | 27 manual input/expected-result walkthroughs in EDGE_CASES.md, including missing evidence, pushes, bounds, draws, late issue, small adjustment flip, collisions, rerun and partial recovery; no automated importer/validator claimed |
| Protected data scope | No changed path under prediction logs, research/issued_research, Previous Sports Results or the published October 11 retrospective; current allocation remains P-580 and highest P-579 |
| Historical results | Scoreboard v5 numbers retained unchanged below a new explicit historical banner; new v10 section starts at zero. No historical probability/baseline/gate re-estimated |
| Whitespace | Active operating documents and new verification artifacts pass diff --check. The full staged check flags one inherited blank line at EOF in the archived original prompt 2; it is retained to preserve the original, whose base blob matches exactly. No check setting was relaxed. An extra blank line in the new synthetic assembled suffix was corrected |

## Release checks

Changed/new relative file links: **88 checked, zero missing** (archived historical links excluded because their original relative layout is intentionally preserved). Current links into the retired mini-log-2 template anchor and old Rank-2 section anchor retain compatibility aliases. Core versions and new-format labels agree; original versions inside archived/legacy history are intentional. Contradiction search found and corrected the remaining CURRENT_STATE sentence that had incorrectly required every card to be numeric.

Staged release: 68 Markdown files, comprising 30 operating/template/example updates, 32 preserved originals, one archive note and five change/implementation/verification artifacts. No protected logs, raw data, issued sources or prior dated reports staged. The single inherited archive whitespace warning is a documented pre-existing exception, not a newly introduced operating defect.

Synthetic evidence does not validate sporting source truth, live timing, calibration, prediction outcomes or fitted-model performance. No source probes, NBL profile recomputation, KBO dataset repair or prospective experiment was performed by this release.

## Detailed fixture checks

| Check | Outcome / evidence |
|---|---|
| C1 | Format/version fields present; real authority reading N/A for explicitly synthetic fixture |
| C2 | EXAMPLE-001 unique in toy mini; no allocatable P-ID or real duplicate-search claim |
| C3 | Four fixed unique contract keys; .80,.80,.70,.70 sorted by key on ties; supplied rows retained |
| C4 | W/P/L/V and result masses sum one; baseline separately sums one; all p and complements recompute |
| C5 | Alternative b_home .80; .80−.80=0, original/shadow unstable; .62 floor passes |
| C6 | Primary .80 exceeds .58; exact joint .20 on {(0,1)}; no independence assumption |
| C7 | No adjustment; low/base/high scenarios retain pair; separate negative fixture catches .10-SD flip |
| C8 | NONE regime; no unmeasured multiplier applied |
| C9 | Toy endpoint draw permitted; real sport-specific rules N/A, no exact engine claimed |
| C10 | Stipulated points field and no live capture/operator; status explicit |
| C11 | Hypothetical cutoff/completion/issue/start ordering and eight-minute lead correct; real pregame proof N/A |
| C12 | Stipulated sporting quantities only; no actual source independence claim |
| C13 | Archive N/A synthetic, not a fabricated sample |
| C14 | Separate stipulated baseline masses produce .75,.75,.60,.60; no actual fitted league claim |
| C15 | Means/variances/covariance and SDs recomputed; decision/appendix present; four-row candidate universe explicit |
| C16 | Files read back; active prefix retained byte-for-byte in settled example; footer unchanged |
| S1 | One source card/one settlement, zero carryovers/addenda; EXAMPLE status preserved |
| S2 | 7,357-byte exact prefix preserved in 11,859-byte settled example |
| S3 | Four original propositions and original p/baseline strings match; expected scores unchanged |
| S4 | Final toy (0,1) makes all four literal rows LOSS; missing-value cases separately remain UNRESOLVED |
| S5 | Evidence expressly synthetic/N/A, never A/B sporting source; bound and unknown-definition fixtures included |
| S6 | 0/2 primary; both-decisive denominator 1 card; no informational wins or shadow extra trials |
| S7 | R1 quotes this fixture; R1–R12 present |
| S8 | All eight deep-loss sections present; no causal percentage or miscalibration proof claimed |
| S9 | Shadow rows separated; originally stipulated baselines preserved |
| S10 | No pending toy fields; real clock N/A; independent missing-evidence fixture exercises queue retention |
| S11 | Brier/log loss and z recomputed; unsupported historic SD/baseline fixture yields NOT_COMPUTABLE |
| S12 | Active/settled/report paths only, no real mini/ID/log changes; lifecycle rerun checked by documented manual scenarios |

Publication receipt is the release commit and independently fetched remote ref, reported in the delivery message. The commit cannot contain its own final SHA; no self-referential hash is fabricated here.
