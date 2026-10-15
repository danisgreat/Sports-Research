"""Executable primary integration: fit -> bandit action -> coherent rows -> delayed feedback."""
from dataclasses import replace
import copy

import numpy as np
import pytest

from ml.config import League
from ml.primary import (ARMS, AdmissionError, admit_history, csv_bytes, digest, forecast,
                        probabilities, read_rows, settle, verify_bundle)
from ml.tests.test_models import synthetic


@pytest.fixture
def inputs(tmp_path):
    capture = tmp_path / "capture.txt"
    capture.write_text("EXAMPLE synthetic fixture, not sporting evidence", encoding="utf-8")
    frame, _, _ = synthetic(n_teams=6, kind="normal")
    lg = League("Basketball/EXAMPLE", "Basketball", "EXAMPLE", "EXAMPLE", "gaussian",
                endpoint="FULL_GAME_INCL_OT", tie_rule="overtime", extra_fraction=5/40)
    history = []
    for row in frame.to_dict("records"):
        date = row["date"].tz_localize("UTC")
        history.append(dict(event_id=row["event_id"], competition=lg.path, endpoint=lg.endpoint,
                            date=date.isoformat(), final_at=(date + __import__('pandas').Timedelta(hours=1)).isoformat(),
                            available_at=(date + __import__('pandas').Timedelta(hours=2)).isoformat(),
                            status="FINAL", admission="RESEARCH_INPUT_REVIEWED", source_url="https://example.org/synthetic",
                            evidence_path=str(capture), evidence_sha256=digest(capture.read_bytes()),
                            **{k: row[k] for k in ("season", "home", "away", "hs", "as_", "reg_hs", "reg_as", "decision")}))
    request = dict(event_id="EXAMPLE-PRIMARY-1", competition=lg.path, endpoint=lg.endpoint,
                   home="T00", away="T01", cutoff="2023-01-01T00:00:00Z", issue_at="2023-01-01T10:00:00Z",
                   actual_start="2023-01-01T11:00:00Z", outcome_exposure="NONE_RECORDED", candidate_recipe="EXAMPLE_TOTAL_200_5")
    contracts = [dict(contract_key="TOTAL-U", family="total", side="UNDER", line="200.5", endpoint=lg.endpoint,
                      definition="FROZEN_FRAMEWORK_CONVENTION", action="STANDARD_COMPLETED"),
                 dict(contract_key="TOTAL-O", family="total", side="OVER", line="200.5", endpoint=lg.endpoint,
                      definition="FROZEN_FRAMEWORK_CONVENTION", action="STANDARD_COMPLETED")]
    return request, lg, history, contracts, tmp_path, capture


def run(inputs, name="bundle", **kwargs):
    req, lg, history, contracts, tmp, _ = inputs
    return forecast(req, lg, history, contracts, tmp/name, rng=np.random.default_rng(19), **kwargs)


def test_fit_primary_and_delayed_bandit_feedback(inputs):
    rec = run(inputs)
    assert rec['selected_arm'] in ARMS
    assert rec['behaviour_probability'] == pytest.approx(1/3)
    assert '|FULL20|' in rec['context']
    folder = inputs[4]/'bundle'
    predictions = read_rows(folder/'PREDICTIONS.csv')
    assert sum(float(r['p_card']) for r in predictions) == pytest.approx(1)
    assert all(float(r['win']) + float(r['push']) + float(r['loss']) == pytest.approx(1) for r in predictions)
    capture = inputs[5]
    feedback = settle(folder, 110, 95, '2023-01-01T13:00:00Z', '2023-01-01T14:00:00Z', capture, digest(capture.read_bytes()))
    assert feedback is not None
    cold = probabilities([feedback], rec['context'], '2023-01-01T12:00:00Z')
    assert cold == pytest.approx(np.full(3, 1/3))
    learned = probabilities([feedback], rec['context'], '2023-01-02T00:00:00Z')
    assert learned[list(ARMS).index(rec['selected_arm'])] > 1/3
    with pytest.raises(AdmissionError, match='duplicate'):
        probabilities([feedback, feedback], rec['context'], '2024-01-01T00:00:00Z')
    feedback['reward'] = 0
    with pytest.raises(AdmissionError, match='reward differs'):
        probabilities([feedback], rec['context'], '2024-01-01T00:00:00Z')


@pytest.mark.parametrize('engine,sport', [('dixon_coles','Soccer'), ('count','Baseball'), ('gaussian','Rugby Union'), ('cricket','Cricket T20')])
def test_supported_model_routes(inputs, engine, sport):
    req, lg, history, contracts, tmp, _ = copy.deepcopy(inputs)
    lg = replace(lg, engine=engine, sport=sport, tie_rule='draw', endpoint='FIRST_INNINGS_FULL_LENGTH' if engine=='cricket' else 'REGULATION', overs_cap=20 if engine=='cricket' else None)
    req['endpoint'] = lg.endpoint
    sampled, _, _ = synthetic(n_teams=6, kind="poisson")
    for n, row in enumerate(history):
        row['endpoint'] = lg.endpoint
        if engine in ('count','dixon_coles'):
            row['hs'] = row['reg_hs'] = int(sampled.iloc[n].hs)
            row['as_'] = row['reg_as'] = int(sampled.iloc[n].as_)
        if engine=='cricket':
            row.update(bat=row['home'], bowl=row['away'], venue='V', runs=row['hs'], legal_balls='120', wickets='5',
                       as_=0, reg_as=0)
    for row in contracts:
        row['endpoint'] = lg.endpoint
        if engine in ('count','dixon_coles'):row['line']='4.5'
    req['venue'] = 'V'
    result = forecast(req, lg, history, contracts, tmp/engine, rng=np.random.default_rng(7))
    assert result['training_rows'] == len(history)
    assert verify_bundle(tmp/engine)['selected_arm'] in ARMS


