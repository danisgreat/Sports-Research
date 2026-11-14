"""Chat-local only: uncalibrated, documented score-grid sensitivity.
No repository model, outcome information, staking or market inputs.
Regulation independent Poisson. No separately fitted empty-net/goalie/PBPs.
A single credited overtime/shootout goal affects neither the 5.5 total
nor the 1.5-goal spread for a regulation-tied game.
"""
import math

MOTOR_SEASON_GF = 69 / 19
MOTOR_SEASON_GA = 45 / 19
MOTOR_L5 = [(2, 3), (3, 4), (5, 1), (3, 1), (3, 1)]
LIBEREC_L5 = [(5, 4), (1, 5), (3, 2), (4, 3), (1, 2)]

# Reciprocal recent/season scoring proxy; deliberately uncalibrated.
mu_home = (MOTOR_SEASON_GF + sum(g2 for _, g2 in LIBEREC_L5)/5) / 2
mu_away = (MOTOR_SEASON_GA + sum(g1 for g1, _ in LIBEREC_L5)/5) / 2

def evaluate(h, a, cap=36):
    hp=[math.exp(-h)*h**i/math.factorial(i) for i in range(cap+1)]
    ap=[math.exp(-a)*a**i/math.factorial(i) for i in range(cap+1)]
    mass = {(x,y):px*py for x,px in enumerate(hp) for y,py in enumerate(ap)}
    s=sum(mass.values())
    # All probabilities below are conditional on included mass; tail negligible.
    cover=sum(v for (x,y),v in mass.items() if x-y>=2)/s
    over=sum(v for (x,y),v in mass.items() if x+y>=6)/s
    reg_home=sum(v for (x,y),v in mass.items() if x>y)/s
    reg_draw=sum(v for (x,y),v in mass.items() if x==y)/s
    return {"home_mu_reg":h,"away_mu_reg":a,"reg_total_mu":h+a,
            "full_total_mu_with_one_ot_so_goal_tie":h+a+reg_draw,
            "motor_minus_1_5":cover,"liberec_plus_1_5":1-cover,
            "over_5_5":over,"under_5_5":1-over,
            "reg_motor_win":reg_home,"reg_draw":reg_draw,"reg_liberec_win":1-reg_home-reg_draw,
            "probability_mass_before_normalization":s}

if __name__ == "__main__":
    from pprint import pprint
    print("CENTRAL — motor season GF/GA, Liberec five-game GF/GA proxies")
    pprint(evaluate(mu_home,mu_away))
    print("SENSITIVITY — declared plausible alternatives, not statistical CI")
    for label,h,a in [
      ("lower_scoring",3.10,2.35),
      ("higher_scoring",3.70,2.80),
      ("Motor_stronger",4.10,2.20),
      ("closer_teams",2.90,2.70)]:
        print(label);pprint(evaluate(h,a))
