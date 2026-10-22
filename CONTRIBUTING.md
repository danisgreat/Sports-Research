# Contribution procedure

**Local keys until settlement; updated mini after every game (MINI-v2).** Defined in [MINI_LOG_IDENTITY_PROTOCOL](MINI_LOG_IDENTITY_PROTOCOL.md); summarised in [CORE](CORE.md) §2.

**Persistent research and corroboration (EXH-v1).** Defined in [RESEARCH_EXHAUSTIVENESS_PROTOCOL](RESEARCH_EXHAUSTIVENESS_PROTOCOL.md); summarised in [CORE](CORE.md) §5.

**Online history and confirmed players (HIST-2026.10.16-v3 / AVAIL-2026.10.16-v4).** Defined in [HISTORICAL_SOURCE_PROTOCOL](HISTORICAL_SOURCE_PROTOCOL.md); summarised in [CORE](CORE.md) §5.

**Required repository fallback (REF-v1).** Defined in [GITHUB_REFERENCE_PROTOCOL](GITHUB_REFERENCE_PROTOCOL.md); summarised in [CORE](CORE.md) §1.

**Google Drive (DRIVE-v2, optional).** Defined in [GOOGLE_DRIVE_EXCHANGE_PROTOCOL](GOOGLE_DRIVE_EXCHANGE_PROTOCOL.md); summarised in [CORE](CORE.md) §1.

**ML/RL scope (MLSCOPE-v3).** Defined in [FORECAST_CYCLE_PROTOCOL](FORECAST_CYCLE_PROTOCOL.md); summarised in [CORE](CORE.md) §7.

The repository holds Markdown, CSV and text only, with one exception: the maintainer model workshop `ml/` (Python source, tests and `requirements.txt`; CURRENT_RULES §0). Do not add code anywhere else, and never add JSON, notebooks, pickles, workflow files or binary data. A framework change is a change to documents; a workshop change must keep `python -m pytest ml/tests` passing, and any regenerated file under `research/model_shadow/` must come from an actual run whose receipt it carries. **Helpers and captures (2026-10-12, R07):** a script used to transform data, and raw captures (HTML pages, source CSVs carrying odds, API dumps), stay **outside** the repository folder. Record each capture's URL, capture time and SHA-256 in the change folder's receipt, and write the transformation rules out in prose in the dataset's `DATA_PROVENANCE.md`, so that a reader can check them by hand. Never stage a whole directory to "clean" a working tree, and never delete another writer's files; move unpublished work to a named quarantine folder outside the repository and list it there. Read [CURRENT_RULES.md](CURRENT_RULES.md) and [CURRENT_STATE.md](CURRENT_STATE.md) first. The pre-rewrite procedure is kept in [archive/superseded_2026-10-09/CONTRIBUTING.md](archive/superseded_2026-10-09/CONTRIBUTING.md).

1. **Inventory first.** Run `git status` and `git log -3`. Note branch, HEAD and any uncommitted work that is not yours. Preserve it; never overwrite unrelated edits.
2. **Preserve originals.** Never edit an issued card, a settled mini, a Combined Log above its end marker, a preserved original in `research/issued_research/`, or a dated verification report. Corrections are dated addenda. If a document must change, copy the old text into `archive/` in the same commit.
3. **Keep contracts explicit.** Identity, endpoint and time stay explicit. Never replace missing data with a guess or a q with a probability.
4. **Sources.** Use the routes in [SOURCES.md](SOURCES.md); record source failures and unknown independence. Keep odds-bearing material out.
5. **Check by hand.** Run the checklist matching your change ([VERIFICATION_PROTOCOL.md](VERIFICATION_PROTOCOL.md) §§2–6) and print evidence. A touched log must retain its entire original byte prefix with changes only at its end; zero deleted lines in numstat alone is insufficient.
6. **Rule or prompt changes.** Align changed versions across METHOD, CURRENT_RULES, CURRENT_STATE, templates and examples; archive originals and add CHANGELOG and implementation/verification records. Preserve original hypothesis registrations and append amendments. User-authorized integrity changes do not require invented statistical proof; predictive effects remain untested until the registered comparison succeeds. Never change a predictive rule on one result.
7. **Publish deliberately.** Inspect the full diff, stage only intended files by path, verify the remote and a clean state before claiming publication. Do not push over someone else's work and do not force-push. No publication is implied by a local edit.

Verify archived source length and coverage before deleting any redundant working mini, and keep unique archive bodies and audit evidence. Scientific and process failures must be visible; a green check shows only what it checks.

Owner primary-model exception (15 October 2026; narrowed by MLSCOPE-v1 to prompts 6 and 8): code still only under ml/; source-reviewed normalized market-free input and immutable output/feedback CSV/Markdown may be written under the named research/primary_predictions/ event folder, under PRIMARY_PREDICTION_PROTOCOL. Preserve source captures externally and existing issued cards; test actual primary inference and delayed sporting feedback, not just prompt wording.

Historical-source procedure: HISTORICAL_SOURCE_PROTOCOL permits game-card collection/reconciliation of reviewed normalized sporting web inputs in the named mini/primary evidence scope. It does not authorize silent shared archive/profile edits or historical card rewrites. Archive repairs use prompt7 with preserved originals and field-level provenance.

**Research retention before model availability (RETAIN-v2).** Defined in [RESEARCH_RETENTION_PROTOCOL](RESEARCH_RETENTION_PROTOCOL.md); summarised in [CORE](CORE.md) §2.

Authorized retention-only import may precede settlement. Retain source cores and verify the canonical prefix/ID mapping. Code remains only in ml/; reviewed future-label candidates may be retained as text/CSV under research/training_candidates/.

**Learning pipeline (LEARN-v1).** Code stays in `ml/`. The permitted CSV/Markdown learning locations are `research/learning_store/` (append-only; written only by `python -m ml ingest add` in prompt 4 or an authorised prompt 8 change), `research/training_releases/` (immutable), `research/prospective/SHADOW_LEDGER.csv` and `research/model_registry/MODEL_REGISTRY.csv` (hash-chained, append-only) and `research/learning_status/REVIEW_LOG.csv` (append-only). Never hand-edit them; captures stay outside the repository with path and hash recorded. Run `python -m pytest ml/tests` before publishing any ML change. Continuous integration via a workflow file, and branch protection, remain owner decisions (workflow files are prohibited above). See [LEARNING_PIPELINE_PROTOCOL](LEARNING_PIPELINE_PROTOCOL.md).
