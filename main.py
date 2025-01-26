import numpy as np
import matplotlib.pyplot as plt
import time

# Constants
grid_size = 20  # Grid size
J = -1          # Antiferromagnetic interaction
k = 1           # Boltzmann constant
T = np.linspace(1.0, 5.0, 50)  # Temperature range
num_iterations = 10000         # Iterations per temperature
grid = np.random.choice([-1, 1], (grid_size, grid_size))  # Initialize random spins

# Staggered weight matrix for staggered magnetization
checkerboard = np.fromfunction(lambda i, j: (-1)**(i + j), grid.shape)

# Simulation
staggered_magnetizations = []

start_time = time.time()
for temp in T:
    beta = 1 / (k * temp)
    staggered_magnetization = []  # Track staggered magnetization for this temperature

    for _ in range(num_iterations):
        # Randomly select a spin to flip
        i, j = np.random.randint(0, grid_size, size=2)
        current_spin = grid[i, j]

        # Calculate the change in energy
        neighbors = (
            grid[(i + 1) % grid_size, j]
            + grid[(i - 1) % grid_size, j]
            + grid[i, (j + 1) % grid_size]
            + grid[i, (j - 1) % grid_size]
        )
        delta_energy = 2 * J * current_spin * neighbors

        # Decide whether to flip the spin
        if delta_energy < 0 or np.random.rand() < np.exp(-delta_energy * beta):
            grid[i, j] *= -1

        # Calculate staggered magnetization
        staggered_magnetization.append(
            np.abs(np.sum(grid * checkerboard)) / (grid_size ** 2)
        )

    # Average staggered magnetization for this temperature
    staggered_magnetizations.append(np.mean(staggered_magnetization))

end_time = time.time()
print("Simulation completed in", end_time - start_time, "seconds")

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(T, staggered_magnetizations, marker='o', label="Staggered Magnetization")
plt.axvline(x=2.27, color='red', linestyle='--', label="Critical Temp (~2.27 for 2D)")
plt.title("Staggered Magnetization vs Temperature")
plt.xlabel("Temperature (T)")
plt.ylabel("Staggered Magnetization")
plt.legend()
plt.grid(True)
plt.show()
