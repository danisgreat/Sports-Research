# Control manifest — 2026-09-25 (post-audit-closure content receipt)

Method: **MDS-2026.09.19-v4.3**
Control revision: **CR-2026.09.21-3** (label unchanged; this follows the 2026-09-23 precedent of a content receipt under the same label)
Status: **CURRENT post-write content receipt**, generated 2026-09-25 about 01:00 AEST after the audit closure (Part 5 §"2026-09-25(a)"–"(b)"; `archive/audit_documents_implemented_2026-09-25/AUDIT_CLOSURE_LEDGER_2026-09-25.md`).

**Purpose.** This is the byte-level SHA-256 receipt that every new card freezes (`METHOD.md` header; PF-7). Relative to `CONTROL_MANIFEST_2026-09-23.md` it adds:
- the 2026-09-24(f) settlement-integrity controls: `C-PROCESS-RECORD-PROVENANCE`, `C-LINEUP-DIFF`, S-1 Rev 2 receipt enforcement, `G-L22(c) COVERING_PAIR`, `C-SUMMARY-FROM-CARD`, `C-PROMOTION-RECEIPT` and MLB gamefeed weather;
- the 2026-09-25 audit-closure implementations: cricket control 19–21 extensions, tennis `TE-P5`/`TE-S2`/`TE-S4` and §9.4, the METHOD §12 wording correction, METHOD field 5 and §7, SCORING §3 and §12, the preflight `participants` object, and the audit-script repair and extension.

**It does not change any forecasting coefficient, probability cap or ranking override.** Run the audit script with `--strict` for cards issued or settled against this manifest.

This manifest is excluded from its own hash table.
- `CONTROL_MANIFEST_2026-09-23.md` remains the receipt for P-495–P-509.
- `CONTROL_MANIFEST_2026-09-21-3.md` remains the receipt for cards issued before 2026-09-23 about 22:00 AEST.
- The two living logs (`PREDICTION_LOG_COMBINED_5.md`, `GAME_LOG_STATUS_CURRENT.md`) are hashed as a write-time snapshot and change with every card.
- The two archived audit files and the closure ledger are hashed at their new archive paths.

**Changed since 2026-09-23 (by bytes):** `README.md`, `METHOD.md`, `CONTROLS.md`, `RULES_GENERAL.md`, `SOURCES.md`, `DATA_SOURCE_REGISTER.md`, `UPCOMING_GAME_RESEARCH_GUIDE.md`, `SCORING_AND_VALIDATION.md`, `PERFORMANCE_ELIGIBILITY_POLICY.md`, `LEARNING_REGISTER.md`, `AGENT_ROLE_AND_TASK.md`, `EXTERNAL_LOGGING_WORKFLOW.md`, `FORECAST_PREFLIGHT_MANIFEST.md`, `RULES_BASEBALL.md`, `RULES_CRICKET.md`, `RULES_SOCCER.md`, `RULES_BASKETBALL.md`, `RULES_AFL.md`, `RULES_NRL_RUGBY.md`, `RULES_RUGBY_UNION.md`, `RULES_AMERICAN_FOOTBALL.md`, `RULES_ICE_HOCKEY.md`, `RULES_TENNIS.md`, `prediction_preflight.py`, `test_prediction_preflight.py`, `audit_card_controls.py`, `NUMERICAL_PROGRAM.md`, `MODEL_AND_DATA_SPEC.md`, `ALGORITHM_PORTFOLIO_AND_EVALUATION.md`, `BASE_RATES_REGISTER.md`, `GAME_LOG_STATUS_CURRENT.md`, `PREDICTION_LOG_COMBINED_5.md`.

**New in the receipt:** `test_audit_card_controls.py`, `archive/audit_documents_implemented_2026-09-25/AUDIT_CLOSURE_LEDGER_2026-09-25.md`.

## SHA-256 file receipt

