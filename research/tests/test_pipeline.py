from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from research.src.dixon_coles import fit_dc, predict
from research.src.emit_card import build, pair_type, price, states
from research.src.features import population_1x2, tb1_md
from research.src.load import parse_openfootball
from research.src.legacy_ledger import extract
from research.src import legacy_ledger
from research.src.settle import FinalReceipt, settle
from research.src.draft_epl import draft
from research.src.pilot import score_events
from research.src.sports.base import Contract
from research.src.nbl_evaluate import checked_data
from research.src.nbl_model import fit as fit_nbl, population_home, predict as predict_nbl
from research.src import feeds
from research.src.nbl_shadow import freeze as freeze_nbl_shadow

ROOT = Path(__file__).resolve().parents[1]


def test_six_seasons_are_complete_and_crosschecked():
    df = pd.read_parquet(ROOT / "data/processed/matches.parquet")
    assert len(df) == 2280
    assert df.groupby("season").size().to_dict() == {f"{y}-{str(y+1)[-2:]}": 380 for y in range(2020, 2026)}
    assert not df.duplicated(["season", "home", "away"]).any()
    assert all(len(set(g.home) | set(g.away)) == 20 for _, g in df.groupby("season"))
    assert not any("odd" in col.lower() or "price" in col.lower() for col in df.columns)


def test_nbl_exact_grain_and_independent_score_resolution():
    import json
    df = checked_data()
    manifest = json.loads((ROOT / "data/processed/nbl_source_manifest.json").read_text(encoding="utf-8"))
    adjudications = json.loads((ROOT / "data/processed/nbl_fixture_adjudications.json").read_text(encoding="utf-8"))
    assert len(df) == 738
    assert manifest["fixture_agree"] == 736
    assert manifest["fixture_adjudicated"] == 2
    assert manifest["fixture_unresolved"] == 0
    assert (df.score_validation_status == "ADJUDICATED_OFFICIAL").sum() == 2
    assert {(x["season"], tuple(x["official"]), tuple(x["fixtures"])) for x in adjudications} == {
        ("NBL23", (76, 105), (76, 103)), ("NBL26", (105, 94), (103, 94))}


def test_nbl_future_scores_cannot_change_precutt_and_joint_price():
    df = checked_data()
    cutoff = pd.Timestamp("2024-01-01T00:00:00Z")
    before = fit_nbl(df, cutoff, 365)
    p0 = population_home(df, cutoff)
    altered = df.copy()
    future = altered.kickoff_utc >= cutoff
    altered.loc[future, "hg"] = 250
    altered.loc[future, "ag"] = 0
    altered.loc[future, "home"] = "FUTURE_ONLY"
    after = fit_nbl(altered, cutoff, 365)
    assert np.array_equal(before.coefficients, after.coefficients)
    assert np.array_equal(before.residual_covariance, after.residual_covariance)
    assert population_home(altered, cutoff) == p0
    joint, p_home = predict_nbl(before, "MEL", "TAS")
    assert joint.residual_sample == before.training_matches
    assert 0 < p_home < 1 and joint.sd_margin > 0 and joint.sd_total > 0


def test_nbl_exact_event_final_adapter_uses_league_status(monkeypatch):
    import json
    raw = (ROOT / "data/raw/nbl_official/nbl26.json").read_bytes()
    obj = json.loads(raw)
    event = next(m for m in obj["matches"] if m.get("season_type") == "regular" and m.get("phase") == "complete")
    import hashlib
    monkeypatch.setattr(feeds, "_fetch", lambda url: (obj, hashlib.sha256(raw).hexdigest(), datetime.now(timezone.utc)))
    receipt = feeds.nbl_final(event["id"], 2025)
    assert (receipt.home_score, receipt.away_score) == (event["home_score"], event["away_score"])
    assert receipt.endpoint == "INCL_OVERTIME"
    assert settle(Contract(event["id"], "TOTAL", "OVER", 0.5, "INCL_OVERTIME"), receipt).result == "W"
    with pytest.raises(ValueError, match="absent"):
        feeds.nbl_final("WRONG-EVENT", 2025)
    event["phase"] = "upcoming"
    with pytest.raises(ValueError, match="not a complete"):
        feeds.nbl_final(event["id"], 2025)


