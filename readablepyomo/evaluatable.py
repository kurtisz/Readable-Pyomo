def _create_code(item, model_variable_name = "model", index_map = dict()):
	if "create_code" in dir(item):
		return item.create_code(model_variable_name, index_map)
	else:
		return str(item)
		
def _get_unbound_sets(item):
	if "get_unbound_sets" in dir(item):
		return item.get_unbound_sets()
	else:
		return []
		
class Evaluatable:
	class BinaryExpression:
		def __init__(self, left, operation, right):
			self.left = left
			self.operation = operation
			self.right = right
			
		def create_code(self, model_variable_name = "model", index_map = dict()):
			return self.left.create_code(model_variable_name, index_map) + " " + self.operation + " " + self.right.create_code(model_variable_name, index_map)
			
		def get_unbound_sets(self):
			return _get_unbound_sets(self.left) + _get_unbound_sets(self.right)
			
	bound_sets = []

class RangeComparison(Evaluatable):
	def __init__(self, lower, expression, upper):
		self.lower = lower
		self.expression = expression
		self.upper = upper
		
	def create_code(self, model_variable_name = "model", index_map = dict()):
		return _create_code(self.lower, model_variable_name, index_map) + " <= " + self.expression.create_code(model_variable_name, index_map) + " <= " + _create_code(self.upper, model_variable_name, index_map)
			
	def get_unbound_sets(self):
		return _get_unbound_sets(self.lower) + self.expression.get_unbound_sets() + _get_unbound_sets(self.upper)
		
class UpperBoundComparison(Evaluatable):
	def __init__(self, expression, upper_bound):
		self.expression = expression
		self.upper_bound = upper_bound
		
	def create_code(self, model_variable_name = "model", index_map = dict()):
		return self.expression.create_code(model_variable_name, index_map) + " <= " + _create_code(self.upper_bound, model_variable_name, index_map)
			
	def get_unbound_sets(self):
		return self.expression.get_unbound_sets() + _get_unbound_sets(self.upper_bound)
		
class LowerBoundComparison(Evaluatable):
	def __init__(self, expression, lower_bound):
		self.expression = expression
		self.lower_bound = lower_bound
		
	def create_code(self, model_variable_name = "model", index_map = dict()):
		return self.expression.create_code(model_variable_name, index_map) + " >= " + _create_code(self.lower_bound, model_variable_name, index_map)
			
	def get_unbound_sets(self):
		return self.expression.get_unbound_sets() + _get_unbound_sets(self.lower_bound)
		
def _evaluatable_mul(self, other):
		return Evaluatable.BinaryExpression(self, "*", other)
		
def _evaluatable_is_within(self, lower, upper):
	return RangeComparison(lower, self, upper)
	
def _evaluatable_is_less_than_or_equal_to(self, upper_bound):
	return UpperBoundComparison(self, upper_bound)
	
def _evaluatable_is_greater_than_or_equal_to(self, lower_bound):
	return LowerBoundComparison(self, lower_bound)
		
Evaluatable.__mul__ = _evaluatable_mul
Evaluatable.is_within = _evaluatable_is_within
Evaluatable.is_less_than_or_equal_to = _evaluatable_is_less_than_or_equal_to
Evaluatable.is_greater_than_or_equal_to = _evaluatable_is_greater_than_or_equal_to