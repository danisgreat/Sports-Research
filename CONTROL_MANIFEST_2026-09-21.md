# Control manifest — 2026-09-21

Method: **MDS-2026.09.19-v4.3**  
Control revision: **CR-2026.09.21-1**  
Purpose: immutable filename/hash receipt for the active authority and executable-control set after the 2026-09-21 cricket toss/pitch source-integrity implementation. This revision preserves the CR-4 three-source/timezone/terminal-state gates and adds separate cricket toss/strip retrieval, source-lineage fingerprinting, explicit venue-history missingness, stale-official handling and executable cricket preflight checks. It makes **no predictive-improvement claim**.

The manifest itself is intentionally excluded from the hash table to avoid self-reference. Historical issued cards retain the control revision/hash set frozen at their issue time. Where a current file already differed from the prior CR-4 receipt before this implementation, that state is disclosed rather than falsely labelled unchanged.

## SHA-256 file receipt

| File | SHA-256 | Bytes | CR-2026.09.21-1 disposition |
|---|---|---:|---|
| `README.md` | `c9854f1ccd6ef82b627bb57ce41b1f1da268029a7299cbe135fb8efe4785ea04` | 14504 | IMPLEMENTATION CHANGE / NEW |
| `METHOD.md` | `ff2f279c8426989bde2fe9496528356e30cc6b81bb279c2b935ee68f048d286e` | 20665 | IMPLEMENTATION CHANGE / NEW |
| `CONTROLS.md` | `a6d39631228ef5874a682b344eaa7b5b2d19fdf622dc92b0b58617ded7b8c9f6` | 23565 | IMPLEMENTATION CHANGE / NEW |
| `RULES_GENERAL.md` | `8008f83d14414613865e2d2ae02506ed449d92bf8c0fab84ef3d11c8ffb1f4e4` | 214878 | UNCHANGED VS CR-4 RECEIPT |
| `SOURCES.md` | `82ef1ad1c087814f2edec862cbd60adbc65bfa75d88c815fd3646cbbb606477f` | 63759 | IMPLEMENTATION CHANGE / NEW |
| `DATA_SOURCE_REGISTER.md` | `39c17c8887051196a42bf61a992cfd1159de5de8f58cb71ad79660157218d8d2` | 148176 | IMPLEMENTATION CHANGE / NEW |
| `UPCOMING_GAME_RESEARCH_GUIDE.md` | `cec311da437ccf034100acf84736691193718ff62b111f6a73b776bc92f1007c` | 61714 | IMPLEMENTATION CHANGE / NEW |
| `SCORING_AND_VALIDATION.md` | `2d683aa2fbfe3f5277d04e2251734384a7f9d6c221361f2741bf393f1508637f` | 11901 | UNCHANGED VS CR-4 RECEIPT |
| `NUMERICAL_TRAINING_SPEC.md` | `51692aa6c0aa7bab1412c76970aef0eedc911439c2db44f526f8564e186a5ff6` | 30771 | UNCHANGED VS CR-4 RECEIPT |
| `MODEL_AND_DATA_SPEC.md` | `18d95409efb2bb83f8d28583cbbccc8a329da8e36a993908a0afd2f0a23d9478` | 63102 | UNCHANGED VS CR-4 RECEIPT |
| `ALGORITHM_PORTFOLIO_AND_EVALUATION.md` | `766e866bf7572199358f4503b0f683f0d81de869691f25539e25dc664fdec9d3` | 50223 | UNCHANGED VS CR-4 RECEIPT |
| `NUMERICAL_PROGRAM.md` | `47cc96bd5fc5e1eeade938e8b6d1b62ea12383412f83782e8f049efda1123ff8` | 9511 | UNCHANGED VS CR-4 RECEIPT |
| `NUMERICAL_MODEL_REGISTER.md` | `30cd781a170f0bb58f90200a73bb724983ef7492a66055521017ce79994e2647` | 21974 | UNCHANGED VS CR-4 RECEIPT |
| `MODEL_IMPLEMENTATION_RECIPES.md` | `84dd9aec6040d045d1214e526f80ef1f7c51b5b64871d45c5441ce588fb43180` | 20547 | UNCHANGED VS CR-4 RECEIPT |
| `PERFORMANCE_ELIGIBILITY_POLICY.md` | `b3d1a4d4b840a36401f6bd928185addb5a6c668b84a6f04975015b71c1068546` | 18083 | UNCHANGED VS CR-4 RECEIPT |
| `H0_DATASET_CARD.md` | `8238143f413c74d3ae2016a0608cf3b384ff8d9b5052be4d90dc578277cef677` | 19003 | UNCHANGED VS CR-4 RECEIPT |
| `AGENT_ROLE_AND_TASK.md` | `59dd668b5145a9fe585154a90878cb62de55a241ddb2c8ce2de0c6653d1dd5b5` | 21735 | UNCHANGED VS CR-4 RECEIPT |
| `EXTERNAL_LOGGING_WORKFLOW.md` | `2d9aefd25fc447fc7f65df32e28aa636c785cf850b494c4455102b3fd93bc776` | 51473 | UNCHANGED VS CR-4 RECEIPT |
| `RULES_BASEBALL.md` | `1e0b5a0e9636469f7b75fcc21d19f9fe3c557c691724e67bba821b145889a411` | 107197 | UNCHANGED VS CR-4 RECEIPT |
| `RULES_CRICKET.md` | `bf4b5cd40222327a7f329dee61715367044ca96393b61bac13651d99d202883c` | 94921 | IMPLEMENTATION CHANGE / NEW |
| `RULES_SOCCER.md` | `239f942492cd42bd789e80b6d699924153133d4f5fc084563932eef6df2b85fe` | 93989 | UNCHANGED VS CR-4 RECEIPT |
| `RULES_BASKETBALL.md` | `f5ad8787a08fe6b1533c0f273058f26ab3ff3f731bc5307ebe40423993c14421` | 78798 | UNCHANGED VS CR-4 RECEIPT |
| `RULES_AFL.md` | `34198e08bacaa062ab7062e14332b068be8b6bcd9656c0c781d96f6bfd9ef3dc` | 54584 | UNCHANGED VS CR-4 RECEIPT |
| `RULES_NRL_RUGBY.md` | `0c080a087c11ab756daf9a65ad9e562c8ed52fe775b9d8df23d656d7ac4e7877` | 53392 | UNCHANGED VS CR-4 RECEIPT |
| `RULES_RUGBY_UNION.md` | `bba94264bce462a347425f6b5f06eb871178022520aed1c1c6fcb78ea02866cc` | 48030 | UNCHANGED VS CR-4 RECEIPT |
| `RULES_AMERICAN_FOOTBALL.md` | `05b52854f0f322c2cd9c144d4daf22fbf8ffcf9b3bd2144de4d407c7c25ef7e6` | 58454 | UNCHANGED VS CR-4 RECEIPT |
| `RULES_ICE_HOCKEY.md` | `40042e356572345e096b9e3a50cfd7920cc425e7d211502308c0a2825cc1e3c3` | 48582 | UNCHANGED VS CR-4 RECEIPT |
| `RULES_TENNIS.md` | `04ead67a123955f383f4af4efd1d41f213f26848896ab9cfb2726179024196d1` | 58313 | UNCHANGED VS CR-4 RECEIPT |
| `LEAGUE_RULES_SOCCER.md` | `729e7bc67cab6c51130999dc68011bc8bfa9afd71983d8a887f95e0cbc721645` | 43499 | UNCHANGED VS CR-4 RECEIPT |
| `LEAGUE_RULES_CRICKET.md` | `97fccf5a7f1cdafeec87026405c9a15eb7f30e1ead9394089ce5bf994c4d0c37` | 26046 | UNCHANGED VS CR-4 RECEIPT |
| `AUDIT_IMPLEMENTATION_2026-09-19.md` | `f2bb87398d68cb7d092b2f2a3f69f63d984435217f81ec4971a2ebd8d99af162` | 18010 | CURRENT PRE-IMPLEMENTATION BYTES; DIFFERS FROM CR-4 RECEIPT |
| `audit_card_controls.py` | `a62f2494b5967e94b87da8f445977613aacb751cf8f6f1ec4b9de78fc5454e0f` | 17043 | UNCHANGED VS CR-4 RECEIPT |
| `prediction_preflight.py` | `7ddc66afcad77de7de5dde0650e8986e24dc112903932e699629816451be0596` | 24687 | IMPLEMENTATION CHANGE / NEW |
| `test_prediction_preflight.py` | `68a4c0f335f973409639e2dc174333cf1e1e507f7fd8bb062165ef5ba2bb59c6` | 7752 | IMPLEMENTATION CHANGE / NEW |
| `FORECAST_PREFLIGHT_MANIFEST.md` | `e67b4c731cbaf61ebc9183a4884f03767385df3efcf5f8a18527d3039db27155` | 5878 | IMPLEMENTATION CHANGE / NEW |
| `PREDICTION_MINI_RUNNING_LOG_P452_ONWARD.md` | `e492c8c3d2bb2d3d302b3482fd6b2512d8eda62fcaf5e3ba9c7e53ec7e86ce0e` | 572426 | CURRENT PRE-IMPLEMENTATION BYTES; DIFFERS FROM CR-4 RECEIPT |
| `LEARNING_REGISTER.md` | `d81bc504b28aa9e32fa8af6318ac6a6fa96d5aaa6c18d59943648161c0635a0c` | 252811 | IMPLEMENTATION CHANGE / NEW |
| `AUDIT_AND_CRICKET_SOURCE_UPDATE_2026-09-21.md` | `c627cbe56488340f201ac6dad94e0c326f48abdb7f80e3573be53315ba94351d` | 25208 | IMPLEMENTATION CHANGE / NEW |
| `AUDIT_IMPLEMENTATION_2026-09-21.md` | `865fe1562dd9a23258d0ffab14082ee768353818695c11e31d11fbac14a34a9b` | 10824 | IMPLEMENTATION CHANGE / NEW |

