import os
import sys
import json
import zipfile
import random
import re
import datetime
import cvxpy as cp
import pandas as pd
from collections import defaultdict

# Set random seed for reproducibility
random.seed(42)

ALL_COUNTIES = [
    'Derbyshire', 'Durham', 'Essex', 'Glamorgan', 'Gloucestershire',
    'Hampshire', 'Kent', 'Lancashire', 'Leicestershire', 'Middlesex',
    'Northamptonshire', 'Nottinghamshire', 'Somerset', 'Surrey',
    'Sussex', 'Warwickshire', 'Worcestershire', 'Yorkshire'
]

COUNTY_VENUES = {
    'Derbyshire': [('County Ground, Derby', 'Derby'), ("Queen's Park, Chesterfield", 'Chesterfield')],
    'Durham': [('Riverside Ground, Chester-le-Street', 'Chester-le-Street'), ('Racecourse Ground, Durham', 'Durham')],
    'Essex': [('County Ground, Chelmsford', 'Chelmsford'), ('Castle Park Cricket Ground, Colchester', 'Colchester'), ('Garon Park, Southend-on-Sea', 'Southend-on-Sea')],
    'Glamorgan': [('Sophia Gardens, Cardiff', 'Cardiff'), ("St Helen's, Swansea", 'Swansea'), ('Penrhyn Avenue, Colwyn Bay', 'Colwyn Bay')],
    'Gloucestershire': [('County Ground, Bristol', 'Bristol'), ('College Ground, Cheltenham', 'Cheltenham')],
    'Hampshire': [('The Rose Bowl, Southampton', 'Southampton'), ('County Ground, Northlands Road, Southampton', 'Southampton'), ("May's Bounty, Basingstoke", 'Basingstoke')],
    'Kent': [('St Lawrence Ground, Canterbury', 'Canterbury'), ('Nevill Ground, Royal Tunbridge Wells', 'Royal Tunbridge Wells'), ('Crabble Athletic Ground, Dover', 'Dover')],
    'Lancashire': [('Old Trafford, Manchester', 'Manchester'), ('Stanley Park, Blackpool', 'Blackpool'), ('Trafalgar Road, Southport', 'Southport')],
    'Leicestershire': [('Grace Road, Leicester', 'Leicester')],
    'Middlesex': [("Lord's Cricket Ground, London", 'London'), ('Uxbridge Cricket Club Ground, Uxbridge', 'Uxbridge')],
    'Northamptonshire': [('County Ground, Northampton', 'Northampton')],
    'Nottinghamshire': [('Trent Bridge, Nottingham', 'Nottingham')],
    'Somerset': [('County Ground, Taunton', 'Taunton'), ('Recreation Ground, Bath', 'Bath')],
    'Surrey': [('The Oval, Kennington, London', 'London'), ('Woodbridge Road, Guildford', 'Guildford')],
    'Sussex': [('County Ground, Hove', 'Hove'), ('Arundel Castle Cricket Ground, Arundel', 'Arundel')],
    'Warwickshire': [('Edgbaston, Birmingham', 'Birmingham')],
    'Worcestershire': [('New Road, Worcester', 'Worcester')],
    'Yorkshire': [('Headingley, Leeds', 'Leeds'), ('North Marine Road Ground, Scarborough', 'Scarborough'), ('Abbeydale Park, Sheffield', 'Sheffield')]
}

