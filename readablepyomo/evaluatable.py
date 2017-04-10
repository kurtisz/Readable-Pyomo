from .evaluatable_stub import Evaluatable
from .expressions import BinaryExpression, RangeComparison
		
def _evaluatable_is_within(self, lower, upper):
	return RangeComparison(lower, self, upper)
		
Evaluatable.__mul__ = BinaryExpression.create_binary_expression_creator("*")
Evaluatable.__rmul__ = Evaluatable.__mul__
Evaluatable.__add__ = BinaryExpression.create_binary_expression_creator("+")
Evaluatable.__sub__ = BinaryExpression.create_binary_expression_creator("-")
Evaluatable.is_within = _evaluatable_is_within
Evaluatable.is_less_than_or_equal_to = BinaryExpression.create_binary_expression_creator("<=")
Evaluatable.is_greater_than_or_equal_to = BinaryExpression.create_binary_expression_creator(">=")
Evaluatable.equals = BinaryExpression.create_binary_expression_creator("==")