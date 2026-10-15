"""Executable primary integration: fit -> full-information expert mixture -> coherent rows -> delayed feedback."""
from dataclasses import replace
import copy

import numpy as np
import pytest

from ml.config import League
from ml.core.distributions import ScoreGrid
from ml.primary import (ARMS, MIX_ARM, AdmissionError, admit_history, csv_bytes, digest, eta_for, feedback_losses,
                        forecast, hedge_weights, information_horizon, mix_grids, read_rows, settle, verify_bundle,
                        warm_start, warm_records, POLICY)
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
                   home="T00", away="T01", scheduled_start="2023-01-01T11:00:00Z", issue_at="2023-01-01T10:00:00Z",
                   actual_start="2023-01-01T11:00:00Z", outcome_exposure="NONE_RECORDED", candidate_recipe="EXAMPLE_TOTAL_200_5")
    contracts = [dict(contract_key="TOTAL-U", family="total", side="UNDER", line="200.5", endpoint=lg.endpoint,
                      definition="FROZEN_FRAMEWORK_CONVENTION", action="STANDARD_COMPLETED"),
                 dict(contract_key="TOTAL-O", family="total", side="OVER", line="200.5", endpoint=lg.endpoint,
                      definition="FROZEN_FRAMEWORK_CONVENTION", action="STANDARD_COMPLETED")]
    return request, lg, history, contracts, tmp_path, capture


def run(inputs, name="bundle", **kwargs):
    req, lg, history, contracts, tmp, _ = inputs
    return forecast(req, lg, history, contracts, tmp/name, rng=np.random.default_rng(19), **kwargs)


def test_mixture_primary_and_full_information_feedback(inputs):
    rec = run(inputs)
    assert rec['selected_arm'] == MIX_ARM and rec['coverage'] == 'FULL20'
    assert rec['warm_start_games'] > 0  # weights already learned from pre-cutoff history
    w = [float(x.split(':')[1]) for x in rec['mixture_weights'].split(';')]
    assert sum(w) == pytest.approx(1) and all(x >= 0 for x in w)
    folder = inputs[4]/'bundle'
    predictions = read_rows(folder/'PREDICTIONS.csv')
    assert sum(float(r['p_card']) for r in predictions) == pytest.approx(1)
    assert all(float(r['win']) + float(r['push']) + float(r['loss']) == pytest.approx(1) for r in predictions)
    capture = inputs[5]
    feedback = settle(folder, 110, 95, '2023-01-01T13:00:00Z', '2023-01-01T14:00:00Z', capture, digest(capture.read_bytes()))
    assert all(0 <= feedback['loss_' + a] <= 1 for a in ARMS)  # every expert is scored: full information
    before, n0 = feedback_losses([feedback], rec['context'], '2023-01-01T12:00:00Z')
    assert n0 == 0 and before == pytest.approx(np.zeros(3))  # not yet available: never learned
    after, n1 = feedback_losses([feedback], rec['context'], '2023-01-02T00:00:00Z')
    assert n1 == 1 and after == pytest.approx([feedback['loss_' + a] for a in ARMS])
    with pytest.raises(AdmissionError, match='duplicate'):
        feedback_losses([feedback, feedback], rec['context'], '2024-01-01T00:00:00Z')
    feedback['loss_' + ARMS[0]] = 0.0
    with pytest.raises(AdmissionError, match='loss differs'):
        feedback_losses([feedback], rec['context'], '2024-01-01T00:00:00Z')


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
    assert verify_bundle(tmp/engine)['selected_arm'] == MIX_ARM


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
    if defect=='same_day':history[0].update(date=req['issue_at'], final_at=req['issue_at'], available_at=req['issue_at'])
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
    total, n = feedback_losses([row], 'X', '2025-01-01T00:00:00Z')
    assert n == 0 and total == pytest.approx([0, 0, 0])


