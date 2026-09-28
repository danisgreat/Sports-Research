# Control manifest — 2026-09-25-2 (post-research-pass content receipt)

Method: **MDS-2026.09.19-v4.3**
Control revision: **CR-2026.09.21-3** (label unchanged; this follows the 2026-09-23 and 2026-09-25 precedent of a content receipt under the same label)
Status: **CURRENT post-write content receipt**, generated 2026-09-25 about 01:20 AEST after the research pass (Part 5 §"2026-09-25(c)"; `RULES_GENERAL.md` §"2026-09-25(b)").

**Purpose.** This is the byte-level SHA-256 receipt that every new card freezes (`METHOD.md` header; PF-7). Relative to `CONTROL_MANIFEST_2026-09-25.md` it adds the 2026-09-25(b) research-pass material:
- the derived reference rates: `BASE_RATES_REGISTER.md` §7 and `RECENCY_AND_REBOUND.md` §7;
- the controls `C-WIDTH-BENCHMARK`, `C-WIDTH-Z`, `C-RECEIPT-TOOL` and `C-HCP-COHERENCE`, the early-season and regime references, and the `R-1` one-game corollary;
- a §"2026-09-25(b)" in each sport file, and the guide, workflow and agent-role steps;
- the tools: `receipts.py` with `test_receipts.py`, and `audit_card_controls.py` fields `WB`, `HC` and `10z`;
- the re-runnable research folder `research/base_rates_2026-09-25/` (queries, scripts, result JSON).

**It does not change any forecasting coefficient, probability cap or ranking override.** Run the audit script with `--strict` for cards issued or settled against this manifest. `WB`, `HC` and `10z` apply from this manifest onward.

This manifest is excluded from its own hash table.
- `CONTROL_MANIFEST_2026-09-25.md` was current from the audit closure until this pass. No card was issued under it: the P-510 mini log was empty throughout.
- `CONTROL_MANIFEST_2026-09-23.md` remains the receipt for P-495–P-509.
- `CONTROL_MANIFEST_2026-09-21-3.md` remains the receipt for cards issued before 2026-09-23 about 22:00 AEST.
- The two living logs (`PREDICTION_LOG_COMBINED_5.md`, `GAME_LOG_STATUS_CURRENT.md`) are hashed as a write-time snapshot and change with every card.

**Line endings.** Every hashed text file is hashed in its CRLF working-tree form, which is what a `core.autocrlf=true` checkout produces. Twenty files written LF-only during the 2026-09-25 passes were converted to CRLF before hashing; their content is unchanged, and git stores LF either way. The earlier `CONTROL_MANIFEST_2026-09-25.md` hashed `audit_card_controls.py` and `GAME_LOG_STATUS_CURRENT.md` in LF form, so a fresh checkout would not have reproduced those two hashes. On a system that checks out LF, re-hash after converting to CRLF.

**Changed since CONTROL_MANIFEST_2026-09-25 (by bytes):** `README.md`, `METHOD.md`, `CONTROLS.md`, `RULES_GENERAL.md`, `SOURCES.md`, `DATA_SOURCE_REGISTER.md`, `UPCOMING_GAME_RESEARCH_GUIDE.md`, `LEARNING_REGISTER.md`, `AGENT_ROLE_AND_TASK.md`, `EXTERNAL_LOGGING_WORKFLOW.md`, `RULES_BASEBALL.md`, `RULES_SOCCER.md`, `RULES_BASKETBALL.md`, `RULES_ICE_HOCKEY.md`, `RULES_TENNIS.md`, `audit_card_controls.py`, `test_audit_card_controls.py`, `RECENCY_AND_REBOUND.md`, `BASE_RATES_REGISTER.md`, `GAME_LOG_STATUS_CURRENT.md`, `PREDICTION_LOG_COMBINED_5.md`, `archive/audit_documents_implemented_2026-09-25/AUDIT_CLOSURE_LEDGER_2026-09-25.md`.

