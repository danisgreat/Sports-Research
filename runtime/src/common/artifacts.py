"""Safe model artifacts: JSON with a model card, never pickle (ML-08).

Loading a pickle executes arbitrary code and breaks across library versions. An artifact here is
a JSON document holding the engine's parameters (numbers, strings, lists, numpy arrays tagged with
dtype and shape, and instances of an explicit allow-list of classes) plus a model card recording
the data hash, code hash, metrics and date range. Loading builds only allow-listed classes and
verifies the stored content hash, so a modified file is refused.
"""

from dataclasses import is_dataclass
import hashlib
import importlib
import json
import platform
from pathlib import Path
from typing import Any, Dict, Optional

import numpy as np

SCHEMA = "runtime-artifact-1"
ALLOWED_MODULE_PREFIX = "runtime.src."


class ArtifactError(ValueError):
    """The artifact is malformed, modified, or refers to a class that is not allowed."""


def _qualified(cls: type) -> str:
    return f"{cls.__module__}:{cls.__qualname__}"


def encode(obj: Any) -> Any:
    """Convert an object tree to JSON-compatible data."""
    if obj is None or isinstance(obj, (bool, int, float, str)):
        if isinstance(obj, float) and not np.isfinite(obj):
            return {"__float__": repr(obj)}
        return obj
    if isinstance(obj, np.generic):
        return encode(obj.item())
    if isinstance(obj, np.ndarray):
        return {"__ndarray__": obj.tolist(), "dtype": str(obj.dtype), "shape": list(obj.shape)}
    if isinstance(obj, (list, tuple)):
        return {"__tuple__": [encode(v) for v in obj]} if isinstance(obj, tuple) else [encode(v) for v in obj]
    if isinstance(obj, dict):
        if not all(isinstance(k, str) for k in obj):
            return {"__dict__": [[encode(k), encode(v)] for k, v in obj.items()]}
        return {k: encode(v) for k, v in obj.items()}
    cls = type(obj)
    if cls.__module__.startswith(ALLOWED_MODULE_PREFIX):
        state = dict(vars(obj)) if not (is_dataclass(obj) and hasattr(obj, "__slots__")) else {}
        return {"__class__": _qualified(cls), "state": {k: encode(v) for k, v in state.items()}}
    raise ArtifactError(f"cannot store object of type {cls.__module__}.{cls.__qualname__}")


def decode(data: Any) -> Any:
    if isinstance(data, list):
        return [decode(v) for v in data]
    if not isinstance(data, dict):
        return data
    if "__float__" in data:
        return float(data["__float__"])
    if "__ndarray__" in data:
        return np.array(data["__ndarray__"], dtype=np.dtype(data["dtype"])).reshape(data["shape"])
    if "__tuple__" in data:
        return tuple(decode(v) for v in data["__tuple__"])
    if "__dict__" in data:
        return {decode(k): decode(v) for k, v in data["__dict__"]}
    if "__class__" in data:
        module_name, _, qualname = data["__class__"].partition(":")
        if not module_name.startswith(ALLOWED_MODULE_PREFIX):
            raise ArtifactError(f"class {data['__class__']!r} is not allowed")
        cls = importlib.import_module(module_name)
        for part in qualname.split("."):
            cls = getattr(cls, part)
        instance = cls.__new__(cls)
        for key, value in data["state"].items():
            object.__setattr__(instance, key, decode(value))
        return instance
    return {k: decode(v) for k, v in data.items()}


def _digest(payload: Dict[str, Any]) -> str:
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def save(obj: Any, path: str, model_card: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Write `obj` to `path` as a hashed JSON artifact and return the written document."""
    import numpy
    import scipy
    body = encode(obj)
    card = {"data_sha256": None, "code_sha256": None, "metrics": {}, "date_range": None, "notes": ""}
    card.update(model_card or {})
    card["environment"] = {"python": platform.python_version(), "numpy": numpy.__version__, "scipy": scipy.__version__}
    document = {"schema": SCHEMA, "model_card": card, "body": body}
    document["content_sha256"] = _digest({"schema": SCHEMA, "model_card": card, "body": body})
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(document, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    return document


def load(path: str) -> Any:
    """Read an artifact, verify its content hash, and rebuild the object."""
    return load_with_card(path)[0]


def load_with_card(path: str):
    try:
        document = json.loads(Path(path).read_bytes().decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise ArtifactError(f"{path} is not a JSON artifact (pickle artifacts are no longer accepted): {exc}") from exc
    if document.get("schema") != SCHEMA:
        raise ArtifactError(f"unsupported artifact schema {document.get('schema')!r}")
    expected = document.get("content_sha256")
    actual = _digest({"schema": document["schema"], "model_card": document["model_card"], "body": document["body"]})
    if expected != actual:
        raise ArtifactError("artifact content hash does not match: the file was modified")
    return decode(document["body"]), document["model_card"]
