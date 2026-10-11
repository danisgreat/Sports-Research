# Manual edge-case walkthroughs

Synthetic documentation fixtures only. These were reasoned through against the new rules/templates; no live forecast, automated validator, import transaction or sporting-source test was executed. EXAMPLE identifiers allocate no P-ID.

| Case / stipulated input | Required and observed documentary result | Controlling check |
|---|---|---|
| Qualitative: identity known, no defensible distribution; one supported direction | One qualitative ranked row, p NOT_ESTIMATED, baseline BASELINE_UNAVAILABLE, numerical gate NOT_ASSESSABLE; retained research, not padded to four | C3/C5/C14 |
| NO_FORECAST: event ambiguity cannot be resolved | Retain intake/ambiguity and follow-up, no ranked row; do not invent participant identity or numerical gate | C2/C3 |
| No baseline but supported p=.70 | Numeric research allowed; paired Brier NOT_COMPUTABLE; never substitute .50 or post-event climatology | C14/S9 |
| Push: W=.60,P=.20,L=.20,V=0 | p_card=.60/.80=.75, unconditional loss .20, not .25; realised PUSH stays outside binary score, retained in coverage | C4/C6/S6 |
| Missing final corner count | Terminal event / UNRESOLVED_EVIDENCE; corner row UNRESOLVED/X, no forced VOID; result-score rows can settle | S4/S5/S10 |
| Partial count bound [8,12], line 10.5 | Crosses threshold: UNRESOLVED/E, no point estimate used to grade | S4/S5 |
| Partial bound [8,10], Under 10.5 | Every feasible value wins: WIN/E with bound/source explanation; retain uncertainty in raw value | S4/S5 |
| Unknown operator retirement rule | Frozen sporting convention may produce a research result; operator settlement UNKNOWN_DEFINITION/UNRESOLVED; no invented post-result default | S4/S5 |
| Actual frozen void condition verified | VOID under that condition, not LOSS and not missing-data erasure; denominator excludes with explicit count | S4/S6 |
| Home .678, away .302, endpoint forbids draw | Sum .980, missing .020: FAIL C4; no fabricated residual reassigned silently | C4 |
| Home .70, away .20, permitted draw .10 | Sum 1, PASS arithmetic; do not force draw into a winner | C4/C9 |
| Same-quantity bracketing O4.5 and U14.5 | Loss sets cannot intersect; exact zero MECHANICALLY_PROTECTED, not proof of predictive skill | C6 |
| Joint unavailable, unconditional losses .20 and .30 | Bounds [0,.20]; no fabricated exact .06 from independence | C6 |
| Adjustment .10 SD flips primary ranks | ADJUSTMENT_DEPENDENT with unadjusted pair; LARGE_ADJUSTMENT false | C7 |
| Numeric candidates .70 and .80 printed in that order | FAIL primary order; sort by unrounded p/key, not by narrative or joint objective | C3 |
| Gate has no eligible alternative | NOT_ASSESSABLE, no invented gap or automatic PASS | C5 |
| Extra nonstandard regime label 'HOT_TEAM' | Not an operative regime; describe unsupported context separately, no invented multiplier | C8 |
| State verified not started after scheduled delay; issue 2 min after scheduled | PREGAME event state may be supported, but scheduled lead −2 and LATE_START band retained | C11 |
| Research finishes before start, actual write occurs after verified start | LIVE_OBSERVED/late research, not pregame; completion timestamp alone fails issue claim | C11 |
| Frozen core exists canonically; new settlement does not | Skip identical core, append missing settlement under same ID; no new card or ID | Import §2/§3 |
| Entire package already imported exactly | Zero new blocks/IDs and no scoreboard double-count; ALREADY_COMPLETED | Import §3 |
| One complete new block then interrupted partial suffix | Compare plan/actual; preserve complete identical block, repair only known uncommitted partial suffix; no full-file restore | Import §3 |
| Different event already owns requested P-ID | Conflict blocks dependent import; no renumber, skip, overwrite or new file to hide collision | Import §2 |
| Old log opening next P-550, current verified entries/state next P-580 | Opening is historical; reconcile current records, never execute removed allocator | Rules §9 |
| Rollover rerun, exact closure/new part already present | No duplicate part/closure; next ID unchanged | Rollover §2/§3 |
| Old card has no original baseline/expected SD | Preserve original text; missing scores/z are NOT_COMPUTABLE, not backfilled | Compatibility/S3/S11 |
| CSV quoted field contains embedded newline | Physical line count does not equal event count; require logical-record accounting or disclose unverified count | Prompt 7 §3 |

## Minimal qualitative record shape

EXAMPLE-QUALITATIVE / NOT_ISSUED / NOT_IMPORTABLE. Known synthetic identity, no reliable scoring parameters. Analysis UNCALIBRATED_QUALITATIVE; one direction 'A to win, stipulated regulation endpoint' based only on explicitly hypothetical availability evidence; p_card NOT_ESTIMATED; BASELINE_P BASELINE_UNAVAILABLE; gate/joint/expected score NOT_COMPUTED with missing-input reason. No numeric proper score. This is a schema branch example, not a claim that a real match has supporting evidence.

## Migration walkthrough

Keep an in-progress mini-log-5 card's exact four original rows and timestamps. Do not add a fifth baseline column to its frozen table. At settlement append a dated missing-baseline/actual-evidence disclosure and current unresolved queue where needed, while preserving its original policy/scoring label. Start mini-log-6 only in the next new mini. An already published historical no-evidence VOID is not automatically regraded by this release.
