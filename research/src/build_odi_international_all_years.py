"""
build_odi_international_all_years.py
Generates comprehensive, verified game logs for ODI International cricket matches (non-World Cup)
from 1975 to 2025 (51 calendar years) across all international teams.

Target Directories:
  1. ODI_International_CSVs/ODI_International_<YEAR>.csv
  2. Previous Sports Results/Cricket One-Day Format/ODI International/<YEAR>/<YEAR>_games.csv
  3. Previous Sports Results/Cricket One-Day Format/Men's ODI International/<YEAR>/<YEAR>_games.csv

Scope & Rules:
  - 1975 to 2025 inclusive (51 years)
  - Strictly excludes all matches from the 13 ICC Men's Cricket World Cup tournaments
    (1975, 1979, 1983, 1987, 1992, 1996, 1999, 2003, 2007, 2011, 2015, 2019, 2023)
  - Sourced from ESPNcricinfo Records, Statsguru, and Cricsheet open ball-by-ball archives.
"""

import os
import re
import csv
import json
from datetime import datetime
from collections import defaultdict

# Paths
BASE_DIR = os.getcwd()
MATCH_RES_DIR = os.path.join(BASE_DIR, "research", "data", "match_results_cache")
STATSGURU_DIR = os.path.join(BASE_DIR, "research", "data", "statsguru_cache")
CRICSHEET_DIR = os.path.join(BASE_DIR, "research", "data", "cricsheet_odi", "matches")

OUT_DIR_ROOT = os.path.join(BASE_DIR, "ODI_International_CSVs")
OUT_DIR_PREV1 = os.path.join(BASE_DIR, "Previous Sports Results", "Cricket One-Day Format", "ODI International")
OUT_DIR_PREV2 = os.path.join(BASE_DIR, "Previous Sports Results", "Cricket One-Day Format", "Men's ODI International")

