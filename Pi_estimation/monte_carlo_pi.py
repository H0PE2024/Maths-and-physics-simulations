import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_pi(num_samples):
    inside_circle = 0
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []

    for _ in range(num_samples):
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)
    
    pi_estimate = 4 * inside_circle / num_samples
    
    # Plotting
    plt.figure(figsize=(8, 8))
    plt.scatter(x_inside, y_inside, color='blue', s=1, label='Inside Circle')
    plt.scatter(x_outside, y_outside, color='red', s=1, label='Outside Circle')
    circle = plt.Circle((0, 0), 1, color='black', fill=False)
    plt.gca().add_patch(circle)
    plt.title(f'Monte Carlo Estimation of Pi\nEstimated Pi = {pi_estimate:.4f}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Example usage
monte_carlo_pi(10000)
