"""Immutable request contracts and confidence sequences for prospective cards.

Request text is owner evidence, not a reconstructed request or a sporting fact.
The confidence sequence targets the average conditional mean, allowing drift.
"""

from __future__ import annotations

import csv
import hashlib
import io
import math
import re
from pathlib import Path

from ml import timing

REQUEST_ROOT = "research/one_chat/requests"
EVENT_FIELDS = (
    "event_id",
    "sport",
    "competition",
    "home",
    "away",
    "scheduled_start",
    "schedule_source",
)
CONTRACT_FIELDS = (
    "label",
    "family",
    "side",
    "line",
    "period",
    "endpoint",
    "action",
    "unit",
    "request_excerpt",
    "baseline_p",
    "baseline_id",
)
REQUEST_FILES = ("REQUEST.txt", "EVENT.csv", "CONTRACTS.csv")
# Registered in EVALUATION_PLAN_v28.0 (v27.0 used eight values from 0.05 to 0.9).
LAMBDAS = (0.5, 0.7, 0.9)
STATISTICAL_RULE = "AVERAGE-CONDITIONAL-MEAN-EB-v2"


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def rows(raw):
    return list(csv.DictReader(io.StringIO(raw.decode("utf-8-sig"))))


def csv_bytes(fields, values):
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(values)
    return out.getvalue().encode("utf-8")


def request_path(key):
    if not re.fullmatch(r"[A-Za-z0-9_-]+", key):
        raise ValueError("a request needs a safe, stable card key")
    return f"{REQUEST_ROOT}/{key}"


def register_request(source, event, contracts, key, root):
    """Keep the exact owner request and explicit settlement definitions before sealing."""
    folder = Path(root) / request_path(key)
    payload = {
        "REQUEST.txt": Path(source).read_bytes(),
        "EVENT.csv": Path(event).read_bytes(),
        "CONTRACTS.csv": Path(contracts).read_bytes(),
    }
    problems = request_problems(payload)
    if problems:
        raise ValueError(" | ".join(problems))
    payload["MANIFEST.csv"] = csv_bytes(
        ("file", "sha256"),
        [dict(file=name, sha256=digest(payload[name])) for name in REQUEST_FILES],
    )
    if folder.exists():
        if all(
            (folder / name).exists() and (folder / name).read_bytes() == raw
            for name, raw in payload.items()
        ):
            return dict(status="ALREADY_REGISTERED", path=str(folder))
        raise ValueError(
            "a registered request is immutable; use a new key and retain the earlier request"
        )
    folder.mkdir(parents=True)
    for name, raw in payload.items():
        (folder / name).write_bytes(raw)
    return dict(
        status="REGISTERED",
        path=str(folder),
        contracts=len(rows(payload["CONTRACTS.csv"])),
    )


def request_problems(payload, meta=None, picks=None):
    problems = []
    try:
        text = payload["REQUEST.txt"].decode("utf-8-sig")
        events, contracts = rows(payload["EVENT.csv"]), rows(payload["CONTRACTS.csv"])
        if len(events) != 1 or set(events[0]) != set(EVENT_FIELDS):
            return [
                "request: exactly one EVENT.csv row with the registered columns is required"
            ]
        event = events[0]
        if not all(event.values()) or not (
            ":" in event["event_id"]
            and re.match(r"https?://\S+$", event["schedule_source"])
        ):
            problems.append(
                "request: namespaced native event_id and official schedule_source are required"
            )
        timing.clock(event["scheduled_start"], "request scheduled_start")
        if not contracts or any(set(r) != set(CONTRACT_FIELDS) for r in contracts):
            return problems + [
                "request: explicit contracts with period, endpoint, action, unit and original excerpt are required"
            ]
        seen = set()
        for r in contracts:
            k = (r["label"], r["side"].upper())
            if k in seen or any(
                not r[f].strip()
                for f in CONTRACT_FIELDS
                if f not in ("line", "baseline_p")
            ):
                problems.append("request: duplicate or incomplete contract definition")
            seen.add(k)
            if r["request_excerpt"] not in text:
                problems.append(
                    f"request {r['label']}: excerpt is absent from the unchanged original request"
                )
            if r["line"] and abs(float(r["line"])) not in {
                abs(float(x))
                for x in re.findall(r"[-+]?\d+(?:\.\d+)?", r["request_excerpt"])
            }:
                problems.append(
                    f"request {r['label']}: numeric line is absent from its original excerpt"
                )
            if r["baseline_p"] and not 0 < float(r["baseline_p"]) < 1:
                problems.append(
                    "request: frozen baseline probability must be between zero and one"
                )
        if meta:
            for f in ("sport", "competition", "home", "away"):
                if event[f] != meta[f]:
                    problems.append(f"request: {f} differs from the card")
            if timing.clock(event["scheduled_start"], "request start") != timing.clock(
                meta["scheduled_start"], "card start"
            ):
                problems.append("request: scheduled start differs from the card")
        if picks is not None:

            def identity(r):
                line = float(r["line"]) if r["line"] else None
                return r["label"], r["family"], r["side"].upper(), line

            if {identity(r) for r in contracts} != {identity(r) for r in picks} or len(
                contracts
            ) != len(picks):
                problems.append(
                    "request: card omits, adds or changes an original requested contract"
                )
    except (KeyError, ValueError, UnicodeError) as exc:
        problems.append("request: " + str(exc))
    return problems


