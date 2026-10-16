"""Basketball feature challenger (BKB-FEATURE-RIDGE-C1) and its chronological ablation study.

Challenger C of the improvement plan: regularised linear regression of regulation home and away points on
point-in-time FEAT-v1 features (L5/L10/L15/L20 scoring, exponential decay, opponent-adjusted form, venue split,
season baseline, rest, possessions-based ratings/pace where sourced, confirmed availability counts), with residual
covariance giving ONE joint score distribution per game. Winner, handicap and total probabilities are projections
of that grid (overtime handled exactly as the V3 Gaussian experts), never separately fitted rows.

Status: DEVELOPMENT_EXPERIMENT. It never enters primary cards. Its forecasts can only be frozen as prospective
shadows (ml.evaluation.prospective). The ablation compares feature sets and tail shapes against the exact V3
experts (``primary._fit_models``) on identical games, refitting weekly from rows whose labels were known by then.
Leagues are never pooled here; each release is one exact competition.
"""
from __future__ import annotations

import argparse
import math
import secrets
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from ml import primary as p
from ml import training_admission as ta
from ml.config import League
from ml.core.distributions import ScoreGrid
from ml.core.metrics import paired_week_interval
from ml.models.common import FitError, apply_tie_rule, normal_extra

MODEL_ID = "BKB-FEATURE-RIDGE-C1"
EVIDENCE_CLASS = "HISTORICAL_DEVELOPMENT_ABLATION_NOT_PROSPECTIVE"
_W = lambda stem: [f"home_{stem}_pf", f"home_{stem}_pa", f"away_{stem}_pf", f"away_{stem}_pa"]
FEATURE_SETS = {
    "BASE": [],
    "L5": _W("L5"), "L10": _W("L10"), "L20": _W("L20"), "DECAY": _W("decay"),
    "MULTI": _W("L5") + _W("L10") + _W("L20"),
}
FEATURE_SETS["FULL"] = FEATURE_SETS["MULTI"] + _W("decay") + [
    f"{s}_{f}" for s in ("home", "away") for f in (
        "oppadj_L10_net", "venue_L20_net", "season_net", "rest_days", "L10_pace", "L10_ortg", "L10_drtg",
        "confirmed_out", "lineup_confirmed")]
V3_ARMS = tuple("V3_" + a for a in p.ARMS)
TAIL_SCALES = {"normal": ((1.0, 1.0),), "scale_mixture": ((0.8, 0.79), (0.2, 1.58))}  # equal total variance


@dataclass(frozen=True)
class RidgeParams:
    alpha: float = 10.0
    inflation: float = 1.0
    tail: str = "normal"

    def __post_init__(self):
        if not (math.isfinite(self.alpha) and self.alpha >= 0 and math.isfinite(self.inflation) and self.inflation > 0
                and self.tail in TAIL_SCALES):
            raise ValueError("invalid ridge/inflation/tail parameters")


