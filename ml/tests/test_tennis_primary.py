"""Synthetic mechanical checks, never sporting calibration evidence."""
from datetime import datetime, timedelta, timezone
from pathlib import Path
import pytest

from ml.tennis_primary import (
    ARMS, POLICY, TennisAdmissionError, game_hold, tiebreak_win, match_grid,
    price, get_predictions, forecast, verify, settle, sha, tennis_score, weights,
)


def fixture(tmp_path):
    capture=tmp_path/"official_citation.txt"
    capture.write_text("Synthetic demonstration evidence; NOT an official sport result.")
    base=datetime(2024,1,1,tzinfo=timezone.utc)
    people=["Alex","Blair","Chris","Daria","Ella","Finn","Gus","Hana"]
    matches=[]
    for k in range(64):
        a=people[k%8]; b=people[(k+1+(k//8)%6)%8]
        if a==b:b=people[(k+3)%8]
        matches.append(dict(event_id=f"H{k:03}",competition="Tennis/SYNTH",status="FINAL",admission="RESEARCH_INPUT_REVIEWED",
                            format="SINGLES",surface="HARD" if k%4!=0 else "CLAY",date=(base+timedelta(days=k)).isoformat(),
                            final_at=(base+timedelta(days=k,hours=3)).isoformat(),
                            available_at=(base+timedelta(days=k,hours=4)).isoformat(),
                            player1=a,player2=b,winner=a if k%3 else b,
                            p1_serve_won="47",p1_serve_total="72",p2_serve_won="45",p2_serve_total="74",
                            source_url="https://example.org/synthetic",evidence_path=str(capture),evidence_sha256=sha(capture.read_bytes())))
    req=dict(event_id="NEXT1",competition="Tennis/SYNTH",format="SINGLES",player1="Alex",player2="Blair",surface="HARD",
             best_of="3",scheduled_start=(base+timedelta(days=80)).isoformat(),issue_at=(base+timedelta(days=79)).isoformat(),
             outcome_exposure="NONE_RECORDED")
    contracts=[dict(contract_key="win",family="MATCH_WINNER",side="PLAYER1",line=""),
               dict(contract_key="handicap",family="GAMES_HANDICAP",side="PLAYER2",line="2.5"),
               dict(contract_key="total",family="GAMES_TOTAL",side="OVER",line="22.5")]
    return req,matches,contracts,capture


def test_serve_and_tiebreak_symmetry():
    assert game_hold(0.5)==pytest.approx(0.5)
    assert game_hold(0.7)>game_hold(0.6)
    assert tiebreak_win(0.5,0.5,0)==pytest.approx(0.5)
    assert tiebreak_win(0.6,0.6,0)==pytest.approx(0.5)


@pytest.mark.parametrize("bestof",[3,5])
def test_tennis_outcome_coherence_and_not_games_winner(bestof):
    grid=match_grid(.64,.65,bestof)
    assert sum(grid.values())==pytest.approx(1,abs=1e-9)
    assert all(k[3]==bestof//2+1 or k[4]==bestof//2+1 for k in grid)
    assert any((winner==1 and g1<g2) or (winner==2 and g2<g1) for (winner,g1,g2,_,_) in grid)
    a=price(grid,dict(family="MATCH_WINNER",side="PLAYER1",line=""))
    b=price(grid,dict(family="MATCH_WINNER",side="PLAYER2",line=""))
    assert a["win"]+b["win"]==pytest.approx(1)
    o=price(grid,dict(family="GAMES_TOTAL",side="OVER",line="22"))
    u=price(grid,dict(family="GAMES_TOTAL",side="UNDER",line="22"))
    assert o["win"]==pytest.approx(u["loss"])
    assert o["push"]==pytest.approx(u["push"])
    assert o["win"]+o["push"]+o["loss"]==pytest.approx(1)


def test_end_to_end_and_late_feedback(tmp_path):
    req,hist,contracts,evidence=fixture(tmp_path)
    out=tmp_path/"forecast"
    folder,predictions=forecast(req,hist,contracts,[],out)
    assert len(predictions)==3
    assert verify(folder)["policy"]==POLICY
    assert all(0<=p["p_card"]<=1 for p in predictions)
    with pytest.raises(TennisAdmissionError,match="immutable"):
        forecast(req,hist,contracts,[],out)
    snap=tmp_path/"feedback.csv"
    _,rec=settle(folder,"6-0,4-6,7-6","2024-03-21T15:00:00+00:00","2024-03-21T16:00:00+00:00","https://example.org/synthetic",
                 evidence,sha(evidence.read_bytes()),snap)
    assert rec["winner"]=="Alex"
    assert all(0<=float(rec["loss_"+a])<=1 for a in ARMS)
    # Available feedback should affect only later forecasts.
    ws,n=weights([rec],dict(req,event_id="NEXT2"),datetime(2024,3,21,15,tzinfo=timezone.utc))
    assert ws==pytest.approx([0.25]*4)
    ws,n=weights([rec],dict(req,event_id="NEXT2"),datetime(2024,3,22,tzinfo=timezone.utc))
    assert n==1 and sum(ws)==pytest.approx(1)
    bad=tmp_path/"forecast"/"PREDICTIONS.csv"
    bad.write_text(bad.read_text().replace("0.","0.2",1))
    with pytest.raises(TennisAdmissionError,match="hash"):
        verify(out)


def test_rejection(tmp_path):
    req,hist,contracts,evidence=fixture(tmp_path)
    assert get_predictions(req,hist,contracts,[])[2]
    with pytest.raises(TennisAdmissionError,match="target"):
        get_predictions(req,[dict(hist[0],event_id="NEXT1")]+hist[1:],contracts)
    with pytest.raises(TennisAdmissionError,match="chronology"):
        get_predictions(req,[dict(hist[0],available_at="2026-01-01T00:00:00Z")]+hist[1:],contracts)
    with pytest.raises(TennisAdmissionError,match="evidence"):
        get_predictions(req,[dict(hist[0],evidence_sha256="not_real")]+hist[1:],contracts)
    with pytest.raises(TennisAdmissionError,match="insufficient"):
        get_predictions(req,hist[:2],contracts)
    with pytest.raises(TennisAdmissionError,match="outcome exposure"):
        get_predictions(dict(req,outcome_exposure="RESULT_SEEN"),hist,contracts)
    with pytest.raises(TennisAdmissionError,match="duplicate tennis"):
        get_predictions(req,hist,contracts+contracts[:1])
    with pytest.raises(TennisAdmissionError,match="incomplete"):
        tennis_score("6-4,3-6",3)
    with pytest.raises(TennisAdmissionError,match="invalid/extra"):
        tennis_score("6-4,6-4,6-4",3)
