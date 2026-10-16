"""Experimental primary forecasts from a deterministic full-information expert mixture.

PRIMARY_HEDGE_MIX_V3 uses exact-time admitted, weekly out-of-sample warm losses and
verified frozen-bundle feedback, counting each event once. All experts are scored
on common sporting questions; whole grids are mixed into one coherent distribution.
This is online expert aggregation, not a trained environment-control RL agent.
V2 and the earlier random Exp3 approach are retained as historical development.
The old 41,752-game replay is a proxy, not validation of V3's warm/feedback policy.
No market inputs, source-truth certification, calibration or predictive gain implied.
"""
from __future__ import annotations

import argparse
import csv
from dataclasses import fields
import hashlib
import io
import math
from pathlib import Path
import secrets
import subprocess
from datetime import datetime, timezone

import numpy as np
import pandas as pd
import scipy

from ml.config import League, SPORT_RULES, get_league
from ml.core.distributions import ScoreGrid
from ml.evaluation.backtest import make_model
from ml.models.baseline import LeagueBaseline
from ml.models.common import FitError, residual_draw_share
from ml.models.cricket import FirstInningsModel, CricketParams

POLICY = "PRIMARY_HEDGE_MIX_V3"
LEGACY_POLICY = "PRIMARY_HEDGE_MIX_V2"
ARMS = ("RATINGS_FAST", "RATINGS_SLOW", "LEAGUE_BASELINE")
MIX_ARM = "HEDGE_MIX"
WARM_WEEKS = 30          # warm start: the last 30 game-weeks before the cutoff (however far back, e.g. after an off-season)
DEFAULT_ETA = 2.0        # used when the replay table has no row for the competition (labelled in the receipt)
ETA_TABLE = Path(__file__).resolve().parents[1] / "research" / "primary_policy" / "ETA_ADMISSION.csv"


class AdmissionError(ValueError):
    """A required identity, time, source, contract or feedback gate failed."""


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def clock(value) -> pd.Timestamp:
    t = pd.Timestamp(value)
    if pd.isna(t) or t.tzinfo is None:
        raise AdmissionError("timestamp requires an explicit timezone")
    return t.tz_convert("UTC")


def read_rows(path: Path) -> list[dict]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames or len(reader.fieldnames) != len(set(reader.fieldnames)):
            raise AdmissionError("missing/duplicate CSV columns")
        rows = list(reader)
    if any(None in r or any(v is None for v in r.values()) for r in rows):
        raise AdmissionError("malformed CSV row")
    return rows


