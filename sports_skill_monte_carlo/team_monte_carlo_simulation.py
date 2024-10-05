# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 22:34:26 2024

@author: carne
"""

import team
import random


# Simulation Constants
TYPICAL_COACH_WIN_PROBABILITY = 0.45
SUPERIOR_COACH_WIN_PROBABILITY = 0.55
NUMBER_OF_TEAMS = 32
GAMES_PER_SEASON = 16
NUMBER_OF_SEASONS = 10
TOL = 0.0001
PLAYOFF_TEAMS = 4

# Create teams with random coach IDs and win probabilities
teams = [team.Team(coach_id=i, win_probability=TYPICAL_COACH_WIN_PROBABILITY) for i in range(1, NUMBER_OF_TEAMS+1)]
next_coach_id = NUMBER_OF_TEAMS + 1

# Choose 1 coach to be superior to the rest
teams[0].set_coach_win_probability(SUPERIOR_COACH_WIN_PROBABILITY)

for season in range(0,NUMBER_OF_SEASONS):
    print("Season: ", season+1)
    for game in range(0,GAMES_PER_SEASON):
        print("Game: ", game+1)
        # Shuffle the teams to ensure random matchups
        random.shuffle(teams)
        
        # Generate 16 matchups
        matchups = [(teams[i], teams[i+1]) for i in range(0, NUMBER_OF_TEAMS, 2)]
        
        # Execute the matchups
        for idx, (team1, team2) in enumerate(matchups, start=1):

            #normalize win/loss probabilities
            t = team1.get_coach_win_probability() + team2.get_coach_win_probability()
            team1_p = team1.get_coach_win_probability() / t
            team2_p = team2.get_coach_win_probability() / t
            assert((team1_p + team2_p > 1-TOL) and team1_p + team2_p < 1+TOL)
            if random.random() <= team1_p:
                #team 1 wins
                team1.increment_wins()
                team2.increment_losses()
                print(f"Matchup {idx}: Team with Coach ID {team1.get_coach_id()} vs Team with Coach ID {team2.get_coach_id()}: Winner {team1.get_coach_id()}")

            else:
                #team 2 wins
                team1.increment_losses()
                team2.increment_wins()
                print(f"Matchup {idx}: Team with Coach ID {team1.get_coach_id()} vs Team with Coach ID {team2.get_coach_id()}: Winner {team2.get_coach_id()}")

    # Sort teams by number of wins (descending)
    sorted_teams_by_wins = sorted(teams, key=lambda x: x.get_wins(), reverse=True)
    for teamx in sorted_teams_by_wins:
        print(f"Team {teamx.get_coach_id()}: Wins={teamx.get_wins()}, Losses={teamx.get_losses()}")
        
    # choose champion
    t = 0
    playoff_teams = []    
    for teamx in sorted_teams_by_wins[0:PLAYOFF_TEAMS]:
        t = t + teamx.get_coach_win_probability()
    for teamx in sorted_teams_by_wins[0:PLAYOFF_TEAMS]:
        playoff_teams.append([teamx, teamx.get_coach_win_probability()/t])
    p = random.random()
    p_cumulative = 0
    for [teamx, p1] in playoff_teams:
        p_cumulative = p_cumulative + p1
        if p <= p_cumulative:
            teamx.won_championship()
            break
    print(f"Champion {teamx.get_team_name()}, Coach: {teamx.get_coach_id()}")

    # reset wins and losses for next season
    for teamx in teams:
        teamx.set_wins(0)
        teamx.set_losses(0)

print("")
print(f"Summary Results for {NUMBER_OF_SEASONS} Seasons")
for teamx in teams:
    print(f"Team: {teamx.get_team_name()}, Championships: {teamx.get_team_championships()}, Coach Win Probability: {teamx.get_coach_win_probability()}")

