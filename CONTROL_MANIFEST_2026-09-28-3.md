# Control manifest — 2026-09-28-3 (sport capability-link propagation)

Method: **MDS-2026.09.19-v4.3**
Control revision: **CR-2026.09.21-3** (label unchanged; content receipt under the same label)
Status: **CURRENT post-write content receipt**, generated 2026-09-28 04:08 AEST by `tools/make_manifest.py` from `CONTROL_MANIFEST_2026-09-28-2.md`.

**Purpose.** This is the byte-level SHA-256 receipt that every new card freezes (`METHOD.md` header; PF-7). Propagates the central exact-scope capability/status authority to all ten active sport-rule modules and the two league reference headers, closing the remaining documentation-link recommendation. The prior same-day VALIDITY_REPAIR receipts remain preserved; this third receipt is the current complete governance snapshot.

**It does not change any forecasting coefficient, probability cap or ranking override.**

**Category (C-RULE-FREEZE):** VALIDITY_REPAIR.

This manifest is excluded from its own hash table. The living logs (`PREDICTION_LOG_COMBINED_5.md`, `GAME_LOG_STATUS_CURRENT.md`) are a write-time snapshot and change with every card. Hashes are taken in CRLF form (`tools/manifest_lib.py`); verify with `python tools/verify_manifest.py`.

**Changed since CONTROL_MANIFEST_2026-09-28-2.md (by bytes):** `METHOD.md`, `RULES_BASEBALL.md`, `RULES_CRICKET.md`, `RULES_SOCCER.md`, `RULES_BASKETBALL.md`, `RULES_AFL.md`, `RULES_NRL_RUGBY.md`, `RULES_RUGBY_UNION.md`, `RULES_AMERICAN_FOOTBALL.md`, `RULES_ICE_HOCKEY.md`, `RULES_TENNIS.md`, `LEAGUE_RULES_CRICKET.md`, `LEAGUE_RULES_SOCCER.md`, `reviews/2026-09-28/IMPLEMENTATION_REPORT.md`.

**New in the receipt:** none.

**Dropped:** none.

**Unchanged:** 138 files.

## SHA-256 file receipt

