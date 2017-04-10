import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from readablepyomo.readablepyomo import *
from readablepyomo.glpk import Glpk

x = Variable("x").within(NonNegativeReals)
y = Variable("y").within(NonNegativeReals)
z = Variable("z").within(NonNegativeReals)

Glpk.solve(
	given(
			variables = (x, y, z)
		)											\
		.maximize(x + z)							\
		.such_that(x.is_less_than_or_equal_to(12))	\
		.such_that(y.is_less_than_or_equal_to(14))	\
		.such_that((z - y).equals(4))				\
		.such_that((2 * x - 3 * y).is_greater_than_or_equal_to(5))
		.such_that(x.is_greater_than_or_equal_to(0)) \
		.such_that(y.is_greater_than_or_equal_to(0))
		).write()