import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


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
plt.figure(figsize=(10,4))
plt.plot(tickerDf.Diff)
plt.title('First Difference over Time (%s)'%ticker_symbol, fontsize=20)
plt.ylabel('Price Difference', fontsize=16)
plt.savefig('plot2.png')

#ACF
acf_plot = plot_acf(tickerDf.Diff)
plt.savefig('plot3.png')

#PACF
pacf_plot = plot_pacf(tickerDf.Diff)
plt.savefig('plot4.png')