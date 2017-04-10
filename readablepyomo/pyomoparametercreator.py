from .pyomoitemcreator import PyomoItemCreator
from pyomo.environ import Param

class PyomoParameterCreator(object):
	''' Creator for translating RP parameters to Pyomo parameters '''
	@staticmethod
	def create_pyomo_parameters(abstract_model, set_map, parameters):
		PyomoItemCreator.create_pyomo_indexable_items(abstract_model, set_map, parameters, "parameter", Param)