def log_mean_exp(values):
    top = max(values)
    return top + math.log(sum(math.exp(v - top) for v in values) / len(values))


def confidence_path(ds, alpha=0.05):
    """Predictable empirical-Bernstein mixture, Howard et al. (2021), Theorem 4.

    X=d+0.75 lies in [0,1]. For any predictable forecast xhat in [0,1],
    exp(lambda*sum(X-E[X|past]) - psi(lambda)*sum((X-xhat)**2)) is a
    nonnegative supermartingale, psi=-log(1-lambda)-lambda. A fixed mixture
    yields a lower CS for the *current* average conditional mean. Past
    crossings are not used as a lower bound for a later, different mean.
    Reference: https://arxiv.org/abs/1810.08240, Theorem 4 and Appendix A.8.
    """
    if not 0 < alpha < 1:
        raise ValueError("alpha must be between zero and one")
    total, variance, result = 0.0, 0.0, []
    threshold = math.log(1 / alpha)
    for n, d in enumerate(ds, 1):
        if not math.isfinite(d) or not -0.75 <= d <= 0.25:
            raise ValueError("game advantage must be finite and within [-0.75, 0.25]")
        # One pseudo-observation at d=0; only earlier games determine this forecast.
        forecast = 0.75 + total / n
        variance += (d + 0.75 - min(max(forecast, 0), 1)) ** 2
        total += d

        def log_e(m):
            return log_mean_exp(
                [
                    lam * (total - n * m) - (-math.log1p(-lam) - lam) * variance
                    for lam in LAMBDAS
                ]
            )

        lo, hi = -0.75, min(0.25, total / n)
        if log_e(lo) < threshold:
            bound = -0.75
        else:
            for _ in range(45):
                mid = (lo + hi) / 2
                if log_e(mid) >= threshold:
                    lo = mid
                else:
                    hi = mid
            bound = lo
        le = log_e(0)
        result.append(
            dict(
                game=n,
                bet="MIXTURE",
                e_value=math.exp(min(le, 700)),
                mean_d=total / n,
                lower_bound_95=bound,
            )
        )
    return result


POWER_SCENARIOS = (
    ("MEAN_ZERO_NULL", None),
    ("COIN_RESULTS_CARD_STATES_55_75", (0.55, 0.75)),
    ("CALIBRATED_FAVOURED_55_65", (0.55, 0.65)),
    ("CALIBRATED_FAVOURED_58_72", (0.58, 0.72)),
    ("CALIBRATED_FAVOURED_62_78", (0.62, 0.78)),
)


def _simulated_game(rng, scenario, band):
    """One game's d: two supplied lines; the card states p on its favoured side."""
    if band is None:
        return rng.choice((0.15, -0.15))
    out = []
    for _ in range(2):
        p = rng.uniform(*band)
        truth = 0.5 if scenario.startswith("COIN") else p
        out.append(0.25 - (p - (1 if rng.random() < truth else 0)) ** 2)
    return sum(out) / 2


def first_crossing(ds, *, alpha=0.05, practical=0.01, horizon=None):
    """First game at which the evidence reaches 1/alpha with mean d at least the practical threshold."""
    total = 0.0
    for i, r in enumerate(confidence_path(ds, alpha)):
        total += ds[i]
        if horizon is not None and i >= horizon:
            return None
        if r["e_value"] >= 1 / alpha and total / (i + 1) >= practical:
            return i + 1
    return None


def power_study(
    *, horizon, runs=200, null_runs=400, seed=20261117, alpha=0.05, practical=0.01
):
    """Deterministic simulation of the registered decision (Python's random module, fixed seed)."""
    import random

    rows = []
    for n, (scenario, band) in enumerate(POWER_SCENARIOS):
        rng = random.Random(seed + n)
        count = null_runs if band is None else runs
        hits = []
        for _ in range(count):
            ds = [_simulated_game(rng, scenario, band) for _ in range(horizon)]
            hit = first_crossing(ds, alpha=alpha, practical=practical, horizon=horizon)
            if hit:
                hits.append(hit)
        hits.sort()
        rows.append(
            dict(
                scenario=scenario,
                runs=count,
                horizon=horizon,
                lambdas=" ".join(str(x) for x in LAMBDAS),
                demonstrated_within_400=sum(h <= 400 for h in hits),
                demonstrated_within_horizon=len(hits),
                share_within_horizon=round(len(hits) / count, 4),
                median_crossing_game=hits[len(hits) // 2] if hits else "",
                seed=seed + n,
            )
        )
    return rows