**New in the receipt:** `receipts.py`, `test_receipts.py`, `research/base_rates_2026-09-25/README.md`, `research/base_rates_2026-09-25/analyze_extra.py`, `research/base_rates_2026-09-25/analyze_leagues.py`, `research/base_rates_2026-09-25/analyze_mlb.py`, `research/base_rates_2026-09-25/analyze_more.py`, `research/base_rates_2026-09-25/analyze_nhl.py`, `research/base_rates_2026-09-25/analyze_nhl_pre.py`, `research/base_rates_2026-09-25/analyze_tennis.py`, `research/base_rates_2026-09-25/extra_results.json`, `research/base_rates_2026-09-25/fetch.py`, `research/base_rates_2026-09-25/league_results.json`, `research/base_rates_2026-09-25/mlb_results.json`, `research/base_rates_2026-09-25/more_results.json`, `research/base_rates_2026-09-25/nhl_results.json`, `research/base_rates_2026-09-25/pooled_checks.py`, `research/base_rates_2026-09-25/pull_all.py`, `research/base_rates_2026-09-25/pull_more.py`, `research/base_rates_2026-09-25/pull_nhl_pre.py`, `research/base_rates_2026-09-25/pull_nhl_tennis.py`, `research/base_rates_2026-09-25/tennis_results.json`.

**Unchanged:** 21 files.

## SHA-256 file receipt

