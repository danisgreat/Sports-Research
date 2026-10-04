"""
greek_helpers.py - Team mapping, arenas, cities, notable players, and metadata
for the Greece Basket League (Greek A1 Ethniki / ESAKE / Stoiximan Basket League).
"""

TEAM_MAP = {
    # Panathinaikos
    'παναθηναϊκός': 'Panathinaikos',
    'παναθηναϊκός α.ο.': 'Panathinaikos',
    'παναθηναϊκός αο': 'Panathinaikos',
    'παο': 'Panathinaikos',
    'panathinaikos': 'Panathinaikos',
    'panathinaikos aktor': 'Panathinaikos',
    'panathinaikos b.c.': 'Panathinaikos',
    'panathinaikos bc': 'Panathinaikos',
    'panathinaikos opap': 'Panathinaikos',
    'panathinaikos superfoods': 'Panathinaikos',
    
    # Olympiacos
    'ολυμπιακός': 'Olympiacos',
    'ολυμπιακός σ.φ.π.': 'Olympiacos',
    'ολυμπιακός σφπ': 'Olympiacos',
    'ολυ': 'Olympiacos',
    'olympiacos': 'Olympiacos',
    'olympiacos b.c.': 'Olympiacos',
    'olympiacos bc': 'Olympiacos',
    'olympiacos piraeus': 'Olympiacos',
    
    # AEK
    'αεκ': 'AEK Athens',
    'α.ε.κ.': 'AEK Athens',
    'aek': 'AEK Athens',
    'aek athens': 'AEK Athens',
    'aek bc': 'AEK Athens',
    'aek betsson': 'AEK Athens',
    
    # Aris
    'άρης': 'Aris Thessaloniki',
    'αρης': 'Aris Thessaloniki',
    'α.σ. άρης': 'Aris Thessaloniki',
    'ασ αρης': 'Aris Thessaloniki',
    'aris': 'Aris Thessaloniki',
    'aris thessaloniki': 'Aris Thessaloniki',
    'aris midea': 'Aris Thessaloniki',
    'aris bc': 'Aris Thessaloniki',
    
    # PAOK
    'παοκ': 'PAOK',
    'π.α.ο.κ.': 'PAOK',
    'paok': 'PAOK',
    'paok thessaloniki': 'PAOK',
    'paok mateco': 'PAOK',
    'paok bc': 'PAOK',
    
    # Panionios
    'πανιώνιος': 'Panionios',
    'πανιωνιος': 'Panionios',
    'πανιώνιος γ.σ.σ.': 'Panionios',
    'πανι': 'Panionios',
    'panionios': 'Panionios',
    'panionios bc': 'Panionios',
    
    # Iraklis
    'ηρακλής': 'Iraklis Thessaloniki',
    'ηρακλης': 'Iraklis Thessaloniki',
    'γ.σ. ηρακλής': 'Iraklis Thessaloniki',
    'ηρα': 'Iraklis Thessaloniki',
    'iraklis': 'Iraklis Thessaloniki',
    'iraklis thessaloniki': 'Iraklis Thessaloniki',
    'iraklis bc': 'Iraklis Thessaloniki',
    
    # Peristeri
    'περιστέρι': 'Peristeri',
    'περιστερι': 'Peristeri',
    'γ.σ. περιστερίου': 'Peristeri',
    'peristeri': 'Peristeri',
    'peristeri bc': 'Peristeri',
    'peristeri bwin': 'Peristeri',
    'peristeri domino\'s': 'Peristeri',
    
    # Maroussi
    'μαρούσι': 'Maroussi',
    'μαρουσι': 'Maroussi',
    'γ.σ. αμαρουσίου': 'Maroussi',
    'μαρ': 'Maroussi',
    'maroussi': 'Maroussi',
    'maroussi bc': 'Maroussi',
    
    # Panellinios
    'πανελλήνιος': 'Panellinios',
    'πανελληνιος': 'Panellinios',
    'πανελλήνιος γ.σ.': 'Panellinios',
    'πγσ': 'Panellinios',
    'panellinios': 'Panellinios',
    'panellinios bc': 'Panellinios',
    
    # Apollon Patras
    'απόλλων πατρών': 'Apollon Patras',
    'απολλων πατρων': 'Apollon Patras',
    'α.σ. απόλλων πατρών': 'Apollon Patras',
    'απόλλων π.': 'Apollon Patras',
    'απόλλων': 'Apollon Patras',
    'apollon patras': 'Apollon Patras',
    'apollon patras carna': 'Apollon Patras',
    'apollon bc': 'Apollon Patras',
    
    # Ionikos Nikaias
    'ίωνικος νίκαιας': 'Ionikos Nikaias',
    'ιωνικός νίκαιας': 'Ionikos Nikaias',
    'ιωνικος νικαιας': 'Ionikos Nikaias',
    'α.ο. ιωνικός νίκαιας': 'Ionikos Nikaias',
    'ίων': 'Ionikos Nikaias',
    'ιων': 'Ionikos Nikaias',
    'ionikos nikaias': 'Ionikos Nikaias',
    'ionikos': 'Ionikos Nikaias',
    'ionikos hellenic coin': 'Ionikos Nikaias',
    
    # Sporting Athens
    'σπόρτιγκ': 'Sporting Athens',
    'σπορτιγκ': 'Sporting Athens',
    'α.ο. σπόρτιγκ αθηνών': 'Sporting Athens',
    'α.ο. σπόρτιγκ': 'Sporting Athens',
    'σπορ': 'Sporting Athens',
    'sporting': 'Sporting Athens',
    'sporting athens': 'Sporting Athens',
    
    # Promitheas Patras
    'προμηθέας': 'Promitheas Patras',
    'προμηθεας': 'Promitheas Patras',
    'προμηθέας πατρών': 'Promitheas Patras',
    'promitheas': 'Promitheas Patras',
    'promitheas patras': 'Promitheas Patras',
    'promitheas patras bc': 'Promitheas Patras',
    'promitheas vikos cola': 'Promitheas Patras',
    
    # Kolossos Rhodes
    'κολοσσός': 'Kolossos Rhodes',
    'κολοσσος': 'Kolossos Rhodes',
    'κολοσσός ρόδου': 'Kolossos Rhodes',
    'kolossos': 'Kolossos Rhodes',
    'kolossos rhodes': 'Kolossos Rhodes',
    'kolossos h Hotels': 'Kolossos Rhodes',
    'kolossos h hotels': 'Kolossos Rhodes',
    
    # Lavrio
    'λαύριο': 'Lavrio Megabolt',
    'λαυριο': 'Lavrio Megabolt',
    'γ.σ. λαυρίου': 'Lavrio Megabolt',
    'lavrio': 'Lavrio Megabolt',
    'lavrio megabolt': 'Lavrio Megabolt',
    'lavrio daicar': 'Lavrio Megabolt',
    
    # Karditsa
    'καρδίτσα': 'Karditsa',
    'καρδιτσα': 'Karditsa',
    'α.σ. καρδίτσας': 'Karditsa',
    'karditsa': 'Karditsa',
    'karditsa iaponiki': 'Karditsa',
    'karditsa bc': 'Karditsa',
    
    # Historical teams
    'δημόκριτος': 'Dimokritos Thessaloniki',
    'μ.α.ο. δημόκριτος': 'Dimokritos Thessaloniki',
    'βαο': 'VAO Thessaloniki',
    'β.α.ο.': 'VAO Thessaloniki',
    'χανθ': 'XANTH Thessaloniki',
    'χ.α.ν.θ.': 'XANTH Thessaloniki',
    'ymca': 'XANTH Thessaloniki',
    'γ.σ. λάρισας': 'GS Larissas',
    'γσ λάρισας': 'GS Larissas',
    'λάρισα': 'GS Larissas',
    'λαρισα': 'GS Larissas',
    'larisa': 'GS Larissas',
    'οξύμπια λάρισας': 'Olympia Larissa',
    'ολύμπια λάρισας': 'Olympia Larissa',
    'ολυμπια λαρισας': 'Olympia Larissa',
    'ρέθυμνο': 'Rethymno Cretan Kings',
    'ρεθυμνο': 'Rethymno Cretan Kings',
    'rethymno': 'Rethymno Cretan Kings',
    'rethymno cretan kings': 'Rethymno Cretan Kings',
    'κύμη': 'Kymi',
    'kymi': 'Kymi',
    'κόροιβος': 'Koroivos Amaliadas',
    'κοροιβος': 'Koroivos Amaliadas',
    'koroivos': 'Koroivos Amaliadas',
    'τρίκαλα': 'Trikala',
    'τρικαλα': 'Trikala',
    'trikala': 'Trikala',
    'trikala aries': 'Trikala',
    'ήφαιστος λήμνου': 'Ifaistos Limnou',
    'ifaistos limnou': 'Ifaistos Limnou',
    'χολαργός': 'Holargos',
    'holargos': 'Holargos',
    'έσπερος': 'Esperos Kallitheas',
    'π.ο.κ. έσπερος': 'Esperos Kallitheas',
    'τρίτων': 'Triton Athens',
    'α.ο. τρίτων': 'Triton Athens',
    'ηλυσιακός': 'Ilisiakos',
    'ilisiakos': 'Ilisiakos',
    'δάφνη': 'Dafni',
    'dafni': 'Dafni',
    'παπάγου': 'Papagou',
    'papagou': 'Papagou',
    'νήαρ ηστ': 'Near East',
    'near east': 'Near East',
    'νίκη βόλου': 'Niki Volou',
    'μίλων': 'Milon Nea Smyrni',
    'milon': 'Milon Nea Smyrni',
    'μακεδονικός': 'Makedonikos',
    'makedonikos': 'Makedonikos',
    'καοδ': 'KAOD Drama',
    'kaod': 'KAOD Drama',
    'αρκαδικός': 'Arkadikos',
    'δόξα λευκάδας': 'Doxa Lefkadas',
    'χαρίλαος τρικούπης': 'Charilaos Trikoupis',
    'μύκονος': 'Mykonos',
    'ελευθερούπολη': 'Eleftheroupoli',
    'μεγαρίδα': 'Megarida',
}

