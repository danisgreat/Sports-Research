# Audit change log — 2026-09-07

**Pass type:** settlement, retrospective and ledger restructuring. **No forecast was issued.**
**Method:** `MDS-2026.09.06-v4.0` (unchanged).
**Constraints unchanged:** `SPORTS_ONLY / MARKET_BLIND`; numerical program at Stage S0; no source `APPROVED FOR FEATURE`; no H0 ingestion authorised; no calibrated/edge/ROI/model-validation claim.
**Scope:** local repository only. Google Drive was not modified (the Drive folder is a stale manual mirror — the user re-syncs it).

---

## 1. Three-log restructuring — per user directive

| Log | Role | ID range | Status after this pass |
|---|---|---|---|
| `PREDICTION_LOG_COMBINED.md` | Historical archive | `P-001`–`P-271` | CLOSED (2026-09-04) — forward pointer appended, not rewritten |
| `PREDICTION_LOG_COMBINED_2.md` | Historical archive + unsettled-log appendix | `P-272`–`P-332` | **CLOSED 2026-09-07** — Status/snapshot updated; `## 2026-09-07(a)` + `## 2026-09-07(b)` + `# Appendix — unsettled and incomplete logs` appended |
| **`PREDICTION_LOG_COMBINED_3.md`** (new) | **Active canonical log** | `P-333` onward | **ACTIVE — opened empty** — next ID `P-333` |

Per the user's directive: `P-318`–`P-332` were **settled and appended to Part 2** (`## 2026-09-07(b)`); Part 2 was then closed at `P-332`; Part 3 opened empty and continues from `P-333`. All inherited unsettled / incomplete follow-ups were given a maximum fresh settlement attempt and quarantined in Part 2's lettered **"Appendix — unsettled and incomplete logs"**. **Part 3 does not carry, track or re-open any of the appendix items.**

## 2. `P-318`–`P-332` settled and folded into Part 2 §"2026-09-07(b)"

Source: `PREDICTION_MINI_RUNNING_LOG_P332_UPDATED.md` (issuance) → `PREDICTION_MINI_RUNNING_LOG_P332_FULLY_UPDATED_2026-09-07.md` (settlement-updated) → stored as `archive/mini_logs/PREDICTION_MINI_RUNNING_LOG_P332.md`.

| Fingerprint | Value |
|---|---|
| Settlement-updated bytes / SHA-256 | 264,499 / `430433B14BF2C6525F05701100A3EAC4C55827C89910CB7E44E9649019138233` |
| Issuance (pre-append) bytes / SHA-256 | 231,106 / `1B860711FDEE6994B97C473D63E43DABB6216841AF6F7337426544283B3ADEBC` |
| Companion settlement mini log bytes / SHA-256 (after 2026-09-07 overlay append) | 93,403 / `B5BBC721E76CBDA672179A401CBA2AB3CC90CCE84AC64E0703F76F52420E67E5` |
| Canonical mapping | `P-318`–`P-332` → `P-318`–`P-332`; no collision; no `TMP-SETTLED-*` needed |

Per the current post-`P-294` procedure, Part 2 folds in the **settlement tables, full contract-row grades, three-question retrospectives and the Brier scorecard** — not the raw card text, which stays in `archive/mini_logs/PREDICTION_MINI_RUNNING_LOG_P332.md`.

### Settlement outcomes (descriptive only)

| Metric | Value |
|---|---|
| Issued sporting cards | 12 (`P-318`, `P-319`, `P-320`, `P-321`, `P-322`, `P-323`, `P-325`, `P-327`, `P-328`, `P-329`, `P-331`, `P-332`) |
| Administrative no-forecast closures | 3 (`P-324` Valencia–Barcelona, `P-326` Western Carolina–Campbell, `P-330` Puerto Rico–Belgium) — all live-state-gate fail-closed, non-scorable |
| Ranked rows settled | 57 = 28 W / 29 L |
| Rank #1 | 9 W / 3 L |
| Potential-winner calls | 7 W / 5 L |

Rank #1 losses: `P-318` (`1H Over 0.5` — 0–0), `P-323` (`1H Over 0.5` p0.74 — second-half-only game), `P-332` (`FT Under 2.5` p0.60 — 5–2 with a hat-trick). All three "smallest change" notes concern phase-separation and widening tails when the participant/lineup state is conflicted.

### First `UNVALIDATED_SUBJECTIVE` Brier scorecard (`METHOD.md` §5)

