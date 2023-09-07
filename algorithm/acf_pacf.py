import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
register_matplotlib_converters()
df_ice_cream = pd.read_csv('ice_cream.csv')
print(df_ice_cream.head())

df_ice_cream.renmae(columns={'DATE':'date','IPN31152N':'production'}, inplace=True)
df_ice_cream['date'] = pd.to_datetime(df_ice_cream.date)
