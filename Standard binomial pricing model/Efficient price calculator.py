import numpy as np
import math

def combinations(n: int, i: int) -> int:

"""
Helper function to calculate the number of combinations that can be obtained by choosing i elements out of a total of n elements. This function essentially returns n choose i.
    
Parameters:
n (int): The total number of elements to choose from.
i (int): The number of elements to be chosen from the total population of n.
    
Returns:
int: The number of combinations in which i elements can be selected from a total of n.
    
"""
    return math.factorial(n) / (math.factorial(n-i)*math.factorial(i))
    
    
def efficient_calculator(r: float, t: float, u: float, d: float, n_intervals: int, current_price: float, strike_price: float, call: bool =False) -> float:

"""
Function to calculate the price of a call or put option.

Parameters:
r (float): Risk-free interest rate.
t (float): Time to maturity/expiry of the option (in years).
u (float): By what factor the stock price can increase at each time step.
d (float): By what factor the stock price can decrease at each time step.
n_intervals (int): The amount of time intervals before expiry of the option.
current_price (float): The price of the stock at t=0.
strike_price (float): The strike price of the stock.
call (bool): Whether the option is a call option (True), or a put option (False, which is the default value).

Returns:
float: The calculated price for the option.
"""

  # Initialise useful quantities
  delta_t = t/n_intervals
  q = (np.exp(r*delta_t) - d)/(u - d)
  value = 0

  # Loop over the possible final prices of the stock at maturity, and calculate the probability of each of those final prices using combinatorics.
  for i in range(n_intervals+1):
    node_prob = combinations(n_intervals, i)*q**i*(1-q)**(n_intervals-i)
    possible_final_price = current_price*(u)**i*(d)**(n_intervals-i)

    # Use that information to add the difference between the strike price and each possible final price to the value, scaled by the respective probability of that node.
    if call:
      value += max(possible_final_price - strike_price, 0)*node_prob
    else:
      value += max(strike_price-possible_final_price, 0)*node_prob

  # Discount by the risk-free rate of interest using the usual exponential form.
  return value*np.exp(-r*t)


# Test the calculator.
efficient_calculator(0.05, 0.75, 1.2, 0.8, 3, 10, 12)
