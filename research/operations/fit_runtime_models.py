"""Fit every runtime engine on the standardised archive with rolling-origin splits and publish build receipts (ML-03).

  python -B -m research.operations.fit_runtime_models run [--only nhl,nba] [--test-seasons 2] [--sample 150] [--out DIR]
  python -B -m research.operations.fit_runtime_models verify [--out DIR]

For each engine: the declared population (regular-season games of one competition from `Previous Sports Results`, read through
`research.src.archive_std`), a point-in-time rolling origin, and an untouched evaluation against the population baseline.

Point in time. A game is predicted by an engine fitted ONLY on games dated before the first day of that game's month
(`known_at` = the end of each earlier game's calendar day), refitted every month. No same-month result can reach a
prediction, and the earlier seasons are the only warm-up. Teams unseen in training get the explicit league-average policy
and are counted in the receipt.

Evaluation. Three contracts per game, all priced from the engine's one score distribution: home win, total over the train-median
half-line, and home cover of the train-median-margin half-line. The population baseline is the training frequency of each event.
Reported per contract: Brier and log loss for engine and baseline, their difference with a week-block bootstrap 95% interval, and
the Cox calibration slope with its interval. Test games are evenly spaced samples (deterministic) because the structure-calibrated
engines cost 0.1-1 s per distinct matchup.

Engines the archive cannot support (tennis serve statistics, cricket ball-by-ball) get an explicit NOT_FITTED receipt with the reason.
Receipts live in research/model_builds/runtime_h0/; model artifacts are JSON with a model card (no pickle).
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import platform
import sys
import time
from collections import Counter
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Callable

import numpy as np

from research.src import archive_std

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'research/model_builds/runtime_h0'
SCHEMA = 'runtime-h0-receipt-1'
EPL_RESULTS = ROOT / 'research/data/processed/league_csv/epl_results.csv'
MAX_TRAIN_SEASONS = 5
MIN_TRAIN_GAMES = 200


@dataclass(frozen=True)
class Spec:
    key: str
    sport_dir: str
    competition: str
    profile: tuple[str, str] | None
    engine_name: str
    endpoint: str | None
    factory: Callable[[Any], Any]
    record: Callable[[archive_std.StdEvent], dict | None]
    context: Callable[[archive_std.StdEvent], dict]
    line_step: float = 1.0                     # lines are chosen on this lattice at half-points


def _teams(e: archive_std.StdEvent) -> dict:
    return {'home_team': e.home, 'away_team': e.away}


def _score_record(e: archive_std.StdEvent) -> dict | None:
    return {'home_team': e.home, 'away_team': e.away, 'home_score': e.home_score, 'away_score': e.away_score, 'date': e.date}


def _goals_record(e: archive_std.StdEvent) -> dict | None:
    return {'home_team': e.home, 'away_team': e.away, 'home_goals': e.home_score, 'away_goals': e.away_score, 'date': e.date}


def _runs_record(e: archive_std.StdEvent) -> dict | None:
    return {'home_team': e.home, 'away_team': e.away, 'home_runs': e.home_score, 'away_runs': e.away_score, 'date': e.date}


def _nrl_record(e: archive_std.StdEvent) -> dict | None:
    if None in (e.home_tries, e.away_tries, e.home_goals, e.away_goals):
        return None
    return {'home_team': e.home, 'away_team': e.away, 'home_tries': e.home_tries, 'away_tries': e.away_tries, 'home_goals': e.home_goals,
            'away_goals': e.away_goals, 'home_score': e.home_score, 'away_score': e.away_score, 'date': e.date}


def _afl_record(e: archive_std.StdEvent) -> dict | None:
    if None in (e.home_goals, e.away_goals, e.home_behinds, e.away_behinds):
        return None
    return {'home_team': e.home, 'away_team': e.away, 'home_goals': e.home_goals, 'away_goals': e.away_goals,
            'home_behinds': e.home_behinds, 'away_behinds': e.away_behinds, 'date': e.date}


def specs() -> dict[str, Spec]:
    from runtime.src.sports.afl.engine import AFLEngine
    from runtime.src.sports.baseball.engine import BaseballEngine
    from runtime.src.sports.basketball.engine import BasketballEngine
    from runtime.src.sports.nfl.engine import NFLEngine
    from runtime.src.sports.nhl.engine import HockeyLateGame, NHLEngine
    from runtime.src.sports.nrl.engine import NRLEngine
    from runtime.src.sports.soccer.engine import SoccerEngine
    avg = 'league_average'
    return {
        'nhl': Spec('nhl', 'Ice Hockey', 'NHL', ('ice_hockey', 'NHL'), 'NHLEngine', 'full_game',
                    lambda p: NHLEngine(league=p, late_game=HockeyLateGame.ILLUSTRATIVE, unknown_team_policy=avg), _goals_record, _teams, 1.0),
        'nba': Spec('nba', 'Basketball', 'NBA', ('basketball', 'NBA'), 'BasketballEngine', 'full_game',
                    lambda p: BasketballEngine(league=p, unknown_team_policy=avg), _score_record, _teams, 1.0),
        'mlb': Spec('mlb', 'Baseball', 'MLB', ('baseball', 'MLB'), 'BaseballEngine', 'full_game',
                    lambda p: BaseballEngine(league=p, unknown_team_policy=avg), _runs_record, _teams, 1.0),
        'nfl': Spec('nfl', 'American Football', 'NFL', ('american_football', 'NFL'), 'NFLEngine', None,
                    lambda p: NFLEngine(league=p, unknown_team_policy=avg), _score_record, _teams, 1.0),
        'nrl': Spec('nrl', 'Rugby League', 'NRL', ('rugby_league', 'NRL'), 'NRLEngine', None,
                    lambda p: NRLEngine(league=p, unknown_team_policy=avg), _nrl_record, _teams, 1.0),
        'afl': Spec('afl', 'AFL', 'AFL', ('afl', 'AFL'), 'AFLEngine', None,
                    lambda p: AFLEngine(league=p, unknown_team_policy=avg), _afl_record, _teams, 1.0),
        'epl': Spec('epl', 'Soccer', 'EPL', None, 'SoccerEngine', 'regulation',
                    lambda p: SoccerEngine(unknown_team_policy=avg), _goals_record, _teams, 1.0),
    }


NOT_FITTED = {
    'tennis': ('TennisEngine', 'The archive holds match results only; the engine needs serve-point and return-point counts per player. '
               'Fit it from Sackmann-format match statistics (SRC-01 ATP/WTA adapter) with `TennisEngine.fit`, then `calibrate_form_sigma` '
               'on the population deciding-set rate.'),
    'cricket': ('CricketEngine', 'The archive holds scorecards, not ball-by-ball phase data; the engine needs per-phase run and wicket rates. '
                'Fit `CricketFormat` rates from Cricsheet ball-by-ball (research/src/download_cricsheet_odi.py) before any cricket row is priced.'),
}


# ----------------------------------------------------------------------------- data
def load_epl(path: Path = EPL_RESULTS) -> list[archive_std.StdEvent]:
    events: list[archive_std.StdEvent] = []
    if not Path(path).exists():
        return events
    with Path(path).open(newline='', encoding='utf-8') as handle:
        for row in csv.DictReader(handle):
            if row['home_score'] == '' or row['away_score'] == '' or row['endpoint'] != 'REGULATION':
                continue
            day = row['scheduled_start_utc'][:10]
            events.append(archive_std.StdEvent(sport='Soccer', competition='EPL', season_year=int(row['season'][:4]) + 1, date=day, stage='regular',
                                               home=row['home'], away=row['away'], home_score=int(row['home_score']), away_score=int(row['away_score']),
                                               origin_path=EPL_RESULTS.relative_to(ROOT).as_posix(), origin_line=0))
    return events


def load_events(spec: Spec, archive_root: Path = archive_std.ARCHIVE_ROOT) -> list[archive_std.StdEvent]:
    if spec.key == 'epl':
        events = load_epl()
    else:
        events = list(archive_std.iter_events(archive_root, sport=spec.sport_dir, competition=spec.competition, stages={'regular'}))
    seen, out = set(), []
    for e in sorted(events, key=lambda e: (e.date, e.home, e.away)):
        key = (e.date, e.home, e.away)
        if key in seen:                                  # duplicated rows carry no extra information and would double-count
            continue
        seen.add(key)
        out.append(e)
    return out


def sha256_file(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


# -------------------------------------------------------------------------- metrics
def _log_loss(y: np.ndarray, p: np.ndarray) -> float:
    p = np.clip(p, 1e-6, 1 - 1e-6)
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))


def contract_metrics(y: np.ndarray, p_engine: np.ndarray, p_base: np.ndarray, blocks: np.ndarray, n_resamples: int = 600) -> dict:
    from runtime.src.common.errors import FitFailed
    from runtime.src.common.uncertainty import block_bootstrap, cox_calibration, percentile_interval
    n = len(y)
    if n < 30 or len(set(blocks.tolist())) < 8:
        return {'n': int(n), 'status': 'INSUFFICIENT_HOLDOUT'}
    brier = lambda yy, pp: float(np.mean((pp - yy) ** 2))
    d_brier = block_bootstrap(lambda yy, pe, pb: brier(yy, pe) - brier(yy, pb), (y, p_engine, p_base), blocks, n_resamples, seed=11)
    d_ll = block_bootstrap(lambda yy, pe, pb: _log_loss(yy, pe) - _log_loss(yy, pb), (y, p_engine, p_base), blocks, n_resamples, seed=12)
    out: dict[str, Any] = {'n': int(n), 'blocks': int(len(set(blocks.tolist()))), 'base_rate': float(np.mean(y)),
           'brier_engine': brier(y, p_engine), 'brier_baseline': brier(y, p_base),
           'delta_brier': brier(y, p_engine) - brier(y, p_base), 'delta_brier_ci95': list(percentile_interval(d_brier)),
           'logloss_engine': _log_loss(y, p_engine), 'logloss_baseline': _log_loss(y, p_base),
           'delta_logloss': _log_loss(y, p_engine) - _log_loss(y, p_base), 'delta_logloss_ci95': list(percentile_interval(d_ll))}
    try:
        alpha, beta = cox_calibration(y, p_engine)
        slopes = block_bootstrap(lambda yy, pe: cox_calibration(yy, pe)[1], (y, p_engine), blocks, 300, seed=13)
        out.update({'calibration_intercept': alpha, 'calibration_slope': beta, 'calibration_slope_ci95': list(percentile_interval(slopes))})
    except FitFailed as exc:
        out['calibration_error'] = exc.reason
    out['beats_baseline_brier'] = bool(out['delta_brier_ci95'][1] < 0.0)
    out['beats_baseline_logloss'] = bool(out['delta_logloss_ci95'][1] < 0.0)
    return out


def week_of(day: str) -> str:
    iso = date.fromisoformat(day).isocalendar()
    return f'{iso[0]}-W{iso[1]:02d}'


def half_line(values: np.ndarray) -> float:
    return float(np.floor(np.median(values)) + 0.5)


# -------------------------------------------------------------------------- the run
def month_start(day: str) -> str:
    return day[:7] + '-01'


def run_spec(spec: Spec, events: list[archive_std.StdEvent], test_seasons: int = 2, sample: int = 150, max_train: int = MAX_TRAIN_SEASONS,
             profile: Any = None) -> dict:
    """Rolling-origin evaluation for one engine. Returns the receipt body (without hashes of the source files)."""
    from runtime.src.common.leagues import get_profile
    started = time.time()
    seasons = sorted({e.season_year for e in events if sum(1 for x in events if x.season_year == e.season_year) >= 100})
    if len(seasons) < test_seasons + 2:
        return {'status': 'INSUFFICIENT_SEASONS', 'seasons_available': seasons}
    test_years = seasons[-test_seasons:]
    if profile is None and spec.profile is not None:
        profile = get_profile(*spec.profile)
    rows: list[dict] = []
    unknown, refits = 0, 0
    for year in test_years:
        season_events = [e for e in events if e.season_year == year]
        picks = np.unique(np.linspace(0, len(season_events) - 1, min(sample, len(season_events))).astype(int))
        chosen = {season_events[i].date + '|' + season_events[i].home + '|' + season_events[i].away for i in picks}
        months = sorted({month_start(e.date) for e in season_events})
        for month in months:
            targets = [e for e in season_events if month_start(e.date) == month and e.date + '|' + e.home + '|' + e.away in chosen]
            if not targets:
                continue
            first_year = max(1, year - max_train)
            train_events = [e for e in events if first_year <= e.season_year <= year and e.date < month]
            train = [r for r in (spec.record(e) for e in train_events) if r is not None]
            if len(train) < MIN_TRAIN_GAMES:
                continue
            if spec.key == 'epl':
                cutoff = date.fromisoformat(month)
                for r in train:
                    r['days_ago'] = (cutoff - date.fromisoformat(r['date'])).days
            engine = spec.factory(profile)
            engine.fit([{k: v for k, v in r.items() if k != 'date'} for r in train])
            refits += 1
            # population baseline lattice from the training games only
            tr_events = [e for e in events if first_year <= e.season_year <= year and e.date < month]
            tot = np.array([e.home_score + e.away_score for e in tr_events], dtype=float)
            mar = np.array([e.home_score - e.away_score for e in tr_events], dtype=float)
            line_total, line_margin = half_line(tot), half_line(mar)
            base_win = float(np.mean(mar[mar != 0] > 0))
            base_over = float(np.mean(tot > line_total))
            base_cover = float(np.mean(mar > line_margin))
            for e in targets:
                ctx = spec.context(e)
                try:
                    dist = engine.predict_distribution(ctx, spec.endpoint) if spec.endpoint else engine.predict_distribution(ctx)
                except Exception as exc:               # a failure is recorded, never silently replaced by a default
                    rows.append({'error': f'{type(exc).__name__}: {exc}'[:160]})
                    continue
                if dist.metadata.get('warnings'):
                    unknown += 1
                actual_margin = e.home_score - e.away_score
                rows.append({'date': e.date, 'week': week_of(e.date), 'p_win': dist.p_home_win(), 'p_over': dist.p_over(line_total),
                             'p_cover': dist.p_home_cover(-line_margin), 'y_win': None if actual_margin == 0 else float(actual_margin > 0),
                             'y_over': float(e.home_score + e.away_score > line_total), 'y_cover': float(actual_margin > line_margin),
                             'b_win': base_win, 'b_over': base_over, 'b_cover': base_cover, 'line_total': line_total, 'line_margin': line_margin})
    good = [r for r in rows if 'error' not in r]
    errors = Counter(r['error'] for r in rows if 'error' in r)
    metrics: dict[str, Any] = {}
    for name, label in (('win', 'home_win'), ('over', 'total_over_train_median'), ('cover', 'home_cover_train_median_margin')):
        use = [r for r in good if r[f'y_{name}'] is not None]
        if not use:
            metrics[label] = {'n': 0, 'status': 'NO_ROWS'}
            continue
        arr = lambda key: np.array([r[key] for r in use], dtype=float)
        metrics[label] = contract_metrics(arr(f'y_{name}'), np.clip(arr(f'p_{name}'), 1e-6, 1 - 1e-6), arr(f'b_{name}'), np.array([r['week'] for r in use]))
    return {'status': 'FITTED_RECEIPT', 'test_seasons': test_years, 'refits': refits, 'predictions': len(good),
            'prediction_errors': dict(errors), 'unknown_team_or_warning_rows': unknown, 'metrics': metrics,
            'lines': {'total_over': sorted({r['line_total'] for r in good})[-1] if good else None},
            'seconds': round(time.time() - started, 1)}


def final_fit(spec: Spec, events: list[archive_std.StdEvent], profile: Any = None, max_train: int = MAX_TRAIN_SEASONS) -> tuple[Any, dict]:
    from runtime.src.common.leagues import get_profile
    if profile is None and spec.profile is not None:
        profile = get_profile(*spec.profile)
    last = max(e.season_year for e in events)
    train_events = [e for e in events if e.season_year > last - max_train]
    records = [r for r in (spec.record(e) for e in train_events) if r is not None]
    if spec.key == 'epl':
        cutoff = date.fromisoformat(max(e.date for e in train_events)) + timedelta(days=1)
        for r in records:
            r['days_ago'] = (cutoff - date.fromisoformat(r['date'])).days
    engine = spec.factory(profile)
    engine.fit([{k: v for k, v in r.items() if k != 'date'} for r in records])
    return engine, {'games': len(records), 'first_date': min(e.date for e in train_events), 'last_date': max(e.date for e in train_events)}


ENGINE_MODULES = {'nhl': 'nhl', 'nba': 'basketball', 'mlb': 'baseball', 'nfl': 'nfl', 'nrl': 'nrl', 'afl': 'afl', 'epl': 'soccer'}


def code_sha(spec: Spec) -> str:
    """SHA-256 over the engine module source and this module's source (what produced the receipt)."""
    import inspect
    from importlib import import_module
    digest = hashlib.sha256()
    for module in (import_module(f'runtime.src.sports.{ENGINE_MODULES[spec.key]}.engine'), sys.modules[__name__]):
        digest.update(inspect.getsource(module).encode('utf-8'))
    return digest.hexdigest()