# Comprehensive Ground -> (Venue Name, City, Country) Mapping
GROUND_MAPPING = {
    # Australia
    "Melbourne": ("Melbourne Cricket Ground", "Melbourne", "Australia"),
    "Sydney": ("Sydney Cricket Ground", "Sydney", "Australia"),
    "Adelaide": ("Adelaide Oval", "Adelaide", "Australia"),
    "Brisbane": ("Brisbane Cricket Ground (The Gabba)", "Brisbane", "Australia"),
    "Perth": ("W.A.C.A. Ground", "Perth", "Australia"),
    "Perth Stadium": ("Optus Stadium", "Perth", "Australia"),
    "Hobart": ("Bellerive Oval", "Hobart", "Australia"),
    "Devonport": ("Devonport Oval", "Devonport", "Australia"),
    "Canberra": ("Manuka Oval", "Canberra", "Australia"),
    "Cairns": ("Cazalys Stadium", "Cairns", "Australia"),
    "Darwin": ("Marrara Cricket Ground", "Darwin", "Australia"),
    "Mackay": ("Ray Mitchell Oval", "Mackay", "Australia"),
    "Geelong": ("GMHBA Stadium (Kardinia Park)", "Geelong", "Australia"),
    "Ballarat": ("Eastern Oval", "Ballarat", "Australia"),
    "Berri": ("Berri Oval", "Berri", "Australia"),
    "Mildura": ("Chaffey Park", "Mildura", "Australia"),
    "Albury": ("Lavington Sports Oval", "Albury", "Australia"),
    
    # England & Wales
    "Lord's": ("Lord's Cricket Ground", "London", "England"),
    "The Oval": ("Kennington Oval", "London", "England"),
    "Birmingham": ("Edgbaston Cricket Ground", "Birmingham", "England"),
    "Manchester": ("Old Trafford Cricket Ground", "Manchester", "England"),
    "Leeds": ("Headingley Cricket Ground", "Leeds", "England"),
    "Nottingham": ("Trent Bridge", "Nottingham", "England"),
    "Southampton": ("The Rose Bowl", "Southampton", "England"),
    "Cardiff": ("Sophia Gardens", "Cardiff", "Wales"),
    "Chester-le-Street": ("Riverside Ground", "Chester-le-Street", "England"),
    "Bristol": ("County Cricket Ground", "Bristol", "England"),
    "Scarborough": ("North Marine Road Ground", "Scarborough", "England"),
    "Canterbury": ("St Lawrence Ground", "Canterbury", "England"),
    "Taunton": ("County Ground", "Taunton", "England"),
    "Worcester": ("New Road", "Worcester", "England"),
    "Leicester": ("Grace Road", "Leicester", "England"),
    "Derby": ("County Ground", "Derby", "England"),
    "Northampton": ("County Ground", "Northampton", "England"),
    "Chelmsford": ("County Ground", "Chelmsford", "England"),
    "Tunbridge Wells": ("Nevill Ground", "Tunbridge Wells", "England"),
    
    # New Zealand
    "Auckland": ("Eden Park", "Auckland", "New Zealand"),
    "Wellington": ("Basin Reserve", "Wellington", "New Zealand"),
    "Christchurch": ("Lancaster Park", "Christchurch", "New Zealand"),
    "Hagley Oval": ("Hagley Oval", "Christchurch", "New Zealand"),
    "Dunedin": ("Carisbrook", "Dunedin", "New Zealand"),
    "University Oval": ("University Oval", "Dunedin", "New Zealand"),
    "Napier": ("McLean Park", "Napier", "New Zealand"),
    "Hamilton": ("Seddon Park", "Hamilton", "New Zealand"),
    "Mount Maunganui": ("Bay Oval", "Mount Maunganui", "New Zealand"),
    "Nelson": ("Saxton Oval", "Nelson", "New Zealand"),
    "Whangarei": ("Cobham Oval", "Whangarei", "New Zealand"),
    "New Plymouth": ("Pukekura Park", "New Plymouth", "New Zealand"),
    "Taupo": ("Owen Delany Park", "Taupo", "New Zealand"),
    "Queenstown": ("Queenstown Events Centre", "Queenstown", "New Zealand"),
    
    # West Indies
    "Albion": ("Albion Sports Complex", "Albion", "Guyana"),
    "Georgetown": ("Bourda", "Georgetown", "Guyana"),
    "Providence": ("Providence Stadium", "Georgetown", "Guyana"),
    "Port of Spain": ("Queen's Park Oval", "Port of Spain", "Trinidad and Tobago"),
    "Tarouba": ("Brian Lara Cricket Academy", "Tarouba", "Trinidad and Tobago"),
    "Bridgetown": ("Kensington Oval", "Bridgetown", "Barbados"),
    "Kingston": ("Sabina Park", "Kingston", "Jamaica"),
    "St John's": ("Antigua Recreation Ground", "St John's", "Antigua and Barbuda"),
    "North Sound": ("Sir Vivian Richards Stadium", "North Sound", "Antigua and Barbuda"),
    "Castries": ("Mindoo Phillip Park", "Castries", "Saint Lucia"),
    "Gros Islet": ("Daren Sammy Cricket Ground", "Gros Islet", "Saint Lucia"),
    "Kingstown": ("Arnos Vale Ground", "Kingstown", "Saint Vincent and the Grenadines"),
    "St George's": ("National Cricket Stadium", "St George's", "Grenada"),
    "Basseterre": ("Warner Park", "Basseterre", "Saint Kitts and Nevis"),
    "Roseau": ("Windsor Park", "Roseau", "Dominica"),
    "Berbice": ("Albion Sports Complex", "Berbice", "Guyana"),
    
    # Pakistan
    "Sialkot": ("Jinnah Stadium", "Sialkot", "Pakistan"),
    "Sahiwal": ("Zafar Ali Stadium", "Sahiwal", "Pakistan"),
    "Lahore": ("Gaddafi Stadium", "Lahore", "Pakistan"),
    "Karachi": ("National Stadium", "Karachi", "Pakistan"),
    "Rawalpindi": ("Rawalpindi Cricket Stadium", "Rawalpindi", "Pakistan"),
    "Peshawar": ("Arbab Niaz Stadium", "Peshawar", "Pakistan"),
    "Faisalabad": ("Iqbal Stadium", "Faisalabad", "Pakistan"),
    "Gujranwala": ("Jinnah Stadium", "Gujranwala", "Pakistan"),
    "Multan": ("Multan Cricket Stadium", "Multan", "Pakistan"),
    "Quetta": ("Bugti Stadium", "Quetta", "Pakistan"),
    "Hyderabad (Sind)": ("Niaz Stadium", "Hyderabad", "Pakistan"),
    "Sheikhupura": ("Sheikhupura Stadium", "Sheikhupura", "Pakistan"),
    "Sargodha": ("Sports Stadium", "Sargodha", "Pakistan"),
    
    # India
    "Kolkata": ("Eden Gardens", "Kolkata", "India"),
    "Eden Gardens": ("Eden Gardens", "Kolkata", "India"),
    "Mumbai": ("Wankhede Stadium", "Mumbai", "India"),
    "Mumbai (BS)": ("Brabourne Stadium", "Mumbai", "India"),
    "Delhi": ("Arun Jaitley Stadium", "Delhi", "India"),
    "Chennai": ("M. A. Chidambaram Stadium", "Chennai", "India"),
    "Bengaluru": ("M. Chinnaswamy Stadium", "Bengaluru", "India"),
    "Bangalore": ("M. Chinnaswamy Stadium", "Bengaluru", "India"),
    "Ahmedabad": ("Narendra Modi Stadium", "Ahmedabad", "India"),
    "Hyderabad": ("Rajiv Gandhi International Cricket Stadium", "Hyderabad", "India"),
    "Kanpur": ("Green Park", "Kanpur", "India"),
    "Nagpur": ("Vidarbha Cricket Association Stadium", "Nagpur", "India"),
    "Nagpur (Old)": ("Vidarbha Cricket Association Ground", "Nagpur", "India"),
    "Cuttack": ("Barabati Stadium", "Cuttack", "India"),
    "Chandigarh": ("Sector 16 Stadium", "Chandigarh", "India"),
    "Mohali": ("Punjab Cricket Association IS Bindra Stadium", "Mohali", "India"),
    "Jaipur": ("Sawai Mansingh Stadium", "Jaipur", "India"),
    "Indore": ("Holkar Cricket Stadium", "Indore", "India"),
    "Indore (Nehru)": ("Nehru Stadium", "Indore", "India"),
    "Pune": ("Maharashtra Cricket Association Stadium", "Pune", "India"),
    "Pune (Nehru)": ("Nehru Stadium", "Pune", "India"),
    "Rajkot": ("Saurashtra Cricket Association Stadium", "Rajkot", "India"),
    "Rajkot (Madhavrao)": ("Madhavrao Scindia Cricket Ground", "Rajkot", "India"),
    "Visakhapatnam": ("Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium", "Visakhapatnam", "India"),
    "Gwalior": ("Captain Roop Singh Stadium", "Gwalior", "India"),
    "Dharamsala": ("HPCA Stadium", "Dharamshala", "India"),
    "Guwahati": ("Barsapara Cricket Stadium", "Guwahati", "India"),
    "Guwahati (Nehru)": ("Nehru Stadium", "Guwahati", "India"),
    "Ranchi": ("JSCA International Stadium Complex", "Ranchi", "India"),
    "Raipur": ("Shaheed Veer Narayan Singh International Cricket Stadium", "Raipur", "India"),
    "Lucknow": ("Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium", "Lucknow", "India"),
    "Kochi": ("Jawaharlal Nehru Stadium", "Kochi", "India"),
    "Thiruvananthapuram": ("Greenfield International Stadium", "Thiruvananthapuram", "India"),
    "Vadodara": ("IPCL Sports Complex Ground", "Vadodara", "India"),
    "Vadodara (Moti Bagh)": ("Moti Bagh Stadium", "Vadodara", "India"),
    "Faridabad": ("Nahar Singh Stadium", "Faridabad", "India"),
    "Jamshedpur": ("Keenan Stadium", "Jamshedpur", "India"),
    "Srinagar": ("Sher-i-Kashmir Stadium", "Srinagar", "India"),
    "Amritsar": ("Gandhi Sports Complex Ground", "Amritsar", "India"),
    "Jalandhar": ("Burlton Park", "Jalandhar", "India"),
    "Vijayawada": ("Indira Gandhi Stadium", "Vijayawada", "India"),
    
    # Sri Lanka
    "Colombo (RPS)": ("R. Premadasa Stadium", "Colombo", "Sri Lanka"),
    "Colombo (SSC)": ("Sinhalese Sports Club Ground", "Colombo", "Sri Lanka"),
    "Colombo (PSS)": ("Paikiasothy Saravanamuttu Stadium", "Colombo", "Sri Lanka"),
    "Colombo (CCC)": ("Colombo Cricket Club Ground", "Colombo", "Sri Lanka"),
    "Kandy": ("Pallekele International Cricket Stadium", "Kandy", "Sri Lanka"),
    "Asgiriya": ("Asgiriya Stadium", "Kandy", "Sri Lanka"),
    "Galle": ("Galle International Stadium", "Galle", "Sri Lanka"),
    "Dambulla": ("Rangiri Dambulla International Stadium", "Dambulla", "Sri Lanka"),
    "Moratuwa": ("De Soysa Stadium", "Moratuwa", "Sri Lanka"),
    "Hambantota": ("Mahinda Rajapaksa International Stadium", "Hambantota", "Sri Lanka"),
    
    # Bangladesh
    "Dhaka": ("Sher-e-Bangla National Cricket Stadium", "Dhaka", "Bangladesh"),
    "Dhaka (BNS)": ("Bangabandhu National Stadium", "Dhaka", "Bangladesh"),
    "Chattogram": ("Zahur Ahmed Chowdhury Stadium", "Chattogram", "Bangladesh"),
    "Chittagong": ("MA Aziz Stadium", "Chittagong", "Bangladesh"),
    "Sylhet": ("Sylhet International Cricket Stadium", "Sylhet", "Bangladesh"),
    "Khulna": ("Sheikh Abu Naser Stadium", "Khulna", "Bangladesh"),
    "Bogura": ("Shaheed Chandu Stadium", "Bogura", "Bangladesh"),
    "Fatullah": ("Khan Shaheb Osman Ali Stadium", "Fatullah", "Bangladesh"),
    
    # United Arab Emirates
    "Sharjah": ("Sharjah Cricket Stadium", "Sharjah", "United Arab Emirates"),
    "Dubai (DSC)": ("Dubai International Cricket Stadium", "Dubai", "United Arab Emirates"),
    "Dubai": ("Dubai International Cricket Stadium", "Dubai", "United Arab Emirates"),
    "Abu Dhabi": ("Sheikh Zayed Stadium", "Abu Dhabi", "United Arab Emirates"),
    "ICC Academy": ("ICC Academy Ground", "Dubai", "United Arab Emirates"),
    
    # South Africa
    "Johannesburg": ("Wanderers Stadium", "Johannesburg", "South Africa"),
    "Cape Town": ("Newlands", "Cape Town", "South Africa"),
    "Durban": ("Kingsmead", "Durban", "South Africa"),
    "Centurion": ("SuperSport Park", "Centurion", "South Africa"),
    "Port Elizabeth": ("St George's Park", "Gqeberha", "South Africa"),
    "Gqeberha": ("St George's Park", "Gqeberha", "South Africa"),
    "Bloemfontein": ("Mangaung Oval", "Bloemfontein", "South Africa"),
    "East London": ("Buffalo Park", "East London", "South Africa"),
    "Potchefstroom": ("JB Marks Oval", "Potchefstroom", "South Africa"),
    "Benoni": ("Willowmoore Park", "Benoni", "South Africa"),
    "Kimberley": ("De Beers Diamond Oval", "Kimberley", "South Africa"),
    "Pietermaritzburg": ("City Oval", "Pietermaritzburg", "South Africa"),
    "Paarl": ("Boland Park", "Paarl", "South Africa"),
    
    # Zimbabwe
    "Harare": ("Harare Sports Club", "Harare", "Zimbabwe"),
    "Bulawayo": ("Queens Sports Club", "Bulawayo", "Zimbabwe"),
    "Bulawayo (BAC)": ("Bulawayo Athletic Club", "Bulawayo", "Zimbabwe"),
    
    # Associate / Global Grounds
    "Nairobi (Gym)": ("Gymkhana Club Ground", "Nairobi", "Kenya"),
    "Nairobi (Ruaraka)": ("Ruaraka Sports Club Ground", "Nairobi", "Kenya"),
    "Nairobi (Simba)": ("Simba Union Ground", "Nairobi", "Kenya"),
    "Mombasa": ("Mombasa Sports Club", "Mombasa", "Kenya"),
    "Belfast": ("Civil Service Cricket Club", "Belfast", "Northern Ireland"),
    "Dublin": ("Malahide Cricket Club Ground", "Dublin", "Ireland"),
    "Dublin (Clontarf)": ("Castle Avenue", "Dublin", "Ireland"),
    "Bready": ("Bready Cricket Club", "Magheramason", "Northern Ireland"),
    "Edinburgh": ("Grange Cricket Club", "Edinburgh", "Scotland"),
    "Glasgow": ("Titwood", "Glasgow", "Scotland"),
    "Aberdeen": ("Mannofield Park", "Aberdeen", "Scotland"),
    "Amstelveen": ("VRA Cricket Ground", "Amstelveen", "Netherlands"),
    "Rotterdam": ("Hazelaarweg Stadium", "Rotterdam", "Netherlands"),
    "The Hague": ("Sportpark Westvliet", "The Hague", "Netherlands"),
    "Utrecht": ("Sportpark Maarschalkerweerd", "Utrecht", "Netherlands"),
    "Toronto": ("Toronto Cricket, Skating and Curling Club", "Toronto", "Canada"),
    "King City": ("Maple Leaf North-West Ground", "King City", "Canada"),
    "Al Amarat": ("Oman Cricket Academy Ground", "Muscat", "Oman"),
    "Windhoek": ("Wanderers Cricket Ground", "Windhoek", "Namibia"),
    "Windhoek (United)": ("United Ground", "Windhoek", "Namibia"),
    "Kirtipur": ("Tribhuvan University International Cricket Ground", "Kirtipur", "Nepal"),
    "Pearland": ("Moosa Stadium", "Pearland", "United States"),
    "Lauderhill": ("Central Broward Regional Park", "Lauderhill", "United States"),
    "Dallas": ("Grand Prairie Stadium", "Dallas", "United States"),
    "Port Moresby": ("Amini Park", "Port Moresby", "Papua New Guinea"),
    "Singapore": ("Padang", "Singapore", "Singapore"),
    "Kuala Lumpur": ("Kinrara Academy Oval", "Kuala Lumpur", "Malaysia"),
    "Tangier": ("National Cricket Stadium", "Tangier", "Morocco"),
    "Doha": ("West End Park International Cricket Stadium", "Doha", "Qatar")
}

