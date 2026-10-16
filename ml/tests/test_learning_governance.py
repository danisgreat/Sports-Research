"""Prospective shadow ledger, model registry and learning-status triggers (EXAMPLE data only)."""
import numpy as np
import pandas as pd
import pytest

from ml import primary as p
from ml import registry as R
from ml import research_ingest as ri
from ml import learning_status as LS
from ml.evaluation import prospective as P
from ml.tests import learning_fixtures as lf

T0 = pd.Timestamp("2026-11-02T09:00:00Z")


def _rows(model, version, role, event, start, prob, rank, key="WIN-H", status="PRE_START_VERIFIED", issued=None):
    issued = issued or start - pd.Timedelta(hours=2)
    return dict(forecast_id=f"{model}-{event}", model_id=model, model_version=version, role=role, event_id=event,
                competition="Basketball/EXAMPLE", endpoint="FULL_GAME_INCL_OT", contract_key=key, family="winner",
                side="HOME", line="", p=repr(prob), rank=str(rank), issued_at=issued.isoformat(),
                scheduled_start=start.isoformat(), training_release="R1", param_version="v1", code_sha256="x" * 64,
                evidence_status=status)


def _season(path, n_weeks, rng, cand_noise, champ_noise=.3):
    outcomes = []
    for i in range(n_weeks * 4):
        rows = []
        start = T0 + pd.Timedelta(days=2 * i)
        q = rng.uniform(.2, .8)
        y = rng.random() < q
        for key, truth in (("WIN-H", q), ("WIN-A", 1 - q)):
            rows += [_rows("CHAMP", "v3", "CHAMPION", f"E{i}", start, float(np.clip(truth + rng.normal(0, champ_noise), .02, .98)), 1 if key == "WIN-H" else 2, key),
                     _rows("CAND", "c1", "CANDIDATE", f"E{i}", start, float(np.clip(truth + rng.normal(0, cand_noise), .02, .98)), 1 if key == "WIN-H" else 2, key)]
            win = y if key == "WIN-H" else not y
            outcomes.append(dict(event_id=f"E{i}", contract_key=key, result="WIN" if win else "LOSS",
                                 final_at=(start + pd.Timedelta(hours=3)).isoformat(),
                                 available_at=(start + pd.Timedelta(hours=4)).isoformat(), evidence_sha256="e" * 64))
        P.freeze(path, rows, now=start - pd.Timedelta(hours=1))  # frozen at issue, before the start
    return pd.DataFrame(outcomes)


def test_freeze_is_append_only_hash_chained_and_refuses_late_or_market_rows(tmp_path):
    ledger = tmp_path / "SHADOW_LEDGER.csv"
    start = T0 + pd.Timedelta(days=1)
    P.freeze(ledger, [_rows("CAND", "c1", "CANDIDATE", "E1", start, .6, 1)], now=start - pd.Timedelta(hours=1))
    with pytest.raises(p.AdmissionError, match="duplicate"):
        P.freeze(ledger, [_rows("CAND", "c1", "CANDIDATE", "E1", start, .6, 1)], now=start - pd.Timedelta(hours=1))
    with pytest.raises(p.AdmissionError, match="before the scheduled start"):
        P.freeze(ledger, [_rows("CAND", "c1", "CANDIDATE", "E2", start, .6, 1)], now=start + pd.Timedelta(minutes=1))
    with pytest.raises(p.AdmissionError, match="market"):
        P.freeze(ledger, [dict(_rows("CAND", "c1", "CANDIDATE", "E3", start, .6, 1), odds="1.9")], now=start - pd.Timedelta(hours=1))
    P.freeze(ledger, [_rows("CHAMP", "v3", "CHAMPION", "E1", start, .55, 1)], now=start - pd.Timedelta(hours=1))
    assert len(P.verify_ledger(ledger)) == 2
    text = ledger.read_text(encoding="utf-8").replace("0.6", "0.7", 1)
    ledger.write_text(text, encoding="utf-8")
    with pytest.raises(p.AdmissionError, match="chain broken"):
        P.verify_ledger(ledger)


def test_paired_evaluation_needs_weeks_and_power_before_any_promotion(tmp_path):
    rng = np.random.default_rng(5)
    few = _season(tmp_path / "few.csv", 3, rng, cand_noise=.05)
    res = P.evaluate(P.verify_ledger(tmp_path / "few.csv"), few, "CHAMP:v3", "CAND:c1", delta=.01)
    assert res["disposition"] == "INSUFFICIENT_EVIDENCE"
    many = _season(tmp_path / "many.csv", 12, rng, cand_noise=.05)
    res = P.evaluate(P.verify_ledger(tmp_path / "many.csv"), many, "CHAMP:v3", "CAND:c1", delta=.01)
    assert res["disposition"] in ("PROMOTION_ELIGIBLE", "CALIBRATION_STUDY") and res["interval"]["status"] == "BELOW_ZERO"
    m = res["models"]["CAND:c1"]
    assert 0 <= m["hit_at_2"] <= 1 and m["ranked_events"] == 48 and m["coverage"] == 1
    b = res["breakdown"]
    assert set(b.dimension) == {"competition", "family", "endpoint"} and (b[b.dimension == "family"].contracts == 96).all()
    worse = _season(tmp_path / "worse.csv", 12, rng, cand_noise=.45, champ_noise=.05)
    assert P.evaluate(P.verify_ledger(tmp_path / "worse.csv"), worse, "CHAMP:v3", "CAND:c1", delta=.01)["disposition"] == "NO_CHANGE"
    with pytest.raises(p.AdmissionError, match="duplicate outcome"):
        P.evaluate(P.verify_ledger(tmp_path / "many.csv"), pd.concat([many, many]), "CHAMP:v3", "CAND:c1", delta=.01)
    early = many.copy()
    early.loc[0, "available_at"] = (T0 - pd.Timedelta(days=3)).isoformat()
    with pytest.raises(p.AdmissionError, match="not prospective"):
        P.evaluate(P.verify_ledger(tmp_path / "many.csv"), early, "CHAMP:v3", "CAND:c1", delta=.01)


