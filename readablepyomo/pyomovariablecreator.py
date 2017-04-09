from .pyomoitemcreator import PyomoItemCreator
from pyomo.environ import Var

class PyomoVariableCreator(object):
	@staticmethod
	def create_pyomo_variables(abstract_model, set_map, variables):
		return PyomoItemCreator.create_pyomo_indexable_items(abstract_model, set_map, variables, "variable", Var)