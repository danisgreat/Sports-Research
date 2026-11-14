"""Research-only EXACT best-of-three tennis point->game->set->match sensitivity.
Fixture: Zsombor Piros vs Daniel Altmaier, Orleans Challenger QF, 13 Nov 2026.
No market odds, previews or bookmaker data used to set probabilities.
No official repository runtime, no calibrated predictive model. Exact enumeration is
conditional on uncalibrated point-service assumptions below and on full completion.
"""
import json, collections, math, hashlib, datetime
from pathlib import Path
from functools import lru_cache

# Dates/scores from current draw and independent result recaps, verified as dated
# pre-request prior results, not future match results. Order: newest first.
PIROS=[
('2026-11-11','Clement Tabur','W','2-6 7-6 6-3','Orleans Challenger indoor'),
('2026-11-10','Luca Nardi','W','7-6 1-6 6-4','Orleans Challenger indoor'),
('2026-11-06','Dalibor Svrcina','L','6-4 0-6 4-6','Bratislava Challenger indoor'),
('2026-11-04','Sascha Gueymard Wayenburg','W','6-3 6-7 6-3','Bratislava Challenger indoor'),
('2026-11-02','Matthew William Donald','W','6-3 6-3','Bratislava Challenger indoor')]
ALTMAIER=[
('2026-11-11','Buvaysar Gadamauri','W','3-6 7-5 6-1','Orleans Challenger indoor'),
('2026-11-10','Adrien Gobat','W','6-2 3-6 6-3','Orleans Challenger indoor'),
('2026-10-31','Alex Molcan','L','4-6 6-7','Paris Masters qualifying indoor'),
('2026-10-29','Jiri Lehecka','L','5-7 4-6','Basel ATP indoor'),
('2026-10-26','Juan Manuel Cerundolo','W','6-7 7-6 6-4','Basel ATP indoor')]

SOURCES={
'official_atp_draw':'https://www.protennislive.com/posting/2026/2273/mds.pdf',
'official_venue_schedule':'https://opendorleans.com/programmation/',
'event_time_court_reporting':'https://tennistonic.com/tennis-news/1081224/prediction-preview-h2h-altmaier-piros-martinez-portero-and-basavareddy-to-play-on-court-1-on-friday-orleans-challenger/',
'history_piros':'https://en.24score.com/tennis/match/211800-piros_zsombor-altmaier_daniel',
'player_indoor_stats':'https://www.tennisexplorer.com/match-detail/?id=3377369',
'basel_altmaier_v_cerundolo':'https://www.tennis.com/tournaments/swiss-indoors-basel/matches/d-altmaier-vs-j-cerundolo-2026-10-26',
'basel_altmaier_v_lehecka':'https://www.tennis.com/tournaments/swiss-indoors-basel/matches/d-altmaier-vs-j-lehecka-2026-10-29',
'paris_altmaier_v_molcan':'https://www.tennis.com/tournaments/rolex-paris-masters/matches/a-molcan-vs-d-altmaier-2026-10-31',
'public_match_stat_summary':'https://www.stevegtennis.com/head-to-head/men/Zsombor_Piros/Daniel_Altmaier/',
}

# Frozen scenario assumptions (point won on own serve), NOT fitted estimates.
# Lower Piros service strength reflects weaker hold% in two Orleans matches;
# upper branch reflects 2026 indoor result advantage, with opponent-level uncertainty.
# A deterministic mixture integrates this between-match uncertainty once.
SCENARIOS=[
{'name':'Altmaier_indoor_serve_advantage','weight':0.25,'p_piros_serve':0.626,'p_altmaier_serve':0.688},
{'name':'base_moderate_altmaier_serve_advantage','weight':0.50,'p_piros_serve':0.649,'p_altmaier_serve':0.669},
{'name':'Piros_indoor_strength_branch','weight':0.25,'p_piros_serve':0.669,'p_altmaier_serve':0.653},
]

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


def window_stats(rows):
    out={}
    for k in (5,10,15,20):
        sub=rows[:k]
        gf=ga=0
        for d,opponent,res,score,venue in sub:
            for pair in score.split():
                a,b=map(int,pair.split('-'));gf+=a;ga+=b
        out['L'+str(k)]={'verified_n':len(sub),'target_n':k,
           'wins':sum(x[2]=='W' for x in sub), 'losses':sum(x[2]=='L' for x in sub),
           'games_for':gf,'games_against':ga,
           'games_per_match': (gf+ga)/len(sub),
           'closure':'COMPLETE_DATED_L5' if k==5 else 'PARTIAL_REMAINDER_NOT_SOURCE_VERIFIED'}
    return out