def test_unknown_market_columns_block_primary(inputs):
    req, lg, history, contracts, tmp, _ = inputs
    history[0]['closing_odds'] = '1.9'
    with pytest.raises(AdmissionError, match='unregistered input'):
        forecast(req, lg, history, contracts, tmp/'market')


def test_all_push_primary_rows_still_score_every_expert(inputs):
    req, lg, history, contracts, tmp, capture = inputs
    for r in contracts:r['line']='200'
    run(inputs)
    out = settle(tmp/'bundle', 110, 90, '2023-01-01T13:00:00Z', '2023-01-01T14:00:00Z',
                 capture, digest(capture.read_bytes()))
    assert out['primary_top2_brier'] == 'NOT_COMPUTED'  # no invented zero loss for pushed primary rows
    assert all(0 <= out['loss_' + a] <= 1 for a in ARMS)


def test_mixture_never_worse_than_random_selection_in_expectation():
    # Jensen: Brier is convex in p, so the weighted mixture beats the expected score of a weighted random draw.
    rng = np.random.default_rng(1)
    for _ in range(200):
        p = rng.uniform(size=3); w = rng.dirichlet(np.ones(3)); y = float(rng.uniform() < .5)
        assert (w @ p - y) ** 2 <= w @ (p - y) ** 2 + 1e-15


def test_mix_grids_union_support_and_coherence():
    a = ScoreGrid.poisson(1.2, 0.8); b = ScoreGrid(np.full((2, 2), .25), 3, 3)
    m = mix_grids([a, b, a], [0.25, 0.5, 0.25])
    assert m.p.sum() == pytest.approx(1)
    assert m.winner()[0] == pytest.approx(0.5 * a.winner()[0] + 0.5 * b.winner()[0])
    with pytest.raises(AdmissionError):
        mix_grids([a, b], [0.7, 0.7])


def test_hedge_weights_follow_lower_loss():
    w = hedge_weights(np.array([10.0, 12.0, 20.0]), 1.0)
    assert w[0] > w[1] > w[2] and w.sum() == pytest.approx(1)
    assert hedge_weights(np.zeros(3), 5.0) == pytest.approx([1/3] * 3)


def test_tampered_mixture_weights_rejected(inputs):
    run(inputs)
    folder = inputs[4]/'bundle'
    receipt = read_rows(folder/'RECEIPT.csv')
    receipt[0]['mixture_weights'] = ';'.join(f'{a}:{x}' for a, x in zip(ARMS, (0.0, 0.0, 1.0)))
    (folder/'RECEIPT.csv').write_bytes(csv_bytes(receipt))
    with pytest.raises(AdmissionError, match='mixture weights differ'):
        verify_bundle(folder)


def test_warm_start_ignores_rows_on_or_after_cutoff(inputs):
    req, lg, history, contracts, tmp, _ = inputs
    train = admit_history(history, information_horizon(req)[0], req['event_id'], lg.path, lg.endpoint)
    as_of = information_horizon(req)[0].tz_localize(None)
    base, n = warm_start(lg, train, as_of)
    leak = train.copy(); leak['date'] = leak['date'] + __import__('pandas').Timedelta(days=4000)
    plus, n2 = warm_start(lg, __import__('pandas').concat([train, leak]), as_of)
    assert n > 0 and n2 == n and plus == pytest.approx(base)


def test_eta_default_is_labelled_for_unreplayed_competition(inputs):
    eta, source, _ = eta_for(inputs[1])
    assert source.startswith('DEFAULT') and eta > 0


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


