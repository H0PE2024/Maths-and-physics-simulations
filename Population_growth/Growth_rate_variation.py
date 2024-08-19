import numpy as np
import matplotlib.pyplot as plt

# Define the exponential growth function
def exponential_growth(P0, r, t):
    return P0 * np.exp(r * t)

# Parameters
P0 = 100  # Initial population
growth_rates = [0.05, 0.1, 0.15]  # Different growth rates
t = np.linspace(0, 50, 500)  # Time from 0 to 50

# Plot
plt.figure(figsize=(12, 8))
for r in growth_rates:
    population = exponential_growth(P0, r, t)
    plt.plot(t, population, label=f'Growth rate (r) = {r}')

plt.title('Exponential Growth with Different Growth Rates')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.show()
