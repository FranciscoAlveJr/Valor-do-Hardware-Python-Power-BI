import yfinance as yf

def acoes(ticker):
    df = yf.Ticker(ticker).history('1y')
    df.reset_index(inplace=True)
    df['ticker'] = ticker.split('.')[0]
    return df

intel = acoes('INTC')
amd = acoes('AMD')
nvidea = acoes('NVDA')

nvidea.head()
amd.head()
intel.head()