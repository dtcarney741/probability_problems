# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 22:34:26 2024

@author: carne
"""

import team
import random
import numpy as np
import matplotlib.pyplot as plt


class MonteCarloSimulator:
    def __init__(self):
        self.coach_win_loss_ratio_data_sets = {}
        self.coach_championships_data_sets = {}

    def add_coach_win_loss_ratio_data_point(self, dataset_name, value):
        if dataset_name not in self.coach_win_loss_ratio_data_sets:
            self.coach_win_loss_ratio_data_sets[dataset_name] = []
        self.coach_win_loss_ratio_data_sets[dataset_name].append(value)

    def add_coach_championships_data_point(self, dataset_name, value):
        if dataset_name not in self.coach_championships_data_sets:
            self.coach_championships_data_sets[dataset_name] = []
        self.coach_championships_data_sets[dataset_name].append(value)

    def get_coach_win_loss_ratio_statistics(self, dataset_name):
        if dataset_name in self.coach_win_loss_ratio_data_sets:
            data = self.coach_win_loss_ratio_data_sets[dataset_name]
            mean = np.mean(data)
            std_dev = np.std(data)
            return mean, std_dev
        else:
            return None, None

    def get_coach_championship_statistics(self, dataset_name):
        if dataset_name in self.coach_championships_data_sets:
            data = self.coach_championships_data_sets[dataset_name]
            mean = np.mean(data)
            std_dev = np.std(data)
            return mean, std_dev
        else:
            return None, None

    def plot_coach_win_loss_ratio_distribution(self, dataset_name):
        if dataset_name in self.coach_win_loss_ratio_data_sets:
            data = self.coach_win_loss_ratio_data_sets[dataset_name]
            plt.hist(data, bins=30, edgecolor='black')
            plt.title(f'{dataset_name} Coach Win Loss Ratio Data Distribution')
            plt.xlabel('Win Loss Ratio')
            plt.ylabel('Frequency')
            plt.show()
        else:
            print(f'Dataset "{dataset_name}" not found.')

    def plot_coach_championships_distribution(self, dataset_name):
        if dataset_name in self.coach_championships_data_sets:
            data = self.coach_championships_data_sets[dataset_name]
            plt.hist(data, bins=30, edgecolor='black')
            plt.title(f'{dataset_name} Coach Championships Data Distribution')
            plt.xlabel('Number of Championships Won')
            plt.ylabel('Frequency')
            plt.show()
        else:
            print(f'Dataset "{dataset_name}" not found.')

    def process_seasons_data(self, teams):
        """
        This function takes the data at the end of a simulation and adds it to the data sets

        Parameters
        ----------
        teams : List of Team objects

        Returns
        -------
        None.

        """
        for teamx in teams:
            w = teamx.get_coach_career_wins()
            l = teamx.get_coach_career_losses()
            c = teamx.get_coach_championships()
            self.add_coach_championships_data_point(teamx.get_coach_win_probability(), c)
            self.add_coach_win_loss_ratio_data_point(teamx.get_coach_win_probability(), w/l)
                   
        
    def simulate_seasons(self, teams, n, games_per_season):
        """
        Simulates multiple seasons of games.
    
        Parameters:
        teams: array of Team objects that are in the league to be simulated
        n (int): The number of seasons to simulate.
        games_per_season (int): The number of games played per season.
    
        Returns:
        None
        
        Modifies:
            Each team in teams is modified based on simulation
            Statistics are collected for each season in:
                self.coach_win_loss_ratio_data_sets
                self.coach_championships_data_sets
        """
        
        for season in range(0, n):
            # reset wins and losses for next season
            for teamx in teams:
                teamx.set_wins(0)
                teamx.set_losses(0)
    
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

        self.process_seasons_data(teams)
        
    
            
            
# Simulation Constants
TYPICAL_COACH_WIN_PROBABILITY = 0.45
SUPERIOR_COACH_WIN_PROBABILITY = 0.55
NUMBER_OF_TEAMS = 32
GAMES_PER_SEASON = 16
NUMBER_OF_SEASONS = 10
TOL = 0.0001
PLAYOFF_TEAMS = 4
SIM_ITERATIONS = 1000


sim = MonteCarloSimulator()

for x in range(0,SIM_ITERATIONS):
    # Create teams with random coach IDs and win probabilities
    teams = [team.Team(coach_id=i, win_probability=TYPICAL_COACH_WIN_PROBABILITY) for i in range(1, NUMBER_OF_TEAMS+1)]
    next_coach_id = NUMBER_OF_TEAMS + 1
    
    # Choose 1 coach to be superior to the rest
    teams[0].set_coach_win_probability(SUPERIOR_COACH_WIN_PROBABILITY)

    sim.simulate_seasons(teams, NUMBER_OF_SEASONS, GAMES_PER_SEASON)
    
    print("")
    print(f"Iteration {x+1}: Summary Results for {NUMBER_OF_SEASONS} Seasons")
    for teamx in teams:
        print(f"Team: {teamx.get_team_name()}, Championships: {teamx.get_team_championships()}, Coach Win Probability: {teamx.get_coach_win_probability()}")
    


# Print statistics from simulation runs
print("")
print("-------------------------")
print("Win Loss Ratio Statistics")
mean, std_dev = sim.get_coach_win_loss_ratio_statistics(TYPICAL_COACH_WIN_PROBABILITY)
print(f'Typyical Coach - Mean: {mean}, Standard Deviation: {std_dev}')
mean, std_dev = sim.get_coach_win_loss_ratio_statistics(SUPERIOR_COACH_WIN_PROBABILITY)
print(f'Superior Coach - Mean: {mean}, Standard Deviation: {std_dev}')
print("")
print("Championship Statistics")
mean, std_dev = sim.get_coach_championship_statistics(TYPICAL_COACH_WIN_PROBABILITY)
print(f'Typyical Coach - Mean: {mean}, Standard Deviation: {std_dev}')
mean, std_dev = sim.get_coach_championship_statistics(SUPERIOR_COACH_WIN_PROBABILITY)
print(f'Superior Coach - Mean: {mean}, Standard Deviation: {std_dev}')

# Plot distributions from simulation runs
sim.plot_coach_win_loss_ratio_distribution(TYPICAL_COACH_WIN_PROBABILITY)
sim.plot_coach_win_loss_ratio_distribution(SUPERIOR_COACH_WIN_PROBABILITY)
sim.plot_coach_championships_distribution(TYPICAL_COACH_WIN_PROBABILITY)
sim.plot_coach_championships_distribution(SUPERIOR_COACH_WIN_PROBABILITY)