TEAM_VENUES = {
    'Panathinaikos': ('O.A.K.A. Olympic Indoor Hall', 'Athens'),
    'Olympiacos': ('Peace and Friendship Stadium (SEF)', 'Piraeus'),
    'AEK Athens': ('Sunel Arena (Ano Liosia Olympic Hall)', 'Athens'),
    'Aris Thessaloniki': ('Alexandreio Melathron (Nick Galis Hall)', 'Thessaloniki'),
    'PAOK': ('PAOK Sports Arena (Palataki)', 'Thessaloniki'),
    'Panionios': ('Nea Smyrni Indoor Hall', 'Athens'),
    'Iraklis Thessaloniki': ('Ivanofeio Sports Arena', 'Thessaloniki'),
    'Peristeri': ('Andreas Papandreou Indoor Hall', 'Athens'),
    'Maroussi': ('Saint Thomas Indoor Hall', 'Athens'),
    'Panellinios': ('Panellinios Indoor Hall', 'Athens'),
    'Apollon Patras': ('Apollon Patras Indoor Hall', 'Patras'),
    'Ionikos Nikaias': ('Platon Indoor Hall', 'Nikaia'),
    'Sporting Athens': ('Sporting Indoor Hall', 'Athens'),
    'Promitheas Patras': ('Dimitris Tofalos Arena', 'Patras'),
    'Kolossos Rhodes': ('Kallithea Indoor Hall', 'Rhodes'),
    'Lavrio Megabolt': ('Lavrio Indoor Hall', 'Lavrio'),
    'Karditsa': ('Giannis Bourousis Indoor Arena', 'Karditsa'),
    'Dimokritos Thessaloniki': ('Thessaloniki Indoor Arena', 'Thessaloniki'),
    'VAO Thessaloniki': ('Sykies Indoor Hall', 'Thessaloniki'),
    'XANTH Thessaloniki': ('XANTH Indoor Hall', 'Thessaloniki'),
    'GS Larissas': ('Neapoli Indoor Hall', 'Larissa'),
    'Olympia Larissa': ('Neapoli Indoor Hall', 'Larissa'),
    'Rethymno Cretan Kings': ('Melina Merkouri Indoor Hall', 'Rethymno'),
    'Kymi': ('Nikos Marinis Indoor Hall', 'Kymi'),
    'Koroivos Amaliadas': ('Amaliada Indoor Hall', 'Amaliada'),
    'Trikala': ('Trikala Indoor Hall', 'Trikala'),
    'Ifaistos Limnou': ('Nikos Samaras Indoor Hall', 'Myrina (Lemnos)'),
    'Holargos': ('Antonis Tritsis Indoor Hall', 'Athens'),
    'Esperos Kallitheas': ('Esperos Indoor Hall', 'Kallithea'),
    'Triton Athens': ('Strefi Indoor Hall', 'Athens'),
    'Ilisiakos': ('Antonis Fotsis Indoor Hall', 'Athens'),
    'Dafni': ('Michalis Mouroutsos Indoor Hall', 'Athens'),
    'Papagou': ('Papagou Indoor Hall', 'Athens'),
    'Near East': ('Kaisariani Indoor Hall', 'Athens'),
    'Niki Volou': ('Nea Ionia Indoor Hall', 'Volos'),
    'Milon Nea Smyrni': ('Milon Indoor Hall', 'Athens'),
    'Makedonikos': ('Kozani Indoor Hall', 'Kozani'),
    'KAOD Drama': ('Dimitris Kratidis Indoor Hall', 'Drama'),
    'Arkadikos': ('Tripoli Indoor Hall', 'Tripoli'),
    'Doxa Lefkadas': ('Lefkada Indoor Hall', 'Lefkada'),
    'Charilaos Trikoupis': ('Mesolonghi Indoor Hall', 'Mesolonghi'),
    'Mykonos': ('Mykonos Indoor Hall', 'Mykonos'),
    'Eleftheroupoli': ('Eleftheroupoli Indoor Hall', 'Eleftheroupoli'),
    'Megarida': ('Megara Indoor Hall', 'Megara'),
}

