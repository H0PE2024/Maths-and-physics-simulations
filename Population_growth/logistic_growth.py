import numpy as np
import matplotlib.pyplot as plt

# Define the logistic growth function
def logistic_growth(P0, r, K, t):
    """
    Calculate the logistic growth of a population.

    Parameters:
    P0 : float
        Initial population size
    r : float
        Growth rate
    K : float
        Carrying capacity
    t : array-like
        Time array

    Returns:
    numpy.ndarray
        Population size at each time point
    """
    return K / (1 + (K - P0) / P0 * np.exp(-r * t))

# Parameters
P0 = 10          # Initial population
r = 0.2          # Growth rate
K = 1000         # Carrying capacity
t = np.linspace(0, 70, 500)  # Time from 0 to 50 in 500 steps

# Compute population growth
P = logistic_growth(P0, r, K, t)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t, P, label='Population Growth', color='b')
plt.title('Logistic Population Growth')
plt.xlabel('Time')
plt.ylabel('Population Size')
plt.axhline(K, color='r', linestyle='--', label='Carrying Capacity (K)')
plt.legend()
plt.grid(True)
plt.show()