def test_nbl_shadow_receipts_are_pregame_and_immutable():
    import json
    receipts = sorted((ROOT / "shadow/nbl27").glob("*.json"))
    assert len(receipts) == 2
    for path in receipts:
        row = json.loads(path.read_text(encoding="utf-8"))
        assert datetime.fromisoformat(row["data_cutoff_utc"]) <= datetime.fromisoformat(row["forecast_utc"]) < datetime.fromisoformat(row["start_utc"])
        assert row["shadow_only"] and not row["performance_eligible"]
        assert row["issuance_status"] == "NO_CARD_ISSUED"
        assert row["p_model_home_ml"] + row["p_model_away_ml"] == pytest.approx(1)
    original = [path.read_bytes() for path in receipts]
    assert freeze_nbl_shadow(now=datetime.fromisoformat(json.loads(receipts[0].read_text(encoding="utf-8"))["forecast_utc"])) == []
    assert [path.read_bytes() for path in receipts] == original


def test_historical_index_has_522_ineligible_slots():
    rows=extract()
    assert len(rows)==522
    assert [r["card_id"] for r in rows]==[f"P-{i:03}" for i in range(1,523)]
    assert all(r["performance_eligible"]=="false" for r in rows)
    assert all(r["record_status"]=="RESERVED_UNDER_RECONCILIATION" for r in rows[517:])


def test_historical_corrections_are_append_only(tmp_path,monkeypatch):
    import csv
    base=tmp_path/"ledger.csv"; revisions=tmp_path/"corrections.csv"
    with base.open("w",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=legacy_ledger.FIELDS);writer.writeheader()
        row=dict.fromkeys(legacy_ledger.FIELDS,"");row.update(card_id="P-001",event="old",performance_eligible="false")
        writer.writerow(row)
    with revisions.open("w",newline="",encoding="utf-8") as f:
        csv.writer(f).writerow(legacy_ledger.CORRECTION_FIELDS)
    monkeypatch.setattr(legacy_ledger,"OUTPUT",base)
    monkeypatch.setattr(legacy_ledger,"CORRECTIONS",revisions)
    change=dict(revision_id="P001-R1",card_id="P-001",field="event",old_value="old",new_value="corrected",
                reason="source correction",source_url="https://example.org/event",retrieved_utc="2026-09-29T00:00:00Z",
                response_sha256="a"*64)
    legacy_ledger.append_correction(change)
    with pytest.raises(ValueError,match="duplicate"):
        legacy_ledger.append_correction(change)
    assert base.read_text(encoding="utf-8").count("corrected")==0
    assert revisions.read_text(encoding="utf-8").count("corrected")==1


def test_future_shuffling_does_not_change_pre_cutoff_forecast():
    df = pd.read_parquet(ROOT / "data/processed/matches.parquet")
    cutoff = pd.Timestamp("2024-02-01T00:00:00Z")
    original = fit_dc(df, cutoff)
    m0 = population_1x2(df, cutoff)
    m1 = tb1_md(df, "2023-24", cutoff, "Arsenal", "Chelsea")
    altered = df.copy()
    future = altered.kickoff_utc >= cutoff
    altered.loc[future, "hg"] = 20
    altered.loc[future, "ag"] = 0
    altered.loc[future, "home"] = "FUTURE_ONLY"
    revised = fit_dc(altered, cutoff)
    assert predict(original, "Arsenal", "Chelsea")[0] == pytest.approx(predict(revised, "Arsenal", "Chelsea")[0])
    assert m0 == pytest.approx(population_1x2(altered, cutoff))
    assert m1 == pytest.approx(tb1_md(altered, "2023-24", cutoff, "Arsenal", "Chelsea"))


