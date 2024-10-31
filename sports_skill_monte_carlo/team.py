# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 22:32:30 2024

@author: carne
"""

# List of unique animal names
animal_names = [
    "Lions", "Tigers", "Bears", "Wolves", "Eagles", "Sharks", "Panthers", "Leopards",
    "Falcons", "Hawks", "Cheetahs", "Jaguars", "Pumas", "Cougars", "Lynxes", "Ocelots",
    "Foxes", "Raccoons", "Otters", "Beavers", "Bison", "Antelopes", "Camels", "Caribou",
    "Chinchillas", "Coyotes", "Dingos", "Dolphins", "Elephants", "Elk", "Ferrets",
    "Gazelles", "Giraffes", "Gorillas", "Hippopotami", "Hyenas", "Ibexes", "Iguanas",
    "Kangaroos", "Koalas", "Lemurs", "Llamas", "Meerkats", "Moose", "Orangutans",
    "Pandas", "Penguins", "Porcupines", "Rhinoceri", "Seals", "Walruses", "Zebras"
]


class Team:
    team_name_index = 0   # Class variable to keep track of the next animal name to assign
    
    def __init__(self, coach_id, win_probability):
        self.team_name = animal_names[Team.team_name_index]
        self.coach_id = coach_id
        self.coach_win_probability = win_probability
        self.wins = 0
        self.losses = 0
        self.coach_career_wins = 0
        self.coach_career_losses = 0
        self.losing_seasons = 0
        self.team_championships = 0
        self.coach_championships = 0
        if Team.team_name_index == len(animal_names)-1:
            Team.team_name_index = 0
        else:
            Team.team_name_index += 1

    def get_team_name(self):
        return self.team_name

    def get_coach_id(self):
        return self.coach_id

    def get_coach_win_probability(self):
        return self.coach_win_probability
        
    def set_coach_win_probability(self, new_probability):
        self.coach_win_probability = new_probability
        
    def get_wins(self):
        return self.wins

    def get_losses(self):
        return self.losses

    def get_coach_career_wins(self):
        return self.coach_career_wins

    def get_coach_career_losses(self):
        return self.coach_career_losses

    def get_coach_championships(self):
        return self.coach_championships
    
    def get_team_championships(self):
        return self.team_championships

    def set_wins(self, wins):
        self.wins = wins

    def set_losses(self, losses):
        self.losses = losses
        
    def increment_wins(self):
        self.wins = self.wins + 1
        self.coach_career_wins = self.coach_career_wins + 1
        
    def increment_losses(self):
        self.losses = self.losses + 1
        self.coach_career_losses = self.coach_career_losses + 1
        
    def get_losing_seasons(self):
        return self.losing_seasons
    
    def increment_losing_seasons(self):
        self.losing_seasons = self.losing_seasons + 1
        
    def won_championship(self):
        self.coach_championships = self.coach_championships + 1
        self.team_championships = self.team_championships + 1
    
    def new_coach(self, coach_id):
        self.coach_id = coach_id
        self.losing_seasons = 0
        self.coach_championships = 0
        self.coach_career_wins = 0
        self.coach_career_losses = 0
