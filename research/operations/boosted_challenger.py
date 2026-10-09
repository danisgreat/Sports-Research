"""Boosted distribution-parameter challenger against the team-strength engine baseline (ML-06).

  python -B -m research.operations.boosted_challenger run [--only nhl,nba,epl] [--sample 150] [--out DIR]
  python -B -m research.operations.boosted_challenger verify [--out DIR]

The challenger (`runtime.src.common.boosting`) predicts the PARAMETERS of the score distribution from point-in-time H0 features
(`research.src.h0_features`): Poisson rates for goal sports, a Gaussian mean plus a heteroscedastic total width for points. The
SAME engine then builds the score grid from those parameters, so contracts stay coherent and the only thing that differs from the
baseline is how the expected values were obtained. The baseline is the engine fitted with ridge team strengths
(`fit_runtime_models`).

Both are scored on identical test games, refitted every month on games dated before the month (rolling origin). Metrics, paired:
winner log loss and the CRPS of the total-score distribution (both lower is better), with a week-block bootstrap 95% interval of the
difference (challenger minus baseline). A challenger "beats" the baseline on a metric only if that interval lies below zero.
The receipt reports the measured result whatever it is; the acceptance bar (beat the baseline on both metrics in at least two
sports) is evaluated in `INDEX.json`, not assumed.
"""
from __future__ import annotations
import argparse
import json
import sys
import time
from datetime import date
from pathlib import Path
from typing import Any

import numpy as np

from research.operations import fit_runtime_models as h0
from research.src import h0_features

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'research/model_builds/runtime_h0/challenger'
SCHEMA = 'boosted-challenger-receipt-1'
SUPPORTED = ('nhl', 'nba', 'epl', 'mlb')
POISSON_SPORTS = {'nhl', 'epl', 'mlb'}
BOOST_PARAMS: dict[str, Any] = dict(n_estimators=250, learning_rate=0.05, max_depth=3, min_leaf=60, l2=10.0, subsample=0.8, patience=25)


def total_pmf(dist) -> np.ndarray:
    grid = dist.grid
    h = np.asarray(dist.home_support, dtype=int)[:, None]
    a = np.asarray(dist.away_support, dtype=int)[None, :]
    out = np.zeros(int(h.max() + a.max()) + 1)
    np.add.at(out, (h + a).ravel(), grid.ravel())
    return out


def crps_total(dist, actual_total: int) -> float:
    """Discrete CRPS of the total-score distribution: sum over t of (F(t) - 1{actual <= t})^2."""
    pmf = total_pmf(dist)
    cdf = np.cumsum(pmf)
    t = np.arange(len(pmf))
    horizon = max(len(pmf), actual_total + 1)
    if horizon > len(pmf):
        cdf = np.concatenate([cdf, np.ones(horizon - len(pmf))])
        t = np.arange(horizon)
    return float(np.sum((cdf - (t >= actual_total)) ** 2))


def _paired(delta: np.ndarray, blocks: np.ndarray, resamples: int = 600) -> dict:
    from runtime.src.common.uncertainty import block_bootstrap, percentile_interval
    boot = block_bootstrap(lambda d: float(np.mean(d)), (delta,), blocks, resamples, seed=21)
    lo, hi = percentile_interval(boot)
    return {'mean_difference': float(np.mean(delta)), 'ci95': [lo, hi], 'challenger_better': bool(hi < 0.0), 'n': int(len(delta))}


def parameters(key: str, models: dict, X: np.ndarray) -> dict:
    """Challenger parameters for the feature rows X."""
    if key in POISSON_SPORTS:
        return {'home': models['home'].predict(X), 'away': models['away'].predict(X)}
    mu_h, mu_a = models['home'].predict(X), models['away'].predict(X)
    return {'home': mu_h, 'away': mu_a, 'total_sd': models['width'].predict_sd(X)}


def fit_models(key: str, X: np.ndarray, y_home: np.ndarray, y_away: np.ndarray, seed: int = 0) -> dict:
    from runtime.src.common.boosting import GaussianBoost, LogVarianceBoost, PoissonBoost
    if key in POISSON_SPORTS:
        poisson_home, poisson_away = PoissonBoost(**BOOST_PARAMS, seed=seed), PoissonBoost(**BOOST_PARAMS, seed=seed)
        poisson_home.fit(X, y_home)
        poisson_away.fit(X, y_away)
        return {'home': poisson_home, 'away': poisson_away}
    home, away, width = GaussianBoost(**BOOST_PARAMS, seed=seed), GaussianBoost(**BOOST_PARAMS, seed=seed), LogVarianceBoost(**BOOST_PARAMS, seed=seed)
    home.fit(X, y_home)
    away.fit(X, y_away)
    resid = ((y_home + y_away) - (home.predict(X) + away.predict(X))) ** 2
    width.fit(X, resid)
    return {'home': home, 'away': away, 'width': width}


