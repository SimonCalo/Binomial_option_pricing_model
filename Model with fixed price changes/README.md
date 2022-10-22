This model differs from most models that you can find online. It is quite unusual. Rather than having changes in price at each node which depend on the price of the stock itself at that node, the changes are given by a fixed amount, not a relative one. In addition, also the probability of the stock price moving up or down does not depend on which node one is at, but it is given by a fixed value, constant for every node. These are minor modifications, but I have seen this exact model come up in Quant tests, therefore I am including it here.

As for the other cases, we create the function such that it can be used to compute the price of the option regardless of the initial price chosen, probability of up-mode, time to maturity, etc.

Here is the description of the situation used to construct this calculator.

Assume that we have a stock that is valued at $100 per share. Its movement over time can be described by the following stochastic process. At each time step, it has either moved up by $1 or down by $1, both with a risk-neutral probability of 0.5. This price process can be modeled by a recombining binomial tree. In a recombining tree the order of up and down moves is irrelevant: given a certain number of up moves and a certain number of down moves, you will end up in the same node regardless of the order in which the moves are taken. We assume that the interest rates are zero.