| Population | Cards | Scored rows | W / L | Mean Brier | 0.5 baseline |
|---|---|---:|---:|---:|---:|
| EPL — `PRIMARY_SCORED` | `P-323`, `P-328` | 10 | 5 / 5 | 0.2666 | 0.2500 |
| MLB — `PRIMARY_SCORED` | `P-331` | 4 | 2 / 2 | 0.1893 | 0.2500 |
| NRL / AFL — `PRIMARY_SCORED` | — | 0 | — | — | — |
| Combined `PRIMARY_SCORED` (this cohort) | 3 | 14 | 7 / 7 | 0.2445 | 0.2500 |
| `EXPLORATORY` scored | `P-325`, `P-327`, `P-329`, `P-332` | 19 | 10 / 9 | 0.1987 | 0.2500 |
| **All scored rows (mixed)** | 7 | **33** | **17 / 16** | **0.2181** | **0.2500** |

**Sample far too small for any calibration, superiority or discrimination claim.** `PRIMARY_SCORED` card count is 3; the 25-card cadence review (`METHOD.md` §7.2) is where the scorecard and the qualitative pattern review are read together. The scorecard is carried forward as the running total in Part 3's snapshot; every `P-333`+ card adds to it. `P-318`–`P-322` predated consistent probability issuance in the mini log and are graded W/L only.

## 3. `P-294`–`P-317` deeper `MDS-2026.09.06-v4.0` retrospective

Applied the current three-question schema (`METHOD.md` §7.2 — driver / knowability / smallest routine change) to `P-294`–`P-317` and the stale carryovers `P-288`/`P-290`–`P-293`/`P-151`/`P-273`. **No settled contract outcome, issued rank, evidence label or reasoning changed.** Full text: `PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md` and `archive/mini_logs/PREDICTION_MINI_RUNNING_LOG_P317.md` §"2026-09-07 APPEND-ONLY SETTLEMENT / RETROSPECTIVE APPENDIX". Folded into Part 2 §"2026-09-07(a)".

## 4. Appendix — unsettled and incomplete logs (Part 2, lettered A–N)

Per the user's directive, every unsettled or incomplete log inherited from Parts 1 and 2 is collected at the bottom of Part 2, lettered A–N with the canonical `P-###` ID preserved, each keeping its existing learnings and recording a **maximum fresh settlement attempt** (2026-09-07). Part 3 does not carry or re-open these.

| Letter | ID | Outcome after 2026-09-07 maximum attempt |
|---|---|---|
| A | `P-126` | IDENTITY_STATE_CONFLICT — unresolved; no authenticated final for the SFA "A" Division fixture |
| B | `P-148-C02` | PROVISIONAL LOSS — Toluca 1–0 confirmed; no field-owning corner count |
| C | `P-149-C02` | PROVISIONAL WIN — Ventura 3–2 confirmed; no complete corner count |
| D | `P-166` | RESEARCH SETTLED (Canberra 5–4 incl. OT; ranks graded); `OPERATOR_ACTION = UNKNOWN_DEFINITION` |
| E | `P-176-C05` | PROVISIONAL WIN — Amiens 3–0; best evidence 8 total corners (Football365 timeline) → Under |
| F | `P-178-C05` | UNRESOLVED — Cannes 2–0; no trusted complete corner total |
| G | `P-179-C05` | PROVISIONAL WIN — 1–1; specialist 9 total corners → Under; provider confirmation missing |
| H | `P-200` | RESEARCH SETTLED (Herning 4–3 incl. OT; ranks graded); `OPERATOR_ACTION = UNKNOWN_DEFINITION` |
| I | `P-217-C01/C02` | RESEARCH SETTLED under `G36.1` on the revised 16-over innings (C01 Over 174.5 W, C02 L); `OPERATOR_ACTION = UNKNOWN_DEFINITION` |
| J | `P-233` | PROVISIONAL WIN — Beijing Guoan 3–1 confirmed; inherited 13 corners → Over; not newly official |
| K | `P-234-C03` | PROVISIONAL WIN — Dalian 1–0 (disrupted match, GK dismissal); inherited 10 → Over; not newly official |
| L | `P-235` | PROVISIONAL WIN — Shanghai Port 3–0 confirmed; inherited 14 → Over; not newly official |
| M | `P-274` | RESEARCH SETTLED (Pittsburgh 5–2; Bachar corrected starter; ranks graded); `OPERATOR_ACTION = UNKNOWN_DEFINITION` |
| N | `P-307` | INCOMPLETE / NO FORECAST ISSUED — administrative, non-scorable |

Also noted for completeness (already closed, not "unsettled"): `P-003` (terminal `UNSETTLEABLE` corners row), `P-316` (`CANONICAL_ALIAS_OF_P-317`).