@pytest.mark.parametrize('issue,actual,expected,source', [
    ('2023-01-01T10:00:00Z', '2023-01-01T11:00:00Z', '2023-01-01T10:00:00Z', 'ISSUE_AT'),        # issued early: nothing later used
    ('2023-01-01T12:30:00Z', '2023-01-01T11:05:00Z', '2023-01-01T11:00:00Z', 'SCHEDULED_START'), # research up to the game-log start
    ('2023-01-01T12:30:00Z', '', '2023-01-01T11:00:00Z', 'SCHEDULED_START'),
    ('2023-01-01T12:30:00Z', '2023-01-01T10:40:00Z', '2023-01-01T10:40:00Z', 'ACTUAL_START'),    # play began before schedule
])
def test_information_horizon_is_the_game_log_scheduled_start(inputs, issue, actual, expected, source):
    req = dict(inputs[0], issue_at=issue, actual_start=actual)
    horizon, got = information_horizon(req)
    assert horizon == __import__('pandas').Timestamp(expected) and got == source


@pytest.mark.parametrize('defect', ['separate_cutoff', 'missing_start', 'blank_start'])
def test_no_separate_cutoff_and_scheduled_start_required(inputs, defect):
    req, lg, history, contracts, tmp, _ = copy.deepcopy(inputs)
    if defect == 'separate_cutoff':req['cutoff'] = '2023-01-01T00:00:00Z'
    if defect == 'missing_start':del req['scheduled_start']
    if defect == 'blank_start':req['scheduled_start'] = ''
    with pytest.raises(AdmissionError, match='cutoff|scheduled_start'):
        forecast(req, lg, history, contracts, tmp/defect)
    assert not (tmp/defect).exists()


def test_receipt_records_horizon_and_late_issue_uses_scheduled_start(inputs):
    req, lg, history, contracts, tmp, _ = copy.deepcopy(inputs)
    req.update(issue_at='2023-01-01T11:30:00Z', actual_start='2023-01-01T11:10:00Z')
    rec = forecast(req, lg, history, contracts, tmp/'late')
    assert rec['information_horizon'].startswith('2023-01-01T11:00:00') and rec['horizon_source'] == 'SCHEDULED_START'
    assert rec['actual_issue_phase'] == 'POST_START_ISSUE'
    history[0]['available_at'] = '2023-01-01T11:20:00+00:00'  # published after the scheduled start: inadmissible
    with pytest.raises(AdmissionError):
        forecast(req, lg, history, contracts, tmp/'late2')


def test_warm_fits_cannot_use_later_published_labels(inputs, monkeypatch):
    import pandas as pd
    from ml import primary
    req, lg, history, _, _, _ = inputs
    train = admit_history(history, information_horizon(req)[0], req['event_id'], lg.path, lg.endpoint)
    delayed = train.iloc[0].event_id
    train.loc[train.event_id == delayed, 'available_at'] = pd.Timestamp('2022-12-31')
    calls = []
    grid = ScoreGrid.poisson(2, 1)
    def fit(lg, earlier, as_of):
        assert (earlier.available_at <= as_of).all()
        assert (earlier.final_at <= as_of).all()
        assert delayed not in set(earlier.event_id)
        calls.append(as_of)
        return {a: lambda *args: (grid, []) for a in ARMS}, 3.5
    monkeypatch.setattr(primary, '_fit_models', fit)
    assert warm_records(lg, train, pd.Timestamp('2023-01-01'))
    assert calls


def test_flagged_experts_cannot_train_warm_weights(inputs, monkeypatch):
    import pandas as pd
    from ml import primary
    req, lg, history, _, _, _ = inputs
    train = admit_history(history, information_horizon(req)[0], req['event_id'], lg.path, lg.endpoint)
    grid = ScoreGrid.poisson(2, 1)
    monkeypatch.setattr(primary, '_fit_models', lambda *args: ({a: lambda *args: (grid, ['RHO_CLAMPED']) for a in ARMS}, 3.5))
    assert warm_start(lg, train, pd.Timestamp('2023-01-01'))[1] == 0


