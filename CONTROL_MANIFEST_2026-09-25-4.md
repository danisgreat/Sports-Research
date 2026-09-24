# Control manifest — 2026-09-25-4 (post-settled-row-review content receipt)

Method: **MDS-2026.09.19-v4.3**
Control revision: **CR-2026.09.21-3** (label unchanged; content receipt under the same label)
Status: **CURRENT post-write content receipt**, generated 2026-09-25 02:25 AEST by `tools/make_manifest.py` from `CONTROL_MANIFEST_2026-09-25-3.md`.

**Purpose.** This is the byte-level SHA-256 receipt that every new card freezes (`METHOD.md` header; PF-7). Relative to CONTROL_MANIFEST_2026-09-25-3.md it adds the 2026-09-25(d) review of every settled log: the settled-row dataset scripts and findings (research/settled_rows_2026-09-25/), the controls C-PLUS-CUSHION, C-DEPARTURE-LEDGER, C-TRACK-RECORD and C-LOW-RESOLUTION-BAND (audit fields DL and PC), the SCORING_AND_VALIDATION §14 review standard, tools/card_math.py and tools/calibration_report.py, and sport-file track-record sections. The regenerable outputs settled_rows.csv, conflicts.csv and coverage.txt are deliberately not hashed.

**It does not change any forecasting coefficient, probability cap or ranking override.**

This manifest is excluded from its own hash table. The living logs (`PREDICTION_LOG_COMBINED_5.md`, `GAME_LOG_STATUS_CURRENT.md`) are a write-time snapshot and change with every card. Hashes are taken in CRLF form (`tools/manifest_lib.py`); verify with `python tools/verify_manifest.py`.

**Changed since CONTROL_MANIFEST_2026-09-25-3.md (by bytes):** `README.md`, `METHOD.md`, `CONTROLS.md`, `RULES_GENERAL.md`, `UPCOMING_GAME_RESEARCH_GUIDE.md`, `SCORING_AND_VALIDATION.md`, `LEARNING_REGISTER.md`, `AGENT_ROLE_AND_TASK.md`, `EXTERNAL_LOGGING_WORKFLOW.md`, `RULES_BASEBALL.md`, `RULES_CRICKET.md`, `RULES_SOCCER.md`, `RULES_BASKETBALL.md`, `RULES_AFL.md`, `RULES_AMERICAN_FOOTBALL.md`, `RULES_TENNIS.md`, `audit_card_controls.py`, `test_audit_card_controls.py`, `NUMERICAL_PROGRAM.md`, `PREDICTION_LOG_COMBINED_5.md`, `CURRENT_RULES.md`, `CHANGELOG.md`.

**New in the receipt:** `tools/card_math.py`, `tools/calibration_report.py`, `tools/test_card_math.py`, `research/settled_rows_2026-09-25/README.md`, `research/settled_rows_2026-09-25/extract_settled_rows.py`, `research/settled_rows_2026-09-25/analyze_settled.py`, `research/settled_rows_2026-09-25/analyze_supplement.py`, `research/settled_rows_2026-09-25/analysis_results.json`, `research/settled_rows_2026-09-25/supplement_results.json`.

**Dropped:** none.

**Unchanged:** 60 files.

## SHA-256 file receipt

