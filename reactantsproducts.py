import numpy as np
import matplotlib.pyplot as plt

# Define the reactants and products.
reactants = ['NaHCO3', 'H3C6H5O7']
products = ['Na3C6H5O7', 'H2O', 'CO2']

# Write the balanced chemical equation.
equation = 'NaHCO3 + H3C6H5O7 <=> Na3C6H5O7 + H2O + CO2'

# Calculate the equilibrium constant.
Keq = np.exp(-(-91.05 / 8.31446261815324 * (298.15)))

# Plot the equilibrium curve.
x = np.arange(0, 1, 0.01)
y = Keq * x ** 2
plt.plot(x, y)
plt.xlabel('Concentration of NaHCO3 (mol/L)')
plt.ylabel('Concentration of CO2 (mol/L)')
plt.title('Equilibrium Curve for the Reaction of Alka-Seltzer')
plt.show()
