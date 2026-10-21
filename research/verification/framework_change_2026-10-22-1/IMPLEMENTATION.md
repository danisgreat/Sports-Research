# Implementation — framework change 2026-10-22-1 (v23.0)

**MDS-2026.10.22-v23.0 / CR-2026.10.22-R1 / P-2026.10.22-v23.0 · ENV-v2 · MLSCOPE-v2 · MINI-v2 · RELEASE-SCOPE-v1 · PREGAME-v1.** Base `main` 29e25a798 (b0ee854f2 after the 21 October review commit). Mode `LOCAL_WORKING_TREE`. Clock read 2026-10-22T00:13+11:00 at start. [Proposal](CHANGE_PROPOSAL.md) · [Simulation review](SIMULATION_REVIEW.md).

## What changed

### Code (`ml/`)

| File | Change |
|---|---|
| `ml/code_identity.py` (new) | Release code scope: static `ast` import closure of `ml.cycle` + `ml.workflow`, digest with LF normalisation, checkout and archive readers |
| `ml/cycle.py` | `code_hash()` uses the closure digest |
| `ml/chat.py` | `archive_code_digest()` uses the same rule, so `pack` stays consistent with releases |
| `ml/pregame.py` (new) | `pregame run` (card-first guard; `card_p` must be printed in the card; NOT_RUN_NO_RELEASE / NOT_RUN_STALE_RELEASE / NOT_RUN_INPUT_REFUSED receipts; runs and accepts the cycle attempt; freezes the card's p_card as `ANALYST_PRIMARY_V1:CARD` beside the model and baseline on identical contract keys), `pregame status` (8-week / 50-game progress), `pregame compare-card` (prospective paired card-versus-model evaluation) |
| `ml/run.py` | Registers `python -m ml pregame` |
| `ml/execution.py` | `verify-log` accepts a backtick-wrapped analysis status (needed for the carried OKC card); invalid statuses still refused |
| `ml/tests/test_pregame.py` (new) | Card-first refusal; card_p must be the printed value, including a near-miss number; executed run freezes 3 model + 1 card rows with matching contract key; no release; stale release; refused input; status; the review/decision rule at its edges; closure contents; LF/CRLF invariance; edits outside the closure keep the digest; static closure ⊇ modules actually loaded; relative and function-level imports |
| `ml/tests/test_chat_execution.py` | Archive digest compared with `cycle.code_hash()`; edits outside the closure keep it |
| `ml/tests/test_execution.py` | Backtick status accepted; backtick-wrapped invalid status refused |
| `ml/tests/test_prompt_consistency.py` | ENV-v1 / MLSCOPE-v1 checks replaced: prompt 1 prices the card before the model step; prompts 2, 5 and the sport files give no model commands; prompts 1–3 run in the working tree; canonical assignment sits in the settlement phase |

### Releases

`research/cycle_releases/NHL-CYCLE-4.csv` and `MLB-CYCLE-4.csv` were frozen with `python -m ml cycle release` against the final code (code digest `0563ffd6…b829`). Every parameter equals v3 (NHL ridge 24, MLB ridge 32; fast 90 / slow 365 days; half-life 20; floor 0.05; eta cap 0.5; minimum 8 weeks / 50 events / δ 0.01). `CURRENT_RELEASES.csv` points to v4. The v3 files stay as history. Before this change the v3 releases were already stale: frozen code `0303f967…`, current code `adb00616…`.

### Controls

- **Replaced by script** (`apply_v23.py`, run outside the repository; every changed file archived from `HEAD` first), over 61 active Markdown files:
  - MINI-v1 → MINI-v2 paragraph ×43;
  - MLSCOPE-v1 → MLSCOPE-v2 ×27;
  - ENV-v1 → ENV-v2 ×17;
  - delivery sentences ×19;
  - canonical-assignment sentence ×19;
  - RETAIN-v3 sentence ×8;
  - three sport-file sentences ×11 each;
  - prompt version ×23.
- **Edited by hand:**
  - prompt 1 core (mode, inputs, Model shadow after the card, analyst method, structural-handling rule, step 7, mandatory output);
  - prompts 2, 3 (new §4 model shadows, new §6 settlement-phase assignment), 4 (§0 intake), 6, 8;
  - COMMON_OPERATING_PROTOCOL and the prompt index (one history heading the version swap had renamed was restored to v22.2);
  - EXECUTION_ENVIRONMENT_PROTOCOL (rewritten as ENV-v2);
  - MINI_LOG_IDENTITY_PROTOCOL;
  - FORECAST_CYCLE_PROTOCOL (new pregame section; release-scope correction);
  - CURRENT_RULES §0–§1;
  - CARD_AND_LOG_TEMPLATES (Model shadow line in the decision block; authority and C2 wording);
  - PROMPTS, README, ml/README, CURRENT_STATE, CHANGELOG, .gitattributes.
- **Archive:** [archive/superseded_2026-10-22-1/](../../../archive/superseded_2026-10-22-1/), the committed bytes of every changed Markdown file. Code history is in git.

### Records

- New active mini [research/active_minis/20261022F6K3OJNO.md](../../active_minis/20261022F6K3OJNO.md): 47,300 bytes, SHA-256 `e826aa99…7729`.
  - It carries `LOCAL-20261021OKCSASR01-G0001` byte-for-byte (block SHA-256 `9964e128…854a`, 30,739 bytes).
  - It adds `LOCAL-20261022F6K3OJNO-G0001`, the Díaz Acosta v Basilashvili draft, as READ_ONLY_DRAFT / NOT_ISSUED.
  - It lists the canonical obligations as pointers.
  - `python -m ml primary verify-log --mini` gives 2 cards, 2 analyst.
- The owner-supplied minis are copied under [research/active_minis/received/2026-10-22/](../../active_minis/received/2026-10-22/):
  - OKCSASR01: 38,819 bytes, `ce1b031d…e789`;
  - T7K4R9F2: 14,140 bytes, `45c7dc61…1e89`.

  These copies were made from the document text delivered in this session; the original attachment bytes were not separately available. The two OKCSASR01 attachments were identical, so one copy is kept.
- No ID was assigned, reserved or consumed. Highest P-622 and next P-623 are unchanged. No grade, forecast or issued record changed.

## Behaviour before and after

| Step | Before (v22.2) | After (v23.0) |
|---|---|---|
| Who runs prompts 1–3 | External chat, read-only, no code | This repository, internet research, commit and push |
| Card probability | Hand arithmetic, no code | The analyst's own declared distribution; code may compute it; still no model input |
| Model | Never before a game | `pregame run` after the card: model, baseline and card frozen on identical rows, or an honest NOT_RUN receipt |
| Settlement | Hand settlement; import later, separately | Card, then shadow (`cycle settle`), then the prompt-4 import in the same session |
| Canonical IDs | Prompt 4 import | Same import, now run as the last step of settlement (settled events only) |
| Release lifetime | Any ml/ edit retired it | Only edits inside the cycle's import closure do |
| Model judged | 50 events + 8 weeks (enforced) | Unchanged floors; `pregame status` flags a progress review at either |

## Verification

- `python -m pytest ml/tests`: **514 passed** (5 min 11 s). After the final dependency-map fix, the four affected files (prompt consistency, pregame, execution, chat execution) were re-run: **131 passed**.
- Manual readback:
  - the prompt 1 core, prompts 2–4 and the sport files show no remaining `EXTERNAL_CHAT` instruction for new work;
  - the active mini's carried block is byte-identical to the received file;
  - every modified Markdown control has an archive copy;
  - `python -m ml pregame status` lists NHL-CYCLE-4 and MLB-CYCLE-4 with 0 events (ACCUMULATING).
- Not exercised: a live `pregame run` on a real fixture. No game was requested in this session; NHL is the only in-season competition with a release.

## Readiness, separately

| Question | Status |
|---|---|
| Can prompt 1 run here with a model shadow? | Yes, for NHL and MLB (active releases). Every other competition records NOT_RUN_NO_RELEASE |
| Does the model feed the card? | No, by rule and by the card-first guard |
| Is any model qualified? | No. 0 prospective events; floors 8 weeks and 50 games |
| Basketball shadow | Not yet: needs admitted NBL/NBA/EuroLeague history and a release (2026-10-21 review, recommendations 1–5) |
| RL | No forecasting role (unchanged) |

## Effects on in-progress work

- New cards go to mini 20261022F6K3OJNO.
- The two carried events await prompt 3, which will settle them and then assign their IDs through the import.
- Older minis keep their formats and their ENV-v1 provenance labels.
