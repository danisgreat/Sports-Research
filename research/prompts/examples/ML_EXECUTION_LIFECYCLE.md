# mini-log-8 / mini-settlement-7 execution lifecycle example

**Online history and confirmed players (HIST-2026.10.16-v2 / AVAIL-2026.10.16-v3).** For every game, research both sides' L5/L10/L15/L20 online under [HISTORICAL_SOURCE_PROTOCOL](../../../HISTORICAL_SOURCE_PROTOCOL.md), with opened sources, dated game rows and true n. Seek exact-game confirmed players, starting roles, bench/replacements and absences under [ROSTER_AVAILABILITY_PROTOCOL](../../../ROSTER_AVAILABILITY_PROTOCOL.md); projected players remain unconfirmed. The retired local results store and its derived profiles are not required inputs or fallbacks. Earlier archive-first directions are superseded.

FORMAT EXAMPLE ONLY / NOT_ISSUED / NOT_IMPORTABLE. Tokens below describe required fields, not an executed sporting forecast. Actual synthetic CLI evidence is listed in the [release verification report](../../verification/framework_change_2026-10-15-7/VERIFICATION_REPORT.md). Preserved earlier manual examples retain mini-log-7 and their original hypothetical numbers.

Create a new mini using [template section 2](../../../CARD_AND_LOG_TEMPLATES.md) with `MINI-LOG-FORMAT: mini-log-8`, a valid authority/lease, empty intake/cards and a header-only ML_EXECUTION_MANIFEST.csv. Creation has zero model attempts and consumes no event ID. `verify-log` should report zero cards/executed/failed/feedback.

For an EXAMPLE event in a competition lacking a profile/archive route, research exact history and sporting metadata. Prepare REQUEST/HISTORY/CONTRACTS/COMPETITION_SOURCE CSVs with the schemas in [the primary protocol](../../../PRIMARY_PREDICTION_PROTOCOL.md). Actually run `primary execute` with those paths. No baseline probability is supplied. The successful route fits its own league grid, team experts and Hedge mixture; the actual attempt's `BUNDLE/PREDICTIONS.csv` contains `p_card` and `baseline_p`. Copy only real values, hashes and counts into the original card.

```text
- **ML execution identity:** EXAMPLE-EVENT | Basketball/EXAMPLE | FULL_GAME_INCL_OT
- **ML execution:** EXEC-v1; <actual attempt/EXECUTION.csv and computed SHA-256>; <actual status>; <manifest row and check output>
- **Learning:** <actual warm/feedback counts, weights and eta from BUNDLE/RECEIPT.csv>
```

Append the same identity and attempt path/hash to the manifest using its registered header. At issue, use PENDING_EVENT with actual event-state evidence and next action. Run `verify-log` on the complete new mini. Never copy these placeholder strings into a real receipt or use an EXAMPLE ID as a canonical P-ID.

If execution really fails because metadata, history, model support or fit is insufficient, retain its FAILED receipt/error. Complete substantive research and use a nonnumeric primary disposition; supported analyst calculations remain NOT_PRIMARY. The manifest uses NOT_APPLICABLE_NO_MODEL with the actual failure reason. A missing execution receipt is not equivalent to a retained failed execution. An unavailable execution environment stays INCOMPLETE, never a fabricated successful run.

At settlement, freeze the exact original mini/manifest and source bundles. Create a mini-settlement-7 package. For a successful eligible terminal bundle actually run `primary settle`, retain the resulting feedback hash and reconcile its effective revision. Copy the original manifest into a new effective manifest and change the row to FEEDBACK_RETAINED only after that output exists and verifies. If a required terminal field is unresolved, use BLOCKED_WITH_EVIDENCE and the exact gap/owner; if not terminal, keep PENDING_EVENT. Missing baseline scores never justify skipping otherwise supported feedback.

Run `verify-log` against the frozen mini and effective manifest, C21/S16 and existing settlement checks. The next event's `execute --feedback` consumes only this real, available, matching-policy feedback. Import preserves the old and effective manifests and all referenced custody paths/hashes; it does not rewrite original cards or turn an EXAMPLE into a live record.
