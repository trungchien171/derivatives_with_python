# Modify the script to handle different strike prices and underlying asset levels

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.family'] = 'serif'

# Import Valuation Function from Chapter 5
import sys
sys.path.append('05_com')
from BSM_option_valuation import BSM_put_value

# Model and Option Parameters
strike_prices = [7500, 8000, 8500]  # list of strike prices
T = 1.0   # time-to-maturity
r = 0.025 # risk-free rate
vol = 0.2 # volatility

# Define the range of index levels dynamically
min_S = 4000  # minimum index level
max_S = 12000 # maximum index level
step_S = 150  # number of points in the range
S = np.linspace(min_S, max_S, step_S)

# Graphical Output
plt.figure()

for K in strike_prices:
    h = np.maximum(K - S, 0)
    C = [BSM_put_value(S0, K, 0, T, r, vol) for S0 in S]

    # plot inner value
    plt.plot(S, h, linestyle='-.', linewidth=1.5, label=f'Inner Value (K={K})')

    # Plot Present Value
    plt.plot(S, C, linewidth=2, label=f'Present Value (K={K})')

# Add Strike Price Lines
for K in strike_prices:
    plt.axvline(K, color='gray', linestyle='--', linewidth=1, label=f'Strike Price K={K}')

plt.grid(True)
plt.legend(loc='best')
plt.xlabel('Index Level $S_0$')
plt.ylabel('Value')
plt.title('European Put Option Value Plot for Multiple Strike Prices')
plt.show()