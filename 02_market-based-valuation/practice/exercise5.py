# Create a function to simulate the payoff of vanilla options and compare it with exotic options like barrier or Asian options.

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.family'] = 'serif'

# Simulate Geometric Brownian Motion (GBM) paths
def simulate_gbm(S0, T, r, sigma, steps, n_paths):
    dt = T / steps
    paths = np.zeros((steps + 1, n_paths))
    paths[0] = S0
    for t in range(1, steps + 1):
        z = np.random.standard_normal(n_paths)
        paths[t] = paths[t - 1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)
    return paths

# Vanilla Option Payoff
def vanilla_call_payoff(S, K):
    return np.maximum(S - K, 0)

def vanilla_put_payoff(S, K):
    return np.maximum(K - S, 0)

# Barrier Option Payoff (Knock-Out Call)
def barrier_call_payoff(S_path, K, barrier):
    S_T = S_path[-1]
    if np.any(S_path >= barrier):
        return 0  # Knocked out
    else:
        return np.maximum(S_T - K, 0)
    
# Asian Option Payoff (Call)
def asian_call_payoff(S_path, K):
    avg_price = np.mean(S_path)
    return np.maximum(avg_price - K, 0)

# Parameters
S0 = 100  # Initial stock price
K = 105   # Strike price
T = 1.0   # Time to maturity (1 year)
r = 0.05  # Risk-free rate
sigma = 0.2  # Volatility
steps = 252  # Daily steps
n_paths = 10000  # Number of paths
barrier = 120  # Barrier level

# Simulate price paths
paths = simulate_gbm(S0, T, r, sigma, steps, n_paths)

# Payoff calculations
vanilla_call = np.mean([vanilla_call_payoff(paths[-1, i], K) for i in range(n_paths)])
barrier_call = np.mean([barrier_call_payoff(paths[:, i], K, barrier) for i in range(n_paths)])
asian_call = np.mean([asian_call_payoff(paths[:, i], K) for i in range(n_paths)])

# Display results
print(f"Vanilla Call Option Payoff: {vanilla_call:.2f}")
print(f"Barrier Call Option Payoff: {barrier_call:.2f}")
print(f"Asian Call Option Payoff: {asian_call:.2f}")

# Plot sample paths
plt.figure(figsize=(10, 6))
plt.plot(paths[:, :5])  # Plot a few sample paths
plt.axhline(barrier, color='red', linestyle='--', label='Barrier Level')
plt.title('Sample GBM Price Paths')
plt.xlabel('Time Steps')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()