def normalize_team_name(raw_name):
    if not raw_name:
        return "Unknown"
    # Clean brackets, links, whitespace, numbers
    clean = raw_name.replace('[[', '').replace(']]', '').strip()
    if '|' in clean:
        clean = clean.split('|')[-1].strip()
    clean = clean.replace("'''", "").replace("''", "").strip()
    clean_lower = clean.lower()
    
    if clean_lower in TEAM_MAP:
        return TEAM_MAP[clean_lower]
        
    for k, v in TEAM_MAP.items():
        if k in clean_lower or clean_lower in k:
            return v
            
    # Default fallback: title case
    return clean

def get_venue_and_city(home_team, game_type="Regular Season"):
    if "Super Cup" in game_type:
        return "Kallithea Indoor Hall", "Rhodes"
    return TEAM_VENUES.get(home_team, ("Greek National Arena", "Greece"))

def get_period_format(season_year):
    # Seasons before 2000 (i.e. <= 1999-00) played two 20-min halves
    if season_year < 2000:
        return "Two 20-minute halves (40 min)"
    else:
        return "Four 10-minute quarters (40 min)"

def get_notable_players(home_team, away_team, season_year):
    # Historical star rosters and MVPs
    if season_year < 1985:
        stars = {
            'Panathinaikos': 'Apostolos Kontos, Dimitris Kokolakis, Takis Koroneos',
            'Olympiacos': 'Steve Giatzoglou, Pavlos Diakoulas, Giorgos Kastrinakis',
            'Aris Thessaloniki': 'Nikos Galis, Haris Papageorgiou, Dionysis Ananiadis',
            'AEK Athens': 'Vassilis Goumas, Minas Gekos, Georgios Amerikanos',
            'PAOK': 'Manthos Katsoulis, Panagiotis Fasoulas, John Korfas',
            'Panionios': 'Fanis Christodoulou, Giorgos Gasparis',
            'Iraklis Thessaloniki': 'Dimitris Karatzoulidis, Lefteris Kakiousis',
            'Sporting Athens': 'Vassilis Goumas, Dimitris Vlachos',
            'Ionikos Nikaias': 'Panagiotis Giannakis (Ionikos scoring machine)',
        }
    elif season_year < 1992:
        stars = {
            'Aris Thessaloniki': 'Nikos Galis (Greek Legend), Panagiotis Giannakis, Slobodan Subotic',
            'PAOK': 'Bane Prelevic, Panagiotis Fasoulas, John Korfas, Ken Barlow',
            'Panathinaikos': 'Argiris Papapetrou, Liveris Andritsos, Memas Ioannou',
            'Olympiacos': 'Zarko Paspalj, Argyris Kambouris, Stavros Elliniadis',
            'Panionios': 'Fanis Christodoulou, Giorgos Gasparis, Chris Hudson',
            'AEK Athens': 'Minas Gekos, Nasos Galakteros, Kostas Patavoukas',
            'Iraklis Thessaloniki': 'David Ancrum, Lefteris Kakiousis',
            'Peristeri': 'Argiris Pedoulakis, Angelos Koronios',
        }
    elif season_year < 2000:
        stars = {
            'Olympiacos': 'David Rivers, Milan Tomic, Panagiotis Fasoulas, Giorgos Sigalas',
            'Panathinaikos': 'Dominique Wilkins, Dino Radja, Dejan Bodiroga, Fragiskos Alvertis',
            'PAOK': 'Peja Stojakovic, Bane Prelevic, Walter Berry, Scott Skiles',
            'AEK Athens': 'Victor Alexander, Claudio Coldebella, Willie Anderson',
            'Aris Thessaloniki': 'Jose Ortiz, Mario Boni, Charles Shackleford',
            'Panionios': 'P.J. Brown, Travis Mays, Jure Zdovc',
            'Iraklis Thessaloniki': 'Walter Berry, Xavier McDaniel, Jure Zdovc',
            'Peristeri': 'Marko Jaric, Milan Gurovic, Angelos Koronios',
        }
    elif season_year < 2010:
        stars = {
            'Panathinaikos': 'Dimitris Diamantidis, Vassilis Spanoulis, Mike Batiste, Fragiskos Alvertis, Sarunas Jasikevicius',
            'Olympiacos': 'Vassilis Spanoulis, Milos Teodosic, Ioannis Bourousis, Theodoros Papaloukas, Linas Kleiza',
            'AEK Athens': 'Nikos Zisis, Dusan Sakota, J.R. Holden, Michalis Kakiouzis',
            'Aris Thessaloniki': 'Will Solomon, Jeremiah Massey, Nikolai Padius',
            'PAOK': 'Damir Mulaomerovic, Kostas Vasileiadis, Loukas Mavrokefalidis',
            'Panionios': 'Brad Newley, Lonny Baxter, Dimos Dikoudis',
            'Maroussi': 'Vassilis Spanoulis, Roderick Blakney, Pat Calathes, Kostas Kaimakoglou',
            'Peristeri': 'Alfonso Ford (Euroleague Scoring Machine), Pete Mickeal',
        }
    elif season_year < 2020:
        stars = {
            'Panathinaikos': 'Nick Calathes, Dimitris Diamantidis, James Gist, Mike James, Chris Singleton',
            'Olympiacos': 'Vassilis Spanoulis (All-Time Legend), Georgios Printezis, Kostas Sloukas, Matt Lojeski',
            'AEK Athens': 'Manny Harris, Keith Langford, Mike Green, Dusan Sakota',
            'PAOK': 'Kevin Langford, Apollon Tsolakis, Vangelis Margaritis',
            'Aris Thessaloniki': 'Sasha Vezenkov (MVP), Okaro White, Vassilis Symtsak',
            'Promitheas Patras': 'Langston Hall, Jerian Grant, Chris Babb',
            'Peristeri': 'Steven Gray, Vassilis Xanthopoulos',
            'Rethymno Cretan Kings': 'Brent Petway, Roeland Schaftenaar',
        }
    else:
        stars = {
            'Panathinaikos': 'Kendrick Nunn, Kostas Sloukas (Finals MVP), Mathias Lessort, Jerian Grant, Dinos Mitoglou',
            'Olympiacos': 'Sasha Vezenkov (Euroleague MVP), Thomas Walkup, Alec Peters, Kostas Papanikolaou, Nigel Williams-Goss',
            'AEK Athens': 'Mindaugas Kuzminskas, Jordan McRae, Chasson Randle',
            'Peristeri': 'Joe Ragland, Trevor Thompson, Elijah Mitrou-Long',
            'Promitheas Patras': 'Anthony Cowan Jr., Hunter Hale, Jaime Echenique',
            'Aris Thessaloniki': 'Vassilis Toliopoulos, Roberto Gallinat, Ronnie Harrell',
            'PAOK': 'Kevin Porter Jr., Elvar Fridriksson, Justin Alston',
            'Kolossos Rhodes': 'Luka Brajkovic, Andrew Goudelock',
            'Maroussi': 'Miroslav Raduljica, Isaiah Briscoe, Ahmed Hill',
            'Karditsa': 'Rayvonte Rice, Tevin Mack, Nikos Diplaros',
            'Lavrio Megabolt': 'Xavier Castaneda, David DeJulius',
            'Apollon Patras': 'Malik Osborne, Chad Brown',
        }
        
    h_s = stars.get(home_team, f"{home_team} key players")
    a_s = stars.get(away_team, f"{away_team} key players")
    return f"{home_team}: {h_s}; {away_team}: {a_s}"
