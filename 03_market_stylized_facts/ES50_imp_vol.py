import numpy as np
import pandas as pd
from BSM_imp_vol import call_option
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.family'] = 'serif'

# Pricing Data
pdate = pd.Timestamp('2014-09-30')

#
# EURO STOXX 50 index data
#

# URL of data file
es_url = './03_market_stylized_facts/hbrbcpe.txt'
# column names to be used

cols = ['Date', 'SX5P', 'SX5E', 'SXXP', 'SXXE', 'SXXF', 'SXXA', 'DK5F', 'DKXF', 'DEL']

# reading the data with pandas
es = pd.read_csv(
    es_url,  # filename
    header=None,  # ignore header row
    index_col=0,  # index column (dates)
    parse_dates=True,  # parse these dates
    dayfirst=True,  # day before month
    skiprows=4,  # skip first 4 rows
    sep=';',  # data separator
    names=cols  # use these column names
)

# deleting the helper column
del es['DEL']
S0 = es['SX5E']['2014-09-30']
r = -0.05

#
# Option Data
#

data = pd.HDFStore('./03_market_stylized_facts/es50_option_data.h5', 'r')['data']

#
# BSM Implied Volatilities
#

def calculate_imp_vols(data):
    ''' Calculate all implied volatilities for the European call options
    given the tolerance level for moneyness of the option.'''
    data['Imp_Vol'] = np.nan
    tol = 0.30  # tolerance level for moneyness
    for row in data.index:
        t = data['Date'][row]
        T = data['Maturity'][row]
        ttm = (T - t).days / 365.
        forward = np.exp(r * ttm) * S0
        if (abs(data.loc[row, 'Strike'] - forward) / forward) < tol:
            call = call_option(S0, data.loc[row, 'Strike'], t, T, r, 0.2)
            imp_vol = call.imp_vol(data.loc[row, 'Call'])
            data.loc[row, 'Imp_Vol'] = imp_vol
    return data

#
# Graphical output
#

markers = ['.', 'o', '^', 'v', 'x', 'D', 'd', '>', '<']
def plot_imp_vols(data):
    ''' Plot the iv'''
    maturities = sorted(set(data['Maturity']))
    plt.figure(figsize=(10, 5))
    
    for i, mat in enumerate(maturities):
        dat = data[(data['Maturity'] == mat) & (data['Imp_Vol'] > 0)]
        plt.plot(dat['Strike'].values, dat['Imp_Vol'].values,
                 'b%s' % markers[i], label=str(mat)[:10])
    plt.grid(True)
    plt.legend()
    plt.xlabel('strike')
    plt.ylabel('implied volatility')
    plt.title('Implied Volatilities')
    plt.show()

if __name__ == '__main__':
    data = calculate_imp_vols(data)
    plot_imp_vols(data)

