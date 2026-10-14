"""DECISION_LAB: a paper-only, historical study of staking policies on EPL results (firewalled; CURRENT_RULES §5a).

Inputs:
- the EPL development predictions written by the backtest (model frozen at each week's Monday from earlier
  games only);
- the local-only, git-excluded football-data captures (Pinnacle pre-closing "taken" prices PSH/PSD/PSA, and
  Pinnacle closing prices PSCH/PSCD/PSCA).

No price or price-derived row is ever written to the repository: only aggregate tables. Nothing here is betting
advice, and no card, rule, rank or width may cite it.
"""
from __future__ import annotations

import csv
from pathlib import Path

import numpy as np
import pandas as pd

from ml.config import REPO_ROOT
from ml.core.metrics import brier, brier_multiclass_half, paired_week_interval
from ml.decision import devig, kelly
from ml.decision.bandit import FullInfoRidge, LinTS

FD_DIR = REPO_ROOT / "research" / "data" / "benchmark" / "football_data"
OUTCOMES = ("H", "D", "A")
WARMUP = (2019, 2020)
TEST = (2021, 2022, 2023, 2024, 2025)


def load_prices() -> pd.DataFrame:
    rows = []
    for f in sorted(FD_DIR.glob("*.csv")):
        season = int(f.stem[:4])
        with open(f, newline="", encoding="utf-8-sig", errors="replace") as fh:
            for r in csv.DictReader(fh):
                try:
                    taken = [float(r[c]) for c in ("PSH", "PSD", "PSA")]
                    close = [float(r[c]) for c in ("PSCH", "PSCD", "PSCA")]
                except (KeyError, ValueError):
                    continue
                rows.append({"season": season, "date": pd.to_datetime(r["Date"], dayfirst=True),
                             "home": r["HomeTeam"].strip(), "away": r["AwayTeam"].strip(), "ftr": r["FTR"].strip(),
                             "o_H": taken[0], "o_D": taken[1], "o_A": taken[2],
                             "c_H": close[0], "c_D": close[1], "c_A": close[2]})
    return pd.DataFrame(rows)


