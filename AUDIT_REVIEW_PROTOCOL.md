# Audit-driven research controls (AUDIT-v1)

MDS-2026.11.15-v24.18 / CR-2026.11.15-R2 / P-2026.11.15-v24.16 / SCV-2026.11.15-v14.
Owner-authorized controls following the 14 November audit. Applies to new numeric
cards issued from 2026-11-15T00:00:00+11:00 and new external event packages created
from that time. Earlier originals keep their method, evidence, timing and grades.
Forecast/profile/kit identities remain v24.15. These controls do not establish
predictive improvement or promote a model, fitted effect or simulator.

## 1. One event, assigned roles, one price

For several chats on one game, use EXT-v3: L1 availability, L2 history and opponent
strength, L3 identity/conditions/contracts, L4 an independent collector check, L5
central pricing. L1-L4 and optional L6 return evidence, not separate primary prices.
Each chat has a distinct chat label and mini namespace; one repository writer merges
accepted evidence into one issued card. Agreement from copied public sources is not
independent corroboration. Keep all parallel originals as dependent research records.

FULL_FIVE is the confirmatory mode. REDUCED and FULL_SIX remain explicit separate
modes. Only authentic pre-exposure SINGLE and pre-start FULL_FIVE comparisons enter
ASSESS-100. This release does not relax those freezes or create missing comparators.
A single researcher may still issue a supported standalone card; five chats are not
a prerequisite for retaining or issuing ordinary research.

## 2. Opponent strength before an underdog-plus lean

Before pricing a positive handicap, L2 and the writer must check the strength and
context of the opponents behind the season margins: dated comparable-opponent
results, home/away, competition/stage and roster regimes, true sample sizes and
source lineage. Record whether a published strength rating or a descriptive
comparison was used. A raw season-average margin alone is insufficient.

This is an evidence check, not a newly fitted adjustment or a betting strategy.
Do not invent a points adjustment, an above-.500 cutoff, a minimum sample threshold
or an empirical success claim from these 21 games. If the check is unavailable,
leave that contract UNPRICED with the missing evidence and next source/action.
Investigate any predictive adjustment on held-out settled history through the
existing hypothesis/release gates before adoption.

## 3. Availability must affect the decision transparently

Identify material returns, absences, debuts, role/minutes restrictions and confirmed
versus projected lineups. If a player change is a main risk, print exact-contract
probabilities with and without the player, the assumed lineup/minutes, effect-table
row/version, scope, uncertainty and overlap with other adjustments.

Use a measured, admitted exact-scope effect for primary probabilities. If there is
no supported effect size, retain clearly labelled sensitivity scenarios outside the
primary PICKS block and leave affected contracts UNPRICED (or the game NO_FORECAST).
Do not manufacture a player effect to fill this requirement. UNKNOWN availability
must remain visible; 'no material change identified' requires an actual dated review,
not an assumption that an unavailable lineup is unchanged.

## 4. Numeric outputs, data sufficiency and legacy methods

The writer/L5 prices supported supplied contracts once, from the supported frozen
reference and admitted adjustments. Every other supplied contract is explicitly
UNPRICED. Qualitative research and NO_FORECAST remain legitimate retained outputs.
Two favourable disagreements between numeric and qualitative chats do not establish
that every research role should generate probabilities.

Each numeric contract declares its method, retained method/scope evidence, actual
sporting sample n, measured coverage, uncertainty and unresolved regimes. A simulation
draw count is never an observation count, coverage or calibration evidence. Explain
thin recent samples and use a supported broader reference where applicable; an
unsupported recent-team or subjective Gaussian/Poisson mixture stays diagnostic.
No new universal shrinkage size, confidence cap or small-sample cutoff is invented.

v4.12 is retired for new primary chat pricing. Preserve its originals and historical
grades as LEGACY_V412_DIAGNOSTIC, with a separate denominator. Never relabel v4.12 as
v24.15 or combine their probabilities as one method. A constant-0.5 Brier comparison
on repeated contracts is descriptive; game-level paired prospective evidence is
required for a predictive-advantage claim.

