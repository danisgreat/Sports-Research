"""Gradient-boosted regression trees for distribution parameters, with no third-party ML dependency (ML-06).

The challenger predicts the PARAMETERS of the score distribution (a Poisson rate, a Gaussian mean, a log-variance) and the engine
turns them into one coherent score grid, so every derived contract stays coherent. It does not predict binary outcomes.

  PoissonBoost         log-rate with Newton boosting on the Poisson deviance (goals, runs)
  GaussianBoost        mean with squared loss (points)
  LogVarianceBoost     heteroscedastic width: log sigma^2 given the mean residuals (a Newton version of NGBoost's second parameter)

Trees are histogram-based (<= 64 bins), depth-limited, with L2-regularised Newton leaves, row subsampling and chronological early
stopping (the validation block is the LAST rows, never a random split). Everything is deterministic given the seed. Fitting
failures raise; there is no silent fallback to a constant model.
"""

from dataclasses import dataclass, field
from typing import List, Optional, Tuple

import numpy as np

from .errors import FitFailed, InsufficientData, NotFitted

MAX_BINS = 64


class Binner:
    """Quantile bin edges per feature; NaN goes to its own bin 0."""

    def __init__(self, n_bins: int = MAX_BINS):
        self.n_bins = min(n_bins, MAX_BINS)
        self.edges: List[np.ndarray] = []

    def fit(self, X: np.ndarray) -> "Binner":
        self.edges = []
        for j in range(X.shape[1]):
            col = X[:, j]
            col = col[np.isfinite(col)]
            if len(col) == 0:
                self.edges.append(np.array([]))
                continue
            qs = np.unique(np.quantile(col, np.linspace(0, 1, self.n_bins)[1:-1]))
            self.edges.append(qs)
        return self

    def transform(self, X: np.ndarray) -> np.ndarray:
        out = np.zeros(X.shape, dtype=np.uint8)
        for j, edges in enumerate(self.edges):
            col = X[:, j]
            idx = np.searchsorted(edges, col, side="right") + 1          # bins 1..len(edges)+1
            idx = np.where(np.isfinite(col), idx, 0)
            out[:, j] = idx.astype(np.uint8)
        return out


@dataclass
class Tree:
    feature: np.ndarray = field(default_factory=lambda: np.array([], dtype=int))     # -1 for leaves
    threshold: np.ndarray = field(default_factory=lambda: np.array([], dtype=int))   # go left if bin <= threshold
    left: np.ndarray = field(default_factory=lambda: np.array([], dtype=int))
    right: np.ndarray = field(default_factory=lambda: np.array([], dtype=int))
    value: np.ndarray = field(default_factory=lambda: np.array([], dtype=float))

    def predict(self, Xb: np.ndarray) -> np.ndarray:
        node = np.zeros(len(Xb), dtype=int)
        for _ in range(64):
            feat = self.feature[node]
            leaf = feat < 0
            if leaf.all():
                break
            go_left = Xb[np.arange(len(Xb)), np.where(leaf, 0, feat)] <= self.threshold[node]
            nxt = np.where(go_left, self.left[node], self.right[node])
            node = np.where(leaf, node, nxt)
        return self.value[node]


