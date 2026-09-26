# Distribution models — Markdown implementation

Revision **MIR-2026.09.19-v2**. Authority: METHOD v4.2, SCORING_AND_VALIDATION and NUMERICAL_PROGRAM. This document implements the calculation layer and specifies estimation/data dependencies. **No real-world model has been fitted or validated.** The executable standard-library reference below is retained inside Markdown as requested; its synthetic acceptance cases prove arithmetic and rejection behavior only.

## 1. MLB A0 and A1

**A0 empirical joint final-score baseline.** Enumerate eligible completed games before the forecast cutoff. Use one `(home_runs, away_runs)` outcome per event, rather than independent home/away empirical draws. The joint empirical distribution retains observed covariance and endpoint behavior. With a context subset of size n and a league-prior grid G, use `(context_counts + k*G)/(n+k)` with k fixed in training/tuning. Report n and k. No context available means fall back to G. Forecasting a current park from its future season totals is prohibited. Empirical zero cells remain zero; log scores can be infinite. Any smoothing is a separately frozen model, not a display-time probability floor.

**A1 interpretable hierarchical joint-run challenger.** For side i against j, model `log(mu_i)=intercept+home_effect+attack_i−prevention_j+park+starter_relief_exposure+lineup+environment`. Partial-pool team, park and pitcher effects toward declared population means; select prior strengths and recency decay within time-ordered training/tuning only. For starter/relief, use expected batters faced or innings in each role and opponent-adjusted run rate, integrating an exit-state mixture; first likely relief arm depends on inning/score/availability. Do not count the same workload mechanism multiple times. Where these fields lack historical availability, use a separately labelled reduced-feature build.

Given a shared game environment `Z ~ Gamma(k, rate=k)`, conditionally independent team counts `H|Z ~ Poisson(Z*mu_h)` and `A|Z ~ Poisson(Z*mu_a)` have the joint negative-multinomial PMF implemented below. It gives covariance `mu_h*mu_a/k` and total variance `mu_h+mu_a+(mu_h+mu_a)^2/k`. This shared component is one candidate, not proof that all team dependence is positive. Opposing effects, extra innings and home batting termination can require explicit states. Test conditional overdispersion after covariate adjustment; the raw league variance alone does not estimate residual shape. Independent Poisson is the k→infinity diagnostic.

`pooled_rate` implements the Gamma-Poisson posterior mean `(runs+k*prior_rate)/(exposure+k)`. It is a transparent shrinkage primitive, not a substitute for fitting the full attack/prevention model or integrating posterior uncertainty. Full posterior predictive output mixes joint PMFs over parameter/scenario draws using `mixture`; retain the assumed or fitted weights and provenance. `shared_gamma_joint` takes rates and shape as explicit inputs and does not claim to estimate them.

Two endpoint routes must never be combined accidentally:

- A final-score model estimates completed final-score labels directly. Its conditional no-tie support is explicitly labelled, and it already includes extras/home termination in the target. This is a reduced-form approximation; check its home/away and key-margin calibration. Do not add extras again.
- A regulation-state model handles the skipped home ninth and walk-offs, then supplies tied-state extra-inning kernels under the exact rules version. `complete_baseball` composes these states. Each kernel is a distribution over additional home/away runs until completion, including repeated tied innings; it is not an independent one-inning draw. It must be estimated/simulated from admitted base-out/runner rules, pitcher/lineup and batting-order states. Capped/tie-permitting competitions require a different endpoint model.

The scoped first pilot compares A0 with A1 on identical games, total thresholds and scoring versions. Exact build/split/source dependencies remain in H0. Advanced A2/A3 models are deferred until these baselines have legitimate evidence.

## 2. Soccer linked phase/full-match model

