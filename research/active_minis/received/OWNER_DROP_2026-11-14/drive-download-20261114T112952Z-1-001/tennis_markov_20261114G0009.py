"""G0009 Tabilo v Tirante, Stockholm 2026. Sports-only illustrative deterministic point/game/set tree.

NOT a calibrated prediction, repo-certified model, executable reference or publicly issued pick.
Model assumptions are scenario inputs, NOT fitted serve/return point rates. Best-of-three;
standard advantage game at deuce and 7-point tiebreak at six-all, winner by two.
No retirement/walkover mass; operator settlement conditions unknown.
"""
from collections import defaultdict
from functools import lru_cache


def hold_point_game(p):
    q = 1 - p
    return p**4 * (1 + 4*q + 10*q*q) + 20*p**3*q**3 * (p*p/(p*p+q*q))


@lru_cache(None)
def tb_win(a, b, first_server, pA, pB):
    if (a >= 7 or b >= 7) and abs(a-b) >= 2:
        return float(a>b)
    if a == b and a >= 6:
        win_two = pA * (1-pB)
        lose_two = (1-pA)*pB
        return win_two / (win_two+lose_two)
    n=a+b
    server = first_server if n == 0 or ((n-1)//2) % 2 == 1 else 1-first_server
    p_score_A = pA if server == 0 else (1-pB)
    return p_score_A * tb_win(a+1,b,first_server,pA,pB) + (1-p_score_A) * tb_win(a,b+1,first_server,pA,pB)


def one_set(initial_server,pA,pB):
    hA,hB=hold_point_game(pA),hold_point_game(pB)
    @lru_cache(None)
    def rec(a,b):
        total=a+b
        server=initial_server if total%2==0 else 1-initial_server
        if (a>=6 or b>=6) and abs(a-b)>=2:
            return {(int(a>b),a,b,server):1.0}
        if a==6 and b==6:
            pt=tb_win(0,0,server,pA,pB)
            return {(1,7,6,1-server):pt,(0,6,7,1-server):1-pt}
        p_win_game=hA if server==0 else (1-hB)
        out=defaultdict(float)
        for key,pr in rec(a+1,b).items():out[key]+=p_win_game*pr
        for key,pr in rec(a,b+1).items():out[key]+=(1-p_win_game)*pr
        return dict(out)
    return rec(0,0)


def match_states(pA,pB):
    sets={0:one_set(0,pA,pB),1:one_set(1,pA,pB)}
    out=defaultdict(float)
    def branch(sa,sb,gA,gB,first,weight,nsets):
        if sa==2 or sb==2:
            out[(int(sa>sb),gA,gB,nsets)]+=weight
            return
        for (a_win,sa_games,sb_games,next_first),prob in sets[first].items():
            branch(sa+a_win,sb+1-a_win,gA+sa_games,gB+sb_games,next_first,weight*prob,nsets+1)
    for first in (0,1):branch(0,0,0,0,first,0.5,0)
    assert abs(sum(out.values())-1)<1e-8
    return dict(out)


def summarize(states):
    sums=lambda check:sum(prob for (won,a,b,sets),prob in states.items() if check(won,a,b,sets))
    t_spread=sums(lambda won,a,b,sets:a-b>=2)
    over=sums(lambda won,a,b,sets:a+b>=25)
    return dict(tabilo_win=sums(lambda won,a,b,sets:bool(won)),tirante_win=sums(lambda won,a,b,sets:not won),tabilo_minus_1_5=t_spread,tirante_plus_1_5=1-t_spread,over_24_5=over,under_24_5=1-over,deciding_set=sums(lambda won,a,b,sets:sets==3),expected_tabilo_games=sum(a*p for (w,a,b,s),p in states.items()),expected_tirante_games=sum(b*p for (w,a,b,s),p in states.items()),expected_sets=sum(s*p for (w,a,b,s),p in states.items()),joint_failure_over_and_tirante_cushion=sums(lambda won,a,b,sets:a+b<=24 and a-b>=2))


if __name__ == '__main__':
    # A=Tabilo, B=Tirante. Weights frozen at 0.25/0.50/0.25 before arithmetic.
    # Serve-point rates are deliberately scenario assumptions, not inferred from
    # single-match sample or raw 2026 pregame feed (none qualified for both).
    cases=[('Tirante_current_indoor_serve_edge',.665,.680,.25),
           ('balanced_indoor_competition',.674,.667,.50),
           ('Tabilo_better_return_regime',.682,.655,.25)]
    overall=defaultdict(float)
    for name,pA,pB,weight in cases:
        ss=match_states(pA,pB)
        for k,v in ss.items():overall[k]+=weight*v
        print(name,'weight',weight,'serve_point',pA,pB,'hold',round(hold_point_game(pA),6),round(hold_point_game(pB),6),'outcomes',{k:round(v,6) for k,v in summarize(ss).items()})
    print('mixture',{k:round(v,6) for k,v in summarize(overall).items()})
    print('checksum',round(sum(overall.values()),12),'states',len(overall))