def csv_bytes(rows: list[dict]) -> bytes:
    if not rows:
        raise AdmissionError("empty output")
    s = io.StringIO(newline="")
    w = csv.DictWriter(s, fieldnames=list(rows[0]), lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    return s.getvalue().encode()


def receipt_file(path, expected: str) -> bytes:
    data = Path(path).read_bytes()
    if digest(data) != expected:
        raise AdmissionError("source/forecast capture hash mismatch")
    return data


def reviewed_source_league(request: dict, row: dict, *, check_evidence=True) -> League:
    """Explicit source-reviewed routing when the local archive is absent or defective.

    This admits competition metadata, never old archive rows or an unsupported engine.
    Sporting source discovery/field review is performed by the research workflow.
    """
    columns = {"sport", "competition", "endpoint", "tie_rule", "extra_fraction", "winner_bonus", "overs_cap",
               "source_url", "available_at", "review_status", "evidence_path", "evidence_sha256",
               "archive_disposition", "reason"}
    if set(row) != columns:
        raise AdmissionError("competition source config requires exact reviewed fields; extra/market columns prohibited")
    sport, competition = row["sport"], row["competition"]
    if not sport.strip() or not competition.strip() or "/" in competition or "\\" in competition or competition in (".", ".."):
        raise AdmissionError("invalid exact competition identity")
    path = sport + "/" + competition
    if path != request["competition"] or row["endpoint"] != request["endpoint"]:
        raise AdmissionError("reviewed competition source scope differs from request")
    rules = SPORT_RULES.get(sport, {})
    if rules.get("engine") not in ("gaussian", "count", "dixon_coles", "cricket"):
        raise AdmissionError("unsupported sport engine; online data does not create a primary adapter")
    if row["endpoint"] != rules["endpoint"] or row["tie_rule"] != rules.get("tie_rule", "draw"):
        raise AdmissionError("reviewed format/endpoint requires an unsupported adapter")
    horizon, _ = information_horizon(request)
    if row["review_status"] != "RESEARCH_INPUT_REVIEWED" or not row["source_url"].startswith("https://") or clock(row["available_at"]) > horizon:
        raise AdmissionError("competition metadata requires reviewed source evidence known by the horizon")
    if row["archive_disposition"] not in ("MISSING", "INCOMPLETE", "INCORRECT") or not row["reason"].strip():
        raise AdmissionError("declare the actual archive defect and source-recovery reason")
    if check_evidence:
        receipt_file(row["evidence_path"], row["evidence_sha256"])
    extra, bonus = float(row["extra_fraction"]), float(row["winner_bonus"])
    if not math.isfinite(extra) or not 0 <= extra <= 1 or not math.isfinite(bonus) or bonus != rules.get("winner_bonus", 1):
        raise AdmissionError("invalid or unsupported competition extra-time configuration")
    needs_extra = row["tie_rule"] in ("overtime", "overtime_residual")
    if (needs_extra and extra <= 0) or (not needs_extra and extra != 0):
        raise AdmissionError("extra-time fraction incompatible with reviewed tie rule")
    cap = float(row["overs_cap"]) if row["overs_cap"] else None
    if rules["engine"] == "cricket":
        if cap is None or not math.isfinite(cap) or cap != rules["overs_cap"]:
            raise AdmissionError("unsupported cricket innings format")
    elif cap is not None:
        raise AdmissionError("non-cricket competition cannot declare overs")
    return League(path, sport, competition, "SOURCE_REVIEWED:" + path, rules["engine"],
                  endpoint=row["endpoint"], tie_rule=row["tie_rule"], extra_fraction=extra,
                  winner_bonus=int(bonus), negbin=rules.get("negbin", False), overs_cap=cap)


def admit_history(rows: list[dict], cutoff, target: str, competition: str, endpoint: str) -> pd.DataFrame:
    """Source custody is checked, never represented as field-owner certification."""
    limit = clock(cutoff)
    checked = set()
    identities = set()
    records = []
    for r in rows:
        if r.get("source_kind", "") not in ("", "ARCHIVE_REVIEWED", "WEB_RECOVERED", "WEB_CORRECTED"):
            raise AdmissionError("unknown historical source kind")
        if r["competition"] != competition or r["endpoint"] != endpoint or r["event_id"] == target or r["event_id"] in identities:
            raise AdmissionError("wrong scope, target event leakage or duplicate training event")
        identities.add(r["event_id"])
        date, final, known = clock(r["date"]), clock(r["final_at"]), clock(r["available_at"])
        if not date <= final <= known <= limit or not date < limit.normalize():
            raise AdmissionError("training event/final/source not known by the information horizon (game-log scheduled start); same-day rows excluded")
        if r["status"] != "FINAL" or r["admission"] != "RESEARCH_INPUT_REVIEWED" or not r["source_url"].startswith("https://"):
            raise AdmissionError("terminal/source review receipt required")
        token = (r["evidence_path"], r["evidence_sha256"])
        if token not in checked:
            receipt_file(*token)
            checked.add(token)
        rec = {"date": date.tz_localize(None), "event_id": r["event_id"], "season": int(r["season"]),
               "final_at": final.tz_localize(None), "available_at": known.tz_localize(None),
               "home": r["home"], "away": r["away"], "decision": r["decision"], "stage": r.get("stage", "REG")}
        if not rec["home"].strip() or not rec["away"].strip() or rec["home"] == rec["away"]:
            raise AdmissionError("invalid training participants")
        for col in ("hs", "as_", "reg_hs", "reg_as"):
            value = float(r[col])
            if not math.isfinite(value) or value < 0 or value != int(value):
                raise AdmissionError("training scores must be nonnegative integers")
            rec[col] = int(value)
        if rec["reg_hs"] > rec["hs"] or rec["reg_as"] > rec["as_"]:
            raise AdmissionError("regulation score exceeds final score")
        from ml.endpoint import regulation_pair
        try:
            regulation_pair(r)
        except ValueError as exc:
            raise AdmissionError(str(exc)) from exc
        # Cricket fields are explicit; no conversion from match winner/total to an innings label.
        for col in ("bat", "bowl", "venue", "legal_balls", "wickets"):
            rec[col] = r.get(col, "")
        if r.get("runs", ""):
            rec["runs"] = float(r["runs"])
            if not math.isfinite(rec["runs"]) or rec["runs"] < 0 or rec["runs"] != int(rec["runs"]):
                raise AdmissionError("invalid first innings runs")
        records.append(rec)
    if not records:
        raise AdmissionError("no admitted history")
    return pd.DataFrame(records).sort_values(["date", "event_id"]).reset_index(drop=True)


def form_rows(train: pd.DataFrame, home: str, away: str, cricket=False) -> list[dict]:
    rows = []
    for team in (home, away):
        games = train[(train.home == team) | (train.away == team)].sort_values("date", ascending=False)
        for n in (5, 10, 15, 20):
            recent = games.head(n)
            if cricket:
                # First-innings-only history cannot supply either team's chase
                # score. Do not present the auxiliary zero as a bowling result.
                scored = recent.loc[recent.bat == team, "runs"].to_numpy()
                conceded = recent.loc[recent.bowl == team, "runs"].to_numpy()
            else:
                scored = np.where(recent.home == team, recent.hs, recent.as_)
                conceded = np.where(recent.home == team, recent.as_, recent.hs)
            rows.append(dict(team=team, window=f"L{n}", n=len(recent),
                             scored_n=len(scored), conceded_n=len(conceded),
                             scored_mean=float(np.mean(scored)) if len(scored) else "NOT_COMPUTED",
                             conceded_mean=float(np.mean(conceded)) if len(conceded) else "NOT_COMPUTED"))
    return rows


def _check_scope(lg: League, train: pd.DataFrame) -> None:
    if lg.data_warnings:
        raise AdmissionError("competition DATA_HOLD: " + ";".join(lg.data_warnings))
    if lg.engine not in ("gaussian", "count", "dixon_coles", "cricket"):
        raise AdmissionError("unsupported exact sport/endpoint; no major-league substitution")
    if lg.engine == "cricket":
        if lg.endpoint != "FIRST_INNINGS_FULL_LENGTH" or not all(c in train for c in ("runs", "bat", "bowl", "venue")):
            raise AdmissionError("cricket requires exact full-length first-innings labels; phases unsupported")
        balls = pd.to_numeric(train.legal_balls, errors="coerce")
        wickets = pd.to_numeric(train.wickets, errors="coerce")
        cap = float(lg.overs_cap) * 6
        if not (balls.between(0, cap) & wickets.between(0, 10) & balls.eq(np.floor(balls)) & wickets.eq(np.floor(wickets)) &
                (balls.eq(cap) | wickets.eq(10))).all():
            raise AdmissionError("short/unknown-length innings cannot train a full-innings endpoint")
        if not (train.home.eq(train.bat) & train.away.eq(train.bowl) & train.hs.eq(train.runs) & train.as_.eq(0)).all():
            raise AdmissionError("innings coordinates must be batting runs versus zero auxiliary; home=bat, away=bowl")


def _fit_models(lg: League, train: pd.DataFrame, as_of: pd.Timestamp):
    """Fit the three experts once; return {arm: pricer(home, away, venue) -> (grid, flags)} and the league line.

    Identical fitting to PRIMARY_EXP3_V1: regulation scores for non-draw endpoints (extras added once by the tie rule),
    final labels for the extra-time winner and residual draw share, fixed predeclared recipes.
    """
    fitting = train.copy()
    if lg.tie_rule != "draw" and lg.engine != "cricket":
        fitting["hs"], fitting["as_"] = train.reg_hs, train.reg_as

    def final_labels(model):
        if hasattr(model, "residual_draw") and hasattr(model, "sd_margin"):
            model.residual_draw = residual_draw_share(train, model.sd_margin)
        if hasattr(model, "p_home_extra"):
            extra = train[train.decision.isin(["Overtime", "Shootout", "EXTRAS"])]
            model.p_home_extra = float((extra.hs > extra.as_).mean()) if len(extra) >= 20 else .5
        return model

    pricers = {}
    if lg.engine == "cricket":
        for arm, days in zip(ARMS[:2], (90.0, 365.0)):
            m = FirstInningsModel("C2", CricketParams(days, 20.0, 20.0, 1.1)).fit(train, as_of)
            pricers[arm] = (lambda m: lambda h, a, v="": (ScoreGrid(m.pmf(h, a, v)[:, None]), []))(m)
        base = FirstInningsModel("C0", CricketParams(365.0, 20.0, 20.0, 1.1)).fit(train, as_of)
        pricers[ARMS[2]] = lambda h, a, v="": (ScoreGrid(base.pmf(h, a, v)[:, None]), [])
        return pricers, float(base.line)
    for arm, days in zip(ARMS[:2], (90.0, 365.0)):
        params = dict(half_life_days=days, ridge=8.0)
        if lg.engine == "gaussian":
            params["cov_inflation"] = 1.1
        model = make_model(lg, params)
        model.fit(fitting, as_of) if lg.engine == "gaussian" else model.fit(fitting, as_of, int(train.season.max()))
        final_labels(model)
        pricers[arm] = (lambda m: lambda h, a, v="": m.grid(h, a))(model)
    base = final_labels(LeagueBaseline(lg).fit(fitting))
    bgrid = base.grid()
    pricers[ARMS[2]] = lambda h, a, v="": (bgrid, [])
    return pricers, float(base.total_line)


def expert_loss(grid: ScoreGrid, hs: int, as_: int, line: float, cricket: bool) -> float:
    """Common-question loss for weighting: mean Brier of P(home wins) and P(total over the league line).

    Cricket first innings: Brier of P(runs over the league line) only (the auxiliary zero has no winner meaning).
    """
    y_over = float(hs + as_ > line)
    p_over = grid.total(line, "OVER").win
    if cricket:
        return (p_over - y_over) ** 2
    y_home = float(hs > as_)
    return 0.5 * ((grid.winner()[0] - y_home) ** 2 + (p_over - y_over) ** 2)


def warm_records(lg: League, train: pd.DataFrame, as_of: pd.Timestamp, excluded=()) -> list[dict]:
    """Every expert's summed loss on the admitted games of the last WARM_WEEKS game-weeks before the cutoff.

    Each game is priced by experts refitted on games strictly before the Monday of its week. Weeks with fewer than
    30 earlier games or a failed fit are skipped. Unseen teams are skipped (as at issue).
    """
    cricket = lg.engine == "cricket"
    if not {"available_at", "final_at"}.issubset(train):
        raise AdmissionError("warm replay requires field known-at/final times, not game dates alone")
    train = train[train.date < as_of.normalize()]  # strictly earlier calendar days, whatever the caller passes
    if train.empty:
        return []
    starts = (train.date.dt.normalize() - pd.to_timedelta(train.date.dt.weekday, unit="D"))
    recent = train
    rows = []
    for ws in sorted(starts.unique())[-WARM_WEEKS:]:
        ws = pd.Timestamp(ws)
        earlier = train[(train.date < ws) & (train.available_at <= ws) & (train.final_at <= ws)]
        if len(earlier) < 30:
            continue
        try:
            pricers, line = _fit_models(lg, earlier, ws)
        except FitError:
            continue
        known = set(earlier.home) | set(earlier.away)
        week = recent[(starts == ws) & recent.home.isin(known) & recent.away.isin(known) & ~recent.event_id.isin(excluded)]
        for g in week.itertuples():
            losses = []
            try:
                for arm in ARMS:
                    grid, flags = pricers[arm](g.home, g.away, getattr(g, "venue", "") or "")
                    if flags:
                        break  # No partial vector or flagged expert can train the mixture.
                    losses.append(expert_loss(grid, int(g.hs), int(g.as_), line, cricket))
            except FitError:
                continue
            if len(losses) != len(ARMS):
                continue
            rows.append(dict(event_id=g.event_id, refit_at=ws.tz_localize("UTC").isoformat(), available_at=g.available_at.tz_localize("UTC").isoformat(),
                             league_line=line, **{"loss_" + a: v for a, v in zip(ARMS, losses)}))
    return rows


def loss_sum(rows: list[dict]) -> np.ndarray:
    values = np.array([[float(r["loss_" + a]) for a in ARMS] for r in rows], dtype=float).reshape(-1, len(ARMS))
    if not np.isfinite(values).all() or np.any((values < 0) | (values > 1)):
        raise AdmissionError("expert losses must be finite values in [0,1]")
    return values.sum(axis=0)


def warm_start(lg: League, train: pd.DataFrame, as_of: pd.Timestamp) -> tuple[np.ndarray, int]:
    rows = warm_records(lg, train, as_of)
    return loss_sum(rows), len(rows)


def mix_grids(grids: list[ScoreGrid], weights) -> ScoreGrid:
    """Weighted mixture of complete score grids on their union support: a valid joint distribution."""
    w = np.asarray(weights, float)
    if not grids or w.ndim != 1 or len(w) != len(grids) or not np.isfinite(w).all() or np.any(w < 0) or abs(w.sum() - 1) > 1e-9:
        raise AdmissionError("mixture weights must be a probability vector over the experts")
    h0 = min(g.h0 for g in grids)
    a0 = min(g.a0 for g in grids)
    h1 = max(g.h0 + g.p.shape[0] for g in grids)
    a1 = max(g.a0 + g.p.shape[1] for g in grids)
    if (h1-h0) * (a1-a0) > 2_000_000:
        raise AdmissionError("unreasonable union-grid dimensions")
    out = np.zeros((h1 - h0, a1 - a0))
    for wi, g in zip(w, grids):
        out[g.h0 - h0:g.h0 - h0 + g.p.shape[0], g.a0 - a0:g.a0 - a0 + g.p.shape[1]] += wi * g.p
    return ScoreGrid(out / out.sum(), h0, a0)


def hedge_weights(cumulative: np.ndarray, eta: float) -> np.ndarray:
    cumulative = np.asarray(cumulative, float)
    if cumulative.shape != (len(ARMS),) or not np.isfinite(cumulative).all() or np.any(cumulative < 0) or not math.isfinite(eta) or eta <= 0:
        raise AdmissionError("finite nonnegative cumulative losses and positive finite eta required")
    z = -eta * (cumulative - np.min(cumulative))
    e = np.exp(z)
    return e / e.sum()


def eta_for(lg: League, horizon=None) -> tuple[float, str, str]:
    """Only an exact-policy, point-in-time admitted parameter can override the provisional default.

    A development results table does not admit its tuned parameters to a different warm/feedback policy.
    """
    if not ETA_TABLE.exists():
        return DEFAULT_ETA, "DEFAULT_NO_ADMITTED_TABLE", "NONE"
    data = ETA_TABLE.read_bytes()
    table = pd.read_csv(io.BytesIO(data))
    needed = {"competition", "policy", "eta", "tune_end", "frozen_at", "evidence_path", "evidence_sha256"}
    if set(table.columns) != needed:
        raise AdmissionError("eta admission table requires exact policy/timing/evidence fields; extra/market columns prohibited")
    row = table[(table.competition == lg.path) & (table.policy == POLICY)]
    if row.empty:
        return DEFAULT_ETA, "DEFAULT_NO_ADMITTED_ROW", digest(data)
    if len(row) != 1:
        raise AdmissionError("conflicting eta admission rows")
    r = row.iloc[0]
    value = float(r.eta)
    if not math.isfinite(value) or value <= 0 or clock(r.tune_end) > clock(r.frozen_at):
        raise AdmissionError("invalid eta or tuning/freeze chronology")
    if horizon is None or clock(r.frozen_at) > clock(horizon):
        return DEFAULT_ETA, "DEFAULT_PARAMETER_NOT_KNOWN_AT_HORIZON", digest(data)
    receipt_file(r.evidence_path, r.evidence_sha256)
    return value, "ADMITTED_EXACT_POLICY_PARAMETER", digest(data)


def fit_experts(lg: League, train: pd.DataFrame, cutoff, home: str, away: str, venue=""):
    """The three experts' grids for one event, with every PRIMARY_EXP3_V1 admission gate unchanged."""
    grids, _ = fit_experts_and_line(lg, train, cutoff, home, away, venue)
    return grids


def fit_experts_and_line(lg: League, train: pd.DataFrame, cutoff, home: str, away: str, venue=""):
    as_of = clock(cutoff).tz_localize(None)
    _check_scope(lg, train)
    if home not in set(train.home) | set(train.away) or away not in set(train.home) | set(train.away):
        raise AdmissionError("unseen participant: no silent prior as a primary model")
    pricers, line = _fit_models(lg, train, as_of)
    experts = {}
    for arm in ARMS:
        grid, flags = pricers[arm](home, away, venue)
        if flags:
            raise AdmissionError("primary model flags require review: " + ";".join(flags))
        experts[arm] = grid
    return experts, line


def price(grid: ScoreGrid, contract: dict, endpoint: str) -> tuple[float, float, float]:
    if contract["endpoint"] != endpoint or contract["definition"] != "FROZEN_FRAMEWORK_CONVENTION":
        raise AdmissionError("endpoint/action definition mismatch")
    family, side = contract["family"], contract["side"]
    if endpoint == "FIRST_INNINGS_FULL_LENGTH" and family != "total":
        raise AdmissionError("innings model cannot price match winner/handicap/powerplay")
    if family == "winner":
        probs = grid.winner()
        if side not in ("HOME", "DRAW", "AWAY"):
            raise AdmissionError("unknown winner side")
        win = probs[("HOME", "DRAW", "AWAY").index(side)]
        if contract["action"] == "DRAW_PUSH" and side != "DRAW":
            return win, probs[1], max(0., 1 - win - probs[1])
        if contract["action"] != "THREE_WAY_DRAW_LOSES":
            raise AdmissionError("winner requires frozen draw-action semantics")
        return win, 0.0, 1 - win
    if family not in ("handicap", "total"):
        raise AdmissionError("unsupported contract family")
    if contract["action"] != "STANDARD_COMPLETED":
        raise AdmissionError("unknown handicap/total action")
    line = float(contract["line"])
    masses = getattr(grid, family)(line, side)
    return masses.win, masses.push, masses.loss


def _parse_vector(text: str) -> dict:
    out = {}
    for part in text.split(";"):
        name, value = part.split(":", 1)
        if name in out:
            raise AdmissionError("duplicate expert vector key")
        out[name] = float(value)
    if set(out) != set(ARMS) or not all(math.isfinite(v) for v in out.values()):
        raise AdmissionError("frozen expert vector must name exactly the three experts")
    return out


def feedback_losses(feedback: list[dict], context: str, before, *, return_rows=False):
    """Full-information delayed feedback: every expert's frozen loss on earlier settled bundles of this context.

    A row counts only if it was available before ``before``; it is re-derived from the hash-verified bundle and the
    evidence-backed final, so a row cannot carry an invented loss.
    """
    admitted = []
    seen = set()
    for row in feedback:
        if row["event_id"] in seen:
            raise AdmissionError("duplicate/revision-conflicting feedback; resolve to one effective row")
        seen.add(row["event_id"])
        if row.get("record_kind") == "RESEARCH_TRAINING_CANDIDATE" or "label_key" in row:
            raise AdmissionError("research settlement targets are not frozen expert feedback; use future training admission")
        if clock(row["available_at"]) > clock(before):
            continue  # Future feedback cannot change today's weights.
        receipt_file(row["bundle"] + "/RECEIPT.csv", row["receipt_sha256"])
        rec = verify_bundle(Path(row["bundle"]))
        if rec["event_id"] != row["event_id"] or rec["context"] != row["context"]:
            raise AdmissionError("feedback identity/context differs from frozen forecast")
        if row["context"] != context:
            continue
        if not clock(rec["issue_at"]) < clock(row["final_at"]) <= clock(row["available_at"]):
            raise AdmissionError("feedback was not observable after actual issue/final")
        expected = settle(Path(row["bundle"]), float(row["home_score"]), float(row["away_score"]),
                          row["final_at"], row["available_at"], row["evidence_path"], row["evidence_sha256"])
        losses = []
        for arm in ARMS:
            value = float(row["loss_" + arm])
            if not math.isfinite(value) or abs(float(expected["loss_" + arm]) - value) > 1e-12:
                raise AdmissionError("feedback loss differs from the frozen expert grids and evidence final")
            losses.append(value)
        admitted.append(dict(event_id=row["event_id"], available_at=row["available_at"],
                             receipt_sha256=row["receipt_sha256"],
                             **{"loss_" + a: v for a, v in zip(ARMS, losses)}))
    return admitted if return_rows else (loss_sum(admitted), len(admitted))


def _load_grids(folder: Path) -> dict:
    grids = {}
    state_rows = read_rows(folder / "GRIDS.csv")
    if set(r["arm"] for r in state_rows) != set(ARMS):
        raise AdmissionError("unknown/missing expert in frozen grids")
    for arm in ARMS:
        cells = [r for r in state_rows if r["arm"] == arm]
        points = [(int(r["home"]), int(r["away"])) for r in cells]
        if not points or len(set(points)) != len(points) or any(min(p) < 0 for p in points):
            raise AdmissionError("duplicate/missing/invalid state-grid cells")
        h0, a0 = min(p[0] for p in points), min(p[1] for p in points)
        shape = (max(p[0] for p in points) - h0 + 1, max(p[1] for p in points) - a0 + 1)
        if shape[0] * shape[1] > 2_000_000:
            raise AdmissionError("unreasonable state-grid dimensions")
        masses = np.zeros(shape)
        for r, (h, a) in zip(cells, points):
            masses[h-h0, a-a0] = float(r["mass"])
        grids[arm] = ScoreGrid(masses, h0, a0)
    return grids


def verify_bundle(folder: Path) -> dict:
    rows = read_rows(folder / "RECEIPT.csv")
    if len(rows) != 1 or rows[0]["policy"] not in (POLICY, LEGACY_POLICY):
        raise AdmissionError("unknown bundle policy/receipt")
    rec = rows[0]
    if rec.get("competition_source_sha256"):
        receipt_file(folder / "COMPETITION_SOURCE.csv", rec["competition_source_sha256"])
        source = read_rows(folder / "COMPETITION_SOURCE.csv")
        request = read_rows(folder / "REQUEST.csv")
        if len(source) != 1 or len(request) != 1:
            raise AdmissionError("exactly one frozen competition source/request required")
        reviewed = reviewed_source_league(request[0], source[0], check_evidence=False)
        frozen = read_rows(folder / "MODEL_CONFIG.csv")
        if len(frozen) != 1 or any(frozen[0][f.name] != repr(getattr(reviewed, f.name)) for f in fields(reviewed)):
            raise AdmissionError("reviewed competition source differs from frozen model config")
    if "history_web_rows" in rec:
        history = read_rows(folder / "HISTORY.csv")
        counts = (sum(r.get("source_kind") in ("WEB_RECOVERED", "WEB_CORRECTED") for r in history),
                  sum(r.get("source_kind") == "ARCHIVE_REVIEWED" for r in history), sum(not r.get("source_kind") for r in history))
        if counts != tuple(int(rec[k]) for k in ("history_web_rows", "history_archive_rows", "history_unspecified_rows")):
            raise AdmissionError("history source coverage differs from frozen inputs")
    for name in ("PREDICTIONS", "GRIDS", "FORMS", "HISTORY", "CONTRACTS", "REQUEST", "FEEDBACK_INPUT", "MODEL_CONFIG"):
        receipt_file(folder / (name + ".csv"), rec[name.lower() + "_sha256"])
    if rec["policy"] == POLICY:
        for name in ("WARM_START", "FEEDBACK_LOSSES", "ETA_ADMISSION"):
            receipt_file(folder / (name + ".csv"), rec[name.lower() + "_sha256"])
        warm, fb = read_rows(folder / "WARM_START.csv"), read_rows(folder / "FEEDBACK_LOSSES.csv")
        ids = [r["event_id"] for r in warm + fb]
        if len(ids) != len(set(ids)) or rec["event_id"] in ids:
            raise AdmissionError("duplicate/target event in learning ledgers")
        if len(warm) != int(rec["warm_start_games"]) or len(fb) != int(rec["feedback_events"]):
            raise AdmissionError("learning ledger counts differ from receipt")
        cumulative = _parse_vector(rec["cumulative_losses"])
        if not np.allclose(loss_sum(warm + fb), [cumulative[a] for a in ARMS], atol=1e-12, rtol=0):
            raise AdmissionError("cumulative losses differ from frozen learning ledgers")
        request_rows = read_rows(folder / "REQUEST.csv")
        if len(request_rows) != 1:
            raise AdmissionError("one frozen request required")
        request = request_rows[0]
        horizon, basis = information_horizon(request)
        if any(rec[k] != request[k] for k in ("event_id", "competition", "endpoint")) or clock(rec["information_horizon"]) != horizon or rec["horizon_source"] != basis:
            raise AdmissionError("receipt identity/horizon differs from frozen request")
        if any(clock(r["available_at"]) > horizon for r in warm + fb):
            raise AdmissionError("future evidence in frozen learning ledgers")
        if not math.isfinite(float(rec["league_line"])):
            raise AdmissionError("finite frozen league line required")
        if rec["eta_table_sha256"] != "NONE" and rec["eta_table_sha256"] != rec["eta_admission_sha256"]:
            raise AdmissionError("eta table changed during inference")
    if rec["selected_arm"] != MIX_ARM:
        raise AdmissionError("primary distribution must be the frozen expert mixture")
    weights = _parse_vector(rec["mixture_weights"])
    cumulative = _parse_vector(rec["cumulative_losses"])
    w = np.array([weights[a] for a in ARMS])
    if np.any(w < 0) or abs(w.sum() - 1) > 1e-12:
        raise AdmissionError("frozen mixture weights are not a probability vector")
    recomputed = hedge_weights(np.array([cumulative[a] for a in ARMS]), float(rec["eta"]))
    if np.max(np.abs(recomputed - w)) > 1e-12:
        raise AdmissionError("mixture weights differ from the frozen losses and learning rate")
    grids = _load_grids(folder)
    mix = mix_grids([grids[a] for a in ARMS], w)
    for row in read_rows(folder / "PREDICTIONS.csv"):
        win, push, loss = price(mix, row, rec["endpoint"])
        if not all(math.isfinite(float(row[k])) and 0 <= float(row[k]) <= 1 for k in ("win", "push", "loss")):
            raise AdmissionError("invalid frozen W/P/L masses")
        if max(abs(win-float(row["win"])), abs(push-float(row["push"])), abs(loss-float(row["loss"]))) > 1e-10:
            raise AdmissionError("issued row not derived from frozen expert mixture")
        expected = win/(win+loss) if win+loss > 0 else "NOT_COMPUTED"
        if expected != "NOT_COMPUTED" and abs(float(row["p_card"]) - expected) > 1e-10:
            raise AdmissionError("decisive probability differs from frozen W/P/L")
        bw, _, bl = price(grids[ARMS[2]], row, rec["endpoint"])
        baseline = bw/(bw+bl) if bw+bl > 0 else "NOT_COMPUTED"
        for name, value in (("p_card", expected), ("baseline_p", baseline)):
            if value == "NOT_COMPUTED":
                valid = row[name] == value
            else:
                valid = math.isfinite(float(row[name])) and abs(float(row[name])-value) <= 1e-10
            if not valid:
                raise AdmissionError(name + " differs from frozen probability grid")
    return rec


def settle(folder: Path, home_score: int, away_score: int, final_at, available_at,
           evidence_path, evidence_sha256) -> dict:
    """Score every frozen expert on the common questions (full information) and the issued top two (diagnostic)."""
    rec = verify_bundle(folder)
    if any(not math.isfinite(s) or s < 0 or s != int(s) for s in (home_score, away_score)):
        raise AdmissionError("invalid final score")
    cricket = rec["endpoint"] == "FIRST_INNINGS_FULL_LENGTH"
    if cricket and away_score != 0:
        raise AdmissionError("first-innings settlement uses batting runs and a zero auxiliary coordinate")
    if not clock(rec["issue_at"]) < clock(final_at) <= clock(available_at):
        raise AdmissionError("terminal feedback before issue/final")
    receipt_file(evidence_path, evidence_sha256)
    grids = _load_grids(folder)
    line = float(rec["league_line"])
    expert = {"loss_" + arm: expert_loss(grids[arm], int(home_score), int(away_score), line, cricket) for arm in ARMS}
    primary = []
    final = ScoreGrid(np.ones((1, 1)), home_score, away_score)
    for row in read_rows(folder / "PREDICTIONS.csv"):
        if row["rank"] not in ("1", "2"):
            continue
        win, push, loss = price(final, row, rec["endpoint"])
        if push == 1:
            continue
        primary.append((float(row["p_card"]) - win) ** 2)
    return dict(event_id=rec["event_id"], context=rec["context"], **expert,
                primary_top2_brier=float(np.mean(primary)) if primary else "NOT_COMPUTED",
                home_score=int(home_score), away_score=int(away_score), final_at=clock(final_at).isoformat(),
                available_at=clock(available_at).isoformat(), bundle=str(folder.resolve()),
                receipt_sha256=digest((folder / "RECEIPT.csv").read_bytes()),
                evidence_path=str(Path(evidence_path).resolve()), evidence_sha256=evidence_sha256)


def information_horizon(request: dict) -> tuple[pd.Timestamp, str]:
    """The latest instant whose information may enter the forecast: there is no separate cutoff.

    It is the game's scheduled (expected) start as recorded in the game log, so lineups, confirmed starters,
    bench and news are researched up to then. It moves earlier only when the forecast was issued earlier
    (nothing after the issue can have been used) or play verifiably began earlier than scheduled.
    """
    if "cutoff" in request:
        raise AdmissionError("no separate cutoff: supply scheduled_start (the expected start in the game log)")
    if not str(request.get("scheduled_start", "")).strip():
        raise AdmissionError("scheduled_start from the game log is required; it is the information horizon")
    bounds = [(clock(request["scheduled_start"]), "SCHEDULED_START"), (clock(request["issue_at"]), "ISSUE_AT")]
    if request.get("actual_start"):
        bounds.append((clock(request["actual_start"]), "ACTUAL_START"))
    horizon, source = min(bounds, key=lambda b: b[0])  # ties resolve to the scheduled start (listed first)
    return horizon, source


def forecast(request: dict, lg: League | None, history: list[dict], contracts: list[dict], output: Path,
             feedback: list[dict] | None = None, rng=None, *, competition_source: list[dict] | None = None) -> dict:
    """``rng`` is accepted for call compatibility and ignored: the V3 primary distribution is deterministic."""
    generating_code = source_hash()
    allowed_request = {"event_id", "competition", "home", "away", "scheduled_start", "issue_at", "actual_start", "endpoint", "venue", "outcome_exposure", "candidate_recipe"}
    if "cutoff" in request:
        raise AdmissionError("no separate cutoff: supply scheduled_start (the expected start in the game log)")
    allowed_history = {"event_id", "competition", "endpoint", "date", "final_at", "available_at", "status", "admission", "source_url", "evidence_path", "evidence_sha256", "source_kind", "season", "home", "away", "hs", "as_", "reg_hs", "reg_as", "decision", "stage", "bat", "bowl", "venue", "runs", "legal_balls", "wickets"}
    allowed_contract = {"contract_key", "family", "side", "line", "endpoint", "definition", "action"}
    if set(request) - allowed_request or any(set(r) - allowed_history for r in history) or any(set(r) - allowed_contract for r in contracts):
        raise AdmissionError("unregistered input columns (including market fields) are prohibited")
    if request["home"] == request["away"] or not request["event_id"].strip():
        raise AdmissionError("invalid identity")
    cutoff, horizon_source = information_horizon(request)  # 'cutoff' below = this horizon, never a separate time
    if competition_source is not None:
        if len(competition_source) != 1:
            raise AdmissionError("exactly one reviewed competition source configuration required")
        lg = reviewed_source_league(request, competition_source[0])
    if lg is None:
        raise AdmissionError("competition configuration missing: research exact metadata from sporting sources")
    issue = clock(request["issue_at"])
    if request["competition"] != lg.path or request["endpoint"] != lg.endpoint:
        raise AdmissionError("request/competition model scope mismatch")
    if lg.sport == "Baseball" and lg.endpoint == "FULL_GAME_INCL_EXTRAS":
        raise AdmissionError("BASEBALL_FINAL_ENDPOINT_REQUIRES_CYCLE_V1: legacy uncensored nine-inning winner/extras model is retired for new full-game forecasts")
    if request.get("outcome_exposure", "") != "NONE_RECORDED":
        raise AdmissionError("outcome-exposed full-event primary forecast blocked")
    start = clock(request["actual_start"]) if request.get("actual_start") else None
    phase = "TIMING_UNVERIFIED" if start is None else ("PREGAME" if issue < start else "POST_START_ISSUE")
    train = admit_history(history, cutoff, request["event_id"], lg.path, lg.endpoint)
    if competition_source is not None and any(not r.get("source_kind") for r in history):
        raise AdmissionError("reviewed source route requires each history row labelled ARCHIVE_REVIEWED, WEB_RECOVERED or WEB_CORRECTED")
    experts, line = fit_experts_and_line(lg, train, cutoff, request["home"], request["away"], request.get("venue", ""))
    forms = form_rows(train, request["home"], request["away"], cricket=lg.engine == "cricket")
    coverage = "SHORT" if min(int(r["n"]) for r in forms if r["window"] == "L20") < 20 else "FULL20"
    recipe = request.get("candidate_recipe", "")
    if not recipe.strip():
        raise AdmissionError("freeze a candidate recipe ID before pricing")
    # Expert losses on common questions are comparable across recipes, coverage and timing phases, so the
    # full-information context pools them per competition and endpoint (V1's finer partition starved learning).
    context = f"{POLICY}|{lg.path}|{lg.endpoint}"
    if any(r["event_id"] == request["event_id"] for r in (feedback or [])):
        raise AdmissionError("target feedback cannot enter its own prediction")
    fb_rows = feedback_losses(feedback or [], context, cutoff, return_rows=True)
    fb_ids = {r["event_id"] for r in fb_rows}
    for row in feedback or []:
        if row["event_id"] not in fb_ids:
            continue
        same = train[train.event_id == row["event_id"]]
        if len(same) and (float(row["home_score"]) != same.iloc[0].hs or float(row["away_score"]) != same.iloc[0].as_):
            raise AdmissionError("history/feedback score conflict; reconcile effective settlement first")
        if len(same):
            original = read_rows(Path(row["bundle"]) / "REQUEST.csv")[0]
            if any(same.iloc[0][k] != original[k] for k in ("home", "away")):
                raise AdmissionError("history/feedback participant orientation conflict")
    warm_rows = warm_records(lg, train, cutoff.tz_localize(None), excluded=fb_ids)
    n_warm, n_fb = len(warm_rows), len(fb_rows)
    cumulative = loss_sum(warm_rows + fb_rows)
    eta, eta_source, eta_sha = eta_for(lg, cutoff)
    weights = hedge_weights(cumulative, eta)
    grid = mix_grids([experts[a] for a in ARMS], weights)
    if not contracts or len({r["contract_key"] for r in contracts}) != len(contracts):
        raise AdmissionError("empty candidate slate or duplicate contract keys")
    priced = []
    semantics = set()
    for contract in contracts:
        if not contract["contract_key"].strip():
            raise AdmissionError("empty contract key")
        win, push, loss = price(grid, contract, lg.endpoint)
        semantic = (contract["family"], contract["side"], float(contract["line"]) if contract["family"] != "winner" else None, contract["endpoint"], contract["action"])
        if semantic in semantics:
            raise AdmissionError("duplicate semantic contract under another key")
        semantics.add(semantic)
        baseline = price(experts[ARMS[2]], contract, lg.endpoint)
        pc = win / (win + loss) if win + loss > 0 else None
        bp = baseline[0] / (baseline[0] + baseline[2]) if baseline[0] + baseline[2] > 0 else "NOT_COMPUTED"
        priced.append(dict(contract_key=contract["contract_key"], family=contract["family"], side=contract["side"],
                           line=contract["line"], endpoint=lg.endpoint, definition=contract["definition"], action=contract["action"],
                           win=win, push=push, loss=loss, p_card=pc if pc is not None else "NOT_COMPUTED",
                           baseline_p=bp, selected_arm=MIX_ARM, rank="", role="DIAGNOSTIC"))
    eligible = [r for r in priced if isinstance(r["p_card"], float) and r["p_card"] <= .90]
    eligible.sort(key=lambda r: (-r["p_card"], r["contract_key"]))
    while eligible and lg.sport == "Baseball" and eligible[0]["family"] == "handicap" and float(eligible[0]["line"]) == 1.5 and eligible[0]["p_card"] < .65:
        eligible.pop(0)["role"] = "INELIGIBLE_RANK1_BASEBALL_PLUS1_5"
    for rank, row in enumerate(eligible[:4], 1):
        row.update(rank=rank, role="PRIMARY" if rank <= 2 else "INFORMATIONAL")
    if not eligible:
        raise AdmissionError("no eligible primary row; retain research as NO_FORECAST")
    grids = [dict(arm=arm, home=h + g.h0, away=a + g.a0, mass=float(g.p[h, a]))
             for arm, g in experts.items() for h, a in np.ndindex(g.p.shape) if g.p[h, a] > 0]
    artifacts = {"PREDICTIONS": csv_bytes(priced), "GRIDS": csv_bytes(grids), "FORMS": csv_bytes(forms),
                 "HISTORY": csv_bytes(history), "CONTRACTS": csv_bytes(contracts), "REQUEST": csv_bytes([request]),
                 "MODEL_CONFIG": csv_bytes([{f.name: repr(getattr(lg, f.name)) for f in fields(lg)}]),
                 "WARM_START": csv_bytes(warm_rows) if warm_rows else b"event_id,refit_at,available_at,league_line,loss_RATINGS_FAST,loss_RATINGS_SLOW,loss_LEAGUE_BASELINE\n",
                 "FEEDBACK_LOSSES": csv_bytes(fb_rows) if fb_rows else b"event_id,available_at,receipt_sha256,loss_RATINGS_FAST,loss_RATINGS_SLOW,loss_LEAGUE_BASELINE\n",
                 "ETA_ADMISSION": ETA_TABLE.read_bytes() if ETA_TABLE.exists() else b"competition,policy,eta,tune_end,frozen_at,evidence_path,evidence_sha256\n",
                 "FEEDBACK_INPUT": csv_bytes(feedback) if feedback else b"event_id\n"}
    if competition_source is not None:
        artifacts["COMPETITION_SOURCE"] = csv_bytes(competition_source)
    rec = dict(policy=POLICY, event_id=request["event_id"], competition=lg.path, endpoint=lg.endpoint,
               information_horizon=cutoff.isoformat(), horizon_source=horizon_source,
               scheduled_start=clock(request["scheduled_start"]).isoformat(), issue_at=issue.isoformat(), actual_issue_phase=phase,
               source_status="HASH_CUSTODY_CHECKED_NOT_OWNER_CERTIFIED", qualification="EXPERIMENTAL_PRIMARY_NOT_CERTIFIED",
               selected_arm=MIX_ARM, context=context, coverage=coverage,
               mixture_weights=";".join(f"{a}:{x:.17g}" for a, x in zip(ARMS, weights)),
               cumulative_losses=";".join(f"{a}:{x:.17g}" for a, x in zip(ARMS, cumulative)),
               eta=f"{eta:.17g}", eta_source=eta_source, eta_table_sha256=eta_sha,
               warm_start_games=n_warm, feedback_events=n_fb, league_line=f"{line:.17g}",
               training_rows=len(train),
               config_origin="REVIEWED_SPORTING_SOURCE" if competition_source is not None else "ARCHIVE_DISCOVERY",
               history_web_rows=sum(r.get("source_kind") in ("WEB_RECOVERED", "WEB_CORRECTED") for r in history),
               history_archive_rows=sum(r.get("source_kind") == "ARCHIVE_REVIEWED" for r in history),
               history_unspecified_rows=sum(not r.get("source_kind") for r in history),
               numpy_version=np.__version__, pandas_version=pd.__version__, scipy_version=scipy.__version__,
               expert_recipe="FAST_half_life90_SLOW365_ridge8_cov_inflation1.1;cricket_C2_ridge20_venue20_inflation1.1",
               issue_clock_status="DECLARED_ISSUE_NOT_INDEPENDENTLY_PUBLISHED", model_id=f"PRIMARY_FRESH_FIT_V3:{lg.path}:{MIX_ARM}",
               candidate_recipe=recipe, model_features="team identity, prior scores, time decay; no fitted availability effects",
               feedback_sha256=digest(csv_bytes(feedback)) if feedback else "NONE",
               code_sha256=generating_code, repository_head=repository_head(), generated_at=datetime.now(timezone.utc).isoformat(),
               **grid.summary(), **{k.lower() + "_sha256": digest(v) for k, v in artifacts.items()})
    # Atomic publication: existing bundles never overwritten, even for a rerun.
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.parent / ("." + output.name + "." + secrets.token_hex(6))
    temporary.mkdir()
    try:
        for name, data in artifacts.items():
            (temporary / (name + ".csv")).write_bytes(data)
        (temporary / "RECEIPT.csv").write_bytes(csv_bytes([rec]))
        (temporary / "FORECAST.md").write_text(
            f"# Experimental primary forecast {request['event_id']}\n\n{POLICY}: primary distribution = expert mixture "
            f"({'; '.join(f'{a} {x:.3f}' for a, x in zip(ARMS, weights))}), weights from {n_warm} warm-start games and "
            f"{n_fb} settled bundles (eta {eta:g}, {eta_source}). {phase}; source truth/calibration/skill NOT_CERTIFIED. "
            "No staking/market inputs. All issued rows use one complete mixture distribution. "
            "Archive form windows may be short; availability effects are not fitted features. "
            "Gate/family/precision and complete candidate-universe checks remain required by the card operator.\n",
            encoding="utf-8")
        if output.exists():
            raise AdmissionError("existing issued bundle; choose a new event/revision output path")
        verify_bundle(temporary)
        if source_hash() != generating_code:
            raise AdmissionError("source changed during inference; retry from stable code")
        temporary.rename(output)
    finally:
        if temporary.exists():
            for file in temporary.iterdir():
                file.unlink()
            temporary.rmdir()
    verify_bundle(output)
    return rec


def source_hash() -> str:
    h = hashlib.sha256()
    root = Path(__file__).parent
    for file in sorted(root.rglob("*.py")):
        if "tests" not in file.relative_to(root).parts:
            h.update(file.relative_to(root).as_posix().encode())
            h.update(hashlib.sha256(file.read_bytes()).digest())
    return h.hexdigest()


def repository_head() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=Path(__file__).parents[1], stderr=subprocess.DEVNULL).decode().strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return "NOT_VERIFIED"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("predict", "execute"):
        predict = sub.add_parser(command)
        for name in ("request", "history", "contracts", "out"):
            predict.add_argument("--" + name, type=Path, required=True)
        predict.add_argument("--feedback", type=Path)
        predict.add_argument("--competition-source", type=Path, help="reviewed exact competition metadata when archive routing is missing or defective")
        predict.add_argument("--seed", type=int, help="accepted for compatibility; V3 is deterministic and ignores it")
    check = sub.add_parser("verify-execution")
    check.add_argument("--attempt", type=Path, required=True)
    check_log = sub.add_parser("verify-log")
    check_log.add_argument("--manifest", type=Path, required=True)
    check_log.add_argument("--mini", type=Path, required=True)
    review = sub.add_parser("settle")
    for name in ("bundle", "evidence", "out"):
        review.add_argument("--" + name, type=Path, required=True)
    for name in ("home-score", "away-score"):
        review.add_argument("--" + name, type=int, required=True)
    for name in ("final-at", "available-at", "evidence-sha256"):
        review.add_argument("--" + name, required=True)
    args = parser.parse_args(argv)
    if args.command == "execute":
        from ml.execution import execute_files
        rec = execute_files(args.request, args.history, args.contracts, args.out,
                            args.feedback, args.competition_source)
        print(f"{rec['event_id']}: {rec['status']}; {args.out / 'EXECUTION.csv'}; {rec['error']}")
        if rec["status"] != "EXECUTED":
            raise SystemExit(1)
        return
    if args.command == "verify-execution":
        from ml.execution import verify_execution
        print(verify_execution(args.attempt)["status"])
        return
    if args.command == "verify-log":
        from ml.execution import verify_log
        print(verify_log(args.manifest, args.mini))
        return
    if args.command == "predict":
        requests = read_rows(args.request)
        if len(requests) != 1:
            raise AdmissionError("exactly one event per request")
        req = requests[0]
        source = read_rows(args.competition_source) if args.competition_source else None
        rec = forecast(req, None if source is not None else get_league(req["competition"]), read_rows(args.history), read_rows(args.contracts),
                       args.out, read_rows(args.feedback) if args.feedback else [],
                       np.random.default_rng(args.seed) if args.seed is not None else None, competition_source=source)
        print(f"{rec['event_id']}: {rec['selected_arm']} weights {rec['mixture_weights']}; {rec['qualification']}; {args.out}")
    else:
        result = settle(args.bundle, args.home_score, args.away_score, args.final_at, args.available_at,
                        args.evidence, args.evidence_sha256)
        with args.out.open("xb") as f:
            f.write(csv_bytes([result]))
        print(f"feedback retained: {args.out}; append to effective feedback inventory only after revision reconciliation")


if __name__ == "__main__":
    main()
