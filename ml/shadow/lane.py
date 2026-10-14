"""Shadow lane: freeze, reveal and settle (ML_RL_IMPLEMENTATION_FRAMEWORK §6, §9.3; research/model_shadow/README.md).

freeze  -> prices every fixture in a fixtures CSV from ONE event grid per game, writes the forecast CSV OUTSIDE
           the repository, and returns the receipt line (path, bytes, real SHA-256, first start) that is committed
           to FREEZE_RECEIPTS.md BEFORE the first scheduled start.
reveal  -> after that start, copies the file into research/model_shadow/<model>/ only if its SHA-256 still matches
           the committed receipt.
settle  -> appends revision-chained WIN/PUSH/LOSS rows from final scores (CURRENT_RULES §8 R17).
"""
from __future__ import annotations

import csv
import hashlib
import io
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from ml.config import SHADOW_ROOT, League
from ml.data.archive import load_league, snapshot_hash, training_frame
from ml.evaluation.backtest import make_model
from ml.models.baseline import TB1, LeagueBaseline
from ml.models.common import FitError

FORECAST_COLUMNS = [
    "shadow_row_id", "model_id", "model_version", "event_key", "competition", "season", "stage",
    "scheduled_start_utc", "cutoff_utc", "frozen_utc", "endpoint", "family", "orientation", "line",
    "mass_win", "mass_push", "mass_loss", "mass_void", "p_decisive", "mean_home", "mean_away", "sd_margin",
    "sd_total", "cov_home_away", "baseline_p", "baseline_id", "team_baseline_p", "calibration", "inputs_status",
    "label_tier_trained_on", "workshop_commit", "data_snapshot_sha256", "archive_commit", "status",
]
SETTLEMENT_COLUMNS = ["shadow_row_id", "revision", "parent_revision", "effective_utc", "result", "observed_value",
                      "evidence_grade", "source_url", "field", "retrieved_utc", "reason"]
MARKET_MARKERS = ("odds", "moneyline", "spread_line", "total_line", "b365", "psch", "psh", "pinnacle", "betfair",
                  "avgh", "maxh", "implied", "vig", "bookmaker", "price")


class MarketColumnError(ValueError):
    pass


def assert_no_market_columns(columns) -> None:
    """C-ML-07: no column carrying a price or market-derived value may cross into the repository."""
    bad = [c for c in columns if any(m in c.lower().replace(" ", "") for m in MARKET_MARKERS)]
    if bad:
        raise MarketColumnError(f"market-bearing columns refused: {bad}")


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def _fmt(x) -> str:
    if x is None:
        return "N/A"
    if isinstance(x, str):
        return x
    if isinstance(x, (float, np.floating)):
        return "N/A" if not np.isfinite(x) else f"{x:.6f}"
    return str(x)


