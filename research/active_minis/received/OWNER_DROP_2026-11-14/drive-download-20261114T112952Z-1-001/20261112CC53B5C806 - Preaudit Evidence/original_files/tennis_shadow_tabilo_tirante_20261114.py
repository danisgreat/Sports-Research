"""Exploratory exact tennis score-grid diagnostic: Tabilo vs Tirante, Stockholm 13 Nov 2026.
NOT a trained or calibrated model and NOT a repository-issued primary forecast.
All parameters are frozen source-derived 52-week serve/return aggregate rates and
explicit analyst sensitivity cases; no market prices/predictions are model inputs.
"""
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
import hashlib, json, math


def game_hold(p):
    q = 1-p
    return p**4*(1+4*q+10*q*q)+20*p**3*q**3*(p*p/(p*p+q*q))


def tb_win(pA,pB,first_server):
    states={(0,0):1.0}; won=0.0
    for k in range(160):
        nxt=defaultdict(float)
        server=first_server if k%4 in (0,3) else 1-first_server
        wp=pA if server==0 else 1-pB
        for (a,b),mass in states.items():
            for win,pr in ((True,wp),(False,1-wp)):
                aa,bb=(a+1,b) if win else (a,b+1)
                if max(aa,bb)>=7 and abs(aa-bb)>=2:
                    if aa>bb:won+=mass*pr
                else:nxt[aa,bb]+=mass*pr
        states=nxt
        if sum(states.values())<1e-14:break
    return won+0.5*sum(states.values())

@lru_cache(maxsize=32)
def set_scores(pA,pB,first_server):
    states={(0,0,first_server):1.0}; out=defaultdict(float)
    for n in range(13):
        nxt=defaultdict(float)
        for (a,b,s),mass in states.items():
            if a==6 and b==6:
                wt=tb_win(pA,pB,s)
                out[7,6,1-s]+=mass*wt
                out[6,7,1-s]+=mass*(1-wt)
            else:
                wa=game_hold(pA) if s==0 else 1-game_hold(pB)
                for aa,bb,pr in ((a+1,b,wa),(a,b+1,1-wa)):
                    if max(aa,bb)>=6 and abs(aa-bb)>=2: out[aa,bb,1-s]+=mass*pr
                    else:nxt[aa,bb,1-s]+=mass*pr
        states=nxt
    assert abs(sum(out.values())-1)<1e-9
    return out

def match_scores(pA,pB):
    score_sets=[set_scores(pA,pB,s) for s in (0,1)]
    outcomes=defaultdict(float)
    for initial in (0,1):
        states={(0,0,0,0,initial):0.5}
        for _ in range(3):
            nxt=defaultdict(float)
            for (sa,sb,ga,gb,s),mass in states.items():
                for (a,b,next_s),pr in score_sets[s].items():
                    sa1,sb1=sa+int(a>b),sb+int(a<b)
                    if max(sa1,sb1)==2:outcomes[ga+a,gb+b,sa1,sb1]+=mass*pr
                    else:nxt[sa1,sb1,ga+a,gb+b,next_s]+=mass*pr
            states=nxt
    assert abs(sum(outcomes.values())-1)<1e-9
    return outcomes

def metrics(pA,pB):
    d=match_scores(pA,pB)
    prob=lambda fn:sum(v for (a,b,sa,sb),v in d.items() if fn(a,b,sa,sb))
    result={
     'service_point_win_Tabilo':pA,'service_point_win_Tirante':pB,
     'service_hold_Tabilo':game_hold(pA),'service_hold_Tirante':game_hold(pB),
     'Tabilo_minus_1_5':prob(lambda a,b,sa,sb:a-b>=2),
     'Tirante_plus_1_5':prob(lambda a,b,sa,sb:a-b<=1),
     'Over_24_5':prob(lambda a,b,sa,sb:a+b>=25),
     'Under_24_5':prob(lambda a,b,sa,sb:a+b<=24),
     'Tabilo_win':prob(lambda a,b,sa,sb:sa==2),
     'Tirante_win':prob(lambda a,b,sa,sb:sb==2),
     'deciding_set':prob(lambda a,b,sa,sb:sa+sb==3),
     'expected_total_games':sum((a+b)*v for (a,b,sa,sb),v in d.items()),
     'expected_margin_Tabilo':sum((a-b)*v for (a,b,sa,sb),v in d.items()),
     'both_qualitative_leans_lose':prob(lambda a,b,sa,sb:a-b>=2 and a+b<=24),
     'Tirante_plus_and_Over_both_win':prob(lambda a,b,sa,sb:a-b<=1 and a+b>=25),
     'total_state_mass':sum(d.values()),'terminal_game_margin_states':len(d),
    }
    assert abs(result['Tabilo_minus_1_5']+result['Tirante_plus_1_5']-1)<1e-10
    assert abs(result['Over_24_5']+result['Under_24_5']-1)<1e-10
    assert abs(result['Tabilo_win']+result['Tirante_win']-1)<1e-10
    return result

