import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.filters.hp_filter import hpfilter

def growth(x):
    x_growth = np.log(x).diff(4) 
    return x_growth

def hp_filter(x):
    cycle = np.ones_like(x)
    cycle[np.isnan(x)] = np.nan
    cycle[~np.isnan(x)] = hpfilter(x[~np.isnan(x)])[0]
    return cycle

def linear_cycle(y):
    y = np.log(y)
    x = np.ones((len(y), 2))
    x[:, 0] = 1
    x[:, 1] = np.arange(len(y))

    model = sm.OLS(y, x).fit()
    trend = model.predict(x)
    cycle = y - trend
    return cycle

def quad_cycle(y):
    x = np.ones((len(y), 3))
    x[:, 0] = 1
    x[:, 1] = np.arange(len(y))
    x[:, 2] = np.arange(len(y))**2

    model = sm.OLS(y, x).fit()
    trend = model.predict(x)
    cycle = y - trend
    return cycle

