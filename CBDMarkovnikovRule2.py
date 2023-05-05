import math

def markovnikov_rule(alkene, reagent):
  """
  This function uses Markovnikov's rule to predict the product of the addition of an unsymmetrical reagent to an unsymmetrical alkene.

  Args:
    alkene: A string representing the alkene.
    reagent: A string representing the reagent.

  Returns:
    A string representing the product of the addition reaction.
  """

  # Get the number of hydrogen atoms on each carbon atom in the alkene.
  hydrogen_atoms_on_carbon_1 = alkene.count('H')
  hydrogen_atoms_on_carbon_2 = alkene.count('H', alkene.find('C') + 1)

  # Determine which carbon atom in the alkene will receive the hydrogen atom from the reagent.
  if hydrogen_atoms_on_carbon_1 > hydrogen_atoms_on_carbon_2:
    carbon_atom_1 = 'more_substituted'
  else:
    carbon_atom_1 = 'less_substituted'

  # Add the hydrogen atom from the reagent to the carbon atom in the alkene.
  product = alkene.replace('C' + carbon_atom_1, 'CH' + carbon_atom_1)

  # Add the rest of the reagent to the product.
  product += reagent

  return product

def main():
  # Get the alkene and reagent from the user.
  alkene = input('Enter the alkene: ')
  reagent = input('Enter the reagent: ')

  # Print the product of the addition reaction.
  print(markovnikov_rule(alkene, reagent))

if __name__ == '__main__':
  main()
