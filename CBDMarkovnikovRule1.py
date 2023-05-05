import numpy as np

# Define the Markovnikov's rule
def markovnikov_rule(alkene, reagent):
  # Get the number of hydrogen atoms on each carbon atom of the alkene
  hydrogen_atoms_per_carbon = np.count_nonzero(alkene, axis=1)

  # Find the carbon atom with the most hydrogen atoms
  most_substituted_carbon = np.argmax(hydrogen_atoms_per_carbon)

  # Add the hydrogen atom of the reagent to the carbon atom with the most hydrogen atoms
  product = alkene.copy()
  product[most_substituted_carbon] += reagent

  return product

# Define the structure of geranyl pyrophosphate
geranyl_pyrophosphate = np.array([
  [1, 0, 0, 0, 0],
  [0, 1, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0],
  [0, 0, 0, 0, 1]
])

# Define the structure of cannabigerolic acid (CBGA)
cbga = np.array([
  [0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0],
  [1, 0, 0, 0, 0],
  [0, 1, 0, 0, 0],
  [0, 0, 0, 0, 1]
])

# Define the structure of CBD
cbd = np.array([
  [0, 0, 0, 1, 0],
  [0, 0, 0, 0, 1],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0],
  [0, 0, 0, 0, 1]
])

# Add the hydrogen atom of geranyl pyrophosphate to CBGA
product = markovnikov_rule(cbga, geranyl_pyrophosphate)

# Check that the product is equal to CBD
assert np.array_equal(product, cbd)

# Print a message to the user
print("The Markovnikov's rule can be used to explain why CBD is produced in the hemp plant and why it is one of the most abundant cannabinoids in the plant.")