ERA_PLAYERS = {
    '70s': {
        'Derbyshire': [('E Barlow', 74, 2), ('M Hendrick', 25, 4), ('A Hill', 82, 0), ('RW Taylor', 45, 0), ('PE Kirsten', 95, 1)],
        'Essex': [('GA Gooch', 114, 1), ('KWR Fletcher', 88, 0), ('JK Lever', 32, 5), ('RE East', 18, 4), ('KS McEwan', 102, 0)],
        'Glamorgan': [('Majid Khan', 105, 2), ('A Jones', 78, 0), ('M Nash', 35, 4), ('DJ Shepherd', 15, 3), ('AE Cordle', 24, 3)],
        'Gloucestershire': [('MJ Procter', 85, 5), ('Zaheer Abbas', 130, 1), ('DA Graveney', 40, 3), ('JB Mortimore', 30, 3), ('AS Brown', 55, 0)],
        'Hampshire': [('BA Richards', 125, 1), ('CG Greenidge', 110, 0), ('RMH Cottam', 15, 4), ('TE Jesty', 68, 2), ('RVC Gilliat', 52, 0)],
        'Kent': [('MC Cowdrey', 75, 0), ('DL Underwood', 20, 6), ('APE Knott', 65, 0), ('RA Woolmer', 84, 2), ('Asif Iqbal', 92, 2)],
        'Lancashire': [('CH Lloyd', 118, 1), ('FM Hayes', 80, 0), ('P Lee', 12, 5), ('J Simmons', 45, 3), ('DP Hughes', 62, 2)],
        'Leicestershire': [('R Illingworth', 45, 4), ('JC Balderstone', 88, 1), ('BF Davison', 96, 0), ('K Higgs', 15, 4), ('P Booth', 25, 3)],
        'Middlesex': [('M Brearley', 82, 0), ('CT Radley', 104, 0), ('JE Emburey', 42, 4), ('FJ Titmus', 38, 3), ('MWW Selvey', 18, 4)],
        'Northamptonshire': [('Mushtaq Mohammad', 112, 3), ('BS Bedi', 15, 5), ('P Willey', 85, 2), ('G Sharp', 70, 0), ('Sarfraz Nawaz', 30, 4)],
        'Nottinghamshire': [('GS Sobers', 95, 3), ('CEB Rice', 88, 4), ('DW Randall', 92, 0), ('SB Hassan', 75, 1), ('M Hendrick', 15, 3)],
        'Somerset': [('IV Richards', 128, 1), ('IT Botham', 94, 5), ('DB Close', 55, 1), ('J Garner', 18, 5), ('PW Denning', 72, 0)],
        'Surrey': [('JH Edrich', 105, 0), ('GP Howarth', 82, 1), ('RD Jackman', 22, 5), ('Intikhab Alam', 45, 3), ('PI Pocock', 15, 4)],
        'Sussex': [('AW Greig', 92, 3), ('JA Snow', 20, 5), ('Imran Khan', 85, 4), ('PWG Parker', 78, 0), ('IJ Gould', 54, 0)],
        'Warwickshire': [('RB Kanhai', 115, 0), ('DL Amiss', 120, 0), ('RGD Willis', 14, 5), ('DJ Brown', 35, 3), ('JA Jameson', 76, 1)],
        'Worcestershire': [('GM Turner', 135, 0), ('N Gifford', 22, 4), ('VA Holder', 28, 4), ('JA Ormrod', 68, 0), ('EJ D\'Oliveira', 55, 2)],
        'Yorkshire': [('G Boycott', 132, 0), ('JH Hampshire', 84, 0), ('CM Old', 42, 4), ('A Sidebottom', 18, 4), ('DL Bairstow', 65, 0)]
    },
    '80s': {
        'Derbyshire': [('JG Wright', 108, 0), ('KJ Barnett', 94, 1), ('MA Holding', 22, 5), ('DG Cork', 45, 4), ('OH Mortensen', 15, 4)],
        'Essex': [('GA Gooch', 142, 1), ('AR Border', 115, 1), ('DR Pringle', 65, 3), ('NA Foster', 25, 5), ('PJ Prichard', 78, 0)],
        'Glamorgan': [('MD Maynard', 98, 0), ('H Morris', 85, 0), ('RC Ontong', 55, 3), ('SP Watkin', 18, 4), ('GC Holmes', 72, 0)],
        'Gloucestershire': [('CA Walsh', 15, 6), ('DA Graveney', 45, 3), ('CWJ Athey', 88, 0), ('P Bainbridge', 62, 2), ('KM Curran', 74, 3)],
        'Hampshire': [('MD Marshall', 35, 6), ('CG Greenidge', 118, 0), ('DI Gower', 105, 0), ('MCJ Nicholas', 72, 0), ('CA Connor', 20, 4)],
        'Kent': [('CS Cowdrey', 82, 0), ('GR Dilley', 25, 5), ('NR Taylor', 90, 0), ('RM Ellison', 42, 4), ('MR Benson', 78, 0)],
        'Lancashire': [('CH Lloyd', 95, 0), ('NH Fairbrother', 88, 0), ('Wasim Akram', 45, 5), ('PJW Allott', 22, 4), ('ID Austin', 35, 3)],
        'Leicestershire': [('DI Gower', 125, 0), ('P Willey', 82, 3), ('NE Briers', 75, 0), ('LES Taylor', 12, 5), ('J Agnew', 18, 4)],
        'Middlesex': [('MW Gatting', 120, 1), ('DL Haynes', 112, 0), ('JE Emburey', 45, 4), ('PH Edmonds', 28, 4), ('WW Daniel', 15, 5)],
        'Northamptonshire': [('AJ Lamb', 115, 0), ('Kapil Dev', 75, 4), ('W Larkins', 98, 0), ('DJ Capel', 62, 3), ('NGB Cook', 18, 4)],
        'Nottinghamshire': [('CEB Rice', 92, 4), ('RJ Hadlee', 55, 6), ('DW Randall', 85, 0), ('BC Broad', 104, 0), ('BN French', 45, 0)],
        'Somerset': [('IV Richards', 135, 1), ('IT Botham', 88, 4), ('PM Roebuck', 78, 0), ('VJ Marks', 52, 3), ('J Garner', 15, 5)],
        'Surrey': [('ST Clarke', 18, 6), ('MA Lynch', 85, 0), ('AJ Stewart', 94, 0), ('GP Thorpe', 82, 0), ('MP Bicknell', 25, 4)],
        'Sussex': [('Imran Khan', 92, 5), ('PWG Parker', 76, 0), ('CM Wells', 84, 2), ('AM Pigott', 20, 4), ('GGD Gould', 58, 0)],
        'Warwickshire': [('AI Kallicharran', 122, 0), ('DL Amiss', 95, 0), ('GC Small', 22, 5), ('DA Reeve', 65, 3), ('TA Munton', 18, 4)],
        'Worcestershire': [('GA Hick', 145, 1), ('IT Botham', 82, 3), ('PA Neale', 75, 0), ('NV Radford', 20, 5), ('RK Illingworth', 38, 3)],
        'Yorkshire': [('G Boycott', 115, 0), ('MD Moxon', 96, 0), ('AA Metcalfe', 74, 0), ('A Sidebottom', 22, 4), ('PE Carrick', 35, 3)]
    },
    '90s': {
        'Derbyshire': [('DG Cork', 65, 5), ('M Azharuddin', 125, 0), ('CJ Adams', 88, 0), ('DE Malcolm', 15, 5), ('KM Barnett', 82, 0)],
        'Durham': [('DC Boon', 105, 0), ('PD Collingwood', 78, 2), ('S Brown', 18, 5), ('J Morris', 84, 0), ('MM Betts', 22, 4)],
        'Essex': [('GA Gooch', 118, 0), ('N Hussain', 92, 0), ('RC Irani', 72, 3), ('ME Waugh', 110, 1), ('PM Such', 15, 4)],
        'Glamorgan': [('MD Maynard', 112, 0), ('H Morris', 88, 0), ('RDB Croft', 58, 4), ('SP Watkin', 20, 5), ('Waqar Younis', 18, 5)],
        'Gloucestershire': [('CA Walsh', 16, 6), ('RC Russell', 68, 0), ('MW Alleyne', 74, 3), ('THC Hancock', 82, 0), ('J Lewis', 24, 4)],
        'Hampshire': [('RA Smith', 104, 0), ('ML Hayden', 115, 0), ('SD Udal', 45, 3), ('KD James', 62, 3), ('CA Connor', 18, 4)],
        'Kent': [('SA Marsh', 58, 0), ('MA Ealham', 72, 4), ('MJ McCague', 18, 5), ('MV Fleming', 65, 3), ('TR Ward', 94, 0)],
        'Lancashire': [('Wasim Akram', 55, 6), ('MA Atherton', 102, 0), ('NH Fairbrother', 88, 0), ('G Chapple', 48, 4), ('WK Hegg', 52, 0)],
        'Leicestershire': [('J Whitaker', 85, 0), ('VJ Wells', 78, 3), ('PV Simmons', 92, 3), ('AD Mullally', 14, 5), ('CC Lewis', 62, 4)],
        'Middlesex': [('MR Ramprakash', 128, 0), ('MW Gatting', 85, 0), ('AR Fraser', 15, 5), ('PCR Tufnell', 12, 5), ('RL Johnson', 32, 4)],
        'Northamptonshire': [('AJ Lamb', 98, 0), ('CEL Ambrose', 20, 6), ('RJ Bailey', 84, 0), ('JP Taylor', 18, 4), ('A Kumble', 35, 5)],
        'Nottinghamshire': [('CL Cairns', 82, 4), ('P Johnson', 88, 0), ('RT Robinson', 94, 0), ('AP Pick', 22, 4), ('MN Bowen', 18, 4)],
        'Somerset': [('ME Trescothick', 108, 0), ('Mushtaq Ahmed', 35, 6), ('RJ Harden', 78, 0), ('AR Caddick', 18, 5), ('GD Rose', 58, 3)],
        'Surrey': [('AJ Stewart', 112, 0), ('GP Thorpe', 105, 0), ('MP Bicknell', 35, 5), ('Saqlain Mushtaq', 25, 6), ('AD Hollioake', 68, 2)],
        'Sussex': [('AP Wells', 92, 0), ('VC Drakes', 42, 5), ('K Greenfield', 65, 0), ('CWJ Athey', 75, 0), ('PW Jarvis', 18, 4)],
        'Warwickshire': [('BC Lara', 155, 0), ('DA Reeve', 62, 3), ('AA Donald', 18, 6), ('NV Knight', 98, 0), ('SM Pollock', 65, 4)],
        'Worcestershire': [('GA Hick', 138, 1), ('TM Moody', 105, 2), ('VS Solanki', 82, 0), ('RK Illingworth', 42, 3), ('SR Lampitt', 32, 4)],
        'Yorkshire': [('MD Moxon', 84, 0), ('D Gough', 35, 5), ('MG Bevan', 115, 1), ('C White', 72, 3), ('CEW Silverwood', 20, 5)]
    },
    '00s': {
        'Derbyshire': [('MJ Di Venuto', 118, 0), ('DG Cork', 58, 4), ('SD Stubbings', 76, 0), ('KJ Dean', 15, 4), ('G Welch', 45, 3)],
        'Durham': [('PD Collingwood', 95, 2), ('MJ Di Venuto', 110, 0), ('SJ Harmison', 18, 5), ('DM Benkenstein', 88, 0), ('G Onions', 15, 5)],
        'Essex': [('AN Cook', 125, 0), ('RC Irani', 78, 2), ('JS Foster', 68, 0), ('Danish Kaneria', 20, 6), ('GR Napier', 48, 3)],
        'Glamorgan': [('RDB Croft', 52, 3), ('MD Maynard', 92, 0), ('MJ Powell', 84, 0), ('DS Harrison', 18, 4), ('MS Kasprowicz', 25, 5)],
        'Gloucestershire': [('RC Russell', 62, 0), ('CM Spearman', 105, 0), ('J Lewis', 22, 5), ('MW Alleyne', 68, 2), ('JMM Averis', 18, 4)],
        'Hampshire': [('SK Warne', 48, 5), ('JP Crawley', 108, 0), ('AD Mascarenhas', 65, 3), ('CT Tremlett', 25, 4), ('N Pothas', 62, 0)],
        'Kent': [('RWT Key', 104, 0), ('M van Jaarsveld', 96, 0), ('JC Tredwell', 42, 3), ('Amjad Khan', 18, 4), ('GO Jones', 68, 0)],
        'Lancashire': [('SG Law', 102, 1), ('MB Loye', 84, 0), ('G Chapple', 55, 4), ('JM Anderson', 15, 5), ('DG Cork', 48, 3)],
        'Leicestershire': [('BJ Hodge', 115, 1), ('DL Maddy', 88, 2), ('PA Nixon', 64, 0), ('SCJ Broad', 38, 4), ('CW Henderson', 18, 4)],
        'Middlesex': [('AJ Strauss', 112, 0), ('EC Joyce', 95, 0), ('OA Shah', 88, 0), ('SD Udal', 42, 3), ('TJ Murtagh', 20, 4)],
        'Northamptonshire': [('DJ Sales', 105, 0), ('MS Panesar', 15, 5), ('JF Brown', 25, 4), ('U Afzaal', 82, 0), ('JJ van der Wath', 48, 3)],
        'Nottinghamshire': [('SP Fleming', 110, 0), ('KP Pietersen', 122, 1), ('SCJ Broad', 42, 4), ('RJ Sidebottom', 18, 5), ('CMW Read', 68, 0)],
        'Somerset': [('ME Trescothick', 120, 0), ('JL Langer', 118, 0), ('AR Caddick', 18, 5), ('C Willoughby', 15, 5), ('JC Hildreth', 92, 0)],
        'Surrey': [('MR Ramprakash', 135, 0), ('MA Butcher', 98, 0), ('MP Bicknell', 35, 4), ('Saqlain Mushtaq', 20, 5), ('IDK Salisbury', 25, 3)],
        'Sussex': [('CJ Adams', 95, 0), ('MW Goodwin', 115, 0), ('Mushtaq Ahmed', 22, 6), ('RJ Kirtley', 20, 4), ('MJ Prior', 78, 0)],
        'Warwickshire': [('IR Bell', 115, 0), ('NV Knight', 88, 0), ('DR Brown', 55, 3), ('AF Giles', 42, 3), ('HH Streak', 45, 4)],
        'Worcestershire': [('VS Solanki', 98, 0), ('GA Hick', 112, 0), ('Kabir Ali', 28, 5), ('GJ Batty', 45, 3), ('DKH Mitchell', 75, 0)],
        'Yorkshire': [('MP Vaughan', 105, 0), ('A McGrath', 84, 2), ('MJ Hoggard', 15, 5), ('D Gough', 22, 4), ('JA Rudolph', 108, 0)]
    },
    '10s': {
        'Derbyshire': [('WL Madsen', 108, 0), ('BA Godleman', 82, 0), ('AP Palladino', 22, 4), ('MHA Footbitt', 15, 5), ('AL Hughes', 55, 2)],
        'Durham': [('SG Borthwick', 88, 2), ('KK Jennings', 105, 0), ('G Onions', 15, 5), ('C Rushworth', 18, 5), ('BA Stokes', 92, 3)],
        'Essex': [('AN Cook', 115, 0), ('T Westley', 85, 0), ('JA Porter', 18, 5), ('SR Harmer', 35, 5), ('RS Bopara', 72, 2)],
        'Glamorgan': [('JA Rudolph', 98, 0), ('CA Ingram', 85, 1), ('MG Hogan', 15, 4), ('GG Wagg', 55, 3), ('CB Cooke', 68, 0)],
        'Gloucestershire': [('M Klinger', 112, 0), ('CD Dent', 84, 0), ('DA Payne', 20, 4), ('LC Norwell', 18, 5), ('HJH Marshall', 78, 0)],
        'Hampshire': [('JM Vince', 104, 0), ('LA Dawson', 65, 3), ('KJ Abbott', 22, 5), ('FH Edwards', 15, 4), ('MA Carberry', 88, 0)],
        'Kent': [('SW Billings', 78, 0), ('JL Denly', 94, 1), ('MT Coles', 45, 4), ('DI Stevens', 82, 4), ('DB Drummond', 88, 0)],
        'Lancashire': [('SJ Croft', 78, 1), ('KK Jennings', 98, 0), ('JM Anderson', 12, 5), ('TE Bailey', 25, 4), ('Haseeb Hameed', 85, 0)],
        'Leicestershire': [('ML Cosgrove', 95, 0), ('CN Ackermann', 88, 1), ('BA Raine', 55, 4), ('CJ McKay', 18, 4), ('NJ Eckersley', 68, 0)],
        'Middlesex': [('SD Robson', 105, 0), ('DJ Malan', 95, 0), ('TR Roland-Jones', 28, 5), ('TJ Murtagh', 18, 5), ('ST Finn', 15, 4)],
        'Northamptonshire': [('AM Wakely', 82, 0), ('BM Duckett', 115, 0), ('RR Gleeson', 18, 4), ('RI Keogh', 65, 2), ('RK Kleinveldt', 42, 3)],
        'Nottinghamshire': [('AD Hales', 108, 0), ('JL Pattinson', 28, 5), ('SR Patel', 75, 3), ('LJ Fletcher', 22, 4), ('JT Ball', 18, 4)],
        'Somerset': [('ME Trescothick', 98, 0), ('JC Hildreth', 102, 0), ('MJ Leach', 18, 5), ('L Gregory', 55, 4), ('CO Overton', 45, 4)],
        'Surrey': [('RJ Burns', 110, 0), ('OJ Pope', 115, 0), ('SM Curran', 65, 3), ('TK Curran', 42, 3), ('A Virdi', 20, 4)],
        'Sussex': [('EC Joyce', 105, 0), ('LJ Wright', 85, 1), ('CJ Jordan', 55, 3), ('JC Archer', 25, 5), ('SJ Magoffin', 18, 5)],
        'Warwickshire': [('IR Bell', 105, 0), ('IJL Trott', 98, 0), ('CR Woakes', 65, 4), ('JS Patel', 35, 5), ('KMD Barker', 45, 3)],
        'Worcestershire': [('DKH Mitchell', 95, 0), ('MM Ali', 92, 3), ('J Leach', 35, 4), ('BL D\'Oliveira', 75, 1), ('CA Morris', 18, 4)],
        'Yorkshire': [('JE Root', 118, 1), ('JM Bairstow', 108, 0), ('GS Ballance', 95, 0), ('JA Brooks', 22, 4), ('BO Coad', 18, 5)]
    }
}

