# Input and authority receipt

Authority mode: LOCAL_WORKING_TREE; main / `adb8560a597e5ff1a5ad21bfc76b3148bd58c719`; read time 2026-10-13T15:36:21+11:00, Australia/Sydney UTC+11. After fetch, HEAD...origin/main = 0 / 0. No branch change or pull. User invoked the complete prompt 4, authorizing scoped commit and main push. Instructions inside settlement documents describe the prior settlement run and do not override this import request.

Current controls: MDS-2026.10.12-v11.0, CR-2026.10.12-R2, SCV-2026.10.12-v7, SEL-2026.10.12-v3. Source retains mini-log-6 / mini-settlement-5, frozen historical format.

Control differences applied locally: SOURCES.md adds the NBA G League source/history section; research/prompts/1_GAME_CARD.md deletes the issue-window sentence. Neither difference changes imported cores or settlement grades. Exact differences retained in CONTROL_DIFFS.txt. Other dirty work is preserved.

Controls read: README.md; CURRENT_STATE.md; METHOD.md; CURRENT_RULES.md §§0–11; SELECTION_RULES.md; CARD_AND_LOG_TEMPLATES.md (compatibility, card, addendum, settlement, C/S audits and canonical wrapper); research/prompts/README.md; local and supplied prompt 4; SCORING_AND_VALIDATION.md (actual scoring path, not retired SCORING.md); VERIFICATION_PROTOCOL.md §§1–3 and 6. Status current administrative section and historical boundary, Part 7 dated opening and complete raw tail, relevant retained original/canonical P-577–P-579 fields, previous import verification and current scoreboard/retrospective inventory inspected. Original and settled source bytes fully inventoried and compared; full marker, source-core, rank/p/baseline and revision readback used. Source card audits retain their original gaps. No live sporting re-research or regrading.

research/current_combined_log.json and the executable runtime are retired/absent. The verified active destination comes from current CURRENT_STATE/status and actual canonical cards, not the old Part 7 opening snapshot or memory.

| Input | Raw bytes | SHA-256 | CRLF | bare LF |
| --- | --- | --- | --- | --- |
| ORIGINAL_MINI.md | 172050 | 364dc74e30520df5711743ecbc9efd5122a9024627f1bba4f4bb7cb9c49adba0 | 0 | 1014 |
| PREDICTION_MINI_SETTLED.md | 228439 | 4c8dd95baf4564ac2c8d0492ef2acd8053acc0a9ea6ecc492329f0f5b469d3a4 | 0 | 1349 |
| SETTLEMENT_MANIFEST.md | 7523 | c90c25e6bfcb2e970dc0e592f1de7473ed241fa53c6ad18a04b9695022dd4a38 | 0 | 80 |
| UNRESOLVED_CARRYOVER.md | 3595 | e695ae82be8d5ceb116cacc10ee6d73a4791a83cebbf792fb2845999a64d6eba | 0 | 14 |
| SETTLEMENT_REPORT.md | 9117 | 63383636b831ce7fb50339b12ff9196bc674499d0556e03a98387a4c34fa95f4 | 0 | 54 |

Missing source companions: LOCAL_ID_MAPPING.md, CARRIED_ORIGINAL_CARD_REFERENCES_P577_P579.md, PRIMARY_PROPER_SCORES.csv, READBACK_VERIFICATION.md. These were not recreated or misrepresented as supplied originals. Independent import mapping and score calculations are generated from the actual frozen source and retained canonical originals. Exact earlier original cores were recovered from the previous committed import master, and normalized CRLF→LF equality against canonical cores was established. This resolves parent identity/ranks without reconstructing forecast text. Absence of the separately claimed source companions remains a package-completeness limitation; all supplied source units have independently verifiable disposition.

| Carryover | Canonical core bytes | Canonical raw SHA | Retained source core bytes | Retained raw SHA | Comparison |
| --- | --- | --- | --- | --- | --- |
| P-577 | 18223 | cc853625c7b959a3004efdaca1b3a2cc7709fcf1b2abb8f60c0ef5a5550e5d69 | 18107 | 939de3f38b99dd9b468d940ff6365858d80aed6ca2a8ff0a7e237e8d31730bb1 | PASS after declared CRLF→LF only |
| P-578 | 20123 | bf417468fcb9b42c05fbd4b4704e51c5197ccd735179b5c5fccfaf720bca7ed5 | 19997 | 78d0fa824cb6ed61c2a2c40cc8bf2b8432c7287fe0e86815ad905f91120187c2 | PASS after declared CRLF→LF only |
| P-579 | 18826 | 5b6baae7bb1e315b711d4183bd43328ab20e5a640c3d19bfbb414ed2728f4bb9 | 18717 | 57359dcae6ffed294a172a4b2ce8aed2094d7f0daa05d16bf9040a7bf22207b7 | PASS after declared CRLF→LF only |

Byte identities: raw source snapshot and destination prefix are distinct from imported literal cores and committed representation. Destination initially 1255058 bytes, SHA-256 `2f46c0d12b3c1f12d65eb372e50f8ed4b116b94908970e22127a8a4d36036906`, CRLF 6534, bare LF 2184. Source settled 228439 bytes, SHA-256 `4c8dd95baf4564ac2c8d0492ef2acd8053acc0a9ea6ecc492329f0f5b469d3a4`, CRLF 0 / bare LF 1349. Existing destination prefix must remain exact; source slices will be appended in LF without conversion.

Git core.autocrlf=true, but local .git/info/attributes marks active log, status and verification folder -text: their committed blobs are checked raw. CURRENT_STATE and SCOREBOARD are text and committed LF is checked separately. Downloads are outside git, so git ls-files --eol cannot describe them; copied input paths receive an actual eol check before commit.
