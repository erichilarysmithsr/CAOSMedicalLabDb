# Import the PyMOL module
import pymol

# Create a new PyMOL session
session = pymol.PyMOL()

# Load the CML file for geranyl pyrophosphate
session.load("geranyl_pyrophosphate.cml")

# Color the atoms in the molecule
session.color("yellow", "sele all")

# Display the molecule
session.show()