UMPIRES_BY_ERA = {
    '70s': ['HD Bird', 'DJ Shepherd', 'D Oslear', 'B Meyer', 'AG Whitehead', 'G Sharp', 'R Palmer', 'MW Kitchen', 'R Julian', 'JW Holder', 'K Palmer'],
    '80s': ['HD Bird', 'DJ Shepherd', 'D Oslear', 'B Meyer', 'AG Whitehead', 'G Sharp', 'R Palmer', 'MW Kitchen', 'R Julian', 'JW Holder', 'P Willey'],
    '90s': ['P Willey', 'JH Hampshire', 'NJ Cowley', 'JH Emburey', 'TE Jesty', 'VA Holder', 'MJ Kitchen', 'G Sharp', 'JW Holder', 'IJ Gould', 'B Dudleston'],
    '00s': ['P Willey', 'JH Hampshire', 'JW Lloyds', 'PJ Hartley', 'MJ Kitchen', 'G Sharp', 'NA Mallender', 'IJ Gould', 'RK Illingworth', 'RA Kettleborough', 'MJC Gough'],
    '10s': ['RA Kettleborough', 'MJC Gough', 'AG Wharf', 'RK Illingworth', 'RT Robinson', 'RJ Bailey', 'MA Gough', 'DJ Millns', 'NGB Cook', 'MJ Saggers', 'PK Pollard', 'ID Blackwell']
}

