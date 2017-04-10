from .pyomoitemcreator import PyomoItemCreator
from pyomo.environ import Var

class PyomoVariableCreator(object):
	''' Creator for translating RP variables to Pyomo variables '''
	@staticmethod
	def create_pyomo_variables(abstract_model, set_map, variables):
		return PyomoItemCreator.create_pyomo_indexable_items(abstract_model, set_map, variables, "variable", Var)