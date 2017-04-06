from .objective import Objective

class Model:
	def __init__(self):
		self.sets = []
		self.parameters = []
		self.variables = []
		self.objective = None
		self.constraint_comparisons = []
		pass
		
	def add_sets(self, setsList):
		self.sets += setsList
		
	def add_parameters(self, parametersList):
		self.parameters += parametersList
		
	def add_variables(self, variablesList):
		self.variables += variablesList
		
	def _set_objective(self, expression, sense):
		self.objective = Objective(sense, expression)
		return self
		
	def minimize(self, expression):
		return self._set_objective(expression, Objective.Sense.MINIMIZE)
		
	def maximize(self, expression):
		return self._set_objective(expression, Objective.Sense.MAXIMIZE)
		
	def such_that(self, comparison):
		self.constraint_comparisons += [comparison]
		return self