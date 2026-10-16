"""Online expert-weighting study: learning-rate schedules, forgetting, context and regime alerts (Improvements 11–14).

Works on a per-event expert ledger (ml.evaluation.v3_backtest LEDGER.csv, or any ledger with the same columns):
event_id, issued_at, available_at, week, y_home, y_over and p_home_<ARM>, p_over_<ARM> for the three V3 experts,
optionally season/context and crps_* columns. Every policy sees feedback only once it was available at the next
event's issue time (delayed full information) and never the event it is weighting.

Because winner and total probabilities of a mixed grid are linear in the weights, the mixture's common-question
probabilities, and therefore its Brier losses, are exact here. Mixture CRPS is not linear; the study reports the
weight-averaged expert CRPS, which is an upper bound on the mixture's CRPS (convexity), labelled as such.

Selection is chronological: every candidate runs over the whole ledger, the schedule is chosen on events issued
before ``tune_end`` only, and only later events are evaluated. The reference is V3 itself (fixed η = 2).
STUDY ONLY: nothing here changes PRIMARY_HEDGE_MIX_V3; an adopted schedule needs a prospective shadow and an
admitted parameter row (PRIMARY_PREDICTION_PROTOCOL §3).
"""
from __future__ import annotations

import argparse
import math
import secrets
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from ml import primary as p
from ml.core.metrics import paired_week_interval

ARMS = p.ARMS
K = len(ARMS)
EVIDENCE_CLASS = "HISTORICAL_DEVELOPMENT_HEDGE_STUDY_NOT_PROSPECTIVE"


def common_losses(ledger: pd.DataFrame, alpha: float = 0.5) -> np.ndarray:
    """Per-event expert loss: alpha*Brier(home) + (1-alpha)*Brier(over); alpha=0.5 is V3's common loss."""
    if not 0 <= alpha <= 1:
        raise ValueError("alpha must lie in [0, 1]")
    ph = ledger[[f"p_home_{a}" for a in ARMS]].to_numpy(float)
    po = ledger[[f"p_over_{a}" for a in ARMS]].to_numpy(float)
    return alpha * (ph - ledger.y_home.to_numpy()[:, None]) ** 2 + (1 - alpha) * (po - ledger.y_over.to_numpy()[:, None]) ** 2


def composite_losses(ledger: pd.DataFrame, a: float, b: float, c: float, scale_margin: float, scale_total: float) -> np.ndarray:
    """Preregistered composite a*Brier(home) + b*CRPS(margin)/scale + c*CRPS(total)/scale (weights fixed in advance)."""
    if min(a, b, c) < 0 or not math.isclose(a + b + c, 1.0) or scale_margin <= 0 or scale_total <= 0:
        raise ValueError("nonnegative composite weights summing to one and positive scales required")
    ph = ledger[[f"p_home_{x}" for x in ARMS]].to_numpy(float)
    cm = ledger[[f"crps_margin_{x}" for x in ARMS]].to_numpy(float)
    ct = ledger[[f"crps_total_{x}" for x in ARMS]].to_numpy(float)
    return a * (ph - ledger.y_home.to_numpy()[:, None]) ** 2 + b * cm / scale_margin + c * ct / scale_total


def ess(w: np.ndarray) -> float:
    return float(1.0 / np.sum(np.asarray(w) ** 2))


def _softmin(cum: np.ndarray, eta: float) -> np.ndarray:
    if math.isinf(eta):
        w = (cum == cum.min()).astype(float)
    else:
        z = np.exp(-eta * (cum - cum.min()))
        w = z
    return w / w.sum()


class FixedHedge:
    """V3: weights ∝ exp(-η · cumulative loss)."""
    def __init__(self, eta: float):
        self.eta, self.cum = eta, np.zeros(K)

    def weights(self, meta) -> np.ndarray:
        return _softmin(self.cum, self.eta)

    def update(self, loss, meta) -> None:
        self.cum = self.cum + loss


