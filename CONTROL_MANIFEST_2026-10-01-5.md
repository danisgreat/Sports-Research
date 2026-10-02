# Control manifest - 2026-10-01-5

Method: **MDS-2026.10.01-v7.1**; control **CR-2026.10.01-I2**.
Status: **CURRENT; selected by METHOD.md**.

User-authorized October overhaul and requested-analysis/canonical-log repair. Earlier receipts and pinned model dependencies remain unchanged. Historical forecast values and original run bytes are preserved. No live qualification or prospective pilot is asserted.

CRLF entries decode optional UTF-8 BOM, normalize newline forms, then hash UTF-8 with CRLF. RAW entries hash exact bytes. This manifest excludes itself, the living status/verification output and active Part 6. Append stores (daily runs, source observations, shadows, canonical ledger/issued/issued_research/pilot transactions) use their own retained hash chains; original shadow custody is separately checked. Restricted benchmark bodies remain local and ignored.

The archive's canonical manifest and source-custody manifest chain its complete indexed CSV/receipt/output scope. Bulk derived CSVs need not be duplicated here. Sport yearly narrative documents outside that archive hash scope remain reference documentation; they are not admitted forecast inputs. Do not infer unlisted source truth or procedural completeness from this receipt.

Listed files: **374**.

User-authorized cleanup refreshed this retained receipt on 2026-10-02 (Australia/Sydney). Removed 385 byte-identical standalone CSV copies in 10 folders and 24 superseded control-manifest files. All 359 retained canonical season CSVs were hash-checked and are unchanged. Season builders now write only under Previous Sports Results. Superseded manifests remain recoverable from Git history. This refresh records file custody, not an independent audit of historical game-data completeness.

