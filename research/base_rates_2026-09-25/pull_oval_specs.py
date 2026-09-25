"""ESPN scoreboard specs for the NFL, AFL and NRL seasons pulled on 2026-09-25(e).

Shared by research/team_baseline_2026-09-25e/pull_oval.py, oval_base_rates.py and
validate_team_baseline.py. Format: label -> (ESPN path, first date, last date, kind).
"""
OVAL = {
    'NFL 2024': ('football/nfl', '20240905', '20250210', 'fb'),
    'NFL 2025': ('football/nfl', '20250904', '20260209', 'fb'),
    'AFL 2025': ('australian-football/afl', '20250306', '20250927', 'afl'),
    'AFL 2026': ('australian-football/afl', '20260305', '20260924', 'afl'),
    'NRL 2025': ('rugby-league/3', '20250301', '20251005', 'nrl'),
    'NRL 2026': ('rugby-league/3', '20260226', '20260924', 'nrl'),
}
