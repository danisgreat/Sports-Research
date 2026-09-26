# Control manifest — 2026-09-27 (2026-09-26(e) predictability across sports)

Method: **MDS-2026.09.19-v4.3**
Control revision: **CR-2026.09.21-3** (label unchanged; content receipt under the same label)
Status: **CURRENT post-write content receipt**, generated 2026-09-27 01:36 AEST by `tools/make_manifest.py` from `CONTROL_MANIFEST_2026-09-26.md`.

**Purpose.** This is the byte-level SHA-256 receipt that every new card freezes (`METHOD.md` header; PF-7). Predictability pass (preregistered P1-P4 in cc447c9; P5 exploratory): the predictability map (C-PREDICTABILITY-MAP, BASE_RATES_REGISTER 7.8), the reference model registry (C-MODEL-ANCHOR, tools/model_anchor.py, status REFERENCE, not a card input), T-FAV70-BAND opened, T-MLB-V2-2025 concluded (replicated). Validity repairs: TB-1 resolution withdrawn for NRL sides and NFL totals (intervals cross 0); the mlb_model.py starter-reconstruction claim corrected. No probability, rank, width, centre or model constant moved.

**It does not change any forecasting coefficient, probability cap or ranking override.**

**Category (C-RULE-FREEZE):** MEASUREMENT.

This manifest is excluded from its own hash table. The living logs (`PREDICTION_LOG_COMBINED_5.md`, `GAME_LOG_STATUS_CURRENT.md`) are a write-time snapshot and change with every card. Hashes are taken in CRLF form (`tools/manifest_lib.py`); verify with `python tools/verify_manifest.py`.

**Changed since CONTROL_MANIFEST_2026-09-26.md (by bytes):** `README.md`, `METHOD.md`, `CONTROLS.md`, `RULES_GENERAL.md`, `LEARNING_REGISTER.md`, `RULES_BASEBALL.md`, `RULES_CRICKET.md`, `RULES_SOCCER.md`, `RULES_BASKETBALL.md`, `RULES_AFL.md`, `RULES_NRL_RUGBY.md`, `RULES_RUGBY_UNION.md`, `RULES_AMERICAN_FOOTBALL.md`, `RULES_ICE_HOCKEY.md`, `RULES_TENNIS.md`, `NUMERICAL_MODEL_REGISTER.md`, `BASE_RATES_REGISTER.md`, `CURRENT_RULES.md`, `CHANGELOG.md`, `tools/team_baseline.py`, `LEARNINGS_INDEX.md`, `tools/mlb_model.py`, `research/sport_shadow/README.md`, `research/sport_models_2026-09-26/README.md`.

**New in the receipt:** `tools/model_anchor.py`, `tools/test_model_anchor.py`, `research/predictability_2026-09-26/PREREGISTRATION.md`, `research/predictability_2026-09-26/README.md`.

**Dropped:** none.

**Unchanged:** 96 files.

## SHA-256 file receipt

