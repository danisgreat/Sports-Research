"""Cross-card experiments on the recurring failure classes, with frozen cohorts, acceptance criteria and power plans (EVL-04).

  python -B -m research.experiments.cross_card build    # (re)write cross_card_v1.json from the definitions below
  python -B -m research.experiments.cross_card verify   # check the lock, hashes and recomputed power plans (CI)
  python -B -m research.experiments.cross_card power --delta 0.02 --sd 0.08 --rows-per-week 5

Each experiment compares ONE candidate against ONE baseline on the same future rows (paired), under the EVL-02 gate:
the week-block bootstrap 95% CI of delta Brier and delta log loss must lie below 0, the candidate's calibration slope CI must
contain 1, and the decision must not depend on the resampling seed. A frozen cohort means: the inclusion rule, start
condition, stopping rule and acceptance are fixed and hashed BEFORE any cohort row is forecast. Nothing here grants
performance eligibility; the power plans state assumptions that the first four weeks of data must replace.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any

from scipy.stats import norm

ROOT = Path(__file__).resolve().parents[2]
LOCK = ROOT / 'research/experiments/cross_card_v1.json'
SCHEMA = 'cross-card-experiments-1'
ALPHA, POWER = 0.025, 0.80                      # one-sided improvement test at 2.5%, 80% power
ASSUMED_CARDS_PER_WEEK = 20                     # operator cadence assumption; change it and the plans change (and must be re-frozen)
MIN_BLOCKS = 8
MAX_FEASIBLE_WEEKS = 26

ACCEPTANCE = {
    'gate': 'EVL-02', 'delta_brier_ci95_upper_below': 0.0, 'delta_log_loss_ci95_upper_below': 0.0,
    'calibration_slope_ci_contains': 1.0, 'seed_stable': True, 'block': 'ISO week', 'min_blocks': MIN_BLOCKS,
    'evaluator': 'runtime.src.common.evaluation.FixedCohortEvaluator.evaluate',
}

# family_filter: the proposition families (research.operations.top_two.family) a cohort row must belong to.
DEFINITIONS: list[dict[str, Any]] = [
    {'id': 'XCARD-1', 'failure_class': 'FIRST_HALF_GOAL_OVERSELECTION', 'sport': 'Soccer', 'family_filter': ['first_half_goals'],
     'hypothesis': 'A fitted half-split model (separate first/second-half rates with a per-half correction) prices first-half goal rows '
                   'with lower Brier loss than the analyst first-half estimate used on cards P-148, P-234, P-250, P-342 and P-377.',
     'candidate': 'runtime.src.sports.soccer.halves (fit_half_split / half_distributions)', 'baseline': 'analyst first-half probability stated on the card',
     'delta_brier': -0.020, 'sd_paired': 0.08, 'share_of_cards': 0.35,
     'row_rule': 'every 1st-half goals row (Over/Under/BTTS-1H) on a soccer card issued after the freeze; both models price the same row'},
    {'id': 'XCARD-2', 'failure_class': 'RUNLINE_CUSHION_CEILING', 'sport': 'Baseball', 'family_filter': ['side_cushion_or_handicap'],
     'hypothesis': 'A bivariate run model with a shared environment shock and starter-leash mixture prices +1.5 run-line rows with lower '
                   'Brier loss than the analyst cushion estimate, removing the cushion ceiling seen on P-274, P-524, P-544 and P-547.',
     'candidate': 'runtime.src.sports.baseball.engine (environment sigma, matchup tau, starter leash)', 'baseline': 'analyst cushion probability on the card',
     'delta_brier': -0.015, 'sd_paired': 0.06, 'share_of_cards': 0.40,
     'row_rule': 'every baseball run-line row (+1.5 or -1.5, either side) on a baseball card issued after the freeze'},
    {'id': 'XCARD-3', 'failure_class': 'BASKETBALL_TOTAL_WITHOUT_PACE_MODEL', 'sport': 'Basketball', 'family_filter': ['match_total'],
     'hypothesis': 'A pace x efficiency bivariate model with a calibrated total spread prices combined-total rows with lower Brier loss '
                   'than a raw points-average total, addressing P-527, P-548 and P-553.',
     'candidate': 'runtime.src.sports.basketball.engine (pace x ppp means, calibrated sd/corr)', 'baseline': 'raw points-per-game average total',
     'delta_brier': -0.015, 'sd_paired': 0.07, 'share_of_cards': 0.30,
     'row_rule': 'every combined-total Over/Under row on a basketball card issued after the freeze'},
    {'id': 'XCARD-4', 'failure_class': 'TENNIS_IID_UNDERDISPERSION', 'sport': 'Tennis', 'family_filter': ['tennis_games', 'match_total'],
     'hypothesis': 'The exact point-to-match tree with a match-level form shock prices total-games and set-score rows with lower Brier loss '
                   'than the i.i.d. tree, whose deciding-set rate was 0.50 against a 0.358 population rate (P-541, P-551, P-555).',
     'candidate': 'runtime.src.sports.tennis.engine (mix_over_form, calibrated form_sigma)', 'baseline': 'same tree with form_sigma = 0 (i.i.d.)',
     'delta_brier': -0.020, 'sd_paired': 0.09, 'share_of_cards': 0.15,
     'row_rule': 'every total-games and games-handicap row on a tennis card issued after the freeze'},
    {'id': 'XCARD-5', 'failure_class': 'WEAK_SLATE_FORCED_RANK', 'sport': 'All', 'family_filter': ['*'],
     'hypothesis': 'Cards whose Rank 1 passes the gate (p_card >= 0.62 and a lead of >= 0.04 over the best non-complementary alternative) '
                   'win Rank 1 at least 5 points more often than cards labelled RANK1_UNSTABLE (PRD-03; also covers P-234 and P-520).',
     'candidate': 'Rank-1 gate in force (runtime.src.common.selection.rank1_gate)', 'baseline': 'ungated Rank 1 (the RANK1_UNSTABLE cohort)',
     'delta_brier': None, 'sd_paired': None, 'share_of_cards': 1.0, 'unit': 'cards', 'primary_metric': 'difference in Rank-1 win rate, gated minus unstable',
     'delta_rate': 0.05, 'p_unstable_share': 0.30, 'rate_sd': 0.5,
     'row_rule': 'Rank 1 of every card issued after the freeze; the gate label is recorded on the card before the event'},
    {'id': 'XCARD-6', 'failure_class': 'SHARED_DRIVER_TOP_TWO', 'sport': 'All', 'family_filter': ['*'],
     'hypothesis': 'Choosing Rank 2 to minimise P(Rank 1 and Rank 2 both lose) lowers the realised TOP2_ALL_LOST rate against choosing the '
                   'next-highest p_card row (PRD-02; P-176, P-492, P-541, P-549, P-555).',
     'candidate': 'Rank-2 diversification (runtime.src.common.selection.propose)', 'baseline': 'Rank 2 = next-highest p_card (shadow row, graded from the final score)',
     'delta_brier': None, 'sd_paired': None, 'share_of_cards': 1.0, 'unit': 'cards', 'primary_metric': 'difference in TOP2_ALL_LOST rate, diversified minus shadow',
     'delta_rate': -0.05, 'rate_sd': 0.4,
     'row_rule': 'every card issued after the freeze; the shadow Rank 2 comes from the priced ladder (appendix A5) and is graded from the final score. '
                 'Requires the machine-readable ladder; until it exists the experiment is REGISTERED_BLOCKED'},
]


def power_plan(delta: float, sd: float, rows_per_week: float, icc: float = 0.05, alpha: float = ALPHA, power: float = POWER) -> dict[str, Any]:
    """Rows and weeks needed to detect a paired mean difference `delta` (absolute) with SD `sd` per row.

    n_independent = ((z_alpha + z_power) * sd / |delta|)^2, inflated by the design effect 1 + (m - 1) * icc for m rows per week-block.
    """
    if delta == 0 or sd <= 0 or rows_per_week <= 0:
        raise ValueError('delta must be non-zero, sd and rows_per_week positive')
    z = norm.ppf(1 - alpha) + norm.ppf(power)
    n_independent = (z * sd / abs(delta)) ** 2
    deff = 1.0 + max(rows_per_week - 1.0, 0.0) * icc
    rows = math.ceil(n_independent * deff)
    weeks = max(math.ceil(rows / rows_per_week), MIN_BLOCKS)
    return {'delta': delta, 'sd_paired': sd, 'rows_per_week': round(rows_per_week, 4), 'icc_assumed': icc, 'alpha_one_sided': alpha,
            'power': power, 'design_effect': round(deff, 4), 'n_independent': math.ceil(n_independent), 'rows_required': rows,
            'weeks_required': weeks, 'feasible_within_weeks': weeks <= MAX_FEASIBLE_WEEKS, 'max_weeks': MAX_FEASIBLE_WEEKS}


def _plan_for(d: dict[str, Any]) -> dict[str, Any]:
    cards_per_week = ASSUMED_CARDS_PER_WEEK
    rows_per_week = cards_per_week * d['share_of_cards']
    if d.get('unit') == 'cards':
        # difference of two proportions between arms of unequal size is handled by the variance of the difference in rates
        sd = d['rate_sd'] * math.sqrt(1.0 + (1.0 / d['p_unstable_share'] if 'p_unstable_share' in d else 1.0))
        plan = power_plan(d['delta_rate'], sd, rows_per_week)
        plan['note'] = 'cards, not rows; rate difference treated as a paired/unpaired contrast with the stated SD'
    else:
        plan = power_plan(d['delta_brier'], d['sd_paired'], rows_per_week)
    plan['feasibility_note'] = ('feasible: the cohort can finish inside the maximum window' if plan['feasible_within_weeks'] else
                                f"NOT feasible in {MAX_FEASIBLE_WEEKS} weeks at this cadence: results are directional monitoring until the plan is met "
                                "(pool further quarters, or accept a larger minimum effect); never read as significance early")
    plan['assumed_cards_per_week'] = cards_per_week
    plan['share_of_cards'] = d['share_of_cards']
    plan['assumption_basis'] = ('sd_paired approximates the mean absolute probability difference between candidate and baseline (delta ~ (p_c - p_b)(p_c + p_b - 2y)); '
                                'replace it with the observed value after four pilot weeks and re-freeze before the cohort starts')
    return plan


def canonical(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(',', ':')).encode('utf-8')


def protocol(d: dict[str, Any]) -> dict[str, Any]:
    body = {k: v for k, v in d.items() if k not in {'sd_paired', 'delta_brier', 'delta_rate', 'rate_sd', 'p_unstable_share'}}
    body.update({'schema': SCHEMA, 'status': 'REGISTERED_NOT_RUN' if d['id'] != 'XCARD-6' else 'REGISTERED_BLOCKED',
                 'cohort': {'inclusion': d['row_rule'], 'start': 'the first card issued after this protocol is frozen and its lock is committed',
                            'exclusions': ['rows with an unresolved contract definition', 'rows graded VOID', 'rows whose forecast was written after the event started'],
                            'unit': d.get('unit', 'rows'), 'stopping_rule': 'fixed: stop when rows_required AND weeks_required are both reached; no interim look decides the result',
                            'frozen': True},
                 'acceptance': dict(ACCEPTANCE), 'power_plan': _plan_for(d), 'performance_eligible': False})
    body['protocol_sha256'] = hashlib.sha256(canonical({k: v for k, v in body.items() if k != 'protocol_sha256'})).hexdigest()
    return body


def build_registry() -> dict[str, Any]:
    protocols = [protocol(d) for d in DEFINITIONS]
    return {'schema': SCHEMA, 'assumed_cards_per_week': ASSUMED_CARDS_PER_WEEK, 'alpha_one_sided': ALPHA, 'power': POWER,
            'protocols': protocols, 'feasible_count': sum(p['power_plan']['feasible_within_weeks'] for p in protocols)}


def verify(path: Path = LOCK) -> list[str]:
    problems: list[str] = []
    if not Path(path).exists():
        return [f'{path} is missing; run `python -B -m research.experiments.cross_card build`']
    stored = json.loads(Path(path).read_text(encoding='utf-8'))
    fresh = build_registry()
    if stored != fresh:
        problems.append('cross_card_v1.json differs from the definitions in cross_card.py (re-freeze with `build` only before any cohort row exists)')
    ids = [p['id'] for p in stored.get('protocols', [])]
    if len(ids) != 6 or len(set(ids)) != 6:
        problems.append(f'expected six distinct experiments, found {ids}')
    from research.operations import top_two
    classes = [p['failure_class'] for p in stored.get('protocols', [])]
    for cls in classes:
        if cls not in top_two.FAILURE_CLASSES:
            problems.append(f'{cls} is not in the failure-class taxonomy')
    for p in stored.get('protocols', []):
        body = {k: v for k, v in p.items() if k != 'protocol_sha256'}
        if hashlib.sha256(canonical(body)).hexdigest() != p['protocol_sha256']:
            problems.append(f"{p['id']}: protocol hash does not match its content")
        if p['performance_eligible'] is not False or not p['cohort']['frozen']:
            problems.append(f"{p['id']}: must be frozen and not performance eligible")
        for key in ('delta_brier_ci95_upper_below', 'delta_log_loss_ci95_upper_below', 'calibration_slope_ci_contains', 'seed_stable'):
            if key not in p['acceptance']:
                problems.append(f"{p['id']}: acceptance lacks {key}")
        plan = p['power_plan']
        if plan['rows_required'] < plan['n_independent'] or plan['weeks_required'] < MIN_BLOCKS:
            problems.append(f"{p['id']}: power plan is internally inconsistent")
    return problems


def evaluate(protocol_id: str, y_true, p_candidate, p_baseline, event_ids, lines, block_ids, registry: Path = LOCK) -> dict[str, Any]:
    """Run the pre-registered acceptance on completed cohort rows (rows-based experiments only)."""
    stored = {p['id']: p for p in json.loads(Path(registry).read_text(encoding='utf-8'))['protocols']}
    spec = stored[protocol_id]
    if spec['cohort']['unit'] != 'rows':
        raise ValueError(f'{protocol_id} is evaluated on cards, not probability rows')
    plan = spec['power_plan']
    from runtime.src.common.evaluation import FixedCohortEvaluator
    result = FixedCohortEvaluator.evaluate(y_true, p_candidate, p_baseline, event_ids_cand=event_ids, event_ids_base=event_ids, lines_cand=lines,
                                           lines_base=lines, block_ids=block_ids, min_sample_size=plan['rows_required'], min_blocks=MIN_BLOCKS)
    result['protocol_sha256'] = spec['protocol_sha256']
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('build')
    sub.add_parser('verify')
    p = sub.add_parser('power')
    p.add_argument('--delta', type=float, required=True)
    p.add_argument('--sd', type=float, required=True)
    p.add_argument('--rows-per-week', type=float, required=True)
    p.add_argument('--icc', type=float, default=0.05)
    args = parser.parse_args(argv)
    if args.command == 'build':
        LOCK.write_text(json.dumps(build_registry(), indent=1, sort_keys=True, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
        print(json.dumps({'written': str(LOCK), 'feasible': build_registry()['feasible_count']}))
        return 0
    if args.command == 'power':
        print(json.dumps(power_plan(args.delta, args.sd, args.rows_per_week, args.icc), indent=1))
        return 0
    problems = verify()
    print(json.dumps({'passed': not problems, 'problems': problems, 'experiments': 6}, indent=1))
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