| File | SHA-256 | Bytes |
|---|---|---:|
| `README.md` | `b7e01a7cf8704cf436648932766bc1df6f729644354317c3dbd13482ec76a9fc` | 22660 |
| `METHOD.md` | `21843f33feb6bb7d973ebf3fa2d03559a6684e4a6043945331af78964a6151c1` | 25939 |
| `CONTROLS.md` | `fe28ef731ead3f4b195f10b7fac9954cfea83e1a47e1df0f6f37c20d8760d4e3` | 30816 |
| `RULES_GENERAL.md` | `41e6f02234610d3aadb21c6a058ebf196a8d99a500ad32d09304ef0418327127` | 235051 |
| `SOURCES.md` | `2e10bc4ef6a528508e775ec05ebb01d2b6328ea4dfa15528a3027b996b56c162` | 73473 |
| `DATA_SOURCE_REGISTER.md` | `088d1d4a7a6944a31fc5e236757c58673d805092083f72cad9225b4ab86ff0de` | 170374 |
| `UPCOMING_GAME_RESEARCH_GUIDE.md` | `9135ada8e2070b589fdb8022ec112338a07127e2e71e65186238c80365ac318e` | 67745 |
| `SCORING_AND_VALIDATION.md` | `896765f9d462f529729c1493ae366ecca113ffc987d8a6388efce5b0eb781e04` | 16355 |
| `PERFORMANCE_ELIGIBILITY_POLICY.md` | `cd6740823a310a557d96c371051a9742c2d78e40e34ef918b3c64d46e9400549` | 18879 |
| `LEARNING_REGISTER.md` | `d6c53b2947400aabac5420e81b3af035d7216cfa53cea5bbe48b197d8d37e94b` | 287367 |
| `AGENT_ROLE_AND_TASK.md` | `90a5caefedd2ca046f187c5ecdd8aeda646ceab871a7fdc1b0f797ac462fe523` | 22825 |
| `EXTERNAL_LOGGING_WORKFLOW.md` | `41dba92159b80de99a1661a1334a4769f961d47c600609dd45b72d0531f831bf` | 61761 |
| `FORECAST_PREFLIGHT_MANIFEST.md` | `34718b2faca3276e7213bc622e01ff06998151390f5f7c3f12497082e7468678` | 9309 |
| `RULES_BASEBALL.md` | `6202025cb37619428c0131574294fc94cca945b150f50dabfe1d106fb6bed9ee` | 120540 |
| `RULES_CRICKET.md` | `5b8dda3f1bd7b33255b03d91730d30600cec2db58182db223a215295993afb4b` | 101945 |
| `RULES_SOCCER.md` | `531b283a1edd894ed0f891c431ad8a141de8713a39a46cc66d7b173b2ca7d27c` | 97217 |
| `RULES_BASKETBALL.md` | `070537eead901d950cd53b2134e74fe4ed228cfb38ab67d0857fe5b3542e6a19` | 89701 |
| `RULES_AFL.md` | `ba16d1de889dcb7704e1035b42c3439ab256e9517481df0edd6a7884908ab081` | 55918 |
| `RULES_NRL_RUGBY.md` | `b6acc1208ea9e9b770b4c2cf8efb3b39ba83ec56e685dfefcbcc06ea930a2ea1` | 54722 |
| `RULES_RUGBY_UNION.md` | `57d4108f24dfc854691f0bd0d400c8603fc8a03c812537478f7a5e0982890adf` | 49313 |
| `RULES_AMERICAN_FOOTBALL.md` | `d58be31e864287d19101ec16d44ae1144f1e11e65f4f4f10fce073a97405a451` | 59828 |
| `RULES_ICE_HOCKEY.md` | `dd29dd52452a69b0594d519d7b6338038353f2f3c7a04cc4a373b5a2b70703d4` | 51778 |
| `RULES_TENNIS.md` | `d7478b60babbcfc7aef70d070702f05fd5f27f6ddd102b36d2244d4e836b8252` | 65665 |
| `LEAGUE_RULES_CRICKET.md` | `b6b13dfa72047b62fd9987e21daa0ec25510ab0853ebbac461b5725de5f99099` | 26252 |
| `LEAGUE_RULES_SOCCER.md` | `236463054f21792ad091fd3f326c7cb12aac767c933ffc4bd2e265acf55df06b` | 43865 |
| `prediction_preflight.py` | `b4d07fef54e71ef8478c5b2cec3af15c5f5accf50ba3e703348ab16609006d26` | 29319 |
| `test_prediction_preflight.py` | `c91ef73ac3faa420e3b67f8e5f345a851c4f9a69e43e75c21be6d3c7a53d5d60` | 11403 |
| `audit_card_controls.py` | `a066ee7e74c80799c73def7123954d6d55f07cbe8dc47310c745cc05d161d98a` | 24951 |
| `test_audit_card_controls.py` | `92843b91c03f1a8211ba432a1c251db6493afc7b2d98d910810da5f23a157962` | 7685 |
| `H0_DATASET_CARD.md` | `a2d44c60788d0506c1108e1629fb2a2e6ac23d6fc41ca87c2e27a6d138152278` | 19413 |
| `NUMERICAL_PROGRAM.md` | `35687ad192cc363be06f0436148fb6e97a9426f7653fed15308f14c07c214208` | 9659 |
| `NUMERICAL_MODEL_REGISTER.md` | `7fe3f9ecfb51f0e0519ef8d91a857b0038393cdb2546fd2a1b3ee52966aef968` | 22540 |
| `NUMERICAL_TRAINING_SPEC.md` | `888fa925485a64642443b7555d8a989aea955d0a7997e23a09edef7db93bbd37` | 31309 |
| `MODEL_AND_DATA_SPEC.md` | `c4d77b5036afbe531387886ee460d35a47ba6d824bf5a13077f20d7c9906b771` | 64024 |
| `ALGORITHM_PORTFOLIO_AND_EVALUATION.md` | `c0dbea56b78a51c5f6a075d7e0ace6e0d84a4fe97a1366cd699624e5783f49aa` | 51138 |
| `MODEL_IMPLEMENTATION_RECIPES.md` | `f016aa31c039dd95152f36a6df56d2758c2769b146b73bd8b8a43fa18e02021c` | 20837 |
| `RECENCY_AND_REBOUND.md` | `58234fa4c0f3babe29f3c3ba94479ac91f441d1e097cf6750daa7c3316bba9bc` | 11914 |
| `BASE_RATES_REGISTER.md` | `3c5d335de047e46ef11381beda2208d9ffd446de1a7ea9bdb2c96b6ceda35939` | 13615 |
| `GAME_LOG_STATUS_CURRENT.md` | `fd70a1c542b59f24a6d915ebac8ef5b2f106a6bf0a7749a4cd0dce3b8624de32` | 135057 |
| `PREDICTION_LOG_COMBINED_5.md` | `a8ca59fb46755b60f3c29baf0d03ca5d5ad604421c5589e5078a875a9e75cf74` | 890542 |
| `archive/audit_documents_implemented_2026-09-25/AUDIT_RECONCILIATION_ALL_SPORTS_2026-09-21.md` | `4cc9ca4c2da51dae05ea01ff864b86c99b273f2ec2cb3347613b776167ab2621` | 14968 |
| `archive/audit_documents_implemented_2026-09-25/AUDIT_IMPLEMENTATION_2026-09-21-CR3.md` | `3ce923f087fc42f5a42fc86ea6d23b2122f75b63be38c3bf2bd19cf66402b978` | 6320 |
| `archive/audit_documents_implemented_2026-09-25/AUDIT_CLOSURE_LEDGER_2026-09-25.md` | `dac68b1b91b13bd8fb3786696edc72d2e07a951723e88b4b83391a9887d43ef9` | 16117 |
