"""Exploratory tennis serve-game Monte Carlo, NOT a repository-authorized primary forecast.
Sources (pre-event snapshots):
https://pythiatennis.com/dalibor-svrcina-vs-otto-virtanen-prediction-and-stats/?d=2026-11-11
Indoor (last 52wk): Svr SPW .637, RPW .420 (n=5); Virt SPW .687, RPW .357 (n=15).
Matchup starting points: Sv (own SPW + (1 - Virt RPW))/2 = .6400;
Virt (own SPW + (1 - Sv RPW))/2 = .6335.
Scenario perturbations intentionally reflect high uncertainty and the more mature indoor surface history of Virtanen.
No other model outputs, market data, or live information are used.
Tiebreaks at 6-6 in each set, 7pt first to 7 by two; best of 3.
Unit of analysis: total full match games, games handicap, match win. Non-completion not simulated.
"""
import numpy as np
from numba import njit
import json

@njit

def hold(p):
    q=1.0-p
    return p**4 * (1.0+4*q+10*q*q) + 20*p**3*q**3 * (p*p/(p*p+q*q))

@njit

def tiebreak(start_serv, ps, pv):
    a,b=0,0
    k=0
    while True:
        if k==0:
            server=start_serv
        elif ((k-1)//2)%2==0:
            server=1-start_serv
        else:
            server=start_serv
        # win of rally for Sv: if Sv serves, ps; if V serves, 1-pv.
        sv_point=(np.random.random() < (ps if server==0 else 1-pv))
        if sv_point: a+=1
        else: b+=1
        if (a>=7 or b>=7) and abs(a-b)>=2:
            return 0 if a>b else 1
        k+=1

@njit

def sim(n, ps, pv, seed):
    np.random.seed(seed)
    hs=hold(ps)
    hv=hold(pv)
    gdiff=np.empty(n,dtype=np.int16)
    total=np.empty(n,dtype=np.int16)
    match_winner=np.empty(n,dtype=np.int8)
    deciding=np.empty(n,dtype=np.int8)
    for i in range(n):
        sets=[0,0]
        games_sv, games_v=0,0
        service_order=0 if np.random.random()<.5 else 1
        total_games=0
        while sets[0]<2 and sets[1]<2:
            sa,sb=0,0
            while True:
                if sa==6 and sb==6:
                    firstserver=(service_order+total_games)%2
                    tiebreak_winner=tiebreak(firstserver,ps,pv)
                    if tiebreak_winner==0:sa+=1
                    else: sb+=1
                    total_games+=1
                    break
                else:
                    server=(service_order+total_games)%2
                    h=hs if server==0 else hv
                    server_wins=np.random.random()<h
                    sv_wins=(server==0 and server_wins) or (server==1 and not server_wins)
                    if sv_wins: sa+=1
                    else: sb+=1
                    total_games+=1
                    if (sa>=6 or sb>=6) and abs(sa-sb)>=2:
                        break
            games_sv+=sa;games_v+=sb
            if sa>sb: sets[0]+=1
            else:sets[1]+=1
        gdiff[i]=games_sv-games_v
        total[i]=games_sv+games_v
        match_winner[i]=0 if sets[0]>sets[1] else 1
        deciding[i]=1 if sets[0]+sets[1]==3 else 0
    return gdiff,total,match_winner,deciding,hs,hv

N=250000
cases=[("lower_virtanen",.645,.631,41276),("base",.632,.647,41277),("higher_virtanen",.620,.663,41278)]
output=[]
for label,ps,pv,seed in cases:
    gd,t,mw,dec,hs,hv=sim(N,ps,pv,seed)
    out={
    'scenario':label,'simulations':N,'p_sv_serve':ps,'p_vi_serve':pv,
    'p_sv_hold':hs,'p_vi_hold':hv,
    'P_Svrcina_plus_0_5':float(np.mean(gd>=0)),
    'P_Virtanen_minus_0_5':float(np.mean(gd<=-1)),
    'P_Over_23_5':float(np.mean(t>=24)),
    'P_Under_23_5':float(np.mean(t<=23)),
    'P_Svrcina_match_winner':float(np.mean(mw==0)),
    'P_Virtanen_match_winner':float(np.mean(mw==1)),
    'P_deciding_set':float(np.mean(dec==1)),
    'P_games_tie':float(np.mean(gd==0)),
    'expected_total_games':float(np.mean(t)),
    'std_total_games':float(np.std(t)),
    'expected_game_margin_Sv':float(np.mean(gd)),
    'std_game_margin_Sv':float(np.std(gd)),
    'P_Virtanen_minus0_5_and_Under23_5':float(np.mean((gd<=-1)&(t<=23))),
    'P_Svrcina_plus0_5_and_Under23_5':float(np.mean((gd>=0)&(t<=23))),
    'typical_total_bins':{str(k):int(np.sum(t==k)) for k in range(18,34)},
    }
    output.append(out)
weights=[.25,.5,.25]
fields=[k for k in output[0] if k.startswith('P_') or k.startswith('expected_') or k.startswith('std_')]
mixture={k:sum(weights[i]*output[i][k] for i in range(3)) for k in fields}
result={'method':'exploratory_shadow_nonrepo_unqualified','cases':output,'mixture_weights':weights,'mixture':mixture}
with open('/mnt/data/TENNIS_SHADOW_DIAGNOSTIC_20261112CC53B5C806-G0001.json','w') as f:json.dump(result,f,indent=2)
print(json.dumps(result,indent=2))