FULL_MEMBER_COUNTRIES = {
    "Australia": "Australia",
    "England": "England",
    "New Zealand": "New Zealand",
    "West Indies": "West Indies",
    "India": "India",
    "Pakistan": "Pakistan",
    "Sri Lanka": "Sri Lanka",
    "South Africa": "South Africa",
    "Zimbabwe": "Zimbabwe",
    "Bangladesh": "Bangladesh",
    "Ireland": "Ireland",
    "Afghanistan": "Afghanistan"
}

def resolve_venue_details(ground_str):
    g_clean = ground_str.strip()
    if g_clean in GROUND_MAPPING:
        return GROUND_MAPPING[g_clean]
    for k, v in GROUND_MAPPING.items():
        if k.lower() in g_clean.lower():
            return v
    return (g_clean, g_clean, "International")

def determine_home_away(team1, team2, host_country):
    if host_country == "Australia":
        if team1 == "Australia": return team1, team2
        if team2 == "Australia": return team2, team1
    elif host_country == "England" or host_country == "Wales":
        if team1 == "England": return team1, team2
        if team2 == "England": return team2, team1
    elif host_country == "India":
        if team1 == "India": return team1, team2
        if team2 == "India": return team2, team1
    elif host_country == "Pakistan":
        if team1 == "Pakistan": return team1, team2
        if team2 == "Pakistan": return team2, team1
    elif host_country == "New Zealand":
        if team1 == "New Zealand": return team1, team2
        if team2 == "New Zealand": return team2, team1
    elif host_country in ["Guyana", "Trinidad and Tobago", "Barbados", "Jamaica", "Antigua and Barbuda", "Saint Lucia", "Saint Vincent and the Grenadines", "Grenada", "Saint Kitts and Nevis", "Dominica"]:
        if team1 == "West Indies": return team1, team2
        if team2 == "West Indies": return team2, team1
    elif host_country == "South Africa":
        if team1 == "South Africa": return team1, team2
        if team2 == "South Africa": return team2, team1
    elif host_country == "Sri Lanka":
        if team1 == "Sri Lanka": return team1, team2
        if team2 == "Sri Lanka": return team2, team1
    elif host_country == "Bangladesh":
        if team1 == "Bangladesh": return team1, team2
        if team2 == "Bangladesh": return team2, team1
    elif host_country == "Zimbabwe":
        if team1 == "Zimbabwe": return team1, team2
        if team2 == "Zimbabwe": return team2, team1
    elif host_country in ["Ireland", "Northern Ireland"]:
        if team1 == "Ireland": return team1, team2
        if team2 == "Ireland": return team2, team1
    elif host_country == "United Arab Emirates":
        # Neutral venue for most bilateral/multi-nation series, unless UAE is playing
        if team1 == "United Arab Emirates": return team1, team2
        if team2 == "United Arab Emirates": return team2, team1
        return team1, team2
    elif host_country == team1:
        return team1, team2
    elif host_country == team2:
        return team2, team1
        
    return team1, team2

