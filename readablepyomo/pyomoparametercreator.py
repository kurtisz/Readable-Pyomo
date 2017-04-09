from .pyomoitemcreator import PyomoItemCreator
from pyomo.environ import Param

class PyomoParameterCreator(object):
	@staticmethod
	def create_pyomo_parameters(abstract_model, set_map, parameters):
		PyomoItemCreator.create_pyomo_indexable_items(abstract_model, set_map, parameters, "parameter", Param)