"""One cross-platform exclusive lock for append-only records (Windows and POSIX).

The lock is an operating-system lock on a side file outside the repository, keyed by the protected file's absolute
path. It is held only while the owning process is alive and inside the block: a writer that dies releases it
automatically, and a live writer can never lose it however long it runs. A leftover side file is not a lock.
"""

from __future__ import annotations

import contextlib
import hashlib
import os
import tempfile
import time
from pathlib import Path


def lock_path(path) -> Path:
    """The side file that guards ``path`` (in the system temporary folder, so no lock file appears in the repository)."""
    key = hashlib.sha256(str(Path(path).resolve()).encode("utf-8")).hexdigest()[:24]
    return Path(tempfile.gettempdir()) / f"sports-research-{key}.lock"


def _try_lock(f) -> bool:
    try:
        if os.name == "nt":
            import msvcrt

            f.seek(0)
            msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, 1)
        else:
            import fcntl

            fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        return True
    except OSError:
        return False


def _unlock(f) -> None:
    if os.name == "nt":
        import msvcrt

        f.seek(0)
        msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)
    else:
        import fcntl

        fcntl.flock(f.fileno(), fcntl.LOCK_UN)


@contextlib.contextmanager
def exclusive(path, *, wait: float = 0.0, what: str = "this record"):
    """Hold the lock for ``path``; wait up to ``wait`` seconds for another writer, then refuse with a clear error."""
    lock = lock_path(path)
    f = open(lock, "a+b")
    try:
        deadline = time.monotonic() + wait
        while not _try_lock(f):
            if time.monotonic() >= deadline:
                raise RuntimeError(
                    f"{what} is locked by another writer ({Path(path).name}); retry when it has finished"
                )
            time.sleep(0.2)
        try:
            f.seek(0)
            f.truncate()
            f.write(str(os.getpid()).encode())
            f.flush()
            yield
        finally:
            _unlock(f)
    finally:
        f.close()