def freeze(model_id: str, lg: League, params: dict, fixtures: pd.DataFrame, out_dir: Path, model_version: str,
           workshop_commit: str, archive_commit: str, cutoff_utc: str, recent_results: pd.DataFrame | None = None,
           handicap_lines: tuple[float, ...] = (), total_lines: tuple[float, ...] = ()) -> dict:
    """Price ``fixtures`` (columns: event_key, season, stage, scheduled_start_utc, home, away)."""
    assert_no_market_columns(fixtures.columns)
    cutoff = pd.Timestamp(cutoff_utc).tz_convert(None) if pd.Timestamp(cutoff_utc).tzinfo else pd.Timestamp(cutoff_utc)
    games, _ = load_league(lg)
    if recent_results is not None and len(recent_results):
        assert_no_market_columns(recent_results.columns)
        games = pd.concat([games, recent_results], ignore_index=True)
    as_of = cutoff.normalize()
    season = int(fixtures["season"].iloc[0])
    train = training_frame(games)
    train = train[(train["date"] < as_of) & (train["season"] >= season - lg.history_seasons)]
    rows = []
    frozen = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    data_sha = snapshot_hash(lg, sorted(train["season"].unique().tolist()))
    try:
        model = make_model(lg, params)
        model.fit(train, as_of, season) if lg.engine != "gaussian" else model.fit(train, as_of)
        base = LeagueBaseline(lg).fit(train)
        bgrid = base.grid()
        cur = games[(games["season"] == season) & (games["stage"].isin(lg.eval_stages)) & (games["date"] < as_of)]
        earlier = games[(games["season"] < season) & (games["stage"].isin(lg.eval_stages))]
        prev = earlier[earlier["season"] == earlier["season"].max()] if len(earlier) else earlier
        const = TB1.calibrate(lg, prev) if (lg.tb1 is not None and not lg.tb1_label.startswith("VALIDATED")) else None
        tb1 = TB1(lg, const).fit(cur, prev, fallback_games=train) if lg.tb1 else None
        fit_error = None
    except FitError as e:
        fit_error = str(e)
    for f in fixtures.itertuples():
        common = {"model_id": model_id, "model_version": model_version, "event_key": f.event_key,
                  "competition": lg.path, "season": f.season, "stage": f.stage,
                  "scheduled_start_utc": f.scheduled_start_utc, "cutoff_utc": cutoff_utc, "frozen_utc": frozen,
                  "endpoint": lg.endpoint, "calibration": "IDENTITY_INSUFFICIENT_CAL",
                  "label_tier_trained_on": "B",
                  "workshop_commit": workshop_commit, "data_snapshot_sha256": data_sha,
                  "archive_commit": archive_commit}
        if fit_error:
            rows.append({**common, "shadow_row_id": f"{model_id}:{f.event_key}:ALL", "family": "ALL",
                         "status": f"NOT_ISSUED:FIT_FAILED:{fit_error}"})
            continue
        g, flags = model.grid(f.home, f.away)
        s = g.summary()
        inputs = "lineup NOT_USED; " + (";".join(flags) if flags else "no new-team prior")
        pw, pdr, pl = g.winner()
        bw, bd, bl = bgrid.winner()
        contracts = [("MONEYLINE_3WAY" if lg.tie_rule == "draw" else "MONEYLINE_2WAY", "HOME", None,
                      (pw, pdr if lg.tie_rule != "draw" else 0.0, pl + (pdr if lg.tie_rule == "draw" else 0.0)),
                      bw / (bw + bl) if lg.tie_rule != "draw" else bw, tb1.p_home_win(f.home, f.away) if tb1 else None)]
        if lg.tie_rule == "draw":
            contracts.append(("MONEYLINE_3WAY", "DRAW", None, (pdr, 0.0, pw + pl), bd, None))
            contracts.append(("MONEYLINE_3WAY", "AWAY", None, (pl, 0.0, pw + pdr), bl, None))
        for line in handicap_lines:
            m = g.handicap(line, "HOME")
            bm = bgrid.handicap(line, "HOME")
            contracts.append(("HANDICAP", "HOME", line, (m.win, m.push, m.loss), bm.p_decisive, None))
        for line in (total_lines or (base.total_line,)):
            m = g.total(line, "OVER")
            bm = bgrid.total(line, "OVER")
            contracts.append(("TOTAL", "OVER", line, (m.win, m.push, m.loss), bm.p_decisive,
                              tb1.p_over(f.home, f.away, line) if tb1 else None))
        for fam, side, line, (w, p, l), bp, tp in contracts:
            dec = w / (w + l) if (w + l) > 0 else None
            rows.append({**common,
                         "shadow_row_id": f"{model_id}:{f.event_key}:{fam}:{side}:{'NA' if line is None else line}",
                         "family": fam, "orientation": side, "line": "N/A" if line is None else line,
                         "mass_win": w, "mass_push": p, "mass_loss": l, "mass_void": "NOT_ESTIMATED",
                         "p_decisive": "NOT_COMPUTED" if dec is None else dec, **s,
                         "baseline_p": bp, "baseline_id": "BASELINE_LEAGUE_V1",
                         "team_baseline_p": "NOT_COMPUTED" if tp is None else tp,
                         "inputs_status": inputs, "status": "FROZEN"})
    buf = io.StringIO()
    wr = csv.DictWriter(buf, fieldnames=FORECAST_COLUMNS, lineterminator="\n")
    wr.writeheader()
    for r in rows:
        wr.writerow({k: _fmt(r.get(k)) for k in FORECAST_COLUMNS})
    data = buf.getvalue().encode("utf-8")
    first = min(pd.to_datetime(fixtures["scheduled_start_utc"], utc=True))
    week = first.isocalendar()
    name = f"SHADOW_FORECASTS_{week[0]}-W{week[1]:02d}.csv"
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / model_id / name
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise FileExistsError(f"{path} exists; frozen files are never overwritten")
    path.write_bytes(data)
    receipt = (f"| `{name}` | {len(data)} | `{sha256_bytes(data)}` | {first.strftime('%Y-%m-%dT%H:%M:%SZ')} | "
               f"{frozen} | {workshop_commit} | PENDING_START |")
    return {"path": path, "bytes": len(data), "sha256": sha256_bytes(data), "first_start_utc": first,
            "receipt_line": receipt, "rows": len(rows)}


