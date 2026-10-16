"""Chronological calibration study and coherent grid recalibration (Improvement 16). Status CALIBRATION_STUDY.

Calibrators are trained only on earlier out-of-sample predictions whose outcomes were available before the fit
time, and chosen on a later tuning window; nothing here is applied to issued cards. Methods:

    IDENTITY   no change (always a candidate; ties resolve to it)
    PLATT      logistic recalibration of logit(p) with a Gaussian prior centred on the identity (a=0, b=1)
    ISOTONIC   pool-adjacent-violators, only with at least ``min_isotonic`` training rows
    HIER_PLATT per-competition Platt shrunk toward the pooled Platt fit (for small competitions)

A score distribution is recalibrated coherently: ``calibrate_grid`` rescales the joint grid by iterative
proportional fitting so that its winner classes and its over/under classes at a reference line hit the calibrated
targets simultaneously. Every winner, handicap and total row is then re-derived from that one grid, so no contract
probability can contradict another for the same match.
"""
from __future__ import annotations

import argparse
import math
import secrets
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import optimize

from ml import primary as p
from ml.core.distributions import CoherenceError, ScoreGrid

EVIDENCE_CLASS = "CALIBRATION_STUDY_NOT_DEPLOYED"
EPS = 1e-6


def _logit(x):
    x = np.clip(np.asarray(x, float), EPS, 1 - EPS)
    return np.log(x / (1 - x))


@dataclass
class Calibrator:
    method: str
    params: dict = field(default_factory=dict)
    n: int = 0

    def __call__(self, prob):
        prob = np.asarray(prob, float)
        if self.method == "IDENTITY":
            return prob
        if self.method in ("PLATT", "HIER_PLATT"):
            a, b = self.params["a"], self.params["b"]
            return 1 / (1 + np.exp(-(a + b * _logit(prob))))
        if self.method == "ISOTONIC":
            x, y = np.asarray(self.params["x"]), np.asarray(self.params["y"])
            return np.interp(prob, x, y)
        raise ValueError("unknown calibration method")


def fit_platt(prob, y, prior_sd: float = 1.0, centre=(0.0, 1.0)) -> Calibrator:
    """MAP logistic recalibration; the prior shrinks toward ``centre`` (identity by default)."""
    x, y = _logit(prob), np.asarray(y, float)
    c = np.asarray(centre, float)

    def nll(beta):
        z = beta[0] + beta[1] * x
        return np.sum(np.logaddexp(0, z) - y * z) + np.sum((beta - c) ** 2) / (2 * prior_sd ** 2)

    res = optimize.minimize(nll, c.copy(), method="BFGS")
    return Calibrator("PLATT", dict(a=float(res.x[0]), b=float(res.x[1])), len(y))


def fit_isotonic(prob, y) -> Calibrator:
    order = np.argsort(prob, kind="stable")
    x, yy = np.asarray(prob, float)[order], np.asarray(y, float)[order]
    blocks = [[v, 1.0, xv, xv] for v, xv in zip(yy, x)]  # mean, weight, x_lo, x_hi
    merged = []
    for b in blocks:
        merged.append(b)
        while len(merged) > 1 and merged[-2][0] > merged[-1][0]:
            hi = merged.pop()
            lo = merged.pop()
            w = lo[1] + hi[1]
            merged.append([(lo[0] * lo[1] + hi[0] * hi[1]) / w, w, lo[2], hi[3]])
    xs, ys = [], []
    for mean, _, lo, hi in merged:
        xs += [lo, hi]
        ys += [mean, mean]
    return Calibrator("ISOTONIC", dict(x=[0.0] + xs + [1.0], y=[ys[0]] + ys + [ys[-1]]), len(yy))


def fit_hierarchical(rows: pd.DataFrame, competition: str, prior_sd: float = 0.5) -> Calibrator:
    pooled = fit_platt(rows.p, rows.y)
    own = rows[rows.competition == competition]
    if own.empty:
        return Calibrator("HIER_PLATT", dict(pooled.params), 0)
    fit = fit_platt(own.p, own.y, prior_sd=prior_sd, centre=(pooled.params["a"], pooled.params["b"]))
    return Calibrator("HIER_PLATT", fit.params, len(own))


def available_before(rows: pd.DataFrame, fit_at) -> pd.DataFrame:
    """Only predictions issued before ``fit_at`` whose outcome was available by then may train a calibrator."""
    t = p.clock(fit_at)
    return rows[(rows.issued_at.map(p.clock) < t) & (rows.outcome_available_at.map(p.clock) <= t)]


def fit_method(method: str, train: pd.DataFrame, *, competition: str = "", min_isotonic: int = 200) -> Calibrator | None:
    if method == "IDENTITY":
        return Calibrator("IDENTITY", {}, len(train))
    if len(train) < 30:
        return None
    if method == "PLATT":
        return fit_platt(train.p, train.y)
    if method == "ISOTONIC":
        return fit_isotonic(train.p, train.y) if len(train) >= min_isotonic else None
    if method == "HIER_PLATT":
        return fit_hierarchical(train, competition) if competition else None
    raise ValueError(method)


