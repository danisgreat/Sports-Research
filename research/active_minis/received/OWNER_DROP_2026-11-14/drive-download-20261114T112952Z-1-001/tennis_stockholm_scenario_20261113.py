"""Uncalibrated, explicit point->game->set->BO3 score-grid sensitivity.
No market inputs; not the repository official ML/REFMODEL run.
Source rows: https://www.tennislive.co.uk/atp/match/thiago-agustin-tirante-VS-alexander-shevchenko/bnp-paribas-nordic-open-stockholm-2026/
As-of 2026-11-12 14:00 UTC (13 Nov 01:00 AEDT). Excludes all walkovers.
"""
import json, collections, math, hashlib, datetime, os
from functools import lru_cache
from pathlib import Path

SOURCE='https://www.tennislive.co.uk/atp/match/thiago-agustin-tirante-VS-alexander-shevchenko/bnp-paribas-nordic-open-stockholm-2026/'
# (date, opponent, W/L, set scores from player's perspective). Played matches only, newest first.
TIR=[
('2026-11-08','Jaume Munar','W','7-6 6-3'),
('2026-11-04','Jan-Lennard Struff','L','7-6 3-6 6-7'),
('2026-11-01','Mattia Bellucci','L','4-6 4-6'),
('2026-10-31','Zachary Svajda','W','3-6 6-1 6-4'),
('2026-10-24','Adrian Mannarino','L','4-6 6-7'),
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
('2026-08-04','Duncan Chan','W','6-3 1-6 7-6')]
SHE=[
('2026-11-11','Casper Ruud','W','6-7 6-4 6-3'),
('2026-11-10','Adrian Mannarino','W','6-1 6-3'),
('2026-11-08','Jacob Fearnley','W','6-2 6-4'),
('2026-11-07','Viktor Durasovic','W','6-1 6-1'),
('2026-11-02','Luka Pavlovic','L','3-6 6-4 4-6'),
('2026-10-18','Stefanos Sakellaridis','L','6-7 4-6'),
('2026-10-17','Daniil Glinka','W','6-3 6-7 7-5'),
('2026-10-16','Mattia Bellucci','L','4-6 4-6'),
('2026-10-15','Jay Dylan Hara Friend','W','6-0 6-4'),
('2026-10-13','Miomir Kecmanovic','W','6-3 6-4'),
('2026-10-05','Yoshihito Nishioka','L','2-6 4-6'),
('2026-09-24','Hubert Hurkacz','L','3-6 6-7'),
('2026-08-30','Dino Prizmic','L','6-2 3-6 3-6 7-5 5-7'),
('2026-08-14','Botic van de Zandschulp','L','4-6 4-6'),
('2026-08-12',"Christopher O'Connell",'L','4-6 1-6'),
('2026-08-11','Pablo Llamas Ruiz','W','6-3 6-4'),
('2026-08-01','Kyrian Jacquet','L','6-4 4-6 3-6'),
('2026-07-21','Jan-Lennard Struff','L','6-3 6-7 4-6'),
('2026-07-18','Stefanos Tsitsipas','L','4-6 6-3 3-6'),
('2026-07-17','Quentin Halys','W','7-6 6-3')]

def window_stats(rows):
    out={}
    for k in (5,10,15,20):
        sub=rows[:k]
        gfor=gagainst=0
        for _,_,_,score in sub:
            for s in score.split():
                x,y=map(int,s.split('-'))
                gfor+=x; gagainst+=y
        out[f'L{k}']={'n':len(sub),'wins':sum(x[2]=='W' for x in sub),'losses':sum(x[2]=='L' for x in sub), 'games_for':gfor,'games_against':gagainst,'total_games':gfor+gagainst,'games_per_match':round((gfor+gagainst)/len(sub),3)}
    return out

def prob_hold(p):
    q=1-p
    return p**4*(1+4*q+10*q*q)+20*p**3*q**3*(p*p/(p*p+q*q))

def tb_win(pA,pB,first):
    @lru_cache(None)
    def f(a,b):
        if a>=7 and a-b>=2:return 1.
        if b>=7 and b-a>=2:return 0.
        if a==b==6:
            x=pA*(1-pB)
            y=(1-pA)*pB
            return x/(x+y)
        n=a+b
        point_served_by_first = (n%4 in (0,3))
        serverA=(first==0)==point_served_by_first
        p=pA if serverA else (1-pB)
        return p*f(a+1,b)+(1-p)*f(a,b+1)
    return f(0,0)

def set_distribution(holdA,holdB,tba,tbb,first):
    current={(0,0):1.}
    terminal=collections.defaultdict(float)
    for i in range(13):
        nxt=collections.defaultdict(float)
        for (a,b),prob in current.items():
            if (a>=6 or b>=6) and abs(a-b)>=2:
                terminal[(a,b,(first+a+b)%2)]+=prob
                continue
            if a==6 and b==6:
                tiebreak=tba if first==0 else tbb
                terminal[(7,6,1-first)]+=prob*tiebreak
                terminal[(6,7,1-first)]+=prob*(1-tiebreak)
                continue
            server=(first+a+b)%2
            h=holdA if server==0 else holdB
            winA=h if server==0 else 1-h
            nxt[(a+1,b)]+=prob*winA
            nxt[(a,b+1)]+=prob*(1-winA)
        current=nxt
    # After 13 games no nonterminal score except terminal 7-6, 6-7 accounted in previous i=12.
    return dict(terminal)