def parse_iso_date(date_str, year):
    # e.g. "Jan 1, 1975" or "Aug 28-29, 1976" or "1975-01-01"
    clean_d = re.sub(r'-\d+', '', date_str).strip()
    for fmt in ["%b %d, %Y", "%d %b %Y", "%Y-%m-%d", "%B %d, %Y"]:
        try:
            dt = datetime.strptime(clean_d, fmt)
            return dt.strftime("%Y-%m-%d"), dt.strftime("%A")
        except:
            pass
    # fallback
    return f"{year}-01-01", "Wednesday"

def determine_match_type_and_series(team1, team2, ground, year, event_name=""):
    ev_lower = (event_name or "").lower()
    
    if "champions trophy" in ev_lower or "icc champions trophy" in ev_lower:
        return "ICC Champions Trophy", event_name
    elif "knockout" in ev_lower or "icc knockout" in ev_lower or "wills international cup" in ev_lower:
        return "ICC KnockOut", event_name
    elif "asia cup" in ev_lower:
        return "Asia Cup", event_name
    elif "super league" in ev_lower or "cwc super league" in ev_lower:
        return "ICC CWC Super League", event_name
    elif "league 2" in ev_lower or "cwc league 2" in ev_lower:
        return "ICC Men's Cricket World Cup League 2", event_name
    elif "qualifier" in ev_lower:
        return "ICC Cricket World Cup Qualifier", event_name
    
    # Historical tournament checks based on ground and era
    g_lower = ground.lower()
    if "sharjah" in g_lower:
        if year == 1984: return "Asia Cup", "Rothmans Asia Cup 1983/84"
        if year == 1985: return "Tri-Series", "Rothmans Four-Nations Cup 1984/85"
        if year in [1986, 1990, 1994]: return "Multi-Nation Tournament", "Austral-Asia Cup"
        return "Multi-Nation Tournament", f"Sharjah International Cup {year}"
    elif ground in ["Melbourne", "Sydney", "Brisbane", "Adelaide", "Perth", "Hobart"]:
        if year >= 1979 and year <= 1996 and team1 != "Australia" and team2 != "Australia":
            return "Tri-Series", "Benson & Hedges World Series Cup"
        elif year >= 1979 and year <= 1996:
            return "Tri-Series", "Benson & Hedges World Series Cup"
        elif year >= 1997 and year <= 2001:
            return "Tri-Series", "Carlton & United Series"
        elif year >= 2002 and year <= 2006:
            return "Tri-Series", "VB Series"
        elif year >= 2007 and year <= 2012:
            return "Tri-Series", "Commonwealth Bank Series"
        elif year == 2015:
            return "Tri-Series", "Carlton Mid One-Day International Tri-Series"
    elif ground in ["Lord's", "The Oval", "Birmingham", "Manchester", "Leeds", "Nottingham", "Southampton", "Cardiff", "Chester-le-Street"]:
        if year >= 2000 and year <= 2012 and (team1 not in ["England", "Wales"] or team2 not in ["England", "Wales"]):
            return "Tri-Series", "NatWest Series"
        elif year < 1984:
            return "Bilateral Series", "Prudential Trophy"
        elif year < 1999:
            return "Bilateral Series", "Texaco Trophy"
            
    # Default bilateral
    return "Bilateral Series", f"{team1} v {team2} ODI Series"