def receipt(state="FINAL", event="x", h=3, a=2, endpoint="FINAL_SCORE"):
    return FinalReceipt(event, state, h, a, endpoint, "https://example.org/final/x",
                        datetime.now(timezone.utc), "a"*64, f"{h}-{a}")


@pytest.mark.parametrize("contract,expected", [
    (Contract("x", "ML", "HOME", None, "FINAL_SCORE"), "W"),
    (Contract("x", "ML", "AWAY", None, "FINAL_SCORE"), "L"),
    (Contract("x", "SPREAD", "HOME", -1.5, "FINAL_SCORE"), "L"),
    (Contract("x", "SPREAD", "AWAY", 1.5, "FINAL_SCORE"), "W"),
    (Contract("x", "TOTAL", "OVER", 5, "FINAL_SCORE"), "P"),
    (Contract("x", "TOTAL", "UNDER", 5.5, "FINAL_SCORE"), "W"),
    (Contract("x", "1X2", "HOME", None, "FINAL_SCORE"), "W"),
    (Contract("x", "1X2", "DRAW", None, "FINAL_SCORE"), "L"),
    (Contract("x", "BTTS", "YES", None, "FINAL_SCORE"), "W"),
    (Contract("x", "BTTS", "NO", None, "FINAL_SCORE"), "L"),
])
def test_feed_settlement(contract, expected):
    assert settle(contract, receipt()).result == expected


def test_settlement_rejects_live_wrong_event_and_endpoint():
    c = Contract("x", "ML", "HOME", None, "FINAL_SCORE")
    with pytest.raises(ValueError, match="not terminal"):
        settle(c, receipt(state="IN_PROGRESS"))
    with pytest.raises(ValueError, match="ID mismatch"):
        settle(c, receipt(event="y"))
    with pytest.raises(ValueError, match="endpoint mismatch"):
        settle(c, receipt(endpoint="REGULATION_9"))


def test_one_distribution_prices_pairs_and_rejects_bad_mass():
    d = states([{"home": 1, "away": 0, "p": .3},
                {"home": 0, "away": 1, "p": .2},
                {"home": 1, "away": 1, "p": .5}])
    over = Contract("x", "TOTAL", "OVER", 1.5, "FINAL_SCORE")
    under = Contract("x", "TOTAL", "UNDER", 1.5, "FINAL_SCORE")
    assert pair_type(d, over, under) == "FORCED_PAIR"
    assert price(d, over)["conditional_win"] == pytest.approx(.5)
    with pytest.raises(ValueError, match="sum to one"):
        states([{"home": 1, "away": 0, "p": .8}])


def test_emitter_requires_pregame_cutoff_and_provenance():
    s = [{"home": 1, "away": 0, "p": .6}, {"home": 0, "away": 1, "p": .4}]
    base = dict(official_event_id="x", card_id="P-523", model_version="test",
                data_checksum="b"*64, start_utc="2026-10-01T10:00:00Z",
                data_cutoff_utc="2026-10-01T08:00:00Z", model_states=s,
                baseline_states=s, contracts=[dict(market="ML", side="HOME", line=None, endpoint="FINAL_SCORE")],
                lane_status="UNVALIDATED", lineup_status="CONFIRMED",
                lineup_source_url="https://example.org/lineup",lineup_retrieved_utc="2026-10-01T08:30:00Z",
                recency_check="NOT_RETRIEVED", state_source_url="https://example.org/schedule")
    output = build(base, datetime(2026,10,1,9,tzinfo=timezone.utc))
    assert output["rows"][0]["p_card"]["conditional_win"] == pytest.approx(.6)
    with pytest.raises(ValueError, match="cutoff <= issue < actual start"):
        build(base, datetime(2026,10,1,11,tzinfo=timezone.utc))