@pytest.mark.parametrize('defect', ['future','target','duplicate','hash','scope','nonterminal','negative','same_day','endpoint'])
def test_bad_history_never_issues(inputs, defect):
    req, lg, history, contracts, tmp, _ = copy.deepcopy(inputs)
    if defect=='future':history[0]['available_at']='2030-01-01T00:00:00Z'
    if defect=='target':history[0]['event_id']=req['event_id']
    if defect=='duplicate':history.append(history[0])
    if defect=='hash':history[0]['evidence_sha256']='0'*64
    if defect=='scope':history[0]['competition']='Other/League'
    if defect=='nonterminal':history[0]['status']='LIVE'
    if defect=='negative':history[0]['hs']=-1
    if defect=='same_day':history[0].update(date=req['cutoff'], final_at=req['cutoff'], available_at=req['cutoff'])
    if defect=='endpoint':history[0]['endpoint']='HALFTIME'
    with pytest.raises(AdmissionError):forecast(req, lg, history, contracts, tmp/defect)
    assert not (tmp/defect).exists()


@pytest.mark.parametrize('defect', ['duplicate_key','duplicate_semantics','phase','nan','exposure','data_hold','unsupported','unknown_team'])
def test_rejects_scope_contract_and_source_failures(inputs, defect):
    req, lg, history, contracts, tmp, _ = copy.deepcopy(inputs)
    if defect=='duplicate_key':contracts.append(contracts[0])
    if defect=='duplicate_semantics':contracts.append(dict(contracts[0], contract_key='ANOTHER'))
    if defect=='phase':contracts[0]['endpoint']='POWERPLAY_6'
    if defect=='nan':contracts[0]['line']='nan'
    if defect=='exposure':req['outcome_exposure']='LIVE_SCORE_SEEN'
    if defect=='data_hold':lg=replace(lg, data_warnings=('UNKNOWN_LABELS',))
    if defect=='unsupported':lg=replace(lg, engine='unsupported')
    if defect=='unknown_team':req['home']='UNSEEN'
    with pytest.raises((AdmissionError, ValueError)):
        forecast(req, lg, history, contracts, tmp/defect)
    assert not (tmp/defect).exists()


def test_issued_bundle_never_overwritten_and_mutation_rejected(inputs):
    run(inputs)
    before = (inputs[4]/'bundle'/'RECEIPT.csv').read_bytes()
    with pytest.raises(AdmissionError, match='existing'):
        run(inputs)
    assert (inputs[4]/'bundle'/'RECEIPT.csv').read_bytes()==before
    (inputs[4]/'bundle'/'PREDICTIONS.csv').write_text('tampered')
    with pytest.raises(AdmissionError, match='hash mismatch'):verify_bundle(inputs[4]/'bundle')


def test_future_feedback_is_not_read_or_learned():
    row=dict(event_id='E', available_at='2030-01-01T00:00:00Z')
    assert probabilities([row], 'X', '2025-01-01T00:00:00Z') == pytest.approx([1/3]*3)


def test_unknown_market_columns_block_primary(inputs):
    req, lg, history, contracts, tmp, _ = inputs
    history[0]['closing_odds'] = '1.9'
    with pytest.raises(AdmissionError, match='unregistered input'):
        forecast(req, lg, history, contracts, tmp/'market')


def test_all_push_has_no_bandit_reward(inputs):
    req, lg, history, contracts, tmp, capture = inputs
    for r in contracts:r['line']='200'
    run(inputs)
    assert settle(tmp/'bundle', 110, 90, '2023-01-01T13:00:00Z', '2023-01-01T14:00:00Z',
                  capture, digest(capture.read_bytes())) is None


def test_baseline_checked_against_retained_grid(inputs):
    run(inputs)
    folder = inputs[4]/'bundle'
    rows = read_rows(folder/'PREDICTIONS.csv')
    rows[0]['baseline_p'] = '.123'
    (folder/'PREDICTIONS.csv').write_bytes(csv_bytes(rows))
    receipt = read_rows(folder/'RECEIPT.csv')
    receipt[0]['predictions_sha256'] = digest((folder/'PREDICTIONS.csv').read_bytes())
    (folder/'RECEIPT.csv').write_bytes(csv_bytes(receipt))
    with pytest.raises(AdmissionError, match='baseline_p differs'):
        verify_bundle(folder)


def test_primary_competition_lookup_does_not_read_unrelated_archives(tmp_path, monkeypatch):
    from ml import config
    from ml.tests.test_cross_sport_integrity import source, result
    rows = [result(**{'Game ID': str(i), 'Date': f'2025-01-0{i+1}'}) for i in range(3)]
    source(tmp_path, monkeypatch, rows)
    unrelated = tmp_path/'Soccer'/'Unrelated'/'2025'
    unrelated.mkdir(parents=True)
    (unrelated/'2025_games.csv').write_text('not even a valid source')
    monkeypatch.setattr(config, 'ARCHIVE', tmp_path)
    original = config._read_head
    def scoped_read(path, *args, **kwargs):
        assert 'Unrelated' not in str(path)
        return original(path, *args, **kwargs)
    monkeypatch.setattr(config, '_read_head', scoped_read)
    config._discover_cached.cache_clear()
    try:
        assert config.get_league('Basketball/Example').engine == 'gaussian'
        with pytest.raises(KeyError):config.get_league('Basketball/Missing')
    finally:
        config._discover_cached.cache_clear()