A0: independent home/away Poisson scores, with opponent-adjusted rates. A1: dynamic attack/prevention/home effects and an optional Dixon–Coles low-score correction. For home rate lambda, away rate mu and rho, multiply the (0,0), (0,1), (1,0), (1,1) cells by `1−lambda*mu*rho`, `1+lambda*rho`, `1+mu*rho`, `1−rho`, respectively. Reject any negative factor; estimate rho in training and check actual improvement. Bivariate/shared-factor alternatives are separate candidates, not corrections stacked automatically.

Fit first-half rates separately from second-half rates. Construct `P(H1,A1)` and `P(H2,A2 | H1,A1, pregame scenarios)`, then sum to obtain `P(HFT,AFT)`. `link_phases` implements this composition. First-half rates are not a fixed fraction of full-time rates; conditional second-half kernels can represent leading/trailing behavior, planned substitutions and pregame red-card scenarios. Actual later red cards cannot enter a pregame forecast. At live halftime, create a distinct live horizon/build and condition on the observed state.

One linked distribution must supply both phase and full-match goal lines, team goals, 1X2 and BTTS. Marginalization must reproduce the printed phase probabilities, and full-time team scores cannot be below first-half scores. Creation, finishing and goal allocation are distinct components. Soccer corners/shots need their own counts and period/provider definitions; goal grids do not generate them.

## 3. Cricket state model

State at each legal delivery: `(innings, legal_balls, runs, wickets, striker/non_striker, remaining_batters, bowler/remaining_quota, target, remaining_scheduled_balls, field_restrictions, weather_rules_state)`. Model joint runs, wicket and extra-ball outcomes; wides/no-balls need legal-ball bookkeeping rather than a fixed balls-per-over assumption. A wicket changes subsequent batter quality, strike, aggression and available resources. The opening six overs and eventual innings total are marginals of one state process, not independent phase success extrapolations.

Fit transitions on earlier same-format/opponent-adjusted data with partial pooling by player/role and uncertainty for sparse combinations. Integrate lineup, toss and interruption scenarios at pregame cutoff. Absorb on target reached, all out, allotted legal balls, declaration or the declared rules-specific endpoint. A chase stops when its target is reached; it never labels a hypothetical uncensored batting-first innings. Test-day targets also track overs/time left, innings transitions and stumps. Activation conditions are checked before outcomes; preserve P-445's NO ACTION example.

Validate wicket/resource-conditioned residuals, phase/innings coherence and target-censoring separately. No standalone coefficient is inferred from P-406's 68/2 powerplay and 118 final or P-445's chase. These identify missing state variables, not fitted weights.

## 4. Remaining sport scopes

| Sport | Retained A0/A1 and state representation | O/U implementation requirement |
|---|---|---|
| Basketball | Competition-specific empirical possession/efficiency baseline; partially pooled joint score/possession model | Shared pace, lineup stints, offensive rebounds, turnovers, free throws, late fouls and OT; quarter and full-game scores from linked states |
| American football | Empirical discrete score baseline; hierarchical drive outcome model | TD/try/FG/safety/non-offensive scores, field position, drive counts and clock; key margins 3/7 estimated at correct cutoff; league-specific OT; no 13.9 SD floor |
| AFL/AFLW | Separate competition scoring-shot/conversion baselines; hierarchical goals/behinds model | Territory and shots versus conversion, common weather/pace, discrete 6/1 scoring, substitutions and quarter linkage |
| Rugby league | Set/field-position empirical baseline; hierarchical tries/conversions/field goals | Possessions, errors/penalties, sin-bin states and golden-point endpoint; regulation and match totals separate |
| Ice hockey | Poisson/empirical regulation baseline; partially pooled shot/goal/goalie model | Manpower and empty-net timing, shared pace and goalkeeper scenarios; OT/shootout goals/results queried under exact contract definition |
| Tennis — scope added | Surface/format serve-return baseline; hierarchical point probabilities with match-state recursion | Point→game→set→match termination, tiebreak/final-set rules, best-of-three/five, retirement action and player workload; one joint games/sets/winner distribution |
| Rugby union — scope added | Competition-specific possession/scoring-event baseline; hierarchical tries/conversions/penalties/drop goals | Territory, cards/front-row/bench and kicker state; discrete score support, phase linkage and competition-specific draw/extra-time rules |

