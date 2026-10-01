"""Fetch the supported official CFB boxscore; broad postseason collection is pending.

No season is filled from descriptions or generic player lists.
"""
try:
    from .archive_sources import fetch_official
except ImportError:
    from archive_sources import fetch_official

if __name__ == "__main__":
    print(fetch_official("cfb_2025_dublin"))
