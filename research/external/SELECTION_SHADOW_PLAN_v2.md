# SELECT-SHADOW-v2: registered shadow plan for the top two picks (v29.4, 23 November 2026)

This registration replaces [SELECT-SHADOW-v1](SELECTION_SHADOW_PLAN_v1.md) before v1 reached any eligible game. It
takes effect at its first independently verified GitHub publication on `main`, the time GitHub recorded for the push
of the commit that first holds this file's exact content. It does not change
[EVALUATION_PLAN_v29.0](EVALUATION_PLAN_v29.0.md). That plan's card protocol, selection policy (the registered rank)
and 600-game Brier test stay frozen. Nothing here reaches a card, a seal, a rank or the registered score. Code:
[`ml/selection_shadow.py`](../../ml/selection_shadow.py).

## 1. Why v1 was replaced

An external review on 23 November 2026 found four defects in v1, and each was reproduced:

1. v1 judged picks one at a time (hit rate per decided pick). A policy that issued one strong pick per card could pass
   it while being useless for a two-pick card. The owner's objective is two picks that both win.
2. v1 dropped a pick on the intake's `NO_DIRECTION` flag, which uses the stated p, while ranking on the conditional p.
   Over 0.50, Under 0.36 (push 0.14) is 58.14% given a decision, yet v1 dropped it.
3. The coverage file and registration time came from the caller, so a run could be fed inputs that were never verified.
4. A second outcome file could silently overwrite a grade.

## 2. The policies, fixed now

All three policies are computed from the same sealed cards.

- **REGISTERED_RANK**: Rank 1 and Rank 2 exactly as the frozen ranker gives them.
- **SHADOW_SIGNAL**: the candidates are the favoured sides of priced supplied lines. There is one probability
  throughout: the stated p conditional on a decision, p divided by the sum of the line's priced sides. The stated p and
  the push probability (1 minus that sum) are shown beside it. A candidate is dropped if its conditional p is below
  0.55 (`BELOW_0.55_CONDITIONAL`; the same 0.05 margin as the registered boundary, not a value tuned on results), or if
  it is flagged `CONTRADICTS_OWN_CENTRE`, `INCOHERENT_ACROSS_LINES` or `NO_RESULT_SOURCE`. A later label that is the
  same contract as a higher one is dropped (`SAME_CONTRACT_AS_A_HIGHER_PICK`). "Same contract" is read from the
  registered request's definitions using the registration's own rule. A winner equals a half-point handicap only on
  the deciding score where no draw is possible, so NPB and KBO baseball, hockey settled in regulation, and a handicap
  on another statistic all stay distinct. Without the definitions, only an exact repeat of family, sides and lines
  counts. The two highest remaining are kept, label order breaking ties. One pick, or none (`NO_STRONG_PICK`), is
  allowed.
- **SHADOW_STRICT**: as SIGNAL, and it also drops `UNMEASURED_AVAILABILITY_PRICED`.

Every pair, the registered ranker's included, is marked `SAME_QUANTITY` when the registered definitions put both labels
on one family, period, endpoint, action and unit, and otherwise `SAME_GAME`. Both kinds are dependent, and the
direction of that dependence is not known. Pair counts by marker are reported; no joint probability is modelled here.

## 3. Inputs, universe and denominators

The inputs are an intake built from every sealed card, the outcome files, and a registered `ml one-chat score` folder
built from that same intake and those same outcome files.

- **Grades.** Each `(card, label, side)` takes one grade. The same grade repeated across files is accepted.
  Conflicting grades are refused, and the run stops. In the decision, every pick of an eligible request must be graded
  `WIN`, `LOSS`, `PUSH` or `VOID`. A missing grade stops the run.
- **Universe.** The universe is the registered score's eligible sequence (`SEQUENCE.csv`, in the scorer's order) where
  the score reports zero custody problems. Only requests whose seal server time is later than this plan's verified
  `main` publication are included, and that time is read from git and GitHub, never from the caller. A run that lacks
  any of these is `DESCRIPTIVE_INPUTS_NOT_VERIFIED` and gives no verdict.
- **Excluded games.** Cards sealed before publication are development data: reported, never decided. A game unsettled
  at the registered 14-day deadline is outside the sequence, exactly as in the registered score.

`SHADOW_SCORE.csv` reports, for each policy:

- requests, requests with a pick, and requests with a pair;
- pair coverage, picks, wins, losses, and pushes or voids;
- the hit rate per pick and per slot;
- decided pairs, with both, one or neither won;
- both-won per pair and per request;
- `SAME_QUANTITY` pairs.

## 4. Decision

The objective is two distinct picks that both win. The statistic is **both-won per eligible request**: the share of
eligible requests on which the policy issued two distinct picks and both won. A request with fewer than two picks, or
with a push or void in its pair, counts as not both won. Abstaining therefore costs a policy.

The decision is taken once, on the first 100 requests of the universe (calendar-free, as the registered checkpoint).
For each variant, the statistic is the variant's rate minus the registered ranker's on the same requests. Its interval
is a request-clustered percentile bootstrap: 10,000 resamples, seed 20261123, and alpha 0.025 for each variant, which
splits 0.05 between the two.

- `IMPROVEMENT_DEMONSTRATED`: the lower end of the interval is above 0, **and** the variant issued two distinct picks on
  at least half the requests (pair-coverage floor 0.5, fixed now).
- `NOT_DEMONSTRATED`: anything else at 100 requests.
- `DESCRIPTIVE_BELOW_100_REQUESTS`: fewer than 100 requests. Nothing is claimed.

The per-pick hit rate, the slot rates and the pair markers are descriptive. A variant that passes becomes a candidate
for a new registration of the card selection policy. It never replaces the registered rank automatically.

## 5. Power and limits

The ranker always issues two picks, so a variant must win both more often while abstaining on some requests. That is
hard to show, and the plan accepts it: a result that only appears by changing the objective after the data would not
count. Thresholds read off settled history (0.58, 0.62) are not used. Any later threshold or objective is registered
here as a new version before it is tested.

On the 13 development cards, the registered ranker issued 26 picks and won 12; of its 13 pairs, 4 won both, 4 one
and 5 neither (both-won per request 0.31). SIGNAL picked on 9 cards and issued 14 picks, winning 7. It made 5 pairs:
1 won both, 3 one and 1 neither (pair coverage 0.38, both-won per request 0.08). STRICT issued nothing. These cards
are development data only.

```text
python -m ml.selection_shadow score --intake <intake from seals> --outcomes <OUTCOMES.csv files> \
    --score <registered score folder on the same intake and outcomes> --out <folder>
```
