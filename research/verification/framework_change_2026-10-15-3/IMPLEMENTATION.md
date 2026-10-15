# Primary mixture and scheduled-start horizon: implementation

PRIMARY-2026.10.15-v2 / MDS-2026.10.15-v14.0 / CR-2026.10.15-R3 / TIMING-2026.10.15-v2. [Proposal](CHANGE_PROPOSAL.md) · [verification](VERIFICATION_REPORT.md) · [document custody](DOCUMENT_CUSTODY.csv) · originals in [archive/superseded_2026-10-15-3/](../../../archive/superseded_2026-10-15-3/ARCHIVE_RECEIPT.md).

## 1. Comparison with the other session's v1

| Aspect | v1 (PRIMARY_EXP3_V1, a826cf6c6) | v2 (PRIMARY_HEDGE_MIX_V2) | Verdict |
|---|---|---|---|
| Experts | FAST 90 d, SLOW 365 d, LEAGUE_BASELINE; cricket C2/C0 | Unchanged | Kept |
| Primary distribution | One expert drawn at random | Weighted mixture of all three grids (union support, still a coherent joint grid) | v2: never worse in expectation (Jensen); replay below |
| Learning signal | 1 − Brier of the drawn expert's own top-two rows; others unobserved | Every expert's Brier on common questions: home win, plus over the league median line | v2: full information, comparable across events |
| Starting state | Uniform, COLD_START | Warm start: weekly refits over the last 30 game-weeks before the horizon | v2: no cold start in any league with history |
| Context | policy, competition, endpoint, coverage, phase, recipe | policy, competition, endpoint | v2: v1's partition would almost never repeat |
| Exploration floor | γ/3 on each arm forever, including the team-blind baseline | None needed (full information) | v2 |
| Reproducibility | Seeded random draw | Deterministic; weights recomputed and checked in verify_bundle | v2 |
| Admission, custody, DATA_HOLD, endpoint, cricket, contracts, firewall | Their implementation | Unchanged; all their rejection tests kept | Kept as written |
| Evidence cutoff | Free-standing `cutoff` ≤ issue | `scheduled_start` from the game log; horizon = earliest of scheduled start, issue, verified actual start | Owner instruction B |

**Replay** ([results](../../model_shadow/PRIMARY_POLICY_REPLAY/RESULTS.md); `python -m ml.evaluation.primary_replay 10`). 28 discovered competitions, 41,752 games, 1,909 competition-weeks. The replay is walk-forward with weekly refits and η tuned on earlier seasons only. Exp3 is scored as its expected loss over 200 seeds.

- Pooled home-win Brier, mixture − Exp3: **−0.0081 [−0.0087, −0.0074]**.
- The difference was below zero in 23 competitions; Minor Leagues, EuroBasket, Danish Metal Ligaen, NRL and VFLW span zero; none was above zero.
- Exp3 priced 15–34% of cards from the team-blind baseline; the mixture gave it about 0 weight.
- Against the best single expert picked in hindsight, the mixture is level, except Greece (+0.0007), which is a DATA_HOLD league that the runtime refuses anyway.

## 2. Code

- [ml/primary.py](../../../ml/primary.py), key functions:
  - `warm_start`, `expert_loss`, `mix_grids`, `hedge_weights` and `eta_for` (η from the replay table, or a labelled default of 2.0);
  - `feedback_losses`, which re-derives each recorded loss from the frozen grids and the evidence final and rejects any mismatch;
  - `information_horizon`;
  - `verify_bundle`, which recomputes the weights and re-mixes the grids;
  - `settle`, which scores every expert and writes `NOT_COMPUTED` rather than a zero when the primary rows pushed.
- Removed: `probabilities` and the Exp3 constants. The CLI's `--seed` is accepted and ignored.
- [ml/evaluation/primary_replay.py](../../../ml/evaluation/primary_replay.py): new replay with a code-digest stability receipt.
- [ml/tests/test_primary.py](../../../ml/tests/test_primary.py): the Exp3 tests are replaced by mixture, full-information feedback, Jensen, union-support, tamper, warm-start leakage, labelled η default, horizon-source, no-`cutoff` and late-information tests.

## 3. Documents

PRIMARY_PREDICTION_PROTOCOL (rewritten §1, §2, §4) and TIMING_RESEARCH_PROTOCOL (§1 horizon paragraph, §3). CURRENT_RULES header, §0, §5 timing, PR-04 step 2 and R28. METHOD steps 2–3 and the primary paragraph. SELECTION_RULES (primary paragraph). CARD_AND_LOG_TEMPLATES (header, Timing field, receipt line, C11 and C19). VERIFICATION_PROTOCOL, ARCHIVE_USE_GUIDE (R1), CURRENT_STATE, HYPOTHESIS_REGISTER (amendment), README and CHANGELOG. The amendment notes in ml/README, research/model_shadow/README and ML_RL_IMPLEMENTATION_FRAMEWORK. In research/prompts: README and COMMON_OPERATING_PROTOCOL.

**Prompt files are not edited.** research/prompts/1_GAME_CARD.md held the owner's uncommitted filled-in game requests and was left untouched. The prompt companion amendment instead tells every prompt to read "bandit" or "selected arm" as the v2 mixture, and "Requested cutoff" as the game-log scheduled start. Prompt version P-2026.10.15-v13.0 is therefore unchanged.

## 4. Limitations (stated, not fixed)

- **η and one-hot weights.** η is tuned per competition on replay seasons, up to 50. Warm starts sum hundreds of games, so weights are often near one-hot (NBA: FAST = 1; EPL: SLOW = 1). The gain over Exp3 is therefore mainly from never drawing a worse expert, not from diversification. Rescaling η by game count is untested and was not adopted.
- **No fitted availability.** Lineups, starters, bench and news are gathered up to the scheduled start but are still not fitted model features (unchanged from v1).
- **Same-day history.** Training games on the horizon's UTC date are still excluded because archive dates carry no time.
- **No prospective evidence.** No bundle has been issued under either version. Every number here is historical development evidence.
