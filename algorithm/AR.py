import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import datetime
from datetime import datetime
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
production_ice_cream=production_ice_cream.asfreq(pd.infer_ferq(production_ice_cream.index))

start_date = pd.to_datetime('2010-01-01')
production_ice_cream = production_ice_cream[s]