class FeatureRidge:
    def __init__(self, lg: League, features: list[str], params: RidgeParams):
        self.lg, self.features, self.params = lg, list(features), params

    def _design(self, rows: pd.DataFrame, fit: bool) -> np.ndarray:
        cols = []
        if fit:
            self.columns, self.centre, self.sds = [], {}, {}
            for f in self.features:
                x = pd.to_numeric(rows.get(f), errors="coerce") if f in rows else pd.Series(np.nan, index=rows.index)
                if x.notna().sum() < 2:
                    continue  # never observed in training: dropped and recorded, not imputed from nothing
                mean = float(x.mean())
                filled = x.fillna(mean)
                sd = float(filled.std(ddof=0))
                if sd > 0:
                    self.columns.append(f)
                    self.centre[f], self.sds[f] = mean, sd
                if x.isna().any() and x.notna().any():
                    self.columns.append(f + "__missing")
                    ind = x.isna().astype(float)
                    self.centre[f + "__missing"], self.sds[f + "__missing"] = float(ind.mean()), float(ind.std(ddof=0)) or 1.0
        for c in self.columns:
            base = c[:-9] if c.endswith("__missing") else c
            x = pd.to_numeric(rows.get(base), errors="coerce") if base in rows else pd.Series(np.nan, index=rows.index)
            v = x.isna().astype(float) if c.endswith("__missing") else x.fillna(self.centre[c])
            cols.append(((v - self.centre[c]) / self.sds[c]).to_numpy(float))
        return np.column_stack(cols) if cols else np.zeros((len(rows), 0))

    def fit(self, rows: pd.DataFrame, fit_at: pd.Timestamp) -> "FeatureRidge":
        fit_at = p.clock(fit_at)
        if len(rows) < 30:
            raise FitError(f"only {len(rows)} training rows")
        if (rows.event_at >= fit_at).any() or (rows.label_available_at > fit_at).any():
            raise FitError("training rows or labels not known by the fit time (leakage)")
        X = self._design(rows, fit=True)
        y = rows[["reg_hs", "reg_as"]].to_numpy(float)
        self.intercept = y.mean(axis=0)
        A = X.T @ X + self.params.alpha * np.eye(X.shape[1])
        try:
            self.beta = np.linalg.solve(A, X.T @ (y - self.intercept)) if X.shape[1] else np.zeros((0, 2))
        except np.linalg.LinAlgError as e:
            raise FitError(str(e)) from e
        resid = y - (self.intercept + X @ self.beta)
        cov = np.cov(resid.T, ddof=1) * self.params.inflation
        if not np.isfinite(cov).all() or np.linalg.det(cov) <= 0:
            raise FitError("residual covariance not positive definite")
        self.cov = cov
        self.sd_margin = float(np.sqrt(cov[0, 0] + cov[1, 1] - 2 * cov[0, 1]))
        return self

    def means(self, rows: pd.DataFrame) -> np.ndarray:
        return self.intercept + self._design(rows, fit=False) @ self.beta

    def grid(self, row: pd.DataFrame) -> ScoreGrid:
        mh, ma = (max(float(v), 0.5) for v in self.means(row)[0])
        parts = [ScoreGrid.bivariate_normal(mh, ma, self.cov * s * s) for _, s in TAIL_SCALES[self.params.tail]]
        g = parts[0] if len(parts) == 1 else p.mix_grids(parts, [w for w, _ in TAIL_SCALES[self.params.tail]])
        return apply_tie_rule(g, self.lg, normal_extra(self.lg, mh - ma, self.sd_margin, mh + ma, 0.0))


# -------------------------------------------------------------------------------------------------------- scoring
def _interval(support: np.ndarray, mass: np.ndarray, level: float) -> tuple[int, int]:
    cdf = np.cumsum(mass)
    lo = support[np.searchsorted(cdf, (1 - level) / 2 - 1e-12)]
    hi = support[min(np.searchsorted(cdf, 1 - (1 - level) / 2 - 1e-12), len(support) - 1)]
    return int(lo), int(hi)


def score_grid(g: ScoreGrid, hs: int, as_: int) -> dict:
    ph = g.winner()[0]
    y = float(hs > as_)
    out = dict(p_home=ph, brier_home=(ph - y) ** 2,
               logloss_home=-math.log(max(ph if y else 1 - ph, 1e-12)),
               crps_margin=g.crps_margin(hs - as_), crps_total=g.crps_total(hs + as_))
    mh, ma = g.means()
    out.update(err_margin=(mh - ma) - (hs - as_), err_total=(mh + ma) - (hs + as_))
    for name, (sup, mass), y_val in (("margin", g.margin_pmf(), hs - as_), ("total", g.total_pmf(), hs + as_)):
        for level in (0.5, 0.8, 0.95):
            lo, hi = _interval(sup, mass, level)
            out[f"cover{int(level * 100)}_{name}"] = float(lo <= y_val <= hi)
    return out


