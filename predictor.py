import sys
import pandas as pd
import random

# Constants.
AVG_D1_OE = 104.7
AVG_D1_TEMPO = 67.7
AVG_D1_OR = 28.5

# Get teams from command line arguments.
name_team1 = sys.argv[1]
name_team2 = sys.argv[2]

# Load CSV data.
df = pd.read_csv('teams.csv')

def get_team_stats(team_name):
    row = df[df['team'].str.lower() == team_name.lower()]
    if row.empty:
        print(f'Team "{team_name}" not found')
        # If team not found, exit the entire Python script with an error code 1 (meaning: "exited due to an issue").
        sys.exit(1)
    
    #.iloc[0] grabs the first row (row 0) from row as a Series.
    return row.iloc[0]

team1 = get_team_stats(name_team1)
team2 = get_team_stats(name_team2)

def compute_tempo(team):
    fga = team['fga']
    fta = team['fta']
    orb = team['orb']
    tov = team['tov']
    mp = team['mp']

    tempo = fga + 0.475 * fta - orb + tov
    return tempo

tempo_team1 = compute_tempo(team1)
tempo_team2 = compute_tempo(team2)

# Compute adjusted tempo.
adjusted_tempo = round((tempo_team1 - AVG_D1_TEMPO) + (tempo_team2 - AVG_D1_TEMPO) + AVG_D1_TEMPO, 2)


def compute_efficiency(team, adjusted_tempo):
    pts = team['pts']
    opp_pts = team['opp_pts']
    oe = round((100 * pts / adjusted_tempo), 2)
    de = round((100 * opp_pts / adjusted_tempo), 2)
    return oe, de

oe1, de1 = compute_efficiency(team1, adjusted_tempo)
oe2, de2 = compute_efficiency(team2, adjusted_tempo)

def compute_adjusted_oe(team_oe, opp_de):
    adjusted_oe = (team_oe - AVG_D1_OE) + (opp_de - AVG_D1_OE) + AVG_D1_OE
    return round(adjusted_oe, 2)

adjusted_oe_team1 = compute_adjusted_oe(oe1, de2)
adjusted_oe_team2 = compute_adjusted_oe(oe2, de1)

def compute_four_factors(team):
    fg = team['fg']
    fg3 = team['fg3']
    fga = team['fga']
    fta = team['fta']
    tov = team['tov']
    orb = team['orb']

    efg = round((fg + 0.5 * fg3) / fga, 2)
    to_pct = round(tov / (fga + 0.475 * fta - orb + tov), 2)
    or_pct = round(orb / (orb + AVG_D1_OR), 2)
    ft_rate = round(fta / fga, 2)
    
    return efg, to_pct, or_pct, ft_rate

efg1, to1, or1, ft_rate1 = compute_four_factors(team1)
efg2, to2, or2, ft_rate2 = compute_four_factors(team2)

# Calculate factor adjustment score using differences between the two teams.
# NOTE: lower TO% is better, so we reverse the calculation.
factor_adjustment_team1 = round((0.4 * (efg1 - efg2)) + (0.25 * (to2 - to1)) + (0.2 * (or1 - or2)) + (0.15 * (ft_rate1 - ft_rate2)), 2)
factor_adjustment_team2 = round((0.4 * (efg2 - efg1)) + (0.25 * (to1 - to2)) + (0.2 * (or2 - or1)) + (0.15 * (ft_rate2 - ft_rate1)), 2)

# Multiply factor by ten to match points.
factor_adjustment_team1 *= 10  
factor_adjustment_team2 *= 10  

# Add random luck factor by selecting random float between -2 and 2.
luck_team1 = random.uniform(-2, 2)
luck_team2 = random.uniform(-2, 2)

# Strength of Schedule (SOS) adjustment.
sos_adjustment_team1 = team1['sos'] * 0.1
sos_adjustment_team2 = team2['sos'] * 0.1

# Calculate predicted score.
predicted_score_team1 = round((adjusted_tempo / 100) * adjusted_oe_team1 + factor_adjustment_team1 + sos_adjustment_team1 + luck_team1, 2)
predicted_score_team2 = round((adjusted_tempo / 100) * adjusted_oe_team2 + factor_adjustment_team2 + sos_adjustment_team2 + luck_team2, 2)

print(f"{name_team1}: ", predicted_score_team1, f" {name_team2}: ", predicted_score_team2)





