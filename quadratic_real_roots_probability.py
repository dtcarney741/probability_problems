# -*- coding: utf-8 -*-
"""
Spyder Editor

A First Course in Stochastic Processes, Samuel Karlin, 1966
    Chapter 1, problem 1, page 21
        Find the probability that a quadratic equation has real roots with 
        each coefficient (a,b,c) randomly distributed between 0 and 1
"""

import random

def random_number_between(x, y):
    """
    Returns a random number between x (inclusive) and y (inclusive).
    """
    return random.uniform(x, y)


RANGE_LOW = 0
RANGE_HIGH = 1
NUM_ITERATIONS = 1000000

real_root_count = 0

for i in range(NUM_ITERATIONS):
    a = random_number_between(RANGE_LOW, RANGE_HIGH)
    b = random_number_between(RANGE_LOW, RANGE_HIGH)
    c = random_number_between(RANGE_LOW, RANGE_HIGH)
    
    b_squared = b**2
    four_ac = 4*a*c
    
    if (b_squared >= four_ac):
        real_root_count = real_root_count + 1
        
        
print("Probability of Real Roots = ", real_root_count/NUM_ITERATIONS)