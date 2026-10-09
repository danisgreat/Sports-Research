"""Top-two counting (Rule T2, SCV-2026.10.09-v4) shared by settlement, import and cohort review.

Only Rank 1 and Rank 2 can count as wins. Ranks 3 and 4 are graded for calibration and
learning but never enter win counts. PUSH and VOID leave the denominators; they are never
losses. A card without a forecast (NO_FORECAST) contributes nothing to counted metrics.
"""
from __future__ import annotations
import collections
import math
import re

from research.operations.diagnostic_rank import metrics as slate_metrics

GRADES = {'W': 'WIN', 'L': 'LOSS', 'P': 'PUSH', 'V': 'VOID'}
GRADE_CODES = {v: k for k, v in GRADES.items()}
EVIDENCE = {
    'A': 'Official / field-owner terminal record for the target field',
    'B': 'Structured provider or multi-source agreement for the target field; official score',
    'C': 'Best-available single-secondary, conflicted or provisional evidence adopted as final',
    'E': 'Estimated from a partial measurement that bounds the target field; confidence stated',
    'OP': "Sporting endpoint known; operator rule absent; card's frozen assumption or framework default applied",
    'X': 'No admissible data; row settled VOID',
}
UNSTABLE_P = 0.60  # Rank 1 below this is labelled RANK1_UNSTABLE (card rule A4.6)
CARD_CLASSES = ('TOP2_ALL_WON', 'TOP2_SPLIT', 'TOP2_ALL_LOST', 'VOID', 'NO_FORECAST')
FAILURE_CLASSES = (
    'FIRST_HALF_GOAL_OVERSELECTION', 'RUNLINE_CUSHION_CEILING', 'BASKETBALL_TOTAL_WITHOUT_PACE_MODEL',
    'TENNIS_IID_UNDERDISPERSION', 'RANK_BY_Q_NOT_P', 'SHARED_DRIVER_TOP_TWO', 'HANDICAP_TAIL_OVERREACH',
    'SMALL_SAMPLE_STRENGTH_OVERREACH', 'PHASE_INCOHERENCE', 'CORNER_ROW_WITHOUT_PROVIDER_OR_NB_MODEL',
    'OVERCONFIDENT_PROBABILITY', 'WEAK_SLATE_FORCED_RANK', 'QUALITATIVE_RANKS_WITHOUT_DISTRIBUTION', 'REGIME_IGNORED',
    'UNFITTED_ANALYST_ADJUSTMENT', 'LATE_INFORMATION', 'ENDPOINT_OR_CONTRACT', 'SOURCE_OR_IDENTITY', 'VARIANCE', 'OTHER',
)
# Synonyms used in the 2026-10-09 deep retrospections, mapped onto the taxonomy above.
FAILURE_CLASS_ALIASES = {'TOP_ROW_DEPENDENCE': 'SHARED_DRIVER_TOP_TWO', 'OVERCONFIDENT_TEAM_TOTAL': 'OVERCONFIDENT_PROBABILITY',
                         'FINALS_REGIME_IGNORED': 'REGIME_IGNORED'}


def failure_class(value):
    """Normalise a recorded failure class onto the taxonomy (None stays None)."""
    if not value:
        return None
    value = FAILURE_CLASS_ALIASES.get(value, value)
    return value if value in FAILURE_CLASSES else 'OTHER'


def grade_code(value: str) -> str:
    """Normalise WIN/LOSS/PUSH/VOID or W/L/P/V to the one-letter code."""
    text = str(value).strip().strip('*').upper()
    if text in GRADES:
        return text
    if text in GRADE_CODES:
        return GRADE_CODES[text]
    raise ValueError(f'unknown grade {value!r}')


def family(contract: str) -> str:
    """Coarse proposition family used for failure-class and calibration tallies."""
    c = contract.lower()
    if 'corner' in c:
        return 'corners'
    if re.search(r'\b(1st|first)[ -]half\b|\b1h\b', c):
        return 'first_half_goals'
    if re.search(r'\bouts\b|strikeouts|\bprop\b', c):
        return 'player_prop'
    if 'games' in c:
        return 'tennis_games'
    if re.search(r'team (total|goals|runs|points)', c):
        return 'team_total'
    if 'both teams' in c or 'btts' in c:
        return 'btts'
    if re.search(r'\b(over|under)\b', c):
        return 'match_total'
    if re.search(r'[+\-−]\s?\d', c) or re.search(r'\b(x2|1x|12)\b', c) or 'or draw' in c or 'double chance' in c:
        return 'side_cushion_or_handicap'
    if 'moneyline' in c or re.search(r'\bml\b', c) or 'winner' in c or re.search(r'\bwin\b', c):
        return 'side_winner'
    return 'other'


def card_outcome(rows, no_forecast: bool = False):
    """Return (card_class, counted_wins, live_top_two_rows) for rows [(rank, grade_code), ...]."""
    top = {rank: grade for rank, grade in rows if rank in (1, 2)}
    live = [g for g in top.values() if g in {'W', 'L'}]
    wins = sum(g == 'W' for g in live)
    if no_forecast:
        return 'NO_FORECAST', 0, 0
    if not live:
        return 'VOID', 0, 0
    if wins == len(live):
        return 'TOP2_ALL_WON', wins, len(live)
    if wins == 0:
        return 'TOP2_ALL_LOST', wins, len(live)
    return 'TOP2_SPLIT', wins, len(live)


def ndcg_at_2(rows):
    """Full-slate NDCG@2 (October 8 clarification); None for slates with push/void rows."""
    ordered = [GRADES[g] for _, g in sorted(rows)]
    result = slate_metrics(ordered)
    return None if result is None else result['ndcg_at_2']


