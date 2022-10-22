def option_price_calculator(r: float, q: float, u: float, d: float, n_intervals: int, current_price: float, strike_price: float, call: bool =False) -> float:

"""
Function to calculate the price of an option.
Since the risk-free interest rate is zero, we do not carry out any of the time evolutions on the price that are done via the usual exponential factor.
This could be easily modified to include the exponential factor as seen in the other calculators.

Parameters:
r (float): Risk-free interest rate.
q (float): The probability of an up-move in the stock price.
u (float): By how much the stock can increase at each time step.
d (float): By how much the stock can decrease at each time step.
n_intervals (int): The amount of time intervals before expiry of the option.
current_price (float): The price of the stock at t=0.
strike_price (float): The strike price of the stock.
call (bool): Whether the option is a call option (True), or a put option (False, which is the default value).

Returns:
float: The calculated price for the option.
"""

  value = 0

  # Initialise an empty list that will contain all the P values related to each of the final possible stock prices.
  initial_P_list = []

  # Fill the initial P list, that will contain n_intervals+1 P values.
  for i in range(n_intervals+1):
  
    # Calculate a possible final price for the stock
    possible_final_price = current_price + i*u - (n_intervals-i)*d
    
    # Calculate the P value, depending on whether we have a call or a put option.
    if call:
      initial_P_list.append(max(possible_final_price - strike_price, 0))
    else:
      initial_P_list.append(max(strike_price-possible_final_price, 0))


  # Going back through the binomial tree, calculate all the P values at each given time interval
  # We do this by looping over the number of intervals in reverse.
  for i in range(n_intervals,0,-1):
    new_list = []
    # For each node at a given point in time, we calculate the P value based on the 2 nodes connected to it at the next time interval.
    for j in range(i):
      new_P_value = (initial_P_list[j]*(1-q) + initial_P_list[j+1]*q)
      new_list.append(new_P_value)

    # Having computed all the P values, we set this newly computed list of P values as our new starting point for the calculation at the next stage.
    initial_P_list = new_list

  # Return the final value
  return initial_P_list[0]
  
# Check the calculation for multiple strike price values.
values_list = [[80, False], [90, False], [93, False], [100, False], [100, True], [105, True], [112, True], [120, True]]
  
# Perform the calculations with the given values.
for element in values_list:
  str_price = element[0]
  call = element[1]
  option_price_calculator(0.0, 0.5, 1, 1, 20, 100, str_price, call=call)
