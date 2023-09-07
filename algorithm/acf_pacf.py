import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
register_matplotlib_converters()
df_ice_cream = pd.read_csv('ice_cream.csv')


df_ice_cream.rename(columns={'DATE':'date','IPN31152N':'production'}, inplace=True)
df_ice_cream['date'] = pd.to_datetime(df_ice_cream.date)
df_ice_cream.set_index('date', inplace=True)
start_date = pd.to_datetime('2010-01-01')
df_ice_cream = df_ice_cream[start_date:]

plt.figure(figsize=(10,4))
plt.plot(df_ice_cream.production)
plt.title('Ice-cream production', fontsize=20)
plt.ylabel('Production', fontsize = 16)