def _fit_tree(Xb: np.ndarray, g: np.ndarray, h: np.ndarray, max_depth: int, min_leaf: int, l2: float, n_bins: int) -> Tree:
    """Greedy depth-wise Newton tree on binned features: leaf value = -G / (H + l2)."""
    feature, threshold, left, right, value = [], [], [], [], []

    def add_leaf(rows: np.ndarray) -> int:
        feature.append(-1)
        threshold.append(0)
        left.append(-1)
        right.append(-1)
        value.append(float(-g[rows].sum() / (h[rows].sum() + l2)))
        return len(feature) - 1

    def grow(rows: np.ndarray, depth: int) -> int:
        node = add_leaf(rows)
        if depth >= max_depth or len(rows) < 2 * min_leaf:
            return node
        G, H = g[rows].sum(), h[rows].sum()
        parent = G * G / (H + l2)
        best = (1e-9, -1, 0)
        for j in range(Xb.shape[1]):
            col = Xb[rows, j]
            gj = np.bincount(col, weights=g[rows], minlength=n_bins + 2)
            hj = np.bincount(col, weights=h[rows], minlength=n_bins + 2)
            nj = np.bincount(col, minlength=n_bins + 2)
            gl, hl, nl = np.cumsum(gj)[:-1], np.cumsum(hj)[:-1], np.cumsum(nj)[:-1]
            gr, hr, nr = G - gl, H - hl, len(rows) - nl
            ok = (nl >= min_leaf) & (nr >= min_leaf)
            if not ok.any():
                continue
            gain = np.where(ok, gl * gl / (hl + l2) + gr * gr / (hr + l2) - parent, -np.inf)
            k = int(np.argmax(gain))
            if gain[k] > best[0]:
                best = (float(gain[k]), j, k)
        if best[1] < 0:
            return node
        _, j, k = best
        mask = Xb[rows, j] <= k
        feature[node], threshold[node] = j, k
        left[node] = grow(rows[mask], depth + 1)
        right[node] = grow(rows[~mask], depth + 1)
        return node

    grow(np.arange(len(Xb)), 0)
    return Tree(np.array(feature), np.array(threshold), np.array(left), np.array(right), np.array(value))