class DiscountedHedge(FixedHedge):
    """Controlled forgetting: each new feedback event multiplies older cumulative loss by gamma."""
    def __init__(self, eta: float, gamma: float):
        super().__init__(eta)
        if not 0 < gamma <= 1:
            raise ValueError("gamma must lie in (0, 1]")
        self.gamma = gamma

    def update(self, loss, meta) -> None:
        self.cum = self.gamma * self.cum + loss


class SeasonResetHedge(FixedHedge):
    """Reset cumulative loss when feedback from a new season arrives (a reproducible regime rule)."""
    def __init__(self, eta: float):
        super().__init__(eta)
        self.season = None

    def update(self, loss, meta) -> None:
        if self.season is not None and meta.get("season") != self.season:
            self.cum = np.zeros(K)
        self.season = meta.get("season")
        self.cum = self.cum + loss


class ESSFloorHedge(FixedHedge):
    """Cap η so the effective number of experts never falls below ``floor`` (prevents weight collapse)."""
    def __init__(self, eta: float, floor: float):
        super().__init__(eta)
        if not 1 <= floor <= K:
            raise ValueError("ESS floor must lie in [1, K]")
        self.floor = floor

    def weights(self, meta) -> np.ndarray:
        w = _softmin(self.cum, self.eta)
        if ess(w) >= self.floor:
            return w
        lo, hi = 0.0, self.eta
        for _ in range(60):  # ESS decreases monotonically in η for fixed losses
            mid = (lo + hi) / 2
            if ess(_softmin(self.cum, mid)) >= self.floor:
                lo = mid
            else:
                hi = mid
        return _softmin(self.cum, lo)


class AdaHedge:
    """De Rooij, van Erven, Grünwald & Koolen (2014): η_t = ln K / Δ, Δ = cumulative mixability gap."""
    def __init__(self):
        self.cum, self.delta = np.zeros(K), 0.0

    def eta(self) -> float:
        return math.log(K) / self.delta if self.delta > 0 else math.inf

    def weights(self, meta) -> np.ndarray:
        return _softmin(self.cum, self.eta())

    def update(self, loss, meta) -> None:
        w, eta = self.weights(meta), self.eta()
        h = float(w @ loss)
        if math.isinf(eta):
            m = float(loss[w > 0].min())
        else:
            m = float(loss.min() - math.log(np.sum(w * np.exp(-eta * (loss - loss.min())))) / eta)
        self.delta += max(h - m, 0.0)
        self.cum = self.cum + loss


class ShrunkContextHedge:
    """Contextual weighting with shrinkage: per-context mean losses pulled toward the global mean by k pseudo-events."""
    def __init__(self, eta: float, k: float):
        self.eta, self.k = eta, k
        self.g_sum, self.g_n, self.c_sum, self.c_n = np.zeros(K), 0, {}, {}

    def weights(self, meta) -> np.ndarray:
        c = meta.get("context_key", "")
        n_c = self.c_n.get(c, 0)
        if self.g_n == 0:
            return np.ones(K) / K
        g_mean = self.g_sum / self.g_n
        mean = (self.c_sum.get(c, np.zeros(K)) + self.k * g_mean) / (n_c + self.k)
        return _softmin(mean * (n_c + self.k), self.eta)

    def update(self, loss, meta) -> None:
        c = meta.get("context_key", "")
        self.g_sum, self.g_n = self.g_sum + loss, self.g_n + 1
        self.c_sum[c] = self.c_sum.get(c, np.zeros(K)) + loss
        self.c_n[c] = self.c_n.get(c, 0) + 1


def run_policy(ledger: pd.DataFrame, policy, losses: np.ndarray, context_col: str | None = None) -> np.ndarray:
    """Weights used at each event (rows in ledger order), from feedback available by that event's issue time."""
    issued = ledger.issued_at.map(p.clock).to_numpy()
    avail = ledger.available_at.map(p.clock).to_numpy()
    order = np.argsort(issued, kind="stable")
    fb_order = list(np.argsort(avail, kind="stable"))
    out, j = np.zeros((len(ledger), K)), 0
    meta_of = lambda i: dict(season=ledger.iloc[i].get("season"),
                             context_key=str(ledger.iloc[i][context_col]) if context_col else "")
    for i in order:
        while j < len(fb_order) and avail[fb_order[j]] <= issued[i]:
            k = fb_order[j]
            if k != i:
                policy.update(losses[k], meta_of(k))
            j += 1
        out[i] = policy.weights(meta_of(i))
    return out


