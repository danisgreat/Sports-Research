import csv

for yr in [1975, 1985, 1998, 2005, 2023]:
    fpath = f"ODI_International_CSVs/ODI_International_{yr}.csv"
    with open(fpath, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        print(f"=== Year {yr} ({len(rows)} matches) ===")
        for r in rows[:2]:
            print(f"  Match {r['Match Number']} [{r['ODI Number']} | {r['Date']}]: {r['Team A']} v {r['Team B']} at {r['Venue']} ({r['City']})")
            print(f"    Scores: {r['First Innings Team']} {r['First Innings Score']} vs {r['Second Innings Team']} {r['Second Innings Score']}")
            print(f"    Result: {r['Winner']} won by {r['Winning Margin']} | Toss: {r['Toss Winner']} chose to {r['Toss Decision']}")
            print(f"    Comment: {r['A Succint one line match comment to summarise that match'][:90]}...")
