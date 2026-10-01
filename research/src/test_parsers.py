"""Run archive/parser regressions through unittest."""
import unittest
import sys
from pathlib import Path

if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    suite=unittest.defaultTestLoader.discover(str(Path(__file__).resolve().parents[1]/"tests"),pattern="test_archive.py")
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    raise SystemExit(0 if result.wasSuccessful() else 1)