def mixture_scores(ledger: pd.DataFrame, w: np.ndarray) -> pd.DataFrame:
    ph = (w * ledger[[f"p_home_{a}" for a in ARMS]].to_numpy(float)).sum(axis=1)
    po = (w * ledger[[f"p_over_{a}" for a in ARMS]].to_numpy(float)).sum(axis=1)
    out = pd.DataFrame(dict(event_id=ledger.event_id, week=ledger.week,
                            brier_home=(ph - ledger.y_home) ** 2, brier_over=(po - ledger.y_over) ** 2))
    out["common_loss"] = 0.5 * (out.brier_home + out.brier_over)
    for col in ("crps_margin", "crps_total"):
        if all(f"{col}_{a}" in ledger for a in ARMS):
            out[col + "_bound"] = (w * ledger[[f"{col}_{a}" for a in ARMS]].to_numpy(float)).sum(axis=1)
    out["ess"] = [ess(x) for x in w]
    out["max_weight"] = w.max(axis=1)
    return out


def default_candidates() -> dict:
    cands = {"V3_FIXED_ETA_2": lambda: FixedHedge(2.0), "ADAHEDGE": AdaHedge}
    for eta in (0.5, 1, 5, 10, 20):
        cands[f"FIXED_ETA_{eta:g}"] = (lambda e: lambda: FixedHedge(e))(eta)
    for gamma in (0.99, 0.995, 0.999):
        cands[f"DISCOUNTED_ETA_2_G{gamma:g}"] = (lambda g: lambda: DiscountedHedge(2.0, g))(gamma)
    for floor in (1.5, 2.0):
        cands[f"ESS_FLOOR_{floor:g}_ETA_20"] = (lambda f: lambda: ESSFloorHedge(20.0, f))(floor)
    cands["SEASON_RESET_ETA_2"] = lambda: SeasonResetHedge(2.0)
    return cands


def page_hinkley(series: np.ndarray, delta: float = 0.005, threshold: float = 0.5) -> int | None:
    """Index of the first upward mean-shift alarm (Page 1954 / Hinkley 1971), or None."""
    mean, cum, low = 0.0, 0.0, 0.0
    for t, x in enumerate(series, 1):
        mean += (x - mean) / t
        cum += x - mean - delta
        low = min(low, cum)
        if cum - low > threshold:
            return t - 1
    return None


def regime_alerts(ledger: pd.DataFrame, losses: np.ndarray, **kw) -> pd.DataFrame:
    """Pairwise loss-difference alarms in availability order: 'expert i became worse than expert j'."""
    order = np.argsort(ledger.available_at.map(p.clock).to_numpy(), kind="stable")
    rows = []
    for i in range(K):
        for j in range(K):
            if i != j:
                idx = page_hinkley((losses[order, i] - losses[order, j]), **kw)
                rows.append(dict(worse=ARMS[i], than=ARMS[j], alarm=idx is not None,
                                 event_id=ledger.iloc[order[idx]].event_id if idx is not None else "",
                                 available_at=ledger.iloc[order[idx]].available_at if idx is not None else ""))
    return pd.DataFrame(rows)