def select(rows: pd.DataFrame, tune_start, tune_end, *, competition: str = "",
           methods=("IDENTITY", "PLATT", "ISOTONIC", "HIER_PLATT"), min_isotonic: int = 200) -> dict:
    """Fit each method on data available before ``tune_start``; score on predictions issued in the tune window."""
    train = available_before(rows, tune_start)
    issued = rows.issued_at.map(p.clock)
    window = rows[(issued >= p.clock(tune_start)) & (issued < p.clock(tune_end))]
    if competition:
        window = window[window.competition == competition]
    if window.empty:
        raise ValueError("empty tuning window")
    results = {}
    for m in methods:
        cal = fit_method(m, train, competition=competition, min_isotonic=min_isotonic)
        if cal is None:
            results[m] = dict(status="NOT_FITTED_INSUFFICIENT_ROWS", n_train=len(train))
            continue
        q = cal(window.p.to_numpy())
        results[m] = dict(status="FITTED", n_train=len(train), tune_brier=float(np.mean((q - window.y) ** 2)),
                          calibrator=cal)
    fitted = {m: r for m, r in results.items() if r["status"] == "FITTED"}
    best = min(fitted, key=lambda m: (round(fitted[m]["tune_brier"], 12), m != "IDENTITY", m))
    return dict(selected=best, results=results, tune_events=len(window))


def final_fit(rows: pd.DataFrame, method: str, fit_at, *, competition: str = "") -> Calibrator:
    """Refit the selected method on everything available at ``fit_at`` (the end of the tuning window)."""
    cal = fit_method(method, available_before(rows, fit_at), competition=competition, min_isotonic=0)
    if cal is None:
        raise ValueError("selected method cannot be refitted on the available rows")
    return cal


# ------------------------------------------------------------------------------------------ coherent grid version
def calibrate_grid(grid: ScoreGrid, home_target: float, *, total_line: float | None = None,
                   over_target: float | None = None, tol: float = 1e-12, max_iter: int = 500) -> ScoreGrid:
    """Raking: scale winner classes (home/away; draw mass held) and over/under classes to their targets jointly."""
    hv = np.arange(grid.h0, grid.h0 + grid.p.shape[0])
    av = np.arange(grid.a0, grid.a0 + grid.p.shape[1])
    margin = hv[:, None] - av[None, :]
    total = hv[:, None] + av[None, :]
    home, draw, away = margin > 0, margin == 0, margin < 0
    g = grid.p.copy()
    d = float(g[draw].sum())
    if not 0 < home_target < 1 - d:
        raise CoherenceError("home target must leave positive away mass after the fixed draw mass")
    classes = [(home, home_target), (draw, d), (away, 1 - d - home_target)] if d > 0 else \
        [(home, home_target), (away, 1 - home_target)]
    if total_line is not None:
        if over_target is None or not 0 < over_target < 1 or total_line != math.floor(total_line) + 0.5:
            raise CoherenceError("a half-point total line and an over target in (0,1) are required together")
        over = total > total_line
        classes += [(over, over_target), (~over, 1 - over_target)]
    for _ in range(max_iter):
        for mask, target in classes:
            cur = g[mask].sum()
            if cur <= 0:
                raise CoherenceError("cannot move mass into an empty class")
            g[mask] *= target / cur
        g /= g.sum()
        if max(abs(g[m].sum() - t) for m, t in classes) < tol:
            return ScoreGrid(g, grid.h0, grid.a0)
    raise CoherenceError("raking did not converge: targets incompatible with the grid's support")


# --------------------------------------------------------------------------------------------------------- report
def study(rows: pd.DataFrame, tune_start, tune_end, test_end=None) -> dict:
    """Select on [tune_start, tune_end); refit at tune_end; evaluate on predictions issued in [tune_end, test_end)."""
    sel = select(rows, tune_start, tune_end)
    cal = final_fit(rows, sel["selected"], tune_end)
    issued = rows.issued_at.map(p.clock)
    test = rows[(issued >= p.clock(tune_end)) & ((issued < p.clock(test_end)) if test_end else True)]
    q = cal(test.p.to_numpy())
    from ml.core.metrics import calibration_fit
    raw_fit, cal_fit = calibration_fit(test.p, test.y), calibration_fit(q, test.y)
    return dict(selection=sel, calibrator=cal, test_events=len(test),
                raw_brier=float(np.mean((test.p - test.y) ** 2)), calibrated_brier=float(np.mean((q - test.y) ** 2)),
                raw_slope=raw_fit["slope"], calibrated_slope=cal_fit["slope"])


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--predictions", type=Path, required=True,
                        help="CSV: issued_at,outcome_available_at,competition,p,y (out-of-sample, one family)")
    for name in ("tune-start", "tune-end"):
        parser.add_argument("--" + name, required=True)
    parser.add_argument("--test-end")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    rows = pd.read_csv(args.predictions)
    if set(rows.columns) != {"issued_at", "outcome_available_at", "competition", "p", "y"}:
        raise p.AdmissionError("exact prediction columns required; no market fields")
    res = study(rows, args.tune_start, args.tune_end, args.test_end)
    if args.out.exists():
        raise FileExistsError(args.out)
    tmp = args.out.parent / ("." + args.out.name + "." + secrets.token_hex(6))
    tmp.mkdir(parents=True)
    cal = res["calibrator"]
    rec = dict(evidence_class=EVIDENCE_CLASS, selected=res["selection"]["selected"], params=repr(cal.params),
               n_fit=cal.n, test_events=res["test_events"], raw_brier=res["raw_brier"],
               calibrated_brier=res["calibrated_brier"], raw_slope=res["raw_slope"],
               calibrated_slope=res["calibrated_slope"], predictions_sha256=p.digest(args.predictions.read_bytes()),
               tune_start=args.tune_start, tune_end=args.tune_end, code_sha256=p.source_hash(),
               generated_at=datetime.now(timezone.utc).isoformat(), deployment="NONE_STUDY_ONLY")
    (tmp / "CALIBRATION_RECEIPT.csv").write_bytes(p.csv_bytes([rec]))
    tmp.rename(args.out)
    print(f"{rec['selected']}: test Brier {rec['raw_brier']:.4f} -> {rec['calibrated_brier']:.4f} (study only)")


if __name__ == "__main__":
    main()