def test_card_kill_paths_close_to_joint_failure_mass():
    s=[{"home":1,"away":0,"p":.3},{"home":0,"away":1,"p":.2},
       {"home":1,"away":1,"p":.5}]
    spec=dict(official_event_id="x",card_id="DRAFT",model_version="test",data_checksum="b"*64,
              start_utc="2026-10-01T10:00:00Z",data_cutoff_utc="2026-10-01T08:00:00Z",
              model_states=s,baseline_states=s,lane_status="VALIDATED",lineup_status="CONFIRMED",
              lineup_source_url="https://example.org/lineup",lineup_retrieved_utc="2026-10-01T08:30:00Z",
              recency_check="NOT_RETRIEVED",state_source_url="https://example.org/schedule",
              contracts=[dict(market="ML",side="HOME",line=None,endpoint="FINAL_SCORE"),
                         dict(market="TOTAL",side="OVER",line=2.5,endpoint="FINAL_SCORE")])
    out=build(spec,datetime(2026,10,1,9,tzinfo=timezone.utc))
    assert sum(x["mass"] for x in out["numbered_top2_kill_paths"])==pytest.approx(out["top2_both_fail"])
    assert out["top2_both_fail"]==pytest.approx(.2)


def test_epl_model_to_shadow_draft_bridge(tmp_path):
    import json
    from datetime import timedelta
    manifest=json.loads((ROOT/"data/processed/epl_2026-27_current_manifest.json").read_text(encoding="utf-8"))
    snapshot=datetime.fromisoformat(manifest["snapshot_utc"])
    now=snapshot+timedelta(hours=1)
    event=dict(official_event_id="TEST-NOT-REAL",card_id="DRAFT",home="Arsenal",away="Chelsea",
               start_utc=(snapshot+timedelta(hours=3)).isoformat(),state="PREGAME",
               state_source_url="https://league.example/event",state_retrieved_utc=(snapshot+timedelta(minutes=20)).isoformat(),
               identity_sources=["https://league.example/event","https://club.example/event","https://media.example/event"],
               lineup_status="PROJECTED",lineup_source_url="https://club.example/lineup",
               lineup_retrieved_utc=(snapshot+timedelta(minutes=25)).isoformat(),
               recency_check="NOT_RETRIEVED",recency_retrieved_utc=(snapshot+timedelta(minutes=30)).isoformat(),
               adjustment_factors={"home":1.0,"away":1.0},adjustment_type="NONE",adjustment_reason="")
    receipt=tmp_path/"fixture.json";output=tmp_path/"draft.json"
    receipt.write_text(json.dumps(event),encoding="utf-8")
    result=draft(receipt,output,now)
    assert result["shadow_only"] is True
    assert len(result["rows"])==7
    assert result["lane_status"]=="UNVALIDATED"
    assert output.exists() and output.with_suffix(".md").exists()


def test_pilot_rejects_unbacked_csv_eligibility_flags(tmp_path):
    import csv
    fields=next(csv.reader((ROOT/"PILOT_LEDGER_TEMPLATE.csv").open(encoding="utf-8")))
    values=[("1X2","HOME","",.5,"W"),("1X2","DRAW","",.25,"L"),
            ("1X2","AWAY","",.25,"L"),("TOTAL","OVER","2.5",.6,"W"),
            ("TOTAL","UNDER","2.5",.4,"L"),("BTTS","YES","",.55,"W"),
            ("BTTS","NO","",.45,"L")]
    path=tmp_path/"pilot.csv"
    with path.open("w",newline="",encoding="utf-8") as f:
        writer=csv.DictWriter(f,fieldnames=fields);writer.writeheader()
        for market,side,line,p,result in values:
            row=dict.fromkeys(fields,"")
            row.update(lane="EPL",event_id="test",market=market,selection=side,line=line,endpoint="REGULATION",
                       p_model=p,p_card=p,result=result,score_home=2,score_away=1,
                       lane_status="VALIDATED",shadow="false",performance_eligible="true",
                       data_cutoff_utc="2026-10-01T08:00:00Z",issued_utc="2026-10-01T09:00:00Z",
                       actual_start_utc="2026-10-01T10:00:00Z",adjustment_type="NONE")
            writer.writerow(row)
    with pytest.raises((ValueError, RuntimeError),match="(?i)(csv|canonical|ledger|bare|json)"):
        score_events(path)
