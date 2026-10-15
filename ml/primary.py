"""Experimental primary sporting forecasts and delayed-feedback model selection.

No market/staking imports. A context-specific Exp3 bandit selects a WHOLE fitted
score distribution, so every contract retains coherent winner/total/push masses.
Only hash-verified immutable prediction bundles can supply later feedback.
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

from ml.config import League, get_league
from ml.core.distributions import ScoreGrid
from ml.evaluation.backtest import make_model
from ml.models.baseline import LeagueBaseline
from ml.models.common import FitError, residual_draw_share
from ml.models.cricket import FirstInningsModel, CricketParams

POLICY = "PRIMARY_EXP3_V1"
ARMS = ("RATINGS_FAST", "RATINGS_SLOW", "LEAGUE_BASELINE")
GAMMA = 0.10


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


def admit_history(rows: list[dict], cutoff, target: str, competition: str, endpoint: str) -> pd.DataFrame:
    """Source custody is checked, never represented as field-owner certification."""
    limit = clock(cutoff)
    checked = set()
    identities = set()
    records = []
    for r in rows:
        if r["competition"] != competition or r["endpoint"] != endpoint or r["event_id"] == target or r["event_id"] in identities:
            raise AdmissionError("wrong scope, target event leakage or duplicate training event")
        identities.add(r["event_id"])
        date, final, known = clock(r["date"]), clock(r["final_at"]), clock(r["available_at"])
        if not date <= final <= known <= limit or not date < limit.normalize():
            raise AdmissionError("training event/final/source not known before cutoff; same-day rows excluded")
        if r["status"] != "FINAL" or r["admission"] != "RESEARCH_INPUT_REVIEWED" or not r["source_url"].startswith("https://"):
            raise AdmissionError("terminal/source review receipt required")
        token = (r["evidence_path"], r["evidence_sha256"])
        if token not in checked:
            receipt_file(*token)
            checked.add(token)
        rec = {"date": date.tz_localize(None), "event_id": r["event_id"], "season": int(r["season"]),
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


def fit_experts(lg: League, train: pd.DataFrame, cutoff, home: str, away: str, venue=""):
    as_of = clock(cutoff).tz_localize(None)
    if lg.data_warnings:
        raise AdmissionError("competition DATA_HOLD: " + ";".join(lg.data_warnings))
    if lg.engine not in ("gaussian", "count", "dixon_coles", "cricket"):
        raise AdmissionError("unsupported exact sport/endpoint; no major-league substitution")
    if home not in set(train.home) | set(train.away) or away not in set(train.home) | set(train.away):
        raise AdmissionError("unseen participant: no silent prior as a primary model")
    fitting = train.copy()
    if lg.tie_rule != "draw" and lg.engine != "cricket":
        # Fit regulation scoring, then add extras ONCE. Preserve final labels for
        # extra-time winner and residual-draw estimates.
        fitting["hs"], fitting["as_"] = train.reg_hs, train.reg_as
    if lg.engine == "cricket":
        balls = pd.to_numeric(train.legal_balls, errors="coerce")
        wickets = pd.to_numeric(train.wickets, errors="coerce")
        cap = float(lg.overs_cap) * 6
        if not (balls.between(0, cap) & wickets.between(0, 10) & balls.eq(np.floor(balls)) & wickets.eq(np.floor(wickets)) &
                (balls.eq(cap) | wickets.eq(10))).all():
            raise AdmissionError("short/unknown-length innings cannot train a full-innings endpoint")
        if not (train.home.eq(train.bat) & train.away.eq(train.bowl) & train.hs.eq(train.runs) & train.as_.eq(0)).all():
            raise AdmissionError("innings coordinates must be batting runs versus zero auxiliary; home=bat, away=bowl")
    def final_labels(model):
        if hasattr(model, "residual_draw") and hasattr(model, "sd_margin"):
            model.residual_draw = residual_draw_share(train, model.sd_margin)
        if hasattr(model, "p_home_extra"):
            extra = train[train.decision.isin(["Overtime", "Shootout", "EXTRAS"])]
            model.p_home_extra = float((extra.hs > extra.as_).mean()) if len(extra) >= 20 else .5
        return model
    experts = {}
    for arm, days in zip(ARMS[:2], (90.0, 365.0)):
        if lg.engine == "cricket":
            if lg.endpoint != "FIRST_INNINGS_FULL_LENGTH" or not all(c in train for c in ("runs", "bat", "bowl", "venue")):
                raise AdmissionError("cricket requires exact full-length first-innings labels; phases unsupported")
            model = FirstInningsModel("C2", CricketParams(days, 20.0, 20.0, 1.1)).fit(train, as_of)
            experts[arm] = ScoreGrid(model.pmf(home, away, venue)[:, None])
        else:
            params = dict(half_life_days=days, ridge=8.0)
            if lg.engine == "gaussian":
                params["cov_inflation"] = 1.1
            model = make_model(lg, params)
            model.fit(fitting, as_of) if lg.engine == "gaussian" else model.fit(fitting, as_of, int(train.season.max()))
            final_labels(model)
            experts[arm], flags = model.grid(home, away)
            if flags:
                raise AdmissionError("primary model flags require review: " + ";".join(flags))
    if lg.engine == "cricket":
        baseline = FirstInningsModel("C0", CricketParams(365.0, 20.0, 20.0, 1.1)).fit(train, as_of)
        experts[ARMS[2]] = ScoreGrid(baseline.pmf(home, away, venue)[:, None])
    else:
        experts[ARMS[2]] = final_labels(LeagueBaseline(lg).fit(fitting)).grid()
    return experts


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


def probabilities(feedback: list[dict], context: str, before) -> np.ndarray:
    """Delayed Exp3: updates only the chosen arm, with its frozen behaviour probability."""
    logs = np.zeros(len(ARMS))
    seen = set()
    ready = []
    for row in feedback:
        if row["event_id"] in seen:
            raise AdmissionError("duplicate/revision-conflicting feedback; resolve to one effective row")
        seen.add(row["event_id"])
        if clock(row["available_at"]) > clock(before):
            continue  # Future reward cannot change today's action.
        receipt_file(row["bundle"] + "/RECEIPT.csv", row["receipt_sha256"])
        rec = verify_bundle(Path(row["bundle"]))
        if rec["event_id"] != row["event_id"] or rec["context"] != row["context"]:
            raise AdmissionError("feedback identity/context differs from frozen forecast")
        if row["context"] != context:
            continue
        if not clock(rec["issue_at"]) < clock(row["final_at"]) <= clock(row["available_at"]):
            raise AdmissionError("feedback was not observable after actual issue/final")
        action, prob, reward = rec["selected_arm"], float(rec["behaviour_probability"]), float(row["reward"])
        if not 0 < prob <= 1 or not 0 <= reward <= 1 or not math.isfinite(reward):
            raise AdmissionError("invalid propensity/reward")
        # Reward must be reconstructed from immutable rows and the evidence-backed final.
        expected = settle(Path(row["bundle"]), int(row["home_score"]), int(row["away_score"]),
                          row["final_at"], row["available_at"], row["evidence_path"], row["evidence_sha256"])
        if expected is None or abs(float(expected["reward"]) - reward) > 1e-12:
            raise AdmissionError("feedback reward differs from frozen contract grades")
        ready.append((clock(row["available_at"]), row["event_id"], ARMS.index(action), prob, reward))
    for _, _, arm, prob, reward in sorted(ready):
        logs[arm] += GAMMA * reward / (len(ARMS) * prob)
        logs -= logs.max()
    weights = np.exp(logs)
    return (1 - GAMMA) * weights / weights.sum() + GAMMA / len(ARMS)


def verify_bundle(folder: Path) -> dict:
    rows = read_rows(folder / "RECEIPT.csv")
    if len(rows) != 1 or rows[0]["policy"] != POLICY:
        raise AdmissionError("unknown bundle policy/receipt")
    rec = rows[0]
    for name in ("PREDICTIONS", "GRIDS", "FORMS", "HISTORY", "CONTRACTS", "REQUEST", "FEEDBACK_INPUT", "MODEL_CONFIG"):
        receipt_file(folder / (name + ".csv"), rec[name.lower() + "_sha256"])
    prop = dict((x.split(":")[0], float(x.split(":")[1])) for x in rec["action_probabilities"].split(";"))
    if set(prop) != set(ARMS) or not all(0 < v <= 1 for v in prop.values()) or abs(sum(prop.values()) - 1) > 1e-12 or float(rec["behaviour_probability"]) != prop[rec["selected_arm"]]:
        raise AdmissionError("frozen behaviour distribution/selected propensity invalid")
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
    for row in read_rows(folder / "PREDICTIONS.csv"):
        w, p, l = price(grids[rec["selected_arm"]], row, rec["endpoint"])
        if max(abs(w-float(row["win"])), abs(p-float(row["push"])), abs(l-float(row["loss"]))) > 1e-10:
            raise AdmissionError("issued row not derived from frozen selected model")
        expected = w/(w+l) if w+l > 0 else "NOT_COMPUTED"
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
           evidence_path, evidence_sha256) -> dict | None:
    rec = verify_bundle(folder)
    if any(not math.isfinite(s) or s < 0 or s != int(s) for s in (home_score, away_score)):
        raise AdmissionError("invalid final score")
    if rec["endpoint"] == "FIRST_INNINGS_FULL_LENGTH" and away_score != 0:
        raise AdmissionError("first-innings settlement uses batting runs and a zero auxiliary coordinate")
    if not clock(rec["issue_at"]) < clock(final_at) <= clock(available_at):
        raise AdmissionError("terminal feedback before issue/final")
    receipt_file(evidence_path, evidence_sha256)
    rows = read_rows(folder / "PREDICTIONS.csv")
    losses = []
    final = ScoreGrid(np.ones((1, 1)), home_score, away_score)
    for row in rows:
        if row["rank"] not in ("1", "2"):
            continue
        win, push, loss = price(final, row, rec["endpoint"])
        if push == 1:
            continue
        losses.append((float(row["p_card"]) - win) ** 2)
    if not losses:
        return None  # No all-push/void reward or invented zero loss.
    return dict(event_id=rec["event_id"], context=rec["context"], reward=1 - float(np.mean(losses)),
                home_score=int(home_score), away_score=int(away_score), final_at=clock(final_at).isoformat(),
                available_at=clock(available_at).isoformat(), bundle=str(folder.resolve()),
                receipt_sha256=digest((folder / "RECEIPT.csv").read_bytes()),
                evidence_path=str(Path(evidence_path).resolve()), evidence_sha256=evidence_sha256)


def forecast(request: dict, lg: League, history: list[dict], contracts: list[dict], output: Path,
             feedback: list[dict] | None = None, rng=None) -> dict:
    allowed_request = {"event_id", "competition", "home", "away", "cutoff", "issue_at", "actual_start", "endpoint", "venue", "outcome_exposure", "candidate_recipe"}
    allowed_history = {"event_id", "competition", "endpoint", "date", "final_at", "available_at", "status", "admission", "source_url", "evidence_path", "evidence_sha256", "season", "home", "away", "hs", "as_", "reg_hs", "reg_as", "decision", "stage", "bat", "bowl", "venue", "runs", "legal_balls", "wickets"}
    allowed_contract = {"contract_key", "family", "side", "line", "endpoint", "definition", "action"}
    if set(request) - allowed_request or any(set(r) - allowed_history for r in history) or any(set(r) - allowed_contract for r in contracts):
        raise AdmissionError("unregistered input columns (including market fields) are prohibited")
    cutoff, issue = clock(request["cutoff"]), clock(request["issue_at"])
    if cutoff > issue or request["home"] == request["away"] or not request["event_id"].strip():
        raise AdmissionError("invalid identity or cutoff after issue")
    if request["competition"] != lg.path or request["endpoint"] != lg.endpoint:
        raise AdmissionError("request/competition model scope mismatch")
    if request.get("outcome_exposure", "") != "NONE_RECORDED":
        raise AdmissionError("outcome-exposed full-event primary forecast blocked")
    start = clock(request["actual_start"]) if request.get("actual_start") else None
    if start is not None and cutoff >= start:
        raise AdmissionError("evidence horizon must precede actual first play")
    phase = "TIMING_UNVERIFIED" if start is None else ("PREGAME" if issue < start else "POST_START_ISSUE")
    train = admit_history(history, cutoff, request["event_id"], lg.path, lg.endpoint)
    experts = fit_experts(lg, train, cutoff, request["home"], request["away"], request.get("venue", ""))
    forms = form_rows(train, request["home"], request["away"], cricket=lg.engine == "cricket")
    coverage = "SHORT" if min(int(r["n"]) for r in forms if r["window"] == "L20") < 20 else "FULL20"
    recipe = request.get("candidate_recipe", "")
    if not recipe.strip():
        raise AdmissionError("freeze a candidate recipe ID before model selection")
    context = f"{POLICY}|{lg.path}|{lg.endpoint}|{coverage}|{phase}|{recipe}"
    if any(r["event_id"] == request["event_id"] for r in (feedback or [])):
        raise AdmissionError("target feedback cannot enter its own prediction")
    probs = probabilities(feedback or [], context, issue)
    # Fresh system randomness by default; seed is an explicit experimental replay option.
    rng = rng if rng is not None else np.random.default_rng(secrets.randbits(128))
    selected = int(rng.choice(len(ARMS), p=probs))
    grid = experts[ARMS[selected]]
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
                           baseline_p=bp, selected_arm=ARMS[selected], rank="", role="DIAGNOSTIC"))
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
                 "FEEDBACK_INPUT": csv_bytes(feedback) if feedback else b"event_id\n"}
    rec = dict(policy=POLICY, event_id=request["event_id"], competition=lg.path, endpoint=lg.endpoint,
               cutoff=cutoff.isoformat(), issue_at=issue.isoformat(), actual_issue_phase=phase,
               source_status="HASH_CUSTODY_CHECKED_NOT_OWNER_CERTIFIED", qualification="EXPERIMENTAL_PRIMARY_NOT_CERTIFIED",
               selected_arm=ARMS[selected], behaviour_probability=float(probs[selected]), context=context,
               action_probabilities=";".join(f"{a}:{p:.17g}" for a, p in zip(ARMS, probs)),
               training_rows=len(train), gamma=GAMMA,
               numpy_version=np.__version__, pandas_version=pd.__version__, scipy_version=scipy.__version__,
               expert_recipe="FAST_half_life90_SLOW365_ridge8_cov_inflation1.1;cricket_C2_ridge20_venue20_inflation1.1",
               issue_clock_status="DECLARED_ISSUE_NOT_INDEPENDENTLY_PUBLISHED", model_id=f"PRIMARY_FRESH_FIT_V1:{lg.path}:{ARMS[selected]}",
               candidate_recipe=recipe, model_features="team identity, prior scores, time decay; no fitted availability effects",
               feedback_sha256=digest(csv_bytes(feedback)) if feedback else "NONE_COLD_START",
               code_sha256=source_hash(), repository_head=repository_head(), generated_at=datetime.now(timezone.utc).isoformat(),
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
            f"# Experimental primary forecast {request['event_id']}\n\n{ARMS[selected]} selected by {POLICY}; "
            f"behaviour probability {probs[selected]:.9f}. {phase}; source truth/calibration/skill NOT_CERTIFIED. "
            "No staking/market inputs. All issued rows use one selected complete distribution. "
            "Archive form windows may be short; availability effects are not fitted features. "
            "Gate/family/precision and complete candidate-universe checks remain required by the card operator.\n",
            encoding="utf-8")
        if output.exists():
            raise AdmissionError("existing issued bundle; choose a new event/revision output path")
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
    predict = sub.add_parser("predict")
    for name in ("request", "history", "contracts", "out"):
        predict.add_argument("--" + name, type=Path, required=True)
    predict.add_argument("--feedback", type=Path)
    predict.add_argument("--seed", type=int, help="explicit research replay; never search seeds after results")
    review = sub.add_parser("settle")
    for name in ("bundle", "evidence", "out"):
        review.add_argument("--" + name, type=Path, required=True)
    for name in ("home-score", "away-score"):
        review.add_argument("--" + name, type=int, required=True)
    for name in ("final-at", "available-at", "evidence-sha256"):
        review.add_argument("--" + name, required=True)
    args = parser.parse_args(argv)
    if args.command == "predict":
        requests = read_rows(args.request)
        if len(requests) != 1:
            raise AdmissionError("exactly one event per request")
        req = requests[0]
        rec = forecast(req, get_league(req["competition"]), read_rows(args.history), read_rows(args.contracts),
                       args.out, read_rows(args.feedback) if args.feedback else [],
                       np.random.default_rng(args.seed) if args.seed is not None else None)
        print(f"{rec['event_id']}: {rec['selected_arm']}; {rec['qualification']}; {args.out}")
    else:
        result = settle(args.bundle, args.home_score, args.away_score, args.final_at, args.available_at,
                        args.evidence, args.evidence_sha256)
        if result is None:
            raise AdmissionError("no decisive original primary rows; no bandit update")
        with args.out.open("xb") as f:
            f.write(csv_bytes([result]))
        print(f"feedback retained: {args.out}; append to effective feedback inventory only after revision reconciliation")


if __name__ == "__main__":
    main()
