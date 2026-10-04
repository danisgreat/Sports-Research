import zipfile
import json
import os
import re
from datetime import datetime

def format_overs(overs_list):
    total_balls = 0
    for ov in overs_list:
        total_balls += len(ov.get('deliveries', []))
    complete_overs = total_balls // 6
    remainder_balls = total_balls % 6
    if remainder_balls == 0:
        return f"{complete_overs}.0 ov"
    else:
        return f"{complete_overs}.{remainder_balls} ov"

def parse_innings(inn):
    team = inn.get('team', '')
    overs = inn.get('overs', [])
    declared = inn.get('declared', False)
    runs = 0
    wickets = 0
    batter_runs = {}
    bowler_wkts = {}
    bowler_runs = {}

    for ov in overs:
        for d in ov.get('deliveries', []):
            r = d.get('runs', {})
            total_r = r.get('total', 0)
            bat_r = r.get('batter', 0)
            runs += total_r
            b = d.get('batter', '')
            batter_runs[b] = batter_runs.get(b, 0) + bat_r
            bw = d.get('bowler', '')
            bowler_runs[bw] = bowler_runs.get(bw, 0) + total_r

            if 'wickets' in d:
                for w in d['wickets']:
                    kind = w.get('kind', '')
                    if kind not in ['run out', 'retired hurt', 'retired not out']:
                        bowler_wkts[bw] = bowler_wkts.get(bw, 0) + 1
                    wickets += 1

    top_bats = sorted(batter_runs.items(), key=lambda x: -x[1])[:2]
    top_bowls = sorted(bowler_wkts.items(), key=lambda x: (-x[1], bowler_runs.get(x[0], 999)))[:2]

    dec_str = 'd' if declared else ''
    ov_str = format_overs(overs)
    score_str = f"{runs}/{wickets}{dec_str} ({ov_str})"

    return {
        'team': team,
        'runs': runs,
        'wickets': wickets,
        'overs': ov_str,
        'declared': declared,
        'score_str': score_str,
        'top_bats': top_bats,
        'top_bowls': top_bowls
    }

