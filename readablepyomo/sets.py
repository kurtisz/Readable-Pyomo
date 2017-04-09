from .set import Set
import pyomo.environ

NonNegativeReals = Set()
PositiveIntegers = Set()
NonNegativeIntegers = Set()
Binary = Set()

# Mapping of Readable Pyomo sets to Pyomo sets
pyomo_set_map = {
					NonNegativeReals: 		pyomo.environ.NonNegativeReals,
					PositiveIntegers: 		pyomo.environ.PositiveIntegers,
					NonNegativeIntegers: 	pyomo.environ.NonNegativeIntegers,
					Binary: 				pyomo.environ.Binary
				}