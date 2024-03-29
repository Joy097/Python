import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import datetime
from datetime import timedelta
from pandas.plotting import register_matplotlib_converters
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
register_matplotlib_converters()
from time import time

def parser(s):
    return datetime.strptime(s, '%Y-%m-%d')
production_ice_cream = pd.read_csv('ice_cream.csv', parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
production_ice_cream.rename('production', inplace=True)
print(production_ice_cream)
production_ice_cream=production_ice_cream.asfreq(pd.infer_freq(production_ice_cream.index))

start_date = pd.to_datetime('2010-01-01')
production_ice_cream = production_ice_cream[start_date:]

plt.figure(figsize=(10,4))
plt.plot(production_ice_cream)
plt.title('Ice-cream production', fontsize=20)
plt.ylabel('Production', fontsize = 16)
plt.savefig('figures/AR.png')

#ACF
acf_plot = plot_acf(production_ice_cream, lags=100)
plt.savefig('figures/AR_acf.png')  

#PACF
pacf_plot = plot_pacf(production_ice_cream)
plt.savefig('figures/AR_pacf.png') 

train_end = datetime(2018,12,1)
test_end = datetime(2019,12,1)

train_data = production_ice_cream[:train_end]
test_data = production_ice_cream[train_end+timedelta(days=1):test_end]

# train with AR
model = ARIMA(train_data, order=(3,0,0))

#fit model
model_fit = model.fit()
print(model_fit.summary())

#now the p-value close to 0 can be considered. but any lag greater than 0.5 has to be avoided
#test the test_data
pred_start_date = test_data.index[0]
pred_end_date = test_data.index[-1]

predictions = model_fit.predict(start=pred_start_date, end=pred_end_date)
residuals = test_data - predictions

plt.figure(figsize=(10,4))
plt.plot(residuals)
plt.title('Residuals from AR', fontsize=20)
plt.ylabel('Error', fontsize = 16)
plt.savefig('figures/AR_residual.png')

plt.figure(figsize=(10,4))
plt.plot(test_data)
plt.plot(predictions)
plt.legend(('Data','Predictions'),fontsize=16)
plt.title('Residuals from AR', fontsize=20)
plt.ylabel('Error', fontsize = 16)
plt.savefig('figures/AR_prediction.png')