def study(ledger: pd.DataFrame, tune_end, *, candidates: dict | None = None, alpha: float = 0.5,
          context_col: str | None = None) -> dict:
    tune_end = p.clock(tune_end)
    issued = ledger.issued_at.map(p.clock)
    tune, test = issued < tune_end, issued >= tune_end
    if not tune.any() or not test.any():
        raise ValueError("both a tuning window and a later evaluation window are required")
    losses = common_losses(ledger, alpha)
    candidates = dict(candidates or default_candidates())
    if context_col:
        for k in (5.0, 20.0):
            candidates[f"CONTEXT_SHRUNK_ETA_2_K{k:g}"] = (lambda kk: lambda: ShrunkContextHedge(2.0, kk))(k)
    scores = {}
    for name, make in candidates.items():
        w = run_policy(ledger, make(), losses, context_col)
        scores[name] = mixture_scores(ledger, w)
    tune_loss = {n: float(s.common_loss[tune.to_numpy()].mean()) for n, s in scores.items()}
    selected = min(sorted(tune_loss), key=lambda n: tune_loss[n])
    ref = scores["V3_FIXED_ETA_2"][test.to_numpy()]
    summary, paired = [], []
    for name, s in scores.items():
        t = s[test.to_numpy()]
        summary.append(dict(policy=name, selected=name == selected, tune_common_loss=tune_loss[name],
                            test_events=len(t), test_common_loss=float(t.common_loss.mean()),
                            test_brier_home=float(t.brier_home.mean()), test_brier_over=float(t.brier_over.mean()),
                            mean_ess=float(t.ess.mean()), collapsed_share=float((t.max_weight > 0.99).mean()),
                            **{c: float(t[c].mean()) for c in ("crps_margin_bound", "crps_total_bound") if c in t}))
        if name != "V3_FIXED_ETA_2":
            iv = paired_week_interval(t.common_loss - ref.common_loss, t.event_id, t.week)
            paired.append(dict(policy=name, reference="V3_FIXED_ETA_2", metric="common_loss", **iv))
    return dict(selected=selected, summary=pd.DataFrame(summary), paired=pd.DataFrame(paired),
                alerts=regime_alerts(ledger[tune.to_numpy()].reset_index(drop=True), losses[tune.to_numpy()]))


def write(result: dict, out: Path, receipt: dict) -> None:
    from ml.evaluation.report import md_table
    out = Path(out)
    if out.exists():
        raise FileExistsError(out)
    tmp = out.parent / ("." + out.name + "." + secrets.token_hex(6))
    tmp.mkdir(parents=True)
    for name in ("summary", "paired", "alerts"):
        result[name].to_csv(tmp / f"{name.upper()}.csv", index=False, lineterminator="\n")
    receipt = dict(receipt, evidence_class=EVIDENCE_CLASS, selected_on_tune_window=result["selected"],
                   **{f"{n}_csv_sha256": p.digest((tmp / f"{n.upper()}.csv").read_bytes()) for n in ("summary", "paired", "alerts")})
    (tmp / "RECEIPT.csv").write_bytes(p.csv_bytes([receipt]))
    s, pr, al = result["summary"], result["paired"], result["alerts"]
    lines = ["# Hedge schedule study", "", f"**Evidence class: `{EVIDENCE_CLASS}`.** Schedules chosen on the tune "
             "window only, evaluated afterwards on identical events; reference = V3 fixed η = 2. CRPS columns are "
             "weight-averaged expert CRPS (upper bounds on the mixture). Study only; PRIMARY_HEDGE_MIX_V3 unchanged.",
             "", md_table(s, list(s.columns), 4), "", md_table(pr, list(pr.columns), 4) if len(pr) else "", "",
             "## Regime alerts (tune window, Page–Hinkley)", "", md_table(al, list(al.columns), 4), "", "## Receipt", "",
             "\n".join(f"- `{k}`: {v}" for k, v in receipt.items())]
    (tmp / "RESULTS.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    tmp.rename(out)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--ledger", type=Path, required=True, help="V3 backtest LEDGER.csv")
    parser.add_argument("--tune-end", required=True)
    parser.add_argument("--context-column")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)
    code = p.source_hash()
    ledger = pd.read_csv(args.ledger)
    result = study(ledger, args.tune_end, context_col=args.context_column)
    write(result, args.out, dict(ledger=str(args.ledger), ledger_sha256=p.digest(args.ledger.read_bytes()),
                                 tune_end=args.tune_end, code_sha256=code, repository_head=p.repository_head(),
                                 generated_at=datetime.now(timezone.utc).isoformat()))
    print(f"selected on tune window: {result['selected']} -> {args.out}")


if __name__ == "__main__":
    main()