**Maximum-attempt routes tried for the eight open corner rows (B, C, E, F, G, J, K, L):** ESPN structured lane by direct `curl` — `chn.fa`/`chn.fa_cup`/`chn.china_fa_cup` → HTTP 400 (no Chinese-cup feed); `fra.3`/`fra.national` → HTTP 400 (no French third-tier feed); ESPN has no MLS Next Pro / SFA "A" Division / Liga MX Femenil feed. FotMob API (`/api/matches`, `/api/matchDetails`) → HTTP 404 (protected/changed). `api.sofascore.com` → 403. WebFetch of Flashscore, FotMob, Tribuna, worldfootball.net, matchendirect.fr → JS-rendered stat panels absent from fetched content, or HTTP 403. WebSearch → confirmed **scores and goal sequences** for every match, **no corner totals**. Conclusion: no reachable field-owning structured corner provider exists for these competitions and none is retrievable through any available tool; under `G10.2`/`L-081` a secondary-aggregator count does not settle a derivative row to this framework's standard. This is the definitive maximum attempt.

## 5. Files moved / created / changed

**Moved** into `prediction logs/` (byte-preserved external-session source artifacts):
- `PREDICTION_MINI_RUNNING_LOG_P317.md` — from repo root; content = settlement-updated 2026-09-07 version (338,176 bytes, SHA-256 `72879B9AB5FBF557CED1B7D6FE128E6EE634A3CF3D85AF5D60E88F2A04C5BE98`). Superset of the prior 298,131-byte root copy (pure append).
- `PREDICTION_MINI_RUNNING_LOG_P332.md` — from repo root (`PREDICTION_MINI_RUNNING_LOG_P332_UPDATED.md`); content = settlement-updated 2026-09-07 version (264,499 bytes).

**Retained at repo root** (heavily cross-referenced settlement reference, ~100 inbound links across ~24 files; matches the `PREDICTION_LOG_COMBINED_P267_SETTLED_2026-09-03.md` "retained at repo root, not renamed, to preserve its own internal cross-references" precedent):
- `PREDICTION_MINI_LOG_SETTLEMENT_2026-09-06.md` — the 2026-09-07 `P-318`–`P-332` overlay was appended (60,316 → 93,403 bytes; pure append). Its one outbound link to the moved `P-317` running log was repathed to `prediction%20logs/`; a file-state note was added at the top.

**Created:**
- `PREDICTION_LOG_COMBINED_3.md` — new active canonical log, opened empty at `P-333`.
- `AUDIT_CHANGELOG_2026-09-07.md` — this file.

**Changed:**
- `PREDICTION_LOG_COMBINED_2.md` — Status → CLOSED at `P-332`; snapshot "As of" / "Next canonical ID" (`P-333`) / queue rows updated; `## 2026-09-07(a)` (restructuring + `P-294`–`P-317` retrospective), `## 2026-09-07(b)` (`P-318`–`P-332` settlement + Brier scorecard) and `# Appendix — unsettled and incomplete logs` (lettered A–N) appended. No settled card, rank or contract outcome altered.
- `PREDICTION_LOG_COMBINED.md` — one dated forward-pointer paragraph appended to its "Two-log restructuring — 2026-09-04" section (not a rewrite).
- `README.md` — active-log pointer → Part 3 (`P-333`, opened empty); "Latest" section; primary-documents table; historical/component lists; performance-eligibility paragraph.
- `METHOD.md` §10 — "currently `PREDICTION_LOG_COMBINED_3.md`, `P-333` onward"; Part 2 closed at `P-332`.
- `CONTROLS.md` — 2026-09-07 note.
- `LEARNING_REGISTER.md` — 2026-09-07 disposition section.

**Not changed:** no `RULES_<SPORT>.md`, no `RULES_GENERAL.md`, no `SOURCES.md`, no `NUMERICAL_PROGRAM.md` — no new gate, weight, source approval or numerical step. The dated `GAME_LOG_LEDGER_2026-09-06.md` / `GAME_LOG_STATUS_INDEX_2026-09-05.md` snapshots are point-in-time and were left as-is (README already lists them as historical, not mandatory reads); the current `P-318`+ / appendix state is carried by Part 2's closing sections and Part 3's snapshot.

## 6. What this pass did not do

- **No settled card's contract outcome (WIN/LOSS/PUSH) was changed.**
- **No probability was minted retroactively** — every card before `P-318` keeps `NOT_GENERATED / NOT PUBLISHED — VALIDATION PENDING`; `P-318`–`P-322` are graded W/L only.
- **No new predictive rule, gate, ordinal bar, fitted weight or coefficient was promoted** (`L-087` firewall). Candidate watch items were recorded, not adopted.
- **No source was approved for a numerical feature.**
- **Google Drive was not touched.**
- The eight inherited corner rows were **not** force-settled from secondary aggregators — that would not meet the framework's own field-ownership standard, and "be honest, accurate" was the instruction. They are recorded in the appendix with their best-available disposition, explicitly labelled.