Tennis and union are DESIGN REGISTERED / DATA BLOCKED. All other sport families retain that status until an actual build exists. **2026-09-26(c):** reduced-feature A0/A1 builds of every row above now exist as code (`tools/sport_models.py`; `NUMERICAL_MODEL_REGISTER.md` §"2026-09-26(c)"). They use final scores only, so the state representations and O/U requirements in this table remain the specification for the full builds. Flexible boosting/neural challengers, learned rankers and pair selectors remain dormant. No cross-sport scalar predicts all totals, and no sport inherits MLB's margin frequencies.

## 5. Executable probability primitives

Run this block in memory with Python's standard library. Every PMF is a map from a nonnegative integer count, or a tuple of such counts, to probability. Truncated analytic grids declare their omitted mass and reject excessive truncation before renormalizing within the declared tolerance. Scores are never silently clipped.

```python
import math
from collections import Counter
from datetime import datetime

TOL = 1e-10

def check_pmf(pmf):
    if not pmf or any(not math.isfinite(p) or p < 0 for p in pmf.values()):
        raise ValueError('invalid probability mass')
    for key in pmf:
        values = key if isinstance(key, tuple) else (key,)
        if not values or any(type(x) is not int or x < 0 for x in values):
            raise ValueError('invalid count support')
    if abs(math.fsum(pmf.values()) - 1) > TOL:
        raise ValueError('mass does not sum to one')
    return pmf

def empirical(outcomes, prior=None, strength=0):
    outcomes = list(outcomes)
    if not math.isfinite(strength) or strength < 0:
        raise ValueError('invalid prior strength')
    if strength and prior is None:
        raise ValueError('prior required')
    if prior is not None:
        check_pmf(prior)
    if not outcomes and not strength:
        raise ValueError('no data or prior')
    counts = Counter(outcomes)
    if prior is not None:
        for key, p in prior.items():
            counts[key] += strength * p
    return check_pmf({key: v / (len(outcomes) + strength)
                      for key, v in counts.items()})

def pooled_rate(runs, exposure, prior_rate, prior_exposure):
    args = (runs, exposure, prior_rate, prior_exposure)
    if any(not math.isfinite(x) or x < 0 for x in args):
        raise ValueError('invalid rate inputs')
    if exposure + prior_exposure <= 0:
        raise ValueError('zero exposure and prior')
    return (runs + prior_rate * prior_exposure) / (exposure + prior_exposure)

def mixture(weighted_pmfs):
    weighted_pmfs = list(weighted_pmfs)
    if not weighted_pmfs or any(not math.isfinite(w) or w < 0
                                for w, _ in weighted_pmfs):
        raise ValueError('invalid mixture weights')
    if abs(math.fsum(w for w, _ in weighted_pmfs) - 1) > TOL:
        raise ValueError('mixture weights must sum to one')
    result = Counter()
    for weight, pmf in weighted_pmfs:
        check_pmf(pmf)
        for key, p in pmf.items():
            result[key] += weight * p
    return check_pmf(dict(result))

def _finite_grid(raw, tail_tolerance):
    mass = math.fsum(raw.values())
    omitted = 1 - mass
    if not 0 < tail_tolerance <= 1e-6:
        raise ValueError('declare a numerical tail tolerance <= 1e-6')
    if mass <= 0 or omitted < -TOL or omitted > tail_tolerance:
        raise ValueError('increase count support; omitted mass too large')
    return check_pmf({k: p / mass for k, p in raw.items()}), max(0., omitted)

def poisson_joint(home_rate, away_rate, max_count=80, tail_tolerance=1e-9):
    if any(not math.isfinite(x) or x <= 0 for x in (home_rate, away_rate)):
        raise ValueError('strictly positive finite rates required')
    if type(max_count) is not int or max_count < 1:
        raise ValueError('invalid support limit')
    def p(rate, n):
        return math.exp(-rate + n * math.log(rate) - math.lgamma(n + 1))
    raw = {(h, a): p(home_rate, h) * p(away_rate, a)
           for h in range(max_count + 1) for a in range(max_count + 1)}
    return _finite_grid(raw, tail_tolerance)

def shared_gamma_joint(home_rate, away_rate, shape, max_count=120,
                       tail_tolerance=1e-9):
    if any(not math.isfinite(x) or x <= 0
           for x in (home_rate, away_rate, shape)):
        raise ValueError('strictly positive finite rates/shape required')
    if type(max_count) is not int or max_count < 1:
        raise ValueError('invalid support limit')
    denominator = shape + home_rate + away_rate
    raw = {}
    for h in range(max_count + 1):
        for a in range(max_count + 1):
            logp = (math.lgamma(shape + h + a) - math.lgamma(shape)
                    - math.lgamma(h + 1) - math.lgamma(a + 1)
                    + shape * math.log(shape / denominator)
                    + h * math.log(home_rate / denominator)
                    + a * math.log(away_rate / denominator))
            raw[h, a] = math.exp(logp)
    return _finite_grid(raw, tail_tolerance)

def dixon_coles(home_rate, away_rate, rho, max_count=60):
    if not math.isfinite(rho):
        raise ValueError('invalid dependence parameter')
    grid, omitted = poisson_joint(home_rate, away_rate, max_count)
    factors = {(0, 0): 1-home_rate*away_rate*rho,
               (0, 1): 1+home_rate*rho, (1, 0): 1+away_rate*rho,
               (1, 1): 1-rho}
    if min(factors.values()) < 0:
        raise ValueError('negative Dixon-Coles cell')
    for key, factor in factors.items():
        grid[key] *= factor
    return check_pmf(grid), omitted

def total_pmf(joint):
    check_pmf(joint)
    result = Counter()
    for (h, a), p in joint.items():
        result[h+a] += p
    return check_pmf(dict(result))

def contract_masses(pmf, line, side='over'):
    check_pmf(pmf)
    if not math.isfinite(line) or side not in ('over', 'under'):
        raise ValueError('invalid line/side')
    under = math.fsum(p for x, p in pmf.items() if x < line)
    push = math.fsum(p for x, p in pmf.items() if x == line)
    over = math.fsum(p for x, p in pmf.items() if x > line)
    return (over, push, under) if side == 'over' else (under, push, over)

def validate_vector(v):
    if len(v) != 3 or any(not math.isfinite(p) or p < 0 for p in v):
        raise ValueError('invalid W/P/L vector')
    if abs(math.fsum(v)-1) > TOL:
        raise ValueError('W/P/L must sum to one')

def decisive_probability(v):
    validate_vector(v)
    return None if v[1] == 1 else v[0] / (1-v[1])

def categorical_scores(v, outcome):
    validate_vector(v)
    if outcome not in ('WIN', 'PUSH', 'LOSS'):
        raise ValueError('not an action-settled W/P/L outcome')
    index = ('WIN', 'PUSH', 'LOSS').index(outcome)
    brier = math.fsum((p-(i == index))**2 for i, p in enumerate(v))/2
    logloss = -math.log(v[index]) if v[index] else math.inf
    q = decisive_probability(v)
    binary = None if outcome == 'PUSH' or q is None else (q-(index == 0))**2
    return {'brier_wpl_half': brier, 'log_loss': logloss,
            'brier_decisive': binary}

def rps(pmf, observed):
    check_pmf(pmf)
    if type(observed) is not int or observed < 0:
        raise ValueError('invalid observation')
    # Iterate beyond the forecast support when the observation is in the tail.
    cdf, score = 0., 0.
    for k in range(max(max(pmf), observed) + 1):
        cdf += pmf.get(k, 0.)
        score += (cdf-(observed <= k))**2
    return score

def link_phases(first_half, second_half_by_state):
    check_pmf(first_half)
    full, paths = Counter(), {}
    for (h1, a1), p1 in first_half.items():
        if not p1:
            continue
        kernel = check_pmf(second_half_by_state[h1, a1])
        for (h2, a2), p2 in kernel.items():
            paths[h1, a1, h2, a2] = p1*p2
            full[h1+h2, a1+a2] += p1*p2
    return check_pmf(dict(full)), check_pmf(paths)

def complete_baseball(regulation, extras_by_tied_state):
    check_pmf(regulation)
    final = Counter()
    for (home, away), p in regulation.items():
        if not p:
            continue
        if home != away:
            final[home, away] += p
            continue
        kernel = check_pmf(extras_by_tied_state[home, away])
        for (dh, da), q in kernel.items():
            if q and dh == da:
                raise ValueError('kernel must end in a completed non-tied game')
            final[home+dh, away+da] += p*q
    return check_pmf(dict(final))

def validate_training_rows(rows, cutoff, endpoint):
    # One completed training observation per event. Use timezone-aware instants.
    seen = set()
    def instant(value):
        t = datetime.fromisoformat(value.replace('Z', '+00:00'))
        if t.utcoffset() is None:
            raise ValueError('timezone required')
        return t
    boundary = instant(cutoff)
    for row in rows:
        if not row['event_id'] or row['event_id'] in seen:
            raise ValueError('duplicate/missing event identity')
        seen.add(row['event_id'])
        if row['endpoint'] != endpoint or row['status'] != 'FINAL':
            raise ValueError('endpoint or final-state mismatch')
        issue = instant(row['forecast_cutoff'])
        if instant(row['features_available_at']) > issue:
            raise ValueError('future feature at forecast cutoff')
        if not issue < instant(row['start_at']) < boundary:
            raise ValueError('invalid pregame/training ordering')
        label_time = instant(row['label_available_at'])
        if not instant(row['start_at']) < label_time < boundary:
            raise ValueError('label unavailable before training cutoff')
        for field in ('home_runs', 'away_runs'):
            if type(row[field]) is not int or row[field] < 0:
                raise ValueError('invalid final score')
    return len(seen)
```