def match_distribution(pA,pB):
    holdA=prob_hold(pA);holdB=prob_hold(pB)
    tba=tb_win(pA,pB,0);tbb=tb_win(pA,pB,1)
    sets={fst:set_distribution(holdA,holdB,tba,tbb,fst) for fst in (0,1)}
    states={(0,0,0,0,0):.5,(0,0,0,0,1):.5}
    terminal=collections.defaultdict(float)
    for _ in range(3):
        nxt=collections.defaultdict(float)
        for (sa,sb,ga,gb,first),prob in states.items():
            for (a,b,next_first),ps in sets[first].items():
                wa=sa+(a>b);wb=sb+(b>a)
                outcome=(wa,wb,ga+a,gb+b,next_first)
                if wa==2 or wb==2:
                    terminal[outcome]+=prob*ps
                else:
                    nxt[outcome]+=prob*ps
        states=nxt
    assert not states
    total=sum(terminal.values())
    assert abs(total-1)<1e-10,total
    out=collections.defaultdict(float)
    for (sa,sb,a,b,first),prob in terminal.items():
        out[(sa,sb,a,b)]+=prob
    return out,{'hold_tir':holdA,'hold_shev':holdB,'tb_tir_serves_first':tba,'tb_shev_serves_first':tbb}

# Sensitivity assumptions, not fitted estimates. Interpreted as point-on-serve on 12 Nov 2026 indoor hard.
# Mixture protocol 0.25/0.5/0.25 with main base Tir moderately favoured by season serve+ranking,
# Shev favourable variation for recent rhythm, Tir favourable variation for rest/serve.
SCENARIOS=[
 {'label':'Shevchenko_stronger_indoors','weight':.25,'tir_point_serve':.682,'shev_point_serve':.700},
 {'label':'Balanced_base','weight':.50,'tir_point_serve':.700,'shev_point_serve':.686},
 {'label':'Tirante_fresher_serve','weight':.25,'tir_point_serve':.714,'shev_point_serve':.666}]

def summarize(dist):
    p_tir=sum(v for (a,b,ga,gb),v in dist.items() if a==2)
    p_tir_margin=sum(v for (a,b,ga,gb),v in dist.items() if ga>=gb)
    p_under=sum(v for (a,b,ga,gb),v in dist.items() if ga+gb<=23)
    p_three=sum(v for (a,b,ga,gb),v in dist.items() if a+b==3)
    ea=sum(ga*v for (a,b,ga,gb),v in dist.items())
    eb=sum(gb*v for (a,b,ga,gb),v in dist.items())
    totals=collections.defaultdict(float)
    margin=collections.defaultdict(float)
    for (a,b,ga,gb),v in dist.items():
        totals[ga+gb]+=v
        margin[ga-gb]+=v
    variance_t=sum((x-(ea+eb))**2*v for x,v in totals.items())
    variance_m=sum((x-(ea-eb))**2*v for x,v in margin.items())
    return {'tirante_winner':p_tir,'shevchenko_winner':1-p_tir,'tirante_plus_0_5_games':p_tir_margin,'shevchenko_minus_0_5_games':1-p_tir_margin,'under_23_5_games':p_under,'over_23_5_games':1-p_under,'three_sets':p_three,'E_tirante_games':ea,'E_shevchenko_games':eb,'E_total_games':ea+eb,'E_tirante_margin':ea-eb,'sd_total_games':math.sqrt(variance_t),'sd_margin_games':math.sqrt(variance_m),'sum_mass':sum(dist.values())}

if __name__=='__main__':
    mixture=collections.defaultdict(float);scenario_out=[]
    for s in SCENARIOS:
        d,m=match_distribution(s['tir_point_serve'],s['shev_point_serve'])
        for k,v in d.items():mixture[k]+=v*s['weight']
        scenario_out.append({**s,'summary':summarize(d),'parameters':m})
    ms=summarize(mixture)
    doc={'disposition':'ILLUSTRATIVE_SCENARIO_ONLY_NOT_OFFICIAL_P_CARD',
        'fixture':'Thiago Agustin Tirante vs Aleksandr Shevchenko, 2026-11-12, Stockholm ATP250 QF',
        'scheduled_start_utc':'2026-11-12T14:00:00+00:00',
        'model':'best-of-three Markov game hold; explicit 6-6 set tie breaks; alternating serve; first set first server 50/50; independent service probabilities conditional on scenario; set-to-set form shocks via mixture not estimated',
        'source':SOURCE,'scope':'regular match completed best-of-3; retires/walkovers excluded; assumed ordinary tiebreak through three sets',
        'mixture':SCENARIOS,'scenarios':scenario_out,'mixed':ms,'data_form':{'tirante':window_stats(TIR),'shevchenko':window_stats(SHE)},
        'source_limitations':['Point-service strength assumptions not fitted and not matched to recent opponents','Indoor 2026 sample small/conflicting across providers','No formal baseline or repository reference run','No independent first-ball timestamp','No medical confirmation','Operator retirement conventions unknown','No actual issue in repository'],
        'prior_games':{'tirante':TIR,'shevchenko':SHE},'calculation':'exact finite match score states, each probability is W mass (no pushes on .5 lines), no simulated randomness'}
    target=Path('/mnt/data/tennis_stockholm_scenario_20261113.json')
    target.write_text(json.dumps(doc,indent=2,ensure_ascii=False)+'\n')
    print('SCENARIOS')
    for x in scenario_out:
        print(x['label'],{k:round(v,4) for k,v in x['summary'].items() if k in ['tirante_winner','tirante_plus_0_5_games','under_23_5_games','E_total_games','three_sets']}, x['parameters'])
    print('MIXED',json.dumps({k:round(v,5) for k,v in ms.items()},indent=2))
    print('WINDOWS',json.dumps(doc['data_form'],indent=2))
    print('SHA256',hashlib.sha256(target.read_bytes()).hexdigest())
