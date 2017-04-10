from .derived import Derived
from .evaluatable_stub import Evaluatable
from .util import subtract_set, to_list
from .rp_util import _create_code, _get_unbound_sets

_INDEX_BASE_NAME = "index"

class Expression(Evaluatable):
	pass
	
class SumExpression(Expression):
	def __init__(self, expression, *sets):
		self._bound_sets = to_list(*sets)
		self._expression = expression
	
	@staticmethod
	def _build_for_clause(set, model_variable_name, num_indexes, index_map):
		index_map[set] = _INDEX_BASE_NAME + str(num_indexes)
		return "for "				+	\
				index_map[set]		+	\
				" in "				+	\
				model_variable_name	+	\
				"."					+	\
				set.get_name()

	def _concat_for_clauses(self, model_variable_name, index_map):
		num_indexes = len(index_map)
		for_clauses = ""
		for set in self._bound_sets:
			for_clauses += SumExpression._build_for_clause(set, model_variable_name, num_indexes, index_map)
			num_indexes += 1
		
		return for_clauses
		
	def create_code(self, model_variable_name, index_map):
		for_clauses = self._concat_for_clauses(model_variable_name, index_map)
		sum_expression = _create_code(self._expression, model_variable_name, index_map)
		return "sum("			+	\
				sum_expression	+	\
				" "				+	\
				for_clauses		+	\
				")"
		
	def get_unbound_sets(self):
		return subtract_set(_get_unbound_sets(self._expression), self._bound_sets)

def sum_over(*sets):
	def create_sum_expression(expression):
		return SumExpression(expression, *sets)
	return create_sum_expression
	
class BinaryExpression(Evaluatable):
	def __init__(self, left, operation, right):
		self.left = left
		self.operation = operation
		self.right = right
		
	def create_code(self, model_variable_name, index_map):
		return _create_code(self.left, model_variable_name, index_map) + " " + self.operation + " " + _create_code(self.right, model_variable_name, index_map)
		
	def get_unbound_sets(self):
		return _get_unbound_sets(self.left) + _get_unbound_sets(self.right)

class RangeComparison(Evaluatable):
	def __init__(self, lower, expression, upper):
		self.lower = lower
		self.expression = expression
		self.upper = upper
		
	def create_code(self, model_variable_name, index_map):
		return _create_code(self.lower, model_variable_name, index_map) + " <= " + _create_code(self.expression, model_variable_name, index_map) + " <= " + _create_code(self.upper, model_variable_name, index_map)
			
	def get_unbound_sets(self):
		return _get_unbound_sets(self.lower) + self.expression.get_unbound_sets() + _get_unbound_sets(self.upper)