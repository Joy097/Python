import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

ticker_symbol = 'SPY'
tickerdata = yf.Ticker(ticker_symbol)
tickerDf = tickerdata.history(period='1d', start='2018-1-1', end='2020-1-1')
tickerDf = tickerDf[['Close']]

plt.figure(figsize=(10,4))
plt.plot(tickerDf.Close)
plt.title('Stock Price over Time (%s)'%ticker_symbol, fontsize=20)
plt.ylabel('Price', fontsize=16)
plt.savefig('plot1.png')

#try to make stationary
first_diffs = tickerDf.Close.values[1:] - tickerDf.Close.values[:-1]
first_diffs = np.concatenate([first_diffs, [0]])

tickerDf['Diff'] = first_diffs
print(tickerDf.head())
