from .objective import Objective
from pyomo.environ import Objective as PyomoObjective
from pyomo.environ import minimize, maximize

class PyomoObjectiveCreator(object):
	''' Creator for translating RP objectives to Pyomo objectives '''
	@staticmethod
	def _get_pyomo_sense(sense):
		if sense == Objective.Sense.MINIMIZE:
			return minimize
		else:
			return maximize
		
	@staticmethod
	def create_pyomo_objective(abstract_model, set_map, parameter_map, variable_map, objective):
		objective_sense = PyomoObjectiveCreator._get_pyomo_sense(objective.get_sense())
		abstract_model.cost = PyomoObjective(rule = objective.create_func(), sense = objective_sense)