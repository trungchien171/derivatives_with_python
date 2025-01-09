# Implement the Black-Scholes model to compute the price of European call and put options

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.family'] = 'serif'

# Import Valuation Function from Chapter 5
import sys
sys.path.append('05_com')
from BSM_option_valuation import BSM_call_value, BSM_put_value

# Model Parameters
S = np.linspace(50, 150, 100)  # underlying asset prices
K = 100  # strike price
t = 0  # valuation date
T = 1.0  # time-to-maturity in years
r = 0.05  # risk-free interest rate
sigma = 0.2  # volatility

# Calculate Call and Put Prices
call_prices = [BSM_call_value(s, K, t, T, r, sigma) for s in S]
put_prices = [BSM_put_value(s, K, t, T, r, sigma) for s in S]

# Plot Call and Put Prices
plt.figure(figsize=(10, 6))
plt.plot(S, call_prices, label='Call Option Price', color='blue')
plt.plot(S, put_prices, label='Put Option Price', color='red')
plt.axvline(K, color='gray', linestyle='--', label='Strike Price (K)')
plt.title('Black-Scholes European Call and Put Option Prices')
plt.xlabel('Underlying Asset Price ($S_0$)')
plt.ylabel('Option Price')
plt.legend()
plt.grid(True)
plt.show()