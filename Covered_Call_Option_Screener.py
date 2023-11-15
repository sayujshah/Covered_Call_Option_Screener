from yahoo_fin import options, stock_info
import pandas as pd

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

    downsideprotection = (1 - ((stockprice - calloptions['Bid']) / stockprice))
    roi = ((calloptions['Strike'] - stockprice + calloptions['Bid']) / stockprice)
    
    columns = {'contractSymbol': calloptions['Contract Name'], 'stockPrice': stockprice, 'strike': calloptions['Strike'], 'bid': calloptions['Bid'], 'impVol': calloptions['Implied Volatility'], 'downsideProtection': downsideprotection  * 100, 'returnIfCalled': roi * 100}
    screener = pd.DataFrame(data = columns)

    print(screener)


if __name__ == "__main__":
    main()