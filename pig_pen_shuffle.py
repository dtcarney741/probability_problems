# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 00:38:07 2024

@author: carne
"""

import random

class PigPen:
    def __init__(self, num_brown_pigs, num_red_pigs):
        self.brown_pigs = num_brown_pigs
        self.red_pigs = num_red_pigs

    def pig_enters(self, pig):
        if pig == "brown":
            self.brown_pigs = self.brown_pigs + 1
        elif pig == "red":
            self.red_pigs = self.red_pigs + 1
        else:
            raise Exception("Invalid pig")
           
    def select_pig_to_leave(self):
        total_pigs = self.brown_pigs + self.red_pigs
        if total_pigs == 0:
            return None  # No pigs in the pen
        choice =random.choice(["brown" for _ in range(self.brown_pigs)] +
                            ["red" for _ in range(self.red_pigs)])
                            
        if choice == "brown":
            self.brown_pigs = self.brown_pigs - 1
        else:
            self.red_pigs = self.red_pigs - 1

        return(choice)

    def compare_pig_counts(self, brown_count, red_count):
        if self.brown_pigs == brown_count and self.red_pigs == red_count:
            return(True)
        else:
            return(False)
    
    
NUM_BROWN_PIGS = 3
NUM_RED_PIGS = 2
NUM_ITERATIONS = 1000000

same_config_count = 0
for i in range(NUM_ITERATIONS):
    # Instantiate pig pens
    pen_A = PigPen(NUM_BROWN_PIGS, NUM_RED_PIGS)
    pen_B = PigPen(NUM_BROWN_PIGS, NUM_RED_PIGS)
    pen_C = PigPen(NUM_BROWN_PIGS, NUM_RED_PIGS)
    pen_D = PigPen(NUM_BROWN_PIGS, NUM_RED_PIGS)

    pig_AtoB = pen_A.select_pig_to_leave()
    pig_BtoC = pen_B.select_pig_to_leave()
    pig_CtoD = pen_C.select_pig_to_leave()
    pig_DtoA = pen_D.select_pig_to_leave()
    
    pen_A.pig_enters(pig_DtoA)
    pen_B.pig_enters(pig_AtoB)
    pen_C.pig_enters(pig_BtoC)
    pen_D.pig_enters(pig_CtoD)

    if (pen_A.compare_pig_counts(NUM_BROWN_PIGS, NUM_RED_PIGS) and 
        pen_B.compare_pig_counts(NUM_BROWN_PIGS, NUM_RED_PIGS) and
        pen_C.compare_pig_counts(NUM_BROWN_PIGS, NUM_RED_PIGS) and
        pen_D.compare_pig_counts(NUM_BROWN_PIGS, NUM_RED_PIGS)):
            same_config_count = same_config_count + 1
            
print("probability of same pen configuration after moves = ", same_config_count/NUM_ITERATIONS)