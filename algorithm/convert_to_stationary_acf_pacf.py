import yfinance as yf
import matplotlib as plt
import pandas as pd

ticker_symbol = 'SPY'
tickerdata = yf.Ticker(ticker_symbol)
tickerDf = tickerdata.history(period='1d', start='2018-1-1', end='2020-1-1')
tickerDf = tickerDf[['Close']]

plt.figure(figsize=(10,4))
plt.plot(tickerDf.Close)
plt.title('Stock Price over Time (%s)'%ticker_symbol, fontsize=20)
plt.ylabel('Price', fontsize=16)
for year in range(2015,2021):
    plt.axvline(pd.to_datetime(str(year)+'-01-01'), color='k', linestyle='--', alpha=0.2)
