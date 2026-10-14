"""Contextual bandit (linear Thompson sampling with exponential forgetting) for stake sizing.

Arms are stake multipliers. Reward is stake x closing-line value, observed at the close (before the result).
Monte Carlo estimates a posterior arm distribution; actions are sampled FROM that distribution.
The returned probabilities are therefore the actual conditional behaviour probabilities, not estimates
of a separately sampled action's propensity.
"""
from __future__ import annotations

import numpy as np


def _validate_config(d, arms, lam, gamma):
    if not isinstance(d, (int, np.integer)) or d <= 0 or len(arms) < 2 or len(set(arms)) != len(arms):
        raise ValueError("positive context dimension and distinct action arms required")
    if not np.isfinite(arms).all() or min(arms) < 0 or not np.isfinite(lam) or lam <= 0 or not np.isfinite(gamma) or not 0 <= gamma <= 1:
        raise ValueError("invalid stake arms, ridge or forgetting factor")


def _context(x, d):
    x = np.asarray(x, float)
    if x.shape != (d,) or not np.isfinite(x).all():
        raise ValueError("context must be a finite vector of the configured dimension")
    return x


class LinTS:
    def __init__(self, d: int, arms: tuple[float, ...] = (0.0, 0.25, 0.5), lam: float = 1.0, v: float = 0.05,
                 gamma: float = 0.999, seed: int = 20261014):
        _validate_config(d, arms, lam, gamma)
        if not np.isfinite(v) or v < 0:
            raise ValueError("posterior scale must be finite and nonnegative")
        self.arms = arms
        self.d = d
        self.A = [lam * np.eye(d) for _ in arms]
        self.b = [np.zeros(d) for _ in arms]
        self.v, self.gamma, self.lam = v, gamma, lam
        self.rng = np.random.default_rng(seed)

    def _sample_scores(self, x: np.ndarray, n: int = 1) -> np.ndarray:
        out = np.empty((n, len(self.arms)))
        for k, (A, b) in enumerate(zip(self.A, self.b)):
            Ainv = np.linalg.inv(A)
            mu = Ainv @ b
            cov = self.v ** 2 * Ainv
            th = self.rng.multivariate_normal(mu, (cov + cov.T) / 2, size=n)
            out[:, k] = th @ x
        return out

    def choose(self, x: np.ndarray, n_prop: int = 200) -> tuple[int, np.ndarray]:
        if not isinstance(n_prop, (int, np.integer)) or n_prop <= 0:
            raise ValueError("n_prop must be positive")
        x = _context(x, self.d)
        s = self._sample_scores(x, n_prop)
        prop = np.bincount(np.argmax(s, axis=1), minlength=len(self.arms)) / n_prop
        prop = np.clip(prop, 1e-3, None)
        prop = prop / prop.sum()
        chosen = int(self.rng.choice(len(self.arms), p=prop))
        return chosen, prop

    def update(self, k: int, x: np.ndarray, r: float) -> None:
        x = _context(x, self.d)
        if not isinstance(k, (int, np.integer)) or not 0 <= k < len(self.arms) or not np.isfinite(r):
            raise ValueError("invalid chosen arm or reward")
        for i in range(len(self.arms)):
            self.A[i] = self.gamma * self.A[i] + (1 - self.gamma) * self.lam * np.eye(self.d)
            self.b[i] = self.gamma * self.b[i]
        self.A[k] += np.outer(x, x)
        self.b[k] += r * x


class FullInfoRidge:
    """Full-information counterpart: every arm's reward is observable here, so fit each arm's reward by ridge."""

    def __init__(self, d: int, arms: tuple[float, ...] = (0.0, 0.25, 0.5), lam: float = 1.0, gamma: float = 0.999):
        _validate_config(d, arms, lam, gamma)
        self.arms = arms
        self.A = [lam * np.eye(d) for _ in arms]
        self.b = [np.zeros(d) for _ in arms]
        self.gamma, self.lam, self.d = gamma, lam, d

    def choose(self, x: np.ndarray) -> int:
        x = _context(x, self.d)
        return int(np.argmax([np.linalg.solve(A, b) @ x for A, b in zip(self.A, self.b)]))

    def update_all(self, x: np.ndarray, rewards: np.ndarray) -> None:
        x = _context(x, self.d)
        rewards = np.asarray(rewards, float)
        if rewards.shape != (len(self.arms),) or not np.isfinite(rewards).all():
            raise ValueError("one finite reward per action arm required")
        for i in range(len(self.arms)):
            self.A[i] = self.gamma * self.A[i] + (1 - self.gamma) * self.lam * np.eye(self.d) + np.outer(x, x)
            self.b[i] = self.gamma * self.b[i] + rewards[i] * x