| File | SHA-256 | Bytes |
|---|---|---:|
| `README.md` | `6e0236836cabc63c3e30d32d71f004790365dc55a7eef0e13153466ef584f040` | 14760 |
| `METHOD.md` | `141344a50e64f60d236d9ce23a2d63ca263fab80e04f46c8f4f73ccbefb85feb` | 31559 |
| `CONTROLS.md` | `86c9afa3b26c492df249fc6ae689dd4da14dd56190768087db74233c01985efe` | 43771 |
| `RULES_GENERAL.md` | `44ea2f115d69c8bf3081397e60cdb146729c3e7ca2adbb1d2b925f84f03154e2` | 292879 |
| `SOURCES.md` | `6e172c9fecf767af75da09d0f745e1428910795aa1e4e674a364b4b3af71faac` | 76886 |
| `DATA_SOURCE_REGISTER.md` | `898affe43d3490b83a2c8a888d88dc2b09cbdfe71024294ae79df9d32d17efef` | 178952 |
| `UPCOMING_GAME_RESEARCH_GUIDE.md` | `a3e7ed767257a7660c5c221cc23ffa6d4d3f3b332430c1ef5705427de445778f` | 76011 |
| `SCORING_AND_VALIDATION.md` | `64cb95cf3afcfd3f4d33f79bc34428aa82d095290810d64e9f62de929e806a22` | 23793 |
| `PERFORMANCE_ELIGIBILITY_POLICY.md` | `a102c231debc12253accf5ade0ed3086c7b51dcf3959e570129ad8b6d96dd2fa` | 19422 |
| `LEARNING_REGISTER.md` | `6b5fe8e9584ba7b65c24b3c1f72e54899114fbbca676412e45ce7fc8a0801962` | 335068 |
| `AGENT_ROLE_AND_TASK.md` | `7ab4a2b52fa33a0cf9f9838926dda2acc6babc71fb1b99c3387873b0c15d52fb` | 25862 |
| `EXTERNAL_LOGGING_WORKFLOW.md` | `b724db948916f0bb4ae8847fcfd7fc278cf5db8fed8a2d04411507f5dcc1a6d8` | 68415 |
| `FORECAST_PREFLIGHT_MANIFEST.md` | `34718b2faca3276e7213bc622e01ff06998151390f5f7c3f12497082e7468678` | 9309 |
| `RULES_BASEBALL.md` | `c0d8bbd5f97dd67e998b37d9af91db1525957cb0c780c5dda3d727555c3861ce` | 140545 |
| `RULES_CRICKET.md` | `288c469d9bb412179339f7494cc4504c7fe661e35205dd3e0ae61206dca127a4` | 113305 |
| `RULES_SOCCER.md` | `673190bc2eace19a658e7b137a11f09493234b8708e016fd709cdff03ff2e441` | 112137 |
| `RULES_BASKETBALL.md` | `9a650aab0f4a2e71b1a06e4a5652754c124fbe6c9971046a987e0ad0a761a2c6` | 108092 |
| `RULES_AFL.md` | `4194823914cd0be790a7657fda20aebe5d6487ef26a9c3614eb54d3ae8efb5bf` | 66322 |
| `RULES_NRL_RUGBY.md` | `962593aad12c8e24b65fd4b76a378d6c2c5a8c922b201973a73161b676f1a53d` | 64919 |
| `RULES_RUGBY_UNION.md` | `476258c0c7f1a65ab6539a4dc69a964f3d9413924d3733c724c3c0830f46eb4e` | 54476 |
| `RULES_AMERICAN_FOOTBALL.md` | `6dafbaec18f43ca50f80cd125a2be41f89a058649af718684f28abb8fc0c2132` | 70737 |
| `RULES_ICE_HOCKEY.md` | `8b7a4d79fd0641dae9b749a8cf2bf6746c04e16ed3dd0f0b23412eca6131f599` | 62167 |
| `RULES_TENNIS.md` | `ba6490d45ea02c2e73ae554953397168f7cb6d4c04a778f08b7b682bb1c3b72e` | 78238 |
| `LEAGUE_RULES_CRICKET.md` | `b6b13dfa72047b62fd9987e21daa0ec25510ab0853ebbac461b5725de5f99099` | 26252 |
| `LEAGUE_RULES_SOCCER.md` | `236463054f21792ad091fd3f326c7cb12aac767c933ffc4bd2e265acf55df06b` | 43865 |
| `prediction_preflight.py` | `b4d07fef54e71ef8478c5b2cec3af15c5f5accf50ba3e703348ab16609006d26` | 29319 |
| `test_prediction_preflight.py` | `c91ef73ac3faa420e3b67f8e5f345a851c4f9a69e43e75c21be6d3c7a53d5d60` | 11403 |
| `audit_card_controls.py` | `c8f5b420e995c28dfbf1daaaf451801248c4f58182dbde2c1eebbb61d0ac9a69` | 35130 |
| `test_audit_card_controls.py` | `84da7061d82bc7cc063499c516298b0e3888356205b349ea26116bdfcba21693` | 17948 |
| `receipts.py` | `33c906e5b6a0f67ffaf103347f058955401923a3cb57ee43158cd7f2d1b3de30` | 21886 |
| `test_receipts.py` | `c841b495300f0e7e7afec7f4b24b1780c6a879b0067ed5b648a800625cee3c08` | 6502 |
| `H0_DATASET_CARD.md` | `a2d44c60788d0506c1108e1629fb2a2e6ac23d6fc41ca87c2e27a6d138152278` | 19413 |
| `NUMERICAL_PROGRAM.md` | `58b16f645172a3b94fae8ffe90af0e1d7f08606df6baa67745e6cc5a29429665` | 13037 |
| `NUMERICAL_MODEL_REGISTER.md` | `ce37a88947d8ed9a999a2d62faa79041c90482d8f68972bae24b237b9de5af8c` | 26528 |
| `NUMERICAL_TRAINING_SPEC.md` | `888fa925485a64642443b7555d8a989aea955d0a7997e23a09edef7db93bbd37` | 31309 |
| `MODEL_AND_DATA_SPEC.md` | `c4d77b5036afbe531387886ee460d35a47ba6d824bf5a13077f20d7c9906b771` | 64024 |
| `ALGORITHM_PORTFOLIO_AND_EVALUATION.md` | `c0dbea56b78a51c5f6a075d7e0ace6e0d84a4fe97a1366cd699624e5783f49aa` | 51138 |
| `MODEL_IMPLEMENTATION_RECIPES.md` | `7bb3ed44e2e51bf7361f57ddcfcbe22223637bc90d4932e6ba9081909ec5c42e` | 21136 |
| `RECENCY_AND_REBOUND.md` | `b35e9684ecb6d468b2570d6e429301cba567f8590e230bb3a46d42ffd4d93f37` | 18248 |
| `BASE_RATES_REGISTER.md` | `dad341c609cd421ef020424e8565640571223e14e2669f50666561a80c90626d` | 34383 |
| `GAME_LOG_STATUS_CURRENT.md` | `7caff59e52c28eaa8326b1baaeaf85a45d970fa826346e817b051cbbcf9b8af7` | 139678 |
| `PREDICTION_LOG_COMBINED_5.md` | `127b0ca79a793860b47fc3a5a6a26f7a3bd95586ed62f439f228c9cfb56e8703` | 1057962 |
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
| `CURRENT_RULES.md` | `ba941afca4178887c39474855099623960d3be6aecc0c029b8a4888175188c49` | 46534 |
| `CHANGELOG.md` | `9d63da461ef0204a7c77e5774dc0a820f07b9e7f0521b7de5b3540a675b38207` | 42864 |
| `CONTRIBUTING.md` | `2a62e9f3910c01e474ad3f5bac3b5b493277b901a4f2caae82d35ab6cfe57ee6` | 4705 |
| `SKILL_BASELINE_LEDGER.md` | `63ab9bddaff8d5381224664aa929df759eebbdbc03a189688c0f8daed4458712` | 10145 |
| `LICENSE` | `1efb20731adc03fb046120ceeceb7f4e0ca0d73b2eb2d5fcf2093350863161b8` | 1211 |
| `.gitignore` | `3d36960f62f2ed189d59bfd55f1ea7e1609e8d7c953e86d15d19202adc46650c` | 1038 |
| `.gitattributes` | `8e7b10c0994c597d8d35111d065d6986c543f5a514d308ec74217885443e9dcc` | 513 |
| `.github/workflows/checks.yml` | `4f28e429fc6f69a1bce9f029572479235edeb468b14a0865e724457a00195743` | 1619 |
| `tools/manifest_lib.py` | `646b30705db92e03c0c83e135274aff6317c41a688d80dd6f4e6099d7bd395e6` | 2133 |
| `tools/make_manifest.py` | `247bfc65d265f643a8225a2dcf29feb86fc88b51a7d3ea31da4cdd360e705de6` | 8576 |
| `tools/verify_manifest.py` | `51fc35aedd098185c6a4e17b63d6bbe5a6c1ca74757be50b6b06dc3f561fa2b4` | 3551 |
| `tools/repo_hygiene.py` | `32f25a888190325ff8994180710571af7cbe6507883c3e386e9b6c5c6dad7981` | 5270 |
| `tools/skill_baseline.py` | `320f3a3aa35cada5cb1f5d31e427e8382d6d22ad276a876fadae1600e917f543` | 7616 |
| `tools/test_repo_tools.py` | `23691fbacce8bf207e5843a0a9e1dafd89fa803d8474c8dec1fcedac8f96c2f6` | 7934 |
| `tools/test_skill_baseline.py` | `5b9af14596de89231a56aed60a24c4d7c817ff6d9748b4d7203a9a6bf50fab18` | 3637 |
| `research/base_rates_2026-09-25/build_skill_baseline_seed.py` | `babaa48ef17feb22916bab7feabf04ff2a4b3d800393fcafaa5246d578d61ede` | 9714 |
| `research/base_rates_2026-09-25/.gitignore` | `03edf42376bb781d8497699bee737ae42badca878e1d27cf191d04e87e8d872c` | 161 |
| `tools/card_math.py` | `a14202a134b101a62950a96e52751a8b5d8236dfb513b8a4a37c091106082677` | 11330 |
| `tools/calibration_report.py` | `15964628f4a89325acff60d3bd07a1ca9c2ded0de0e76574cf1c6a88622cf042` | 8502 |
| `tools/test_card_math.py` | `f3c65d208b5bcbb4850b0ebfc531d192038cf5ee3bbc670fbf33b4b8cd0144c7` | 5601 |
| `research/settled_rows_2026-09-25/README.md` | `b30c19d31bfe21a70222cc76fe200846bc0da89083a86fac9b308f1112a17ee1` | 9792 |
| `research/settled_rows_2026-09-25/extract_settled_rows.py` | `5aa5a094855d1894e8cb29f9c9fd9cc96d33befbf515ce7aa79fb92552e54a17` | 19751 |
| `research/settled_rows_2026-09-25/analyze_settled.py` | `4eff0b3eb4b3d497a361dc450eca97cb86979ca543cfba33f09c1eabb1a82b32` | 8463 |
| `research/settled_rows_2026-09-25/analyze_supplement.py` | `148653ad9e111b5730cb1ce5267a7b3f07c1e4036dd12c802b4907f603b7491b` | 4868 |
| `research/settled_rows_2026-09-25/analysis_results.json` | `b1441e3e1c1f471286271e90738e2dcf3c8cd5036b4fc2773c304877da0b229f` | 17392 |
| `research/settled_rows_2026-09-25/supplement_results.json` | `78b9ed833e03bf85a43851f00434456a463a223cc16987eacc3be3e61dab0beb` | 5262 |
| `tools/rank_model.py` | `d6589f7f6a16fdf078446c75c3cd5c834a8cc3c341969bcf0daadb24357c38df` | 22683 |
| `tools/rank_model_coefficients.json` | `d8b6d12a7a48804a2e4ec366066bd66ead1b880d8c23dffd54c81d6483a62c68` | 341 |
| `tools/test_rank_model.py` | `e0c7960ea338fb9c68ac4e62099d1ee4e14836f4d6b038d84eb8c1f20ef0de9e` | 6736 |
| `tools/team_baseline.py` | `f8c0281fe5d007b0e2be98bcd84d12eba5f78d1bfda206b1f6e3e7708a8297f0` | 27457 |
| `tools/test_team_baseline.py` | `eaed5279e273bef44da03b6fc63744ad076571b2a8ffd6bbbde713d3e1183d3b` | 4885 |
| `research/rank_model_2026-09-25e/README.md` | `d0eba618b172973f389ee79cbc5dbd686fa978d421da314b74fed2b05c94a4cb` | 11431 |
| `research/rank_model_2026-09-25e/validate_rank_model.py` | `8de3651281eeb547981b0471d63ec3293d3288b87b04bdd1d393423d665eb00d` | 13308 |
| `research/team_baseline_2026-09-25e/README.md` | `2cea0dc61b944733479804d1f7ac01c91f7d91df55aeb39ef5121424e9b30ee3` | 9237 |
| `research/team_baseline_2026-09-25e/validate_team_baseline.py` | `d926982f8b0a1acaf1bbe3a769fa9f37a6b163f7d57cd12b18930b78138b9da7` | 8691 |
| `research/team_baseline_2026-09-25e/oval_base_rates.py` | `62617d80a3eec1c8f077df04dfa03ae1d97f5144e33c1d95029b7dd6596ca7dd` | 5991 |
| `research/team_baseline_2026-09-25e/pull_oval.py` | `ebf68e78db6e555c0228f52327252b02918842c0b33e3ab9cc9b62643eae77a4` | 1114 |
| `research/base_rates_2026-09-25/pull_oval_specs.py` | `1b757907548ea1341eb5e3119c509dd2705aaa34f6dd79637896acc4144a7ea3` | 694 |
| `LEARNINGS_INDEX.md` | `6ee462d5df7ce8f1db11bce35d86686ccd3e78328092c776e35ef5b9feeed113` | 37494 |
| `MARKET_BENCHMARK_LEDGER.md` | `c17ac01e622fc07e020c28ac576fcd6f0478af06b0212610b2f37ac3591aa467` | 3349 |
| `tools/slate_universe.py` | `9331769ace5441d9d1c63f3ae5412b1c8960cd1e8c44cfb569236e5935141550` | 15186 |
| `tools/test_slate_universe.py` | `030a22aefb59d4df5da9b538bd89533eb82172baf3e709da1fdf3ef1f3bb3db4` | 4689 |
| `tools/market_benchmark.py` | `fdc541ceb97b784d9c2b0c0f82a27a9f4e422b4b05e18b55a072f11a9ecf4eba` | 11107 |
| `tools/test_market_benchmark.py` | `56cd7541090ed5180c7841d94d6cfdfd8371b7b332c582c2d05e3442c5d1e794` | 4559 |
| `tools/evidence_status.py` | `985f233ddfa96903679e3517d17b833595c066d4cfdfdd7d2e9da523298ee4b2` | 9596 |
| `tools/test_evidence_status.py` | `63db5f665c55102118eeb6eaf4326e9fa46c1db49b180143543ffdc6eb45da3b` | 4954 |
| `tools/mlb_model.py` | `afd72c2f739fe330fa1d8cd5519c5cea1c0457e83ac69ebc71670798440903ad` | 30349 |
| `tools/test_mlb_model.py` | `e683dd68f913beaf8aecd938ce3b9616bf6e875860809bf2b70f69ad11406c7f` | 9939 |
| `research/mlb_shadow/README.md` | `d8cab21b78a75948795a00bc18a7e9b5a313567af517d4e9fc36d60710c424a2` | 3442 |
| `tools/sport_models.py` | `8439e379299a6c52ffca6b0565ddd8fd49d3b7b014dabc2b1d1b09ade04fc002` | 96649 |
| `tools/sport_data.py` | `60beb71298a396201db5f9dd99478a88e765ca873c145010c7ac34f2ddf40667` | 22430 |
| `tools/test_sport_models.py` | `927147b812bcf841f686c2696e3db137263e5c40a8af7538c8e599025ad4f9df` | 35079 |
| `research/sport_shadow/README.md` | `d91cbe00bf4c0f99f7082de69f896e9231cb7b4efc9df9dd0c3970db5e69bf44` | 5861 |
| `research/sport_models_2026-09-26/README.md` | `2dc1655e47d866ef07a955e5207eeeb633d0dc265db24dfa6888eadc99831ba5` | 27910 |
| `research/sport_models_2026-09-26/validation_results.json` | `0967c988b8ca62be57d8bdfb789bb37ac0237d88959677c952fee0fa7d6f79ea` | 74704 |
| `tools/model_anchor.py` | `8191b38d6f0e5ff1b94269254a037e52781ba269cf0208f027ec6e3a8f8a8689` | 14427 |
| `tools/test_model_anchor.py` | `5129c18ccb1dc7904d7825005bee42c72858d8df8a3a1780098accade9e336e1` | 3304 |
| `research/predictability_2026-09-26/PREREGISTRATION.md` | `8dca83f036eb588cbc10542eda3231f234f84e1bf09b01526e0c4ae736696be4` | 6072 |
| `research/predictability_2026-09-26/README.md` | `2d51819d868b1d6176a5bbdeb56e45e3f77834047b2ecc2cf84a8b35fde96c30` | 12558 |