def wilson(wins: int, n: int, z: float = 1.96):
    """95% Wilson interval; (None, None) when n is 0."""
    if n == 0:
        return (None, None)
    p = wins / n
    denom = 1 + z * z / n
    centre = p + z * z / (2 * n)
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((centre - half) / denom, (centre + half) / denom)


def summarise(cards):
    """Aggregate counted metrics over card dicts.

    Each card: {'id', 'sport', 'rows': [(rank, grade, p_card_or_None, contract)], 'no_forecast': bool,
    'winner_call': 'CORRECT'|'INCORRECT'|other, 'failure_class': str|None}.
    """
    totals = collections.Counter()
    by_sport = collections.defaultdict(collections.Counter)
    rank1_family = collections.defaultdict(collections.Counter)
    failure = collections.Counter()
    ndcgs = []
    for card in cards:
        rows = [(r[0], r[1]) for r in card['rows']]
        outcome, wins, live = card_outcome(rows, card.get('no_forecast', False))
        if outcome == 'NO_FORECAST':
            totals['no_forecast_cards'] += 1
            continue
        totals['cards'] += 1
        totals[outcome] += 1
        totals['counted_wins'] += wins
        totals['counted_live_rows'] += live
        rank = {r[0]: r for r in card['rows']}
        for k in (1, 2):
            totals[f'rank{k}_{rank[k][1] if k in rank else "V"}'] += 1
        if outcome in {'TOP2_ALL_WON', 'TOP2_SPLIT'}:
            totals['hit_at_2'] += 1
        totals['winner_' + str(card.get('winner_call', 'NOT_AUDITED'))] += 1
        sport = by_sport[card.get('sport', 'UNKNOWN')]
        sport['cards'] += 1
        sport['counted_wins'] += wins
        sport['counted_live_rows'] += live
        sport['rank1_' + (rank[1][1] if 1 in rank else 'V')] += 1
        if 1 in rank:
            if rank[1][1] in {'W', 'L'}:
                rank1_family[family(rank[1][3])][rank[1][1]] += 1
            if rank[1][1] == 'L':
                failure[failure_class(card.get('failure_class')) or 'UNCLASSIFIED'] += 1
        value = ndcg_at_2(rows)
        if value is not None:
            ndcgs.append(value)
    live1 = totals['rank1_W'] + totals['rank1_L']
    live2 = totals['rank2_W'] + totals['rank2_L']
    summary = {
        'totals': dict(totals),
        'counted_win_rate': totals['counted_wins'] / totals['counted_live_rows'] if totals['counted_live_rows'] else None,
        'counted_win_rate_ci95': wilson(totals['counted_wins'], totals['counted_live_rows']),
        'rank1_win_rate': totals['rank1_W'] / live1 if live1 else None,
        'rank1_ci95': wilson(totals['rank1_W'], live1),
        'rank2_win_rate': totals['rank2_W'] / live2 if live2 else None,
        'rank2_ci95': wilson(totals['rank2_W'], live2),
        'mean_ndcg_at_2': sum(ndcgs) / len(ndcgs) if ndcgs else None,
        'ndcg_slates': len(ndcgs),
        'by_sport': {k: dict(v) for k, v in sorted(by_sport.items())},
        'rank1_by_family': {k: dict(v) for k, v in sorted(rank1_family.items())},
        'rank1_failure_classes': dict(failure),
    }
    return summary


def calibration(cards, bins=(0.0, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0)):
    """Reliability table, Brier and log loss over every graded W/L row with a stated p_card (all ranks)."""
    pairs = [(r[2], 1.0 if r[1] == 'W' else 0.0) for c in cards if not c.get('no_forecast')
             for r in c['rows'] if r[1] in {'W', 'L'} and r[2] is not None and 0.0 < r[2] < 1.0]
    table = []
    for lo, hi in zip(bins, bins[1:]):
        members = [(p, y) for p, y in pairs if lo <= p < hi or (hi == 1.0 and p == 1.0)]
        if members:
            table.append({'bin': f'[{lo:.1f},{hi:.1f})', 'n': len(members),
                          'mean_p': sum(p for p, _ in members) / len(members),
                          'win_rate': sum(y for _, y in members) / len(members)})
        else:
            table.append({'bin': f'[{lo:.1f},{hi:.1f})', 'n': 0, 'mean_p': None, 'win_rate': None})
    if not pairs:
        return {'n': 0, 'bins': table, 'brier': None, 'log_loss': None, 'climatology_brier': None,
                'reliability_slope': None, 'reliability_intercept': None}
    n = len(pairs)
    base = sum(y for _, y in pairs) / n
    mean_p = sum(p for p, _ in pairs) / n
    var_p = sum((p - mean_p) ** 2 for p, _ in pairs) / n
    # Least-squares reliability line win = a + b * p (perfect calibration: a = 0, b = 1).
    slope = sum((p - mean_p) * (y - base) for p, y in pairs) / n / var_p if var_p else None
    intercept = base - slope * mean_p if slope is not None else None
    brier = sum((p - y) ** 2 for p, y in pairs) / n
    clim = sum((base - y) ** 2 for _, y in pairs) / n
    log_loss = -sum(y * math.log(p) + (1 - y) * math.log(1 - p) for p, y in pairs) / n
    return {'n': n, 'bins': table, 'brier': brier, 'log_loss': log_loss, 'climatology_brier': clim,
            'brier_skill_score': 1 - brier / clim if clim else None, 'base_rate': base, 'mean_p': mean_p,
            'reliability_slope': slope, 'reliability_intercept': intercept}
