"""Retired legacy helper; delegates to the verified canonical archive CLI.

This filename is retained for compatibility and does not claim full historical
roster, coaching, officiating or game collection. See PIPELINE_STATUS.md.
"""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/"research"))
from src.archive import main

if __name__ == "__main__":
    raise SystemExit(main(["build", *sys.argv[1:]]))