| File | Mode | SHA-256 | Bytes |
|---|---|---|---:|
| `.gitattributes` | RAW | `c1c236f8579e8ff9cdd7cdd89fc59b3b604921ca898957c3a6d89d35533df02e` | 296 |
| `.github/workflows/research.yml` | RAW | `851fa151823a2a1a58bc27240f01db4afbb27ab4f17cb0b0228cc320c427a55a` | 1050 |
| `.gitignore` | RAW | `6727bf657383c5fc0457d727e7933d4c8b273a17b741fe759b2d409021f02bf1` | 600 |
| `BASE_RATES_REGISTER.md` | CRLF | `13e3245a8d3d5aa61b595a703ecaf8a77ac0baaeaa700836a096cfedcedfbd7a` | 37325 |
| `CARD_AND_LOG_TEMPLATES.md` | CRLF | `42d27e224f3e829475af9132a1d8ec7ee65966d9d76e085513fd69f5d2a39cc5` | 5160 |
| `CHANGELOG.md` | CRLF | `a8e7c23ed8e3174c8989169d4a36096fae05922b795e324097008fa119deccdd` | 65676 |
| `CONTRIBUTING.md` | CRLF | `e13458b408c63a1024e736e3c7ed9e56e5908885c10caa55ad83f8e509b58423` | 1599 |
| `CURRENT_RULES.md` | CRLF | `f2ef75ce17be91f2bcbdd13ae4084d37d776987750e5adeb29311cada5580b15` | 13033 |
| `GAME_PREDICTION_RANK_LOG.csv` | RAW | `4bb0592221b7c9c94a75f13559eb9a233055a436b8a2e880cfe9d96bff3a97d7` | 1523097 |
| `HISTORICAL_LINK_INDEX.md` | CRLF | `d88da53952d78ee205d7511e2be20f474ab83acc627bf1d8f3a6860738426ab9` | 68536 |
| `IMPLEMENTATION_2026-10-01.md` | CRLF | `224fece2169f8b3098e2c62bc2762a7bb9cf2a1b353f04cea9a4b70b299755b2` | 23161 |
| `LEAGUE_RULES_CRICKET.md` | CRLF | `4a851a9bba96150aa06e17641df26e3091d1f440b921592b4493fac378a96fbd` | 26895 |
| `LEAGUE_RULES_SOCCER.md` | CRLF | `89020a837653ff4a0678acf583be75b763360d0ea476d2ee20e96bba3e529b16` | 44378 |
| `LEARNING_REGISTER.md` | CRLF | `9ef3409094f65ffde7044b448bd22259921098eb73cd5d03e5ce754b5a3bc797` | 354016 |
| `LEARNINGS_INDEX.md` | CRLF | `04d4d9c2d2c3404017928b9b127ad4899c1666ee3bb5cae03d6bbf823cffccc4` | 45920 |
| `LICENSE.md` | CRLF | `1efb20731adc03fb046120ceeceb7f4e0ca0d73b2eb2d5fcf2093350863161b8` | 1211 |
| `MARKET_BENCHMARK_LEDGER.md` | CRLF | `d886b11c3fef4aec742749d4e41a4926a36345abab51240693d9b6482e1f9b1c` | 3883 |
| `METHOD.md` | CRLF | `af837301982dc0dd97f4419f3e604960d79e4d0961aa51137c21be7ccb902b1b` | 3415 |
| `P518_P522_RECONCILIATION.md` | CRLF | `ae085ef1324ebdc255bab7194ef897be3bf327b1953a2af1bfa89f57a4c9c4df` | 14447 |
| `PIPELINE_IMPLEMENTATION_2026-09-29.md` | CRLF | `14c2cf97a48aeeb49f7e33fdca17d85264da195a4bb07e7cf22de9df6e7864d1` | 10151 |
| `prediction logs/PREDICTION_LOG_COMBINED.md` | CRLF | `9b6f07a5ccd5c10209e5c7701b9698ed71eaab6aecbf156af36d8fffe7efaf81` | 4139536 |
| `prediction logs/PREDICTION_LOG_COMBINED_2.md` | CRLF | `b63569d6ff05b42f4cc9ef49f6e5f723e11eefdb554928b8ec2af98587f22c64` | 565262 |
| `prediction logs/PREDICTION_LOG_COMBINED_3.md` | CRLF | `aabfc9f9c155f4752c92129611332a6f2cb8e747564d86c8835ad685157fbf6c` | 419639 |
| `prediction logs/PREDICTION_LOG_COMBINED_4.md` | CRLF | `91216b87bdd8c0786240ffbb3fdc3fd338703598d0731fa2fc16a21b5a26b14e` | 854587 |
| `prediction logs/PREDICTION_LOG_COMBINED_5.md` | CRLF | `29a627d17b5bea00f0bf65e038bf421c3353deae53834d870ab72531a548896d` | 1058646 |
| `Previous Sports Results/_canonical/manifest.json` | RAW | `0eeccc333fe3769793bf7ad3fa89d34233cc148be036fddbfac852164972efd3` | 5429565 |
| `Previous Sports Results/_canonical/README.md` | CRLF | `53e6a87db0476238ab50d88ff639d5f3fd03f4bd9ea394b8ed5d1af9a639eba0` | 4321 |
| `Previous Sports Results/_custody/corrections.jsonl` | RAW | `98bbd026e2253dc1bf1e0733745686e333969bbb7bb1b82b72a8b1ad2befbb98` | 310172 |
| `Previous Sports Results/_custody/originals_index.jsonl` | RAW | `396117e4059905c452ca091808aad99538d3500600a763ed4aa302d57f3f37d2` | 10935 |
| `Previous Sports Results/_custody/verified_facts.json` | RAW | `ff6b4e51dc41b4ace89e9e6831657be4897168c8c4d8ea3d53538ae61fb75c0e` | 3644 |
| `Previous Sports Results/_football_research/audit_all_american_football.py` | RAW | `27bea219e04cd2ca2aad36450ebee21516bc4a486bf8cf2eb4950eeee38fb3d9` | 465 |
| `Previous Sports Results/_football_research/collect.py` | RAW | `7c412765e4bed28cd0d6750a8d3689de30db51d0e8245d036aa28f3a0b2abdaa` | 16533 |
| `Previous Sports Results/_football_research/generate_nfl_perfect.py` | RAW | `bcc3f386f3f0788b7a1685ab412d64a9deb11ff29b300887cd0001d6a0f391f2` | 462 |
| `Previous Sports Results/_football_research/master_audit.py` | RAW | `27bea219e04cd2ca2aad36450ebee21516bc4a486bf8cf2eb4950eeee38fb3d9` | 465 |
| `Previous Sports Results/_football_research/PIPELINE_STATUS.md` | CRLF | `9fc848087a401727f250aae26e0f574d2209ed263734ad7436e9e914ee000382` | 2473 |
| `Previous Sports Results/_football_research/standardize_headers.py` | RAW | `bcc3f386f3f0788b7a1685ab412d64a9deb11ff29b300887cd0001d6a0f391f2` | 462 |
| `Previous Sports Results/_football_research/test_marquee.py` | RAW | `27bea219e04cd2ca2aad36450ebee21516bc4a486bf8cf2eb4950eeee38fb3d9` | 465 |
| `Previous Sports Results/_football_research/update_afl_grand_final_perfect.py` | RAW | `bcc3f386f3f0788b7a1685ab412d64a9deb11ff29b300887cd0001d6a0f391f2` | 462 |
| `Previous Sports Results/_football_research/update_afl_league_perfect.py` | RAW | `bcc3f386f3f0788b7a1685ab412d64a9deb11ff29b300887cd0001d6a0f391f2` | 462 |
| `Previous Sports Results/_football_research/update_aflw_rosters_perfect.py` | RAW | `bcc3f386f3f0788b7a1685ab412d64a9deb11ff29b300887cd0001d6a0f391f2` | 462 |
| `Previous Sports Results/_football_research/update_american_football_meta.py` | RAW | `bcc3f386f3f0788b7a1685ab412d64a9deb11ff29b300887cd0001d6a0f391f2` | 462 |
| `Previous Sports Results/_football_research/update_american_football_part1.py` | RAW | `bcc3f386f3f0788b7a1685ab412d64a9deb11ff29b300887cd0001d6a0f391f2` | 462 |
| `Previous Sports Results/_football_research/update_nfl_perfect.py` | RAW | `bcc3f386f3f0788b7a1685ab412d64a9deb11ff29b300887cd0001d6a0f391f2` | 462 |
| `Previous Sports Results/_football_research/update_super_bowl_perfect.py` | RAW | `bcc3f386f3f0788b7a1685ab412d64a9deb11ff29b300887cd0001d6a0f391f2` | 462 |
| `Previous Sports Results/_football_research/update_ufl_ifaf_perfect.py` | RAW | `bcc3f386f3f0788b7a1685ab412d64a9deb11ff29b300887cd0001d6a0f391f2` | 462 |
| `Previous Sports Results/COVERAGE_AND_BLANK_YEARS.md` | CRLF | `c454be2637f3ee50b7251ec47cc468184c05c5ffb377e09b5f0dd37c0135ad01` | 86365 |
| `Previous Sports Results/DATA_SOURCES_IMPLEMENTATION.md` | CRLF | `c4a744b42757fdcd98d105bec03825db6bacad8b23896acb412f34552f73ae6e` | 84660 |
| `Previous Sports Results/README.md` | CRLF | `cdca614c37d2bd5134938f3ec6f9f1b58b5e6c7993c60836e8155c1bc3f488ea` | 42081 |
| `PROBABILITY_TOOLKIT.md` | CRLF | `f00694a339699f8c1338443417df65985ed16b298e4e04a4267d562c2a6e7650` | 51551 |
| `PROMPTS.md` | CRLF | `2b915cac9d2ec65cbec0f574102f97b3c71cc9db45f4beaa83bce447deed79d4` | 4071 |
| `README.md` | CRLF | `ad716907c3c7d6dff033d3aa7d0bdd42f0c2541d73ee89fdf786c7b17bd630dd` | 4203 |
| `RECORD_ELIGIBILITY_SCHEMA.md` | CRLF | `06823697af83682cb744279f10cd749091be2ffed684c4c229db98cddcd42566` | 4003 |
| `research/.gitignore` | RAW | `f07b2a42cecd1f614a7b5c1f69238d13a5a5313d22b1aaa18a1887cc7f061e04` | 67 |
| `research/admission_registry.json` | RAW | `923f1d1e15578d808a9d86031e7753663e264b87e151cf9ec517d77dfe9f9014` | 41210 |
| `research/baseline_definitions/epl-empirical-score-0.1.0.json` | RAW | `543b4fd4b9ae2c7ae83c83d6e70fd485ed8028a2ad09909a2664eef5a93fcd45` | 1459 |
| `research/baseline_definitions/epl-population-score-0.2.0.json` | RAW | `ff2dd10d2eb9bbaf6af091b89d67baba00c001485b66e0f63280451c6e0c2545` | 1530 |
| `research/baseline_definitions/nbl-population-home-0.1.0.json` | RAW | `7c782581c3a206d432c5a015f1e1f970bd5e9b15818378bfd3f573ff67e28cf6` | 1300 |
| `research/baselines.csv` | RAW | `d624f9baf3e70bb16a7d982594f84c4969f223ad9ae8b5cbab42f7b248eb5a3a` | 1316 |
| `research/custody/implementation_2026-10-01/.gitattributes` | RAW | `c70cb9473d237db6e014364b97cefb2090107b781110e3e7c9187bfb5ebf5f37` | 150 |
| `research/custody/implementation_2026-10-01/.gitignore` | RAW | `ed8bcf8e6400a38456c155502976429b6c71837393e51341d6494a4b9dcd7cc0` | 380 |
| `research/custody/implementation_2026-10-01/BASE_RATES_REGISTER.md` | CRLF | `f9df00b888606a14e843342c5237e675247d3028411f94aeca4a4da852ef24ae` | 36415 |
| `research/custody/implementation_2026-10-01/CARD_AND_LOG_TEMPLATES.md` | CRLF | `93dd416fe642147c61df3240e2bfc6a2a8aa930b4e19ea35b86bd2da555d8141` | 20587 |
| `research/custody/implementation_2026-10-01/CHANGELOG.md` | CRLF | `234ad8f71ed14740a0ac89ab2ab2caaaa258af3310b83468d0e9a0404b014a1a` | 61287 |
| `research/custody/implementation_2026-10-01/CONTRIBUTING.md` | CRLF | `bac7a3ba9e228762d3eff57b253b5191195bfe6eb2cab8bd06885cd7dbe4401a` | 2044 |
| `research/custody/implementation_2026-10-01/CURRENT_RULES.md` | CRLF | `c9cd50462cdc731d979d852eda46f74898e329043f8394410d5e2e3e75834c04` | 42420 |
| `research/custody/implementation_2026-10-01/extra_intake_snapshot/PREDICTION_MINI_RUNNING_LOG_P523_ONWARD.md` | CRLF | `621789c49f8cb542f646e7f0281a1dcd429ba589ed695ae33fdf0852bc3abd64` | 20129 |
| `research/custody/implementation_2026-10-01/extra_intake_snapshot/PREDICTION_MINI_RUNNING_LOG_P523_ONWARD.md.sha256` | RAW | `1a23b3baee5e42d1ea63a6ab551f5a35a50fd55cf9ccd2634025cbd7cb0bf5ff` | 66 |
| `research/custody/implementation_2026-10-01/GAME_LOG_STATUS_CURRENT.md` | CRLF | `f9b9899635f49b5be7dac46d104fc0ff618fe0dae14d0085a174267d8af52e9b` | 142909 |
| `research/custody/implementation_2026-10-01/GAME_PREDICTION_RANK_LOG.csv` | RAW | `4bb0592221b7c9c94a75f13559eb9a233055a436b8a2e880cfe9d96bff3a97d7` | 1523097 |
| `research/custody/implementation_2026-10-01/HISTORICAL_LINK_INDEX.md` | CRLF | `d88da53952d78ee205d7511e2be20f474ab83acc627bf1d8f3a6860738426ab9` | 68536 |
| `research/custody/implementation_2026-10-01/LEAGUE_RULES_CRICKET.md` | CRLF | `4c73d2b33e460b0bca3bf992dd706531cc5e93238ea0b2be2fbdfc78ed28beec` | 26610 |
| `research/custody/implementation_2026-10-01/LEAGUE_RULES_SOCCER.md` | CRLF | `2fb2db93e7a1369884ae74e8a71c633cb70f347c8142cc1a4b4306f5183a454c` | 44093 |
| `research/custody/implementation_2026-10-01/LEARNING_REGISTER.md` | CRLF | `9a4917c69740f75e73529d2b9263301bf88140579237d0f1044e39d2ffd7d369` | 348190 |
| `research/custody/implementation_2026-10-01/LEARNINGS_INDEX.md` | CRLF | `c953ee180e34c2f834446409d9faae5e0a415eaa68e70c93b4c83caeac515a50` | 43203 |
| `research/custody/implementation_2026-10-01/LICENSE.md` | CRLF | `1efb20731adc03fb046120ceeceb7f4e0ca0d73b2eb2d5fcf2093350863161b8` | 1211 |
| `research/custody/implementation_2026-10-01/manifest.json` | RAW | `715bf1d32d24c2fbf16d6dc4a540e4fde62700532adba424436d30dfa90038c4` | 44810 |
| `research/custody/implementation_2026-10-01/MARKET_BENCHMARK_LEDGER.md` | CRLF | `d886b11c3fef4aec742749d4e41a4926a36345abab51240693d9b6482e1f9b1c` | 3883 |
| `research/custody/implementation_2026-10-01/METHOD.md` | CRLF | `c48467a0f9992bbd7d2094c2c07df9f4a83124523d174c5d972f54adc6bcfd7e` | 6025 |
| `research/custody/implementation_2026-10-01/P518_P522_RECONCILIATION.md` | CRLF | `6d2e39e94121e72ac5d6cbf0e536a54e33b6865738cc1cca21e7678f12fbc6c8` | 8436 |
| `research/custody/implementation_2026-10-01/PIPELINE_IMPLEMENTATION_2026-09-29.md` | CRLF | `847391f31470322290df5a6f152b3cefa93b4593567400981a24bb2933fba2e5` | 9668 |
| `research/custody/implementation_2026-10-01/PROBABILITY_TOOLKIT.md` | CRLF | `c6fe84a9243251881b2468791d7d0c0d42612d4f799c64d19b826f22a97e834b` | 50453 |
| `research/custody/implementation_2026-10-01/PROMPTS.md` | CRLF | `35ccf01715d913fb4b2f8fe8cb50cf8ae363f80e884fbb5c50502492518f27f2` | 18390 |
| `research/custody/implementation_2026-10-01/README.md` | CRLF | `2cb07aeeb6fbfdf029af901fb5b26366e31c274e0dd1c82f99ce9d48d7e638b7` | 7991 |
| `research/custody/implementation_2026-10-01/RECORD_ELIGIBILITY_SCHEMA.md` | CRLF | `38194d3f1dd5c9c3e4744a061883ce2ea5e580f7edd6317d7b1d8165410aaa67` | 6543 |
| `research/custody/implementation_2026-10-01/research/runs/epl_2025-26_closing_benchmark.json` | RAW | `a5cc3f197effca26ea96b47943001fb8c3d6e7195a090ed1100288b20af45b54` | 444 |
| `research/custody/implementation_2026-10-01/research/runs/epl_2025-26_holdout.csv` | RAW | `79affa039094859c84d7dfff8114f30aef9f70d86b35e8a53217fb4e14d0008d` | 130428 |
| `research/custody/implementation_2026-10-01/research/runs/epl_2025-26_holdout.json` | RAW | `5cadf89505287a18a84f3db2db1bdabadb59431b9f225b1bc4ea9d5e397774dd` | 3782 |
| `research/custody/implementation_2026-10-01/research/runs/epl_tuning_lock.json` | RAW | `adbe0390675be8da4e19176e52a6c7691b32b816084301a6741ce67e86aad553` | 1033 |
| `research/custody/implementation_2026-10-01/research/runs/epl_tuning_xi_0_001.csv` | RAW | `13a8eb8a5e2dc2e8cf59797cb3ef3fb9051e78cd3db6fb503072e834807c1125` | 520858 |
| `research/custody/implementation_2026-10-01/research/runs/epl_tuning_xi_0_0019.csv` | RAW | `0e748659d76226fc10f40d31e046e95b91caa7646dd3fba0d6cdd211f24fcfd7` | 522333 |
| `research/custody/implementation_2026-10-01/research/runs/epl_tuning_xi_0_003.csv` | RAW | `5f27f9a62fb1377686cb8d7b1e40437d649685f681c2712e16c8fb608a86594e` | 521507 |
| `research/custody/implementation_2026-10-01/research/runs/evaluation_environment.json` | RAW | `e5f6162fe671daef0ffa62cffb0ac456c72e76714ba863a11c17e31d5c97cbb2` | 1114 |
| `research/custody/implementation_2026-10-01/research/runs/nbl_2025-26_holdout.csv` | RAW | `f9c8a0912f968304f1c1910e4b7cd2728f03e910ba3a1bb28cc92848e9b70092` | 50641 |
| `research/custody/implementation_2026-10-01/research/runs/nbl_2025-26_holdout.json` | RAW | `cacbda05740b13543d27facdf5771497be37866eb55f4a71c79c0fb554addabf` | 2462 |
| `research/custody/implementation_2026-10-01/research/runs/nbl_tuning_half_life_180.csv` | RAW | `939954cadca623c7a44de441695149a16b108cf52f6693045b97753d1e71b150` | 129673 |
| `research/custody/implementation_2026-10-01/research/runs/nbl_tuning_half_life_365.csv` | RAW | `9a08fc4ed5a6283ca2728008316ec5022cd37b1d0dd5406c65fab713586193ae` | 129684 |
| `research/custody/implementation_2026-10-01/research/runs/nbl_tuning_half_life_730.csv` | RAW | `cbb97f6732be9c589b1d6ada7c3def1b0485ebbe159d9c9c0124c44d045c3d42` | 129771 |
| `research/custody/implementation_2026-10-01/research/runs/nbl_tuning_lock.json` | RAW | `f0d4c03c65fabdabb49bb2eee6ef275c29f806c457943f7dc659692c3183e7e0` | 1307 |
| `research/custody/implementation_2026-10-01/research/shadow/nbl27/36f8c608-58ad-11f1-aa0e-2bbb920071b5.json` | RAW | `ed28d070d28c0339d09e2116fbe6b986dc3b9c629b29ba38b9eddfbd247b0f85` | 1268 |
| `research/custody/implementation_2026-10-01/research/shadow/nbl27/3718a994-58ad-11f1-add9-d98e318e0a1e.json` | RAW | `beee987497a3a76cde3f69b179b4ee339a0ac7a398347cf04a6de56f15deef17` | 1269 |
| `research/custody/implementation_2026-10-01/research/src/__init__.py` | RAW | `b23cde9797abfb99fe132a2d5b863c26e574bfe947c90c62b8586fdec8172661` | 72 |
| `research/custody/implementation_2026-10-01/research/src/baselines.py` | RAW | `4c4e7ed764df8079372c576f24652c6e0ee05cc770a55f774f2a48152530b8e7` | 2447 |
| `research/custody/implementation_2026-10-01/research/src/benchmark.py` | RAW | `9e5a0815ded279e0cd68b906472ba04bd428815c8cce58e5c064c89893000ab8` | 2708 |
| `research/custody/implementation_2026-10-01/research/src/build_afl_all_years.py` | RAW | `7164041386249b893b822d9893d1dfcc40b953e8835b86a5c6b12487cbb3aff8` | 18036 |
| `research/custody/implementation_2026-10-01/research/src/build_aflw_all_years.py` | RAW | `b1dcfc411437d454b6445784454cc6897991710d7c8ede6de1b7c1df36d38a58` | 30634 |
| `research/custody/implementation_2026-10-01/research/src/build_cfb_all_years.py` | RAW | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | 0 |
| `research/custody/implementation_2026-10-01/research/src/collect_cfb_postseason.py` | RAW | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | 0 |
| `research/custody/implementation_2026-10-01/research/src/control_manifest.py` | RAW | `81543b5015e0c0ecb46c81736245e37e039c3ecad7f4fd3f76ba07ebf7fbdc75` | 3826 |
| `research/custody/implementation_2026-10-01/research/src/current.py` | RAW | `2da11bf6fb665717afa9626ae218c7ba2d59089692dca6614f6bfc798b6c5e55` | 3265 |
| `research/custody/implementation_2026-10-01/research/src/dixon_coles.py` | RAW | `3cb47e0845b558fecde03f9c1f4f14b730964f82a6b3cef79474962f73d02f1f` | 6062 |
| `research/custody/implementation_2026-10-01/research/src/draft_epl.py` | RAW | `d195871a6c8bce43855299ce7e8910fddf2984835053a67b28c3d77a0b486c8e` | 5787 |
| `research/custody/implementation_2026-10-01/research/src/emit_card.py` | RAW | `c5c02e1af2e2ec8fc2093dabfc379f78beddd9871416bdd2dac93b05cf7ee009` | 13088 |
| `research/custody/implementation_2026-10-01/research/src/evaluate.py` | RAW | `6ac830d8c09bf4221c94e693af2ad32065fcc645e1badaa6d53712b2f3717d5d` | 7579 |
| `research/custody/implementation_2026-10-01/research/src/features.py` | RAW | `73b8ff815b9153b1f16d168613fd754df0bef4923cf0c9d09d80137e6017d006` | 2321 |
| `research/custody/implementation_2026-10-01/research/src/feeds.py` | RAW | `50c02b0dc6472a34c4363de9e0409a4be2137cf9e1110ab83079ed6b55f5698e` | 4905 |
| `research/custody/implementation_2026-10-01/research/src/legacy_ledger.py` | RAW | `e2b013472443b120b39ea37ca4becf5b819a7b990b811ba92b5c8d3685e3fd9d` | 6657 |
| `research/custody/implementation_2026-10-01/research/src/load.py` | RAW | `647dea85c5ff32b64c80b356c61c784280a77362e3a958fea2ef73b5350229a4` | 8309 |
| `research/custody/implementation_2026-10-01/research/src/nbl_current.py` | RAW | `60fdd7024c77ad6e01fc56b0911312970eb2b8cbfd45e26cfeb8c9cda16d6abd` | 5035 |
| `research/custody/implementation_2026-10-01/research/src/nbl_evaluate.py` | RAW | `273d6d44160100d400534ac81a0146f901641530d3a50ad69f0d61655fa7328c` | 7954 |
| `research/custody/implementation_2026-10-01/research/src/nbl_load.py` | RAW | `df16d1414b21bb375e3170c28f585ea7bd1a1369a8f8637e159c6f9e168a2bdd` | 11681 |
| `research/custody/implementation_2026-10-01/research/src/nbl_model.py` | RAW | `3fb4df6ee26c8405b2d633edfbe4911acdbfd739dad55bf480214b9c3de10ffe` | 3994 |
| `research/custody/implementation_2026-10-01/research/src/nbl_shadow.py` | RAW | `0d90cb2dc4edd47c202c0741b6cdd36891364ff1e150ebccb41f92ceb17fb364` | 5233 |
| `research/custody/implementation_2026-10-01/research/src/pilot.py` | RAW | `b4f73c5da536b7ee88dc9cc8391583e95d41052f6a126c4f689bd5b24976eb4d` | 6627 |
| `research/custody/implementation_2026-10-01/research/src/settle.py` | RAW | `6cbe3e494f6a65099c24728272e46c8938cb06428a2e783ffaab8c8c2f06bd3e` | 3270 |
| `research/custody/implementation_2026-10-01/research/src/test_parsers.py` | RAW | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | 0 |
| `research/custody/implementation_2026-10-01/RULES_AFL.md` | CRLF | `0d484bd98f94931a5b943a7745c6986b4053d851e009295c21232eed17982193` | 37979 |
| `research/custody/implementation_2026-10-01/RULES_AMERICAN_FOOTBALL.md` | CRLF | `ee4875832616051320043e0f5ca784f0962721eea66dcdaa8309921009e400f2` | 43972 |
| `research/custody/implementation_2026-10-01/RULES_BASEBALL.md` | CRLF | `e055da0b26e65e2813ebfc46aed261449c80b3af7c401fbb64db7547d4ed87ef` | 63198 |
| `research/custody/implementation_2026-10-01/RULES_BASKETBALL.md` | CRLF | `b3b40e51a9395fc9ec7a3e2792cb41d703caf5f2badc70777f37eb9de1d2a183` | 48564 |
| `research/custody/implementation_2026-10-01/RULES_CRICKET.md` | CRLF | `e88fecaceb1f3ac1037de4d2e8920a8c050769429cfbbcc7d1d9e9b718b02844` | 57700 |
| `research/custody/implementation_2026-10-01/RULES_ICE_HOCKEY.md` | CRLF | `dd98dbbea86b84f80b6a4a76ed128d14cb01f17723d40cb4692827d538921af3` | 36832 |
| `research/custody/implementation_2026-10-01/RULES_NRL_RUGBY.md` | CRLF | `98384bcf5c343d1b17b30c3b01d7e24e59ccddb489660dcc7531869e48fd78fc` | 35430 |
| `research/custody/implementation_2026-10-01/RULES_RUGBY_UNION.md` | CRLF | `bb98d55c354d69438ff9967e3d6061c1b8187f25be7bf09ebb580f9c7884378d` | 34655 |
| `research/custody/implementation_2026-10-01/RULES_SOCCER.md` | CRLF | `88698b4e478a34677baddb7af6efae6881ab6d171839c14364362e36bbd96def` | 43023 |
| `research/custody/implementation_2026-10-01/RULES_TENNIS.md` | CRLF | `8ce618e5ddc029a3743767aa77294cb0aff67d8a5cbbebf9daf7da010aa3e865` | 44073 |
| `research/custody/implementation_2026-10-01/SCORING_AND_VALIDATION.md` | CRLF | `b5935e6daaf4bb9087d7c1d82135fb78c1bed2251a6fa06ef1e09e07bbf5c991` | 29132 |
| `research/custody/implementation_2026-10-01/SKILL_BASELINE_LEDGER.md` | CRLF | `fa12e9c8d1a0b7ab9814ff6905ab973121a8c3606aedffaabbda45fceb9c1636` | 12491 |
| `research/custody/implementation_2026-10-01/source_registry_first_observation.json` | RAW | `dcca91a8ce7d87b14b070fd0c08115dd215bad6b8022f8eb6959bf9438435bed` | 11079 |
| `research/custody/implementation_2026-10-01/SOURCES.md` | CRLF | `0c92c3cdeb5d8e7a96805fdc24d29fbd00f1fe2f50ffcc761da95346f3984d5f` | 84725 |
| `research/custody/implementation_2026-10-01/VALIDATION_EVIDENCE.md` | CRLF | `986f353d216aefd2221058c8aea927f3d9b2dc3c92dcc03cdbde41345cfe997a` | 50646 |
| `research/custody/implementation_2026-10-01/VERIFICATION_PROTOCOL.md` | CRLF | `2830ffbdefd968b729df1d40f89d47a10c6e39558a586ad1f208d0a59e8a5ede` | 7413 |
| `research/custody/implementation_2026-10-01/VERIFICATION_RECEIPT_2026-09-28.md` | CRLF | `28b19eab7bafc552f19ac18e02ef7131b5885f141e8084eb8e30ab1932ff1c57` | 14471 |
| `research/data/eurobasket_cache.json` | RAW | `b6bb4f0ca8cc42a922e37fe12d68313caa51e95ce10a55035b9f10f8a46d8a28` | 431553 |
| `research/data/nba_cache/nbaallelo.json` | RAW | `1e2d58cf6bc0579154603ea213f038e27352acf8596d32fb57a473ced01c6a57` | 61118766 |
| `research/data/nba_cache/sdv_nba_schedules.json` | RAW | `1bd921127ae63f9d33d385d45b2a1ba3112e9e96594fa6b8a4a7dca2c6da9523` | 84515617 |
| `research/data/nbl_box_team.csv` | RAW | `d4f5ff92a4fff426a5065b9a9373cb04a1c3cb16482ed2a803edb7f103093905` | 957665 |
| `research/data/nbl_results_wide.csv` | RAW | `f366a1892382ff9217f3a4df05cffa76c9c56b2b8887aec8df0391f777d15db1` | 2003973 |
| `research/data/nbl_rosetta_preseason.json` | RAW | `944c797e3904dc5a7e8d8eafb738d9b782a5577dbd63d10d0e148d3550fb80d0` | 237573 |
| `research/data/nhl_cache/nhl_1975_19751976.json` | RAW | `2f800cb1a0f6909cdfcc65cb95904ff55f9fbdaa56e86fda5ed60efc08535647` | 1145645 |
| `research/data/nhl_cache/nhl_1976_19761977.json` | RAW | `971eca02ae900f82de3e3c0bb6ddc3783a0d5570ece97e4d3137ce04ca78da9e` | 1113068 |
| `research/data/nhl_cache/nhl_1977_19771978.json` | RAW | `ec7a65f4443752b38aee41c327e46dd9c81281e9e48f137de09de626666422c1` | 1114408 |
| `research/data/nhl_cache/nhl_1978_19781979.json` | RAW | `6bd847a6b5ec7d09bac08065c83968a864c0f7a2b41d2dd3a99f3c978447113b` | 1057187 |
| `research/data/nhl_cache/nhl_1979_19791980.json` | RAW | `4c4909a5d33db321cc9ac865fe2fe8e6f8b171c4dd3fd2e4bc670c87ef80fd4d` | 1333828 |
| `research/data/nhl_cache/nhl_1980_19801981.json` | RAW | `c2c0e7ca4fa292d385ba82e1fb581ce8ebf9b6fe40cc49d5eee7d2d8b6d4e953` | 1341936 |
| `research/data/nhl_cache/nhl_1981_19811982.json` | RAW | `f46e91198c5cd16d8b3db3c76dc33b00935ff294e669d8b6edd469867f81e6ce` | 1352636 |
| `research/data/nhl_cache/nhl_1982_19821983.json` | RAW | `c136e20c05fe1521e2e6c498dfdb472dcb3b5ad3d2e046c598cfbb9567ca354d` | 1331592 |
| `research/data/nhl_cache/nhl_1983_19831984.json` | RAW | `64589b098528799f692a93454acf42e7ded899aab1d77532370eaf79fd42d77e` | 1338996 |
| `research/data/nhl_cache/nhl_1984_19841985.json` | RAW | `0dea52dc4fe4a458f3f6c6ead9039fdabe3d04fa84c4f6077427b50fddb974ba` | 1340632 |
| `research/data/nhl_cache/nhl_1985_19851986.json` | RAW | `1bad246d24d4cbf1adaddabbce4587a54aad43b065a0d3192671dbb394da8c94` | 1342134 |
| `research/data/nhl_cache/nhl_1986_19861987.json` | RAW | `95cf2ca311a51368fb05edfdc44131442e29c48b0b4892f405f6370f0b00bcfc` | 1368638 |
| `research/data/nhl_cache/nhl_1987_19871988.json` | RAW | `84af23373170cbc7e89147a308b61dcdb5d09dcd8c59f7e5c8c3ba36a5a3f0f2` | 1358004 |
| `research/data/nhl_cache/nhl_1988_19881989.json` | RAW | `98728e53e3b7c72380d212acba0fc7997541762e63ab6d9b2f906ccb25f4a428` | 1358646 |
| `research/data/nhl_cache/nhl_1989_19891990.json` | RAW | `4614875bacc5b05e08e841076d6fd7468c21ee0f2f4c783cb7d43be8b1c7982e` | 1379138 |
| `research/data/nhl_cache/nhl_1990_19901991.json` | RAW | `8fb38a18d5c6ce1a66b58fb0240794f9d4e22d79cfb7c8e1ec67fc84211b2a21` | 1392637 |
| `research/data/nhl_cache/nhl_1991_19911992.json` | RAW | `667868e7ed1e1e36efb70c54589d24676629a3eaf8e893a8863e6386695bc4fa` | 1422552 |
| `research/data/nhl_cache/nhl_1992_19921993.json` | RAW | `f11069bc8de7f6bf37a1e99ba47c199b7d97a8d69fe8ac746d23a3416cf7f282` | 1611486 |
| `research/data/nhl_cache/nhl_1993_19931994.json` | RAW | `45dd8ea436845fd87a71bb93c0d17e71da66f7c7caf8808274d0529c30c4b654` | 1737503 |
| `research/data/nhl_cache/nhl_1994_19941995.json` | RAW | `c242833008fc9f8f4c7745434c5ce10768e30826624d7426b13f0588d77b05c0` | 1045583 |
| `research/data/nhl_cache/nhl_1995_19951996.json` | RAW | `972722d017a39174a6fb48f228f1e29a1353d2f4c8969c7e78212f78aecf5175` | 1683867 |
| `research/data/nhl_cache/nhl_1996_19961997.json` | RAW | `27f343a20a396b646a29ed22d3a9ae56d97f369323f0e4ff81fc7d8a0dac71da` | 1675039 |
| `research/data/nhl_cache/nhl_1997_19971998.json` | RAW | `cc5293005b418a1f23bac6f8ca1275a6dd8f417366c1c41b95b90df560ef10be` | 1677945 |
| `research/data/nhl_cache/nhl_1998_19981999.json` | RAW | `44acbd975110b5508d88ae8469353c97047a5e9f011bec94d8ae79e2512b3ace` | 1746027 |
| `research/data/nhl_cache/nhl_1999_19992000.json` | RAW | `1b7d234e536fed5e1ee5121255c8d2e902ac94bc228f536d5ae1495f3d880e0d` | 1779306 |
| `research/data/nhl_cache/nhl_2000_20002001.json` | RAW | `9369dbe52b71576893d2137926f23040d202dda76d1d094cce72c97d9670a094` | 1909760 |
| `research/data/nhl_cache/nhl_2001_20012002.json` | RAW | `90a2a67236d524abbeb6f60faeb56e4fb25b19912ac3de8a9aedd0ebed94afd7` | 1919314 |
| `research/data/nhl_cache/nhl_2002_20022003.json` | RAW | `b818965fa8d5c44771c1229717f6060a5c3f7c4241c137ffdaa5e8630ffb5728` | 1911532 |
| `research/data/nhl_cache/nhl_2003_20032004.json` | RAW | `ba4467fd32bd84b846cc23c25607c4bce74513cd9fffc5d6a54a355d8ef16c39` | 1915868 |
| `research/data/nhl_cache/nhl_2005_20052006.json` | RAW | `875d7da5229cbd8312006cbaaa47ca0b8bd022bf2c3854d1816757a625f8d98c` | 2047878 |
| `research/data/nhl_cache/nhl_2006_20062007.json` | RAW | `9af434d874058b0ec5ff706bb459e6a991f5a3ad401797d2f8392f3450d1d26d` | 2277994 |
| `research/data/nhl_cache/nhl_2007_20072008.json` | RAW | `2da823e63d02f355d3e7f016836c71e136fe36100486fd48c79f4761f49afa0c` | 2420154 |
| `research/data/nhl_cache/nhl_2008_20082009.json` | RAW | `5e226a6314adf627993b552db78ee7237081c6a274689b2121a64ae6e29ccea0` | 2549224 |
| `research/data/nhl_cache/nhl_2009_20092010.json` | RAW | `9cc3b4b16be0d216931651733f905bc5b5ce5cdc93af8b82592626c5c45d1dc8` | 2536290 |
| `research/data/nhl_cache/nhl_2010_20102011.json` | RAW | `53ecb99dcd09adcd85e116d73b2c8c4f0ec74c8c904fa74cb3dc3e8299fc3a60` | 2468639 |
| `research/data/nhl_cache/nhl_2011_20112012.json` | RAW | `9c122e0d02b208ff6e472cbb19271ebab3736db8b4d8e65ab7302b78c383f696` | 2457019 |
| `research/data/nhl_cache/nhl_2012_20122013.json` | RAW | `bb8936544097d700f130b7255db8c898102f39f819fff9ea2a9baa249729f799` | 1435432 |
| `research/data/nhl_cache/nhl_2013_20132014.json` | RAW | `aba9556d37e696a50fe149f6120142adf5606fa7d2b822ff975df399fc28364e` | 2472196 |
| `research/data/nhl_cache/nhl_2014_20142015.json` | RAW | `971c2d8187ee19a0a2aca1392db16df5578044d9c7206f132a7fa3fa58cf051f` | 2480257 |
| `research/data/nhl_cache/nhl_2015_20152016.json` | RAW | `864cd754dd7d8de6737fa74a7ed390784f5b92224a6b11660c2ae4ace7bed5a8` | 2499075 |
| `research/data/nhl_cache/nhl_2016_20162017.json` | RAW | `1affd4b78a700d547e83a8ef78a80173db6bbc4c93295fef5efd3ffe818e519c` | 2468865 |
| `research/data/nhl_cache/nhl_2017_20172018.json` | RAW | `163c1fd16a0272639a3310a30bb0cebe8c7114cea4eeea270c0d4325037ab173` | 2397367 |
| `research/data/nhl_cache/nhl_2018_20182019.json` | RAW | `fdf099b00dfa154f95faac7ad23e56567c177b3a5a938cd48d56eb6f416b6273` | 2679171 |
| `research/data/nhl_cache/nhl_2019_20192020.json` | RAW | `d27722ccf76e6e106cdd647092577aab4765cf38a719771324936b623d23fb55` | 2505838 |
| `research/data/nhl_cache/nhl_2020_20202021.json` | RAW | `a5dfb117c13f1c7362f0ad11e25a409b9cef6b1275147cf84bbbac220b468c8f` | 1808474 |
| `research/data/nhl_cache/nhl_2021_20212022.json` | RAW | `76cec3c0ee32f3bb72ae5a1cd1e9315c2aab968b2c21e939c2aca648251dba1e` | 2789163 |
| `research/data/nhl_cache/nhl_2022_20222023.json` | RAW | `25ed87a10d0b6b849910233ba7151ead9ad674d036e1e432c8fdd45587db894d` | 2740305 |
| `research/data/nhl_cache/nhl_2023_20232024.json` | RAW | `5899ff0cc53a2e0304109af6719e89c41eb71be38b83d584a6513c991e5a9133` | 3044295 |
| `research/data/nhl_cache/nhl_2024_20242025.json` | RAW | `0a25056ee756ed53051b7b66ee7f4e073edd8e62ddeed29adcd1b842fc47a3ee` | 3192075 |
| `research/data/nhl_cache/nhl_2025_20252026.json` | RAW | `5ba5a6b603a5c72d09d7d94f65f10c35f88ebd1fcd3628bcc1d22439f02cf5ce` | 3235733 |
| `research/data/processed/data_manifest.json` | RAW | `129458f7aa9a8bbc776cc1da9038ac916de5601f14138a799a66a63f2212ab41` | 5240 |
| `research/data/processed/epl_2026-27_current.parquet` | RAW | `4d68693c465442168dded8082041dace555b07134b9191dd5ff7ed1e1b221f8c` | 6723 |
| `research/data/processed/epl_2026-27_current_manifest.json` | RAW | `4142ab5fafa4d3d59453ab2c23a21f1c34b332042e19e71d34657084baac4067` | 612 |
| `research/data/processed/epl_2026-27_population_states.json` | RAW | `cab2944e47a17a0bbd0b465453f6a3af3cf446a4a9608afe51aa22a3523ec43c` | 30893 |
| `research/data/processed/league_csv/epl_results.csv` | RAW | `420caddff7da5b36a9c02eac9d365104a9cdbfb14e3612edcf8d7e71e2d91cb3` | 826679 |
| `research/data/processed/league_csv/manifest.json` | RAW | `994e063e09d200139048ad0d156af116f63e0bb956d1c24d45785851b32f7cbf` | 1143 |
| `research/data/processed/league_csv/nbl_results.csv` | RAW | `b9c0e07b23c41bb8f3ed4aa4ab6565b76f980276c10adf4014d304605434f63e` | 295022 |
| `research/data/processed/legacy_learning/cards.csv` | RAW | `4b324b385355ee1fbbdd197f71d4c9b8f8a866d70bb6f2d13c0a936250b7614c` | 61953 |
| `research/data/processed/legacy_learning/contracts.csv` | RAW | `98dc790a5108fe40418989f61c865ad956ceb31ca662a19b33bbb4a4d10b721a` | 831818 |
| `research/data/processed/legacy_learning/manifest.json` | RAW | `7612d91c2a8aabf89f80c0c1ab68de0e1ec7333c593914dda48585dfb255ec2b` | 603862 |
| `research/data/processed/legacy_learning/source_anchor_corrections.json` | RAW | `952155d3740f47b7156137b24181afed6bdb490544a368d31be6999f62c4c9fb` | 31129 |
| `research/data/processed/matches.parquet` | RAW | `d65079171b422c3bcc902d760427f86c385efd6b5dfa4bc1432a645b0d5187fc` | 32072 |
| `research/data/processed/nbl_2026-27_current.parquet` | RAW | `48f743268e6094289efabeac8f9f21cb00bca3439ce34c0be2192ce47255023f` | 6958 |
| `research/data/processed/nbl_2026-27_current_manifest.json` | RAW | `8a334c6bfcb6358ad939c0b46ab363e8b99ef892ac3f3e86172eb689fdb8354f` | 801 |
| `research/data/processed/nbl_2026-27_fixtures.json` | RAW | `d45014ada951875bce187a442fc1bb63c7cae0d40cb14eb5d45101943d6e73da` | 50718 |
| `research/data/processed/nbl_crosscheck_disagreements.json` | RAW | `12ac568a7c1f61bbba85374fafbd48c5c1fd331a163013664b744c6c80ff0bb4` | 35549 |
| `research/data/processed/nbl_data_manifest.json` | RAW | `243cf8f42508af48ac1f4689ba1c6aa3e320caa0999ae0669f78ed48323ea6c0` | 2837 |
| `research/data/processed/nbl_fixture_adjudications.json` | RAW | `8611ecdb77f5775c26f682d9c6a72a63c108deb5c4c60ecab8c056e26e552bf3` | 842 |
| `research/data/processed/nbl_fixture_unresolved.json` | RAW | `a5338d955b09046ec0b16f3a9625b7955c763aae07dc722e474e6078745f932f` | 4 |
| `research/data/processed/nbl_matches.parquet` | RAW | `7c5100c8087864ce9cf9ad1187af171fd90636a2fdbbd58672664a774704bff1` | 46817 |
| `research/data/processed/nbl_source_manifest.json` | RAW | `a045cd3bb105c8ddad379c38b9db4016ffbd62591fdd66bbdc5804db9386e167` | 3203 |
| `research/data/raw/nbl_official/nbl22.json` | RAW | `68da84ccbcdc6d792f8287d1b8d7d91b81ee2f27f4668c98f7db50e72dba464b` | 262082 |
| `research/data/raw/nbl_official/nbl23.json` | RAW | `e625cad7337da879fa3ada11023ed82be8e784d7071a064c3e7775879a62e654` | 285035 |
| `research/data/raw/nbl_official/nbl24.json` | RAW | `3c07082276652970b339958a037d101a8334ca3ba80bc5664853e3825b97640f` | 286143 |
| `research/data/raw/nbl_official/nbl25.json` | RAW | `f29f95efaae1b4191597f42726f17c0aa2241919d3bfada05e356b9fefb7248f` | 284407 |
| `research/data/raw/nbl_official/nbl26.json` | RAW | `25b65a979dc5c810bee0474acf1844f976f20c51747791650c76c4e424f71b9e` | 346246 |
| `research/data/raw/nbl_official/nbl27_20260929T045201Z.json` | RAW | `ebd96fb54bd13ca61ae1202a0d1a9ed6a000e2708f4599bb9a20b773b943c448` | 320704 |
| `research/data/raw/openfootball/2020-21.txt` | RAW | `2123fa19c676d0194c69380dceb61f9413bfe6b89eb6c538cd269d8d856ba255` | 27068 |
| `research/data/raw/openfootball/2021-22.txt` | RAW | `592df232fbc7c2f36ec3e643eef608f77fcbf7d8da0706c94c99248d60b932b3` | 26953 |
| `research/data/raw/openfootball/2022-23.txt` | RAW | `c85a2f8ac64975435b8359eb923eaa09e48f33d47672c8b32d2c6e99a8cec5f0` | 26495 |
| `research/data/raw/openfootball/2023-24.txt` | RAW | `0bfb4a7fffe0b1bf7318955686eafeb28fc9676346ae433259e7409d69551450` | 26357 |
| `research/data/raw/openfootball/2024-25.txt` | RAW | `e39716b01af0c8654a9fae7b5555e6b02f506ea05239e0d0eef41936ba80e1e3` | 30316 |
| `research/data/raw/openfootball/2025-26.txt` | RAW | `38c1de56c9e9b6662c7efc1420b7e1fe00dddbb502fe72d8f759e773ba3c093b` | 51782 |
| `research/data/raw/openfootball/2026-27.txt` | RAW | `a2366ea9f7f55b8afd666e455666ba9019f9c62da8864f6bcf3adff65300b445` | 22800 |
| `research/data/wiki_cache/ACC_Championship_Game.json` | RAW | `80c22fe3e8b5db02fa6685d25b7c953a78738c6840564bb9fa87caf762b956f2` | 46505 |
| `research/data/wiki_cache/Big_12_Championship_Game.json` | RAW | `a1ac708fbd62240f1f1b71b07ebf94b012e2167cfc70f939378ee9448777ccea` | 29865 |
| `research/data/wiki_cache/Big_Ten_Football_Championship_Game.json` | RAW | `47837db6b3ad86064d86cbee69819fb346afccf75942d071f8515ae4d537f121` | 44158 |
| `research/data/wiki_cache/Chicago_College_All-Star_Game.json` | RAW | `f7ce59fc522aecd866dcab8d1bf041021d817461a29c50e21f0d2ce2d73f9257` | 39381 |
| `research/data/wiki_cache/Cotton_Bowl_Classic.json` | RAW | `1aa0e6f1d1bd10fb6ce79efe62b8326dfaf05b3c6ee12fb5d89c4697ba08ccc2` | 95995 |
| `research/data/wiki_cache/Fiesta_Bowl.json` | RAW | `5eed8bf710c593c1c457da24a3ec58f8f203107066e127400c2290714b1eb8fb` | 75449 |
| `research/data/wiki_cache/Kickoff_Classic.json` | RAW | `cf34c95f96bf6279aa15e0d6f39a6d3351261553f12c2089657cbb479b9966c0` | 10672 |
| `research/data/wiki_cache/List_of_College_Football_Playoff_games.json` | RAW | `a8504ada47bc1beccc8a228209dd67963e6f1fe617a91cf6ffecf628dcec3fff` | 28669 |
| `research/data/wiki_cache/Orange_Bowl.json` | RAW | `d6bc9956562787d70a3d6a231888e2dfd796a9c760f2a73bd5b7b91d7c0e8607` | 73355 |
| `research/data/wiki_cache/Pac-12_Football_Championship_Game.json` | RAW | `d9b370fb5356cd2d0ce1febf5c98ff80fd75238bf4e4e8b68d57d3ec038e8d12` | 36551 |
| `research/data/wiki_cache/Peach_Bowl.json` | RAW | `d8b5c6d214724400aa715318b973a668c6f77d06aea2d7b841f52a497941ac92` | 55251 |
| `research/data/wiki_cache/Pigskin_Classic.json` | RAW | `6debcb576205ac297ce0d35810517cd4c83bf96f135f2c0525c50f52e8d0a905` | 8788 |
| `research/data/wiki_cache/Rose_Bowl_Game.json` | RAW | `069dd53ee6be70dffb2cb3f0603824ba5b124cec69d60527bc12d44e231a9ad8` | 145909 |
| `research/data/wiki_cache/SEC_Championship_Game.json` | RAW | `9a2b86e628b08a837b97ed86dbf6174b6c59125037f471989b05892563946909` | 36286 |
| `research/data/wiki_cache/Sugar_Bowl.json` | RAW | `28d2743b14283a818d2019210825a2814d4fa90af41b555fdd1125da16180028` | 70957 |
| `research/data/wnba_cache/fivethirtyeight_wnba_elo.json` | RAW | `fb7f11f6b5cd4712f1ea5ebe67e576bdc5f20ff5b0fd6a819b6e29418fe295d7` | 3242558 |
| `research/data/wnba_cache/sdv_wnba_schedule.json` | RAW | `0b72d7d23580271ea56fa094b8ba9539cd2c5ae16bf1e5b4687228ff76191794` | 16373432 |
| `research/EPL_EVENT_RECEIPT_TEMPLATE.json` | RAW | `25f25678011b2f9150d815994ba786803c99b4d3db21d5fc85490ad825c8ffe8` | 444 |
| `research/EPL_PREREGISTRATION_2026-09-29.md` | CRLF | `ad08fbaa6436d90aaee89948fc1347d99b3c6eb1eef787f96faa34e974157637` | 4134 |
| `research/issued_research/P-523-0fd247ea4c6b4450a37b7bd6e32e1101.md` | CRLF | `3eb0170377235649de31838e7131d3d4f972fdcd63cdca76c7987e325a238fd3` | 13996 |
| `research/issued_research/P-523-0fd247ea4c6b4450a37b7bd6e32e1101.original.txt` | RAW | `f7082acc7acf00d452ab05511c1b23f29e21615c1247d2ea5fe9fb9d52a15c6c` | 11938 |
| `research/issued_research/P-524-427e10b469894624b66263c57b5b4561.md` | CRLF | `1d77974347c5d352ff88a9884b92265409a8408cb8f4b53e543d28e2c8029f9c` | 8932 |
| `research/issued_research/P-524-427e10b469894624b66263c57b5b4561.original.txt` | RAW | `555aa41eeedd9c7d8c84850940a93287fad1cc8e7264cf3b063178bf9eb5f47e` | 6803 |
| `research/issued_research/P-525-86ae2a4dd237491d9f37cfce0da5f9fd.md` | CRLF | `01dfce60537e960af6310f1d0aa5b4720842ff8e7f9428e69896467acc2c011d` | 14448 |
| `research/issued_research/P-525-86ae2a4dd237491d9f37cfce0da5f9fd.original.txt` | RAW | `516cecdbf710d01ed00dbc2b89135e8f9970961c82e6177303946aae65efcbda` | 9657 |
| `research/issued_research/P-526-0676a2a79b094ceab6433c33bd800263.md` | CRLF | `6730a6a46b2901715a7a3aa6552a708c2ccbd10062bbf8d86b082a9c239ed7e7` | 18725 |
| `research/issued_research/P-526-0676a2a79b094ceab6433c33bd800263.original.txt` | RAW | `ab237649f6f9e753df6a9edb25f9cb55cf2ee9a3ae55e582e86de71c97aa9ff7` | 17890 |
| `research/model_builds/build_2026-10-01.json` | RAW | `010d967885b384cd7798601f7e818d1a948551808433b273cb37af18fa7cf2a3` | 37808 |
| `research/model_builds/current.json` | RAW | `010d967885b384cd7798601f7e818d1a948551808433b273cb37af18fa7cf2a3` | 37808 |
| `research/NBL_PREREGISTRATION_2026-09-29.md` | CRLF | `54e648ef5b5be9a0c57e010064af2b8083c53cc90c2857f5967e51f1cfcbffba` | 3659 |
| `research/operations/__init__.py` | RAW | `795ce7adcfdfd3a2924e77be565e0d84a0d079b50c5cada2984c57e7d3a4b89f` | 83 |
| `research/operations/control_freeze.py` | RAW | `602a384a672e4af252f40dd2325093f6696c68b780d737da245f1add32f72ca4` | 2205 |
| `research/operations/log_card.py` | RAW | `3282cffb15f85c2383e02872d99c7244db9afbba1cd23079e8da476d7c550b3f` | 12146 |
| `research/operations/test_log_card.py` | RAW | `c214e0d1c81f353cdc87e9fc80aa426ae0dee06f6b6261b4eb27ba09794eed3e` | 4388 |
| `research/operations/verify_custody.py` | RAW | `8b42304288b55478e4b6bf937d7daa3e99591d00eeca689be9051aa2852176dd` | 1565 |
| `research/PILOT_LEDGER_TEMPLATE.csv` | RAW | `3ecc0f6ca55e1c83c8f0b7696ac5b6e52617232dc9ac707f8a09d28117121091` | 544 |
| `research/PILOT_LOCK_TEMPLATE.json` | RAW | `1d104394448726c1d59d0f3e40f4478354ead06e633237b98497c9b9cb2aa649` | 1081 |
| `research/README.md` | CRLF | `c60848c98a0f9a3431bf583fe2e8c72b6245a50609c0f78602f83137bc7467d7` | 11161 |
| `research/requirements.lock.txt` | RAW | `508a508c3effa08821e9fe17d87ef1204ffd5c8aa9069e4788401906c7120301` | 280 |
| `research/requirements.txt` | RAW | `53b1e4cddadb065e558976db559b51444afbd91602ec73775f690b794addb0b9` | 74 |
| `research/runs/epl_2025-26_closing_benchmark.json` | RAW | `a5cc3f197effca26ea96b47943001fb8c3d6e7195a090ed1100288b20af45b54` | 444 |
| `research/runs/epl_2025-26_holdout.csv` | RAW | `79affa039094859c84d7dfff8114f30aef9f70d86b35e8a53217fb4e14d0008d` | 130428 |
| `research/runs/epl_2025-26_holdout.json` | RAW | `5cadf89505287a18a84f3db2db1bdabadb59431b9f225b1bc4ea9d5e397774dd` | 3782 |
| `research/runs/epl_tuning_lock.json` | RAW | `adbe0390675be8da4e19176e52a6c7691b32b816084301a6741ce67e86aad553` | 1033 |
| `research/runs/epl_tuning_xi_0_001.csv` | RAW | `13a8eb8a5e2dc2e8cf59797cb3ef3fb9051e78cd3db6fb503072e834807c1125` | 520858 |
| `research/runs/epl_tuning_xi_0_0019.csv` | RAW | `0e748659d76226fc10f40d31e046e95b91caa7646dd3fba0d6cdd211f24fcfd7` | 522333 |
| `research/runs/epl_tuning_xi_0_003.csv` | RAW | `5f27f9a62fb1377686cb8d7b1e40437d649685f681c2712e16c8fb608a86594e` | 521507 |
| `research/runs/evaluation_environment.json` | RAW | `e5f6162fe671daef0ffa62cffb0ac456c72e76714ba863a11c17e31d5c97cbb2` | 1114 |
| `research/runs/implementation_2026-10-01/development_protocol.json` | RAW | `beb2e2b8470f33da78e6ede346904584f22db612916d339c978f7dbe69b0f108` | 2534 |
| `research/runs/implementation_2026-10-01/family_diagnostics.json` | RAW | `9a8f0cd7539129720510b932796ed16bd544634dffb37d2fd56b15b1aa64446e` | 112170 |
| `research/runs/implementation_2026-10-01/family_forecasts.csv` | RAW | `17de2c5536f03a8e5005e0ec2af2c32ecd82f9efcbf430d230d5347306bdeac5` | 7295880 |
| `research/runs/implementation_2026-10-01/source_observations.json` | RAW | `b2aa1a937a06aa72300ddce52edecf152d85c4bf54fc893147951a3094d78877` | 13984 |
| `research/runs/nbl_2025-26_holdout.csv` | RAW | `f9c8a0912f968304f1c1910e4b7cd2728f03e910ba3a1bb28cc92848e9b70092` | 50641 |
| `research/runs/nbl_2025-26_holdout.json` | RAW | `cacbda05740b13543d27facdf5771497be37866eb55f4a71c79c0fb554addabf` | 2462 |
| `research/runs/nbl_tuning_half_life_180.csv` | RAW | `939954cadca623c7a44de441695149a16b108cf52f6693045b97753d1e71b150` | 129673 |
| `research/runs/nbl_tuning_half_life_365.csv` | RAW | `9a08fc4ed5a6283ca2728008316ec5022cd37b1d0dd5406c65fab713586193ae` | 129684 |
| `research/runs/nbl_tuning_half_life_730.csv` | RAW | `cbb97f6732be9c589b1d6ada7c3def1b0485ebbe159d9c9c0124c44d045c3d42` | 129771 |
| `research/runs/nbl_tuning_lock.json` | RAW | `f0d4c03c65fabdabb49bb2eee6ef275c29f806c457943f7dc659692c3183e7e0` | 1307 |
| `research/schemas/baseline_definition_TEMPLATE.json` | RAW | `14290f04e6ec0a7a5d8a41f977df12fe910c3337ae56a492c3f89e2cd08e46f9` | 1221 |
| `research/schemas/event_universe_TEMPLATE.json` | RAW | `fea659a9005b2a5144a5bd4b29f88fdbb48a33c9c57b9a68dc18ef049233b59d` | 700 |
| `research/schemas/forecast_evidence_TEMPLATE.json` | RAW | `eb8b01aa1120b510ad74def18ae7b8e9225c6825a3e369da0e605976313a759c` | 2177 |
| `research/schemas/live_qualification_TEMPLATE.json` | RAW | `8cad4cdedffd1a23078243f9209c3480e5d910b73d4f2f133809a3a0692bc261` | 1193 |
| `research/schemas/pilot_lock_v2_TEMPLATE.json` | RAW | `37dde4c8baed4ea4c79df72945ccef655e74a214718c9a5ed471257b9577c8cf` | 1040 |
| `research/SETTLED_OUTCOMES_CORRECTIONS.csv` | RAW | `57a8b7491c0f6205ff3ecdf643b698745be6b84f26bf71d6393015b08c580710` | 27219 |
| `research/SETTLED_OUTCOMES_LEDGER.csv` | RAW | `8dd7c0ecf1d4c59b062b6e966e35e93d1040c42e96746fac581f34c2eb0383c9` | 188510 |
| `research/sources_registry.json` | RAW | `031ca77a5d8fb791c3f0dc9e8fecd62e7cba5647ba7ba63ddba11cd2817f4716` | 12113 |
| `research/src/__init__.py` | RAW | `b23cde9797abfb99fe132a2d5b863c26e574bfe947c90c62b8586fdec8172661` | 72 |
| `research/src/acceptance.py` | RAW | `c3a6e80161d14506fac2c9cb1947a5140f4ca3d4cbbe1a21b63d2a4f8d7f83e7` | 4980 |
| `research/src/archive.py` | RAW | `59399ef295a973520bd0a4a9e23cfaadf27bc3ff8175e1e9ef00358b72d11d8a` | 42075 |
| `research/src/archive_sources.py` | RAW | `0ab83e2479c21e9b4c08725ebcbce556f2cda6466d0e05360296f75dfe73f2c3` | 19860 |
| `research/src/baselines.py` | RAW | `6dee712ca36b14fb6261b8ab60f94690d3e2fe9085d8961933dd31a43d37d011` | 2650 |
| `research/src/benchmark.py` | RAW | `9e5a0815ded279e0cd68b906472ba04bd428815c8cce58e5c064c89893000ab8` | 2708 |
| `research/src/build_afl_all_years.py` | RAW | `e3778a500a3b9bdb15b40dc2c319e15ff361c15e1ddf81c3daf5d6aea3feeb8d` | 794 |
| `research/src/build_aflw_all_years.py` | RAW | `e3778a500a3b9bdb15b40dc2c319e15ff361c15e1ddf81c3daf5d6aea3feeb8d` | 794 |
| `research/src/build_cfb_all_years.py` | RAW | `e3778a500a3b9bdb15b40dc2c319e15ff361c15e1ddf81c3daf5d6aea3feeb8d` | 794 |
| `research/src/build_eurobasket_all_years.py` | RAW | `db8e53a73ebe88b345db8f154564bd07dbad3c4448d27c2f826bfad769223c31` | 18278 |
| `research/src/build_euroleague_all_years.py` | RAW | `24d9d1b5d37f2fdb4bfa0108582842c2fdff81ca7e228085b1943a4396901d1d` | 12708 |
| `research/src/build_nba_all_years.py` | RAW | `4f9ad25bb5b3804bfe5dcfd4b321acb7142733b6c1b62a9f1f310f39d1206566` | 22346 |
| `research/src/build_nbl_all_years.py` | RAW | `a11a03b9473e9850281be475408c59ab4abcf9f40a21deac196538e8ae76a993` | 19505 |
| `research/src/build_nhl_all_years.py` | RAW | `0ba602fe7b1d47709dca3da479913bc01f536e18e0f1438e26132b4953c47b32` | 18000 |
| `research/src/build_wnba_all_years.py` | RAW | `37bb3717557bf278c6d4c9a937d88ddbbe748c21f228af74c30571a8cc7018d5` | 21563 |
| `research/src/builds.py` | RAW | `24243fc940516a8ac647e38173ec4cfda13d6bbe96c79ae5641c12554daf429b` | 2523 |
| `research/src/candidate_models.py` | RAW | `54fc8cb4b6c80ec4ae517ccebc774dd47bab096c844f732254f22363cec320cf` | 3768 |
| `research/src/collect_cfb_postseason.py` | RAW | `a7cdf97b9f459dcb96e34c9073008aefddfef661dbebd60f9e02e06d553c56e1` | 358 |
| `research/src/control_manifest.py` | RAW | `ce751b7d61445f1795cd8f483ebe40db428115472ed90fb7339ac197efb59458` | 4844 |
| `research/src/current.py` | RAW | `8981ce6fabcd7133690f0b9691024895b0948ad27215bf414e7321cf65ada289` | 816 |
| `research/src/daily.py` | RAW | `4efe15f0e234f9fd706bb0998256d61bf8c84f7b3f7474d24bbf2faf8cf600f8` | 16508 |
| `research/src/dixon_coles.py` | RAW | `3cb47e0845b558fecde03f9c1f4f14b730964f82a6b3cef79474962f73d02f1f` | 6062 |
| `research/src/draft_epl.py` | RAW | `4eb2b0413b67f13a9eec0be027ab38e0e3601cda11196e01845f7c223ccee442` | 6237 |
| `research/src/eligibility.py` | RAW | `fb99aea052d9e5a61c52b30de1545591876be3c142dfd792716ae97566028923` | 34812 |
| `research/src/emit_card.py` | RAW | `e498109374de6160912233f00401551a5b7a0ba2a5e43fc4df835b3b710cbe81` | 13388 |
| `research/src/evaluate.py` | RAW | `bbd6086a55dcd427f60dca6c06fbf6348600ed551096f40831cf015323c4d38c` | 8536 |
| `research/src/export_lanes.py` | RAW | `dbd4434d2fdd46fe2bb35875260b34f7cc5e54692448eb486a9bd1b1fcc9e8b9` | 3331 |
| `research/src/features.py` | RAW | `73b8ff815b9153b1f16d168613fd754df0bef4923cf0c9d09d80137e6017d006` | 2321 |
| `research/src/feeds.py` | RAW | `8088078db9709fd6b353df69393574fcb91091a7a7c06ba4e54d0d4196278b96` | 5343 |
| `research/src/fetch_all_eurobasket_data.py` | RAW | `1de39513d359a6456a5d4784bea6c456c2894a2ea9e27bb425a816d7ef0428d4` | 12582 |
| `research/src/history.py` | RAW | `a99f2f672e5c7b8109819d2b4c8d2cdab5357a63cf0dd4b840f208e609a8711e` | 7619 |
| `research/src/issue.py` | RAW | `e3fa2f728b5972c30f1181c7d7be93ec16c805d9a9afcf6a537071b65f6c2cb5` | 17728 |
| `research/src/ledger.py` | RAW | `93e6c2bc5719ebaaa683980dd93d0744bbb8039f9072852a3c7516d91ebe9f16` | 17397 |
| `research/src/legacy_ledger.py` | RAW | `e2b013472443b120b39ea37ca4becf5b819a7b990b811ba92b5c8d3685e3fd9d` | 6657 |
| `research/src/load.py` | RAW | `647dea85c5ff32b64c80b356c61c784280a77362e3a958fea2ef73b5350229a4` | 8309 |
| `research/src/model_custody.py` | RAW | `5d8fbe259eb63a9626ab681714ef27e629b97cef4b2986e9b53dc0ad3f51c51b` | 1437 |
| `research/src/model_diagnostics.py` | RAW | `5bce08f668b50979e8467b21e875b29477c597e787e6d46adfa9aeca00af99b6` | 13248 |
| `research/src/nbl_current.py` | RAW | `beb82126b25fd642bd21995284e80f84299114b45a6e5f1deb4ece06199d36fe` | 798 |
| `research/src/nbl_evaluate.py` | RAW | `273d6d44160100d400534ac81a0146f901641530d3a50ad69f0d61655fa7328c` | 7954 |
| `research/src/nbl_load.py` | RAW | `df16d1414b21bb375e3170c28f585ea7bd1a1369a8f8637e159c6f9e168a2bdd` | 11681 |
| `research/src/nbl_model.py` | RAW | `3fb4df6ee26c8405b2d633edfbe4911acdbfd739dad55bf480214b9c3de10ffe` | 3994 |
| `research/src/nbl_shadow.py` | RAW | `3a0d67573d986ed5ff6619fcf887c7fa7419a91a86858c69ab3d959c0f2bf6ad` | 5328 |
| `research/src/pilot.py` | RAW | `32d1bc35a532b11eeec07df91cba704036e76953699dfcac484c175bcdad40ce` | 24643 |
| `research/src/point_in_time.py` | RAW | `0c0b145165ba7b95bb98ae7fb7b66f0b90909e4d8c43a618bd3c54b879e9fd04` | 4924 |
| `research/src/settle.py` | RAW | `11832435f3fea9eb7226cb2e9002a18c75e1495c142d58ab2f891432e1545807` | 3403 |
| `research/src/sources.py` | RAW | `4928f3cdbd8e16ef9719626c9c4253281c4e55426f556be6896daf4a40714757` | 7903 |
| `research/src/sports/__init__.py` | RAW | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | 0 |
| `research/src/sports/base.py` | RAW | `e778ed1ca9d2dd2cdaea205f82fa32367701f548444a9a8d3e5f388768fb5a82` | 1702 |
| `research/src/sports/basketball/__init__.py` | RAW | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | 0 |
| `research/src/sports/basketball/joint.py` | RAW | `f89d50cfcbcba80abae4a2a421fcd522f469c9b48bc757c7855f179992e90658` | 2791 |
| `research/src/sports/soccer/__init__.py` | RAW | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | 0 |
| `research/src/test_parsers.py` | RAW | `367582248a108e164c96240a1e181d611552ee0ead6acf00cd0d70116a51cdd2` | 444 |
| `research/src/workflow.py` | RAW | `1efe59fea667920e33ebe8d203036709f6141cd1b4b0653dc8d427c4ad09ef53` | 4430 |
| `research/tests/test_archive.py` | RAW | `f56538d21c6309d29312244bc5939a011e4083978ef53d78e967c5117b9910c4` | 16298 |
| `research/tests/test_custody_and_history.py` | RAW | `85ef4667e799e18568c93eb8241d51240fba3bc18c6bc6acf28fd09f6e3cdfe2` | 2088 |
| `research/tests/test_daily.py` | RAW | `e8018cf10ff64618b20966552d6c6e312b189aa8e8fefbe65a804798fb8dad33` | 1764 |
| `research/tests/test_eligibility.py` | RAW | `39b87d4973cbdb038ca0c638d069d10165a0b4b13831e233ad2b3e277e4b4b70` | 27524 |
| `research/tests/test_issue_ledger.py` | RAW | `560fd8f8fd13dfdfca250de506df67b453c3f8c82191078427d81fe72604be33` | 7595 |
| `research/tests/test_model_improvements.py` | RAW | `142d2354f2b03ed8d046f7a7b9c3cbb7f09845da8899d649781fdb9690d26560` | 3888 |
| `research/tests/test_pilot_controls.py` | RAW | `6a9e1e434dcbe677c556eb0aa42390e6cca0d0e40b1ee17639cf896e10e7ea45` | 7549 |
| `research/tests/test_pipeline.py` | RAW | `ab0ff2fa1e4d6c8df67e13ca7d1c3fecab27cb245d98f2d7610cd47131f94072` | 14066 |
| `RULES_AFL.md` | CRLF | `c367f289ea7544404082629e67fdc648ed2e87c1256ecabdc2072dfdd41bff7f` | 38453 |
| `RULES_AMERICAN_FOOTBALL.md` | CRLF | `e771edfc4432d079d8162e18118d4c40ce1da7523fd069806c65b72b781c1816` | 44446 |
| `RULES_BASEBALL.md` | CRLF | `bce91cadc3bee101e38a1456a21c70cf4348d664275b700cc9fcc8a23b373211` | 63672 |
| `RULES_BASKETBALL.md` | CRLF | `607a458afdd6af9ceac44a19723f4db298a3d6220b14d6dd2193df896b13e456` | 49038 |
| `RULES_CRICKET.md` | CRLF | `093399a1231c332eda7d8036dda25598a2c2092a2c4512e55e522f8c410a569f` | 58174 |
| `RULES_ICE_HOCKEY.md` | CRLF | `cf0bbf9eaa82ae40b2b213a1ee7429ebb631407804a30bc1afa7b05caa6da492` | 37306 |
| `RULES_NRL_RUGBY.md` | CRLF | `d5d231e5916f50bf5f1ac3eb0eb185d37d592360de6595b48eaa5486875a8c1a` | 35904 |
| `RULES_RUGBY_UNION.md` | CRLF | `07c959c19e521921fa22c9653cada87c019e2fc4b5f331f4212509fc4640a4f2` | 35129 |
| `RULES_SOCCER.md` | CRLF | `2243ab2944c988a0a74f00e4aaa4edd056668173bed410f9bdfda8775d526c2b` | 43497 |
| `RULES_TENNIS.md` | CRLF | `7a20d6e49f970d8a43f70927d97c9ddcaf58d1393ab4878d1887a733366be1e7` | 44547 |
| `SCORING_AND_VALIDATION.md` | CRLF | `a7fb8687a0009cd99b3cfdd3395fdee8943723efb4747c7e7d161aee192d14ab` | 6797 |
| `SKILL_BASELINE_LEDGER.md` | CRLF | `b73977044b45d1bd0269e2017093a144ce0ceea484a909ac01c2eedd17e765c5` | 13159 |
| `SOURCES.md` | CRLF | `781d603b379b5bfc58fb8495c57dc4df956c0d21b4fb8ccdba721b465897e9ed` | 130931 |
| `VALIDATION_EVIDENCE.md` | CRLF | `9021401cc30d19d4276db8b49887a833ffa2d69b9871362686d66ef1fac07294` | 51224 |
| `VERIFICATION_PROTOCOL.md` | CRLF | `621be3c63d0af1e0a86a88ecfcdedd078be4350969c5ee30df57c7ab16566837` | 3160 |
