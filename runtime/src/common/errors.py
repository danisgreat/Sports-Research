"""Failure types shared by every fitted component.

A fit that does not converge must never look like a valid flat model (ML-02): optimiser
failures raise `FitFailed`, and a component that was never successfully fitted raises
`NotFitted` when asked to predict.
"""

from typing import Any, Optional


class FitFailed(RuntimeError):
    """An optimiser did not converge, so the component must not be used to predict."""

    def __init__(self, model: str, reason: str):
        super().__init__(f"{model}: fit failed: {reason}")
        self.model = model
        self.reason = reason


class NotFitted(RuntimeError):
    """A component was asked to predict before a successful fit."""


class MissingInputs(ValueError):
    """A prediction needs an input (league profile, team strength, expected value) that was not supplied."""


class UnknownTeam(MissingInputs):
    """A team has no fitted strength and the engine's policy is to refuse rather than guess."""


class InsufficientData(ValueError):
    """Too few usable records to fit; no league-typical default is substituted."""


class MissingScore(ValueError):
    """A training record has no usable score; no default is ever substituted (DST-01)."""


def require_converged(result: Any, model: str, grad_tol: Optional[float] = None) -> None:
    """Raise `FitFailed` unless an scipy `OptimizeResult` converged.

    `grad_tol` accepts a result flagged unsuccessful only because of line-search precision
    loss when the gradient norm is already below the tolerance; anything else fails.
    """
    if result.success:
        return
    jac = getattr(result, "jac", None)
    if grad_tol is not None and jac is not None:
        import numpy as np
        if bool(np.all(np.isfinite(jac))) and float(np.linalg.norm(jac, ord=np.inf)) <= grad_tol:
            return
    raise FitFailed(model, str(getattr(result, "message", "optimiser reported failure")))


def finite_score(record: dict, *keys: str) -> float:
    """First present, finite, non-negative score among `keys`; 0 is a valid score.

    Replaces `a or b` coercion, which turned shutouts into league-typical defaults.
    """
    for key in keys:
        if key in record and record[key] is not None:
            value = float(record[key])
            if value != value or value in (float("inf"), float("-inf")) or value < 0:
                raise MissingScore(f"score field {key!r} is not a finite non-negative number: {record[key]!r}")
            return value
    raise MissingScore(f"none of {keys} present in record {sorted(record)[:8]}")
