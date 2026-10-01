"""Safe compatibility entry point; legacy narrative enrichment is retired.

Original bytes are preserved in Previous Sports Results/_custody/originals.
This builds canonical results from exact evidence. It does not populate raw
seasons with award winners, guessed players, or manufactured descriptions.
"""
import sys
try:
    from .archive import main as archive_main, team_key
except ImportError:
    from archive import main as archive_main, team_key


def normalize_team(name):
    key = team_key(name)
    return {"north melbourne": "North Melbourne", "port adelaide": "Port Adelaide", "melbourne": "Melbourne"}.get(key, (name or "").strip())


def main():
    return archive_main(["build", *sys.argv[1:]])


if __name__ == "__main__":
    raise SystemExit(main())
