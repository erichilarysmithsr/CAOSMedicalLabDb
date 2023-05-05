import math

def markovnikov_rule(alkene, reagent):
  """
  This function uses the Markovnikov's rule to predict the product of the addition of a reagent to an alkene.

  Args:
    alkene: A string representing the alkene.
    reagent: A string representing the reagent.

  Returns:
    A string representing the product of the addition reaction.
  """

  # Get the number of hydrogen atoms on each carbon atom in the alkene.
  hydrogen_atoms_on_carbon_1 = alkene.count('H')
  hydrogen_atoms_on_carbon_2 = alkene.count('H', 1)

  # Determine which carbon atom in the alkene is more substituted.
  more_substituted_carbon = hydrogen_atoms_on_carbon_1 > hydrogen_atoms_on_carbon_2

  # Add the reagent to the more substituted carbon atom in the alkene.
  product = reagent + alkene[more_substituted_carbon]

  return product