def test_registry_is_chained_and_enforces_transitions(tmp_path):
    reg = tmp_path / "MODEL_REGISTRY.csv"
    base = dict(model_id="EX-MODEL", version="1", scope="Basketball/EXAMPLE", generating_commit="abc",
                code_reference="ml/x.py", recorded_at="2026-10-16T00:00:00Z")
    R.append(dict(base, status="DEVELOPMENT_EXPERIMENT"), reg)
    with pytest.raises(p.AdmissionError, match="PROSPECTIVE_SHADOW"):
        R.append(dict(base, status="PROSPECTIVELY_QUALIFIED", authority="owner"), reg)
    R.append(dict(base, status="PROSPECTIVE_SHADOW"), reg)
    report = tmp_path / "REPORT.md"
    report.write_text("disposition NO_CHANGE", encoding="utf-8")
    with pytest.raises(p.AdmissionError, match="PROMOTION_ELIGIBLE"):
        R.append(dict(base, status="PROSPECTIVELY_QUALIFIED", authority="owner", evaluation_report=str(report)), reg)
    with pytest.raises(p.AdmissionError, match="authority"):
        R.append(dict(base, status="AUTHORISED_EXPERIMENTAL_PRIMARY"), reg)
    R.append(dict(base, status="RETIRED"), reg)
    with pytest.raises(p.AdmissionError, match="reactivated"):
        R.append(dict(base, status="PROSPECTIVE_SHADOW"), reg)
    with pytest.raises(p.AdmissionError, match="rollback_to"):
        R.append(dict(base, version="2", status="ROLLED_BACK", rollback_to="EX-MODEL:9"), reg)
    assert [r["status"] for r in R.verify(reg)] == ["DEVELOPMENT_EXPERIMENT", "PROSPECTIVE_SHADOW", "RETIRED"]
    reg.write_text(reg.read_text(encoding="utf-8").replace("ml/x.py", "ml/y.py", 1), encoding="utf-8")
    with pytest.raises(p.AdmissionError, match="chain broken"):
        R.verify(reg)


def test_repository_registry_records_the_actual_current_models():
    current = R.current()
    assert current["PRIMARY_HEDGE_MIX_V3:3"]["status"] == "AUTHORISED_EXPERIMENTAL_PRIMARY"
    assert current["PRIMARY_HEDGE_MIX_V2:2"]["status"] == "RETIRED"
    assert current["TENNIS_EXPERIMENTAL_HEDGE_V1:1"]["status"] == "DEVELOPMENT_EXPERIMENT"
    assert not any(r["status"] == "PROSPECTIVELY_QUALIFIED" for r in current.values())


def test_learning_counters_and_review_clocks_by_sport_and_competition(tmp_path):
    frame = lf.season_frame()
    lf.ingest_frame(tmp_path, tmp_path / "s", frame, "all")
    store = ri.load_store(tmp_path / "s")
    res = LS.status(store, thresholds=(("INTERIM", "ALL", 50), ("COMPREHENSIVE", "ALL", 300), ("SPORT", "*", 100),
                                       ("COMPETITION", "*", 20)))
    s = res["status"].set_index(["scope_level", "scope"])
    assert s.loc[("ALL", "ALL"), "unique_settled_games"] == len(frame) == s.loc[("SPORT", "Basketball"), "unique_settled_games"]
    assert s.loc[("ALL", "ALL"), "hedge_feedback_games"] == 0  # research-only results never become expert feedback
    t = res["triggers"].set_index(["level", "scope"])
    assert t.loc[("INTERIM", "ALL"), "status"] == "DUE" and t.loc[("COMPREHENSIVE", "ALL"), "status"] == "NOT_DUE"
    reviewed_through = max(LS.settled_events(store).settled_at)
    log = pd.DataFrame([dict(review_id="RV1", level="INTERIM", scope="ALL", through_at=reviewed_through.isoformat(),
                             disposition="NO_CHANGE", report_path="", recorded_at=reviewed_through.isoformat())])
    alerts = pd.DataFrame([dict(scope="Basketball", kind="SOURCE_QUALITY_FAILURE",
                                raised_at=(reviewed_through + pd.Timedelta(days=1)).isoformat(), evidence_path="x")])
    res = LS.status(store, reviews=log, alerts=alerts)
    t = res["triggers"].set_index(["level", "scope"])
    assert t.loc[("INTERIM", "ALL"), "settled_since_last"] == 0 and t.loc[("SPORT", "Basketball"), "status"] == "EARLY_REVIEW"
    bad = tmp_path / "REVIEW_LOG.csv"
    bad.write_bytes(p.csv_bytes([dict(log.iloc[0], disposition="AUTO_PROMOTE")]))
    with pytest.raises(p.AdmissionError, match="disposition"):
        LS.read_reviews(bad)
