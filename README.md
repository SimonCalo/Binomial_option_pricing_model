This repository contains a series of templates to calculate the price of a call or put option using the binomial pricing model. This is an extremely popular and intuitive model, often used in practice to calculate the price of an option. The models presented in this repository are based on [this article](https://www.investopedia.com/articles/investing/021215/examples-understand-binomial-option-pricing-model.asp) which explains in details various features of the binomial pricing model.
I noticed a small mistake in the above article unfortunately, which I recently reported to Investopedia. The mistake is in the sign of the exponent contained in q. For more references on how to construct a binomial option pricing model in Python (that I personally used to develop the code contained here) I recommend [this article](https://medium.com/engineer-quant/binomial-option-pricing-model-5e6b9e91c7da) and [this one](https://www.codearmo.com/python-tutorial/options-trading-binomial-pricing-model).

I included two folders containing two variations of how binomial pricing models can work. One of them, is the standard version of how this model works, where at each node, the price at the following time step is given by a percentage change of the current price (A more detailed description of this model together with Python code is contained in the folder named "Standard binomial pricing model"). The other is a variation of this model, where the change in price is given by a fixed amount (for example, 1,2,etc. $). This is contained in the folder called "Model with fixed price changes".

The two Python programs are essentially the same, up to a small difference, that in principle can be incorporated in code encompassing both methods.

In addition, the folder "Standard binomial pricing model" contains two different Python codes that both work in the same way, but one is more intuitive, while the other is less intuitive but more efficient. The same could, of course, also be applied to the code contained in "Model with fixed price changes".