| File | SHA-256 | Bytes |
|---|---|---:|
| `README.md` | `87b03efa2621f6691eaa4a5d8807def8f6a192e156bc59f27b957aca6ff7a6e3` | 14322 |
| `METHOD.md` | `4dc5727ebb85015e4a2a3445d7691994d039a25881e160486da42e694591a911` | 29534 |
| `CONTROLS.md` | `86c9afa3b26c492df249fc6ae689dd4da14dd56190768087db74233c01985efe` | 43771 |
| `RULES_GENERAL.md` | `6c3563b645183b14c6774641ff2bb89add26ff5a5f03a0e9075be706a6648e54` | 293961 |
| `SOURCES.md` | `6e172c9fecf767af75da09d0f745e1428910795aa1e4e674a364b4b3af71faac` | 76886 |
| `DATA_SOURCE_REGISTER.md` | `898affe43d3490b83a2c8a888d88dc2b09cbdfe71024294ae79df9d32d17efef` | 178952 |
| `UPCOMING_GAME_RESEARCH_GUIDE.md` | `a3e7ed767257a7660c5c221cc23ffa6d4d3f3b332430c1ef5705427de445778f` | 76011 |
| `SCORING_AND_VALIDATION.md` | `42bdf6fc0d9c293a3e59cbc09682273c7a0b6bee8cb6a9f03ccd95aa91918961` | 25616 |
| `PERFORMANCE_ELIGIBILITY_POLICY.md` | `a102c231debc12253accf5ade0ed3086c7b51dcf3959e570129ad8b6d96dd2fa` | 19422 |
| `LEARNING_REGISTER.md` | `59d90b3a31e642d21f5ff2dea6d993af2039797baff9a48f0d7654055805a951` | 336129 |
| `AGENT_ROLE_AND_TASK.md` | `7ab4a2b52fa33a0cf9f9838926dda2acc6babc71fb1b99c3387873b0c15d52fb` | 25862 |
| `EXTERNAL_LOGGING_WORKFLOW.md` | `b724db948916f0bb4ae8847fcfd7fc278cf5db8fed8a2d04411507f5dcc1a6d8` | 68415 |
| `FORECAST_PREFLIGHT_MANIFEST.md` | `34718b2faca3276e7213bc622e01ff06998151390f5f7c3f12497082e7468678` | 9309 |
| `RULES_BASEBALL.md` | `eb548a4685b1132cb19b54ada50e9c900b8ba29b9618e3eefd729ee00e0bb121` | 140938 |
| `RULES_CRICKET.md` | `fc368199238ced891df727b42a4570c59be8478d7f84ee7362dfa425db550c95` | 113698 |
| `RULES_SOCCER.md` | `14017c285bb54cd49747af6d5de64cdd4c995e56e93eb1019f7a91e0321c4d7e` | 112530 |
| `RULES_BASKETBALL.md` | `5bbf86123d3159f30551118b1cf44142f89644bd1db4e3f075e1ba9abd63d548` | 108485 |
| `RULES_AFL.md` | `c247a53ad0a5ddaf4503617c0b74cb6ab70a990cdc5f0212be14c35ae53e7a12` | 66715 |
| `RULES_NRL_RUGBY.md` | `25fb2131599f7931e22e8d2bece0ff3c47a901b62bbe859cbb7c4618e58a9349` | 65312 |
| `RULES_RUGBY_UNION.md` | `38e231b5b4361405a265deed238e274432f6be1452ad1201271e6b6d0534bc77` | 54869 |
| `RULES_AMERICAN_FOOTBALL.md` | `0cb24f6c925e9c6e71d2589cae4d807fa7f34551edfa3350d39bd0be5f935e23` | 71347 |
| `RULES_ICE_HOCKEY.md` | `136bfbc997c3c7df69ca9fd4ddf7d0ace46a922adca943af1775d6509dd0da56` | 62560 |
| `RULES_TENNIS.md` | `ae6188c72bb724fc8cd88d99033274ce3ed19b0a5547085136fd6dac68ce0c85` | 78631 |
| `LEAGUE_RULES_CRICKET.md` | `e45ef80bfcac03a58ab6949fc6be03d8a2c538d2ea2f60268eed2d98330bee37` | 26645 |
| `LEAGUE_RULES_SOCCER.md` | `34ba905d6bc55eb37b03ceb7e643c459f911d2ef3e1efd6ae573c99632f537b2` | 44258 |
| `prediction_preflight.py` | `b4d07fef54e71ef8478c5b2cec3af15c5f5accf50ba3e703348ab16609006d26` | 29319 |
| `test_prediction_preflight.py` | `c91ef73ac3faa420e3b67f8e5f345a851c4f9a69e43e75c21be6d3c7a53d5d60` | 11403 |
| `audit_card_controls.py` | `c8f5b420e995c28dfbf1daaaf451801248c4f58182dbde2c1eebbb61d0ac9a69` | 35130 |
| `test_audit_card_controls.py` | `84da7061d82bc7cc063499c516298b0e3888356205b349ea26116bdfcba21693` | 17948 |
| `receipts.py` | `33c906e5b6a0f67ffaf103347f058955401923a3cb57ee43158cd7f2d1b3de30` | 21886 |
| `test_receipts.py` | `c841b495300f0e7e7afec7f4b24b1780c6a879b0067ed5b648a800625cee3c08` | 6502 |
| `H0_DATASET_CARD.md` | `a2d44c60788d0506c1108e1629fb2a2e6ac23d6fc41ca87c2e27a6d138152278` | 19413 |
| `NUMERICAL_PROGRAM.md` | `d49b179f7ffa87d1e25601e0ab78bc7a009fa1ef146092918b3670ed2020115d` | 13829 |
| `NUMERICAL_MODEL_REGISTER.md` | `205b44aaf4a7c1ab7ff2b461fb15c30f89ae38bf89d4508b94a5fc56cc1b0870` | 26779 |
| `NUMERICAL_TRAINING_SPEC.md` | `888fa925485a64642443b7555d8a989aea955d0a7997e23a09edef7db93bbd37` | 31309 |
| `MODEL_AND_DATA_SPEC.md` | `c4d77b5036afbe531387886ee460d35a47ba6d824bf5a13077f20d7c9906b771` | 64024 |
| `ALGORITHM_PORTFOLIO_AND_EVALUATION.md` | `c0dbea56b78a51c5f6a075d7e0ace6e0d84a4fe97a1366cd699624e5783f49aa` | 51138 |
| `MODEL_IMPLEMENTATION_RECIPES.md` | `7bb3ed44e2e51bf7361f57ddcfcbe22223637bc90d4932e6ba9081909ec5c42e` | 21136 |
| `RECENCY_AND_REBOUND.md` | `b35e9684ecb6d468b2570d6e429301cba567f8590e230bb3a46d42ffd4d93f37` | 18248 |
| `BASE_RATES_REGISTER.md` | `dad341c609cd421ef020424e8565640571223e14e2669f50666561a80c90626d` | 34383 |
| `GAME_LOG_STATUS_CURRENT.md` | `3567d706ccd50048f9cb394497d4a72c5f5971f1e1a5d35ef04fe840c78b3d84` | 140752 |
| `PREDICTION_LOG_COMBINED_5.md` | `5802878c6e9edeb5ab21478a02d8c40e82921aa646dd475575c9dc1b050e07af` | 1058187 |
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
| `CURRENT_RULES.md` | `2897250ba44546dd807c6a3edd10ff6cf6f3b4b39872fdf3c75c487995ee9e3a` | 46456 |
| `CHANGELOG.md` | `2c5bbb6e2d3eedd3a8a04a776be541975a085dd47ecae28eeb942c83fe08a07e` | 43150 |
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
| `tools/skill_baseline.py` | `87c3047d09deed99148ad267275647c439e11f9eefba6a17d2d0d9e79385f79b` | 11061 |
| `tools/test_repo_tools.py` | `23691fbacce8bf207e5843a0a9e1dafd89fa803d8474c8dec1fcedac8f96c2f6` | 7934 |
| `tools/test_skill_baseline.py` | `2cb57eb6dcaffa0b06d95e580e71a95fd0c1b1b412e4b8549e6cd776be79dadf` | 4392 |
| `research/base_rates_2026-09-25/build_skill_baseline_seed.py` | `babaa48ef17feb22916bab7feabf04ff2a4b3d800393fcafaa5246d578d61ede` | 9714 |
| `research/base_rates_2026-09-25/.gitignore` | `03edf42376bb781d8497699bee737ae42badca878e1d27cf191d04e87e8d872c` | 161 |
| `tools/card_math.py` | `a14202a134b101a62950a96e52751a8b5d8236dfb513b8a4a37c091106082677` | 11330 |
| `tools/calibration_report.py` | `808dc5c0c11dae93915d0d5dbdc3096422556e6770f90afa1c4a0f813e8551f3` | 17789 |
| `tools/test_card_math.py` | `8026c1a74135b8a1896f5f7bbd7db63abf213f5001411069eb17827a6cd79aec` | 7299 |
| `research/settled_rows_2026-09-25/README.md` | `216958df41e51991de7558ebb6a88300678f6d1c5f47a334a4651870c0b6cabb` | 10899 |
| `research/settled_rows_2026-09-25/extract_settled_rows.py` | `162759f367b2609e0c306036695dc2547f0db1598c75227b650e0d2d8af682db` | 29207 |
| `research/settled_rows_2026-09-25/analyze_settled.py` | `4eff0b3eb4b3d497a361dc450eca97cb86979ca543cfba33f09c1eabb1a82b32` | 8463 |
| `research/settled_rows_2026-09-25/analyze_supplement.py` | `148653ad9e111b5730cb1ce5267a7b3f07c1e4036dd12c802b4907f603b7491b` | 4868 |
| `research/settled_rows_2026-09-25/analysis_results.json` | `b1441e3e1c1f471286271e90738e2dcf3c8cd5036b4fc2773c304877da0b229f` | 17392 |
| `research/settled_rows_2026-09-25/supplement_results.json` | `78b9ed833e03bf85a43851f00434456a463a223cc16987eacc3be3e61dab0beb` | 5262 |
| `tools/rank_model.py` | `5e17522e41cc14f80aa2db2eafbb4d5be4418c9775cc9eaff2790eb6bd8dc9e9` | 24043 |
| `tools/rank_model_coefficients.json` | `d8b6d12a7a48804a2e4ec366066bd66ead1b880d8c23dffd54c81d6483a62c68` | 341 |
| `tools/test_rank_model.py` | `af8506088bf140856ac63814163a7d395b6b2c6e6963abc0be85a17ba699f53a` | 7687 |
| `tools/team_baseline.py` | `f8c0281fe5d007b0e2be98bcd84d12eba5f78d1bfda206b1f6e3e7708a8297f0` | 27457 |
| `tools/test_team_baseline.py` | `eaed5279e273bef44da03b6fc63744ad076571b2a8ffd6bbbde713d3e1183d3b` | 4885 |
| `research/rank_model_2026-09-25e/README.md` | `d0eba618b172973f389ee79cbc5dbd686fa978d421da314b74fed2b05c94a4cb` | 11431 |
| `research/rank_model_2026-09-25e/validate_rank_model.py` | `8de3651281eeb547981b0471d63ec3293d3288b87b04bdd1d393423d665eb00d` | 13308 |
| `research/team_baseline_2026-09-25e/README.md` | `2cea0dc61b944733479804d1f7ac01c91f7d91df55aeb39ef5121424e9b30ee3` | 9237 |
| `research/team_baseline_2026-09-25e/validate_team_baseline.py` | `d926982f8b0a1acaf1bbe3a769fa9f37a6b163f7d57cd12b18930b78138b9da7` | 8691 |
| `research/team_baseline_2026-09-25e/oval_base_rates.py` | `62617d80a3eec1c8f077df04dfa03ae1d97f5144e33c1d95029b7dd6596ca7dd` | 5991 |
| `research/team_baseline_2026-09-25e/pull_oval.py` | `ebf68e78db6e555c0228f52327252b02918842c0b33e3ab9cc9b62643eae77a4` | 1114 |
| `research/base_rates_2026-09-25/pull_oval_specs.py` | `1b757907548ea1341eb5e3119c509dd2705aaa34f6dd79637896acc4144a7ea3` | 694 |
| `LEARNINGS_INDEX.md` | `e6188a3ad44df91e232d8a5d5d6ea440ed4684f8b54fe430f7320ce09292045b` | 37697 |
| `MARKET_BENCHMARK_LEDGER.md` | `c17ac01e622fc07e020c28ac576fcd6f0478af06b0212610b2f37ac3591aa467` | 3349 |
| `tools/slate_universe.py` | `9331769ace5441d9d1c63f3ae5412b1c8960cd1e8c44cfb569236e5935141550` | 15186 |
| `tools/test_slate_universe.py` | `030a22aefb59d4df5da9b538bd89533eb82172baf3e709da1fdf3ef1f3bb3db4` | 4689 |
| `tools/market_benchmark.py` | `fdc541ceb97b784d9c2b0c0f82a27a9f4e422b4b05e18b55a072f11a9ecf4eba` | 11107 |
| `tools/test_market_benchmark.py` | `56cd7541090ed5180c7841d94d6cfdfd8371b7b332c582c2d05e3442c5d1e794` | 4559 |
| `tools/evidence_status.py` | `1d7ff13c141f556193f31e7cd9f4e95401c3ff62376afa941f001d2f5a6e4673` | 11103 |
| `tools/test_evidence_status.py` | `920a2b2e978d9063f3b7c1d7d7404a91168490cacdf7717446892f463cc679ac` | 8851 |
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
| `research/predictability_2026-09-26/README.md` | `03308bd4b4e5c91faf2fc4fb40d51598e0fb1b5a625203b7d03f406425f0fbb6` | 14783 |
| `tools/semantic_validation.py` | `43b126d14f1fdceccb143227e56eb9a760befe6e11308875f60b46dac9d3ce3f` | 27848 |
| `tools/prospective_eligibility.py` | `748c06105ef2d1b2b6afb3916b147add53e9520aa2ddb994c0262caa1663669e` | 7997 |
| `tools/test_semantic_validation.py` | `58c11ff68ed28dee7dc408885e533a232fa9403ac895dec0bd786f936379cccb` | 14807 |
| `tools/test_prospective_eligibility.py` | `8ca313dfc3405bfd03be8c2a87cf09c3e8afa009e9bc51a428e50fc79c492dd3` | 6614 |
| `tools/test_settled_row_extractor.py` | `2046284ff692450f69e6e51e32b22945b761825bc51bf7dbfb88315c035c818d` | 3529 |
| `tools/test_calibration_report.py` | `43aa696e82b636b8580ab9f5d71baece9607111e490f9bc853ddec54b9da0c93` | 4130 |
| `research/settled_rows_2026-09-28/prospective_record.schema.json` | `db37f4ba6228b1b43762739c3f540638608c77412e84418435d6e8d29218dad0` | 15248 |
| `research/settled_rows_2026-09-28/prospective_records.json` | `785d8805edded4c4ca6328b8248b1ea914b77869211a18d1e8e7fd1b26b14207` | 47 |
| `research/settled_rows_2026-09-28/RECORD_SCHEMA.md` | `535b961ea55f65fc778b668d5fbbf752ac6a5dd2e9cf764504742032c3006cc5` | 8031 |
| `research/settled_rows_2026-09-28/CAPABILITY_STATUS.md` | `6a50863f89c1c4e18d0906e12e630b86302d9eb25148b244d54217595106801a` | 6760 |
| `research/settled_rows_2026-09-28/generated/README.md` | `c7ebd1326f5555bc4343379a047eace64faf2723a2bfe129927d7cae651be2d3` | 3161 |
| `research/settled_rows_2026-09-28/generated/settled_rows.csv` | `d3362b3e4ddf8e125434b41cd6c8a6ead2283f8d523ab62ef78449f305d78215` | 532819 |
| `research/settled_rows_2026-09-28/generated/conflicts.csv` | `5f092e104e56dcf98254015cf798c4912c0f4e8e710e32c27d2ba4d4457f9a47` | 14335 |
| `research/settled_rows_2026-09-28/generated/unattributed_rows.csv` | `3112e1d12e1cd19cacd0dcbc8023df19092fc113121c5367a69a9cbc8eb82146` | 9701 |
| `research/settled_rows_2026-09-28/generated/coverage.txt` | `4feb17964648135e39ab038512759053dbcf3f7e7d5b5ef57be7f169b5983b39` | 608 |
| `reviews/2026-09-28/SPORTS_RESEARCH_COMPREHENSIVE_REVIEW.md` | `578b4c8b5ff9b5e2df853acc7d0c17600a46a1403f0c0c22b1a6a3397fb22c59` | 31868 |
| `reviews/2026-09-28/SPORTS_RESEARCH_REPAIR_PLAN.md` | `9e82c75c1ad8032c36e760fc1297d96e168fbebba938cb53385513f6e63c21d6` | 23205 |
| `reviews/2026-09-28/IMPLEMENTATION_REPORT.md` | `2af56d6fac8334ff90f455e4e01c5f11748e96840bc2690c45f2213b7415fa4f` | 11863 |
| `reviews/2026-09-28/ARCHIVED_RULE_DELETION_RECEIPT.md` | `a2a53859e9a0850eb850fb076369a4190bc56892e9c66b708d8a94de660b6b9a` | 2683 |
| `reviews/2026-09-28/P518_P522_EXTERNAL_SOURCE_READBACK.md` | `a2db8066cd7efdc3890e0cef696d00e46ca19077f5cb7b75849885792994128e` | 4564 |
| `reviews/2026-09-28/P518_P522_RECONCILIATION_REGISTER.csv` | `81ab6868e13687817c2e5d0a563fafdff8759e3eb616421fde81eb24d90e25c1` | 2518 |
| `reviews/2026-09-28/mlb_822678_verification.json` | `a557294febd92d4db0f170a49ae18b675e451060717cb1d9a613641f68693d15` | 5630 |
| `reviews/2026-09-28/audit_evidence.json` | `4e16b0f87a35b1a9740d0bf3c9b42d1189616f35fe987c22b019a2ce82d83c18` | 557221 |
| `reviews/2026-09-28/VALIDATION_RECEIPT.md` | `45cf97bf1fd965dff69c9329f35e3133f7b319048d72722f42803eef48e293fb` | 3320 |
| `reviews/2026-09-28/extraction_preview/README.md` | `91d86809fda900fe379205e040a67ad21388ab66248ff10a33e3958a9921717b` | 897 |
| `archive/reconciliation_2026-09-28/PREDICTION_MINI_RUNNING_LOG_P518_ONWARD_WORKTREE_SNAPSHOT_2026-09-28.md` | `c4d497bf339010eae2ff5df23a2d76290983585671666e74791618342565cf30` | 141740 |
| `archive/reconciliation_2026-09-28/PREDICTION_MINI_RUNNING_LOG_P518_ONWARD_INDEX_SNAPSHOT_2026-09-28.md` | `edb9afdb2c8fb166dd2a0ad7f63856d5671996f2357a31fbef6295ebc0a9b35e` | 104484 |
| `PREGAME_ELIGIBILITY_REGISTER_2026-09-05.md` | `81ca820ddc7a295d7315758957ec9360591bc3c57d6e9627671a4ad33be298f3` | 81726 |
