"""Platform-independent bytes for text artefacts whose custody hashes were recorded from Windows checkouts (GOV-02).

Parts 1-5 of the Combined Prediction Log and the rank CSV are not marked `-text` in .gitattributes, so Git writes them with the
platform's line endings: CRLF on the Windows machines where every custody hash was recorded, LF on Linux. Their recorded hashes and
byte offsets are over CRLF bytes. `custody_bytes` returns the CRLF form on every platform (CRLF input is unchanged), so a verifier
sees identical bytes on Windows and Linux checkouts of the same commit. Files already pinned as exact bytes with `-text`
(Parts 6 and 7, everything under research/) are returned as stored.
"""
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CRLF_CUSTODY = frozenset({'prediction logs/PREDICTION_LOG_COMBINED.md', 'prediction logs/PREDICTION_LOG_COMBINED_2.md',
                          'prediction logs/PREDICTION_LOG_COMBINED_3.md', 'prediction logs/PREDICTION_LOG_COMBINED_4.md',
                          'prediction logs/PREDICTION_LOG_COMBINED_5.md', 'GAME_PREDICTION_RANK_LOG.csv'})


def to_crlf(raw: bytes) -> bytes:
    """Normalise every line ending to CRLF (a lone CR is left alone)."""
    return raw.replace(b'\r\n', b'\n').replace(b'\n', b'\r\n')


def relative(path: Path, root: Path = ROOT) -> str:
    try:
        return Path(path).resolve().relative_to(Path(root).resolve()).as_posix()
    except ValueError:
        return Path(path).as_posix()


def custody_bytes(path: Path, root: Path = ROOT) -> bytes:
    """The bytes a custody hash is computed over: CRLF form for the files in CRLF_CUSTODY, stored bytes for everything else."""
    raw = Path(path).read_bytes()
    return to_crlf(raw) if relative(path, root) in CRLF_CUSTODY else raw


def windows_path(value: str) -> Path:
    """A receipt path recorded on Windows ('research\\\\data\\\\x') resolved on any platform."""
    return Path(str(value).replace('\\', '/'))
