import yfinance as yf
ticker_symbol = 'SPY'
tickerdata = yf.Ticker(ticker_symbol)
tickerDf = tickerdata.history(period='1d', start='2015-1-1', end='2020-1-1')
