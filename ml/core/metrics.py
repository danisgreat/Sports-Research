"""Proper scores, calibration diagnostics and paired week-block intervals (SCORING_AND_VALIDATION §3–§5)."""
from __future__ import annotations

import math

import numpy as np
import pandas as pd
from scipy import optimize, stats


def brier(p, y) -> np.ndarray:
    return (np.asarray(p, float) - np.asarray(y, float)) ** 2


def log_loss(p, y, eps: float = 0.0) -> np.ndarray:
    """Binary log loss; no hidden clipping unless eps > 0 is passed explicitly."""
    p = np.asarray(p, float)
    y = np.asarray(y, float)
    if eps:
        p = np.clip(p, eps, 1 - eps)
    with np.errstate(divide="ignore"):
        return -(y * np.log(p) + (1 - y) * np.log(1 - p))


def brier_multiclass_half(probs: np.ndarray, outcome_idx: np.ndarray) -> np.ndarray:
    """Half-sum multiclass Brier: 0.5 * sum_k (p_k - y_k)^2 (SCORING §3 scaling)."""
    probs = np.asarray(probs, float)
    onehot = np.zeros_like(probs)
    onehot[np.arange(len(probs)), np.asarray(outcome_idx, int)] = 1.0
    return 0.5 * ((probs - onehot) ** 2).sum(axis=1)


def iso_week(dates: pd.Series) -> pd.Series:
    d = pd.to_datetime(dates)
    iso = d.dt.isocalendar()
    return iso["year"].astype(str) + "-W" + iso["week"].astype(int).map("{:02d}".format)


def paired_week_interval(diff: pd.Series, event: pd.Series, week: pd.Series, conf: float = 0.95) -> dict:
    """Average paired differences within event, then within ISO week; t-interval over week means.

    Negative values favour the candidate. k < 8 weeks is reported as INSUFFICIENT_EVIDENCE (SCORING §5).
    """
    df = pd.DataFrame({"d": diff.values, "e": event.values, "w": week.values}).dropna()
    if df.empty:
        return {"k_weeks": 0, "n_events": 0, "mean": float("nan"), "lo": float("nan"), "hi": float("nan"),
                "sd_w": float("nan"), "status": "NOT_COMPUTABLE"}
    ev = df.groupby(["w", "e"], sort=False)["d"].mean().reset_index()
    wk = ev.groupby("w")["d"].mean()
    k = len(wk)
    m = float(wk.mean())
    sd = float(wk.std(ddof=1)) if k > 1 else float("nan")
    if k > 1 and sd > 0:
        t = stats.t.ppf(0.5 + conf / 2, k - 1)
        half = t * sd / math.sqrt(k)
    else:
        half = float("nan")
    status = "INSUFFICIENT_EVIDENCE" if k < 8 else ("BELOW_ZERO" if m + half < 0 else
                                                    ("ABOVE_ZERO" if m - half > 0 else "SPANS_ZERO"))
    return {"k_weeks": k, "n_events": int(len(ev)), "mean": m, "lo": m - half, "hi": m + half, "sd_w": sd,
            "status": status}


def reliability_table(p, y, bins: int = 10) -> pd.DataFrame:
    """Complete predeclared bins over [0, 1]; empty bins are retained (SCORING §4)."""
    p = np.asarray(p, float)
    y = np.asarray(y, float)
    edges = np.linspace(0, 1, bins + 1)
    idx = np.clip(np.digitize(p, edges[1:-1], right=False), 0, bins - 1)
    rows = []
    for b in range(bins):
        m = idx == b
        n = int(m.sum())
        rows.append({
            "bin": f"[{edges[b]:.1f}, {edges[b + 1]:.1f}{']' if b == bins - 1 else ')'}",
            "n": n,
            "mean_p": float(p[m].mean()) if n else float("nan"),
            "hit_rate": float(y[m].mean()) if n else float("nan"),
            "wilson_lo": wilson(y[m].sum(), n)[0] if n else float("nan"),
            "wilson_hi": wilson(y[m].sum(), n)[1] if n else float("nan"),
        })
    return pd.DataFrame(rows)


def wilson(k: float, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return float("nan"), float("nan")
    ph = k / n
    centre = (ph + z * z / (2 * n)) / (1 + z * z / n)
    half = z * math.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return centre - half, centre + half


def brier_decomposition(p, y, bins: int = 10) -> dict:
    """Murphy decomposition on fixed bins: Brier ~= reliability - resolution + uncertainty (+ within-bin term)."""
    p = np.asarray(p, float)
    y = np.asarray(y, float)
    n = len(p)
    edges = np.linspace(0, 1, bins + 1)
    idx = np.clip(np.digitize(p, edges[1:-1]), 0, bins - 1)
    obar = y.mean()
    rel = res = 0.0
    for b in range(bins):
        m = idx == b
        nb = m.sum()
        if nb:
            rel += nb * (p[m].mean() - y[m].mean()) ** 2
            res += nb * (y[m].mean() - obar) ** 2
    rel /= n
    res /= n
    unc = obar * (1 - obar)
    bs = float(brier(p, y).mean())
    return {"brier": bs, "reliability": rel, "resolution": res, "uncertainty": unc,
            "within_bin_residual": bs - (rel - res + unc)}


def calibration_fit(p, y) -> dict:
    """Calibration-in-the-large, ECE and the logistic (Cox) intercept/slope of y on logit(p)."""
    p = np.clip(np.asarray(p, float), 1e-6, 1 - 1e-6)
    y = np.asarray(y, float)
    x = np.log(p / (1 - p))

    def nll(b):
        z = b[0] + b[1] * x
        return np.sum(np.logaddexp(0, z) - y * z)

    def grad(b):
        q = 1 / (1 + np.exp(-(b[0] + b[1] * x)))
        return np.array([np.sum(q - y), np.sum((q - y) * x)])

    res = optimize.minimize(nll, np.array([0.0, 1.0]), jac=grad, method="BFGS")
    q = 1 / (1 + np.exp(-(res.x[0] + res.x[1] * x)))
    w = q * (1 - q)
    info = np.array([[w.sum(), (w * x).sum()], [(w * x).sum(), (w * x * x).sum()]])
    try:
        se = np.sqrt(np.diag(np.linalg.inv(info)))
    except np.linalg.LinAlgError:
        se = np.array([np.nan, np.nan])
    rt = reliability_table(p, y)
    ece = float(np.nansum(rt["n"] * (rt["mean_p"] - rt["hit_rate"]).abs()) / len(p))
    return {
        "n": int(len(p)),
        "cal_in_large": float(p.mean() - y.mean()),
        "ece": ece,
        "intercept": float(res.x[0]), "intercept_se": float(se[0]),
        "slope": float(res.x[1]), "slope_se": float(se[1]),
        "converged": bool(res.success),
    }


def cluster_bootstrap_mean(values: np.ndarray, clusters: np.ndarray, n_boot: int = 2000, seed: int = 20261014) -> tuple:
    """Percentile interval of a mean, resampling whole clusters (cards, weeks)."""
    rng = np.random.default_rng(seed)
    df = pd.DataFrame({"v": values, "c": clusters})
    g = df.groupby("c")["v"].agg(["sum", "count"])
    s, c = g["sum"].to_numpy(), g["count"].to_numpy()
    k = len(g)
    draws = rng.integers(0, k, size=(n_boot, k))
    means = s[draws].sum(axis=1) / c[draws].sum(axis=1)
    return float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))