## 6. Acceptance cases and execution boundary

Required checks: normalized nonnegative support; integer/half-line complement and push identities; exact conditional-q scoring; realised pushes retained; all-push q undefined; infinite log loss retained; out-of-support RPS; rejected negative/unnormalized masses; finite-grid tail tolerance; shared-environment means/covariance; valid/invalid Dixon–Coles factors; linked-phase marginal recovery; full-match scores no lower than phase scores; tied-on-line baseball completion always Over; no tied completed MLB state; missing extra kernel fails; duplicate events/future features/late labels/timezone/endpoint mismatches fail.

The runnable acceptance suite and its actual results are recorded in audit_2026-09-17_implementation/VALIDATION.md. Analytical/synthetic checks cannot replace the future H0 quality audit, fitted-parameter uncertainty, same-game baseline comparison, untouched TEST or prospective shadow. No model-family recommendation in this document is a demonstrated accuracy gain.

<!-- DEEP-RESEARCH-IMPLEMENTATION-2026-09-19-V42 -->
## 2026-09-19(c) — required wrapper around every numerical recipe

Every recipe is called through a market-independent wrapper:

```text
sports_evidence = validate_and_freeze_sources(raw_records, cutoff)
features = build_features(sports_evidence)          # no contract line/odds/fantasy fields
predictive_distribution = model.predict_distribution(features)
freeze(predictive_distribution, model_hash, feature_hash, source_hash)
contract_probs = query_distribution(predictive_distribution, contract_line)
```

A recipe that accepts `line`, `odds`, `price`, `market_probability`, `consensus`, `closing_line`, fantasy projection/ownership or an equivalent proxy as a predictive argument is non-compliant. Any optional scenario adjustment must be sourced to a real sporting state and either learned from chronological training data or represented as an explicit uncertainty mixture; arbitrary signed centre edits are invalid.
