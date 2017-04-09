from pyomo.environ import Set
from .sets import pyomo_set_map
from .pyomoitemcreator import PyomoItemCreator

class PyomoSetCreator(object):
	@staticmethod
	def create_pyomo_sets(abstract_model, sets):
		set_map = pyomo_set_map
		for i in range(len(sets)):
			pyomo_set_creator = lambda set : Set()
			set_map[sets[i]] = PyomoItemCreator.create_and_set_abstract_model_indexed_property_item(abstract_model, sets[i], "set", i, pyomo_set_creator, None)
		return set_map