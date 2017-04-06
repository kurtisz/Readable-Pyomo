from .evaluatable import Evaluatable
from .util import subtract_set

_INDEX_BASE_NAME = "index"

class Expression(Evaluatable):
	pass
			
def _build_for_clause(set, model_variable_name, num_indexes, index_map):
	index_map[set] = _INDEX_BASE_NAME + str(num_indexes)
	return "for "				+	\
			index_map[set]		+	\
			" in "				+	\
			model_variable_name	+	\
			"."					+	\
			set.get_name()
	
def _concat_for_clauses(sets, model_variable_name, index_map):
	num_indexes = 0
	for_clauses = ""
	for set in sets:
		for_clauses += _build_for_clause(set, model_variable_name, num_indexes, index_map)
		num_indexes += 1
	
	return for_clauses

def sum_over(*sets):
	class SumExpression(Expression):
		def __init__(self, expression):
			self._bound_sets = list(sets)
			self._expression = expression
			
		def create_code(self, model_variable_name, index_map):
			for_clauses = _concat_for_clauses(self._bound_sets, model_variable_name, index_map)
			sum_expression = self._expression.create_code(model_variable_name, index_map)
			return "sum("			+	\
					sum_expression	+	\
					" "				+	\
					for_clauses		+	\
					")"
			
		def get_unbound_sets(self):
			return subtract_set(self._expression.get_unbound_sets(), self._bound_sets)
	
	return SumExpression