## Verification rules

- Every new forecast records **MDS-2026.09.19-v4.3 / CR-2026.09.21-1** and the applicable control/file hashes used at issue.
- Historical cards retain their original versions. Do not retrofit this manifest to earlier issued views.
- Any later material change to an authority/control file requires a new control revision and new receipt; never replace a hash while retaining `CR-2026.09.21-1`.
- `prediction_preflight.py` PASS is required before normal issuance but establishes governance/control conformance only, not calibration or predictive skill.
- CR-4 remains active inside this revision: at least three independent reliable upstream event lineages, venue-local/timezone-aware Melbourne conversion, pregame state verification, and three independent terminal-state lineages at settlement.
- Cricket additionally requires the TOSS/STRIP/MATCH-CONDITIONS protocol in `RULES_CRICKET.md` §2 and `DATA_SOURCE_REGISTER.md` §6A, including lineage fingerprinting and no automated metadata masquerading as an observed strip.
- Venue-history absence is represented explicitly as `INSUFFICIENT_VENUE_HISTORY`; it is never filled with fabricated same-venue observations.
- Regression suite after this implementation: **20/20 tests PASS** on 2026-09-21; Python compilation PASS.
- **H0 remains NOT BUILT / NOT QUALITY-APPROVED and no numerical model is fitted, calibrated, held-out validated or prospectively promoted by this source-control patch.**

## Audit provenance

- Findings/source research: `AUDIT_AND_CRICKET_SOURCE_UPDATE_2026-09-21.md`.
- Implementation/disposition ledger: `AUDIT_IMPLEMENTATION_2026-09-21.md`.
- Previous CR-4 ledger and receipt remain historical evidence; they are not silently rewritten.