def get_era_key(year):
    if year < 1980: return '70s'
    if year < 1990: return '80s'
    if year < 2000: return '90s'
    if year < 2010: return '00s'
    return '10s'

def generate_notable_players(team1, team2, era_key):
    p1_list = ERA_PLAYERS.get(era_key, {}).get(team1, [])
    p2_list = ERA_PLAYERS.get(era_key, {}).get(team2, [])
    
    parts = []
    if p1_list:
        sample1 = random.sample(p1_list, min(2, len(p1_list)))
        desc1 = [f"{p[0]} {p[1]}" if p[2] == 0 else f"{p[0]} {p[1]} & {p[2]} wkts" for p in sample1]
        parts.append(f"{team1}: {', '.join(desc1)}")
    if p2_list:
        sample2 = random.sample(p2_list, min(2, len(p2_list)))
        desc2 = [f"{p[0]} {p[1]}" if p[2] == 0 else f"{p[0]} {p[1]} & {p[2]} wkts" for p in sample2]
        parts.append(f"{team2}: {', '.join(desc2)}")
    return ' | '.join(parts)

def generate_match_scores(winner, loser, result, team_bat_first, team_bat_second):
    # Generates multi-day scores consistent with the outcome
    inn1_team = team_bat_first
    inn2_team = team_bat_second
    
    if result == 'Win':
        # Types of win:
        # 1: innings and runs (~25%)
        # 2: wickets (~45%)
        # 3: runs (~30%)
        roll = random.random()
        
        if roll < 0.25:
            # Innings win
            margin_val = random.randint(15, 110)
            margin_type = 'innings and runs'
            winning_margin = f"innings and {margin_val} runs"
            follow_on = 'Yes'
            
            if winner == inn1_team:
                inn1_runs = random.randint(380, 520)
                inn1_wkts = random.randint(5, 9)
                inn1_dec = 'd'
                inn1_ov = f"{random.randint(110, 145)}.{random.randint(0, 5)} ov"
                
                # Loser batted 2nd and 3rd
                inn2_runs = (inn1_runs - margin_val) // 2
                inn2_wkts = 10
                inn2_ov = f"{random.randint(55, 80)}.{random.randint(0, 5)} ov"
                
                inn3_team = loser
                inn3_runs = (inn1_runs - margin_val) - inn2_runs
                inn3_wkts = 10
                inn3_ov = f"{random.randint(55, 85)}.{random.randint(0, 5)} ov"
                
                inn4_team = ''
                inn4_score = ''
                inn4_runs = ''
                inn4_wkts = ''
                inn4_ov = ''
            else:
                # Winner batted 2nd
                inn1_runs = random.randint(140, 220)
                inn1_wkts = 10
                inn1_dec = ''
                inn1_ov = f"{random.randint(50, 75)}.{random.randint(0, 5)} ov"
                
                inn2_runs = inn1_runs + margin_val + random.randint(140, 220)
                inn2_wkts = random.randint(7, 10)
                inn2_dec = 'd' if inn2_wkts < 10 else ''
                inn2_ov = f"{random.randint(110, 140)}.{random.randint(0, 5)} ov"
                
                inn3_team = loser
                inn3_runs = inn2_runs - inn1_runs - margin_val
                inn3_wkts = 10
                inn3_ov = f"{random.randint(50, 75)}.{random.randint(0, 5)} ov"
                
                inn4_team = ''
                inn4_score = ''
                inn4_runs = ''
                inn4_wkts = ''
                inn4_ov = ''
                
            inn1_score = f"{inn1_runs}/{inn1_wkts}{inn1_dec} ({inn1_ov})"
            inn2_score = f"{inn2_runs}/{inn2_wkts} ({inn2_ov})"
            inn3_score = f"{inn3_runs}/{inn3_wkts} ({inn3_ov})"
            
            total_runs = inn1_runs + inn2_runs + inn3_runs
            total_wkts = inn1_wkts + inn2_wkts + inn3_wkts
            match_score = f"{inn1_team} {inn1_runs}/{inn1_wkts}{inn1_dec} - {inn2_team} {inn2_runs} & {inn3_runs}" if winner == inn1_team else f"{inn1_team} {inn1_runs} & {inn3_runs} - {inn2_team} {inn2_runs}/{inn2_wkts}{inn2_dec}"
            
        elif roll < 0.70:
            # Win by wickets (chasing team wins in 4th innings)
            wkts_left = random.randint(2, 9)
            margin_val = wkts_left
            margin_type = 'wickets'
            winning_margin = f"{wkts_left} wickets"
            follow_on = 'No'
            
            inn1_runs = random.randint(220, 360)
            inn1_wkts = 10
            inn1_ov = f"{random.randint(75, 105)}.{random.randint(0, 5)} ov"
            inn1_score = f"{inn1_runs}/{inn1_wkts} ({inn1_ov})"
            
            lead1 = random.randint(-40, 60)
            inn2_runs = inn1_runs + lead1
            inn2_wkts = 10
            inn2_ov = f"{random.randint(75, 110)}.{random.randint(0, 5)} ov"
            inn2_score = f"{inn2_runs}/{inn2_wkts} ({inn2_ov})"
            
            # Winner is inn2_team (chasing team in 4th innings)
            if winner == inn2_team:
                inn3_team = inn1_team
                inn3_runs = random.randint(160, 280)
                inn3_wkts = 10
                inn3_ov = f"{random.randint(60, 95)}.{random.randint(0, 5)} ov"
                inn3_score = f"{inn3_runs}/{inn3_wkts} ({inn3_ov})"
                
                target = (inn1_runs + inn3_runs) - inn2_runs + 1
                inn4_team = inn2_team
                inn4_runs = target + random.randint(0, 3)
                inn4_wkts = 10 - wkts_left
                inn4_ov = f"{random.randint(40, 80)}.{random.randint(0, 5)} ov"
                inn4_score = f"{inn4_runs}/{inn4_wkts} ({inn4_ov})"
            else:
                # Winner is inn1_team (batted 1st, won by wickets after follow on or declaration)
                inn3_team = inn1_team
                inn3_runs = random.randint(180, 260)
                inn3_wkts = random.randint(4, 7)
                inn3_ov = f"{random.randint(55, 75)}.0 ov"
                inn3_score = f"{inn3_runs}/{inn3_wkts}d ({inn3_ov})"
                
                inn4_team = inn2_team
                inn4_runs = random.randint(140, 200)
                inn4_wkts = 10
                inn4_ov = f"{random.randint(50, 75)}.{random.randint(0, 5)} ov"
                inn4_score = f"{inn4_runs}/{inn4_wkts} ({inn4_ov})"
                winning_margin = f"{random.randint(25, 95)} runs"
                margin_val = int(winning_margin.split(' ')[0])
                margin_type = 'runs'
                
            total_runs = inn1_runs + inn2_runs + inn3_runs + inn4_runs
            total_wkts = inn1_wkts + inn2_wkts + inn3_wkts + inn4_wkts
            match_score = f"{inn1_team} {inn1_runs} & {inn3_runs} - {inn2_team} {inn2_runs} & {inn4_runs}/{inn4_wkts}"
            
        else:
            # Win by runs (defending team wins in 4th innings)
            margin_val = random.randint(18, 145)
            margin_type = 'runs'
            winning_margin = f"{margin_val} runs"
            follow_on = 'No'
            
            inn1_runs = random.randint(250, 380)
            inn1_wkts = 10
            inn1_ov = f"{random.randint(80, 110)}.{random.randint(0, 5)} ov"
            inn1_score = f"{inn1_runs}/{inn1_wkts} ({inn1_ov})"
            
            inn2_runs = random.randint(200, 340)
            inn2_wkts = 10
            inn2_ov = f"{random.randint(70, 100)}.{random.randint(0, 5)} ov"
            inn2_score = f"{inn2_runs}/{inn2_wkts} ({inn2_ov})"
            
            inn3_team = inn1_team
            inn3_runs = random.randint(180, 280)
            inn3_wkts = random.randint(5, 10)
            dec_str = 'd' if inn3_wkts < 10 else ''
            inn3_ov = f"{random.randint(55, 85)}.{random.randint(0, 5)} ov"
            inn3_score = f"{inn3_runs}/{inn3_wkts}{dec_str} ({inn3_ov})"
            
            target = (inn1_runs + inn3_runs) - inn2_runs + 1
            inn4_team = inn2_team
            inn4_runs = target - margin_val
            inn4_wkts = 10
            inn4_ov = f"{random.randint(50, 85)}.{random.randint(0, 5)} ov"
            inn4_score = f"{inn4_runs}/{inn4_wkts} ({inn4_ov})"
            
            total_runs = inn1_runs + inn2_runs + inn3_runs + inn4_runs
            total_wkts = inn1_wkts + inn2_wkts + inn3_wkts + inn4_wkts
            match_score = f"{inn1_team} {inn1_runs} & {inn3_runs}{dec_str} - {inn2_team} {inn2_runs} & {inn4_runs}"
            
    else:
        # Draw
        winning_margin = 'Draw'
        margin_val = ''
        margin_type = 'draw'
        follow_on = 'No'
        
        inn1_runs = random.randint(310, 460)
        inn1_wkts = random.randint(6, 10)
        inn1_dec = 'd' if inn1_wkts < 10 else ''
        inn1_ov = f"{random.randint(95, 130)}.{random.randint(0, 5)} ov"
        inn1_score = f"{inn1_runs}/{inn1_wkts}{inn1_dec} ({inn1_ov})"
        
        inn2_runs = random.randint(280, 420)
        inn2_wkts = random.randint(7, 10)
        inn2_dec = 'd' if inn2_wkts < 10 and inn2_runs > inn1_runs else ''
        inn2_ov = f"{random.randint(90, 125)}.{random.randint(0, 5)} ov"
        inn2_score = f"{inn2_runs}/{inn2_wkts}{inn2_dec} ({inn2_ov})"
        
        inn3_team = inn1_team
        inn3_runs = random.randint(180, 290)
        inn3_wkts = random.randint(3, 8)
        inn3_dec = 'd' if inn3_wkts < 8 else ''
        inn3_ov = f"{random.randint(50, 85)}.{random.randint(0, 5)} ov"
        inn3_score = f"{inn3_runs}/{inn3_wkts}{inn3_dec} ({inn3_ov})"
        
        # 4th innings ended before completion
        inn4_team = inn2_team
        inn4_runs = random.randint(130, 240)
        inn4_wkts = random.randint(3, 8)
        inn4_ov = f"{random.randint(40, 75)}.{random.randint(0, 5)} ov"
        inn4_score = f"{inn4_runs}/{inn4_wkts} ({inn4_ov})"
        
        total_runs = inn1_runs + inn2_runs + inn3_runs + inn4_runs
        total_wkts = inn1_wkts + inn2_wkts + inn3_wkts + inn4_wkts
        match_score = f"{inn1_team} {inn1_runs}/{inn1_wkts}{inn1_dec} & {inn3_runs}/{inn3_wkts}{inn3_dec} - {inn2_team} {inn2_runs}/{inn2_wkts}{inn2_dec} & {inn4_runs}/{inn4_wkts}"

    return {
        'inn1_team': inn1_team, 'inn1_score': inn1_score, 'inn1_runs': inn1_runs, 'inn1_wkts': inn1_wkts, 'inn1_ov': inn1_ov,
        'inn2_team': inn2_team, 'inn2_score': inn2_score, 'inn2_runs': inn2_runs, 'inn2_wkts': inn2_wkts, 'inn2_ov': inn2_ov,
        'inn3_team': inn3_team, 'inn3_score': inn3_score, 'inn3_runs': inn3_runs, 'inn3_wkts': inn3_wkts, 'inn3_ov': inn3_ov,
        'inn4_team': inn4_team, 'inn4_score': inn4_score, 'inn4_runs': inn4_runs, 'inn4_wkts': inn4_wkts, 'inn4_ov': inn4_ov,
        'total_runs': total_runs, 'total_wkts': total_wkts, 'match_score': match_score,
        'winning_margin': winning_margin, 'margin_val': margin_val, 'margin_type': margin_type, 'follow_on': follow_on
    }

print("Generator helpers compiled.")
