# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 21:39:52 2024

@author: carne
"""
USE_DECIMAL = False

import decimal
import matplotlib.pyplot as plt
import numpy as np


# Set the precision for the decimal calculations (e.g., 50 digits)
decimal.getcontext().prec = 100

def birthday_probability_method2(n):
    # This method came from AI (both ChatGPT on the open internet and the private AI engine at Sierra Space)
    # The AI tried to explain it in terms of probability reasoning, but it didn't really make sense
    # It turns out that the math in this method exactly matches the explanation in Aiden's probability text book
    # but is performed in a different way. I have confirmed this in Excel
    
    # Total number of possible birthdays (365 days in a year)
    if USE_DECIMAL:
        total_days = decimal.Decimal(365)
        
        # Initialize the probability that no two people share the same birthday (as 1)
        prob_no_shared = decimal.Decimal(1)
        
        one = decimal.Decimal(1)
    else:
        total_days = 365
        
        # Initialize the probability that no two people share the same birthday (as 1)
        prob_no_shared = 1
        
        one = 1
        
    
    # Calculate the probability that no two people share the same birthday
    for i in range(n):
        prob_no_shared *= (total_days - i) / total_days
    
    # The probability that at least two people share the same birthday
    prob_shared = one - prob_no_shared
    
    return prob_shared


def birthday_probability_method1(n):
    # This method came from a google search - it appears to be an approximation and not correctly rooted in probability theory
    # At first reading, it appeared to be valid probability reasoning
    if USE_DECIMAL:
        # Total number of possible birthdays (365 days in a year)
        total_days = decimal.Decimal(365)
        
        # Total number of possible birthdays that aren't the same in a group of 2 people
        not_shared = decimal.Decimal(364)

        one = decimal.Decimal(1)
    else:
        # Total number of possible birthdays (365 days in a year)
        total_days = 365
        
        # Total number of possible birthdays that aren't the same in a group of 2 people
        not_shared = 364

        one = 1
        
        
    # combinations of 2 people in n
    if USE_DECIMAL:
        c = decimal.Decimal(n*(n-1)/2)
    else:
        c = n*(n-1)/2

    p = (not_shared/total_days)**c
    
    prob_shared = one - p
    
    return prob_shared


def birthday_probability_method3(n):
    # This is the exact calculation method from Aiden's probability text book based on probability theory.
    # It is mathematically identical to method 1, though calculated in a slightly different order.
    
    if USE_DECIMAL:
        total_days = decimal.Decimal(365)
        
        # Initialize the probability that no two people share the same birthday (as 1)
        prob_no_shared = decimal.Decimal(1)
        
        one = decimal.Decimal(1)
    else:
        total_days = 365
        
        # Initialize the probability that no two people share the same birthday (as 1)
        prob_no_shared = 1
        
        one = 1
        
    multiplier = total_days
    for i in range(n):
        prob_no_shared *= multiplier
        multiplier = multiplier - one
        
    prob_no_shared = prob_no_shared / (total_days**n)
    prob_shared = one - prob_no_shared
    
    return prob_shared
        
        
def birthday_probability_method4(n):
    # This method came from Aiden's probability text book and is a simple approximation of the exact answer
    # It almost exactly matches the approximation of method 2 from the google search in result, but is different in
    # math operations
    if USE_DECIMAL:
        # Total number of possible birthdays (365 days in a year)
        total_days = decimal.Decimal(365)
        
        one = decimal.Decimal(1)
        
    else:
        # Total number of possible birthdays (365 days in a year)
        total_days = 365
        
        one = 1
        
    p = np.exp(-n*(n-1)/(2*total_days))

    prob_shared = one - p
    
    return prob_shared

# Example usage
method1 = []
method2 = []
method3 = []
method4 = []
for n in range(2,365):
    p = birthday_probability_method1(n)
    method1.append(p)
    p = birthday_probability_method2(n)
    method2.append(p)
    p = birthday_probability_method3(n)
    method3.append(p)
    p = birthday_probability_method4(n)
    method4.append(p)


error12 = [i - j for i, j in zip(method1, method2)]
error42 = [i - j for i, j in zip(method4, method2)]
error32 = [i - j for i, j in zip(method3, method2)]

# Plotting the data using matplotlib
plt.figure(figsize=(10, 6))
plt.plot(range(2, 365), method1, label="Method 1", color="blue")
plt.plot(range(2, 365), method2, label="Method 2", color="red", linestyle='--')
plt.plot(range(2, 365), method3, label="Method 3", color="green", linestyle='--')
plt.plot(range(2, 365), method4, label="Method 4", color="orange", linestyle='-')


plt.title("Birthday Paradox: Comparison of Method 1 and Method 2")
plt.xlabel("Number of People (n)")
plt.ylabel("Probability of at least one shared birthday")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(range(2, 365), error12, label="error12", color="red", linestyle='--')
plt.scatter(range(2, 365), error32, label="error32", color="blue", linestyle='--')
plt.scatter(range(2, 365), error42, label="error42", color="green", linestyle='--')
plt.grid(True)
plt.show()
