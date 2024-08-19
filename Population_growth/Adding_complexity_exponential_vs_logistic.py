import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
# Extended Logistic Growth Model with Variable Carrying Capacity
def extended_logistic_growth(P, t, r, K0, K_rate):
    K = K0 + K_rate * t  # Carrying capacity increases linearly over time
    return r * P * (1 - P / K)

# Parameters for extended model
K0 = 50          # Initial carrying capacity
K_rate = 2       # Rate of increase of carrying capacity

# Solve the differential equation with extended model
P_ext_log = odeint(extended_logistic_growth, P0, t, args=(r_log, K0, K_rate))

# Plot the results with complexity
plt.figure(figsize=(10, 6))

# Plot Extended Logistic Growth
plt.plot(t, P_ext_log, label=f'Extended Logistic Growth (r={r_log}, K0={K0}, K_rate={K_rate})', color='purple')
plt.title('Extended Logistic Growth Model with Varying Carrying Capacity')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.grid(True)

plt.show()