| File | SHA-256 | Bytes |
|---|---|---:|
| `README.md` | `de87d626e46c900bce63e3825263acf3f4800fcacbdda0ed7f5736ee4be2d9d0` | 25942 |
| `METHOD.md` | `5f0cd61b7e0354897828182b7234a9b196d943a184a26812fa97d4def62b39bd` | 26636 |
| `CONTROLS.md` | `b0e9ad79a95071424e486b0c64cf1e878344d76cfe21f1bc911f78b1cac02da8` | 33110 |
| `RULES_GENERAL.md` | `6be72b0d1f20e7c6cb39184a10e07924cdb2205292b424e731948053490729ef` | 242629 |
| `SOURCES.md` | `d61d60ff50b77bbffd5c8d7aca92060b13a60cd2283a5b0cf9f79df771fdbd60` | 74808 |
| `DATA_SOURCE_REGISTER.md` | `7fec3e934a43e2a0e434f9d08571b2bb48d92142a36035bcc382f1f8a24b70a1` | 175090 |
| `UPCOMING_GAME_RESEARCH_GUIDE.md` | `9122fcafc39d59887187524415da04941b6bd0a169deaf2e2637e636dd3a5e84` | 70060 |
| `SCORING_AND_VALIDATION.md` | `896765f9d462f529729c1493ae366ecca113ffc987d8a6388efce5b0eb781e04` | 16355 |
| `PERFORMANCE_ELIGIBILITY_POLICY.md` | `cd6740823a310a557d96c371051a9742c2d78e40e34ef918b3c64d46e9400549` | 18879 |
| `LEARNING_REGISTER.md` | `b99ec02e8cdef4d0760f3de307b55ce1a2d0a6a7b46cdbf3fe9b678f3abf3147` | 293653 |
| `AGENT_ROLE_AND_TASK.md` | `867d83b8735d69662ec0e2329edf060c9578dc62c038702888cb907da4ed2b47` | 23660 |
| `EXTERNAL_LOGGING_WORKFLOW.md` | `260a78378130523ee0b0c98cc93417dd0bcfad514196bf090ec4c2bd8cbd1a57` | 63353 |
| `FORECAST_PREFLIGHT_MANIFEST.md` | `34718b2faca3276e7213bc622e01ff06998151390f5f7c3f12497082e7468678` | 9309 |
| `RULES_BASEBALL.md` | `2a0f921d0c787cf2d95b0d68ebcd8cea430ae27bfb9b0d2c41dacee0d938f8c9` | 123340 |
| `RULES_CRICKET.md` | `5b8dda3f1bd7b33255b03d91730d30600cec2db58182db223a215295993afb4b` | 101945 |
| `RULES_SOCCER.md` | `a73290009da43766878f19a13c7a4df401979869673f3757d05b0f25c2a6a92a` | 99280 |
| `RULES_BASKETBALL.md` | `5d440b9236e6ae2c360b36d17c49eae512f693adda36b7fc38d5ae8c7bc33f49` | 93817 |
| `RULES_AFL.md` | `ba16d1de889dcb7704e1035b42c3439ab256e9517481df0edd6a7884908ab081` | 55918 |
| `RULES_NRL_RUGBY.md` | `b6acc1208ea9e9b770b4c2cf8efb3b39ba83ec56e685dfefcbcc06ea930a2ea1` | 54722 |
| `RULES_RUGBY_UNION.md` | `57d4108f24dfc854691f0bd0d400c8603fc8a03c812537478f7a5e0982890adf` | 49313 |
| `RULES_AMERICAN_FOOTBALL.md` | `d58be31e864287d19101ec16d44ae1144f1e11e65f4f4f10fce073a97405a451` | 59828 |
| `RULES_ICE_HOCKEY.md` | `a58401086cb63d3996051c5c7cf07df4b9c702f2f7d4db8a6d7704f6482c8b80` | 54593 |
| `RULES_TENNIS.md` | `ac0cd7453d76de12f4d8d9572aad834b8dc3b02b25c1a04355529a253abd6d5a` | 68817 |
| `LEAGUE_RULES_CRICKET.md` | `b6b13dfa72047b62fd9987e21daa0ec25510ab0853ebbac461b5725de5f99099` | 26252 |
| `LEAGUE_RULES_SOCCER.md` | `236463054f21792ad091fd3f326c7cb12aac767c933ffc4bd2e265acf55df06b` | 43865 |
| `prediction_preflight.py` | `b4d07fef54e71ef8478c5b2cec3af15c5f5accf50ba3e703348ab16609006d26` | 29319 |
| `test_prediction_preflight.py` | `c91ef73ac3faa420e3b67f8e5f345a851c4f9a69e43e75c21be6d3c7a53d5d60` | 11403 |
| `audit_card_controls.py` | `81f6cfe0ba8f2516c8cf1cf7fa5a26447b296945ce9ee97f7015323d2a23549c` | 27876 |
| `test_audit_card_controls.py` | `cef1fe2aa46a487df277adb11eada2aae29ef5c4edbeda6e16b49ef2b25f619a` | 11079 |
| `receipts.py` | `33c906e5b6a0f67ffaf103347f058955401923a3cb57ee43158cd7f2d1b3de30` | 21886 |
| `test_receipts.py` | `c841b495300f0e7e7afec7f4b24b1780c6a879b0067ed5b648a800625cee3c08` | 6502 |
| `H0_DATASET_CARD.md` | `a2d44c60788d0506c1108e1629fb2a2e6ac23d6fc41ca87c2e27a6d138152278` | 19413 |
| `NUMERICAL_PROGRAM.md` | `35687ad192cc363be06f0436148fb6e97a9426f7653fed15308f14c07c214208` | 9659 |
| `NUMERICAL_MODEL_REGISTER.md` | `7fe3f9ecfb51f0e0519ef8d91a857b0038393cdb2546fd2a1b3ee52966aef968` | 22540 |
| `NUMERICAL_TRAINING_SPEC.md` | `888fa925485a64642443b7555d8a989aea955d0a7997e23a09edef7db93bbd37` | 31309 |
| `MODEL_AND_DATA_SPEC.md` | `c4d77b5036afbe531387886ee460d35a47ba6d824bf5a13077f20d7c9906b771` | 64024 |
| `ALGORITHM_PORTFOLIO_AND_EVALUATION.md` | `c0dbea56b78a51c5f6a075d7e0ace6e0d84a4fe97a1366cd699624e5783f49aa` | 51138 |
| `MODEL_IMPLEMENTATION_RECIPES.md` | `f016aa31c039dd95152f36a6df56d2758c2769b146b73bd8b8a43fa18e02021c` | 20837 |
| `RECENCY_AND_REBOUND.md` | `b35e9684ecb6d468b2570d6e429301cba567f8590e230bb3a46d42ffd4d93f37` | 18248 |
| `BASE_RATES_REGISTER.md` | `a254fad38f0890191a790204ab836dc5555134435a22c9bd3f4105216bf74b20` | 26617 |
| `GAME_LOG_STATUS_CURRENT.md` | `1e28c9e473399b9abc0b0787001a61bfcb606ec2649110fc5e7b80a848310186` | 135708 |
| `PREDICTION_LOG_COMBINED_5.md` | `eb76d1d2ce9a88a8c1d5e85e6b548eaa840ddea95ae09cac06773452b5bd5d71` | 893504 |
| `archive/audit_documents_implemented_2026-09-25/AUDIT_RECONCILIATION_ALL_SPORTS_2026-09-21.md` | `4cc9ca4c2da51dae05ea01ff864b86c99b273f2ec2cb3347613b776167ab2621` | 14968 |
| `archive/audit_documents_implemented_2026-09-25/AUDIT_IMPLEMENTATION_2026-09-21-CR3.md` | `3ce923f087fc42f5a42fc86ea6d23b2122f75b63be38c3bf2bd19cf66402b978` | 6320 |
| `archive/audit_documents_implemented_2026-09-25/AUDIT_CLOSURE_LEDGER_2026-09-25.md` | `22b5a8b01fda9b07d0062506e25d3d4992d4fc04c9742c70c3bf8157448a8272` | 17137 |
| `research/base_rates_2026-09-25/README.md` | `e62e32f84c0ceaf536acbfd26010e3b2845ef867e9b3fb2a73b4ceec93fbfebf` | 4297 |
| `research/base_rates_2026-09-25/analyze_extra.py` | `07b85846c3a3969662883a177e412ba3d428be58c36e0380f1f63d93f5b1441b` | 3952 |
| `research/base_rates_2026-09-25/analyze_leagues.py` | `c277fbea3457ab6cfcad9d654d6f108be5c630d75fb3d5bb2fa8f154bd146595` | 12818 |
| `research/base_rates_2026-09-25/analyze_mlb.py` | `37eeb60dd15dfec070e8a1220acc3d9c947481b724603f7e6bb5a12bb2eb92f7` | 3871 |
| `research/base_rates_2026-09-25/analyze_more.py` | `939e7e1cffb8c7951f1cc795ff331ef07ab80d3f4538c3ca80820a09b60990c7` | 4845 |
| `research/base_rates_2026-09-25/analyze_nhl.py` | `c889c185a596cc3191ecd794a3263419554d916bad3fcd763733575d88613e2b` | 3811 |
| `research/base_rates_2026-09-25/analyze_nhl_pre.py` | `e4b70d8615a73743d7897b86ec7de491ba57cf3c92d1484a4fa2767ac40bec55` | 322 |
| `research/base_rates_2026-09-25/analyze_tennis.py` | `4e508b00e77dd428a992e0428c3bb3acaddbb254ae72024a20cfe36e7a7be51b` | 4975 |
| `research/base_rates_2026-09-25/extra_results.json` | `b0712035363175342dc4dad16107c26f1ae4e3ce46ecf0e01b5d4d457737c2e8` | 3768 |
| `research/base_rates_2026-09-25/fetch.py` | `6ac05a3beaca1b9f1921e848f5119e5012efa185de5e6c59ca5e9b061aed5488` | 2705 |
| `research/base_rates_2026-09-25/league_results.json` | `5217d09ecbd55a63bbd3ad2330141ce428c47e22a8d78a7c681e081a3892386f` | 17454 |
| `research/base_rates_2026-09-25/mlb_results.json` | `6fc884ceab5f7aff2f5f0985c6b6a5efd05622b80fea00bfa92f544696689005` | 5807 |
| `research/base_rates_2026-09-25/more_results.json` | `86c76c3329108e1ffe44f34a8a82bbdeacb2224d21f9f65fc88c08b787bc7298` | 5300 |
| `research/base_rates_2026-09-25/nhl_results.json` | `0186286b32d3f373faeb8946aebee7cb195d85e0ec349377baac1fda76b99b00` | 2149 |
| `research/base_rates_2026-09-25/pooled_checks.py` | `a84d47f596dc3474bdc09b3344a8aceda82f9f319192ea81229f06c082b78c40` | 3282 |
| `research/base_rates_2026-09-25/pull_all.py` | `de3c068d4dd900fe48d16c11af47c98a46e7885a9c83119d18d3c3dbe0a397f2` | 591 |
| `research/base_rates_2026-09-25/pull_more.py` | `14c90f5481a6e4ddc04950918040d6d0b919dc99bee5db5cfd05439d9ec294de` | 2449 |
| `research/base_rates_2026-09-25/pull_nhl_pre.py` | `53a6ea9ece407426622606c1a7d97b08154d7721e12aa40aef75620357cb4fe8` | 328 |
| `research/base_rates_2026-09-25/pull_nhl_tennis.py` | `32d15bcb8efc7bb69d880883c0e6d91610758b676c58ed63d31fb6d9054517c6` | 3509 |
| `research/base_rates_2026-09-25/tennis_results.json` | `274650d4117e9b75bfaaaa028f43a7f6ae599a265a46a397ba94d326d886f34e` | 5574 |