def test_feedback_event_is_not_counted_again_in_warm_history(inputs):
    req, lg, history, contracts, tmp, capture = inputs
    run(inputs)
    fb = settle(tmp/'bundle', 110, 95, '2023-01-01T13:00:00Z', '2023-01-01T14:00:00Z', capture, digest(capture.read_bytes()))
    prior = dict(history[0], event_id=req['event_id'], home=req['home'], away=req['away'], hs=110, as_=95,
                 reg_hs=110, reg_as=95, date='2023-01-01T11:00:00Z', final_at=fb['final_at'], available_at=fb['available_at'])
    nxt = dict(req, event_id='EXAMPLE-NEXT', scheduled_start='2023-01-03T11:00:00Z', issue_at='2023-01-03T10:00:00Z', actual_start='2023-01-03T11:00:00Z')
    rec = forecast(nxt, lg, history+[prior], contracts, tmp/'next', feedback=[fb])
    warm = read_rows(tmp/'next'/'WARM_START.csv')
    learned = read_rows(tmp/'next'/'FEEDBACK_LOSSES.csv')
    assert req['event_id'] not in {r['event_id'] for r in warm}
    assert [r['event_id'] for r in learned] == [req['event_id']]
    assert rec['feedback_events'] == 1
    prior['hs'] = 111;prior['reg_hs'] = 111
    with pytest.raises(AdmissionError, match='score conflict'):
        forecast(nxt, lg, history+[prior], contracts, tmp/'conflict', feedback=[fb])
    fb['home_score'] = '110.5'
    with pytest.raises(AdmissionError, match='invalid final score'):
        feedback_losses([fb], rec['context'], '2023-01-04T00:00:00Z')


@pytest.mark.parametrize('eta,loss', [(float('nan'),[0,1,2]),(float('inf'),[0,1,2]),(-1,[0,1,2]),(0,[0,1,2]),(1,[0,float('nan'),2]),(1,[-1,0,1])])
def test_invalid_learning_parameters_rejected(eta, loss):
    with pytest.raises(AdmissionError):hedge_weights(np.array(loss), eta)


def test_eta_parameter_requires_exact_policy_and_known_at(inputs, monkeypatch):
    from ml import primary
    tmp, capture = inputs[4:]
    table = tmp/'eta.csv'
    row = dict(competition=inputs[1].path, policy=POLICY, eta=5, tune_end='2022-01-01T00:00:00Z',
               frozen_at='2022-02-01T00:00:00Z', evidence_path=str(capture), evidence_sha256=digest(capture.read_bytes()))
    table.write_bytes(csv_bytes([row]));monkeypatch.setattr(primary, 'ETA_TABLE', table)
    assert eta_for(inputs[1], '2022-01-15T00:00:00Z')[1] == 'DEFAULT_PARAMETER_NOT_KNOWN_AT_HORIZON'
    assert eta_for(inputs[1], '2023-01-01T00:00:00Z')[:2] == (5, 'ADMITTED_EXACT_POLICY_PARAMETER')
    table.write_bytes(csv_bytes([row,row]))
    with pytest.raises(AdmissionError, match='conflicting eta'):eta_for(inputs[1], '2023-01-01T00:00:00Z')
    row['policy'] = 'OTHER_POLICY';table.write_bytes(csv_bytes([row]))
    assert eta_for(inputs[1], '2023-01-01T00:00:00Z')[1] == 'DEFAULT_NO_ADMITTED_ROW'
    row['closing_odds'] = '1.9';table.write_bytes(csv_bytes([row]))
    with pytest.raises(AdmissionError, match='extra/market columns'):
        eta_for(inputs[1], '2023-01-01T00:00:00Z')


def test_cumulative_losses_bound_to_saved_learning_rows(inputs):
    run(inputs)
    folder=inputs[4]/'bundle'
    receipt=read_rows(folder/'RECEIPT.csv')
    receipt[0]['cumulative_losses']=';'.join(f'{a}:0' for a in ARMS)
    receipt[0]['mixture_weights']=';'.join(f'{a}:{1/3}' for a in ARMS)
    (folder/'RECEIPT.csv').write_bytes(csv_bytes(receipt))
    with pytest.raises(AdmissionError, match='frozen learning ledgers'):verify_bundle(folder)