def join(pred: pd.DataFrame, prices: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    m = pred.merge(prices, on=["season", "date", "home", "away"], how="left", indicator=True)
    info = {"predictions": len(pred), "matched": int((m["_merge"] == "both").sum())}
    m = m[m["_merge"] == "both"].drop(columns="_merge")
    oi = m["outcome_idx"].map({0: "H", 1: "D", 2: "A"})
    info["ftr_mismatch"] = int((oi != m["ftr"]).sum())
    m = m[oi == m["ftr"]].copy()
    return m.reset_index(drop=True), info


def run(pred: pd.DataFrame, seed: int = 20261014, model_id: str = "SOC-PREMIER-LEAGUE-DC-r1") -> dict:
    prices = load_prices()
    df, info = join(pred, prices)
    out: dict = {"join": info, "model_id": model_id}

    # 1. de-vig method chosen on warm-up seasons by closing log loss
    warm = df[df["season"].isin(WARMUP)]
    ll = {}
    for name, fn in devig.METHODS.items():
        q = np.vstack([fn(r) for r in warm[["c_H", "c_D", "c_A"]].to_numpy()])
        ll[name] = float(-np.mean(np.log(q[np.arange(len(q)), warm["outcome_idx"].to_numpy()])))
    method = min(ll, key=ll.get)
    out["devig_logloss_warmup"] = ll
    out["devig_method"] = method
    fn = devig.METHODS[method]
    qc = np.vstack([fn(r) for r in df[["c_H", "c_D", "c_A"]].to_numpy()])
    qo = np.vstack([fn(r) for r in df[["o_H", "o_D", "o_A"]].to_numpy()])
    for i, k in enumerate(OUTCOMES):
        df[f"qc_{k}"], df[f"qo_{k}"] = qc[:, i], qo[:, i]
    pm = df[["MODEL_p_home", "MODEL_p_draw", "MODEL_p_away"]].to_numpy()

    # 2. MKT-BENCH: model and comparators against the no-vig close (post-settlement scoring view)
    test = df["season"].isin(TEST).to_numpy()
    sources = {"MODEL": pm, "BASELINE_LEAGUE_V1": df[["BASE_p_home", "BASE_p_draw", "BASE_p_away"]].to_numpy(),
               "TB1": df[["TB1_p_home", "TB1_p_draw", "TB1_p_away"]].to_numpy(), "NOVIG_TAKEN": qo, "NOVIG_CLOSE": qc}
    y = df["outcome_idx"].to_numpy()
    bench = []
    for name, P in sources.items():
        b3 = brier_multiclass_half(P, y)
        df[f"b3_{name}"] = b3
        for s in [*TEST, "ALL"]:
            mask = test if s == "ALL" else (df["season"] == s).to_numpy()
            bench.append({"source": name, "season": s, "n": int(mask.sum()), "brier_3way": float(b3[mask].mean())})
    out["bench"] = pd.DataFrame(bench)
    paired = []
    for other in ("NOVIG_CLOSE", "NOVIG_TAKEN", "TB1", "BASELINE_LEAGUE_V1"):
        for s in [*TEST, "ALL"]:
            d = df[test] if s == "ALL" else df[df["season"] == s]
            res = paired_week_interval(d["b3_MODEL"] - d[f"b3_{other}"], d["event_id"], d["week"])
            paired.append({"model_minus": other, "season": s, **res})
    out["bench_paired"] = pd.DataFrame(paired)

    # 3. staking simulation
    sigma_p = float(np.std((pm - qc)[df["season"].isin(WARMUP).to_numpy()]))
    out["sigma_p_warmup"] = sigma_p
    ev = pm * df[["o_H", "o_D", "o_A"]].to_numpy() - 1
    kbest = ev.argmax(axis=1)
    r_ = np.arange(len(df))
    df["k"] = kbest
    df["p_k"] = pm[r_, kbest]
    df["o_k"] = df[["o_H", "o_D", "o_A"]].to_numpy()[r_, kbest]
    df["ev_k"] = ev[r_, kbest]
    df["clv_k"] = df["o_k"] * qc[r_, kbest] - 1
    df["gap_open_k"] = df["p_k"] - qo[r_, kbest]
    df["won_k"] = (df["outcome_idx"].to_numpy() == kbest).astype(float)
    df["f_full"] = [kelly.kelly_full(p, o) for p, o in zip(df["p_k"], df["o_k"])]
    df["shrink"] = [kelly.shrink_factor(f, o, sigma_p) for f, o in zip(df["f_full"], df["o_k"])]
    df = df.sort_values(["date", "event_id"]).reset_index(drop=True)
    df["wk"] = df["fit_date"].astype(str)
    df["round_idx"] = df.groupby("season")["wk"].transform(lambda s: pd.factorize(s)[0]) / 40.0

    def context(r) -> np.ndarray:
        return np.array([1.0, r.ev_k, r.p_k, r.gap_open_k, r.round_idx])

    arms = (0.0, 0.25, 0.5)
    bandit = LinTS(5, arms, seed=seed)
    full = FullInfoRidge(5, arms)
    policies = ["FLAT_EV>0.03", "QUARTER_KELLY_SHRUNK", "LINTS_BANDIT", "FULL_INFO_RIDGE"]
    stakes = {p: np.zeros(len(df)) for p in policies}
    props, chosen = np.zeros((len(df), len(arms))), np.zeros(len(df), int)
    for i, r in enumerate(df.itertuples()):
        base = r.shrink * r.f_full
        stakes["FLAT_EV>0.03"][i] = 0.01 if r.ev_k > 0.03 else 0.0
        stakes["QUARTER_KELLY_SHRUNK"][i] = min(0.02, 0.25 * base)
        x = context(r)
        a, pr = bandit.choose(x)
        chosen[i], props[i] = a, pr
        stakes["LINTS_BANDIT"][i] = min(0.02, arms[a] * base)
        stakes["FULL_INFO_RIDGE"][i] = min(0.02, arms[full.choose(x)] * base)
        rewards = np.array([min(0.02, m * base) * r.clv_k for m in arms])
        bandit.update(a, x, rewards[a])
        full.update_all(x, rewards)
    df["bandit_arm"] = chosen
    for i, a in enumerate(arms):
        df[f"prop_{i}"] = props[:, i]

    sims = []
    for p in policies:
        df[f"stake_{p}"] = stakes[p]
        sims.append(simulate(df[df["season"].isin(TEST)], p))
    out["policies"] = pd.DataFrame(sims)

    # 4. off-policy evaluation check: IPS estimate of "always arm 1 (quarter)" from the bandit logs vs exact value
    t = df[df["season"].isin(TEST)]
    base = t["shrink"] * t["f_full"]
    exact = np.minimum(0.02, arms[1] * base) * t["clv_k"]
    ips = np.where(t["bandit_arm"] == 1, exact / t["prop_1"], 0.0)
    out["ope"] = {"exact_mean_reward": float(exact.mean()), "ips_estimate": float(ips.mean()),
                  "ips_se": float(ips.std(ddof=1) / np.sqrt(len(ips))), "n": int(len(t)),
                  "bandit_arm_share": {str(a): float((t["bandit_arm"] == i).mean()) for i, a in enumerate(arms)}}
    out["frame_rows"] = len(df)
    return out


def simulate(d: pd.DataFrame, policy: str, slate_cap: float = 0.10, halt_dd: float = 0.20) -> dict:
    """Signal quality (CLV over every decision the policy stakes) is reported separately from the bankroll path.

    Bankroll guardrail: a drawdown beyond ``halt_dd`` halts staking for the rest of the study (a halt pending manual
    review, ML_RL_IMPLEMENTATION_FRAMEWORK §10.3), so bankroll figures after a halt are frozen.
    """
    bank, peak, max_dd, halted_week = 1.0, 1.0, 0.0, None
    staked = pnl = 0.0
    sig = d[d[f"stake_{policy}"] > 0]
    for wk, g in d.groupby("wk", sort=True):
        if halted_week is not None:
            break
        s = kelly.cap_slate(g[f"stake_{policy}"].to_numpy(), slate_cap)
        ret = np.where(g["won_k"].to_numpy() == 1, s * (g["o_k"].to_numpy() - 1), -s)
        staked += s.sum() * bank
        pnl += ret.sum() * bank
        bank *= 1 + ret.sum()
        peak = max(peak, bank)
        max_dd = max(max_dd, 1 - bank / peak)
        if 1 - bank / peak > halt_dd:
            halted_week = wk
    if sig.empty:
        return {"policy": policy, "n_bets": 0}
    iv = paired_week_interval(sig["clv_k"], sig["event_id"], sig["week"])
    return {"policy": policy, "n_bets": len(sig), "mean_clv": float(sig["clv_k"].mean()),
            "clv_week_lo": iv["lo"], "clv_week_hi": iv["hi"], "share_clv_positive": float((sig["clv_k"] > 0).mean()),
            "stake_weighted_clv": float(np.average(sig["clv_k"], weights=sig[f"stake_{policy}"])),
            "hit_rate": float(sig["won_k"].mean()), "mean_odds": float(sig["o_k"].mean()),
            "turnover": staked, "pnl": pnl, "roi": pnl / staked if staked else float("nan"), "final_bankroll": bank,
            "max_drawdown": max_dd, "halted_at_week": halted_week or "never"}