def challenger_context(key: str, params: dict, i: int, baseline_engine: Any) -> dict:
    if key == 'nhl':
        return {'home_xg': float(params['home'][i]), 'away_xg': float(params['away'][i])}
    if key == 'epl':
        rho = float(getattr(baseline_engine.dixon_coles, 'rho', -0.05))
        return {'home_xg': float(params['home'][i]), 'away_xg': float(params['away'][i]), 'dixon_coles_rho': rho}
    if key == 'mlb':
        return {'home_expected_runs': float(params['home'][i]), 'away_expected_runs': float(params['away'][i])}
    return {'home_expected_points': float(params['home'][i]), 'away_expected_points': float(params['away'][i]),
            'total_sd': float(np.clip(params['total_sd'][i], 8.0, 40.0))}


def run_sport(key: str, events: list, test_seasons: int = 2, sample: int = 150, max_train: int = h0.MAX_TRAIN_SEASONS) -> dict:
    spec = h0.specs()[key]
    from runtime.src.common.leagues import get_profile
    started = time.time()
    profile = get_profile(*spec.profile) if spec.profile else None
    seasons = sorted({e.season_year for e in events if sum(1 for x in events if x.season_year == e.season_year) >= 100})
    if len(seasons) < test_seasons + 2:
        return {'status': 'INSUFFICIENT_SEASONS', 'seasons_available': seasons}
    rows = h0_features.build_rows(events)
    index = {(r['date'], r['home'], r['away']): i for i, r in enumerate(rows)}
    X_all = h0_features.matrix(rows)
    out_rows: list[dict] = []
    refits = 0
    for year in seasons[-test_seasons:]:
        season_events = [e for e in events if e.season_year == year]
        picks = np.unique(np.linspace(0, len(season_events) - 1, min(sample, len(season_events))).astype(int))
        chosen = {(season_events[i].date, season_events[i].home, season_events[i].away) for i in picks}
        for month in sorted({h0.month_start(e.date) for e in season_events}):
            targets = [e for e in season_events if h0.month_start(e.date) == month and (e.date, e.home, e.away) in chosen]
            if not targets:
                continue
            first_year = max(1, year - max_train)
            train = [e for e in events if first_year <= e.season_year <= year and e.date < month]
            if len(train) < h0.MIN_TRAIN_GAMES:
                continue
            tr_idx = [index[(e.date, e.home, e.away)] for e in train]
            baseline = spec.factory(profile)
            recs = [r for r in (spec.record(e) for e in train) if r is not None]
            if key == 'epl':
                cutoff = date.fromisoformat(month)
                for r in recs:
                    r['days_ago'] = (cutoff - date.fromisoformat(r['date'])).days
            baseline.fit([{k: v for k, v in r.items() if k != 'date'} for r in recs])
            Xtr = X_all[tr_idx]
            models = fit_models(key, Xtr, np.array([e.home_score for e in train], dtype=float), np.array([e.away_score for e in train], dtype=float))
            refits += 1
            t_idx = [index[(e.date, e.home, e.away)] for e in targets]
            params = parameters(key, models, X_all[t_idx])
            tot = np.array([e.home_score + e.away_score for e in train], dtype=float)
            for k, e in enumerate(targets):
                if e.home_score == e.away_score:
                    continue
                try:
                    base_dist = baseline.predict_distribution(spec.context(e), spec.endpoint) if spec.endpoint else baseline.predict_distribution(spec.context(e))
                    ctx = challenger_context(key, params, k, baseline)
                    chal_dist = baseline.predict_distribution(ctx, spec.endpoint) if spec.endpoint else baseline.predict_distribution(ctx)
                except Exception as exc:                 # recorded, never replaced by a default
                    out_rows.append({'error': f'{type(exc).__name__}: {exc}'[:160]})
                    continue
                y = float(e.home_score > e.away_score)
                actual_total = int(e.home_score + e.away_score)
                pb, pc = np.clip(base_dist.p_home_win(), 1e-6, 1 - 1e-6), np.clip(chal_dist.p_home_win(), 1e-6, 1 - 1e-6)
                out_rows.append({'week': h0.week_of(e.date), 'y': y, 'll_base': -(y * np.log(pb) + (1 - y) * np.log(1 - pb)),
                                 'll_chal': -(y * np.log(pc) + (1 - y) * np.log(1 - pc)), 'crps_base': crps_total(base_dist, actual_total),
                                 'crps_chal': crps_total(chal_dist, actual_total), 'mean_total_pred_base': float(sum(base_dist.expected_scores())),
                                 'mean_total_pred_chal': float(sum(chal_dist.expected_scores())), 'actual_total': actual_total, 'train_mean_total': float(tot.mean())})
    good = [r for r in out_rows if 'error' not in r]
    errors = [r['error'] for r in out_rows if 'error' in r]
    if len(good) < 40:
        return {'status': 'INSUFFICIENT_HOLDOUT', 'predictions': len(good), 'errors': errors[:3]}
    blocks = np.array([r['week'] for r in good])
    ll = _paired(np.array([r['ll_chal'] - r['ll_base'] for r in good]), blocks)
    crps = _paired(np.array([r['crps_chal'] - r['crps_base'] for r in good]), blocks)
    return {'status': 'MEASURED', 'predictions': len(good), 'prediction_errors': len(errors), 'refits': refits,
            'test_seasons': seasons[-test_seasons:], 'features': h0_features.FEATURES,
            'winner_log_loss': {**ll, 'baseline': float(np.mean([r['ll_base'] for r in good])), 'challenger': float(np.mean([r['ll_chal'] for r in good]))},
            'total_crps': {**crps, 'baseline': float(np.mean([r['crps_base'] for r in good])), 'challenger': float(np.mean([r['crps_chal'] for r in good]))},
            'beats_baseline_on_both': bool(ll['challenger_better'] and crps['challenger_better']),
            'total_bias': {'baseline': float(np.mean([r['mean_total_pred_base'] - r['actual_total'] for r in good])),
                           'challenger': float(np.mean([r['mean_total_pred_chal'] - r['actual_total'] for r in good]))},
            'seconds': round(time.time() - started, 1)}


