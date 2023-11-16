from yahoo_fin import options, stock_info
import pandas as pd
from datetime import datetime
import numpy as np
import math
import scipy.stats as stats

def get_option_chain(ticker, expiration_date=None):
    option_chain = options.get_calls(ticker, expiration_date)
    return option_chain

def main():
    ticker = input("Enter the stock ticker: ")
    expiration_date = input("Enter the expiration date (optional): ")

    # Default to the next available expiration date if not specified
    if not expiration_date:
        expiration_date = None

    calloptions = get_option_chain(ticker, expiration_date)
    stockprice = stock_info.get_live_price(ticker)
    diff_in_days = (datetime.strptime(expiration_date, "%Y-%m-%d") - datetime.now()).days
    impVol_string = calloptions['Implied Volatility'].str.replace('%', '')
    impVol = impVol_string.astype(float) / 100

    S = stockprice
    K = calloptions['Strike']
    T = diff_in_days / 365
    r = 0.0453
    d = 0
    sigma = 0.704
    d1 = (np.log(S / K) + (((r - d) + ((sigma ** 2) / 2)) * T)) / (sigma * np.sqrt(T))
    delta = np.exp(-1 * d * T) * stats.norm.cdf(d1)

    downsideprotection = (1 - ((stockprice - calloptions['Bid']) / stockprice))
    roi = ((calloptions['Strike'] - stockprice + calloptions['Bid']) / stockprice)
    
    columns = {'contractSymbol': calloptions['Contract Name'], 'stockPrice': stockprice, 'strike': calloptions['Strike'], 'bid': calloptions['Bid'], 'impVol': impVol, 'delta': delta, 'downsideProtection': downsideprotection  * 100, 'returnIfCalled': roi * 100}
    screener = pd.DataFrame(data = columns)

    print(screener)


if __name__ == "__main__":
    main()