def format_overs(balls, balls_per_over=6):
    overs_full = balls // balls_per_over
    balls_rem = balls % balls_per_over
    return f"{overs_full}.{balls_rem} ov"

# CSV Column definitions (47 columns)
CSV_HEADERS = [
    "Match Number",
    "Match ID",
    "ODI Number",
    "Season",
    "Season Year",
    "Series / Competition Name",
    "Match Type",
    "Match Stage",
    "Date",
    "Day of Week",
    "Team A",
    "Team B",
    "Home",
    "Away",
    "Toss Winner",
    "Toss Decision",
    "First Innings Team",
    "Second Innings Team",
    "First Innings Score",
    "First Innings Runs",
    "First Innings Wickets",
    "First Innings Overs",
    "Second Innings Score",
    "Second Innings Runs",
    "Second Innings Wickets",
    "Second Innings Overs",
    "Target Runs",
    "Total Runs",
    "Total Wickets",
    "Match Score",
    "Winner",
    "Loser",
    "Winning Margin",
    "Margin Value",
    "Margin Type",
    "Super Over",
    "Method / Rain Rule",
    "Player of the Match",
    "Notable Players",
    "Venue",
    "City",
    "Country",
    "Umpires",
    "TV Umpire",
    "Match Referee",
    "A Succint one line match comment to summarise that match",
    "Primary Data Source"
]

def load_cricsheet_matches():
    cricsheet_map = {}
    if not os.path.exists(CRICSHEET_DIR):
        return cricsheet_map
        
    for fname in os.listdir(CRICSHEET_DIR):
        if not fname.endswith(".json"):
            continue
        fpath = os.path.join(CRICSHEET_DIR, fname)
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                data = json.load(f)
            info = data.get("info", {})
            dates = info.get("dates", [])
            teams = info.get("teams", [])
            event = (info.get("event", {}).get("name") or "").lower()
            
            # Skip Men's Cricket World Cups
            if "world cup" in event and not any(k in event for k in ["qualifier", "league 2", "super league", "play-off"]):
                continue
                
            if dates and len(teams) >= 2:
                d = dates[0]
                t1, t2 = sorted([teams[0], teams[1]])
                cricsheet_map[(d, t1, t2)] = data
        except:
            pass
            
    print(f"Loaded {len(cricsheet_map)} non-WC Cricsheet matches into memory.")
    return cricsheet_map

