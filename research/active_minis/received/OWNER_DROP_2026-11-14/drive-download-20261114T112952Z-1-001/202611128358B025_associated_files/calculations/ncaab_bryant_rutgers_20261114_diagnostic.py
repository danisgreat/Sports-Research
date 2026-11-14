"""Chat-local, uncalibrated NCAA basketball scoring sensitivity. No repository freeze or model run.
Inputs: Bryant, Rutgers 2026-27 official box-score aggregates through Nov 10, 2026.
Not an officially calibrated predictive model. Independent team scores and OT parameters are assumptions.
"""
import json
import numpy as np
from datetime import datetime,timezone

BRYANT_GAMES=[
    {'date':'2026-11-02','opponent':'Siena','pf':80,'pa':75,'fga':65,'orb':11,'tov':14,'fta':25},
    {'date':'2026-11-05','opponent':'Quinnipiac','pf':56,'pa':66,'fga':61,'orb':12,'tov':12,'fta':13},
    {'date':'2026-11-08','opponent':'Fairfield','pf':59,'pa':68,'fga':54,'orb':10,'tov':20,'fta':17},
    {'date':'2026-11-10','opponent':'Providence','pf':55,'pa':78,'fga':47,'orb':6,'tov':25,'fta':14}]
RUTGERS_GAMES=[
    {'date':'2026-11-06','opponent':'New Haven','pf':81,'pa':54,'fga':60,'orb':13,'tov':11,'fta':18},
    {'date':'2026-11-10','opponent':'NJIT','pf':101,'pa':64,'fga':60,'orb':12,'tov':8,'fta':41}]
for g in BRYANT_GAMES+RUTGERS_GAMES:
    g['est_poss']=g['fga']-g['orb']+g['tov']+0.44*g['fta']

b_avg=np.mean([g['pf'] for g in BRYANT_GAMES]); b_allowed=np.mean([g['pa'] for g in BRYANT_GAMES])
r_avg=np.mean([g['pf'] for g in RUTGERS_GAMES]); r_allowed=np.mean([g['pa'] for g in RUTGERS_GAMES])
# Symmetric offense/defense arithmetic baseline (NOT opponent-adjusted).
central={'Rutgers':(r_avg+b_allowed)/2, 'Bryant':(b_avg+r_allowed)/2}
# Tempo estimated from possessions; no rate correction on center, since points per game are the direct prior.
poss={'Bryant':float(np.mean([g['est_poss'] for g in BRYANT_GAMES])),'Rutgers':float(np.mean([g['est_poss'] for g in RUTGERS_GAMES]))}

SEED=202611140910; N=200_000

def simulate(mu_r,mu_b,sd_r=13.5,sd_b=12.5,seed=SEED,n=N):
    rng=np.random.default_rng(seed)
    r=np.rint(np.maximum(0,rng.normal(mu_r,sd_r,n))).astype(int)
    b=np.rint(np.maximum(0,rng.normal(mu_b,sd_b,n))).astype(int)
    # Overtime: for regulation ties simulate additional 5-minute periods independently.
    # Poisson(5.5) is a transparent assumption, not a measured NCAA input.
    ot=0; t=r==b
    while np.any(t) and ot<12:
        ot+=1
        r[t]+=rng.poisson(5.5,size=int(t.sum()))
        b[t]+=rng.poisson(5.5,size=int(t.sum()))
        t=(r==b)
    tot=r+b; margin=r-b
    result={
        'n':n,'seed':seed,'mu_regulation_rutgers':mu_r,'mu_regulation_bryant':mu_b,
        'sd_regulation_rutgers':sd_r,'sd_regulation_bryant':sd_b,
        'overtime_rounds_max':ot,'unresolved_after_max':int(t.sum()),
        'rutgers_win':float(np.mean(margin>0)),
        'bryant_win':float(np.mean(margin<0)),
        'bryant_plus21_5':float(np.mean(margin<=21)),
        'rutgers_minus21_5':float(np.mean(margin>=22)),
        'over148_5':float(np.mean(tot>=149)),
        'under148_5':float(np.mean(tot<=148)),
        'mean_final_rutgers':float(r.mean()),'mean_final_bryant':float(b.mean()),
        'mean_final_total':float(tot.mean()),'mean_final_margin':float(margin.mean()),
        'regulation_tie_fraction':None,
    }
    return result

cases={
    'central':simulate(central['Rutgers'],central['Bryant']),
    'press_accelerates_6_total':simulate(central['Rutgers']+4,central['Bryant']+2,seed=SEED+1),
    'slower_half_court_minus6_total':simulate(central['Rutgers']-3,central['Bryant']-3,seed=SEED+2),
    'rutgers_mismatch_plus5_margin':simulate(central['Rutgers']+4,central['Bryant']-1,seed=SEED+3),
    'bryant_resistance_minus5_margin':simulate(central['Rutgers']-1,central['Bryant']+4,seed=SEED+4),
}
output={'status':'CHAT_LOCAL_SCENARIO_UNCALIBRATED_NOT_ISSUED','fixture':'Bryant @ Rutgers','scheduled_start':'2026-11-14T10:00:00+11:00',
        'historical_regulation_team_means':{'rutgers_pf':r_avg,'rutgers_pa':r_allowed,'bryant_pf':b_avg,'bryant_pa':b_allowed},
        'possessions_approximate_from_stats':poss,
        'central_regulation_estimate':central,
        'full_game_incl_overtime':True,
        'scenarios':cases,
        'uncertainty_note':'Neither the independent team-score SDs nor overtime rate are fitted/validated for this competition. No bookmaker prices, results, or in-play inputs used.'}
with open('/mnt/data/ncaab_bryant_rutgers_20261114_results.json','w') as f:
    json.dump(output,f,indent=2)
print(json.dumps(output,indent=2))
