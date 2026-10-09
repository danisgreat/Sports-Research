"""Quantitative regime flags (PRD-07): recover known multipliers, apply the interval rule, keep the register in sync."""
import json
from pathlib import Path

import numpy as np
import pytest

from research.operations import regimes
from research.src.archive_std import StdEvent

ROOT = Path(__file__).resolve().parents[2]


def league(finals_mult=0.90, seasons=12, regular=300, finals=40, seed=4, mean=5.5):
    rng = np.random.default_rng(seed)
    events = []
    for s in range(seasons):
        year = 2010 + s
        for stage, n, mult in (('regular', regular, 1.0), ('finals', finals, finals_mult)):
            for i in range(n):
                events.append(StdEvent(sport='Ice Hockey', competition='SYN', season_year=year, date=f'{year}-{1 + i % 12:02d}-{1 + i % 27:02d}', stage=stage,
                                       home=f'H{i % 10}', away=f'A{i % 9}', home_score=int(rng.poisson(mean / 2 * mult)), away_score=int(rng.poisson(mean / 2 * mult))))
    return events


def test_finals_multiplier_is_recovered_and_significant():
    result = regimes.finals_compression(league(0.88, finals=120))
    assert result['status'] == 'ESTIMATED' and result['seasons'] == 12
    assert result['estimate'] == pytest.approx(0.88, abs=0.06) and result['ci95'][1] < 1.0
    assert result['significant'] is True and result['recommended'] == result['estimate']


def test_a_null_effect_is_published_but_not_recommended():
    result = regimes.finals_compression(league(1.0, finals=80, seed=9))
    assert result['status'] == 'ESTIMATED' and result['ci95'][0] <= 1.0 <= result['ci95'][1]
    assert result['significant'] is False and result['recommended'] == 1.0 and result['estimate'] != 1.0


def test_too_few_seasons_is_not_estimated():
    assert regimes.finals_compression(league(seasons=3))['status'] == 'INSUFFICIENT_SEASONS'


def test_rule_change_ratio():
    events = []
    rng = np.random.default_rng(2)
    for year in range(2013, 2024):
        mean = 40.0 if year < 2020 else 46.0
        for i in range(250):
            events.append(StdEvent(sport='Rugby League', competition='SYN', season_year=year, date=f'{year}-05-{1 + i % 28:02d}', stage='regular', home='A', away='B',
                                   home_score=int(rng.normal(mean / 2, 6)), away_score=int(rng.normal(mean / 2, 6))))
    spec = {'name': 'six_again', 'effective_season': 2020, 'before': (2015, 2019), 'after': (2022, 2023), 'note': 'x'}
    result = regimes.rule_change(events, spec)
    assert result['status'] == 'INSUFFICIENT_SEASONS'                       # two post-change seasons are too few to bootstrap
    spec['after'] = (2020, 2023)
    result = regimes.rule_change(events, spec)
    assert result['status'] == 'ESTIMATED' and result['estimate'] == pytest.approx(46 / 40, abs=0.04) and result['recommended'] > 1.1


def test_early_season_flag_uses_the_first_five_games():
    result = regimes.early_season(league(1.0, seasons=8, regular=250, finals=0))
    assert result['status'] in ('ESTIMATED', 'INSUFFICIENT_SEASONS')


def test_register_block_is_spliced_idempotently_and_verify_detects_edits(tmp_path):
    register = tmp_path / 'BASE_RATES_REGISTER.md'
    register.write_text('# Register\r\n\r\nExisting text.\r\n', encoding='utf-8', newline='')
    config = tmp_path / 'regimes.json'
    data = {'schema': regimes.SCHEMA, 'method': 'm', 'archive_files': 1, 'archive_sha256': 'x', 'not_estimable': regimes.NOT_ESTIMABLE,
            'leagues': {'SYN': {'sport': 'Ice Hockey', 'FINALS_COMPRESSION': {'status': 'ESTIMATED', 'estimate': 0.9, 'ci95': [0.88, 0.93], 'seasons': 12,
                                                                                 'significant': True, 'recommended': 0.9},
                                'EARLY_SEASON': {'status': 'INSUFFICIENT_SEASONS', 'seasons': 2}}}}
    config.write_text(json.dumps(data), encoding='utf-8')
    text = register.read_text(encoding='utf-8').replace('\r\n', '\n')
    once = regimes.splice(text, regimes.render(data))
    assert regimes.splice(once, regimes.render(data)) == once and once.count(regimes.BEGIN) == 1 and 'Existing text.' in once
    register.write_text(once.replace('\n', '\r\n'), encoding='utf-8', newline='')
    assert regimes.verify(config, register) == []
    register.write_text(once.replace('0.900', '0.800').replace('\n', '\r\n'), encoding='utf-8', newline='')
    assert regimes.verify(config, register)
    data['leagues']['SYN']['FINALS_COMPRESSION']['recommended'] = 0.7
    config.write_text(json.dumps(data), encoding='utf-8')
    assert any('interval rule' in p for p in regimes.verify(config, register))


def test_published_regimes_are_consistent_and_state_what_cannot_be_measured():
    assert regimes.verify() == []
    data = json.loads(regimes.CONFIG.read_text(encoding='utf-8'))
    assert {'NRL', 'NBA', 'NHL', 'MLB', 'AFL', 'NFL'} <= set(data['leagues']) and 'RULE_CHANGE:six_again' in data['leagues']['NRL']
    assert set(data['not_estimable']) == {'RULE_CHANGE:kbl_foreign_player_2026_27', 'CUP_ROTATION'}
    assert regimes.multiplier('NRL', 'FINALS_COMPRESSION') < 1.0 and regimes.multiplier('NRL', 'NOT_A_FLAG') == 1.0 and regimes.multiplier('XXX', 'EARLY_SEASON') == 1.0
