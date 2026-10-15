"""Reject misleading replay pooling, dropped failures and unsafe reruns."""
import numpy as np
import pandas as pd
import pytest

from ml.evaluation import primary_replay as replay


def scores():
    return pd.DataFrame(dict(season=[2024]*8, event_id=[str(i) for i in range(8)],
                             week=[f'2024-W{i+1:02d}' for i in range(8)],
                             **{p+'_home':np.linspace(.1,.3,8) for p in ['FAST','SLOW','BASELINE','EQUAL_MIX','HEDGE_MIX','EXP3_SELECT']},
                             EXP3_p_baseline=[.3]*8, HEDGE_w_baseline=[.1]*8))


def test_pooled_weeks_are_shared_across_competitions():
    a=scores();a['comp']='A';b=scores();b['comp']='B'
    result=replay.pooled_interval(pd.concat([a,b],ignore_index=True))
    assert result['k_weeks']==8 and result['n_events']==16


def test_failure_only_report_is_retained_and_rerun_cannot_overwrite(tmp_path, monkeypatch):
    output=tmp_path/'report';monkeypatch.setattr(replay,'OUT',output)
    replay.write([dict(competition='Example',status='NO_TUNE_OR_TEST_ROWS')],dict(kind='EXAMPLE'))
    text=(output/'RESULTS.md').read_text(encoding='utf8')
    assert 'NO_TUNE_OR_TEST_ROWS' in text and 'NOT_COMPUTABLE' in text
    before=(output/'RESULTS.md').read_bytes()
    with pytest.raises(FileExistsError):replay.write([],dict(kind='EXAMPLE'))
    assert (output/'RESULTS.md').read_bytes()==before


def test_data_hold_competition_is_not_pooled(tmp_path,monkeypatch):
    monkeypatch.setattr(replay,'OUT',tmp_path/'report')
    replay.write([dict(competition='HELD',n_test=8,eta=2,rows=scores(),data_warnings='UNVERIFIED_SOURCE')],dict(kind='EXAMPLE'))
    assert 'NOT_COMPUTABLE' in (replay.OUT/'RESULTS.md').read_text(encoding='utf8')
    assert pd.read_csv(replay.OUT/'PAIRED_ROWS.csv').empty
    assert pd.read_csv(replay.OUT/'RESULTS.csv').iloc[0]['warnings']=='UNVERIFIED_SOURCE'


def test_policy_trajectory_does_not_depend_on_dataframe_index():
    frame=pd.DataFrame({'week':['2024-W01','2024-W02'],**{a+'_loss':[.1,.3] for a in replay.ARMS}})
    shifted=frame.copy();shifted.index=[40,70]
    assert np.allclose(replay.hedge_weights(frame,2), replay.hedge_weights(shifted,2))
    assert np.allclose(replay.exp3_expected(frame,3), replay.exp3_expected(shifted,3))


def test_flagged_replay_game_is_retained_in_coverage_not_scored(tmp_path,monkeypatch):
    from types import SimpleNamespace
    from ml.config import League
    from ml.core.distributions import ScoreGrid
    lg=League('Soccer/EXAMPLE','Soccer','EXAMPLE','EXAMPLE','dixon_coles')
    games=pd.DataFrame(dict(date=pd.to_datetime(['2023-12-01','2024-01-02']),season=[2023,2024],
                            event_id=['old','new'],home=['A','A'],away=['B','B'],hs=[1,2],as_=[0,1],stage=['REG','REG']))
    grid=ScoreGrid.poisson(1,1)
    experts={a:SimpleNamespace(grid=lambda *args:(grid,['RHO_CLAMPED'])) for a in replay.ARMS[:2]}
    experts[replay.ARMS[2]]=SimpleNamespace(grid=lambda:grid,total_line=2.5)
    monkeypatch.setattr(replay,'load_league',lambda lg:(games,None))
    monkeypatch.setattr(replay,'_fit_window',lambda *args:games.iloc[:1])
    monkeypatch.setattr(replay,'_experts',lambda *args:experts)
    result=replay.predictions(lg,[2024])
    assert result.empty and result.attrs['coverage']['flagged']==1
    assert result.attrs['coverage']['requested']==1
