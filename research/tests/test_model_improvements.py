import json
from datetime import datetime, timezone
import numpy as np
import pandas as pd
import pytest
from research.src.model_diagnostics import family_rows, reliability, wilson, elo_probability
from research.src.point_in_time import eligible_features, lagged_form
from research.src.evaluate import run_tuning, run_holdout


def test_opened_epl_tuning_and_holdout_cannot_be_overwritten():
    with pytest.raises(RuntimeError, match="already locked"):
        run_tuning()
    with pytest.raises(RuntimeError, match="already exists"):
        run_holdout()


def test_one_distribution_all_families_and_half_scaled_brier():
    matrix=np.array([[.1,.05,.05],[.1,.3,.1],[.05,.1,.15]])
    records=family_rows({"event_id":"x"},"candidate",matrix,1,1)
    assert {r["family"] for r in records}=={"1X2","TOTAL_2_5","BTTS"}
    for row in records:
        vector=np.array(json.loads(row["probabilities"]))
        assert vector.sum()==pytest.approx(1)
        assert row["brier"]==pytest.approx(np.square(vector-np.eye(len(vector))[row["outcome"]]).sum()/2)


def test_reliability_preserves_empty_bins_and_uncertainty():
    report=reliability([.8,.8,.8],[1,0,1])
    assert report["bins"][0]["n"]==0
    assert report["bins"][0]["observed_rate_ci95"] is None
    assert report["bins"][4]["observed_rate_ci95"][0] < 2/3 < report["bins"][4]["observed_rate_ci95"][1]
    assert wilson(0,0) is None


def test_future_results_do_not_change_elo():
    games=pd.DataFrame({"event_id":["a","b"],"home":["A","A"],"away":["B","B"],
                        "hg":[90,70],"ag":[80,100],"kickoff_utc":pd.to_datetime(["2026-01-01Z".replace("Z","T00:00Z"),"2026-02-01T00:00Z"],utc=True)})
    cutoff=pd.Timestamp("2026-01-20T00:00Z")
    before=elo_probability(games,cutoff,"A","B")
    games.loc[1,"hg"]=1000
    assert elo_probability(games,cutoff,"A","B")==before


def test_postgame_awards_and_future_lineups_never_become_features():
    rows=[dict(event_id="x",entity_id="A",feature="award",temporal_role="POSTGAME",value="winner"),
          dict(event_id="x",entity_id="A",feature="lineup",temporal_role="PREGAME",available_at_utc="2026-10-01T11:00Z",source_receipt_sha256="a"*64,value=1)]
    result=eligible_features(rows,"2026-10-01T10:00Z")
    assert not result["records"]
    assert {r["reason"] for r in result["excluded"]}=={"POSTGAME_OR_UNDEFINED_TEMPORAL_ROLE","AVAILABLE_AFTER_CUTOFF"}


def test_lagged_form_deduplicates_and_requires_availability():
    row=dict(event_id="x",home_team_id="A",away_team_id="B",training_eligible=True,phase="regular",
             home_score=10,away_score=5,event_date="2026-09-01")
    assert lagged_form([row],"A","2026-10-01T00:00Z")["n"]==0
    result=lagged_form([row,row],"A","2026-10-01T00:00Z",allow_date_assumption=True)
    assert result["n"]==1 and result["points_for"]==10
    assert result["excluded"][0]["reason"]=="DUPLICATE_OR_MISSING_EVENT_ID"
    with pytest.raises(ValueError, match="timezone"):
        eligible_features([],"2026-10-01")


def test_candidate_width_never_uses_future_result_labels(monkeypatch):
    from research.src import candidate_models
    from research.src.nbl_evaluate import checked_data
    monkeypatch.setattr(candidate_models,"verify_model_build",lambda *args: {})
    games=checked_data()
    cutoff=pd.Timestamp("2024-01-01T00:00Z")
    before,receipt=candidate_models.nbl(games,cutoff,"MEL","TAS")
    changed=games.copy()
    changed.loc[changed.kickoff_utc>=cutoff,"hg"]=250
    changed.loc[changed.kickoff_utc>=cutoff,"ag"]=0
    after,later=candidate_models.nbl(changed,cutoff,"MEL","TAS")
    assert before==pytest.approx(after)
    assert receipt["sd_margin"]==pytest.approx(later["sd_margin"])
    assert receipt["oof_residual_n"]==later["oof_residual_n"]
