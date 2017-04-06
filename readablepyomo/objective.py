class Objective:
	class Sense:
		MINIMIZE = 0
		MAXIMIZE = 1
		
	def __init__(self, sense, expression):
		self._sense = sense
		self._expression = expression
		
	def get_sense(self):
		return self._sense
		
	def create_func(self):
		# Model variable name pass in must match name of parameter to function
		return lambda model : eval(self._expression.create_code("model", dict()), locals())