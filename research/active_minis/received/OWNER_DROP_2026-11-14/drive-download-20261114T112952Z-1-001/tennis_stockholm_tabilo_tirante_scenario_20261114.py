#!/usr/bin/env python3
"""Reproducible NON-ISSUED, UNCALIBRATED tennis scenario diagnostic.

2026 Stockholm ATP 250 semifinal, Tabilo vs Tirante. Only the two players'
pre-match sporting evidence is used; no odds, tips, live in-match state or market
prices. Three *assumed*, NOT fitted, service-point probabilities. The given
handicap and total are priced from the same exact best-of-three set-score grid.
This is not the GitHub repo reference stage or a certified forecast.
"""
from __future__ import annotations
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, math

DATA_SOURCES={
  'official_fixture':'https://www.stockholmopen.se/en/tournament/spelschema?dayToDisplay=2',
  'official_qf':'https://www.stockholmopen.se/en/tournament/nyheter/torsdag-1-sammanfattning',
  'official_head_to_head':'https://www.stockholmopen.se/en/tournament/head-to-head/singles/te30/t0a1',
  'tabilo_season':'https://www.tennisabstract.com/cgi-bin/player-classic.cgi?f=A2026qq&p=AlejandroTabilo',
  'tirante_season':'https://www.tennisabstract.com/cgi-bin/player-classic.cgi?f=ACareerqq&p=202058%2FThiago-Agustin-Tirante&q=ZacharySvajda',
  'tabilo_results_alternate':'https://www.betexplorer.com/tennis/player/tabilo-alejandro/YgVnM5vO/results/',
  'tirante_results_alternate':'https://tennis-db.com/players/203/thiago-agustin-tirante/matches',
  'tabilo_qf':'https://www.tennis.com/tournaments/stockholm-open/matches/a-michelsen-vs-a-tabilo-2026-11-12',
  'tirante_qf':'https://www.tennis.com/tournaments/stockholm-open/matches/t-tirante-vs-a-shevchenko-2026-11-12',
}
# Date, opponent, W/L, score from the *named player's* side. Completed matches
# only; Båstad against Tirante and Stockholm Etcheverry walkovers excluded.
# Provisional game-result form captures, not the league's official training archive.
TABILO=[
 ('2026-11-12','Alex Michelsen','W','7-5 7-6'),
 ('2026-11-11','Lorenzo Sonego','W','7-6 6-7 7-5'),
 ('2026-11-02','Rafael Jodar','L','2-6 3-6'),
 ('2026-10-26','Rafael Jodar','L','4-6 2-6'),
 ('2026-10-07','Pablo Carreno Busta','L','6-4 6-7 4-6'),
 ('2026-09-30','Denis Shapovalov','L','5-7 6-3 4-6'),
 ('2026-09-30','Tommy Paul','W','6-1 6-2'),
 ('2026-09-23','Adrian Mannarino','L','4-6 4-6'),
 ('2026-09-19','Daniel Merida Aguilar','L','7-5 3-6 3-6'),
 ('2026-08-31','Alexander Zverev','L','2-6 6-7 2-6'),
 ('2026-08-31','Alexei Popyrin','W','2-6 7-6 7-6 6-2'),
 ('2026-08-05','Hubert Hurkacz','L','4-6 6-7'),
 ('2026-08-02','Rafael Jodar','L','7-6 4-6 4-6'),
 ('2026-08-01','Ben Shelton','W','4-6 7-5 6-4'),
 ('2026-07-30','Terence Atmane','W','6-3 7-6'),
 ('2026-07-27','Tallon Griekspoor','W','7-6 4-6 6-4'),
 ('2026-07-22','Tiago Torres','L','4-6 4-6'),
 ('2026-07-18','Andrey Rublev','L','4-6 6-4 4-6'),
 ('2026-07-16','Lautaro Midon','W','6-4 6-7 6-4'),
 ('2026-06-30','Kamil Majchrzak','L','3-6 5-7 5-7'),
]
TIRANTE=[
 ('2026-11-12','Aleksandr Shevchenko','W','7-6 6-7 6-3'),
 ('2026-11-08','Jaume Munar','W','7-6 6-3'),
 ('2026-11-04','Jan-Lennard Struff','L','7-6 3-6 6-7'),
 ('2026-11-01','Mattia Bellucci','L','4-6 4-6'),
 ('2026-10-31','Zachary Svajda','W','3-6 6-1 6-4'),
 ('2026-10-24','Adrian Mannarino','L','4-6 4-6'),
 ('2026-10-19','Facundo Diaz Acosta','L','7-6 1-6 4-6'),
 ('2026-10-10','Rafael Jodar','L','6-4 2-6 3-6'),
 ('2026-10-08','Hamad Medjedovic','W','6-4 6-2'),
 ('2026-09-30','Jan-Lennard Struff','L','1-6 4-6'),
 ('2026-09-19','Mert Alkaya','W','6-2 6-4'),
 ('2026-08-31','Adrian Mannarino','L','6-4 6-3 3-6 3-6 3-6'),
 ('2026-08-21','Arthur Fils','L','3-6 2-6'),
 ('2026-08-19','Jakub Mensik','W','5-7 6-4 6-4'),
 ('2026-08-17','Martin Landaluce','W','7-6 7-6'),
 ('2026-08-15','Novak Djokovic','W','2-6 6-4 6-4'),
 ('2026-08-13','Jan Choinski','W','7-6 6-7 7-6'),
 ('2026-08-09','Learner Tien','L','4-6 4-6'),
 ('2026-08-07','Alexei Popyrin','W','6-3 6-4'),
 ('2026-08-05','Taylor Fritz','W','7-5 6-3'),
]
# Three scenarios frozen before running; heuristic translates surface/hand/rest
# uncertainty into point-serve strengths. Base anchored roughly to season hard
# point-on-serve records Tabilo 65.7%, Tirante 67.3%, adjusted narratively
# for opponent left/right and fatigue. These shifts have no fitted effect sizes.
SCENARIOS=[
 {'id':'Tabilo_left_hand_rest_advantage', 'weight':0.25, 'p_tabilo_serve':0.681, 'p_tirante_serve':0.653},
 {'id':'Base_balanced', 'weight':0.50, 'p_tabilo_serve':0.672, 'p_tirante_serve':0.667},
 {'id':'Tirante_high_serve_case', 'weight':0.25, 'p_tabilo_serve':0.657, 'p_tirante_serve':0.689},
]