class _Boost:
    """Shared boosting loop; subclasses define the link, the gradient/Hessian and the validation loss."""

    def __init__(self, n_estimators: int = 200, learning_rate: float = 0.05, max_depth: int = 3, min_leaf: int = 40, l2: float = 5.0,
                 subsample: float = 0.8, validation_fraction: float = 0.15, patience: int = 20, seed: int = 0):
        if not 0 < learning_rate <= 1 or max_depth < 1 or n_estimators < 1:
            raise ValueError("invalid boosting hyper-parameters")
        self.n_estimators, self.learning_rate, self.max_depth, self.min_leaf, self.l2 = n_estimators, learning_rate, max_depth, min_leaf, l2
        self.subsample, self.validation_fraction, self.patience, self.seed = subsample, validation_fraction, patience, seed
        self.binner: Optional[Binner] = None
        self.trees: List[Tree] = []
        self.base: float = 0.0
        self.best_iteration: int = 0
        self.validation_curve: List[float] = []

    # to be provided
    def _init(self, y: np.ndarray) -> float:
        raise NotImplementedError

    def _grad_hess(self, y: np.ndarray, F: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        raise NotImplementedError

    def _loss(self, y: np.ndarray, F: np.ndarray) -> float:
        raise NotImplementedError

    def fit(self, X: np.ndarray, y: np.ndarray, offset: Optional[np.ndarray] = None) -> "_Boost":
        X, y = np.asarray(X, dtype=float), np.asarray(y, dtype=float)
        if X.ndim != 2 or y.shape != (len(X),):
            raise ValueError("X must be (n, k) and y (n,)")
        if len(X) < 4 * self.min_leaf:
            raise InsufficientData(f"need at least {4 * self.min_leaf} rows, got {len(X)}")
        if not np.isfinite(y).all():
            raise ValueError("y must be finite")
        self._check_y(y)
        n_val = int(len(X) * self.validation_fraction)
        n_fit = len(X) - n_val
        self.binner = Binner().fit(X[:n_fit])
        Xb = self.binner.transform(X)
        off = np.zeros(len(y)) if offset is None else np.asarray(offset, dtype=float)
        self.base = self._init(y[:n_fit] - 0.0)
        F = np.full(len(y), self.base) + off
        rng = np.random.default_rng(self.seed)
        best_loss, since_best, self.trees, self.validation_curve = np.inf, 0, [], []
        keep = 0
        for it in range(self.n_estimators):
            g, h = self._grad_hess(y[:n_fit], F[:n_fit])
            rows = np.flatnonzero(rng.random(n_fit) < self.subsample) if self.subsample < 1.0 else np.arange(n_fit)
            if len(rows) < 2 * self.min_leaf:
                rows = np.arange(n_fit)
            tree = _fit_tree(Xb[rows], g[rows], h[rows], self.max_depth, self.min_leaf, self.l2, MAX_BINS)
            self.trees.append(tree)
            F = F + self.learning_rate * tree.predict(Xb)
            if n_val:
                loss = self._loss(y[n_fit:], F[n_fit:])
                self.validation_curve.append(loss)
                if not np.isfinite(loss):
                    raise FitFailed(type(self).__name__, "validation loss became non-finite")
                if loss < best_loss - 1e-9:
                    best_loss, since_best, keep = loss, 0, it + 1
                else:
                    since_best += 1
                    if since_best >= self.patience:
                        break
            else:
                keep = it + 1
        self.trees = self.trees[:keep]
        self.best_iteration = keep
        if not self.trees:
            raise FitFailed(type(self).__name__, "no boosting round improved the validation loss")
        return self

    def _check_y(self, y: np.ndarray) -> None:
        return None

    def decision(self, X: np.ndarray, offset: Optional[np.ndarray] = None) -> np.ndarray:
        if self.binner is None or not self.trees:
            raise NotFitted(f"{type(self).__name__}: fit before predicting")
        Xb = self.binner.transform(np.asarray(X, dtype=float))
        F = np.full(len(Xb), self.base) + (0.0 if offset is None else np.asarray(offset, dtype=float))
        for tree in self.trees:
            F = F + self.learning_rate * tree.predict(Xb)
        return F


class PoissonBoost(_Boost):
    """log mu = base + sum of trees; Newton boosting on the Poisson negative log-likelihood."""

    def _check_y(self, y: np.ndarray) -> None:
        if (y < 0).any():
            raise ValueError("Poisson targets must be non-negative")

    def _init(self, y: np.ndarray) -> float:
        return float(np.log(max(y.mean(), 1e-3)))

    def _grad_hess(self, y: np.ndarray, F: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        mu = np.exp(np.clip(F, -10, 10))
        return mu - y, mu

    def _loss(self, y: np.ndarray, F: np.ndarray) -> float:
        mu = np.exp(np.clip(F, -10, 10))
        return float(np.mean(mu - y * np.log(np.maximum(mu, 1e-12))))

    def predict(self, X: np.ndarray, offset: Optional[np.ndarray] = None) -> np.ndarray:
        return np.exp(np.clip(self.decision(X, offset), -10, 10))


class GaussianBoost(_Boost):
    """mean = base + sum of trees; squared loss."""

    def _init(self, y: np.ndarray) -> float:
        return float(y.mean())

    def _grad_hess(self, y: np.ndarray, F: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        return F - y, np.ones_like(y)

    def _loss(self, y: np.ndarray, F: np.ndarray) -> float:
        return float(np.mean((F - y) ** 2))

    def predict(self, X: np.ndarray, offset: Optional[np.ndarray] = None) -> np.ndarray:
        return self.decision(X, offset)


class LogVarianceBoost(_Boost):
    """log sigma^2 given squared residuals r2: loss 0.5 (v + r2 exp(-v)), Newton step with Hessian 0.5 r2 exp(-v)."""

    def _check_y(self, y: np.ndarray) -> None:
        if (y < 0).any():
            raise ValueError("squared residuals must be non-negative")

    def _init(self, y: np.ndarray) -> float:
        return float(np.log(max(y.mean(), 1e-6)))

    def _grad_hess(self, y: np.ndarray, F: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        e = y * np.exp(-np.clip(F, -20, 20))
        return 0.5 * (1.0 - e), np.maximum(0.5 * e, 0.05)

    def _loss(self, y: np.ndarray, F: np.ndarray) -> float:
        return float(np.mean(0.5 * (F + y * np.exp(-np.clip(F, -20, 20)))))

    def predict_sd(self, X: np.ndarray, offset: Optional[np.ndarray] = None) -> np.ndarray:
        return np.sqrt(np.exp(np.clip(self.decision(X, offset), -20, 20)))