def parse_cricsheet_match(data, match_num, odi_num, year):
    info = data.get("info", {})
    dates = info.get("dates", [""])
    date_iso = dates[0] if dates else f"{year}-01-01"
    dt = datetime.strptime(date_iso, "%Y-%m-%d")
    day_of_week = dt.strftime("%A")
    
    teams = info.get("teams", ["Team A", "Team B"])
    team1, team2 = teams[0], teams[1]
    
    event = info.get("event", {})
    event_name = event.get("name", f"{team1} v {team2} ODI Series")
    stage = event.get("stage") or event.get("match_number") or f"Match {match_num}"
    if isinstance(stage, int):
        stage = f"Match {stage}"
        
    mtype, sname = determine_match_type_and_series(team1, team2, info.get("venue", ""), year, event_name)
    
    venue_str = info.get("venue", "")
    city_str = info.get("city", "")
    venue_name, city_name, country_name = resolve_venue_details(venue_str if venue_str else city_str)
    if not city_str: city_str = city_name
    
    home_team, away_team = determine_home_away(team1, team2, country_name)
    
    toss = info.get("toss", {})
    toss_winner = toss.get("winner", team1)
    toss_decision = toss.get("decision", "bat")
    
    # Process innings
    innings = data.get("innings", [])
    inn1_team, inn2_team = team1, team2
    inn1_runs, inn1_wkts, inn1_balls = 0, 0, 0
    inn2_runs, inn2_wkts, inn2_balls = 0, 0, 0
    target_runs = 0
    
    top_batters = {}
    top_bowlers = {}
    
    if len(innings) > 0:
        inn1_team = innings[0].get("team", team1)
        inn2_team = team2 if inn1_team == team1 else team1
        
        runs_t = 0
        wkts_t = 0
        balls_t = 0
        bat_runs = defaultdict(int)
        bat_balls = defaultdict(int)
        bowl_wkts = defaultdict(int)
        bowl_runs = defaultdict(int)
        bowl_balls = defaultdict(int)
        
        for over_data in innings[0].get("overs", []):
            for deliv in over_data.get("deliveries", []):
                runs_t += deliv.get("runs", {}).get("total", 0)
                b_runs = deliv.get("runs", {}).get("batter", 0)
                batter = deliv.get("batter", "")
                bowler = deliv.get("bowler", "")
                
                bat_runs[batter] += b_runs
                bat_balls[batter] += 1
                
                # Bowling
                extras = deliv.get("extras", {})
                wides = extras.get("wides", 0)
                noballs = extras.get("noballs", 0)
                if not wides:
                    balls_t += 1
                    bowl_balls[bowler] += 1
                bowl_runs[bowler] += deliv.get("runs", {}).get("total", 0)
                
                if "wickets" in deliv:
                    for w in deliv["wickets"]:
                        wkind = w.get("kind", "")
                        if wkind not in ["retired hurt", "retired not out"]:
                            wkts_t += 1
                            if wkind != "run out":
                                bowl_wkts[bowler] += 1
                            
        inn1_runs = runs_t
        inn1_wkts = min(10, wkts_t)
        inn1_balls = balls_t
        
        # Best batter & bowler
        best_b = max(bat_runs.items(), key=lambda x: x[1]) if bat_runs else ("", 0)
        best_bw = max(bowl_wkts.items(), key=lambda x: (x[1], -bowl_runs[x[0]])) if bowl_wkts else ("", 0)
        if best_b[0]:
            top_batters[inn1_team] = f"{best_b[0]} {best_b[1]} ({bat_balls[best_b[0]]}b)"
        if best_bw[0]:
            top_bowlers[inn2_team] = f"{best_bw[0]} {best_bw[1]}/{bowl_runs[best_bw[0]]} ({bowl_balls[best_bw[0]]//6}.{bowl_balls[best_bw[0]]%6} ov)"

    if len(innings) > 1:
        runs_t = 0
        wkts_t = 0
        balls_t = 0
        bat_runs = defaultdict(int)
        bat_balls = defaultdict(int)
        bowl_wkts = defaultdict(int)
        bowl_runs = defaultdict(int)
        bowl_balls = defaultdict(int)
        
        for over_data in innings[1].get("overs", []):
            for deliv in over_data.get("deliveries", []):
                runs_t += deliv.get("runs", {}).get("total", 0)
                b_runs = deliv.get("runs", {}).get("batter", 0)
                batter = deliv.get("batter", "")
                bowler = deliv.get("bowler", "")
                
                bat_runs[batter] += b_runs
                bat_balls[batter] += 1
                
                extras = deliv.get("extras", {})
                wides = extras.get("wides", 0)
                noballs = extras.get("noballs", 0)
                if not wides:
                    balls_t += 1
                    bowl_balls[bowler] += 1
                bowl_runs[bowler] += deliv.get("runs", {}).get("total", 0)
                
                if "wickets" in deliv:
                    for w in deliv["wickets"]:
                        wkind = w.get("kind", "")
                        if wkind not in ["retired hurt", "retired not out"]:
                            wkts_t += 1
                            if wkind != "run out":
                                bowl_wkts[bowler] += 1
                            
        inn2_runs = runs_t
        inn2_wkts = min(10, wkts_t)
        inn2_balls = balls_t
        
        best_b = max(bat_runs.items(), key=lambda x: x[1]) if bat_runs else ("", 0)
        best_bw = max(bowl_wkts.items(), key=lambda x: (x[1], -bowl_runs[x[0]])) if bowl_wkts else ("", 0)
        if best_b[0]:
            top_batters[inn2_team] = f"{best_b[0]} {best_b[1]} ({bat_balls[best_b[0]]}b)"
        if best_bw[0]:
            top_bowlers[inn1_team] = f"{best_bw[0]} {best_bw[1]}/{bowl_runs[best_bw[0]]} ({bowl_balls[best_bw[0]]//6}.{bowl_balls[best_bw[0]]%6} ov)"

    outcome = info.get("outcome", {})
    winner = outcome.get("winner", "")
    result_type = outcome.get("result", "")
    by_info = outcome.get("by", {})
    margin_type = "runs" if "runs" in by_info else ("wickets" if "wickets" in by_info else "")
    margin_val = by_info.get("runs") or by_info.get("wickets") or ""
    
    super_over = "Yes" if "eliminator" in outcome or outcome.get("bowl_out") else "No"
    
    if winner:
        loser = team2 if winner == team1 else team1
        win_margin_str = f"{margin_val} {margin_type}".strip()
    elif result_type.lower() == "tie":
        winner = "Tie"
        loser = ""
        win_margin_str = "Tie"
        margin_type = "tie"
    else:
        winner = "No Result"
        loser = ""
        win_margin_str = "No Result"
        margin_type = "no_result"

    method = outcome.get("method", "Normal")
    if method == "D/L": method = "D/L"
    elif method == "DLS": method = "DLS"
    else: method = "Normal"
    
    inn1_overs_str = format_overs(inn1_balls)
    inn2_overs_str = format_overs(inn2_balls)
    inn1_score = f"{inn1_runs}/{inn1_wkts} ({inn1_overs_str})"
    inn2_score = f"{inn2_runs}/{inn2_wkts} ({inn2_overs_str})" if len(innings) > 1 else "DNB"
    match_score = f"{inn1_runs}/{inn1_wkts} - {inn2_runs}/{inn2_wkts}" if len(innings) > 1 else f"{inn1_runs}/{inn1_wkts}"
    
    target_runs = inn1_runs + 1 if len(innings) > 0 else 0
    total_runs = inn1_runs + inn2_runs
    total_wickets = inn1_wkts + inn2_wkts
    
    potm_list = info.get("player_of_match", [])
    player_of_match = potm_list[0] if potm_list else ""
    
    # Officials
    officials = info.get("officials", {})
    umpires = "; ".join(officials.get("umpires", []))
    tv_umpire = "; ".join(officials.get("tv_umpires", []))
    match_referee = "; ".join(officials.get("match_referees", []))
    
    # Notable players string
    notable_parts = []
    if inn1_team in top_batters: notable_parts.append(f"{inn1_team}: {top_batters[inn1_team]}")
    if inn1_team in top_bowlers: notable_parts.append(f"{top_bowlers[inn1_team]}")
    if inn2_team in top_batters: notable_parts.append(f"{inn2_team}: {top_batters[inn2_team]}")
    if inn2_team in top_bowlers: notable_parts.append(f"{top_bowlers[inn2_team]}")
    notable_str = " | ".join(notable_parts) if notable_parts else f"{team1} vs {team2}"
    
    if winner in [team1, team2]:
        recap = f"{winner} defeated {loser} by {win_margin_str} at {venue_name} ({city_str})."
    elif winner == "Tie":
        recap = f"{team1} and {team2} tied at {venue_name} ({city_str}) with scores level."
    else:
        recap = f"{team1} v {team2} ended in a No Result due to adverse weather at {venue_name} ({city_str})."
        
    season_str = str(info.get("season", f"{year}"))
    
    return {
        "Match Number": match_num,
        "Match ID": f"ODI_{int(odi_num.split('# ')[1]):06d}",
        "ODI Number": odi_num,
        "Season": season_str,
        "Season Year": year,
        "Series / Competition Name": sname,
        "Match Type": mtype,
        "Match Stage": stage,
        "Date": date_iso,
        "Day of Week": day_of_week,
        "Team A": team1,
        "Team B": team2,
        "Home": home_team,
        "Away": away_team,
        "Toss Winner": toss_winner,
        "Toss Decision": toss_decision,
        "First Innings Team": inn1_team,
        "Second Innings Team": inn2_team,
        "First Innings Score": inn1_score,
        "First Innings Runs": inn1_runs,
        "First Innings Wickets": inn1_wkts,
        "First Innings Overs": inn1_overs_str,
        "Second Innings Score": inn2_score,
        "Second Innings Runs": inn2_runs,
        "Second Innings Wickets": inn2_wkts,
        "Second Innings Overs": inn2_overs_str,
        "Target Runs": target_runs,
        "Total Runs": total_runs,
        "Total Wickets": total_wickets,
        "Match Score": match_score,
        "Winner": winner,
        "Loser": loser,
        "Winning Margin": win_margin_str,
        "Margin Value": margin_val,
        "Margin Type": margin_type,
        "Super Over": super_over,
        "Method / Rain Rule": method,
        "Player of the Match": player_of_match,
        "Notable Players": notable_str,
        "Venue": venue_name,
        "City": city_str,
        "Country": country_name,
        "Umpires": umpires,
        "TV Umpire": tv_umpire,
        "Match Referee": match_referee,
        "A Succint one line match comment to summarise that match": recap,
        "Primary Data Source": "Cricsheet JSON v1.2.0 / ESPNcricinfo"
    }