def summarize_g8(dist):
    p_plus=sum(v for (sa,sb,a,b),v in dist.items() if a-b>=-2)
    p_over=sum(v for (sa,sb,a,b),v in dist.items() if a+b>=23)
    p_win=sum(v for (sa,sb,a,b),v in dist.items() if sa==2)
    p_three=sum(v for (sa,sb,a,b),v in dist.items() if sa+sb==3)
    ea=sum(a*v for (sa,sb,a,b),v in dist.items())
    eb=sum(b*v for (sa,sb,a,b),v in dist.items())
    mu_t=ea+eb;mu_m=ea-eb
    var_t=sum(((a+b)-mu_t)**2*v for (sa,sb,a,b),v in dist.items())
    var_m=sum(((a-b)-mu_m)**2*v for (sa,sb,a,b),v in dist.items())
    return {'piros_plus_2_5_games':p_plus,'altmaier_minus_2_5_games':1-p_plus,
           'over_22_5_games':p_over,'under_22_5_games':1-p_over,
           'piros_match_winner':p_win,'altmaier_match_winner':1-p_win,
           'three_sets':p_three,'E_piros_games':ea,'E_altmaier_games':eb,
           'E_combined_games':mu_t,'E_piros_minus_altmaier_games':mu_m,
           'SD_total_games':math.sqrt(var_t),'SD_margin_games':math.sqrt(var_m),
           'sum_mass':sum(dist.values()),
           'p_cover_plus_2_5_and_over':sum(v for (sa,sb,a,b),v in dist.items() if a-b>=-2 and a+b>=23),
           'p_fail_both_top_two':sum(v for (sa,sb,a,b),v in dist.items() if (a-b<=-3) and (a+b<=22))}

if __name__=='__main__':
    mix=collections.defaultdict(float);results=[]
    for row in SCENARIOS:
        d,params=match_distribution(row['p_piros_serve'],row['p_altmaier_serve'])
        for key,v in d.items():mix[key]+=row['weight']*v
        results.append({**row,'derived_parameters':params,'outputs':summarize_g8(d)})
    final=summarize_g8(mix)
    assert abs(final['sum_mass']-1)<1e-10
    assert abs(final['piros_plus_2_5_games']+final['altmaier_minus_2_5_games']-1)<1e-12
    assert abs(final['over_22_5_games']+final['under_22_5_games']-1)<1e-12
    assert abs(final['piros_match_winner']+final['altmaier_match_winner']-1)<1e-12
    doc={
        'fixture':'Piros vs Altmaier, Orleans Challenger 125 quarterfinal, 2026-11-13',
        'nominal_kickoff':'2026-11-13T23:00:00+11:00 (13:00 Europe/Paris; time sources conflict)',
        'model_disposition':'ILLUSTRATIVE_SCENARIO_NOT_PRIMARY_OR_CERTIFIED',
        'distribution':'exact best-of-3 point-to-game-to-set finite recursion, standard seven-point tiebreak to 2 margin, alternating server, random initial server 50/50, complete-match condition, low/base/high mixture',
        'form_data':{'Piros':window_stats(PIROS),'Altmaier':window_stats(ALTMAIER)},
        'prior_games':{'Piros':PIROS,'Altmaier':ALTMAIER},
        '2026_indoor_win_loss_public_source':{'Piros':'13-3 TennisExplorer','Altmaier':'6-4 TennisExplorer (TennisTonic 6-5; conflicting scope)'},
        '2026_orleans_first_two_game_hold_public_source':{'Piros':'23 holds / 30 service games = 76.7%','Altmaier':'24 holds / 27 service games = 88.9%; public stats are from only 2 matches'},
        'scenarios':results,'scenario_mixture':SCENARIOS,'mixed_outputs':final,
        'research_sources':SOURCES,
        'excluded_sources':['betting odds','market movements','analyst predictions'],
        'limitation':['Point-serve input values uncalibrated and not directly fitted from opponent-adjusted tour-level stats','10/15/20 pre-cutoff dated event rows missing or incomplete','Starting fitness/withdrawal and live first point not independently verified','No tested match-form shock sigma; only mixture scenarios','No competition-specific league-only baseline sample for O/U 22.5 and margin +/-2.5','Retirement and operator settlement unknown; conditional on full completion','No official GitHub ml reference, lint, pregame freeze, learning-log or import','No independent cross-source full lineup/medical verification'],
    }
    path=Path('/mnt/data/tennis_orleans_piros_altmaier_scenario_20261113.json')
    path.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'scenarios':[{**{'name':x['name']}, **{k:round(x['outputs'][k],5) for k in ['piros_plus_2_5_games','over_22_5_games','piros_match_winner','E_combined_games']}} for x in results], 'mixed':{k:round(v,6) for k,v in final.items()},'json_sha256':hashlib.sha256(path.read_bytes()).hexdigest()},indent=2))
