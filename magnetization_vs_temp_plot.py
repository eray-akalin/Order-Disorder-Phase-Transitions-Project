import numpy as np
import matplotlib.pyplot as plt


def initialize_grid(size):
    """Initialize the grid with random spins (+1 or -1)."""
    return np.random.choice([-1, 1], size=(size, size))


def calculate_delta_e(grid, i, j, J, H):
    """Calculate the energy change if we flip the spin at (i, j)."""
    size = grid.shape[0]
    spin = grid[i, j]
    neighbors = (
            grid[(i + 1) % size, j] +
            grid[i, (j + 1) % size] +
            grid[(i - 1) % size, j] +
            grid[i, (j - 1) % size]
    )

    # Energy difference due to spin flip:
    # Current energy contribution: -J * spin * neighbors - H * spin
    # After flip: -J * (-spin) * neighbors - H * (-spin) = J * spin * neighbors + H * spin
    delta_E = 2 * J * spin * neighbors + 2 * H * spin
    return delta_E


def metropolis_step(grid, T, J, H):
    """Perform one Metropolis step with an external field H."""
    size = grid.shape[0]
    for _ in range(size ** 2):
        i, j = np.random.randint(0, size, 2)
        delta_E = calculate_delta_e(grid, i, j, J, H)
        # Metropolis acceptance criterion
        if delta_E <= 0 or np.random.rand() < np.exp(-delta_E / T):
            grid[i, j] *= -1
    return grid


def magnetization(grid):
    """Calculate the magnetization of the grid allowing negative values."""
    return np.sum(grid) / grid.size


def simulate(grid_size, J, H, temps, steps_per_temp):
    """
    Simulate the Ising model by cooling from a high temperature (disordered, random spins)
    to a low temperature (ordered, spins aligned). The external field H biases the system
    towards positive magnetization at low temperatures.
    """
    # Start from a random configuration at high temperature
    grid = initialize_grid(grid_size)
    magnetizations = []

    for T in temps:
        for _ in range(steps_per_temp):
            grid = metropolis_step(grid, T, J, H)
        magnetizations.append(magnetization(grid))
    return magnetizations


grid_size = 50
J = 1
H = 0.05  # A small positive field to ensure positive alignment at low T
# Cooling: start at T=5 (highly disordered) and end at T=1 (strong order due to field)
temps = np.linspace(5, 1, 50)
steps_per_temp = 100

magnetizations = simulate(grid_size, J, H, temps, steps_per_temp)

plt.figure(figsize=(8, 6))
plt.plot(temps, magnetizations, marker="o")
plt.title("Disorder to Order with Negative Fluctuations at High T")
plt.gca().invert_xaxis()  # High T on the left, low T on the right

plt.xlabel("Temperature (T)")
plt.ylabel("Magnetization")
plt.axvline(x=2.27, color="red", linestyle="--", label="Critical Temp (~2.27 for 2D)")
plt.legend()
plt.grid(True)
plt.show()