def write_index(out: Path) -> dict:
    index: dict[str, Any] = {'schema': 'boosted-challenger-index-1', 'sports': {}}
    for path in sorted(out.glob('*.challenger.json')):
        r = json.loads(path.read_text(encoding='utf-8'))
        index['sports'][r['key']] = {'status': r['status'], 'beats_baseline_on_both': r.get('beats_baseline_on_both'),
                                     'winner_log_loss_diff': r.get('winner_log_loss', {}).get('mean_difference'),
                                     'total_crps_diff': r.get('total_crps', {}).get('mean_difference')}
    winners = [k for k, v in index['sports'].items() if v.get('beats_baseline_on_both')]
    index['acceptance'] = {'criterion': 'challenger beats the engine baseline on winner log loss AND total CRPS (95% block-bootstrap interval below 0) in >= 2 sports',
                           'sports_beaten': winners, 'met': len(winners) >= 2}
    (out / 'INDEX.json').write_text(json.dumps(index, indent=1, sort_keys=True) + '\n', encoding='utf-8', newline='\n')
    return index


def verify(out: Path = OUT) -> list[str]:
    path = out / 'INDEX.json'
    if not path.exists():
        return [f'{path} missing; run `boosted_challenger run`']
    index = json.loads(path.read_text(encoding='utf-8'))
    problems = []
    for key in index['sports']:
        if not (out / f'{key}.challenger.json').exists():
            problems.append(f'{key}: receipt missing')
    if len(index['sports']) < 2:
        problems.append('fewer than two sports measured')
    return problems


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    r = sub.add_parser('run')
    r.add_argument('--only')
    r.add_argument('--sample', type=int, default=150)
    r.add_argument('--test-seasons', type=int, default=2)
    r.add_argument('--out', type=Path, default=OUT)
    v = sub.add_parser('verify')
    v.add_argument('--out', type=Path, default=OUT)
    args = parser.parse_args(argv)
    if args.command == 'verify':
        problems = verify(args.out)
        print(json.dumps({'passed': not problems, 'problems': problems}, indent=1))
        return 1 if problems else 0
    chosen = set(args.only.split(',')) if args.only else set(SUPPORTED)
    args.out.mkdir(parents=True, exist_ok=True)
    for key in SUPPORTED:
        if key not in chosen:
            continue
        spec = h0.specs()[key]
        result = run_sport(key, h0.load_events(spec), args.test_seasons, args.sample)
        receipt = {'schema': SCHEMA, 'key': key, 'engine': spec.engine_name, 'competition': spec.competition, **result}
        (args.out / f'{key}.challenger.json').write_text(json.dumps(receipt, indent=1, sort_keys=True, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
        print(json.dumps({'key': key, 'status': result['status'], 'logloss': result.get('winner_log_loss', {}).get('mean_difference'),
                          'crps': result.get('total_crps', {}).get('mean_difference'), 'seconds': result.get('seconds')}), flush=True)
    write_index(args.out)
    return 0


if __name__ == '__main__':
    sys.exit(main())