def parse_cricsheet_match(data, match_id):
    info = data.get('info', {})
    season = str(info.get('season', ''))
    dates = info.get('dates', [])
    start_date = dates[0] if dates else ''
    end_date = dates[-1] if dates else start_date
    duration_days = len(dates) if dates else 4

    teams = info.get('teams', [])
    team_a = teams[0] if len(teams) > 0 else 'Unknown'
    team_b = teams[1] if len(teams) > 1 else 'Unknown'

    # Determine venue & city
    venue = info.get('venue', '')
    city = info.get('city', '')

    # Determine home / away
    # In county cricket, home is often team whose home ground is the venue
    home_team = team_a
    away_team = team_b
    venue_lower = venue.lower()
    if 'oval' in venue_lower or 'guildford' in venue_lower:
        home_team, away_team = ('Surrey', team_b if team_a == 'Surrey' else team_a)
    elif 'lord' in venue_lower or 'uxbridge' in venue_lower:
        home_team, away_team = ('Middlesex', team_b if team_a == 'Middlesex' else team_a)
    elif 'headingley' in venue_lower or 'scarborough' in venue_lower:
        home_team, away_team = ('Yorkshire', team_b if team_a == 'Yorkshire' else team_a)
    elif 'edgbaston' in venue_lower:
        home_team, away_team = ('Warwickshire', team_b if team_a == 'Warwickshire' else team_a)
    elif 'old trafford' in venue_lower or 'blackpool' in venue_lower or 'southport' in venue_lower:
        home_team, away_team = ('Lancashire', team_b if team_a == 'Lancashire' else team_a)
    elif 'trent bridge' in venue_lower:
        home_team, away_team = ('Nottinghamshire', team_b if team_a == 'Nottinghamshire' else team_a)
    elif 'taunton' in venue_lower or 'bath' in venue_lower:
        home_team, away_team = ('Somerset', team_b if team_a == 'Somerset' else team_a)
    elif 'chelmsford' in venue_lower or 'colchester' in venue_lower:
        home_team, away_team = ('Essex', team_b if team_a == 'Essex' else team_a)
    elif 'canterbury' in venue_lower or 'tunbridge' in venue_lower or 'beckham' in venue_lower:
        home_team, away_team = ('Kent', team_b if team_a == 'Kent' else team_a)
    elif 'hove' in venue_lower or 'arundel' in venue_lower:
        home_team, away_team = ('Sussex', team_b if team_a == 'Sussex' else team_a)
    elif 'cardiff' in venue_lower or 'swansea' in venue_lower or 'sophia' in venue_lower:
        home_team, away_team = ('Glamorgan', team_b if team_a == 'Glamorgan' else team_a)
    elif 'bristol' in venue_lower or 'cheltenham' in venue_lower:
        home_team, away_team = ('Gloucestershire', team_b if team_a == 'Gloucestershire' else team_a)
    elif 'rose bowl' in venue_lower or 'ageas' in venue_lower or 'southampton' in venue_lower:
        home_team, away_team = ('Hampshire', team_b if team_a == 'Hampshire' else team_a)
    elif 'worcester' in venue_lower or 'new road' in venue_lower:
        home_team, away_team = ('Worcestershire', team_b if team_a == 'Worcestershire' else team_a)
    elif 'northampton' in venue_lower:
        home_team, away_team = ('Northamptonshire', team_b if team_a == 'Northamptonshire' else team_a)
    elif 'grace road' in venue_lower or 'leicester' in venue_lower:
        home_team, away_team = ('Leicestershire', team_b if team_a == 'Leicestershire' else team_a)
    elif 'derby' in venue_lower or 'chesterfield' in venue_lower:
        home_team, away_team = ('Derbyshire', team_b if team_a == 'Derbyshire' else team_a)
    elif 'chester-le-street' in venue_lower or 'durham' in venue_lower or 'riverside' in venue_lower:
        home_team, away_team = ('Durham', team_b if team_a == 'Durham' else team_a)

    # Event / Division
    event = info.get('event', {})
    event_name = event.get('name', 'County Championship')
    group = event.get('group', '')
    stage = event.get('stage', '')
    match_number = event.get('match_number', '')

    comp_name = 'County Championship'
    if 'Bob Willis' in event_name:
        comp_name = 'Bob Willis Trophy'

    # Match Type & Division
    match_type = 'County Championship'
    div_group = 'Division One'
    if comp_name == 'Bob Willis Trophy':
        match_type = 'Bob Willis Trophy'
        if 'Final' in str(stage) or 'Final' in str(match_number):
            match_type = 'Final'
            div_group = 'Final'
        else:
            div_group = str(group) if group else 'Group Stage'
    else:
        if str(group) == '2' or 'Division Two' in event_name or 'Division 2' in event_name:
            match_type = 'Division Two'
            div_group = 'Division Two'
        elif str(group) == '1' or 'Division One' in event_name or 'Division 1' in event_name:
            match_type = 'Division One'
            div_group = 'Division One'
        elif 'Division 3' in event_name:
            match_type = 'Division Three'
            div_group = 'Division Three'
        elif group:
            match_type = f"Group {group}"
            div_group = f"Group {group}"
        else:
            match_type = 'Division One'
            div_group = 'Division One'

    # Toss
    toss = info.get('toss', {})
    toss_winner = toss.get('winner', '')
    toss_decision = toss.get('decision', '')
    if toss.get('uncontested'):
        toss_decision = f"uncontested - {toss_decision}"

    # Innings
    raw_innings = data.get('innings', [])
    parsed_inns = [parse_innings(inn) for inn in raw_innings]

    # Follow-on detection
    follow_on = 'No'
    if len(parsed_inns) >= 3:
        if parsed_inns[1]['team'] == parsed_inns[2]['team']:
            follow_on = 'Yes'

    # Populate innings 1 to 4
    inn_fields = {}
    for idx in range(1, 5):
        if idx <= len(parsed_inns):
            p = parsed_inns[idx-1]
            inn_fields[f'Innings {idx} Team'] = p['team']
            inn_fields[f'Innings {idx} Score'] = p['score_str']
            inn_fields[f'Innings {idx} Runs'] = p['runs']
            inn_fields[f'Innings {idx} Wickets'] = p['wickets']
            inn_fields[f'Innings {idx} Overs'] = p['overs']
        else:
            inn_fields[f'Innings {idx} Team'] = ''
            inn_fields[f'Innings {idx} Score'] = ''
            inn_fields[f'Innings {idx} Runs'] = ''
            inn_fields[f'Innings {idx} Wickets'] = ''
            inn_fields[f'Innings {idx} Overs'] = ''

    total_runs = sum(p['runs'] for p in parsed_inns)
    total_wickets = sum(p['wickets'] for p in parsed_inns)

    # Match Score string
    # E.g. Essex 250 & 180/4d v Somerset 210 & 218
    # Or just summary
    team_inns = {}
    for p in parsed_inns:
        t = p['team']
        if t not in team_inns:
            team_inns[t] = []
        team_inns[t].append(p['score_str'].split(' ')[0]) # without overs for compact score

    match_score_parts = []
    for t, scores in team_inns.items():
        match_score_parts.append(f"{t} {' & '.join(scores)}")
    match_score = ' - '.join(match_score_parts)

    # Outcome
    outcome = info.get('outcome', {})
    winner = outcome.get('winner', '')
    result = outcome.get('result', '')
    loser = ''
    margin_str = ''
    margin_val = ''
    margin_type = ''

    if winner:
        result = 'Win'
        loser = team_b if winner == team_a else team_a
        by = outcome.get('by', {})
        if 'innings' in by and 'runs' in by:
            margin_str = f"innings and {by['runs']} runs"
            margin_val = by['runs']
            margin_type = 'innings and runs'
        elif 'runs' in by:
            margin_str = f"{by['runs']} runs"
            margin_val = by['runs']
            margin_type = 'runs'
        elif 'wickets' in by:
            margin_str = f"{by['wickets']} wickets"
            margin_val = by['wickets']
            margin_type = 'wickets'
    elif result == 'draw':
        result = 'Draw'
        winner = 'Draw'
        loser = 'None'
        margin_str = 'Draw'
        margin_type = 'draw'
    elif result == 'tie':
        result = 'Tie'
        winner = 'Tie'
        loser = 'None'
        margin_str = 'Tie'
        margin_type = 'tie'
    else:
        result = 'Draw'
        winner = 'Draw'
        loser = 'None'
        margin_str = 'Draw'
        margin_type = 'draw'

    pom = info.get('player_of_match', [])
    player_of_match = pom[0] if pom else ''

    # Notable players
    notable_parts = []
    for p in parsed_inns:
        t = p['team']
        parts = []
        for b, r in p['top_bats']:
            parts.append(f"{b} {r}")
        for bw, w in p['top_bowls']:
            if w > 0:
                parts.append(f"{bw} {w} wkts")
        if parts:
            notable_parts.append(f"{t}: {', '.join(parts)}")
    notable_players = ' | '.join(notable_parts)

    # Officials
    officials = info.get('officials', {})
    umpires = '; '.join(officials.get('umpires', []))

    # Match comment
    if result == 'Win':
        comment = f"{winner} defeated {loser} by {margin_str} at {venue} ({city})."
    elif result == 'Tie':
        comment = f"Match tied between {team_a} and {team_b} at {venue} ({city})."
    else:
        comment = f"Match drawn between {team_a} and {team_b} at {venue} ({city})."

    return {
        'Match ID': f"CCH_{match_id}",
        'Season': season,
        'Season Year': int(season) if season.isdigit() else 2020,
        'Competition': comp_name,
        'Match Type': match_type,
        'Division / Group': div_group,
        'Stage / Round': str(match_number) if match_number else 'Group Stage',
        'Date': start_date,
        'Start Date': start_date,
        'End Date': end_date,
        'Duration (Days)': duration_days,
        'Team A': team_a,
        'Team B': team_b,
        'Home': home_team,
        'Away': away_team,
        'Toss Winner': toss_winner,
        'Toss Decision': toss_decision,
        **inn_fields,
        'Total Runs': total_runs,
        'Total Wickets': total_wickets,
        'Match Score': match_score,
        'Result': result,
        'Winner': winner,
        'Loser': loser,
        'Winning Margin': margin_str,
        'Margin Value': margin_val,
        'Margin Type': margin_type,
        'Follow-On Enforced': follow_on,
        'Player of the Match': player_of_match,
        'Notable Players': notable_players,
        'Venue': venue,
        'City': city,
        'Umpires': umpires,
        'A Succint one line match comment to summarise that match': comment,
        'Primary Data Source': 'Cricsheet JSON v1.2.0 Open Data / ECB Official Scorecards'
    }

print("Cricsheet parser module loaded successfully.")
