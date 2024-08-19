import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define the time range for the simulation
t = np.linspace(0, 20, 500)  # Time from 0 to 20 units

# Exponential Growth Model
def exponential_growth(P, t, r):
    return r * P

# Logistic Growth Model
def logistic_growth(P, t, r, K):
    return r * P * (1 - P / K)

# Extended Logistic Growth Model with Variable Carrying Capacity
def extended_logistic_growth(P, t, r, K0, K_rate):
    K = K0 + K_rate * t  # Carrying capacity increases linearly over time
    return r * P * (1 - P / K)

# Parameters
r_exp = 0.2   # Growth rate for exponential model
r_log = 0.2   # Growth rate for logistic model
K = 100       # Carrying capacity for logistic model
K0 = 50       # Initial carrying capacity for extended model
K_rate = 2    # Rate of increase of carrying capacity
P0 = 10       # Initial population

# Solve the differential equations
P_exp = odeint(exponential_growth, P0, t, args=(r_exp,))
P_log = odeint(logistic_growth, P0, t, args=(r_log, K))
P_ext_log = odeint(extended_logistic_growth, P0, t, args=(r_log, K0, K_rate))

# Plot the individual results
plt.figure(figsize=(18, 12))

# Plot Exponential Growth
plt.subplot(2, 2, 1)
plt.plot(t, P_exp, label=f'Exponential Growth (r={r_exp})', color='blue')
plt.title('Exponential Growth Model')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.annotate('Simple model for unlimited resources\nPopulation grows exponentially', xy=(0.5, 0.5), xycoords='axes fraction',
             fontsize=10, ha='center', bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='lightblue'))

# Plot Logistic Growth
plt.subplot(2, 2, 2)
plt.plot(t, P_log, label=f'Logistic Growth (r={r_log}, K={K})', color='green')
plt.title('Logistic Growth Model')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.annotate('Improved model with limited resources\nPopulation approaches carrying capacity', xy=(0.5, 0.5), xycoords='axes fraction',
             fontsize=10, ha='center', bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='lightgreen'))

# Plot Extended Logistic Growth
plt.subplot(2, 2, 3)
plt.plot(t, P_ext_log, label=f'Extended Logistic Growth (r={r_log}, K0={K0}, K_rate={K_rate})', color='purple')
plt.title('Extended Logistic Growth Model')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.annotate('Model with variable carrying capacity\nAllows adaptation to changing environments', xy=(0.5, 0.5), xycoords='axes fraction',
             fontsize=10, ha='center', bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='purple'))

# Plot Comparison
plt.subplot(2, 2, 4)
plt.plot(t, P_exp, label=f'Exponential Growth (r={r_exp})', color='blue', linestyle='--')
plt.plot(t, P_log, label=f'Logistic Growth (r={r_log}, K={K})', color='green', linestyle='-.')
plt.plot(t, P_ext_log, label=f'Extended Logistic Growth (r={r_log}, K0={K0}, K_rate={K_rate})', color='purple')
plt.title('Comparison of Growth Models')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.annotate('Comparison of models\nShows how complexity improves realism', xy=(0.5, 0.5), xycoords='axes fraction',
             fontsize=10, ha='center', bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='lightgray'))

plt.tight_layout()
plt.show()
