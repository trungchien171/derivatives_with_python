# Extend the Black-Scholes model to calculate and visualize option sensitivities (Delta, Gamma, Theta, Vega, and Rho)

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.stats import norm
mpl.rcParams['font.family'] = 'serif'

def d1(St, K, T, r, sigma):
    return (np.log(St / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

def d2(St, K, T, r, sigma):
    return d1(St, K, T, r, sigma) - sigma * np.sqrt(T)

# Black-Scholes Greeks
def delta(St, K, T, r, sigma, option='call'):
    if option == 'call':
        return norm.cdf(d1(St, K, T, r, sigma))
    elif option == 'put':
        return norm.cdf(d1(St, K, T, r, sigma)) - 1
    
def gamma(St, K, T, r, sigma):
    return norm.pdf(d1(St, K, T, r, sigma)) / (St * sigma * np.sqrt(T))

def theta(St, K, T, r, sigma, option='call'):
    d1_ = d1(St, K, T, r, sigma)
    d2_ = d2(St, K, T, r, sigma)
    term1 = -(St * norm.pdf(d1_) * sigma) / (2 * np.sqrt(T))
    if option == 'call':
        return term1 - r * K * np.exp(-r * T) * norm.cdf(d2_)
    elif option == 'put':
        return term1 + r * K * np.exp(-r * T) * norm.cdf(-d2_)

def vega(St, K, T, r, sigma):
    return St * norm.pdf(d1(St, K, T, r, sigma)) * np.sqrt(T)

def rho(St, K, T, r, sigma, option='call'):
    d2_ = d2(St, K, T, r, sigma)
    if option == 'call':
        return K * T * np.exp(-r * T) * norm.cdf(d2_)
    elif option == 'put':
        return -K * T * np.exp(-r * T) * norm.cdf(-d2_)
    
# Parameters
S = np.linspace(50, 150, 100)  # Range of underlying prices
K = 100  # Strike price
T = 1.0  # Time to maturity (1 year)
r = 0.05  # Risk-free rate
sigma = 0.2  # Volatility

# Calculate Greeks
delta_values = [delta(s, K, T, r, sigma, option='call') for s in S]
gamma_values = [gamma(s, K, T, r, sigma) for s in S]
theta_values = [theta(s, K, T, r, sigma, option='call') for s in S]
vega_values = [vega(s, K, T, r, sigma) for s in S]
rho_values = [rho(s, K, T, r, sigma, option='call') for s in S]

# Plot Greeks
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.plot(S, delta_values, label='Delta', color='blue')
plt.title('Delta')
plt.xlabel('Underlying Price')
plt.ylabel('Delta')
plt.grid(True)

plt.subplot(2, 3, 2)
plt.plot(S, gamma_values, label='Gamma', color='green')
plt.title('Gamma')
plt.xlabel('Underlying Price')
plt.ylabel('Gamma')
plt.grid(True)

plt.subplot(2, 3, 3)
plt.plot(S, theta_values, label='Theta', color='red')
plt.title('Theta')
plt.xlabel('Underlying Price')
plt.ylabel('Theta')
plt.grid(True)

plt.subplot(2, 3, 4)
plt.plot(S, vega_values, label='Vega', color='purple')
plt.title('Vega')
plt.xlabel('Underlying Price')
plt.ylabel('Vega')
plt.grid(True)

plt.subplot(2, 3, 5)
plt.plot(S, rho_values, label='Rho', color='brown')
plt.title('Rho')
plt.xlabel('Underlying Price')
plt.ylabel('Rho')
plt.grid(True)

plt.tight_layout()
plt.show()
