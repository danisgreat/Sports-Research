"""SRC-05: the standard-schema adapter maps rows faithfully and rejects inconsistent ones."""
import csv

from research.src import archive_std

NHL_HEADER = ["Game Number", "Season Year", "Game Type (Pre-Season, Regular Season)", "Date", "Home", "Away", "Home Score", "Away Score",
              "Total Goals", "Winning Margin", "Decision Type", "Overtime", "Shootout"]
AFL_HEADER = ["Game Number", "Game Type (pre-Season, Regular Season)", "Home", "Away", "Date", "Game Score", "Total Points", "Winning Margin"]


def write(root, sport, competition, year, header, rows):
    folder = root / sport / competition / str(year)
    folder.mkdir(parents=True)
    with (folder / f"{year}_games.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(rows)


def test_numeric_columns_flags_and_zero_scores(tmp_path):
    write(tmp_path, "Ice Hockey", "NHL", 2025, NHL_HEADER, [
        [1, 2025, "Regular Season", "2025-10-08", "Dallas Stars", "St. Louis Blues", 0, 0, 0, 0, "Regulation", "No", "No"],
        [2, 2025, "Regular Season", "2025-10-09", "Dallas Stars", "St. Louis Blues", 2, 1, 3, 1, "Shootout", "Yes", "Yes"],
        [3, 2025, "Regular Season", "2025-10-10", "Dallas Stars", "St. Louis Blues", 3, 1, 5, 2, "Regulation", "No", "No"],   # total disagrees
        [4, 2025, "Regular Season", "not-a-date", "Dallas Stars", "St. Louis Blues", 3, 1, 4, 2, "Regulation", "No", "No"],
    ])
    coverage = {}
    events = list(archive_std.iter_events(tmp_path, coverage=coverage))
    assert [(e.home_score, e.away_score) for e in events] == [(0, 0), (2, 1)]      # a 0-0 score is kept, never defaulted
    assert events[1].overtime is True and events[1].shootout is True and events[0].overtime is False
    stats = coverage[("Ice Hockey", "NHL", 2025)]
    assert (stats.rows, stats.accepted) == (4, 2)
    assert stats.reasons == {"declared_total_disagrees": 1, "invalid_event_date": 1}


def test_score_text_assigns_scores_by_team_identity(tmp_path):
    write(tmp_path, "AFL", "AFL", 2025, AFL_HEADER, [
        [1, "Regular Season", "Geelong", "Essendon", "2025-03-01", "Essendon 12.11 (83) def. Geelong Cats 10.8 (68)", 151, 15],
        [2, "Regular Season", "Geelong", "Essendon", "2025-03-08", "Geelong Cats 12.11 (83) def. Essendon 10.8 (68)", 151, 15],
        [3, "Regular Season", "Geelong", "Essendon", "2025-03-15", "Geelong Cats 12.11 (83) def. Collingwood 10.8 (68)", 151, 15],
    ])
    events = list(archive_std.iter_events(tmp_path))
    assert [(e.home, e.home_score, e.away_score) for e in events] == [("Geelong", 68, 83), ("Geelong", 83, 68)]
    assert all(e.score_source == "score_text" for e in events)
    # goals and behinds come from the G.B notation and must agree with the bracketed points
    assert (events[0].home_goals, events[0].home_behinds, events[0].away_goals, events[0].away_behinds) == (10, 8, 12, 11)
    assert archive_std.afl_goals_behinds("Geelong 12.11 (84) def. Essendon 10.8 (68)") is None


def test_coverage_report_and_build(tmp_path):
    write(tmp_path / "raw", "Ice Hockey", "NHL", 2025, NHL_HEADER, [
        [1, 2025, "Regular Season", "2025-10-08", "Dallas Stars", "St. Louis Blues", 4, 3, 7, 1, "Overtime", "Yes", "No"]])
    report = archive_std.coverage_report(tmp_path / "raw")
    assert report["totals"] == {"rows": 1, "accepted": 1}
    assert "Ice Hockey" in archive_std.render_coverage(report)
    counts = archive_std.build(tmp_path / "out", tmp_path / "raw")
    assert counts == {"ice_hockey": 1}
    row = next(csv.DictReader((tmp_path / "out" / "ice_hockey.csv").open(encoding="utf-8")))
    assert list(row) == archive_std.STD_FIELDS and row["overtime"] == "True"
