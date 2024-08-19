import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Parameters
r_s = 0.1  # Growth rate of sheep
K_s = 500  # Carrying capacity of sheep
alpha = 0.01  # Predation rate
beta = 0.1  # Rate of converting sheep into new wolves
delta = 0.1  # Death rate of wolves

# Predator-prey model (differential equations)
def predator_prey_model(y, t, r_s, K_s, alpha, beta, delta):
    S, W = y
    dSdt = r_s * S * (1 - S / K_s) - alpha * S * W
    dWdt = beta * alpha * S * W - delta * W
    return [dSdt, dWdt]

# Time points
t = np.linspace(0, 200, 1000)

# Create a figure with subplots
fig, axs = plt.subplots(3, 2, figsize=(10, 10))

# Plot 1: No Sheep Initially
initial_conditions_1 = [0, 50]  # S(0) = 0, W(0) = 50
solution_1 = odeint(predator_prey_model, initial_conditions_1, t, args=(r_s, K_s, alpha, beta, delta))
axs[0, 0].plot(t, solution_1[:, 0], label='Sheep Population (S)')
axs[0, 0].plot(t, solution_1[:, 1], label='Wolf Population (W)')
axs[0, 0].set_title('1) No Sheep Initially',fontsize =8)
axs[0, 0].set_xlabel('Time',fontsize = 5)
axs[0, 0].set_ylabel('Population')
axs[0, 0].legend()

# Plot 2: No Wolves Initially
initial_conditions_2 = [50, 0]  # S(0) = 50, W(0) = 0
solution_2 = odeint(predator_prey_model, initial_conditions_2, t, args=(r_s, K_s, alpha, beta, delta))
axs[0, 1].plot(t, solution_2[:, 0], label='Sheep Population (S)')
axs[0, 1].plot(t, solution_2[:, 1], label='Wolf Population (W)')
axs[0, 1].set_title('2) No Wolves Initially',fontsize =8)
axs[0, 1].set_xlabel('Time',fontsize = 5)
axs[0, 1].set_ylabel('Population')
axs[0, 1].legend()

# Plot 3: High Wolves, Low Sheep
initial_conditions_3 = [50, 200]  # S(0) = 50, W(0) = 200
solution_3 = odeint(predator_prey_model, initial_conditions_3, t, args=(r_s, K_s, alpha, beta, delta))
axs[1, 0].plot(t, solution_3[:, 0], label='Sheep Population (S)')
axs[1, 0].plot(t, solution_3[:, 1], label='Wolf Population (W)')
axs[1, 0].set_title('3) High Wolves, Low Sheep',fontsize =8)
axs[1, 0].set_xlabel('Time',fontsize = 5)
axs[1, 0].set_ylabel('Population')
axs[1, 0].legend()

# Plot 4: Low Wolves, High Sheep
initial_conditions_4 = [400, 10]  # S(0) = 400, W(0) = 10
solution_4 = odeint(predator_prey_model, initial_conditions_4, t, args=(r_s, K_s, alpha, beta, delta))
axs[1, 1].plot(t, solution_4[:, 0], label='Sheep Population (S)')
axs[1, 1].plot(t, solution_4[:, 1], label='Wolf Population (W)')
axs[1, 1].set_title('4) Low Wolves, High Sheep',fontsize =8)
axs[1, 1].set_xlabel('Time',fontsize = 5)
axs[1, 1].set_ylabel('Population')
axs[1, 1].legend()

# Plot 5: Low Wolves, Low Sheep
initial_conditions_5 = [50, 10]  # S(0) = 50, W(0) = 10
solution_5 = odeint(predator_prey_model, initial_conditions_5, t, args=(r_s, K_s, alpha, beta, delta))
axs[2, 0].plot(t, solution_5[:, 0], label='Sheep Population (S)')
axs[2, 0].plot(t, solution_5[:, 1], label='Wolf Population (W)')
axs[2, 0].set_title('5) Low Wolves, Low Sheep',fontsize =8)
axs[2, 0].set_xlabel('Time',fontsize = 5)
axs[2, 0].set_ylabel('Population')
axs[2, 0].legend()

# Hide the empty subplot in the bottom-right corner
fig.delaxes(axs[2, 1])

# Adjust layout
plt.tight_layout()
plt.show()