def window_stats(rows):
    out={}
    for k in (5,10,15,20):
        subset=rows[:k]; wins=sum(row[2]=='W' for row in subset)
        gf=ga=0
        for dt,opp,result,score in subset:
            for segment in score.split():
                x,y=map(int,segment.split('-'));gf+=x;ga+=y
        out[f'L{k}']={'n':len(subset),'wins':wins,'losses':len(subset)-wins,'games_for':gf,'games_against':ga,'games_per_match':(gf+ga)/len(subset)}
    return out

def game_hold(p):
    q=1-p
    return p**4*(1+4*q+10*q*q)+20*p**3*q**3*(p*p/(p*p+q*q))

def tiebreak_win(pA,pB,first):
    @lru_cache(None)
    def recur(a,b):
        if a>=7 and a-b>=2:return 1.0
        if b>=7 and b-a>=2:return 0.0
        if a==b==6:
            x=pA*(1-pB);y=(1-pA)*pB
            return x/(x+y)
        n=a+b
        served_by_initial=(n%4 in (0,3))
        serverA=((first==0)==served_by_initial)
        p=pA if serverA else 1-pB
        return p*recur(a+1,b)+(1-p)*recur(a,b+1)
    return recur(0,0)

def set_grid(hA,hB,tbA,tbB,first):
    state={(0,0):1.0}; terminal=defaultdict(float)
    for _ in range(13):
        nextstate=defaultdict(float)
        for (a,b),mass in state.items():
            if (a>=6 or b>=6) and abs(a-b)>=2:
                terminal[(a,b,(first+a+b)%2)]+=mass;continue
            if a==b==6:
                tw=tbA if first==0 else tbB
                terminal[(7,6,1-first)]+=mass*tw
                terminal[(6,7,1-first)]+=mass*(1-tw)
                continue
            server=(first+a+b)%2
            pA=hA if server==0 else 1-hB
            nextstate[(a+1,b)]+=mass*pA
            nextstate[(a,b+1)]+=mass*(1-pA)
        state=nextstate
    return dict(terminal)

def match_grid(pA,pB):
    hA,hB=game_hold(pA),game_hold(pB)
    tA,tB=tiebreak_win(pA,pB,0),tiebreak_win(pA,pB,1)
    sets={fst:set_grid(hA,hB,tA,tB,fst) for fst in (0,1)}
    states={(0,0,0,0,0):0.5,(0,0,0,0,1):0.5}
    terminal=defaultdict(float)
    for _ in range(3):
        nxt=defaultdict(float)
        for (sa,sb,ga,gb,first),m in states.items():
            for (a,b,next_first),ps in sets[first].items():
                key=(sa+(a>b),sb+(b>a),ga+a,gb+b,next_first)
                if key[0]==2 or key[1]==2:terminal[key]+=m*ps
                else:nxt[key]+=m*ps
        states=nxt
    assert not states
    out=defaultdict(float)
    for (sa,sb,ga,gb,first),m in terminal.items():out[(sa,sb,ga,gb)]+=m
    assert abs(sum(out.values())-1)<1e-10
    return out,{'hold_tabilo':hA,'hold_tirante':hB,'tie_break_win_A_first':tA,'tie_break_win_B_first':tB}

