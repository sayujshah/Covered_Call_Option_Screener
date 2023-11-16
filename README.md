# Covered_Call_Option_Screener
**A call option screener using Yahoo Finance**

The initial "Covered_Call_Option_Screener.py" file allows for a user to screen for any call option chain based on ticker and expiration date (optional). The screener provides the contract name, most recent stock price, strike price, bid price, implied volatility, and two custom metrics I have calculated called "Downside Protection" and "Return If Called."

Downside Protection is the biggest drop in the stock price one can endure before they begin to lose money when following a basic covered call strategy. The Return If Called is the maximum profit potential if the contract is called at the strike price the premium was sold at.

The Delta of each option contract is also calculated manually following the [Black-Scholes Model](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model)
$$d_1=\frac{\ln(\frac{S}{K}) + (((r-d) + \frac{\sigma^2}{2})\times T)}{\sigma\times\sqrt{T}}$$
$$\delta = -D\times T\times N(d_1)$$

where:

- $S$ = Stock Price
- $K$ = Strike Price
- $\sigma$ = Implied Volatility
- $T$ = Time to Expiration / 365
- $r$ = Risk-Free Rate of Return
- $d$ = Dividend Yield

$N(d_1)$ = Standard Normal Cumulative Distribution of $d_1$

**<ins>TO DO<ins>**
- Add a custom-calculated "Expected Return" column that takes Implied Volatility, Downside Protection, and Return If Called into account to find the best strike price
- Develop an automated process that searches through a database of stock tickers to find optimal call options based on Expected Value for a covered call trading strategy