## 5. Source access and market-content exposure

Every chat receives the current reader-access decisions in its generated packet.
Check actual reader, host, exact path, observation/expiry times and redirects before
opening a page. BLOCKED and RULES_UNKNOWN mean use a permitted alternative or retain
UNAVAILABLE. A root allowance does not override a blocked path. Source refreshes use
the existing separately versioned, pinned access-update procedure; never edit an
old snapshot or infer that a later audit establishes an earlier access decision.

Prefer sporting statistics/official sources without predictions or odds. The owner's
stats-only exception remains: a permitted mixed-content page may supply only its
sporting fields. Record the URL, exact fields used, prediction/odds exposure status,
why a cleaner alternative was unavailable, and whether any predictive content was
actually seen. Do not claim that reading is independently verifiable when it is not.
No odds, tips, implied probabilities or third-party predictions enter calculations.
If predictive/outcome content contaminates the analysis, disclose it and exclude the
affected work from the applicable clean/prospective comparison; retain the original.

## 6. Hash-bound numeric contract review

Every new PICKS_V2 header includes:

```text
audit_policy: AUDIT-v1
audit_event_key: EV2-<native-fixture identity hash>
audit_review: research/contract_reviews/<local-key>/CONTRACT_REVIEW.csv
audit_review_sha256: <SHA-256 of the exact review file bytes>
```

Keep the review and its method/opponent/availability notes under research/contract_reviews/<local-key>/ (raw-byte Git custody is configured there). Generate a blank draft, then fill it from real evidence:

```text
python -m ml audit-controls template --mini MINI.md --key LOCAL-<MINI_KEY>-G0001 --out CONTRACT_REVIEW.csv
python -m ml card lint --mini MINI.md --key LOCAL-<MINI_KEY>-G0001
```

The exact CSV columns are printed by the template (`ml.audit_controls.FIELDS`).
There is one row per numeric PICKS label. UNPRICED contracts stay in the existing
UNPRICED block with reasons. Rows identify sport, competition, native fixture ID,
game number when applicable, participants, scheduled start with offset, date in that
stated offset, official schedule URL and observation time. A next-day rematch is a
different event. Use `external event-key` with competition/native ID/game number;
the resulting EV2 key is the `audit_event_key`. For an EXT event it also matches the
manifest event key. Never guess a native ID or reconcile a score by team names alone.

Method fields: `method_status: SUPPORTED_REFERENCE`, an explicit method ID, retained
repository-relative method/scope evidence and its byte SHA-256, actual positive n,
coverage fraction in (0,1], and uncertainty. This label means the existing reference
is supported for use; it does not mean calibrated skill has been demonstrated.
The existing reference/adjustment/receipt checks still apply independently.

Opponent fields: CHECKED, UNAVAILABLE or NOT_APPLICABLE, with evidence/reason.
Numeric plus handicaps require CHECKED and a retained `opponent_evidence` path with
its exact byte SHA-256. Every numeric row similarly binds its dated availability
review with `availability_evidence` and `availability_evidence_sha256`. Availability fields:
NO_MATERIAL_CHANGE_IDENTIFIED, MEASURED, UNQUANTIFIED or SCENARIO_ONLY, with evidence.
MEASURED requires `p_with`/`p_without` in [0,1] for that exact contract, an
`availability_effect_id` and its exact version from EFFECT_TABLES.csv. The current
row must be an admitted availability/player effect for this competition and target;
missing, superseded, null, unmeasured or unrelated effect rows are refused.
UNQUANTIFIED/SCENARIO_ONLY cannot supply primary numeric rows.
The checker validates structure, hashes and consistency; a human reviewer must still
verify the evidence establishes the claimed sporting fact/effect/scope.