def summarize(d):
    W=lambda condition:sum(v for (sa,sb,a,b),v in d.items() if condition(sa,sb,a,b))
    Ptab=W(lambda sa,sb,a,b:sa==2)
    cover_tab=W(lambda sa,sb,a,b:a-b>=2)
    over=W(lambda sa,sb,a,b:a+b>=25)
    dset=W(lambda sa,sb,a,b:sa+sb==3)
    ea=sum(a*v for (sa,sb,a,b),v in d.items());eb=sum(b*v for (sa,sb,a,b),v in d.items())
    sdT=math.sqrt(sum((a+b-ea-eb)**2*v for (sa,sb,a,b),v in d.items()))
    sdM=math.sqrt(sum((a-b-ea+eb)**2*v for (sa,sb,a,b),v in d.items()))
    joint=W(lambda sa,sb,a,b:a-b>=2 and a+b<=24) # both ranked lose: Tirante +1.5 and Over24.5
    return {'tabilo_match_winner':Ptab,'tirante_match_winner':1-Ptab,'tabilo_minus_1_5':cover_tab,
            'tirante_plus_1_5':1-cover_tab,'over_24_5':over,'under_24_5':1-over,
            'three_sets':dset,'E_tabilo_games':ea,'E_tirante_games':eb,'E_total_games':ea+eb,
            'E_tabilo_margin_games':ea-eb,'sd_total_games':sdT,'sd_margin_games':sdM,
            'joint_failure_tirante_plus_and_over':joint,'mass':sum(d.values())}

def main():
    scenarios=[]; mixture=defaultdict(float)
    for s in SCENARIOS:
        g,params=match_grid(s['p_tabilo_serve'],s['p_tirante_serve'])
        scenarios.append({**s,'parameters':params,'summary':summarize(g)})
        for key,v in g.items():mixture[key]+=s['weight']*v
    out={'fixture':'Alejandro Tabilo vs Thiago Agustin Tirante, Stockholm ATP 250 SF, 2026-11-13 14:00 CET',
         'scheduled_start':'2026-11-14T00:00:00+11:00','status':'ILLUSTRATIVE_NOT_PRIMARY_NOT_ISSUED',
         'governing_research_mode':'SPORTS_ONLY_MARKET_BLIND',
         'timing':'RUN_AFTER_SCHEDULE; INPUT_CLEANLINESS_UNVERIFIED; LIVE_SCORE_POSSIBLY_EXPOSED_IN_SEARCH',
         'method':'exact best of three (game-hold from serve point p; set and tiebreak recursion; two initial service orders; 0.25/0.5/0.25 mixture); independent points and fixed serves within each scenario; uncertainty NOT calibrated',
         'scenarios':scenarios,'mixed':summarize(mixture),'source_urls':DATA_SOURCES,
         'pre_match_prior_games':{'tabilo':TABILO,'tirante':TIRANTE},
         'form_windows':{'tabilo':window_stats(TABILO),'tirante':window_stats(TIRANTE)},
         'key_limitations':['Sport level sources show match near/after nominal start; no verified first ball','Official full QF records existed before scheduled start but capture time after start','2026 surface rate data not independently verified as pre-start frozen snapshot','serve-point scenario adjustments not fitted or calibrated','no tour-only same-line baseline built','unconfirmed health/actual first server and retirement operator terms','models do not include dynamic form shocks beyond scenario-level mixture']}
    path=Path('/mnt/data/tennis_stockholm_tabilo_tirante_scenario_20261114.json')
    path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print('JSON',path,'sha256',hashlib.sha256(path.read_bytes()).hexdigest())
    print('SCENARIO SUMMARY')
    for row in scenarios:
        print(row['id'], {k:round(v,5) for k,v in row['summary'].items() if k in ('tirante_plus_1_5','over_24_5','tabilo_match_winner','E_total_games')})
    print('MIXTURE',{k:round(v,5) for k,v in out['mixed'].items()})
    print('WINDOWS',out['form_windows'])
if __name__=='__main__':main()