| File | SHA-256 | Bytes |
|---|---|---:|
| `README.md` | `e535867cacda8142a775b05b15bec2c151f0c7617986c995ddd1fb1c4b1fbd0c` | 9572 |
| `METHOD.md` | `5eda6881b9fb9cee169fee34f1f2e0f90337945d55ff6cf36e3434986ccd2bfa` | 27948 |
| `CONTROLS.md` | `74e911978b7792c99f34a38e625a6d694822de77126b23c8ecc746cf2a2d9ace` | 37139 |
| `RULES_GENERAL.md` | `c2cd4512de7f2cf395ec249b6dc738350cf2269b12fd4bedd4b3b5b7a5077e5d` | 254443 |
| `SOURCES.md` | `d61d60ff50b77bbffd5c8d7aca92060b13a60cd2283a5b0cf9f79df771fdbd60` | 74808 |
| `DATA_SOURCE_REGISTER.md` | `7fec3e934a43e2a0e434f9d08571b2bb48d92142a36035bcc382f1f8a24b70a1` | 175090 |
| `UPCOMING_GAME_RESEARCH_GUIDE.md` | `bf75e8294dc654ada60bbb773708448c844cd6b790f890c308edf9a2217f5eb5` | 72868 |
| `SCORING_AND_VALIDATION.md` | `95432ea9e75fa777d35f77e123f9cb3f3f9e732af95985833a3fe46a320b76f2` | 19679 |
| `PERFORMANCE_ELIGIBILITY_POLICY.md` | `a102c231debc12253accf5ade0ed3086c7b51dcf3959e570129ad8b6d96dd2fa` | 19422 |
| `LEARNING_REGISTER.md` | `d3adc8050668e3cce404d8e82ebdf2e5eb90ab3c25dbc03a1a81064a870c2e7d` | 304823 |
| `AGENT_ROLE_AND_TASK.md` | `60e5b779b265e217611a41f8a118de364aded22cce71c193c357c4e588ee4bbf` | 24929 |
| `EXTERNAL_LOGGING_WORKFLOW.md` | `8745cb2140fb37d670d52958d3e076caf18913d70c2a5bfe203ccfdacfaf01ad` | 66312 |
| `FORECAST_PREFLIGHT_MANIFEST.md` | `34718b2faca3276e7213bc622e01ff06998151390f5f7c3f12497082e7468678` | 9309 |
| `RULES_BASEBALL.md` | `a2f2a7bb79719887c6461117b2e5c41caaa8b6642614366dac4cb8ee70de4c47` | 124919 |
| `RULES_CRICKET.md` | `6e3357713a3b26da01115ecd0b833dc51bb64c3dd103b9f0aa4569270ea1d1aa` | 102990 |
| `RULES_SOCCER.md` | `3607d8b7f734f6794c6ba3fcd07fd397ab52723a22e2468d1beeb81549b2c9f4` | 100429 |
| `RULES_BASKETBALL.md` | `bb7f5f267c34361b31184f5c5a68e004c7e296bfca3ca9cebddfcf09b5c72f3f` | 95185 |
| `RULES_AFL.md` | `122c5df22823314c675af728433846a090c5ab2ea536d6bf5ce323d7d9fd5ef1` | 56863 |
| `RULES_NRL_RUGBY.md` | `b6acc1208ea9e9b770b4c2cf8efb3b39ba83ec56e685dfefcbcc06ea930a2ea1` | 54722 |
| `RULES_RUGBY_UNION.md` | `57d4108f24dfc854691f0bd0d400c8603fc8a03c812537478f7a5e0982890adf` | 49313 |
| `RULES_AMERICAN_FOOTBALL.md` | `b2e2930c0a1f2f22370f9cfc86e76699e92dadfc0f9b2e0a88acbd7297797ac7` | 60718 |
| `RULES_ICE_HOCKEY.md` | `a58401086cb63d3996051c5c7cf07df4b9c702f2f7d4db8a6d7704f6482c8b80` | 54593 |
| `RULES_TENNIS.md` | `d28fe0b56bc3b93a78edcdc4e660adf2389ab4ee13e57024895d85cf7b404676` | 69877 |
| `LEAGUE_RULES_CRICKET.md` | `b6b13dfa72047b62fd9987e21daa0ec25510ab0853ebbac461b5725de5f99099` | 26252 |
| `LEAGUE_RULES_SOCCER.md` | `236463054f21792ad091fd3f326c7cb12aac767c933ffc4bd2e265acf55df06b` | 43865 |
| `prediction_preflight.py` | `b4d07fef54e71ef8478c5b2cec3af15c5f5accf50ba3e703348ab16609006d26` | 29319 |
| `test_prediction_preflight.py` | `c91ef73ac3faa420e3b67f8e5f345a851c4f9a69e43e75c21be6d3c7a53d5d60` | 11403 |
| `audit_card_controls.py` | `31a22a07cea40ff7b7bdfc300b6cb449ca707d43ac631ac3711d35dd5142d794` | 30337 |
| `test_audit_card_controls.py` | `140307c2849d5e6f45b36fd1e7cb14498cb1c3deac10b857dabc4ec3fa6e9248` | 13375 |
| `receipts.py` | `33c906e5b6a0f67ffaf103347f058955401923a3cb57ee43158cd7f2d1b3de30` | 21886 |
| `test_receipts.py` | `c841b495300f0e7e7afec7f4b24b1780c6a879b0067ed5b648a800625cee3c08` | 6502 |
| `H0_DATASET_CARD.md` | `a2d44c60788d0506c1108e1629fb2a2e6ac23d6fc41ca87c2e27a6d138152278` | 19413 |
| `NUMERICAL_PROGRAM.md` | `bd82f29e15cab12853a9a05cae71369219284cc639d8a9735b6b845c55682d99` | 11311 |
| `NUMERICAL_MODEL_REGISTER.md` | `7fe3f9ecfb51f0e0519ef8d91a857b0038393cdb2546fd2a1b3ee52966aef968` | 22540 |
| `NUMERICAL_TRAINING_SPEC.md` | `888fa925485a64642443b7555d8a989aea955d0a7997e23a09edef7db93bbd37` | 31309 |
| `MODEL_AND_DATA_SPEC.md` | `c4d77b5036afbe531387886ee460d35a47ba6d824bf5a13077f20d7c9906b771` | 64024 |
| `ALGORITHM_PORTFOLIO_AND_EVALUATION.md` | `c0dbea56b78a51c5f6a075d7e0ace6e0d84a4fe97a1366cd699624e5783f49aa` | 51138 |
| `MODEL_IMPLEMENTATION_RECIPES.md` | `f016aa31c039dd95152f36a6df56d2758c2769b146b73bd8b8a43fa18e02021c` | 20837 |
| `RECENCY_AND_REBOUND.md` | `b35e9684ecb6d468b2570d6e429301cba567f8590e230bb3a46d42ffd4d93f37` | 18248 |
| `BASE_RATES_REGISTER.md` | `9b79fd409e43d13d40bda1a3afb8dce6b2135dba621399a4da5a1f2982ad23d3` | 27071 |
| `GAME_LOG_STATUS_CURRENT.md` | `1e28c9e473399b9abc0b0787001a61bfcb606ec2649110fc5e7b80a848310186` | 135708 |
| `PREDICTION_LOG_COMBINED_5.md` | `ed5d2ba2421f8e597880693951eed3c7854b97ddfa1552d20c3983b1838179bf` | 899036 |
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
| `CURRENT_RULES.md` | `3fcddc9e0b3e368301a588575f06abcd4277cbde49b48b41b302e9b7548cebac` | 29631 |
| `CHANGELOG.md` | `cefd50f25f0084cbe53381675e9a9acd57077f71ef7e8a1919e33bcecc248329` | 29831 |
| `CONTRIBUTING.md` | `3f6613706d74371319720ec83bbc18fefa39dc98b6169e5bf4af1b0915aeb427` | 3801 |
| `SKILL_BASELINE_LEDGER.md` | `0d914665196efe3983da38970a98cfc97444d6d66360cc65ed425569010bd92d` | 9842 |
| `LICENSE` | `1efb20731adc03fb046120ceeceb7f4e0ca0d73b2eb2d5fcf2093350863161b8` | 1211 |
| `.gitignore` | `78d5d3fa98cb9d31837e524eb218713d10820a0e6ddf73b22d5595697fd187b9` | 843 |
| `.gitattributes` | `8e7b10c0994c597d8d35111d065d6986c543f5a514d308ec74217885443e9dcc` | 513 |
| `.github/workflows/checks.yml` | `fedefe694e26c153292cddfc78b86837ee63766dc8fbce3a3e775cc891e1a0dc` | 1506 |
| `tools/manifest_lib.py` | `646b30705db92e03c0c83e135274aff6317c41a688d80dd6f4e6099d7bd395e6` | 2133 |
| `tools/make_manifest.py` | `e8e61475a06fdbdf76543d4da209584d2552326c86c62cda2a6ac19645305a43` | 5159 |
| `tools/verify_manifest.py` | `51fc35aedd098185c6a4e17b63d6bbe5a6c1ca74757be50b6b06dc3f561fa2b4` | 3551 |
| `tools/repo_hygiene.py` | `fed26719c9b4e354f2a545a469f762527b6a92893b6ef124528f1f58693532cb` | 3846 |
| `tools/skill_baseline.py` | `ae5cb0be0328cabee235deff66db3dadf1f19da6884ad66c71ae0693f13146e7` | 5722 |
| `tools/test_repo_tools.py` | `48cd7ceb321d6948bf4f9d034492c4765f2cc23fa77e99e3705b8519c9d932a5` | 5574 |
| `tools/test_skill_baseline.py` | `17e395c1703dba96eec1f80949a064ddddd5e836a676e245d1329b25763f5413` | 2688 |
| `research/base_rates_2026-09-25/build_skill_baseline_seed.py` | `babaa48ef17feb22916bab7feabf04ff2a4b3d800393fcafaa5246d578d61ede` | 9714 |
| `research/base_rates_2026-09-25/.gitignore` | `03edf42376bb781d8497699bee737ae42badca878e1d27cf191d04e87e8d872c` | 161 |
| `tools/card_math.py` | `a14202a134b101a62950a96e52751a8b5d8236dfb513b8a4a37c091106082677` | 11330 |
| `tools/calibration_report.py` | `15964628f4a89325acff60d3bd07a1ca9c2ded0de0e76574cf1c6a88622cf042` | 8502 |
| `tools/test_card_math.py` | `f3c65d208b5bcbb4850b0ebfc531d192038cf5ee3bbc670fbf33b4b8cd0144c7` | 5601 |
| `research/settled_rows_2026-09-25/README.md` | `d42edc381e689def7bed840c5f2bf7ac4607a7db76be01fe74e0088f65de5af8` | 7881 |
| `research/settled_rows_2026-09-25/extract_settled_rows.py` | `0916d97d561b8517d8a7cf99884bfac0c1006a20744e924b1512ae965d6e9f5b` | 17941 |
| `research/settled_rows_2026-09-25/analyze_settled.py` | `4eff0b3eb4b3d497a361dc450eca97cb86979ca543cfba33f09c1eabb1a82b32` | 8463 |
| `research/settled_rows_2026-09-25/analyze_supplement.py` | `148653ad9e111b5730cb1ce5267a7b3f07c1e4036dd12c802b4907f603b7491b` | 4868 |
| `research/settled_rows_2026-09-25/analysis_results.json` | `b1441e3e1c1f471286271e90738e2dcf3c8cd5036b4fc2773c304877da0b229f` | 17392 |
| `research/settled_rows_2026-09-25/supplement_results.json` | `78b9ed833e03bf85a43851f00434456a463a223cc16987eacc3be3e61dab0beb` | 5262 |
