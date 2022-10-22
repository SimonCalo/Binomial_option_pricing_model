This is the most common setup for binomial pricing, where the price of the stock changes with a certain percentage change compared to its current price at every time step. This corresponds to the model presented in the Investopedia article linked at the beginning.

I present here two different algorithms to obtain the price for an option via the binomial model. The first approach (simply called "Price calculator") is a clearer one, where it is easier for novices to understand and follow the logic, since it is quite close to the one presented in the Investopedia article.
The second method (called "Efficient price calculator") is more efficient, and it requires a single loop to perform the calculation. In more technical terms, this second method only runs in O(n_intervals + 1) time, while the other method takes more than twice as long. This method, however, requires a deeper understanding of combinatorics and simple maths to be understood in full detail. This second method is essentially the one that can be found [in this article](https://www.codearmo.com/python-tutorial/options-trading-binomial-pricing-model) that I also linked previously.



