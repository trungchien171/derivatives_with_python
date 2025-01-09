# Plot how the option price changes with varying levels of volatility or time to maturity

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.family'] = 'serif'

# Import Valuation Function from Chapter 5
import sys
sys.path.append('05_com')
from BSM_option_valuation import BSM_call_value, BSM_put_value

# Parameters
St = 100  # Current stock price
K = 105   # Strike price
t = 0     # Valuation date
T = 1.0   # Time to maturity (1 year)
r = 0.05  # Risk-free rate

# Varying Volatility
volatility = np.linspace(0.01, 1.0, 100)  # Volatility range from 1% to 100%
call_prices = [BSM_call_value(St, K, t, T, r, vol) for vol in volatility]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(volatility, call_prices, label='Call Option Price', color='blue')
plt.title('Option Price vs. Volatility')
plt.xlabel('Volatility (σ)')
plt.ylabel('Call Option Price')
plt.grid(True)
plt.legend()
plt.show()