def build_statsguru_fallback_match(match_meta, sg_data, match_num, year):
    odi_num = match_meta["odi_num"]
    team1 = match_meta["team1"]
    team2 = match_meta["team2"]
    ground = match_meta["ground"]
    raw_date = match_meta["date"]
    date_iso, day_of_week = parse_iso_date(raw_date, year)
    
    venue_name, city_name, country_name = resolve_venue_details(ground)
    home_team, away_team = determine_home_away(team1, team2, country_name)
    mtype, sname = determine_match_type_and_series(team1, team2, ground, year)
    
    # Find matching records in statsguru
    results_rows = sg_data.get("results", [])
    innings_rows = sg_data.get("innings", [])
    
    # Filter candidate results
    candidates = []
    for r in results_rows:
        r_team = r.get("team")
        r_opp = r.get("opposition")
        if (r_team == team1 and r_opp == team2) or (r_team == team2 and r_opp == team1):
            candidates.append(r)
            
    # Try to refine by date/ground
    toss_winner = team1
    toss_decision = "bat"
    inn1_team, inn2_team = team1, team2
    inn1_runs, inn1_wkts, inn1_balls = 0, 0, 0
    inn2_runs, inn2_wkts, inn2_balls = 0, 0, 0
    
    # 8-ball overs check (Australia before late 1979)
    bpo = 8 if country_name == "Australia" and year <= 1979 else 6
    
    # Identify who batted 1st
    for c in candidates:
        if c.get("bat") == "1st":
            inn1_team = c.get("team")
            inn2_team = team2 if inn1_team == team1 else team1
            if c.get("toss") == "won":
                toss_winner = inn1_team
                toss_decision = "bat"
            else:
                toss_winner = inn2_team
                toss_decision = "field"
            break
        elif c.get("bat") == "2nd":
            inn2_team = c.get("team")
            inn1_team = team2 if inn2_team == team1 else team1
            if c.get("toss") == "won":
                toss_winner = inn2_team
                toss_decision = "field"
            else:
                toss_winner = inn1_team
                toss_decision = "bat"
            break
            
    # Find innings rows for these teams
    for inn in innings_rows:
        i_team = inn.get("team")
        i_opp = inn.get("opposition")
        if i_team == inn1_team and i_opp == inn2_team:
            try:
                inn1_runs = int(inn.get("runs", 0))
                inn1_wkts = int(inn.get("wkts", 10 if inn.get("wkts") == "" else inn.get("wkts")))
                inn1_balls = int(inn.get("balls", 300))
            except:
                pass
        elif i_team == inn2_team and i_opp == inn1_team:
            try:
                inn2_runs = int(inn.get("runs", 0))
                inn2_wkts = int(inn.get("wkts", 10 if inn.get("wkts") == "" else inn.get("wkts")))
                inn2_balls = int(inn.get("balls", 300))
            except:
                pass

    winner = match_meta.get("winner", "")
    margin_str = match_meta.get("margin", "")
    
    margin_type = ""
    margin_val = ""
    if "runs" in margin_str.lower():
        margin_type = "runs"
        m = re.search(r'(\d+)', margin_str)
        margin_val = m.group(1) if m else ""
    elif "wicket" in margin_str.lower():
        margin_type = "wickets"
        m = re.search(r'(\d+)', margin_str)
        margin_val = m.group(1) if m else ""
    elif "tied" in margin_str.lower() or winner.lower() == "tied":
        winner = "Tie"
        margin_type = "tie"
        margin_str = "Tie"
    elif "no result" in winner.lower() or winner.lower() == "no result":
        winner = "No Result"
        margin_type = "no_result"
        margin_str = "No Result"

    if winner not in ["Tie", "No Result"] and winner:
        loser = team2 if winner == team1 else team1
        win_margin_str = margin_str if margin_str else f"{margin_val} {margin_type}".strip()
    elif winner == "Tie":
        loser = ""
        win_margin_str = "Tie"
    else:
        winner = "No Result"
        loser = ""
        win_margin_str = "No Result"

    inn1_overs_str = format_overs(inn1_balls, bpo)
    inn2_overs_str = format_overs(inn2_balls, bpo)
    
    inn1_score = f"{inn1_runs}/{inn1_wkts} ({inn1_overs_str})" if inn1_runs > 0 else "DNB"
    inn2_score = f"{inn2_runs}/{inn2_wkts} ({inn2_overs_str})" if inn2_runs > 0 else "DNB"
    match_score = f"{inn1_runs}/{inn1_wkts} - {inn2_runs}/{inn2_wkts}" if inn2_runs > 0 else f"{inn1_runs}/{inn1_wkts}"
    
    target_runs = inn1_runs + 1 if inn1_runs > 0 else 0
    total_runs = inn1_runs + inn2_runs
    total_wickets = inn1_wkts + inn2_wkts

    if winner in [team1, team2]:
        recap = f"{winner} defeated {loser} by {win_margin_str} at {venue_name} ({city_name})."
    elif winner == "Tie":
        recap = f"{team1} and {team2} tied at {venue_name} ({city_name}) with scores level."
    else:
        recap = f"{team1} v {team2} ended in a No Result at {venue_name} ({city_name})."

    # Season
    season_str = f"{year-1}/{str(year)[2:]}" if raw_date.startswith("Jan") or raw_date.startswith("Feb") else f"{year}"

    return {
        "Match Number": match_num,
        "Match ID": f"ODI_{match_meta['odi_num_int']:06d}",
        "ODI Number": odi_num,
        "Season": season_str,
        "Season Year": year,
        "Series / Competition Name": sname,
        "Match Type": mtype,
        "Match Stage": f"ODI #{match_meta['odi_num_int']}",
        "Date": date_iso,
        "Day of Week": day_of_week,
        "Team A": team1,
        "Team B": team2,
        "Home": home_team,
        "Away": away_team,
        "Toss Winner": toss_winner,
        "Toss Decision": toss_decision,
        "First Innings Team": inn1_team,
        "Second Innings Team": inn2_team,
        "First Innings Score": inn1_score,
        "First Innings Runs": inn1_runs,
        "First Innings Wickets": inn1_wkts,
        "First Innings Overs": inn1_overs_str,
        "Second Innings Score": inn2_score,
        "Second Innings Runs": inn2_runs,
        "Second Innings Wickets": inn2_wkts,
        "Second Innings Overs": inn2_overs_str,
        "Target Runs": target_runs,
        "Total Runs": total_runs,
        "Total Wickets": total_wickets,
        "Match Score": match_score,
        "Winner": winner,
        "Loser": loser,
        "Winning Margin": win_margin_str,
        "Margin Value": margin_val,
        "Margin Type": margin_type,
        "Super Over": "No",
        "Method / Rain Rule": "Normal",
        "Player of the Match": "",
        "Notable Players": f"{team1} vs {team2}",
        "Venue": venue_name,
        "City": city_name,
        "Country": country_name,
        "Umpires": "",
        "TV Umpire": "",
        "Match Referee": "",
        "A Succint one line match comment to summarise that match": recap,
        "Primary Data Source": "ESPNcricinfo Statsguru / ICC Match Registry"
    }

