from .evaluatable_stub import Evaluatable
from .expressions import BinaryExpression, RangeComparison

def _create_binary_expression_creator(operator):
	def _create_binary_expression(left, right):
		return BinaryExpression(left, operator, right)
	return _create_binary_expression
		
def _evaluatable_is_within(self, lower, upper):
	return RangeComparison(lower, self, upper)
		
Evaluatable.__mul__ = _create_binary_expression_creator("*")
Evaluatable.__rmul__ = Evaluatable.__mul__
Evaluatable.__add__ = _create_binary_expression_creator("+")
Evaluatable.__sub__ = _create_binary_expression_creator("-")
Evaluatable.is_within = _evaluatable_is_within
Evaluatable.is_less_than_or_equal_to = _create_binary_expression_creator("<=")
Evaluatable.is_greater_than_or_equal_to = _create_binary_expression_creator(">=")
Evaluatable.equals = _create_binary_expression_creator("==")