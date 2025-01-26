# Computational Simulation of an Order-Disorder Phase Transition

## Project Overview
This project (size of 7 people) presents a computational simulation of a **2D Ising model** to study **order-disorder phase transitions** in a magnetic system. The model aims to explore how thermal fluctuations influence spin alignment and phase transitions, using **Monte Carlo methods** to simulate different temperature scenarios.

## Simulation Details

### Order-to-Disorder Transition
At **low temperatures**, spins align in an antiferromagnetic order, forming a checkerboard pattern to minimize energy. As temperature increases, thermal fluctuations disrupt this order, leading to random spin distribution and a disordered state.

Key observations:
- **Low temperatures:** Spins align with near-zero magnetization.
- **Critical temperature (T_c):** Sharp transition from order to disorder.
- **High temperatures:** Random spin orientation with zero net magnetization.

### Disorder-to-Order Transition
The system transitions from a disordered to an ordered phase as temperature decreases. Key characteristics include:
- Spins becoming more aligned below the critical temperature.
- Magnetization sharply increasing as order is restored.

### Monte Carlo Experiment
Monte Carlo methods are used to estimate system states by random sampling. In this project, we implemented a Monte Carlo simulation with:
- **10,000 steps per temperature value.**
- **Averaged measurements over the last 2,000 steps** to minimize fluctuations.
- The inclusion of an **external bias (h = 0.1)** to analyze equilibrium magnetization shifts.

### Ising Model and Phase Transitions
The Ising model is widely used in statistical physics to simulate ferromagnetic behavior in materials. It helps study:
- **Critical phenomena** near phase transition temperatures.
- **Energy changes, specific heat peaks, and susceptibility** across temperature variations.

## Files Included
- `main.py` - Main script for running the Ising model simulation.
- `magnetization_vs_temp_plot.py` - Script for generating magnetization plots.
- `Final Report.pdf` - Detailed report of the project's objectives, methodology, and findings.
- `plot.png` - Visualization of phase transition behaviors.

## Results
The simulation successfully demonstrates phase transitions with the following observations:
- At temperatures below **T_c ≈ 2.31**, the system maintains an ordered state.
- Near the critical temperature, magnetization sharply declines.
- Above the critical point, disorder dominates with minimal magnetization.

## Final Report Preview

Here is a preview of the final report:

![Final Report Screenshot](final%20report.png)
