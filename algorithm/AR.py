import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import datetime
from datetime import timedelta
from pandas.plotting import register_matplotlib_converters
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARMA
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
model = ARMA(train_data, order=(3,0))
