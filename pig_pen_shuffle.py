# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 00:38:07 2024

Integrated Alegebra and Trigonometry, Fisher and Ziebur, 1958
    Chapter 8, problem 7, page 335
        A pig pen is divided into 4 sections, say A, B, C, and D. In the evening
        the farmer places 3 black pigs and 2 red pigs in each section. During
        the night 1 pig in pen A gets into pen B. Then 1 pig in pen B escapes to
        pen C, and in succession a pig goes from pen C to D, and one goes from
        pen D to pen A. What is the probability that after the exchange the
        color distribution of pigs in each section will be the same as it was
        originally?
        
@author: David Carney
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
WITH_MIXING = True                 # True if pigs from the previous pen are included in the selection of pigs that can leave the pen

same_config_count = 0
pen_A_same_config_count = 0
pen_B_same_config_count = 0
pen_C_same_config_count = 0
pen_D_same_config_count = 0

for i in range(NUM_ITERATIONS):
    # Instantiate pig pens
    pen_A = PigPen(NUM_BROWN_PIGS, NUM_RED_PIGS)
    pen_B = PigPen(NUM_BROWN_PIGS, NUM_RED_PIGS)
    pen_C = PigPen(NUM_BROWN_PIGS, NUM_RED_PIGS)
    pen_D = PigPen(NUM_BROWN_PIGS, NUM_RED_PIGS)

    if WITH_MIXING == False:
        pig_AtoB = pen_A.select_pig_to_leave()
        pig_BtoC = pen_B.select_pig_to_leave()
        pig_CtoD = pen_C.select_pig_to_leave()
        pig_DtoA = pen_D.select_pig_to_leave()
    
        pen_A.pig_enters(pig_DtoA)
        pen_B.pig_enters(pig_AtoB)
        pen_C.pig_enters(pig_BtoC)
        pen_D.pig_enters(pig_CtoD)
    else:
        pig_AtoB = pen_A.select_pig_to_leave()
        pen_B.pig_enters(pig_AtoB)
        pig_BtoC = pen_B.select_pig_to_leave()
        pen_C.pig_enters(pig_BtoC)
        pig_CtoD = pen_C.select_pig_to_leave()
        pen_D.pig_enters(pig_CtoD)
        pig_DtoA = pen_D.select_pig_to_leave()
        pen_A.pig_enters(pig_DtoA)
        

    if (pen_A.compare_pig_counts(NUM_BROWN_PIGS, NUM_RED_PIGS) and 
        pen_B.compare_pig_counts(NUM_BROWN_PIGS, NUM_RED_PIGS) and
        pen_C.compare_pig_counts(NUM_BROWN_PIGS, NUM_RED_PIGS) and
        pen_D.compare_pig_counts(NUM_BROWN_PIGS, NUM_RED_PIGS)):
            same_config_count = same_config_count + 1
            
    if pen_A.compare_pig_counts(NUM_BROWN_PIGS, NUM_RED_PIGS):
        pen_A_same_config_count = pen_A_same_config_count + 1
        
    if pen_B.compare_pig_counts(NUM_BROWN_PIGS, NUM_RED_PIGS):
        pen_B_same_config_count = pen_B_same_config_count + 1

    if pen_C.compare_pig_counts(NUM_BROWN_PIGS, NUM_RED_PIGS):
        pen_C_same_config_count = pen_C_same_config_count + 1

    if pen_D.compare_pig_counts(NUM_BROWN_PIGS, NUM_RED_PIGS):
        pen_D_same_config_count = pen_D_same_config_count + 1

            
print("probability of same pen configuration after moves = ", same_config_count/NUM_ITERATIONS)
print("probability of pen A same configuration after moves = ", pen_A_same_config_count/NUM_ITERATIONS)
print("probability of pen B same configuration after moves = ", pen_B_same_config_count/NUM_ITERATIONS)
print("probability of pen C same configuration after moves = ", pen_C_same_config_count/NUM_ITERATIONS)
print("probability of pen D same configuration after moves = ", pen_D_same_config_count/NUM_ITERATIONS)