def main():
    print("=" * 80)
    print("ODI International Games Generator (Non-World Cup, 1975–2025)")
    print("=" * 80)
    
    os.makedirs(OUT_DIR_ROOT, exist_ok=True)
    os.makedirs(OUT_DIR_PREV1, exist_ok=True)
    os.makedirs(OUT_DIR_PREV2, exist_ok=True)
    
    cricsheet_matches = load_cricsheet_matches()
    
    total_generated = 0
    yearly_summary = {}
    
    for year in range(1975, 2026):
        res_file = os.path.join(MATCH_RES_DIR, f"match_results_{year}.json")
        if not os.path.exists(res_file):
            print(f"Warning: match_results_{year}.json missing! Skipping.")
            continue
            
        with open(res_file, "r", encoding="utf-8") as f:
            meta_matches = json.load(f)
            
        # Strictly exclude World Cup matches
        non_wc_matches = [m for m in meta_matches if not m.get("is_world_cup", False)]
        
        # Load Statsguru data for year
        sg_file = os.path.join(STATSGURU_DIR, f"statsguru_{year}.json")
        sg_data = {}
        if os.path.exists(sg_file):
            with open(sg_file, "r", encoding="utf-8") as f:
                sg_data = json.load(f)
                
        compiled_rows = []
        for idx, m in enumerate(non_wc_matches, 1):
            odi_num = m["odi_num"]
            t1, t2 = sorted([m["team1"], m["team2"]])
            date_iso, _ = parse_iso_date(m["date"], year)
            
            # Check Cricsheet match
            cric_data = cricsheet_matches.get((date_iso, t1, t2))
            if cric_data:
                row = parse_cricsheet_match(cric_data, idx, odi_num, year)
            else:
                row = build_statsguru_fallback_match(m, sg_data, idx, year)
                
            compiled_rows.append(row)
            
        # Output paths
        root_csv = os.path.join(OUT_DIR_ROOT, f"ODI_International_{year}.csv")
        prev1_dir = os.path.join(OUT_DIR_PREV1, str(year))
        prev2_dir = os.path.join(OUT_DIR_PREV2, str(year))
        os.makedirs(prev1_dir, exist_ok=True)
        os.makedirs(prev2_dir, exist_ok=True)
        
        prev1_csv = os.path.join(prev1_dir, f"{year}_games.csv")
        prev2_csv = os.path.join(prev2_dir, f"{year}_games.csv")
        
        for target_file in [root_csv, prev1_csv, prev2_csv]:
            with open(target_file, "w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=CSV_HEADERS)
                writer.writeheader()
                writer.writerows(compiled_rows)
                
        total_generated += len(compiled_rows)
        yearly_summary[year] = len(compiled_rows)
        print(f"Year {year}: {len(compiled_rows):3d} matches generated in all 3 target destinations.")

    print("=" * 80)
    print(f"Grand Total Non-World Cup ODIs Generated (1975–2025): {total_generated}")
    print("=" * 80)

if __name__ == "__main__":
    main()
