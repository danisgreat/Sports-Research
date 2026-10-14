"""Decision-lab arithmetic and shadow-lane custody (C-ML-07, C-ML-08, C-ML-10, C-ML-16, C-ML-17)."""
import hashlib
from datetime import datetime, timedelta, timezone

import numpy as np
import pandas as pd
import pytest

from ml.decision import devig, kelly
from ml.decision.bandit import FullInfoRidge, LinTS
from ml.shadow import lane


def test_devig_methods_normalise_and_shin_shrinks_longshots():
    odds = np.array([1.40, 4.80, 8.50])
    for fn in devig.METHODS.values():
        assert fn(odds).sum() == pytest.approx(1.0)
    m, s = devig.multiplicative(odds), devig.shin(odds)
    assert s[0] > m[0] and s[2] < m[2]  # favourite-longshot correction


def test_kelly_formulas():
    assert kelly.kelly_full(0.5, 2.2) == pytest.approx((0.5 * 1.2 - 0.5) / 1.2)
    assert kelly.kelly_full(0.4, 2.2) == 0.0
    f = kelly.kelly_full(0.5, 2.2, p_push=0.1)
    assert f == pytest.approx((0.5 * 1.2 - 0.4) / (1.2 * 0.9))
    assert 0 < kelly.shrink_factor(0.08, 2.2, 0.03) < 1
    assert kelly.stake(0.7, 2.5, 0.0) == 0.02  # the hard cap binds
    assert kelly.cap_slate(np.array([0.06, 0.06])).sum() == pytest.approx(0.10)


def test_clv_definition():
    assert devig.clv(2.10, 0.50) == pytest.approx(0.05)


def test_bandits_learn_the_better_arm():
    x = np.array([1.0, 0.5])
    b = LinTS(2, (0.0, 1.0), v=0.01, seed=1)
    f = FullInfoRidge(2, (0.0, 1.0))
    for _ in range(300):
        a, prop = b.choose(x)
        assert prop.sum() == pytest.approx(1.0)
        b.update(a, x, [0.0, 0.2][a])
        f.update_all(x, np.array([0.0, 0.2]))
    assert b.choose(x)[0] == 1 and f.choose(x) == 1


# C-ML-07 market columns never cross the boundary
@pytest.mark.parametrize("col", ["B365H", "PSCH", "home_moneyline", "spread_line", "total_line", "Over Odds"])
def test_c_ml_07_market_columns_refused(col):
    with pytest.raises(lane.MarketColumnError):
        lane.assert_no_market_columns(["event_key", col])


def test_c_ml_07_contract_line_column_allowed():
    lane.assert_no_market_columns(["event_key", "line", "league_median_line", "mass_push", "p_decisive"])


def _setup_receipt(tmp_path, monkeypatch, start: datetime, digest: str, name="SHADOW_FORECASTS_2026-W43.csv"):
    monkeypatch.setattr(lane, "SHADOW_ROOT", tmp_path / "shadow")
    d = tmp_path / "shadow" / "M-r1"
    d.mkdir(parents=True)
    (d / "FREEZE_RECEIPTS.md").write_text(
        "| file | bytes | sha256 | first_start_utc | frozen_utc | workshop | status |\n|---|---|---|---|---|---|---|\n"
        f"| `{name}` | 10 | `{digest}` | {start.strftime('%Y-%m-%dT%H:%M:%SZ')} | x | y | PENDING_START |\n",
        encoding="utf-8")
    return d


def test_c_ml_17_reveal_refused_before_start_and_on_hash_mismatch(tmp_path, monkeypatch):
    f = tmp_path / "SHADOW_FORECASTS_2026-W43.csv"
    f.write_bytes(b"event_key,line\nE1,2.5\n")
    digest = hashlib.sha256(f.read_bytes()).hexdigest()
    start = datetime(2026, 10, 20, tzinfo=timezone.utc)
    _setup_receipt(tmp_path, monkeypatch, start, digest)
    with pytest.raises(ValueError, match="not passed"):
        lane.reveal(f, "M-r1", now_utc=start - timedelta(minutes=1))           # C-ML-08 / C-ML-17 negative
    dest = lane.reveal(f, "M-r1", now_utc=start + timedelta(minutes=1))        # legitimate edge: just after start
    assert dest.read_bytes() == f.read_bytes()


def test_c_ml_10_reveal_refuses_tampered_file(tmp_path, monkeypatch):
    f = tmp_path / "SHADOW_FORECASTS_2026-W43.csv"
    f.write_bytes(b"event_key,line\nE1,2.5\n")
    _setup_receipt(tmp_path, monkeypatch, datetime(2026, 1, 1, tzinfo=timezone.utc), "0" * 64)
    with pytest.raises(ValueError, match="SHA-256"):
        lane.reveal(f, "M-r1")


def test_c_ml_16_settlement_first_revision_and_push():
    fc = pd.DataFrame([{"shadow_row_id": "a", "event_key": "E1", "family": "HANDICAP", "orientation": "HOME", "line": -3.0},
                       {"shadow_row_id": "b", "event_key": "E1", "family": "TOTAL", "orientation": "OVER", "line": 200.5},
                       {"shadow_row_id": "c", "event_key": "E2", "family": "TOTAL", "orientation": "OVER", "line": 200.5}])
    finals = pd.DataFrame([{"event_key": "E1", "hs": 103, "as_": 100}])
    s = lane.settle_rows(fc, finals, "https://example.invalid/box", "A").set_index("shadow_row_id")
    assert s.loc["a", "result"] == "PUSH" and s.loc["b", "result"] == "WIN"
    assert s.loc["c", "result"] == "UNRESOLVED"  # missing evidence is never VOID or LOSS
    assert set(s["parent_revision"]) == {"NONE"} and set(s["revision"]) == {"revision-1"}
