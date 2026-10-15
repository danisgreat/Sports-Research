# Primary mixture and scheduled-start horizon: proposal

**Owner instructions (15 October 2026):**

1. "continue the implementation after checking the other session's most recent implementation to see if your implementation is better and more accurate"
2. "there shouldn't be any cutoff, the cutoff can be whatever time is the expected game start in the game log, gather sources of information like lineups, confirmed starters, bench, other news, etc, up until then"

## A. Expert combination

The released primary runtime (PRIMARY-2026.10.15-v1, commit a826cf6c6) produced each primary distribution by drawing ONE of three fitted experts at random (delayed Exp3, γ = 0.10). It learned only from the drawn expert's top-two rows, in a fine context partition (policy, competition, endpoint, coverage, timing phase, recipe).

The problem is not a bandit. All three experts' complete grids are frozen in every bundle, so every expert's loss is observed after every final. Two consequences follow:

- **Selection is dominated.** Brier and log loss are convex, so the mixture with weights *w* scores no worse than the expected score of drawing an expert with probabilities *w* (Jensen). Exp3's exploration also forces at least γ/3 ≈ 3.3% probability on every arm, including the team-blind baseline, forever.
- **Learning was starved.** Only the drawn arm was updated, only on its own top-two rows, and only within contexts so narrow that most would never repeat.

Proposal: replace the bandit with full-information exponential weights (Hedge) over the same three experts, on common questions (home-win and over-league-line Brier). Warm-start the weights from pre-horizon history, update them from settled bundles, and publish the deterministic mixture. Keep every admission, custody, endpoint, DATA_HOLD and market-firewall gate of v1.

## B. Information horizon

v1 required a free-standing `cutoff` at or before the issue time. Proposal: remove it. The horizon becomes the game's scheduled start from the game log, and lineups, confirmed starters, bench and news are researched up until then. It moves earlier only where the facts require: an earlier actual issue, or a verified earlier first play.

## Acceptance

- The mixture must not be worse than Exp3 in a walk-forward replay on the runtime's own experts.
- Every v1 rejection test must still pass.
- Tampered weights, horizon leakage and a `cutoff` column must be rejected.
- A real-archive mechanics run must succeed.

The replay is historical development evidence. It certifies no prospective skill.