def _v3_frame(rows: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(dict(date=rows.event_at.map(lambda t: t.tz_convert("UTC").tz_localize(None)),
                             event_id=rows.event_uid, season=rows.season.astype(int), home=rows.home, away=rows.away,
                             hs=rows.hs.astype(int), as_=rows.as_.astype(int), reg_hs=rows.reg_hs.astype(int),
                             reg_as=rows.reg_as.astype(int), decision=rows.decision.fillna("").astype(str),
                             final_at=rows.label_available_at.map(lambda t: t.tz_localize(None)),
                             available_at=rows.label_available_at.map(lambda t: t.tz_localize(None))))


def week_start(t: pd.Timestamp) -> pd.Timestamp:
    t = t.tz_convert("UTC").normalize()
    return t - pd.Timedelta(days=t.weekday())


def rolling(rows: pd.DataFrame, lg: League, arms: dict, start, end=None) -> pd.DataFrame:
    """Weekly refits; each arm is fitted only on rows whose game and label were known by that Monday.

    ``arms`` maps name -> (feature list, RidgeParams) or the literal "V3" for the three exact V3 experts.
    """
    start = p.clock(start)
    test = rows[(rows.event_at >= start) & ((rows.event_at < p.clock(end)) if end is not None else True)]
    out = []
    for ws, block in test.groupby(test.event_at.map(week_start), sort=True):
        train = rows[(rows.event_at < ws) & (rows.label_available_at <= ws)]
        fitted = {}
        for name, spec in arms.items():
            try:
                if spec == "V3":
                    pricers, _ = p._fit_models(lg, _v3_frame(train), ws.tz_localize(None))
                    for arm in p.ARMS:
                        fitted["V3_" + arm] = ("V3", pricers[arm])
                else:
                    fitted[name] = ("RIDGE", FeatureRidge(lg, spec[0], spec[1]).fit(train, ws))
            except FitError:
                continue
        for r in block.itertuples():
            frame = block[block.event_uid == r.event_uid]
            for name, (kind, m) in fitted.items():
                try:
                    if kind == "V3":
                        g, flags = m(r.home, r.away, "")
                        if flags:
                            continue  # V3 refuses unseen teams; the event is dropped from paired comparisons
                    else:
                        g = m.grid(frame)
                except (FitError, ValueError):
                    continue
                out.append(dict(event_uid=r.event_uid, event_at=r.event_at, week=ws.date().isoformat(), arm=name,
                                **score_grid(g, int(r.hs), int(r.as_))))
    return pd.DataFrame(out)


def complete_events(scored: pd.DataFrame) -> pd.DataFrame:
    """Keep only events scored by every arm, so all comparisons use identical games."""
    if scored.empty:
        return scored
    arms = scored.arm.nunique()
    keep = scored.groupby("event_uid").arm.nunique()
    return scored[scored.event_uid.isin(keep[keep == arms].index)].reset_index(drop=True)


def _composite(frame: pd.DataFrame, scale: float) -> float:
    return float((frame.brier_home + 0.5 * (frame.crps_margin + frame.crps_total) / scale).mean())


def ablate(rows: pd.DataFrame, lg: League, tune_start, test_start, *, alphas=(1.0, 10.0, 100.0),
           inflations=(1.0, 1.15), tails=("normal", "scale_mixture")) -> dict:
    """Tune each feature set on [tune_start, test_start), then evaluate all arms on [test_start, end)."""
    tune_start, test_start = p.clock(tune_start), p.clock(test_start)
    if not tune_start < test_start:
        raise ValueError("tuning window must precede the test window")
    early = rows[rows.event_at < tune_start]
    scale = float((early.hs - early.as_).std()) if len(early) > 2 else 10.0
    chosen = {}
    for name, feats in FEATURE_SETS.items():
        grid = [RidgeParams(a, i, t) for a in alphas for i in inflations for t in tails]
        scored = complete_events(rolling(rows, lg, {str(k): (feats, prm) for k, prm in enumerate(grid)},
                                         tune_start, test_start))
        if scored.empty:
            continue
        best = min(range(len(grid)), key=lambda k: (_composite(scored[scored.arm == str(k)], scale), k))
        chosen[name] = grid[best]
    if not chosen:
        raise FitError("no feature set could be tuned (insufficient rows before the tune window)")
    arms = {name: (FEATURE_SETS[name], prm) for name, prm in chosen.items()}
    arms["V3"] = "V3"
    test = complete_events(rolling(rows, lg, arms, test_start))
    return dict(chosen=chosen, scale=scale, test=test)


def summarise(test: pd.DataFrame, reference: str = "BASE") -> tuple[pd.DataFrame, pd.DataFrame]:
    metrics = ["brier_home", "logloss_home", "crps_margin", "crps_total", "cover50_margin", "cover80_margin",
               "cover95_margin", "cover50_total", "cover80_total", "cover95_total"]
    summary = test.groupby("arm")[metrics].mean()
    summary["mae_margin"] = test.groupby("arm").err_margin.apply(lambda e: e.abs().mean())
    summary["mae_total"] = test.groupby("arm").err_total.apply(lambda e: e.abs().mean())
    summary["events"] = test.groupby("arm").event_uid.nunique()
    paired = []
    for ref in [reference] + [a for a in V3_ARMS if a in set(test.arm)]:
        if ref not in set(test.arm):
            continue
        base = test[test.arm == ref].set_index("event_uid")
        for arm in sorted(set(test.arm) - {ref}):
            cand = test[test.arm == arm].set_index("event_uid").reindex(base.index)
            for metric in ("brier_home", "crps_margin", "crps_total"):
                iv = paired_week_interval(cand[metric] - base[metric], pd.Series(base.index), base.week)
                paired.append(dict(arm=arm, reference=ref, metric=metric, **iv))
    return summary.reset_index(), pd.DataFrame(paired)


def write_ablation(result: dict, out: Path, receipt: dict) -> None:
    from ml.evaluation.report import md_table
    if Path(out).exists():
        raise FileExistsError(out)
    summary, paired = summarise(result["test"])
    tmp = Path(out).parent / ("." + Path(out).name + "." + secrets.token_hex(6))
    tmp.mkdir(parents=True)
    result["test"].to_csv(tmp / "ABLATION_ROWS.csv", index=False, lineterminator="\n")
    summary.to_csv(tmp / "ABLATION_SUMMARY.csv", index=False, lineterminator="\n")
    paired.to_csv(tmp / "PAIRED.csv", index=False, lineterminator="\n")
    tuned = pd.DataFrame([dict(feature_set=k, alpha=v.alpha, inflation=v.inflation, tail=v.tail)
                          for k, v in result["chosen"].items()])
    tuned.to_csv(tmp / "TUNED_PARAMETERS.csv", index=False, lineterminator="\n")
    receipt = dict(receipt, evidence_class=EVIDENCE_CLASS, model_id=MODEL_ID, scale=result["scale"],
                   **{f.lower().replace(".", "_") + "_sha256": p.digest((tmp / f).read_bytes())
                      for f in ("ABLATION_ROWS.csv", "ABLATION_SUMMARY.csv", "PAIRED.csv", "TUNED_PARAMETERS.csv")})
    (tmp / "RECEIPT.csv").write_bytes(p.csv_bytes([receipt]))
    cols = list(summary.columns)
    lines = [f"# {MODEL_ID} ablation", "", f"**Evidence class: `{EVIDENCE_CLASS}`.** One exact competition; weekly "
             "refits from rows whose game and label were known by each Monday; feature sets tuned (alpha, covariance "
             "inflation, tail) on the tune window only; every arm scored on identical games. Negative paired means "
             "favour the arm. Fewer than eight weeks is INSUFFICIENT_EVIDENCE; this is not prospective validation "
             "and promotes nothing.", "", "## Test-window summary", "", md_table(summary, cols, 4), "",
             "## Paired differences (arm − reference)", "",
             md_table(paired, list(paired.columns), 4) if len(paired) else "No paired rows.", "",
             "## Tuned parameters (tune window only)", "", md_table(tuned, list(tuned.columns), 4), "", "## Receipt", "",
             "\n".join(f"- `{k}`: {v}" for k, v in receipt.items())]
    (tmp / "RESULTS.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    tmp.rename(out)


def league_from_source(path: Path) -> League:
    rows = p.read_rows(path)
    if len(rows) != 1:
        raise p.AdmissionError("one reviewed competition source row required")
    now = datetime.now(timezone.utc).isoformat()
    request = dict(competition=rows[0]["sport"] + "/" + rows[0]["competition"], endpoint=rows[0]["endpoint"],
                   scheduled_start=now, issue_at=now)
    lg = p.reviewed_source_league(request, rows[0])
    if lg.sport != "Basketball":
        raise p.AdmissionError("the basketball challenger applies to basketball competitions only")
    return lg


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    a = sub.add_parser("ablate")
    a.add_argument("--release", type=Path, required=True)
    a.add_argument("--competition-source", type=Path, required=True)
    a.add_argument("--tune-start", required=True)
    a.add_argument("--test-start", required=True)
    a.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    code = p.source_hash()
    lg = league_from_source(args.competition_source)
    man = ta.verify_release(args.release, rebuild=False)
    if man["competition"] != lg.path:
        raise p.AdmissionError("release competition differs from the reviewed competition source")
    result = ablate(ta.load_rows(args.release), lg, args.tune_start, args.test_start)
    if p.source_hash() != code:
        raise RuntimeError("generating source changed during the ablation")
    write_ablation(result, args.out, dict(release_id=man["release_id"], release_rows_sha256=man["rows_csv_sha256"],
                                          tune_start=args.tune_start, test_start=args.test_start, code_sha256=code,
                                          repository_head=p.repository_head(),
                                          generated_at=datetime.now(timezone.utc).isoformat()))
    print(f"ablation written to {args.out}")


if __name__ == "__main__":
    main()
