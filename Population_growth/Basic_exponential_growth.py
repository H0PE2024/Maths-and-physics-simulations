import numpy as np
import matplotlib.pyplot as plt

# Define the exponential growth function
def exponential_growth(P0, r, t):
    return P0 * np.exp(r * t)

# Parameters
P0 = 100  # Initial population
r = 0.1   # Growth rate
t = np.linspace(0, 50, 500)  # Time from 0 to 50

# Calculate population over time
population = exponential_growth(P0, r, t)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t, population, label=f'Growth rate (r) = {r}')
plt.title('Exponential Growth Over Time')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.show()
