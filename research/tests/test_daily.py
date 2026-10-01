import json
from datetime import datetime, timezone
import pandas as pd
import pytest
from research.src.daily import parse_nbl, parse_epl_fixtures, grade_nbl_shadows


def test_nbl_future_final_duplicate_and_incomplete_page_are_rejected():
    now=datetime(2026,10,1,tzinfo=timezone.utc)
    row=dict(id="x",season_type="regular",starts_at_ms=1790847000000,round_label="3",
             home={"team_code":"MEL"},away={"team_code":"ADL"},phase="complete",home_score=100,away_score=90)
    with pytest.raises(ValueError,match="impossible"):
        parse_nbl(dict(total=1,matches=[row]),now)
    with pytest.raises(ValueError,match="pagination"):
        parse_nbl(dict(total=2,matches=[row]),now)
    row.update(phase="upcoming")
    with pytest.raises(ValueError,match="duplicate"):
        parse_nbl(dict(total=2,matches=[row,row]),now)


def test_epl_summer_schedule_clock_converts_to_utc_and_official_id_stays_missing(tmp_path):
    path=tmp_path/"2026-27.txt"
    path.write_text("▪ Matchday 1\n Fri Aug 21 2026\n  20:00 Arsenal FC v Coventry City FC\n",encoding="utf-8")
    rows,excluded=parse_epl_fixtures(path,datetime(2026,8,20,tzinfo=timezone.utc))
    assert not excluded
    assert rows[0]["kickoff_utc"]==datetime(2026,8,21,19,tzinfo=timezone.utc)
    assert rows[0]["official_event_id"] is None


def test_source_state_live_is_coverage_exclusion_not_global_failure():
    row=dict(id="x",season_type="regular",starts_at_ms=1790847000000,round_label="3",
             home={"team_code":"MEL"},away={"team_code":"ADL"},phase="live")
    finals,fixtures,excluded=parse_nbl(dict(total=1,matches=[row]),datetime(2026,10,1,9,tzinfo=timezone.utc))
    assert not fixtures and finals.empty
    assert excluded[0]["reason"]=="NOT_FRESH_PREGAME_OR_TERMINAL"
