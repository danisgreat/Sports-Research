"""Contextual bandit (linear Thompson sampling with exponential forgetting) for stake sizing.

Arms are stake multipliers. Reward is stake x closing-line value, observed at the close (before the result).
Propensities are estimated by Monte Carlo over the posterior so the logs support off-policy evaluation.
"""
from __future__ import annotations

import numpy as np


class LinTS:
    def __init__(self, d: int, arms: tuple[float, ...] = (0.0, 0.25, 0.5), lam: float = 1.0, v: float = 0.05,
                 gamma: float = 0.999, seed: int = 20261014):
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
        s = self._sample_scores(x, n_prop + 1)
        chosen = int(np.argmax(s[0]))
        prop = np.bincount(np.argmax(s[1:], axis=1), minlength=len(self.arms)) / n_prop
        prop = np.clip(prop, 1e-3, None)
        return chosen, prop / prop.sum()

    def update(self, k: int, x: np.ndarray, r: float) -> None:
        for i in range(len(self.arms)):
            self.A[i] = self.gamma * self.A[i] + (1 - self.gamma) * self.lam * np.eye(self.d)
            self.b[i] = self.gamma * self.b[i]
        self.A[k] += np.outer(x, x)
        self.b[k] += r * x


class FullInfoRidge:
    """Full-information counterpart: every arm's reward is observable here, so fit each arm's reward by ridge."""

    def __init__(self, d: int, arms: tuple[float, ...] = (0.0, 0.25, 0.5), lam: float = 1.0, gamma: float = 0.999):
        self.arms = arms
        self.A = [lam * np.eye(d) for _ in arms]
        self.b = [np.zeros(d) for _ in arms]
        self.gamma, self.lam, self.d = gamma, lam, d

    def choose(self, x: np.ndarray) -> int:
        return int(np.argmax([np.linalg.solve(A, b) @ x for A, b in zip(self.A, self.b)]))

    def update_all(self, x: np.ndarray, rewards: np.ndarray) -> None:
        for i in range(len(self.arms)):
            self.A[i] = self.gamma * self.A[i] + (1 - self.gamma) * self.lam * np.eye(self.d) + np.outer(x, x)
            self.b[i] = self.gamma * self.b[i] + rewards[i] * x