The PICKS checker, external card append and ledger admission share this gate.
Do not bypass a refusal by omitting the policy or backdating issue time. If a needed
field cannot be established, retain research/UNPRICED/NO_FORECAST rather than guessing.

## 7. Final mini and associated-file handover

Record request time, research start/end and save/write time separately, using actual
offset-aware clocks. Preserve uncertain message-receipt times as unknown. Keep the
TIMING-v3 not-started observation URL/time and outcome-exposure declaration. A file
hash or typed timestamp is custody evidence, not independent publication proof.

Hand over the actual final cumulative mini, not a pre-append readback, a script,
a pasted rendering or a contents index. Every new card has matching BEGIN/END CARD
markers in its chat's own LOCAL namespace; no canonical IDs or borrowed namespaces.
Keep immutable originals, parented corrections and all associated files.

```text
python -m ml audit-controls handover --base FOLDER --mini FINAL_MINI.md --mini-key MINIKEY --writer CHAT_LABEL --files ASSOCIATED_1.md ASSOCIATED_2.csv --out HANDOVER.csv
python -m ml audit-controls verify-handover --base FOLDER --manifest HANDOVER.csv
```

Download/deliver every manifest member together. The receiving writer re-runs
verify-handover on the received files before settlement/import. Missing or changed
members stay MISSING_ORIGINAL, never reconstructed from their outputs. The manifest
records exact byte lengths, hashes, paths, card inventory and declared writer; it
does not grant a repository lease or certify publication. Never overwrite an earlier
handover. Duplicate games reconcile to one canonical event; preserve all originals.

## 8. Executable first-play review and effective scoring

TIMING-v3 still accepts research begun before actual first play and finished later.
Primary admission now requires the same URL/time/exposure declarations as the card
checker, and checks them against an available verified actual first-play time.
The input horizon remains unchanged. No forced early finish or 30-minute cutoff.

Before scoring a PRE_START_RESEARCH card, obtain the official actual first play,
retain its normalized sporting evidence under the repository, and append its review:

```text
python -m ml ledger correct-timing --key LOCAL-<MINI_KEY>-G0001 --actual-start ISO_WITH_OFFSET --source-url OFFICIAL_URL --evidence research/<event-folder>/FIRST_PLAY.csv --reason "Official first-play review"
python -m ml ledger score --results RESULTS.csv --out NEW_SCORE_FOLDER
```

FIRST_PLAY.csv has exactly `local_key,actual_start,source_url,observed_at,note` and
one normalized official fact. Its card, first-play time and URL must match the
correction; observation must be after first play and no later than the correction.
Audit the source before retrieving it. Preserve its raw capture externally and cite
that capture/lineage in the note. A machine checks consistency, not whether the
declared sporting source is truthful; the settlement reviewer verifies that fact.

`TIMING_CORRECTIONS.csv` is append-only and hash-chained. Each revision binds the
original card's ledger rows and evidence bytes. The scorer reads its effective
revision and exports TIMING_EFFECTIVE.csv. A valid reviewed PRE_START_RESEARCH card
joins the pooled PREGAME scoring group; research/observation inconsistent with first
play becomes POST_START_ISSUE. Until reviewed it is TIMING_UNVERIFIED in scoring.
A naked `timing` column in RESULTS.csv is not a verified revision. Broken chains,
changed evidence and stale ledger bindings refuse scoring. Correct mistakes by a
new evidenced revision; never edit the original card, ledger rows or an older review.

## 9. Learning and acceptance boundaries

Loss reviews produce registered hypotheses, not automatic parameter changes. Separate
facts known at the time from hindsight; descriptive leans are not issued bets. Count
unique games and disclose repeated contracts, copied sources and mixed methods.
All 21 match finals from the audited batch are recorded, but three corner-market
rows remain unresolved and some originals/source lineages remain missing. This
release does not close those queues or add any games to ASSESS-100 retrospectively.