# 52 weeks through Nov 12. PythiaTennis historical stats table, not its predictions or odds.
# Indoor match samples Tabilo=4, Tirante=7; all-surface Tabilo=68, Tirante=58.
rate={
'Tabilo':{'all_serve':.659,'all_return':.365,'indoor_serve':.631,'indoor_return':.324,'all_n':68,'indoor_n':4},
'Tirante':{'all_serve':.667,'all_return':.356,'indoor_serve':.674,'indoor_return':.307,'all_n':58,'indoor_n':7}}
# Matchup serve win = average(player own service point win and opponent lost return points).
all_T=(rate['Tabilo']['all_serve']+1-rate['Tirante']['all_return'])/2
all_I=(rate['Tirante']['all_serve']+1-rate['Tabilo']['all_return'])/2
ind_T=(rate['Tabilo']['indoor_serve']+1-rate['Tirante']['indoor_return'])/2
ind_I=(rate['Tirante']['indoor_serve']+1-rate['Tabilo']['indoor_return'])/2
k=20  # analyst sensitivity, NOT fitted or calibrated
shr_T=(k*all_T+rate['Tabilo']['indoor_n']*ind_T)/(k+rate['Tabilo']['indoor_n'])
shr_I=(k*all_I+rate['Tirante']['indoor_n']*ind_I)/(k+rate['Tirante']['indoor_n'])
scenarios={
 'all_surface_52wk':(all_T,all_I),
 'indoor_shrink20_matches':(shr_T,shr_I),
 'indoor_only_52wk_small_n':(ind_T,ind_I),
 'tabilo_improves_tirante_slips_1p5pp':(shr_T+.015,shr_I-.015),
 'tirante_improves_tabilo_slips_1p5pp':(shr_T-.015,shr_I+.015),
}
if __name__=='__main__':
    data={
      'event':'Alejandro Tabilo vs Thiago Agustin Tirante / Stockholm ATP 250 SF / 2026-11-13',
      'method':'Exact best-of-three game/tiebreak/set/match Markov-chain enumeration; initial server 50:50',
      'status':'EXPLORATORY_SHADOW_NOT_FRAMEWORK_PRIMARY_NOT_CALIBRATED',
      'contracts': ['Tabilo -1.5 completed match games','Tirante +1.5 completed match games','Over 24.5 completed match games','Under 24.5 completed match games'],
      'input_data':rate,
      'source_urls':['https://pythiatennis.com/alejandro-tabilo-vs-thiago-agustin-tirante-prediction-and-stats/?d=2026-11-13','https://www.stockholmopen.se/en/tournament/spelschema?dayToDisplay=7','https://www.stockholmopen.se/en/tournament/resultat?resultDay=6'],
      'sensitivities':{'k_shrink_match_equivalents':k,'serve_stress_plus_minus_points':0.015,'scenario_weights':'NONE; no weighted average published'},
      'assumptions':['IID service points, fixed player point probability per scenario','No injury/retirement/withdrawal/shortened match','Alternating service games and standard 6-6 tiebreak, first to 7 by 2','First server 50:50','No Elo, H2H, odds, external predictions or rest/fatigue effects entered into probabilities','No competition/level/opponent-adjusted calibration; small indoor n'],
      'results':{name:metrics(*ab) for name,ab in scenarios.items()}}
    target=Path('/mnt/data/TENNIS_SHADOW_DIAGNOSTIC_20261112CC53B5C806-G0009.json')
    target.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
    for name,metrics in data['results'].items():
       print(name, {k:round(metrics[k],4) for k in ('Tirante_plus_1_5','Tabilo_minus_1_5','Over_24_5','Under_24_5','Tabilo_win','deciding_set','expected_total_games','both_qualitative_leans_lose')})
    print('WROTE',target,'SHA256',hashlib.sha256(target.read_bytes()).hexdigest())
