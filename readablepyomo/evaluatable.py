from .evaluatable_stub import Evaluatable
from .expressions import BinaryExpression, RangeComparison, UpperBoundComparison, LowerBoundComparison, EqualityComparison
		
def _evaluatable_mul(self, other):
	return BinaryExpression(self, "*", other)

def _evaluatable_add(self, other):
	return BinaryExpression(self, "+", other)

def _evaluatable_sub(self, other):
	return BinaryExpression(self, "-", other)
		
def _evaluatable_is_within(self, lower, upper):
	return RangeComparison(lower, self, upper)
	
def _evaluatable_is_less_than_or_equal_to(self, upper_bound):
	return UpperBoundComparison(self, upper_bound)
	
def _evaluatable_is_greater_than_or_equal_to(self, lower_bound):
	return LowerBoundComparison(self, lower_bound)
	
def _evaluatable_equals(self, value):
	return EqualityComparison(self, value)
		
Evaluatable.__mul__ = _evaluatable_mul
Evaluatable.__rmul__ = _evaluatable_mul
Evaluatable.__add__ = _evaluatable_add
Evaluatable.__sub__ = _evaluatable_sub
Evaluatable.is_within = _evaluatable_is_within
Evaluatable.is_less_than_or_equal_to = _evaluatable_is_less_than_or_equal_to
Evaluatable.is_greater_than_or_equal_to = _evaluatable_is_greater_than_or_equal_to
Evaluatable.equals = _evaluatable_equals