"""python -m ml sim <baseball|tennis|hockey|cricket|props> ...  (each simulator documents its own arguments)."""
import importlib
import sys

MODULES = {"baseball": "ml.sim.baseball", "tennis": "ml.sim.tennis", "hockey": "ml.sim.hockey", "cricket": "ml.sim.cricket",
           "props": "ml.sim.props"}


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] not in MODULES:
        print(__doc__)
        raise SystemExit(2)
    importlib.import_module(MODULES[argv[0]]).main(argv[1:])


if __name__ == "__main__":
    main()