def reveal(csv_path: Path, model_id: str, now_utc: datetime | None = None) -> Path:
    """Copy a frozen file into the repository after its first start, if the committed receipt matches."""
    now_utc = now_utc or datetime.now(timezone.utc)
    data = csv_path.read_bytes()
    digest = sha256_bytes(data)
    rec = (SHADOW_ROOT / model_id / "FREEZE_RECEIPTS.md").read_text(encoding="utf-8")
    line = next((ln for ln in rec.splitlines() if f"`{csv_path.name}`" in ln), None)
    if line is None:
        raise ValueError("no committed receipt for this file")
    if f"`{digest}`" not in line:
        raise ValueError("SHA-256 differs from the committed receipt; the file is not revealed")
    first = pd.Timestamp(line.split("|")[4].strip())
    if now_utc < first.to_pydatetime():
        raise ValueError("first scheduled start has not passed; reveal refused")
    header = data.decode("utf-8").splitlines()[0].split(",")
    assert_no_market_columns(header)
    dest = SHADOW_ROOT / model_id / csv_path.name
    if dest.exists():
        raise FileExistsError(dest)
    dest.write_bytes(data)
    return dest


def settle_rows(forecasts: pd.DataFrame, finals: pd.DataFrame, source_url: str, evidence_grade: str) -> pd.DataFrame:
    """First-revision settlements. ``finals``: event_key, hs, as_ (final at the forecast endpoint)."""
    assert_no_market_columns(finals.columns)
    m = forecasts.merge(finals, on="event_key", how="left")
    out = []
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for r in m.itertuples():
        if pd.isna(getattr(r, "hs", np.nan)):
            res, obs, why = "UNRESOLVED", "N/A", "final score not available"
        else:
            margin, total = r.hs - r.as_, r.hs + r.as_
            fam, side = r.family, r.orientation
            if fam.startswith("MONEYLINE"):
                x = margin if side == "HOME" else (-margin if side == "AWAY" else (1 if margin == 0 else -1))
                res = "WIN" if x > 0 else ("PUSH" if x == 0 and fam == "MONEYLINE_2WAY" else "LOSS")
                obs = f"{int(r.hs)}-{int(r.as_)}"
            elif fam == "HANDICAP":
                x = margin + float(r.line)
                res = "WIN" if x > 0 else ("PUSH" if x == 0 else "LOSS")
                obs = str(int(margin))
            else:
                x = total - float(r.line)
                res = "WIN" if x > 0 else ("PUSH" if x == 0 else "LOSS")
                obs = str(int(total))
            why = "final score"
        out.append({"shadow_row_id": r.shadow_row_id, "revision": "revision-1", "parent_revision": "NONE",
                    "effective_utc": now, "result": res, "observed_value": obs, "evidence_grade": evidence_grade,
                    "source_url": source_url, "field": "final score", "retrieved_utc": now, "reason": why})
    return pd.DataFrame(out, columns=SETTLEMENT_COLUMNS)
