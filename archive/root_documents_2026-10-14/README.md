# Historical root-document archive — 14 October 2026

**Status: historical reference only.** User-authorised archival of the ten root files marked ARCHIVE in the review. These specifications, audits, ledgers and receipts do not override [current rules](../../CURRENT_RULES.md) or [current state](../../CURRENT_STATE.md). No runtime or certification system is restored.

**Preservation:** all ten Markdown originals retain the exact pre-move working bytes and text. Git uses the same LF-normalised committed representation as their original root blobs (the separate raw-working and committed hashes below make the distinction explicit). Original relative links were written for a repository-root location and are deliberately not rewritten inside preserved evidence. Use [LINK_RECOVERY.md](LINK_RECOVERY.md) for navigable targets, including existing legacy missingness. Frozen incoming references can be recovered through [HISTORICAL_LINK_INDEX](../../HISTORICAL_LINK_INDEX.md#root-document-archive-2026-10-14).

**Base commit:** `5d754a426e0d864db314b88a818036a039cf255e`. **Change class:** EDITORIAL; method/control/scoring/selection/prompt versions unchanged.

| Archived original | Why it left the root |
|---|---|
| [DATA_SOURCE_REGISTER.md](DATA_SOURCE_REGISTER.md) | Suspended runtime-ingestion/source specification; current source routes are in SOURCES.md. |
| [FRAMEWORK_RETROSPECTIVE_2026-10-09.md](FRAMEWORK_RETROSPECTIVE_2026-10-09.md) | Dated retrospective and implementation evidence; code-based recommendations were subsequently suspended. |
| [H0_DATASET_CARD.md](H0_DATASET_CARD.md) | Suspended H0 training/feature-store specification; not an implemented current dataset. |
| [IMPLEMENTATION_2026-10-01.md](IMPLEMENTATION_2026-10-01.md) | Dated implementation report for removed runtime, pipelines, registries and CI. |
| [MARKET_BENCHMARK_LEDGER.md](MARKET_BENCHMARK_LEDGER.md) | Empty legacy closing-market comparison design; retained as historical documentation. |
| [NUMERICAL_MODEL_REGISTER.md](NUMERICAL_MODEL_REGISTER.md) | Suspended numerical portfolio/promotion specification; no runtime restored. |
| [PIPELINE_IMPLEMENTATION_2026-09-29.md](PIPELINE_IMPLEMENTATION_2026-09-29.md) | Superseded September pipeline plan and historical release gates. |
| [RECORD_ELIGIBILITY_SCHEMA.md](RECORD_ELIGIBILITY_SCHEMA.md) | Suspended certification/eligibility design; current research lifecycle is elsewhere. |
| [SKILL_BASELINE_LEDGER.md](SKILL_BASELINE_LEDGER.md) | Historical seed evaluation and prospective protocol; original observations retained. |
| [VERIFICATION_RECEIPT_2026-09-28.md](VERIFICATION_RECEIPT_2026-09-28.md) | Dated September 28–29 execution receipt, retained as evidence rather than current procedure. |

## Custody inventory

| File | Raw working bytes | Raw working SHA-256 | CRLF / total LF | Prior committed bytes | Prior committed SHA-256 |
|---|---:|---|---|---:|---|
| `DATA_SOURCE_REGISTER.md` | 9565 | `ccbef3040f071a3fb5c70fdd701284c7e92204006356f030f1b55d57140133a1` | 105 / 105 | 9460 | `1cf9f2b3dfe56036e90a816fc1d7a08d72b8ed02ec3845431e99cd68be963280` |
| `FRAMEWORK_RETROSPECTIVE_2026-10-09.md` | 62359 | `dbeae08b35b9cf226f0a8fbdbdb4488b33d86255ce6399226eaa4413619ff2cb` | 0 / 420 | 62359 | `dbeae08b35b9cf226f0a8fbdbdb4488b33d86255ce6399226eaa4413619ff2cb` |
| `H0_DATASET_CARD.md` | 6952 | `7c195d53185e14bb1302ce6dcb23b5712c94e5b8e7fbbde2e2e303886a39b5e6` | 0 / 98 | 6952 | `7c195d53185e14bb1302ce6dcb23b5712c94e5b8e7fbbde2e2e303886a39b5e6` |
| `IMPLEMENTATION_2026-10-01.md` | 24291 | `f90709276279516014b783f966298748442cf81dd00af8dfd45811ee298f5c2e` | 183 / 183 | 24108 | `18cfeb14f5ea2e5e6ee2fe76381380686a8a6709701c9e2629c08dfdf8d8d803` |
| `MARKET_BENCHMARK_LEDGER.md` | 5013 | `cbc09e4d7d521ab7b23fecb1c11a6f794d5daf5eef1049992566d723f044ecc9` | 38 / 38 | 4975 | `276438d5d0213dc00053a3db441fd4c7515421d295b5c623f25db5d39d9ccaee` |
| `NUMERICAL_MODEL_REGISTER.md` | 17171 | `d5cae71eb72c45b092261824fcc05042fde2d3b44b64c56ec5c0e13b582b1658` | 0 / 156 | 17171 | `d5cae71eb72c45b092261824fcc05042fde2d3b44b64c56ec5c0e13b582b1658` |
| `PIPELINE_IMPLEMENTATION_2026-09-29.md` | 11281 | `15cd8769c65fae2ccc155b292373189cab1825dc2b0979106ff34b693feaa4de` | 59 / 59 | 11222 | `88b547fc40f1e8dce163646750c9f75eda36f034bb426d7980a105c818dc12be` |
| `RECORD_ELIGIBILITY_SCHEMA.md` | 5112 | `67d02a4d57d418b8b3d814d0d55bb1a506bad2e6613783c9d5baf48c47fb7ba5` | 29 / 29 | 5083 | `a57ce978b1d3d5b04621d355f03b73455c29f0279789c100a4e6efddf44cf448` |
| `SKILL_BASELINE_LEDGER.md` | 14289 | `52f2e405ae9ea65ad555b2a88bcb9a157b701a278e5d171c9c8bf972ab2b92af` | 125 / 125 | 14164 | `d6fb6d55e32716398618f14b178bc65034c34a73ceb365896f4ead8cae358072` |
| `VERIFICATION_RECEIPT_2026-09-28.md` | 15601 | `e0f72fc11629823a41e3c4ae75f288def95b7852ea6d662a1df7847cdf341d1d` | 94 / 94 | 15507 | `4ac7af417eb4247a7363ee16eff03f1040f9f6667f57119a0b2080f9941b3b62` |

## Navigation before this change

The six before-edit root documents are preserved in `navigation_before/`. They are snapshots, not a second operating authority. Their relative links also use the original root context and are covered by LINK_RECOVERY.

- [README.md](navigation_before/README.md)
- [ACTIVE_FILE_INDEX.md](navigation_before/ACTIVE_FILE_INDEX.md)
- [CURRENT_STATE.md](navigation_before/CURRENT_STATE.md)
- [HYPOTHESIS_REGISTER.md](navigation_before/HYPOTHESIS_REGISTER.md)
- [HISTORICAL_LINK_INDEX.md](navigation_before/HISTORICAL_LINK_INDEX.md)
- [CHANGELOG.md](navigation_before/CHANGELOG.md)

[Implementation and verification receipt](../../research/verification/root_document_archive_2026-10-14/ARCHIVE_RECEIPT.md).