def build(spec: Spec, out: Path, test_seasons: int, sample: int, archive_root: Path = archive_std.ARCHIVE_ROOT) -> dict:
    from runtime.src.common import artifacts
    events = load_events(spec, archive_root)
    result = run_spec(spec, events, test_seasons, sample)
    receipt: dict[str, Any] = {'schema': SCHEMA, 'engine': spec.engine_name, 'key': spec.key, 'sport_dir': spec.sport_dir, 'competition': spec.competition,
                               'population': 'regular-season games, de-duplicated by (date, home, away)', 'events_loaded': len(events), **result}
    if result['status'] != 'FITTED_RECEIPT':
        receipt['reason'] = 'fewer than test_seasons + 2 seasons with at least 100 games'
    else:
        files = sorted({e.origin_path for e in events if e.origin_path})
        receipt['data'] = {'files': len(files), 'seasons': [min(e.season_year for e in events), max(e.season_year for e in events)],
                           'files_sha256': hashlib.sha256('\n'.join(f'{f}:{sha256_file(ROOT / f)}' for f in files if (ROOT / f).exists()).encode()).hexdigest()}
        engine, info = final_fit(spec, events)
        receipt['final_fit'] = info
        receipt['code_sha256'] = code_sha(spec)
        receipt['environment'] = {'python': platform.python_version(), 'numpy': np.__version__}
        out.mkdir(parents=True, exist_ok=True)
        artifacts.save(engine, str(out / f'{spec.key}.model.json'),
                       {'data_sha256': receipt['data']['files_sha256'], 'code_sha256': receipt['code_sha256'],
                        'metrics': {k: {m: v.get(m) for m in ('n', 'delta_brier', 'delta_brier_ci95', 'calibration_slope')} for k, v in receipt['metrics'].items()},
                        'date_range': [info['first_date'], info['last_date']], 'notes': f'{spec.engine_name} fitted on the last {MAX_TRAIN_SEASONS} seasons; see receipt'})
        receipt['artifact'] = f'{spec.key}.model.json'
    out.mkdir(parents=True, exist_ok=True)
    (out / f'{spec.key}.receipt.json').write_text(json.dumps(receipt, indent=1, sort_keys=True, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
    return receipt


def write_index(out: Path) -> dict:
    index: dict[str, Any] = {'schema': 'runtime-h0-index-1', 'receipts': {}, 'not_fitted': {k: {'engine': e, 'reason': r} for k, (e, r) in NOT_FITTED.items()}}
    for path in sorted(out.glob('*.receipt.json')):
        r = json.loads(path.read_text(encoding='utf-8'))
        wins = {k: v.get('beats_baseline_brier') for k, v in r.get('metrics', {}).items()}
        index['receipts'][r['key']] = {'engine': r['engine'], 'status': r['status'], 'test_seasons': r.get('test_seasons'), 'predictions': r.get('predictions'),
                                       'beats_baseline_brier': wins, 'receipt_sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
    (out / 'INDEX.json').write_text(json.dumps(index, indent=1, sort_keys=True) + '\n', encoding='utf-8', newline='\n')
    return index


def verify(out: Path = OUT) -> list[str]:
    """Every runtime engine has either a fitted receipt (hashes intact, artifact loadable) or an explicit NOT_FITTED reason."""
    from runtime.src.common import artifacts
    problems = []
    index_path = out / 'INDEX.json'
    if not index_path.exists():
        return [f'{index_path} is missing; run `fit_runtime_models run`']
    index = json.loads(index_path.read_text(encoding='utf-8'))
    wanted = set(specs()) | set(NOT_FITTED)
    covered = set(index['receipts']) | set(index['not_fitted'])
    if wanted - covered:
        problems.append(f'engines without a receipt or NOT_FITTED reason: {sorted(wanted - covered)}')
    for key, entry in index['receipts'].items():
        path = out / f'{key}.receipt.json'
        if not path.exists() or hashlib.sha256(path.read_bytes()).hexdigest() != entry['receipt_sha256']:
            problems.append(f'{key}: receipt missing or changed since the index was written')
            continue
        receipt = json.loads(path.read_text(encoding='utf-8'))
        if receipt['status'] == 'FITTED_RECEIPT':
            try:
                artifacts.load(str(out / receipt['artifact']))
            except Exception as exc:  # noqa: BLE001
                problems.append(f'{key}: artifact does not load: {exc}')
    return problems


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    r = sub.add_parser('run')
    r.add_argument('--only')
    r.add_argument('--test-seasons', type=int, default=2)
    r.add_argument('--sample', type=int, default=150)
    r.add_argument('--out', type=Path, default=OUT)
    v = sub.add_parser('verify')
    v.add_argument('--out', type=Path, default=OUT)
    args = parser.parse_args(argv)
    if args.command == 'verify':
        problems = verify(args.out)
        print(json.dumps({'passed': not problems, 'problems': problems}, indent=1))
        return 1 if problems else 0
    chosen = set(args.only.split(',')) if args.only else set(specs())
    for key, spec in specs().items():
        if key in chosen:
            receipt = build(spec, args.out, args.test_seasons, args.sample)
            brief = {k: v.get('delta_brier') for k, v in receipt.get('metrics', {}).items()}
            print(json.dumps({'key': key, 'status': receipt['status'], 'predictions': receipt.get('predictions'), 'delta_brier': brief, 'seconds': receipt.get('seconds')}), flush=True)
    write_index(args.out)
    return 0


if __name__ == '__main__':
    sys.exit(main())
